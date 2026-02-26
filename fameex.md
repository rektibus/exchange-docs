Documentation
API Basic Information
This Spot Trading document lists the REST interface's baseurl as https://openapi.fameex.com.
This Spot Trading document lists the REST interface's backup baseurl as https://openapi.fameex.net.
This Contract Trading document lists the REST interface's baseurl as https://futuresopenapi.fameex.com.
This Contract Trading document lists the REST interface's backup baseurl as https://futuresopenapi.fameex.net.
All interfaces will return a JSON, object, or array.
If the response contains an array, the array elements are arranged in reverse chronological order, with earlier data appearing first.
All times and timestamps are in Unix time, with units in milliseconds.
Document Input Parameter Specifications
Input parameter names marked with a red * indicate that the parameter is mandatory; otherwise, it is optional.

The interface is case-sensitive to input parameter characters, and this will be explicitly stated in the interface. For example, if the interface requires an uppercase trading pair name, you must input BTCUSDT; inputting btcusdt is not allowed.

The document specifies the types of input parameters, and you must input according to the specified type. For example, the integer type can only accept numeric inputs;3 is correct, but "3" is not allowed.

General Interface Information
All requests are based on the Https protocol, and the Content-Type in the request header must be set to:'application/json'.
For GET method interfaces, parameters must be sent in the query string.
ForPOST method interfaces, parameters must be sent in the request body .
The order of parameters does not matter.
Whether the Interface Requires Signature Verification
Interface types are divided into: public, market, trade, and account.

Public and market-type interfaces can be accessed without an API-KEY or signature.
Trade and account security interfaces require API-KEY and signature verification before access.
The signature content is related to the parameters; if the parameters are input incorrectly, an error or empty value will be returned.
Interfaces requiring signature verification must include X-CH-SIGN,X-CH-APIKEY, and X-CH-TS in the Header for verification.
X-CH-TS (timestamp) is Unix time, in milliseconds.
X-CH-APIKEY is the user's apiKey.
X-CH-SIGN is the signature encryption key, which is the secretKey.The signature rules and examples can be referenced as follows: Signature Rules, Signature Example(#ExampleWithRequestParameters).
(The apiKeyand secretKey in the document are virtual values; the actual content needs to be obtained by the user through the API management on the front-end page.)
Interface Type	Authentication Type
Public	NONE
Market	NONE
Trade	TRADE
Account	USER_DATA
Interface Authentication Types
Each interface has its own authentication type, which determines what kind of authentication should be performed when accessing it.
If an API-KEY is required, it should be passed in the HTTP header as the X-CH-APIKEY field.
API-KEY and API-Secret are case-sensitive.
You can modify the permissions of the API-KEY in the user center on the web page, such as reading account information, sending trade instructions, and sending withdrawal instructions.
Authentication Type	Description	Header
NONE	Interfaces that do not require authentication	
TRADE	Interfaces that require a valid API-KEY and signature	X-CH-SIGN，X-CH-APIKEY，X-CH-TS
USER_DATA	Interfaces that require a valid API-KEY and signature	X-CH-SIGN，X-CH-APIKEY，X-CH-TS
USER_STREAM	Interfaces that require a valid API-KEY	X-CH-APIKEY，X-CH-TS
MARKET_DATA	Interfaces that require a valid API-KEY	X-CH-APIKEY，X-CH-TS

Interfaces Requiring Signature (TRADE and USER_DATA)
When calling TRADE or USER_DATA interfaces, the signature parameter should be passed in the HTTP header as the X-CH-SIGN .
X-CH-SIGN uses the HMAC SHA256 encryption algorithm, with the API-Secret corresponding to the API-KEY as the key forHMAC SHA256.
The X-CH-SIGN request header uses the （+string concatenation） of timestamp + method + requestPath + body as the object.
The timestamp value is the same as the X-CH-TS request header, the method is the request method in uppercase:GET/POST.
requestPath is the request interface path, for example:sapi/v1/order?symbol=ethusdt&orderID=111000111.
body is the string of the request body (post only), and if it is a GET request, body can be omitted.
The signature is case-insensitive.
Interface Examples
Below are examples of interfaces, showing the interface format, access links, and parameter descriptions.

GET Example: Get Server Time
GET https://openapi.fameex.com/sapi/v1/time

GET without request parameters

Request Example

const https = require('https');

const url = 'https://openapi.fameex.com/sapi/v1/time';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Response Example

{
  "timezone": "UTC",
  "server_time": 1705039779880
}
Response Parameters

Parameter Name	Type	Example	Description
timezone	string	UTC	Server timezone
server_time	long	1705039779880	Server timestamp

GET Example: Order Query
GET https://openapi.fameex.com/sapi/v1/order

GET with request parameters

Request Headers

Parameter Name	Type	Description
X-CH-SIGN*	string	Signature
X-CH-APIKEY*	string	Your API-key
X-CH-TS*	integer	Timestamp
Request Parameters

Parameter Name	Type	Description
orderId*	string	Order ID
symbol*	string	Lowercasetrading pair name, e.g.,ethusdt
API Data

Key	Value
apiKey	your API-KEY
secretKey	your API-SECRET
The following is an example of calling the interface to place an order using echo, openssl, and curl tools in a Linux bash environment.(The above apikey and secretKey are for demonstration only; please replace them with your real apiKey and secretKey)

Request Example

const axios = require("axios");
const crypto = require("crypto");

// API related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/sapi/v1/order";
const QUERY_STRING = "?orderId=12&symbol=ethusdt";

// Calculate the complete request URL
const REQUEST_PATH = REQUEST_URL + QUERY_STRING;
const FULL_URL = API_URL + REQUEST_PATH;

// API authentication information
const API_KEY = "your API-KEY";
const API_SECRET = "your API-SECRET";

// Generate the current millisecond-level timestamp
const timestamp = Date.now().toString();

// Request method
const METHOD = "GET";

// Generate signature (X-CH-SIGN) - GET requests have no body
const SIGN_PAYLOAD = timestamp + METHOD + REQUEST_PATH;
const SIGNATURE = crypto
  .createHmac("sha256", API_SECRET)
  .update(SIGN_PAYLOAD)
  .digest("hex");

// **Print debug information**
console.log("==== Request information ====");
console.log("Timestamp (X-CH-TS):", timestamp);
console.log("Sign Payload (String to be signed):", SIGN_PAYLOAD);
console.log("Signature (X-CH-SIGN):", SIGNATURE);
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
  "X-CH-SIGN": SIGNATURE,
  "X-CH-APIKEY": API_KEY,
  "X-CH-TS": timestamp,
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });
HMAC-SHA256 Signature example

// Generate Signature (X-CH-SIGN) - GET request has no body
const SIGN_PAYLOAD = timestamp + METHOD + REQUEST_PATH;
const SIGNATURE = crypto
  .createHmac("sha256", API_SECRET)
  .update(SIGN_PAYLOAD)
  .digest("hex");
// JavaScript code (categorized under HTTP)

let secretKey = pm.environment.get("SecretKey");  // Retrieve API key from environment variables
let timestampString = String(Date.now()); // Generate timestamp (accurate to milliseconds)
let method = pm.request.method; // Get request method (GET, POST, etc.)

let fullUrl = pm.request.url.toString();
let requestPath = "/"+fullUrl.split("/").slice(3).join("/"); // Get the part after `example.com`

