# Options Orders

Source: https://docs.alpaca.markets/docs/options-orders

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
# Options Orders
This page provides examples of valid order payloads
# Tier 1 Orders

## Sell a Covered Call

```
`{
  "symbol": "AAPL231201C00195000",
  "qty": "2",
  "side": "sell",
  "type": "limit",
  "limit_price": "1.05",
  "time_in_force": "day"
}`
```

Note, the account must have an existing position of 200 shares of AAPL as the order is for 2 contracts, and each option contract is for 100 shares of underlying.

## Sell a Cash-Secured Put

```
`{
  "symbol": "AAPL231201P00175000",
  "qty": "1",
  "side": "sell",
  "type": "market",
  "time_in_force": "day"
}`
```

Note, the account must have sufficient buying power.  The account must have ($175 strike) x (100 shares) x (1 contract) = $17,500 USD buying power available.

# Tier 2 Orders

## Buy a Call

```
`{
  "symbol": "AAPL240119C00190000",
  "qty": "1",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}`
```

The account must have sufficient buying power to afford the call option.  If the market order is executed at $5.10, the account must have ($5.10 execution price) x (100 shares) x (1 contract) = $510.00 USD buying power.

## Buy a Put

```
`{
  "symbol": "AAPL240119P00170000",
  "qty": "1",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}`
```

The account must have sufficient buying power to afford purchasing put option.  If the market order is executed at  $1.04, the account must have ($1.04 execution price) x (100 shares) x (1 contract) = $104.00 USD buying power.Updated 5 months ago Options TradingOptions Level 3 Trading- Ask AI
