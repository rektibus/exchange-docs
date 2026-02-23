Spot Trading
API for spot trading by regular users

Preparation for Access
Trading Pairs
A trading pair consists of a base currency and a quote currency. For example, in the trading pair BTC/USDT, BTC is the base currency and USDT is the quote currency.

Applying for an API Key
To apply for an API Key, access the Hibt app on your mobile device, go to the personal settings page, and find the API management section. After successful creation, be sure to note the following information:

Access Key: The API access key

Secret Key: The key used for signature authentication and encryption (only visible during application)

API Authentication
Public APIs are used for retrieving basic information and market data. Public APIs do not require authentication to be called.

Private APIs are used for trading and account management. Each private request must be signed using your API Secret Key for verification.

REST API
https://api.hibt0.com/user-open-api

Signature Authentication
Private interfaces, except for public ones (such as basic information and market data), must use your API Key for encryption to verify whether the parameters or parameter values have been altered during transmission. Each API Key needs to have the appropriate permissions to access the corresponding interfaces. Every newly created API Key must be assigned permissions. Before using an interface, make sure your API Key has the required permissions.

The contents required for a valid request are as follows:

Method request URL: For example, https://api.hibt0.com/open-api/v1/trade/order.

API access key (X-ACCESS-KEY): The Access Key from the API Key you applied for.

Request timestamp (X-TIMESTAMP): The millisecond timestamp at the time of the request, used during the signature process.

Required and optional parameters: Each method has a set of required and optional parameters that define the API call. You can view these parameters and their meanings in the description of each method.

Signature: The value calculated via encryption to ensure the signature is valid and has not been tampered with. For the security of your API Key, the signature for parameters expires 5 minutes after generation.

Signature Required Parameter: For interfaces requiring signature authentication, the reqTime parameter must be included (its value is the latest server time, which can be obtained via the **/v1/common/systemTime** interface).

Encryption Method
To calculate the signature, the request must be normalized first, because when using HMAC for signature calculation, the result will be completely different for different contents. Therefore, before performing the signature calculation, please normalize the request. The following is an example of a request to query the details of an order:

Order request URL:


Copy
https://api.hibt0.com/user-open-api/v1/trade/order?amount=0.12&direction=ASK&price=7126.4285&symbol=BTC/USDT&reqTime=1672502400000
Sort the parameters in ASCII order and include the request timestamp timestamp:


Copy
amount=0.12&direction=ASK&price=7126.4285&reqTime=1672502400000&symbol=BTC/USDT&timestamp=1672502400000
Use the secretKey to encrypt the sorted request parameters using HMAC SHA256, resulting in:


Copy
550ac73ace8c34372e0e1dd6631e890c7bd16697af8bb4e2908e966b50aba4e0
Constructing HTTP Requests

Use X-ACCESS-KEY to store the access key information and pass it in the header as a parameter.

Use X-SIGNATURE to store the generated signature and pass it in the header as a parameter.

Use X-TIMESTAMP to store the request timestamp and pass it in the header as a parameter.

Request Methods

Currently, there are only two methods: GET and POST.

GET requests: All parameters are included in the path parameters.

POST requests: All parameters are sent in the request body in form-data format.

Response Format

All APIs return data in JSON format. At the top level of the JSON response, there are three fields: message, code, and data. The first two fields represent the request status and information, while the actual business data is contained in the data field.


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}
Common Error Codes
1xxx (Access Failure)
2xxx (Business Failure)
Error Code
Description
0

Success

1001

API request rate limit exceeded

1101

API Key authentication failed

1102

Secret key decryption failed

1103

Access IP not in the whitelist

2001

Parameter is empty

2002

Time range error

2003

Request time parameter is empty

2004

Request time expired

2101

Account does not exist

2102

API Key does not exist

2103

Trading pair does not exist

2201

User API Key disabled

2202

IP disabled

2203

API expired

2204

Insufficient API permissions

9999

Other exceptions, refer to message

Spot API
Basic Information API
Server Time

HTTP Request

GET /v1/common/systemTime

Authentication: No

Rate Limit: 100 requests/second

Request Parameters

This endpoint does not accept any parameters.

Response Fields

Field Name
Data Type
Description
data

long

Server timestamp


Copy
{
  "message": "success",
  "code": "0",
  "data": 1672502400000
}
All Trading Pair Information
HTTP Request

GET /v1/common/symbols

Authentication: No

Rate Limit: 5 requests/second

Request Parameters

This endpoint does not accept any parameters.

Response Fields

Field Name
Data Type
Description
symbol

string

Trading pair

baseCoinScale

integer

Precision for the quoted currency

coinScale

integer

Precision for the base currency

priceScale

integer

Price precision

baseSymbol

string

Base currency

coinSymbol

string

Quote currency

minTurnover

decimal

Minimum order transaction amount

minVolume

decimal

Minimum order quantity

maxVolume

decimal

Maximum order quantity

enable

integer

Whether trading is supported (0-No; 1-Yes)

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "symbol": "BTC/USDT", // Trading pair
      "baseCoinScale": 4, // Precision of quote currency amount
      "coinScale": 4, // Precision of base currency amount
      "priceScale": 2, // Price precision
      "baseSymbol": "USDT", // Quote currency
      "coinSymbol": "BTC", // Base currency
      "minTurnover": 10, // Minimum order value
      "minVolume": 0.001, // Minimum order quantity
      "maxVolume": 50, // Maximum order quantity
      "enable": 1 // Whether it is enabled
    },
    {
      "symbol": "ETH/USDT",
      "baseCoinScale": 4,
      "coinScale": 4,
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "minTurnover": 10,
      "minVolume": 0.01,
      "maxVolume": 500,
      "enable": 1
    }
  ]
}
Latest Trade Price
This endpoint provides the latest trade price for a trading pair.

HTTP Request

GET /v1/market/ticker/price

Authentication: No

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

Response Fields

Field Name
Data Type
Description
tickerPrice

decimal

Latest trade price

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": {
    "tickerPrice": 40000
  }
}
K-Line Data
HTTP Request

POST /v1/market/kline

Authentication: No

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

true

Trading pair

period

string

true

Time intervals: "1min", "5min", "15min", "30min", "60min", "4hour", "1day", "1week", "1mon", "1year"

size

int

false

Number of data points to retrieve, default is 100, max is 500

from

long

true

Start time (ms)

to

long

true

End time (ms)

Response Fields

Field Name
Data Type
Description
openPrice

decimal

Opening price

highestPrice

decimal

Highest price

lowestPrice

decimal

Lowest price

closePrice

decimal

Closing price

time

long

K-line timestamp (ms)

volume

decimal

Trading volume

turnover

decimal

Trading turnover

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "openPrice": "123456",
      "highestPrice": "45678",
      "lowestPrice": 0.5,
      "closePrice": 0.1,
      "volume": 0.1,
      "time": 1672502400000,
      "turnover": 1.2
    }
  ]
}
Order Book Depth Data
This endpoint returns the current order book depth data for a specified trading pair.

HTTP Request

GET /v1/market/depth

Authentication: No

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
Value Range
symbol

string

Yes

Trading pair

depth

integer

Yes

Number of depth levels to return

Maximum 50 levels

Response Fields

Field Name
Data Type
Description
symbol

string

Trading pair

bids

array

Buy order book depth list

asks

array

Sell order book depth list

timestamp

datetime

Time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": {
      "symbol" : "BTC/USDT",
      "timestamp" : "1723199363658",
      "bids" : [ [ "36074.99", "0.27225537" ], [ "36074.81", "0.00967628" ] ],
      "asks" : [ [ "36075.06", "0.55858424" ], [ "36075.24", "0.22475193" ] ]
  }
}
Account Balance
This endpoint returns the balance information for a specified currency.

HTTP Request

POST /v1/account/balance

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
coin

string

No

Currency

Response Fields

Field Name
Data Type
Description
coin

string

Currency

balance

decimal

Available balance

frozenBalance

decimal

Frozen balance

isLock

string

Whether locked

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "coin": "USDT",
      "balance": 1000,
      "frozenBalance": 1000,
      "isLock": "IS_FALSE"
    },{
      "coin": BTC,
      "balance": 1,
      "frozenBalance": 0.01,
      "isLock": "IS_TRUE"
    }
  ]
}
Bill List
This endpoint returns the bill list data for a specified currency.

HTTP Request

POST /v1/account/bill

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
coin

string

Yes

Currency

startTime

long

Yes

Start time (ms)

endTime

long

Yes

End time (ms)

Response Fields

Field Name
Data Type
Description
uid

long

User UID

firstLevelBillType

string

Primary bill type, e.g., 2 for trades

secondLevelBillType

string

Secondary bill type name, e.g., 1 for deposit, 4 for spot buy, 5 for spot sell

tradeType

int

Trade type; e.g., 1 for spot trading

amount

decimal

Amount

coinUnit

string

Currency

createTime

long

Creation time (ms)

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "uid": "123456",
      "firstLevelBillType": 2,
      "secondLevelBillType: 4,
      "tradeType: 1,
      "amount: 15.00,
      "coinUnit": "USDT",
      "createTime": 1672502400000
    }
  ]
}
Current Orders
HTTP Request

POST /v1/trade/openOrder

Authentication: Yes

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

direction

integer

Yes

Order direction (0-Buy; 1-Sell)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

price

decimal

Order price

avgPrice

decimal

Average trade price

amount

decimal

Order quantity

tradedAmount

decimal

Quantity traded

turnover

decimal

Trade amount (traded quantity * trade price)

symbol

string

Trading pair

baseSymbol

string

Quote currency

coinSymbol

string

Base currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-Pending; 1-Completed; 2-Canceled; 3-Expired; 4-Partially Filled)

type

integer

Type (0-Market; 1-Limit)

completedTime

long

Order completion time

canceledTime

long

Order cancellation time

time

long

Order creation time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677194831589408768",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 0,
      "amount": 0.1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677269378757951488",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 0,
      "amount": 1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Historical Orders (Within 3 Months)
HTTP Request

POST /v1/trade/history

Authentication: Yes

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

startTime

long

Yes

Start time (ms)

endTime

long

Yes

End time (ms)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

price

decimal

Order price

avgPrice

decimal

Average trade price

amount

decimal

Order quantity

tradedAmount

decimal

Quantity traded

turnover

decimal

Trade amount (traded quantity * trade price)

symbol

string

Trading pair

