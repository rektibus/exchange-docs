Introduction

## EnsoX Integration Notes

### APIs
- **New Spot Trading API** (used for WS): `wss://trade.cex.io/api/spot/ws-public` — typed subscriptions (`trade_subscribe`, `order_book_subscribe`), fields nested in `data.*`.
- **Old API** (used for REST recovery): `https://cex.io/api/trade_history/{symbol1}/{symbol2}/` — simple GET, returns `[{type, date, amount, price, tid}]`. Symbol requires slash separator (`BTC/USD`), not dash.
- REST: `rest_symbol_transform: "replace_separator:/"` converts `BTC-USD` → `BTC/USD`.

### Known Quirks
1. **Duplicate `order_book_increment` messages**: Every orderbook increment arrives TWICE with the SAME `seqId`. This is a CEX server-side behavior, not a config bug. The depth engine handles this correctly because level updates are idempotent (setting the same price/qty twice is a no-op).
2. **`tradeHistorySnapshot` not observed**: Docs say it should arrive after `trade_subscribe`, but the public WS never sends it. Added to `ack_mapping` defensively.
3. **Very low trade volume**: BTC-USD can go 30+ seconds without a trade. Bursts of 10-15 trades then appear together.
4. **10-second keepalive**: CEX disconnects if no message sent within 10 seconds. Config uses `heartbeat_ms: 8000` with JSON ping `{"e":"ping"}`.

### Field Mapping (WS vs REST)
| Data | WS Field | REST Field | Canonical |
|------|----------|------------|-----------|
| Price | `data.price` | `price` | price |
| Quantity | `data.amount` | `amount` | quantity |
| Side | `data.side` (BUY/SELL) | `type` (buy/sell) | side |
| Timestamp | `data.dateISO` (ISO) | `date` (unix seconds string) | timestamp |
| Trade ID | `data.tradeId` | `tid` | trade_id |

Last updated: 2026-02-04

Welcome to CEX.IO Spot Trading trader and developer documentation. This document outline system functionality, market details, and APIs.

Latest Changes
Please find the list of changes in API functionality effective from the specified date.

2025-07-11

REST API, WebSocket API - added optional parameter "accountIds" for Cancel All Orders method (REST, WebSocket specifications), which allows Client to cancel all open orders only on indicated accounts.

2024-07-12

REST API, WebSocket API - added new Wallet Balance method (REST, WebSocket specifications), which allows Client to retrieve current balances on his CEX.IO Wallet account.

2024-01-31

REST API, WebSocket API - CEX.IO Exchange Plus product has been rebranded as CEX.IO Spot Trading, accompanied by new REST and WebSocket (WS) API endpoints for both public and private interactions.

Clients are advised to transition to the new API endpoints, as the old endpoints will be deactivated in the near future. The specific dates for the deactivation will be communicated separately.

General
Accounts
When Client deposits or withdraws funds, or places an order, the Main account is used by default. If Client wants to use multiple accounts, he can create sub-accounts.

Sub-accounts is the option the Client can use at his will. Client can specify the sub-account in his trade order, and that instructs CEX.IO Spot Trading, which sub-account to use to transfer to/from the funds during this order execution. Only one sub-account can be specified for single trade order.

Sub-accounts may be useful for Client if he wishes to distinguish orders by certain criteria, for example trade strategies, portfolios or projects, etc. If Client doesn't need such option, he can then simply ignore it and use only his main account, without specifying sub-accounts.

When depositing funds to his Spot Trading account, Client can omit sub-accounts, for funds to be transferred to his main account in Spot Trading. Alternatively, Client can specify a sub-account, to which funds should be transferred. Sub-account ID is a string, the length of which should be more than 0 and less than 256.

Client can transfer funds between his sub-accounts via API or by using Spot Trading terminal. Client can view his sub-accounts and main account balances via API or by using Spot Trading terminal.

Sub-account creation
Sub-account should be created using Create Account method prior to receiving crypto deposit address, depositing funds from external crypto wallet, CEX.IO Wallet account or transferring funds from other Spot Trading sub-account.
Deposit and Withdrawal
Spot Trading has its own separate balances (main account or subaccounts), which can be replenished either from CEX.IO Wallet or from external wallet.

To be able to trade via Spot Trading, Client should prepare his CEX.IO account:
Client should be registered on CEX.IO website and complete required user verification.
Client can fund his CEX.IO account using any available deposit methods (for example, bank transfer, payment card or crypto transfer).
Client can withdraw his funds from CEX.IO account using any available withdrawal method (for example, bank transfer, payment card or crypto transfer).
For more details check the "How to Add Funds" and "How to Withdraw Funds" articles in our Knowledge Base.

Limits and Commissions
Internal transfers and transfers between CEX.IO Wallet and CEX.IO Spot Trading are free of charge and not limited. Nevertheless, external deposits have limits, which can be accessed via Processing Info REST/WebSocket requests.

Minimum deposit amount
If the amount of external deposit will be lower than minimum deposit amount, such deposit would not be credited to the Client's account and considered as lost.
Trading
This section contains information regarding trading principles, type of orders, order requirements and other details.

Order Types
Note: Some order types may be restricted to some Clients/Symbols/etc.
Market — an order that the Client makes through Spot Trading to buy or sell Symbol immediately at the best price currently available.

Important notice regarding Market orders
CEX.IO Spot Trading may partially execute market orders based on system constraints. Market orders carry inherent risks, including partial or unexpected trades.
Limit — an order placed by Client through Spot Trading to buy or sell an amount of currency at a specified price or better. Because the limit order is not a market order, it may not be executed if the price set by the Client cannot be met during the period of time, in which the order is left open. After being placed, Limit orders can be:

Fully executed immediately.
Not executed immediately, and left open to be fully or partially executed, or cancelled.
Partially executed immediately and have open outstanding amount waiting to be fully or partially executed, or cancelled.
Stop Limit — an order to buy or sell an amount of Symbol for defined price when its market price surpasses a stop price point. Once the price surpasses the predefined stop price point, the Stop Limit order becomes a Limit order.

Order TimeInForce
When Client indicates TimeInForce value in the request, he instructs CEX.IO Spot Trading on how long the order should be open after initial placement or execution. TimeInForce should be indicated for all types of orders (Limit, Stop Limit, Market).

Good Till Cancel (GTC) — the order remains open till either full execution or cancellation. GTC orders can be executed partially.

Immediate or Cancel (IOC) — the order may be immediately executed (fully or partially) or not immediately executed. An outstanding amount after immediate execution will be cancelled.

Good Till Date (GTD) — the order remains open till it is either fully executed, or cancelled, or till the time reaches the moment specified in ExpireTime. GTD orders can be partially executed.

Notice
For Market orders only IOC TimeInForce value is allowed.
API
Client interacts with CEX.IO Spot Trading through API (Application Programming Interface). There are two available API channels which can be used by Client:

WS (WebSocket) — this API should be used for trading, receiving information about Client’s accounts balances and receiving market data.
REST — this API should be used for trading and receiving information about Client’s accounts balances.
CEX.IO Spot Trading provides both Public and Private connections. Endpoints are indicated in relevant Sections.

Public API connection is designed for Clients to get acquainted with Spot Trading API connection and smooth further integration with CEX.IO Spot Trading via Private API channels. Thus, Public API has certain limitations restrictions and CEX.IO Spot Trading encourages Clients to integrate via Private API, which presents higher API rate limits, full trading and accounts tracking functionality, more frequent order book updates, additional available API methods etc.

For Public API connection no API keys are required. For Private API connection Client should generate REST\WebSocket API Key with required permission levels via CEX.IO Spot Trading Web Terminal (trade.cex.io/terminal) in the API Keys Management Profile section.

We published public client library to communicate with Spot Trading via REST and WS. You can use it if you have NodeJS or just check realization and adapt it to your programming language. You can check it via the following link

Maintenance period
CEX.IO Spot Trading regularly performs maintenance to ensure proper functionality of the system and deliver the best system performance to Clients. CEX.IO Spot Trading informs Clients in advance about scheduled maintenances. During the ongoing maintenance period:

CEX.IO Spot Trading may cancel all active Client’s orders.
CEX.IO Spot Trading may limit acceptance of Client’s new orders.
CEX.IO Spot Trading may close active WS connections. After maintenance period is over, Client should reconnect in such case.
Limit other system’s functionality affected during maintenance.
CEX.IO Spot Trading's team does its best to achieve 100% availability of all the services and components. However, in rare cases due to various reasons there can also occur short-time unscheduled maintenance periods.

Nevertheless, in response to API requests Client can receive error messages about temporary unavailability of some services in case of ongoing scheduled or unscheduled maintenance (for example, "market_data is on maintenance", "order_placement is on maintenance", "order_cancellation is on maintenance", "order_status is on maintenance" etc.).

Operating hours
CEX.IO Spot Trading operates 24/7 with no holidays. However, Spot Trading might be unavailable at maintenance periods and unexpected IT system failures.

REST
The REST API has endpoints for getting acquainted with system configuration and public data (Public calls), and also account and order management (Private calls). All requests must be sent to specified URLs (different for Public and Private methods) with POST method. Request parameters must be sent as JSON stringified object in request body. If request is successful, CEX.IO Spot Trading sends response with “ok” parameter and requested information in “data” parameter, which by default is an object (if not otherwise indicated in specification to method)

Public API Calls
REST API Public Endpoint URL

https://trade.cex.io/api/spot/rest-public

API Rate Limit
Public API rate limit is implied in order to protect the system from DDoS attacks and ensuring all Clients can have same level of stable access to CEX.IO Spot Trading API endpoints. Public requests are limited by IP address from which public API requests are made. Request limits are determined from cost associated with each public API call. By default, each public request has a cost of 1 point, but for some specific requests this cost can be higher. See up-to-date request API rate limit cost information in specification of each method.

Client request limitations
CEX.IO Spot Trading limits Public API calls to maximum of 100 points per minute, considering that each Public API call has its' cost (see below). When an API rate limit is exceeded, a 429 status will be returned. CEX.IO Spot Trading will continue to serve processing of Public API calls starting from the next calendar minute.
Response Codes
HTTP Code	Description
200: OK	Request is correct. The body of the response will include the requested data.
400: Bad Request	There was an error with the request. The action you requested may not exist.
422: Unprocessable Entity	There was an error with the request. The body of the response will have more info. Some possible reasons: Missing params or The format of data is wrong.
429: Too Many Requests	This status indicates that the too many requests were sent to Public API endpoint in a given period of time.
500: Service Unavailable	This status indicates that something is wrong on the server side, additional info will be provided in response. If this status is returned too often, please contact your account manager to clarify or fix the problem.
Order Book
This method allows Client to receive current order book snapshot for specific trading pair.

HTTP REQUEST

POST /get_order_book

API Rate Limit Cost: 1

Order Book Request Parameters
Get Order Book request for one trading pair.

Request (Client sends request to receive order book snapshot for BTC-USD trading pair)

{
  "pair": "BTC-USD"
}
Response (CEX.IO Spot Trading successfully responds to the request with current order book snapshot for BTC-USD trading pair)

{
  "ok": "ok",
  "data": {
    "timestamp": 1676037221433,
    "currency1": "BTC",
    "currency2": "USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}

Field Name	Mandatory	Format	Description
pair	Yes	String	Trading pair, for which Client wants to request an Order Book snapshot. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
timestamp	Yes	Number	Order book snapshot server time - UTC timestamp in milliseconds.
currency1	Yes	String	The first currency in the requested trading pair.
currency2	Yes	String	The second currency in the requested trading pair.
bids	Yes	Array	This array contains a list of bids of the order book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book.
asks	Yes	Array	This array contains a list of asks of the Order Book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Candles
By using Candles method Client can receive historical OHLCV candles of different resolutions and data types.

Client can indicate additional timeframe and limit filters to make response more precise to Client’s requirements.

HTTP REQUEST

POST /get_candles

API Rate Limit Cost: 1

Candles Request Parameters
Get Candles request for BTC-USD trading pair.

Request (Client sends request to receive 1 bestAsk open candles for BTC-USD trading pair as of current time)

{
  "pair": "BTC-USD",
  "fromISO": 1675953089378,
  "limit": 1,
  "dataType": "bestAsk",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading successfully responds to the request, 1 closed 1h candle)

{
  "ok": "ok",
  "data": {
    "timestamp": 1675951200000,
    "open": 22945.3,
    "high": 23163.4,
    "low": 22913,
    "close": 22920.1,
    "volume": 779.00675644,
    "resolution": "1h",
    "isClosed": true,
    "timestampISO": "2023-02-09T14:00:00.000Z"
  }
}
Request (Client sends request to receive 1 bestBid open candles for 3 pairs as of current time)

{
  "pairsList": ["BTC-USD","ETH-USD","XXX-YYY"],
  "toISO": 1676041279412,
  "limit": 1,
  "dataType": "bestBid",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading successfully responds to the request, pairs with 1 open candle for each + unsupported pair message)

{ 
  "ok": "ok",
  "data": {
    "BTC-USD":[ 
      {
        "timestamp": 1676041200000,
        "high": 21791.3,
        "low": 21772.4,
        "close": 21782.6,
        "open": 21791.3,
        "volume": 36.87654321,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "ETH-USD":[ 
      {
        "timestamp": 1676041200000,
        "high": 1545.21,
        "low": 1543.65,
        "close": 1544.95,
        "open": 1545.21,
        "volume": 34.12345678,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "XXX-YYY": {
      "error": { 
        "code": 400, 
        "reason": "Unsupported pair XXX-YYY" 
      }
    } 
  }
}
Request (Client sends request to receive last 1 hour bestAsk candle for LUNC-BUSD pair)

{
  "pair": "LUNC-BUSD",
  "toISO": 1676042478383,
  "limit": 1,
  "dataType": "bestAsk",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading responds with empty candle, which means no candle is available upon requested parameters)

{
  "ok": "ok",
  "data": {
    "timestamp": 1676041200000,
    "resolution": "1h",
    "timestampISO": "2023-02-10T15:00:00.000Z"
  }
}
Field Name	Mandatory	Format	Description
pair	No	String	Trading pair, for which Client wants to receive historical OHLCV candles. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles for one specific trading pair. If "pair" field is present, then "pairsList" field should be absent. Either "pair" or "pairsList" should be indicated in the request anyway.
pairsList	No	Array or String	Array with trading pairs, for which Client wants to receive last historical OHLCV candles. At least 1 trading pair should be indicated in this field. If this field is present and contains valid values, then it means Client wants to receive last OHLCV candle for each indicated trading pair in the list. If "pairsList" field is present, then "pair" field should be absent. Either "pairsList" or "pair" should be indicated in the request anyway.
fromISO	No	Number (UTC timestamp)	The starting moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the first one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
toISO	No	Number (UTC timestamp)	The last moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the last one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
limit	No	Number (Integer)	Maximum number of OHLCV candles to be returned in response. Indicated number should be greater than zero. This field is mandatory if at least one of “fromISO” or “toISO” fields is specified in request. This field should be absent if both “fromISO” and “toISO” are specified in request. If “pairsList” field is specified in the request, then the value of this field should equal 1 (only last candle for each requested trading pair will be returned in response).
dataType	Yes	String	The type of data, on the basis of which returned OHLC prices in candles should be calculated. Allowed values: “bestAsk”, “bestBid”.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
Candles Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
XXX-YYY	No	Object or Array	Represents an array or an object which describes XXX-YYY trading pair candle details if pairsList parameter was indicated in the request. If it represents an array - then candle for XXX-YYY trading pair is presented, if an object - then candle for XXX-YYY trading pair could not be returned and error description is returned inside an object. If pairsList was not indicated in the request, then this parameter should be absent.
XXX-YYY.N	No	Object	Represents an object with XXX-YYY trading pair candle or error description.
timestamp	Yes	Number	OHLCV candle timestamp - UTC timestamp in milliseconds.
open	No	Number (Float)	Opening price of OHLCV candle in quote currency.
high	No	Number (Float)	Highest price of OHLCV candle in quote currency, which was reached during candle timeframe.
low	No	Number (Float)	Lowest price of OHLCV candle in quote currency, which was reached during candle timeframe.
close	No	Number (Float)	Closing price of OHLCV candle in quote currency.
volume	No	Number (Float)	Total base currency amount traded during a specific candle timeframe period.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
isClosed	No	Boolean	Indicates whether the specific candle is currently closed. If the value of this field is true, then it means this candle has been already closed. If this field is absent, then it means this candle is still open.
timestampISO	Yes	String	OHLCV candle date & time in ISO format (“YYYY-MM-DDTHH:mm:ss.SSSZ").
error	No	Object	If this field is present, then requested candle can not be returned. Represents human readable error reason of why request is not successful.
error.code	No	Number	Represents numeric code of occurred error.
error.reason	No	String	Represents human readable error reason of why candle could not be returned.
Trade History
This method allows Client to obtain historical data as to occurred trades upon requested trading pair.

Client can supplement Trade History request with additional filter parameters, such as timeframe period, tradeIds range, side etc. to receive trades which match request parameters.

HTTP REQUEST

POST /get_trade_history

API Rate Limit Cost: 1

Trade History Request Parameters
Get Trade History request

Request (Client sends request to receive trade history for BTC-USD trading pair)

{
  "pair": "BTC-USD"
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "ok": "ok",
  "data": {  
    "pageSize": 1000,
    "trades": [
      {
        "tradeId": "1675399566795-0",
        "dateISO": "2023-02-03T04:46:06.795Z",
        "side": "SELL",
        "price": "21149.2",
        "amount": "10.00000000"
      },
      {
        "tradeId": "1675401193999-0",
        "dateISO": "2023-02-03T05:13:13.999Z",
        "side": "BUY",
        "price": "25896.0",
        "amount": "0.00000001"
      },
      {
        "tradeId": "1675401207800-0",
        "dateISO": "2023-02-03T05:13:27.800Z",
        "side": "SELL",
        "price": "21146.0",
        "amount": "0.00000001"
      }
    ]
  }
}
Field Name	Mandatory	Format	Description
pair	Yes	String	Trading pair, for which Client wants to receive trades history. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
side	No	String	Side of requested trades. If this field is present, it should contain only one of allowed values: “BUY” or “SELL”. If this field is not indicated in the request, then response would contain trades for "BUY" and "SELL" sides.
fromDateISO	No	String	The starting moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If “fromDateISO” and “pageSize” parameters are not specified in request, then by default last 1000 trades will be returned in response. If this field is present, then “fromTradeId” and “toTradeId” fields should not be indicated in the request.
toDateISO	No	String	The last moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If this field is present, then “fromDateISO” should also be present, “fromTradeId” and “toTradeId” fields should be absent.
fromTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, starting from which subsequent trades should be returned in response. If this field is present, then “fromDateISO” and “toDateISO” fields should not be indicated in the request.
toTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, which should be the last trade returned in response. If this field is present, then “fromTradeId” should also be present, “fromDateISO” and “toDateISO” fields should not be indicated in the request.
pageSize	No	Number (Integer)	Maximum number of trades, which should be returned in response. If this field is present then the value should be more than zero and not more than 10000. If indicated value is more than 10000, the response will still contain only up to 10000 trades max. If this field is not specified in request, then by default 1000 trades would be returned in response.
Trade History Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
pageSize	Yes	Number (Integer)	Maximum number of trades, which can be returned in response.
trades	Yes	Array	An array containing data as to each trade event which satisfies requested criteria. If request is successful, this field should be present in response. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted by “dateISO” value in ascending order (from older to newer, considering “fromDateISO” / “toDateISO” or “fromTradeId” / “toTradeId” if indicated in request). If a few trade events occurred at the same moment of time, then such trade events are sorted additionally by “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	If trade event is available, then represents an object which describes specific Х trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade in base currency.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Ticker
This method is designed to obtain current information about Ticker, including data about current prices, 24h price & volume changes, last trade event etc. of certain assets.

HTTP REQUEST

POST /get_ticker

API Rate Limit Cost: 1

Ticker Request Parameters
Get Ticker request

Request (Client sends request to receive ticker for one pair)

{
  "pairs": ["BTC-USD"]
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "ok": "ok",
  "data": {
    "BTC-USD": { 
      "bestBid": "23771.3",
      "bestAsk": "23895.2",
      "bestBidChange": "-398.5",
      "bestBidChangePercentage": "-1.64",
      "bestAskChange": "-362.4",
      "bestAskChangePercentage": "-1.49",
      "volume30d": "1311.83096457",
      "low": "22920.1",
      "high": "25379.4",
      "volume": "21.14500755",
      "quoteVolume": "509738.03240736",
      "lastTradeVolume": "0.00493647",
      "last": "23771.3",
      "lastTradePrice": "23895.2",
      "priceChange": "-481.7",
      "priceChangePercentage": "-1.98",
      "lastTradeDateISO": "2023-02-23T12:26:13.486Z",
      "volumeUSD": "286794.97"
    }
  }
}
Get Ticker request

Request (Client sends request to receive ticker for multiple pairs)

{
  "e": "get_ticker",
  "oid": "16781762556482_get_ticker",
  "data": {
    "pairs": ["ADA-USD", "BTC-USD", "ETH-USD", "SHIB-USD"]
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "ok": "ok",
  "data": {
    "ADA-USD": {
      "bestBid": "0.387159",
      "bestAsk": "0.387938",
      "bestBidChange": "0.001354",
      "bestBidChangePercentage": "0.35",
      "bestAskChange": "-0.000370",
      "bestAskChangePercentage": "-0.09",
      "volume30d": "6530615.77263454",
      "low": "0.379304",
      "high": "0.395922",
      "volume": "33554.76625400",
      "quoteVolume": "12971.29778584",
      "lastTradeVolume": "30.53522000",
      "last": "0.388926",
      "lastTradePrice": "0.387938",
      "priceChange": "0.001489",
      "priceChangePercentage": "0.38",
      "lastTradeDateISO": "2023-02-23T12:23:40.391Z",
      "volumeUSD": "45000.43"
    },
    "BTC-USD": {
      "bestBid": "23771.3",
      "bestAsk": "23895.2",
      "bestBidChange": "-398.5",
      "bestBidChangePercentage": "-1.64",
      "bestAskChange": "-362.4",
      "bestAskChangePercentage": "-1.49",
      "volume30d": "1311.83096457",
      "low": "22920.1",
      "high": "25379.4",
      "volume": "21.14500755",
      "quoteVolume": "509738.03240736",
      "lastTradeVolume": "0.00493647",
      "last": "23771.3",
      "lastTradePrice": "23895.2",
      "priceChange": "-481.7",
      "priceChangePercentage": "-1.98",
      "lastTradeDateISO": "2023-02-23T12:26:13.486Z",
      "volumeUSD": "286794.97"
    },
    "ETH-USD": {
      "bestBid": "1640.41",
      "bestAsk": "1648.25",
      "bestBidChange": "-6.58",
      "bestBidChangePercentage": "-0.39",
      "bestAskChange": "-5.41",
      "bestAskChangePercentage": "-0.32",
      "volume30d": "10500.56442743",
      "low": "1599.44",
      "high": "1680.62",
      "volume": "267.63458000",
      "quoteVolume": "439523.29960757",
      "lastTradeVolume": "0.17435800",
      "last": "1648.97",
      "lastTradePrice": "1648.25",
      "priceChange": "2.08",
      "priceChangePercentage": "0.12",
      "lastTradeDateISO": "2023-02-23T12:25:11.251Z",
      "volumeUSD": "148920.84"
    },
    "SHIB-USD": {
      "bestBid": "0.00001276",
      "bestAsk": "0.00001354",
      "bestBidChange": "0.00000045",
      "bestBidChangePercentage": "3.65",
      "bestAskChange": "0.00000032",
      "bestAskChangePercentage": "2.42",
      "volume30d": "34227200927",
      "low": "0.00001231",
      "high": "0.00001369",
      "volume": "331030734",
      "quoteVolume": "4371.24465887",
      "lastTradeVolume": "20245767",
      "last": "0.00001295",
      "lastTradePrice": "0.00001354",
      "priceChange": "-0.00000027",
      "priceChangePercentage": "-2.04",
      "lastTradeDateISO": "2023-02-23T12:05:47.380Z",
      "volumeUSD": "3782974.41"
    } 
  } 
}
Field Name	Mandatory	Format	Description
pairs	Yes	Array of Strings	List of supported trading pairs for which Client wants to receive ticker data. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present in the request, then at least 1 pair should be indicated in an array. If this field is absent, then it means Client requests ticker data for all supported pairs.
Ticker Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
XXX-YYY	No	Object	Represents an object which describes XXX-YYY trading pair ticker .
XXX-YYY.bestBid	No	String (parseable as float)	Current highest buy order price (bestBid) in Order Book.
XXX-YYY.bestAsk	No	String (parseable as float)	Current lowest sell order price (bestAsk) in Order Book.
XXX-YYY.bestBidChange	No	String (parseable as float)	Last 24h bestBid price change in quote currency.
XXX-YYY.bestBidChangePercentage	No	String (parseable as float)	Last 24h bestBid price change in percentage.
XXX-YYY.bestAskChange	No	String (parseable as float)	Last 24h bestAsk price change in quote currency.
XXX-YYY.bestAskChangePercentage	No	String (parseable as float)	Last 24h bestAsk price change in percentage.
XXX-YYY.volume30d	Yes	String (parseable as float)	Last 30 days trading volume in base currency.
XXX-YYY.low	No	String (parseable as float)	Last 24h lowest trade price.
XXX-YYY.high	No	String (parseable as float)	Last 24h highest trade price.
XXX-YYY.volume	Yes	String (parseable as float)	Last 24 hours volume in base currency.
XXX-YYY.quoteVolume	Yes	String (parseable as float)	Last 24 hours volume in quote currency.
XXX-YYY.lastTradeVolume	No	String (which can be parsed as Float)	Last trade volume in base currency.
XXX-YYY.last	No	String (which can be parsed as Float)	Last indicative price.
XXX-YYY.lastTradePrice	No	String (parseable as float)	Last trade price in CEX.IO Ecosystem.
XXX-YYY.priceChange	No	String (which can be parsed as Float)	Last 24h price change in quote currency.
XXX-YYY.priceChangePercentage	No	String (which can be parsed as Float)	Last 24h price change in percentage.
XXX-YYY.lastTradeDateISO	No	String	Date & Time of last trade in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
XXX-YYY.volumeUSD	Yes	String (parseable as float)	Last 24h volume equivalent in USD currency.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Server Time
This method is used to get the current time on Spot Trading server. It can be useful for applications that have to be synchronized with the server's time.

HTTP REQUEST

POST /get_server_time

API Rate Limit Cost: 1

Get Server Time request

Request (client sends a request get server time)

{}
Response (CEX.IO Spot Trading successfully responds to the request with current server time)

{
  "ok": "ok",
  "data": {
    "timestamp": 1231239102398, // timestamp milliseconds
    "ISODate": "2022-09-09T09:09:55.999Z"
  }
}
Server Time Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
timestamp	Yes	Number	CEX.IO Spot Trading server current time - UTC timestamp in milliseconds.
ISODate	Yes	String	CEX.IO Spot Trading server current date and time in UTC in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ).
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Pairs Info
Pair Info method allows Client to receive the parameters for all supported trading pairs.

HTTP REQUEST

POST /get_pairs_info

API Rate Limit Cost: 1

Pairs Info Request Parameters
Get Pairs Info request

Request (Client sends request to receive information about BTC-USD trading pair)

{
  "pair": ["BTC-USD"]
}
Response (CEX.IO Spot Trading successfully responds to the request with BTC-USD trading pair information)

{
  "ok": "ok",
  "data": {
    "base": "BTC",
    "quote": "USD",
    "baseMin": "0.0004",
    "baseMax": "60",
    "baseLotSize": "0.00000001",
    "quoteMin": "10",
    "quoteMax": "1000000",
    "quoteLotSize": "0.01000000",
    "basePrecision": 8,
    "quotePrecision": 8,
    "pricePrecision": 1,
    "minPrice": "1700.0",
    "maxPrice": "211250.0"
  }
}
Field Name	Mandatory	Format	Description
pairs	No	Array of Strings	List of supported trading pairs for which Client wants to receive configuration parameters. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present in the request, then at least 1 pair should be indicated in an array. If this field is absent, then it means Client requests configuration parameters for all supported pairs.
Pairs Info Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
X	No	Object	Represents an object which describes specific trading pair configuration parameters in CEX.IO Spot Trading system. If there are no objects in returned array, then it means there are no supported trading pairs, which satisfy Client’s request criteria.
X.base	Yes	String	Name of the first (base) currency in trading pair.
X.quote	Yes	String	Name of the first (base) currency in trading pair.
X.baseMin	Yes	String (parseable as float)	Minimum order amount in base currency.
X.baseMax	Yes	String (parseable as float)	Maximum order amount in base currency.
X.baseLotSize	Yes	String (parseable as float)	Order lot size in base currency. Such limitation allows only order amounts that are a multiple of baseLotSize. For example, if trading pair baseLotSize is 0.5, then order amounts 1.5, 4, 10.5 will be accepted, while amounts 0.3, 1.2, 10.9 will be rejected by the system.
X.quoteMin	Yes	String (parseable as float)	Minimum order amount in quote currency.
X.quoteMax	Yes	String (parseable as float)	Minimum order amount in quote currency.
X.quoteLotSize	Yes	String (parseable as float)	Order lot size in quote currency. Such limitation allows only order amounts that are a multiple of quote lot size. For example, if trading pair quoteLotSize is 0.01, then order amounts 0.5, 4, 10.59 will be accepted, while amounts 0.313, 1.2987, 1000.989 will be rejected by the system.
X.basePrecision	Yes	Number	Number of decimal places for the base currency executed amounts, used inside CEX.IO Spot Trading system.
X.quotePrecision	Yes	Number	Number of decimal places for the quote currency executed amounts, used inside CEX.IO Spot Trading system.
pricePrecision	Yes	Number	Number of allowed decimal places for the trading pair price. Such limitation allows only order prices, the number of decimal places in which doesn’t exceed pricePrecision value. For example, if trading pair pricePrecision is 3, then order limit prices 0.3, 1.94, 10, 10348.591 will be accepted, while prices 0.3136, 1.2987, 1000.98981234 will be rejected by the system.
X.minPrice	Yes	String (parseable as float)	Minimum allowed trading pair price. Orders with indication of prices, which are lower than specified value will be rejected by the system.
X.maxPrice	Yes	String (parseable as float)	Maximum allowed trading pair price. Orders with indication of prices, which are higher than specified value will be rejected by the system.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Currencies Info
Currencies Info method allows Client to receive the parameters for all currencies configured in CEX.IO Spot Trading as well as the deposit and withdrawal availability between CEX.IO Spot Trading and CEX.IO Wallet.

HTTP REQUEST

POST /get_currencies_info

API Rate Limit Cost: 1

Currencies Info Request Parameters
Successful Get Currencies Info Request

Request (Client sends request to receive currencies information)

{}
Response (CEX.IO Spot Trading successfully responds to the request with information about all available currencies for the Client)

{
  "ok": "ok",
  "data": [
    {
      "currency": "USDT",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 6
    },
    {
      "currency": "BTC",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 8
    },
    {
      "currency": "SHIB",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 0,
      "walletPrecision": 0
    },
    {
      "currency": "LUNC",
      "walletDeposit": false,
      "walletWithdrawal": false,
      "fiat": false,
      "precision": 2,
      "walletPrecision": null
    },
    {
      "currency": "USD",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": true,
      "precision": 8,
      "walletPrecision": 2
    }
  ]
}
Currencies Info request (Indicated 2 specific currencies)

Request (Client sends get currencies info request for 2 currencies)

{
  "currencies": ["ETH", "USD"]
}
Response (CEX.IO Spot Trading responds to the request with information for indicated currencies)

{
  "ok": "ok",
  "data": [
    {
      "currency": "ETH",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 6
    },
    {
      "currency": "USD",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": true,
      "precision": 8,
      "walletPrecision": 2
    }
  ]
}
Currencies Info request (Indicated unsupported currency)

Request (Client sends get currencies info request with indicated unsupported currency)

{
  "currencies": ["CCC"]
}
Response (CEX.IO Spot Trading responds to the request with empty array as requested currency is not supported)

{
  "ok": "ok",
  "data": []
}
Currencies Info request (No currencies indicated)

Request (Client sends get currencies info request with indicated currencies parameter but without any specific currencies)

{
  "currencies": []
}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "ok": "ok", 
  "data": {
    "error": "Parameter currencies should be Array of Strings"
  }
}
Field Name	Mandatory	Format	Description
currencies	No	Array of Strings	List of supported currencies for which Client wants to receive configuration parameters. Currencies should be indicated in upper case and of string type. The list should contain only valid currency symbols. If this field is present in the request, then at least 1 currency should be indicated in an array. If this field is absent, then it means Client requests configuration parameters for all supported currencies.
Currencies Info Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
X	No	Object	Represents an object which describes specific currency configuration parameters in CEX.IO Spot Trading system. If there are no objects in returned array, then it means there are no supported currencies, which satisfy Client’s request criteria.
X.currency	Yes	String	Currency name.
X.walletDeposit	Yes	Boolean	Describes current availability to deposit currency X to CEX.IO Spot Trading from CEX.IO Wallet. Only true or false values are allowed herein.
X.walletWithdrawal	Yes	Boolean	Describes current availability to withdraw currency X from CEX.IO Spot Trading to CEX.IO Wallet. Only true or false values are allowed herein.
X.fiat	Yes	Boolean	Indicates if the currency is a fiat currency or cryptocurrency. If the value is true, then indicated currency is fiat. If the value is false, then indicated currency is cryptocurrency.
X.precision	Yes	Number	Number of decimal places in amounts of specific currency used inside CEX.IO Spot Trading system (e.g. for internal transfers, executed amounts in orders etc.).
X.walletPrecision	Yes	Number or null	If the value of this parameter is a number, then it describes the number of decimal places in amounts of specific currency used for transfers to or out of CEX.IO Spot Trading system (e.g. for deposits\withdrawals from\to CEX.IO Wallet or external addresses). If the value is null, then deposits and withdrawals of specific currency from\to CEX.IO Wallet are not available.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Processing Info
This request allows Client to receive detailed information about available options to make deposits from external wallets and withdrawals to external wallets as to each supported cryptocurrency, including cryptocurrency name and available blockchains for deposit\withdrawals. Also, as to each supported blockchain there are indicated type of cryptocurrency on indicated blockchain, current deposit\withdrawal availability, minimum amounts for deposits\withdrawals, external withdrawal fees.

Processing Information makes Client more flexible in choosing desired blockchain for receiving Deposit address and initiating external withdrawals via certain blockchain, so that Client uses more convenient way of transferring his crypto assets to or from CEX.IO Ecosystem.

Note that this method indicates minimum deposit\withdrawal limits and external withdrawal fees for external crypto transfers. Currently, deposits and withdrawals of funds between CEX.IO Wallet and CEX.IO Spot Trading account are free.
Currently, external withdrawals are not supported via CEX.IO Spot Trading API.
HTTP REQUEST

POST /get_processing_info

API Rate Limit Cost: 10

Processing Info Request Parameters
Get Processing Info Request for one specific cryptocurrency

Request (Client queries processing info for "BTC")

{
  "currencies": ["BTC"]
}
Response (CEX.IO Spot Trading responds that only 'bitcoin' blockchain is supported for deposits\withdrawals of "BTC")

{
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    }
  }
}
Get Processing Info Request for several cryptocurrencies

Request (Client queries processing info for "BTC" and "USDC")

{
  "currencies": ["BTC","USDC"]
}
Response (CEX.IO Spot Trading responds that for deposits\withdrawals 'bitcoin' blockchain is supported for "BTC" and "ethereum", "stellar" and "tron" blockchains are supported for "USDC")

{
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    },
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40",
          "depositConfirmations": 25
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 1
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 21
        }
      }
    }
  }
}
Get Processing Info - No available blockchains

Request (Client queries processing info for supported cryptocurrency "ZEC")

{
  "currencies": ["ZEC"]
}
Response (CEX.IO Spot Trading responds that request was processed successfully but no blockchains are supported for "ZEC")

{
  "ok": "ok",
  "data": {}
}
Get Processing Info - Invalid and fiat cryptocurrency

Request (Client queries processing info for "BTC", "ETH", "XXX" and "USD")

{
  "currencies": ["BTC", "ETH", "XXX", "USD"]
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currencies "XXX" and "USD" are indicated in the request)

{
  "ok": "ok",
  "data": {
    "error": "Request contains unsupported currencies: XXX, USD."
  }
}
Get Processing Info - Invalid value type in "currencies" array

Request (Client queries processing info with invalid values type in "currencies" field)

{
  "currencies": [1,2,3]
}
Response (CEX.IO Spot Trading responds that error occurred because wrong type of value was indicated in "currencies" array and only string values are allowed)

{
  "ok": "ok",
  "data": {
    "error": "Currencies array should consist of string type values."
  }
}
Get Processing Info - Not an array indicated in "currencies" field

Request (Client queries processing info with indicating empty object ({}) in "currencies" field)

{
  "currencies": {}
}
Response (CEX.IO Spot Trading responds that error occurred because only array is allowed in "currencies" field)

{
  "ok": "ok",
  "data": {
    "error": "Currencies should be array."
  }
}
Field Name	Mandatory	Format	Description
currencies	No	Array	List of cryptocurrencies for which Client wants to get information about supported blockchains for deposit\withdraw, limits and commissions. Cryptocurrencies should be in upper case and of string type. The list should contain only valid cryptocurrency symbols. If this field is missing or contains an empty array ([]), then it means Client wants to get processing info for all available cryptocurrencies.
Processing Info Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data.YYY	Yes	String	Cryptocurrency symbol specified in Client's request.
data.YYY.name	Yes	String	Cryptocurrency name.
data.YYY.blockchains	Yes	Object	This object contains info about all supported blockchains to deposit\withdraw cryptocurrency YYY.
data.YYY.blockchains.X	Yes	Object	This object contains details and limitations for deposit\withdrawal of cryptocurrency YYY via blockchain X, including data about blockchain type, current availability to deposit\withdraw, minimum deposit\withdrawal limit and external withdrawal fees.
data.YYY.blockchains.X. type	Yes	String	Type of cryptocurrency YYY on blockchain X.
data.YYY.blockchains.X. deposit	Yes	String	Describes current availability to deposit cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minDeposit	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be deposited from external wallet via blockchain X.
data.YYY.blockchains.X. withdrawal	Yes	String	Describes current availability to withdraw cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minWithdrawal	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be withdrawn to external wallet via blockchain X.
data.YYY.blockchains.X. withdrawalFee	Yes	String (which can be parsed as Float)	Amount of withdrawal fee in cryptocurrency YYY, which which would be charged and subtracted from withdrawal amount if blockchain X is used for withdrawal.
data.YYY.blockchains.X. depositConfirmations	Yes	Number	Minimal confirmation number for transaction in the blockchain to be deposited to Client’s CEX.IO Spot Trading account.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	String	If this field is present, then request is not successful. Represents numeric code of occurred error.
Private API Calls
The REST API has endpoint for account and order management. All requests must be sent to specified URL with POST method. Request parameters must be sent as JSON stringified object in request body.

REST API Private Endpoint URL

https://trade.cex.io/api/spot/rest

API Rate Limit
API Rate Limit for Private API calls is defined as to each API Key, which means that if API Rate Limit has been reached for one of Client’s API Key, Client can still proceed with sending requests by other API Keys. Request limits are determined from cost associated with each private API call. By default, each private request has a cost of 1 point, but for some specific requests this cost can be higher. See up-to-date request rate limit cost information in specification of each method.

API Rate Limit is cumulative for API calls made via different protocols (REST & WebSocket) but with the same API Key.
Client request limitations
CEX.IO Spot Trading limits Private API calls to maximum of 200 points per minute, considering that each Private API call has its' cost (see below). When an API rate limit is exceeded, a 429 status will be returned. CEX.IO Spot Trading will continue to serve processing of Public API calls starting from the next calendar minute.
Response Codes
HTTP Code	Description
200: OK	Request is correct. The body of the response will include the requested data.
400: Bad Request	There was an error with the request. The action you requested may not exist.
401: Unauthorized	Token is invalid. If your API key is wrong a 401 will also be served, so check the response body, it might be that the API_KEY is invalid. Also this code will be returned if signature is incorrect, so double check your signing algorythm.
422: Unprocessable Entity	There was an error with the request. The body of the response will have more info. Some possible reasons: Missing params or The format of data is wrong.
429: Too Many Requests	This status indicates that the user has sent too many requests in a given period of time.
500: Service Unavailable	This status indicates that something is wrong on the server side, additional info will be provided in response. If this status is returned too often, please contact support team to clarify or fix the problem.
Authentication
const crypto = require('crypto')
const request = require('request')

const action = 'get_order_book'
const params = { "pair": "BTC-USD" }

const apiKey = 'base64_string_key'
const apiSecret = 'base64_string_secret'

const timestamp = parseInt(Date.now() / 1000)
const payload = action + timestamp + JSON.stringify(params)
const signature = crypto.createHmac('sha256', apiSecret).update(payload).digest('base64')

const headers = {
  'X-AGGR-KEY': apiKey,
  'X-AGGR-TIMESTAMP': timestamp,
  'X-AGGR-SIGNATURE': signature,
  'Content-Type': 'application/json'
}

request({
  url: `https://trade.cex.io/api/spot/rest/${action}`,
  method: 'POST',
  headers: headers,
  json: true,
  body: params
}, (error, response, body) => {
  console.log('statusCode:', response && response.statusCode)
  console.log('body:', body)
})
CEX.IO Spot Trading uses API keys to allow access to private APIs.

Client can generate, configure and manage api keys, set permission levels, whitelisted IPs for API key etc. via Spot Trading Web Terminal in the API Keys Management Profile section.

API Keys limit
By default Client can have up to 5 API Keys.
All REST requests must contain the following headers:

Header name	Description
X-AGGR-KEY	The api key as a string.
X-AGGR-TIMESTAMP	A unix timestamp (in seconds) for your request.
X-AGGR-SIGNATURE	The base64-encoded signature (see Signing a Request).
Content-Type	All request bodies should have content type application/json and be valid JSON.
Signing a Request
The X-AGGR-SIGNATURE header is generated by creating a HMAC-SHA256 using the base64-decoded secret key on the payload. Payload consist from string action + timestamp + body (where + represents string concatenation) and base64-encode the output.

The action is same as api endpoint with underscores, e.g. get_my_orders.

The timestamp value is the same as the X-AGGR-TIMESTAMP header.

The body is the request body string (in all cases this is JSON stringified request params object).

API Key Permissions
To restrict access to certain functionality while using of API Keys there should be defined specific set of permissions for each API Key. The defined set of permissions can be edited further if necessary.

The following permission levels are available for API Keys:

Read – permission level for viewing of account related data, receiving reports, subscribing to market data etc.

Trade – permission level, which allows placing and cancelling orders on behalf of account.

Funds Internal – permission level, which allows transferring funds between accounts (between sub-accounts or main account and sub-accounts) of CEX.IO Spot Trading Portfolio.

Funds Wallet - permission level, which allows transferring funds from CEX.IO Spot Trading accounts (main account and sub-accounts) to CEX.IO Wallet and vice versa.

Required permissions as to each API method are listed in the documentation below.

Current Fee
This method indicates current fees at specific moment of time with consideration of Client's up-to-date 30d volume and day of week (fees can be different for e.g. on weekends).

HTTP REQUEST

POST /get_my_current_fee

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Current Fee Request Parameters
Get Current Fee - Successful request

Request (Client sends request to receive all his trading fees)

{}
Response (CEX.IO Spot Trading responds with trading fees for all pairs supported for Client)

{
  "ok": "ok",
  "data": {
    "tradingFee": {
      "BTC-USD": {
        "percent": "0.5"
      },
      "XRP-USD": {
        "percent": "0.1"
      },
      "ETH-BTC": {
        "percent": "0.1"
      },
      "ADA-USD": {
        "percent": "0.1"
      },
      "ETH-USD": {
        "percent": "0.5"
      },
      "BTC-EUR": {
        "percent": "0.5"
      }
    }
  }
}
Get Current Fee (Indicated specific pairs)

Request (Client sends request to receive his trading fees for specified pair)

{
  "pairs": ["BTC-USD","ETH-USD"]
}
Response (CEX.IO Spot Trading responds with trading fees for specified pairs)

{
  "ok": "ok",
  "data": {
    "tradingFee":{
      "BTC-USD": {
        "percent": "0.5"
      },
      "ETH-USD":{
        "percent": "0.5"
      }
    }
  }
}
Get Current Fee - Invalid Request

Request (Client sends request to find transactions without valid JSON object)

{""}
Response (CEX.IO Spot Trading responds to the request with error message)

{
   "error": "Bad Request"
}
Field Name	Mandatory	Format	Description
pairs	No	Array of strings	Currency pair, for which Client wants to receive his fee. Pair should contain two currencies in upper case divided by "-" symbol. Pair should be listed in traditional direction. For example, "BTC-USD", but not "USD-BTC". If this field is missing, or if it contains empty string (""), or null, then it means Client wants to receive fee for all pairs.
Current Fee Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
tradingFee	Yes	Object	Represents trading fees for all supported trading pairs.
XXX-YYY	Yes	Object	Represents data about trading fee for specific XXX-YYY trading pair.
XXX-YYY.percent	Yes	String (parseable as float)	Represents fee percent for XXX-YYY trading pair.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Fee Strategy
Fee Strategy returns all fee options, which could be applied for Client, considering Client’s trading volume, day of week, pairs, group of pairs etc.

This method provides information about general fee strategy, which includes all possible trading fee values that can be applied for Client. To receive current trading fees, based on Client's current 30d trading volume, Client should use [Current Fee] method. To receive current 30d trading volume, Client should use [Volume] method.
Trading risk disclaimer
Reduced fees based on volume do not imply reduced trading risk. Trading cryptoassets involves significant risk of loss.
HTTP REQUEST

POST /get_fee_strategy

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Get Fee Strategy - Successful request

Request (Client requests available Fee Strategies)

{}
Response (CEX.IO Spot Trading responds with default fee options)

{ 
  "ok": "ok",
  "data": {
    "strategyConfig": {
      "default": [
        {
          "fee": "0.25",
          "volume": 10000
        },
        {
          "fee": "0.23",
          "volume": 100000
        },
        {
          "fee": "0.19",
          "volume": 500000
        },
        {
          "fee": "0.17",
          "volume": 1000000
        },
        {
          "fee": "0.15",
          "volume": 2500000
        },
        {
        "fee": "0.13",
        "volume": 5000000
        },
        {
          "fee": "0.11",
          "volume": 10000000
        },
        {
          "fee": "0.10",
          "volume": 20000000
        }
      ]
    }
  }
}
Get Fee Strategy - Successful request

Request (Client requests available Fee Strategies)

{}
Response (CEX.IO Spot Trading responds with multiple fee options, depending on the pair and day of the week)

{
  "ok": "ok",
  "data": {
    "strategyConfig": {
      "default": [
        {
          "fee":"0.25",
          "volume":10000
        },
        {
          "fee":"0.23",
          "volume":100000
        },
        {
          "fee":"0.19",
          "volume":500000
        },
        {
          "fee":"0.17",
          "volume":1000000
        },
        {
          "fee":"0.15",
          "volume":2500000
        },
        {
          "fee":"0.13",
          "volume":5000000
        },
        {
          "fee":"0.11",
          "volume":10000000
        },
        {
          "fee":"0.10",
          "volume":20000000
        }
      ],
      "perTier": {
        "reducedFee": {
          "name": "Reduced Fee",
          "description": "Reduced fee description",
          "pairList": [
            "BCH-USD",
            "ETH-USD"
          ],
          "schedule": [
            {
              "fee":"0.15",
              "volume":10000
            },
            {
              "fee":"0.11",
              "volume":30000
            },
            {
              "fee":"0.08",
              "volume":50000
            }
          ]
        },
        "hotPairs": {
          "name": "Hot",
          "description": "Trending pairs",
          "pairList": [
            "ETH-EUR",
            "USDT-GBP"
          ],
          "schedule": [
            {
              "fee":"0.20",
              "volume":10000
            },
            {
              "fee":"0.15",
              "volume":100000
            },
            {
              "fee":"0.10",
              "volume":150000
            }
          ]
        }
      },
      "perWeekend": {
        "default":[
          {
            "fee":"0.22",
            "volume":10000
          },
          {
            "fee":"0.2",
            "volume":100000
          },
          {
            "fee":"0.16",
            "volume":500000
          },
          {
            "fee":"0.14",
            "volume":1000000
          },
          {
            "fee":"0.12",
            "volume":2500000
          },
          {
            "fee":"0.1",
            "volume":5000000
          },
          {
            "fee":"0.08",
            "volume":10000000
          },
          {
            "fee":"0.07",
            "volume":20000000
          }
        ],
        "perTier": {
          "reducedFee": {
            "name": "Reduced Fee",
            "description": "Reduced fee description",
            "pairList": [
              "BCH-USD",
              "ETH-USD"
            ],
            "schedule": [
              {
                "fee":"0.14",
                "volume":10000
              },
              {
                "fee":"0.1",
                "volume":30000
              },
              {
                "fee":"0.07",
                "volume":50000
              }
            ]
          },
          "hotPairs": {
            "name": "Hot",
            "description": "Trending pairs",
            "pairList": [
              "ETH-EUR",
              "USDT-GBP"
            ],
            "schedule": [
              {
                "fee":"0.18",
                "volume":10000
              },
              {
                "fee":"0.13",
                "volume":100000
              },
              {
                "fee":"0.08",
                "volume":150000
              }
            ]
          }
        }
      }
    }
  }
}
Fee Strategy Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
strategyConfig	Yes	Object	This object defines details about Client's available fee options.
default	Yes	Array of objects	Represents possible fee levels, which are applied by default for pairs, if such pairs are not specified in "perTier.pairList" field. If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
default.ObjectN	Yes	Object	Indicate fee value based on Client's 30d total trading volume.
default.ObjectN.fee	Yes	String	Fee percent which will be applied, if Client's 30d total trading volume up to the value, indicated in "volume" of this object.
default.ObjectN.volume	Yes	Number	Represents Client's 30d trading volume (by default in USD), up to which "fee" value is applied. For receiving current 30d trading volume Client should use Volume method.
perTier	No	Object	Represents possible fee levels for specific sets of pairs indicated in "pairList" field of each tier. "perTier" fee levels have higher priority compared to default fee levels. This field could be missing if Client's strategy configuration doesn't include different fee levels for pair tiers.
perTier.CCCCC	No	Object	Describes fee details of "CCCCC" pair tier.
perTier.CCCCC.name	Yes	String	Name of specific pair tier.
perTier.CCCCC.description	Yes	String	Description of specific pair tier.
perTier.CCCCC.pairList	Yes	Array of strings	Indicates trading pairs list, which are included in CCCCC pair tier.
perTier.CCCCC.schedule	Yes	Array of objects	Indicates fee levels, which can be applied for trading pairs from "pairList" field of specific pair tier. If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
perTier.CCCCC.schedule.ObjectM	Yes	Object	Indicate fee value for pair tier CCCCCC based on Client's 30d total trading volume.
perTier.CCCCC.schedule.ObjectM.fee	Yes	String	Fee percent which will be applied for pairs from pair tier CCCCC if Client's 30d total trading volume up to the value, indicated in "volume" field of this object.
perTier.CCCCC.schedule.ObjectM.volume	Yes	Number	Represents Client's 30d trading volume (by default in USD), up to which "fee" value is applied. For receiving current 30d trading volume Client should use Volume method.
perWeekend	No	Object	Represents fees, which apply only on weekends (Saturday and Sunday according to UTC time) and have higher priority than "default" and "perTier" fees. This field can be missing If there are no different weekend fees in fee strategy.
perWeekend.default	No	Array of objects	Represents possible weekend fee levels, which are applied by default for pairs, if such pairs are not specified in "perTier.pairList" field. Has the same srtucture as "default". If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
perWeekend.perTier	No	Object	Represents possible weekend fee levels for specific sets of pairs indicated in "pairList" field of each tier. "perTier" fee levels have higher priority compared to default fee levels. This field could be missing if Client's strategy configuration doesn't include different fee levels for pair tiers. Has the same structure as "perTier".
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Volume
This request allows Client to receive his trading volume for the last 30 days in USD equivalent.

HTTP REQUEST

POST /get_my_volume

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Get My Volume - Successful request

Request (Client sends request to receive his 30 day trading volume)

{}
Response (CEX.IO Spot Trading responds with Client's 30-day trading volume in USD equivalent)

{
   "ok": "ok",
   "data": {
     "period": "30d",
     "volume": "35016.9181338",
     "currency": "USD"
   }
}
Get My Volume - Invalid request

Request (Client sends request to find transactions without valid JSON object)

{[]}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "error": "Bad Request"
}
Volume Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
period	Yes	String	Represents period for which Client's volume is calculated. Only “30d” value can be returned in this field.
volume	Yes	String (parseable as float)	Represents Client’s cumulative trading volume in “currency” equivalent for returned period.
currency	Yes	String	Represents the currency in which trading volume is calculated. Only “USD” value can be returned in this field.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Create Account
This request allows Client to create new sub-account.

Sub-accounts limit
By default Client can have up to 5 sub-accounts, including main account.
HTTP REQUEST

POST /do_create_account

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Create Account Request Parameters
Create Account - Successful request

Request (Client sends request to create new sub-account)

{
  "accountId": "account2",
  "currency": "BTC"
}
Response (CEX.IO Spot Trading responds with accountId that has been created)

{
  "ok": "ok",
  "data": {
    "accountId": "account2"
  }
}
Create Account - Create new sub-account with already existing accountId name

Request (Client sends request to create new sub-account with indicating already existing accountId)

{
  "accountId": "account2",
  "currency": "USDT"
}
Response (CEX.IO Spot Trading responds with indication of accountId, which has already been created. New accountId with the same name is not created.)

{
  "ok": "ok",
  "data": {
    "accountId": "account2"
  }
}
Create Account - Invalid request (missing mandatory parameter)

Request (Client sends request to create new sub-account without indicating requested accountId name)

{
  "currency": "BTC"
}
Response (CEX.IO Spot Trading responds with error indicating mandatory accountId parameter value is missing in Client's request.)

{ 
  "error": "Mandatory parameter accountId is missing",
  "statusCode": 422
}
Create Account - Invalid request (forbidden symbols used)

Request (Client sends request to create new sub-account with forbidden symbols in requested accountId name)

{
  "accountId": "account%2",
  "currency": "BTC"
}
Response (CEX.IO Spot Trading responds with error that requested accountId contained forbidden symbols.)

{ 
  "error": "Sub-account name should contain only lower and uppercase Latin letters, numbers, underscore (\"_\") or hyphen (\"-\")",
  "statusCode": 500
}
Field Name	Mandatory	Format	Description
accountId	Yes	String	New unique sub-account name which Client requests to create. The value in this field can contain only lower and uppercase Latin letters, numbers, underscore ("_") or hyphen ("-").
currency	Yes	String	Represents crypto or fiat currency symbol which Client expects to be initialy deposited to new sub-account (e.g. from Client's other Spot Trading sub-account, from CEX.IO Wallet acount, from external crypto wallet etc.).
Create Account Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	By default indicates name of new sub-account, which has been created. Nevertheless, if sub-account name requested by Client already exists, CEX.IO Spot Trading will return the name of this sub-account without creating of new sub-account with the same name.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Account Status V3
By using Account Status V3 method, Client can find out current balance and its indicative equivalent in converted currency (by default “USD”), amounts locked in open (active) orders as to each sub-account and currency.

If trading fee balance is available for Client, then response will also contain general trading fee balance data such as promo name, currency name, total balance and expiration date of this promo on Trading Fee Balance.

It’s Client’s responsibility to track his sub-accounts available trading balance as current sub-account balance reduced by the balance amount locked in open (active) orders on sub-account.

HTTP REQUEST

POST /get_my_account_status_v3

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Request Parameters
Get My Account Status V3 for All Accounts for All Currencies

Request (Client sends request to find out his accounts’ statuses for all his accounts for all currencies)

{
  "accountIds": []
}
Response (CEX.IO Spot Trading responds that Client has main account with currencies "USD", "ADA" and "BTC" and sub-account "hallo" with currencies "ETH" and "SHIB". Also, it contains balance equivalents in converted currency for each account and each currency)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "ADA": {
          "balance": "20.24000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "16.21191616"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V3 for selected Sub-accounts for All Currencies

Request (Client sends a request to find out Client's accounts’ statuses for specified accounts for all currencies)

{
  "accountIds": ["hallo", "superhat"]
}
Response (CEX.IO Spot Trading responds that Client has sub-account "hallo" with currencies "ETH" and "SHIB". Sub-account "superhat" status was requested, but is not included into response because Client doesn't have "superhat" sub-account. The main account is not included, because it was not requested)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for Selected Currencies

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies)

{
  "currencies":["USD","BTC"]
}
Response (CEX.IO Spot Trading responds that Client has main account and sub-account "account123", each with currencies "USD" and "BTC". Note that other currencies (like "EUR", "ETH" etc.) are not included into response, because their balances were not requested)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "USD": {
          "balance": "100.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "100.00000000"
        },
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for One Selected Currency

Request (Client sends request to find out his accounts’ statuses for all accounts for "BTC" currency)

{
  "currencies": ["BTC"]
}
Response (CEX.IO Spot Trading responds that main account and sub-account "account123" have "BTC" balances. Note that other currencies (like "USD", "EUR", "SHIB" etc.) and other sub-accounts are not included in the response, because they were not requested or do not contain balances in requested currencies)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V3 - No Account Matching Criteria

Request (Client sends request to find out his accounts’ statuses for main account and sub-account "hallo" only for "EUR" currency balance)

{
  "currencies": ["EUR"],
  "accountIds": ["", "hallo"]
}
Response (CEX.IO Spot Trading responds that Client has no accounts which satisfy request criteria)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {}
  }
}
Get My Account Status V3 for Single Account for Single Currency

Request (Client sends request to find out the main account status for USD currency)

{
  "currencies": ["USD"],
  "accountIds": [""]
}
Response (CEX.IO Spot Trading responds that Client has main account and includes USD balance on it. No other accounts are included, and no other currencies are included, because they were not requested for)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "100.79438200",
          "balanceOnHold": "70.00000000",
          "balanceInConvertedCurrency": "100.79438200"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for Selected Currencies with available Trading Fee Balance

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies. Client has available Trading Fee Balance)

Note that Client has available "lifetimeBonus" and limited "welcome_bonus" for USDT currency

{
  "currencies":["USD","BTC","USDT"]
}
Response (CEX.IO Spot Trading responds that Client has balances in "EUR", "USD", "BTC" and "USDT" on main account, balance in "USD" on "subAccount2" sub-account and two trading fee balances)

Note that Client has available "lifetimeBonus" and limited "welcome_bonus" for USDT currency

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "87683.66518161",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "87683.66518161"
        },
        "BTC": {
          "balance": "564.88201513",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15114322.12602735"
        },
        "USDT": {
          "balance": "995752294.59920270",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "991868860.65026580"
        }
      },
      "subAccount2": {
        "USD": {
          "balance": "123.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "123.00000000"
        }
      }
    },
    "tradingFeeBalancesPerAccounts": {
      "lifetimeBonus": {
        "USDT": {
          "balance": "50.00000000"
        }
      },
      "welcome_bonus": {
        "USDT": {
          "balance": "15.00000000",
          "expirationDate": "2023-07-28T17:20:00.000Z"
        }
      }
    }
  }
}
Get My Account Status V3 - Incorrect Request

Request (Client sends request, however "accountIds" field contains not an Array but a number value)

{
  "accountIds": 3,
  "currencies":["BTC"]
}
Response (CEX.IO Spot Trading responds about request processing error because not an array has been sent in "accountIds" field and "accountIds" array should consist of string type values)

{
  "error": "accountIds array should consist of string type values",
  "statusCode": 422
}
Field Name	Mandatory	Format	Description
currencies	No	Array	List of currencies for which Client wants to find out their accounts' balances. Currencies should be in upper case and of string type. Each currency should be present only once in this array. For example, ["USD", "BTC", "EUR", "BTC"] is not allowed. If this field is missing or contains an empty array ([]), then it means Client wants to find out balances for all available currencies.
accountIds	No	Array	List of account identifiers for which Client wants to find out their accounts' balances. Empty string ("") value in this array represents Client’s main account. Each account identifier should be of string type and should be present only once in this array. For example, ["hallo", "", "account123", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find out balances for all accounts.
Account Status V3 Response Parameters
Field Name	Mandatory	Format	Description
data	Yes	Object	This object contains response details. It should contain balancesPerAccounts and convertedCurrency mandatory fields and could also contain creditLine optional field (if credit line is enabled for Client).
data.convertedCurrency	Yes	String	The currency in which balanceInConvertedCurrency is calculated by CEX.IO Spot Trading. By default only "USD" value is allowed herein.
data.balancesPerAccounts	Yes	Object	This object contains details about Client's currencies' balances as to each account which satisfies request criteria. It might be empty object ("{}"), but this field should be present anyway and it should contain an object. If this field contains an empty object, then it means Client has no accounts which satisfy Client’s request criteria.
data.balancesPerAccounts.X	No	Object	Represents an object which describes X account statuses for each currency. If X is ""(empty string), that means X is main account. Otherwise, it represents X sub-account.
data.balancesPerAccounts.X.YYY	No	Object	Represents an object which describes X account statuses for YYY currency.
data.balancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency. It includes balance which is reserved (locked) for active orders (please find this information in "balanceOnHold" field).
data.balancesPerAccounts.X.YYY. balanceOnHold	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is reserved (locked) for active orders.
data.balancesPerAccounts.X.YYY. balanceInConvertedCurrency	No	String (which can be parsed as Float)	Equivalent in converted currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in converted currency, then this field would be missing.
data.tradingFeeBalancesPerAccounts	No	Object	This object contains details about Client’s trading fee balances. This object can be absent if Client has no available trading fee balances because they were never obtained OR if all of obtained trading fee balances have already expired or were fully utilized.
data.tradingFeeBalancesPerAccounts.X	Yes	Object	Represents an object which describes available trading fee balances which were obtained in the framework of X promo campaign name or as a “lifetimeBonus”.
data.tradingFeeBalancesPerAccounts.X.YYY	Yes	Object	Represents an object which describes details as to YYY currency trading fee balance.
data.tradingFeeBalancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Available amount of YYY currency trading fee balance, expirationDate of which has not been reached yet and which can be used for trading fee utilization.
data.tradingFeeBalancesPerAccounts.X.YYY. expirationDate	No	Datetime	Expiration date of YYY currency trading fee balance. Format: YYYY-MM-DDTHH:MM:SS.sssZ .This field can be absent for “lifetimeBonus” trading fee account, which means YYY trading fee balance amount has no set expiration date.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only ok value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Account Status V2 (deprecated)
Notice
Account Status V2 method is deprecated. Information about current balances and Trading Fee Balance (if available) can be requested only via Account Status V3 ([REST], [WebSocket] specifications) method.
Using Account Status V2 request, Client can find out current balance and its indicative equivalent in converted currency (by default “USD”), available trading balance and amounts which are locked in open (active) orders as to each sub-account and currency.

Available trading balance is calculated as current balance plus overdraft limit (if allowed for the Client) and reduced by the balance amount locked in open (active) orders.

If credit line is enabled for Client, then response will also contain data as to the base currency name, exposure limit, total debt amount, currencies balance equivalents in base currency as to each currency on all Client’s accounts (main account and sub-accounts).

If overdraft limit for specific currency is enabled for Client, then response will also contain data as to amount of overdraft limit for such currency on all Client’s accounts (main account and sub-account), which have balance in specified currency.

HTTP REQUEST

POST /get_my_account_status_v2

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Request Parameters
Get My Account Status V2 for All Accounts for All Currencies

Request (Client sends request to find out his accounts’ statuses for all his accounts for all currencies)

{
  "accountIds": []
}
Response (CEX.IO Spot Trading responds that Client has main account with currencies "USD", "ADA" and "BTC" and sub-account "hallo" with currencies "ETH" and "SHIB". Also, it contains balance equivalents in converted currency for each account and each currency)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "39.79438200",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "ADA": {
          "balance": "20.24000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "20.24000000",
          "balanceInConvertedCurrency": "16.21191616"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "15.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceAvailable": "362523",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V2 for selected Sub-accounts for All Currencies

Request (Client sends a request to find out Client's accounts’ statuses for specified accounts for all currencies)

{
  "accountIds": ["hallo", "superhat"]
}
Response (CEX.IO Spot Trading responds that Client has sub-account "hallo" with currencies "ETH" and "SHIB". Sub-account "superhat" status was requested, but is not included into response because Client doesn't have "superhat" sub-account. The main account is not included, because it was not requested)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "15.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceAvailable": "362523",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V2 for All Accounts for Selected Currencies

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies)

{
  "currencies":["USD","BTC"]
}
Response (CEX.IO Spot Trading responds that Client has main account and sub-account "account123", each with currencies "USD" and "BTC". Note that other currencies (like "EUR", "ETH" etc.) are not included into response, because their balances were not requested)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "39.79438200",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "USD": {
          "balance": "100.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "100.00000000",
          "balanceInConvertedCurrency": "100.00000000"
        },
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "1.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V2 for All Accounts for One Selected Currency

Request (Client sends request to find out his accounts’ statuses for all accounts for "BTC" currency)

{
  "currencies": ["BTC"]
}
Response (CEX.IO Spot Trading responds that main account and sub-account "account123" have "BTC" balances. Note that other currencies (like "USD", "EUR", "SHIB" etc.) and other sub-accounts are not included in the response, because they were not requested or do not contain balances in requested currencies)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "1.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V2 - No Account Matching Criteria

Request (Client sends request to find out his accounts’ statuses for main account and sub-account "hallo" only for "EUR" currency balance)

{
  "currencies": ["EUR"],
  "accountIds": ["", "hallo"]
}
Response (CEX.IO Spot Trading responds that Client has no accounts which satisfy request criteria)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {}
  }
}
Get My Account Status V2 for Single Account for Single Currency

Request (Client sends request to find out the main account status for USD currency)

{
  "currencies": ["USD"],
  "accountIds": [""]
}
Response (CEX.IO Spot Trading responds that Client has main account and includes USD balance on it. No other accounts are included, and no other currencies are included, because they were not requested for)

{
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "100.79438200",
          "balanceOnHold": "70.00000000",
          "balanceAvailable": "30.79438200",
          "balanceInConvertedCurrency": "100.79438200"
        }
      }
    }
  }
}
Get My Account Status V2 - Incorrect Request

Request (Client sends request, however "accountIds" field contains not an Array but a number value)

{
  "accountIds": 3,
  "currencies":["BTC"]
}
Response (CEX.IO Spot Trading responds about request processing error because not an array has been sent in "accountIds" field and "accountIds" array should consist of string type values)

{
  "error": "accountIds array should consist of string type values",
  "statusCode": 422
}
Field Name	Mandatory	Format	Description
currencies	No	Array	List of currencies for which Client wants to find out their accounts' balances. Currencies should be in upper case and of string type. Each currency should be present only once in this array. For example, ["USD", "BTC", "EUR", "BTC"] is not allowed. If this field is missing or contains an empty array ([]), then it means Client wants to find out balances for all available currencies.
accountIds	No	Array	List of account identifiers for which Client wants to find out their accounts' balances. Empty string ("") value in this array represents Client’s main account. Each account identifier should be of string type and should be present only once in this array. For example, ["hallo", "", "account123", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find out balances for all accounts.
Response Parameters
Field Name	Mandatory	Format	Description
data	Yes	Object	This object contains response details. It should contain balancesPerAccounts and convertedCurrency mandatory fields and could also contain creditLine optional field (if credit line is enabled for Client).
data.convertedCurrency	Yes	String	The currency in which balanceInConvertedCurrency is calculated by CEX.IO Spot Trading. By default only "USD" value is allowed herein.
data.creditLine	No	Object	This object contains details about Client's credit line configuration (if enabled for Client), including information about the base currency, exposure limit and total debt. If credit line is not enabled for Client, then this field would be missing.
data.balancesPerAccounts	Yes	Object	This object contains details about Client's currencies' balances as to each account which satisfies request criteria. It might be empty object ("{}"), but this field should be present anyway and it should contain an object. If this field contains an empty object, then it means Client has no accounts which satisfy Client’s request criteria.
data.balancesPerAccounts.X	No	Object	Represents an object which describes X account statuses for each currency. If X is ""(empty string), that means X is main account. Otherwise, it represents X sub-account.
data.balancesPerAccounts.X.YYY	No	Object	Represents an object which describes X account statuses for YYY currency.
data.balancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency. It includes balance which is reserved (locked) for active orders (please find this information in "balanceOnHold" field).
data.balancesPerAccounts.X.YYY. balanceOnHold	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is reserved (locked) for active orders.
data.balancesPerAccounts.X.YYY. balanceAvailable	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is available for trading. It is calculated as current X account balance in YYY currency plus overdraft limit for YYY currency (if enabled for the Client) and reduced by the X account balance amount in YYY currency, which is locked in open (active) orders.
data.balancesPerAccounts.X.YYY. balanceInBaseCurrency	No	String (which can be parsed as Float)	Equivalent in base currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If credit line is not enabled for Client OR if current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in base currency, then this field would be missing.
data.balancesPerAccounts.X.YYY. balanceInConvertedCurrency	No	String (which can be parsed as Float)	Equivalent in converted currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in converted currency, then this field would be missing.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only ok value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Wallet Balance
This request allows Client to receive his CEX.IO Wallet balances, which can be useful for Client to check his current Wallet balances before depositing funds from to Spot Trading sub-accounts or after withdrawing funds from Spot Trading sub-accounts to CEX.IO Wallet account.

HTTP REQUEST

POST /get_my_wallet_balance

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Get My Wallet Balance - Successful request

Request (Client sends request to receive his Wallet account balances)

{}
Response (CEX.IO Spot Trading responds with Client's current balances in BTC, ETH, USD, EUR on his Wallet account)

{
  "ok": "ok",
  "data": {
    "BTC": {
      "balance": "9.72101000"
    },
    "ETH": {
      "balance": "10.000000"
    },
    "USD": {
      "balance": "23567.02"
    },
    "EUR": {
      "balance": "728.99"
    }
  }
}
Wallet Balance Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
XXX	Yes	Object	Represents an object which describes CEX.IO Wallet account status for XXX currency.
XXX.balance	Yes	String (which can be parsed as Float)	Current CEX.IO Wallet account balance in XXX currency.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Orders
This request allows Client to find out info about his orders.

Duplicated clientOrderIds
If Client has several orders with the same clientOrderId (if orders were created in a significant period of time) and will query orders by clientOrderId, response will return an array with all orders’ details in which requested clientOrderId has been indicated by the Client.
HTTP REQUEST

POST /get_my_orders

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Orders Request Parameters
Get My Orders - All Open Orders

Request (Client sends request to find all his open orders for all pairs and all accounts; setting no criteria for orders means that Client wants to get statuses for all open orders)

{}
Response (CEX.IO Spot Trading responds that Client has 3 open orders)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "26", // Market BUY 0.01 BTC/USD with main account
      "clientOrderId": "1465300456557-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Market",
      "timeInForce": null,
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.01000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": null,
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": null,
      "initialOnHoldAmountCcy2": "21.00000000",
      "expireTime": null,
      "effectiveTime": null
    },
    {
      "orderId": "20", // Limit BUY 0.1 BTC/USD at price 400 with "hallo" sub-account
      "clientOrderId": "1465299989578-0",
      "clientId": "BitFok",
      "accountId": "hallo",
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.10000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": "400.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": null,
      "initialOnHoldAmountCcy2": "21.00000000",
      "expireTime": null,
      "effectiveTime": null
    },
    {
      "orderId": "18", // Limit SELL 0.02 BTC/EUR at price 600 with main account
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders with Paging

Request (Client sends request to find all his open orders and wants to see the second page expecting the result set is chunked to pages size 2 (not more than 2 orders per page))

{
  "pageSize": 2,
  "pageNumber": 1
}
Response (supposed that Client has 3 open orders (like in previous example), CEX.IO Spot Trading responds with second page, which includes only the last single order)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders for Selected Pair

Request (Client sends request to find all his open orders for "BTC-EUR" pair)

{
  "pair": "BTC-EUR"
}
Response (CEX.IO Spot Trading responds that Client has 1 open order for BTC-EUR pair)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders for Account and Pair

Request (Client sends request to find all his open orders for currency pair "BTC-USD" and for sub-accounts "hallo" or "superhat")

{
  "accountIds": ["hallo", "superhat"],
  "pair": "BTC-USD"
}
Response (CEX.IO Spot Trading responds that Client has only one open order that satisfies request criteria, this order is on "hallo" sub-account)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "20",
      "clientOrderId": "1465299989578-0",
      "clientId": "BitFok",
      "accountId": "hallo",
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.10000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": "400.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - Accounts, Paging, Period, Empty Result

Request (Client wants to see not more than 50 open orders from main account which were received by server between 2016-06-06T16:11:29 and 2016-06-07T08:53:09)

{
  "accountIds": [""],
  "pageSize": 50,
  "serverCreateTimestampFrom": 1465229489578,
  "serverCreateTimestampTo": 1465289589579
}
Response (CEX.IO Spot Trading responds that Client has no open orders, which satisfy request criteria)

{
  "ok": "ok",
  "data": []
}
Get My Orders - All Archived Orders for Selected Side

Request (Client sends request to find all his archived SELL orders)

{
  "archived": true,
  "side": "SELL",
  "serverCreateTimestampFrom": 1516699048964,
  "serverCreateTimestampTo": 1516699987501
}
Response (supposed that Client has 3 archived orders (like in previous example), CEX.IO Spot Trading responds to Client that he has 1 archived order which satisfies request criteria)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Order - Incorrect Request

Request (Client sends request, but doesn't specify data object)

{}
Response (CEX.IO Spot Trading responds that error occurred. Note: "data" field hold an object value here, not the array)

{
  "error": "Bad Request"
}
Get My Order - Page Size is Too Big

Request (Client sends request to get all archived orders and wishes to get first 5,000 orders list as a response to this request)

{
  "archived": true,
  "pageSize": 5000
}
Response (CEX.IO Spot Trading responds that such request is not allowed. Requested page size is too big, maximum allowed value is 1000)

{
  "error": "Page size is limited to 1000 items"
}
Get My Order - Incorrect Archived Type

Request (Client sends request to get his open orders, however "archived" field value is a number)

{
  "archived": 0
}
Response (CEX.IO Spot Trading responds that such request is not allowed. Field "archived" should be either true, or false, or it should be missing)

{
  "error": "Archived parameter should be boolean"
}
Get My Orders - Single Order by OrderId

Request (Client sends request to find his single order by orderId)

{
  "orderId": 18
}
Response (CEX.IO Spot Trading responds with status of this order)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - Single Order by clientOrderId

Request (Client sends request to find his single order by clientOrderId)

{
  "clientOrderId": "1465299852968-0"
}
Response (CEX.IO Spot Trading responds with status of this order)

{
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Field Name	Mandatory	Format	Description
clientOrderId	No	String	Order identifier assigned by Client. If this field is present, then it means Client wants to see the status of the exact order. In this case, CEX.IO Spot Trading ignores all other parameters in "data" field.
orderId	No	Number	Order identifier assigned by CEX.IO Spot Trading. If both fields "orderId" and "clientOrderId" are present, then CEX.IO Spot Trading ignores "orderId" field. If this field is present (and "clientOrderId" is absent), then it means Client wants to see the status of the exact order. In this case, CEX.IO Spot Trading ignores all other parameters in "data" field.
archived	No	Boolean	If value is true, then it means Client wants to get his completed (archived) orders. "Completed" means that order is in one of its final statuses. If value is false or if this field is missing, it means Client wants to get his open orders. Value should be in boolean type. So values like null, 0, 1, "true", "hallo" and similar are not allowed.
pair	No	String	Currency pair, for which Client wants to find his orders. Pair should contain two currencies in upper case divided by "-" symbol. Pair should be listed in traditional direction. For example, "BTC-USD", but not "USD-BTC". If this field is missing, or if it contains empty string (""), or null, then it means Client wants to find his orders for all pairs.
side	No	String	Side of the orders, for which Client wants to find his orders.
accountIds	No	Array	List of account identifiers, for which Client wants to find his orders. Empty string ("") or null value in this array represents Client’s main account. Each account identifier should be present only once in this array. For example, ["hallo", "", "superhat", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find his orders for all accounts.
serverCreate TimestampFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest server timestamp when order is received. In the result set orders’ serverCreateTimestamp should be greater than or equal to (>=) serverCreateTimestampFrom. Period indicated by serverCreateTimestampFrom and serverCreateTimestampTo values can not be greater than 365 days. This parameter is mandatory if Client queries info about archived orders.
serverCreate TimestampTo	No	Number	UTC timestamp in milliseconds. Represents the latest server timestamp when order is received. In the result set orders’ serverCreateTimestamp should be less than (<) serverCreateTimestampTo. Period indicated by serverCreateTimestampFrom and serverCreateTimestampTo values can not be greater than 365 days. If this field is missing than current date is set by default.
sortOrder	No	String	Sort order of the result set. The result array is sorted by serverCreateTimestamp. "ASC" - ascending order, "DESC" - descending order. If this field is missing then the default sort order is "DESC".
pageSize	No	Number	Because the result might contain too many orders, Client should specify which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of orders in the result for this request. If this field is missing, then the default value of 1000 is used. This value cannot be greater than 1000.
pageNumber	No	Number	Because the result might contain too many orders, Client should specify which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize orders per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 0. If this field is missing, then the default value of 0 is used. This value cannot be lower than 0.
Orders Response Parameters
Field Name	Mandatory	Format	Description
data	Yes	Array or Object	This object contains list of orders which satisfy request criteria. It might be empty array ([]). If this array is empty, then it means Client has no orders, which satisfy Client’s request criteria. The result array is sorted by "clientOrderCreationTimestamp" field with specified order. In case of error, the value of this field should be not Array, but Object.
orderId	Yes	String	Order identifier assigned by CEX.IO Spot Trading.
clientOrderId	Yes	String	Order identifier assigned by Client.
clientId	Yes	String	Client Comp id.
accountId	Yes	String	Represents Client’s account id, which was used for order processing. If this value is null, then it means Client’s main account. Otherwise, it means identifier of Client’s sub-account.
status	Yes	String	Represents current execution status of this order. Status can be PENDING_NEW, NEW, PARTIALLY_FILLED, FILLED, EXPIRED, REJECTED, PENDING_CANCEL, CANCELLED.
statusIsFinal	Yes	Boolean	Represents whether this order is in the final state or not.
currency1	Yes	String	Represents first currency in currency pair of this order.
currency2	Yes	String	Represents second currency in currency pair of this order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timeInForce	Yes	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders where time in force is not applied, for example, for Market orders.
comment	Yes	String	Text, which was provided by Client during order creation. If value is null, then it means Client did not provide such text during order creation.
rejectCode	Yes	Number	Error code if the order is rejected. If value is null, that means there is no error code.
rejectReason	Yes	String	Human readable error description if the order is rejected. If value is null, that means there is no error description.
executedAmountCcy1	Yes	String (which can be parsed as Float)	Represents executed amount in currency1. If this value is null, then it means there is no executed amount (order has no executions).
executedAmountCcy2	Yes	String (which can be parsed as Float)	Represents executed amount in currency2. If this value is null, then it means there is no executed amount (order has no executions).
requestedAmountCcy1	Yes	String (which can be parsed as Float)	Represents order amount in currency1, which was requested by Client. If this value is null, then it means there is no requested amount in currency1 (order should have then requested amount in currency1).
requestedAmountCcy2	Yes	String (which can be parsed as Float)	Represents order amount in currency2, which was requested by Client. If this value is null, then it means there is no requested amount in currency2 (order should have then requested amount in currency2).
initialOnHoldAmountCcy1	Yes	String (which can be parsed as Float)	Represents amount in currency1, which was hold from Client's balance by CEX.IO Spot Trading before order execution. If this value is null, then it means that amount in currency1 was not hold from Client's account for this order.
initialOnHoldAmountCcy2	Yes	String (which can be parsed as Float)	Represents amount in currency2, which was hold from Client's balance by CEX.IO Spot Trading before order execution. If this value is null, then it means that amount in currency2 was not hold from Client's account for this order.
feeAmount	Yes	String (which can be parsed as Float)	Represents order commission amount, which was charged for this order. If this value is null, then it means there is no commission amount charged for this order.
feeCurrency	Yes	String	Represents order commission currency, in which feeAmount is calculated for this order.
price	Yes	String (which can be parsed as Float)	Represents order price, which was provided by Client during order creation. If this value is null, then it means there is no requested price for this order. It happens for order where price cannot be requested, for example, Market orders or Stop orders.
averagePrice	Yes	String (which can be parsed as Float)	Represents average order execution price. If this value is null, then it means there is no executed amount (order has no executions).
clientCreateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents a timestamp provided by Client during creation of the order.
serverCreateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents server timestamp when order was received.
lastUpdateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents server timestamp when order changed its state last time.
expireTime	Yes	Number	UTC timestamp in milliseconds. Represents an expired timestamp provided by Client during creation of the order. If this value is null, then it means Client did not provide expire time during order creation.
effectiveTime	Yes	Number	UTC timestamp in milliseconds. Represents an effective timestamp provided by Client during creation of the order. If this value is null, then it means that Client did not provide effective time during order creation.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
New Order
This method works only with CEX.IO Spot Trading sub-accounts.
Client can place new orders via REST API by using Do My New Order Request. The parameters and samples of such requests are shown in this section.

Response message indicates the last up-to-date status of order which is available in the system at the moment of sending the response.

If the Client did not receive a Response message to Do My New Order Request - the Client can query current status of the order by using Get My Orders Request with clientOrderId parameter.

When sending a request for new order, it is highly recommended to use clientOrderId parameter which corresponds to the specific new order request on the client's side. Spot Trading protects multiple placing of orders with the same clientOrderId for a reasonable period of time.

If more than one new orders with identical clientOrderId and other order parameters are identified - Spot Trading places only the first order and returns the status of such order to the Client in response to the second and subsequent new order requests with the same parameters. If orders with identical clientOrderId but with different other order parameters are identified - Spot Trading processes only the first order and rejects the second and subsequent new order requests with the same clientOrderID but with different other order parameters. Nevertheless, if Client creates more than one orders with same clientOrderId in a significant period of time, order with same clientOrderId can be accepted by the system. It's Client's responsibility to control unique indication of clientOrderIds.

Order limitations
The system has a limit on the number of active (open) orders. By default, Client can have a maximum of 20 active taker orders. Once limit is reached, the system will reject any new orders with a reject reason “Too many active orders” until the total number of active orders is below the limit.
Important notice regarding Market orders
CEX.IO Spot Trading can partially execute market orders in order to prevent Client's possible loss. Market orders that were executed but not completely filled will have "CANCELED" status.
HTTP REQUEST

POST /do_my_new_order

API Rate Limit Cost: 1

API Key Permission

This method requires “Trade” permission set for API Key.

New Order Request Parameters
Do My New Order - place Limit SELL order

Request (Client requests to place a Limit order to SELL 0.01 BTC for USD at price 7,500)

{
  "clientOrderId": "1521711134775",
  "accountId": "testAccount",
  "currency1": "BTC",
  "currency2": "USD",
  "side": "SELL",
  "timestamp": 1521711134775,
  "orderType": "Limit",
  "timeInForce": "GTC",
  "amountCcy1": "0.01",
  "price": 7500,
  "comment": "v_overdraft_test"
}
Response (CEX.IO Spot Trading sends acknowledgement message with a current status of order)

{
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "17062",
    "clientOrderId": "1521711134775",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998836_0_1",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "7500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Do My New Order - place Market BUY order

Request (Client requests to place a Market order to BUY 10 BTC for USD)

{
  "accountId": "someAccount01",
  "clientOrderId": "manual_1614173000191",
  "currency1": "BTC",
  "currency2": "USD",
  "side": "BUY",
  "timestamp": 1614173000191,
  "orderType": "Market",
  "amountCcy1": 10
}
Response (CEX.IO Spot Trading sends acknowledgement message with a status of order. The order has been rejected due to insufficient funds on Client’s account)

{
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "338306",
    "clientOrderId": "manual_1614173000191",
    "accountId": "someAccount01",
    "status": "REJECTED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "10.00000000",
    "requestedAmountCcy2": null,
    "orderType": "Market",
    "timeInForce": null,
    "comment": null,
    "executionType": "Rejected",
    "executionId": "1614012430993_103_295",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "averagePrice": null,
    "feeAmount": null,
    "feeCurrency": null,
    "orderRejectReason": "{\"code\":403,\"reason\":\"Insufficient funds\"}",
    "rejectCode":403,
    "rejectReason":"Insufficient funds"
  }
}
Do My New Order - place Market BUY order

Request (Client requests to place a Market order to BUY 10 BTC for USD)

{
  "accountId": "someAccount01",
  "clientOrderId": "manual_1614173000191",
  "currency1": "BTC",
  "currency2": "USD",
  "side": "BUY",
  "timestamp": 1614173000191,
  "orderType": "Market",
  "amountCcy1": 10
}
Response (CEX.IO Spot Trading sends acknowledgement message with a status of order. The order has been rejected due to the exceeded limit of active (open) orders)

{
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "338306",
    "clientOrderId": "manual_1614173000191",
    "accountId": "someAccount01",
    "status": "REJECTED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "10.00000000",
    "requestedAmountCcy2": null,
    "orderType": "Market",
    "timeInForce": null,
    "comment": null,
    "executionType": "Rejected",
    "executionId": "1614012430993_103_295",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "averagePrice": null,
    "feeAmount": null,
    "feeCurrency": null,
    "orderRejectReason": "{\"code\":437,\"reason\":\"Too many active orders\"}",
    "rejectCode":437,
    "rejectReason":"Too many active orders"
  }
}
Do My New Order - place Limit BUY order

Request (Client requests to place a Limit order to SELL 0.01 BTC for USD at price 18,500)

{
  "clientOrderId": "1521713494191",
  "accountId": "testAccount",
  "currency1": "BTC",
  "currency2": "USD",
  "side": "BUY",
  "timestamp": 1521713494191,
  "orderType": "Limit",
  "timeInForce": "GTC",
  "amountCcy1": "0.01",
  "price": 18500,
  "comment": "v_overdraft_test"
}
Response (CEX.IO Spot Trading sends acknowledgement message with a current status of order)

{
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "17065",
    "clientOrderId": "1521713494191",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998877_2_4",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Do My New Order - Invalid request

Request (Client requests to place a Limit order with missing price field)

{
  "clientOrderId": "1521736196695",
  "accountId": "testAccount",
  "currency1": "BTC",
  "currency2": "USD",
  "side": "BUY",
  "timestamp": 1521736196695,
  "orderType": "Limit",
  "timeInForce": "GTC",
  "amountCcy1": "0.001",
  "comment": "v_overdraft_test"
}
Response (CEX.IO Spot Trading sends response that has no field "ok" and has "error" field containing error description)

{
  "error": "Mandatory parameter price is missing"
}
Field Name	Mandatory	Format	Description
clientOrderId	No	String	Order identifier assigned by Client. If this field is absent, it will be set automatically to current timestamp in milliseconds.
accountId	Yes	String	Client’s sub-account ID. Empty string value ("") is not allowed in this field.
currency1	Yes	String	Represents first currency in currency pair of this order.
currency2	Yes	String	Represents second currency in currency pair of this order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timestamp	Yes	Number	UTC timestamp in milliseconds, represents client-side order creation time. By default, timestamp should be within 30000 ms timeframe with server time, otherwise, order will be rejected. Please be informed that default timeframe value 30000 ms can be changed for the Client by request.
timeInForce	No	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders, where time in force is not applied, for example, for Market orders.
comment	No	String	Comment for order. Maximum length of comment string is 255 characters. If value is null, then it means Client did not provide such text during order creation.
amountCcy1	No	String (parseable as Float)	Represents order amount in currency1. This value can be null if order requests amount in currency2.
amountCcy2	No	String (parseable as Float)	Represents order amount in currency2. This value can be null if order requests amount in currency1.
price	No	String (parseable as Float)	Represents order price. Please omit this field for orders, where price cannot be requested, for example, Market orders or Stop orders.
expireTime	No	Number	UTC timestamp in milliseconds. If Expire Time is in the past, order will be rejected.
stopPrice	No	String (parseable as Float)	Stop Price for Stop and StopLimit types of orders.
New Order Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
clientId	Yes	String	Client CompId.
accountId	Yes	String	Client’s sub-account ID via which order has been created.
orderId	Yes	String	Order identifier assigned by CEX.IO Spot Trading. "NONE" value can be returned if order is rejected due to validation errors: failed minOrderAmountCcy, maxOrderAmountCcy, lotSizeCcy, max active orders checks.
clientOrderId	Yes	String	Order identifier assigned by Client.
status	Yes	String	Represents current execution status of this order.
currency1	Yes	String	Represents first currency in currency pair of the order.
currency2	Yes	String	Represents second currency in currency pair of the order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timeInForce	Yes	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders, where time in force is not applied, for example, for Market orders.
comment	Yes	String	Text value that was provided by Client during order creation. If value is null, it means Client did not provide such text during order creation.
orderRejectReason	No	String	Text field describing rejection reason. Often (but not always) it is a JSON representation of an object with two fields: "code" — numeric error code; "reason" — human readable error description. If value is null, that means there is no error description.
rejectCode	No	Number	Numeric error code.
rejectReason	No	String	Text field indicating human readable error description. If value is null, that means there is no error description.
executedAmountCcy1	Yes	String (which can be parsed as Float)	Represents executed amount in currency1. If this value is 0, then it means there is no executed amount (order has no executions).
executedAmountCcy2	Yes	String (which can be parsed as Float)	Represents executed amount in currency2. If this value is 0, then it means there is no executed amount (order has no executions).
requestedAmountCcy1	Yes	String (which can be parsed as Float)	Represents order amount in currency1, which was requested by Client. If this value is null, then it means there is no requested amount in currency1 (order should have then requested amount in currency2)
requestedAmountCcy2	Yes	String (which can be parsed as Float)	Represents order amount in currency2, which was requested by Client. If this value is null, then it means there is no requested amount in currency2 (order should have then requested amount in currency1).
feeAmount	Yes	String (which can be parsed as Float)	Represents order commission amount, which was charged for this order . If this value is 0, then it means there is no commission amount charged for this order so far.
feeCurrency	Yes	String	Represents order commission currency, in which feeAmount is calculated.
price	Yes	String (which can be parsed as Float)	Represents order price, which was provided by Client during order creation. If this value is null, then it means there is no requested price for this order. It happens for orders, where price cannot be requested, for example, Market orders or Stop orders.
averagePrice	Yes	String (which can be parsed as Float)	Represents average order execution price. If this value is null, then it means there is no executed amount (order has no executions).
expireTime	Yes	Number	UTC timestamp in milliseconds. Represents an expired timestamp provided by Client during creation of the order. If this value is null, then it means Client did not provide expire time during order creation.
effectiveTime	Yes	Number	UTC timestamp in milliseconds. Represents an effective timestamp provided by Client during creation of the order. If this value is null, then it means that Client did not provide effective time during order creation.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Cancel Order
Client can cancel orders.

HTTP REQUEST

POST /do_cancel_my_order

API Rate Limit Cost: 1

API Key Permission

This method requires “Trade” permission set for API Key.

Cancel Order Request Parameters
Do Cancel My Order - successful cancellation of Limit SELL BTC order by clientOrderId

Request (Client requests to cancel order that was created with clientOrderId equal to "1521719532817")

{
  "clientOrderId": "1521719532817",
  "cancelRequestId": "cancel_1521719532817",
  "timestamp": 1521719535310
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming that the cancellation request is accepted)

{
  "ok": "ok",
  "data": {}
}
Do Cancel My Order - successful cancellation of Limit BUY BTC order by orderId

Request (Client requests to cancel order, to which CEX.IO Spot Trading assigned orderId equal to 123456789)

{
  "orderId": 123456789,
  "cancelRequestId": "cancel_1521719532818",
  "timestamp": 1521719535311
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming that the cancellation request is accepted)

{
  "ok": "ok",
  "data": {}
}
Do Cancel My Order - incorrect request with missing "orderId" and "clientOrderId" parameters

Request (Client requests to cancel order but doesn't indicate either "orderId" or "clientOrderId" parameters)

{
  "cancelRequestId": "cancel_1521719532834",
  "timestamp": 1521719535322
}
Response (CEX.IO Spot Trading responds that either "clientOrderId" or "orderId" should be specified)

{
  "error": "ClientOrderId or orderId should be specified",
  "statusCode": 422
}
Do Cancel My Order - incorrect request with both "orderId" and "clientOrderId" parameters

Request (Client requests to cancel order but indicates both "orderId" and "clientOrderId" parameters)

{
  "clientOrderId": "1521719532817",
  "orderId": 123456789,
  "cancelRequestId": "cancel_1521719532899",
  "timestamp": 1521719535349
}
Response (CEX.IO Spot Trading responds that either "clientOrderId" or "orderId" should be specified - not both of them)

{
  "error": "Only one of the fields ClientOrderId or orderId should be specified, not both",
  "statusCode": 422
}
Field Name	Mandatory	Format	Description
orderId	No	Number	Order identifier assigned by CEX.IO Spot Trading. If this field is present and contains valid value, then it means Client wants to cancel specific order with orderId, which was assigned by CEX.IO Spot Trading. If "orderId" field is present, then "clientOrderId" should be absent. Either "orderId" or "clientOrderId" should be indicated in request anyway.
clientOrderId	No	String	Order identifier assigned by Client when the order was created. If this field is present and contains valid value, then it means Client wants to cancel specific order with clientOrderId indicated by Client at order placement. If "clientOrderId" field is present, then "orderId" field should be absent. Either "clientOrderId" or "orderId" should be indicated in request anyway.
cancelRequestId	Yes	String	Cancel request identifier assigned by Client.
timestamp	Yes	Number	Current client time - UTC timestamp in milliseconds.
Cancel Order Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Cancel All Orders
Client can cancel all open orders via REST API.

HTTP REQUEST

POST /do_cancel_all_orders

API Rate Limit Cost: 5

API Key Permission

This method requires “Trade” permission set for API Key.

Cancel All Orders Request Parameters
Do Cancel All Orders

Request (Client requests to cancel all open orders)

{}
Response (CEX.IO Spot Trading sends acknowledgement message confirming the list of client’s open orders, which system is trying to cancel. There are 2 open orders in this case)

{
  "ok": "ok",
  "data": {
    "clientOrderIds": ["1575459943138","1575459942041"]
  }
}
Do Cancel All Orders - There are no client’s open orders

Request (Client requests to cancel all open orders)

{}
Response (CEX.IO Spot Trading sends acknowledgement message confirming there are no client’s open orders)

{
  "ok": "ok",
  "data": {
    "clientOrderIds": []
  }
}
Field Name	Mandatory	Format	Description
accountIds	No	Array	List of account identifiers on which Client wants to cancel all open orders. Empty string ("") value in this array represents Client’s Wallet account. Each account identifier should be of string type, e.g. ["subAccount1", "", "account123", "hallo"]. If this field is missing or if it contains an empty array ([]), then it means Client wants to cancel all open orders on all Spot Trading sub-accounts and Wallet account.
Cancel All Orders Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
clientOrderIds	Yes	Array	This object contains list of client’s open orders, which Spot Trading system is trying to cancel on all accounts or specific accounts (if Client indicated specific accounts in accountIds field of the request). It might be an empty array ([]). If this array is empty, then it means there are no client’s open orders which satisfy requested criteria.
Order Book
This method allows Client to receive current order book snapshot for specific trading pair.

HTTP REQUEST

POST /get_order_book

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Order Book Request Parameters
Get Order Book request for one trading pair.

Request (Client sends request to receive order book snapshot for BTC-USD trading pair)

{
  "pair": "BTC-USD"
}
Response (CEX.IO Spot Trading successfully responds to the request with current order book snapshot for BTC-USD trading pair)

{
  "ok": "ok",
  "data": {
    "timestamp": 1676037221433,
    "currency1": "BTC",
    "currency2": "USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}
Field Name	Mandatory	Format	Description
pair	Yes	String	Trading pair, for which Client wants to request an Order Book snapshot. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
timestamp	Yes	Number	Order book snapshot server time - UTC timestamp in milliseconds.
currency1	Yes	String	The first currency in the requested trading pair.
currency2	Yes	String	The second currency in the requested trading pair.
bids	Yes	Array	This array contains a list of bids of the order book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book.
asks	Yes	Array	This array contains a list of asks of the Order Book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Candles
By using Candles method Client can receive historical OHLCV candles of different resolutions and data types.

Client can indicate additional timeframe and limit filters to make response more precise to Client’s requirements.

HTTP REQUEST

POST /get_candles

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Candles Request Parameters
Get Candles request for BTC-USD trading pair.

Request (Client sends request to receive 1 bestAsk open candles for BTC-USD trading pair as of current time)

{
  "pair": "BTC-USD",
  "fromISO": 1675953089378,
  "limit": 1,
  "dataType": "bestAsk",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading successfully responds to the request, 1 closed 1h candle)

{
  "ok": "ok",
  "data": {
    "timestamp": 1675951200000,
    "open": 22945.3,
    "high": 23163.4,
    "low": 22913,
    "close": 22920.1,
    "volume": 779.00675644,
    "resolution": "1h",
    "isClosed": true,
    "timestampISO": "2023-02-09T14:00:00.000Z"
  }
}
Request (Client sends request to receive 1 bestBid open candles for 3 pairs as of current time)

{
  "pairsList": ["BTC-USD","ETH-USD","XXX-YYY"],
  "toISO": 1676041279412,
  "limit": 1,
  "dataType": "bestBid",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading successfully responds to the request, pairs with 1 open candle for each + unsupported pair message)

{ 
  "ok": "ok",
  "data": {
    "BTC-USD":[ 
      {
        "timestamp": 1676041200000,
        "high": 21791.3,
        "low": 21772.4,
        "close": 21782.6,
        "open": 21791.3,
        "volume": 36.87654321,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "ETH-USD":[ 
      {
        "timestamp": 1676041200000,
        "high": 1545.21,
        "low": 1543.65,
        "close": 1544.95,
        "open": 1545.21,
        "volume": 34.12345678,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "XXX-YYY": {
      "error": { 
        "code": 400, 
        "reason": "Unsupported pair XXX-YYY" 
      }
    } 
  }
}
Request (Client sends request to receive last 1 hour bestAsk candle for LUNC-BUSD pair)

{
  "pair": "LUNC-BUSD",
  "toISO": 1676042478383,
  "limit": 1,
  "dataType": "bestAsk",
  "resolution": "1h"
}
Response (CEX.IO Spot Trading responds with empty candle, which means no candle is available upon requested parameters)

{
  "ok": "ok",
  "data": {
    "timestamp": 1676041200000,
    "resolution": "1h",
    "timestampISO": "2023-02-10T15:00:00.000Z"
  }
}
Field Name	Mandatory	Format	Description
pair	No	String	Trading pair, for which Client wants to receive historical OHLCV candles. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles for one specific trading pair. If "pair" field is present, then "pairsList" field should be absent. Either "pair" or "pairsList" should be indicated in the request anyway.
pairsList	No	Array or String	Array with trading pairs, for which Client wants to receive last historical OHLCV candles. At least 1 trading pair should be indicated in this field. If this field is present and contains valid values, then it means Client wants to receive last OHLCV candle for each indicated trading pair in the list. If "pairsList" field is present, then "pair" field should be absent. Either "pairsList" or "pair" should be indicated in the request anyway.
fromISO	No	Number (UTC timestamp)	The starting moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the first one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
toISO	No	Number (UTC timestamp)	The last moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the last one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
limit	No	Number (Integer)	Maximum number of OHLCV candles to be returned in response. Indicated number should be greater than zero. This field is mandatory if at least one of “fromISO” or “toISO” fields is specified in request. This field should be absent if both “fromISO” and “toISO” are specified in request. If “pairsList” field is specified in the request, then the value of this field should equal 1 (only last candle for each requested trading pair will be returned in response).
dataType	Yes	String	The type of data, on the basis of which returned OHLC prices in candles should be calculated. Allowed values: “bestAsk”, “bestBid”.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
Candles Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
XXX-YYY	No	Object or Array	Represents an array or an object which describes XXX-YYY trading pair candle details if pairsList parameter was indicated in the request. If it represents an array - then candle for XXX-YYY trading pair is presented, if an object - then candle for XXX-YYY trading pair could not be returned and error description is returned inside an object. If pairsList was not indicated in the request, then this parameter should be absent.
XXX-YYY.N	No	Object	Represents an object with XXX-YYY trading pair candle or error description.
timestamp	Yes	Number	OHLCV candle timestamp - UTC timestamp in milliseconds.
open	No	Number (Float)	Opening price of OHLCV candle in quote currency.
high	No	Number (Float)	Highest price of OHLCV candle in quote currency, which was reached during candle timeframe.
low	No	Number (Float)	Lowest price of OHLCV candle in quote currency, which was reached during candle timeframe.
close	No	Number (Float)	Closing price of OHLCV candle in quote currency.
volume	No	Number (Float)	Total base currency amount traded during a specific candle timeframe period.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
isClosed	No	Boolean	Indicates whether the specific candle is currently closed. If the value of this field is true, then it means this candle has been already closed. If this field is absent, then it means this candle is still open.
timestampISO	Yes	String	OHLCV candle date & time in ISO format (“YYYY-MM-DDTHH:mm:ss.SSSZ").
error	No	Object	If this field is present, then requested candle can not be returned. Represents human readable error reason of why request is not successful.
error.code	No	Number	Represents numeric code of occurred error.
error.reason	No	String	Represents human readable error reason of why candle could not be returned.
Trade History
This method allows Client to obtain historical data as to occurred trades upon requested trading pair.

Client can supplement Trade History request with additional filter parameters, such as timeframe period, tradeIds range, side etc. to receive trades which match request parameters.

HTTP REQUEST

POST /get_trade_history

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Trade History Request Parameters
Get Trade History request

Request (Client sends request to receive trade history for BTC-USD trading pair)

{
  "pair": "BTC-USD"
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "ok": "ok",
  "data": {  
    "pageSize": 100,
    "trades": [
      {
        "tradeId": "1675399566795-0",
        "dateISO": "2023-02-03T04:46:06.795Z",
        "side": "SELL",
        "price": "21149.2",
        "amount": "10.00000000"
      },
      {
        "tradeId": "1675401193999-0",
        "dateISO": "2023-02-03T05:13:13.999Z",
        "side": "BUY",
        "price": "25896.0",
        "amount": "0.00000001"
      },
      {
        "tradeId": "1675401207800-0",
        "dateISO": "2023-02-03T05:13:27.800Z",
        "side": "SELL",
        "price": "21146.0",
        "amount": "0.00000001"
      }
    ]
  }
}
Field Name	Mandatory	Format	Description
pair	Yes	String	Trading pair, for which Client wants to receive trades history. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
side	No	String	Side of requested trades. If this field is present, it should contain only one of allowed values: “BUY” or “SELL”. If this field is not indicated in the request, then response would contain trades for "BUY" and "SELL" sides.
fromDateISO	No	String	The starting moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If “fromDateISO” and “pageSize” parameters are not specified in request, then by default last 1000 trades will be returned in response. If this field is present, then “fromTradeId” and “toTradeId” fields should not be indicated in the request.
toDateISO	No	String	The last moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If this field is present, then “fromDateISO” should also be present, “fromTradeId” and “toTradeId” fields should be absent.
fromTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, starting from which subsequent trades should be returned in response. If this field is present, then “fromDateISO” and “toDateISO” fields should not be indicated in the request.
toTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, which should be the last trade returned in response. If this field is present, then “fromTradeId” should also be present, “fromDateISO” and “toDateISO” fields should not be indicated in the request.
pageSize	No	Number (Integer)	Maximum number of trades, which should be returned in response. If this field is present then the value should be more than zero and not more than 1000. If indicated value is more than 1000, the response will still contain only up to 1000 trades max. If this field is not specified in request, then by default 100 trades would be returned in response.
Trade History Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
pageSize	Yes	Number (Integer)	Maximum number of trades, which can be returned in response.
trades	Yes	Array	An array containing data as to each trade event which satisfies requested criteria. If request is successful, this field should be present in response. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted by “dateISO” value in ascending order (from older to newer, considering “fromDateISO” / “toDateISO” or “fromTradeId” / “toTradeId” if indicated in request). If a few trade events occurred at the same moment of time, then such trade events are sorted additionally by “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	If trade event is available, then represents an object which describes specific Х trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade in base currency.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Transaction History
This request allows Client to find his financial transactions (deposits, withdrawals, internal transfers, commissions or trades).

HTTP REQUEST

POST /get_my_transaction_history

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Transaction History Request Parameters
Get My Transaction History - For Main Account with specified period

Request (Client sends request to find all transactions for the main account with specified period)

{
  "accountId": "",
  "type": "",
  "dateTo": 1614336230587,
  "dateFrom": 1613101662720,
  "sortOrder": "ASC"
}
Response

{
  "ok": "ok",
  "data": [
    {
      "transactionId": "trade_335805_finalization_BTC",
      "timestamp": "2021-02-12T09:44:35.078Z",
      "accountId": "",
      "type": "trade",
      "amount": "0.00200000",
      "details": "Finalization Trade orderId='335805' for DEMO_USER",
      "currency": "BTC"
    },
    {
      "transactionId": "trade_335805_finalization_USD",
      "timestamp": "2021-02-12T09:44:35.078Z",
      "accountId": "",
      "type": "trade",
      "amount": "-33.40944038",
      "details": "Finalization Trade orderId='335805' for DEMO_USER",
      "currency": "USD"
    },
    {
      "transactionId": "commission_trade_335805",
      "timestamp": "2021-02-12T09:44:35.090Z",
      "accountId": "",
      "type": "commission",
      "amount": "-0.16704721",
      "details": "Commission for orderId='335805' for DEMO_USER",
      "currency": "USD"
    }
  ]
}
Get My Transaction History - For Main Account with Paging

Request (Client sends request to find transactions for the main account and wants to see second page expecting the result set is chunked to pages size 3 (not more than 3 transactions per page))

{
  "accountId": "",
  "type": "",
  "pageSize": 3,
  "pageNumber": 2,
  "sortOrder": "DESC"
}
Response

{
  "ok": "ok",
  "data": [
    {
      "transactionId": "commission_trade_338348",
      "timestamp": "2021-02-24T16:36:23.271Z",
      "accountId": "",
      "type": "commission",
      "amount": "-1242.90844594",
      "details": "Commission for orderId='338348' for DEMO_USER",
      "currency": "USD"
    },
    {
      "transactionId": "trade_338348_finalization_BTC",
      "timestamp": "2021-02-24T16:36:23.259Z",
      "accountId": "",
      "type": "trade",
      "amount": "-1.56398259",
      "details": "Finalization Trade orderId='338348' for DEMO_USER",
      "currency": "BTC"
    },
    {
      "transactionId": "trade_338348_finalization_USD",
      "timestamp": "2021-02-24T16:36:23.259Z",
      "accountId": "",
      "type": "trade",
      "amount": "77753.71512521",
      "details": "Finalization Trade orderId='338348' for DEMO_USER",
      "currency": "USD"
    }
  ]
}
Get My Transaction History - Deposit Transactions for Main Account

Request (Client sends request to find all deposit transactions for main account)

{
  "accountId": "",
  "type": "deposit",
  "sortOrder": "DESC"
}
Response

{
  "ok": "ok",
  "data": [
    {
      "transactionId": "deposit_135857381",
      "timestamp": "2021-02-19T10:56:16.255Z",
      "accountId": "",
      "type": "deposit",
      "amount": "0.05000000",
      "details": "Deposit depositId=135857381 for DEMO_USER",
      "currency": "BTC"
    }
  ]
}
Get My Transaction History - For non-existing sub-account

Request (Client sends request for non-existing sub-account)

{
  "accountId": "nonExistingAcc"
}
Response

{
  "ok": "ok",
  "data": []
}
Get My Transaction History - Incorrect "type" parameter

Request (Client sends request with incorrect "type" parameter)

{
  "accountId": "",
  "type": "limitOrder"
}
Response

{
  "error": "Operation type is not supported. Supported types: trade,commission,deposit,withdraw,internalTransfer"
}
Get My Transaction History - Page size is more than 100

Request

{
  "accountId": "",
  "type": "",
  "pageSize": 150,
  "pageNumber": 1
}
Response

{
  "error": "Page size is limited to 100 items"
}
Get My Transaction History - For Incorrect Request

Request (Client sends request to find transactions without valid JSON object)

{[]}
Response

{
  "error": "Bad Request"
}
Field Name	Mandatory	Format	Description
accountId	No	String	Account identifier, for which Client wants to find transactions. Empty string ("") or null value in this field represents Client’s main account. If this field is missing, then it means Client wants to find transactions for the main account and all sub-accounts.
type	No	String	If this field is present and contains one of the allowed values, then it means Client wants to get only transactions related to specified operation type. Allowed values are: "trade", "deposit", "withdraw", "internalTransfer, "commission". If this field is missing or if this field is present but contains an empty string (""), then it means Client wants to get transactions for all operation types.
dateFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest moment in time when transactions were created. In the result set transactions’ timestamp field value should be greater than or equal to (>=) dateFrom. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateFrom should be less than the value in the field dateTo.
dateTo	No	Number	UTC timestamp in milliseconds. Represents the latest moment in time when transactions were created. In the result set transactions’ timestamp field value should be less than (<) dateTo. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateTo should be greater than the value in the field dateFrom.
sortOrder	No	String	Sort order of the result set. The result array is sorted by "timestamp" field. Allowed values: "ASC" - ascending order, "DESC" - descending order. If this field is missing then the default sort order is "DESC", so recently created transactions come first and oldest transactions come last.
pageSize	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of transactions in the result for this request and cannot be greater than 100. If this field is missing, then the default value of 100 is used. If this field contains one of the allowed values and, simultaneously, the pageNumber field is missing, then the default pageNumber value is applied. Specifying the value in the field pageSize is mandatory if the value in the field pageNumber is also sent in the Client's request.
pageNumber	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize transactions per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 1. If this field is missing, then the default value of 1 is used. This value cannot be lower than 1. If any valid value is specified in this field, then it is mandatory to also send the value in the field pageSize in the Client’s request.
Transaction History Response Parameters
Field Name	Mandatory	Format	Description
data	Yes	Array or Object	This object contains list of transactions, which satisfies request criteria. It might be empty array ([]). If this array is empty, then it means there are no transactions, which satisfy Client’s request criteria. In case of error, the value of this field should be not Array, but Object.
transactionId	Yes	String	Unique identifier of transaction.
timestamp	Yes	Datetime	Represents server timestamp when this transaction happened. Format: YYYY-MM-DDTHH:MM:SS.sssZ .
accountId	Yes	String	Represents the Account ID.
type	Yes	String	Represents the type of this operation. Allowed values are "trade", "deposit", "withdraw", "internalTransfer", "commission".
amount	Yes	String (which can be parsed as Float)	Represents amount of the transaction.
details	Yes	String	Represents transaction details.
currency	Yes	String	Represents the currency of the transaction.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Funding History
This request allows Client to find his deposit and withdrawal transactions.

HTTP REQUEST

POST /get_my_funding_history

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Funding History Request Parameters
Get My Funding History - For Main Account and all sub-accounts

Request (Client sends request to find deposit/withdrawal transactions for the main account and all sub-accounts)

{}
Response (CEX.IO Spot Trading responds that Client has 2 withdrawal transactions (1 withdrawal from sub-account and 1 withdrawal from main account) and 3 deposit transactions (2 deposits to sub-accounts and 1 deposit to main account))

{
  "ok": "ok",
  "data": [
    {
      "txId": 148126,
      "clientId": "TestClient",
      "accountId": "100107_test",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "81.04000000",
      "commissionAmount": "1.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:25.272Z"
    },
    {
      "txId": 148127,
      "clientId": "TestClient",
      "accountId": "",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "11.34000000",
      "commissionAmount": "0.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:17.193Z"
    },
    {
      "txId": 148128,
      "clientId": "TestClient",
      "accountId": "100108_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "15.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:18:48.682Z"
    },
    {
      "txId": 148129,
      "clientId": "TestClient",
      "accountId": "100109_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:17:45.399Z"
    },
    {
      "txId": 148130,
      "clientId": "TestClient",
      "accountId": "",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:16:41.585Z"
    }
  ]
}
Get My Funding History - For Main Account and all Sub-accounts with Paging

Request (Client sends request to find deposit/withdrawal transactions for the main account and all sub-accounts and wants to see the first page expecting the result set is chunked to pages size 2 (not more than 2 transactions per page))

{
  "pageSize": 2,
  "pageNumber": 1
}
Response (Supposed that Client has 5 transactions (like in previous example), CEX.IO Spot Trading responds with the first page, which includes 2 transactions)

{
  "ok": "ok",
  "data": [
    {
      "txId": 148126,
      "clientId": "TestClient",
      "accountId": "100107_test",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "81.04000000",
      "commissionAmount": "1.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:25.272Z"
    },
    {
      "txId": 148127,
      "clientId": "TestClient",
      "accountId": "",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "11.34000000",
      "commissionAmount": "0.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:17.193Z"
    }
  ]
}
Get My Funding History - For Specified Sub-Account

Request (Client sends request to find deposit/withdrawal transactions for specified sub-account)

{
  "accountId": "123"
}
Response (CEX.IO Spot Trading responds with deposit/withdrawal transactions for specified sub-account)

{
  "ok": "ok",
  "data": [
    {
      "txId": 148129,
      "clientId": "TestClient",
      "accountId": "123",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:17:45.399Z"
    }
  ]
}
Get My Funding History - Deposit Transactions for Main Account and all Sub-accounts with specified Period

Request (Client sends request to find all deposit transactions for main account and all sub-accounts, which happened within specified period)

{
  "direction": "deposit",
  "dateFrom": 1514337745869,
  "dateTo": 1614337745869
}
Response (CEX.IO Spot Trading responds that Client has only one transaction, which satisfies requested criteria)

{
  "ok": "ok",
  "data": [
    {
      "txId": 148128,
      "clientId": "TestClient",
      "accountId": "100108_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "15.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:18:48.682Z"
    }
  ]
}
Get My Funding History - For Incorrect Request

Request (Client sends request to find some deposit/withdrawal transactions without valid JSON object)

{[]}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed)

{
  "error": "Bad Request"
}
Field Name	Mandatory	Format	Description
accountId	No	String	Account identifier, for which Client wants to find transactions. Empty string ("") or null value in this field represents Client’s main account. If this field is missing, then it means Client wants to find deposits and withdrawals for the main account and all sub-accounts.
txId	No	Number	Transaction identifier. If this field is present, then it means Client wants to get information only for specified transaction.
direction	No	String	If this field is present and contains one of the allowed values, then it means Client wants to get only transactions related to specified operation type. Allowed values are: "deposit", "withdraw". If this field is missing or if this field is present but contains an empty string (""), then it means Client wants to get all deposits and withdrawals.
currency	No	String	If this field is present, then it means Client wants to get only transactions in the specified currency. If this field is missing, then it means Client wants to get deposits/withdrawals in all currencies.
dateFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest moment in time when transactions were created. In the result set transactions’ timestamp field value should be greater than or equal to (>=) dateFrom. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateFrom should be less than the value in the field dateTo.
dateTo	No	Number	UTC timestamp in milliseconds. Represents the latest moment in time when transactions were created. In the result set transactions’ timestamp field value should be less than (<) dateTo. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateTo should be greater than the value in the field dateFrom.
pageSize	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of transactions in the result for this request and cannot be greater than 100. If this field is missing, then the default value of 100 is used. If this field contains one of the allowed values and, simultaneously, the pageNumber field is missing, then the default pageNumber value is applied. Specifying the value in the field pageSize is mandatory if the value in the field pageNumber is also sent in the Client's request.
pageNumber	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize transactions per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 1. If this field is missing, then the default value of 1 is used. This value cannot be lower than 1. If any valid value is specified in this field, then it is mandatory to also send the value in the field pageSize in the Client’s request.
Funding History Response Parameters
Field Name	Mandatory	Format	Description
data	Yes	Array or Object	This object contains list of transactions, which satisfies request criteria. It might be empty array ([]). If this array is empty, then it means there are no transactions, which satisfy Client’s request criteria. In case of error, the value of this field should be not Array, but Object.
txId	Yes	Number	Unique ID of the transaction.
clientId	Yes	String	Represents the Client’s name.
accountId	Yes	String	Represents the Account ID.
currency	Yes	String	Represents the currency of the transaction.
direction	Yes	String	Represents the type of this operation. Allowed values - "deposit", "withdraw".
amount	Yes	String (which can be parsed as Float)	Represents amount of the transaction.
commissionAmount	Yes	String (which can be parsed as Float)	Represents commission amount of the transaction.
status	Yes	String	Represents the status of the transaction.
updatedAt	Yes	Datetime	Represents server timestamp when this transaction happened. Format: YYYY-MM-DDTHH:MM:SS.sssZ .
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Internal Transfer
This method works only with CEX.IO Spot Trading sub-accounts.
Client can request to transfer funds between his sub-accounts. CEX.IO Spot Trading does not charge Client any commission for transferring funds between his accounts. Along with a response to this request, CEX.IO Spot Trading sends Account Event messages to Client if this request is successful.

HTTP REQUEST

POST /do_my_internal_transfer

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Internal” permission set for API Key.

Internal Transfer Request Parameters
Do My Internal Transfer - Transfer Between Sub-accounts

Request (Client requests to transfer 2 USD from sub-account "superhat" to sub-account "hallo". Note that "amount" field is String in this request and is allowed as well Float)

{
  "fromAccountId": "superhat",
  "toAccountId": "hallo",
  "amount": "2",
  "currency": "USD",
  "clientTxId": "123"
}
Response (CEX.IO Spot Trading responds to Client that internal transfer operation was successful and shows transactionId of this transfer)

{
  "ok": "ok",
  "data": {
    "transactionId": 777
  }
}
Do My Internal Transfer - Duplicate clientTxId

Request (Client requests to transfer 4 USD from sub-account "superhat" to sub-account "hallo" with clientTxId = "123" which was already used in the previous example to transfer 2 USD)

{
  "fromAccountId": "superhat",
  "toAccountId": "hallo",
  "amount": "4",
  "currency": "USD",
  "clientTxId": "123"
}
Response (CEX.IO Spot Trading detects duplicate and funds are not transferred between accounts. CEX.IO Spot Trading responds to Client with transactionId of the successful transfer (first transfer with clientTxId = "123"))

{
  "ok": "ok",
  "data": {
    "transactionId": 777
  }
}
Do My Internal Transfer - Insufficient Funds

Request (Client requests to transfer 180 USD from sub-account "superhat" to sub-account "hallo", but there are only 18 USD on "superhat" sub-account)

{
  "fromAccountId": "superhat",
  "toAccountId": "hallo",
  "amount": 180,
  "currency": "USD",
  "clientTxId": "12342134442"
}
Response (CEX.IO Spot Trading responds that Client has insufficient funds on his "superhat" sub-account. So, the internal transfer was rejected, balances did not change)

{
  "error": "Insufficient funds"
}
Do My Internal Transfer - Incorrect Amount

Request (Client requests to transfer -10 USD from sub-account "superhat" to sub-account "hallo", but amount is <0, which is not allowed)

{
  "fromAccountId": "superhat",
  "toAccountId": "hallo",
  "amount": "-10",
  "currency": "USD",
  "clientTxId": "12342134442"
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed and amount should be greater than zero)

{
  "error": "Amount should be greater than zero"
}
Do My Internal Transfer - Incorrect AccountId

Request (Client requests to transfer 10 USD to sub-account "hallo", but does not specify from which sub-account namely)

{
  "toAccountId": "hallo",
  "amount": 10,
  "currency": "USD",
  "clientTxId": "12342134442"
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed and mandatory parameter is missing)

{
  "error": "Mandatory parameter fromAccountId is missing"
}
Do My Internal Transfer - Same fromAccountId and toAccountId

Request (Client requests to transfer 10 USD from sub-account "superhat" to sub-account "superhat" (same account))

{
  "fromAccountId": "superhat",
  "toAccountId": "superhat",
  "amount": 10,
  "currency": "USD",
  "clientTxId": "12342134442"
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed and fromAccountId and toAccountId should be different)

{
  "error": "fromAccountId and toAccountId should be different"
}
Do My Internal Transfer - Invalid Currency

Request (Client requests to transfer 10 ABC from sub-account "superhat" to sub-account "testAccount1". However, ABC is not a valid currency)

{
  "fromAccountId": "superhat",
  "toAccountId": "testAccount1",
  "amount": 20,
  "currency": "ABC",
  "clientTxId": "12342134442"
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed because currency ABC is not supported)

{
  "error": "Unsupported currency ABC"
}
Field Name	Mandatory	Format	Description
clientTxId	No	String	Unique identifier of transfer specified by Client. If two (or more) transfers with the same clientTxId are received by the system - only first transfer will be processed, second and subsequent transfers will return transactionId of the first completed internal transfer for clientTxId.
fromAccountId	Yes	String	Account identifier of sub-account, from which Client wants to transfer funds. Empty string value ("") in this field is not allowed.
toAccountId	Yes	String	Account identifier of sub-account, to which Client wants to transfer funds. Empty string value ("") in this field is not allowed. Destination Account should be created by Client beforehand via Create Account method or Spot Trading Web Portal.
currency	Yes	String	Currency of internal transfer.
amount	Yes	Float (or String which can be parsed as Float)	Amount of the transaction. It should be greater than 0.
Internal Transfer Response Parameters
Field Name	Mandatory	Format	Description
transactionId	No	Number	Unique identifier of successful internal transfer transaction.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Processing Info
This request allows Client to receive detailed information about available options to make deposits from external wallets and withdrawals to external wallets as to each supported cryptocurrency, including cryptocurrency name and available blockchains for deposit\withdrawals. Also, as to each supported blockchain there are indicated type of cryptocurrency on indicated blockchain, current deposit\withdrawal availability, minimum amounts for deposits\withdrawals, external withdrawal fees.

Processing Information makes Client more flexible in choosing desired blockchain for receiving Deposit address and initiating external withdrawals via certain blockchain, so that Client uses more convenient way of transferring his crypto assets to or from CEX.IO Ecosystem.

Note that this method indicates minimum deposit\withdrawal limits and external withdrawal fees for external crypto transfers. Currently, deposits and withdrawals of funds between CEX.IO Wallet and CEX.IO Spot Trading account are free.
Currently, external withdrawals are not supported via CEX.IO Spot Trading API.
HTTP REQUEST

POST /get_processing_info

API Rate Limit Cost: 10

API Key Permission

This method requires “Read” permission set for API Key.

Processing Info Request Parameters
Get Processing Info Request for one specific cryptocurrency

Request (Client queries processing info for "BTC")

{
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds that only 'bitcoin' blockchain is supported for deposits\withdrawals of "BTC")

{
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    }
  }
}
Get Processing Info Request for several cryptocurrencies

Request (Client queries processing info for "BTC" and "USDC")

{
  "data": {
    "currencies": ["BTC","USDC"]
  }
}
Response (CEX.IO Spot Trading responds that for deposits\withdrawals 'bitcoin' blockchain is supported for "BTC" and "ethereum", "stellar" and "tron" blockchains are supported for "USDC")

{
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    },
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40",
          "depositConfirmations": 25
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 1
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 21
        }
      }
    }
  }
}
Get Processing Info - No available blockchains

Request (Client queries processing info for supported cryptocurrency "ZEC")

{
  "data": {
    "currencies": ["ZEC"]
  }
}
Response (CEX.IO Spot Trading responds that request was processed successfully but no blockchains are supported for "ZEC")

{
  "ok": "ok",
  "data": {}
}
Get Processing Info - Invalid and fiat cryptocurrency

Request (Client queries processing info for "BTC", "ETH", "XXX" and "USD")

{
  "data": {
    "currencies": ["BTC", "ETH", "XXX", "USD"]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currencies "XXX" and "USD" are indicated in the request)

{
  "ok": "ok",
  "data": {
    "error": "Request contains unsupported currencies: XXX, USD."
  }
}
Get Processing Info - Invalid value type in "currencies" array

Request (Client queries processing info with invalid values type in "currencies" field)

{
  "data": {
    "currencies": [1,2,3]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because wrong type of value was indicated in "currencies" array and only string values are allowed)

{
  "ok": "ok",
  "data": {
    "error": "Currencies array should consist of string type values."
  }
}
Get Processing Info - Not an array indicated in "currencies" field

Request (Client queries processing info with indicating empty object ({}) in "currencies" field)

{
  "data": {
    "currencies": {}
  }
}
Response (CEX.IO Spot Trading responds that error occurred because only array is allowed in "currencies" field)

{
  "ok": "ok",
  "data": {
    "error": "Currencies should be array."
  }
}
Field Name	Mandatory	Format	Description
currencies	No	Array	List of cryptocurrencies for which Client wants to get information about supported blockchains for deposit\withdraw, limits and commissions. Cryptocurrencies should be in upper case and of string type. The list should contain only valid cryptocurrency symbols. If this field is missing or contains an empty array ([]), then it means Client wants to get processing info for all available cryptocurrencies.
Processing Info Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data.YYY	Yes	String	Cryptocurrency symbol specified in Client's request.
data.YYY.name	Yes	String	Cryptocurrency name.
data.YYY.blockchains	Yes	Object	This object contains info about all supported blockchains to deposit\withdraw cryptocurrency YYY.
data.YYY.blockchains.X	Yes	Object	This object contains details and limitations for deposit\withdrawal of cryptocurrency YYY via blockchain X, including data about blockchain type, current availability to deposit\withdraw, minimum deposit\withdrawal limit and external withdrawal fees.
data.YYY.blockchains.X. type	Yes	String	Type of cryptocurrency YYY on blockchain X.
data.YYY.blockchains.X. deposit	Yes	String	Describes current availability to deposit cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minDeposit	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be deposited from external wallet via blockchain X.
data.YYY.blockchains.X. withdrawal	Yes	String	Describes current availability to withdraw cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minWithdrawal	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be withdrawn to external wallet via blockchain X.
data.YYY.blockchains.X. withdrawalFee	Yes	String (which can be parsed as Float)	Amount of withdrawal fee in cryptocurrency YYY, which which would be charged and subtracted from withdrawal amount if blockchain X is used for withdrawal.
data.YYY.blockchains.X. depositConfirmations	Yes	Number	Minimal confirmation number for transaction in the blockchain to be deposited to Client’s Spot Trading account.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	String	If this field is present, then request is not successful. Represents numeric code of occurred error.
Deposit Address
This method works only with CEX.IO Spot Trading sub-accounts.
This method can be used by Client for receiving a crypto address to deposit cryptocurrency to CEX.IO Spot Trading sub-accounts.

Blockchains for deposit
The list of available blockchains for generating deposit address can be received by Client via Processing Info request.
HTTP REQUEST

POST /get_deposit_address

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Deposit Address Request Parameters
Get Deposit Address Request for sub-account to deposit "BTC" cryptocurrency via 1 available blockchain

Client sends get_processing_info request for receiving all available blockchains to deposit BTC

{
  "currencies": ["BTC"]
}
Response (CEX.IO Spot Trading responds with processing info with only one available "bitcoin" blockchain for BTC)

{
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005"
        }
      }
    }
  }
}
Request (Client queries deposit address for BTC cryptocurrency on "bitcoin" blockchain)

{
  "accountId": "testAccount1", // sub-account ID
  "currency": "BTC", // currency "BTC"
  "blockchain": "bitcoin" // required blockchain
}
Response (CEX.IO Spot Trading responds with information about crypto address to deposit BTC via "bitcoin" blockchain)

{
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "currency": "BTC",
    "blockchain": "bitcoin"
  }
}
Get Deposit Address Request for sub-account to deposit "USDC" cryptocurrency via specific blockchain

Client sends get_processing_info request for receiving all available blockchains to deposit USDC

{
  "currencies": ["USDC"]
}
Response (CEX.IO Spot Trading responds that there are 3 available blockchains to deposit USDC, namely "ethereum", "stellar" and "tron")

{
  "ok": "ok",
  "data": {
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40"
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "20"
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1"
        }
      }
    }
  }
}
Request (Client queries deposit address for sub-account "superhat" for USDC cryptocurrency to further deposit it via "tron" blockchain as most profitable for Client)

{
  "accountId": "superhat",
  "currency": "USDC",
  "blockchain": "tron"
}
Response (CEX.IO Spot Trading responds with information about crypto address to deposit USDC via "tron" blockchain on "superhat" account)

{
  "ok": "ok",
  "data": {
    "accountId": "superhat",
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "currency": "USDC",
    "blockchain": "tron"
  }
}
Get Deposit Address Request for sub-account to deposit "XRP" cryptocurrency

Client sends get_processing_info request for receiving of all available blockchains to deposit XRP

{
  "currencies": ["XRP"]
}
Response (CEX.IO Spot Trading responds that there is only 1 available blockchain to deposit XRP, namely "ripple")

{
  "ok": "ok",
  "data": {
    "XRP": {
      "name": "Ripple",
      "blockchains": {
        "ripple": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0",
          "withdrawal": "enabled",
          "minWithdrawal": "0.3",
          "withdrawalFee": "0.25"
        }
      }
    }
  }
}
Request (Client queries deposit address for sub-account "superhat" for XRP cryptocurrency to further deposit it via "ripple" blockchain)

{
  "accountId": "superhat",
  "currency": "XRP",
  "blockchain": "ripple"
}
Response (CEX.IO Spot Trading responds with destination and memo to deposit XRP via "ripple" blockchain)

{
  "ok": "ok",
  "data": {
    "accountId": "superhat",
    "destination": "rE1sdh25BJQ3qFwngiTBwaq3zPGGYcrjp1",
    "memo": "65629",
    "currency": "XRP",
    "blockchain": "ripple"
  }
}
Get Deposit Address - Unsupported currency

Request (Client queries deposit address)

{
  "accountId": "testAccount1",
  "currency": "XXX",
  "blockchain": "ethereum"
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currency is specified in the request)

{
  "error": "Unsupported currency XXX",
  "statusCode": 422
}
Get Deposit Address - Unsupported blockchain

Request (Client queries deposit address)

{
  "accountId": "testAccount1",
  "currency": "ETC",
  "blockchain": "tezos"
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currency is specified in the request)

{
  "error": "Blockchain is not supported.",
  "statusCode": 500
}
Field Name	Mandatory	Format	Description
accountId	Yes	String	Sub-account identifier, to which Client wants to make a deposit. Empty string value ("") in this field is not allowed.
currencies	Yes	String	Cryptocurrency name, for which Client wants to get a deposit address.
blockchain	Yes	String	Blockchain name, via which Client wants to make a deposit of requested currency. Available blockchains can be received via Processing Info request.
Deposit Address Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	Sub-account identifier, to which Client wants to make a deposit.
address	No	String	Crypto address for deposit. Please be informed that destination and memo fields are used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
destination	No	String	Destination address for deposit used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
memo	No	String	A special identifier used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
currency	Yes	String	Cryptocurrency name, for which deposit address is generated.
blockchain	Yes	String	Blockchain name, via which requested cryptocurrency can be deposited via generated address.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Funds Deposit from Wallet
This method works only with CEX.IO Spot Trading sub-accounts.
Client can deposit funds from CEX.IO Wallet to Spot Trading sub-account.

The system avoids processing of multiple deposit requests with the same clientTxId. If multiple deposit requests with identical clientTxId are received - the system processes only the first deposit request and rejects the second and subsequent deposit requests with the same clientTxId.

HTTP REQUEST

POST /do_deposit_funds_from_wallet

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Wallet” permission set for API Key.

Funds Deposit from Wallet Request Parameters
Funds Deposit Request from CEX.IO Wallet to Spot Trading sub-account

Request (Client queries deposit of BTC to sub-account "testAccount1")

{
  "amount": 0.001,
  "currency": "BTC",
  "accountId": "testAccount1",
  "clientTxId": "tx-depositFromWallet-test-1684398846720_1"
}
Response (CEX.IO Spot Trading responds with information that transaction was approved)

{
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684398846720_1",
    "currency": "BTC",
    "status": "approved"
  }
}
Funds Deposit Request from CEX.IO Wallet to Spot Trading sub-account

Request (Client queries deposit of BTC to sub-account "testAccount1")

{
  "amount": 0.001,
  "currency": "BTC",
  "accountId": "testAccount1",
  "clientTxId": "tx-depositFromWallet-test-1684399110416_1"
}
Response (CEX.IO Spot Trading responds with information that transaction is pending)

{
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684399110416_1",
    "currency": "BTC",
    "status": "pending"
  }
}
Invalid Deposit Request (too low amount)

Request (Client queries deposit of invalid amount)

{
  "amount": 0.00000002,
  "currency": "BTC",
  "accountId": "testAccount1",
  "clientTxId": "tx-depositFromWallet-test-1631101114709"
}
Response (CEX.IO Spot Trading responds that deposit was rejected due to low amount)

{
  "error": "Too low amount to deposit 0.00000002 BTC. Minimum amount 0.00100000 BTC",
  "statusCode": 500
}
Invalid Deposit Request (unsupported currency)

Request (Client queries deposit of unsupported currency)

{
  "amount": 25,
  "currency": "XXX",
  "accountId": "testAccount1",
  "clientTxId": "tx-depositFromWallet-test-1631103998454"
}
Response (CEX.IO Spot Trading responds that deposit was rejected because currency is not supported)

{
  "error": "Unsupported currency XXX",
  "statusCode": 422
}
Field Name	Mandatory	Format	Description
clientTxId	Yes	String	Transaction identifier assigned by Client.
accountId	Yes	String	Sub-account identifier, to which Client wants to deposit funds. Empty string value (“”) in this field is not allowed.
currency	Yes	String	Crypto or fiat currency symbol for deposit.
amount	Yes	Float (or String which can be parsed as Float)	Amount for deposit.
Funds Deposit from Wallet Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	Sub-account identifier, to which Client initiated deposit funds.
clientTxId	Yes	String	Transaction identifier assigned by Client.
currency	Yes	String	Crypto or fiat currency symbol for deposit.
status	Yes	String	Deposit transaction status. Allowed values - "rejected", "pending", "approved".
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
Funds Withdrawal to Wallet
This method works only with CEX.IO Spot Trading sub-accounts.
Client can withdraw funds from Spot Trading sub-account to CEX.IO Wallet.

The system avoids multiple withdrawal requests with the same clientTxId. If multiple withdrawal requests with identical clientTxId are received - the system processes only the first withdrawal request and rejects the second and subsequent withdrawal requests with the same clientTxId.

HTTP REQUEST

POST /do_withdrawal_funds_to_wallet

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Wallet” permission set for API Key.

Funds Withdrawal to Wallet Request Parameters
Funds Withdrawal Request from Spot Trading sub-account to CEX.IO Wallet

Request (Client queries withdrawal of BTC from sub-account "testAccount1")

{
  "amount": 0.001,
  "currency": "BTC",
  "accountId": "testAccount1",
  "clientTxId": "tx-withdrawToWallet-test-1684399231967_1"
}
Response (CEX.IO Spot Trading responds with information that transaction was approved)

{
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399231967_1",
    "currency": "BTC",
    "status": "approved"
  }
}
Funds Withdrawal Request from Spot Trading sub-account to CEX.IO Wallet

Request (Client queries withdrawal of XRP from sub-account "testAccount1")

{
  "amount": 200,
  "currency": "XRP",
  "accountId": "testAccount1",
  "clientTxId": "tx-withdrawToWallet-test-1684399377964_1"
}
Response (CEX.IO Spot Trading responds with information that transaction is pending)

{
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399377964_1",
    "currency": "XRP",
    "status": "pending"
  }
}
Invalid Withdrawal Request (too low amount)

Request (Client queries withdrawal of invalid amount)

{
  "amount": 0.00000002,
  "currency": "BTC",
  "clientTxId": "tx-withdrawToWallet-test-1630598297863",
  "accountId": "testAccount1"
}
Response (CEX.IO Spot Trading responds that withdrawal was rejected due to low amount)

{
  "error": "Too low amount to withdraw 0.00000002 BTC. Minimum amount 0.00100000 BTC",
  "statusCode": 500
}
Invalid Withdrawal Request (unsupported currency)

Request (Client queries withdrawal of unsupported currency)

{
  "amount": "10",
  "currency": "XXX",
  "clientTxId": "tx-withdrawToWallet-test-1630598290954",
  "accountId": "testAccount1"
}
Response (CEX.IO Spot Trading responds that withdrawal was rejected because currency is not supported)

{
  "error": "Unsupported currency XXX",
  "statusCode": 422
}
Field Name	Mandatory	Format	Description
clientTxId	Yes	String	Transaction identifier assigned by Client.
accountId	Yes	String	Sub-account identifier, from which Client wants to withdraw funds. Empty string value (“”) in this field is not allowed.
currency	Yes	String	Crypto or fiat currency symbol for withdrawal.
amount	Yes	Float (or String which can be parsed as Float)	Amount for withdrawal.
Funds Withdrawal to Wallet Response Parameters
Field Name	Mandatory	Format	Description
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	Sub-account identifier, from which Client initiated funds withdrawal.
clientTxId	Yes	String	Transaction identifier assigned by Client.
currency	Yes	String	Crypto or fiat currency symbol for withdrawal.
status	Yes	String	Withdrawal transaction status. Allowed values - “rejected”, “pending”, “approved”.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
statusCode	No	Number	If this field is present, then request is not successful. Represents numeric code of occurred error.
WebSocket
WebSocket is a TCP-based full-duplex communication protocol. Full-duplex means that both parties can send each other messages asynchronously using the same communication channel. This section describes which messages should CEX.IO Spot Trading and Client send each other. All messages should be valid JSON objects.

WebSocket API is mostly used to obtain information or do actions which are not available or not easy to do using REST API. However, some requests or actions are possible to do in both REST API and WebSocket API. CEX.IO Spot Trading sends messages to Client as a response to request previously sent by Client, or as a notification about some event (without prior Client’s request).

Request should contain request identifier “e”. If it starts with “get”, then such request is used to obtain some information. If it starts with “do”, then such request is used to trigger some action in CEX.IO Spot Trading.

Keep in mind that WebSocket API does not support message resending functionality, and WebSocket connection might be terminated at any time by any party. Connection might be terminated right after the “do” request, so there is a relatively small chance that Client can miss the response for this action. So, in such case Client does not know if this action was successful or not, and there is no guarantee that Client can get this response even if he reconnects in a moment right after disconnection. If such situation happens, then Client should take necessary actions to find out the result of such actions (for example, Client should request account status or request transactions history).

In most requests, messages from Client should include the field “oid”. It should contain a string, an identifier of the request. This identifier is included in Spot Trading's responses, so it is possible for Client to link each response with his correspondent request. Client can use current timestamp in milliseconds, or a random number, or any other identifier he likes as “oid” value. It should not be unique, however it is better to use unique identifier for “oid”.

Calling incorrect or unsupported methods
If Client calls WebSocket API method that is incorrect/unsupported, CEX.IO Spot Trading responds with error, sends disconnected event and closes WebSocket connection afterwards.
Public API Calls
Connection
Connection should be established using SSL.

WebSocket API Public Endpoint URL

wss://trade.cex.io/api/spot/ws-public

Either Client or CEX.IO Spot Trading can terminate WebSocket connection at any time.

Once connected, CEX.IO Spot Trading sends “connected” message to Client.

Query Parameters
From	To	Message	Description
CEX.IO Spot Trading	Client	{"e":"connected"}	By successful connection, CEX.IO Spot Trading notifies Client about it by sending him a message.
Keep Connection Alive
To keep connection alive, Client should periodically send any valid message to CEX.IO Spot Trading. Maximum allowed period between two closest Client’s messages is 10 seconds (however, this parameter might be changed by CEX.IO Spot Trading in future). If Client exceeds this limit (meaning, Client sends less than 1 message per 10 seconds), then CEX.IO Spot Trading can terminate the connection.

If Client has no messages to send, then he should send “ping” message to keep the connection alive. Client can send ping messages any time he wishes, even if he has enough other messages to send. Once Client sends a “ping” message, CEX.IO Spot Trading responds with a “pong” message.

Keeping Connection Alive Example
Sequence id	From	To	Message	Description
1	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends “ping”.
2	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
3	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 5 seconds.
4	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
5	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 8 seconds.
6	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
7				CEX.IO Spot Trading keeps connection open if Client sends any valid message at least once per 10 seconds.
Example of Keeping Connection Alive with Idle Client
Sequence id	From	To	Message	Description
1	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends “ping”.
2	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
3	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 5 seconds.
4	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
5				Client does not send any messages for more than 10 seconds.
6	CEX.IO Spot Trading	Client	{"e":"disconnected"}	CEX.IO Spot Trading notifies Client that he is about to Close the connection in a moment because the Client is idle. This message, however, is optional.
7				CEX.IO Spot Trading terminates the connection.
Unsupported method call
Unsupported method call example

Response (by successful connection, CEX.IO Spot Trading notifies Client about it by sending him a message)

{
  "e": "connected"
}
Request (Client calls some_unsupported_method WebSocket API method that does not exist)

{
  "e": "some_unsupported_method",
  "oid": "1523433664816_1_some_unsupported_method",
  "data": {
    "foobar": 1
  }
}
Response (CEX.IO Spot Trading responds with error)

{
  "e": "some_unsupported_method",
  "oid": "1523439125503_1_some_unsupported_method",
  "data": {
    "error": "Unsupported message type some_unsupported_method"
  }
}
Response (CEX.IO Spot Trading sends disconnected event and closes WebSocket connection afterwards)

{
  "e": "disconnected"
}
Client sends JSON messages to CEX.IO Spot Trading using WebSocket. Each message should contain e field, which defines the message type. Client should use message types which are described in documentation. Once Client sends message type which is not described in documentation, then CEX.IO Spot Trading replies with error, sends disconnected event to Client and closes WebSocket connection.

API Rate limit
Public API rate limit is implied in order to protect the system from DDoS attacks and ensuring all Clients can have same level of stable access to CEX.IO Spot Trading API endpoints. Public requests are limited by IP address from which public API requests are made. Request limits are determined from cost associated with each public API call. By default, each public request has a cost of 1 point, but for some specific requests this cost can be higher. See up-to-date request rate limit cost information in specification of each method.

Client request limitations
CEX.IO Spot Trading limits Public API calls to maximum of 100 points per minute, considering that each Public API call has its' cost (see below). If request rate limit is reached then CEX.IO Spot Trading replies with error, sends disconnected event to Client and closes WS connection afterwards. CEX.IO Spot Trading will continue to serve Client starting from the next calendar minute. In the following example, request counter will be reset at 11:02:00.000.
Rate limit exceeded example
Seq id	Time	Type	Message	Comment
1.1	11:01:05.853	Request	{"e":"get_order_book", "data": [], "oid": "1523433_1_get_order_book"}	Client sends request to get order book.
1.2	11:01:05.856	Response	{"e":"get_order_book", "oid": "1523433_1_get_order_book", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with order book.
2.1	11:01:06.001	Request	{"e":"get_order_book", "data": [], "oid": "1523433_2_get_order_book"}	Client sends request to get order book.
2.2	11:01:06.104	Response	{"e":"get_order_book", "oid": "1523433_2_get_order_book", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with order book
...	...	...	...	...
100.1	11:01:20.213	Request	{"e":"get_order_book", "data": [], "oid": "1523433_100_get_order_book"}	Client sends request to get order book.
100.2	11:01:20.345	Response	{"e":"get_order_book", "oid": "1523433_100_get_order_book", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with order book.
101.1	11:01:20.390	Request	{"e":"get_order_book", "data": [], "oid": "1523433_101_get_order_book"}	Client sends request to get order book.
101.2	11:01:20.400	Response	{"e":"get_order_book", "oid": "1523433_101_get_order_book", "data": {"error": "API rate limit reached"}}	CEX.IO Spot Trading responds with error: API rate limit reached.
102.1	11:01:20.403	Response	{"e”:”disconnected”}	CEX.IO Spot Trading notifies Client before disconnecting WS by sending him a disconnected event.
Order Book
This method allows Client to receive current order book snapshot for specific trading pair.

REQUEST

get_order_book

API Rate Limit Cost: 1

Order Book Request Parameters
Get Order Book request for one trading pair.

Request (Client sends request to receive order book snapshot for BTC-USD trading pair)

{
  "e": "get_order_book",
  "oid": "152171113_get_order_book",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request with current order book snapshot for BTC-USD trading pair)

{
  "e": "get_order_book",
  "oid": "152171113_get_order_book",
  "ok": "ok",
  "data": {
    "timestamp": 1676037221433,
    "currency1": "BTC",
    "currency2": "USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_order_book" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to request an Order Book snapshot. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_order_book" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
timestamp	Yes	Number	Current client time - UTC timestamp in milliseconds.
currency1	Yes	String	The first currency in the requested trading pair.
currency2	Yes	String	The second currency in the requested trading pair.
bids	Yes	Array	This array contains a list of bids of the order book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book.
asks	Yes	Array	This array contains a list of asks of the Order Book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Order Book Subscribe
Client by subscribing via WebSocket can subscribe to order book feed upon requested trading pair.

In response to Order Book Subscribe request Client will receive current (initial) order book snapshot for requested pair with indicated seqId number.

To track following updates to Order Book Client needs to subscribe via WebSocket to “order_book_increment“ messages, which would contain trading pair name, seqId number, Bids and Asks price levels deltas.

REQUEST

order_book_subscribe

API Rate Limit Cost: 1

Order Book Subscribe Request Parameters
Order Book Subscribe request

Request (Client sends BTC-USD order book subscription request)

{
  "e": "order_book_subscribe",
  "oid": "16147857398591_order_book_subscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "order_book_subscribe",
  "oid": "16147857398591_order_book_subscribe",
  "ok": "ok",
  "data": {
    "seqId": 1680908,
    "pair": "BTC-USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}
Order Book Increment (CEX.IO Spot Trading sends BTC-USD order book increment)

{ 
  "e": "order_book_increment",
  "ok": "ok",
  "data": { 
    "seqId": 1680909,
    "pair": "BTC-USD",
    "bids": [ 
      [
        "21770.5",
        "0.00000000"
      ],
      [
        "21755.9",
        "0.00000272"
      ],
      [
        "21753.4",
        "1.12345678"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "2.89000000"
      ],
      [
        "21841.0",
        "0.00000000"
      ],
      [
        "21842.0",
        "7.54419136"
      ],
      [
        "21841.4",
        "0.01000000"
      ],
      [
        "21839.5",
        "0.55000000"
      ]
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_subscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to subscribe for receiving Order Book snapshot and updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Subscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_subscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
seqId	Yes	Number	Unique ID of the Order Book snapshot message. The value returned in this field is an initial seqId for order book feed. Further Order Book Increment seqId value should be incremented from value returned in this field.
pair	Yes	String	Trading pair, for which Order Book snapshot is returned.
bids	Yes	Array	This array contains a list of bids of the order book snapshot. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book snapshot.
asks	Yes	Array	This array contains a list of asks of the order book snapshot. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book snapshot.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Order Book Increment Messages
In case of successful subscription server will send order_book_subscribe response, which contains full order book at that moment.

Following messages are “order_book_increment“ messages, which should be applied to the initial Order Book snapshot incrementally on the Client’s side to keep Order Book snapshot up to date. Each Order Book Increment item should be applied to existing snapshot at specific price level.

All Order Book messages have parameter seqId. Received snapshot of trading pair order book contains seqId number which should be considered by Client as initial seqId number for order book feed. SeqId increments on each further order_book_increment message.

If a Client subscribes to multiple order books for different trade pairs, Client should track the pair name and seqId number in each new Order Book Increment message received in order to correctly add increments to the corresponding Order Book Snapshot for that trade pair.

If one or a few Order Book update messages were not received by the Client, it is required to re-subscribe to Order Book for receiving a new actual snapshot in order to keep Order book up to date.

If Client receives message with seqId number which is lower than previous seqIds received in the subscribed feed - Client is required to re-subscribe to Order Book for receiving a new actual snapshot in order to keep Order book up to date. Such situation happens when CEX.IO Spot Trading’s internal system is restarted and Order Book subscription is automatically re-subscribed for the Client.

Order Book Increment Message Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_increment" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
seqId	Yes	Number	Unique ID of the Order Book update message. First Order Book increment should contain the value in this field equal to Order Book snapshot seqId incremented by 1. The value of this field in further Order Book increment messages should equal to previous Order Book increment seqId incremented by 1.
pair	Yes	String	Trading pair, for which Order Book update is returned.
bids	Yes	Array	This array contains a list of bids deltas - price levels of the Order Book entries. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates updated amount of the Order Book entry. The value in this field can be an empty array in case Order Book bids were not changed since previous Order Book update message.
asks	Yes	Array	This array contains a list of asks deltas - price levels of the Order Book entries. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates updated amount of the Order Book entry. The value in this field can be an empty array in case Order Book asks were not changed since previous Order Book update message.
Order Book Unsubscribe
It's highly recommended to unsubscribe from order book when it is no longer needed.

REQUEST

order_book_unsubscribe

API Rate Limit Cost: 1

Order Book Unsubscribe Request Parameters
Order Book Unsubscribe request

Request (Client sends BTC-USD order book unsubscribe request)

{
  "e": "order_book_unsubscribe",
  "oid": "16147857488591_order_book_unsubscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "order_book_unsubscribe",
  "oid": "16147857488591_order_book_unsubscribe",
  "ok": "ok",
  "data": {
    "pair": "BTC-USD"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to unsubscribe from receiving Order Book updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Unsubscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
pair	Yes	String	Indicates trading pair, for which Client would be unsubscribed from receiving further Order Book updates.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Candles
By using Candles method Client can receive historical OHLCV candles of different resolutions and data types.

Client can indicate additional timeframe and limit filters to make response more precise to Client’s requirements.

REQUEST

get_candles

API Rate Limit Cost: 1

Candles Request Parameters
Get Candles request

Request (Client sends request to receive 1 bestAsk open candles for BTC-USD trading pair as of current time)

{
  "e": "get_candles",
  "oid": "16760394893891_get_candles",
  "ok": "ok",
  "data": {
    "pair": "BTC-USD",
    "fromISO": 1675953089378,
    "limit": 1,
    "dataType": "bestAsk",
    "resolution": "1h"
  }
} 
Response (CEX.IO Spot Trading successfully responds to the request, 1 closed 1h candle)

{
  "e": "get_candles",
  "oid": "16760394893891_get_candles",
  "ok": "ok",
  "data":[
    {
      "timestamp": 1675951200000,
      "open": 22945.3,
      "high": 23163.4,
      "low": 22913,
      "close": 22920.1,
      "volume": 779.00675644,
      "resolution": "1h",
      "isClosed": true,
      "timestampISO": "2023-02-09T14:00:00.000Z"
    }
  ]
}
Request (Client sends request to receive 1 bestBid open candles for 3 pairs as of current time)

{
  "e": "get_candles",
  "oid": "1676041279412_get_candles",
  "data": {
    "pairsList": ["BTC-USD","ETH-USD","XXX-YYY"],
    "toISO": 1676041279412,
    "limit": 1,
    "dataType": "bestBid",
    "resolution": "1h"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request, pairs with 1 open candle for each + unsupported pair message)

{ 
  "e": "get_candles",
  "oid": "1676041279412_get_candles",
  "ok": "ok",
  "data": {
    "BTC-USD": [ 
      { 
        "timestamp": 1676041200000,
        "high": 21791.3,
        "low": 21772.4,
        "close": 21782.6,
        "open": 21791.3,
        "volume": 36.87654321,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "ETH-USD": [ 
      {
        "timestamp": 1676041200000,
        "high": 1545.21,
        "low": 1543.65,
        "close": 1544.95,
        "open": 1545.21,
        "volume": 34.12345678,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z" 
      } 
    ],
    "XXX-YYY": {
      "error": { 
        "code": 400, 
        "reason": "Unsupported pair XXX-YYY" 
      }
    }
  }
}
Request (Client sends request to receive last 1 hour bestAsk candle for LUNC-BUSD pair)

{
  "e": "get_candles",
  "oid": "16760424783851_get_candles",
  "data": {
    "pair":"LUNC-BUSD",
    "toISO":1676042478383,
    "limit":1,
    "dataType":"bestAsk",
    "resolution":"1h"
  }
}
Response (CEX.IO Spot Trading responds with empty candle, which means no candle is available upon requested parameters)

{
  "e": "get_candles",
  "oid": "16760424783851_get_candles",
  "ok": "ok",
  "data": {
    "timestamp": 1676041200000,
    "resolution": "1h",
    "timestampISO": "2023-02-10T15:00:00.000Z"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_candles" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	No	String	Trading pair, for which Client wants to receive historical OHLCV candles. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles for one specific trading pair. If "pair" field is present, then "pairsList" field should be absent. Either "pair" or "pairsList" should be indicated in the request anyway.
pairsList	No	Array or String	Array with trading pairs, for which Client wants to receive last historical OHLCV candles. At least 1 trading pair should be indicated in this field. If this field is present and contains valid values, then it means Client wants to receive last OHLCV candle for each indicated trading pair in the list. If "pairsList" field is present, then "pair" field should be absent. Either "pairsList" or "pair" should be indicated in the request anyway.
fromISO	No	Number (UTC timestamp)	The starting moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the first one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
toISO	No	Number (UTC timestamp)	The last moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the last one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
limit	No	Number (Integer)	Maximum number of OHLCV candles to be returned in response. Indicated number should be greater than zero. This field is mandatory if at least one of “fromISO” or “toISO” fields is specified in request. This field should be absent if both “fromISO” and “toISO” are specified in request. If “pairsList” field is specified in the request, then the value of this field should equal 1 (only last candle for each requested trading pair will be returned in response).
dataType	Yes	String	The type of data, on the basis of which returned OHLC prices in candles should be calculated. Allowed values: “bestAsk”, “bestBid”.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
Candles Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_candles" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
timestamp	Yes	Number	OHLCV candle timestamp - UTC timestamp in milliseconds.
open	No	Number (Float)	Opening price of OHLCV candle in quote currency.
high	No	Number (Float)	Highest price of OHLCV candle in quote currency, which was reached during candle timeframe.
low	No	Number (Float)	Lowest price of OHLCV candle in quote currency, which was reached during candle timeframe.
close	No	Number (Float)	Closing price of OHLCV candle in quote currency.
volume	No	Number (Float)	Total base currency amount traded during a specific candle timeframe period.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
isClosed	No	Boolean (true)	Indicates whether the specific candle is currently closed. If the value of this field is true, then it means this candle has been already closed. If this field is absent, then it means this candle is still open.
timestampISO	Yes	String	OHLCV candle date & time in ISO format (“YYYY-MM-DDTHH:mm:ss.SSSZ").
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade History
This method allows Client to obtain historical data as to occurred trades upon requested trading pair.

Client can supplement Trade History request with additional filter parameters, such as timeframe period, tradeIds range, side etc. to receive trades which match request parameters.

REQUEST

get_trade_history

API Rate Limit Cost: 1

Trade History Request Parameters
Get Trade History Request

Request (Client sends request to receive trade history for BTC-USD trading pair)

{
  "e": "get_trade_history",
  "oid": "16760424783866_get_trade_history",
  "data": {
   "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "get_trade_history",
  "oid": "16760424783866_get_trade_history",
  "ok": "ok",
  "data": {
    "pageSize": 1000,
    "trades": [
      {
        "tradeId": "1675399566795-0",
        "dateISO": "2023-02-03T04:46:06.795Z",
        "side": "SELL",
        "price": "21149.2",
        "amount": "10.00000000"
      },
      {
        "tradeId": "1675401193999-0",
        "dateISO": "2023-02-03T05:13:13.999Z",
        "side": "BUY",
        "price": "25896.0",
        "amount": "0.00000001"
      },
      {
        "tradeId": "1675401207800-0",
        "dateISO": "2023-02-03T05:13:27.800Z",
        "side": "SELL",
        "price": "21146.0",
        "amount": "0.00000001"
      }
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_trade_history" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to receive trades history. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
side	No	String	Side of requested trades. If this field is present, it should contain only one of allowed values: “BUY” or “SELL”. If this field is not indicated in the request, then response would contain trades for "BUY" and "SELL" sides.
fromDateISO	No	String	The starting moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If “fromDateISO” and “pageSize” parameters are not specified in request, then by default last 1000 trades will be returned in response. If this field is present, then “fromTradeId” and “toTradeId” fields should not be indicated in the request.
toDateISO	No	String	The last moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If this field is present, then “fromDateISO” should also be present, “fromTradeId” and “toTradeId” fields should be absent.
fromTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, starting from which subsequent trades should be returned in response. If this field is present, then “fromDateISO” and “toDateISO” fields should not be indicated in the request.
toTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, which should be the last trade returned in response. If this field is present, then “fromTradeId” should also be present, “fromDateISO” and “toDateISO” fields should not be indicated in the request.
pageSize	No	Number (Integer)	Maximum number of trades, which should be returned in response. If this field is present then the value should be more than zero and not more than 10000. If indicated value is more than 10000, the response will still contain only up to 10000 trades max. If this field is not specified in request, then by default 1000 trades would be returned in response.
Trade History Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_trade_history" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
pageSize	Yes	Number (Integer)	Maximum number of trades, which can be returned in response.
trades	Yes	Array	An array containing data as to each trade event which satisfies requested criteria. If request is successful, this field should be present in response. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted by “dateISO” value in ascending order (from older to newer, considering “fromDateISO” / “toDateISO” or “fromTradeId” / “toTradeId” if indicated in request). If a few trade events occurred at the same moment of time, then such trade events are sorted additionally bt “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	Represents an object which describes specific trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade Subscribe
By using the Trade Subscribe method Client can subscribe via WebSocket to live feed of trade events which occur on requested trading pair.

In response to Trade Subscribe request Client will receive a unique identifier of trade subscription which should further be used for unsubscription when trade subscription is no longer needed for Client.

Client should subscribe via WebSocket to “tradeHistorySnapshot” and “tradeUpdate” messages to receive initial and periodical Trade History snapshots, and live trade events for requested trading pair.

REQUEST

trade_subscribe

API Rate Limit Cost: 1

Trade Subscribe Request Parameters
Trade Subscribe request

Request (Client sends trade subscribe request)

{
  "e": "trade_subscribe",
  "oid": "72955210375_trade_subscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "trade_subscribe",
  "oid": "72955210375_trade_subscribe",
  "ok": "ok",
  "data": {
    "reqId":"1678176120060_1"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_subscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to subscribe for receiving trade event updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Trade Subscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_subscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
reqId	Yes	String	Identifier of WebSocket connection in which trade subscription feed is created.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade History Snapshot
Right after the User initiates a new Trade Subscription, they'll get a tradeHistorySnapshot containing last 200 trade events upon requested pair. Then, the server will start sending a stream (series) of tradeUpdate events.

However, tradeUpdate updates can be received before tradeHistorySnapshot. Additionally, some tradeUpdate messages received after tradeHistorySnapshot may partially repeat trades already received from the snapshot.

Also, TradeHistorySnapshot events in some cases can arrive during a session while regular tradeUpdate events are being received. To handle this case, the Client should store the tradeId of the last trade processed and ignore all trades with a tradeId that is equal to or less than the stored tradeId value, whether they come from a snapshot or update.

Trade History Snapshot message

{
  "e": "tradeHistorySnapshot",
  "ok": "ok",
  "data": { 
    "pair": "BTC-USD",
    "trades": [
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:22:25.734Z",
        "price": "22562.1",
        "amount": "0.00975172",
        "tradeId": "1678152145734-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:22:53.141Z",
        "price": "22566.6",
        "amount": "0.00975075",
        "tradeId": "1678152173141-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:23:10.109Z",
        "price": "22571.1",
        "amount": "0.00974977",
        "tradeId": "1678152190109-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:23:33.461Z",
        "price": "22586.3",
        "amount": "0.05557372",
        "tradeId": "1678152213461-0"
      }
    ]
  }
}
Trade History Snapshot Message Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "tradeHistorySnapshot" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
pair	Yes	String	Trading pair, for which trades history snapshot is returned in response.
trades	Yes	Array	An array containing data as to last 200 trade events which satisfies requested criteria. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted in ascending order. If a few trade events occurred at the same moment of time, then such trade events are sorted additionally bt “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	Represents an object which describes specific trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
Trade Update Message Parameters
Trade Update message

{
  "e": "tradeUpdate",
  "ok": "ok",
  "data": { 
    "pair": "BTC-USD",
    "side": "BUY",
    "dateISO": "2023-03-07T08:04:16.117Z",
    "price": "22615.3",
    "amount": "0.01000000",
    "tradeId": "1678176256117-0" 
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "tradeUpdate" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
pair	Yes	String	The trading pair on which the trade event occurred.
side	Yes	String	Side of trade event.
dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
price	Yes	String (parseable as float)	Trade execution price.
amount	Yes	String (parseable as float)	Amount of trade.
tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”, “1677696747988-2”, etc.).
Trade Unsubscribe
It's highly recommended to unsubscribe from existing trade subscription when it is no longer needed for Client.

REQUEST

trade_unsubscribe

API Rate Limit Cost: 1

Trade Unsubscribe Request Parameters
Request

{
  "e": "trade_unsubscribe",
  "oid": "16781762553800_trade_unsubscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "trade_unsubscribe",
  "oid": "16781762553800_trade_unsubscribe",
  "ok": "ok",
  "data": {
    "reqId":"1678176120060_1"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
data.pair	Yes	String	Trading pair, for which Client wants to unsubscribe from receiving trade event updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Trades Unsubscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
reqId	Yes	String	Identifier of WebSocket connection in which trade subscription feed is removed.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Ticker
This method is designed to obtain current information about Ticker, including data about current prices, 24h price & volume changes, last trade event etc. of certain assets.

REQUEST

get_ticker

API Rate Limit Cost: 1

Ticker Request Parameters
Get Ticker request

Request (Client sends request to receive ticker for one pair)

{
  "e": "get_ticker",
  "oid": "10181762572482_get_ticker",
  "data": {
    "pairs": ["BTC-USD"]
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "get_ticker",
  "oid": "10181762572482_get_ticker",
  "ok": "ok",
  "data": {
    "BTC-USD": {
      "bestBid": "23771.3",
      "bestAsk": "23895.2",
      "bestBidChange": "-398.5",
      "bestBidChangePercentage": "-1.64",
      "bestAskChange": "-362.4",
      "bestAskChangePercentage": "-1.49",
      "volume30d": "1311.83096457",
      "low": "22920.1",
      "high": "25379.4",
      "volume": "21.14500755",
      "quoteVolume": "509738.03240736",
      "lastTradeVolume": "0.00493647",
      "last": "23771.3",
      "lastTradePrice": "23895.2",
      "priceChange": "-481.7",
      "priceChangePercentage": "-1.98",
      "lastTradeDateISO": "2023-02-23T12:26:13.486Z",
      "volumeUSD": "286794.97"
    }
  }
}
Get Ticker request

Request (Client sends request to receive ticker for multiple pairs)

{
  "e": "get_ticker",
  "oid": "16781762556482_get_ticker",
  "data": {
    "pairs": ["ADA-USD", "BTC-USD", "ETH-USD", "SHIB-USD"]
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "get_ticker",
  "oid": "16781762556482_get_ticker",
  "ok": "ok",
  "data": {
    "ADA-USD": { 
      "bestBid": "0.387159",
      "bestAsk": "0.387938",
      "bestBidChange": "0.001354",
      "bestBidChangePercentage": "0.35",
      "bestAskChange": "-0.000370",
      "bestAskChangePercentage": "-0.09",
      "volume30d": "6530615.77263454",
      "low": "0.379304",
      "high": "0.395922",
      "volume": "33554.76625400",
      "quoteVolume": "12971.29778584",
      "lastTradeVolume": "30.53522000",
      "last": "0.388926",
      "lastTradePrice": "0.387938",
      "priceChange": "0.001489",
      "priceChangePercentage": "0.38",
      "lastTradeDateISO": "2023-02-23T12:23:40.391Z",
      "volumeUSD": "45000.43"
    },
    "BTC-USD": {
      "bestBid": "23771.3",
      "bestAsk": "23895.2",
      "bestBidChange": "-398.5",
      "bestBidChangePercentage": "-1.64",
      "bestAskChange": "-362.4",
      "bestAskChangePercentage": "-1.49",
      "volume30d": "1311.83096457",
      "low": "22920.1",
      "high": "25379.4",
      "volume": "21.14500755",
      "quoteVolume": "509738.03240736",
      "lastTradeVolume": "0.00493647",
      "last": "23771.3",
      "lastTradePrice": "23895.2",
      "priceChange": "-481.7",
      "priceChangePercentage": "-1.98",
      "lastTradeDateISO": "2023-02-23T12:26:13.486Z",
      "volumeUSD": "286794.97"
    },
    "ETH-USD": {
      "bestBid": "1640.41",
      "bestAsk": "1648.25",
      "bestBidChange": "-6.58",
      "bestBidChangePercentage": "-0.39",
      "bestAskChange": "-5.41",
      "bestAskChangePercentage": "-0.32",
      "volume30d": "10500.56442743",
      "low": "1599.44",
      "high": "1680.62",
      "volume": "267.63458000",
      "quoteVolume": "439523.29960757",
      "lastTradeVolume": "0.17435800",
      "last": "1648.97",
      "lastTradePrice": "1648.25",
      "priceChange": "2.08",
      "priceChangePercentage": "0.12",
      "lastTradeDateISO": "2023-02-23T12:25:11.251Z",
      "volumeUSD": "148920.84"
    },
    "SHIB-USD": {
      "bestBid": "0.00001276",
      "bestAsk": "0.00001354",
      "bestBidChange": "0.00000045",
      "bestBidChangePercentage": "3.65",
      "bestAskChange": "0.00000032",
      "bestAskChangePercentage": "2.42",
      "volume30d": "34227200927",
      "low": "0.00001231",
      "high": "0.00001369",
      "volume": "331030734",
      "quoteVolume": "4371.24465887",
      "lastTradeVolume": "20245767",
      "last": "0.00001295",
      "lastTradePrice": "0.00001354",
      "priceChange": "-0.00000027",
      "priceChangePercentage": "-2.04",
      "lastTradeDateISO": "2023-02-23T12:05:47.380Z",
      "volumeUSD": "3782974.41"
    } 
  } 
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_ticker" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pairs	No	Array of Strings	List of supported trading pairs for which Client wants to receive ticker data. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present in the request, then at least 1 pair should be indicated in an array. If this field is absent, then it means Client requests ticker data for all supported pairs.
Ticker Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_ticker" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
XXX-YYY	No	Object	Represents an object which describes XXX-YYY trading pair ticker
XXX-YYY.bestBid	No	String (parseable as float)	Current highest buy order price (bestBid) in Order Book.
XXX-YYY.bestAsk	No	String (parseable as float)	Current lowest sell order price (bestAsk) in Order Book.
XXX-YYY.bestBidChange	No	String (parseable as float)	Last 24h bestBid price change in quote currency.
XXX-YYY.bestBidChangePercentage	No	String (parseable as float)	Last 24h bestBid price change in percentage.
XXX-YYY.bestAskChange	No	String (parseable as float)	Last 24h bestAsk price change in quote currency.
XXX-YYY.bestAskChangePercentage	No	String (parseable as float)	Last 24h bestAsk price change in percentage.
XXX-YYY.volume30d	Yes	String (parseable as float)	Last 30d trading volume in base currency.
XXX-YYY.low	No	String (parseable as float)	Last 24h lowest trade price.
XXX-YYY.high	No	String (parseable as float)	Last 24h highest trade price.
XXX-YYY.volume	Yes	String (parseable as float)	Last 24h volume in base currency.
XXX-YYY.quoteVolume	Yes	String (parseable as float)	Last 24h volume in quote currency.
XXX-YYY.lastTradeVolume	No	String (which can be parsed as Float)	Last trade volume in base currency.
XXX-YYY.last	No	String (which can be parsed as Float)	Last indicative price.
XXX-YYY.lastTradePrice	No	String (parseable as float)	Last trade price in CEX.IO Ecosystem.
XXX-YYY.priceChange	No	String (which can be parsed as Float)	Last 24h price change in quote currency.
XXX-YYY.priceChangePercentage	No	String (which can be parsed as Float)	Last 24h price change in percentage.
XXX-YYY.lastTradeDateISO	No	String	Date & Time of last trade in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
XXX-YYY.volumeUSD	Yes	String (parseable as float)	Last 24h volume equivalent in USD currency.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Server Time
This method is used to get the current time on CEX.IO Spot Trading server. It can be useful for applications that have to be synchronized with the server's time.

REQUEST

get_server_time

API Rate Limit Cost: 1

Server Time Request Parameters
Get Server Time request

Request (Client sends a request to get server time)

{
  "e": "get_server_time",
  "oid": "16760424783867_get_server_time",
  "data": {}
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "get_server_time",
  "oid": "16760424783867_get_server_time",
  "ok": "ok",
  "data": {
    "timestamp": 1231239102398, // time in milliseconds 
    "ISODate": "2022-09-09T09:09:55.999Z"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_server_time" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
Server Time Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_server_time" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
timestamp	Yes	String	CEX.IO Spot Trading server current time - UTC timestamp in milliseconds.
ISODate	Yes	String	CEX.IO Spot Trading server current date and time in UTC in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ).
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Pairs info
Pair Info method allows Client to receive the parameters for all supported trading pairs.

REQUEST

get_pairs_info

API Rate Limit Cost: 1

Pairs info Request Parameters
Get Pairs Info request

Request (Client sends get pairs info request without any parameters)

{
  "e": "get_pairs_info",
  "oid": "16760424783886_get_pairs_info",
  "data": {}
}
Response (CEX.IO Spot Trading responds to the request with all available pairs for Client)

{
  "e": "get_pairs_info",
  "oid": "16760424783886_get_pairs_info",
  "ok": "ok",
  "data": [
    {
      "base":"BTC",
      "quote":"USD",
      "baseMin":"0.0001",
      "baseMax":"47",
      "baseLotSize":"0.00000001",
      "quoteMin":"10",
      "quoteMax":"1000000",
      "quoteLotSize":"0.01000000",
      "basePrecision":8,
      "quotePrecision":8,
      "pricePrecision":1,
      "minPrice":"14500.2",
      "maxPrice":"24500.2"
    },
    {
      "base": "BTTC",
      "quote": "USD",
      "baseMin": "3888888",
      "baseMax": "1562",
      "baseLotSize": "1",
      "quoteMin": "10",
      "quoteMax": "1000000",
      "quoteLotSize": "0.01000000",
      "basePrecision": 0,
      "quotePrecision": 8,
      "pricePrecision": 8,
      "minPrice": "21.00000000",
      "maxPrice": "0.00000710"
    },
    {
      "base": "ETH",
      "quote": "BTC",
      "baseMin": "0.012",
      "baseMax": "846",
      "baseLotSize": "0.00000100",
      "quoteMin": "0.002",
      "quoteMax": "60",
      "quoteLotSize": "0.00000001",
      "basePrecision": 8,
      "quotePrecision": 8,
      "pricePrecision": 6,
      "minPrice": "0.007437",
      "maxPrice": "0.743700"
    }
  ] 
}
Get Info request (for specific pairs)

Request (Client sends get pairs info request for BTC-USD and ADA-USD trading pairs)

{
  "e": "get_pairs_info",
  "oid": "16760424787386_get_pairs_info",
  "data": {
    "pairs": ["BTC-USD", "ADA-USD"]
  }
}
Response (CEX.IO Spot Trading responds to the request with information about indicated trading pairs)

{ 
  "e": "get_pairs_info",
  "oid": "16760424787386_get_pairs_info",
  "ok": "ok",
  "data": [
    {
      "base": "BTC",
      "quote": "USD",
      "baseMin": "0.0004",
      "baseMax": "60",
      "baseLotSize": "0.00000001",
      "quoteMin": "10",
      "quoteMax": "1000000",
      "quoteLotSize": "0.01000000",
      "basePrecision": 8,
      "quotePrecision": 8,
      "pricePrecision": 1,
      "minPrice": "1700.0",
      "maxPrice": "211250.0"
    },
    {
      "base": "ADA",
      "quote": "USD",
      "baseMin": "50",
      "baseMax": "3786000",
      "baseLotSize": "0.00000100",
      "quoteMin": "10",
      "quoteMax": "1000000",
      "quoteLotSize": "0.01000000",
      "basePrecision": 8,
      "quotePrecision": 8,
      "pricePrecision": 6,
      "minPrice": "0.033583",
      "maxPrice": "3.358320"
    }
  ]
}
Get Pairs Info request (indicated unsupported trading pair)

Request (Client sends get pairs info request for unsupported trading pair)

{
  "e": "get_pairs_info",
  "oid": "16766239787386_get_pairs_info",
  "data": {
    "pairs": ["XXX-YYY"]
  }
}
Response (CEX.IO Spot Trading responds to the request with empty array as requested pair is not supported for Client)

{
  "e": "get_pairs_info",
  "oid": "16766239787386_get_pairs_info",
  "ok": "ok",
  "data": []
}
Get Pairs Info request (indicated unsupported trading pair)

Request (Client sends get pairs info request with indicated pairs parameter but without any specific pairs)

{
  "e": "get_pairs_info",
  "oid": "15283239787386_get_pairs_info",
  "data": {
    "pairs": []
  }
}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "e": "get_pairs_info",
  "oid": "15283239787386_get_pairs_info",
  "ok": "ok",
  "data": {
    "error": "Parameter pairs should be Array of Strings",
    "statusCode": 422
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_pairs_info" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pairs	No	Array of Strings	List of supported trading pairs for which Client wants to receive configuration parameters. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present in the request, then at least 1 pair should be indicated in an array. If this field is absent, then it means Client requests configuration parameters for all supported pairs.
Pairs Info Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_pairs_info" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
X	No	Object	Represents an object which describes specific trading pair configuration parameters in CEX.IO Spot Trading system. If there are no objects in returned array, then it means there are no supported trading pairs, which satisfy Client’s request criteria.
X.base	Yes	String	Name of the first (base) currency in trading pair.
X.quote	Yes	String	Name of the first (base) currency in trading pair.
X.baseMin	Yes	String (parseable as float)	Minimum order amount in base currency.
X.baseMax	Yes	String (parseable as float)	Maximum order amount in base currency.
X.baseLotSize	Yes	String (parseable as float)	Order lot size in base currency. Such limitation allows only order amounts that are a multiple of baseLotSize. For example, if trading pair baseLotSize is 0.5, then order amounts 1.5, 4, 10.5 will be accepted, while amounts 0.3, 1.2, 10.9 will be rejected by the system.
X.quoteMin	Yes	String (parseable as float)	Minimum order amount in quote currency.
X.quoteMax	Yes	String (parseable as float)	Minimum order amount in quote currency.
X.quoteLotSize	Yes	String (parseable as float)	Order lot size in quote currency. Such limitation allows only order amounts that are a multiple of quote lot size. For example, if trading pair quoteLotSize is 0.01, then order amounts 0.5, 4, 10.59 will be accepted, while amounts 0.313, 1.2987, 1000.989 will be rejected by the system.
X.basePrecision	Yes	Number	Number of decimal places for the base currency executed amounts, used inside CEX.IO Spot Trading system.
X.quotePrecision	Yes	Number	Number of decimal places for the quote currency executed amounts, used inside CEX.IO Spot Trading system.
pricePrecision	Yes	Number	Number of allowed decimal places for the trading pair price. Such limitation allows only order prices, the number of decimal places in which doesn’t exceed pricePrecision value. For example, if trading pair pricePrecision is 3, then order limit prices 0.3, 1.94, 10, 10348.591 will be accepted, while prices 0.3136, 1.2987, 1000.98981234 will be rejected by the system.
X.minPrice	Yes	String (parseable as float)	Minimum allowed trading pair price. Orders with indication of prices, which are lower than specified value will be rejected by the system.
X.maxPrice	Yes	String (parseable as float)	Maximum allowed trading pair price. Orders with indication of prices, which are higher than specified value will be rejected by the system.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Currencies Info
Currencies Info method allows Client to receive the parameters for all currencies configured in CEX.IO Spot Trading as well as the deposit and withdrawal availability between CEX.IO Spot Trading and CEX.IO Wallet.

REQUEST

get_currencies_info

API Rate Limit Cost: 1

Currencies Info Request Parameters
Currencies Info request (No parameters indicated)

Request (Client sends the request without any parameters)

{
  "e": "get_currencies_info",
  "oid": "16760424783869_get_currencies_info",
  "data": {}
}
Response (CEX.IO Spot Trading successfully responds to the request with information about all currencies configured in CEX.IO Spot Trading system)

{
  "e": "get_currencies_info",
  "oid": "16760424783869_get_currencies_info",
  "ok": "ok",
  "data": [
    {
      "currency": "USDT",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 6
    },
    {
      "currency": "BTC",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 8
    },
    {
      "currency": "SHIB",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 0,
      "walletPrecision": 0
    },
    {
      "currency": "LUNC",
      "walletDeposit": false,
      "walletWithdrawal": false,
      "fiat": false,
      "precision": 2,
      "walletPrecision": null
    },
    {
      "currency": "USD",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": true,
      "precision": 8,
      "walletPrecision": 2
    }  
  ]
}
Currencies Info request (Indicated 2 specific currencies)

Request (Client sends get currencies info request for 2 currencies)

{
  "e": "get_currencies_info",
  "oid": "16760436274869_get_currencies_info",
  "data": {
    "currencies": ["ETH", "USD"]
  }
}
Response (CEX.IO Spot Trading responds to the request with information for indicated currencies)

{
  "e": "get_currencies_info",
  "oid": "16760436274869_get_currencies_info",
  "ok": "ok",
  "data": [
    {
      "currency": "ETH",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": false,
      "precision": 8,
      "walletPrecision": 6
    },
    {
      "currency": "USD",
      "walletDeposit": true,
      "walletWithdrawal": true,
      "fiat": true,
      "precision": 8,
      "walletPrecision": 2
    }
  ]
}
Currencies Info request (Indicated unsupported currency)

Request (Client sends get currencies info request with indicated unsupported currency)

{
  "e": "get_currencies_info",
  "oid": "16760492853069_get_currencies_info",
  "data": {
    "currencies": ["CCC"]
  }
}
Response (CEX.IO Spot Trading responds to the request with empty array as requested currency is not supported)

{
  "e": "get_currencies_info",
  "oid": "16760492853069_get_currencies_info",
  "ok": "ok",
  "data": []
}
Get Currencies Info request (No currencies indicated)

Request (Client sends get currencies info request with indicated currencies parameter but without any specific currencies)

{
  "e": "get_currencies_info",
  "oid": "16890492853072_get_currencies_info",
  "data": {
    "currencies": [] 
  }
}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "e": "get_currencies_info",
  "oid": "16890492853072_get_currencies_info",
  "ok": "ok", 
  "data": {
    "error": "Parameter currencies should be Array of Strings"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_currencies_info" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
currencies	No	Array of Strings	List of supported currencies for which Client wants to receive configuration parameters. Currencies should be indicated in upper case and of string type. The list should contain only valid currency symbols. If this field is present in the request, then at least 1 currency should be indicated in an array. If this field is absent, then it means Client requests configuration parameters for all supported currencies.
Currencies Info Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_currencies_info" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
X	No	Object	Represents an object which describes specific currency configuration parameters in CEX.IO Spot Trading system. If there are no objects in returned array, then it means there are no supported currencies, which satisfy Client’s request criteria.
X.currency	Yes	String	Currency name.
X.walletDeposit	Yes	Boolean	Describes current availability to deposit currency X to CEX.IO Spot Trading from CEX.IO Wallet. Only true or false values are allowed herein.
X.walletWithdrawal	Yes	Boolean	Describes current availability to withdraw currency X from CEX.IO Spot Trading to CEX.IO Wallet. Only true or false values are allowed herein.
X.fiat	Yes	Boolean	Indicates if the currency is a fiat currency or cryptocurrency. If the value is true, then indicated currency is fiat. If the value is false, then indicated currency is cryptocurrency.
X.precision	Yes	Number	Number of decimal places in amounts of specific currency used inside CEX.IO Spot Trading system (e.g. for internal transfers, executed amounts in orders etc.).
X.walletPrecision	Yes	Number or null	If the value of this parameter is a number, then it describes the number of decimal places in amounts of specific currency used for transfers to or out of CEX.IO Spot Trading system (e.g. for deposits\withdrawals from\to CEX.IO Wallet or external addresses). If the value is null, then deposits and withdrawals of specific currency from\to CEX.IO Wallet are not available.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Processing Info
This request allows Client to receive detailed information about available options to make deposits from external wallets and withdrawals to external wallets as to each supported cryptocurrency, including cryptocurrency name and available blockchains for deposit\withdrawals. Also, as to each supported blockchain there are indicated type of cryptocurrency on indicated blockchain, current deposit\withdrawal availability, minimum amounts for deposits\withdrawals, external withdrawal fees.

Processing Information makes Client more flexible in choosing desired blockchain for receiving Deposit address and initiating external withdrawals via certain blockchain, so that Client uses more convenient way of transferring his crypto assets to or from CEX.IO Ecosystem.

Note that this method indicates minimum deposit\withdrawal limits and external withdrawal fees for external crypto transfers. Currently, deposits and withdrawals of funds between CEX.IO Wallet and CEX.IO Spot Trading account are free.
Currently, external withdrawals are not supported via CEX.IO Spot Trading API.
HTTP REQUEST

get_processing_info

API Rate Limit Cost: 10

Processing Info Request Parameters
Get Processing Info Request for one specific cryptocurrency

Request (Client queries processing info for "BTC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_1_get_processing_info",
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds that only 'bitcoin' blockchain is supported for deposits\withdrawals of "BTC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_1_get_processing_info",
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    }
  }
}
Get Processing Info Request for several cryptocurrencies

Request (Client queries processing info for "BTC" and "USDC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_2_get_processing_info",
  "data": {
    "currencies": ["BTC","USDC"]
  }
}
Response (CEX.IO Spot Trading responds that for deposits\withdrawals 'bitcoin' blockchain is supported for "BTC" and "ethereum", "stellar" and "tron" blockchains are supported for "USDC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_2_get_processing_info",
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    },
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40",
          "depositConfirmations": 25
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 1
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 21
        }
      }
    }
  }
}
Get Processing Info - No available blockchains

Request (Client queries processing info for supported cryptocurrency "ZEC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_4_get_processing_info",
  "data": {
    "currencies": ["ZEC"]
  }
}
Response (CEX.IO Spot Trading responds that request was processed successfully but no blockchains are supported for "ZEC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_4_get_processing_info",
  "ok": "ok",
  "data": {}
}
Get Processing Info - Invalid and fiat cryptocurrency

Request (Client queries processing info for "BTC", "ETH", "XXX" and "USD")

{
  "e": "get_processing_info",
  "oid": "1521724219900_5_get_processing_info",
  "data": {
    "currencies": ["BTC", "ETH", "XXX", "USD"]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currencies "XXX" and "USD" are indicated in the request)

{
  "e": "get_processing_info",
  "oid": "1521724219900_5_get_processing_info",
  "data": {
    "error": "Request contains unsupported currencies: XXX, USD."
  }
}
Get Processing Info - Invalid value type in "currencies" array

Request (Client queries processing info with invalid values type in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_6_get_processing_info",
  "data": {
    "currencies": [1,2,3]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because wrong type of value was indicated in "currencies" array and only string values are allowed)

{
  "e": "get_processing_info",
  "oid": "1521724219900_6_get_processing_info",
  "data": {
    "error": "Currencies array should consist of string type values."
  }
}
Get Processing Info - Not an array indicated in "currencies" field

Request (Client queries processing info with indicating empty object ({}) in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_7_get_processing_info",
  "data": {
    "currencies": {}
  }
}
Response (CEX.IO Spot Trading responds that error occurred because only array is allowed in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_7_get_processing_info",
  "data": {
    "error": "Currencies should be array."
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_processing_info" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
currencies	No	Array	List of cryptocurrencies for which Client wants to get information about supported blockchains for deposit\withdraw, limits and commissions. Cryptocurrencies should be in upper case and of string type. The list should contain only valid cryptocurrency symbols. If this field is missing or contains an empty array ([]), then it means Client wants to get processing info for all available cryptocurrencies.
Processing Info Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_processing_info" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
data.YYY	Yes	String	Cryptocurrency symbol specified in Client's request.
data.YYY.name	Yes	String	Cryptocurrency name.
data.YYY.blockchains	Yes	Object	This object contains info about all supported blockchains to deposit\withdraw cryptocurrency YYY.
data.YYY.blockchains.X	Yes	Object	This object contains details and limitations for deposit\withdrawal of cryptocurrency YYY via blockchain X, including data about blockchain type, current availability to deposit\withdraw, minimum deposit\withdrawal limit and external withdrawal fees.
data.YYY.blockchains.X. type	Yes	String	Type of cryptocurrency YYY on blockchain X.
data.YYY.blockchains.X. deposit	Yes	String	Describes current availability to deposit cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minDeposit	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be deposited from external wallet via blockchain X.
data.YYY.blockchains.X. withdrawal	Yes	String	Describes current availability to withdraw cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minWithdrawal	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be withdrawn to external wallet via blockchain X.
data.YYY.blockchains.X. withdrawalFee	Yes	String (which can be parsed as Float)	Amount of withdrawal fee in cryptocurrency YYY, which which would be charged and subtracted from withdrawal amount if blockchain X is used for withdrawal.
data.YYY.blockchains.X. depositConfirmations	Yes	Number	Minimal confirmation number for transaction in the blockchain to be deposited to Client’s Spot Trading account.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Private API Calls
Connection
Connection should be established using SSL.

WebSocket API Private Endpoint URL

wss://trade.cex.io/api/spot/ws

Either Client or CEX.IO Spot Trading can terminate WebSocket connection at any time.

Once connected, CEX.IO Spot Trading sends “connected” message to Client.

Query Parameters
From	To	Message	Description
CEX.IO Spot Trading	Client	{"e":"connected"}	By successful connection, CEX.IO Spot Trading notifies Client about it by sending him a message.
Keep Connection Alive
To keep connection alive, Client should periodically send any valid message to CEX.IO Spot Trading. Maximum allowed period between two closest Client’s messages is 10 seconds (however, this parameter might be changed by CEX.IO Spot Trading in future). If Client exceeds this limit (meaning, Client sends less than 1 message per 10 seconds), then CEX.IO Spot Trading can terminate the connection.

If Client has no messages to send, then he should send “ping” message to keep the connection alive. Client can send ping messages any time he wishes, even if he has enough other messages to send. Once Client sends a “ping” message, CEX.IO Spot Trading responds with a “pong” message.

Keeping Connection Alive Example
Sequence id	From	To	Message	Description
1	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends “ping”.
2	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
3	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 5 seconds.
4	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
5	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 8 seconds.
6	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
7				CEX.IO Spot Trading keeps connection open if Client sends any valid message at least once per 10 seconds.
Example of Keeping Connection Alive with Idle Client
Sequence id	From	To	Message	Description
1	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends “ping”.
2	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
3	Client	CEX.IO Spot Trading	{"e":"ping"}	Client sends next “ping” in 5 seconds.
4	CEX.IO Spot Trading	Client	{"e":"pong"}	Almost immediately, CEX.IO Spot Trading responds with “pong”.
5				Client does not send any messages for more than 10 seconds.
6	CEX.IO Spot Trading	Client	{"e":"disconnected"}	CEX.IO Spot Trading notifies Client that he is about to Close the connection in a moment because the Client is idle. This message, however, is optional.
7				CEX.IO Spot Trading terminates the connection.
Authentication
CEX.IO Spot Trading uses API keys to allow access to Private APIs.

Client can generate, configure and manage api keys, set permission levels, whitelisted IPs for API key etc. via Spot Trading Web Terminal in the API Keys Management Profile section.

API Keys limit
By default Client can have up to 5 API Keys.
CEX.IO Spot Trading will respond to Client with either ok or error result.

Successful Authentication Example

Response (by successful connection, CEX.IO Spot Trading notifies Client about it by sending him a message)

{
  "e": "connected"
}
Request (Client sends a valid authentication request)

{
  "e": "auth",
  "auth": {
    "key": "djnvod237HF934jcvxj3723",
    "signature": "9732fdd0db3bbbf09941365436840f36e3a2a5d076576f87d154a69c8eab194f",
    "timestamp": 1465229405
  }
}
Response (authentication is successful)

{
  "e": "auth",
  "ok": "ok",
  "data": {
    "ok": "ok"
  }
}
Authentication Request
Field Name	Mandatory	Format	Description	Value Range
e	Yes	String	Describes the type of this message.	auth
timestamp	Yes	Unix time	Represents current Client’s time. To be considered as valid, the moment described in this field should be within 20-second range of Spot Trading’s current time.	Number of seconds that have elapsed since 00:00:00 UTC
key	Yes	String	Client’s apiKey which was provided by CEX.IO Spot Trading earlier.	
signature	Yes	String	Signature is a HMAC-SHA256 encoded message containing: timestamp and API key. The HMAC-SHA256 code must be generated using a secretKey which was provided by CEX.IO Spot Trading earlier. This code must be converted to its hexadecimal representation (64 lowercase characters)	Only numbers and latin characters are allowed
Authentication Response
Signature Example in Python2

message = timestamp + api_key
signature = hmac.new(API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest()
Signature Example in Python3

message = repr(ts) + api_key
signature = hmac.new(bytearray(secret.encode('utf-8')), msg=bytearray(message.encode('utf-8')), digestmod=hashlib.sha256).hexdigest()
Signature Example in NodeJS

const crypto = require('crypto');
var hmac = crypto.createHmac('sha256', apiSecret);
hmac.update(timestamp + apiKey);
var signature = hmac.digest('hex');
Field Name	Mandatory	Format	Description	Value Range
e	Yes	String	Describes the type of this message.	auth
data.ok	This field should be present in case of successful authentication. Otherwise, it should be missing.	String	If this field is present, then authentication is successful. If this field is missing, then authentication is not successful.	ok
ok	This field should be present in case of successful authentication. Otherwise, it should be missing.	String	If this field is present, then authentication is successful. If this field is missing, then authentication is not successful.	ok
data.error	This field should be present in case of unsuccessful authentication. Otherwise, it should be missing.	String	If this field is present, then authentication is not successful. Represents human readable error reason of why authentication is not successful.	
Error Codes
Error Code	Description
Timestamp is not in 20sec range	invalid timestamp
Invalid signature	invalid signature
Invalid API key	mandatory field “key” is missing or is incorrect
API key is not activated	inactivated API key
API Key Permissions
To restrict access to certain functionality while using of API Keys there should be defined specific set of permissions for each API Key. The defined set of permissions can be edited further if necessary.

The following permission levels are available for API Keys:

Read – permission level for viewing of account related data, receiving reports, subscribing to market data etc.

Trade – permission level, which allows placing and cancelling orders on behalf of account.

Funds Internal – permission level, which allows transferring funds between accounts (between sub-accounts or main account and sub-accounts) of CEX.IO Spot Trading Portfolio.

Funds Wallet - permission level, which allows transferring funds from CEX.IO Spot Trading Portfolio accounts (main account and sub-accounts) to CEX.IO Wallet and vice versa.

Required permissions as to each API method are listed in the documentation below.

Unsupported method call
Unsupported method call example

Response (by successful connection, CEX.IO Spot Trading notifies Client about it by sending him a message)

{
  "e": "connected"
}
Request (Client sends a valid authentication request)

{
  "e": "auth",
  "auth": {
    "key": "djnvod237HF934jcvxj3723",
    "signature": "9732fdd0db3bbbf09941365436840f36e3a2a5d076576f87d154a69c8eab194f",
    "timestamp": 1465229405
  }
}
Response (CEX.IO Spot Trading responds that authentication is successful)

{
  "e": "auth",
  "ok": "ok",
  "data": {
    "ok": "ok"
  }
}
Request (Client calls some_unsupported_method WebSocket API method that does not exist)

{
  "e": "some_unsupported_method",
  "oid": "1523433664816_1_some_unsupported_method",
  "data": {
    "foobar": 1
  }
}
Response (CEX.IO Spot Trading responds with error)

{
  "e": "some_unsupported_method",
  "oid": "1523439125503_1_some_unsupported_method",
  "data": {
    "error": "Unsupported message type some_unsupported_method"
  }
}
Response (CEX.IO Spot Trading sends disconnected event and closes WebSocket connection afterwards)

{
  "e": "disconnected"
}
Client sends JSON messages to CEX.IO Spot Trading using WebSocket. Each message should contain e field, which defines the message type. Client should use message types which are described in documentation. Once Client sends message type which is not described in documentation, then CEX.IO Spot Trading replies with error, sends disconnected event to Client and closes WebSocket connection.

API Rate limit
API Rate Limit for Private API calls is defined as to each API Key, which means that if API Rate Limit has been reached for one of Client’s API Key, Client can still proceed with sending requests by other API Keys. Request limits are determined from cost associated with each private API call. By default, each private request has a cost of 1 point, but for some specific requests this cost can be higher. See up-to-date request API Rate Limit cost information in specification of each method.

API Rate Limit is cumulative for API calls made via different protocols (REST & WebSocket) but with the same API Key.
Client request limitations
CEX.IO Spot Trading limits Private API calls to maximum of 200 points per minute, considering that each Private API call has its' cost (see below). If API Rate Limit is reached, then CEX.IO Spot Trading replies with error, sends disconnected event to Client and closes WS connection afterwards. CEX.IO Spot Trading will continue to serve Client starting from the next calendar minute. In the following example, request counter will be reset at 11:02:00.000.
Rate limit exceeded example
Seq id	Time	Type	Message	Comment
1.1	11:01:05.853	Request	{"e":"get_my_funding_history", "data": {"accountId”:"test1"}, "oid": "1523433_1_get_my_funding_history"}	Client sends request to get funding history for accountId “test1”.
1.2	11:01:05.856	Response	{"e":"get_my_funding_history", "oid": "1523433_1_get_my_funding_history", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with funding history.
2.1	11:01:06.001	Request	{"e":"get_my_funding_history", "data": {"accountId”:"test2"}, "oid": "1523433_2_get_my_funding_history"}	Client sends request to get funding history for accountId “test2”.
2.2	11:01:06.104	Response	{"e":"get_my_funding_history", "oid": "1523433_2_get_my_funding_history", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with funding history
...	...	...	...	...
200.1	11:01:20.213	Request	{"e":"get_my_funding_history", "data": {"accountId”:”test200"}, "oid": "1523433_200_get_my_funding_history"}	Client sends request to get funding history for accountId “test200”.
200.2	11:01:20.345	Response	{"e":"get_my_funding_history", "oid": "1523433_300_get_my_funding_history", "data": [],"ok": "ok"}	CEX.IO Spot Trading responds with funding history.
201.1	11:01:20.390	Request	{"e":"get_my_funding_history", "data": {"accountId”:”test201"}, "oid": "1523433_201_get_my_funding_history"}	Client sends request to get funding history for accountId “test201”.
201.2	11:01:20.400	Response	{"e":"get_my_funding_history", "oid": "1523433_201_get_my_funding_history", "data": {"error": "API rate limit reached"}}	CEX.IO Spot Trading responds with error: API rate limit reached.
202.1	11:01:20.403	Response	{"e”:”disconnected”}	CEX.IO Spot Trading notifies Client before disconnecting WS by sending him a disconnected event.
Account Events
Once connected and authenticated, Client continually receives notifications about balance changes of his main account and sub-accounts. Once any event affecting Client’s account balances happens (order placing, order execution, order cancellation, deposit, withdrawal, etc.), then CEX.IO Spot Trading sends a notification to Client through WebSocket with a new account balance snapshot.

Accounts events in WS API should not be used by Client for building own accounting. There are various of reasons not to use it for accounting, the most important is that current WS API does not support resending missed messages (which might happen upon disconnection). Such events are designed as push notifications to allow Client to do some actions in “real-time” manner. For example, it can be used to update balance information in Client’s UI system by each balance change.

Account event represents the snapshot of the Client’s account available balance (funds which Client can use for order placing, for withdrawal, etc.) and on hold balance (funds reserved for active orders, withdrawals in progress, etc.) at some moment in time. So, in case of active trading, such information in the event message might be not up-to-date at the moment Client receives the message. If Client needs to know up-to-date account balances he can additionally use Account Status V3 request to find it out.

Client can ignore such event if he doesn't need it, or can additionally use Account Status V3 request to find out his actual account balances.

Account Event Notification
Account Event Notifications Examples

CEX.IO Spot Trading notifies Client that withdrawal operation was requested from main account and CEX.IO Spot Trading started to process it. New available balance on main account after withdrawal is 0.68 USD. Note that it is not possible to find out details about this withdrawal (such as, withdrawal amount) from this notification as only total onHoldBalance is indicated herein.

{
  "e": "account_update",
  "ok": "ok",
  "data":{
    "clientId": "BitFok",
    "accountId": "",
    "currency": "USD",
    "balance": "0.68000000",
    "onHoldBalance": "1000.00000000",
    "timestamp":1465299989915,
    "action": "withdraw",
    "id": "16552948"
  }
}
CEX.IO Spot Trading notifies Client that some order event happened for order id 2639 for sub-account “hallo”. The updated balance on “hallo” sub-account after order event is 201.86 USD. Note that from this notification, it is not possible to find out what exactly happened (either order creation, or order cancellation, or order execution) with the order, as well as any other details on this order (which order type, etc.). This event just notifies Client that USD balance on “hallo” sub-account was changed and this change happened during processing the order with ID 2639.

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "hallo",
    "currency": "USD",
    "balance": "201.86000000",
    "onHoldBalance": "850.00000000",
    "timestamp": 1465300456900,
    "action": "order",
    "id": "2639"
  }
}
CEX.IO Spot Trading notifies Client that deposit operation was requested to main account and CEX.IO Spot Trading processed it. The updated balance on the main account after deposit is 9.09 BTC.

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "",
    "currency": "BTC",
    "balance": "9.09000000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1465235652000,
    "action": "deposit",
    "id": "12sQff9U13"
  }
}
CEX.IO Spot Trading notifies Client that withdrawal operation was not successful and funds are returned to Client’s main account. The updated balance on the main account after withdrawal rollback is 100 EUR. Note that from this notification, it is not possible to find out the reason of error. However, there is an operation ID “12F009” which should be used during problem investigation, if needed.

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "",
    "currency": "EUR",
    "balance": "100.00000000",
    "onHoldBalance": "52.73000000",
    "timestamp": 1465299989915,
    "action": "withdrawRollback",
    "id": "12F009"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "account_update" value allowed.
data.clientId	Yes	String	Client CompId.
data.accountId	Yes	String	Client’s sub-account ID, on which the balance was changed. If the value is empty string, then it means that the balance on the Client’s main account was changed.
data.currency	Yes	String	Currency for which account balance was changed.
data.action	Yes	String	Action, which triggered account balance change.
data.id	Yes	String	Identifier of the action, which triggered account balance change. For example, if action is “order”, then this field holds identifier of the order (which was assigned by CEX.IO Spot Trading, not Client) that triggered account balance change.
data.balance	Yes	String (which can be parsed as Float)	Represents a snapshot of the account available balance after the action. Note that this snapshot might be inaccurate (means that it can represent available balance snapshot after two actions, but not necessarily after just this single action), for example if some other action happened right after this action. To get the new actual account available balance, Client can additionally make Account Status V3 request.
data.onHoldBalance	Yes	String (which can be parsed as Float)	Represents a snapshot of the account on hold balance (locked in orders, locked for withdrawals etc.). Note that this snapshot might be inaccurate (means that it can represent on hold balance snapshot after two actions, but not necessarily after just this single action), for example if some other action happened right after this action. To get the new actual account on hold balance, Client can additionally make Account Status V3 request.
data.timestamp	Yes	Number	UTC timestamp in milliseconds. Represents a moment in time when the balance snapshot was taken.
ok	No	String	ok value represents that event notification is successfully generated.
Action Types
Action	Description
order	order creation, order cancellation, order execution
deposit	deposit operation is requested
withdraw	withdrawal operation is requested
withdrawRollback	withdrawal error happened, funds are returned back to Client
internalTransfer	internal transfer between Client’s accounts
Current Fee
This method indicates current fees at specific moment of time with consideration of Client's up-to-date 30d volume and day of week (fees can be different for e.g. on weekends).

REQUEST

get_my_current_fee

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Fee Request Parameters
Get Current Fee - Successful request

Request (Client sends request to receive all his trading fees)

{
  "e": "get_my_current_fee",
  "oid": "152171243_get_my_current_fee",
  "data": {}
}
Response (CEX.IO Spot Trading responds with trading fees for all pairs supported for Client)

{
  "e": "get_my_current_fee",
  "oid": "152171243_get_my_current_fee",
  "ok": "ok",
  "data": {
    "tradingFee": {
      "BTC-USD": {
        "percent": "0.5"
      },
      "XRP-USD":{
        "percent": "0.1"
      },
      "ETH-BTC": {
        "percent": "0.1"
      },
      "ADA-USD": {
        "percent": "0.1"
      },
      "ETH-USD": {
        "percent": "0.5"
      },
      "BTC-EUR": {
        "percent": "0.5"
      }
    }
  }
}
Get Current Fee (Indicated specific pairs)

Request (Client sends request to receive his trading fees for specified pair)

{
  "e": "get_my_current_fee",
  "oid": "152171244_get_my_current_fee",
  "data":{
    "pairs": ["BTC-USD","ETH-USD"]
  }
}
Response (CEX.IO Spot Trading responds with trading fees for specified pairs)

{
  "e": "get_my_current_fee",
  "oid": "152171244_get_my_current_fee",
  "ok": "ok",
  "data": {
    "tradingFee":{
      "BTC-USD": {
        "percent": "0.5"
      },
      "ETH-USD":{
        "percent": "0.5"
      }
    }
  }
}
Get Current Fee - Invalid Request

Request (Client sends request to find transactions without valid JSON object)

{
  "e": "get_my_current_fee",
  "oid": "152171245_get_my_current_fee",
  "data": {""}
}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "e": "get_my_current_fee",
  "oid": "152171245_get_my_current_fee",
  "data": {
    "error": "Bad Request"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_current_fee" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pairs	No	Array of strings	Currency pair, for which Client wants to receive his fee. Pair should contain two currencies in upper case divided by "-" symbol. Pair should be listed in traditional direction. For example, "BTC-USD", but not "USD-BTC". If this field is missing, or if it contains empty string (""), or null, then it means Client wants to receive fee for all pairs.
Current Fee Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_current_fee" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
tradingFee	Yes	Object	Represents trading fees for all supported trading pairs.
XXX-YYY	Yes	Object	Represents data about trading fee for specific XXX-YYY trading pair.
XXX-YYY.percent	Yes	String (parseable as float)	Represents fee percent for XXX-YYY trading pair.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Fee Strategy
Fee Strategy returns all fee options, which could be applied for Client, considering Client’s trading volume, day of week, pairs, group of pairs etc.

This method provides information about general fee strategy, which includes all possible trading fee values that can be applied for Client. To receive current trading fees, based on Client's current 30d trading volume, Client should use [Current Fee] method. To receive current 30d trading volume, Client should use [Volume] method.
Trading risk disclaimer
Reduced fees based on volume do not imply reduced trading risk. Trading cryptoassets involves significant risk of loss.
REQUEST

get_fee_strategy

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Fee Strategy Request Parameters
Get Fee Strategy - Successful request

Request (Client requests available Fee Strategies)

{
  "e": "get_fee_strategy",
  "oid": "1465405014648_get_fee_strategy",
  "data": {}
}
Response (CEX.IO Spot Trading responds with default fee options)

{
  "e": "get_fee_strategy",
  "oid": "1465405014648_get_fee_strategy",  
  "ok": "ok",
  "data": {
    "strategyConfig": {
      "default": [
        {
          "fee": "0.25",
          "volume": 10000
        },
        {
          "fee": "0.23",
          "volume": 100000
        },
        {
          "fee": "0.19",
          "volume": 500000
        },
        {
          "fee": "0.17",
          "volume": 1000000
        },
        {
          "fee": "0.15",
          "volume": 2500000
        },
        {
        "fee": "0.13",
        "volume": 5000000
        },
        {
          "fee": "0.11",
          "volume": 10000000
        },
        {
          "fee": "0.10",
          "volume": 20000000
        }
      ]
    }
  }
}
Get Fee Strategy - Successful request

Request (Client requests available Fee Strategies)

{
  "e": "get_fee_strategy",
  "oid": "1465405014649_get_fee_strategy",
  "data": {}
}
Response (CEX.IO Spot Trading responds with multiple fee options, depending on the pair and day of the week)

{
  "e": "get_fee_strategy",
  "oid": "1465405014649_get_fee_strategy",  
  "ok": "ok",
  "data": {
    "strategyConfig": {
      "default": [
        {
          "fee":"0.25",
          "volume":10000
        },
        {
          "fee":"0.23",
          "volume":100000
        },
        {
          "fee":"0.19",
          "volume":500000
        },
        {
          "fee":"0.17",
          "volume":1000000
        },
        {
          "fee":"0.15",
          "volume":2500000
        },
        {
          "fee":"0.13",
          "volume":5000000
        },
        {
          "fee":"0.11",
          "volume":10000000
        },
        {
          "fee":"0.10",
          "volume":20000000
        }
      ],
      "perTier": {
        "reducedFee": {
          "name": "Reduced Fee",
          "description": "Reduced fee description",
          "pairList": [
            "BCH-USD",
            "ETH-USD"
          ],
          "schedule": [
            {
              "fee":"0.15",
              "volume":10000
            },
            {
              "fee":"0.11",
              "volume":30000
            },
            {
              "fee":"0.08",
              "volume":50000
            }
          ]
        },
        "hotPairs": {
          "name": "Hot",
          "description": "Trending pairs",
          "pairList": [
            "ETH-EUR",
            "USDT-GBP"
          ],
          "schedule": [
            {
              "fee":"0.20",
              "volume":10000
            },
            {
              "fee":"0.15",
              "volume":100000
            },
            {
              "fee":"0.10",
              "volume":150000
            }
          ]
        }
      },
      "perWeekend": {
        "default":[
          {
            "fee":"0.22",
            "volume":10000
          },
          {
            "fee":"0.2",
            "volume":100000
          },
          {
            "fee":"0.16",
            "volume":500000
          },
          {
            "fee":"0.14",
            "volume":1000000
          },
          {
            "fee":"0.12",
            "volume":2500000
          },
          {
            "fee":"0.1",
            "volume":5000000
          },
          {
            "fee":"0.08",
            "volume":10000000
          },
          {
            "fee":"0.07",
            "volume":20000000
          }
        ],
        "perTier": {
          "reducedFee": {
            "name": "Reduced Fee",
            "description": "Reduced fee description",
            "pairList": [
              "BCH-USD",
              "ETH-USD"
            ],
            "schedule": [
              {
                "fee":"0.14",
                "volume":10000
              },
              {
                "fee":"0.1",
                "volume":30000
              },
              {
                "fee":"0.07",
                "volume":50000
              }
            ]
          },
          "hotPairs": {
            "name": "Hot",
            "description": "Trending pairs",
            "pairList": [
              "ETH-EUR",
              "USDT-GBP"
            ],
            "schedule": [
              {
                "fee":"0.18",
                "volume":10000
              },
              {
                "fee":"0.13",
                "volume":100000
              },
              {
                "fee":"0.08",
                "volume":150000
              }
            ]
          }
        }
      }
    }
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_fee_strategy" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
Fee Strategy Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_fee_strategy" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
strategyConfig	Yes	Object	This object defines details about Client's available fee options.
default	Yes	Array of objects	Represents possible fee levels, which are applied by default for pairs, if such pairs are not specified in "perTier.pairList" field. If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
default.ObjectN	Yes	Object	Indicate fee value based on Client's 30d total trading volume.
default.ObjectN.fee	Yes	String	Fee percent which will be applied, if Client's 30d total trading volume up to the value, indicated in "volume" of this object.
default.ObjectN.volume	Yes	Number	Represents Client's 30d trading volume (by default in USD), up to which "fee" value is applied. For receiving current 30d trading volume Client should use Volume method.
perTier	No	Object	Represents possible fee levels for specific sets of pairs indicated in "pairList" field of each tier. "perTier" fee levels have higher priority compared to default fee levels. This field could be missing if Client's strategy configuration doesn't include different fee levels for pair tiers.
perTier.CCCCC	No	Object	Describes fee details of "CCCCC" pair tier.
perTier.CCCCC.name	Yes	String	Name of specific pair tier.
perTier.CCCCC.description	Yes	String	Description of specific pair tier.
perTier.CCCCC.pairList	Yes	Array of strings	Indicates trading pairs list, which are included in CCCCC pair tier.
perTier.CCCCC.schedule	Yes	Array of objects	Indicates fee levels, which can be applied for trading pairs from "pairList" field of specific pair tier. If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
perTier.CCCCC.schedule.ObjectM	Yes	Object	Indicate fee value for pair tier CCCCCC based on Client's 30d total trading volume.
perTier.CCCCC.schedule.ObjectM.fee	Yes	String	Fee percent which will be applied for pairs from pair tier CCCCC if Client's 30d total trading volume up to the value, indicated in "volume" field of this object.
perTier.CCCCC.schedule.ObjectM.volume	Yes	Number	Represents Client's 30d trading volume (by default in USD), up to which "fee" value is applied. For receiving current 30d trading volume Client should use Volume method.
perWeekend	No	Object	Represents fees, which apply only on weekends (Saturday and Sunday according to UTC time) and have higher priority than "default" and "perTier" fees. This field can be missing If there are no different weekend fees in fee strategy.
perWeekend.default	No	Array of objects	Represents possible weekend fee levels, which are applied by default for pairs, if such pairs are not specified in "perTier.pairList" field. Has the same srtucture as "default". If returned array contains only 1 object and zero "volume" value, then "fee" value represents fixed commission, which does not depend on Client's 30d trading volume.
perWeekend.perTier	No	Object	Represents possible weekend fee levels for specific sets of pairs indicated in "pairList" field of each tier. "perTier" fee levels have higher priority compared to default fee levels. This field could be missing if Client's strategy configuration doesn't include different fee levels for pair tiers. Has the same structure as "perTier".
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Volume
This request allows Client to receive his trading volume for the last 30 days in USD equivalent.

REQUEST

get_my_volume

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Volume Request Parameters
Get My Volume - Successful request

Request (Client sends request to receive his 30 day trading volume)

{
  "e": "get_my_volume",
  "oid": "186471243_get_my_volume",
  "data": {}
}
Response (CEX.IO Spot Trading responds with Client's 30-day trading volume in USD equivalent)

{
  "e": "get_my_volume",
  "oid": "186471243_get_my_volume",
  "ok": "ok",
  "data": {
    "period": "30d",
    "volume": "35016.9181338",
    "currency": "USD"
  }
}
Get My Volume - Invalid request

Request (Client sends request to find transactions without valid JSON object)

{
  "e": "get_my_volume",
  "oid": "190641243_get_my_volume",
  "data": {[]}
}
Response (CEX.IO Spot Trading responds to the request with error message)

{
  "e": "get_my_volume",
  "oid": "190641243_get_my_volume",
  "data": {
    "error": "Bad Request"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_volume" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
Volume Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_volume" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
period	Yes	String	Represents period for which Client's volume is calculated. Only “30d” value can be returned in this field.
volume	Yes	String (parseable as float)	Represents Client’s cumulative trading volume in “currency” equivalent for returned period.
currency	Yes	String	Represents the currency in which trading volume is calculated. Only “USD” value can be returned in this field.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Create Account
This request allows Client to create new sub-account.

Sub-accounts limit
By default Client can have up to 5 sub-accounts, including main account.
REQUEST

do_create_account

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Create Account Request Parameters
Create Account - Successful request

Request (Client sends request to create new sub-account)

{
  "e": "do_create_account",
  "oid": "186471243_create_account",
  "data": {
    "accountId": "account2",
    "currency": "BTC"
  }
}
Response (CEX.IO Spot Trading responds with accountId that has been created)

{
  "e": "do_create_account",
  "oid": "186471243_create_account",
  "ok": "ok",
  "data": {
    "accountId": "account2"
  }
}
Create Account - Create new sub-account with already existing accountId name

Request (Client sends request to create new sub-account with indicating already existing accountId)

{
  "e": "do_create_account",
  "oid": "186471244_create_account",
  "data": {
    "accountId": "account2",
    "currency": "BTC"
  }
}
Response (CEX.IO Spot Trading responds with indication of accountId, which has already been created. New accountId with the same name is not created.)

{
  "e": "do_create_account",
  "oid": "186471244_create_account",
  "ok": "ok",
  "data": {
    "accountId": "account2"

  }
}
Create Account - Invalid request (missing mandatory parameter)

Request (Client sends request to create new sub-account without indicating requested accountId name)

{
  "e": "do_create_account",
  "oid": "190641298_create_account",
  "data": {
    "currency": "BTC"
  }
}
Response (CEX.IO Spot Trading responds with error indicating mandatory accountId parameter value is missing in Client's request.)

{
  "e": "do_create_account",
  "oid": "190641298_create_account",
  "data": {
    "error": "Mandatory parameter accountId is missing"
  }
}
Create Account - Invalid request (forbidden symbols used)

Request (Client sends request to create new sub-account with forbidden symbols in requested accountId name)

{
  "e": "do_create_account",
  "oid": "190641333_create_account",
  "data": {
    "accountId": "account%2",
    "currency": "BTC"
  }
}
Response (CEX.IO Spot Trading responds with error that requested accountId contained forbidden symbols.)

{
  "e": "do_create_account",
  "oid": "190641298_create_account",
  "data": {
    "error": "Sub-account name should contain only lower and uppercase Latin letters, numbers, underscore (\"_\") or hyphen (\"-\")"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_create_account" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
accountId	Yes	String	New unique sub-account name which Client requests to create. The value in this field can contain only lower and uppercase Latin letters, numbers, underscore ("_") or hyphen ("-").
currency	Yes	String	Represents crypto or fiat currency symbol which Client expects to be initialy deposited to new sub-account (e.g. from Client's other Spot Trading sub-account, from CEX.IO Wallet acount, from external crypto wallet etc.).
Create Account Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_create_account" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
accountId	Yes	String	By default indicates name of new sub-account, which has been created. Nevertheless, if sub-account name requested by Client already exists, CEX.IO Spot Trading will return the name of this sub-account without creating of new sub-account with the same name.
error	No	Object	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Account Status V3
By using Account Status V3 method, Client can find out current balance and its indicative equivalent in converted currency (by default “USD”), amounts locked in open (active) orders as to each sub-account and currency.

If trading fee balance is available for Client, then response will also contain general trading fee balance data such as promo name, currency name, total balance and expiration date of this promo on Trading Fee Balance.

It’s Client’s responsibility to track his sub-accounts available trading balance as current sub-account balance reduced by the balance amount locked in open (active) orders on sub-account.

REQUEST

get_my_account_status_v3

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Account Status V3 Request Parameters
Get My Account Status V3 for All Accounts for All Currencies

Request (Client sends request to find out his accounts’ statuses for all his accounts for all currencies)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168103_1_get_my_account_status_v3",
  "data": {
    "accountIds": []
  }
}
Response (CEX.IO Spot Trading responds that Client has main account with currencies "USD", "ADA" and "BTC" and sub-account "hallo" with currencies "ETH" and "SHIB". Also, it contains balance equivalents in converted currency for each account and each currency)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168103_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "ADA": {
          "balance": "20.24000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "16.21191616"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V2 for selected Sub-accounts for All Currencies

Request (Client sends a request to find out Client's accounts’ statuses for specified accounts for all currencies)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168104_1_get_my_account_status_v3",
  "data": {
    "accountIds": ["hallo", "superhat"]
  }
}
Response (CEX.IO Spot Trading responds that Client has sub-account "hallo" with currencies "ETH" and "SHIB". Sub-account "superhat" status was requested, but is not included into response because Client doesn't have "superhat" sub-account. The main account is not included, because it was not requested)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168104_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for Selected Currencies

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168105_1_get_my_account_status_v3",
  "data": {
    "currencies":["USD","BTC"]
  }
}
Response (CEX.IO Spot Trading responds that Client has main account and sub-account "account123", each with currencies "USD" and "BTC". Note that other currencies (like "EUR", "ETH" etc.) are not included into response, because their balances were not requested)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168105_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "USD": {
          "balance": "100.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "100.00000000"
        },
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for One Selected Currency

Request (Client sends request to find out his accounts’ statuses for all accounts for "BTC" currency)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168106_1_get_my_account_status_v3",
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds that main account and sub-account "account123" have "BTC" balances. Note that other currencies (like "USD", "EUR", "SHIB" etc.) and other sub-accounts are not included in the response, because they were not requested or do not contain balances in requested currencies)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168106_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V3 - No Account Matching Criteria

Request (Client sends request to find out his accounts’ statuses for main account and sub-account "hallo" only for "EUR" currency balance)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168107_1_get_my_account_status_v3",
  "data": {
    "currencies": ["EUR"],
    "accountIds": ["", "hallo"]
  }
}
Response (CEX.IO Spot Trading responds that Client has no accounts which satisfy request criteria)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168107_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {}
  }
}
Get My Account Status V3 for Single Account for Single Currency

Request (Client sends request to find out the main account status for USD currency)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168108_1_get_my_account_status_v3",
  "data": {
    "currencies": ["USD"],
    "accountIds": [""]
  }
}
Response (CEX.IO Spot Trading responds that Client has main account and includes USD balance on it. No other accounts are included, and no other currencies are included, because they were not requested for)

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168108_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "100.79438200",
          "balanceOnHold": "70.00000000",
          "balanceInConvertedCurrency": "100.79438200"
        }
      }
    }
  }
}
Get My Account Status V3 for All Accounts for Selected Currencies with available Trading Fee Balance

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies. Client has available Trading Fee Balance)

Note that Client has available "lifetimeBonus" and limited "welcome_bonus" for USDT currency

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168109_1_get_my_account_status_v3",
  "data": {
      "currencies":["USD","BTC","USDT"]
  }
}
Response (CEX.IO Spot Trading responds that Client has balances in "EUR", "USD", "BTC" and "USDT" on main account, balance in "USD" on "subAccount2" sub-account and two trading fee balances)

Note that Client has available "lifetimeBonus" and limited "welcome_bonus" for USDT currency

{
  "e": "get_my_account_status_v3",
  "oid": "1465340168109_1_get_my_account_status_v3",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
          "USD": {
            "balance": "87683.66518161",
            "balanceOnHold": "0.00000000",
            "balanceInConvertedCurrency": "87683.66518161"
          },
          "BTC": {
            "balance": "564.88201513",
            "balanceOnHold": "0.00000000",
            "balanceInConvertedCurrency": "15114322.12602735"
          },
          "USDT": {
            "balance": "995752294.59920270",
            "balanceOnHold": "0.00000000",
            "balanceInConvertedCurrency": "991868860.65026580"
          }
      },
      "subAccount2": {
          "USD": {
            "balance": "123.00000000",
            "balanceOnHold": "0.00000000",
            "balanceInConvertedCurrency": "123.00000000"
        }
      }
    },
  "tradingFeeBalancesPerAccounts": {
    "lifetimeBonus": {
        "USDT": {
          "balance": "50.00000000"
        }
      },
    "welcome_bonus": {
        "USDT": {
          "balance": "15.00000000",
          "expirationDate": "2023-07-28T17:20:00.000Z"
        }
      }
    }
  }
}
Get My Account Status V3 - Incorrect Request

Request (Client sends request, however "accountIds" field contains not an Array but a number value)

{
  "e": "get_my_account_status_v3",
  "oid": "1465392818634_2_get_my_account_status_v3",
  "data": {
    "accountIds": 3,
    "currencies":["BTC"]
  }
}
Response (CEX.IO Spot Trading responds about request processing error because not an array has been sent in "accountIds" field and "accountIds" array should consist of string type values)

{
  "e": "get_my_account_status_v3",
  "oid": "1465392818634_2_get_my_account_status_v3",
  "data": {
    "error": "accountIds array should consist of string type values"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_account_status_v3" value allowed.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. It might be empty object ("{}"), which means that Client sets no criteria for accounts. However, this field should be present anyway and it should contain an object. Setting no criteria for accounts means that Client wants to get statuses for all accounts and for all currencies. CEX.IO Spot Trading encourages Client to always set criteria to get only the accounts which Client is interested in. It will make request processing faster and Client will get a faster response.
data.currencies	No	Array	List of currencies for which Client wants to find out their accounts' balances. Currencies should be in upper case and of string type. Each currency should be present only once in this array. For example, ["USD", "BTC", "EUR", "BTC"] is not allowed. If this field is missing or contains an empty array ([]), then it means Client wants to find out balances for all available currencies.
data.accountIds	No	Array	List of account identifiers for which Client wants to find out their accounts' balances. Empty string ("") value in this array represents Client’s main account. Each account identifier should be of string type and should be present only once in this array. For example, ["hallo", "", "account123", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find out balances for all accounts.
Account Status V3 Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_account_status_v3" value allowed.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only ok value is allowed here.
data	Yes	Object	This object contains response details. It should contain balancesPerAccounts and convertedCurrency mandatory fields and could also contain creditLine optional field (if credit line is enabled for Client).
data.convertedCurrency	Yes	String	The currency in which balanceInConvertedCurrency is calculated by CEX.IO Spot Trading. By default only "USD" value is allowed herein.
data.balancesPerAccounts	Yes	Object	This object contains details about Client's currencies' balances as to each account which satisfies request criteria. It might be empty object ("{}"), but this field should be present anyway and it should contain an object. If this field contains an empty object, then it means Client has no accounts which satisfy Client’s request criteria.
data.balancesPerAccounts.X	No	Object	Represents an object which describes X account statuses for each currency. If X is ""(empty string), that means X is main account. Otherwise, it represents X sub-account.
data.balancesPerAccounts.X.YYY	No	Object	Represents an object which describes X account statuses for YYY currency.
data.balancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency. It includes balance which is reserved (locked) for active orders (please find this information in "balanceOnHold" field).
data.balancesPerAccounts.X.YYY. balanceOnHold	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is reserved (locked) for active orders.
data.balancesPerAccounts.X.YYY. balanceInConvertedCurrency	No	String (which can be parsed as Float)	Equivalent in converted currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in converted currency, then this field would be missing.
data.tradingFeeBalancesPerAccounts	No	Object	This object contains details about Client’s trading fee balances. This object can be absent if Client has no available trading fee balances because they were never obtained OR if all of obtained trading fee balances have already expired or were fully utilized.
data.tradingFeeBalancesPerAccounts.X	Yes	Object	Represents an object which describes available trading fee balances which were obtained in the framework of X promo campaign name or as a “lifetimeBonus”.
data.tradingFeeBalancesPerAccounts.X.YYY	Yes	Object	Represents an object which describes details as to YYY currency trading fee balance.
data.tradingFeeBalancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Available amount of YYY currency trading fee balance, expirationDate of which has not been reached yet and which can be used for trading fee utilization.
data.tradingFeeBalancesPerAccounts.X.YYY. expirationDate	No	Datetime	Expiration date of YYY currency trading fee balance. Format: YYYY-MM-DDTHH:MM:SS.sssZ .This field can be absent for “lifetimeBonus” trading fee account, which means YYY trading fee balance amount has no set expiration date.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Account Status V2 (deprecated)
Notice
Account Status V2 method is deprecated. Information about current balances and Trading Fee Balance (if available) can be requested only via Account Status V3 ([REST], [WebSocket] specifications) method.
Using Account Status V2 request, Client can find out current balance and its indicative equivalent in converted currency (by default “USD”), available trading balance and amounts which are locked in open (active) orders as to each sub-account and currency.

Available trading balance is calculated as current balance plus overdraft limit (if allowed for the Client) and reduced by the balance amount locked in open (active) orders.

If credit line is enabled for Client, then response will also contain data as to the base currency name, exposure limit, total debt amount, currencies balance equivalents in base currency as to each currency on all Client’s accounts (main account and sub-accounts).

If overdraft limit for specific currency is enabled for Client, then response will also contain data as to amount of overdraft limit for such currency on all Client’s accounts (main account and sub-account), which have balance in specified currency.

REQUEST

get_my_account_status_v2

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Account Status V2 Request Parameters
Get My Account Status V2 for All Accounts for All Currencies

Request (Client sends request to find out his accounts’ statuses for all his accounts for all currencies)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "accountIds": []
  }
}
Response (CEX.IO Spot Trading responds that Client has main account with currencies "USD", "ADA" and "BTC" and sub-account "hallo" with currencies "ETH" and "SHIB". Also, it contains balance equivalents in converted currency for each account and each currency)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "39.79438200",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "ADA": {
          "balance": "20.24000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "20.24000000",
          "balanceInConvertedCurrency": "16.21191616"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "15.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceAvailable": "362523",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V2 for selected Sub-accounts for All Currencies

Request (Client sends a request to find out Client's accounts’ statuses for specified accounts for all currencies)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "accountIds": ["hallo", "superhat"]
  }
}
Response (CEX.IO Spot Trading responds that Client has sub-account "hallo" with currencies "ETH" and "SHIB". Sub-account "superhat" status was requested, but is not included into response because Client doesn't have "superhat" sub-account. The main account is not included, because it was not requested)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "hallo": {
        "ETH": {
          "balance": "15.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "15.00000000",
          "balanceInConvertedCurrency": "38962.11113119"
        },
        "SHIB": {
          "balance": "1573107",
          "balanceOnHold": "1210584",
          "balanceAvailable": "362523",
          "balanceInConvertedCurrency": "35.61514248"
        }
      }
    }
  }
}
Get My Account Status V2 for All Accounts for Selected Currencies

Request (Client sends request to find out his accounts’ statuses for all accounts for selected currencies)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "currencies":["USD","BTC"]
  }
}
Response (CEX.IO Spot Trading responds that Client has main account and sub-account "account123", each with currencies "USD" and "BTC". Note that other currencies (like "EUR", "ETH" etc.) are not included into response, because their balances were not requested)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "39.79438200",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "39.79438200",
          "balanceInConvertedCurrency": "39.79438200"
        },
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "USD": {
          "balance": "100.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "100.00000000",
          "balanceInConvertedCurrency": "100.00000000"
        },
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "1.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V2 for All Accounts for One Selected Currency

Request (Client sends request to find out his accounts’ statuses for all accounts for "BTC" currency)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds that main account and sub-account "account123" have "BTC" balances. Note that other currencies (like "USD", "EUR", "SHIB" etc.) and other sub-accounts are not included in the response, because they were not requested or do not contain balances in requested currencies)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "BTC": {
          "balance": "0.00040000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "0.00040000",
          "balanceInConvertedCurrency": "15.67344000"
        }
      },
      "account123": {
        "BTC": {
          "balance": "1.00000000",
          "balanceOnHold": "0.00000000",
          "balanceAvailable": "1.00000000",
          "balanceInConvertedCurrency": "39157.90502748"
        }
      }
    }
  }
}
Get My Account Status V2 - No Account Matching Criteria

Request (Client sends request to find out his accounts’ statuses for main account and sub-account "hallo" only for "EUR" currency balance)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "currencies": ["EUR"],
    "accountIds": ["", "hallo"]
  }
}
Response (CEX.IO Spot Trading responds that Client has no accounts which satisfy request criteria)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {}
  }
}
Get My Account Status V2 for Single Account for Single Currency

Request (Client sends request to find out the main account status for USD currency)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "data": {
    "currencies": ["USD"],
    "accountIds": [""]
  }
}
Response (CEX.IO Spot Trading responds that Client has main account and includes USD balance on it. No other accounts are included, and no other currencies are included, because they were not requested for)

{
  "e": "get_my_account_status_v2",
  "oid": "1465340168103_1_get_my_account_status_v2",
  "ok": "ok",
  "data": {
    "convertedCurrency": "USD",
    "balancesPerAccounts": {
      "": {
        "USD": {
          "balance": "100.79438200",
          "balanceOnHold": "70.00000000",
          "balanceAvailable": "30.79438200",
          "balanceInConvertedCurrency": "100.79438200"
        }
      }
    }
  }
}
Get My Account Status V2 - Incorrect Request

Request (Client sends request, however "accountIds" field contains not an Array but a number value)

{
  "e": "get_my_account_status_v2",
  "oid": "1465392818634_2_get_my_account_status_v2",
  "data": {
    "accountIds": 3,
    "currencies":["BTC"]
  }
}
Response (CEX.IO Spot Trading responds about request processing error because not an array has been sent in "accountIds" field and "accountIds" array should consist of string type values)

{
  "e": "get_my_account_status_v2",
  "oid": "1465392818634_2_get_my_account_status_v2",
  "data": {
    "error": "accountIds array should consist of string type values"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_account_status_v2" value allowed.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. It might be empty object ("{}"), which means that Client sets no criteria for accounts. However, this field should be present anyway and it should contain an object. Setting no criteria for accounts means that Client wants to get statuses for all accounts and for all currencies. CEX.IO Spot Trading encourages Client to always set criteria to get only the accounts which Client is interested in. It will make request processing faster and Client will get a faster response.
data.currencies	No	Array	List of currencies for which Client wants to find out their accounts' balances. Currencies should be in upper case and of string type. Each currency should be present only once in this array. For example, ["USD", "BTC", "EUR", "BTC"] is not allowed. If this field is missing or contains an empty array ([]), then it means Client wants to find out balances for all available currencies.
data.accountIds	No	Array	List of account identifiers for which Client wants to find out their accounts' balances. Empty string ("") value in this array represents Client’s main account. Each account identifier should be of string type and should be present only once in this array. For example, ["hallo", "", "account123", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find out balances for all accounts.
Account Status V2 Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_account_status_v2" value allowed.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only ok value is allowed here.
data	Yes	Object	This object contains response details. It should contain balancesPerAccounts and convertedCurrency mandatory fields and could also contain creditLine optional field (if credit line is enabled for Client).
data.convertedCurrency	Yes	String	The currency in which balanceInConvertedCurrency is calculated by CEX.IO Spot Trading. By default only "USD" value is allowed herein.
data.creditLine	No	Object	This object contains details about Client's credit line configuration (if enabled for Client), including information about the base currency, exposure limit and total debt. If credit line is not enabled for Client, then this field would be missing.
data.balancesPerAccounts	Yes	Object	This object contains details about Client's currencies' balances as to each account which satisfies request criteria. It might be empty object ("{}"), but this field should be present anyway and it should contain an object. If this field contains an empty object, then it means Client has no accounts which satisfy Client’s request criteria.
data.balancesPerAccounts.X	No	Object	Represents an object which describes X account statuses for each currency. If X is ""(empty string), that means X is main account. Otherwise, it represents X sub-account.
data.balancesPerAccounts.X.YYY	No	Object	Represents an object which describes X account statuses for YYY currency.
data.balancesPerAccounts.X.YYY. balance	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency. It includes balance which is reserved (locked) for active orders (please find this information in "balanceOnHold" field).
data.balancesPerAccounts.X.YYY. balanceOnHold	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is reserved (locked) for active orders.
data.balancesPerAccounts.X.YYY. balanceAvailable	Yes	String (which can be parsed as Float)	Current X account balance in YYY currency which is available for trading. It is calculated as current X account balance in YYY currency plus overdraft limit for YYY currency (if enabled for the Client) and reduced by the X account balance amount in YYY currency, which is locked in open (active) orders.
data.balancesPerAccounts.X.YYY. balanceInBaseCurrency	No	String (which can be parsed as Float)	Equivalent in base currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If credit line is not enabled for Client OR if current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in base currency, then this field would be missing.
data.balancesPerAccounts.X.YYY. balanceInConvertedCurrency	No	String (which can be parsed as Float)	Equivalent in converted currency of current YYY currency balance on Client's X account. This amount is calculated according to CEX.IO Spot Trading indicative exchange rate of YYY currency to base currency. If current YYY currency balance on Client's X account is zero OR if CEX.IO Spot Trading failed to calculate such equivalent in converted currency, then this field would be missing.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Wallet Balance
This request allows Client to receive his CEX.IO Wallet balances, which can be useful for Client to check his current Wallet balances before depositing funds from to Spot Trading sub-accounts or after withdrawing funds from Spot Trading sub-accounts to CEX.IO Wallet account.

REQUEST

get_my_wallet_balance

API Rate Limit Cost: 5

API Key Permission

This method requires "Read" permission set for API Key.

Wallet Balance Request Parameters
Get My Wallet Balance - Successful request

Request (Client sends request to receive his Wallet account balances)

{
  "e": "get_my_wallet_balance",
  "oid": "186471243_get_my_wallet_balance",
  "data": {}
}
Response (CEX.IO Spot Trading responds with Client's current balances in BTC, ETH, USD, EUR on his Wallet account)

{
  "e": "get_my_wallet_balance",
  "oid": "186471243_get_my_wallet_balance",
  "ok": "ok",
  "data": {
    "BTC": {
      "balance": "9.72101000"
    },
    "ETH": {
      "balance": "10.000000"
    },
    "USD": {
      "balance": "23567.02"
    },
    "EUR": {
      "balance": "728.99"
    }
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_wallet_balance" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. Empty object should be sent to get Client's CEX.IO Wallet account balances.
Wallet Balance Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_wallet_balance" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
XXX	Yes	Object	Represents an object which describes CEX.IO Wallet account status for XXX currency.
XXX.balance	Yes	String (which can be parsed as Float)	Current CEX.IO Wallet account balance in XXX currency.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Orders
This request allows Client to find out info about his orders.

Duplicated clientOrderIds
If Client has several orders with the same clientOrderId (if orders were created in a significant period of time) and will query orders by clientOrderId, response will return an array with all orders’ details in which requested clientOrderId has been indicated by the Client.
REQUEST

get_my_orders

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Orders Request Parameters
Get My Orders - All Open Orders

Request (Client sends request to find all his open orders for all pairs and all accounts)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {}
}
Response (CEX.IO Spot Trading responds that Client has 3 open orders)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "26", // Market BUY 0.01 BTC/USD with main account
      "clientOrderId": "1465300456557-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Market",
      "timeInForce": null,
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.01000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": null,
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": null,
      "initialOnHoldAmountCcy2": "21.00000000",
      "expireTime": null,
      "effectiveTime": null
    },
    {
      "orderId": "20", // Limit BUY 0.1 BTC/USD at price 400 with "hallo" sub-account
      "clientOrderId": "1465299989578-0",
      "clientId": "BitFok",
      "accountId": "hallo",
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.10000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": "400.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": null,
      "initialOnHoldAmountCcy2": "21.00000000",
      "expireTime": null,
      "effectiveTime": null
    },
    {
      "orderId": "18", // Limit SELL 0.02 BTC/EUR at price 600 with main account
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders with Paging

Request (Client sends request to find all his open orders and wants to see the second page expecting the result set is chunked to pages size 2 (not more than 2 orders per page))

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "pageSize": 2,
    "pageNumber": 1
  }
}
Response (supposed that Client has 3 open orders (like in previous example), CEX.IO Spot Trading responds with second page, which includes only the last single order)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders for Selected Pair

Request (Client sends request to find all his open orders for "BTC-EUR" pair)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "pair": "BTC-EUR"
  }
}
Response (CEX.IO Spot Trading responds that Client has 1 open order for BTC-EUR pair)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - All Open Orders for Account and Pair

Request (Client sends request to find all his open orders for currency pair "BTC-USD" and for sub-accounts "hallo" or "superhat")

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "accountIds": ["hallo", "superhat"],
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading responds that Client has only one open order that satisfies request criteria, this order is on "hallo" sub-account)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "20",
      "clientOrderId": "1465299989578-0",
      "clientId": "BitFok",
      "accountId": "hallo",
      "status": "NEW",
      "currency1": "BTC",
      "currency2": "USD",
      "side": "BUY",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": null,
      "rejectReason": null,
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.10000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "USD",
      "price": "400.0000",
      "averagePrice": null,
      "statusIsFinal": false,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - Accounts, Paging, Period, Empty Result

Request (Client wants to see not more than 50 open orders from main account which were received by server between 2016-06-06T16:11:29 and 2016-06-07T08:53:09)

{
  "e": "get_my_orders",
  "oid": "2_1_get_my_orders",
  "data": {
    "accountIds": [""],
    "pageSize": 50,
    "serverCreateTimestampFrom": 1465229489578,
    "serverCreateTimestampTo": 1465289589579
  }
}
Response (CEX.IO Spot Trading responds that Client has no open orders, which satisfy request criteria)

{
  "e": "get_my_orders",
  "oid": "2_1_get_my_orders",
  "ok": "ok",
  "data": []
}
Get My Orders - All Archived Orders for Selected Side

Request (Client sends request to find all his archived orders)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "archived": true,
    "side": "SELL",
    "serverCreateTimestampFrom": 1516699048964,
    "serverCreateTimestampTo": 1516699987501
  }
}
Response (supposed that Client has 3 archived orders (like in previous example), CEX.IO Spot Trading responds to Client that he has 1 archived order which satisfies request criteria)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Order - Incorrect Request

Request (Client sends a request, but doesn't specify mandatory "data" field)

{
  "e": "get_my_orders",
  "oid": "1465409645363_1_get_my_orders"
}
Response (CEX.IO Spot Trading responds that error occurred. Note: "data" field hold an object value here, not the array)

{
  "e": "get_my_orders",
  "oid": "1465409645363_1_get_my_orders",
  "data": {
    "error": "Internal error"
  }
}
Get My Order - Page Size is Too Big

Request (Client sends a request to get all archived orders and wishes to get first 5,000 orders list as a response to this request)

{
  "e": "get_my_orders",
  "oid": "1465477794024_1_get_my_orders",
  "data": {
    "archived": true,
    "pageSize": 5000
  }
}
Response (CEX.IO Spot Trading responds that such request is not allowed. Requested page size is too big, maximum allowed value is 1000)

{
  "e": "get_my_orders",
  "oid": "1465477794024_1_get_my_orders",
  "data": {
    "error": "Page size is limited to 1000 items"
  }
}
Get My Order - Incorrect Archived Type

Request (Client made a request to get his open orders, however "archived" field value is a number)

{
  "e": "get_my_orders",
  "oid": "1465478161261_1_get_my_orders",
  "data": {
    "archived": 0
  }
}
Response (CEX.IO Spot Trading responds that such request is not allowed. Field "archived" should be either true, or false, or it should be missing)

{
  "e": "get_my_orders",
  "oid": "1465478161261_1_get_my_orders",
  "data": {
    "error": "Archived parameter should be boolean"
  }
}
Get My Orders - Single Order by OrderId

Request (Client sends request to find his single order by orderId)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "orderId": 18
  }
}
Response (CEX.IO Spot Trading responds with status of this order)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Get My Orders - Single Order by clientOrderId

Request (Client sends request to find his single order by clientOrderId)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "data": {
    "clientOrderId": "1465299852968-0"
  }
}
Response (CEX.IO Spot Trading responds with status of this order)

{
  "e": "get_my_orders",
  "oid": "1465405014762_1_get_my_orders",
  "ok": "ok",
  "data": [
    {
      "orderId": "18",
      "clientOrderId": "1465299852968-0",
      "clientId": "BitFok",
      "accountId": null,
      "status": "REJECTED",
      "currency1": "BTC",
      "currency2": "EUR",
      "side": "SELL",
      "orderType": "Limit",
      "timeInForce": "GTC",
      "comment": null,
      "rejectCode": 403,
      "rejectReason": "Insufficient funds",
      "executedAmountCcy1": null,
      "executedAmountCcy2": null,
      "requestedAmountCcy1": "0.02000000",
      "requestedAmountCcy2": null,
      "feeAmount": null,
      "feeCurrency": "EUR",
      "price": "600.0000",
      "averagePrice": null,
      "statusIsFinal": true,
      "clientCreateTimestamp": 1516699748938,
      "serverCreateTimestamp": 1516699748964,
      "lastUpdateTimestamp": 1516699748983,
      "initialOnHoldAmountCcy1": "0.02000000",
      "initialOnHoldAmountCcy2": null,
      "expireTime": null,
      "effectiveTime": null
    }
  ]
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_orders" value allowed.
oid	Yes	String	Unique ID of this request
data	Yes	Object	This object contains request details. It might be empty object ("{}"), which means that Client sets no criteria for orders, which Client wants to see. However, this field should be present anyway and it should contain an object. Setting no criteria for orders means that Client wants to get statuses for all his open orders.
clientOrderId	No	String	Order identifier assigned by Client. If this field is present, then it means Client wants to see the status of the exact order. In this case, CEX.IO Spot Trading ignores all other parameters in "data" field.
orderId	No	Number	Order identifier assigned by CEX.IO Spot Trading. If both fields "orderId" and "clientOrderId" are present, then CEX.IO Spot Trading ignores "orderId" field. If this field is present (and "clientOrderId" is not present), then it means Client wants to see the status of the exact order. In this case, CEX.IO Spot Trading ignores all other parameters in "data" field.
archived	No	Boolean	If value is true, then it means Client wants to get his completed (archived) orders. "Completed" means that order is in one of its final statuses. If value is false or if this field is missing, it means Client wants to get his open orders. Value should be in boolean type. So values like null, 0, 1, "true", "hallo" and similar are not allowed.
pair	No	String	Currency pair, for which Client wants to find his orders. Pair should contain two currencies in upper case divided by "-" symbol. Pair should be listed in traditional direction. For example, "BTC-USD", but not "USD-BTC". If this field is missing, or if it contains an empty string (""), or null, then it means Client wants to find his orders for all pairs.
side	No	String	Side of the orders, for which Client wants to find his orders.
accountIds	No	Array	List of account identifiers, for which Client wants to find his orders. Empty string ("") or null value in this array represents Client’s main account. Each account identifier should be present only once in this array. For example, ["hallo", "", "superhat", "hallo"] is not allowed. If this field is missing or if it contains an empty array ([]), then it means Client wants to find his orders for all accounts.
serverCreate TimestampFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest server timestamp when order is received. In the result set orders’ serverCreateTimestamp should be greater than or equal to (>=) serverCreateTimestampFrom. Period indicated by serverCreateTimestampFrom and serverCreateTimestampTo values can not be greater than 365 days. This parameter is mandatory if Client queries info about archived orders.
serverCreate TimestampTo	No	Number	UTC timestamp in milliseconds. Represents the latest server timestamp when order is received. In the result set orders’ serverCreateTimestamp should be less than (<) serverCreateTimestampTo. Period indicated by serverCreateTimestampFrom and serverCreateTimestampTo values can not be greater than 365 days. If this field is missing than current date is set by default.
sortOrder	No	String	Sort order of the result set. The result array is sorted by serverCreateTimestamp. "ASC" - ascending order, "DESC" - descending order. If this field is missing then the default sort order is "DESC".
pageSize	No	Number	Because the result might contain too many orders, Client should specify which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of orders in the result for this request. If this field is missing, then the default value of 1000 is used. This value cannot be greater than 1000.
pageNumber	No	Number	Because the result might contain too many orders, Client should specify which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize orders per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 0. If this field is missing, then the default value of 0 is used. This value cannot be lower then 0.
Orders Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_orders" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Array or Object	This object contains list of orders which satisfy request criteria. It might be an empty array ([]). If this array is empty, then it means Client has no orders, which satisfy Client’s request criteria. The result array is sorted by "clientOrderCreationTimestamp" field with specified order. In case of error, the value of this filed should be not Array, but Object.
orderId	Yes	String	Order identifier assigned by CEX.IO Spot Trading.
clientOrderId	Yes	String	Order identifier assigned by Client.
clientId	Yes	String	Client Comp id.
accountId	Yes	String	Represents Client’s account id, which was used for order processing. If this value is null, then it means Client’s main account. Otherwise, it means identifier of Client’s sub-account.
status	Yes	String	Represents current execution status of this order. Status can be PENDING_NEW, NEW, PARTIALLY_FILLED, FILLED, EXPIRED, REJECTED, PENDING_CANCEL, CANCELLED.
statusIsFinal	Yes	Boolean	Represents whether this order is in the final state or not.
currency1	Yes	String	Represents first currency in currency pair of this order.
currency2	Yes	String	Represents second currency in currency pair of this order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timeInForce	Yes	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders where time in force is not applied, for example, for Market orders.
comment	Yes	String	Text, which was provided by Client during order creation. If value is null, then it means Client did not provide such text during order creation.
rejectCode	Yes	Number	Error code if the order is rejected. If value is null, that means there is no error code.
rejectReason	Yes	String	Human readable error description if the order is rejected. If value is null, that means there is no error description.
executedAmountCcy1	Yes	String (which can be parsed as Float)	Represents executed amount in currency1. If this value is null, then it means there is no executed amount (order has no executions).
executedAmountCcy2	Yes	String (which can be parsed as Float)	Represents executed amount in currency2. If this value is null, then it means there is no executed amount (order has no executions).
requestedAmountCcy1	Yes	String (which can be parsed as Float)	Represents order amount in currency1, which was requested by Client. If this value is null, then it means there is no requested amount in currency1 (order should have then requested amount in currency2)
requestedAmountCcy2	Yes	String (which can be parsed as Float)	Represents order amount in currency2, which was requested by Client. If this value is null, then it means there is no requested amount in currency2 (order should have then requested amount in currency1).
initialOnHoldAmountCcy1	Yes	String (which can be parsed as Float)	Represents amount in currency1 which was hold from Client balance by CEX.IO Spot Trading before order execution. If this value is null, then it means that amount in currency1 was not hold from Client's account for this order.
initialOnHoldAmountCcy2	Yes	String (which can be parsed as Float)	Represents amount in currency2 which was hold from Client balance by CEX.IO Spot Trading before order execution. If this value is null, then it means that amount in currency2 was not hold from Client's account for this order.
feeAmount	Yes	String (which can be parsed as Float)	Represents order commission amount, which was charged for this order. If this value is null, then it means there is no commission amount charged for this order.
feeCurrency	Yes	String	Represents order commission currency.
price	Yes	String (which can be parsed as Float)	Represents order price, which was provided by Client during order creation. If this value is null, then it means there is no requested price for this order. It happens for orders where price cannot be requested, for example, Market orders or Stop orders.
averagePrice	Yes	String (which can be parsed as Float)	Represents average order execution price. If this value is null, then it means there is no executed amount (order has no executions).
clientCreateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents a timestamp provided by Client during creation of the order.
serverCreateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents server timestamp when order was received.
lastUpdateTimestamp	Yes	Number	UTC timestamp in milliseconds. Represents server timestamp when order changed its state last time.
expireTime	Yes	Number	UTC timestamp in milliseconds. Represents an expired timestamp provided by Client during creation of the order. If this value is null, then it means Client did not provide expire time during order creation.
effectiveTime	Yes	Number	UTC timestamp in milliseconds. Represents an effective timestamp provided by Client during creation of the order. If this value is null, then it means that Client did not provide effective time during order creation.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
New Order
This method works only with CEX.IO Spot Trading sub-accounts.
Client can place new orders via WebSocket API by using Do My New Order Request. Along with a response to this request, CEX.IO Spot Trading sends Account Event and Execution Report messages to Client if the request is successful.

Response message indicates the last up-to-date status of order which is available in the system at the moment of sending the response.

If the Client did not receive a Response message to Do My New Order Request - the Client can query current status of the order by using Get My Orders Request with clientOrderId parameter.

When sending a request for new order, it is highly recommended to use clientOrderId parameter which corresponds to the specific new order request on the client's side. Spot Trading protects multiple placing of orders with the same clientOrderId for a reasonable period of time.

If more than one new orders with identical clientOrderId and other order parameters are identified - Spot Trading places only the first order and returns the status of such order to the Client in response to the second and subsequent new order requests with the same parameters. If orders with identical clientOrderId but with different other order parameters are identified - Spot Trading processes only the first order and rejects the second and subsequent new order requests with the same clientOrderID but with different other order parameters. Nevertheless, if Client creates more than one orders with same clientOrderId in a significant period of time, order with same clientOrderId can be accepted by the system. It's Client's responsibility to control unique indication of clientOrderIds.

Order limitations
The system has a limit on the number of active (open) orders. By default, Client can have a maximum of 20 active taker orders. Once limit is reached, the system will reject any new orders with a reject reason “Too many active orders” until the total number of active orders is below the limit.
Important notice regarding Market orders
CEX.IO Spot Trading can partially execute market orders in order to prevent Client's possible loss. Market orders that were executed but not completely filled will have "CANCELED" status.
REQUEST

do_my_new_order

API Rate Limit Cost: 1

API Key Permission

This method requires “Trade” permission set for API Key.

New Order Request Parameters
Do My New Order - place Limit SELL order

Request (Client requests to place a Limit order to sell 0.01 BTC for USD at price 7,500)

{
  "e": "do_my_new_order",
  "oid": "1521711134776_1_do_my_new_order",
  "data": {
    "clientOrderId": "1521711134775",
    "accountId": "testAccount",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "timestamp": 1521711134775,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "amountCcy1": "0.01",
    "price": 7500,
    "comment": "v_overdraft_test"
  }
}
Response (CEX.IO Spot Trading sends acknowledgement message with a current status of order)

{
  "e": "do_my_new_order",
  "oid": "1521711134776_1_do_my_new_order",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "17062",
    "clientOrderId": "1521711134775",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998836_0_1",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "7500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Before order execution starts, requested amount is locked on Client’s account. After requested amount subtracted balance is 9.9893 BTC)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "BTC",
    "balance": "9.98930000",
    "onHoldBalance": "0.01000000",
    "timestamp": 1521708409281,
    "action": "order",
    "id": "17059"
  }
}
Response (CEX.IO Spot Trading sends Execution Report event for the new order. The first Execution Report contains initial state: executed amounts are both 0, no fee has been charged so far)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17062",
    "clientOrderId": "1521711134775",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998836_0_1",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "7500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. As a result of selling 0.1 BTC Client earned 170.63 USD and new balance is 9274.94197930 USD)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "USD",
    "balance": "9274.94197930",
    "onHoldBalance": "0.00000000",
    "timestamp": 1521711136458,
    "action": "order",
    "id": "17062"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification after fee was charged (0.60063 USD). Updated balance is 9274.34134930 USD)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "USD",
    "balance": "9274.34134930",
    "onHoldBalance": "00.00000000",
    "timestamp": 1521711136727,
    "action": "order",
    "id": "17062"
  }
}
Response (CEX.IO Spot Trading sends final execution report. It has status FILLED, executed amount in currency 1 is equal to requested amount in currency 1. Average price is greater than was requested for SELL order (therefore limit order was executed immediately). feeAmount field contains actual fee amount)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17062",
    "clientOrderId": "1521711134775",
    "accountId": "testAccount",
    "status": "FILLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.01000000",
    "executedAmountCcy2": "170.63000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "Trade",
    "executionId": "1521616998836_0_2",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "7500.00",
    "averagePrice": "17063.00",
    "lastQuantity": "0.01000000",
    "lastPrice": "17063.00",
    "lastAmountCcy1": "0.01000000",
    "lastAmountCcy2": "170.63000000",    
    "feeAmount": "0.60063000",
    "feeCurrency": "USD"
  }
}
Do My New Order - place Limit BUY order

Request (Client requests to place a Limit order to buy 0.01 BTC for USD at price 18,500)

{
  "e": "do_my_new_order",
  "oid": "1521713494191_1_do_my_new_order",
  "data": {
    "clientOrderId": "1521713494191",
    "accountId": "testAccount",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "timestamp": 1521713494191,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "amountCcy1": "0.01",
    "price": 18500,
    "comment": "v_overdraft_test"
  }
}
Response (CEX.IO Spot Trading sends acknowledgement message with a current status of order)

{
  "e": "do_my_new_order",
  "oid": "1521713494191_1_do_my_new_order",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "17065",
    "clientOrderId": "1521713494191",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998877_2_4",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Before order execution starts, CEX.IO Spot Trading calculates approximate amount of currency2 (USD) needed to buy requested amount of currency1 (BTC). This calculation uses current market data and expected fee. This approximate amount is then locked on Client’s account. After the amount was subtracted, the balance is 9161.57071930 USD)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "USD",
    "balance": "9161.57071930",
    "onHoldBalance": "185.46250000",
    "timestamp": 1521713494503,
    "action": "order",
    "id": "17065"
  }
}
Response (CEX.IO Spot Trading sends Execution Report for the new order. The first Execution Report contains initial state: executed amounts are both 0, no fee has been charged so far)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17065",
    "clientOrderId": "1521713494191",
    "accountId": "testAccount",
    "status": "NEW",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "New",
    "executionId": "1521616998877_2_4",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. As a result of buying BTC we have 0.01 BTC added to Client’s balance, and the result is 9.9693 BTC)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "BTC",
    "balance": "9.96930000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1521713495376,
    "action": "order",
    "id": "17065"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification after order has been executed. By now we know actual price and fee amounts. We’ve got a better deal than our previous approximation suggested. So, current balance is 9174.76767930 which is more than 9161.57071930 that we had after funds were initially locked for the order)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "testAccount",
    "currency": "USD",
    "balance": "9174.76767930",
    "onHoldBalance": "0.00000000",
    "timestamp": 1521713495615,
    "action": "order",
    "id": "17065"
  }
}
Response (CEX.IO Spot Trading sends final execution report. It has status FILLED, executed amount in currency 1 is equal to requested amount in currency 1. Average price is less than was requested for BUY order (therefore limit order was executed immediately). feeAmount field contains actual fee amount)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17065",
    "clientOrderId": "1521713494191",
    "accountId": "testAccount",
    "status": "FILLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.01000000",
    "executedAmountCcy2": "173.04000000",
    "requestedAmountCcy1": "0.01000000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "Trade",
    "executionId": "1521616998877_2_5",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": "17304.00",
    "lastQuantity": "0.01000000",
    "lastPrice": "17304.00",
    "lastAmountCcy1": "0.01000000",
    "lastAmountCcy2": "173.04000000",
    "feeAmount": "0.61304000",
    "feeCurrency": "USD"
  }
}
Do My New Order - place Market BUY order

Request (Client requests to place a Market order to buy 10 BTC for USD)

{
   "e": "do_my_new_order",
  "oid": "16141730009391_do_my_new_order",
  "data": {
     "accountId": "someAccount01",
     "clientOrderId": "manual_1614173000191",
     "currency1": "BTC",
     "currency2": "USD",
     "side": "BUY",
     "timestamp": 1614173000191,
     "orderType": "Market",
     "amountCcy1": 10
   }
}
Response (CEX.IO Spot Trading sends acknowledgement message with a status of order. The order has been rejected due to insufficient funds on Client’s account)

{
  "e": "do_my_new_order",
  "oid": "16141730009391_do_my_new_order",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "338306",
    "clientOrderId": "manual_1614173000191",
    "accountId": "someAccount01",
    "status": "REJECTED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "10.00000000",
    "requestedAmountCcy2": null,
    "orderType": "Market",
    "timeInForce": null,
    "comment": null,
    "executionType": "Rejected",
    "executionId": "1614012430993_103_295",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "averagePrice": null,
    "feeAmount": null,
    "feeCurrency": null,
    "orderRejectReason": "{\"code\":403,\"reason\":\"Insufficient funds\"}",
    "rejectCode": 403,
    "rejectReason": "Insufficient funds"
  }
}
Do My New Order - place Market BUY order

Request (Client requests to place a Market order to buy 10 BTC for USD)

{
   "e": "do_my_new_order",
  "oid": "16141730009391_do_my_new_order",
   "data": {
     "accountId": "someAccount01",
     "clientOrderId": "manual_1614173000191",
     "currency1": "BTC",
     "currency2": "USD",
     "side": "BUY",
     "timestamp": 1614173000191,
     "orderType": "Market",
     "amountCcy1": 10
   }
}
Response (CEX.IO Spot Trading sends acknowledgement message with a status of order. The order has been rejected due to the exceeded limit of active (open) orders)

{
  "e": "do_my_new_order",
  "oid": "16141730009391_do_my_new_order",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "orderId": "338306",
    "clientOrderId": "manual_1614173000191",
    "accountId": "someAccount01",
    "status": "REJECTED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "10.00000000",
    "requestedAmountCcy2": null,
    "orderType": "Market",
    "timeInForce": null,
    "comment": null,
    "executionType": "Rejected",
    "executionId": "1614012430993_103_295",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "averagePrice": null,
    "feeAmount": null,
    "feeCurrency": null,
    "orderRejectReason": "{\"code\":437,\"reason\":\"Too many active orders\"}",
    "rejectCode":437,
    "rejectReason":"Too many active orders"
  }
}
Do My New Order - Invalid request

Request (Client requests to place a limit order with missing price field)

{
  "e": "do_my_new_order",
  "oid": "1521736196696_1_do_my_new_order",
  "data": {
    "clientOrderId": "1521736196695",
    "accountId": "testAccount",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "timestamp": 1521736196695,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "amountCcy1": "0.001",
    "comment": "v_overdraft_test"
  }
}
Response (CEX.IO Spot Trading sends response that has no field "ok" and has "data.error" field containing error description)

{
  "e": "do_my_new_order",
  "oid": "1521736196696_1_do_my_new_order",
  "data": {
    "error": "Mandatory parameter price is missing"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_my_new_order" value is allowed here.
oid	Yes	String	Unique ID of this request.
clientOrderId	No	String	Order identifier assigned by Client. If this field is absent, it will be set automatically to current timestamp in milliseconds.
accountId	Yes	String	Client’s sub-account ID. Empty string value ("") is not allowed in this field.
currency1	Yes	String	Represents first currency in currency pair of this order.
currency2	Yes	String	Represents second currency in currency pair of this order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timestamp	Yes	Number	UTC timestamp in milliseconds, represents client-side order creation time. By default, timestamp should be within 30000 ms timeframe with server time, otherwise, order will be rejected. Please be informed that default timeframe value 30000 ms can be changed for the Client by request.
timeInForce	No	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders, where time in force is not applied, for example, for Market orders.
comment	No	String	Comment for order. Maximum length of comment string is 255 characters. If value is null, then it means Client did not provide such text during order creation.
amountCcy1	No	String (parseable as Float)	Represents order amount in currency1. This value can be null if order requests amount in currency2.
amountCcy2	No	String (parseable as Float)	Represents order amount in currency2. This value can be null if order requests amount in currency1.
price	No	String (parseable as Float)	Represents order price. Please omit this field for orders, where price cannot be requested, for example, Market orders or Stop orders.
expireTime	No	Number	UTC timestamp in milliseconds. If Expire Time is in the past, order will be rejected with the corresponding error.
stopPrice	No	String (parseable as Float)	Stop Price for Stop and StopLimit orders types.
New Order Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_my_new_order" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
clientId	Yes	String	Client CompId.
accountId	Yes	String	Client’s sub-account ID via which order has been created.
orderId	Yes	String	Order identifier assigned by CEX.IO Spot Trading. "NONE" value can be returned if order is rejected due to validation errors: failed minOrderAmountCcy, maxOrderAmountCcy, lotSizeCcy, max active orders checks.
clientOrderId	Yes	String	Order identifier assigned by Client.
status	Yes	String	Represents current execution status of this order.
currency1	Yes	String	Represents first currency in currency pair of the order.
currency2	Yes	String	Represents second currency in currency pair of the order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timeInForce	Yes	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders, where time in force is not applied, for example, for Market orders.
comment	Yes	String	Text value that was provided by Client during order creation. If value is null, it means Client did not provide such text during order creation.
orderRejectReason	No	String	Text field describing rejection reason. Often (but not always) it is a JSON representation of an object with two fields: "code" — numeric error code; "reason" — human readable error description. If value is null, that means there is no error description.
rejectCode	No	Number	Numeric error code.
rejectReason	No	String	Text field indicating human readable error description. If value is null, that means there is no error description.
executedAmountCcy1	Yes	String (which can be parsed as Float)	Represents executed amount in currency1. If this value is 0, then it means there is no executed amount (order has no executions).
executedAmountCcy2	Yes	String (which can be parsed as Float)	Represents executed amount in currency2. If this value is 0, then it means there is no executed amount (order has no executions).
requestedAmountCcy1	Yes	String (which can be parsed as Float)	Represents order amount in currency1, which was requested by Client. If this value is null, then it means there is no requested amount in currency1 (order should have then requested amount in currency2).
requestedAmountCcy2	Yes	String (which can be parsed as Float)	Represents order amount in currency2, which was requested by Client. If this value is null, then it means there is no requested amount in currency2 (order should have then requested amount in currency1).
feeAmount	Yes	String (which can be parsed as Float)	Represents order commission amount, which was charged for this order. If this value is 0, then it means there is no commission amount charged for this order so far.
feeCurrency	Yes	String	Represents order commission currency.
price	Yes	String (which can be parsed as Float)	Represents order price, which was provided by Client during order creation. If this value is null, then it means there is no requested price for this order. It happens for orders, where price cannot be requested, for example, Market orders or Stop orders.
averagePrice	Yes	String (which can be parsed as Float)	Represents average order execution price. If this value is null, then it means there is no executed amount (order has no executions).
expireTime	Yes	Number	UTC timestamp in milliseconds. Represents an expired timestamp provided by Client during creation of the order. If this value is null, then it means Client did not provide expire time during order creation.
effectiveTime	Yes	Number	UTC timestamp in milliseconds. Represents an effective timestamp provided by Client during creation of the order. If this value is null, then it means that Client did not provide effective time during order creation.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
New Order Event Notification
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message, only "executionReport" value is allowed here.
ok	Yes	String	"ok" value represents that event notification is successfully generated.
messageType	Yes	String	Describes the type of this message, only "executionReport" value is allowed here.
clientId	Yes	String	Client's CompId.
accountId	Yes	String	Client’s sub-account ID via which order has been created.
orderId	Yes	String	Order identifier assigned by CEX.IO Spot Trading.
clientOrderId	Yes	String	Order identifier assigned by Client.
status	Yes	String	Represents current execution status of this order.
currency1	Yes	String	Represents first currency in currency pair of the order.
currency2	Yes	String	Represents second currency in currency pair of the order.
side	Yes	String	Represents side of this order.
orderType	Yes	String	Represents order type of this order.
timeInForce	Yes	String	Represents time in force of this order. For details see "Order TimeInForce" section. This value can be null for orders, where time in force is not applied, for example, for Market orders.
comment	Yes	String	Text value that was provided by Client during order creation. If value is null, it means Client did not provide such text during order creation.
executionType	Yes	String	Describes the type of order execution event, due to which executionReport is being sent to Client. Allowed values are “PendingNew”, “New”, “Trade”, “PendingCancel” , “Canceled”, “Rejected”, “OrderStatus”.
orderRejectReason	No	String	Text field describing rejection reason. Often (but not always) it is a JSON representation of an object with two fields: "code" — numeric error code; "reason" — human readable error description. If value is null, that means there is no error description.
executedAmountCcy1	Yes	String (which can be parsed as Float)	Represents executed amount in currency1. If this value is 0, then it means there is no executed amount (order has no executions).
executedAmountCcy2	Yes	String (which can be parsed as Float)	Represents executed amount in currency2. If this value is 0, then it means there is no executed amount (order has no executions).
requestedAmountCcy1	Yes	String (which can be parsed as Float)	Represents order amount in currency1, which was requested by Client. If this value is null, then it means there is no requested amount in currency1 (order should have then requested amount in currency2).
requestedAmountCcy2	Yes	String (which can be parsed as Float)	Represents order amount in currency2, which was requested by Client. If this value is null, then it means there is no requested amount in currency2 (order should have then requested amount in currency1).
lastAmountCcy1	No	String (which can be parsed as Float)	Represents last trade executed amount in currency1. This field should be present if executionType is "Trade". This field should be missing if executionType is not "Trade".
lastAmountCcy2	No	String (which can be parsed as Float)	Represents last trade executed amount in currency2. This field should be present if executionType is "Trade". This field should be missing if executionType is not "Trade".
feeAmount	Yes	String (which can be parsed as Float)	Represents order commission amount, which was charged for this order. If this value is 0, then it means there is no commission amount charged for this order so far.
feeCurrency	Yes	String	Represents order commission currency.
price	Yes	String (which can be parsed as Float)	Represents order price, which was provided by Client during order creation. If this value is null, then it means there is no requested price for this order. It happens for orders, where price cannot be requested, for example, Market orders or Stop orders.
averagePrice	Yes	String (which can be parsed as Float)	Represents average order execution price. If this value is null, then it means there is no executed amount (order has no executions).
expireTime	Yes	Number	UTC timestamp in milliseconds. Represents an expired timestamp provided by Client during creation of the order. If this value is null, then it means Client did not provide expire time during order creation.
effectiveTime	Yes	Number	UTC timestamp in milliseconds. Represents an effective timestamp provided by Client during creation of the order. If this value is null, then it means that Client did not provide effective time during order creation.
Cancel Order
Client can cancel orders. Along with a response to this request, CEX.IO Spot Trading sends Account Event and Execution Report messages to Client if this request is successful. Also, if request to cancel an order is declined, CEX.IO Spot Trading sends Order Cancellation Rejection message.

REQUEST

do_cancel_my_order

API Rate Limit Cost: 1

API Key Permission

This method requires “Trade” permission set for API Key.

Cancel Order Request Parameters
Do Cancel My Order - successful cancellation of Limit SELL BTC order by clientOrderId

Request (Client requests to cancel order that was created with clientOrderId equal to "1521719532817")

{
  "e": "do_cancel_my_order",
  "oid": "1521719532817_2_do_cancel_my_order",
  "data": {
    "clientOrderId": "1521719532817",
    "cancelRequestId": "cancel_1521719532817",
    "timestamp": 1521719535310
  }
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming that the cancellation request is accepted)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532817_2_do_cancel_my_order",
  "ok": "ok",
  "data": {}
}
Response (CEX.IO Spot Trading sends Execution Report for order being cancelled. Now it’s in the state PENDING_CANCEL)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17066",
    "clientOrderId": "cancel_1521719532817",
    "OrigClOrdID": "1521719532817",
    "accountId": null,
    "status": "PENDING_CANCEL",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00010000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "PendingCancel",
    "executionId": "1521616998877_2_7",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Funds that were previously locked for the order are now returned to the account’s balance)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "",
    "currency": "BTC",
    "balance": "9.96930000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1521719535842,
    "action": "order",
    "id": "17066"
  }
}
Response (CEX.IO Spot Trading sends final execution report. It specifies final order status CANCELLED, executed amounts are 0, fee has not been charged)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "17066",
    "clientOrderId": "cancel_1521719532817",
    "OrigClOrdID": "1521719532817",
    "accountId": null,
    "status": "CANCELLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00010000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "v_overdraft_test",
    "executionType": "Canceled",
    "executionId": "1521616998877_2_8",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "18500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Do Cancel My Order - successful cancellation of Limit BUY BTC order by orderId

Request (Client requests to cancel order, to which CEX.IO Spot Trading assigned orderId equal to 123456789)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532818_2_do_cancel_my_order",
  "data": {
    "orderId": 123456789,
    "cancelRequestId": "cancel_1521719532818",
    "timestamp": 1521719535311
  }
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming that the cancellation request is accepted)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532818_2_do_cancel_my_order",
  "ok": "ok",
  "data": {}
}
Response (CEX.IO Spot Trading sends Execution Report for order being cancelled. Now it’s in the state PENDING_CANCEL)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "123456789",
    "clientOrderId": "cancel_1521719532818",
    "OrigClOrdID": "1521719532818",
    "accountId": null,
    "status": "PENDING_CANCEL",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00010000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel_order_test",
    "executionType": "PendingCancel",
    "executionId": "1521616998878_2_7",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "12500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Funds that were previously locked for the order are now returned to the account’s balance)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "",
    "currency": "USD",
    "balance": "13459.85",
    "onHoldBalance": "0.00000000",
    "timestamp": 1521719535843,
    "action": "order",
    "id": "123456789"
  }
}
Response (CEX.IO Spot Trading sends final execution report. It specifies final order status CANCELLED, executed amounts are 0, fee has not been charged)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "123456789",
    "clientOrderId": "cancel_1521719532818",
    "OrigClOrdID": "1521719532818",
    "accountId": null,
    "status": "CANCELLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "BUY",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00010000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel_order_test",
    "executionType": "Canceled",
    "executionId": "1521616998879_2_8",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "12500.00",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Do Cancel My Order - incorrect request with missing "orderId" and "clientOrderId" parameters

Request (Client requests to cancel order but doesn't indicate either "orderId" or "clientOrderId" parameters)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532835_do_cancel_my_order",
  "data": {
    "cancelRequestId": "cancel_1521719532834",
    "timestamp": 1521719535322
  }
}
Response (CEX.IO Spot Trading responds that either "clientOrderId" or "orderId" should be specified)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532836_do_cancel_my_order",
  "data": {
    "error": "ClientOrderId or orderId should be specified"
  }
}
Do Cancel My Order - incorrect request with both "orderId" and "clientOrderId" parameters

Request (Client requests to cancel order but indicates both "orderId" and "clientOrderId" parameters)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532836_do_cancel_my_order",
  "data": {
    "clientOrderId": "1521719532817",
    "orderId": 123456789,
    "cancelRequestId": "cancel_1521719532899",
    "timestamp": 1521719535349
  }
}
Response (CEX.IO Spot Trading responds that either "clientOrderId" or "orderId" should be specified - not both of them)

{
  "e": "do_cancel_my_order",
  "oid": "1521719532836_do_cancel_my_order",
  "data": {
    "error": "Only one of the fields ClientOrderId or orderId should be specified, not both"
  }
}
Do Cancel My Order - invalid cancellation request

Request (Client requests to cancel order with clientOrderId equal to "omg_not_an_order_order" (that has never been created))

{
  "e": "do_cancel_my_order",
  "oid": "1521723623618_1_do_cancel_my_order",
  "data": {
    "clientOrderId": "omg_not_an_order_order",
    "cancelRequestId": "cancel_omgorder",
    "timestamp": 1521723623618
  }
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming that the cancellation request is accepted)

{
  "e": "do_cancel_my_order",
  "oid": "1521723623618_1_do_cancel_my_order",
  "ok": "ok",
  "data": {}
}
Response (CEX.IO Spot Trading sends orderCancelReject with reason "unknown_order")

{
  "e": "orderCancelReject",
  "ok": "ok",
  "data": {
    "messageType": "orderCancelReject",
    "clientId": "IT_DEMO",
    "orderId": "NONE",
    "cancelRequestId": "cancel_omgorder",
    "clientOrderId": "omg_not_an_order_order",
    "accountId": null,
    "orderStatus": "REJECTED",
    "responseTo": "order_cancel_request",
    "cancelRejectReason": "unknown_order"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_cancel_my_order" value is allowed here.
oid	Yes	String	Unique ID of this request.
orderId	No	Number	Order identifier assigned by CEX.IO Spot Trading. If this field is present and contains valid value, then it means Client wants to cancel specific order with orderId, which was assigned by CEX.IO Spot Trading. If "orderId" field is present, then "clientOrderId" should be absent. Either "orderId" or "clientOrderId" should be indicated in request anyway.
clientOrderId	No	String	Order identifier assigned by Client when the order was created. If this field is present and contains valid value, then it means Client wants to cancel specific order with clientOrderId indicated by Client at order placement. If "clientOrderId" field is present, then "orderId" field should be absent. Either "clientOrderId" or "orderId" should be indicated in request anyway.
cancelRequestId	Yes	String	Cancel request identifier assigned by Client.
timestamp	Yes	Number	Current client time - UTC timestamp in milliseconds.
Cancel Order Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_cancel_my_order" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Order Cancellation Rejection event
If request to cancel an order is declined, CEX.IO Spot Trading sends Order Cancellation Rejection message.

Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "orderCancelReject" value is allowed here.
ok	Yes	String	Represents that event notification is successfully generated. Only "ok" value is allowed here.
messageType	Yes	String	Describes the type of this message. Only "orderCancelReject" value is allowed here.
clientId	Yes	String	Client's CompId.
accountId	No	String	If order referenced by clientOrderId field in cancellation request was found, this field contains client’s sub-account ID, that was specified when the order was created. If order was not found, this field will not be included.
orderId	Yes	String	If order referenced by clientOrderId field in cancellation request was found, this field contains order identifier assigned by CEX.IO Spot Trading. If order was not found, this field will contain string "NONE".
clientOrderId	Yes	String	Order identifier specified in cancellation request which should have matched with corresponding field of an existing order.
orderStatus	Yes	String	Represents current execution status of this order. If order was not found, it contains value "REJECTED".
responseTo	Yes	String	The type of request that caused sending this notification.
cancelRejectReason	No	String	Textual description of reason for rejection.
Cancel All Orders
Client can cancel all open orders via WebSocket API. Along with a response to this request CEX.IO Spot Trading will start cancellation process for all open orders and send corresponding Account Event and Execution Report messages to the Client.

REQUEST

do_cancel_all_orders

API Rate Limit Cost: 5

API Key Permission

This method requires “Trade” permission set for API Key.

Cancel All Orders Request Parameters
Do Cancel All Orders

Request (Client requests to cancel all opened orders)

{
  "e": "do_cancel_all_orders",
  "oid": "1521711134776_1_do_cancel_all_orders",
  "data": {}
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming the list of Client’s opened orders which system is trying to cancel. There are 2 open orders in this case)

{
  "e": "do_cancel_all_orders",
  "oid": "1575459976724_1_do_cancel_all_orders",
  "ok": "ok",
  "data": {
    "clientOrderIds": ["1575459943138","1575459942041"]
  }
}
Response (CEX.IO Spot Trading sends Execution Report for the first order being cancelled. Now it’s in the state PENDING_CANCEL)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "2284074",
    "clientOrderId": "CANCEL_IT_DEMO_2284074",
    "OrigClOrdID": "1575459943138",
    "accountId": null,
    "status": "PENDING_CANCEL",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00100000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel all orders test",
    "executionType": "PendingCancel",
    "executionId": "1574407721714_101_19759",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "12000.0",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Execution Report for the second order being cancelled. Now it’s in the state PENDING_CANCEL)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "2284073",
    "clientOrderId": "CANCEL_IT_DEMO_2284073",
    "OrigClOrdID": "1575459942041",
    "accountId": null,
    "status": "PENDING_CANCEL",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00100000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel all orders test",
    "executionType": "PendingCancel",
    "executionId": "1574407716536_102_19009",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime":null,
    "price": "12000.0",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Funds that were previously locked for the first order are now returned to the account’s balance)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "",
    "currency": "BTC",
    "balance": "0.16922000",
    "onHoldBalance": "0.00100000",
    "timestamp": 1575459977538,
    "action": "order",
    "id": "2284074"
  }
}
Response (CEX.IO Spot Trading sends final execution report for the first order. It specifies final order status CANCELLED, executed amounts are 0, fee hasn't been charged)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "2284074",
    "clientOrderId": "CANCEL_IT_DEMO_2284074",
    "OrigClOrdID": "1575459943138",
    "accountId": null,
    "status": "CANCELLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00100000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel all orders test",
    "executionType": "Canceled",
    "executionId": "1574407721714_101_19761",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "12000.0",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification. Funds that were previously locked for the second order are now returned to the account’s balance)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "IT_DEMO",
    "accountId": "",
    "currency": "BTC",
    "balance": "0.17022000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1575459977542,
    "action": "order",
    "id": "2284073"
  }
}
Response (CEX.IO Spot Trading sends final execution report for the second order. It specifies final order status CANCELLED, executed amounts are 0, fee hasn't been charged)

{
  "e": "executionReport",
  "ok": "ok",
  "data": {
    "messageType": "executionReport",
    "clientId": "IT_DEMO",
    "orderId": "2284073",
    "clientOrderId": "CANCEL_IT_DEMO_2284073",
    "OrigClOrdID": "1575459942041",
    "accountId": null,
    "status": "CANCELLED",
    "currency1": "BTC",
    "currency2": "USD",
    "side": "SELL",
    "executedAmountCcy1": "0.00000000",
    "executedAmountCcy2": "0.00000000",
    "requestedAmountCcy1": "0.00100000",
    "requestedAmountCcy2": null,
    "orderType": "Limit",
    "timeInForce": "GTC",
    "comment": "cancel all orders test",
    "executionType": "Canceled",
    "executionId": "1574407716536_102_19010",
    "transactTime": null,
    "expireTime": null,
    "effectiveTime": null,
    "price": "12000.0",
    "averagePrice": null,
    "feeAmount": "0.00000000",
    "feeCurrency": "USD"
  }
}
Do Cancel All Orders - There are no Client’s open orders

Request (Client requests to cancel all opened orders)

{
  "e": "do_cancel_all_orders",
  "oid": "1521711134776_1_do_cancel_all_orders",
  "data": {}
}
Response (CEX.IO Spot Trading sends acknowledgement message confirming there are no Client’s open orders)

{
  "e": "do_cancel_all_orders",
  "oid": "1575459976724_1_do_cancel_all_orders",
  "ok": "ok",
  "data": {
    "clientOrderIds": []
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_cancel_all_orders" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. If it is an empty object ("{}"), then it means client wants to cancell all open orders on all Spot Trading sub-accounts and Wallet account.
accountIds	No	Array	List of account identifiers on which Client wants to cancel all open orders. Empty string ("") value in this array represents Client’s Wallet account. Each account identifier should be of string type, e.g. ["subAccount1", "", "account123", "hallo"]. If this field is missing or if it contains an empty array ([]), then it means Client wants to cancel all open orders on all Spot Trading sub-accounts and Wallet account.
Cancel All Orders Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_cancel_all_orders" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
clientOrderIds	Yes	Array	This object contains list of client’s open orders, which Spot Trading system is trying to cancel on all accounts or specific accounts (if Client indicated specific accounts in accountIds field of the request). It might be an empty array ([]). If this array is empty, then it means there are no client’s open orders which satisfy requested criteria.
Order Book
This method allows Client to receive current order book snapshot for specific trading pair.

REQUEST

get_order_book

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Order Book Request Parameters
Get Order Book request for one trading pair.

Request (Client sends request to receive order book snapshot for BTC-USD trading pair)

{
  "e": "get_order_book",
  "oid": "152171113_get_order_book",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request with current order book snapshot for BTC-USD trading pair)

{
  "e": "get_order_book",
  "oid": "152171113_get_order_book",
  "ok": "ok",
  "data": {
    "timestamp": 1676037221433,
    "currency1": "BTC",
    "currency2": "USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_order_book" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to request an Order Book snapshot. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_order_book" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
timestamp	Yes	Number	Current client time - UTC timestamp in milliseconds.
currency1	Yes	String	The first currency in the requested trading pair.
currency2	Yes	String	The second currency in the requested trading pair.
bids	Yes	Array	This array contains a list of bids of the order book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book.
asks	Yes	Array	This array contains a list of asks of the Order Book. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Order Book Subscribe
Client by subscribing via WebSocket can subscribe to order book feed upon requested trading pair.

In response to Order Book Subscribe request Client will receive current (initial) order book snapshot for requested pair with indicated seqId number.

To track following updates to Order Book Client needs to subscribe via WebSocket to “order_book_increment“ messages, which would contain trading pair name, seqId number, Bids and Asks price levels deltas.

REQUEST

order_book_subscribe

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Order Book Subscribe Request Parameters
Order Book Subscribe request

Request (Client sends BTC-USD order book subscription request)

{
  "e": "order_book_subscribe",
  "oid": "16147857398591_order_book_subscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "order_book_subscribe",
  "oid": "16147857398591_order_book_subscribe",
  "ok": "ok",
  "data": {
    "seqId": 1680908,
    "pair": "BTC-USD",
    "bids": [
      [
        "21770.5",
        "0.00990261"
      ],
      [
        "21755.9",
        "0.05648272"
      ],
      [
        "21752.2",
        "25.91719331"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "26.98043900"
      ],
      [
        "21841.0",
        "8.51054857"
      ],
      [
        "21842.0",
        "2.49919136"
      ]
    ]
  }
}
Order Book Increment (CEX.IO Spot Trading sends BTC-USD order book increment)

{ 
  "e": "order_book_increment",
  "ok": "ok",
  "data": {
    "seqId": 1680909,
    "pair": "BTC-USD",
    "bids": [
      [
        "21770.5",
        "0.00000000"
      ],
      [
        "21755.9",
        "0.00000272"
      ],
      [
        "21753.4",
        "1.12345678"
      ]
    ],
    "asks": [
      [
        "21840.9",
        "2.89000000"
      ],
      [
        "21841.0",
        "0.00000000"
      ],
      [
        "21842.0",
        "7.54419136"
      ],
      [
        "21841.4",
        "0.01000000"
      ],
      [
        "21839.5",
        "0.55000000"
      ]
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_subscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to subscribe for receiving Order Book snapshot and updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Subscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_subscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
seqId	Yes	Number	Unique ID of the Order Book snapshot message. The value returned in this field is an initial seqId for order book feed. Further Order Book Increment seqId value should be incremented from value returned in this field.
pair	Yes	String	Trading pair, for which Order Book snapshot is returned.
bids	Yes	Array	This array contains a list of bids of the order book snapshot. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no bids are available in the Order Book snapshot.
asks	Yes	Array	This array contains a list of asks of the order book snapshot. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates amount of the Order Book entry. The value in this field can be an empty array in case of no asks are available in the Order Book snapshot.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Order Book Increment Messages
In case of successful subscription server will send order_book_subscribe response, which contains full order book at that moment.

Following messages are “order_book_increment“ messages, which should be applied to the initial Order Book snapshot incrementally on the Client’s side to keep Order Book snapshot up to date. Each Order Book Increment item should be applied to existing snapshot at specific price level.

All Order Book messages have parameter seqId. Received snapshot of trading pair order book contains seqId number which should be considered by Client as initial seqId number for order book feed. SeqId increments on each further order_book_increment message.

If a Client subscribes to multiple order books for different trade pairs, Client should track the pair name and seqId number in each new Order Book Increment message received in order to correctly add increments to the corresponding Order Book Snapshot for that trade pair.

If one or a few Order Book update messages were not received by the Client, it is required to re-subscribe to Order Book for receiving a new actual snapshot in order to keep Order book up to date.

If Client receives message with seqId number which is lower than previous seqIds received in the subscribed feed - Client is required to re-subscribe to Order Book for receiving a new actual snapshot in order to keep Order book up to date. Such situation happens when CEX.IO Spot Trading’s internal system is restarted and Order Book subscription is automatically re-subscribed for the Client.

Order Book Increment Message Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_increment" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
seqId	Yes	Number	Unique ID of the Order Book update message. First Order Book increment should contain the value in this field equal to Order Book snapshot seqId incremented by 1. The value of this field in further Order Book increment messages should equal to previous Order Book increment seqId incremented by 1.
pair	Yes	String	Trading pair, for which Order Book update is returned.
bids	Yes	Array	This array contains a list of bids deltas - price levels of the Order Book entries. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates updated amount of the Order Book entry. The value in this field can be an empty array in case Order Book bids were not changed since previous Order Book update message.
asks	Yes	Array	This array contains a list of asks deltas - price levels of the Order Book entries. The first value of an array element indicates price level of the Order Book entry, the second value of an array element indicates updated amount of the Order Book entry. The value in this field can be an empty array in case Order Book asks were not changed since previous Order Book update message.
Order Book Unsubscribe
It's highly recommended to unsubscribe from order book when it is no longer needed.

REQUEST

order_book_unsubscribe

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Order Book Unsubscribe Request Parameters
Order Book Unsubscribe request

Request (Client sends BTC-USD order book unsubscribe request)

{
  "e": "order_book_unsubscribe",
  "oid": "16147857488591_order_book_unsubscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "order_book_unsubscribe",
  "oid": "16147857488591_order_book_unsubscribe",
  "ok": "ok",
  "data": {
    "pair": "BTC-USD"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to unsubscribe from receiving Order Book updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Order Book Unsubscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "order_book_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
pair	Yes	String	Indicates trading pair, for which Client would be unsubscribed from receiving further Order Book updates.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Candles
By using Candles method Client can receive historical OHLCV candles of different resolutions and data types.

Client can indicate additional timeframe and limit filters to make response more precise to Client’s requirements.

REQUEST

get_candles

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Candles Request Parameters
Get Candles request

Request (Client sends request to receive 1 bestAsk open candles for BTC-USD trading pair as of current time)

{
  "e": "get_candles",
  "oid": "16760394893891_get_candles",
  "ok": "ok",
  "data": {
    "pair": "BTC-USD",
    "fromISO": 1675953089378,
    "limit": 1,
    "dataType": "bestAsk",
    "resolution": "1h"
  }
} 
Response (CEX.IO Spot Trading successfully responds to the request, 1 closed 1h candle)

{
  "e": "get_candles",
  "oid": "16760394893891_get_candles",
  "ok": "ok",
  "data": [
    {
      "timestamp": 1675951200000,
      "open": 22945.3,
      "high": 23163.4,
      "low": 22913,
      "close": 22920.1,
      "volume": 779.00675644,
      "resolution": "1h",
      "isClosed": true,
      "timestampISO": "2023-02-09T14:00:00.000Z"
    }
  ]
}
Request (Client sends request to receive 1 bestBid open candles for 3 pairs as of current time)

{
  "e": "get_candles",
  "oid": "1676041279412_get_candles",
  "data": {
    "pairsList": ["BTC-USD","ETH-USD","XXX-YYY"],
    "toISO": 1676041279412,
    "limit": 1,
    "dataType": "bestBid",
    "resolution": "1h"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request, pairs with 1 open candle for each + unsupported pair message)

{ 
  "e": "get_candles",
  "oid": "1676041279412_get_candles",
  "ok": "ok",
  "data": {
    "BTC-USD": [
      {
        "timestamp": 1676041200000,
        "high": 21791.3,
        "low": 21772.4,
        "close": 21782.6,
        "open": 21791.3,
        "volume": 36,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z"
      }
    ],
    "ETH-USD": [
      {
        "timestamp": 1676041200000,
        "high": 1545.21,
        "low": 1543.65,
        "close": 1544.95,
        "open": 1545.21,
        "volume": 34,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z"
      }
    ],
    "XXX-YYY": {
      "error": {
        "code": 400,
        "reason": "Unsupported pair XXX-YYY"
      }
    }
    "BTC-USD": [
      {
        "timestamp": 1676041200000,
        "high": 21791.3,
        "low": 21772.4,
        "close": 21782.6,
        "open": 21791.3,
        "volume": 36.87654321,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z"
      }
    ],
    "ETH-USD": [
      {
        "timestamp": 1676041200000,
        "high": 1545.21,
        "low": 1543.65,
        "close": 1544.95,
        "open": 1545.21,
        "volume": 34.12345678,
        "resolution": "1h",
        "timestampISO": "2023-02-10T15:00:00.000Z"
      }
    ],
    "XXX-YYY": {
      "error": {
        "code": 400,
        "reason": "Unsupported pair XXX-YYY"
      }
    }
  }
}
Request (Client sends request to receive last 1 hour bestAsk candle for LUNC-BUSD pair)

{
  "e": "get_candles",
  "oid": "16760424783851_get_candles",
  "data": {
    "pair": "LUNC-BUSD",
    "toISO": 1676042478383,
    "limit": 1,
    "dataType": "bestAsk",
    "resolution": "1h"
  }
}
Response (CEX.IO Spot Trading responds with empty candle, which means no candle is available upon requested parameters)

{
  "e": "get_candles",
  "oid": "16760424783851_get_candles",
  "ok": "ok",
  "data": [
    {
      "timestamp": 1676041200000,
      "resolution": "1h",
      "timestampISO": "2023-02-10T15:00:00.000Z"
    }
  ]
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_candles" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	No	String	Trading pair, for which Client wants to receive historical OHLCV candles. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles for one specific trading pair. If "pair" field is present, then "pairsList" field should be absent. Either "pair" or "pairsList" should be indicated in the request anyway.
pairsList	No	Array or String	Array with trading pairs, for which Client wants to receive last historical OHLCV candles. At least 1 trading pair should be indicated in this field. If this field is present and contains valid values, then it means Client wants to receive last OHLCV candle for each indicated trading pair in the list. If "pairsList" field is present, then "pair" field should be absent. Either "pairsList" or "pair" should be indicated in the request anyway.
fromISO	No	Number (UTC timestamp)	The starting moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the first one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
toISO	No	Number (UTC timestamp)	The last moment of time of the requested period for which OHLCV candles should be returned - UTC timestamp in milliseconds. If this field is present and contains valid value, then it means Client wants to receive OHLCV candles, the last one of which includes indicated moment of time. Either "fromISO" or "toISO" should be indicated in the request anyway.
limit	No	Number (Integer)	Maximum number of OHLCV candles to be returned in response. Indicated number should be greater than zero. This field is mandatory if at least one of “fromISO” or “toISO” fields is specified in request. This field should be absent if both “fromISO” and “toISO” are specified in request. If “pairsList” field is specified in the request, then the value of this field should equal 1 (only last candle for each requested trading pair will be returned in response).
dataType	Yes	String	The type of data, on the basis of which returned OHLC prices in candles should be calculated. Allowed values: “bestAsk”, “bestBid”.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
Candles Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_candles" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
timestamp	Yes	Number	OHLCV candle timestamp - UTC timestamp in milliseconds.
open	No	Number (Float)	Opening price of OHLCV candle in quote currency.
high	No	Number (Float)	Highest price of OHLCV candle in quote currency, which was reached during candle timeframe.
low	No	Number (Float)	Lowest price of OHLCV candle in quote currency, which was reached during candle timeframe.
close	No	Number (Float)	Closing price of OHLCV candle in quote currency.
volume	No	Number (Float)	Total base currency amount traded during a specific candle timeframe period.
resolution	Yes	String	Timeframe from which OHLCV candles data should be calculated. Allowed values: “1m”, “5m”, “15m”, “30m”, "1h", “2h”, “4h”, “1d”.
isClosed	No	Boolean (true)	Indicates whether the specific candle is currently closed. If the value of this field is true, then it means this candle has been already closed. If this field is absent, then it means this candle is still open.
timestampISO	Yes	String	OHLCV candle date & time in ISO format (“YYYY-MM-DDTHH:mm:ss.SSSZ").
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade History
This method allows Client to obtain historical data as to occurred trades upon requested trading pair.

Client can supplement Trade History request with additional filter parameters, such as timeframe period, tradeIds range, side etc. to receive trades which match request parameters.

REQUEST

get_trade_history

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Trade History Request Parameters
Get Trade History Request

Request (Client sends request to receive trade history for BTC-USD trading pair)

{
  "e": "get_trade_history",
  "oid": "16760424783866_get_trade_history",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "get_trade_history",
  "oid": "16760424783866_get_trade_history",
  "ok": "ok",
  "data": {
    "pageSize": 100,
    "trades": [
      {
        "tradeId": "1675399566795-0",
        "dateISO": "2023-02-03T04:46:06.795Z",
        "side": "SELL",
        "price": "21149.2",
        "amount": "10.00000000"
      },
      {
        "tradeId": "1675401193999-0",
        "dateISO": "2023-02-03T05:13:13.999Z",
        "side": "BUY",
        "price": "25896.0",
        "amount": "0.00000001"
      },
      {
        "tradeId": "1675401207800-0",
        "dateISO": "2023-02-03T05:13:27.800Z",
        "side": "SELL",
        "price": "21146.0",
        "amount": "0.00000001"
      }
    ]
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_trade_history" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to receive trades history. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
side	No	String	Side of requested trades. If this field is present, it should contain only one of allowed values: “BUY” or “SELL”. If this field is not indicated in the request, then response would contain trades for "BUY" and "SELL" sides.
fromDateISO	No	String	The starting moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If “fromDateISO” and “pageSize” parameters are not specified in request, then by default last 1000 trades will be returned in response. If this field is present, then “fromTradeId” and “toTradeId” fields should not be indicated in the request.
toDateISO	No	String	The last moment of time of the requested period in ISO format (YYYY-MM-DDTHH:mm:ss.SSSZ) for which trades are requested. If this field is present, then “fromDateISO” should also be present, “fromTradeId” and “toTradeId” fields should be absent.
fromTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, starting from which subsequent trades should be returned in response. If this field is present, then “fromDateISO” and “toDateISO” fields should not be indicated in the request.
toTradeId	No	String	Unique trade identifier (tradeId) in CEX.IO Spot Trading system, which should be the last trade returned in response. If this field is present, then “fromTradeId” should also be present, “fromDateISO” and “toDateISO” fields should not be indicated in the request.
pageSize	No	Number (Integer)	Maximum number of trades, which should be returned in response. If this field is present then the value should be more than zero and not more than 1000. If indicated value is more than 1000, the response will still contain only up to 1000 trades max. If this field is not specified in request, then by default 100 trades would be returned in response.
Trade History Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_trade_history" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
pageSize	Yes	Number (Integer)	Maximum number of trades, which can be returned in response.
trades	Yes	Array	An array containing data as to each trade event which satisfies requested criteria. If request is successful, this field should be present in response. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted by “dateISO” value in ascending order (from older to newer, considering “fromDateISO” / “toDateISO” or “fromTradeId” / “toTradeId” if indicated in request). If a few trade events occurred at the same moment of time, then such trade events are sorted additionally bt “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	Represents an object which describes specific trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade Subscribe
By using the Trade Subscribe method Client can subscribe via WebSocket to live feed of trade events which occur on requested trading pair.

In response to Trade Subscribe request Client will receive a unique identifier of trade subscription which should further be used for unsubscription when trade subscription is no longer needed for Client.

Client should subscribe via WebSocket to “tradeHistorySnapshot” and “tradeUpdate” messages to receive initial and periodical Trade History snapshots, and live trade events for requested trading pair.

REQUEST

trade_subscribe

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Trade Subscribe Request Parameters
Trade Subscribe request

Request (Client sends trade subscribe request)

{
  "e": "trade_subscribe",
  "oid": "72955210375_trade_subscribe",
  "data": {
    "pair": "BTC-USD"
  }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "trade_subscribe",
  "oid": "72955210375_trade_subscribe",
  "ok": "ok",
  "data": {
    "reqId":"1678176120060_1"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_subscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
pair	Yes	String	Trading pair, for which Client wants to subscribe for receiving trade event updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Trade Subscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_subscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
reqId	Yes	String	Identifier of WebSocket connection in which trade subscription feed is created.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Trade History Snapshot
Right after the User initiates a new Trade Subscription, they'll get a tradeHistorySnapshot containing last 200 trade events upon requested pair. Then, the server will start sending a stream (series) of tradeUpdate events.

However, tradeUpdate updates can be received before tradeHistorySnapshot. Additionally, some tradeUpdate messages received after tradeHistorySnapshot may partially repeat trades already received from the snapshot.

Also, TradeHistorySnapshot events in some cases can arrive during a session while regular tradeUpdate events are being received. To handle this case, the Client should store the tradeId of the last trade processed and ignore all trades with a tradeId that is equal to or less than the stored tradeId value, whether they come from a snapshot or update.

Trade History Snapshot message

{
  "e": "tradeHistorySnapshot",
  "ok": "ok",
  "data": { 
    "pair": "BTC-USD",
    "trades": [
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:22:25.734Z",
        "price": "22562.1",
        "amount": "0.00975172",
        "tradeId": "1678152145734-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:22:53.141Z",
        "price": "22566.6",
        "amount": "0.00975075",
        "tradeId": "1678152173141-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:23:10.109Z",
        "price": "22571.1",
        "amount": "0.00974977",
        "tradeId": "1678152190109-0"
      },
      {
        "side": "BUY",
        "dateISO": "2023-03-07T01:23:33.461Z",
        "price": "22586.3",
        "amount": "0.05557372",
        "tradeId": "1678152213461-0"
      }
    ]
  }
}
Trade History Snapshot Message Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "tradeHistorySnapshot" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
pair	Yes	String	Trading pair, for which trades history snapshot is returned in response.
trades	Yes	Array	An array containing data as to last 200 trade events which satisfies requested criteria. It might be an empty array ([]). If this array is empty, then it means there are no trades, which satisfy Client’s request criteria. If there are trades, which satisfy requested criteria, then the elements in array are sorted in ascending order. If a few trade events occurred at the same moment of time, then such trade events are sorted additionally bt “tradeId” value from lowest to higher sequence number (e.g. first “1677696747571-0”, then “1677696747571-1” etc.)
trades.X	No	Object	Represents an object which describes specific trade event details.
trades.X.side	Yes	String	Side of trade event.
trades.X.dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
trades.X.price	Yes	String (parseable as float)	Trade execution price.
trades.X.amount	Yes	String (parseable as float)	Amount of trade.
trades.X.tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”). If several trades occurred at the same moment of time, then they differ from each other by incremented sequence number, starting from 0 (e.g. “1677696747571-0”, “1677696747571-1”, “1677696747571-2” etc.).
Trade Update Message Parameters
Trade Update message

{
  "e": "tradeUpdate",
  "ok": "ok",
  "data": { 
    "pair": "BTC-USD",
    "side": "BUY",
    "dateISO": "2023-03-07T08:04:16.117Z",
    "price": "22615.3",
    "amount": "0.01000000",
    "tradeId": "1678176256117-0" 
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "tradeUpdate" value is allowed here.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains message details.
pair	Yes	String	The trading pair on which the trade event occurred.
side	Yes	String	Side of trade event.
dateISO	Yes	String	Date & Time of trade event in ISO format. (YYYY-MM-DDTHH:mm:ss.SSSZ).
price	Yes	String (parseable as float)	Trade execution price.
amount	Yes	String (parseable as float)	Amount of trade.
tradeId	Yes	String	Unique trade identifier in CEX.IO Spot Trading system. The value in this field should consist of trade UTC timestamp in milliseconds and sequence number separated by ”-” symbol (e.g. “1677696747571-0”, “1677696747988-2”, etc.).
Trade Unsubscribe
It's highly recommended to unsubscribe from existing trade subscription when it is no longer needed for Client.

REQUEST

trade_unsubscribe

API Rate Limit Cost: 1

API Key Permission

This method requires "Read" permission set for API Key.

Trade Unsubscribe Request Parameters
Request

{
 "e": "trade_unsubscribe",
  "oid": "16781762553800_trade_unsubscribe",
  "data": {
    "pair": "BTC-USD"
 }
}
Response (CEX.IO Spot Trading successfully responds to the request)

{
  "e": "trade_unsubscribe",
  "oid": "16781762553800_trade_unsubscribe",
  "ok": "ok",
  "data": {
    "reqId": "1678176120060_1"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
data.pair	Yes	String	Trading pair, for which Client wants to unsubscribe from receiving trade event updates. Trading pair should contain two currencies in uppercase divided by “-“ symbol. Pair should be listed in traditional direction. For example “BTC-USD”, but not “USD-BTC”.
Trades Unsubscribe Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "trade_unsubscribe" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
reqId	Yes	String	Identifier of WebSocket connection in which trade subscription feed is removed.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Transaction History
This request allows Client to find out his financial transactions (deposits, withdrawals, internal transfers, commissions or trades).

REQUEST

get_my_transaction_history

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Transaction History Request Parameters
Get My Transaction History - For Main Account with specified period

Request (Client sends request to find transactions of all types for the main account with specified period and sort the results in ascending order)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "accountId": "",
    "type": "",
    "dateFrom": 1613101662720,
    "dateTo": 1614336230587,
    "sortOrder": "ASC"
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "ok": "ok",
  "data": [
    {
      "transactionId": "trade_335805_finalization_BTC",
      "timestamp": "2021-02-12T09:44:35.078Z",
      "accountId": "",
      "type": "trade",
      "amount": "0.00200000",
      "details": "Finalization Trade orderId=\'335805\' for DEMO_USER",
      "currency": "BTC"
    },
    {
      "transactionId": "trade_335805_finalization_USD",
      "timestamp": "2021-02-12T09:44:35.078Z",
      "accountId": "",
      "type": "trade",
      "amount": "-33.40944038",
      "details": "Finalization Trade orderId=\'335805\' for DEMO_USER",
      "currency": "USD"
    },
    {
      "transactionId": "commission_trade_335805",
      "timestamp": "2021-02-12T09:44:35.090Z",
      "accountId": "",
      "type": "commission",
      "amount": "-0.16704721",
      "details": "Commission for orderId=\'335805\' for DEMO_USER",
      "currency": "USD"
    }
  ]
}
Get My Transaction History - For Main Account with Paging

Request (Client sends request to find transactions of all types for the main account and wants to see the second page expecting the result set is chunked to pages size 3 (not more than 3 transactions per page))

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "accountId": "",
    "type": "",
    "pageSize": 3,
    "pageNumber": 2,
    "sortOrder": "DESC"
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "ok": "ok",
  "data": [
    {
      "transactionId": "commission_trade_338348",
      "timestamp": "2021-02-24T16:36:23.271Z",
      "accountId":"",
      "type": "commission",
      "amount": "-1242.90844594",
      "details": "Commission for orderId=\'338348\' for DEMO_USER",
      "currency": "USD"
    },
    {
      "transactionId": "trade_338348_finalization_BTC",
      "timestamp": "2021-02-24T16:36:23.259Z",
      "accountId": "",
      "type": "trade",
      "amount": "-1.56398259",
      "details": "Finalization Trade orderId=\'338348\' for DEMO_USER",
      "currency": "BTC"
    },
    {
      "transactionId": "trade_338348_finalization_USD",
      "timestamp": "2021-02-24T16:36:23.259Z",
      "accountId": "",
      "type": "trade",
      "amount": "77753.71512521",
      "details": "Finalization Trade orderId=\'338348\' for DEMO_USER",
      "currency": "USD"
    }
  ]
}
Get My Transaction History - Deposit Transactions for Main Account

Request (Client sends request to find all deposit transactions for main account)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "accountId": "",
    "type": "deposit"
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "ok": "ok",
  "data": [
    {
      "transactionId": "deposit_135857381",
      "timestamp": "2021-02-19T10:56:16.255Z",
      "accountId": "",
      "type": "deposit",
      "amount": "0.05000000",
      "details": "Deposit depositId=135857381 for DEMO_USER",
      "currency": "BTC"
    }
  ]
}
Get My Transaction History - For non-existing sub-account

Request (Client sends request for non-existing sub-account)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data":{
    "accountId": "nonExistingAcc"
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "ok": "ok",
  "data": []
}
Get My Transaction History - Incorrect "type" parameter

Request (Client sends request with incorrect "type" parameter)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "accountId": "",
    "type": "limitOrder"
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "error": "Operation type is not supported. Supported types: trade,commission,deposit,withdraw,internalTransfer"
  }
}
Get My Transaction History - Page size is more than 100

Request (Client sends request with invalid pageSize value)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "accountId": "",
    "type": "",
    "pageSize": 150,
    "pageNumber": 1
  }
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "error": "Page size is limited to 100 items"
  }
}
Get My Transaction History - For Incorrect Request

Request (Client sends request to find his transactions, but mandatory "data" field is missing)

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history"
}
Response

{
  "e": "get_my_transaction_history",
  "oid": "1465501899597_1_get_my_transaction_history",
  "data": {
    "error": "Internal error"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_transaction_history" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. It might be an empty object ("{}"), which means that Client sets no criteria for transactions which Client wants to see. However, this field should be present anyway and it should contain an object. Setting no criteria for transactions means that Client wants to get all transactions for the main account and all sub-accounts.
accountId	No	String	Account identifier, for which Client wants to find transactions. Empty string ("") or null value in this field represents Client’s main account. If this field is missing, then it means Client wants to find transactions for the main account and all sub-accounts.
type	No	String	If this field is present and contains one of the allowed values, then it means Client wants to get only transactions related to specified operation type. Allowed values are "trade", "deposit", "withdraw", "internalTransfer, "commission". If this field is missing or if this field is present but contains an empty string (""), then it means Client wants to get transactions for all operation types.
dateFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest moment in time when transactions were created. In the result set transactions’ timestamp field value should be greater than or equal to (>=) dateFrom. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateFrom should be less than the value in the field dateTo.
dateTo	No	Number	UTC timestamp in milliseconds. Represents the latest moment in time when transactions were created. In the result set transactions’ timestamp field value should be less than (<) dateTo. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateTo should be greater than the value in the field dateFrom.
sortOrder	No	String	Sort order of the result set. The result array is sorted by "timestamp" field. Allowed values: "ASC" - ascending order, "DESC" - descending order. If this field is missing then the default sort order is "DESC", so recently created transactions come first and oldest transactions come last.
pageSize	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of transactions in the result for this request and cannot be greater than 100. If this field is missing, then the default value of 100 is used. If this field contains one of the allowed values and, simultaneously, the pageNumber field is missing, then the default pageNumber value is applied. Specifying the value in the field pageSize is mandatory if the value in the field pageNumber is also sent in the Client's request.
pageNumber	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize transactions per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 1. If this field is missing, then the default value of 1 is used. This value cannot be lower than 1. If any valid value is specified in this field, then it is mandatory to also send the value in the field pageSize in the Client’s request.
Transaction History Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_transaction_history" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Array or Object	This object contains list of transactions, which satisfies request criteria. It might be an empty array ([]). If this array is empty, then it means there are no transactions, which satisfy Client’s request criteria. In case of error, the value of this filed should be not Array, but Object.
transactionId	Yes	String	Unique identifier of transaction.
timestamp	Yes	Datetime	Represents server timestamp when this transaction happened. Format: YYYY-MM-DDTHH:MM:SS.sssZ .
accountId	Yes	String	Represents the Account ID.
type	Yes	String	Represents the type of this operation. Allowed values are "trade", "deposit", "withdraw", "internalTransfer", "commission".
amount	Yes	String (which can be parsed as Float)	Represents amount of the transaction.
details	Yes	String	Represents transaction details.
currency	Yes	String	Represents the currency of the transaction.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Funding History
This request allows Client to find his deposit and withdrawal transactions.

REQUEST

get_my_funding_history

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Funding History Request Parameters
Get My Funding History - For Main Account and all sub-accounts

Request (Client sends request to find deposit/withdrawal transactions for the main account and all sub-accounts.)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "data": {}
}
Response (CEX.IO Spot Trading responds that Client has 2 withdrawal transactions (1 withdrawal from sub-account and 1 withdrawal from main account) and 3 deposit transactions (2 deposits to sub-accounts and 1 deposit to main account))

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "ok": "ok",
  "data": [
    {
      "txId": 148126,
      "clientId": "TestClient",
      "accountId": "100107_test",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "81.04000000",
      "commissionAmount": "1.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:25.272Z"
    },
    {
      "txId": 148127,
      "clientId": "TestClient",
      "accountId": "",
      "currency": "BTC",
      "direction": "withdraw",
      "amount": "11.34000000",
      "commissionAmount": "0.14000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:17.193Z"
    },
    {
      "txId": 148128,
      "clientId": "TestClient",
      "accountId": "100108_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "15.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:18:48.682Z"
    },
    {
      "txId": 148129,
      "clientId": "TestClient",
      "accountId": "100109_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:17:45.399Z"
    },
    {
      "txId": 148130,
      "clientId": "TestClient",
      "accountId": "",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-16T13:16:41.585Z"
    }
  ]
}
Get My Funding History - For Main Account and all Sub-accounts with Paging

Request (Client sends request to find deposit/withdrawal transactions for the main account and all sub-accounts and wants to see the first page expecting the result set is chunked to pages size 2 (not more than 2 transactions per page))

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "data": {
    "pageSize": 2,
    "pageNumber": 1
  }
}
Response (Supposed that Client has 5 transactions (like in previous example), CEX.IO Spot Trading responds with the first page, which includes 2 transactions)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "ok": "ok",
  "data": [
    {
      "txId": 148128,
      "clientId": "TestClient",
      "accountId": "100108_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "15.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:25.272Z"
    },
    {
      "txId": 148129,
      "clientId": "TestClient",
      "accountId": "100109_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:17.193Z"
    }
  ]
}
Get My Funding History - For Specified Sub-Account

Request (Client sends request to find deposit/withdrawal transactions for specified sub-account)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "data": {
    "accountId": "100109_test"
  }
}
Response (CEX.IO Spot Trading responds with deposit/withdrawal transactions for specified sub-account)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "ok": "ok",
  "data": [
    {
      "txId": 148129,
      "clientId": "TestClient",
      "accountId": "100109_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "55.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-14T15:09:12.557Z"
    }
  ]
}
Get My Funding History - Deposit Transactions for Main Account and all Sub-accounts with specified Period

Request (Client sends request to find all deposit transactions for main account and all sub-accounts, which happened within specified period)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "data": {
    "direction": "deposit",
    "dateFrom": 1514337745869,
    "dateTo": 1614337745869
  }
}
Response (CEX.IO Spot Trading responds that Client has only one transaction, which satisfies requested criteria)

{
  "e": "get_my_funding_history",
  "oid": "1465501899597_1_get_my_funding_history",
  "ok": "ok",
  "data": [
    {
      "txId": 148128,
      "clientId": "TestClient",
      "accountId": "100108_test",
      "currency": "BTC",
      "direction": "deposit",
      "amount": "15.34000000",
      "commissionAmount": "0.00000000",
      "status": "approved",
      "updatedAt": "2021-02-19T10:56:17.193Z"
    }
  ]
}
Get My Funding History - For Incorrect Request

Request (Client sends request to find some deposit/withdrawal transactions, but mandatory "data" field is missing)

{
  "e": "get_my_funding_history",
  "oid": "1465567380491_1_get_my_funding_history"
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed)

{
  "e": "get_my_funding_history",
  "oid": "1465567380491_1_get_my_funding_history",
  "data": {
    "error": "Internal error"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_funding_history" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details. It might be an empty object ("{}"), which means that Client sets no criteria for transactions which Client wants to see. However, this field should be present anyway and it should contain an object. Setting no criteria for transactions means that Client wants to get all deposits and withdrawals for the main account and all sub-accounts.
accountId	No	String	Account identifier, for which Client wants to find transactions. Empty string ("") or null value in this field represents Client’s main account. If this field is missing, then it means Client wants to find deposits and withdrawals for the main account and all sub-accounts.
txId	No	Number	Transaction identifier. If this field is present, then it means Client wants to get information only for specified transaction.
direction	No	String	If this field is present and contains one of the allowed values, then it means Client wants to get only transactions related to specified operation type. Allowed values are: "deposit", "withdraw". If this field is missing or if this field is present but contains an empty string (""), then it means Client wants to get all deposits and withdrawals.
currency	No	String	If this field is present, then it means Client wants to get only transactions in the specified currency. If this field is missing, then it means Client wants to get deposits/withdrawals in all currencies.
dateFrom	No	Number	UTC timestamp in milliseconds. Represents the earliest moment in time when transactions were created. In the result set transactions’ timestamp field value should be greater than or equal to (>=) dateFrom. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateFrom should be less than the value in the field dateTo.
dateTo	No	Number	UTC timestamp in milliseconds. Represents the latest moment in time when transactions were created. In the result set transactions’ timestamp field value should be less than (<) dateTo. If the request contains values in both fields dateFrom and dateTo, then the value in the field dateTo should be greater than the value in the field dateFrom.
pageSize	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. This parameter limits the maximum number of transactions in the result for this request and cannot be greater than 100. If this field is missing, then the default value of 100 is used. If this field contains one of the allowed values and, simultaneously, the pageNumber field is missing, then the default pageNumber value is applied. Specifying the value in the field pageSize is mandatory if the value in the field pageNumber is also sent in the Client's request.
pageNumber	No	Number	Because the result might contain too many transactions, Client should specify, which portion of the result list he wants to get as a response to this request. Result list is chunked into pages for not more than data.pageSize transactions per each page. This parameter specifies, which page number of the result set Client wants to see as the response to this request. First page number is 1. If this field is missing, then the default value of 1 is used. This value cannot be lower than 1. If any valid value is specified in this field, then it is mandatory to also send the value in the field pageSize in the Client’s request.
Funding History Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_my_funding_history" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Array or Object	This object contains list of transactions, which satisfies request criteria. It might be an empty array ([]). If this array is empty, then it means there are no transactions, which satisfy Client’s request criteria. In case of error, the value of this field should be not Array, but Object.
txId	Yes	Number	Unique ID of the transaction.
clientId	Yes	String	Represents the Client’s name.
accountId	Yes	String	Represents the Account ID.
currency	Yes	String	Represents the currency of the transaction.
direction	Yes	String	Represents the type of this operation. Allowed values: "deposit", "withdraw".
amount	Yes	String (which can be parsed as Float)	Represents amount of the transaction.
commissionAmount	Yes	String (which can be parsed as Float)	Represents commission amount of the transaction.
status	Yes	String	Represents the status of the transaction.
updatedAt	Yes	Datetime	Represents server timestamp when this transaction happened. Format: YYYY-MM-DDTHH:MM:SS.sssZ .
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Internal Transfer
This method works only with CEX.IO Spot Trading sub-accounts.
Client can request to transfer funds between his sub-accounts. CEX.IO Spot Trading does not charge Client any commission for transferring funds between his accounts. Along with a response to this request, CEX.IO Spot Trading sends Account Event messages to Client if this request is successful.

REQUEST

do_my_internal_transfer

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Internal” permission set for API Key.

Internal Transfer Request Parameters
Do My Internal Transfer - Transfer between sub-accounts

Request (Client requests to transfer 2 USD from sub-account "superhat" to sub-account "hallo". Note that "amount" field is String in this request and is allowed as well Float)

{
  "e": "do_my_internal_transfer",
  "oid": "1465572149539_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "hallo",
    "amount": "2",
    "currency": "USD",
    "clientTxId": "123"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification event before the response. New "superhat" balance is 18 USD.)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "superhat",
    "currency": "USD",
    "balance": "18.00000000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1465569413260,
    "action": "internalTransfer",
    "id": 672
  }
}
Response (CEX.IO Spot Trading responds to Client that internal transfer operation was successful and shows transactionId of this transfer)

{
  "e": "do_my_internal_transfer",
  "oid": "1465572149539_1_do_my_internal_transfer",
  "ok": "ok",
  "data": {
    "transactionId": 777
  }
}
Response (CEX.IO Spot Trading sends Account Event notification event before the response. New "hallo" balance is 2 USD)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "hallo",
    "currency": "USD",
    "balance": "2.00000000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1456839391786,
    "action": "internalTransfer",
    "id": 673
  }
}
Do My Internal Transfer - Duplicate clientTxId

Request (Client requests to transfer 4 USD from sub-account "superhat" to sub-account "hallo" with clientTxId = "123" which was already used in the previous example to transfer 2 USD)

{
  "e": "do_my_internal_transfer",
  "oid": "1465572149539_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "hallo",
    "amount": "4",
    "currency": "USD",
    "clientTxId": "123"
  }
}
Response (CEX.IO Spot Trading sends Account Event notification event before the response. "superhat" balance is already 18 USD after previous transfer)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "superhat",
    "currency": "USD",
    "balance": "18.00000000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1465569413260,
    "action": "internalTransfer",
    "possibleResend": true,
    "id": 672
  }
}
Response (CEX.IO Spot Trading detects duplicate and funds are not transferred between accounts. CEX.IO Spot Trading responds to Client with transactionId of the successful transfer (first transfer with clientTxId = "123"))

{
  "e": "do_my_internal_transfer",
  "oid": "1465572149539_1_do_my_internal_transfer",
  "ok": "ok",
  "data": {
    "transactionId": 777
  }
}
Response (CEX.IO Spot Trading sends Account Event notification event before the response. "hallo" balance is already 2 USD)

{
  "e": "account_update",
  "ok": "ok",
  "data": {
    "clientId": "BitFok",
    "accountId": "hallo",
    "currency": "USD",
    "balance": "2.00000000",
    "onHoldBalance": "0.00000000",
    "timestamp": 1456839391786,
    "action": "internalTransfer",
    "possibleResend": true,
    "id": 673
  }
}
Do My Internal Transfer - Insufficient Funds

Request (Client requests to transfer 180 USD from sub-account "superhat" to sub-account "hallo", but there are only 18 USD on "superhat" sub-account)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573018233_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "hallo",
    "amount": 180,
    "currency": "USD"
  }
}
Response (CEX.IO Spot Trading responds that Client has insufficient funds on his "superhat" sub-account. So the internal transfer was rejected, balances did not change)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573018233_1_do_my_internal_transfer",
  "data": {
    "error": "Insufficient funds"
  }
}
Do My Internal Transfer - Incorrect amount

Request (Client requests to transfer -10 USD from sub-account "superhat" to sub-account "hallo", but amount is < 0, which is not allowed)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573131917_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "hallo",
    "amount": "-10",
    "currency": "USD"
  }
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed and amount should be greater than zero)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573131917_1_do_my_internal_transfer",
  "data": {
    "error": "Amount should be greater than zero"
  }
}
Do My Internal Transfer - Incorrect accountId

Request (Client requests to transfer 10 USD to sub-account "hallo", but does not specify from which sub-account namely)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573587788_1_do_my_internal_transfer",
  "data": {
    "toAccountId": "hallo",
    "amount": 10,
    "currency": "USD",
    "clientTxId": "12342134442"
  }
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed because mandatory parameter fromAccountId was not specified)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573587788_1_do_my_internal_transfer",
  "data": {
    "error": "Mandatory parameter fromAccountId is missing"
  }
}
Do My Internal Transfer - Same fromAccountId and toAccountId values

Request (Client requests to transfer 10 USD from sub-account "superhat" to sub-account "superhat" (same account))

{
  "e": "do_my_internal_transfer",
  "oid": "1465573725661_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "superhat",
    "amount": 10,
    "currency": "USD"
  }
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed and fromAccountId and toAccountId values should be different)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573725661_1_do_my_internal_transfer",
  "data": {
    "error": "fromAccountId and toAccountId should be different"
  }
}
Do My Internal Transfer - Invalid currency

Request (Client requests to transfer 10 ABC from sub-account "superhat" to sub-account "testAccount1". However, ABC is not a valid currency)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573926410_1_do_my_internal_transfer",
  "data": {
    "fromAccountId": "superhat",
    "toAccountId": "testAccount1",
    "amount": 20,
    "currency": "ABC"
  }
}
Response (CEX.IO Spot Trading responds to Client that such request is not allowed)

{
  "e": "do_my_internal_transfer",
  "oid": "1465573926410_1_do_my_internal_transfer",
  "data": {
    "error": "Unsupported currency ABC"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_my_internal_transfer" value is allowed here.
oid	Yes	String	Unique ID of this request.
clientTxId	No	String	Unique identifier of transfer specified by Client. If two (or more) transfers with the same clientTxId are received by the system - only first transfer will be processed, second and subsequent transfers will return transactionId of the first completed internal transfer for clientTxId.
fromAccountId	Yes	String	Account identifier of sub-account, from which Client wants to transfer funds. Empty string value ("") in this field is not allowed.
toAccountId	Yes	String	Account identifier of sub-account, to which Client wants to transfer funds. Empty string value ("") in this field is not allowed. Destination Account should be created by Client beforehand via Create Account method or Spot Trading Web Portal.
currency	Yes	String	Currency of internal transfer.
amount	Yes	Float (or String which can be parsed as Float)	Amount of the transaction. It should be greater than zero.
Internal Transfer Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_my_internal_transfer" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
transactionId	No	Number	Unique identifier of successful internal transfer transaction.
data.error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Processing Info
This request allows Client to receive detailed information about available options to make deposits from external wallets and withdrawals to external wallets as to each supported cryptocurrency, including cryptocurrency name and available blockchains for deposit\withdrawals. Also, as to each supported blockchain there are indicated type of cryptocurrency on indicated blockchain, current deposit\withdrawal availability, minimum amounts for deposits\withdrawals, external withdrawal fees.

Processing Information makes Client more flexible in choosing desired blockchain for receiving Deposit address and initiating external withdrawals via certain blockchain, so that Client uses more convenient way of transferring his crypto assets to or from CEX.IO Ecosystem.

Note that this method indicates minimum deposit\withdrawal limits and external withdrawal fees for external crypto transfers. Currently, deposits and withdrawals of funds between CEX.IO Wallet and CEX.IO Spot Trading account are free.
Currently, external withdrawals are not supported via CEX.IO Spot Trading API.
REQUEST

get_processing_info

API Rate Limit Cost: 10

API Key Permission

This method requires “Read” permission set for API Key.

Processing Info Request Parameters
Get Processing Info Request for one specific cryptocurrency

Request (Client queries processing info for "BTC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_1_get_processing_info",
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds that only 'bitcoin' blockchain is supported for deposits\withdrawals of "BTC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_1_get_processing_info",
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    }
  }
}
Get Processing Info Request for several cryptocurrencies

Request (Client queries processing info for "BTC" and "USDC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_2_get_processing_info",
  "data": {
    "currencies": ["BTC","USDC"]
  }
}
Response (CEX.IO Spot Trading responds that for deposits\withdrawals 'bitcoin' blockchain is supported for "BTC" and "ethereum", "stellar" and "tron" blockchains are supported for "USDC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_2_get_processing_info",
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005",
          "depositConfirmations": 2
        }
      }
    },
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40",
          "depositConfirmations": 25
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 1
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1",
          "depositConfirmations": 21
        }
      }
    }
  }
}
Get Processing Info - No available blockchains

Request (Client queries processing info for supported cryptocurrency "ZEC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_4_get_processing_info",
  "data": {
    "currencies": ["ZEC"]
  }
}
Response (CEX.IO Spot Trading responds that request was processed successfully but no blockchains are supported for "ZEC")

{
  "e": "get_processing_info",
  "oid": "1521724219900_4_get_processing_info",
  "ok": "ok",
  "data": {}
}
Get Processing Info - Invalid and fiat cryptocurrency

Request (Client queries processing info for "BTC", "ETH", "XXX" and "USD")

{
  "e": "get_processing_info",
  "oid": "1521724219900_5_get_processing_info",
  "data": {
    "currencies": ["BTC", "ETH", "XXX", "USD"]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currencies "XXX" and "USD" are indicated in the request)

{
  "e": "get_processing_info",
  "oid": "1521724219900_5_get_processing_info",
  "data": {
    "error": "Request contains unsupported currencies: XXX, USD."
  }
}
Get Processing Info - Invalid value type in "currencies" array

Request (Client queries processing info with invalid values type in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_6_get_processing_info",
  "data": {
    "currencies": [1,2,3]
  }
}
Response (CEX.IO Spot Trading responds that error occurred because wrong type of value was indicated in "currencies" array and only string values are allowed)

{
  "e": "get_processing_info",
  "oid": "1521724219900_6_get_processing_info",
  "data": {
    "error": "Currencies array should consist of string type values."
  }
}
Get Processing Info - Not an array indicated in "currencies" field

Request (Client queries processing info with indicating empty object ({}) in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_7_get_processing_info",
  "data": {
    "currencies": {}
  }
}
Response (CEX.IO Spot Trading responds that error occurred because only array is allowed in "currencies" field)

{
  "e": "get_processing_info",
  "oid": "1521724219900_7_get_processing_info",
  "data": {
    "error": "Currencies should be array."
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_processing_info" value is allowed here.
oid	Yes	String	Unique ID of this request.
data	Yes	Object	This object contains request details.
currencies	No	Array	List of cryptocurrencies for which Client wants to get information about supported blockchains for deposit\withdraw, limits and commissions. Cryptocurrencies should be in upper case and of string type. The list should contain only valid cryptocurrency symbols. If this field is missing or contains an empty array ([]), then it means Client wants to get processing info for all available cryptocurrencies.
Processing Info Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "get_processing_info" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details.
data.YYY	Yes	String	Cryptocurrency symbol specified in Client's request.
data.YYY.name	Yes	String	Cryptocurrency name.
data.YYY.blockchains	Yes	Object	This object contains info about all supported blockchains to deposit\withdraw cryptocurrency YYY.
data.YYY.blockchains.X	Yes	Object	This object contains details and limitations for deposit\withdrawal of cryptocurrency YYY via blockchain X, including data about blockchain type, current availability to deposit\withdraw, minimum deposit\withdrawal limit and external withdrawal fees.
data.YYY.blockchains.X. type	Yes	String	Type of cryptocurrency YYY on blockchain X.
data.YYY.blockchains.X. deposit	Yes	String	Describes current availability to deposit cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minDeposit	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be deposited from external wallet via blockchain X.
data.YYY.blockchains.X. withdrawal	Yes	String	Describes current availability to withdraw cryptocurrency YYY via blockchain X. Only "enabled" or "disabled" values are allowed herein.
data.YYY.blockchains.X. minWithdrawal	Yes	String (which can be parsed as Float)	Minimum amount of cryptocurrency YYY which can be withdrawn to external wallet via blockchain X.
data.YYY.blockchains.X. withdrawalFee	Yes	String (which can be parsed as Float)	Amount of withdrawal fee in cryptocurrency YYY, which which would be charged and subtracted from withdrawal amount if blockchain X is used for withdrawal.
data.YYY.blockchains.X. depositConfirmations	Yes	Number	Minimal confirmation number for transaction in the blockchain to be deposited to Client’s Spot Trading account.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Deposit Address
This method works only with CEX.IO Spot Trading sub-accounts.
This method can be used by Client for receiving a crypto address to deposit cryptocurrency to CEX.IO Spot Trading sub-accounts.

Blockchains for deposit
The list of available blockchains for generating deposit address can be received by Client via Processing Info request.
REQUEST

get_deposit_address

API Rate Limit Cost: 5

API Key Permission

This method requires “Read” permission set for API Key.

Deposit Address Parameters Parameters
Get Deposit Address Request for sub-account to deposit "BTC" cryptocurrency via 1 available blockchain

Client sends get_processing_info request for receiving all available blockchains to deposit BTC

{
  "e": "get_processing_info",
  "oid": "1521724219999_1_get_processing_info",
  "data": {
    "currencies": ["BTC"]
  }
}
Response (CEX.IO Spot Trading responds with processing info with only one available "bitcoin" blockchain for BTC)

{
  "e": "get_processing_info",
  "oid": "1521724219999_1_get_processing_info",
  "ok": "ok",
  "data": {
    "BTC": {
      "name": "Bitcoin",
      "blockchains": {
        "bitcoin": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0.0001",
          "withdrawal": "enabled",
          "minWithdrawal": "0.002",
          "withdrawalFee": "0.0005"
        }
      }
    }
  }
}
Request (Client queries deposit address for BTC cryptocurrency on "bitcoin" blockchain)

{
  "e": "get_deposit_address",
  "oid": "1521724219900_1_get_deposit_address",
  "data": {
    "accountId": "testAccount1", // sub-account ID
    "currency": "BTC", // currency "BTC"
    "blockchain": "bitcoin" // required blockchain
  }
}
Response (CEX.IO Spot Trading responds with information about crypto address to deposit BTC via "bitcoin" blockchain)

{
  "e": "get_deposit_address",
  "oid": "1521724219900_1_get_deposit_address",
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "currency": "BTC",
    "blockchain": "bitcoin"
  }
}
Get Deposit Address Request for sub-account to deposit "USDC" cryptocurrency via specific blockchain

Client sends get_processing_info request for receiving all available blockchains to deposit USDC

{
  "e": "get_processing_info",
  "oid": "1521724219999_2_get_processing_info",
  "data": {
    "currencies": ["USDC"]
  }
}
Response (CEX.IO Spot Trading responds that there are 3 available blockchains to deposit USDC, namely "ethereum", "stellar" and "tron")

{
  "e": "get_processing_info",
  "oid": "1521724219999_2_get_processing_info",
  "ok": "ok",
  "data": {
    "USDC": {
      "name": "USD Coin",
      "blockchains": {
        "ethereum": {
          "type": "ERC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "40"
        },
        "stellar": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "20"
        },
        "tron": {
          "type": "TRC20",
          "deposit": "enabled",
          "minDeposit": "5",
          "withdrawal": "enabled",
          "minWithdrawal": "50",
          "withdrawalFee": "1"
        }
      }
    }
  }
}
Request (Client queries deposit address for sub-account "superhat" for USDC cryptocurrency to further deposit it via "tron" blockchain as most profitable for Client)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_2_get_deposit_address",
  "data": {
    "accountId": "superhat",
    "currency": "USDC",
    "blockchain": "tron"
  }
}
Response (CEX.IO Spot Trading responds with information about crypto address to deposit USDC via "tron" blockchain on "superhat" account)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_2_get_deposit_address",
  "ok": "ok",
  "data": {
    "accountId": "superhat",
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "currency": "USDC",
    "blockchain": "tron"
  }
}
Get Deposit Address Request for sub-account to deposit "XRP" cryptocurrency

Request (Client sends get_processing_info request for receiving of all available blockchains to deposit XRP)

{
  "e": "get_processing_info",
  "oid": "1521724219999_3_get_processing_info",
  "data": {
    "currencies": ["XRP"]
  }
}
Response (CEX.IO Spot Trading responds that there is only 1 available blockchain to deposit XRP, namely "ripple")

{
  "e": "get_processing_info",
  "oid": "1521724219999_3_get_processing_info",
  "ok": "ok",
  "data": {
    "XRP": {
      "name": "Ripple",
      "blockchains": {
        "ripple": {
          "type": "coin",
          "deposit": "enabled",
          "minDeposit": "0",
          "withdrawal": "enabled",
          "minWithdrawal": "0.3",
          "withdrawalFee": "0.25"
        }
      }
    }
  }
}
Request (Client queries deposit address for sub-account "superhat" for XRP cryptocurrency to further deposit it via "ripple" blockchain)

{
  "e": "get_deposit_address",
  "oid": "1521724219933_3_get_deposit_address",
  "data": {
    "accountId": "superhat",
    "currency": "XRP",
    "blockchain": "ripple"
  }
}
Response (CEX.IO Spot Trading responds with destination and memo to deposit XRP via "ripple" blockchain)

{
  "e": "get_deposit_address",
  "oid": "1521724219933_3_get_deposit_address",
  "ok": "ok",
  "data": {
    "accountId": "superhat",
    "destination": "rE1sdh25BJQ3qFwngiTBwaq3zPGGYcrjp1",
    "memo": "65629",
    "currency": "XRP",
    "blockchain": "ripple"
  }
}
Get Deposit Address - Unsupported currency

Request (Client queries deposit address)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_4_get_deposit_address",
  "data": {
    "accountId": "testAccount1",
    "currency": "XXX",
    "blockchain": "ethereum"
  }
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currency is specified in the request)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_4_get_deposit_address",
  "data": {
    "error": "Unsupported currency XXX"
  }
}
Get Deposit Address - Unsupported blockchain

Request (Client queries deposit address)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_5_get_deposit_address",
  "data": {
    "accountId": "testAccount1",
    "currency": "ETC",
    "blockchain": "tezos"
  }
}
Response (CEX.IO Spot Trading responds that error occurred because unsupported currency is specified in the request)

{
  "e": "get_deposit_address",
  "oid": "1521724219999_5_get_deposit_address",
  "data": {
    "error": "Blockchain is not supported."
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_deposit_funds_from_wallet" value is allowed here.
oid	Yes	String	Unique ID of this request.
accountId	Yes	String	Sub-account identifier, to which Client wants to make a deposit. Empty string value ("") in this field is not allowed.
currency	Yes	String	Cryptocurrency name, for which Client wants to get a deposit address.
blockchain	Yes	String	Blockchain name, via which Client wants to make a deposit of requested currency. Available blockchains can be received via Processing Info request.
Deposit Address Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_deposit_funds_from_wallet" value is allowed here.
oid	Yes	String	Unique ID of this Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
data	Yes	Object	This object contains response details with generated cryptocurrency address.
accountId	Yes	String	Sub-account identifier, to which Client wants to make a deposit.
address	No	String	Crypto address for deposit. Please be informed that destination and memo fields are used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
destination	No	String	Destination address for deposit used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
memo	No	String	A special identifier used for ledger cryptocurrencies (e.g. XRP, XLM, ATOM).
currency	Yes	String	Cryptocurrency name, for which deposit address is generated.
blockchain	Yes	String	Blockchain name, via which requested cryptocurrency can be deposited via generated address.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Funds Deposit from Wallet
This method works only with CEX.IO Spot Trading sub-accounts.
Client can deposit funds from CEX.IO Wallet to Spot Trading sub-account.

The system avoids processing of multiple deposit requests with the same clientTxId. If multiple deposit requests with identical clientTxId are received - the system processes only the first deposit request and rejects the second and subsequent deposit requests with the same clientTxId.

REQUEST

do_deposit_funds_from_wallet

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Wallet” permission set for API Key.

Funds Deposit from Wallet Request Parameters
Funds Deposit Request from CEX.IO Wallet to Spot Trading sub-account

Request (Client queries deposit of BTC to sub-account "testAccount1")

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631100952225_deposit_from_wallet",
  "data": {
    "amount": 0.001,
    "currency": "BTC",
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684398846720_1"
  }
}
Response (CEX.IO Spot Trading responds with information that transaction was approved)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631100952225_deposit_from_wallet",
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684398846720_1",
    "currency": "BTC",
    "status": "approved"
  }
}
Funds Deposit Request from CEX.IO Wallet to Spot Trading sub-account

Request (Client queries deposit of XRP to sub-account)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631101631321_deposit_from_wallet",
  "data": {
    "amount": 200,
    "currency": "XRP",
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684399110416_1"
  }
}
Response (CEX.IO Spot Trading responds with information that transaction is pending)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631101631321_deposit_from_wallet",
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-depositFromWallet-test-1684399110416_1",
    "currency": "XRP",
    "status": "pending"
  }
}
Invalid Deposit Request (too low amount)

Request (Client queries deposit of invalid amount)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631101114709_deposit_from_wallet",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "depositFromWallet-test-1631101114709",
    "currency": "BTC",
    "amount": 0.00000002
  }
}
Response (CEX.IO Spot Trading responds that deposit was rejected due to low amount)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631101114709_deposit_from_wallet",
  "data": {
    "error": "Too low amount to deposit 0.00000002 BTC. Minimum amount 0.00100000 BTC"
  }
}
Invalid Deposit Request (unsupported currency)

Request (Client queries deposit of unsupported currency)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631103998454_deposit_from_wallet",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "depositFromWallet-test-1631103998454",
    "currency": "XXX",
    "amount": 25
  }
}
Response (CEX.IO Spot Trading responds that deposit was rejected because currency is not supported)

{
  "e": "do_deposit_funds_from_wallet",
  "oid": "1631103998454_deposit_from_wallet",
  "data": {
    "error": "Unsupported currency XXX"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_deposit_funds_from_wallet" value is allowed here.
oid	Yes	String	Unique ID of this request.
clientTxId	Yes	String	Transaction identifier assigned by Client.
accountId	Yes	String	Sub-account identifier, to which Client wants to deposit funds. Empty string value (“”) in this field is not allowed.
currency	Yes	String	Crypto or fiat currency symbol for deposit.
amount	Yes	Float (or String which can be parsed as Float)	Amount for deposit.
Funds Deposit from Wallet Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_deposit_funds_from_wallet" value is allowed here.
oid	Yes	String	Unique ID of this Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	Sub-account identifier, to which Client initiated deposit funds.
clientTxId	Yes	String	Transaction identifier assigned by Client.
currency	Yes	String	Crypto or fiat currency symbol for deposit
status	Yes	String	Deposit transaction status. Allowed values - "rejected", "pending", "approved".
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.
Funds Withdrawal to Wallet
This method works only with CEX.IO Spot Trading sub-accounts.
Client can withdraw funds from Spot Trading sub-account to CEX.IO Wallet.

The system avoids multiple withdrawal requests with the same clientTxId. If multiple withdrawal requests with identical clientTxId are received - the system processes only the first withdrawal request and rejects the second and subsequent withdrawal requests with the same clientTxId.

REQUEST

do_withdrawal_funds_to_wallet

API Rate Limit Cost: 1

API Key Permission

This method requires “Funds Wallet” permission set for API Key.

Funds Withdrawal to Wallet Request Parameters
Funds Withdrawal Request from Spot Trading sub-account to CEX.IO Wallet

Request (Client queries withdrawal of BTC from sub-account "testAccount1")

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598254954_withdraw_to_wallet",
  "data": {
    "amount": 0.001,
    "currency": "BTC",
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399231967_1"
  }
}
Response (CEX.IO Spot Trading responds with information that transaction was approved)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598254954_withdraw_to_wallet",
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399231967_1",
    "currency": "BTC",
    "status": "approved"
  }
}
Funds Withdrawal Request from Spot Trading sub-account to CEX.IO Wallet

Request (Client queries withdrawal of XRP from sub-account "testAccount1")

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598290977_withdraw_to_wallet",
  "data": {
    "amount": 200,
    "currency": "XRP",
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399377964_1"
  }
}
Response (CEX.IO Spot Trading responds with information that transaction is pending)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598290977_withdraw_to_wallet",
  "ok": "ok",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "tx-withdrawToWallet-test-1684399377964_1",
    "currency": "XRP",
    "status": "pending"
  }
}
Invalid Withdrawal Request (too low amount)

Request (Client queries withdrawal of invalid amount)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598297863_withdraw_to_wallet",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "withdrawToWallet-test-1630598297863",
    "currency": "BTC",
    "amount": 0.00000002
  }
}
Response (CEX.IO Spot Trading responds that withdrawal was rejected due to low amount)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598297863_withdraw_to_wallet",
  "data": {
    "error": "Too low amount to withdraw 0.00000002 BTC. Minimum amount 0.00100000 BTC"
  }
}
Invalid Withdrawal Request (unsupported currency)

Request (Client queries withdrawal of unsupported currency)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598290954_withdraw_to_wallet",
  "data": {
    "accountId": "testAccount1",
    "clientTxId": "withdrawToWallet-test-1630598290954",
    "currency": "XXX",
    "amount": 10
  }
}
Response (CEX.IO Spot Trading responds that withdrawal was rejected because currency is not supported)

{
  "e": "do_withdrawal_funds_to_wallet",
  "oid": "1630598290954_withdraw_to_wallet",
  "data": {
    "error": "Unsupported currency XXX"
  }
}
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_withdrawal_funds_to_wallet" value is allowed here.
oid	Yes	String	Unique ID of this request.
clientTxId	Yes	String	Transaction identifier assigned by Client.
accountId	Yes	String	Sub-account identifier, from which Client wants to withdraw funds. Empty string value (“”) in this field is not allowed.
currency	Yes	String	Crypto or fiat currency symbol for deposit.
amount	Yes	Float (or String which can be parsed as Float)	Amount for withdrawal.
Funds Withdrawal to Wallet Response Parameters
Field Name	Mandatory	Format	Description
e	Yes	String	Describes the type of this message. Only "do_withdrawal_funds_to_wallet" value is allowed here.
oid	Yes	String	Unique ID of Client’s request, for which this message is in response to.
ok	No	String	If this field is present, then request is successful. If this field is missing, then request is not successful. Only "ok" value is allowed here.
accountId	Yes	String	Sub-account identifier, from which Client initiated funds withdrawal.
clientTxId	Yes	String	Transaction identifier assigned by Client.
currency	Yes	String	Crypto or fiat currency symbol for withdrawal.
status	Yes	String	Withdrawal transaction status. Allowed values - “rejected”, “pending”, “approved”.
error	No	String	If this field is present, then request is not successful. Represents human readable error reason of why request is not successful.