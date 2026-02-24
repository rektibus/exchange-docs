
    

# Welcome

Welcome to Bitget ApiDoc! Click here for quick start

## Coming Soon

| 

| No. 
| Interface 
| Launch Date 
| Remark 
 |

| 1 
| Feature on 'Earn' 
| End of Oct, 2023 
| Bitget Earn, will be available in V2 
 |

### Update Forecast

ETA Sep 06, 2023
- Forecast 
  /api/spot/v1/public/products added response field：`maxOrderNum`
   /api/spot/v1/public/product added response field：`maxOrderNum`

# Update Log

Oct 10, 2023

- Get order history and Get order detail added new field on response: 'feeDetail.newFees'

  "feeDetail": "{\"BGB\":{\"deduction\":true,\"feeCoinCode\":\"BGB\",
  \"totalDeductionFee\":-0.017118519726,
  \"totalFee\":-0.017118519726,\"newFees\":{\"t\":1,\"d\":1,\"r\":1,\"c\":1}}}"
  

- Validation logic changes on withdraw and withdraw-v2

There are 3 types of withdrawal address: 'Normal', 'Universal' and 'EVM address'

- Change only apply to for 'Normal' address: 

- Old logic: Withdraw will only validate the 'address' (withdraw with a wrong 'address + coin' will fail in a later steps)

- New logic: Withdraw will validate the 'address + coin' (withdraw with a wrong 'address + coin' will fail right away)

Sep 05, 2023

- New interface Get merged depth data

Aug 23, 2023

Websocket error response format change：

From:

{

  "event":"error",

  "code":30003,

  "msg":"instType:SP,channel:ticker,instId:BTC-USDT Symbol not exists"

}

To:

{

  "event":"error",

  "arg":

    {

      "instType":"SP",

      "channel":"ticker",

      "instId":"BTC-USDT"

    },

  "code":30003,

  "msg":"instType:SP,channel:ticker,instId:BTC-USDT Symbol not exists",

  "op":"subscribe"

}

Aug 19, 2023

- New feature: Loans

Aug 11, 2023

- New feature to support RSA signature: RSA Signature Demo Code

31/07/2023

- Interface Inner Withdraw v2 supports uid/mobile/email

18/07/2023

- New interface Convert

06/07/2023

- New interface Get All Notices

03/07/2023

- New interface Get History Candles Data

20/06/2023

- New interface Tax

16/06/2023

- New interface Get Account Assets Lite

20/05/2023

- Get order details added response fields: 'feeDetail' and `orderSource`

- Get order history added response fields: 'feeDetail' and `orderSource`

12/05/2023

- New interface Get User Fee Ratio

21/04/2023

- New interface P2P endpoint

28/03/2023

- Transfer support 'Spot Margin Account'

17/03/2023

- New interface Get Market Trades

- New interface Cancel order By Symbol

15/03/2023

- Get Symbols and Get Single Symbol added response fields: 'buyLimitPriceRatio', 'sellLimitPriceRatio'

- Get Candle Data request field 'limit': max 1000

- New interface Transfer V2, Withdraw V2, Inner Withdraw v2 to support 'clientOid'

- Get Withdraw list added request field: 'clientOid', added response fields: 'clientOid', 'tag'

- Get Deposit list added response fields: 'tag'

- Get Transfer List added response fields: 'clientOid', 'transferId', added request param: 'clientOid'

- New interface Cancel order V2 cancel by 'clientOid'

- New interface Cancel order in batch V2 (single instruments) cancel by 'clientOids'

- Get order details, Get order List, Get order history added response fields: 'enterPointSource'

- Get Symbols added request fields: 'clientOid'

- Cancel plan order added request fields: 'clientOid'

- Get current plan orders Get history plan orders added request/response fields: 'clientOid', added response fields: 'enterPointSource'

- Order Channel push data added field: 'eps'

- WebSocket error codes added new error code

13/02/2023

- RestAPI -> Market -> added VIP fee rate

- RestAPI -> Account -> Get Bills modify param 'coinId' to non-required

28/12/2022

- Provide brand new telegram group for Openapi technical support

16/12/2022

- added new enums on 'bizType'

06/12/2022

- RestAPI -> Account -> added Get sub Account Spot Assets

- RestAPI -> Public -> added Get Coin List rateLimit updated to 3/s(IP)

- RestAPI -> Public -> added Get Single Ticker add response parameter: 'bidSz', 'askSz'

- WebsocketAPI -> Private Channel -> Order Channel -> Push data parameters -> 'status' supplement enum: 'init'

- WebsocketAPI -> Public Channel -> Ticker Channel -> Push data parameters -> added 'bidSz', 'askSz'

15/11/2022

- RestAPI -> Trade -> added 

Place plan order

- Modify plan order

- Cancel plan order

- Get current plan orders

- Get history plan orders

18/10/2022

- `Wallet` -> add  Sub Transfer

19/09/2022

- `Account` -> `Get ApiKey Info` add Response `trader`

13/09/2022

- `Account` -> `Get ApiKey Info` add Response `parentId`

19/08/2022

- `Market` -> `Get Candles Data` add request parameter UTC0 

- `Market` -> `Get All Tickers` , `Get Single Ticker` add response  `openUtc0`

15/08/2022

- GET request It is forbidden to transmit parameters in the `Request Body`, please pass the parameters in `QueryString`

08/08/2022

- add `Signature Demo Code`  Example

06/08/2022

- add PostMan Example

03/08/2022

- add Request Example

21/07/2022

- Websocket connection addition rules, please refer to the Connection directory

24/06/2022

- Added getInfo interface

- `assets` add `coin` parameter

05/05/2022

- Added wallet interface

12/02/2022 【Ticker】

- ticker add `buyOne`, `sellOne`

07/1/2022

- Removed domain name https://capi.bitgetapi.com

Add main domain name https://api.bitget.com

- Add error code

- Frequency limiting rules

| 

| Request Url 
| rule 
 |

| /api/spot/v1/public/time 
| 20c/1s 
 |

| /api/spot/v1/public/currencies 
| 20c/1s 
 |

| /api/spot/v1/public/products 
| 20c/1s 
 |

| /api/spot/v1/public/product 
| 20c/1s 
 |

| /api/spot/v1/market/ticker 
| 20c/1s 
 |

| /api/spot/v1/market/tickers 
| 20c/1s 
 |

| /api/spot/v1/market/fills 
| 20c/1s 
 |

| /api/spot/v1/market/candles 
| 20c/1s 
 |

| /api/spot/v1/market/depth 
| 20c/1s 
 |

| /api/spot/v1/account/assets 
| 10c/1s 
 |

| /api/spot/v1/account/bills 
| 10c/1s 
 |

| /api/spot/v1/account/transferRecords 
| 20c/1s 
 |

| /api/spot/v1/trade/orders 
| 10c/1s 
 |

| /api/spot/v1/trade/batch-orders 
| 5c/1s 
 |

| /api/spot/v1/trade/cancel-order 
| 10c/1s 
 |

| /api/spot/v1/trade/cancel-batch-orders 
| 10c/1s 
 |

| /api/spot/v1/trade/orderInfo 
| 20c/1s 
 |

| /api/spot/v1/trade/open-orders 
| 20c/1s 
 |

| /api/spot/v1/trade/history 
| 20c/1s 
 |

| /api/spot/v1/trade/fills 
| 20c/1s 
 |

24/09/ 2021【WebSocket Api 】

- WebSocket Public Channel and Private Channel Online

15/09/2021 【Add transfer record interface】

- Added transfer record interface

05/07/2021【New creation v1 Spot trading document】

- New creation of V1 document

- Supporting of error message

# Introduction

## API Introduction

Welcome to Bitget developer documentation!

This document is the only official document of Bitget API. The capabilities provided by Bitget API will be continuously updated here. Please pay attention to it in time.

You can switch to access different business APIs by clicking the upper menu, and you can switch the document language by clicking the language button on the upper right.

On the right side of the document is an example of request parameters and response results.

## Update follow-up

Regarding API additions, updates, and offline information, Bitget will issue announcements in advance. It is recommended that users follow and subscribe to our announcements to obtain relevant information in a timely manner.

You can click here  to subscribe to the announcement.

## Contact us

If you have any questions or suggestions, feel free to contact us:

- Email API@bitget.com

- Telegram Join

# Quick start

## Prepare to integrate

If you need to use the API, please log in to the web page, then apply the API key and complete the permission configuration, and then develop and trade according to the details of this document.

You can click here to create the API Key after login.

Each user can create 10 sets of Api Keys, and each Api Key can set permissions for reading and trading.

The permissions are described as follows:

- Read-Only permission: Read permission authorized to query data, such as market data.

- Trade permission: Transaction permission authorized to call the interface of placing and cancelling orders.

- Transfer permission: With this permission it authorized to transfer coins between accounts inside Bitget.

- Withdraw permission: Authorized to withdraw assets from Bitget account, `noted that you can only withdraw coins through an whitelisted IP address.`

After successfully created the API Key, please remember the following information:

- `APIKey` The identity of API transactions, it is generated by a random algorithm.

- `Secretkey` The private key is randomly generated by the system and used for Signature generation.

- `Passphrase` Passphrase is set by the user. It should be noted that if the Passphrase is forgotten, it cannot be retrieved, and the API Key needs to be recreated.

User can bind IP address when he creates APIKey, It is strongly recommended to bind IP for security reason. 

risk warning：

These three keys are highly related to account security, please keep in mind DO NOT DISCLOSE Secretkey and Passphrase to anyone at any circumstances, even with BitGet employees.

Leaking any of these three keys may cause loss of your assets. If you find by any chance that the APIKey is compromised, please delete the APIKey as soon as possible.

 

## SDK / Code example

SDK（Recommended）

Java | Python | Node Js | Golang | PHP 

PostMan Demo

PostMan 

You should first try to config the APIKey, Secretkey and Passphrase in the `Environments` tab on left of the PostMan

## Interface Type

This chapter is consist of the following two aspects for the interface types:

- Public interface

- Private interface

Public interface

The public interface can be used to obtain configuration information and market data. Public requests can be called without authentication.

Private interface

The private interface can be used for order management and account management. Every private request must be Signatured.

The private interface will be verified from server side with your APIKey.

## Access restriction

This chapter mainly focuses on access restrictions:

- Rest API when the access exceeds the frequency limit, it will return the 429 status: the request is too frequent.

Rest API

If a valid APIKey is passed with the request, We will use APIKey to limit the frequency; if not, the public IP Address will be used to limit the frequency.

Frequency limit rules: There are separate instructions on each interface. If there is no specific instruction, the frequency limit of general interface is 10 times per second.

Special note: When place orders in batches, 10 orders per currency pair will be counted as one request. For example, a batch order like: 1 order with ETHUSDT, 10 order with BTCUSDT, then the rate-limit will count this batch order as 2 requests.

## API domain

You can use different domain as below Rest API.

| 

| Domain 
| REST API 
| Recommend to use 
 |

| Domain1 
| https://api.bitget.com 
| Main Domain 
 |

| Domain2 
| https://capi.bitget.com 
| Old domain 
 |

## API Public parameters

### side

Trade direction

| 

| String 
| Description 
 |

| sell 
| Sell 
 |

| buy 
| Buy 
 |

### orderType

Order type

| 

| String 
| Description 
 |

| limit 
| Limit order 
 |

| market 
| Market order 
 |

### force

Order type

| 

| String 
| Description 
 |

| normal 
| Good till cancel 
 |

| post_only 
| Maker Only 
 |

| fok 
| Fill Or Kill（FOK） 
 |

| ioc 
| Immediate-Or-Cancel（IOC） 
 |

### status

Order status

| 

| String 
| Description 
 |

| init 
| initial, inserted into DB 
 |

| new 
| Unfilled, pending in orderbook 
 |

| partial_fill 
| Partially filled 
 |

| full_fill 
| Fully filled 
 |

| cancelled 
| Cancelled 
 |

### groupType

Major types of transaction

| 

| String 
| Description 
 |

| deposit 
| Deposit 
 |

| withdraw 
| Withdrawal 
 |

| transaction 
| Trade 
 |

| transfer 
| Transfer 
 |

| other 
| Others 
 |

### bizType

Business type

| 

| String 
| Description 
 |

| deposit 
| Deposit 
 |

| withdraw 
| Withdrawal 
 |

| buy 
| Buy 
 |

| Sell 
| sell 
 |

| deduction of handling fee 
| deduction of handling fee 
 |

| transfer-in 
| Transfer-in 
 |

| transfer-out 
| Transfer-out 
 |

| rebate rewards 
| rebate rewards 
 |

| airdrop rewards 
| airdrop rewards 
 |

| USDT contract rewards 
| USDT contract rewards 
 |

| mix contract rewards 
| mix contract rewards 
 |

| System lock 
| System lock 
 |

| User lock 
| User lock 
 |

### deposit withdrawal order status

| 

| String 
| Description 
 |

| cancel 
| Cancel 
 |

| reject 
| Reject 
 |

| success 
| Success 
 |

| wallet-fail 
| Wallet failed 
 |

| wallet-processing 
| Wallet processing 
 |

| first-audit 
| 1st audit 
 |

| recheck 
| 2nd audit 
 |

| first-reject 
| 1st audit rejected 
 |

| recheck-reject 
| 2nd audit rejected 
 |

### withdrawal type

User withdrawal address query

| 

| String 
| Description 
 |

| chain-on 
| On blockchain 
 |

| inner-transfer 
| Internal address 
 |

### triggerType

| 

| String 
| Description 
 |

| fill_price 
| fill price 
 |

| market_price 
| mark price 
 |

### accountType

| 

| String 
| Description 
 |

| EXCHANGE 
| spot account 
 |

| CONTRACT 
| contract account 
 |

| USDT_MIX 
| USDT Future account 
 |

| USD_MIX 
| Mix account 
 |

| USDC_MIX 
| usdc futures 
 |

| MARGIN_CROSS 
| margin cross 
 |

| MARGIN_ISOLATED 
| margin isolated 
 |

### Candlestick line timeframe

granularity

- 1min (1 minute)

- 5min (5 minutes)

- 15min (15 minutes)

- 30min (30 minutes)

- 1h (1 hour)

- 4h (4 hours)

- 6h (6 hours)

- 12h (12 hours)

- 1day (1 day)

- 3day (3 days)

- 1week (1 week)

- 1M (monthly line)

- 6Hutc (UTC0 6 hour)

- 12Hutc (UTC0 12 hour)

- 1Dutc (UTC0 1day)

- 3Dutc (UTC0 3rd)

- 1Wutc (UTC0 weekly)

- 1Mutc (UTC0 monthly)

### fromType,toType(transfer in type，transfer out type)

| 

| String 
| Description 
 |

| spot 
| spot asset coin 
 |

| mix_usdt 
| USDT transfer only 
 |

| mix_usd 
| BTC, ETH, EOS, XRP, USDC 
 |

| mix_usdc 
| USDC transfer only 
 |

| margin_cross 
| cross margin account 
 |

| margin_isolated 
| isolated margin account 
 |

### enterPointSource

| 

| String 
| Description 
 |

| WEB 
| WEB Client 
 |

| APP 
| APP Client 
 |

| API 
| API Client 
 |

| SYS 
| SYS Client 
 |

| ANDROID 
| ANDROID Client 
 |

| IOS 
| IOS Client 
 |

### p2pAdvertisementStatus

| 

| String 
| Description 
 |

| online 
| p2p advertisement online 
 |

| offline 
| p2p advertisement offline 
 |

| editing 
| p2p advertisement editing 
 |

| completed 
| p2p advertisement completed 
 |

### p2pOrderStatus

| 

| String 
| Description 
 |

| pending_pay 
| p2p order pending pay 
 |

| paid 
| p2p order paid 
 |

| appeal 
| p2p order appeal 
 |

| completed 
| p2p order completed 
 |

| cancelled 
| p2p order cancelled 
 |

### orderSource

| 

| String 
| Description 
 |

| normal 
| normal order 
 |

| market 
| market order 
 |

| spot_trader_buy 
| spot trace trader buy (trader) 
 |

| spot_follower_buy 
| Spot follower buy (follower) 
 |

| spot_trader_sell 
| spot trace trader sell (trader) 
 |

| spot_follower_sell 
| Spot follower sell (follower) 
 |

### noticeType

| 

| String 
| Description 
 |

| NEW_NOTICE 
| Latest Announcements 
 |

| TRADING_AND_ACTIVITIES 
| Trading competitions and promotions 
 |

| NEW_COIN_LAUNCH 
| Coin listings 
 |

| MAINTENANCE_SYSTEM_UPGRADE 
| Maintenance or System Updates 
 |

### tax type spot

- Deposit

- Withdrawal

- User fees

- Fiat withdrawal success - Deduct

- Sell

- Buy

- Transaction fee deduct

- Strategic purchase-user accounts

- Subscribe to trader-user accounts

- System charges fees

- Strategic refund-User account

- Subscription fee refund-user account

- Strategic Income-Traders' accounts

- Crypto Voucher Distribution

- Copy Trade expense

- Judicial recall

- Copy Trade profit

- Refund Copy Trade commission

- Buy Crypto

- Deduction of judicial recall

- Buy with card

- System lock-up

- Airdrop Reward-B

- Decrease due to ETF settlement

- Increase due to ETF settlement

- System lock-up

- User lock-up

- Trading fee rebate

- Manage background lock positions

- Automatic deposit

- Automatic withdrawal

- Deposit from strategy account

- Withdraw to strategy account

- Lotto rewards

- User contract trial fund

- User contract simulation fund

- Delegate

- Undelegate

- Rebate rewards

- Rebate rewards

- Consumption

- Gains

- Unlock locked order

- Deduction

- Return

- Release

- Repayment

- Forced liquidation return

- The locked order is returned to the system

- The locked order is returned to the system

- Failed

- Withdrawal frozen

- Mirror fund

- Supplement fund

- Reduce fund

- Settlement out

- Withdrawal unfreeze

- Deposit

- Deposit

- Ordinary Withdrawal

- Ordinary Withdrawal

- Fast withdrawal fee

- Airdrop Reward-A

- Subscribe

- Interest

- Penalty

- Redemption

- Activity fund(USDT-Ⓜ)

- Activity fund

- Activity fund(Coin-Ⓜ)

- Activity fund

- Increase exchange rate

- Reduce exchange rate

- Transfer in

- Activity issuance

- Transfer out

- Super account

- System account

- Exchange spending

- Exchange income

- Sent

- Received

- MegaSwap Transfer in

- MegaSwap Transfer out

- Channel referral rewards

- System account

- Sell Crypto

- Fiat deposit

### tax type future and margin

| 

| String 
| Description 
 |

| transfer_in 
| Transfer into  account 
 |

| transfer_out 
| Transfer out from  account 
 |

| borrow 
| Borrow 
 |

| repay 
| Repay 
 |

| liquidation_fee 
| Liquidation_fee 
 |

| compensate 
| Liquidation compensate (when account balance less than 0 after liquidation) 
 |

| deal_in 
| Buy in 
 |

| deal_out 
| Sell out 
 |

| system_fee_in 
| Taker maker fee 
 |

| interest_repay 
| Interest repay 
 |

| confiscated 
| Confiscated when liquidation 
 |

| exchange_in 
| coin exchange income (i.e. USDT to BTC, 'BTC' is exchange_in) 
 |

| exchange_out 
| coin exchange pay out (i.e. USDT to BTC, 'USDT' is exchange_out) 
 |

### tax type p2p

| 

| String 
| Description 
 |

| transfer_in 
| Transfer into  account 
 |

| transfer_out 
| Transfer out from  account 
 |

| SELL 
| Sell crypto 
 |

| BUY 
| Buy crypto 
 |

## API Verification

Initiating request

The header of all REST requests must contain the following keys:

- ACCESS-KEY：API KEY as a string.

- ACCESS-SIGN： Sign with base64 encoding (see Signature).

- ACCESS-TIMESTAMP： The timestamp of your request. Value equals to milliseconds since Epoch.

- ACCESS-PASSPHRASE：The passphrase you set when creating the API KEY.

- Content-Type：Standardized setting to application/json.

- locale: Support multiple languages, such as: Chinese (zh-CN), English (en-US)

```
//Java
System.currentTimeMillis();

```

```
//python
import time
time.time_ns() / 1000000

```

```
//Golang
import (
  "time"
)
int64(time.Now().UnixNano()/1000000)

```

```
//Javascript
Math.round(new Date())

```

```
//PHP
microtime(true) * 1000;

```

## Signature

The request header of ACCESS-SIGN is obtained by encrypting timestamp + method.toUpperCase() + requestPath + "?" + queryString + body **string (+ means string concat) encrypt by **HMAC SHA256 **algorithm, and encode the encrypted result through **BASE64.

Description for each parameter of the signature

- timestamp： Same as ACCESS-TIMESTAMP request header. Value equals to milliseconds since Epoch.

- method：Request method (POST/GET), all uppercase letters.

- requestPath：Request interface path. 

- queryString：The query string in the request URL (the request parameter after the ?).

- body： The string corresponding to the request body. If the request has no body (usually a GET request), the body can be omitted.

When queryString is empty, the signature format

```
timestamp + method.toUpperCase() + requestPath + body

```

 

When queryString is not empty, the signature format

```
timestamp + method.toUpperCase() + requestPath + "?" + queryString + body

```

For example

To obtain in-depth information, take BTCUSDT as an example:

- timestamp = 1591089508404

- method = "GET"

- requestPath = "/api/spot/v1/market/depth"

- queryString= "?symbol=btcusdt_spbl&limit=20"

Generate the string to be signed:

'1591089508404GET/api/spot/v1/market/depth?symbol=btcusdt_spbl&limit=20'

Place order，take BTCUSDT as an example:

- timestamp = 1561022985382

- method = "POST"

- requestPath = "/api/spot/v1/order/order"

- body = {"symbol":"btcusdt_spbl","quantity":"8","side":"buy","price":"1","orderType":"limit","clientOrderId":"bitget#123456"}

Generate the string to be signed:

'1561022985382POST/api/spot/v3/order/order{"symbol":"btcusdt_spbl","size":"8","side":"buy","price":"1","orderType":"limit","clientOrderId":"bitget#123456"}'

 

Steps to generate the final signature

HMAC

Step 1. Use the private key secretkey to encrypt the string to be signed with hmac sha256

```
String payload = hmac_sha256(secretkey, Message);

```

 

Step 2. Base64 encoding for Signature.

```
String signature = base64.encode(payload);

```

RSA

Step 1. Use the RSA privateKey privateKey to encrypt the string to be signed with SHA-256

Step 2. Base64 encoding for Signature.

## HMAC Signature Demo Code

Java

```
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.management.RuntimeErrorException;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

@Slf4j
public class CheckSign {

    private static final String secretKey = "";

    public static void main(String[] args) throws Exception {
        //POST sign example
//        String timestamp = "1684813405151";
//        String body = "{\"symbol\":\"TRXUSDT_UMCBL\",\"marginCoin\":\"USDT\",\"size\":551,\"side\":\"open_long\",\"orderType\":\"limit\",\"price\":0.0555,\"timeInForceValue\":\"normal\"}";
//
//        String sign = generate(timestamp,"POST","/api/mix/v1/order/placeOrder" ,null,body,secretKey);
//        log.info("sign:{}",sign);

        //GET sign example
        String timestamp = "1684814440729";
        String queryString = "symbol=btcusdt_umcbl&marginCoin=usdt";
        String sign = generate(timestamp,"GET","/api/mix/v1/account/account" ,queryString,null,secretKey);
        log.info("sign:{}",sign);
    }

    private static Mac MAC;

    static {
        try {
            CheckSign.MAC = Mac.getInstance("HmacSHA256");
        } catch (NoSuchAlgorithmException var1) {
            throw new RuntimeErrorException(new Error("Can't get Mac's instance."));
        }
    }

    public static String generate(String timestamp, String method, String requestPath,
                                  String queryString, String body, String secretKey)
            throws CloneNotSupportedException, InvalidKeyException, UnsupportedEncodingException {

        method = method.toUpperCase();
        body = StringUtils.defaultIfBlank(body, StringUtils.EMPTY);
        queryString = StringUtils.isBlank(queryString) ? StringUtils.EMPTY : "?" + queryString;
        String preHash = timestamp + method + requestPath + queryString + body;
        log.info("preHash:{}",preHash);
        byte[] secretKeyBytes = secretKey.getBytes("UTF-8");
        SecretKeySpec secretKeySpec = new SecretKeySpec(secretKeyBytes, "HmacSHA256");
        Mac mac = (Mac) CheckSign.MAC.clone();
        mac.init(secretKeySpec);
        return Base64.getEncoder().encodeToString(mac.doFinal(preHash.getBytes("UTF-8")));
    }

}

```

Python

```
import hmac
import base64
import json
import time

def get_timestamp():
    return int(time.time() * 1000)

def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)

def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body

def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]

if __name__ == '__main__':
    API_SECRET_KEY = ""

    timestamp = "1685013478665" # get_timestamp()
    request_path = "/api/mix/v1/order/placeOrder"
    # POST
    params = {"symbol": "TRXUSDT_UMCBL", "marginCoin": "USDT", "price": 0.0555, "size": 551, "side": "open_long", "orderType": "limit", "timeInForceValue": "normal"}
    body = json.dumps(params)
    sign = sign(pre_hash(timestamp, "POST", request_path, str(body)), API_SECRET_KEY)
    print(sign)

    # GET
    body = ""
    request_path = "/api/mix/v1/account/account"
    params = {"symbol": "TRXUSDT_UMCBL", "marginCoin": "USDT"}
    request_path = request_path + parse_params_to_str(params)
    sign = sign(pre_hash(timestamp, "GET", request_path, str(body)), API_SECRET_KEY)
    print(sign)

```

For more demo code on other languages, please refer to SDK/Code Example

## RSA Signature Demo Code

Java

```
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.management.RuntimeErrorException;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import org.springframework.util.Base64Utils;

@Slf4j
public class CheckSign {

    public static void main(String[] args) throws Exception {
        //GET sign example
//        String timestamp = "1684814440729";
//        String queryString = "symbol=btcusdt_umcbl&marginCoin=usdt";
//        String signContent = timestamp + "GET" + "/api/mix/v1/account/account?" + queryString;
//        String sign = generate(signContent);
//        log.info("sign:{}",sign);

        //POST sign example
        String timestamp = "1684814440729";
        String preContent = timestamp + "POST" + "/api/spot/v1/trade/orders";
        String body = "{\"symbol\":\"btcusdt_spbl\",\"quantity\":\"8\",\"side\":\"buy\",\"price\":\"1\",\"orderType\":\"limit\",\"clientOrderId\":\"bitget1233456\"}";
        String signContent = preContent + body;
        String sign = generate(signContent);
        log.info("sign:{}",sign);
    }

  /**
   *
   * @param content: the string to be signed
   * @return
   */
  private String generate(String content) {
    String privateKey = "-----BEGIN PRIVATE KEY-----\n" +
            "xxxxxxxxxxxxxxxxxxxx9w0BAQEFAASCBKgwggSkAgEAAoIBAQD5C1iP01MC9fh5\n" +
            "43mGx8WgJRAp3Xz9Tcqfz6HzoSg+zd8HVxKXRTXBwMDBfLxfQXobptz1tDlPUs+g\n" +
            "YI38X8XEBZi5U4EBaZ5qHxArBTimyNXX6WNL6hTw0MI238cGKiW0WvWd9v6Z6/LX\n" +
            "i6uFUiUEsZiiuHXcO7EKGuvBrVIRl57FzvOPD5QKfhVxcHr63NfEViAEQfQH4IN2\n" +
            "+mu+L8epkWkmbua4jILUP+LXvHN7ZMiWP9bouw3r4l6v0NJ4XyucSYJL9fJ81rsI\n" +
            "iUoD1S7xlSboujR4RSsFZKFyurE1c8XiU2aZ2qq+6vjby0ncE4dKVu5x/iJZ4gsL\n" +
            "bneZujBLAgMBAAECggEAD6cF5uw6QGpjNo30emMd6aXKsUbpbyYvgQHUxPIxDFl2\n" +
            "FgkD8xv3d/j8ZGzJjhcYbJp9MrgkDfc/c23+HomKbXqIkcVMy2DvAu523q1SVTE0\n" +
            "N4DEq+XHcSc9vaMs6BdIDWDWJRp8AAKTXba6jgOOrg/Xbwq25aOeyerNPHv/N3m3\n" +
            "VImJZVV+ZcetUZ82UdX7NkvV4qmRi8se47OXUT9aypzpvGbSukkqXuE4GtKGoybR\n" +
            "R1sJtU10ap3QvyVNshn2QJnRd3GN2UENDvZS3ZvSY6f/Cq7K/EAmrsstOdUB2Ihn\n" +
            "POnI9/MrghWFq/n3ekuArWc54bDai0deKFl9KvI2oQKBgQD9ekRFMB6ueRCCeoyg\n" +
            "TOGvvW3d7X7G90XKL1xKhrg6mYh65hfQaxbihfOcrneFOoc3BgZwnbAZpF+hlq9J\n" +
            "klu69adhYlMxP2nF3PGj5vPln9/rd6/gcFFE9o7zZhI166PsmlxQ7/N0SCnlao7y\n" +
            "HZQoeeFJ1xuvCHVlNsTR+XZ88QKBgQD7hckVvGxIftcZsHChP8TFcDAn1IsaVbyt\n" +
            "i1UZ5JPznSLTcdb8YPtFr9afiCJ4b2NqRe8gCpUCUi+urnoMMsqMxTUMopiLPh2S\n" +
            "SYaBgpQYUIDLpt+Wx06krbOOyXVZ8RtgYLMpMhFCsRyzovqe8/LZQfQKWfQGTAXS\n" +
            "qL5vdyiw+wKBgQC7DMDYdbwOcFRYlOq1WEarExTCUoHdfZfIrc5jSKsmwynN14H3\n" +
            "US9gFg1BsBWPATPKzO1vqU3Mfln7umC73/9FJgZQfOh7TRpW4saGduXAq4voDTiC\n" +
            "XR/7zh6LSuVhWPRsozRAnfF/+8i+/TVjQaSVgetYPB63uXw4JoRzlq1zYQKBgQDJ\n" +
            "7ASb25G+vX1n1TsGaNBKhR9TypEFylDXreTbDaMtTzg3Mcwa/qyarGiL2Fl8AEh6\n" +
            "d7xaJ8SqgVpgTRgUFO6BBozpINt/5ZUN7NL7w92qi25qkAQt4sGi+QQOnHMGisak\n" +
            "n90VNGmg9dkJ6cxzsXqDqiwF52M9bui5zthbWfkj4wKBgEFVT+jf235aihaS88Oj\n" +
            "MbR078tvsFiRBICHlYCIef7/a+gt7N1u9sEGlPspY3HuPamA39201BuItD9X83VR\n" +
            "Vg+HjkeQIIrxmfvZn1O8/l+ItSNUzQhX6T0cSdCo6KtmZLBQ6Zaw7r63GcdvSdR2\n" +
            "xxxxxxxxxxxxxxxxxxxxxxx\n" +
            "-----END PRIVATE KEY-----\n";
    try {
      String parsedPem = privateKey.replace("\n", "").trim();
      parsedPem = parsedPem
              .replace("-----BEGIN PRIVATE KEY-----", "")
              .replace("-----END PRIVATE KEY-----", "");
      PKCS8EncodedKeySpec priPKCS8 = new PKCS8EncodedKeySpec(Base64Utils.decodeFromString(parsedPem));
      KeyFactory keyFactory = KeyFactory.getInstance("RSA");
      PrivateKey priKey = keyFactory.generatePrivate(priPKCS8);
      Signature signature = Signature.getInstance("SHA256WithRSA");
      signature.initSign(priKey);
      signature.update(content.getBytes(StandardCharsets.UTF_8));
      String sign = Base64Utils.encodeToString(signature.sign());
      return sign;
    } catch (Exception ex) {
      throw new RuntimeException("create sign  failed", ex);
    }
  }

}

```