baseSymbol

string

Quote currency

coinSymbol

string

Base currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-Pending; 1-Completed; 2-Canceled; 3-Expired; 4-Partially Filled)

type

integer

Type (0-Market; 1-Limit)

completedTime

long

Order completion time

canceledTime

long

Order cancellation time

time

long

Order creation time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677226372826791936",
      "price": 35000,
      "avgPrice": 35000,
      "amount": 0.1,
      "tradedAmount": 0.1,
      "turnover": 3500,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677261905426776064",
      "price": 2000,
      "avgPrice": 2000,
      "amount": 1,
      "tradedAmount": 1,
      "turnover": 2000,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Spot Order Placement
HTTP Request

POST /v1/trade/order

Authentication: Yes

Rate Limit: 20 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

price

decimal

Yes

Price (set to 0 for market orders)

amount

decimal

Yes

Quantity (Market Buy: amount in quote currency, e.g., USDT; Market Sell: quantity of base currency to sell)

direction

integer

Yes

Direction (0-Buy; 1-Sell)

type

integer

Yes

Type (0-Market; 1-Limit)

Response Fields

Field Name
Data Type
Description
data

string

Order ID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": "E1677226372826791936"
}
Cancel Order
HTTP Request

POST /v1/trade/cancel

Authentication: Yes

Rate Limit: 20 requests/second

Request Parameters

Parameter
Data Type
Required
Description
orderId

string

Yes

Order ID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}
Rebate List
HTTP Request

POST /v1/account/rebateInfo

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Response Fields

Field Name
Data Type
Description
invitedUID

long

Invited user's UID

parentUID

long

Inviter's (parent) UID

createTime

long

Creation time (ms)

coin

string

Rebate coin type

rebateAmount

decimal

Rebate amount

rebateUsdtAmount

decimal

Rebate amount in equivalent USDT

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "invitedUID": "123456",
      "parentUID": "45678",
      "coin": "BTC",
      "rebateAmount": 0.1,
      "rebateUsdtAmount": 0.1,
      "createTime": 1672502400000
    }
  ]
}
User Information
HTTP Request

POST /v1/account/uInfo

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Response Fields

Field Name
Data Type
Description
uid

long

User UID

email

string

Email address

mobile

string

Mobile number

parentUid

long

Inviter's UID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": 
    {
      "uid": "123456",
      "email": "45678@qq.com",
      "mobile": 13800138000,
      "parentUid": 45678
    }
}




















# Perpetual Contract Trading

## Preparation for Integration

### **Trading Pairs**

A trading pair consists of a base currency and a quote currency. For example, in the trading pair `btc_usdt`, `btc` is the base currency, and `usdt` is the quote currency.

### Applying for an API Key

To apply for an API Key, visit the Hibt official website via mobile. Navigate to the personal settings page, locate API management, and submit your application. Upon successful creation, ensure you securely save the following information:

* Access Key: The access key for API requests.
* Secret Key: The secret key used for signature authentication and encryption (visible only during the application process).
* Password: Required for managing APIs.

### **API Authentication**

Public endpoints provide access to basic information and market data. These endpoints can be accessed without authentication.

Private endpoints are used for trading and account management. Each private request must be signed using your API Secret Key for verification.

### **REST API** <a href="#rest-api" id="rest-api"></a>

`https://fapi.hibt0.com/open-api`

### **Signature Authentication**

Private endpoints (used for trading and account management) require encryption with your API Key to validate that parameters or values have not been altered during transmission. Each API Key must have the appropriate permissions to access corresponding endpoints. When creating a new API Key, assign the required permissions. Before using an endpoint, ensure your API Key has the necessary permissions.

A valid request must include the following components:

* Request URL: Example `https://api.hibt0.com/open-api/v2/order/open`.
* Header - Access Key (`X-ACCESS-KEY`): Your API Key's Access Key, as obtained during API Key creation.
* Header - Body Signature (`X-SIGNATURE`): Encrypted data generated by signing the request body with your Secret Key.
* Timestamp (`timestamp`): A field in the POST request body or GET request URL parameters representing the current millisecond timestamp. This is required for signing.
* Required and Optional Parameters: Each method specifies the required and optional parameters for the API call. Check the method documentation for details.
* Signature: An encrypted value ensuring the integrity and authenticity of the request. \*\*For your API Key's security, signatures expire after **5 minutes**.
* Mandatory Signature Parameter: Any authenticated request must include the timestamp parameter for signature generation (use the latest server time from the `v2/server/time` endpoint).

**Encryption Method**

Body Content of the Open Position POST Request

```json
{
    "customID": "11111", // Your custom order ID
    "symbol": "btc_usdt", // Trading pair
    "type": 1, // 1: Limit order, 2: Market order
    "side": 1, // Direction: 1 for buy, 2 for sell
    "leverage": 10, // Leverage
    "price": "2660", // Order price (used for limit orders). Not required for market orders.
    "amount": "0.01", // Order quantity
    "triggerType": 2, // Trigger type for take-profit/stop-loss: 1 for trade price, 2 for index price. Can be omitted if not setting take-profit/stop-loss.
    "spPrice": "2770", // Preset take-profit price. Not required if not setting take-profit.
    "slPrice": "2450", // Preset stop-loss price. Not required if not setting stop-loss.
    "isSetSp": true, // Whether to set take-profit
    "isSetSl": true, // Whether to set stop-loss
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

Sort the parameters in ASCII order.

`amount=0.01&customID=11111&isSetSl=true&isSetSp=true&leverage=10&price=2660&side=1&slPrice=2450&spPrice=2770&symbol=btc_usdt&timestamp=1724916869475&triggerType=2&type=1`

Encrypt the sorted request parameters using HMAC SHA256 with the secretKey to obtain the result.

`9543936a83c8b4fd0aae02a6e6fa272dc8ebc95b871f620eb23ae1a6dadffee7`

```python
import json
import hmac
import hashlib
from collections import OrderedDict


def bytes_to_hex(bytes_array):
    """Convert bytes array to hex string."""
    return ''.join(['%02x' % byte for byte in bytes_array])


def generate_hmac_sha256(data, key):
    """Generate HMAC SHA256 signature for the given data and key."""
    secret_key = key.encode()
    message = data.encode()
    signature = hmac.new(secret_key, message, hashlib.sha256).digest()
    return bytes_to_hex(signature)


def get_sort(json_str):
    """Sort the JSON string by keys."""
    # Parse JSON string
    data = json.loads(json_str, object_pairs_hook=OrderedDict)

    # Create a new dictionary to store sorted key-value pairs
    sorted_data = OrderedDict()

    # Sort the original dictionary keys and insert them into the new dictionary in order
    for key in sorted(data.keys()):
        if data[key] != "":
            sorted_data[key] = data[key]

    return sorted_data


def get_key(json_str, secret_key):
    """Generate a signature for the given JSON string and secret key."""
    # Filter out empty string values
    sortData = get_sort(json_str)
    filtered_data = {k: v for k, v in sortData.items() if v != ""}
    # Concatenate the signature string
    sign_str = []
    for k, v in filtered_data.items():
        # If v is a list, convert it to a string
        if isinstance(v, list):
            for i in range(len(v)):
                v[i] = get_sort(json.dumps(v[i], ensure_ascii=False, separators=(',', ':')))
            v = json.dumps(v, ensure_ascii=False, separators=(',', ':'))
            sign_str.append(f"{k}={v}")
            continue
        sign_str.append(f"{k}={v}")
    sorted(sign_str)  # Sort by dictionary order
    sign_str = '&'.join(sign_str)
    print("Signature string:", sign_str)

    # Calculate HMAC SHA256 signature
    signature = generate_hmac_sha256(sign_str, secret_key)
    return signature
    # print("Signature:", signature)

if __name__ == '__main__':
    json_str = {"items": [{"amount": "1", "customID": "123223", "leverage": 20, "side": 1, "symbol": "eth_usdt", "type": 2}, {"amount": "0.01", "customID": "321322", "leverage": 100, "side": 1, "symbol": "btc_usdt", "type": 2}], "timestamp": 1725599130897}
    g = json.dumps(json_str)
    a = get_key(g, "your secret key")
    print(a)  # Print signature
```

**Note: If a parameter field contains an array, convert it to a JSON string separately and then append it to the signature string.**

**Constructing HTTP Requests**

1. `Use X-ACCESS-KEY to store the access key information and pass it as a parameter in the header.`
2. `Use X-SIGNATURE to store the generated signature information and pass it as a parameter in the header.`
3. `Use X-TIMESTAMP to store the request timestamp and pass it as a parameter in the header.`

**Request Methods**

Currently, there are only two methods: GET and POST.

* **GET Requests:** All parameters are included in the URL path.
* **POST Requests:** All parameters are sent in JSON format within the request body.

**Response Format**

```json
{
  "msg": "success",
  "code": 0,
  "data": ""
}
```

### **Common Error Codes**

#### **21XXXX (Parameter Errors)**

#### **22XXXX (Business Errors)**

| Error Code | Description                                 |
| ---------- | ------------------------------------------- |
| 210001     | Invalid parameters                          |
| 210004     | Incorrect take-profit price                 |
| 210005     | Incorrect stop-loss price                   |
| 210007     | Only data from the past 3 months is allowed |
| 210008     | Only data within a 7-day range is allowed   |
| 210009     | Only data within a 3-month range is allowed |
| 210010     | Invalid trading pair                        |
| 210011     | endTime exceeds the current time            |
| 210116     | Invalid user                                |
| 210117     | Asset balance not found                     |
| 220001     | Data not found                              |
| 220002     | Timestamp expired                           |
| 220003     | X-ACCESS-KEY not provided                   |
| 220004     | API key authentication failed               |
| 220005     | X-SIGNATURE not provided                    |
| 220007     | Access Key expired                          |
| 220008     | Signature verification failed               |
| 220011     | Authorization expired                       |
| 220012     | IP address not in whitelist                 |
| 220013     | No query permissions                        |
| 220014     | No trading permissions                      |
| 220015     | WebSocket: Invalid event type               |
| 220017     | Too many requests                           |
| 210019     | Unauthorized                                |
| 210020     | No trading or query permissions             |
| 210021     | Invalid Access Key                          |

## **Basic Information API**

### Server Time Retrieval

**HTTP Request**

**GET** `/v2/server/time`

**Authentication**: No

**Request Parameters**

None

**Response Example**

```json
{
    "code":0,
    "msg":"success",
    "data":{"serverTime":1724916869475}  //ms
}

