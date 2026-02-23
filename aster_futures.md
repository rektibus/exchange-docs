General Info
Overview¶
This API may require the user's AGENT.
To create an AGENT please click here and switch to Pro API at the top
The base endpoint is: https://fapi.asterdex.com
All endpoints return either a JSON object or array.
Data is returned in ascending order. Oldest first, newest last.
All time and timestamp related fields are in milliseconds.
All data types adopt definition in JAVA.
HTTP Return Codes¶
HTTP 4XX return codes are used for for malformed requests; the issue is on the sender's side.
HTTP 403 return code is used when the WAF Limit (Web Application Firewall) has been violated.
HTTP 429 return code is used when breaking a request rate limit.
HTTP 418 return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.
HTTP 5XX return codes are used for internal errors; the issue is on Aster's side.
HTTP 503 return code is used when the API successfully sent the message but not get a response within the timeout period. It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success.
Error Codes and Messages¶
Any endpoint can return an ERROR
The error payload is as follows:


{
  "code": -1121,
  "msg": "Invalid symbol."
}
Specific error codes and messages defined in Error Codes Page.
General Information on Endpoints¶
For GET endpoints, parameters must be sent as a query string.
For POST, PUT, and DELETE method APIs, send data in the request body (content type application/x-www-form-urlencoded)
Parameters may be sent in any order.
LIMITS¶
The /fapi/v3/exchangeInfo rateLimits array contains objects related to the exchange's RAW_REQUEST, REQUEST_WEIGHT, and ORDER rate limits. These are further defined in the ENUM definitions section under Rate limiters (rateLimitType).
A 429 will be returned when either rate limit is violated.
Aster Finance has the right to further tighten the rate limits on users with intent to attack.
IP Limits¶
Every request will contain X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter) in the response headers which has the current used weight for the IP for all request rate limiters defined.
Each route has a weight which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier weight.
When a 429 is received, it's your obligation as an API to back off and not spam the API.
Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).
IP bans are tracked and scale in duration for repeat offenders, from 2 minutes to 3 days.
The limits on the API are based on the IPs, not the API keys.
It is strongly recommended to use websocket stream for getting data as much as possible, which can not only ensure the timeliness of the message, but also reduce the access restriction pressure caused by the request.
Order Rate Limits¶
Every order response will contain a X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter) header which has the current order count for the account for all order rate limiters defined.
Rejected/unsuccessful orders are not guaranteed to have X-MBX-ORDER-COUNT-** headers in the response.
The order rate limit is counted against each account.
Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less!
API authentication type¶
Each API has its own authentication type, which determines what kind of authentication is required when accessing it.
If authentication is required, a signer should be included in the request body.
Security Type	Description
NONE	API that does not require authentication
TRADE	A valid signer and signature are required
USER_DATA	A valid signer and signature are required
USER_STREAM	A valid signer and signature are required
MARKET_DATA	A valid signer and signature are required
Authentication signature payload¶
Parameter	Description
user	Main account wallet address
signer	API wallet address
nonce	Current timestamp, in microseconds
signature	Signature
Endpoints requiring signature¶
Security Type: TRADE, USER_DATA, USER_STREAM, MARKET_DATA
After converting the API parameters to strings, sort them by their key values in ASCII order to generate the final string. Note: All parameter values must be treated as strings during the signing process.
After generating the string, combine it with the authentication signature parameters user, signer, and nonce, then use Web3’s ABI parameter encoding to generate the bytecode.
After generating the bytecode, use the Keccak algorithm to generate the hash.
Use the private key of API wallet address to sign the hash using web3’s ECDSA signature algorithm, generating the final signature.
Timing Security¶
A SIGNED endpoint also requires a parameter, timestamp, to be sent which should be the millisecond timestamp of when the request was created and sent.
An additional parameter, recvWindow, may be sent to specify the number of milliseconds after timestamp the request is valid for. If recvWindow is not sent, it defaults to 5000.
The logic is as follows:


if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow){
    // process request
  } 
  else {
    // reject request
  }
Example of POST /fapi/v3/order¶
All parameters are passed through the request body (Python 3.9.6)¶
The following parameters are API registration details. The values for user, signer, and privateKey are for demonstration purposes only (the privateKey corresponds to the signer).¶
Key	Value	Desc
user	0x63DD5aCC6b1aa0f563956C0e534DD30B6dcF7C4e	Login wallet address
signer	0x21cF8Ae13Bb72632562c6Fff438652Ba1a151bb0	Click Here
privateKey	0x4fd0a42218f3eae43a6ce26d22544e986139a01e5b34a62db53757ffca81bae1	Click Here
The nonce parameter is the current system time in microseconds. If it exceeds the system time or lags behind it by more than 5 seconds, the request is considered invalid.¶

#python
nonce = math.trunc(time.time()*1000000)
print(nonce)
#1748310859508867

//java
Instant now = Instant.now();
long microsecond = now.getEpochSecond() * 1000000 + now.getNano() / 1000;
Example: Post an order (using Python as an example).¶

import time
import requests
from eth_account.messages import  encode_structured_data
from eth_account import Account

typed_data = {
  "types": {
    "EIP712Domain": [
      {"name": "name", "type": "string"},
      {"name": "version", "type": "string"},
      {"name": "chainId", "type": "uint256"},
      {"name": "verifyingContract", "type": "address"}
    ],
    "Message": [
      { "name": "msg", "type": "string" }
    ]
  },
  "primaryType": "Message",
  "domain": {
    "name": "AsterSignTransaction",
    "version": "1",
    "chainId": 1666,
    "verifyingContract": "0x0000000000000000000000000000000000000000"
  },
  "message": {
    "msg": "$msg"
  }
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'PythonApp/1.0'
}
order_url = 'https://fapi.asterdex-testnet.com/fapi/v3/order'

# config your user and agent info here
user = '*'
signer = '*'
private_key = "*"

def get_url(my_dict) -> str:
       return '&'.join(f'{key}={str(value)}'for key, value in my_dict.items())

_last_ms = 0
_i = 0

def get_nonce():
    global _last_ms, _i
    now_ms = int(time.time())

    if now_ms == _last_ms:
        _i += 1
    else:
        _last_ms = now_ms
        _i = 0

    return now_ms * 1_000_000 + _i

def send_by_url() :
    param = 'symbol=ASTERUSDT&side=BUY&type=LIMIT&quantity=10&price=0.6&timeInForce=GTC'

    param += '&nonce=' + str(get_nonce())
    param += '&user=' + user
    param += '&signer=' + signer

    typed_data['message']['msg'] = param
    message = encode_structured_data(typed_data)
    signed = Account.sign_message(message, private_key=private_key)
    print(signed.signature.hex())

    url = order_url + '?' + param + '&signature=' + signed.signature.hex()

    print(url)
    res = requests.post(url, headers=headers)

    print(res.text)