Python

```
import base64
import json
import time
import base64
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def get_timestamp():
    return int(time.time() * 1000)

def rsa_sign(message, private_key):
  pri_key = RSA.importKey(private_key)
  encoded_param = SHA256.new(bytes(message, encoding='utf-8'))
  sign_str = PKCS1_v1_5.new(pri_key).sign(encoded_param)
  return base64.b64encode(sign_str).decode()

def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body

def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]

if __name__ == '__main__':
    private_key = '''-----BEGIN PRIVATE KEY-----
XXXXXXXXXXANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdTR5gmwGH77wE
e0ljABC58EVhiw7fPXWhMh7gZwurQQ8M/I9/VA8lDjwwoGuuJ6enurdfwhpZxeZH
P3wdmwvD7XLESEXVuxJv5hdpI9m6ydInK9SA8IbaF4yYWp0l4N2mA44MzadA7QZq
bQtQPlyPZHeia5q/NZHFWCrCbW2lGAAWwrhQq9LceVIW75e213xtnps0pGlII7Ye
xLkoazuhC1X8YNSxlCdLOiz1GvOeVSeiSZx31o/O+rj7tDFpSgZJEXRmtGRoJkJy
10EGSrvUMezCVSOcb1hCExg4osK6rBKnDjFjwQvwvNNZq0JG+CkfH8eHAa7gSK50
In51go29AgMBAAECggEAEvYk30hQGu7PH0stQX3UhlVsR6HXnRlvgIrmJe7F/VLO
WaZoNdUQLktU/heYY1nsX8+mIyjmvEOayqPgdkEmXevVlcuQf38Zbduynr3vlRCX
AJnL9+8GkmucSxFBODuu/EAZc3mm27C2wUV7w6SAy9g0g6Os97ehZsSGAwHl4aye
i6KtB07LAA10Eh5Ptq4YAfCYiUO7j10pQ+DJKqN9N1eyjyw5eixEgCpudcbpCc9X
+EK6zxk8Ynr0ANX8/LwvokqgYBK1UIL6ear0dtKmeFU+KwrmkKZfXk8/Amr/O8Ot
iHTTr1SLyQKRzq3La149LMmNkUYxaMSV/KGTEV7ukQKBgQDQl/fA3mxXtQg2IjTB
cvDBGhB4c3haECWcP7TQWJDb30vxOKeq1k9YPUfegZga5zlyV28PAZnb0m5x07+0
OY4862brT+pje9OhQxfkAY6AtJaiIqhCcw5ew8Go/Ja1ML0jZESWG1MWBJtCcFTm
d3+n9yU1fB1Ze0adilYmyu7zwwKBgQDBDPJZgSj7YssPyRmo3bO0MjknfYBqXvwi
6TxV11mJRe5BJ9Rc2WXGfEm3DEn7TO/Wv0t7Yqm6/sXg5HzriN/PHlaVtE6wlXe7
3gpYKjlm99KO7KKWYqP812mASl6ydLX9QWozlOXjVhWMuSGqMWjut4J3P8jlkOJ6
pNq9c8/gfwKBgQCxwvAl8ubNj78hsuDWgsddKIMkwvKrfdsvXrMOYouAdLjZJvjs
A5q2jfKzUil3s9km8g/479pYlOn+Iv/Z7Lqke8/HdOFASoQ9h1nSuujgEgXUwkg1
6Ks0Ywqkoi0k2BY3FPnGGh8iQma1pdkUVn35fAq/m7e/S+kP1JY6lPIx1QKBgQCS
jxul67KLNrNmpot+ceGt2bseSd8l4jqU3nDZ0oW8+4Qnnu9QFhN4Hn9wIjpAOGaU
p+HMKFknB6h+Vbior98JxMSDHsHmuXKPA8DishumGlqV+vxsIzLQD1Ge/dbqsERB
olnYEyB7+KyfiyUNqjk5kcPQeHIyJk5qQaF21udoTQKBgDOMbtM0Nq7cd/SAHISR
VYIGGXRFNqAjLJW7DRJGxw3AEwxKG+nxNLeG7GsQDyPCvZSKwRpdpXRTh+6mzXqe
pQ6+33v2gOtez8Cwo6tgyKRi6QPObQk00vbrKEBTihP30m81rwBPzjwj7iKXxWgA
DJoVsaqGOaIf4qXXXXXXXXXX
-----END PRIVATE KEY-----'''

    timestamp = get_timestamp()
    request_path = "/api/mix/v1/order/placeOrder"
    # POST
    params = {"symbol": "TRXUSDT_UMCBL", "marginCoin": "USDT", "price": 0.0555, "size": 551, "side": "open_long", "orderType": "limit", "timeInForceValue": "normal"}
    body = json.dumps(params)
    sign = rsa_sign(pre_hash(timestamp, "POST", request_path, str(body)), private_key)
    print(sign)

    # GET
    body = ""
    request_path = "/api/mix/v1/account/account"
    params = {"symbol": "TRXUSDT_UMCBL", "marginCoin": "USDT"}
    request_path = request_path + parse_params_to_str(params)
    sign = rsa_sign(pre_hash(timestamp, "GET", request_path, str(body)), private_key)
    print(sign)

```

NodeJs

```
export function sign() {

    const private_key = '-----BEGIN PRIVATE KEY-----\n' +
        'XXXXXXXXXXANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdTR5gmwGH77wE\n' +
        'e0ljABC58EVhiw7fPXWhMh7gZwurQQ8M/I9/VA8lDjwwoGuuJ6enurdfwhpZxeZH\n' +
        'P3wdmwvD7XLESEXVuxJv5hdpI9m6ydInK9SA8IbaF4yYWp0l4N2mA44MzadA7QZq\n' +
        'bQtQPlyPZHeia5q/NZHFWCrCbW2lGAAWwrhQq9LceVIW75e213xtnps0pGlII7Ye\n' +
        'xLkoazuhC1X8YNSxlCdLOiz1GvOeVSeiSZx31o/O+rj7tDFpSgZJEXRmtGRoJkJy\n' +
        '10EGSrvUMezCVSOcb1hCExg4osK6rBKnDjFjwQvwvNNZq0JG+CkfH8eHAa7gSK50\n' +
        'In51go29AgMBAAECggEAEvYk30hQGu7PH0stQX3UhlVsR6HXnRlvgIrmJe7F/VLO\n' +
        'WaZoNdUQLktU/heYY1nsX8+mIyjmvEOayqPgdkEmXevVlcuQf38Zbduynr3vlRCX\n' +
        'AJnL9+8GkmucSxFBODuu/EAZc3mm27C2wUV7w6SAy9g0g6Os97ehZsSGAwHl4aye\n' +
        'i6KtB07LAA10Eh5Ptq4YAfCYiUO7j10pQ+DJKqN9N1eyjyw5eixEgCpudcbpCc9X\n' +
        '+EK6zxk8Ynr0ANX8/LwvokqgYBK1UIL6ear0dtKmeFU+KwrmkKZfXk8/Amr/O8Ot\n' +
        'iHTTr1SLyQKRzq3La149LMmNkUYxaMSV/KGTEV7ukQKBgQDQl/fA3mxXtQg2IjTB\n' +
        'cvDBGhB4c3haECWcP7TQWJDb30vxOKeq1k9YPUfegZga5zlyV28PAZnb0m5x07+0\n' +
        'OY4862brT+pje9OhQxfkAY6AtJaiIqhCcw5ew8Go/Ja1ML0jZESWG1MWBJtCcFTm\n' +
        'd3+n9yU1fB1Ze0adilYmyu7zwwKBgQDBDPJZgSj7YssPyRmo3bO0MjknfYBqXvwi\n' +
        '6TxV11mJRe5BJ9Rc2WXGfEm3DEn7TO/Wv0t7Yqm6/sXg5HzriN/PHlaVtE6wlXe7\n' +
        '3gpYKjlm99KO7KKWYqP812mASl6ydLX9QWozlOXjVhWMuSGqMWjut4J3P8jlkOJ6\n' +
        'pNq9c8/gfwKBgQCxwvAl8ubNj78hsuDWgsddKIMkwvKrfdsvXrMOYouAdLjZJvjs\n' +
        'A5q2jfKzUil3s9km8g/479pYlOn+Iv/Z7Lqke8/HdOFASoQ9h1nSuujgEgXUwkg1\n' +
        '6Ks0Ywqkoi0k2BY3FPnGGh8iQma1pdkUVn35fAq/m7e/S+kP1JY6lPIx1QKBgQCS\n' +
        'jxul67KLNrNmpot+ceGt2bseSd8l4jqU3nDZ0oW8+4Qnnu9QFhN4Hn9wIjpAOGaU\n' +
        'p+HMKFknB6h+Vbior98JxMSDHsHmuXKPA8DishumGlqV+vxsIzLQD1Ge/dbqsERB\n' +
        'olnYEyB7+KyfiyUNqjk5kcPQeHIyJk5qQaF21udoTQKBgDOMbtM0Nq7cd/SAHISR\n' +
        'VYIGGXRFNqAjLJW7DRJGxw3AEwxKG+nxNLeG7GsQDyPCvZSKwRpdpXRTh+6mzXqe\n' +
        'pQ6+33v2gOtez8Cwo6tgyKRi6QPObQk00vbrKEBTihP30m81rwBPzjwj7iKXxWgA\n' +
        'DJoVsaqGOaIf4qXXXXXXXXXX\n' +
        '-----END PRIVATE KEY-----\n'

    const ts = Date.now();
    const NodeRSA = require('node-rsa')
    const pri_key = new NodeRSA(private_key)

    //GET
    const ts = Date.now();
    const params = 'coin=USDT&startTime=1687744761000&endTime=1690336761929'
    const endpoint = '/api/spot/v1/wallet/withdrawal-list'
    const method = "GET"
    const pre_hash = String(ts) + method + endpoint + '?' + params
    const sign = pri_key.sign(pre_hash, 'base64', 'UTF-8')

    //POST
    const endpoint_post = '/api/spot/v1/trade/open-orders'
    const params_post = '{"symbol": "BTCUSDT_SPBL"}'
    const method_post = "POST"
    const pre_hash_post = String(ts) + method_post + endpoint_post + params_post
    const sign_post = pri_key.sign(pre_hash_post, 'base64', 'UTF-8')

    return sign
}

```

## Request interaction

All requests are based on the Https protocol, and the Content-Type in the POST request header information needs to be standardized as:'application/json'.

Request interaction description

- Request parameters: encapsulate parameters according to the interface request parameters.

- Submit request parameters: submit the encapsulated request parameters to the server through GET/POST.

- Server response: the server first performs parameter security verification on the user's requested data, and then returns the response data to the user in JSON format according to the business logic after passing the verification.

- Data processing: processing the server response data.

Success

HTTP status code 200 indicates a successful response and may contain content. If the response contains content, it will be displayed in the corresponding return content.

Common error codes

- 400 Bad Request – Invalid request format 

- 401 Unauthorized – Invalid API Key

- 403 Forbidden – You do not have access to the requested resource 

- 404 Not Found - The request is not found

- 429 Too Many Requests - Requests are too frequent and are limited by the system

- 500 Internal Server Error – Internal Server Error

- If it is failed, return body usually have an error message

## Standard Specification

Timestamp

The unit of ACCESS-TIMESTAMP in the request signature is milliseconds. The timestamp of the request must be within 30 seconds of the API service time, otherwise the request will be considered expired and rejected. If there is a large deviation between the local server time and the API server time, we recommend that you update the timestamp by query and compare the time difference between API server time and the time in your code.

Frequency limiting rules

If the request is too frequent, the system will automatically limit the request and return the “429 too many requests” status code in the http header.

· Public interface: For the market information interfaces, the global rate limit is 2 seconds with max. 20 requests.

· Authorization interface: restrict the call of the authorization interface through apikey, refer to the frequency limitation rule of each interface for frequency limitation.

Request format

There are currently only two supported request methods: GET and POST

- GET: The parameters are transmitted to the server in the path through queryString.

- POST: The parameters are sending to the server in json format.

# RestAPI

## Notice

### Get All Notices

Return data within one month

Rate Limit: 20 times/1s (IP)

HTTP Request

- GET /api/spot/v1/notice/queryAllNotices

Response Parameter

| 

| Parameter 
| Description 
 |

| noticeType 
| String 
 |

| startTime 
| String 
 |

| endTime 
| String 
 |

| languageType 
| String 
 |

Request Example

```
curl "/api/spot/v1/notice/queryAllNotices?languageType=en_US"

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1688008631614,
  "data": [
    {
      "noticeId": "23685",
      "noticeTitle": "test0629",
      "noticeDesc": "new notice",
      "createTime": "1688008040000",
      "languageType": "en_US",
      "noticeUrl": "https://www.bitget.com/en_US/support/articles/23685"
    }
  ]
}

```

Response Parameters

| 

| Parameter 
| Description 
 |

| noticeId 
| notice id 
 |

| noticeTitle 
| notice title 
 |

| noticeDesc 
| notice desc 
 |

| createTime 
| create time 
 |

| languageType 
| languageType 
 |

| noticeUrl 
| notice url 
 |

## Public

### Get Server Time

Rate Limit: 20 times/1s (IP)

HTTP Request

Obtain server time

- GET /api/spot/v1/public/time

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/time"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1622097118135,
    "data": 1622097118134
}

```

### Get Coin List

Rate Limit: 3 times/1s (IP)

HTTP Request 

Obtain all coins information on the platform

- GET /api/spot/v1/public/currencies

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/currencies"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "coinId":"1",
            "coinName":"BTC",
            "coinDisplayName":"BTC",
            "transfer":"true",
            "chains":[
                {
                    "chain":null,
                    "needTag":"false",
                    "withdrawable":"true",
                    "rechargeable":"true",
                    "withdrawFee":"0.005",
                    "depositConfirm":"1",
                    "withdrawConfirm":"1",
                    "minDepositAmount":"0.001",
                    "minWithdrawAmount":"0.001",
                    "browserUrl":"https://blockchair.com/bitcoin/testnet/transaction/"
                }
            ]
        }
    ]
}

```

Response Parameters

| 

| Parameter 
| Description 
 |

| coinId 
| Coin ID 
 |

| coinName 
| Coin name 
 |

| coinDisplayName 
| Coin display name 
 |

| transfer 
| Whether can be transferred 
 |

| chains 
|  
 |

| > chain 
| Chain name 
 |

| > needTag 
| Whether need the tag 
 |

| > withdrawable 
| Whether can be withdrawn 
 |

| > rechargeable 
| Whether can deposit 
 |

| > withdrawFee 
| Withdrawal fee, fixed amount 
 |

| > depositConfirm 
| Deposit no. of confirmation block 
 |

| > extraWithDrawFee 
| Extra withdraw fee, only applicable for part of the coins. On chain destruction, `0.1` means `10%` 
 |

| > withdrawConfirm 
| Withdrawal no. of confirmation block 
 |

| > minDepositAmount 
| Min. deposit amount, BTC 
 |

| > minWithdrawAmount 
| Min. withdrawal amount, BTC 
 |

| > browserUrl 
| Blockchain browser 
 |

### Get Symbols

Rate Limit: 20 times/1s (IP)

HTTP Request 

obtain basic configuration information of all trading pairs

- GET /api/spot/v1/public/products

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/products"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "symbol":"BTCUSDT_SPBL",
            "symbolName":"BTCUSDT",
            "symbolDisplayName":"BTCUSDT",
            "baseCoin":"BTC",
            "quoteCoin":"USDT",
            "minTradeAmount":"0.0001",
            "maxTradeAmount":"10000",
            "takerFeeRate":"0.001",
            "makerFeeRate":"0.001",
            "priceScale":"4",
            "quantityScale":"8",
            "minTradeUSDT":"5",
            "status":"online",
            "buyLimitPriceRatio": "0.05",
            "sellLimitPriceRatio": "0.05"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| symbol Id 
 |

| symbolName 
| symbol name 
 |

| symbolDisplayName 
| symbol display name 
 |

| baseCoin 
| Base coin 
 |

| quoteCoin 
| Denomination coin 
 |

| minTradeAmount 
| Min. trading amount 
 |

| maxTradeAmount 
| Max. trading amount 
 |

| takerFeeRate 
| Default taker transaction fee rate, could be overwritten by personal fee rate 
 |

| makerFeeRate 
| Default maker transaction fee rate, could be overwritten by personal fee rate 
 |

| priceScale 
| Pricing scale 
 |

| quantityScale 
| Quantity scale 
 |

| status 
| Status: offline,gray,online 
 |

| minTradeUSDT 
| Min trade USDT amount 
 |

| buyLimitPriceRatio 
| Buy price gap from market price, "0.05" means: 5% 
 |

| sellLimitPriceRatio 
| Sell price gap from market price, "0.05" means: 5% 
 |

### Get Single Symbol

Rate Limit: 20 times/1s (IP)

HTTP Request 

obtain all ticker information

- GET /api/spot/v1/public/product

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/product?symbol=BTCUSDT_SPBL"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "symbol":"BTCUSDT_SPBL",
            "symbolName":"BTCUSDT",
            "symbolDisplayName":"BTCUSDT",
            "baseCoin":"BTC",
            "quoteCoin":"USDT",
            "minTradeAmount":"0.0001",
            "maxTradeAmount":"10000",
            "takerFeeRate":"0.001",
            "makerFeeRate":"0.001",
            "priceScale":"4",
            "quantityScale":"8",
            "minTradeUSDT":"5",
            "status":"online",
            "buyLimitPriceRatio": "0.05",
            "sellLimitPriceRatio": "0.05"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| Symbol ID 
 |

| symbolName 
| Symbol Name 
 |

| symbolDisplayName 
| Symbol display name 
 |

| baseCoin 
| Base coin 
 |

| quoteCoin 
| Denomination coin 
 |

| minTradeAmount 
| Min. trading amount 
 |

| maxTradeAmount 
| Max. trading amount 
 |

| takerFeeRate 
| Taker transaction fee rate, could be overwritten by personal fee rate 
 |

| makerFeeRate 
| Maker transaction fee rate, could be overwritten by personal fee rate 
 |

| priceScale 
| Pricing scale 
 |

| quantityScale 
| Quantity scale 
 |

| status 
| Status 
 |

| minTradeUSDT 
| Min trade USDT amount 
 |

| buyLimitPriceRatio 
| Buy price gap from market price, "0.05" means: 5% 
 |

| sellLimitPriceRatio 
| Sell price gap from market price, "0.05" means: 5% 
 |

## Market

### Get Single Ticker

Rate Limit: 20 times/1s (IP)

HTTP Request 

- GET /api/spot/v1/market/ticker

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/market/ticker?symbol=BTCUSDT_SPBL"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "data": {
        "symbol": "BTCUSDT",
        "high24h": "24175.65",
        "low24h": "23677.75",
        "close": "24014.11",
        "quoteVol": "177689342.3025",
        "baseVol": "7421.5009",
        "usdtVol": "177689342.302407",
        "ts": "1660704288118",
        "buyOne": "24013.94",
        "sellOne": "24014.06",
        "bidSz": "0.0663",
        "askSz": "0.0119",
        "openUtc0": "23856.72",
        "changeUtc":"0.00301",
        "change":"0.00069"
    }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| Symbol Id 
 |

| high24h 
| 24h highest price 
 |

| close 
| Latest transaction price 
 |

| low24h 
| 24h lowest price 
 |

| ts 
| System timestamp, milliseconds 
 |

| baseVol 
| Base coin volume 
 |

| quoteVol 
| Denomination coin volume 
 |

| buyOne 
| buy one price 
 |

| sellOne 
| sell one price 
 |

| bidSz 
| Bid1 size 
 |

| askSz 
| Ask1 size 
 |

| usdtVol 
| USDT volume 
 |

| openUtc0 
| UTC0 opening price 
 |

| changeUtc 
| change since UTC0, 0.01 means 1% 
 |

| change 
| change, 0.01 means 1% 
 |

### Get All Tickers

Rate Limit: 20 times/1s (IP)

HTTP Request

- GET /api/spot/v1/market/tickers

Request Example 