```

### Retrieve All Trading Pairs

**HTTP Request**

**GET** `/v2/market/symbols`

**Request Parameters**: None

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "symbol": "", // Trading pair symbol
            "supportTrade": true, // Whether trading is supported
            "volumePrecision": 0, // Precision of the trading volume (number of decimal places after the decimal point)
            "pricePrecision": 0, // Precision of the trading price (number of decimal places after the decimal point)
            "marketMiniAmount": "", // Minimum market order quantity for the trading pair
            "limitMiniAmount": "" // Minimum limit order quantity for the trading pair
        }
    ]
}
```

### Retrieve Ticker Data for Trading Pairs

**HTTP Request**

**GET** `/v2/market/tickers`

**Request Parameters**

| Parameter | Description  | Required                         | Type   |
| --------- | ------------ | -------------------------------- | ------ |
| symbol    | Trading Pair | No (returns all if not provided) | string |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "symbol": "", // Trading pair symbol
            "amount": "", // Trading volume measured in the base currency (e.g., BTC)
            "volume": "", // Trading volume measured in the quote currency (e.g., USDT)
            "open": "", // Opening price of the last 24 hours
            "close": "", // Closing price of the last 24 hours
            "high": "", // Highest price of the last 24 hours
            "low": "", // Lowest price of the last 24 hours
            "lastPrice": "", // Latest traded price
            "lastAmount": "", // Volume of the latest traded price
            "lastTime": 0, // Timestamp of the latest trade
            "change": 5.55 // Price change percentage
        }
    ]
}
```

### Retrieve K-Line Data for a Specific Trading Pair

**HTTP Request**

**GET** `/v2/market/candle`

**Request Parameters**

| Parameter | Description                                                                                                                                                           | Required | Type   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------ |
| symbol    | Trading Pair                                                                                                                                                          | Yes      | string |
| period    | Data time granularity (interval for each candle): M1, M5, M15, M30, H1, H4, H6, D1                                                                                    | Yes      | string |
| start     | Start timestamp for query, in milliseconds                                                                                                                            | No       | int    |
| end       | End timestamp for query, in milliseconds                                                                                                                              | No       | int    |
| count     | Number of K-Line data points to return \[1, 500]. Default is 200, max is 500. If `start` and `end` are provided, the actual returned count depends on the time range. | No       | int    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "symbol": "", // Trading pair symbol
            "amount": "", // Trading volume measured in the base currency
            "volume": "", // Trading volume measured in the quote currency
            "open": "", // Opening price of the current period
            "close": "", // Closing price of the current period
            "high": "", // Highest price of the current period
            "low": "", // Lowest price of the current period
            "ts": 0 // Timestamp of the start of the current period
        }
    ]
}
```

### Retrieve Ticker Prices for Trading Pairs

**HTTP Request**

**GET** `/v2/market/ticker/price`

**Request Parameters**

| Parameter | Description  | Required                          | Type   |
| --------- | ------------ | --------------------------------- | ------ |
| symbol    | Trading Pair | No (returns all pairs if omitted) | string |

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":[
        {
            "symbol": "",
            "price":""
        }
    ]
}
```

### Retrieve Market Depth for a Trading Pair

**HTTP Request**

**GET** `/v2/market/depth`

**Request Parameters**

| Parameter | Description                            | Required | Type   |
| --------- | -------------------------------------- | -------- | ------ |
| symbol    | Trading Pair                           | Yes      | string |
| limit     | Depth levels (5, 10, 20, 50, 100, 200) | No       | int    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "bid": [
            [
                "9638.0",     // Bid price
                "431"         // Bid quantity
            ]
        ],
        "ask": [
            [
                "9638.0",     // Ask price
                "431"        // Ask quantity
            ]
        ]
    }
}
```

### Retrieve Latest Trades for a Trading Pair

**HTTP Request**

**GET** `/v2/market/deals`

**Request Parameters**

| Parameter | Description  | Required | Type   |
| --------- | ------------ | -------- | ------ |
| symbol    | Trading Pair | Yes      | string |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "symbol": "", // Trading pair symbol
        "amount": "", // Trading volume measured in the base currency
        "price": "", // Trade execution price in quote currency
        "side": "", // Trade direction: "sell" or "buy", where "buy" indicates a purchase and "sell" indicates a sale
        "time": 0 // Current timestamp in milliseconds
    }]
}
```

### Query Trading Pair Mark Price

**HTTP Request**

**GET** `/v2/market/index`

**Request Parameters**

| Parameter | Description  | Required                               | Type   |
| --------- | ------------ | -------------------------------------- | ------ |
| symbol    | Trading Pair | No (returns all pairs if not provided) | string |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "symbol": "", // Trading pair
        "marketPrice": "" // Market price
    }]
}
```

### Query Funding Rate

**HTTP Request**

**GET** `/v2/market/fundingRate`

**Request Parameters**

| Parameter | Description                                           | Required | Type   |
| --------- | ----------------------------------------------------- | -------- | ------ |
| symbol    | Trading Pair                                          | Yes      | string |
| startTime | Start timestamp in ms (only supports a 3-month range) | No       | int64  |
| endTime   | End timestamp                                         | No       | int64  |
| limit     | Number of records (default 100, max 1000)             | No       | int    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "symbol": "",
            "rate": "", // Funding rate
            "time": 0 // Timestamp
        }
    ]
}
```

### Query Risk Limit

**HTTP Request**

**GET** `/v2/market/riskLimit`

**Request Parameters**

| Parameter | Description  | Required | Type   |
| --------- | ------------ | -------- | ------ |
| symbol    | Trading Pair | Yes      | string |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "symbol": "", // Trading pair symbol
            "minValue": "", // Minimum position value
            "maxValue": "", // Maximum position value
            "maxLeverage": 0, // Maximum available leverage
            "maintenanceMarginRate": "" // Maintenance margin rate
        }
    ]
}
```

### Query Latest Contract Market Data

**HTTP Request**

**GET** `/v2/market/contracts`

**Request Parameters**

| Parameter | Description  | Required                    | Type   |
| --------- | ------------ | --------------------------- | ------ |
| symbol    | Trading Pair | No (returns all if omitted) | string |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [
        {
            "ticker_id": "Contract ID", // Contract Identifier
            "base_currency": "Base Currency", // Base Currency
            "quote_currency": "Quote Currency", // Quote Currency
            "last_price": "Last Price", // Last Price
            "base_volume": "Base Currency Volume", // Base Currency Volume
            "USD_volume": "USD Volume", // USD Volume
            "quote_volume": "Quote Currency Volume", // Quote Currency Volume
            "bid": "Bid Price", // Bid Price
            "ask": "Ask Price", // Ask Price
            "high": "High Price", // High Price
            "low": "Low Price", // Low Price
            "product_type": "Product Type", // Product Type
            "open_interest": "Open Interest (Base Currency)", // Open Interest (Base Currency)
            "open_interest_usd": "Open Interest (USD)", // Open Interest (USD)
            "index_price": "Index Price", // Index Price
            "creation_timestamp": 0, // Creation Timestamp
            "expiry_timestamp": 0, // Expiry Timestamp
            "funding_rate": "Funding Rate", // Funding Rate
            "next_funding_rate": "Next Funding Rate", // Next Funding Rate
            "next_funding_rate_timestamp": 0, // Next Funding Rate Timestamp
            "maker_fee": "Maker Fee Rate", // Maker Fee Rate
            "taker_fee": "Taker Fee Rate", // Taker Fee Rate
            "contract_type": "Contract Type", // Contract Type
            "contract_price": "Contract Face Value", // Contract Face Value
            "contract_price_currency": "Contract Face Value Currency" // Contract Face Value Currency
        }
    ]
}
```

### Query Contract Trading Specifications

**HTTP Request**

**GET** `/v2/market/contractSpecifications`

**Request Parameters** None

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":[
        {
            "contract_type": "okb_usdt",
            "contract_price": "123.45", //Last Price
            "contract_price_currency": "usdt"
        }
    ]
}
```

### Query Contract Order Book

**HTTP Request**

**GET** `/v2/market/orderBook`

**Request Parameters**

| Parameter | Description  | Required | Type   |
| --------- | ------------ | -------- | ------ |
| depth     | Level 1-100  | No       | int    |
| symbol    | Trading pair | No       | string |

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":[
        {
            "ticker_id": "btc_usdt",  // 交易对标识符，例如 "BTCUSD"
            "timestamp": 1689991200,  // 时间戳（毫秒级）
            "bids": [  // 买方订单列表
                ["10000.50", "2.3"],  // [价格, 数量]
                ["9999.75", "1.1"]
            ],
            "asks": [  // 卖方订单列表
                ["10001.00", "3.5"],
                ["10002.25", "0.8"]
            ]
        }
    ]
}
```

## **Trading API**

### Open Position

**HTTP Request**

**POST** `/v2/order/open`

**Authentication Required** Yes

**Request Parameters**

```json
{
    "customID": "11111", // Your custom order ID. Optional; if provided, it must be unique.
    "symbol": "btc_usdt", // Trading pair
    "type": 1, // 1: Limit Order, 2: Market Order
    "side": 1, // Direction: 1 for buy, 2 for sell
    "leverage": 10, // Leverage
    "price": "2660", // Order price (used for limit orders; not required for market orders)
    "amount": "0.01", // Order quantity
    "triggerType": 2, // Take profit/stop loss trigger type: 1: Last price, 2: Index price; optional if not setting TP/SL
    "spPrice": "2770", // Preset take profit price; optional if not setting TP
    "slPrice": "2450", // Preset stop loss price; optional if not setting SL
    "isSetSp": true, // Whether to set take profit
    "isSetSl": true, // Whether to set stop loss
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "orderID": "24081233332184101100143203708" // Order ID
    }
}
```

### **Batch Opening Positions**

**HTTP Request**

**POST** `/v2/order/batchOpen`

**Authentication Required** Yes

**Request Parameters**

```json
{
    "timestamp": 1724916869475, // Current timestamp in milliseconds

    "items":[{
        "customID": "11111", // Your custom order ID. Optional; if provided, it must be unique.
        "symbol": "btc_usdt", // Trading pair
        "type": 1, // 1: Limit Order, 2: Market Order
        "side": 1, // Direction: 1 for buy, 2 for sell
        "leverage": 10, // Leverage
        "price": "2660", // Order price (used for limit orders; not required for market orders)
        "amount": "0.01", // Order quantity
        "triggerType": 2, // Take profit/stop loss trigger type: 1: Last price, 2: Index price; optional if not setting TP/SL
        "spPrice": "2770", // Preset take profit price; optional if not setting TP
        "slPrice": "2450", // Preset stop loss price; optional if not setting SL
        "isSetSp": true, // Whether to set take profit
        "isSetSl": true // Whether to set stop loss
    },
     {
                 "customID": "11111", // Your custom order ID. Optional; if provided, it must be unique.
                 "symbol": "btc_usdt", // Trading pair
                 "type": 1, // 1: Limit Order, 2: Market Order
                 "side": 1, // Direction: 1 for buy, 2 for sell
                 "leverage": 10, // Leverage
                 "price": "2660", // Order price (used for limit orders; not required for market orders)
                 "amount": "0.01", // Order quantity
                 "triggerType": 2, // Take profit/stop loss trigger type: 1: Last price, 2: Index price; optional if not setting TP/SL
                 "spPrice": "2770", // Preset take profit price; optional if not setting TP
                 "slPrice": "2450", // Preset stop loss price; optional if not setting SL
                 "isSetSp": true, // Whether to set take profit
                 "isSetSl": true // Whether to set stop loss
      }]}

