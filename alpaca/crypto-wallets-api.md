# crypto-wallets-api

Source: https://docs.alpaca.markets/docs/crypto-wallets-api

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
# Crypto Wallets API
Please note you have to reach out to Alpaca to enable Crypto Wallets API access. Please reach out to your Customer Success Manager or your Sales Representative to enable this feature for you.

## Overview

The Alpaca Crypto Wallets API enables you to deposit, withdraw, and manage cryptocurrency assets within your Alpaca account. This document explains how to use Alpaca’s Crypto Wallets API to test fund accounts with crypto assets (like USDC), verify transfers, and begin trading.

## Supported Assets

### Supported Testnets & Faucets (Sandbox)

To test deposit and withdrawal flows for different assets across supported blockchain networks, you can use the following testnet faucets. Always ensure you’re requesting tokens and interacting on the correct network (e.g., Ethereum Sepolia, Solana Devnet).
Stablecoins

- USDC (Testnet/Devnet Support)

- Networks: Ethereum Sepolia, Solana Devnet
- Faucet: Circle Testnet Faucet

- USDG (Testnet Support)

- Networks: Ethereum Sepolia, Solana Devnet
- Faucet: Paxos Faucet

- USDT (Testnet)

- Network: Ethereum Sepolia
- Faucet:

- WeenusTokenFaucet GitHub
- Contract Address: 0x7439...fB9 on Etherscan

BTC (Testnet)

- tBTC — Bitcoin Testnet4 Faucet

Solana (Devnet)

- Solana Devnet Faucet – Airdrop SOL

ETH (Sepolia)

- 
Alchemy Sepolia Faucet

- 
Google Cloud Sepolia Faucet

- 
QuickNode Faucet

XRP (Testnet)

- XRPL Tesnet Faucet

## Getting Started: Sandbox Testing Guide

### Step 1: Generate Your Funding Wallet Address

Create or retrieve your crypto funding wallet address for the desired asset:
`GET /v1/accounts/{account_id}/wallets?asset=USDC&network=ethereum`
Response:
JSON
```
`{
    "asset_id": "5d0de74f-827b-41a7-9f74-9c07c08fe55f",
    "address": "0x42a76C83014e886e639768D84EAF3573b1876844",
    "created_at": "2025-08-07T08:52:40.656166Z"
}`
```

### Step 2: Fund Your Wallet (Sandbox)

For USDC Testing:

- Visit the Circle Sepolia Faucet: https://faucet.circle.com
- Paste your wallet address from Step 1
- Click Send
- Wait for ~12 block confirmations (typically 2-3 minutes)

### Step 3: Verifying Deposits

Monitor incoming transfers to confirm your deposit:
Option 1: Poll transfers API
`GET /v1/accounts/{account_id}/wallets/transfers`
Response:
JSON
```
`[
    {
        "id": "876b1c4f-df5e-4d1b-beaa-81af7f7bd02c",
        "tx_hash": "0xaca1f6ba105a68771d966b4ce17e0992ad3d8030d127cdb18e113efa3a864992",
        "direction": "INCOMING",
        "amount": "10",
        "usd_value": "9.99707",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0x3C3380cdFb94dFEEaA41cAD9F58254AE380d752D",
        "to_address": "0x42a76C83014e886e639768D84EAF3573b1876844",
        "status": "COMPLETE",
        "created_at": "2025-08-07T10:31:41.964121Z",
        "network_fee": "0",
        "fees": "0"
    },
    {
        "id": "bf31ecca-e28c-4f9a-8e81-12bbf79836fd",
        "tx_hash": "0x849de6f0f225c18b58f3dea5a76a42a0dcba4902ce069147bb0dcd585a3e699b",
        "direction": "INCOMING",
        "amount": "5",
        "usd_value": "4.998794999999999",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "to_address": "0x42a76C83014e886e639768D84EAF3573b1876844",
        "status": "COMPLETE",
        "created_at": "2025-08-08T11:13:26.263719Z",
        "network_fee": "0",
        "fees": "0"
    }
]
`
```

Status Values:

- `PROCESSING`: Transaction submitted to blockchain
- `COMPLETE`: Funds available for trading
- `FAILED`: Transaction failed

Option 2: NTA SSE event
Sample event showing incoming deposit:
JSON
```
`{
    "id": "a6a3f62c-d4dd-4b6f-9b3a-fb65892c9695",
    "qty": 10,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "OCT",
    "net_amount": 0,
    "description": "Deposit Transaction, transfer_id: 296f3a5b-72e8-4ec6-b1fe-77048e77e87f, tx_hash: 0x97fa0e98598d7bedf2871bc1846daa076cddafaa9046b3697b6cd89ca7304932",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9997",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:09:01.061337Z",
    "event_ulid": "01K5GG9ZC5A3CVKP5QEZ79PVEX"
}
`
```

