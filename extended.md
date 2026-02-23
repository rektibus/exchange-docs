Extended API Documentation
By using the Extended API, you agree to the Extended Terms & Privacy Policy. If you do not agree to the foregoing terms, do not use the Extended API.

Introduction
 This documentation is a work in progress and will be updated regularly based on user feedback and the addition of new functionality.
Welcome to the Extended API Documentation! This guide is designed to assist traders and developers in integrating with our hybrid perpetuals exchange.

Extended operates as a hybrid Central Limit Order Book (CLOB) exchange. While order processing, matching, position risk assessment, and transaction sequencing are handled off-chain, trade settlement occurs on-chain via Starknet.

Extended is designed to operate in a completely trustless manner, enabled by two core principles:

Users retain self-custody of their funds, with all assets held in smart contracts on Starknet. This means Extended has no custodial access to user assets under any circumstances.

On-chain validation of the trading logic ensures that fraudulent or incorrect transactions, including liquidations that are contrary to the on-chain rules, are never permitted.

All transactions that happen on Extended are settled on Starknet. While Starknet does not rely on Ethereum Layer 1 for every individual transaction, it inherits Ethereum’s security by publishing zero-knowledge proofs every few hours. These proofs validate state transitions on Starknet, ensuring the integrity and correctness of the entire system.

Extended's on-chain logic and smart contracts have undergone extensive audits by external security firms. The audit reports are available below:

ChainSecurity.

Public audit competition.

For a deeper breakdown of the core principles that make Extended trustless, see the blog Why Safe. For more on Extended Exchange's roadmap and architecture, check out Extended Vision and Architecture, respectively.

To optimize high-frequency trading performance, the Extended API operates asynchronously. When you place an order, it immediately returns an order ID, even before the order is officially recorded in the book. To track your order status in real time subscribe to the Order WebSocket stream, which delivers instant updates on confirmations, cancellations, and rejections.

StarkEx to Starknet migration
On August 12, 2025, Extended began the migration from StarkEx to Starknet. This transition marks the first step toward our long-term vision of the Extended ecosystem and the introduction of unified margin. You can read more about the broader migration rationale and vision in our documentation.

Existing Extended users will need to migrate from the current StarkEx instance to the new Starknet instance. The migration process has been designed to be as seamless as possible and is explained here. New users will be onboarded directly to the Starknet instance.

For the Starknet instance of the platform, the following changes vs StarkEx apply:

Wallet support: In addition to EVM-compatible wallets, we will also support Starknet-compatible wallets.

Signing logic: New signing logic in line with the SNIP12 standard (EIP712 for Starknet) and examples are available via the SDK.

Deposits and withdrawals: For EVM wallets, we support deposits and withdrawals on six major EVM chains, currently only via the user interface. For Starknet wallets, deposits and withdrawals via Starknet are now supported.

URL: The URL for the Starknet instance is api.starknet.extended.exchange, vs. api.extended.exchange for the StarkEx instance.

The migration will be rolled out in three stages:

Stage 1 – Dual Operation Mode,

Stage 2 – StarkEx Wind-Down Mode,

Stage 3 – StarkEx Freeze.

While the StarkEx instance will remain fully operational during Stage 1 of the migration, certain restrictions will apply starting August 12. Please review them carefully here.

Until the migration is complete, all StarkEx-specific details can be found in the dedicated section of the API documentation.

Python SDK
SDK configuration

from dataclasses import dataclass


@dataclass
class EndpointConfig:
    chain_rpc_url: str
    api_base_url: str
    stream_url: str
    onboarding_url: str
    signing_domain: str
    collateral_asset_contract: str
    asset_operations_contract: str
    collateral_asset_on_chain_id: str
    collateral_decimals: int


STARKNET_TESTNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://rpc.sepolia.org",
    api_base_url="https://api.starknet.sepolia.extended.exchange/api/v1",
    stream_url="wss://starknet.sepolia.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.starknet.sepolia.extended.exchange",
    signing_domain="starknet.sepolia.extended.exchange",
    collateral_asset_contract="",
    asset_operations_contract="",
    collateral_asset_on_chain_id="",
    collateral_decimals=6,
    starknet_domain=StarknetDomain(name="Perpetuals", version="v0", chain_id="SN_SEPOLIA", revision="1"),
    collateral_asset_id="0x1",
)

STARKNET_MAINNET_CONFIG = EndpointConfig(
    chain_rpc_url="",
    api_base_url="https://api.starknet.extended.exchange/api/v1",
    stream_url="wss://api.starknet.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.starknet.extended.exchange",
    signing_domain="extended.exchange",
    collateral_asset_contract="",
    asset_operations_contract="",
    collateral_asset_on_chain_id="0x1",
    collateral_decimals=6,
    starknet_domain=StarknetDomain(name="Perpetuals", version="v0", chain_id="SN_MAIN", revision="1"),
    collateral_asset_id="0x1",
)
 The SDK and the SDK documentation will be updated regularly to include additional functionality and more examples.
Getting Started:

For installation instructions, please refer to the description provided.

For reference implementations, explore the examples folder.

For SDK configuration, please refer to the config description.

Supported Features:

Account creation and authorisation.

Order Management.

Account Management.

Transfers.

Withdrawals (for Starknet wallets only).

Market Information.

We are committed to enhancing the SDK with more functionalities based on user feedback and evolving market needs.

Mainnet
Our Mainnet is running on Starknet.

Base URL for the Mainnet API endpoints: https://api.starknet.extended.exchange/.

UI URL: https://app.extended.exchange/perp.

Testnet
Our Testnet is running on Sepolia.

Base URL for the Testnet API endpoints: https://api.starknet.sepolia.extended.exchange/.

UI URL: https://starknet.sepolia.extended.exchange/perp

On the testnet, users can claim $1,000 worth of test USDC per hour for each wallet. This can be done by clicking the 'Claim' button in the 'Account' section, located at the bottom right of the Extended Testnet Trade screen.

Allowed HTTP Verbs
GET: Retrieves a resource or list of resources.

POST: Creates a resource.

PATCH: Updates a resource.

DELETE: Deletes a resource.

Authentication
Due to the trustless, self-custody nature of the Extended exchange, transactions involving user funds require both an API key and a valid Stark signature.

For order management, both an API key and Stark signature are necessary. For other endpoints, only the API key signature is required. Stark signatures are generated using a private Stark key.

Account Creation, API and Stark Key Management
Currently, accounts can be created through the SDK or the User Interface:

SDK - refer to the onboarding example.

User Interface - connect your wallet on extended.exchange to create your Extended account.

You can create up to ten Extended sub-accounts per one wallet address. You can add and manage all sub-accounts associated with your connected wallet in the 'Account' section, located at the bottom right of the Extended Trade screen.

On the API management page, you can obtain API keys, Stark keys, and Vault numbers for each of your sub-accounts. Note that each sub-account is a separate Starknet position and therefore has unique API and Stark keys.

Authenticate Using API Key
Extended uses a simplified authentication scheme for API access. Include your API key in the HTTP header as follows: X-Api-Key: <API_KEY_FROM_API_MANAGEMENT_PAGE_OF_UI>.

Mandatory headers
For both REST and WebSocket API requests, the User-Agent header is required.

Rate Limits
REST API endpoints are subject to rate limits. For real-time data, consider using the WebSockets API instead.

All REST API endpoints are throttled by IP address. Currently, the rate limit is set at 1,000 requests per minute, shared across all endpoints. We plan to increase these limits as our system expands. If you require an increase in the rate limit now, please reach out to our team on Discord.

Higher rate limit of 60,000 requests per 5 minutes apply for the market makers.

When a REST API rate limit is exceeded, a 429 status code will be returned.

Pagination
Paginated response schema:

type PaginatedResponse = {
  "status": "ok" | "error"
  "data": object | object[] | string | number,
  "error": {
    "code": number,
    "message": string
  },
  "pagination": {
    "cursor": number // Current cursor
    "count": number  // Count of the items in the response
  }
}
General not paginated response schema:

type GeneralResponse = {
  "status": "ok" | "error",
  "data": object | object[] | string | number,
  "error": {
    "code": number,
    "message": string
  }
}
The Extended API uses a cursor-based pagination model across all endpoints that may return large volumes of items.

Items are automatically sorted in descending order by ID unless otherwise specified in the endpoint description. As IDs increase over time, the most recent items are always returned first.

Pagination parameters are passed via the query string. These parameters include:

Parameter	Required	Type	Description
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, use the cursor from the pagination section of the previous response.
limit	no	number	The maximum number of items that should be returned.
Public REST-API
The following Public REST API endpoints enable users to access comprehensive information about available markets, their configurations, and trading statistics.

Get markets
HTTP Request
GET /api/v1/info/markets?market={market}

Get a list of available markets, their configurations, and trading statistics.

To request data for several markets, use the following format: GET /api/v1/info/markets?market=market1&market=market2.

Please note that the margin schedule by market is not covered by this endpoint. For more details on the margin schedule, please refer to the documentation.

Market statuses
Status	Description
ACTIVE	Market is active, and all types of orders are permitted.
REDUCE_ONLY	Market is in reduce only mode, and only reduce only orders are allowed.
DELISTED	Market is delisted, and trading is no longer permitted.
PRELISTED	Market is in prelisting stage, and trading not yet available.
DISABLED	Market is completly disabled, and trading is not allowed.
Query Parameters
Parameter	Required	Type	Description
market	no	string[]	List of names of the requested markets.
Response example:

{
  "status": "ok",
  "data": [
    {
      "name": "BTC-USD",
      "assetName": "BTC",
      "assetPrecision": 6,
      "collateralAssetName": "USD",
      "collateralAssetPrecision": 6,
      "active": true,
      "status": "ACTIVE",
      "marketStats": {
        "dailyVolume": "39659164065",
        "dailyVolumeBase": "39659164065",
        "dailyPriceChangePercentage": "5.57",
        "dailyLow": "39512",
        "dailyHigh": "42122",
        "lastPrice": "42000",
        "askPrice": "42005",
        "bidPrice": "39998",
        "markPrice": "39950",
        "indexPrice": "39940",
        "fundingRate": "0.001",
        "nextFundingRate": 1701563440,
        "openInterest": "1245.2",
        "openInterestBase": "1245.2"
      },
      "tradingConfig": {
        "minOrderSize": "0.001",
        "minOrderSizeChange": "0.001",
        "minPriceChange": "0.001",
        "maxMarketOrderValue": "1000000",
        "maxLimitOrderValue": "5000000",
        "maxPositionValue": "10000000",
        "maxLeverage": "50",
        "maxNumOrders": "200",
        "limitPriceCap": "0.05",
        "limitPriceFloor": "0.05"
      },
      "l2Config": {
        "type": "STARKX",
        "collateralId": "0x35596841893e0d17079c27b2d72db1694f26a1932a7429144b439ba0807d29c",
        "collateralResolution": 1000000,
        "syntheticId": "0x4254432d3130000000000000000000",
        "syntheticResolution": 10000000000
      }
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].name	yes	string	Name of the market.
data[].assetName	yes	string	Name of the base asset.
data[].assetPrecision	yes	number	Number of decimals for the base asset.
data[].collateralAssetName	yes	string	Name of the collateral asset.
data[].collateralAssetPrecision	yes	number	Number of decimals for the collateral asset.
data[].active	yes	boolean	Indicates if the market is currently active. Can be true or false.
data[].status	yes	string	Market status.
data[].marketStats.dailyVolume	yes	string	Trading volume of the market in the previous 24 hours in the collateral asset.
data[].marketStats.dailyVolumeBase	yes	string	Trading volume of the market in the previous 24 hours in the base asset.
data[].marketStats.dailyPriceChange	yes	string	Absolute price change of the last trade price over the past 24 hours.
data[].marketStats.dailyPriceChangePercentage	yes	string	Percent price change of the last trade price over the past 24 hours.
data[].marketStats.dailyLow	yes	string	Lowest trade price over the past 24 hours.
data[].marketStats.dailyHigh	yes	string	Highest trade price over the past 24 hours.
data[].marketStats.lastPrice	yes	string	Last price of the market.
data[].marketStats.askPrice	yes	string	Current best ask price of the market.
data[].marketStats.bidPrice	yes	string	Current best bid price of the market.
data[].marketStats.markPrice	yes	string	Current mark price of the market.
data[].marketStats.indexPrice	yes	string	Current index price of the market.
data[].marketStats.fundingRate	yes	string	Current funding rate, calculated every minute.
data[].marketStats.nextFundingRate	yes	number	Timestamp of the next funding update.
data[].marketStats.openInterest	yes	string	Open interest in collateral asset.
data[].marketStats.openInterestBase	yes	string	Open interest in base asset.
data[].tradingConfig.minOrderSize	yes	string	Minimum order size for the market.
data[].tradingConfig.minOrderSizeChange	yes	string	Minimum order size change for the market.
data[].tradingConfig.minPriceChange	yes	string	Minimum price change for the market.
data[].tradingConfig.maxMarketOrderValue	yes	string	Maximum market order value for the market.
data[].tradingConfig.maxLimitOrderValue	yes	string	Maximum limit order value for the market.
data[].tradingConfig.maxPositionValue	yes	string	Maximum position value for the market.
data[].tradingConfig.maxLeverage	yes	string	Maximum leverage available for the market.
data[].tradingConfig.maxNumOrders	yes	string	Maximum number of open orders for the market.
data[].tradingConfig.limitPriceCap	yes	string	Limit order price cap.
data[].tradingConfig.limitPriceFloor	yes	string	Limit order floor ratio.
data[].l2Config.type	yes	string	Type of Layer 2 solution. Currently, only 'STARKX' is supported.
data[].l2Config.collateralId	yes	string	Starknet collateral asset ID.
data[].l2Config.collateralResolution	yes	number	Collateral asset resolution, the number of quantums (Starknet units) that fit within one "human-readable" unit of the collateral asset.
data[].l2Config.syntheticId	yes	string	Starknet synthetic asset ID.
data[].l2Config.syntheticResolution	yes	number	Synthetic asset resolution, the number of quantums (Starknet units) that fit within one "human-readable" unit of the synthetic asset.
Get market statistics
HTTP Request
GET /api/v1/info/markets/{market}/stats

Get the latest trading statistics for an individual market.

Please note that the returned funding rate represents the most recent funding rate, which is calculated every minute.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": {
    "dailyVolume": "10283410.122959",
    "dailyVolumeBase": "3343.1217",
    "dailyPriceChange": "-26.00",
    "dailyPriceChangePercentage": "-0.0084",
    "dailyLow": "3057.98",
    "dailyHigh": "3133.53",
    "lastPrice": "3085.70",
    "askPrice": "3089.05",
    "bidPrice": "3087.50",
    "markPrice": "3088.439710293828",
    "indexPrice": "3089.556987078441",
    "fundingRate": "-0.000059",
    "nextFundingRate": 1716192000000,
    "openInterest": "35827242.257619",
    "openInterestBase": "11600.4344",
    "deleverageLevels": {
      "shortPositions": [
        {
          "level": 1,
          "rankingLowerBound": "-1354535.1454"
        },
        {
          "level": 2,
          "rankingLowerBound": "-6.3450"
        },
        {
          "level": 3,
          "rankingLowerBound": "-0.3419"
        },
        {
          "level": 4,
          "rankingLowerBound": "0.0000"
        }
      ],
      "longPositions": [
        {
          "level": 1,
          "rankingLowerBound": "-2978.4427"
        },
        {
          "level": 2,
          "rankingLowerBound": "0.0000"
        },
        {
          "level": 3,
          "rankingLowerBound": "0.0000"
        },
        {
          "level": 4,
          "rankingLowerBound": "0.0001"
        }
      ]
    }
  }
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.dailyVolume	yes	string	Trading volume of the market in the previous 24 hours in the collateral asset.
data.dailyVolumeBase	yes	string	Trading volume of the market in the previous 24 hours in the base asset.
data.dailyPriceChange	yes	string	Absolute price change of the last trade price over the past 24 hours.
data.dailyPriceChangePercentage	yes	string	Percent price change of the last trade price over the past 24 hours.
data.dailyLow	yes	string	Lowest trade price over the past 24 hours.
data.dailyHigh	yes	string	Highest trade price over the past 24 hours.
data.lastPrice	yes	string	Last price of the market.
data.askPrice	yes	string	Current best ask price of the market.
data.bidPrice	yes	string	Current best bid price of the market.
data.markPrice	yes	string	Current mark price of the market.
data.indexPrice	yes	string	Current index price of the market.
data.fundingRate	yes	string	Current funding rate, calculated every minute.
data.nextFundingRate	yes	number	Timestamp of the next funding update.
data.openInterest	yes	string	Open interest in collateral asset.
data.openInterestBase	yes	string	Open interest in base asset.
data.deleverageLevels	yes	enum	Auto Deleveraging (ADL) levels for long and short positions, ranging from level 1 (lowest risk) to level 4 (highest risk) of ADL. For details, please refer to the documentation.
Get market order book
HTTP Request
GET /api/v1/info/markets/{market}/orderbook

Get the latest orderbook for an individual market.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": {
    "market": "BTC-USD",
    "bid": [
      {
        "qty": "0.04852",
        "price": "61827.7"
      },
      {
        "qty": "0.50274",
        "price": "61820.5"
      }
    ],
    "ask": [
      {
        "qty": "0.04852",
        "price": "61840.3"
      },
      {
        "qty": "0.4998",
        "price": "61864.1"
      }
    ]
  }
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.bid	yes	object[]	List of bid orders.
data.bid[].qty	yes	string	Qty for the price level.
data.bid[].price	yes	string	Bid price.
data.ask	yes	object[]	List of ask orders.
data.ask[].qty	yes	string	Qty for the price level.
data.ask[].price	yes	string	Ask price.
Get market last trades
HTTP Request
GET /api/v1/info/markets/{market}/trades

Get the latest trade for an individual market.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": [
    {
      "i": 1844000421446684673,
      "m": "BTC-USD",
      "S": "SELL",
      "tT": "TRADE",
      "T": 1728478935001,
      "p": "61998.5",
      "q": "0.04839"
    },
    {
      "i": 1844000955650019328,
      "m": "BTC-USD",
      "S": "SELL",
      "tT": "TRADE",
      "T": 1728479062365,
      "p": "61951.4",
      "q": "0.00029"
    }
  ]
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Type	Description
data[].i	number	Trade ID.
data[].m	string	Market name.
data[].S	string	Side of taker trades. Can be BUY or SELL.
data[].tT	string	Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.
data[].T	number	Timestamp (in epoch milliseconds) when the trade happened.
data[].p	string	Trade price.
data[].q	string	Trade quantity in base asset.
Get candles history
HTTP Request
GET /api/v1/info/candles/{market}/{candleType}

Get the candles history for an individual market for the timeframe specified in the request. Candles are sorted by timestamp in descending order.

Available price types include:

Trades (last) price: GET /api/v1/info/candles/{market}/trades.

Mark price: GET /api/v1/info/candles/{market}/mark-prices.

Index price: GET /api/v1/info/candles/{market}/index-prices.

The endpoint returns a maximum of 10,000 records.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
candleType	yes	string	Price type. Can be trades, mark-prices, or index-prices.
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	The time interval between data points.
limit	yes	number	The maximum number of items that should be returned.
endTime	no	number	End timestamp (in epoch milliseconds) for the requested period.
Response example:

{
  "status": "OK",
  "data": [
    {
      "o": "65206.2",
      "l": "65206.2",
      "h": "65206.2",
      "c": "65206.2",
      "v": "0.0",
      "T": 1715797320000
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR
data[].o	yes	string	Open price.
data[].c	yes	string	Close price.
data[].h	yes	string	Highest price.
data[].l	yes	string	Lowest price.
data[].v	yes	string	Trading volume (Only for trades candles).
data[].T	yes	number	Starting timestamp (in epoch milliseconds) for the candle.
Get funding rates history
HTTP Request
GET /api/v1/info/{market}/funding?startTime={startTime}&endTime={endTime}

Get the funding rates history for an individual market for the timeframe specified in the request. The funding rates are sorted by timestamp in descending order.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

While the funding rate is calculated every minute, it is only applied once per hour. The records represent the 1-hour rates that were applied for the payment of funding fees.

For details on how the funding rate is calculated on Extended, please refer to the documentation.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Names of the requested market.
Query Parameters
Parameter	Required	Type	Description
startTime	yes	number	Starting timestamp (in epoch milliseconds) for the requested period.
endTime	yes	number	Ending timestamp (in epoch milliseconds) for the requested period.
cursor	no	number	Determines the offset of the returned result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "m": "BTC-USD",
      "T": 1701563440,
      "f": "0.001"
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].m	yes	string	Name of the requested market.
data[].T	yes	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
data[].f	yes	string	Funding rates used for funding fee payments.
Get open interest history
HTTP Request
GET /api/v1/info/{market}/open-interests?interval={interval}&startTime={startTime}&endTime={endTime}

Get the open interest history for an individual market for the timeframe specified in the request. The open interests are sorted by timestamp in descending order.

The endpoint returns a maximum of 300 records; proper combination of start and end time should be used to access records beyond this limit.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Names of the requested market.
Query Parameters
Parameter	Required	Type	Description
startTime	yes	number	Starting timestamp (in epoch milliseconds) for the requested period.
endTime	yes	number	Ending timestamp (in epoch milliseconds) for the requested period.
interval	yes	enum	P1H for hour and P1D for day
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "i": "151193.8952300000000000",
      "I": "430530.0000000000000000",
      "t": 1749513600000
    },
    {
      "i": "392590.9522500000000000",
      "I": "1147356.0000000000000000",
      "t": 1749600000000
    },
    {
      "i": "397721.7285100000000000",
      "I": "1224362.0000000000000000",
      "t": 1749686400000
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].i	yes	string	Open interest in USD.
data[].I	yes	string	Open interest in synthetic asset.
data[].t	yes	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
Get builder dashboard
GET /api/v1/info/builder/dashboard

Response example:

{
  "status": "OK",
  "data": {
    "total": [
      {
        "builderName": "FlowBot",
        "volume": "439912489.2299",
        "extendedFees": "106512.842391",
        "activeUsers": 181
      }
    ],
    "daily": [
      {
        "date": "2025-12-15",
        "builderName": "FlowBot",
        "volume": "12720299.02594",
        "extendedFees": "3180.074578",
        "activeUsers": 24
      },
      {
        "date": "2025-12-16",
        "builderName": "FlowBot",
        "volume": "11827429.94026",
        "extendedFees": "2956.857352",
        "activeUsers": 21
      }
    ]
  }
}
Returns builder dashboard statistics including total and daily trading volume, fees, and active users for the authenticated builder.

Response
Parameter	Required	Type	Description
data.total	yes	object[]	Array containing total aggregated statistics.
data.total[].builderName	yes	string	Name of the builder.
data.total[].volume	yes	string	Total trading volume generated by the builder.
data.total[].extendedFees	yes	string	Total fees earned by the builder to the extended exchange.
data.total[].activeUsers	yes	number	Total number of active users for the builder.
data.daily	yes	object[]	Array containing daily statistics.
data.daily[].date	yes	string	Date in YYYY-MM-DD format.
data.daily[].builderName	yes	string	Name of the builder.
data.daily[].volume	yes	string	Daily trading volume generated by the builder.
data.daily[].extendedFees	yes	string	Daily fees earned by the builder to the extended exchange.
data.daily[].activeUsers	yes	number	Number of active users for the builder on that date.
Private REST-API
Account
You can create up to ten Extended sub-accounts for each wallet address. For more details, please refer to the Authentication section of the API Documentation.

The Private API endpoints listed below grant access to details specific to each sub-account, such as balances, transactions, positions, orders, trades, and the fee rates applied. Additionally, there are endpoints for retrieving the current leverage and adjusting it.

Please note that all endpoints in this section will only return records for the authenticated sub-account.

Get account details
HTTP Request
GET /api/v1/user/account/info

Response example:

 {
  "status": "OK",
  "data": {
    "status": "ACTIVE",
    "l2Key": "0x123",
    "l2Vault": 321,
    "accountId": 123,
    "description": "abc",
    "bridgeStarknetAddress": "0x21be84f913dbddbfc0a3993e1f949933139f427f88eb6bfd247ab3ef7174487"
  }
}
Get current account details.

Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.status	yes	string	Account status.
data.l2Key	yes	string	Account public key in perp contract.
data.l2Vault	yes	string	Position ID in perp contract.
data.accountId	yes	string	Account ID.
data.description	no	string	Account description (name).
data.bridgeStarknetAddress	yes	string	Starknet account address for EVM bridging.
Get balance
HTTP Request
GET /api/v1/user/balance

Get key balance details for the authenticated sub-account. Returns a 404 error if the user’s balance is 0.

Account Balance = Deposits - Withdrawals + Realised PnL.

Equity = Account Balance + Unrealised PnL.

Available Balance for Trading = Equity - Initial Margin Requirement.

Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirement).

Unrealised PnL (mark-price-based) = The sum of unrealised PnL across open positions, calculated as Position Size * (Mark Price - Entry Price).

Unrealised PnL (mid-price-based) = The sum of unrealised PnL across open positions, calculated as Position Size * (Mid Price - Entry Price).

Initial Margin Requirement for a given market = Max(Abs(Position Value + Value of Buy Orders), Abs(Position Value + Value of Sell Orders))*1/Leverage.

Account Margin Ratio = Maintenance Margin requirement of all open positions / Equity. Liquidation is triggered when Account Margin Ratio > 100%.

Account Exposure = Sum(All positions value)

Account Leverage = Exposure / Equity.

Response example:

{
  "status": "OK",
  "data": {
    "collateralName": "USDC",
    "balance": "13500",
    "equity": "12000",
    "availableForTrade": "1200",
    "availableForWithdrawal": "100",
    "unrealisedPnl": "-10.1",
    "initialMargin": "160",
    "marginRatio": "1.5",
    "exposure": "12751.859629",
    "leverage": "1275.1860",
    "updatedTime": 1701563440
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.collateralName	yes	string	Name of the collateral asset used for the account.
data.balance	yes	string	Account balance expressed in the collateral asset, also known as Wallet balance.
data.equity	yes	string	Equity of the account.
data.availableForTrade	yes	string	Available Balance for Trading.
data.availableForWithdrawal	yes	string	Available Balance for Withdrawals.
data.unrealisedPnl	yes	string	Current unrealised PnL of the account.
data.initialMargin	yes	string	Collateral used to open the positions and orders.
data.marginRatio	yes	string	Margin ratio of the account.
data.exposure	yes	string	Exposure of the account.
data.leverage	yes	string	Leverage of the account.
data.updatedTime	yes	number	Timestamp (in epoch milliseconds) when the server generated the balance message.
Get deposits, withdrawals, transfers history
HTTP Request
GET /api/v1/user/assetOperations?&type={type}&status={status}

Get the history of deposits, withdrawals, and transfers between sub-accounts for the authenticated sub-account. Optionally, the request can be filtered by a specific transaction type or status.

The endpoint returns 50 records per page; pagination should be used to access records beyond this limit. Transactions are sorted by timestamp in descending order.

Transactions types
Transaction	Description
DEPOSIT	Deposit.
CLAIM	Testing funds claim. Available only on Extended Testnet.
TRANSFER	Transfer between sub-accounts within one wallet.
WITHDRAWAL	Withdrawal.
Transactions statuses
Status	Description
CREATED	Transaction created on Extended.
IN_PROGRESS	Transaction is being processed by Extended, Starknet or bridge provider.
COMPLETED	Transaction completed.
REJECTED	Transaction rejected.
Response example:

{
    "status": "OK",
    "data": [
        {
            "id": "1951255127004282880",
            "type": "TRANSFER",
            "status": "COMPLETED",
            "amount": "-3.0000000000000000",
            "fee": "0",
            "asset": 1,
            "time": 1754050449502,
            "accountId": 100009,
            "counterpartyAccountId": 100023
        },
        {
            "id": "0x6795eac4ebbdd9fb88f85e3ce4ce4e61895049591c89ad5db8046a4546d2cdd",
            "type": "DEPOSIT",
            "status": "COMPLETED",
            "amount": "4.9899990000000000",
            "fee": "0.0000000000000000",
            "asset": 1,
            "time": 1753872990528,
            "accountId": 100009,
            "transactionHash": "0x93829e61480b528bb18c1b94f0afbc672fb2b340fbfd2f329dffc4180e24b894",
            "chain": "ETH"
        },
        {
            "id": "1950490023665475584",
            "type": "WITHDRAWAL",
            "status": "COMPLETED",
            "amount": "-4.0000000000000000",
            "fee": "0.0001000000000000",
            "asset": 1,
            "time": 1753868034651,
            "accountId": 100009,
            "transactionHash": "0x6d89968d72fc766691d4772048edaf667c88894aedf71f0490c2592c1d268691",
            "chain": "ETH"
        },
    ],
    "pagination": {
        "cursor": 23,
        "count": 23
    }
}
Query Parameters
Parameter	Required	Type	Description
type	no	string	Transaction type. Refer to the list of transaction types in the endpoint description above.
status	no	string	Transaction status. Refer to the list of statuses in the endpoint description above.
cursor	no		Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response
Parameter	Required	Type	Description
status	yes	string	Response status. Can be OK or ERROR.
data[].id	yes	number or string	Transaction ID. A number assigned by Extended for transfers and withdrawals. An onchain id string for deposits.
data[].type	yes	string	Transaction type. Refer to the list of transaction types in the endpoint description above.
data[].status	yes	string	Transaction status. Refer to the list of statuses in the endpoint description above.
data[].amount	yes	string	Transaction amount, absolute value in collateral asset.
data[].fee	yes	string	Fee paid.
data[].asset	yes	string	Collateral asset name.
data[].time	yes	number	Timestamp (epoch milliseconds) when the transaction was updated.
data[].accountId	yes	number	Account ID; source account for transfers and withdrawals; destination account for deposits.
data[].counterpartyAccountId	no	number	Account ID; destination account for transfers.
data[].transactionHash	no	string	Onchain transaction hash. Not available for transfers.
data[].chain	no	string	Source chain name for deposits; target chain name for withdrawals.
Get positions
HTTP Request
GET /api/v1/user/positions?market={market}&side={side}

Get all open positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for multiple markets, use the following format: GET /api/v1/user/positions?market=market1&market2.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be LONG or SHORT.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1,
      "accountId": 1,
      "market": "BTC-USD",
      "side": "LONG",
      "leverage": "10",
      "size": "0.1",
      "value": "4000",
      "openPrice": "39000",
      "markPrice": "40000",
      "liquidationPrice": "38200",
      "margin": "20",
      "unrealisedPnl": "1000",
      "realisedPnl": "1.2",
      "tpTriggerPrice": "41000",
      "tpLimitPrice": "41500",
      "slTriggerPrice": "39500",
      "slLimitPrice": "39000",
      "adl": "2.5",
      "maxPositionSize": "0.2",
      "createdTime": 1701563440000,
      "updatedTime": 1701563440
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Position ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].leverage	yes	string	Position leverage.
data[].size	yes	string	Position size, absolute value in base asset.
data[].value	yes	string	Position value, absolute value in collateral asset.
data[].openPrice	yes	string	Position's open (entry) price.
data[].markPrice	yes	string	Current mark price of the market.
data[].liquidationPrice	yes	string	Position's liquidation price.
data[].margin	yes	string	Position's margin in collateral asset.
data[].unrealisedPnl	yes	string	Position's Unrealised PnL.
data[].realisedPnl	yes	string	Position's Realised PnL.
data[].tpTriggerPrice	no	string	Take Profit Trigger price.
data[].tpLimitPrice	no	string	Take Profit Limit price.
data[].slTriggerPrice	no	string	Stop Loss Trigger price.
data[].slLimitPrice	no	string	Stop Loss Limit price.
data[].maxPositionSize	yes	string	Maximum allowed position size, absolute value in base asset.
data[].adl	yes	string	Position's Auto-Deleveraging (ADL) ranking in the queue, expressed as a percentile. A value closer to 100 indicates a higher likelihood of being ADLed.
data[].createdTime	yes	number	Timestamp (epoch milliseconds) when the position was created.
data[].updatedTime	yes	number	Timestamp (epoch milliseconds) when the position was updated.
Get positions history
HTTP Request
GET /api/v1/user/positions/history?market={market}&side={side}

Get all open and closed positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for several markets, use the following format: GET /api/v1/user/positions/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be long or short.
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "accountId": 1,
      "market": "BTC-USD",
      "side": "LONG",
      "exitType": "TRADE",
      "leverage": "10",
      "size": "0.1",
      "maxPositionSize": "0.2",
      "openPrice": "39000",
      "exitPrice": "40000",
      "realisedPnl": "1.2",
      "createdTime": 1701563440000,
      "closedTime": 1701563440
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Position ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].exitType	no	string	The exit type of the last trade that reduced the position. Can be TRADE, LIQUIDATION, or DELEVERAGE.
data[].leverage	yes	string	Position leverage.
data[].size	yes	string	Position size, absolute value in base asset.
data[].maxPositionSize	yes	string	Maximum position size during the position's lifetime, absolute value in base asset.
data[].openPrice	yes	string	The weighted average price of trades that contributed to increasing the position.
data[].exitPrice	no	string	The weighted average price of trades that contributed to decreasing the position.
data[].realisedPnl	yes	string	Position Realised PnL.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) when the position was created.
data[].closedTime	no	number	Timestamp (in epoch milliseconds) when the position was closed, applicable only for closed positions.
Get open orders
HTTP Request
GET /api/v1/user/orders?market={market}&type={type}&side={side}

Get all open orders for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, conditional, tpsl or twap).

Open orders correspond to the following order statuses from the list below: new, partially filled, untriggered.

To request data for several markets, use the following format: GET /api/v1/user/orders?market=market1&market2.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
Order status reasons (when cancelled or rejected)
Reason	Description
NONE	Order was accepted.
UNKNOWN	Technical status reason.
UNKNOWN_MARKET	Market does not exist.
DISABLED_MARKET	Market is not active.
NOT_ENOUGH_FUNDS	Insufficient balance to create order.
NO_LIQUIDITY	Not enough liquidity in the market to execute the order.
INVALID_FEE	Fee specified in the create order request is invalid.
INVALID_QTY	Quantity specified is invalid.
INVALID_PRICE	Price specified is invalid.
INVALID_VALUE	Order exceeds the maximum value.
UNKNOWN_ACCOUNT	Account does not exist.
SELF_TRADE_PROTECTION	Order cancelled to prevent self-trading.
POST_ONLY_FAILED	Order could not be posted as a post-only order.
REDUCE_ONLY_FAILED	Reduce-only order failed due to position size conflict.
INVALID_EXPIRE_TIME	Expiration time specified is invalid.
POSITION_TPSL_CONFLICT	TPSL order for the entire position already exists.
INVALID_LEVERAGE	Leverage specified is invalid.
PREV_ORDER_NOT_FOUND	The order to be replaced does not exist.
PREV_ORDER_TRIGGERED	The order to be replaced has been triggered and cannot be replaced.
TPSL_OTHER_SIDE_FILLED	The opposite side of a TP/SL order has been filled.
PREV_ORDER_CONFLICT	Conflict with an existing order during replacement.
ORDER_REPLACED	Order has been replaced by another order.
POST_ONLY_MODE	Exchange is in post-only mode, only post-only orders are allowed.
REDUCE_ONLY_MODE	Exchange is in reduce-only mode, only reduce-only orders are allowed.
TRADING_OFF_MODE	Trading is currently disabled.
NEGATIVE_EQUITY	Account has negative equity.
ACCOUNT_LIQUIDATION	Account is under liquidation.
Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
type	no	string	Order type. Can be LIMIT, CONDITIONAL, TPSL or TWAP.
side	no	string	Order side. Can be BUY or SELL.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1775511783722512384,
      "accountId": 3017,
      "externalId": "2554612759479898620327573136214120486511160383028978112799136270841501275076",
      "market": "ETH-USD",
      "type": "LIMIT",
      "side": "BUY",
      "status": "PARTIALLY_FILLED",
      "price": "3300",
      "averagePrice": "3297.00",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "trigger": {
        "triggerPrice": "3300",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "takeProfit": {
        "triggerPrice": "3500",
        "triggerPriceType": "LAST",
        "price": "3340",
        "priceType": "MARKET"
      },
      "stopLoss": {
        "triggerPrice": "2800",
        "triggerPriceType": "LAST",
        "price": "2660",
        "priceType": "MARKET"
      },
      "reduceOnly": false,
      "postOnly": false,
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1712754771819
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type. Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get orders history
HTTP Request
GET /api/v1/user/orders/history?market={market}&type={type}&side={side}&id={id}&externalId={externalId}

Get orders history for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, market, conditional, tpsl or twap). Note: Scaled orders are represented as multiple individual limit orders in the system.

Orders history corresponds to the following order statuses from the list below: filled, cancelled, rejected, expired.

To request data for several markets, use the following format: GET /api/v1/user/orders/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. The records for closed non-filled orders are available only for the past 7 days.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
Query Parameters
Parameter	Required	Type	Description
id	no	number	List of internal Ids of the requested orders.
externalId	no	string[]	List of external Ids of the requested orders.
market	no	string[]	List of names of the requested markets.
type	no	string	Order type. Can be limit, market, conditional, tpsl or twap.
side	no	string	Order side. Can be buy or sell.
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "externalId": "ExtId-1",
      "accountId": 1,
      "market": "BTC-USD",
      "status": "FILLED",
      "type": "LIMIT",
      "side": "BUY",
      "price": "39000",
      "averagePrice": "39000",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "reduceOnly": false,
      "postOnly": false,
      "trigger": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "tpslType": "ORDER",
      "takeProfit": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "stopLoss": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1706563440
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get order by id
HTTP Request
GET /api/v1/user/orders/{id}

Get order by id for the authenticated sub-account.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
URL Parameters
Parameter	Required	Type	Description
id	yes	number	Order to be retrieved, ID assigned by Extended.
Response example:

