Overview
Connection Details
GRVT's services are hosted in AWS Tokyo (ap-northeast-1).

For close partners with high trading volumes, we offer AWS PrivateLink.

Authentication
GRVT supports API Authentication via session cookies, and API keys.

You may follow the below steps to authenticate your requests.

This section is conveniently inlined at every authenticated endpoint for your convenience.

Authentication
In order to authenticate, you must first provision a valid API key. API keys can be provisioned via the GRVT UI.

# These are the variables you will need to set manually
GRVT_API_KEY="<insert_key_here>"
GRVT_SUB_ACCOUNT_ID="<insert_sub_account_id_here>"
Then, choose the environment you want to authenticate against.

# dev
GRVT_AUTH_ENDPOINT="https://edge.dev.gravitymarkets.io/auth/api_key/login"
# staging
GRVT_AUTH_ENDPOINT="https://edge.staging.gravitymarkets.io/auth/api_key/login"
# testnet
GRVT_AUTH_ENDPOINT="https://edge.testnet.grvt.io/auth/api_key/login"
# prod
GRVT_AUTH_ENDPOINT="https://edge.grvt.io/auth/api_key/login"
Now, let’s authenticate and retrieve both the session cookie and the X-Grvt-Account-Id header value that you’ll need to access any endpoints requiring authentication.

echo $GRVT_API_KEY
echo $GRVT_SUB_ACCOUNT_ID
echo $GRVT_AUTH_ENDPOINT

RESPONSE=$(
    curl $GRVT_AUTH_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Cookie: rm=true;' \
        -d '{"api_key": "'$GRVT_API_KEY'"}' \
        -s -i
)

GRVT_COOKIE=$(echo "$RESPONSE" | grep -i 'set-cookie:' | grep -o 'gravity=[^;]*')
GRVT_ACCOUNT_ID=$(echo "$RESPONSE" | grep 'x-grvt-account-id:' | awk '{print $2}' | tr -d '\r')

echo "$GRVT_COOKIE"
echo "$GRVT_ACCOUNT_ID"
Order Creation
Python SDK
We have a Python SDK available for usage. (link)


pip install grvt-pysdk
Step-by-Step Guide
For specific information on how to sign and create an order, here's a step-by-step guide, using our Python SDK:

Step 8-1: Fetch All Instruments
Step 8-2: Use Instrument Map in Order Signing
Step 8-3: Create An Order
Step 8-4: Sign Order
Step 8-5: Submit The Order
Chain IDs
Network	Ethereum L1 Chain ID	GRVT L2 Chain ID
Sepolia (Dev)	11155111	327
Sepolia (Stg)	11155111	327
Sepolia (Testnet)	11155111	326
Mainnet	1	325
Encoding (Full vs Lite)
For more versatile usage, all our APIs and Websockets are offered in full and lite variants.

These variants are identical except for the JSON field_name used:

`full` uses the full field name, e.g. `order_id`
`lite` uses the shortened field name, e.g. `oi`
This is allows for users to trade off between simplicity and performance.

WebSocket Subscription
Connecting to Authenticated Endpoints
To subscribe to authenticated WebSocket streams (e.g., trade-related feeds), you must establish a WebSocket connection with both your GRVT_COOKIE and X-Grvt-Account-Id included. If your WebSocket client supports custom headers, set both as headers during the initial handshake. If custom headers are not supported, append x_grvt_account_id as a query parameter to the endpoint URL.

Example (With Custom Headers):
wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
-H "Cookie: $GRVT_COOKIE" \
-H "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID"
Example (Without Custom Headers):
wscat -c "wss://trades.dev.gravitymarkets.io/ws/full?x_grvt_account_id=$GRVT_ACCOUNT_ID" \
-H "Cookie: $GRVT_COOKIE"
Full examples are available in the Try it out section of any Trading Websocket endpoint.

In either case, once connected, you can send authenticated requests (e.g., subscribe) and interact with trade-related streams.

Request
Websocket subscriptions are initiated by sending a JSON RPC Request to the server.

They have the following structure:

stream: The stream to subscribe to
feed: The list of feeds to subscribe to
method: The JSONRPC method. This is always `"subscribe"`
is_full: Whether to subscribe to the `full` or `lite` feed.
{
    "stream":"v1.book.s",
    "feed":["BTC_USDT_Perp@500-100-10"],
    "method":"subscribe",
    "is_full":true
}
Response
Upon subscribing, the server will respond with an initial JSON RPC Response.

In the successful case, the following response will be returned:

stream: The stream that was subscribed to
subs: The list of subscriptions that were successfully subscribed to
unsubs: The list of subscriptions that were unsubscribed from
{
    "stream":"v1.book.s",
    "subs":["BTC_USDT_Perp@500-100-10"],
    "unsubs":[]
}
In the case of an error, the following response will be returned:

code: The error code
message: The error message
status: The HTTP status code
{
    "code":3001,
    "message":"Stream handler not found",
    "status":400
}
Feed Structure
For each WebSocket stream, users may subscribe to multiple feeds. Each stream defines its own feed structure, which is documented on the relevant page. However, they all share the same underlying structure.

Firstly, feeds are broken down into primary@secondary selector pairs.

`primary` is used to determine the type of streaming data received.
`secondary` is used to determine the format/subtype of the streaming data received.
When subscribing to the same primary selector again, the previous secondary selector will be replaced.

eg. If previously subcribing to "BTC_USDT_Perp@500-100-10" and then subscribing to "BTC_USDT_Perp@500-1-10", the subscribe response will return.

{
    "stream":"v1.book.s",
    "subs":["BTC_USDT_Perp@500-1-10"],
    "unsubs":["BTC_USDT_Perp@500-100-10"]
}
Within each primary or secondary selector, fields are separated by -, and ordered by the schema definition.

Feed Data Stream
The feed data stream will return a continuous stream of JSON objects. It has the following structure:

stream: The stream that the data is from
selector: The selector that the data is from
sequence_number: This increases by one for each feed object published in the `stream`/`selector` pair. If the number `jumps`, it indicates data loss.
feed: The feed data object. Different for each stream.
{
    "stream": "v1.book.s",
    "selector": "BTC_USDT_Perp@500-100-10",
    "sequence_number": "872634876",
    "feed": {}
}
Event Time
All feed data is published with an event_time timestamp (in unix nanoseconds). This timestamp is stamped by our core cluster, and is guaranteed to be consistent across all services and nodes. For All Streams, other than MiniTicker raw streams, event time is a globally consistent unique identifier for a message. ie. All connections via WebSocket/REST can agree that a message is the same via its event_time.

Sequence Number
Sequence Numbers are stamped at the gateway level. Which means that it only has relevance within a single websocket connection, and nothing more. It helps you to guarantee that you received the right number of snapshot updates, and did not miss any delta updates.

All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas
Num snapshots returned in JSON RPC Response (per stream): You can ensure that you received the right number of snapshots
First sequence number returned in JSON RPC Response (per stream): You can ensure that you received the first stream, without gaps from snapshots
Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect
Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.
 Back to top
Made with Material for MkDocs




Learn
INTRODUCTION
Getting Started
Performance meetssafety and privacy

GRVT is a custodial centralized exchange powered by ZK(zero knowledge) technology. We are first official Appchain on zkSync's Hyperchain and received an investment from Matter Labs, the creators of zkSync.

Testnet

https://testnet.grvt.io/

Mainnet

https://grvt.io/

Architecture Overview
GRVT's hybrid exchange architecture overview

GRVT adopts a hybrid architecture that matches and stores data off chain and provides smart contract level guarantees of their execution on chain. GRVT adopted this architecture to improve throughput by processing transactions off the Ethereum Mainnet.

Architecture Overview

Offchain
All user actions are initially processed off-chain by GRVT servers. Only actions impacting user funds, such as trades or account creation, are eventually pushed on-chain by GRVT. Non-fund-related actions, like KYC, remain off-chain. The GRVT servers forward relevant user actions to the GRVT chain. Key user actions that are pushed on-chain include transactions processed by the following:

Matching Engine: Orders that are matched by the matching engine are sent on-chain
Risk Engine: Liquidations are sent to the chain
Account Management: Creation of entities such as trading accounts or addition of wallets that can use funds
Fund Management: Internal and external transfer of funds
Onchain
A subset of the off chain actions are pushed to the GRVT chain. These actions are then published as zero-knowledge proofs to verify off-chain transactions on Ethereum.