```
curl "https://api.bitget.com/api/spot/v1/market/tickers"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "data": [{
        "symbol": "BTCUSDT",
        "high24h": "24175.65",
        "low24h": "23677.75",
        "close": "24014.11",
        "quoteVol": "177689342.3025",
        "baseVol": "7421.5009",
        "usdtVol": "177689342.302407",
        "ts": "1660704288118",
        "buyOne": "24013.94",
        "sellOne": "24014.06",
        "bidSz": "0.0663",
        "askSz": "0.0119",
        "openUtc0": "23856.72",
        "changeUtc":"0.00301",
        "change":"0.00069"
    }]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| Symbol Id 
 |

| high24h 
| 24h highest price 
 |

| close 
| Latest transaction price 
 |

| low24h 
| 24h lowest price 
 |

| ts 
| System timestamp 
 |

| baseVol 
| Base coin volume 
 |

| quoteVol 
| Denomination coin volume 
 |

| buyOne 
| buy one price 
 |

| sellOne 
| sell one price 
 |

| bidSz 
| Bid1 size 
 |

| askSz 
| Ask1 size 
 |

| usdtVol 
| USDT volume 
 |

| openUtc0 
| UTC0  open price 
 |

| changeUtc 
| change since UTC0, 0.01 means 1% 
 |

| change 
| change, 0.01 means 1% 
 |

### Get Recent Trades

Get most recent 500 trades

Rate Limit: 10 times/1s (IP)

HTTP Request

- GET /api/spot/v1/market/fills

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| limit 
| String 
| No 
| Default is 100，Max. is 500 
 |

Request Example   

```
curl "https://api.bitget.com/api/spot/v1/market/fills?symbol=BTCUSDT_SPBL"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "symbol":"BFTUSDT_SPBL",
            "tradeId":"781698148534505473",
            "side":"buy",
            "fillPrice":"2.38735",
            "fillQuantity":"2470.6224",
            "fillTime":"1622097282536"
        },
        {
            "symbol":"BFTUSDT_SPBL",
            "tradeId":"781698140590493697",
            "side":"sell",
            "fillPrice":"2.38649",
            "fillQuantity":"3239.7976",
            "fillTime":"1622097280642"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| Symbol ID 
 |

| tradeId 
| Filled order ID 
 |

| side 
| Trade direction, 'buy', 'sell' 
 |

| fillPrice 
| Transaction price, quote coin 
 |

| fillQuantity 
| Transaction quantity, base coin 
 |

| fillTime 
| Transaction time 
 |

### Get Market Trades

Fetch trade history within 30 days, response will be cached with same param for 10 minutes, please revise 'endTime' to get the latest records

Rate Limit: 10 times/1s (IP)

HTTP Request

- GET /api/spot/v1/market/fills-history

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| limit 
| String 
| No 
| Default is 500, Max is 1000 
 |

| tradeId 
| String 
| No 
| tradeId, return records with 'tradeId' less than the provided value 
 |

| startTime 
| String 
| No 
| startTime, ms 
 |

| endTime 
| String 
| No 
| endTime, ms 
 |

Request Example 

```
curl "https://api.bitget.com/api/spot/v1/market/fills-history?symbol=btcusdt_spbl&limit=2&tradeId=1020221685304578123&startTime=1678965010861&endTime=1678965910861"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1678965934811,
    "data": [
        {
            "symbol": "BTCUSDT_SPBL",
            "tradeId": "1020221668657385473",
            "side": "Sell",
            "fillPrice": "21120",
            "fillQuantity": "0.5985",
            "fillTime": "1678965721000"
        },
        {
            "symbol": "BTCUSDT_SPBL",
            "tradeId": "1020221660121976833",
            "side": "Buy",
            "fillPrice": "21120",
            "fillQuantity": "0.3119",
            "fillTime": "1678965719000"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| symbol 
| Symbol ID 
 |

| tradeId 
| Filled order ID, desc 
 |

| side 
| Trade direction, 'Buy', 'Sell' 
 |

| fillPrice 
| Transaction price, quote coin 
 |

| fillQuantity 
| Transaction quantity, base coin 
 |

| fillTime 
| Transaction time 
 |

### Get Candle Data

Rate Limit: 20 times/1s (IP)

HTTP Request 

obtain candlestick line data

- GET /api/spot/v1/market/candles

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| period 
| String 
| Yes 
| Candlestick line time unit, granularity (refer to the following list for values) 
 |

| after 
| String 
| No 
| Time after, milliseconds, return greater than or equals 
 |

| before 
| String 
| No 
| Time before, milliseconds, return less than or equals 
 |

| limit 
| String 
| No 
| Default 100, max 1000 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/market/candles?symbol=BTCUSDT_SPBL&period=1min&after=1659076670000&before=1659080270000&limit=100"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "open":"2.34517",
            "high":"2.34771",
            "low":"2.34214",
            "close":"2.34555",
            "quoteVol":"189631.101357091",
            "baseVol":"80862.6823",
            "usdtVol":"189631.101357091",
            "ts":"1622091360000"
        },
        {
            "open":"2.34391",
            "high":"2.34903",
            "low":"2.34391",
            "close":"2.34608",
            "quoteVol":"167725.002115681",
            "baseVol":"71479.3205",
            "usdtVol":"167725.002115681",
            "ts":"1622091420000"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| ts 
| System timestamp 
 |

| open 
| Opening price 
 |

| high 
| Highest price 
 |

| low 
| Lowest price 
 |

| close 
| Closing price 
 |

| baseVol 
| Base coin volume 
 |

| quoteVol 
| Denomination coin volume 
 |

| usdtVol 
| USDT volume 
 |

period

- 1min (1 minute)

- 5min (5 minutes)

- 15min (15 minutes)

- 30min (30 minutes)

- 1h (1 hour)

- 4h (4 hours)

- 6h (6 hours)

- 12h (12 hours)

- 1day (1 day)

- 3day (3 days)

- 1week (1 week)

- 1M (monthly line)

- 6Hutc (UTC0 6 hour)

- 12Hutc (UTC0 12 hour)

- 1Dutc (UTC0 1day)

- 3Dutc (UTC0 3rd)

- 1Wutc (UTC0 weekly)

- 1Mutc (UTC0 monthly)

### Get History Candle Data

Rate Limit: 20 times/1s (IP)

HTTP Request

obtain history candlestick line data

- GET /api/spot/v1/market/history-candles

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| period 
| String 
| Yes 
| Candlestick line time unit, granularity (refer to the following list for values) 
 |

| endTime 
| String 
| Yes 
| endTime, milliseconds 
 |

| limit 
| String 
| No 
| Default 100, max 200 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/market/history-candles?symbol=BTCUSDT_SPBL&period=1min&endTime=1659080270000&limit=100"

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":[
        {
            "open":"2.34517",
            "high":"2.34771",
            "low":"2.34214",
            "close":"2.34555",
            "quoteVol":"189631.101357091",
            "baseVol":"80862.6823",
            "usdtVol":"189631.101357091",
            "ts":"1622091360000"
        },
        {
            "open":"2.34391",
            "high":"2.34903",
            "low":"2.34391",
            "close":"2.34608",
            "quoteVol":"167725.002115681",
            "baseVol":"71479.3205",
            "usdtVol":"167725.002115681",
            "ts":"1622091420000"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| ts 
| System timestamp 
 |

| open 
| Opening price 
 |

| high 
| Highest price 
 |

| low 
| Lowest price 
 |

| close 
| Closing price 
 |

| baseVol 
| Base coin volume 
 |

| quoteVol 
| Denomination coin volume 
 |

| usdtVol 
| USDT volume 
 |

period

- 1min (1 minute)

- 5min (5 minutes)

- 15min (15 minutes)

- 30min (30 minutes)

- 1h (1 hour)

- 4h (4 hours)

- 6h (6 hours)

- 12h (12 hours)

- 1day (1 day)

- 3day (3 days)

- 1week (1 week)

- 1M (monthly line)

- 6Hutc (UTC0 6 hour)

- 12Hutc (UTC0 12 hour)

- 1Dutc (UTC0 1day)

- 3Dutc (UTC0 3rd)

- 1Wutc (UTC0 weekly)

- 1Mutc (UTC0 monthly)

### Get Depth

Rate Limit: 20 times/1s (IP)

HTTP Request

- GET /api/spot/v1/market/depth

Request Example

```
curl "https://api.bitget.com/api/spot/v1/market/depth?symbol=BTCUSDT_SPBL&type=step0&limit=100"

```

Response

```
{
    "code":"00000",
    "msg":"success",
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

```

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| type 
| String 
| Yes 
| Default: step0; value: step0, step1, step2, step3, step4, step5 
 |

| limit 
| String 
| No 
| default 150, max 200 
 |

type

- step0 original price

- step1 original price * 10 and round up

- step2 original price * 100 and round up

- step3 original price * 1000 and round up

- step4 original price * 1000 and round up to a multiple of 5

- step5 original price * 10000 and round up

example

- BTCUSDT priceScale: 2

- current price  39223.42

- step1 39223.5

- step2 39224.0

- step3 39230.0

- step4 39250.0

- step5 39300.0

 

 

 

 

 

 

 

 

 

 

 

### Get merged depth data

Speed limit rule: 20 times/1s

HTTP Request

- GET /api/spot/v1/market/merge-depth

请求参数

| 

| parameter name 
| Parameter Type 
| Required 
| describe 
 |

| symbol 
| String 
| Yes 
| 
                                                                                                                                                                                                                                                                                                                      Trading pair name, for example: BTCUSDT_SPBL 
 |

| precision 
| String 
| No 
| Price accuracy, according to the selected accuracy as the step size to return the cumulative depth, enumeration value: scale0/scale1/scale2/scale3, scale0 is not merged, the default value, in general, scale1 is the merged depth of the transaction pair’s quotation accuracy*10, generally In this case, scale2 is the quotation precision *100, scale3 is the quotation precision *1000, and the precision corresponding to 0/1/2/3 is subject to the actual return parameter "scale". The quotation precision of each trading pair is different, and some currencies The pair does not have scale2, and the request for a scale that does not exist for the currency pair will be processed according to the maximum scale. Example: A certain trading pair only has scale 0/1, and when scale2 is requested, it will be automatically reduced to scale1. 
 |

| limit 
| String 
| No 
| Fixed gear enumeration value: 1/5/15/50/max, the default gear is 100. When the actual depth does not meet the limit, it will be returned according to the actual gear. Passing in max will return the maximum gear of the trading pair. 
 |

request example

```
curl "https://api.bitget.com/api/spot/v1/market/merge-depth?symbol=BTCUSDT_SPBL&precision=scale0&limit=5"

```

return data

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692761101932,
  "data": {
    "asks": [
      [
        0.00000881,
        1000000
      ],
      [
        0.00000900,
        1000000
      ],
      [
        0.00001010,
        1000000
      ],
      [
        0.00001020,
        1110000
      ],
      [
        0.00001030,
        110000
      ]
    ],
    "bids": [
      [
        0.00000870,
        130000
      ],
      [
        0.00000860,
        130000
      ],
      [
        0.00000850,
        130000
      ],
      [
        0.00000840,
        130000
      ],
      [
        0.00000830,
        130000
      ]
    ],
    "ts": "1692761101940",
    "scale": "0.00000001",
    "precision": "scale0",
    "isMaxPrecision": "NO"
  }
}

```

Return value description

| 

| parameter name 
| Parameter Type 
| field description 
 |

| asks 
| Array 
| All buy orders at the current price, such as ["38084.5","0.5"], "38084.5" represents the depth price, and "0.5" represents the amount of base currency 
 |

| bids 
| Array 
| All sell orders at the current price 
 |

| precision 
| String 
| Current gear, for example: scale 1 
 |

| scale 
| String 
| The actual precision value, for example: 0.1 
 |

| isMaxPrecision 
| String 
| YES means it is already the maximum precision, NO is not the maximum precision 
 |

| ts 
| String 
| The time corresponding to the current depth 
 |

### VIP fee rate

Rate Limit: 10 times/1s (IP)

HTTP Request

- GET /api/spot/v1/market/spot-vip-level

Request Example

```
curl "https://api.bitget.com/api/spot/v1/market/spot-vip-level"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1675759699382,
    "data": [
        {
            "level": 1,
            "dealAmount": "1000000",
            "assetAmount": "50000",
            "takerFeeRate": "0",
            "makerFeeRate": "0",
            "withdrawAmount": "300",
            "withdrawAmountUSDT": "5000000"
        }
    ]
}

```

Response parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| level 
| Integer 
| Yes 
| VIP level 
 |

| dealAmount 
| BigDecimal 
| Yes 
| Transaction volume (USDT) within 30 days 
 |

| assetAmount 
| BigDecimal 
| Yes 
| Asset amount (USDT) 
 |

| takerFeeRate 
| BigDecimal 
| No 
| Taker fee rate, actual fee rate please refer to official announcement when '0' 
 |

| makerFeeRate 
| BigDecimal 
| No 
| Maker fee rate, actual fee rate please refer to official announcement when '0' 
 |

| withdrawAmount 
| BigDecimal 
| Yes 
| 24 hours withdraw amount (BTC) 
 |

| withdrawAmountUSDT 
| BigDecimal 
| Yes 
| 24 hours withdraw amount (USDT) 
 |

## Wallet

### Transfer

Main account only

Rate Limit：5/sec (uid)

HTTP Request

- POST /api/spot/v1/wallet/transfer

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/transfer" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"fromType": "spot","toType": "mix_usdt","amount": "100","coin": "USDT"}'

```

Response:

```
{
    "code":"00000",
    "msg":"success"
}

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| fromType 
| String 
| Yes 
| out account type 
 |

| toType 
| String 
| Yes 
| inner account type 
 |

| amount 
| String 
| Yes 
| transfer amount 
 |

| coin 
| String 
| Yes 
| transfer coin 
 |

| symbol 
| String 
| No 
| Must provide when fromType or toType = margin_isolated 
 |

| clientOid 
| String 
| No 
| custom id 
 |

- fromType, toType

spot            Accept all kinds of coins

- mix_usdt    Only USDT

- mix_usd      Coins like BTC, ETH, EOS, XRP, USDC

- mix_usdc    Only USDC

- margin_cross    Coins supported by spot cross-margin

- margin_isolated   Coins supported by spot isolated-margin

fromType/toType restriction

| 

| fromType 
| toType 
| Desc 
 |

| spot 
| spot 
| Good to go 
 |

| spot 
| mix_usdt 
| Only USDT 
 |

| spot 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| spot 
| mix_usdc 
| Only USDC 
 |

| mix_usdt 
| spot 
| Only USDT 
 |

| mix_usdt 
| mix_usd 
| Not allow 
 |

| mix_usdt 
| mix_usdc 
| Not allow 
 |

| mix_usdt 
| mix_usdt 
| Only USDT 
 |

| mix_usd 
| spot 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usd 
| mix_usdt 
| Not allow 
 |

| mix_usd 
| mix_usdc 
| Only USDC 
 |

| mix_usd 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usdc 
| spot 
| Only USDC 
 |

| mix_usdc 
| mix_usdt 
| Not allow 
 |

| mix_usdc 
| mix_usd 
| Only USDC 
 |

| mix_usdc 
| mix_usdc 
| Only USDC 
 |

| xxx 
| margin_cross 
| Only coins that supported by spot cross-margin 
 |

| xxx 
| margin_isolated 
| Only coins that supported by spot isolated-margin 
 |

 

 

 

 

 

 

### Transfer V2

Main account only

Rate Limit：5/sec (uid)

HTTP Request

- POST /api/spot/v1/wallet/transfer-v2

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/transfer-v2" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"fromType": "spot","toType": "mix_usdt","amount": "100","coin": "USDT"}'

```

Response:

```
{
    "code":"00000",
    "msg":"success",
    "data": {
        "transferId":"123456",
        "clientOrderId":"x123"
    }
}

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| fromType 
| String 
| Yes 
| out account type 
 |

| toType 
| String 
| Yes 
| inner account type 
 |

| amount 
| String 
| Yes 
| transfer amount 
 |

| coin 
| String 
| Yes 
| transfer coin 
 |

| symbol 
| String 
| No 
| Must provide when fromType or toType = margin_isolated 
 |

| clientOid 
| String 
| No 
| custom id 
 |

Response parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| transferId 
| String 
| Yes 
| Transfer ID 
 |

| clientOrderId 
| String 
| Yes 
| Client Order ID 
 |

- fromType, toType

spot            Accept all kinds of coins

- mix_usdt    Only USDT

- mix_usd      Coins like BTC, ETH, EOS, XRP, USDC

- mix_usdc    Only USDC

- margin_cross    Coins supported by spot cross-margin

- margin_isolated   Coins supported by spot isolated-margin

fromType/toType restriction

| 

| fromType 
| toType 
| Desc 
 |

| spot 
| spot 
| Good to go 
 |

| spot 
| mix_usdt 
| Only USDT 
 |

| spot 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| spot 
| mix_usdc 
| Only USDC 
 |

| mix_usdt 
| spot 
| Only USDT 
 |

| mix_usdt 
| mix_usd 
| Not allow 
 |

| mix_usdt 
| mix_usdc 
| Not allow 
 |

| mix_usdt 
| mix_usdt 
| Only USDT 
 |

| mix_usd 
| spot 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usd 
| mix_usdt 
| Not allow 
 |

| mix_usd 
| mix_usdc 
| Only USDC 
 |

| mix_usd 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usdc 
| spot 
| Only USDC 
 |

| mix_usdc 
| mix_usdt 
| Not allow 
 |

| mix_usdc 
| mix_usd 
| Only USDC 
 |

| mix_usdc 
| mix_usdc 
| Only USDC 
 |

| xxx 
| margin_cross 
| Only coins that supported by spot cross-margin 
 |

| xxx 
| margin_isolated 
| Only coins that supported by spot isolated-margin 
 |

 

 

 

 

 

 

### Sub Transfer

Initiate by the main account. Restricted by the sub accounts

This interface supports to transfer in below ways

| 

| Transfer from 
| Transfer to 
| Desc 
 |

| main account 
| sub account 
| Sub account belongs to the main account 
 |

| sub account 
| sub account 
| Two sub account belongs to the same main account 
 |

| sub account 
| main account 
| Sub account belongs to the main account 
 |

1). Main/Sub transfer requires IP whitelist

2). Transfer between fromUserId and toUserId should have direct/brother relationship

3). Note the risk may increase when transfer out from account with cross margin mode

 

Rate Limit：2/sec (uid)

HTTP Request

- POST /api/spot/v1/wallet/subTransfer

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/subTransfer" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"fromType": "spot","toType": "mix_usdt","amount": "100","coin": "USDT","clientOid":"12345","fromUserId":"1","toUserId":"2"}'

```

Response:

```
{
    "code":"00000",
    "msg":"success"
}

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| fromType 
| String 
| Yes 
| from account type 
 |

| toType 
| String 
| Yes 
| to account type 
 |

| amount 
| String 
| Yes 
| transfer amount 
 |

| coin 
| String 
| Yes 
| transfer coin 
 |

| clientOid 
| String 
| Yes 
| unique custom id, idempotent control 
 |

| fromUserId 
| String 
| Yes 
| from user ID 
 |

| toUserId 
| String 
| Yes 
| to user ID 
 |

 

 

 

 

 

 

- fromType, toType

spot            Accept all kinds of coins

- mix_usdt    Only USDT

- mix_usd      Coins like BTC, ETH, EOS, XRP, USDC

- mix_usdc    Only USDC

- margin_cross    Coins supported by spot cross-margin

- margin_isolated   Coins supported by spot isolated-margin

fromType/toType restriction

| 

| fromType 
| toType 
| Desc 
 |

| spot 
| spot 
| Good to go 
 |

| spot 
| mix_usdt 
| Only USDT 
 |

| spot 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| spot 
| mix_usdc 
| Only USDC 
 |

| mix_usdt 
| spot 
| Only USDT 
 |

| mix_usdt 
| mix_usd 
| Not allow 
 |

| mix_usdt 
| mix_usdc 
| Not allow 
 |

| mix_usdt 
| mix_usdt 
| Only USDT 
 |

| mix_usd 
| spot 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usd 
| mix_usdt 
| Not allow 
 |

| mix_usd 
| mix_usdc 
| Only USDC 
 |

| mix_usd 
| mix_usd 
| Only  margin Coin like BTC, ETH, EOS, XRP, USDC 
 |

| mix_usdc 
| spot 
| Only USDC 
 |

| mix_usdc 
| mix_usdt 
| Not allow 
 |

| mix_usdc 
| mix_usd 
| Only USDC 
 |

| mix_usdc 
| mix_usdc 
| Only USDC 
 |

| xxx 
| margin_cross 
| Only coins that supported by spot cross-margin 
 |

| xxx 
| margin_isolated 
| Only coins that supported by spot isolated-margin 
 |

### Get Coin Address

Rate Limit：5/sec (uid)

HTTP Request

- GET /api/spot/v1/wallet/deposit-address

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| Yes 
| currency name 
 |

| chain 
| String 
| Yes 
| chain name 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/wallet/deposit-address?coin=USDT&chain=trc20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response:

```
{
  "code": "00000",
  "msg": "success",
  "data": {
    "address": "1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv",
    "chain": "BTC-Bitcoin",
    "coin": "BTC",
    "tag": "",
    "url": "https://btc.com/1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| address 
| currency address 
 |

| chain 
| chain name 
 |

| coin 
| currency name 
 |

| tag 
| tag 
 |

| url 
| Blockchain browser address 
 |

### Withdraw

Main account only

Just withdraw coins on the chain

Rate Limit：5/sec (Uid)

HTTP Request

- POST /api/spot/v1/wallet/withdrawal

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| Yes 
| currency name 
 |

| address 
| String 
| Yes 
| withdraw address 
 |

| chain 
| String 
| Yes 
| chain name 
 |

| tag 
| String 
| No 
| tag 
 |

| amount 
| String 
| Yes 
| Withdraw amount 
 |

| remark 
| String 
| No 
| remark 
 |

| clientOid 
| String 
| No 
| custom id 
 |

'address' should be in your main-account's address book

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/withdrawal" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"coin": "USDT","address": "TBQ2LGFysnqkscvKqLBxnVVVw7ohiDvbdZ","chain": "trc20","amount": "10"}'

```

Response:

```
{
  "code": "00000",
  "msg": "success",
  "data": "888291686266343424"
}

```

Response Description

| 

| Parameter 
| Description 
 |

| data 
| Order ID 
 |

### Withdraw V2

Main account only

Just withdraw coins on the chain

Rate Limit：5/sec (Uid)

HTTP Request

- POST /api/spot/v1/wallet/withdrawal-v2

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| Yes 
| currency name 
 |

| address 
| String 
| Yes 
| withdraw address 
 |

| chain 
| String 
| Yes 
| chain name 
 |

| tag 
| String 
| No 
| tag 
 |

| amount 
| String 
| Yes 
| Withdraw amount 
 |

| remark 
| String 
| No 
| remark 
 |

| clientOid 
| String 
| No 
| custom id 
 |

'address' should be in your main-account's address book

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/withdrawal-v2" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"coin": "USDT","address": "TBQ2LGFysnqkscvKqLBxnVVVw7ohiDvbdZ","chain": "trc20","amount": "10"}'

```

Response:

```
{
  "code": "00000",
  "msg": "success",
  "data": {
    "orderId":888291686266343424",
    "clientOrderId":"123"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

| clientOrderId 
| client order ID 
 |

### Inner Withdraw

Main account only

Internal withdrawal means that both users are on the Bitget platform

Withdraw money directly in the form of uid, without going on the chain, no need to pass the address

Rate Limit：5/sec (Uid)

HTTP Request

- POST /api/spot/v1/wallet/withdrawal-inner

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| Yes 
| currency 
 |

| toUid 
| String 
| Yes 
| target uid 
 |

| amount 
| String 
| Yes 
| Withdraw amount 
 |

| clientOid 
| String 
| No 
| custom id 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/withdrawal-inner" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"coin": "USDT","toUid": "6314497154","amount": "10"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "data": "888291686266343424"
}

```

Response Description

| 

| Parameter 
| description 
 |

| data 
| Order ID 
 |

### Inner Withdraw v2

Main account only

Internal withdrawal means that both users are on the Bitget platform

Withdraw money directly in the form of uid, without going on the chain, no need to pass the address

Rate Limit：5/sec (Uid)

HTTP Request

- POST /api/spot/v1/wallet/withdrawal-inner-v2

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| Yes 
| currency 
 |

| toUid 
| String 
| Yes 
| target uid 
 |

| amount 
| String 
| Yes 
| Withdraw amount 
 |

| clientOid 
| String 
| No 
| custom id 
 |

| toType 
| String 
| No 
| 'email/mobile/uid', default 'uid' 
 |

| areaCode 
| String 
| No 
| Tel area code, This field is mandatory when the toType equals to 'mobile' 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/wallet/withdrawal-inner-v2" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"coin": "USDT","toUid": "6314497154","amount": "10"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "data": {
    "orderId":888291686266343424",
    "clientOrderId":"123"
  }
}

```

Response Description

| 

| Parameter 
| description 
 |

| orderId 
| Order ID 
 |

| clientOrderId 
| client order ID 
 |

### Get Withdraw list

Rate Limit：20/1s (Uid)

HTTP Request

- GET /api/spot/v1/wallet/withdrawal-list

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| currency 
 |

| clientOid 
| String 
| No 
| clientOid 
 |

| startTime 
| String 
| Yes 
| start Time (timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end Time(timestamp ms) 
 |

| pageNo 
| String 
| No 
| pageNo default 1 
 |

| pageSize 
| String 
| No 
| pageSize default 20, max 100 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/wallet/withdrawal-list?coin=USDT&clientOid=123&startTime=1659036670000&endTime=1659076670000&pageNo=1&pageSize=20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response:

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1654507973411,
    "data": [
        {
            "id": "912533114861326336",
            "txId": "912533114861326336",
            "coin": "USDT",
            "clientOid": "123",
            "type": "withdraw",
            "amount": "10.00000000",
            "status": "success",
            "toAddress": "7713789662",
            "fee": "0.00000000",
            "chain": "erc20",
            "confirm": "0",
            "tag": null,
            "cTime": "1653290769222",
            "uTime": "1653290769222"
        }
    ]
}

```

Response Description

| 

| Parameter 
| Description 
 |

| id 
| order Id 
 |

| txId 
| trade Id 
 |

| coin 
| currency 
 |

| clientOid 
| clientOid 
 |

| type 
| type: 'withdraw' 
 |

| amount 
| withdraw amount 
 |

| status 
| status 
 |

| toAddress 
| Withdraw address 
 |

| fee 
| Withdraw fee 
 |

| chain 
| Withdraw chain 
 |

| confirm 
| confirm times for withdraw 
 |

| tag 
| tag 
 |

| cTime 
| create time 
 |

| uTime 
| update time 
 |

- status

Pending

- pending_review

- Pending_fail

- pending_review_fail

- wallet_processing

- wallet_fail

- cancel

- reject

- success

- wait_frozen waiting to be frozen

- wait_create_order to create order

- deposit_check deposit to be checked

- deposit_check_fail deposit check failed

- dealing processing

- frozen_fail 

- wait_unfreeze to be unfreeze

- wait_deducted to be deducted

- wait_recharge to be recharge

- wait_recharge_system to be system recharge

- recharge_fail_risk_wait_to_system risk control failed, to be system recharge

- risk_audit risk control auditing

- pre_success waiting on chain confirmation

- wait_small_check small amount checking

- unknown

### Get Deposit List

Rate Limit：20/1s (Uid)

HTTP Request

- GET /api/spot/v1/wallet/deposit-list

Request Parameter

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| currency 
 |

| startTime 
| String 
| Yes 
| start time(timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end time(timestamp ms) 
 |

| pageNo 
| String 
| No 
| pageNo default 1 
 |

| pageSize 
| String 
| No 
| pageSize default20  Max 100 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/wallet/deposit-list?coin=USDT&startTime=1659036670000&endTime=1659076670000&pageNo=1&pageSize=20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response:

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1654507973411,
    "data": [
        {
            "id": "912533114861326336",
            "txId": "912533114861326336",
            "coin": "USDT",
            "type": "deposit",
            "amount": "10.00000000",
            "status": "success",
            "toAddress": "7713789662",
            "fee":"0",
            "chain": "erc20",
            "confirm":"10",
            "tag": null,
            "cTime": "1653290769222",
            "uTime": "1653290769222"
        }
    ]
}

```

Response Data

| 

| Parameter 
| Description 
 |

| id 
| order Id 
 |

| txId 
| trade Id 
 |

| coin 
| currency 
 |

| type 
| type: 'deposit' 
 |

| amount 
| deposit amount 
 |

| status 
| status 
 |

| toAddress 
| deposit address 
 |

| fee 
| fee, might be null 
 |

| confirm 
| confirm, might be null 
 |

| chain 
| deposit chain 
 |

| tag 
| tag 
 |

| cTime 
| create time 
 |

| uTime 
| update time 
 |

- status

Pending

- pending_review

- Pending_fail

- pending_review_fail

- wallet_processing

- wallet_fail

- cancel

- reject

- success

- wait_frozen waiting to be frozen

- wait_create_order to create order

- deposit_check deposit to be checked

- deposit_check_fail deposit check failed

- dealing processing

- frozen_fail 

- wait_unfreeze to be unfreeze

- wait_deducted to be deducted

- wait_recharge to be recharge

- wait_recharge_system to be system recharge

- recharge_fail_risk_wait_to_system risk control failed, to be system recharge

- risk_audit risk control auditing

- pre_success waiting on chain confirmation

- wait_small_check small amount checking

- unknown

### Get User Fee Ratio

Rate Limit：10/sec (Uid)

HTTP Request

- GET /api/user/v1/fee/query

Request Parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| yes 
| symbol（mix：BTCUSDT_UMCBL， spot：BTCUSDT_SPBL， spot margin：BTCUSDT） 
 |

| business 
| String 
| yes 
| business type（mix：mix， spot：spot， spot margin：margin） 
 |

Request Example

```
curl "https://api.bitget.com/api/user/v1/fee/query?symbol=BTCUSDT_UMCBL&business=mix" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1683875302853,
    "data": {
        "makerRate": "0.0002",
        "takerRate": "0.0006"
    }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| makerRate 
| maker fee 
 |

| takerRate 
| taker fee 
 |

## Account

### Get ApiKey Info

Rate Limit：1/sec (Uid)

HTTP Request

- GET  /api/spot/v1/account/getInfo

Request Example

```
curl "https://api.bitget.com/api/spot/v1/account/getInfo" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "data": {
        "user_id": "714229403",
        "inviter_id": "682221498",
        "ips": "172.23.88.91",
        "authorities": [
            "trade",
            "readonly"
        ],
        "parentId":566624801,
        "trader":false,
        "isSpotTrader": false
    }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| user_id 
| uid 
 |

| inviter_id 
| Inviter ID 
 |

| agent_inviter_code 
| agent inviter code 
 |

| channel 
| channel 
 |

| ips 
| ip whitelist address 
 |

| authorities 
| apiKey permission 
 |

| parentId 
| Parent Uid 
 |

| trader 
| true is Trader, false is not 
 |

| isSpotTrader 
| true is Spot Trader, false is not 
 |

### Get Account Assets

Rate Limit: 10 times/1s (uid)

HTTP Request 

obtain account assets

- GET /api/spot/v1/account/assets

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| CoinName, default will return data even assets are 0 when 'coin' is null 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/account/assets?coin=USDT" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response

```
{
  "code":"00000",
  "message":"success",
  "data":[
    {
        "coinId":"10012",
        "coinName":"usdt",
        "coinDisplayName":"usdt",
        "available":"0",
        "frozen":"0",
        "lock":"0",
        "uTime":"1622697148"
    }
]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| coinId 
| Coin ID 
 |

| coinName 
| Coin name 
 |

| coinDisplayName 
| Coin display name 
 |

| available 
| Available assets 
 |

| frozen 
| Frozen: create order frozen margin 
 |

| lock 
| Locked assets, like become a fiat/p2p merchant 
 |

| uTime 
| Update timing 
 |

### Get Account Assets Lite

Rate Limit: 10 times/1s (uid)

HTTP Request

- GET /api/spot/v1/account/assets-lite

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| CoinName, default 'coin' is null, will return data with assets > 0; if 'coin' is not null, will return the coin no matter what the assets is 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/account/assets-lite?coin=USDT" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response

```
{
  "code":"00000",
  "message":"success",
  "data":[
    {
        "coinId":"10012",
        "coinName":"usdt",
        "coinDisplayName":"usdt",
        "available":"0",
        "frozen":"0",
        "lock":"0",
        "uTime":"1622697148"
    }
]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| coinId 
| Coin ID 
 |

| coinName 
| Coin name 
 |

| coinDisplayName 
| Coin display name 
 |

| available 
| Available assets 
 |

| frozen 
| Frozen: create order frozen margin 
 |

| lock 
| Locked assets, like become a fiat/p2p merchant 
 |

| uTime 
| Update timing 
 |

### Get sub Account Spot Assets

Main account only

Rate Limit: 1 times/10s (uid)

HTTP Request 

obtain account assets

- POST /api/spot/v1/account/sub-account-spot-assets

Request parameter
- N/A

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/account/sub-account-spot-assets" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d "{}"

```

Response

```
{
  "code":"00000",
  "message":"success",
  "data":[
    {
      "userId": 9165454769,
      "spotAssetsList": [
        {
          "coinId": 1,
          "coinName": "BTC",
          "available": "1.1",
          "frozen": "0",
          "lock": "1.1"
        }
      ]
    },
    {
      "userId": 1765254759,
      "spotAssetsList": [
        {
          "coinId": 2,
          "coinName": "ETH",
          "available": "12.1",
          "frozen": "0",
          "lock": "1.1"
        }
      ]
    }
]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| coinId 
| Coin ID 
 |

| coinName 
| Coin name 
 |

| available 
| Available assets 
 |

| frozen 
| Frozen assets 
 |

| lock 
| Locked assets 
 |

### Get Bills

Rate Limit: 10 times/1s (uid)

HTTP Request

Obtain transaction detail flow

- POST /api/spot/v1/account/bills

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| coinId 
| Integer 
| No 
| Coin ID 
 |

| groupType 
| String 
| No 
| Transaction group type groupType 
 |

| bizType 
| String 
| No 
| Business type bizType 
 |

| after 
| String 
| No 
| Returns data that less than the passed billId 
 |

| before 
| String 
| No 
| Returns data that grater than the passed billId 
 |

| limit 
| Integer 
| No 
| The number of returned results, the default is 100, the max. is 500 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/account/bills" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d '{ 
    "coinId":"2",
    "groupType":"deposit",
    "bizType":"deposit",
    "before":"987952085712531455",
    "after":"987952085712531457",
    "limit":"100"
}'

```

Response

```
{
  "code":"00000",
  "message":"success",
  "data":[{
      "cTime":"1622697148",
      "coinId":"22",
      "coinName":"usdt",
      "groupType":"deposit",
      "bizType":"transfer-in", 
      "quantity":"1",
      "balance": "1",
      "fees":"0",
      "billId":"1291"
}]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| cTime 
| Creation time 
 |

| coinId 
| Coin Id 
 |

| coinName 
| Coin name 
 |

| groupType 
| Transaction flow type 
 |

| bizType 
| Transaction bill business type 
 |

| quantity 
| Quantity 
 |

| balance 
| Assets before transfer 
 |

| fees 
| Transaction fees 
 |

| billId 
| ID 
 |

### Get Transfer List

Rate Limit: 20 times/1s (uid)

HTTP Request

- GET /api/spot/v1/account/transferRecords

Request parameter

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| coinId 
| Integer 
| Yes 
| Coin ID 
 |

| fromType 
| String 
| Yes 
| Major type of bill accountType 
 |

| after 
| String 
| Yes 
| End time, seconds 
 |

| before 
| String 
| Yes 
| Start time, seconds 
 |

| clientOid 
| String 
| No 
| clientOid, match record that equals to the provided value 
 |

| limit 
| Integer 
| No 
| The number of returned results, the default is 100, the max. is 500 
 |

Request Example

```
curl "https://api.bitget.com/api/spot/v1/account/transferRecords?coinId=2&fromType=exchange&after=1659076670&before=1659076670&limit=100" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Response

```
{
    "code":"00000",
    "data":[
        {
            "coinName":"btc",
            "status":"Successful",
            "toType":"USD_MIX",
            "toSymbol":"",
            "fromType":"CONTRACT",
            "fromSymbol":"BTC/USD",
            "amount":"1000.00000000",
            "tradeTime":"1631070374488",
            "clientOid": "1",
            "transferId": "997381107487641600"
        }
    ],
    "msg":"success"
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| coinName 
| Coin name 
 |

| status 
| Transfer status: Successful, Failed, Processing 
 |

| toType 
| Transfer in account type  accountType 
 |

| toSymbol 
| Transfer to account Symbol 
 |

| fromType 
| Transfer out account type  accountType 
 |

| fromSymbol 
| Transfer from account Symbol 
 |

| amount 
| Number of transfers 
 |

| tradeTime 
| Transfer time, ms 
 |

| clientOid 
| client order ID 
 |

| transferId 
| Transfer ID 
 |

- fromType

exchange: spot

- usdt_mix: future USDT

- usdc_mix: future USDC

- usd_mix: future coins

- margin_cross: cross margin account

- margin_isolated: isolated margin account

## Trade

### Place order

Rate Limit: 10/sec (uid)

Trader Rate Limit: 1/sec (uid)

HTTP Request 

- POST /api/spot/v1/trade/orders

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/orders" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","side": "buy","orderType": "limit","force":"normal","price":"23222.5","quantity":"1","clientOrderId":"myorder_16569403333"}'

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":{
        "orderId":"1001",
        "clientOrderId":"hgXjh89AsxleMSw"
    }
}

```

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| side 
| String 
| Yes 
| Trade direction: buy or sell 
 |

| orderType 
| String 
| Yes 
| Order type limit/market 
 |

| force 
| String 
| Yes 
| force 
 |

| price 
| String 
| No 
| Limit pricing, null if orderType is market 
 |

| quantity 
| String 
| Yes 
| Order quantity, base coin when orderType is limit; quote coin when orderType is buy-market, base coin when orderType is sell-market 
 |

| clientOrderId 
| String 
| No 
| Custom id length: 40 
 |

Duplicate clientOrderId Response

```
{
    "code": "43118",
    "msg": "clientOrderId duplicate"
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| code 
| "00000": success, else failure 
 |

| msg 
| "success" or failure message 
 |

| data 
| response data 
 |

| > orderId 
| Order ID 
 |

| > clientOrderId 
| Custom ID 
 |

 

 

### Batch order

Rate Limit: 5/sec (uid)

Trader Rate Limit: 1/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/batch-orders

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/batch-orders" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderList":[{"side":"buy","orderType": "limit","force":"normal","price":"23222.5","quantity":"1","clientOrderId":"myorder_16569403333"}] }'

```

Response

```
{
    "code":"00000",
    "msg":"success",
    "data":{
        "orderId":"1001",
        "clientOrderId":"hgXjh89AsxleMSw"
    }
}

```

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| orderList 
| List 
| Yes 
| order data list (max length 50) 
 |

- orderList

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| side 
| String 
| Yes 
| Order side buy/sell 
 |

| orderType 
| String 
| Yes 
| Order type limit/market 
 |

| force 
| String 
| Yes 
| order time force 
 |

| price 
| String 
| No 
| Limit price, null if orderType is market 
 |

| quantity 
| String 
| Yes 
| Order quantity, base coin 
 |

| clientOrderId 
| String 
| No 
| Custom order ID 
 |

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1666336231317,
    "data": {
        "resultList": [
            {
                "orderId": "96724974842718610",
                "clientOrderId": "1"
            }
        ],
        "failure": [
            {
                "orderId": "96724974842718611",
                "clientOrderId": "1",
                "errorMsg": "clientOrderId duplicate"
            }
        ]
    }
}

```

Response Body

| 

| Parameter 
| Description 
 |

| resultList 
| Success result array 
 |

| > orderId 
| Order ID 
 |

| > clientOrderId 
| client order ID 
 |

| Failure 
| Failed Array 
 |

| > orderId 
| Order ID 
 |

| > clientOrderId 
| client order ID 
 |

| > errorMsg 
| error message 
 |

 

 

 

 

 

 

 

 

 

 

 

 

 

 

### Cancel order

Rate Limit: 10 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/cancel-order

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| orderId 
| String 
| Yes 
| Order ID 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/cancel-order" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderId": "34923828882"}'

