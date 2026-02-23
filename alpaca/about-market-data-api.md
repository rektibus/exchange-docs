# About Market Data API

Source: https://docs.alpaca.markets/docs/about-market-data-api

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
# About Market Data API
Gain seamless access to a wealth of data with Alpaca Market Data API, offering real-time and historical information for equities, options, crypto and more.
# Overview

The Market Data API offers seamless access to market data through both HTTP and WebSocket protocols. With a focus on historical and real-time data, developers can efficiently integrate these APIs into their applications.
To simplify the integration process, we provide user-friendly SDKs in Python, Go, NodeJS, and C#. These SDKs offer comprehensive functionalities, making it easier for developers to work with the Market Data APIs & Web Sockets.
To experiment with the APIs, developers can try them with Postman: either through the public workspace on Postman or directly from our GitHub repository.
By leveraging Alpaca Market Data API and its associated SDKs, developers can seamlessly incorporate historical and real-time market data into their applications, enabling them to build powerful and data-driven financial products.

# Subscription Plans

Alpaca offers two distinct subscription models depending on how you access our platform:

- Trading API: For individual traders using Alpaca&#x27;s trading platform directly
- Broker API: For broker partners building their own trading platforms on top of Alpaca&#x27;s infrastructure

ℹ️Which one applies to me?If you signed up for an Alpaca account to trade or build a personal trading app, you&#x27;re using the Trading API. If you&#x27;re a business integrating Alpaca as your backend brokerage provider, you&#x27;re using the Broker API.

## Trading API Subscriptions

For individual traders and developers using Alpaca&#x27;s Trading API, we offer two subscription plans: Basic and Algo Trader Plus.
The Basic plan serves as the default option for both Paper and Live trading accounts, ensuring all users can access essential data with zero cost. However, this plan only includes limited real-time data: for equities only the IEX exchange, for options only the indicative feed. For advanced traders we recommend subscribing to Algo Trader Plus which includes complete market coverage for stocks and options as well.

### Equities

BasicAlgo Trader Plus
 | Pricing | Free | $99 / month
 | Securities coverage | US Stocks & ETFs | US Stocks & ETFs
 | Real-time market coverage | IEX | All US Stock Exchanges
 | Websocket subscriptions | 30 symbols | Unlimited
 | Historical data timeframe | Since 2016 | Since 2016
 | Historical data limitation* | latest 15 minutes | no restriction
 | Historical API calls | 200 / min | 10,000 / min
Our data sources are directly fed by the CTA (Consolidated Tape Association), which is administered by NYSE (New York Stock Exchange), and the UTP (Unlisted Trading Privileges) stream, which is administered by Nasdaq. The synergy of these two sources ensures comprehensive market coverage, encompassing 100% of market volume.

### Options

BasicAlgo Trader Plus
 | Securities coverage | US Options Securities | US Options Securities
 | Real-time market coverage | Indicative Pricing Feed | OPRA Feed
 | Websocket subscriptions | 200 quotes | 1000 quotes
 | Historical data limitation* | latest 15 minutes | no restriction
 | Historical API calls | 200 / min | 10,000 / min
Our options data sources are directly fed by OPRA (Options Price Reporting Authority).

## Broker API Subscriptions

For broker partners integrating Alpaca&#x27;s Broker API, we offer tiered subscription plans designed for higher-volume, multi-user platforms.
For equities, the below subscription plans are available.

Subscription NameRPM (Request Per Minute)Stream Connection LimitStream Symbol LimitPrice (per month)Options Indicative Feed
 | Standard | 1,000 | 5 | unlimited | included | additional $1,000 per month
 | StandardPlus3000 | 3,000 | 5 | unlimited | $500 | additional $1,000 per month
 | StandardPlus5000 | 5,000 | 5 | unlimited | $1,000 | included
 | StandardPlus10000 | 10,000 | 10 | unlimited | $2,000 | included
Note: Standard subscription plans will only be active when integration starts. Prior to that, the account will be on the Basic plan listed above. Additionally, similar to the free plan all the standard plans are real time IEX or 15 mins delayed SIP.
For partners on the Standard and StandardPlus3000 plans, an additional subscription fee of $1,000 / month enables access to the same equities plan for options. For StandardPlus5000 and StandardPlus10000 plans, options are included.
📘We offer custom pricing and tailored solutions for Broker API partners seeking to leverage our comprehensive market data. Our goal is to meet the specific needs and requirements of our valued partners, ensuring they have access to the data and tools necessary to enhance their services and provide exceptional value to their customers. If none of the subscription plans listed above are believed to be suitable, kindly reach out to our sales team.

# Authentication

With the exception of historical crypto data, all market data endpoints require authentication. Authentication differs between the Trading & Broker API. API keys can be acquired in the web UI (under the API keys on the right sidebar).

### Trading API

You should authenticate by passing the key / secret pair in the HTTP request headers named:

- `APCA-API-KEY-ID`
- `APCA-API-SECRET-KEY`

### Broker API

Broker API uses the Client Credentials authentication flow. You must first exchange your credentials for a short-lived access token, then use that token to authenticate API requests.

- Step 1: Request an access token

cURL
```
`curl -X POST "https://authx.alpaca.markets/v1/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials" \
     -d "client_id={YOUR_CLIENT_ID}" \
     -d "client_secret={YOUR_CLIENT_SECRET}"`
```

- Step 2: Use the token to authenticate

cURL
```
`curl -X GET "https://data.alpaca.markets/v2/..." \
     -H "Authorization: Bearer {TOKEN}"`
```

🚧Note: Access tokens are valid for 15 minutes. Do not request a new token for each API call.
For the WebSocket stream authentication, kindly refer to the WebSocket Stream documentation.Updated 25 days ago Alpaca&#x27;s MCP ServerGetting Started with Market Data API- Ask AI
