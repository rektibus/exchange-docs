Arkham Exchange API
Change Log#
2024-11-04 - Added rate limits
Introduction#
The Arkham Exchange provides a RESTful HTTP API and a Websocket API that enables access to the Arkham Exchange trading platform. It allows you to interact with the exchange programmatically, including trading, order management and market data.

The Rest API endpoint is available at the following base URL:

https://arkm.com/api
Authentication#
API Keys
The Arkham Exchange API uses API keys for authentication. You can create an API key and API Secret in the API Settings section of the Arkham Exchange website.

To authenticate with the API, include the API key in the +""+Arkham-API-Key+""+ header of your HTTP requests.

Signing Requests
To better protect your account, endpoints will require the request to be signed with your API Secret. The signature is a HMAC-SHA256 signed with your API Secret of the following data:

Your API key
The Expiry timestamp
The HTTP method of the request
The path of the request
The body of the request
The expiry timestamp is the time at which the request will expire formatted as a Unix timestamp in microseconds i.e. The number of non-leap seconds which have passed since 00:00:00 UTC on Thursday, 1 January 1970 multiplied by 1000000 as an integer.

The request will be rejected if the request is received by the server after the expiry timestamp or if the timestamp represents a time more than 15 minutes in the future.

The expiry timestamp is passed in the +""+Arkham-Expires+""+ header of the request.

The signature is passed in the +""+Arkham-Signature+""+ header of the request as a base64 encoded string.

Bash Example:

Set the BASE_URL, API_KEY, API_SECRET, METHOD, REQUEST_PATH and BODY variables to the required values:

API_KEY=<your-api-key>
API_SECRET=<your-api-secret>
BASE_URL=https://arkm.com/api
METHOD="POST"
REQUEST_PATH="/orders/cancel/all"
BODY="{}"
Note: For GET requests, the BODY should be an empty string.

Set the expiry timestamp - in this case 5 minutes from now:

EXPIRES=$(($(/bin/date +%s) + 300))000000
Calculate the signature

HMAC_KEY=$(/bin/echo -n "$API_SECRET" | base64 -D | xxd -p -c 64)
SIGNATURE=$(/bin/echo -n "$API_KEY$EXPIRES$METHOD$REQUEST_PATH$BODY" | openssl dgst -sha256 -mac HMAC -macopt hexkey:$HMAC_KEY -binary | base64)
Make the signed request

curl -X $METHOD \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Arkham-Api-Key: $API_KEY" \
	-H "Arkham-Expires: $EXPIRES" \
	-H "Arkham-Signature: $SIGNATURE" \
	-d "$BODY" \
	$BASE_URL$REQUEST_PATH
Rate Limits#
Arkham Exchange API rate limits are based on two factors as outlined below:

30 Day Trading Volume
ARKM Balance
Requirement (30D Spot Volume / 30D Perps Volume / ARKM Balance)	REST Spot Order Limit / Sec (Per User)	REST Perps Order Limit / Sec (Per User)	REST Perps Order Limit / Sec (Per IP)	REST Message Request Limit / Sec (Per User)	REST Message Request Limit / Sec (Per IP)	WebSocket Message Request Limit / Sec (Per User)
< 500,000 USDT Spot and < 5,000,000 USDT Perps and < 5000 ARKM	20	40	150	40	5	10
≥ 500,000 USDT Spot or ≥ 5,000,000 USDT Perps or ≥ 5000 ARKM	30	400	150	400	5	10
≥ 1,000,000 USDT Spot or ≥ 10,000,000 USDT Perps or ≥ 20,000 ARKM	40	550	150	550	5	10
≥ 2,500,000 USDT Spot or ≥ 25,000,000 USDT Perps or ≥ 50,000 ARKM	60	750	150	750	5	10
≥ 5,000,000 USDT Spot or ≥ 50,000,000 USDT Perps or ≥ 100,000 ARKM	80	1,500	150	1,500	5	10
≥ 10,000,000 USDT Spot or ≥ 100,000,000 USDT Perps or ≥ 200,000 ARKM	150	2,500	150	2,500	5	10
≥ 25,000,000 USDT Spot or ≥ 250,000,000 USDT Perps or ≥ 300,000 ARKM	200	3,500	150	3,500	5	10
≥ 50,000,000 USDT Spot or ≥ 500,000,000 USDT Perps or ≥ 500,000 ARKM	300	5,000	150	5,000	5	10
Note:

Timing: 30 day snapshots of trading volume and ARKM holdings are taken at 5:00 PM UTC every Saturday and updated API rate limits are calculated between 8:00 PM and 10:00 PM UTC. The updated limits apply to the following week starting at 12:00 AM UTC Sunday. A user's ARKM balance is defined by their lowest ARKM balance over the last 30 days. For the first 30 days of trading, Trading Volume and ARKM Holdings discounts will be based on all previous trading days (i.e., 15 trading days on day 16 of trading being live).

Perpetuals and Margin#
Leverage and Margin Schedule in USDT Perpetuals
On Arkham Exchange, users cannot directly specify the maximum leverage they wish to use. Instead, the leverage is dynamic and determined by Margin Schedule, which adjusts margin requirements based on position size. As the position size increases, the required margin also increases, reducing the effective leverage.

The margin schedule applies progressively higher initial margin rates for larger positions to ensure that risk is managed as position sizes grow.

How Margin Schedule Works
Margin Schedule defines position bands with corresponding initial margin rates and maintenance margin rates. The maintenance margin rate is set at half of the initial margin rate, and the effective leverage is determined based on the initial margin rate.

Here is the margin schedule for USDT perpetuals:

Margin Schedule A - Initial & Maintenance Margin Rates
Position Size (USDT)	Initial Margin (%)	Maintenance Margin (%)	Effective Leverage
0 - 1,000,000	2.00%	1.00%	50x
1,000,001 - 2,000,000	4.00%	2.00%	25x
2,000,001 - 5,000,000	5.00%	2.50%	20x
5,000,001 - 10,000,000	10.00%	5.00%	10x
10,000,001 - 20,000,000	20.00%	10.00%	5x
20,000,001 - 60,000,000	30.00%	15.00%	3.33x
60,000,001+	50.00%	25.00%	2x
The initial margin rate is the percentage of your position size that must be held as collateral to open a position.
The maintenance margin rate is half the initial margin, representing the collateral required to maintain the position and avoid liquidation.
Example of Dynamic Leverage Based on Margin Schedule A
Let’s walk through an example using Margin Schedule A:

Position 1: 800,000 USDT long on BTC/USDT.

Initial Margin Rate: 2% (since the position size is below 1,000,000 USDT).
Initial Margin: 2% of 800,000 USDT = 16,000 USDT.
Maintenance Margin: 1% of 800,000 USDT = 8,000 USDT.
Effective Leverage: 50x.
Position 2: 3,000,000 USDT short on ETH/USDT.

Initial Margin Rate: 5% (for positions between 2,000,001 and 5,000,000 USDT).
Initial Margin: 5% of 3,000,000 USDT = 150,000 USDT.
Maintenance Margin: 2.5% of 3,000,000 USDT = 75,000 USDT.
Effective Leverage: 20x.
In this example, Position 1 uses higher leverage because it's in a smaller band with a lower margin requirement (2%). Position 2 has a larger size and thus requires more collateral (5%), leading to lower leverage.

How Margin Netting and Unrealized PnL Work Under This Model
When a subaccount holds multiple positions, margin netting combines the margin requirements of all open positions and offsets them using the net unrealized profit and loss (PnL) across positions.

Example of Multiple Positions with Margin Netting
Assume the trader holds two positions:

Position 1:

Long BTC/USDT.
Position size: 1,500,000 USDT.
Initial Margin Rate: 4%.
Initial Margin: 4% of 1,500,000 = 60,000 USDT.
Maintenance Margin: 2% of 1,500,000 = 30,000 USDT.
Unrealized PnL: +50,000 USDT (the position is in profit).
Position 2:

Short ETH/USDT.
Position size: 3,500,000 USDT.
Initial Margin Rate: 5%.
Initial Margin: 5% of 3,500,000 = 175,000 USDT.
Maintenance Margin: 2.5% of 3,500,000 = 87,500 USDT.
Unrealized PnL: -30,000 USDT (the position is in a loss).
Netting the Margin Requirements:

Total Initial Margin: 60,000 USDT (Position 1) + 175,000 USDT (Position 2) = 235,000 USDT.
Unrealized PnL offset: The net unrealized PnL is +20,000 USDT (50,000 USDT from Position 1 minus 30,000 USDT from Position 2).
Effective margin requirement: After netting the unrealized PnL, the effective margin requirement becomes:
235,000 USDT - 20,000 USDT = 215,000 USDT.
This means the trader only needs 215,000 USDT in margin to support both positions, as the profit from the BTC/USDT position offsets the losses from the ETH/USDT position, reducing the overall margin requirement and the risk of liquidation.

Impact of Margin Schedules on Risk Management
Larger positions require more margin: As your position size increases, the margin requirement also increases, reducing the effective leverage.

Smaller positions offer higher leverage: Traders with smaller positions can use higher leverage because the margin requirements are lower. However, higher leverage also increases the potential risk.

Unrealized PnL reduces risk: The unrealized profit from one position can offset the losses of another, reducing the overall margin requirement and helping to avoid liquidation.

Key Takeaways
Dynamic leverage is applied automatically based on the size of your position, with smaller positions allowing higher leverage and larger positions requiring more margin.
Margin netting allows unrealized PnL from one position to offset the margin requirement for another, reducing the risk of liquidation.
Monitoring positions is important because while unrealized profit can lower margin requirements, market volatility can quickly shift your net PnL, increasing the risk of liquidation.
Funding Rates#
Overview
Sampling Interval: Every second
Funding Interval: Every hour
Calculation: Funding rate is calculated based on the difference between the perpetual futures price and the index (spot) price, sampled every second
Min/Max Values: Funding rate is capped between -0.25% and 0.25%.
Transfer of Funding: Funding payments are transferred between traders once every hour
Funding Rate Calculation
The funding rate is derived from the price difference between the perpetual futures contract price and the index price. This difference is sampled every second over the course of an hour.

The formula for the funding rate at any given second is as follows:

Funding Rate Sample
t
=
perpPrice
t
−
indexPrice
t
indexPrice
t
Funding Rate Sample 
t
​
 = 
indexPrice 
t
​
 
perpPrice 
t
​
 −indexPrice 
t
​
 
​
 

Where:

perpPrice_t: The price of the perpetual futures contract at time t.
indexPrice_t: The index price (or spot price) of the underlying asset at time t.
The difference is divided by the index price to express it as a percentage.

Hourly Funding Rate
The hourly funding rate is computed as the average of the second-by-second funding rates over the entire hour.

Hourly Funding Rate
=
1
24
∗
n
∑
t
=
1
n
perpPrice
t
−
indexPrice
t
indexPrice
t
Hourly Funding Rate= 
24∗n
1
​
 ∑ 
t=1
n
​
  
indexPrice 
t
​
 
perpPrice 
t
​
 −indexPrice 
t
​
 
​
 

Where:

( n ) is the total number of seconds in an hour (3600 seconds).
This average captures the typical difference between the perpetual futures price and the index price over the funding interval.

Funding Payment
The funding payment is the actual amount exchanged between long and short position holders, based on the trader’s notional position size.

Funding Payment
=
Position Size
×
Mark Price
×
Hourly Funding Rate
Funding Payment=Position Size×Mark Price×Hourly Funding Rate

Long Position Holders: If the hourly funding rate is positive, long position holders will pay short position holders.
Short Position Holders: If the hourly funding rate is negative, short position holders will pay long position holders.
Example
Suppose that the perpetual futures price for Bitcoin over an hour is consistently higher than the index price.

Average perpetual futures price (perpPrice) = $30,500
Average index price (indexPrice) = $30,000
Using the formula for the hourly funding rate:

Hourly Funding Rate
=
30
,
500
−
30
,
000
30
,
000
∗
24
=
0.00069583
Hourly Funding Rate= 
30,000∗24
30,500−30,000
​
 =0.00069583

A trader with a long position of $100,000 notional value would then calculate their funding payment as follows:

Funding Payment
=
100
,
000
×
0.00069583
=
69.58
 
USD
Funding Payment=100,000×0.00069583=69.58USD

Since the funding rate is positive, the long position holder pays $69.58 to the short position holder.

Liquidations#
Below Maintenance Margin and Liquidation Process
When trading USDT perpetuals, it’s crucial to maintain sufficient margin to avoid liquidation. If your portfolio falls below required margin thresholds, the exchange has a structured liquidation process involving Liquidity Support Providers (LSPs), the insurance fund, and automatic deleveraging (ADL) to manage risk effectively.

What Happens When a Subaccount Falls Below Maintenance Margin?
If the margin in your subaccount drops below the maintenance margin (half of the initial margin), liquidation is triggered. The exchange will attempt to close your positions through the Liquidity Support Provider (LSP) program. If there isn’t sufficient liquidity, the exchange will draw on its insurance fund to cover any shortfall. As a last resort, automatic deleveraging (ADL) is used to close out positions against opposing traders.

The Liquidation Process
1. Liquidity Support Provider (LSP) Program
When a subaccount falls below the maintenance margin, the exchange first attempts to liquidate the position by passing it to participants in the Liquidity Support Provider (LSP) program. LSPs are professional market participants (such as liquidity providers, hedge funds, or proprietary traders) who agree to absorb liquidated positions in exchange for favorable pricing and liquidity incentives.

Role of LSPs: LSPs provide liquidity by taking over liquidated positions at a negotiated price, helping to minimize market impact.
LSP Participation: Positions are transferred to LSPs in chunks, and they take over the risk, thus preventing a forced sale at unfavorable market prices. This step helps ensure that large liquidations do not directly impact the market price or cause significant slippage.
Liquidation at Mark Price + 1% Spread: When a liquidation occurs, LSP participants are allowed to purchase the liquidated position at the Mark Price plus a 1% spread. This ensures that liquidity providers are fairly compensated for taking on liquidated positions, which may carry higher risk in turbulent market conditions.
2. Exchange Insurance Fund
Arkham maintains an Insurance Fund to safeguard traders and the overall ecosystem from extreme market events, particularly during liquidations. Here's how the Insurance Fund ensures the protection of both traders and LSP participants:

Covering Losses: In the event that a liquidation results in a negative balance or insufficient funds to cover the full position, the Insurance Fund is used to make up the difference, ensuring that LSP participants receive the liquidated positions at Mark Price + 1%, even if the liquidated trader's account balance is inadequate.

Fair Pricing for LSP: The 1% spread above the Mark Price acts as a buffer, offering an incentive to LSP participants and reducing their risk. The Insurance Fund guarantees that the exchange is able to honor this spread, maintaining fairness in the liquidation process.

By ensuring that LSP participants are compensated with a mark price plus 1% spread and using the Insurance Fund to cover potential shortfalls, Arkham promotes a healthy liquidity environment while protecting traders from excessive loss exposure.

3. Automatic Deleveraging (ADL)
If LSP program participants can't fully cover the liquidated position, the exchange resorts to automatic deleveraging (ADL). In ADL, the system automatically closes out positions by matching them with opposing open positions held by other traders on the platform.

How ADL Works: The exchange looks for opposing positions (e.g., a long position matched against a short position) held by other participants. The positions are closed out against each other to bring the account back into compliance with the margin requirements.
Impact on Other Traders: Traders with high leverage and profits are prioritized for ADL matching, meaning their positions might be automatically reduced or closed to balance the risk on the exchange.
Example
Trader’s Initial Position:

Trader A holds a long position of 10 BTCP in a perpetual contract with an entry price of $30,000.
Maintenance Margin Requirement: 5% of the total position value, that requires a collateral of $15,000.
Market Movement:

The price of BTC perpetual drops to $28,000.
Trader A’s equity is now:
Equity
=
Current Position Value
−
Amount Invested
+
Collateral
Current Position Value
=
10
 
BTC
×
28
,
000
=
280
,
000
Amount Invested
=
30
,
000
×
10
=
300
,
000
Equity
=
280
,
000
−
300
,
000
+
15
,
000
=
−
5
,
000
Equity=Current Position Value−Amount Invested+Collateral
Current Position Value=10BTC×28,000=280,000
Amount Invested=30,000×10=300,000
Equity=280,000−300,000+15,000=−5,000
Maintenance margin required:
5
%
 of 
270
,
000
=
13
,
500
5% of 270,000=13,500
Since Trader A’s equity is below the required maintenance margin, their subaccount is passed on to liquidation engine.
Liquidation Process
Step 1: Attempt to Liquidate via LSPs
Liquidation Trigger:

Since Trader A’s equity is below the required maintenance margin, their subaccount gets liquidated.
The exchange attempts to pass Trader A’s position to LSP participants. The BTC price is $28,000, and they take it on at Mark Price - 1% Spread:
LSP Purchase Price
=
28
,
000
−
(
28
,
000
×
0.01
)
=
27
,
720
LSP Purchase Price=28,000−(28,000×0.01)=27,720
LSP Involvement:

The exchange sells 5 BTC to LSPs at $27,720 per BTC:
Value of Liquidated Position to LSP
=
5
 
BTC
×
27
,
720
=
138
,
600
Value of Liquidated Position to LSP=5BTC×27,720=138,600
Insurance Fund Usage:

Shortfall
=
138
,
600
+
5
BTC
×
28
,
000
+
15
,
000
−
300
,
000
=
−
6
,
400
Shortfall=138,600+5BTC×28,000+15,000−300,000=−6,400
The Insurance Fund covers this shortfall so that LSPs receive the liquidated positions at the agreed price, ensuring no losses occur for them despite Trader A's account deficiency.
Step 2: Remaining Position and ADL
Remaining Position:

Trader A now has 5 BTC remaining which will be deleveraged
Automatic Deleveraging (ADL):

Suppose another trader, Trader B, has a short position of 10 BTC at $28,000.
The exchange identifies Trader B’s short position to match it against Trader A’s liquidated position.
Since Trader B has a profitable short position, the exchange will deleverage 5 BTC of their short position at mark price of $28,000 realising a PnL of 5 * $2000 = $10,000.
Closing Positions:

Trader B’s position is closed out for 5 BTC, while Trader A’s long position is effectively liquidated.
The remaining short position for Trader B becomes 5 BTC.
Summary of Outcomes
Trader A:

Had their 10 BTC long position liquidated.
Resulting shortfall of $6,400 was covered by the Insurance Fund.
Liquidity Support Providers:

Acquired 5 BTC at $27,720, absorbing some risk but benefiting from the premium.
Trader B:

Partially closed their 5 BTC short position, gaining $10,000 profit from the market movement and helping to balance risk across the exchange.
Key Takeaways
LSPs facilitate smoother liquidations by absorbing positions and maintaining market stability, which helps prevent a rapid decline in price due to forced sales.
The Insurance Fund acts as a safety net, ensuring LSPs and the exchange can operate without incurring losses due to trader defaults.
Automatic Deleveraging (ADL) provides a mechanism to manage risk and maintain balance by matching positions across different traders.
This example illustrates how a perpetual contract liquidation works in a practical scenario, showing how different mechanisms come together to manage risk and maintain a stable trading environment.