// The X-CH-SIGN request header is composed of the string:timestamp + method + requestPath + body (where + represents string concatenation)
// The `body` is the string representation of the request payload (POST only). If it is a GET request, the `body` can be omitted.
let signPayload = timestampString + method.toUpperCase() + requestPath;
if (method.toUpperCase() === "POST") {
    let body = pm.request.body ? pm.request.body.raw : null; // Get the request body (if present)
    if (body) {
        try {
            const parsedBody = JSON.parse(body); // Attempt to parse JSON
            let bodyString = JSON.stringify(parsedBody);
            signPayload += bodyString
        } catch (e) {
            signPayload += body; // If not JSON, directly append the raw body
        }
    } else {
        console.log("POST method failed to process body data");
    }
}

//The signature uses the HMAC-SHA256 algorithm, with the API-Secret corresponding to the API-KEY as the HMAC-SHA256 key.
const crypto = require('crypto-js'); // Load the CryptoJS library.
// Calculate the signature
let signature = crypto.HmacSHA256(signPayload, secretKey).toString(crypto.enc.Hex);

// Set Headers
pm.variables.set('xChTs', timestampString);
pm.variables.set('xChSign', signature);
Return example

{}
POST Example: Create a Test Order
POST https://openapi.fameex.com/sapi/v1/order/test

Request Headers

Parameter Name	Type	Description
X-CH-SIGN*	string	Signature
X-CH-APIKEY*	string	Your API key
X-CH-TS*	integer	Timestamp
Request parameters

Parameter name	Example
symbol	BTCUSDT
side	BUY
type	LIMIT
volume	1
price	9300
API Data

Key	Value
apiKey	your API-KEY
secretKey	your API-SECRET
The following is an example of placing an order by calling an API in a Linux Bash environment using echo, openssl, and curl tools.(The apikey and secretKey above are for demonstration purposes only. Please replace them with your actual apiKey and secretKey.)

Request Example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const URL = "https://openapi.fameex.com";
const REQUEST_PATH = "/sapi/v1/order/test";
const API_URL = URL + REQUEST_PATH;
const API_KEY = "your API-KEY";
const API_SECRET = "your API-SECRET";

// Generate the current millisecond-level timestamp
const timestamp = Date.now().toString();

// Request method
const METHOD = "POST";

// Define the request body (in JSON format)
const bodyJson = JSON.stringify({
  symbol: "BTCUSDT",
  price: "9300",
  volume: "1",
  side: "BUY",
  type: "LIMIT",
});

// Generate signature (X-CH-SIGN)
const signPayload = timestamp + METHOD + REQUEST_PATH + bodyJson;
const signature = crypto
  .createHmac("sha256", API_SECRET)
  .update(signPayload)
  .digest("hex");

// **Print debug information**
console.log("==== Request information ====");
console.log("Timestamp (X-CH-TS):", timestamp);
console.log("Sign Payload (String to be signed):", signPayload);
console.log("Signature (X-CH-SIGN):", signature);
console.log("Request Body:", bodyJson);
console.log("==================");

// Send request
const headers = {
  "Content-Type": "application/json",
  "X-CH-SIGN": signature,
  "X-CH-APIKEY": API_KEY,
  "X-CH-TS": timestamp,
};

axios
  .post(API_URL, bodyJson, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });

body

{
  "symbol": "BTCUSDT",
  "price": "9300",
  "volume": "1",
  "side": "BUY",
  "type": "LIMIT"
}
HMAC-SHA256 Signature example

// Generate signature (X-CH-SIGN)
const signPayload = timestamp + METHOD + REQUEST_PATH + bodyJson;
const signature = crypto
  .createHmac("sha256", API_SECRET)
  .update(signPayload)
  .digest("hex");
// JavaScript Code (categorized under HTTP)

let secretKey = pm.environment.get("SecretKey");  // Get API key from environment variables
let timestampString = String(Date.now()); // Generate a timestamp (precise to milliseconds)
let method = pm.request.method; // Get the request method (GET, POST, etc.)

let fullUrl = pm.request.url.toString();
let requestPath = "/"+fullUrl.split("/").slice(3).join("/"); // Get the part after `example.com`

// The `X-CH-SIGN` header is formed by concatenating the string `timestamp + method + requestPath + body` (where `+` indicates string concatenation)
// The `body` is the request body string (for POST requests only). If it's a GET request, the body can be omitted.
let signPayload = timestampString + method.toUpperCase() + requestPath;
if (method.toUpperCase() === "POST") {
    let body = pm.request.body ? pm.request.body.raw : null; // Get the request body (if available)
    if (body) {
        try {
            const parsedBody = JSON.parse(body); // Try to parse JSON
            let bodyString = JSON.stringify(parsedBody);
            signPayload += bodyString
        } catch (e) {
            signPayload += body; // If it's not JSON, directly append the raw body
        }
    } else {
        console.log("Failed to process body data for POST method");
    }
}

// The signature uses the HMAC SHA256 algorithm, with the API-Secret corresponding to the API-KEY as the key for HMAC SHA256.
const crypto = require('crypto-js'); // Load the CryptoJS library
// Calculate the signature
let signature = crypto.HmacSHA256(signPayload, secretKey).toString(crypto.enc.Hex);

// Set up Headers
pm.variables.set('xChTs', timestampString);
pm.variables.set('xChSign', signature);
Return example

{}
HTTP status code types
The HTTP 4XX error codes are used to indicate errors in the request content, behavior, or format.
The HTTP 429 error code indicates a warning for exceeding the access rate limit, meaning the IP will be blocked soon.
HTTP 418 indicates that after receiving a 429 error, the client continued to make requests, resulting in being blocked.
The HTTP 5XX error codes indicate internal server errors; this means the problem is on the server side. When handling this error, never treat it as a failed task because the execution status is unknown—it could be either successful or failed.
HTTP 504 indicates that the API server has submitted a request to the business core but has not received a response. It is important to note that the 504 code does not represent a failed request, but rather an unknown status. It is likely that the request has been executed, but it may also have failed, requiring further confirmation.
Any API may return an ERROR. The error response payload is as follows:
Return example

{
  "code": -1121,
  "msg": "Invalid symbol."
}
For more details, refer to Response Code Types

Access restriction
Each API will have a rate limit description below it.
Violating the rate limit will result in receiving an HTTP 429 error, which is a warning.
When receiving an HTTP 429 warning, the caller should reduce the access frequency or stop accessing the service.
Time synchronization security
The signature interfaces require the timestamp to be passed in the HTTP header with the X-CH-TS field. Its value should be the Unix timestamp (in milliseconds) at the time the request is sent, e.g., 1528394129373.
When the server receives a request, it will check the timestamp in the request. If the timestamp is older than 5000 milliseconds, the request will be considered invalid. This time window value can be customized by sending the optional parameter recvWindow.
Additionally, if the server calculates that the client’s timestamp is more than one second ahead of the server’s time, the request will also be rejected.
Java Logical Pseudocode：

if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {
  // process request
} else {
  // reject request
}
Regarding Transaction Timeliness: The internet connection is not 100% reliable and cannot be fully depended on. Therefore, the latency from your local system to the exchange server will have fluctuations. This is the purpose of setting the recvWindow. If you are engaged in high-frequency trading and have higher requirements for transaction timeliness, you can adjust recvWindow flexibly to meet your needs. It is not recommended to use a recvWindow greater than 5 seconds.

Return Code Type
Description and Causes of Exception Codes and Error Codes