def send_by_body() :
       my_dict = {"symbol": "ASTERUSDT", "type": "LIMIT", "side": "BUY",
                  "timeInForce": "GTC", "quantity": "10", "price": "0.6"}

       my_dict['nonce'] = str(get_nonce())
       my_dict['user'] = user
       my_dict['signer'] = signer

       content = get_url(my_dict)
       typed_data['message']['msg'] = content
       message = encode_structured_data(typed_data)

       signed = Account.sign_message(message, private_key=private_key)
       print(signed.signature.hex())

       my_dict['signature'] = signed.signature.hex()

       print(my_dict)
       res = requests.post(order_url, data=my_dict, headers=headers)

       print(res.text)

if __name__ == '__main__':
    send_by_url()
    # send_by_body()
Public Endpoints Info¶
Terminology¶
base asset refers to the asset that is the quantity of a symbol.
quote asset refers to the asset that is the price of a symbol.
ENUM definitions¶
Symbol type:

FUTURE
Contract type (contractType):

PERPETUAL
Contract status(contractStatus，status):

PENDING_TRADING
TRADING
PRE_SETTLE
SETTLING
CLOSE
Order status (status):

NEW
PARTIALLY_FILLED
FILLED
CANCELED
REJECTED
EXPIRED
Order types (orderTypes, type):

LIMIT
MARKET
STOP
STOP_MARKET
TAKE_PROFIT
TAKE_PROFIT_MARKET
TRAILING_STOP_MARKET
Order side (side):

BUY
SELL
Position side (positionSide):

BOTH
LONG
SHORT
Time in force (timeInForce):

GTC - Good Till Cancel
IOC - Immediate or Cancel
FOK - Fill or Kill
GTX - Good Till Crossing (Post Only)
Working Type (workingType)

MARK_PRICE
CONTRACT_PRICE
Response Type (newOrderRespType)

ACK
RESULT
Kline/Candlestick chart intervals:

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
Rate limiters (rateLimitType)

REQUEST_WEIGHT


{
    "rateLimitType": "REQUEST_WEIGHT",
    "interval": "MINUTE",
    "intervalNum": 1,
    "limit": 2400
  }
ORDERS


{
    "rateLimitType": "ORDERS",
    "interval": "MINUTE",
    "intervalNum": 1,
    "limit": 1200
   }
REQUEST_WEIGHT
ORDERS
Rate limit intervals (interval)

MINUTE
Filters¶
Filters define trading rules on a symbol or an exchange.

Symbol filters¶
PRICE_FILTER¶
/exchangeInfo format:


{
    "filterType": "PRICE_FILTER",
    "minPrice": "0.00000100",
    "maxPrice": "100000.00000000",
    "tickSize": "0.00000100"
  }
The PRICE_FILTER defines the price rules for a symbol. There are 3 parts:

minPrice defines the minimum price/stopPrice allowed; disabled on minPrice == 0.
maxPrice defines the maximum price/stopPrice allowed; disabled on maxPrice == 0.
tickSize defines the intervals that a price/stopPrice can be increased/decreased by; disabled on tickSize == 0.
Any of the above variables can be set to 0, which disables that rule in the price filter. In order to pass the price filter, the following must be true for price/stopPrice of the enabled rules:

price >= minPrice
price <= maxPrice
(price-minPrice) % tickSize == 0
LOT_SIZE¶
/exchangeInfo format:


{
    "filterType": "LOT_SIZE",
    "minQty": "0.00100000",
    "maxQty": "100000.00000000",
    "stepSize": "0.00100000"
  }
The LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

minQty defines the minimum quantity allowed.
maxQty defines the maximum quantity allowed.
stepSize defines the intervals that a quantity can be increased/decreased by.
In order to pass the lot size, the following must be true for quantity:

quantity >= minQty
quantity <= maxQty
(quantity-minQty) % stepSize == 0
MARKET_LOT_SIZE¶
/exchangeInfo format:


{
    "filterType": "MARKET_LOT_SIZE",
    "minQty": "0.00100000",
    "maxQty": "100000.00000000",
    "stepSize": "0.00100000"
  }
The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for MARKET orders on a symbol. There are 3 parts:

minQty defines the minimum quantity allowed.
maxQty defines the maximum quantity allowed.
stepSize defines the intervals that a quantity can be increased/decreased by.
In order to pass the market lot size, the following must be true for quantity:

quantity >= minQty
quantity <= maxQty
(quantity-minQty) % stepSize == 0
MAX_NUM_ORDERS¶
/exchangeInfo format:


{
    "filterType": "MAX_NUM_ORDERS",
    "limit": 200
  }
The MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open on a symbol.

Note that both "algo" orders and normal orders are counted for this filter.

MAX_NUM_ALGO_ORDERS¶
/exchangeInfo format:


{
    "filterType": "MAX_NUM_ALGO_ORDERS",
    "limit": 100
  }
The MAX_NUM_ALGO_ORDERS filter defines the maximum number of all kinds of algo orders an account is allowed to have open on a symbol.

The algo orders include STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET, and TRAILING_STOP_MARKET orders.

PERCENT_PRICE¶
/exchangeInfo format:


{
    "filterType": "PERCENT_PRICE",
    "multiplierUp": "1.1500",
    "multiplierDown": "0.8500",
    "multiplierDecimal": 4
  }
The PERCENT_PRICE filter defines valid range for a price based on the mark price.

In order to pass the percent price, the following must be true for price:

BUY: price <= markPrice * multiplierUp
SELL: price >= markPrice * multiplierDown
MIN_NOTIONAL¶
/exchangeInfo format:


{
    "filterType": "MIN_NOTIONAL",
    "notional": "1"
  }
The MIN_NOTIONAL filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the price * quantity. Since MARKET orders have no price, the mark price is used.







General Info
Overview¶
This API may require the user's AGENT.
To create an AGENT please click here and switch to Pro API at the top
The base endpoint is: https://fapi.asterdex.com
All endpoints return either a JSON object or array.
Data is returned in ascending order. Oldest first, newest last.
All time and timestamp related fields are in milliseconds.
All data types adopt definition in JAVA.
HTTP Return Codes¶
HTTP 4XX return codes are used for for malformed requests; the issue is on the sender's side.
HTTP 403 return code is used when the WAF Limit (Web Application Firewall) has been violated.
HTTP 429 return code is used when breaking a request rate limit.
HTTP 418 return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.
HTTP 5XX return codes are used for internal errors; the issue is on Aster's side.
HTTP 503 return code is used when the API successfully sent the message but not get a response within the timeout period. It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success.
Error Codes and Messages¶
Any endpoint can return an ERROR
The error payload is as follows:


{
  "code": -1121,
  "msg": "Invalid symbol."
}
Specific error codes and messages defined in Error Codes Page.
General Information on Endpoints¶
For GET endpoints, parameters must be sent as a query string.
For POST, PUT, and DELETE method APIs, send data in the request body (content type application/x-www-form-urlencoded)
Parameters may be sent in any order.
LIMITS¶
The /fapi/v3/exchangeInfo rateLimits array contains objects related to the exchange's RAW_REQUEST, REQUEST_WEIGHT, and ORDER rate limits. These are further defined in the ENUM definitions section under Rate limiters (rateLimitType).
A 429 will be returned when either rate limit is violated.
Aster Finance has the right to further tighten the rate limits on users with intent to attack.
IP Limits¶
Every request will contain X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter) in the response headers which has the current used weight for the IP for all request rate limiters defined.
Each route has a weight which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier weight.
When a 429 is received, it's your obligation as an API to back off and not spam the API.
Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).
IP bans are tracked and scale in duration for repeat offenders, from 2 minutes to 3 days.
The limits on the API are based on the IPs, not the API keys.
It is strongly recommended to use websocket stream for getting data as much as possible, which can not only ensure the timeliness of the message, but also reduce the access restriction pressure caused by the request.
Order Rate Limits¶
Every order response will contain a X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter) header which has the current order count for the account for all order rate limiters defined.
Rejected/unsuccessful orders are not guaranteed to have X-MBX-ORDER-COUNT-** headers in the response.
The order rate limit is counted against each account.
Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less!
API authentication type¶
Each API has its own authentication type, which determines what kind of authentication is required when accessing it.
If authentication is required, a signer should be included in the request body.
Security Type	Description
NONE	API that does not require authentication
TRADE	A valid signer and signature are required
USER_DATA	A valid signer and signature are required
USER_STREAM	A valid signer and signature are required
MARKET_DATA	A valid signer and signature are required
Authentication signature payload¶
Parameter	Description
user	Main account wallet address
signer	API wallet address
nonce	Current timestamp, in microseconds
signature	Signature
Endpoints requiring signature¶
Security Type: TRADE, USER_DATA, USER_STREAM, MARKET_DATA
After converting the API parameters to strings, sort them by their key values in ASCII order to generate the final string. Note: All parameter values must be treated as strings during the signing process.
After generating the string, combine it with the authentication signature parameters user, signer, and nonce, then use Web3’s ABI parameter encoding to generate the bytecode.
After generating the bytecode, use the Keccak algorithm to generate the hash.
Use the private key of API wallet address to sign the hash using web3’s ECDSA signature algorithm, generating the final signature.
Timing Security¶
A SIGNED endpoint also requires a parameter, timestamp, to be sent which should be the millisecond timestamp of when the request was created and sent.
An additional parameter, recvWindow, may be sent to specify the number of milliseconds after timestamp the request is valid for. If recvWindow is not sent, it defaults to 5000.
The logic is as follows:


if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow){
    // process request
  } 
  else {
    // reject request
  }
Example of POST /fapi/v3/order¶
All parameters are passed through the request body (Python 3.9.6)¶
The following parameters are API registration details. The values for user, signer, and privateKey are for demonstration purposes only (the privateKey corresponds to the signer).¶
Key	Value	Desc
user	0x63DD5aCC6b1aa0f563956C0e534DD30B6dcF7C4e	Login wallet address
signer	0x21cF8Ae13Bb72632562c6Fff438652Ba1a151bb0	Click Here
privateKey	0x4fd0a42218f3eae43a6ce26d22544e986139a01e5b34a62db53757ffca81bae1	Click Here
The nonce parameter is the current system time in microseconds. If it exceeds the system time or lags behind it by more than 5 seconds, the request is considered invalid.¶

#python
nonce = math.trunc(time.time()*1000000)
print(nonce)
#1748310859508867

//java
Instant now = Instant.now();
long microsecond = now.getEpochSecond() * 1000000 + now.getNano() / 1000;
Example: Post an order (using Python as an example).¶

import time
import requests
from eth_account.messages import  encode_structured_data
from eth_account import Account

typed_data = {
  "types": {
    "EIP712Domain": [
      {"name": "name", "type": "string"},
      {"name": "version", "type": "string"},
      {"name": "chainId", "type": "uint256"},
      {"name": "verifyingContract", "type": "address"}
    ],
    "Message": [
      { "name": "msg", "type": "string" }
    ]
  },
  "primaryType": "Message",
  "domain": {
    "name": "AsterSignTransaction",
    "version": "1",
    "chainId": 1666,
    "verifyingContract": "0x0000000000000000000000000000000000000000"
  },
  "message": {
    "msg": "$msg"
  }
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'PythonApp/1.0'
}
order_url = 'https://fapi.asterdex-testnet.com/fapi/v3/order'

# config your user and agent info here
user = '*'
signer = '*'
private_key = "*"

def get_url(my_dict) -> str:
       return '&'.join(f'{key}={str(value)}'for key, value in my_dict.items())

_last_ms = 0
_i = 0

def get_nonce():
    global _last_ms, _i
    now_ms = int(time.time())

    if now_ms == _last_ms:
        _i += 1
    else:
        _last_ms = now_ms
        _i = 0

    return now_ms * 1_000_000 + _i

def send_by_url() :
    param = 'symbol=ASTERUSDT&side=BUY&type=LIMIT&quantity=10&price=0.6&timeInForce=GTC'

    param += '&nonce=' + str(get_nonce())
    param += '&user=' + user
    param += '&signer=' + signer

    typed_data['message']['msg'] = param
    message = encode_structured_data(typed_data)
    signed = Account.sign_message(message, private_key=private_key)
    print(signed.signature.hex())

    url = order_url + '?' + param + '&signature=' + signed.signature.hex()

    print(url)
    res = requests.post(url, headers=headers)

    print(res.text)

def send_by_body() :
       my_dict = {"symbol": "ASTERUSDT", "type": "LIMIT", "side": "BUY",
                  "timeInForce": "GTC", "quantity": "10", "price": "0.6"}

       my_dict['nonce'] = str(get_nonce())
       my_dict['user'] = user
       my_dict['signer'] = signer

       content = get_url(my_dict)
       typed_data['message']['msg'] = content
       message = encode_structured_data(typed_data)

       signed = Account.sign_message(message, private_key=private_key)
       print(signed.signature.hex())

       my_dict['signature'] = signed.signature.hex()

       print(my_dict)
       res = requests.post(order_url, data=my_dict, headers=headers)

       print(res.text)

if __name__ == '__main__':
    send_by_url()
    # send_by_body()
