API Introduction
Users are welcome to make use of this WEEX API developer documentation.

This document serves as the official reference for WEEX API features which are continuously being updated. Check back regularly for updates!

You can switch between the different API operations by clicking on the top menu. The documentation language can be changed via the language button in the upper right corner.

Request parameters and response result examples are provided on the right side of the documentation.
Market Making/Quantitative Trading
We welcome institutional partners with proven market-making strategies and substantial trading volumes to join our Market Maker Program.To apply, please provide the following information in an email to us:

support@weex.com (for market maker application)

Your UID (ensure no commission affiliations exist for this UID)

Screenshots as proof of 30-day market-making volume from other exchanges

A brief description of your market-making strategy (no details required)
API Update Notifications
WEEX will announce API additions, updates, deprecations, and other critical changes through official notices in advance. It is recommended to follow and subscribe to API change notifications to stay updated.

Click here to subscribe to announcement


Preparation
To use the API, please log in to the web platform, create and configure API keys with proper permissions, then proceed with development and trading as detailed in this documentation.

Click here to create an API Key.

Each user can create up to 10 API Key groups. Each key can be configured for "Read" and/or "Trade" permissions.

Permission details:

Read permission: for data queries such as market data.
Trade permission: enables order placement, cancellation, and related actions.
After creating an API Key, securely store the following:

APIKey — The unique identifier for API authentication which is algorithmically generated.
SecretKey — The system-generated private key for signature encryption.
Passphrase —A user-defined access phrase. Note: If lost, the Passphrase cannot be recovered. You must create a new API key.
tip
You can bind IP addresses to API keys when creating API keys. Unrestricted API keys (with no IP address binding) pose security risks.

warning
Risk warning: These three keys directly impact account security. Never share your Passphrase. Losing any of these keys may result in asset loss. Delete compromised API keys immediately.



API Types
This section categorizes APIs into two types:

Public APIs
Private APIs
Public APIs

Public APIs allow users to retrieve configuration and market data.These requests do not require authentication.

Private APIs

Private APIs enable order management and account management.Each private request must be authenticated using a standardized signature method.

Private APIs require validation with your API key.




Access Restrictions
This section outlines access restrictions:

Rest API: Returns the "429 Too Many Requests" status if the frequency limit is exceeded.
Rest API

Requests with valid API keys are rate-limited by the API key. Requests without API keys are rate-limited by the public IP address.

Rate limiting rules: The default limit is 10 requests/second unless specified otherwise in individual endpoint documentation.

Special note for batch orders: Placing a batch order comprised of 4 trading pairs with 10 orders each counts as 1 request.



LIMITS
There is rate limit for APIKey frequency, upon exceed client will get code 429: Too many requests. The account is used as the basic unit of speed limit for the endpoints that need to carry APIKey. For endpoints that do not need to carry APIKey, IP addresses are used as the basic unit of rate limiting.

Limits Description

According to the two modes of IP and UID limit, each are independent.

Endpoints are marked according to IP or UID limit and their corresponding weight value.

Each endpoint with IP limits has an independent 500 every 10 second limit.

Each endpoint with UID limits has an independent 500 every 10 second limit.

Limits Error

When a 429 is received, it's your obligation as an API to back off and not spam the API.

API Public Parameters
side(order direction)

Field	Description
sell	Sell order
buy	Buy order
orderType (Order Type)

Field	Description
limit	Limit order
market	Market order
force (Order Type)

Field	Description
normal	Default order, no special controls needed
postOnly	Post-only order
fok	Fill-Or-Kill order
ioc	Immediate-Or-Cancel order
status (Order Status)

Field	Description
new	Unfilled
partial_fill	Partially filled
full_fill	All Filled
cancelled	Canceled
groupType (Major transaction types)

Field	Description
deposit	Deposit
withdraw	Withdraw
transaction	Trade
transfer	Transfer
other	Others
bizType (Account capital flow operation type)

Field	Description
deposit	Deposit
withdraw	Withdraw
buy	Buy
sell	Sell
transfer-in	Inbound transfer
transfer-out	Outbound transfer
status (Order status)

