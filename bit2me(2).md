Pro (Trading Spot) REST API
Server
Server:
https://gateway.bit2me.com
Gateway API

No authentication selected
Client Libraries
Shell Curl
Data hierarchy (Collapsed)​
Data hierarchy
**Parent account / parent wallet**: This account / wallet is manually created by Bit2Me and provided to you via API Keys. This is your company's master account and wallet. Parent accounts must be KYB'ed before operating.
Sub Account / wallet: A parent account can create one (1) sub account / wallet on behalf of each end user. You can generate as many end users as you want, but each can only operate on a single sub account or wallet. Sub Accounts must be KYC'ed before operating.

Pocket: A wallet can own many pockets. Each pocket can hold a specific type of currency. For example: "BTC pocket", "ETH pocket", "EUR pocket"… pockets are optional (you can operate at a wallet level).

Fig. - Data hierarchy
Introduction (Collapsed)​
Introduction
👏 Welcome to Bit2Me as API.

We help individuals, exchanges, mining pools, tokens issuers, investment funds, governments and institutions to access, trade and manage cryptocurrencies and digital assets optimally.

Being the access door to markets without friction, leaving obsolete the traditional financial system, the company is made up of more than 300 people: idealists, technological entrepreneurs, researchers, quantitative, financial traders, lawyers and engineers from large companies.

We operate tirelessly around all time and world phases, with central offices in Spain, Europe.

The documentation that follows gives you access to our Crypto market data, Trading, and Custody products.

Logical steps to operate with API (Collapsed)​
Logical steps to operate with API
[Auth] Obtain your API Keys for production environment from Bit2Me team.

[Subaccount] Using your API Key, generate sub accounts for each individual user.

[KYC] Perform the KYC to the individual user. If you are a regulated entity and already perform an equivalent KYC on your side, our sales team will explain to you how to reuse it.

[Funding] your parent account with fiat money.

Important notes

A minimum fiat balance is required to operate, as part of the initial set up there is a one time fiat transfer that must be sent to the fiat account that Bit2Me will tell you during the onboarding process
If you are a bank, the parent fiat account will be held in your own institution
During the day to day operations, fiat money must be funded to the main account. You should keep records of fiat money balances of each subaccount
4.1 [Funding] your account with EUR.

4.2 [Funding] your account with BRL.

4.3 [Funding] your account with ARS. (Soon)

*If you're looking for USD, please get in touch with our sales team. Currently this is only available in Bit2Me Pro.

[Funding] your account with crypto.

Obtain [Market] information for price and rates.

Get a list of assets
Get ticker information for currency pair
[Wallet] Create proforma transaction with the buy, sell or exchange operation you want to execute.

After that:

7.1 [Wallet] Execute the proforma transaction you created earlier.

[Trading] Use Bit2Me Pro to do your high-frequency trading.

Deposit funds into your Bit2Me Pro account
Place an order
[Earn] Deposit or withdraw crypto from earn protocols.

List supported assets
Get assets annual percentage yields.
List subaccount earn wallets.
Deposit/withdraw cryptos in earn.
[Transfers] Move money between users (peer to peer):

First create a transfer from the origin user.
Then claim the transfer for the destination user.
[Withdraw] your fiat.

[Withdraw] your crypto.


IMPORTANT: Logical steps are not examples, if you're looking for them, check the next section.

Quickstart (Collapsed)​
Quickstart
Official Repositories
Are you a coder? Check out these GitHub repositories to kickstart your journey with us!

Bit2Me Broker
Bit2Me Pro
Postman
You can test the Bit2Me API from Postman by importing our OpenAPI specification. You have two options:

Option 1 — Import by link

In Postman, go to Import → Link.
Paste this URL: https://api.bit2me.com/openapi.json
Option 2 — Import by file

Download the spec using the button below.
In Postman, go to Import → File and select the downloaded file.
Download OpenAPI (for Postman)

AI Agents and LLMs
Your LLM or AI agent can use our OpenAPI spec as the source of truth for the Bit2Me API: endpoints, authentication, parameters, schemas, and responses.

Bit2Me MCP (Model Context Protocol) — Bit2Me offers an MCP server so AI assistants (Claude, Cursor, IDEs with MCP support) can call the Bit2Me API in a standard way.