Trade Settlement: Matched orders are settled on chain
Risk Engine Validation: Liquidations are validated on chain as being fair based on smart contract logic
Account Management Validations: Account Management actions are validated on chain
Fund Management: Fund transfers are validated and settled on chain
GRVT Native Deposit Contracts
GRVTBridgeProxy
Contract address used for depositing native tokens:
0xE17aeD2fC55f4A876315376ffA49FE6358113a65

L1NativeTokenVault
Contract that holds the deposited funds:
0xbed1eb542f9a5aa6419ff3deb921a372681111f6

When you deposit native tokens through GRVT, you’ll interact with GRVTBridgeProxy, while your assets will ultimately be stored in the L1NativeTokenVault.

CORE CONCEPTS
Accounts and Users
Funding Account
Funding accounts are the highest level on-chain identity in GRVT. The purpose of the funding account is primarily fund management. They process deposits, withdrawals, external Transfers to other funding accounts and internal transfers to linked trading accounts.

Trading Account
Each funding account can link to multiple trading accounts. To trade derivatives, you must transfer funds from your funding account to a specific trading account.

Accounts and Users

Users
In the case of individual accounts, each account has a maximum of one user. The user has access to all the linked trading accounts.

In the case of business accounts, each account can have one or more users. User can have accessto the funding account and/or trading trading accounts separately depending on their permissions.

User Identifiers
One User, One Email, One Wallet

User Identifiers

In GRVT, each user must register both Web2 and Web3 credentials.

Web2 Credentials (Emails)

Each user must sign up via email with a password setup or Google/Microsoft OAuth. This grants access to non-trading features such as completing your KYC, referrals, and more. It also allows you to view your portfolio and positions.

Web3 Credentials (Wallets)

Each user must then register a wallet on GRVT to enable trading features. Only trades signed with registered wallets can be executed by our trading engine. Additionally, actions that affect the ownership of your assets, such as trading, require a registered wallet.

Credential Type	Identifier (Sample)	Secret	Use Case
Web2	email (e.g., wagmi@gmail.com)	password/OAuth	Read + Write (No Trading)
Web3	public key (e.g., 0xb794f5ea0ba39494ce839613fffba74279579268)	private key	Own, Sign Trades
Account Identifiers
The on-chain Funding AccountID matches the wallet address that created the account. Business accounts can have multiple users, each with their own wallet linked to the funding account.

Individual Account Representation
Individual Account

Business Account Representation
Business Account

Funding Account Off-Chain Representation (Read + Write)
Off-Chain accountIDs	Off chain user email addresses
ACC:2aO9cE9kJkah16urpA7DQKPOEdx	john@gmail.com
ACC:2aO9cE9kJkah16urpA7DQKPOFxk	chris@outlook.com
ACC:2aO9cE9kJkah16urajkDQKPOEdx	neil@firma.io, bruce@firma.io
Funding Account On-Chain Representation (Own)
On-Chain accountIDs	On-Chain user wallets
0xb794f5ea0ba39494ce839613fffba74279579268	0xb794f5ea0ba39494ce839613fffba74279579268
0xdB055877e6c13b6A6B25aBcAA29B393777dD0a73	0xdB055877e6c13b6A6B25aBcAA29B393777dD0a73
0x40b38765696e3d5d8d9d834d8aad4bb6e418e489	0x40b38765696e3d5d8d9d834d8aad4bb6e418e489, 0xe92d1a43df510f82c66382592a047d288f85226f
API Keys
API keys for programmatic trading

API Keys are only registered at Trading Account level with trade only permissions. Each API key needs to be tagged to a valid Ethereum public address.

How to authenticate using API keys?
You will receive a session token by authenticating against your API key. This session token must be used then used in your read and write requests.
How to authorize transactions using API keys?
Each API key must be tagged to a valid Ethereum address. There are two ways of doing so
Input (Secure): You possess a public/private key pair. You provide the public address, while only you have access to the secret private key.
Generate (Convenient): The GRVT front-end client generates a public/private key pair in your browser and allows you to copy the secret private key. GRVT does not store the private key after it is generated.
The Secret Private key must be used to sign orders using EIP-712 signing method.
API keys 1

Mapping of API Keys to Trading Accounts
API keys 2

Learn more: Video Explanation

PBAC for Business Accounts
Permission Based Access Control for Business Accounts

Funding Account Permissions
There are four permissions on a Business funding account. Only those with a Funding Admin role are able to assign permissions to others.

Permission	Permissions
Funding Admin	
Highest permission in the exchange, that supersedes all other permissions
Can create Trading Accounts
Can trigger actions need to meet a multi-signature threshold like adding users to funding account, or adding a withdrawal/transfer address
Internal Transfer	
Can transfer funds from the Funding Account to associated Trading Accounts
External Transfer	
Can transfer funds to other funding accounts within GRVT if these accounts are in the transfer address book
Withdrawal	
Can withdraw funds to pre-approved Layer 1 wallets
Trading Account Permissions
Permission	Access
Trading Admin	
Can add users to their Trading Accounts.
Inherits "Trade" and "Transfer" permissions
Trade	
Can trade from the given Trading Account
Transfer	Can internally transfer funds to Funding Account or other trading accounts within the same Business Account
PBAC for Business Accounts
Visual Representation of Permission Based Access Control for Business Accounts
Multi-signature Admin Operations
Multi-signature operations for Business Account

Privileged operations on the Business Funding Account, like onboarding new users or adding withdrawal wallets, require multi-signature approvals. Only those with the Funding Admin roles are authorized to approve these actions.

Funding Admin can set custom thresholds, such as ⅔ (indicating two out of three Admins must sign off on the action) for these approvals.

Admin Operations
Adding/editing permissions of users the Funding Account
Setting a new multi-sig threshold
Adding/Removing eligible wallets in the Withdrawal Address Book for withdrawals
Adding/Removing funding account addresses in the Transfer Address Book for external transfers
Admin Operations

HELP CENTER
Contact Support



API Setup Guide
A short and simple API Setup guide to get you rolling quick!
It assumes bare minimum knowledge about GRVT. So anyone can get through these steps. (ideally!)

Step 1: Create Web2 Account
Link: https://testnet.grvt.io/exchange/sign-up

create account

Follow the instructions to create your Personal Or Business Account.

Step 2: Create Wallet
create wallet create wallet

Follow the instructions to link your wallet to GRVT. You may link any of your existing wallets, or create a convenient web wallet on GRVT.

Step 3: Create Web3 Accounts
GRVT has a two tier account structure.

Funding (main) Account: Used to bridge funds in and out of GRVT, acts as an administrative layer.
Trading (sub) Account: Used for derivative trading.
create wallet

Follow the instructions to complete the setup.

You have to sign on-chain to create your accounts, since this is the way we protect your self-custody.

Step 4: Mint Tokens & Transfer
In testnet, we give you a convenient way to mint tokens, so that you can get up and testing quicker.
Please remember to mint sufficient funds, and transfer some to your trading accounts.
You may always revisit this link https://testnet.grvt.io/exchange/deposit to get more.

mint

Step 5: Create API Key
Finally we are getting to the heart of things!
Create an API Key at this site https://testnet.grvt.io/exchange/account/api-keys.

Create API Key Create API Key Create API Key

Step 6: API Docs Auth
Authentication
In order to authenticate, you must first provision a valid API key. API keys can be provisioned via the GRVT UI.

# These are the variables you will need to set manually
GRVT_API_KEY="<insert_key_here>"
GRVT_SUB_ACCOUNT_ID="<insert_sub_account_id_here>"
Then, choose the environment you want to authenticate against.

# dev
GRVT_AUTH_ENDPOINT="https://edge.dev.gravitymarkets.io/auth/api_key/login"
# staging
GRVT_AUTH_ENDPOINT="https://edge.staging.gravitymarkets.io/auth/api_key/login"
# testnet
GRVT_AUTH_ENDPOINT="https://edge.testnet.grvt.io/auth/api_key/login"
# prod
GRVT_AUTH_ENDPOINT="https://edge.grvt.io/auth/api_key/login"
Now, let’s authenticate and retrieve both the session cookie and the X-Grvt-Account-Id header value that you’ll need to access any endpoints requiring authentication.