```

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "success": {
            "11111": "orderID",
            "2222222": "orderID"
        }, // Custom order IDs mapped to their corresponding order IDs
        "fail": {
            "333333": "sp price error",
            "44444444": "bad symbol"
        }  // Custom order IDs mapped to their respective error messages
    }
}
```

### **Cancel Order**

**HTTP Request**

**POST** `/v2/order/cancel`

**Authentication Required** Yes

**Request Parameters**

```json
{
    "symbol": "btc_usdt",
    "orderID": "22222222", // Choose one of: orderID, customID, or positionID
    "customID": "",
    "positionID": "",
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":{
        "success":{"11111":"orderID", "2222222":"orderID"}, // {"自定义订单id":"委托单id"}
        "fail":{"333333":"orderID", "44444444":"orderID",}  // {"自定义订单id":"委托单id"}
    }
}
```

### **Batch Cancel Orders**

**HTTP Request**

**POST** `/v2/order/batchCancel`

**Authentication Required** Yes

**Request Parameters**

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "symbol": "btc_usdt",
  "listOrderID": ["11111"], // Choose one among listOrderID, listCustomID, or listPositionID, or leave all empty
  "listCustomID": [""],
  "listPositionID": [""],
  "timestamp": 1724916869475 // Current timestamp in milliseconds
}
</code></pre>

**Response Example**

```json
{
	"msg":"success",
    "code":0,
    "data":{
        "success":{"11111":"orderID", "2222222":"orderID"}, // {"自定义订单id":"委托单id"}
        "fail":{"333333":"orderID", "44444444":"orderID",}  // {"自定义订单id":"委托单id"}
    }
}
```

### **Close Position**

**HTTP Request**

**POST** `/v2/order/close`

**Authentication Required** Yes

**Request Parameters**

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "amount": "0.01",
  "price": "2256", // Only for limit order close
  "type": 1, // 1 for Limit, 2 for Market
  "positionID": "12222222222222", // Position ID
  "timestamp": 1724916869475 // Current timestamp in milliseconds
}
</code></pre>

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "orderID": "24081233332184101100143203708" // Order ID
    }
}
```

### **Close All Positions**

**HTTP Request**

**POST** `/v2/order/closeAll`

**Authentication Required** Yes

**Request Parameters**

```json
{
    "symbol": "btc_usdt",
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "listOrderID": ["24081233332184101100143203708"] // Order IDs
    }
}
```

### **Query Unfinished Orders**

**HTTP Request**

**GET** `/v2/order/unFinish`

**Authentication Required** Yes

**Request Parameters**

| Parameter  | Description                                                                          | Required | Data Type |
| ---------- | ------------------------------------------------------------------------------------ | -------- | --------- |
| symbol     | Trading pair                                                                         | No       | string    |
| orderID    | Order ID // Either orderID, customID, or positionID must be provided, or none at all | No       | string    |
| customID   | Custom order ID                                                                      | No       | string    |
| positionID | Position ID                                                                          | No       | string    |
| timestamp  | Current timestamp in milliseconds                                                    | Yes      |           |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "id": "", // Order ID
        "customID": "", // Custom Order ID
        "symbol": "", // Trading Pair
        "type": 1, // Order Type: 1 = Limit, 2 = Market
        "action": 0, // Order Event: 0 = Open, 1 = Close, 2 = Stop Loss, 3 = Take Profit, 4 = Forced Close, 5 = FOK Forced Close, 6 = ADL Reduce Position, 7 = Add Position, 8 = Reverse Open, 9 = Margin Call
        "side": 1, // Trading Direction: 1 = Buy, 2 = Sell
        "positionID": "", // Position ID
        "price": "", // Order Price (only valid for limit orders)
        "leverage": 0, // Leverage
        "amount": "", // Order Quantity
        "frozen": "", // Frozen Margin
        "filledAmount": "", // Filled Quantity
        "filledPrice": "", // Average Filled Price
        "filledValue": "", // Filled Value
        "triggerType": 2, // Trigger Type for Stop Loss/Take Profit: 1 = Last Price, 2 = Index Price
        "spPrice": "", // Preset Take Profit Price
        "slPrice": "", // Preset Stop Loss Price
        "state": 1, // Order Status: 1 = Active, 2 = Filled, 3 = Cancelled, 4 = Partially Filled, 5 = Partially Filled & Cancelled, 6 = Cancelling
        "profit": "", // Realized Profit/Loss (for closed orders)
        "fee": "", // Original Fee
        "pointFee": "", // Fee Discounted by Points/Bonuses
        "pointProfit": "", // Profit/Loss Discounted by Points/Bonuses
        "closePrice": "", // Liquidation Price
        "triggerPrice": "", // Trigger Price
        "createdAt": 0, // Creation Timestamp
        "updatedAt": 0 // Last Update Timestamp
    }]
}
```

### **Query Details of Completed Orders**

**HTTP Request**

**GET** `/v2/order/finishedInfo`

**Authentication Required** Yes

**Request Parameters**

| Parameter  | Description                                                          | Data Type |
| ---------- | -------------------------------------------------------------------- | --------- |
| symbol     | Trading pair                                                         | string    |
| orderID    | Order ID // Either orderID, customID, or positionID must be provided | string    |
| customID   | Custom order ID                                                      | string    |
| positionID | Position ID                                                          | string    |
| timestamp  | Current timestamp in milliseconds                                    | number    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "id": "", // Order ID
        "customID": "", // Custom Order ID
        "symbol": "", // Trading Pair
        "type": 1, // Order Type: 1 = Limit, 2 = Market
        "action": 0, // Order Event: 0 = Open, 1 = Close, 2 = Stop Loss, 3 = Take Profit, 4 = Forced Close, 5 = FOK Forced Close, 6 = ADL Reduce Position, 7 = Add Position, 8 = Reverse Open, 9 = Margin Call
        "side": 1, // Trading Direction: 1 = Buy, 2 = Sell
        "positionID": "", // Position ID
        "price": "", // Order Price (only valid for limit orders)
        "leverage": 0, // Leverage
        "amount": "", // Order Quantity
        "frozen": "", // Frozen Margin
        "filledAmount": "", // Filled Quantity
        "filledPrice": "", // Average Filled Price
        "filledValue": "", // Filled Value
        "triggerType": 2, // Trigger Type for Stop Loss/Take Profit: 1 = Last Price, 2 = Index Price
        "spPrice": "", // Preset Take Profit Price
        "slPrice": "", // Preset Stop Loss Price
        "state": 1, // Order Status: 1 = Active, 2 = Filled, 3 = Cancelled, 4 = Partially Filled, 5 = Partially Filled & Cancelled, 6 = Cancelling
        "profit": "", // Realized Profit/Loss (for closed orders)
        "fee": "", // Original Fee
        "pointFee": "", // Fee Discounted by Points/Bonuses
        "pointProfit": "", // Profit/Loss Discounted by Points/Bonuses
        "closePrice": "", // Liquidation Price
        "triggerPrice": "", // Trigger Price
        "createdAt": 0, // Creation Timestamp
        "updatedAt": 0 // Last Update Timestamp
    }
}
```

### **Query History of Completed Orders**

**HTTP Request**

**GET** `/v2/order/finished`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description                       | Data Type |
| --------- | --------------------------------- | --------- |
| symbol    | Trading pair                      | string    |
| startTime | Start time (timestamp)            | int       |
| endTime   | End time (timestamp)              | int       |
| pageIndex | Page number for pagination        | int       |
| pageSize  | Number of items per page, max 50  | int       |
| timestamp | Current timestamp in milliseconds | number    |

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":{
        "total":100, //总量
        "page":1, //当前第几页
        "data":[{
            "id": "", //订单id
            "customID": "", //自定义订单id
            "symbol": "",//交易对
            "type": 1, //订单类型 订单类型 1限价 2市价
            "action": 0, //订单事件 0开仓 1平仓 2止损 3止盈 4强平 5FOK强平 6ADL减仓 7加仓 8反向开仓 9穿仓
            "side": 1,  //交易方向 1 buy 2 sell
            "positionID": "", //仓位id
            "price": "", //订单价格，限价单才有值
            "leverage": 0, //杠杆
            "amount": "", //下单量
            "frozen": "", //冻结保证金
            "filledAmount": "", //已完成量
            "filledPrice": "", //成交均价
            "filledValue": "",//成交价值
            "triggerType": 2, //止盈止损触发类型 1成交价 2指数价
            "spPrice": "", //预设止盈价
            "slPrice": "", //预设止损价
            "state": 1,//状态 1正常 2已完成 3撤销 4部分成交 5部分成交已撤销 6撤销中
            "profit": "", //已实现盈亏（平仓订单使用）
            "fee": "", //原始手续费
            "pointFee": "", //积分(赠金)手续费抵扣
            "pointProfit": "", //积分(赠金)盈亏抵扣
            "closePrice": "", //破产价
            "triggerPrice": "", //触发价
            "createdAt": 0,
            "updatedAt": 0
        }]
    }

}
```

### **Add Conditional Order**

**HTTP Request**

