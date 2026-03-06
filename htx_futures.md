Solution Architecture
HTX swap API colocation solution is built on AWS infrastructure. Client will connect via AWS “PrivateLink” to access HTX’s services directly through fast AWS connection without being routed to public networks.

Performance Improvement
The network delay of colocation solution is estimated to be 10ms to 50ms faster than the ordinary connection. This improvement estimated should be used as a guidance only as the actual improvement depends on many factors.

Eligibility
Colocation is only available to higher tier market makers. To check if your account is eligible please talk to your dedicated account manager.





Partial Liquidation
Margin ratio is an indicator to estimate the risk of users’assets. When the margin ratio is less than or equal to 0%, liquidation will be triggered.
It is recommended that you pay close attention to margin ratio changes, so as to avoid your positions from liquidation.
HTX contracts implement a partial liquidation mechanism, in which the system will lower the corresponding tier of an adjustment factor to avoid your positions from being liquidated at one time.
More detail to see: Partial Liquidation

Insurance Funds and Clawback Mechanism
Insurance funds are designed to cover the losses from forced liquidation.
In a fluctuating market, users’ positions may be liquidated. When the order cannot be filled at the takeover price, resulting in huge losses that are greater than the part insurance funds can undertake, the platform will implement the “clawback” mechanism. Each profitable account in the current period compensates the over loss of liquidation according to its profit ratio.
More detail in here: Partial Liquidation

Tiered Adjustment Factor
The adjustment factor is designed to prevent users from extended margin call loss. HTX Contracts use a tiered adjustment factor mechanism, which supports up to five tiers based on the position amount.
For contracts with different expirations under the different account modes, they are separately calculated. The larger the use’s net positions, the higher the tier, and the greater the risk.
More detail in here: Tiered Adjustment Factor of USDT-margined Contract



Matching System: Order accepted by the Order System will enter the Matching System. Once orders are matched/filled, the settlement service will be executed and the matching result will be returned to the Order System; otherwise, the unfilled orders will go into the order book for matching.
Price Priority: Higher-priced buy orders have priority over lower-priced buy orders; the reverse is true, lower-priced sell orders have priority over higher-priced sell orders.
Time Priority: Buy orders at the same price are executed according to the time of entry to the Server.
When the highest bid price is the same as the lowest ask price of the order book, this price is what we call transaction price.
When the bid price is higher than the lowest ask price of the order book up to the minute, the lowest ask price will be the transaction price.
When the ask price is lower than the highest bid price of the order book up to the minute, the highest bid price will be the transaction price.



permission type	Content Type	Interface Mode	Context	Request Type	Desc	Signature Required
Read	Market Data	general	/linear-swap-api/v1/swap_contract_info	GET	Get Contracts Information	No
Read	Market Data	general	/linear-swap-api/v1/swap_index	GET	Get contract Index Price Information	No
Read	Market Data	general	/linear-swap-api/v1/swap_price_limit	GET	Query Swap Price Limitation	No
Read	Market Data	general	/linear-swap-api/v1/swap_open_interest	GET	Get Contract Open Interest Information	No
Read	Market Data	general	/linear-swap-api/v1/swap_risk_info	GET	Query information on contract insurance fund balance and estimated clawback rate	No
Read	Market Data	general	/inear-swap-api/v1/swap_insurance_fund	GET	Query history records of insurance fund balance	No
Read	Market Data	isolated margin	/linear-swap-api/v1/swap_adjustfactor	GET	Query information on Tiered Adjustment Factor	No
Read	Market Data	general	/linear-swap-api/v1/swap_his_open_interest	GET	Query information on open interest	No
Read	Market Data	general	/linear-swap-api/v1/swap_elite_account_ratio	GET	Query Top Trader Sentiment Index Function-Account	No
Read	Market Data	general	/linear-swap-api/v1/swap_elite_position_ratio	GET	Query Top Trader Sentiment Index Function-Position	No
Read	Market Data	general	/linear-swap-api/v1/swap_liquidation_orders	GET	Query Liquidation Order Information	No
Read	Market Data	general	/linear-swap-api/v1/swap_settlement_records	GET	Query historical settlement records of the platform interface	No
Read	Market Data	isolated margin	/linear-swap-api/v1/swap_api_state	GET	Query information on system status	No
Read	Market Data	general	/linear-swap-api/v1/swap_funding_rate	GET	Query funding rate	No
Read	Market Data	general	/linear-swap-api/v1/swap_batch_funding_rate	GET	[General]Query a Batch of Funding Rate	No
Read	Market Data	general	/linear-swap-api/v1/swap_historical_funding_rate	GET	Query Historical Funding Rate	No
Read	Market Data	general	/linear-swap-ex/market/depth	GET	Get Market Depth	No
Read	Market Data	General	/linear-swap-ex/market/bbo	GET	Get Market BBO Data	No
Read	Market Data	general	/linear-swap-ex/market/history/kline	GET	Get KLine Data	No
Read	Market Data	general	/index/market/history/linear_swap_mark_price_kline	GET	Get Kline Data of Mark Price	No
Read	Market Data	general	/linear-swap-ex/market/detail/merged	GET	Get Market Data Overview	No
Read	Market Data	general	/linear-swap-ex/market/detail/batch_merged	GET	Get a Batch of Market Data Overview	No
Read	Market Data	general	/v2/linear-swap-ex/market/detail/batch_merged	GET	Get a Batch of Market Data Overview(V2)	No
Read	Market Data	general	/index/market/history/linear_swap_basis	GET	Query Basis Data	No
Read	Market Data	general	/index/market/history/linear_swap_premium_index_kline	GET	Query Liquidation Order Information	No
Read	Market Data	general	/index/market/history/linear_swap_estimated_rate_kline	GET	Query Swap Market Data interface	No
Read	Market Data	general	/linear-swap-ex/market/trade	GET	Query The Last Trade of a Contract	No
Read	Market Data	general	/linear-swap-ex/market/history/trade	GET	Query a Batch of Trade Records of a Contract	No
Read	Market Data	cross margin	/linear-swap-api/v1/swap_cross_adjustfactor	GET	Query Information On Tiered Adjustment Factor	No
Read	Market Data	cross margin	/linear-swap-api/v1/swap_cross_transfer_state	GET	Query Information On Transfer State	No
Read	Market Data	cross margin	/linear-swap-api/v1/swap_cross_trade_state	GET	Query Information On Trade State	No
Read	Market Data	general	/linear-swap-api/v1/swap_estimated_settlement_price	GET	Get the estimated settlement price	No
Read	Market Data	general	/linear-swap-api/v1/swap_ladder_margin	GET	[Isolated]Query information on Tiered Margin	No
Read	Market Data	general	/linear-swap-api/v1/swap_cross_ladder_margin	GET	[Cross]Query information on Tiered Margin	No
Read	Account	isolated margin	/linear-swap-api/v1/swap_balance_valuation	POST	[General]Query Asset Valuation	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_account_info	POST	Query User’s Account Information	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_position_info	POST	Query User’s position Information	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_available_level_rate	POST	Query user’s available leverage	Yes
Trade	Account	general	/linear-swap-api/v1/swap_sub_auth	POST	[General]Set a Batch of Sub-Account Trading Permissions	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_sub_account_list	POST	Query assets information of all sub-accounts under the master account (Query by coins)	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_sub_account_info_list	POST	[Isolated]Query a Batch of Sub-Account's Assets Information	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_cross_sub_account_info_list	POST	[Cross]Query a Batch of Sub-Account's Assets Information	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_sub_account_info	POST	Query a single sub-account's assets information	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_sub_position_info	POST	Query a single sub-account's position information	Yes
Read	Account	general	/linear-swap-api/v1/swap_financial_record	POST	Query account financial records	Yes
Read	Account	general	/linear-swap-api/v1/swap_financial_record_exact	POST	[General]Query account financial records via Multiple Fields	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_user_settlement_records	POST	Query Settlement Records of Users	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_user_settlement_records	POST	Query Settlement Records of Users	Yes
Read	Account	general	/linear-swap-api/v1/swap_order_limit	POST	Query contract information on order limit	Yes
Read	Account	general	/linear-swap-api/v1/swap_fee	POST	Query information on contract trading fee	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_transfer_limit	POST	Query information on Transfer Limit	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_position_limit	POST	Query information on position limit	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_lever_position_limit	POST	[Isolated]Query Users' Position Limit for All Leverages	Yes
Read	Account	isolated margin	/linear-swap-api/v1/swap_account_position_info	POST	Query Assets And Positions	Yes
Trade	Account	general	/linear-swap-api/v1/swap_master_sub_transfer	POST	Transfer between master account and sub-accounts	Yes
Read	Account	general	/linear-swap-api/v1/swap_master_sub_transfer_record	POST	Query transfer records of master account	Yes
Trade	Account	general	/linear-swap-api/v1/swap_transfer_inner	POST	Transfer between different margin accounts under the same account	Yes
Read	Account	general	/linear-swap-api/v1/swap_api_trading_status	GET	Query user's API indicator disable information	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_account_info	POST	Query User's Account Information	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_position_info	POST	Query User's Position Information	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_sub_account_list	POST	Query Assets Information Of All Sub-Accounts Under The Master Account	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_sub_account_info	POST	Query A Sub-Account's Assets Information	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_sub_position_info	POST	Query A Sub-Account's Position Information	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_transfer_limit	POST	Query Information On Transfer Limit	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_position_limit	POST	Query Information On Position Limit	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_lever_position_limit	POST	[Cross]Query Users' Position Limit for All Leverages	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_account_position_info	POST	Query Assets And Positions	Yes
Read	Account	cross margin	/linear-swap-api/v1/swap_cross_available_level_rate	POST	Query User’s Available Leverage	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_switch_position_mode	POST	[Isolated]Switch Position Mode	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_switch_position_mode	POST	[Cross]Switch Position Mode	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_order	POST	Place an Order	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_batchorder	POST	Place a Batch of Orders	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_switch_lever_rate	POST	Switch Leverage	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_cancel	POST	Cancel an Order	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_cancelall	POST	Cancel All Orders	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_order_info	POST	Get Information of an Order	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_order_detail	POST	Get Trade Details of an Order	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_openorders	POST	Get Current Orders	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_hisorders	POST	Get History Orders	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_matchresults	POST	Acquire History Match Results	Yes
Read	Trade	isolated margin	/linear-swap-api/v1/swap_hisorders_exact	POST	[Isolated]Get History Orders via Multiple Fields	Yes
Read	Trade	Cross margin	/linear-swap-api/v1/swap_cross_hisorders_exact	POST	[Cross]Get History Orders via Multiple Fields	Yes
Read	Trade	Isolated margin	/linear-swap-api/v1/swap_matchresults_exact	POST	[Isolated]Get History Match Results via Multiple Fields	Yes
Read	Trade	Cross margin	/linear-swap-api/v1/swap_cross_matchresults_exact	POST	[Cross]Get History Match Results via Multiple Fields	Yes
Trade	Trade	isolated margin	/linear-swap-api/v1/swap_lightning_close_position	POST	Place Lightning Close Order	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_trigger_order	POST	Place an Trigger Order	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_trigger_cancel	POST	Cancel a Trigger Order	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_trigger_cancelall	POST	Cancel all trigger Orders	Yes
Read	Strategy	isolated margin	/linear-swap-api/v1/swap_trigger_openorders	POST	Get all open trigger Orders	Yes
Read	Strategy	isolated margin	/linear-swap-api/v1/swap_trigger_hisorders	POST	Get all history trigger Orders	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_switch_lever_rate	POST	Switch Leverage	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_order	POST	Place An Order	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_batchorder	POST	Place A Batch Of Orders	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_cancel	POST	Cancel An Order	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_cancelall	POST	Cancel All Orders	Yes
Read	Trade	cross margin	/linear-swap-api/v1/swap_cross_order_info	POST	Get Information of order	Yes
Read	Trade	cross margin	/linear-swap-api/v1/swap_cross_order_detail	POST	Get Detail Information of order	Yes
Read	Trade	cross margin	/linear-swap-api/v1/swap_cross_openorders	POST	Current unfilled order acquisition	Yes
Read	Trade	cross margin	/linear-swap-api/v1/swap_cross_hisorders	POST	Get History Orders	Yes
Read	Trade	cross margin	/linear-swap-api/v1/swap_cross_matchresults	POST	Get History Match Results	Yes
Trade	Trade	cross margin	/linear-swap-api/v1/swap_cross_lightning_close_position	POST	Place Lightning Close Position	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_trigger_order	POST	Place Trigger Order	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_trigger_cancel	POST	Cancel Trigger Order	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_trigger_cancelall	POST	Cancel All Trigger Orders	Yes
Read	Strategy	cross margin	/linear-swap-api/v1/swap_cross_trigger_openorders	POST	Query Open Trigger Order	Yes
Read	Strategy	cross margin	/inear-swap-api/v1/swap_cross_trigger_hisorders	POST	Query Trigger Order History	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_tpsl_order	POST	[Isolated]Set a Take-profit and Stop-loss Order for an Existing Position	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_tpsl_cancel	POST	[Isolated]Cancel a Take-profit and Stop-loss Order	Yes
Trade	Strategy	isolated margin	/linear-swap-api/v1/swap_tpsl_cancelall	POST	[Isolated]Cancel all Take-profit and Stop-loss Orders	Yes
Read	Strategy	isolated margin	/linear-swap-api/v1/swap_tpsl_openorders	POST	[Isolated]Open take-profit and stop-loss orders	Yes
Read	Strategy	isolated margin	/linear-swap-api/v1/swap_tpsl_hisorders	POST	[Isolated]Take-profit and stop-loss histoty orders	yes
Read	Strategy	isolated margin	/linear-swap-api/v1/swap_relation_tpsl_order	POST	[Isolated]Query Info Of Take-profit and Stop-loss Order That Related To Position Opening Order	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_tpsl_order	POST	[Cross]Set a Take-profit and Stop-loss Order for an Existing Position	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_tpsl_cancel	POST	[Cross]Cancel a Take-profit and Stop-loss Order	Yes
Trade	Strategy	cross margin	/linear-swap-api/v1/swap_cross_tpsl_cancelall	POST	[Cross]Cancel all Take-profit and Stop-loss Orders	Yes
Read	Strategy	cross margin	/linear-swap-api/v1/swap_cross_tpsl_openorders	POST	[Cross]Open take-profit and stop-loss orders	Yes
Read	Strategy	cross margin	/linear-swap-api/v1/swap_cross_tpsl_hisorders	POST	[Cross]Take-profit and stop-loss histoty orders	Yes
Read	Strategy	cross margin	/linear-swap-api/v1/swap_cross_relation_tpsl_order	POST	[Cross]Query Info Of Take-profit and Stop-loss Order That Related To Position Opening Order	Yes
Trade	Account	general	https://api.huobi.pro/v2/account/transfer	POST	Transfer margin between Spot account and USDT Margined Contracts account	Yes
Trade	Strategy	Isolated	/linear-swap-api/v1/swap_track_order	POST	【Isolated】Place a Trailing Order	Yes
Trade	Strategy	Isolated	/linear-swap-api/v1/swap_track_cancel	POST	【Isolated】Cancel a Trailing Order Order	Yes
Trade	Strategy	Isolated	/linear-swap-api/v1/swap_track_cancelall	POST	【Isolated】Cancel All Trailing Orders	Yes
Read	Strategy	Isolated	/linear-swap-api/v1/swap_track_openorders	POST	【Isolated】Current unfilled trailing order acquisition	Yes
Read	Strategy	Isolated	/linear-swap-api/v1/swap_track_hisorders	POST	【Isolated】Get History Trailing Orders	Yes
Trade	Strategy	Cross	/linear-swap-api/v1/swap_cross_track_order	POST	【Cross】Place a Trailing Order	Yes
Trade	Strategy	Cross	/linear-swap-api/v1/swap_cross_track_cancel	POST	【Cross】Cancel a Trailing Order Order	Yes
Trade	Strategy	Cross	/linear-swap-api/v1/swap_cross_track_cancelall	POST	【Cross】Cancel All Trailing Orders	Yes
Read	Strategy	Cross	/linear-swap-api/v1/swap_cross_track_openorders	POST	【Cross】Current unfilled trailing order acquisition	Yes
Read	Strategy	Cross	/linear-swap-api/v1/swap_cross_track_hisorders	POST	【Cross】Get History Trailing Orders	Yes







Address	Applicable sites	Applicable functions	Applicable trading pairs
https://api.hbdm.com	HTX USDT Margined Contracts	API	Trading pairs provided by HTX USDT Margined Contracts
Notice
If you can't connect "https://api.hbdm.com", please use "https://api.btcgateway.pro" for debug purpose. If your server is deployed in AWS, we recommend using "https://api.hbdm.vn".











Signature Guide
Considering that API requests may get tampered in the process of transmission, to keep the transmission secure, you have to use your API Key to do Signature Authentication for all private interface except for public interface (used for acuqiring basic information and market data), in this way to verify whether the parameters/ parameter value get tampered or not in the process of transmission

A legitimate request consists of following parts：

Request address of method, i.e. visit server address--api.hbdm.com, e.g.: api.hbdm.com/linear-swap-api/v1/swap_order

API Access Key ID (AccessKeyId): Access Key of the API Key that you apply.

Method of Signature (SignatureMethod): The first one is for users to use the elliptic curve digital signature algorithm, using Ed25519. ‌The second, hash-based protocol for user-computed signatures, uses HmacSHA256.

Ed25519 introduction: It is a high-performance digital signature algorithm that provides fast signature verification and generation while having high security.
Signature Version (SignatureVersion): It adopts version 2 in terms of Signature Version.

Timestamp (Timestamp): The time when you send the request (UTC time zone) : (UTC time zone) : (UTC time zone), e.g.: 2017-05-11T16:22:06

Must-fill parameters & optional parameters: For each method, there are a group of must-fill parameters and optional parameters used to address the API request, which can be found in the illustration of each method as well as their meaning. Please note that, in terms of "Get" requests, it needs to do Signature calculation for all the original parameters in each method ; In terms of "Post" requests, no need to do Signature calculation for the original parameters in each method, which means only four parameters need to do Signature calculation in "Post" requests, i.e. AccessKeyId, SignatureMethod, SignatureVersion, Timestamp with other parameters placed in "body".

Signature: The result of Signature calculation which is used to verify if signature is valid and not tampered.

Create API Key
You could create API Key at

API Key consists of the following two parts.

"Access Key", the Key used to visit API.

"Secret Key", the Key used to do Signature authentication and verification (visible during application period).

When create API Key, users could bind IP address, as the validity of unbond IP address is only 90 days.
API Key has operation authorization of trading, borrowing, deposit and withdrawal etc..
Both Access Key and Secret Key are closely related with account security, please do not disclose them to others for any reasons anytime.
Ed25519 Steps for Signature
Normative request for Signature calculation Different contents will get totally different results when use HMAC to calculate Signature, therefore, please normalize the requests before doing Signature calculation. Take the request of inquering order details as an example:

query details of one order

https://api.hbdm.com/linear-swap-api/v1/swap_order?

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

&SignatureMethod=Ed25519

&SignatureVersion=2

&Timestamp=2017-05-11T15:19:30

1. Request methods (GET/POST): add line breaker "\n".
POST\n

2. Text the visit address in lowercase, adding line breake "\n"
api.hbdm.com\n

3. Visit the path of methods, adding line breaker "\n"
/linear-swap-api/v1/swap_order\n

4. Rank the parameter names according to the sequence of ASCII codes, for example, below is the parameters in original sequence and the new sequence:
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=Ed25519

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

Use UTF-8 to encode when it has already been encoded by URI with hexadecimals in Uppercase, e.g., ":" wiil be encoded to "%3A" while space to "%20".Timestamp should be written in the form of YYYY-MM-DDThh:mm:ss and encoded with URI.

5. After ranking
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=Ed25519

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

6. Following the sequence above, link parameters with "&"
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30

7. Form the final character strings that need to do Signature calculation as following:
POST\n

api.hbdm.com\n

/linear-swap-api/v1/swap_order\n

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=Ed25519&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30

8. Use the "request character strings" formed in the last step and your Secret Key to create a digital Signature.
4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=

Use the request string obtained in the previous step to generate the private key of Ed25519 and add it to generate a signature.
Encode the generated signature with base-64, and the resulting value is used as the digital signature of this interface call.
9. Add the digital Signature into the parameters of request path.
The final request sent to Server via API should be like:

https://api.hbdm.com/linear-swap-api/v1/swap_order?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&order-id=1234567890&SignatureMethod=Ed25519&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&Signature=4F65x5A2bLyMWVQj3Aqp%2BB4w%2BivaA7n5Oi2SuYtCJ9o%3D

Add all the must authentication parameters into the parameters of request path;

Add the digital Signature encoded with URL code into the path parameters with the parameter name of "Signature".

HmacSHA256 Steps for Signature
Normative request for Signature calculation Different contents will get totally different results when use HMAC to calculate Signature, therefore, please normalize the requests before doing Signature calculation. Take the request of inquering order details as an example:

query details of one order

https://api.hbdm.com/linear-swap-api/v1/swap_order?

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

&SignatureMethod=HmacSHA256

&SignatureVersion=2

&Timestamp=2017-05-11T15:19:30

1. Request methods (GET/POST): add line breaker "\n".
POST\n

2. Text the visit address in lowercase, adding line breake "\n"
api.hbdm.com\n

3. Visit the path of methods, adding line breaker "\n"
/linear-swap-api/v1/swap_order\n

4. Rank the parameter names according to the sequence of ASCII codes, for example, below is the parameters in original sequence and the new sequence:
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

Use UTF-8 to encode when it has already been encoded by URI with hexadecimals in Uppercase, e.g., ":" wiil be encoded to "%3A" while space to "%20".Timestamp should be written in the form of YYYY-MM-DDThh:mm:ss and encoded with URI.

5. After ranking
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

6. Following the sequence above, link parameters with "&"
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30

7. Form the final character strings that need to do Signature calculation as following:
POST\n

api.hbdm.com\n

/linear-swap-api/v1/swap_order\n

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30

8. Use the "request character strings" formed in the last step and your Secret Key to create a digital Signature.
4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=

Take the request character string formed in the last step and API Secret Key as two parameters, encoding them with the Hash Function HmacSHA256 to get corresponding Hash value.

Encoding the Hash value with base-64 code, the result will be the digital Signature of this request.

9. Add the digital Signature into the parameters of request path.
The final request sent to Server via API should be like:

https://api.hbdm.com/linear-swap-api/v1/swap_order?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&order-id=1234567890&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&Signature=4F65x5A2bLyMWVQj3Aqp%2BB4w%2BivaA7n5Oi2SuYtCJ9o%3D

Add all the must authentication parameters into the parameters of request path;

Add the digital Signature encoded with URL code into the path parameters with the parameter name of "Signature".


Future, Coin Margined Swap,Option Swap and USDT Margined Contracts are using separate API rate limits.

Please note that, for both public interface and private interface, there are rate limits, more details are as below:

Generally, the private interface rate limit of API key is at most 144 times every 3 seconds for each UID (Trade Interface: at most 72 times every 3 seconds. Read Interface: at most 72 times every 3 seconds) (this rate limit is shared by all the altcoins contracts delivered by different date). API Interface List

For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

（2）For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

WebSocket, the private order push interface, requires API KEY Verification:

Each UID can build at most create 30 WS connections for private order push at the same time. For each account, contracts of the same underlying coin only need to subscribe one WS order push, e.g. users only need to create one WS order push connection for BTC Contract which will automatically push orders of BTC-USDTcontracts. Please note that the rate limit of WS order push and RESTFUL private interface are separated from each other, with no relations.

Both read and trade interfaces will return the ratelimit info.You can refer to the following fields of "header" from api response. E.g.,you will get the total Read ratelimit("ratelimit-limit") and the remaining Read ratelimit("ratelimit-remaining") when you query the order info(/linear-swap-api/v1/swap_account_info) , and you will get the total Trade ratelimit("ratelimit-limit") and the remaining Trade ratelimit("ratelimit-remaining") when you place an order(/linear-swap-api/v1/swap_order)). API Interface List

Will response following string for "header" via api

ratelimit-limit: the upper limit of requests per time, unit: times

ratelimit-interval: reset interval (reset the number of request), unit: ms

ratelimit-remaining: the left available request number for this round, unit: times

ratelimit-reset: upper limit of reset time used to reset request number, unit: ms

When API Limitation on Order Cancellation Ratio is triggered,the following string for "header" via api will also be returned:

recovery-time: recovery timestamp, whose unit is millisecond, showing the end time of prohibition, or the access retrieval timestamp;

if you are not in the prohibition period, the field is not included in returned header;


The system will calculate the order cancellation ratio automatically when the total number of orders placed via certain order price types by the API user goes equal to or larger than 3,000 within 10 minutes. If the order cancellation ratio is greater than 99%, the user will be prohibited for 5 minutes from placing orders via certain API order price types which will be listed below (The response of placing orders will return: 1084 Your contract API is disabled, please try again after {0} (GMT+8).).
A 30-minute API order placement prohibition will be triggered if the user was prohibited for 3 times within an hour (The response of placing orders will return: 1084 Your contract API is disabled, please try again after {0} (GMT+8).). After resuming access, the total number of prohibited times will be cleared during the previous period and will not be counted into the total prohibited times in the new period.
Please note that the prohibition from placing orders will cause no effect on order cancellation via API as well as order placement and cancellation via other terminals. We’ll keep you notified on each prohibition via SMS and email.
Only four API order price types will be prohibited which are Limit order, Post_only, FOK and IOC. Please note that you can still use freely other order price types during the banned period, such as Lightning Close, BBO, Optimal 5, Optimal 10 and Optimal 20, opponent_ioc, lightning_ioc, optimal_5_ioc, optimal_10_ioc，optimal_20_ioc，opponent_fok，lightning_fok，optimal_5_fok，optimal_10_fok，optimal_20_fok,etc.
The response header returned by HTTP request:
When placing order by using the four prohibited order price types during the prohibition period, the message header returned by interface will include the field: "recovery-time: recovery timestamp" whose unit is millisecond, showing the end time of prohibition, or the access retrieval timestamp; if you are not in the prohibition period, the field is not included in returned header;
Please note that our system calculates order cancellation ratio according to UID and therefore, the master account UID and sub-accounts UIDs will be counted separately. The calculation period is 10 min/time(The start time starts at 00:00 and the end time is 00:10. Every 10 minutes is a cycle.).
Definition of Indicators：