echo $GRVT_API_KEY
echo $GRVT_SUB_ACCOUNT_ID
echo $GRVT_AUTH_ENDPOINT

RESPONSE=$(
    curl $GRVT_AUTH_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Cookie: rm=true;' \
        -d '{"api_key": "'$GRVT_API_KEY'"}' \
        -s -i
)

GRVT_COOKIE=$(echo "$RESPONSE" | grep -i 'set-cookie:' | grep -o 'gravity=[^;]*')
GRVT_ACCOUNT_ID=$(echo "$RESPONSE" | grep 'x-grvt-account-id:' | awk '{print $2}' | tr -d '\r')

echo "$GRVT_COOKIE"
echo "$GRVT_ACCOUNT_ID"
The above section is inlined at every authenticated RPC & WS.

Follow the instructions to authenticate using your API Key.

Step 7: API Docs (Try It Out)
At every part of our API Docs, there's a working example you may use to test things out. You should be all set now! But don't hesitate to contact our team if you need any further help!

Try It Out!

Step 8: Order Creation
This is the most frequently asked question.

Python SDK
We have a Python SDK available for usage. (link)


pip install grvt-pysdk
Step-by-Step Guide
For specific information on how to sign and create an order, here's a step-by-step guide, using our Python SDK:

Step 8-1: Fetch All Instruments
Step 8-2: Use Instrument Map in Order Signing
Step 8-3: Create An Order
Step 8-4: Sign Order
Step 8-5: Submit The Order
Chain IDs
Network	Ethereum L1 Chain ID	GRVT L2 Chain ID
Sepolia (Dev)	11155111	327
Sepolia (Stg)	11155111	327
Sepolia (Testnet)	11155111	326
Mainnet	1	325



MarketData APIs
All requests should be made using the POST HTTP method.

Instrument
Get Instrument
FULL ENDPOINT: full/v1/instrument
LITE ENDPOINT: lite/v1/instrument

Request
Response
Errors
Try it out
ApiGetInstrumentRequest

Fetch a single instrument by supplying the asset or instrument name

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
Query

Full Request


{
    "instrument": "BTC_USDT_Perp"
}
Lite Request

{
    "i": "BTC_USDT_Perp"
}

Get All Instruments
FULL ENDPOINT: full/v1/all_instruments
LITE ENDPOINT: lite/v1/all_instruments

Request
Response
Errors
Try it out
ApiGetAllInstrumentsRequest

Fetch all instruments

Name
Lite	Type	Required
Default	Description
is_active
ia	boolean	False
false	Fetch only active instruments
Query

Full Request


{
    "is_active": true
}
Lite Request

{
    "ia": true
}

Get Filtered Instruments
FULL ENDPOINT: full/v1/instruments
LITE ENDPOINT: lite/v1/instruments

Request
Response
Errors
Try it out
ApiGetFilteredInstrumentsRequest

Fetch a list of instruments based on the filters provided

Name
Lite	Type	Required
Default	Description
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
is_active
ia	boolean	False
false	Request for active instruments only
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 100000
Kind
Query

Full Request


{
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"],
    "is_active": true,
    "limit": 500
}
Lite Request

{
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"],
    "ia": true,
    "l": 500
}

Get Currency
FULL ENDPOINT: full/v1/currency
LITE ENDPOINT: lite/v1/currency

Request
Response
Errors
Try it out
ApiGetCurrencyRequest

Fetch all currencies

Name
Lite	Type	Required
Default	Description
Query

Full Request


{
}
Lite Request

{
}

Get Margin Rules
FULL ENDPOINT: full/v1/margin_rules
LITE ENDPOINT: lite/v1/margin_rules

Request
Response
Errors
Try it out
ApiGetMarginRulesRequest

API request payload to get margin rules for a particular instrument

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The instrument to query margin rules for
Query

Full Request


{
    "instrument": "BTC_USDT_Perp"
}
Lite Request

{
    "i": "BTC_USDT_Perp"
}

Ticker
Mini Ticker
FULL ENDPOINT: full/v1/mini
LITE ENDPOINT: lite/v1/mini

Request
Response
Errors
Try it out
ApiMiniTickerRequest

Retrieves a single mini ticker value for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more performant, and useful.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
Query

Full Request


{
    "instrument": "BTC_USDT_Perp"
}
Lite Request

{
    "i": "BTC_USDT_Perp"
}

Ticker
FULL ENDPOINT: full/v1/ticker
LITE ENDPOINT: lite/v1/ticker

Request
Response
Errors
Try it out
ApiTickerRequest

Retrieves a single ticker value for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more performant, and useful.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
Query

Full Request


{
    "instrument": "BTC_USDT_Perp"
}
Lite Request

{
    "i": "BTC_USDT_Perp"
}

Orderbook
Orderbook Levels
FULL ENDPOINT: full/v1/book
LITE ENDPOINT: lite/v1/book

Request
Response
Errors
Try it out
ApiOrderbookLevelsRequest

Retrieves aggregated price depth for a single instrument, with a maximum depth of 10 levels. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
depth
d	integer	True	Depth of the order book to be retrieved (10, 50, 100, 500)
Query

Full Request


{
    "instrument": "BTC_USDT_Perp",
    "depth": 50
}
Lite Request

{
    "i": "BTC_USDT_Perp",
    "d": 50
}

Trade
Trade
FULL ENDPOINT: full/v1/trade
LITE ENDPOINT: lite/v1/trade

Request
Response
Errors
Try it out
ApiTradeRequest

Retrieves up to 1000 of the most recent trades in any given instrument. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.
This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
limit
l	integer	True	The limit to query for. Defaults to 500; Max 1000
Query

Full Request


{
    "instrument": "BTC_USDT_Perp",
    "limit": 500
}
Lite Request

{
    "i": "BTC_USDT_Perp",
    "l": 500
}

Trade History
FULL ENDPOINT: full/v1/trade_history
LITE ENDPOINT: lite/v1/trade_history

Request
Response
Errors
Try it out
ApiTradeHistoryRequest

Perform historical lookup of public trades in any given instrument.
This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.
Only data from the last three months will be retained.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
start_time
st	string	False
0	The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned
end_time
et	string	False
now()	The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
Query

Full Request


{
    "instrument": "BTC_USDT_Perp",
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "i": "BTC_USDT_Perp",
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}

Candlestick
Candlestick
FULL ENDPOINT: full/v1/kline
LITE ENDPOINT: lite/v1/kline

Request
Response
Errors
Try it out
ApiCandlestickRequest

Kline/Candlestick bars for an instrument. Klines are uniquely identified by their instrument, type, interval, and open time.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
interval
i1	CandlestickInterval	True	The interval of each candlestick
type
t	CandlestickType	True	The type of candlestick data to retrieve
start_time
st	string	False
0	Start time of kline data in unix nanoseconds
end_time
et	string	False
now()	End time of kline data in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
CandlestickInterval
CandlestickType
Query

Full Request


{
    "instrument": "BTC_USDT_Perp",
    "interval": "CI_1_M",
    "type": "TRADE",
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "i": "BTC_USDT_Perp",
    "i1": "CI_1_M",
    "t": "TRADE",
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}

Settlement
Funding Rate
FULL ENDPOINT: full/v1/funding
LITE ENDPOINT: lite/v1/funding

Request
Response
Errors
Try it out
ApiFundingRateRequest

Lookup the historical funding rate of a perpetual future.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
start_time
st	string	False
0	Start time of funding rate in unix nanoseconds
end_time
et	string	False
now()	End time of funding rate in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
agg_type
at	FundingRateAggregationType	False
'FUNDING_INTERVAL'	Aggregation method for historical funding rate observations. Defaults to using the instrument-specific funding interval.
FundingRateAggregationType


MarketData Websocket Streams
Ticker
Mini Ticker Snap
STREAM: v1.mini.s

Feed Selector
Feed Data
Errors
Try it out
WSMiniTickerFeedSelectorV1

