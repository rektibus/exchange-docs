v1.0.0
OAS 3.1.0
Bit2Me API Gateway
Introduction
👏 Welcome to Bit2Me as API.

We help individuals, exchanges, mining pools, tokens issuers, investment funds, governments and institutions to access, trade and manage cryptocurrencies and digital assets optimally.

Being the access door to markets without friction, leaving obsolete the traditional financial system, the company is made up of more than 300 people: idealists, technological entrepreneurs, researchers, quantitative, financial traders, lawyers and engineers from large companies.

We operate tirelessly around all time and world phases, with central offices in Spain, Europe.

The documentation that follows gives you access to our Crypto market data, Trading, and Custody products.

Data hierarchy
**Parent account / parent wallet**: This account / wallet is manually created by Bit2Me and provided to you via API Keys. This is your company’s master account and wallet. Parent accounts must be KYB’ed before operating.
Sub Account / wallet: A parent account can create one (1) sub account / wallet on behalf of each end user. You can generate as many end users as you want, but each can only operate on a single sub account or wallet. Sub Accounts must be KYC'ed before operating.

Pocket: A wallet can own many pockets. Each pocket can hold a specific type of currency. For example: “BTC pocket”, “ETH pocket”, “EUR pocket”… pockets are optional (you can operate at a wallet level).

Fig. - Data hierarchy
Quickstart
Official Repositories
Are you a coder? Check out these GitHub repositories to kickstart your journey with us!

Bit2Me Broker
Bit2Me Pro
Postman
You can test the Bit2Me API from Postman by importing our OpenAPI specification. You have two options: Option 1 — Import by link

In Postman, go to Import → Link. 2. Paste this URL (replace with your docs base URL if different): https://docs.bit2me.com/openapi.json Option 2 — Import by file
Download the spec using the button below. 2. In Postman, go to Import → File and select the downloaded file. Download OpenAPI (for Postman)
AI Agents and LLMs
Your LLM or AI agent can use our OpenAPI spec as the source of truth for the Bit2Me API: endpoints, authentication, parameters, schemas, and responses. Bit2Me MCP (Model Context Protocol) — Bit2Me offers an MCP server so AI assistants (Claude, Cursor, IDEs with MCP support) can call the Bit2Me API in a standard way. Integration guide: https://mcp.bit2me.com — step-by-step instructions to add the Bit2Me MCP to your assistant. Spec URLs (copy if needed) — Main spec: this documentation site's base URL + /openapi.json Per-product specs (same origin):

/openapi/crypto.json - /openapi/embed.json - /openapi/money-flow.json - /openapi/trading-spot-rest.json - /openapi/trading-spot-websockets.json Snippets for rules, skills and commands:
Rule (copy & paste): The Bit2Me OpenAPI spec is at [this site]/openapi.json. Use it as the source of truth for endpoints, auth, parameters, and responses. - Skill (copy & paste): When working with Bit2Me API, consult the OpenAPI spec at [this site]/openapi.json and validate paths, methods, parameters, auth, and schemas against it. - Command (copy & paste): Read the OpenAPI spec from [this site]/openapi.json and use it as the source of truth. Propose only HTTP calls and payloads that are valid according to that spec.
Logical steps to operate with API
[Auth] Obtain your API Keys for production environment from Bit2Me team.

[Subaccount] Using your API Key, generate sub accounts for each individual user.

[KYC] Perform the KYC to the individual user. If you are a regulated entity and already perform an equivalent KYC on your side, our sales team will explain to you how to reuse it.

[Funding] your parent account with fiat money.

Important notes

A minimum fiat balance is required to operate, as part of the initial set up there is a one time fiat transfer that must be sent to the fiat account that Bit2Me will tell you during the onboarding process
If you are a bank, the parent fiat account will be held in your own institution
During the day to day operations, fiat money must be funded to the main account. You should keep records of fiat money balances of each subaccount
4.1 [Funding] your account with EUR.

4.2 [Funding] your account with BRL.

4.3 [Funding] your account with ARS. (Soon)

*If you're looking for USD, please get in touch with our sales team. Currently this is only available in Bit2Me Pro.

[Funding] your account with crypto.

Obtain [Market] information for price and rates.

Get a list of assets
Get ticker information for currency pair
[Wallet] Create proforma transaction with the buy, sell or exchange operation you want to execute.

After that:

7.1 [Wallet] Execute the proforma transaction you created earlier.

[Trading] Use Bit2Me Pro to do your high-frequency trading.

Deposit funds into your Bit2Me Pro account
Place an order
[Earn] Deposit or withdraw crypto from earn protocols.

List supported assets
Get assets annual percentage yields.
List subaccount earn wallets.
Deposit/withdraw cryptos in earn.
[Transfers] Move money between users (peer to peer):

First create a transfer from the origin user.
Then claim the transfer for the destination user.
[Withdraw] your fiat.

[Withdraw] your crypto.


IMPORTANT: Logical steps are not examples, if you're looking for them, check the next section.

Use cases
The following are some common use cases that illustrate how our API can be leveraged:

Perform KYC process

In order to perfom the KYC process first step is complete subaccount data following the examples in linked section. Following information must be provided

{
  "person": {
    "name": <String>,
    "surname": <String>,
    "birthDate": <DateISO8601>,
    "nationalityCountryCode": <CountryISO3166-1Alpha2>,
  },
  "profile": {
    "langCode": <LangISO639-1>,
    "currencyCode": <CurrencyISO4217>,
    "timeZone": <String>
  }
}
Is mandatory to add an address to the subaccount following the examples in linked section.

Init verification identity process. This process has a predefined number of retries, once the limit has been overcomed, contact with our support department in order to reset it. Remaining retries can be checked following the examples in linked section.

Enable main account google authenticator 2fa

Retrieve 2fa user verification following the examples in linked section. Sfatype is obtained in the response. A valid 2fa code is sent using indicated sfaType.

Start 2fa enablement process following the examples in linked section.
This endpoint returns a secret that has to be used to configure google authenticator and generate valid 2fa codes.
Following headers must be sent:

x-totp: [[2fa-code obtained in previous step]]
x-totp-type: [[sfaType obtained in previous response]]
End 2fa enablement process following the examples in linked section.

Enable subaccount google authenticator 2fa

Start subaccount 2fa enablement process following the examples in linked section.
This endpoint returns a secret that has to be used to configure google authenticator and generate valid 2fa codes.

End subaccount 2fa enablement process following the examples in linked section.

Deposit crypto in subaccount
Subaccount users can receive crypto from a network address. Following steps should be done to achieve this action:

Create subaccount crypto pocket.
If subaccount doesn't have a crypto pocket first step is to create one.

Get unique address for crypto pocket.
Once subaccount crypto pocket is created, unique address can be generated.

Receive cryptos in crypto pocket using generated address.
In order to transfer assets from another platform, initiate a withdrawal from that account and paste this address into the destination field.

Once the operation has been processed and the funds received in the pocket, a notification of type "wallet.trx.confirmed" will be sent through websockets.

Fiat deposit

For EUR: Check your bank accounts and make a fiat transfer.

For BRL: Create a deposit proforma.

{
  "amount": "10",
  "description": "BRL deposit",
  "currency": "BRL",
  "feeType": "REA",
  "orderType": "deposit",
  "destination?": {
    "type": "pocket",
    "value": "<UUID of an BRL pocket>"
  },
  "method": {
    "type": "hub-latam",
  }
}
5.1. Receiving fiat deposits notifications

When a fiat deposit is done (via bank transfer) a notification is generated via websockets. Multiple notifications types can be generated related to fiat deposits:

wallet-transaction-v1

teller-order-v1

teller.deposit.transfer.success

teller.deposit.transfer.error

More information of this notifications can be found in websockets previously provided link.

Calculate pocket balances

A pocket is needed. Pocket balance can be checked for fiat and crypto pockets.
Same operation can be used for subaccounts.

Get pocket balance following examples in linked section

Crypto buy operation
To perform a buy operation follow next steps:

Generate a proforma with following body

{
  "operation": "buy",
  "pair": "BTC/EUR",
  "amount": "100",
  "currency": "EUR"
}
With previous example, a proforma for an operation of buying 100 EUR of BTC is created. In the response, the id of the generated proforma is obtained.

Execute proforma confirmation using previously obtained id

Crypto sell operation
To perform a sell operation follow next steps:

Generate a proforma with following body

{
  "operation": "sell",
  "pair": "BTC/EUR",
  "amount": "0.001",
  "currency": "BTC"
}
With previous example, a proforma for an operation of selling 0.001 BTC is created. In the response, the id of the generated proforma is obtained.

Execute proforma confirmation using previously obtained id

Crypto swap operation
To perform a swap operation follow next steps:

Generate a proforma with following body

{
  "pocket": "<UUID of a user crypto pocket>",
  "amount": "0.001",
  "currency": "BTC",
  "destination": {
      "pocket": "<UUID of a user crypto pocket>"
  },
  "type": "SEA",
  "userCurrency": "EUR"
}
With previous example, a proforma for an operation of swaping 0.001 BTC is created. In the response, the id of the generated proforma is obtained.

Execute proforma confirmation using previously obtained id

For more examples, go to wallet create transaction cURL section in requests samples side.

Deposit crypto in earn service

Check available assets in earn service

Create earn deposit
The pocketId must be a valid pocket identifier for the same currency you are depositing.
This operation can also be done for subaccounts as stated in linked section examples.

Withdraw crypto from earn service

List user earn wallets for detailed information This endpoint can also be used for subaccounts as stated in linked sections example

Create earn withdraw
The pocketId must be a valid pocket identifier for the same currency you are withdrawing.
This operation can also be done for subaccounts as stated in linked section examples.

Fiat withdraw (EUR)

An EUR pocket is needed

Create withdraw proforma following examples in linked section.

{
  "pocket": "<UUID of an EUR pocket>",
  "amount": "10",
  "currency": "EUR",
  "type": "SEA",
  "concept": "",
  "note": "",
  "destination": {
    "bankAccount": {
        "bankAccount": "<IBAN bank account>",
        "country": "ES",
        "receiverName": "Test"
    }
  },
  "userCurrency": "EUR"
}
These call will return an id field that has to be used in the next endpoint call.

To confirm previous generated transaction, 2fa is requested

Execute withdraw order following examples in linked section.
The response contains an id that identifies the executed withdraw order

Fiat withdraw (BRL)
Fiat withdraws for Brazil are made using Pix instant payment platform. Following steps should be done to achieve this action:

An EUR pocket is needed

Create pix withdraw proforma following examples in linked section.

{
  "pocket": "<UUID of an EUR pocket>",
  "amount": "10",
  "currency": "EUR",
  "type": "SEA",
  "concept": "",
  "note": "",
  "destination": {
    "bankAccount": {
        "bankAccount": "<IBAN bank account>",
        "country": "BR",
        "receiverName": "Test",
        "bankBranch": "02",
        "bankCode": "01",
        "bankName": "Bank test",
        "taxDocument": "<CPF-CNPS>"
    }
  },
  "userCurrency": "EUR"
}
These call will return an id field that has to be used in the next endpoint call.

To confirm previous generated transaction, 2fa is requested

Execute pix withdraw order following examples in linked section.
The response contains an id that identifies the executed withdraw order

Withdraw crypto from subaccount
Subaccount users can send crypto to a network address. Next steps should be followed to achieve this action:

A subaccount crypto pocket with funds is needed.

Create a transaction following the examples in linked section.
When generating transaction, following body example can be used:

{
  "pocket": "<UUID of a user subaccount crypto pocket>",
  "currency": "ETH",
  "amount": "0.005",
  "type": "SEA",
  "destination": {
      "address": "<Network address>",
      "network": "<Network name>"
  },
  // If needed
  // "queryParams" : "<Memo/Tag>"
  "userCurrency": "EUR"
}
To confirm previous generated transaction, first 2fa has to be requested