Order Cancellation Ratio =Total number of invalid cancellation / Total number of placed orders (all types of orders placed via API)
Total number of placed order: Total number of placed orders refers to all orders placed via API which meet these requirements:
1.the order type is placing orders (Order Type = 1),
2.order price types include Limit Order, Post_only, FOK and IOC.
3.order creating time should be within the interval between 3 seconds before the start time of the calculation period and the end time of the calculation period.
Total number of invalid cancellation:Total number of invalid cancellation refers to all cancellation orders placed via API which meet the requirements.
the order type is placing orders (order Type=1),
the order price types are Limit Order, post_only, FOK and IOC.
the order status is “Orders cancelled” (status=7).
order with 0 fulfilled.
the interval between order cancellation and placement should be less than or equal to 3 seconds.
the order cancellation time should be within the calculation period.
In order to ensure stability and transaction performance of API, please try to reduce order cancellation rate and cancellation amount during peak periods to avoid frequent triggering of API restriction mechanism.Suggestions of reducing order cancellation rate are as below:

1. Set orders’ price to BBO prices as close as possible;
2. Prolong the interval properly between each order placement and cancellation;
3. Try to increase your amount for each order and reduce the frequency of order;
4. Try to improve your order fulfillment rate:
（1）Please try to use order prices types that help more on order fulfillment in preference such as BBO, Optimal 5, Optimal 10, Optimal 20, lightning Close, opponent_ioc, lightning_ioc, optimal_5_ioc, optimal_10_ioc，optimal_20_ioc，opponent_fok，lightning_fok，optimal_5_fok，optimal_10_fok，optimal_20_fok, etc.
（2）Try to use best bid/ask price when placing IOC orders, FOK orders and Post_only orders.
5. Please try to extend your request polling cycle when implementing your strategy.



Error Code	Error Details Description
403	invalid ID
1000	System error.
1001	System is unprepared.
1002	Query error.
1003	Abnormal redis operation.
1004	System busy. Please try again later.
1010	Account doesn't exist.
1011	The user's session doesn't exist.
1012	The user's account doesn't exist.
1013	This contract symbol doesn't exist.
1014	This contract doesn't exist.
1015	The index price does not exist.
1016	The bid offer does not exist. Please input the price.
1017	Order doesn't exist.
1018	Main account doesn't exist.
1019	Main account doesn't exist in the sub-account white list.
1020	The number of your sub-account exceeds the maximum. Please contact customer service.
1021	Account open failed. Main account hasn’t opened contract trading account yet.
1030	Input error.
1031	Incorrect form source.
1032	The number of access exceeded the limit.
1033	Incorrect field of contract period.
1034	Incorrect field of order price type.
1035	Incorrect field of form direction.
1036	Incorrect field of open long form.
1037	The leverage is invalid. Please contact the customer service.
1038	The order price exceeds the precision limit, please modify and order again.
1039	Buy price must be lower than {0}{1}. Sell price must exceed {2}{3}.
1040	Invalid amount, please modify and order again.
1041	The order amount exceeds the limit ({0}Cont), please modify and order again.
1042	Current positions have triggered position limits ({0}Cont). Please order after changing the amount.
1043	Current positions have triggered position limits ({0}Cont). Please order after changing the amount.
1044	Current positions have triggered position limits of our platform. Please order after changing the amount.
1045	Unable to switch leverage due to open orders.
1046	Abnormal service. Please try again later.
1047	Insufficient margin available.
1048	Insufficient close amount available.
1049	Open a position with market price is not available.contracts
1050	Customer's order number is repeated. Please try again later.
1051	No orders to cancel.
1052	The number exceeds the batch limit.
1053	Unable to get the latest price range.
1054	Unable to get the latest price.
1055	The price is not reasonable, and the account equity will be less than 0 after placing this order. Please modify the price and place the order.
1056	In settlement. Your order can’t be placed/withdrew currently.
1057	Your order can’t be placed due to trading halt.
1058	Your order can’t be placed due to trade suspension.
1059	In delivery. Your order can’t be placed/withdrew currently.
1060	Your order can’t be placed currently due to abnormal contracts status.
1061	This order doesn't exist.
1062	Cancelling. Please be patient.
1063	The order has been executed.
1064	The main key of order conflicts.
1065	The form number of client isn't an integer.
1066	{0} cannot be empty.
1067	Illegal parameter {0}.
1068	Export error.
1069	The price is not reasonable.
1070	Empty data, cannot be exported.
1071	Repeated cancellation. Your order has been canceled.
1072	Sell price must be lower than {0}{1}.
1073	Position abnormal. Please contact the customer service.
1074	Unable to order currently. Please contact the customer service.
1075	The price is not reasonable, and the margin rate will be less than 0 after placing this order. Please modify the price and place the order.
1076	No orders, please try again later.
1077	In settlement or delivery. Unable to get assets of current contract.
1078	In settlement or delivery. Unable to get assets of some contracts.
1079	In settlement or delivery. Unable to get positions of current contract.
1080	In settlement or delivery. Unable to get positions of some contracts.
1081	The number of your {0} contract trigger orders exceeds the limit {1}.
1082	Trigger type parameter error.
1083	Your position is in the process of forced liquidation. Unable to place order temporarily.
1084	Your contract API is disabled, please try again after {0} (GMT+8).
1085	Trigger order failed, please modify the price and place the order again or contact the customer service.
1086	{0} contract is restricted of opening positions on {1}. Please contact customer service.
1087	{0} contract is restricted of closing positions on {1}. Please contact customer service.
1088	{0} contract is restricted of withdraw order on {1}. Please contact customer service.
1089	Transfer is temporarily restricted for {0} account, please contact customer service support.
1090	Margin rate is lower than 0. Order can’t be placed.
1091	Equity is less than 0. Order can’t be placed.
1092	The Flash Closing Order takes the {0}th price at the order book. After placing an order, the account equity will be less than 0. Please manually enter the price or place an order with the counterparty price.
1093	The Flash Closing Order takes the {0}th price at the order book. The margin rate will be less than 0 after placing an order. Please manually enter the price or place an order with the counterparty price.
1094	The leverage cannot be empty, please switch the leverage or contact customer service
1095	Non-trading state, unable to switch the leverage temporarily
1097	adl freeze status prohibits users from placing orders
1100	Unable to open a position currently. Please contact the customer service.
1101	Unable to close a position currently. Please contact the customer service.
1102	Unable to transfer in currently. Please contact customer service.
1103	Unable to transfer out currently. Please contact customer service.
1104	Trading is prohibited due to contracts trading constraints.
1105	Only Close is available due to contracts trading constraints.
1106	Delivery or settlement in progress, unable to transfer.
1108	Abnormal service. Please try again later.
1109	Sub-account doesn't own the permissions to open positions. Please contact customer service.
1110	Sub-account doesn't own the permissions to close positions. Please contact customer service.
1111	Sub-account doesn't own the permissions to transfer in. Please contact customer service.
1112	Sub-account doesn't own the permissions to transfer out. Please contact customer service.
1113	The sub-account does not have transaction permissions. Please login main account to authorize.
1114	The sub-account does not have transfer permissions. Please login main account to authorize.
1115	You have no access permissions of this sub-account.
1200	Login error. Please try again.
1220	You don’t have access permission as you have not opened contracts trading.
1221	The total balances of Exchange Account can't meet the requirements for opening contracts.
1222	The days of opening account can't meet the requirements for opening contracts.
1223	The VIP level can't meet the requirements for opening contracts.
1224	Your country/region can't meet the requirements for opening contracts.
1225	Failed to open contracts.
1226	Repeated account.
1227	HTX Contract does not support sub-accounts. Please log out sub-account and log in again with primary account.
1228	You have not activated contract trading currently, please activate first.
1229	Cannot agree twice.
1230	You haven't finished the risk verification.
1231	You haven't finished the ID Verification.
1232	The format/size of the image you uploaded does not meet the requirements. Please re-upload.
1233	High leverage is not enabled (Please sign in the APP or web with your main account to agree to the High-Leverage Agreement)
1234	For {0} contracts, the number of the position-opening orders which are not fully filled cannot exceed {1}.
1235	For {0} contracts, the number of the position-closing orders which are not fully filled cannot exceed {1}.
1250	Unable to get the HT_token.
1251	Unable to get BTC assets. Please try again later.
1252	Unable to get currency account assets. Please try again later.
1253	Error in signature verification.
1254	The sub-account has no permission to open futures, please go to the web side to log in the main account and open.
1300	Transfer failed.
1301	Insufficient amount available.
1302	Transfer failed.
1303	The single transfer-out amount must be no less than {0}{1}.
1304	The single transfer-out amount must be no more than {0}{1}.
1305	The single transfer-in amount must be no less than {0}{1}.
1306	The single transfer-in amount must be no more than {0}{1}.
1307	Your accumulative transfer-out amount is over the daily maximum, {0}{1}. You can't transfer out for the time being.
1308	Your accumulative transfer-in amount is over the daily maximum, {0}{1}. You can't transfer in for the time being.
1309	Your accumulative net transfer-out amount is over the daily maximum, {0}{1}. You can't transfer out for the time being.
1310	Your accumulative net transfer-in amount is over the daily maximum, {0}{1}. You can't transfer in for the time being.
1311	The platform's accumulative transfer-out amount is over the daily maximum. You can't transfer out for the time being.
1312	The platform's accumulative transfer-in amount is over the daily maximum. You can't transfer in for the time being.
1313	The platform's accumulative net transfer-out amount is over the daily maximum. You can't transfer out for the time being.
1314	The platform's accumulative net transfer-in amount is over the daily maximum. You can't transfer in for the time being.
1315	Wrong transfer type.
1316	Failed to freeze the transfer.
1317	Failed to unfreeze the transfer.
1318	Failed to confirm the transfer.
1319	Failed to acquire the available transfer amount.
1320	The contract status is abnormal. Transfer is unavailable temporarily.
1321	Transfer failed. Please try again later or contact customer service.
1322	Invalid amount. Must be more than 0.
1323	Abnormal service, transfer failed. Please try again later.
1325	Failed to set trading unit
1326	Failed to obtain trading units
1327	No transfer permission, transfer failed, please contact customer service
1328	No transfer permission, transfer failed, please contact customer service
1329	No transfer permission, transfer failed, please contact customer service
1330	No transfer permission, transfer failed, please contact customer service
1331	Exceeds limit of transfer accuracy (8 digits). Please modify it
1332	The contract doesn't exist.
1333	Failed to open the Maker&Taker agreement
1334	Failed to check the Maker&Taker agreement
1335	Failed to check the second confirmation setting of Maker&Taker
1336	Failed to update the second confirmation setting of Maker&Taker
1337	Failed to check the settings of Maker&Taker
1338	Failed to update the settings of Maker&Taker
1339	Nickname contains illegal words, please modify it
1340	Nickname has been used, please modify it
1341	The enrollment has ended
1342	You cannot set nickname for sub-account
1343	Invalid indicator, please reset
1344	Sorry, {0} contracts can add market reminders currently at most
1345	Sorry, currently {0} can set up to {1} reminders
1346	The indicator already exists, please do not set it repeatedly
1347	{0} parameter is incorrect, please modify.
1348	This contract does not support cross margin mode.
1349	The leverage of the order does not match the leverage of the current position, please switch the leverage first.
1401	order price shall be lower than the strike price.
1403	The number of take-profit and stop-loss orders for {0} contract shall not exceed {1}
1404	Take-profit and stop-loss orders can only be bound with orders for opening a position
1405	The take-profit price shall not be {0}{1}{2}
1406	Your chances of lucky draw have been used up
1407	The stop-loss price shall not be {0}{1}{2}
1408	Unable to cancel because the take-profit and stop-loss order does not take effect.
1409	You have no access to set a take-profit and stop-loss order, please contact our customer service.
1410	The number of sub-accounts for batch operation cannot exceed {0}
1411	Settlement in progress, unable to query order information.
1412	{0} does not meet with the price precision limit {1}.
1413	You have no access to set a Trailing Stop order, please contact our customer service.
1414	You have not activated the grid trading. Please log in to the Web or APP with your main account, and agree with the protocol to activate the grid trading.
1415	Terminate price (Take-profit/Stop-loss price) cannot be within the range of grid price, please modify!
1416	Exceeds the maximum running time, which is{0} days and {1} hours, please modify!
1417	Exceeds the range of grid quantity, which is ({0} ~ {1}), please modify!
1418	At most {0} grids trading orders can be running at the same time, please cancel other grid trading orders first.
1419	Exceeds the range of initial margin ({0} ~ {1}} {2}).
1420	You have no access to grid trading on HTX Futures, please contact our customer service.
1421	There are open orders or positions of the current contract, please cancel these orders or close these positions first.
1422	The PnL per grid is expected to be less than 0, please modify!
1423	The spread between the lowest and the highest grid price is unreasonable, please modify!
1424	This grid trading has been terminated for other reasons. Therefore, it cannot be modified or manually terminated now.
1425	The callback rate should be {0}{1}, please modify!
1426	The activation price should be {0} the latest price.
1427	The number of your {0} contract trailing stop order orders exceeds the limit {1}.
1428	The coupon for the same type of contract can only be collected once by each user.
1429	Already received; please do not collect again!
1430	Invalid coupon; please refresh!
1431	The system is in maintenance and is expected to resume at {0} (GMT+8).
1432	A grid trading is being initialized or terminated; unable to place an order currently.
1433	The grid trading is terminated caused by placing/canceling order manually; please check “Order History” for details.
1434	Less than the minimum initial margin ({0}{1}), which causes the quantity per grid less than the minimum order quantity, please modify!
1435	The grid has been terminated by you.
1436	The grid trading exceeds the effective duration; terminated automatically.
1437	The grid trading has been terminated for system reasons, please contact our customer service.
1438	The grid trading has been terminated due to the termination condition being triggered.
1439	The grid trading has been terminated due to a liquidation being triggered.
1440	{0} contracts fail to be cancelled.
1441	The trigger price must be lower than the highest termination price and higher than the lowest termination price, please modify!
1442	The effective duration must be a minute longer than the running time, please modify!
1443	Delivery of {0} contract causes grid trading termination.
1450	The risk level you ranked does not support the use of current leverage.
1451	The risk level you ranked does not support the use of current leverage, please log in the main account for checking.
1452	The number of grid orders exceeds the order quantity limits; Unable to place any order temporarily.
1453	The number of all your trigger orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1454	The number of all your take profit and stop loss orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1455	The number of all your trailing stop orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1461	Current positions have triggered position limits ({0}{1}). Please modify.
1462	Current positions have triggered position limits ({0}{1}). Please modify.
12001	Invalid submission time.
12002	Incorrect signature version.
12003	Incorrect signature method.
12004	Private key is expired.
12005	Incorrect IP address.
12006	The submission time can't be empty.
12007	Incorrect public key.
12008	Verification failed.
12009	The user is locked or doesn't exist.











1. Query contract history orders interface: /linear-swap-api/v1/swap_hisorders
To ensure timelines and to reduce latency, users are highly recommended to get contract history orders information faster from server memory using interface “query contract order information” (URL: /linear-swap-api/v1/swap_order_info).

For users who use interface “query contract history orders” (URL: /linear-swap-api/v1/swap_hisorders), please enter as many query conditions as possible (including contract_code, trade_type（recommended to send “0” to query all）, type, status, create_date). Besides, try not to enter a big integer in parameter “create_date”. You are kindly suggested to query one-day data at a time.

2. Query contract match results interface: /linear-swap-api/v1/swap_matchresults
To improve query performance and response speed, please enter as many querying conditions as possible (including contract_code, trade_type（recommended to send “0” to query all）, create_date). Besides, try not to enter a big integer in parameter “create_date”. You are kindly suggested to query one-day data at a time.
3. Query contract financial record interface: /linear-swap-api/v1/swap_financial_record
To improve query performance and response speed, please enter as many querying conditions as possible (including symbol, type(recommended to leave it blank to query all), create_date). Besides, try not to enter a big integer in parameter “create_date”. You are kindly suggested to query one-day data at a time.
4. Query contract order detail interface: /linear-swap-api/v1/swap_order_detail
When querying orders without parameter(such as the parameter: created_at), the query result data may be delayed. It is recommended to pass the two parameters of the interface: created_at (order timestamp) and order_type (order type, default 1), the database will be directly queried, and the query results data will be more timely.

Querying condition “created_at” uses 13-bit long type time stamp (including milliseconds). Querying performance will be improved when accurate time stamps are entered.

For example: the converted time stamp of "2019/10/18 10:26:22" is 1571365582123. The returned ts from interface “contract_order” can be used as time stamp to query corresponding order. 0 is not allowed in parameter “created_at”.

5. WebSocket subscription to Market Depth data:
For acquiring market depth data within 150 steps, you are kindly suggested to use step0, step1, step2, step3, step4, step5, step14, step15, step16, step17；

For acquiring market depth data within 20 steps, you are kindly suggested to use step6, step7, step8, step9, step10, step11, step12, step13, step18, step19；

Since the large volume of pushing 150 steps data every 100ms, WebSocket disconnection may occur frequently if client’s network bandwidth is insufficient or the processing is not in time; therefore, we highly recommend users using step6, step7, step8, step9, step10, step11, step12, step13, step18, step19 to acquire 20 steps data. For instance, subscribing 20 steps data.

{

"sub": "market.BTC-USDT.depth.step6",

"id": "id5"

}

We also suggest that you subscribe incremental market depth data.orderbook event will be checked every 30ms. If there is no orderbook event, you will not receive any orderbook data.you HAVE TO maintain local orderbook data,such as updating your local orderbook bids and asks data.You can subscribe 20 or 150 unmerged data.
{

"sub": "market.BTC-USDT.depth.size_20.high_freq",

"data_type":"incremental",

"id": "id1"

}

6. Place order interface (URL: /linear-swap-api/v1/swap_order) and place a batch of orders interface (URL:/linear-swap-api/v1/swap_batchorder):
We recommend to fill in the parameter “client_order_id”(should be unique from user-side),which can help users to acquire order status and other order information according to the parameter “client_order_id" from

query order information interface (URL: /linear-swap-api/v1/swap_order_info ) when there is no returned information due to network or other problems.

7. The best deployment of program server
It is recommended that place the server in AWS Tokyo C zone and use the api.hbdm.vn domain, which can effectively reduce network disconnection and network timeout.





Q1: Is the API Key for swap and spot the same ?
Yes. The Swap API key and spot API key are same. You can create API using the following link. click here

Q2: Why are APIs disconnected or timeout?
The network connection is unstable if the server locates in China mainland,it is suggested to invoke APIS from a server located in 1c area of AWS Tokyo.

You can use api.btcgateway.pro or api.hbdm.vn to debug for China mainland network.

Q3: Why is the websocket often disconnected?
It seems that most of the abnormal websocket issues (such as disconnect, websocket close )(websocket: close 1006 (abnormal closure))are caused by different network environment. The following measures can effectively reduce websocket issues.

It would be better if the server is located in 1c area of AWS Tokyo with url api.hbdm.vn and implement websocket re-connection mechanism. Both market heartbeat and order heartbeat should response with Pong with different format, following Websocket market heartbeat and account heartbeat requirement.here

Q4: what is the difference between api.hbdm.com and api.hbdm.vn?
The api.hbdm.vn uses AWS's CDN service. it should be more stable and faster for AWS users. The api.hbdm.com uses Cloudflare's CDN service.

Q5: What is the colocation service ? which attention points should we know ?
Actually ,colo corresponds to a vpc node, which directly connects to private network of HTX's future, so it will reduce the latency between the client and the HTX future server (bypassing the CDN)

HTX future and HTX swap have the same colo, so the domain name connecting the USDT Margined Contracts api and the future api are the same.

Note : Colo needs to use api.hbdm.com for signature(authentication) to avoid getting 403 error: Verification failure.

Q6: Why does signature verification return failure (403: Verification failure) ?
The signature process of USDT Margined Contracts is similar to HTX future and coin margined swap . In addition to the following precautions,please refer to the swap or future demo to verify whether the signature is successful. Please check your own signature code after demo verification is successful. The coin margined swap code demo is here. The future code demo is here. The USDT Margined Contracts code demo is here.

Check if the API key is valid and copied correctly.
Check if the IP is in whitelist
Check if th timestamp is UTC time
Check if parameters are sorted alphabetically
Check if the encoding is UTF-8
Check if the signature has base64 encoding
Any method with parameters for GET requests should be signed
Any method with parameters for POST requests don't need to be signed
Check if whether the signature is URI encoded and Hexadecimal characters must be capitalized, such as ":" should be encoded as "%3A", and the space shoule be encoded as "%20"
The authorization of websocket is similar to the authorization of restful interface.Pls note that the json body of the websocket authorization shouldn't be URL encoded
The host in signature text should be the same as the host in your API request.The proxy may change the request host, you can try without proxy;Some http/websocket library may include port in the host, you can try to append port in signature host, like "api.hbdm.com:443"
The hidden text in API Key and Secret Key may have impact on the signature.
If the reason for signature failure has not been found through the above methods. And you can confirm that by this demo which is specially explaining the signature.

Q7: Is the ratelimit of public market based on IP ? Is the ratelimit of interface with private key based on UID?
Yes. The ratelimit of interface with private key is based on the UID, not the API key. The master and sub accounts are separately ratelimited and don't affect each other.

Q8: Is there any recommendation for third-party framework which integrates HTX swap?
There is an open source asynchronous quantization framework which integrates HTX future and HTX swap: here. If you have any quetsions, please open a ticket in github issues.





Q1: What is the USDT Margined Swap funding rate settlement cycle? Which interface can be used to check the status when the fund rate is settled?
We warmly remind you that HTX USDT Margined Swap is settled every 8 hours, 4 hours, or 1 hour, depending on the specific instrument. You can refer to the `settlement_period` field in the /linear-swap-api/v1/swap_contract_info ([General] Query Contract Info) for details.

（1）Orders can't be placed or cancelled during settlement period, error code "1056" will be returned if users place or cancel orders.

You are recommended to request contract information by this two ways:

restful, every few seconds during settlement period to access: /linear-swap-api/v1/swap_contract_info
websocket, Subscribe Contract Info (no authentication): public.$symbol.contract_info
It's in settlement time if there is any number of 5, 6, 7, 8 included in the returned status code of contract_status, while it indicates that settlement completed and users could place and cancel orders as usual if the returned status code is 1.

（2）When querying fund or position information during the settlement period, error codes will be returned. Error code and their meaning are as following:

Error code "1077" indicates that "the fund query of current perpetual swap trading pair failed during the settlement";
Error code "1078" indicates that "the fund query of part of perpetual swap trading pairs failed during the settlement";
Error code "1079" indicates that "the position query of current perpetual swap trading pair failed during the settlement";
Error code "1080" indicates that "the position query of part of perpetual swap trading pairs failed during the settlement";
You are recommended to read the status code from the returned message. If the above four types of status code appear, the returned data is not accurate and couldn't be used as reference.

Q2: How to query the system status of the exchange?
There are two common statuses of the exchange systems: settlement/delivery in progress; suspended for maintenance; when the system is in these two kinds of statuses, the system will return the response error code and error information when calling the related API interfaces.

a. How to judge whether the settlement/delivery has been done?

Users can judge from the value “contract_status” returned by the “Get Information of an Order” interface (/linear-swap-api/v1/swap_contract_info);

or Subscribe Contract Info (no authentication): public.$symbol.contract_info

If the return parameter contract_status is 1, it means that the settlement/delivery has been done and the trading has been resumed now.

b. How to judge whether the system is suspended for maintenance or not?