{
  "status": "OK",
  "data": {
    "id": 1784963886257016832,
    "externalId": "ExtId-1",
    "accountId": 1,
    "market": "BTC-USD",
    "status": "FILLED",
    "type": "LIMIT",
    "side": "BUY",
    "price": "39000",
    "averagePrice": "39000",
    "qty": "0.2",
    "filledQty": "0.1",
    "payedFee": "0.0120000000000000",
    "reduceOnly": false,
    "postOnly": false,
    "trigger": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "triggerPriceDirection": "UP",
      "executionPriceType": "MARKET"
    },
    "tpslType": "ORDER",
    "takeProfit": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "price": "35000",
      "priceType": "MARKET",
      "starkExSignature": ""
    },
    "stopLoss": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "price": "35000",
      "priceType": "MARKET",
      "starkExSignature": ""
    },
    "createdTime": 1701563440000,
    "updatedTime": 1701563440000,
    "timeInForce": "IOC",
    "expireTime": 1706563440
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.id	yes	number	Order ID assigned by Extended.
data.externalId	yes	string	Order ID assigned by user.
data.accountId	yes	number	Account ID.
data.market	yes	string	Market name.
data.status	yes	string	Order status.
data.statusReason	no	string	Reason for REJECTED or CANCELLED status.
data.type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data.side	yes	string	Order side. Can be BUY or SELL.
data.price	no	string	Worst accepted price in the collateral asset.
data.averagePrice	no	string	Actual filled price, empty if not filled.
data.qty	yes	string	Order size in base asset.
data.filledQty	no	string	Actual filled quantity in base asset.
data.payedFee	no	string	Paid fee.
data.reduceOnly	no	boolean	Whether the order is Reduce-only.
data.postOnly	no	boolean	Whether the order is Post-only.
data.trigger.triggerPrice	no	string	Trigger price for conditional orders.
data.trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data.trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data.trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data.tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data.takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data.takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data.takeProfit.price	no	string	Take Profit order price.
data.takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data.stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data.stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data.stopLoss.price	no	string	Stop loss order price.
data.stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data.createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data.updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data.timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data.expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get orders by external id
HTTP Request
GET /api/v1/user/orders/external/{externalId}

Get orders by external id for the authenticated sub-account.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
URL Parameters
Parameter	Required	Type	Description
externalId	yes	number	Order to be retrieved, ID assigned by user.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "externalId": "ExtId-1",
      "accountId": 1,
      "market": "BTC-USD",
      "status": "FILLED",
      "type": "LIMIT",
      "side": "BUY",
      "price": "39000",
      "averagePrice": "39000",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "reduceOnly": false,
      "postOnly": false,
      "trigger": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "tpslType": "ORDER",
      "takeProfit": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "stopLoss": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1706563440
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get trades
HTTP Request
GET /api/v1/user/trades?market={market}&type={type}&side={side}

Get trades history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by trade type (trade, liquidation or deleverage) and side (buy or sell).

To request data for several markets, use the following format: GET /api/v1/user/trades?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
type	no	string	Trade type. Can be trade, liquidation or deleverage.
side	no	string	Order side. Can be buy or sell.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "accountId": 3017,
      "market": "BTC-USD",
      "orderId": 9223372036854775808,
      "externalId": "ext-1",
      "side": "BUY",
      "price": "58853.4000000000000000",
      "qty": "0.0900000000000000",
      "value": "5296.8060000000000000",
      "fee": "0.0000000000000000",
      "tradeType": "DELEVERAGE",
      "createdTime": 1701563440000,
      "isTaker": true
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Trade ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].orderId	yes	string	Order ID assigned by Extended.
data[].externalOrderId	yes	string	Order ID assigned by user. Populated only on websocket stream.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].averagePrice	yes	string	Actual filled price.
data[].filledQty	yes	string	Actual filled quantity in base asset.
data[].value	yes	string	Actual filled absolute nominal value in collateral asset.
data[].fee	yes	string	Paid fee.
data[].isTaker	yes	boolean	Whether the trade was executed as a taker.
data[].tradeType	yes	string	Trade type. Can be TRADE (for regular trades), LIQUIDATION (for liquidaton trades) or DELEVERAGE (for ADL trades).
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) when the trade happened.
Get funding payments
HTTP Request
GET /api/v1/user/funding/history?market={market}&side={side}&fromTime={fromTime}

Get funding payments history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by side (long or short) and from time as a start point.

To request data for several markets, use the following format: GET /api/v1/user/funding/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be long or short.
fromTime	yes	number	Starting timestamp (in epoch milliseconds).
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 8341,
      "accountId": 3137,
      "market": "BNB-USD",
      "positionId": 1821237954501148672,
      "side": "LONG",
      "size": "1.116",
      "value": "560.77401888",
      "markPrice": "502.48568",
      "fundingFee": "0",
      "fundingRate": "0",
      "paidTime": 1723147241346
    }
  ],
  "pagination": {
    "cursor": 8341,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Funding payment ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].positionId	yes	number	Position ID assigned by Extended.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].value	yes	string	Position value at funding payment time.
data[].markPrice	yes	string	Mark price at funding payment time
data[].fundingFee	yes	string	Funding payment size.
data[].fundingRate	yes	string	Funding rate.
data[].paidTime	yes	number	Timestamp (in epoch milliseconds) when the funding payment happened.
Get rebates
HTTP Request
GET /api/v1/user/rebates/stats

Get rebates related data for the authenticated sub-account.

Response example:

{
  "status": "OK",
  "data": [
    {
      "totalPaid": "0",
      "rebatesRate": "0",
      "marketShare": "0.002",
      "nextTierMakerShare": "0.01",
      "nextTierRebateRate": "0.00005"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.totalPaid	yes	string	Total rebates paid.
data.rebatesRate	yes	string	Current rebates rate.
data.marketShare	yes	string	Maker volume share.
data.nextTierMakerShare	yes	string	Maker volume share required to increase rebates.
data.nextTierRebateRate	yes	string	Rebates rate for next maker share threshold.
Get current leverage
HTTP Request
GET /api/v1/user/leverage?market={market}

Get current leverage for the authenticated sub-account. You can get current leverage for all markets, a single market, or multiple specific markets.

To request data for several markets, use the format GET/api/v1/user/leverage?market=market1&market=market2.

Query Parameters
Parameter	Required	Type	Description
market	no	string	Name of the requested market.
Response example:

{
  "status": "OK",
  "data": [
    {
      "market": "SOL-USD",
      "leverage": "10"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.leverage	yes	string	Current leverage.
Update leverage
HTTP Request
PATCH /api/v1/user/leverage

Update leverage for an individual market.

Modifying your leverage will impact your Available balance and Initial Margin requirements of your open position and orders in the market.

To adjust your leverage, you must meet two requirements:

The total value of your open position and triggered orders must remain below the maximum position value allowed for the selected leverage.

Your Available balance must be sufficient to cover the additional Margin requirements (if any) associated with the new leverage.

Failure to meet either of these criteria will result in an error.

For details on Margin requirements, please refer to the documentation.

Request example:

{
  "market": "BTC-USD",
  "leverage": "10"
}
Body Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
leverage	yes	string	Target leverage.
Response example:

{
  "status": "OK",
  "data": {
    "market": "BTC-USD",
    "leverage": "10"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.leverage	yes	string	Updated leverage.
Get fees
HTTP Request
GET /api/v1/user/fees?market={market}

Get current fees for the sub-account. Currently, Extended features a flat fee structure:

Taker: 0.025%

Maker: 0.000%

The team reserves the right to update the fee schedule going forward.

For updates on the Fee Schedule, please refer to the documentation.

Query Parameters
Parameter	Required	Type	Description
market	no	string	Name of the requested market.
builderId	no	string	builder client id
Response example:

{
  "status": "OK",
  "data": [
    {
      "market": "BTC-USD",
      "makerFeeRate": "0.00000",
      "takerFeeRate": "0.00025",
      "builderFeeRate": "0.0001"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.makerFeeRate	yes	string	Maker fee rate.
data.takerFeeRate	yes	string	Taker fee rate.
data.builderFeeRate	yes	string	Builder fee rate.
Order management
The Private API endpoints listed below allow you to create, cancel, and manage orders from the authenticated sub-account.

Starknet-Specific Logic
Extended settles all transactions on-chain on Starknet. As a result, order creation might differ from centralized exchanges in a few ways:

Stark Key Signature: Required for all order management endpoints. For details, please refer to the reference implementation in the Python SDK.

Price Parameter: All orders, including market orders, require a price as a mandatory parameter.

Fee Parameter: All orders require a fee as a mandatory parameter. The Fee parameter represents the maximum fee a user is willing to pay for an order. Use the maker fee for Post-only orders and the taker fee for all other orders. Enter the fee in decimal format (e.g., 0.1 for 10%). To view current fees, use the Get fees endpoint, which displays applicable fee rates.

Expiration Timestamp: All orders, including Fill or Kill and Immediate or Cancel orders, require an expiration timestamp as a mandatory parameter. When submitting orders via the API, enter the expiration time as an epoch timestamp in milliseconds. On the Mainnet, the maximum allowable expiration time is 90 days from the order creation date. On the Testnet, 28 days from the order creation date.

Market Orders: Extended does not natively support market orders. On the UI, market orders are created as limit Immediate-or-Cancel orders with a price parameter set to ensure immediate execution. For example, Market Buy Orders are set at the best ask price multiplied by 1.0075, and Market Sell Orders at the best bid price multiplied by 0.9925 (subtracting 0.75%).

TPSL Orders: Orders with Take Profit and/or Stop Loss require multiple signatures.

Create or edit order
HTTP Request
POST /api/v1/user/order

Create a new order or edit (replace) an open order. When you create an order via our REST API, the initial response will confirm whether the order has been successfully accepted. Please be aware that, although rare, orders can be canceled or rejected by the Matching Engine even after acceptance at the REST API level. To receive real-time updates on your order status, subscribe to the Account updates WebSocket stream. This stream provides immediate notifications of any changes to your orders, including confirmations, cancellations, and rejections.

Currently, we support limit, market, conditional and tpsl order types via API, along with reduce-only and post-only settings. For API trading, we offer the following Time-in-force settings: GTT (Good till time - default) and IOC (Immediate or cancel). On the Mainnet, the maximum allowable expiration time for GTT orders is 90 days from the order creation date. On the Testnet, 28 days from the order creation date. For details on supported order types and settings, please refer to the documentation.

To successfully place an order, it must meet the following requirements:

Trading Rules. For detailed information, please refer to the trading rules documentation.

Order Cost Requirements. For detailed information, please refer to the order cost documentation.

Margin Schedule Requirements. For detailed information, please refer to the margin schedule documentation.

Price requirements, which are described below.

Price requirements
Limit Orders
Long Limit Orders: Order Price ≤ Mark Price * (1+Limit Order Price Cap)
Short Limit Orders: Order Price ≥ Mark Price * (1-Limit Order Floor Ratio)
Market Orders
Long Market Order: Order Price ≤ Mark Price * (1 + 5%)
Short Market Order: Order Price ≥ Mark Price * (1 - 5%)
Conditional Orders
Short Conditional Orders: Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)
Long Conditional Orders: Order Price ≤ Trigger Price * (1+Limit Order Price Cap)
TPSL Orders
Entry order: Buy; TPSL order: Sell.

Validation	Stop loss	Take profit
Trigger price validation	Trigger price < Entry order price	Trigger price > Entry order price.
Limit price validation	Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)	Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)
Entry order: Sell; TPSL order: Buy.

Validation	Stop loss	Take profit
Trigger price validation	Trigger price > Entry order price.	Trigger price < Entry order price.
Limit price validation	Order Price ≤ Trigger Price * (1+Limit Order Price Cap)	Order Price ≤ Trigger Price * (1+Limit Order Price Cap)
Orders Edit
To edit (replace) an open order, add its ID as the cancelId parameter. You can edit multiple parameters at once. Editing is available for all orders except for triggered TPSL orders.

Order editing and validations:

If any updated parameter fails the validations described above, all updates will be rejected.
If validations fail at the REST API level, the initial open order remains unchanged.
In the rare event that validations pass at the REST API level but fail at the Matching Engine, both the updated order and the initial open order will be cancelled.
Editable Order Parameters:

For All Order Types (except triggered TPSL orders): Order price and Execution Order Price Type (market or limit)
For All Order Types (except untriggered entire position TPSL orders and triggered TPSL orders): Order size
For Conditional and Untriggered TPSL Orders: Trigger price
For Conditional Orders: Trigger price direction (up or down)
For Non-TPSL Orders: All TPSL parameters
Self trade protection
Self-trade protection is a mechanism that prevents orders from the same client or sub-account from executing against each other. When two such orders are about to match, the system applies the self-trade protection mode specified on the taker order to determine how to handle the potential self-match.

Value	Description
DISABLED	Self trade protection is disabled
ACCOUNT	Trades within same sub-account are disabled, trades between sub-accounts are enabled.
CLIENT	Trades within same sub-account and between sub-accounts are disabled.
Request
Request example:

{
  "id": "e581a9ca-c3a2-4318-9706-3f36a2b858d3",
  "market": "BTC-USDT",
  "type": "CONDITIONAL",
  "side": "BUY",
  "qty": "1",
  "price": "1000",
  "timeInForce": "GTT",
  "expiryEpochMillis": 1715884049245,
  "fee": "0.0002",
  "nonce": "876542",
  "settlement": {
    "signature": {
      "r": "0x17a89cb97c64f546d2dc9189e1ef73547487b228945dcda406cd0e4b8301bd3",
      "s": "0x385b65811a0fc92f109d5ebc30731efd158ee4e502945cd2fcb35a4947b045e"
    },
    "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
    "collateralPosition": "4272448241247734333"
  },
  "reduceOnly": true,
  "postOnly": false,
  "selfTradeProtectionLevel": "ACCOUNT",
  "trigger": {
    "triggerPrice": "12000",
    "triggerPriceType": "LAST",
    "direction": "UP",
    "executionPriceType": "LIMIT"
  },
  "tpSlType": "ORDER",
  "takeProfit": {
    "triggerPrice": "1050",
    "triggerPriceType": "LAST",
    "price": "1300",
    "priceType": "LIMIT",
    "settlement": {
      "signature": {
        "r": "0x5b45f0fb2b8e075f6a5f9b4c039ccf1c01c56aa212c63f943337b920103c3a1",
        "s": "0x46133ab89d90a3ae2a3a7680d2a27e30fa015c0c4979931164c51b52b27758a"
      },
      "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
      "collateralPosition": "4272448241247734333"
    }
  },
  "stopLoss": {
    "triggerPrice": "950",
    "triggerPriceType": "LAST",
    "price": "900",
    "priceType": "LIMIT",
    "settlement": {
      "signature": {
        "r": "0x5033ad23fe851d16ceec5dd99f2f0c9585c5abec3f09ec89a32a961536ba55",
        "s": "0x1234ee151a8b5c68efb4adaa2eaf1dcc4a5107d4446274a69389ef8abd2dcf"
      },
      "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
      "collateralPosition": "4272448241247734333"
    }
  },
  "builderFee": "0.0001",
  "builderId": 2017
}
Body Parameters
Parameter	Required	Type	Description
id	yes	string	Order ID assigned by user.
market	yes	string	Market name.
type	yes	string	Order type. Can be limit, market, conditional or tpsl.
side	yes	string	Order side. Can be buy or sell.
qty	yes	string	Order size in base asset.
price	yes	string	Worst accepted price in collateral asset. Note that price is optional for a tpsl type position.
reduceOnly	no	boolean	Whether the order should be Reduce-only.
postOnly	no	boolean	Whether the order should be Post-only.
timeInForce	yes	string	Time-in-force setting. Can be GTT (Good till time) or IOC (Immediate or cancel). This parameter will default to GTT.
expiryEpochMillis	yes	number	Timestamp (in epoch milliseconds) when the order expires if not filled. Cannot exceed 3 months from the order creation time.
fee	yes	string	Highest accepted fee for the trade, expressed in decimal format (e.g., 0.1 for 10%). Use the maker fee for Post-only orders and the taker fee for all other orders.
cancelId	no	string	External ID of the order that this order is replacing.
settlement	yes	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
nonce	yes	string	Nonce is part of the settlement and must be a number ≥1 and ≤2^31. Please make sure to check the Python SDK reference implementation.
selfTradeProtectionLevel	yes	string	Level of self trade protection. Can be DISABLED, ACCOUNT(default) and CLIENT.
trigger.triggerPrice	no	string	Price threshold for triggering a conditional order.
trigger.triggerPriceType	no	string	Type of price used for the order triggering. Can be last, mark or index.
trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be up (the order will be triggered when the price reaches or surpasses the set trigger price) or down (the order will be triggered when the price reaches or drops below the set trigger price).
trigger.executionPriceType	no	string	Type of price used for the order execution. Can be limit or market.
tpSlType	no	string	TPSL type determining TPSL order size. Can be order or position.
takeProfit.triggerPrice	no	string	Take Profit Trigger price.
takeProfit.triggerPriceType	no	string	Type of price used for the Take Profit order triggering. Can be last, mid (to be added soon), mark or index.
takeProfit.price	no	string	Take Profit order price.
takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as market or limit order.
takeProfit.settlement	no	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
triggerPrice	no	string	Stop loss Trigger price.
stopLoss.triggerPriceType	no	string	Type of price used for the Stop Loss order triggering. Can be last, mid (to be added soon), mark or index.
stopLoss.price	no	string	Stop loss order price.
stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as market or limit order.
stopLoss.settlement	no	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
builderFee	no	number	Amount that user will pay builder (an alternative ui maker) for the trade. Expressed in decimal format (e.g., 0.1 for 10%)
builderId	no	number	Builder client id that will receive the builderFee
Response example:

{
  "status": "OK",
  "data": {
    "id": 1791389621914243072,
    "externalId": "31097979600959341921260192820644698907062844065707793749567497227004358262"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.id	yes	number	Order ID assigned by Extended.
data.externalId	yes	string	Order ID assigned by user.
Cancel order by ID
HTTP Request
DELETE /api/v1/user/order/{id}

Cancel an individual order by Extended ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation.

URL Parameters
Parameter	Required	Type	Description
id	yes	number	Order to be canceled, ID assigned by Extended.
Cancel order by external id
HTTP Request
DELETE /api/v1/user/order?externalId={externalId}

Cancel an individual order by user ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation.

URL Parameters
Parameter	Required	Type	Description
externalId	yes	string	Order to be canceled, Order ID assigned by user.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Mass Cancel
HTTP Request
POST /api/v1/user/order/massCancel

Mass Cancel enables the cancellation of multiple orders by ID, by specific market, or for all orders within an account.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation request.

Although all parameters are optional, at least one must be specified.

Request example:

{
  "orderIds": [
    1,
    2
  ],
  "externalOrderIds": [
    "ExtId-1",
    "ExtId-2"
  ],
  "markets": [
    "BTC-USD",
    "ETH-USD"
  ],
  "cancelAll": true
}
Body Parameters
Parameter	Required	Type	Description
markets	no	string[]	Market names where all orders should be cancelled.
cancelAll	no	boolean	Indicates whether all open orders for the account should be cancelled.
orderIds	no	number[]	Cancel by Extended IDs.
externalOrderIds	no	string[]	Cancel by external IDs.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Mass auto-cancel (dead man's switch)
HTTP Request
POST /api/v1/user/deadmanswitch?countdownTime={countdownTime}

The dead man's switch automatically cancels all open orders for the account at the end of the specified countdown if no Mass Auto-Cancel request is received within this timeframe. Setting the time to zero will remove any outstanding scheduled cancellations.

Positions and account status are not affected by the dead man's switch.

Request Parameters
Parameter	Required	Type	Description
countdownTime	yes	number	Time till Scheduled Mass Cancel (in seconds), should be non-negative. Setting the time to zero will remove any outstanding scheduled cancellations.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Bridge Config
HTTP Request
GET /api/v1/user/bridge/config

Response example:

{
  "chains": [
    {
      "chain":"ARB",
      "contractAddress":"0x10417734001162Ea139e8b044DFe28DbB8B28ad0"
    }
  ]
}
Returns EVM chains supported for deposits and withdrawals for EVM-wallets.

Response
Parameter	Required	Type	Description
chains	yes	object[]	List of Chain objects.
Chain object
Parameter	Required	Type	Description
chain	yes	string	Chain name.
contractAddress	yes	string	Bridge contract address for the chain.
Get bridge quote
HTTP Request
GET /api/v1/user/bridge/quote?chainIn=ARB&chainOut=STRK&amount=100

Response example:

{
  "id": "68aaa",
  "fee": "0.1"
}
Gets a quote for an EVM deposit/withdrawal.

Request Parameters
Parameter	Required	Type	Description
chainIn	yes	string	Chain where bridge will accept funds. For deposit set EVM chain, for withdrawal STRK.
chainOut	yes	string	Chain where bridge will send funds. For deposit set STRK chain, for withdrawal EVM.
amount	yes	number	Amount in USD that user should pay to bridge contract on chainIn.
Response
Parameter	Required	Type	Description
id	yes	string	Quote ID.
fee	yes	decimal	Bridge fee.
Commit quote
HTTP Request
POST /api/v1/user/bridge/quote?id=68aaa

Commits a quote for EVM deposit/withdrawal.

If a quote is deemed acceptable it needs to be committed before the bridge can be executed. This tells our bridge provider Rhino.fi to start watching for a transaction on the origin chain that deposits the required funds into the bridge contract. Rhino.fi will then issue a commitment ID to be used when sending the funds to be bridged.

Deposits
For EVM wallets, we support deposits and withdrawals on six major chains via the Rhino.fi bridge—Arbitrum, Ethereum, Base, Binance Smart Chain, Avalanche, and Polygon—currently. Please refer to the documentation for transaction limits and estimated processing times.

For Starknet wallets, we support USDC deposits via on-chain interaction and through the User Interface. To deposit on-chain, invoke the Starknet contract at 0x062da0780fae50d68cecaa5a051606dc21217ba290969b302db4dd99d2e9b470.

Extended doesn't charge fees on deposits or withdrawals, but for EVM chains, bridge fees may apply. All deposits and withdrawals are subject to gas fees.

EVM deposit requires bridging, please read Bridge section before proceeding.

EVM deposit consists of four steps:

1) User retrieves supported chains and bridge contracts via GET /bridge/config.

2) User requests a quote via GET /bridge/quote.

3) If the user accepts the bridge fee, they confirm the quote using POST /bridge/quote.

4) Finally, the user calls the depositWithId function on the source chain. See the rhino.fi docs for more details.

 Incorrectly sent funds are non-recoverable by Extended. Follow the execution order exactly as described. When calling depositWithId, use the exact same ID, amount, and token address. Test with a small amount first to ensure everything works correctly.
Withdrawals
For EVM wallets, we support deposits and withdrawals on six major chains—Arbitrum, Ethereum, Base, Binance Smart Chain, Avalanche, and Polygon. Please refer to the documentation for transaction limits and estimated processing times.

For Starknet wallets, we support withdrawals via the User Interface and API, as described below.

Note that Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirements).

Extended doesn't charge fees on deposits or withdrawals, but for EVM chains, bridge fees may apply. All deposits and withdrawals are subject to gas fees. Withdrawals are only permitted to wallets that are linked to the authorised account.

EVM withdrawals
EVM withdrawals involve bridging, please read the Bridge section first before proceeding. The withdrawal process consists of four steps:

1) User retrieves supported chains and bridge contracts via GET /bridge/config. 2) User requests a quote with GET /bridge/quote. 3) If the user accepts the bridge fee, they confirm the quote using POST /bridge/quote. 4) Finally, the user submits a Starknet withdrawal with the quoteId to the bridgeStarknetAddress associated with their account. See Account for details.

Starknet withdrawals
To initiate a Starknet withdrawal, send a "Create Withdrawal" request as described below or use the corresponding SDK method, signed with a private L2 key. Starknet withdrawals are only available for accounts created with a Starknet wallet.

HTTP Request
POST /api/v1/user/withdrawal

Request
Request example:

{
  "accountId":"100006",
  "amount":"2",
  "chainId":"STRK",
  "asset":"USD",
  "settlement":{
    "recipient":"0x00f7016a6f1281925ef584bdc1fd2276b2fef02d0741acce215bc512857030dc",
    "positionId":300006,
    "collateralId":"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "amount":"2000000",
    "expiration":{
      "seconds":1755690249
    },
    "salt":93763903,
    "signature":{
      "r":"1110b06f591a5495b07c1e6ccc9478cbf2301af3a207c082be4c63fde19dd0b",
      "s":"cc93ea79708889869c94c95efdb005f0f15c16dec94a93e7efda33eaf7bcbd"
    }
  }
}
Body Parameters
Parameter	Required	Type	Description
chainId	yes	string	For starknet withdrawals, the type should be STRK.
accountId	yes	number	Source account ID.
amount	yes	string	Withdrawal amount, absolute value in collateral asset.
asset	yes	string	Collateral asset name.
settlement	yes	object	Withdrawal object StarkKey signature. For details, please refer to the Python SDK.
quoteId	yes	object	Bridge quote id for bridged withdrawal.
Response example:

{
  "status": "OK",
  "data": 1820796462590083072
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data	yes	number	Withdrawal ID, assigned by Extended.
Create transfer
HTTP Request
POST /api/v1/user/transfer

Create a transfer between sub-accounts associated with the same wallet.

Request
Request example:

{
  "fromAccount": 3004,
  "toAccount": 7349,
  "amount": "1000",
  "transferredAsset": "USD",
  "settlement": {
    "amount": 1000000000,
    "assetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
    "expirationTimestamp": 478932,
    "nonce": 758978120,
    "receiverPositionId": 104350,
    "receiverPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
    "senderPositionId": 100005,
    "senderPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
    "signature": {
      "r": "6be1839e2ca76484a1a0fcaca9cbbe3792a23656d42ecee306c31e65aadb877",
      "s": "7b8f81258e16f0f90cd12f02e81427e54b4ebf7646e9b14b57f74c2cb44bff6"
    }
  }
}
Body Parameters
Parameter	Required	Type	Description
fromAccount	yes	number	Source account ID.
toAccount	yes	number	Destination account ID.
amount	yes	string	Transfer amount, absolute value in collateral asset.
transferredAsset	yes	string	Collateral asset name.
settlement	yes	object	Transfer object StarkKey signature (including nonce and transfer parameters). For details, please refer to the Python SDK.
Response example:

{
  "status": "OK",
  "data": {
    "validSignature": true,
    "id": 1820778187672010752
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.validSignature	yes	boolean	Indicates whether the signature is valid.
data.id	yes	number	Transfer ID assigned by Extended.
Referrals
Extended offers a referral program. The following API endpoints allow you to issue referral codes and retrieve your referral statistics.

Glossary
Referral – A client who was invited by another client.
Referee – A client who invited another client.
Affiliate – A client who successfully applied to the Affiliate Program.
Subaffiliate – A referred user who is also an affiliate, and was referred by an affiliate.
Referred volume – The trading volume of all clients referred by the user (non-transitive).
Rebate – The reward paid to the referee of affiliate, derived from the trading fees of his referrals.
Rebate rate – The percentage of fees paid by the referral that the referee or affiliate receive.
Rebate = rebate_rate * (trading_fees - rewards_to_other_programs)
Referral schedule – A set of rules (tiers) that determine the rebate rate based on the L30D referred volume.
Shared objects
Tier object
Example:

{
  "totalVolume": "0",
  "rebateRate": "0.1",
  "volumeLimitPerReferral": "0"
}
Tier is the lowest-level object that defines the rules of the referral program.

Parameter	Required	Type	Description
totalVolume	yes	number	Minimum Last 30D referred volume for the rebate rate tier.
rebateRate	yes	number	The rebate rate.
volumeLimitPerReferral	yes	number	Maximum trading volume eligible for a fee discount per referral.
Refferal schedule object
Example:

{
  "tiers": [
    {
      "totalVolume": "0",
      "rebateRate": "0.1",
      "volumeLimitPerReferral": "0"
    }
  ]
}
Contains a list of Tiers objects.

Parameter	Required	Type	Description
tiers	yes	object[]	List of Tiers objects.
Refferal group object
Example:

{
  "id": 1,
  "schedule": {
    "tiers": [
      {
        "totalVolume": "0",
        "rebateRate": "0.1",
        "volumeLimitPerReferral": "0"
      }
    ]
  },
  "subaffiliateRate": "0.1"
}
Contains the Referral schedule object and the sub-affiliate rebate rate. Each affiliate can have two types of Referral groups — the Main group and the Protection-period group.

Parameter	Required	Type	Description
id	yes	number	Group ID.
schedule	yes	object	Refferal schedule object.
subaffiliateRate	yes	number	Rebate rate that referee gains from their subaffiliate referral rebates.
Affiliate object
Example:

{
  "clientId": 42,
  "name": "ABC",
  "onboarded": 1746784655000,
  "mainGroup": {
    "id": 1,
    "schedule": {
      "tiers": [
        {
          "totalVolume": "0",
          "rebateRate": "0.1",
          "volumeLimitPerReferral": "0"
        }
      ]
    },
    "subaffiliateRate": "0"
  },
  "d30ReferredVolume": "2000"
}
Parameter	Required	Type	Description
clientId	yes	number	Affiliate's client ID on Extended.
name	yes	string	Affiliate's name on Extended.
onboarded	yes	number	Affiliate's onboarding timestamp (Unix).
mainGroup	yes	number	Affiliate's Main Refferal group object.
d30ReferredVolume	yes	number	Last 30D volume of users referred by the Affiliate.
protectionPeriodGroup	no	number	Affiliate's Refferal group during protection period.
protectionPeriodUntil	no	number	End of protection period (Unix timestamp).
Period
Enum that specifies the time period for fetching data. Can be DAY, WEEK, MONTH, YEAR, ALL.

Granularity
Enum that specifies the time period for fetching data. Can be DAY, WEEK, MONTH.

Get affiliate data
GET /api/v1/user/affiliate

Response example:

{
  "clientId": 42,
  "name": "ABC",
  "onboarded": 1746784655000,
  "mainGroup": {
    "id": 1,
    "schedule": {
      "tiers": [
        {
          "totalVolume": "0",
          "rebateRate": "0.1",
          "volumeLimitPerReferral": "0"
        }
      ]
    },
    "subaffiliateRate": "0"
  },
  "d30ReferredVolume": "2000"
}
If the user is an affiliate, returns their affiliate data; otherwise, returns a 404.

Response
See Affiliate object in the Shared objects section of Referrals documentation.

Get referral status
GET /api/v1/user/referrals/status

Response example:

{
  "active": true, 
  "limit": 10000,
  "tradedVolume": 100
}
Returns the user’s referral program status.

Response
Parameter	Required	Type	Description
active	yes	boolean	Program is active for the user - user can issue referral codes. Can be true or false.
limit	yes	number	Trading volume required to activate the referral program.
tradedVolume	yes	number	User's current traded volume.
Get referral links
GET /api/v1/user/referrals/links

Response example:

[
  {
    "id": "ABC",
    "issuedBy": 42,
    "issuedAt": 1746785907329,
    "label": "ABC",
    "isDefault": true,
    "hiddenAtUi": false,
    "overallRebates": "50"
  }
]
Returns referral links issued by the user.

Response
Parameter	Required	Type	Description
id	yes	string	Link ID.
issuedBy	yes	number	Referral client ID.
issuedAt	yes	number	Link issue timestamp (Unix).
label	yes	string	Label added by user.
isDefault	yes	boolean	Link set as default for the client. Can be true or false.
hiddenAtUi	yes	boolean	Link is visible for the client. Can be true or false.
overallRebates	yes	number	Total rebates for the link.
Get referral dashboard
GET /api/v1/user/referrals/dashboard?period={PERIOD}

Response example:

{
  "referralLinkToDirectKeyMetrics": {
    "ABC": {
      "rebateEarned": {
        "current": "200",
        "previous": "100"
      },
      "totalFeesPaid": {
        "current": "2000",
        "previous": "1000"
      },
      "tradingVolume": {
        "current": "20000",
        "previous": "10000"
      },
      "activeTraders": {
        "current": 200,
        "previous": 100
      }
    }
  },
  "subaffiliateToKeyMetrics": {
    "2": {
      "rebateEarned": {
        "current": "200",
        "previous": "100"
      },
      "subaffiliateEarnings": {
        "current": "2500",
        "previous": "1250"
      }
    }
  },
  "activeSubaffiliates": {
    "current": 1,
    "previous": 0
  },
  "affiliates": [
    {
      "clientId": 2,
      "name": "RUSLAN",
      "onboarded": 1746792229516,
      "mainGroup": {
        "id": 1,
        "schedule": {
          "tiers": [
            {
              "totalVolume": "0",
              "rebateRate": "0.1",
              "volumeLimitPerReferral": "0"
            }
          ]
        },
        "subaffiliateRate": "0"
      }
    }
  ],
  "users": [
    {
      "firstTradedOn": 1746792228516,
      "wallet": "0x42...a8a91",
      "rebate": "100",
      "tradedVolume": "10000",
      "totalFees": "1000"
    }
  ],
  "daily": [
    {
      "date": "2025-05-09",
      "subaffiliates": [
        {
          "id": 2,
          "rebate": "5",
          "activeUsers": 2,
          "referredTradingVolume": "100",
          "earnings": "10"
        }
      ],
      "links": [
        {
          "link": "ABC",
          "rebate": "10",
          "activeUsers": 4,
          "referredTradingVolume": "200",
          "referredFees": "20",
          "referredL30Volume": "2000"
        }
      ]
    },
    {
      "date": "2025-05-08",
      "subaffiliates": [],
      "links": []
    }
  ],
  "weekly": [
    {
      "date": "2025-05-09",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-05-02",
      "subaffiliates": [],
      "links": []
    }
  ],
  "monthly": [
    {
      "date": "2025-05-09",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-04-11",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-04-13",
      "subaffiliates": [],
      "links": []
    }
  ]
}
Returns referral program statistic for the selected period.

Request parameters
Parameter	Required	Type	Description
period	yes	string	Requested period.
Response
The Affiliate object is described in the Shared objects section of Referrals documentation. The descriptions of other objects returned by this endpoint are provided below.

Parameter	Required	Type	Description
referralLinkToDirectKeyMetrics	yes	object	Metrics aggregated by referral codes (Map).
subaffiliateToKeyMetrics	yes	object	Metrics aggregated by subaffiliates (Map).
activeSubaffiliates	yes	number	Number of active subaffiliates.
affiliates	yes	object[]	List of Affiliate objects for subaffiliates active during the period.
users	yes	object[]	List of UserStat objects for users active during the period.
daily	yes	object[]	List of AffiliateStat objects for the period with 1 day granularity.
weekly	yes	object[]	List of AffiliateStat objects for the period with 1 week granularity.
monthly	yes	object[]	List of AffiliateStat objects for the period with 1 month granularity.
CurrentToPrevious<T>
Parameter	Required	Type	Description
current	yes	object	<T> data for current period.
previous	yes	object	<T> data for previous period.
DirectKeyMetrics
Parameter	Required	Type	Description
rebateEarned	yes	object	CurrentToPrevious<Number>. Rebates earned during the period.
totalFeesPaid	yes	object	CurrentToPrevious<Number>. Total amount of fees paid by referrals during the period.
tradingVolume	yes	object	CurrentToPrevious<Number>. Referred volume during the period.
activeTraders	yes	object	CurrentToPrevious<Number>. Number of active traders among referrals during the period.
SubaffiliateKeyMetrics
Parameter	Required	Type	Description
rebateEarned	yes	object	CurrentToPrevious<Number>. Rebates earned during the period.
subaffiliateEarnings	yes	object	CurrentToPrevious<Number>. Total rebates earned by subaffiliates during the period.
UserStat
Parameter	Required	Type	Description
firstTradedOn	no	number	Referral's first trade timestamp (Unix).
wallet	yes	string	Masked referral's wallet.
referredBy	no	number	User's referee.
referralLink	no	string	Referral link code used by the referral.
rebate	yes	number	Rebate.
tradedVolume	yes	number	Referral's traded volume during the period.
totalFees	yes	number	Total fees paid by the referral during the period.
AffiliateStat
Parameter	Required	Type	Description
date	yes	string	Last date of the period.
subaffiliates	yes	object[]	List of SubaffiliateStat objects for the period grouped by subaffiliates.
links	yes	object[]	List of LinkStat objects for the period grouped by links.
SubaffiliateStat
Parameter	Required	Type	Description
id	yes	number	Subaffiliate's client ID on Extended.
rebate	yes	number	Rebate earned by Subaffiliate (rebate from referrals of his referrals).
activeUsers	yes	number	Number of active traders among Subaffiliate's referrals.
referredTradingVolume	yes	number	Subaffiliate's referred volume.
earnings	yes	number	Subaffiliate's rebate.
LinkStat
Parameter	Required	Type	Description
link	yes	string	Referral link code.
rebate	yes	number	Rebate earned through the link.
activeUsers	yes	number	Count of active referrals invited through the link.
referredTradingVolume	yes	number	Volume referred through the link.
referredFees	yes	number	Total fees paid by referrals invited through the link.
referredL30Volume	yes	number	Last 30D volume referred through the link.
Use referral link
POST /api/v1/user/referrals/use

Request example: json { "code": "ABC" }

Activate referral link for the authenticated client.

Create referral link code
POST /api/v1/user/referrals

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Create referral link code.

Update referral link code
PUT /api/v1/user/referrals

Update referral link code.

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Points
Points-related endpoints let users view their earned points and leaderboard ranking.

Get Earned Points
HTTP Request
GET /api/v1/user/rewards/earned

Returns points earned by the authenticated client across all seasons and epochs.

Authentication
This endpoint requires authentication.

Response example: json { "status": "OK", "data": [ { "seasonId": 1, "epochRewards": [ { "epochId": 1, "startDate": "2023-01-01T00:00:00Z", "endDate": "2023-01-31T23:59:59Z", "pointsReward": "50.25" } ] } ] }

Response
Parameter	Type	Description
data[].seasonId	number	The ID of the reward season.
data[].epochRewards	array	List of rewards earned in each epoch.
data[].epochRewards.epochId	number	The ID of the epoch.
data[].epochRewards.startDate	string	The start date of the epoch (ISO format).
data[].epochRewards.endDate	string	The end date of the epoch (ISO format).
data[].epochRewards.pointsReward	string	The number of points earned in the epoch.
Get points leaderboard stats
HTTP Request
GET /api/v1/user/rewards/leaderboard/stats

Returns the leaderboard statistics for the authenticated client, including total points, leaderboard rank, and points league levels.

Authentication
This endpoint requires authentication.

Response example: json { "status": "OK", "data": { "totalPoints": "1250.75", "rank": 42, "tradingRewardLeague": "QUEEN", "liquidityRewardLeague": "PAWN", "referralRewardLeague": "KING" } }

Response
Parameter	Type	Description
totalPoints	string	The total number of points earned.
rank	number	The client's rank on the leaderboard.
tradingRewardLeague	string	The client's league for trading points.
liquidityRewardLeague	string	The client's league for liquidity points.
referralRewardLeague	string	The client's league for referral points.
Points league levels
The following table describes the points-league levels for tradingRewardLeague, liquidityRewardLeague, and referralRewardLeague.

Value	Description
KING	King league - highest tier.
QUEEN	Queen league - second-highest tier.
ROOK	Rook league - advanced tier.
KNIGHT	Knight league - intermediate tier.
PAWN	Pawn league - entry-level tier.
Get account equity history
HTTP Request
GET /api/v1/portfolio/charts/equities?accountId={accountId}&interval={interval}

Returns equity history for the chosen accounts per date. To request data for several accounts, use the format GET /api/v1/portfolio/charts/equities?accountId=1000&accountId=10001&interval=WEEK.

Authentication
This endpoint requires authentication.

Request
Query Parameters
Parameter	Required	Type	Description
accountId	yes	number	Id of user account.
interval	yes	string	Time interval. Can be DAY, WEEK, MONTH, YEAR or ALL.
Response example:

{
  "status": "OK",
  "data": [
    {
      "date": "2025-08-10",
      "value": "700"
    },
    {
      "date": "2025-08-11",
      "value": "1400"
    }
  ]
}
Get account PnL history
HTTP Request
GET /api/v1/portfolio/charts/pnl?accountId={accountId}&interval={interval}&pnlType={pnlType}

Returns total or realised Pnl history for the chosen accounts per date. To request data for several accounts, use the format GET /api/v1/portfolio/charts/pnl?accountId=1000&accountId=10001&interval=WEEK&pnlType=TOTAL_PNL.

Authentication
This endpoint requires authentication.

Request
Query Parameters
Parameter	Required	Type	Description
accountId	yes	number	Account ID.
interval	yes	string	Time interval. Can be DAY, WEEK, MONTH, YEAR or ALL.
pnlType	yes	string	Pnl type. Can be TOTAL_PNL or REALISED_PNL.
Response example:

                {
  "status": "OK",
  "data": [
    {
      "date": "2025-08-10",
      "value": "700"
    },
    {
      "date": "2025-08-11",
      "value": "1400"
    }
  ]
}
Get Vault performance
HTTP Request
GET /api/v1/vault/public/performance?interval={interval}

Returns performance of vault, which includes data as total pnl, sharpe ratio, profit factor, etc.

Authentication
This endpoint does not require authentication.

Request
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	Time interval. Can be WEEK, MONTH, YEAR or ALL.
Response example:

{
  "status": "OK",
  "data": {
    "totalPnl": "1156",
    "aprPercentage": "17.5495",
    "profitFactor": "1.5887",
    "winRate": "0.2881",
    "maxDrawdown": "0.2182",
    "tradingVolume": "6000",
    "sharpeRatio": "252.96",
    "aprBreakdown": {
      "baseApr": "10.6551",
      "maxExtraApr": "6.8944"
    }
  }
}
Get Vault summary
HTTP Request
GET /api/v1/vault/public/summary

Returns a summary of the vault for a whole period.

Authentication
This endpoint does not require authentication.

Response example:

{
  "status": "OK",
  "data": {
    "equity": "11000",
    "walletBalance": "2000",
    "lastMonthApr": "422.7917",
    "exposure": "10000",
    "numberOfDepositors": 3,
    "ageDays": 227,
    "profitShare": "0",
    "aprBreakdown": {
      "baseApr": "416.1",
      "maxExtraApr": "6.6917"
    }
  }
}
Public WebSocket streams
Extended offers a WebSocket API for streaming updates.

Connect to the WebSocket streams using wss://api.starknet.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from the client, it will respond with a pong if one is received.

Order book stream
HTTP Request
GET /stream.extended.exchange/v1/orderbooks/{market}

Subscribe to the orderbooks stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

In the current version we support the following depth specifications:

Full orderbook. Push frequency: 100ms. The initial response from the stream will be a snapshot of the order book. Subsequent snapshot updates will occur every minute, while updates between snapshots are delivered in delta format, reflecting only changes since the last update. Best Bid & Ask updates are always provided as snapshots.

Best bid & ask. Push frequency: 10ms. To subscribe for Best bid & ask use GET /stream.extended.exchange/v1/orderbooks/{market}?depth=1. Best bid & ask updates are always snapshots.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Query Parameters
Parameter	Required	Type	Description
depth	no	string	Specify '1' to receive updates for best bid & ask only.
Response example:

{
  "ts": 1701563440000,
  "type": "SNAPSHOT",
  "data": {
    "m": "BTC-USD",
    "b": [
      {
        "p": "25670",
        "q": "0.1",
        "c": "0.3"
      }
    ],
    "a": [
      {
        "p": "25770",
        "q": "0.1",
        "c": "0.2"
      }
    ]
  },
  "seq": 1
}
Response
Parameter	Type	Description
type	string	Type of message. Can be SNAPSHOT or DELTA.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data.m	string	Market name.
data.t	string	Type of message. Can be SNAPSHOT or DELTA.
data.b	object[]	List of bid orders. For a snapshot, bids are sorted by price in descending order.
data.b[].p	string	Bid price.
data.b[].q	string	Bid size. For a snapshot, this represents the absolute size; for a delta, the change in size.
data.b[].c	string	Bid size. For a snapshot and delta, this represents the absolute size.
data.a	object[]	List of ask orders. For a snapshot, asks are sorted by price in ascending order.
data.a[].p	string	Ask price.
data.a[].q	string	Ask size. For a snapshot, this represents the absolute size; for a delta, the change in size.
data.a[].c	string	Ask size. For a snapshot and delta, this represents the absolute size.
seq	number	Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.
Trades stream
HTTP Request
GET /stream.extended.exchange/v1/publicTrades/{market}

Subscribe to the trades stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Historical trade data is currently available only to authorized accounts via the private REST API.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "ts": 1701563440000,
  "data": [
    {
      "m": "BTC-USD",
      "S": "BUY",
      "tT": "TRADE",
      "T": 1701563440000,
      "p": "25670",
      "q": "0.1",
      "i": 25124
    }
  ],
  "seq": 2
}
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].m	string	Market name.
data[].S	string	Side of taker trades. Can be BUY or SELL.
data[].tT	string	Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.
data[].T	number	Timestamp (in epoch milliseconds) when the trade happened.
data[].p	string	Trade price.
data[].q	string	Trade quantity in base asset.
data[].i	number	Trade ID.
seq	number	Monotonic sequence: Since there are no deltas, clients can skip trades that arrive out of sequence.
Funding rates stream
HTTP Request
GET /stream.extended.exchange/v1/funding/{market}

Subscribe to the funding rates stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

For historical funding rates data, use the Get funding rates history endpoint.

While the funding rate is calculated every minute, it is applied only once per hour. The records include only those funding rates that were used for funding fee payments.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "ts": 1701563440000,
  "data": {
      "m": "BTC-USD",
      "T": 1701563440000,
      "f": "0.001"
  },
  "seq": 2
}
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].m	string	Market name.
data[].T	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
data[].f	string	Funding rates that were applied for funding fee payments.
seq	number	Monotonic sequence: Since there are no deltas, clients can skip funding rates that arrive out of sequence.
Candles stream
HTTP Request
GET /stream.extended.exchange/v1/candles/{market}/{candleType}?interval={interval}

Subscribe to the candles stream for a specific market.

The interval parameter should be specified in the ISO 8601 duration format. Available intervals include: P30D (Calendar month), P7D (Calendar week), PT24H, PT12H, PT8H, PT4H, PT2H, PT1H, PT30M, PT15M, PT5M and PT1M.

Trades price response example:

{
  "ts": 1695738675123,
  "data": [ 
    {
      "T": 1695738674000,
      "o": "1000.0000",
      "l": "800.0000",
      "h": "2400.0000",
      "c": "2100.0000",
      "v": "10.0000"
    }
  ],
  "seq": 1
}
Mark and Index price response example:

{
  "ts": 1695738675123,
  "data": [
    {
      "T": 1695738674000,
      "o": "1000.0000",
      "l": "800.0000",
      "h": "2400.0000",
      "c": "2100.0000"
    }
  ],
  "seq": 1
}
Available price types include:

Last price: GET /stream.extended.exchange/v1/candles/{market}/trades?interval=PT1M

Mark price: GET /stream.extended.exchange/v1/candles/{market}/mark-prices?interval=PT1M

Index price: GET /stream.extended.exchange/v1/candles/{market}/index-prices?interval=PT1M

Push frequency: 1-10s.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Select an individual market.
candleType	yes	string	Price type. Can be trades, mark-prices or index-prices.
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	Duration of candle (duration in ISO 8601).
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].T	number	Starting timestamp (in epoch milliseconds) of the candle.
data[].o	string	Open price.
data[].c	string	Close price.
data[].h	string	Highest price.
data[].l	string	Lowest price.
data[].v	string	Trading volume (only for trade candles).
seq	number	Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.
Mark price stream
HTTP Request
GET /stream.extended.exchange/v1/prices/mark/{market}