### Step 4: Trading with Deposited Assets (Optional)

Convert your deposited crypto to USD buying power by selling against USD:
`POST /v1/trading/accounts/{account_id}/orders`
Request Body:
JSON
```
`{
  "symbol": "USDC/USD",
  "qty": "50",
  "side": "sell",
  "type": "market", 
  "time_in_force": "day"
}`
```

### Step 5: Start Trading

Once your USDC converts to USD buying power, you can:

- Trade equities and ETFs
- Trade other crypto pairs

In order to check your USD buying power, you can call Retrieve Trading Details for an Account API endpoint, and look for `buying_power`.

## Withdrawing Crypto Assets

### Overview

Withdrawing cryptocurrency from your Alpaca account requires a multi-step process to ensure fund safety:

- Whitelist the destination address
- Verify whitelist approval status
- Request withdrawal to approved address
- Monitor withdrawal status

### Step 1: Whitelist Destination Address

Before withdrawing, you must whitelist the destination wallet address:
`POST v1/accounts/{account_id}/wallets/whitelists`
Request Body:
JSON
```
`{
  "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
  "asset": "USDC"
}`
```

Response:
JSON
```
`[
    {
        "id": "45efdedd-28cd-4665-98b4-601d5f34ae0a",
        "chain": "ETH",
        "asset": "USDC",
        "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "created_at": "2025-08-07T13:16:46.49111Z",
        "status": "PENDING"
    }
]`
```

### Step 2: Check Whitelist Approval Status

Monitor your whitelisted addresses to confirm approval (within 24 hours):
`GET v1/accounts/{account_id}/wallets/whitelists`
Response:
JSON
```
`[
    {
        "id": "45efdedd-28cd-4665-98b4-601d5f34ae0a",
        "chain": "ETH",
        "asset": "USDC",
        "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "created_at": "2025-08-07T13:16:46.49111Z",
        "status": "APPROVED"
    }
]
`
```

### Step 3: Request Withdrawal

Once approved, create a withdrawal transfer:
`POST /v1/accounts/{account_id}/wallets/transfers`
Request Body:
JSON
```
`{
 "amount": "55",
 "address": "34c18dbe-0983-4e61-b493-9578714dae23",
 "asset": "USDC"
}`
```

Response:
JSON
```
`{
    "id": "f8fe06fe-702e-4d79-802c-f31cb1677f7c",
    "tx_hash": null,
    "direction": "OUTGOING",
    "amount": "55",
    "usd_value": "54.9725",
    "chain": "ETH",
    "asset": "USDC",
    "from_address": "0xA0D2C7210D7e2112A4F7888B8658CB579226dB3B",
    "to_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
    "status": "PROCESSING",
    "created_at": "2025-09-19T08:37:25.436307Z",
    "network_fee": "20",
    "fees": "0.3025"
}
`
```

### Step 4: Monitor Withdrawal Status

Track your withdrawal progress:
Option 1: Poll transfers API
`GET /v1/accounts/{account_id}/wallets/transfers`
Response:
JSON
```
`[ {
        "id": "f8fe06fe-702e-4d79-802c-f31cb1677f7c",
        "tx_hash": null,
        "direction": "OUTGOING",
        "amount": "55",
        "usd_value": "54.9725",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0xA0D2C7210D7e2112A4F7888B8658CB579226dB3B",
        "to_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "status": "PROCESSING",
        "created_at": "2025-09-19T08:37:25.436307Z",
        "network_fee": "0",
        "fees": "0.3025"
    }
]
`
```

Option 2: NTA SSE event
Sample event showing outgoing withdrawals:
JSON
```
`{
    "id": "a554262e-71dc-4a02-a0c0-271bcb9480e4",
    "qty": -54.6975,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "OCT",
    "net_amount": 0,
    "description": "Withdrawal Transaction, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821881Z",
    "event_ulid": "01K5GJFGQDE4WQME5F38ZTXSTS"
}
`
```

You can also expect to see `CFEE` depending on your correspondent configuration linked to the withdrawal transactions.
JSON
```
`{
    "id": "5abfdea7-de14-4985-8632-428e8ffb7aa5",
    "qty": 1.3475,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Correspondent Transaction Fee, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.819319Z",
    "event_ulid": "01K5GJFGQBCWVHV4YDV13QW68V"
}

{
    "id": "106a8e17-af4f-4dd1-a0a7-463ea035cb12",
    "qty": -0.275,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Transaction Fee, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821196Z",
    "event_ulid": "01K5GJFGQDDT69PTT6K37N1CQN"
}

{
    "id": "472f9c57-22b7-41a0-82b2-396e51fb99cf",
    "qty": -1.375,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Correspondent Transaction Income, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821937Z",
    "event_ulid": "01K5GJFGQDE5RGMVCJBDS42K0P"
}
`
```
Updated about 1 month ago Crypto TradingFunding Accounts- Ask AI