Users can judge from the value “heartbeat” pushed by the “Queried if system interface is available” interface (https://api.hbdm.com/heartbeat/)

or the “Subscribe system status updates” interface ("topic: public.$service.heartbeat");

If the return parameter heartbeat is 1, it means that the system is available now and can be connected normally.






Error Code	Error Details Description
403	invalid ID
1000	System error.
1001	System is unprepared.
1002	Query error.
1003	Abnormal redis operation.
1004	System busy. Please try again later.
1010	Account doesn't exist.
1011	The user's session doesn't exist.
1012	The user's account doesn't exist.
1013	This contract symbol doesn't exist.
1014	This contract doesn't exist.
1015	The index price does not exist.
1016	The bid offer does not exist. Please input the price.
1017	Order doesn't exist.
1018	Main account doesn't exist.
1019	Main account doesn't exist in the sub-account white list.
1020	The number of your sub-account exceeds the maximum. Please contact customer service.
1021	Account open failed. Main account hasn’t opened contract trading account yet.
1030	Input error.
1031	Incorrect form source.
1032	The number of access exceeded the limit.
1033	Incorrect field of contract period.
1034	Incorrect field of order price type.
1035	Incorrect field of form direction.
1036	Incorrect field of open long form.
1037	The leverage is invalid. Please contact the customer service.
1038	The order price exceeds the precision limit, please modify and order again.
1039	Buy price must be lower than {0}{1}. Sell price must exceed {2}{3}.
1040	Invalid amount, please modify and order again.
1041	The order amount exceeds the limit ({0}Cont), please modify and order again.
1042	Current positions have triggered position limits ({0}Cont). Please order after changing the amount.
1043	Current positions have triggered position limits ({0}Cont). Please order after changing the amount.
1044	Current positions have triggered position limits of our platform. Please order after changing the amount.
1045	Unable to switch leverage due to open orders.
1046	Abnormal service. Please try again later.
1047	Insufficient margin available.
1048	Insufficient close amount available.
1049	Open a position with market price is not available.contracts
1050	Customer's order number is repeated. Please try again later.
1051	No orders to cancel.
1052	The number exceeds the batch limit.
1053	Unable to get the latest price range.
1054	Unable to get the latest price.
1055	The price is not reasonable, and the account equity will be less than 0 after placing this order. Please modify the price and place the order.
1056	In settlement. Your order can’t be placed/withdrew currently.
1057	Your order can’t be placed due to trading halt.
1058	Your order can’t be placed due to trade suspension.
1059	In delivery. Your order can’t be placed/withdrew currently.
1060	Your order can’t be placed currently due to abnormal contracts status.
1061	This order doesn't exist.
1062	Cancelling. Please be patient.
1063	The order has been executed.
1064	The main key of order conflicts.
1065	The form number of client isn't an integer.
1066	{0} cannot be empty.
1067	Illegal parameter {0}.
1068	Export error.
1069	The price is not reasonable.
1070	Empty data, cannot be exported.
1071	Repeated cancellation. Your order has been canceled.
1072	Sell price must be lower than {0}{1}.
1073	Position abnormal. Please contact the customer service.
1074	Unable to order currently. Please contact the customer service.
1075	The price is not reasonable, and the margin rate will be less than 0 after placing this order. Please modify the price and place the order.
1076	No orders, please try again later.
1077	In settlement or delivery. Unable to get assets of current contract.
1078	In settlement or delivery. Unable to get assets of some contracts.
1079	In settlement or delivery. Unable to get positions of current contract.
1080	In settlement or delivery. Unable to get positions of some contracts.
1081	The number of your {0} contract trigger orders exceeds the limit {1}.
1082	Trigger type parameter error.
1083	Your position is in the process of forced liquidation. Unable to place order temporarily.
1084	Your contract API is disabled, please try again after {0} (GMT+8).
1085	Trigger order failed, please modify the price and place the order again or contact the customer service.
1086	{0} contract is restricted of opening positions on {1}. Please contact customer service.
1087	{0} contract is restricted of closing positions on {1}. Please contact customer service.
1088	{0} contract is restricted of withdraw order on {1}. Please contact customer service.
1089	Transfer is temporarily restricted for {0} account, please contact customer service support.
1090	Margin rate is lower than 0. Order can’t be placed.
1091	Equity is less than 0. Order can’t be placed.
1092	The Flash Closing Order takes the {0}th price at the order book. After placing an order, the account equity will be less than 0. Please manually enter the price or place an order with the counterparty price.
1093	The Flash Closing Order takes the {0}th price at the order book. The margin rate will be less than 0 after placing an order. Please manually enter the price or place an order with the counterparty price.
1094	The leverage cannot be empty, please switch the leverage or contact customer service
1095	Non-trading state, unable to switch the leverage temporarily
1100	Unable to open a position currently. Please contact the customer service.
1101	Unable to close a position currently. Please contact the customer service.
1102	Unable to transfer in currently. Please contact customer service.
1103	Unable to transfer out currently. Please contact customer service.
1104	Trading is prohibited due to contracts trading constraints.
1105	Only Close is available due to contracts trading constraints.
1106	Delivery or settlement in progress, unable to transfer.
1108	Abnormal service. Please try again later.
1109	Sub-account doesn't own the permissions to open positions. Please contact customer service.
1110	Sub-account doesn't own the permissions to close positions. Please contact customer service.
1111	Sub-account doesn't own the permissions to transfer in. Please contact customer service.
1112	Sub-account doesn't own the permissions to transfer out. Please contact customer service.
1113	The sub-account does not have transaction permissions. Please login main account to authorize.
1114	The sub-account does not have transfer permissions. Please login main account to authorize.
1115	You have no access permissions of this sub-account.
1200	Login error. Please try again.
1220	You don’t have access permission as you have not opened contracts trading.
1221	The total balances of Exchange Account can't meet the requirements for opening contracts.
1222	The days of opening account can't meet the requirements for opening contracts.
1223	The VIP level can't meet the requirements for opening contracts.
1224	Your country/region can't meet the requirements for opening contracts.
1225	Failed to open contracts.
1226	Repeated account.
1227	Huobi Contract does not support sub-accounts. Please log out sub-account and log in again with primary account.
1228	You have not activated contract trading currently, please activate first.
1229	Cannot agree twice.
1230	You haven't finished the risk verification.
1231	You haven't finished the ID Verification.
1232	The format/size of the image you uploaded does not meet the requirements. Please re-upload.
1233	High leverage is not enabled (Please sign in the APP or web with your main account to agree to the High-Leverage Agreement)
1234	For {0} contracts, the number of the position-opening orders which are not fully filled cannot exceed {1}.
1235	For {0} contracts, the number of the position-closing orders which are not fully filled cannot exceed {1}.
1250	Unable to get the HT_token.
1251	Unable to get BTC assets. Please try again later.
1252	Unable to get currency account assets. Please try again later.
1253	Error in signature verification.
1254	The sub-account has no permission to open futures, please go to the web side to log in the main account and open.
1300	Transfer failed.
1301	Insufficient amount available.
1302	Transfer failed.
1303	The single transfer-out amount must be no less than {0}{1}.
1304	The single transfer-out amount must be no more than {0}{1}.
1305	The single transfer-in amount must be no less than {0}{1}.
1306	The single transfer-in amount must be no more than {0}{1}.
1307	Your accumulative transfer-out amount is over the daily maximum, {0}{1}. You can't transfer out for the time being.
1308	Your accumulative transfer-in amount is over the daily maximum, {0}{1}. You can't transfer in for the time being.
1309	Your accumulative net transfer-out amount is over the daily maximum, {0}{1}. You can't transfer out for the time being.
1310	Your accumulative net transfer-in amount is over the daily maximum, {0}{1}. You can't transfer in for the time being.
1311	The platform's accumulative transfer-out amount is over the daily maximum. You can't transfer out for the time being.
1312	The platform's accumulative transfer-in amount is over the daily maximum. You can't transfer in for the time being.
1313	The platform's accumulative net transfer-out amount is over the daily maximum. You can't transfer out for the time being.
1314	The platform's accumulative net transfer-in amount is over the daily maximum. You can't transfer in for the time being.
1315	Wrong transfer type.
1316	Failed to freeze the transfer.
1317	Failed to unfreeze the transfer.
1318	Failed to confirm the transfer.
1319	Failed to acquire the available transfer amount.
1320	The contract status is abnormal. Transfer is unavailable temporarily.
1321	Transfer failed. Please try again later or contact customer service.
1322	Invalid amount. Must be more than 0.
1323	Abnormal service, transfer failed. Please try again later.
1325	Failed to set trading unit
1326	Failed to obtain trading units
1327	No transfer permission, transfer failed, please contact customer service
1328	No transfer permission, transfer failed, please contact customer service
1329	No transfer permission, transfer failed, please contact customer service
1330	No transfer permission, transfer failed, please contact customer service
1331	Exceeds limit of transfer accuracy (8 digits). Please modify it
1332	The contract doesn't exist.
1333	Failed to open the Maker&Taker agreement
1334	Failed to check the Maker&Taker agreement
1335	Failed to check the second confirmation setting of Maker&Taker
1336	Failed to update the second confirmation setting of Maker&Taker
1337	Failed to check the settings of Maker&Taker
1338	Failed to update the settings of Maker&Taker
1339	Nickname contains illegal words, please modify it
1340	Nickname has been used, please modify it
1341	The enrollment has ended
1342	You cannot set nickname for sub-account
1343	Invalid indicator, please reset
1344	Sorry, {0} contracts can add market reminders currently at most
1345	Sorry, currently {0} can set up to {1} reminders
1346	The indicator already exists, please do not set it repeatedly
1347	{0} parameter is incorrect, please modify.
1348	This contract does not support cross margin mode.
1349	The leverage of the order does not match the leverage of the current position, please switch the leverage first.
1401	order price shall be lower than the strike price.
1403	The number of take-profit and stop-loss orders for {0} contract shall not exceed {1}
1404	Take-profit and stop-loss orders can only be bound with orders for opening a position
1405	The take-profit price shall not be {0}{1}{2}
1406	Your chances of lucky draw have been used up
1407	The stop-loss price shall not be {0}{1}{2}
1408	Unable to cancel because the take-profit and stop-loss order does not take effect.
1409	You have no access to set a take-profit and stop-loss order, please contact our customer service.
1410	The number of sub-accounts for batch operation cannot exceed {0}
1411	Settlement in progress, unable to query order information.
1412	{0} does not meet with the price precision limit {1}.
1413	You have no access to set a Trailing Stop order, please contact our customer service.
1414	You have not activated the grid trading. Please log in to the Web or APP with your main account, and agree with the protocol to activate the grid trading.
1415	Terminate price (Take-profit/Stop-loss price) cannot be within the range of grid price, please modify!
1416	Exceeds the maximum running time, which is{0} days and {1} hours, please modify!
1417	Exceeds the range of grid quantity, which is ({0} ~ {1}), please modify!
1418	At most {0} grids trading orders can be running at the same time, please cancel other grid trading orders first.
1419	Exceeds the range of initial margin ({0} ~ {1}} {2}).
1420	You have no access to grid trading on Huobi Futures, please contact our customer service.
1421	There are open orders or positions of the current contract, please cancel these orders or close these positions first.
1422	The PnL per grid is expected to be less than 0, please modify!
1423	The spread between the lowest and the highest grid price is unreasonable, please modify!
1424	This grid trading has been terminated for other reasons. Therefore, it cannot be modified or manually terminated now.
1425	The callback rate should be {0}{1}, please modify!
1426	The activation price should be {0} the latest price.
1427	The number of your {0} contract trailing stop order orders exceeds the limit {1}.
1428	The coupon for the same type of contract can only be collected once by each user.
1429	Already received; please do not collect again!
1430	Invalid coupon; please refresh!
1431	The system is in maintenance and is expected to resume at {0} (GMT+8).
1432	A grid trading is being initialized or terminated; unable to place an order currently.
1433	The grid trading is terminated caused by placing/canceling order manually; please check “Order History” for details.
1434	Less than the minimum initial margin ({0}{1}), which causes the quantity per grid less than the minimum order quantity, please modify!
1435	The grid has been terminated by you.
1436	The grid trading exceeds the effective duration; terminated automatically.
1437	The grid trading has been terminated for system reasons, please contact our customer service.
1438	The grid trading has been terminated due to the termination condition being triggered.
1439	The grid trading has been terminated due to a liquidation being triggered.
1440	{0} contracts fail to be cancelled.
1441	The trigger price must be lower than the highest termination price and higher than the lowest termination price, please modify!
1442	The effective duration must be a minute longer than the running time, please modify!
1443	Delivery of {0} contract causes grid trading termination.
1450	The risk level you ranked does not support the use of current leverage.
1451	The risk level you ranked does not support the use of current leverage, please log in the main account for checking.
1452	The number of grid orders exceeds the order quantity limits; Unable to place any order temporarily.
1453	The number of all your trigger orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1454	The number of all your take profit and stop loss orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1455	The number of all your trailing stop orders exceeds the limit set by the platform; Unable to place any orders temporarily.
1484	Reverse order involves Reduce Only order.
1485	One-way mode is unavailable for grid trading.
1486	One-way mode is unavailable temporarily.
1487	We are sorry you have no access to one-way mode.
1488	Opening positions is unavailable in one-way mode temporarily.
1489	Closing positions is unavailable in one-way mode temporarily.
1490	Opening after closing exceeds the limit (conts).
1491	Reduce Only order parameter error!
1492	Amount of Reduce Only order exceeds the amount available to close.
1493	Position mode cannot be adjusted for open orders.
1494	Position mode cannot be adjusted for existing positions.
1495	Position mode cannot be adjusted for open grid orders.
1496	Position mode cannot be adjusted due to the contract’s non-trading status.
1497	Position mode parameter passing error!
1498	Margin account incorrect!
1499	Hedge mode currently; Unavailable to place orders in one-way mode.
1500	One-way mode currently; Unavailable to place orders in hedge mode.
12001	Invalid submission time.
12002	Incorrect signature version.
12003	Incorrect signature method.
12004	Private key is expired.
12005	Incorrect IP address.
12006	The submission time can't be empty.
12007	Incorrect public key.
12008	Verification failed.
12009	The user is locked or doesn't exist.




Q1: How often are the snapshot orderbook subscription and incremental orderbook subscription pushed?
The snapshot orderbook subscription(market.$contract_code.depth.$type) is checked once every 100MS.If there is an update,it will be pushed. It will be pushed at least 1 second.The incremental orderbook subscription is checked once every 30MS.If there is an update,it will be pushed.If there is no update, it will not be pushed.

Q2: How often is the market trade subscription pushed?
The market trade subscription will be pushed when there is a transaction.

Q3: Are there historical Kline data or historical market trade data?
The historical kline data can be obtained via API interface /market/history/kline with the request params from, to (the time period cannot exceed two years). And the qty of data records cannot be exceeding 2000 in each time.

The historical trade data can be obtained by subscribing the websocket topic: market.$symbol.trade.detail

or can be downloaded from download historical market data

But also, you can download that data using The demo of downloading historical market data

Q4: How to get MACD and other technical indicators on Kline?
The API does not have interfaces to get technical indicators such as MACD. You can refer to TradingView and other websites to calculate them.

Q5: What is the definition of timestamp in the document?
The timestamp in the document refers to the total number of seconds or total milliseconds from Greenwich Mean Time, January 1, 1970, 00:00:00 (Beijing Time, January 1, 1970, 08:00:00) to the present.

Q6: What is the definition of the 150 level and 20 level of MBP?
The Subscription of MBP data: market.$contract_code.depth.$type.150 price level means the current bids and asks splited into 150 level by price.20 price level means the current bids and asks splited into 20 level by price.

Q7: What is the meaning of merged depth when subscribing MBP data?
The subscrpition of MBP data:market.$contract_code.depth.$type：

step16 and step18 are merged by 7 decimal places.bids down,asks up.step17 and step19 are merged by 6 decimal places.bids down,asks up.step1 and step7 are merged by 5 decimal places.bids down,asks up.step2 and step8 are merged by 4 decimal places.bids down,asks up.step3 and step9 are merged by 3 decimal places.bids down,asks up.step4 and step10 are merged by 2 decimal places.bids down,asks up.step5 and step11 are merged by 1 decimal places.bids down,asks up.step12 and step14 are combined by single digit.bids down,asks up.step13 and step15 are combined by tens.bids down,asks up.

Example:

step4(0.01):

bids price: 100.123, 100.245.The merged bids price are 100.12, 100.24.

asks price: 100.123, 100.245The merged asks price are 100.13, 100.25.

("Down" and "Up" are rounded up or down, if the price is down, the asks price is not rounded down, and the bids price is rounded up.)

150 price level: step0 to step5, step14 to step17；

20 price level: step6 to step13, step18, step19;

More examples：

step1(0.00001):

price: 1.123456The merged bid price is 1.12345.The merged ask price is 1.12346.

step7(0.00001):

price: 1.123456The merged bid price is 1.12345.The merged ask price is 1.12346.

step6(0.000001)

price: 1.123456The merged bid price is 1.123456.The merged ask price is 1.123456.

step11(0.1):

price: 1.123456The merged bid price is 1.1.The merged ask price is 1.1.

Q8:Does websocket's position channel push full data or incrementall data each time?
Subscription of position event: "positions.BTC-USDT".The latest position is pushed,including the volumes, available volumes, frozen volumes.If there is no update,it will not be pushed.

Q9: Does websocket's position channel push data when the unrealized profit is updated?
Subscription of position event: "positions.BTC-USDT".It will not be pushed if only unrealized profit is updated.It will be pushed only when position event is updated.

Q10: What is the difference between market detail and trade detail in WS?
Market Detail(market.$contract_code.detail) is the merged market data. It will be checked every 0.5s,pushed once trade event updates,including the OHLCV data,etc.Trade Detail(market.$contract_code.trade.detail) is pushed once trade event updates,including trade price, trade volume, trade direction,etc.

Q11: What is the meaning of the two ts pushed by subscription of incremental MBP ?
Subscription of incremental MBP：market.$contract_code.depth.size_${size}.high_freq，The outer ts is the timestamp when the market server sends the data.The inner ts is the timestamp when the orderbook is checked.

Q12: What is the difference between websocket subscription of MBP and incremental MBP? How often is the incremental MBP pushed?
market.$contract_code.depth.$type is snapshot MBP data，market.$contract_code.depth.size_${size}.high_freq is incremental MBP data.Snapshot MBP data is checked every 100ms,pushed at least every 1s.Incremental MBP data is checked every 30ms.It will not be pushed,if MBP has no update.

Q13: How to maintain local MBP data subscribing incremental MBP:market.$contract_code.depth.size_${size}.high_freq?
Snapshot MBP data will be pushed for the first time, and the incremental MBP data will be pushed afterwards.

(1) Compare the incremental price with the previous full MBP data, and replace the order amount with the same price;

(2) If the price is not in the local MBP data,add the price to the local MBP data;

(3) If a price level is gone, data such as [8100, 0] will be pushed.You have to remove the same price of local MBP data;

(4) For the same websocket connection, the incremental data version is incremented; if the version is not incremented, you need to re-subscribe and re-maintain the local full MBP data;

Q14: What's the difference between "funding_rate" and "realized_rate" in the response of /linear-swap-api/v1/swap_historical_funding_rate interface?
Generally, "funding_rate" is equal to "realized_rate".Only when the payment of funding fee will cause the liquidation of the user's position, the funding fee is under or not charged(And the fee is the actual funding fee:"realized_rate").The current funding rate:"funding_rate" remains unchanged.

Q15: When subscribing the same topic of several contract codes, will several ws be needed?
Since Futures, Coin Margined swaps, USDT Margined Contracts and Options are different contracts with different interface addresses, different ws will be needed.

In Futures, Coin Margined swaps, USDT Margined Contracts and Options thereof, as long as the interface address is the same, one ws is enough.

Q16: Is it available to place/cancel an order via WS??
Currently, it is not supported.

Q17: How to subscribe order status?
a. Successfully trade: “Subscribe Match Order Data (matchOrders.$contract_code)” or “Subscribe Order Data (orders.$contract_code)”

b. Successfully cancel: Subscribe Account Equity Updates Data (accounts.$contract_code)

Q18: What is the difference between the “Subscribe Match Order Data (matchOrders.$contract_code)” and “Subscribe Order Data (orders.$contract_code)”?
The pushed data of these two interfaces are different. Compared to “Subscribe Match Order Data (matchOrders.$contract_code)”, there are more fields for “Subscribe Order Data (orders.$contract_code)”

In general, the match order data (Subscribe Match Order Data “matchOrders.$contract_code”) may be pushed faster than the settled order data (Subscribe Order Data “orders.$contract_code”).

The orders of forced liquidation and netting will not be pushed in “Subscribe Match Order Data (matchOrders.$contract_code)”

Q19: How often is the “Subscribe Kline Data (market.$contract_code.kline.$period)” pushed?
If any transaction is completed, it will push every 500ms. If not, it will push according to the subscribe period

Q20: How to judge whether the push is delayed?
Please first synchronize the time of the server through https://api.hbdm.com/api/v1/timestamp), and the “ts” in the returned data is timestamp (ms) and the corresponding time zone is UTC+8.

The outer layer of each pushed data has a “ts”, which represents the time stamp (ms) when the server pushes the data to the client and the corresponding time zone is UTC+8.

When the data pushed arrive, the procedure will record the local time “ts”. When the local time “ts” is much later than the pushing data “ts”, you can use the following methods to improve the delay:

a. Reduce the data pushed by reducing the number of WS subscriptions.

b. Check the stability and speed of the network between procedure and the servers (please replace api.btcgateway.pro with the domain name used by the program)

curl -o /dev/null -s -w time_namelookup"(s)":%{time_namelookup}"\n"time_connect"(s)":%{time_connect}"\n"time_starttransfer"(s)":%{time_starttransfer}"\n"time_total"(s)":%{time_total}"\n"speed_download"(B/s)":%{speed_download}"\n" api.btcgateway.pro

and you will receive data as below:

time_namelookup(s):0.001378

time_connect(s):0.128641

time_starttransfer(s):0.276588

time_total(s):0.276804

speed_download(B/s):2010.000

If you run the above command multiple times in a row, and the results obtained each time are very different, you can: a. Select an appropriate HTX domain name, b. Optimize or reselect the network where the program is located.











When you report an API error, you need to attach your request URL, the original complete body of the request and the complete request URL parameters, and the original complete log of the server's response. If it is a websocket subscription, you need to provide the address of the subscription, the topic of the subscription, and the original complete log pushed by the server.

If it is an order-related issue, use the API order query interface /linear-swap-api/v1/swap_order_info to keep the complete log returned and provide your UID and order number.















/linear-swap-api/v1/swap_funding_rate ([General] Query funding rate)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive."BTC-USDT" ...
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 false	response status	"ok" , "error"
ts	long	 false	response timestamp.unit:millionSeconds.	
<data>		 false		
symbol	string	 false	symbol	"BTC","ETH"...
contract_code	string	 false	contract code,eg:"BTC-USDT"	
fee_asset	string	 false	fee asset	eg:"BTC","ETH"...
funding_time	string	 false	current funding time	
funding_rate	string	 false	current funding rate（Updated once a minute）	
estimated_rate	string	 false	(Deprecated, default is null)	
next_funding_time	string	 false	(Deprecated, default is null)	
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_fund
ing_rate?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":{
"funding_rate":"0.000100000000000000"
"contract_code":"BTC-USDT"
"symbol":"BTC"
"fee_asset":"BTC"
"funding_time":"1603699200000"
"estimated_rate":"null"
"next_funding_time":"null"
}
"ts":1603696494714
}





/linear-swap-api/v1/swap_batch_funding_rate ([General]Query a Batch of Funding Rate)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code，if not filled in, default as all	"BTC-USDT" ...
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	the result of server handles for the request	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>	object array	 true		
symbol	string	 true	symbol	
contract_code	string	 true	contract code	"BTC-USDT" ...
fee_asset	string	 true	fee asset	"USDT...
funding_time	string	 true	current funding time(Millisecond)	
funding_rate	string	 true	current funding rate（Updated once a minute）	
estimated_rate	string	 true	(Deprecated, default is null)	
next_funding_time	string	 true	(Deprecated, default is null)	
</data>		 false		
Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_batch_funding_rate?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"funding_rate":"-0.007500000000000000"
"contract_code":"ETC-USDT"
"symbol":"ETC"
"fee_asset":"USDT"
"funding_time":"1613976000000"
"estimated_rate":"null"
"next_funding_time":"null"
}
1:{
"funding_rate":"-0.007500000000000000"
"contract_code":"ADA-USDT"
"symbol":"ADA"
"fee_asset":"USDT"
"funding_time":"1613976000000"
"estimated_rate":"null"
"next_funding_time":"null"
}
]
"ts":1614045373795
}






/linear-swap-api/v1/swap_historical_funding_rate ([General] Query historical funding rate)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.eg:"BTC-USDT" ...
page_index	int	 false	page index. 1 by default	
page_size	int	 false	page size.20 by default. 50 at most	[1-50]
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 false	response status	"ok" , "error"
ts	long	 false	response timestamp.unit:millionSeconds.	
<data>		 false		
symbol	string	 false	symbol	eg:"BTC","ETH"...
contract_code	string	 false	contract code	eg: "BTC-USDT
fee_asset	string	 false	fee asset	eg:"USDT"
funding_time	string	 false	funding time	
funding_rate	string	 false	funding rate	
realized_rate	string	 false	(Deprecated, default is null)	
avg_premium_index	string	 false	average premium index	
</data>		 false		
total_page	int	 false	total page	
current_page	int	 false	current page	
total_size	int	 false	total size	
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_historical_funding_rate?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":{
"total_page":14
"current_page":1
"total_size":14
"data":[
0:{
"avg_premium_index":"0.000049895833333333"
"funding_rate":"0.000100000000000000"
"funding_time":"1603670400000"
"realized_rate":"null"
"contract_code":"BTC-USDT"
"symbol":"BTC"
"fee_asset":"USDT"
}
]
}
"ts":1603696680599
}





/linear-swap-api/v3/swap_liquidation_orders ([General] Query Liquidation Orders(New))
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.
The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.
one of pair and contract_code must be filled in; and all filled in, the contract_code is the preferred.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
contract	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.e.g. "BTC-USDT"	
pair	string	 false	pair	BTC-USDT	
trade_type	int	 true	trade type	0:All; 1: Open long; 2: Open short; 3: Close short; 4: Close long; 5: Liquidate long positions; 6: Liquidate short positions, 17:buy(one-way mode), 18:sell(one-way mode)	
start_time	long	 false	Query start time, query by data creation time	Value range [((end-time) – 2h), (end-time)], maximum query window size is 2 hours, query window shift should be within past 90 days.	
end_time	long	 false	Query end time, query data by creation time	Value range [(present-90d), present], maximum query window size is 48 hours, query window shift should be within past 90 days.	now
direct	string	 false	Search direct, If the direction is NEXT, the data is returned in positive chronological order; if the direction is PREV, the data is returned in reverse chronological order	next, prev default is prev	next
from_id	long	 false	If the query direction is prev, from_id should be the min query_id in the last query result. If the query direction is next, from_id should be the max query_id in the last query result	Search query_id to begin with	
Response Parameter
Parameter	Data Type	Required	Description	Value Range
code	int	 true	State code	
msg	string	 true	The code description	
ts	long	 true	Timestamp	
<data>	object array	 true		
query_id	long	 true	Query id, which can be used as the from_id field for the next query request.	
symbol	string	 true	symbol	
contract_code	string	 true	contract code	e.g. swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
created_at	long	 true	liquidation time	
direction	string	 true		"buy":buy"sell": sell
offset	string	 true		"open":open "close": close, "both"
volume	decimal	 true	liquidation volume (cont)	
amount	decimal	 true	liquidation amount (token)	
price	decimal	 true	bankruptcy price	
trade_turnover	decimal	 true	liquidation amount (quotation token)	
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
</data>		 false		
Request example
curl"/linear-swap-api/v3/swap_liquidation_orders?trade_type=5&contract=BTC-USDT"
Response Example
Success Example
{
"code":200
"msg":""
"data":[
0:{
"query_id":452057
"contract_code":"BTC-USDT-211210"
"symbol":"USDT"
"direction":"sell"
"offset":"close"
"volume":479
"price":51441.7
"created_at":1638593647864
"amount":0.479
"trade_turnover":24640.5743
"business_type":"futures"
"pair":"BTC-USDT"
}
]
"ts":1604312615051
}



/linear-swap-api/v1/swap_settlement_records ([General] Query historical settlement records of the platform interface)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	Contract Code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
start_time	long	 false	Start time（timestamp，unit: millisecond）	Value range: [(Current time minus 90 days), Current time] ，default current time minus 90 days
end_time	long	 false	End time（timestamp，unit: millisecond）	Value range: (start_time, current time)，default current time
page_index	int	 false	Page, default page 1 if not filled	
page_size	int	 false	Page items, default 20, shall not exceed 50	
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
<data>		 false		
symbol	string	 true	Variety code	"BTC", "ETH" ...
volume	decimal	 true	Position quantity(volume). Sum of both buy and sell sides	
amount	decimal	 true	Position quantity(Currency). Sum of both buy and sell sides	
contract_code	string	 true	Contract Code	eg swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
value	decimal	 true	Total position volume（The unit is the denominated currency of the contract. e.g:USDT）	
trade_amount	decimal	 true	trading volume within the last 24 hours (coin). Sum of both buy and sell sides	
trade_volume	decimal	 true	trading volume within the last 24 hours (cont). Sum of both buy and sell sides	
trade_turnover	decimal	 true	trading amount within the last 24 hours. Sum of both buy and sell sides	
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
</data>		 false		
Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_settlement_records?contract_code=BTC-USDT&start_time=xxxxx&end_time=xxx&page_index=xxx&page_size=100"
Response Example
Success Example
{
"status":"ok"
"data":{
"total_page":1
"current_page":1
"total_size":12
"settlement_record":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211203"
"settlement_time":1638518400000
"clawback_ratio":0
"settlement_price":56792.3
"settlement_type":"delivery"
"business_type":"futures"
"pair":"BTC-USDT"
}
1:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211203"
"settlement_time":1638489600000
"clawback_ratio":0
"settlement_price":57028.6
"settlement_type":"settlement"
"business_type":"futures"
"pair":"BTC-USDT"
}
]
}
"ts":1638756873768
}