Public Endpoints Info¶
Terminology¶
base asset refers to the asset that is the quantity of a symbol.
quote asset refers to the asset that is the price of a symbol.
ENUM definitions¶
Symbol type:

FUTURE
Contract type (contractType):

PERPETUAL
Contract status(contractStatus，status):

PENDING_TRADING
TRADING
PRE_SETTLE
SETTLING
CLOSE
Order status (status):

NEW
PARTIALLY_FILLED
FILLED
CANCELED
REJECTED
EXPIRED
Order types (orderTypes, type):

LIMIT
MARKET
STOP
STOP_MARKET
TAKE_PROFIT
TAKE_PROFIT_MARKET
TRAILING_STOP_MARKET
Order side (side):

BUY
SELL
Position side (positionSide):

BOTH
LONG
SHORT
Time in force (timeInForce):

GTC - Good Till Cancel
IOC - Immediate or Cancel
FOK - Fill or Kill
GTX - Good Till Crossing (Post Only)
Working Type (workingType)

MARK_PRICE
CONTRACT_PRICE
Response Type (newOrderRespType)

ACK
RESULT
Kline/Candlestick chart intervals:

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
Rate limiters (rateLimitType)

REQUEST_WEIGHT


{
    "rateLimitType": "REQUEST_WEIGHT",
    "interval": "MINUTE",
    "intervalNum": 1,
    "limit": 2400
  }
ORDERS


{
    "rateLimitType": "ORDERS",
    "interval": "MINUTE",
    "intervalNum": 1,
    "limit": 1200
   }
REQUEST_WEIGHT
ORDERS
Rate limit intervals (interval)

MINUTE
Filters¶
Filters define trading rules on a symbol or an exchange.

Symbol filters¶
PRICE_FILTER¶
/exchangeInfo format:


{
    "filterType": "PRICE_FILTER",
    "minPrice": "0.00000100",
    "maxPrice": "100000.00000000",
    "tickSize": "0.00000100"
  }
The PRICE_FILTER defines the price rules for a symbol. There are 3 parts:

minPrice defines the minimum price/stopPrice allowed; disabled on minPrice == 0.
maxPrice defines the maximum price/stopPrice allowed; disabled on maxPrice == 0.
tickSize defines the intervals that a price/stopPrice can be increased/decreased by; disabled on tickSize == 0.
Any of the above variables can be set to 0, which disables that rule in the price filter. In order to pass the price filter, the following must be true for price/stopPrice of the enabled rules:

price >= minPrice
price <= maxPrice
(price-minPrice) % tickSize == 0
LOT_SIZE¶
/exchangeInfo format:


{
    "filterType": "LOT_SIZE",
    "minQty": "0.00100000",
    "maxQty": "100000.00000000",
    "stepSize": "0.00100000"
  }
The LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

minQty defines the minimum quantity allowed.
maxQty defines the maximum quantity allowed.
stepSize defines the intervals that a quantity can be increased/decreased by.
In order to pass the lot size, the following must be true for quantity:

quantity >= minQty
quantity <= maxQty
(quantity-minQty) % stepSize == 0
MARKET_LOT_SIZE¶
/exchangeInfo format:


{
    "filterType": "MARKET_LOT_SIZE",
    "minQty": "0.00100000",
    "maxQty": "100000.00000000",
    "stepSize": "0.00100000"
  }
The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for MARKET orders on a symbol. There are 3 parts:

minQty defines the minimum quantity allowed.
maxQty defines the maximum quantity allowed.
stepSize defines the intervals that a quantity can be increased/decreased by.
In order to pass the market lot size, the following must be true for quantity:

quantity >= minQty
quantity <= maxQty
(quantity-minQty) % stepSize == 0
MAX_NUM_ORDERS¶
/exchangeInfo format:


{
    "filterType": "MAX_NUM_ORDERS",
    "limit": 200
  }
The MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open on a symbol.

Note that both "algo" orders and normal orders are counted for this filter.

MAX_NUM_ALGO_ORDERS¶
/exchangeInfo format:


{
    "filterType": "MAX_NUM_ALGO_ORDERS",
    "limit": 100
  }
The MAX_NUM_ALGO_ORDERS filter defines the maximum number of all kinds of algo orders an account is allowed to have open on a symbol.

The algo orders include STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET, and TRAILING_STOP_MARKET orders.

PERCENT_PRICE¶
/exchangeInfo format:


{
    "filterType": "PERCENT_PRICE",
    "multiplierUp": "1.1500",
    "multiplierDown": "0.8500",
    "multiplierDecimal": 4
  }
The PERCENT_PRICE filter defines valid range for a price based on the mark price.

In order to pass the percent price, the following must be true for price:

BUY: price <= markPrice * multiplierUp
SELL: price >= markPrice * multiplierDown
MIN_NOTIONAL¶
/exchangeInfo format:


{
    "filterType": "MIN_NOTIONAL",
    "notional": "1"
  }
The MIN_NOTIONAL filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the price * quantity. Since MARKET orders have no price, the mark price is used.












WebSocket Market Data
Overview¶
The baseurl for websocket is wss://fstream.asterdex.com
Streams can be access either in a single raw stream or a combined stream
Raw streams are accessed at /ws/\<streamName>
Combined streams are accessed at /stream?streams=\<streamName1>/\<streamName2>/\<streamName3>
Combined stream events are wrapped as follows: {"stream":"\<streamName>","data":\<rawPayload>}
All symbols for streams are lowercase
A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark
The websocket server will send a ping frame every 5 minutes. If the websocket server does not receive a pong frame back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
WebSocket connections have a limit of 10 incoming messages per second.
A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
A single connection can listen to a maximum of 200 streams.
Considering the possible data latency from RESTful endpoints during an extremely volatile market, it is highly recommended to get the order status, position, etc from the Websocket user data stream.
Live Subscribing/Unsubscribing to streams¶
The following data can be sent through the websocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
The id used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify the messages going back and forth.
Subscribe to a stream¶
Response


{
  "result": null,
  "id": 1
}
Request
{ "method": "SUBSCRIBE", "params": [ "btcusdt@aggTrade", "btcusdt@depth" ], "id": 1 }

Unsubscribe to a stream¶
Response


{
  "result": null,
  "id": 312
}
Request
{ "method": "UNSUBSCRIBE", "params": [ "btcusdt@depth" ], "id": 312 }

Listing Subscriptions¶
Response


{
  "result": [
    "btcusdt@aggTrade"
  ],
  "id": 3
}
Request
{ "method": "LIST_SUBSCRIPTIONS", "id": 3 }

Setting Properties¶
Currently, the only property can be set is to set whether combined stream payloads are enabled are not. The combined property is set to false when connecting using /ws/ ("raw streams") and true when connecting using /stream/.

Response