Integration guide: https://mcp.bit2me.com — step-by-step instructions to add the Bit2Me MCP to your assistant.

Spec URLs (copy if needed) — Main spec: https://api.bit2me.com/openapi.json

Per-product specs (same origin):

https://api.bit2me.com/openapi/crypto.json
https://api.bit2me.com/openapi/embed.json
https://api.bit2me.com/openapi/money-flow.json
https://api.bit2me.com/openapi/trading-spot-rest.json
https://api.bit2me.com/openapi/trading-spot-websockets.json
Snippets for rules, skills and commands:

Rule (copy & paste): The Bit2Me OpenAPI spec is at https://api.bit2me.com/openapi.json. Use it as the source of truth for endpoints, auth, parameters, and responses.
Skill (copy & paste): When working with Bit2Me API, consult the OpenAPI spec at https://api.bit2me.com/openapi.json and validate paths, methods, parameters, auth, and schemas against it.
Command (copy & paste): Read the OpenAPI spec from https://api.bit2me.com/openapi.json and use it as the source of truth. Propose only HTTP calls and payloads that are valid according to that spec.
Rate Limit (Collapsed)​
Rate Limit
To ensure optimal performance and reliability of our API, we have implemented rate limits on the number of requests that can be made within a given timeframe. Below is a table detailing the allowed requests per minute (RPM) for different tiers:

Tier	Max. RPM (request per minute)
Starter	600
Medium	800
Pro	1000
To request a new tier, contact our support center

All endpoints of this API are designed to enforce strict usage policies to ensure fair access and optimal performance for all users. As a result, any request that exceeds the allowed rate limits, may trigger a HTTP response with two types of error:

Code 429: The user has sent too many requests in a given timeframe.
Code 418: The user has been banned from accessing the API.
Important note: It is essential for users to adhere to the specified guidelines to avoid these error responses and maintain uninterrupted access to the API's functionalities, otherwise you'll be banned.

Status (Collapsed)​
Status
🔔 Stay updated with the latest platform updates and outages! Click the button below to suscribe to our service to receive all the news and announcements directly to your inbox.

👉 Suscribe 👈

Use cases (Collapsed)​
Use cases
The following are some common use cases that illustrate how our API can be leveraged:

Perform KYC process - Complete subaccount data, add address, init verification identity process
Enable main account google authenticator 2fa - Retrieve 2fa user verification, start and end 2fa enablement process
Enable subaccount google authenticator 2fa - Start and end subaccount 2fa enablement process
Deposit crypto in subaccount - Create crypto pocket, get unique address, receive cryptos
Fiat deposit - For EUR check bank accounts and make transfer, for BRL create deposit proforma
Calculate pocket balances - Get pocket balance for fiat and crypto pockets
Crypto buy operation - Generate proforma for buy operation, execute proforma confirmation
Crypto sell operation - Generate proforma for sell operation, execute proforma confirmation
Crypto swap operation - Generate proforma for swap operation, execute proforma confirmation
Deposit crypto in earn service - Check available assets, create earn deposit
Withdraw crypto from earn service - List user earn wallets, create earn withdraw
Fiat withdraw (EUR) - Create withdraw proforma, execute withdraw order
Fiat withdraw (BRL) - Create pix withdraw proforma, execute pix withdraw order
Withdraw crypto from subaccount - Create transaction with network address, confirm transaction
For detailed examples with request bodies and step-by-step instructions, check the specific operation endpoints in the API documentation.

Funding (Collapsed)​
FundingOperations
get
/v1/trading/wallet/balance
get
/v1/trading/movement
post
/v1/trading/wallet/deposit
post
/v1/trading/wallet/withdraw
Market Data (Collapsed)​
Market DataOperations
get
/v1/trading/trade/last
get
/v1/trading/market-config
get
/v1/trading/candle
get
/v2/trading/order-book
get
/v2/trading/tickers
Trading (Collapsed)​
TradingOperations
post
/v1/trading/order
delete
/v1/trading/order/{id}
get
/v1/trading/order/{id}
get
/v1/trading/order/{id}/trades
get
/v1/trading/order
get
/v1/trading/trade
WebSockets Authentication (Collapsed)​
WebSockets AuthenticationOperations
post
/v1/signin/apikey