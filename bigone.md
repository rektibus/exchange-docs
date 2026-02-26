

Contract Error Codes
This page documents the specific error codes (anomaly keywords) returned by the BigONE Contract OpenAPI (/api/contract/v2/).

Error Response Format
Errors in the Contract API return a 400 or 403 HTTP status code with the following JSON structure:

{
  "anomaly": "anomaly.order/price-out-of-range"
}

The anomaly field contains a keyword identifying the specific business logic error.

Trading & Market Errors
Anomaly Keyword	Description
anomaly.trades/stopped	Trading is suspended for the platform.
anomaly.trades/suspended	Trading is suspended for the specific instrument.
Order Validation Errors
Anomaly Keyword	Description
anomaly.order/price-out-of-range	Order price is beyond the allowed price limits.
anomaly.open-order/price-invalid-loss	Stop loss price is invalid for the current market conditions.
anomaly.open-order/price-invalid-profit	Take profit price is invalid for the current market conditions.
anomaly.request/invalid-params	One or more request parameters are malformed or invalid.
Position & Account Errors
Anomaly Keyword	Description
anomaly.close-position/position-not-found	Attempted to close a position that does not exist.
anomaly.adjust-margin/invalid-lerverage	The requested leverage adjustment is invalid.
anomaly.adjust-margin/position-too-large	The position size exceeds the allowed limit for the requested margin.
anomaly.limit-risk/position-too-large	The position size exceeds the risk limit.
anomaly.adjust-risk-limit/too-small-or-too-large	Risk limit adjustment value is out of allowed range.




ontract WebSocket API
The Contract WebSocket API allows you to subscribe to real-time public market data and private user data updates.

The Contract API uses URL-based subscriptions for public channels and a single Authenticated Stream for private data.

Error Handling & Status Codes
Since subscriptions are URL-based, errors primarily occur during the connection handshake:

HTTP 101 Switching Protocols: Connection successful.
HTTP 401 Unauthorized: (Private Stream) Invalid or missing Authorization header.
HTTP 400 Bad Request: Invalid parameters in the URL.
HTTP 500 Internal Server Error: Server-side issue during connection.
If a connection is dropping or invalid after the handshake, the server will simply close the connection.

Public Channels
Public channels are accessed by connecting to specific WebSocket URLs. No authentication is required.

Market Depth (Order Book)
Push snapshot at first, and keep pushing real-time changes later.

URL
wss://api.big.one/ws/contract/v2/depth@{symbol}

Request Example
wscat -c wss://api.big.one/ws/contract/v2/depth@BTCUSD

Response Example (Snapshot)
{
    "to": 91277134,
    "bestPrices": {
        "ask": 11202.5,
        "bid": 11192.5
    },
    "lastPrice": 11183.5,
    "bids": {
        "11192": 35,
        "11184": 742,
        "11192.5": 389,
        "11188": 293
    },
    "asks": {
        "11202.5": 1806,
        "11212.5": 2138,
        "11211.5": 19308
    },
    "from": 0
}

Response Example (Real-time)
{
    "bids": {
        "11183": 3500
    },
    "lastPrice": 11183.5,
    "from": 91277135,
    "bestPrices": {
        "ask": 11202.5,
        "bid": 11192.5
    },
    "asks": {},
    "to": 91277135
}

Market Trades
Subscribe to real-time trade execution history.

URL
wss://api.big.one/ws/contract/v2/trades@{symbol}

Request Example
wscat -c wss://api.big.one/ws/contract/v2/trades@BTCUSD

Response Example (Snapshot)
[
    {
        "id": "5aefeab9-6840-0000-0001-0000056fe3c8",
        "symbol": "BTCUSD",
        "price": 11178.5,
        "size": 100,
        "matchedAt": 1562288776609,
        "side": "BUY"
    },
    {
        "id": "5aefeb33-e940-0000-0001-0000056fea51",
        "symbol": "BTCUSD",
        "price": 11180,
        "size": 60,
        "matchedAt": 1562288902053,
        "side": "SELL"
    }
]