Subscribe to the mark price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Mark prices are used to calculate unrealized P&L and serve as the reference for liquidations. The stream provides real-time updates whenever a mark price changes.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "type": "MP",
  "data": {
    "m": "BTC-USD",
    "p": "25670",
    "ts": 1701563440000
  },
  "ts": 1701563440000,
  "seq": 1,
  "sourceEventId": null
}
Response
Parameter	Type	Description
type	string	Type identifier for mark price stream ("MP").
data.m	string	Market name.
data.p	string	Mark price value.
data.ts	number	Timestamp (in epoch milliseconds) when the price was calculated.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
seq	number	Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.
sourceEventId	number	ID of the source event that triggered this update (null for regular updates).
Index price stream
HTTP Request
GET /stream.extended.exchange/v1/prices/index/{market}

Subscribe to the index price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

An index price is a composite spot price sourced from multiple external providers. It is used as the reference for funding-rate calculations.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "type": "IP",
  "data": {
    "m": "BTC-USD",
    "p": "25680",
    "ts": 1701563440000
  },
  "ts": 1701563440000,
  "seq": 1,
  "sourceEventId": null
}
Response
Parameter	Type	Description
type	string	Type identifier for index price stream ("IP").
data.m	string	Market name.
data.p	string	Index price value.
data.ts	number	Timestamp (in epoch milliseconds) when the price was calculated.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
seq	number	Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.
sourceEventId	number	ID of the source event that triggered this update (null for regular updates).
Private WebSocket streams
Connect to the WebSocket streams using ws://api.starknet.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from clients, it will respond with a pong if it receives one.

Extended employs a simplified authentication scheme for API access. Authenticate by using your API key, which should be included in an HTTP header as follows: X-Api-Key: <API_KEY_FROM_API_MANAGEMENT_PAGE_OF_UI>.

Account updates stream
HTTP Request
GET /stream.extended.exchange/v1/account

Orders updates response example:

{
  "type": "ORDER",
  "data": {
    "orders": [
      {
        "id": 1791181340771614723,
        "accountId": 1791181340771614721,
        "externalId": "-1771812132822291885",
        "market": "BTC-USD",
        "type": "LIMIT",
        "side": "BUY",
        "status": "NEW",
        "price": "12400.000000",
        "averagePrice": "13140.000000",
        "qty": "10.000000",
        "filledQty": "3.513000",
        "payedFee": "0.513000",
        "trigger": {
          "triggerPrice": "1220.00000",
          "triggerPriceType": "LAST",
          "direction": "UP",
          "executionPriceType": "LIMIT"
        },
        "tpSlType": "ORDER",
        "takeProfit": {
          "triggerPrice": "1.00000",
          "triggerPriceType": "LAST",
          "price": "1.00000",
          "priceType": "LIMIT"
        },
        "stopLoss": {
          "triggerPrice": "1.00000",
          "triggerPriceType": "LAST",
          "price": "1.00000",
          "priceType": "LIMIT"
        },
        "reduceOnly": true,
        "postOnly": false,
        "createdTime": 1715885888571,
        "updatedTime": 1715885888571,
        "expireTime": 1715885888571
      }
    ]
  },
  "ts": 1715885884837,
  "seq": 1
}
Trades updates response example:

{
  "type": "TRADE",
  "data": {
    "trades": [
      {
        "id": 1784963886257016832,
        "accountId": 3017,
        "market": "BTC-USD",
        "orderId": 9223372036854775808,
        "externalOrderId": "ext-1",
        "side": "BUY",
        "price": "58853.4000000000000000",
        "qty": "0.0900000000000000",
        "value": "5296.8060000000000000",
        "fee": "0.0000000000000000",
        "tradeType": "DELEVERAGE",
        "createdTime": 1701563440000,
        "isTaker": true
      }
    ]
  },
  "ts": 1715885884837,
  "seq": 1
}
Account balance updates response example:

{
  "type": "BALANCE",
  "data": {
    "balance": {
      "collateralName": "BTC",
      "balance": "100.000000",
      "equity": "20.000000",
      "availableForTrade": "3.000000",
      "availableForWithdrawal": "4.000000",
      "unrealisedPnl": "1.000000",
      "initialMargin": "0.140000",
      "marginRatio": "1.500000",
      "updatedTime": 1699976104901,
      "exposure": "12751.859629",
      "leverage": "1275.1860"
    }
  },
  "ts": 1715885952304,
  "seq": 1
}
Positions updates response example:

{
  "type": "POSITION",
  "data": {
    "positions": [
      {
        "id": 1791183357858545669,
        "accountId": 1791183357858545665,
        "market": "BTC-USD",
        "side": "SHORT",
        "leverage": "5.0",
        "size": "0.3",
        "value": "12751.8596295830",
        "openPrice": "42508.00",
        "markPrice": "42506.1987652769",
        "liquidationPrice": "75816.37",
        "margin": "637.59",
        "unrealisedPnl": "100.000000",
        "realisedPnl": "200.000000",
        "tpTriggerPrice": "1600.0000",
        "tpLimitPrice": "1500.0000",
        "slTriggerPrice": "1300.0000",
        "slLimitPrice": "1250.0000",
        "adl": 1,
        "createdAt": 1715886365748,
        "updatedAt": 1715886365748
      }
    ]
  },
  "ts": 1715886365748,
  "seq": 1
}
Subscribe to the account updates stream.

The initial responses will include comprehensive information about the account, including balance, open positions, and open orders, i.e. everything from GET /v1/user/balance, GET /v1/user/positions, GET /v1/user/orders.

Subsequent responses will contain all updates related to open orders, trades, account balance, or open positions in a single message.

The response attributes will align with the responses from the corresponding REST API endpoints: Get trades, Get positions, Get open orders and Get balance. Refer to the Account section for details.

Error responses
Unless specified otherwise for a particular endpoint and HTTP status code, the error response model follows the general response format and includes an error code along with a descriptive message for most errors.

Error code	Error	Description
GENERAL		
400	BadRequest	Invalid or missing parameters.
401	Unauthorized	Authentication failure.
403	Forbidden	Access denied.
404	NotFound	Resource not found.
422	UnprocessableEntity	Request format is correct, but data is invalid.
429	RateLimited	Number of calls from the IP address has exceeded the rate limit.
500	InternalServerError	Internal server error.
MARKET,	ASSET & ACCOUNT	
1000	AssetNotFound	Asset not found.
1001	MarketNotFound	Market not found.
1002	MarketDisabled	Market is disabled.
1003	MarketGroupNotFound	Market group not found.
1004	AccountNotFound	Account not found.
1005	NotSupportedInterval	Not supported interval.
1006	UnhandledError	Application error.
1008	ClientNotFound	Client not found.
1009	ActionNotAllowed	Action is not allowed.
1010	MaintenanceMode	Maintenance mode.
1011	PostOnlyMode	Post only mode.
1012	ReduceOnlyMode	Reduce only mode.
1013	InvalidPercentage	Percentage should be between 0 and 1.
1014	MarketReduceOnly	Market is in reduce only mode, non-reduce only orders are not allowed.
LEVERAGE	UPDATE	
1049	InvalidLeverageBelowMinLeverage	Leverage below min leverage.
1050	InvalidLeverageExceedsMaxLeverage	Leverage exceeds max leverage.
10501	InvalidLeverageMaxPositionValueExceeded	Max position value exceeded for new leverage.
1052	InvalidLeverageInsufficientMargin	Insufficient margin for new leverage.
1053	InvalidLeverageInvalidPrecision	Leverage has invalid precision.
STARKNET	SIGNATURES	
1100	InvalidStarknetPublicKey	Invalid Starknet public key.
1101	InvalidStarknetSignature	Invalid Starknet signature.
1102	InvalidStarknetVault	Invalid Starknet vault.
ORDER		
1120	OrderQtyLessThanMinTradeSize	Order quantity less than min trade size, based on market-specific trading rules.
1121	InvalidQtyWrongSizeIncrement	Invalid quantity due to the wrong size increment, based on market-specific Minimum Change in Trade Size trading rule.
1122	OrderValueExceedsMaxOrderValue	Order value exceeds max order value, based on market-specific trading rules.
1123	InvalidQtyPrecision	Invalid quantity precision, currently equals to market-specific Minimum Change in Trade Size.
1124	InvalidPriceWrongPriceMovement	Invalid price due to wrong price movement, based on market-specific Minimum Price Change trading rule.
1125	InvalidPricePrecision	Invalid price precision, currently equals to market-specific Minimum Price Change.
1126	MaxOpenOrdersNumberExceeded	Max open orders number exceeded, currently 200 orders per market.
1127	MaxPositionValueExceeded	Max position value exceeded, based on the Margin schedule.
1128	InvalidTradingFees	Trading fees are invalid. Refer to Order management section for details.
1129	InvalidPositionTpslQty	Invalid quantity for position TP/SL.
1130	MissingOrderPrice	Order price is missing.
1131	MissingTpslTrigger	TP/SL order trigger is missing.
1132	NotAllowedOrderType	Order type is not allowed.
1133	InvalidOrderParameters	Invalid order parameters.
1134	DuplicateOrder	Duplicate Order.
1135	InvalidOrderExpiration	Order expiration date must be within 90 days for the Mainnet, 28 days for the Testnet.
1136	ReduceOnlyOrderSizeExceedsPositionSize	Reduce-only order size exceeds open position size.
1137	ReduceOnlyOrderPositionIsMissing	Position is missing for a reduce-only order.
1138	ReduceOnlyOrderPositionSameSide	Position is the same side as a reduce-only order.
1139	MarketOrderMustBeIOC	Market order must have time in force IOC.
1140	OrderCostExceedsBalance	New order cost exceeds available balance.
1141	InvalidPriceAmount	Invalid price value.
1142	EditOrderNotFound	Edit order not found.
1143	MissingConditionalTrigger	Conditional order trigger is missing.
1144	PostOnlyCantBeOnConditionalMarketOrder	Conditional market order can't be Post-only.
1145	NonReduceOnlyOrdersNotAllowed	Non reduce-only orders are not allowed.
1146	TwapOrderMustBeGTT	Twap order must have time in force GTT.
1147	OpenLossExceedsEquity	Open loss exceeds equity.
1148	TPSLOpenLossExceedsEquity	TP/SL open loss exceeds equity.
GENERAL	ACCOUNT	
1500	AccountNotSelected	Account not selected.
WITHDRAWAL		
1600	WithdrawalAmountMustBePositive	Withdrawal amount must be positive.
1601	WithdrawalDescriptionToLong	Withdrawal description is too long.
1602	WithdrawalRequestDoesNotMatchSettlement	Withdrawal request does not match settlement.
1604	WithdrawalExpirationTimeIsTooSoon	Withdrawal expiration time is below the 14 days minimum.
1605	WithdrawalInvalidAsset	Withdrawal asset is not valid.
1607	WithdrawalBlockedForAccount	Withdrawals blocked for the account. Please contact the team on Discord to unblock the withdrawals.
1608	WithdrawalAccountDoesNotBelongToUser	The withdrawal address does not match the account address.
TRANSFERS		
1650	InvalidVaultTransferAmount	Vault transfer amount is incorrect.
REFERRAL	CODE	
1700	ReferralCodeAlreadyExist	Referral code already exist.
1701	ReferralCodeInvalid	Referral code is not valid.
1703	ReferralProgramIsNotEnabled	Referral program is not enabled.
1704	ReferralCodeAlreadyApplied	Referral code already applied.
Legacy: StarkEx SDK
SDK configuration

from dataclasses import dataclass


@dataclass
class EndpointConfig:
    chain_rpc_url: str
    api_base_url: str
    stream_url: str
    onboarding_url: str
    signing_domain: str
    collateral_asset_contract: str
    asset_operations_contract: str
    collateral_asset_on_chain_id: str
    collateral_decimals: int

TESTNET_CONFIG_LEGACY_SIGNING_DOMAIN = EndpointConfig(
    chain_rpc_url="https://rpc.sepolia.org",
    api_base_url="https://api.testnet.extended.exchange/api/v1",
    stream_url="wss://api.testnet.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.testnet.extended.exchange",
    signing_domain="x10.exchange",
    collateral_asset_contract="0x0c9165046063b7bcd05c6924bbe05ed535c140a1",
    asset_operations_contract="0x7f0C670079147C5c5C45eef548E55D2cAc53B391",
    collateral_asset_on_chain_id="0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
    collateral_decimals=6,
)

STARKEX_MAINNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://cloudflare-eth.com",
    api_base_url="https://api.extended.exchange/api/v1",
    stream_url="wss://api.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.extended.exchange",
    signing_domain="extended.exchange",
    collateral_asset_contract="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    asset_operations_contract="0x1cE5D7f52A8aBd23551e91248151CA5A13353C65",
    collateral_asset_on_chain_id="0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d",
    collateral_decimals=6,
)
Extended now operates on the Starknet instance. The wind-down plan for the StarkEx instance can be found here. StarkEx-specific details apply only to users whose Extended account was created before August 12, 2025, and who have not yet migrated to Starknet. In all other cases, please follow the Starknet-specific logic described above.

StarkEx Python SDK:

For installation instructions, please refer to the description provided.

For reference implementations, explore the examples folder.

For SDK configuration, please refer to the config description.

Supported Features:

Account creation and authorisation.

Order Management.

Account Management.

Deposits, Transfers, and Withdrawals.

Market Information.





Extended API Documentation
By using the Extended API, you agree to the Extended Terms & Privacy Policy. If you do not agree to the foregoing terms, do not use the Extended API.

Introduction
 This documentation is a work in progress and will be updated regularly based on user feedback and the addition of new functionality.
Welcome to the Extended API Documentation! This guide is designed to assist traders and developers in integrating with our hybrid perpetuals exchange.

Extended operates as a hybrid Central Limit Order Book (CLOB) exchange. While order processing, matching, position risk assessment, and transaction sequencing are handled off-chain, trade settlement occurs on-chain via Starknet.

Extended is designed to operate in a completely trustless manner, enabled by two core principles:

Users retain self-custody of their funds, with all assets held in smart contracts on Starknet. This means Extended has no custodial access to user assets under any circumstances.

On-chain validation of the trading logic ensures that fraudulent or incorrect transactions, including liquidations that are contrary to the on-chain rules, are never permitted.

All transactions that happen on Extended are settled on Starknet. While Starknet does not rely on Ethereum Layer 1 for every individual transaction, it inherits Ethereum’s security by publishing zero-knowledge proofs every few hours. These proofs validate state transitions on Starknet, ensuring the integrity and correctness of the entire system.

Extended's on-chain logic and smart contracts have undergone extensive audits by external security firms. The audit reports are available below:

ChainSecurity.

Public audit competition.

For a deeper breakdown of the core principles that make Extended trustless, see the blog Why Safe. For more on Extended Exchange's roadmap and architecture, check out Extended Vision and Architecture, respectively.

To optimize high-frequency trading performance, the Extended API operates asynchronously. When you place an order, it immediately returns an order ID, even before the order is officially recorded in the book. To track your order status in real time subscribe to the Order WebSocket stream, which delivers instant updates on confirmations, cancellations, and rejections.

StarkEx to Starknet migration
On August 12, 2025, Extended began the migration from StarkEx to Starknet. This transition marks the first step toward our long-term vision of the Extended ecosystem and the introduction of unified margin. You can read more about the broader migration rationale and vision in our documentation.

Existing Extended users will need to migrate from the current StarkEx instance to the new Starknet instance. The migration process has been designed to be as seamless as possible and is explained here. New users will be onboarded directly to the Starknet instance.

For the Starknet instance of the platform, the following changes vs StarkEx apply:

Wallet support: In addition to EVM-compatible wallets, we will also support Starknet-compatible wallets.

Signing logic: New signing logic in line with the SNIP12 standard (EIP712 for Starknet) and examples are available via the SDK.

Deposits and withdrawals: For EVM wallets, we support deposits and withdrawals on six major EVM chains, currently only via the user interface. For Starknet wallets, deposits and withdrawals via Starknet are now supported.

URL: The URL for the Starknet instance is api.starknet.extended.exchange, vs. api.extended.exchange for the StarkEx instance.

The migration will be rolled out in three stages:

Stage 1 – Dual Operation Mode,

Stage 2 – StarkEx Wind-Down Mode,

Stage 3 – StarkEx Freeze.

While the StarkEx instance will remain fully operational during Stage 1 of the migration, certain restrictions will apply starting August 12. Please review them carefully here.

Until the migration is complete, all StarkEx-specific details can be found in the dedicated section of the API documentation.

Python SDK
SDK configuration

from dataclasses import dataclass


@dataclass
class EndpointConfig:
    chain_rpc_url: str
    api_base_url: str
    stream_url: str
    onboarding_url: str
    signing_domain: str
    collateral_asset_contract: str
    asset_operations_contract: str
    collateral_asset_on_chain_id: str
    collateral_decimals: int


STARKNET_TESTNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://rpc.sepolia.org",
    api_base_url="https://api.starknet.sepolia.extended.exchange/api/v1",
    stream_url="wss://starknet.sepolia.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.starknet.sepolia.extended.exchange",
    signing_domain="starknet.sepolia.extended.exchange",
    collateral_asset_contract="",
    asset_operations_contract="",
    collateral_asset_on_chain_id="",
    collateral_decimals=6,
    starknet_domain=StarknetDomain(name="Perpetuals", version="v0", chain_id="SN_SEPOLIA", revision="1"),
    collateral_asset_id="0x1",
)

STARKNET_MAINNET_CONFIG = EndpointConfig(
    chain_rpc_url="",
    api_base_url="https://api.starknet.extended.exchange/api/v1",
    stream_url="wss://api.starknet.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.starknet.extended.exchange",
    signing_domain="extended.exchange",
    collateral_asset_contract="",
    asset_operations_contract="",
    collateral_asset_on_chain_id="0x1",
    collateral_decimals=6,
    starknet_domain=StarknetDomain(name="Perpetuals", version="v0", chain_id="SN_MAIN", revision="1"),
    collateral_asset_id="0x1",
)
 The SDK and the SDK documentation will be updated regularly to include additional functionality and more examples.
Getting Started:

For installation instructions, please refer to the description provided.

For reference implementations, explore the examples folder.

For SDK configuration, please refer to the config description.

Supported Features:

Account creation and authorisation.

Order Management.

Account Management.

Transfers.

Withdrawals (for Starknet wallets only).

Market Information.

We are committed to enhancing the SDK with more functionalities based on user feedback and evolving market needs.

Mainnet
Our Mainnet is running on Starknet.

Base URL for the Mainnet API endpoints: https://api.starknet.extended.exchange/.

UI URL: https://app.extended.exchange/perp.

Testnet
Our Testnet is running on Sepolia.

Base URL for the Testnet API endpoints: https://api.starknet.sepolia.extended.exchange/.

UI URL: https://starknet.sepolia.extended.exchange/perp

On the testnet, users can claim $1,000 worth of test USDC per hour for each wallet. This can be done by clicking the 'Claim' button in the 'Account' section, located at the bottom right of the Extended Testnet Trade screen.

Allowed HTTP Verbs
GET: Retrieves a resource or list of resources.

POST: Creates a resource.

PATCH: Updates a resource.

DELETE: Deletes a resource.

Authentication
Due to the trustless, self-custody nature of the Extended exchange, transactions involving user funds require both an API key and a valid Stark signature.

For order management, both an API key and Stark signature are necessary. For other endpoints, only the API key signature is required. Stark signatures are generated using a private Stark key.

Account Creation, API and Stark Key Management
Currently, accounts can be created through the SDK or the User Interface:

SDK - refer to the onboarding example.

User Interface - connect your wallet on extended.exchange to create your Extended account.

You can create up to ten Extended sub-accounts per one wallet address. You can add and manage all sub-accounts associated with your connected wallet in the 'Account' section, located at the bottom right of the Extended Trade screen.

On the API management page, you can obtain API keys, Stark keys, and Vault numbers for each of your sub-accounts. Note that each sub-account is a separate Starknet position and therefore has unique API and Stark keys.

Authenticate Using API Key
Extended uses a simplified authentication scheme for API access. Include your API key in the HTTP header as follows: X-Api-Key: <API_KEY_FROM_API_MANAGEMENT_PAGE_OF_UI>.

Mandatory headers
For both REST and WebSocket API requests, the User-Agent header is required.

Rate Limits
REST API endpoints are subject to rate limits. For real-time data, consider using the WebSockets API instead.

All REST API endpoints are throttled by IP address. Currently, the rate limit is set at 1,000 requests per minute, shared across all endpoints. We plan to increase these limits as our system expands. If you require an increase in the rate limit now, please reach out to our team on Discord.

Higher rate limit of 60,000 requests per 5 minutes apply for the market makers.

When a REST API rate limit is exceeded, a 429 status code will be returned.

Pagination
Paginated response schema:

type PaginatedResponse = {
  "status": "ok" | "error"
  "data": object | object[] | string | number,
  "error": {
    "code": number,
    "message": string
  },
  "pagination": {
    "cursor": number // Current cursor
    "count": number  // Count of the items in the response
  }
}
General not paginated response schema:

type GeneralResponse = {
  "status": "ok" | "error",
  "data": object | object[] | string | number,
  "error": {
    "code": number,
    "message": string
  }
}
The Extended API uses a cursor-based pagination model across all endpoints that may return large volumes of items.

Items are automatically sorted in descending order by ID unless otherwise specified in the endpoint description. As IDs increase over time, the most recent items are always returned first.

Pagination parameters are passed via the query string. These parameters include:

Parameter	Required	Type	Description
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, use the cursor from the pagination section of the previous response.
limit	no	number	The maximum number of items that should be returned.
Public REST-API
The following Public REST API endpoints enable users to access comprehensive information about available markets, their configurations, and trading statistics.

Get markets
HTTP Request
GET /api/v1/info/markets?market={market}

Get a list of available markets, their configurations, and trading statistics.

To request data for several markets, use the following format: GET /api/v1/info/markets?market=market1&market=market2.

Please note that the margin schedule by market is not covered by this endpoint. For more details on the margin schedule, please refer to the documentation.

Market statuses
Status	Description
ACTIVE	Market is active, and all types of orders are permitted.
REDUCE_ONLY	Market is in reduce only mode, and only reduce only orders are allowed.
DELISTED	Market is delisted, and trading is no longer permitted.
PRELISTED	Market is in prelisting stage, and trading not yet available.
DISABLED	Market is completly disabled, and trading is not allowed.
Query Parameters
Parameter	Required	Type	Description
market	no	string[]	List of names of the requested markets.
Response example:

{
  "status": "ok",
  "data": [
    {
      "name": "BTC-USD",
      "assetName": "BTC",
      "assetPrecision": 6,
      "collateralAssetName": "USD",
      "collateralAssetPrecision": 6,
      "active": true,
      "status": "ACTIVE",
      "marketStats": {
        "dailyVolume": "39659164065",
        "dailyVolumeBase": "39659164065",
        "dailyPriceChangePercentage": "5.57",
        "dailyLow": "39512",
        "dailyHigh": "42122",
        "lastPrice": "42000",
        "askPrice": "42005",
        "bidPrice": "39998",
        "markPrice": "39950",
        "indexPrice": "39940",
        "fundingRate": "0.001",
        "nextFundingRate": 1701563440,
        "openInterest": "1245.2",
        "openInterestBase": "1245.2"
      },
      "tradingConfig": {
        "minOrderSize": "0.001",
        "minOrderSizeChange": "0.001",
        "minPriceChange": "0.001",
        "maxMarketOrderValue": "1000000",
        "maxLimitOrderValue": "5000000",
        "maxPositionValue": "10000000",
        "maxLeverage": "50",
        "maxNumOrders": "200",
        "limitPriceCap": "0.05",
        "limitPriceFloor": "0.05"
      },
      "l2Config": {
        "type": "STARKX",
        "collateralId": "0x35596841893e0d17079c27b2d72db1694f26a1932a7429144b439ba0807d29c",
        "collateralResolution": 1000000,
        "syntheticId": "0x4254432d3130000000000000000000",
        "syntheticResolution": 10000000000
      }
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].name	yes	string	Name of the market.
data[].assetName	yes	string	Name of the base asset.
data[].assetPrecision	yes	number	Number of decimals for the base asset.
data[].collateralAssetName	yes	string	Name of the collateral asset.
data[].collateralAssetPrecision	yes	number	Number of decimals for the collateral asset.
data[].active	yes	boolean	Indicates if the market is currently active. Can be true or false.
data[].status	yes	string	Market status.
data[].marketStats.dailyVolume	yes	string	Trading volume of the market in the previous 24 hours in the collateral asset.
data[].marketStats.dailyVolumeBase	yes	string	Trading volume of the market in the previous 24 hours in the base asset.
data[].marketStats.dailyPriceChange	yes	string	Absolute price change of the last trade price over the past 24 hours.
data[].marketStats.dailyPriceChangePercentage	yes	string	Percent price change of the last trade price over the past 24 hours.
data[].marketStats.dailyLow	yes	string	Lowest trade price over the past 24 hours.
data[].marketStats.dailyHigh	yes	string	Highest trade price over the past 24 hours.
data[].marketStats.lastPrice	yes	string	Last price of the market.
data[].marketStats.askPrice	yes	string	Current best ask price of the market.
data[].marketStats.bidPrice	yes	string	Current best bid price of the market.
data[].marketStats.markPrice	yes	string	Current mark price of the market.
data[].marketStats.indexPrice	yes	string	Current index price of the market.
data[].marketStats.fundingRate	yes	string	Current funding rate, calculated every minute.
data[].marketStats.nextFundingRate	yes	number	Timestamp of the next funding update.
data[].marketStats.openInterest	yes	string	Open interest in collateral asset.
data[].marketStats.openInterestBase	yes	string	Open interest in base asset.
data[].tradingConfig.minOrderSize	yes	string	Minimum order size for the market.
data[].tradingConfig.minOrderSizeChange	yes	string	Minimum order size change for the market.
data[].tradingConfig.minPriceChange	yes	string	Minimum price change for the market.
data[].tradingConfig.maxMarketOrderValue	yes	string	Maximum market order value for the market.
data[].tradingConfig.maxLimitOrderValue	yes	string	Maximum limit order value for the market.
data[].tradingConfig.maxPositionValue	yes	string	Maximum position value for the market.
data[].tradingConfig.maxLeverage	yes	string	Maximum leverage available for the market.
data[].tradingConfig.maxNumOrders	yes	string	Maximum number of open orders for the market.
data[].tradingConfig.limitPriceCap	yes	string	Limit order price cap.
data[].tradingConfig.limitPriceFloor	yes	string	Limit order floor ratio.
data[].l2Config.type	yes	string	Type of Layer 2 solution. Currently, only 'STARKX' is supported.
data[].l2Config.collateralId	yes	string	Starknet collateral asset ID.
data[].l2Config.collateralResolution	yes	number	Collateral asset resolution, the number of quantums (Starknet units) that fit within one "human-readable" unit of the collateral asset.
data[].l2Config.syntheticId	yes	string	Starknet synthetic asset ID.
data[].l2Config.syntheticResolution	yes	number	Synthetic asset resolution, the number of quantums (Starknet units) that fit within one "human-readable" unit of the synthetic asset.
Get market statistics
HTTP Request
GET /api/v1/info/markets/{market}/stats

Get the latest trading statistics for an individual market.

Please note that the returned funding rate represents the most recent funding rate, which is calculated every minute.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": {
    "dailyVolume": "10283410.122959",
    "dailyVolumeBase": "3343.1217",
    "dailyPriceChange": "-26.00",
    "dailyPriceChangePercentage": "-0.0084",
    "dailyLow": "3057.98",
    "dailyHigh": "3133.53",
    "lastPrice": "3085.70",
    "askPrice": "3089.05",
    "bidPrice": "3087.50",
    "markPrice": "3088.439710293828",
    "indexPrice": "3089.556987078441",
    "fundingRate": "-0.000059",
    "nextFundingRate": 1716192000000,
    "openInterest": "35827242.257619",
    "openInterestBase": "11600.4344",
    "deleverageLevels": {
      "shortPositions": [
        {
          "level": 1,
          "rankingLowerBound": "-1354535.1454"
        },
        {
          "level": 2,
          "rankingLowerBound": "-6.3450"
        },
        {
          "level": 3,
          "rankingLowerBound": "-0.3419"
        },
        {
          "level": 4,
          "rankingLowerBound": "0.0000"
        }
      ],
      "longPositions": [
        {
          "level": 1,
          "rankingLowerBound": "-2978.4427"
        },
        {
          "level": 2,
          "rankingLowerBound": "0.0000"
        },
        {
          "level": 3,
          "rankingLowerBound": "0.0000"
        },
        {
          "level": 4,
          "rankingLowerBound": "0.0001"
        }
      ]
    }
  }
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.dailyVolume	yes	string	Trading volume of the market in the previous 24 hours in the collateral asset.
data.dailyVolumeBase	yes	string	Trading volume of the market in the previous 24 hours in the base asset.
data.dailyPriceChange	yes	string	Absolute price change of the last trade price over the past 24 hours.
data.dailyPriceChangePercentage	yes	string	Percent price change of the last trade price over the past 24 hours.
data.dailyLow	yes	string	Lowest trade price over the past 24 hours.
data.dailyHigh	yes	string	Highest trade price over the past 24 hours.
data.lastPrice	yes	string	Last price of the market.
data.askPrice	yes	string	Current best ask price of the market.
data.bidPrice	yes	string	Current best bid price of the market.
data.markPrice	yes	string	Current mark price of the market.
data.indexPrice	yes	string	Current index price of the market.
data.fundingRate	yes	string	Current funding rate, calculated every minute.
data.nextFundingRate	yes	number	Timestamp of the next funding update.
data.openInterest	yes	string	Open interest in collateral asset.
data.openInterestBase	yes	string	Open interest in base asset.
data.deleverageLevels	yes	enum	Auto Deleveraging (ADL) levels for long and short positions, ranging from level 1 (lowest risk) to level 4 (highest risk) of ADL. For details, please refer to the documentation.
Get market order book
HTTP Request
GET /api/v1/info/markets/{market}/orderbook

Get the latest orderbook for an individual market.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": {
    "market": "BTC-USD",
    "bid": [
      {
        "qty": "0.04852",
        "price": "61827.7"
      },
      {
        "qty": "0.50274",
        "price": "61820.5"
      }
    ],
    "ask": [
      {
        "qty": "0.04852",
        "price": "61840.3"
      },
      {
        "qty": "0.4998",
        "price": "61864.1"
      }
    ]
  }
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.bid	yes	object[]	List of bid orders.
data.bid[].qty	yes	string	Qty for the price level.
data.bid[].price	yes	string	Bid price.
data.ask	yes	object[]	List of ask orders.
data.ask[].qty	yes	string	Qty for the price level.
data.ask[].price	yes	string	Ask price.
Get market last trades
HTTP Request
GET /api/v1/info/markets/{market}/trades