/linear-swap-api/v1/swap_elite_account_ratio ([General] Query Top Trader Sentiment Index Function-Account)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
period	string	 true	period	5min, 15min, 30min, 60min,4hour,1day
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
period	string	 true	period	5min, 15min, 30min, 60min,4hour,1day
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>		 false		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	e.g. swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<list>		 false		
buy_ratio	decimal	 true	Net long position ratio	
sell_ratio	decimal	 true	Net short position ratio	
ts	long	 true	Time of Respond Generation	
</list>		 false		
</data>		 false		
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>		 false		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	e.g. swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<list>		 false		
buy_ratio	decimal	 true	net long accounts ratio	
sell_ratio	decimal	 true	net short accounts ratio	
locked_ratio	decimal	 true	locked accounts ratio	
ts	long	 true	Time of Respond Generation	
</list>		 false		
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_elite_account_ratio?contract_code=BTC-USDT&period=5min"
Response Example
Success Example
{
"status":"ok"
"data":{
"list":[
0:{
"buy_ratio":0.5
"sell_ratio":0.5
"locked_ratio":0
"ts":1638115200000
}
]
"symbol":"BTC"
"contract_code":"BTC-USDT"
"business_type":"swap"
"pair":"BTC-USDT"
}
"ts":1638169688105
}





/linear-swap-api/v1/swap_elite_position_ratio ([General] Query Top Trader Sentiment Index Function-Position)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
period	string	 true	period	5min, 15min, 30min, 60min,4hour,1day
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>		 false		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	e.g. swap: "BTC-USDT"... , future: "BTC-USDT-FUTURES" ...
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<list>		 false		
buy_ratio	decimal	 true	Net long position ratio	
sell_ratio	decimal	 true	Net short position ratio	
ts	long	 true	Time of Respond Generation	
</list>		 false		
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_elite_position_ratio?contract_code=BTC-USDT&period=1day"
Response Example
Success Example
{
"status":"ok"
"data":{
"list":[
0:{
"buy_ratio":0.5
"sell_ratio":0.5
"ts":1638460800000
}
]
"symbol":"BTC"
"contract_code":"BTC-USDT-FUTURES"
"business_type":"futures"
"pair":"BTC-USDT"
}
"ts":1638756121395
}





/linear-swap-api/v1/swap_api_state ([Isolated] Query information on system status)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: This interface only supports isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code	Case-Insenstive.e.g. "BTC-USDT"
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>	object array	 true		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	Contract Code	"BTC-USDT"...
margin_mode	string	 true	margin mode	isolated : "isolated"
margin_account	string	 true	margin account	"BTC-USDT"...
open	int	 true	open order access：when “1”, then access available; when “0”, access unavailable"1"	
close	int	 true	close order access：when “1”, then access available; when “0”, access unavailable "1"	
cancel	int	 true	order cancellation access：when “1”, then access available; when “0”, access unavailable "1"	
transfer_in	int	 true	deposit access：when “1”, then access available; when “0”, access unavailable "1"	
transfer_out	int	 true	withdraw access： when “1”, then access available; when “0”, access unavailable "1"	
master_transfer_sub	int	 true	transfer from master to sub account："1" is available，“0” is unavailable	
sub_transfer_master	int	 true	transfer from sub to master account："1" is available，“0” is unavailable	
master_transfer_sub_inner_in	int	 true	Transfer_in access for transfer from main account to sub-account - crossing account: "1" represents "available", "0" represents "unavailable"	
master_transfer_sub_inner_out	int	 true	Transfer_out access for transfer from main account to sub-account - crossing account: "1" represents "available", "0" represents "unavailable"	
sub_transfer_master_inner_in	int	 true	Transfer_in access for transfer from sub-account to main account - crossing account: "1" represents "available", "0" represents "unavailable"	
sub_transfer_master_inner_out	int	 true	Transfer_out access for transfer from sub-account to main account - crossing account: "1" represents "available", "0" represents "unavailable"	
transfer_inner_in	int	 true	Transfer_in access for transfer between different margin accounts under the same account："1" represents "available", "0" represents "unavailable"	
transfer_inner_out	int	 true	Transfer_out access for transfer between different margin accounts under the same account："1" represents "available", "0" represents "unavailable"	
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_api_state?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT"
"margin_mode":"isolated"
"margin_account":"BTC-USDT"
"open":1
"close":1
"cancel":1
"transfer_in":1
"transfer_out":1
"master_transfer_sub":1
"sub_transfer_master":1
"master_transfer_sub_inner_in":1
"master_transfer_sub_inner_out":1
"sub_transfer_master_inner_in":1
"sub_transfer_master_inner_out":1
"transfer_inner_in":1
"transfer_inner_out":1
}
]
"ts":1603696366019










/linear-swap-api/v1/swap_cross_ladder_margin ([Cross]Query information on Tiered Margin)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface only supports cross margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code, if not filled in return all contract infomation	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair	BTC-USDT
contract_type	string	 false	contract type	swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	business type, default is swap	futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	result of server handled request	"ok" , "error"
<data>	object array	 true		
symbol	string	 true	symbol	such as: "BTC"
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
margin_mode	string	 true	margin mode	cross
margin_account	string	 true	margin account	such as:USDT”
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<list>	object array	 true		
lever_rate	int	 true	lever rate	
<ladders>	object array	 true	ladders for margin	
min_margin_balance	decimal	 true	min margin balance(the starting point in this ladder, included in this ladder)	
max_margin_balance	decimal	 true	max margin balance(the end point in this ladder, excluded in this ladder, is next ladder's min_margin_balance)	
min_margin_available	decimal	 true	min margin available(in the range of this ladder margin balance)	
max_margin_available	decimal	 true	max margin available（not in the range of this ladder margin balance, is next ladder's min_margin_available)	
</ladders>		 false		
</list>		 false		
</data>		 false		
ts	long	 true	Time of Respond Generation，Unit：Millisecond	
Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_cross_ladder_margin?contract_code=BTC-USDT&pair=BTC-USDT&contract_type=swap&business_type=swap"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"margin_account":"USDT"
"symbol":"BTC"
"contract_code":"BTC-USDT"
"margin_mode":"cross"
"list":[
0:{
"lever_rate":2
"ladders":[
0:{
"min_margin_balance":0
"max_margin_balance":NULL
"min_margin_available":0
"max_margin_available":NULL
}
]
}
]
"business_type":"swap"
"pair":"BTC-USDT"
"contract_type":"swap"
}
]
"ts":1638755685337
}







/linear-swap-api/v1/swap_ladder_margin ([Isolated]Query information on Tiered Margin)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: This interface only supports isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code, if not filled in return all contract infomation	such as: “BTC-USDT”, “ETH-USDT”。。。
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	status	"ok" , "error"
<data>	object array	 true		
symbol	string	 true	symbol	such as: "BTC"
contract_code	string	 true	contract code	such as: "BTC-USDT"
margin_mode	string	 true	margin mode	isolated: isolated
margin_account	string	 true	margin account	such as: “BTC-USDT”
<list>	object array	 true		
lever_rate	int	 true	lever rate	
<ladders>	object array	 true	ladders for margin	
min_margin_balance	decimal	 true	min margin balance(the starting point in this ladder, included in this ladder)	
max_margin_balance	decimal	 true	max margin balance(the end point in this ladder, excluded in this ladder, is next ladder's min_margin_balance)	
min_margin_available	decimal	 true	min margin available(in the range of this ladder margin balance)	
max_margin_available	decimal	 true	max margin available（not in the range of this ladder margin balance, is next ladder's min_margin_available)	
</ladders>		 false		
</list>		 false		
</data>		 false		
ts	long	 true	Time of Respond Generation，Unit：Millisecond	
Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_ladder_margin?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"margin_account":"BTC-USDT"
"symbol":"BTC"
"contract_code":"BTC-USDT"
"margin_mode":"isolated"
"list":[
0:{
"lever_rate":20
"ladders":[
0:{
"min_margin_balance":0
"max_margin_balance":250000
"min_margin_available":0
"max_margin_available":250000
}
1:{
"min_margin_balance":250000
"max_margin_balance":2500000
"min_margin_available":250000
"max_margin_available":1000000
}
2:{
"min_margin_balance":2500000
"max_margin_balance":10000000
"min_margin_available":1000000
"max_margin_available":2500000
}
3:{
"min_margin_balance":10000000
"max_margin_balance":85000000
"min_margin_available":2500000
"max_margin_available":10000000
}
4:{
"min_margin_balance":85000000
"max_margin_balance":NULL
"min_margin_available":10000000
"max_margin_available":NULL
}
]
}
]
}
]
"ts":1612504906880
}





/linear-swap-api/v1/swap_estimated_settlement_price ([General]Get the estimated settlement price)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code, return all without filling in	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair	BTC-USDT
contract_type	string	 false	contract type	swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	business type, default is swap	futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	status	
<data>	object array	 true		
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
estimated_settlement_price	decimal	 true	Current-period estimated settlement price /Current-period estimated delivery price (When the settlement type is "delivery", it is estimated delivery price; Otherwise, it is estimated settlement price)	
settlement_type	string	 true	settlement type	“delivery”，“settlement”
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
</data>		 false		
ts	long	 true	Time of Respond Generation，Unit: Millisecond	
Notes: 
When the "settlement_type" is "settlement", the "estimated_settlement_price" will be calculated and updated from 10 minutes before settlement and until the settlement. In the other moment(including settlement), "estimated_settlement_price" is empty, but the other fields will be displayed normally.
When the "settlement_type" is "delivery", the "estimated_settlement_price" will be calculated and updated from 10 minutes before settlement and until the delivery. In the other moment(including delivery), "estimated_settlement_price" is empty, but the other fields will be displayed normally.
Estimated settlement price will be calculated and updated every 6 seconds.

Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_estimated_settlement_price?contract_code=BTC-USDT&pair=BTC-USDT&contract_type=swap&business_type=swap"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"contract_code":"BTC-USDT-211210"
"estimated_settlement_price":NULL
"settlement_type":"settlement"
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"this_week"
}
1:{
"contract_code":"BTC-USDT-211217"
"estimated_settlement_price":NULL
"settlement_type":"settlement"
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"next_week"
}
2:{
"contract_code":"BTC-USDT-211231"
"estimated_settlement_price":NULL
"settlement_type":"settlement"
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"quarter"
}
3:{
"contract_code":"BTC-USDT"
"estimated_settlement_price":NULL
"settlement_type":"settlement"
"business_type":"swap"
"pair":"BTC-USDT"
"contract_type":"swap"
}
]
"ts":1638755400222
}




linear-swap-api/v1/swap_adjustfactor ([Isolated] Query information on Tiered Adjustment Factor)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: This interface only supports isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code	Case-Insenstive.e.g. "BTC-USDT"
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>		 false		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	e.g. "BTC-USDT"
margin_mode	string	 true	margin mode	isolated : "isolated"
<list>		 false		
lever_rate	decimal	 true	Leverage	
<ladders>		 false		
min_size	decimal	 true	Min net position limit	
max_size	decimal	 true	Max net position limit	
ladder	int	 true	Tier	
adjust_factor	decimal	 true	Adjustment Factor	
</ladders>		 false		
</list>		 false		
</data>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_adjustfactor?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT"
"margin_mode":"isolated"
"list":[
0:{
"lever_rate":125
"ladders":[
0:{
"ladder":0
"min_size":0
"max_size":8999
"adjust_factor":0.65
}
1:{
"ladder":1
"min_size":9000
"max_size":89999
"adjust_factor":0.8
}
2:{
"ladder":2
"min_size":90000
"max_size":NULL
"adjust_factor":0.85
}
]
}
]
}
]
"ts":1603695606565
}





/linear-swap-api/v1/swap_cross_adjustfactor ([Cross] Query Information On Tiered Adjustment Factor)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface only supports cross margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair	BTC-USDT
contract_type	string	 false	contract type	swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	business type, default is swap	futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>	object array	 true		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
margin_mode	string	 true	margin mode	cross: cross margin mode
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<list>	object array	 true		
lever_rate	decimal	 true	lever rate	
<ladders>	object array	 true		
min_size	decimal	 true	min net position limit	
max_size	decimal	 true	max net position limit	
ladder	int	 true	tier	from 0
adjust_factor	decimal	 true	adjustment factor	
</ladders>		 false		
</list>		 false		
</data>		 false		
Request example
curl"https://api.hbdm.com/linear-swap-api/v1/swap_cross_adjustfactor?contract_code=BTC-USDT&pair=BTC-USDT&contract_type=swap&business_type=swap"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211210"
"margin_mode":"cross"
"list":[
0:{
"lever_rate":1
"ladders":[
0:{
"ladder":0
"min_size":0
"max_size":3999
"adjust_factor":0.005
}
1:{
"ladder":1
"min_size":4000
"max_size":39999
"adjust_factor":0.01
}
2:{
"ladder":2
"min_size":40000
"max_size":79999
"adjust_factor":0.015
}
3:{
"ladder":3
"min_size":80000
"max_size":119999
"adjust_factor":0.02
}
4:{
"ladder":4
"min_size":120000
"max_size":NULL
"adjust_factor":0.025
}
]
}
]
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"this_week"
}
]
"ts":1638754992327
}




/linear-swap-api/v1/swap_price_limit ([General] Query Swap Price Limitation)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-201101; When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 false	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair, BTC-USDT
contract_type	string	 false	contract type: swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	business type, default is swap: futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" ,"error"
<data>		 false		
symbol	string	 true	Variety code	"BTC","ETH" ...
high_limit	decimal	 true	Highest Buying Price	
low_limit	decimal	 true	Lowest Selling Price	
contract_code	string	 true	Contract Code	eg swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<data>		 false		
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_price_limit?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT"
"high_limit":49629
"low_limit":47682.8
"business_type":"swap"
"pair":"BTC-USDT"
"contract_type":"swap"
}
1:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211210"
"high_limit":49645.2
"low_limit":47698.5
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"this_week"
}
2:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211217"
"high_limit":49699.7
"low_limit":47750.8
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"next_week"
}
3:{
"symbol":"BTC"
"contract_code":"BTC-USDT-211231"
"high_limit":50135.1
"low_limit":47214.8
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"quarter"
}
]
"ts":1638753887869
}




linear-swap-api/v1/swap_open_interest ([General] Get Swap Open Interest Information)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-201101; When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 false	eg swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair, BTC-USDT
contract_type	string	 false	contract type: swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	business type, default is swap: futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
<data>		 false		
symbol	string	 true	Variety code	"BTC", "ETH" ...
volume	decimal	 true	Position quantity(volume). Sum of both buy and sell sides	
amount	decimal	 true	Position quantity(Currency). Sum of both buy and sell sides	
contract_code	string	 true	Contract Code	eg swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
value	decimal	 true	Total position volume（The unit is the denominated currency of the contract. e.g:USDT）	
trade_amount	decimal	 true	trading volume within the last 24 hours (coin). Sum of both buy and sell sides	
trade_volume	decimal	 true	trading volume within the last 24 hours (cont). Sum of both buy and sell sides	
trade_turnover	decimal	 true	trading amount within the last 24 hours. Sum of both buy and sell sides	
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
</data>		 false		
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_open_interest?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"volume":78696
"amount":78.696
"symbol":"BTC"
"value":3823138.2456
"contract_code":"BTC-USDT"
"trade_amount":0
"trade_volume":0
"trade_turnover":0
"business_type":"swap"
"pair":"BTC-USDT"
"contract_type":"swap"
}
1:{
"volume":10925
"amount":10.925
"symbol":"BTC"
"value":530662.21
"contract_code":"BTC-USDT-211217"
"trade_amount":0
"trade_volume":0
"trade_turnover":0
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"next_week"
}
2:{
"volume":27104
"amount":27.104
"symbol":"BTC"
"value":1316937.2832
"contract_code":"BTC-USDT-211210"
"trade_amount":0
"trade_volume":0
"trade_turnover":0
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"this_week"
}
3:{
"volume":201143
"amount":201.143
"symbol":"BTC"
"value":9775067.0568
"contract_code":"BTC-USDT-211231"
"trade_amount":0
"trade_volume":0
"trade_turnover":0
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"quarter"
}
]
"ts":1638754059540
}




/linear-swap-api/v1/swap_contract_info ([General] Query Contract Info)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "support_margin_mode" should be "all" when querying the contract information which supports the cross margin mode and the isolated margin mode both. The value of "cross" or "isolated" just can query the contract information which only supports the cross margin mode or the isolated margin mode. Please keep attention.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-201101; When both of pair, contract_type and contract_code filled in, the contract_code is the preferred.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

When support_margin_mode is isolated，contract_type, business_type should not be futures type. And when support_margin_mode is cross, the return data is future's data
Notes：contract elements it can display more futures fields, we recommend you to use it.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 false	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
support_margin_mode	string	 false	support margin mode cross："cross"；isolated："isolated"；all："all"
pair	string	 false	BTC-USDT
contract_type	string	 false	swap, this_week, next_week, quarter, next_quarter
business_type	string	 false	futures, swap, all(default is swap)
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
<data>		 false		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	Contract Code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
contract_size	decimal	 true	Contract Value (USDT of one contract)	10, 100...
price_tick	decimal	 true	Minimum Variation of Contract Price	0.001, 0.01...
settlement_date	string	 true	Settlement Date	eg "1490759594752"
settlement_period	string	 true	Perpetual futures contract settlement period Unit: Hour	e.g.: "4" represents 4 hours
create_date	string	 true	Listing Date	eg "20190808"
delivery_time	string	 true	delivery time（When the contract does not need to be delivered, the field value is an empty string），millesecond timestamp	
contract_status	int	 true	Contract Status	contract status ： 0: Delisting,1: Listing,2: Pending Listing,3: Suspension,4: Suspending of Listing,6: Delivering,8: Delivered
support_margin_mode	string	 false	support margin mode	cross："cross"；isolated："isolated"；all："all"
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
delivery_date	string	 true	delivery date, empty string when swap	such as: "20180720"
adjust	object array	 false	Invalid field	
price_estimated	object array	 false	Invalid field	
open_type	int	 false	Invalid field	
trade_partition	string	 true	Invalid field	
</data>		 false		
ts	long	 true	Time of Respond Generation，Unit：Millisecond	
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_contract_info?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT"
"contract_size":0.001
"price_tick":0.1
"delivery_date":""
"delivery_time":""
"create_date":"20201021"
"contract_status":1
"adjust":[]
"price_estimated":[]
"settlement_date":"1764316800000"
"support_margin_mode":"all"
"open_type":0
"settlement_period":"8"
"business_type":"swap"
"pair":"BTC-USDT"
"contract_type":"swap"
"trade_partition":"USDT"
}
]
"ts":1764298317931
}






/linear-swap-api/v1/swap_index ([General] Query Swap Index Price Information)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 false	Case-insenstive."BTC-USDT","ETH-USDT"...
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
<data>		 false		
contract_code	string	 true	contract code	"BTC-USDT","ETH-USDT"...
index_price	decimal	 true	Index Price	
index_ts	Long	 true	Index time	
</data>		 false		
ts	long	 true	Time of Respond Generation，Unit：Millisecond	
Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_index?contract_code=BTC-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"index_price":13076.32986568
"index_ts":1603694592011
"contract_code":"BTC-USDT"
}
]
"ts":1603694596400
}








/linear-swap-api/v1/swap_query_elements ([General]Contract Elements)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: 20 times/2s

Interface description: Get Contract Elements info

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	Contract code, if empty, query all	BTC-USDT...
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 false		ok , "error"
<data>	object array	 true		
contract_code	string	 true	BTC-USDT...	
mode_type	int	 true	Margin Mode: 1: Isolated margin; 2: Cross margin and isolated margin; 3: Cross margin	
swap_delivery_type	int	 true	Type of Futures: 1: USDT-M perpetual futures; 2: USDT-M delivery futures; 3: Both of them	
instrument_index_code	string	 true	index	
real_time_settlement	int	 true	Whether to enable real-time settlement: 0: No; 1: Yes	
transfer_profit_ratio	Number	 true	Available coefficient of isolated margin	
cross_transfer_profit_ratio	Number	 true	Available coefficient of cross margin	
instrument_type	list	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
trade_partition	String	 true	trade partition USDT HUSD	
min_level	int	 true	min level	
max_level	int	 true	max level	
settle_period	int	 true	settle period	
funding_rate_cap	int	 true	funding rate cap	
funding_rate_floor	int	 true	funding rate floor	
trigger_protect	decimal	 false	Threshold for price Protection	
long_position_limit		 false	long position limit	
offset_order_limit		 false	offset order limit	
open_order_limit		 false	open order limit	
short_position_limit		 false	short position limit	
<contract_infos>	object array	 true		
contract_code	string	 true	contract code	
instrument_type	list	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
settlement_date	string	 true	The next settlement time of the contract	Timestamps, such as "1490759594752"	
delivery_time	string	 true	delivery time（When the contract does not need to be delivered, the field value is an empty string），millesecond timestamp		
create_date	string	 true	Listing Date	eg "20190808"
contract_status	int	 true	Contract Status	contract status ： 0: Delisting,1: Listing,2: Pending Listing,3: Suspension,4: Suspending of Listing,6: Delivering,8: Delivered
delivery_date	string	 true	delivery date, empty string when swap	such as: "20180720"
<contract_infos>	object array	 true		
<price_ticks>	object array	 false	The Minimum Price Change	
business_type	Integer	 true	1: Perpetual futures; 2: Delivery futures; 3: Perpetual futures + delivery futures	
price	String	 true	The Minimum Price Change	
<instrument_values>		 true	contract Face Value	
business_type	Integer	 true	1: Perpetual futures; 2: Delivery futures; 3: Perpetual futures + delivery futures	
price	String	 true	contract Face Value	
<order_limits>	object array	 true	The maximum quantity of single order (Cont)	
instrument_type	int	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
open	String	 true	Open position	
close	String	 true	Close position	
order_type	int	 true	Order type
0: Price limit & Post only
1: IOC & FOK	
open_after_closing	String	 true	open after closing	
<normal_limits>		 false	Hard Price Limit	
instrument_type	int	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
open	String	 true	Open position	
close	String	 true	Close position	
<open_limits>	object	 false	Non-basis Price Limit	
instrument_type	int	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
open	String	 true	Open position	
close	String	 true	Close position	
<trade_limits>		 false	Basis Price Limit	
instrument_type	int	 true	Types of Futures Expiration: 1: Weekly futures; 2: Bi-weekly futures; 3: Quarterly futures; 4: Bi-quarterly futures; 0: Perpetual futures	
open	String	 true	Open position	
close	String	 true	Close position	
</data>		 false		
ts	long	 true		
Request example
curl"https://api.hbdm.com?contract_code=XRP-USDT"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"contract_code":"BTC-USDT"
"funding_rate_cap":"0.003750000000000000"
"funding_rate_floor":"-0.003750000000000000"
"mode_type":2
"swap_delivery_type":3
"settle_period":8
"instrument_index_code":"BTC-USDT"
"price_ticks":[
0:{
"business_type":1
"price":"0.100000000000000000"
}
1:{
"business_type":2
"price":"0.100000000000000000"
}
]
"instrument_values":[
0:{
"business_type":1
"price":"0.001000000000000000"
}
1:{
"business_type":2
"price":"0.001000000000000000"
}
]
"min_level":"1"
"max_level":"200"
"order_limits":[
0:{
"open_after_closing":"500000"
"order_type":0
"instrument_type":0
"open":"500000"
"close":"500000"
}
1:{
"open_after_closing":"500000"
"order_type":1
"instrument_type":0
"open":"500000"
"close":"500000"
}
2:{
"open_after_closing":"170000"
"order_type":0
"instrument_type":1
"open":"170000"
"close":"170000"
}
3:{
"open_after_closing":"170000"
"order_type":1
"instrument_type":1
"open":"170000"
"close":"170000"
}
4:{
"open_after_closing":"170000"
"order_type":0
"instrument_type":2
"open":"170000"
"close":"170000"
}
5:{
"open_after_closing":"170000"
"order_type":1
"instrument_type":2
"open":"170000"
"close":"170000"
}
]
"normal_limits":[
0:{
"instrument_type":0
"open":"0.06"
"close":"0.06"
}
1:{
"instrument_type":1
"open":"0.08"
"close":"0.08"
}
2:{
"instrument_type":2
"open":"0.08"
"close":"0.08"
}
]
"open_limits":[
0:{
"instrument_type":0
"open":"0.05"
"close":"0.05"
}
1:{
"instrument_type":1
"open":"0.04"
"close":"0.04"
}
2:{
"instrument_type":2
"open":"0.04"
"close":"0.04"
}
]
"trade_limits":[
0:{
"instrument_type":0
"open":"0.05"
"close":"0.05"
}
1:{
"instrument_type":1
"open":"0.02"
"close":"0.02"
}
2:{
"instrument_type":2
"open":"0.02"
"close":"0.02"
}
]
"real_time_settlement":1
"transfer_profit_ratio":1
"cross_transfer_profit_ratio":1
"instrument_type":[
0:0
1:1
2:2
]
"price_tick":"0.100000000000000000"
"instrument_value":"0.001000000000000000"
"trade_partition":"USDT"
"open_order_limit":"500000.000000000000000000"
"offset_order_limit":"500000.000000000000000000"
"long_position_limit":"148550000.000000000000000000"
"short_position_limit":"148550000.000000000000000000"
"contract_infos":[
0:{
"contract_code":"BTC-USDT"
"instrument_type":0
"settlement_date":"1765555200000"
"delivery_time":""
"create_date":"20201021"
"contract_status":1
"delivery_date":""
"trigger_protect":0.05
}
1:{
"contract_code":"BTC-USDT-251219"
"instrument_type":1
"settlement_date":"1766131200000"
"delivery_time":"1766131200000"
"create_date":"20251205"
"contract_status":1
"delivery_date":"20251219"
"trigger_protect":0.05
}
2:{
"contract_code":"BTC-USDT-251226"
"instrument_type":2
"settlement_date":"1766736000000"
"delivery_time":"1766736000000"
"create_date":"20250912"
"contract_status":1
"delivery_date":"20251226"
"trigger_protect":0.05
}
]
}
]
"ts":1703217085568
}








https://api.hbdm.com/api/v1/timestamp ([General]Get current system timestamp)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Request Address
Environment	Address
Online	https://api.hbdm.com/api/v1/timestamp
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes:  
No parameters are needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
status	string	 true	Request Processing Result
ts	long	 true	current system timestamp
Request example
curl"https://api.hbdm.com/api/v1/timestamp"
Response Example
Success Example
{
"status":"ok"
"ts":1578124684692
}