Response Example (Real-time)
[
    {
        "id": "5af01b50-9700-0000-0001-000005727d9b",
        "symbol": "BTCUSD",
        "price": 11138,
        "size": 267,
        "matchedAt": 1562301514332,
        "side": "BUY"
    }
]

Candlestick (K-Line)
Subscribe to OHLCV data.

URL
wss://api.big.one/ws/contract/v2/candlesticks/{period}@{symbol}

Supported Periods: 1MIN, 5MIN, 15MIN, 30MIN, 1H, 4H, 6H, 12H, 1D

Request Example
wscat -c wss://api.big.one/ws/contract/v2/candlesticks/1MIN@BTCUSD

Response Example
[
    {
        "symbol": "BTCUSD",
        "type": "1MIN",
        "time": 1562301000000,
        "open": 11119.5,
        "close": 11109.5,
        "high": 11123.5,
        "low": 11109.5,
        "nTrades": 4,
        "volume": 3427,
        "turnover": 0.30820388075,
        "version": 91383701,
        "nextTs": 1562301060000
    }
]

Contract Instruments
Get real-time contract details (funding rate, open interest, etc.).

URL
Single Symbol: wss://api.big.one/ws/contract/v2/instruments@{symbol}
All Instruments: wss://api.big.one/ws/contract/v2/instruments
Parameters
Parameter	Type	Required	Description
symbol	string	No	Contract Symbol (e.g., BTCUSD). If omitted, subscribes to all instruments.
Request Example (Single Symbol)
wscat -c wss://api.big.one/ws/contract/v2/instruments@BTCUSD

Request Example (All Instruments)
wscat -c wss://api.big.one/ws/contract/v2/instruments

Response Example
[
    {
        "turnover24h": 0.354295837,
        "openInterest": 3412,
        "volume24hInUsd": 4000,
        "fundingRate": 0,
        "volume24h": 4000,
        "last24hMaxPrice": 11290,
        "btcPrice": 11255.51,
        "latestPrice": 11290,
        "symbol": "BTCUSD",
        "openValue": 0.300825969916003,
        "last24hMinPrice": 11290,
        "openTime": 0,
        "markPrice": 11255.51,
        "indexPrice": 11255.51
    }
]

Private Stream (Authenticated)
Private data (Cash, Positions, Orders, Trades) is all pushed through a single Stream channel.

Authentication
Authentication is handled via the HTTP Authorization Header during the WebSocket handshake.

Header Format: Authorization: Bearer {YOUR_JWT_TOKEN}

URL
wss://api.big.one/ws/contract/v2/stream

Request Example
wscat -H "Authorization: Bearer YOUR_JWT_TOKEN" -c wss://api.big.one/ws/contract/v2/stream

Response Data Structure
The stream pushes a JSON object containing any updates to the following keys:

cash (Account Balance)
positions
orders (Order Status Updates)
trades (User Trades)
Response Example
{
    "cash": {
        "id": "5aed7b45-5d19-40f2-0005-ca49d01f33e3",
        "userId": "5aec525e-335d-4724-0005-20153b361f89",
        "currency": "USDT",
        "balances": 0.2,
        "available": 0.2,
        "margin": 0,
        "positionMargin": 0,
        "orderMargin": 0,
        "positionValue": 0,
        "unrealizedPnl": 0,
        "marginBalances": 0.2,
        "marginRate": 0,
        "leverage": 0
    },
    "positions": [
        {
            "id": "5aed7b45-5d19-40f2-0005-ca49d01f33e3",
            "userId": "5aec525e-335d-4724-0005-20153b361f89",
            "symbol": "BTCUSD",
            "currency": "BTC",
            "isCross": true,
            "marginRate": 0.01,
            "feeRateTaker": 0.0007,
            "feeRateMaker": 0.0006,
            "size": 100,
            "notional": 0.008857,
            "initMargin": 0.00008857,
            "margin": 0.01,
            "orderMargin": 0,
            "realisedPnl": 0,
            "totalPnl": 0,
            "markPrice": 11303.14,
            "riskLimit": 100,
            "liquidatePrice": 10000.5,
            "entryPrice": 11290,
            "unrealizedPnl": 0,
            "leverage": 100,
            "equity": 0.1,
            "value": 1.2,
            "risk": 0,
            "rom": 0,
            "buyingNotional": 0,
            "sellingNotional": -0.116909,
            "buyingSize": 0,
            "sellingSize": -1400,
            "seqNo": 0
        }
    ],
    "orders": [
        {
             "id": "5aefeab9-6840-0000-0001-0000056fe3c8",
             "userId": "5aec525e-335d-4724-0005-20153b361f89",
             "liquidateUserId": null,
             "symbol": "BTCUSD",
             "currency": "USDT",
             "type": "LIMIT",
             "side": "BUY",
             "status": "PARTIALLY_FILLED",
             "price": 49500.0,
             "avgPrice": 49450,
             "size": 1.0,
             "notional": 49500,
             "filled": 0.5,
             "filledNotional": 24725
        }
    ],
    "trades": [
        {
             "id": "5aefeab9-6840-0000-0001-0000056fe3c8",
             "orderId": "5aefeab9-6840-0000-0001-0000056fe3c8",
             "symbol": "BTCUSD",
             "side": "BUY",
             "price": 49500.0,
             "size": 0.5,
             "notional": 24750,
             "fee": 0.05,
             "feeRate": 0.002,
             "pnl": 0
        }
    ]
}








Get List of Contracts Detail
GET
https://api.big.one/api/contract/v2/instruments
Returns detailed information about all available contract instruments including prices, funding rates, and trading volume.

Responses
200
Success

application/json
Schema
Example (auto)
Schema
Array [
usdtPrice
number
USDT Index Price

Example: 0.99929568
symbol
string
Contract Instrument Symbol

Example: BTCUSD
btcPrice
number
BTC Index Price

Example: 87413.1
ethPrice
number
ETH Index Price

Example: 2921.36
nextFundingRate
number
Estimated next funding rate

Example: 0.0001
fundingRate
number
Current funding rate

Example: 0.0001974
latestPrice
number
Latest transaction price

Example: 87391
last24hPriceChange
number
24h price change percentage

Example: 0.0041
indexPrice
number
Index price

Example: 87413.1
volume24h
number
24h trading volume (in contract size)

Example: 3889971
turnover24h
number
24h turnover

Example: 44.5192334698948
nextFundingTime
integer<int64>
Next funding timestamp

Example: 1766685600000
markPrice
number
Mark price

Example: 87422.65075531
last24hMaxPrice
number
Highest price in the last 24 hours

Example: 87997.5
volume24hInUsd
number
24h trading volume (in USD)

Example: 3891564.20722726
openValue
number
Open Value

Example: 29.7443056608277
last24hMinPrice
number
Lowest price in the last 24 hours

Example: 86313.5
openInterest
number
Total open interest

Example: 1376246
]
curl
go
python
java
javascript
CURL
curl -L 'https://api.big.one/api/contract/v2/instruments' \
-H 'Accept: application/json'


Request
Collapse all
Send API Request
Response
Clear
200
Headers