The following return content is for basic parameter validation. If the return code is not included in the return code types listed below, it indicates an error outside the business layer, and you need to contact technical personnel for resolution.
10XX - General Server and Network Errors
Code:-1000 UNKNOWN
Code	Tag	msg	Cause
1000	UNKNOWN	An unknown error occurred while processing the request	An unknown error occurred while processing the request
Code:-1001 DISCONNECTED
Code	Tag	msg	Cause
1001	DISCONNECTED	Internal error; unable to process your request. Please try again	Internal error; unable to process your request
Code:-1002 UNAUTHORIZED
Code	Tag	msg	Cause
1002	UNAUTHORIZED	You do not have permission to execute this request. The request requires an API Key. We recommend attaching X-CH-APIKEY in all request headers	The request header is missing X-CH-APIKEY
Code:-1003 TOO_MANY_REQUESTS
Code	Tag	msg	Cause
1003	TOO_MANY_REQUESTS	The request is too frequent and exceeds the limit	The request is too frequent and exceeds the limit
Code:-1004 NO_THIS_COMPANY
Code	Tag	msg	Cause
1004	NO_THIS_COMPANY	You do not have permission to execute this request. User does not exist	You do not have permission to execute this request. User does not exist
Code:-1006 UNEXPECTED_RESP
Code	Tag	msg	Cause
1006	UNEXPECTED_RESP	The received message does not conform to the preset format, and the order status is unknown	The received message does not conform to the preset format, and the order status is unknown
Code:-1007 TIMEOUT
Code	Tag	msg	Cause
1007	TIMEOUT	Timeout waiting for backend server response. Sending status unknown; execution status unknown	Request timeout
Code:-1014 UNKNOWN_ORDER_COMPOSITION
Code	Tag	msg	Cause
1014	UNKNOWN_ORDER_COMPOSITION	Unsupported order combination	The order combination does not exist or an incorrect order combination was entered
Code:-1015 TOO_MANY_ORDERS
Code	Tag	msg	Cause
1015	TOO_MANY_ORDERS	Too many orders. Please reduce the number of your orders	The order quantity exceeds the maximum limit
Code:-1016 SERVICE_SHUTTING_DOWN
Code	Tag	msg	Cause
1016	SERVICE_SHUTTING_DOWN	Server offline	The server is offline and the interface is unavailable
Code:-1017 NO_CONTENT_TYPE
Code	Tag	msg	Cause
1017	NO_CONTENT_TYPE	We recommend attaching Content-Type in all request headers and setting it to application/json	The request header is missing Content-Type
Code:-1020 UNSUPPORTED_OPERATION
Code	Tag	msg	Cause
1020	UNSUPPORTED_OPERATION	This operation is not supported	An incorrect request operation was made. You need to coordinate with the technical team to resolve the issue
Code:-1021 INVALID_TIMESTAMP
Code	Tag	msg	Cause
1021	INVALID_TIMESTAMP	Invalid timestamp, the time offset is too large	The timestamp offset is too large. The server determines that the client’s time is more than 1 second ahead of the server’s time based on the timestamp in the request
Code:-1022 INVALID_SIGNATURE
Code	Tag	msg	Cause
1022	INVALID_SIGNATURE	Invalid signature	Signature verification failed
Code:-1023 UNAUTHORIZED
Code	Tag	msg	Cause
1023	UNAUTHORIZED	You do not have permission to execute this request. The request requires a timestamp. We recommend attaching X-CH-TS in all request headers	The request header is missing X-CH-TS
Code:-1024 UNAUTHORIZED
Code	Tag	msg	Cause
1024	UNAUTHORIZED	You do not have permission to execute this request. The request requires a sign. We recommend attaching X-CH-SIGN in all request headers	The request header is missing X-CH-SIGN
11XX - Issue in the request content
Code:-1100 ILLEGAL_CHARS
Code	Tag	msg	Cause
1100	ILLEGAL_CHARS	Issue in the request content	Issue in the request content
Code:-1101 TOO_MANY_PARAMETERS
Code	Tag	msg	Cause
1101	TOO_MANY_PARAMETERS	Too many parameters sent	The parameter content is too large or duplicate parameter values have been detected
Code:-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED
Code	Tag	msg	Cause
1102	MANDATORY_PARAM_EMPTY_OR_MALFORMED	Mandatory parameter {0} was not sent, is empty, or has an incorrect format	The parameter is empty; a required parameter was not provided or has an incorrect input format
Code:-1103 UNKNOWN_PARAM
Code	Tag	msg	Cause
1103	UNKNOWN_PARAM	An unknown parameter was sent	The parameter content or format in the request is incorrect. Please check if the fields contain spaces
Code:-1104 UNREAD_PARAMETERS
Code	Tag	msg	Cause
1104	UNREAD_PARAMETERS	Not all sent parameters were read	Not all sent parameters were read; the parameter '%s' was read, but '%s' was sent
Code:-1105 PARAM_EMPTY
Code	Tag	msg	Cause
1105	PARAM_EMPTY	Parameter {0} is empty	A required parameter is empty
Code:-1106 PARAM_NOT_REQUIRED
Code	Tag	msg	Cause
1106	PARAM_NOT_REQUIRED	This parameter does not need to be sent	The parameter '%s' does not need to be sent
Code:-1111 BAD_PRECISION
Code	Tag	msg	Cause
1111	BAD_PRECISION	The precision exceeds the maximum value defined for this asset	The precision exceeds the maximum value defined for this asset
Code:-1112 NO_DEPTH
Code	Tag	msg	Cause
1112	NO_DEPTH	There are no open orders for the trading pair	The order to be canceled does not exist
Code:-1116 INVALID_ORDER_TYPE
Code	Tag	msg	Cause
1116	INVALID_ORDER_TYPE	Invalid order type	Invalid order type
Code:-1117 INVALID_SIDE
Code	Tag	msg	Cause
1117	INVALID_SIDE	Invalid buy/sell direction	Invalid buy/sell direction
Code:-1121 BAD_SYMBOL
Code	Tag	msg	Cause
1121	BAD_SYMBOL	Invalid contract	Incorrect trading pair name or contract name
Code:-1136 ORDER_QUANTITY_TOO_SMALL
Code	Tag	msg	Cause
1136	ORDER_QUANTITY_TOO_SMALL	The order quantity is less than the minimum value	The order quantity is less than the minimum value
Code:-1138 ORDER_PRICE_WAVE_EXCEED
Code	Tag	msg	Cause
1138	ORDER_PRICE_WAVE_EXCEED	The order price exceeds the allowed range	The order price exceeds the allowed range
Code:-1139 ORDER_NOT_SUPPORT_MARKET
Code	Tag	msg	Cause
1139	ORDER_NOT_SUPPORT_MARKET	This trading pair does not support market orders	This trading pair does not support market orders
Code:-1145 ORDER_NOT_SUPPORT_CANCELLATION
Code	Tag	msg	Cause
1145	ORDER_NOT_SUPPORT_CANCELLATION	The order status does not allow cancellation	The order cannot be canceled
Code:-1147 PRICE_VOLUME_PRESION_ERROR
Code	Tag	msg	Cause
1147	PRICE_VOLUME_PRESION_ERROR	Price or quantity precision exceeds the maximum limit	The order price or quantity exceeds the maximum limit
2XXX - Other related return codes
Code:-2013 NO_SUCH_ORDER
Code	Tag	msg	Cause
2013	NO_SUCH_ORDER	The order does not exist	The order does not exist
Code:-2015 REJECTED_API_KEY
Code	Tag	msg	Cause
2015	REJECTED_API_KEY	Invalid API key, IP, or operation permission	Signature or IP verification failed
Code:-2016 EXCHANGE_LOCK
Code	Tag	msg	Cause
2016	EXCHANGE_LOCK	Trading is frozen	The user's trading is frozen
Code:-2017 BALANCE_NOT_ENOUGH
Code	Tag	msg	Cause
2017	BALANCE_NOT_ENOUGH	Insufficient balance	The user’s account has an insufficient balance
Code:-2100 PARAM_ERROR
Code	Tag	msg	Cause
2100	PARAM_ERROR	Parameter issue	Parameter input error
Code:-2200 ORDER_CREATE_FAILS
Code	Tag	msg	Cause
2200	ORDER_CREATE_FAILS	Illegal IP	Not a trusted IP
Code:35
Code	Tag	msg	Cause
35		Order placement is prohibited	The user's trading may be restricted
Enumeration type
Trading pair
Value	Description
base	Refers to the trading asset of a trading pair, specifically the asset name that appears in the front part
quote	Refers to the pricing asset of a trading pair, specifically the asset name that appears in the latter part
Order status
Value	Description
New Order	Create a new order
Partially Filled	Partially filled
Filled	Fully filled
Cancelled	Canceled
To be Cancelled	Canceling
Partially Filled/Cancelled	Partially filled/Canceled
REJECTED	Order rejected
Order type
Value	Description
LIMIT	Limit order
MARKET	Market order
Order direction
Value	Description
BUY	Buy order
SELL	Sell order
K-line interval
Value	Description	Example
min	Minute	1min, 5min, 15min, 30min, 60min
h	Hour	1h, 4h
day	Day	1day
week	Week	1week
month	Month	
Spot trading
Public
Security type: None
Public-type interfaces can be accessed freely without an API key or signature
Test connection
GET https://openapi.fameex.com/sapi/v1/ping