Subscribes to a mini ticker feed for a single instrument. The mini.s channel offers simpler integration. To experience higher publishing rates, please use the mini.d channel.
Unlike the mini.d channel which publishes an initial snapshot, then only streams deltas after, the mini.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of the mini ticker.
After the snapshot, the server will only send deltas of the mini ticker.
The server will send a delta if any of the fields in the mini ticker have changed.


Field Semantics:
[DeltaOnly] If a field is not updated, {}
If a field is updated, {field: '123'}
If a field is set to zero, {field: '0'}
If a field is set to null, {field: ''}

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (0 - raw, 50, 100, 200, 500, 1000, 5000)
Snapshot (200, 500, 1000, 5000)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.mini.s",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.mini.s",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Mini Ticker Delta
STREAM: v1.mini.d

Feed Selector
Feed Data
Errors
Try it out
WSMiniTickerFeedSelectorV1

Subscribes to a mini ticker feed for a single instrument. The mini.s channel offers simpler integration. To experience higher publishing rates, please use the mini.d channel.
Unlike the mini.d channel which publishes an initial snapshot, then only streams deltas after, the mini.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of the mini ticker.
After the snapshot, the server will only send deltas of the mini ticker.
The server will send a delta if any of the fields in the mini ticker have changed.


Field Semantics:
[DeltaOnly] If a field is not updated, {}
If a field is updated, {field: '123'}
If a field is set to zero, {field: '0'}
If a field is set to null, {field: ''}

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (0 - raw, 50, 100, 200, 500, 1000, 5000)
Snapshot (200, 500, 1000, 5000)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.mini.d",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.mini.d",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Ticker Snap
STREAM: v1.ticker.s

Feed Selector
Feed Data
Errors
Try it out
WSTickerFeedSelectorV1

Subscribes to a ticker feed for a single instrument. The ticker.s channel offers simpler integration. To experience higher publishing rates, please use the ticker.d channel.
Unlike the ticker.d channel which publishes an initial snapshot, then only streams deltas after, the ticker.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of the ticker.
After the snapshot, the server will only send deltas of the ticker.
The server will send a delta if any of the fields in the ticker have changed.


Field Semantics:
[DeltaOnly] If a field is not updated, {}
If a field is updated, {field: '123'}
If a field is set to zero, {field: '0'}
If a field is set to null, {field: ''}

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (100, 200, 500, 1000, 5000)
Snapshot (500, 1000, 5000)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.ticker.s",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.ticker.s",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Ticker Delta
STREAM: v1.ticker.d

Feed Selector
Feed Data
Errors
Try it out
WSTickerFeedSelectorV1

Subscribes to a ticker feed for a single instrument. The ticker.s channel offers simpler integration. To experience higher publishing rates, please use the ticker.d channel.
Unlike the ticker.d channel which publishes an initial snapshot, then only streams deltas after, the ticker.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of the ticker.
After the snapshot, the server will only send deltas of the ticker.
The server will send a delta if any of the fields in the ticker have changed.


Field Semantics:
[DeltaOnly] If a field is not updated, {}
If a field is updated, {field: '123'}
If a field is set to zero, {field: '0'}
If a field is set to null, {field: ''}

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (100, 200, 500, 1000, 5000)
Snapshot (500, 1000, 5000)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.ticker.d",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.ticker.d",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Orderbook
Orderbook Snap
STREAM: v1.book.s

Feed Selector
Feed Data
Errors
Try it out
WSOrderbookLevelsFeedSelectorV1

Subscribes to aggregated orderbook updates for a single instrument. The book.s channel offers simpler integration. To experience higher publishing rates, please use the book.d channel.
Unlike the book.d channel which publishes an initial snapshot, then only streams deltas after, the book.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of all levels of the Orderbook.
After the snapshot, the server will only send levels that have changed in value.


Subscription Pattern:
Delta - instrument@rate
Snapshot - instrument@rate-depth