**POST** `/v2/entrust/add`

**Authentication Required** Yes

**Request Parameters**

```json
{
	"customID": "11111", // Custom order ID
	"symbol": "btc_usdt", // Trading pair
	"side": 1, // Trade direction: 1 for buy, 2 for sell
	"triggerType": 1, // Trigger type: 1 for latest price, 2 for index price
	"triggerPrice": "", // Trigger price
	"amount": "", // Order quantity
	"price": "", // Entrusted price
	"leverage": 0, // Leverage
	"spSlTriggerType": 0, // Take profit/stop loss trigger type: 1 for latest price, 2 for index price
	"spPrice": "", // Preset take-profit price (provide if setting take profit)
	"slPrice": "", // Preset stop-loss price (provide if setting stop loss)
	"IsSetSp": false, // Whether to set take profit
	"IsSetSl": false, // Whether to set stop loss
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "id": "", // Order ID
        "symbol": "", // Trading Pair
        "leverage": 0, // Leverage
        "triggerType": 1, // Trigger Type: 1 = Last Price, 2 = Index Price
        "triggerPrice": "", // Trigger Price
        "status": 2, // Status: 1 = Pending, 2 = Placed, 3 = Cancelled by User, 4 = Cancelled by System
        "side": 1, // Trading Direction: 1 = Buy, 2 = Sell
        "price": "", // Order Price
        "startPrice": "", // Trigger Order Price
        "amount": "", // Order Quantity
        "spSlTriggerType": 0, // Take Profit/Stop Loss Trigger Type
        "spPrice": "", // Preset Take Profit Price
        "slPrice": "", // Preset Stop Loss Price
        "isSetSp": false, // Is Take Profit Set
        "isSetSl": false, // Is Stop Loss Set
        "frozen": "", // Frozen Margin
        "createdAt": 0, // Creation Timestamp
        "updatedAt": 0 // Last Update Timestamp
    }
}
```

### **Cancel Conditional Order**

**HTTP Request**

**POST** `/v2/entrust/cancel`

**Authentication Required** Yes

**Request Parameters**

```json
{
	"symbol": "", // Trading pair
	"entrustID": "", // Entrust ID (choose either this or custom ID)
	"customID": "", // Custom user ID
    "timestamp": 1724916869475 // Current timestamp in milliseconds
}
```

**Response Example**

```json
{
    "msg":"success",
    "code":0,
    "data":["委托id1"，"委托id2"] // 返回取消成功的列表
}
```

### **Retrieve Unfinished Conditional Orders**

**HTTP Request**

**GET** `/v2/entrust/unFinish`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description       | Data Type |
| --------- | ----------------- | --------- |
| symbol    | Trading pair      | string    |
| timestamp | Current timestamp | number    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "id": "", // Order ID
        "symbol": "", // Trading Pair
        "leverage": 0, // Leverage
        "triggerType": 1, // Trigger Type: 1 = Last Price, 2 = Index Price
        "triggerPrice": "", // Trigger Price
        "status": 2, // Status: 1 = Pending, 2 = Placed, 3 = Cancelled by User, 4 = Cancelled by System
        "side": 1, // Trading Direction: 1 = Buy, 2 = Sell
        "price": "", // Order Price
        "startPrice": "", // Trigger Order Price
        "amount": "", // Order Quantity
        "spSlTriggerType": 0, // Take Profit/Stop Loss Trigger Type
        "spPrice": "", // Preset Take Profit Price
        "slPrice": "", // Preset Stop Loss Price
        "isSetSp": false, // Is Take Profit Set
        "isSetSl": false, // Is Stop Loss Set
        "frozen": "", // Frozen Margin
        "createdAt": 0, // Creation Timestamp
        "updatedAt": 0 // Last Update Timestamp
    }]
}
```

### **Retrieve Completed Conditional Orders List**

**HTTP Request**

**GET** `/v2/entrust/finished`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description                    | Data Type |
| --------- | ------------------------------ | --------- |
| symbol    | Trading pair                   | string    |
| pageIndex | Pagination index               | int       |
| pageSize  | Number of entries (maximum 50) | int       |
| timestamp | Current timestamp              | number    |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "total": 100, // Total number of orders
        "page": 1, // Current page number
        "data": [{
            "id": "", // Order ID
            "symbol": "", // Trading pair
            "leverage": 0, // Leverage
            "triggerType": 1, // Trigger type: 1 = Last price, 2 = Index price
            "triggerPrice": "", // Trigger price
            "status": 2, // Order status: 1 = Pending, 2 = Placed, 3 = Cancelled by user, 4 = Cancelled by system
            "side": 1, // Trading direction: 1 = Buy, 2 = Sell
            "price": "", // Order price
            "startPrice": "", // Trigger order price
            "amount": "", // Order quantity
            "spSlTriggerType": 0, // Take profit/stop loss trigger type
            "spPrice": "", // Preset take profit price
            "slPrice": "", // Preset stop loss price
            "isSetSp": false, // Is take profit set
            "isSetSl": false, // Is stop loss set
            "frozen": "", // Frozen margin
            "createdAt": 0, // Creation timestamp
            "updatedAt": 0 // Last update timestamp
        }]
    }
}
```

## **Account Interface**

### **Retrieve Account Balance**

**HTTP Request**

**GET** `/v2/account/balance`

**Authentication Required** Yes

**Request Parameters** None

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "balance": "Balance",  // Account balance
        "frozen": "Frozen Margin",  // Frozen margin for open orders
        "margin": "Position Margin",  // Margin held for open positions
        "point": "Points (Bonuses)",  // Points or bonuses
        "loans": "Loans",  // Amount borrowed
        "profit": "Unrealized Profit/Loss",  // Unrealized profit/loss
        "unProfit": "Floating Profit",  // Floating profit
        "unLosses": "Floating Loss",  // Floating loss
        "coin": "Coin"  // Cryptocurrency
    }
}
```

### **Adjust Opening Leverage**

**HTTP Request**

**POST** `/v2/account/setLeverage`

**Authentication Required** Yes

**Request Parameters**

```json
{
	"symbol": "", // Trading pair
	"leverage": 0, // Leverage
    "timestamp": 1724916869475 // Current timestamp in ms
}
```

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": {
        "symbol": "", // Trading pair
        "leverage": 0 // Leverage
    }
}
```

### **Get User Positions**

**HTTP Request**

**GET** `/v2/account/position`

**Authentication Required** Yes

**Request Parameters**

| Parameter  | Description             | Required | Type   |
| ---------- | ----------------------- | -------- | ------ |
| symbol     | Trading pair            | No       | string |
| positionID | Position ID             | No       | string |
| timestamp  | Current timestamp in ms | Yes      |        |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "positionID": "",          // Position ID
        "symbol": "",              // Trading pair
        "side": 0,                 // Position side (1: Buy, 2: Sell)
        "leverage": 0,             // Leverage multiple used
        "price": "",               // Average transaction price
        "amount": "",              // Position quantity
        "frozenAmount": "",        // Frozen quantity for liquidation
        "margin": "",               // Margin held for the position
        "triggerType": 1,           // Trigger type for take profit and stop loss: 1 = Transaction price, 2 = Index price
        "spPrice": "",             // Take profit price
        "slPrice": "",             // Stop loss price
        "openProfit": "",           // Unrealized profit/loss
        "updatedAt": 0,            // Timestamp
        "spSlModel": 0,            // Take profit and stop loss model: 1 = Full take profit and stop loss, 2 = Partial take profit and stop loss
        "spType": 0,               // Take profit type: 0 = Not set, 1 = Limit price, 2 = Market price
        "slType": 0,               // Stop loss type: 0 = Not set, 1 = Limit price, 2 = Market price
        "spTriggerPrice": "",      // Take profit trigger price
        "slTriggerPrice": "",     // Stop loss trigger price
        "spSlPartData": [          // Partial take profit and stop loss data
            {
                "id": 0,
                "triggerType": 1,  // Trigger type for take profit and stop loss
                "spPrice": "",     // Take profit price
                "slPrice": "",     // Stop loss price
                "amount": "",      // Quantity for take profit and stop loss
                "spType": 1,       // Take profit type: 0 = Not set, 1 = Limit price, 2 = Market price
                "slType": 1,       // Stop loss type: 0 = Not set, 1 = Limit price, 2 = Market price
                "spTriggerPrice": "", // Take profit trigger price
                "slTriggerPrice": ""  // Stop loss trigger price
            }
        ]
    }]
}
```

### **Get Account Trade History**

**HTTP Request**

**GET** `/v2/account/order`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description                                 | Required | Type   |
| --------- | ------------------------------------------- | -------- | ------ |
| symbol    | Trading pair                                | Yes      | string |
| startTime | Start time in seconds                       | No       | int64  |
| endTime   | End time in seconds                         | No       | int64  |
| limit     | Number of entries (default: 500, max: 1000) | No       | int    |
| timestamp | Current timestamp in ms                     | Yes      |        |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "id": "",                          // Order ID
        "symbol": "",                      // Contract identifier
        "type": 0,                         // Order type (1: Limit, 2: Market)
        "action": 0,                       // Order event (0: Open, 1: Close, 2: Stop Loss, 3: Take Profit, 4: Liquidation, 5: FOK Liquidation, 6: ADL Reduction, 7: Margin Increase, 8: Opposite Position, 9: Margin Call)
        "side": 0,                         // Trading direction (1: Buy, 2: Sell)
        "positionId": "",                  // Position ID
        "price": "",                       // Order price (only for Limit orders)
        "leverage": 0,                     // Leverage multiple
        "amount": "",                      // Order quantity
        "frozen": "",                      // Frozen margin (OpenPrice * Amount * BaseMarginRate)
        "filledAmount": "",                // Filled quantity
        "filledPrice": "",                 // Weighted average price of filled orders
        "filledValue": "",                 // Total value of filled orders
        "triggerType": 0,                  // Trigger type for Take Profit and Stop Loss (1: Transaction price, 2: Index price)
        "spPrice": "",                     // Preset Take Profit price
        "slPrice": "",                     // Preset Stop Loss price
        "createdAt": 0,                    // Creation time
        "updatedAt": 0,                    // Last update time
        "state": 0,                        // Order state (1: Normal, 2: Completed, 3: Canceled, 4: Partially Filled, 5: Partially Filled & Canceled, 6: Canceling)
        "profit": "",                      // Realized profit/loss (for closed orders)
        "fee": "",                         // Transaction fee
        "pointFee": "",                    // Fee deduction using points (bonuses)
        "pointProfit": "",                 // Profit/loss deduction using points (bonuses)
        "closePrice": ""                    // Bankruptcy price
    }]
}
```

