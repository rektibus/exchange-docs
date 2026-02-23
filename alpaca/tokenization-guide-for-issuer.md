# Tokenization Guide for Issuer

Source: https://docs.alpaca.markets/docs/tokenization-guide-for-issuer

---

## Introduction
- Welcome- About Alpaca- Alpaca API Platform- Authentication- SDKs and Tools- Additional Resources
## BROKER API
- About Broker API- Getting Started with Broker API- Credentials Management- Use Cases- Integration Setup with Alpaca- Broker API FAQs- Mandatory Corporate Actions- Voluntary Corporate Actions- FDIC Sweep Program- Instant Funding- Fully Paid Securities Lending- 24/5 Trading- OmniSub- Fixed Income- Customer Account Opening- Accounts Statuses- International Accounts- Domestic (USA) Accounts- Data Validations- IRA Accounts Overview- Crypto Trading- Crypto Wallets API- Funding Accounts- Journals API- Funding Wallets- ACH Funding- Instant Funding- Trading- Portfolio Rebalancing- SSE Events- Account Status Events for KYCaaS- Daily Processes and Reconcilations- Banking Holiday Funding Processes- Statements and Confirms- Local Currency Trading (LCT)- Example Trading App (Ribbit)- Options Trading Overview- Fixed Income- Tokenization Guide for Issuer- Tokenization Guide for Authorized Participant- Custodial accounts
## TRADING API
- About Trading API- Getting Started with Trading API- Working with /account- Working with /assets- Working with /orders- Working with /positions- Paper Trading- Trading Account- Crypto Spot Trading- Crypto Orders- Crypto Pricing Data- Crypto Spot Trading Fees- Options Trading- Options Orders- Options Level 3 Trading- Non-Trade Activities for Option Events- Account Activities- Fractional Trading- Margin and Short Selling- Placing Orders- DMA Gateway / Advanced Order Types- User Protection- Websocket Streaming- Trading API FAQs- Position Average Entry Price Calculation- Regulatory Fees- Alpaca&#x27;s MCP Server
## Market Data API
- About Market Data API- Getting Started with Market Data API- Historical API- Historical Stock Data- Historical Crypto Data- Historical Option Data- Historical News Data- WebSocket Stream- Real-time Stock Data- Real-time Crypto Data- Real-time News- Real-time Option Data- Market Data FAQ
## Connect API
- About Connect API- Registering Your App- Using OAuth2 and Trading API
## FIX API
- About FIX API- FIX Specification
# Tokenization Guide for Issuer
Instant Tokenization Network (ITN) is a platform designed to streamline and accelerate the process of in-kind mint and redemption of tokenized assets. The goal of ITN is to enable efficient, secure, and rapid conversion of real-world and digital assets to and from various tokens issued by partners on the network. The network acts as instant settlement rails for market participants to programmatically rebalance inventory, thereby stitching together fragmented tokenized asset liquidity across the industry. This document will guide the Issuer of tokenized assets on how to start using Alpaca’s Instant Tokenization Network.
# Overview

Before you start integrating into Alpaca&#x27;s ITN (Instant Tokenization Network) as an issuer of tokenized assets, you would need to:

- Complete your integration into Alpaca&#x27;s Broker API offering.
- Have an account in your name at Alpaca.

If you have not done so yet, please make sure to reach out to Alpaca sales to initiate the conversation.
If you have already done so, the below document will guide you to integrate into ITN. This will be achieved by:

- Implementing 4 endpoints on your platform that Alpaca will utilize to process account linking & token minting.

- Account Linking
- Tokenized Assets
- Mint Request
- Mint Confirmation

- Integrating with 2 Alpaca endpoints that you will utilize to complete token minting and redemption flows.

- Mint Confirmation Callback
- Redeem Request

## Important Prerequisite

During the mint and redeem process, Instant Tokenization Network will journal securities to/from the AP&#x27;s Alpaca account to/from the Issuer&#x27;s Alpaca account. If you, as an issuer, hold multiple accounts at Alpaca, please ensure to inform Alpaca which of your accounts should be designated for tokenization.

# Handshake Process

