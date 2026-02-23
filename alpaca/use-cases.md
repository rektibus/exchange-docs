# Use Cases

Source: https://docs.alpaca.markets/docs/use-cases

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
# Use Cases
There are several different use cases for Broker API integration. Below are some common ones, but please do not hesitate to reach out to our sales team if you have a different case in mind. We want our platform to encourage a broad range of use cases.

- Broker dealer (fully-disclosed, omnibus)
- Registered Investment Advisor (RIA)

We support most use cases internationally.
Depending on the case, the API methods you want to use could vary. For example, the omnibus broker-dealer case never uses API to open a customer account since the trading accounts are created upfront and you will submit orders to them, and manage your end customer accounting on your end. More details on each use case are described in the following sections.

# Broker Dealer

## Fully-Disclosed

You are a registered broker-dealer in your jurisdiction and you introduce your customers to Alpaca to establish individual accounts on a fully-disclosed basis. Alpaca receives each customer’s information in order to open an account and provide our services.
Depending on your registration status and regulations in your jurisdiction, you may own the full end-to-end user experience from account opening, to trading, and reporting. You are responsible for maintaining a robust Customer Identification Program (CIP) and Know Your Customer (KYC) procedures, in accordance with Anti-Money Laundering (AML) regulations. To ensure compliance with applicable laws, Alpaca will conduct due diligence on your firm, including a thorough review of your CIP/KYC/AML program.
In this setup, you will use most of the API methods such as the Account, Transfer and Trading API. In addition, you can move cash and securities between your firm account and end-customer accounts using the Journal API to implement features such as reward programs.

## Omnibus

You are a registered broker-dealer and you manage customer accounting and one main trading account for the entire trading flow of your customers. In the omnibus setup, your end customer information (e.g. name, address) is not disclosed to Alpaca.
When submitting customer orders for your two trading accounts, you will indicate if the order is for the long or short position of each customer. To meet our regulatory requirements, you will be required to submit a “sub-tag” in each order to identify different customer’s order flow. This can be just an arbitrary text string such as UUID or a customer ID number. Alpaca, as well as our trading execution venues, need to be able to review and account for all trading activity. Failure to submit the required trading order flow information may result in the suspension of the entire order flow.
As each end customer is not disclosed to Alpaca, you are responsible for all tax reporting in your local jurisdiction. If you are a non-US broker-dealer, this will likely require registration with the IRS as a Foreign Financial Institution (FFI) and get certified as a Qualified Intermediary (QI) to be certified to manage taxes on the US-sourced income by foreigners.

# Registered Investment Advisor (RIA)

You are a SEC-registered RIA with customers either in or outside the US.
Similar to the Trading/Investing App approach described above, the end customer is introduced to Alpaca on an individual basis. The account approval process is owned by Alpaca, and you own the user experience and most of the communications. Unless you have a robust CIP/KYC/AML program in place that has been vetted by Alpaca, your customers will go through Alpaca’s CIP/KYC/AML process.
The Account API works slightly differently from the fully-disclosed case for this setup. Please see the rest of API documentation for more details.
As an RIA, you can communicate with your customers directly. Alpaca will work hand-in-hand with you to market your service using Broker API in a compliant manner.
Currently, Alpaca does not support order allocation and advisory fee calculation as built-in functionality. These items are on our roadmap.Updated 5 months ago Credentials ManagementIntegration Setup with Alpaca- Ask AI