### **Get Account Balance Record**

**HTTP Request**

**GET** `/v2/account/balanceRecord`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description                                                                                                                                                                        | Required | Type   |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------ |
| symbol    | Trading pair                                                                                                                                                                       | No       | string |
| startTime | Start time in ms (interval: 30 days)                                                                                                                                               | No       | int64  |
| endTime   | End time in ms (interval: 30 days)                                                                                                                                                 | No       | int64  |
| event     | Event type: 1: Deposit, 2: Deduction, 3: Transfer In, 4: Transfer Out, 9: Funding Fee, 201: Open Long, 202: Open Short, 204: Close Long, 205: Close Short, 206: Forced Liquidation | No       | int    |
| limit     | Number of entries (default: 500, max: 1000)                                                                                                                                        | No       | int    |
| timestamp | Current timestamp                                                                                                                                                                  | Yes      |        |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "id": "",                          // Transaction ID
        "event": 0,                        // Type: 1: Deposit, 2: Withdrawal, 3: Transfer In, 4: Transfer Out, 9: Funding Fee, 201: Long Position Open, 202: Short Position Open, 204: Long Position Close, 205: Short Position Close, 206: Liquidation
        "amount": "",                      // Amount representing either balance-related operations or profit/loss for trading-related operations
        "coin": "",                        // Cryptocurrency
        "fee": "",                         // Transaction fee
        "symbol": "",                      // Associated trading pair
        "note": "",                        // Remarks
        "createdAt": 0                     // Timestamp
    }]
}
```

### **Get User Forced Liquidation History**

**HTTP Request**

**GET** `/v2/account/orderForced`

**Authentication Required** Yes

**Request Parameters**

| Parameter | Description                                                                                                       | Required | Type   |
| --------- | ----------------------------------------------------------------------------------------------------------------- | -------- | ------ |
| symbol    | Trading pair                                                                                                      | No       | string |
| startTime | Start time in ms (start and end interval must be within 7 days)                                                   | No       | int64  |
| endTime   | End time in ms                                                                                                    | No       | int64  |
| action    | Forced liquidation type: 4 - Forced Liquidation, 5 - FOK Liquidation, 6 - ADL (Auto-Deleveraging), 9 - Bankruptcy | No       | int    |
| limit     | Number of entries (default: 500, max: 1000)                                                                       | No       | int    |
| timestamp | Current timestamp                                                                                                 | Yes      |        |

**Response Example**

```json
{
    "msg": "success",
    "code": 0,
    "data": [{
        "id": "",                          // Order ID
        "symbol": "",                      // Currency pair
        "type": 0,                         // Order type (1: Limit, 2: Market)
        "action": 0,                       // Liquidation type: 4 - Liquidation, 5 - FOK Liquidation, 6 - ADL Auto Deleveraging, 9 - Margin Call
        "side": 0,                         // Trading direction (1: Buy, 2: Sell)
        "positionID": "",                  // Position ID
        "price": "",                       // Order price (only applicable for Limit orders)
        "leverage": 0,                     // Leverage
        "amount": "",                      // Order quantity
        "frozen": "",                      // Frozen margin (OpenPrice * Amount * BaseMarginRate)
        "filledAmount": "",                // Filled quantity
        "filledPrice": "",                 // Weighted average filled price
        "filledValue": "",                 // Total filled value
        "triggerType": 0,                  // Trigger type for Take Profit and Stop Loss (1: Transaction price, 2: Index price)
        "spPrice": "",                     // Preset Take Profit price
        "slPrice": "",                     // Preset Stop Loss price
        "createdAt": 0,                    // Creation time
        "updatedAt": 0,                    // Last update time
        "state": 0,                        // Order status (1: Normal, 2: Completed, 3: Cancelled, 4: Partially Filled, 5: Partially Filled & Cancelled, 6: Cancelling)
        "profit": "",                      // Realized profit/loss (for closed orders)
        "fee": "",                         // Transaction fee
        "pointFee": "",                    // Fee deduction using points (bonuses)
        "pointProfit": "",                 // Profit/loss deduction using points (bonuses)
        "closePrice": ""                   // Margin call price
    }]
}
```

## Contract WebSocket API

**Request URL** Example: `wss://fapi.hibt0.com/v2/ws`

**API Authentication**

For subscriptions that require authentication, send the authentication message first.

#### **ignature**: Simply sign the timestamp string.

```json
{"event":"auth","accessKey":"XXX","timestamp":"XXX","signature":"XXX"}
```

#### **Subscribe to Topic**

`{"event":"sub", "topic":"Topic Content"}`

**Subscribe to Market Depth**

Supported market depth topics: 5deep, 10deep, 20deep

Request JSON: `{"event":"sub","topic":"btc_usdt.5deep"}`

**Response Example**

```json
{
    "type":"btc_usdt.5deep",
 	"ts":1725356328427,
 	"data":{
        "symbol":"btc_usdt",
  		"asks":["58930.89","2.51","58930.99","2.38","58931.09","2.9","58931.19","3.72","58931.29","1.41"],
  		"bids":["58930.71","1.44","58930.61","1.61","58930.51","2.22","58930.41","1.22","58930.31","1.94"]
 	}
}
```

### **Subscribe to Ticker**

Request JSON: `{"event":"sub","topic":"btc_usdt.ticker"}`

**Response Example**

```json
{
  "type": "btc_usdt.ticker",
  "ts": 1725356998063,
  "data": {
    "symbol": "btc_usdt",
    "amount": "473529.69",   // BTC Volume
    "volume": "27853751718.826", // Total USDT Value
    "open": "58147.82", // 24-Hour Opening Price
    "close": "58920.25",
    "high": "59805.51", // 24-Hour High Price
    "low": "58103.55", // 24-Hour Low Price
    "lastPrice": "58920.25", // Last Traded Price
    "lastAmount": "0.99", // Volume of the Last Trade
    "lastTime": 1725356998061,
    "change": "1.32" // 24-Hour Price Change Percentage
  }
}
```

### **Subscribe to Index**

Request JSON: `{"event":"sub","topic":"btc_usdt.index"}`

**Response Example**

```json
{
  "type": "btc_usdt.index",
  "ts": 1725357439229,
  "data": {
    "symbol": "btc_usdt",
    "price": "58901.1",
    "time": 1725357439228
  }
}
```

### **Subscribe to Latest Trades**

Request JSON: `{"event":"sub","topic":"btc_usdt.trade"}`

**Response Example**

```json
{
  "type": "btc_usdt.trade",
  "ts": 1725357599308,
  "data": [
    "58872.48", // Trade Price
    "1",  // Trade Side: 1 - Buy, 2 - Sell
    "2.59", // Trade Volume (BTC)
    "1725357599305" // Timestamp
  ]
}
```

### **Subscribe to K-Line**

Request JSON: `{"event":"sub","topic":"btc_usdt.candle.M1"}`

Supported Time Intervals:

```
"M1","M5","M15","M30","H1","H2","H4","H6","H12","D1","W1"
```

**Response Example**

```json
{
  "type": "btc_usdt.candle.M1",
  "ts": 1725357897306,
  "data": [
    "410.89", // Trading Volume
    "24207865.8365", // Trading Volume in USDT
    "58891.64", // Opening Price
    "58945.88", // High Price
    "58891.64", // Low Price
    "58923.96", // Closing Price
    "1725357840000" // Timestamp
  ]
}
```

### **Subscribe to Plan Order Trigger Push (Authentication Required)**

Request JSON: `{"event":"sub","topic":"user.entrust"}`

**Response Example**

```json
{
    "type": "user.entrust",
    "ts": 1725437392251,
    "data": [
        {
            "id": "24090408062338901100109440001",
            "symbol": "btc_usdt",
            "leverage": 10, // Leverage
            "triggerType": 2, // Trigger Type: 1 - Last Traded Price, 2 - Mark Price
            "triggerPrice": "56762", // Trigger Price
            "status": 2, // Status: 1 - Pending, 2 - Placed, 3 - Cancelled by User, 4 - Cancelled by System
            "side": 1, // Trade Direction: 1 - Buy, 2 - Sell
            "price": "56830", // Order Price
            "startPrice": "", // Trigger Order Price (not used in this context)
            "amount": "0.12", // Order Quantity
            "spSlTriggerType": 0, // Stop Profit/Loss Trigger Type (not specified)
            "spPrice": "0", // Preset Take Profit Price
            "slPrice": "0", // Preset Stop Loss Price
            "isSetSp": false, // Is Take Profit Set?
            "isSetSl": false, // Is Stop Loss Set?
            "frozen": "", // Frozen Margin
            "createdAt": 1725437183389,
            "updatedAt": 1725437392240
        }
    ]
}
```

### **Subscribe to Position Change (Authentication Required)**

Request JSON: `{"event":"sub","topic":"user.position"}`

**Response Example**

```json
{
    "type": "user.position",
    "ts": 1725364233774,
    "data": [
        {
            "positionID": "240903114238636010629", // Position ID
            "symbol": "btc_usdt", // Trading pair
            "side": 1, // Position direction: 1 - Buy, 2 - Sell
            "leverage": 10, // Leverage
            "price": "59066", // Average entry price
            "amount": "0.21", // Position size
            "frozenAmount": "0.21", // Frozen position size for liquidation
            "margin": "1240.386", // Margin held for the position
            "triggerType": 1, // Stop Profit/Loss trigger type
            "spPrice": "", // Take Profit price (not set)
            "slPrice": "", // Stop Loss price (not set)
            "openProfit": "", // Unrealized profit/loss
            "updatedAt": 1725364233773,
            "spSlModel": 1, // Stop Profit/Loss model: 1 - Full, 2 - Partial
            "spType": 0, // Take Profit type: 0 - Not set, 1 - Limit, 2 - Market
            "slType": 0, // Stop Loss type: 0 - Not set, 1 - Limit, 2 - Market
            "spTriggerPrice": "0", // Take Profit trigger price (not set)
            "slTriggerPrice": "0", // Stop Loss trigger price (not set)
            "spSlPartData": [{
                "id": 0,
                "triggerType": 1, // Partial Stop Profit/Loss trigger type
                "spPrice": "", // Partial Take Profit price (not set)
                "slPrice": "", // Partial Stop Loss price (not set)
                "amount": "", // Quantity for partial Stop Profit/Loss
                "spType": 0, // Partial Take Profit type: 0 - Not set, 1 - Limit, 2 - Market
                "slType": 0, // Partial Stop Loss type: 0 - Not set, 1 - Limit, 2 - Market
                "spTriggerPrice": "", // Partial Take Profit trigger price (not set)
                "slTriggerPrice": ""  // Partial Stop Loss trigger price (not set)
            }] // Partial Stop Profit/Loss data
        }
    ]
}
```

