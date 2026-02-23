# crypto-trading

Source: https://docs.alpaca.markets/docs/crypto-trading

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
# Crypto Spot Trading
Trade crypto through our API and the Alpaca web dashboard! Trade all day, seven days a week, as frequently as you’d like.🚧
### As of November 18, 2022, cryptocurrency trading is open to select international jurisdictions and some U.S. jurisdictions.
To view the supported US regions for crypto trading, click here.

# Supported Coins

Alpaca supports over 20+ unique crypto assets across 56 trading pairs. Current trading pairs are based on BTC, USD,  USDT and USDC) with more assets and trading pairs coming soon.
To query all available crypto assets and pairs you can you use the following API call:
cURL
```
`curl --request GET &#x27;https://api.alpaca.markets/v2/assets?asset_class=crypto&#x27; \
--header &#x27;Apca-Api-Key-Id: <KEY>&#x27; \
--header &#x27;Apca-Api-Secret-Key: <SECRET>&#x27;`
```

Below is a sample trading pair object composed of two assets, BTC and USD.
JSON
```
`{
  "id": "276e2673-764b-4ab6-a611-caf665ca6340",
  "class": "crypto",
  "exchange": "ALPACA",
  "symbol": "BTC/USD",
  "name": "BTC/USD pair",
  "status": "active",
  "tradable": true,
  "marginable": false,
  "shortable": false,
  "easy_to_borrow": false,
  "fractionable": true,
  "min_order_size": "0.0001",
  "min_trade_increment": "0.0001",
  "price_increment": "1"
}`
```

Note that symbology for trading pairs has changed from our previous format, where `BTC/USD` was previously referred to as `BTCUSD`. Our API has made proper changes to support the legacy convention as well for backwards compatibility.
For further reference see Assets API. add link

# Supported Orders

When submitting crypto orders through the Orders API and the Alpaca web dashboard, Market, Limit and Stop Limit orders are supported while the supported `time_in_force` values are `gtc`, and `ioc`. We accept fractional orders as well with either `notional` or `qty` provided.
You can submit crypto orders for any supported crypto pair via API, see the below cURL POST request.
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

The above request submits a market order via API to buy 0.0001 BTC with USD (BTC/USD pair) that is good till end of day.
To learn more see orders and fractional trading.
All cryptocurrency assets are fractionable but the supported decimal points vary depending on the cryptocurrency. See Assets entity for information on fractional precisions per asset.
Note these values could change in the future.

# Crypto Market Data

You can check out the documentation and the API reference of our crypto market data.
Here we provide an example to request the latest order book data (bids and asks) for the following three coin pairs: BTC/USD, ETH/BTC, and ETH/USD.
cURL
```
`curl &#x27;https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD&#x27;`
```

JSON
```
`{
    "orderbooks": {
        "BTC/USD": {
            "a": [
                {
                    "p": 66051.621,
                    "s": 0.275033
                },
                ...
            ],
            "b": [
                {
                    "p": 65986.962,
                    "s": 0.27813
                },
                ...
            ],
            "t": "2024-07-24T07:31:01.373709495Z"
        },
        "ETH/USD": { ... }
        },
        "ETH/BTC": { ... }
    }
}`
```

Additionally, you can subscribe to real-time crypto data via Websockets. Example below leverages wscat to subscribe to BTC/USD order book.
JSON
```
`$ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action":"auth","key":"<YOUR API KEY>","secret":"<YOUR API SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe","quotes":["ETH/USD"]}
< [{"T":"subscription","trades":[],"quotes":["ETH/USD"],"orderbooks":[],"bars":[],"updatedBars":[],"dailyBars":[]}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3450.2,"as":4.3803,"t":"2024-07-24T07:38:06.88490478Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3451.1,"as":8.73823,"t":"2024-07-24T07:38:06.88493591Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88511154Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.644,"bs":8.797,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88512141Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.51,"bs":4.33,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88516355Z"}]`
```

For further reference of real-time crypto pricing data see its documentation.

# Transferring Crypto

Alpaca now offers native on-chain crypto transfers with wallets! If you have crypto trading enabled and reside in an eligible US state or international jurisdiction you can access wallets on the web dashboard via the Crypto Transfers tab.
Alpaca wallets currently support transfers for Bitcoin, Ethereum, and all Ethereum (ERC20) based tokens. To learn more on transferring crypto with Alpaca, see Crypto Wallets FAQs

# Crypto Spot Trading Fees

While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller&#x27;s posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. A maker is someone who adds liquidity, and the order gets placed on the order book.  A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.
See the below table with volume-tiered fee pricing:
Tier30D Trading Volume (USD)MakerTaker10 - 100,00015 bps25 bps2100,000 - 500,00012 bps22 bps3500,000 - 1,000,00010 bps20 bps41,000,000 - 10,000,0008 bps18 bps510,000,000 - 25,000,0005 bps15 bps625,000,000 - 50,000,0002 bps13 bps750,000,000 - 100,000,0002 bps12 bps8100,000,000+0 bps10 bps
The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples,

- Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
- Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
- Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
- Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`

To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`. See below example of CFEE object:
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

# Margin and Short Selling

Cryptocurrencies cannot be bought on margin. This means that you cannot use leverage to buy them and orders are evaluated against `non_marginable_buying_power`.
Cryptocurrencies can not be sold short.

# Trading Hours

Crypto trading is offered for 24 hours everyday and your orders will be executed throughout the day.

# Trading Limits

Currently, an order (buy or sell) must not exceed $200k in notional. This is per an order.Updated 5 months ago Trading AccountCrypto Orders- Ask AI
