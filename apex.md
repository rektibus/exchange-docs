We have language bindings in Shell, Python! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

General
v3.0.0

API Resources and Support Channels
Home - Access and manage your trades.
OpenApi-SDK for v3
- OpenApi-Python-SDK - Official OpenApi Python SDK
- OpenApi-Node.JS-SDK - Official OpenApi Node JS SDK
OpenApi-Demo
- Apex API Demo — We provide demos in three languages for your reference, and we will continue to update them.
Telegram - Discussion Chat Group
Discord - Official Discussion Discord Group
Twitter - Official Twitter Channel
REST Base Endpoint
Testnet:
https://testnet.omni.apex.exchange/api/

Mainnet:
https://omni.apex.exchange/api/

Websocket Endpoint
Timestamp = Current Unix Timestamp

Testnet:
Public Websocket API
wss://qa-quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232

Private Websocket API
wss://qa-quote.omni.apex.exchange/realtime_private?v=2&timestamp=1661415017233

Mainnet:
Public Websocket API
wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232

Private Websocket API
wss://quote.omni.apex.exchange/realtime_private?v=2&timestamp=1661415017233

Testnet
ApeX Omni's testnet can be found on https://testnet.omni.apex.exchange, built on the BNB test chain or base sepolia test chain.
You can obtain assets for use on the testnet via the faucet here https://testnet.omni.apex.exchange/faucet.
ApeX Omni's USDT Token Address (BNB test chain): 0x01CB59F3C16FAfe63955e4d435adAFa23d9aBBde
ApeX Omni's USDT Token Address (base sepolia test chain): 0x2340C88808dcE139B36864970074315BCb0c9Fe0
Development
apex omni is being actively developed, and new API changes should arrive on apex omni very quickly. apex omni uses requests and websocket for its methods, alongside other built-in modules. Anyone is welcome to branch/fork the repository and add their own upgrades. If you think you've made substantial improvements to the module, submit a pull request and we'll gladly take a look.
Multi-Chain Deposits and Withdrawals
ApeX Omni supports deposits and withdrawals on 5 different chains: Ethereum, BNB Chain, Base, Mantle and Arbitrum with more supported chains and supported tokens coming soon.

To trade on ApeX Omni, deposit in your Omni funding account and transfer funds to Perps account or Spot account.

Cross Collateral supports
Cross Collateral now supports 8 tokens: $USDC, $WBTC, $WETH, $ETH, $cmETH, $mETH, $cbBTC and $USDe. All of this tokens can be deposited on ApeX Omni alongside USDT. Learn more about cross collateral here: https://apex-pro.gitbook.io/apex-pro/apex-omni-live-now/omni-perps/cross-collateral

Query path and Parameters:
You must include ApeX Omni's version number in the url path, e.g. v3.
The parameter "url path" is not case-sensitive and lower case letters will be displayed by default. The en-dash (-) can be used as spaces between individual words.
The HTTP endpoint parameters are in camel case, opening with lower case letters.
Due to different time zones with time parameters, please use int64 across all instances by default.
Randomly generated id and numbers may be long in length and considering that the js display may be intercepted, these will be reflected as a string by default
For customized request headers, please enter key in upper case and use the en-dash (-) as spaces between individual words.
Http Get Request
Please add parameters to the query path.as
https://omni.apex.exchange/api/v3/transfers?limit=100&page=1&currencyId=USDC&chainIds=1

Http Post Request
Enter order data in body, in the content-type x-www-form-urlencoded. You do not need to encode your data. as l2Key=xxx&ethAddress=yyy&chainId=zzz

All requests made to private endpoints must be authenticated. The following signatures must be used for authentication:

1. ApiKey Signature
An apiKey signature is required for all private API endpoints
Users can obtain and save their public and private apiKey via wallet signature verification on ApeX Omni desktop or app
API trading users can utilize python-sdk to generate the private and public key pair for apiKey and save them for future API requests, refer to python sdk
Generate apiKey

from apexomni.constants import APEX_OMNI_HTTP_MAIN, NETWORKID_OMNI_MAIN_ARB, NETWORKID_MAIN

print("Hello, Apex Omni")
priKey = "your eth private key"

client = HttpPrivate_v3(APEX_OMNI_HTTP_MAIN, network_id=NETWORKID_MAIN, eth_private_key=priKey)
configs = client.configs_v3()

zkKeys = client.derive_zk_key(client.default_address)
print(zkKeys)
print(zkKeys['seeds'])
print(zkKeys['l2Key'])
print(zkKeys['pubKeyHash'])

nonceRes = client.generate_nonce_v3(refresh="false", l2Key=zkKeys['l2Key'],ethAddress=client.default_address, chainId=NETWORKID_OMNI_MAIN_ARB)

regRes = client.register_user_v3(nonce=nonceRes['data']['nonce'],l2Key=zkKeys['l2Key'], seeds=zkKeys['seeds'],ethereum_address=client.default_address)

print(regRes['data']['apiKey']['key'])
print(regRes['data']['apiKey']['secret'])
print(regRes['data']['apiKey']['passphrase'])

time.sleep(10)
accountRes = client.get_account_v3()
print(accountRes)

#back zkKeys, apiKey,and accountId for private Api or create-order transfer or withdraw

print(regRes['data']['apiKey'])

changeRes = client.change_pub_key_v3(chainId=NETWORKID_OMNI_MAIN_ARB, seeds=zkKeys.get('seeds'), ethPrivateKey=priKey, zkAccountId = accountRes.get('spotAccount').get('zkAccountId'), subAccountId = accountRes.get('spotAccount').get('defaultSubAccountId'),
                                     newPkHash = zkKeys.get('pubKeyHash'),  nonce= accountRes.get('spotAccount').get('nonce'), l2Key= zkKeys.get('l2Key'))
print(changeRes)

time.sleep(10)
accountRes = client.get_account_v3()
print(accountRes)
Signature content message includes timeStamp + method + path + dataString
message = timeStamp + method + path + dataString

Get Requests: dataString content is not required, append query parameters in the path message = timeStamp + method + path

Post Requests: Request body is saved in dataString content. To ensure proper sorting for parameters within the request body, parameters will be sorted by alphabetical order, refer to python sdk

Sign request message by apiSecret

def sign(
        self,
        request_path,
        method,
        iso_timestamp,
        data,
):
    sortedItems=sorted(data.items(),key=lambda x:x[0],reverse=False)
    dataString = '&'.join('{key}={value}'.format(
        key=x[0], value=x[1]) for x in sortedItems if x[1] is not None)

    message_string = (
            iso_timestamp +
            method +
            request_path +
            dataString
    )

    hashed = hmac.new(
        base64.standard_b64encode(
            (self.api_key_credentials['secret']).encode(encoding='utf-8'),
        ),
        msg=message_string.encode(encoding='utf-8'),
        digestmod=hashlib.sha256,
    )
    return base64.standard_b64encode(hashed.digest()).decode()
Place signature content, apiKey and related information in the request header
Parameter	Position	Type	Type	Comment
APEX-SIGNATURE	header	string	true	signstr
APEX-TIMESTAMP	header	string	true	request timeStamp
APEX-API-KEY	header	string	true	key
APEX-PASSPHRASE	header	string	true	passphrase
2. ZkKeys Signature
Fastest path (recommended): use our official Python SDK to generate and persist your l2Key and seeds for future API requests — see ApeX Pro OpenAPI · Python SDK.
Users can also obtain and persist l2Key and seeds via wallet signature verification on ApeX Omni (desktop/app).
Alternative (more involved): if you prefer to self-implement via third-party SDKs or raw API signing, you will need to handle message selection, wallet signing, signature normalization to seeds, ZK key derivation, and payload signing yourself (see Self-signing with the third-party ZkLink SDK below).
For orders, transfers, and withdrawals, two signatures are required:

Signature	Where it lives	Purpose	Protects
apiKey	HTTP headers (APEX-SIGNATURE, APEX-TIMESTAMP, APEX-API-KEY, APEX-PASSPHRASE)	Authenticate the client and prevent replay	Method, path, timestamp, (optionally) body digest
zkKeys	Request body (payload signature)	Prove the user approved the exact trading parameters under L2 rules	Price, size, side, symbol, expiration, etc.
Self-signing with the third-party ZkLink SDK
Choose the SDK for your target language. You can build from source (see README build steps) or download a prebuilt from Releases.
Create seeds by signing this onboarding message (EIP-191 personal_sign / signMessage), byte-for-byte: > ApeX Omni Mainnet or ApeX Omni Testnet
> Address: {0xYourEthereumAddress}
> Action: ApeX Omni Onboarding
Derive keys with the SDK: initialize signer from seeds (hex, lowercase, no 0x), then read l2Key and pubKeyHash. Persist seeds/l2Key for reuse.
Tip: See the Python example in the right panel (switch the language tab to python). If you need a more detailed zk signing example, refer to Apex API Demo, where we provide implementations in multiple languages.

Client_id and Nonce Generation
When creating order and withdrawal requests, you will need to send a unique and randomly generated client_Id to server. You can refer to python codes:

def random_client_id():
   return str(int(float(str(random.random())[2:])))
When utilizing zkKeys signatures in creating order and withdrawal requests, you will need to change client_Id to nonce and slotId in the server. Refer to python codes for the algorithm:

message = hashlib.sha256()
        message.update(clientId.encode())  # Encode as UTF-8.
        nonceHash = message.hexdigest()
        nonceInt = int(nonceHash, 16)

        maxUint32 = np.iinfo(np.uint32).max
        maxUint64 = np.iinfo(np.uint64).max

        slotId = (nonceInt % maxUint64)/maxUint32
        nonce = nonceInt % maxUint32
        accountId = int(accountId, 10) % maxUint32
Margin
On ApeX Omni, USDT is the default settleCurrency for all available contracts on the platform. The tick size for USDT is set by default to 6 decimal points.
Every contract will have an initialMarginRate and maintenanceMarginRate.
initialMarginRate (IMR): The margin required to open a position and is based on the position size and leverage.
maintenanceMarginRate (MMR): The minimum amount required for holding a leveraged position
Margin required for each single position:

initialMargin = abs（Size * Oracle Price* initialMarginRate）
maintenanceMargin = abs（Size * Oracle Price* maintenanceMarginRate）
Margin required by all positions under all contract types under your account:

total initialMargin = Σ abs（Size * Oracle Price* initialMarginRate） 
total maintenanceMargin = Σ abs（Size * Oracle Price* maintenanceMarginRate）
TotalAccountValue =Q+Σ abs（Size*Oracle Price）
where Q is the USDT balance in your account.
Liquidation
When the net equity of the account falls below the maintenance margin required, your position will be taken over by the liquidation engine and liquidated.

Funding Fee
Funding fees will be exchanged between long and short position holders every 1 hour.
Please note that the funding rate will fluctuate in real time every 1 hour. If the funding rate is positive upon settlement, long position holders will pay the funding fees to short position holders. Similarly, when the funding rate is negative, short positive holders will pay long position holders.

Funding Fees = Position Value * Index Price * Funding Rate 
Index Price
ApeX Pro utilizes Index Price in the following case(s):

User Balance
Liquidation Price
Profits and Losses
Funding Fees
Index Price is the sum of prices pulled from multiple crypto spot exchanges, then calculated based on weighted average. It is also used to derive funding fees.

Rate Limits
IP Rate Limit
If you receive a HTTP 403 (Access Denied) response, your IP has been either temporarily or permanently banned. You should immediately review the below guidelines to ensure that your application does not continue to violate the limit.

Limit	Comment
Limit 600 requests per 60 secs	Per IP
API Rate Limit
Rate Limits for All Private Endpoints Per Account

Limit	Comment
300 requests per 60 secs	POST request
600 requests per 60 secs	GET request
Orders Limit
Rate Limits for Creating Orders

Limit	Comment
200 orders	Per user
User
v3.0.0
The API endpoints of User require authentication.

POST Generate nonce
POST /v3/generate-nonce

Generate and obtain nonce before registration. The nonce is used to assemble the signature field upon registration.

curl https://omni.apex.exchange/api/v3/generate-nonce -X POST -d 'l2Key={l2Key}&ethAddress={ethAddress}&chainId={chainId}'
Request Parameters
Parameter	Position	Type	Required	Comment
body	body	object	false	none
» l2Key	body	string	true	User's l2Key of zkKeys
» ethAddress	body	string	true	User's Ethereum address
» chainId	body	string	true	API trading users to enter "9"(NETWORKID_MAIN) on mainnet
Successful Response Generation