Test the connectivity of the REST API

Request example

const https = require('https');

const url = 'https://openapi.fameex.com/sapi/v1/ping';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Return example

{}
Server time
GET https://openapi.fameex.com/sapi/v1/time

Get server time

Request example

const https = require('https');

const url = 'https://openapi.fameex.com/sapi/v1/time';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Return example

{
  "timezone": "China Standard Time",
  "serverTime": 1705039779880
}
Return parameters

parameter name	Type	Example	Description
timezone	string	China Standard Time	Server time zone
serverTime	long	1705039779880	Server timestamp

Currency Pair List
GET https://openapi.fameex.com/sapi/v1/symbols

Retrieve the set of currency pairs supported by the market

Request Example

const https = require('https');

const url = 'https://openapi.fameex.com/sapi/v1/symbols';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Return example

{
  "code": 0,
  "msg": "Success",
  "data": {
    "symbols": [
      {
        "symbol": "BTCUSDT",
        "baseAsset": "BTC",
        "quoteAsset": "USDT",
        "pricePrecision": 2,
        "quantityPrecision": 5,
        "limitMoneyMin": "1",
        "limitVolumeMin": "0.00001",
        "limitVolumeMax": "100",
        "limitMoneyMax": "1000000"
      },
      {
        "symbol": "LTCUSDT",
        "baseAsset": "LTC",
        "quoteAsset": "USDT",
        "pricePrecision": 2,
        "quantityPrecision": 3,
        "limitMoneyMin": "5",
        "limitVolumeMin": "0.001",
        "limitVolumeMax": "11509.049",
        "limitMoneyMax": "9000000"
      },
      {
        "symbol": "FILUSDT",
        "baseAsset": "FIL",
        "quoteAsset": "USDT",
        "pricePrecision": 3,
        "quantityPrecision": 2,
        "limitMoneyMin": "5",
        "limitVolumeMin": "0.89",
        "limitVolumeMax": "890000",
        "limitMoneyMax": "2000000"
      },
      {
        "symbol": "DOTUSDT",
        "baseAsset": "DOT",
        "quoteAsset": "USDT",
        "pricePrecision": 3,
        "quantityPrecision": 3,
        "limitMoneyMin": "5",
        "limitVolumeMin": "0.56",
        "limitVolumeMax": "560000",
        "limitMoneyMax": "2000000"
      },
      {
        "symbol": "XLMUSDT",
        "baseAsset": "XLM",
        "quoteAsset": "USDT",
        "pricePrecision": 4,
        "quantityPrecision": 1,
        "limitMoneyMin": "5",
        "limitVolumeMin": "12",
        "limitVolumeMax": "12000000",
        "limitMoneyMax": "2000000"
      }
    ]
  }
}
Return parameter

Parameter name	Type	Example	Description
symbol	string	btcusdt	Lowercasecurrency pair name
baseAsset	string	BTC	Base currency
quoteAsset	string	USDT	Quote currency
pricePrecision	integer	6	Price precision
quantityPrecision	integer	3	Quantity precision
limitMoneyMin	BigDecimal	0.0001	Minimum order amount limit for orders
limitVolumeMin	BigDecimal	0.0001	Minimum order quantity limit for orders
limitVolumeMax	BigDecimal	0.0001	Maximum order quantity limit for orders
limitMoneyMax	BigDecimal	0.0001	Maximum order amount limit for orders
Market data
Security type: None
The interfaces below the market data do not require an API key or signature for free access.
Order book
GET https://openapi.fameex.com/sapi/v1/depth

Get market order book depth information

Request parameters

Parameter name	Type	Description
symbol*	string	Uppercasecurrency pair name, for example:BTCUSDT
limit	integer	Default: 100; Maximum: 100
Request example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/sapi/v1/depth";
const QUERY_STRING = "?symbol=BTCUSDT&limit=100";

// Calculate the full request path
const REQUEST_PATH = REQUEST_URL + QUERY_STRING;
const FULL_URL = API_URL + REQUEST_PATH;

// **Print debug information**
console.log("==== Request information ====");
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });

Return example

{
  "code": 0,
  "msg": "Success",
  "data": {
    "time": 1764180842868,
    "bids": [
      [90058.6, 7.7918],
      [90058.59, 7.09332]
    ],
    "asks": [
      [90058.7, 4.35464],
      [90058.72, 3.95142]
    ]
  }
}
Return parameter

Parameter name	Type	Example	Description
time	long	1595563624731	Current timestamp
bids	array	[[3.9,43.1],[4.0,19.2]]	Order book bid information, the array length is 2, index 1 is the price, type is float; index 2 is the quantity corresponding to the current price, type is float
asks	array	[[4.0,12.0],[5.1,28.0]]	Order book ask information, the array length is 2, index 1 is the price, type is float; index 2 is the quantity corresponding to the current price, type is float
The information corresponding to bids and asks represents all the prices in the order book and the quantities corresponding to those prices, arranged from the best price (highest bid and lowest ask) downwards

Market Ticker
GET https://openapi.fameex.com/sapi/v1/ticker

Get 24-hour price change data

Request example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/sapi/v1/ticker";
const QUERY_STRING = "?symbol=BTCUSDT";

// Calculate the full request path
const REQUEST_PATH = REQUEST_URL + QUERY_STRING;
const FULL_URL = API_URL + REQUEST_PATH;

// **Print debug information**
console.log("==== Request information ====");
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });
Request parameters

Parameter name	Type	Description
symbol*	string	Uppercase currency pair name, for example: BTCUSDT
Return example

{
  "code": 0,
  "msg": "Success",
  "data": {
    "amount": 1357550713.60334,
    "high": 90267.9,
    "vol": 15520.54679,
    "last": 90253.5,
    "low": 86180.1,
    "buy": 90217.6,
    "sell": 90217.7,
    "rose": "+0.0295494912",
    "time": 1764180900000
  }
}
Return parameter

Parameter name	Type	Example	Description
time	long	1595563624731	Current timestamp
high	float	9900.51	Highest price
low	float	9100.34	Lowest price
last	float	9211.60	Latest trade price
vol	float	4691.0	Trading volume
amount	float	22400.0	Transaction Amount
buy	float	9210.0	Bid price
sell	float	9213.0	Ask price
rose	string	+0.05	Price change percentage,+indicates an increase,-indicates a decrease, and +0.05indicates a5% increase
Market Ticker-V2
GET https://openapi.fameex.com/v2/public/ticker

