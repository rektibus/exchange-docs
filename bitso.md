rading API: Overview
Learn about the business value of the API and how it can help you enhance your business.

Welcome to Bitso's Trading API documentation, a RESTful API that exposes Bitso's Digital and Fiat Currency Trading platform. We are excited you are here! 💛

Bitso's Trading API enables you to integrate the Bitso trading platform with third-party solutions, such as trading applications, charting programs, point-of-sale systems, and many more. The API is easy to use, and integrating it into your solutions is a short-lived and trouble-free effort.

The Trading API provides a set of four public endpoints to retrieve information such as available exchange order books and data from a specified book: trading information, open orders, and recent trades.

The service also comprises a set of private endpoints that enable you to manage your orders and your Bitso account. All of the requests to these private endpoints must be signed and require API Keys. For further details on how to get your API Keys and create signed requests, see the sections, Set Up Your Testing Environment and Authentication.

This guide documents all the details on how the service works, its onboarding requirements, and the error messages it might throw. You will be up and running in a jiffy! 🚀


History of Changes
2025-08-22
Introduced slippage_tolerance optional parameter to the Place an Order page to allow users to set their preferred slippage tolerance percentage. Not providing the parameter will disable slippage protection.

2025-05-27
Order origin_id uniqueness is now scoped to active orders. This update simplifies the order management process by removing the prior requirement for unique origin_id across all active and traded orders.

2025-04-14
Added instructions to the Place an Order article for configuring the minor and major parameters when using the POST /orders endpoint for Limit and Market Orders, providing clearer guidance for order placement.

2025-03-14
Introduced Nonce v2 for enhanced request reliability and security, reducing rejected valid requests for high-traffic users.

2025-03-12
In the article 17: Validation Errors - Part 2, added error messages 1700-1707.

Added a new number sequence to the list of error codes: 17: Validation Errors - Part 2

Renamed 03: Validation Errors to 03: Validation Errors - Part 1.

2025-03-07
In the article 03: Validation Errors, added the following error message:

0382: Third-party withdrawals are blocked
2025-02-28
In the article 03: Validation Errors, added the following error message:

0381: Contact not found
2025-02-12
The title of the article Update an Order changed to Replace an Order. It documents the former version (v3) of the PATCH /orders/ method.

2025-02-12
Released a new version (v4) of the method PATCH /orders/. The article Modify an Order explains the updates:

Changed the definition of the needed available balance.
Eliminated the constraint related to the parameter origin_id.
Eliminated origin_id from the body parameters.
Introduced a new body parameter, cancel.
2025-01-08
The supported character set of the parameter origin_id added the dash character, -. This change was propagated to the articles that explain the order- and trade-related endpoints that use the parameter.

2024-12-16
Formerly, error code 0343: Incorrect amount was shared with another error status. To improve clarity, the team introduced a specific error message, 0379: Insufficient balance, detailed in article 03: Validation Errors.

2024-12-05
In the article 02: Authentication Errors, added the following error message:

0216: Your account has been restricted; please get in touch with your contact at Bitso
Users with a PTS line might get this message, and their contact is a member of the Market Maker support team.
2024-10-07
Added the article Understand Bitso's Auth Mechanism.

2024-10-04
The endpoint Update an Order was released.

2024-09-26
In the article 07: Account Errors, added the following error messages:

0729: Error saving external bank account
0730: Invalid external bank account
0731: Error getting external bank account list
0732: Error getting external bank account
2024-09-18
The method GET /api/v4/currency_conversions/{conversion_id}\ added a fourth possible state: queued.

2024-09-04
In the article Trades Channel, the table explaining the returned payload had the t entry incorrectly labeled as Maker side. It was changed to Trader side. The t stands for trader.

2024-04-11
In the article 02: Authentication Errors, added error code 0215: Incorrect request signature.

2023-05-09
In the article 02: Authentication Errors, added error code 0214: Invalid reCAPTCHA.

2023-04-10
In the article 03: Validation Errors, added the following error messages:

0377: Order matched, but trade records still being processed
0378: Order has not been matched yet
2023-04-10
Added the following information to the documentation of the WebSocket API to align with the code:

In the General article, the section Fields Included in Messages.
In the Trades Channel, Orders Channel, and Diff-Orders Channel articles, the field sent to the example message.
2023-04-05
In the endpoint balance, the following updates were made to align with the code:

Added the next fields to the response-body table and sample response:
pending_deposit
pending_withdrawal
Updated the endpoint's URL so that it points to sandbox.
2023-03-29
Added the following information to the documentation of the Websocket API to align with the code:

Trades section:
Addition of the field x to the table.
Modification of the server messages payload to show field added.
Diff-Orders section:
Addition of the field z to the table.
Modification of the server messages payload of cancelled orders to show field added.
2023-03-16
In the endpoint open_orders, the following updates were made to align with the code:

Added the next fields to the response-body table and sample response:
origin_id
time_in_force
Added the query parameter source.
Updated the endpoint's URL so that it points to sandbox.
2023-03-16
In the endpoint order_trades, the following updates were made to align with the code:

Added the next fields to the response-body table and sample response:
minor_currency
major_currency
Changed the type of the tid field from long to string.
Updated the endpoint's URL so that it points to sandbox.
2023-03-16
In the endpoint /fees/, the following updates were made to align with the code:

Added the next fields to the response-body table and sample response:
volume_currency
current_volume
next_volume
next_maker_fee_percent
next_taker_fee_percent
nextVolume
nextFee
nextTakerFee
deposit_fees
Updated the endpoint's URL so that it points to sandbox.
2023-03-14
Updated the URL of the endpoint /orders/ so that it points to sandbox.

2023-03-14
In the endpoint user_trades, the following updates were made to align with the code:

Added the next fields to the response-body table and sample response:
minor_currency
major_currency
Changed the type of the tid field from long to string.
Updated the endpoint's URL so that it points to sandbox.
2023-03-10
In the endpoint available_books, the following changes were made to align with the code:

Added the next fields to the response-body table and sample response:
default_chart
fees
tick_size
Updated the endpoint's URL so that it points to sandbox.
2023-03-10
In the endpoint /ticker/ the following changes were made to align with the code:

Added the next fields to the response-body table and sample response:
change_24
rolling_average_change
Updated the endpoint's URL so that it points to sandbox.
2023-03-10
Added the documentation of the /currency_conversions/ endpoint, responsible for requesting and executing quotes:

POST /api/v3/currency_conversions: Request a conversion quote

PUT /api/v3/currency_conversions/{quoteId}: Execute a conversion quote

GET /api/v3/currency_conversions/{quoteId}: Retrieve the details of a conversion quote

2023-03-03
Added the following information to the documentation of the Websocket API to align with the code:

General section:
Was: Remove it, in which case it does not have an a field (amount).
Changed to: Cancel it, in which case it does not have the fields a (amount) and v (value).
Trades section:
Addition of the fields mo, to, and t to the payload of the server messages.
Diff-Orders section:
Addition of the field s to the table.
Modification of the server messages payload of open orders to show field added.
Addition of a sample payload for cancelled orders.
Orders section:
Addition of the fields o and s to the table.
Modification of the server messages payload to show fields added.
2023-03-02
The article Diff-Orders Channel incorrectly documented the t field as follows:

0 indicates sell
1 indicates buy
The code has it the other way around. Docs were aligned with the code.