Confirm previous generated transaction using next endpoint

Rate Limit
To ensure optimal performance and reliability of our API, we have implemented rate limits on the number of requests that can be made within a given timeframe. Below is a table detailing the allowed requests per minute (RPM) for different tiers:

Tier	Max. RPM (request per minute)
Starter	600
Medium	800
Pro	1000
To request a new tier, contact our support center

All endpoints of this API are designed to enforce strict usage policies to ensure fair access and optimal performance for all users. As a result, any request that exceeds the allowed rate limits, may trigger a HTTP response with two types of error:

Code 429: The user has sent too many requests in a given timeframe.
Code 418: The user has been banned from accessing the API.
Important note: It is essential for users to adhere to the specified guidelines to avoid these error responses and maintain uninterrupted access to the API's functionalities, otherwise you'll be banned.

Status
🔔 Stay updated with the latest platform updates and outages! Click the button below to suscribe to our service to receive all the news and announcements directly to your inbox.

👉 Suscribe 👈

WebSockets
This service has a websocket interface to communicate to the client all the notifications that happen in the platform. After the websocket connection you must send the JWT token or the API Key in order to authenticate the connection. If the authentication fails the websocket is closed immediately with code 4000.

WebSockets connection are limited by IP and also uses the same Rate Limiter as the HTTP calls:

If the maximum number of concurrent connections (50) from the same IP is exceeded a handshake error is returned with code 429.
If the maximum number of messages sent (50 per second) from the same connection is exceeded, it will be closed with code 4001.
Please also note, that you can ONLY receive events with a logged in account.

Reconnect policy
We recommend implementing an on disconnect: reconnect policy for WebSocket connections to our platform. This strategy ensures that, in the event of a connection interruption, the client will automatically attempt to reconnect, which enhances resilience and user experience.

By maintaining an active connection and efficiently reestablishing it, interruptions in communication are minimized, and a continuous flow of data is guaranteed, which is essential for real-time applications. This practice not only optimizes performance but also contributes to greater stability in interactions with our platform.

Code Snippets Examples
Example (browser-index.html)

  <!DOCTYPE HTML>
    <html>
        <head>
            <script type = "text/javascript>

            const ws = new WebSocket (`wss://${host}:${port}/`);

            ws.addEventListener ('error', err => {
              console.error ('websocket error:', err);
            });

            ws.addEventListener ('open', () => {
              console.debug ('websocket connected');

              // send the jwt token to authenticate the connection
              ws.send (JSON.stringify ({ type: 'authenticate', payload: { token: jwt }}));

              // or alternatively authenticate with apikey
              ws.send (JSON.stringify ({ type: 'authenticate', payload: { apikey: [apikey] }}));
            });

            ws.addEventListener ('message', message => {
              const msg = JSON.parse (message.data);
              console.debug (`websocket message: type: ${msg.type}, id: ${msg.id}, time: ${msg.time}`);
            });

            ws.addEventListener ('close', evt => {
              if (evt.code === 4000) {
                console.log (`Error while authenticating: ${evt.code}/${evt.reason}`);
              }
              else if (evt.code === 4001) {
                console.log (`Error rate limit: ${evt.code}/${evt.reason}`);
              }
              // handle reconnect logic
            });

            </script>

        </head>
        <body>
        ......
        </body>
    </html>

Example to receive tx notifications from BTC testnet crypto explorer (server- node.js)

  const ws = new WebSocket (`wss://${host}:${port}/v1/explorer/BTCTEST`);

  ws.addEventListener ('error', err => {
    console.error ('websocket error:', err);
  });

  ws.addEventListener ('open', () => {
    console.debug ('websocket connected');

    // subscribe to 'inv' room
    ws.send (JSON.stringify ([ 'subscribe', 'inv' ]));
  });

  ws.addEventListener ('message', message => {
    const msg = JSON.parse (message);

    // we want just transactions
    if (msg[0] === 'tx') {
      console.debug ('websocket message:', msg[1]);
      // ...
    }
  });

  ws.addEventListener ('close', evt => {
    if (evt.code === 4001) {
      console.log (`Error rate limit: ${evt.code}/${evt.reason}`);
    }
    else if (evt.code === 4002) {
      console.log (`Wrong crypto explorer: ${evt.code}/${evt.reason}`);
    }
    // handle reconnect logic
  });
WebSockets received
All WebSockets recieved have the same structure:

{ channel: string, id: string, time: number, type: string, payload: object }

Depends on the type, the payload is different:

Type	Payload	Description
 
file.download.error	{ message }	Error downloading a file.
file.download	{ path }	Receiving a file.
accouting.entries.success	{ }	Accounting a document generation.
accounting.entries.error	{ error: { date, message } }	Error generating accounting document.
 
affiliate.activity	{ action, serial, earnings, points } [ action: 'newEarnings' ]
{ action, earnings } [ action: 'adminUpdate' ]
{ action } [ action: 'payoutRejected' ]	An affiliate has generated an activity.
affiliate.invoice	{ email, langCode, name, surname, action, pocketId, pocketName, earnings }	Affiliate benefits have been processed and invoice generated.
 
currency.rates	{ type, rates } [ type: 'fiat' || 'crypto' ]	Receipt of currency price changes in case they have changed.
 
instant.process.postponed.orders.finished	{ }	Notification when orders postponed due to exchange failure have been reprocessed correctly.
 
social.payment.expiration	{ type, email, langCode, name, surname, amount, currency }	Pending payment expired.
social.payment.success	{ pocketId, amount, currency }	You have received a payment.
social.payment.pending	{ name, surname, amount, currency, expiryDate }	Pending payment.
 
teller.new.card.success	{ cardId, alias }	Credit card added successfully.
teller.new.card.error	{ code, message }	Failed to add new credit card.
teller.purchase.card.success	{ pocketId, amount, currency, transactionId }	Purchase made correctly by credit card.
teller-order-v1	{ orderId, status, type, error }	Teller order performed
[DEPRECATED] use teller-order-v1
teller.purchase.card.error
{ code, message }	Failed to buy with a credit card.
[DEPRECATED] use wallet-transaction-v1
teller.deposit.card.success
{ pocketId, amount, currency, transactionId }	Credit card deposit made correctly.
[DEPRECATED] use teller-order-v1
teller.deposit.card.error
{ code, message }	Failed to deposit with credit card.
teller.deposit.transfer.success	{ pocketId, amount, currency, transactionId }	Deposit by bank transfer received.
teller.deposit.transfer.error	{ code, message }	Error when depositing bank transfer.
 
[DEPRECATED] use teller-order-v1
notice.unverified.card
{ email, langCode, last_4 }	User performs an operation with a card that is not verified.
 
[DEPRECATED] use teller-order-v1
launchpad.purchase.card.error
{ code, message }	User tries to make a purchase through Launchpad using credit card as payment method and some kind of error occurs.
 
identity.pending	{ langCode, email }	Pending Identity.
identity.validated	{ langCode, email }	Verified identity.
identity.rejected	{ langCode, email }	Identity rejected.
identity.nodata	{ langCode, email }	Identity without data.
identity.image.uploaded	{ image, dataUrl } [ image: 'document' || 'selfie' ]	An image of the verification process via smartphone has been uploaded successfully.
identity.image.error	{ image, dataUrl } [ image: 'document' || 'selfie' ]	Error uploading image verification process using smartphone.
email.confirm.done	{ email }	Email confirmed correctly.
 
identity.enhanced.measures.required	{ langCode, email }	User receives a message via websocket indicating that his identity is in Pending status.
 
wallet.promo.referral.error	{ pocketId, amount, currency }	An error has occurred when receiving the 5€ promo of a new referral when buying 100€.
wallet.promo.referral.success	{ pocketId, amount, currency }	For being affiliated and having made an operation equal to or greater than 100€ you have received {{amount}} FREE.
wallet-transaction-v1	{ userId, pocketId, amount, currency, transactionId, status, tellerId }	Wallet transaction performed
wallet.trx.received	{ pocketId, amount, currency, transactionId, langCode, name, surname?, pocketName, email }	Transaction received from the blockchain successfully.
wallet.trx.confirmed	{ pocketId, amount, currency, transactionId }	Transaction confirmed.
wallet.trx.reimbursement	{ pocketId, amount, currency, bankAccount, transactionId, tellerOrderId }	Transaction refunded.
wallet.trx.cancellation	{ pocketId, amount, currency, bankAccount, transactionId, tellerOrderId }	Transaction canceled.
 
launchpad.purchase.card.success	{ transactionId }	User makes a successful purchase using credit card as a payment method.
launchpad.purchase.pocket.success	{ transactionId }	User makes a successful purchase using his EUR wallet as a payment method.
launchpad.purchase.pocket.error	{ transactionId }	User tries to make a purchase using his EUR wallet as a payment method but the operation fails.
Authentication
ApiKeyAuth
The Bit2Me Crypto API service requires an api key to access private endpoints. 🔑 To get your API Keys, please get in touch with our sales team. Our knowledge base contains a detailed guide on how to work with API keys.

⚠️ Never share an API key, if you suspect that an API key was compromised revoke it immediately.

When generating an API key, you can ask us to customize it using the following scopes for the keys:

Read - grants access to all api endpoints, except for creating or canceling orders and transfers.

Trade - allows creation or cancellation of orders.

Withdraw - allows withdrawals (these withdrawals bypass two factor authentication).

You may optionally add an IP restriction. Any request using that API key is rejected, unless the source IP of the request is one of the trusted IPs.

⚠️ Always select the minimal required scope for an api key. We recommend to set one or more trusted IPs to further harden API keys with scope Trade or Withdraw.

Make sure that your client validates the server certificate and aborts if validation fails. For accessing the API a valid API-Key must be passed in the header.

info
To operate on behalf of a subaccount.
It is necessary to add the token that identifies it. To do this the following key/value must be sent on header:

X-SUBACCOUNT-ID: <subaccount id>
The following key/value must be sent on header:

X-API-KEY: <your api key>
Nonce header is also required to be sent. The nonce value corresponds to the current value of the unix timestamp in UTC and has a valid time window of 5 seconds.

x-nonce: 1687155308
If request needs to be signed you have to include following header:

api-signature: <signature>
Signature must be generated using the nonce, the request URL and the body. An example in javascript to GET /v1/trading/wallet/balance is shown below:

const axios = require('axios');
const crypto = require('crypto');

const API_KEY = 'YOUR API KEY;
const SECRET = 'YOUR SECRET;

const NONCE = Date.now(); // MUST be UTC time zone
const PATH = '/v1/trading/wallet/balance';
const SERVER = 'https://gateway.bit2me.com';

const getAuthHeaders = (nonce, path, body) => {
  const messageToSign = getClientMessageToSign(nonce, path, body);
  const signature = getMessageSignature(messageToSign, SECRET);

  return {
    headers: {
      'x-api-key': API_KEY,
      'api-signature': signature,
      'x-nonce': nonce
    }
  };
};

const getClientMessageToSign = (nonce, url, body) => {
  const hasBody = !!body;

  return hasBody
    ? `${nonce}:${url}:${JSON.stringify(body)}`
    : `${nonce}:${url}`;
};

const getMessageSignature = (message, secret) => {
  const hash = crypto.createHash('sha256');
  const hmac = crypto.createHmac('sha512', secret);
  const hashDigest = hash.update(message).digest('binary');
  const hmacDigest = hmac.update(hashDigest, 'binary').digest('base64');

  return hmacDigest;
};

const config = getAuthHeaders(NONCE, PATH, undefined);
const response = await axios.get(`${SERVER}${PATH}`, config);
console.log(response.data);

Important: The body used to generate the signature must be the request body string. In javascript, it can be obtained with JSON.stringify(body).

const nonce = 1687155308;
const url = '/v1/trading/order';
const body = {
  side: "sell",
  symbol: "B2M/EUR",
  price: "0.09999",
  amount: "5001.00000000",
  orderType: "limit"
};