https://api.hbdm.com/heartbeat/ ([General]Query whether the system is available)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Request Address
Environment	Address
Online	https://api.hbdm.com/heartbeat/
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes:  
No parameters are needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	"ok" or "error"...
<data>	dict object	 false	
heartbeat	int	 false	future 1: avaiable 0: not available(maintenance with service suspended)
swap_heartbeat	int	 false	coin margined swap 1: avaiable 0: not available(maintenance with service suspended)
estimated_recovery_time	long	 false	null: normal. estimated recovery time :millionseconds.
swap_estimated_recovery_time	long	 false	null: normal. coin margined swap estimated recovery time millionseconds.
linear_swap_heartbeat	long	 false	USDT margined Contracts 1: avaiable 0: not available(maintenance with service suspended)
linear_swap_estimated_recovery_time	long	 false	null: normal. USDT margined Contracts estimated recovery time millionseconds.
</data>		 false	
Notes: 
Heartbeat is 1 is available, 0 is not available.

Request example
curl"https://api.hbdm.com/heartbeat/"
Response Example
Success Example
{
"status":"ok"
"data":{
"heartbeat":1
"estimated_recovery_time":NULL
"swap_heartbeat":1
"swap_estimated_recovery_time":NULL
"linear_swap_heartbeat":1
"linear_swap_estimated_recovery_time":NULL
}
"ts":1557714418033
}





https://api.hbdm.com/heartbeat ([General]Maintenance with service suspended)
Request type: GET

Signature verification: Yes

Interface permission: Read

Interface description: During the maintenance of the business system, in addition to the below two interfaces(Get system status, Query whether the system is available) for users to query the system status, all “rest” interfaces of the API business will return this in a fixed manner:{"status": "maintain"}. During maintenance with service suspended，all websocket notify interfaces except subscribing system status updates（Subscribe system status updates）can't work，and will push 1006 error code to clients.Response{    "status": "maintain"}Query whether the system is available: https://api.hbdm.com/heartbeat/for getting the infomation that system maintenance with service suspended, could by subscrib system status updates websocket interface.

































/linear-swap-ex/market/depth ([General] Get Market Depth)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 true	swap: "BTC-USDT"... , future: "BTC-USDT-220325" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
type	string	 true	Get depth data within step 150, use step0, step1, step2, step3, step4, step5, step14, step15, step16, step17（merged depth data 0-5,14-17）；when step is 0，depth data will not be merged; Get depth data within step 20, use step6, step7, step8, step9, step10, step11, step12, step13, step18, step19(merged depth data 7-13,18-19); when step is 6, depth data will not be merged.
Notes: 
step16, step17, step18, and step19 are only for SHIB-USDT contract, and the other contracts is not supported now.

Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	Data belonged channel，Format： market.period		
status	string	 true	Request Processing Result		
ts	long	 true	Time of Respond Generation，Unit：Millisecond		"ok" , "error"
<tick>		object array	 false		
mrid		long	 true	Order ID		
id	long	 true	tick ID		
asks	object	 false	Sell,[price(Ask price), vol(Ask orders (cont.) )], price in ascending sequence		
bids	object	 false	Buy,[price(Bid price), vol(Bid orders(Cont.))], Price in descending sequence		
ts	long	 true	Time of Respond Generation, Unit: Millisecond		
version	long	 true	version ID		
ch	string	 true	Data channel, Format： market.period		
</tick>			 false		
Request example
curl "https://api.hbdm.com/linear-swap-ex/market/depth?contract_code=BTC-USDT&type=step0"
Response Example
Success Example
{
"ch":"market.BTC-USDT-CQ.depth.step6"
"status":"ok"
"tick":{
"asks":[
0:[
0:48611.5
1:741
]
1:[
0:48635.2
1:792
]
]
"bids":[
0:[
0:48596.4
1:90
]
1:[
0:48585.7
1:180
]
]
"ch":"market.BTC-USDT-CQ.depth.step6"
"id":1638754215
"mrid":1250406
"ts":1638754215640
"version":1638754215
}
"ts":1638754216092
}












/linear-swap-ex/market/bbo ([General]Get Market BBO Data)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: he interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-220325" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 false	business type, default is swap	futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	the result of server handling to request	"ok" , "error"
<ticks>	object array	 true		
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-220325" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 true	business type	futures, swap
mrid	long	 true	Match ID, unique identification	
ask	array	 false	[Ask 1 price, Ask 1 qty (cont)]	
bid	array	 false	[Bid 1 price, Bid 1 qty (cont)]	
ts	long	 true	The system detects the orderbook time point, unit: milliseconds	
</ticks>		 false		
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
Request example
curl"https://api.hbdm.com/linear-swap-ex/market/bbo?contract_code=BTC-USDT&pair=BTC-USDT&contract_type=swap&business_type=swap"
Response Example
Success Example
{
"status":"ok"
"ticks":[
0:{
"business_type":"futures"
"contract_code":"BTC-USDT-CW"
"ask":[
0:48637.3
1:746
]
"bid":[
0:48482.5
1:385
]
"mrid":1251224
"ts":1638754357868
}
1:{
"business_type":"futures"
"contract_code":"BTC-USDT-NW"
"ask":[
0:48620.1
1:1000
]
"bid":[
0:48461
1:524
]
"mrid":1251162
"ts":1638754344746
}
2:{
"business_type":"futures"
"contract_code":"BTC-USDT-CQ"
"ask":[
0:48630.9
1:868
]
"bid":[
0:48577.1
1:63
]
"mrid":1251236
"ts":1638754359301
}
3:{
"business_type":"swap"
"contract_code":"BTC-USDT"
"ask":[
0:48511.6
1:91
]
"bid":[
0:48508.9
1:95
]
"mrid":334931
"ts":1638754361719
}
]
"ts":1638754363648
}




/linear-swap-ex/market/history/kline ([General] Get KLine Data)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-220325" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ	
period	string	 true	KLine Type	1min, 5min, 15min, 30min, 60min, 1hour,4hour,1day, 1mon	
size	int	 false	Acquisition Quantity	[1,2000]	150
from	long	 false	start timestamp seconds.		
to	long	 false	end timestamp seconds		
Notes: 
Either size field or from and to fields need to be filled.
If size field and from/to fields are not filled, It will return error messages.
If from field is filled, to field need to filled too.
The api can mostly return the klines of last two years.
If from to size are all filled,'from' and 'to' will be ignored.

Response Parameter
Parameter	Data Type	Required	Description
ch	string	 true	Data belonged channel，Format： market.period
status	string	 true	Request Processing Result
ts	long	 true	Time of Respond Generation, Unit: Millisecond
<data>	kline data	 false	
id	long	 true	kline id,the same as kline timestamp, kline start timestamp
vol	decimal	 true	Trade Volume(Cont.) . Sum of both buy and sell sides
count	decimal	 true	Order Quantity. Sum of both buy and sell sides
open	decimal	 true	Open Price
close	decimal	 true	Clos Price, the price in the last kline is the latest order price
low	decimal	 true	Low Price
high	decimal	 true	High Price
amount	decimal	 true	Trade Amount(Coin), trade amount(coin)=sum(order quantity of a single order * face value of the coin/order price). Sum of both buy and sell sides
trade_turnover	decimal	 true	Transaction amount, that is, sum (transaction quantity * contract face value * transaction price). Sum of both buy and sell sides
</data>		 false	
Request example
curl "https://api.hbdm.com/linear-swap-ex/market/history/kline?contract_code=BTC-USDT&period=1day&from=1587052800&to=1591286400"
Response Example
Success Example
{
"ch":"market.BTC-USDT.kline.1min"
"data":[
0:{
"amount":0.004
"close":13076.8
"count":1
"high":13076.8
"id":1603695060
"low":13076.8
"open":13076.8
"trade_turnover":52.3072
"vol":4
}
]
"status":"ok"
"ts":1603695099234
}





/index/market/history/linear_swap_mark_price_kline ([General]Get Kline Data of Mark Price)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
period	string	 true	period	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week,1mon
size	int	 true	size	[1,2000]
Notes: 
At one time 2000 at most
The input parameters are not case sensitive and all support

Response Parameter
Parameter	Data Type	Required	Description
ch	string	 true	channel, format: market.period
<data>	object array	 true	
id	long	 true	id
vol	string	 true	trade vol(cont), value is 0
count	string	 true	trade count, value is 0
open	string	 true	open price
close	string	 true	close price
low	string	 true	low price
high	string	 true	high price
amount	string	 true	trade amount, value is 0
trade_turnover	string	 true	trade turnover, value is 0
</data>		 false	
ts	long	 true	Time of Respond Generation, Unit: Millisecond
Request example
curl"https://api.hbdm.com/index/market/history/linear_swap_mark_price_kline?contract_code=BTC-USDT&period=5&size=100"
Response Example
Success Example
{
"ch":"market.BTC-USDT.mark_price.5min"
"data":[
0:{
"amount":"0"
"close":"31078.68"
"count":"0"
"high":"31078.68"
"id":1611105300
"low":"31078.68"
"open":"31078.68"
"trade_turnover":"0"
"vol":"0"
}
1:{
"amount":"0"
"close":"31078.68"
"count":"0"
"high":"31078.68"
"id":1611105600
"low":"31078.68"
"open":"31078.68"
"trade_turnover":"0"
"vol":"0"
}
]
"status":"ok"
"ts":1611106791703
}





linear-swap-ex/market/detail/merged ([General] Get Market Data Overview)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-220325" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	Data belonged channel，format： market.$contract_code.detail.merged	
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<tick>	object	 true	kline data (Start at 00:00(UTC+8) of the day)	
id	long	 true	kline id,the same as kline timestamp	
vol	string	 true	Trade Volume(Cont.), from nowtime - 24 hours. Sum of both buy and sell sides	
count	decimal	 true	Order Quantity, from nowtime - 24 hours. Sum of both buy and sell sides	
open	string	 true	Opening Price	
close	string	 true	Closing Price, the price in the last kline is the latest order price	
low	string	 true	Low	
high	string	 true	High	
amount	string	 true	Trade Amount(Coin), trade amount(coin)=sum(order quantity of a single order * face value of the coin/order price),from nowtime - 24 hours. Sum of both buy and sell sides	
ask	object	 true	Sell,[price(Ask price), vol(Ask orders (cont.) )], price in ascending sequence	
bid	object	 true	Buy,[price(Bid price), vol(Bid orders(Cont.))], Price in descending sequence	
trade_turnover	string	 true	Transaction amount, that is, sum (transaction quantity * contract face value * transaction price),from nowtime - 24 hours. Sum of both buy and sell sides	
ts	long	 true	Timestamp	
</tick>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-ex/market/detail/merged?contract_code=BTC-USDT"
Response Example
Success Example
{
"ch":"market.BTC-USDT.detail.merged"
"status":"ok"
"tick":{
"amount":"12.526"
"ask":[
0:13084.2
1:131
]
"bid":[
0:13082.9
1:38
]
"close":"13076.8"
"count":2920
"high":"13205.3"
"id":1603695162
"low":"12877.5"
"open":"12916.2"
"trade_turnover":"163247.3982"
"ts":1603695162580
"vol":"12526"
}
"ts":1603695162580
}





v2/linear-swap-ex/market/detail/batch_merged ([General]Get a Batch of Market Data Overview(V2))
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.
The interface data updated frequency is 50ms
The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.
business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 false	business type, default is swap	futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	status	"ok" , "error"
<ticks>	object array	 true		
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 true	business type	futures, swap
id	long	 true	id	
amount	string	 true	Trade Amount(Coin) ,from nowtime - 24 hours. Sum of both buy and sell sides	
ask	array	 true	[ask one price, ask one vol(cont)]	
bid	array	 true	[bid one price, bid one vol(cont)]	
open	string	 true	open price	
close	string	 true	close price	
count	decimal	 true	Order Quantity, from nowtime - 24 hours. Sum of both buy and sell sides	
high	string	 true	high price	
low	string	 true	low price	
vol	string	 true	Transaction amount, from nowtime - 24 hours. Sum of both buy and sell sides	
number_of	string	 true	number of(cont), from nowtime - 24 hours. Sum of both buy and sell sides	
ts	long	 true	timestamp	
</ticks>		 false		
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
Request example
curl"https://api.hbdm.com/v2/linear-swap-ex/market/detail/batch_merged?contract_code=BTC-USDT&business_type=swap"
Response Example
Success Example
{
"status":"ok"
"ticks":[
0:{
"id":1650792083
"ts":1650792083179
"ask":[
0:39736.6
1:1285
]
"bid":[
0:39736.5
1:6070
]
"business_type":"swap"
"contract_code":"BTC-USDT"
"open":"39760"
"close":"39736.6"
"low":"39316.3"
"high":"39971.2"
"amount":"6891.566"
"count":48262
"vol":"273472535.834"
"number_of":"6891566"
}
]
"ts":1650792083179
}



/linear-swap-ex/market/trade ([General] Query The Last Trade of a Contract)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

business_type is a required parameter when query info of futures contract, and its value must be futures or all.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description
contract_code	string	 false	contract code or contract type, swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 false	business type, default is swap: futures, swap, all
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	Data belonged channel，Format： market.$contract_code.trade.detail	
status	string	 true		"ok","error"
ts	long	 true	Sending time	
<tick>		 false		
id	long	 true	Unique Order Id(symbol level).	
ts	long	 true	Latest Creation Time	
<data>		 false		
id	long	 true	Unique Transaction Id(symbol level)	
price	string	 true	Price	
amount	string	 true	Quantity(Cont.). Sum of both buy and sell sides	
direction	string	 true	The direction to buy or sell is the direction of the taker (active transaction)	
ts	long	 true	Order Creation Time	
quantity	string	 true	trading quantity(coin)	
contract_code	string	 true	Contract Code or Contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
business_type	string	 true	business type	futures, swap
trade_turnover	string	 true	trade turnover(quoted currency)	
</data>		 false		
</tick>		 false		
Request example
curl "https://api.hbdm.com/linear-swap-ex/market/trade?contract_code=BTC-USDT"
Response Example
Success Example
{
"ch":"market.*.trade.detail"
"status":"ok"
"tick":{
"data":[
0:{
"amount":"6"
"ts":1603695230083
"id":1314755250000
"price":"13083"
"direction":"buy"
"quantity":0.006
"contract_code":"BTC-USDT"
"business_type":"swap"
"trade_turnover":78.498
}
]
"id":1603695235127
"ts":1603695235127
}
"ts":1603695235127
}




/linear-swap-ex/market/history/trade ([General] Query a Batch of Trade Records of a Contract)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
size	int	 true	Number of Trading Records Acquisition	[1, 2000]
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	Data belonged channel，Format： market.$contract_code.trade.detail	
<data>	object array	 true		
<data>	object array	 true		
amount	decimal	 true	Quantity(Cont.). Sum of both buy and sell sides	
direction	string	 true	The direction to buy or sell is the direction of the taker (active transaction)	
id	long	 true	Unique Transaction Id(symbol level)	
price	decimal	 true	Price	
ts	long	 true	Order Creation Time	
quantity	decimal	 true	trading quantity(coin)	
trade_turnover	decimal	 true	trade turnover(quoted currency)	
</data>		 false		
id	long	 true	Unique Order Id(symbol level).	
ts	long	 true	Latest transaction time	
</data>		 false		
status	string	 true		"ok"，"error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
Request example
curl "https://api.hbdm.com/linear-swap-ex/market/history/trade?contract_code=BTC-USDT&size=100"
Response Example
Success Example
{
"ch":"market.BTC-USDT.trade.detail"
"data":[
0:{
"data":[
0:{
"amount":2
"direction":"buy"
"id":1314767870000
"price":13081.3
"ts":1603695383124
"quantity":0.002
"trade_turnover":26.1626
}
]
"id":131476787
"ts":1603695383124
}
]
"status":"ok"
"ts":1603695388965
}





linear-swap-api/v1/swap_his_open_interest ([General] Query information on open interest)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

one of (pair+contract_type) and contract_code must be filled in(if all of them not filled in, will get 1014 error code); and all filled in, the contract_code is the preferred.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 false	contract_code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
pair	string	 false	pair	BTC-USDT
contract_type	string	 false	contract type	swap, this_week, next_week, quarter, next_quarter
period	string	 true	Period Type	1 hour:"60min"，4 hours:"4hour"，12 hours:"12hour"，1 day:"1day"
size	int	 false	Request Amount	Default：48，Data Range [1,200]
amount_type	int	 true	Open interest unit	1:-cont，2:-cryptocurrenty
Response Parameter
Parameter	Data Type	Required	Description	Value Range
status	string	 true	Request Processing Result	"ok" , "error"
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>		 false	Dictionary Data	
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	e.g. swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
<tick>		 false		
volume	decimal	 true	Open Interest.	
amount_type	int	 true	Open Interest Unit	1:-cont，2:- cryptocurrency
value	decimal	 true	Total position volume (the unit shall be the denominated currency of the contract, eg, USDT)	
ts	long	 true	Recording Time	
</tick>		 false		
</data>		 false		
Notes: 
tick field：Tick data is arranged in reverse chronological order；

Request example
curl "https://api.hbdm.com/linear-swap-api/v1/swap_his_open_interest?contract_code=BTC-USDT&period=60min&amount_type=1"
Response Example
Success Example
{
"status":"ok"
"data":{
"symbol":"BTC"
"tick":[
0:{
"volume":27112
"amount_type":1
"ts":1638720000000
"value":1321498.5264
}
]
"contract_code":"BTC-USDT-211210"
"business_type":"futures"
"pair":"BTC-USDT"
"contract_type":"this_week"
}
"ts":1638755582116
}





/index/market/history/linear_swap_premium_index_kline ([General] Query Premium Index Kline Data)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.e.g. "BTC-USDT","ETH-USDT".
period	string	 true	kline period	1min,5min, 15min, 30min, 60min,4hour,1day,1week,1mon
size	int	 true	kline size	[1,2000]
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	data channel	eg： market.period
<data>		 false	object	
id	long	 true	index kline id,the same as kline timestamp, kline start timestamp	
vol	string	 true	Trade Volume(Cont.) The value is 0	
count	string	 true	Order Quantity The value is 0	
open	string	 true	Opening Price	
close	string	 true	Closing Price, the price in the last kline is the latest order price	
low	string	 true	Lowest Price	
high	string	 true	Highest Price	
amount	string	 true	Trade Amount(Coin), The value is 0. )	
trade_turnover	string	 true	Transaction amount, the value is 0.	
</data>		 false		
status	string	 true	process status	"ok" , "error"
ts	long	 true	timestamp of the response of the server, unit：millionseconds	
Request example
curl "https://api.hbdm.com/index/market/history/linear_swap_premium_index_kline?contract_code=BTC-USDT&period=1min&size=1"
Response Example
Success Example
{
"ch":"market.BTC-USDT.premium_index.1min"
"data":[
0:{
"amount":"0"
"close":"0.0000079166666666"
"count":"0"
"high":"0.0000079166666666"
"id":1603696920
"low":"0.0000079166666666"
"open":"0.0000079166666666"
"trade_turnover":"0"
"vol":"0"
}
]
"status":"ok"
"ts":1603696958348
}




/index/market/history/linear_swap_estimated_rate_kline ([General] Query Estimated Funding Rate Kline Data)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.e.g. "BTC-USDT","ETH-USDT".
period	string	 true	kline period	1min,5min, 15min, 30min, 60min,4hour,1day,1week,1mon
size	int	 true	kline size	[1,2000]
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	data channel	eg： market.period
<data>		 false	object	
id	long	 true	kline ID	
vol	string	 true	Trade Volume(Cont.) The value is 0	
count	string	 true	Order Quantity The value is 0	
open	string	 true	Opening Price	
close	string	 true	Closing Price, the price in the last kline is the latest order price	
low	string	 true	Lowest Price	
high	string	 true	Highest Price	
amount	string	 true	Trade Amount(Coin), The value is 0. )	
trade_turnover	string	 true	Transaction amount, the value is 0.	
</data>		 false		
status	string	 true	process status	"ok" , "error"
ts	long	 true	timestamp of the response of the server	unit：millionseconds
Request example
curl "https://api.hbdm.com/index/market/history/linear_swap_estimated_rate_kline?contract_code=BTC-USDT&period=1min&size=1"
Response Example
Success Example
{
"ch":"market.BTC-USDT.estimated_rate.1min"
"data":[
0:{
"amount":"0"
"close":"0.0001"
"count":"0"
"high":"0.0001"
"id":1603697100
"low":"0.0001"
"open":"0.0001"
"trade_turnover":"0"
"vol":"0"
}
]
"status":"ok"
"ts":1603697104902
}




/index/market/history/linear_swap_basis ([General] Query Basis Data)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

（1）For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Request Address
Environment	Address
Online	https://api.hbdm.com
Online  (preferred by aws customers)	https://api.hbdm.vn
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ	
period	string	 true	kline period	1min,5min, 15min, 30min, 60min,4hour,1day,1mon	
basis_price_type	string	 false	use basis price type to calculate the basis data	open price："open"，close price："close"，highest price："high"，lowest price："low"，avg=（high price +low price）/2："average"	Using open price default
size	int	 true	data size	[1,2000]	150
Response Parameter
Parameter	Data Type	Required	Description	Value Range
ch	string	 true	data channel，eg： market.basis	
<data>	object array	 false		
id	long	 true	unique id	
contract_price	string	 true	contract last price	
index_price	string	 true	index price	
basis	string	 true	basis=contract_price - index_price	
basis_rate	string	 true	basis_rate=basis/index_price	
</data>		 false		
status	string	 true	status	"ok" , "error"
ts	long	 true	created time	
Request example
curl "https://api.hbdm.com/index/market/history/linear_swap_basis?contract_code=BTC-USDT&period=1min&size=1"
Response Example
Success Example
{
"ch":"market.BTC-USDT.basis.1min.open"
"data":[
0:{
"basis":"15.29074235666667"
"basis_rate":"0.001170582317307796"
"contract_price":"13077.8"
"id":1603697160
"index_price":"13062.509257643333"
}
]
"status":"ok"
"ts":1603697170804
}


















































websocket data




