2022-08-18
Added a new error code, '0506'.
Added documentation for the new withdrawal endpoints.
Added documentation for the new withdrawal methods endpoints.
Deprecated the Crypto withdrawal endpoints.
Deprecated the SPEI withdrawal endpoints.
2022-03-10
Added new error codes, '0414' - '0417'.
2022-01-18
Added new error codes to indicate when trading or conversions are disabled on your account.
2021-11-24
Fixed a documentation inconsistency between the REST API service and the implementation:
In the open_orders service, the request parameters were wrong; presently, the parameters are book and currency as defined in the service implementation.
2021-09-27
Updated the URL in General > Developer Testing Server to point to the newly configured sandbox environment.
2021-07-27
Fixed a documentation inconsistency between the REST API service and the implementation:
In the open_orders and lookup_orders services, the status response object field now lists the possible value partially filled instead of partial-fill.
2021-07-19
Fixed a documentation inconsistency between the REST API service and the implementation:
In the user_trades service, the parameter book changed to non-required.
2021-06-25
An inconsistency existed in the documentation of the Diff-Orders and Orders channels. It described the t field as number 0 for selling and 1 for buying, but the correct implementation is the opposite. To make the documentation consistent with the implementation, we updated the field to number 0 for buying and 1 for selling. This update was for documentation only; nothing changed on the consumer side.
2021-06-24
Fixed documentation inconsistencies between the REST API service and the implementation:
In the order_trades service, the response object field make_side changed to maker_side.
In this same service, we upgraded the created_at field format from 2021-06-11T09:25:05+0000 to 2021-06-11T09:25:05.000+00:00.
2020-08-21
Deleted some old API errors from v2 and migrated to v3 errors in some cases:
20 to 0301: Unknown Order book, if book is not valid
22 to 0408: Incorrect amount value, it must be a non-zero positive value
0410 is documented now: Trading not enabled
0411 is documented now: Trading not enabled for market orders
22 to 0302: Incorrect time frame (not ‘hour’ or 'minute’), when the time_in_force parameter is not valid
22 to 0407: Invalid precision, when price parameter is not present
22 to 0407: Invalid precision, when tick_size is not valid
20 to 0201: Invalid Nonce or Invalid Credentials when user_id isn't present
2020-06-10
Added the ability to query a withdrawal by its origin ID:
GET /v3/withdrawals?origin_ids={origin_id},{origin_id},{origin_id}
2020-06-09
Deprecated the endpoint /v3/{api_method}/client_id/{client_id}:
GET /v3/order_trades/client_id/{client_id}
GET /v3/orders/client_id/{client_id}-{client_id}-{client_id}/
DELETE /v3/orders/client_id/{client_id}-{client_id}-{client_id}/


Set Up Your Testing Environment
Learn how to set up your account, API credentials, and account funds.

When working on integrations, use our testing environment to verify your code before running it on production.

Do not perform testing on the production environment.

You require creating first a personal or business account in the testing environment. Later, you will need to create an account again in production. You need to generate API credentials in both accounts and use them according to the environment where you are executing your code.

The production URL is like the one of the testing environment; it only eliminates the word stage or sandbox.

For example,

Testing Environment: https://stage.bitso.com/api/v3/withdrawals
Production Environment: https://bitso.com/api/v3/withdrawals


Create Signed Requests
Dive into the implementation details of Bitso's HMAC signature.

To authenticate in any of the API endpoints, all of your HTTP requests must be valid JSON objects and include the following three fields in the Authorization header payload:

key: The API Key that you generated. See the section, Set Up Your Testing Environment.
nonce: An integer that must be unique and increase with each API call. Bitso recommends using a Unix timestamp.
signature: A Hash-based Message Authentication Code (HMAC). For further details, refer to the next section, Build Your Signature.
Build Your Signature
To generate a signature for an HTTP request, you must create a hash-based message authentication code (HMAC) that uses the hash function SHA-256.

To create an SHA-256 HMAC, use your generated Bitso API Secret as the cryptographic key on the concatenation of:


                  nonce  +  HTTP method  +  request path  +  JSON payload
Do not include the plus signs, +, in the concatenated string. Hex encode the obtained output.

Ensure the following is true when creating the signature:

The nonce value is the same as the nonce field in the Authorization header.
The request path and JSON payload values are precisely the same as those used in the request.
Authentication Header
Construct the authentication header using the fields outlined at the beginning of this article. The header format is as follows:

Auth_Header: Bitso `key`:`nonce`:`signature`

Replace `key`, `nonce`, and `signature` with the appropriate values as described earlier.

Examples
The shell script on the left tab below exemplifies a signed HTTP GET request to the /balance/ endpoint. Ensure to replace the values of the variables API_KEY and API_SECRET with the ones you generated.

The right tab exemplifies a pre-request script that builds the authentication header in JavaScript for the Postman API testing platform. Ensure to create the environment variables api-key and api-secret and assign them your Bitso credentials.

Add new API Key
Shell Signed Request
Auth Header Pre-Request Script

#!/bin/bash
# requires:
# -httpie: https://github.com/jkbrzt/httpie

URL="https://stage.bitso.com/api/v3/balance/"
#Use your Bitso credentials
API_KEY="vToM******"
API_SECRET="*****197c28f2b782ed5ae**********"
SECS=$(date +%s)
DNONCE=$(expr 1000 '*' "$SECS")
HTTPmethod=GET
JSONPayload=""
RequestPath="/api/v3/balance/"
SIGNATURE=$(echo -n $DNONCE$HTTPmethod$RequestPath$JSONPayload | openssl dgst -binary -sha256 -hmac $API_SECRET | xxd -p -c 256 )
AUTH_HEADER="Bitso $API_KEY:$DNONCE:$SIGNATURE"
http GET $URL Authorization:"$AUTH_HEADER"



Nonce v2 Rollout
We have introduced Nonce v2, an improved version of the nonce parameter included in the Auth header payload.

Why Nonce v2?
We're improving how we protect your requests to enhance security and efficiency. Nonce v1 worked well, but users sending many requests —like our high-traffic power users— sometimes experienced valid actions being flagged as suspicious. That's not ideal. Nonce v2 resolves this issue, ensuring a smoother experience while maintaining rock-solid security.

What does Nonce v2 improve?
Here's why you will love the change:

Fewer Rejected Requests: Valid requests won't be blocked just because they arrive out of order—ideal for users sending multiple calls.
Top-Notch Security: It still prevents replay attacks (those sneaky repeat attempts), keeping your account safe.
Smoother Workflow: It handles real-world usage efficiently, whether sending one request or a hundred.
Nonce v2 focuses on reliability and flexibility, adapting to how you use our APIs.

How does it affect me?
The transition to Nonce v2 is straightforward. Simply update how you generate nonce values (explained further down). Once updated, you will seamlessly be using Nonce v2, a more reliable mechanism with the same strong protection.

How can I use Nonce v2?
The same header currently supporting Nonce v1 will also support Nonce v2. To integrate with the improved validation process, send nonce values with the Nonce v2 format. For details, refer to the provided examples.

When can I start using Nonce v2?
Right now.

What does Nonce v2 look like?
Nonce v2 is a number between 14 and 19 digits, formed by concatenating:

A 13-digit Epoch timestamp in milliseconds (for example, 1731349200123 for March 11, 2025, 12:00:00.123 UTC).
A random salt (1 to 6 digits, for example, 123456).
Examples:
19 digits: 1731349200123123456 (timestamp 1731349200123 + salt 123456)
18 digits: 173134920012378901 (timestamp 1731349200123 + salt 78901)
16 digits: 1731349200123999 (timestamp 1731349200123 + salt 999)
Bitso recommends a 6-digit salt for maximum entropy.

Will Nonce v1 be deprecated?
Yes, we will deprecate Nonce v1 in November 2025. After this date, the service will reject all Nonce v1 validations, so be sure to switch to Nonce v2 before then.

Examples of Nonce v2 Generation
Below are examples in various programming languages demonstrating how to generate a Nonce v2 value according to the specification (13-digit Epoch timestamp in milliseconds + up to 6-digit random salt).

Each example includes comments explaining the process and an example output.

Java
JavaScript
Python
C++

import java.time.Instant;

public class NonceV2Generator {
    public static String generateNonceV2() {
        // Get current timestamp in milliseconds (13 digits)
        long timestamp = Instant.now().toEpochMilli();
      
        // Generate random salt (up to 6 digits, here using 6 digits for consistency)
        int salt = (int) (Math.random() * 900000) + 100000; // Range: 100000-999999
      
        // Concatenate timestamp and salt
        return String.format("%d%d", timestamp, salt);
    }
  
    public static void main(String[] args) {
        System.out.println("Nonce v2 Example: " + generateNonceV2());
    }
}

// Example Output: 1731349200123456789  
// (Timestamp: 1731349200123, Salt: 456789)


Understand Bitso's Auth Mechanism
How Bitso's HMAC signature helps prevent malicious attacks.

Client-server interactions are prone to cyberattacks that can compromise the data exchanged. Let's understand two common attacks that can occur:

Man-in-the-Middle (MITM) Attack: The attacker secretly intercepts and potentially alters the communication between two parties who believe they are directly communicating. The attacker positions themselves between the two parties (for instance, an API consumer and a web server) and can eavesdrop on, modify, or even inject malicious content into the exchanged data.
Replay Attack: The attacker intercepts valid data transmissions (for instance, login credentials or authentication tokens) and maliciously retransmits them (or "replays" them) to trick the system into granting unauthorized access or executing a fraudulent transaction. The key aspect of a replay attack is that the attacker does not need to decrypt or alter the data—they simply capture and resend it.
How Nonces Help Prevent Replay Attacks
A nonce—short for 'number used once'—is a unique, one-time-use value the client generates for each request. It thwarts replay attacks by ensuring each message is unique, even if the same request is made multiple times.

When a client sends a request to a server, it includes the nonce in the request. The server checks the nonce's uniqueness against its temporary store of nonces; if it finds the nonce is new, it processes the request. Otherwise, it rejects the request, preventing the replay attack.

When we combine a nonce with a form of sequence number or timestamp, for example, our implementation asks for it to increase with each request, a message is not only unique but also time-sensitive.

How HMAC Helps Prevent MITM Attacks
Hash-based Authentication Codes (HMAC)—a cryptographic mechanism—helps prevent MITM attacks by ensuring the authenticity and integrity of the message being transmitted between two parties.

HMAC uses a shared secret key known only to the sender and the receiver. When sending a message, the sender computes the HMAC using the message and the secret key and transmits both the message and the HMAC.

The receiver, who also knows the secret key, recomputes the HMAC using the received message and compares it to the HMAC sent by the sender. If they match, it proves the message came from a legitimate sender (authentication) and was not tampered with (integrity). A discrepancy immediately exposes a tampering attempt and alerts the receiver to reject the message.

An attacker in the middle cannot forge a valid HMAC without knowing the secret key, preventing them from impersonating the sender. They only see the message and the resulting HMAC. Without the secret key, the attacker cannot reverse-engineer the HMAC to alter the message or generate new valid HMACs for fraudulent messages.

How HMAC and Nonces Work Together
HMAC alone does not protect against replay attacks. However, combined with a nonce, it becomes a highly effective way to prevent MITM and replay attacks. Merging both schemes ensures that each message is authentic, untampered, and unique. It works in the following way:

HMAC for Message Integrity and Authentication: Only the sender and receiver can compute the correct HMAC because they share the secret key, which ensures the authenticity of the sender and the message's integrity during transmission. However, an attacker could still capture a legitimate message and resend it with the same HMAC.
Nonce for Uniqueness and Freshness: The addition of a nonce to each request makes them unique. If a message is captured and replayed, it won't be accepted because the server detects the nonce reuse, preventing replay attacks.
Step-by-Step Process:
Client Sends Request with Nonce:
The client generates a nonce.
The client appends the nonce to the message.
The client computes the HMAC using the message, nonce, and a shared secret key.
The message, nonce, and HMAC are sent to the server.
Server Validates the Request:
Upon receiving the message, the server verifies whether the nonce has been used before.
If the nonce is new and valid, the server accepts the request.
Otherwise, the server rejects it as a replay attempt.
The server recomputes the HMAC using the received message, nonce, and shared secret key.
If the HMACs match, the server confirms the authenticity and integrity of the message.
If they don't match, the server rejects the message as an MITM attack.
How HMAC Drawbacks are Subdued
Despite HMAC's strengths in securing message integrity and authentication, it has limitations and potential drawbacks, which we can summarize as follows:

Key management: HMAC requires a shared secret key between the sender and receiver, posing challenges in securing key distribution and management.
No confidentiality: HMAC only ensures integrity and authentication, not encryption. The message itself is not encrypted, meaning an attacker could still read the content even if they can't modify it. HMAC must be combined with encryption algorithms if confidentiality is required.
Vulnerability to brute force and key exposure: If a weak key is chosen, for example, a short or easily guessable key, the HMAC can be vulnerable to brute force attacks where an attacker tries different keys until they find the correct one. It is also susceptible to key exposure. If the secret key is leaked or compromised in any way, HMAC becomes entirely insecure because an attacker with the key can forge valid HMACs.
Hash function dependence: Security risks exist when the implementation uses weak or compromised hash functions. HMAC is only as strong as the underlying hash function. If the hash function is compromised, then the HMAC can be vulnerable to collision attacks.
Performance overhead: Computational and performance costs can be a consideration in high-throughput or resource-limited environments. While HMAC is computationally efficient, it still adds overhead due to the hashing process. HMAC internally hashes the message twice—once with an inner key and once with an outer key. This double hashing makes it more secure but also more resource-intensive compared to single-hash algorithms.
Lack of native replay attack protection: HMAC alone does not prevent replay attacks. Mitigating these attacks requires additional mechanisms to prevent message resending.
However, when we combine HMAC with proper practices such as secure key management, the addition of nonces, robust hash functions, and long enough strong keys, HMAC remains a robust, trustable method for message integrity and authentication.

Summary
HMAC prevents MITM attacks by providing authentication (ensuring the message comes from a legitimate sender) and integrity (detecting any changes to the message). It makes it impossible for an attacker to forge or modify messages without knowing the secret key. When combined with nonces the uniqueness of each message can be guaranteed, preventing the replay of previous valid messages. Together, they provide a robust defense against attackers trying to intercept or replay valid messages.



General
This article caters to basic information about the API's implementation.

Bitso’s APIs conform to the principles and constraints of the REST architectural style. They rely on the HTTP client-server protocol to fetch resources and have predictable, resource-oriented URLs. The requests and responses are JSON-encoded exclusively, including error responses, and they use traditional HTTP methods to perform actions for a given resource.

HTTP API Responses
Successful API calls return the following JSON response object:

Successful response

{ "success": true, "payload": {RELEVANT_DATA_HERE} }
Whereas, unsuccessful calls return the JSON response object that follows:

Unsuccessful response

{ "success": false, "error": {"message": ERROR_MESSAGE, "code": ERROR_CODE} }
Number Precision
Responses return decimal numbers as strings to preserve full precision across platforms. Bitso recommends converting your numbers to type string to avoid undesired consequences derived from precision and truncation errors.

Rate Limits
Bitso's APIs establish rate limits based on one-minute windows. The limit for public API requests (no need for authentication) is by IP address, which allows 60 requests per minute (RPM). While the limit is by user account for private API requests, allowing 300 RPM. However, you need to be a verified user to have a 300-RPM limit, and a verified user means the account has fully completed the KYC process.

If you exceed these limits, then the system locks you out for one minute. Continuous one-minute lockouts might result in a 24-hour block. Order cancellations are not subject to API rate limiting.

📘
Custom Limits
Contact developers@bitso.com for more information on custom API rate limits for your account.

Notation
Our documentation uses the following terminology:

Major: Denotes the primary currency in the trade, usually the base currency (the first currency in the pair). It represents the quantity being bought or sold.
Minor: Denotes the secondary currency, usually the quote currency (the second currency in the pair). It represents the equivalent value in the base currency.
Major_Minor: It is how our APIs always refer to an order book, for instance, btc_mxn.
Example
Let's take the MXN/Digital Dollars (USDC) currency pair as an example:

If you buy 5,000 MXN/USDC, the amounts break down as follows:

Major amount: 5,000 MXN (the base currency you are trading).
Minor amount: The equivalent in USDC, calculated using the exchange rate
If the exchange rate is MXN/USDC = 0.050, then: 5,000 MXN × 0.050 = 250 USDC (minor amount)

It means you are exchanging 5,000 Mexican Pesos for 250 Digital Dollars at the given exchange rate.

Developer Testing Server
When working on integrations, Bitso recommends using our sandbox server before running your code on production. The server's URL is as follows: https://api-sandbox.bitso.com/api/v3/

You can fund accounts on the testing server with Bitcoin Testnet and Ethereum's Ropsten Testnet.

Language Detection
If you use API keys, then the initial detection phase is the language configured in your settings. The language setting defaults to a predefined value depending on your country of residence when you sign up for a Bitso account.

To force a specific language, use the Accept-Language header on your request, which overrides the default setting.

When none of these settings are configured, then the default language is English, en.



List Available Books
The method GET /available_books/ enables you to retrieve a list of existing exchange order books and their respective order placement limits.

HTTP Request
GET https://stage.bitso.com/api/v3/available_books
JSON Response Payload
The endpoint returns a JSON array of available exchange order books. Every element in the array is a JSON object that contains the following fields:

Field Name	Description	Type	Units
book	The order book symbol	String	Major_Minor
default_chart	Price chart that provides information about the current and past state of the market. Possible values: depth, candle, hollow, line, and trading view.	String	
fees	The fee structure applied in the book. See the table below for its description.	Object	
margin_enabled	Indicates whether margin trading is enabled for this book.	Boolean	
minimum_amount	The minimum amount of major when placing an order.	String	Major
maximum_amount	The maximum amount of major when placing an order.	String	Major
minimum_price	The minimum price when placing an order.	String	Minor
maximum_price	The maximum price when placing an order.	String	Minor
minimum_value	The minimum value amount (amount*price) when placing an order.	String	Minor
maximum_value	The maximum value amount (amount*price) when placing an order.	String	Minor
tick_size	The minimum price difference that must exist at all times between consecutive bid and offer prices in the order book. In other words, it is the minimum increment in which prices can change in the order book.	String	
The following table describes the fees object:

Field Name	Description	Type	Units
flat_rate	Acts as a fallback mechanism that specifies the fees to apply to makers and takers in case a fee structure is not defined for the book.	Object	
structure	Describes the fee tiers defined based on the volume traded. For example, in the payload shown, the first tier goes from 0 to 1,500,000, the second from 1,500,001 to 2,000,000, and so forth. Increasing your trading volume lowers fees only if it reaches the next tier. Every tier shows the fee applied to makers and takers as a decimal, and the volume figures reported are denominated in the minor currency.	Array	Minor
The following response object exemplifies the JSON array returned, showing only a small set of elements:

curl https://stage.bitso.com/api/v3/available_books

Available Books Response Object

{
   "payload":[
      {
         "default_chart":"candle",
         "minimum_price":"500",
         "margin_enabled":true,
         "fees":{
            "flat_rate":{
               "maker":"0.500",
               "taker":"0.650"
            },
            "structure":[
               {
                  "volume":"1500000",
                  "maker":"0.00500",
                  "taker":"0.00650"
               },
               {
                  "volume":"2000000",
                  "maker":"0.00490",
                  "taker":"0.00637"
               },
               {
                  "volume":"5000000",
                  "maker":"0.00480",
                  "taker":"0.00624"
               },
               {
                  "volume":"7000000",
                  "maker":"0.00440",
                  "taker":"0.00572"
               },
               {
                  "volume":"10000000",
                  "maker":"0.00420",
                  "taker":"0.00546"
               },
               {
                  "volume":"15000000",
                  "maker":"0.00400",
                  "taker":"0.00520"
               },
               {
                  "volume":"35000000",
                  "maker":"0.00370",
                  "taker":"0.00481"
               },
               {
                  "volume":"50000000",
                  "maker":"0.00300",
                  "taker":"0.00390"
               },
               {


                Get Ticker
The method GET /ticker/ enables you to retrieve trading information from the specified book.

HTTP Request
GET https://stage.bitso.com/api/v3/ticker
Query Parameters
You can use the following query parameter in your request:

Parameter	Description	Required
book	Specifies which book to use.	Yes
JSON Response Payload
The endpoint returns a JSON object representing the trading information of the given book. This JSON object includes the following fields:

Field Name	Description	Type	Units
ask	The lowest sell order.	String	Minor/Major
bid	The highest buy order.	String	Minor/Major
book	The order book symbol.	String	Major_Minor
change_24	The price variation during the last 24 hours	String	Minor/Major
created_at	The date and time when the service generated the ticker.	String	ISO 8601 timestamp
high	The last-24-hour price high.	String	Minor/Major
last	The last-traded price.	String	Minor/Major
low	The last-24-hour price low.	String	Minor/Major
rolling_average_change	The unweighted arithmetic average (mean) of the price change (percentage) during the previous six hours, also known as moving average change. A data point is obtained during six one-hour periods in the following way: The percentage of price change during h1 and h2 is p1, the one during h2 and h3 is p2, and so forth until the period between h6 and h7, which yields p6. The unweighted arithmetic average of these six readings is what the endpoint reports.	Object	
volume	The last-24-hour volume.	String	Major
vwap	The last-24-hour-volume-weighted average price (vwap).	String	Minor/Major
The following response object exemplifies the JSON object returned:

curl https://stage.bitso.com/api/v3/ticker?book=btc_mxn

Ticker Response Object

{
  "high": "472472.82",
  "last": "372110.00",
  "created_at": "2023-03-09T20:58:23+00:00",
  "book": "btc_mxn",
  "volume": "112.81964756",
  "vwap": "388387.4631589659",
  "low": "10000.00",
  "ask": "372800.00",
  "bid": "372110.00",
  "change_24": "-25580.00",
  "rolling_average_change": {
    "6": "-0.5228"
  }



  List Order Book
The method GET /order_book/ enables you to retrieve a list of all open orders in the specified book. The value of the aggregate query parameter determines the response returned:

True: The service aggregates the orders by price, and the response includes only the top 50 orders for each side of the book. It is the default behavior.
False: The response consists of the whole order book.
HTTP Request
GET https://stage.bitso.com/api/v3/order_book
Query Parameters
You can use the following query parameters in your request:

Parameter	Description	Required	Default Value
aggregate	Specifies whether the response should aggregate orders by price.	No	true
book	Specifies the book to use.	Yes	
JSON Response Payload
The endpoint returns a JSON object with Asks and Bids. Each of these is a JSON array of open orders, and each open order is represented as a JSON object. The response fields are as follows:

Field Name	Description	Type
asks	The list of open asks.	JSON array
bids	The list of open bids.	JSON array
sequence	An increasing integer value for each order book update.	Long
updated_at	The date and time when the service last updated the order.	ISO 8601 timestamp
Asks and Bids in the aggregated order books are JSON dictionaries with the following fields:

Field Name	Descriptiion	Type	Units
amount	The major amount in the order.	String	Major
book	The order book symbol.	String	Major_Minor
price	The price per unit of major.	String	Minor
Asks and Bids in the unaggregated (whole) order books are JSON dictionaries with the following fields:

Field Name	Descriptiion	Type	Units
amount	The major amount in the order.	String	Major
book	The order book symbol.	String	Major_Minor
oid	The order's ID.	String	
price	The price per unit of major.	String	Minor
The following response objects exemplify the JSON objects returned:

curl https://stage.bitso.com/api/v3/order_book?book=btc_mxn

Order Book Aggregated Response Object
Order Book Unaggregated Response Object

{
    "success": true,
    "payload": {
        "asks": [{
            "book": "btc_mxn",
            "price": "5632.24",
            "amount": "1.34491802"
        },{
            "book": "btc_mxn",
            "price": "5633.44",
            "amount": "0.4259"
        },{
            "book": "btc_mxn",
            "price": "5642.14",
            "amount": "1.21642"
        }],
        "bids": [{
            "book": "btc_mxn",
            "price": "6123.55",
            "amount": "1.12560000"
        },{
            "book": "btc_mxn",
            "price": "6121.55",
            "amount": "2.23976"
        }],
        "updated_at": "2016-04-08T17:52:31.000+00:00",
        "sequence": "27214"
    }
}




List Trades
The method GET /trades/ enables you to retrieve a list of recent trades from the specified book.

HTTP Request
GET https://stage.bitso.com/api/v3/trades
Query Parameters
You can use the following query parameters in your request:

Parameter	Description	Required	Default Value
book	Specifies which book to use.	Yes	
limit	Specifies the number of objects to return. Maximum is 100.	No	25
marker	Specifies to return older or newer objects (depending on the value of the sort parameter) than the object with the given ID.	No	
sort	Specifies the ordering direction of returned objects. Valid values: asc, desc.	No	desc
JSON Response Payload
The endpoint returns a descending JSON array of transactions. Every element in the array is a JSON object that contains the following fields:

Field Name	Description	Type	Units
amount	The major amount transacted.	String	Major
book	The order book symbol.	String	Major_Minor
created_at	The date and time when the service executed the trade.	String	ISO 8601 timestamp
maker_side	An indicator of the maker order side (maker order is the order that was opened in the order book).	String	
price	The price per unit of major.	String	Minor
tid	The trade's ID.	Long	
The following response object exemplifies the JSON array returned:

curl https://stage.bitso.com/api/v3/trades?book=btc_mxn

Trades Response Object

{
    "success": true,
    "payload": [{
        "book": "btc_mxn",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "amount": "0.02000000",
        "maker_side": "buy",
        "price": "5545.01",
        "tid": 55845
    }, {
        "book": "btc_mxn",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "amount": "0.33723939",
        "maker_side": "sell",
        "price": "5633.98",
        "tid": 55844
    }]
}


General
This article explains the channels the API provides, the format of the messages sent, the channel subscription procedure, and a channel connection example.

Available Channels
The WebSocket API uses the following communication channels to facilitate real-time data transfer from and to the server:

Trades Channel: Sends a message whenever the service executes a new trade in the corresponding order book.

Orders Channel: Maintains an up-to-date list of the top 20 asks and the top 20 bids. New messages are sent across the channel whenever there is a change in either top 20 items.

Diff-Orders Channel: Sends across any modifications to the order book, specifically any state changes in existing orders (including orders not in the top 20 items) and any new orders. The service could do the following with an order:

Cancel it, in which case it does not have the fields a (amount) and v (value).
Partially fill it, which reflects in the amount field. You can look up an order's state via the Look Up Orders endpoint.
Each message in the Diff-Orders channel contains a sequence number, which is an increasing integer value. Each new message increments the sequence number by one. If you see a sequence number greater than the previous one by more than one unit, it means a message has been dropped, and you need to update the order book to get to the correct state.

In theory, you can get a copy of the whole order book via REST once and keep it up to date using the Diff-Orders channel with the algorithm explained in the section, How to Keep an Order Book.

Fields Included in Messages
All of the messages from every channel of the WebSocket API are JSON objects that contain four mandatory fields:

type: Represents the channel sending the message.
book: Indicates the corresponding order book.
payload: Stores data relevant to the subscribed channel.
sent: Indicates when the service broadcasted the event to the publish-subscribe messaging in milliseconds (timestamp).
However, the Diff-Orders channel adds one field to this list of four mandatory elements, so the messages from this channel contain five required fields:

sequence: Stores an increasing integer value.
Sample Messages
The following JSON objects depict the mandatory fields contained in every message of the WebSocket API channels:

Mandatory Fields in Trades and Orders Channels
Mandatory Fields in Diff-Orders Channel

{
   "type": "...",
   "book": "...",
   "payload": ["..."],
   "sent": 123465789
}
How to Keep an Order Book
To get a copy of the whole order book once via REST and keep it up to date:

Subscribe to the Diff-Orders channel.
Queue any message that comes into this channel.
Retrieve the whole order book by calling the REST /order_book/ endpoint.
Play back the queued messages, discarding the ones with a sequence number below or equal to the one from the REST order book.
Apply the subsequent queued messages to your local order book data structure.
Apply real-time messages to your local order book as they come in through the stream.
📘
Timestamp Field
An order's timestamp field is immutable. Even if the service mutates the amount field or removes the order, the timestamp field remains as it was when the service created the order.

A timestamp is not unique, and different orders can have the same timestamp.

How to Subscribe to a Channel
To connect to the channels of the WebSocket API, perform the following steps:

Create a WebSocket instance:
Creating Instance

websocket = new WebSocket('wss://ws.bitso.com');
Subscribe to each of the channels you want to connect to:
Subscribing to a Channel

websocket.onopen = function() {
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'trades' }));
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'diff-orders' }));
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'orders' }));
};
The server acknowledges each subscription to a channel with a message. For example, a successful subscription to the trades channel returns the following acknowledgment message:

Acknowledging the Subscription

{"action": "subscribe", "response": "ok", "time": 1455831538045, "type": "trades"}
When you've successfully subscribed to a channel, listen for messages and handle them appropriately:
Listening for Messages

websocket.onmessage = function(message){
                var data = JSON.parse(message.data);

                if (data.type == 'trades' && data.payload) {

                }
                else if (data.type == 'diff-orders' && data.payload) {

                }
                else if (data.type == 'orders' && data.payload) {

                }
            };
Keep alive messages look like this:

JSON

{"type": "ka"}
Implementation Example
The following native JavaScript implementation can serve as a channel connection example:

https://bitso.com/demo ws.html



Trades Channel
This article explains the subscription and server messages produced in the Trades channel.

Subscription Messages
Subscription messages have the following formats:

Client Subscription Message
Server Subscription Response Message

{
   "action": "subscribe",
   "book": "btc_mxn",
   "type": "trades"
}
Server JSON Messages
The server's returned payload contains an array with one or more trades of the following form:

Field Name

Description

Type

Units

a

The amount

String

Major

i

A number that uniquely identifies the transaction.

Number

mo

Maker Order ID

String

r

The rate

String

Minor

t

Taker side. Possible values:

0 indicates buy
1 indicates sell
Number

to

Taker Order ID