[
  {
    "usdtPrice": 1.0000003,
    "symbol": "BTCUSD",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.000264,
    "latestPrice": 67163,
    "last24hPriceChange": -0.0307,
    "indexPrice": 67195,
    "volume24h": 8000143,
    "turnover24h": 117.5582109251584,
    "nextFundingTime": 1772157600000,
    "markPrice": 67210.83315785,
    "last24hMaxPrice": 69946.5,
    "volume24hInUsd": 7899323.983116019,
    "openValue": 29.18298505334425,
    "last24hMinPrice": 66436.5,
    "openInterest": 1237038
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ETHUSD",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": -0.0001433,
    "latestPrice": 2000.93,
    "last24hPriceChange": -0.0347,
    "indexPrice": 2002.3,
    "volume24h": 529758,
    "turnover24h": 257.5635666556,
    "nextFundingTime": 1772157600000,
    "markPrice": 2002.04390583,
    "last24hMaxPrice": 2140.36,
    "volume24hInUsd": 515719.52951450786,
    "openValue": 118.9863249462565,
    "last24hMinPrice": 1974.68,
    "openInterest": 161870
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "BTCUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.00002308,
    "fundingRate": -0.0001873,
    "latestPrice": 67169,
    "last24hPriceChange": -0.0301,
    "indexPrice": 67194.98,
    "volume24h": 3038595,
    "turnover24h": 206629199.7465,
    "nextFundingTime": 1772157600000,
    "markPrice": 67183.74701519,
    "last24hMaxPrice": 69959,
    "volume24hInUsd": 206629261.73525992,
    "openValue": 326436.56754,
    "last24hMinPrice": 66474,
    "openInterest": 7276
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ETHUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001812,
    "latestPrice": 2001.35,
    "last24hPriceChange": -0.0343,
    "indexPrice": 2002.47,
    "volume24h": 337930,
    "turnover24h": 69388964.126,
    "nextFundingTime": 1772157600000,
    "markPrice": 2002.79385947,
    "last24hMaxPrice": 2144.27,
    "volume24hInUsd": 69388984.94268924,
    "openValue": 43358.19115,
    "last24hMinPrice": 1975.07,
    "openInterest": 394
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "DOTUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.48,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 1.548,
    "last24hPriceChange": -0.019,
    "indexPrice": 1.546,
    "volume24h": 99155,
    "turnover24h": 160871.729,
    "nextFundingTime": 1772157600000,
    "markPrice": 1.54613798,
    "last24hMaxPrice": 1.748,
    "volume24hInUsd": 160869.28696715378,
    "openValue": 15017.094,
    "last24hMinPrice": 1.524,
    "openInterest": 1678
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "UNIUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001787,
    "latestPrice": 3.77,
    "last24hPriceChange": -0.0786,
    "indexPrice": 3.768,
    "volume24h": 44257,
    "turnover24h": 176848.107,
    "nextFundingTime": 1772157600000,
    "markPrice": 3.768601,
    "last24hMaxPrice": 4.287,
    "volume24hInUsd": 176848.1600544321,
    "openValue": 5365.6861,
    "last24hMinPrice": 3.715,
    "openInterest": 919
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "FILUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.48,
    "nextFundingRate": 0.0001,
    "fundingRate": -0.0001838,
    "latestPrice": 0.994,
    "last24hPriceChange": -0.0787,
    "indexPrice": 0.9952,
    "volume24h": 65648,
    "turnover24h": 67889.195,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.99503674,
    "last24hMaxPrice": 1.105,
    "volume24hInUsd": 67888.1644420199,
    "openValue": 14630.13515,
    "last24hMinPrice": 0.979,
    "openInterest": 775
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "XRPUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001838,
    "latestPrice": 1.3889,
    "last24hPriceChange": -0.0581,
    "indexPrice": 1.38973,
    "volume24h": 151180,
    "turnover24h": 21756024.36,
    "nextFundingTime": 1772157600000,
    "markPrice": 1.38995799,
    "last24hMaxPrice": 1.4986,
    "volume24hInUsd": 21756030.886807308,
    "openValue": 658.44,
    "last24hMinPrice": 1.3826,
    "openInterest": 5
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "AVAXUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001806,
    "latestPrice": 9.204,
    "last24hPriceChange": -0.0565,
    "indexPrice": 9.2057,
    "volume24h": 340711,
    "turnover24h": 3221042.176,
    "nextFundingTime": 1772157600000,
    "markPrice": 9.20718387,
    "last24hMaxPrice": 10.064,
    "volume24hInUsd": 3220993.280579768,
    "openValue": 895.4731,
    "last24hMinPrice": 8.932,
    "openInterest": 28
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "SOLUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001712,
    "latestPrice": 85.36,
    "last24hPriceChange": -0.0398,
    "indexPrice": 85.357,
    "volume24h": 230123,
    "turnover24h": 20158781.18,
    "nextFundingTime": 1772157600000,
    "markPrice": 85.37004255,
    "last24hMaxPrice": 92.38,
    "volume24hInUsd": 20158787.227634355,
    "openValue": 651.655,
    "last24hMinPrice": 83.88,
    "openInterest": 4
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "DOGEUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001812,
    "latestPrice": 0.09601,
    "last24hPriceChange": -0.0754,
    "indexPrice": 0.096061,
    "volume24h": 72587,
    "turnover24h": 7300957.47,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.09607654,
    "last24hMaxPrice": 0.1084,
    "volume24hInUsd": 7300959.660287241,
    "openValue": 1002.748,
    "last24hMinPrice": 0.0935,
    "openInterest": 10
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ORDIUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.003,
    "fundingRate": 0.0001,
    "latestPrice": 2.404,
    "last24hPriceChange": -0.0785,
    "indexPrice": 2.4153,
    "volume24h": 633643,
    "turnover24h": 1597774.976,
    "nextFundingTime": 1772157600000,
    "markPrice": 2.41551557,
    "last24hMaxPrice": 2.74,
    "volume24hInUsd": 1597775.4553324927,
    "openValue": 28.278,
    "last24hMinPrice": 2.341,
    "openInterest": 12
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "LINKUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 8.978,
    "last24hPriceChange": -0.0497,
    "indexPrice": 8.9787,
    "volume24h": 930728,
    "turnover24h": 8586378.315,
    "nextFundingTime": 1772157600000,
    "markPrice": 8.97950135,
    "last24hMaxPrice": 9.576,
    "volume24hInUsd": 8586380.890913494,
    "openValue": 42.344,
    "last24hMinPrice": 8.782,
    "openInterest": 5
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "LTCUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 55.17,
    "last24hPriceChange": -0.0536,
    "indexPrice": 55.167,
    "volume24h": 633483,
    "turnover24h": 35752203.59,
    "nextFundingTime": 1772157600000,
    "markPrice": 55.17192365,
    "last24hMaxPrice": 58.96,
    "volume24hInUsd": 35751660.8715495,
    "openValue": 0,
    "last24hMinPrice": 54.35,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "TRUMPUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 3.441,
    "last24hPriceChange": -0.0441,
    "indexPrice": 3.4473,
    "volume24h": 1779630,
    "turnover24h": 6261792.188,
    "nextFundingTime": 1772157600000,
    "markPrice": 3.44760767,
    "last24hMaxPrice": 3.691,
    "volume24hInUsd": 6261794.066537657,
    "openValue": 0,
    "last24hMinPrice": 3.406,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "XINUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.0005,
    "fundingRate": -0.0005,
    "latestPrice": 0,
    "last24hPriceChange": 0,
    "indexPrice": 53.273,
    "volume24h": 0,
    "turnover24h": 0,
    "nextFundingTime": 1772157600000,
    "markPrice": 53.24922586,
    "last24hMaxPrice": 0,
    "volume24hInUsd": 0,
    "openValue": 81.62,
    "last24hMinPrice": 0,
    "openInterest": 1
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ADAUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.2857,
    "last24hPriceChange": -0.0454,
    "indexPrice": 0.2853,
    "volume24h": 151385,
    "turnover24h": 446814.099,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.28532546,
    "last24hMaxPrice": 0.3167,
    "volume24hInUsd": 446814.2330442297,
    "openValue": 99.446,
    "last24hMinPrice": 0.2794,
    "openInterest": 36
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "SUIUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.919,
    "last24hPriceChange": -0.0735,
    "indexPrice": 0.9206,
    "volume24h": 8704108,
    "turnover24h": 8350495.1869,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.92068216,
    "last24hMaxPrice": 1.025,
    "volume24hInUsd": 8350497.692048556,
    "openValue": 40.322,
    "last24hMinPrice": 0.9012,
    "openInterest": 35
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "AUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.08,
    "last24hPriceChange": -0.0361,
    "indexPrice": 0.0801,
    "volume24h": 70357,
    "turnover24h": 58031.89,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.08010715,
    "last24hMaxPrice": 0.084,
    "volume24hInUsd": 58031.907409567,
    "openValue": 0,
    "last24hMinPrice": 0.079,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "WLFIUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.1154,
    "last24hPriceChange": -0.0195,
    "indexPrice": 0.1158,
    "volume24h": 755233,
    "turnover24h": 877964.375,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.11581034,
    "last24hMaxPrice": 0.1224,
    "volume24hInUsd": 877964.6383893125,
    "openValue": 0,
    "last24hMinPrice": 0.1136,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ENAUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.1046,
    "last24hPriceChange": -0.0482,
    "indexPrice": 0.10481,
    "volume24h": 12235189,
    "turnover24h": 13427705.322,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.10481935,
    "last24hMaxPrice": 0.1188,
    "volume24hInUsd": 13427709.350311596,
    "openValue": 0,
    "last24hMinPrice": 0.1031,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "AVNTUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.1728,
    "last24hPriceChange": -0.0724,
    "indexPrice": 0.17548,
    "volume24h": 5359761,
    "turnover24h": 969435.4548,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.17549566,
    "last24hMaxPrice": 0.1895,
    "volume24hInUsd": 969435.7456306365,
    "openValue": 0,
    "last24hMinPrice": 0.1721,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "PUMPUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.00175,
    "last24hPriceChange": -0.0894,
    "indexPrice": 0.0017533,
    "volume24h": 270655,
    "turnover24h": 499372.541,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.00175346,
    "last24hMaxPrice": 0.001981,
    "volume24hInUsd": 499372.6908117623,
    "openValue": 0,
    "last24hMinPrice": 0.001729,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ASTERUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.6969,
    "last24hPriceChange": -0.0274,
    "indexPrice": 0.6973,
    "volume24h": 3692833,
    "turnover24h": 2610879.3313,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.69736223,
    "last24hMaxPrice": 0.7332,
    "volume24hInUsd": 2610880.1145637995,
    "openValue": 1.2358,
    "last24hMinPrice": 0.6868,
    "openInterest": 1
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "BNBUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 619.18,
    "last24hPriceChange": -0.021,
    "indexPrice": 618.955,
    "volume24h": 79446,
    "turnover24h": 4980848.457,
    "nextFundingTime": 1772157600000,
    "markPrice": 619.01024173,
    "last24hMaxPrice": 642.69,
    "volume24hInUsd": 4980849.951254537,
    "openValue": 0,
    "last24hMinPrice": 611.31,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "PEPEUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.000003814,
    "last24hPriceChange": -0.1278,
    "indexPrice": 0.0000038123,
    "volume24h": 531574,
    "turnover24h": 2160381.478,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.00000381,
    "last24hMaxPrice": 0.000004444,
    "volume24hInUsd": 2160382.1261144434,
    "openValue": 0,
    "last24hMinPrice": 0.000003773,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ZECUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 238.46,
    "last24hPriceChange": -0.0697,
    "indexPrice": 238.79,
    "volume24h": 4172680,
    "turnover24h": 103334546.749,
    "nextFundingTime": 1772157600000,
    "markPrice": 238.81131201,
    "last24hMaxPrice": 260.6,
    "volume24hInUsd": 103334577.74936402,
    "openValue": 46.506,
    "last24hMinPrice": 235.24,
    "openInterest": 2
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "TONUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.00004727,
    "fundingRate": 0.0001,
    "latestPrice": 1.2936,
    "last24hPriceChange": -0.0355,
    "indexPrice": 1.29403,
    "volume24h": 1785290,
    "turnover24h": 23117863.78,
    "nextFundingTime": 1772157600000,
    "markPrice": 1.29414549,
    "last24hMaxPrice": 1.3451,
    "volume24hInUsd": 23117870.715359133,
    "openValue": 0,
    "last24hMinPrice": 1.2616,
    "openInterest": 0
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "HYPEUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 28.18,
    "last24hPriceChange": -0.0214,
    "indexPrice": 28.2215,
    "volume24h": 504147,
    "turnover24h": 14347669.74,
    "nextFundingTime": 1772157600000,
    "markPrice": 28.22401877,
    "last24hMaxPrice": 29.398,
    "volume24hInUsd": 14347451.942373347,
    "openValue": 0,
    "last24hMinPrice": 27.574,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "HBARUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.1003,
    "last24hPriceChange": -0.0337,
    "indexPrice": 0.100337,
    "volume24h": 181016,
    "turnover24h": 1851330.06,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.10034596,
    "last24hMaxPrice": 0.1069,
    "volume24hInUsd": 1851330.615399018,
    "openValue": 0,
    "last24hMinPrice": 0.0987,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "GIGGLEUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001852,
    "latestPrice": 26.95,
    "last24hPriceChange": 0.0174,
    "indexPrice": 26.97,
    "volume24h": 722474,
    "turnover24h": 1947869.042,
    "nextFundingTime": 1772157600000,
    "markPrice": 26.97445814,
    "last24hMaxPrice": 30.27,
    "volume24hInUsd": 1947869.6263607126,
    "openValue": 758.41145,
    "last24hMinPrice": 25.6,
    "openInterest": 110
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "DASHUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 34.02,
    "last24hPriceChange": -0.0513,
    "indexPrice": 34.116,
    "volume24h": 20720,
    "turnover24h": 726645.68,
    "nextFundingTime": 1772157600000,
    "markPrice": 34.11904485,
    "last24hMaxPrice": 36.33,
    "volume24hInUsd": 726645.897993704,
    "openValue": 0,
    "last24hMinPrice": 33.67,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ZENUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 5.504,
    "last24hPriceChange": -0.0432,
    "indexPrice": 5.5075,
    "volume24h": 207803,
    "turnover24h": 1172742.098,
    "nextFundingTime": 1772157600000,
    "markPrice": 5.50799154,
    "last24hMaxPrice": 5.869,
    "volume24hInUsd": 1172742.4498226293,
    "openValue": 0,
    "last24hMinPrice": 5.316,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "PAXGUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 5190.14,
    "last24hPriceChange": -0.004,
    "indexPrice": 5196.08,
    "volume24h": 4916,
    "turnover24h": 255081.3535,
    "nextFundingTime": 1772157600000,
    "markPrice": 5196.54375014,
    "last24hMaxPrice": 5217.59,
    "volume24hInUsd": 255081.43002440606,
    "openValue": 0,
    "last24hMinPrice": 5144.26,
    "openInterest": 0
  },
  {
    "usdtPrice": 0.99998482,
    "symbol": "MERLUSDT",
    "btcPrice": 67195.24,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.0434,
    "last24hPriceChange": -0.0686,
    "indexPrice": 0.04336,
    "volume24h": 142877,
    "turnover24h": 64396.878,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.04336387,
    "last24hMaxPrice": 0.0469,
    "volume24hInUsd": 64395.90045539196,
    "openValue": 0,
    "last24hMinPrice": 0.0425,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "MONUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.00007388,
    "latestPrice": 0.0207,
    "last24hPriceChange": -0.0407,
    "indexPrice": 0.020695,
    "volume24h": 118006,
    "turnover24h": 255940.064,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.02069636,
    "last24hMaxPrice": 0.02254,
    "volume24hInUsd": 255940.1407820192,
    "openValue": 0,
    "last24hMinPrice": 0.02055,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "BCHUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.00060913,
    "fundingRate": 0.0001,
    "latestPrice": 480.6,
    "last24hPriceChange": -0.0715,
    "indexPrice": 481.135,
    "volume24h": 118363,
    "turnover24h": 5900065.346,
    "nextFundingTime": 1772157600000,
    "markPrice": 481.1779413,
    "last24hMaxPrice": 518.31,
    "volume24hInUsd": 5900067.116019604,
    "openValue": 96.862,
    "last24hMinPrice": 478.07,
    "openInterest": 2
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "BREVUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.00060849,
    "fundingRate": 0.0001,
    "latestPrice": 0.1393,
    "last24hPriceChange": 0.0146,
    "indexPrice": 0.13923,
    "volume24h": 67131,
    "turnover24h": 93238.252,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.13924243,
    "last24hMaxPrice": 0.1452,
    "volume24hInUsd": 93238.2799714756,
    "openValue": 0,
    "last24hMinPrice": 0.1345,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "SKRUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": 0.0001,
    "fundingRate": 0.0001,
    "latestPrice": 0.02068,
    "last24hPriceChange": -0.1035,
    "indexPrice": 0.02071,
    "volume24h": 8478,
    "turnover24h": 18541.449,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.02071185,
    "last24hMaxPrice": 0.02317,
    "volume24hInUsd": 18541.4545624347,
    "openValue": 0,
    "last24hMinPrice": 0.02057,
    "openInterest": 0
  },
  {
    "usdtPrice": 1.0000003,
    "symbol": "ELSAUSDT",
    "btcPrice": 67195,
    "ethPrice": 2002.3,
    "nextFundingRate": -0.00044507,
    "fundingRate": 0.0001,
    "latestPrice": 0.086,
    "last24hPriceChange": 0.0631,
    "indexPrice": 0.0868,
    "volume24h": 11448,
    "turnover24h": 97682.8,
    "nextFundingTime": 1772157600000,
    "markPrice": 0.08680775,
    "last24hMaxPrice": 0.0919,
    "volume24hInUsd": 97682.82930484,
    "openValue": 0,
    "last24hMinPrice": 0.0799,







Get OrderBook Snapshot
GET
https://api.big.one/api/contract/v2/depth@:symbol/snapshot
Returns the current order book snapshot for a contract, showing aggregate quantities at each price level.

Request
Path Parameters
symbol
string
required
The contract symbol (e.g., BTCUSD, BTCUSDT).

Example: BTCUSD
Responses
200
Success

application/json
Schema
Example (auto)
Schema
bids
object
asks
object
to
integer<int64>
The ending sequence ID of this snapshot.

from
integer<int64>
The starting sequence ID of this snapshot.

lastPrice
number
The price of the most recent trade.

bestPrices
object








Get Trade List
GET
https://api.big.one/api/contract/v2/trades
Get Trade List

Request
Query Parameters
symbol
string
Contract Symbol (e.g. BTCUSD)

Example: BTCUSD
id
string
Pagination offset ID. Returns trades older than this ID.

Example: 5aef4041-ee43-4a60-0005-705a0f1edcb4
limit
integer
Page size limit

Default value: 100
Example: 20
side
string
Possible values: [BUY, SELL, FUNDING, ADL_BUY, ADL_SELL, TRADING]

Trade Side

Example: BUY
order-id
string
Order ID. Filter by order.

Example: 5aef4041-ee43-4a60-0005-705a0f1edcb4
Responses
200
Success

application/json
Schema
Example (auto)
Example
Schema
Array [
id
string<uuid>
The unique trade identifier.

Example: 5aef4041-f300-0000-0001-00000000001b
orderId
string<uuid>
The order ID that was filled by this trade.

Example: 5aef4041-ee43-4a60-0005-705a0f1edcb4
ts
integer<int64>
The trade timestamp (Unix microseconds).

Example: 1562244089804
side
string
The trade side. BUY = long position filled, SELL = short position filled.

Possible values: [BUY, SELL]

Example: SELL
symbol
string
The contract symbol.

Example: BTCUSD
currency
string
The currency used for settlement of fees and PnL.

Example: BTC
size
number
The number of contracts filled in this trade.

Example: 1000
notional
number
The trade notional value in the quote currency.

Example: 0.08857395925
price
number
The execution price of the trade.

Example: 11290
feeRate
number
The fee rate applied to this trade.

Example: 0.0007
pnl
number
The realized PnL from this trade (0 for taker trades).

Example: 0
fee
number
The trading fee charged for this trade.

Example: 0.00006200177148
order
object
]