Field	Description
cancel	Canceled
reject	Rejected
success	Success
wallet-fail	Wallet failed
wallet-processing	Wallet is processing
first-audit	First review
recheck	Second review
first-reject	First review rejected
recheck-reject	Second review rejected
type (Withdrawal address query)

Field	Description
chain-on	On-chain
inner-transfer	Internal address
accountType (Account type)

Not case-sensitive

Field	Description
EXCHANGE	Spot account
OTC_SGD	OTC account
CONTRACT	Futures account
USD_MIX	Quanto swap account
USDT_MIX	USDT-M perpetual futures account
Candlestick intervals (granularity)

1min (1 minute)
5min (5 minutes)
15min (15 minutes)
30min (30 minutes)
1h (1 hour)
4h (4 hours)
12h (12 hours)
1day (1 day)
1week (1 week)
Previous
LIMITS



API Domain
You can use different domain as below Rest API.

Domain Name	API	Description
Spot REST Domain	https://api-spot.weex.com	Main Domain
Contract REST Domain	https://api-contract.weex.com	Main Domain


Signature
The ACCESS-SIGN request header is generated by using the HMAC SHA256 method encryption on the timestamp + method.toUpperCase() + requestPath + "?" + queryString + body string (+ denotes string concatenation), and putting the result through BASE64 encoding.

Signature Field Description

timestamp: This matches the ACCESS-TIMESTAMP header.
method: The request method (POST/GET), with all letters in uppercase.
requestPath: API endpoint path.
queryString: The query parameters after the "?" in the URL.
body: The string that corresponds to the request body (omitted if empty, typically for GET requests).
Signature format rules if queryString is empty

timestamp + method.toUpperCase() + requestPath + body
Signature format rules if queryString is not empty

timestamp + method.toUpperCase() + requestPath + "?" + queryString + body
Examples

Fetching market depth, using BTCUSDT as an example:

Timestamp = 1591089508404
Method = "GET"
requestPath = "/api/v2/market/depth"
queryString= "?symbol=btcusdt_spbl&limit=20"
Generate the string to be signed:

'1591089508404GET/api/v2/market/depth?symbol=btcusdt_spbl&limit=20'
Placing an order, using BTCUSDT_SPBL as an example:

Timestamp = 1561022985382

Method = "POST"

requestPath = "/api/v2/order/order"

body =

{"symbol":"btcusdt_spbl","quantity":"8","side":"buy","price":"1","orderType":"limit","clientOrderId":"ww#123456"}


Generate the string to be signed:

'1561022985382POST/api/spotPro/v3/order/order{"symbol":"btcusdt_spbl","size":"8","side":"buy","price":"1","orderType":"limit","clientOrderId":"ww#123456"}'


Steps to generate the final signature

Encrypt the unsigned string with HMAC SHA256 using your secretKey
Signature = hmac_sha256(secretkey, Message)
Encode the signature using Base64
Signature = base64.encode(Signature)