const bodyString = JSON.stringify(body);
const messageToSign = `${nonce}:${url}:${bodyString}`;
const signature = getMessageSignature(messageToSign, SECRET);

const response = await axios.post(`${SERVER}${url}`, body, {
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': API_KEY,
    'api-signature': signature,
    'x-nonce': nonce
  }
});
TOTP
There are some operations that require 2FA authentication. Following headers must be included in this cases:

Header x-totp - contains 2FA code

Header x-totp-type - contains the type of how the 2FA code was received (Type: ['gauth', 'sms', 'email'])

⚠️ For subaccount operations the totp-type always will be 'gauth'

Server
Server:
https://gateway.bit2me.com
Gateway API

No authentication selected
Client Libraries
Shell Curl
Access ​
AccessOperations
post
/v1/signin/embed
post
/v1/signin/apikey
get
/v3/signin/sfa
Signing to embed subaccount​
Generates an access token and refresh token that you can use to call other APIs.

Body
required
application/json
The data to sigin

accessToken
Type:string
Responses
Request Example forpost/v1/signin/embed
# Signin to embed subaccount
curl -X POST ${SERVER_URL}/v1/signin/embed
  -H 'Content-type: application/json'
  -d '{"accessToken":"<token>"}'

{
  "accessToken": {
    "token": "string",
    "expirationTime": 1
  },
  "refreshToken": {
    "token": "string",
    "expirationTime": 1
  },
  "session": {
    "id": "string",
    "expirationTime": 1
  }
}
Success

Authorize user by apiKey​
Authorize user by apiKey

Body
application/json
The data to sigin

userId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
Responses
Request Example forpost/v1/signin/apikey
const axios = require('axios');
const crypto = require('crypto');

const API_KEY = 'YOUR_API_KEY';
const SECRET = 'YOUR_API_SECRET';

const NONCE = Date.now();
const PATH = '/v1/signin/apikey';
const SERVER = 'https://gateway.bit2me.com';

const getAuthHeaders = (nonce, path, body) => {
  const messageToSign = getClientMessageToSign(nonce, path, body);
  const signature = getMessageSignature(messageToSign, SECRET);

  return {
    headers: {
      'x-api-key': API_KEY,
      'api-signature': signature,
      'x-nonce': nonce
    }
  };
};

const getClientMessageToSign = (nonce, url, body) => {
  const hasBody = !!body && Object.keys(body).length > 0;

  return hasBody
    ? `${nonce}:${url}:${JSON.stringify(body)}`
    : `${nonce}:${url}`;
};

const getMessageSignature = (message, secret) => {
  const hash = crypto.createHash('sha256');
  const hmac = crypto.createHmac('sha512', secret);
  const hashDigest = hash.update(message).digest('binary');
  const hmacDigest = hmac.update(hashDigest, 'binary').digest('base64');

  return hmacDigest;
};

const config = getAuthHeaders(NONCE, PATH);
axios.post(`${SERVER}${PATH}`, {}, config).then(response=>console.log(response.data));

{
  "accessToken": {
    "token": "string",
    "expirationTime": 1
  }
}
Success

Check 2fa user type​
Check active user verification and start the process

Responses
Request Example forget/v3/signin/sfa
# Get user 2fa type
curl -X GET ${SERVER_URL}/v3/signin/sfa
  -H 'X-API-KEY: <api key>'

{
  "sfaType": "gauth",
  "retryIntervalSeconds": 0
}
Success

Account ​
AccountOperations
put
/v1/account/update
get
/v3/account
delete
/v1/account
get
/v2/account/address
post
/v2/account/address
put
/v1/account/address
delete
/v1/account/address
get
/v1/account/verify/identity
post
/v1/account/verify/identity
get
/v1/account/professions
get
/v1/account/purposes
get
/v1/account/employment-status
get
/v1/account/deposit-estimation
get
/v1/account/funds-origin
get
/v1/account/subaccount
post
/v1/account/subaccount
put
/v1/account/users/person/identity
post
/v1/account/settings/sfa
put
/v1/account/settings/sfa
post
/v1/account/subaccount/sfa
put
/v1/account/subaccount/sfa
Update account​
Update info for an account

Body
required
application/json
The account details to be updated

address
Type:object
alias
Type:string
Pattern:^[0-9a-z\-_]{2,30}$
depositEstimation
Type:object
fundsOrigin
Type:object
person
Type:object
profile
Type:object
selfInvoiceIdentityNumber
Type:string
max length:  
30
so
Type:string
type
Type:string
enum
person
company
employee
version
Type:string
Responses
Request Example forput/v1/account/update
# Update subaccount
curl -X PUT ${SERVER_URL}/v1/account/update
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
  -d '{
      "person": {
        "name": <String>,
        "surname": <String>,
        "birthDate": <DateISO8601>,
        "nationalityCountryCode": <CountryISO3166-1Alpha2>,
      },
      "profile": {
        "langCode": <LangISO639-1>,
        "currencyCode": <CurrencyISO4217>,
        "timeZone": <String>
      }
    }'

{
  "result": true
}
Success

Get account details​
Get account details, personal data is returned masked

Responses
Request Example forget/v3/account
curl https://gateway.bit2me.com/v3/account \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "id": "string",
  "email": "hello@example.com",
  "realEmail": "hello@example.com",
  "phone": {
    "number": "string",
    "countryCode": "string"
  },
  "alias": "string",
  "person": {
    "name": "string",
    "surname": "string",
    "gender": "male",
    "nationalityCountryCode": "string"
  },
  "profile": {
    "langCode": "string",
    "currencyCode": "string",
    "timeZone": "string",
    "avatar": {
      "sm": "string",
      "md": "string",
      "lg": "string"
    }
  },
  "selfInvoiceIdentityNumber": "string",
  "registrationDate": "2026-02-17T14:25:44.778Z",
  "type": "person",
  "depositEstimation": {
    "minimum": 1,
    "maximum": 1
  },
  "fundsOrigin": {
    "type": "salary",
    "othersReason": "string"
  },
  "accountPurpose": "savings",
  "secondFactorAuth": {
    "alwaysRequired": true
  },
  "documentValidity": "valid",
  "company": {
    "businessName": "string",
    "kindOfSociety": "string",
    "constitutionDate": "2026-02-17T14:25:44.778Z",
    "constitutionCountryCode": "string",
    "registeredOffice": "string",
    "sector": "string",
    "autonomus": true,
    "obligedSubject": true,
    "overTheCounter": true,
    "politicallyExposedPersonPartners": true,
    "politicalPartners": [
      {
        "name": "string",
        "position": "string"
      }
    ],
    "firstTradeEstimatedValue": 1,
    "annualTradeEstimatedValue": 1,
    "billingVolume": 1,
    "numberOfPartners": 1,
    "reasonForTheOperation": [
      "string"
    ],
    "typeOfOperationsToPerform": [
      "string"
    ],
    "identity": {
      "type": "none",
      "number": "string",
      "countryCode": "string",
      "updatedAt": "2026-02-17T14:25:44.778Z"
    },
    "taxId": "string",
    "legalEntityId": "string",
    "contact": {
      "name": "string",
      "surname": "string",
      "typeOfDocument": "none",
      "numberOfDocument": "string"
    },
    "attorneyInFact": {
      "name": "string",
      "surname": "string",
      "typeOfDocument": "none",
      "numberOfDocument": "string"
    },
    "legalTerms": true,
    "service": "string",
    "webUrl": null,
    "shareholdingStructure": null,
    "services": [
      "crypto_investment"
    ],
    "otherServices": null,
    "partners": [
      {
        "nationalityCountryCode": "string",
        "companyPartnerId": "string",
        "documentType": "none",
        "documentNumber": "string",
        "documentCountryCode": "string",
        "birthdate": "2026-02-17T14:25:44.778Z",
        "sharePercentage": 1,
        "fullName": "string",
        "isPoliticallyExposed": true,
        "deletedAt": "2026-02-17T14:25:44.778Z"
      }
    ],
    "economicCapacityModel": "model_200"
  },
  "accountCompleted": true,
  "knowledgeLevel": 1,
  "registrationReason": "investing",
  "knowledgeQuestionsStatus": "completed"
}
Success

Delete account​
Delete user account

Responses
200
Success

Request Example fordelete/v1/account
curl https://gateway.bit2me.com/v1/account \
  --request DELETE \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

List user addresses​
Get the addresses of a specific user

Query Parameters
addressId
Type:string
The address id

isResidence
Type:boolean
Value of the isResidence field

Responses
Request Example forget/v2/account/address
curl https://gateway.bit2me.com/v2/account/address \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "alias": "string",
    "streetAddress": "string",
    "city": "string",
    "stateCode": "string",
    "zip": "string",
    "countryCode": "string",
    "isResidence": true,
    "isDefaultAddress": true
  }
]
Success

Create address​
Add address to an user

Body
required
application/json
Address params

city
Type:string
max length:  
255
required
countryCode
Type:string
Pattern:^[A-Z]{2}$
required
nationalityCountryCode
Type:string
Pattern:^[A-Z]{2}$
required
stateCode
Type:string
required
Value obtained from 'fips' (Federal Information Processing Standard (https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)) field in /v1/misc/country/{countryISOCode}/region response.

Additional information of this endpoint is available in misc section

streetAddress
Type:string
max length:  
255
required
zip
Type:string
max length:  
255
required
alias
Type:string
max length:  
50
id
Type:string
Format:uuid
isDefaultAddress
Type:boolean
isResidence
Type:boolean
userId
Type:string
Format:uuid
Responses
Request Example forpost/v2/account/address
# Create subaccount address
curl -X POST ${SERVER_URL}/v2/account/address
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
  -d '{
      "city": <String>,
      "countryCode": <CountryISO3166-1Alpha2>,
      "nationalityCountryCode": <CountryISO3166-1Alpha2>,
      "stateCode": <String>,
      "streetAddress": <String>,
      "zip": <String>
    }'

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "alias": "string",
  "streetAddress": "string",
  "city": "string",
  "stateCode": "string",
  "zip": "string",
  "countryCode": "string",
  "isResidence": true,
  "isDefaultAddress": true
}
Created

Update address​
Update user address

Query Parameters
addressId
Type:string
required
The address id

Body
required
application/json
Address params

city
Type:string
max length:  
255
required
countryCode
Type:string
Pattern:^[A-Z]{2}$
required
nationalityCountryCode
Type:string
Pattern:^[A-Z]{2}$
required
stateCode
Type:string
required
Value obtained from 'fips' (Federal Information Processing Standard (https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)) field in /v1/misc/country/{countryISOCode}/region response.

Additional information of this endpoint is available in misc section

streetAddress
Type:string
max length:  
255
required
zip
Type:string
max length:  
255
required
alias
Type:string
max length:  
50
id
Type:string
Format:uuid
isDefaultAddress
Type:boolean
isResidence
Type:boolean
userId
Type:string
Format:uuid
Responses
Request Example forput/v1/account/address
curl 'https://gateway.bit2me.com/v1/account/address?addressId=' \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "id": "",
  "userId": "",
  "alias": "",
  "streetAddress": "",
  "city": "",
  "stateCode": "",
  "zip": "",
  "countryCode": "",
  "isResidence": true,
  "isDefaultAddress": true,
  "nationalityCountryCode": ""
}'
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "alias": "string",
    "streetAddress": "string",
    "city": "string",
    "stateCode": "string",
    "zip": "string",
    "countryCode": "string",
    "isResidence": true,
    "isDefaultAddress": true
  }
]
Success

Delete address​
Remove user address

Query Parameters
addressId
Type:string
required
The address id

Responses
204
Success

Request Example fordelete/v1/account/address
curl 'https://gateway.bit2me.com/v1/account/address?addressId=' \
  --request DELETE \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Get identity verification status​