Get 24-hour price change data

Request example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/v2/public/ticker";

// Calculate the full request path
const REQUEST_PATH = REQUEST_URL;
const FULL_URL = API_URL + REQUEST_PATH;

// **Print debug information**
console.log("==== Request information ====");
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });
Response example

{
  "code": "0",
  "msg": "Succeed",
  "data": {
    "MNT_USDT": {
      "base_id": "MNT",
      "quote_volume": 3049025.662482,
      "quote_id": "USDT",
      "base_volume": 4123162.07,
      "isFrozen": 1,
      "last_price": 0.7491
    },
    "PEPE_USDT": {
      "base_id": "PEPE",
      "quote_volume": 19215044.55550406,
      "quote_id": "USDT",
      "base_volume": 2733395751472,
      "isFrozen": 1,
      "last_price": 0.00000731
    }
  },
  "message": null,
  "succ": true
}
Response parameters

Parameter name	Type	Example	Description
code	string	0	Return Code
msg	string	Succeed	Return information
message	string	null	error message
succ	boolean	true	Operation ID
data	object		
base_id	string	MNT	Trading Currency
quote_id	string	USDT	Denominated currency
base_volume	float	4123162.07	Trading Volume
quote_volume	float	3049025.662482	Transaction Amount
last_price	float	0.7491	Latest transaction price
isFrozen	number	1	Freeze flag

Recent transactions
GET https://openapi.fameex.com/sapi/v1/trades

Get recent transaction data

Request Example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/sapi/v1/trades";
const QUERY_STRING = "?symbol=BTCUSDT&limit=10";

// Calculate the complete request URL
const REQUEST_PATH = REQUEST_URL + QUERY_STRING;
const FULL_URL = API_URL + REQUEST_PATH;

// **Print debugging information**
console.log("==== Request information ====");
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });
Request parameters

Parameter name	Type	Description
symbol*	string	Capitalize the currency pair name, for example: BTCUSDT
limit	string	Default: 100; Maximum: 1000
Response example

{
  "code": 0,
  "msg": "Success",
  "data": [
    {
      "side": "BUY",
      "price": 90310.4,
      "qty": 0.06466,
      "time": 1764181079236
    },
    {
      "side": "BUY",
      "price": 90305.6,
      "qty": 0.51622,
      "time": 1764181078271
    }
  ]
}
Response parameters

Parameter name	Type	Example	Description
price	float	131.0000000000000000	Trading price
time	long	1704788645416	Current timestamp
qty	float	0.1000000000000000	Quantity (contracts)
side	string	buy/sell	Active order direction
K-line/Candlestick data
GET https://openapi.fameex.com/sapi/v1/klines

Get K-line data

Request Example

const axios = require("axios");
const crypto = require("crypto");

// API-related information
const API_URL = "https://openapi.fameex.com";
const REQUEST_URL = "/sapi/v1/klines";
const QUERY_STRING = "?symbol=BTCUSDT&interval=1min&limit=5";

// Calculate the complete request URL
const REQUEST_PATH = REQUEST_URL + QUERY_STRING;
const FULL_URL = API_URL + REQUEST_PATH;

// **Print debugging information**
console.log("==== Request information ====");
console.log("Request URL:", FULL_URL);
console.log("==================");

// Send GET request
const headers = {
  "Content-Type": "application/json",
};