String

v

The value

String

Minor

x

Creation timestamp

Number

Milliseconds

Example of Server Messages
Messages on the Trades channel look like this:

Server Payload

{
  "type": "trades",
  "book": "btc_mxn",
  "payload": [
    {
      "i": 77777,
      "a": "0.0035",
      "r": "7190",
      "v": "25.16",
      "mo": "laasdqw1ywYgfYI2",
      "to": "asADW123wedwqeYk",
      "t": 0,
      "x": 1675555546102
    }
  ],
  "sent": 1675555546102 
}



Diff-Orders Channel
This article explains the subscription and server messages produced in the Diff-Orders channel.

Subscription Messages
Subscription messages have the following formats:

Client Subscription Message
Server Subscription Response Message

websocket.send (JSON.stringify(
  { action: 'subscribe', 
    book: 'btc_mxn', 
    type: 'diff-orders' }))
Server JSON Messages
The server's returned payload contains an array with one or more orders of the following form:

Field Name

Description

Type

Units

a

The amount

String

Major

d

Unix timestamp

Number

Milliseconds

o

Order ID

String

r

The rate

String

Minor

s

Order status
Valid values: open, cancelled, and completed.
The definitions of each state are below the table.

String

t

Possible values:

0 indicates buy
1 indicates sell
Number