```

Response

```
{

  "code":"00000",
   "message":"success",
  "data": "202934892814667"
}   

```

 

 

 

 

 

 

 

### Cancel order V2

Rate Limit: 10 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/cancel-order-v2

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| orderId 
| String 
| No 
| Order ID, 'clientOid' & 'orderId' must have one 
 |

| clientOid 
| String 
| No 
| Client Order ID, 'clientOid' & 'orderId' must have one 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/cancel-order-v2" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderId": "34923828882"}'

```

Response

```
{

  "code":"00000",
   "message":"success",
  "data": {
    "orderId":"34923828881",
    "clientOrderId":"xx001"
  }
} 

```

 

 

 

 

 

### Cancel order By Symbol

Rate Limit: 10 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/cancel-symbol-order

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/cancel-symbol-order" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL"}'

```

Response

```
{

  "code":"00000",
   "message":"success",
  "data": "BTCUSDT_SPBL"
} 

```

Final cancel result should be re-confirmed

 

 

 

 

 

### Cancel order in batch (single instruments)

Rate Limit: 5 times/1s (uid)

HTTP Request

- POST /api/spot/v1/trade/cancel-batch-orders

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| orderIds 
| String[] 
| Yes 
| Order ID array, max size: 50 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/cancel-batch-orders" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderIds": ["34923828882"]}'

```

Response

```
{

  "code":"00000",
  "message":"success",
  "data": ["202934892814667"]
}   

```

 

 

 

 

 

 

 

### Cancel order in batch V2 (single instruments)

Rate Limit: 5 times/1s (uid)

HTTP Request

- POST /api/spot/v1/trade/cancel-batch-orders-v2

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| orderIds 
| String[] 
| No 
| Order ID array, 'orderIds' or 'clientOids' must have one 
 |

| clientOids 
| String[] 
| No 
| clientOid array, 'orderIds' or 'clientOids' must have one 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/cancel-batch-orders-v2" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderIds": ["34923828882"]}'

```

Response

```
{

  "code":"00000",
  "message":"success",
  "data": {
        "resultList":[
            {
                "orderId":"34923828882",
                "clientOrderId":"xxx002"
            }
        ],
        "failure":[
            {
                "clientOrderId":"xxx001",
                "errorMsg":"duplicate clientOrderId",
                "errorCode":"40725"
            }
        ]
    }
} 

```

 

 

 

 

 

 

 

### Get order details

Rate Limit: 20 times/sec(uid)

HTTP Request

- POST /api/spot/v1/trade/orderInfo

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| orderId 
| String 
| No 
| Order ID, clientOrderId and orderId should have one 
 |

| clientOrderId 
| String 
| No 
| Custom ID, clientOrderId and orderId should have one (clientOrderId must be user-generated to be valid, and only orders within 24 hours can be queried) 
 |

User could query cancelled/filled order details within 24 hours; Noted that after 24 hours should query via history interface

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/orderInfo" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderId": "34923828882"}'

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1684492945476,
    "data": [
        {
            "accountId": "222222222",
            "symbol": "TRXUSDT_SPBL",
            "orderId": "1041901704004947968",
            "clientOrderId": "c5e8a5e1-a07f-4202-8061-b88bd598b264",
            "price": "0",
            "quantity": "10.0000000000000000",
            "orderType": "market",
            "side": "buy",
            "status": "full_fill",
            "fillPrice": "0.0699782527055350",
            "fillQuantity": "142.9015000000000000",
            "fillTotalAmount": "9.9999972790000000",
            "enterPointSource": "API",
            "feeDetail": "{\"BGB\":{\"deduction\":true,\"feeCoinCode\":\"BGB\",\"totalDeductionFee\":-0.017118519726,\"totalFee\":-0.017118519726,\"newFees\":{\"t\":1,\"d\":1,\"r\":1,"\c\":1}}}",
            "orderSource": "market",
            "cTime": "1684134644509"
        }
    ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| accountId 
| Account ID 
 |

| symbol 
| Symbol Id 
 |

| orderId 
| Order ID 
 |

| clientOrderId 
| Custom ID 
 |

| price 
| Order price, quote coin 
 |

| quantity 
| Order quantity (base coin when orderType=limit; quote coin when orderType=market) 
 |

| orderType 
| Order type, limit/market 
 |

| side 
| Order direction, buy/sell 
 |

| status 
| Order status 
 |

| fillPrice 
| Transaction price 
 |

| fillQuantity 
| Transaction quantity 
 |

| fillTotalAmount 
| Total transaction volume 
 |

| enterPointSource 
| enterPointSource 
 |

| cTime 
| Creation time 
 |

| feeDetail 
| order fee detail, json string 
 |

| > deduction 
| Is deduction 
 |

| > feeCoinCode 
| Fee coin, like BGB 
 |

| > totalDeductionFee 
| Total deduction 
 |

| > totalFee 
| Total fee 
 |

| > newFees 
| Object 
 |

| >> t 
| Total fee, base coin when 'buy', quote coin when 'sell' 
 |

| >> d 
| Fee deduction: BGB quantity 
 |

| >> r 
| Real fee deducted, base coin when 'buy', quote coin when 'sell' 
 |

| >> c 
| Coupon deducted: base coin when 'buy', quote coin when 'sell' 
 |

| orderSource 
| orderSource 
 |

### Get order List

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/open-orders

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| No 
| Symbol Id. If query all, pass empty string "" 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/open-orders" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL"}'

```

Response

```
{
  "code":"00000",
  "message":"success",
"data":[{
  "accountId":"10012",
  "symbol":"btcusdt_spbl",
  "orderId":"2222222",
  "clientOrderId":"xxxxxxx",
  "price":"34829.12",
  "quantity":"1",  
  "orderType":"limit",
  "side":"buy",
  "status":"new",
  "fillPrice":"0",
  "fillQuantity":"0",
  "fillTotalAmount":"0",
  "enterPointSource": "WEB",
  "cTime":"1622697148"
}]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| accountId 
| Account ID 
 |

| symbol 
| Trading pair name 
 |

| orderId 
| Order ID 
 |

| clientOrderId 
| Custom ID 
 |

| price 
| Order price 
 |

| quantity 
| Order quantity (base coin when orderType=limit; quote coin when orderType=market) 
 |

| orderType 
| Order type, limit/market 
 |

| side 
| Order direction, buy/sell 
 |

| status 
| Order status 
 |

| fillPrice 
| Transaction price 
 |

| fillQuantity 
| Transaction quantity 
 |

| fillTotalAmount 
| Total transaction volume 
 |

| enterPointSource 
| enterPointSource 
 |

| cTime 
| Creation time 
 |

### Get order history

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/history

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol Id 
 |

| after 
| String 
| No 
| orderId, return the data less than this orderId 
 |

| before 
| String 
| No 
| orderId, return the data greater than this orderId 
 |

| limit 
| Integer 
| No 
| The number of returned results, the default is 100, the max. is 500 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/history" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","after":"1659076670000","before":"1659076670000","limit":"100"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684493060724,
  "data": [
    {
      "accountId": "2222222222",
      "symbol": "TRXUSDT_SPBL",
      "orderId": "1041901704004947968",
      "clientOrderId": "c5e8a5e1-a07f-4202-8061-b88bd598b264",
      "price": "0",
      "quantity": "10.0000000000000000",
      "orderType": "market",
      "side": "buy",
      "status": "full_fill",
      "fillPrice": "0.0699782527055350",
      "fillQuantity": "142.9015000000000000",
      "fillTotalAmount": "9.9999972790000000",
      "enterPointSource": "API",
      "feeDetail": "{\"BGB\":{\"deduction\":true,\"feeCoinCode\":\"BGB\",\"totalDeductionFee\":-0.017118519726,\"totalFee\":-0.017118519726,\"newFees\":{\"t\":1,\"d\":1,\"r\":1,"\c\":1}}}",
      "orderSource": "market",
      "cTime": "1684134644509"
    }
  ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| accountId 
| Account ID 
 |

| symbol 
| Symbol Id 
 |

| orderId 
| Order ID 
 |

| clientOrderId 
| Custom ID 
 |

| price 
| Order price 
 |

| quantity 
| Order quantity (base coin when orderType=limit; quote coin when orderType=market) 
 |

| orderType 
| Order type, limit/market 
 |

| side 
| Order direction, buy/sell 
 |

| status 
| Order status 
 |

| fillPrice 
| Transaction price 
 |

| fillQuantity 
| Transaction quantity 
 |

| fillTotalAmount 
| Total transaction volume 
 |

| enterPointSource 
| enterPointSource 
 |

| cTime 
| Creation time 
 |

| feeDetail 
| order fee detail 
 |

| > deduction 
| Is deduction 
 |

| > feeCoinCode 
| Fee coin, like BGB 
 |

| > totalDeductionFee 
| Total deduction 
 |

| > totalFee 
| Total fee 
 |

| > newFees 
| Object 
 |

| >> t 
| Total fee, base coin when 'buy', quote coin when 'sell' 
 |

| >> d 
| Fee deduction: BGB quantity 
 |

| >> r 
| Real fee deducted, base coin when 'buy', quote coin when 'sell' 
 |

| >> c 
| Coupon deducted: base coin when 'buy', quote coin when 'sell' 
 |

| orderSource 
| orderSource 
 |

### Get transaction details

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/trade/fills

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| orderId 
| String 
| No 
| Order ID 
 |

| after 
| String 
| No 
| Max orderId, return data less than this 'orderId' 
 |

| before 
| String 
| No 
| Min orderId, return data greater or equals to this 'orderId' 
 |

| limit 
| Integer 
| No 
| The number of returned results, the default is 100, the max. is 500 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/trade/fills" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "BTCUSDT_SPBL","orderId":"34923828882","after":"349234552212","before":"34923775522","limit":"100"}'

```

Response

```
{
  "code":"",
  "message":"",
  "data":[{
  "accountId":"1001",
  "symbol":"btcusdt_spbl",
  "orderId":"100021",
  "fillId":"102211",
  "orderType":"limit",
  "side":"buy",
  "fillPrice":"38293.12",
  "fillQuantity":"1",
  "fillTotalAmount":"38293.12",
  "cTime":"1622697148",
  "feeCcy":"btc",
  "fees":"0.0001"
}]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| accountId 
| account ID 
 |

| symbol 
| Symbol ID 
 |

| orderId 
| order ID 
 |

| fillId 
| fill ID 
 |

| orderType 
| order type  (limit/market ) 
 |

| side 
| order side (buy/ sell) 
 |

| fillPrice 
| order filled price 
 |

| fillQuantity 
| order filled quantity 
 |

| fillTotalAmount 
| order filled total amount 
 |

| cTime 
| create time (milli seconds) 
 |

| feeCcy 
| fee currency 
 |

| fees 
| fees 
 |

### Place plan order

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/plan/placePlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| side 
| String 
| Yes 
| order side (buy/ sell) 
 |

| triggerPrice 
| BigDecimal 
| Yes 
| order trigger price 
 |

| executePrice 
| BigDecimal 
| No 
| Execute price, could not be null when orderType=limit 
 |

| size 
| BigDecimal 
| Yes 
| purchase quantity, base coin amount when orderType=limit, quote coin amount when orderType=market 
 |

| triggerType 
| String 
| Yes 
| order trigger type (fill_price/market_price ) 
 |

| orderType 
| String 
| Yes 
| order type  (limit/market ) 
 |

| clientOid 
| String 
| No 
| Customized client order ID, idempotent control 
 |

| timeInForceValue 
| String 
| No 
| Order validity 
 |

| placeType 
| String 
| No 
| amount/total 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/placePlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"symbol": "TRXUSDT_SPBL", "side": "buy", "triggerPrice": 0.041572, "executePrice": "0.041572", "size": 151, "triggerType": "market_price", "orderType": "limit","clientOid": "12345", "timeInForceValue": "normal"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134576535,
  "data": {
    "orderId": "974792555020390400",
    "clientOrderId": "974792554995224576"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| order ID 
 |

| clientOrderId 
| Custom ID 
 |

 

 

 

 

 

 

 

 

### Modify plan order

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/plan/modifyPlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| orderId 
| String 
| No 
| Order ID, 'orderId' or 'clientOid' must have one 
 |

| clientOid 
| String 
| No 
| Client Order ID, 'orderId' or 'clientOid' must have one 
 |

| triggerPrice 
| BigDecimal 
| Yes 
| order trigger price 
 |

| executePrice 
| BigDecimal 
| No 
| order execute price 
 |

| size 
| String 
| No 
| purchase quantity 
 |

| orderType 
| String 
| Yes 
| order type (limit/market) 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/modifyPlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"orderId": "974792060738441216", "triggerPrice": 0.041222, "executePrice":"0.041272", "size": 156, "orderType":"limit"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668136575920,
  "data": {
    "orderId": "974792060738441216",
    "clientOrderId": "974792554995224576"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| order ID 
 |

| clientOrderId 
| Custom ID 
 |

 

 

 

 

 

 

 

 

### Cancel plan order

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/plan/cancelPlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| orderId 
| String 
| No 
| Order ID, 'orderId' or 'clientOid' must have one 
 |

| clientOid 
| String 
| No 
| Client Order ID, 'orderId' or 'clientOid' must have one 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/cancelPlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"orderId": "974792060738441216"}'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134497496,
  "data": "974792060738441216"
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| data 
| orderId or clientOid, same as input param 
 |

 

 

 

 

 

 

 

 

### Get current plan orders

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/plan/currentPlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| pageSize 
| String 
| Yes 
| Page Size 
 |

| lastEndId 
| String 
| No 
| last end ID （Pagination needs） 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/currentPlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{ "symbol": "TRXUSDT_SPBL", "pageSize":"20" }'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134581005,
  "data": {
    "nextFlag": false,
    "endId": 974792555020390400,
    "orderList": [
      {
        "orderId": "974792555020390400",
        "clientOid":"xxx001",
        "symbol": "TRXUSDT_SPBL",
        "size": "151",
        "executePrice": "0.041572",
        "triggerPrice": "0.041572",
        "status": "not_trigger",
        "orderType": "limit",
        "side": "buy",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "cTime": "1668134576563"
      }
    ]
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

| clientOid 
| Client Order ID 
 |

| symbol 
| Symbol ID 
 |

| size 
| Purchase quantity, base coin amount when orderType=limit, quote coin amount when orderType=market 
 |

| executePrice 
| Order execute price 
 |

| triggerPrice 
| Order   trigger price 
 |

| status 
| Order status 
 |

| orderType 
| Order type 
 |

| side 
| Buying direction 
 |

| triggerType 
| Order trigger type 
 |

| enterPointSource 
| enterPointSource 
 |

| cTime 
| Create time 
 |

| placeType 
| place type 
 |

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

### Get history plan orders

Rate Limit: 20 times/sec (uid)

HTTP Request

- POST /api/spot/v1/plan/historyPlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbol 
| String 
| Yes 
| Symbol ID 
 |

| pageSize 
| String 
| Yes 
| Page Size 
 |

| lastEndId 
| String 
| No 
| last end ID （Pagination needs） 
 |

| startTime 
| String 
| Yes 
| start time.   (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) 
 |

| endTime 
| String 
| Yes 
| end time 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/historyPlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{ "symbol": "TRXUSDT_SPBL", "pageSize":"20", "startTime":"1667889483000", "endTime":"1668134732000" }'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "nextFlag": false,
    "endId": 974792060738441216,
    "orderList": [
      {
        "orderId": "974792060738441216",
        "clientOid":"xxx001",
        "symbol": "TRXUSDT_SPBL",
        "size": "156",
        "executePrice": "0.041272",
        "triggerPrice": "0.041222",
        "status": "cancel",
        "orderType": "limit",
        "side": "buy",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "cTime": "1668134458717"
      }
    ]
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

| clientOid 
| Client Order ID 
 |

| symbol 
| Symbol ID 
 |

| size 
| Purchase quantity, base coin amount when orderType=limit, quote coin amount when orderType=market 
 |

| executePrice 
| Order execute price 
 |

| triggerPrice 
| Order   trigger price 
 |

| status 
| Order status 
 |

| orderType 
| Order type 
 |

| side 
| Buying direction 
 |

| triggerType 
| Order trigger type 
 |

| enterPointSource 
| enterPointSource 
 |

| cTime 
| Create time 
 |

| placeType 
| place type 
 |

 

 

 

 

### batch cancel plan orders

Rate Limit: 10 times/sec (uid)

HTTP Request

-  POST /api/spot/v1/plan/batchCancelPlan

Request Body

| 

| Parameter name 
| Parameter type 
| Required 
| Description 
 |

| symbols 
| List 
| No 
| symbols：["BTCUSDT_SPBL", "ETHUSDT_SPNL"], when symbols is empty, will cancel all spot plan open orders 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/plan/batchCancelPlan" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{ "symbols": ["BTCUSDT_SPBL", "ETHUSDT_SPNL"] }'

```

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683876261117,
  "data": [
    {
      "orderId": "10401817882538259200",
      "clientOid": "10408117882913093376",
      "result": true
    },
    {
      "orderId": "10401817887238259200",
      "clientOid": "10401817882213193376",
      "result": true
    }
  ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| spot plan order ID 
 |

| clientOid 
| spot plan order Client Order ID 
 |

| result 
| true is success 
 |

## P2P endpoint

### P2P merchant list

Limit rule 10 times/1s (uid)

HTTP Request

- GET /api/p2p/v1/merchant/merchantList

Request Parameter

| 

| Parameter Name 
| Parameter Type 
| Required 
| Description 
 |

| online 
| String 
| no 
| is online (yes/no) 
 |

| merchantId 
| String 
| no 
| merchant ID 
 |

| lastMinId 
| String 
| no 
| minId 
 |

| pageSize 
| String 
| no 
| Page Size(default 100) 
 |

Reversal Request Example

```
curl "https://api.bitget.com/api/p2p/v1/merchant/merchantList?online=yes&pageSize=20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Reversal Response Data

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681195810516,
  "data": {
    "resultList": [
      {
        "registerTime": "1678674575000",
        "nickName": "zed-test1",
        "isOnline": "no",
        "merchantId": "3784051421",
        "averagePayment": "3",
        "averageRelease": "2",
        "totalTrades": "23",
        "totalBuy": "10",
        "totalSell": "13",
        "totalCompletionRate": "0.9",
        "thirtyTrades": "8",
        "thirtySell": "4",
        "thirtyBuy": "4",
        "thirtyCompletionRate": "0.8"
      }
    ],
    "minId": "594"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| resultList 
| response array 
 |

| > registerTime 
| register time, ms 
 |

| > nickName 
| nick name 
 |

| > isOnline 
| is online, yes/no 
 |

| > merchantId 
| merchant ID 
 |

| > averagePayment 
| average payment time, min 
 |

| > averageRealese 
| average realese coin time, min 
 |

| > totalTrades 
| total No. of trades 
 |

| > totalBuy 
| total No. of buy 
 |

| > totalSell 
| total No. of sell 
 |

| > totalCompletionRate 
| total completion rate 
 |

| > thirtyTrades 
| thirty days total No. of trades 
 |

| > thirtySell 
| thirty days total No. of sell 
 |

| > thirtyBuy 
| thirty days total No. of buy 
 |

| > thirtyCompletionRate 
| thirty days total completion rate 
 |

| minId 
| response data minimum 'merchantId' in resultList 
 |

### get merchant information

Limit rule 10 times/1s (uid)

HTTP Request

- GET /api/p2p/v1/merchant/merchantInfo

Request Parameter

| 

| Parameter Name 
| Parameter Type 
| Required 
| Description 
 |

Reversal Request Example

```
curl "https://api.bitget.com/api/p2p/v1/merchant/merchantInfo" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Reversal Response Data

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681194805204,
  "data": {
    "registerTime": "1672039640000",
    "nickName": "Mark",
    "realName": "M***K",
    "merchantId": "2569373299",
    "averagePayment": "2",
    "averageRealese": "3",
    "totalTrades": "2",
    "totalBuy": "1",
    "totalSell": "0",
    "totalCompletionRate": "1",
    "thirtyTrades": "12",
    "thirtySell": "4",
    "thirtyBuy": "8",
    "thirtyCompletionRate": "0.71",
    "kycFlag": true,
    "emailBindFlag": true,
    "mobileBindFlag": true,
    "email": "****@gmail.com",
    "mobile": "107****434"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| registerTime 
| register time, ms 
 |

| nickName 
| nick name 
 |

| realName 
| kyc name 
 |

| merchantId 
| merchant ID 
 |

| kycFlag 
| is kyc: true/false 
 |

| emailBindFlag 
| is bind email: true/false 
 |

| mobileBindFlag 
| is bind mobile: true/false 
 |

| email 
| email 
 |

| mobile 
| mobile 
 |

| averagePayment 
| average payment time, min 
 |

| averageRealese 
| average realese coin time, min 
 |

| totalTrades 
| total No. of trade 
 |

| totalBuy 
| total No. of buy 
 |

| totalSell 
| total No. of sell 
 |

| totalCompletionRate 
| total completion rate 
 |

| thirtyTrades 
| thirty days total No. of trade 
 |

| thirtySell 
| thirty days total No. of sell 
 |

| thirtyBuy 
| thirty days total No. of buy 
 |

| thirtyCompletionRate 
| thirty days total completion rate 
 |

### get advertisement list

Limit rule 10 times/1s (uid)

HTTP Request

- GET /api/p2p/v1/merchant/advList

Request Parameter

| 

| Parameter Name 
| Parameter Type 
| Required 
| Description 
 |

| advNo 
| String 
| no 
| advertisement No 
 |

| type 
| String 
| no 
| buy/sell 
 |

| status 
| String 
| no 
| advertisement status 
 |

| languageType 
| String 
| no 
| zh-CN/en-US 
 |

| coin 
| String 
| no 
| coin 
 |

| fiat 
| String 
| no 
| fiat 
 |

| orderBy 
| String 
| no 
| order by desc：createTime/price (default createTime) 
 |

| payMethodId 
| String 
| no 
| advertisement payMethodId 
 |

| lastMinId 
| String 
| no 
| The minId returned by the previous query, will return records with advId less than the given 'lastMinId' 
 |

| startTime 
| String 
| yes 
| start time, ms 
 |

| endTime 
| String 
| no 
| end time, ms 
 |

| pageSize 
| String 
| no 
| page Size(default 100) 
 |

Reversal Request Example

```
curl "https://api.bitget.com/api/p2p/v1/merchant/advList?startTime=1659403328000&endTime=1659410528000&pageSize=20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Reversal Response Data

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681198612226,
  "data": {
    "advList": [
      {
        "advId": "100",
        "advNo": "1012099637487755264",
        "type": "buy",
        "amount": "100",
        "dealAmount": "0",
        "coin": "USDT",
        "price": "1",
        "coinPrecision": "4",
        "fiatCode": "USD",
        "fiatPrecision": "2",
        "fiatSymbol": "$",
        "status": "online",
        "hide": "no",
        "maxAmount": "100",
        "minAmount": "10",
        "payDuration": "5",
        "turnoverNum": "1",
        "turnoverRate": "1.00",
        "remark": null,
        "userLimit": {
          "minCompleteNum": "10",
          "maxCompleteNum": "0",
          "placeOrderNum": "0",
          "allowMerchantPlace": "no",
          "thirtyCompleteRate": "0",
          "country": ""
        },
        "paymentMethod": [
          {
            "paymentMethod": "",
            "paymentId": "3",
            "paymentInfo": [
              {
                "name": "",
                "required": true,
                "type": "number"
              },
              {
                "name": "",
                "required": true,
                "type": "file"
              }
            ]
          }
        ],
        "ctime": "1677029278156"
      }
    ],
    "minId": "100"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| advList 
| response array 
 |

| > advId 
| ID 
 |

| > advNo 
| advertisement No 
 |

| > type 
| sell/buy 
 |

| > amount 
| advertisement buy/sell amount 
 |

| > dealAmount 
| deal amount 
 |

| > coin 
| buy/sell coin (BGB,USDT,BTC,ETH) 
 |

| > price 
| payment fiat (USD, JPY, CNY) 
 |

| > coinPrecision 
| coin precision 
 |

| > fiatCode 
| fiat code 
 |

| > fiatPrecision 
| fiat precision 
 |

| > fiatSymbol 
| fiat symbol 
 |

| > status 
| advertisement status 
 |

| > hide 
| advertisement hide: yes/no 
 |

| > maxAmount 
| Maximum Order Quantity 
 |

| > minAmount 
| Minimum Order Quantity 
 |

| > payDuration 
| order payment duration, min 
 |

| > turnoverNum 
| merchant total trade Number 
 |

| > turnoverRate 
| merchant total trade completion 
 |

| > remark 
| remark 
 |

| > ctime 
| create time, ms 
 |

| > userLimit 
| user place order limit 
 |

| >> minCompleteNum 
| user minimum completion orders 
 |

| >> maxCompleteNum 
| user maximum completion orders 
 |

| >> placeOrderNum 
| user maximum place orders in this advertisement 
 |

| >> allowMerchantPlace 
| allow merchant place order: yes/no 
 |

| >> thirtyCompleteRate 
| thirty days completion rate 
 |

| > paymentMethod 
| payment method 
 |

| >> paymentMethod 
| payment method name 
 |

| >> paymentId 
| payment id 
 |

| >> paymentInfo 
| payment information 
 |

| >>> required 
| required: true/false 
 |

| >>> name 
| pay detail description 
 |

| >>> type 
| pay detail type, file/number, please ignore this field 
 |

| > merchantCertifiedResult 
| merchant certified 
 |

| >> imageUrl 
| merchant certified image 
 |

| >> desc 
| merchant certified desc 
 |

| minId 
| response data minimum 'advId' 
 |

### merchant get P2P order list

Limit rule 10 times/1s (uid)

HTTP Request

- GET /api/p2p/v1/merchant/orderList

Request Parameter

| 

| Parameter Name 
| Parameter Type 
| Required 
| Description 
 |

| advNo 
| String 
| Yes 
| advertisement No 
 |

| type 
| String 
| No 
| buy/sell 
 |

| orderNo 
| String 
| No 
| order No 
 |

| status 
| String 
| No 
| p2p order status 
 |

| languageType 
| String 
| Yes 
| zh-CN/en-US 
 |

| coin 
| String 
| No 
| coin 
 |

| fiat 
| String 
| No 
| fiat 
 |

| lastMinId 
| String 
| No 
| The minId returned by the previous query, will return records with advNo less than the given 'lastMinId' 
 |

| startTime 
| String 
| Yes 
| start time, ms 
 |

| endTime 
| String 
| No 
| end time, ms 
 |

| pageSize 
| String 
| No 
| page size(default 100) 
 |

Reversal Request Example

```
curl "https://api.bitget.com/api/p2p/v1/merchant/orderList?startTime=1659403328000&endTime=1659410528000&pageSize=20" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json"

```

Reversal Response Data

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1681201761390,
  "data": {
    "orderList": [
      {
        "orderId": "557",
        "orderNo": "1029222647482966017",
        "advNo": "1027001359783845889",
        "price": "1",
        "count": "11",
        "type": "buy",
        "fiat": "USD",
        "coin": "USDT",
        "withdrawTime": "",
        "representTime": "",
        "paymentTime": "",
        "releaseCoinTime": "",
        "amount": "11",
        "buyerRealName": "Jordan",
        "sellerRealName": "Mark",
        "status": "cancelled",
        "paymentInfo": {
          "paymethodName": "paypal",
          "paymethodId": "3",
          "paymethodInfo": [
            {
              "name": "IBC",
              "required": true,
              "type": "number",
              "value": "11****"
            },
            {
              "name": "Paypal",
              "required": true,
              "type": "file",
              "value": "http://bitgetapp.com/otc/images/20230116/498ab1b8-3ba6-44bd-9570-b3e5c118233f.jpg"
            }
          ]
        },
        "ctime": "1681111722251"
      }
    ],
    "minId": "557"
  }
}

```

Response Description

| 

| Parameter 
| Description 
 |

| orderList 
| response array 
 |

| > orderId 
| ID 
 |

| > orderNo 
| order No 
 |

| > advNo 
| advertisement No 
 |

| > type 
| buy/sell 
 |

| > count 
| order coin amount 
 |

| > coin 
| coin 
 |

| > price 
| price 
 |

| > fiat 
| fiat 
 |

| > withdrawTime 
| withdraw time 
 |

| > representTime 
| order appeal time 
 |

| > releaseCoinTime 
| release coin time 
 |

| > paymentTime 
| payment time 
 |

| > amount 
| order fiat amount 
 |

| > status 
| p2p order status 
 |

| > buyerRealName 
| buyer kyc name 
 |

| > sellerRealName 
| seller kyc name 
 |

| > ctime 
| create time 
 |

| > paymentInfo 
| payment information 
 |

| >> paymethodName 
| pay method name 
 |

| >> paymethodId 
| pay method ID 
 |

| >> paymethodInfo 
| pay method information 
 |

| >>> name 
| name 
 |

| >>> required 
| required: true/false 
 |

| >>> type 
| type, number/file, please ignore this field 
 |

| >>> value 
| value 
 |

| minId 
| response data minimum 'orderId' 
 |

 

## Sub-Account Endpoints

- The endpoints documented in this section are for Main-Account, and only allowed to create/modify virtual sub-accounts 

- The master account ApiKey needs to be bound to the ip whitelist

### Create Virtual Sub Account

Limit Rule：5c/1s  (uid)

HTTP Request

- POST  /api/user/v1/sub/virtual-create

Request Pam

| 

| Parameter Name 
| Type 
| Required 
| Description 
 |

| subName 
| List 
| Yes 
| Virtual nickname English letters with a length of 8 characters 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/user/v1/sub/virtual-create" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"subName": ["bitgeton"]}'

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1682660169412,
    "data": {
        "failAccounts": [
            "guningfh@virtual-bitget.com"
        ],
        "successAccounts": [
            {
                "subUid": "9837924274",
                "subName": "guningfk@virtual-bitget.com",
                "status": "normal",
                "auth": [
                    "contract_trade",
                    "spot_trade"
                ],
                "remark": null,
                "cTime": "1682660169573"
            }
        ]
    }
}

```

Response

| 

| Parameter 
| Description 
 |

| subUid 
| virtual sub uid 
 |

| subName 
| Virtual Email 
 |

| status 
| virtual account status 
 |

| auth 
| Virtual auth 
 |

| remark 
| account label 
 |

| cTime 
| Create time timestamp 
 |

- status

normal 

- freeze 

- auth

readonly

- spot_trade 

- contract_trade 

- failAccounts   create fail accounts

subName is duplicated

- The number of created sub-accounts has reached the limit

### Modify Virtual Account

Limit Rule：5c/1s (uid)

HTTP Request

- POST /api/user/v1/sub/virtual-modify

Request (Request Body)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| subUid 
| String 
| Yes 
| virtual sub uid 
 |

| perm 
| String 
| Yes 
| Perm  , 
 |

| status 
| String 
| Yes 
| Virtual account status 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/user/v1/sub/virtual-modify" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"subUid": "9837924274","perm":"spot_trade,contract_trade", "status":"normal"}'

```

Response 

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1682660666458,
    "data": "success"
}

