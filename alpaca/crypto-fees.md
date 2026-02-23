# Crypto Spot Trading Fees

Source: https://docs.alpaca.markets/docs/crypto-fees

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
# Crypto Spot Trading Fees
While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller&#x27;s posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. A maker is someone who adds liquidity, and the order gets placed on the order book.  A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.
See the below table with volume-tiered fee pricing:

Tier30D Crypto Volume (USD)MakerTake
 | 1 | 0 - 100,000 | 0.15% | 0.25%
 | 2 | 100,000 - 500,000 | 0.12% | 0.22%
 | 3 | 500,000 - 1,000,000 | 0.10% | 0.20%
 | 4 | 1,000,000 - 10,000,000 | 0.08% | 0.18%
 | 5 | 10,000,000- 25,000,000 | 0.05% | 0.15%
 | 6 | 25,000,000 - 50,000,000 | 0.02% | 0.13%
 | 7 | 50,000,000 - 100,000,000 | 0.02% | 0.12%
 | 8 | 100,000,000+ | 0.00% | 0.10%
The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples:

- Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
- Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
- Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
- Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`

To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`.
See below example of CFEE object:
JSON
```
`{
    "id": "20220812000000000::53be51ba-46f9-43de-b81f-576f241dc680",
    "activity_type": "CFEE",
    "date": "2022-08-12",
    "net_amount": "0",
    "description": "Coin Pair Transaction Fee (Non USD)",
    "symbol": "ETHUSD",
    "qty": "-0.000195",
    "price": "1884.5",
    "status": "executed"
}`
```

Fees are currently calculated and posted end of day. If you query on same day of trade you might not get results. We will be providing an update for fee posting to be real-time in the near future.
📘
### Check out our Crypto Trading FAQ here
Updated 5 months ago Crypto Pricing DataOptions Trading- Ask AI