v

The value

String

Minor

z

Timestamp of the last update (excluding Open orders)

Number

Milliseconds

An order can be in one of three possible states:

OPEN: An order appears as open when the service adds it to the book, and remains in this state while it is partially matched.
COMPLETED: An order appears as completed when the service has matched the order for its whole amount or value and removed it from the book.
CANCELLED: The order was cancelled and removed from the book.
Example of Server Messages
Messages on the Diff-Orders channel for open and cancelled orders look like this:

Server Payload Open Order
Server Payload Cancelled Order

{
  "type": "diff-orders",
  "book": "btc_mxn",
  "sequence": 2734,
  "payload": [
    {
      "o": "laasdqw1ywYgfYI2",
      "d": 1675555546102,
      "r": "22222",
      "t": 0,
      "a": "0.25",
      "v": "5312.25",
      "s": "open"
    }
  ],
  "sent": 1675555546102
}




Orders Channel
This article explains the subscription and server messages produced in the Orders channel.

Subscription Messages
Subscription messages have the following formats:

Client Subscription Message
Server Subscription Response Message

websocket.send (JSON.stringify(
  { action: 'subscribe', 
    book: 'btc_mxn', 
    type: 'orders' }))
Server JSON Messages
The server's returned payload contains a JSON object with two keys, one for the bids and the other for the asks on the order book. Both bids and asks include an array of orders of the following form:

Field Name

Description

Type

Units

a

The amount

String

Major

d

Unix timestamp

Number

Milliseconds

o

Order ID

String

r

The rate

String

Minor

s

The status. Set to undefined by default.

String

t

Possible values:

0 indicates buy
1 indicates sell
Number

v

The value

String

Minor

Example of Server Messages
Messages on the Orders channel look like this:

Server Payload

{
  "type": "orders",
  "book": "btc_mxn",
  "payload": {
    "bids": [
      {
        "o": "laasdqw1ywYgfYI2",
        "r": "5555",
        "a": "0.001343",
        "v": "9.64",
        "t": 1,
        "d": 1454445394039,
        "s": "undefined"
      },
      {
        "o": "laasdqw1ywYgfYI2",
        "r": "7777",
        "a": "0.007715",
        "v": "55.41",
        "t": 1,
        "d": 1455319938419,
        "s": "undefined"
      },
      {
        "o": "laasdqw1ywYgfYI2",
        "r": "7777",
        "a": "1.59667303",
        "v": "11468.9",
        "t": 1,
        "d": 1455314800000,
        "s": "undefined"
      }
    ],
    "asks": [
      {
        "o": "laasdqw1ywYgfYI2",
        "r": "7777",
        "a": "0.29437179",
        "v": "2134.51",
        "t": 0,
        "d": 1455314800000,
        "s": "undefined"
      },
      {
        "o": "laasdqw1ywYgfYI2",
        "r": "7777",
        "a": "1.32057812",
        "v": "9576.46",
        "t": 0,
        "d": 1455314800000,
        "s": "undefined"
      }
    ]
  },


Understanding Conversions
A conversion is a transaction that enables you to buy or sell any two Bitso-supported assets at a fixed rate rather than at dynamic market prices. For example, the Bitso app creates conversions when you buy or sell cryptocurrencies. A conversion's underlying operation is a trade, and it might be necessary to execute several trades to complete the conversion amount.

Users benefit from conversions in the following ways:

They let them know the exact amount of assets they will receive or need to spend at a fixed rate.
They enable them to select any two currencies supported by Bitso to buy or sell without placing orders in a trading book or worrying whether a given currency pair exists in a book. You can convert a couple of currencies even if a trading book does not exist for them because Bitso's Conversion Engine has the ability to hop among available books to perform the needed conversion.
Conversions have a specific flow:

Request a conversion quote: Use the method POST /api/v4/currency_conversions specifying the currencies to convert as well as the amount, and the call returns a conversion rate, which is fixed and valid for the next 30 seconds.
Execute the conversion quote: The request-quote call also provides a quote ID (id), which identifies the quote to submit to Bitso's Conversion Engine. Use the method PUT /api/v4/currency_conversions/{quote_id} to execute your conversion. A successful conversion returns a conversion ID (oid), which is useful to track your conversion.
Track your conversion: After submitting your conversion quote, you can retrieve the conversion details and determine its status with the method GET /api/v4/currency_conversions/{conversion_id}.
The following articles explain the details of each of these steps.



Request a Conversion Quote
The POST /api/v4/currency_conversions method enables you to request a conversion quote. Before you can execute a conversion of your working capital from one currency to another, you must request a quote, which presents, among others, the conversion rate offered, the amount to spend in the source currency, the amount to receive in the target currency, and the fee charged if the quote is accepted.

Quotes expire in 30 seconds. Hence, you must accept (execute) it within this period. When a quote expires, you can no longer run it and must request a new one.

You can request the quote in two different, mutually exclusive ways:

Setting how much you want to convert (spend_amount) from one currency to another.
Specifying how much you expect to receive (receive_amount) as a product of the conversion.
In either, you also specify the source and target currencies.

HTTP Request
To request a conversion, complete the following HTTP request using the appropriate body parameters:

POST https://stage.bitso.com/api/v4/currency_conversions

Header Parameters
You must specify the following authentication parameters in your request:

Parameter	Description	Required
key	See the section, Authentication	Yes
signature	See the section, Authentication	Yes
nonce	See the section, Authentication	Yes
Body Parameters
Body parameters must be JSON encoded and precisely the same as the JSON payload used to construct the signature:

Parameter	Description	Type	Required
from_currency	The ticker of the source currency. For example, mxn.	String	Yes
to_currency	The ticker of the target currency. For example, btc.	String	Yes
receive_amount	The amount you expect to receive as a result of the conversion, specified in the target currency. This value should be a positive number.	String	No. See callout below
spend_amount	The amount you are willing to convert, specified in the source currency. This value should be a positive number.	String	No. See callout below
🚧
Mutually exclusive parameters
Recall these amounts are mutually exclusive, so ensure you include only one of them in your request.

📘
Supported currencies
For details on supported currencies, see the section, Currency Dictionary.

Request Examples
The next examples show the two ways the endpoint offers to specify the amount in your request.

Conversion Quote Request Body receive_amount
Conversion Quote Request Body spend_amount

{
    "from_currency":"mxn",
    "to_currency":"usd",
    "receive_amount":"100"
}
JSON Response Payload
A successful call returns a JSON object representing a conversion quote. The following response objects exemplify the JSON object returned:

Conversion Quote Response Body
Conversion Quote Response Body

{
    "success": true,
    "payload": {
        "id": "zmAfx2rvNnv1Jn0Q",
        "from_amount": "1854.21860516",
        "from_currency": "mxn",
        "to_amount": "100.00000000",
        "to_currency": "usd",
        "estimated_slippage": {
            "value": "0.0000",
            "level": "normal",
            "message": ""
        },
        "created": 1719862339217,
        "expires": 1719862369217,
        "rate": "18.54",
        "plain_rate": "18.36",
        "rate_currency": "mxn",
        "padding": "0.0098",
        "book": "xrp_mxn",
        "next_recurrent_events": {
            "WEEKLY": 1720467139217,
            "DAILY": 1719948739217,
            "MONTHLY": 1722540739217
        }
    }
}
The value of the id variable is the path parameter (quote_id) you need to use when executing-a-conversion-quote.

The fields included in the response object have the following meaning:

Field Name	Description	Type
book	The book to use.	String
created	The quote's creation epoch in milliseconds.	Number
estimated_slippage	An estimation of the difference between the expected execution rate and the actual execution rate.	Object
expires	The quote's expiration epoch in milliseconds.	Number
from_amount	The amount you are willing to convert specified in the source currency.	String
from_currency	The ticker of the source currency.	String
id	The quote's unique ID.	String
next_recurrent_events	Indicates when the next conversions are to take place in milliseconds. Used when conversions are programmed in the Bitso application to occur at specific periods.	Object
padding	The fee users pay for the conversion.	String
plain_rate	The market's exchange rate without the spread value added to rate.	String
rate	The exchange rate Bitso offers users for the conversion.	String
rate_currency	The ticker of the currency in which the conversion rate is expressed.	String
to_amount	The amount you expect to receive as a product of the conversion specified in the target currency.	String
to_currency	The ticker of the target currency.	String



Execute a Conversion Quote
The PUT /api/v4/currency_conversions/{quote_id} method enables you to execute a conversion quote within the 30-second expiration limit. You use the value of the variable id returned by the request-quote call to submit the conversion to Bitso's Conversion Engine. After you submit a conversion, it starts executing asynchronously.

It is impossible to cancel the execution of a conversion quote once you have submitted it.

HTTP Request
PUT https://stage.bitso.com/api/v4/currency_conversions/{quote_id}
Header Parameters
You must specify the following authentication parameters in your request:

Parameter	Description	Required
key	See the section, Authentication	Yes
signature	See the section, Authentication	Yes
nonce	See the section, Authentication	Yes
Path Parameters
You must specify the following path parameter in your request:

Parameter	Description	Required
quote_id	Identifies the quote you want to execute. The request-quote call returns it as id.	Yes
JSON Response Payload
A successful call returns a JSON object representing the executed conversion. The following response object exemplifies the JSON object returned:

Execute Conversion Response Body

{
    "success": true,
    "payload": {
        "oid": "7316"
    }
}
The value of the oid variable is the path parameter (conversion_id) you need to use when getting-a-conversion-status.

The meaning of the response object field is as follows:

Field Name	Description	Type
oid	The conversion's unique ID.	String


Get a Conversion Status
Given that a conversion executes asynchronously, to know when the conversion fully completes, it is necessary to retrieve its status. The GET /api/v4/currency_conversions/{conversion_id} method enables you to recover a conversion's details and its updated state. Then, after submitting the conversion quote for execution, you can use this method to poll the quote and determine its status.

Conversions can be in one of four possible states:

OPEN: This is the initial state. The service created the transaction and is awaiting execution. This state will eventually change to queued when the conversion starts executing.
QUEUED: Bitso's Conversion Engine is executing the transaction. A conversion usually remains in this state for no more than one second. However, in moments of high load, it could be longer but never higher than 10 seconds (production environment).
COMPLETED: The conversion ended successfully; the funds are now in the target currency.
FAILED: The system could not complete the conversion; the funds remain in the original currency. You can retry by getting another quote.
A conversion's normal flow is Open → Queued → Completed or Failed, and there is no way to bypass any status or speed up the transition to the next state. The Conversion Engine has mechanisms to monitor the transactions in the production environment continuously, and in case one becomes stuck, the Bitso team fixes it.

HTTP Request
GET https://stage.bitso.com/api/v4/currency_conversions/{conversion_id}
Header Parameters
You must specify the following authentication parameters in your request:

Parameter	Description	Required
key	See the section, Authentication	Yes
signature	See the section, Authentication	Yes
nonce	See the section, Authentication	Yes
Path Parameters
You must specify the following path parameter in your request:

Parameter	Description	Required
conversion_id	Identifies the conversion you want to retrieve. The execute-a-conversion-quote call returns it as oid.	Yes
JSON Response Payload
A successful call returns a JSON object representing the executed conversion. The following response object exemplifies the JSON object returned:

Retrieve Conversion Response Body

{
    "success": true,
    "payload": {
        "id": "7316",
        "from_amount": "1854.21860516",
        "from_currency": "mxn",
        "to_amount": "100.00000000",
        "to_currency": "usd",
        "created": 1719862355209,
        "expires": 1719862385209,
        "rate": "18.54218605",
        "plain_rate": "18.36",
        "rate_currency": "mxn",
        "book": "xrp_mxn",
        "status": "completed"
    }
}
The response object fields have the following meaning:

Field Name	Description	Type
book	The book used.	String
created	The conversion's creation epoch in milliseconds.	Number
expires	The conversion's expiration epoch in milliseconds.	Number
from_amount	The amount converted specified in the source currency.	String
from_currency	The ticker of the source currency.	String
id	The conversion's unique identifier.	String
plain_rate	The market's exchange rate without the spread value added to rate.	String
rate	The exchange rate Bitso offers users for the conversion.	String
rate_currency	The ticker of the currency in which the conversion rate is expressed.	String
status	The conversion's state. Possible values: open, queued, completed, and failed.	String
to_amount	The amount received as a product of the conversion specified in the target currency.	String
to_currency	The ticker of the target currency.	String


Error Categories
Error codes consist of four digits; the first two indicate an error category, whereas the last two define a specific error.

The categories included are the following:

01: Unknown Errors
02: Authentication Errors
03: Validation Errors - Part 1
04: System Limit Errors
05: User Limit Errors
06: Funds Errors
07: Account Errors
08: Throttling Errors
09: Unsupported-Method Errors
10: Miscellaneous Errors
11: Operation Errors
12: Phone-Related Errors
13: OTP Errors
14: Not-Found Errors
16: SPEI Remittance Errors
17: Validation Errors - Part 2
The following pages list the errors contained in each category.


The category Unknown Errors: 01 (HTTP 500) includes the following set:

0101: Unknown Error
0102: Invalid Ripple Withdrawal


The category Authentication Errors: 02 (HTTP 401) includes the following set:

0201: Check your credentials
0202: API key is not authorized to execute the requested method
0203: Login token is invalid or expired
0204: Incorrect PIN
0205: Too many login attempts
0206: Invalid nonce type
0207: Invalid nonce value
0208: Authentication is required to execute requested operation
0209: Two Factor authentication required
0210: Device authentication required
0211: Device authentication failed (Invalid IP or expired Token)
0212: Access Denied - This code is reserved for internal use
0213: IP address is not allowed to access this resource
0214: Invalid ReCAPTCHA - There was an issue validating the reCAPTCHA
0215: Incorrect request signature
0216: Your account has been restricted; please get in touch with your contact at Bitso
(Users with a PTS line might get this message, and their contact is a member of the Market Maker support team.)


The category Validation Errors: 03 (HTTP 400) includes the following set:

0301: Unknown Order book
0302: Incorrect time frame (not 'hour' or 'minute')
0303: Required field missing
0304: Required field not valid (email, phone_number)
0305: Invalid SMS code (would also apply to correct code but not-correct client ID)
0306: Order side not in (buy, sell)
0307: Order type not in (limit, market)
0308: Order request cannot include both minor and major
0309: Order request must include either minor or major
0310: Incorrect WID (non-existent or does not belong to user)
0311: Incorrect FID (non-existent or does not belong to user)
0312: Incorrect OID (non-existent or does not belong to user)
0313: Selected currency not in (mxn, btc, eth)
0314: Auto-trade not available for selected currencies
0315: Invalid address
0316: Invalid Ripple currency
0317: Invalid SPEI number
0318: Invalid SPEI numeric_ref
0319: Invalid SPEI notes_ref
0320: Invalid pagination parameters
0321: Incorrect TID (non-existent)
0322: Not a Valid URL
0323: No associated country code
0324: Number already in use
0325: Phone already verified
0326: API key is not active
0327: Service unavailable for requesting location
0328: Service unavailable for requesting country
0329: Market order type must be in (maj, min)
0330: Withdrawals locked for this account
0331: Invalid referral code for Bitso Transfer
0332: Empty PIN
0333: PIN locked. Too many attempts
0334: Bitso Transfers need either an email, phone_number, or refcode specified
0335: Invalid SPEI recipient name
0336: No data found for KYC (CURP-Mexico, CUIL-Argentina, CPF-Brazil)
0337: No KYC found for data (CURP-Mexico, CUIL-Argentina, CPF-Brazil)
0338: Multiple KYCs found for data (CURP-Mexico, CUIL-Argentina, CPF-Brazil)
0339: Email is already in use
0340: Not supported country
0341: Invalid postal code
0342: Invalid CVU
0343: Incorrect amount
0344: Invalid BIND recipient name
0345: Quote is expired or invalid
0346: You need to agree to the new terms and conditions
0347: Too many attempts to validate KYC (CURP-Mexico, CUIL-Argentina, CPF-Brazil)
0348: KYC data did not match with user data. (CURP-Mexico, CUIL-Argentina, CPF-Brazil)
0349: Already in use
0350: Cannot disable a currency with positive balance
0351: Unable to generate CVU for user
0352: Disposable email not allowed
0353: Current withdrawal fee is higher than specified maximum
0354: No defined legal operation entity
0355: Incorrect hash (non-existent or does not belong to user)
0356: Duplicate origin ID provided
0357: Incorrect origin ID (non-existent or does not belong to user)
0358: The password must have at least 8 characters
0359: The password is too long
0360: At least one field is required but none was submitted
0361: Two or more fields were submitted when only one is required
0362: Invalid callback URL
0363: Invalid Transaction ID (Either non-existent or does not belong to the user)
0364: Password doesn't meet security requirements
0365: Two factor authentication method is already enabled
0366: Two factor authentication method is not enabled
0367: Unable to generate quote at the present time
0368: Rejected withdrawal to restricted address
0369: Incorrect device ID
0370: File type not allowed
0371: File size limit exceeded
0372: Incorrect value type for field
0373: Request has expired
0374: Invalid 2FA recovery code
0375: Reserved for internal use
0376: Limit of Bitso Transfer reached
0377: Order matched, but trade records still being processed
0378: Order has not been matched yet
0379: Insufficient balance
0381: Contact not found
0382: Third-party withdrawals are blocked
0384: Withdrawal request not found
0385: User not allowed to update withdrawal request
0386: Withdrawal request cannot be updated to desired state
0387: Address not found
0388: User not onboarded with provider
0389: Invalid description

The category System-Limit Errors: 04 (HTTP 400) includes the following set:

0401: Incorrect price, below the minimum
0402: Incorrect price, above than maximum
0403: Incorrect major, below the minimum
0404: Incorrect major, above the maximum
0405: Incorrect minor, below the minimum
0406: Incorrect minor, above the maximum
0407: Invalid precision
0408: Incorrect amount value, it must be a non-zero positive value.
0410: Trading not enabled
0411: Trading not enabled for market orders
0412: Incorrect stop, below the minimum
0413: Incorrect stop, above the maximum
0414: Internal use
0415: Internal use
0416: Internal use
0417: Internal use

The category Throttling Errors: 08 (HTTP 420) includes the following set:

0801: You have hit the request rate-limit
0802: Too many attempts to perform an operation
The category Unsupported-Method Errors: 09 (HTTP 400) includes the following set:

0901: Unsupported HTTP method

The category Miscellaneous Errors: 10 (400 error) includes the following set:

1000: API temporarily disabled (More info in error message)
1001: Too many open orders
1002: Unable to process order
1003: Operation timeout
1004: Deprecated functionality
1005: Invalid operation
1006: No content for given mobile client name (204 code)
1007: Internal use
1008: Trading disabled
1009: Conversions disabled

---

## EnsoX Integration Notes

### Adapter
`zig_adapter` — no dedicated Elixir adapter. All parsing in Zig via config.

### WS Trades Channel
- URL: `wss://ws.bitso.com`
- Subscribe: `{"action":"subscribe","book":"<symbol>","type":"trades"}` per symbol
- Discriminator: `type` field
- Envelope: `{"type":"trades","book":"btc_mxn","payload":[...],"sent":1675555546102}`
- Trade fields (short names): `r`=rate/price, `a`=amount, `t`=side(0=buy,1=sell), `x`=timestamp(ms), `i`=trade_id, `v`=value, `mo`=maker_order_id, `to`=taker_order_id
- `payload` is an ARRAY of trades → Zig `array_key: "payload"` handles iteration
- Side: numeric `0`=buy, `1`=sell (not text)

### WS Orders Channel (Depth)
- Subscribe: `{"action":"subscribe","book":"<symbol>","type":"orders"}` per symbol
- Top 20 bid/ask **snapshot**, refreshed on every change
- Envelope: `{"type":"orders","book":"btc_mxn","payload":{"bids":[...],"asks":[...]}}`
- Level fields: `r`=rate/price, `a`=amount (same short names as trades)
- Mapped as depth handler with `level_format: "named"`, `is_snapshot: true`

### WS diff-orders (NOT used)
- Individual order state changes (open/cancelled/completed) — NOT depth levels
- Classified as ack (`text_ack_patterns`)

### REST Trades (Recovery)
- Endpoint: `GET /v3/trades?book=<symbol>&limit=100&sort=asc`
- Response: `{"success":true,"payload":[{"book","created_at","amount","maker_side","price","tid"}]}`
- Pagination: `marker=<tid>` (trade ID-based, NOT time-based). No `after`/`before` time params.
- Timestamp: ISO 8601 (`created_at`)
- Side field: `maker_side` (text: "buy"/"sell")
- Max 100 per request

### REST Orderbook Snapshot
- Endpoint: `GET /v3/order_book?book=<symbol>&aggregate=true`
- Returns 50 bids + 50 asks (aggregated)
- Level format: `{"book":"btc_mxn","price":"1253090","amount":"0.11177"}`
- Response path: `payload.bids` / `payload.asks`

### Products
- Endpoint: `GET /v3/available_books`
- Symbol format: `btc_mxn` (lowercase, underscore separator)
- Response path: `payload`

### Rate Limits
- Public: 60 RPM (1 req/s) → `rate_limit_ms: 1000`
- Private: 300 RPM (verified user)
- Exceeding: 1-minute lockout, repeated = 24-hour block

### Verified: 2026-03-04