```

- status

normal 

- freeze 

- auth

spot_trade 

- readonly

- contract_trade 

### Batch Create Virtual Account And ApiKey

This interface can create a virtual sub-account and a sub-account apikey together. The created virtual sub-account has contract and spot permissions by default.

Limit Rule：1c/1s (uid)

HTTP Request

- POST /api/user/v1/sub/virtual-api-batch-create

Request (Request Body)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| List 
| List 
|  
|  
 |

| -- subName 
| String 
| Yes 
| Virtual nickname (letters with a length of 8 characters) 
 |

| -- passphrase 
| String 
| Yes 
| Password (Password length is 8~32 letters + numbers) case sensitive 
 |

| -- label 
| String 
| Yes 
| label limit 20 
 |

| -- ip 
| String 
| No 
| Virtual sub-account ApiKey ip whitelist 
 |

| -- perm 
| String 
| No 
| Sub-account apiKey permissions 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/user/v1/sub/virtual-api-batch-create" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"list":[{"subName":"armendon","passphrase":"1r1b6uX6PQ9tbKwa","perm":"spot_trade,contract_trade","label":"1681808312065"}]}'

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1682662465346,
    "data": {
        "list": [
            {
                "subUid": "4236327146",
                "subName": "armendon@virtual-bitget.com",
                "label": "1681808312065",
                "apiKey": "bg_d32ff9d9**********c3d2bc5e23",
                "secretKey": "af22848395e3d97e08dbd9a876a1XXXXXXXXXXXXXXX",
                "perm": "readonly,spot_trade,contract_trade",
                "ip": ""
            }
        ]
    }
}

```

- status

normal 

- freeze 

- auth

spot_trade 

- contract_trade 

- readonly 

### Get Virtual Account List

Limit Rule：10c/1s (uid)

HTTP Request

- GET  /api/user/v1/sub/virtual-list

Request (Request Param)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| pageSize 
| String 
| No 
| Default20 Max100 
 |

| pageNo 
| String 
| No 
| PageNo Default  1 
 |

| status 
| String 
| No 
| virtual status 
 |

Request Example

```
curl "https://api.bitget.com/api/user/v1/sub/virtual-list" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \

```

Response 

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1656589586807,
    "data": {
        "hasNextPage": false,
        "lastEndId": 51,
        "list": [
            {
                "subUid": "7713789662",
                "subName": "mySub01@bgbroker6314497154",
                "status": "normal",
                "auth": [
                    "readonly",
                    "spot_trade",
                    "contract_trade"
                ],
                "remark": "mySub01",
                "cTime": "1653287983475"
            }
        ]
    }
}

```

- status

normal 

- freeze 

- auth

spot_trade 

- contract_trade 

- readonly

### Create Virtual Account ApiKey

Limit Rule：5c/1s (uid)

HTTP Request

- POST /api/user/v1/sub/virtual-api-create

Request (Request Body)

| 

| Paarameter 
| Type 
| Required 
| Description 
 |

| subUid 
| String 
| Yes 
| virtual sub uid 
 |

| passphrase 
| String 
| Yes 
| Password (Password length is 8~32 letters + numbers) case sensitive 
 |

| label 
| String 
| Yes 
| label 
 |

| ip 
| String 
| No 
| ip，Max 30 
 |

| perm 
| String 
| No 
| perm，default readonly 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/user/v1/sub/virtual-api-create" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"subUid":"983792","passphrase":"1r1b6usadasdasd","label":"1682396356594","perm":"spot_trade"}'

```

Response 

```
{
  "code": "00000",
  "msg": "success",
  "data": [
    {
      "subUid": "58281113",
      "label": "sub api",
      "apiKey": "bg_djwwwls98a1s0dLK3deq2",
      "secretKey": "Sjwwwls98a1s0dLK3deq2",
      "perm": "spot_trade,contract_trade",
      "ip": "127.127.127.127"
    }
  ]
}

```

Response

| 

| Paarameter 
| Description 
 |

| subUid 
| Sub uid 
 |

| label 
| sub apikey label 
 |

| apikey 
| apikey 
 |

| secretKey 
| sub apikey secretKey 
 |

| perm 
| Perm 
 |

| ip 
| subApiKey ip whileList 
 |

- perm

spot_trade

- contract_trade

- readonly

### Modify Virtual Account ApiKey

Limit Rule：5c/1s (uid)

HTTP Request

- POST /api/user/v1/sub/virtual-api-modify

Request (Request Body)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| subUid 
| String 
| Yes 
| sub account uid 
 |

| subApiKey 
| String 
| Yes 
| sub account apikey 
 |

| passphrase 
| String 
| Yes 
| subApiKey passphrase 
 |

| label 
| String 
| Yes 
| Sub Apikey label 
 |

| ip 
| String 
| No 
| Will overwrite the previous ip information(If no ip is passed, the whitelist is set to empty)  Max 30 
 |

| perm 
| String 
| No 
| perm 
 |

Request Example

```
curl -X POST "https://api.bitget.com/api/user/v1/sub/virtual-api-modify" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"subUid":"983792","subApiKey":"bg_ab5735b8a90f2d4","passphrase":"1r1b6usadasdasd","label":"1682396356594","perm":"spot_trade"}'

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1682661350849,
    "data": {
        "subUid": "9837924274",
        "label": "1682396356594",
        "apiKey": "bg_19aab20aafdb177408faf3fba6580656",
        "perm": "spot_trade",
        "ip": ""
    }
}

```

Response

| 

| Parameter 
| Desciption 
 |

| subUid 
| Sub uid 
 |

| label 
| apikey lable 
 |

| apikey 
| sub apikey 
 |

| perm 
| perm 
 |

| ip 
| sub apikey ip whitelist 
 |

- perm

spot_trade

- contract_trade

- readonly

### Get Virtual Sub  ApiKey List

Limit Rule：10c/1s (uid)

HTTP Request

- GET /api/user/v1/sub/virtual-api-list

Request

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| subUid 
| String 
| Yes 
| Sub uid 
 |

Request Example

```
curl "https://api.bitget.com/api/user/v1/sub/virtual-api-list?subUid=1111111" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \

```

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1682661432874,
    "data": [
        {
            "subUid": "9837924274",
            "label": "1682396356594",
            "apiKey": "bg_ab5735b8a90f2d4c02771b36e8dbebf4",
            "perm": "spot_trade",
            "ip": ""
        }
    ]
}

```

Response

| 

| Parameter 
| Desciption 
 |

| subUid 
| Sub virtual Uid 
 |

| label 
| Apikey label 
 |

| apikey 
| sub apikey 
 |

| perm 
| Perm 
 |

| ip 
| sub ApiKey  ip whilelist 
 |

## Convert

### Get Convert Coins

Limit Rule: 10c/1s (uid)

HTTP Request

- GET /api/spot/v1/convert/currencies

RequestParameter(Request Param)

Request Example

```
curl "https://api.bitget.com/api/spot/v1/convert/currencies" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \

```

Response

```
{
  "code": "00000",
  "data": [
    {
      "coin": "ETH",
      "available": "0.9994",
      "maxCcy": "5",
      "minCcy": "0.0005"
    }
  ],
  "msg": "success",
  "requestTime": 1627293612502
}

```

Response

| 

| Parameter 
| Description 
 |

| coin 
| coin name 
 |

| available 
| account available 
 |

| maxCcy 
| Max convert, When used as fromCoin, it represents the maximum amount that can be consumed, and when used as toCoin, it represents the maximum amount that can be obtained 
 |

| minCcy 
| Min convert, When used as fromCoin, it represents the minimum amount that can be consumed. When used as toCoin, it represents the minimum amount of convert. 
 |

### Get Quoted Price

Get the quote price and request the convert interface within 8 seconds, and it cannot be converted if it expires

Get a quote of the toCoin amount when the fromCoin amount is consumed

Get a quote of the consumed amount of fromCoin when getting the amount of toCoin

need `trade` or `spot_trade`

Limit Rule: 5c/1s (uid)  

HTTP Request

- POST  /api/spot/v1/convert/quoted-price

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| fromCoin 
| String 
| Yes 
| consumption coin 
 |

| fromCoinSz 
| String 
| No 
| Consumption size  (fromCoinSz and toCoinSz Only one is allowed to be passed in once) 
 |

| toCoin 
| String 
| Yes 
| Goal Coin 
 |

| toCoinSz 
| String 
| No 
| size of Goal Coin (fromCoinSz and toCoinSz Only one is allowed to be passed in once) 
 |

RequestParameter(Request Param)

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/convert/quotedPrice" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"fromCoin": "USDT","fromCoinSz":"444","toCoin":"ETH"}'

```

Response

```
{
  "code": "00000",
  "data": {
    "fee": "0",
    "fromCoinSz": "444",
    "fromCoin": "USDT",
    "cnvtPx": "0.0005226794534969",
    "toCoinSz": "0.23206967",
    "toCoin": "ETH",
    "traceId": "1060321041546502144"
  },
  "msg": "success",
  "requestTime": 1627293612502
}

```

| 

| Parameter 
| Description 
 |

| fromCoin 
| Consumption coin name 
 |

| fromCoinSz 
| Consumption coin size 
 |

| cnvtPx 
| convert price 
 |

| toCoin 
| Goal Coin name 
 |

| toCoinSz 
| size of Goal Coin 
 |

| traceId 
| trace Id 
 |

| fee 
| convert fee 
 |

### Convert

need `trade` or `spot_trade`

Limit Rule: 5c/1s (uid) 

HTTP Request

- POST  /api/spot/v1/convert/trade

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| fromCoin 
| String 
| Yes 
| Consumption Coin      eg USDT 
 |

| fromCoinSz 
| String 
| Yes 
| Consumption Coin size 
 |

| cnvtPx 
| String 
| Yes 
| convert price  `/quotedPrice`  `cnvtPx` 
 |

| toCoin 
| String 
| Yes 
| Goal Coin eg BGB 
 |

| toCoinSz 
| String 
| Yes 
| size of Goal Coin `/quotedPrice`  `toCoinSz` 
 |

| traceId 
| String 
| Yes 
| trace Id     `/quotedPrice`  `traceId`  8 seconds expires 
 |

RequestParameter(Request Param)

Request Example

```
curl -X POST "https://api.bitget.com/api/spot/v1/convert/trade" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
  -d \'{"fromCoin": "USDT","fromCoinSz":"444","toCoin":"ETH","cnvtPx":"0.0005226794534969","toCoinSz":"0.23206967","traceId":"1060321041546502144"}'

```

Response

```
{
  "code": "00000",
  "data": {
    "timestamp": "1688527221603",
    "cnvtPx": "0.00052268",
    "toCoinSz": "0.23206967",
    "toCoin": "ETH"
  },
  "msg": "success",
  "requestTime": 1627293612502
}

```

| 

| Parameter 
| Description 
 |

| toCoin 
| Goal coin name 
 |

| toCoinSz 
| size of Goal Coin 
 |

| cnvtPx 
| convert price 
 |

| timestamp 
| get quote price 
 |

### Convert History

Limit Rule: 10c/1s (uid)

HTTP Request

- GET  /api/spot/v1/convert/convert-record

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| startTime 
| String 
| Yes 
| start time (ms timestamp) 
 |

| endTime 
| String 
| Yes 
| end time (timestamp ms) Maximum difference 90 days 
 |

| pageSize 
| String 
| No 
| default 20  max 100 
 |

| lastEndId 
| String 
| No 
| last endId 
 |

RequestParameter(Request Param)

Request Example

```
curl "https://api.bitget.com/api/spot/v1/account/convert-record?startTime=1686128558000&endTime=1686214958000&pageSize=10" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \

```

Response

```
{
  "code": "00000",
  "data": {
    "dataList": [
      {
        "id": "1060326726652944385",
        "timestamp": "1688527512229",
        "cnvtPx": "0.00052268",
        "fee": "0",
        "fromCoinSz": "444",
        "fromCoin": "USDT",
        "toCoinSz": "0.23206967",
        "toCoin": "ETH"
      }
    ],
    "endId": "1060325507679150080"
  },
  "msg": "success",
  "requestTime": 1627293612502
}

```

| 

| Parameter 
| Description 
 |

| dataList 
| List 
 |

| -- id 
| record Id 
 |

| -- timestamp 
| Convert trade time, Unix timestamp format in milliseconds, e.g. 1597026383085 
 |

| -- cnvtPx 
| convert price 
 |

| -- fee 
| convert fee 
 |

| -- fromCoinSz 
| Consumption Coin size 
 |

| -- fromCoin 
| Consumption Coin name 
 |

| -- toCoinSz 
| size of Goal Coin 
 |

| -- toCoin 
| Goal Coin name 
 |

| endId 
| last end id 
 |

## Tax

### Spot Account Record

It is recommended that APIKey  onlyn check the tax permission 

limit rule:  1c/1s (uid)

*HTTP Request *

- GET /api/user/v1/tax/spot-record

Request Parameter(Request Param)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| default all coin 
 |

| startTime 
| String 
| Yes 
| start time(timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end time (timestamp ms) and   startTime Maximum range 366 days 
 |

| pageSize 
| String 
| No 
| default500 Max500 
 |

| lastEndId 
| String 
| No 
| last data id 
 |

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
      "id": "1050266154437103616",
      "coin": "AIBB",
      "type": "Interest",
      "amount": "6018333.33333333",
      "fee": "0",
      "total": "468575833.33333306",
      "timestamp": "1686128884851"
    }
  ]
}

```

Response Description

| 

| Parameter 
| Description 
 |

| id 
| record id  lastEndId 
 |

| coin 
| coin name 
 |

| type 
| biz type spot 
 |

| amount 
| account change 
 |

| fee 
| fee 
 |

| total 
| account total 
 |

| timestamp 
| record create time (timestamp ms) 
 |

### Future Account Record

It is recommended that APIKey  onlyn check the tax permission 

limit rule:  1c/1s (uid)

HTTP Request

- GET /api/user/v1/tax/future-record

Request Parameter(Request Param)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| productType 
| String 
| No 
| default USDT future 
 |

| marginCoin 
| String 
| No 
| default all marginCoin 
 |

| startTime 
| String 
| Yes 
| start time(timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end time (timestamp ms) and   startTime Maximum range 366 days 
 |

| pageSize 
| String 
| No 
| default500 Max500 
 |

| lastEndId 
| String 
| No 
| last data id 
 |

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
            "id": "1024179365593391107",
            "symbol": "TRXUSDT_UMCBL",
            "marginCoin": "USDT",
            "type": "close_long",
            "amount": "0.10545",
            "fee": "-0.02134863",
            "timestamp": "1679909309766"
        }
  ]
}

```

Response Description

| 

| Parameter 
| Description 
 |

| id 
| record id  lastEndId 
 |

| coin 
| Coin name 
 |

| type 
| biz type future 
 |

| amount 
| account change 
 |

| fee 
| fee 
 |

| timestamp 
| record create time (timestamp ms) 
 |

### Margin Account Record

It is recommended that APIKey  onlyn check the tax permission 

limit rule:  1c/1s (uid)

HTTP Request

- GET /api/user/v1/tax/margin-record

Request Parameter(Request Param)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| marginType 
| String 
| No 
| MarginType isolated/crossed 
 |

| coin 
| String 
| No 
| default all coin 
 |

| startTime 
| String 
| Yes 
| start time(timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end time (timestamp ms) and   startTime Maximum range 366 days 
 |

| pageSize 
| String 
| No 
| default500 Max500 
 |

| lastEndId 
| String 
| No 
| last data id 
 |

Response

```
{
    "code": "00000",
    "msg": "success",
    "requestTime": 1687259242290,
    "data": [
        {
            "id": "1050267830387408896",
            "symbol": null,
            "coin": "USDT",
            "type": "transfer_in",
            "amount": "13333",
            "fee": "0",
            "total": "13333",
            "timestamp": "1686129284474"
        }
    ]
}

```

Response Description

| 

| Parameter 
| Description 
 |

| id 
| record id  lastEndId 
 |

| coin 
| coin name 
 |

| type 
| biz type margin 
 |

| amount 
| Account change 
 |

| fee 
| fee 
 |

| total 
| account total 
 |

| timestamp 
| record create time (timestamp ms) 
 |

### P2P Account Record

It is recommended that APIKey  onlyn check the tax permission 

limit rule:  1c/1s (uid)

HTTP Request

- GET /api/user/v1/tax/p2p-record

Request Parameter(Request Param)

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| coin 
| String 
| No 
| default all coin 
 |

| startTime 
| String 
| Yes 
| start time(timestamp ms) 
 |

| endTime 
| String 
| Yes 
| end time (timestamp ms) and   startTime Maximum range 366 days 
 |

| pageSize 
| String 
| No 
| default500 Max500 
 |

| lastEndId 
| String 
| No 
| last data id 
 |

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687260620793,
  "data": [
    {
      "id": "1752117",
      "coin": "USDT",
      "type": "BUY",
      "total": "10",
      "timestamp": "1680582050393"
    }
  ]
}

```

Response Description

| 

| Parameter 
| Description 
 |

| id 
| record id  lastEndId 
 |

| coin 
| coin name 
 |

| type 
| biz type p2p 
 |

| total 
| account total 
 |

| timestamp 
| record create time (timestamp ms) 
 |

 

 

 

 

 

 

 

 

 

## Loans

### Query currency data list

Rate Limit: 10 times/1s (IP)

HTTP Request

- GET /api/spot/v1/public/loan/coinInfos

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/loan/coinInfos" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| coin 
| String 
| no 
| coin 
 |

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433281223,
  "data": {
    "loanInfos": [
      {
        "coin": "USDT",
        "hourRate7D": "0.00000617",
        "rate7D": "0.054",
        "hourRate30D": "0.00000879",
        "rate30D": "0.077",
        "minUsdt": "200",
        "maxUsdt": "1000000",
        "min": "200",
        "max": "1000000"
      }
  ],
  "pledgeInfos": [
    {
      "coin": "MATIC",
      "initRate": "0.6",
      "supRate": "0.75",
      "forceRate": "0.83",
      "minUsdt": "0",
      "maxUsdt": "200000"
    }
  ]
  } 
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanInfos 
| Loan infos 
 |

| >coin 
| Loan coin 
 |

| >hourRate7D 
| 7 days fixed rate per hour percentage 
 |

| >rate7D 
| 7-day fixed rate annualized percentage 
 |

| >hourRate30D 
| 30-day fixed rate hourly percentage 
 |

| >rate30D 
| 30-day fixed rate annualized percentage 
 |

| >minUsdt 
| Minimum Borrowable limit usdt 
 |

| >maxUsdt 
| Maximum borrowing limit usdt 
 |

| >min 
| Minimum borrowing limit 
 |

| >max 
| Maximum borrowing limit 
 |

| pledgeInfos 
| Pledge infos 
 |

| >coin 
| Pledge coin 
 |

| >initRate 
| Initial pledge rate percentage 
 |

| >supRate 
| Percentage of supplementary guarantee pledge rate 
 |

| >forceRate 
| Forced Liquidation Pledge Rate Percentage 
 |

| >minUsdt 
| Minimum pledge limit usdt 
 |

| >maxUsdt 
| Maximum pledge limit usdt 
 |

 

 

 

 

 

 

 

 

 

 

### Query hourly estimated interest and loan amount

Rate Limit: 10 times/1s (IP)

HTTP Request

- GET /api/spot/v1/public/loan/hour-interest

Request Example

```
curl "https://api.bitget.com/api/spot/v1/public/loan/hour-interest?loanCoin=USDT&pledgeCoin=ETH&pledgeAmount=0.2&daily=SEVEN" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| loanCoin 
| String 
| yes 
| Loan coin 
 |

| pledgeCoin 
| String 
| yes 
| Pledge coin 
 |

| daily 
| String 
| yes 
| Pledge days 
 |

| pledgeAmount 
| String 
| no 
| Pledge amount 
 |

- daily

SEVEN       7 days

- THIRTY    30 days

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692433739845,
  "data": {
    "hourInterest": "0.00133436",
    "loanAmount": "216.2654"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| hourInterest 
| Estimated interest amount per hour 
 |

| loanAmount 
| Borrowable amount 
 |

 

 

 

 

 

 

 

 

 

 

### Borrow coin

Rate Limit: 10 times/1s (UID)

HTTP Request

- POST /api/spot/v1/loan/borrow

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/borrow" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
 -d \'{
    "loanCoin":"ETH",
    "pledgeCoin":"USDT",
    "daily":"SEVEN",
    "loanAmount":"0.01"
}'

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| loanCoin 
| String 
| yes 
| Loan coin 
 |

| pledgeCoin 
| String 
| yes 
| Pledge coin 
 |

| daily 
| String 
| yes 
| Pledge days 
 |

| pledgeAmount 
| String 
| no 
| Pledge amount 
 |

| loanAmount 
| String 
| no 
| Loan amount  pledgeAmount and loanAmount must send one 
 |

- daily

SEVEN       7 days

- THIRTY    30 days

Response

```
{
  "code":"00000",
  "msg":"success",
  "requestTime":163123213132,
  "data": {
    "orderId": "1076713704374022144"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

 

 

 

 

 

 

 

 

 

 

### Query the list of loan orders

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/ongoing-orders

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/ongoing-orders?orderId=1076713704374022144" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| no 
| Order ID 
 |

| loanCoin 
| String 
| no 
| Loan coin 
 |

| pledgeCoin 
| String 
| no 
| Pledge coin 
 |

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692434611622,
  "data": [
    {
      "orderId": "1076713704374022144",
      "loanCoin": "ETH",
      "loanAmount": "1",
      "interestAmount": "0.00000229",
      "hourInterestRate": "0.000229",
      "pledgeCoin": "USDT",
      "pledgeAmount": "2619.69231032",
      "pledgeRate": "65",
      "supRate": "75",
      "forceRate": "83",
      "borrowTime": "1692434472156",
      "expireTime": "1693036799999"
    }
  ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

| loanCoin 
| Loan coin 
 |

| loanAmount 
| Loan amount 
 |

| interestAmount 
| Interest amount 
 |

| hourInterestRate 
| Hour interest rate 
 |

| pledgeCoin 
| Pledge coin 
 |

| pledgeAmount 
| Pledge amount 
 |

| pledgeRate 
| Pledge rate 
 |

| supRate 
| Supplementary rate 
 |

| forceRate 
| Forced Liquidation Pledge Rate Percentage 
 |

| borrowTime 
| Borrow time  millseconds 
 |

| expireTime 
| Expire time millseconds 
 |

 

 

 

 

 

 

 

 

 

 

### Repay Loan Orders

Rate Limit: 10 times/1s (UID)

HTTP Request

- POST /api/spot/v1/loan/repay

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/repay" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
 -d \'{
    "orderId":"ETH",
    "repayAll":"yes",
    "repayUnlock":"yes"
}'

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| yes 
| Order ID 
 |

| amount 
| String 
| no 
| Repay amount 
 |

| repayUnlock 
| String 
| no 
| Repay unlock, default value: yes 
 |

| repayAll 
| String 
| yes 
| Repay all 
 |

- repayUnlock

yes       yes

- no        no

- repayAll

yes       yes

- no        no

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "repayAmount": "1566.23820848",
    "payInterest": "0.1185634",
    "repayLoanAmount": "1566.22635214",
    "repayUnlockAmount": "195"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanCoin 
| Loan coin 
 |

| pledgeCoin 
| Pledge coin 
 |

| repayAmount 
| Repay amount 
 |

| payInterest 
| payment interest 
 |

| repayLoanAmount 
| Repay loan amount 
 |

| repayUnlockAmount 
| Pledge currency releases the amount of collateral 
 |

 

 

 

 

 

 

 

 

 

 

### Query the repayment history list

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/repay-history

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/repay-history?startTime=1685957902000&endTime=1691228302423" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| no 
| Order ID 
 |

| loanCoin 
| String 
| no 
| Loan coin 
 |

| pledgeCoin 
| String 
| no 
| Pledge coin 
 |

| startTime 
| String 
| yes 
| Start time, only supports querying the data of the past three months 
 |

| endTime 
| String 
| yes 
| End time 
 |

| pageNo 
| String 
| no 
| pageNo default 1 
 |

| pageSize 
| String 
| no 
| pageSize  default 10，max 100 
 |

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [{
    "orderId": "1278182632",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "repayAmount": "1566.23820848",
    "payInterest": "0.1185634",
    "repayLoanAmount": "1566.22635214",
    "repayUnlockAmount": "195",
    "repayTime": "1684747525424"
  }, {
    "orderId": "1278182633",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "repayAmount": "1566.23820848",
    "payInterest": "0.1185634",
    "repayLoanAmount": "1566.22635214",
    "repayUnlockAmount": "195",
    "repayTime": "1684747525424"
  }]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order id 
 |

| loanCoin 
| Loan coin 
 |

| loanAmount 
| Pledge coin 
 |

| repayAmount 
| Repay amount 
 |

| payInterest 
| Payment interest 
 |

| repayLoanAmount 
| Loan Currency Repayment of Principal Amount 
 |

| repayUnlockAmount 
| Pledge currency releases the amount of collateral 
 |

| repayTime 
| Repayment time 
 |

 

 

 

 

 

 

 

 

 

 

### Adjust pledge rate

Rate Limit: 10 times/1s (UID)

HTTP Request

- POST /api/spot/v1/loan/revise-pledge

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/revise-pledge" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" \
 -d \'{
    "orderId":"1278182633",
    "pledgeCoin":"USDT",
    "reviseType":"OUT",
    "amount":"1"
}'

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| yes 
| Order ID 
 |

| amount 
| String 
| yes 
| Repay amount 
 |

| pledgeCoin 
| String 
| yes 
| Pledge coin 
 |

| reviseType 
| String 
| yes 
| Repay Type 
 |

- reviseType

OUT   Withdraw collateral

- IN   supplementary collateral

Response

```
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": {
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "afterPledgeRate": "60.5"
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanCoin 
| Loan coin 
 |