Field Semantics:
[DeltaOnly] If a level is not updated, level not published
If a level is updated, {size: '123'}
If a level is set to zero, {size: '0'}
Incoming levels will be published as soon as price moves
Outgoing levels will be published with size = 0

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (50, 100, 500, 1000)
Snapshot (500, 1000)
depth
d	integer	False
'0'	Depth of the order book to be retrieved
Delta(0 - unlimited)
Snapshot(10, 50, 100, 500)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.book.s",
        "selectors": ["BTC_USDT_Perp@500-50"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.book.s",
        "subs": ["BTC_USDT_Perp@500-50"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Orderbook Delta
STREAM: v1.book.d

Feed Selector
Feed Data
Errors
Try it out
WSOrderbookLevelsFeedSelectorV1

Subscribes to aggregated orderbook updates for a single instrument. The book.s channel offers simpler integration. To experience higher publishing rates, please use the book.d channel.
Unlike the book.d channel which publishes an initial snapshot, then only streams deltas after, the book.s channel publishes full snapshots at each feed.

The Delta feed will work as follows:

On subscription, the server will send a full snapshot of all levels of the Orderbook.
After the snapshot, the server will only send levels that have changed in value.


Subscription Pattern:
Delta - instrument@rate
Snapshot - instrument@rate-depth


Field Semantics:
[DeltaOnly] If a level is not updated, level not published
If a level is updated, {size: '123'}
If a level is set to zero, {size: '0'}
Incoming levels will be published as soon as price moves
Outgoing levels will be published with size = 0

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
rate
r	integer	True	The minimal rate at which we publish feeds (in milliseconds)
Delta (50, 100, 500, 1000)
Snapshot (500, 1000)
depth
d	integer	False
'0'	Depth of the order book to be retrieved
Delta(0 - unlimited)
Snapshot(10, 50, 100, 500)
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.book.d",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.book.d",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Trade
Trade
STREAM: v1.trade

Feed Selector
Feed Data
Errors
Try it out
WSTradeFeedSelectorV1

Subscribes to a stream of Public Trades for an instrument.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
limit
l	integer	True	The limit to query for. Valid values are (50, 200, 500, 1000). Default is 50
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.trade",
        "selectors": ["BTC_USDT_Perp@500"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.trade",
        "subs": ["BTC_USDT_Perp@500"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Candlestick
Candlestick
STREAM: v1.candle

Feed Selector
Feed Data
Errors
Try it out
WSCandlestickFeedSelectorV1

Subscribes to a stream of Kline/Candlestick updates for an instrument. A Kline is uniquely identified by its open time.
A new Kline is published every interval (if it exists). Upon subscription, the server will send the 5 most recent Kline for the requested interval.

Name
Lite	Type	Required
Default	Description
instrument
i	string	True	The readable instrument name:
Perpetual: ETH_USDT_Perp
Future: BTC_USDT_Fut_20Oct23
Call: ETH_USDT_Call_20Oct23_2800
Put: ETH_USDT_Put_20Oct23_2800
interval
i1	CandlestickInterval	True	The interval of each candlestick
type
t	CandlestickType	True	The type of candlestick data to retrieve
CandlestickInterval
CandlestickType
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.candle",
        "selectors": ["BTC_USDT_Perp@CI_1_M-TRADE"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.candle",
        "subs": ["BTC_USDT_Perp@CI_1_M-TRADE"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Trading API
Order
Create Order
Cancel Order
Cancel All Orders
Get Order
Open Orders
Order History
Cancel On Disconnect
Execution
Fill History
Funding Payment History
Position
Positions
Set Position Config
Add Position Margin
Get Position Margin Limits
Transfer
Deposit History
Transfer
Transfer History
Withdrawal
Withdrawal History
Account
Sub Account Summary
Sub Account History
Aggregated Account Summary
Funding Account Summary
DeriskMMRatio
Set Derisk M M Ratio
Account
Get Sub Accounts
InitialLeverage
Get All Initial Leverage
Set Initial Leverage
Vault
Vault Burn Tokens
Vault Invest
Vault Investor Summary
Vault Redeem
Vault Redeem Cancel
Vault Redemption Queue
Vault Manager Investment History
Builder
Get Authorized Builders
Execution
Builder Fill History
Trading APIs
All requests should be made using the POST HTTP method.

Order
Create Order
FULL ENDPOINT: full/v1/create_order
LITE ENDPOINT: lite/v1/create_order

Request
Response
Errors
Try it out
ApiCreateOrderRequest

Create an order on the orderbook for this trading account.

Name
Lite	Type	Required
Default	Description
order
o	Order	True	The order to create
Order
Query

Full Request


{
    "order": {
        "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
        "is_market": false,
        "time_in_force": "GOOD_TILL_TIME",
        "post_only": false,
        "reduce_only": false,
        "legs": [{
            "instrument": "BTC_USDT_Perp",
            "size": "10.5",
            "limit_price": "65038.01",
            "is_buying_asset": true
        }],
        "signature": {
            "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
            "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
            "v": 28,
            "expiration": "1697788800000000000",
            "nonce": 1234567890,
            "chain_id": "325"
        },
        "metadata": {
            "client_order_id": "23042",
            "create_time": "1697788800000000000",
            "trigger": {
                "trigger_type": "TAKE_PROFIT",
                "tpsl": {
                    "trigger_by": "LAST",
                    "trigger_price": "65038.10",
                    "close_position": false
                }
            },
            "broker": "BROKER_CODE"
        },
        "builder": "'$GRVT_MAIN_ACCOUNT_ID'",
        "builder_fee": 0.001
    }
}
Lite Request

{
    "o": {
        "sa": "'$GRVT_SUB_ACCOUNT_ID'",
        "im": false,
        "ti": "GOOD_TILL_TIME",
        "po": false,
        "ro": false,
        "l": [{
            "i": "BTC_USDT_Perp",
            "s": "10.5",
            "lp": "65038.01",
            "ib": true
        }],
        "s": {
            "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
            "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
            "v": 28,
            "e": "1697788800000000000",
            "n": 1234567890,
            "ci": "325"
        },
        "m": {
            "co": "23042",
            "ct": "1697788800000000000",
            "t": {
                "tt": "TAKE_PROFIT",
                "t": {
                    "tb": "LAST",
                    "tp": "65038.10",
                    "cp": false
                }
            },
            "b": "BROKER_CODE"
        },
        "b": "'$GRVT_MAIN_ACCOUNT_ID'",
        "bf": 0.001
    }
}

Cancel Order
FULL ENDPOINT: full/v1/cancel_order
LITE ENDPOINT: lite/v1/cancel_order

Request
Response
Errors
Try it out
ApiCancelOrderRequest

Cancel an order on the orderbook for this trading account. Either order_id or client_order_id must be provided.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID cancelling the order
order_id
oi	string	False
0	Cancel the order with this order_id
client_order_id
co	string	False
0	Cancel the order with this client_order_id
time_to_live_ms
tt	string	False
100	Specifies the time-to-live (in milliseconds) for this cancellation.
During this period, any order creation with a matching client_order_id will be cancelled and not be added to the GRVT matching engine.
This mechanism helps mitigate time-of-flight issues where cancellations might arrive before the corresponding orders.
Hence, cancellation by order_id ignores this field as the exchange can only assign order_ids to already-processed order creations.
The duration cannot be negative, is rounded down to the nearest 100ms (e.g., '670' -> '600', '30' -> '0') and capped at 5 seconds (i.e., '5000').
Value of '0' or omission results in the default time-to-live value being applied.
If the caller requests multiple successive cancellations for a given order, such that the time-to-live windows overlap, only the first request will be considered.
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "order_id": "0x1028403",
    "client_order_id": "23042",
    "time_to_live_ms": "500"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "oi": "0x1028403",
    "co": "23042",
    "tt": "500"
}

Cancel All Orders
FULL ENDPOINT: full/v1/cancel_all_orders
LITE ENDPOINT: lite/v1/cancel_all_orders

Request
Response
Errors
Try it out
ApiCancelAllOrdersRequest

Cancel all orders on the orderbook for this trading account. This may not match new orders in flight.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID cancelling all orders
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be cancelled
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be cancelled
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be cancelled
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"]
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"]
}

Get Order
FULL ENDPOINT: full/v1/order
LITE ENDPOINT: lite/v1/order

Request
Response
Errors
Try it out
ApiGetOrderRequest

Retrieve the order for the account. Either order_id or client_order_id must be provided.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
order_id
oi	string	False
0	Filter for order_id
client_order_id
co	string	False
0	Filter for client_order_id
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "order_id": "0x1028403",
    "client_order_id": "23042"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "oi": "0x1028403",
    "co": "23042"
}

Open Orders
FULL ENDPOINT: full/v1/open_orders
LITE ENDPOINT: lite/v1/open_orders

Request
Response
Errors
Try it out
ApiOpenOrdersRequest

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"]
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"]
}

Order History
FULL ENDPOINT: full/v1/order_history
LITE ENDPOINT: lite/v1/order_history

Request
Response
Errors
Try it out
ApiOrderHistoryRequest

Retrieves the order history for the account.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
start_time
st	string	False
0	The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned
end_time
et	string	False
now()	The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"],
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"],
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}

Cancel On Disconnect
FULL ENDPOINT: full/v1/cancel_on_disconnect
LITE ENDPOINT: lite/v1/cancel_on_disconnect

Request
Response
Errors
Try it out
ApiCancelOnDisconnectRequest

Auto-Cancel All Open Orders when the countdown time hits zero.

Market Maker inputs a countdown time parameter in milliseconds (e.g. 120000 for 120s) rounded down to the smallest second follows the following logic:
- Market Maker initially entered a value between 0 -> 1000, which is rounded to 0: will result in termination of their COD
- Market Maker initially entered a value between 1001 -> 300_000, which is rounded to the nearest second: will result in refresh of their COD
- Market Maker initially entered a value bigger than 300_000, which will result in error (upper bound)
Market Maker will send a heartbeat message by calling the endpoint at specific intervals (ex. every 30 seconds) to the server to refresh the count down.

If the server does not receive a heartbeat message within the countdown time, it will cancel all open orders for the specified Sub Account ID.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID cancelling the orders for
countdown_time
ct	string	False
1000	Countdown time in milliseconds (ex. 120000 for 120s).

0 to disable the timer.

Does not accept negative values.

Minimum acceptable value is 1,000.

Maximum acceptable value is 300,000
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "countdown_time": 300
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "ct": 300
}

Execution
Fill History
FULL ENDPOINT: full/v1/fill_history
LITE ENDPOINT: lite/v1/fill_history

Request
Response
Errors
Try it out
ApiFillHistoryRequest

Query for all historical fills made by a single account. A single order can be matched multiple times, hence there is no real way to uniquely identify a trade.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to request for
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
start_time
st	string	False
0	The start time to apply in unix nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned
end_time
et	string	False
now()	The end time to apply in unix nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"],
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"],
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}

Funding Payment History
FULL ENDPOINT: full/v1/funding_payment_history
LITE ENDPOINT: lite/v1/funding_payment_history

Request
Response
Errors
Try it out
ApiFundingPaymentHistoryRequest

Query for all historical funding payments made by a single account.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to request for
instrument
i	string	False
all	The perpetual instrument to filter for
start_time
st	string	False
0	The start time to apply in unix nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned
end_time
et	string	False
now()	The end time to apply in unix nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the query from
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "instrument": "BTC_USDT_Perp",
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": "",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"]
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "i": "BTC_USDT_Perp",
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": "",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"]
}

Position
Positions
FULL ENDPOINT: full/v1/positions
LITE ENDPOINT: lite/v1/positions

Request
Response
Errors
Try it out
ApiPositionsRequest

Query the positions of a sub account

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to request for
kind
k	[Kind]	False
all	The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
base
b	[string]	False
all	The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned
quote
q	[string]	False
all	The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
Kind
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "kind": ["PERPETUAL"],
    "base": ["BTC", "ETH"],
    "quote": ["USDT", "USDC"]
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "k": ["PERPETUAL"],
    "b": ["BTC", "ETH"],
    "q": ["USDT", "USDC"]
}

Set Position Config
FULL ENDPOINT: full/v1/set_position_config
LITE ENDPOINT: lite/v1/set_position_config

Request
Response
Errors
Try it out
ApiSetSubAccountPositionMarginConfigRequest

Sets the margin type and leverage configuration for a specific position (instrument) within a sub account.

