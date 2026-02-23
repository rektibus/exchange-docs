# crypto-pricing-data

Source: https://docs.alpaca.markets/docs/crypto-pricing-data

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
# Crypto Pricing Data
Alpaca provides free limited crypto data and a more advanced unlimited paid plan.To request trading pairs data via REST API, see Crypto Pricing Data REST API Reference.
The example below requests the latest order book data (bid and asks) for the following three crypto trading pairs: BTC/USD, ETH/BTC and ETH/USD.
cURL
```
`curl --request GET &#x27;https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD,SOL/USDT&#x27; \
--header &#x27;Apca-Api-Key-Id: <KEY>&#x27; \
--header &#x27;Apca-Api-Secret-Key: <SECRET>&#x27;`
```

```
`{
    "orderbooks": {
        "BTC/USD": {
            "a": [
                {
                    "p": 27539.494,
                    "s":  0.2632414
                },
                ...
            ],
            "b": [
                {
                    "p": 27511.78083,
                    "s": 0.26265668
                },
                ...
            ],
            "t": "2023-03-18T13:31:44.932988033Z"
        },
        "ETH/USD": { ... },
        "ETH/BTC": { ... },
        "SOL/USDT": { ... }
    }
}`
```

# Real-Time Crypto Market Data

Additionally, you can subscribe to real-time crypto data via Websockets. Example below leverages wscat to subscribe to:

- BTC/USD trades.
- ETH/USDT and ETH/USD quotes.
- BTC/USD order books

```
` $ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "<KEY>", "secret": "<SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe", "trades":["BTC/USD"], "quotes":["ETH/USDT","ETH/USD"], "orderbooks":["BTC/USD"]}
< [{"T":"subscription","trades":["BTC/USD"],"quotes":["ETH/USDT","ETH/USD"],"orderbooks":["BTC/USD"],"updatedBars":[],"dailyBars":[]}]
< [{"T":"o","S":"BTC/USD","t":"2023-03-18T13:51:29.754747009Z","b":[{"p":27485.3445,"s":0.25893365},{"p":27466.92727,"s":0.52351568},...],"a":[{"p":27512.92,"s":0.26137249},{"p":27547.9425,"s":0.52011956},...],"r":true}]
< [{"T":"q","S":"ETH/USDT","bp":1815.55510989,"bs":8.24941727,"ap":1818.4,"as":4.15121428,"t":"2023-03-18T13:51:33.256826818Z"}]
< ...`
```
Updated 5 months ago Crypto OrdersCrypto Spot Trading Fees- Ask AI