| pledgeCoin 
| Pledge coin 
 |

| afterPledgeRate 
| Adjusted Pledge Rate Percentage 
 |

 

 

 

 

 

 

 

 

 

 

### Query the historical list of adjusted pledge ratios

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/revise-history

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/revise-history?startTime=1691119224000&endTime=1692436119603" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| no 
| Order ID 
 |

| reviseSide 
| String 
| no 
| Revise side 
 |

| pledgeCoin 
| String 
| no 
| Pledge coin 
 |

| startTime 
| String 
| yes 
| Start time, only supports querying the data of the past three months 
 |

| endTime 
| String 
| yes 
| End time 
 |

| pageNo 
| String 
| no 
| pageNo default 1 
 |

| pageSize 
| String 
| no 
| pageSize  default 10，max 100 
 |

- reviseSide

down   turn down

- up   turn up

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436125845,
  "data": [
    {
      "loanCoin": "ETH",
      "pledgeCoin": "USDT",
      "orderId": "1076713704374022144",
      "reviseTime": "1692436102448",
      "reviseSide": "down",
      "reviseAmount": "10",
      "afterPledgeRate": "64.75",
      "beforePledgeRate": "65"
    }
  ]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanCoin 
| Loan coin 
 |

| pledgeCoin 
| Pledge coin 
 |

| orderId 
| Order ID 
 |

| reviseTime 
| Adjust time 
 |

| reviseSide 
| Adjust direction 
 |

| reviseAmount 
| Adjustment quantity 
 |

| afterPledgeRate 
| Adjusted Pledge Rate Percentage 
 |

| beforePledgeRate 
| Pledge rate percentage before adjustment 
 |

 

 

 

 

 

 

 

 

 

 

### Query loan history list

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/borrow-history

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/borrow-history?startTime=1691119224000&endTime=1692436119603" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| no 
| Order ID 
 |

| loanCoin 
| String 
| no 
| Loan coin 
 |

| pledgeCoin 
| String 
| no 
| Pledge coin 
 |

| status 
| String 
| no 
| Status 
 |

| startTime 
| String 
| yes 
| Start time, only supports querying the data of the past three months 
 |

| endTime 
| String 
| yes 
| End time 
 |

| pageNo 
| String 
| no 
| pageNo default 1 
 |

| pageSize 
| String 
| no 
| pageSize  default 10，amx 100 
 |

- status

rollback failure

- force liquidation

- repay already repaid

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [{
    "orderId": "1278182632",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "initPledgeAmount": "0.757",
    "initLoanAmount": "4321321.23820848",
    "hourRate": "59.1",
    "daily": "7",
    "borrowTime": "1684747528424",
    "status": "REPAY"
  }, {
    "orderId": "1278182633",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "initPledgeAmount": "0.757",
    "initLoanAmount": "4321321.23820848",
    "hourRate": "59.1",
    "daily": "7",
    "borrowTime": "1684747528424",
    "status": "REPAY"
  }]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanCoin 
| Loan coin 
 |

| pledgeCoin 
| Pledge coin 
 |

| orderId 
| Order ID 
 |

| initPledgeAmount 
| Initialize the pledge amount 
 |

| initLoanAmount 
| Initialize the loan amount 
 |

| hourRate 
| hourly rate percentage 
 |

| daily 
| Pledge loan days 
 |

| borrowTime 
| Borrowing time 
 |

| status 
| Status 
 |

 

 

 

 

 

 

 

 

 

 

### Query the list of assets and liabilities

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/debts

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/debts?startTime=1691119224000&endTime=1692436119603" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

N/A

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1692436610750,
  "data": {
    "pledgeInfos": [
      {
        "coin": "USDT",
        "amount": "28826.61539642",
        "amountUsdt": "28826.61"
      }
    ],
    "loanInfos": [
      {
        "coin": "ETH",
        "amount": "11.00002748",
        "amountUsdt": "18730.85"
      }
    ]
  }
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| loanInfos 
| Pledged assets info 
 |

| >coin 
| Coin 
 |

| >amount 
| Amount 
 |

| >amountUsdt 
| Amount usdt 
 |

| pledgeInfos 
| Pledge assets Info 
 |

| >coin 
| Coin 
 |

| >amount 
| Amount 
 |

| >amountUsdt 
| Amount usdt 
 |

 

 

 

 

 

 

 

 

 

 

### Query the list of forced liquidation records

Rate Limit: 10 times/1s (UID)

HTTP Request

- GET /api/spot/v1/loan/reduces

Request Example

```
curl "https://api.bitget.com/api/spot/v1/loan/reduces?startTime=1691119224000&endTime=1692436119603" \
  -H "ACCESS-KEY:you apiKey" \
  -H "ACCESS-SIGN:*******" \
  -H "ACCESS-PASSPHRASE:*****" \
  -H "ACCESS-TIMESTAMP:1659076670000" \
  -H "locale:en-US" \
  -H "Content-Type: application/json" 

```

Request Parameter

| 

| Parameter 
| type 
| Required 
| description 
 |

| orderId 
| String 
| no 
| Order ID 
 |

| loanCoin 
| String 
| no 
| Loan coin 
 |

| pledgeCoin 
| String 
| no 
| Pledge coin 
 |

| status 
| String 
| no 
| Status 
 |

| startTime 
| String 
| yes 
| Start time, only supports querying the data of the past three months 
 |

| endTime 
| String 
| yes 
| End time 
 |

| pageNo 
| String 
| no 
| pageNo default 1 
 |

| pageSize 
| String 
| no 
| pageSize  default 10，max 100 
 |

- status

COMPLETE completed liquidation

- WAIT liquidating

Response

```

{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684747525424,
  "data": [{
    "orderId": "1278182632",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "reduceTime": "0.757",
    "pledgeRate": "98.2",
    "pledgePrice": "111.4",
    "status": "COMPLETE",
    "pledgeAmount": "1213.5",
    "reduceFee": "REPAY",
    "residueAmount": "3234.2",
    "runlockAmount": "23",
    "repayLoanAmount": "53.2"
  }, {
    "orderId": "1278182632",
    "loanCoin": "TRX",
    "pledgeCoin": "USDT",
    "reduceTime": "0.757",
    "pledgeRate": "98.2",
    "pledgePrice": "111.4",
    "status": "COMPLETE",
    "pledgeAmount": "1213.5",
    "reduceFee": "REPAY",
    "residueAmount": "3234.2",
    "runlockAmount": "23",
    "repayLoanAmount": "53.2"
  }]
}

```

Response Parameter

| 

| Parameter 
| Description 
 |

| orderId 
| Order ID 
 |

| loanCoin 
| Loan coin 
 |

| pledgeCoin 
| Pledge coin 
 |

| reduceTime 
| Liquidation time 
 |

| pledgeRate 
| Pledge rate percentage during liquidation 
 |

| pledgePrice 
| Pledge price when Liquidation 
 |

| status 
| Liquidation status 
 |

| pledgeAmount 
| Liquidation of the number of pledged coins 
 |

| reduceFee 
| Liquidation fee 
 |

| residueAmount 
| Remaining pledged coin amount 
 |

| runlockAmount 
| Release the amount of pledged coin 
 |

| repayLoanAmount 
| Repayment of loan amount 
 |

 

 

 

 

 

 

 

 

 

 

# WebSocketAPI

## Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

- The WebSocket request header size for data transmission between client and server is only 2 bytes.

- Either the client or server can initiate data transmission.

- There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

It is strongly recommended that developers use WebSocket API to obtain market information and transaction depth.
​     

| 

| domain 
| WebSocket API 
| Recommended to use 
 |

| domain 1 
| wss://ws.bitget.com/spot/v1/stream 
| internationality 
 |

## Connect

Connection instructions:

Connection limit: 100 connections per IP

When subscribing to a public channel, no login is required. 

When subscribing to a private channel, MUST login before subscribe to any channel(s)

Subscription limit: 240 times per hour

If there’s a network problem, the system will automatically close the connection.

The connection will be closed automatically if the subscription is not established or, no data pushed from server for more than 30 seconds.

Client should keep ping the server in every 30 seconds. Server will close the connections which has no ping over 120 seconds(even when the client is still receiving data from the server)

To keep the connection stable:

- Set a timer of 30 seconds.

- If the timer is triggered, send the String 'ping'.

- Expect a 'pong' as a response. If the response message is not received within 30 seconds, please raise an error and/or reconnect.

- The Websocket server accepts up to 10 messages per second. The message includes:

PING frame

- Messages in JSON format, such as subscribe, unsubscribe.

- If the user sends more messages than the limitation, the connection will be disconnected. IPs that are repeatedly disconnected may be blocked by the server;

- A single connection can subscribe up to 1000 Streams;

- A single IP can create up to 100 connections.

## Login

api_key: Unique identification for invoking API. Requires user to apply one manually.

passphrase: APIKey password

timestamp: the Unix Epoch time, the unit is seconds

sign: signature string

method: always 'GET'

requestPath: always '/user/verify'

secretKey: The security key generated when the user applies for APIKey, e.g. : 22582BD0CFF14C41EDBF1AB98506286D

the signature algorithm is as follows:

```
Concatenate "timestamp", "method", "requestPath", and "body" as string
Encrypt the string using Hmac_SHA256 with secretKey
Base64 encode the Hmac_SHA256 output

```

Sign example
`
sign=CryptoJS.enc.Base64.Stringify(
    CryptoJS.HmacSHA256(timestamp +'GET'+'/user/verify', secretKey)
)
`

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the server time(noted it return milliseconds, while in websocket login you should use seconds) and then set the timestamp.

For the description of the signature method, refer to the verification section in the API overview

Steps to generate the final signature:

Step 1. Use the private key secretkey to encrypt the string to be signed with hmac sha256

Signature = hmac_sha256(secretkey, Message)

The second step is to base64 encode the Signature

Signature = base64.encode(Signature)

If login fails, it will automatically disconnect

Request format description

```
{
    "op": "login",
    "args": [{
        "apiKey": "<api_key>",
        "passphrase": "<passphrase>",
        "timestamp": "<timestamp>",
        "sign": "<sign>"
    }]
}

```

Request Example

```
{
    "op": "login",
    "args": [{
        "apiKey": "bg_573af5eca856acd91c230da294ce2105",
        "passphrase": "123456",
        "timestamp": "1538054050",
        "sign": "8RCOqCJAhhEh4PWcZB/96QojLDqMAg4qNynIixFzS3E="
    }]
} 

```

Successful Response Example

```
{
    "event": "login",
    "code": "0",
    "msg": ""
} 

```

Failure Response Example

```
{
    "event": "error",
    "code": "30005",
    "msg": "error"
}

```

## Subscribe

Subscription Instructions

Request format description

```
{
  "op": "subscribe",
  "args": ["<SubscriptionTopic>"]
}

```

WebSocket channels are divided into two categories: `public` and `private` channels.

`Public channels` -- includes 

Tickers channel

Candlesticks channel

Depth channel

Trades Channel

etc -- do not require log in.

- `instId` refer to  Get Symbols in response field: `symbolName`

`Private channels` -- including 

Account Channel

Order Channel

etc -- require login.

- User account channel `instId` is `default` : Get all currency assets