Return the current status of the identity verification

Responses
Request Example forget/v1/account/verify/identity
curl https://gateway.bit2me.com/v1/account/verify/identity \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "status": "nodata",
  "error": [
    "number"
  ],
  "image": [
    "document"
  ],
  "disableProcess": true,
  "risk": {
    "level": "undefined",
    "minPoints": 0,
    "maxPoints": 0,
    "action": "string"
  },
  "kycExpress": {
    "status": "success",
    "updatedAt": "2026-02-17"
  },
  "questions": true,
  "extraMeasurePending": true,
  "extraMeasuresNotApproved": {
    "compliance": [
      "MR2"
    ]
  },
  "tier": 1
}
Success

Set data to be verified​
Send the data to be verified (change the status to pending)

Responses
Request Example forpost/v1/account/verify/identity
curl https://gateway.bit2me.com/v1/account/verify/identity \
  --request POST \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "result": true
}
Success

List professions​
Get professions. Only lower case.

Query Parameters
langCode
Type:string
Lang code

Responses
Request Example forget/v1/account/professions
curl https://gateway.bit2me.com/v1/account/professions
{
  "total": 1,
  "data": [
    {
      "id": "string",
      "description": "string",
      "professionCode": "string",
      "langCode": "string"
    }
  ]
}
Success

List purposes​
Get purposes. Only lower case.

Query Parameters
langCode
Type:string
Lang code

Responses
Request Example forget/v1/account/purposes
curl https://gateway.bit2me.com/v1/account/purposes
{
  "total": 1,
  "data": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "langCode": "string"
    }
  ]
}
Success

List employment status​
All employment status translations. Only lower case

Query Parameters
langCode
Type:string
Lang code

Responses
200
A list of employmentStatus translations

Request Example forget/v1/account/employment-status
curl https://gateway.bit2me.com/v1/account/employment-status \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

List deposit estimations​
All deposits estimations

Responses
200
A list of employmentStatus translations

Request Example forget/v1/account/deposit-estimation
curl https://gateway.bit2me.com/v1/account/deposit-estimation \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

List funds origin​
All funds origins. Only lower case.

Query Parameters
langCode
Type:string
Lang code

Responses
200
A list of funds origins

Request Example forget/v1/account/funds-origin
curl https://gateway.bit2me.com/v1/account/funds-origin \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

List subaccounts​
Get my subaccounts

Responses
Request Example forget/v1/account/subaccount
curl https://gateway.bit2me.com/v1/account/subaccount \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "total": 1,
  "data": [
    {
      "id": "string",
      "email": "hello@example.com",
      "name": "string",
      "surname": "string",
      "phone": {
        "number": "string",
        "countryCode": "string"
      }
    }
  ]
}
Success

Create subaccount​
Create a subaccount

Body
required
application/json
The details to create the subaccount

email
Type:string
min length:  
6
max length:  
96
Format:email
required
name
Type:string
required
phone
Type:object
required
surname
Type:string
required
Responses
Request Example forpost/v1/account/subaccount
# Create subaccount
curl -X POST ${SERVER_URL}/v1/account/subaccount
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -d '{
    "email": "<user email>",
    "name": "<user name>",
    "surname": "<user surname>",
    "phone": {
      "number": "<phoneNumber>",
      "countryCode": "<countryCode>",
    }
  }'

{
  "userId": "string"
}
Success

Update user person identity​
Update user person identity

Body
required
application/json
The details to update user person identity

countryCode
Type:string
Pattern:^[A-Z]{2}$
required
expiryDate
Type:string
Format:date-time
required
the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z

number
Type:string
max length:  
24
required
type
Type:string
enum
required
none
idcard
passport
drivinglicense
visa
Responses
Request Example forput/v1/account/users/person/identity
curl https://gateway.bit2me.com/v1/account/users/person/identity \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "type": "none",
  "number": "",
  "expiryDate": "",
  "countryCode": ""
}'
{
  "result": true
}
Success

Start 2fa enablement​
Starts the process to enable the two-factor authentication. After calling this endpoint you must call (PUT) /v1/account/settings/sfa and pass a TOTP to finish the process.

Responses
Request Example forpost/v1/account/settings/sfa
# Start 2fa enablement
curl -X POST ${SERVER_URL}/v1/account/settings/sfa
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-TOTP: <2fa code>'
  -H 'X-TOTP-TYPE: <['gauth', 'sms', 'email']>'
  -d '{}'

{
  "qrImage": "string",
  "secret": "string",
  "name": "string"
}
Success

End 2fa enablement​
Ends the process to enable the two-factor authentication. With this endpoint we make sure that the TOTP on the server side and the TOTP on the client side match.

Body
required
application/json
The details to end the process

totp
Type:string
Pattern:^[0-9]{4,6}$
required
alwaysRequired
Type:boolean
sessionId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
Responses
Request Example forput/v1/account/settings/sfa
# End 2fa enablement
curl -X PUT ${SERVER_URL}/v1/account/settings/sfa
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -d '{
    "totp": <2fa code>,
  }'

{
  "result": true
}
Success

Start subaccount 2fa enablement​
Init subaccount google authenticator 2fa process

Body
required
application/json
The details to init subaccount 2fa process

subaccountUserId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
Responses
Request Example forpost/v1/account/subaccount/sfa
curl https://gateway.bit2me.com/v1/account/subaccount/sfa \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "subaccountUserId": ""
}'
{
  "secret": "string"
}
Success

End subaccount 2fa enablement​
End subaccount google authenticator 2fa process

Body
required
application/json
The details to end subaccount 2fa process

subaccountUserId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
totp
Type:string
Pattern:^[0-9]{4,6}$
required
Responses
Request Example forput/v1/account/subaccount/sfa
curl https://gateway.bit2me.com/v1/account/subaccount/sfa \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "subaccountUserId": "",
  "totp": ""
}'
{
  "result": true
}
Success

KYC ​
KYCOperations
post
/v3/account/verify/identity/init
get
/v1/verifier/subaccount/file
get
/v1/account/verify/identity/verification/retry
Init KYC verification​
Init KYC verification iframe. Open the redirectUrl in a native browser.

Do NOT open the url in webviews to avoid incompatibilities with screen or camera recording permissions.

Body
application/json
locale
Type:string
required
errorUrl
Type:string
successUrl
Type:string
workflowId
enum
default: 
10011
const:  
10011
Workflow id: 10011

10011
Responses
Request Example forpost/v3/account/verify/identity/init
curl https://gateway.bit2me.com/v3/account/verify/identity/init \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "locale": "",
  "workflowId": 10011,
  "successUrl": "",
  "errorUrl": ""
}'
{
  "redirectUrl": "string",
  "token": "string",
  "reference": "string",
  "provider": "jumio"
}
Success

Identity file download​
Download an identity file of a subaccount

Query Parameters
identityFileType
Type:string
enum
required
The identity file type to download

backDocument
frontDocument
selfie
livenessFrontDocument
livenessBackDocument
livenessSelfie
subAccountId
Type:string
required
The identifier of the subaccount

Responses
Request Example forget/v1/verifier/subaccount/file
curl 'https://gateway.bit2me.com/v1/verifier/subaccount/file?identityFileType=backDocument&subAccountId=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
file
Success

Check verification retry​
Gets a response based on whether the user can retry the verification process

Responses
200
Success

Request Example forget/v1/account/verify/identity/verification/retry
# Check subaccount verification retries
curl -X GET ${SERVER_URL}/v1/account/verify/identity/verification/retry
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'

{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Not acceptable

Wallet ​
WalletOperations
get
/v2/wallet/pocket/{pocketId}/{network}/address
post
/v1/wallet/pocket
get
/v1/wallet/pocket
put
/v1/wallet/pocket
delete
/v1/wallet/pocket
post
/v1/wallet/transaction
get
/v1/wallet/transaction
post
/v1/wallet/transaction/proforma
get
/v1/wallet/transaction/{id}
put
/v1/wallet/transaction/{id}
get
/v1/wallet/settings/assets
get
/v2/wallet/transaction
List pocket addresses​
Find all address by pocket ID and Network or create one new

Path Parameters
pocketId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
network
Type:string
required
Responses
Request Example forget/v2/wallet/pocket/{pocketId}/{network}/address
# Subaccount pocket addresses
curl -X GET ${SERVER_URL}/v2/wallet/pocket/{pocketId}/{network}/address
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
    

[
  {
    "id": "string",
    "createdAt": "2026-02-17T14:25:44.778Z",
    "address": "string",
    "network": "ethereum",
    "tag": "string"
  }
]
Success

Create pocket​
Create a new pocket

Body
required
application/json
currency
Type:string
required
Valid currency symbol

name
Type:string
min length:  
1
max length:  
20
required
Responses
Request Example forpost/v1/wallet/pocket
# Create subaccount pocket
curl -X POST ${SERVER_URL}/v1/wallet/pocket
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
  -d '
    {
      "currency":"BTC",
      "name":"Bitcoin pocket",
      "color":"0"
    }'
    

{
  "id": "string"
}
Success

Get pocket details​
Get the data of a specific pocket or the data of all pockets of the user (if the id param is not set)

Query Parameters
id
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
With this parameter you can specify the pocket you want to get the data from. If this parameter is not set, all pockets of the user are returned

Responses
Request Example forget/v1/wallet/pocket
# Retrieve one pocket details
curl -X GET ${SERVER_URL}/v1/wallet/pocket?id=<pocketId>
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'

# Retrieve all pocket details
curl -X GET ${SERVER_URL}/v1/wallet/pocket
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'

# Subaccounts. Retrieve one pocket details
curl -X GET ${SERVER_URL}/v1/wallet/pocket?id=<pocketId>
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'

# Subaccounts. Retrieve all pocket details
curl -X GET ${SERVER_URL}/v1/wallet/pocket
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
    

[
  {
    "id": "string",
    "name": "string",
    "color": 1,
    "currency": "BTC",
    "balance": "string",
    "blockedBalance": "string",
    "createdAt": "2026-02-17T14:25:44.778Z"
  }
]
Success

Update pocket​
Update pocket data

Body
required
application/json
id
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
color
Type:integer
min:  
0
max:  
15
Tag to categorize the pocket

name
Type:string
min length:  
1
max length:  
20
Responses
Request Example forput/v1/wallet/pocket
curl https://gateway.bit2me.com/v1/wallet/pocket \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "id": "",
  "name": "",
  "color": 1
}'
{
  "result": true
}
Success

Delete pocket​
Delete a pocket

Query Parameters
id
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
Responses
Request Example fordelete/v1/wallet/pocket
curl 'https://gateway.bit2me.com/v1/wallet/pocket?id=' \
  --request DELETE \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "result": true
}
Success

Execute transaction​
Executes a previuosly created transaction

Body
required
application/json
proforma
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
concept
Type:string
max length:  
100
note
Type:string
max length:  
100
Responses
Request Example forpost/v1/wallet/transaction
const axios = require('axios');
const crypto = require('crypto');

const API_KEY = 'YOUR_API_KEY';
const SECRET = 'YOUR_API_SECRET';

const NONCE = Date.now();
const PATH = '/v1/wallet/transaction';
const SERVER = 'https://gateway.bit2me.com';

const getAuthHeaders = (nonce, path, body) => {
  const messageToSign = getClientMessageToSign(nonce, path, body);
  const signature = getMessageSignature(messageToSign, SECRET);

  return {
    headers: {
      'x-api-key': API_KEY,
      'api-signature': signature,
      'x-nonce': nonce
    }
  };
};

const getClientMessageToSign = (nonce, url, body) => {
  const hasBody = !!body && Object.keys(body).length > 0;

  return hasBody
    ? `${nonce}:${url}:${JSON.stringify(body)}`
    : `${nonce}:${url}`;
};