axios
  .get(FULL_URL, { headers })
  .then((response) => {
    console.log("Response Code:", response.status);
    console.log("Response Body:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error.response ? error.response.data : error.message);
  });
Request parameters

Parameter name	Type	Description
symbol*	string	Uppercase trading pair name, e.g., BTCUSDT
interval*	string	K-line chart interval, acceptable values:1min,5min,15min,30min,60min,1day,1week,1month (min = minutes, day = days, week = weeks, month = months)
limit	integer	Default: 100; Maximum: 300
Return example

{
  "code": 0,
  "msg": "Success",
  "data": [
    {
      "high": 87754.2,
      "vol": 13.29173,
      "low": 87694.4,
      "idx": 1764175260000,
      "close": 87719.7,
      "open": 87739.7
    },
    {
      "high": 87723.1,
      "vol": 8.95014,
      "low": 87687.3,
      "idx": 1764175320000,
      "close": 87723.1,
      "open": 87719.7
    }
  ]
}
Response parameters

Parameter name	Type	Example	Description
idx	long	1538728740000	Start timestamp
open	float	6129.41	Opening price
close	float	6225.63	Closing price
high	float	6228.77	Highest price
low	float	6220.13	Lowest price
vol	float	2456.11	Trading volume








Contract trading
Public
Security type: None
The APIs under the public section can be freely accessed without an API key or signature.
Test connection
GET https://futuresopenapi.fameex.com/fapi/v1/ping

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/ping';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Response example

{}
Response parameters

{}

Test the connectivity of the REST API

Get server time
GET https://futuresopenapi.fameex.com/fapi/v1/time

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/time';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Response example

{
  "timezone": "China Standard Time",
  "serverTime": 1704962055664
}
Response parameters

Parameter name	Type	Example	Description
timezone	string	China Standard Time	Server timezone
serverTime	long	1607702400000	Server timestamp
Contract list
GET https://futuresopenapi.fameex.com/fapi/v1/contracts

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/contracts';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Response example

[
  {
    "symbol": "E-ETC-USDT",
    "pricePrecision": 3,
    "side": 1,
    "maxMarketVolume": 200000,
    "multiplier": 1.0,
    "minOrderVolume": 1,
    "maxMarketMoney": 500000.0,
    "type": "E",
    "maxLimitVolume": 300000,
    "maxValidOrder": 10,
    "multiplierCoin": "ETC",
    "minOrderMoney": 1.0,
    "maxLimitMoney": 500000.0,
    "status": 1
  },
  {
    "symbol": "E-ATOM-USDT",
    "pricePrecision": 3,
    "side": 1,
    "maxMarketVolume": 100000,
    "multiplier": 1.0,
    "minOrderVolume": 1,
    "maxMarketMoney": 200000.0,
    "type": "E",
    "maxLimitVolume": 200000,
    "maxValidOrder": 10,
    "multiplierCoin": "ATOM",
    "minOrderMoney": 20.0,
    "maxLimitMoney": 2000000.0,
    "status": 1
  }
]
Response parameters

Parameter name	Type	Example	Description
symbol	string	E-BTC-USDT	Uppercasecontract name
pricePrecision	number	3	Price precision
status	number	1	Contract status (0:Not tradable, 1:Tradable)
type	string	E	Contract type (E:Perpetual contract, S:Simulated contract, others areHybrid contract)
side	number	1	Contract direction (0:Inverse, 1:Linear)
multiplier	number	1.0000000000000000	Contract nominal value
minOrderVolume	number	1	Minimum order quantity
minOrderMoney	number	1.0000000000000000	Minimum order amount
maxMarketVolume	number	200000	Maximum order quantity for market orders
maxMarketMoney	number	500000.0000000000000000	Maximum order amount for market orders
maxLimitVolume	number	300000	Maximum order quantity for limit orders
maxLimitMoney	number	500000.0000000000000000	Maximum order amount for limit orders
maxValidOrder	number	10	Maximum number of active orders allowed
Market data
Security type: None
APIs under the market section can be freely accessed without an API key or signature
Order book
GET https://futuresopenapi.fameex.com/fapi/v1/depth

Market order book depth information

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/depth?contractName=E-BTC-USDT&limit=100';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Request parameters

Parameter name	Type	Description
contractName*	string	Uppercasecontract name, such asE-BTC-USDT
limit	integer	Default: 100; Maximum: 100
Response example

{
  "time": 1704962463000,
  "bids": [
    [
      3.9, //Price
      16.1 //Quantity
    ],
    [4.0, 29.3]
  ],
  "asks": [
    [
      4.000002, //Price
      12.0 //Quantity
    ],
    [5.1, 28.0]
  ]
}
Response parameters

Parameter name	Type	Example	Description
time	long	1595563624731	Current timestamp
bids	list	[[3.9,16.1],[4.0,29.3]]	Order book bid information, where the first element is the price (type: float), and the second element is the quantity corresponding to the current price (type: float)
asks	list	[[4.00000200,12.0],[5.1,28.0]]	Order book ask information, where the first element is the price (type: float), and the second element is the quantity corresponding to the current price (type: float)
The information corresponding to bids and asks represents all the prices and their associated quantities in the order book, arranged from the best price downwards

Market Ticker
GET https://futuresopenapi.fameex.com/fapi/v1/ticker

24-hour price change data

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/ticker?contractName=E-BTC-USDT';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Request parameters

Parameter name	Type	Description
contractName*	string	Uppercasecontract name, such asE-BTC-USDT
Return example

{
  "high": 56120.22,
  "vol": 51.21,
  "last": 55989.93,
  "low": 55982.24,
  "buy": 55988.1,
  "sell": 55990.1,
  "rose": "+0.05",
  "time": 1704966225000
}
Response parameters

Parameter name	Type	Example	Description
time	long	1595563624731	Timestamp
high	float	56120.22	Highest price
low	float	55982.24	Lowest price
last	float	55989.93	Latest price
vol	float	51.21	Trading volume
rose	string	+0.05	Price change percentage.+indicates an increase,-indicates a decrease, and+0.05means a5%increase
buy	float	55988.10	Buy price (highest bid price)
sell	float	55990.10	Sell price (lowest ask price)
Market Ticker-V2
GET https://futuresopenapi.fameex.com/swap-api/v2/tickers

Get 24-hour price change data

Request example

Return example

[
  {
    "base_currency": "ETH",
    "open_interest_usd": "3158506.047",
    "quote_volume": "475254656162",
    "base_volume": "2135453.51",
    "open_interest": "1372.13",
    "index_price": "2302.705",
    "basis": "0.0003",
    "quote_currency": "USDT",
    "ticker_id": "ETH-USDT",
    "funding_rate": "0.0000632068687814",
    "high": "2318.84",
    "product_type": "Perpetual",
    "low": "2160.71",
    "ask": "2301.96",
    "next_funding_rate_timestam": 1741248000000,
    "bid": "2301.8",
    "last_price": "2301.9"
  }
]
Return parameter

Name	Type	Example	Description
ticker_id	string	ETH-USDT	Trading Pairs
product_type	string	Perpetual	Contract Type
base_currency	string	ETH	Trading Currency
quote_currency	string	USDT	Denominated currency
last_price	float	2301.9	Latest transaction price
index_price	float	2302.705	Index Price
base_volume	float	2135453.51	Trading Volume
quote_volume	string	475254656162	Transaction Amount
bid	float	2301.8	Buy one price
ask	float	2301.96	Selling price
high	float	2318.84	Highest Price
low	float	2160.71	Lowest Price
open_interest	float	1372.13	Number of open positions
open_interest_usd	float	3158506.047	Opening amount
basis	float	0.0003	Basis
funding_rate	float	0.0000632068687814	Funding Rate
next_funding_rate_timestam	float	1741248000000	Next funding rate time
Get index/mark price
GET https://futuresopenapi.fameex.com/fapi/v1/index

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/index?contractName=E-BTC-USDT&limit=100';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Request parameters

Parameter name	Type	Description
contractName*	string	Uppercasecontract name, such asE-BTC-USDT
limit	string	Default: 100; Maximum: 1000
Return example

{
  "currentFundRate": -0.00375,
  "indexPrice": 27905.98,
  "tagPrice": 27824.4422146875,
  "nextFundRate": -0.00375
}
Response parameters

Name	Type	Example	Description
indexPrice	float	27905.9800000000000000	Index price
tagPrice	float	27824.4422146875000000	Mark price
nextFundRate	float	-0.0037500000000000	Funding rate price
currentFundRate	float	-0.0037500000000000	Previous funding rate (used for this period's settlement)
K-line / Candlestick chart data
GET https://futuresopenapi.fameex.com/fapi/v1/klines

Request example

const https = require('https');

const url = 'https://futuresopenapi.fameex.com/fapi/v1/klines?contractName=E-BTC-USDT&interval=1min&limit=100&startTime=1739116800000&endTime=1739852318000';

https.get(url, (res) => {
  let data = '';

  // A chunk of data has been received.
  res.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  res.on('end', () => {
    console.log("Response:", data);
  });

}).on('error', (err) => {
  console.log('Request error:', err.message);
});
Request parameters

Parameter name	Type	Description
contractName*	string	Uppercasecontract name, such asE-BTC-USDT
interval*	string	The time intervals for K-line charts, recognizable parameter values are:1min,5min,15min,30min,1h,1day,1week,1month(min = minute, h = hour, day = day, week = week, month = month)
limit	integer	默认：100；最大：300
startTime	long	Start timestamp
endTime	long	End timestamp
Response example.

[
  {
    "high": 6228.77,
    "vol": 111,
    "low": 6190.48,
    "idx": 15946403400000,
    "close": 6210.51,
    "open": 6195.8
  },
  {
    "high": 6228.77,
    "vol": 222,
    "low": 6228.77,
    "idx": 15876321600000,
    "close": 6228.77,
    "open": 6228.77
  },
  {
    "high": 6228.77,
    "vol": 333,
    "low": 6228.77,
    "idx": 15876321000000,
    "close": 6228.77,
    "open": 6228.77
  }
]
Response parameters

Parameter name	Type	Example	Description
idx	long	15946403400000	Start timestamp
open	float	6195.80	Opening price
close	float	6210.51	Closing price
high	float	6228.77	Highest price
low	float	6190.48	Lowest price
vol	float	111	Volume traded







ebsocket
Overview
WebSocket is a new protocol in HTML5. It enables full-duplex communication between the client and the server, allowing data to be transmitted quickly in both directions. A connection between the client and the server can be established through a simple handshake, and the server can actively push information to the client based on business rules. Its advantages are as follows:

The request header information is relatively small, about 2 bytes, when transmitting data between the client and the server.
Both the client and the server can actively send data to each other.
There is no need to create and destroy TCP requests multiple times, saving bandwidth and server resources.
It is strongly recommended that developers use the WebSocket API to get market data, such as market prices and order book depth.
Spot
Basic Information
url：wss://wsapi.fameex.com/v1/ws/stream/public。
Response example

{
  "event_rep": "",
  "channel": "system",
  "data": {
    "status": "ready"
  },
  "tick": null,
  "ts": "1766066323820",
  "status": "ok"
}
Heartbeat
To keep the connection active and stable, it is recommended to perform the following actions:

After receiving each message, the user should set a timer with a duration of N seconds, where N is less than 30.

If the timer is triggered (i.e., no new message is received within N seconds), send the string 'ping'.

You should expect a text string 'pong' as a response. If no response is received within N seconds, trigger an error or reconnect.

Heartbeat example

{
  "event": "heartbeat",
  "params": {
    "channel": "ping"
  }
}
Response example

{
  "event_rep": "",
  "channel": "",
  "data": {
    "channel": "pong"
  },
  "tick": null,
  "ts": "1766061007743",
  "status": "ok"
}
Subscription / Unsubscription Parameters
Kline interval suffixes

Seconds: 1s
Minutes: 1m, 3m, 5m, 15m, 30m
Hours: 1h, 2h, 4h, 6h, 8h, 12h
Days: 1d, 3d
Weeks: 1w
Months: 1M
event	channel	description
sub	market_${symbol}_depth_step	Subscribe incremental order book depth
unsub	market_${symbol}_depth_step	Unsubscribe incremental order book depth
sub	market_${symbol}_trade	Subscribe real-time trades
unsub	market_${symbol}_trade	Unsubscribe real-time trades
sub	market_${symbol}_ticker	Subscribe 24h market ticker
unsub	market_${symbol}_ticker	Unsubscribe 24h market ticker
sub	market*${symbol}_kline*${interval}	Subscribe ${interval} real-time Kline data
unsub	market*${symbol}_kline*${interval}	Unsubscribe ${interval} real-time Kline data
sub	market_${symbol}_kline_1M	Subscribe 1-month historical Kline data
unsub	market_${symbol}_kline_1M	Unsubscribe 1M real-time Kline data
Subscription
Subscribe Incremental Order Book Depth
Subscription example

{
  "event": "sub",
  "params": {
    "channel": "market_${symbol}_depth_step", // ${symbol}, E.g. btcusdt
    "cb_id": "1" // Business ID, optional
  }
}
Response example

{
  "event_rep": "",
  "channel": "market_btcusdt_depth_step",
  "data": null,
  "tick": {
    "pair": "BTCUSDT",
    "bids": [
      // Buy orders
      ["87263.1", "0.1"],
      ["87263.09", "0.1"]
    ],
    "asks": [
      // Sell orders
      ["85528.97", "0.1"],
      ["85554.73", "0.1"]
    ],
    "pre_update_id": "9164837",
    "last_update_id": "9164840"
  },
  "ts": "1766062757172",
  "status": "ok"
}
How to Properly Maintain a Local Order Book Copy
Open a WebSocket connection to wss://wsapi.fameex.com/v1/ws/stream/public and subscribe to the incremental depth channel.
Begin buffering the received events. Record the last_update_id value from the first event you receive.
Fetch the depth snapshot from https://spotapi.fameex.com/spot/v1/market/orderbook?symbol=${symbol}.
If the update_id in the snapshot is less than or equal to the last_update_id value from step 2, return to step 3.
From the received events, discard all events where last_update_id <= the update_id in the snapshot. Now the first event's last_update_id should be within the [pre_update_id; last_update_id] range.
Set your local order book to the snapshot. Its update ID is update_id.
Apply all buffered events, as well as all subsequent events.
To Apply an Event to Your Local Order Book, Follow This Update Process:
Determine whether the event needs to be processed:
If the event's last update ID (last_update_id) is less than the local order book's update ID (update_id), ignore the event.
If the event's first update ID (pre_update_id) is greater than the local order book's update ID plus 1, it means you have missed some events. Discard your local order book and resync from the beginning.
Typically, the next event's pre_update_id equals the previous event's last_update_id + 1.
Set the order book's update ID (update_id) to the last update ID (last_update_id) of the processed event.
Subscribe Real-time Trades
Subscription example

{
  "event": "sub",
  "params": {
    "channel": "market_${symbol}_trade", // ${symbol}, E.g. btcusdt
    "cb_id": "1" // Business ID, optional
  }
}
Response example

{
  "event_rep": "",
  "channel": "market_btcusdt_trade",
  "data": [
    {
      "amount": "22790.07645", // Total amount
      "ds": "",
      "price": "87671.00", // Price
      "side": "SELL", // Trade side: buy, sell
      "ts": "1766063060107",
      "vol": "0.25995" // Quantity
    }
  ],
  "tick": null,
  "ts": "1766063061126",
  "status": "ok"
}
Subscribe Kline Market Data
Subscription example

{
  "event": "sub",
  "params": {
    // ${symbol}, E.g. btcusdt
    // ${interval}, E.g. 1min/5min/15min/30min/60min/1day/1week/1
    "channel": "market_${symbol}_kline_${interval}",
    "cb_id": "1" // Business ID, optional
  }
}
Response example

{
  "event_rep": "",
  "channel": "market_btcusdt_kline_1m",
  "data": null,
  "tick": {
    "amount": "1701994.52252",
    "close": "88291.70", // Close price
    "ds": "",
    "high": "88328.90", // High price
    "ts": "1766065020000",
    "low": "88169.40", // Low price
    "open": "88211.60", // Open price
    "vol": "19.2841" // Trading volume
  },
  "ts": "1766065072255",
  "status": "ok"
}
Subscribe 24h Market Ticker
Subscription example

{
  "event": "sub",
  "params": {
    "channel": "market_${symbol}_ticker", // ${symbol}, E.g. btcusdt
    "cb_id": "1" // Business ID, optional
  }
}
Response example

{
  "event_rep": "",
  "channel": "market_btcusdt_ticker",
  "data": null,
  "tick": {
    "amount": "1080601292.38171", // Trading amount
    "close": "88953.30", // Close price
    "high": "90364.3", // High price
    "low": "85312.9", // Low price
    "open": "87507.60", // Open price
    "rose": "0.0172601894", // Price change rate
    "vol": "12398.36035" // Trading volume
  },
  "ts": "1766065787125",
  "status": "ok"
}
Futures
Basic information
The basic contract market data endpoint：wss://futuresws.fameex.com/kline-api/ws。
The basic contract market data backup endpoint：wss://futuresws.fameex.net/kline-api/ws。
The returned data, except for heartbeat data, will be compressed in binary format (users need to decompress it using the Gzip algorithm).
Heartbeat
To keep the connection active and stable, it is recommended to perform the following actions:

After receiving each message, the user should set a timer with a duration of N seconds, where N is less than 30.

If the timer is triggered (i.e., no new message is received within N seconds), send the string 'ping'.

You should expect a text string 'pong' as a response. If no response is received within N seconds, trigger an error or reconnect.

The heartbeat response

{
  "pong": 15359750
}
Demo
Websocket Demo

Subscribe/Unsubscribe Parameters
event	channel	description
sub	market_$symbol_depth_step0	Subscribe to Depth
unsub	market_$symbol_depth_step0	Unsubscribe from Depth
sub	market_$symbol_trade_ticker	Subscribe to Real-time Trades
unsub	market_$symbol_trade_ticker	Unsubscribe from Real-time Trades
sub	market_$symbol_ticker	Subscribe to 24h Market Data
unsub	market_$symbol_ticker	Unsubscribe from 24h Market Data
sub	market_$symbol_kline_1min	Subscribe to 1-Minute Real-time Kline Data
req	market_$symbol_kline_1month	Request 1-Month Historical Kline Data
Subscribe
Subscribe to full depth
Subscription Example

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_depth_step0", // $symbol E.g. Spot trading：btcusdt Futures：e_btcusdt
    "cb_id": "1" // Business ID is optional
  }
}
Return example