Impact on Traders from Liquidation and ADL
LSP Program and Insurance Fund: These mechanisms are designed to minimize the impact of liquidation on the market and ensure traders’ positions are closed without significant losses beyond the maintenance margin.

Automatic Deleveraging (ADL): Traders with high leverage and high profits may see their positions automatically reduced or closed as part of the ADL process. This ensures that the exchange maintains risk management, but it can affect traders’ open positions unexpectedly.

Monitoring Margin Levels: To avoid liquidation, traders should closely monitor their positions and maintain sufficient collateral. If your position falls below the initial or maintenance margin, the liquidation process will start, and you may lose your position partially or entirely.

The liquidation process ensures that the exchange maintains stability and protects traders and the market from sudden, large-scale liquidations.

#Margin Schedules
Margin schedules are used to determine the margin requirements for a given position size. Each trading pair has one of the below margin schedules associated with it.

Each margin schedule defines a series of bands, where each band has a position size range, a maximum leverage, an initial margin rate and a rebate. The initial margin requirement is calculated as the position size multiplied by the initial margin rate minus the rebate. The rebate is provided so that there is no discontinuity in the margin requirement when moving between bands.

#Margin Schedule A
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 1,000,000
50x
2%
0
1,000,000 - 2,000,000
25x
4%
20,000
2,000,000 - 5,000,000
20x
5%
40,000
5,000,000 - 10,000,000
10x
10%
290,000
10,000,000 - 20,000,000
5x
20%
1,290,000
20,000,000 - 60,000,000
3.33x
30%
3,290,000
60,000,000 - 200,000,000
2x
50%
15,290,000
#Margin Schedule B
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 250,000
50x
2%
0
250,000 - 750,000
25x
4%
5,000
750,000 - 1,000,000
20x
5%
12,500
1,000,000 - 5,000,000
10x
10%
62,500
5,000,000 - 10,000,000
5x
20%
562,500
10,000,000 - 30,000,000
3.33x
30%
1,562,500
30,000,000 - 100,000,000
2x
50%
7,562,500
#Margin Schedule C
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 250,000
25x
4%
0
250,000 - 500,000
20x
5%
2,500
500,000 - 1,000,000
10x
10%
27,500
1,000,000 - 2,500,000
5x
20%
127,500
2,500,000 - 50,000,000
3.33x
30%
377,500
50,000,000 - 100,000,000
2x
50%
10,377,500
#Margin Schedule D
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 10,000
20x
5%
0
10,000 - 250,000
10x
10%
500
250,000 - 500,000
5x
20%
25,500
500,000 - 2,000,000
3.33x
30%
75,500
2,000,000 - 5,000,000
2x
50%
475,500
#Margin Schedule E
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 10,000
10x
10%
0
10,000 - 100,000
5x
20%
1,000
100,000 - 1,000,000
3.33x
30%
11,000
1,000,000 - 5,000,000
2x
50%
211,000
#Margin Schedule F
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 10,000
5x
20%
0
10,000 - 100,000
3.33x
30%
1,000
100,000 - 500,000
2x
50%
21,000
#Margin Schedule G
Position Size (USDT)
Maximum Leverage
Initial Margin Rate
Rebate (USDT)
0 - 10,000
3.33x
30%
0
10,000 - 50,000
2x
50%
2,000
#Error Responses
There is a fixed set of errors returned by the API and Websocket when a failure occurs, each has a unique name which maps to a specific HTTP status code and (deprecated) websocket error code.

#1XXXX General Errors
These errors can occur for a variety of reasons and may be returned by the API or Websocket on any endpoint.

ID	Name	Status Code	WS Code
10000	InternalError	500	0
10001	BadRequest	400	1
10002	Unauthorized	401	2
10003	InvalidSymbol	400	3
10004	SymbolRequired	400	4
10005	RateLimitExceeded	429	11
10006	Forbidden	403	13
10007	InvalidIP	400	1
10008	Throttled	503	1
10009	KeyNotPermitted	401	1
10010	ParsingKey	401	1
10011	VerifyingKey	401	1
10012	RequiresRead	403	1
10013	RequiresWrite	403	1
10014	SignatureMissing	400	1
10015	ExpiresMissing	400	1
10016	ParsingExpires	400	1
10017	ExpiresTooFar	403	1
10018	ExpiredSignature	403	1
10019	SignatureMismatch	401	1
10020	IPNotAllowed	403	1
10021	MFA	401	1
10022	ParsingRequest	400	1
10023	SubaccountNotFound	404	1
10024	Conflict	409	1
10025	NotFound	404	1
10026	ApiKeyNotAllowed	400	1
10027	MethodNotAllowed	405	1
#2XXXX General Websocket Errors
These errors only occur in the context of Websocket connections.

ID	Name	Status Code	WS Code
20001	InvalidMethod	400	5
20002	MethodRequired	400	6
20003	InvalidChannel	400	7
20004	ChannelRequired	400	8
20005	InvalidGroup	400	10
#3XXXX Trading Errors
These errors occur in the context of trading operations such as creating or cancelling orders.

ID	Name	Status Code	WS Code
30001	InvalidSize	400	1
30002	InvalidPrice	400	1
30003	InvalidPostOnly	400	1
30004	InvalidReduceOnly	400	1
30005	InvalidNotional	400	1
30006	UnknownOrderType	400	1
30007	PairNotEnabled	400	1
30008	TradingFreeze	400	1
30009	PostOnly	400	1
30010	InsufficientBalance	400	1
30011	InvalidPair	400	1
30012	NoMarkPrice	400	1
30013	InsufficientLiquidity	400	1
30014	ClientOrderIdAlreadyExists	400	1
30015	ClientOrderIdNotFound	400	1
30016	ReduceOnlyInvalid	400	1
30017	UnsupportedOrderSide	400	1
30018	UnsupportedAssetType	400	1
30019	PositionLimit	400	1
30020	InvalidClientOrderID	400	1
30021	InvalidTriggerType	400	1
30022	InvalidTriggerPriceType	400	1
30023	InvalidOrderSide	400	1
30024	InvalidOrderType	400	1
30025	InvalidBrokerId	400	1
30026	UserFrozen	400	1
30027	UserDeleted	404	1
30028	OrderIdNotFound	400	1
#4XXXX Funding Errors
These errors occur in the context of funding operations such as deposits, withdrawals, and transfers.

ID	Name	Status Code	WS Code
40001	FailedRiskCheck	400	1
40002	MemoNotSupported	400	1
40003	InvalidWithdrawalAddress	400	1
40004	PositionNotFound	404	1
40005	InvalidChain	400	1
40006	FuturesNotEnabled	400	1
40007	SubaccountHasOpenFuturePositions	400	1
40008	LspAssignmentGreaterThanMaxNotional	400	1
40009	LspMaxNotionalGreaterThanMarginLimit	400	1
40010	LspMaxNotionalMustNotBeNegative	400	1
40011	PortfolioLiquidation	400	1
40012	NegativeAmount	400	1
40013	ZeroAmount	400	1
40014	NeedStateAcknowledgement	400	1
#9XXXX Other Errors
These errors occur in the context of other API requests.