{
  "data": {
    "nonce": "1123940951220551680",
    "nonceExpired": 1648727402292
  }
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» nonce	string	true	none	nonce
» nonceExpired	integer	true	none	The time at which nonce expires, please complete registration before this time
POST Registration & Onboarding
POST /v3/onboarding

Consolidate onboarding data and generate digital signature via your wallet. You can refer to python sdk, derive_zk_key for more information
Create your zkKey pair with your signature, including (seeds, l2Key, pubKeyHash）
Send consolidated onboarding data request to the server for response to user registration data, including API keys
curl https://omni.apex.exchange/api/v3/onboarding -H 'APEX-SIGNATURE: ***' -H 'APEX-ETHEREUM-ADDRESS: ***' -X POST -d 'l2Key={l2Key}&ethereumAddress={ethereumAddress}&referredByAffiliateLink={referredByAffiliateLink}&country={country}'
changePubKeyStatus (
    INIT                   // ini 
    REGISTERING            //registering (waiting for l2 execute)
    UN_CHANGE_PUB_KEY          // un ChangePubKey
    PROCESSING             // ChangePubKey in progress
    FINISH                 // ChangePubKey is finished
)

Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Onboarding signature
APEX-ETHEREUM-ADDRESS	header	string	true	Ethereum address
body	body	object	false	none
» l2Key	body	string	true	Public l2Key associated with the zkKeys you created.
» ethereumAddress	body	string	true	Ethereum address associated with the user being created.
» referredByAffiliateLink	body	string	false	Referred affiliate link
» country	body	string	false	Country code: Must be ISO 3166-1 Alpha-2 compliant
Successful Response Generation

{
  "apiKey": {
    "apiKey": "d4fc8895-2aec-00",
    "key": "d4fc8895-2aec-0025-a620",
    "secret": "l5oxJeCvjqAps",
    "remark": "",
    "ips": []
  },
  "user": {
    "ethereumAddress": "0xc4C5036b68a",
    "isRegistered": false,
    "email": "11@aa.com",
    "username": "pythonTest",
    "referredByAffiliateLink": "",
    "affiliateLink": "0",
    "apexTokenBalance": "",
    "stakedApexTokenBalance": "",
    "isEmailVerified": false,
    "isSharingUsername": false,
    "isSharingAddress": false,
    "country": "",
    "id": "1213724853023293440",
    "avatarUrl": "",
    "avatarBorderUrl": "",
    "emailNotifyGeneralEnable": false,
    "emailNotifyTradingEnable": false,
    "emailNotifyAccountEnable": false,
    "popupNotifyTradingEnable": false,
    "appNotifyTradingEnable": false
  },
  "account": {
    "ethereumAddress": "0xc4c5036b68a",
    "l2Key": "oxaaaa",
    "id": "3505225848",
    "version": "123",
    "spotAccount": {
      "createdAt": 1690365436385,
      "updatedAt": 1690365436385,
      "zkAccountId": "3505225848111",
      "isMultiSigEthAddress": false,
      "defaultSubAccountId": "3505225848111",
      "nonce": 1111,
      "status": "NORMAL",
      "subAccounts": [
        {
          "subAccountId": "3505225848111",
          "l2Key": "0x1123",
          "nonce": 11,
          "nonceVersion": 11,
          "changePubKeyStatus": "REGISTING"
        }
      ]
    },
    "spotWallets": [
      {
        "userId": "12137",
        "accountId": "350",
        "subAccountId": "350",
        "balance": "1191781.577364",
        "tokenId": "1",
        "pendingDepositAmount": "0.000000",
        "pendingWithdrawAmount": "0.000000",
        "pendingTransferOutAmount": "0.000000",
        "pendingTransferInAmount": "0.000000",
        "createdAt": 1690365436385,
        "updatedAt": 1690365436385
      }
    ],
    "experienceMoney": [
      {
        "availableAmount": "0.000000",
        "totalNumber": "0",
        "totalAmount": "0.000000",
        "recycledAmount": "0.000000",
        "token": "USDT"
      }
    ],
    "contractAccount": {
      "createdAt": 1690365436385,
      "takerFeeRate": "0.00050",
      "makerFeeRate": "0.00020",
      "minInitialMarginRate": "0",
      "status": "NORMAL",
      "unrealizePnlPriceType": "INDEX_PRICE"
    },
    "contractWallets": [
      {
        "userId": "121372485302",
        "accountId": "350522584833",
        "balance": "1191778.137753",
        "token": "USDT",
        "pendingDepositAmount": "0.000000",
        "pendingWithdrawAmount": "0.000000",
        "pendingTransferOutAmount": "0.000000",
        "pendingTransferInAmount": "0.000000"
      }
    ],
    "positions": [
      {
        "isPrelaunch": false,
        "symbol": "BTC-USDT",
        "status": "",
        "side": "LONG",
        "size": "0.000",
        "entryPrice": "0.00",
        "exitPrice": "",
        "createdAt": 1690366452416,
        "updatedTime": 1690366452416,
        "fee": "0.000000",
        "fundingFee": "0.000000",
        "lightNumbers": "",
        "customInitialMarginRate": "0"
      }
    ],
    "isNewUser": false
  }
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» apiKey	object	true	none	none
»» key	string	true	none	Placed in request header for sending to server
»» passphrase	string	true	none	Placed in request header for sending to server
»» secret	string	true	none	Used to generate signature
» user	object	true	none	none
»» ethereumAddress	string	true	none	Ethereum address
»» isRegistered	boolean	true	none	Registration confirmation
»» email	string	true	none	Email
»» username	string	true	none	Username
»» referredByAffiliateLink	string	true	none	referred Affiliate Link
»» isEmailVerified	boolean	true	none	Email binding confirmation
»» emailNotifyGeneralEnable	boolean	true	none	Newsletter, Market Updates, Product notify
»» emailNotifyTradingEnable	boolean	true	none	Deposits、Withdrawals, Account notify
»» emailNotifyAccountEnable	boolean	true	none	Order and Liquidation notify
»» popupNotifyTradingEnable	boolean	true	none	Trading pop-up notify
» account	object	true	none	none
»» l2Key	string	true	none	User's l2Key
»» ethereumAddress	string	true	none	User's ethereumAddress
»» id	string	true	none	User's account ID
»» spotAccount	object	true	none	User's spot account
»»» createdAt	integer	true	none	User's account create time
»»» updatedAt	integer	true	none	User's account update time
»»» zkAccountId	string	true	none	User's zk account ID
»»» defaultSubAccountId	string	true	none	User's zk default sub account ID
»»» nonce	integer	true	none	User's account nonce
»»» status	string	true	none	User's account status
»»» subAccounts	[object]	true	none	User's sub accounts
»»»» subAccountId	string	false	none	User's sub account ID
»»»» l2Key	string	false	none	User's sub account l2Key
»»»» nonce	integer	false	none	User's sub account nonce
»»»» nonceVersion	integer	false	none	User's sub account nonce version
»»»» changePubKeyStatus	string	false	none	User's sub account change pubKey status
»» spotWallets	[object]	true	none	User's spot wallets
»»» tokenId	string	false	none	Spot token ID
»»» pendingDepositAmount	string	false	none	Pending deposit amount
»»» pendingWithdrawAmount	string	false	none	Pending withdraw amount
»»» pendingTransferOutAmount	string	false	none	Pending transfer out amount
»»» pendingTransferInAmount	string	false	none	Pending transfer in amount
»» experienceMoney	[object]	true	none	Experience money
»»» availableAmount	string	false	none	Available experience money amount
»»» totalNumber	string	false	none	Total experience money number
»»» totalAmount	string	false	none	Total experience money value
»»» recycledAmount	string	false	none	Recycled experience money value
»» contractAccount	object	true	none	
»»» makerFeeRate	string	true	none	Maker fee rate
»»» takerFeeRate	string	true	none	Taker fee rate
»»» createdAt	integer	true	none	Created time
»»» minInitialMarginRate	string	true	none	Min Initial Margin Rate
»»» status	string	false	none	Account status
»» contractWallets	[object]	true	none	Contract wallets
»»» token	string	false	none	Asset token
»»» balance	string	false	none	Wallet balance
»»» pendingDepositAmount	string	true	none	Pending deposit amount
»»» pendingWithdrawAmount	string	true	none	Pending withdrawal amount
»»» pendingTransferOutAmount	string	true	none	Pending outbound transfer amount
»»» pendingTransferInAmount	string	true	none	Pending inbound transfer amount
»» openPositions	[object]	true	none	Open positions
»»» symbol	string	false	none	Symbol
»»» side	string	false	none	Side
»»» size	string	false	none	Size
»»» entryPrice	string	false	none	Entry price
»»» fee	string	false	none	Order fee
»»» createdAt	integer	false	none	Created at
»»» updatedTime	integer	false	none	Updated time
»»» fundingFee	string	false	none	Funding fee
»»» lightNumbers	string	false	none	ADL ranking
GET Retrieve User Data
GET /v3/user

curl https://omni.apex.exchange/api/v3/user -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "ethereumAddress": "0x091aaaaaaaaaa",
  "isRegistered": true,
  "email": "email@apex.exchange",
  "username": "supersam15o",
  "userData": {},
  "isEmailVerified": false,
  "emailNotifyGeneralEnable": false,
  "emailNotifyTradingEnable": false,
  "emailNotifyAccountEnable": false,
  "popupNotifyTradingEnable": false
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» ethereumAddress	string	true	none	Ethereum address
» isRegistered	boolean	true	none	Registration completed
» email	string	true	none	Email
» username	string	true	none	Username
» userData	object	true	none	none
» isEmailVerified	boolean	true	none	none
» emailNotifyGeneralEnable	string	true	none	Newsletter, market and product updates
» emailNotifyTradingEnable	string	true	none	Order and liquidation updates
» emailNotifyAccountEnable	string	true	none	Deposit, withdrawal and account updates
» popupNotifyTradingEnable	string	true	none	Enable trading notifications
POST Edit User Data
POST /v3/modify-user

curl https://omni.apex.exchange/api/v3/modify-user -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'userData={userData}&email={email}&username={username}&isSharingUsername={isSharingUsername}&isSharingAddress={isSharingAddress}&country={country}&emailNotifyGeneralEnable={emailNotifyGeneralEnable}&emailNotifyTradingEnable={emailNotifyTradingEnable}&emailNotifyAccountEnable={emailNotifyAccountEnable}&popupNotifyTradingEnable={popupNotifyTradingEnable}'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» userData	body	string	false	none
» email	body	string	false	Email
» username	body	string	false	Username
» isSharingUsername	body	string	false	none
» isSharingAddress	body	string	false	none
» country	body	string	false	country
» emailNotifyGeneralEnable	body	string	false	Newsletter, market and product updates
» emailNotifyTradingEnable	body	string	false	Order and liquidation updates
» emailNotifyAccountEnable	body	string	false	Deposit, withdrawal and account updates
» popupNotifyTradingEnable	body	string	false	Enable trading notifications
Successful Response Generation

{
  "ethereumAddress": "0x091aaaaaaaaaa",
  "isRegistered": true,
  "email": "email@apex.exchange",
  "username": "supersam15o",
  "userData": {},
  "isEmailVerified": false,
  "emailNotifyGeneralEnable": false,
  "emailNotifyTradingEnable": false,
  "emailNotifyAccountEnable": false,
  "popupNotifyTradingEnable": false
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» ethereumAddress	string	true	none	Ethereum address
» isRegistered	boolean	true	none	Registration completed
» email	string	true	none	Email
» username	string	true	none	Username
» userData	object	true	none	none
» isEmailVerified	boolean	true	none	none
» emailNotifyGeneralEnable	string	true	none	Newsletter, market and product updates
» emailNotifyTradingEnable	string	true	none	Order and liquidation updates
» emailNotifyAccountEnable	string	true	none	Deposit, withdrawal and account updates
» popupNotifyTradingEnable	string	true	none	Enable trading notifications
Account
v3.0.0
The API endpoints of Account require authentication.

GET Account Data & Positions
GET /v3/account

Get the authenticated user’s account by id (the id is derived from client information and the bound Ethereum address).
The response returns account identifiers (id, ethereumAddress, l2Key) together with the current trading state in one request: spotAccount, spotWallets, experienceMoney, contractAccount, contractWallets, and positions.

curl https://omni.apex.exchange/api/v3/account -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
Successful Response Generation

{
  "ethereumAddress": "0xc4c5036b68a",
  "l2Key": "oxaaaa",
  "id": "3505225848",
  "version": "123",
  "spotAccount": {
    "createdAt": 1690365436385,
    "updatedAt": 1690365436385,
    "zkAccountId": "3505225848111",
    "isMultiSigEthAddress": false,
    "defaultSubAccountId": "3505225848111",
    "nonce": 1111,
    "status": "NORMAL",
    "subAccounts": [
      {
        "subAccountId": "3505225848111",
        "l2Key": "0x1123",
        "nonce": 11,
        "nonceVersion": 11,
        "changePubKeyStatus": "REGISTING"
      }
    ]
  },
  "spotWallets": [
    {
      "userId": "12137",
      "accountId": "350",
      "subAccountId": "350",
      "balance": "1191781.577364",
      "tokenId": "1",
      "pendingDepositAmount": "0.000000",
      "pendingWithdrawAmount": "0.000000",
      "pendingTransferOutAmount": "0.000000",
      "pendingTransferInAmount": "0.000000",
      "createdAt": 1690365436385,
      "updatedAt": 1690365436385
    }
  ],
  "experienceMoney": [
    {
      "availableAmount": "0.000000",
      "totalNumber": "0",
      "totalAmount": "0.000000",
      "recycledAmount": "0.000000",
      "token": "USDT"
    }
  ],
  "contractAccount": {
    "createdAt": 1690365436385,
    "takerFeeRate": "0.00050",
    "makerFeeRate": "0.00020",
    "minInitialMarginRate": "0",
    "status": "NORMAL",
    "unrealizePnlPriceType": "INDEX_PRICE",
    "token": "USDC"
  },
  "contractWallets": [
    {
      "userId": "121372485302",
      "accountId": "350522584833",
      "balance": "1191778.137753",
      "asset": "USDT",
      "pendingDepositAmount": "0.000000",
      "pendingWithdrawAmount": "0.000000",
      "pendingTransferOutAmount": "0.000000",
      "pendingTransferInAmount": "0.000000"
    }
  ],
  "positions": [
    {
      "isPrelaunch": false,
      "symbol": "BTC-USDT",
      "status": "",
      "side": "LONG",
      "size": "0.000",
      "entryPrice": "0.00",
      "exitPrice": "",
      "createdAt": 1690366452416,
      "updatedTime": 1690366452416,
      "fee": "0.000000",
      "fundingFee": "0.000000",
      "lightNumbers": "",
      "customInitialMarginRate": "0"
    }
  ],
  "isNewUser": false
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» account	object	true	none	none
»» l2Key	string	true	none	User's l2Key
»» ethereumAddress	string	true	none	User's ethereumAddress
»» id	string	true	none	User's account ID
»» spotAccount	object	true	none	User's spot account
»»» createdAt	integer	true	none	User's account create time
»»» updatedAt	integer	true	none	User's account update time
»»» zkAccountId	string	true	none	User's zk account ID
»»» defaultSubAccountId	string	true	none	User's zk default sub account ID
»»» nonce	integer	true	none	User's account nonce
»»» status	string	true	none	User's account status
»»» subAccounts	[object]	true	none	User's sub accounts
»»»» subAccountId	string	false	none	User's sub account ID
»»»» l2Key	string	false	none	User's sub account l2Key
»»»» nonce	integer	false	none	User's sub account nonce
»»»» nonceVersion	integer	false	none	User's sub account nonce version
»»»» changePubKeyStatus	string	false	none	User's sub account change pubKey status
»» spotWallets	[object]	true	none	User's spot wallets
»»» tokenId	string	false	none	Spot token ID
»»» pendingDepositAmount	string	false	none	Pending deposit amount
»»» pendingWithdrawAmount	string	false	none	Pending withdraw amount
»»» pendingTransferOutAmount	string	false	none	Pending transfer out amount
»»» pendingTransferInAmount	string	false	none	Pending transfer in amount
»» experienceMoney	[object]	true	none	Experience money
»»» availableAmount	string	false	none	Available experience money amount
»»» totalNumber	string	false	none	Total number
»»» totalAmount	string	false	none	Total value
»»» recycledAmount	string	false	none	Recycled value
»» contractAccount	object	true	none	
»»» makerFeeRate	string	true	none	Maker fee rate
»»» takerFeeRate	string	true	none	Taker fee rate
»»» createdAt	integer	true	none	Created time
»»» minInitialMarginRate	string	true	none	Min initial margin rate
»»» status	string	false	none	Account status
»» contractWallets	[object]	true	none	Contract wallets
»»» asset	string	false	none	Asset
»»» balance	string	false	none	Wallet balance
»» pendingDepositAmount	string	true	none	Pending deposit amount
»» pendingWithdrawAmount	string	true	none	Pending withdrawal amount
»» pendingTransferOutAmount	string	true	none	Pending outbound transfer amount
»» pendingTransferInAmount	string	true	none	Pending inbound transfer amount
»» openPositions	[object]	true	none	Open positions
»»» symbol	string	false	none	Symbol
»»» side	string	false	none	Side
»»» size	string	false	none	Size
»»» entryPrice	string	false	none	Entry price
»»» fee	string	false	none	Order fee
»»» createdAt	integer	false	none	Created at
»»» updatedTime	integer	false	none	Updated time
»»» fundingFee	string	false	none	Funding fee
»»» lightNumbers	string	false	none	ADL ranking
GET Account balance
GET /v3/account-balance

curl https://omni.apex.exchange/api/v3/account-balance -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "totalEquityValue": "100.000000",
  "availableBalance": "100.000000",
  "initialMargin": "100.000000",
  "maintenanceMargin": "100.000000",
  "symbolToOraclePrice": {
    "BTC-USDT": {
      "oraclePrice": "20000",
      "createdTime": 124566
    }
  }
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status code 200

Parameter	Type	Required	Limit	Comment
» totalEquityValue	string	true	none	
» availableBalance	string	true	none	
» initialMargin	string	true	none	
» maintenanceMargin	string	true	none	
» symbolToOraclePrice	object	true	none	
»» BTC-USDC	object	true	none	
»»» oraclePrice	string	true	none	
»»» createdTime	integer	true	none	
GET Funding Rate
GET /v3/funding

curl https://omni.apex.exchange/api/v3/funding?limit={limit}&page={page}&symbol={symbol}&side={side} -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	false	none
limit	query	string	false	Default at 100
page	query	string	false	Page numbers start from 0
beginTimeInclusive	query	string	false	Start time
endTimeExclusive	query	string	false	End time
side	query	string	false	Side
status	query	string	false	Order status
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "fundingValues": [
    {
      "id": "1234",
      "symbol": "BTC-USD",
      "fundingValue": "10000",
      "rate": "0.0000125000",
      "positionSize": "500",
      "price": "90",
      "side": "LONG",
      "status": "SUCCESS",
      "fundingTime": 1647502440973,
      "transactionId": "1234556"
    }
  ],
  "totalSize": 11
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» fundingValues	[object]	true	none	none
»» id	string	false	none	id
»» symbol	string	false	none	Symbol
»» fundingValue	string	false	none	Funding fee value
»» rate	string	false	none	Funding rate
»» positionSize	string	false	none	Open position size
»» price	string	false	none	Symbol price
»» side	string	false	none	Position side
»» status	string	false	none	Position funding status
»» fundingTime	integer	false	none	Funding fee time
»» transactionId	string	false	none	Successful wallet transaction ID
» totalSize	integer	true	none	Total size
GET User Historial Profit and Loss
GET /v3/historical-pnl

curl https://omni.apex.exchange/api/v3/historical-pnl?limit={limit}&page={page}&beginTimeInclusive={beginTimeInclusive}&endTimeExclusive={endTimeExclusive}&type={type}&symbol={symbol} -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
beginTimeInclusive	query	string	false	StartTime
endTimeExclusive	query	string	false	EndTime
type	query	string	false	Position type
symbol	query	string	false	Symbol
page	query	string	false	Page numbers start from 0
limit	query	string	false	Default at 100
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "historicalPnl": [
    { "symbol": "BTC-USDC",
      "size": "1.0000",
      "totalPnl": "1.0000",
      "price": "1.0000",
      "createdAt": 1647502440973,
      "type": "CLOSE_POSITION",
      "isLiquidate": false,
      "isDeleverage": false
    }
  ],
  "totalSize": 12
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Position	Type	Required	Comment
» historicalPnl	[object]	true	none	none
»» size	string	false	none	Size
»» totalPnl	string	false	none	Closing profit and loss
»» price	string	false	none	Price
»» exitPrice	string	false	none	Closing price
»» createdAt	integer	false	none	Time
»» type	string	false	none	postion type
»» isLiquidate	boolean	false	none	Liquidate
»» isDeleverage	boolean	false	none	ADL
» totalSize	integer	true	none	none
GET Yesterday's Profit & Loss
GET /v3/yesterday-pnl

curl https://omni.apex.exchange/api/v3/yesterday-pnl -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "data": "11.11"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» data	string	true	none	Profit and loss value
GET Historical Asset Value
GET /v3/history-value

curl https://omni.apex.exchange/api/v3/history-value -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
endTime	query	int64	false	Start time
startTime	query	int64	false	End time
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "historyValues": [
    {
      "accountTotalValue": "123.11",
      "dateTime": 1651406864000
    }
  ]
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» historyValues	[object]	true	none	none
»» accountTotalValue	string	false	none	Assets
»» dateTime	integer	false	none	Assets date and time snapshot
POST Sets the initial margin rate of a contract
POST /v3/set-initial-margin-rate

curl https://omni.apex.exchange/api/v3/set-initial-margin-rate -H "Content-Type: application/x-www-form-urlencoded" -H "APEX-SIGNATURE: ***" -H "APEX-TIMESTAMP: ***" -H "APEX-API-KEY: ***" -H "APEX-PASSPHRASE: ***" -X POST -d "symbol=BTC-USDC&initialMarginRate=0.02"

Body

symbol: string
initialMarginRate: string

Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» symbol	body	string	true	symbol
» initialMarginRate	body	string	true	initialMarginRate(the reciprocal of the opening leverage)
Successful Response Generation

Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Asset
v3.0.0
The API endpoints of Asset require authentication.

POST User transfer asset from fund account to contract account
POST /v3/transfer-out

Body Request

amount: string
clientTransferId: string
timestamp: 0
tokenId: string
token: string
fee: string
signature: string
zkAccountId: string
nonce: 0
receiverAccountId: string
receiverZkAccountId: string
receiverSubAccountId: string
receiverAddress: string
subAccountId: string

Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	yes	Request signature
APEX-TIMESTAMP	header	string	yes	Request timestamp
APEX-API-KEY	header	string	yes	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	yes	apiKeyCredentials.passphrase
body	body	object	no	none
» amount	body	string	yes	Amount
» clientTransferId	body	string	yes	Unique id of the client associated with the transfer. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
» timestamp	body	integer	yes	Timestamp，sec
» tokenId	body	string	yes	Asset token id
» token	body	string	yes	Asset token
» fee	body	string	yes	Transfer fee, default is 0
» signature	body	string	yes	The signature for the transfer,
» zkAccountId	body	string	yes	User's zk account id
» nonce	body	integer	yes	User's eth address nonce
» receiverAccountId	body	string	yes	Contract asset pool account id
» receiverZkAccountId	body	string	yes	Contract asset pool zk account id
» receiverSubAccountId	body	string	yes	Contract asset pool sub account id, default is 0
» receiverAddress	body	string	yes	Contract asset pool eth address
» subAccountId	body	string	yes	User's sub account id,default is 0
Successful Response Generation

{
  "id": "1234455",
  "type": "TRANSFER_OUT"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	true	none	
» type	string	true	none	
POST User transfer asset from contract account to fund account
POST /v3/contract-transfer-out

example

Body Request

amount: string
clientWithdrawId: string
expireTime: 0
ethAddress: string
signature: string
token: string

Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	yes	Request signature
APEX-TIMESTAMP	header	string	yes	Request timestamp
APEX-API-KEY	header	string	yes	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	yes	apiKeyCredentials.passphrase
body	body	object	no	none
» amount	body	string	yes	Amount
» clientWithdrawId	body	string	yes	Unique id of the client associated with the transfer. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
» expireTime	body	integer	yes	Expire time，sec
» ethAddress	body	string	yes	User's eth address
» signature	body	string	yes	The signature for the transfer, signed with private key.
» token	body	string	yes	Asset token
Successful Response Generation

{
  "id": "12345",
  "type": "PERP_TO_ZK"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	true	none	
» type	string	true	none	
POST User Withdrawal
POST /v3/withdrawal

withdrawalToSign = {  
humanAmount: params.amount,  
expirationIsoTimestamp: params.expiration,  
clientId,  
positionId,  
};  
example

curl https://omni.apex.exchange/api/v3/withdrawal -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'amount=1&clientWithdrawId=xxx&timestamp=1234556&ethAddress=0x123&signature=0x1123&zkAccountId=111&subAccountId=0&l2Key=0x12345&toChainId=3&l2SourceTokenId=140&l1TargetTokenId=140&fee=0&nonce=1&isFastWithdraw=false'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» amount	body	string	yes	Amount
» clientWithdrawId	body	string	yes	Unique id of the client associated with the withdrawal. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
» timestamp	body	integer	yes	Timestamp，sec
» ethAddress	body	string	yes	EthAddress
» signature	body	string	yes	The signature for the withdraw, signed with zkKeys.
» zkAccountId	body	string	yes	The user's zkAccountId
» subAccountId	body	string	yes	The user's subAccountId, default is 0
» l2Key	body	string	yes	Zk l2Key
» toChainId	body	string	yes	To chainId
» l2SourceTokenId	body	string	yes	Default is 140,(USDT)
» l1TargetTokenId	body	string	yes	Default is 140,(USDT)
» fee	body	string	yes	Default is 0
» nonce	body	integer	yes	The user zk account nonce
» isFastWithdraw	body	string	yes	Defalut is false
Successful Response Generation

{
  "id": "1234455",
  "type": "WITHDRAW"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	true	none	id
» type	string	true	none	type
GET Withdrawal Fees
the withdrawal need zkAvailableAmount >= withdrawAmount
the fast withdrawal needzkAvailableAmount >= withdrawAmount && fastPoolAvailableAmount>= withdrawAmount
GET /v3/withdraw-fee

curl https://omni.apex.exchange/api/v3/withdraw-fee?amount={amount}&chainId={chainId}&tokenId={tokenId} -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' 
Request Parameters
Parameter	Position	Type	Required	Comment
amount	query	string	false	USDT
chainIds	query	string	false	withdraw to chainId
tokenId	query	string	false	default is 140(USDT)
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
    "withdrawFeeAndPoolBalances": [
        {
            "chainId": "123",
            "tokenId": "111",
            "fee": "1.1",
            "zkAvailableAmount": "1.1",
            "fastpoolAvailableAmount": "1.1"
        }
    ]
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» withdrawFeeAndPoolBalances	[object]	true	none	Fee and Pool
»» chainId	string	true	none	ChainId
»» zklinkTokenId	string	true	none	TokenId
»» fee	string	true	none	Fee
»» zklinkAvailableAmount	string	true	none	Pool zklink available amount
»» fastpoolAvailableAmount	string	false	none	Fast pool available amount
POST Submit Withdraw Claim
POST /v3/submit-withdraw-claim

curl https://omni.apex.exchange/api/v3/submit-withdraw-claim \
  -H 'APEX-SIGNATURE: ***' \
  -H 'APEX-TIMESTAMP: ***' \
  -H 'APEX-API-KEY: ***' \
  -H 'APEX-PASSPHRASE: ***' \
  -X POST \
  -d 'id=123&transactionHash=0xabc'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» id	body	string	yes	Withdraw id
» transactionHash	body	string	yes	L1 transaction hash
Successful Response Generation

{
  "code": 0,
  "msg": ""
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» code	integer	true	none	Response status code
» msg	string	true	none	Response message
GET Contract Account Transfer Limits
GET /v3/contract-transfer-limit

curl https://omni.apex.exchange/api/v3/contract-transfer-limit?token={token} -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
token	query	string	true	USDT
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
    "withdrawAvailableAmount": "100.1",
    "transferAvailableAmount": "100.1",
    "experienceMoneyAvailableAmount": "100.1",
    "experienceMoneyRecycledAmount": "100.1",
    "withdrawAvailableOriginAmount": "100.1",
    "experienceMoneyNeedRecycleAmount": "100.1"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» withdrawAvailableAmount	string	true	none	Withdraw available amount
» transferAvailableAmount	string	true	none	Transfer available amount
» experienceMoneyAvailableAmount	string	true	none	Experience money available amount
» experienceMoneyRecycledAmount	string	true	none	Experience money recycled amount
» withdrawAvailableOriginAmount	string	true	none	Withdraw available origin amount
» experienceMoneyNeedRecycleAmount	string	true	none	Experience money need recycle amount
GET Repayment price
GET /v3/repayment-price

Direction (
    SPOT_TO_PRICING             //Spot assets -> Priced assets (usdt)
    PRICING_TO_SPOT            //Priced assets (usdt)->Spot assets
)
Status (
    PENDING_CHECKING        
    PENDING_CENSORING      
    SUCCESS                 
    SUCCESS_L2_APPROVED   
    FAILED_CHECK_INVALID    
    FAILED_CENSOR_FAILURE  
    FAILED_L2_REJECTED       
)
Request Parameters
Parameter	Position	Type	Required	Comment
repaymentPriceTokens	query	string	yes	
clientId	query	string	yes	none
APEX-SIGNATURE	header	string	yes	none
APEX-TIMESTAMP	header	string	yes	none
APEX-API-KEY	header	string	yes	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	yes	apiKeyCredentials.passphrase
repaymentPriceTokens: ETH|1,BTC|0.1
Successful Response Generation

Successful

{
  "repaymentTokens": [
    {
      "token": "ETH",
      "price": "3000",
      "size": "1"
    }
  ]
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» repaymentTokens	[object]	true	none	
»» token	string	false	none	
»» price	string	false	none	
»» size	string	false	none	
POST User manual repayment V3
POST /v3/manual-create-repayment

Body

repaymentTokens: ETH|3000|1,BTC|60000|0.1
clientId: string
signature: string
expireTime: 0
poolRepaymentTokens: ETH|3000|1,BTC|60000|0.1

Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	yes	none
APEX-TIMESTAMP	header	string	yes	none
APEX-API-KEY	header	string	yes	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	yes	apiKeyCredentials.passphrase
body	body	object	yes	none
» repaymentTokens	body	string	yes	token
» clientId	body	string	yes	Unique id of the client associated with the transfer. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
» signature	body	string	yes	none
» expireTime	body	integer	yes	sec
» poolRepaymentTokens	body	string	yes	token
Successful Response Generation

Successful

{
  "id": "1234455"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	true	none	
GET Deposit and Withdraw Data
GET /v3/transfers

curl https://omni.apex.exchange/api/v3/transfers?limit={limit}&page={page}&currencyId={currencyId}&chainIds={chainIds} -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
direction (
NEXT 
PREVIOUS 
)

TransfersType (
DEPOSIT 
WITHDRAW 
FAST_WITHDRAW 
OMNI_TO_PERP //spot account -> contract account
OMNI_FROM_PERP //spot account <- contract account
AFFILIATE_REBATE // affliate rebate
REFERRAL_REBATE // referral rebate
BROKER_REBATE // broker rebate
)

Deposit Status{
PENDING_RISK_CHECKING // risk checking
PENDING_SEND_L2 // sending to l2
SUCCESS // deposit success
SUCCESS_L2_APPROVED // L2 approved success
FAILED_RISK_CHECKING // risk checking failed
FAILED_SEND_L2 // sending to l2 failed
FAILED_L2_REJECTED // l2 rejected
}

Withdrawal and FastWithdrawal Status{
PENDING_WITHDRAW_L1_TRY // pending withdraw
PENDING_SEND_L2 // pending send
SUCCESS // withdraw success 
SUCCESS_L2_APPROVED // l2 approve withdraw success
WITHDRAW_CAN_BE_CLAIM //the withdrawal can be claim
PENDING_L1_CLAIMING //pengding claim
SUCCESS_L1_CLAIMED //claim success
FAILED_WITHDRAW_L1_TRY_REJECTED // withdraw to l1 be rejected
FAILED_SEND_L2 // withdraw failed
FAILED_L2_REJECTED // withdraw failed by l2 
FAST_WITHDRAW_L1_SUCCESS // fast withdraw success 
FAILED_L1_CLAIMED_REJECTED //claim failed
}

TransferStatus (
PENDING_CHECKING // transfer checking
PENDING_SEND_L2 // sending to l2
SUCCESS // transfer success
SUCCESS_L2_APPROVED // l2 approved
FAILED_CHECK_INVALID // transfer check failed
FAILED_SEND_L2 // transfer send failed
FAILED_L2_REJECTED // l2 rejected
)
Request Parameters
Parameters	Position	Type	Required	Comments
limit	query	integer	false	Page limit default at 100
id	query	string	no	if direction is NEXT the id is the last one of this page, or direction is PREVIOUS the id is first one of this page
tokenId	query	string	no	Filter to show only token ID, all will be searched if the field is empty
beginTimeInclusive	query	integer	false	Start time
endTimeExclusive	query	string	false	End time
chainIds	query	string	false	Check for multiple chainID records, separated by commas
transferType	query	string	false	Check for multiple transferType records, separated by commas
subAccountId	query	string	yes	none, default 0
direction	query	string	no	default NEXT
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
    "transfers": [
        {
            "id": "1111",
            "type": "WITHDRAW",
            "amount": "3000",
            "transactionHash": "0x12aaaaaaaa",
            "status": "PENDING",
            "createdAt": 1647502440973,
            "updatedAt": 1647502440973,
            "confirmedAt": 1647502440973,
            "fromTokenId": "12",
            "toTokenId": "12",
            "chainId": "1235",
            "orderId": "1235",
            "ethAddress": "0x1235",
            "fromEthAddress": "0x1235",
            "toEthAddress": "0x1235",
            "fee": "11",
            "clientId": "12345"
        }
    ]
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» transfers	[object]	true	none	none
»» id	string	false	none	none
»» type	string	false	none	DEPOSIT, WITHDRAW or FAST_WITHDRAW
»» Amount	string	false	none	Amount
»» transactionHash	string	false	none	Transaction hash
»» status	string	false	none	Status
»» createdAt	integer	false	none	Created at
»» updatedAt	string	false	none	Only applicable for deposits
»» clientId	string	false	none	Client to create a randomized id (only for withdrawal)
»» orderId	string	true	none	Success Wallet Transaction Id
»» chainId	string	true	none	Supported chainId
»» fee	string	true	none	Fee
» totalSize	string	true	none	Total size
Trade
v3.0.0
The API endpoints of Trade require authentication.

POST Creating Orders
Market orders: Unlike CEX, ApeX requires a price (zkLink signature). Derive it from order size and market depth or call GET /v3/get-worst-price. The price must be worse than the index price, otherwise the order will be canceled.
Expiration: Applies to orders and withdrawals; recommend 28 days. L2 signatures use hours, API uses seconds. L2 = (now_ms + 28d) / 3,600,000; API = L2 * 3,600,000.
POST /v3/order

TimeInForce (  
GOOD_TIL_CANCEL // Effective until canceled, default.   
FILL_OR_KILL // Immediately and completely filled or canceled.   
IMMEDIATE_OR_CANCEL // Immediately executed or canceled.    
)  
example

curl https://omni.apex.exchange/api/v3/order -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'symbol={symbol}&side={side}&type={type}&size={size}&price={price}&limitFee={limitFee}&expiration={expiration}&timeInForce={timeInForce}&triggerPrice={triggerPrice}&trailingPercent={trailingPercent}&clientOrderId={clientOrderId}&signature={signature}&reduceOnly=false'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» symbol	body	string	true	Symbol
» side	body	string	true	BUY or SELL
» type	body	string	true	"LIMIT", "MARKET","STOP_LIMIT", "STOP_MARKET", "TAKE_PROFIT_LIMIT", "TAKE_PROFIT_MARKET"
» size	body	string	true	Size
» price	body	string	true	Price
» limitFee	body	string	true	limitFee = price * size * takerFeeRate( from GET /v1/account)
» expiration	body	string	true	Order expiry time
» timeInForce	body	string	false	"GOOD_TIL_CANCEL", "FILL_OR_KILL", "IMMEDIATE_OR_CANCEL", "POST_ONLY"
» triggerPrice	body	string	false	Trigger price
» trailingPercent	body	string	false	Conditional order trailing-stop
» clientOrderId	body	string	true	Randomized client id
» signature	body	string	true	zkKey signature
» reduceOnly	body	string	false	Reduce-only
Successful Response Generation

{
    "id": "1234",
    "clientId": "1234",
    "accountId": "12345",
    "symbol": "BTC-USD",
    "side": "SELL",
    "price": "18000",
    "limitFee": "100",
    "fee": "100",
    "triggerPrice": "1.2",
    "trailingPercent": "0.12",
    "size": "100",
    "remainingSize": "100",
    "type": "LIMIT",
    "createdAt": 1647502440973,
    "updatedTime": 1647502440973,
    "expiresAt": 1647502440973,
    "status": "PENDING",
    "timeInForce": "GOOD_TIL_CANCEL",
    "postOnly": false,
    "reduceOnly": false,
    "stopPnl": false,
    "latestMatchFillPrice": "reason",
    "cumMatchFillSize": "0.1",
    "cumMatchFillValue": "1000",
    "cumMatchFillFee": "1",
    "cumSuccessFillSize": "0.1",
    "cumSuccessFillValue": "1000",
    "cumSuccessFillFee": "1",
    "triggerPriceType": "INDEX",
    "isOpenTpslOrder": true,
    "isSetOpenTp": true,
    "isSetOpenSl": false,
    "openTpParam": {
        "side": "SELL",
        "price": "18000",
        "limitFee": "100",
        "clientOrderId": "111100",
        "triggerPrice": "1.2",
        "trailingPercent": "0.12",
        "size": "100"
    },
    "openSlParam": {
        "side": "SELL",
        "price": "18000",
        "limitFee": "100",
        "clientOrderId": "111100",
        "triggerPrice": "1.2",
        "trailingPercent": "0.12",
        "size": "100"
    }
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	false	none	Order id
»» orderId	string	false	none	Order id
» clientOrderId	string	false	none	Client create the Randomized id
» accountId	string	false	none	Account ID
» symbol	string	false	none	Symbol
» side	string	false	none	BUY or SELL
» price	string	false	none	Order open price
» limitFee	string	false	none	Order open max. fee
» fee	string	false	none	Order open actual fee
» triggerPrice	string	false	none	Conditional order trigger price
» trailingPercent	string	false	none	Conditional order trailing-stop
» size	string	false	none	Order open size
» type	string	false	none	Order type
» createdAt	integer	false	none	Order create at
» updatedTime	integer	false	none	Order update time
» expiresAt	integer	false	none	Order expires at
» status	string	false	none	Order status
» timeInForce	string	false	none	Open order timeInForce
» postOnly	boolean	false	none	Open Post-only order
» reduceOnly	boolean	false	none	Open Reduce-only order
» latestMatchFillPrice	string	false	none	Latest match fill price
» cumMatchFillSize	string	false	none	Cumulative match fill size
» cumMatchFillValue	string	false	none	Cumulative match fill value
» cumMatchFillFee	string	false	none	Cumulative match fill fee
» cumSuccessFillSize	string	false	none	Cumulative success fill size
» cumSuccessFillValue	string	false	none	Cumulative success fill value
» cumSuccessFillFee	string	false	none	Cumulative success fill fee
POST Cancel Order
POST /v3/delete-order

curl https://omni.apex.exchange/api/v3/delete-order -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'id={id}'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» id	body	string	false	none
Successful Response Generation

{
  "data": "123456"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» data	string	true	none	Order ID
POST Cancel Order By ClientOrderId
POST /v3/delete-client-order-id

curl https://omni.apex.exchange/api/v3/delete-client-order-id` -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'id={id}'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» id	body	string	false	none
Successful Response Generation

{
  "data": "123456"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» data	string	true	none	Order ID
GET Open Orders
GET /v3/open-orders

Order type   
"UNKNOWN_ORDER_TYPE",   
 "LIMIT", //Limit price   
 "MARKET", //Market price   
 "STOP_LIMIT", //Stop limit order   
 "STOP_MARKET", //Stop market order   
 "TAKE_PROFIT_LIMIT",//Take profit limit orders   
 "TAKE_PROFIT_MARKET",//Take profit market orders  

Order Status   
 "PENDING", // Order submitted but not yet processesd   
 "OPEN", // Order pending, partially filled   
 "FILLED", // Order has been completely filled   
 "CANCELED", //Order is canceled and may have been partially filled.   
 "EXPIRED", // Order has expired and may have been partially filled.   
 "UNTRIGGERED", // Order conditions have not been triggered  

Order Cancelation Reason {   
 "UNKNOWN_ORDER_CANCEL_REASON"  // Unknown   
 "EXPIRED"  // Order has expired   
 "USER_CANCELED"  // User manually canceled order     
 "COULD_NOT_FILL"  // Unable to fill FOK/IOC/Post-only orders   
 "REDUCE_ONLY_CANCELED"  // Unable to fulfil reduce-only orders    
 "LIQUIDATE_CANCELED"  // Account or orders triggered liquidation resulting in automatic order cancelation  
 "INTERNAL_FAILED"  // Internal processing issues including order matching failure or L2 validation failure   
}
example

curl https://omni.apex.exchange/api/v3/open-orders -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
Successful Response Generation

{
  "data": [
    {
      "id": "1234",
      "clientOrderId": "1234",
      "accountId": "12345",
      "symbol": "BTC-USD",
      "side": "SELL",
      "price": "18000",
      "limitFee": "100",
      "fee": "100",
      "triggerPrice": "1.2",
      "trailingPercent": "0.12",
      "size": "100",
      "type": "LIMIT",
      "createdAt": 1647502440973,
      "updatedTime": 1647502440973,
      "expiresAt": 1647502440973,
      "status": "PENDING",
      "timeInForce": "GOOD_TIL_CANCEL",
      "postOnly": false,
      "reduceOnly": false,
      "latestMatchFillPrice": "reason",
      "cumMatchFillSize": "0.1",
      "cumMatchFillValue": "1000",
      "cumMatchFillFee": "1",
      "cumSuccessFillSize": "0.1",
      "cumSuccessFillValue": "1000",
      "cumSuccessFillFee": "1"
    }
  ]
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» orders	[object]	true	none	none
»» id	string	false	none	Order id
»» orderId	string	false	none	Order id
»» clientOrderId	string	false	none	Client create the Randomized id
»» accountId	string	false	none	Account ID
»» symbol	string	false	none	Symbol
»» side	string	false	none	BUY or SELL
»» price	string	false	none	Order open price
»» limitFee	string	false	none	Order open max. fee
»» fee	string	false	none	Order open actual fee
»» triggerPrice	string	false	none	Conditional order trigger price
»» trailingPercent	string	false	none	Conditional order trailing-stop
»» size	string	false	none	Order open size
»» type	string	false	none	Order type
»» createdAt	integer	false	none	Order create at
»» updatedTime	integer	false	none	Order update time
»» expiresAt	integer	false	none	Order expires at
»» status	string	false	none	Order status
»» timeInForce	string	false	none	Open order timeInForce
»» postOnly	boolean	false	none	Open Post-only order
»» reduceOnly	boolean	false	none	Open Reduce-only order
»» latestMatchFillPrice	string	false	none	Latest match fill price
»» cumMatchFillSize	string	false	none	Cumulative match fill size
»» cumMatchFillValue	string	false	none	Cumulative match fill value
»» cumMatchFillFee	string	false	none	Cumulative match fill fee
»» cumSuccessFillSize	string	false	none	Cumulative success fill size
»» cumSuccessFillValue	string	false	none	Cumulative success fill value
»» cumSuccessFillFee	string	false	none	Cumulative success fill fee
POST Cancel all Open Orders
POST /v3/delete-open-orders

Body Request Parameters

symbol: BTC-USDT,ETH-USDT

curl https://omni.apex.exchange/api/v3/delete-open-orders -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' -X POST -d 'symbol={BTC-USDC,ETH-USDC}'
Request Parameters
Parameter	Position	Type	Required	Comment
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
body	body	object	false	none
» symbol	body	string	false	"BTC-USDT,ETH-USDT", Cancel all orders if none
Successful Response Generation

{

}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

GET All Order History
GET /v3/history-orders

Order type 
 "UNKNOWN_ORDER_TYPE",   
 "LIMIT", //Limit price   
 "MARKET", //Market price   
 "STOP_LIMIT", //Stop limit order   
 "STOP_MARKET", //Stop market order   
 "TAKE_PROFIT_LIMIT",//Take profit limit orders   
 "TAKE_PROFIT_MARKET",//Take profit market orders  

Order Status   
 "PENDING", // Order submitted but not yet processesd   
 "OPEN", // Order pending, partially filled   
 "FILLED", // Order has been completely filled    
 "CANCELED", //Order is canceled and may have been partially filled.    
 "EXPIRED", // Order has expired and may have been partially filled.   
 "UNTRIGGERED", // Order conditions have not been triggered  

Order Cancelation Reason {   
 "UNKNOWN_ORDER_CANCEL_REASON"  // Unknown   
 "EXPIRED"  // Order has expired   
 "USER_CANCELED"  // User manually canceled order     
 "COULD_NOT_FILL"  // Unable to fill FOK/IOC/Post-only orders   
 "REDUCE_ONLY_CANCELED"  // Unable to fulfil reduce-only orders    
 "LIQUIDATE_CANCELED"  // Account or orders triggered liquidation resulting in automatic order cancelation  
 "INTERNAL_FAILED"  // Internal processing issues including order matching failure or L2 validation failure   
}
example

curl https://omni.apex.exchange/api/v3/history-orders -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	false	none
status	query	string	false	none
side	query	string	false	BUY or SELL
type	query	string	false	"LIMIT", "MARKET","STOP_LIMIT", "STOP_MARKET", "TAKE_PROFIT_LIMIT","TAKE_PROFIT_MARKET"
limit	query	string	false	default 100
beginTimeInclusive	query	string	false	Start time
endTimeExclusive	query	string	false	End time
page	query	string	false	Page numbers start from 0
orderType	query	string	false	"ACTIVE","CONDITION","HISTORY"
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "orders": [
    {
      "id": "1234",
      "clientOrderId": "1234",
      "accountId": "12345",
      "symbol": "BTC-USD",
      "side": "SELL",
      "price": "18000",
      "limitFee": "100",
      "fee": "100",
      "triggerPrice": "1.2",
      "trailingPercent": "0.12",
      "size": "100",
      "type": "LIMIT",
      "createdAt": 1647502440973,
      "updatedTime": 1647502440973,
      "expiresAt": 1647502440973,
      "status": "PENDING",
      "timeInForce": "GOOD_TIL_CANCEL",
      "postOnly": false,
      "reduceOnly": false,
      "latestMatchFillPrice": "reason",
      "cumMatchFillSize": "0.1",
      "cumMatchFillValue": "1000",
      "cumMatchFillFee": "1",
      "cumSuccessFillSize": "0.1",
      "cumSuccessFillValue": "1000",
      "cumSuccessFillFee": "1"
    }
  ],
  "totalSize": 12
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» orders	[object]	true	none	none
»» id	string	false	none	Order id
»» orderId	string	false	none	Order id
»» clientOrderId	string	false	none	Client create the Randomized id
»» accountId	string	false	none	Account ID
»» symbol	string	false	none	Symbol
»» side	string	false	none	BUY or SELL
»» price	string	false	none	Order open price
»» limitFee	string	false	none	Order open max. fee
»» fee	string	false	none	Order open actual fee
»» triggerPrice	string	false	none	Conditional order trigger price
»» trailingPercent	string	false	none	Conditional order trailing-stop
»» size	string	false	none	Order open size
»» type	string	false	none	Order type
»» createdAt	integer	false	none	Order create at
»» updatedTime	integer	false	none	Order update time
»» expiresAt	integer	false	none	Order expires at
»» status	string	false	none	Order status
»» timeInForce	string	false	none	Open order timeInForce
»» postOnly	boolean	false	none	Open Post-only order
»» reduceOnly	boolean	false	none	Open Reduce-only order
»» latestMatchFillPrice	string	false	none	Latest match fill price
»» cumMatchFillSize	string	false	none	Cumulative match fill size
»» cumMatchFillValue	string	false	none	Cumulative match fill value
»» cumMatchFillFee	string	false	none	Cumulative match fill fee
»» cumSuccessFillSize	string	false	none	Cumulative success fill size
»» cumSuccessFillValue	string	false	none	Cumulative success fill value
»» cumSuccessFillFee	string	false	none	Cumulative success fill fee
» totalSize	integer	true	none	total order size
GET Order ID
GET /v3/order

curl https://omni.apex.exchange/api/v3/order?id={id} -h 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
id	query	string	true	none
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "id": "123456",
  "clientOrderId": "1234",
  "accountId": "afoo",
  "symbol": "BTC-USD",
  "side": "SELL",
  "price": "18000",
  "triggerPrice": "1.2",
  "trailingPercent": "0.12",
  "size": "100",
  "type": "LIMIT",
  "createdAt": 1647502440973,
  "unfillableAt": 1647502440973,
  "expiresAt": 1647502440973,
  "status": "PENDING",
  "timeInForce": "GOOD_TIL_CANCEL",
  "postOnly": false,
  "cancelReason": "reason"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	false	none	Order id
» orderId	string	false	none	Order id
» clientOrderId	string	false	none	Client create the Randomized id
» accountId	string	false	none	Account ID
» symbol	string	false	none	Symbol
» side	string	false	none	BUY or SELL
» price	string	false	none	Order open price
» limitFee	string	false	none	Order open max. fee
» fee	string	false	none	Order open actual fee
» triggerPrice	string	false	none	Conditional order trigger price
» trailingPercent	string	false	none	Conditional order trailing-stop
» size	string	false	none	Order open size
» type	string	false	none	Order type
» createdAt	integer	false	none	Order create at
» updatedTime	integer	false	none	Order update time
» expiresAt	integer	false	none	Order expires at
» status	string	false	none	Order status
» timeInForce	string	false	none	Open order timeInForce
» postOnly	boolean	false	none	Open Post-only order
» reduceOnly	boolean	false	none	Open Reduce-only order
» latestMatchFillPrice	string	false	none	Latest match fill price
» cumMatchFillSize	string	false	none	Cumulative match fill size
» cumMatchFillValue	string	false	none	Cumulative match fill value
» cumMatchFillFee	string	false	none	Cumulative match fill fee
» cumSuccessFillSize	string	false	none	Cumulative success fill size
» cumSuccessFillValue	string	false	none	Cumulative success fill value
» cumSuccessFillFee	string	false	none	Cumulative success fill fee
GET Order by clientOrderId
GET /v3/order-by-client-order-id

curl https://omni.apex.exchange/api/v3/order-by-client-order-id?id={id} -h 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***'
Request Parameters
Parameter	Position	Type	Required	Comment
id	query	string	true	none
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "id": "123456",
  "clientOrderId": "1234",
  "accountId": "afoo",
  "symbol": "BTC-USD",
  "side": "SELL",
  "price": "18000",
  "triggerPrice": "1.2",
  "trailingPercent": "0.12",
  "size": "100",
  "type": "LIMIT",
  "createdAt": 1647502440973,
  "unfillableAt": 1647502440973,
  "expiresAt": 1647502440973,
  "status": "PENDING",
  "timeInForce": "GOOD_TIL_CANCEL",
  "postOnly": false,
  "cancelReason": "reason"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» id	string	false	none	Order id
» orderId	string	false	none	Order id
» clientOrderId	string	false	none	Client create the Randomized id
» accountId	string	false	none	Account ID
» symbol	string	false	none	Symbol
» side	string	false	none	BUY or SELL
» price	string	false	none	Order open price
» limitFee	string	false	none	Order open max. fee
» fee	string	false	none	Order open actual fee
» triggerPrice	string	false	none	Conditional order trigger price
» trailingPercent	string	false	none	Conditional order trailing-stop
» size	string	false	none	Order open size
» type	string	false	none	Order type
» createdAt	integer	false	none	Order create at
» updatedTime	integer	false	none	Order update time
» expiresAt	integer	false	none	Order expires at
» status	string	false	none	Order status
» timeInForce	string	false	none	Open order timeInForce
» postOnly	boolean	false	none	Open Post-only order
» reduceOnly	boolean	false	none	Open Reduce-only order
» latestMatchFillPrice	string	false	none	Latest match fill price
» cumMatchFillSize	string	false	none	Cumulative match fill size
» cumMatchFillValue	string	false	none	Cumulative match fill value
» cumMatchFillFee	string	false	none	Cumulative match fill fee
» cumSuccessFillSize	string	false	none	Cumulative success fill size
» cumSuccessFillValue	string	false	none	Cumulative success fill value
» cumSuccessFillFee	string	false	none	Cumulative success fill fee
GET Trade History
GET /v3/fills

curl https://omni.apex.exchange/api/v3/fills?limit=100&page=0&symbol=BTC-USDC&side=BUY -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' 
Order Type  
 "UNKNOWN_ORDER_TYPE"    
 "LIMIT", //Limit price   
 "MARKET", //Market price   
 "STOP_LIMIT", //Stop limit order   
 "STOP_MARKET", //Stop market order   
 "TAKE_PROFIT_LIMIT",//Take profit limit orders   
 "TAKE_PROFIT_MARKET",//Take profit market orders  

Order Fill Status
  "PENDING_CENSORING",   // Order submitted and pending initial review (censoring). The system is verifying transaction data, compliance, and integrity before processing.
  "SUCCESS",              // Transaction succeeded and funds/positions have been credited. Awaiting Level-2 (L2) verification approval.
  "SUCCESS_L2_APPROVED",  // Transaction successfully passed L2 verification and is fully approved. Final state.
  "FAILED_CENSOR_FAILURE",// Transaction failed during initial review. Submitted data was invalid or inconsistent.
  "FAILED_L2_REJECTED",   // Transaction failed during L2 verification. 

Order Cancelation Reason {   
 "UNKNOWN_ORDER_CANCEL_REASON"  // Unknown   
 "EXPIRED"  // Order has expired   
 "USER_CANCELED"  // User manually canceled order     
 "COULD_NOT_FILL"  // Unable to fill FOK/IOC/Post-only orders   
 "REDUCE_ONLY_CANCELED"  // Unable to fulfil reduce-only orders    
 "LIQUIDATE_CANCELED"  // Account or orders triggered liquidation resulting in automatic order cancelation  
 "INTERNAL_FAILED"  // Internal processing issues including order matching failure or L2 validation failure   
}
Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	false	Symbol
side	query	string	false	BUY or SELL
limit	query	string	false	default at 100
beginTimeInclusive	query	string	false	Start time
endTimeExclusive	query	string	false	End time
page	query	string	false	Page numbers start from 0
orderType	query	string	false	orderType
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "orders": [
    {
      "id": "1234",
      "clientOrderId": "1234",
      "orderId": "123546",
      "accountId": "12345",
      "symbol": "BTC-USD",
      "side": "SELL",
      "price": "18000",
      "limitFee": "100",
      "fee": "100",
      "triggerPrice": "1.2",
      "trailingPercent": "0.12",
      "size": "100",
      "type": "LIMIT",
      "createdAt": 1647502440973,
      "updatedTime": 1647502440973,
      "expiresAt": 1647502440973,
      "status": "PENDING",
      "timeInForce": "GOOD_TIL_CANCEL",
      "postOnly": false,
      "reduceOnly": false,
      "latestMatchFillPrice": "reason",
      "cumMatchFillSize": "0.1",
      "cumMatchFillValue": "1000",
      "cumMatchFillFee": "1",
      "cumSuccessFillSize": "0.1",
      "cumSuccessFillValue": "1000",
      "cumSuccessFillFee": "1"
    }
  ],
  "totalSize": 12
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» orders	[object]	true	none	none
»» id	string	false	none	Order id
»» orderId	string	false	none	Order id
»» clientOrderId	string	false	none	Client create the Randomized id
»» accountId	string	false	none	Account ID
»» symbol	string	false	none	Symbol
»» side	string	false	none	BUY or SELL
»» price	string	false	none	Order open price
»» limitFee	string	false	none	Order open max. fee
»» fee	string	false	none	Order open actual fee
»» triggerPrice	string	false	none	Conditional order trigger price
»» trailingPercent	string	false	none	Conditional order trailing-stop
»» size	string	false	none	Order open size
»» type	string	false	none	Order type
»» createdAt	integer	false	none	Order create at
»» updatedTime	integer	false	none	Order update time
»» expiresAt	integer	false	none	Order expires at
»» status	string	false	none	Order status
»» timeInForce	string	false	none	Open order timeInForce
»» postOnly	boolean	false	none	Open Post-only order
»» reduceOnly	boolean	false	none	Open Reduce-only order
»» latestMatchFillPrice	string	false	none	Latest match fill price
»» cumMatchFillSize	string	false	none	Cumulative match fill size
»» cumMatchFillValue	string	false	none	Cumulative match fill value
»» cumMatchFillFee	string	false	none	Cumulative match fill fee
»» cumSuccessFillSize	string	false	none	Cumulative success fill size
»» cumSuccessFillValue	string	false	none	Cumulative success fill value
»» cumSuccessFillFee	string	false	none	Cumulative success fill fee
» totalSize	integer	true	none	Total order size
GET Worst Price
GET /v3/get-worst-price

get market price from orderbook

curl https://omni.apex.exchange/api/v3/get-worst-price?size=1&symbol=BTC-USDT&side=BUY -H 'APEX-SIGNATURE: ***' -H 'APEX-TIMESTAMP: ***' -H 'APEX-API-KEY: ***' -H 'APEX-PASSPHRASE: ***' 
Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	true	Symbol
size	query	string	true	Order open size
side	query	string	true	BUY or SELL order
APEX-SIGNATURE	header	string	true	Request signature
APEX-TIMESTAMP	header	string	true	Request timestamp
APEX-API-KEY	header	string	true	apiKeyCredentials.key
APEX-PASSPHRASE	header	string	true	apiKeyCredentials.passphrase
Successful Response Generation

{
  "worstPrice": "123.00",
  "bidOnePrice": "123.00",
  "askOnePrice": "123.00"
}
Response Status Code
Status Code	Definition	Comment	Data Model
200	OK	Success	Inline
Response Parameters
Status Code 200

Parameter	Type	Required	Limit	Comment
» worstPrice	string	true	none	Lowest price
» bidOnePrice	string	true	none	Bid price
» askOnePrice	string	true	none	Ask price
PublicApi
v3.0.0
The API endpoints of Asset do not require authentication.

GET System Time
GET /v3/time

curl "https://omni.apex.exchange/api/v3/time" 
Successful Response

{
  "data": {
    "time": 1648626529
  }
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	Success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» time	integer	true	none	none
GET All Config Data
USDC and USDT config

GET /v3/symbols

curl "https://omni.apex.exchange/api/v3/symbols" 
Successful Response

{
    "spotConfig": {
        "assets": [
            {
                "tokenId": "17",
                "token": "USDC",
                "displayName": "USD Coin",
                "decimals": 18,
                "showStep": "0.01",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_USDC.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "35",
                "token": "BNB",
                "displayName": "BNB",
                "decimals": 18,
                "showStep": "0.001",
                "iconUrl": "https://static-pro.apex.exchange/icon/BNB.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "36",
                "token": "ETH",
                "displayName": "Ethereum",
                "decimals": 18,
                "showStep": "0.0001",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_ETH.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "140",
                "token": "USDT",
                "displayName": "Tether USD Coin",
                "decimals": 18,
                "showStep": "0.01",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_USDT.svg",
                "l2WithdrawFee": "0"
            }
        ],
        "global": {
            "defaultRegisterTransferToken": "USDT",
            "defaultRegisterTransferTokenId": "140",
            "defaultRegisterSubAccountId": "0",
            "defaultChangePubKeyZklinkChainId": "3",
            "defaultChangePubKeyFeeTokenId": "140",
            "defaultChangePubKeyFeeToken": "USDT",
            "defaultChangePubKeyFee": "0",
            "registerTransferLpAccountId": "577029250759000065",
            "registerTransferLpSubAccount": "0",
            "registerTransferLpSubAccountL2Key": "0x2924686165271a5de8248833a8ab7a6f7fb7f950d7512ecd56952283cc434d8c",
            "perpLpAccountId": "",
            "perpLpSubAccount": "",
            "perpLpSubAccountL2Key": "",
            "contractAssetPoolAccountId": "577390086971195406",
            "contractAssetPoolZkAccountId": "46",
            "contractAssetPoolSubAccount": "0",
            "contractAssetPoolL2Key": "0xa54a045e186e7e8635b1d444e14f59c86767c685bbfff92d6b7118113d845d2f",
            "contractAssetPoolEthAddress": "0xa50A3b5c5f6192742db99fA21d832ddd72D3028E"
        },
        "spot": [],
        "multiChain": {
            "chains": [
                {
                    "chain": "BNB Chain - Testnet",
                    "chainId": "3",
                    "chainType": "0",
                    "l1ChainId": "97",
                    "chainIconUrl": "https://l2dex-image-static.dev.apexplus.exchange/chains/chain_tokens/BSC/BNB_BNB.svg",
                    "contractAddress": "0x20F48e49549163976f974E8983Bb451E5Dcf53fD",
                    "stopDeposit": false,
                    "feeLess": false,
                    "gasLess": false,
                    "gasToken": "BNB",
                    "dynamicFee": true,
                    "feeGasLimit": 300000,
                    "blockTimeSeconds": 15,
                    "rpcUrl": "https://data-seed-prebsc-2-s1.binance.org:8545",
                    "webRpcUrl": "https://data-seed-prebsc-2-s1.binance.org:8545",
                    "webTxUrl": "https://testnet.bscscan.com/tx/",
                    "txConfirm": 15,
                    "withdrawGasFeeLess": false,
                    "tokens": [
                        {
                            "decimals": 6,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/USDT.svg",
                            "token": "USDT",
                            "tokenAddress": "0x01cb59f3c16fafe63955e4d435adafa23d9abbde",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "USDT",
                            "needResetApproval": true,
                            "minFee": "2",
                            "maxFee": "200",
                            "feeRate": "0.0001"
                        },
                        {
                            "decimals": 6,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/USDC.svg",
                            "token": "USDC",
                            "tokenAddress": "0xf35a44977e9831f564c9af3b721748e840c1ef4c",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "USDC",
                            "needResetApproval": true,
                            "minFee": "2",
                            "maxFee": "200",
                            "feeRate": "0.0001"
                        },
                        {
                            "decimals": 18,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/BNB.svg",
                            "token": "BNB",
                            "tokenAddress": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "BNB",
                            "needResetApproval": true,
                            "minFee": "0.00001",
                            "maxFee": "0.01",
                            "feeRate": "0.0001"
                        }
                    ]
                },
                {
                    "chain": "Base Sepolia Chain - Testnet",
                    "chainId": "11",
                    "chainType": "0",
                    "l1ChainId": "84532",
                    "chainIconUrl": "https://l2dex-image-static.dev.apexplus.exchange/chains/chain_logos/base.svg",
                    "contractAddress": "0x8cDdB93BD8845aE509a6eC1e29836852A9b41b10",
                    "stopDeposit": false,
                    "feeLess": false,
                    "gasLess": false,
                    "gasToken": "ETH",
                    "dynamicFee": true,
                    "feeGasLimit": 300000,
                    "blockTimeSeconds": 0,
                    "rpcUrl": "https://sepolia.base.org",
                    "webRpcUrl": "https://sepolia.base.org",
                    "webTxUrl": "https://sepolia.basescan.org/tx/",
                    "txConfirm": 15,
                    "withdrawGasFeeLess": false,
                    "tokens": [
                        {
                            "decimals": 6,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/USDT.svg",
                            "token": "USDT",
                            "tokenAddress": "0x2340c88808dce139b36864970074315bcb0c9fe0",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "USDT",
                            "needResetApproval": true,
                            "minFee": "2",
                            "maxFee": "200",
                            "feeRate": "0.0001"
                        },
                        {
                            "decimals": 6,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/USDC.svg",
                            "token": "USDC",
                            "tokenAddress": "0xaf3a3fd0eea662dd1aefa8b04c201038a4ff5761",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "USDC",
                            "needResetApproval": true,
                            "minFee": "2",
                            "maxFee": "200",
                            "feeRate": "0.0001"
                        },
                        {
                            "decimals": 18,
                            "iconUrl": "https://l2dex-image-static.dev.apexplus.exchange/icon/ETH.svg",
                            "token": "ETH",
                            "tokenAddress": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
                            "pullOff": false,
                            "withdrawEnable": true,
                            "slippage": "",
                            "isDefaultToken": false,
                            "displayToken": "ETH",
                            "needResetApproval": true,
                            "minFee": "0.00001",
                            "maxFee": "0.01",
                            "feeRate": "0.0001"
                        }
                    ]
                }
            ],
            "maxWithdraw": "",
            "minDeposit": "",
            "minWithdraw": ""
        }
    },
    "contractConfig": {
        "assets": [
            {
                "tokenId": "60017",
                "token": "USDC",
                "displayName": "USD Coin",
                "decimals": 18,
                "showStep": "0.01",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_USDC.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "60035",
                "token": "BNB",
                "displayName": "BNB",
                "decimals": 18,
                "showStep": "0.001",
                "iconUrl": "https://static-pro.apex.exchange/icon/BNB.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "60036",
                "token": "ETH",
                "displayName": "Ethereum",
                "decimals": 18,
                "showStep": "0.0001",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_ETH.svg",
                "l2WithdrawFee": "0"
            },
            {
                "tokenId": "60140",
                "token": "USDT",
                "displayName": "Tether USD Coin",
                "decimals": 18,
                "showStep": "0.0001",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/Ethereum/Ethereum_USDT.svg",
                "l2WithdrawFee": "0"
            }
        ],
        "tokens": [
            {
                "token": "BTC",
                "stepSize": "0.001",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/BTC.svg"
            },
            {
                "token": "EIGEN",
                "stepSize": "0.001",
                "iconUrl": "https://static-pro.apex.exchange/chains/chain_tokens/EIGEN.svg"
            }
        ],
        "global": {
            "feeAccountId": "",
            "feeAccountL2Key": "",
            "contractAssetLpAccountId": "",
            "contractAssetLpL2Key": "",
            "operationAccountId": "",
            "operationL2Key": "",
            "experienceMoneyAccountId": "",
            "experienceMoneyL2Key": "",
            "agentAccountId": "",
            "agentL2Key": "",
            "finxFeeAccountId": "",
            "finxFeeL2Key": "",
            "negativeRateAccountId": "",
            "negativeRateL2Key": "",
            "brokerAccountId": "",
            "brokerL2Key": ""
        },
        "perpetualContract": [
        {
                    "baselinePositionValue": "50000.0000",
                    "crossId": 30002,
                    "crossSymbolId": 10,
                    "crossSymbolName": "BTCUSDT",
                    "digitMerge": "0.1,0.2,0.4,1,2",
                    "displayMaxLeverage": "100",
                    "displayMinLeverage": "1",
                    "enableDisplay": true,
                    "enableOpenPosition": true,
                    "enableTrade": true,
                    "fundingImpactMarginNotional": "6",
                    "fundingInterestRate": "0.0003",
                    "incrementalInitialMarginRate": "0.00250",
                    "incrementalMaintenanceMarginRate": "0.00100",
                    "incrementalPositionValue": "50000.0000",
                    "initialMarginRate": "0.01",
                    "maintenanceMarginRate": "0.005",
                    "maxOrderSize": "50",
                    "maxPositionSize": "100",
                    "minOrderSize": "0.0010",
                    "maxMarketPriceRange": "0.025",
                    "settleAssetId": "USDT",
                    "baseTokenId": "BTC",
                    "stepSize": "0.001",
                    "symbol": "BTC-USDT",
                    "symbolDisplayName": "BTCUSDT",
                    "tickSize": "0.1",
                    "maxMaintenanceMarginRate": "0.5000",
                    "maxPositionValue": "5000000.0000",
                    "tagIconUrl": "https://static-pro.apex.exchange/icon/LABLE_HOT.svg",
                    "tag": "HOT",
                    "riskTip": false,
                    "defaultInitialMarginRate": "0.05",
                    "klineStartTime": 0,
                    "maxMarketSizeBuffer": "0.98",
                    "enableFundingSettlement": true,
                    "indexPriceDecimals": 2,
                    "indexPriceVarRate": "0.0005",
                    "openPositionOiLimitRate": "0.05",
                    "fundingMaxRate": "0.000234",
                    "fundingMinRate": "-0.000234",
                    "fundingMaxValue": "",
                    "enableFundingMxValue": true,
                    "l2PairId": "50001",
                    "settleTimeStamp": 0,
                    "isPrelaunch": false,
                    "riskLimitConfig": {
                        "positionSteps": [
                            "0",
                            "50000",
                            "100000",
                            "200000",
                            "300000",
                            "500000",
                            "1000000",
                            "2000000",
                            "3000000",
                            "4000000",
                            "5000000"
                        ],
                        "imrSteps": [
                            "0.01",
                            "0.01333",
                            "0.02",
                            "0.04",
                            "0.05",
                            "0.1",
                            "0.2",
                            "0.25",
                            "0.33333",
                            "0.5",
                            "1"
                        ],
                        "mmrSteps": [
                            "0.005",
                            "0.0065",
                            "0.01",
                            "0.02",
                            "0.025",
                            "0.05",
                            "0.1",
                            "0.125",
                            "0.15",
                            "0.25",
                            "0.5"
                        ]
                    }
}
        ],
        "prelaunchContract": [
            {
                "baselinePositionValue": "50000.0000",
                "crossId": 5,
                "crossSymbolId": 10,
                "crossSymbolName": "EIGENUSDT",
                "digitMerge": "0.5,1,2,5,10",
                "displayMaxLeverage": "30",
                "displayMinLeverage": "1",
                "enableDisplay": true,
                "enableOpenPosition": true,
                "enableTrade": true,
                "fundingImpactMarginNotional": "60",
                "fundingInterestRate": "0.0003",
                "incrementalInitialMarginRate": "0.00250",
                "incrementalMaintenanceMarginRate": "0.00100",
                "incrementalPositionValue": "200000.0000",
                "initialMarginRate": "0.03333",
                "maintenanceMarginRate": "0.00700",
                "maxOrderSize": "50",
                "maxPositionSize": "100",
                "minOrderSize": "0.0010",
                "maxMarketPriceRange": "0.025",
                "settleAssetId": "USDT",
                "baseTokenId": "EIGEN",
                "stepSize": "0.001",
                "symbol": "EIGEN-USDT",
                "symbolDisplayName": "EIGENUSDT",
                "tickSize": "0.5",
                "maxMaintenanceMarginRate": "0.03000",
                "maxPositionValue": "10050000.0000",
                "tagIconUrl": "",
                "tag": "",
                "riskTip": false,
                "defaultLeverage": "",
                "klineStartTime": 0,
                "maxMarketSizeBuffer": "0.98",
                "enableFundingSettlement": true,
                "indexPriceDecimals": 2,
                "indexPriceVarRate": "0.0005",
                "openPositionOiLimitRate": "0.05",
                "fundingMaxRate": "0.000234",
                "fundingMinRate": "-0.000234",
                "fundingMaxValue": "",
                "enableFundingMxValue": true,
                "l2PairId": "60001",
                "settleTimeStamp": 1000000,
                "isPrelaunch": true,
                "riskLimitConfig": {
                    "positionSteps": null,
                    "imrSteps": null,
                    "mmrSteps": null
                }
            }
        ],
        "maxMarketBalanceBuffer": "0.98"
    }
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	type	required	limit	comment
» spotConfig	object	true	none	Spot trade config
»» assets	[object]	true	none	Spot trade assets
»»» tokenId	string	true	none	ZK token ID
»»» token	string	true	none	ZK token name
»»» displayName	string	true	none	ZK token displayName
»»» decimals	integer	true	none	Contract token decimal point accuracy
»»» showStep	string	true	none	Token show decimals
»»» iconUrl	string	true	none	Token icon url
»»» l2WithdrawFee	string	true	none	Token withdraw fee
»» global	object	true	none	
»»» defaultRegisterTransferToken	string	true	none	Default transfer token, as 'USDT'
»»» defaultRegisterTransferTokenId	string	true	none	Default transfer zk token ID, as '141'
»»» defaultRegisterSubAccountId	string	true	none	Default transfer zk sub account ID, as '0'
»»» defaultChangePubKeyZklinkChainId	string	true	none	Default transfer zk chain ID, as '9'
»»» defaultChangePubKeyFeeTokenId	string	true	none	Default change pub key fee token ID, as '141'
»»» defaultChangePubKeyFeeToken	string	true	none	Default change pub key fee token, as 'USDT'
»»» defaultChangePubKeyFee	string	true	none	Default change pub key fee, as '0'
»»» registerTransferLpAccountId	string	true	none	transfer Lp account ID
»»» registerTransferLpSubAccount	string	true	none	transfer Lp sub account ID
»»» registerTransferLpSubAccountL2Key	string	true	none	transfer Lp account l2Key
»»» perpLpAccountId	string	true	none	Perp Lp account ID
»»» perpLpSubAccount	string	true	none	Perp Lp sub account ID
»»» perpLpSubAccountL2Key	string	true	none	Perp Lp account l2Key
»»» contractAssetPoolAccountId	string	true	none	Contract asset pool account ID
»»» contractAssetPoolZkAccountId	string	true	none	Contract asset pool zk account ID
»»» contractAssetPoolSubAccount	string	true	none	Contract asset pool sub account ID
»»» contractAssetPoolL2Key	string	true	none	Contract asset pool account l2Key
»»» contractAssetPoolEthAddress	string	true	none	Contract asset pool eth address
»» spot	[string]	true	none	Spot symbols
»» multiChain	object	true	none	none
»»» maxWithdraw	string	true	none	Maximum withdrawal amount
»»» minWithdraw	string	true	none	Minimum withdrawal amount
»»» minDeposit	string	true	none	Minimum deposit amount
»»» currency	string	true	USDC	Currency
»»» chains	[object]	true	none	none
»»»» chain	string	true	none	Chain
»»»» contractAddress	string	true	none	Contract address
»»»» chainIconUrl	string	true	none	Chain icon url
»»»» gasToken	string	true	none	Gas token name
»»»» rpcUrl	string	true	none	Chain RPC service Url
»»»» chainId	integer	true	none	Chain ID
»»»» feeLess	boolean	true	none	Enable trading fees
»»»» depositGasFeeLess	boolean	false	none	Enable deposit gas fees
»»»» withdrawGasFeeLess	boolean	false	none	Enable withdraw gas fees
»»»» minFee	string	true	none	Minimum deposit gas fee: If gas+value*fee_rate is lesser than min_fee, min_fee amount will be charged instead
»»»» feeRate	string	true	none	Fee rate
»»»» webTxUrl	string	true	none	Transaction tx URL
»»»» tokens	[object]	true	none	none
»»»»» token	string	true	none	Token name
»»»»» tokenAddress	string	true	none	Token address
»»»»» decimals	integer	true	none	Token decimal point accuracy
»»»»» iconUrl	string	true	none	Token icon URL
»»»»» pullOff	bool	true	none	Enable taking down of listing, default as FALSE
»»»» gasLess	boolean	true	none	Enable gas free transaction
»»»»» withdrawEnable	boolean	true	none	Enable withdraw
»»»»» slippage	string	true	none	Swap slippage
»»»»» isDefaultToken	boolean	true	none	If it is default token
»»»»» displayToken	string	true	none	Display token name
»»»»» needResetApproval	boolean	true	none	If it is need to reset approval
»»»»» maxFee	string	true	none	Max deposit gas fee
» contractConfig	object	true	none	Contract trade Config
»» assets	[object]	true	none	Contract trade assets
»»» tokenId	string	true	none	ZK token ID
»»» token	string	true	none	ZK token name
»»» displayName	string	true	none	ZK token displayName
»»» decimals	integer	true	none	Contract token decimal point accuracy
»»» showStep	string	true	none	Token show decimals
»»» iconUrl	string	true	none	Token icon url
»»» l2WithdrawFee	string	true	none	Token withdraw fee
»» tokens	[object]	true	none	Contract trade tokens
»»» token	string	true	none	Contract trade token name
»»» stepSize	string	true	none	Minimum step size
»»» iconUrl	string	true	none	Contract trade token icon URL
»» global	object	true	none	Contract trade global config
»»» feeAccountId	string	true	none	Contract fee account ID
»»» feeAccountL2Key	string	true	none	Contract fee account L2Key
»»» contractAssetLpAccountId	string	true	none	Contract asset Lp account ID
»»» contractAssetLpL2Key	string	true	none	Contract asset Lp account l2Key
»»» operationAccountId	string	true	none	Contract operation account ID
»»» operationL2Key	string	true	none	Contract operation account l2Key
»»» experienceMoneyAccountId	string	true	none	Contract experience money account ID
»»» experienceMoneyL2Key	string	true	none	Contract experience money l2Key
»»» agentAccountId	string	true	none	Contract agent account ID
»»» agentL2Key	string	true	none	Contract agent account l2Key
»»» finxFeeAccountId	string	true	none	Contract finx account ID
»»» finxFeeL2Key	string	true	none	Contract finx account l2Key
»»» negativeRateAccountId	string	true	none	Contract negative rate account ID
»»» negativeRateL2Key	string	true	none	Contract negative rate account l2Key
»»» brokerAccountId	string	true	none	Contract broker account ID
»»» brokerL2Key	string	true	none	Contract broker account l2Key
»» prelaunchContract	[object]	true	none	Prelaunch contract symbols
»» perpetualContract	[object]	true	none	Perpetual contract symbols
»»» baselinePositionValue	string	false	none	Baseline position vaue
»»» crossId	integer	false	none	Quote API use id for symbol
»»» crossSymbolId	integer	false	none	Quote API use symbolId for symbol
»»» crossSymbolName	string	false	none	Quote API use symbolName for symbol
»»» digitMerge	string	false	none	Depth digit merge
»»» displayMaxLeverage	string	false	none	Maximum leverage
»»» displayMinLeverage	string	false	none	Minimum leverage
»»» enableDisplay	boolean	false	none	Enable display
»»» enableOpenPosition	boolean	false	none	Enable open position
»»» enableTrade	boolean	false	none	Enable trade
»»» fundingImpactMarginNotional	string	false	none	Not required on frontend
»»» fundingInterestRate	string	false	none	Funding rate ratio
»»» incrementalInitialMarginRate	string	false	none	
»»» incrementalMaintenanceMarginRate	string	false	none	
»»» incrementalPositionValue	string	false	none	Incremental position value
»»» initialMarginRate	string	false	none	Incremental initial margin rate
»»» maintenanceMarginRate	string	false	none	Incremental maintenance margin rate
»»» maxOrderSize	string	false	none	Maximum order size
»»» maxPositionSize	string	false	none	Maximum position size
»»» minOrderSize	string	false	none	Minimum order size
»»» maxMarketPriceRange	string	false	none	Maximum market price rangee
»»» settleAssetId	string	false	none	Settlement asset id
»»» baseTokenId	string	false	none	
»»» stepSize	string	false	none	Minimum step size
»»» symbol	string	false	none	
»»» symbolDisplayName	string	false	none	Symbol display name
»»» tickSize	string	false	none	Minimum tick size
»»» maxMaintenanceMarginRate	string	false	none	Maximum maintenance margin rate
»»» maxPositionValue	string	false	none	Maximum position value
»»» tagIconUrl	string	false	none	Tag icon URL
»»» tag	string	false	none	Symbol Tag
»»» riskTip	boolean	false	none	If it has risk tips
»»» defaultLeverage	string	false	none	Default trade leverage
»»» maxMarketSizeBuffer	string	false	none	Maximum market trade size buffer
»»» enableFundingSettlement	boolean	false	none	Enable funding settlement
»»» indexPriceDecimals	integer	false	none	Index price decimals
»»» indexPriceVarRate	string	false	none	Index price var rate
»»» openPositionOiLimitRate	string	false	none	Open position oi limit rate
»»» fundingMaxRate	string	false	none	Funding maximum rate
»»» fundingMinRate	string	false	none	Funding minimum rate
»»» fundingMaxValue	string	false	none	Funding maximum value
»»» enableFundingMxValue	boolean	false	none	Enable funding maximum value
»»» l2PairId	string	false	none	zk l2 pair Id
»»» settleTimeStamp	integer	false	none	Settle time
»»» isPrelaunch	boolean	false	none	If it is prelaunch symbol
»»» riskLimitConfig	object	false	none	Risk Limit config
»»»» positionSteps	null	true	none	Position steps
»»»» imrSteps	null	true	none	Initial margin rate steps
»»»» mmrSteps	null	true	none	Maintenance margin rate steps
GET Market Depth
GET /v3/depth

Retrieve all active orderbook for one symbol, inclue all bids and asks.

Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	true	use crossSymbolName responded from All Config Data
limit	query	string	false	Default at 100
curl "https://omni.apex.exchange/api/v3/depth?symbol=BTCUSDT" 
Successful Response Generation

success

{
  "data": {
    "a": [
      [
        "98743.4",
        "0.071"
      ],
      [
        "98743.5",
        "0.035"
      ]
    ],
    "b": [
      [
        "98742.3",
        "0.529"
      ],
      [
        "98742.2",
        "0.178"
      ]
    ],
    "s": "BTCUSDT",
    "u": 1076833
  },
  "timeCost": 1056809
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» data	[object]	true	none	none
»» a	[array]	false	none	Sell
»» b	[array]	false	none	Buy
»» s	string	false	none	Symbol
»» u	integer	false	none	none
GET Newest Trading Data
GET /v3/trades

Retrieve trading data.

Request Parameters
Parameter	Position	type	required	comment
symbol	query	string	true	use crossSymbolName responded from All Config Data
limit	query	string	false	Limit, maximum is 500
curl "https://omni.apex.exchange/api/v3/trades?symbol=BTCUSDT" 
Successful Response Generation

success

{
  "data": [
    {
      "S": "BUY",
      "v": "0.001",
      "p": "29000",
      "s": "BTCUSDT",
      "T": 1647502440973
    }
  ]
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» data	[object]	true	none	none
»» S	string	false	none	Side
»» v	string	false	none	Size
»» p	string	false	none	Price
»» s	string	false	none	Symbol
»» T	integer	false	none	Trade time
GET Candlestick Chart Data
GET /v3/klines

Retrieves all candlestick chart data.
Candlestick chart time indicators: Numbers represent minutes, D for Days, M for Month and W for Week — 1 5 15 30 60 120 240 360 720 "D" "M" "W"

Request Parameters
Parameter	Position	Type	Required	Comment
interval	query	string	false	Candlestick chart time indicators: Numbers represent minutes, D for Days, M for Month and W for Week — 1 5 15 30 60 120 240 360 720 "D" "M" "W"
start	query	string	false	Start time, second timestamp
end	query	string	false	End time, second timestamp
limit	query	string	false	Limit, maximum is 200
symbol	query	string	false	use crossSymbolName responded from All Config Data
curl "https://omni.apex.exchange/api/v3/klines?symbol=BTCUSDT&interval=5" 
Successful Response Generation

success

{
  "data": [
    {
      "start": 1647511440000,
      "symbol": "BTCUSDC",
      "interval": "1",
      "low": "40000",
      "high": "45000",
      "open": "45000",
      "close": "40000",
      "volume": "1.002",
      "turnover": "3"
    }
  ]
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» klines	[object]	true	none	none
»» start	integer	false	none	Start time
»» symbol	string	true	none	Currency
»» interval	string	true	none	Chart interval
»» low	string	false	none	Low price
»» high	string	false	none	High price
»» open	string	false	none	Open price
»» close	string	false	none	Close price
»» volume	string	false	none	Trading volume
»» turnover	string	false	none	Turnover
GET Ticker Data
GET /v3/ticker

Get the latest data on symbol tickers.

Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	true	use crossSymbolName responded from All Config Data
curl "https://omni.apex.exchange/api/v3/ticker?symbol=BTCUSDT" 
Successful Response Generation

success

{
  "data": [
    {
      "symbol": "BTCUSDT",
      "price24hPcnt": "0.450141",
      "lastPrice": "43511.50",
      "highPrice24h": "43513.50",
      "lowPrice24h": "29996.00",
      "markPrice": "43513.50",
      "indexPrice": "40828.94",
      "openInterest": "2036854775808",
      "turnover24h": "5626085.23749999",
      "volume24h": "169.317",
      "fundingRate": "0",
      "predictedFundingRate": "0",
      "nextFundingTime": "10:00:00",
      "tradeCount": 100
    }
  ]
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» tickers	[object]	true	none	none
»» symbol	string	false	none	Symbol
»» price24hPcnt	string	false	none	24H change (%)
»» lastPrice	string	false	none	Last price
»» highPrice24h	string	false	none	24H highest price
»» lowPrice24h	string	false	none	24H lowest price
»» markPrice	string	false	none	mark price
»» indexPrice	string	false	none	Index price
»» openInterest	string	false	none	Open interest
»» turnover24h	string	false	none	24H turnover
»» volume24h	string	false	none	24H trading volume
»» fundingRate	string	false	none	Funding rate
»» predictedFundingRate	string	false	none	Predicted funding rate
»» nextFundingTime	string	false	none	Next funding rate
»» tradeCount	string	false	none	24H trade count
GET Funding Rate History
GET /v3/history-funding

Request Parameters
Parameter	Position	Type	Required	Comment
symbol	query	string	true	use crossSymbolName responded from All Config Data
Limit	query	string	false	Default at 100
beginTimeInclusive	query	string	false	Start time
endTimeExclusive	query	string	false	End time
page	query	string	false	Page numbers start from 0
curl "https://omni.apex.exchange/api/v3/history-funding?symbol=BTC-USDT" 
Successful Response Generation

success

{
  "historyFunds": [
    {
      "symbol": "BTC-USDT",
      "rate": "0.0000125000",
      "price": "31297.5000008009374142",
      "fundingTime": 12315555,
      "fundingTimestamp": 12315555
    }
  ],
  "totalSize": 11
}
Response Status Code
Status Code	Value	Comment	Data Model
200	OK	success	Inline
Response Parameters
status code 200

Parameter	Type	Required	Limit	Comment
» historicalFunds	[object]	true	none	none
»» symbol	string	false	none	none
»» rate	string	false	none	Funding rate
»» price	string	false	none	Price
»» fundingTime	integer	false	none	Time
»» fundingTimestamp	integer	false	none	Funding timestamp
» totalSize	integer	true	none	Size
Public Websocket
 For connection details, please refer to the WebSocket Endpoint.
Due to network complexity, your may get disconnected at any time. Please follow the instructions below to ensure that you receive WebSocket messages on time:

Keep connection alive by sending heartbeat packet
Reconnect as soon as possible if disconnected
How to Send

ws.send('{"op":"ping","args":["1661415022821"]}');
Response Example

'{"op":"pong","args":["1661415030233"]}'
wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"ping","args":["1756831783000"]}
When receiving a ping message from the server, a pong message needs to be returned to the server.

ws.send('{"op":"pong","args":["1661415022821"]}');
Heartbeat Packet
To avoid networks or program issues, we recommend that you send the ping heartbeat packet every 15 seconds to maintain the WebSocket connection.

Server Check With Ping Pong Test:

Check the connection ever 15 seconds and look at the client timestamp
If the difference between the client timestamp and the current timestamp exceeds 150s, the connection will be closed
How to Subscribe to Topics
Understanding Websocket Filters
After establishing the connection, one can subscribe to a new topic by sending a JSON request. The specific formats are as follows:

ws.send('{"op": "subscribe", "args": ["topic.filter"]}'); 
The topic indicates the data you would like to receive whilst the filter parses for the specific data you desire, for example, the symbol. The topic is mandatory but the filter is optional.
To subscribe to more than one topic, simply list multiple topics out like this:

ws.send('{"op": "subscribe", "args": ["topic.filter", "topic.filter"]}');
Unsubscribing From Websocket Topics
You can dynamically subscribe and unsubscribe from topics (with or without filters) without websocket disconnection as follows:

ws.send('{"op": "unsubscribe", "args": ["topic.filter", "topic.filter"]}');
Intervals
Some topics are pushed out at specific intervals. If the args contains a millisecond parameter, such as 100ms, this topic is pushed at intervals. Otherwise, topis will be pushed constantly.

Understanding Subscription Response
Each subscription will have a response. You can determine whether the subscription is successful based on the response.

{
        "success":true, 
        "ret_msg":"",
        "conn_id":"647c3de8-6f66-44ab-a323-72067589372e",
        "request":{
            "op":"subscribe",
            "args":[
            "instrumentInfo.H.BTCUSDT"
        ]
        }
}
Depth
Fetches the orderbook with a depth of 25 or 200 orders per side.

After the subscription response, the first response will be the snapshot response. This shows the entire order book. The data is sorted by price, starting with the lowest buys and ending with the highest sells.

Following this, all responses are in the delta format, which represents updates to the order book relative to the last response.

Request Parameters
Parameter	Type	Limit	Comment
» op	string	true	Subscribe
» args	string	true	Order book
» limit	string	true	25 or 200
» frequency	string	true	H means High frequency, M means middle frequency
» symbol	string	true	Symbol
How to Subscribe

wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"subscribe","args":["orderBook200.H.BTCUSDT"]}
< {
    "topic":"orderBook200.H.BTCUSDT",
    "type":"delta",
    "data":{
        "s":"BTCUSDT",
        "b":[
            [
                "18990.5",
                "0"
            ],
            [
                "18979.5",
                "0"
            ]
        ],
        "a":[
            [
                "19010.5",
                "0"
            ],
            [
                "19037.5",
                "0"
            ]
        ],
        "u":249003
    },
    "cs":44132980,
    "ts":1661416027956272
  }
Response data
Parameter	Type	Comment
» topic	string	Same as request args
» type	string	Snapshot or delta
» s	string	Symbol
» u	int	Update ID: According to whether the Update ID is continuous, the client will need to determine if there is a packet loss in the process of receiving data. Snapshot resets the Update ID and it will start counting again from 1.
» b	array	Buy[price,size], size set as 0 will delete this item
» a	array	Sell[price,size], size set as 0 will delete this item
Trade
Get trades for a specific symbol.

TickDirection
The TickDirection can be one of the following values:

PlusTick
ZeroPlusTick
MinusTick
ZeroMinusTick
Request Parameters
Parameter	Type	Limit	Comment
» op	string	true	Subscribe
» args	string	true	Recently trade
» frequency	string	true	H means High frequency, M means middle frequency
» symbol	string	true	Symbol
How to Subscribe

wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"subscribe","args":["recentlyTrade.H.BTCUSDT"]}
< {
    "topic":"recentlyTrade.H.BTCUSDT",
    "type":"snapshot",
    "data":[
        {
            "T":1647502440973,
            "s":"BTCPERP",
            "S":"Buy",
            "v":"1.000",
            "p":"43513.00",
            "L":"PlusTick",
            "i":"a3afbef7-d8de-5b87-a32f-d06f041a249d"
        }
    ],
    "cs":44132980,
    "ts":1661416027956272
  }
Response data
Parameter	Type	Comment
» topic	string	Same as request args
» type	string	Snapshot
» s	string	Symbol
» T	int	Timestamp
» S	string	Buy or Sell
» v	string	Volume
» p	string	Price
» L	string	Tick direction
» i	string	uuid
Ticker
Get latest information for symbol.

This topic only utilizes the update field. Both the delete and insert fields are null. If a key is not found in the update field, its value has not changed.

Request Parameters
Parameter	Type	Limit	Comment
» op	string	true	Subscribe
» args	string	true	Instrument info
» frequency	string	true	H means High frequency, M means middle frequency
» symbol	string	true	Symbol
How to Subscribe

wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"subscribe","args":["instrumentInfo.H.BTCUSDT"]}
< {
    "topic":"instrumentInfo.H.BTCUSDT",
        "type":"snapshot",
        "data":{
        "symbol":"BTCUSDT",
            "lastPrice":"21572.5",
            "price24hPcnt":"-0.0194318181818182",
            "highPrice24h":"25306.5",
            "lowPrice24h":"17001.5",
            "turnover24h":"1334891.4545",
            "volume24h":"64.896",
            "nextFundingTime":"2022-08-26T08:00:00Z",
            "oraclePrice":"21412.060000000002752512",
            "indexPrice":"21409.82",
            "openInterest":"49.598",
            "tradeCount":"0",
            "fundingRate":"0.0000125",
            "predictedFundingRate":"0.0000125"
    },
    "cs":44939063,
        "ts":1661500091955487
  }
Response data
Parameter	Type	Comment
» topic	string	Same as request args
» type	string	Snapshot or delta
»» symbol	string	Symbol
»» price24hPcnt	string	24H change (%)
»» lastPrice	string	Last price
»» highPrice24h	string	24H highest price
»» lowPrice24h	string	24H lowest price
»» oraclePrice	string	Oracle price
»» indexPrice	string	Index price
»» openInterest	string	Open interest
»» turnover24h	string	24H turnover
»» volume24h	string	24H trading volume
»» fundingRate	string	Funding rate
»» predictedFundingRate	string	Predicted funding rate
»» nextFundingTime	string	Next funding rate
»» tradeCount	string	24H trade count
Candlestick Chart
Currently supported intervals:

1 3 5 15 30
60 120 240 360 720
D
W
M
If confirm is true, this will indicate the last ticker price within the specified interval.

request
Parameter	Type	Limit	Comment
» op	string	true	Subscribe
» args	string	true	Candle
» interval	string	true	Interval
» symbol	string	true	Symbol
How to Subscribe

wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"subscribe","args":["candle.1.BTCUSDT"]}
< {
    "topic":"candle.1.BTCUSDT",
        "data":[
        {
            "start":1647511440000,
            "end":1647511499999,
            "interval":"1",
            "open":"44111",
            "close":"44111",
            "high":"44111",
            "low":"44111",
            "volume":"0",
            "turnover":"0",
            "confirm":true,
            "time":1647511500752
        }
    ],
        "ts":1647511500752,
        "type":"snapshot"
  }
Response data
Parameter	Type	Comment
» topic	string	Same as request args
» type	string	Snapshot or delta
»» start	integer	Start time
»» symbol	string	Symbol
»» interval	string	Candlestick chart time indicators: Numbers represent minutes, D for Days, M for Month and W for Week — 1 5 15 30 60 120 240 360 720 "D" "M" "W"
»» low	string	Low price
»» high	string	High price
»» open	string	Open price
»» close	string	Close price
»» volume	string	Trading volume
»» turnover	string	Turnover
»» confirm	string	If it is the last tick of this candle
»» time	string	Current time
All Tickers
Get latest information for all symbols.

This topic only utilizes the update field. Both the delete and insert fields are null. If a key is not found in the update field, its value has not changed.

Request
Parameter	Type	Limit	Comment
» op	string	true	Subscribe
» args	string	true	Instrument info
» frequency	string	true	H means High frequency, M means middle frequency
» symbol	string	true	Symbol
How to Subscribe

wscat -c wss://quote.omni.apex.exchange/realtime_public?v=2&timestamp=1661415017232
> {"op":"subscribe","args":["instrumentInfo.all"]}
< {
    "topic":"instrumentInfo.all",
        "data":[
        {
            "s":"LINKUSDT",
            "p":"6.966",
            "pr":"-0.0510829587249694",
            "h":"7.401",
            "l":"6.931",
            "op":"6.966",
            "xp":"6.965",
            "to":"37279.7137",
            "v":"5128.7",
            "fr":"0.0000125",
            "o":"5647.1",
            "tc":"0"
        },
        {
            "s":"BTCUSDT",
            "p":"21572.5",
            "pr":"-0.0194318181818182",
            "h":"25306.5",
            "l":"17001.5",
            "op":"21412.060000000002752512",
            "xp":"21409.83",
            "to":"1334891.4545",
            "v":"64.858",
            "fr":"0.0000125",
            "o":"49.598",
            "tc":"0"
        },
        {
            "s":"ETHUSDT",
            "p":"1680.45",
            "pr":"-0.0150631538844767",
            "h":"1805.65",
            "l":"1680.45",
            "op":"1654.64",
            "xp":"1654.1",
            "to":"664502.346",
            "v":"389.16",
            "fr":"0.0000125",
            "o":"375.87",
            "tc":"0"
        },
        {
            "s":"DOGEUSDT",
            "p":"0.0621",
            "pr":"-0.1013024602026049",
            "h":"0.1481",
            "l":"0.0501",
            "mp":"0.06773",
            "xp":"0.0677",
            "to":"5007.69",
            "v":"70977",
            "fr":"0.0000125",
            "o":"43216",
            "tc":"0"
        }
    ],
        "type":"snapshot",
        "ts":1661500091389816
}
Response data
Parameter	Type	Comment
» topic	string	Same as request args
»» s	string	Symbol
»» pr	string	24H change (%)
»» p	string	Last price
»» h	string	24H highest price
»» l	string	24H lowest price
»» mp	string	Mark price
»» xp	string	Index price
»» o	string	Open interest
»» to	string	24H turnover
»» v	string	24H trading volume
»» fr	string	Funding rate
»» tc	string	24H trade count
Private Websocket
 For connection details, please refer to the WebSocket Endpoint.
Send Authority Request
Use apiKeyCredentials.secret sign, the rule as code
The topic can be subscribed to during authentication
Send authority request
After each successful subscription, the client will receive the snapshot (full data)
Type : snapshot means full data, delta means incremental data. If it is none, type will default to snapshot.

const apiKeyCredentials = {"key":"f6c1e736-fa6b-01df-2822-b9359b3918ae","secret":"sAVchdqy_n9zY7TOIDsqkyg0we3uF0_gGbvyIoob","passphrase":"Ri08mFrOt2Uaiym"}
const timestamp = 1647502440973;
const request_path = '/ws/accounts';
const http_method = 'GET';
const messageString: string = (
    timestamp +
    http_method +
    request_path);

const key = Buffer.from(this.apiKeyCredentials.secret).toString('base64');
const hash = cryptojs.HmacSHA256(messageString, key);
const signature = hash.toString(cryptojs.enc.Base64);

//auth sign
const req = {
    'type': 'login',
    'topics': ['ws_notify_v1','ws_zk_accounts_v3'], 
    'httpMethod':http_method,
    'requestPath':request_path,
    'apiKey': apiKeyCredentials['key'],
    'passphrase': apiKeyCredentials['passphrase'],
    'timestamp': timestamp,
    'signature': signature,
}

sendStr = {
                "op": "login",
                "args": [JSON.stringify(req)]
            }
websocket.send(JSON.stringify(sendStr));


//add subscribe
websocket.send(JSON.stringify({"op":"subscribe","args":["ws_zk_accounts_v3", "ws_notify_v1"]}));

//cancel subscribe
websocket.send({"op":"unsubscribe","args":["ws_zk_accounts_v3","ws_notify_v1"]});
Response Errors：

request param error
{"success":false,"ret_msg":"msg param error","conn_id":"xxxxxxxxxxsasad"}

user authority error
{"success":false,"ret_msg":"login authority err,"conn_id":"xxxxxxxxxxsasad"}

Subscription Success Push Data
    {
  "contractAccounts": [
    {
      "l2Key": "0x711df5ffc57b033b22c65e38e4b3d8b1947eaee7403aaa4ff5847d31ca0b0700",
      "accountId": "584232029671915612",
      "createdAt": 1717953051513,
      "makerFeeRate": "0.00000000",
      "takerFeeRate": "0.00025",
      "unrealizePnlPriceType": "MARKET_PRICE",
      "userId": "1213724853023293440",
      "updatedAt": 1718452222267,
      "status": "NORMAL"
    }
  ],
  "spotWallets": [
    {
      "accountId": "584232029671915612",
      "pendingDepositAmount": "0.000000000000000000",
      "subAccountId": "0",
      "balance": "28994.971947673600000001",
      "pendingWithdrawAmount": "0.000000000000000000",
      "pendingTransferInAmount": "0.000000000000000000",
      "pendingTransferOutAmount": "0.000000000000000000",
      "userId": "1213724853023293440",
      "token": "USDT"
    }
  ],
  "spotAccounts": [
    {
      "accountId": "584232029671915612",
      "createdAt": 1717128570381,
      "subAccounts": [
        {
          "l2Key": "0x711df5ffc57b033b22c65e38e4b3d8b1947eaee7403aaa4ff5847d31ca0b0700",
          "nonceVersion": 0,
          "changePubKeyStatus": "FINISH",
          "subAccountId": "0",
          "nonce": 10
        }
      ],
      "defaultSubAccountId": "0",
      "zkAccountId": "229",
      "userId": "1213724853023293440",
      "ethAddress": "0xc4c5036b68a42d8f1c6ba9ba8e5dd49ad5c1ef5c",
      "nonce": 1,
      "updatedAt": 1718789127665,
      "status": "NORMAL"
    }
  ],
  "transfers": [],
  "positionClosedTransactions": [],
  "orders": [
    {
      "cumSuccessLiquidateFee": "0",
      "symbol": "BTC-USDT",
      "openSlParams": {
        "triggerSize": "",
        "triggerPrice": "",
        "triggerPriceType": "UNKNOWN_PRICE_TYPE"
      },
      "cumSuccessFillFee": "0",
      "type": "STOP_MARKET",
      "isPositionTpsl": true,
      "isDeleverage": false,
      "createdAt": 1718104870661,
      "isSetOpenTp": false,
      "price": "52200.0",
      "cumSuccessFillValue": "0",
      "id": "588326929847812444",
      "cancelReason": "UNKNOWN_ORDER_CANCEL_REASON",
      "timeInForce": "IMMEDIATE_OR_CANCEL",
      "updatedAt": 1718104870661,
      "limitFee": "0.270000000000000000",
      "side": "SELL",
      "clientId": "4171300479007599",
      "triggerPrice": "58000",
      "triggerPriceType": "MARKET",
      "expiresAt": 1720523854,
      "openTpParams": {
        "triggerSize": "",
        "triggerPrice": "",
        "triggerPriceType": "UNKNOWN_PRICE_TYPE"
      },
      "cumSuccessFillSize": "0",
      "accountId": "584232029671915612",
      "size": "0.010",
      "reduceOnly": true,
      "isSetOpenSl": false,
      "isLiquidate": false,
      "remainingSize": "0.010",
      "status": "UNTRIGGERED"
    },
    {
      "cumSuccessLiquidateFee": "0",
      "symbol": "BTC-USDT",
      "openSlParams": {
        "triggerSize": "",
        "triggerPrice": "",
        "triggerPriceType": "UNKNOWN_PRICE_TYPE"
      },
      "cumSuccessFillFee": "0",
      "type": "TAKE_PROFIT_MARKET",
      "isPositionTpsl": true,
      "isDeleverage": false,
      "createdAt": 1718104870651,
      "isSetOpenTp": false,
      "price": "86900.0",
      "cumSuccessFillValue": "0",
      "id": "588326929805869404",
      "cancelReason": "UNKNOWN_ORDER_CANCEL_REASON",
      "timeInForce": "IMMEDIATE_OR_CANCEL",
      "updatedAt": 1718104870651,
      "limitFee": "0.440000000000000000",
      "side": "SELL",
      "clientId": "8086734464495621",
      "triggerPrice": "79000",
      "triggerPriceType": "MARKET",
      "expiresAt": 1720523854,
      "openTpParams": {
        "triggerSize": "",
        "triggerPrice": "",
        "triggerPriceType": "UNKNOWN_PRICE_TYPE"
      },
      "cumSuccessFillSize": "0",
      "accountId": "584232029671915612",
      "size": "0.010",
      "reduceOnly": true,
      "isSetOpenSl": false,
      "isLiquidate": false,
      "remainingSize": "0.010",
      "status": "UNTRIGGERED"
    }
  ],
  "positions": [
    {
      "symbol": "BTC-USDT",
      "exitPrice": "0",
      "side": "LONG",
      "openValue": "710.000000000000000000",
      "sumOpen": "0.011",
      "fundingFee": "-2.094765226613730193",
      "sumClose": "0",
      "entryPrice": "64545.454545454545454545",
      "accountId": "584232029671915612",
      "customImr": "0.05000",
      "size": "0.011",
      "realizedPnl": "0",
      "updatedAt": 1718104870634
    },
    {
      "symbol": "BTC-USDT",
      "exitPrice": "0",
      "side": "SHORT",
      "openValue": "0.000000000000000000",
      "sumOpen": "0",
      "fundingFee": "0",
      "sumClose": "0",
      "entryPrice": "0",
      "accountId": "584232029671915612",
      "customImr": "0.05000",
      "size": "0.000",
      "realizedPnl": "0",
      "updatedAt": 1718099221473
    }
  ],
  "experienceMoney": [
    {
      "totalAmount": "0.000000000000000000",
      "totalNumber": "0",
      "recycledAmount": "0.000000000000000000",
      "availableAmount": "0.000000000000000000",
      "token": "USDT"
    }
  ],
  "contractWallets": [
    {
      "pendingDepositAmount": "0.000000000000000000",
      "balance": "281.891287099786269807",
      "pendingWithdrawAmount": "0.000000000000000000",
      "pendingTransferInAmount": "0",
      "pendingTransferOutAmount": "0",
      "token": "USDT"
    }
  ],
  "deleverages": [
    {
      "symbol": "BTC-USDT",
      "lightNumber": "5",
      "side": "LONG"
    }
  ],
  "fills": []
}

Response Parameters
Parameter	Type	Required	Limit	Comment
» contents	object	true	none	
»» contractAccounts	[object]	true	none	
»»» l2Key	string	false	none	User's account l2Key
»»» accountId	string	false	none	User's account ID
»»» createdAt	integer	false	none	User's account create time
»»» makerFeeRate	string	false	none	Maker fee rate
»»» takerFeeRate	string	false	none	Taker fee rate
»»» unrealizePnlPriceType	string	false	none	User unrealize Pnl price type, as 'MARKET_PRICE'
»»» userId	string	false	none	User's user ID
»»» updatedAt	integer	false	none	User's account update time
»»» status	string	false	none	User's account status
»» spotWallets	[object]	true	none	User's spot account
»»» accountId	string	false	none	User's account ID
»»» pendingDepositAmount	string	false	none	Pending deposit amount
»»» subAccountId	string	false	none	User's sub account ID
»»» balance	string	false	none	Asset balance
»»» pendingWithdrawAmount	string	false	none	Pending withdraw amount
»»» pendingTransferInAmount	string	false	none	Pending transfer in amount
»»» pendingTransferOutAmount	string	false	none	Pending transfer out amount
»»» userId	string	false	none	User's user ID
»»» token	string	false	none	Asset token name
»» spotAccounts	[object]	true	none	
»»» accountId	string	false	none	User's account ID
»»» createdAt	integer	false	none	User's spot account create time
»»» subAccounts	[object]	false	none	User's sub accounts
»»»» l2Key	string	false	none	User's sub account l2Key
»»»» nonceVersion	integer	false	none	User's sub account nonce version
»»»» changePubKeyStatus	string	false	none	User's sub account change pubKey status
»»»» subAccountId	string	false	none	User's sub account ID
»»»» nonce	integer	false	none	User's sub account nonce
»»» defaultSubAccountId	string	false	none	User's zk default sub account ID
»»» zkAccountId	string	false	none	User's zk account ID
»»» userId	string	false	none	User's user ID
»»» ethAddress	string	false	none	User's ethereum address
»»» nonce	integer	false	none	User's account nonce
»»» updatedAt	integer	false	none	User's account update time
»»» status	string	false	none	User's account status
»» transfers	[string]	true	none	
»» positionClosedTransactions	[string]	true	none	
»» orders	[object]	true	none	
»»» cumSuccessLiquidateFee	string	true	none	Cumulative liquidate fee
»»» symbol	string	true	none	Symbol
»»» openSlParams	object	true	none	Open Sl order params
»»»» triggerSize	string	true	none	Order trigger size
»»»» triggerPrice	string	true	none	Order trigger price
»»»» triggerPriceType	string	true	none	Order trigger type
»»» cumSuccessFillFee	string	true	none	Cumulative fill fee
»»» type	string	true	none	order type
»»» isPositionTpsl	boolean	true	none	If the order is position Tpsl
»»» isDeleverage	boolean	true	none	If the order is deleverage
»»» createdAt	integer	true	none	The order created time
»»» isSetOpenTp	boolean	true	none	If the order is set open Tp
»»» price	string	true	none	Order Price
»»» cumSuccessFillValue	string	true	none	Cumulative fill value
»»» id	string	true	none	Order ID
»»» cancelReason	string	true	none	Order cancel reason
»»» timeInForce	string	true	none	Order timeInForce
»»» updatedAt	integer	true	none	Order updated time
»»» limitFee	string	true	none	Order limit fee
»»» side	string	true	none	Order side
»»» clientId	string	true	none	Order client ID
»»» triggerPrice	string	true	none	Condition order trigger price
»»» triggerPriceType	string	true	none	Condition order trigger type
»»» expiresAt	integer	true	none	Order expired time
»»» openTpParams	object	true	none	Open Tp order params
»»»» triggerSize	string	true	none	Order trigger size
»»»» triggerPrice	string	true	none	Order trigger price
»»»» triggerPriceType	string	true	none	Order trigger type
»»» cumSuccessFillSize	string	true	none	umulative fill size
»»» size	string	true	none	Order size
»»» reduceOnly	boolean	true	none	If the order is reduce only
»»» isSetOpenSl	boolean	true	none	If the order is set open Sl
»»» isLiquidate	boolean	true	none	If the order is liquidate
»»» remainingSize	string	true	none	The order remaining size
»»» status	string	true	none	The order's status
»» positions	[object]	true	none	Open positions
»»» symbol	string	true	none	Symbol
»»» exitPrice	string	true	none	
»»» side	string	true	none	Side
»»» openValue	string	true	none	Position open value
»»» sumOpen	string	true	none	Position cumulative opened size
»»» fundingFee	string	true	none	Position funding fee
»»» sumClose	string	true	none	Position cumulative closed size
»»» entryPrice	string	true	none	Position cumulative entry price
»»» accountId	string	true	none	User's account ID
»»» customImr	string	true	none	Symbol's custom initial margin rate
»»» size	string	true	none	Position size
»»» realizedPnl	string	true	none	Postion realized Pnl
»»» updatedAt	integer	true	none	Postion update time
»» experienceMoney	[object]	true	none	Experience money
»»» totalAmount	string	false	none	Total experience money value
»»» totalNumber	string	false	none	Total experience money number
»»» recycledAmount	string	false	none	Recycled experience money value
»»» availableAmount	string	false	none	Available experience money amount
»»» token	string	false	none	Experience money token
»» contractWallets	[object]	true	none	
»»» pendingDepositAmount	string	false	none	Pending deposit amount
»»» balance	string	false	none	Wallet balance
»»» pendingWithdrawAmount	string	false	none	Pending withdrawal amount
»»» pendingTransferInAmount	string	false	none	Pending inbound transfer amount
»»» pendingTransferOutAmount	string	false	none	Pending outbound transfer amount
»»» token	string	false	none	Asset token name
»» deleverages	[object]	true	none	
»»» symbol	string	false	none	Symbol name
»»» lightNumber	string	false	none	ADL ranking
»»» side	string	false	none	Open side
»» fills	[string]	true	none	Fills
» topic	string	true	none	Subscribe topic
» type	string	true	none	
» timestamp	integer	true	none	Message time
Order Submission Push
{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "orders":[
        {
          "symbol":"ETH-USDT",
          "cumSuccessFillFee":"0.625000",
          "trailingPercent":"0",
          "type":"LIMIT",
          "unfillableAt":1654779600000,
          "isDeleverage":false,
          "createdAt":1652185521339,
          "price":"2500.0",
          "cumSuccessFillValue":"0",
          "id":"2048046080",
          "cancelReason":"",
          "timeInForce":1,
          "updatedAt":1652185521392,
          "limitFee":"0.625000",
          "side":"BUY",
          "clientOrderId":"522843990",
          "triggerPrice":"",
          "expiresAt":1654779600000,
          "cumSuccessFillSize":"0",
          "accountId":"1024000",
          "size":"0.500",
          "reduceOnly":false,
          "isLiquidate":false,
          "remainingSize":"0.000",
          "status":"PENDING"
        }
      ]
   }
}
Post-Submission of Maker Order Push
{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "fills":[

      ],
      "positions":[

      ],
      "orders":[
        {
          "symbol":"ETH-USDT",
          "cumSuccessFillFee":"0.625000",
          "trailingPercent":"0",
          "type":"LIMIT",
          "unfillableAt":1654779600000,
          "isDeleverage":false,
          "createdAt":1652185521339,
          "price":"2500.0",
          "cumSuccessFillValue":"0",
          "id":"2048046080",
          "cancelReason":"",
          "timeInForce":1,
          "updatedAt":1652185521392,
          "limitFee":"0.625000",
          "side":"BUY",
          "clientOrderId":"522843990",
          "triggerPrice":"",
          "expiresAt":1654779600000,
          "cumSuccessFillSize":"0",
          "accountId":"1024000",
          "size":"0.500",
          "reduceOnly":false,
          "isLiquidate":false,
          "remainingSize":"0.000",
          "status":"OPEN"
        }
      ],
      "accounts":[

      ],
      "transfers":[

      ]
   }
}

Post-Cancel Order Push
{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "fills":[

      ],
      "positions":[

      ],
      "orders":[
         {
           "symbol":"ETH-USDT",
           "cumSuccessFillFee":"0.625000",
           "trailingPercent":"0",
           "type":"LIMIT",
           "unfillableAt":1654779600000,
           "isDeleverage":false,
           "createdAt":1652185521339,
           "price":"2500.0",
           "cumSuccessFillValue":"0",
           "id":"2048046080",
           "cancelReason":"",
           "timeInForce":1,
           "updatedAt":1652185521392,
           "limitFee":"0.625000",
           "side":"BUY",
           "clientOrderId":"522843990",
           "triggerPrice":"",
           "expiresAt":1654779600000,
           "cumSuccessFillSize":"0",
           "accountId":"1024000",
           "size":"0.500",
           "reduceOnly":false,
           "isLiquidate":false,
           "remainingSize":"0.000",
           "status":"CANCELED"
         }
      ],
      "accounts":[

      ],
      "transfers":[

      ]
   }
}

Successful Order Execution Push

{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "fills":[
         {
           "symbol":"ETH-USDT",
           "side":"BUY",
           "orderId":"2048046080",
           "fee":"0.625000",
           "liquidity":"TAKER",
           "accountId":"1024000",
           "createdAt":1652185521361,
           "isOpen":true,
           "size":"0.500",
           "price":"2500.0",
           "quoteAmount":"1250.0000",
           "id":"2048000182272",
           "updatedAt":1652185678345
         }
      ],
      "positions":[
         {
           "symbol":"ETH-USDT",
           "exitPrice":"0",
           "side":"LONG",
           "maxSize":"2820.000",
           "sumOpen":"1.820",
           "sumClose":"0.000",
           "netFunding":"0.000000",
           "entryPrice":"2500.000000000000000000",
           "accountId":"1024000",
           "createdAt":1652179377769,
           "size":"1.820",
           "realizedPnl":"0",
           "closedAt":1652185521392,
           "updatedAt":1652185521392
         }
      ],
      "orders":[
         {
           "symbol":"ETH-USDT",
           "cumSuccessFillFee":"0.625000",
           "trailingPercent":"0",
           "type":"LIMIT",
           "unfillableAt":1654779600000,
           "isDeleverage":false,
           "createdAt":1652185521339,
           "price":"2500.0",
           "cumSuccessFillValue":"1250.0000",
           "id":"2048046080",
           "cancelReason":"",
           "timeInForce":1,
           "updatedAt":1652185521392,
           "limitFee":"0.625000",
           "side":"BUY",
           "clientOrderId":"522843990",
           "triggerPrice":"",
           "expiresAt":1654779600000,
           "cumSuccessFillSize":"0.500",
           "accountId":"1024000",
           "size":"0.500",
           "reduceOnly":false,
           "isLiquidate":false,
           "remainingSize":"0.000",
           "status":"FILLED"
         }
      ],
      "accounts":[
      ],
      "transfers":[
      ]
   }
}

Deposit Success Push
{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "fills":[
      ],
      "positions":[
      ],
      "orders":[         
      ],
     "wallets":[
       {
         "balance":"438.486000",
         "asset":"USDT"
       }
     ]
   }
}

Withdrawal Request Submission Push

{
   "type":"delta",
   "timestamp":1647502440973,
   "topic":"ws_zk_accounts_v3",
   "contents":{
      "fills":[

      ],
      "positions":[

      ],
      "orders":[

      ],
      "accounts":[
      ],
      "transfers":[
         {
            "status":"QUEUED",
            "transactionId":"39190120",
            "id":"89abf9d72432",
            "type":"WITHDRAWAL",
            "creditAsset":"USDT",
            "creditAmount":"100",
            "transactionHash":null,
            "confirmedAt":null,
            "createdAt":1647502440973,
            "expiresAt":1647502440973
         }
      ]
   }
}

Notify Message Push
{
  "contents": {
    "unreadNum": 24, 
    "notifyMsgList": [
      {
        "id": "1145486332832022528",  
        "category": 1, 
        "lang": "en",
        "title": "Deposit success ", 
        "content": "Your deposit of 100.000000 USDT has been confirmed.", 
        "androidLink": "", 
        "iosLink": "", 
        "webLink": "",  
        "read": false, 
        "createdTime": 1682357834534  
      }
      ...
    ]
  },
  "topic": "ws_notify_v1",
  "type": "snapshot"
}
Response Parameters
Parameter	Type	Comment
» notifyMsgList	object	Notification message list
»» id	string	Notification ID
»» category	int	Notification category
»» lang	string	Language
»» title	string	Title
»» content	string	Content
»» androidLink	string	Android link
»» iosLink	string	Ios link
»» webLink	string	Web link
»» read	bool	If notification has been read
»» createdTime	int	Created time
New Notification Message Push
Response

{
  "contents": {
    "notify_list": [
      {
        "id": "1145486332832022528",  
        "category": "NOTIFY_CATEGORY_ACCOUNT", 
        "lang": "en", 
        "title": "Deposit success ", 
        "content": "Your deposit of 100.000000 USDT has been confirmed.", 
        "androidLink": "", 
        "iosLink": "", 
        "webLink": "",  
        "read": false, 
        "createdTime": 1682357834534 
      }
    ]
  },
  "topic": "ws_notify_v1",
  "type": "delta"
}
Gnosis Multi-Sig Wallet Endpoint for Market Makers
v3.0.0

Creating a Gnosis Safe Multi-Sig Wallet
Click on https://gnosis-safe.io/app/ to access the application on desktop. Refer to the document gnosis_safe and create your multi-sig wallet according to the following steps:

Select the Ethereum network
You will need to connect an existing wallet to Gnosis Safe to create an account and ensure that you have some ETH in the wallet to pay for transaction fees that may be incurred during the setup
Enter the wallet name and include the names, addresses and number of stakeholders involved in the authentication of withdrawals from this multi-sig wallet. Once you're certain that all information entered is accurate, you can proceed with the creation of the Gnosis Safe wallet
Transfer funds into the Gnosis Safe wallet
Use ETH Multi Address to register Apex Omni account
1) Use Apex Omni's python SDK: Authorize your Ethereum private keys to create Zklink seeds, l2key and pubkeyHash — refer to python codes demo_register_mul_address_v3_step1.py

from apexomni.http_private_v3 import HttpPrivate_v3
from apexomni.constants import APEX_OMNI_HTTP_MAIN, NETWORKID_OMNI_MAIN_ARB

print("Hello, Apex Omni")
priKey = "your eth private key"

client = HttpPrivate_v3(APEX_OMNI_HTTP_MAIN, network_id=NETWORKID_OMNI_MAIN_ARB, eth_private_key=priKey)
configs = client.configs_v3()

zkKeys = client.derive_zk_key(client.default_address)

nonceRes = client.generate_nonce_v3(refresh="false", l2Key=zkKeys['l2Key'],ethAddress=client.default_address, chainId=NETWORKID_OMNI_MAIN_ARB)

regRes = client.register_user_v3(nonce=nonceRes['data']['nonce'],l2Key=zkKeys['l2Key'], seeds=zkKeys['seeds'],ethereum_address=client.default_address,
                                 eth_mul_address="your mul eth address", isLpAccount=True)
2) eth_mul_address use ZkLink Smart Contract ABI Code zklink.json to executed setAuthPubkeyHash on chain - ETH mainnet contract address is 0x35D173cdfE4d484BC5985fDa55FABad5892c7B82 （arb chainId is 4 ） - ARB mainnet contract address is 0x3169844a120c0f517b4eb4a750c08d8518c8466a （arb chainId is 9 ） - choose setAuthPubkeyHash method，pubkeyHash set pubkeyHash by step 1 ，nonce the first register set 0

3) Use Apex Omni's python SDK: demo_register_mul_address_v3_step2.py

from apexomni.http_private_v3 import HttpPrivate_v3
from apexomni.http_private import HttpPrivate
from apexomni.constants import APEX_HTTP_TEST, NETWORKID_TEST, APEX_HTTP_MAIN, NETWORKID_MAIN, APEX_OMNI_HTTP_TEST, \
APEX_OMNI_HTTP_MAIN, NETWORKID_OMNI_MAIN_ARB

print("Hello, Apex Omni")

key = 'your apiKey-key from register'
secret = 'your apiKey-secret from register'
passphrase = 'your apiKey-passphrase from register'

seeds = 'your zk seeds from register'
l2Key = 'your l2Key seeds from register'
pubKeyHash = 'your l2Key seeds from pubKeyHash'


client = HttpPrivate_v3(APEX_OMNI_HTTP_MAIN, network_id=NETWORKID_OMNI_MAIN_ARB, api_key_credentials={'key': key,'secret': secret, 'passphrase': passphrase})
configs = client.configs_v3()

accountRes = client.get_account_v3()
print(accountRes)

changeRes = client.change_pub_key_v3(chainId=NETWORKID_OMNI_MAIN_ARB, seeds= seeds, zkAccountId = accountRes.get('spotAccount').get('zkAccountId'), subAccountId = accountRes.get('spotAccount').get('defaultSubAccountId'),
newPkHash=pubKeyHash,  nonce=accountRes.get('spotAccount').get('nonce'), l2Key= l2Key, ethSignatureType='Onchain')
print(changeRes)

time.sleep(10)
accountRes = client.get_account_v3()
print(accountRes)
Authorize StarkWare Contract to Transfer token via Gnosis Safe
As deposits will be processed through zklink, you will need to authorize the zklink contract to transfer your token assets.

Proceed with a new transaction via Gnosis Safe
Enter transaction details:
Enter the erc20 token contract address:
Enter the erc20 token contract ABI and select the approve method
[{
"inputs": [{
"internalType": "address",
"name": "spender",
"type": "address" }, {
"internalType": "uint256", "name": "value",
"type": "uint256"
}],
"name": "approve", "outputs": [{
"internalType": "bool", "name": "",
"type": "bool"
}],
"stateMutability": "nonpayable", "type": "function"
}]
Spender address (Enter zklink's contract address)
value: For accuracy, we recommend that you enter the correct deposit amount (to 6 decimal places), e.g. 100 USDT should be entered as 100000000
Deposit via Gnosis Safe
Approve the token to deposit
Run Contract depositERC20 method to deposit erc20 tokens or depositETH method to deposit ETH, enter transaction details:
token: erc20 token address
amount: Deposit amount, converted according to erc20 token decimals, e.g. 100 USDT should be entered as 100000000
zkLinkAddress: gnosis wallet address, the leading zero needs to be padded with 24 zeros, for example
0x71d375b54f6d2c678759a3e84b6ee5ba4eba3847 to 0x00000000000000000000000071d375b54f6d2c678759a3e84b6ee5ba4eba3847
subAccountId: set to 0,
mapping: set to false
After reviewing the parameters and ensuring that they are correct, confirm the deposit transaction
For other stakeholders involved in the Gnosis Safe wallet, use your personal wallet to authorize the transaction and complete the deposit process
Errors
The API uses the following error codes:

Error Code	Meaning
400	Bad Request : Your request is invalid.
403	IP banned : Your IP is banned.
404	Not Found : The request path could not be found.
500	Internal Server Error: We're experiencing issues with our server. Please try again later.
503	Service Unavailable: We're temporarily offline for maintenance. Please try again later.
10001	Failed : error request.
10002	Requires Login : Your API key is wrong.
10003	Too Many Requests : Slow down!
10004	Request Timeout
Error Key	Meaning
UNKNOWN	("Service Error ."),
INVALID_L2_SIGNATURE	("Invalid L2 signature."),
INVALID_ETH_ADDRESS	("Invalid ethAddress."),
INVALID_LP_ACCOUNT	("Invalid lp account id. {accountId}"),
INVALID_FEE	("Invalid fee request {fee}"),
INVALID_L2_TX	("Invalid l2 txhash"),
INVALID_USER_ID	("Invalid userId. {userId}"),
INVALID_ACCOUNT_ID	("Invalid accountId. {accountId}"),
INVALID_CURRENCY_ID	("invalid currencyId. {currencyId} "),
INVALID_CLIENT_WITHDRAW_ID	("Invalid clientWithdraw Id. {clientWithdrawId}"),
INVALID_CLIENT_TRANSFER_ID	("Invalid clientTransfer Id. {clientTransferId}"),
INVALID_PAGE_SIZE	("Invalid page size. {size}"),
EMPTY_CHAIN_ID	("Empty chainId."),
EMPTY_CLIENT_FAST_WITHDRAW_ID	("Empty clientFastWithdraw Id."),
EMPTY_PARAM	("{name}Empty request param."),
EMPTY_CLIENT_WITHDRAW_ID	("Empty clientWithdraw Id."),
EMPTY_CLIENT_TRANSFER_ID	("Empty clientTransfer Id."),
AMOUNT_MUST_GREETER_ZERO	("Amount must greater than 0. {amount}"),
ACCOUNT_NOT_FOUND	("The account does not exist. {accountId}"),
ACCOUNT_NOT_FOUND_L2KEY	("The account does not exist. {l2Key}"),
ACCOUNT_NOT_FOUND_LP	("The account does not exist. {lpAccountId}"),
ACCOUNT_CONFLICT_L2KEY	("The account already exists. Please select another account. {l2Key}"),
ORDER_NOT_FOUND	("This order does not exist. {orderId}"),
ORDER_NOT_CANCEL_MATCHED	("Order processing, please do not cancel. {orderId}"),
ORDER_NOT_CANCEL_FILLED	("Order successful, please do not cancel. {orderId}"),
ORDER_NOT_CANCEL_INVALID_STATUS	("Invalid order, please do not cancel. {orderId}"),
ORDER_INVALID_ORDER_TYPE	("This order type is invalid. {orderType}"),
ORDER_INVALID_TIME_IN_FORCE	("Invalid time-in-force. {timeInForce}"),
ORDER_INVALID_STATUS	("This order status is invalid. {orderStatus}"),
ORDER_INVALID_ORDER_SIDE	("This order direction is invalid. {orderSide}"),
ORDER_LIMIT_FEE_NOT_ENOUGH	("Insufficient gas fees on this order. {limitFee}"),
ORDER_FILL_TRANSACTION_ID_NOT_FOUND	("This order does not exist.{transactionId}"),
ORDER_FILL_TRANSACTION_CENSOR_ROUND_CONFLICT	("Order submission error. {censorRound}"),
ORDER_FILL_TRANSACTION_INVALID_STATUS	("Order submission status is invalid. {transactionStatus}"),
ORDER_EMPTY_CLIENT_ORDER_ID	("Empty clientOrderId."),
ORDER_INVALID_CLIENT_ORDER_ID	("Invalid clientOrderId. {clientOrderId}"),
ORDER_LIQUIDATE_ORDER_FAILED	("Liquidation Unsuccessful."),
ORDER_DELEVERAGE_WITH_SAME_ACCOUNT	("The deleveraging account and the liquidation account are the same, transaction has failed."),
ORDER_CLIENT_ORDER_DATA_CONFLICT	("Please resubmit your order. {clientOrderId}"),
ORDER_PRICE_MUST_GREETER_ZERO	("Price must greater than 0. {price}"),
ORDER_SIZE_MUST_GREETER_ZERO	("Size must greater than 0. {size}"),
ORDER_VALUE_MUST_GREETER_ZERO	("Value must greater than 0. {value}"),
ORDER_LIMIT_FEE_MUST_GREETER_ZERO	("LimitFee must greater than or equal 0. {limitFee}"),
ORDER_TRIGGER_PRICE_MUST_GREETER_ZERO	("TriggerPrice must greater than 0. {triggerPrice}"),
ORDER_SYMBOL_DISABLE_TRADE	("Symbol {symbol} disable trade"),
ORDER_SIZE_SMALLER_THAN_SYMBOL_MIN_ORDER_SIZE	("Order size {size} smaller than symbol {symbol} min order size {minOrderSize}"),
ORDER_SIZE_GREATER_THAN_SYMBOL_MAX_ORDER_SIZE	("Order size {size} greater than symbol {symbol} max order size {maxOrderSize}"),
ORDER_LIQUIDATING_ACCOUNT_CANNOT_CREATE_ORDER	("Account is liquidating, cannot create order"),
ORDER_OPEN_ORDER_COUNT_LIMIT_EXCEED	("You have {openOrderCount} open orders, cannot create new order"),
ORDER_WITH_THIS_PRICE_CANNOT_REDUCE_POSITION_ONLY	("Order with this price {price} cannot reduce position only"),
ORDER_SYMBOL_DISABLE_OPEN_POSITION	("Symbol '{symbol}' disable open position"),
ORDER_IS_REDUCE_ONLY_CANNOT_OPEN_POSITION	("Order is reduce-only, cannot open position"),
ORDER_IS_LIQUIDATE_ONLY_CANNOT_OPEN_POSITION	("Order liquidated, cannot open position"),
ORDER_IS_DELEVERAGE_ONLY_CANNOT_OPEN_POSITION	("Order auto deleveraged, cannot open position"),
ORDER_POSSIBLE_GREATER_THAN_SYMBOL_MAX_POSITION	("If order is filled, it can be greater than symbol '{symbol}' max. position size {maxPositionSize}"),
ORDER_IS_LIQUIDATE_NOT_MATCH_PRE_CONDITION	("Liquidation order not match pre-condition: beforeTV({beforeTV}) < beforeTR({beforeTR})"),
ORDER_IS_LIQUIDATE_AND_DELEVERAGE_NOT_MATCH_PRE_CONDITION	("Liquidation and ADL order not match pre-condition:beforeTV({beforeTV}) < 0"),
ORDER_POSSIBLE_LEAD_TO_ACCOUNT_LIQUIDATED	("If order is filled, your account may be liquidated."),
ORDER_POSSIBLE_LEAD_TO_ACCOUNT_LIQUIDATED_TV_TR_RATE_NOT_IMPROVED	("If order is filled and TV/TR does not improve, your account may be liquidated."),
ORDER_THERE_IS_NOT_ENOUGH_MARGIN_TO_OPEN_POSITION	("If order is filled, there is insufficient margin to open position"),
CROSS_DEPOSIT_DATA_ERROR	("Deposit error"),
CROSS_DEPOSIT_CURRENCY_ID_AMOUNT_CHANGED	("Deposit error. {currencyId}, {amount}"),
CROSS_WITHDRAW_WALLET_BALANCE_NOT_ENOUGH	("Insufficient wallet balance."),
CROSS_WITHDRAW_DATA_ERROR	("Cross-chain withdrawal error"),
CROSS_WITHDRAW_ID_NOT_FOUND	("Cross-chain withdrawal error. {withdrawId}"),
CROSS_WITHDRAW_INVALID_STATUS	("Cross-chain withdrawal error. {status}"),
CROSS_WITHDRAW_GREETER_MAX_ABLE_AMOUNT	("Your withdrawal amount has exceeded the max. withdrawal limit, please try again."),
CROSS_WITHDRAW_RISK_CHECK_FAILED	("Cross-chain withdrawal error"),
CROSS_WITHDRAW_INVALID_ARGUMENT	("Cross-chain withdrawal error"),
FAST_WITHDRAW_DATA_ERROR	("Fast withdrawal error."),
FAST_WITHDRAW_GREETER_MAX_ABLE_AMOUNT	("Your withdrawal amount has exceeded the max. withdrawal limit, please try again."),
FAST_WITHDRAW_RISK_CHECK_FAILED	("Fast withdrawal error."),
FAST_WITHDRAW_INVALID_ARGUMENT	("Fast withdrawal error."),
FAST_WITHDRAW_ID_NOT_FOUND	("Fast withdrawal error. {withdrawId}"),
FAST_WITHDRAW_INVALID_STATUS	("Fast withdrawal error. {status}"),
FAST_WITHDRAW_WALLET_BALANCE_NOT_ENOUGH	("Fast withdrawal unsuccessful, insufficient wallet balance."),
DEPOSIT_ASSET_ID_INVALID	("Deposit error. {assetId}"),
DEPOSIT_AMOUNT_INVALID	("Invalid deposit amount. {amount}"),
DEPOSIT_ASSET_ID_AMOUNT_CHANGED	("Data error! Incorrect deposit amount.. {assetId},{amount}"),
DEPOSIT_STATUS_INVALID	("Data error! Incorrect deposit status. {status}"),
DEPOSIT_CENSOR_ROUND_CONFLICT	(" Deposit censor round conflict. {censorRound}"),
DEPOSIT_ID_NOT_FOUND	("Data error! Incorrect deposit ID. {depositId}"),
WITHDRAW_INVALID_ARGUMENT	("Client withdrawal data conflict."),
WITHDRAW_WALLET_BALANCE_NOT_ENOUGH	("Withdrawal unsuccessful, insufficient wallet balance."),
WITHDRAW_CANNOT_FIND_WITHDRAW	("Withdrawal error. ${withdrawId}"),
WITHDRAW_CENSOR_ROUND_CONFLICT	("Withdraw censor round conflict. ${censorRound}"),
WITHDRAW_INVALID_STATUS	("Withdrawal status invalid. ${status}"),
TRANSFER_WITH_SAME_ACCOUNT	("invalid parameters, transfer with same account. ${accountId}"),
TRANSFER_CONDITION_FACT_REG_ADDRESS_EMPTY	("conditionFactRegistryAddress is empty"),
TRANSFER_CONDITION_FACT_EMPTY	("conditionFact is empty"),
NOT_CONDITION_TRANSFER_IN	("Not condition transferIn. ${transferInId}"),
NOT_CONDITION_TRANSFER_OUT	("Not condition transferOut. ${transferOutId}"),
TRANSFER_IN_STATUS_INVALID	("transferIn status invalid. ${status}"),
TRANSFER_OUT_STATUS_INVALID	("transferOut status invalid. {status}"),
TRANSFER_OUT_CENSOR_ROUND_CONFLICT	("transferOut censor round conflict. ${censorRound}"),
TRANSFER_IN_CENSOR_ROUND_CONFLICT	("transferIn censor round conflict. {censorRound}"),
CLIENT_TRANSFER_OUT_DATA_CONFLICT	("Client transfer out data conflict. ${clientTransferId}"),
TRANSFER_WALLET_BALANCE_NOT_ENOUGH