{
  "result": null,
  "id": 5
}
Request
{ "method": "SET_PROPERTY", "params": [ "combined", true ], "id": 5 }

Retrieving Properties¶
Response


{
  "result": true, // Indicates that combined is set to true.
  "id": 2
}
Request
{ "method": "GET_PROPERTY", "params": [ "combined" ], "id": 2 }

Error Messages¶
Error Message	Description
{"code": 0, "msg": "Unknown property"}	Parameter used in theSET_PROPERTY or GET_PROPERTY was invalid
{"code": 1, "msg": "Invalid value type: expected Boolean"}	Value should only betrue or false
{"code": 2, "msg": "Invalid request: property name must be a string"}	Property name provided was invalid
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}	Parameterid had to be provided or the value provided in the id parameter is an unsupported type
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one ofSUBSCRIBE, UNSUBSCRIBE, LIST_SUBSCRIPTIONS, SET_PROPERTY, GET_PROPERTY at line 1 column 28"}	Possible typo in the provided method or provided method was neither of the expected values
{"code": 2, "msg": "Invalid request: too many parameters"}	Unnecessary parameters provided in the data
{"code": 2, "msg": "Invalid request: property name must be a string"}	Property name was not provided
{"code": 2, "msg": "Invalid request: missing fieldmethod at line 1 column 73"}	method was not provided in the data
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}	JSON data sent has incorrect syntax.
Aggregate Trade Streams¶
Payload:


{
  "e": "aggTrade",  // Event type
  "E": 123456789,   // Event time
  "s": "BTCUSDT",    // Symbol
  "a": 5933014,     // Aggregate trade ID
  "p": "0.001",     // Price
  "q": "100",       // Quantity
  "f": 100,         // First trade ID
  "l": 105,         // Last trade ID
  "T": 123456785,   // Trade time
  "m": true,        // Is the buyer the market maker?
}
The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.

Stream Name: <symbol>@aggTrade

Update Speed: 100ms

Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.
Mark Price Stream¶
Payload:


{
    "e": "markPriceUpdate",     // Event type
    "E": 1562305380000,         // Event time
    "s": "BTCUSDT",             // Symbol
    "p": "11794.15000000",      // Mark price
    "i": "11784.62659091",      // Index price
    "P": "11784.25641265",      // Estimated Settle Price, only useful in the last hour before the settlement starts
    "r": "0.00038167",          // Funding rate
    "T": 1562306400000          // Next funding time
  }
Mark price and funding rate for a single symbol pushed every 3 seconds or every second.

Stream Name: <symbol>@markPrice or <symbol>@markPrice@1s

Update Speed: 3000ms or 1000ms

Mark Price Stream for All market¶
Payload:


[ 
  {
    "e": "markPriceUpdate",     // Event type
    "E": 1562305380000,         // Event time
    "s": "BTCUSDT",             // Symbol
    "p": "11185.87786614",      // Mark price
    "i": "11784.62659091"       // Index price
    "P": "11784.25641265",      // Estimated Settle Price, only useful in the last hour before the settlement starts
    "r": "0.00030000",          // Funding rate
    "T": 1562306400000          // Next funding time
  }
]
Mark price and funding rate for all symbols pushed every 3 seconds or every second.

Stream Name: !markPrice@arr or !markPrice@arr@1s

Update Speed: 3000ms or 1000ms

Kline/Candlestick Streams¶
Payload:


{
  "e": "kline",     // Event type
  "E": 123456789,   // Event time
  "s": "BTCUSDT",    // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BTCUSDT",  // Symbol
    "i": "1m",      // Interval
    "f": 100,       // First trade ID
    "L": 200,       // Last trade ID
    "o": "0.0010",  // Open price
    "c": "0.0020",  // Close price
    "h": "0.0025",  // High price
    "l": "0.0015",  // Low price
    "v": "1000",    // Base asset volume
    "n": 100,       // Number of trades
    "x": false,     // Is this kline closed?
    "q": "1.0000",  // Quote asset volume
    "V": "500",     // Taker buy base asset volume
    "Q": "0.500",   // Taker buy quote asset volume
    "B": "123456"   // Ignore
  }
}
The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).

Kline/Candlestick chart intervals:

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
Stream Name: <symbol>@kline_<interval>

Update Speed: 250ms

Individual Symbol Mini Ticker Stream¶
Payload:


{
    "e": "24hrMiniTicker",  // Event type
    "E": 123456789,         // Event time
    "s": "BTCUSDT",         // Symbol
    "c": "0.0025",          // Close price
    "o": "0.0010",          // Open price
    "h": "0.0025",          // High price
    "l": "0.0010",          // Low price
    "v": "10000",           // Total traded base asset volume
    "q": "18"               // Total traded quote asset volume
  }
24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

Stream Name: <symbol>@miniTicker

Update Speed: 500ms

All Market Mini Tickers Stream¶
Payload:


[  
  {
    "e": "24hrMiniTicker",  // Event type
    "E": 123456789,         // Event time
    "s": "BTCUSDT",         // Symbol
    "c": "0.0025",          // Close price
    "o": "0.0010",          // Open price
    "h": "0.0025",          // High price
    "l": "0.0010",          // Low price
    "v": "10000",           // Total traded base asset volume
    "q": "18"               // Total traded quote asset volume
  }
]
24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

Stream Name: !miniTicker@arr

Update Speed: 1000ms

Individual Symbol Ticker Streams¶
Payload:


{
  "e": "24hrTicker",  // Event type
  "E": 123456789,     // Event time
  "s": "BTCUSDT",     // Symbol
  "p": "0.0015",      // Price change
  "P": "250.00",      // Price change percent
  "w": "0.0018",      // Weighted average price
  "c": "0.0025",      // Last price
  "Q": "10",          // Last quantity
  "o": "0.0010",      // Open price
  "h": "0.0025",      // High price
  "l": "0.0010",      // Low price
  "v": "10000",       // Total traded base asset volume
  "q": "18",          // Total traded quote asset volume
  "O": 0,             // Statistics open time
  "C": 86400000,      // Statistics close time
  "F": 0,             // First trade ID
  "L": 18150,         // Last trade Id
  "n": 18151          // Total number of trades
}
24hr rollwing window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

Stream Name: <symbol>@ticker

Update Speed: 500ms

All Market Tickers Streams¶
Payload:


[
    {
      "e": "24hrTicker",  // Event type
      "E": 123456789,     // Event time
      "s": "BTCUSDT",     // Symbol
      "p": "0.0015",      // Price change
      "P": "250.00",      // Price change percent
      "w": "0.0018",      // Weighted average price
      "c": "0.0025",      // Last price
      "Q": "10",          // Last quantity
      "o": "0.0010",      // Open price
      "h": "0.0025",      // High price
      "l": "0.0010",      // Low price
      "v": "10000",       // Total traded base asset volume
      "q": "18",          // Total traded quote asset volume
      "O": 0,             // Statistics open time
      "C": 86400000,      // Statistics close time
      "F": 0,             // First trade ID
      "L": 18150,         // Last trade Id
      "n": 18151          // Total number of trades
    }
]
24hr rollwing window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