Before an entity can mint or redeem your tokenized assets through ITN, they will need to reach out to Alpaca’s operation team for a "handshake" step through which Alpaca will need to verify that the entity is:

- An existing client of Alpaca.
- An existing client of your firm and registered as an authorized participant (AP) on your platform.

To automate this process, you will need to provide an account linking endpoint that Alpaca can utilize to link an AP’s account at Alpaca to their account on your platform. Alpaca will maintain this linking and use it during the mint and redeem processes.

#### Issuer’s Account Linking Endpoint

Alpaca will invoke your account linking endpoint by providing the AP&#x27;s email and their Alpaca account number. Your endpoint should respond with the AP’s account number on your platform that Alpaca will store for future use during the mint and redeem flow:
Expected Request
Endpoint
HTML
```
`POST /tokenization/accounts/connect`
```

Body
JSON
```
`{
  "email": "[email&#160;protected]",
  "account" : "alpaca_account_number"
}`
```

FieldDescription
 | email | AP’s email used on the Issuer’s platform
 | account | AP&#x27;s Alpaca account number
Expected Response
Body
JSON
```
`{
  "client_id": "5505-1234-ABC-4G45"
}`
```

FieldDescription
 | client_id | AP’s account identifier on the Issuer’s platform
Status Codes

StatusDescription
 | 200 | OK - Successful link
 | 404 | Email not found
 | 409 | Account already linked

# Tokenized Assets Data

You will need to provide Alpaca an endpoint that can be used to retrieve the list of supported tokenized assets on your issuer platform. The endpoint should provide the following data:

- underlying symbol
- token symbol
- supported blockchain networks

Expected Request
Endpoint
HTML
```
`GET /tokenization/tokens`
```

Expected Response
Body
JSON
```
`{
  "tokens": [
    {
	"underlying": "AAPL",
	"token": "tAAPL",	
	"networks": ["solana", "ethereum"]
    },
    {
	"underlying": "TSLA",
  	"token": "tTSLA",
	"networks": ["solana", "ethereum"]
   }
  ]
}`
```

FieldDescription
 | tokens | List of supported tokens
 | underlying | Underlying asset symbol
 | token | Token asset symbol
 | networks | List of supported networks
Alpaca will use this information when validating an AP&#x27;s mint request.

# Mint Endpoint and Workflow

The token minting flow has multiple steps that begin when an AP requests token minting from Alpaca. The steps are explained below & depicted in Figure 1 to help you visualize, and all endpoints mentioned are documented below as well.

- The Authorized Participant sends Alpaca a mint request.
- Alpaca invokes an endpoint on your platform to submit a mint request, with a JSON object in the body. Your platform will need to validate the mint request.
- Alpaca journals the underlying security from the AP’s account into your Alpaca account.
- Alpaca invokes another endpoint on your platform to confirm the underlying asset&#x27;s journal status.
- Your platform deposits the tokens into the AP’s wallet on a successful journal.
- Your platform invokes Alpaca’s endpoint to confirm the successful token mint, providing the designated Alpaca tokenization account_id as a URL parameter in the endpoint.

Figure 1. Minting a tokenized asset

## Endpoints you need to provide

#### Issuer’s Mint Request Endpoint

This endpoint will be invoked by Alpaca at step 2.
Expected Request
Endpoint
HTML
```
`POST /tokenization/mint`
```

Body
JSON
```
`{
  "id": "12345-678-90AB",
  "qty": "1.23",
  "underlying_symbol": "TSLA",
  "token_symbol": "TSLAx",
  "network": "solana",
  "client_id": "98765432",
  "wallet_address": "<AP&#x27;s wallet address to deposit the tokenized asset>"
}`
```

FieldDescription
 | id | Unique request identifier assigned by Alpaca
 | qty | The underlying quantity to convert into the tokenized asset. The value can be fractional.
 | underlying_symbol | Underlying asset symbol
 | token_symbol | Tokenized asset symbol
 | network | The token’s blockchain network. Currently, we support the following networks:
- solana
- base

 | client_id | AP’s account identifier on the Issuer&#x27;s platform. This is the account identifier received during the handshake/account linking step.
 | wallet_address | The destination wallet address where the tokenized assets should be deposited