{
  "channel": "market_btcusdt_depth_step0",
  "ts": 1506584998239,
  "tick": {
    "asks": [
      //Sell order
      [10000.19, 0.93],
      [10001.21, 0.2],
      [10002.22, 0.34]
    ],
    "buys": [
      //Buy order
      [9999.53, 0.93],
      [9998.2, 0.2],
      [9997.19, 0.21]
    ]
  }
}
Subscribe to real-time trades
Subscription Example

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_trade_ticker", // $symbol E.g. Spot trading: btcusdt，Futures: e_btcusdt
    "cb_id": "1" // Business ID is optional
  }
}
Response example

{
  "channel": "market_$symbol_trade_ticker",
  "ts": 1506584998239, // Request time
  "tick": {
    "id": 12121, // The "maximum transaction ID in the data"
    "ts": 1506584998239, // The "maximum timestamp in the data"
    "data": [
      {
        "side": "buy", // Buy/Sell Direction
        "price": 32.233, // Unit Price
        "vol": 232, // Quantity
        "amount": 323, // Total Amount
        "ds": "2017-09-1023: 12: 21"
      }
    ]
  }
}
Subscribe to K-line market data
Subscription example

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]", // $symbol E.g. btcusdt
    "cb_id": "1" // Business ID is optional
  }
}
Return example