Stream Name: !ticker@arr

Update Speed: 1000ms

Individual Symbol Book Ticker Streams¶
Payload:


{
  "e":"bookTicker",         // event type
  "u":400900217,            // order book updateId
  "E": 1568014460893,       // event time
  "T": 1568014460891,       // transaction time
  "s":"BNBUSDT",            // symbol
  "b":"25.35190000",        // best bid price
  "B":"31.21000000",        // best bid qty
  "a":"25.36520000",        // best ask price
  "A":"40.66000000"         // best ask qty
}
Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

Stream Name: <symbol>@bookTicker

Update Speed: Real-time

All Book Tickers Stream¶
Payload:


{
  // Same as <symbol>@bookTicker payload
}
Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

Stream Name: !bookTicker

Update Speed: Real-time

Liquidation Order Streams¶
Payload:


{

    "e":"forceOrder",                   // Event Type
    "E":1568014460893,                  // Event Time
    "o":{

        "s":"BTCUSDT",                   // Symbol
        "S":"SELL",                      // Side
        "o":"LIMIT",                     // Order Type
        "f":"IOC",                       // Time in Force
        "q":"0.014",                     // Original Quantity
        "p":"9910",                      // Price
        "ap":"9910",                     // Average Price
        "X":"FILLED",                    // Order Status
        "l":"0.014",                     // Order Last Filled Quantity
        "z":"0.014",                     // Order Filled Accumulated Quantity
        "T":1568014460893,               // Order Trade Time

    }

}
The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.

For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

Stream Name: <symbol>@forceOrder

Update Speed: 1000ms

All Market Liquidation Order Streams¶
Payload:


{

    "e":"forceOrder",                   // Event Type
    "E":1568014460893,                  // Event Time
    "o":{

        "s":"BTCUSDT",                   // Symbol
        "S":"SELL",                      // Side
        "o":"LIMIT",                     // Order Type
        "f":"IOC",                       // Time in Force
        "q":"0.014",                     // Original Quantity
        "p":"9910",                      // Price
        "ap":"9910",                     // Average Price
        "X":"FILLED",                    // Order Status
        "l":"0.014",                     // Order Last Filled Quantity
        "z":"0.014",                     // Order Filled Accumulated Quantity
        "T":1568014460893,               // Order Trade Time

    }

}
The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market.

For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

Stream Name: !forceOrder@arr

Update Speed: 1000ms

Partial Book Depth Streams¶
Payload:


{
  "e": "depthUpdate", // Event type
  "E": 1571889248277, // Event time
  "T": 1571889248276, // Transaction time
  "s": "BTCUSDT",
  "U": 390497796,
  "u": 390497878,
  "pu": 390497794,
  "b": [          // Bids to be updated
    [
      "7403.89",  // Price Level to be
      "0.002"     // Quantity
    ],
    [
      "7403.90",
      "3.906"
    ],
    [
      "7404.00",
      "1.428"
    ],
    [
      "7404.85",
      "5.239"
    ],
    [
      "7405.43",
      "2.562"
    ]
  ],
  "a": [          // Asks to be updated
    [
      "7405.96",  // Price level to be
      "3.340"     // Quantity
    ],
    [
      "7406.63",
      "4.525"
    ],
    [
      "7407.08",
      "2.475"
    ],
    [
      "7407.15",
      "4.800"
    ],
    [
      "7407.20",
      "0.175"
    ]
  ]
}
Top <levels> bids and asks, Valid <levels> are 5, 10, or 20.

Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@500ms OR <symbol>@depth<levels>@100ms.

Update Speed: 250ms, 500ms or 100ms

Diff. Book Depth Streams¶
Payload:


{
  "e": "depthUpdate", // Event type
  "E": 123456789,     // Event time
  "T": 123456788,     // Transaction time 
  "s": "BTCUSDT",     // Symbol
  "U": 157,           // First update ID in event
  "u": 160,           // Final update ID in event
  "pu": 149,          // Final update Id in last stream(ie `u` in last stream)
  "b": [              // Bids to be updated
    [
      "0.0024",       // Price level to be updated
      "10"            // Quantity
    ]
  ],
  "a": [              // Asks to be updated
    [
      "0.0026",       // Price level to be updated
      "100"          // Quantity
    ]
  ]
}
Bids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing)

Stream Name: <symbol>@depth OR <symbol>@depth@500ms OR <symbol>@depth@100ms

Update Speed: 250ms, 500ms, 100ms

How to manage a local order book correctly¶
Open a stream to wss://fstream.asterdex.com/stream?streams=btcusdt@depth.
Buffer the events you receive from the stream. For same price, latest received update covers the previous one.
Get a depth snapshot from https://fapi.asterdex.com/fapi/v3/depth?symbol=BTCUSDT&limit=1000 .
Drop any event where u is < lastUpdateId in the snapshot.
The first processed event should have U <= lastUpdateId AND u >= lastUpdateId
While listening to the stream, each new event's pu should be equal to the previous event's u, otherwise initialize the process from step 3.
The data in each event is the absolute quantity for a price level.
If the quantity is 0, remove the price level.
Receiving an event that removes a price level that is not in your local order book can happen and is normal.





Error Codes
Overview¶
Here is the error JSON payload:


{
  "code":-1121,
  "msg":"Invalid symbol."
}
Errors consist of two parts: an error code and a message. Codes are universal,but messages can vary.

10xx - General Server or Network issues¶
-1000 UNKNOWN

An unknown error occured while processing the request.
-1001 DISCONNECTED

Internal error; unable to process your request. Please try again.
-1002 UNAUTHORIZED

You are not authorized to execute this request.
-1003 TOO_MANY_REQUESTS

Too many requests queued.
Too many requests; please use the websocket for live updates.
Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.
-1004 DUPLICATE_IP

This IP is already on the white list
-1005 NO_SUCH_IP

No such IP has been white listed
-1006 UNEXPECTED_RESP

An unexpected response was received from the message bus. Execution status unknown.
-1007 TIMEOUT

Timeout waiting for response from backend server. Send status unknown; execution status unknown.
-1010 ERROR_MSG_RECEIVED

ERROR_MSG_RECEIVED.
-1011 NON_WHITE_LIST

This IP cannot access this route.
-1013 INVALID_MESSAGE

INVALID_MESSAGE.
-1014 UNKNOWN_ORDER_COMPOSITION

Unsupported order combination.
-1015 TOO_MANY_ORDERS