This configuration is applied per-instrument, allowing different margin settings for different positions.


Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to set the margin type and leverage for
instrument
i	string	True	The instrument of the position to set the margin type and leverage for
margin_type
mt	PositionMarginType	True	The margin type to set for the position
leverage
l	string	True	The leverage to set for the position
signature
s	Signature	True	The signature of this operation
PositionMarginType
Signature
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "instrument": "BTC_USDT_Perp",
    "margin_type": "ISOLATED",
    "leverage": "1.5",
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "i": "BTC_USDT_Perp",
    "mt": "ISOLATED",
    "l": "1.5",
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Add Position Margin
FULL ENDPOINT: full/v1/add_position_margin
LITE ENDPOINT: lite/v1/add_position_margin

Request
Response
Errors
Try it out
ApiAddIsolatedPositionMarginRequest

The request to add margin to a isolated position

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to add isolated margin in or remove margin from
instrument
i	string	True	The instrument to add margin into, or remove margin from
amount
a	string	True	The amount of margin to add to the position, positive to add, negative to remove, expressed in quote asset decimal units
signature
s	Signature	True	The signature of this operation
Signature
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "instrument": "BTC_USDT_Perp",
    "amount": "123456.78",
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "i": "BTC_USDT_Perp",
    "a": "123456.78",
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Get Position Margin Limits
FULL ENDPOINT: full/v1/get_position_margin_limits
LITE ENDPOINT: lite/v1/get_position_margin_limits

Request
Response
Errors
Try it out
ApiGetIsolatedPositionMarginLimitsRequest

The request to get the max addable and removable amount for an isolated position

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to get the margin limits for
instrument
i	string	True	The isolated position asset to get the margin limits for
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "instrument": "BTC_USDT_Perp"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "i": "BTC_USDT_Perp"
}

Transfer
Deposit History
FULL ENDPOINT: full/v1/deposit_history
LITE ENDPOINT: lite/v1/deposit_history

Request
Response
Errors
Try it out
ApiDepositHistoryRequest

The request to get the historical deposits of an account
The history is returned in reverse chronological order
Both finalized and pending deposits are returned, and pending deposits are indicated by an empty confirmedTime field.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
currency
c	[string]	True	The token currency to query for, if nil or empty, return all deposits. Otherwise, only entries matching the filter will be returned
start_time
st	string	False
0	The start time to query for in unix nanoseconds
end_time
et	string	False
now()	The end time to query for in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c1	string	False
''	The cursor to indicate when to start the next query from
main_account_id
ma	string	False
``	Main account ID being queried. By default, applies the requestor's main account ID.
Query

Full Request


{
    "currency": ["USDT", "USDC"],
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": "",
    "main_account_id": null
}
Lite Request

{
    "c": ["USDT", "USDC"],
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c1": "",
    "ma": null
}

Transfer
FULL ENDPOINT: full/v1/transfer
LITE ENDPOINT: lite/v1/transfer

Request
Response
Errors
Try it out
ApiTransferRequest

This API allows you to transfer funds in multiple different ways


Between SubAccounts within your Main Account

Between your MainAccount and your SubAccounts

To other MainAccounts that you have previously allowlisted

Fast Withdrawal Funding Address
For fast withdrawals, funds must be sent to the designated funding account address. Please ensure you use the correct address based on the environment:
Production Environment Address:
[To be updated, not ready yet]
This address should be specified as the to_account_id in your API requests for transferring funds using the transfer API. Ensure accurate input to avoid loss of funds or use the UI.

Name
Lite	Type	Required
Default	Description
from_account_id
fa	string	True	The main account to transfer from
from_sub_account_id
fs	string	True	The subaccount to transfer from (0 if transferring from main account)
to_account_id
ta	string	True	The main account to deposit into
to_sub_account_id
ts	string	True	The subaccount to transfer to (0 if transferring to main account)
currency
c	string	True	The token currency to transfer
num_tokens
nt	string	True	The number of tokens to transfer, quoted in tokenCurrency decimal units
signature
s	Signature	True	The signature of the transfer
transfer_type
tt	TransferType	True	The type of transfer
transfer_metadata
tm	string	True	The metadata of the transfer
Signature
TransferType
Query

Full Request


{
    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "currency": "USDT",
    "num_tokens": "1500.0",
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    },
    "transfer_type": "UNSPECIFIED",
    "transfer_metadata": "{\"provider\":\"XY\",\"direction\":\"WITHDRAWAL\",\"provider_tx_id\":\"txn123456\",\"chainid\":\"42161\",\"endpoint\":\"0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0\"}"
}
Lite Request

{
    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "fs": "'$GRVT_SUB_ACCOUNT_ID'",
    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "ts": "'$GRVT_SUB_ACCOUNT_ID'",
    "c": "USDT",
    "nt": "1500.0",
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    },
    "tt": "UNSPECIFIED",
    "tm": "{\"provider\":\"XY\",\"direction\":\"WITHDRAWAL\",\"provider_tx_id\":\"txn123456\",\"chainid\":\"42161\",\"endpoint\":\"0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0\"}"
}

Transfer History
FULL ENDPOINT: full/v1/transfer_history
LITE ENDPOINT: lite/v1/transfer_history

Request
Response
Errors
Try it out
ApiTransferHistoryRequest

The request to get the historical transfers of an account
The history is returned in reverse chronological order

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
currency
c	[string]	True	The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned
start_time
st	string	False
0	The start time to query for in unix nanoseconds
end_time
et	string	False
now()	The end time to query for in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c1	string	False
''	The cursor to indicate when to start the next query from
tx_id
ti	string	False
0	The transaction ID to query for
main_account_id
ma	string	False
``	Main account ID being queried. By default, applies the requestor's main account ID.
transfer_types
tt	[TransferType]	False
[]	The transfer type to filters for. If the list is empty, return all transfer types.
TransferType
Query

Full Request


{
    "currency": ["USDT", "USDC"],
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": "",
    "tx_id": "1028403",
    "main_account_id": null,
    "transfer_types": ["UNSPECIFIED"]
}
Lite Request

{
    "c": ["USDT", "USDC"],
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c1": "",
    "ti": "1028403",
    "ma": null,
    "tt": ["UNSPECIFIED"]
}

Withdrawal
FULL ENDPOINT: full/v1/withdrawal
LITE ENDPOINT: lite/v1/withdrawal

Request
Response
Errors
Try it out
ApiWithdrawalRequest

Leverage this API to initialize a withdrawal from GRVT's Hyperchain onto Ethereum.
Do take note that the bridging process does take time. The GRVT UI will help you keep track of bridging progress, and notify you once its complete.

If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is ~25 USDT.
Withdrawal fees also apply to cover the cost of the Ethereum transaction.
Note that your funds will always remain in self-custory throughout the withdrawal process. At no stage does GRVT gain control over your funds.

Name
Lite	Type	Required
Default	Description
from_account_id
fa	string	True	The main account to withdraw from
to_eth_address
te	string	True	The Ethereum wallet to withdraw into
currency
c	string	True	The token currency to withdraw
num_tokens
nt	string	True	The number of tokens to withdraw, quoted in tokenCurrency decimal units
signature
s	Signature	True	The signature of the withdrawal
Signature
Query

Full Request


{
    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "currency": "USDT",
    "num_tokens": "1500.0",
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
    "c": "USDT",
    "nt": "1500.0",
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Withdrawal History
FULL ENDPOINT: full/v1/withdrawal_history
LITE ENDPOINT: lite/v1/withdrawal_history

Request
Response
Errors
Try it out
ApiWithdrawalHistoryRequest

The request to get the historical withdrawals of an account
The history is returned in reverse chronological order
Both finalized and pending withdrawals are returned, and pending withdrawals are indicated by an empty l1Hash field.

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
currency
c	[string]	True	The token currency to query for, if nil or empty, return all withdrawals. Otherwise, only entries matching the filter will be returned
start_time
st	string	False
0	The start time to query for in unix nanoseconds
end_time
et	string	False
now()	The end time to query for in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c1	string	False
''	The cursor to indicate when to start the next query from
main_account_id
ma	string	False
``	Main account ID being queried. By default, applies the requestor's main account ID.
Query

Full Request


{
    "currency": ["USDT", "USDC"],
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": "",
    "main_account_id": null
}
Lite Request

{
    "c": ["USDT", "USDC"],
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c1": "",
    "ma": null
}

Account
Sub Account Summary
FULL ENDPOINT: full/v1/account_summary
LITE ENDPOINT: lite/v1/account_summary

Request
Response
Errors
Try it out
ApiSubAccountSummaryRequest

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
}