const getMessageSignature = (message, secret) => {
  const hash = crypto.createHash('sha256');
  const hmac = crypto.createHmac('sha512', secret);
  const hashDigest = hash.update(message).digest('binary');
  const hmacDigest = hmac.update(hashDigest, 'binary').digest('base64');

  return hmacDigest;
};

const body = {
    "proforma": "PROFORMA_ID" // id obtained in create transaction step
  };

const config = getAuthHeaders(NONCE, PATH, body);
axios.post(`${SERVER}${PATH}`,body,config).then(response=>console.log(response.data));

{
  "result": true
}
Success

deprecated
List transactions​
Obtains all transactions related to a pocket. If pocketId is not specified, all user's transactions are returned.

Transactions can be paginated using offset and limit parameters. For example, to get the third page and show 20 registers per page you would use the following query:

/v1/wallet/transaction?offset=40&limit=20
Multiple filtering options could be applied when retrieving transactions. Example:

/v1/wallet/transaction?pocketId=9a2dfa96-2fb8-4b76-a9bd-83949c417540&type=deposit
Query Parameters
pocketId
Type:string
Pattern:^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12},?)+$
The pocket identifier to get the transactions or comma delimited list of pocket IDs

offset
Type:integer
min:  
0
max:  
9007199254740991
Specify the number of entries to be skipped (0 by default)

limit
Type:integer
min:  
1
max:  
100
Specify the maximum number of entries to be returned (20 by default)

keyword
Type:string
min length:  
1
max length:  
120
Pattern:^[\w\u00C0-\u017F \-,]+$
Specify a list (comma-separated values) of keywords to be used to filter the query

type
Type:string
enum
Specify the transaction type to filter the entries to be returned (or comma delimited list of types)

transfer
withdrawal
deposit
subtype
Type:string
enum
Specify the transaction subtype to filter the entries to be returned (or comma delimited list of subtypes)

purchase
sell
manual-send
automatic-send
manual-transfer
method
Type:string
enum
Specify the transaction method to filter the entries to be returned (or comma delimited list of methods)

pocket
blockchain
card
bank
bank-transfer
profit-share
promo-referral
from
Type:string
Format:date-time
Specify the start date (ISO 8601) to filter the date (mandatory if the to parameter is set)

to
Type:string
Format:date-time
Specify the end date (ISO 8601) to filter the date (mandatory if the from parameter is set)

userCurrency
Type:string
default: 
"EUR"
The user's currency (used to show a rate from it to Euro)

Responses
Request Example forget/v1/wallet/transaction
curl https://gateway.bit2me.com/v1/wallet/transaction \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "total": 1,
  "data": [
    {
      "id": "string",
      "date": "2026-02-17",
      "type": "deposit",
      "concept": "string",
      "origin": {
        "currency": "string",
        "amount": "string",
        "pocketId": "string",
        "pocketName": "string",
        "class": "pocket",
        "rate": {
          "rate": {
            "value": "string",
            "pair": {
              "base": "BTC",
              "quote": "BTC"
            }
          }
        }
      },
      "destination": {
        "currency": "string",
        "amount": "string",
        "pocketName": "string",
        "pocketId": "string",
        "address": "string",
        "addressNetwork": "string",
        "addressInBlacklist": true,
        "class": "pocket",
        "rate": {
          "rate": {
            "value": "string",
            "pair": {
              "base": "BTC",
              "quote": "BTC"
            }
          }
        }
      },
      "transaction": {
        "confirmedAt": "2026-02-17T14:25:44.778Z",
        "confirmationCount": 0
      }
    }
  ]
}
Success

Create transaction​
Creates a new proforma transaction (it includes an expiration time)

If the type parameter is not specified, REA is used by default.

The destination parameter only accepts one field (use destination.address to specify a crytocurrency address or destination.pocket to specify the ID of the destination pocket)

Security Constraints: User's email must be validated in order to use this endpoint.

For peer to peer transactions, a sell operation has to be made on source pocket and a buy operation has to be made on destination pocket

IMPORTANT: All blockchain withdrawals must be accompanied by Travel Rule information to be processed. Please see.

Body
required
application/json
amount
Type:string
min length:  
1
max length:  
50
Pattern:^[0-9]*\.?[0-9]*$
required
currency
Type:string
required
concept
Type:string
max length:  
100
destination
Type:object
note
Type:string
max length:  
100
operation
Type:string
enum
This property is not necessary for other operation types

purchase
withdrawal-trading
deposit-trading
social-payment
launchpad-purchase
buy
sell
origin
Type:object
pair
Type:string
Pattern:^[A-Z0-9]+/[A-Z0-9]+$
pocket
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
queryParams
Type:object
Used for some cryptos that need extra parameters to do blockchain sendings. For example, memo in XRP.

receiverName
Type:string
type
Type:string
enum
Indicates if the amount of the transaction is what the receiver will get or what will be deducted from the sender's balance:

SEA: Acronym for Send Exact Amount
REA: Acronym for Receive Exact Amount
SEA
REA
Responses
Request Example forpost/v1/wallet/transaction/proforma
const axios = require('axios');
const crypto = require('crypto');

const API_KEY = 'YOUR_API_KEY';
const SECRET = 'YOUR_API_SECRET';

const NONCE = Date.now();
const PATH = '/v1/wallet/transaction/proforma';
const SERVER = 'https://gateway.bit2me.com';

const getAuthHeaders = (nonce, path, body) => {
  const messageToSign = getClientMessageToSign(nonce, path, body);
  const signature = getMessageSignature(messageToSign, SECRET);

  return {
    headers: {
      'x-api-key': API_KEY,
      'api-signature': signature,
      'x-nonce': nonce
    }
  };
};

const getClientMessageToSign = (nonce, url, body) => {
  const hasBody = !!body && Object.keys(body).length > 0;

  return hasBody
    ? `${nonce}:${url}:${JSON.stringify(body)}`
    : `${nonce}:${url}`;
};

const getMessageSignature = (message, secret) => {
  const hash = crypto.createHash('sha256');
  const hmac = crypto.createHmac('sha512', secret);
  const hashDigest = hash.update(message).digest('binary');
  const hmacDigest = hmac.update(hashDigest, 'binary').digest('base64');

  return hmacDigest;
};

// Body example for buy operation
const body = {
    "operation": "buy",
    "pair": "BTC/EUR",
    "amount": "100",
    "currency": "EUR"
  };

// Body example for sell operation
// const body = {
//    "operation": "sell",
//    "pair": "BTC/EUR",
//    "amount": "0.0002",
//    "currency": "BTC"
//  };

// Body example for swap operation
// const body = {
//    "pocket": "<UUID of a user crypto pocket>",
//    "amount": "0.001",
//    "currency": "BTC",
//    "destination": {
//        "pocket": "<UUID of a user crypto pocket>"
//    },
//    "type": "SEA",
//    "userCurrency": "EUR"
//  };

// Body example for withdraw operation
// const body = {
//    "pocket": "<UUID of an EUR pocket>",
//    "amount": "10",
//    "currency": "EUR",
//    "type": "SEA",
//    "concept": "",
//    "note": "",
//    "destination": {
//      "bankAccount": {
//          "bankAccount": "<IBAN bank account>",
//          "country": "ES",
//          "receiverName": "Test",
//      }
//    },
//    "userCurrency": "EUR"
//  };

const config = getAuthHeaders(NONCE, PATH, body);
axios.post(`${SERVER}${PATH}`,body,config).then(response=>console.log(response.data));

{
  "id": "string",
  "expirationTime": "2026-02-17T14:25:44.778Z",
  "origin": {
    "amount": "string",
    "currency": "BTC",
    "rate": {
      "rate": {
        "value": "string",
        "pair": {
          "base": "BTC",
          "quote": "BTC"
        }
      }
    }
  },
  "destination": {
    "amount": "string",
    "currency": "BTC",
    "rate": {
      "rate": {
        "value": "string",
        "pair": {
          "base": "BTC",
          "quote": "BTC"
        }
      }
    }
  },
  "fee": {
    "network": {
      "amount": "string",
      "currency": "string"
    },
    "flip": {
      "percentage": "string",
      "amount": "string",
      "currency": "BTC"
    },
    "teller": {
      "fixed": {
        "amount": "string",
        "currency": "BTC"
      },
      "variable": {
        "percentage": "string",
        "amount": "string",
        "currency": "BTC"
      }
    }
  },
  "flip": {
    "rate": {
      "value": "string",
      "pair": {
        "base": "BTC",
        "quote": "BTC"
      }
    }
  },
  "userRate": {
    "rate": {
      "value": "string",
      "pair": {
        "base": "BTC",
        "quote": "BTC"
      }
    }
  },
  "userAmount": {
    "currency": "BTC",
    "amount": "string"
  }
}
Success

Get transaction details​
Get the details of a transaction

Path Parameters
id
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
The transaction id (returned by GET /v1/transaction)

Query Parameters
userCurrency
Type:string
default: 
"EUR"
The user's currency (used to show a rate from it to Euro)

Responses
Request Example forget/v1/wallet/transaction/{id}
curl 'https://gateway.bit2me.com/v1/wallet/transaction/{id}' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "date": "2026-02-17T14:25:44.778Z",
  "type": "deposit",
  "concept": "string",
  "note": "string",
  "origin": {
    "currency": "string",
    "amount": "string",
    "pocketName": "string",
    "pocketId": "string",
    "class": "pocket",
    "rate": {
      "rate": {
        "value": "string",
        "pair": {
          "base": "BTC",
          "quote": "BTC"
        }
      }
    }
  },
  "destination": {
    "currency": "string",
    "amount": "string",
    "pocketName": "string",
    "pocketId": "string",
    "address": "string",
    "addressNetwork": "string",
    "addressInBlacklist": true,
    "class": "pocket",
    "rate": {
      "rate": {
        "value": "string",
        "pair": {
          "base": "BTC",
          "quote": "BTC"
        }
      }
    }
  },
  "transaction": {
    "hash": "string",
    "confirmedAt": "2026-02-17T14:25:44.778Z",
    "confirmationCount": 0
  },
  "fee": {
    "network": {
      "amount": "string",
      "currency": "BTC",
      "rate": {
        "rate": {
          "value": "string",
          "pair": {
            "base": "BTC",
            "quote": "BTC"
          }
        }
      }
    },
    "flip": {
      "percentage": "string",
      "amount": "string",
      "currency": "BTC"
    },
    "teller": {
      "id": "string",
      "feeCurrency": "string",
      "fixedFee": "string",
      "variableFee": "string",
      "variableFeePercentage": "string"
    }
  },
  "flip": {
    "rate": {
      "value": "string",
      "pair": {
        "base": "BTC",
        "quote": "BTC"
      }
    }
  },
  "substractFeeType": "SEA"
}
Success

Update transaction​
Updates some data of the specified transaction

Path Parameters
id
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
The transaction id

Body
application/json
note
Type:string
max length:  
100
required
Responses
Request Example forput/v1/wallet/transaction/{id}
curl 'https://gateway.bit2me.com/v1/wallet/transaction/{id}' \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "note": ""
}'
{
  "result": true
}
Success

Get assets settings​
Responses
Request Example forget/v1/wallet/settings/assets
curl https://gateway.bit2me.com/v1/wallet/settings/assets
[
  {
    "symbol": "BTC",
    "actions": [
      "deposit"
    ],
    "limit": {
      "instant": {
        "min": "string",
        "max": "string"
      }
    }
  }
]
Success

List transactions​
Get user transactions. Transactions can be paginated using offset and limit parameters. For example, to get the third page and show 20 registers per page you would use the following query:

/v2/wallet/transaction?offset=40&limit=20

Query Parameters
offset
Type:integer
min:  
0
max:  
9007199254740991
Specify the number of entries to be skipped (0 by default)

limit
Type:integer
min:  
1
max:  
100
Specify the maximum number of entries to be returned (20 by default)

year
Type:integer
Filter movements to this specific year