{
  "channel": "market_$symbol_kline_1min", // 1min represents 1-minute candlestick
  "ts": 1506584998239, // Request time
  "tick": {
    "id": 1506602880, // The starting value of the time scale
    "vol": 1212.12211, // Trading volume
    "open": 2233.22, // Opening price
    "close": 1221.11, // Closing price
    "high": 22322.22, // Highest price
    "low": 2321.22 // Lowest price
  }
}
Subscribe to 24h market ticker
Subscription Example

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_ticker", // $symbol E.g. 币币：btcusdt Futures：e_btcusdt
    "cb_id": "1" // Business ID is optional
  }
}
Response example

{
  "channel": "market_$symbol_ticker",
  "ts": 1506584998239, // Request time
  "tick": {
    "amount": 123.1221, // Trading volume
    "vol": 1212.12211, // Trading volume
    "open": 2233.22, // Opening price
    "close": 1221.11, // Closing price
    "high": 22322.22, // Highest price
    "low": 2321.22, // Lowest price
    "rose": -0.2922 // Price change or percentage change
  }
}
Request Historical K-line Data
Subscription Example

{
  "event": "req",
  "params": {
    "channel": "market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]",
    "cb_id": "1",
    "endIdx": "1506602880", // Return the previous pageSize number of records before endIdx. This is optional
    "pageSize": 100 // Optional
  }
}
Response example

{
  "event_rep": "rep",
  "channel": "market_$symbol_kline_5min",
  "cb_id": "Return the same way",
  "ts": 1506584998239, // Request time
  "data": [
    // Up to 300 entries
    {
      "id": 1506602880, // The starting value of the time scale
      "amount": 123.1221, // Trading volume
      "vol": 1212.12211, // Trading volume
      "open": 2233.22, // Opening price
      "close": 1221.11, // Closing price
      "high": 22322.22, // Highest price
      "low": 2321.22 // Lowest price
    },
    {
      "id": 1506602880, // The starting value of the time scale
      "amount": 123.1221, // Trading volume
      "vol": 1212.12211, // Trading volume
      "open": 2233.22, // Opening price
      "close": 1221.11, // Closing price
      "high": 22322.22, // Highest price
      "low": 2321.22 // Lowest price
    }
  ]
}
Request transaction records
Request example

{
  "event": "req",
  "params": {
    "channel": "market_$symbol_trade_ticker", // $symbol E.g. Spot trading：btcusdt Futures：e_btcusdt
    "cb_id": "1" // Business ID is optional
  }
}
Response example

{
  "event_rep": "rep",
  "channel": "market_$symbol_trade_ticker",
  "cb_id": "Return along the original route",
  "ts": 1506584998239,
  "status": "ok",
  "data": [
    {
      "side": "buy", // Order direction:buy，sell
      "price": 32.233, // Unit Price
      "vol": 232, // Quantity
      "amount": 323 // Total Amount
    },
    {
      "side": "buy", // Order direction:buy，sell
      "price": 32.233, // Unit Price
      "vol": 232, // Quantity
      "amount": 323 // Total Amount
    }
  ]
}
SDK development library
Java
JAVA Demo

"Frequently Asked Questions" (FAQ)
What is the maximum allowable time difference between the timestamp parameter in the API request and the server's received time?
When the server receives a request, it checks the timestamp in the request. If the timestamp is from more than 5000 milliseconds ago, the request is considered invalid. This time window can be customized by sending the optional parameter recvWindow.

The request header 'X-CH-TS' cannot be empty. How to resolve this?
First, it is recommended to print theX-CH-TSheader. When an exception occurs, check ifX-CH-TSis empty. Additionally, it is suggested to optimize the code by checking ifX-CH-TSis empty before each request.

Why does the signature authentication always return an invalid signature?
You can print the request header information and the string before signing. Key points to focus on are as follows:

Compare your request headers with the following sample request headers one by one
Example of request headers：

Content-Type: application/json

X-CH-APIKEY: 44c541a1-****-****-****-10fe390df2

X-CH-SIGN: ssseLeefrffraoEQ3yI9qEtI1CZ82ikZ4xSG5Kj8gnl3uw=

X-CH-TS: 1574327555669
Is the API key correctly configured in the program?

Does the string before signing conform to the standard format? The order of all elements must remain consistent. You can copy the following example and compare it with your string before signing：

GET example

POST example

Why does the API return ILLEGAL_CONTENT_TYPE(-1017)?
We recommend attachingContent-Typein all request headers and setting it to'application/json'

Is there a limit on the API call frequency per second?
There is a limit. You can refer to the documentation for the access frequency limits of each API

What is the basis for the API access frequency limit?
Personal data access is limited based on the*API-key, while public data access is limited based on theIP. It is important to note that if a user provides valid personal information when requesting public data, the limit will be based on theAPI-key*

How is HTTP status code 429 caused?
Requesting the API exceeds the access frequency limit. It is recommended to reduce the access frequency.

Will the IP be blocked if the API call exceeds the access frequency limit? How long will the block last?
Under normal circumstances, the IP will not be blocked. Reducing the access frequency should resolve the issue.

Why did the WebSocket connection get disconnected?
The WebSocket connection was disconnected because the heartbeat was not added. The client needs to send a pong message to maintain the connection stability
The WebSocket connection may be disconnected due to network issues, such as the client sending a pong message that the server did not receive, or other network-related causes.
It is recommended that users implement a WebSocket reconnection mechanism, so that the program can automatically reconnect if the heartbeat (ping/pong) connection is unexpectedly disconnected.
Why does the user get a Time Out error when requesting the API?
Why does the user get a Time Out error when requesting the API?

How to get all the trading pairs from the platform?
You can get all the trading pairs from the/sapi/v1/symbolsendpoint in spot trading.

Is there a limit on the number of orders or cancellations that can be processed in bulk?
Yes. The bulk API has a limit of 10 orders.

What is newClientOrderId and what is its purpose?
newClientOrderId is a custom order ID that you can use to identify your order. After placing the order, you can use the newClientOrderId and call the "Order Information" API to check the order status.
The user needs to ensure that this ID is unique, as we do not perform duplicate checks. If there are duplicates, only the most recent order can be canceled or queried when performing cancel or order status operations.
How to get the latest transaction price?
You can get the latest transaction price by fetching the Ticker information. The 'last' value in the returned result is the latest trade price.

Can the 24-hour trading volume in the Ticker API show negative growth?
Yes, it can. The 24-hour trading volume is a rolling data (with a 24-hour sliding window), and it is possible for the cumulative trading volume and trading value in the later window to be smaller than in the previous window.
## REST Trades Recovery
Tested on 2026-02-26. The endpoint /api/v2/trades and /v2/public/trades/market_pair require API keys (returns code -1002). There is NO PUBLIC REST TRADES endpoint for FameEX Futures.