ID	Name	Status Code	WS Code
90001	InvalidAlertType	400	1
90002	InvalidAlertPriceType	400	1
90003	InvalidVoucherStatus	400	1
90004	InvalidCandleDuration	400	1
90005	InvalidNotificationType	400	1
90006	TooManyMFAAttempts	429	1
90007	InvalidMFA	401	1
90008	TooManyAttempts	429	1
90009	InvalidRole	400	1
90010	InvalidEmail	400	1
90011	ChangeEmailRequestRateLimited	429	1
#Api Errors
Response Body
// Example Response Body
{
  "id": 10000,
  "message": "internal error",
  "name": "InternalError"
}
Name	Type	Required	Description
object	Yes	
.id	integer	Yes	The unique identifier for the error Enum: 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 20001, 20002, 20003, 20004, 20005, 30001, 30002, 30003, 30004, 30005, 30006, 30007, 30008, 30009, 30010, 30011, 30012, 30013, 30014, 30015, 30016, 30017, 30018, 30019, 30020, 30021, 30022, 30023, 30024, 30025, 30026, 30027, 30028, 40001, 40002, 40003, 40004, 40005, 40006, 40007, 40008, 40009, 40010, 40011, 40012, 40013, 40014, 90001, 90002, 90003, 90004, 90005, 90006, 90007, 90008, 90009, 90010, 90011
.message	string	Yes	Additional details about the error
.name	string	Yes	The name of the error Enum: "InternalError", "BadRequest", "Unauthorized", "InvalidSymbol", "SymbolRequired", "RateLimitExceeded", "Forbidden", "InvalidIP", "Throttled", "KeyNotPermitted", "ParsingKey", "VerifyingKey", "RequiresRead", "RequiresWrite", "SignatureMissing", "ExpiresMissing", "ParsingExpires", "ExpiresTooFar", "ExpiredSignature", "SignatureMismatch", "IPNotAllowed", "MFA", "ParsingRequest", "SubaccountNotFound", "Conflict", "NotFound", "ApiKeyNotAllowed", "MethodNotAllowed", "InvalidMethod", "MethodRequired", "InvalidChannel", "ChannelRequired", "InvalidGroup", "InvalidSize", "InvalidPrice", "InvalidPostOnly", "InvalidReduceOnly", "InvalidNotional", "UnknownOrderType", "PairNotEnabled", "TradingFreeze", "PostOnly", "InsufficientBalance", "InvalidPair", "NoMarkPrice", "InsufficientLiquidity", "ClientOrderIdAlreadyExists", "ClientOrderIdNotFound", "ReduceOnlyInvalid", "UnsupportedOrderSide", "UnsupportedAssetType", "PositionLimit", "InvalidClientOrderID", "InvalidTriggerType", "InvalidTriggerPriceType", "InvalidOrderSide", "InvalidOrderType", "InvalidBrokerId", "UserFrozen", "UserDeleted", "OrderIdNotFound", "FailedRiskCheck", "MemoNotSupported", "InvalidWithdrawalAddress", "PositionNotFound", "InvalidChain", "FuturesNotEnabled", "SubaccountHasOpenFuturePositions", "LspAssignmentGreaterThanMaxNotional", "LspMaxNotionalGreaterThanMarginLimit", "LspMaxNotionalMustNotBeNegative", "PortfolioLiquidation", "NegativeAmount", "ZeroAmount", "NeedStateAcknowledgement", "InvalidAlertType", "InvalidAlertPriceType", "InvalidVoucherStatus", "InvalidCandleDuration", "InvalidNotificationType", "TooManyMFAAttempts", "InvalidMFA", "TooManyAttempts", "InvalidRole", "InvalidEmail", "ChangeEmailRequestRateLimited"
#API Routes
User#
#Get User
GET /user
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
{
  "airdropKycAt": 1704067200000000,
  "becameVipAt": 1704067200000000,
  "country": "abc123",
  "createdAt": 1704067200000000,
  "dmm": true,
  "email": "example@example.com",
  "featureFlags": [
    "feature1",
    "feature2"
  ],
  "freezeSettings": {
    "freezeAccountMgmt": true,
    "freezeDeposit": true,
    "freezeReduceOnlyTrading": true,
    "freezeTrading": true,
    "freezeWithdrawal": true,
    "offboardingMode": true
  },
  "id": 1,
  "kycVerifiedAt": 1704067200000000,
  "pmm": true,
  "requireMFA": true,
  "settings": {
    "allowSequenceEmails": true,
    "autogenDepositAddresses": true,
    "confirmBeforePlaceOrder": true,
    "hideBalances": true,
    "language": "en",
    "marginUsageThreshold": 1.23,
    "notifyAnnouncements": true,
    "notifyCommissions": true,
    "notifyDeposits": true,
    "notifyMarginUsage": true,
    "notifyOrderFills": true,
    "notifyPushNotifications": true,
    "notifyRebates": true,
    "notifySendEmail": true,
    "notifyWithdrawals": true,
    "tickerTapeScroll": true,
    "updatesFlash": true
  },
  "subaccounts": [
    {
      "createdAt": 1704067200000000,
      "futuresEnabled": true,
      "id": 1,
      "isLsp": true,
      "lspSettings": [
        {
          "maxAssignmentNotional": "200.1",
          "maxExposureNotional": "200.1",
          "symbol": "BTC_USDT"
        }
      ],
      "name": "abc123",
      "payFeesInArkm": true,
      "pinned": true
    }
  ],
  "username": "username"
}
Name	Type	Required	Description
object	Yes	
.airdropKycAt	integer	Yes	Time in microseconds since unix epoch
.becameVipAt	integer	Yes	Time in microseconds since unix epoch
.country	string	No	
.createdAt	integer	Yes	Time in microseconds since unix epoch
.dmm	boolean	Yes	
.email	string	Yes	Format: email
.featureFlags	array	Yes	List of feature flags enabled for the user
.featureFlags[*]	string	-	
.freezeSettings	object	Yes	
.freezeSettings.freezeAccountMgmt	boolean	Yes	
.freezeSettings.freezeDeposit	boolean	Yes	
.freezeSettings.freezeReduceOnlyTrading	boolean	Yes	
.freezeSettings.freezeTrading	boolean	Yes	
.freezeSettings.freezeWithdrawal	boolean	Yes	
.freezeSettings.offboardingMode	boolean	Yes	
.id	integer	Yes	
.kycVerifiedAt	integer	Yes	Time in microseconds since unix epoch
.pmm	boolean	Yes	
.requireMFA	boolean	Yes	
.settings	object	Yes	
.settings.allowSequenceEmails	boolean	Yes	
.settings.autogenDepositAddresses	boolean	Yes	
.settings.confirmBeforePlaceOrder	boolean	Yes	
.settings.hideBalances	boolean	Yes	
.settings.language	string	No	Enum: "en", "zh", "vi", "uk", "es", "ru", "ar", "ur", "hi"
.settings.marginUsageThreshold	number	Yes	
.settings.notifyAnnouncements	boolean	Yes	
.settings.notifyCommissions	boolean	Yes	
.settings.notifyDeposits	boolean	Yes	
.settings.notifyMarginUsage	boolean	Yes	
.settings.notifyOrderFills	boolean	Yes	
.settings.notifyPushNotifications	boolean	Yes	
.settings.notifyRebates	boolean	Yes	
.settings.notifySendEmail	boolean	Yes	
.settings.notifyWithdrawals	boolean	Yes	
.settings.tickerTapeScroll	boolean	Yes	
.settings.updatesFlash	boolean	Yes	
.subaccounts	array	Yes	
.subaccounts[*]	object	-	
.subaccounts[*].createdAt	integer	Yes	Time in microseconds since unix epoch
.subaccounts[*].futuresEnabled	boolean	Yes	if true futures trading is enabled for the subaccount
.subaccounts[*].id	integer	Yes	
.subaccounts[*].isLsp	boolean	Yes	if true the subaccount is a liquidity provider
.subaccounts[*].lspSettings	array	Yes	
.subaccounts[*].lspSettings[*]	object	-	
.subaccounts[*].lspSettings[*].maxAssignmentNotional	string	Yes	
.subaccounts[*].lspSettings[*].maxExposureNotional	string	Yes	
.subaccounts[*].lspSettings[*].symbol	string	Yes	
.subaccounts[*].name	string	Yes	
.subaccounts[*].payFeesInArkm	boolean	Yes	if true and ARKM balance is sufficient fees are paid in ARKM with a discount. This is only available for USDT pairs
.subaccounts[*].pinned	boolean	Yes	
.username	string	Yes	
Public#
#Get Alerts
GET /public/alerts
Response Body
// Example Response Body
[
  {
    "id": 1,
    "lastUpdated": 1704067200000000,
    "message": "abc123",
    "type": "abc123"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].id	integer	Yes	
[*].lastUpdated	integer	Yes	Time in microseconds since unix epoch
[*].message	string	Yes	
[*].type	string	Yes	
#Get Announcements
GET /public/announcements
Get announcements for a specific locale

Parameters
Name	In	Type	Required	Description
locale	query	string	Yes	Enum: "en", "zh", "vi", "uk", "es", "ru", "ar", "ur", "hi"
Response Body
// Example Response Body
[
  {
    "content": "abc123",
    "createdAt": 1704067200000000,
    "id": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].content	string	Yes	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch
[*].id	integer	Yes	
#Get Assets
GET /public/assets
Response Body
// Example Response Body
[
  {
    "chains": [
      {
        "assetSymbol": "BTC",
        "blockTime": 1,
        "confirmations": 1,
        "name": "abc123",
        "symbol": "abc123",
        "type": 1
      }
    ],
    "featuredPair": "BTC_USDT",
    "geckoId": "btc",
    "imageUrl": "https://example.com/image.png",
    "minDeposit": "10",
    "minWithdrawal": "10",
    "moonPayChain": "BTC",
    "moonPayCode": "btc",
    "name": "abc123",
    "stablecoin": true,
    "status": "staged",
    "symbol": "BTC",
    "withdrawalFee": "0.01"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].chains	array	Yes	
[*].chains[*]	object	-	
[*].chains[*].assetSymbol	string	Yes	
[*].chains[*].blockTime	integer	Yes	
[*].chains[*].confirmations	integer	Yes	
[*].chains[*].name	string	Yes	
[*].chains[*].symbol	string	Yes	
[*].chains[*].type	integer	Yes	
[*].featuredPair	string	Yes	
[*].geckoId	string	Yes	
[*].imageUrl	string	Yes	Format: url
[*].minDeposit	string	Yes	
[*].minWithdrawal	string	Yes	
[*].moonPayChain	string	No	
[*].moonPayCode	string	No	
[*].name	string	Yes	
[*].stablecoin	boolean	Yes	
[*].status	string	Yes	Enum: "staged", "listed", "delisted"
[*].symbol	string	Yes	
[*].withdrawalFee	string	Yes	
#Get Book
GET /public/book
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
limit	query	integer	No	
Response Body
// Example Response Body
{
  "asks": [
    {
      "price": "1.23",
      "size": "20.1"
    }
  ],
  "bids": [
    {
      "price": "1.23",
      "size": "20.1"
    }
  ],
  "group": "0.01",
  "lastTime": 1731686400000000,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.asks	array	Yes	
.asks[*]	object	-	
.asks[*].price	string	Yes	
.asks[*].size	string	Yes	
.bids	array	Yes	
.bids[*]	object	-	
.bids[*].price	string	Yes	
.bids[*].size	string	Yes	
.group	string	Yes	
.lastTime	integer	Yes	Time in microseconds since unix epoch
.symbol	string	Yes	
#Get Candles
GET /public/candles
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
duration	query	string	Yes	Enum: "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d", "3d", "7d", "30d"
start	query	integer	Yes	Time in microseconds since unix epoch
end	query	integer	Yes	Time in microseconds since unix epoch
Response Body
// Example Response Body
[
  {
    "close": "1.23",
    "duration": 60000000,
    "high": "1.23",
    "low": "1.23",
    "open": "1.23",
    "quoteVolume": "200.1",
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "volume": "20.1"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].close	string	Yes	
[*].duration	integer	Yes	Enum: 60000000, 180000000, 300000000, 900000000, 1800000000, 3600000000, 7200000000, 14400000000, 21600000000, 43200000000, 86400000000, 259200000000, 604800000000, 2592000000000
[*].high	string	Yes	
[*].low	string	Yes	
[*].open	string	Yes	
[*].quoteVolume	string	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].volume	string	Yes	
#Get Chains
GET /public/chains
Response Body
// Example Response Body
[
  {
    "assetSymbol": "BTC",
    "blockTime": 1,
    "confirmations": 1,
    "name": "abc123",
    "symbol": "abc123",
    "type": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].assetSymbol	string	Yes	
[*].blockTime	integer	Yes	
[*].confirmations	integer	Yes	
[*].name	string	Yes	
[*].symbol	string	Yes	
[*].type	integer	Yes	
#Get Contracts
GET /public/contracts
Response Body
// Example Response Body
[
  {
    "baseSymbol": "BTC",
    "fundingRate": "0.000733",
    "high24h": "100000.1",
    "indexCurrency": "USDT",
    "indexPrice": "100000.1",
    "low24h": "90000.1",
    "markPrice": "100000.1",
    "nextFundingRate": "0.000733",
    "nextFundingTime": 1731686400000000,
    "openInterest": "1.1",
    "openInterestUSD": "100000.1",
    "price": "100000.1",
    "price24hAgo": "90000.1",
    "productType": "spot",
    "quoteSymbol": "USDT",
    "quoteVolume24h": "100000.1",
    "symbol": "BTC_USDT",
    "usdVolume24h": "100000.1",
    "volume24h": "1.1"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].baseSymbol	string	Yes	
[*].fundingRate	string	Yes	
[*].high24h	string	Yes	
[*].indexCurrency	string	Yes	
[*].indexPrice	string	Yes	
[*].low24h	string	Yes	
[*].markPrice	string	Yes	
[*].nextFundingRate	string	Yes	
[*].nextFundingTime	integer	Yes	Time in microseconds since unix epoch
[*].openInterest	string	Yes	
[*].openInterestUSD	string	Yes	
[*].price	string	Yes	
[*].price24hAgo	string	Yes	
[*].productType	string	Yes	Enum: "spot", "perpetual"
[*].quoteSymbol	string	Yes	
[*].quoteVolume24h	string	Yes	
[*].symbol	string	Yes	
[*].usdVolume24h	string	Yes	
[*].volume24h	string	Yes	
#Get Funding Rate History
GET /public/funding-rate-history
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
start	query	integer	Yes	Time in microseconds since unix epoch
end	query	integer	Yes	Time in microseconds since unix epoch
Response Body
// Example Response Body
[
  {
    "time": 1704067200000000,
    "value": "1.23"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].value	string	Yes	
#Get Index Price
GET /public/index-price
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
Response Body
// Example Response Body
{
  "constituents": [
    {
      "exchange": "binance",
      "price": "1.23",
      "time": 1704067200000000,
      "weight": "1.23"
    }
  ],
  "price": "1.23",
  "symbol": ".BTC_USDT",
  "time": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.constituents	array	Yes	
.constituents[*]	object	-	
.constituents[*].exchange	string	Yes	Enum: "binance", "bybit", "okx", "coinbase", "kraken", "kucoin", "gateio", "bitmart", "htx", "mexc", "bitget", "crypto.com", "gemini", "binance_us", "arkham"
.constituents[*].price	string	Yes	
.constituents[*].time	integer	Yes	Time of the last update according to the exchange
.constituents[*].weight	string	Yes	
.price	string	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
#Get Index Price History
GET /public/index-price-history
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
start	query	integer	Yes	Time in microseconds since unix epoch
end	query	integer	Yes	Time in microseconds since unix epoch
Response Body
// Example Response Body
[
  {
    "time": 1704067200000000,
    "value": "1.23"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].value	string	Yes	
#Get Index Prices
GET /public/index-prices
Response Body
// Example Response Body
[
  {
    "constituents": [
      {
        "exchange": "binance",
        "price": "1.23",
        "time": 1704067200000000,
        "weight": "1.23"
      }
    ],
    "price": "1.23",
    "symbol": ".BTC_USDT",
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].constituents	array	Yes	
[*].constituents[*]	object	-	
[*].constituents[*].exchange	string	Yes	Enum: "binance", "bybit", "okx", "coinbase", "kraken", "kucoin", "gateio", "bitmart", "htx", "mexc", "bitget", "crypto.com", "gemini", "binance_us", "arkham"
[*].constituents[*].price	string	Yes	
[*].constituents[*].time	integer	Yes	Time of the last update according to the exchange
[*].constituents[*].weight	string	Yes	
[*].price	string	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
#Get L1 Book
GET /public/level-one-book
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
limit	query	integer	No	
Response Body
// Example Response Body
{
  "askPrice": "1.23",
  "askSize": "20.1",
  "bidPrice": "1.23",
  "bidSize": "20.1",
  "revisionId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.askPrice	string	No	
.askSize	string	No	
.bidPrice	string	No	
.bidSize	string	No	
.revisionId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
#Get Margin Schedules
GET /public/margin-schedules
Response Body
// Example Response Body
[
  {
    "bands": [
      {
        "leverageRate": "2",
        "marginRate": "0.5",
        "positionLimit": "5000000",
        "rebate": "211000"
      }
    ],
    "name": "E"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].bands	array	Yes	
[*].bands[*]	object	-	
[*].bands[*].leverageRate	string	Yes	leverage rate applied in this band
[*].bands[*].marginRate	string	Yes	Initial margin rate applied in this band
[*].bands[*].positionLimit	string	Yes	Maximum position size for this band
[*].bands[*].rebate	string	Yes	Initial margin rebate applied in this band
[*].name	string	Yes	Margin schedule name Enum: "A", "B", "C", "D", "E", "F", "G"
#Get MarketCap Chart
GET /public/marketcapchart
Response Body
// Example Response Body
{
  "market_cap_chart": {
    "market_cap": [
      [
        1.23
      ]
    ],
    "volume": [
      [
        1.23
      ]
    ]
  }
}
Name	Type	Required	Description
object	Yes	
.market_cap_chart	object	Yes	
.market_cap_chart.market_cap	array	Yes	
.market_cap_chart.market_cap[*]	array	-	
.market_cap_chart.market_cap[*][*]	number	-	
.market_cap_chart.volume	array	Yes	
.market_cap_chart.volume[*]	array	-	
.market_cap_chart.volume[*][*]	number	-	
#Get Market Caps
GET /public/marketcaps
Response Body
// Example Response Body
{
  "market_cap_change_percentage_24h_usd": 1.23,
  "market_cap_percentage_btc": 1.23,
  "total_market_cap": 1.23
}
Name	Type	Required	Description
object	Yes	
.market_cap_change_percentage_24h_usd	number	Yes	
.market_cap_percentage_btc	number	Yes	
.total_market_cap	number	Yes	
#Get Pair
GET /public/pair
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
Response Body
// Example Response Body
{
  "baseGeckoId": "btc",
  "baseImageUrl": "https://example.com/image.png",
  "baseIsStablecoin": true,
  "baseName": "Bitcoin",
  "baseSymbol": "BTC",
  "marginSchedule": "A",
  "maxLeverage": "10",
  "maxPrice": "1000000",
  "maxPriceScalarDown": "0.5",
  "maxPriceScalarUp": "1.5",
  "maxSize": "1000000",
  "minLotSize": "0.01",
  "minNotional": "5",
  "minPrice": "0.001",
  "minSize": "0.01",
  "minTickPrice": "0.001",
  "pairType": "spot",
  "quoteGeckoId": "usdt",
  "quoteImageUrl": "https://example.com/image.png",
  "quoteIsStablecoin": true,
  "quoteName": "Tether",
  "quoteSymbol": "USDT",
  "status": "staged",
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.baseGeckoId	string	Yes	
.baseImageUrl	string	Yes	Format: url
.baseIsStablecoin	boolean	Yes	
.baseName	string	Yes	
.baseSymbol	string	Yes	
.marginSchedule	string	No	Enum: "A", "B", "C", "D", "E", "F", "G"
.maxLeverage	string	No	
.maxPrice	string	Yes	
.maxPriceScalarDown	string	Yes	Orders rejected if price is less than this scalar times the index price
.maxPriceScalarUp	string	Yes	Orders rejected if price is greater than this scalar times the index price
.maxSize	string	Yes	
.minLotSize	string	Yes	
.minNotional	string	Yes	Minimum notional (price * size) for orders
.minPrice	string	Yes	
.minSize	string	Yes	
.minTickPrice	string	Yes	
.pairType	string	Yes	Enum: "spot", "perpetual"
.quoteGeckoId	string	Yes	
.quoteImageUrl	string	Yes	Format: url
.quoteIsStablecoin	boolean	Yes	
.quoteName	string	Yes	
.quoteSymbol	string	Yes	
.status	string	Yes	Enum: "staged", "listed", "delisted"
.symbol	string	Yes	
#Get Pairs
GET /public/pairs
Response Body
// Example Response Body
[
  {
    "baseGeckoId": "btc",
    "baseImageUrl": "https://example.com/image.png",
    "baseIsStablecoin": true,
    "baseName": "Bitcoin",
    "baseSymbol": "BTC",
    "marginSchedule": "A",
    "maxLeverage": "10",
    "maxPrice": "1000000",
    "maxPriceScalarDown": "0.5",
    "maxPriceScalarUp": "1.5",
    "maxSize": "1000000",
    "minLotSize": "0.01",
    "minNotional": "5",
    "minPrice": "0.001",
    "minSize": "0.01",
    "minTickPrice": "0.001",
    "pairType": "spot",
    "quoteGeckoId": "usdt",
    "quoteImageUrl": "https://example.com/image.png",
    "quoteIsStablecoin": true,
    "quoteName": "Tether",
    "quoteSymbol": "USDT",
    "status": "staged",
    "symbol": "BTC_USDT"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].baseGeckoId	string	Yes	
[*].baseImageUrl	string	Yes	Format: url
[*].baseIsStablecoin	boolean	Yes	
[*].baseName	string	Yes	
[*].baseSymbol	string	Yes	
[*].marginSchedule	string	No	Enum: "A", "B", "C", "D", "E", "F", "G"
[*].maxLeverage	string	No	
[*].maxPrice	string	Yes	
[*].maxPriceScalarDown	string	Yes	Orders rejected if price is less than this scalar times the index price
[*].maxPriceScalarUp	string	Yes	Orders rejected if price is greater than this scalar times the index price
[*].maxSize	string	Yes	
[*].minLotSize	string	Yes	
[*].minNotional	string	Yes	Minimum notional (price * size) for orders
[*].minPrice	string	Yes	
[*].minSize	string	Yes	
[*].minTickPrice	string	Yes	
[*].pairType	string	Yes	Enum: "spot", "perpetual"
[*].quoteGeckoId	string	Yes	
[*].quoteImageUrl	string	Yes	Format: url
[*].quoteIsStablecoin	boolean	Yes	
[*].quoteName	string	Yes	
[*].quoteSymbol	string	Yes	
[*].status	string	Yes	Enum: "staged", "listed", "delisted"
[*].symbol	string	Yes	
#Get Server Time
GET /public/server-time
Response Body
// Example Response Body
{
  "serverTime": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.serverTime	integer	Yes	Time in microseconds since unix epoch
#Get Ticker
GET /public/ticker
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
Response Body
// Example Response Body
{
  "baseSymbol": "BTC",
  "fundingRate": "0.000733",
  "high24h": "100000.1",
  "indexCurrency": "USDT",
  "indexPrice": "100000.1",
  "low24h": "90000.1",
  "markPrice": "100000.1",
  "nextFundingRate": "0.000733",
  "nextFundingTime": 1731686400000000,
  "openInterest": "1.1",
  "openInterestUSD": "100000.1",
  "price": "100000.1",
  "price24hAgo": "90000.1",
  "productType": "spot",
  "quoteSymbol": "USDT",
  "quoteVolume24h": "100000.1",
  "symbol": "BTC_USDT",
  "usdVolume24h": "100000.1",
  "volume24h": "1.1"
}
Name	Type	Required	Description
object	Yes	
.baseSymbol	string	Yes	
.fundingRate	string	Yes	
.high24h	string	Yes	
.indexCurrency	string	Yes	
.indexPrice	string	Yes	
.low24h	string	Yes	
.markPrice	string	Yes	
.nextFundingRate	string	Yes	
.nextFundingTime	integer	Yes	Time in microseconds since unix epoch
.openInterest	string	Yes	
.openInterestUSD	string	Yes	
.price	string	Yes	
.price24hAgo	string	Yes	
.productType	string	Yes	Enum: "spot", "perpetual"
.quoteSymbol	string	Yes	
.quoteVolume24h	string	Yes	
.symbol	string	Yes	
.usdVolume24h	string	Yes	
.volume24h	string	Yes	
#Get Tickers
GET /public/tickers
Response Body
// Example Response Body
[
  {
    "baseSymbol": "BTC",
    "fundingRate": "0.000733",
    "high24h": "100000.1",
    "indexCurrency": "USDT",
    "indexPrice": "100000.1",
    "low24h": "90000.1",
    "markPrice": "100000.1",
    "nextFundingRate": "0.000733",
    "nextFundingTime": 1731686400000000,
    "openInterest": "1.1",
    "openInterestUSD": "100000.1",
    "price": "100000.1",
    "price24hAgo": "90000.1",
    "productType": "spot",
    "quoteSymbol": "USDT",
    "quoteVolume24h": "100000.1",
    "symbol": "BTC_USDT",
    "usdVolume24h": "100000.1",
    "volume24h": "1.1"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].baseSymbol	string	Yes	
[*].fundingRate	string	Yes	
[*].high24h	string	Yes	
[*].indexCurrency	string	Yes	
[*].indexPrice	string	Yes	
[*].low24h	string	Yes	
[*].markPrice	string	Yes	
[*].nextFundingRate	string	Yes	
[*].nextFundingTime	integer	Yes	Time in microseconds since unix epoch
[*].openInterest	string	Yes	
[*].openInterestUSD	string	Yes	
[*].price	string	Yes	
[*].price24hAgo	string	Yes	
[*].productType	string	Yes	Enum: "spot", "perpetual"
[*].quoteSymbol	string	Yes	
[*].quoteVolume24h	string	Yes	
[*].symbol	string	Yes	
[*].usdVolume24h	string	Yes	
[*].volume24h	string	Yes	
#Get Public Trades
GET /public/trades
Parameters
Name	In	Type	Required	Description
symbol	query	string	Yes	
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "price": "1.23",
    "revisionId": 1,
    "size": "20.1",
    "symbol": "BTC_USDT",
    "takerSide": "buy",
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].price	string	Yes	
[*].revisionId	integer	Yes	
[*].size	string	Yes	
[*].symbol	string	Yes	
[*].takerSide	string	Yes	Enum: "buy", "sell"
[*].time	integer	Yes	Time in microseconds since unix epoch
Orders#
#Get Orders
GET /orders
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "arkmFeePaid": "20.1",
    "avgPrice": "1.23",
    "brokerId": 1,
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "creditFeePaid": "200.1",
    "executedNotional": "200.1",
    "executedSize": "20.1",
    "lastArkmFee": "0.01",
    "lastCreditFee": "0.01",
    "lastMarginBonusFee": "0.01",
    "lastPrice": "1.5",
    "lastQuoteFee": "0.01",
    "lastSize": "1000",
    "lastTime": 1704067200000000,
    "marginBonusFeePaid": "200.1",
    "orderId": 1,
    "postOnly": true,
    "price": "1.23",
    "quoteFeePaid": "200.1",
    "reduceOnly": true,
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "status": "new",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "type": "limitGtc",
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
[*].avgPrice	string	Yes	Average price filled so far in the order
[*].brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
[*].clientOrderId	string	No	
[*].creditFeePaid	string	Yes	Total fee paid via credits so far in the order
[*].executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
[*].executedSize	string	Yes	Total quantity filled so far in the order
[*].lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
[*].lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
[*].lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
[*].lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
[*].lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
[*].lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
[*].lastTime	integer	Yes	Time of the last status update on the order
[*].marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
[*].orderId	integer	Yes	
[*].postOnly	boolean	Yes	If true the order is post-only
[*].price	string	Yes	The original price of the order
[*].quoteFeePaid	string	Yes	Total quote fee paid so far in the order
[*].reduceOnly	boolean	Yes	If true the order is reduce-only
[*].revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	The original size of the order
[*].status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
[*].userId	integer	Yes	
#Get Open Order By Client Order Id
GET /orders/by-client-order-id
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
clientOrderId	query	string	No	
Response Body
// Example Response Body
{
  "arkmFeePaid": "20.1",
  "avgPrice": "1.23",
  "brokerId": 1,
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "creditFeePaid": "200.1",
  "executedNotional": "200.1",
  "executedSize": "20.1",
  "lastArkmFee": "0.01",
  "lastCreditFee": "0.01",
  "lastMarginBonusFee": "0.01",
  "lastPrice": "1.5",
  "lastQuoteFee": "0.01",
  "lastSize": "1000",
  "lastTime": 1704067200000000,
  "marginBonusFeePaid": "200.1",
  "orderId": 1,
  "postOnly": true,
  "price": "1.23",
  "quoteFeePaid": "200.1",
  "reduceOnly": true,
  "revisionId": 1,
  "side": "buy",
  "size": "20.1",
  "status": "new",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000,
  "triggerOrderId": 1,
  "type": "limitGtc",
  "userId": 1
}
Name	Type	Required	Description
object	Yes	
.arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
.avgPrice	string	Yes	Average price filled so far in the order
.brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
.clientOrderId	string	No	
.creditFeePaid	string	Yes	Total fee paid via credits so far in the order
.executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
.executedSize	string	Yes	Total quantity filled so far in the order
.lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
.lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
.lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
.lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
.lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
.lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
.lastTime	integer	Yes	Time of the last status update on the order
.marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
.orderId	integer	Yes	
.postOnly	boolean	Yes	If true the order is post-only
.price	string	Yes	The original price of the order
.quoteFeePaid	string	Yes	Total quote fee paid so far in the order
.reduceOnly	boolean	Yes	If true the order is reduce-only
.revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	The original size of the order
.status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
.subaccountId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
.triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
.userId	integer	Yes	
#Cancel Order
POST /orders/cancel
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "orderId": 1,
  "subaccountId": 1,
  "timeToCancel": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.clientOrderId	string	No	client order ID to cancel, required if orderId is not provided
.orderId	integer	No	order ID to cancel, required if clientOrderId is not provided
.subaccountId	integer	No	Default: 0
.timeToCancel	integer	No	Time to cancel the order, 0 for immediate. Granularity is 1 second. Default: 0
Response Body
// Example Response Body
{
  "orderId": 1
}
Name	Type	Required	Description
object	Yes	
.orderId	integer	Yes	
#Cancel and Replace Order
POST /orders/cancel-replace
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "brokerId": 1,
  "cancelClientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "cancelOrderId": 1,
  "cancelSubaccountId": 1,
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "postOnly": false,
  "price": "1.23",
  "reduceOnly": false,
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.cancelClientOrderId	string	No	Client Order ID of the order to cancel and replace with the new order
.cancelOrderId	integer	No	ID of the order to cancel and replace with the new order
.cancelSubaccountId	integer	No	Subaccount ID of the order to cancel and replace with the new order Default: 0
.clientOrderId	string	No	
.postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.price	string	No	limit price, 0 for market orders
.reduceOnly	boolean	No	if true, the order will only reduce the position size.
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	No	Default: 0
.symbol	string	Yes	
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Body
// Example Response Body
{
  "cancelResponse": {
    "orderId": 1
  },
  "createResponse": {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "orderId": 1,
    "price": "1.23",
    "side": "buy",
    "size": "20.1",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "type": "limitGtc"
  }
}
Name	Type	Required	Description
object	Yes	
.cancelResponse	object	No	
.cancelResponse.orderId	integer	Yes	
.createResponse	object	No	
.createResponse.clientOrderId	string	No	
.createResponse.orderId	integer	Yes	
.createResponse.price	string	Yes	
.createResponse.side	string	Yes	Enum: "buy", "sell"
.createResponse.size	string	Yes	
.createResponse.subaccountId	integer	Yes	
.createResponse.symbol	string	Yes	
.createResponse.time	integer	Yes	Time in microseconds since unix epoch
.createResponse.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Cancel All
POST /orders/cancel/all
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "subaccountId": 1,
  "timeToCancel": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.subaccountId	integer	Yes	Default: 0
.timeToCancel	integer	Yes	Time to cancel all orders, 0 for immediate. Granularity is 1 second. Use this to set a dead man's switch. Default: 0
#Get Order History
GET /orders/history
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
symbol	query	string	No	
subaccountId	query	integer	No	Default: 0
limit	query	integer	No	Default: 50
offset	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "arkmFeePaid": "20.1",
    "avgPrice": "1.23",
    "brokerId": 1,
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "creditFeePaid": "200.1",
    "executedNotional": "200.1",
    "executedSize": "20.1",
    "lastArkmFee": "0.01",
    "lastCreditFee": "0.01",
    "lastMarginBonusFee": "0.01",
    "lastPrice": "1.5",
    "lastQuoteFee": "0.01",
    "lastSize": "1000",
    "lastTime": 1704067200000000,
    "marginBonusFeePaid": "200.1",
    "orderId": 1,
    "postOnly": true,
    "price": "1.23",
    "quoteFeePaid": "200.1",
    "reduceOnly": true,
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "status": "new",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "type": "limitGtc",
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
[*].avgPrice	string	Yes	Average price filled so far in the order
[*].brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
[*].clientOrderId	string	No	
[*].creditFeePaid	string	Yes	Total fee paid via credits so far in the order
[*].executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
[*].executedSize	string	Yes	Total quantity filled so far in the order
[*].lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
[*].lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
[*].lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
[*].lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
[*].lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
[*].lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
[*].lastTime	integer	Yes	Time of the last status update on the order
[*].marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
[*].orderId	integer	Yes	
[*].postOnly	boolean	Yes	If true the order is post-only
[*].price	string	Yes	The original price of the order
[*].quoteFeePaid	string	Yes	Total quote fee paid so far in the order
[*].reduceOnly	boolean	Yes	If true the order is reduce-only
[*].revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	The original size of the order
[*].status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
[*].userId	integer	Yes	
#Get all order for Client Order Id
GET /orders/history/by-client-order-id
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
clientOrderId	query	string	No	
Response Body
// Example Response Body
[
  {
    "arkmFeePaid": "20.1",
    "avgPrice": "1.23",
    "brokerId": 1,
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "creditFeePaid": "200.1",
    "executedNotional": "200.1",
    "executedSize": "20.1",
    "lastArkmFee": "0.01",
    "lastCreditFee": "0.01",
    "lastMarginBonusFee": "0.01",
    "lastPrice": "1.5",
    "lastQuoteFee": "0.01",
    "lastSize": "1000",
    "lastTime": 1704067200000000,
    "marginBonusFeePaid": "200.1",
    "orderId": 1,
    "postOnly": true,
    "price": "1.23",
    "quoteFeePaid": "200.1",
    "reduceOnly": true,
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "status": "new",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "type": "limitGtc",
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
[*].avgPrice	string	Yes	Average price filled so far in the order
[*].brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
[*].clientOrderId	string	No	
[*].creditFeePaid	string	Yes	Total fee paid via credits so far in the order
[*].executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
[*].executedSize	string	Yes	Total quantity filled so far in the order
[*].lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
[*].lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
[*].lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
[*].lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
[*].lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
[*].lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
[*].lastTime	integer	Yes	Time of the last status update on the order
[*].marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
[*].orderId	integer	Yes	
[*].postOnly	boolean	Yes	If true the order is post-only
[*].price	string	Yes	The original price of the order
[*].quoteFeePaid	string	Yes	Total quote fee paid so far in the order
[*].reduceOnly	boolean	Yes	If true the order is reduce-only
[*].revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	The original size of the order
[*].status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
[*].userId	integer	Yes	
#Get Total Orders
GET /orders/history_offset
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
symbol	query	string	No	
subaccountId	query	integer	No	Default: 0
limit	query	integer	No	Default: 50
offset	query	integer	No	Default: 0
Response Body
// Example Response Body
{
  "orders": [
    {
      "arkmFeePaid": "20.1",
      "avgPrice": "1.23",
      "brokerId": 1,
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "creditFeePaid": "200.1",
      "executedNotional": "200.1",
      "executedSize": "20.1",
      "lastArkmFee": "0.01",
      "lastCreditFee": "0.01",
      "lastMarginBonusFee": "0.01",
      "lastPrice": "1.5",
      "lastQuoteFee": "0.01",
      "lastSize": "1000",
      "lastTime": 1704067200000000,
      "marginBonusFeePaid": "200.1",
      "orderId": 1,
      "postOnly": true,
      "price": "1.23",
      "quoteFeePaid": "200.1",
      "reduceOnly": true,
      "revisionId": 1,
      "side": "buy",
      "size": "20.1",
      "status": "new",
      "subaccountId": 1,
      "symbol": "BTC_USDT",
      "time": 1704067200000000,
      "triggerOrderId": 1,
      "type": "limitGtc",
      "userId": 1
    }
  ],
  "total": 1
}
Name	Type	Required	Description
object	Yes	
.orders	array	Yes	
.orders[*]	object	-	
.orders[*].arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
.orders[*].avgPrice	string	Yes	Average price filled so far in the order
.orders[*].brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
.orders[*].clientOrderId	string	No	
.orders[*].creditFeePaid	string	Yes	Total fee paid via credits so far in the order
.orders[*].executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
.orders[*].executedSize	string	Yes	Total quantity filled so far in the order
.orders[*].lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
.orders[*].lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
.orders[*].lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
.orders[*].lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
.orders[*].lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
.orders[*].lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
.orders[*].lastTime	integer	Yes	Time of the last status update on the order
.orders[*].marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
.orders[*].orderId	integer	Yes	
.orders[*].postOnly	boolean	Yes	If true the order is post-only
.orders[*].price	string	Yes	The original price of the order
.orders[*].quoteFeePaid	string	Yes	Total quote fee paid so far in the order
.orders[*].reduceOnly	boolean	Yes	If true the order is reduce-only
.orders[*].revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
.orders[*].side	string	Yes	Enum: "buy", "sell"
.orders[*].size	string	Yes	The original size of the order
.orders[*].status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
.orders[*].subaccountId	integer	Yes	
.orders[*].symbol	string	Yes	
.orders[*].time	integer	Yes	Time in microseconds since unix epoch
.orders[*].triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
.orders[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
.orders[*].userId	integer	Yes	
.total	integer	Yes	
#Create Order
POST /orders/new
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "brokerId": 1,
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "postOnly": false,
  "price": "1.23",
  "reduceOnly": false,
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.clientOrderId	string	No	
.postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.price	string	No	limit price, 0 for market orders
.reduceOnly	boolean	No	if true, the order will only reduce the position size.
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	No	Default: 0
.symbol	string	Yes	
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Body
// Example Response Body
{
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "orderId": 1,
  "price": "1.23",
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000,
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.clientOrderId	string	No	
.orderId	integer	Yes	
.price	string	Yes	
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Create Multiple Orders
POST /orders/new/batch
Orders are processed sequentially and returned in the same order as the input requests.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "orders": [
    {
      "brokerId": 1,
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "postOnly": false,
      "price": "1.23",
      "reduceOnly": false,
      "side": "buy",
      "size": "20.1",
      "subaccountId": 1,
      "symbol": "BTC_USDT",
      "type": "limitGtc"
    }
  ]
}
Name	Type	Required	Description
object	Yes	
.orders	array	Yes	
.orders[*]	object	-	
.orders[*].brokerId	integer	No	The ID of the broker used to create this order Default: 0
.orders[*].clientOrderId	string	No	
.orders[*].postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.orders[*].price	string	No	limit price, 0 for market orders
.orders[*].reduceOnly	boolean	No	if true, the order will only reduce the position size.
.orders[*].side	string	Yes	Enum: "buy", "sell"
.orders[*].size	string	Yes	
.orders[*].subaccountId	integer	No	Default: 0
.orders[*].symbol	string	Yes	
.orders[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Body
// Example Response Body
{
  "orders": [
    {
      "orderId": 1,
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "symbol": "BTC_USDT",
      "subaccountId": 0,
      "side": "buy",
      "type": "limitGtc",
      "size": "20.1",
      "price": "1.23"
    },
    {
      "clientOrderId": "123e4567-e89b-12d3-a456-426614174001",
      "symbol": "BTC_USDT",
      "subaccountId": 0,
      "side": "buy",
      "type": "limitGtc",
      "size": "20.1",
      "price": "0",
      "error": {
        "id": 30002,
        "name": "InvalidPrice",
        "message": "price must be greater than 0"
      }
    }
  ]
}
Name	Type	Required	Description
object	Yes	
.orders	array	Yes	
.orders[*]	object	-	
.orders[*].clientOrderId	string	No	
.orders[*].error	object	No	
.orders[*].error.id	integer	Yes	The unique identifier for the error Enum: 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 20001, 20002, 20003, 20004, 20005, 30001, 30002, 30003, 30004, 30005, 30006, 30007, 30008, 30009, 30010, 30011, 30012, 30013, 30014, 30015, 30016, 30017, 30018, 30019, 30020, 30021, 30022, 30023, 30024, 30025, 30026, 30027, 30028, 40001, 40002, 40003, 40004, 40005, 40006, 40007, 40008, 40009, 40010, 40011, 40012, 40013, 40014, 90001, 90002, 90003, 90004, 90005, 90006, 90007, 90008, 90009, 90010, 90011
.orders[*].error.message	string	Yes	Additional details about the error
.orders[*].error.name	string	Yes	The name of the error Enum: "InternalError", "BadRequest", "Unauthorized", "InvalidSymbol", "SymbolRequired", "RateLimitExceeded", "Forbidden", "InvalidIP", "Throttled", "KeyNotPermitted", "ParsingKey", "VerifyingKey", "RequiresRead", "RequiresWrite", "SignatureMissing", "ExpiresMissing", "ParsingExpires", "ExpiresTooFar", "ExpiredSignature", "SignatureMismatch", "IPNotAllowed", "MFA", "ParsingRequest", "SubaccountNotFound", "Conflict", "NotFound", "ApiKeyNotAllowed", "MethodNotAllowed", "InvalidMethod", "MethodRequired", "InvalidChannel", "ChannelRequired", "InvalidGroup", "InvalidSize", "InvalidPrice", "InvalidPostOnly", "InvalidReduceOnly", "InvalidNotional", "UnknownOrderType", "PairNotEnabled", "TradingFreeze", "PostOnly", "InsufficientBalance", "InvalidPair", "NoMarkPrice", "InsufficientLiquidity", "ClientOrderIdAlreadyExists", "ClientOrderIdNotFound", "ReduceOnlyInvalid", "UnsupportedOrderSide", "UnsupportedAssetType", "PositionLimit", "InvalidClientOrderID", "InvalidTriggerType", "InvalidTriggerPriceType", "InvalidOrderSide", "InvalidOrderType", "InvalidBrokerId", "UserFrozen", "UserDeleted", "OrderIdNotFound", "FailedRiskCheck", "MemoNotSupported", "InvalidWithdrawalAddress", "PositionNotFound", "InvalidChain", "FuturesNotEnabled", "SubaccountHasOpenFuturePositions", "LspAssignmentGreaterThanMaxNotional", "LspMaxNotionalGreaterThanMarginLimit", "LspMaxNotionalMustNotBeNegative", "PortfolioLiquidation", "NegativeAmount", "ZeroAmount", "NeedStateAcknowledgement", "InvalidAlertType", "InvalidAlertPriceType", "InvalidVoucherStatus", "InvalidCandleDuration", "InvalidNotificationType", "TooManyMFAAttempts", "InvalidMFA", "TooManyAttempts", "InvalidRole", "InvalidEmail", "ChangeEmailRequestRateLimited"
.orders[*].orderId	integer	No	
.orders[*].price	string	Yes	
.orders[*].side	string	Yes	Enum: "buy", "sell"
.orders[*].size	string	Yes	
.orders[*].subaccountId	integer	Yes	
.orders[*].symbol	string	Yes	
.orders[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Create Simple Order
POST /orders/new/simple
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "brokerId": 1,
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	Yes	Default: 0
.symbol	string	Yes	
Response Body
// Example Response Body
{
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "orderId": 1,
  "price": "1.23",
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000,
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.clientOrderId	string	No	
.orderId	integer	Yes	
.price	string	Yes	
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Get Order By Id
GET /orders/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
id	path	integer	Yes	
Response Body
// Example Response Body
{
  "arkmFeePaid": "20.1",
  "avgPrice": "1.23",
  "brokerId": 1,
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "creditFeePaid": "200.1",
  "executedNotional": "200.1",
  "executedSize": "20.1",
  "lastArkmFee": "0.01",
  "lastCreditFee": "0.01",
  "lastMarginBonusFee": "0.01",
  "lastPrice": "1.5",
  "lastQuoteFee": "0.01",
  "lastSize": "1000",
  "lastTime": 1704067200000000,
  "marginBonusFeePaid": "200.1",
  "orderId": 1,
  "postOnly": true,
  "price": "1.23",
  "quoteFeePaid": "200.1",
  "reduceOnly": true,
  "revisionId": 1,
  "side": "buy",
  "size": "20.1",
  "status": "new",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000,
  "triggerOrderId": 1,
  "type": "limitGtc",
  "userId": 1
}
Name	Type	Required	Description
object	Yes	
.arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
.avgPrice	string	Yes	Average price filled so far in the order
.brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
.clientOrderId	string	No	
.creditFeePaid	string	Yes	Total fee paid via credits so far in the order
.executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
.executedSize	string	Yes	Total quantity filled so far in the order
.lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
.lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
.lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
.lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
.lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
.lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
.lastTime	integer	Yes	Time of the last status update on the order
.marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
.orderId	integer	Yes	
.postOnly	boolean	Yes	If true the order is post-only
.price	string	Yes	The original price of the order
.quoteFeePaid	string	Yes	Total quote fee paid so far in the order
.reduceOnly	boolean	Yes	If true the order is reduce-only
.revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	The original size of the order
.status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
.subaccountId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
.triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
.userId	integer	Yes	
Trades#
#Get User Trades
GET /trades
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
symbol	query	string	No	
subaccountId	query	integer	No	Default: 0
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "arkmFee": "20.1",
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "orderId": 1,
    "price": "1.23",
    "quoteFee": "200.1",
    "revisionId": 1,
    "size": "20.1",
    "symbol": "BTC_USDT",
    "takerSide": "buy",
    "time": 1704067200000000,
    "userSide": "buy"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFee	string	Yes	
[*].clientOrderId	string	Yes	
[*].orderId	integer	Yes	
[*].price	string	Yes	
[*].quoteFee	string	Yes	
[*].revisionId	integer	Yes	
[*].size	string	Yes	
[*].symbol	string	Yes	
[*].takerSide	string	Yes	Enum: "buy", "sell"
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userSide	string	Yes	Enum: "buy", "sell"
#Get User Trades History
GET /trades/history
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
symbol	query	string	No	
subaccountId	query	integer	No	Default: 0
limit	query	integer	No	Default: 50
offset	query	integer	No	Default: 0
Response Body
// Example Response Body
{
  "total": 1,
  "trades": [
    {
      "arkmFee": "20.1",
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "orderId": 1,
      "price": "1.23",
      "quoteFee": "200.1",
      "revisionId": 1,
      "size": "20.1",
      "symbol": "BTC_USDT",
      "takerSide": "buy",
      "time": 1704067200000000,
      "userSide": "buy"
    }
  ]
}
Name	Type	Required	Description
object	Yes	
.total	integer	Yes	
.trades	array	Yes	
.trades[*]	object	-	
.trades[*].arkmFee	string	Yes	
.trades[*].clientOrderId	string	Yes	
.trades[*].orderId	integer	Yes	
.trades[*].price	string	Yes	
.trades[*].quoteFee	string	Yes	
.trades[*].revisionId	integer	Yes	
.trades[*].size	string	Yes	
.trades[*].symbol	string	Yes	
.trades[*].takerSide	string	Yes	Enum: "buy", "sell"
.trades[*].time	integer	Yes	Time in microseconds since unix epoch
.trades[*].userSide	string	Yes	Enum: "buy", "sell"
#Get User Trades By Time
GET /trades/time
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
from	query	integer	No	time from, inclusive
to	query	integer	No	time to, inclusive
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "arkmFee": "20.1",
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "orderId": 1,
    "price": "1.23",
    "quoteFee": "200.1",
    "revisionId": 1,
    "size": "20.1",
    "symbol": "BTC_USDT",
    "takerSide": "buy",
    "time": 1704067200000000,
    "userSide": "buy"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFee	string	Yes	
[*].clientOrderId	string	Yes	
[*].orderId	integer	Yes	
[*].price	string	Yes	
[*].quoteFee	string	Yes	
[*].revisionId	integer	Yes	
[*].size	string	Yes	
[*].symbol	string	Yes	
[*].takerSide	string	Yes	Enum: "buy", "sell"
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userSide	string	Yes	Enum: "buy", "sell"
Trigger Orders#
#Get Trigger Orders
GET /trigger-orders
Get all trigger orders for the authenticated user.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "postOnly": true,
    "price": "1.23",
    "reduceOnly": true,
    "side": "buy",
    "size": "20.1",
    "status": "staged",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "triggerPrice": "1.23",
    "triggerPriceType": "last",
    "triggerType": "takeProfit",
    "type": "limitGtc"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].clientOrderId	string	Yes	
[*].postOnly	boolean	Yes	
[*].price	string	Yes	
[*].reduceOnly	boolean	Yes	
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	
[*].status	string	Yes	Enum: "staged", "triggered", "cancelled"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	Yes	
[*].triggerPrice	string	Yes	
[*].triggerPriceType	string	Yes	Enum: "last", "mark", "index"
[*].triggerType	string	Yes	Enum: "takeProfit", "stopLoss"
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Cancel Trigger Order
POST /trigger-orders/cancel
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "triggerOrderId": 1
}
Name	Type	Required	Description
object	Yes	
.clientOrderId	string	No	
.subaccountId	integer	No	Default: 0
.symbol	string	Yes	
.triggerOrderId	integer	No	
.triggerPriceType		No	
Response Body
// Example Response Body
{
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "triggerOrderId": 1
}
Name	Type	Required	Description
object	Yes	
.clientOrderId	string	No	
.subaccountId	integer	No	Default: 0
.symbol	string	Yes	
.triggerOrderId	integer	No	
.triggerPriceType		No	
#Cancel AllTrigger Orders
POST /trigger-orders/cancel/all
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "subaccountId": 1,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.subaccountId	integer	Yes	
.symbol	string	Yes	
.triggerPriceType		No	
Response Body
// Example Response Body
{
  "subaccountId": 1,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.subaccountId	integer	Yes	
.symbol	string	Yes	
.triggerPriceType		No	
#Create Trigger Order
POST /trigger-orders/new
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "brokerId": 1,
  "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
  "postOnly": false,
  "price": "1.23",
  "reduceOnly": false,
  "side": "buy",
  "size": "20.1",
  "subaccountId": 1,
  "symbol": "BTC_USDT",
  "triggerPrice": "1.23",
  "triggerPriceType": "last",
  "triggerType": "takeProfit",
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.clientOrderId	string	No	
.postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.price	string	No	limit price, 0 for market orders
.reduceOnly	boolean	No	if true, the order will only reduce the position size.
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.subaccountId	integer	No	Default: 0
.symbol	string	Yes	
.triggerPrice	string	Yes	
.triggerPriceType	string	Yes	Enum: "last", "mark", "index"
.triggerType	string	Yes	Enum: "takeProfit", "stopLoss"
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Body
// Example Response Body
{
  "price": "1.23",
  "side": "buy",
  "size": "20.1",
  "symbol": "BTC_USDT",
  "triggerOrderId": 1,
  "type": "limitGtc"
}
Name	Type	Required	Description
object	Yes	
.price	string	Yes	
.side	string	Yes	Enum: "buy", "sell"
.size	string	Yes	
.symbol	string	Yes	
.triggerOrderId	integer	Yes	
.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Account#
#Get Airdrops
GET /account/airdrops
Get the user's airdrops

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "id": 1,
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].id	integer	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Balance Updates
GET /account/balance-updates
Get the user's balance updates

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
reason	query	string	No	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "balance": "20.1",
    "id": 1,
    "reason": "orderFill",
    "subaccountId": 1,
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].balance	string	Yes	
[*].id	integer	Yes	
[*].reason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
#Get Balances
GET /account/balances
Get the user's current balances

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "balance": "20.1",
    "balanceUSDT": "200.1",
    "free": "20.1",
    "freeUSDT": "200.1",
    "lastUpdateAmount": "20.1",
    "lastUpdateId": 1,
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "priceUSDT": "1.23",
    "subaccountId": 1,
    "symbol": "BTC"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].balance	string	Yes	
[*].balanceUSDT	string	Yes	
[*].free	string	Yes	
[*].freeUSDT	string	Yes	
[*].lastUpdateAmount	string	Yes	
[*].lastUpdateId	integer	Yes	
[*].lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
[*].priceUSDT	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
#Get Balances across all subaccounts
GET /account/balances/all
Get the user's current balances across all subaccounts

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "balance": "20.1",
    "balanceUSDT": "200.1",
    "free": "20.1",
    "freeUSDT": "200.1",
    "lastUpdateAmount": "20.1",
    "lastUpdateId": 1,
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "priceUSDT": "1.23",
    "subaccountId": 1,
    "symbol": "BTC"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].balance	string	Yes	
[*].balanceUSDT	string	Yes	
[*].free	string	Yes	
[*].freeUSDT	string	Yes	
[*].lastUpdateAmount	string	Yes	
[*].lastUpdateId	integer	Yes	
[*].lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
[*].priceUSDT	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
#Get User Subaccount Balance History
GET /account/balances/history
Get the balance history for a subaccount

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
start	query	integer	No	Time in microseconds since unix epoch
end	query	integer	No	Time in microseconds since unix epoch
appendCurrentBalance	query	boolean	No	
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
#Get Commissions
GET /account/commissions
Get the user's commissions

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 100
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "id": 1,
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].id	integer	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Deposit Addresses
GET /account/deposit/addresses
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
chain	query	string	Yes	
Response Body
// Example Response Body
{
  "addresses": [
    "abc123"
  ]
}
Name	Type	Required	Description
object	Yes	
.addresses	array	Yes	
.addresses[*]	string	-	
#Create Deposit Address
POST /account/deposit/addresses/new
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "chain": "abc123",
  "isMoonpay": true,
  "subaccountId": 1
}
Name	Type	Required	Description
object	Yes	
.chain	string	Yes	
.isMoonpay	boolean	Yes	Default: false
.subaccountId	integer	Yes	Default: 0
Response Body
// Example Response Body
{
  "address": "abc123"
}
Name	Type	Required	Description
object	Yes	
.address	string	Yes	
#Get Deposits
GET /account/deposits
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "chain": "abc123",
    "confirmed": true,
    "depositAddress": "abc123",
    "id": 1,
    "price": "1.23",
    "symbol": "BTC",
    "time": 1704067200000000,
    "transactionHash": "abc123"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].chain	string	Yes	
[*].confirmed	boolean	Yes	
[*].depositAddress	string	Yes	
[*].id	integer	Yes	
[*].price	string	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].transactionHash	string	Yes	
#Get User Fees
GET /account/fees
Get the user's current trading fees

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
{
  "perpMakerFee": "1.23",
  "perpTakerFee": "1.23",
  "spotMakerFee": "1.23",
  "spotTakerFee": "1.23"
}
Name	Type	Required	Description
object	Yes	
.perpMakerFee	string	Yes	
.perpTakerFee	string	Yes	
.spotMakerFee	string	Yes	
.spotTakerFee	string	Yes	
#Get Funding Rate Payments
GET /account/funding-rate-payments
Get the user's funding rate payments

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 100
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "id": 1,
    "indexPrice": "1.23",
    "pairSymbol": "BTC_USDT",
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].id	integer	Yes	
[*].indexPrice	string	Yes	
[*].pairSymbol	string	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Position Limits
GET /account/leverage
Gets the user specified position leverage

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
Response Body
// Example Response Body
[
  {
    "leverage": "1.23",
    "symbol": "BTC_USDT"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].leverage	string	Yes	
[*].symbol	string	Yes	
#Get Position Limits
POST /account/leverage
Sets the user specified position leverage for a given pair

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "leverage": "1.23",
  "subaccountId": 1,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.leverage	string	Yes	
.subaccountId	integer	No	
.symbol	string	Yes	
#Get Liquidation Price
GET /account/liquidation-price
Get liquidation price for a perpetual position

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
symbol	query	string	No	
Response Body
// Example Response Body
{
  "price": "1.23",
  "subaccountId": 1,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.price	string	No	
.subaccountId	integer	Yes	
.symbol	string	Yes	
#Get LSP Assignments
GET /account/lsp-assignments
Get the user's lsp assignments

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 100
Response Body
// Example Response Body
[
  {
    "base": "20.1",
    "id": 1,
    "pairSymbol": "BTC_USDT",
    "price": "1.23",
    "quote": "200.1",
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].base	string	Yes	
[*].id	integer	Yes	
[*].pairSymbol	string	Yes	
[*].price	string	Yes	
[*].quote	string	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Account Margin
GET /account/margin
Get the user's current margin usage details

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
Response Body
// Example Response Body
{
  "available": "5000",
  "bonus": "100",
  "initial": "1000",
  "liquidation": "400",
  "locked": "1000",
  "maintenance": "600",
  "pnl": "100",
  "subaccountId": 1,
  "total": "6000",
  "totalAssetValue": "1.0"
}
Name	Type	Required	Description
object	Yes	
.available	string	Yes	Total margin available for opening new positions
.bonus	string	Yes	Total margin bonus
.initial	string	Yes	Initial margin required to open a position
.liquidation	string	Yes	Amount of Margin required to prevent portfolio liquidations
.locked	string	Yes	Total margin locked due to open positions and open orders
.maintenance	string	Yes	Amount of Margin required to prevent partial liquidations
.pnl	string	Yes	Total unrealized PnL
.subaccountId	integer	Yes	
.total	string	Yes	Total margin in the account, includes unrealized PnL
.totalAssetValue	string	Yes	Total value of all assets in the account in USDT
#Get Account Margin across all subaccounts
GET /account/margin/all
Get the user's current margin usage details

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "available": "5000",
    "bonus": "100",
    "initial": "1000",
    "liquidation": "400",
    "locked": "1000",
    "maintenance": "600",
    "pnl": "100",
    "subaccountId": 1,
    "total": "6000",
    "totalAssetValue": "1.0"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].available	string	Yes	Total margin available for opening new positions
[*].bonus	string	Yes	Total margin bonus
[*].initial	string	Yes	Initial margin required to open a position
[*].liquidation	string	Yes	Amount of Margin required to prevent portfolio liquidations
[*].locked	string	Yes	Total margin locked due to open positions and open orders
[*].maintenance	string	Yes	Amount of Margin required to prevent partial liquidations
[*].pnl	string	Yes	Total unrealized PnL
[*].subaccountId	integer	Yes	
[*].total	string	Yes	Total margin in the account, includes unrealized PnL
[*].totalAssetValue	string	Yes	Total value of all assets in the account in USDT
#Get Notifications
GET /account/notifications
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
type	query	string	No	Enum: "announcement", "order", "price", "margin", "deposit", "withdrawal", "deleverage", "rebate", "commission", "adjustment", "airdrop", "reward", "expiration"
limit	query	integer	No	Default: 50
offset	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "id": 1,
    "isRead": true,
    "message": "abc123",
    "orderId": 1,
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "title": "abc123",
    "type": "announcement"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].id	integer	Yes	
[*].isRead	boolean	Yes	
[*].message	string	Yes	
[*].orderId	integer	No	
[*].subaccountId	integer	Yes	
[*].symbol	string	No	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].title	string	Yes	
[*].type	string	Yes	Enum: "announcement", "order", "price", "margin", "deposit", "withdrawal", "deleverage", "rebate", "commission", "adjustment", "airdrop", "reward", "expiration"
#Mark Notifications Read
POST /account/notifications/read
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "lastReadTime": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.lastReadTime	integer	Yes	Time in microseconds since unix epoch
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Get Position Updates
GET /account/position-updates
Get the user's position updates

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
reason	query	string	No	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "avgEntryPrice": "1.23",
    "base": "20.1",
    "baseDelta": "20.1",
    "id": 1,
    "pairSymbol": "BTC_USDT",
    "quote": "200.1",
    "quoteDelta": "200.1",
    "reason": "orderFill",
    "subaccountId": 1,
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].avgEntryPrice	string	Yes	
[*].base	string	Yes	
[*].baseDelta	string	Yes	
[*].id	integer	Yes	
[*].pairSymbol	string	Yes	
[*].quote	string	Yes	
[*].quoteDelta	string	Yes	
[*].reason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
#Get Positions
GET /account/positions
Get list of the current positions

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
Response Body
// Example Response Body
[
  {
    "averageEntryPrice": "67992.60",
    "base": "1",
    "breakEvenPrice": "1.23",
    "initialMargin": "200.1",
    "lastUpdateBaseDelta": "20.1",
    "lastUpdateId": 1,
    "lastUpdateQuoteDelta": "200.1",
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "maintenanceMargin": "200.1",
    "markPrice": "1.23",
    "openBuyNotional": "200.1",
    "openBuySize": "20.1",
    "openSellNotional": "200.1",
    "openSellSize": "20.1",
    "pnl": "200.1",
    "quote": "-67992.60",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "value": "200.1"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].averageEntryPrice	string	Yes	
[*].base	string	Yes	
[*].breakEvenPrice	string	No	
[*].initialMargin	string	Yes	
[*].lastUpdateBaseDelta	string	Yes	
[*].lastUpdateId	integer	Yes	
[*].lastUpdateQuoteDelta	string	Yes	
[*].lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
[*].maintenanceMargin	string	Yes	
[*].markPrice	string	Yes	
[*].openBuyNotional	string	Yes	
[*].openBuySize	string	Yes	
[*].openSellNotional	string	Yes	
[*].openSellSize	string	Yes	
[*].pnl	string	Yes	
[*].quote	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].value	string	Yes	
#Get Realized PnL
GET /account/realized-pnl
Get the user's realized pnl

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 100
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "id": 1,
    "pairSymbol": "BTC_USDT",
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].id	integer	Yes	
[*].pairSymbol	string	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Rebates
GET /account/rebates
Get the user's rebates

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	
before	query	integer	No	
limit	query	integer	No	Default: 100
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "assetSymbol": "BTC",
    "id": 1,
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].assetSymbol	string	Yes	
[*].id	integer	Yes	
[*].subaccountId	integer	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].userId	integer	Yes	
#Get Referral Links
GET /account/referral-links
Get the user's referral links

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "createdAt": 1704067200000000,
    "deletedAt": 1704067200000000,
    "id": "abc123",
    "lastUsedAt": 1704067200000000,
    "slug": "abc123",
    "uses": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch
[*].deletedAt	integer	No	Time in microseconds since unix epoch
[*].id	string	Yes	
[*].lastUsedAt	integer	No	Time in microseconds since unix epoch
[*].slug	string	No	
[*].uses	integer	Yes	
#Create Referral Link
POST /account/referral-links
Create a referral link for the user

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
{
  "linkId": [
    1
  ]
}
Name	Type	Required	Description
object	Yes	
.linkId	array	Yes	
.linkId[*]	integer	-	
#Update Referral Link Slug
PUT /account/referral-links/{id}/slug
Update the slug for a referral link

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	string	Yes	
Request Body
// Example Request Body
{
  "slug": "abc123"
}
Name	Type	Required	Description
object	Yes	
.slug	string	Yes	
#Get Active Sessions
GET /account/sessions
Get the user's active sessions

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
{
  "currentSession": 1,
  "sessions": [
    {
      "createdAt": "abc123",
      "deletedAt": "abc123",
      "expiresAt": "abc123",
      "id": 1,
      "ipAddress": "abc123",
      "ipApproved": true,
      "ipInfo": {
        "location": {
          "city": "abc123",
          "country": "abc123",
          "latitude": 1.23,
          "longitude": 1.23,
          "postalCode": "abc123",
          "region": "abc123",
          "timezone": "abc123"
        },
        "privacy": {
          "hosting": true,
          "proxy": true,
          "relay": true,
          "service": "abc123",
          "tor": true,
          "vpn": true
        }
      },
      "lastMfaAt": "abc123",
      "lastUsedAt": "abc123",
      "maxExpiration": "abc123",
      "updatedAt": "abc123",
      "userAgent": "abc123",
      "userId": 1
    }
  ]
}
Name	Type	Required	Description
object	Yes	
.currentSession	integer	Yes	
.sessions	array	Yes	
.sessions[*]	object	-	
.sessions[*].createdAt	string	Yes	Format: date-time
.sessions[*].deletedAt	string	No	Format: date-time
.sessions[*].expiresAt	string	Yes	Format: date-time
.sessions[*].id	integer	Yes	
.sessions[*].ipAddress	string	Yes	
.sessions[*].ipApproved	boolean	Yes	
.sessions[*].ipInfo	object	Yes	
.sessions[*].ipInfo.location	object	Yes	
.sessions[*].ipInfo.location.city	string	No	
.sessions[*].ipInfo.location.country	string	No	
.sessions[*].ipInfo.location.latitude	number	No	
.sessions[*].ipInfo.location.longitude	number	No	
.sessions[*].ipInfo.location.postalCode	string	No	
.sessions[*].ipInfo.location.region	string	No	
.sessions[*].ipInfo.location.timezone	string	No	
.sessions[*].ipInfo.privacy	object	Yes	
.sessions[*].ipInfo.privacy.hosting	boolean	Yes	
.sessions[*].ipInfo.privacy.proxy	boolean	Yes	
.sessions[*].ipInfo.privacy.relay	boolean	Yes	
.sessions[*].ipInfo.privacy.service	string	No	
.sessions[*].ipInfo.privacy.tor	boolean	Yes	
.sessions[*].ipInfo.privacy.vpn	boolean	Yes	
.sessions[*].lastMfaAt	string	No	Format: date-time
.sessions[*].lastUsedAt	string	Yes	Format: date-time
.sessions[*].maxExpiration	string	No	Format: date-time
.sessions[*].updatedAt	string	Yes	Format: date-time
.sessions[*].userAgent	string	Yes	
.sessions[*].userId	integer	Yes	
#Delete Session
POST /account/sessions/delete
Delete a session for the user

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "sessionId": 1
}
Name	Type	Required	Description
object	Yes	
.sessionId	integer	Yes	
#Terminate All Sessions
POST /account/sessions/terminate-all
Terminate all sessions for the user

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
#Get User Settings
GET /account/settings
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
{
  "allowSequenceEmails": true,
  "autogenDepositAddresses": true,
  "confirmBeforePlaceOrder": true,
  "hideBalances": true,
  "language": "en",
  "marginUsageThreshold": 1.23,
  "notifyAnnouncements": true,
  "notifyCommissions": true,
  "notifyDeposits": true,
  "notifyMarginUsage": true,
  "notifyOrderFills": true,
  "notifyPushNotifications": true,
  "notifyRebates": true,
  "notifySendEmail": true,
  "notifyWithdrawals": true,
  "tickerTapeScroll": true,
  "updatesFlash": true
}
Name	Type	Required	Description
object	Yes	
.allowSequenceEmails	boolean	Yes	
.autogenDepositAddresses	boolean	Yes	
.confirmBeforePlaceOrder	boolean	Yes	
.hideBalances	boolean	Yes	
.language	string	No	Enum: "en", "zh", "vi", "uk", "es", "ru", "ar", "ur", "hi"
.marginUsageThreshold	number	Yes	
.notifyAnnouncements	boolean	Yes	
.notifyCommissions	boolean	Yes	
.notifyDeposits	boolean	Yes	
.notifyMarginUsage	boolean	Yes	
.notifyOrderFills	boolean	Yes	
.notifyPushNotifications	boolean	Yes	
.notifyRebates	boolean	Yes	
.notifySendEmail	boolean	Yes	
.notifyWithdrawals	boolean	Yes	
.tickerTapeScroll	boolean	Yes	
.updatesFlash	boolean	Yes	
#Get Price Alerts
GET /account/settings/price-alert
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
symbol	query	string	No	
Response Body
// Example Response Body
{
  "alertPrice": "1.23",
  "alertPriceType": "last",
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.alertPrice	string	Yes	
.alertPriceType	string	Yes	Enum: "last", "mark", "index"
.symbol	string	Yes	
#Set Price Alert
PUT /account/settings/price-alert
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
symbol	query	string	No	
Request Body
// Example Request Body
{
  "alertPrice": "1.23",
  "alertPriceType": "last",
  "alertType": "above"
}
Name	Type	Required	Description
object	Yes	
.alertPrice	string	Yes	
.alertPriceType	string	Yes	Enum: "last", "mark", "index"
.alertType	string	Yes	Enum: "above", "below"
#Delete Price Alert
DELETE /account/settings/price-alert
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
symbol	query	string	No	
#Update User Settings
POST /account/settings/update
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "allowSequenceEmails": true,
  "autogenDepositAddresses": true,
  "confirmBeforePlaceOrder": true,
  "hideBalances": true,
  "language": "en",
  "marginUsageThreshold": 1.23,
  "notifyAnnouncements": true,
  "notifyCommissions": true,
  "notifyDeposits": true,
  "notifyMarginUsage": true,
  "notifyOrderFills": true,
  "notifyPushNotifications": true,
  "notifyRebates": true,
  "notifySendEmail": true,
  "notifyWithdrawals": true,
  "tickerTapeScroll": true,
  "updatesFlash": true
}
Name	Type	Required	Description
object	Yes	
.allowSequenceEmails	boolean	No	
.autogenDepositAddresses	boolean	No	
.confirmBeforePlaceOrder	boolean	No	
.hideBalances	boolean	No	
.language	string	No	Enum: "en", "zh", "vi", "uk", "es", "ru", "ar", "ur", "hi"
.marginUsageThreshold	number	No	
.notifyAnnouncements	boolean	No	
.notifyCommissions	boolean	No	
.notifyDeposits	boolean	No	
.notifyMarginUsage	boolean	No	
.notifyOrderFills	boolean	No	
.notifyPushNotifications	boolean	No	
.notifyRebates	boolean	No	
.notifySendEmail	boolean	No	
.notifyWithdrawals	boolean	No	
.tickerTapeScroll	boolean	No	
.updatesFlash	boolean	No	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Create State Disclaimer Acknowledgement
POST /account/state-disclaimer/acknowledgements
Acknowledge a state-specific disclaimer

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "stateCode": "abc123"
}
Name	Type	Required	Description
object	Yes	
.stateCode	string	Yes	
Response Body
// Example Response Body
{
  "acknowledged": true
}
Name	Type	Required	Description
object	Yes	
.acknowledged	boolean	Yes	
#Get Transfers
GET /account/transfers
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "counterparty": 1,
    "id": 1,
    "subaccountId": 1,
    "symbol": "BTC",
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	Amount of asset transferred, negative if sent, positive if received.
[*].counterparty	integer	Yes	
[*].id	integer	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
#Unsubscribe from Reminder Emails
GET /account/unsubscribe
Unsubscribe from reminder emails using the link from an email

Parameters
Name	In	Type	Required	Description
linkId	query	string	Yes	
#Get Watchlist
GET /account/watchlist
Get a list of the pairs in your watchlist

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  "BTC_USDT"
]
Name	Type	Required	Description
array	Yes	
[*]	string	-	
#Add to Watchlist
POST /account/watchlist/add
Add a pair to the watchlist

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.symbol	string	Yes	
#Remove from Watchlist
POST /account/watchlist/remove
Remove a pair from your watchlise

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.symbol	string	Yes	
#Account Withdraw
POST /account/withdraw
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "addressId": 1,
  "amount": "20.1",
  "beneficiary": {
    "firstName": "abc123",
    "isSelf": true,
    "isVasp": true,
    "lastName": "abc123"
  },
  "subaccountId": 1,
  "symbol": "BTC"
}
Name	Type	Required	Description
object	Yes	
.addressId	integer	Yes	
.amount	string	Yes	
.beneficiary	object	No	
.beneficiary.firstName	string	No	
.beneficiary.isSelf	boolean	Yes	
.beneficiary.isVasp	boolean	No	
.beneficiary.lastName	string	No	
.subaccountId	integer	Yes	Default: 0
.symbol	string	Yes	
Response Body
// Example Response Body
1
Name	Type	Required	Description
integer	Yes	
#Account Withdraw With MFA
POST /account/withdraw/with-mfa
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "address": "abc123",
  "amount": "20.1",
  "beneficiary": {
    "firstName": "abc123",
    "isSelf": true,
    "isVasp": true,
    "lastName": "abc123"
  },
  "chain": "abc123",
  "isMoonpay": true,
  "subaccountId": 1,
  "symbol": "BTC"
}
Name	Type	Required	Description
object	Yes	
.address	string	Yes	
.amount	string	Yes	
.beneficiary	object	No	
.beneficiary.firstName	string	No	
.beneficiary.isSelf	boolean	Yes	
.beneficiary.isVasp	boolean	No	
.beneficiary.lastName	string	No	
.chain	string	Yes	
.isMoonpay	boolean	Yes	Default: false
.subaccountId	integer	Yes	Default: 0
.symbol	string	Yes	
Response Body
// Example Response Body
1
Name	Type	Required	Description
integer	Yes	
#List Withdrawal Addresses
GET /account/withdrawal/addresses
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "address": "abc123",
    "chain": "abc123",
    "confirmed": true,
    "createdAt": 1704067200000000,
    "hasBeneficiary": true,
    "id": 1,
    "label": "abc123",
    "updatedAt": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].address	string	Yes	
[*].chain	string	Yes	
[*].confirmed	boolean	Yes	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch
[*].hasBeneficiary	boolean	Yes	
[*].id	integer	Yes	
[*].label	string	Yes	
[*].updatedAt	integer	Yes	Time in microseconds since unix epoch
#Create Withdrawal Address
POST /account/withdrawal/addresses
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "address": "abc123",
  "chain": "abc123",
  "label": "abc123",
  "memo": 1
}
Name	Type	Required	Description
object	Yes	
.address	string	Yes	
.chain	string	Yes	
.label	string	Yes	
.memo	integer	No	
Response Body
// Example Response Body
1
Name	Type	Required	Description
integer	Yes	
#Confirm Withdrawal Address
POST /account/withdrawal/addresses/confirm
Request Body
// Example Request Body
{
  "code": "248df4b7-aa70-47b8-a036-33ac447e668d"
}
Name	Type	Required	Description
object	Yes	
.code	string	Yes	Format: uuid
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Resend Withdrawal Address Verification Email
POST /account/withdrawal/addresses/resend
Resend the verification email for an existing unconfirmed withdrawal address.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "id": 1
}
Name	Type	Required	Description
object	Yes	
.id	integer	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Get Withdrawal Address
GET /account/withdrawal/addresses/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Response Body
// Example Response Body
{
  "address": "abc123",
  "chain": "abc123",
  "confirmed": true,
  "createdAt": 1704067200000000,
  "hasBeneficiary": true,
  "id": 1,
  "label": "abc123",
  "updatedAt": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.address	string	Yes	
.chain	string	Yes	
.confirmed	boolean	Yes	
.createdAt	integer	Yes	Time in microseconds since unix epoch
.hasBeneficiary	boolean	Yes	
.id	integer	Yes	
.label	string	Yes	
.updatedAt	integer	Yes	Time in microseconds since unix epoch
#Update Withdrawal Address Label
PUT /account/withdrawal/addresses/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Request Body
// Example Request Body
{
  "label": "abc123"
}
Name	Type	Required	Description
object	Yes	
.label	string	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Delete Withdrawal Address
DELETE /account/withdrawal/addresses/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Get Withdrawal Address Beneficiary
GET /account/withdrawal/addresses/{id}/beneficiary
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Response Body
// Example Response Body
{
  "firstName": "abc123",
  "isSelf": true,
  "isVasp": true,
  "lastName": "abc123",
  "withdrawalAddressId": 1
}
Name	Type	Required	Description
object	Yes	
.firstName	string	No	
.isSelf	boolean	Yes	
.isVasp	boolean	No	
.lastName	string	No	
.withdrawalAddressId	integer	Yes	
#Update Withdrawal Address Beneficiary
PUT /account/withdrawal/addresses/{id}/beneficiary
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Request Body
// Example Request Body
{
  "firstName": "abc123",
  "isSelf": true,
  "isVasp": true,
  "lastName": "abc123"
}
Name	Type	Required	Description
object	Yes	
.firstName	string	No	
.isSelf	boolean	Yes	
.isVasp	boolean	No	
.lastName	string	No	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Get Withdrawals
GET /account/withdrawals
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	query	integer	No	Default: 0
before	query	integer	No	
limit	query	integer	No	Default: 50
Response Body
// Example Response Body
[
  {
    "amount": "20.1",
    "chain": "abc123",
    "confirmed": true,
    "id": 1,
    "price": "1.23",
    "subaccountId": 1,
    "symbol": "BTC",
    "time": 1704067200000000,
    "transactionHash": "abc123",
    "withdrawalAddress": "abc123"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].amount	string	Yes	
[*].chain	string	Yes	
[*].confirmed	boolean	Yes	
[*].id	integer	Yes	
[*].price	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].transactionHash	string	No	
[*].withdrawalAddress	string	Yes	
Subaccounts#
#Get Subaccounts
GET /subaccounts
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "createdAt": 1704067200000000,
    "futuresEnabled": true,
    "id": 1,
    "isLsp": true,
    "lspSettings": [
      {
        "maxAssignmentNotional": "200.1",
        "maxExposureNotional": "200.1",
        "symbol": "BTC_USDT"
      }
    ],
    "name": "abc123",
    "payFeesInArkm": true,
    "pinned": true
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch
[*].futuresEnabled	boolean	Yes	if true futures trading is enabled for the subaccount
[*].id	integer	Yes	
[*].isLsp	boolean	Yes	if true the subaccount is a liquidity provider
[*].lspSettings	array	Yes	
[*].lspSettings[*]	object	-	
[*].lspSettings[*].maxAssignmentNotional	string	Yes	
[*].lspSettings[*].maxExposureNotional	string	Yes	
[*].lspSettings[*].symbol	string	Yes	
[*].name	string	Yes	
[*].payFeesInArkm	boolean	Yes	if true and ARKM balance is sufficient fees are paid in ARKM with a discount. This is only available for USDT pairs
[*].pinned	boolean	Yes	
#Create Subaccount
POST /subaccounts
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "name": "abc123"
}
Name	Type	Required	Description
object	Yes	
.name	string	Yes	
Response Body
// Example Response Body
{
  "id": 1
}
Name	Type	Required	Description
object	Yes	
.id	integer	Yes	
#Update Subaccount
PUT /subaccounts
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "id": 1,
  "name": "abc123",
  "pinned": true
}
Name	Type	Required	Description
object	Yes	
.id	integer	Yes	
.name	string	No	
.pinned	boolean	No	
#Create Perpetual Transfer
POST /subaccounts/perp-transfer
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "fromSubaccountId": 1,
  "symbol": "BTC",
  "toSubaccountId": 1
}
Name	Type	Required	Description
object	Yes	
.fromSubaccountId	integer	Yes	
.symbol	string	Yes	
.toSubaccountId	integer	Yes	
Response Body
// Example Response Body
{
  "transferId": 1
}
Name	Type	Required	Description
object	Yes	
.transferId	integer	Yes	
#Create Transfer
POST /subaccounts/transfer
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "amount": "20.1",
  "fromSubaccountId": 1,
  "symbol": "BTC",
  "toSubaccountId": 1
}
Name	Type	Required	Description
object	Yes	
.amount	string	Yes	
.fromSubaccountId	integer	Yes	
.symbol	string	Yes	
.toSubaccountId	integer	Yes	
Response Body
// Example Response Body
{
  "transferId": 1
}
Name	Type	Required	Description
object	Yes	
.transferId	integer	Yes	
#Update Portfolio Settings
POST /subaccounts/update-settings
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "futuresEnabled": true,
  "isLsp": true,
  "lspSettingUpdates": [
    {
      "maxAssignmentNotional": "200.1",
      "maxExposureNotional": "200.1",
      "symbol": "BTC_USDT"
    }
  ],
  "payFeesInArkm": true,
  "subaccountId": 1
}
Name	Type	Required	Description
object	Yes	
.futuresEnabled	boolean	Yes	
.isLsp	boolean	Yes	
.lspSettingUpdates	array	Yes	
.lspSettingUpdates[*]	object	-	
.lspSettingUpdates[*].maxAssignmentNotional	string	Yes	
.lspSettingUpdates[*].maxExposureNotional	string	Yes	
.lspSettingUpdates[*].symbol	string	Yes	
.payFeesInArkm	boolean	Yes	if true and ARKM balance is sufficient fees are paid in ARKM with a discount. This is only available for USDT pairs
.subaccountId	integer	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Delete Subaccount
DELETE /subaccounts/{subaccountId}
Deletes the specified subaccount by ID

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
subaccountId	path	integer	Yes	
Other#
#Api Key List
GET /api-key
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "createdAt": 1704067200000000,
    "expiresAt": 1704067200000000,
    "id": 1,
    "ipWhitelist": [
      "192.168.1.0/24",
      "10.0.0.0/8"
    ],
    "name": "abc123",
    "read": true,
    "withdraw": false,
    "write": true
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch
[*].expiresAt	integer	No	Time in microseconds since unix epoch
[*].id	integer	Yes	
[*].ipWhitelist	array	Yes	
[*].ipWhitelist[*]	string	-	
[*].name	string	Yes	
[*].read	boolean	Yes	
[*].withdraw	boolean	Yes	
[*].write	boolean	Yes	
#Api Key Create
POST /api-key/create
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "expiresAt": 1704067200000000,
  "ipWhitelist": [
    "192.168.1.0/24",
    "10.0.0.0/8"
  ],
  "name": "My API Key",
  "read": true,
  "withdraw": false,
  "write": true
}
Name	Type	Required	Description
object	Yes	
.expiresAt	integer	Yes	Time in microseconds since unix epoch
.ipWhitelist	array	Yes	
.ipWhitelist[*]	string	-	
.name	string	Yes	
.read	boolean	Yes	
.withdraw	boolean	Yes	
.write	boolean	Yes	
Response Body
// Example Response Body
{
  "createdAt": 1704067200000000,
  "expiresAt": 1704067200000000,
  "id": 1,
  "ipWhitelist": [
    "192.168.1.0/24",
    "10.0.0.0/8"
  ],
  "key": "248df4b7-aa70-47b8-a036-33ac447e668d",
  "name": "abc123",
  "read": true,
  "secret": "Yr2IKeF2Ayg+gUg44bxYma1gmOrJiKjhahRd0MpoM0o=",
  "withdraw": false,
  "write": true
}
Name	Type	Required	Description
object	Yes	
.createdAt	integer	Yes	Time in microseconds since unix epoch
.expiresAt	integer	No	Time in microseconds since unix epoch
.id	integer	Yes	
.ipWhitelist	array	Yes	
.ipWhitelist[*]	string	-	
.key	string	Yes	Format: uuid
.name	string	Yes	
.read	boolean	Yes	
.secret	string	Yes	Base64 encoded 32 byte secret Format: base64
.withdraw	boolean	Yes	
.write	boolean	Yes	
#Fireblocks Api Key List
GET /api-key/fireblocks
List all Fireblocks Network Link API keys for the authenticated user.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Response Body
// Example Response Body
[
  {
    "createdAt": 1704067200000000,
    "id": 1,
    "name": "abc123"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].createdAt	integer	Yes	Time in microseconds since unix epoch Format: date-time
[*].id	integer	Yes	
[*].name	string	Yes	
#Create Fireblocks API Key
POST /api-key/fireblocks/create
Create a new Fireblocks Network Link API key.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Body
// Example Request Body
{
  "name": "My Fireblocks API Key"
}
Name	Type	Required	Description
object	Yes	
.name	string	Yes	
Response Body
// Example Response Body
{
  "createdAt": 1704067200000000,
  "id": 1,
  "key": "248df4b7-aa70-47b8-a036-33ac447e668d",
  "name": "abc123",
  "secret": "Yr2IKeF2Ayg+gUg44bxYma1gmOrJiKjhahRd0MpoM0o="
}
Name	Type	Required	Description
object	Yes	
.createdAt	integer	Yes	Time in microseconds since unix epoch Format: date-time
.id	integer	Yes	
.key	string	Yes	Format: uuid
.name	string	Yes	
.secret	string	Yes	Base64 encoded 32 byte secret Format: base64
#Update Fireblocks API Key
PUT /api-key/fireblocks/update/{id}
Update a Fireblocks Network Link API key.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Request Body
// Example Request Body
{
  "name": "My Updated Fireblocks API Key"
}
Name	Type	Required	Description
object	Yes	
.name	string	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Delete Fireblocks API Key
DELETE /api-key/fireblocks/{id}
Delete a Fireblocks Network Link API key.

Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
#Api Key Update
PUT /api-key/update/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
Request Body
// Example Request Body
{
  "ipWhitelist": [
    "192.168.1.0/24",
    "10.0.0.0/8"
  ],
  "name": "My Updated API Key",
  "read": true,
  "withdraw": false,
  "write": false
}
Name	Type	Required	Description
object	Yes	
.ipWhitelist	array	Yes	
.ipWhitelist[*]	string	-	
.name	string	Yes	
.read	boolean	Yes	
.withdraw	boolean	Yes	
.write	boolean	Yes	
Response Body
// Example Response Body
"abc123"
Name	Type	Required	Description
string	Yes	
#Api Key Delete
DELETE /api-key/{id}
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Parameters
Name	In	Type	Required	Description
id	path	integer	Yes	
#Authenticate
POST /authenticate
Parameters
Name	In	Type	Required	Description
tradeInToken	query	string	No	
redirectPath	query	string	No	
#Websocket API
The Arkham Exchange WebSocket API is a real-time API that provides access to the Arkham Exchange trading platform. It allows you to subscribe to real-time market data, order book updates, and account information.

It is recommended to use the WebSocket API for real-time data as it is more efficient than polling the REST API due to the lower latency, reduced number of tcp connections and lower bandwidth usage.

Each data type is exposed a stream that can be subscribed to on a connection. The connection is kept open and data is streamed to the client as it becomes available.

Connecting to the WebSocket API#
The WebSocket API is available at the following URL:

wss://arkm.com/ws
Subscribing to a Stream#
To subscribe to a stream, send a JSON formatted subscribe message on the connection. See below for details and examples of the format of the subscribe messages for each stream.

Subscribing to a stream that is already subscribed to will have no effect.

Unsubscribing from a Stream#
If you no longer wish to receive data from a stream, send a JSON message with an unsubscribe message on the connection. See below for details and examples of the format of the unsubscribe messages for each stream.

Snapshot Messages#
Some streams provide a snapshot message when you first subscribe to the stream. This message contains the current state of the data which can be used to initialise the client's state. After the snapshot message, the stream will send the same messages as if you had subscribed to the stream without the snapshot. For example, the L2 Order Book stream can provide a snapshot of the current order book when you first subscribe to the stream which can be used to construct a copy of the order book on the client side.

Execution Messages#
The websocket API provides the ability to create and manage orders on the exchange. This functionality is provided through the execute method on the WebSocket API.

Sending an execute message to the WebSocket API will not subscribe to any stream but will return an error or a response message similar to the REST API.

All execution messages require an authenicated websocket connection to be used, and an API key with sufficent permissions.

The confirmationId field can be used to correlate the response message with the request message.

Websocket Authentication#
Websocket authentication is done using the same API key and secret as the REST API. The API key should be included in the +""+Arkham-API-Key+""+ header of the initial HTTP request to the websocket endpoint.

The signature is calculated in the same way as for the REST API and should be included in the +""+Arkham-Signature+""+ header of the initial HTTP request to the websocket endpoint. The body of the request should be empty.

For example, to connect to the websocket API using wscat:

# First install wscat if you haven't already
npm install -g wscat

# Set the API_KEY and API_SECRET environment variables
API_KEY=<your-api-key>
API_SECRET=<your-api-secret>

BASE_URL=wss://arkm.com
METHOD="GET"
REQUEST_PATH="/ws"

# Set the expiry timestamp - in this case 5 minutes from now
EXPIRES=$(($(/bin/date +%s) + 300))000000

# Calculate the signature
HMAC_KEY=$(/bin/echo -n "$API_SECRET" | base64 -D | xxd -p -c 64)
SIGNATURE=$(/bin/echo -n "$API_KEY$EXPIRES$METHOD$REQUEST_PATH" | openssl dgst -sha256 -mac HMAC -macopt hexkey:$HMAC_KEY -binary | base64)


# Make the request
wscat \
	-H "Arkham-Api-Key: $API_KEY" \
	-H "Arkham-Expires: $EXPIRES" \
	-H "Arkham-Signature: $SIGNATURE" \
	--connect $BASE_URL$REQUEST_PATH \
	-x '{"args":{"channel":"order_statuses"},"method":"subscribe"}'
Rate Limits#
The WebSocket API has a rate limit of 5 connections per second per IP address and 10 connections per second per account. If you exceed these limits, you will receive a 429 error response on the HTTP request to the WebSocket endpoint.

Heartbeat Messages#
The WebSocket API will regularly send a ping control frame to ensure the connection is still active, if the client does not promptly respond with a pong frame the connection will be dropped. This functionality is generally handled by websocket client implementations, but may need to be manually configure based on the client library.

The client may also send a ping message to the server to check the connection is still active. The server will respond with a pong message on the "pong" channel.

For example, to send a ping message to the server using wscat:

wscat \
	-H "Arkham-Api-Key: $API_KEY" \
	-H "Arkham-Expires: $EXPIRES" \
	-H "Arkham-Signature: $SIGNATURE" \
	--connect $BASE_URL$REQUEST_PATH \
	-x '{"method":"ping"}'
{"channel":"pong"}
Confirmation Messages#
By default the websocket will not send any confirmations on reciept of subscription messages from the client, if you would like these you can attach a (non-empty) confirmationId string to the message and the api will respond with a message on the confirmations channel with the same confirmationId before any other messages. If the message fails validation, the error message in the response will include the confirmationId sent in the request.

Also every subsequent message for that subscription will include the same confirmationId field, allowing you to easily route messages to the correct handler.

#Websocket Streams
#Candlestick data
Channel Name
"candles"
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "candles",
    "params": {
      "duration": "1m",
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "candles"
.args.params	object	Yes	
.args.params.duration	string	No	Enum: "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d", "3d", "7d", "30d"
.args.params.symbol	string	Yes	
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "candles",
    "params": {
      "duration": "1m",
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "candles"
.args.params	object	Yes	
.args.params.duration	string	No	Enum: "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d", "3d", "7d", "30d"
.args.params.symbol	string	Yes	
Update Message
// Example Update Message
{
  "channel": "candles",
  "confirmationId": "abc123",
  "data": {
    "close": "1.23",
    "duration": 60000000,
    "high": "1.23",
    "low": "1.23",
    "open": "1.23",
    "quoteVolume": "200.1",
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "volume": "20.1"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "candles"
.confirmationId	string	No	
.data	object	Yes	
.data.close	string	Yes	
.data.duration	integer	Yes	Enum: 60000000, 180000000, 300000000, 900000000, 1800000000, 3600000000, 7200000000, 14400000000, 21600000000, 43200000000, 86400000000, 259200000000, 604800000000, 2592000000000
.data.high	string	Yes	
.data.low	string	Yes	
.data.open	string	Yes	
.data.quoteVolume	string	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
.data.volume	string	Yes	
#Ticker Updates
Channel Name
"ticker"
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "ticker",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "ticker"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "ticker",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "ticker"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Snapshot Message
// Example Snapshot Message
{
  "baseSymbol": "BTC",
  "fundingRate": "0.000733",
  "high24h": "100000.1",
  "indexCurrency": "USDT",
  "indexPrice": "100000.1",
  "low24h": "90000.1",
  "markPrice": "100000.1",
  "nextFundingRate": "0.000733",
  "nextFundingTime": 1731686400000000,
  "openInterest": "1.1",
  "openInterestUSD": "100000.1",
  "price": "100000.1",
  "price24hAgo": "90000.1",
  "productType": "spot",
  "quoteSymbol": "USDT",
  "quoteVolume24h": "100000.1",
  "symbol": "BTC_USDT",
  "usdVolume24h": "100000.1",
  "volume24h": "1.1"
}
Name	Type	Required	Description
object	Yes	
.baseSymbol	string	Yes	
.fundingRate	string	Yes	
.high24h	string	Yes	
.indexCurrency	string	Yes	
.indexPrice	string	Yes	
.low24h	string	Yes	
.markPrice	string	Yes	
.nextFundingRate	string	Yes	
.nextFundingTime	integer	Yes	Time in microseconds since unix epoch
.openInterest	string	Yes	
.openInterestUSD	string	Yes	
.price	string	Yes	
.price24hAgo	string	Yes	
.productType	string	Yes	Enum: "spot", "perpetual"
.quoteSymbol	string	Yes	
.quoteVolume24h	string	Yes	
.symbol	string	Yes	
.usdVolume24h	string	Yes	
.volume24h	string	Yes	
Update Message
// Example Update Message
{
  "channel": "ticker",
  "confirmationId": "abc123",
  "data": {
    "baseSymbol": "BTC",
    "fundingRate": "0.000733",
    "high24h": "100000.1",
    "indexCurrency": "USDT",
    "indexPrice": "100000.1",
    "low24h": "90000.1",
    "markPrice": "100000.1",
    "nextFundingRate": "0.000733",
    "nextFundingTime": 1731686400000000,
    "openInterest": "1.1",
    "openInterestUSD": "100000.1",
    "price": "100000.1",
    "price24hAgo": "90000.1",
    "productType": "spot",
    "quoteSymbol": "USDT",
    "quoteVolume24h": "100000.1",
    "symbol": "BTC_USDT",
    "usdVolume24h": "100000.1",
    "volume24h": "1.1"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "ticker"
.confirmationId	string	No	
.data	object	Yes	
.data.baseSymbol	string	Yes	
.data.fundingRate	string	Yes	
.data.high24h	string	Yes	
.data.indexCurrency	string	Yes	
.data.indexPrice	string	Yes	
.data.low24h	string	Yes	
.data.markPrice	string	Yes	
.data.nextFundingRate	string	Yes	
.data.nextFundingTime	integer	Yes	Time in microseconds since unix epoch
.data.openInterest	string	Yes	
.data.openInterestUSD	string	Yes	
.data.price	string	Yes	
.data.price24hAgo	string	Yes	
.data.productType	string	Yes	Enum: "spot", "perpetual"
.data.quoteSymbol	string	Yes	
.data.quoteVolume24h	string	Yes	
.data.symbol	string	Yes	
.data.usdVolume24h	string	Yes	
.data.volume24h	string	Yes	
#L2 order book
Channel Name
"l2_updates"
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "l2_updates",
    "params": {
      "group": "0.01",
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "l2_updates"
.args.params	object	Yes	
.args.params.group	string	No	Price group for aggregation, must be a multiple of 1, 10, 100 or 1000 of the tick size. Default is the tick size.
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "l2_updates",
    "params": {
      "group": "0.01",
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "l2_updates"
.args.params	object	Yes	
.args.params.group	string	No	Price group for aggregation, must be a multiple of 1, 10, 100 or 1000 of the tick size. Default is the tick size.
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Snapshot Message
// Example Snapshot Message
{
  "asks": [
    {
      "price": "1.23",
      "size": "20.1"
    }
  ],
  "bids": [
    {
      "price": "1.23",
      "size": "20.1"
    }
  ],
  "group": "0.01",
  "lastTime": 1731686400000000,
  "symbol": "BTC_USDT"
}
Name	Type	Required	Description
object	Yes	
.asks	array	Yes	
.asks[*]	object	-	
.asks[*].price	string	Yes	
.asks[*].size	string	Yes	
.bids	array	Yes	
.bids[*]	object	-	
.bids[*].price	string	Yes	
.bids[*].size	string	Yes	
.group	string	Yes	
.lastTime	integer	Yes	Time in microseconds since unix epoch
.symbol	string	Yes	
Update Message
// Example Update Message
{
  "channel": "l2_updates",
  "confirmationId": "abc123",
  "data": {
    "group": "1.23",
    "price": "1.23",
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "symbol": "BTC_USDT",
    "time": 1704067200000000
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "l2_updates"
.confirmationId	string	No	
.data	object	Yes	
.data.group	string	Yes	
.data.price	string	Yes	
.data.revisionId	integer	Yes	
.data.side	string	Yes	Enum: "buy", "sell"
.data.size	string	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
#L1 order book
Channel Name
"l1_updates"
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "l1_updates",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "l1_updates"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "l1_updates",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "l1_updates"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Snapshot Message
// Example Snapshot Message
{
  "askPrice": "1.23",
  "askSize": "20.1",
  "bidPrice": "1.23",
  "bidSize": "20.1",
  "revisionId": 1,
  "symbol": "BTC_USDT",
  "time": 1704067200000000
}
Name	Type	Required	Description
object	Yes	
.askPrice	string	No	
.askSize	string	No	
.bidPrice	string	No	
.bidSize	string	No	
.revisionId	integer	Yes	
.symbol	string	Yes	
.time	integer	Yes	Time in microseconds since unix epoch
Update Message
// Example Update Message
{
  "channel": "l1_updates",
  "confirmationId": "abc123",
  "data": {
    "askPrice": "1.23",
    "askSize": "20.1",
    "bidPrice": "1.23",
    "bidSize": "20.1",
    "revisionId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "l1_updates"
.confirmationId	string	No	
.data	object	Yes	
.data.askPrice	string	No	
.data.askSize	string	No	
.data.bidPrice	string	No	
.data.bidSize	string	No	
.data.revisionId	integer	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
#Trades
Channel Name
"trades"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "trades",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trades"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "trades",
    "params": {
      "snapshot": true,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trades"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.symbol	string	Yes	
Snapshot Message
// Example Snapshot Message
[
  {
    "price": "1.23",
    "revisionId": 1,
    "size": "20.1",
    "symbol": "BTC_USDT",
    "takerSide": "buy",
    "time": 1704067200000000
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].price	string	Yes	
[*].revisionId	integer	Yes	
[*].size	string	Yes	
[*].symbol	string	Yes	
[*].takerSide	string	Yes	Enum: "buy", "sell"
[*].time	integer	Yes	Time in microseconds since unix epoch
Update Message
// Example Update Message
{
  "channel": "trades",
  "confirmationId": "abc123",
  "data": {
    "price": "1.23",
    "revisionId": 1,
    "size": "20.1",
    "symbol": "BTC_USDT",
    "takerSide": "buy",
    "time": 1704067200000000
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "trades"
.confirmationId	string	No	
.data	object	Yes	
.data.price	string	Yes	
.data.revisionId	integer	Yes	
.data.size	string	Yes	
.data.symbol	string	Yes	
.data.takerSide	string	Yes	Enum: "buy", "sell"
.data.time	integer	Yes	Time in microseconds since unix epoch
#User Balances
Channel Name
"balances"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "balances",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "balances"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "balances",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "balances"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Snapshot Message
// Example Snapshot Message
[
  {
    "balance": "20.1",
    "balanceUSDT": "200.1",
    "free": "20.1",
    "freeUSDT": "200.1",
    "lastUpdateAmount": "20.1",
    "lastUpdateId": 1,
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "priceUSDT": "1.23",
    "subaccountId": 1,
    "symbol": "BTC"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].balance	string	Yes	
[*].balanceUSDT	string	Yes	
[*].free	string	Yes	
[*].freeUSDT	string	Yes	
[*].lastUpdateAmount	string	Yes	
[*].lastUpdateId	integer	Yes	
[*].lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
[*].priceUSDT	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
Update Message
// Example Update Message
{
  "channel": "balances",
  "confirmationId": "abc123",
  "data": {
    "balance": "20.1",
    "balanceUSDT": "200.1",
    "free": "20.1",
    "freeUSDT": "200.1",
    "lastUpdateAmount": "20.1",
    "lastUpdateId": 1,
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "priceUSDT": "1.23",
    "subaccountId": 1,
    "symbol": "BTC"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "balances"
.confirmationId	string	No	
.data	object	Yes	
.data.balance	string	Yes	
.data.balanceUSDT	string	Yes	
.data.free	string	Yes	
.data.freeUSDT	string	Yes	
.data.lastUpdateAmount	string	Yes	
.data.lastUpdateId	integer	Yes	
.data.lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
.data.lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
.data.priceUSDT	string	Yes	
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
#User Positions
Channel Name
"positions"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "positions",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "positions"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "positions",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "positions"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Snapshot Message
// Example Snapshot Message
[
  {
    "averageEntryPrice": "67992.60",
    "base": "1",
    "breakEvenPrice": "1.23",
    "initialMargin": "200.1",
    "lastUpdateBaseDelta": "20.1",
    "lastUpdateId": 1,
    "lastUpdateQuoteDelta": "200.1",
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "maintenanceMargin": "200.1",
    "markPrice": "1.23",
    "openBuyNotional": "200.1",
    "openBuySize": "20.1",
    "openSellNotional": "200.1",
    "openSellSize": "20.1",
    "pnl": "200.1",
    "quote": "-67992.60",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "value": "200.1"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].averageEntryPrice	string	Yes	
[*].base	string	Yes	
[*].breakEvenPrice	string	No	
[*].initialMargin	string	Yes	
[*].lastUpdateBaseDelta	string	Yes	
[*].lastUpdateId	integer	Yes	
[*].lastUpdateQuoteDelta	string	Yes	
[*].lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
[*].lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
[*].maintenanceMargin	string	Yes	
[*].markPrice	string	Yes	
[*].openBuyNotional	string	Yes	
[*].openBuySize	string	Yes	
[*].openSellNotional	string	Yes	
[*].openSellSize	string	Yes	
[*].pnl	string	Yes	
[*].quote	string	Yes	
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].value	string	Yes	
Update Message
// Example Update Message
{
  "channel": "positions",
  "confirmationId": "abc123",
  "data": {
    "averageEntryPrice": "67992.60",
    "base": "1",
    "breakEvenPrice": "1.23",
    "initialMargin": "200.1",
    "lastUpdateBaseDelta": "20.1",
    "lastUpdateId": 1,
    "lastUpdateQuoteDelta": "200.1",
    "lastUpdateReason": "orderFill",
    "lastUpdateTime": 1704067200000000,
    "maintenanceMargin": "200.1",
    "markPrice": "1.23",
    "openBuyNotional": "200.1",
    "openBuySize": "20.1",
    "openSellNotional": "200.1",
    "openSellSize": "20.1",
    "pnl": "200.1",
    "quote": "-67992.60",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "value": "200.1"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "positions"
.confirmationId	string	No	
.data	object	Yes	
.data.averageEntryPrice	string	Yes	
.data.base	string	Yes	
.data.breakEvenPrice	string	No	
.data.initialMargin	string	Yes	
.data.lastUpdateBaseDelta	string	Yes	
.data.lastUpdateId	integer	Yes	
.data.lastUpdateQuoteDelta	string	Yes	
.data.lastUpdateReason	string	Yes	Enum: "deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"
.data.lastUpdateTime	integer	Yes	Time in microseconds since unix epoch
.data.maintenanceMargin	string	Yes	
.data.markPrice	string	Yes	
.data.openBuyNotional	string	Yes	
.data.openBuySize	string	Yes	
.data.openSellNotional	string	Yes	
.data.openSellSize	string	Yes	
.data.pnl	string	Yes	
.data.quote	string	Yes	
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
.data.value	string	Yes	
#User Order Status
Channel Name
"order_statuses"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "order_statuses",
    "params": {
      "snapshot": true,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "order_statuses"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "order_statuses",
    "params": {
      "snapshot": true,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "order_statuses"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.subaccountId	integer	No	Default: 0
Snapshot Message
// Example Snapshot Message
[
  {
    "arkmFeePaid": "20.1",
    "avgPrice": "1.23",
    "brokerId": 1,
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "creditFeePaid": "200.1",
    "executedNotional": "200.1",
    "executedSize": "20.1",
    "lastArkmFee": "0.01",
    "lastCreditFee": "0.01",
    "lastMarginBonusFee": "0.01",
    "lastPrice": "1.5",
    "lastQuoteFee": "0.01",
    "lastSize": "1000",
    "lastTime": 1704067200000000,
    "marginBonusFeePaid": "200.1",
    "orderId": 1,
    "postOnly": true,
    "price": "1.23",
    "quoteFeePaid": "200.1",
    "reduceOnly": true,
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "status": "new",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "type": "limitGtc",
    "userId": 1
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
[*].avgPrice	string	Yes	Average price filled so far in the order
[*].brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
[*].clientOrderId	string	No	
[*].creditFeePaid	string	Yes	Total fee paid via credits so far in the order
[*].executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
[*].executedSize	string	Yes	Total quantity filled so far in the order
[*].lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
[*].lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
[*].lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
[*].lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
[*].lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
[*].lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
[*].lastTime	integer	Yes	Time of the last status update on the order
[*].marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
[*].orderId	integer	Yes	
[*].postOnly	boolean	Yes	If true the order is post-only
[*].price	string	Yes	The original price of the order
[*].quoteFeePaid	string	Yes	Total quote fee paid so far in the order
[*].reduceOnly	boolean	Yes	If true the order is reduce-only
[*].revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	The original size of the order
[*].status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
[*].userId	integer	Yes	
Update Message
// Example Update Message
{
  "channel": "order_statuses",
  "confirmationId": "abc123",
  "data": {
    "arkmFeePaid": "20.1",
    "avgPrice": "1.23",
    "brokerId": 1,
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "creditFeePaid": "200.1",
    "executedNotional": "200.1",
    "executedSize": "20.1",
    "lastArkmFee": "0.01",
    "lastCreditFee": "0.01",
    "lastMarginBonusFee": "0.01",
    "lastPrice": "1.5",
    "lastQuoteFee": "0.01",
    "lastSize": "1000",
    "lastTime": 1704067200000000,
    "marginBonusFeePaid": "200.1",
    "orderId": 1,
    "postOnly": true,
    "price": "1.23",
    "quoteFeePaid": "200.1",
    "reduceOnly": true,
    "revisionId": 1,
    "side": "buy",
    "size": "20.1",
    "status": "new",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "type": "limitGtc",
    "userId": 1
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "order_statuses"
.confirmationId	string	No	
.data	object	Yes	
.data.arkmFeePaid	string	Yes	Total ARKM fee paid so far in the order
.data.avgPrice	string	Yes	Average price filled so far in the order
.data.brokerId	integer	No	The ID of the broker used to create this order. If unset or 0, this will be omitted from the response.
.data.clientOrderId	string	No	
.data.creditFeePaid	string	Yes	Total fee paid via credits so far in the order
.data.executedNotional	string	Yes	Total notional value filled so far in the order, 0 if no fills
.data.executedSize	string	Yes	Total quantity filled so far in the order
.data.lastArkmFee	string	Yes	ARKM fee paid for the last trade, only present on taker and maker statuses
.data.lastCreditFee	string	Yes	Credit fee paid for the last trade, only present on taker and maker statuses
.data.lastMarginBonusFee	string	Yes	Margin bonus fee paid for the last trade, only present on taker and maker statuses
.data.lastPrice	string	Yes	Price of the last trade, only present on taker and maker statuses
.data.lastQuoteFee	string	Yes	Quote fee paid for the last trade, only present on taker and maker statuses
.data.lastSize	string	Yes	Size of the last trade, only present on taker and maker statuses
.data.lastTime	integer	Yes	Time of the last status update on the order
.data.marginBonusFeePaid	string	Yes	Total fee paid via margin bonus so far in the order
.data.orderId	integer	Yes	
.data.postOnly	boolean	Yes	If true the order is post-only
.data.price	string	Yes	The original price of the order
.data.quoteFeePaid	string	Yes	Total quote fee paid so far in the order
.data.reduceOnly	boolean	Yes	If true the order is reduce-only
.data.revisionId	integer	Yes	An identifier for the order's current state, unique to the pair
.data.side	string	Yes	Enum: "buy", "sell"
.data.size	string	Yes	The original size of the order
.data.status	string	Yes	Enum: "new", "taker", "booked", "maker", "cancelled", "closed"
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
.data.triggerOrderId	integer	No	The ID of the trigger order that created this order, if any
.data.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
.data.userId	integer	Yes	
#User Margin
Channel Name
"margin"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "margin",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "margin"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "margin",
    "params": {
      "snapshot": true,
      "snapshotInterval": 1,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "margin"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.snapshotInterval	integer	No	Interval in seconds for getting snapshot data, set to regularly get refreshed snapshot values
.args.params.subaccountId	integer	No	Default: 0
Snapshot Message
// Example Snapshot Message
{
  "available": "5000",
  "bonus": "100",
  "initial": "1000",
  "liquidation": "400",
  "locked": "1000",
  "maintenance": "600",
  "pnl": "100",
  "subaccountId": 1,
  "total": "6000",
  "totalAssetValue": "1.0"
}
Name	Type	Required	Description
object	Yes	
.available	string	Yes	Total margin available for opening new positions
.bonus	string	Yes	Total margin bonus
.initial	string	Yes	Initial margin required to open a position
.liquidation	string	Yes	Amount of Margin required to prevent portfolio liquidations
.locked	string	Yes	Total margin locked due to open positions and open orders
.maintenance	string	Yes	Amount of Margin required to prevent partial liquidations
.pnl	string	Yes	Total unrealized PnL
.subaccountId	integer	Yes	
.total	string	Yes	Total margin in the account, includes unrealized PnL
.totalAssetValue	string	Yes	Total value of all assets in the account in USDT
Update Message
// Example Update Message
{
  "channel": "margin",
  "confirmationId": "abc123",
  "data": {
    "available": "5000",
    "bonus": "100",
    "initial": "1000",
    "liquidation": "400",
    "locked": "1000",
    "maintenance": "600",
    "pnl": "100",
    "subaccountId": 1,
    "total": "6000",
    "totalAssetValue": "1.0"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "margin"
.confirmationId	string	No	
.data	object	Yes	
.data.available	string	Yes	Total margin available for opening new positions
.data.bonus	string	Yes	Total margin bonus
.data.initial	string	Yes	Initial margin required to open a position
.data.liquidation	string	Yes	Amount of Margin required to prevent portfolio liquidations
.data.locked	string	Yes	Total margin locked due to open positions and open orders
.data.maintenance	string	Yes	Amount of Margin required to prevent partial liquidations
.data.pnl	string	Yes	Total unrealized PnL
.data.subaccountId	integer	Yes	
.data.total	string	Yes	Total margin in the account, includes unrealized PnL
.data.totalAssetValue	string	Yes	Total value of all assets in the account in USDT
#User Trigger Orders
Channel Name
"trigger_orders"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "trigger_orders",
    "params": {
      "snapshot": true,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trigger_orders"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "trigger_orders",
    "params": {
      "snapshot": true,
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trigger_orders"
.args.params	object	Yes	
.args.params.snapshot	boolean	No	Default: false
.args.params.subaccountId	integer	No	Default: 0
Snapshot Message
// Example Snapshot Message
[
  {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "postOnly": true,
    "price": "1.23",
    "reduceOnly": true,
    "side": "buy",
    "size": "20.1",
    "status": "staged",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "triggerPrice": "1.23",
    "triggerPriceType": "last",
    "triggerType": "takeProfit",
    "type": "limitGtc"
  }
]
Name	Type	Required	Description
array	Yes	
[*]	object	-	
[*].clientOrderId	string	Yes	
[*].postOnly	boolean	Yes	
[*].price	string	Yes	
[*].reduceOnly	boolean	Yes	
[*].side	string	Yes	Enum: "buy", "sell"
[*].size	string	Yes	
[*].status	string	Yes	Enum: "staged", "triggered", "cancelled"
[*].subaccountId	integer	Yes	
[*].symbol	string	Yes	
[*].time	integer	Yes	Time in microseconds since unix epoch
[*].triggerOrderId	integer	Yes	
[*].triggerPrice	string	Yes	
[*].triggerPriceType	string	Yes	Enum: "last", "mark", "index"
[*].triggerType	string	Yes	Enum: "takeProfit", "stopLoss"
[*].type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Update Message
// Example Update Message
{
  "channel": "trigger_orders",
  "confirmationId": "abc123",
  "data": {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "postOnly": true,
    "price": "1.23",
    "reduceOnly": true,
    "side": "buy",
    "size": "20.1",
    "status": "staged",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "triggerOrderId": 1,
    "triggerPrice": "1.23",
    "triggerPriceType": "last",
    "triggerType": "takeProfit",
    "type": "limitGtc"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "trigger_orders"
.confirmationId	string	No	
.data	object	Yes	
.data.clientOrderId	string	Yes	
.data.postOnly	boolean	Yes	
.data.price	string	Yes	
.data.reduceOnly	boolean	Yes	
.data.side	string	Yes	Enum: "buy", "sell"
.data.size	string	Yes	
.data.status	string	Yes	Enum: "staged", "triggered", "cancelled"
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
.data.triggerOrderId	integer	Yes	
.data.triggerPrice	string	Yes	
.data.triggerPriceType	string	Yes	Enum: "last", "mark", "index"
.data.triggerType	string	Yes	Enum: "takeProfit", "stopLoss"
.data.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#User LSP Assignments
Channel Name
"lsp_assignments"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Subcribe Message
// Example Subcribe Message
{
  "method": "subscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "lsp_assignments",
    "params": {
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "subscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "lsp_assignments"
.args.params	object	Yes	
.args.params.subaccountId	integer	No	Default: 0
Unsubscribe Message
// Example Unsubscribe Message
{
  "method": "unsubscribe",
  "confirmationId": "abc123",
  "args": {
    "channel": "lsp_assignments",
    "params": {
      "subaccountId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "unsubscribe"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "lsp_assignments"
.args.params	object	Yes	
.args.params.subaccountId	integer	No	Default: 0
Update Message
// Example Update Message
{
  "channel": "lsp_assignments",
  "confirmationId": "abc123",
  "data": {
    "base": "20.1",
    "id": 1,
    "pairSymbol": "BTC_USDT",
    "price": "1.23",
    "quote": "200.1",
    "subaccountId": 1,
    "time": 1704067200000000,
    "userId": 1
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "lsp_assignments"
.confirmationId	string	No	
.data	object	Yes	
.data.base	string	Yes	
.data.id	integer	Yes	
.data.pairSymbol	string	Yes	
.data.price	string	Yes	
.data.quote	string	Yes	
.data.subaccountId	integer	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
.data.userId	integer	Yes	
#Confirmation Messages
Confimation Message
// Example Confimation Message
{
  "channel": "confirmations",
  "confirmationId": "abc123"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "confirmations"
.confirmationId	string	No	
#Websocket Requests
#Place a new order
Channel Name
"orders/new"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "orders/new",
  "confirmationId": "abc123",
  "args": {
    "channel": "orders/new",
    "params": {
      "brokerId": 1,
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "postOnly": false,
      "price": "1.23",
      "reduceOnly": false,
      "side": "buy",
      "size": "20.1",
      "subaccountId": 1,
      "symbol": "BTC_USDT",
      "type": "limitGtc"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "orders/new"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "orders/new"
.args.params	object	Yes	
.args.params.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.args.params.clientOrderId	string	No	
.args.params.postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.args.params.price	string	No	limit price, 0 for market orders
.args.params.reduceOnly	boolean	No	if true, the order will only reduce the position size.
.args.params.side	string	Yes	Enum: "buy", "sell"
.args.params.size	string	Yes	
.args.params.subaccountId	integer	No	Default: 0
.args.params.symbol	string	Yes	
.args.params.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Message
// Example Response Message
{
  "channel": "orders/new",
  "confirmationId": "abc123",
  "data": {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "orderId": 1,
    "price": "1.23",
    "side": "buy",
    "size": "20.1",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "time": 1704067200000000,
    "type": "limitGtc"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "orders/new"
.confirmationId	string	No	
.data	object	Yes	
.data.clientOrderId	string	No	
.data.orderId	integer	Yes	
.data.price	string	Yes	
.data.side	string	Yes	Enum: "buy", "sell"
.data.size	string	Yes	
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
.data.time	integer	Yes	Time in microseconds since unix epoch
.data.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Cancel an order
Channel Name
"orders/cancel"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "orders/cancel",
  "confirmationId": "abc123",
  "args": {
    "channel": "orders/cancel",
    "params": {
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "orderId": 1,
      "subaccountId": 1,
      "timeToCancel": 1704067200000000
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "orders/cancel"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "orders/cancel"
.args.params	object	Yes	
.args.params.clientOrderId	string	No	client order ID to cancel, required if orderId is not provided
.args.params.orderId	integer	No	order ID to cancel, required if clientOrderId is not provided
.args.params.subaccountId	integer	No	Default: 0
.args.params.timeToCancel	integer	No	Time to cancel the order, 0 for immediate. Granularity is 1 second. Default: 0
Response Message
// Example Response Message
{
  "channel": "orders/cancel",
  "confirmationId": "abc123",
  "data": {
    "orderId": 1
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "orders/cancel"
.confirmationId	string	No	
.data	object	Yes	
.data.orderId	integer	Yes	
#Cancel all orders
Channel Name
"orders/cancel/all"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "orders/cancel/all",
  "confirmationId": "abc123",
  "args": {
    "channel": "orders/cancel/all",
    "params": {
      "subaccountId": 1,
      "timeToCancel": 1704067200000000
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "orders/cancel/all"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "orders/cancel/all"
.args.params	object	Yes	
.args.params.subaccountId	integer	Yes	Default: 0
.args.params.timeToCancel	integer	Yes	Time to cancel all orders, 0 for immediate. Granularity is 1 second. Use this to set a dead man's switch. Default: 0
Response Message
// Example Response Message
{
  "channel": "orders/cancel/all",
  "confirmationId": "abc123",
  "data": {}
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "orders/cancel/all"
.confirmationId	string	No	
.data	object	Yes	
#Place a new trigger order
Channel Name
"trigger_orders/new"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "trigger_orders/new",
  "confirmationId": "abc123",
  "args": {
    "channel": "trigger_orders/new",
    "params": {
      "brokerId": 1,
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "postOnly": false,
      "price": "1.23",
      "reduceOnly": false,
      "side": "buy",
      "size": "20.1",
      "subaccountId": 1,
      "symbol": "BTC_USDT",
      "triggerPrice": "1.23",
      "triggerPriceType": "last",
      "triggerType": "takeProfit",
      "type": "limitGtc"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "trigger_orders/new"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trigger_orders/new"
.args.params	object	Yes	
.args.params.brokerId	integer	No	The ID of the broker used to create this order Default: 0
.args.params.clientOrderId	string	No	
.args.params.postOnly	boolean	No	if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders.
.args.params.price	string	No	limit price, 0 for market orders
.args.params.reduceOnly	boolean	No	if true, the order will only reduce the position size.
.args.params.side	string	Yes	Enum: "buy", "sell"
.args.params.size	string	Yes	
.args.params.subaccountId	integer	No	Default: 0
.args.params.symbol	string	Yes	
.args.params.triggerPrice	string	Yes	
.args.params.triggerPriceType	string	Yes	Enum: "last", "mark", "index"
.args.params.triggerType	string	Yes	Enum: "takeProfit", "stopLoss"
.args.params.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
Response Message
// Example Response Message
{
  "channel": "trigger_orders/new",
  "confirmationId": "abc123",
  "data": {
    "price": "1.23",
    "side": "buy",
    "size": "20.1",
    "symbol": "BTC_USDT",
    "triggerOrderId": 1,
    "type": "limitGtc"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "trigger_orders/new"
.confirmationId	string	No	
.data	object	Yes	
.data.price	string	Yes	
.data.side	string	Yes	Enum: "buy", "sell"
.data.size	string	Yes	
.data.symbol	string	Yes	
.data.triggerOrderId	integer	Yes	
.data.type	string	Yes	Enum: "limitGtc", "limitIoc", "limitFok", "market"
#Cancel a trigger order
Channel Name
"trigger_orders/cancel"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "trigger_orders/cancel",
  "confirmationId": "abc123",
  "args": {
    "channel": "trigger_orders/cancel",
    "params": {
      "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
      "subaccountId": 1,
      "symbol": "BTC_USDT",
      "triggerOrderId": 1
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "trigger_orders/cancel"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trigger_orders/cancel"
.args.params	object	Yes	
.args.params.clientOrderId	string	No	
.args.params.subaccountId	integer	No	Default: 0
.args.params.symbol	string	Yes	
.args.params.triggerOrderId	integer	No	
.args.params.triggerPriceType		No	
Response Message
// Example Response Message
{
  "channel": "trigger_orders/cancel",
  "confirmationId": "abc123",
  "data": {
    "clientOrderId": "e895221c-8c3c-41db-a911-6b9f4ec4c2e0",
    "subaccountId": 1,
    "symbol": "BTC_USDT",
    "triggerOrderId": 1
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "trigger_orders/cancel"
.confirmationId	string	No	
.data	object	Yes	
.data.clientOrderId	string	No	
.data.subaccountId	integer	No	Default: 0
.data.symbol	string	Yes	
.data.triggerOrderId	integer	No	
.data.triggerPriceType		No	
#Cancel all trigger orders
Channel Name
"trigger_orders/cancel/all"
Security
This endpoint requires API Key authentication
This enpoint requires a HMAC signed request
Request Message
// Example Request Message
{
  "method": "trigger_orders/cancel/all",
  "confirmationId": "abc123",
  "args": {
    "channel": "trigger_orders/cancel/all",
    "params": {
      "subaccountId": 1,
      "symbol": "BTC_USDT"
    }
  }
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "trigger_orders/cancel/all"
.confirmationId	string	No	
.args	object	Yes	
.args.channel	string	Yes	Value: "trigger_orders/cancel/all"
.args.params	object	Yes	
.args.params.subaccountId	integer	Yes	
.args.params.symbol	string	Yes	
.args.params.triggerPriceType		No	
Response Message
// Example Response Message
{
  "channel": "trigger_orders/cancel/all",
  "confirmationId": "abc123",
  "data": {
    "subaccountId": 1,
    "symbol": "BTC_USDT"
  }
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "trigger_orders/cancel/all"
.confirmationId	string	No	
.data	object	Yes	
.data.subaccountId	integer	Yes	
.data.symbol	string	Yes	
.data.triggerPriceType		No	
Errors Responses#
Internal Error
// Example Internal Error
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 0,
  "id": 10000,
  "name": "InternalError",
  "message": "internal error"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Bad Request
// Example Bad Request
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 1,
  "id": 10001,
  "name": "BadRequest",
  "message": "bad request: invalid snapshot interval: -2"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Unauthorized
// Example Unauthorized
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 2,
  "id": 10002,
  "name": "Unauthorized",
  "message": "unauthorized"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Invalid Symbol
// Example Invalid Symbol
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 3,
  "id": 10003,
  "name": "InvalidSymbol",
  "message": "invalid symbol: abc123"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Symbol Required
// Example Symbol Required
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 4,
  "id": 10004,
  "name": "SymbolRequired",
  "message": "symbol is required"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Invalid Method
// Example Invalid Method
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 5,
  "id": 20001,
  "name": "InvalidMethod",
  "message": "invalid method: abc123"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Method Required
// Example Method Required
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 6,
  "id": 20002,
  "name": "MethodRequired",
  "message": "method is required"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Invalid Channel
// Example Invalid Channel
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 7,
  "id": 20003,
  "name": "InvalidChannel",
  "message": "invalid channel: abc123"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Channel Required
// Example Channel Required
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 8,
  "id": 20004,
  "name": "ChannelRequired",
  "message": "channel is required"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Invalid Group
// Example Invalid Group
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 10,
  "id": 20005,
  "name": "InvalidGroup",
  "message": "group 123 does not exist"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Rate Limit Exceeded
// Example Rate Limit Exceeded
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 11,
  "id": 10005,
  "name": "RateLimitExceeded",
  "message": "open order limit exceeded: 100"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
Forbidden
// Example Forbidden
{
  "channel": "errors",
  "confirmationId": "abc123",
  "code": 13,
  "id": 10006,
  "name": "Forbidden",
  "message": "forbidden: write permission required"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "errors"
.confirmationId	string	No	
.code	integer	Yes	
.id	integer	Yes	
.name	string	Yes	
.message	string	Yes	
#Ping/Pong Messages
Ping Message
// Example Ping Message
{
  "method": "ping",
  "confirmationId": "abc123"
}
Name	Type	Required	Description
object	Yes	
.method	string	Yes	Value: "ping"
.confirmationId	string	No	
Pong Response
// Example Pong Response
{
  "channel": "pong",
  "confirmationId": "abc123"
}
Name	Type	Required	Description
object	Yes	
.channel	string	Yes	Value: "pong"
.confirmationId	string	No	