Expected Response
Body
JSON
```
`{
  "issuer_request_id": "123-456-ABCD-7890",
  "status": "created"
}`
```

FieldDescription
 | issuer_request_id | Unique identifier assigned by the Issuer
 | status | Tokenization request status. Once the request has been successfully validated, the Issuer will create a mint tokenization request on their platform. This does not mean that the token is created.
- created

Status Codes

StatusDescription
 | 200 | OK
 | 400 | 
- Invalid Wallet: Wallet does not belong to client
- Invalid Token: Token not available on the network
- Insufficient Eligibility: Client not eligible
- Failed Validation: Invalid data payload

#### Issuer Mint Journal Confirmation Endpoint

This endpoint will be invoked by Alpaca at step 4.
Expected Request
Endpoint
HTML
```
`/tokenization/mint/confirm`
```

Body
JSON
```
`{
  "id": "12345-678-90AB",
  "issuer_request_id": "ABC-123-DEF-456",
  "status": "<completed/rejected>"
}`
```

FieldDescription
 | id | Unique request identifier previously assigned by Alpaca
 | issuer_request_id | Unique identifier assigned by the Issuer as previously received on the mint response
 | status | The journal status. Valid values are:
- rejected
- completed

Expected Response
Expected Status Codes

StatusDescription
 | 200 | OK

## Endpoints you need to integrate with

#### Alpaca&#x27;s Mint Confirmation Callback Endpoint

This endpoint will be invoked by your platform at step 6.
Request
Endpoint
HTML
```
`POST /v1/accounts/:account_id/tokenization/callback/mint`
```

Body
JSON
```
`{
  "id": "12345-678-90AB",
  "client_id": "5505-1234-ABC-4G45",
  "wallet_address": "<AP&#x27;s wallet address where the tokenized assets were deposited>",
  "tx_hash": "0x12345678",
  "network": "solana"
}`
```

FieldDescription
 | id | Unique request identifier previously assigned by Alpaca
 | client_id | AP’s account identifier on the Issuer&#x27;s platform
 | wallet_address | Wallet address where the tokenized assets were deposited
 | tx_hash | Mint’s transaction hash on the blockchain
 | network | The token’s blockchain network. Currently, we support the following networks:
- solana
- base

Response
Status Codes

StatusDescription
 | 200 | OK
 | 400 | Internal failure while processing the mint confirmation

# Redeem Endpoint and Workflow

The token redeem flow has multiple steps that begin when an AP deposits token into a redemption wallet address that you provide them with. The steps are explained below & depicted in Figure 2 to help you visualize, and all endpoints mentioned are documented below as well.

- The token redemption process will be initiated by an end client by moving tokens into the a redemption wallet address provided by you as an Issuer, at which point these tokens should be removed from circulation.
- Your platform should then notify Alpaca that an AP has redeemed their tokens by invoking an endpoint. Your platform should provide their designated Alpaca tokenization account_id as a URL parameter in the endpoint.
- Alpaca will journal the underlying asset from your Alpaca account as an issuer, into the AP’s Alpaca account.

Figure 2. Redeeming a tokenized asset

## Endpoint you need to integrate with

#### Alpaca&#x27;s Redeem Request Endpoint

This endpoint will be invoked by your platform at step 2.
Request
Endpoint
HTML
```
`POST /v1/accounts/:account_id/tokenization/redeem`
```

Body
JSON
```
`{
  "issuer_request_id": "ABC-123-DEF-456",
  "underlying_symbol": "AAPL",
  "token_symbol": "AAPLx",
  "client_id": "5505-1234-ABC-4G45",
  "qty": "1.23",
  "network": "solana",
  "wallet_address": "<the originating wallet address for the redeemed tokens>",
  "tx_hash": "0x12345678"
}`
```

FieldDescription
 | issuer_request_id | Unique identifier assigned by the Issuer
 | underlying_symbol | Underlying asset symbol
 | token_symbol | Token asset symbol
 | client_id | AP’s account identifier on the Issuer&#x27;s platform
 | qty | The quantity to convert into the underlying asset. The value can be fractional.
 | network | The originating token’s blockchain network. Currently, we support the following networks:
- solana
- base

 | wallet_address | The address where the redeemed tokens were originally held
 | tx_hash | The transaction hash of the tokens being sent to the Issuer&#x27;s redemption wallet
Response
Body
JSON
```
`{
  "id": "12345-678-90AB",
  "issuer_request_id": "ABCDEF123",
  "created_at":"2025-09-12T17:28:48.642437-04:00",
  "type": "redeem",
  "status": "completed",
  "underlying_symbol": "TSLA",
  "token_symbol" : "TSLAx",
  "qty" : "123.45",
  "issuer" : "xstocks",
  "network": "solana",
  "wallet_address": "0x1234567A",
  "tx_hash" : "0x1234567A",
  "fees" : "0.567"
}`
```

FieldDescription
 | id | Unique request identifier assigned by Alpaca
 | issuer_request_id | Unique identifier assigned by the Issuer
 | created_at | Timestamp when Alpaca received the redeem request
 | type | Tokenization request type:
- redeem

 | status | Current status of the redemption request:
- pending
- completed
- rejected

 | underlying_symbol | The underlying asset symbol
 | token_symbol | The tokenized asset symbol
 | qty | The quantity to convert into the underlying asset. It can be fractional.
 | issuer | The tokenized asset&#x27;s Issuer. Valid values are:
- xstocks
- st0x

 | network | The token&#x27;s blockchain network. Valid values are:
- solana
- base

 | wallet_address | The originating wallet where the tokenized assets were previously held
 | tx_hash | The transaction hash of the tokens being sent to the Issuer&#x27;s redemption wallet
 | fees | The fees charged for this tokenization request

# Additional Useful Endpoints

#### List Tokenization Requests

You can use the following endpoint to list the tokenization requests performed through your platform. You will need to provide your designated Alpaca tokenization account_id as a URL parameter in the endpoint.
Request
Endpoint
HTML
```
`GET /v1/accounts/:account_id/tokenization/requests`
```

Response
Body
JSON
```
`[
   {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  }
]`
```

FieldDescription
 | id | Unique request identifier assigned by Alpaca
 | issuer_request_id | Unique identifier assigned by the Issuer
 | created_at | Timestamp when the request was created
 | updated_at | Timestamp when the request was last updated
 | type | Tokenization request type. Valid values are:
- mint
- redeem

 | status | Current status of the tokenization request:
- pending
- completed
- rejected

 | underlying_symbol | The underlying asset symbol
 | token_symbol | The token asset symbol
 | qty | The quantity for this request
 | issuer | The tokenized asset&#x27;s Issuer. Valid values are:
- xstocks
- st0x

 | network | The token&#x27;s blockchain&#x27;s network. Valid values are:
- solana
- base

 | wallet_address | The wallet address associated with this request
 | tx_hash | The transaction hash on the blockchain
 | fees | The fees charged for this tokenization request

# Glossary

- Authorized Participant: An entity licensed to conduct digital asset business in the tokenized asset, e.g xstocks. The Issuer only sells tokenized assets to Authorized Participants (AP). The AP can sell the tokenized assets to their clients.
- Issuer: Financial entity which purchases the underlying equity securities, wraps them and creates/issues tokens which are backed by the same.
- Mint: The act of converting underlying equity securities into tokenized assets.
- Redeem: The act of converting tokenized assets into their underlying equity securities.

Alpaca&#x27;s Instant Tokenization Network is owned and developed by AlpacaDB, Inc. and Alpaca Crypto LLC.
Additional geographic restrictions may apply for tokenization services based on local regulatory requirements. Neither Alpaca Crypto LLC nor Alpaca Securities LLC are the issuer of, nor directly involved in, the tokenization of any assets. Tokenization is performed by a third party. Tokenized assets do not represent direct equity ownership in any underlying company or issuer. Instead, tokenized assets generally provide economic exposure to the equity securities of an underlying issuer. As such, holders of tokenized assets have no voting rights, dividend entitlements, or legal claims to the underlying company shares or any residual assets in the event of the underlying company’s liquidation or insolvency, unless explicitly stated otherwise. All investments involve risk. For more information, please see our Tokenization Risk Disclosure.Updated about 1 month ago Fixed IncomeTokenization Guide for Authorized Participant- Ask AI
