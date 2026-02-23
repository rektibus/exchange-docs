# Crypto Orders

Source: https://docs.alpaca.markets/docs/crypto-orders

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
# Crypto Orders
You can submit crypto orders through the traditional orders API endpoints (`POST/orders`).

- The following order types are supported: `market`, `limit` and `stop_limit`
- The following `time_in_force` values are supported: `gtc`, and `ioc`
- We accept fractional orders as well with either `notional` or `qty` provided

You can submit crypto orders for a any supported crypto pair via API, see the below cURL POST request.
cURL
```
`curl --request POST &#x27;https://paper-api.alpaca.markets/v2/orders&#x27; \
--header &#x27;Apca-Api-Key-Id: <KEY>&#x27; \
--header &#x27;Apca-Api-Secret-Key: <SECRET>&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
  "symbol": "BTC/USD",
  "qty": "0.0001",
  "side": "buy",
  "type": "market",
  "time_in_force": "gtc"
}&#x27;`
```

The above request submits a market order via API to buy 0.0001 BTC with USD (BTC/USD pair) that is good till end of day.Updated 5 months ago Crypto Spot TradingCrypto Pricing Data- Ask AI