Get the latest trade for an individual market.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
Successful response example:

{
  "status": "OK",
  "data": [
    {
      "i": 1844000421446684673,
      "m": "BTC-USD",
      "S": "SELL",
      "tT": "TRADE",
      "T": 1728478935001,
      "p": "61998.5",
      "q": "0.04839"
    },
    {
      "i": 1844000955650019328,
      "m": "BTC-USD",
      "S": "SELL",
      "tT": "TRADE",
      "T": 1728479062365,
      "p": "61951.4",
      "q": "0.00029"
    }
  ]
}
Error response example:

{
  "status": "ERROR",
  "error": {
    "code": "NOT_FOUND",
    "message": "Market not found"
  }
}
Response
Parameter	Type	Description
data[].i	number	Trade ID.
data[].m	string	Market name.
data[].S	string	Side of taker trades. Can be BUY or SELL.
data[].tT	string	Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.
data[].T	number	Timestamp (in epoch milliseconds) when the trade happened.
data[].p	string	Trade price.
data[].q	string	Trade quantity in base asset.
Get candles history
HTTP Request
GET /api/v1/info/candles/{market}/{candleType}

Get the candles history for an individual market for the timeframe specified in the request. Candles are sorted by timestamp in descending order.

Available price types include:

Trades (last) price: GET /api/v1/info/candles/{market}/trades.

Mark price: GET /api/v1/info/candles/{market}/mark-prices.

Index price: GET /api/v1/info/candles/{market}/index-prices.

The endpoint returns a maximum of 10,000 records.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
candleType	yes	string	Price type. Can be trades, mark-prices, or index-prices.
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	The time interval between data points.
limit	yes	number	The maximum number of items that should be returned.
endTime	no	number	End timestamp (in epoch milliseconds) for the requested period.
Response example:

{
  "status": "OK",
  "data": [
    {
      "o": "65206.2",
      "l": "65206.2",
      "h": "65206.2",
      "c": "65206.2",
      "v": "0.0",
      "T": 1715797320000
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR
data[].o	yes	string	Open price.
data[].c	yes	string	Close price.
data[].h	yes	string	Highest price.
data[].l	yes	string	Lowest price.
data[].v	yes	string	Trading volume (Only for trades candles).
data[].T	yes	number	Starting timestamp (in epoch milliseconds) for the candle.
Get funding rates history
HTTP Request
GET /api/v1/info/{market}/funding?startTime={startTime}&endTime={endTime}

Get the funding rates history for an individual market for the timeframe specified in the request. The funding rates are sorted by timestamp in descending order.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

While the funding rate is calculated every minute, it is only applied once per hour. The records represent the 1-hour rates that were applied for the payment of funding fees.

For details on how the funding rate is calculated on Extended, please refer to the documentation.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Names of the requested market.
Query Parameters
Parameter	Required	Type	Description
startTime	yes	number	Starting timestamp (in epoch milliseconds) for the requested period.
endTime	yes	number	Ending timestamp (in epoch milliseconds) for the requested period.
cursor	no	number	Determines the offset of the returned result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "m": "BTC-USD",
      "T": 1701563440,
      "f": "0.001"
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].m	yes	string	Name of the requested market.
data[].T	yes	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
data[].f	yes	string	Funding rates used for funding fee payments.
Get open interest history
HTTP Request
GET /api/v1/info/{market}/open-interests?interval={interval}&startTime={startTime}&endTime={endTime}

Get the open interest history for an individual market for the timeframe specified in the request. The open interests are sorted by timestamp in descending order.

The endpoint returns a maximum of 300 records; proper combination of start and end time should be used to access records beyond this limit.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Names of the requested market.
Query Parameters
Parameter	Required	Type	Description
startTime	yes	number	Starting timestamp (in epoch milliseconds) for the requested period.
endTime	yes	number	Ending timestamp (in epoch milliseconds) for the requested period.
interval	yes	enum	P1H for hour and P1D for day
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "i": "151193.8952300000000000",
      "I": "430530.0000000000000000",
      "t": 1749513600000
    },
    {
      "i": "392590.9522500000000000",
      "I": "1147356.0000000000000000",
      "t": 1749600000000
    },
    {
      "i": "397721.7285100000000000",
      "I": "1224362.0000000000000000",
      "t": 1749686400000
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].i	yes	string	Open interest in USD.
data[].I	yes	string	Open interest in synthetic asset.
data[].t	yes	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
Get builder dashboard
GET /api/v1/info/builder/dashboard

Response example:

{
  "status": "OK",
  "data": {
    "total": [
      {
        "builderName": "FlowBot",
        "volume": "439912489.2299",
        "extendedFees": "106512.842391",
        "activeUsers": 181
      }
    ],
    "daily": [
      {
        "date": "2025-12-15",
        "builderName": "FlowBot",
        "volume": "12720299.02594",
        "extendedFees": "3180.074578",
        "activeUsers": 24
      },
      {
        "date": "2025-12-16",
        "builderName": "FlowBot",
        "volume": "11827429.94026",
        "extendedFees": "2956.857352",
        "activeUsers": 21
      }
    ]
  }
}
Returns builder dashboard statistics including total and daily trading volume, fees, and active users for the authenticated builder.

Response
Parameter	Required	Type	Description
data.total	yes	object[]	Array containing total aggregated statistics.
data.total[].builderName	yes	string	Name of the builder.
data.total[].volume	yes	string	Total trading volume generated by the builder.
data.total[].extendedFees	yes	string	Total fees earned by the builder to the extended exchange.
data.total[].activeUsers	yes	number	Total number of active users for the builder.
data.daily	yes	object[]	Array containing daily statistics.
data.daily[].date	yes	string	Date in YYYY-MM-DD format.
data.daily[].builderName	yes	string	Name of the builder.
data.daily[].volume	yes	string	Daily trading volume generated by the builder.
data.daily[].extendedFees	yes	string	Daily fees earned by the builder to the extended exchange.
data.daily[].activeUsers	yes	number	Number of active users for the builder on that date.
Private REST-API
Account
You can create up to ten Extended sub-accounts for each wallet address. For more details, please refer to the Authentication section of the API Documentation.

The Private API endpoints listed below grant access to details specific to each sub-account, such as balances, transactions, positions, orders, trades, and the fee rates applied. Additionally, there are endpoints for retrieving the current leverage and adjusting it.

Please note that all endpoints in this section will only return records for the authenticated sub-account.

Get account details
HTTP Request
GET /api/v1/user/account/info

Response example:

 {
  "status": "OK",
  "data": {
    "status": "ACTIVE",
    "l2Key": "0x123",
    "l2Vault": 321,
    "accountId": 123,
    "description": "abc",
    "bridgeStarknetAddress": "0x21be84f913dbddbfc0a3993e1f949933139f427f88eb6bfd247ab3ef7174487"
  }
}
Get current account details.

Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.status	yes	string	Account status.
data.l2Key	yes	string	Account public key in perp contract.
data.l2Vault	yes	string	Position ID in perp contract.
data.accountId	yes	string	Account ID.
data.description	no	string	Account description (name).
data.bridgeStarknetAddress	yes	string	Starknet account address for EVM bridging.
Get balance
HTTP Request
GET /api/v1/user/balance

Get key balance details for the authenticated sub-account. Returns a 404 error if the user’s balance is 0.

Account Balance = Deposits - Withdrawals + Realised PnL.

Equity = Account Balance + Unrealised PnL.

Available Balance for Trading = Equity - Initial Margin Requirement.

Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirement).

Unrealised PnL (mark-price-based) = The sum of unrealised PnL across open positions, calculated as Position Size * (Mark Price - Entry Price).

Unrealised PnL (mid-price-based) = The sum of unrealised PnL across open positions, calculated as Position Size * (Mid Price - Entry Price).

Initial Margin Requirement for a given market = Max(Abs(Position Value + Value of Buy Orders), Abs(Position Value + Value of Sell Orders))*1/Leverage.

Account Margin Ratio = Maintenance Margin requirement of all open positions / Equity. Liquidation is triggered when Account Margin Ratio > 100%.

Account Exposure = Sum(All positions value)

Account Leverage = Exposure / Equity.

Response example:

{
  "status": "OK",
  "data": {
    "collateralName": "USDC",
    "balance": "13500",
    "equity": "12000",
    "availableForTrade": "1200",
    "availableForWithdrawal": "100",
    "unrealisedPnl": "-10.1",
    "initialMargin": "160",
    "marginRatio": "1.5",
    "exposure": "12751.859629",
    "leverage": "1275.1860",
    "updatedTime": 1701563440
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.collateralName	yes	string	Name of the collateral asset used for the account.
data.balance	yes	string	Account balance expressed in the collateral asset, also known as Wallet balance.
data.equity	yes	string	Equity of the account.
data.availableForTrade	yes	string	Available Balance for Trading.
data.availableForWithdrawal	yes	string	Available Balance for Withdrawals.
data.unrealisedPnl	yes	string	Current unrealised PnL of the account.
data.initialMargin	yes	string	Collateral used to open the positions and orders.
data.marginRatio	yes	string	Margin ratio of the account.
data.exposure	yes	string	Exposure of the account.
data.leverage	yes	string	Leverage of the account.
data.updatedTime	yes	number	Timestamp (in epoch milliseconds) when the server generated the balance message.
Get deposits, withdrawals, transfers history
HTTP Request
GET /api/v1/user/assetOperations?&type={type}&status={status}

Get the history of deposits, withdrawals, and transfers between sub-accounts for the authenticated sub-account. Optionally, the request can be filtered by a specific transaction type or status.

The endpoint returns 50 records per page; pagination should be used to access records beyond this limit. Transactions are sorted by timestamp in descending order.

Transactions types
Transaction	Description
DEPOSIT	Deposit.
CLAIM	Testing funds claim. Available only on Extended Testnet.
TRANSFER	Transfer between sub-accounts within one wallet.
WITHDRAWAL	Withdrawal.
Transactions statuses
Status	Description
CREATED	Transaction created on Extended.
IN_PROGRESS	Transaction is being processed by Extended, Starknet or bridge provider.
COMPLETED	Transaction completed.
REJECTED	Transaction rejected.
Response example:

{
    "status": "OK",
    "data": [
        {
            "id": "1951255127004282880",
            "type": "TRANSFER",
            "status": "COMPLETED",
            "amount": "-3.0000000000000000",
            "fee": "0",
            "asset": 1,
            "time": 1754050449502,
            "accountId": 100009,
            "counterpartyAccountId": 100023
        },
        {
            "id": "0x6795eac4ebbdd9fb88f85e3ce4ce4e61895049591c89ad5db8046a4546d2cdd",
            "type": "DEPOSIT",
            "status": "COMPLETED",
            "amount": "4.9899990000000000",
            "fee": "0.0000000000000000",
            "asset": 1,
            "time": 1753872990528,
            "accountId": 100009,
            "transactionHash": "0x93829e61480b528bb18c1b94f0afbc672fb2b340fbfd2f329dffc4180e24b894",
            "chain": "ETH"
        },
        {
            "id": "1950490023665475584",
            "type": "WITHDRAWAL",
            "status": "COMPLETED",
            "amount": "-4.0000000000000000",
            "fee": "0.0001000000000000",
            "asset": 1,
            "time": 1753868034651,
            "accountId": 100009,
            "transactionHash": "0x6d89968d72fc766691d4772048edaf667c88894aedf71f0490c2592c1d268691",
            "chain": "ETH"
        },
    ],
    "pagination": {
        "cursor": 23,
        "count": 23
    }
}
Query Parameters
Parameter	Required	Type	Description
type	no	string	Transaction type. Refer to the list of transaction types in the endpoint description above.
status	no	string	Transaction status. Refer to the list of statuses in the endpoint description above.
cursor	no		Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response
Parameter	Required	Type	Description
status	yes	string	Response status. Can be OK or ERROR.
data[].id	yes	number or string	Transaction ID. A number assigned by Extended for transfers and withdrawals. An onchain id string for deposits.
data[].type	yes	string	Transaction type. Refer to the list of transaction types in the endpoint description above.
data[].status	yes	string	Transaction status. Refer to the list of statuses in the endpoint description above.
data[].amount	yes	string	Transaction amount, absolute value in collateral asset.
data[].fee	yes	string	Fee paid.
data[].asset	yes	string	Collateral asset name.
data[].time	yes	number	Timestamp (epoch milliseconds) when the transaction was updated.
data[].accountId	yes	number	Account ID; source account for transfers and withdrawals; destination account for deposits.
data[].counterpartyAccountId	no	number	Account ID; destination account for transfers.
data[].transactionHash	no	string	Onchain transaction hash. Not available for transfers.
data[].chain	no	string	Source chain name for deposits; target chain name for withdrawals.
Get positions
HTTP Request
GET /api/v1/user/positions?market={market}&side={side}

Get all open positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for multiple markets, use the following format: GET /api/v1/user/positions?market=market1&market2.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be LONG or SHORT.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1,
      "accountId": 1,
      "market": "BTC-USD",
      "side": "LONG",
      "leverage": "10",
      "size": "0.1",
      "value": "4000",
      "openPrice": "39000",
      "markPrice": "40000",
      "liquidationPrice": "38200",
      "margin": "20",
      "unrealisedPnl": "1000",
      "realisedPnl": "1.2",
      "tpTriggerPrice": "41000",
      "tpLimitPrice": "41500",
      "slTriggerPrice": "39500",
      "slLimitPrice": "39000",
      "adl": "2.5",
      "maxPositionSize": "0.2",
      "createdTime": 1701563440000,
      "updatedTime": 1701563440
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Position ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].leverage	yes	string	Position leverage.
data[].size	yes	string	Position size, absolute value in base asset.
data[].value	yes	string	Position value, absolute value in collateral asset.
data[].openPrice	yes	string	Position's open (entry) price.
data[].markPrice	yes	string	Current mark price of the market.
data[].liquidationPrice	yes	string	Position's liquidation price.
data[].margin	yes	string	Position's margin in collateral asset.
data[].unrealisedPnl	yes	string	Position's Unrealised PnL.
data[].realisedPnl	yes	string	Position's Realised PnL.
data[].tpTriggerPrice	no	string	Take Profit Trigger price.
data[].tpLimitPrice	no	string	Take Profit Limit price.
data[].slTriggerPrice	no	string	Stop Loss Trigger price.
data[].slLimitPrice	no	string	Stop Loss Limit price.
data[].maxPositionSize	yes	string	Maximum allowed position size, absolute value in base asset.
data[].adl	yes	string	Position's Auto-Deleveraging (ADL) ranking in the queue, expressed as a percentile. A value closer to 100 indicates a higher likelihood of being ADLed.
data[].createdTime	yes	number	Timestamp (epoch milliseconds) when the position was created.
data[].updatedTime	yes	number	Timestamp (epoch milliseconds) when the position was updated.
Get positions history
HTTP Request
GET /api/v1/user/positions/history?market={market}&side={side}

Get all open and closed positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for several markets, use the following format: GET /api/v1/user/positions/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be long or short.
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "accountId": 1,
      "market": "BTC-USD",
      "side": "LONG",
      "exitType": "TRADE",
      "leverage": "10",
      "size": "0.1",
      "maxPositionSize": "0.2",
      "openPrice": "39000",
      "exitPrice": "40000",
      "realisedPnl": "1.2",
      "createdTime": 1701563440000,
      "closedTime": 1701563440
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Position ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].exitType	no	string	The exit type of the last trade that reduced the position. Can be TRADE, LIQUIDATION, or DELEVERAGE.
data[].leverage	yes	string	Position leverage.
data[].size	yes	string	Position size, absolute value in base asset.
data[].maxPositionSize	yes	string	Maximum position size during the position's lifetime, absolute value in base asset.
data[].openPrice	yes	string	The weighted average price of trades that contributed to increasing the position.
data[].exitPrice	no	string	The weighted average price of trades that contributed to decreasing the position.
data[].realisedPnl	yes	string	Position Realised PnL.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) when the position was created.
data[].closedTime	no	number	Timestamp (in epoch milliseconds) when the position was closed, applicable only for closed positions.
Get open orders
HTTP Request
GET /api/v1/user/orders?market={market}&type={type}&side={side}

Get all open orders for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, conditional, tpsl or twap).

Open orders correspond to the following order statuses from the list below: new, partially filled, untriggered.

To request data for several markets, use the following format: GET /api/v1/user/orders?market=market1&market2.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
Order status reasons (when cancelled or rejected)
Reason	Description
NONE	Order was accepted.
UNKNOWN	Technical status reason.
UNKNOWN_MARKET	Market does not exist.
DISABLED_MARKET	Market is not active.
NOT_ENOUGH_FUNDS	Insufficient balance to create order.
NO_LIQUIDITY	Not enough liquidity in the market to execute the order.
INVALID_FEE	Fee specified in the create order request is invalid.
INVALID_QTY	Quantity specified is invalid.
INVALID_PRICE	Price specified is invalid.
INVALID_VALUE	Order exceeds the maximum value.
UNKNOWN_ACCOUNT	Account does not exist.
SELF_TRADE_PROTECTION	Order cancelled to prevent self-trading.
POST_ONLY_FAILED	Order could not be posted as a post-only order.
REDUCE_ONLY_FAILED	Reduce-only order failed due to position size conflict.
INVALID_EXPIRE_TIME	Expiration time specified is invalid.
POSITION_TPSL_CONFLICT	TPSL order for the entire position already exists.
INVALID_LEVERAGE	Leverage specified is invalid.
PREV_ORDER_NOT_FOUND	The order to be replaced does not exist.
PREV_ORDER_TRIGGERED	The order to be replaced has been triggered and cannot be replaced.
TPSL_OTHER_SIDE_FILLED	The opposite side of a TP/SL order has been filled.
PREV_ORDER_CONFLICT	Conflict with an existing order during replacement.
ORDER_REPLACED	Order has been replaced by another order.
POST_ONLY_MODE	Exchange is in post-only mode, only post-only orders are allowed.
REDUCE_ONLY_MODE	Exchange is in reduce-only mode, only reduce-only orders are allowed.
TRADING_OFF_MODE	Trading is currently disabled.
NEGATIVE_EQUITY	Account has negative equity.
ACCOUNT_LIQUIDATION	Account is under liquidation.
Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
type	no	string	Order type. Can be LIMIT, CONDITIONAL, TPSL or TWAP.
side	no	string	Order side. Can be BUY or SELL.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1775511783722512384,
      "accountId": 3017,
      "externalId": "2554612759479898620327573136214120486511160383028978112799136270841501275076",
      "market": "ETH-USD",
      "type": "LIMIT",
      "side": "BUY",
      "status": "PARTIALLY_FILLED",
      "price": "3300",
      "averagePrice": "3297.00",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "trigger": {
        "triggerPrice": "3300",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "takeProfit": {
        "triggerPrice": "3500",
        "triggerPriceType": "LAST",
        "price": "3340",
        "priceType": "MARKET"
      },
      "stopLoss": {
        "triggerPrice": "2800",
        "triggerPriceType": "LAST",
        "price": "2660",
        "priceType": "MARKET"
      },
      "reduceOnly": false,
      "postOnly": false,
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1712754771819
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type. Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get orders history
HTTP Request
GET /api/v1/user/orders/history?market={market}&type={type}&side={side}&id={id}&externalId={externalId}

Get orders history for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, market, conditional, tpsl or twap). Note: Scaled orders are represented as multiple individual limit orders in the system.

Orders history corresponds to the following order statuses from the list below: filled, cancelled, rejected, expired.

To request data for several markets, use the following format: GET /api/v1/user/orders/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. The records for closed non-filled orders are available only for the past 7 days.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
Query Parameters
Parameter	Required	Type	Description
id	no	number	List of internal Ids of the requested orders.
externalId	no	string[]	List of external Ids of the requested orders.
market	no	string[]	List of names of the requested markets.
type	no	string	Order type. Can be limit, market, conditional, tpsl or twap.
side	no	string	Order side. Can be buy or sell.
cursor	no	number	Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.
limit	no	number	Maximum number of items that should be returned.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "externalId": "ExtId-1",
      "accountId": 1,
      "market": "BTC-USD",
      "status": "FILLED",
      "type": "LIMIT",
      "side": "BUY",
      "price": "39000",
      "averagePrice": "39000",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "reduceOnly": false,
      "postOnly": false,
      "trigger": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "tpslType": "ORDER",
      "takeProfit": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "stopLoss": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1706563440
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get order by id
HTTP Request
GET /api/v1/user/orders/{id}

Get order by id for the authenticated sub-account.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
URL Parameters
Parameter	Required	Type	Description
id	yes	number	Order to be retrieved, ID assigned by Extended.
Response example:

{
  "status": "OK",
  "data": {
    "id": 1784963886257016832,
    "externalId": "ExtId-1",
    "accountId": 1,
    "market": "BTC-USD",
    "status": "FILLED",
    "type": "LIMIT",
    "side": "BUY",
    "price": "39000",
    "averagePrice": "39000",
    "qty": "0.2",
    "filledQty": "0.1",
    "payedFee": "0.0120000000000000",
    "reduceOnly": false,
    "postOnly": false,
    "trigger": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "triggerPriceDirection": "UP",
      "executionPriceType": "MARKET"
    },
    "tpslType": "ORDER",
    "takeProfit": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "price": "35000",
      "priceType": "MARKET",
      "starkExSignature": ""
    },
    "stopLoss": {
      "triggerPrice": "34000",
      "triggerPriceType": "LAST",
      "price": "35000",
      "priceType": "MARKET",
      "starkExSignature": ""
    },
    "createdTime": 1701563440000,
    "updatedTime": 1701563440000,
    "timeInForce": "IOC",
    "expireTime": 1706563440
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.id	yes	number	Order ID assigned by Extended.
data.externalId	yes	string	Order ID assigned by user.
data.accountId	yes	number	Account ID.
data.market	yes	string	Market name.
data.status	yes	string	Order status.
data.statusReason	no	string	Reason for REJECTED or CANCELLED status.
data.type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data.side	yes	string	Order side. Can be BUY or SELL.
data.price	no	string	Worst accepted price in the collateral asset.
data.averagePrice	no	string	Actual filled price, empty if not filled.
data.qty	yes	string	Order size in base asset.
data.filledQty	no	string	Actual filled quantity in base asset.
data.payedFee	no	string	Paid fee.
data.reduceOnly	no	boolean	Whether the order is Reduce-only.
data.postOnly	no	boolean	Whether the order is Post-only.
data.trigger.triggerPrice	no	string	Trigger price for conditional orders.
data.trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data.trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data.trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data.tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data.takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data.takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data.takeProfit.price	no	string	Take Profit order price.
data.takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data.stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data.stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data.stopLoss.price	no	string	Stop loss order price.
data.stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data.createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data.updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data.timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data.expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get orders by external id
HTTP Request
GET /api/v1/user/orders/external/{externalId}

Get orders by external id for the authenticated sub-account.

Order statuses
Status	Description
NEW	Order in the order book, unfilled.
PARTIALLY_FILLED	Order in the order book, partially filled.
FILLED	Order fully filled.
UNTRIGGERED	Conditional order waiting for the trigger price.
CANCELLED	Order cancelled.
REJECTED	Order rejected.
EXPIRED	Order expired.
TRIGGERED	Technical status, transition from UNTRIGGERED to NEW.
URL Parameters
Parameter	Required	Type	Description
externalId	yes	number	Order to be retrieved, ID assigned by user.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "externalId": "ExtId-1",
      "accountId": 1,
      "market": "BTC-USD",
      "status": "FILLED",
      "type": "LIMIT",
      "side": "BUY",
      "price": "39000",
      "averagePrice": "39000",
      "qty": "0.2",
      "filledQty": "0.1",
      "payedFee": "0.0120000000000000",
      "reduceOnly": false,
      "postOnly": false,
      "trigger": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "triggerPriceDirection": "UP",
        "executionPriceType": "MARKET"
      },
      "tpslType": "ORDER",
      "takeProfit": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "stopLoss": {
        "triggerPrice": "34000",
        "triggerPriceType": "LAST",
        "price": "35000",
        "priceType": "MARKET",
        "starkExSignature": ""
      },
      "createdTime": 1701563440000,
      "updatedTime": 1701563440000,
      "timeInForce": "IOC",
      "expireTime": 1706563440
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Order ID assigned by Extended.
data[].externalId	yes	string	Order ID assigned by user.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].status	yes	string	Order status.
data[].statusReason	no	string	Reason for REJECTED or CANCELLED status.
data[].type	yes	string	Order type. Can be LIMIT, MARKET, CONDITIONAL, TPSL or TWAP.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].price	no	string	Worst accepted price in the collateral asset.
data[].averagePrice	no	string	Actual filled price, empty if not filled.
data[].qty	yes	string	Order size in base asset.
data[].filledQty	no	string	Actual filled quantity in base asset.
data[].payedFee	no	string	Paid fee.
data[].reduceOnly	no	boolean	Whether the order is Reduce-only.
data[].postOnly	no	boolean	Whether the order is Post-only.
data[].trigger.triggerPrice	no	string	Trigger price for conditional orders.
data[].trigger.triggerPriceType	no	string	Trigger price type . Can be LAST, MARK or INDEX.
data[].trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).
data[].trigger.executionPriceType	no	string	Execution price type. Can be LIMIT or MARKET.
data[].tpSlType	no	string	TPSL type determining TPSL order size. Can be ORDER or POSITION.
data[].takeProfit.triggerPrice	no	string	Take Profit Trigger price.
data[].takeProfit.triggerPriceType	no	string	Take Profit Trigger price type. Can be LAST, MARK or INDEX.
data[].takeProfit.price	no	string	Take Profit order price.
data[].takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as MARKET or LIMIT order.
data[].stopLoss.triggerPrice	no	string	Stop loss Trigger price.
data[].stopLoss.triggerPriceType	no	string	Stop Loss Trigger price type. Can be LAST, MARK or INDEX.
data[].stopLoss.price	no	string	Stop loss order price.
data[].stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) of order creation.
data[].updatedTime	yes	number	Timestamp (in epoch milliseconds) of order update.
data[].timeInForce	yes	string	Time-in-force. Can be GTT (Good till time) or IOC (Immediate or cancel).
data[].expireTime	yes	number	Timestamp (in epoch milliseconds) when the order expires.
Get trades
HTTP Request
GET /api/v1/user/trades?market={market}&type={type}&side={side}

Get trades history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by trade type (trade, liquidation or deleverage) and side (buy or sell).

To request data for several markets, use the following format: GET /api/v1/user/trades?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
type	no	string	Trade type. Can be trade, liquidation or deleverage.
side	no	string	Order side. Can be buy or sell.
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 1784963886257016832,
      "accountId": 3017,
      "market": "BTC-USD",
      "orderId": 9223372036854775808,
      "externalId": "ext-1",
      "side": "BUY",
      "price": "58853.4000000000000000",
      "qty": "0.0900000000000000",
      "value": "5296.8060000000000000",
      "fee": "0.0000000000000000",
      "tradeType": "DELEVERAGE",
      "createdTime": 1701563440000,
      "isTaker": true
    }
  ],
  "pagination": {
    "cursor": 1784963886257016832,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Trade ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].orderId	yes	string	Order ID assigned by Extended.
data[].externalOrderId	yes	string	Order ID assigned by user. Populated only on websocket stream.
data[].side	yes	string	Order side. Can be BUY or SELL.
data[].averagePrice	yes	string	Actual filled price.
data[].filledQty	yes	string	Actual filled quantity in base asset.
data[].value	yes	string	Actual filled absolute nominal value in collateral asset.
data[].fee	yes	string	Paid fee.
data[].isTaker	yes	boolean	Whether the trade was executed as a taker.
data[].tradeType	yes	string	Trade type. Can be TRADE (for regular trades), LIQUIDATION (for liquidaton trades) or DELEVERAGE (for ADL trades).
data[].createdTime	yes	number	Timestamp (in epoch milliseconds) when the trade happened.
Get funding payments
HTTP Request
GET /api/v1/user/funding/history?market={market}&side={side}&fromTime={fromTime}

Get funding payments history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by side (long or short) and from time as a start point.

To request data for several markets, use the following format: GET /api/v1/user/funding/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

Query Parameters
Parameter	Required	Type	Description
market	no	string	List of names of the requested markets.
side	no	string	Position side. Can be long or short.
fromTime	yes	number	Starting timestamp (in epoch milliseconds).
Response example:

{
  "status": "OK",
  "data": [
    {
      "id": 8341,
      "accountId": 3137,
      "market": "BNB-USD",
      "positionId": 1821237954501148672,
      "side": "LONG",
      "size": "1.116",
      "value": "560.77401888",
      "markPrice": "502.48568",
      "fundingFee": "0",
      "fundingRate": "0",
      "paidTime": 1723147241346
    }
  ],
  "pagination": {
    "cursor": 8341,
    "count": 1
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data[].id	yes	number	Funding payment ID assigned by Extended.
data[].accountId	yes	number	Account ID.
data[].market	yes	string	Market name.
data[].positionId	yes	number	Position ID assigned by Extended.
data[].side	yes	string	Position side. Can be LONG or SHORT.
data[].value	yes	string	Position value at funding payment time.
data[].markPrice	yes	string	Mark price at funding payment time
data[].fundingFee	yes	string	Funding payment size.
data[].fundingRate	yes	string	Funding rate.
data[].paidTime	yes	number	Timestamp (in epoch milliseconds) when the funding payment happened.
Get rebates
HTTP Request
GET /api/v1/user/rebates/stats

Get rebates related data for the authenticated sub-account.

Response example:

{
  "status": "OK",
  "data": [
    {
      "totalPaid": "0",
      "rebatesRate": "0",
      "marketShare": "0.002",
      "nextTierMakerShare": "0.01",
      "nextTierRebateRate": "0.00005"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.totalPaid	yes	string	Total rebates paid.
data.rebatesRate	yes	string	Current rebates rate.
data.marketShare	yes	string	Maker volume share.
data.nextTierMakerShare	yes	string	Maker volume share required to increase rebates.
data.nextTierRebateRate	yes	string	Rebates rate for next maker share threshold.
Get current leverage
HTTP Request
GET /api/v1/user/leverage?market={market}

Get current leverage for the authenticated sub-account. You can get current leverage for all markets, a single market, or multiple specific markets.

To request data for several markets, use the format GET/api/v1/user/leverage?market=market1&market=market2.

Query Parameters
Parameter	Required	Type	Description
market	no	string	Name of the requested market.
Response example:

{
  "status": "OK",
  "data": [
    {
      "market": "SOL-USD",
      "leverage": "10"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.leverage	yes	string	Current leverage.
Update leverage
HTTP Request
PATCH /api/v1/user/leverage

Update leverage for an individual market.

Modifying your leverage will impact your Available balance and Initial Margin requirements of your open position and orders in the market.

To adjust your leverage, you must meet two requirements:

The total value of your open position and triggered orders must remain below the maximum position value allowed for the selected leverage.

Your Available balance must be sufficient to cover the additional Margin requirements (if any) associated with the new leverage.

Failure to meet either of these criteria will result in an error.

For details on Margin requirements, please refer to the documentation.

Request example:

{
  "market": "BTC-USD",
  "leverage": "10"
}
Body Parameters
Parameter	Required	Type	Description
market	yes	string	Name of the requested market.
leverage	yes	string	Target leverage.
Response example:

{
  "status": "OK",
  "data": {
    "market": "BTC-USD",
    "leverage": "10"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.leverage	yes	string	Updated leverage.
Get fees
HTTP Request
GET /api/v1/user/fees?market={market}

Get current fees for the sub-account. Currently, Extended features a flat fee structure:

Taker: 0.025%

Maker: 0.000%

The team reserves the right to update the fee schedule going forward.

For updates on the Fee Schedule, please refer to the documentation.

Query Parameters
Parameter	Required	Type	Description
market	no	string	Name of the requested market.
builderId	no	string	builder client id
Response example:

{
  "status": "OK",
  "data": [
    {
      "market": "BTC-USD",
      "makerFeeRate": "0.00000",
      "takerFeeRate": "0.00025",
      "builderFeeRate": "0.0001"
    }
  ]
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.market	yes	string	Market name.
data.makerFeeRate	yes	string	Maker fee rate.
data.takerFeeRate	yes	string	Taker fee rate.
data.builderFeeRate	yes	string	Builder fee rate.
Order management
The Private API endpoints listed below allow you to create, cancel, and manage orders from the authenticated sub-account.

Starknet-Specific Logic
Extended settles all transactions on-chain on Starknet. As a result, order creation might differ from centralized exchanges in a few ways:

Stark Key Signature: Required for all order management endpoints. For details, please refer to the reference implementation in the Python SDK.

Price Parameter: All orders, including market orders, require a price as a mandatory parameter.

Fee Parameter: All orders require a fee as a mandatory parameter. The Fee parameter represents the maximum fee a user is willing to pay for an order. Use the maker fee for Post-only orders and the taker fee for all other orders. Enter the fee in decimal format (e.g., 0.1 for 10%). To view current fees, use the Get fees endpoint, which displays applicable fee rates.

Expiration Timestamp: All orders, including Fill or Kill and Immediate or Cancel orders, require an expiration timestamp as a mandatory parameter. When submitting orders via the API, enter the expiration time as an epoch timestamp in milliseconds. On the Mainnet, the maximum allowable expiration time is 90 days from the order creation date. On the Testnet, 28 days from the order creation date.

Market Orders: Extended does not natively support market orders. On the UI, market orders are created as limit Immediate-or-Cancel orders with a price parameter set to ensure immediate execution. For example, Market Buy Orders are set at the best ask price multiplied by 1.0075, and Market Sell Orders at the best bid price multiplied by 0.9925 (subtracting 0.75%).

TPSL Orders: Orders with Take Profit and/or Stop Loss require multiple signatures.

Create or edit order
HTTP Request
POST /api/v1/user/order

Create a new order or edit (replace) an open order. When you create an order via our REST API, the initial response will confirm whether the order has been successfully accepted. Please be aware that, although rare, orders can be canceled or rejected by the Matching Engine even after acceptance at the REST API level. To receive real-time updates on your order status, subscribe to the Account updates WebSocket stream. This stream provides immediate notifications of any changes to your orders, including confirmations, cancellations, and rejections.

Currently, we support limit, market, conditional and tpsl order types via API, along with reduce-only and post-only settings. For API trading, we offer the following Time-in-force settings: GTT (Good till time - default) and IOC (Immediate or cancel). On the Mainnet, the maximum allowable expiration time for GTT orders is 90 days from the order creation date. On the Testnet, 28 days from the order creation date. For details on supported order types and settings, please refer to the documentation.

To successfully place an order, it must meet the following requirements:

Trading Rules. For detailed information, please refer to the trading rules documentation.

Order Cost Requirements. For detailed information, please refer to the order cost documentation.

Margin Schedule Requirements. For detailed information, please refer to the margin schedule documentation.

Price requirements, which are described below.

Price requirements
Limit Orders
Long Limit Orders: Order Price ≤ Mark Price * (1+Limit Order Price Cap)
Short Limit Orders: Order Price ≥ Mark Price * (1-Limit Order Floor Ratio)
Market Orders
Long Market Order: Order Price ≤ Mark Price * (1 + 5%)
Short Market Order: Order Price ≥ Mark Price * (1 - 5%)
Conditional Orders
Short Conditional Orders: Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)
Long Conditional Orders: Order Price ≤ Trigger Price * (1+Limit Order Price Cap)
TPSL Orders
Entry order: Buy; TPSL order: Sell.

Validation	Stop loss	Take profit
Trigger price validation	Trigger price < Entry order price	Trigger price > Entry order price.
Limit price validation	Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)	Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)
Entry order: Sell; TPSL order: Buy.

Validation	Stop loss	Take profit
Trigger price validation	Trigger price > Entry order price.	Trigger price < Entry order price.
Limit price validation	Order Price ≤ Trigger Price * (1+Limit Order Price Cap)	Order Price ≤ Trigger Price * (1+Limit Order Price Cap)
Orders Edit
To edit (replace) an open order, add its ID as the cancelId parameter. You can edit multiple parameters at once. Editing is available for all orders except for triggered TPSL orders.

Order editing and validations:

If any updated parameter fails the validations described above, all updates will be rejected.
If validations fail at the REST API level, the initial open order remains unchanged.
In the rare event that validations pass at the REST API level but fail at the Matching Engine, both the updated order and the initial open order will be cancelled.
Editable Order Parameters:

For All Order Types (except triggered TPSL orders): Order price and Execution Order Price Type (market or limit)
For All Order Types (except untriggered entire position TPSL orders and triggered TPSL orders): Order size
For Conditional and Untriggered TPSL Orders: Trigger price
For Conditional Orders: Trigger price direction (up or down)
For Non-TPSL Orders: All TPSL parameters
Self trade protection
Self-trade protection is a mechanism that prevents orders from the same client or sub-account from executing against each other. When two such orders are about to match, the system applies the self-trade protection mode specified on the taker order to determine how to handle the potential self-match.

Value	Description
DISABLED	Self trade protection is disabled
ACCOUNT	Trades within same sub-account are disabled, trades between sub-accounts are enabled.
CLIENT	Trades within same sub-account and between sub-accounts are disabled.
Request
Request example:

{
  "id": "e581a9ca-c3a2-4318-9706-3f36a2b858d3",
  "market": "BTC-USDT",
  "type": "CONDITIONAL",
  "side": "BUY",
  "qty": "1",
  "price": "1000",
  "timeInForce": "GTT",
  "expiryEpochMillis": 1715884049245,
  "fee": "0.0002",
  "nonce": "876542",
  "settlement": {
    "signature": {
      "r": "0x17a89cb97c64f546d2dc9189e1ef73547487b228945dcda406cd0e4b8301bd3",
      "s": "0x385b65811a0fc92f109d5ebc30731efd158ee4e502945cd2fcb35a4947b045e"
    },
    "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
    "collateralPosition": "4272448241247734333"
  },
  "reduceOnly": true,
  "postOnly": false,
  "selfTradeProtectionLevel": "ACCOUNT",
  "trigger": {
    "triggerPrice": "12000",
    "triggerPriceType": "LAST",
    "direction": "UP",
    "executionPriceType": "LIMIT"
  },
  "tpSlType": "ORDER",
  "takeProfit": {
    "triggerPrice": "1050",
    "triggerPriceType": "LAST",
    "price": "1300",
    "priceType": "LIMIT",
    "settlement": {
      "signature": {
        "r": "0x5b45f0fb2b8e075f6a5f9b4c039ccf1c01c56aa212c63f943337b920103c3a1",
        "s": "0x46133ab89d90a3ae2a3a7680d2a27e30fa015c0c4979931164c51b52b27758a"
      },
      "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
      "collateralPosition": "4272448241247734333"
    }
  },
  "stopLoss": {
    "triggerPrice": "950",
    "triggerPriceType": "LAST",
    "price": "900",
    "priceType": "LIMIT",
    "settlement": {
      "signature": {
        "r": "0x5033ad23fe851d16ceec5dd99f2f0c9585c5abec3f09ec89a32a961536ba55",
        "s": "0x1234ee151a8b5c68efb4adaa2eaf1dcc4a5107d4446274a69389ef8abd2dcf"
      },
      "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f",
      "collateralPosition": "4272448241247734333"
    }
  },
  "builderFee": "0.0001",
  "builderId": 2017
}
Body Parameters
Parameter	Required	Type	Description
id	yes	string	Order ID assigned by user.
market	yes	string	Market name.
type	yes	string	Order type. Can be limit, market, conditional or tpsl.
side	yes	string	Order side. Can be buy or sell.
qty	yes	string	Order size in base asset.
price	yes	string	Worst accepted price in collateral asset. Note that price is optional for a tpsl type position.
reduceOnly	no	boolean	Whether the order should be Reduce-only.
postOnly	no	boolean	Whether the order should be Post-only.
timeInForce	yes	string	Time-in-force setting. Can be GTT (Good till time) or IOC (Immediate or cancel). This parameter will default to GTT.
expiryEpochMillis	yes	number	Timestamp (in epoch milliseconds) when the order expires if not filled. Cannot exceed 3 months from the order creation time.
fee	yes	string	Highest accepted fee for the trade, expressed in decimal format (e.g., 0.1 for 10%). Use the maker fee for Post-only orders and the taker fee for all other orders.
cancelId	no	string	External ID of the order that this order is replacing.
settlement	yes	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
nonce	yes	string	Nonce is part of the settlement and must be a number ≥1 and ≤2^31. Please make sure to check the Python SDK reference implementation.
selfTradeProtectionLevel	yes	string	Level of self trade protection. Can be DISABLED, ACCOUNT(default) and CLIENT.
trigger.triggerPrice	no	string	Price threshold for triggering a conditional order.
trigger.triggerPriceType	no	string	Type of price used for the order triggering. Can be last, mark or index.
trigger.triggerPriceDirection	no	string	Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be up (the order will be triggered when the price reaches or surpasses the set trigger price) or down (the order will be triggered when the price reaches or drops below the set trigger price).
trigger.executionPriceType	no	string	Type of price used for the order execution. Can be limit or market.
tpSlType	no	string	TPSL type determining TPSL order size. Can be order or position.
takeProfit.triggerPrice	no	string	Take Profit Trigger price.
takeProfit.triggerPriceType	no	string	Type of price used for the Take Profit order triggering. Can be last, mid (to be added soon), mark or index.
takeProfit.price	no	string	Take Profit order price.
takeProfit.priceType	no	string	Indicates whether the Take profit order should be executed as market or limit order.
takeProfit.settlement	no	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
triggerPrice	no	string	Stop loss Trigger price.
stopLoss.triggerPriceType	no	string	Type of price used for the Stop Loss order triggering. Can be last, mid (to be added soon), mark or index.
stopLoss.price	no	string	Stop loss order price.
stopLoss.priceType	no	string	Indicates whether the Stop loss order should be executed as market or limit order.
stopLoss.settlement	no	object	StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.
builderFee	no	number	Amount that user will pay builder (an alternative ui maker) for the trade. Expressed in decimal format (e.g., 0.1 for 10%)
builderId	no	number	Builder client id that will receive the builderFee
Response example:

{
  "status": "OK",
  "data": {
    "id": 1791389621914243072,
    "externalId": "31097979600959341921260192820644698907062844065707793749567497227004358262"
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.id	yes	number	Order ID assigned by Extended.
data.externalId	yes	string	Order ID assigned by user.
Cancel order by ID
HTTP Request
DELETE /api/v1/user/order/{id}

Cancel an individual order by Extended ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation.

URL Parameters
Parameter	Required	Type	Description
id	yes	number	Order to be canceled, ID assigned by Extended.
Cancel order by external id
HTTP Request
DELETE /api/v1/user/order?externalId={externalId}

Cancel an individual order by user ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation.

URL Parameters
Parameter	Required	Type	Description
externalId	yes	string	Order to be canceled, Order ID assigned by user.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Mass Cancel
HTTP Request
POST /api/v1/user/order/massCancel

Mass Cancel enables the cancellation of multiple orders by ID, by specific market, or for all orders within an account.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation request.

Although all parameters are optional, at least one must be specified.

Request example:

{
  "orderIds": [
    1,
    2
  ],
  "externalOrderIds": [
    "ExtId-1",
    "ExtId-2"
  ],
  "markets": [
    "BTC-USD",
    "ETH-USD"
  ],
  "cancelAll": true
}
Body Parameters
Parameter	Required	Type	Description
markets	no	string[]	Market names where all orders should be cancelled.
cancelAll	no	boolean	Indicates whether all open orders for the account should be cancelled.
orderIds	no	number[]	Cancel by Extended IDs.
externalOrderIds	no	string[]	Cancel by external IDs.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Mass auto-cancel (dead man's switch)
HTTP Request
POST /api/v1/user/deadmanswitch?countdownTime={countdownTime}

The dead man's switch automatically cancels all open orders for the account at the end of the specified countdown if no Mass Auto-Cancel request is received within this timeframe. Setting the time to zero will remove any outstanding scheduled cancellations.

Positions and account status are not affected by the dead man's switch.

Request Parameters
Parameter	Required	Type	Description
countdownTime	yes	number	Time till Scheduled Mass Cancel (in seconds), should be non-negative. Setting the time to zero will remove any outstanding scheduled cancellations.
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
Bridge Config
HTTP Request
GET /api/v1/user/bridge/config

Response example:

{
  "chains": [
    {
      "chain":"ARB",
      "contractAddress":"0x10417734001162Ea139e8b044DFe28DbB8B28ad0"
    }
  ]
}
Returns EVM chains supported for deposits and withdrawals for EVM-wallets.

Response
Parameter	Required	Type	Description
chains	yes	object[]	List of Chain objects.
Chain object
Parameter	Required	Type	Description
chain	yes	string	Chain name.
contractAddress	yes	string	Bridge contract address for the chain.
Get bridge quote
HTTP Request
GET /api/v1/user/bridge/quote?chainIn=ARB&chainOut=STRK&amount=100

Response example:

{
  "id": "68aaa",
  "fee": "0.1"
}
Gets a quote for an EVM deposit/withdrawal.

Request Parameters
Parameter	Required	Type	Description
chainIn	yes	string	Chain where bridge will accept funds. For deposit set EVM chain, for withdrawal STRK.
chainOut	yes	string	Chain where bridge will send funds. For deposit set STRK chain, for withdrawal EVM.
amount	yes	number	Amount in USD that user should pay to bridge contract on chainIn.
Response
Parameter	Required	Type	Description
id	yes	string	Quote ID.
fee	yes	decimal	Bridge fee.
Commit quote
HTTP Request
POST /api/v1/user/bridge/quote?id=68aaa

Commits a quote for EVM deposit/withdrawal.

If a quote is deemed acceptable it needs to be committed before the bridge can be executed. This tells our bridge provider Rhino.fi to start watching for a transaction on the origin chain that deposits the required funds into the bridge contract. Rhino.fi will then issue a commitment ID to be used when sending the funds to be bridged.

Deposits
For EVM wallets, we support deposits and withdrawals on six major chains via the Rhino.fi bridge—Arbitrum, Ethereum, Base, Binance Smart Chain, Avalanche, and Polygon—currently. Please refer to the documentation for transaction limits and estimated processing times.

For Starknet wallets, we support USDC deposits via on-chain interaction and through the User Interface. To deposit on-chain, invoke the Starknet contract at 0x062da0780fae50d68cecaa5a051606dc21217ba290969b302db4dd99d2e9b470.

Extended doesn't charge fees on deposits or withdrawals, but for EVM chains, bridge fees may apply. All deposits and withdrawals are subject to gas fees.

EVM deposit requires bridging, please read Bridge section before proceeding.

EVM deposit consists of four steps:

1) User retrieves supported chains and bridge contracts via GET /bridge/config.

2) User requests a quote via GET /bridge/quote.

3) If the user accepts the bridge fee, they confirm the quote using POST /bridge/quote.

4) Finally, the user calls the depositWithId function on the source chain. See the rhino.fi docs for more details.

 Incorrectly sent funds are non-recoverable by Extended. Follow the execution order exactly as described. When calling depositWithId, use the exact same ID, amount, and token address. Test with a small amount first to ensure everything works correctly.
Withdrawals
For EVM wallets, we support deposits and withdrawals on six major chains—Arbitrum, Ethereum, Base, Binance Smart Chain, Avalanche, and Polygon. Please refer to the documentation for transaction limits and estimated processing times.

For Starknet wallets, we support withdrawals via the User Interface and API, as described below.

Note that Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirements).

Extended doesn't charge fees on deposits or withdrawals, but for EVM chains, bridge fees may apply. All deposits and withdrawals are subject to gas fees. Withdrawals are only permitted to wallets that are linked to the authorised account.

EVM withdrawals
EVM withdrawals involve bridging, please read the Bridge section first before proceeding. The withdrawal process consists of four steps:

1) User retrieves supported chains and bridge contracts via GET /bridge/config. 2) User requests a quote with GET /bridge/quote. 3) If the user accepts the bridge fee, they confirm the quote using POST /bridge/quote. 4) Finally, the user submits a Starknet withdrawal with the quoteId to the bridgeStarknetAddress associated with their account. See Account for details.

Starknet withdrawals
To initiate a Starknet withdrawal, send a "Create Withdrawal" request as described below or use the corresponding SDK method, signed with a private L2 key. Starknet withdrawals are only available for accounts created with a Starknet wallet.

HTTP Request
POST /api/v1/user/withdrawal

Request
Request example:

{
  "accountId":"100006",
  "amount":"2",
  "chainId":"STRK",
  "asset":"USD",
  "settlement":{
    "recipient":"0x00f7016a6f1281925ef584bdc1fd2276b2fef02d0741acce215bc512857030dc",
    "positionId":300006,
    "collateralId":"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "amount":"2000000",
    "expiration":{
      "seconds":1755690249
    },
    "salt":93763903,
    "signature":{
      "r":"1110b06f591a5495b07c1e6ccc9478cbf2301af3a207c082be4c63fde19dd0b",
      "s":"cc93ea79708889869c94c95efdb005f0f15c16dec94a93e7efda33eaf7bcbd"
    }
  }
}
Body Parameters
Parameter	Required	Type	Description
chainId	yes	string	For starknet withdrawals, the type should be STRK.
accountId	yes	number	Source account ID.
amount	yes	string	Withdrawal amount, absolute value in collateral asset.
asset	yes	string	Collateral asset name.
settlement	yes	object	Withdrawal object StarkKey signature. For details, please refer to the Python SDK.
quoteId	yes	object	Bridge quote id for bridged withdrawal.
Response example:

{
  "status": "OK",
  "data": 1820796462590083072
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data	yes	number	Withdrawal ID, assigned by Extended.
Create transfer
HTTP Request
POST /api/v1/user/transfer

Create a transfer between sub-accounts associated with the same wallet.

Request
Request example:

{
  "fromAccount": 3004,
  "toAccount": 7349,
  "amount": "1000",
  "transferredAsset": "USD",
  "settlement": {
    "amount": 1000000000,
    "assetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
    "expirationTimestamp": 478932,
    "nonce": 758978120,
    "receiverPositionId": 104350,
    "receiverPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
    "senderPositionId": 100005,
    "senderPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
    "signature": {
      "r": "6be1839e2ca76484a1a0fcaca9cbbe3792a23656d42ecee306c31e65aadb877",
      "s": "7b8f81258e16f0f90cd12f02e81427e54b4ebf7646e9b14b57f74c2cb44bff6"
    }
  }
}
Body Parameters
Parameter	Required	Type	Description
fromAccount	yes	number	Source account ID.
toAccount	yes	number	Destination account ID.
amount	yes	string	Transfer amount, absolute value in collateral asset.
transferredAsset	yes	string	Collateral asset name.
settlement	yes	object	Transfer object StarkKey signature (including nonce and transfer parameters). For details, please refer to the Python SDK.
Response example:

{
  "status": "OK",
  "data": {
    "validSignature": true,
    "id": 1820778187672010752
  }
}
Response
Parameter	Required	Type	Description
status	yes	string	Can be OK or ERROR.
data.validSignature	yes	boolean	Indicates whether the signature is valid.
data.id	yes	number	Transfer ID assigned by Extended.
Referrals
Extended offers a referral program. The following API endpoints allow you to issue referral codes and retrieve your referral statistics.

Glossary
Referral – A client who was invited by another client.
Referee – A client who invited another client.
Affiliate – A client who successfully applied to the Affiliate Program.
Subaffiliate – A referred user who is also an affiliate, and was referred by an affiliate.
Referred volume – The trading volume of all clients referred by the user (non-transitive).
Rebate – The reward paid to the referee of affiliate, derived from the trading fees of his referrals.
Rebate rate – The percentage of fees paid by the referral that the referee or affiliate receive.
Rebate = rebate_rate * (trading_fees - rewards_to_other_programs)
Referral schedule – A set of rules (tiers) that determine the rebate rate based on the L30D referred volume.
Shared objects
Tier object
Example:

{
  "totalVolume": "0",
  "rebateRate": "0.1",
  "volumeLimitPerReferral": "0"
}
Tier is the lowest-level object that defines the rules of the referral program.

Parameter	Required	Type	Description
totalVolume	yes	number	Minimum Last 30D referred volume for the rebate rate tier.
rebateRate	yes	number	The rebate rate.
volumeLimitPerReferral	yes	number	Maximum trading volume eligible for a fee discount per referral.
Refferal schedule object
Example:

{
  "tiers": [
    {
      "totalVolume": "0",
      "rebateRate": "0.1",
      "volumeLimitPerReferral": "0"
    }
  ]
}
Contains a list of Tiers objects.

Parameter	Required	Type	Description
tiers	yes	object[]	List of Tiers objects.
Refferal group object
Example:

{
  "id": 1,
  "schedule": {
    "tiers": [
      {
        "totalVolume": "0",
        "rebateRate": "0.1",
        "volumeLimitPerReferral": "0"
      }
    ]
  },
  "subaffiliateRate": "0.1"
}
Contains the Referral schedule object and the sub-affiliate rebate rate. Each affiliate can have two types of Referral groups — the Main group and the Protection-period group.

Parameter	Required	Type	Description
id	yes	number	Group ID.
schedule	yes	object	Refferal schedule object.
subaffiliateRate	yes	number	Rebate rate that referee gains from their subaffiliate referral rebates.
Affiliate object
Example:

{
  "clientId": 42,
  "name": "ABC",
  "onboarded": 1746784655000,
  "mainGroup": {
    "id": 1,
    "schedule": {
      "tiers": [
        {
          "totalVolume": "0",
          "rebateRate": "0.1",
          "volumeLimitPerReferral": "0"
        }
      ]
    },
    "subaffiliateRate": "0"
  },
  "d30ReferredVolume": "2000"
}
Parameter	Required	Type	Description
clientId	yes	number	Affiliate's client ID on Extended.
name	yes	string	Affiliate's name on Extended.
onboarded	yes	number	Affiliate's onboarding timestamp (Unix).
mainGroup	yes	number	Affiliate's Main Refferal group object.
d30ReferredVolume	yes	number	Last 30D volume of users referred by the Affiliate.
protectionPeriodGroup	no	number	Affiliate's Refferal group during protection period.
protectionPeriodUntil	no	number	End of protection period (Unix timestamp).
Period
Enum that specifies the time period for fetching data. Can be DAY, WEEK, MONTH, YEAR, ALL.

Granularity
Enum that specifies the time period for fetching data. Can be DAY, WEEK, MONTH.

Get affiliate data
GET /api/v1/user/affiliate

Response example:

{
  "clientId": 42,
  "name": "ABC",
  "onboarded": 1746784655000,
  "mainGroup": {
    "id": 1,
    "schedule": {
      "tiers": [
        {
          "totalVolume": "0",
          "rebateRate": "0.1",
          "volumeLimitPerReferral": "0"
        }
      ]
    },
    "subaffiliateRate": "0"
  },
  "d30ReferredVolume": "2000"
}
If the user is an affiliate, returns their affiliate data; otherwise, returns a 404.

Response
See Affiliate object in the Shared objects section of Referrals documentation.

Get referral status
GET /api/v1/user/referrals/status

Response example:

{
  "active": true, 
  "limit": 10000,
  "tradedVolume": 100
}
Returns the user’s referral program status.

Response
Parameter	Required	Type	Description
active	yes	boolean	Program is active for the user - user can issue referral codes. Can be true or false.
limit	yes	number	Trading volume required to activate the referral program.
tradedVolume	yes	number	User's current traded volume.
Get referral links
GET /api/v1/user/referrals/links

Response example:

[
  {
    "id": "ABC",
    "issuedBy": 42,
    "issuedAt": 1746785907329,
    "label": "ABC",
    "isDefault": true,
    "hiddenAtUi": false,
    "overallRebates": "50"
  }
]
Returns referral links issued by the user.

Response
Parameter	Required	Type	Description
id	yes	string	Link ID.
issuedBy	yes	number	Referral client ID.
issuedAt	yes	number	Link issue timestamp (Unix).
label	yes	string	Label added by user.
isDefault	yes	boolean	Link set as default for the client. Can be true or false.
hiddenAtUi	yes	boolean	Link is visible for the client. Can be true or false.
overallRebates	yes	number	Total rebates for the link.
Get referral dashboard
GET /api/v1/user/referrals/dashboard?period={PERIOD}

Response example:

{
  "referralLinkToDirectKeyMetrics": {
    "ABC": {
      "rebateEarned": {
        "current": "200",
        "previous": "100"
      },
      "totalFeesPaid": {
        "current": "2000",
        "previous": "1000"
      },
      "tradingVolume": {
        "current": "20000",
        "previous": "10000"
      },
      "activeTraders": {
        "current": 200,
        "previous": 100
      }
    }
  },
  "subaffiliateToKeyMetrics": {
    "2": {
      "rebateEarned": {
        "current": "200",
        "previous": "100"
      },
      "subaffiliateEarnings": {
        "current": "2500",
        "previous": "1250"
      }
    }
  },
  "activeSubaffiliates": {
    "current": 1,
    "previous": 0
  },
  "affiliates": [
    {
      "clientId": 2,
      "name": "RUSLAN",
      "onboarded": 1746792229516,
      "mainGroup": {
        "id": 1,
        "schedule": {
          "tiers": [
            {
              "totalVolume": "0",
              "rebateRate": "0.1",
              "volumeLimitPerReferral": "0"
            }
          ]
        },
        "subaffiliateRate": "0"
      }
    }
  ],
  "users": [
    {
      "firstTradedOn": 1746792228516,
      "wallet": "0x42...a8a91",
      "rebate": "100",
      "tradedVolume": "10000",
      "totalFees": "1000"
    }
  ],
  "daily": [
    {
      "date": "2025-05-09",
      "subaffiliates": [
        {
          "id": 2,
          "rebate": "5",
          "activeUsers": 2,
          "referredTradingVolume": "100",
          "earnings": "10"
        }
      ],
      "links": [
        {
          "link": "ABC",
          "rebate": "10",
          "activeUsers": 4,
          "referredTradingVolume": "200",
          "referredFees": "20",
          "referredL30Volume": "2000"
        }
      ]
    },
    {
      "date": "2025-05-08",
      "subaffiliates": [],
      "links": []
    }
  ],
  "weekly": [
    {
      "date": "2025-05-09",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-05-02",
      "subaffiliates": [],
      "links": []
    }
  ],
  "monthly": [
    {
      "date": "2025-05-09",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-04-11",
      "subaffiliates": [],
      "links": []
    },
    {
      "date": "2025-04-13",
      "subaffiliates": [],
      "links": []
    }
  ]
}
Returns referral program statistic for the selected period.

Request parameters
Parameter	Required	Type	Description
period	yes	string	Requested period.
Response
The Affiliate object is described in the Shared objects section of Referrals documentation. The descriptions of other objects returned by this endpoint are provided below.

Parameter	Required	Type	Description
referralLinkToDirectKeyMetrics	yes	object	Metrics aggregated by referral codes (Map).
subaffiliateToKeyMetrics	yes	object	Metrics aggregated by subaffiliates (Map).
activeSubaffiliates	yes	number	Number of active subaffiliates.
affiliates	yes	object[]	List of Affiliate objects for subaffiliates active during the period.
users	yes	object[]	List of UserStat objects for users active during the period.
daily	yes	object[]	List of AffiliateStat objects for the period with 1 day granularity.
weekly	yes	object[]	List of AffiliateStat objects for the period with 1 week granularity.
monthly	yes	object[]	List of AffiliateStat objects for the period with 1 month granularity.
CurrentToPrevious<T>
Parameter	Required	Type	Description
current	yes	object	<T> data for current period.
previous	yes	object	<T> data for previous period.
DirectKeyMetrics
Parameter	Required	Type	Description
rebateEarned	yes	object	CurrentToPrevious<Number>. Rebates earned during the period.
totalFeesPaid	yes	object	CurrentToPrevious<Number>. Total amount of fees paid by referrals during the period.
tradingVolume	yes	object	CurrentToPrevious<Number>. Referred volume during the period.
activeTraders	yes	object	CurrentToPrevious<Number>. Number of active traders among referrals during the period.
SubaffiliateKeyMetrics
Parameter	Required	Type	Description
rebateEarned	yes	object	CurrentToPrevious<Number>. Rebates earned during the period.
subaffiliateEarnings	yes	object	CurrentToPrevious<Number>. Total rebates earned by subaffiliates during the period.
UserStat
Parameter	Required	Type	Description
firstTradedOn	no	number	Referral's first trade timestamp (Unix).
wallet	yes	string	Masked referral's wallet.
referredBy	no	number	User's referee.
referralLink	no	string	Referral link code used by the referral.
rebate	yes	number	Rebate.
tradedVolume	yes	number	Referral's traded volume during the period.
totalFees	yes	number	Total fees paid by the referral during the period.
AffiliateStat
Parameter	Required	Type	Description
date	yes	string	Last date of the period.
subaffiliates	yes	object[]	List of SubaffiliateStat objects for the period grouped by subaffiliates.
links	yes	object[]	List of LinkStat objects for the period grouped by links.
SubaffiliateStat
Parameter	Required	Type	Description
id	yes	number	Subaffiliate's client ID on Extended.
rebate	yes	number	Rebate earned by Subaffiliate (rebate from referrals of his referrals).
activeUsers	yes	number	Number of active traders among Subaffiliate's referrals.
referredTradingVolume	yes	number	Subaffiliate's referred volume.
earnings	yes	number	Subaffiliate's rebate.
LinkStat
Parameter	Required	Type	Description
link	yes	string	Referral link code.
rebate	yes	number	Rebate earned through the link.
activeUsers	yes	number	Count of active referrals invited through the link.
referredTradingVolume	yes	number	Volume referred through the link.
referredFees	yes	number	Total fees paid by referrals invited through the link.
referredL30Volume	yes	number	Last 30D volume referred through the link.
Use referral link
POST /api/v1/user/referrals/use

Request example: json { "code": "ABC" }

Activate referral link for the authenticated client.

Create referral link code
POST /api/v1/user/referrals

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Create referral link code.

Update referral link code
PUT /api/v1/user/referrals

Update referral link code.

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Points
Points-related endpoints let users view their earned points and leaderboard ranking.

Get Earned Points
HTTP Request
GET /api/v1/user/rewards/earned

Returns points earned by the authenticated client across all seasons and epochs.

Authentication
This endpoint requires authentication.

Response example: json { "status": "OK", "data": [ { "seasonId": 1, "epochRewards": [ { "epochId": 1, "startDate": "2023-01-01T00:00:00Z", "endDate": "2023-01-31T23:59:59Z", "pointsReward": "50.25" } ] } ] }

Response
Parameter	Type	Description
data[].seasonId	number	The ID of the reward season.
data[].epochRewards	array	List of rewards earned in each epoch.
data[].epochRewards.epochId	number	The ID of the epoch.
data[].epochRewards.startDate	string	The start date of the epoch (ISO format).
data[].epochRewards.endDate	string	The end date of the epoch (ISO format).
data[].epochRewards.pointsReward	string	The number of points earned in the epoch.
Get points leaderboard stats
HTTP Request
GET /api/v1/user/rewards/leaderboard/stats

Returns the leaderboard statistics for the authenticated client, including total points, leaderboard rank, and points league levels.

Authentication
This endpoint requires authentication.

Response example: json { "status": "OK", "data": { "totalPoints": "1250.75", "rank": 42, "tradingRewardLeague": "QUEEN", "liquidityRewardLeague": "PAWN", "referralRewardLeague": "KING" } }

Response
Parameter	Type	Description
totalPoints	string	The total number of points earned.
rank	number	The client's rank on the leaderboard.
tradingRewardLeague	string	The client's league for trading points.
liquidityRewardLeague	string	The client's league for liquidity points.
referralRewardLeague	string	The client's league for referral points.
Points league levels
The following table describes the points-league levels for tradingRewardLeague, liquidityRewardLeague, and referralRewardLeague.

Value	Description
KING	King league - highest tier.
QUEEN	Queen league - second-highest tier.
ROOK	Rook league - advanced tier.
KNIGHT	Knight league - intermediate tier.
PAWN	Pawn league - entry-level tier.
Get account equity history
HTTP Request
GET /api/v1/portfolio/charts/equities?accountId={accountId}&interval={interval}

Returns equity history for the chosen accounts per date. To request data for several accounts, use the format GET /api/v1/portfolio/charts/equities?accountId=1000&accountId=10001&interval=WEEK.

Authentication
This endpoint requires authentication.

Request
Query Parameters
Parameter	Required	Type	Description
accountId	yes	number	Id of user account.
interval	yes	string	Time interval. Can be DAY, WEEK, MONTH, YEAR or ALL.
Response example:

{
  "status": "OK",
  "data": [
    {
      "date": "2025-08-10",
      "value": "700"
    },
    {
      "date": "2025-08-11",
      "value": "1400"
    }
  ]
}
Get account PnL history
HTTP Request
GET /api/v1/portfolio/charts/pnl?accountId={accountId}&interval={interval}&pnlType={pnlType}

Returns total or realised Pnl history for the chosen accounts per date. To request data for several accounts, use the format GET /api/v1/portfolio/charts/pnl?accountId=1000&accountId=10001&interval=WEEK&pnlType=TOTAL_PNL.

Authentication
This endpoint requires authentication.

Request
Query Parameters
Parameter	Required	Type	Description
accountId	yes	number	Account ID.
interval	yes	string	Time interval. Can be DAY, WEEK, MONTH, YEAR or ALL.
pnlType	yes	string	Pnl type. Can be TOTAL_PNL or REALISED_PNL.
Response example:

                {
  "status": "OK",
  "data": [
    {
      "date": "2025-08-10",
      "value": "700"
    },
    {
      "date": "2025-08-11",
      "value": "1400"
    }
  ]
}
Get Vault performance
HTTP Request
GET /api/v1/vault/public/performance?interval={interval}

Returns performance of vault, which includes data as total pnl, sharpe ratio, profit factor, etc.

Authentication
This endpoint does not require authentication.

Request
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	Time interval. Can be WEEK, MONTH, YEAR or ALL.
Response example:

{
  "status": "OK",
  "data": {
    "totalPnl": "1156",
    "aprPercentage": "17.5495",
    "profitFactor": "1.5887",
    "winRate": "0.2881",
    "maxDrawdown": "0.2182",
    "tradingVolume": "6000",
    "sharpeRatio": "252.96",
    "aprBreakdown": {
      "baseApr": "10.6551",
      "maxExtraApr": "6.8944"
    }
  }
}
Get Vault summary
HTTP Request
GET /api/v1/vault/public/summary

Returns a summary of the vault for a whole period.

Authentication
This endpoint does not require authentication.

Response example:

{
  "status": "OK",
  "data": {
    "equity": "11000",
    "walletBalance": "2000",
    "lastMonthApr": "422.7917",
    "exposure": "10000",
    "numberOfDepositors": 3,
    "ageDays": 227,
    "profitShare": "0",
    "aprBreakdown": {
      "baseApr": "416.1",
      "maxExtraApr": "6.6917"
    }
  }
}
Public WebSocket streams
Extended offers a WebSocket API for streaming updates.

Connect to the WebSocket streams using wss://api.starknet.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from the client, it will respond with a pong if one is received.

Order book stream
HTTP Request
GET /stream.extended.exchange/v1/orderbooks/{market}

Subscribe to the orderbooks stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

In the current version we support the following depth specifications:

Full orderbook. Push frequency: 100ms. The initial response from the stream will be a snapshot of the order book. Subsequent snapshot updates will occur every minute, while updates between snapshots are delivered in delta format, reflecting only changes since the last update. Best Bid & Ask updates are always provided as snapshots.

Best bid & ask. Push frequency: 10ms. To subscribe for Best bid & ask use GET /stream.extended.exchange/v1/orderbooks/{market}?depth=1. Best bid & ask updates are always snapshots.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Query Parameters
Parameter	Required	Type	Description
depth	no	string	Specify '1' to receive updates for best bid & ask only.
Response example:

{
  "ts": 1701563440000,
  "type": "SNAPSHOT",
  "data": {
    "m": "BTC-USD",
    "b": [
      {
        "p": "25670",
        "q": "0.1",
        "c": "0.3"
      }
    ],
    "a": [
      {
        "p": "25770",
        "q": "0.1",
        "c": "0.2"
      }
    ]
  },
  "seq": 1
}
Response
Parameter	Type	Description
type	string	Type of message. Can be SNAPSHOT or DELTA.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data.m	string	Market name.
data.t	string	Type of message. Can be SNAPSHOT or DELTA.
data.b	object[]	List of bid orders. For a snapshot, bids are sorted by price in descending order.
data.b[].p	string	Bid price.
data.b[].q	string	Bid size. For a snapshot, this represents the absolute size; for a delta, the change in size.
data.b[].c	string	Bid size. For a snapshot and delta, this represents the absolute size.
data.a	object[]	List of ask orders. For a snapshot, asks are sorted by price in ascending order.
data.a[].p	string	Ask price.
data.a[].q	string	Ask size. For a snapshot, this represents the absolute size; for a delta, the change in size.
data.a[].c	string	Ask size. For a snapshot and delta, this represents the absolute size.
seq	number	Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.
Trades stream
HTTP Request
GET /stream.extended.exchange/v1/publicTrades/{market}

Subscribe to the trades stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Historical trade data is currently available only to authorized accounts via the private REST API.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "ts": 1701563440000,
  "data": [
    {
      "m": "BTC-USD",
      "S": "BUY",
      "tT": "TRADE",
      "T": 1701563440000,
      "p": "25670",
      "q": "0.1",
      "i": 25124
    }
  ],
  "seq": 2
}
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].m	string	Market name.
data[].S	string	Side of taker trades. Can be BUY or SELL.
data[].tT	string	Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.
data[].T	number	Timestamp (in epoch milliseconds) when the trade happened.
data[].p	string	Trade price.
data[].q	string	Trade quantity in base asset.
data[].i	number	Trade ID.
seq	number	Monotonic sequence: Since there are no deltas, clients can skip trades that arrive out of sequence.
Funding rates stream
HTTP Request
GET /stream.extended.exchange/v1/funding/{market}

Subscribe to the funding rates stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

For historical funding rates data, use the Get funding rates history endpoint.

While the funding rate is calculated every minute, it is applied only once per hour. The records include only those funding rates that were used for funding fee payments.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "ts": 1701563440000,
  "data": {
      "m": "BTC-USD",
      "T": 1701563440000,
      "f": "0.001"
  },
  "seq": 2
}
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].m	string	Market name.
data[].T	number	Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.
data[].f	string	Funding rates that were applied for funding fee payments.
seq	number	Monotonic sequence: Since there are no deltas, clients can skip funding rates that arrive out of sequence.
Candles stream
HTTP Request
GET /stream.extended.exchange/v1/candles/{market}/{candleType}?interval={interval}

Subscribe to the candles stream for a specific market.

The interval parameter should be specified in the ISO 8601 duration format. Available intervals include: P30D (Calendar month), P7D (Calendar week), PT24H, PT12H, PT8H, PT4H, PT2H, PT1H, PT30M, PT15M, PT5M and PT1M.

Trades price response example:

{
  "ts": 1695738675123,
  "data": [ 
    {
      "T": 1695738674000,
      "o": "1000.0000",
      "l": "800.0000",
      "h": "2400.0000",
      "c": "2100.0000",
      "v": "10.0000"
    }
  ],
  "seq": 1
}
Mark and Index price response example:

{
  "ts": 1695738675123,
  "data": [
    {
      "T": 1695738674000,
      "o": "1000.0000",
      "l": "800.0000",
      "h": "2400.0000",
      "c": "2100.0000"
    }
  ],
  "seq": 1
}
Available price types include:

Last price: GET /stream.extended.exchange/v1/candles/{market}/trades?interval=PT1M

Mark price: GET /stream.extended.exchange/v1/candles/{market}/mark-prices?interval=PT1M

Index price: GET /stream.extended.exchange/v1/candles/{market}/index-prices?interval=PT1M

Push frequency: 1-10s.

URL Parameters
Parameter	Required	Type	Description
market	yes	string	Select an individual market.
candleType	yes	string	Price type. Can be trades, mark-prices or index-prices.
Query Parameters
Parameter	Required	Type	Description
interval	yes	string	Duration of candle (duration in ISO 8601).
Response
Parameter	Type	Description
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
data[].T	number	Starting timestamp (in epoch milliseconds) of the candle.
data[].o	string	Open price.
data[].c	string	Close price.
data[].h	string	Highest price.
data[].l	string	Lowest price.
data[].v	string	Trading volume (only for trade candles).
seq	number	Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.
Mark price stream
HTTP Request
GET /stream.extended.exchange/v1/prices/mark/{market}

Subscribe to the mark price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Mark prices are used to calculate unrealized P&L and serve as the reference for liquidations. The stream provides real-time updates whenever a mark price changes.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "type": "MP",
  "data": {
    "m": "BTC-USD",
    "p": "25670",
    "ts": 1701563440000
  },
  "ts": 1701563440000,
  "seq": 1,
  "sourceEventId": null
}
Response
Parameter	Type	Description
type	string	Type identifier for mark price stream ("MP").
data.m	string	Market name.
data.p	string	Mark price value.
data.ts	number	Timestamp (in epoch milliseconds) when the price was calculated.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
seq	number	Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.
sourceEventId	number	ID of the source event that triggered this update (null for regular updates).
Index price stream
HTTP Request
GET /stream.extended.exchange/v1/prices/index/{market}

Subscribe to the index price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

An index price is a composite spot price sourced from multiple external providers. It is used as the reference for funding-rate calculations.

URL Parameters
Parameter	Required	Type	Description
market	no	string	Select an individual market. If not specified, the subscription includes all markets.
Response example:

{
  "type": "IP",
  "data": {
    "m": "BTC-USD",
    "p": "25680",
    "ts": 1701563440000
  },
  "ts": 1701563440000,
  "seq": 1,
  "sourceEventId": null
}
Response
Parameter	Type	Description
type	string	Type identifier for index price stream ("IP").
data.m	string	Market name.
data.p	string	Index price value.
data.ts	number	Timestamp (in epoch milliseconds) when the price was calculated.
ts	number	Timestamp (in epoch milliseconds) when the system generated the data.
seq	number	Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.
sourceEventId	number	ID of the source event that triggered this update (null for regular updates).
Private WebSocket streams
Connect to the WebSocket streams using ws://api.starknet.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from clients, it will respond with a pong if it receives one.

Extended employs a simplified authentication scheme for API access. Authenticate by using your API key, which should be included in an HTTP header as follows: X-Api-Key: <API_KEY_FROM_API_MANAGEMENT_PAGE_OF_UI>.

Account updates stream
HTTP Request
GET /stream.extended.exchange/v1/account

Orders updates response example:

{
  "type": "ORDER",
  "data": {
    "orders": [
      {
        "id": 1791181340771614723,
        "accountId": 1791181340771614721,
        "externalId": "-1771812132822291885",
        "market": "BTC-USD",
        "type": "LIMIT",
        "side": "BUY",
        "status": "NEW",
        "price": "12400.000000",
        "averagePrice": "13140.000000",
        "qty": "10.000000",
        "filledQty": "3.513000",
        "payedFee": "0.513000",
        "trigger": {
          "triggerPrice": "1220.00000",
          "triggerPriceType": "LAST",
          "direction": "UP",
          "executionPriceType": "LIMIT"
        },
        "tpSlType": "ORDER",
        "takeProfit": {
          "triggerPrice": "1.00000",
          "triggerPriceType": "LAST",
          "price": "1.00000",
          "priceType": "LIMIT"
        },
        "stopLoss": {
          "triggerPrice": "1.00000",
          "triggerPriceType": "LAST",
          "price": "1.00000",
          "priceType": "LIMIT"
        },
        "reduceOnly": true,
        "postOnly": false,
        "createdTime": 1715885888571,
        "updatedTime": 1715885888571,
        "expireTime": 1715885888571
      }
    ]
  },
  "ts": 1715885884837,
  "seq": 1
}
Trades updates response example:

{
  "type": "TRADE",
  "data": {
    "trades": [
      {
        "id": 1784963886257016832,
        "accountId": 3017,
        "market": "BTC-USD",
        "orderId": 9223372036854775808,
        "externalOrderId": "ext-1",
        "side": "BUY",
        "price": "58853.4000000000000000",
        "qty": "0.0900000000000000",
        "value": "5296.8060000000000000",
        "fee": "0.0000000000000000",
        "tradeType": "DELEVERAGE",
        "createdTime": 1701563440000,
        "isTaker": true
      }
    ]
  },
  "ts": 1715885884837,
  "seq": 1
}
Account balance updates response example:

{
  "type": "BALANCE",
  "data": {
    "balance": {
      "collateralName": "BTC",
      "balance": "100.000000",
      "equity": "20.000000",
      "availableForTrade": "3.000000",
      "availableForWithdrawal": "4.000000",
      "unrealisedPnl": "1.000000",
      "initialMargin": "0.140000",
      "marginRatio": "1.500000",
      "updatedTime": 1699976104901,
      "exposure": "12751.859629",
      "leverage": "1275.1860"
    }
  },
  "ts": 1715885952304,
  "seq": 1
}
Positions updates response example:

{
  "type": "POSITION",
  "data": {
    "positions": [
      {
        "id": 1791183357858545669,
        "accountId": 1791183357858545665,
        "market": "BTC-USD",
        "side": "SHORT",
        "leverage": "5.0",
        "size": "0.3",
        "value": "12751.8596295830",
        "openPrice": "42508.00",
        "markPrice": "42506.1987652769",
        "liquidationPrice": "75816.37",
        "margin": "637.59",
        "unrealisedPnl": "100.000000",
        "realisedPnl": "200.000000",
        "tpTriggerPrice": "1600.0000",
        "tpLimitPrice": "1500.0000",
        "slTriggerPrice": "1300.0000",
        "slLimitPrice": "1250.0000",
        "adl": 1,
        "createdAt": 1715886365748,
        "updatedAt": 1715886365748
      }
    ]
  },
  "ts": 1715886365748,
  "seq": 1
}
Subscribe to the account updates stream.

The initial responses will include comprehensive information about the account, including balance, open positions, and open orders, i.e. everything from GET /v1/user/balance, GET /v1/user/positions, GET /v1/user/orders.

Subsequent responses will contain all updates related to open orders, trades, account balance, or open positions in a single message.

The response attributes will align with the responses from the corresponding REST API endpoints: Get trades, Get positions, Get open orders and Get balance. Refer to the Account section for details.

Error responses
Unless specified otherwise for a particular endpoint and HTTP status code, the error response model follows the general response format and includes an error code along with a descriptive message for most errors.

Error code	Error	Description
GENERAL		
400	BadRequest	Invalid or missing parameters.
401	Unauthorized	Authentication failure.
403	Forbidden	Access denied.
404	NotFound	Resource not found.
422	UnprocessableEntity	Request format is correct, but data is invalid.
429	RateLimited	Number of calls from the IP address has exceeded the rate limit.
500	InternalServerError	Internal server error.
MARKET,	ASSET & ACCOUNT	
1000	AssetNotFound	Asset not found.
1001	MarketNotFound	Market not found.
1002	MarketDisabled	Market is disabled.
1003	MarketGroupNotFound	Market group not found.
1004	AccountNotFound	Account not found.
1005	NotSupportedInterval	Not supported interval.
1006	UnhandledError	Application error.
1008	ClientNotFound	Client not found.
1009	ActionNotAllowed	Action is not allowed.
1010	MaintenanceMode	Maintenance mode.
1011	PostOnlyMode	Post only mode.
1012	ReduceOnlyMode	Reduce only mode.
1013	InvalidPercentage	Percentage should be between 0 and 1.
1014	MarketReduceOnly	Market is in reduce only mode, non-reduce only orders are not allowed.
LEVERAGE	UPDATE	
1049	InvalidLeverageBelowMinLeverage	Leverage below min leverage.
1050	InvalidLeverageExceedsMaxLeverage	Leverage exceeds max leverage.
10501	InvalidLeverageMaxPositionValueExceeded	Max position value exceeded for new leverage.
1052	InvalidLeverageInsufficientMargin	Insufficient margin for new leverage.
1053	InvalidLeverageInvalidPrecision	Leverage has invalid precision.
STARKNET	SIGNATURES	
1100	InvalidStarknetPublicKey	Invalid Starknet public key.
1101	InvalidStarknetSignature	Invalid Starknet signature.
1102	InvalidStarknetVault	Invalid Starknet vault.
ORDER		
1120	OrderQtyLessThanMinTradeSize	Order quantity less than min trade size, based on market-specific trading rules.
1121	InvalidQtyWrongSizeIncrement	Invalid quantity due to the wrong size increment, based on market-specific Minimum Change in Trade Size trading rule.
1122	OrderValueExceedsMaxOrderValue	Order value exceeds max order value, based on market-specific trading rules.
1123	InvalidQtyPrecision	Invalid quantity precision, currently equals to market-specific Minimum Change in Trade Size.
1124	InvalidPriceWrongPriceMovement	Invalid price due to wrong price movement, based on market-specific Minimum Price Change trading rule.
1125	InvalidPricePrecision	Invalid price precision, currently equals to market-specific Minimum Price Change.
1126	MaxOpenOrdersNumberExceeded	Max open orders number exceeded, currently 200 orders per market.
1127	MaxPositionValueExceeded	Max position value exceeded, based on the Margin schedule.
1128	InvalidTradingFees	Trading fees are invalid. Refer to Order management section for details.
1129	InvalidPositionTpslQty	Invalid quantity for position TP/SL.
1130	MissingOrderPrice	Order price is missing.
1131	MissingTpslTrigger	TP/SL order trigger is missing.
1132	NotAllowedOrderType	Order type is not allowed.
1133	InvalidOrderParameters	Invalid order parameters.
1134	DuplicateOrder	Duplicate Order.
1135	InvalidOrderExpiration	Order expiration date must be within 90 days for the Mainnet, 28 days for the Testnet.
1136	ReduceOnlyOrderSizeExceedsPositionSize	Reduce-only order size exceeds open position size.
1137	ReduceOnlyOrderPositionIsMissing	Position is missing for a reduce-only order.
1138	ReduceOnlyOrderPositionSameSide	Position is the same side as a reduce-only order.
1139	MarketOrderMustBeIOC	Market order must have time in force IOC.
1140	OrderCostExceedsBalance	New order cost exceeds available balance.
1141	InvalidPriceAmount	Invalid price value.
1142	EditOrderNotFound	Edit order not found.
1143	MissingConditionalTrigger	Conditional order trigger is missing.
1144	PostOnlyCantBeOnConditionalMarketOrder	Conditional market order can't be Post-only.
1145	NonReduceOnlyOrdersNotAllowed	Non reduce-only orders are not allowed.
1146	TwapOrderMustBeGTT	Twap order must have time in force GTT.
1147	OpenLossExceedsEquity	Open loss exceeds equity.
1148	TPSLOpenLossExceedsEquity	TP/SL open loss exceeds equity.
GENERAL	ACCOUNT	
1500	AccountNotSelected	Account not selected.
WITHDRAWAL		
1600	WithdrawalAmountMustBePositive	Withdrawal amount must be positive.
1601	WithdrawalDescriptionToLong	Withdrawal description is too long.
1602	WithdrawalRequestDoesNotMatchSettlement	Withdrawal request does not match settlement.
1604	WithdrawalExpirationTimeIsTooSoon	Withdrawal expiration time is below the 14 days minimum.
1605	WithdrawalInvalidAsset	Withdrawal asset is not valid.
1607	WithdrawalBlockedForAccount	Withdrawals blocked for the account. Please contact the team on Discord to unblock the withdrawals.
1608	WithdrawalAccountDoesNotBelongToUser	The withdrawal address does not match the account address.
TRANSFERS		
1650	InvalidVaultTransferAmount	Vault transfer amount is incorrect.
REFERRAL	CODE	
1700	ReferralCodeAlreadyExist	Referral code already exist.
1701	ReferralCodeInvalid	Referral code is not valid.
1703	ReferralProgramIsNotEnabled	Referral program is not enabled.
1704	ReferralCodeAlreadyApplied	Referral code already applied.
Legacy: StarkEx SDK
SDK configuration

from dataclasses import dataclass


@dataclass
class EndpointConfig:
    chain_rpc_url: str
    api_base_url: str
    stream_url: str
    onboarding_url: str
    signing_domain: str
    collateral_asset_contract: str
    asset_operations_contract: str
    collateral_asset_on_chain_id: str
    collateral_decimals: int

TESTNET_CONFIG_LEGACY_SIGNING_DOMAIN = EndpointConfig(
    chain_rpc_url="https://rpc.sepolia.org",
    api_base_url="https://api.testnet.extended.exchange/api/v1",
    stream_url="wss://api.testnet.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.testnet.extended.exchange",
    signing_domain="x10.exchange",
    collateral_asset_contract="0x0c9165046063b7bcd05c6924bbe05ed535c140a1",
    asset_operations_contract="0x7f0C670079147C5c5C45eef548E55D2cAc53B391",
    collateral_asset_on_chain_id="0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
    collateral_decimals=6,
)

STARKEX_MAINNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://cloudflare-eth.com",
    api_base_url="https://api.extended.exchange/api/v1",
    stream_url="wss://api.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.extended.exchange",
    signing_domain="extended.exchange",
    collateral_asset_contract="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    asset_operations_contract="0x1cE5D7f52A8aBd23551e91248151CA5A13353C65",
    collateral_asset_on_chain_id="0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d",
    collateral_decimals=6,
)
Extended now operates on the Starknet instance. The wind-down plan for the StarkEx instance can be found here. StarkEx-specific details apply only to users whose Extended account was created before August 12, 2025, and who have not yet migrated to Starknet. In all other cases, please follow the Starknet-specific logic described above.

StarkEx Python SDK:

For installation instructions, please refer to the description provided.

For reference implementations, explore the examples folder.

For SDK configuration, please refer to the config description.

Supported Features:

Account creation and authorisation.

Order Management.

Account Management.

Deposits, Transfers, and Withdrawals.

Market Information.

# Authentication

Authentication is crucial for ensuring that only authorized users can access private APIs. This document outlines the authentication mechanisms used for public and private APIs.

## Public API

Public APIs do not require authentication. These interfaces are accessible to anyone without the need for any credentials.

```
No authentication is required for public interfaces.
```

## Private API

Private APIs require authentication to ensure that only authorized users can access them. Authentication is achieved using custom headers that include a timestamp and a signature.

### Auth Header

The following headers must be included in the request to authenticate access to private APIs:

| Name                    | Location | Type   | Required | Description                                                                 |
| ----------------------- | -------- | ------ | -------- | --------------------------------------------------------------------------- |
| `X-edgeX-Api-Timestamp` | header   | string | must     | The timestamp when the request was made. This helps prevent replay attacks. |
| `X-edgeX-Api-Signature` | header   | string | must     | The signature generated using the private key and request details.          |

### CURL Example

```curl
curl --location --request GET 'https://pro.edgex.exchange/api/v1/private/account/getPositionTransactionPage?filterTypeList=SETTLE_FUNDING_FEE&size=10&accountId=544159487963955214' \
--header 'X-edgeX-Api-Signature: 06d28020763542c0afc296dc8743797c6fda8ea9727745b57b671f70326dfed6077cd******************************aff3162e39d05d9df1c3ddf9648650382d6e62ff1076b14c0e6c687088d3917d8490e5412a080a6e9ea940c720ddd' \
--header 'X-edgeX-Api-Timestamp: 1736313025024'
```

### Signature Elements

The signature is generated using the following elements:

| **Signature Element**          | **Description**                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `X-edgeX-Api-Timestamp`        | The timestamp when the request was made. This is retrieved from the request header. |
| **Request Method (Uppercase)** | The HTTP method of the request, converted to uppercase (e.g., GET, POST).           |
| **Request Path**               | The URI path of the request (e.g., `/api/v1/resource`).                             |
| **Request Parameter/Body**     | The query parameters or request body, sorted alphabetically.                        |

#### Request Parameter To Signature Content

The request parameters are concatenated into a single string that forms the signature content. This string includes the timestamp, HTTP method, request path, and sorted query parameters or request body, ensuring the integrity and authenticity of the request.

For example, the following request parameters are concatenated into a single string:

> 1735542383256GET/api/v1/private/account/getPositionTransactionPageaccountId=543429922991899150\&filterTypeList=SETTLE\_FUNDING\_FEE\&size=10

#### How To GET Your Private Key

To sign messages, you need to obtain your private key. This key is used to generate signatures that authorize various actions on the platform.

<figure><img src="https://306066812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpfcaPbebWLbUlo9XcPCp%2Fuploads%2Fgit-blob-7d724b6b784a7e308cb4e836bb25f3c952fa0fcb%2F20250102-134437.png?alt=media" alt=""><figcaption><p><strong>How To GET Your Private Key</strong></p></figcaption></figure>

> **Warning:** Keep your private key secure and never share it with anyone. Anyone with access to your private key can sign messages on your behalf.

### Private API Example

**Private API Auth Signature:** This is used for authentication. We do not want the hash computation to consume excessive CPU resources. Therefore, this will use SHA3 to hash the request body string before signing.

We provide SDKs in multiple languages to help you get started quickly.