User can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 4096 bytes.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }, {
        "instType": "SP",
        "channel": "candle5m",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribe channels 
 |

| > instType 
| String 
| No 
| Instrument type`SP`: Spot public channel  `SPBL` Spot private channel 
 |

| > channel 
| String 
| Yes 
| Channel name, please refer to each examples below 
 |

| > instId 
| String 
| No 
| refer to Get Symbols  in response field: `symbolName`; at some cases 'default' 
 |

Example response

```
{
    "event": "subscribe",
    "args": {
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }
}

```

Return parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event, `subscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| No 
| Instrument type`SP`: Spot public channel  `SPBL` Spot private channel 
 |

| > channel 
| String 
| Yes 
| Channel name, same as request 
 |

| > instId 
| String 
| No 
| Instrument ID 
 |

| code 
| String 
| No 
| Error code 
 |

| msg 
| String 
| No 
| Error message 
 |

## Unsubscribe

Unsubscribe from one or more channels.

Request format description

```
{
  "op": "unsubscribe",
  "args": ["< SubscriptionTopic> "]
}

```

Request Example

```
{
    "op": "unsubscribe",
    "args": [{
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }, {
        "instType": "SP",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of channels to unsubscribe from 
 |

| > instType 
| String 
| Yes 
| Instrument type`SP`: Spot public channel  `SPBL` Spot private channel 
 |

| > channel 
| String 
| Yes 
| Channel name, please refer to each examples below 
 |

| > instId 
| String 
| Yes 
| refer to Get Symbols in response field: `symbolName`; at some cases 'default' 
 |

Example response

```
{
    "event": "unsubscribe",
    "args": {
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }
} 

```

Return parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event, `unsubscribe` `error` 
 |

| arg 
| Object 
| Yes 
| Unsubscribed channel 
 |

| >instType 
| String 
| No 
| Instrument type`SP`: Spot public channel  `SPBL` Spot private channel 
 |

| > channel 
| String 
| Yes 
| Channel name 
 |

| > instId 
| String 
| Yes 
| Instrument ID 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

## Checksum

This mechanism will assist users to checking the accuracy of depth data.

### Merging incremental data into full data

After subscribing to the incremental push channel (such as `books` 400 levels) of Order Book Channel, users first receive the initial snapshot of the market depth. Afterwards the incremental data is subsequently received, you are responsible to update the snapshot locally.

- If there is a same price, compare the amount. If the amount is 0, delete this depth data. If the amount changes, replace the original data.

- If there is no same price, sort by price (bids in descending order, asks in ascending order), and insert the depth information into the local snapshot.

### Calculate Checksum

Use the first 25 bids and asks in the local snapshot to build a string (where a colon connects the price and amount in an ask or a bid), and then calculate the CRC32 value (32-bit signed integer).

Calculate Checksum

```
1. More than 25 levels of bid and ask
A local snapshot of market depth (only 2 levels of the orderbook are shown here, while 25 levels of orderbook should actually be intercepted):
    "bids": [
      [ 43231.1, 4 ],   //bid1
      [ 43231,   6 ]    //bid2
    ]
    "asks": [
      [ 43232.8, 9 ],   //ask1
      [ 43232.9, 8 ]    //ask2
    ]
Build the string to check CRC32:
"43231.1:4:43232.8:9:43231:6:43232.9:8"
The sequence:
"bid1[price:amount]:ask1[price:amount]:bid2[price:amount]:ask2[price:amount]"

2. Less than 25 levels of bid or ask
A local snapshot of market depth:
    "bids": [
      [ 3366.1, 7 ]
    ]
    "asks": [
      [ 3366.8, 9 ],
      [ 3368  , 8 ],
      [ 3372  , 8 ]
    ]

Build the string to check CRC32:
"3366.1:7:3366.8:9:3368:8:3372:8"
The sequence:
"bid1[price:amount]:ask1[price:amount]:ask2[price:amount]:ask3[price:amount]"

```

- When the bid and ask depth data exceeds 25 levels, each of them will intercept 25 levels of data, and the string to be checked is queued in a way that the bid and ask depth data are alternately arranged.
Such as: `bid1[price:amount]`:`ask1[price:amount]`:`bid2[price:amount]`:`ask2[price:amount]`...

- When the bid or ask depth data is less than 25 levels, the missing depth data will be ignored.
Such as: `bid1[price:amount]`:`ask1[price:amount]`:`ask2[price:amount]`:`ask3[price:amount]`...

- If price is '0.5000', DO NOT calculate the checksum by '0.5', please DO use the original value

## Public Channels

### Tickers Channel

Retrieve the last traded price, bid price, ask price and 24-hour trading volume of the instruments. Data will be pushed every 200 ms.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribed channels 
 |

| > instType 
| String 
| Yes 
| Instrument type`SP`: Spot public channel; `MC`: Contract/future channel 
 |

| > channel 
| String 
| Yes 
| Channel name, `ticker` 
 |

| > instId 
| String 
| Yes 
| Instrument ID, refer to Get Symbols in response field: `symbolName`, a sample value could be like `BTCUSDT` 
 |

Successful Response Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "SP",
        "channel": "ticker",
        "instId": "BTCUSDT"
    }]
}

```

Failure Response Example

```
{
    "event": "error",
    "arg": {
        "instType": "sp",
        "channel": "ticker",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:sp,ticker:candle1D,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event, `subscribe` `unsubscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| Yes 
| Instrument Type 
 |

| > channel 
| String 
| Yes 
| Channel name 
 |

| > instId 
| String 
| Yes 
| Instrument name 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| arg 
| Object 
| Successfully subscribed channel 
 |

| > instType 
| String 
| Instrument Type 
 |

| > channel 
| String 
| Channel name 
 |

| > instId 
| String 
| Instrument ID 
 |

| action 
| String 
| Push data action, incremental or full data.  `update`: incremental; `snapshot`: full, channel 'ticker' would only return 'snapshot' 
 |

| data 
| Array 
| Subscribed data array 
 |

| >instId 
| String 
| Instrument ID, BTCUSDT 
 |

| >last 
| String 
| Latest traded price from the moment this data generated 
 |

| >bestAsk 
| String 
| Best ask price or: ask1 price 
 |

| >bestBid 
| String 
| Best bid price or: bid1 price 
 |

| >open24h 
| String 
| Open price in the past 24 hours 
 |

| >high24h 
| String 
| Highest price in the past 24 hours 
 |

| >low24h 
| String 
| Lowest price in the past 24 hours 
 |

| >baseVolume 
| String 
| 24h trading volume,  with a unit of `currency`. BTC is base currency in BTCUSDT 
 |

| >quoteVolume 
| String 
| 24h trading volume, with a unit of `contract`.USDT is quote contract in BTCUSDT 
 |

| >ts 
| String 
| Ticker data generation time, Unix timestamp format in milliseconds 
 |

| >labeId 
| Long 
| Label ID 
 |

| >openUtc 
| String 
| Open price in UTC time 
 |

| >chgUTC 
| String 
| Change rate since openUtc, that is: (last - openUtc) / openUtc, scale e-5 
 |

| >bidSz 
| String 
| Best bid size 
 |

| >askSz 
| String 
| Best ask size 
 |

Response Example

```
{
    "action": "snapshot",
    "arg": {
        "instType": "sp",
        "channel": "ticker",
        "instId": "BTCUSDT"
    },
    "data": [
        {
            "instId": "BTCUSDT",
            "last": "20193.17",
            "open24h": "19112.64",
            "high24h": "20374.29",
            "low24h": "18973.16",
            "bestBid": "20192.420000",
            "bestAsk": "20196.440000",
            "baseVolume": "13177.3815",
            "quoteVolume": "261300702.3745",
            "ts": 1664292040025,
            "labeId": 0,
            "openUtc": "19226.5300000000000000",
            "chgUTC": "0.05028",
            "bidSz": "0.06",
            "askSz": "0.0119"
        }
    ]
}

```

### Candlesticks Channel

Retrieve the candlesticks data of an instrument. Data will be pushed every 500 ms.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "sp",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscription channels 
 |

| > instType 
| String 
| Yes 
| Instrument Type `SP`: spot; `MC`: contract/future 
 |

| > channel 
| String 
| Yes 
| Channel Name，`candle1W, candle1D, candle12H, candle4H, candle1H, candle30, candle15m, candle5m, candle1m` 
 |

| > instId 
| String 
| Yes 
| Instrument ID for example :BTCUSDT 
 |

Successful Response Example

```
{
    "event": "subscribe",
    "arg": {
        "instType": "sp",
        "channel": "candle1D",
        "instId": "BTCUSDT"
    }
}

```

Failure Response Example

```
{
    "event": "error",
    "arg": {
        "instType": "sp",
        "channel": "candle1D",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:sp,channel:candle1D,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event, `subscribe` `unsubscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| Yes 
| Instrument Type 
 |

| > channel 
| String 
| Yes 
| channel name 
 |

| > instId 
| String 
| Yes 
| Instrument name 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

Push Data Example - snapshot

```
{
    "action": "snapshot",
    "arg": {
        "instType": "sp",
        "channel": "candle1D",
        "instId": "BTCUSDT"
    },
    "data": [
        ["1597026383085", "8533.02", "8553.74", "8527.17", "8548.26", "45247"]
    ]
} 

```

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| arg 
| Object 
| Successfully subscribed channel 
 |

| > instType 
| String 
| Instrument Type 
 |

| > channel 
| String 
| Channel name 
 |

| > instId 
| String 
| Instrument ID 
 |

| data 
| Array 
| Subscription data array, format in String Array 
 |

| > ts 
| String 
| Data generation time, Unix timestamp format in milliseconds 
 |

| > o 
| String 
| Open price 
 |

| > h 
| String 
| highest price 
 |

| > l 
| String 
| Lowest price 
 |

| > c 
| String 
| Close price 
 |

| >v 
| String 
| Trading volume, with a unit of `contact` 
 |

### Depth channel

Subscribe depth(order book) data

`books`: Push the full snapshot data for the first time, push incrementally later, that is, if there is a change in depth, the depth data that has changed will be pushed

`books5`: Push 5 levels of snapshot data every time

`book15` 15 levels of snapshot data  every time

| 

| Channel 
| Length of bids 
| Length of asks 
| Remark 
 |

| books 
| maximum 200 
| maximum 200 
| Snapshot and update might return less than 200 bids/asks as per symbol's orderbook various from each other; The number of bids/asks is not a fixed value and may vary in the future 
 |

| books5 
| 5 
| 5 
| Top 5 order book of "books" that begins from bid1/ask1 
 |

| books15 
| 15 
| 15 
| Top 15 order book of "books" that begins from bid1/ask1 
 |

For example, if the whole order book consist of 20 bids and 12 asks

channel books return 20 bids and 12 asks

channel books5 return 5 bids and 5 asks, bids return from index 15 to 19(index 19 is bid1), asks return from index 0 to index 4

channel books15 return 15 bids index from 5 to 19(index 19 is bid1), and return 12 asks index from 0 to 11

Noted that bids are in descending order, while asks are in ascending order

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "sp",
        "channel": "books5",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribed channels 
 |

| > instType 
| String 
| Yes 
| Instrument Type `SP` 
 |

| > channel 
| String 
| Yes 
| Channel name, `books` `books5` or `books15` 
 |

| > instId 
| String 
| Yes 
| Instrument ID 
 |

Example Response

```
{
    "event": "subscribe",
    "arg": {
        "instType": "sp",
        "channel": "books5",
        "instId": "BTCUSDT"
    }
}

```

Failure example

```
{
    "event": "error",
    "arg": {
        "instType": "sp",
        "channel": "books5",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:sp,channel:books5,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event，`subscribe` `unsubscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| Yes 
| Instrument Type 
 |

| > channel 
| String 
| Yes 
| Channel name 
 |

| > instId 
| String 
| Yes 
| Instrument ID 
 |

| msg 
| String 
| No 
| Error Message 
 |

| code 
| String 
| No 
| Error Code 
 |

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| arg 
| Object 
| Successfully subscribed channel 
 |

| > instType 
| String 
| Instrument Type 
 |

| > channel 
| String 
| Channel name 
 |

| > instId 
| String 
| Instrument ID 
 |

| action 
| String 
| Push data action, incremental push data or full push data `snapshot`: full `update`: incremental 
 |

| data 
| Array 
| Subscribed data 
 |

| > asks 
| Array 
| Order book on sell side, ascending order 
 |

| > bids 
| Array 
| Order book on buy side, descending order 
 |

| > ts 
| String 
| Order book generation time, Unix timestamp format in milliseconds 
 |

| > checksum 
| Integer 
| Checksum, calculate and compare the checksum, re-subscribe if mis-match 
 |

An example of the array of asks and bids values: ["411.8", "10"] "411.8" is the depth price, "10" is the size

### Trades Channel

Retrieve the recent trading data. Data will be pushed whenever there is a trade.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "sp",
        "channel": "trade",
        "instId": "BTCUSDT"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribed channels 
 |

| > instType 
| String 
| Yes 
| Instrument Type, `sp` : spot 
 |

| > channel 
| String 
| Yes 
| Channel Name，`trade` 
 |

| > instId 
| String 
| Yes 
| Instrument ID, i.e. BTCUSDT 
 |

Successful Response Example

```
{
    "event": "subscribe",
    "arg": [{
        "instType": "sp",
        "channel": "trade",
        "instId": "BTCUSDT"
    }]
}

```

Failure Response Example

```
{
    "event": "error",
    "arg": {
        "instType": "sp",
        "channel": "trade",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:sp,channel:trade,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event，`subscribe` `unsubscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| Yes 
| InstrumentType 
 |

| > channel 
| String 
| Yes 
| Channel Name 
 |

| > instId 
| String 
| Yes 
| Instrument ID 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| arg 
| Object 
| Successfully subscribed channel 
 |

| > instType 
| String 
| Instrument Type 
 |

| > channel 
| String 
| Channel Name 
 |

| > instId 
| String 
| Instrument ID 
 |

| data 
| Array 
| Subscribed data 
 |

| > ts 
| String 
| Filled time, Unix timestamp format in milliseconds 
 |

| > px 
| String 
| Trade price 
 |

| > sz 
| String 
| Trade size 
 |

| > side 
| String 
| Trade direction, `buy`, `sell` 
 |

## Private Channel

### Account Channel

Subscribe account information. Data will be pushed when triggered by events such as placing/canceling order, and will also be pushed when transfer in/out or withdraw/deposit.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "instType": "spbl",
        "channel": "account",
        "instId": "default"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribed channels 
 |

| > instType 
| String 
| Yes 
| Instrument Type,`spbl` 
 |

| > channel 
| String 
| Yes 
| Channel Name，`account` 
 |

| > instId 
| String 
| Yes 
| Currency, always 'default' 
 |

Successful Response Example 

```
{
    "event": "subscribe",
    "arg": {
        "instType": "spbl",
        "channel": "account",
        "instId": "default"
    }
} 

```

Failure Response Example

```
{
    "event": "error",
    "arg": {
        "instType": "spbl",
        "channel": "account",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:SP,channel:account,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Operation, `subscribe` `unsubscribe` `error` 
 |

| arg 
| Object 
| No 
| Subscribed channel 
 |

| > instType 
| String 
| Yes 
| Instrument Type 
 |

| > channel 
| String 
| Yes 
| Channel Name 
 |

| > instId 
| String 
| No 
| Currency 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

Push Data Example

```
{
    "action": "snapshot",
    "arg": {
        "instType": "spbl",
        "channel": "account",
        "instId": "default"
    },
    "data": [{
        "coinId": "2",
        "coinName": "USDT",
        "available": "1000.0000"
    }, {
        "coinId": "1",
        "coinName": "BTC",
        "available": "1.35000"
    }]
}

```

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| action 
| String 
| `snapshot`: snapshot of current account, `update`: incremental changes 
 |

| arg 
| Object 
| Successfully subscribed channel 
 |

| > instType 
| String 
| Instrument Type 
 |

| > channel 
| String 
| Channel Name 
 |

| > instId 
| String 
| Currency 
 |

| data 
| Array 
| Subscribed data 
 |

| > coinId 
| String 
| Coin Id 
 |

| > coinName 
| String 
| Coin Name, BTC, USDT 
 |

| > available 
| String 
| balance 
 |

First push: full push.

Incremental push: push transaction changes

### Order Channel

Retrieve order information. Data will not be pushed when first subscribed. Data will only be pushed when triggered by events such as placing/canceling order.

Request Example

```
{
    "op": "subscribe",
    "args": [{
        "channel": "orders",
        "instType": "spbl",
        "instId": "BTCUSDT_SPBL"
    }]
}

```

Request parameters

| 

| Parameter 
| Type 
| Required 
| Description 
 |

| op 
| String 
| Yes 
| Operation，`subscribe` `unsubscribe` 
 |

| args 
| Array 
| Yes 
| List of subscribed channels 
 |

| > instType 
| String 
| Yes 
| Instrument Type,spbl 
 |

| > channel 
| String 
| Yes 
| Channel Name, `orders` 
 |

| > instId 
| String 
| Yes 
| Instrument Id, BTCUSDT_SPBL 
 |

Successful Response Example

```
{
    "event": "subscribe",
    "arg": {
        "channel": "orders",
        "instType": "spbl",
        "instId": "BTCUSDT_SPBL"
    }
}

```

Failure Response Example

```
{
    "event": "error",
    "arg": {
        "instType": "spbl",
        "channel": "orders",
        "instId": "BTC-USDT"
    },
    "code": 30001,
    "msg": "instType:SP,channel:orders,instId:BTC-USDT doesn't exist",
    "op": "subscribe"
}

```

Response parameters

| 

| Parameters 
| Type 
| Required 
| Description 
 |

| event 
| String 
| Yes 
| Event，`subscribe` `unsubscribe` `errror` 
 |

| arg 
| Object 
| No 
| Subscribed Data 
 |

| > channel 
| String 
| Yes 
| Channel Name 
 |

| > instType 
| String 
| Yes 
| Instrument Type`spbl：private spot 
 |

| > instId 
| String 
| No 
| Instrument Id 
 |

| code 
| String 
| No 
| Error Code 
 |

| msg 
| String 
| No 
| Error Message 
 |

Push data Example

```
{
  "data":[
    {
      "notional":"6.290480",
      "side":"buy",
      "sz":"0.0040",
      "px":"1572.62",
      "orderFee":[

      ],
      "eps":"WEB",
      "cTime":1678789919603,
      "ordId":"10194123402951243161",
      "instId":"ETHUSDT_SPBL",
      "clOrdId":"b712d4e8-bec1-4124-ae83-e7aa44cfcdd2",
      "accFillSz":"0.0000",
      "avgPx":"0.00",
      "force":"normal",
      "uTime":1678789919603,
      "ordType":"limit",
      "status":"new"
    }
  ],
  "arg":{
    "instType":"spbl",
    "instId":"default",
    "channel":"orders"
  },
  "action":"snapshot"
}

```

Push data parameters

| 

| Parameter 
| Type 
| Description 
 |

| action 
| String 
| 'snapshot' 
 |

| arg 
| String 
| Subscribe arg 
 |

| > channel 
| String 
| Channel Name 
 |

| > instType 
| String 
| Instrument Type 
 |

| > instId 
| String 
| Instrument Id 
 |

| data 
| Array 
| Subscribed Data 
 |

| > instId 
| String 
| Instrument Id 
 |

| > ordId 
| String 
| Order Id 
 |

| > clOrdId 
| String 
| Client customized order ID 
 |

| > px 
| String 
| Order price 
 |

| > sz 
| String 
| The original order quantity 
 |

| > notional 
| String 
| The purchase amount, which will be returned when the market price is purchased 
 |

| > ordType 
| String 
| Order Type  `market` `limit` 
 |

| > force 
| String 
| Category`normal``twap``adl``full_liquidation``partial_liquidation` 
 |

| > side 
| String 
| order side，`buy` `sell` 
 |

| > fillPx 
| String 
| fill price 
 |

| > tradeId 
| String 
|  
 |

| > fillSz 
| String 
| fill size 
 |

| > fillTime 
| String 
| fill time 
 |

| > fillFee 
| String 
| last filled fee, negative 
 |

| > fillFeeCcy 
| String 
| last filled fee currency 
 |

| > execType 
| String 
| Order flow type, T: taker M: maker 
 |

| > accFillSz 
| String 
| Accumulated fill quantity 
 |

| > avgPx 
| String 
| Average filled price. If none is filled, it will return `0`. 
 |

| > status 
| String 
| order state `new`, `partial-fill`, `full-fill`, `cancelled` 
 |

| > eps 
| String 
| enterPointSource 
 |

| > cTime 
| String 
| Created time, Unix timestamp format in milliseconds 
 |

| > uTime 
| String 
| Updated time, Unix timestamp format in milliseconds 
 |

| > orderFee 
| Array 
| fee list 
 |

| >> feeCcy 
| String 
| Fee currency 
 |

| >> fee 
| String 
| Negative fee: the user transaction fee charged by the platform. Positive fee means rebate. 
 |

# RestAPI  error code

| 

| Error message 
| Error code 
| http status code 
 |

| 00000 
| success! 
| 400 
 |

| 40001 
| ACCESS_KEY cannot be empty 
| 400 
 |

| 40002 
| ACCESS_SIGN cannot be empty 
| 400 
 |

| 40003 
| Signature cannot be empty 
| 400 
 |

| 40004 
| Request timestamp expired 
| 400 
 |

| 40005 
| Invalid ACCESS_TIMESTAMP 
| 400 
 |

| 40006 
| Invalid ACCESS_KEY 
| 400 
 |

| 40007 
| Invalid Content_Type 
| 400 
 |

| 40008 
| Request timestamp expired 
| 400 
 |

| 40009 
| sign signature error 
| 400 
 |

| 40010 
| Request timed out 
| 400 
 |

| 40011 
| ACCESS_PASSPHRASE cannot be empty 
| 400 
 |

| 40012 
| apikey/password is incorrect 
| 400 
 |

| 40013 
| User status is abnormal 
| 400 
 |

| 40014 
| Incorrect permissions, need {0} permissions 
| 400 
 |

| 40015 
| System is abnormal, please try again later 
| 400 
 |

| 40016 
| The user must bind the phone or Google 
| 400 
 |

| 40017 
| Parameter verification failed {0} 
| 400 
 |

| 00171 
| Parameter verification failed {0}{1} 
| 400 
 |

| 00172 
| Parameter verification failed 
| 400 
 |

| 40018 
| Invalid IP 
| 400 
 |

| 40019 
| Parameter {0} cannot be empty 
| 400 
 |

| 40020 
| Parameter {0} error 
| 400 
 |

| 40021 
| User disable withdraw 
| 400 
 |

| 40022 
| The business of this account has been restricted 
| 400 
 |

| 40023 
| The business of this account has been restricted 
| 400 
 |

| 40024 
| Account has been frozen 
| 400 
 |

| 40025 
| The business of this account has been restricted 
| 400 
 |

| 40026 
| User is disabled 
| 400 
 |

| 40027 
| Withdrawals in this account area must be kyc 
| 400 
 |

| 40028 
| This subUid does not belong to this account 
| 400 
 |

| 40029 
| This account is not a Broker, please apply to become a Broker first 
| 400 
 |

| 40031 
| The account has been cancelled and cannot be used again 
| 400 
 |

| 40032 
| The Max of sub-account created has reached the limit 
| 400 
 |

| 40033 
| This email has been bound 
| 400 
 |

| 40034 
| Parameter {0} does not exist 
| 400 
 |

| 50001 
| coin {0} does not support cross 
| 400 
 |

| 50002 
| symbol {0} does not support isolated 
| 400 
 |

| 50003 
| coin {0} does not support isolated 
| 400 
 |

| 50004 
| symbol {0} does not support cross 
| 400 
 |

| 40035 
| Judging from your login information, you are required to complete KYC first for compliance reasons. 
| 400 
 |

| 40036 
| passphrase is error 
| 400 
 |

| 40037 
| Apikey does not exist 
| 400 
 |

| 40038 
| The current ip is not in the apikey ip whitelist 
| 400 
 |

| 40039 
| FD Broker's user signature error 
| 400 
 |

| 40040 
| user api key permission setting error 
| 400 
 |

| 40041 
| User's ApiKey does not exist 
| 400 
 |

| 40043 
| FD Broker does not exist 
| 400 
 |

| 40045 
| The bound user cannot be an FD broker 
| 400 
 |

| 40047 
| FD Broker binding related interface call frequency limit 
| 400 
 |

| 40048 
| The user's ApiKey must be the parent account 
| 400 
 |

| 40049 
| User related fields decrypt error 
| 400 
 |

| 40051 
| This account is not a FD Broker, please apply to become a FD Broker first 
| 400 
 |

| 40052 
| Security settings have been modified for this account. For the safety of your account, withdrawals are prohibited within 24 hours 
| 400 
 |

| 40053 
| Value range verification failed: {0} should be between {1} 
| 400 
 |

| 40054 
| The data fetched by {0} is empty 
| 400 
 |

| 40055 
| subName must be an English letter with a length of 8 
| 400 
 |

| 40056 
| remark must be length of 1 ~ 20 
| 400 
 |

| 40057 
| Parameter {0} {1} does not meet specification 
| 400 
 |

| 40058 
| Parameter {0} Only a maximum of {1} is allowed 
| 400 
 |

| 40059 
| Parameter {0} should be less than {1} 
| 400 
 |

| 40060 
| subNames already exists 
| 400 
 |

| 40061 
| sub-account not allow access 
| 400 
 |

| 40063 
| API exceeds the maximum limit added 
| 400 
 |

| 40064 
| Sub-account creation failed, please check if there is a duplicate 
| 400 
 |

| 40065 
| This subApikey does not exist 
| 400 
 |

| 40066 
| This subUid does not belong to the account or is not a virtual sub-account 
| 400 
 |

| 40067 
| sub-account create failed, please check if there is a duplicate 
| 400 
 |

| 40068 
| Disable subaccount access 
| 400 
 |

| 40069 
| The maximum number of sub-accounts created has been reached 
| 400 
 |

| 40070 
| passphrase 8-32 characters with letters and numbers 
| 400 
 |

| 40071 
| subName exist duplication 
| 400 
 |

| 40072 
| symbol {0} is Invalid or not supported mix contract trade 
| 400 
 |

| 40102 
| Symbol does not exist 
| 400 
 |

| 40109 
| The data of the order cannot be found, please confirm the order number 
| 400 
 |

| 40200 
| Server upgrade, please try again later 
| 400 
 |

| 40301 
| Permission has not been obtained yet. If you need to use it, please contact customer service 
| 400 
 |

| 40303 
| Can only query up to 20,000 data 
| 400 
 |

| 40304 
| clientOid or clientOrderId length cannot greater than 50 
| 400 
 |

| 40305 
| clientOid or clientOrderId length cannot greater than 64, and cannot be Martian characters 
| 400 
 |

| 40306 
| Batch processing orders can only process up to 20 
| 400 
 |

| 40308 
| The contract is being temporarily maintained 
| 400 
 |

| 40309 
| The contract has been removed 
| 400 
 |

| 40400 
| Status check abnormal 
| 400 
 |

| 40401 
| The operation cannot be performed 
| 400 
 |

| 40402 
| orderId or clientOId format error 
| 400 
 |

| 40407 
| The query direction is not the direction entrusted by the plan 
| 400 
 |

| 40408 
| Range error 
| 400 
 |

| 40409 
| wrong format 
| 400 
 |

| 40704 
| Can only check the data of the last three months 
| 400 
 |

| 40705 
| The start and end time cannot exceed 90 days 
| 400 
 |

| 40706 
| Wrong order price 
| 400 
 |

| 40707 
| Start time is greater than end time 
| 400 
 |

| 40708 
| client_oid duplicate 
| 400 
 |

| 40709 
| There is no position in this position, and no automatic margin call can be set 
| 400 
 |

| 40710 
| Abnormal account status 
| 400 
 |

| 40711 
| Insufficient contract account balance 
| 400 
 |

| 40712 
| Insufficient margin 
| 400 
 |

| 40713 
| Cannot exceed the maximum transferable margin amount 
| 400 
 |

| 40714 
| No direct margin call is allowed 
| 400 
 |

| 40715 
| delegate count can not high max of open count 
| 400 
 |

| 40716 
| This trading pair not support Cross Margin mode 
| 400 
 |

| 40717 
| The number of closed positions cannot exceed the number of sheets held 
| 400 
 |

| 40718 
| The entrusted price of Pingduo shall not be lower than the bursting price 
| 400 
 |

| 40719 
| Flat empty entrustment price is not allowed to be higher than explosion price 
| 400 
 |

| 40720 
| swap hand depth does not exist 
| 400 
 |

| 40721 
| Market price list is not allowed at present 
| 400 
 |

| 40722 
| Due to excessive price fluctuations and the  insufficient market price entrusted cost,  the opening commission is failed. 
| 400 
 |

| 40723 
| The total number of unexecuted orders is too high 
| 400 
 |

| 40724 
| Parameter is empty 
| 400 
 |

| 40725 
| service return an error 
| 400 
 |

| 40726 
| Cross margin not support Auto Margin Replenishment (AMR) 
| 400 
 |

| 40727 
| Cross margin not support margin adjustment 
| 400 
 |

| 40728 
| You’re log in as trader, please close position for current copy trade orders 
| 400 
 |

| 40729 
| Failed to adjust the position, the current position or order or plan order 
| 400 
 |

| 40730 
| There is currently a commission or a planned commission, and the leverage cannot be adjusted 
| 400 
 |

| 40731 
| This product does not support copy trading 
| 400 
 |

| 40732 
| Not currently a trader 
| 400 
 |

| 40199 
| Traders are prohibited from calling the API 
| 400 
 |

| 40733 
| The order closing has been processed 
| 400 
 |

| 40734 
| Failed to place an order, the minimum number of traders to open a position {0} 
| 400 
 |

| 40735 
| Long position take profit price should be greater than the average opening price 
| 400 
 |

| 40736 
| Long position take profit price is greater than the current price 
| 400 
 |

| 40737 
| The short position take profit price should be less than the average opening price 
| 400 
 |

| 40738 
| The short position take profit price should be less than the current price 
| 400 
 |

| 40739 
| The stop loss price of a long position should be less than the average opening price 
| 400 
 |

| 40740 
| The stop loss price of a long position should be less than the current price 
| 400 
 |

| 40741 
| The stop loss price of a short position should be greater than the average opening price 
| 400 
 |

| 40742 
| The stop loss price of the short position should be greater than the current price 
| 400 
 |

| 40743 
| The order is being closed and cannot be closed again 
| 400 
 |

| 40744 
| The tracking order status is wrong 
| 400 
 |

| 40745 
| This order is being commissioned, and liquidation is not supported temporarily 
| 400 
 |

| 40746 
| The current maximum number of positions that can be closed is {0}, if you exceed the number, please go to the current order to close the position 
| 400 
 |

| 40747 
| The bonus is not allowed to hold two-way positions 
| 400 
 |

| 40748 
| The commission price is higher than the highest bid price 
| 400 
 |

| 40749 
| The commission price is lower than the lowest selling price 
| 400 
 |

| 40750 
| The plan commission for this contract has reached the upper limit 
| 400 
 |

| 40751 
| The contract's stop profit and stop loss order has reached the upper limit 
| 400 
 |

| 40752 
| You are disabled for current business, if you have any questions, please contact customer service 
| 400 
 |

| 40753 
| The contract transaction business is disabled, if you have any questions, please contact customer service 
| 400 
 |

| 40754 
| balance not enough 
| 400 
 |

| 40755 
| Not enough open positions are available. 
| 400 
 |

| 40756 
| The balance lock is insufficient. 
| 400 
 |

| 40757 
| Not enough position is available. 
| 400 
 |

| 40758 
| The position lock is insufficient. 
| 400 
 |

| 40759 
| No assets 
| 400 
 |

| 40760 
| Account abnormal status 
| 400 
 |

| 40761 
| The total number of unfilled orders is too high 
| 400 
 |

| 40762 
| The order size is greater than the max open size 
| 400 
 |

| 40763 
| The number of orders cannot exceed the maximum amount of the corresponding gear 
| 400 
 |

| 40764 
| The remaining amount of the order is less than the current transaction volume 
| 400 
 |

| 40765 
| The remaining volume of the position is less than the current transaction volume 
| 400 
 |

| 40766 
| The number of open orders is less than this transaction volume 
| 400 
 |

| 40767 
| Position does not exist when opening a position 
| 400 
 |

| 40768 
| Order does not exist 
| 400 
 |

| 40769 
| Reject order has been completed 
| 400 
 |

| 40770 
| The settlement or fee currency configuration was not found. 
| 400 
 |

| 40771 
| When there is a gap, you cannot have a position closing order. 
| 400 
 |

| 40772 
| The account does not exist 
| 400 
 |

| 40773 
| Closed positions can only occur in two-way positions. 
| 400 
 |

| 40774 
| The order type for unilateral position must also be the unilateral position type. 
| 400 
 |

| 40775 
| The market-making account can only be a unilateral position type. 
| 400 
 |

| 40776 
| Error creating order. 
| 400 
 |

| 40777 
| Cancel order error. 
| 400 
 |

| 40778 
| Coin pair {0} does not support {1} currency as margin 
| 400 
 |

| 40779 
| Please check that the correct delegateType is used 
| 400 
 |

| 40780 
| There are multiple risk handling records for the same symbolId at the same time 
| 400 
 |

| 40781 
| The transfer order was not found 
| 400 
 |

| 40782 
| Internal transfer error 
| 400 
 |

| 40783 
| No gear found 
| 400 
 |

| 40784 
| Need to configure modify depth account 
| 400 
 |

| 40785 
| Need to configure draw line account 
| 400 
 |

| 40786 
| Duplicate clientOid 
| 400 
 |

| 40787 
| The price step does not match 
| 400 
 |

| 40788 
| Internal batch transfer error 
| 400 
 |

| 40789 
| The tokenId is duplicated in the configuration item 
| 400 
 |

| 40790 
| Duplicate symbolCode in configuration item 
| 400 
 |

| 40791 
| The baseToken or quoteToken of symbolCode does not exist 
| 400 
 |

| 40792 
| The symbol in the configuration item is duplicated 
| 400 
 |

| 40793 
| The symbolCode of BusinessSymbol does not exist 
| 400 
 |

| 40794 
| The supportMarginToken of BusinessSymbol is not configured 
| 400 
 |

| 40795 
| The transaction is suspended due to settlement or maintenance reasons 
| 400 
 |

| 40796 
| The adjusted leverage is not within the appropriate range 
| 400 
 |

| 40797 
| Exceeded the maximum settable leverage 
| 400 
 |

| 40798 
| Insufficient contract account balance 
| 400 
 |

| 40799 
| Cannot be less than the minimum transfer amount 
| 400 
 |

| 40800 
| Insufficient amount of margin 
| 400 
 |

| 40801 
| Cannot exceed the maximum transferable deposit amount 
| 400 
 |

| 40802 
| Position is zero and direct margin call is not allowed 
| 400 
 |

| 40803 
| The leverage is reduced and the amount of margin call is incorrect 
| 400 
 |

| 40804 
| The number of closed positions cannot exceed the number of positions held 
| 400 
 |

| 40805 
| Unsupported operation 
| 400 
 |

| 40806 
| Unsupported currency 
| 400 
 |

| 40807 
| The account does not exist 
| 400 
 |

| 40808 
| Parameter verification exception {0} 
| 400 
 |

| 40809 
| Execution price parameter verification exception 
| 400 
 |

| 40810 
| Triggered price parameter verification exception 
| 400 
 |

| 40811 
| The parameter {0} should not be null 
| 400 
 |

| 40812 
| The condition {0} is not met 
| 400 
 |

| 40813 
| The parameter {0} must have a value and cannot be empty 
| 400 
 |

| 40814 
| No change in leverage 
| 400 
 |

| 40815 
| The order price is higher than the highest bid price 
| 400 
 |

| 40816 
| The order price is lower than the lowest selling price 
| 400 
 |

| 40817 
| The current order status cannot be cancelled 
| 400 
 |

| 40818 
| The current order type cannot be cancelled 
| 400 
 |

| 40819 
| The order does not exist! 
| 400 
 |

| 40820 
| The order price for closing a long position is not allowed to be lower than the liquidation price 
| 400 
 |

| 40821 
| The closing order price cannot be higher than the liquidation price 
| 400 
 |

| 40822 
| The contract configuration does not exist 
| 400 
 |

| 40823 
| The transaction or reasonable marked price does not exist 
| 400 
 |

| 40824 
| Currently, it is not allowed to list market orders 
| 400 
 |

| 40825 
| Contract opponent depth does not exist 
| 400 
 |

| 40826 
| Due to excessive price fluctuations, the market order cost is insufficient, and the position opening order failed. 
| 400 
 |

| 40827 
| The bonus is not allowed to hold two-way positions 
| 400 
 |

| 40828 
| Special market making accounts cannot manually place orders 
| 400 
 |

| 40829 
| The take profit price of a long position should be greater than the average open price 
| 400 
 |

| 40830 
| The take profit price of the long position should be greater than the current price 
| 400 
 |

| 40831 
| The short position take profit price should be less than the average open price 
| 400 
 |

| 40832 
| The take profit price of short positions should be less than the current price 
| 400 
 |

| 40833 
| The stop loss price of a long position should be less than the average opening price 
| 400 
 |

| 40834 
| The stop loss price of the long position should be less than the current price 
| 400 
 |

| 40835 
| The stop loss price of the short position should be greater than the average opening price 
| 400 
 |

| 40836 
| The stop loss price of the short position should be greater than the current price 
| 400 
 |

| 40837 
| There is no position in this position, so stop-profit and stop-loss orders cannot be made 
| 400 
 |

| 40838 
| There is no position in this position, and automatic margin call cannot be set 
| 400 
 |

| 40839 
| The automatic margin call function of this contract has been suspended 
| 400 
 |

| 40840 
| Duplicate shard market making account 
| 400 
 |

| 40841 
| Online environment does not allow execution 
| 400 
 |

| 40842 
| Current configuration does not allow adjustment, please try again later 
| 400 
 |

| 40843 
| no_datasource_key_exists 
| 400 
 |

| 40844 
| This contract is under temporary maintenance 
| 400 
 |

| 40845 
| This contract has been removed 
| 400 
 |

| 40846 
| Status verification abnormal 
| 400 
 |

| 40847 
| The operation cannot be performed 
| 400 
 |

| 40848 
| Cannot open a copy transaction if there is a position 
| 400 
 |

| 40849 
| This user already has an ongoing copy 
| 400 
 |

| 40850 
| The copy is in progress, the balance cannot be transferred 
| 400 
 |

| 40851 
| Account status is wrong, cannot end copying 
| 400 
 |

| 40852 
| There are unfilled orders, cannot end the copy 
| 400 
 |

| 40853 
| There is an unexecuted plan order, cannot end the copy 
| 400 
 |

| 40854 
| This product does not support copy trading 
| 400 
 |

| 40855 
| The user has ended copying and cannot end copying again 
| 400 
 |

| 40856 
| Data abnormal 
| 400 
 |

| 40857 
| Document number error 
| 400 
 |

| 40858 
| Error tracking order status 
| 400 
 |

| 40859 
| This order is being closed and cannot be closed again 
| 400 
 |

| 40860 
| The trader does not exist and cannot be set to follow 
| 400 
 |

| 40861 
| The trader has been disabled and cannot be set to follow 
| 400 
 |

| 40862 
| Please cancel the current order 
| 400 
 |

| 40863 
| Please cancel the current plan 
| 400 
 |

| 40864 
| Please close the current position with orders 
| 400 
 |

| 40865 
| This order is being commissioned, and it is not currently supported to close the position 
| 400 
 |

| 40866 
| You are currently a trader, please close the position under the current order 
| 400 
 |

| 40867 
| Currently the maximum number of positions that can be closed is {0}, please go to the current order to close the position if the amount exceeds 
| 400 
 |

| 40868 
| You are currently a trader and currently do not support liquidation through planned orders 
| 400 
 |

| 40869 
| You are currently a trader and currently do not support modification of leverage 
| 400 
 |

| 40870 
| You are currently copying an order and currently do not support modifying the leverage 
| 400 
 |

| 40871 
| The leverage does not meet the configuration, and you cannot become a trader 
| 400 
 |

| 40872 
| Failed to adjust position, currently holding position or order or plan order 
| 400 
 |

| 40873 
| The account has a margin and needs to be transferred out 
| 400 
 |

| 40874 
| Whole position mode does not support automatic margin call 
| 400 
 |

| 40875 
| Whole position mode does not support margin adjustment 
| 400 
 |

| 40876 
| Too many tracking orders 
| 400 
 |

| 40877 
| Too many follow-up orders 
| 400 
 |

| 40878 
| The contract index data is abnormal. In order to avoid causing your loss, please try again later. 
| 400 
 |

| 40879 
| The risk is being processed, and the funds cannot be adjusted. 
| 400 
 |

| 40880 
| The risk is being processed and the leverage cannot be adjusted. 
| 400 
 |

| 40881 
| There is currently an order, or an order is planned, and the leverage cannot be adjusted. 
| 400 
 |

| 40882 
| You are currently a trader and you cannot switch to the full position mode 
| 400 
 |

| 40883 
| When the currencies are mixed, it cannot be adjusted to the warehouse-by-warehouse mode 
| 400 
 |

| 40884 
| When a one-way position is held, it cannot be adjusted to a position-by-position mode 
| 400 
 |

| 40885 
| In the case of position by position mode, it cannot be adjusted to one-way position 
| 400 
 |

| 40886 
| The automatic margin call cannot be adjusted in the full position mode 
| 400 
 |

| 40887 
| Failed to place the order, the number of single lightning open positions is at most {0} 
| 400 
 |

| 40888 
| Failed to place the order, the maximum amount of single lightning closing is {0} 
| 400 
 |

| 40889 
| The plan order of this contract has reached the upper limit 
| 400 
 |

| 40890 
| The order of stop-profit and stop-loss for this contract has reached the upper limit 
| 400 
 |

| 40891 
| Insufficient position, can not set take profit or stop loss 
| 400 
 |

| 40892 
| Failed to place the order, the minimum number of positions opened by the trader is {0} 
| 400 
 |

| 40893 
| Unable to update the leverage factor of this position, there is not enough margin! 
| 400 
 |

| 40894 
| The documentary closing has been processed 
| 400 
 |

| 40895 
| The preset price does not match the order/execution price 
| 400 
 |

| 40896 
| The default stop profit and stop loss has been partially fulfilled and cannot be modified 
| 400 
 |

| 40897 
| The system experience gold account does not exist 
| 400 
 |

| 40898 
| The system experience gold account balance is insufficient 
| 400 
 |

| 40899 
| The number of stored users exceeds the limit 
| 400 
 |

| 40900 
| The system experience gold account is inconsistent 
| 400 
 |

| 40901 
| The contract experience fund balance is insufficient 
| 400 
 |

| 40902 
| Future time is not allowed 
| 400 
 |

| 40903 
| Failed to obtain leverage information 
| 400 
 |

| 40904 
| Failed to collect funds 
| 400 
 |

| 40905 
| Failed to collect user funds 
| 400 
 |

| 40906 
| Failed to pay user funds 
| 400 
 |

| 40907 
| The payment cannot be transferred 
| 400 
 |

| 40908 
| Concurrent operation failed 
| 400 
 |

| 40909 
| Transfer processing 
| 400 
 |

| 40910 
| Operation timed out 
| 400 
 |

| 40911 
| Request timestamp expired 
| 400 
 |

| 40912 
| single cancel cannot exceed 50 
| 400 
 |

| 40913 
| {0} must be passed one 
| 400 
 |

| 40914 
| Trader the maximum leverage can use is {0} 
| 400 
 |

| 40915 
| Long position take profit price please > mark price 
| 400 
 |

| 40916 
| The business of this account has been restricted 
| 400 
 |

| 40917 
| Stop price for long positions please < mark price {0} 
| 400 
 |

| 40918 
| Traders open positions with orders too frequently 
| 400 
 |

| 40919 
| This function is not open yet 
| 400 
 |

| 40920 
| Position or order exists, the position mode cannot be switched 
| 400 
 |

| 40921 
| The order size cannot exceed the maximum size of the positionLevel 
| 400 
 |

| 40922 
| Only work order modifications are allowed 
| 400 
 |

| 40923 
| Order size and price have not changed 
| 400 
 |

| 40924 
| orderId and clientOid must have one 
| 400 
 |

| 40925 
| price or size must be passed in together 
| 400 
 |

| 43013 
| Take profit price needs> current price 
| 400 
 |

| 43014 
| Take profit price needs to be <current price 
| 400 
 |

| 43015 
| Stop loss price needs to be <current price 
| 400 
 |

| 43016 
| Stop loss price needs to be> current price 
| 400 
 |

| 43017 
| You are currently a trader and currently do not support liquidation through planned orders 
| 400 
 |

| 43020 
| Stop profit and stop loss order does not exist 
| 400 
 |

| 43021 
| The stop-profit and stop-loss order has been closed 
| 400 
 |

| 43022 
| Failed to trigger the default stop loss 
| 400 
 |

| 43023 
| Insufficient position, can not set profit or stop loss 
| 400 
 |

| 43024 
| Take profit/stop loss in an existing order, please change it after canceling all 
| 400 
 |

| 43025 
| Plan order does not exist 
| 400 
 |

| 43026 
| The planned order has been closed 
| 400 
 |

| 43027 
| The minimum order value {0} is not met 
| 400 
 |

| 43028 
| Please enter an integer multiple of {0} for price 
| 400 
 |

| 43029 
| The size of the current Order > the maximum number of positions that can be closed 
| 400 
 |

| 43030 
| Take profit order already existed 
| 400 
 |

| 43031 
| Stop loss order already existed 
| 400 
 |

| 43032 
| rangeRate is smaller than {0} 
| 400 
 |

| 43033 
| Trailing order does not exist 
| 400 
 |

| 43034 
| The trigger price should be ≤ the current market price 
| 400 
 |

| 43035 
| The trigger price should be ≥ the current market price 
| 400 
 |

| 43036 
| Trader modify tpsl can only be operated once within 300ms 
| 400 
 |

| 43037 
| The minimum order amount allowed for trading is {0} 
| 400 
 |

| 43038 
| The maximum order amount allowed for trading is {0} 
| 400 
 |

| 43039 
| Maximum price limit exceeded {0} 
| 400 
 |

| 43040 
| Minimum price limit exceeded {0} 
| 400 
 |

| 43041 
| Maximum transaction amount {0} 
| 400 
 |

| 43042 
| Minimum transaction amount {0} 
| 400 
 |

| 43043 
| There is no position 
| 400 
 |

| 43044 
| The follow order status error 
| 400 
 |

| 43045 
| The trader is ful 
| 400 
 |

| 43046 
| User does not exist 
| 400 
 |

| 43047 
| Followers are not allowed to follow again within xx minutes after being removed, please try again later! 
| 400 
 |

| 43048 
| The symbol is null 
| 400 
 |

| 43049 
| Margin coin is not allowed 
| 400 
 |

| 43050 
| Leverage exceeds the effective range 
| 400 
 |

| 43051 
| Maximum limit exceeded 
| 400 
 |

| 43052 
| Follow order count can not less than {0} 
| 400 
 |

| 43053 
| The copy ratio cannot exceed {0} 
| 400 
 |

| 43054 
| The copy ratio cannot be less than {0} 
| 400 
 |

| 43055 
| The take loss ratio must be between {0}-{1} 
| 400 
 |

| 43056 
| The take profit ratio must be between {0}-{1} 
| 400 
 |

| 43057 
| It is not allowed to bring orders or copy orders between sub-accounts 
| 400 
 |

| 43058 
| Parameter verification failed 
| 400 
 |

| 43059 
| Request failed, please try again 
| 400 
 |

| 43060 
| Sort rule must send 
| 400 
 |

| 43061 
| Sort Flag must send 
| 400 
 |

| 43062 
| not to follow 
| 400 
 |

| 43063 
| Can not follow trade with yourself 
| 400 
 |

| 43064 
| Tracking order status error 
| 400 
 |

| 43065 
| Tracking No does not exist 
| 400 
 |

| 43066 
| operation failed 
| 400 
 |

| 43067 
| The loaded data has reached the upper limit, and the maximum support for loading {0} data 
| 400 
 |

| 43068 
| The status of the current follower is abnormal and removal is not allowed for now 
| 400 
 |

| 43069 
| A follower account can only be removed when its equity is lower than {0} USDT 
| 400 
 |

| 43001 
| The order does not exist 
| 400 
 |

| 43002 
| Pending order failed 
| 400 
 |

| 43003 
| Pending order failed 
| 400 
 |

| 43004 
| There is no order to cancel 
| 400 
 |

| 43005 
| Exceed the maximum number of orders 
| 400 
 |

| 43006 
| The order quantity is less than the minimum transaction quantity 
| 400 
 |

| 43007 
| The order quantity is greater than the maximum transaction quantity 
| 400 
 |

| 43008 
| The current order price cannot be less than {0}{1} 
| 400 
 |

| 43009 
| The current order price exceeds the limit {0}{1} 
| 400 
 |

| 43010 
| The transaction amount cannot be less than {0}{1} 
| 400 
 |

| 43011 
| The parameter does not meet the specification {0} 
| 400 
 |

| 43012 
| Insufficient balance 
| 400 
 |

| 41103 
| param {0} error 
| 400 
 |

| 41101 
| param {0} error 
| 400 
 |

| 41113 
| symbol is offline 
| 400 
 |

| 41114 
| The current trading pair is under maintenance, please refer to the official announcement for the opening time 
| 400 
 |

| 42013 
| transfer fail 
| 400 
 |

| 42014 
| The current currency does not support deposit 
| 400 
 |

| 42015 
| The current currency does not support withdrawal 
| 400 
 |

| 42016 
| symbol {0} is Invalid or not supported spot trade 
| 400 
 |

| 41100 
| error {0} 
| 400 
 |

| 43111 
| param error {0} 
| 400 
 |

| 43112 
| The amount of coins withdrawn is less than the handling fee {0} 
| 400 
 |

| 43113 
| The daily limit {0} is exceeded in a single transaction 
| 400 
 |

| 43114 
| Withdrawal is less than the minimum withdrawal count {0} 
| 400 
 |

| 43115 
| The current trading pair is opening soon, please refer to the official announcement for the opening time 
| 400 
 |

| 43116 
| This chain requires a tag to withdraw coins 
| 400 
 |

| 43117 
| Exceeds the maximum amount that can be transferred 
| 400 
 |

| 43118 
| clientOrderId duplicate 
| 400 
 |

| 43119 
| Trading is not open 
| 400 
 |

| 43120 
| symbol is not open trade 
| 400 
 |

| 43121 
| Withdrawal address cannot be your own 
| 400 
 |

| 43122 
| The purchase limit of this currency is {0}, and there is still {1} left 
| 400 
 |

| 43123 
| param error {0} 
| 400 
 |

| 43124 
| withdraw step is error 
| 400 
 |

| 43125 
| No more than 8 decimal places 
| 400 
 |

| 43126 
| This currency does not support withdrawals 
| 400 
 |

| 43127 
| Sub transfer not by main account, or main/sub relationship error 
| 400 
 |

| 43128 
| Exceeded the limit of the maximum number of orders for the total transaction pair {0} 
| 400 
 |

| 45034 
| clientOid duplicate 
| 400 
 |

| 47001 
| Currency recharge is not enabled 
| 400 
 |

| 47002 
| Address verification failed 
| 400 
 |

| 45001 
| Unknown error 
| 400 
 |

| 45002 
| Insufficient asset 
| 400 
 |

| 45003 
| Insufficient position 
| 400 
 |

| 45004 
| Insufficient lock-in asset 
| 400 
 |

| 45005 
| Insufficient available positions 
| 400 
 |

| 45006 
| Insufficient position 
| 400 
 |

| 45007 
| Insufficient lock position 
| 400 
 |

| 45008 
| No assets 
| 400 
 |

| 45009 
| The account is at risk and cannot perform trades temporarily 
| 400 
 |

| 45010 
| The number of orders cannot exceed the maximum amount of the corresponding leverage 
| 400 
 |

| 45011 
| Order remaining volume < Current transaction volume 
| 400 
 |

| 45012 
| Remaining volume of position < Volume of current transaction 
| 400 
 |

| 45013 
| The number of open orders < Current transaction volume 
| 400 
 |

| 45014 
| Position does not exist during opening 
| 400 
 |

| 45017 
| Settlement or the coin for transaction configuration not found 
| 400 
 |

| 45018 
| In the case of a netting, you cannot have a liquidation order 
| 400 
 |

| 45019 
| Account does not exist 
| 400 
 |

| 45020 
| Liquidation can only occur under two-way positions 
| 400 
 |

| 45021 
| When one-way position is held, the order type must also be one-way position type 
| 400 
 |

| 45023 
| Error creating order 
| 400 
 |

| 45024 
| Cancel order error 
| 400 
 |

| 45025 
| The currency pair does not support the currency as a margin 
| 400 
 |

| 45026 
| Please check that the correct delegateType is used 
| 400 
 |

| 45031 
| The order is finalized 
| 400 
 |

| 45035 
| Price step mismatch 
| 400 
 |

| 45043 
| Due to settlement or maintenance reasons, the trade is suspended 
| 400 
 |

| 45044 
| Leverage is not within the suitable range after adjustment 
| 400 
 |

| 45045 
| Exceeds the maximum possible leverage 
| 400 
 |

| 45047 
| Reduce the leverage and the amount of additional margin is incorrect 
| 400 
 |

| 45051 
| Execution price parameter verification is abnormal 
| 400 
 |

| 45052 
| Trigger price parameter verification anbormal 
| 400 
 |

| 45054 
| No change in leverage 
| 400 
 |

| 45055 
| The current order status cannot be cancelled 
| 400 
 |

| 45056 
| The current order type cannot be cancelled 
| 400 
 |

| 45057 
| The order does not exist! 
| 400 
 |

| 45060 
| TP price of long position > Current price {0} 
| 400 
 |

| 45061 
| TP price of short position < Current price {0} 
| 400 
 |

| 45062 
| SL price of long position < Current price {0} 
| 400 
 |

| 45064 
| TP price of long position > order price {0} 
| 400 
 |

| 45065 
| TP price of short position < order price {0} 
| 400 
 |

| 45066 
| SL price of long position < order price {0} 
| 400 
 |

| 45067 
| SL price of short position > order price {0} 
| 400 
 |

| 45068 
| There is no position temporarily, and the order of TP and SL cannot be carried out 
| 400 
 |

| 45075 
| The user already has an ongoing copy trade 
| 400 
 |

| 45082 
| Copy trade number error 
| 400 
 |

| 45089 
| You are currently copy trading, leverage cannot be changed 
| 400 
 |

| 45091 
| Too many tracking orders 
| 400 
 |

| 45097 
| There is currently an order or a limit order, and the leverage cannot be adjusted 
| 400 
 |

| 45098 
| You are currently a trader and cannot be switched to the full position mode 
| 400 
 |

| 45099 
| When there are different coins, it cannot be adjusted to Isolated Margin mode 
| 400 
 |

| 45100 
| When a one-way position is held, it cannot be adjusted to the Isolated Margin mode 
| 400 
 |

| 45101 
| In Isolated Margin mode, it cannot be adjusted to a one-way position 
| 400 
 |

| 45102 
| In the full position mode, the automatic margin call cannot be adjusted 
| 400 
 |

| 45103 
| Failed to place the order, the maximum amount of single flash opening position is %s 
| 400 
 |

| 45104 
| Failed to place the order, the maximum amount of single flash closing position is %s 
| 400 
 |

| 45106 
| copy trade liquidation has been processed 
| 400 
 |

| 45107 
| API is restricted to open positions. If you have any questions, please contact our customer service 
| 400 
 |

| 45108 
| API is restricted to close position. If you have any questions, please contact our customer service 
| 400 
 |

| 45109 
| The current account is a two-way position 
| 400 
 |

| 45110 
| less than the minimum amount {0} USDT 
| 400 
 |

| 45111 
| less than the minimum order quantity 
| 400 
 |

| 45112 
| more than the maximum order quantity 
| 400 
 |

| 45113 
| Maximum order value limit triggered 
| 400 
 |

| 45114 
| The minimum order requirement is not met 
| 400 
 |

| 45115 
| The price you enter should be a multiple of {0} 
| 400 
 |

| 45116 
| The count of positions hold by the account exceeds the maximum count {0} 
| 400 
 |

| 45117 
| Currently holding positions or orders, the margin mode cannot be adjusted 
| 400 
 |

| 45118 
| Reached the upper limit of the order of transactions (the current number of order + the current number of orders) {0} 
| 400 
 |

| 45119 
| This symbol does not support position opening operation 
| 400 
 |

| 45120 
| size > max can open order size 
| 400 
 |

| 45121 
| The reasonable mark price deviates too much from the market, and your current leveraged position opening risk is high 
| 400 
 |

| 45122 
| Short position stop loss price please > mark price {0} 
| 400 
 |

| 45123 
| Insufficient availability, currently only market orders can be placed 
| 400 
 |

| 45124 
| Please edit and submit again. 
| 400 
 |

| 45125 
| Order cancellation is unavailable for inactive orders. Please cancel parent order and place a new order. 
| 400 
 |

| 45126 
| Order cancellation is unavailable for inactive orders. Please cancel parent order and place a new order. 
| 400 
 |

| 45127 
| Position brackets disabled TP SL 
| 400 
 |

| 45128 
| Position brackets disabled modify qty 
| 400 
 |

| 45129 
| Cancel order is too frequent, the same orderId is only allowed to be canceled once in a second 
| 400 
 |

| 47003 
| Withdraw address is not in addressBook 
| 400 
 |

| 49000 
| apiKey and userId mismatch 
| 400 
 |

| 49001 
| not custody account, operation deny 
| 400 
 |

| 49002 
| missing http header: ACCESS-BROKER-KEY or ACCESS-BROKER-SIGN 
| 400 
 |

| 49003 
| illegal IP, access deny 
| 400 
 |

| 49004 
| illegal ACCESS-BROKER-KEY 
| 400 
 |

| 49005 
| access deny: sub account 
| 400 
 |

| 49006 
| ACCESS-BROKER-SIGN check sign fail 
| 400 
 |

| 49007 
| account is unbound 
| 400 
 |

| 49008 
| account is bound 
| 400 
 |

| 49009 
| clientUserId check mismatch with the bound user ID 
| 400 
 |

| 49010 
| account: {0} still have assets: {1} 
| 400 
 |

| 49011 
| kyc must be done before bind 
| 400 
 |

| 49020 
| unsupported coin 
| 400 
 |

| 49021 
| operation accepted 
| 400 
 |

| 49022 
| access deny 
| 400 
 |

| 49023 
| insufficient fund 
| 400 
 |

| 49024 
| {0} decimal precision error 
| 400 
 |

| 49025 
| Parameter mismatch with the initial requestId, request body: {0} 
| 400 
 |

| 49026 
| {0} maximum {1} digits 
| 400 
 |

| 49030 
| custody account, operation deny 
| 400 
 |

| 49040 
| Unknown Error 
| 400 
 |

| 60001 
| StartTime not empty 
| 400 
 |

| 60002 
| MerchantId not empty 
| 400 
 |

| 60003 
| Not found the p2p order 
| 400 
 |

| 60004 
| Not found the p2p advertisement 
| 400 
 |

| 60005 
| Not found the p2p merchant 
| 400 
 |

| 70001 
| Activity ID not correct 
| 400 
 |

| 70002 
| rankType error 
| 400 
 |

| 40000 
| Bitget is providing services to many countries and regions around the world and strictly adheres to the rules and regulatory requirements of each country and region. According to the relevant regulations, Bitget is currently unable to provide services to your region (Mainland China) and you do not have access to open positions.Apologies for any inconvenience caused! 
| 400 
 |

| 48001 
| Parameter validation failed {0} 
| 400 
 |

| 48002 
| Missing request Parameter 
| 400 
 |

| 46013 
| This symbol limits the selling amount{0}，Remaining{0} 
| 400 
 |

| 40404 
| Request URL NOT FOUND 
| 400 
 |

| 50010 
| Unknown error 
| 400 
 |

| 50012 
| The account has been suspended or deleted. Please contact our Customer Support 
| 400 
 |

| 50013 
| The account has been suspended and deleted. Please contact our Customer Support 
| 400 
 |

| 50019 
| The user is forbidden to trade. 
| 400 
 |

| 50059 
| This currency cannot be transferred 
| 400 
 |

| 50052 
| The asset balance will be less than 0 after transferring 
| 400 
 |

| 50048 
| The maximum number of orders is exceeded 
| 400 
 |

| 50046 
| The price is too low 
| 400 
 |

| 50047 
| The price is too high 
| 400 
 |

| 50026 
| The trading pair is currently unavailable 
| 400 
 |

| 50025 
| The trading pair is currently unavailable 
| 400 
 |

| 50016 
| The number of open orders is smaller than the minimum limit of the trading pair 
| 400 
 |

| 50017 
| The number of open orders is bigger than the maximum limit of the trading pair 
| 400 
 |

| 50023 
| The account has been suspended due to abnormal behavior. Please contact our Customer Support is you have any questions. 
| 400 
 |

| 50031 
| System error 
| 400 
 |

| 50044 
| The system account is not found 
| 400 
 |

| 50049 
| The request body of the system user is empty 
| 400 
 |

| 50050 
| The system loan collection has been done 
| 400 
 |

| 50027 
| The trading pair is suspended for maintenance 
| 400 
 |

| 50030 
| The trading pair will soon be available 
| 400 
 |

| 50029 
| The trading pair has no order price 
| 400 
 |

| 50028 
| The trading pair is removed 
| 400 
 |

| 50040 
| The repayment amount must be more than 0 
| 400 
 |

| 50042 
| The repayment amount must be more than the interest 
| 400 
 |

| 50041 
| The repayment amount must be less than your available balance 
| 400 
 |

| 50051 
| The user in reconciliation is not in the system (cache) 
| 400 
 |

| 50024 
| The trading pair does not exist 
| 400 
 |

| 50011 
| Parameter verification error 
| 400 
 |

| 50053 
| The amount is less than 0 when making loan repayment 
| 400 
 |

| 50056 
| The amount is less than 0 when paying liquidation fees 
| 400 
 |

| 50054 
| The amount is less than 0 when making interest repayment 
| 400 
 |

| 50055 
| The amount is less than 0 when paying trading fees 
| 400 
 |

| 50033 
| The topic of the websocket query does not exist 
| 400 
 |

| 50057 
| The amount is less than 0 when paying the excessive loss resulted from liquidation 
| 400 
 |

| 50032 
| The currency does not exist 
| 400 
 |

| 50036 
| The loan configuration does not exist 
| 400 
 |

| 50037 
| This currency cannot be borrowed 
| 400 
 |

| 50038 
| The system limit is exceeded 
| 400 
 |

| 50034 
| The borrowing amount must be over 0.00000001 
| 400 
 |

| 50035 
| The maximum borrowing amount is exceeded 
| 400 
 |

| 50020 
| Insufficient balance 
| 400 
 |

| 50045 
| Insufficient locked asset 
| 400 
 |

| 50015 
| Currently, sub-accounts cannot engage in margin trading 
| 400 
 |

| 50021 
| The margin trading account does not exist 
| 400 
 |

| 50022 
| The account is liquidated 
| 400 
 |

| 50014 
| The account already exists 
| 400 
 |

| 50060 
| Duplicated clientOid 
| 400 
 |

| 50058 
| After the profit is used to cover the excessive loss resulted from liquidation, the balance will be less than 0 
| 400 
 |

| 50039 
| The currency and the trading pair do not match 
| 400 
 |

| 50018 
| The price must be 0 or higher 
| 400 
 |

| 50043 
| Unknown transaction type 
| 400 
 |

| 50061 
| There is a problem with the parameter you requested 
| 400 
 |

| 50062 
| The order status is cancelled or fullFill 
| 400 
 |

| 50063 
| Token precision must less than or equal to eight 
| 400 
 |

| 50064 
| Your account is temporarily frozen. Please contact customer support if you have any questions 
| 400 
 |

| 50065 
| symbol_off_shelf 
| 400 
 |

| 50066 
| Position closing, please try again later 
| 400 
 |

| 31001 
| The user is not a trader 
| 400 
 |

| 31002 
| Condition {0} is not satisfied 
| 400 
 |

| 31003 
| Parameter {0} must have a value, cannot be empty 
| 400 
 |

| 31004 
| Take profit price must be > current price 
| 400 
 |

| 31005 
| Stop loss price must be < current price 
| 400 
 |

| 31006 
| The order is in the process of being placed, closing of the position is not supported at the moment 
| 400 
 |

| 31007 
| Order does not exist 
| 400 
 |

| 31008 
| There is no position in this position, no take profit or stop loss order can be made 
| 400 
 |

| 31009 
| Tracking order status error 
| 400 
 |

| 31010 
| Clear user prompt 
| 400 
 |

| 31011 
| The order is not completely filled and the order is closed prompting the cancellation of the commission 
| 400 
 |

| 31012 
| Pullback greater than {0} 
| 400 
 |

| 31013 
| Pullback range is less than {0} 
| 400 
 |

| 31014 
| Stop gain yield greater than {0} 
| 400 
 |

| 31015 
| Stop loss yield less than {0} 
| 400 
 |

| 31016 
| Batch execution exception 
| 400 
 |

| 31017 
| Maximum price limit exceeded {0} 
| 400 
 |

| 31018 
| Minimum price change of {0} 
| 400 
 |

| 31019 
| Support trading currency pair does not exist 
| 400 
 |

| 31020 
| Business is restricted 
| 400 
 |

| 31021 
| The currency pair is not available for trading, please select another currency pair 
| 400 
 |

| 31022 
| Minimum order size for this trading area is not met, please select another trading area 
| 400 
 |

| 31023 
| Ending order processing 
| 400 
 |

| 31024 
| The order is not completely filled, please go to \"Spot trading\"-\"Current orders\" to cancel the order and then sell or close the operation! 
| 400 
 |

| 31025 
| The user is not a trader 
| 400 
 |

| 31026 
| The user is not exist 
| 400 
 |

| 31027 
| Operation failed, please try again 
| 400 
 |

| 31028 
| Parameter verification failed 
| 400 
 |

| 31029 
| User is not existed 
| 400 
 |

| 31030 
| Chosen trading pair is empty 
| 400 
 |

| 31031 
| You’re log in as trader,can not follow trade 
| 400 
 |

| 31032 
| Can not follow trade with yourself 
| 400 
 |

| 31033 
| Fail to remove 
| 400 
 |

| 31034 
| This trader’s no. of follower has reached limit, please select other trader 
| 400 
 |

| 31035 
| Follow order ratio can not less than{0} 
| 400 
 |

| 31036 
| Follow order ratio can not greater than{0} 
| 400 
 |

| 31037 
| Follow order count can not less than{0} 
| 400 
 |

| 31038 
| Exceeds max. limit 
| 400 
 |

| 31039 
| Can not set reminder as your Elite Trader status has been revoked 
| 400 
 |

| 31040 
| T/P ratio must between {0}%%-{1}%% 
| 400 
 |

| 31041 
| S/L ratio must between {0}%%-{1}%% 
| 400 
 |

| 31042 
| The status of your Elite Trader has been suspended, please contact online customer service to resume. 
| 400 
 |

| 31043 
| Your copy trade follower cap is too high. Please contact customer support to lower it if you want to enable this function! 
| 400 
 |

| 31044 
| You are applying to become a trader now. Copying trade is not allowed 
| 400 
 |

| 31045 
| The max. quantity for TP/SL is {0}. For any quantity exceeding this limit, please operate under “Initiated Copies”. 
| 400 
 |

| 31046 
| No copy trade relationship is allowed between a parent account and its sub-account 
| 400 
 |

| 31047 
| No copying is allowed within {0} minutes after the copier has been removed. Please try again later. 
| 400 
 |

| 31048 
| Only this trader's referrals are allowed to follow this trader at the moment. Please create an account with the trader's referral link! 
| 400 
 |

| 31049 
| The trader's status is abnormal or has been revoked, and cannot be viewed at this time! 
| 400 
 |

| 31050 
| This trader UID is already set for the region. 
| 400 
 |

| 31051 
| traderUserId error 
| 400 
 |

| 31052 
| Cannot set trading symbol that have not been opened by traders. 
| 400 
 |

| 31053 
| executePrice cannot exceed triggerPrice 的{0} 
| 400 
 |

| 31054 
| No order to cancel 
| 400 
 |

| 20001 
| startTime should be less than endTime 
| 400 
 |

| 22001 
| No order to cancel 
| 400 
 |

| 22002 
| No position to close 
| 400 
 |

| 22003 
| modify price and size, please pass in newClientOid 
| 400 
 |

| 22004 
| This symbol {0} not support API trade 
| 400 
 |

| 22005 
| This symbol does not support  cross mode 
| 400 
 |

| 22006 
| limit price > risk price 
| 400 
 |

| 22007 
| limit price < risk price 
| 400 
 |

| 22008 
| market price > risk price 
| 400 
 |

| 22009 
| market price < risk price 
| 400 
 |

| 22010 
| Please bind ip whitelist address 
| 400 
 |

| 40100 
| Due to regulatory requirements, Hong Kong IPs are required to complete identity verification first 
| 400 
 |

| 40101 
| Please complete KYC 
| 400 
 |

| 00001 
| startTime and endTime interval cannot be greater than 366 days 
| 400 
 |

| 12001 
| {0} can be used at most 
| 400 
 |

| 12002 
| Current currency {0}, limit net sell value {1} USD 
| 400 
 |

| 12003 
| Current currency {0}, limit net buy value {1} USD 
| 400 
 |

| 13001 
| Withdraw is too frequent 
| 400 
 |

| 13002 
| Currency does not exist 
| 400 
 |

| 13003 
| Withdrawal exceeds the monthly limit 
| 400 
 |

| 13004 
| Your remaining withdrawal amount{0} 
| 400 
 |

| 13005 
| Failed to generate address 
| 400 
 |

| 60006 
| Parameter error 
| 400 
 |

| 60007 
| upload image cannot exceed 5M 
| 400 
 |

| 60008 
| The image format must be [". jpg", ". jpeg", ". png"] 
| 400 
 |

| 60009 
| The image format error 
| 400 
 |

| 60010 
| upload error 
| 400 
 |

| 60011 
| Ordinary users can not post ads 
| 400 
 |

| 60012 
| Please change your status from offline to online before posting your ads！ 
| 400 
 |

| 60013 
| Insufficient balance 
| 400 
 |

| 60014 
| Fiat info not found 
| 400 
 |

| 60015 
| Digital currency info not found 
| 400 
 |

| 60016 
| Only supports publish CNY advertisement 
| 400 
 |

| 60017 
| Not support publish CNY advertisement 
| 400 
 |

| 60018 
| Your KYC certification only supports publishing {0} 
| 400 
 |

| 60019 
| Post failed. Unable to obtain preference price 
| 400 
 |

| 60020 
| advertisement type error 
| 400 
 |

| 60021 
| Payment method is empty 
| 400 
 |

| 60022 
| Trading amount incorrect 
| 400 
 |

| 60023 
| Beyond fiat limit ({0}-{1}) 
| 400 
 |

| 60024 
| Fund reconciliation errors 
| 400 
 |

| 60025 
| The remark length cannot be longer than the configuration length 
| 400 
 |

| 60026 
| Exclusive country error 
| 400 
 |

| 60027 
| Payment time limit error 
| 400 
 |

| 60028 
| Payment method error 
| 400 
 |

| 60029 
| publish advertisement error 
| 400 
 |

| 60030 
| status error 
| 400 
 |

| 60031 
| The advertisement number is too long 
| 400 
 |

| 60032 
| The advertisement not exist 
| 400 
 |

| 60033 
| Posted ad amount incorrect 
| 400 
 |

| 60034 
| Number of images attached in the remark cannot exceed the allocation limit. 
| 400 
 |

| 60035 
| Edit advertisement error 
| 400 
 |

| 60036 
| payTimeLimit cannot be empty 
| 400 
 |

| 60037 
| Post failed. Price is significantly deviated from preference price 
| 400 
 |

| 60038 
| Post failed. Incorrect floating rate 
| 400 
 |

| 60039 
| User does not exist 
| 400 
 |

| 60040 
| Unauthorized access not supported 
| 400 
 |

| 60041 
| Edit advertisement price error 
| 400 
 |

| 60042 
| limitPrice not empty 
| 400 
 |

| 60043 
| The advertisement status update fail 
| 400 
 |

| 60044 
| The advertisement status in editing can be edited 
| 400 
 |

| 60045 
| Exceeding the number of advertisement that can be published 
| 400 
 |

| 60046 
| priceValue not empty 
| 400 
 |

| 60047 
| userPayMethodId not empty 
| 400 
 |

| 40926 
| Your identity authentication is still under review. Please wait for the review to pass before trying this function again 
| 400 
 |

| 13007 
| The current currency is {0}, and the net purchase value of {1} USD is limited within 24 hours, and the net purchase value of {2} USD is also allowed for {3} 
| 400 
 |

| 11000 
| withdraw address is not in addressBook 
| 400 
 |

| 40103 
| based on your IP address , it appears that you are located in a country or region where we are currently unable to provide services 
| 400 
 |

| 40104 
| Unable to withdraw to this account Please make sure this is a valid and verified account 
| 400 
 |

| 30001 
| Minimum Price Change {0} % 
| 400 
 |

| 40928 
| Risk control, currently your max open size is {0} {1}. The size was calculated with all the main-sub accounts 
| 400 
 |

| 47003 
| Withdraw address is not in addressBook 
| 400 
 |

| 13008 
| A single withdrawal exceeds the maximum limit 
| 400 
 |

| 13009 
| Exceeds withdrawal daily limit 
| 400 
 |

| 32038 
| The sell price cannot be lower than the trigger price percent{0} 
| 400 
 |

# WebSocket error code

| 

| Error Message 
| Error Code 
 |

| Channel does not exist 
| 30001 
 |

| Illegal request 
| 30002 
 |

| Invalid op 
| 30003 
 |

| User needs to log in 
| 30004 
 |

| Login failed 
| 30005 
 |

| request too many 
| 30006 
 |

| request over limit,connection close 
| 30007 
 |

| Invalid ACCESS_KEY 
| 30011 
 |

| Invalid ACCESS_PASSPHRASE 
| 30012 
 |

| Invalid ACCESS_TIMESTAMP 
| 30013 
 |

| Request timestamp expired 
| 30014 
 |

| Invalid signature 
| 30015 
 |

| Param error 
| 30016 
 |

  