market.$contract_code.kline.$period ([General] Subscribe Kline data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
period	string	 true	Kline Period	1min, 5min, 15min, 30min, 60min,4hour,1day,1week, 1mon
Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Request Parameter
ts	long	 true	Time of Respond Generation，Unit：Millisecond
<tick>		 false	
id	long	 true	kline id,the same as kline timestamp, kline start timestamp
mrid	long	 true	ID Order ID
vol	decimal	 true	Trade Volume(Cont.). Sum of both buy and sell sides
count	decimal	 true	Order Quantity. Sum of both buy and sell sides
open	decimal	 true	Open Price
close	decimal	 true	Clos Price, the price in the last kline is the latest order price
low	decimal	 true	Low Price
high	decimal	 true	High Price
amount	decimal	 true	Trade Amount(Coin), trade amount(coin)=sum(order quantity of a single order * face value of the coin/order price). Sum of both buy and sell sides
trade_turnover	decimal	 true	Transaction amount, that is, sum (transaction quantity * contract face value * transaction price). Sum of both buy and sell sides
</tick>		 false	
Subscription Example
{
"sub":"market.BTC-USDT.kline.1min"
"id":"id1"
}
Example of a Successful Subscription
{
"id":"id1"
"status":"ok"
"subbed":"market.BTC-USDT.kline.1min"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.kline.1min"
"ts":1603707124366
"tick":{
"id":1603707120
"mrid":131592424
"open":13067.7
"close":13067.7
"high":13067.7
"low":13067.7
"amount":0.004
"vol":4
"trade_turnover":52.2708
"count":1
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.kline.1min"
"id":"id1"
}





market.$contract_code.kline.$period ([General] Request Kline data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
period	string	 true	Kline Period	1min, 5min, 15min, 30min, 60min,4hour,1day,1week, 1mon
Notes: 
If between time range [t1, t5], there are t1-t5 KLines in quantity.
from: t1, to: t5, return [t1, t5].
from: t5, to: t1, which t5 > t1, return [].
from: t5, return [t5].
from: t3, return [t3, t5].
to: t5, return [t1, t5].
from: t which t3 < t to: t which t3 < t from: t1 and to: t2, should satisfy 1325347200 < t1 < t2 < 2524579200.
Clients can request 2000 Klines at most in one request

Data Update
Parameter	Data Type	Required	Description
rep	string	 true	Request Parameter
status	string	 true	status
id	string	 true	Request ID
wsid	long	 true	wsid
<data>		 false	
id	long	 true	kline id,the same as kline timestamp, kline start timestamp
vol	decimal	 true	Trade Volume(Cont.). Sum of both buy and sell sides
count	decimal	 true	Order quantity. Sum of both buy and sell sides
open	decimal	 true	Open Price
close	decimal	 true	Clos Price, the price in the latest Kline is the last order price
low	decimal	 true	Low Price
high	decimal	 true	High Price
amount	decimal	 true	Trade Amount(Coin), trade amount(coins)=sum(order quantity of a single order * face value of the coin/order price). Sum of both buy and sell sides
trade_turnover	decimal	 true	Transaction amount, that is, sum (transaction quantity * contract face value * transaction price). Sum of both buy and sell sides
</data>		 false	
Subscription Example
{
"req":"market.BTC-USDT.kline.1min"
"id":"id4"
"from":1579247342
"to":1579247342
}
Example of a Successful Subscription
{
"id":"id4"
"rep":"market.BTC-USDT.kline.60min"
"wsid":467277265
"status":"ok"
"data":[
0:{
"id":1603270800
"open":12198
"close":12196.7
"low":11715.8
"high":12300
"amount":0.276
"vol":276
"trade_turnover":3315.9104
"count":39
}
1:{
"id":1603274400
"open":12196.7
"close":12277.9
"low":12111
"high":12289.9
"amount":0.198
"vol":198
"trade_turnover":2420.7728
"count":21
}
]
}






market.$contract_code.depth.$type ([General] Subscribe Market Depth Data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
type	string	 true	Depth Type	(Non-Aggregated Depth)
step0: 150 levels
step6: 20 levels 30 levels→
(Aggregated Depth)
step1, step2, step3, step4, step5, step14, step15, step16, step17: 150 levels.
step6, step7, step8, step9, step10, step11, step12, step13, step18, step19: 20 levels 30→
levels.
Notes: 
When clients choose merged depth data, WebSocket server will only display the merged price within price steps in order book. Please note that the merged depth price will not make any change on the actual order price.
step16, step17, step18, and step19 are only for SHIB-USDT contract, and the other contracts is not supported now.
steps between step1 and step5, step14 and step17 are merged orderbook data of step 150. steps between step7 and step13, step18, step19 are merged orderbook data of step 20. Details are below:
Depth	precision
step16、step18	0.0000001
step17、step19	0.000001
step1、step7	0.00001
step2、step8	0.0001
step3、step9	0.001
step4、step10	0.01
step5、step11	0.1
step14、step12	1
step15、step13	10

Data Update
Parameter	Data Type	Required	Description
ts	string	 true	Time of Respond Generation, Unit: Millisecond
ch	long	 true	Data channel, Format： market.period
<tick>		 false	
mrid	long	 true	Order ID
id	long	 true	tick ID
asks	object	 false	Sell,[price(Ask price), vol(Ask orders (cont.) )], price in ascending sequence
bids	object	 false	Buy,[price(Bid price), vol(Bid orders(Cont.))], Price in descending sequence
ts	long	 true	Timestamp for depth generation; generated once every 100ms, unit: millisecond
version	long	 true	version ID
ch	string	 true	Data channel, Format： market.period
</tick>		 false	
Subscription Example
{
"sub":"market.BTC-USDT.depth.step0"
"id":"id5"
}
Example of a Successful Subscription
{
"id":"id1"
"status":"ok"
"subbed":"market.BTC-USDT.depth.step0"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.depth.step6"
"ts":1603707576468
"tick":{
"mrid":131596447
"id":1603707576
"bids":[
0:[
0:13071.9
1:38
]
1:[
0:13068
1:5
]
]
"asks":[
0:[
0:13081.9
1:197
]
1:[
0:13099.7
1:371
]
]
"ts":1603707576467
"version":1603707576
"ch":"market.BTC-USDT.depth.step6"
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.depth.step0"
"id":"id5"
}







market.$contract_code.depth.size_${size}.high_freq ([General] Subscribe Incremental Market Depth Data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Default Value
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
size	string	 true	Depth size	20: stands for 20 unmerged data. 150:stands for 150 unmerged data.
Data Update
Parameter	Data Type	Required	Description
ts	string	 true	Timestamp of Respond Generation, Unit: Millisecond
ch	long	 true	Data channel, Format：market.$contract_code.depth.size_${size}.high_freq
<tick>		 false	
mrid	long	 true	Order ID
id	long	 true	tick ID，system timestamp.seconds
asks	object	 true	Sell,[price(Ask price), vol(Ask orders (cont.) )], price in ascending sequence
bids	object	 true	Buy,[price(Bid price), vol(Bid orders(Cont.))], Price in descending sequence
ts	long	 true	Timepoint for system detecting orderbook, unit: millisecond
version	long	 true	version ID,auto increment ID.
event	string	 true	event type: update or snapshot
ch	string	 true	Data channel, Format： market.$contract_code.depth.size_${size}.high_freq
</tick>		 false	
Notes: 
when data_type is incremental,snapshot data wil be pushed for the first time. When re-connection occurs, snapshort data will be pushed for the first time.
version: auto increment in single websocket connection. version may be different among several websocket subscription connections.
orderbook will be pushed if orderbook is updated whenever incremental or snapshot.
orderbook event will be checked every 30ms. If there is no orderbook event, you will not receive any orderbook data.
you HAVE TO maintain local orderbook data,such as updating your local orderbook bids and asks data.

Subscription Example
{
"sub":"market.BTC-USDT.depth.size_20.high_freq"
"data_type":"incremental"
"id":"id generated by client"
}
Example of a Successful Subscription
{
"status":"ok"
"subbed":"market.BTC-USDT.depth.size_20.high_freq"
"data_type":"incremental"
"id":"id generated by client"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.depth.size_20.high_freq"
"tick":{
"asks":[
0:[
0:13081.9
1:206
]
1:[
0:13099.7
1:371
]
]
"bids":[
0:[
0:13071.9
1:38
]
1:[
0:13060
1:400
]
]
"ch":"market.BTC-USDT.depth.size_20.high_freq"
"event":"snapshot"
"id":131597620
"mrid":131597620
"ts":1603707712356
"version":1512467
}
"ts":1603707712357
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.depth.size_20.high_freq"
"data_type":"incremental"
"id":"id generated by client"
}




market.$contract_code.detail ([General] Subscribe Market Detail Data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Data channel，Format： market.$contract_code.detail
ts	long	 true	Time of Respond Generation, Unit: Millisecond
<tick>		 false	
id	long	 true	ID
mrid	long	 true	Order ID
open	decimal	 true	Open Price
close	decimal	 true	Clos Price, the price from the latest kline is the last order price
high	decimal	 true	High Price
low	decimal	 true	Low Price
amount	decimal	 true	Trade Amount(Coins), Trade amount(Coin)=SUM(quantity(cont.)*face value/ order price. Sum of both buy and sell sides
vol	decimal	 true	Trade volume(Cont.)， the sum volume of both buy and sell sides. Sum of both buy and sell sides
count	decimal	 true	fulfilled order quantity. Sum of both buy and sell sides
trade_turnover	decimal	 true	Transaction amount, that is, sum (transaction quantity * contract face value * transaction price). Sum of both buy and sell sides
ask	array	 true	Sell,[price(Ask price), vol(Ask orders (cont.) )]
bid	array	 true	Buy,[price(Bid price), vol(Bid orders(Cont.))]
</tick>		 false	
Notes: 
Bid price(p1) and ask price(p1) are not updated in real time, there will be some delay (about 500ms).
The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Example
{
"sub":"market.BTC-USDT.detail"
"id":"id6"
}
Example of a Successful Subscription
{
"id":"id6"
"status":"ok"
"subbed":"market.BTC-USDT.detail"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.detail"
"ts":1603707870528
"tick":{
"id":1603707840
"mrid":131599205
"open":12916.2
"close":13065.8
"high":13205.3
"low":12852.8
"amount":30.316
"vol":30316
"trade_turnover":395073.4918
"count":2983
"asks":[
0:13081.9
1:206
]
"bids":[
0:13071.9
1:38
]
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.detail"
"id":"id6"
}




market.$contract_code.bbo ([General] Subscribe market BBO data push)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Data channel, Format： market.$contract_code.bbo
ts	long	 true	Timestamp of Respond Generation, Unit: Millisecond
<tick>	object	 true	
ch	string	 true	Data channel, Format： market.$contract_code.bbo
mrid	string	 true	Order ID
id	long	 true	tick ID
ask	array	 false	Best Ask Quotation,[price(Ask price), vol(Ask order (cont.) )]
bid	array	 false	Best Bid Quotation,[price(Bid price), vol(Bid order(Cont.))]
version	long	 true	version ID.
ts	long	 true	Time of Respond Generation, Unit: Millisecond
<\tick>		 false	
Notes: 
When any one of the buy_one price, buy_one quantity, sell_one price and sell_one quantity changes, the system will push BBO price.
If there are multiple changes in the price or quantity of buy_one or sell_one at the same time, the system will push the latest price and quantity of buy_one and sell one with the intermediate data discarded.
When the data received by the client is failed or delayed, the old data buffer in the server will be discarded.The latest BBO will be pushed.
version（version number). Use match id directly to ensure it is globally unique and the value of version number pushed is the largest.

Subscription Example
{
"sub":"market.BTC-USDT.bbo"
"id":"id8"
}
Example of a Successful Subscription
{
"id":"id8"
"status":"ok"
"subbed":"market.BTC-USDT.bbo"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.bbo"
"ts":1603707934525
"tick":{
"mrid":131599726
"id":1603707934
"bid":[
0:13064
1:38
]
"ask":[
0:13072.3
1:205
]
"ts":1603707934525
"version":131599726
"ch":"market.BTC-USDT.bbo"
}
}




market.$contract_code.trade.detail ([General] Request Trade Detail Data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
Data Update
Parameter	Data Type	Required	Description
rep	string	 true	Data Channel，Format： market.$contract_code.trade.detail
status	string	 true	Request Status
id	long	 true	Request ID
<data>		 false	
id	long	 true	Unique Transaction Id(symbol level)
price	string	 true	Price
amount	string	 true	Quantity(Cont.). Sum of both buy and sell sides
direction	string	 true	The direction to buy or sell is the direction of the taker (active transaction)
ts	long	 true	Order Creation Time
quantity	string	 true	trading quantity(coin)
trade_turnover	string	 true	trade turnover(quoted currency)
</data>		 false	
ts	long	 true	server response time
Notes: 
There are "quantity" parameter in return data only after 21:00:00 on February 3, 2021

Subscription Example
{
"req":"market.BTC-USDT.trade.detail"
"size":50
"id":"id8"
}
Example of a Successful Subscription
{
"data":[
0:{
"amount":"22"
"ts":1603706942240
"id":1315909380000
"price":"13068.4"
"direction":"sell"
"quantity":"0.022"
"trade_turnover":"288.334"
}
1:{
"amount":"2"
"ts":1603706947767
"id":1315909430000
"price":"13068.5"
"direction":"buy"
"quantity":"0.002"
"trade_turnover":"26.334"
}
]
"id":"id8"
"rep":"market.BTC-USDT.trade.detail"
"status":"ok"
"ts":1603708046534
}




market.$contract_code.trade.detail ([General] Subscribe Trade Detail Data)
Signature verification: No

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-ws
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-ws
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code or contract type	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Data channel,format: market.$contract_code.trade.detail
ts	long	 true	Request time
<tick>		 false	
id	long	 true	Unique Order Id(symbol level).
ts	long	 true	tick time
<data>		 false	
amount	decimal	 true	quantity(Cont.). Sum of both buy and sell sides
ts	long	 true	trade timestamp
id	long	 true	Unique Transaction Id(symbol level)
price	decimal	 true	Price
direction	string	 true	The direction to buy or sell is the direction of the taker (active transaction)
quantity	decimal	 true	trading quantity(coin)
trade_turnover	decimal	 true	trade turnover(quoted currency)
</data>		 false	
</tick>		 false	
Subscription Example
{
"sub":"market.BTC-USDT.trade.detail"
"id":"id7"
}
Example of a Successful Subscription
{
"id":"id7"
"status":"ok"
"subbed":"market.BTC-USDT.trade.detail"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.trade.detail"
"ts":1603708208346
"tick":{
"id":131602265
"ts":1603708208335
"data":[
0:{
"amount":2
"ts":1603708208335
"id":1316022650000
"price":13073.3
"direction":"buy"
"quantity":0.002
"trade_turnover":26.334
}
]
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.trade.detail"
"id":"id7"
}





market.$contract_code.index.$period ([General] Subscribe Index Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	index symbol	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1mon
Notes: 
Pushed once the index data is changed.
Periodical Push when the index data hasn't changed according to the kline period.

Data Update
Parameter	Data Type	Required	Description
ch	string	 false	Data channel，Format：market.$contract_code.index.$period
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<tick>	object array	 false	
id	string	 false	index kline id,the same as kline timestamp,kline start timestamp
vol	string	 false	Trade Volume. The value is 0.
count	decimal	 false	count. The value is 0.
open	string	 false	open index price
close	string	 false	close index price
low	string	 false	lowest index price
high	string	 false	highest index price
amount	string	 false	amount based on coins.
</tick>		 false	
Subscription Example
{
"sub":"market.BTC-USDT.index.1min"
"id":"id1"
}
Example of a Successful Subscription
{
"id":"id1"
"status":"ok"
"subbed":"market.BTC-USDT.index.1min"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.index.15min"
"ts":1607309592214
"tick":{
"id":1607309100
"open":"19213.505"
"close":"19242.05"
"high":"19248.31"
"low":"19213.505"
"amount":"0"
"vol":"0"
"count":0
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.index.1min"
"id":"id1"
}
Error Code Explanation
Error Code	Error	Error Description	Solution:





market.$contract_code.index.$period ([General] Request Index Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	index symbol	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1mon
Notes: 
Pushed once the index data is changed.

Data Update
Parameter	Data Type	Required	Description
req	string	 true	Data channel，Format：market.$contract_code.index.$period
status	string	 true	Request processing result
id	string	 true	ID
wsid	long	 true	wsid
ts	long	 true	Time of Respond Generation, Unit: Millisecond
<data>	object array	 false	Details：data parameters
id	decimal	 false	index kline id,the same as kline timestamp,kline start timestamp
vol	decimal	 false	Trade Volume. The value is 0.
count	decimal	 false	count. The value is 0.
open	decimal	 false	open index price
close	decimal	 false	close index price
low	decimal	 false	lowest index price
high	decimal	 false	highest index price
amount	decimal	 false	amount based on coins.
</data>		 false	
Subscription Example
{
"req":"market.btc-usdt.index.1min"
"id":"id4"
"from":1571000000
"to":1573098606
}
Example of a Successful Subscription
{
"id":"id4"
"rep":"market.BTC-USDT.index.15min"
"wsid":3673570133
"ts":1607310136031
"status":"ok"
"data":[
0:{
"id":1607309100
"open":19213.505
"close":19207.245
"low":19207.245
"high":19248.31
"amount":0
"vol":0
"count":0
}
1:{
"id":1607310000
"open":19199.655
"close":19174.48
"low":19174.48
"high":19208.11
"amount":0
"vol":0
"count":0
}
]
}







market.$contract_code.premium_index.$period ([General] Subscribe Premium Index Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Notes: 
Pushed once the index data is changed.
Periodical Push when the index data hasn't changed according to the kline period.

Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Data channel，Format： market.period
<tick>	object array	 true	
id	long	 true	index kline id,the same as kline timestamp, kline start timestamp
vol	string	 true	Trade Volume(Cont.). The value is 0.
count	string	 true	count. The value is 0.
open	string	 true	open index price
close	string	 true	close index price
low	string	 true	lowest index price
high	string	 true	highest index price
amount	string	 true	amount based on coins.
</tick>		 false	
ts	long	 true	Time of Respond Generation, Unit: Millisecond
Subscription Example
{
"sub":"market.BTC-USDT.premium_index.1min"
"id":"id7"
}
Example of a Successful Subscription
{
"id":"id7"
"status":"ok"
"subbed":"market.BTC-USDT.premium_index.1min"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.premium_index.1min"
"ts":1603708380380
"tick":{
"id":1603708380
"open":"0.000068125"
"close":"0.000068125"
"high":"0.000068125"
"low":"0.000068125"
"amount":"0"
"vol":"0"
"count":"0"
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.premium_index.1min"
"id":"id7"
}





market.$contract_code.premium_index.$period ([General] Request Premium Index Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Notes: 
Pushed once the index data is updated.

Data Update
Parameter	Data Type	Required	Description
rep	string	 true	Data channel，Format： market.period
status	string	 true	Request processing result
id	string	 true	ID
wsid	long	 true	wsid
ts	long	 true	Time of Respond Generation, Unit: Millisecond
<data>	object array	 true	
id	long	 true	index kline id,the same as kline timestamp, kline start timestamp
vol	string	 true	Trade Volume(Cont.). The value is 0.
count	string	 true	count. The value is 0.
open	string	 true	open index price
close	string	 true	close index price
low	string	 true	lowest index price
high	string	 true	highest index price
amount	string	 true	amount based on coins.
</data>		 false	
Subscription Example
{
"req":"market.BTC-USDT.premium_index.1min"
"id":"id4"
"from":1571000000
"to":1573098606
}
Example of a Successful Subscription
{
"id":"id4"
"rep":"market.BTC-USDT.premium_index.15min"
"wsid":1524762738
"ts":1603782744066
"status":"ok"
"data":[
0:{
"id":1603641600
"open":"0"
"close":"0.0000970833333333"
"low":"0"
"high":"0.0000997916666666"
"amount":"0"
"vol":"0"
"count":"0"
}
]
}




market.$contract_code.estimated_rate.$period ([General] Subscribe Estimated Funding Rate Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Notes: 
Pushed once the kline data is changed.
Periodical Push when the kline data hasn't changed according to the kline period.

Data Update
Parameter	Data Type	Required	Description
ch	string	 true	Data channel，Format： market.period
<tick>	object array	 true	
id	long	 true	index kline id,the same as kline timestamp
vol	string	 true	Trade Volume(Cont.). The value is 0.
count	string	 true	count. The value is 0.
open	string	 true	open index price
close	string	 true	close index price
low	string	 true	lowest index price
high	string	 true	highest index price
amount	string	 true	amount based on coins.
trade_turnover	string	 true	Transaction amount, the value is 0.
</tick>		 false	
ts	long	 true	Time of Respond Generation, Unit: Millisecond
Subscription Example
{
"sub":"market.btc-usdt.estimated_rate.1min"
"id":"id7"
}
Example of a Successful Subscription
{
"id":"id7"
"status":"ok"
"subbed":"market.btc-usdt.estimated_rate.1min"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.estimated_rate.1min"
"ts":1603708560233
"tick":{
"id":1603708560
"open":"0.0001"
"close":"0.0001"
"high":"0.0001"
"low":"0.0001"
"amount":"0"
"vol":"0"
"count":"0"
"trade_turnover":"0"
}
}
Example of a Subscription Cancellation
{
"unsub":"market.btc-usdt.estimated_rate.1min"
"id":"id7"
}





market.$contract_code.estimated_rate.$period ([General] Request Estimated Funding Rate Kline Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	Case-Insenstive.Both uppercase and lowercase are supported.."BTC-USDT","ETH-USDT"...
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Data Update
Parameter	Data Type	Required	Description	Value Range
rep	string	 true	Data channel, Format： market.period	
status	string	 true	Request status	"ok" , "error"
id	string	 true	ID	
wsid	long	 true	wsid	
ts	long	 true	Time of Respond Generation, unit: millisecond	
<data>	object array	 true		
id	long	 true	index kline id,the same as kline timestamp	
vol	string	 true	Trade Volume(Cont.). The value is 0.	
count	string	 true	count. The value is 0.	
open	string	 true	open index price	
close	string	 true	close index price	
low	string	 true	lowest index price	
high	string	 true	highest index price	
amount	string	 true	amount based on coins.	
trade_turnover	string	 true	Transaction amount, the value is 0.	
</data>		 false		
Subscription Example
{
"req":"market.BTC-USDT.estimated_rate.1min"
"id":"id4"
"from":1579247342
"to":1579247342
}
Example of a Successful Subscription
{
"id":"id4"
"rep":"market.BTC-USDT.estimated_rate.15min"
"wsid":3674722864
"ts":1603782867314
"status":"ok"
"data":[
0:{
"id":1603641600
"open":"0.0001"
"close":"0.0001"
"low":"0.0001"
"high":"0.0001"
"amount":"0"
"vol":"0"
"count":"0"
"trade_turnover":"0"
}
]
}





market.$contract_code.basis.$period.$basis_price_type ([General] Subscribe Basis Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ	
period	string	 true	kline period	1min,5min, 15min, 30min, 60min,4hour,1day,1mon	
basis_price_type	string	 false	use basis price type to calculate the basis data	open price："open"，close price："close"，highest price："high"，lowest price："low"，avg=（high price +low price）/2："average"	Using open price default
Data Update
Parameter	Data Type	Required
ch	string	 false
<tick>	object array	 false
id	long	 false
contract_price	string	 false
index_price	string	 false
basis	string	 false
basis_rate	string	 false
</tick>		 false
ts	long	 false
Subscription Example
{
"sub":"market.BTC-USDT.basis.1min.open"
"id":"id7"
}
Example of a Successful Subscription
{
"id":"id7"
"status":"ok"
"subbed":"market.BTC-USDT.basis.1min.open"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.basis.1min.open"
"ts":1617164081549
"tick":{
"id":1617164040
"index_price":"58686.78333333333"
"contract_price":"58765"
"basis":"78.21666666667"
"basis_rate":"0.0013327816285723049700163397705562309"
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.basis.1min.open"
"id":"id7"
}





market.$contract_code.basis.$period.$basis_price_type ([General] Request Basis Data)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ	
period	string	 true	kline type	1min, 5min, 15min, 30min, 60min,4hour,1day, 1mon	
basis_price_type	string	 false	use basis price type to calculate the basis data	open price："open"，close price："close"，highest price："high"，lowest price："low"，avg=（high price +low price）/2："average"	Using open price default
Data Update
Parameter	Data Type	Required	Description	Value Range
rep	string	 true	Data belonged channel Format: market.basis	
status	string	 true	Return Statu	"ok" , "error"
id	string	 true	Request ID	
wsid	long	 true	wsid	
ts	long	 true	Time of Respond Generation, unit: millisecond	
<data>	object array	 false		
id	long	 true	unique id	
contract_price	string	 true	contract last price	
index_price	string	 true	index price	
basis	string	 true	basis=contract_price - index_price	
basis_rate	string	 true	basis_rate=basis/index_price	
</data>		 false		
Subscription Example
{
"req":"market.btc-usdt.basis.1min.open"
"id":"id4"
"from":1579247342
"to":1579247342
}
Example of a Successful Subscription
{
"data":[
0:{
"basis":"-27.593412766666006"
"basis_rate":"-0.0021317871729511838"
"contract_price":"12916.2"
"id":1603641600
"index_price":"12943.793412766667"
}
]
"id":"id4"
"rep":"market.BTC-USDT.basis.15min.open"
"status":"ok"
"ts":1603783024207
"wsid":1308653018
}




market.$contract_code.mark_price.$period ([General]Subscribe Kline Data of Mark Price)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
period	string	 true	period	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Data Update
Parameter	Data Type	Required	Description
ch	string	 true	channel, format: market.period
<tick>	object array	 true	
id	long	 true	id
vol	string	 true	trade vol(cont), value is 0
count	string	 true	trade count, value is 0
open	string	 true	open price
close	string	 true	close price
low	string	 true	low price
high	string	 true	high price
amount	string	 true	trade amount, value is 0
trade_turnover	string	 true	trade turnover, value is 0
</tick>		 false	
ts	long	 true	Time of Respond Generation, Unit: Millisecond
Subscription Example
{
"sub":"market.BTC-USDT.mark_price.1min"
"id":"id1"
}
Example of a Successful Subscription
{
"id":"id1"
"status":"ok"
"subbed":"market.BTC-USDT.mark_price.1min"
"ts":1489474081631
}
Example of a Data Update
{
"ch":"market.BTC-USDT.mark_price.1min"
"ts":1489474082831
"tick":{
"vol":"0"
"close":"9800.12"
"count":"0"
"high":"9800.12"
"id":1529898780
"low":"9800.12"
"open":"9800.12"
"trade_turnover":"0"
"amount":"0"
}
}
Example of a Subscription Cancellation
{
"unsub":"market.BTC-USDT.mark_price.1min"
"id":"id1"
}




market.$contract_code.mark_price.$period ([General]Request Kline Data of Mark Price)
Signature verification: Yes

Interface permission: Read

Rate Limit: For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：
For websocket: The rate limit for “req” request is 50 times at once. No limit for “sub” request as the data will be pushed by sever voluntarily.

Interface description: The interface supports cross margin mode and isolated margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625; and supports contract type: BTC-USDT, BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/ws_index
Online  (preferred by aws customers)	wss://api.hbdm.vn/ws_index
Request Parameter
Field Name	Type	Description

No data

Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule

No data

Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ... or BTC-USDT-CW, BTC-USDT-NW, BTC-USDT-CQ, BTC-USDT-NQ
period	string	 true	period	1min, 5min, 15min, 30min, 60min,4hour,1day, 1week, 1mon
Data Update
Parameter	Data Type	Required	Description	Value Range
req	string	 true	channel, format: market.period	
status	string	 true	status	"ok" , "error"
id	string	 true	id	
wsid	long	 true	wsid	
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
<data>	object array	 true		
id	long	 true	kline id	
vol	string	 true	trade vol(cont), value is 0	
count	string	 true	trade count, value is 0	
open	string	 true	open price	
close	string	 true	close price	
low	string	 true	low price	
high	string	 true	high price	
amount	string	 true	trade amount, value is 0	
trade_turnover	string	 true	trade turnover, value is 0	
</data>		 false		
Subscription Example
{
"req":"market.BTC-USDT.mark_price.5min"
"id":"id4"
"from":1579247342
"to":1579247342
}
Example of a Successful Subscription
{
"rep":"market.BTC-USDT.mark_price.1min"
"status":"ok"
"id":"id4"
"wsid":1231323423
"ts":1579489028884
"data":[
0:{
"vol":"0"
"close":"9800.12"
"count":"0"
"high":"9800.12"
"id":1529898780
"low":"9800.12"
"open":"9800.12"
"trade_turnover":"0"
"amount":"0"
}
]
}





ccounts.$contract_code ([Isolated] Subscribe Account Equity Updates Data(sub))
Signature verification: No

Interface permission: Read

Rate Limit: WebSocket, the private order push interface, requires API KEY Verification:

Each UID can build at most create 30 WS connections for private order push at the same time. For each account, contracts of the same underlying coin only need to subscribe one WS order push, e.g. users only need to create one WS order push connection for BTC Contract which will automatically push orders of BTC-USDT contracts. Please note that the rate limit of WS order push and RESTFUL private interface are separated from each other, with no relations.

Interface description: This interface only supports isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-notification
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-notification
Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
accounts.*	accounts.*	Allowed
accounts.contract_code1	accounts.*	Allowed
accounts.contract_code1	accounts.contract_code1	Allowed
accounts.contract_code1	accounts.contract_code1	Not Allowed
accounts.*	accounts.contract_code1	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description	Default Value
contract_code	string	 true	contract code	"*" all(it means to subscribe the balance change of all coins), "BTC-USDT"...
cid	string	 false	Current request's ID	
Notes: 
A regular push of account is performed every 5 sedconds.The event field of the reponse is "snapshot".If there is a push in 5 seconds, snapshot push will be skipped.

Data Update
Parameter	Data Type	Required	Description	Value Range
op	string	 false	Operator Name，Subscribe value is sub	
topic	string	 true	Subscribe Topic Name	
uid	long	 true	account uid	
ts	string	 true	Time of Respond Generation, Unit: Millisecond	
event	string	 true	Related events of position change notification	notification on account asset change such as commit order(order.open), fulfill order(order.match)(excluding liquidated order and settled orders), settlement and delivery(settlement), fulfill liquidation order(order.liquidation)(including voluntarily fulfilled liquidation order and the fulfilled liquidation order taken over by system ) , cancel order(order.cancel), asset transfer（contract.transfer) (ncluding transfer with exchange accounts, transfer between main account and sub-account, and tranfer between different margin accounts.), system (contract.system), other asset change(other), switch leverage(switch_lever_rate), initial margin(init), ADL trade
<data>	object array	 true		
symbol	string	 true	Coins. "BTC","ETH"...	
contract_code	string	 true	Contract Code	
margin_asset	string	 true	margin asset	
margin_balance	decimal	 true	Account Equity	
margin_static	decimal	 true	Static Equity	
margin_position	decimal	 true	Position Margi(the margin for holding currenty positions)	
margin_frozen	decimal	 true	Frozen Margin	
margin_available	decimal	 true	Available Margin	
profit_real	decimal	 true	Realized Profits&Losses	
profit_unreal	decimal	 true	Unrealized Profits&Losses	
risk_rate	decimal	 true	Margin Ratio	
liquidation_price	decimal	 true	Liquidation Price	
withdraw_available	decimal	 true	Assets available to withdraw	
lever_rate	int	 true	Leverage	
adjust_factor	decimal	 true	Adjustment Factor	
margin_mode	string	 true	margin mode isolated : "isolated"	
margin_account	string	 true	margin account "BTC-USDT"...	
position_mode	string	 true	position mode single_side，dual_side	
</data>		 false		
Subscription Example
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"accounts.BTC-USDT"
}
Example of a Successful Subscription
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"accounts.BTC-USDT"
"ts":1670903745088
"err-code":0
}
Example of a Data Update
{
"op":"notify"
"topic":"accounts.btc-usdt"
"ts":1603711370689
"event":"order.open"
"data":[
0:{
"symbol":"BTC"
"contract_code":"BTC-USDT"
"margin_balance":79.72434662
"margin_static":79.79484662
"margin_position":1.31303
"margin_frozen":4.0662
"margin_available":74.34511662
"profit_real":0.03405608
"profit_unreal":-0.0705
"withdraw_available":74.34511662
"risk_rate":14.745772976801513
"liquidation_price":92163.42096277916
"lever_rate":10
"adjust_factor":0.075
"margin_asset":"USDT"
"margin_mode":"isolated"
"margin_account":"BTC-USDT"
"position_mode":"dual_side"
}




ositions_cross.$contract_code ([Cross] Subscribe Position Updates（sub）)
Signature verification: No

Interface permission: Read

Rate Limit: WebSocket, the private order push interface, requires API KEY Verification:

Each UID can build at most create 30 WS connections for private order push at the same time. For each account, contracts of the same underlying coin only need to subscribe one WS order push, e.g. users only need to create one WS order push connection for BTC Contract which will automatically push orders of BTC-USDT contracts. Please note that the rate limit of WS order push and RESTFUL private interface are separated from each other, with no relations.

Interface description: The interface only supports cross margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-notification
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-notification
Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
positions_cross.*	positions_cross.*	Allowed
positions_cross.contract_code1	positions_cross.*	Allowed
positions_cross.contract_code1	positions_cross.contract_code1	Allowed
positions_cross.contract_code1	positions_cross.contract_code1	Not Allowed
positions_cross.*	positions_cross.contract_code1	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	all: *(swap and future), swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
cid	string	 false	Current request's ID	
Data Update
Parameter	Data Type	Required	Description	Value Range
op	string	 false	operaton name, fixed as notify;	
topic	string	 true	topic	
ts	long	 true	server response timestamp	
uid	string	 true	uid	
event	string	 true	Related events of position change notification	notification on account asset change such as commit order(order.open), fulfill order(order.match)(excluding liquidated order and settled orders), settlement and delivery(settlement), fulfill liquidation order(order.liquidation)(including voluntarily fulfilled liquidation order and the fulfilled liquidation order taken over by system ) , cancel order(order.cancel), asset transfer（contract.transfer) (ncluding transfer with exchange accounts, transfer between main account and sub-account, and tranfer between different margin accounts.), system (contract.system), other asset change(other), switch leverage(switch_lever_rate), initial margin(init), ADL trade
<data>	object array	 true		
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
margin_mode	string	 true	margin mode	cross: cross margin mode
margin_account	string	 true	margin account	"USDT"...
volume	decimal	 true	position quantity	
available	decimal	 true	positions available to close	
frozen	decimal	 true	positions frozen	
cost_open	decimal	 true	opening average price	
cost_hold	decimal	 true	average price of position	
profit_unreal	decimal	 true	unrealized profits and losses	
profit_rate	decimal	 true	profit rate	
profit	decimal	 true	profit	
margin_asset	string	 true	margin asset	
position_margin	decimal	 true	position margin	
lever_rate	int	 true	leverage	
direction	string	 true	transaction direction of positions	"buy":long "sell":short
last_price	decimal	 true	latest trade price	
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
position_mode	string	 true	position mode	single_side，dual_side
adl_risk_percent	decimal	 false	The risk level of the current position being forced to reduce the position by adl(Pushed every 5 seconds, not updated in real time)	1、2、3、4、5
</data>		 false		
Notes: 
A regular push of position is performed every 5 sedconds.The event field of the reponse is "snapshot".If there is a push in 5 seconds, snapshot push will be skipped.
When switching leverage with no positions, the event "switch_lever_rate" will not be pushed by the position topic.
In the one-way position mode: only push the data of contract which with the position (that is, only push the data of the one-way non-empty position), if there is no position, it will not be pushed

Subscription Example
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"positions_cross.BTC-USDT"
}
Example of a Successful Subscription
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"positions_cross.BTC-USDT"
"ts":1670903745088
"err-code":0
}
Example of a Data Update
{
"op":"notify"
"topic":"positions_cross.btc-usdt"
"ts":1639107468139
"event":"order.match"
"data":[
0:{
"contract_type":"swap"
"pair":"BTC-USDT"
"business_type":"swap"
"symbol":"BTC"
"contract_code":"BTC-USDT"
"volume":1
"available":1
"frozen":0
"cost_open":48284.9
"cost_hold":48284.9
"profit_unreal":-0.0001
"profit_rate":-0.000010355204214985
"profit":-0.0001
"margin_asset":"USDT"
"position_margin":9.65696
"lever_rate":5
"direction":"buy"
"last_price":48284.8
"margin_mode":"cross"
"margin_account":"USDT"
"position_mode":"dual_side"
"adl_risk_percent":"3"
}
]
"uid":"123456789"
}
Example of a Subscription Cancellation
{
"op":"unsub"
"topic":"positions_cross.BTC-USDT"
"cid":"40sG903yz80oDFWr"
}




matchOrders.$contract_code ([Isolated] Subscribe Match Order Data（sub))
Signature verification: No

Interface permission: Read

Rate Limit: WebSocket, the private order push interface, requires API KEY Verification:

Each UID can build at most create 30 WS connections for private order push at the same time. For each account, contracts of the same underlying coin only need to subscribe one WS order push, e.g. users only need to create one WS order push connection for BTC Contract which will automatically push orders of BTC-USDT contracts. Please note that the rate limit of WS order push and RESTFUL private interface are separated from each other, with no relations.

Interface description: This interface only supports isolated margin mode.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-notification
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-notification
Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
matchOrders.*	matchOrders.*	Allowed
matchOrders.contract_code1	matchOrders.*	Allowed
matchOrders.contract_code1	matchOrders.contract_code1	Allowed
matchOrders.contract_code1	matchOrders.contract_code1	Not Allowed
matchOrders.*	matchOrders.contract_code1	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	"*" all(it means to subscribe the all match orders) "BTC-USDT"...
cid	string	 false	Current request's ID	
Notes: 
The order status of 'post_only' type pushed by ws is ethier '7:canceled' or '3:submitted'.
The orders will be pushed when matched by matching engine.
The delivery orders will not be pushed.
The orders transfered from future or to future will not be pushed.
The netting and forced liquidation orders will not be pushed.
The orders will generally be pushed faster than the normal orders subscription.But It's not guranted.
If there is an order with N trades,including 1 taker and N maker,it will push N+1 trades at most.

Data Update
Parameter	Data Type	Required	Description	Value Range
op	string 	 false	notify	
topic	string	 true	topic	
ts	long	 true	server response timestamp	
uid	string	 true	account uid	
symbol	string	 true	symbol	"BTC","ETH"...
contract_code	string	 true	contract code	
status	int	 true	1. Ready to submit the orders; 2. Ready to submit the orders; 3. Have sumbmitted the orders; 4. Orders partially matched; 5. Orders cancelled with partially matched; 6. Orders fully matched; 7. Orders cancelled;	
order_id	long	 true	order id	
order_id_str	string	 true	order id	
client_order_id	long	 true	client order id	
order_type	int	 true	order_type	1. Quotation; 2. Cancelled order; 3. Forced liquidation; 4. Delivery Order
trade_volume	decimal	 true	trade volume	
volume	decimal	 true	volume	
direction	string	 true	direction	"buy" : "sell"
offset	string	 true	offset	"open", "close", "both"
lever_rate	int	 true	lever rate	
price	decimal	 true	price	
created_at	long	 true	created time	
order_source	string	 true	order source	system、web、api、m、risk、settlement、ios、android、windows、mac、trigger、tpsl
order_price_type	string	 true	type of order price	"market": Market Order，"limit”: Limit Order "opponent":BBO "post_only": Post-Only Order, No order limit but position limit for post-only orders.,optimal_5： Optimal , optimal_10： Optimal 10, optimal_20：Optimal 20，ioc: IOC Order,，fok：FOK Order, "opponent_ioc"：IOC order using the BBO price，"optimal_5_ioc"：optimal_5 IOC，"optimal_10_ioc"：optimal_10 IOC，"optimal_20_ioc"：optimal_20 IOC, "opponent_fok"：FOK order using the BBO price，"optimal_5_fok"：optimal_5 FOK，"optimal_10_fok"：optimal_10 FOK，"optimal_20_fok"：optimal_20 FOK
margin_mode	string	 true	margin mode	isolated : "isolated"
margin_account	string	 true	margin account	"BTC-USDT"...
is_tpsl	int	 true	whether to set take-profit and stop-loss order	1：yes；0：no
reduce_only	int	 true	reduce only	0: no, 1: yes
<trade>	object array	 true		
id	string	 true	the global unique id of the trade.	
trade_id	long	 true	In this interface, trade_id is the same with match_id of linear-swap-api/v1/swap_matchresults. trade_id is the result of sets of order execution and trade confirmation. NOTE: trade_id is not unique, which includes all trade records of a taker order and N maker orders. If the taker order matches with N maker orders, it will create N trades with same trade_id.	
trade_price	decimal	 true	trade price	
trade_volume	decimal	 true	trade volume（cont）	
trade_turnover	decimal	 true	trade turnover	
created_at	long	 true	created time	
role	string	 true	taker or maker	
self_match_prevent	int	 false	Self trading prevention	0 means self-trading is allowed, 1 means self-trading is not allowed, which means canceling taker orders and retaining maker orders. The default value is 1.
</trade>		 false		
self_match_prevent_new	string	 true	Prevent self-trading	cancel_taker: Cancel a taker order cancel_maker: Cancel a maker order  cancel_both: Cancel all orders allow: Allow self-trading
Subscription Example
{
"op":"sub"
"topic":"matchOrders.BTC-USDT"
"cid":"40sG903yz80oDFWr"
}
Example of a Successful Subscription
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"matchOrders.BTC-USDT"
"ts":1670903745088
"err-code":0
}
Example of a Data Update
{
"op":"notify"
"topic":"matchOrders.btc-usdt"
"ts":1600926986125
"symbol":"BTC"
"contract_code":"BTC-USDT"
"status":6
"order_id":758688290195656700
"order_id_str":"758688290195656704"
"client_order_id":NULL
"order_type":1
"created_at":1600926984112
"trade":[
0:{
"trade_id":14470
"id":"14470-758688290195656704-1"
"trade_volume":1
"trade_price":10329.11
"trade_turnover":103.2911
"created_at":1600926986046
"role":"taker"
}
]
"uid":"123456789"
"volume":1
"trade_volume":1
"direction":"buy"
"offset":"open"
"lever_rate":5
"price":10329.11
"order_source":"web"
"order_price_type":"opponent"
"margin_mode":"isolated"
"margin_account":"BTC-USDT"
"is_tpsl":0
"reduce_only":0
"self_match_prevent_new":"cancel_both"
}
Example of a Subscription Cancellation
{
"op":"unsub"
"topic":"matchOrders.BTC-USDT"
"cid":"40sG903yz80oDFWr"
}




rigger_order_cross.$contract_code ([Cross] Subscribe trigger orders updates(sub))
Signature verification: No

Interface permission: Read

Rate Limit: WebSocket, the private order push interface, requires API KEY Verification:

Each UID can build at most create 30 WS connections for private order push at the same time. For each account, contracts of the same underlying coin only need to subscribe one WS order push, e.g. users only need to create one WS order push connection for BTC Contract which will automatically push orders of BTC-USDT contracts. Please note that the rate limit of WS order push and RESTFUL private interface are separated from each other, with no relations.

Interface description: The interface only supports cross margin mode.

The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.

Subscription Address
Environment	Address
Online	wss://api.hbdm.com/linear-swap-notification
Online  (preferred by aws customers)	wss://api.hbdm.vn/linear-swap-notification
Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
trigger_order_cross.*	trigger_order_cross.*	Allowed
trigger_order_cross.contract_code1	trigger_order_cross.*	Allowed
trigger_order_cross.contract_code1	trigger_order_cross.contract_code1	Allowed
trigger_order_cross.contract_code1	trigger_order_cross.contract_code1	Not Allowed
trigger_order_cross.*	trigger_order_cross.contract_code1	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description	Value Range
contract_code	string	 true	contract code	all: *(swap and future), swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
cid	string	 false	Current request's ID	
Data Update
Parameter	Data Type	Required	Description	Value Range
op	string	 true	operaton name, fixed as notify	
topic	string	 true	topic	
ts	long	 true	Time of Respond Generation, Unit: Millisecond	
uid	string	 true	uid	
event	string	 true	event	order，cancel，trigger_success，trigger_fail
<data>	object array	 true		
symbol	string	 true	symbol	
contract_code	string	 true	contract code	swap: "BTC-USDT"... , future: "BTC-USDT-210625" ...
margin_mode	string	 true	margin mode	cross: cross margin mode
margin_account	string	 true	margin account	"USDT"...
trigger_type	string	 true	trigger type： ge great than or equal to；le less than or equal to	
volume	decimal	 true	place volume	
order_type	int	 true	order type	1. Place orders
direction	string	 true	direction	"buy"/"sell"
offset	string	 true	"open", "close"	"open","close",both
lever_rate	int	 true	leverage	
order_id	decimal	 true	order ID	
order_id_str	string	 true	order ID	
relation_order_id	string	 true	Relation order ID is the string related to the limit orders, The value is -1 before the trigger orders executed.	
order_price_type	string	 true	type of order price	"limit"，"optimal_5"，"optimal_10"，"optimal_20"
status	int	 true	order status	2. Ready to submit the orders; 4. Orders partially matched; 5. Orders cancelled with partially matched; 6. Orders fully matched;
order_source	string	 true	order source	system、web、api、m、risk、settlement、ios、android、windows、mac、trigger
trigger_price	decimal	 true	trigger price	
triggered_price	decimal	 true	triggered price	
order_price	decimal	 true	order price	
created_at	long	 true	created time	
triggered_at	long	 true	triggered time	
order_insert_at	long	 true	insert time	
canceled_at	long	 true	canceled time	
fail_code	int	 true	fail code	
fail_reason	string	 true	fail reason	
contract_type	string	 true	contract type	swap, this_week, next_week, quarter, next_quarter
pair	string	 true	pair	such as: “BTC-USDT”
business_type	string	 true	business type	futures, swap
reduce_only	int	 true	reduce only	0: no, 1: yes
</data>		 false		
Notes: 
The intermediate states processed by the order status system will not be pushed, such as in the progress of placing an order, The descriptions of specific event notifications are as below:
when the order status is 2（Submitted），event notification is order（trigger order placed successfully）；
when the order status is 4（Order placed successfully），event notification is trigger_success（trigger order triggered successfully）；
when the order status is 6（Canceled），event notification is cancel（trigger order canceled successfully）；
when the order status is 5（Order failed to be placed），event notification is trigger_fail（trigger order failed to be triggered）；
Single coin cannot be re-suscribed, and all coins subscription can cover single coin subscription; single coin cannot be subscribed after subscribing all coins.

Subscription Example
{
"op":"sub"
"topic":"trigger_order_cross.BTC-USDT"
"cid":"40sG903yz80oDFWr"
}
Example of a Successful Subscription
{
"op":"sub"
"cid":"40sG903yz80oDFWr"
"topic":"trigger_order.BTC-USDT"
"ts":1670903745088
"err-code":0
}
Example of a Data Update
{
"op":"notify"
"topic":"trigger_order_cross.*"
"ts":1639123353369
"event":"order"
"uid":"123456789"
"data":[
0:{
"contract_type":"swap"
"pair":"BTC-USDT"
"business_type":"swap"
"symbol":"BTC"
"contract_code":"BTC-USDT"
"trigger_type":"le"
"volume":1
"order_type":1
"direction":"buy"
"offset":"open"
"lever_rate":1
"order_id":918895474461802500
"order_id_str":"918895474461802496"
"relation_order_id":"-1"
"order_price_type":"limit"
"status":2
"order_source":"api"
"trigger_price":40000
"triggered_price":NULL
"order_price":40000
"created_at":1639123353364
"triggered_at":0
"order_insert_at":0
"canceled_at":0
"fail_code":NULL
"fail_reason":NULL
"margin_mode":"cross"
"margin_account":"USDT"
"reduce_only":0
}
]
}
Example of a Subscription Cancellation
{
"op":"unsub"
"topic":"trigger_order_cross.BTC-USDT"
"cid":"40sG903yz80oDFWr"
}








Permission	Content Type	Interface Mode	Request Method	Type	Description	Authentication Required
Read	Market Data Interface	general	market.$contract_code.kline.$period	sub	Subscribe KLine data	No
Read	Market Data Interface	general	market.$contract_code.kline.$period	req	Request Kline Data	No
Read	Market Data Interface	general	market.$contract_code.depth.$type	sub	Subscribe Market Depth Data	No
Read	Market Data Interface	general	market.$contract_code.depth.size_${size}.high_freq	sub	Subscribe Incremental Market Depth Data	No
Read	Market Data Interface	general	market.$contract_code.bbo	sub	Subscribe market BBO data push	No
Read	Market Data Interface	general	market.$contract_code.detail	sub	Subscribe Market Detail Data	No
Read	Market Data Interface	general	market.$contract_code.trade.detail	req	Request Trade Detail Data	No
Read	Market Data Interface	general	market.$contract_code.trade.detail	sub	Subscribe Trade Detail Data	No
Read	Index and Basis Interface	general	market.$contract_code.index.$period	sub	Subscribe Index Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.index.$period	sub	Request Index Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.basis.$period.$basis_price_type	sub	Subscribe Basis Data	No
Read	Index and Basis Interface	general	market.$contract_code.basis.$period.$basis_price_type	req	Request Basis Data	No
Read	Index and Basis Interface	general	market.$contract_code.premium_index.$period	sub	Subscribe Premium Index Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.premium_index.$period	req	Request Premium Index Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.estimated_rate.$period	sub	Subscribe Estimated Funding Rate Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.estimated_rate.$period	req	Request Estimated Funding Rate Kline Data	No
Read	Index and Basis Interface	general	market.$contract_code.mark_price.$period	sub	Subscribe Kline Data of Mark Price	No
Read	Index and Basis Interface	general	market.$contract_code.mark_price.$period	req	Request Kline Data of Mark Price	No
Read	Trade Interface	general	public.$contract_code.liquidation_orders	sub	Subscribe Liquidation Orders (no authentication) (sub)	No
Read	Trade Interface	general	public.$contract_code.funding_rate	sub	Subscribe funding rate (no authentication)（sub）	No
Read	Trade Interface	general	public.$contract_code.contract_info	sub	Subscribe Contract Info (no authentication)（sub）	No
Read	Trade Interface	Isolated Margin	orders.$contract_code	sub	Subscribe Order Data(sub)	Yes
Read	Account Interface	Isolated Margin	accounts.$contract_code	sub	Subscribe Account Equity Updates Data(sub)	Yes
Read	Account Interface	Isolated Margin	positions.$contract_code	sub	Subscribe Position Updates(sub)	Yes
Read	Trade Interface	Isolated Margin	matchOrders.$contract_code	sub	Subscribe Match Order Data（sub)	Yes
Read	Trade Interface	Isolated Margin	trigger_order.$contract_code	sub	Subscribe trigger orders updates(sub)	Yes
Read	Account Interface	cross margin	orders_cross.$contract_code	sub	Subscribe Order Data	Yes
Read	Account Interface	cross margin	accounts_cross.$margin_account	sub	Subscribe Account Equity Updates Data	Yes
Read	Trade Interface	cross margin	positions_cross.$contract_code	sub	Subscribe Position Updates	Yes
Read	Trade Interface	cross margin	matchOrders_cross.$contract_code	sub	Subscribe Match Order Data	Yes
Read	Trade Interface	cross margin	trigger_order_cross.$contract_code	sub	Subscribe trigger orders updates(sub)	Yes
Read	System Status Interface	cross margin	public.$service.heartbeat	sub	Subscription system status updates





Market Data Request and Subscription: wss://api.hbdm.com/linear-swap-ws

Order Push Subscription: wss://api.hbdm.com/linear-swap-notification

Index Kline Data and Basis Data Subscription: wss://api.hbdm.com/ws_index

System status updates subscription ：wss://api.hbdm.com/center-notification

If the url: api.hbdm.com can't be accessed, please use the url below:

Market Data Request and Subscription Address: wss://api.btcgateway.pro/linear-swap-ws;

Order Push Subscription：wss://api.btcgateway.pro/linear-swap-notification

Index Kline Data and Basis Data Subscription: wss://api.btcgateway.pro/ws_index

System status updates subscription ：wss://api.btcgateway.pro/center-notification

If you have further queries about HTX USDT Margined Contracts order push subscription, please refer to Demo

Note:
If you can't connect "https://api.hbdm.com", please use "https://api.btcgateway.pro" for debug purpose. If your server is deployed in AWS, we recommend using "https://api.hbdm.vn".






There is rate limit for both public and private interfaces. More details are laid out as below:

Generally, the private interface rate limit of API key is at most 144 times every 3 seconds for each UID (Trade Interface: at most 72 times every 3 seconds. Read Interface: at most 72 times every 3 seconds) (this rate limit is shared by all the altcoins contracts delivered by different date).

For public interfaces used to get information of non-market data (such as request information of index, price limit, delivery and settlement, positions, etc.), the rate limit for each IP is 240 times every 3 seconds. (Please note that the 240 times/3s rate limit is shared by all the requests for non-market data under this UID)

For public interface to get market data such as Get Kline data, Get Market Data Overview, Get Contract Information,Get market in-depth data, Get premium index Kline, Get real-time forecast capital rate kline, Get basis data, Get the last Trade of a Contract and so on：

(1) For restful interfaces, products, (future, coin margined swap, usdt margined Contracts)800 times/second for one IP at most　　 (2) The rate limit for “req” request is 50 times/s at most. No limit for “sub” request as the data will be pushed by server voluntarily.

The order push private WebSocket interface requires API Key for authentication.

Each UID can create 30 WS connections at most for private order push at the same time. The user under this UID only need to subscribe one WS order push for the contracts of the same underlying coins. For example, users only need to create one WS order push connection for BTC Contract, which our system will automatically push orders of BTC weekly, BTC biweekly and BTC quarterly contracts via this connection.

Note: The rate limit of WS order push and RESTFUL private interface are separated from each other with no relations.

40 subscriptions at most can be sent in one second in websocket connections.
Response the following strings for “Header” via API

ratelimit-limit： the upper request limit per time, unit: times

ratelimit-interval： reset interval(reset the number of request ), unit: ms

ratelimit-remaining： available request number left in this round, unit: times

ratelimit-reset： upper limit of reset time used to request number， unit: ms







WebSocket API supports two-way heartbeat. Both Server and Client can send ping message, which the opposite side can return with pong message.

WebSocket Server sends heartbeat：
{"ping": 18212558000}

WebSocket Client should respond:：
{"pong": 18212558000}

Note: Once the WebSocket Client and WebSocket Server get connected, the server will send a heartbeat every 5 seconds (the frequency might change). The connection will get disconnected automatically if the WebSocket Client ignores the heartbeat message for 5 times. The server will remain connection if the WebSocket Client responds one “ping” value within the latest 2 heartbeat messages.




During making connection and authentication, server will disconnect connection automatically when error occurs. Before disconnecting, server will send notification below,

{

`"op": "close", // represents server disconnect connection voluntarily

`"ts": long // Server pushes local timestamp

}




After authentication, if clients encountered internal error or request data out from Operator List, WebSocket server will return error message. But server will remain connection

{

"op": "error", // means server receive data out from Operator List or clients got internal error

"ts": long// Server pushes local timestamp

}




Type	Description
ping	Server sends heatbeat with a Ping
pong	Clients responds heatbeat with a Pong
auth	Authentication
sub	Subscribe Message
unsub	Unsubscribe Message
notify	Server pushes subscribe message


Type	applicative operator type	Description
orders.$contract_code	sub,ubsub	Subscribe/unsubscribe the order data of a given pair; when the $contract_code value is *, it stands for subscribing/unsubscribing the data of all pairs


Return Error Code	Return description
0	Request successfully.
2001	Invalid authentication.
2002	Authentication required.
2003	Authentication failed.
2004	Number of visits exceeds limit.
2005	Connection has been authenticated.
2007	You don’t have access permission as you have not opened contracts trading.
2010	Topic error.
2011	Contract doesn't exist.
2012	Topic not subscribed.
2013	Authentication type doesn't exist.
2014	Repeated subscription.
2020	This contract does not support cross margin mode.
2021	Illegal parameter margin_account.
2030	Exceeds connection limit of single user.
2040	Missing required parameter.





https://status-linear-swap.huobigroup.com/api/v2/summary.json ([General]Get system status)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: For public interface used to get information of index, price limit, settlement, delivery, open positions and so on, the rate limit is 240 times every 3 second at most for each IP (this 240 times every 3 second public interface rate limit is shared by all the requests from that IP of non-marketing information, like above).

Interface description: This endpoint allows users to get system status, Incidents and planned maintenance.

The system status can also be obtained through email, SMS, webhook, RSS/Atom feed. Users can You can click here to subscribe. The subscription function depends on Google services. Before you subscribe, please ensure that you can access Google services normally.

Request Address
Environment	Address
Online	https://status-linear-swap.huobigroup.com/api/v2/summary.json
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes:  
No parameters are needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
page		 false	basic information of status page
{id	string	 false	page id
name	string	 false	page name
url	string	 false	page url
time_zone	string	 false	time zone
updated_at}	string	 false	page update time
components		 false	System components and their status
[{id	string	 false	component id
name	string	 false	component name, including Order submission, Order cancellation, Deposit etc.
status	string	 false	component status, value range: operational, degraded_performance, partial_outage, major_outage, under maintenance
created_at	string	 false	component create time
updated_at	string	 false	component update time
.......}]		 false	for details of other fields, please refer to the return example
incidents		 false	System fault incident and their status. If there is no fault at present, it will return to null
[{id	string	 false	incident id
name	string	 false	incident name
status	string	 false	incident staus, value range: investigating, identified, monitoring, resolved
created_at	string	 false	incident creat time
updated_at	string	 false	incident update time
.......}]		 false	for details of other fields, please refer to the return example
scheduled_maintenances		 false	System scheduled maintenance incident and status. If there is no scheduled maintenance at present, it will return to null
[{id	string	 false	incident id
name	string	 false	incident name
status	string	 false	incident staus, value range: scheduled, in progress, verifying, completed
created_at	string	 false	incident creat time
updated_at	string	 false	incident update time
scheduled_for	string	 false	scheduled maintenance start time
scheduled_until	string	 false	scheduled maintenance end time
.......}]		 false	for details of other fields, please refer to the return example
status		 false	The overall current status of the system
{indicator	string	 false	system indicator, value range: none, minor, major, critical, maintenance
description}	string	 false	system description, value range: All Systems Operational, Minor Service Outager, Partial System Outage, Partially Degraded Service, Service Under Maintenance
Request example
curl "https://status-linear-swap.huobigroup.com/api/v2/summary.json"
Response Example
Success Example
{
"page":{
"id":"p0qjfl24znv5"
"name":"HTX Futures-USDT-margined Swaps"
"url":"https://status-linear-swap.huobigroup.com"
"time_zone":"Asia/Singapore"
"updated_at":"2020-02-07T10:25:14.717Z"
}
"components":[
0:{
"id":"h028tnzw1n5l"
"name":"Deposit"
"status":"operational"
"created_at":"2019-12-05T02:07:12.372Z"
"updated_at":"2020-02-07T09:27:15.563Z"
"position":1
"description":NULL
"showcase":true
"group_id":"gtd0nyr3pf0k"
"page_id":"p0qjfl24znv5"
"group":false
"only_show_if_degraded":false
}
]
"incidents":[
0:{
"id":"rclfxz2g21ly"
"name":"Market data is delayed"
"status":"investigating"
"created_at":"2020-02-11T03:15:01.913Z"
"updated_at":"2020-02-11T03:15:02.003Z"
"monitoring_at":NULL
"resolved_at":NULL
"impact":"minor"
"shortlink":"http://stspg.io/pkvbwp8jppf9"
"started_at":"2020-02-11T03:15:01.906Z"
"page_id":"p0qjfl24znv5"
"incident_updates":[
0:{
"id":"dwfsk5ttyvtb"
"status":"investigating"
"body":"Market data is delayed"
"incident_id":"rclfxz2g21ly"
"created_at":"2020-02-11T03:15:02.000Z"
"updated_at":"2020-02-11T03:15:02.000Z"
"display_at":"2020-02-11T03:15:02.000Z"
"affected_components":[
0:{
"code":"nctwm9tghxh6"
"name":"Market data"
"old_status":"operational"
"new_status":"degraded_performance"
}
]
"deliver_notifications":true
"custom_tweet":NULL
"tweet_id":NULL
}
]
"components":[
0:{
"id":"nctwm9tghxh6"
"name":"Market data"
"status":"degraded_performance"
"created_at":"2020-01-13T09:34:48.284Z"
"updated_at":"2020-02-11T03:15:01.951Z"
"position":8
"description":NULL
"showcase":false
"group_id":NULL
"page_id":"p0qjfl24znv5"
"group":false
"only_show_if_degraded":false
}
]
}
]
"scheduled_maintenances":[
0:{
"id":"k7g299zl765l"
"name":"Schedule maintenance"
"status":"scheduled"
"created_at":"2020-02-11T03:16:31.481Z"
"updated_at":"2020-02-11T03:16:31.530Z"
"monitoring_at":NULL
"resolved_at":NULL
"impact":"maintenance"
"shortlink":"http://stspg.io/md4t4ym7nytd"
"started_at":"2020-02-11T03:16:31.474Z"
"page_id":"p0qjfl24znv5"
"incident_updates":[
0:{
"id":"8whgr3rlbld8"
"status":"scheduled"
"body":"We will be undergoing scheduled maintenance during this time."
"incident_id":"k7g299zl765l"
"created_at":"2020-02-11T03:16:31.527Z"
"updated_at":"2020-02-11T03:16:31.527Z"
"display_at":"2020-02-11T03:16:31.527Z"
"affected_components":[
0:{
"code":"h028tnzw1n5l"
"name":"Deposit And Withdraw - Deposit"
"old_status":"operational"
"new_status":"operational"
}
]
"deliver_notifications":true
"custom_tweet":NULL
"tweet_id":NULL
}
]
"components":[
0:{
"id":"h028tnzw1n5l"
"name":"Deposit"
"status":"operational"
"created_at":"2019-12-05T02:07:12.372Z"
"updated_at":"2020-02-10T12:34:52.970Z"
"position":1
"description":NULL
"showcase":false
"group_id":"gtd0nyr3pf0k"
"page_id":"p0qjfl24znv5"
"group":false
"only_show_if_degraded":false
}
]
"scheduled_for":"2020-02-15T00:00:00.000Z"
"scheduled_until":"2020-02-15T01:00:00.000Z"
}
]
"status":{
"indicator":"minor"
"description":"Partially Degraded Service"
}
}





public.$contract_code.contract_info ([General] Unsubscribe Contract Info Data(no authentication)(unsub))
Signature verification: No

Interface permission: Read

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address

No data

Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
public.*.contract_info	public.*.contract_info	Allowed
public.contract_code1.contract_info 	public.*.contract_info	Allowed
public.contract_code1.contract_info 	public.contract_code1.contract_info 	Allowed
public.contract_code1.contract_info 	public.contract_code1.contract_info 	Not Allowed
public.*.contract_info	public.contract_code1.contract_info 	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description
contract_code	string	 true	* all(it means to unsubscribe the all orders) BTC-USDT,ETH-USDT...
Notes: 
The request parameter "contract_code" supports the contract code of futures, in that the format is BTC-USDT-210625.
unsubscripting * is ok under business_type filled in. when business_type is swap, unsubscripting * means to unsubscripting all swap contracts; when business_type is futures, unsubscripting * means to unsubscripting all futures contracts;
unsubscription scope must be greater than or equal to the subscription scope and in that it just can be success.

Data Update
Parameter	Data Type	Required

No data

Subscription Example
{
"op":"unsub"
"topic":"public.BTC-USDT.contract_info"
"cid":"40sG903yz80oDFWr"
}





public.$contract_code.funding_rate ([General] Unsubscribe Funding Rate Data(no authentication)(unsub))
Signature verification: No

Interface permission: Read

Interface description: The interface supports cross margin mode and isolated margin mode.

Subscription Address
Environment	Address

No data

Request Parameter
Field Name	Type	Description
op	string	Required； Operator Name，value for unsubscribe is unsub;
cid	string	Optional; ID Client requests unique ID
topic	string	Required；Unsubscribe Topic Name, format: orders.$contract_code; For parameter details please check req Subscribe Parameter
Rule description
Subscribe(sub)	Unsubscribe( unsub )	Rule
public.*.funding_rate	public.*.funding_rate	Allowed
public.contract_code1.funding_rate	public.*.funding_rate	Allowed
public.contract_code1.funding_rate	public.contract_code1.funding_rate	Allowed
public.contract_code1.funding_rate	public.contract_code1.funding_rate	Not Allowed
public.*.funding_rate	public.contract_code1.funding_rate	Not Allowed
Subscription Parameter
Parameter	Data Type	Required	Description
contract_code	string	 true	* all(it means to unsubscribe the all orders) BTC-USDT,ETH-USDT...
Data Update
Parameter	Data Type	Required

No data

Subscription Example
{
"op":"unsub"
"topic":"public.BTC-USDT.funding_rate"
"cid":"40sG903yz80oDFWr"








Error Code	Error Description
1000	System error.
1001	The system is not ready.
1002	Inquiry error. Please try again later.
1003	Redis error.
1004	System busy. Please try again later.
1005	Query timeout, please try again.
1010	Account doesn't exist.
1011	The user's session doesn't exist.
1012	The user's account doesn't exist.
1013	This contract symbol doesn't exist.
1014	This contract doesn't exist.
1015	The index price does not exist.
1016	The bid/ask price does not exist. Please input the price.
1017	Order doesn't exist.
1018	Main account doesn't exist.
1019	Your main account is not whitelisted for opening subaccounts.
1020	The number of your subaccounts has exceeded the limit. Please contact customer service.
1021	Failed to open an account. Your main account has not been activated for futures trading. Please activate before trading.
1029	{0}
1030	Input error.
1031	Illegal request.
1032	Maximum number of access attempts exceeded.
1033	Contract expiration value error.
1034	Order quotation type value error.
1035	Order side value error.
1036	Order open/close value error.
1037	The leverage is invalid. Please contact the customer service.
1038	The price has exceeded the precision limit. Please modify and place order again.
1039	Buy price must be lower than {0}{1}. Sell price must be higher than {2}{3}.
1040	The amount cannot be left empty or smaller than the value of one contract. Please modify and place order again.
1041	The amount has exceeded the limit ({0} Cont), please modify and place order again.
1042	The total positions (this order + open orders + positions) have exceeded the long-position limit ({0}{1}). Please modify.
1043	The total positions (this order + open orders + positions) have exceeded the short-position limit ({0}{1}). Please modify.
1044	The position limit has been triggered. Please modify.
1045	Unable to change leverage due to open orders.
1046	The position for this contract does not exist.
1047	Insufficient margin available.
1048	Insufficient open positions to be closed. Please check whether there are open orders under "Limit Orders".
1049	Market price is not supported at the moment for opening a position.
1050	Duplicate order number
1051	No cancellable orders.
1052	The number of batch canceling/placing has exceeded the limit.
1053	Unable to access the latest price range.
1054	Unable to access the latest price.
1055	Invalid price as it would cause the account equity to be less than zero. Please modify the price and place the order again.
1056	Settling. Unable to place/cancel orders currently.
1057	Orders cannot be placed during a trading halt.
1058	Orders cannot be placed while the target token is suspended for trading.
1059	Delivering contracts. Unable to place/cancel orders currently.
1060	Orders cannot be placed as the futures contracts are not in trading hours.
1061	The order does not exist.
1062	Canceling. Thank you for your patience.
1063	The order has been executed.
1064	The main key of order conflicts.
1065	Customer order numbers should be integers.
1066	{0} cannot be empty.
1067	Illegal parameter {0}.
1068	Export error
1069	Invalid price
1070	Exporting failed as the data is null.
1071	Repeated cancellation. Your order has been canceled.
1072	Sell price must be lower than {0}{1}.
1073	Position abnormal. Please contact the customer service.
1074	Order placement error. Please contact customer service.
1075	Invalid price as it would cause the margin rate to be less than zero. Please modify the price and place the order again.
1076	No data in the order book. Please try again later.
1077	Delivering and settling contracts. Unable to access the current contract.
1078	Delivering and settling contracts. Unable to access some contracts.
1079	Delivering and settling contracts. Unable to access the position of the current contract.
1080	Delivering and settling contracts. Unable to access the positions of some contracts.
1081	The number of your trigger orders for {0} Perpetual Futures shall not exceed {1}.
1082	Trigger type parameter error
1083	Your position has been taken over for liquidation. Unable to place orders now.
1084	Your contract API is disabled, please try again after {0} (GMT+8).
1085	Failed to place the trigger order. Please modify the price and place the order again, or contact customer service.
1086	{0} contracts do not support opening positions on {1} at the moment. Please contact customer service.
1087	{0} contracts do not support closing positions on {1} at the moment. Please contact customer service.
1088	{0} contracts do not support cancellation on {1} at the moment. Please contact customer service.
1089	Transfer service is temporarily suspended for {0} account. Please contact customer service.
1090	Cannot place this order as the margin ratio is \u2265 100%.
1091	Cannot place this order as the account equity is less than 0.
1092	The bid/ask {0} price is adopted for Flash Close. The account equity would be less than zero if this order was placed. Please manually input a valid price or place an order with the BBO price.
10921	The account equity would be less than zero if this order was placed. Please enter a new price or place the order at BBO price.
1093	The bid/ask {0} price is adopted for Flash Close. The margin rate would be less than zero if this order was placed. Please manually input a valid price or place an order with the BBO price.
10931	The margin rate will decline to below 0 if this order is placed. Please enter a new price or place order at BBO price.
1094	Leverage cannot be empty. Please choose leverage or contact customer service.
1095	Cannot change leverage as the futures contracts are not in trading hours.
1096	When the balance of the trial bonus accounts for the net available amount of {0}, the trial bonus is only used for open positions
1097	adl freeze status prohibits users from placing orders
1098	adl frozen status prohibits transfer
1099	Transfer is temporarily restricted for {0} account, please contact customer service support.
1100	You have no permission to open positions. Please contact customer service.
1101	You have no permission to close positions. Please contact customer service.
1102	You have no permission to transfer in. Please contact customer service.
1103	You have no permission to transfer out. Please contact customer service.
1104	The current trading is not permitted due to futures trading restrictions.
1105	You can only close this position due to futures trading restrictions.
1106	You can only close this position due to futures trading restrictions.
1108	Dubbo call error
1109	Subaccounts have no permission to open positions. Please contact customer service.
1110	Subaccounts have no permission to close positions. Please contact customer service.
1111	Subaccounts have no permission to transfer in. Please contact customer service.
1112	Subaccounts have no permission to transfer out. Please contact customer service.
1113	Subaccounts have no permission to trade. Please log in to your main account to authorize permissions.
1114	Subaccounts have no permission to transfer. Please log in to your main account to authorize permissions.
1115	You have no permission to access this subaccount.
1200	Failed to log in. Please try again.
1205	You have no access permissions.
1206	To protect you from high risk exposure, high leverage is not supported. For any questions, please contact customer service.
1220	You have no access since you have not activated futures trading yet.
1221	Unable to activate futures trading due to insufficient balance in your spot account.
1222	Unable to activate futures trading as the required duration hasn't been met since your account was activated.
1223	The VIP level can't meet the requirements for opening contracts.
1224	Your country/region can't meet the requirements for opening contracts.
1225	Failed to open contracts.
1226	Repeated account.
1227	HTX Futures are not supported in subaccounts. Please log in to your main account.
1228	You have not activated futures trading yet. Please activate it first.
1229	You've already consented to the Agreement.
1230	You haven't finished the risk verification.
1231	You haven't finished the ID Verification.
1232	The format/size of the image you uploaded does not meet the requirements. Please re-upload.
1233	High leverage is not enabled (Please agree to the High-Leverage Agreement with your main account on our website or app.)
1234	The unfilled orders of opening positions for {0} contracts cannot exceed {1}.
1235	The unfilled orders of closing position for {0} contracts cannot exceed {1}.
1250	Cannot access HT.n
1251	Unable to get BTC assets. Please try again later.
1252	Unable to query spot account balance. Please try again later.
1253	Signature verification error
1254	Futures trading cannot be activated for subaccounts. Please log in to your main account on our website to activate.
1300	Transfer failed.
1301	Insufficient transferable amount
1302	Failed to transfer due to system error.
1303	Each outward transfer cannot be less than {0}{1}.
1304	Each outward transfer cannot exceed {0}{1}.
1305	Each inward transfer cannot be less than {0}{1}.
1306	Each inward transfer cannot exceed {0}{1}.
1307	Your daily cumulative outward transfer amount has exceeded {0}{1}. Unable to make the transfer.
1308	Your daily cumulative inward transfer amount has exceeded {0}{1}. Unable to make the transfer.
1309	Your daily cumulative net outward transfer amount has exceeded {0}{1}. Unable to make the transfer.
1310	Your daily cumulative net inward transfer amount has exceeded {0}{1}. Unable to make the transfer.
1311	The daily upper limit for outward transfer has been reached. Unable to make the transfer.
1312	The daily upper limit for inward transfer has been reached. Unable to make the transfer.
1313	The daily upper limit for net outward transfer has been reached. Unable to make the transfer.
1314	The daily upper limit for net inward transfer has been reached. Unable to make the transfer.
1315	Wrong transfer type.
1316	Failed to freeze the transfer.
1317	Failed to unfreeze the transfer.
1318	Failed to confirm the transfer.
1319	Failed to query the transferable amount.
1320	Cannot make transfers as the futures contracts are not in trading hours.
1321	Transfer failed. Please try again later or contact customer service.
1322	Invalid amount. Must be more than 0.
1323	Transfer failed due to service error. Please try again later.
1325	Failed to set trading unit
1326	Failed to access trading units.
1327	Transfer failed for lack of transfer permission. Please contact customer service.
1328	Transfer failed for lack of transfer permission. Please contact customer service.
1329	Transfer failed for lack of transfer permission. Please contact customer service.
1330	Transfer failed for lack of transfer permission. Please contact customer service.
1331	The number of decimals has exceeded the precision limit. Please modify and resubmit.
1332	The perpetual contract does not exist.
1333	Failed to agree to the Maker & Taker Agreement.
1334	Failed to query the Maker & Taker Agreement
1335	Failed to set double confirmation for querying Maker & Taker orders.
1336	Failed to set double confirmation for upgrading Maker & Taker orders.
1337	ailed to set the settings for querying Maker & Taker orders.
1338	Failed to set the settings for upgrading Maker & Taker orders.
1339	Nickname contains illegal words. Please modify.
1340	This nickname has been taken. Please modify.
1341	The enrollment has ended
1342	Nicknames cannot be set for subaccounts.
1343	Invalid indicator. Please reset.
1344	Sorry. You can set real-time market reminders for a maximum of {0} contract products.
1345	Sorry. A maximum of {1} reminders can be set for the {0} contract.
1346	The indicator already exists. You don't need to repeat the setting.
1347	{0} parameter is incorrect. Please modify.
1348	This contract does not support cross margin mode.
1349	The leverage for new orders does not match current positions. Please change the leverage.
1401	This project is not available in your country or region.
1403	The number of take-profit / stop-loss orders for {0} perpetual contract shall not exceed {1}.
1404	Take-profit and stop-loss can only be set for orders that are placed to open positions.
1405	The take-profit price shall not be {0}{1}{2}
1406	Your chances have been used up
1407	The stop-loss price shall not be {0}{1}{2}
1408	Unable to cancel because the take-profit / stop-loss order has not taken effect yet.
1409	You have no permission to place take-profit / stop-loss orders. Please contact customer service.
1410	The number of sub-accounts for batch operation cannot exceed {0}
1411	Settling. Unable to query order information.
1412	{0} does not meet with the decimal precision limit {1}.
1413	You have no permission to place a Trailing Stop order. Please contact customer service.
1414	You have not activated grid trading yet. Please log in to your main account on our website or app, and agree to the grid trading agreement.
1415	The lowest termination price must be lower than the lowest grid price and the latest price; while the highest termination price must be higher than the highest grid price and the latest price. Please modify and resubmit.
1416	Exceeding the maximum running time, which is {0} days and {1} hours. Please modify and resubmit.
1417	Exceeding the range of grid quantity, which is ({0} ~ {1}). Please modify and resubmit.
1418	At most {0} grid orders can run at the same time. Please cancel other grid orders first.
1419	At most {0} grid orders can run at the same time. Please cancel other grid orders first.
1420	You have no permission for Futures grid trading. Please contact customer service.
1421	You have open orders or positions for this futures contract. Please cancel orders or close positions first.
1422	The estimated PnL per grid is less than 0. Please modify and resubmit.
1423	The lower-upper price range of the grid is invalid. Please modify and resubmit.
1424	This grid trading has been terminated for other reasons. Unable to modify or terminate manually.
1425	The callback rate should be {0} {1}. Please modify and resubmit.
1426	The activation price should be {0} the latest price.
1427	The number of your {0} trailing-stop perpetual futures orders cannot exceed the limit {1}.
1428	You can only collect one coupon for the same contract type.
1429	Coupon already claimed. You don't have to repeat the action.
1430	Coupon expired. Please refresh.
1431	The system is in maintenance and is expected to resume at {0} (GMT+8).
1432	A grid trading is being initialized or terminated. Unable to place an order now.
1433	The grid trading is terminated due to the manual placing/canceling of orders. Please check \u201COrder History\u201D for details.
1434	The amount is less than the minimum initial margin ({0}{1}), which would cause the amount per grid to be less than the minimum allowable amount. Please modify and resubmit.
1435	The grid has been terminated by you.
1436	Timeout and the grid has terminated automatically.
1437	The grid has been terminated due to a system error. Please contact customer service.
1438	The grid has been terminated after the termination condition was triggered.
1439	The grid has been terminated as liquidation was triggered.
1440	Failed to cancel the {0} contract.
1441	The trigger price must be lower than the highest termination price and higher than the lowest termination price. Please modify and resubmit.
1442	The effective duration must be longer than the running time by one minute or more. Please modify!
1443	The grid has been terminated due to the delivery of the {0} contract.
1450	Current leverage is not supported at your risk level.
1451	Current leverage is not supported at your risk level. Please check the details on your main account.
1452	Grid orders have exceeded the maximum limit. Unable to place orders now.
1453	The number of all your trigger orders has exceeded the maximum limit. Unable to place more orders now.
1454	The number of all your take-profit / stop-loss orders has exceeded the maximum limit. Unable to place more orders now.
1455	The number of all your trailing stop orders has exceeded the maximum limit. Unable to place more orders now.
1502	Market orders are not allowed to place orders for one-way positions.
1503	The trader only supports the two-way position mode.
1504	After closing the trader status, the leverage can be modified.
1505	After becoming a trader, only the following trading pairs are allowed to trade:{0}
1506	After closing the copy trading, the leverage can be modified.
1507	The copy trading only supports two-way Position Mode
1508	You are using Copy Trading right now. You will have to exit Copy Trading (and unfollow your Copied Trader) before you can start trading futures.
1511	The stop-loss price is near the liquidation price and may not trigger the stop-loss order. Please adjust the price and try again.
1600	The trader only supports the cross-position mode.
12001	Invalid submission time.
12002	Incorrect signature version.
12003	Incorrect signature method.
12004	Incorrect signature method.
12005	IP address error
12006	The submission time cannot be left blank.
12007	Incorrect public key
12008	Verification failed.
12009	User has been locked or does not exist.
1350	This project is not available in your country or region.
1457	You are not eligible to participate. Please refer to the event rules.
1458	Query attempts have exceeded the limit of {0}.
1460	The contract is currently not available. Please do not transfer in.
1461	The total positions (this order + open orders + positions) have exceeded the long-position limit ({0}{1}). Please modify and resubmit.
1462	The total positions (this order + open orders + positions) have exceeded the short-position limit ({0}{1}). Please modify and resubmit.
1463	With {0}X leverage, the position limit is {1} USDT for a long position and {2} USDT for a short position. Cannot change to this leverage as your current position would exceed the position limit.
1464	The number of unfilled orders for opening positions of {0} delivery futures (including all expirations) shall not exceed {1}.
1465	The number of unfilled orders for closing positions of {0} futures (including all expirations) shall not exceed {1}.
1466	The trading volume of subaccounts will be booked into your main account. Please log in to your main account to check.
1467	{0}
1468	The number of take-profit and stop-loss orders for all {0} Futures(including all types) shall not exceed {1}
1469	The number of your trigger orders for {0} Futures(including all types) shall not exceed {1}.
1470	The number of your {0} Futures(including all types) trailing stop orders exceeds the limit {1}.
1471	The trail fund voucher has been redeemed or has expired.
1472	The trail fund voucher is no longer available. Please consult customer service for details.
1481	Failed to open some subaccounts.
1482	Subaccount does not exist.
1480	We are sorry that the risk control rule was triggered due to your operations, please contact our Customer Service! Thank you for your support!
1483	Insufficient; Unable to Claim
1484	Reverse order involves Reduce Only order.
1485	One-way mode is unavailable for grid trading.
1486	One-way mode is unavailable temporarily.
1487	We are sorry you have no access to one-way mode.
1488	Opening positions is unavailable in one-way mode temporarily.
1489	Closing positions is unavailable in one-way mode temporarily.
1490	Opening after closing exceeds the limit (conts).
1491	Reduce Only order parameter error!
1492	Amount of Reduce Only order exceeds the amount available to close.
1493	Position mode cannot be adjusted for open orders.
1494	Position mode cannot be adjusted for existing positions.
1495	Position mode cannot be adjusted for open grid orders.
1496	Position mode cannot be adjusted due to the contract\u2019s non-trading status.
1497	Position mode parameter passing error!
1498	Margin account incorrect!
1499	Hedge mode currently; Unavailable to place orders in one-way mode.
1500	One-way mode currently; Unavailable to place orders in hedge mode.
1510	Since you are the merged cross and isolated margin account for USDT-M futures , you cannot use the APIs. If you need to use, please change the account type via '/linear-swap-api/v3/swap_switch_account_type' 1900={0};{1}
1511	The stop-loss price is near the liquidation price and may not trigger the stop-loss order. Please adjust the price and try again.
1700	TWAP service has been temporarily suspended
1701	Total Size should be no smaller than Chunk Size
1702	The maximum allowable number of TWAP orders has been reached
1703	The maximum allowable number of TWAP orders has been reached
1704	Distance (ratio) to market price: {0}-{1}
1705	Time Interval: {0} - {1} seconds
2001	Order failed. The trial bonus cannot be used for futures trades under the isolated margin mode
2011	There is an isolated position, please close it
2012	There is an isolated pending order, please cancel the order
2013	The account has isolated position and pending orders, please remove
2014	There are assets in the isolated account, please transfer to the full account
1900	{0};{1}
2100	One-way Mode does not support TP/SL market orders at the moment
4000	The merged cross and isolated margin account for USDT-M futures has only one USDT account.
4001	The merged cross and isolated margin account for USDT-M futures has only one USDT account. No need to transfer between users.
4002	The merged cross and isolated margin account for USDT-M futures is unavailable.Please complete the query with {0}
4003	The merged cross and isolated margin account for USDT-M futures is unavailable.Please complete the query with {0}
4004	The merged cross and isolated margin account for USDT-M futures is unavailable.Please complete the query with {0}
4005	The merged cross and isolated margin account for USDT-M futures is unavailable.Please complete the query with {0}
4006	No margin can be increased or decreased without a position
4007	Unified account special interface, non - one account is not available
4009	Function suspended
4010	HT deduction not yet enabled
4011	Close positions based on the maximum amount that can be closed without passing in the volume field.
50001	In view of the laws and regulations of your country/region, you understand that you bear the responsibility for any further proceeding or operation.
50002	Dear users, services are not available according to the rules and regulations in your country or region.
50003	Please assess and understand all the risks carefully and allocate your funds prudently when trading Futures products.
50004	In view of the laws and regulations of your country/region, you understand that you bear the responsibility for any further proceeding or operation.
50101	Please assess and understand all the risks carefully and allocate your funds prudently when trading Futures products.
50102	Dear user, please complete KYC identity verification before trading.
50103	Sorry, assets transfers between this sub-account and its main account are not available.
6021	Request timed out，please try again later.