### **Subscribe to Order Execution Notifications (Authentication Required)**

```
Request JSON: `{"event":"sub","topic":"user.order"}`
```

**Response Example**

```json
{
    "type": "user.order",
    "ts": 1725432998830,
    "data": [
        {
            "id": "24090406563872601100109440728", // Order ID
            "customID": "", // Custom Order ID
            "symbol": "btc_usdt", // Trading Pair
            "type": 2, // Order Type: 1 - Limit, 2 - Market
            "action": 0, // Order Action: 0 - Open Position, 1 - Close Position, 2 - Stop Loss, 3 - Take Profit, 4 - Forced Liquidation, 5 - FOK Forced Liquidation, 6 - ADL Reduction, 7 - Add Position, 8 - Reverse Open Position, 9 - Margin Call
            "side": 1, // Trade Direction: 1 - Buy, 2 - Sell
            "positionID": "240904065638726010729", // Position ID
            "price": "0", // Order Price (only applicable for limit orders)
            "leverage": 10, // Leverage
            "amount": "0.2", // Order Quantity
            "frozen": "1128.5496", // Frozen Margin: OpenPrice * Amount * BaseMarginRate
            "filledAmount": "0", // Filled Quantity
            "filledPrice": "0", // Average Filled Price
            "filledValue": "", // Filled Value (not provided)
            "triggerType": 1, // Stop Profit/Loss Trigger Type: 1 - Last Traded Price, 2 - Index Price
            "spPrice": "0", // Preset Take Profit Price
            "slPrice": "0", // Preset Stop Loss Price
            "state": 0, // Order State: 1 - Active, 2 - Filled, 3 - Cancelled, 4 - Partially Filled, 5 - Partially Filled & Cancelled, 6 - Cancelling
            "profit": "", // Realized Profit/Loss (for closed orders)
            "fee": "", // Transaction Fee
            "pointFee": "", // Fee Offset by Points/Bonuses
            "pointProfit": "", // Profit/Loss Offset by Points/Bonuses
            "closePrice": "", // Liquidation Price
            "triggerPrice": "", // Trigger Price
            "createdAt": 1725432998726,
            "updatedAt": 0
        }
    ]
}
```

### **Subscribe to Account Balance Changes (Authentication Required)**

Request JSON: `{"event":"sub","topic":"user.balance"}`

**Response Example**

```json
{
  "type": "user.balance",
  "ts": 1725364751331,
  "data": {
    "balance": "4853.95", // Balance in USDT
    "frozen": "0", // Margin frozen due to open orders
    "margin": "1181.29", // Margin held for open positions
    "point": "0", // Bonus balance
    "loans": "", // Loans (not provided)
    "profit": "0",  // Unrealized profit and loss (sum of unProfit and unLosses)
    "unProfit": "0",  // Unrealized profit
    "unLosses": "0", // Unrealized loss
    "coin": "usdt" // Currency (USDT)
  }
}
```












# Spot Trading (Market Maker)

## API Introduction

### Access preparation

#### Trading pairs

A trading pair consists of a base currency and a quote currency. Taking the trading pair BTC/USDT as an example, BTC is the base currency, and USDT is the quote currency.

#### Apply for API Key

After successful creation, please be sure to remember the following information:

* `Access Key` API Access Key
* `Secret Key` Key used for signature authentication encryption (visible only during application)

**Interface Authentication**&#x20;

Public interfaces can be used to obtain basic information and market data. Public interfaces can be called without authentication.&#x20;

Private interfaces can be used for trade management and account management. Each private request must be signed and verified using your API Key.

#### Access URLs

**REST API**

<https://api.hibt0.com/open-api>

#### Signature Authentication

API requests are susceptible to tampering during transmission over the internet. To ensure that the request has not been altered, private interfaces, excluding public interfaces (basic information, market data), must use your API Key for encryption to verify whether parameters or parameter values have changed during transmission. Each API Key needs appropriate permissions to access the corresponding interfaces, and each newly created API Key requires assignment of permissions. Before using an interface, please check the permission type for each interface and confirm that your API Key has the necessary permissions.

What is required for a legitimate request:

* Method request address:  That is, the access server address <https://api.hibt0.co/open-api。>
* API Access Key (X-ACCESS-KEY) : The Access Key in the API Key you applied for.
* Required and Optional Parameters: Each method has a set of required and optional parameters for defining API calls. You can review these parameters and their meanings in the documentation for each method.
* Signature: The value calculated by encryption, used to ensure that the signature is valid and has not been tampered with,  **For the security of your API Key, a parameter signature will expire after 5 minutes.**
* **Signature Required Parameters \*\* : For interfaces that require signature authentication, the reqTime parameter must be added (the value passed is the latest server time, which can be obtained through the/v1/common/systemTime interface).**

#### Encryption

Standardize the Request for Signature Calculation: Because using HMAC for signature calculation results in completely different outcomes for different content, it's essential to standardize the request before performing signature calculation. The following example illustrates the process using a request to query details for a specific order:

Order Request URL

```
https://api.hibt0.com/open-api/v1/trade/order?amount=0.12&direction=ASK&price=7126.4285&symbol=BTC_USDT&reqTime=1672502400000
```

Sort parameters in ASCII order:

```
amount=0.12&direction=ASK&price=7126.4285&reqTime=1672502400000&symbol=BTC_USDT
```

The result obtained by encrypting the sorted request parameters with HMAC SHA256 using secretKey:

```
550ac73ace8c34372e0e1dd6631e890c7bd16697af8bb4e2908e966b50aba4e0
```

#### Build HTTP request usage

1. Using **X-ACCESS-KEY** stores access key information and passes parameters in the header
2. Using **X-Signature** stores the generated signature information and passes parameters in the header

#### Request method

There are currently only two methods available: **GET** and **POST**

* GET request: All parameters are in the path parameters
* POST request: All parameters are sent in form data format in the request body

#### Response Format

All interfaces are in JSON format. At the top layer of JSON, there are three fields: `message, code, and data.` The first two fields represent the request status and information, and the actual business data is in the data field.

```
{
  "message": "success",
  "code": "0",
  "data": ""
}
```

### Common failure codes

#### **1xxx (access failure class)**

#### **2xxx (business failure category)**

| Failure code | describe                                                                |
| ------------ | ----------------------------------------------------------------------- |
| 0            | sccuess                                                                 |
| 1001         | Interface request flow limiting                                         |
| 1101         | API Key authentication failed                                           |
| 1102         | Decryption of the key failed                                            |
| 1103         | Access IP is not in the whitelist                                       |
| 2001         | The parameter is empty                                                  |
| 2002         | Time range error                                                        |
| 2003         | The request time parameter is empty                                     |
| 2004         | The request time has expired                                            |
| 2101         | Account does not exist                                                  |
| 2102         | API key does not exist                                                  |
| 2103         | Trading pair does not exist                                             |
| 2201         | User API Key disabled                                                   |
| 2202         | IP is disabled                                                          |
| 9999         | Other exception, please refer to the content of the message for details |

## Spot Interface

### Basic Information Interface

#### **Server Time**

**HTTP Request**

* GET `/v1/common/systemTime`

**Authentication: No**

**Rate Limit: 100 requests per second**

**Request Parameters**

This interface does not accept any parameters.

**Response Fields**

<table><thead><tr><th width="250.33333333333331">Field Name</th><th>Data Type</th><th>Description</th></tr></thead><tbody><tr><td>data</td><td>long</td><td>Server timestamp</td></tr></tbody></table>

```json
{
  "message": "success",
  "code": "0",
  "data": 1672502400000
}
```

#### **All Trading Pair Information**

**HTTP Request**

* GET `/v1/common/symbols`

**Authentication: No**

**Rate Limit: 5 requests per second**

**Request Parameters**

This interface does not accept any parameters.

**Response Fields**

| Field Name    | Data Type | Description                         |
| ------------- | --------- | ----------------------------------- |
| symbol        | string    | Trading Pair                        |
| baseCoinScale | integer   | Quote Currency Quantity Precision   |
| coinScale     | integer   | Base Currency Quantity Precision    |
| priceScale    | integer   | Price Precision                     |
| baseSymbol    | string    | Quote Currency                      |
| coinSymbol    | string    | Base Currency                       |
| minTurnover   | decimal   | Min Order Execution Amount          |
| minVolume     | decimal   | Min Order Quantity                  |
| maxVolume     | decimal   | Max Order Quantity                  |
| enable        | integer   | Is Trading Supported (0-No; 1-Yes)" |

```json
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "symbol": "BTC/USDT", // Trading Pair
      "baseCoinScale": 4, // Quote Currency Quantity Precision
      "coinScale": 4, // Base Currency Quantity Precision
      "priceScale": 2, // Price Precision
      "baseSymbol": "USDT", // Quote Currency
      "coinSymbol":"BTC", // Base Currency
      "minTurnover": 10, // Minimum Order Execution Amount
      "minVolume": 0.001, // Min Order Quantity
      "maxVolume": 50, // Max Order Quantity
      "enable":  1 // Is Trading Supported
    },
    {
      "symbol": "ETH/USDT",
      "baseCoinScale": 4,
      "coinScale": 4,
      "baseSymbol": "USDT",
      "coinSymbol":"ETH",
      "minTurnover": 10,
      "minVolume": 0.01,
      "maxVolume": 500,
      "enable": 1
    }
  ]
}
```

### Market Data Interface

#### **Last Trade Price**

&#x20;   This interface provides the current latest transaction price for the trading pair.

**HTTP Request**

* GET `/v1/market/ticker/price`

**Authentication: No**

**Rate Limit: 10 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description  |
| ---------- | --------- | ----------- | ------------ |
| symbol     | string    | true        | Trading Pair |

**Response Fields**