Sub Account History
FULL ENDPOINT: full/v1/account_history
LITE ENDPOINT: lite/v1/account_history

Request
Response
Errors
Try it out
ApiSubAccountHistoryRequest

The request to get the history of a sub account
SubAccount Summary values are snapshotted once every hour
No snapshots are taken if the sub account has no activity in the hourly window
History is preserved only for the last 30 days

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to request for
start_time
st	string	False
0	Start time of sub account history in unix nanoseconds
end_time
et	string	False
now()	End time of sub account history in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the next query from
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}

Aggregated Account Summary
FULL ENDPOINT: full/v1/aggregated_account_summary
LITE ENDPOINT: lite/v1/aggregated_account_summary

Request
Response
Errors
Try it out
EmptyRequest

Used for requests that do not require any parameters

Name
Lite	Type	Required
Default	Description
Query

Full Request


{
}
Lite Request

{
}

Funding Account Summary
FULL ENDPOINT: full/v1/funding_account_summary
LITE ENDPOINT: lite/v1/funding_account_summary

Request
Response
Errors
Try it out
EmptyRequest

Used for requests that do not require any parameters

Name
Lite	Type	Required
Default	Description
Query

Full Request


{
}
Lite Request

{
}

DeriskMMRatio
Set Derisk M M Ratio
FULL ENDPOINT: full/v1/set_derisk_mm_ratio
LITE ENDPOINT: lite/v1/set_derisk_mm_ratio

Request
Response
Errors
Try it out
ApiSetDeriskToMaintenanceMarginRatioRequest

The request to set the derisk margin to maintenance margin ratio of a sub account

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to set the leverage for
ratio
r	string	True	The derisk margin to maintenance margin ratio of this sub account
signature
s	Signature	True	The signature of this operation
Signature
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "ratio": "1.5",
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "r": "1.5",
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Account
Get Sub Accounts
FULL ENDPOINT: full/v1/get_sub_accounts
LITE ENDPOINT: lite/v1/get_sub_accounts

Request
Response
Errors
Try it out
EmptyRequest

Used for requests that do not require any parameters

Name
Lite	Type	Required
Default	Description
Query

Full Request


{
}
Lite Request

{
}

InitialLeverage
Get All Initial Leverage
FULL ENDPOINT: full/v1/get_all_initial_leverage
LITE ENDPOINT: lite/v1/get_all_initial_leverage

Request
Response
Errors
Try it out
ApiGetAllInitialLeverageRequest

The request to get the initial leverage of a sub account

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to get the leverage for
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
}

Set Initial Leverage
FULL ENDPOINT: full/v1/set_initial_leverage
LITE ENDPOINT: lite/v1/set_initial_leverage

Request
Response
Errors
Try it out
ApiSetInitialLeverageRequest

The request to set the initial leverage of a sub account

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to set the leverage for
instrument
i	string	True	The instrument to set the leverage for
leverage
l	string	True	The leverage to set for the sub account
Query

Full Request


{
    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
    "instrument": "BTC_USDT_Perp",
    "leverage": "10"
}
Lite Request

{
    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
    "i": "BTC_USDT_Perp",
    "l": "10"
}

Vault
Vault Burn Tokens
FULL ENDPOINT: full/v1/vault_burn_tokens
LITE ENDPOINT: lite/v1/vault_burn_tokens

Request
Response
Errors
Try it out
ApiVaultBurnTokensRequest

Request payload for burning tokens in a vault.

This API allows a client to burn a specified amount of tokens in a particular vault.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to burn tokens from.
currency
c	string	True	The currency used for the burn. This should be the vault's quote currency.
num_tokens
nt	string	True	The number of tokens to burn.
signature
s	Signature	True	The digital signature from the investing account.
This signature must be generated by the main account ID and is used to verify the authenticity of the request.
The signature must comply with AccountPermExternalTransfer permission.
Signature
Query

Full Request