Request Processing
Java
Python
package com.weex.lcp.utils;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class ApiClient {
    // API Info
    private static final String API_KEY = ""; // Replace with your actual API Key
    private static final String SECRET_KEY = ""; // Replace with your actual Secret Key
    private static final String ACCESS_PASSPHRASE = ""; // Replace with your actual Access Passphrase
    private static final String BASE_URL = ""; // Replace with your actual API address
    // Generate signature (POST request)
    public static String generateSignature(String secretKey, String timestamp, String method, String requestPath, String queryString, String body) throws Exception {
        String message = timestamp + method.toUpperCase() + requestPath + queryString + body;
        return generateHmacSha256Signature(secretKey, message);
    }
    // Generate signature (GET request)
    public static String generateSignatureGet(String secretKey, String timestamp, String method, String requestPath, String queryString) throws Exception {
        String message = timestamp + method.toUpperCase() + requestPath + queryString;
        return generateHmacSha256Signature(secretKey, message);
    }
    // Generate HMAC SHA256 signature
    private static String generateHmacSha256Signature(String secretKey, String message) throws Exception {
        SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKeySpec);
        byte[] signatureBytes = mac.doFinal(message.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(signatureBytes);
    }
    // Send POST request
    public static String sendRequestPost(String apiKey, String secretKey, String accessPassphrase, String method, String requestPath, String queryString, String body) throws Exception {
        String timestamp = String.valueOf(System.currentTimeMillis());
        String signature = generateSignature(secretKey, timestamp, method, requestPath, queryString, body);
        HttpPost postRequest = new HttpPost(BASE_URL + requestPath);
        postRequest.setHeader("ACCESS-KEY", apiKey);
        postRequest.setHeader("ACCESS-SIGN", signature);
        postRequest.setHeader("ACCESS-TIMESTAMP", timestamp);
        postRequest.setHeader("ACCESS-PASSPHRASE", accessPassphrase);
        postRequest.setHeader("Content-Type", "application/json");
        postRequest.setHeader("locale", "en-US");
        StringEntity entity = new StringEntity(body, StandardCharsets.UTF_8);
        postRequest.setEntity(entity);
        try (CloseableHttpClient httpClient = HttpClients.createDefault()) {
            CloseableHttpResponse response = httpClient.execute(postRequest);
            return EntityUtils.toString(response.getEntity(), StandardCharsets.UTF_8);
        }
    }
    // Send GET request
    public static String sendRequestGet(String apiKey, String secretKey, String accessPassphrase, String method, String requestPath, String queryString) throws Exception {
        String timestamp = String.valueOf(System.currentTimeMillis());
        String signature = generateSignatureGet(secretKey, timestamp, method, requestPath, queryString);
        HttpGet getRequest = new HttpGet(BASE_URL + requestPath+queryString);
        getRequest.setHeader("ACCESS-KEY", apiKey);
        getRequest.setHeader("ACCESS-SIGN", signature);
        getRequest.setHeader("ACCESS-TIMESTAMP", timestamp);
        getRequest.setHeader("ACCESS-PASSPHRASE", accessPassphrase);
        getRequest.setHeader("Content-Type", "application/json");
        getRequest.setHeader("locale", "en-US");
        try (CloseableHttpClient httpClient = HttpClients.createDefault()) {
            CloseableHttpResponse response = httpClient.execute(getRequest);
            return EntityUtils.toString(response.getEntity(), StandardCharsets.UTF_8);
        }
    }
    // Example usage
    public static void main(String[] args) {
        try {
            // GET request example
            String requestPath = "/api/uni/v3/order/currentPlan";
            String queryString = "?symbol=cmt_bchusdt&delegateType=0&startTime=1742213127794&endTime=1742213506548";
            String response = sendRequestGet(API_KEY, SECRET_KEY, ACCESS_PASSPHRASE, "GET", requestPath, queryString);
            System.out.println("GET Response: " + response);
            // POST request example
             String body = "{\"symbol\": \"ETHUSDT_SPBL\", \"limit\": \"2\"}";
             response = sendRequestPost(API_KEY, SECRET_KEY, ACCESS_PASSPHRASE, "POST", requestPath, "", body);
             System.out.println("POST Response: " + response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


All requests are based on the HTTPS protocol. The Content-Type in the request headers must be set to 'application/json'.

Request Processing

Request parameters: Parameter encapsulation according to endpoint request parameter specification.
Submit request: Submit the encapsulated parameters to the server via GET/POST.
Server response: The server first performs security checks on the request data, and after passing the check, returns the response data to the user in the JSON format based on the operation logic.
Data processing: Process the server response data.
Success

HTTP 200 status codes indicates success and may contain content.Response content (if any) will be included in the returned data.

Common error codes

400 Bad Request – Invalid request format
401 Unauthorized – Invalid API Key
403 Forbidden – You do not have access to the requested resource
404 Not Found — No requests found
429 Too Many Requests – Rate limit exceeded
500 Internal Server Error – We had a problem with our server
Failed responses include error descriptions in the body.


Standard Specifications
Timestamp

The ACCESS-TIMESTAMP in request signatures is in milliseconds.Requests are rejected if the timestamp deviates by over 30 seconds from the API server time. If the local server time deviates significantly from the API server time, we recommend updating the HTTP header by querying the API server time.

Rate limiting rules

Too frequent requests will be rate-limited automatically and return the 429 status code in the HTTP header.

Public endpoints (such as market data endpoints): Uniform frequency of up to 20 requests per 2 seconds.
Authorization endpoints: Rate limits are based on the API key (see endpoint-specific rules).
Request formats

Only two request methods are supported: GET and POST

GET: Parameters are sent via queryString in the path to the server.
POST: Parameters are sent as a JSON-formatted body to the serve




Get Server Time
HTTP Request Retrieve the server's current timestamp.

GET /api/v2/public/time
Weight(IP): 1

Request parameters

NONE

Request example

curl "https://api-spot.weex.com/api/v2/public/time"

Response parameters

Field Name	Type	Field Description
data	Long	Server time
Response example

{
    "code": "00000",
    "msg": "success",
    "requestTime": 1622097118135,
    "data": 1622097118134
}




Basic Crypto Information
HTTP Request Retrieve all crypto information on the platform

GET /api/v2/public/currencies
Weight(IP): 1

Request parameters

NONE

Request example

curl "https://api-spot.weex.com/api/v2/public/currencies"


Response parameters

Field	Field Description
coinId	Crypto ID
coinName	Name of the crypto
transfer	Whether transfer is supported
chains	Blockchain information
> chain	Name of the blockchain
> needTag	Whether a tag is required
> withdrawAble	Whether withdrawals are enabled
> rechargeAble	Whether deposits are enabled
> withdrawFee	Withdrawal transaction fee
> depositConfirm	Number of block confirmations required for deposits
> withdrawConfirm	Number of block confirmations required for withdrawals
> minDepositAmount	Minimum deposit amount
> minWithdrawAmount	Minimum withdrawal amount
> browserUrl	Blockchain explorer URL for the network
Response example

{
    "code":"00000",
    "msg":"success",
    "requestTime":1622097139437,
    "data":[
        {
            "coinId":"1",
            "coinName":"BTC",
            "transfer":"true",
            "chains":[
                {
                    "chain":null,
                    "needTag":"false",
                    "withdrawAble":"true",
                    "rechargeAble":"true",
                    "withdrawFee":"0.005",
                    "depositConfirm":"1",
                    "withdrawConfirm":"1",
                    "minDepositAmount":"0.001",
                    "minWithdrawAmount":"0.001",
                    "browserUrl":"https://blockchair.com/bitcoin/testnet/transaction/"
                }
            ]
        },
        {
            "coinId":"2",
            "coinName":"USDT",
            "transfer":"true",
            "chains":[
                {
                    "chain":"ERC20",
                    "needTag":"false",
                    "withdrawAble":"true",
                    "rechargeAble":"true",
                    "withdrawFee":"0.01",
                    "depositConfirm":"12",
                    "withdrawConfirm":"1",
                    "minDepositAmount":"0.1",
                    "minWithdrawAmount":"0.1",
                    "browserUrl":"https://ropsten.etherscan.io/tx/"
                }
            ]
        }
    ]
}





API Default Symbol
HTTP Request Retrieve the trading pairs available for API trading on the platform

GET /api/v2/public/products
Weight(IP): 1

Request parameters

NONE

Request example

curl "https://api-spot.weex.com/api/v2/public/products"

Response parameters

Field Name	Type	Field Description
data	array	Trading pairs supported for API trading
Response example

{
  "code": "00000",
  "data": ["ETHUSDC_SPBL", "BTCUSDT_SPBL"],
  "msg": "success",
  "requestTime": "1743647243696"
}




Get Symbol Info
HTTP Request Get trading pair information, supporting individual, multiple, and full queries

GET /api/v2/public/exchangeInfo
Weight(IP): 10

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	No	Trading pair name, e.g. BTCUSDT_SPBL
symbols	String	No	Multiple trading pair names,e.g. BTCUSDT_SPBL,ETHUSDC_SPBL
Request example

curl "https://api-spot.weex.com/api/v2/public/exchangeInfo?symbol=BTCUSDT_SPBL"


curl "https://api-spot.weex.com/api/v2/public/exchangeInfo?symbols=BTCUSDT_SPBL,ETHUSDC_SPBL"


Response parameters

Field Name	Type	Field Description
symbol	String	Trading pair
baseCoin	String	Base currency
quoteCoin	String	Quote currency
tickSize	String	Minimum price increment (for quoteCoin)
stepSize	String	Minimum quantity increment (for baseCoin)
minTradeAmount	String	Minimum trade amount
maxTradeAmount	String	Maximum trade amount
takerFeeRate	String	Taker fee rate
makerFeeRate	String	Maker fee rate
buyLimitPriceRatio	String	Buy limit price ratio
sellLimitPriceRatio	String	Sell limit price ratio
marketBuyLimitSize	String	Market order buy size limit
marketSellLimitSize	String	Market order sell size limit
marketFallbackPriceRatio	String	Market order fallback price ratio
enableTrade	Boolean	Whether trading is enabled
enableDisplay	Boolean	Whether display is enabled
displayDigitMerge	String	Depth aggregation (e.g.: "1,0.1,0.001")
displayNew	Boolean	Whether newly listed pair
displayHot	Boolean	Whether hot trading pair
supportTracing	Boolean	Whether copy trading is supported
supportPlanMarket	Boolean	Whether market orders are supported in conditional orders
Response example

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743661516052,
  "data": [
    {
      "symbol": "BTCUSDT_SPBL",
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "tickSize": "0.1",
      "stepSize": "0.00000001",
      "minTradeAmount": "0.00001",
      "maxTradeAmount": "99999",
      "takerFeeRate": "0.001",
      "makerFeeRate": "0",
      "buyLimitPriceRatio": "0.99",
      "sellLimitPriceRatio": "0.99",
      "marketBuyLimitSize": "99999",
      "marketSellLimitSize": "99999",
      "marketFallbackPriceRatio": "0",
      "enableTrade": true,
      "enableDisplay": true,
      "displayDigitMerge": "",
      "displayNew": false,
      "displayHot": false,
      "supportTracing": true,
      "supportPlanMarket": true
    }
  ]
}




Get Single Ticker
HTTP request Retrieve single ticker data

GET /api/v2/market/ticker
Weight(IP): 1

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	Yes	Trading pair name
Request example

curl "https://api-spot.weex.com/api/v2/market/ticker?symbol=BTCUSDT_SPBL"


Response parameters

Field Name	Type	Field Description
symbol	String	Trading pair name
priceChange	String	Price change amount
priceChangePercent	String	Price change percentage
trades	long	24-hour trade count
size	String	24-hour trading volume (quantity)
value	String	24-hour trading value (amount)
high	String	24-hour highest price
low	String	24-hour lowest price
open	String	Opening price (24-hour period)
close	String	Closing price (24-hour period)
highTime	long	Timestamp of 24-hour high
lowTime	long	Timestamp of 24-hour low
startTime	long	Start timestamp of 24-hour period
endTime	long	End timestamp of 24-hour period
lastPrice	String	Last traded price
openInterest	String	Open interest (for derivatives)
ts	long	System timestamp
Response example

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743665793483,
  "data": {
    "symbol": "BTCUSDT_SPBL",
    "priceChange": "-965.6",
    "priceChangePercent": "-0.011451",
    "trades": 105901,
    "size": "78570.57284800",
    "value": "6731333236.9492884000",
    "high": "88495.5",
    "low": "82175.9",
    "open": "84319.6",
    "close": "83354.0",
    "highTime": 1743625002550,
    "lowTime": 1743638655112,
    "startTime": 1743576300000,
    "endTime": 1743665400000,
    "lastPrice": "83354.0",
    "openInterest": "0",
    "ts": 1750060557824
  }
}

Previous
Get Symbol Info


Get All Ticker
HTTP request Retrieve all ticker data

GET /api/v2/market/tickers
Weight(IP): 20

Request parameters

NONE

Request example

curl "https://api-spot.weex.com/api/v2/market/tickers"

Response parameters

Field Name	Type	Field Description
symbol	String	Trading pair name
priceChange	String	Price change amount
priceChangePercent	String	Price change percentage
trades	long	24-hour trade count
size	String	24-hour trading volume (quantity)
value	String	24-hour trading value (amount)
high	String	24-hour highest price
low	String	24-hour lowest price
open	String	Opening price (24-hour period)
close	String	Closing price (24-hour period)
highTime	long	Timestamp of 24-hour high
lowTime	long	Timestamp of 24-hour low
startTime	long	Start timestamp of 24-hour period
endTime	long	End timestamp of 24-hour period
lastPrice	String	Last traded price
openInterest	String	Open interest (for derivatives)
ts	long	System timestamp
Response example

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743667090710,
  "data": [{
    "symbol": "BTCUSDT_SPBL",
    "priceChange": "-628.0",
    "priceChangePercent": "-0.007465",
    "trades": 106283,
    "size": "78680.72453000",
    "value": "6740487302.7932238000",
    "high": "88495.5",
    "low": "82175.9",
    "open": "84125.9",
    "close": "83497.9",
    "highTime": 1743625002550,
    "lowTime": 1743638655112,
    "startTime": 1743577200000,
    "endTime": 1743666300000,
    "lastPrice": "83497.9",
    "openInterest": "0",
    "ts": 1750060557824
  }]
}

Previous
Get Single Ticker



Get Trades
HTTP request Retrieve trade data

GET /api/v2/market/fills
Weight(IP): 5

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	Yes	Trading pair ID
limit	String	No	Default: 100, max: 1,000
Request example

curl "https://api-spot.weex.com/api/v2/market/fills?symbol=BTCUSDT_SPBL&limit=1"


Response parameters

Field Name	Type	Field Description
symbol	String	Trading pair symbol
tradeId	String	Trade order ID
fillTime	long	Trade execution timestamp
fillPrice	String	Execution price
fillQuantity	String	Executed quantity
tradeValue	String	Total trade value (price × quantity)
bestMatch	boolean	Whether fully matched
buyerMaker	boolean	Whether buyer was the maker
Response example

{
    "code": "00000",
    "msg": "success",
    "requestTime": 1743668717640,
    "data": [
        {
            "symbol": "BTCUSDT_SPBL",
            "tradeId": "778a5376-a0b6-4c8f-ab64-dd6ea40f896e",
            "fillTime": 1743668713364,
            "fillPrice": "83609.7",
            "fillQuantity": "0.00011400",
            "tradeValue": "9.531505800",
            "bestMatch": true,
            "buyerMaker": true
        }
    ]
}


Previous
Get All Ticker


Get Candlestick Data
HTTP request Retrieve candlestick data

GET /api/v2/market/candles
Weight(IP): 1

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	Yes	Futures name
period	String	Yes	Candlestick interval, valid values include: [1m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,1w,1M]
limit	String	No	Number of results
Request example

curl "https://api-spot.weex.com/api/v2/market/candles?symbol=BTCUSDT_SPBL&period=30m&limit="


Response parameters

Field Name	Type	Field Description
0	long	System timestamp (ms)
1	String	Opening price
2	String	Highest price
3	String	Lowest price
4	String	Closing price
5	String	Trading volume
6	String	Trading turnover
Response example

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1743669821003,
  "data": [
    [
      1743669000000,
      "83654.0",
      "83778.0",
      "83531.5",
      "83688.7",
      "248.17024800",
      "20755885.859164900"
    ],
    [
      1743667200000,
      "83457.9",
      "83719.0",
      "83457.9",
      "83654.0",
      "247.94000200",
      "20730711.264144200"
    ]
  ]
}




Get OrderBook Depth
HTTP request Retrieve depth data

GET /api/v2/market/depth
Weight(IP): 1

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	Yes	Futures name
type	String	No	Default: step0: no aggregation.Values: step0, step1, step2, step3, step4, step5
limit	String	No	Number of entries (Only 15 and 200)
Request example

curl "https://api-spot.weex.com/api/v2/market/depth?symbol=BTCUSDT_SPBL&type=step0&limit="


Response parameters

Field Name	Type	Field Description
asks	array	Ask [Price, Quantity]
bids	array	Bid [Price, Quantity]
Response example

{
    "code":"00000",
    "msg":"success",
    "requestTime":1622102974025,
    "data":{
        "asks":[
            [
                "38084.5",
                "0.0039"
            ],
            [
                "38085.7",
                "0.0018"
            ],
            [
                "38086.7",
                "0.0310"
            ],
            [
                "38088.2",
                "0.5303"
            ]
        ],
        "bids":[
            [
                "38073.7",
                "0.4993000000000000"
            ],
            [
                "38073.4",
                "0.4500"
            ],
            [
                "38073.3",
                "0.1179"
            ],
            [
                "38071.5",
                "0.2162"
            ]
        ],
        "timestamp":"1622102974025"
    }
}