| Field Name  | Data Type | Description      |
| ----------- | --------- | ---------------- |
| tickerPrice | decimal   | Last Trade Price |

```json
{
  "message": "success",
  "code": "0",
  "data": {
      "tickerPrice": 40000
    }
}
```

#### **Order Book Data**

&#x20;   This interface returns the current depth data for the specified trading pair.

**HTTP Request**

* GET `/v1/market/depth`

**Authentication: No**

**Rate Limit: 10 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description                     | 取值范围    |
| ---------- | --------- | ----------- | ------------------------------- | ------- |
| symbol     | string    | true        | Trading Pair                    |         |
| depth      | integer   | true        | Number of Depth Levels Returned | 最大 50 档 |

**Response Fields**

| Field Name | Data Type | Description    |
| ---------- | --------- | -------------- |
| symbol     | string    | Trading Pair   |
| bids       | array     | Bid Depth List |
| asks       | array     | Ask Depth List |
| timestamp  | datetime  | Time           |

```json
{
  "message": "success",
  "code": "0",
  "data": {
      "symbol" : "BTC/USDT",
      "timestamp" : "2023-11-22 10:00:00",
      "bids" : [ [ "36074.99", "0.27225537" ], [ "36074.81", "0.00967628" ] ],
      "asks" : [ [ "36075.06", "0.55858424" ], [ "36075.24", "0.22475193" ] ]
  }
}
```

**Historical KLines**

This endpoint returns the historical candlestick (K-line) data for a specified trading pair.

**HTTP Request**

**GET** `/v1/market/kline`

**Authentication: No**

**Rate Limit: 2 requests per second**

**Request Parameters**

<table><thead><tr><th>Field Name</th><th>Data Type</th><th>Is required</th><th width="135.05615234375">Description</th><th width="247.8958740234375">Data Range</th></tr></thead><tbody><tr><td>symbol</td><td>string</td><td>true</td><td>symbol</td><td></td></tr><tr><td>period</td><td>string</td><td>true</td><td>period</td><td>Min:1min;5min;15min;30minxHour:1hour;4hour 天:1day Week:1week Month:1month</td></tr><tr><td>from</td><td>long</td><td>true</td><td>start time</td><td>Milliseconds</td></tr><tr><td>to</td><td>long </td><td>false</td><td>end time</td><td>Milliseconds. If not provided, the current time is used.</td></tr><tr><td>limit</td><td>integer</td><td>false</td><td>Number of returned records</td><td>If not provided, the default is 500; the maximum is 1000.</td></tr></tbody></table>

**Response Fields**

```json
{
  "data": [
    [
      "1765555200000", // Open time
      "89926.2",       // Open price
      "90050.0",       // High price
      "89785.5",       // Low price
      "89959.9",       // Close price
      "30.8345",       // Volume
      "2773034.7896",  // Quote asset volume
      "2209"           // Number of trades
    ],
    [
      "1765555260000",
      "89960",
      "90031.5",
      "89863.9",
      "89911.9",
      "19.8816",
      "1788283.7845",
      "1808"
    ]
  ],
  "code": 0,
  "message": "SUCCESS",
  "success": true
}

```

### Historical Trades

This endpoint returns the trade history of a specified trading pair (queried in reverse chronological order).

**HTTP Request**

**GET** `/v1/market/historicalTrades`

**Authentication: No**

**Rate Limit: 2 requests per second**

**Request Parameters**

<table><thead><tr><th>Field Name</th><th>数据类型</th><th>是否必须</th><th width="135.05615234375">描述</th><th width="247.8958740234375">说明</th></tr></thead><tbody><tr><td>symbol</td><td>string</td><td>true</td><td>交易对</td><td></td></tr><tr><td>beforeId</td><td>string</td><td>false</td><td>查询开始id</td><td>查询该id之前的交易记录，不传按最新成交id向前查询</td></tr><tr><td>limit</td><td>integer</td><td>false</td><td>返回条数</td><td>不填默认100，最大100</td></tr></tbody></table>

**Response Fields**

```json
{
  "data": [
    {
      "id": "693d3d73453ac877d3233e55", // Trade ID
      "price": "90487.8",              // Trade price
      "qty": "0.0024",                 // Trade quantity
      "quoteQty": "217.170912",        // Quote asset volume
      "time": 1765621107203,           // Trade time
      "side": "SELL"                   // Trade side: BUY or SELL
    },
    {
      "id": "693d3d72453ac877d3233e14",
      "price": "90487.8",
      "qty": "0.0026976",
      "quoteQty": "244.10013216",
      "time": 1765621106245,
      "side": "BUY"
    }
  ],
  "code": 0,
  "message": "SUCCESS",
  "success": true
}
```

### Account Interface

#### **Account Balance**

**HTTP Request**

* POST `/v1/account/balance`

**Authentication: Yes**

**Rate Limit: 5 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description |
| ---------- | --------- | ----------- | ----------- |
| coin       | string    | false       | Currency    |

**Response Fields**

| Field Name    | Data Type | Description    |
| ------------- | --------- | -------------- |
| coin          | string    | Currency       |
| balance       | decimal   | Balance        |
| frozenBalance | decimal   | Frozen Balance |
| isLock        | string    | Lock Status    |

```json
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "coin": "USDT",
      "balance": 1000,
      "frozenBalance": 1000,
      "isLock": "IS_FALSE"
    },{
      "coin": BTC,
      "balance": 1,
      "frozenBalance": 0.01,
      "isLock": "IS_TRUE"
    }
  ]
}
```

### Trading Interface

#### **Open Orders**

**HTTP Request**

* POST `/v1/trade/openOrder`

**Authentication: Yes**

**Rate Limit: 10 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description               |
| ---------- | --------- | ----------- | ------------------------- |
| symbol     | string    | true        | Trading Pair              |
| direction  | integer   | true        | Direction (0-Buy; 1-Sell) |

**Response Fields**

| Field Name    | Data Type | Description                                                                    |
| ------------- | --------- | ------------------------------------------------------------------------------ |
| orderId       | string    | Order ID                                                                       |
| clOrdId       | string    | Customer Custom Order ID                                                       |
| price         | decimal   | Order Price                                                                    |
| avgPrice      | decimal   | Average Transaction Price                                                      |
| amount        | decimal   | Order Amount                                                                   |
| tradedAmount  | decimal   | Filled Quantity                                                                |
| turnover      | decimal   | Transaction Amount (Filled Quantity \* Transaction Price)                      |
| symbol        | string    | Trading Pair                                                                   |
| baseSymbol    | string    | Quote Currency                                                                 |
| coinSymbol    | string    | Base Currency                                                                  |
| direction     | integer   | Direction (0-Buy; 1-Sell)                                                      |
| status        | integer   | Status (0-In Progress; 1-Completed; 2-Canceled; 3-Timeout; 4-Partially Filled) |
| type          | integer   | Type (0-Market Order; 1-Limit Order)                                           |
| completedTime | long      | Order Completion Time                                                          |
| canceledTime  | long      | Order Cancel Time                                                              |
| time          | long      | Order Create Time                                                              |

```json
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677194831589408768",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 0,
      "amount": 0.1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677269378757951488",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 0,
      "amount": 1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
```

#### **Historical Orders (Last 3 Months)**

**HTTP Request**

* POST `/v1/trade/history`

**Authentication: Yes**

**Rate Limit: 10 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description               |
| ---------- | --------- | ----------- | ------------------------- |
| symbol     | string    | true        | Trading Pair              |
| startTime  | long      | true        | Start Time (milliseconds) |
| endTime    | long      | true        | End Time (milliseconds)   |

**Response Fields**

| Field Name    | Data Type | Description                                                                    |
| ------------- | --------- | ------------------------------------------------------------------------------ |
| orderId       | string    | Order ID                                                                       |
| clOrdId       | string    | Customer Custom Order ID                                                       |
| price         | decimal   | Order Price                                                                    |
| avgPrice      | decimal   | Average Transaction Price                                                      |
| amount        | decimal   | Order Amount                                                                   |
| tradedAmount  | decimal   | Filled Quantity                                                                |
| turnover      | decimal   | Transaction Amount (Filled Quantity \* Transaction Price)                      |
| symbol        | string    | Trading Pair                                                                   |
| baseSymbol    | string    | Quote Currency                                                                 |
| coinSymbol    | string    | Base Currency                                                                  |
| direction     | integer   | Direction (0-Buy; 1-Sell)                                                      |
| status        | integer   | Status (0-In Progress; 1-Completed; 2-Canceled; 3-Timeout; 4-Partially Filled) |
| type          | integer   | Type (0-Market Order; 1-Limit Order)                                           |
| completedTime | long      | Order Completion Time                                                          |
| canceledTime  | long      | Order Cancel Time                                                              |
| time          | long      | Order Create Time                                                              |

```json
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677226372826791936",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 35000,
      "amount": 0.1,
      "tradedAmount": 0.1,
      "turnover": 3500,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677261905426776064",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 2000,
      "amount": 1,
      "tradedAmount": 1,
      "turnover": 2000,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
```

#### **Create Order**

**HTTP Request**

* POST `/v1/trade/order`

**Authentication: Yes**

**Rate Limit: 20 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description                                                                                                                                    |
| ---------- | --------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| symbol     | string    | true        | Trading Pair                                                                                                                                   |
| price      | decimal   | true        | Price (Set to 0 for Market Order)                                                                                                              |
| amount     | decimal   | true        | Quantity (For Market Buy Order: Represents the amount to buy in USDT; For Market Sell Order: Represents the quantity of base currency to sell) |
| direction  | integer   | true        | Direction (0-Buy; 1-Sell)                                                                                                                      |
| type       | integer   | true        | Type (0-Market Order; 1-Limit Order)                                                                                                           |

**Response Fields**

| Field Name | Data Type | Description |
| ---------- | --------- | ----------- |
| data       | string    | Order ID    |

```json
{
  "message": "success",
  "code": "0",
  "data": "E1677226372826791936"
}
```

#### **Cancel Order**

**HTTP Request**

* POST `/v1/trade/cancel`

**Authentication: Yes**

**Rate Limit: 20 requests per second**

**Request Parameters**

| Field Name | Data Type | Is required | Description  |
| ---------- | --------- | ----------- | ------------ |
| symbol     | string    | true        | Trading Pair |
| orderId    | string    | true        | Order ID     |

**Response Fields**

```json
{
  "message": "success",
  "code": "0",
  "data": ""
}
```