> [Python SDK: make\_authenticated\_request](https://github.com/edgex-Tech/edgex-python-sdk/blob/main/edgex_sdk/internal/async_client.py#L161)
>
> [Golang SDK: requestInterceptor](https://github.com/edgex-Tech/edgex-golang-sdk/blob/5a8c8617e8a934c85c8c8c85a1878543f0053b7b/sdk/client.go#L97)

#### Java Example

Below is a Java implementation of the Ecdsa signature algorithm. This example demonstrates how to sign a GET request using a private key.

```java
import java.math.BigInteger;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.time.Duration;

import org.web3j.abi.TypeEncoder;
import org.web3j.abi.datatypes.Utf8String;
import org.web3j.crypto.Hash;
import org.web3j.utils.Numeric;
import org.web3j.abi.datatypes.generated.Uint256;

import com.starkbank.ellipticcurve.utils.RandomInteger;
import com.starkbank.ellipticcurve.PrivateKey;
import com.starkbank.ellipticcurve.Curve;
import com.starkbank.ellipticcurve.Signature;
import com.starkbank.ellipticcurve.Math;
import com.starkbank.ellipticcurve.Point;

public class EcdsaSignatureDemo {

    private static final BigInteger K_MODULUS = Numeric
            .toBigInt("0x0800000000000010ffffffffffffffffb781126dcae7b2321e66a241adc64d2f");

    private static Curve secp256k1 = new Curve(BigInteger.ONE,
            new BigInteger("3141592653589793238462643383279502884197169399375105820974944592307816406665"),
            new BigInteger("3618502788666131213697322783095070105623107215331596699973092056135872020481"),
            new BigInteger("3618502788666131213697322783095070105526743751716087489154079457884512865583"),
            new BigInteger("874739451078007766457464989774322083649278607533249481151382481072868806602"),
            new BigInteger("152666792071518830868575557812948353041420400780739481342941381225525861407"),
            "secp256k1", new long[] { 1L, 3L, 132L, 0L, 10L });

    // replace with your account id and private key    
    private static final String AccountID = "****";
    private static final String PrivateKey = "****";

    public static void main(String[] args) {
        String host = "https://pro.edgex.exchange";
        String path = "/api/v1/private/account/getAccountById";
        String method = "GET";
        String param = "accountId=" + AccountID;
        long timestamp = System.currentTimeMillis();

        String message = timestamp + method + path + param;
        String signature = signParams(message);

        String requestUrl = host + path + "?" + param;

        try {
            HttpClient client = HttpClient.newBuilder()
                    .connectTimeout(Duration.ofSeconds(30))
                    .build();

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(requestUrl))
                    .timeout(Duration.ofSeconds(30))
                    .header("X-edgeX-Api-Signature", signature)
                    .header("X-edgeX-Api-Timestamp", String.valueOf(timestamp))
                    .header("Content-Type", "application/json")
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Response Status: " + response.statusCode());
            System.out.println("Response Body: " + response.body());

        } catch (Exception e) {
            System.err.println("Request failed: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static String signParams(String message) {
        String msg = TypeEncoder.encodePacked(new Utf8String(message));
        BigInteger msgHash = Numeric.toBigInt(Hash.sha3(Numeric.hexStringToByteArray(msg)));
        msgHash = msgHash.mod(K_MODULUS);


        // Please replace it with a real private key when actually using
        String privateKeyHex = PrivateKey;
        if (privateKeyHex.startsWith("0x")) {
            privateKeyHex = privateKeyHex.substring(2);
        }
        BigInteger mySecretKey = new BigInteger(privateKeyHex, 16);
        PrivateKey privateKey = new PrivateKey(secp256k1, mySecretKey);

        Signature signature = sign(msgHash, privateKey);

        return TypeEncoder.encodePacked(new Uint256(signature.r)) +
                TypeEncoder.encodePacked(new Uint256(signature.s)) +
                TypeEncoder.encodePacked(new Uint256(privateKey.publicKey().point.y));
    }

    private static Signature sign(BigInteger numberMessage, PrivateKey privateKey) {
        Curve curve = privateKey.curve;
        BigInteger randNum = RandomInteger.between(BigInteger.ONE, curve.N);
        Point randomSignPoint = Math.multiply(curve.G, randNum, curve.N, curve.A, curve.P);
        BigInteger r = randomSignPoint.x.mod(curve.N);
        BigInteger s = numberMessage.add(r.multiply(privateKey.secret)).multiply(Math.inv(randNum, curve.N))
                .mod(curve.N);
        return new Signature(r, s);
    }
}
```

```
<dependency>
    <groupId>org.web3j</groupId>
    <artifactId>core</artifactId>
    <version>4.10.3</version>
</dependency>

<dependency>
    <groupId>com.starkbank.ellipticcurve</groupId>
    <artifactId>starkbank-ecdsa</artifactId>
    <version>1.0.2</version>
</dependency>
```

### Request Body To Body String Code Example

The following Java code example demonstrates how to convert a JSON request body into a sorted string format suitable for signature generation:

```java
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class RequestBodyToString {
    private static final String EMPTY_STRING = "";

    private static String getValue(JsonElement valueJson) {
        if (valueJson.isJsonNull()) {
            return EMPTY_STRING;
        } else if (valueJson.isJsonPrimitive()) {
            return valueJson.getAsString();
        } else if (valueJson.isJsonArray()) {
            JsonArray valueArray = valueJson.getAsJsonArray();
            if (valueArray.isEmpty()) {
                return EMPTY_STRING;
            }
            List<String> values = new ArrayList<>();
            for (JsonElement itemValue : valueArray) {
                values.add(getValue(itemValue));
            }
            return String.join("&", values);
        } else if (valueJson.isJsonObject()) {
            TreeMap<String, String> sortedDataMap = new TreeMap<>();
            JsonObject valueJsonObj = valueJson.getAsJsonObject();
            for (String key : valueJsonObj.keySet()) {
                sortedDataMap.put(key, getValue(valueJsonObj.get(key)));
            }
            return sortedDataMap.keySet().stream()
                    .map(key -> key + "=" + sortedDataMap.get(key))
                    .collect(Collectors.joining("&"));
        }
        return EMPTY_STRING;
    }
}
```

### Signature Algorithm

The signature algorithm used is Ecdsa (Elliptic Curve Digital Signature Algorithm).


# L2 Signature

## How To Sign Message

### Overview

In Layer 2 trading systems, to ensure transaction security and prevent unauthorized operations, critical operations (such as limit orders, transfers, withdrawals, etc.) require users to provide digital signatures to prove the legitimacy of the operations. This signature is passed through the `l2Signature` parameter.

### How To GET Your L2 Private Key

To generate l2Signature, you first need to obtain your L2 private key. This key is used to generate signatures that authorize various actions on the platform.

<figure><img src="https://306066812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpfcaPbebWLbUlo9XcPCp%2Fuploads%2Fgit-blob-7d724b6b784a7e308cb4e836bb25f3c952fa0fcb%2F20250102-134437.png?alt=media" alt=""><figcaption><p><strong>How To GET Your L2 Private Key</strong></p></figcaption></figure>

> **⚠️ Security Warning:**
>
> * Keep your private key secure and never share it with anyone
> * Anyone with access to your private key can sign messages and execute operations on your behalf

### Signature Algorithm

#### Two algorithms are used in the signature process:

1. **ECDSA** (Elliptic Curve Digital Signature Algorithm) is used to generate and verify signatures.
2. **Pedersen Hash** which consumes more CPU resources compared to regular Ethereum signatures, is used for message hashing.

L2Signature generation follows these standard steps:

1. **Collect Parameters**: Gather all required parameters for the operation
2. **Calculate Hash**: Use Pedersen Hash to compute the message hash
3. **Generate Signature**: Use ECDSA algorithm and L2 private key to sign the hash
4. **Format Output**: Format the signature according to API requirements

> [Python L2Signature Demo](https://github.com/edgex-Tech/edgex-python-sdk/blob/main/edgex_sdk/internal/client.py#L111)

> [Golang L2Signature Demo](https://github.com/edgex-Tech/edgex-golang-sdk/blob/main/sdk/internal/utils.go#L30)

> [Java Script L2Signature Demo](https://www.npmjs.com/package/@starkware-industries/starkware-crypto-utils#signing-a-starkex-order)

#### Java L2Signature Example

Below is a Java implementation of the Ecdsa signature algorithm. This example demonstrates how to sign a message using a private key.

```java

    public static CreateOrderRequest signOrder(
            CreateOrderRequest request,
            Contract contract,
            Coin quotelCoin,
            PrivateKey privateKey) {
        BigInteger msgHash = L2SignUtil.hashLimitOrder(
                request.getSide() == OrderSide.BUY,
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                BigIntUtil.toBigInt(contract.getStarkExSyntheticAssetId()),
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Value())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Size())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(contract.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2LimitFee())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.fromLongBits(request.getAccountId()),
                UnsignedInteger.valueOf(request.getL2Nonce()),
                UnsignedInteger.valueOf(request.getL2ExpireTime() / (60 * 60 * 1000L)));
        Signature signature = Ecdsa.sign(msgHash, privateKey);
        return request.toBuilder()
                .setL2Signature(L2Signature.newBuilder()
                        .setR(BigIntUtil.toHexStr(signature.r))
                        .setS(BigIntUtil.toHexStr(signature.s))
                        .build())
                .build();
    }

    public static BigInteger hashLimitOrder(
            boolean isBuyingSynthetic,
            BigInteger assetIdCollateral,
            BigInteger assetIdSynthetic,
            BigInteger assetIdFee,
            UnsignedLong amountCollateral,
            UnsignedLong amountSynthetic,
            UnsignedLong maxAmountFee,
            UnsignedLong positionId,
            UnsignedInteger nonce,
            UnsignedInteger expirationTimestamp) {
        BigInteger assetIdSell;
        BigInteger assetIdBuy;
        UnsignedLong amountSell;
        UnsignedLong amountBuy;
        if (isBuyingSynthetic) {
            assetIdSell = assetIdCollateral;
            assetIdBuy = assetIdSynthetic;
            amountSell = amountCollateral;
            amountBuy = amountSynthetic;
        } else {
            assetIdSell = assetIdSynthetic;
            assetIdBuy = assetIdCollateral;
            amountSell = amountSynthetic;
            amountBuy = amountCollateral;
        }
        BigInteger packedMessage0 = amountSell.bigIntegerValue();
        packedMessage0 = packedMessage0.shiftLeft(64).add(amountBuy.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(64).add(maxAmountFee.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(32).add(nonce.bigIntegerValue());

        BigInteger packedMessage1 = BigInteger.valueOf(3);
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(32).add(expirationTimestamp.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(17);

        BigInteger msg = pedersenHash(assetIdSell, assetIdBuy);
        msg = pedersenHash(msg, assetIdFee);
        msg = pedersenHash(msg, packedMessage0);
        msg = pedersenHash(msg, packedMessage1);
        return msg;
    }

    public static BigInteger pedersenHash(BigInteger... input) {
        BigInteger[][] points = PEDERSEN_POINTS;
        Point shiftPoint = new Point(points[0][0], points[0][1]);
        for (int i = 0; i < input.length; i++) {
            BigInteger x = input[i];
            for (int j = 0; j < 252; j++) {
                int pos = 2 + i * 252 + j;
                Point pt = new Point(points[pos][0], points[pos][1]);
                if (x.and(BigInteger.ONE).intValue() != 0) {
                    shiftPoint = EcMath.add(shiftPoint, pt, Curve.secp256k1.A, Curve.secp256k1.P);
                }
                x = x.shiftRight(1);
            }
        }
        return shiftPoint.x;
    }

    public static Signature sign(BigInteger msgHash, PrivateKey privateKey) {
        Curve curve = privateKey.curve;
        BigInteger randNum = new BigInteger(curve.N.toByteArray().length * 8 - 1, new SecureRandom()).abs().add(BigInteger.ONE);
        Point randomSignPoint = EcMath.multiply(curve.G, randNum, curve.N, curve.A, curve.P);
        BigInteger r = randomSignPoint.x.mod(curve.N);
        BigInteger s = ((msgHash.add(r.multiply(privateKey.secret))).multiply(EcMath.inv(randNum, curve.N))).mod(curve.N);
        return Signature.create(r, s);
    }

```

## Signature Construction Guide

This section provides detailed instructions for constructing signatures for various actions on the platform. Each operation has specific message formats and parameter requirements.

### Withdrawal Signature

Used to authorize withdrawing assets from Layer 2 to an Ethereum address.

#### Parameters

* `assetIdCollateral` - Asset ID for the collateral token from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `positionId` - User's account ID in Layer 2
* `ethAddress` - Destination Ethereum address for withdrawal
* `nonce` - Unique transaction identifier to prevent replay attacks
* `expirationTimestamp` - Unix timestamp when signature expires
* `amount` - Amount to withdraw in base units

#### Calculation

The following TypeScript function constructs the withdrawal message for signing:

```typescript
// Construct withdrawal message for signing
function getWithdrawalToAddressMsg({
  assetIdCollateral,
  positionId,
  ethAddress, 
  nonce,
  expirationTimestamp,
  amount
}) {
  // Pack parameters into 256-bit words
  const w1 = assetIdCollateral;
  let w5 = BigInt(withdrawalToAddress); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(nonce); 
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 49;

  // Calculate Pedersen hash
  return pedersen([
    pedersen([w1, ethAddress]),
    w5.toString(16)
  ]);
}
```

### Limit Order Signature

Used to authorize a limit order for perpetual trading.

#### Parameters

* `assetIdSynthetic` - Synthetic asset ID from [`meta_data.contractList.starkExSyntheticAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `assetIdCollateral` - Collateral asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `isBuyingSynthetic` - `true` for buy orders, `false` for sell orders
* `assetIdFee` - Fee token asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `amountSynthetic` - Amount of synthetic asset
* `amountCollateral` - Amount of collateral asset
* `maxAmountFee` - Maximum fee amount allowed
* `nonce` - Unique order identifier
* `positionId` - User's position ID
* `expirationTimestamp` - Unix timestamp when order expires

#### Calculation

The following TypeScript function constructs the limit order message for signing:

```typescript
function getLimitOrderMsg({
  assetIdSynthetic,
  assetIdCollateral,
  isBuyingSynthetic,
  assetIdFee,
  amountSynthetic,
  amountCollateral,
  maxAmountFee,
  nonce,
  positionId,
  expirationTimestamp
}) {
  // Determine sell/buy assets based on order side
  const [assetIdSell, assetIdBuy] = isBuyingSynthetic 
    ? [assetIdCollateral, assetIdSynthetic]
    : [assetIdSynthetic, assetIdCollateral];
  const [amountSell, amountBuy] = isBuyingSynthetic
    ? [amountCollateral, amountSynthetic] 
    : [amountSynthetic, amountCollateral];

  // Pack order data into 256-bit words
  const w1 = assetIdSell;
  const w2 = assetIdBuy;
  const w3 = assetIdFee;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);

  let w4 = BigInt(amountSell);
  w4 = (w4 << 64) + BigInt(amountBuy);
  w4 = (w4 << 64) + BigInt(maxAmountFee);
  w4 = (w4 << 32) + BigInt(nonce);
  msg = pedersen([msg, w4.toString(16)]);

  let w5 = BigInt(limitOrderWithFees); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 17;

  return pedersen([msg, w5.toString(16)]);
}
```

### Transfer Signature

Used to authorize transfers between Layer 2 accounts.

#### Parameters

* `assetId` - Asset ID being transferred
* `receiverPublicKey` - Recipient's public key
* `senderPositionId` - Sender's position ID
* `receiverPositionId` - Recipient's position ID
* `srcFeePositionId` - Fee source position ID
* `nonce` - Unique transfer identifier
* `amount` - Transfer amount
* `expirationTimestamp` - Unix timestamp when transfer expires
* `assetIdFee` - Fee token asset ID (optional, default '0')
* `maxAmountFee` - Maximum fee amount (optional, default '0')

#### Calculation

The following TypeScript function constructs the transfer message for signing:

```typescript
function getTransferMsg({
  assetId,
  receiverPublicKey,
  senderPositionId,
  receiverPositionId,
  srcFeePositionId,
  nonce,
  amount,
  expirationTimestamp,
  assetIdFee = '0',
  maxAmountFee = '0'
}) {
  // Pack transfer data into 256-bit words
  const w1 = assetId;
  const w2 = assetIdFee;
  const w3 = receiverPublicKey;

  let w4 = BigInt(senderPositionId);
  w4 = (w4 << 64) + BigInt(receiverPositionId);
  w4 = (w4 << 64) + BigInt(srcFeePositionId); 
  w4 = (w4 << 32) + BigInt(nonce);

  let w5 = BigInt(transfer); // Constant identifier
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 64) + BigInt(maxAmountFee);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 81;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);
  msg = pedersen([msg, w4.toString(16)]);
  return pedersen([msg, w5.toString(16)]);
}
```

For more details on the signature construction, see the [StarkEx documentation](https://docs.starkware.co/starkex/perpetual/signature_construction_perpetual.html).


# L2 Signature

## How To Sign Message

### Overview

In Layer 2 trading systems, to ensure transaction security and prevent unauthorized operations, critical operations (such as limit orders, transfers, withdrawals, etc.) require users to provide digital signatures to prove the legitimacy of the operations. This signature is passed through the `l2Signature` parameter.

### How To GET Your L2 Private Key

To generate l2Signature, you first need to obtain your L2 private key. This key is used to generate signatures that authorize various actions on the platform.

<figure><img src="https://306066812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpfcaPbebWLbUlo9XcPCp%2Fuploads%2Fgit-blob-7d724b6b784a7e308cb4e836bb25f3c952fa0fcb%2F20250102-134437.png?alt=media" alt=""><figcaption><p><strong>How To GET Your L2 Private Key</strong></p></figcaption></figure>

> **⚠️ Security Warning:**
>
> * Keep your private key secure and never share it with anyone
> * Anyone with access to your private key can sign messages and execute operations on your behalf

### Signature Algorithm

#### Two algorithms are used in the signature process:

1. **ECDSA** (Elliptic Curve Digital Signature Algorithm) is used to generate and verify signatures.
2. **Pedersen Hash** which consumes more CPU resources compared to regular Ethereum signatures, is used for message hashing.

L2Signature generation follows these standard steps:

1. **Collect Parameters**: Gather all required parameters for the operation
2. **Calculate Hash**: Use Pedersen Hash to compute the message hash
3. **Generate Signature**: Use ECDSA algorithm and L2 private key to sign the hash
4. **Format Output**: Format the signature according to API requirements

> [Python L2Signature Demo](https://github.com/edgex-Tech/edgex-python-sdk/blob/main/edgex_sdk/internal/client.py#L111)

> [Golang L2Signature Demo](https://github.com/edgex-Tech/edgex-golang-sdk/blob/main/sdk/internal/utils.go#L30)

> [Java Script L2Signature Demo](https://www.npmjs.com/package/@starkware-industries/starkware-crypto-utils#signing-a-starkex-order)

#### Java L2Signature Example

Below is a Java implementation of the Ecdsa signature algorithm. This example demonstrates how to sign a message using a private key.

```java

    public static CreateOrderRequest signOrder(
            CreateOrderRequest request,
            Contract contract,
            Coin quotelCoin,
            PrivateKey privateKey) {
        BigInteger msgHash = L2SignUtil.hashLimitOrder(
                request.getSide() == OrderSide.BUY,
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                BigIntUtil.toBigInt(contract.getStarkExSyntheticAssetId()),
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Value())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Size())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(contract.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2LimitFee())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.fromLongBits(request.getAccountId()),
                UnsignedInteger.valueOf(request.getL2Nonce()),
                UnsignedInteger.valueOf(request.getL2ExpireTime() / (60 * 60 * 1000L)));
        Signature signature = Ecdsa.sign(msgHash, privateKey);
        return request.toBuilder()
                .setL2Signature(L2Signature.newBuilder()
                        .setR(BigIntUtil.toHexStr(signature.r))
                        .setS(BigIntUtil.toHexStr(signature.s))
                        .build())
                .build();
    }

    public static BigInteger hashLimitOrder(
            boolean isBuyingSynthetic,
            BigInteger assetIdCollateral,
            BigInteger assetIdSynthetic,
            BigInteger assetIdFee,
            UnsignedLong amountCollateral,
            UnsignedLong amountSynthetic,
            UnsignedLong maxAmountFee,
            UnsignedLong positionId,
            UnsignedInteger nonce,
            UnsignedInteger expirationTimestamp) {
        BigInteger assetIdSell;
        BigInteger assetIdBuy;
        UnsignedLong amountSell;
        UnsignedLong amountBuy;
        if (isBuyingSynthetic) {
            assetIdSell = assetIdCollateral;
            assetIdBuy = assetIdSynthetic;
            amountSell = amountCollateral;
            amountBuy = amountSynthetic;
        } else {
            assetIdSell = assetIdSynthetic;
            assetIdBuy = assetIdCollateral;
            amountSell = amountSynthetic;
            amountBuy = amountCollateral;
        }
        BigInteger packedMessage0 = amountSell.bigIntegerValue();
        packedMessage0 = packedMessage0.shiftLeft(64).add(amountBuy.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(64).add(maxAmountFee.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(32).add(nonce.bigIntegerValue());

        BigInteger packedMessage1 = BigInteger.valueOf(3);
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(32).add(expirationTimestamp.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(17);

        BigInteger msg = pedersenHash(assetIdSell, assetIdBuy);
        msg = pedersenHash(msg, assetIdFee);
        msg = pedersenHash(msg, packedMessage0);
        msg = pedersenHash(msg, packedMessage1);
        return msg;
    }

    public static BigInteger pedersenHash(BigInteger... input) {
        BigInteger[][] points = PEDERSEN_POINTS;
        Point shiftPoint = new Point(points[0][0], points[0][1]);
        for (int i = 0; i < input.length; i++) {
            BigInteger x = input[i];
            for (int j = 0; j < 252; j++) {
                int pos = 2 + i * 252 + j;
                Point pt = new Point(points[pos][0], points[pos][1]);
                if (x.and(BigInteger.ONE).intValue() != 0) {
                    shiftPoint = EcMath.add(shiftPoint, pt, Curve.secp256k1.A, Curve.secp256k1.P);
                }
                x = x.shiftRight(1);
            }
        }
        return shiftPoint.x;
    }

    public static Signature sign(BigInteger msgHash, PrivateKey privateKey) {
        Curve curve = privateKey.curve;
        BigInteger randNum = new BigInteger(curve.N.toByteArray().length * 8 - 1, new SecureRandom()).abs().add(BigInteger.ONE);
        Point randomSignPoint = EcMath.multiply(curve.G, randNum, curve.N, curve.A, curve.P);
        BigInteger r = randomSignPoint.x.mod(curve.N);
        BigInteger s = ((msgHash.add(r.multiply(privateKey.secret))).multiply(EcMath.inv(randNum, curve.N))).mod(curve.N);
        return Signature.create(r, s);
    }

```

## Signature Construction Guide

This section provides detailed instructions for constructing signatures for various actions on the platform. Each operation has specific message formats and parameter requirements.

### Withdrawal Signature

Used to authorize withdrawing assets from Layer 2 to an Ethereum address.

#### Parameters

* `assetIdCollateral` - Asset ID for the collateral token from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `positionId` - User's account ID in Layer 2
* `ethAddress` - Destination Ethereum address for withdrawal
* `nonce` - Unique transaction identifier to prevent replay attacks
* `expirationTimestamp` - Unix timestamp when signature expires
* `amount` - Amount to withdraw in base units

#### Calculation

The following TypeScript function constructs the withdrawal message for signing:

```typescript
// Construct withdrawal message for signing
function getWithdrawalToAddressMsg({
  assetIdCollateral,
  positionId,
  ethAddress, 
  nonce,
  expirationTimestamp,
  amount
}) {
  // Pack parameters into 256-bit words
  const w1 = assetIdCollateral;
  let w5 = BigInt(withdrawalToAddress); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(nonce); 
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 49;

  // Calculate Pedersen hash
  return pedersen([
    pedersen([w1, ethAddress]),
    w5.toString(16)
  ]);
}
```

### Limit Order Signature

Used to authorize a limit order for perpetual trading.

#### Parameters

* `assetIdSynthetic` - Synthetic asset ID from [`meta_data.contractList.starkExSyntheticAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `assetIdCollateral` - Collateral asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `isBuyingSynthetic` - `true` for buy orders, `false` for sell orders
* `assetIdFee` - Fee token asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `amountSynthetic` - Amount of synthetic asset
* `amountCollateral` - Amount of collateral asset
* `maxAmountFee` - Maximum fee amount allowed
* `nonce` - Unique order identifier
* `positionId` - User's position ID
* `expirationTimestamp` - Unix timestamp when order expires

#### Calculation

The following TypeScript function constructs the limit order message for signing:

```typescript
function getLimitOrderMsg({
  assetIdSynthetic,
  assetIdCollateral,
  isBuyingSynthetic,
  assetIdFee,
  amountSynthetic,
  amountCollateral,
  maxAmountFee,
  nonce,
  positionId,
  expirationTimestamp
}) {
  // Determine sell/buy assets based on order side
  const [assetIdSell, assetIdBuy] = isBuyingSynthetic 
    ? [assetIdCollateral, assetIdSynthetic]
    : [assetIdSynthetic, assetIdCollateral];
  const [amountSell, amountBuy] = isBuyingSynthetic
    ? [amountCollateral, amountSynthetic] 
    : [amountSynthetic, amountCollateral];

  // Pack order data into 256-bit words
  const w1 = assetIdSell;
  const w2 = assetIdBuy;
  const w3 = assetIdFee;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);

  let w4 = BigInt(amountSell);
  w4 = (w4 << 64) + BigInt(amountBuy);
  w4 = (w4 << 64) + BigInt(maxAmountFee);
  w4 = (w4 << 32) + BigInt(nonce);
  msg = pedersen([msg, w4.toString(16)]);

  let w5 = BigInt(limitOrderWithFees); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 17;

  return pedersen([msg, w5.toString(16)]);
}
```

### Transfer Signature

Used to authorize transfers between Layer 2 accounts.

#### Parameters

* `assetId` - Asset ID being transferred
* `receiverPublicKey` - Recipient's public key
* `senderPositionId` - Sender's position ID
* `receiverPositionId` - Recipient's position ID
* `srcFeePositionId` - Fee source position ID
* `nonce` - Unique transfer identifier
* `amount` - Transfer amount
* `expirationTimestamp` - Unix timestamp when transfer expires
* `assetIdFee` - Fee token asset ID (optional, default '0')
* `maxAmountFee` - Maximum fee amount (optional, default '0')

#### Calculation

The following TypeScript function constructs the transfer message for signing:

```typescript
function getTransferMsg({
  assetId,
  receiverPublicKey,
  senderPositionId,
  receiverPositionId,
  srcFeePositionId,
  nonce,
  amount,
  expirationTimestamp,
  assetIdFee = '0',
  maxAmountFee = '0'
}) {
  // Pack transfer data into 256-bit words
  const w1 = assetId;
  const w2 = assetIdFee;
  const w3 = receiverPublicKey;

  let w4 = BigInt(senderPositionId);
  w4 = (w4 << 64) + BigInt(receiverPositionId);
  w4 = (w4 << 64) + BigInt(srcFeePositionId); 
  w4 = (w4 << 32) + BigInt(nonce);

  let w5 = BigInt(transfer); // Constant identifier
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 64) + BigInt(maxAmountFee);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 81;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);
  msg = pedersen([msg, w4.toString(16)]);
  return pedersen([msg, w5.toString(16)]);
}
```

For more details on the signature construction, see the [StarkEx documentation](https://docs.starkware.co/starkex/perpetual/signature_construction_perpetual.html).


# L2 Signature

## How To Sign Message

### Overview

In Layer 2 trading systems, to ensure transaction security and prevent unauthorized operations, critical operations (such as limit orders, transfers, withdrawals, etc.) require users to provide digital signatures to prove the legitimacy of the operations. This signature is passed through the `l2Signature` parameter.

### How To GET Your L2 Private Key

To generate l2Signature, you first need to obtain your L2 private key. This key is used to generate signatures that authorize various actions on the platform.

<figure><img src="https://306066812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpfcaPbebWLbUlo9XcPCp%2Fuploads%2Fgit-blob-7d724b6b784a7e308cb4e836bb25f3c952fa0fcb%2F20250102-134437.png?alt=media" alt=""><figcaption><p><strong>How To GET Your L2 Private Key</strong></p></figcaption></figure>

> **⚠️ Security Warning:**
>
> * Keep your private key secure and never share it with anyone
> * Anyone with access to your private key can sign messages and execute operations on your behalf

### Signature Algorithm

#### Two algorithms are used in the signature process:

1. **ECDSA** (Elliptic Curve Digital Signature Algorithm) is used to generate and verify signatures.
2. **Pedersen Hash** which consumes more CPU resources compared to regular Ethereum signatures, is used for message hashing.

L2Signature generation follows these standard steps:

1. **Collect Parameters**: Gather all required parameters for the operation
2. **Calculate Hash**: Use Pedersen Hash to compute the message hash
3. **Generate Signature**: Use ECDSA algorithm and L2 private key to sign the hash
4. **Format Output**: Format the signature according to API requirements

> [Python L2Signature Demo](https://github.com/edgex-Tech/edgex-python-sdk/blob/main/edgex_sdk/internal/client.py#L111)

> [Golang L2Signature Demo](https://github.com/edgex-Tech/edgex-golang-sdk/blob/main/sdk/internal/utils.go#L30)

> [Java Script L2Signature Demo](https://www.npmjs.com/package/@starkware-industries/starkware-crypto-utils#signing-a-starkex-order)

#### Java L2Signature Example

Below is a Java implementation of the Ecdsa signature algorithm. This example demonstrates how to sign a message using a private key.

```java

    public static CreateOrderRequest signOrder(
            CreateOrderRequest request,
            Contract contract,
            Coin quotelCoin,
            PrivateKey privateKey) {
        BigInteger msgHash = L2SignUtil.hashLimitOrder(
                request.getSide() == OrderSide.BUY,
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                BigIntUtil.toBigInt(contract.getStarkExSyntheticAssetId()),
                BigIntUtil.toBigInt(quotelCoin.getStarkExAssetId()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Value())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2Size())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(contract.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.valueOf(new BigDecimal(request.getL2LimitFee())
                        .multiply(new BigDecimal(BigIntUtil.toBigInt(quotelCoin.getStarkExResolution())))
                        .toBigIntegerExact()),
                UnsignedLong.fromLongBits(request.getAccountId()),
                UnsignedInteger.valueOf(request.getL2Nonce()),
                UnsignedInteger.valueOf(request.getL2ExpireTime() / (60 * 60 * 1000L)));
        Signature signature = Ecdsa.sign(msgHash, privateKey);
        return request.toBuilder()
                .setL2Signature(L2Signature.newBuilder()
                        .setR(BigIntUtil.toHexStr(signature.r))
                        .setS(BigIntUtil.toHexStr(signature.s))
                        .build())
                .build();
    }

    public static BigInteger hashLimitOrder(
            boolean isBuyingSynthetic,
            BigInteger assetIdCollateral,
            BigInteger assetIdSynthetic,
            BigInteger assetIdFee,
            UnsignedLong amountCollateral,
            UnsignedLong amountSynthetic,
            UnsignedLong maxAmountFee,
            UnsignedLong positionId,
            UnsignedInteger nonce,
            UnsignedInteger expirationTimestamp) {
        BigInteger assetIdSell;
        BigInteger assetIdBuy;
        UnsignedLong amountSell;
        UnsignedLong amountBuy;
        if (isBuyingSynthetic) {
            assetIdSell = assetIdCollateral;
            assetIdBuy = assetIdSynthetic;
            amountSell = amountCollateral;
            amountBuy = amountSynthetic;
        } else {
            assetIdSell = assetIdSynthetic;
            assetIdBuy = assetIdCollateral;
            amountSell = amountSynthetic;
            amountBuy = amountCollateral;
        }
        BigInteger packedMessage0 = amountSell.bigIntegerValue();
        packedMessage0 = packedMessage0.shiftLeft(64).add(amountBuy.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(64).add(maxAmountFee.bigIntegerValue());
        packedMessage0 = packedMessage0.shiftLeft(32).add(nonce.bigIntegerValue());

        BigInteger packedMessage1 = BigInteger.valueOf(3);
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(64).add(positionId.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(32).add(expirationTimestamp.bigIntegerValue());
        packedMessage1 = packedMessage1.shiftLeft(17);

        BigInteger msg = pedersenHash(assetIdSell, assetIdBuy);
        msg = pedersenHash(msg, assetIdFee);
        msg = pedersenHash(msg, packedMessage0);
        msg = pedersenHash(msg, packedMessage1);
        return msg;
    }

    public static BigInteger pedersenHash(BigInteger... input) {
        BigInteger[][] points = PEDERSEN_POINTS;
        Point shiftPoint = new Point(points[0][0], points[0][1]);
        for (int i = 0; i < input.length; i++) {
            BigInteger x = input[i];
            for (int j = 0; j < 252; j++) {
                int pos = 2 + i * 252 + j;
                Point pt = new Point(points[pos][0], points[pos][1]);
                if (x.and(BigInteger.ONE).intValue() != 0) {
                    shiftPoint = EcMath.add(shiftPoint, pt, Curve.secp256k1.A, Curve.secp256k1.P);
                }
                x = x.shiftRight(1);
            }
        }
        return shiftPoint.x;
    }

    public static Signature sign(BigInteger msgHash, PrivateKey privateKey) {
        Curve curve = privateKey.curve;
        BigInteger randNum = new BigInteger(curve.N.toByteArray().length * 8 - 1, new SecureRandom()).abs().add(BigInteger.ONE);
        Point randomSignPoint = EcMath.multiply(curve.G, randNum, curve.N, curve.A, curve.P);
        BigInteger r = randomSignPoint.x.mod(curve.N);
        BigInteger s = ((msgHash.add(r.multiply(privateKey.secret))).multiply(EcMath.inv(randNum, curve.N))).mod(curve.N);
        return Signature.create(r, s);
    }

```

## Signature Construction Guide

This section provides detailed instructions for constructing signatures for various actions on the platform. Each operation has specific message formats and parameter requirements.

### Withdrawal Signature

Used to authorize withdrawing assets from Layer 2 to an Ethereum address.

#### Parameters

* `assetIdCollateral` - Asset ID for the collateral token from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `positionId` - User's account ID in Layer 2
* `ethAddress` - Destination Ethereum address for withdrawal
* `nonce` - Unique transaction identifier to prevent replay attacks
* `expirationTimestamp` - Unix timestamp when signature expires
* `amount` - Amount to withdraw in base units

#### Calculation

The following TypeScript function constructs the withdrawal message for signing:

```typescript
// Construct withdrawal message for signing
function getWithdrawalToAddressMsg({
  assetIdCollateral,
  positionId,
  ethAddress, 
  nonce,
  expirationTimestamp,
  amount
}) {
  // Pack parameters into 256-bit words
  const w1 = assetIdCollateral;
  let w5 = BigInt(withdrawalToAddress); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(nonce); 
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 49;

  // Calculate Pedersen hash
  return pedersen([
    pedersen([w1, ethAddress]),
    w5.toString(16)
  ]);
}
```

### Limit Order Signature

Used to authorize a limit order for perpetual trading.

#### Parameters

* `assetIdSynthetic` - Synthetic asset ID from [`meta_data.contractList.starkExSyntheticAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `assetIdCollateral` - Collateral asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `isBuyingSynthetic` - `true` for buy orders, `false` for sell orders
* `assetIdFee` - Fee token asset ID from [`meta_data.coinList.starkExAssetId`](https://edgex-1.gitbook.io/edgeX-documentation/api/public-api/metadata-api)
* `amountSynthetic` - Amount of synthetic asset
* `amountCollateral` - Amount of collateral asset
* `maxAmountFee` - Maximum fee amount allowed
* `nonce` - Unique order identifier
* `positionId` - User's position ID
* `expirationTimestamp` - Unix timestamp when order expires

#### Calculation

The following TypeScript function constructs the limit order message for signing:

```typescript
function getLimitOrderMsg({
  assetIdSynthetic,
  assetIdCollateral,
  isBuyingSynthetic,
  assetIdFee,
  amountSynthetic,
  amountCollateral,
  maxAmountFee,
  nonce,
  positionId,
  expirationTimestamp
}) {
  // Determine sell/buy assets based on order side
  const [assetIdSell, assetIdBuy] = isBuyingSynthetic 
    ? [assetIdCollateral, assetIdSynthetic]
    : [assetIdSynthetic, assetIdCollateral];
  const [amountSell, amountBuy] = isBuyingSynthetic
    ? [amountCollateral, amountSynthetic] 
    : [amountSynthetic, amountCollateral];

  // Pack order data into 256-bit words
  const w1 = assetIdSell;
  const w2 = assetIdBuy;
  const w3 = assetIdFee;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);

  let w4 = BigInt(amountSell);
  w4 = (w4 << 64) + BigInt(amountBuy);
  w4 = (w4 << 64) + BigInt(maxAmountFee);
  w4 = (w4 << 32) + BigInt(nonce);
  msg = pedersen([msg, w4.toString(16)]);

  let w5 = BigInt(limitOrderWithFees); // Constant identifier
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 64) + BigInt(positionId);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 17;

  return pedersen([msg, w5.toString(16)]);
}
```

### Transfer Signature

Used to authorize transfers between Layer 2 accounts.

#### Parameters

* `assetId` - Asset ID being transferred
* `receiverPublicKey` - Recipient's public key
* `senderPositionId` - Sender's position ID
* `receiverPositionId` - Recipient's position ID
* `srcFeePositionId` - Fee source position ID
* `nonce` - Unique transfer identifier
* `amount` - Transfer amount
* `expirationTimestamp` - Unix timestamp when transfer expires
* `assetIdFee` - Fee token asset ID (optional, default '0')
* `maxAmountFee` - Maximum fee amount (optional, default '0')

#### Calculation

The following TypeScript function constructs the transfer message for signing:

```typescript
function getTransferMsg({
  assetId,
  receiverPublicKey,
  senderPositionId,
  receiverPositionId,
  srcFeePositionId,
  nonce,
  amount,
  expirationTimestamp,
  assetIdFee = '0',
  maxAmountFee = '0'
}) {
  // Pack transfer data into 256-bit words
  const w1 = assetId;
  const w2 = assetIdFee;
  const w3 = receiverPublicKey;

  let w4 = BigInt(senderPositionId);
  w4 = (w4 << 64) + BigInt(receiverPositionId);
  w4 = (w4 << 64) + BigInt(srcFeePositionId); 
  w4 = (w4 << 32) + BigInt(nonce);

  let w5 = BigInt(transfer); // Constant identifier
  w5 = (w5 << 64) + BigInt(amount);
  w5 = (w5 << 64) + BigInt(maxAmountFee);
  w5 = (w5 << 32) + BigInt(expirationTimestamp);
  w5 = w5 << 81;

  // Calculate message hash
  let msg = pedersen([w1, w2]);
  msg = pedersen([msg, w3]);
  msg = pedersen([msg, w4.toString(16)]);
  return pedersen([msg, w5.toString(16)]);
}
```

For more details on the signature construction, see the [StarkEx documentation](https://docs.starkware.co/starkex/perpetual/signature_construction_perpetual.html).


# Funding API

## FundingPublicApi

### GET Get Latest Funding Rate by Contract ID

GET /api/v1/public/funding/getLatestFundingRate

#### Request Parameters

| Name       | Location | Type   | Required | Description |
| ---------- | -------- | ------ | -------- | ----------- |
| contractId | query    | string | No       | Contract ID |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "contractId": "10000001",
            "fundingTime": "1734595200000",
            "fundingTimestamp": "1734597720000",
            "oraclePrice": "101559.9220921285450458526611328125",
            "indexPrice": "101522.558968500",
            "fundingRate": "-0.00005537",
            "isSettlement": false,
            "forecastFundingRate": "-0.00012293",
            "previousFundingRate": "0.00000567",
            "previousFundingTimestamp": "1734595140000",
            "premiumIndex": "-0.00036207",
            "avgPremiumIndex": "-0.00032293",
            "premiumIndexTimestamp": "1734597720000",
            "impactMarginNotional": "100",
            "impactAskPrice": "101485.8",
            "impactBidPrice": "101484.7",
            "interestRate": "0.0003",
            "predictedFundingRate": "0.00005000",
            "fundingRateIntervalMin": "240",
            "starkExFundingIndex": "101559.9220921285450458526611328125"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597737870",
    "responseTime": "1734597737873",
    "traceId": "5e27ebfb0ae79f51bbd347d2bf3585f9"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#schemapagedatafundingrate>) |

### GET Get Funding Rate History by Contract ID with Pagination

GET /api/v1/public/funding/getFundingRatePage

#### Request Parameters

| Name                        | Location | Type   | Required | Description                                                                                                                                        |
| --------------------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId                  | query    | string | No       | Contract ID                                                                                                                                        |
| size                        | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100                                                                  |
| offsetData                  | query    | string | No       | Pagination offset. If not provided or empty, retrieves the first page                                                                              |
| filterSettlementFundingRate | query    | string | No       | If true, only query settlement funding rates (funding rate settlement occurs every 8 hours, with a predicted funding rate calculated every minute) |
| filterBeginTimeInclusive    | query    | string | No       | Start time. If not provided, retrieves the oldest data                                                                                             |
| filterEndTimeExclusive      | query    | string | No       | End time. If not provided, retrieves the latest data                                                                                               |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "contractId": "10000001",
                "fundingTime": "1733702400000",
                "fundingTimestamp": "1733702400000",
                "oraclePrice": "101120.888977311551570892333984375",
                "indexPrice": "101121.681521500",
                "fundingRate": "0.00005000",
                "isSettlement": true,
                "forecastFundingRate": "",
                "previousFundingRate": "0.00005000",
                "previousFundingTimestamp": "1733702340000",
                "premiumIndex": "0.00022566",
                "avgPremiumIndex": "0.00017953",
                "premiumIndexTimestamp": "1733702400000",
                "impactMarginNotional": "500",
                "impactAskPrice": "101269.6",
                "impactBidPrice": "101269.1",
                "interestRate": "0.0003",
                "predictedFundingRate": "0.00005000",
                "fundingRateIntervalMin": "240",
                "starkExFundingIndex": "101120.888977311551570892333984375"
            }
        ],
        "nextPageOffsetData": "0880A08A97B532"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597585432",
    "responseTime": "1734597586672",
    "traceId": "02465a59be5d19088ba7e4b5c6b94f6d"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                      |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatafundingrate>) |

## Data Models

#### pagedatafundingrate

| Name         | Type                                              | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------------------- | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                                            | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | [PageDataFundingRate](#schemapagedatafundingrate) | false    | none        | General pagination response                                     |
| errorParam   | object                                            | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                                 | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                                 | false    | none        | Server response time                                            |
| traceId      | string                                            | false    | none        | Call trace ID                                                   |

#### schemapagedatafundingrate

| Name               | Type                                 | Required | Constraints | Description                                                                  |
| ------------------ | ------------------------------------ | -------- | ----------- | ---------------------------------------------------------------------------- |
| dataList           | \[[FundingRate](#schemafundingrate)] | false    | none        | Data list                                                                    |
| nextPageOffsetData | string                               | false    | none        | Offset data to retrieve the next page. Empty string if there is no next page |

#### listfundingrate

| Name         | Type                                 | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------ | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                               | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | \[[FundingRate](#schemafundingrate)] | false    | none        | Successful response data                                        |
| errorParam   | object                               | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                    | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                    | false    | none        | Server response time                                            |
| traceId      | string                               | false    | none        | Call trace ID                                                   |

#### schemafundingrate

| Name                     | Type          | Required | Constraints | Description                                                                                                                                                                            |
| ------------------------ | ------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId               | string(int64) | false    | none        | Contract ID                                                                                                                                                                            |
| fundingTime              | string(int64) | false    | none        | Funding rate settlement time. E.g., the funding rate for the 08:00-09:00 period is calculated from the previous 07:00-08:00 data, finalized at 08:00, and used for settlement at 09:00 |
| fundingTimestamp         | string(int64) | false    | none        | Funding rate calculation time in milliseconds                                                                                                                                          |
| oraclePrice              | string        | false    | none        | Oracle price                                                                                                                                                                           |
| indexPrice               | string        | false    | none        | Index price                                                                                                                                                                            |
| fundingRate              | string        | false    | none        | Funding rate                                                                                                                                                                           |
| isSettlement             | boolean       | false    | none        | Funding rate settlement flag                                                                                                                                                           |
| forecastFundingRate      | string        | false    | none        | Forecast funding rate                                                                                                                                                                  |
| previousFundingRate      | string        | false    | none        | Previous funding rate                                                                                                                                                                  |
| previousFundingTimestamp | string(int64) | false    | none        | Previous funding rate calculation time in milliseconds                                                                                                                                 |
| premiumIndex             | string        | false    | none        | Premium index                                                                                                                                                                          |
| avgPremiumIndex          | string        | false    | none        | Average premium index                                                                                                                                                                  |
| premiumIndexTimestamp    | string        | false    | none        | Premium index calculation time                                                                                                                                                         |
| impactMarginNotional     | string        | false    | none        | Quantity required for deep weighted buy/sell price calculation                                                                                                                         |
| impactAskPrice           | string        | false    | none        | Deep weighted ask price                                                                                                                                                                |
| impactBidPrice           | string        | false    | none        | Deep weighted bid price                                                                                                                                                                |
| interestRate             | string        | false    | none        | Fixed interest rate                                                                                                                                                                    |
| predictedFundingRate     | string        | false    | none        | Comprehensive interest rate (interestRate/frequency)                                                                                                                                   |
| fundingRateIntervalMin   | string(int64) | false    | none        | Funding rate time interval in minutes                                                                                                                                                  |
| starkExFundingIndex      | string        | false    | none        | StarkEx funding index                                                                                                                                                                  |


# Funding API

## FundingPublicApi

### GET Get Latest Funding Rate by Contract ID

GET /api/v1/public/funding/getLatestFundingRate

#### Request Parameters

| Name       | Location | Type   | Required | Description |
| ---------- | -------- | ------ | -------- | ----------- |
| contractId | query    | string | No       | Contract ID |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "contractId": "10000001",
            "fundingTime": "1734595200000",
            "fundingTimestamp": "1734597720000",
            "oraclePrice": "101559.9220921285450458526611328125",
            "indexPrice": "101522.558968500",
            "fundingRate": "-0.00005537",
            "isSettlement": false,
            "forecastFundingRate": "-0.00012293",
            "previousFundingRate": "0.00000567",
            "previousFundingTimestamp": "1734595140000",
            "premiumIndex": "-0.00036207",
            "avgPremiumIndex": "-0.00032293",
            "premiumIndexTimestamp": "1734597720000",
            "impactMarginNotional": "100",
            "impactAskPrice": "101485.8",
            "impactBidPrice": "101484.7",
            "interestRate": "0.0003",
            "predictedFundingRate": "0.00005000",
            "fundingRateIntervalMin": "240",
            "starkExFundingIndex": "101559.9220921285450458526611328125"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597737870",
    "responseTime": "1734597737873",
    "traceId": "5e27ebfb0ae79f51bbd347d2bf3585f9"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#schemapagedatafundingrate>) |

### GET Get Funding Rate History by Contract ID with Pagination

GET /api/v1/public/funding/getFundingRatePage

#### Request Parameters

| Name                        | Location | Type   | Required | Description                                                                                                                                        |
| --------------------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId                  | query    | string | No       | Contract ID                                                                                                                                        |
| size                        | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100                                                                  |
| offsetData                  | query    | string | No       | Pagination offset. If not provided or empty, retrieves the first page                                                                              |
| filterSettlementFundingRate | query    | string | No       | If true, only query settlement funding rates (funding rate settlement occurs every 8 hours, with a predicted funding rate calculated every minute) |
| filterBeginTimeInclusive    | query    | string | No       | Start time. If not provided, retrieves the oldest data                                                                                             |
| filterEndTimeExclusive      | query    | string | No       | End time. If not provided, retrieves the latest data                                                                                               |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "contractId": "10000001",
                "fundingTime": "1733702400000",
                "fundingTimestamp": "1733702400000",
                "oraclePrice": "101120.888977311551570892333984375",
                "indexPrice": "101121.681521500",
                "fundingRate": "0.00005000",
                "isSettlement": true,
                "forecastFundingRate": "",
                "previousFundingRate": "0.00005000",
                "previousFundingTimestamp": "1733702340000",
                "premiumIndex": "0.00022566",
                "avgPremiumIndex": "0.00017953",
                "premiumIndexTimestamp": "1733702400000",
                "impactMarginNotional": "500",
                "impactAskPrice": "101269.6",
                "impactBidPrice": "101269.1",
                "interestRate": "0.0003",
                "predictedFundingRate": "0.00005000",
                "fundingRateIntervalMin": "240",
                "starkExFundingIndex": "101120.888977311551570892333984375"
            }
        ],
        "nextPageOffsetData": "0880A08A97B532"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597585432",
    "responseTime": "1734597586672",
    "traceId": "02465a59be5d19088ba7e4b5c6b94f6d"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                      |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatafundingrate>) |

## Data Models

#### pagedatafundingrate

| Name         | Type                                              | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------------------- | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                                            | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | [PageDataFundingRate](#schemapagedatafundingrate) | false    | none        | General pagination response                                     |
| errorParam   | object                                            | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                                 | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                                 | false    | none        | Server response time                                            |
| traceId      | string                                            | false    | none        | Call trace ID                                                   |

#### schemapagedatafundingrate

| Name               | Type                                 | Required | Constraints | Description                                                                  |
| ------------------ | ------------------------------------ | -------- | ----------- | ---------------------------------------------------------------------------- |
| dataList           | \[[FundingRate](#schemafundingrate)] | false    | none        | Data list                                                                    |
| nextPageOffsetData | string                               | false    | none        | Offset data to retrieve the next page. Empty string if there is no next page |

#### listfundingrate

| Name         | Type                                 | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------ | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                               | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | \[[FundingRate](#schemafundingrate)] | false    | none        | Successful response data                                        |
| errorParam   | object                               | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                    | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                    | false    | none        | Server response time                                            |
| traceId      | string                               | false    | none        | Call trace ID                                                   |

#### schemafundingrate

| Name                     | Type          | Required | Constraints | Description                                                                                                                                                                            |
| ------------------------ | ------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId               | string(int64) | false    | none        | Contract ID                                                                                                                                                                            |
| fundingTime              | string(int64) | false    | none        | Funding rate settlement time. E.g., the funding rate for the 08:00-09:00 period is calculated from the previous 07:00-08:00 data, finalized at 08:00, and used for settlement at 09:00 |
| fundingTimestamp         | string(int64) | false    | none        | Funding rate calculation time in milliseconds                                                                                                                                          |
| oraclePrice              | string        | false    | none        | Oracle price                                                                                                                                                                           |
| indexPrice               | string        | false    | none        | Index price                                                                                                                                                                            |
| fundingRate              | string        | false    | none        | Funding rate                                                                                                                                                                           |
| isSettlement             | boolean       | false    | none        | Funding rate settlement flag                                                                                                                                                           |
| forecastFundingRate      | string        | false    | none        | Forecast funding rate                                                                                                                                                                  |
| previousFundingRate      | string        | false    | none        | Previous funding rate                                                                                                                                                                  |
| previousFundingTimestamp | string(int64) | false    | none        | Previous funding rate calculation time in milliseconds                                                                                                                                 |
| premiumIndex             | string        | false    | none        | Premium index                                                                                                                                                                          |
| avgPremiumIndex          | string        | false    | none        | Average premium index                                                                                                                                                                  |
| premiumIndexTimestamp    | string        | false    | none        | Premium index calculation time                                                                                                                                                         |
| impactMarginNotional     | string        | false    | none        | Quantity required for deep weighted buy/sell price calculation                                                                                                                         |
| impactAskPrice           | string        | false    | none        | Deep weighted ask price                                                                                                                                                                |
| impactBidPrice           | string        | false    | none        | Deep weighted bid price                                                                                                                                                                |
| interestRate             | string        | false    | none        | Fixed interest rate                                                                                                                                                                    |
| predictedFundingRate     | string        | false    | none        | Comprehensive interest rate (interestRate/frequency)                                                                                                                                   |
| fundingRateIntervalMin   | string(int64) | false    | none        | Funding rate time interval in minutes                                                                                                                                                  |
| starkExFundingIndex      | string        | false    | none        | StarkEx funding index                                                                                                                                                                  |




# Funding API

## FundingPublicApi

### GET Get Latest Funding Rate by Contract ID

GET /api/v1/public/funding/getLatestFundingRate

#### Request Parameters

| Name       | Location | Type   | Required | Description |
| ---------- | -------- | ------ | -------- | ----------- |
| contractId | query    | string | No       | Contract ID |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "contractId": "10000001",
            "fundingTime": "1734595200000",
            "fundingTimestamp": "1734597720000",
            "oraclePrice": "101559.9220921285450458526611328125",
            "indexPrice": "101522.558968500",
            "fundingRate": "-0.00005537",
            "isSettlement": false,
            "forecastFundingRate": "-0.00012293",
            "previousFundingRate": "0.00000567",
            "previousFundingTimestamp": "1734595140000",
            "premiumIndex": "-0.00036207",
            "avgPremiumIndex": "-0.00032293",
            "premiumIndexTimestamp": "1734597720000",
            "impactMarginNotional": "100",
            "impactAskPrice": "101485.8",
            "impactBidPrice": "101484.7",
            "interestRate": "0.0003",
            "predictedFundingRate": "0.00005000",
            "fundingRateIntervalMin": "240",
            "starkExFundingIndex": "101559.9220921285450458526611328125"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597737870",
    "responseTime": "1734597737873",
    "traceId": "5e27ebfb0ae79f51bbd347d2bf3585f9"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#schemapagedatafundingrate>) |

### GET Get Funding Rate History by Contract ID with Pagination

GET /api/v1/public/funding/getFundingRatePage

#### Request Parameters

| Name                        | Location | Type   | Required | Description                                                                                                                                        |
| --------------------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId                  | query    | string | No       | Contract ID                                                                                                                                        |
| size                        | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100                                                                  |
| offsetData                  | query    | string | No       | Pagination offset. If not provided or empty, retrieves the first page                                                                              |
| filterSettlementFundingRate | query    | string | No       | If true, only query settlement funding rates (funding rate settlement occurs every 8 hours, with a predicted funding rate calculated every minute) |
| filterBeginTimeInclusive    | query    | string | No       | Start time. If not provided, retrieves the oldest data                                                                                             |
| filterEndTimeExclusive      | query    | string | No       | End time. If not provided, retrieves the latest data                                                                                               |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "contractId": "10000001",
                "fundingTime": "1733702400000",
                "fundingTimestamp": "1733702400000",
                "oraclePrice": "101120.888977311551570892333984375",
                "indexPrice": "101121.681521500",
                "fundingRate": "0.00005000",
                "isSettlement": true,
                "forecastFundingRate": "",
                "previousFundingRate": "0.00005000",
                "previousFundingTimestamp": "1733702340000",
                "premiumIndex": "0.00022566",
                "avgPremiumIndex": "0.00017953",
                "premiumIndexTimestamp": "1733702400000",
                "impactMarginNotional": "500",
                "impactAskPrice": "101269.6",
                "impactBidPrice": "101269.1",
                "interestRate": "0.0003",
                "predictedFundingRate": "0.00005000",
                "fundingRateIntervalMin": "240",
                "starkExFundingIndex": "101120.888977311551570892333984375"
            }
        ],
        "nextPageOffsetData": "0880A08A97B532"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597585432",
    "responseTime": "1734597586672",
    "traceId": "02465a59be5d19088ba7e4b5c6b94f6d"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                      |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatafundingrate>) |

## Data Models

#### pagedatafundingrate

| Name         | Type                                              | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------------------- | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                                            | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | [PageDataFundingRate](#schemapagedatafundingrate) | false    | none        | General pagination response                                     |
| errorParam   | object                                            | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                                 | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                                 | false    | none        | Server response time                                            |
| traceId      | string                                            | false    | none        | Call trace ID                                                   |

#### schemapagedatafundingrate

| Name               | Type                                 | Required | Constraints | Description                                                                  |
| ------------------ | ------------------------------------ | -------- | ----------- | ---------------------------------------------------------------------------- |
| dataList           | \[[FundingRate](#schemafundingrate)] | false    | none        | Data list                                                                    |
| nextPageOffsetData | string                               | false    | none        | Offset data to retrieve the next page. Empty string if there is no next page |

#### listfundingrate

| Name         | Type                                 | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------ | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                               | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | \[[FundingRate](#schemafundingrate)] | false    | none        | Successful response data                                        |
| errorParam   | object                               | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                    | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                    | false    | none        | Server response time                                            |
| traceId      | string                               | false    | none        | Call trace ID                                                   |

#### schemafundingrate

| Name                     | Type          | Required | Constraints | Description                                                                                                                                                                            |
| ------------------------ | ------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId               | string(int64) | false    | none        | Contract ID                                                                                                                                                                            |
| fundingTime              | string(int64) | false    | none        | Funding rate settlement time. E.g., the funding rate for the 08:00-09:00 period is calculated from the previous 07:00-08:00 data, finalized at 08:00, and used for settlement at 09:00 |
| fundingTimestamp         | string(int64) | false    | none        | Funding rate calculation time in milliseconds                                                                                                                                          |
| oraclePrice              | string        | false    | none        | Oracle price                                                                                                                                                                           |
| indexPrice               | string        | false    | none        | Index price                                                                                                                                                                            |
| fundingRate              | string        | false    | none        | Funding rate                                                                                                                                                                           |
| isSettlement             | boolean       | false    | none        | Funding rate settlement flag                                                                                                                                                           |
| forecastFundingRate      | string        | false    | none        | Forecast funding rate                                                                                                                                                                  |
| previousFundingRate      | string        | false    | none        | Previous funding rate                                                                                                                                                                  |
| previousFundingTimestamp | string(int64) | false    | none        | Previous funding rate calculation time in milliseconds                                                                                                                                 |
| premiumIndex             | string        | false    | none        | Premium index                                                                                                                                                                          |
| avgPremiumIndex          | string        | false    | none        | Average premium index                                                                                                                                                                  |
| premiumIndexTimestamp    | string        | false    | none        | Premium index calculation time                                                                                                                                                         |
| impactMarginNotional     | string        | false    | none        | Quantity required for deep weighted buy/sell price calculation                                                                                                                         |
| impactAskPrice           | string        | false    | none        | Deep weighted ask price                                                                                                                                                                |
| impactBidPrice           | string        | false    | none        | Deep weighted bid price                                                                                                                                                                |
| interestRate             | string        | false    | none        | Fixed interest rate                                                                                                                                                                    |
| predictedFundingRate     | string        | false    | none        | Comprehensive interest rate (interestRate/frequency)                                                                                                                                   |
| fundingRateIntervalMin   | string(int64) | false    | none        | Funding rate time interval in minutes                                                                                                                                                  |
| starkExFundingIndex      | string        | false    | none        | StarkEx funding index                                                                                                                                                                  |



# Funding API

## FundingPublicApi

### GET Get Latest Funding Rate by Contract ID

GET /api/v1/public/funding/getLatestFundingRate

#### Request Parameters

| Name       | Location | Type   | Required | Description |
| ---------- | -------- | ------ | -------- | ----------- |
| contractId | query    | string | No       | Contract ID |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "contractId": "10000001",
            "fundingTime": "1734595200000",
            "fundingTimestamp": "1734597720000",
            "oraclePrice": "101559.9220921285450458526611328125",
            "indexPrice": "101522.558968500",
            "fundingRate": "-0.00005537",
            "isSettlement": false,
            "forecastFundingRate": "-0.00012293",
            "previousFundingRate": "0.00000567",
            "previousFundingTimestamp": "1734595140000",
            "premiumIndex": "-0.00036207",
            "avgPremiumIndex": "-0.00032293",
            "premiumIndexTimestamp": "1734597720000",
            "impactMarginNotional": "100",
            "impactAskPrice": "101485.8",
            "impactBidPrice": "101484.7",
            "interestRate": "0.0003",
            "predictedFundingRate": "0.00005000",
            "fundingRateIntervalMin": "240",
            "starkExFundingIndex": "101559.9220921285450458526611328125"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597737870",
    "responseTime": "1734597737873",
    "traceId": "5e27ebfb0ae79f51bbd347d2bf3585f9"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#schemapagedatafundingrate>) |

### GET Get Funding Rate History by Contract ID with Pagination

GET /api/v1/public/funding/getFundingRatePage

#### Request Parameters

| Name                        | Location | Type   | Required | Description                                                                                                                                        |
| --------------------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId                  | query    | string | No       | Contract ID                                                                                                                                        |
| size                        | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100                                                                  |
| offsetData                  | query    | string | No       | Pagination offset. If not provided or empty, retrieves the first page                                                                              |
| filterSettlementFundingRate | query    | string | No       | If true, only query settlement funding rates (funding rate settlement occurs every 8 hours, with a predicted funding rate calculated every minute) |
| filterBeginTimeInclusive    | query    | string | No       | Start time. If not provided, retrieves the oldest data                                                                                             |
| filterEndTimeExclusive      | query    | string | No       | End time. If not provided, retrieves the latest data                                                                                               |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "contractId": "10000001",
                "fundingTime": "1733702400000",
                "fundingTimestamp": "1733702400000",
                "oraclePrice": "101120.888977311551570892333984375",
                "indexPrice": "101121.681521500",
                "fundingRate": "0.00005000",
                "isSettlement": true,
                "forecastFundingRate": "",
                "previousFundingRate": "0.00005000",
                "previousFundingTimestamp": "1733702340000",
                "premiumIndex": "0.00022566",
                "avgPremiumIndex": "0.00017953",
                "premiumIndexTimestamp": "1733702400000",
                "impactMarginNotional": "500",
                "impactAskPrice": "101269.6",
                "impactBidPrice": "101269.1",
                "interestRate": "0.0003",
                "predictedFundingRate": "0.00005000",
                "fundingRateIntervalMin": "240",
                "starkExFundingIndex": "101120.888977311551570892333984375"
            }
        ],
        "nextPageOffsetData": "0880A08A97B532"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597585432",
    "responseTime": "1734597586672",
    "traceId": "02465a59be5d19088ba7e4b5c6b94f6d"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                      |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatafundingrate>) |

## Data Models

#### pagedatafundingrate

| Name         | Type                                              | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------------------- | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                                            | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | [PageDataFundingRate](#schemapagedatafundingrate) | false    | none        | General pagination response                                     |
| errorParam   | object                                            | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                                 | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                                 | false    | none        | Server response time                                            |
| traceId      | string                                            | false    | none        | Call trace ID                                                   |

#### schemapagedatafundingrate

| Name               | Type                                 | Required | Constraints | Description                                                                  |
| ------------------ | ------------------------------------ | -------- | ----------- | ---------------------------------------------------------------------------- |
| dataList           | \[[FundingRate](#schemafundingrate)] | false    | none        | Data list                                                                    |
| nextPageOffsetData | string                               | false    | none        | Offset data to retrieve the next page. Empty string if there is no next page |

#### listfundingrate

| Name         | Type                                 | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------ | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                               | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | \[[FundingRate](#schemafundingrate)] | false    | none        | Successful response data                                        |
| errorParam   | object                               | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                    | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                    | false    | none        | Server response time                                            |
| traceId      | string                               | false    | none        | Call trace ID                                                   |

#### schemafundingrate

| Name                     | Type          | Required | Constraints | Description                                                                                                                                                                            |
| ------------------------ | ------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId               | string(int64) | false    | none        | Contract ID                                                                                                                                                                            |
| fundingTime              | string(int64) | false    | none        | Funding rate settlement time. E.g., the funding rate for the 08:00-09:00 period is calculated from the previous 07:00-08:00 data, finalized at 08:00, and used for settlement at 09:00 |
| fundingTimestamp         | string(int64) | false    | none        | Funding rate calculation time in milliseconds                                                                                                                                          |
| oraclePrice              | string        | false    | none        | Oracle price                                                                                                                                                                           |
| indexPrice               | string        | false    | none        | Index price                                                                                                                                                                            |
| fundingRate              | string        | false    | none        | Funding rate                                                                                                                                                                           |
| isSettlement             | boolean       | false    | none        | Funding rate settlement flag                                                                                                                                                           |
| forecastFundingRate      | string        | false    | none        | Forecast funding rate                                                                                                                                                                  |
| previousFundingRate      | string        | false    | none        | Previous funding rate                                                                                                                                                                  |
| previousFundingTimestamp | string(int64) | false    | none        | Previous funding rate calculation time in milliseconds                                                                                                                                 |
| premiumIndex             | string        | false    | none        | Premium index                                                                                                                                                                          |
| avgPremiumIndex          | string        | false    | none        | Average premium index                                                                                                                                                                  |
| premiumIndexTimestamp    | string        | false    | none        | Premium index calculation time                                                                                                                                                         |
| impactMarginNotional     | string        | false    | none        | Quantity required for deep weighted buy/sell price calculation                                                                                                                         |
| impactAskPrice           | string        | false    | none        | Deep weighted ask price                                                                                                                                                                |
| impactBidPrice           | string        | false    | none        | Deep weighted bid price                                                                                                                                                                |
| interestRate             | string        | false    | none        | Fixed interest rate                                                                                                                                                                    |
| predictedFundingRate     | string        | false    | none        | Comprehensive interest rate (interestRate/frequency)                                                                                                                                   |
| fundingRateIntervalMin   | string(int64) | false    | none        | Funding rate time interval in minutes                                                                                                                                                  |
| starkExFundingIndex      | string        | false    | none        | StarkEx funding index                                                                                                                                                                  |





# Funding API

## FundingPublicApi

### GET Get Latest Funding Rate by Contract ID

GET /api/v1/public/funding/getLatestFundingRate

#### Request Parameters

| Name       | Location | Type   | Required | Description |
| ---------- | -------- | ------ | -------- | ----------- |
| contractId | query    | string | No       | Contract ID |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "contractId": "10000001",
            "fundingTime": "1734595200000",
            "fundingTimestamp": "1734597720000",
            "oraclePrice": "101559.9220921285450458526611328125",
            "indexPrice": "101522.558968500",
            "fundingRate": "-0.00005537",
            "isSettlement": false,
            "forecastFundingRate": "-0.00012293",
            "previousFundingRate": "0.00000567",
            "previousFundingTimestamp": "1734595140000",
            "premiumIndex": "-0.00036207",
            "avgPremiumIndex": "-0.00032293",
            "premiumIndexTimestamp": "1734597720000",
            "impactMarginNotional": "100",
            "impactAskPrice": "101485.8",
            "impactBidPrice": "101484.7",
            "interestRate": "0.0003",
            "predictedFundingRate": "0.00005000",
            "fundingRateIntervalMin": "240",
            "starkExFundingIndex": "101559.9220921285450458526611328125"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597737870",
    "responseTime": "1734597737873",
    "traceId": "5e27ebfb0ae79f51bbd347d2bf3585f9"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#schemapagedatafundingrate>) |

### GET Get Funding Rate History by Contract ID with Pagination

GET /api/v1/public/funding/getFundingRatePage

#### Request Parameters

| Name                        | Location | Type   | Required | Description                                                                                                                                        |
| --------------------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId                  | query    | string | No       | Contract ID                                                                                                                                        |
| size                        | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100                                                                  |
| offsetData                  | query    | string | No       | Pagination offset. If not provided or empty, retrieves the first page                                                                              |
| filterSettlementFundingRate | query    | string | No       | If true, only query settlement funding rates (funding rate settlement occurs every 8 hours, with a predicted funding rate calculated every minute) |
| filterBeginTimeInclusive    | query    | string | No       | Start time. If not provided, retrieves the oldest data                                                                                             |
| filterEndTimeExclusive      | query    | string | No       | End time. If not provided, retrieves the latest data                                                                                               |

> Example Response

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "contractId": "10000001",
                "fundingTime": "1733702400000",
                "fundingTimestamp": "1733702400000",
                "oraclePrice": "101120.888977311551570892333984375",
                "indexPrice": "101121.681521500",
                "fundingRate": "0.00005000",
                "isSettlement": true,
                "forecastFundingRate": "",
                "previousFundingRate": "0.00005000",
                "previousFundingTimestamp": "1733702340000",
                "premiumIndex": "0.00022566",
                "avgPremiumIndex": "0.00017953",
                "premiumIndexTimestamp": "1733702400000",
                "impactMarginNotional": "500",
                "impactAskPrice": "101269.6",
                "impactBidPrice": "101269.1",
                "interestRate": "0.0003",
                "predictedFundingRate": "0.00005000",
                "fundingRateIntervalMin": "240",
                "starkExFundingIndex": "101120.888977311551570892333984375"
            }
        ],
        "nextPageOffsetData": "0880A08A97B532"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734597585432",
    "responseTime": "1734597586672",
    "traceId": "02465a59be5d19088ba7e4b5c6b94f6d"
}
```

#### Response Codes

| Status Code | Status Code Description                                 | Description      | Data Model                      |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatafundingrate>) |

## Data Models

#### pagedatafundingrate

| Name         | Type                                              | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------------------- | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                                            | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | [PageDataFundingRate](#schemapagedatafundingrate) | false    | none        | General pagination response                                     |
| errorParam   | object                                            | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                                 | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                                 | false    | none        | Server response time                                            |
| traceId      | string                                            | false    | none        | Call trace ID                                                   |

#### schemapagedatafundingrate

| Name               | Type                                 | Required | Constraints | Description                                                                  |
| ------------------ | ------------------------------------ | -------- | ----------- | ---------------------------------------------------------------------------- |
| dataList           | \[[FundingRate](#schemafundingrate)] | false    | none        | Data list                                                                    |
| nextPageOffsetData | string                               | false    | none        | Offset data to retrieve the next page. Empty string if there is no next page |

#### listfundingrate

| Name         | Type                                 | Required | Constraints | Description                                                     |
| ------------ | ------------------------------------ | -------- | ----------- | --------------------------------------------------------------- |
| code         | string                               | false    | none        | Status code. "SUCCESS" for success, otherwise indicates failure |
| data         | \[[FundingRate](#schemafundingrate)] | false    | none        | Successful response data                                        |
| errorParam   | object                               | false    | none        | Parameter information in the error message                      |
| requestTime  | string(timestamp)                    | false    | none        | Server request reception time                                   |
| responseTime | string(timestamp)                    | false    | none        | Server response time                                            |
| traceId      | string                               | false    | none        | Call trace ID                                                   |

#### schemafundingrate

| Name                     | Type          | Required | Constraints | Description                                                                                                                                                                            |
| ------------------------ | ------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contractId               | string(int64) | false    | none        | Contract ID                                                                                                                                                                            |
| fundingTime              | string(int64) | false    | none        | Funding rate settlement time. E.g., the funding rate for the 08:00-09:00 period is calculated from the previous 07:00-08:00 data, finalized at 08:00, and used for settlement at 09:00 |
| fundingTimestamp         | string(int64) | false    | none        | Funding rate calculation time in milliseconds                                                                                                                                          |
| oraclePrice              | string        | false    | none        | Oracle price                                                                                                                                                                           |
| indexPrice               | string        | false    | none        | Index price                                                                                                                                                                            |
| fundingRate              | string        | false    | none        | Funding rate                                                                                                                                                                           |
| isSettlement             | boolean       | false    | none        | Funding rate settlement flag                                                                                                                                                           |
| forecastFundingRate      | string        | false    | none        | Forecast funding rate                                                                                                                                                                  |
| previousFundingRate      | string        | false    | none        | Previous funding rate                                                                                                                                                                  |
| previousFundingTimestamp | string(int64) | false    | none        | Previous funding rate calculation time in milliseconds                                                                                                                                 |
| premiumIndex             | string        | false    | none        | Premium index                                                                                                                                                                          |
| avgPremiumIndex          | string        | false    | none        | Average premium index                                                                                                                                                                  |
| premiumIndexTimestamp    | string        | false    | none        | Premium index calculation time                                                                                                                                                         |
| impactMarginNotional     | string        | false    | none        | Quantity required for deep weighted buy/sell price calculation                                                                                                                         |
| impactAskPrice           | string        | false    | none        | Deep weighted ask price                                                                                                                                                                |
| impactBidPrice           | string        | false    | none        | Deep weighted bid price                                                                                                                                                                |
| interestRate             | string        | false    | none        | Fixed interest rate                                                                                                                                                                    |
| predictedFundingRate     | string        | false    | none        | Comprehensive interest rate (interestRate/frequency)                                                                                                                                   |
| fundingRateIntervalMin   | string(int64) | false    | none        | Funding rate time interval in minutes                                                                                                                                                  |
| starkExFundingIndex      | string        | false    | none        | StarkEx funding index                                                                                                                                                                  |




# Withdraw API

## WithdrawPrivateApi

### GET Get Withdrawals By Withdraw ID

GET /api/v1/private/withdraw/getWithdrawById

#### Request Parameters

| Name           | Location | Type   | Required | Description                                                                         |
| -------------- | -------- | ------ | -------- | ----------------------------------------------------------------------------------- |
| accountId      | query    | string | Yes      | Account ID                                                                          |
| withdrawIdList | query    | string | Yes      | List of withdraw IDs to retrieve. Used to batch fetch withdraw records by their IDs |

> Response Example

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "id": "563516408235819790",
            "userId": "543429922866069763",
            "accountId": "543429922991899150",
            "coinId": "1000",
            "amount": "10.000000",
            "ethAddress": "0x1fB51aa234287C3CA1F957eA9AD0E148Bb814b7A",
            "erc20Address": "0x...",
            "clientWithdrawId": "client_withdraw_123",
            "riskSignature": {
                "r": "0x...",
                "s": "0x...",
                "v": "0x..."
            },
            "l2Nonce": "123456789",
            "l2ExpireTime": "1734352781355",
            "l2Signature": {
                "r": "0x...",
                "s": "0x...",
                "v": "0x..."
            },
            "extraType": "",
            "extraDataJson": "",
            "status": "SUCCESS_L2_APPROVED",
            "collateralTransactionId": "563516408265179918",
            "censorTxId": "830852",
            "censorTime": "1734352781355",
            "censorFailCode": "",
            "censorFailReason": "",
            "l2TxId": "1022403",
            "l2RejectTime": "0",
            "l2RejectCode": "",
            "l2RejectReason": "",
            "l2ApprovedTime": "1734353551654",
            "createdTime": "1734352781355",
            "updatedTime": "1734353551715"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734664486740",
    "responseTime": "1734664486761",
    "traceId": "b3086f53c2d4503f6a4790b80f0e534b"
}
```

#### Response

| Status Code | Status Code Description                                 | Description      | Data Model              |
| ----------- | ------------------------------------------------------- | ---------------- | ----------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#withdrawlist) |

### GET Get Withdrawals By Client Withdraw ID

GET /api/v1/private/withdraw/getWithdrawByClientWithdrawId

#### Request Parameters

| Name                 | Location | Type   | Required | Description                                                                                       |
| -------------------- | -------- | ------ | -------- | ------------------------------------------------------------------------------------------------- |
| accountId            | query    | string | Yes      | Account ID                                                                                        |
| clientWithdrawIdList | query    | string | Yes      | List of client-defined withdraw IDs. Used to batch fetch withdraw records by client-specified IDs |

> Response Example

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": [
        {
            "id": "563516408235819790",
            "userId": "543429922866069763",
            "accountId": "543429922991899150",
            "coinId": "1000",
            "amount": "10.000000",
            "ethAddress": "0x1fB51aa234287C3CA1F957eA9AD0E148Bb814b7A",
            "erc20Address": "0x...",
            "clientWithdrawId": "client_withdraw_123",
            "riskSignature": {
                "r": "0x...",
                "s": "0x...",
                "v": "0x..."
            },
            "l2Nonce": "123456789",
            "l2ExpireTime": "1734352781355",
            "l2Signature": {
                "r": "0x...",
                "s": "0x...",
                "v": "0x..."
            },
            "extraType": "",
            "extraDataJson": "",
            "status": "SUCCESS_L2_APPROVED",
            "collateralTransactionId": "563516408265179918",
            "censorTxId": "830852",
            "censorTime": "1734352781355",
            "censorFailCode": "",
            "censorFailReason": "",
            "l2TxId": "1022403",
            "l2RejectTime": "0",
            "l2RejectCode": "",
            "l2RejectReason": "",
            "l2ApprovedTime": "1734353551654",
            "createdTime": "1734352781355",
            "updatedTime": "1734353551715"
        }
    ],
    "msg": null,
    "errorParam": null,
    "requestTime": "1734664486740",
    "responseTime": "1734664486761",
    "traceId": "b3086f53c2d4503f6a4790b80f0e534b"
}
```

#### Response

| Status Code | Status Code Description                                 | Description      | Data Model              |
| ----------- | ------------------------------------------------------- | ---------------- | ----------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#withdrawlist) |

### GET Get Active Withdrawals with Pagination

GET /api/v1/private/withdraw/getActiveWithdraw

#### Request Parameters

| Name                            | Location | Type   | Required | Description                                                                                                                                 |
| ------------------------------- | -------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| accountId                       | query    | string | Yes      | Account ID                                                                                                                                  |
| size                            | query    | string | No       | Number of items to retrieve. Must be greater than 0 and less than or equal to 100. Default: 100                                             |
| offsetData                      | query    | string | No       | Pagination offset. If empty or not provided, the first page is retrieved                                                                    |
| filterCoinIdList                | query    | string | No       | Filter withdrawals by specified coin IDs. If not provided, all coin withdrawals are retrieved                                               |
| filterStatusList                | query    | string | No       | Filter withdrawals by specified statuses. If not provided, all status withdrawals are retrieved                                             |
| filterStartCreatedTimeInclusive | query    | string | No       | Filter withdrawals created after or at the specified start time (inclusive). If not provided or 0, retrieves records from the earliest time |
| filterEndCreatedTimeExclusive   | query    | string | No       | Filter withdrawals created before the specified end time (exclusive). If not provided or 0, retrieves records up to the latest time         |

> Response Example

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "dataList": [
            {
                "id": "563516408235819790",
                "userId": "543429922866069763",
                "accountId": "543429922991899150",
                "coinId": "1000",
                "amount": "10.000000",
                "ethAddress": "0x1fB51aa234287C3CA1F957eA9AD0E148Bb814b7A",
                "erc20Address": "0x...",
                "clientWithdrawId": "client_withdraw_123",
                "riskSignature": {
                    "r": "0x...",
                    "s": "0x...",
                    "v": "0x..."
                },
                "l2Nonce": "123456789",
                "l2ExpireTime": "1734352781355",
                "l2Signature": {
                    "r": "0x...",
                    "s": "0x...",
                    "v": "0x..."
                },
                "extraType": "",
                "extraDataJson": "",
                "status": "SUCCESS_L2_APPROVED",
                "collateralTransactionId": "563516408265179918",
                "censorTxId": "830852",
                "censorTime": "1734352781355",
                "censorFailCode": "",
                "censorFailReason": "",
                "l2TxId": "1022403",
                "l2RejectTime": "0",
                "l2RejectCode": "",
                "l2RejectReason": "",
                "l2ApprovedTime": "1734353551654",
                "createdTime": "1734352781355",
                "updatedTime": "1734353551715"
            }
        ],
        "nextPageOffsetData": ""
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734664486740",
    "responseTime": "1734664486761",
    "traceId": "b3086f53c2d4503f6a4790b80f0e534b"
}
```

#### Response

| Status Code | Status Code Description                                 | Description      | Data Model                  |
| ----------- | ------------------------------------------------------- | ---------------- | --------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#pagedatawithdraw) |

### GET Get Withdraw Available Amount

GET /api/v1/private/withdraw/getWithdrawAvailableAmount

#### Request Parameters

| Name      | Location | Type   | Required | Description                                  |
| --------- | -------- | ------ | -------- | -------------------------------------------- |
| accountId | query    | string | Yes      | Account ID                                   |
| coinId    | query    | string | Yes      | Coin ID to check available withdrawal amount |

> Response Example

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "availableAmount": "100.000000"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734664486740",
    "responseTime": "1734664486761",
    "traceId": "b3086f53c2d4503f6a4790b80f0e534b"
}
```

#### Response

| Status Code | Status Code Description                                 | Description      | Data Model                            |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#getwithdrawavailableamount) |

### POST Create Withdraw

POST /api/v1/private/withdraw/createWithdraw

#### Request Parameters

| Name             | Location | Type   | Required | Description                                                                                                                |
| ---------------- | -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| accountId        | body     | string | Yes      | Account ID                                                                                                                 |
| coinId           | body     | string | Yes      | Currency ID                                                                                                                |
| amount           | body     | string | Yes      | Withdraw amount (decimal format)                                                                                           |
| ethAddress       | body     | string | Yes      | Ethereum address for the withdrawal                                                                                        |
| erc20Address     | body     | string | Yes      | ERC20 token contract address                                                                                               |
| clientWithdrawId | body     | string | Yes      | Client-defined ID for idempotency verification                                                                             |
| riskSignature    | body     | string | Yes      | Risk control signature (128 characters fixed length)                                                                       |
| l2Nonce          | body     | string | Yes      | L2 signature nonce. First 32 bits of sha256(client\_withdraw\_id)                                                          |
| l2ExpireTime     | body     | string | Yes      | L2 signature expiration time in milliseconds. For signature generation/verification, use hours: l2\_expire\_time / 3600000 |
| l2Signature      | body     | string | Yes      | L2 signature submitted (128 characters fixed length)                                                                       |
| extraType        | body     | string | Yes      | Additional type for upper-layer business use                                                                               |
| extraDataJson    | body     | string | No       | Extra data in JSON format, defaults to empty string                                                                        |

#### Request Body Schema

```json
{
    "accountId": "543429922991899150",
    "coinId": "1000",
    "amount": "10.000000",
    "ethAddress": "0x1fB51aa234287C3CA1F957eA9AD0E148Bb814b7A",
    "erc20Address": "0x...",
    "clientWithdrawId": "client_withdraw_123",
    "riskSignature": "0x...",
    "l2Nonce": "123456789",
    "l2ExpireTime": "1734352781355",
    "l2Signature": "0x...",
    "extraType": "",
    "extraDataJson": ""
}
```

> Response Example

> 200 Response

```json
{
    "code": "SUCCESS",
    "data": {
        "withdrawId": "563516408235819790"
    },
    "msg": null,
    "errorParam": null,
    "requestTime": "1734664486740",
    "responseTime": "1734664486761",
    "traceId": "b3086f53c2d4503f6a4790b80f0e534b"
}
```

#### Response

| Status Code | Status Code Description                                 | Description      | Data Model                |
| ----------- | ------------------------------------------------------- | ---------------- | ------------------------- |
| 200         | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | default response | [Result](#createwithdraw) |

## Data Models

#### WithdrawList

| Name         | Type                               | Required | Constraints | Description          | Notes                                                          |
| ------------ | ---------------------------------- | -------- | ----------- | -------------------- | -------------------------------------------------------------- |
| code         | string                             | false    | none        | Status Code          | Returns "SUCCESS" on success; otherwise, it indicates failure. |
| data         | [WithdrawModel](#withdrawmodel)\[] | false    | none        | Withdraw List        | Array of withdraw records                                      |
| errorParam   | object                             | false    | none        | Error Parameters     | Error message parameter information                            |
| requestTime  | string(timestamp)                  | false    | none        | Server Request Time  | Time at which the server received the request                  |
| responseTime | string(timestamp)                  | false    | none        | Server Response Time | Time at which the server sent the response                     |
| traceId      | string                             | false    | none        | Trace ID             | Invocation trace ID                                            |

#### PageDataWithdraw

| Name               | Type                               | Required | Constraints | Description      | Notes                                                                    |
| ------------------ | ---------------------------------- | -------- | ----------- | ---------------- | ------------------------------------------------------------------------ |
| dataList           | [WithdrawModel](#withdrawmodel)\[] | false    | none        | Data List        | Array of withdraw records                                                |
| nextPageOffsetData | string                             | false    | none        | Next Page Offset | Offset for retrieving the next page. If no next page data, empty string. |

#### WithdrawModel

| Name                    | Type                                  | Required | Constraints | Description               | Notes                                                                                                            |
| ----------------------- | ------------------------------------- | -------- | ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| id                      | string(int64)                         | false    | none        | Withdraw ID               | Unique identifier for the withdraw record                                                                        |
| userId                  | string(int64)                         | false    | none        | User ID                   | ID of the owning user                                                                                            |
| accountId               | string(int64)                         | false    | none        | Account ID                | ID of the owning account                                                                                         |
| coinId                  | string(int64)                         | false    | none        | Coin ID                   | ID of the collateral coin                                                                                        |
| amount                  | string                                | false    | none        | Withdraw Amount           | Amount of the withdrawal                                                                                         |
| ethAddress              | string                                | false    | none        | Ethereum Address          | Ethereum address for the withdrawal                                                                              |
| erc20Address            | string                                | false    | none        | ERC20 Contract Address    | Contract address of the withdrawn token                                                                          |
| clientWithdrawId        | string                                | false    | none        | Client Withdraw ID        | Client-defined ID for idempotency verification                                                                   |
| riskSignature           | [L2SignatureModel](#l2signaturemodel) | false    | none        | Risk Signature            | Risk control signature                                                                                           |
| l2Nonce                 | string(int64)                         | false    | none        | L2 Nonce                  | L2 signature nonce. First 32 bits of sha256(client\_withdraw\_id)                                                |
| l2ExpireTime            | string(int64)                         | false    | none        | L2 Expire Time            | L2 signature expiration time in milliseconds                                                                     |
| l2Signature             | [L2SignatureModel](#l2signaturemodel) | false    | none        | L2 Signature              | L2 signature submitted                                                                                           |
| extraType               | string                                | false    | none        | Extra Type                | Additional type for upper-layer business use                                                                     |
| extraDataJson           | string                                | false    | none        | Extra Data JSON           | Extra data in JSON format                                                                                        |
| status                  | string                                | false    | none        | Withdraw Status           | Current status of the withdrawal                                                                                 |
| collateralTransactionId | string(int64)                         | false    | none        | Collateral Transaction ID | Associated collateral transaction ID when status is SUCCESS\_XXX/FAILED\_L2\_REJECT/FAILED\_L2\_REJECT\_APPROVED |
| censorTxId              | string(int64)                         | false    | none        | Censor Transaction ID     | Censorship processing sequence number when status is SUCCESS\_XXX/FAILED\_XXX                                    |
| censorTime              | string(int64)                         | false    | none        | Censor Time               | Censorship processing time when status is SUCCESS\_XXX/FAILED\_XXX                                               |
| censorFailCode          | string                                | false    | none        | Censor Fail Code          | Censorship failure code                                                                                          |
| censorFailReason        | string                                | false    | none        | Censor Fail Reason        | Censorship failure reason                                                                                        |
| l2TxId                  | string(int64)                         | false    | none        | L2 Transaction ID         | Layer 2 transaction ID                                                                                           |
| l2RejectTime            | string(int64)                         | false    | none        | L2 Reject Time            | Layer 2 rejection time                                                                                           |
| l2RejectCode            | string                                | false    | none        | L2 Reject Code            | Layer 2 rejection code                                                                                           |
| l2RejectReason          | string                                | false    | none        | L2 Reject Reason          | Layer 2 rejection reason                                                                                         |
| l2ApprovedTime          | string(int64)                         | false    | none        | L2 Approved Time          | Layer 2 approval time                                                                                            |
| createdTime             | string(int64)                         | false    | none        | Created Time              | Record creation time                                                                                             |
| updatedTime             | string(int64)                         | false    | none        | Updated Time              | Record last update time                                                                                          |

#### L2SignatureModel

| Name | Type   | Required | Constraints | Description           | Notes                            |
| ---- | ------ | -------- | ----------- | --------------------- | -------------------------------- |
| r    | string | false    | none        | Signature R Component | Bigint represented as hex string |
| s    | string | false    | none        | Signature S Component | Bigint represented as hex string |
| v    | string | false    | none        | Signature V Component | Bigint represented as hex string |

#### GetWithdrawAvailableAmount

| Name         | Type                                                                | Required | Constraints | Description               | Notes                                                          |
| ------------ | ------------------------------------------------------------------- | -------- | ----------- | ------------------------- | -------------------------------------------------------------- |
| code         | string                                                              | false    | none        | Status Code               | Returns "SUCCESS" on success; otherwise, it indicates failure. |
| data         | [GetWithdrawAvailableAmountModel](#getwithdrawavailableamountmodel) | false    | none        | Available Amount Response | Response data for available withdrawal amount                  |
| errorParam   | object                                                              | false    | none        | Error Parameters          | Error message parameter information                            |
| requestTime  | string(timestamp)                                                   | false    | none        | Server Request Time       | Time at which the server received the request                  |
| responseTime | string(timestamp)                                                   | false    | none        | Server Response Time      | Time at which the server sent the response                     |
| traceId      | string                                                              | false    | none        | Trace ID                  | Invocation trace ID                                            |

#### GetWithdrawAvailableAmountModel

| Name            | Type   | Required | Constraints | Description      | Notes                                            |
| --------------- | ------ | -------- | ----------- | ---------------- | ------------------------------------------------ |
| availableAmount | string | false    | none        | Available Amount | Available amount for withdrawal (decimal format) |

#### CreateWithdraw

| Name         | Type                                        | Required | Constraints | Description              | Notes                                                          |
| ------------ | ------------------------------------------- | -------- | ----------- | ------------------------ | -------------------------------------------------------------- |
| code         | string                                      | false    | none        | Status Code              | Returns "SUCCESS" on success; otherwise, it indicates failure. |
| data         | [CreateWithdrawModel](#createwithdrawmodel) | false    | none        | Create Withdraw Response | Response data for withdraw creation                            |
| errorParam   | object                                      | false    | none        | Error Parameters         | Error message parameter information                            |
| requestTime  | string(timestamp)                           | false    | none        | Server Request Time      | Time at which the server received the request                  |
| responseTime | string(timestamp)                           | false    | none        | Server Response Time     | Time at which the server sent the response                     |
| traceId      | string                                      | false    | none        | Trace ID                 | Invocation trace ID                                            |

#### CreateWithdrawModel

| Name       | Type          | Required | Constraints | Description | Notes                             |
| ---------- | ------------- | -------- | ----------- | ----------- | --------------------------------- |
| withdrawId | string(int64) | false    | none        | Withdraw ID | ID of the created withdraw record |




# Websocket API

### WebSocket API Documentation

This document outlines the WebSocket API for both private (user account) and public (market data) information.

### (Private WebSocket) User Account Information WebSocket Interface

#### Description

* **01.** Private WebSocket connections do not require subscriptions; data is automatically pushed after a successful connection. This includes both trading messages and custom messages.
* **02.** Trading messages are identified with the type `type-event`. Other message types will be defined separately.
* **03.** The `event` field within the body of a trading message can be one of the following: `Snapshot`, `ACCOUNT_UPDATE`, `DEPOSIT_UPDATE`, `WITHDRAW_UPDATE`, `TRANSFER_IN_UPDATE`, `TRANSFER_OUT_UPDATE`, `ORDER_UPDATE`, `FORCE_WITHDRAW_UPDATE`, `FORCE_TRADE_UPDATE`, `FUNDING_SETTLEMENT`, `ORDER_FILL_FEE_INCOME`, `START_LIQUIDATING`, `FINISH_LIQUIDATING`, or `UNRECOGNIZED`.
* **04.** Ping-Pong Mechanism:
  * **Server Ping (Heartbeat):**
    * After a successful WebSocket connection, the server sends a Ping message at a fixed interval. The message body looks like: `{"type":"ping","time":"1693208170000"}`. The `time` field is the server's timestamp when the Ping was sent.
    * The client must respond with a Pong message upon receipt, with a body like: `{"type":"pong","time":"1693208170000"}`.
    * If the server doesn't receive a Pong response after 5 consecutive Pings, the server will terminate the connection.
  * **Client Ping (Latency Measurement):**
    * After a successful WebSocket connection, the client can also initiate a Ping message with a body like: `{"type":"ping","time":"1693208170000"}`. The `time` field is the client's timestamp when the Ping was sent.
    * The server will immediately respond with a Pong message, with a body like: `{"type":"pong","time":"1693208170000"}`. The `time` field in the Pong will match the `time` field in the client's Ping.
* **05.** Authentication:
  * **Web:**
    * Browsers don't allow custom headers during WebSocket connections, so special handling is required.
    * Use the same authentication logic as HTTP. Create a JSON string using the `X-edgeX-Api-Signature`, `X-edgeX-Api-Timestamp` key-value pairs, for example: `{"X-edgeX-Api-Signature": "00e6b34cf9c3c0ca407cc2fe149fad836206c97201f236137c0e89fd079760470672b5257fa372710b5863d1ec6e0215e5bd6b2c3a319eda88886250a100524706ea3dd81a7fc864893c8c6f674e4a4510c369f939bdc0259a0980dfde882c2d", "X-edgeX-Api-Timestamp": "1705720068228"}`.
    * Base64 encode this JSON string.
    * During the WebSocket request, pass the base64 encoded value in the `SEC_WEBSOCKET_PROTOCOL` header.
  * **App/API:**
    * App/API WebSocket connections can use [custom](https://edgex-1.gitbook.io/edgeX-documentation/authentication#private-api) headers. Therefore, Apps/API can continue using the same authentication logic as HTTP, or they can use the Web authentication method described above.
    * WebSocket is a GET request and there is no need to sign the request body.

#### URL: `/api/v1/private/ws`

**Payload**

```json
{
  // The type for trading messages is "trade-event". Custom messages have their own defined type. "error" indicates an error message sent by the server.
  "type": "trade-event",
  // The body of a trading message has the structure below. The message structure for custom messages will be defined separately by the user.
  "content": {
    // The event that triggered the data update
    "event": "ACCOUNT_UPDATE",
    // Data update version
    "version": "1000",
    // Data
    "data": {
      // Account information
      "account": [
      ],
      // Collateral information
      "collateral": [
      ],
      // Collateral transaction details
      "collateralTransaction": [
      ],
      // Position information
      "position": [
      ],
      // Position transaction details
      "positionTransaction": [
      ],
       // Deposit records
      "deposit": [
      ],
      // Withdrawal records
      "withdraw": [
      ],
      // Transfer in records
      "transferIn": [
      ],
      // Transfer out records
      "transferOut": [
      ],
      // Order information
      "order": [
      ],
      // Trade details
      "orderFillTransaction": [
      ]
    }
  }
}
```

### (Public WebSocket) Market Data WebSocket Interface

#### URL: `/api/v1/public/ws`

#### Description

* **01.** When subscribing or unsubscribing, the server will validate the channel. For invalid channels, the server will respond with an error message, for example: `{"type":"error","content":{"code":"INVALID_CONTRACT_ID""msg":"invalid contractId:100000001"}}`
* **02.** The message structure for subscribing and unsubscribing is: `{"type": "subscribe", "channel": "ticker.10000001"}`.
* **03.** Ping-Pong Mechanism:
  * **Server Ping (Heartbeat):**
    * After a successful WebSocket connection, the server sends a Ping message at a fixed interval. The message body looks like: `{"type":"ping","time":"1693208170000"}`. The `time` field is the server's timestamp when the Ping was sent.
    * The client must respond with a Pong message upon receipt, with a body like: `{"type":"pong","time":"1693208170000"}`.
    * If the server doesn't receive a Pong response after 5 consecutive Pings, the server will terminate the connection.
  * **Client Ping (Latency Measurement):**
    * After a successful WebSocket connection, the client can also initiate a Ping message with a body like: `{"type":"ping","time":"1693208170000"}`. The `time` field is the client's timestamp when the Ping was sent.
    * The server will immediately respond with a Pong message, with a body like: `{"type":"pong","time":"1693208170000"}`. The `time` field in the Pong will match the `time` field in the client's Ping.

#### Subscription Metadata

**Request**

```json
{
  "type": "subscribe",
  "channel": "metadata"
}
```

**Response**

```json
{
  "type": "subscribed",
  "channel": "metadata"
}
```

**Payload**

```json
{
  // error
  "type":  "quote-event",
  "channel": "metadata",
  "content": {
    // snapshot quote-event 
    "dataType": "Snapshot", 
    // 
    "channel": "metadata",
    "data": [
      {
        // Coin information
        "coin": [
        ],
        // Contract information
        "contract": [
        ]
      }
    ]
  }
}
```

#### Subscribe to 24-Hour Market Ticker

**Channel Explanation**

| Channel             | Description                                              |
| ------------------- | -------------------------------------------------------- |
| ticker.{contractId} | Subscribe to the ticker of contract `contractId`         |
| ticker.all          | Subscribe to the ticker of all contracts                 |
| ticker.all.1s       | Subscribe to the ticker of all contracts (periodic push) |

**Request**

```json
{
  "type": "subscribe",
  "channel": "ticker.10000001"
}
```

**Response**

```json
{
  "type": "subscribed",
  "channel": "ticker.10000001"
}
```

**Payload**

```json
{
  "type": "payload",
  "channel": "ticker.10000001",
  "content": {
    "dataType": "Snapshot",
    "channel": "ticker.10000001",
    "data": [
      {
        "contractId": "string",
        "priceChange": "string",
        "priceChangePercent": "string",
        "trades": "string",
        "size": "string",
        "value": "string",
        "high": "string",
        "low": "string",
        "open": "string",
        "close": "string",
        "highTime": "string",
        "lowTime": "string",
        "startTime": "string",
        "endTime": "string",
        "lastPrice": "string"
      }
    ]
  }
}
```

#### Subscribe to K-Line Data

**Channel Explanation**

| Channel                                   | Description                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------- |
| kline.{priceType}.{contractId}.{interval} | Subscribe to the `interval` K-Line of contract `contractId` based on `priceType` |

**`priceType` Parameter**

| Value       | Description       |
| ----------- | ----------------- |
| LAST\_PRICE | Last Price K-Line |
| MARK\_PRICE | Mark Price K-Line |

**`interval` Parameter**

| Value      | Description      |
| ---------- | ---------------- |
| MINUTE\_1  | 1-Minute K-Line  |
| MINUTE\_5  | 5-Minute K-Line  |
| MINUTE\_15 | 15-Minute K-Line |
| MINUTE\_30 | 30-Minute K-Line |
| HOUR\_1    | 1-Hour K-Line    |
| HOUR\_2    | 2-Hour K-Line    |
| HOUR\_4    | 4-Hour K-Line    |
| HOUR\_6    | 6-Hour K-Line    |
| HOUR\_8    | 8-Hour K-Line    |
| HOUR\_12   | 12-Hour K-Line   |
| DAY\_1     | Daily K-Line     |
| WEEK\_1    | Weekly K-Line    |
| MONTH\_1   | Monthly K-Line   |

**Request**

```json
{
  "type": "subscribe",
  "channel": "kline.LAST_PRICE.10000001.MINUTE_1"
}
```

**Response**

```json
{
  "type": "subscribed",
  "channel": "kline.LAST_PRICE.10000001.MINUTE_1"
}
```

**Payload**

```json
{
  "type": "payload",
  "channel": "kline.LAST_PRICE.10000001.MINUTE_1",
  "content": {
    "dataType": "Changed",
    "channel": "kline.LAST_PRICE.10000001.MINUTE_1",
    "data": [
      {
        "klineId": "1",
        "contractId": "10000001",
        "klineType": "MINUTE_1",
        "klineTime": "1688365544504",
        "trades": "5",
        "size": "10.1",
        "value": "100000",
        "high": "31200",
        "low": "31000",
        "open": "3150",
        "close": "31010",
        "makerBuySize": "5",
        "makerBuyValue": "150000"
      }
    ]
  }
}
```

#### Subscribe to Order Book

**Usage Instructions**

> After a successful subscription, a full dataset is pushed once initially (`depthType=SNAPSHOT`), and subsequent pushes will be incremental updates (`depthType=CHANGED`).

**Channel Explanation**

| Channel                    | Description                                                                  |
| -------------------------- | ---------------------------------------------------------------------------- |
| depth.{contractId}.{depth} | Subscribe to the order book of contract `contractId` with a depth of `depth` |

**`depth` Parameter**

| Value | Description |
| ----- | ----------- |
| 15    | 15 levels   |
| 200   | 200 levels  |

**Request**

```json
{
  "type": "subscribe",
  "channel": "depth.10000001.15"
}
```

**Response**

```json
{
  "type": "subscribed",
  "channel": "depth.10000001.15"
}
```

**Payload**

```json
{
  "type": "payload",
  "channel": "depth.10000001.15",
  "content": {
    "dataType": "Snapshot",
    "channel": "depth.10000001.15",
    "data": [
      {
        "startVersion": "string",
        "endVersion": "string",
        "level": 0,
        "contractId": "10000001",
        "depthType": "Snapshot", // Data type: SNAPSHOT for full data, CHANGED for incremental data
        "bids": [
          [
            "26092",
            // Price
            "0.9014"
            // Size. A size of 0 indicates a deletion. Positive numbers mean increase. Negative numbers mean decrease.
          ],
          [
            "26091",
            "0.9667"
          ]
        ],
        "asks": [
          [
            "26093",
            "0.964"
          ],
          [
            "26094",
            "1.0213"
          ]
        ]
      }
    ]
  }
}
```

#### Subscribe to Latest Trades

**Channel Explanation**

| Channel             | Description                                             |
| ------------------- | ------------------------------------------------------- |
| trades.{contractId} | Subscribe to the latest trades of contract `contractId` |

**Request**

```json
{
  "type": "subscribe",
  "channel": "trades.10000001"
}
```

**Response**

```json
{
  "type": "subscribed",
  "channel": "trades.10000001"
}
```

**Payload**

```json
{
  "type": "payload",
  "channel": "trades.10000001",
  "content": {
    "dataType": "Changed",
    "channel": "trades.10000001",
    "data": [
      {
        "ticketId": "1",
        "time": "1688365544504",
        "price": "30065.12",
        "size": "0.01",
        "value": "300.6512",
        "takerOrderId": "10",
        "makerOrderId": "11",
        "takerAccountId": "3001",
        "makerAccountId": "3002",
        "contractId": "10000001",
        "isBestMatch": true,
        "isBuyerMaker": false
      }
    ]
  }
}
```
