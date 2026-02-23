# Independentreserve API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://www.independentreserve.com/api

[ Go to the home page](/)

  * Personal  Personal

Account types 

    * [Personal](/features/personal)
    * [Trust](/features/trust)

Solutions for 

    * [Family offices](/features/family-offices-asset-managers)
    * [High-net-worth individuals](/features/high-net-worth)

Ways to trade 

    * [API](/features/api)
    * [Bank transfer](/buy/bank-transfer)
    * [Dollar-cost averaging](/features/recurring-buy)
    * [Leveraged trading](/features/leveraged-trading)
    * [OTC (Over-the-counter)](/features/otc)
    * [SWIFT](https://www.independentreserve.com/blog/knowledge-base/how-to-deposit-nzd-and-usd-using-swift)

[Features](/features)

    * [24/7 support](/features/premium-support)
    * [Fees](/fees)
    * [Mobile app](/features/mobile-app)
    * [Multi-user](/features/multi-user)
    * [Security](/security)
    * [Wallet](/features/wallet)

  * Business  Business

Account types 

    * [Company](/features/company-accounts)
    * [Institutional](/institutions)
    * [Trust](/features/trust)

Solutions for 

    * [Asset managers](/features/family-offices-asset-managers)
    * [Family offices](/features/family-offices-asset-managers)
    * [Web 3 Builders](/features/web3-blockchain-builders)

Ways to trade 

    * [API](/features/api)
    * [Bank transfer](/buy/bank-transfer)
    * [Dollar-cost averaging](/features/recurring-buy)
    * [Leveraged trading](/features/leveraged-trading)
    * [OTC (Over-the-counter)](/features/otc)
    * [SWIFT](https://www.independentreserve.com/blog/knowledge-base/how-to-deposit-nzd-and-usd-using-swift)

[Features](/features)

    * [24/7 support](/features/premium-support)
    * [Fees](/fees)
    * [Mobile app](/features/mobile-app)
    * [Multi-user](/features/multi-user)
    * [Security](/security)
    * [Wallet](/features/wallet)

  * [ OTC  OTC ](/features/otc)
  * [ Markets  Markets ](/markets)

Currency | Price | Actions  
---|---|---  
[ Bitcoin BTC ](/market/btc "Bitcoin price USD") | USD 68,129.11 |  [Buy](/buy/bitcoin "Buy Bitcoin") [Sell](/sell/bitcoin "Sell Bitcoin")  
[ Ethereum ETH ](/market/eth "Ethereum price USD") | USD 2,010.21 |  [Buy](/buy/ethereum "Buy Ethereum") [Sell](/sell/ethereum "Sell Ethereum")  
[ Solana SOL ](/market/sol "Solana price USD") | USD 85.5924 |  [Buy](/buy/solana "Buy Solana") [Sell](/sell/solana "Sell Solana")  
[ XRP XRP ](/market/xrp "XRP price USD") | USD 1.48648 |  [Buy](/buy/xrp "Buy XRP") [Sell](/sell/xrp "Sell XRP")  
[ USD Coin USDC ](/market/usdc "USD Coin price USD") | USD 0.99350 |  [Buy](/buy/usdc "Buy USD Coin") [Sell](/sell/usdc "Sell USD Coin")  
[ Tether USD USDT ](/market/usdt "Tether USD price USD") | USD 1.00447 |  [Buy](/buy/tether "Buy Tether USD") [Sell](/sell/tether "Sell Tether USD")  
  
[View all](/markets)

  * [ Help  Help ](/help)

Getting started 

    * [Start here](/help/getting-started)
    * [Personal accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-personal-account-with-independent-reserve)
    * [Company accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-company-account)
    * [Trust accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-trust-account)

Resources 

    * [Blog](https://www.independentreserve.com/blog)
    * [Fees](/fees)
    * [Knowledge base](https://www.independentreserve.com/blog/knowledge-base)
    * [Market updates](https://www.independentreserve.com/blog/market-update)
    * [Security](/security)

Contact 

    * [Contact support](https://portal.independentreserve.com/support)
    * [Forgot password](https://portal.independentreserve.com/login/forgot-password)
    * [Media](mailto:media@independentreserve.com)
    * [Trouble logging in](https://portal.independentreserve.com/login/help-center)

  * [ About  About ](/about)

About 

    * [About us](/about)
    * [Community initiatives](/community-initiatives)
    * [Fees](/fees)
    * [News and announcements](https://www.independentreserve.com/blog/news)
    * [Security](/security)




Toggle main menu

[Log in](https://portal.independentreserve.com/login) [Create account](https://portal.independentreserve.com/register)

EN

  * [Home](/)
  * [Features](/features)
  * API



# API

## [ ](#overview)Overview 

Independent Reserve features a JSON based HTTP API that is comprised of [Public](#public-methods) and [Private](#private-methods) endpoints. 

  * All calls are made over SSL to `https://api.independentreserve.com`
  * Public methods do not require an authentication token and should be accessed via HTTP GET.
  * Private methods require a valid authentication token and are accessed via HTTP POST.
  * Ensure that the `contentType` of the your JSON POST is set to `application/json`. 
  * The client can receive a compressed response by adding header `Accept-Encoding: gzip, deflate`



We also support [WebSockets](#websockets). 

Refer to the table below for the the decimal places supported when placing orders. On Independent Reserve, a cryptocurrency is defined as a _primary currency_ , a fiat currency as a _secondary currency_. 

Currency | Code |  Order Primary Currency  
Decimal Places  |  Order Secondary Currency  
Decimal Places   
---|---|---|---  
Bitcoin  |  Xbt

### Heads Up!

For historical reasons, the API currency code for Bitcoin is `Xbt` |  8  |  2   
Ethereum  |  Eth |  8  |  2   
Solana  |  Sol |  5  |  4   
XRP  |  Xrp |  5  |  5   
USD Coin  |  Usdc |  5  |  5   
Tether USD  |  Usdt |  5  |  5   
Aave  |  Aave |  5  |  4   
Cardano  |  Ada |  5  |  5   
Macropod AUD  |  Audm |  5  |  5   
Avalanche  |  Avax |  5  |  5   
Basic Attention Token  |  Bat |  5  |  5   
Bitcoin Cash  |  Bch |  8  |  2   
Bonk  |  Bonk |  0  |  8   
Compound  |  Comp |  8  |  2   
Dai  |  Dai |  5  |  5   
Dogecoin  |  Doge |  5  |  5   
Polkadot  |  Dot |  5  |  4   
Ethereum Classic  |  Etc |  8  |  2   
The Graph  |  Grt |  5  |  5   
Hyperliquid  |  Hype |  5  |  5   
Chainlink  |  Link |  4  |  4   
Litecoin  |  Ltc |  8  |  2   
Decentraland  |  Mana |  5  |  5   
Matic  |  Matic |  5  |  5   
Maker  |  Mkr |  8  |  2   
Pudgy Penguins  |  Pengu |  5  |  5   
Pepe  |  Pepe |  0  |  8   
Render  |  Render |  5  |  5   
The Sandbox  |  Sand |  5  |  5   
Shiba Inu  |  Shib |  0  |  8   
Synthetix  |  Snx |  5  |  4   
Official Trump  |  Trump |  5  |  5   
TRON  |  Trx |  5  |  5   
Uniswap  |  Uni |  5  |  4   
dogwifhat  |  Wif |  5  |  5   
Tether Gold  |  Xaut |  6  |  2   
Stellar Lumens  |  Xlm |  5  |  5   
yearn.finance  |  Yfi |  8  |  2   
0x  |  Zrx |  5  |  5   
  
## [ ](#public-methods)Public methods 

Public methods should be accessed via HTTP GET and do not require an authentication token to be passed.

The following public API methods are available:

  * [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes)
  * [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes)
  * [GetValidLimitOrderTypes](#GetValidLimitOrderTypes)
  * [GetValidMarketOrderTypes](#GetValidMarketOrderTypes)
  * [GetValidOrderTypes](#GetValidOrderTypes)
  * [GetValidTransactionTypes](#GetValidTransactionTypes)
  * [GetNetworks](#GetNetworks)
  * [GetPrimaryCurrencyConfig2](#GetPrimaryCurrencyConfig2)
  * [GetMarketSummary](#GetMarketSummary)
  * [GetOrderBook](#GetOrderBook)
  * [GetAllOrders](#GetAllOrders)
  * [GetTradeHistorySummary](#GetTradeHistorySummary)
  * [GetRecentTrades](#GetRecentTrades)
  * [GetFxRates](#GetFxRates)
  * [GetOrderMinimumVolumes](#GetOrderMinimumVolumes)
  * [GetDepositFees](#GetDepositFees)
  * [GetFiatWithdrawalFees](#GetFiatWithdrawalFees)
  * [GetCryptoWithdrawalFees2](#GetCryptoWithdrawalFees2)



### [ ](#GetValidPrimaryCurrencyCodes)GetValidPrimaryCurrencyCodes 

Returns a list of valid primary currency codes. These are the cryptocurrencies which can be traded on Independent Reserve. 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidPrimaryCurrencyCodes

Copy

Response
    
    
    [
      "Xbt",
      "Eth",
      "Sol",
      "Xrp",
      "Usdc",
      "Usdt",
      "Aave",
      "Ada",
      "Audm",
      "Avax",
      "Bat",
      "Bch",
      "Bonk",
      "Comp",
      "Dai",
      "Doge",
      "Dot",
      "Etc",
      "Grt",
      "Hype",
      "Link",
      "Ltc",
      "Mana",
      "Matic",
      "Mkr",
      "Pengu",
      "Pepe",
      "Render",
      "Sand",
      "Shib",
      "Snx",
      "Trump",
      "Trx",
      "Uni",
      "Wif",
      "Xaut",
      "Xlm",
      "Yfi",
      "Zrx"
    ]

### [ ](#GetValidSecondaryCurrencyCodes)GetValidSecondaryCurrencyCodes 

Returns a list of valid secondary currency codes. These are the fiat currencies which are supported by Independent Reserve for trading purposes. 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidSecondaryCurrencyCodes

Copy

Response
    
    
    [
      "Aud",
      "Usd",
      "Nzd",
      "Sgd"
    ]

### [ ](#GetValidLimitOrderTypes)GetValidLimitOrderTypes 

Returns a list of valid _limit_ order types which can be placed onto the Independent Reserve exchange platform. 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidLimitOrderTypes

Copy

Response
    
    
    [
      "LimitBid",
      "LimitOffer"
    ]

### [ ](#GetValidMarketOrderTypes)GetValidMarketOrderTypes 

Returns a list of valid _market_ order types which can be placed onto the Independent Reserve exchange platform. 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidMarketOrderTypes

Copy

Response
    
    
    [
      "MarketBid",
      "MarketOffer"
    ]

### [ ](#GetValidOrderTypes)GetValidOrderTypes 

Returns a list of all valid order types which can be placed onto the Independent Reserve exchange platform. 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidOrderTypes

Copy

Response
    
    
    [
      "LimitBid",
      "LimitOffer",
      "MarketBid",
      "MarketOffer"
    ]

### [ ](#GetValidTransactionTypes)GetValidTransactionTypes 

Returns a list of valid transaction types.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetValidTransactionTypes

Copy

Response
    
    
    [
      "AccountFee",
      "Brokerage",
      "Deposit",
      "DepositFee",
      "GST",
      "ReferralCommission",
      "StatementFee",
      "Trade",
      "Withdrawal",
      "WithdrawalFee"
    ]

### [ ](#GetNetworks)GetNetworks 

Returns the set of blockchain networks in use. For more details - see [Listed tokens and contract addresses on Independent Reserve](https://www.independentreserve.com/blog/knowledge-base/listed-tokens-and-contract-addresses). 

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetNetworks

Copy

Response
    
    
    [
      "Bitcoin",
      "Ethereum",
      "BitcoinCash",
      "Litecoin",
      "XrpLedger",
      "EosIo",
      "Stellar",
      "EthereumClassic",
      "BitcoinSV",
      "Dogecoin",
      "Polkadot",
      "Cardano",
      "Solana",
      "Tron"
    ]

### [ ](#GetPrimaryCurrencyConfig2)GetPrimaryCurrencyConfig2 

Returns the configuration of all primary currencies.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetPrimaryCurrencyConfig2

Copy

Response
    
    
    [
      {
        "Currency": "Xbt",
        "Name": "Bitcoin",
        "IsTradeEnabled": true,
        "DecimalPlaces": {
          "OrderPrimaryCurrency": 8,
          "OrderSecondaryCurrency": 2
        },
        "Networks": [
          {
            "Network": "Bitcoin",
            "IsDelisted": false,
            "IsDepositEnabled": true,
            "IsWithdrawalEnabled": true
          }
        ]
      },
      {
        "Currency": "Usdc",
        "Name": "USD Coin",
        "IsTradeEnabled": true,
        "DecimalPlaces": {
          "OrderPrimaryCurrency": 5,
          "OrderSecondaryCurrency": 5
        },
        "Networks": [
          {
            "Network": "Ethereum",
            "IsDelisted": false,
            "IsDepositEnabled": true,
            "IsWithdrawalEnabled": true
          },
          {
            "Network": "Solana",
            "IsDelisted": false,
            "IsDepositEnabled": false,
            "IsWithdrawalEnabled": false
          }
        ]
      }
    ]

#### Return value descriptions

  * **IsTradeEnabled** \- Indicates whether trading is temporarily enabled/disabled
  * **DecimalPlaces.OrderPrimaryCurrency** \- Number of decimal places accepted for order volume when denominated in primary currency 
  * **DecimalPlaces.OrderSecondaryCurrency** \- Number of decimal places accepted for price denominated in secondary currency 
  * **Networks** \- Array of blockchain networks that this currency can be deposited/withdrawn to
  * **Networks.Network** \- The blockchain network these properties apply to
  * **Networks.IsDelisted** \- When set to true, a permanent delisting has occurred. Only withdrawals are allowed, no further deposits or trading may occur. 
  * **Networks.IsDepositEnabled** \- Indicates whether deposits are temporarily enabled/disabled
  * **Networks.IsWithdrawalEnabled** \- Indicates whether withdrawals are temporarily enabled/disabled



### [ ](#GetMarketSummary)GetMarketSummary 

Returns a current snapshot of the Independent Reserve market for a given currency pair.

#### Parameters

  * **primaryCurrencyCode** \- The cryptocurrency for which to retrieve market summary. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency in which to retrieve market summary. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 



#### Notes

  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 



GET

https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd

Copy

Response
    
    
    {
      "DayHighestPrice": 45005.12,
      "DayLowestPrice": 43418.84,
      "DayAvgPrice": 44211.98,
      "DayVolumeXbt": 45.68239145,
      "DayVolumeXbtInSecondaryCurrrency": 0.2355363,
      "CurrentLowestOfferPrice": 44763.99,
      "CurrentHighestBidPrice": 44345.75,
      "LastPrice": 44496.56,
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd",
      "CreatedTimestampUtc": "2022-02-10T09:34:05.2287498Z"
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- UTC timestamp of when the market summary was generated 
  * **CurrentHighestBidPrice** \- Current highest bid on order book 
  * **CurrentLowestOfferPrice** \- Current lowest offer on order book 
  * **DayAvgPrice** \- Weighted average traded price over last 24 hours 
  * **DayHighestPrice** \- Highest traded price over last 24 hours 
  * **DayLowestPrice** \- Lowest traded price over last 24 hours 
  * **DayVolumeXbt** \- Volume of primary currency traded in last 24 hours 
  * **DayVolumeXbtInSecondaryCurrrency** \- Volume of primary currency traded in last 24 hours for chosen secondary currency 
  * **LastPrice** \- Last traded price
  * **PrimaryCurrencyCode** \- The primary currency being summarised 
  * **SecondaryCurrencyCode** \- The secondary currency being used for pricing 



### [ ](#GetOrderBook)GetOrderBook 

Returns the Order Book for a given currency pair.

#### Parameters

  * **primaryCurrencyCode** \- The cryptocurrency for which to retrieve order book. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency in which to retrieve order book. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **maxDepthVolume** \- Limit the results to a maximum cumulated volume. This is an optional parameter. 
  * **maxDepthValue** \- Limit the results to a maximum value (price * volume). This is an optional parameter. 



#### Notes

  * If both _maxDepthVolume_ and _maxDepthValue_ parameters are specified, the returned set is the upper limit of either one. 
  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 
  * If you wish to retrieve order guids for each order, please use the [GetAllOrders](#GetAllOrders) method. 



GET

https://api.independentreserve.com/Public/GetOrderBook?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd

Copy

Response
    
    
    {
      "BuyOrders": [
        {
          "OrderType": "LimitBid",
          "Price": 497.02,
          "Volume": 0.01
        },
        {
          "OrderType": "LimitBid",
          "Price": 490,
          "Volume": 1
        }
      ],
      "SellOrders": [
        {
          "OrderType": "LimitOffer",
          "Price": 500,
          "Volume": 1
        },
        {
          "OrderType": "LimitOffer",
          "Price": 505,
          "Volume": 1
        }
      ],
      "CreatedTimestampUtc": "2022-08-05T06:42:11.3032208Z",
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd"
    }

#### Return value descriptions

  * **BuyOrders** \- List of all Buy Orders on order book 
    * **OrderType** \- Type of order
    * **Price** \- Order price in secondary currency
    * **Volume** \- Order volume in primary currency
  * **SellOrders** \- List of all Sell Orders on order book
  * **CreatedTimestampUtc** \- UTC timestamp of when the order book was generated 
  * **PrimaryCurrencyCode** \- The primary currency being shown 
  * **SecondaryCurrencyCode** \- The secondary currency being used for pricing 



### [ ](#GetAllOrders)GetAllOrders 

Returns the Order Book for a given currency pair including order identifiers.

#### Parameters

  * **primaryCurrencyCode** \- The cryptocurrency for which to retrieve order book. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency in which to retrieve order book. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **maxDepthVolume** \- Limit the results to a maximum cumulated volume. This is an optional parameter. 
  * **maxDepthValue** \- Limit the results to a maximum value (price * volume). This is an optional parameter. 



#### Notes

  * If both _maxDepthVolume_ and _maxDepthValue_ parameters are specified, the returned set is the upper limit of either one. 
  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 



GET

https://api.independentreserve.com/Public/GetAllOrders?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd

Copy

Response
    
    
    {
      "BuyOrders": [
        {
          "Guid": "78c52285-61de-4ccb-914e-d86db9fb498d",
          "Price": 497.02,
          "Volume": 0.01
        },
        {
          "Guid": "b0ae2cde-cefb-451d-8c65-92082e062856",
          "Price": 490,
          "Volume": 1
        }
      ],
      "SellOrders": [
        {
          "Guid": "9a32ae71-391e-4a21-8817-603472d75342",
          "Price": 500,
          "Volume": 1
        },
        {
          "Guid": "8ee0209f-fd46-4d90-9eed-ab475485e157",
          "Price": 505,
          "Volume": 1
        }
      ],
      "CreatedTimestampUtc": "2022-08-05T06:42:11.3032208Z",
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd"
    }

#### Return value descriptions

  * **BuyOrders** \- List of all Buy Orders on order book 
    * **Guid** \- Unique order identifier
    * **Price** \- Order price in secondary currency
    * **Volume** \- Order volume in primary currency
  * **SellOrders** \- List of all Sell Orders on order book
  * **CreatedTimestampUtc** \- UTC timestamp of when the order book was generated 
  * **PrimaryCurrencyCode** \- The primary currency being shown 
  * **SecondaryCurrencyCode** \- The secondary currency being used for pricing 



### [ ](#GetTradeHistorySummary)GetTradeHistorySummary 

Returns summarised historical trading data for a given currency pair. Data is summarised into 1 hour intervals. 

#### Parameters

  * **primaryCurrencyCode** \- The cryptocurrency for which to retrieve trade history. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency in which to retrieve trade history. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **numberOfHoursInThePastToRetrieve** \- How many past hours of historical summary data to retrieve (maximum is **240**) 



#### Notes

  * This method caches return values for 30 minutes. Calling it more than once per 30 minutes will result in cached data being returned. 



GET

https://api.independentreserve.com/Public/GetTradeHistorySummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd&numberOfHoursInThePastToRetrieve=24

Copy

Response
    
    
    {
      "CreatedTimestampUtc ": "2022-08-05T09:02:57.5440691Z",
      "HistorySummaryItems": [
        {
          "AverageSecondaryCurrencyPrice": 510,
          "ClosingSecondaryCurrencyPrice": 510,
          "StartTimestampUtc": "2022-08-04T09:00:00Z",
          "EndTimestampUtc": "2022-08-04T10:00:00Z",
          "HighestSecondaryCurrencyPrice": 510,
          "LowestSecondaryCurrencyPrice": 510,
          "NumberOfTrades": 0,
          "OpeningSecondaryCurrencyPrice": 510,
          "PrimaryCurrencyVolume": 0,
          "SecondaryCurrencyVolume": 0
        }
      ],
      "NumberOfHoursInThePastToRetrieve": 1,
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd"
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- TC timestamp of when the data was generated 
  * **HistorySummaryItems** \- List of hourly summary blocks 
    * **AverageSecondaryCurrencyPrice** \- Deprecated, not used 
    * **ClosingSecondaryCurrencyPrice** \- Last traded price in hour 
    * **StartTimestampUtc** \- UTC Start time of hour
    * **EndTimestampUtc** \- UTC End time of hour
    * **HighestSecondaryCurrencyPrice** \- Highest traded price during hour 
    * **LowestSecondaryCurrencyPrice** \- Lowest traded price during hour 
    * **NumberOfTrades** \- umber of trades executed during hour 
    * **OpeningSecondaryCurrencyPrice** \- Opening traded price at start of hour 
    * **PrimaryCurrencyVolume** \- Volume of primary currency trade during hour 
    * **SecondaryCurrencyVolume** \- Deprecated, not used
  * **NumberOfHoursInThePastToRetrieve** \- Number of past hours being returned 
  * **PrimaryCurrencyCode** \- The primary currency being shown 
  * **SecondaryCurrencyCode** \- The secondary currency being used for pricing 



### [ ](#GetRecentTrades)GetRecentTrades 

Returns a list of most recently executed trades for a given currency pair.

#### Parameters

  * **primaryCurrencyCode** \- The cryptocurrency for which to retrieve recent trades. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency in which to retrieve recent trades. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **numberOfRecentTradesToRetrieve** \- How many recent trades to retrieve (maximum is **50**) 



#### Notes

  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 



GET

https://api.independentreserve.com/Public/GetRecentTrades?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd&numberOfRecentTradesToRetrieve=10

Copy

Response
    
    
    {
      "CreatedTimestampUtc": "2023-08-05T09:14:39.4830696Z",
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd",
      "Trades": [
        {
          "TradeGuid": "593e609d-041a-4f46-a41d-2cb8e908973f",
          "Taker": "Bid",
          "PrimaryCurrencyAmount": 1,
          "SecondaryCurrencyTradePrice": 27299.23,
          "TradeTimestampUtc": "2023-07-31T10:34:05.935412Z"
        },
        {
          "TradeGuid": "593effff-041a-4f46-a41d-2cb8e908973g",
          "Taker": "Offer",
          "PrimaryCurrencyAmount": 0.01,
          "SecondaryCurrencyTradePrice": 27300.12,
          "TradeTimestampUtc": "2023-07-31T10:33:24.8458426Z"
        }
      ]
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- TC timestamp of when the data was generated 
  * **PrimaryCurrencyCode** \- The primary currency being shown 
  * **SecondaryCurrencyCode** \- The secondary currency being used for pricing 
  * **Trades** \- List of individual trades 
    * **TradeGuid** \- Unique identifier of the trade 
    * **Taker** \- The order side that was the taker. Possible values are `Bid`, `Offer`
    * **PrimaryCurrencyAmount** \- Amount traded in primary currency 
    * **SecondaryCurrencyTradePrice** \- Price of trade in secondary currency 
    * **TradeTimestampUtc** \- UTC timestamp of trade



### [ ](#GetFxRates)GetFxRates 

Returns a list of exchange rates used by Independent Reserve when depositing funds or withdrawing funds from accounts. 

This method does not take any parameters.

#### Notes

  * The rates represent the amount of Currency Code B that can be bought with 1 unit of Currency Code A.
  * This method caches return values for 1 minute. Calling it more than once per minute will result in cached data being returned. 



GET

https://api.independentreserve.com/Public/GetFxRates

Copy

Response
    
    
    [
      {
        "CurrencyCodeA": "Aud",
        "CurrencyCodeB": "Usd",
        "Rate": 0.8683
      },
      {
        "CurrencyCodeA": "Usd",
        "CurrencyCodeB": "Aud",
        "Rate": 1.1517
      }
    ]

### [ ](#GetOrderMinimumVolumes)GetOrderMinimumVolumes 

Returns a list of minimum allowed volumes for orders.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetOrderMinimumVolumes

Copy

Response
    
    
    {
      "Xbt": 0.0001,
      "Bch": 0.001,
      "Eth": 0.001,
      "Ltc": 0.01,
      "Xrp": 1,
      "Omg": 0.1,
      "Zrx": 1,
      "Eos": 0.1,
      "Xlm": 10,
      "Bat": 1,
      "Usdt": 1,
      "Etc": 0.01,
      "Pmgt": 0.001,
      "Link": 0.1,
      "Usdc": 1,
      "Mkr": 0.001,
      "Dai": 1,
      "Comp": 0.001,
      "Snx": 0.1,
      "Yfi": 0.0001,
      "Aave": 0.01,
      "Grt": 1,
      "Dot": 0.1,
      "Uni": 0.1,
      "Ada": 1,
      "Matic": 0.1,
      "Doge": 1
    }

### [ ](#GetDepositFees)GetDepositFees 

Returns the fee schedule for fiat deposits. Crypto deposits do not incur fees.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetDepositFees

Copy

Response
    
    
    [
      {
        "DepositType": "Swift",
        "FreeThreshold": 5000,
        "Fee": {
          "Fixed": 15,
          "Percentage": null
        }
      },
      {
        "DepositType": "Eft",
        "FreeThreshold": 100,
        "Fee": {
          "Fixed": 0.99,
          "Percentage": null
        }
      },
      {
        "DepositType": "Osko",
        "FreeThreshold": 1000,
        "Fee": {
          "Fixed": 2.5,
          "Percentage": null
        }
      },
      {
        "DepositType": "SGD-FAST",
        "FreeThreshold": null,
        "Fee": {
          "Fixed": 0,
          "Percentage": 0.55
        }
      }
    ]

#### Return value descriptions

  * **DepositType** \- The method of deposit
  * **FreeThreshold** \- An amount below this threshold will incur a deposit fee. When null, the fee is always applied. 
  * **Fee** \- Deposit fee which will be deducted from deposit amount when under threshold. Denominated in the deposit currency. 
    * **Fixed** \- Fixed fee amount
    * **Percentage** \- Percentage fee



### [ ](#GetFiatWithdrawalFees)GetFiatWithdrawalFees 

Returns the fee schedule for all withdrawals.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetFiatWithdrawalFees

Copy

Response
    
    
    [
      {
        "WithdrawalType": "Wire Transfer",
        "MinimumAmount": 50,
        "CurrencyCode": "Aud",
        "Fee": {
          "Fixed": 0,
          "Percentage": null
        }
      },
      {
        "WithdrawalType": "Wire Transfer",
        "MinimumAmount": 50,
        "CurrencyCode": "Usd",
        "Fee": {
          "Fixed": 20,
          "Percentage": null
        }
      },
      {
        "WithdrawalType": "Osko",
        "MinimumAmount": 0.01,
        "CurrencyCode": "Aud",
        "Fee": {
          "Fixed": 1.5,
          "Percentage": null
        }
      },
      {
        "WithdrawalType": "SGD-FAST",
        "MinimumAmount": 0.01,
        "CurrencyCode": "Sgd",
        "Fee": {
          "Fixed": 0,
          "Percentage": 0.55
        }
      }
    ]

#### Return value descriptions

  * **WithdrawalType** \- The withdrawal method
  * **MinimumAmount** \- The minimum withdrawal amount
  * **CurrencyCode** \- The withdrawal currency
  * **Fee** \- Withdrawal fee which will be charged from your account. 
    * **Fixed** \- Fixed fee amount
    * **Percentage** \- Percentage fee



### [ ](#GetCryptoWithdrawalFees2)GetCryptoWithdrawalFees2 

Returns the fee schedule for crypto withdrawals.

This method does not take any parameters.

GET

https://api.independentreserve.com/Public/GetCryptoWithdrawalFees2

Copy

Response
    
    
    [
      {
        "Fee": 0.00001,
        "Network": "Bitcoin",
        "Currency": "Xbt"
      },
      {
        "Fee": 2,
        "Network": "Tron",
        "Currency": "Usdt"
      },
      {
        "Fee": 5,
        "Network": "Ethereum",
        "Currency": "Usdt"
      }
    ]

#### Return value descriptions

  * **Fee** \- Withdrawal fee for the currency over the specified **Network**. Denominated in the **Currency**. 



## [ ](#authentication)Authentication 

All private API methods require authentication. All method parameters (except signature) are required to authenticate a request. There are three additional parameters which should be passed to private API methods: 

  * API Key
  * Nonce or Expiry
  * Signature



### [ ](#authentication-api-key)API key 

To generate an API Key, go to the Settings page, "API Keys" and then "Generate API Key". Select the level of access. Ensure that you the lowest level of access required for your usage. 

When creating an API key, we strongly recommend restricting it to a set of whitelisted IP addresses. We will reject any usage of the key from an IP address not whitelisted. 

For security reasons, API keys created without IP whitelisting will be automatically disabled if left unused for 6 months. 

### [ ](#authentication-nonce)Nonce or Expiry 

Either specify a `nonce` or `expiry`. One of these parameters must be specified, but not both. Using an expiry has the advantage of not needing to synchronise a nonce across multiple threads. 

When using nonce, it should be a 64-bit unsigned integer. The nonce must increase with each request made to the API. For example, if the nonce is set to 1 in the first request, it must be set to at least 2 in the subsequent request. It is not necessary to start with 1. A common practice is to use Unix time for this parameter. 

When using expiry, it should be a Unix UTC timestamp in seconds. For example 2024-03-02T01:23:45Z has Unix timestamp 1709342625. The server will reject any request with an expiry in the past or more than 30 seconds into the future. Additionally, the API key must have been restricted to at least one IP Address at the time of creation. 

Whichever parameter is chosen, it must be used to form the signature.

### [ ](#authentication-signature)Signature 

Signature is a HMAC-SHA256 encoded message. The message is comma-separated string containing the API method URL, and a comma separated list of all method parameters (except signature) in the form: "parameterName=parameterValue". The HMAC-SHA256 code must be generated using the API Secret that was generated with your API key. This code must be converted to it's hexadecimal representation. 

#### Notes

To avoid typical errors please ensure that in your code

  * the parameter names are spelled correctly;
  * the parameter values are same in signature input string and message body;
  * the parameter sequence used to create the signature must match the method documentation.



Example (Python)
    
    
    import time
    import requests
    import hmac
    import hashlib
    import json
    from collections import OrderedDict
    
    url = 'https://api.independentreserve.com/Private/GetOpenOrders'
    
    key = 'api_key'
    
    secret = 'api_secret'
    
    currentTime = int(time.time())
    nonce = currentTime
    expiry = currentTime + 3 # Expire in three seconds
    
    # make sure that parameter order is correct as specified in method documentation
    parameters = [
        url,
        'apiKey=' + key,
        'nonce=' + str(nonce),
        'primaryCurrencyCode=Xbt',
        'secondaryCurrencyCode=Usd',
        'pageIndex=1',
        'pageSize=10'
    ]
    
    message = ','.join(parameters)
    
    signature = hmac.new(
        secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256).hexdigest().upper()
    
    # make sure this collection ordered in the same way as parameters
    data = OrderedDict([
        ('apiKey', key),
        ('nonce', nonce),  # Either nonce or expiry here
        ('signature', str(signature)),
        ('primaryCurrencyCode', 'Xbt'),
        ('secondaryCurrencyCode', 'Usd'),
        ('pageIndex', 1),
        ('pageSize', 10)])
    
    headers = {'Content-Type': 'application/json'}
    
    r = requests.post(url, data=json.dumps(data, sort_keys=False), headers=headers)
    
    print(r.content)

## [ ](#private-methods)Private methods 

Private methods should be accessed via HTTP POST and require a valid authentication token to be passed. Parameters for all private methods, including the three parameters to authenticate the call, must be posted as a JSON object. 

The table below lists the private API methods along with the `API Role` required to access the method. 

The Restricted Withdrawals role can only withdraw to whitelisted addresses and bank accounts. To whitelist an address or a bank account, please first execute a withdrawal using the web portal or alternatively for cryptocurrency, add the address to the address book. 

You can request via [Support](https://portal.independentreserve.com/support) to restrict API key usage to a specific IP address. 

Method  |  API Roles   
---|---  
[GetOpenOrders](#GetOpenOrders) |  Full Access Trade Read Only Restricted Withdrawals  
[GetClosedOrders](#GetClosedOrders) |  Full Access Trade Read Only Restricted Withdrawals  
[GetClosedFilledOrders](#GetClosedFilledOrders) |  Full Access Trade Read Only Restricted Withdrawals  
[GetOrderDetails](#GetOrderDetails) |  Full Access Trade Read Only Restricted Withdrawals  
[GetAccounts](#GetAccounts) |  Full Access Trade Read Only Restricted Withdrawals  
[GetTransactions](#GetTransactions) |  Full Access Trade Read Only Restricted Withdrawals  
[GetFiatBankAccounts](#GetFiatBankAccounts) |  Full Access Trade Read Only Restricted Withdrawals  
[GetDigitalCurrencyDepositAddress2](#GetDigitalCurrencyDepositAddress2) |  Full Access Trade Read Only Restricted Withdrawals  
[GetDigitalCurrencyDepositAddresses2](#GetDigitalCurrencyDepositAddresses2) |  Full Access Trade Read Only Restricted Withdrawals  
[GetTrades](#GetTrades) |  Full Access Trade Read Only Restricted Withdrawals  
[GetTradesByOrder](#GetTradesByOrder) |  Full Access Trade Read Only Restricted Withdrawals  
[GetBrokerageFees](#GetBrokerageFees) |  Full Access Trade Read Only Restricted Withdrawals  
[GetDigitalCurrencyWithdrawal](#GetDigitalCurrencyWithdrawal) |  Full Access Trade Read Only Restricted Withdrawals  
[GetFiatWithdrawal](#GetFiatWithdrawal) |  Full Access Trade Read Only Restricted Withdrawals  
[GetDepositLimits](#GetDepositLimits) |  Full Access Trade Read Only Restricted Withdrawals  
[GetWithdrawalLimits](#GetWithdrawalLimits) |  Full Access Trade Read Only Restricted Withdrawals  
[PlaceLimitOrder](#PlaceLimitOrder) |  Full Access Trade Restricted Withdrawals  
[PlaceMarketOrder](#PlaceMarketOrder) |  Full Access Trade Restricted Withdrawals  
[CancelOrder](#CancelOrder) |  Full Access Trade Restricted Withdrawals  
[CancelOrders](#CancelOrders) |  Full Access Trade Restricted Withdrawals  
[SynchDigitalCurrencyDepositAddressWithBlockchain](#SynchDigitalCurrencyDepositAddressWithBlockchain) |  Full Access Trade Restricted Withdrawals  
[WithdrawFiatCurrency](#WithdrawFiatCurrency) |  Full Access Restricted Withdrawals  
[WithdrawCrypto](#WithdrawCrypto) |  Full Access Restricted Withdrawals  
  
### [ ](#GetOpenOrders)GetOpenOrders 

Retrieves a page of a specified size with your currently Open and Partially Filled orders.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The primary currency of orders. This is an optional parameter. 
  * **secondaryCurrencyCode** \- The secondary currency of orders. This is an optional parameter. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 100. 



POST

https://api.independentreserve.com/Private/GetOpenOrders

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Usd",
      "pageIndex": 1,
      "pageSize": 25
    }

Response
    
    
    {
      "PageSize": 25,
      "TotalItems": 2,
      "TotalPages": 1,
      "Data": [
        {
          "CreatedTimestampUtc": "2025-06-02T04:17:58.9621625+00:00",
          "OrderType": "LimitOffer",
          "Volume": 0.5,
          "Outstanding": 0.5,
          "Price": 200000,
          "AvgPrice": 200000,
          "Value": 100000,
          "Status": "Open",
          "OrderGuid": "c65214ed-d7e7-4cdd-a8a1-4deb29841537",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 0.5,
            "Outstanding": 0.5,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-1",
          "TimeInForce": "Gtc"
        },
        {
          "CreatedTimestampUtc": "2025-06-02T04:18:21.6877157+00:00",
          "OrderType": "LimitBid",
          "Volume": 500,
          "Outstanding": 500,
          "Price": 0.5,
          "AvgPrice": 0.5,
          "Value": 250,
          "Status": "Open",
          "OrderGuid": "755bed0e-f8fb-4854-9f4a-8144f6b9b2cb",
          "PrimaryCurrencyCode": "Xrp",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 500,
            "Outstanding": 500,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-2",
          "TimeInForce": "Gtc"
        }
      ]
    }

#### Return value descriptions

  * **PageSize** \- Number of orders shown per page
  * **TotalItems** \- Total number of open orders
  * **TotalPages** \- Total number of pages
  * **Data** \- List of all open orders 
    * **AvgPrice** \- Average price for all trades executed for the order 
    * **CreatedTimestampUtc** \- UTC timestamp of when order was created 
    * **FeePercent** \- Brokerage fee
    * **OrderGuid** \- Unique identifier of the order
    * **OrderType** \- Type of order
    * **Outstanding** \- Unfilled volume still outstanding on this order 
    * **Price** \- Order limit price in secondary currency
    * **PrimaryCurrencyCode** \- Primary currency of order
    * **SecondaryCurrencyCode** \- Secondary currency of order 
    * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
    * **Value** \- The value of the order, denominated in secondary currency 
    * **Original**
      * **Volume** \- The original volume ordered
      * **Outstanding** \- Unfilled volume outstanding on this order in original currency 
      * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#GetClosedOrders)GetClosedOrders 

Retrieves a page of a specified size with your Closed and Cancelled orders.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The primary currency of orders. This is an optional parameter. 
  * **secondaryCurrencyCode** \- The secondary currency of orders. This is an optional parameter. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 5000. 
  * **fromTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2023-08-01T08:00:00Z`, from which you want to retrieve orders. This is an optional parameter. 
  * **includeTotals** \- Defaults to `true` for backward compatibility. When set to `false`, response time is improved and the `TotalItems` and `TotalPages` properties are returned as `-1`. 



#### Notes

  * Only recently cancelled orders will be returned; cancelled orders are regularly purged from history. 



POST

https://api.independentreserve.com/Private/GetClosedOrders

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Usd",
      "includeTotals": false,
      "pageIndex": 1,
      "pageSize": 25,
      "fromTimestampUtc": "2023-08-01T08:00:00Z"
    }

Response
    
    
    {
      "PageSize": 25,
      "TotalItems": 50,
      "TotalPages": 2,
      "Data": [
        {
          "CreatedTimestampUtc": "2025-06-02T04:59:46.4025043+00:00",
          "OrderType": "MarketOffer",
          "Volume": 0.01,
          "Outstanding": 0,
          "Price": null,
          "AvgPrice": 28648.14,
          "Value": 286.4814,
          "Status": "Filled",
          "OrderGuid": "d16287b2-03f4-4bfc-8837-a18e9fef7e65",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 0.01,
            "Outstanding": 0,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-4"
        },
        {
          "CreatedTimestampUtc": "2025-06-02T04:20:43.4806825+00:00",
          "OrderType": "LimitBid",
          "Volume": 0.01,
          "Outstanding": 0,
          "Price": 101000,
          "AvgPrice": 38664.76,
          "Value": 386.6476,
          "Status": "Filled",
          "OrderGuid": "aeeb8129-1a53-44c8-9f56-26341713ccf3",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 0.01,
            "Outstanding": 0,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-3",
          "TimeInForce": "Gtc"
        }
      ]
    }

#### Return value descriptions

  * **PageSize** \- Number of orders shown per page
  * **TotalItems** \- Total number of closed orders
  * **TotalPages** \- Total number of pages
  * **Data** \- List of closed and recently cancelled orders 
    * **AvgPrice** \- Average price for all trades executed for the order 
    * **CreatedTimestampUtc** \- UTC timestamp of when order was created 
    * **FeePercent** \- Brokerage fee
    * **OrderGuid** \- Unique identifier of the order
    * **OrderType** \- Type of order,
    * **Outstanding** \- Unfilled volume still outstanding on this order 
    * **Price** \- Order limit price in secondary currency
    * **PrimaryCurrencyCode** \- Primary currency of order
    * **SecondaryCurrencyCode** \- Secondary currency of order 
    * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
    * **Value** \- The value of the order, denominated in secondary currency 
    * **Volume** \- The original volume ordered
    * **Original**
      * **Volume** \- The original volume ordered
      * **Outstanding** \- Unfilled volume outstanding on this order in original currency 
      * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#GetClosedFilledOrders)GetClosedFilledOrders 

Retrieves a page of a specified size with your Closed orders which have had some or all of their outstanding volume filled. 

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The primary currency of orders. This is an optional parameter. 
  * **secondaryCurrencyCode** \- The secondary currency of orders. This is an optional parameter. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 5000. 
  * **fromTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2023-08-01T08:00:00Z`, from which you want to retrieve orders. This is an optional parameter. 
  * **includeTotals** \- Defaults to `true` for backward compatibility. When set to `false`, response time is improved and the `TotalItems` and `TotalPages` properties are returned as `-1`. 



POST

https://api.independentreserve.com/Private/GetClosedFilledOrders

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Usd",
      "includeTotals": false,
      "pageIndex": 1,
      "pageSize": 25
    }

Response
    
    
    {
      "PageSize": 25,
      "TotalItems": 50,
      "TotalPages": 2,
      "Data": [
        {
          "CreatedTimestampUtc": "2025-06-02T04:59:46.4025043+00:00",
          "OrderType": "MarketOffer",
          "Volume": 0.01,
          "Outstanding": 0,
          "Price": null,
          "AvgPrice": 28648.14,
          "Value": 286.4814,
          "Status": "Filled",
          "OrderGuid": "d16287b2-03f4-4bfc-8837-a18e9fef7e65",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 0.01,
            "Outstanding": 0,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-4"
        },
        {
          "CreatedTimestampUtc": "2025-06-02T04:20:43.4806825+00:00",
          "OrderType": "LimitBid",
          "Volume": 0.01,
          "Outstanding": 0,
          "Price": 101000,
          "AvgPrice": 38664.76,
          "Value": 386.6476,
          "Status": "Filled",
          "OrderGuid": "aeeb8129-1a53-44c8-9f56-26341713ccf3",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Aud",
          "FeePercent": 0.005,
          "Original": {
            "Volume": 0.01,
            "Outstanding": 0,
            "VolumeCurrencyType": "Primary"
          },
          "ClientId": "my-client-id-3",
          "TimeInForce": "Gtc"
        }
      ]
    }

#### Return value descriptions

  * **PageSize** \- Number of orders shown per page
  * **TotalItems** \- Total number of closed orders
  * **TotalPages** \- Total number of pages
  * **Data** \- List of closed and partially filled orders 
    * **AvgPrice** \- Average price for all trades executed for the order 
    * **CreatedTimestampUtc** \- UTC timestamp of when order was created 
    * **FeePercent** \- Brokerage fee
    * **OrderGuid** \- Unique identifier of the order
    * **OrderType** \- Type of order
    * **Outstanding** \- Unfilled volume still outstanding on this order 
    * **Price** \- Order limit price in secondary currency
    * **PrimaryCurrencyCode** \- Primary currency of order
    * **SecondaryCurrencyCode** \- Secondary currency of order 
    * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
    * **Value** \- The value of the order, denominated in secondary currency 
    * **Volume** \- The original volume ordered
    * **Original**
      * **Volume** \- The original volume ordered
      * **Outstanding** \- Unfilled volume outstanding on this order in original currency 
      * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#GetOrderDetails)GetOrderDetails 

Retrieves details about a single order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **orderGuid** \- The guid of the order^.
  * **clientId** \- The clientId that was supplied when placing an order ^. 



^ Only one of these parameters may be supplied at a time 

POST

https://api.independentreserve.com/Private/GetOrderDetails

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "orderGuid": "c7347e4c-b865-4c94-8f74-d934d4b0b177",
      "clientId": null
    }

Response
    
    
    {
      "OrderGuid": "c7347e4c-b865-4c94-8f74-d934d4b0b177",
      "CreatedTimestampUtc": "2022-09-23T12:39:34.3817763Z",
      "Type": "MarketBid",
      "VolumeOrdered": 5,
      "VolumeFilled": 5,
      "Price": null,
      "AvgPrice": 100,
      "ReservedAmount": 0,
      "Status": "Filled",
      "PrimaryCurrencyCode": "Xbt",
      "SecondaryCurrencyCode": "Usd",
      "ClientId": "bd9fde9d-aec7-4b81-a5f0-eb88b2e75723"
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- UTC timestamp of when order was created 
  * **OrderGuid** \- Unique identifier of the order
  * **Type** \- Type of order
  * **VolumeOrdered** \- The original volume ordered
  * **VolumeFilled** \- Volume already filled on this order
  * **Price** \- Order limit price in secondary currency
  * **AvgPrice** \- Average price for all trades executed for the order 
  * **ReservedAmount** \- The amount of funds reserved in your account by this order 
  * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
  * **PrimaryCurrencyCode** \- Primary currency of order
  * **SecondaryCurrencyCode** \- Secondary currency of order
  * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#GetAccounts)GetAccounts 

Retrieves information about your Independent Reserve accounts in crypto and fiat currencies.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 



POST

https://api.independentreserve.com/Private/GetAccounts

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}"
    }

Response
    
    
    [
      {
        "AccountGuid": "66dcac65-bf07-4e68-ad46-838f51100424",
        "AccountStatus": "Active",
        "AvailableBalance": 45.334,
        "CurrencyCode": "Xbt",
        "TotalBalance": 46.81
      },
      {
        "AccountGuid": "49994921-60ec-411e-8a78-d0eba078d5e9",
        "AccountStatus": "Active",
        "AvailableBalance": 14345.53,
        "CurrencyCode": "Usd",
        "TotalBalance": 15784.07
      }
    ]

#### Return value descriptions

  * **AccountGuid** \- Unique identifier of account
  * **AccountStatus** \- Status of account
  * **AvailableBalance** \- Available balance in account to trade or withdraw 
  * **CurrencyCode** \- Currency of account
  * **TotalBalance** \- Total balance in account



### [ ](#GetTransactions)GetTransactions 

Retrieves a page of a specified size containing all transactions made on an account.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **accountGuid** \- The Guid of your Independent Reserve account. You can retrieve information about your accounts via the [GetAccounts](#GetAccounts) method. 
  * **fromTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2022-08-01T08:00:00Z`, from which you want to retrieve transactions. This is an optional parameter. 
  * **toTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2022-08-07T08:00:00Z`, until which you want to retrieve transactions. This is an optional parameter. 
  * **txTypes** \- Array of transaction types for filtering. This is an optional parameter. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 5000. 
  * **includeTotals** \- Defaults to `true` for backward compatibility. When set to `false`, response time is improved and the `TotalItems` and `TotalPages` properties are returned as `-1`. 



#### Notes

Array parameters should be serialized for signature input as comma-separated value list.   
**Example:** `txTypes=Brokerage,Trade`

POST

https://api.independentreserve.com/Private/GetTransactions

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "accountGuid": "49994921-60ec-411e-8a78-d0eba078d5e9",
      "fromTimestampUtc": "2024-03-01T09:00:00Z",
      "toTimestampUtc": null,
      "txTypes": [
        "Brokerage",
        "Trade"
      ],
      "includeTotals": false,
      "pageIndex": 1,
      "pageSize": 25
    }

Response
    
    
    {
      "PageSize": 25,
      "TotalItems": 6,
      "TotalPages": 1,
      "Data": [
        {
          "TransactionGuid": "27e6cbc9-e9cc-4725-882f-690cd6641ff8",
          "Balance": 199954.27,
          "BitcoinTransactionId": null,
          "BitcoinTransactionOutputIndex": null,
          "EthereumTransactionId": null,
          "Comment": null,
          "CreatedTimestampUtc": "2024-03-03T05:33:48.2354125Z",
          "Credit": null,
          "CurrencyCode": "Usd",
          "Debit": 6.98,
          "SettleTimestampUtc": "2024-03-03T05:36:24.5532653Z",
          "Status": "Confirmed",
          "Type": "Brokerage",
          "CorrelationId": "27e6cbc9-e9cc-4725-882f-690cd6641ff0"
        },
        {
          "CorrelationId": "bcbab3b4-87df-4f6a-9891-f24d358a7e5d",
          "BitcoinTransactionId": null,
          "BitcoinTransactionOutputIndex": null,
          "EthereumTransactionId": null,
          "Network": "XrpLedger",
          "TransactionGuid": "13a012e8-1c00-4603-9136-32b5f268815c",
          "SettleTimestampUtc": null,
          "CreatedTimestampUtc": "2024-12-04T23:47:08.7551132+00:00",
          "Type": "Withdrawal",
          "Status": "Pending",
          "CurrencyCode": "Xrp",
          "Credit": null,
          "Debit": 50,
          "Comment": "Withdrawing to rNxBErJ7z5SveBaC9htqaEK2P61Gs56EcW"
        }
      ]
    }

#### Return value descriptions

  * **TransactionGuid** \- Unique identifier of the transaction 
  * **Balance** \- Running balance in account
  * **BitcoinTransactionId** \- Related Bitcoin network transaction 
  * **BitcoinTransactionOutputIndex** \- Related Bitcoin network transaction output index 
  * **Network** \- The blockchain network this occurred on (where applicable) 
  * **EthereumTransactionId** \- Related Ethereum network transaction 
  * **Comment** \- Comments related to transaction
  * **CreatedTimestampUtc** \- UTC created timestamp of transaction 
  * **Credit** \- Credit amount
  * **CurrencyCode** \- Currency of account this transaction relates to 
  * **Debit** \- Debit amount
  * **SettleTimestampUtc** \- UTC settlement timestamp
  * **Status** \- Transaction status
  * **Type** \- Transaction type
  * **CorrelationId** \- This is a context sensitive key. If the transaction is a withdrawal, it will be the primary key for the withdrawal request. When the transaction is a crypto deposit, the value will be the transaction hash from the network. In the case of a trade, the value will be the tradeGuid. 



### [ ](#GetFiatBankAccounts)GetFiatBankAccounts 

Retrieves the list of pre-configured external bank accounts.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 



POST

https://api.independentreserve.com/Private/GetFiatBankAccounts

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}"
    }

Response
    
    
    [
      {
        "PayId": {
          "Id": "user@example.com",
          "Type": "Email"
        },
        "Guid": "51f59e78-9c6b-4f7d-9c1b-171695f6292f",
        "Name": "PayID: user@example.com"
      },
      {
        "Bsb": "062623",
        "Country": "Australia",
        "Currency": "AUD",
        "AccountNumber": "123456789",
        "AccountHolderName": "Lastname Firstname",
        "Guid": "df0a8341-f3b7-43b4-a64e-7e951753bef8",
        "Name": "External Bank"
      }
    ]

### [ ](#GetDigitalCurrencyDepositAddress2) GetDigitalCurrencyDepositAddress2 

Retrieves the deposit address which should be used for cryptocurrency deposits.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The cryptocurrency to generate deposit address for. 



Example 1

POST

https://api.independentreserve.com/Private/GetDigitalCurrencyDepositAddress2

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Render"
    }

Response
    
    
    [
      {
        "Network": "Solana",
        "Address": "8sYTnN2rJbbgnrfcmQGpDqQmMr73YrLV3fepEd2q9WWL",
        "Tag": null
      }
    ]

Example 2 - Tagged Currency

POST

https://api.independentreserve.com/Private/GetDigitalCurrencyDepositAddress2

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Xrp"
    }

Response
    
    
    [
      {
        "Network": "XrpLedger",
        "Address": "r36xdATZKfyHQfsWqwButyxvzAW73wXvXL",
        "Tag": "2282896822"
      }
    ]

#### Return value descriptions

  * **Network** \- Blockchain network this applies to
  * **Address** \- Digital address to use for deposits
  * **Tag** \- Returned for cryptocurrencies that support tags (for example: Xrp, Xlm) 



### [ ](#GetDigitalCurrencyDepositAddresses2) GetDigitalCurrencyDepositAddresses2 

Retrieves a page of cryptocurrency deposit addresses which have been assigned to your account.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **network** \- The blockchain network to deposit on 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 50. 



Example 1

POST

https://api.independentreserve.com/Private/GetDigitalCurrencyDepositAddresses2

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "network": "Solana",
      "pageIndex": 1,
      "pageSize": 10
    }

Response
    
    
    {
      "Data": [
        {
          "Network": "Solana",
          "Address": "489YyzudYC53M1vqf2p6JuWJnR93YgMZ9ZiKZsbftUeV",
          "Tag": null
        }
      ],
      "PageSize": 10,
      "TotalItems": 1,
      "TotalPages": 1
    }

Example 2 - Tagged Currency

POST

https://api.independentreserve.com/Private/GetDigitalCurrencyDepositAddresses2

Copy

Request
    
    
    {
      "apiKey": "1e7f4eb1-3945-4e30-b748-93d13818a0e8",
      "nonce": "638719877518281099",
      "network": "XrpLedger",
      "pageIndex": 1,
      "pageSize": 10,
      "signature": "2DD0D5C5EDA4506BEB25A3490E1895C48EEF33C969F3C2BEC6C2846CEED8D134"
    }

Response
    
    
    {
      "Data": [
        {
          "Network": "XrpLedger",
          "Address": "rN7JdndUxYnBJaUzP3bs4aGH1eJi5pk6gR",
          "Tag": "1868796781"
        }
      ],
      "PageSize": 10,
      "TotalItems": 1,
      "TotalPages": 1
    }

#### Return value descriptions

  * **Network** \- The blockchain network to deposit on 
  * **Address** \- Deposit address to use
  * **Tag** \- Returned for cryptocurrencies that support tags (for example: Xrp, Xlm) 



### [ ](#GetTrades)GetTrades 

Retrieves a page of a specified size containing trades which were executed against your orders.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 5000. 
  * **fromTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2022-08-01T08:00:00Z`, from which you want to retrieve transactions. This is an optional parameter. 
  * **toTimestampUtc** \- The timestamp in UTC, specified according to ISO 8601 standard, e.g. `2022-08-07T08:00:00Z`, until which you want to retrieve transactions. This is an optional parameter. 
  * **includeTotals** \- Defaults to true for backward compatibility. When set to false, response time is improved and the `TotalItems` and `TotalPages` properties are returned as `-1`. 



#### Notes

  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 



POST

https://api.independentreserve.com/Private/GetTrades

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "pageIndex": 1,
      "pageSize": 5
    }

Response
    
    
    {
      "Data": [
        {
          "TradeGuid": "593e609d-041a-4f46-a41d-2cb8e908973f",
          "TradeTimestampUtc": "2022-12-16T03:44:19.2187707Z",
          "OrderGuid": "8bf851a3-76d2-439c-945a-93367541d467",
          "OrderType": "LimitBid",
          "OrderTimestampUtc": "2022-12-16T03:43:36.7423769Z",
          "VolumeTraded": 0.5,
          "Price": 410,
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Usd"
        },
        {
          "TradeGuid": "13c1e71c-bfb4-452c-b13e-e03535f98b09",
          "TradeTimestampUtc": "2022-12-11T11:37:42.2089564Z",
          "OrderGuid": "1ce88acf-6013-4867-b58d-77f0e41ec475",
          "OrderType": "LimitBid",
          "OrderTimestampUtc": "2022-12-11T11:37:42.0724391Z",
          "VolumeTraded": 0.4,
          "Price": 399,
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Usd"
        }
      ],
      "PageSize": 5,
      "TotalItems": 20,
      "TotalPages": 4
    }

#### Return value descriptions

  * **TradeGuid** \- Unique identifier of the trade
  * **TradeTimestampUtc** \- UTC timestamp corresponding to trade execution 
  * **OrderGuid** \- Unique identifier of the order which was matched as part of the trade 
  * **OrderType** \- The type of order which was matched
  * **OrderTimestampUtc** \- UTC timestamp when order was created 
  * **VolumeTraded** \- The volume of primary currency traded
  * **Price** \- The price in secondary currency at which the trade was executed 
  * **PrimaryCurrencyCode** \- The primary currency which was traded 
  * **SecondaryCurrencyCode** \- The secondary currency in which the trade was denominated 



### [ ](#GetTradesByOrder)GetTradesByOrder 

Retrieves the list of trades executed against your order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **orderGuid** \- Unique identifier of the order^. 
  * **pageIndex** \- Must be larger than 0. 
  * **pageSize** \- Must be between 1 and 50. 
  * **clientId** \- The clientId that was supplied when placing an order ^



^ At least one of these parameters should be supplied 

#### Notes

  * This method caches return values for 1 second. Calling it more than once per second will result in cached data being returned. 



POST

https://api.independentreserve.com/Private/GetTradesByOrder

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "orderGuid": "79eac4c9-f24f-4746-a013-2dfa3a295e11",
      "clientId": "a96ff431-7f47-4ab5-9974-4a2c6b6eb8d8",
      "pageIndex": 1,
      "pageSize": 5
    }

Response
    
    
    {
      "Data": [
        {
          "TradeGuid": "97be0f79-f003-4d74-86cf-c4d2960e4bcb",
          "TradeTimestampUtc": "2020-05-20T12:13:24.0368425+00:00",
          "OrderGuid": "79eac4c9-f24f-4746-a013-2dfa3a295e11",
          "OrderType": "MarketBid",
          "OrderTimestampUtc": "2020-05-20T12:13:24.0268429+00:00",
          "VolumeTraded": 0.19316949,
          "Price": 315.21,
          "PrimaryCurrencyCode": "Ltc",
          "SecondaryCurrencyCode": "Aud"
        },
        {
          "TradeGuid": "8fb3f7fc-8041-4914-8369-dc5ee7056566",
          "TradeTimestampUtc": "2020-05-20T12:13:24.0368425+00:00",
          "OrderGuid": "79eac4c9-f24f-4746-a013-2dfa3a295e11",
          "OrderType": "MarketBid",
          "OrderTimestampUtc": "2020-05-20T12:13:24.0268429+00:00",
          "VolumeTraded": 0.20683051,
          "Price": 314,
          "PrimaryCurrencyCode": "Ltc",
          "SecondaryCurrencyCode": "Aud"
        }
      ],
      "PageSize": 5,
      "TotalItems": 20,
      "TotalPages": 4
    }

#### Return value descriptions

  * **TradeGuid** \- Unique identifier of the trade
  * **TradeTimestampUtc** \- UTC timestamp corresponding to trade execution
  * **OrderGuid** \- Unique identifier of the order which was matched as part of the trade
  * **OrderType** \- The type of order which was matched
  * **OrderTimestampUtc** \- UTC timestamp when order was created
  * **VolumeTraded** \- The volume of primary currency traded
  * **Price** \- The price - denominated in the secondary currency - at which the trade was executed 
  * **PrimaryCurrencyCode** \- The primary currency which was traded
  * **SecondaryCurrencyCode** \- The secondary currency in which the trade was denominated



### [ ](#GetBrokerageFees)GetBrokerageFees 

Retrieves information about the trading fees for the cryptocurrencies in your Independent Reserve account. 

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 



POST

https://api.independentreserve.com/Private/GetBrokerageFees

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}"
    }

Response
    
    
    [
      {
        "CurrencyCode": "Xbt",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Xrp",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Eth",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Eos",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Bch",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Ltc",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Etc",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Xlm",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Bat",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Omg",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Rep",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Zrx",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Gnt",
        "Fee": 0.005
      },
      {
        "CurrencyCode": "Pla",
        "Fee": 0.005
      }
    ]

#### Return value descriptions

  * **CurrencyCode** \- The currency the fee applies to
  * **Fee** \- Fee value



### [ ](#GetDigitalCurrencyWithdrawal)GetDigitalCurrencyWithdrawal 

Get the details of a specific digital currency withdrawal

#### Parameters

Either `transactionGuid` or `clientId` must be specified as the key to retrieve the record. 

  * **apiKey** \- Your API Key
  * **nonce** \- Nonce value
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call 
  * **transactionGuid** \- This should either be the TransactionGuid returned by WithdrawDigitalCurrency, or the CorrelationId returned by GetTransactions. 
  * **clientId** \- If the withdrawal was created with a `clientId`, it can be retrieved by the same `clientId`



POST

https://api.independentreserve.com/Private/GetDigitalCurrencyWithdrawal

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "transactionGuid": "2a93732f-3f40-4685-b3bc-ff3ec326090d",
      "clientId": null
    }

Response
    
    
    {
      "TransactionGuid": "dc932e19-562b-4c50-821e-a73fd048b93b",
      "PrimaryCurrencyCode": "Xrp",
      "Network": "XrpLedger",
      "CreatedTimestampUtc": "2020-04-01T05:26:30.5093622+00:00",
      "Amount": {
        "Total": 1.1231,
        "Fee": 0.0001
      },
      "Destination": {
        "Address": "rwyzH6FHHKfQoKdrtnDbwE8PuAmxzsA41X",
        "Tag": "3113"
      },
      "Status": "Pending",
      "Transaction": null,
      "ClientId": "my-unique-tracking-id-2383486"
    }

#### Return value descriptions

  * **TransactionGuid** \- Unique identifier of the withdrawal 
  * **PrimaryCurrencyCode** \- Currency being withdrawn
  * **CreatedTimestampUtc** \- Timestamp in UTC when fiat withdrawal request was created 
  * **Network** \- The blockchain network to withdraw on 
  * **Amount**
    * **Total** \- Total amount being withdrawn by the user (inclusive of any fees) 
    * **Fee** \- Fee amount which will be taken out of the withdrawal amount 
  * **Destination**
    * **Address** \- Target cryptocurrency address
    * **Tag** \- Target cryptocurrency destination tag.
  * **Status** \- Request status in the workflow (Pending, Held, Approved, Executing, Executed, Rejected, Cancelled) 
  * **Transaction** \- Value is null if transaction hasn't been broadcasted to the network 
    * **Hash** \- Related blockchain network transaction
    * **OutputIndex** \- The index of the transaction output to the destination address. This value is specified only for Xbt, Bch, Bsv, Ltc. 



### [ ](#GetFiatWithdrawal)GetFiatWithdrawal 

Get details on a specific fiat withdrawal. See [our FAQ](/help/faq#withdrawals) for more information on fiat withdrawals. 

#### Parameters

Either `fiatWithdrawalRequestGuid` or `clientId` must be specified as the key to retrieve the record. 

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **fiatWithdrawalRequestGuid** \- Fiat withdrawal request identifier. 
  * **clientId** \- If the withdrawal was created with a clientId, it can be retrieved by the same clientId 



POST

https://api.independentreserve.com/Private/GetFiatWithdrawal

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "fiatWithdrawalRequestGuid": "2e9ad56c-1954-4b0f-b3d8-2ade7fad93ff",
      "clientId": null
    }

Response
    
    
    {
      "FiatWithdrawalRequestGuid": "2e9ad56c-1954-4b0f-b3d8-2ade7fad93ff",
      "AccountGuid": "eda82a84-57fe-4ce6-9ee5-45a41063ee23",
      "Status": "Pending",
      "CreatedTimestampUtc": "2022-12-18T14:08:47.4032405Z",
      "TotalWithdrawalAmount": 50,
      "FeeAmount": 20,
      "Currency": "Usd",
      "ClientId": "my-unique-tracking-id-2383386"
    }

#### Return value descriptions

  * **FiatWithdrawalRequestGuid** \- fiat withdrawal request identifier 
  * **AccountGuid** \- IR account to withdraw from
  * **Status** \- Request status in the workflow
  * **CreatedTimestampUtc** \- Timestamp in UTC when fiat withdrawal request was created 
  * **TotalWithdrawalAmount** \- Total amount being withdrawn by the user (inclusive of any fees) 
  * **FeeAmount** \- Fee amount which will be taken out of the withdrawal amount 
  * **Currency** \- Currency being withdrawn



### [ ](#GetDepositLimits)GetDepositLimits 

Get fiat deposit limits.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 



POST

https://api.independentreserve.com/Private/GetDepositLimits

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}"
    }

Response
    
    
    {
      "Fiat": [
        {
          "DepositType": "PoliPayment",
          "MaxTransactionAmount": 1000,
          "Limits": [
            {
              "Deposited": 300,
              "Period": "Day",
              "AutomaticApprovalLimit": 1000
            }
          ]
        },
        {
          "DepositType": "Osko",
          "MaxTransactionAmount": 10000,
          "Limits": [
            {
              "Deposited": 400,
              "Period": "Day",
              "AutomaticApprovalLimit": 10000
            }
          ]
        }
      ]
    }

#### Return value descriptions

  * **Fiat** \- Array of deposit types 
    * **DepositType** \- Method of deposit
    * **MaxTransactionAmount** \- Maximum amount of a single payment 
    * **Limits**
      * **Deposited** \- Total amount of deposits processed within the period 
      * **Period** \- "Day"
      * **AutomaticApprovalLimit** \- Deposits up to this amount in the period will be processed and credited to your account automatically. Amounts over this limit will require review by an operator. 



### [ ](#GetWithdrawalLimits)GetWithdrawalLimits 

Get withdrawal limits.

#### Parameters

  * **apiKey** : Your API Key.
  * **nonce** : Nonce value.
  * **signature** : HMAC-SHA256 encoded message to authenticate API call. 



POST

https://api.independentreserve.com/Private/GetWithdrawalLimits

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}"
    }

Response
    
    
    {
      "Xbt": [
        {
          "Withdrawn": 0.38,
          "Period": "P12H",
          "AutomaticApprovalLimit": 6
        }
      ],
      "Eth": [
        {
          "Withdrawn": 0.1,
          "Period": "P12H",
          "AutomaticApprovalLimit": 80
        }
      ],
      "Xrp": [
        {
          "Withdrawn": 0,
          "Period": "P12H",
          "AutomaticApprovalLimit": 30000
        }
      ]
    }

#### Return value descriptions

  * **Xbt** \- Primary currency code 
    * **Withdrawn** \- Total amount of withdrawals processed within the period 
    * **Period** \- Sliding window the limit applies to. Formatted as Iso8601 duration 
    * **AutomaticApprovalLimit** \- Withdrawals up to this amount made during the period will be processed automatically 



### [ ](#PlaceLimitOrder)PlaceLimitOrder 

Places new limit bid / offer order. A Limit Bid is a buy order and a Limit Offer is a sell order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The cryptocurrency code of limit order. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency of limit order. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **orderType** \- The type of limit order. Must be a valid limit order type, which can be checked via the [GetValidLimitOrderTypes](#GetValidLimitOrderTypes) method. 
  * **price** \- The price in secondary currency to buy/sell.
  * **volume** \- The volume to buy/sell in primary currency.
  * **timeInForce** \- See details below
  * **clientId** \- Specify your own clientId to a maximum of 36 characters. Uniqueness of clientId will be enforced across orders for a guaranteed 24 hours minimum, but in most cases longer. If an order is placed with a duplicate clientId, it will be rejected. Do not insert sensitive data, the clientId is publicly visible via our [websocket channels](https://github.com/independentreserve/websockets/blob/master/orderbook-ticker.md#clientid). 



##### Time In Force

When placing limit orders, several different options are available for the `timeInForce` argument. If omitted, the assumed value is `Gtc`. 

Parameter Value | Description  
---|---  
`Gtc` |  (Good Til Cancelled) This order will stay on the order book until it is either filled or cancelled by a subsequent event.   
`Ioc` |  (Immediate Or Cancel) If any volume from the order can be executed immediately, it will be executed. If there is any remaining unfilled volume, the order will be cancelled and not placed on the order book. When the price does not cross the market, the response will be `(400) TimeInForce.Ioc order cannot be executed.`  
`Fok` |  (Fill Or Kill) The order will be cancelled if it cannot be fully executed at the time of placement.   
`Moc` |  (Maker Or Cancel) If the order fully or partially crosses the spread at the time of placement, it will be immediately rejected. The order will only be placed if no part of the order will be executed immediately. An order with the Moc flag always functions as a maker order and never as a taker order.   
  
POST

https://api.independentreserve.com/Private/PlaceLimitOrder

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "clientId": "{client-id}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Usd",
      "orderType": "LimitBid",
      "price": 485.76,
      "volume": 0.358,
      "timeInForce": "Gtc"
    }

Response
    
    
    {
      "CreatedTimestampUtc": "2022-08-05T06:42:11.3032208Z",
      "OrderGuid": "719c495c-a39e-4884-93ac-280b37245037",
      "Price": 485.76,
      "PrimaryCurrencyCode": "Xbt",
      "ReservedAmount": 0.358,
      "SecondaryCurrencyCode": "Usd",
      "Status": "Open",
      "Type": "LimitOffer",
      "VolumeFilled": 0,
      "VolumeOrdered": 0.358
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- TC timestamp of when order was created 
  * **OrderGuid** \- Unique identifier of the order
  * **Price** \- Order limit price in secondary currency
  * **PrimaryCurrencyCode** \- Primary currency of order
  * **ReservedAmount** \- The amount of funds reserved in your account by this order 
  * **SecondaryCurrencyCode** \- Secondary currency of order
  * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
  * **Type** \- Type of order
  * **VolumeFilled** \- Volume already filled on this order
  * **VolumeOrdered** \- The original volume ordered
  * **VolumeCurrencyType** \- Indicate in which currency the volume is denominated 



### [ ](#PlaceMarketOrder)PlaceMarketOrder 

Place new market bid / offer order. A Market Bid is a buy order and a Market Offer is a sell order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** : HMAC-SHA256 encoded message to authenticate API call. 
  * **primaryCurrencyCode** \- The cryptocurrency code of market order. Must be a valid primary currency, which can be checked via the [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes) method. 
  * **secondaryCurrencyCode** \- The fiat currency of market order. Must be a valid secondary currency, which can be checked via the [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes) method. 
  * **orderType** \- The type of market order. Must be a valid market order type, which can be checked via the [GetValidMarketOrderTypes](#GetValidMarketOrderTypes) method. 
  * **volume** \- The volume of currency to order, denominated in _volumeCurrencyType_. 
  * **volumeCurrencyType** \- Optional with default value of "Primary". Possible values are _Primary, Secondary._
  * **clientId** \- Specify your own clientId to a maximum of 36 characters. Uniqueness of clientId will be enforced across orders for a guaranteed 24 hours minimum, but in most cases longer. If an order is placed with a duplicate clientId, it will be rejected. Do not insert sensitive data, the clientId is publicly visible via our [websocket channels](https://github.com/independentreserve/websockets/blob/master/orderbook-ticker.md#clientid). 
  * **allowedSlippagePercent** \- Optional parameter for slippage protection. The order will be rejected once the fill price moves by more than the specified percentage from the best order book price at the time of placement. Value should be the range of 0 to 100. 



Example 1

POST

https://api.independentreserve.com/Private/PlaceMarketOrder

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "clientId": "{client-id}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Usd",
      "orderType": "MarketOffer",
      "volume": 0.025
    }

Response
    
    
    {
      "CreatedTimestampUtc": "2022-08-05T06:42:11.3032208Z",
      "OrderGuid": "5c8885cd-5384-4e05-b397-9f5119353e10",
      "PrimaryCurrencyCode": "Xbt",
      "ReservedAmount": 0.025,
      "SecondaryCurrencyCode": "Usd",
      "Status": "Open",
      "Type": "MarketOffer",
      "VolumeFilled": 0,
      "VolumeOrdered": 0.025
    }

Example 2

POST

https://api.independentreserve.com/Private/PlaceMarketOrder

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "primaryCurrencyCode": "Xbt",
      "secondaryCurrencyCode": "Aud",
      "orderType": "MarketOffer",
      "volume": "77.8",
      "volumeCurrencyType": "Secondary"
    }

Response
    
    
    {
      "CreatedTimestampUtc": "2020-05-21T01:38:06.090333+00:00",
      "OrderGuid": "4994b087-70d7-457f-babe-6c226c5bc4e3",
      "PrimaryCurrencyCode": "Xbt",
      "ReservedAmount": 9716.94255222,
      "SecondaryCurrencyCode": "Aud",
      "Status": "Open",
      "Type": "MarketOffer",
      "VolumeFilled": 0,
      "VolumeOrdered": 77.8,
      "VolumeCurrencyType": "Secondary"
    }

#### Return value descriptions

  * **CreatedTimestampUtc** \- TC timestamp of when order was created 
  * **OrderGuid** \- Unique identifier of the order
  * **PrimaryCurrencyCode** \- Primary currency of order
  * **ReservedAmount** \- The amount of funds reserved in your account by this order 
  * **SecondaryCurrencyCode** \- Secondary currency of order
  * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
  * **Type** \- Type of order
  * **VolumeFilled** \- Volume already filled on this order
  * **VolumeOrdered** \- The original volume ordered
  * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#CancelOrder)CancelOrder 

Cancels a previously placed order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **orderGuid** \- The guid of currently open or partially filled order. 



#### Notes

  * The order must be in either 'Open' or 'PartiallyFilled' status to be valid for cancellation. You can retrieve list of Open and Partially Filled orders via the [GetOpenOrders](#GetOpenOrders) method. You can also check an individual order's status by calling the [GetOrderDetails](#GetOrderDetails) method. 



POST

https://api.independentreserve.com/Private/CancelOrder

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "orderGuid": "719c495c-a39e-4884-93ac-280b37245037"
    }

Response
    
    
    {
      "AvgPrice": 455.48,
      "CreatedTimestampUtc": "2022-08-05T06:42:11.3032208Z",
      "OrderGuid": "719c495c-a39e-4884-93ac-280b37245037",
      "Price": 485.76,
      "PrimaryCurrencyCode": "Xbt",
      "ReservedAmount": 0.358,
      "SecondaryCurrencyCode": "Usd",
      "Status": "Cancelled",
      "Type": "LimitOffer",
      "VolumeFilled": 0,
      "VolumeOrdered": 0.358
    }

#### Return value descriptions

  * **AvgPrice** \- Average price for all trades executed for the order 
  * **CreatedTimestampUtc** \- TC timestamp of when order was created 
  * **OrderGuid** \- Unique identifier of the order
  * **Price** \- Order limit price in secondary currency
  * **PrimaryCurrencyCode** \- Primary currency of order
  * **ReservedAmount** \- The amount of funds reserved in your account by this order 
  * **SecondaryCurrencyCode** \- Secondary currency of order
  * **Status** \- See [OrderStatus.cs](https://github.com/independentreserve/dotNetApiClient/blob/master/src/DotNetClientApi/Data/OrderStatus.cs) for possible values 
  * **Type** \- Type of order
  * **VolumeFilled** \- Volume already filled on this order
  * **VolumeOrdered** \- The original volume ordered
  * **VolumeCurrencyType** \- Whether volume is denominated in Primary or Secondary currency 



### [ ](#CancelOrders)CancelOrders 

Accepts an array of orderGuid so that multiple orders can be cancelled in the one call.

Response will contain cancellation result for each individual order.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **orderGuids** \- An array of order guids.



#### Notes

  * The orderGuids parameter is a JSON array in the POST body but for signature generation, the orderGuids should be formatted as csv. For example `orderGuids=Guid1,Guid2`. 
  * The order must be in either 'Open' or 'PartiallyFilled' status to be valid for cancellation. You can retrieve list of Open and Partially Filled orders via the [GetOpenOrders](#GetOpenOrders) method. You can also check an individual order's status by calling the [GetOrderDetails](#GetOrderDetails) method. 



POST

https://api.independentreserve.com/Private/CancelOrders

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "orderGuids": [
        "5053e267-6060-44a8-9ab6-77f36fed86df",
        "309d8b71-868c-4408-9346-c5aca4c3efdb"
      ]
    }

Response
    
    
    {
      "5053e267-6060-44a8-9ab6-77f36fed86df": {
        "IsSuccess": true,
        "Message": null
      },
      "309d8b71-868c-4408-9346-c5aca4c3efdb": {
        "IsSuccess": true,
        "Message": null
      }
    }

### [ ](#SynchDigitalCurrencyDepositAddressWithBlockchain) SynchDigitalCurrencyDepositAddressWithBlockchain 

Forces the deposit address to be checked for cryptocurrency deposits.

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **depositAddress** \- The cryptocurrency deposit address to check for new deposits. 
  * **primaryCurrencyCode** \- Primary currency code.



POST

https://api.independentreserve.com/Private/SynchDigitalCurrencyDepositAddressWithBlockchain

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "depositAddress": "12a7FbBzSGvJd36wNesAxAksLXMWm4oLUJ",
      "primaryCurrencyCode": "Bch"
    }

Response
    
    
    {
      "DepositAddress": "12a7FbBzSGvJd36wNesAxAksLXMWm4oLUJ",
      "LastCheckedTimestampUtc": "2022-05-05T09:35:22.4032405Z",
      "NextUpdateTimestampUtc": "2022-05-05T09:45:22.4032405Z"
    }

#### Return value descriptions

  * **DepositAddress** \- Cryptocurrency deposit address to be updated 
  * **LastCheckedTimestampUtc** \- UTC timestamp of when this address was last checked against the blockchain 
  * **NextUpdateTimestampUtc** \- UTC timestamp of when this address is scheduled to next be checked against the blockchain 



### [ ](#WithdrawCrypto)WithdrawCrypto 

Creates a cryptocurrency withdrawal request. There is a [minimum withdrawal value](/help/faq#withdrawals) for each cryptocurrency, except where the available balance is less than this amount. In all cases, the withdrawal amount must be greater than the withdrawal fee. Take care to provide a valid destination address. **Cryptocurrency withdrawals are irreversible once sent.**

#### Notes

  * Only API Keys which are explicitly marked as being allowed to withdraw cryptocurrency can call this method. 



#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **network** \- Crypto can be withdrawn on multiple networks where available. See [GetNetworks](/features/api#GetNetworks). 
  * **primaryCurrencyCode** \- Primary currency code.
  * **withdrawalAddress** \- Target Bitcoin or Ether withdrawal address. 
  * **destinationTag** \- Optional. For cryptocurrencies that support tags (for example: XRP) 
  * **amount** \- The amount of cryptocurrency to withdraw.
  * **comment** \- Withdrawal comment. Should not exceed 500 characters. 
  * **clientId** \- Optional. Specify your own clientId to a maximum of 36 characters. Uniqueness of clientId will be enforced for a guaranteed 24 hours minimum, but in most cases longer. If a crypto withdrawal is placed with a duplicate clientId, it will be rejected. 



POST

https://api.independentreserve.com/Private/WithdrawCrypto

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "network": "XrpLedger",
      "primaryCurrencyCode": "Xrp",
      "withdrawalAddress": "rN7JdndUxYnBJaUzP3bs4aGH1eJi5pk6gR",
      "destinationTag": "12345",
      "amount": "50",
      "comment": "My comment",
      "clientId": "MyClientId123123"
    }

Response
    
    
    {
      "TransactionGuid": "648d7ea1-1355-4ff8-ba80-3896a7bf39b1",
      "PrimaryCurrencyCode": "Xrp",
      "Network": "XrpLedger",
      "CreatedTimestampUtc": "2025-01-09T05:38:28.4491776+00:00",
      "Amount": {
        "Total": 50,
        "Fee": 0.01
      },
      "Destination": {
        "Address": "rN7JdndUxYnBJaUzP3bs4aGH1eJi5pk6gR",
        "Tag": "12345"
      },
      "Status": "Pending",
      "ClientId": "MyClientId123123"
    }

#### Return value descriptions

  * **TransactionGuid** \- Unique identifier of the withdrawal 
  * **PrimaryCurrencyCode** \- Currency being withdrawn
  * **network** \- The blockchain network the withdrawal will be made on.
  * **CreatedTimestampUtc** \- Timestamp in UTC when fiat withdrawal request was created 
  * **Amount**
    * **Total** \- Total amount being withdrawn by the user (inclusive of any fees) 
    * **Fee** \- Fee amount which will be taken out of the withdrawal amount 
  * **Destination**
    * **Address** \- Target cryptocurrency address
    * **Tag** \- Target cryptocurrency destination tag.
  * **Status** \- Request status in the workflow (Pending, Held, Approved, Executing, Executed, Rejected, Cancelled) 



### [ ](#WithdrawFiatCurrency)WithdrawFiatCurrency 

Creates a Fiat currency withdrawal from your Independent Reserve account to an external bank account. See the [fiat withdrawals FAQ](/help/faq#withdrawals) for more information. 

#### Parameters

  * **apiKey** \- Your API Key.
  * **nonce** \- Nonce value.
  * **signature** \- HMAC-SHA256 encoded message to authenticate API call. 
  * **secondaryCurrencyCode** \- The Independent Reserve fiat currency account to withdraw from. 
  * **withdrawalAmount** \- Amount of fiat currency to withdraw. 
  * **fiatBankAccountGuid** : Fiat bank account guid
  * **useNpp** : Send instantly using NPP
  * **comment** \- Withdrawal comment. Should not exceed 500 characters. 
  * **clientId** \- Optional. Specify your own clientId to a maximum of 36 characters. Uniqueness of clientId will be enforced for a guaranteed 24 hours minimum, but in most cases longer. If a fiat withdrawal is placed with a duplicate clientId, it will be rejected. 



POST

https://api.independentreserve.com/Private/WithdrawFiatCurrency

Copy

Request
    
    
    {
      "apiKey": "{api-key}",
      "nonce": "{nonce}",
      "signature": "{signature}",
      "secondaryCurrencyCode": "{secondaryCurrencyCode}",
      "withdrawalAmount": "{withdrawalAmount}",
      "fiatBankAccountGuid": "{fiatBankAccountGuid}",
      "useNpp": "true",
      "comment": "{comment}",
      "clientId": null
    }

Response
    
    
    {
      "FiatWithdrawalRequestGuid": "a953d73e-e650-471f-a502-676dea9574ea",
      "AccountGuid": "137edc8f-d681-4a61-905c-5e761317193b",
      "Status": "Executed",
      "CreatedTimestampUtc": "2020-09-30T14:08:47.4032405Z",
      "TotalWithdrawalAmount": 11.5,
      "FeeAmount": 1.5,
      "Currency": "Aud",
      "ClientId": "my-unique-tracking-id-2383286"
    }

#### Return value descriptions

  * **FiatWithdrawalRequestGuid** \- Unique indentifier of this request 
  * **AccountGuid** \- IR account to withdraw from
  * **Status** \- Request status in the workflow
  * **CreatedTimestampUtc** \- Timestamp in UTC when fiat withdrawal request was created 
  * **TotalWithdrawalAmount** \- Total amount being withdrawn by the user (inclusive of any fees) 
  * **FeeAmount** \- Fee amount which will be taken out of the withdrawal amount 
  * **Currency** \- Currency being withdrawn



## [ ](#error-handling)Error handling 

The API uses standard HTTP status codes 200/400 to indicate the success/failure of a request. In the event of an error, the response body will contain a JSON object with `ErrorCode` and `Message` properties like below: 
    
    
    {
      "ErrorCode": "ValidationError",
      "Message": "Invalid primary currency code"
    }

The following table lists the specific error codes that the API can return. The `Message` property in the response may contain more context specific details. The description below is a general guide for the class of error. 

Error Code | Description  
---|---  
`UnexpectedError` | An error occurred internally to Independent Reserve. The client should check account or order status and send a new request if required.  
`ValidationError` | One or more properties in the request were invalid. Check Message property for more information.  
`AccessDenied` | Check that your credentials are correct.  
`RequestDuplicated` | A prior request with the same ClientId has already been received.  
`RecordDoesNotExist` | The request was for a key that doesn't exist in our system.  
`RecordNotWhitelisted` | This can happen when a crypto address or bank account is not whitelisted for the operation attempted.  
`UserSuspended` | Access to this account is temporarily suspended for security reasons.  
`UserInactive` | The account has been permanently closed.  
`UserFrozen` | Some functions on this account are limited. Logon to Portal for more information.  
`OrderLimitExceeded` | The order attempted has exceeded internal limits. The order size should be reduced.  
`WithdrawalDisabled` | Withdrawals for the selected currency are temporarily unavailable.  
  
## [ ](#api-changes)API Changes 

To support different deposit and withdrawal networks per cryptocurrency (bridging), the endpoints below were introduced or modified in January 2025. Endpoints that were replaced remain operational. 

  * `GetNetworks` is new
  * `GetPrimaryCurrencyConfig2` replaced `~~GetPrimaryCurrencyConfig~~`
  * `GetCryptoWithdrawalFees2` replaced `~~GetCryptoWithdrawalFees~~`
  * `GetTransactions` now additionally returns _Network_ property
  * `GetDigitalCurrencyWithdrawal` now additionally returns _Network_ property
  * `GetDigitalCurrencyDepositAddress2` replaced `~~GetDigitalCurrencyDepositAddress~~`
  * `GetDigitalCurrencyDepositAddresses2` replaced `~~GetDigitalCurrencyDepositAddresses~~`
  * `WithdrawCrypto` replaced `~~WithdrawDigitalCurrency~~`



## [ ](#sample-api-clients)Sample API clients 

Below are sample API client code libraries that can be used as a point of reference or as the basis of your own applications that integrate with Independent Reserve. 

Please keep in mind that neither Independent Reserve nor the third party authors are responsible for losses due to bugs or improper use of the API. Independent Reserve have performed an initial review of the veracity of the third party code but cannot vouch for any changes made since then. If you have concerns, please contact us via the support page. 

Platform/Language | Project link  
---|---  
.NET |  <https://github.com/independentreserve/dotNetApiClient>  
Postman |  <https://github.com/independentreserve/dotNetApiClient/tree/master/test/Postman>  
Node.js |  <https://github.com/davesag/ir-api> (third party authored)  
PHP |  <https://github.com/elliotchance/independentreserve> (third party authored)  
Java |  <https://github.com/timmolter/XChange> (third party authored)  
Python |  <https://github.com/MelchiSalins/pyindependentreserve> (third party authored)  
Rust |  <https://github.com/tcharding/rust-crypto-trader> (third party authored)  
  
## [ ](#websockets)WebSockets 

WebSockets documentation is available on our **[github repository](https://github.com/independentreserve/websockets)**. 

  * [Overview](#overview)
  * [Public methods ](#public-methods)
    * [GetValidPrimaryCurrencyCodes](#GetValidPrimaryCurrencyCodes)
    * [GetValidSecondaryCurrencyCodes](#GetValidSecondaryCurrencyCodes)
    * [GetValidLimitOrderTypes](#GetValidLimitOrderTypes)
    * [GetValidMarketOrderTypes](#GetValidMarketOrderTypes)
    * [GetValidOrderTypes](#GetValidOrderTypes)
    * [GetValidTransactionTypes](#GetValidTransactionTypes)
    * [GetNetworks](#GetNetworks)
    * [GetPrimaryCurrencyConfig2](#GetPrimaryCurrencyConfig2)
    * [GetMarketSummary](#GetMarketSummary)
    * [GetOrderBook](#GetOrderBook)
    * [GetAllOrders](#GetAllOrders)
    * [GetTradeHistorySummary](#GetTradeHistorySummary)
    * [GetRecentTrades](#GetRecentTrades)
    * [GetFxRates](#GetFxRates)
    * [GetOrderMinimumVolumes](#GetOrderMinimumVolumes)
    * [GetDepositFees](#GetDepositFees)
    * [GetFiatWithdrawalFees](#GetFiatWithdrawalFees)
    * [GetCryptoWithdrawalFees2](#GetCryptoWithdrawalFees2)
  * [Authentication](#authentication)
  * [Private methods ](#private-methods)
    * [GetOpenOrders](#GetOpenOrders)
    * [GetClosedOrders](#GetClosedOrders)
    * [GetClosedFilledOrders](#GetClosedFilledOrders)
    * [GetOrderDetails](#GetOrderDetails)
    * [GetAccounts](#GetAccounts)
    * [GetTransactions](#GetTransactions)
    * [GetFiatBankAccounts](#GetFiatBankAccounts)
    * [GetDigitalCurrencyDepositAddress2](#GetDigitalCurrencyDepositAddress2)
    * [GetDigitalCurrencyDepositAddresses2](#GetDigitalCurrencyDepositAddresses2)
    * [GetTrades](#GetTrades)
    * [GetTradesByOrder](#GetTradesByOrder)
    * [GetBrokerageFees](#GetBrokerageFees)
    * [GetDigitalCurrencyWithdrawal](#GetDigitalCurrencyWithdrawal)
    * [GetFiatWithdrawal](#GetFiatWithdrawal)
    * [GetDepositLimits](#GetDepositLimits)
    * [GetWithdrawalLimits](#GetWithdrawalLimits)
    * [PlaceLimitOrder](#PlaceLimitOrder)
    * [PlaceMarketOrder](#PlaceMarketOrder)
    * [CancelOrder](#CancelOrder)
    * [CancelOrders](#CancelOrders)
    * [SynchDigitalCurrencyDepositAddressWithBlockchain](#SynchDigitalCurrencyDepositAddressWithBlockchain)
    * [WithdrawFiatCurrency](#WithdrawFiatCurrency)
    * [WithdrawCrypto](#WithdrawCrypto)
  * [Error handling](#error-handling)
  * [API Changes](#api-changes)
  * [Sample API clients](#sample-api-clients)
  * [WebSockets](#websockets)



Start trading

[Log in](https://portal.independentreserve.com/login) [Get started](https://portal.independentreserve.com/register)

Wanting to do an OTC deal? [Learn more here](/features/otc)

Trade

  * [Buy crypto](/buy)
  * [Sell crypto](/sell)
  * [Buy Bitcoin](/buy/bitcoin)
  * [Crypto exchange](/)
  * [Bitcoin & crypto OTC](/features/otc)



About

  * [About us](/about)
  * [Careers](/careers)
  * [General enquiries](mailto:general@independentreserve.com)
  * [Media enquiries](mailto:media@independentreserve.com)



Help

  * [API](/features/api)
  * [Blog](https://www.independentreserve.com/blog)
  * [EOFY](/eofy)
  * [FAQs](/help/faq)
  * [Fees](/fees)
  * [Knowledge base](https://www.independentreserve.com/blog/knowledge-base)
  * [News](https://www.independentreserve.com/blog/news)
  * [Protect your account](https://www.independentreserve.com/blog/knowledge-base/protect-your-account)
  * [Security](/security)



### Select your region: 

EN

Social

[ Follow us on X (Twitter)](https://x.com/indepreserve "Follow us on X \(Twitter\)")[ Follow us on LinkedIn](https://www.linkedin.com/company/independent-reserve "Follow us on LinkedIn")[ Follow us on TikTok](https://www.tiktok.com/@independentreserve "Follow us on TikTok")[ Watch on YouTube](https://www.youtube.com/independentreserve "Watch on YouTube")[ Like us on Facebook](https://www.facebook.com/independentreserve "Like us on Facebook")[ Follow us on Instagram](https://www.instagram.com/independentreserve/ "Follow us on Instagram")[ Submit to Reddit](https://www.reddit.com/r/independentreserve "Submit to Reddit")[ Listen on Spotify](https://open.spotify.com/show/4vdfEXvQZGUDXyHJloxBiN "Listen on Spotify")

We’re certified

[ Go to the home page](/)

© 2026 Independent Reserve Pty. Ltd. ABN 46 164 257 069

  * [Terms & conditions](/help/terms-and-conditions)
  * [Privacy collection notice](/help/privacy-collection-notice)
  * [Privacy policy](/help/privacy-policy)
  * [Anti money laundering (AML) policy](/help/aml-policy)



[Log in](https://portal.independentreserve.com/login) [Create account](https://portal.independentreserve.com/register)

  * Personal

Account types 

    * [Personal](/features/personal)
    * [Trust](/features/trust)

Solutions for 

    * [Family offices](/features/family-offices-asset-managers)
    * [High-net-worth individuals](/features/high-net-worth)

Ways to trade 

    * [API](/features/api)
    * [Bank transfer](/buy/bank-transfer)
    * [Dollar-cost averaging](/features/recurring-buy)
    * [Leveraged trading](/features/leveraged-trading)
    * [OTC (Over-the-counter)](/features/otc)
    * [SWIFT](https://www.independentreserve.com/blog/knowledge-base/how-to-deposit-nzd-and-usd-using-swift)

[Features](/features)

    * [24/7 support](/features/premium-support)
    * [Fees](/fees)
    * [Mobile app](/features/mobile-app)
    * [Multi-user](/features/multi-user)
    * [Security](/security)
    * [Wallet](/features/wallet)

  * Business

Account types 

    * [Company](/features/company-accounts)
    * [Institutional](/institutions)
    * [Trust](/features/trust)

Solutions for 

    * [Asset managers](/features/family-offices-asset-managers)
    * [Family offices](/features/family-offices-asset-managers)
    * [Web 3 Builders](/features/web3-blockchain-builders)

Ways to trade 

    * [API](/features/api)
    * [Bank transfer](/buy/bank-transfer)
    * [Dollar-cost averaging](/features/recurring-buy)
    * [Leveraged trading](/features/leveraged-trading)
    * [OTC (Over-the-counter)](/features/otc)
    * [SWIFT](https://www.independentreserve.com/blog/knowledge-base/how-to-deposit-nzd-and-usd-using-swift)

[Features](/features)

    * [24/7 support](/features/premium-support)
    * [Fees](/fees)
    * [Mobile app](/features/mobile-app)
    * [Multi-user](/features/multi-user)
    * [Security](/security)
    * [Wallet](/features/wallet)

  * [OTC](/features/otc)
  * Markets

Currency | Price | Actions  
---|---|---  
[ Bitcoin BTC ](/market/btc "Bitcoin price USD") | USD 68,129.11 |  [Buy](/buy/bitcoin "Buy Bitcoin") [Sell](/sell/bitcoin "Sell Bitcoin")  
[ Ethereum ETH ](/market/eth "Ethereum price USD") | USD 2,010.21 |  [Buy](/buy/ethereum "Buy Ethereum") [Sell](/sell/ethereum "Sell Ethereum")  
[ Solana SOL ](/market/sol "Solana price USD") | USD 85.5924 |  [Buy](/buy/solana "Buy Solana") [Sell](/sell/solana "Sell Solana")  
[ XRP XRP ](/market/xrp "XRP price USD") | USD 1.48648 |  [Buy](/buy/xrp "Buy XRP") [Sell](/sell/xrp "Sell XRP")  
[ USD Coin USDC ](/market/usdc "USD Coin price USD") | USD 0.99350 |  [Buy](/buy/usdc "Buy USD Coin") [Sell](/sell/usdc "Sell USD Coin")  
[ Tether USD USDT ](/market/usdt "Tether USD price USD") | USD 1.00447 |  [Buy](/buy/tether "Buy Tether USD") [Sell](/sell/tether "Sell Tether USD")  
  
[View all](/markets)

  * Help

Getting started 

    * [Start here](/help/getting-started)
    * [Personal accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-personal-account-with-independent-reserve)
    * [Company accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-company-account)
    * [Trust accounts](https://www.independentreserve.com/blog/knowledge-base/how-to-create-a-trust-account)

Resources 

    * [Blog](https://www.independentreserve.com/blog)
    * [Fees](/fees)
    * [Knowledge base](https://www.independentreserve.com/blog/knowledge-base)
    * [Market updates](https://www.independentreserve.com/blog/market-update)
    * [Security](/security)

Contact 

    * [Contact support](https://portal.independentreserve.com/support)
    * [Forgot password](https://portal.independentreserve.com/login/forgot-password)
    * [Media](mailto:media@independentreserve.com)
    * [Trouble logging in](https://portal.independentreserve.com/login/help-center)

  * About

About 

    * [About us](/about)
    * [Community initiatives](/community-initiatives)
    * [Fees](/fees)
    * [News and announcements](https://www.independentreserve.com/blog/news)
    * [Security](/security)




Region: EN

Select your region

  * Australia (English) 
  * New Zealand (English) 
  * Global (English) 
  * Singapore (English) 
  * 新加坡 (中文) 



[ LinkedIn](https://www.linkedin.com/company/independent-reserve/ "LinkedIn")[ X/Twitter](https://twitter.com/indepreserve "X/Twitter")[ YouTube](https://www.youtube.com/independentreserve "YouTube")[ Spotify](https://open.spotify.com/show/4vdfEXvQZGUDXyHJloxBiN "Spotify")[ Facebook](https://www.facebook.com/independentreserve "Facebook")[ Instagram](https://www.instagram.com/independentreserve/ "Instagram")[ TikTok](https://www.tiktok.com/@independentreserve "TikTok")

Close this dialog

## Choose your region and language

  * Australia (English) 
  * New Zealand (English) 
  * Global (English) 
  * Singapore (English) 
  * 新加坡 (中文) 



Close this dialog