{
    "vault_id": "3477045127917224",
    "currency": "USDT",
    "num_tokens": 1000000,
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "vi": "3477045127917224",
    "c": "USDT",
    "nt": 1000000,
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Vault Invest
FULL ENDPOINT: full/v1/vault_invest
LITE ENDPOINT: lite/v1/vault_invest

Request
Response
Errors
Try it out
ApiVaultInvestRequest

Request payload for investing in a vault.

This API allows a client to invest a specified amount of tokens in a particular vault.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to invest in.
currency
c	string	True	The currency used for the investment. This should be the vault's quote currency.
num_tokens
nt	string	True	The investment sum, in terms of the token currency specified (i.e., numTokens of '1000' with tokenCurrency of 'USDT' denotes investment of 1,000 USDT).
signature
s	Signature	True	The digital signature from the investing account.
This signature must be generated by the main account ID and is used to verify the authenticity of the request.
The signature must comply with AccountPermExternalTransfer permission.
Signature
Query

Full Request


{
    "vault_id": "3477045127917224",
    "currency": "USDT",
    "num_tokens": 1000000,
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "vi": "3477045127917224",
    "c": "USDT",
    "nt": 1000000,
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Vault Investor Summary
FULL ENDPOINT: full/v1/vault_investor_summary
LITE ENDPOINT: lite/v1/vault_investor_summary

Request
Response
Errors
Try it out
ApiVaultInvestorSummaryRequest

Request payload for fetching the summary of a vault investor.

This API allows a client to retrieve the summary of investments in a specific vault.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to fetch the summary for.
Query

Full Request


{
    "vault_id": "3477045127917224"
}
Lite Request

{
    "vi": "3477045127917224"
}

Vault Redeem
FULL ENDPOINT: full/v1/vault_redeem
LITE ENDPOINT: lite/v1/vault_redeem

Request
Response
Errors
Try it out
ApiVaultRedeemRequest

Request payload for redeeming from a vault.

This API allows a client to redeem a specified amount of tokens from a particular vault.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to redeem from.
currency
c	string	True	The currency used for the redemption. This should be the vault's quote currency.
num_tokens
nt	string	True	The number of shares to redeem.
signature
s	Signature	True	The digital signature from the investing account.
This signature must be generated by the main account ID and is used to verify the authenticity of the request.
The signature must comply with AccountPermExternalTransfer permission.
Signature
Query

Full Request


{
    "vault_id": "3477045127917224",
    "currency": "USDT",
    "num_tokens": 1000000,
    "signature": {
        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "expiration": "1697788800000000000",
        "nonce": 1234567890,
        "chain_id": "325"
    }
}
Lite Request

{
    "vi": "3477045127917224",
    "c": "USDT",
    "nt": 1000000,
    "s": {
        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
        "v": 28,
        "e": "1697788800000000000",
        "n": 1234567890,
        "ci": "325"
    }
}

Vault Redeem Cancel
FULL ENDPOINT: full/v1/vault_redeem_cancel
LITE ENDPOINT: lite/v1/vault_redeem_cancel

Request
Response
Errors
Try it out
ApiVaultRedeemCancelRequest

Request payload for canceling a vault redemption.

This API allows a client to cancel a previously initiated redemption from a vault.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to cancel the redemption from.
Query

Full Request


{
    "vault_id": "3477045127917224"
}
Lite Request

{
    "vi": "3477045127917224"
}

Vault Redemption Queue
FULL ENDPOINT: full/v1/vault_view_redemption_queue
LITE ENDPOINT: lite/v1/vault_view_redemption_queue

Request
Response
Errors
Try it out
ApiVaultViewRedemptionQueueRequest

Request payload for a vault manager to view the redemption queue for their vault.

Fetches the redemption queue for a vault, ordered by descending priority.

Urgent redemption requests, defined as having been pending >90% of the manager-defined maximum redemption period, have top priority (following insertion order).

Non-urgent redemption requests are otherwise prioritized by insertion order, unless they are >5x the size of the smallest redemption request.

E.g., If FIFO ordering (all non-urgent) is 1k -> 50k -> 100k -> 20k -> 10k -> 25k, then priority ordering is 1k -> 10k -> 50k -> 20k -> 100k -> 25k.

Only displays redemption requests that are eligible for automated redemption, i.e., have been pending for the manager-defined minimum redemption period.

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to fetch the redemption queue for.
Query

Full Request


{
    "vault_id": "3477045127917224"
}
Lite Request

{
    "vi": "3477045127917224"
}

Vault Manager Investment History
FULL ENDPOINT: full/v1/vault_manager_investor_history
LITE ENDPOINT: lite/v1/vault_manager_investor_history

Request
Response
Errors
Try it out
ApiQueryVaultManagerInvestorHistoryRequest

Request for the manager to retrieve the vault investor history for their vault

Name
Lite	Type	Required
Default	Description
vault_id
vi	string	True	The unique identifier of the vault to filter by
only_own_investments
oo	boolean	True	Whether to only return investments made by the manager
start_time
st	string	False
0	Optional. Start time in unix nanoseconds
end_time
et	string	False
now()	Optional. End time in unix nanoseconds
Query

Full Request


{
    "vault_id": "2312134",
    "only_own_investments": true,
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000"
}
Lite Request

{
    "vi": "2312134",
    "oo": true,
    "st": "1697788800000000000",
    "et": "1697788800000000000"
}

Builder
Get Authorized Builders
FULL ENDPOINT: full/v1/get_authorized_builders
LITE ENDPOINT: lite/v1/get_authorized_builders

Request
Response
Errors
Try it out
EmptyRequest

Used for requests that do not require any parameters

Name
Lite	Type	Required
Default	Description
Query

Full Request


{
}
Lite Request

{
}

Execution
Builder Fill History
FULL ENDPOINT: full/v1/builder_fill_history
LITE ENDPOINT: lite/v1/builder_fill_history

Request
Response
Errors
Try it out
ApiBuilderFillHistoryRequest

The request to get the historical builder trade of a builder
The history is returned in reverse chronological order

Pagination works as follows:

We perform a reverse chronological lookup, starting from end_time. If end_time is not set, we start from the most recent data.
The lookup is limited to limit records. If more data is requested, the response will contain a next cursor for you to query the next page.
If a cursor is provided, it will be used to fetch results from that point onwards.
Pagination will continue until the start_time is reached. If start_time is not set, pagination will continue as far back as our data retention policy allows.

Name
Lite	Type	Required
Default	Description
start_time
st	string	False
0	The start time to query for in unix nanoseconds
end_time
et	string	False
now()	The end time to query for in unix nanoseconds
limit
l	integer	False
500	The limit to query for. Defaults to 500; Max 1000
cursor
c	string	False
''	The cursor to indicate when to start the next query from
Query

Full Request


{
    "start_time": "1697788800000000000",
    "end_time": "1697788800000000000",
    "limit": 500,
    "cursor": ""
}
Lite Request

{
    "st": "1697788800000000000",
    "et": "1697788800000000000",
    "l": 500,
    "c": ""
}



Trading Websocket Streams
Order
Order
STREAM: v1.order

Feed Selector
Feed Data
Errors
Try it out
WSOrderFeedSelectorV1

Subscribes to a feed of order updates pertaining to orders made by your account.
Each Order can be uniquely identified by its order_id or client_order_id.
To subscribe to all orders, specify an empty instrument (eg. 2345123).
Otherwise, specify the instrument to only receive orders for that instrument (eg. 2345123-BTC_USDT_Perp).

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
instrument
i	string	False
'all'	The instrument filter to apply.
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.order",
        "selectors": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.order",
        "subs": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Order State
STREAM: v1.state

Feed Selector
Feed Data
Errors
Try it out
WSOrderStateFeedSelectorV1

Subscribes to a feed of order updates pertaining to orders made by your account.
Unlike the Order Stream, this only streams state updates, drastically improving throughput, and latency.
Each Order can be uniquely identified by its order_id or client_order_id.
To subscribe to all orders, specify an empty instrument (eg. 2345123).
Otherwise, specify the instrument to only receive orders for that instrument (eg. 2345123-BTC_USDT_Perp).

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
instrument
i	string	False
'all'	The instrument filter to apply.
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.state",
        "selectors": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.state",
        "subs": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Cancel Status
STREAM: v1.cancel

Feed Selector
Feed Data
Errors
Try it out
WSCancelFeedSelectorV1

Subscribes to a feed of time-to-live expiry events for order cancellations requested by a given subaccount.
This stream presently only provides expiry updates for cancel-order requests set with a valid TTL value.
Successful order cancellations will reflect as updates published to the order-state stream.
A future release will expand the functionality of this stream to provide more general status updates on order cancellation requests.
Each Order can be uniquely identified by its client_order_id.


Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.cancel",
        "selectors": ["'$GRVT_SUB_ACCOUNT_ID'"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.cancel",
        "subs": ["'$GRVT_SUB_ACCOUNT_ID'"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Execution
Fill
STREAM: v1.fill

Feed Selector
Feed Data
Errors
Try it out
WSFillFeedSelectorV1

Subscribes to a feed of private trade updates. This happens when a trade is executed.
To subscribe to all private trades, specify an empty instrument (eg. 2345123).
Otherwise, specify the instrument to only receive private trades for that instrument (eg. 2345123-BTC_USDT_Perp).

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The sub account ID to request for
instrument
i	string	False
'all'	The instrument filter to apply.
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.fill",
        "selectors": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.fill",
        "subs": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Positions
STREAM: v1.position

Feed Selector
Feed Data
Errors
Try it out
WSPositionsFeedSelectorV1

Subscribes to a feed of position updates.
Updates get published when a trade is executed, and when leverage configurations are changed for instruments with ongoing positions.
To subscribe to all positions, specify an empty instrument (eg. 2345123).
Otherwise, specify the instrument to only receive positions for that instrument (eg. 2345123-BTC_USDT_Perp).

Name
Lite	Type	Required
Default	Description
sub_account_id
sa	string	True	The subaccount ID to filter by
instrument
i	string	False
'all'	The instrument filter to apply.
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.position",
        "selectors": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.position",
        "subs": ["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Transfer
Deposit
STREAM: v1.deposit

Feed Selector
Feed Data
Errors
Try it out
WSDepositFeedSelectorV1

Subscribes to a feed of deposits. This will execute when there is any deposit to selected account.
To subscribe to a main account, specify the account ID (eg. 0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a).

Name
Lite	Type	Required
Default	Description
main_account_id
ma	string	True	The main account ID to request for
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.deposit",
        "selectors": ["'$GRVT_MAIN_ACCOUNT_ID'"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.deposit",
        "subs": ["'$GRVT_MAIN_ACCOUNT_ID'"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Transfer
STREAM: v1.transfer

Feed Selector
Feed Data
Errors
Try it out
WSTransferFeedSelectorV1

Subscribes to a feed of transfers. This will execute when there is any transfer to or from the selected account.
To subscribe to a main account, specify the account ID (eg. 0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a).
To subscribe to a sub account, specify the main account and the sub account dash separated (eg. 0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a-1920109784202388).

Name
Lite	Type	Required
Default	Description
main_account_id
ma	string	True	The main account ID to request for
sub_account_id
sa	string	False
'0'	The sub account ID to request for
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.transfer",
        "selectors": ["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.transfer",
        "subs": ["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe

Withdrawal
STREAM: v1.withdrawal

Feed Selector
Feed Data
Errors
Try it out
WSWithdrawalFeedSelectorV1

Subscribes to a feed of withdrawals. This will execute when there is any withdrawal from the selected account.
To subscribe to a main account, specify the account ID (eg. 0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a).

Name
Lite	Type	Required
Default	Description
main_account_id
ma	string	True	The main account ID to request for
JSONRPC Wrappers
Subscribe
Full Subscribe Request


{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "stream": "v1.withdrawal",
        "selectors": ["'$GRVT_MAIN_ACCOUNT_ID'"]
    },
    "id": 123
}
Full Subscribe Response

{
    "jsonrpc": "2.0",
    "result": {
        "stream": "v1.withdrawal",
        "subs": ["'$GRVT_MAIN_ACCOUNT_ID'"],
        "unsubs": [],
        "num_snapshots": [10],
        "first_sequence_number": [872634876]
    },
    "id": 123,
    "method": "subscribe"
}
Unsubscribe
Legacy Subscribe