currency
Type:string
Currency in which movements has been involved

operation
Type:string
enum
Operation to filter

purchase
sell
swap
deposit
withdrawal
Responses
Request Example forget/v2/wallet/transaction
curl https://gateway.bit2me.com/v2/wallet/transaction \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "data": [
    {
      "id": "f040acdf-62b0-4040-9574-655fdcf7e541",
      "note": "This is a transaction note",
      "date": "2024-03-28T13:06:18.032Z",
      "completedAt": "2024-03-28T13:06:18.032Z",
      "canceledAt": "2024-03-28T13:06:18.032Z",
      "concept": "Concept of the transaction",
      "type": "transfer",
      "subtype": "purchase",
      "method": "pocket",
      "status": "completed",
      "substractFeeType": "SEA",
      "denomination": {
        "amount": "1.00000000",
        "currency": "EUR",
        "rate": {
          "rate": {
            "value": "227887340800401254",
            "pair": {
              "base": "string",
              "quote": "string"
            }
          }
        }
      },
      "frequency": "punctual",
      "isInitialRecurringOrder": false,
      "origin": {
        "currency": "EUR",
        "pocketName": "Euro pocket",
        "pocketId": "9ca6cf96-4645-4658-b086-6cdb367c16bd",
        "bankAccount": "string",
        "email": "string",
        "phone": {
          "number": "string",
          "countryCode": "string"
        },
        "alias": "string",
        "fullName": "string",
        "address": "string",
        "addressNetwork": "string",
        "addressTag": "string",
        "addressInBlacklist": "string",
        "amount": "1.00000000",
        "amountAfterFees": "string",
        "rate": {
          "rate": {
            "value": "64109951628652730944317449085",
            "pair": {
              "base": "string",
              "quote": "string"
            }
          }
        },
        "converted": {
          "amount": "string",
          "amountAfterFees": "string",
          "currency": "string"
        },
        "userAmount": {
          "currency": "EUR",
          "value": "0.99500000"
        },
        "userId": "string",
        "class": "pocket"
      },
      "destination": {
        "currency": "EUR",
        "pocketName": "Euro pocket",
        "pocketId": "9ca6cf96-4645-4658-b086-6cdb367c16bd",
        "bankAccount": "string",
        "email": "string",
        "phone": {
          "number": "string",
          "countryCode": "string"
        },
        "alias": "string",
        "fullName": "string",
        "address": "string",
        "addressNetwork": "string",
        "addressTag": "string",
        "addressInBlacklist": "string",
        "amount": "1.00000000",
        "amountAfterFees": "string",
        "rate": {
          "rate": {
            "value": "44502283176925129659630346180939",
            "pair": {
              "base": "string",
              "quote": "string"
            }
          }
        },
        "converted": {
          "amount": "string",
          "amountAfterFees": "string",
          "currency": "string"
        },
        "userAmount": {
          "currency": "EUR",
          "value": "0.99500000"
        },
        "userId": "string",
        "class": "pocket"
      },
      "transaction": {
        "hash": "string",
        "confirmedAt": "string",
        "confirmationCount": 0
      },
      "fee": {
        "network": {
          "amount": "string",
          "currency": "string"
        },
        "flip": {
          "percentage": "string",
          "amount": "string",
          "currency": "string"
        },
        "teller": {
          "fixed": {
            "amount": "string",
            "currency": "string"
          },
          "variable": {
            "percentage": "string",
            "amount": "string",
            "currency": "string"
          },
          "id": "string",
          "feeCurrency": "string",
          "fixedFee": "string",
          "variableFee": "string",
          "variableFeePercentage": "string"
        }
      },
      "flip": {
        "rate": {
          "value": "50547463180856306652608572641483737727703894078151",
          "pair": {
            "base": "string",
            "quote": "string"
          }
        }
      },
      "benefit": {
        "tier": 0,
        "levelId": "d140c42a-be88-4987-8c3d-38635124ec69",
        "quantity": "0.000000000000000000",
        "percentage": 50,
        "currency": "B2M",
        "amount": 0.53157921
      },
      "userRate": {
        "rate": {
          "value": "528366091465614317160787256192667",
          "pair": {
            "base": "string",
            "quote": "string"
          }
        }
      },
      "userAmount": {
        "currency": "EUR",
        "amount": "string"
      },
      "instantId": "2be1f76b-9332-4e96-9e58-8f9d65206b02",
      "company": {
        "destination": {
          "currency": "EUR",
          "amount": "41.00000000",
          "rate": {
            "value": "811106",
            "pair": {
              "base": "string",
              "quote": "string"
            }
          }
        }
      }
    }
  ],
  "total": 15
}
Success

Funding ​
FundingOperations
post
/v1/blockchain-manager/travel-rule-order/{orderId}
post
/v1/teller/order/cancel
get
/v1/teller/order/status
get
/v1/teller/pocket/reference
get
/v1/teller/iban/validate
post
/v1/teller/order/proforma
post
/v1/teller/order
Provide travel rule information​
The Travel Rule is a regulation that requires transfers of funds, including crypto assets, to include information about the originator and the beneficiary to prevent money laundering and terrorist financing. More information

When you create a blockchain withdrawal, its status will be set to waiting-user-information. To proceed with the transaction, you must send the required Travel Rule parameters. If this information is not provided, the operation will remain in this status and will be automatically canceled within a few hours.

Body
required
application/json
name
Type:string
required
Beneficiary person name or company name.

personType
Type:string
enum
required
If sending to a person or company.

person
company
walletOwnership
Type:string
enum
required
If sending to a own or others address.

own
other
walletType
Type:string
enum
required
Wallet type where the user is sending the information. It coud be an exchange or selfhosted wallet.

exchange
unhosted
exchangeName
Type:string
Exchange name if the operation is send to it.

surname
Type:string
Beneficiary person surname.

Responses
400
Validation errors

401
Unauthorized

Request Example forpost/v1/blockchain-manager/travel-rule-order/{orderId}
curl 'https://gateway.bit2me.com/v1/blockchain-manager/travel-rule-order/{orderId}' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "walletType": "exchange",
  "exchangeName": "",
  "walletOwnership": "own",
  "personType": "person",
  "name": "",
  "surname": ""
}'
{
  "result": true
}
Success

Cancel deposit order​
Changes an order status from "waiting-user" to "cancelled" after the user accepting the transaction

Body
required
application/json
description
Type:string
required
orderId
Type:string
required
Responses
200
Success

Request Example forpost/v1/teller/order/cancel
curl https://gateway.bit2me.com/v1/teller/order/cancel \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "orderId": "",
  "description": ""
}'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Get order status​
Gets order status. If no order is found, "pending" status is returned as default value.

Query Parameters
id
Type:string
required
The order ID or the wallet proforma ID

Responses
Request Example forget/v1/teller/order/status
# Get subaccount order status
curl -X GET ${SERVER_URL}/v1/teller/order/status/<orderId>
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'

{
  "status": "pending"
}
Success

Get pocket reference​
Returns a reference for the specified pocket. Reference is generated if it doesn't exist.

Query Parameters
pocketId
Type:string
required
Id of the pocket to retrieve the reference from

Responses
Request Example forget/v1/teller/pocket/reference
curl 'https://gateway.bit2me.com/v1/teller/pocket/reference?pocketId=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "pocket": {
    "userId": "string",
    "pocketId": "string",
    "reference": "string"
  },
  "bankAccounts": {}
}
Success

Check iban validity​
Get if iban is valid

Query Parameters
iban
Type:string
required
Iban to check

Responses
Request Example forget/v1/teller/iban/validate
curl 'https://gateway.bit2me.com/v1/teller/iban/validate?iban=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "result": true
}
Success

Create deposit​
Create a deposit proforma. In order to execute this order, should be confirmed with /v1/teller/order

Body
application/json
amount
Type:string
required
currency
Type:string
required
method
Type:object
required
orderType
Type:string
enum
required
deposit
purchase
description
Type:string
destination
Type:object
feeType
Type:string
enum
Indicates if the amount of the transaction is what the receiver will get or what will be deducted from the sender's balance:

SEA: Acronym for Send Exact Amount
REA: Acronym for Receive Exact Amount
SEA
REA
Responses
Request Example forpost/v1/teller/order/proforma
curl https://gateway.bit2me.com/v1/teller/order/proforma \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "amount": "10",
  "description": "An order description",
  "currency": "",
  "feeType": "SEA",
  "orderType": "deposit",
  "destination": {
    "type": "pocket",
    "value": "eb775a29-365d-4881-b7b9-1fa66fe1eb4d"
  },
  "method": {
    "type": "creditcard",
    "params": {}
  }
}'
Execute deposit order​
Execute a card order, previously created with /v1/teller/order/proforma

Body
application/json
orderId
Type:string
required
Responses
Request Example forpost/v1/teller/order
curl https://gateway.bit2me.com/v1/teller/order \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "orderId": "dfcf2797-05f2-4cbb-ae5b-f5608dbbf6a9"
}'
Transfers ​
TransfersOperations
get
/v1/social-pay/order
post
/v1/social-pay/order
post
/v1/social-pay/order/claim
List user pay orders​
Get all pending pay order of a user

Responses
412
User not found

Request Example forget/v1/social-pay/order
curl https://gateway.bit2me.com/v1/social-pay/order \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "orderId": "string",
  "createdAt": "2026-02-17T14:25:44.778Z",
  "expiryDate": "2026-02-17T14:25:44.778Z",
  "userId": "string",
  "pocketId": "string",
  "type": "email",
  "email": "hello@example.com",
  "phone": {
    "number": "string",
    "countryCode": "string"
  },
  "currency": "string",
  "amount": "string",
  "status": "waiting-funds",
  "statusChanges": [
    {
      "newStatus": "waiting-funds",
      "author": "string",
      "created": "2026-02-17T14:25:44.778Z",
      "reason": "string"
    }
  ],
  "senderName": "string",
  "alias": "string",
  "note": "string",
  "walletMovementId": "string"
}
Success

Create order​
Creates a new payment order

Body
required
application/json
amount
Type:string
min length:  
1
max length:  
50
Pattern:^[0-9]*\.?[0-9]*$
required
currency
Type:string
required
Valid currency symbol

pocketId
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
required
type
Type:string
enum
required
email
phone
alias
alias
Type:string
email
Type:string
min length:  
6
max length:  
96
Format:email
note
Type:string
phone
Type:object
Responses
400
Validation error

403
User forbidden to create orders

412
User not valid

Request Example forpost/v1/social-pay/order
curl https://gateway.bit2me.com/v1/social-pay/order \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "pocketId": "",
  "type": "email",
  "email": "",
  "phone": {
    "number": "",
    "countryCode": ""
  },
  "alias": "",
  "amount": "",
  "currency": "BTC",
  "note": ""
}'
{
  "orderId": "string",
  "createdAt": "2026-02-17T14:25:44.778Z",
  "expiryDate": "2026-02-17T14:25:44.778Z",
  "userId": "string",
  "pocketId": "string",
  "type": "email",
  "email": "hello@example.com",
  "phone": {
    "number": "string",
    "countryCode": "string"
  },
  "currency": "string",
  "amount": "string",
  "status": "waiting-funds",
  "statusChanges": [
    {
      "newStatus": "waiting-funds",
      "author": "string",
      "created": "2026-02-17T14:25:44.778Z",
      "reason": "string"
    }
  ],
  "senderName": "string",
  "alias": "string",
  "note": "string",
  "walletMovementId": "string"
}
Success

Claim order​
Claim user pay orders

Body
required
application/json
Type:array object[]
Responses
400
Validation error

403
User forbidden to claim orders

412
User not valid

Request Example forpost/v1/social-pay/order/claim
curl https://gateway.bit2me.com/v1/social-pay/order/claim \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '[
  {
    "pocketId": "",
    "orderId": ""
  }
]'
{
  "result": true
}
Success