Too many new orders.
Too many new orders; current limit is %s orders per %s.
-1016 SERVICE_SHUTTING_DOWN

This service is no longer available.
-1020 UNSUPPORTED_OPERATION

This operation is not supported.
-1021 INVALID_TIMESTAMP

Timestamp for this request is outside of the recvWindow.
Timestamp for this request was 1000ms ahead of the server's time.
-1022 INVALID_SIGNATURE

Signature for this request is not valid.
-1023 START_TIME_GREATER_THAN_END_TIME

Start time is greater than end time.
11xx - Request issues¶
-1100 ILLEGAL_CHARS

Illegal characters found in a parameter.
Illegal characters found in parameter '%s'; legal range is '%s'.
-1101 TOO_MANY_PARAMETERS

Too many parameters sent for this endpoint.
Too many parameters; expected '%s' and received '%s'.
Duplicate values for a parameter detected.
-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

A mandatory parameter was not sent, was empty/null, or malformed.
Mandatory parameter '%s' was not sent, was empty/null, or malformed.
Param '%s' or '%s' must be sent, but both were empty/null!
-1103 UNKNOWN_PARAM

An unknown parameter was sent.
-1104 UNREAD_PARAMETERS

Not all sent parameters were read.
Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.
-1105 PARAM_EMPTY

A parameter was empty.
Parameter '%s' was empty.
-1106 PARAM_NOT_REQUIRED

A parameter was sent when not required.
Parameter '%s' sent when not required.
-1108 BAD_ASSET

Invalid asset.
-1109 BAD_ACCOUNT

Invalid account.
-1110 BAD_INSTRUMENT_TYPE

Invalid symbolType.
-1111 BAD_PRECISION

Precision is over the maximum defined for this asset.
-1112 NO_DEPTH

No orders on book for symbol.
-1113 WITHDRAW_NOT_NEGATIVE

Withdrawal amount must be negative.
-1114 TIF_NOT_REQUIRED

TimeInForce parameter sent when not required.
-1115 INVALID_TIF

Invalid timeInForce.
-1116 INVALID_ORDER_TYPE

Invalid orderType.
-1117 INVALID_SIDE

Invalid side.
-1118 EMPTY_NEW_CL_ORD_ID

New client order ID was empty.
-1119 EMPTY_ORG_CL_ORD_ID

Original client order ID was empty.
-1120 BAD_INTERVAL

Invalid interval.
-1121 BAD_SYMBOL

Invalid symbol.
-1125 INVALID_LISTEN_KEY

This listenKey does not exist.
-1127 MORE_THAN_XX_HOURS

Lookup interval is too big.
More than %s hours between startTime and endTime.
-1128 OPTIONAL_PARAMS_BAD_COMBO

Combination of optional parameters invalid.
-1130 INVALID_PARAMETER

Invalid data sent for a parameter.
Data sent for parameter '%s' is not valid.
-1136 INVALID_NEW_ORDER_RESP_TYPE

Invalid newOrderRespType.
20xx - Processing Issues¶
-2010 NEW_ORDER_REJECTED

NEW_ORDER_REJECTED
-2011 CANCEL_REJECTED

CANCEL_REJECTED
-2013 NO_SUCH_ORDER

Order does not exist.
-2014 BAD_API_KEY_FMT

API-key format invalid.
-2015 REJECTED_MBX_KEY

Invalid API-key, IP, or permissions for action.
-2016 NO_TRADING_WINDOW

No trading window could be found for the symbol. Try ticker/24hrs instead.
-2018 BALANCE_NOT_SUFFICIENT

Balance is insufficient.
-2019 MARGIN_NOT_SUFFICIEN

Margin is insufficient.
-2020 UNABLE_TO_FILL

Unable to fill.
-2021 ORDER_WOULD_IMMEDIATELY_TRIGGER

Order would immediately trigger.
-2022 REDUCE_ONLY_REJECT

ReduceOnly Order is rejected.
-2023 USER_IN_LIQUIDATION

User in liquidation mode now.
-2024 POSITION_NOT_SUFFICIENT

Position is not sufficient.
-2025 MAX_OPEN_ORDER_EXCEEDED

Reach max open order limit.
-2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED

This OrderType is not supported when reduceOnly.
-2027 MAX_LEVERAGE_RATIO

Exceeded the maximum allowable position at current leverage.
-2028 MIN_LEVERAGE_RATIO

Leverage is smaller than permitted: insufficient margin balance.
40xx - Filters and other Issues¶
-4000 INVALID_ORDER_STATUS

Invalid order status.
-4001 PRICE_LESS_THAN_ZERO

Price less than 0.
-4002 PRICE_GREATER_THAN_MAX_PRICE

Price greater than max price.
-4003 QTY_LESS_THAN_ZERO

Quantity less than zero.
-4004 QTY_LESS_THAN_MIN_QTY

Quantity less than min quantity.
-4005 QTY_GREATER_THAN_MAX_QTY

Quantity greater than max quantity.
-4006 STOP_PRICE_LESS_THAN_ZERO

Stop price less than zero.
-4007 STOP_PRICE_GREATER_THAN_MAX_PRICE

Stop price greater than max price.
-4008 TICK_SIZE_LESS_THAN_ZERO

Tick size less than zero.
-4009 MAX_PRICE_LESS_THAN_MIN_PRICE

Max price less than min price.
-4010 MAX_QTY_LESS_THAN_MIN_QTY

Max qty less than min qty.
-4011 STEP_SIZE_LESS_THAN_ZERO

Step size less than zero.
-4012 MAX_NUM_ORDERS_LESS_THAN_ZERO

Max mum orders less than zero.
-4013 PRICE_LESS_THAN_MIN_PRICE

Price less than min price.
-4014 PRICE_NOT_INCREASED_BY_TICK_SIZE

Price not increased by tick size.
-4015 INVALID_CL_ORD_ID_LEN

Client order id is not valid.
Client order id length should not be more than 36 chars
-4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP

Price is higher than mark price multiplier cap.
-4017 MULTIPLIER_UP_LESS_THAN_ZERO

Multiplier up less than zero.
-4018 MULTIPLIER_DOWN_LESS_THAN_ZERO

Multiplier down less than zero.
-4019 COMPOSITE_SCALE_OVERFLOW

Composite scale too large.
-4020 TARGET_STRATEGY_INVALID

Target strategy invalid for orderType '%s',reduceOnly '%b'.
-4021 INVALID_DEPTH_LIMIT

Invalid depth limit.
'%s' is not valid depth limit.
-4022 WRONG_MARKET_STATUS

market status sent is not valid.
-4023 QTY_NOT_INCREASED_BY_STEP_SIZE

Qty not increased by step size.
-4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN

Price is lower than mark price multiplier floor.
-4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO

Multiplier decimal less than zero.
-4026 COMMISSION_INVALID

Commission invalid.
%s less than zero.
%s absolute value greater than %s
-4027 INVALID_ACCOUNT_TYPE

Invalid account type.
-4028 INVALID_LEVERAGE

Invalid leverage
Leverage %s is not valid
Leverage %s already exist with %s
-4029 INVALID_TICK_SIZE_PRECISION

Tick size precision is invalid.
-4030 INVALID_STEP_SIZE_PRECISION

Step size precision is invalid.
-4031 INVALID_WORKING_TYPE

Invalid parameter working type
Invalid parameter working type: %s
-4032 EXCEED_MAX_CANCEL_ORDER_SIZE

Exceed maximum cancel order size.
Invalid parameter working type: %s
-4033 INSURANCE_ACCOUNT_NOT_FOUND

Insurance account not found.
-4044 INVALID_BALANCE_TYPE

Balance Type is invalid.
-4045 MAX_STOP_ORDER_EXCEEDED

Reach max stop order limit.
-4046 NO_NEED_TO_CHANGE_MARGIN_TYPE

No need to change margin type.
-4047 THERE_EXISTS_OPEN_ORDERS

Margin type cannot be changed if there exists open orders.
-4048 THERE_EXISTS_QUANTITY

Margin type cannot be changed if there exists position.
-4049 ADD_ISOLATED_MARGIN_REJECT

Add margin only support for isolated position.
-4050 CROSS_BALANCE_INSUFFICIENT

Cross balance insufficient.
-4051 ISOLATED_BALANCE_INSUFFICIENT

Isolated balance insufficient.
-4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN

No need to change auto add margin.
-4053 AUTO_ADD_CROSSED_MARGIN_REJECT

Auto add margin only support for isolated position.
-4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT

Cannot add position margin: position is 0.
-4055 AMOUNT_MUST_BE_POSITIVE

Amount must be positive.
-4056 INVALID_API_KEY_TYPE

Invalid api key type.
-4057 INVALID_RSA_PUBLIC_KEY

Invalid api public key
-4058 MAX_PRICE_TOO_LARGE

maxPrice and priceDecimal too large,please check.
-4059 NO_NEED_TO_CHANGE_POSITION_SIDE

No need to change position side.
-4060 INVALID_POSITION_SIDE

Invalid position side.
-4061 POSITION_SIDE_NOT_MATCH

Order's position side does not match user's setting.
-4062 REDUCE_ONLY_CONFLICT

Invalid or improper reduceOnly value.
-4063 INVALID_OPTIONS_REQUEST_TYPE

Invalid options request type
-4064 INVALID_OPTIONS_TIME_FRAME

Invalid options time frame
-4065 INVALID_OPTIONS_AMOUNT

Invalid options amount
-4066 INVALID_OPTIONS_EVENT_TYPE

Invalid options event type
-4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS

Position side cannot be changed if there exists open orders.
-4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY

Position side cannot be changed if there exists position.
-4069 INVALID_OPTIONS_PREMIUM_FEE

Invalid options premium fee
-4070 INVALID_CL_OPTIONS_ID_LEN

Client options id is not valid.
Client options id length should be less than 32 chars
-4071 INVALID_OPTIONS_DIRECTION

Invalid options direction
-4072 OPTIONS_PREMIUM_NOT_UPDATE

premium fee is not updated, reject order
-4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO

input premium fee is less than 0, reject order
-4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER

Order amount is bigger than upper boundary or less than 0, reject order
-4075 OPTIONS_PREMIUM_OUTPUT_ZERO

output premium fee is less than 0, reject order
-4076 OPTIONS_PREMIUM_TOO_DIFF

original fee is too much higher than last fee
-4077 OPTIONS_PREMIUM_REACH_LIMIT

place order amount has reached to limit, reject order
-4078 OPTIONS_COMMON_ERROR

options internal error
-4079 INVALID_OPTIONS_ID

invalid options id
invalid options id: %s
duplicate options id %d for user %d
-4080 OPTIONS_USER_NOT_FOUND

user not found
user not found with id: %s
-4081 OPTIONS_NOT_FOUND

options not found
options not found with id: %s
-4082 INVALID_BATCH_PLACE_ORDER_SIZE

Invalid number of batch place orders.
Invalid number of batch place orders: %s
-4083 PLACE_BATCH_ORDERS_FAIL

Fail to place batch orders.
-4084 UPCOMING_METHOD

Method is not allowed currently. Upcoming soon.
-4085 INVALID_NOTIONAL_LIMIT_COEF

Invalid notional limit coefficient
-4086 INVALID_PRICE_SPREAD_THRESHOLD

Invalid price spread threshold
-4087 REDUCE_ONLY_ORDER_PERMISSION

User can only place reduce only order
-4088 NO_PLACE_ORDER_PERMISSION

User can not place order currently
-4104 INVALID_CONTRACT_TYPE

Invalid contract type
-4114 INVALID_CLIENT_TRAN_ID_LEN

clientTranId is not valid
Client tran id length should be less than 64 chars
-4115 DUPLICATED_CLIENT_TRAN_ID

clientTranId is duplicated
Client tran id should be unique within 7 days
-4118 REDUCE_ONLY_MARGIN_CHECK_FAILED

ReduceOnly Order Failed. Please check your existing position and open orders
-4131 MARKET_ORDER_REJECT

The counterparty's best price does not meet the PERCENT_PRICE filter limit
-4135 INVALID_ACTIVATION_PRICE

Invalid activation price
-4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION

Quantity must be zero with closePosition equals true
-4138 REDUCE_ONLY_MUST_BE_TRUE

Reduce only must be true with closePosition equals true
-4139 ORDER_TYPE_CANNOT_BE_MKT

Order type can not be market if it's unable to cancel
-4140 INVALID_OPENING_POSITION_STATUS

Invalid symbol status for opening position
-4141 SYMBOL_ALREADY_CLOSED

Symbol is closed
-4142 STRATEGY_INVALID_TRIGGER_PRICE

REJECT: take profit or stop order will be triggered immediately
-4144 INVALID_PAIR

Invalid pair
-4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION

Leverage reduction is not supported in Isolated Margin Mode with open positions
-4164 MIN_NOTIONAL

Order's notional must be no smaller than 5.0 (unless you choose reduce only)
Order's notional must be no smaller than %s (unless you choose reduce only)
-4165 INVALID_TIME_INTERVAL

Invalid time interval
Maximum time interval is %s days
-4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP

Price is higher than stop price multiplier cap.
Limit price can't be higher than %s.
-4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN

Price is lower than stop price multiplier floor.
Limit price can't be lower than %s.
 Back to top
Made with Material for MkDocs