Earn ​
EarnOperations
post
/v1/earn/movements
get
/v2/earn/wallets
get
/v1/earn/wallets/{walletId}
get
/v1/earn/wallets/{walletId}/movements
get
/v1/earn/summary
get
/v1/earn/movements/{type}/summary
get
/v2/earn/assets
get
/v2/earn/apy
get
/v1/earn/wallets/rewards/config
get
/v1/earn/wallets/{walletId}/rewards/config
patch
/v1/earn/wallets/{walletId}/rewards/config
get
/v1/earn/wallets/{walletId}/rewards/summary
Create earn deposit/withdrawal​
Create a withdraw or deposit movement in Earn

Body
required
application/json
The details to create the movement

amount
Type:string
min length:  
1
max length:  
50
Pattern:^[0-9]*\.?[0-9]*$
required
currency
Type:string
required
Valid currency symbol

type
Type:string
enum
required
deposit
withdrawal
lockPeriod
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
termsAndConditions
Type:string
Pattern:^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
withholdingAmount
Type:string
min length:  
1
max length:  
50
Pattern:^[0-9]*\.?[0-9]*$
Responses
Request Example forpost/v1/earn/movements
# Create deposit for subaccount
curl -X POST ${SERVER_URL}/v1/earn/movements
  -H 'Content-type: application/json'
  -H 'X-API-KEY: <api key>'
  -H 'X-SUBACCOUNT-ID: <subaccount id>'
  -d '
    {
      "currency":"BTC",
      "amount":"1",
      "type":"deposit"
    }'

{
  "walletMovementId": "70b89183-c7fa-4460-91ce-34d53d739868",
  "movementId": "70b89183-c7fa-4460-91ce-34d53d739868"
}
Success

List earn wallets​
Get a list of earn wallets

Query Parameters
userCurrency
Type:string
Currency to show convertedBalance

sortBy
Type:string
enum
Sorting field

currency
balance
sortDirection
Type:string
enum
Sorting direction

ascending
descending
offset
Type:integer
default: 
0
Integer numbers.

limit
Type:integer
default: 
0
Integer numbers.

Responses
Request Example forget/v2/earn/wallets
curl https://gateway.bit2me.com/v2/earn/wallets \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "total": 1,
    "data": [
      {
        "walletId": "string",
        "userId": "string",
        "currency": "string",
        "balance": "string",
        "lockPeriod": {
          "lockPeriodId": "string",
          "months": 1
        },
        "convertedBalance": {
          "value": "string",
          "currency": "string"
        },
        "createdAt": "2026-02-17T14:25:44.778Z",
        "updatedAt": "2026-02-17T14:25:44.778Z"
      }
    ]
  }
]
Success

Get earn wallet by id​
Retrieves full information of selected wallet

Path Parameters
walletId
Type:string
required
Wallet identifier

Query Parameters
userCurrency
Type:string
Currency to show convertedBalance

Responses
Request Example forget/v1/earn/wallets/{walletId}
curl 'https://gateway.bit2me.com/v1/earn/wallets/{walletId}' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "total": 1,
    "data": [
      {
        "walletId": "string",
        "userId": "string",
        "currency": "string",
        "balance": "string",
        "lockPeriod": {
          "lockPeriodId": "string",
          "months": 1
        },
        "convertedBalance": {
          "value": "string",
          "currency": "string"
        },
        "createdAt": "2026-02-17T14:25:44.778Z",
        "updatedAt": "2026-02-17T14:25:44.778Z"
      }
    ]
  }
]
Success

List earn wallet movements​
Retrieves list of wallet movements.

Movements can be paginated using offset and limit parameters. For example, to get the third page and show 20 registers per page you would use the following query:

/v1/earn/wallets/{walletId}/movements?offset=40&limit=20
Path Parameters
walletId
Type:string
required
Wallet identifier

Query Parameters
userCurrency
Type:string
Currency to show convertedAmount

offset
Type:integer
min:  
0
default: 
0
Specify the number of entries to be skipped (0 by default)

limit
Type:integer
min:  
1
max:  
100
default: 
20
Specify the maximum number of entries to be returned (20 by default)

sortBy
enum
const:  
createdAt
Sorting field

createdAt
sortDirection
Type:string
enum
Sorting direction

ascending
descending
Responses
Request Example forget/v1/earn/wallets/{walletId}/movements
curl 'https://gateway.bit2me.com/v1/earn/wallets/{walletId}/movements' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "total": 1,
    "data": [
      {
        "movementId": "string",
        "userId": "string",
        "type": "deposit",
        "createdAt": "2026-02-17T14:25:44.778Z",
        "walletId": "string",
        "amount": {
          "value": "string",
          "currency": "string"
        },
        "rate": {
          "amount": {
            "value": "string",
            "currency": "string"
          },
          "pair": "string"
        },
        "convertedAmount": {
          "value": "string",
          "currency": "string"
        },
        "source": {
          "walletId": "string",
          "currency": "string"
        },
        "issuer": {
          "service": "string",
          "id": "string"
        }
      }
    ]
  }
]
Success

Get user summary​
Retrieves user summary

Query Parameters
userCurrency
Type:string
Currency to show balance

Responses
Request Example forget/v1/earn/summary
curl https://gateway.bit2me.com/v1/earn/summary \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  [
    {
      "currency": "string",
      "totalBalance": "string",
      "totalRewards": "string"
    }
  ]
]
Success

Get summary by operation​
Retrieves summary of movements per operation (deposit, reward, withdrawal)

Path Parameters
type
Type:string
enum
required
Operation type

deposit
reward
withdrawal
Query Parameters
userCurrency
Type:string
Currency to show balance

rateMoment
Type:string
enum
default: 
"current"
required
Rate moment

creation
current
order
Type:string
enum
default: 
"desc"
required
Sorting direction

desc
asc
Responses
Request Example forget/v1/earn/movements/{type}/summary
curl 'https://gateway.bit2me.com/v1/earn/movements/deposit/summary?rateMoment=current&order=desc' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  [
    {
      "type": "string",
      "currency": "string",
      "total": "string",
      "converted": {
        "amount": "string",
        "currency": "string"
      }
    }
  ]
]
Operation summary

List supported assets​
Retrieves full list of supported assets in earn service

Query Parameters
type
Type:string
enum
Asset type

partner
farming-pool
Responses
401
Unauthorized

Request Example forget/v2/earn/assets
curl https://gateway.bit2me.com/v2/earn/assets
[
  {
    "currency": "string",
    "disabled": true,
    "isNew": true,
    "currenciesRewardAllowed": [
      {
        "currency": "string",
        "extraYield": 1,
        "type": "daily"
      }
    ],
    "levelExtraYieldType": "space-pool"
  }
]
Returns info of currencies found

Get annual percentage yields by currency​
Get current annual percentage yields by currency. Value of currency is an object wich reward type as a key and annual percentage yield as value

Responses
200
Returns the annual percentage yields found

401
Unauthorized

500
Request Example forget/v2/earn/apy
curl https://gateway.bit2me.com/v2/earn/apy
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

List wallets rewards config​
Retrieves rewards configuration for user wallets

Responses
200
Return rewards settings for user wallets

401
Unauthorized

Request Example forget/v1/earn/wallets/rewards/config
curl https://gateway.bit2me.com/v1/earn/wallets/rewards/config \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Get wallet rewards config​
Retrieves rewards configuration for selected wallet

Path Parameters
walletId
Type:string
required
Wallet identifier

Responses
200
Return reward settings by wallet

401
Unauthorized

Request Example forget/v1/earn/wallets/{walletId}/rewards/config
curl 'https://gateway.bit2me.com/v1/earn/wallets/{walletId}/rewards/config' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Update wallet rewards config​
Update wallet reward configuration for selected wallet

Path Parameters
walletId
Type:string
required
Wallet identifier

Body
required
application/json
rewardCurrency
Type:string
required
Currency to obtain the reward

Responses
200
Returns the result of operation

401
Unauthorized

404
Wallet not found

406
Reward currency is not allowed

Request Example forpatch/v1/earn/wallets/{walletId}/rewards/config
curl 'https://gateway.bit2me.com/v1/earn/wallets/{walletId}/rewards/config' \
  --request PATCH \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN' \
  --data '{
  "rewardCurrency": ""
}'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Get wallet rewards summary​
Retrieves full list of rewards summary for selected wallet

Path Parameters
walletId
Type:string
required
Wallet identifier

Query Parameters
userCurrency
Type:string
Currency to show balance

Responses
200
Wallet's rewards summary

404
Wallet not found

Request Example forget/v1/earn/wallets/{walletId}/rewards/summary
curl 'https://gateway.bit2me.com/v1/earn/wallets/{walletId}/rewards/summary' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "message": "string",
  "error": "string",
  "statusCode": 1,
  "reqId": "string",
  "data": {}
}
Error

Pro (Trading Spot) (Collapsed)​
REST API
The REST API is divided into groups of endpoints dedicated to different functionalities.

Market Data
Trading
Funding
WebSockets Authentication
API keys are required to call any of the account specific (private) API endpoints, such as the trading and funding endpoints. API keys are not required to call the market data endpoints.

You can find different code samples and how to call authorized endpoints in the following GitHub repository.

REST Rate Limits
Users using the REST API have a limit of requests per minute associated with an IP address. This rate limit could be found here.

There are some endpoints with specific rate limits by user account:

Endpoint	Description	Max. RPS (request per second)
POST /v1/trading/order	Create one order	15/sec
DELETE /v1/trading/order/{id}	Delete one order	15/sec
DELETE /v1/trading/order	Delete many orders	1/sec
GET /v1/trading/order	Get orders	5/sec
GET /v1/trading/order/{id}	Get one order	5/sec
GET /v1/trading/trade	Get trades	5/sec
GET /v1/trading/order/{id}/trades	Get trades of one order	5/sec
GET /v1/trading/wallet/balance	Get balance	5/sec
POST /v1/trading/wallet/deposit	Deposit funds from Wallet to Pro	1/sec
POST /v1/trading/wallet/withdraw	Withdraw funds from Pro to Wallet	1/sec
There are some endpoints with specific rate limits by IP address:

Endpoint	Description	Max. RPS (request per second)
GET /v1/trading/candle	Get OHLCV (open, highest, lowest, close, volume) information	5/sec
WebSockets API
The WebSockets API offers real-time information and allows orders management.

The user has to subscribe to channels in order to get real-time information, and the user has to send specific commands to the WebSockets server in order to manage the orders.

Our WebSockets server provides public channels, with information that can subscribe any user, and private channels. To subscribe to the private channels the user must be logged in.

You can find different code samples and how to call authorized endpoints in the following GitHub repository.

WebSockets Rate Limits
Users using the WebSockets API have a limit of messages per second associated with a connection and command. Review the maximum concurrent connection limit and the overall message per second limit at WebSockets Rate Limit section

⚠️ The connection will be aborted if the request limit has been reached. ⚠️

Command	Max. messages per second
Authenticate	1
Subscribe	50
Unsubscribe	50
AddOrder	10
AddOrders (batch orders)	1
CancelOrder	10
CancelOrders (batch orders)	1
CancelAllOrders	1
AutoCancelOrdersOnDisconnection	5
Order Limits
A rate limit applies to the number of orders clients can have open on each market at one time and the number they can add and cancel orders on each market per hour. These limits apply to all API types (Rest API and WebSockets API) and according to the tier established for the user:

User	Purpose	Max. Open Orders by symbol	Max. Created/Cancelled Orders last hour by symbol
Standard	General purpose	20	1000
Advanced	Market makers, High-Frequency Trading	100	Up to 10000
To exceed these limits, contact our support center https://support.bit2me.com/en/support/home

FAQ
Spot API supports one of following order types:

market: will be executed at the best price available in the order book. Runs immediately. The exact price of the operation is not guaranteed.
limit: allows you to buy or sell at a fixed price that you determine, although depending on how the market moves you can get a better price. It is executed when the market price reaches the set price. The order is not guaranteed to be executed
stop-limit: order has to set 2 prices: stop price and limit price. When the market reaches the stop price then the order becomes a limit order.
Orders expire every 30 days - automatically cancelled. For partially filled orders, they will also be canceled after 30 days and the unfilled order quantity is unlocked.

Cancelled market maker orders not partially filled are stored for 7 days. After that period they are automatically deleted from the system.

Errors
Code	Description
AMOUNT_PRECISION_EXCEEDED	The number of decimals in the indicated amount is greater than the maximum supported for this market
BUY_PRICE_IS_ABOVE_INITIAL_PRICE	The indicated buy order price is higher than the initial price determined for this market not yet started
BUY_STOP_PRICE_IS_BELOW_INITIAL_PRICE	The indicated stop buy order price is lower than the initial price determined for this market not yet started
CREATE_ORDERS_DISABLED_TEMPORALLY	Order creation operations are temporarily disabled
CURRENCY_NOT_SUPPORTED	Currency not supported
DELETE_CLOSED_ORDER	The order you are trying to cancel is deleted or completed
DELETE_ORDERS_DISABLED_TEMPORALLY	Order cancellation operations are temporarily disabled
DEPOSITS_DISABLED_TEMPORALLY	Fund deposits are temporarily disabled
ERROR_CREATING_INTERNAL_ORDER	There was an error creating the indicated order
ERROR_CREATING_ORDER	There was an error creating orders
MARKET_CONFIG_NOT_FOUND	The market does not exist or is disabled
MAX_CREATED_ORDERS_REACHED	The maximum number of created orders allowed in the last hour for this market has been reached
MAX_OPEN_ORDERS_REACHED	The maximum number of open orders allowed has been reached
MISSING_FROM_POCKET_ID	The identifier of the wallet from which the funds came from has not been indicated
NOT_ENOUGH_BALANCE	You do not have enough funds
NOT_ENOUGH_LIQUIDITY	There is not enough liquidity in the market
ORDER_AMOUNT_GREATER_MARKET_MAX	The order amount exceeds the maximum allowed for this market
ORDER_AMOUNT_LOWER_EQUAL_ZERO	The order amount must be positive
ORDER_PRICE_LOWER_EQUAL_ZERO	The price of the order must be positive
ORDER_SIZE_LOWER_MARKET_MIN	The order is below minimum size (amount per price) required for the market
PRICE_GREATER_MARKET_MAX	The order price is above maximum allowed for this market
ORDER_STOP_PRICE_LOWER_EQUAL_ZERO	The order stop price must be positive
PRICE_LOWER_MARKET_MIN	The order price is below minimum required for this market
PRICE_PRECISION_EXCEEDED	The number of decimals in price is greater than the maximum allowed for this market
ONLY_LIMIT_ORDERS_ALLOWED	Limit orders are only allowed to be created at this time
ORDER_AMOUNT_GREATER_TOTAL_AMOUNT_IN_PURCHASE	The sell order amount exceeds the total buy liquidity for this market
ORDER_AMOUNT_GREATER_TOTAL_AMOUNT_IN_SALE	The buy order amount exceeds the total sell liquidity for this market
ORDER_AMOUNT_LOWER_MARKET_MIN	The order amount is below minimum required for this market
SELL_PRICE_IS_BELOW_INITIAL_PRICE	The sell order price is below initial price for this market not yet started
SELL_STOP_PRICE_IS_ABOVE_INITIAL_PRICE	The stop sell order price is above initial price for this market not yet started
TIME_IN_FORCE_INVALID	The time in force value is not allowed in this order type
TRADING_WALLET_NOT_BALANCE	Wallet has no balance
TRADING_WALLET_NOT_FOUND	Wallet identifier not found
USER_IS_ALREADY_CREATING_ORDER	The user is creating another order simultaneously
WITHDRAWS_DISABLED_TEMPORALLY	Withdrawals are temporarily disabled
Market ​
MarketOperations
get
/v1/currency/convert
get
/v1/currency/rate
get
/v3/currency/ticker/{symbol}
get
/v3/currency/market-data/{symbol}
get
/v1/currency/prices
get
/v3/currency/chart
get
/v2/currency/assets
get
/v2/currency/assets/{symbol}
get
/v1/currency/ohlca/{symbol}
Currency conversion​
Convert the specified amounts to the specified currency

Query Parameters
from
Type:string
Pattern:^[A-Z0-9]{1,10}(,[A-Z0-9]{1,10})*$
required
Comma delimited list of base currencies (can be just one in order to use the same currency base for all convertions)

to
Type:string
Pattern:^[A-Z0-9]{1,10}(,[A-Z0-9]{1,10})*$
required
The target currency

value
Type:string
Pattern:^-?\d+(?:\.\d+)?(?:,-?\d+(?:\.\d+)?)*$
required
Comma delimited list of values (number of values must be equal to number of times)

time
Type:string
Pattern:^((([0-9]{4}-[0-9]{1,2}-[0-9]{1,2}T[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{1,3}Z)|([0-9]{13})),?)+$
required
Comma delimited list of times (ISO 8601 or epoch) (number of times must be equal to number of values)

Responses
Request Example forget/v1/currency/convert
curl 'https://gateway.bit2me.com/v1/currency/convert?from=&to=&value=&time=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  0.111
]
Success

Currencies rates​
Returns all supported exchange rates in USD

Query Parameters
type
Type:string
enum
Currency type

all
fiat
crypto
time
Type:string
max length:  
1024
Pattern:^((([0-9]{4}-[0-9]{1,2}-[0-9]{1,2}T[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{1,3}Z)|([0-9]{13})),?)+$
required
Comma delimited list of times (ISO 8601 or epoch). If this parameter is not specifed, the current time is used

Responses
Request Example forget/v1/currency/rate
curl 'https://gateway.bit2me.com/v1/currency/rate?time=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "fiat": {},
    "crypto": {}
  }
]
Success

Cryptocurrency data​
Returns the data of given cryptocurrency in the selected currency

Path Parameters
symbol
Type:string
Pattern:^[A-Z]{3}$
required
Query Parameters
rateCurrency
Type:string
Pattern:^[A-Z]{3}$
interval
Type:array[string]
enum
Period of time for consultation

one_hour
one_day
one_week
one_month
one_year
extended
Type:boolean
default: 
true
Flag to include market data

Responses
Request Example forget/v3/currency/ticker/{symbol}
curl 'https://gateway.bit2me.com/v3/currency/ticker/{symbol}' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "currency": {
    "cryptoCurrency": [
      {
        "time": 1,
        "interval": "string",
        "price": "string",
        "marketCap": "string",
        "totalVolume": "string",
        "fullyDilutedMarketCap": "string",
        "maxSupply": "string",
        "totalSupply": "string"
      }
    ]
  }
}
Success

Market data​
Returns the market data for given currency in USD

Path Parameters
symbol
Type:string
required
Currency to fetch market data for

Responses
Request Example forget/v3/currency/market-data/{symbol}
curl 'https://gateway.bit2me.com/v3/currency/market-data/{symbol}' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "marketCap": "1156846107704",
  "totalVolume": "28457174871",
  "fullyDilutedMarketCap": "1229760916272",
  "maxSupply": 21000000,
  "totalSupply": 21000000
}
Success

Currency price​
Returns the price of cryptocurrencies in the selected currency for any number of intervals, always returning the current rate

Query Parameters
currency
Type:string
Pattern:^[A-Z]{3}$
interval
Type:array[string]
enum
Period of time for consultation

one_hour
one_day
one_week
one_month
one_year
Responses
Request Example forget/v1/currency/prices
curl https://gateway.bit2me.com/v1/currency/prices \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "time": 1738164880678,
  "interval": "one_day",
  "price": "58217.00000000000610707973"
}
Success

Currency chart​
Returns historic price chart of given ticker

Query Parameters
ticker
Type:string
Pattern:^[\w\d]{1,}/[\w\d]{1,}$
required
Ticker container both currencies. Example BTC/EUR

temporality
Type:array[string]
enum
Temporality of the chart

one-hour
four-hours
twelve-hours
one-day
one-week
Responses
Request Example forget/v3/currency/chart
curl 'https://gateway.bit2me.com/v3/currency/chart?ticker=' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  [
    1712497400000,
    0.0933,
    0.9855
  ],
  [
    1712498400000,
    0.9222,
    0.9856
  ],
  [
    1712499400000,
    0.9222,
    null
  ]
]
Success

Get all assets​
Return all assets

Query Parameters
includeTestnet
Type:boolean
Includes assets from currencies from Testnets

showExchange
Type:boolean
Includes exchange property on assets

Responses
Request Example forget/v2/currency/assets
curl https://gateway.bit2me.com/v2/currency/assets \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "symbol": {
    "symbol": "string",
    "name": "string",
    "slug": "string",
    "mainwebUri": "string",
    "uriScheme": "string",
    "hexColor": "string",
    "assetType": "string",
    "exponent": 0,
    "unitPriceScale": 0,
    "transactionUnitPriceScale": 0,
    "addressRegex": "string",
    "hasImage": true,
    "hasPaymentRequest": true,
    "isERC20Token": true,
    "enabled": true,
    "lite": true,
    "exchange": "string",
    "pairsWith": [
      "string"
    ]
  }
}
Success

Get one asset​
Return an asset by symbol

Path Parameters
symbol
Type:string
required
Symbol ID

Query Parameters
showExchange
Type:boolean
Includes exchange property on assets

Responses
Request Example forget/v2/currency/assets/{symbol}
curl 'https://gateway.bit2me.com/v2/currency/assets/{symbol}' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "symbol": "string",
  "name": "string",
  "slug": "string",
  "mainwebUri": "string",
  "uriScheme": "string",
  "hexColor": "string",
  "assetType": "string",
  "exponent": 0,
  "unitPriceScale": 0,
  "transactionUnitPriceScale": 0,
  "addressRegex": "string",
  "hasImage": true,
  "hasPaymentRequest": true,
  "isERC20Token": true,
  "enabled": true,
  "lite": true,
  "exchange": "string",
  "pairsWith": [
    "string"
  ]
}
Success

Get OHLCA for a currency​
Returns OHLCA for the given symbol

Path Parameters
symbol
Type:string
Pattern:^[A-Z]{3}$
required
Query Parameters
time
Type:date-time
Datetime (ISO format)

timeframe
Type:string
enum
required
Timeframe

1H
4H
12H
1D
1W
1M
1Y
Responses
Request Example forget/v1/currency/ohlca/{symbol}
curl 'https://gateway.bit2me.com/v1/currency/ohlca/{symbol}?timeframe=1H' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
{
  "open": "string",
  "high": "string",
  "low": "string",
  "close": "string",
  "average": "string"
}
Success

Loan (Collapsed)​
LoanOperations
get
/v1/loan/ltv
get
/v2/loan/currency/configuration
get
/v1/loan/movements
get
/v1/loan/orders
post
/v1/loan/orders
get
/v1/loan/orders/{orderId}
post
/v1/loan/orders/{orderId}/guarantee/increase
post
/v1/loan/orders/{orderId}/payback
Misc ​
MiscOperations
get
/v1/misc/country/{countryISOCode}/region
Get country regions​
Get country regions

Path Parameters
countryISOCode
Type:string
Pattern:^[A-Z]{2}$
required
Query Parameters
langCode
Type:string
enum
Language fo localize country names

EN
ES
Responses
Request Example forget/v1/misc/country/{countryISOCode}/region
curl 'https://gateway.bit2me.com/v1/misc/country/{countryISOCode}/region' \
  --header 'X-API-KEY: YOUR_SECRET_TOKEN'
[
  {
    "iso": "string",
    "iso3": "string",
    "name": "string",
    "fips": "string"
  }
]
Success

Models