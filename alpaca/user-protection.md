# User Protection

Source: https://docs.alpaca.markets/docs/user-protection

---

## Introduction
- Welcome- About Alpaca- Alpaca API Platform- Authentication- SDKs and Tools- Additional Resources
## BROKER API
- About Broker API- Getting Started with Broker API- Credentials Management- Use Cases- Integration Setup with Alpaca- Broker API FAQs- Mandatory Corporate Actions- Voluntary Corporate Actions- FDIC Sweep Program- Instant Funding- Fully Paid Securities Lending- 24/5 Trading- OmniSub- Fixed Income- Customer Account Opening- Accounts Statuses- International Accounts- Domestic (USA) Accounts- Data Validations- IRA Accounts Overview- Crypto Trading- Crypto Wallets API- Funding Accounts- Journals API- Funding Wallets- ACH Funding- Instant Funding- Trading- Portfolio Rebalancing- SSE Events- Account Status Events for KYCaaS- Daily Processes and Reconcilations- Banking Holiday Funding Processes- Statements and Confirms- Local Currency Trading (LCT)- Example Trading App (Ribbit)- Options Trading Overview- Fixed Income- Tokenization Guide for Issuer- Tokenization Guide for Authorized Participant- Custodial accounts
## TRADING API
- About Trading API- Getting Started with Trading API- Working with /account- Working with /assets- Working with /orders- Working with /positions- Paper Trading- Trading Account- Crypto Spot Trading- Crypto Orders- Crypto Pricing Data- Crypto Spot Trading Fees- Options Trading- Options Orders- Options Level 3 Trading- Non-Trade Activities for Option Events- Account Activities- Fractional Trading- Margin and Short Selling- Placing Orders- DMA Gateway / Advanced Order Types- User Protection- Websocket Streaming- Trading API FAQs- Position Average Entry Price Calculation- Regulatory Fees- Alpaca&#x27;s MCP Server
## Market Data API
- About Market Data API- Getting Started with Market Data API- Historical API- Historical Stock Data- Historical Crypto Data- Historical Option Data- Historical News Data- WebSocket Stream- Real-time Stock Data- Real-time Crypto Data- Real-time News- Real-time Option Data- Market Data FAQ
## Connect API
- About Connect API- Registering Your App- Using OAuth2 and Trading API
## FIX API
- About FIX API- FIX Specification
# User Protection
We have enabled several types of protections to enhance your trading experience.

- Pattern Day Trader (PDT) Protection
- Day Trade Margin Call (DTMC) Protection
- Preventing Wash Trades
- Limit order price away sanity check

Please note that these do not apply to crypto trading as cryptocurrencies are not marginable. Pattern Day Trading rule does not apply to crypto trading either. Preventing Wash Trades does apply to crypto trading.

# Pattern Day Trader (PDT) Protection at Alpaca

In order to prevent Alpaca Brokerage Account customers from unintentionally being designated as a Pattern Day Trader (PDT), the Alpaca Trading platform checks the PDT rule condition every time an order is submitted from a customer. If the order could potentially result in the account being flagged as a PDT, the order is rejected, and API returns error with HTTP status code 403 (Forbidden).

## The Rule

A day trade is defined as a round-trip pair of trades within the same day (including extended hours). This is best described as an initial or opening transaction that is subsequently closed later in the same calendar day. For long positions, this would consist of a buy and then sell. For short positions, selling a security short and buying it back to cover the short position on the same day would also be considered a day trade.
An account is designated as a Pattern Day Trader if it makes four (4) or more day trades within five (5) business days, and the number of day trades represents more than six percent (6%) of the total trades within the same five (5) business days window. Day trades less than this criteria will not flag the account for PDT.
Cryptocurrency trading is not subject to the PDT rule. As a result, crypto orders are not evaluated by PDT protection logic and round-trip crypto trades on the same day do not contribute to the day trade count.
Day trades are counted regardless of share quantity or frequency throughout the day. Here are some FINRA-provided examples:
Example A:
09:30 Buy 250 ABC

09:31 Buy 250 ABC

13:00 Sell 500 ABC

The customer has executed one day trade.
Example B:

09:30 Buy 100 ABC

09:31 Sell 100 ABC

09:32 Buy 100 ABC

13:00 Sell 100 ABC

The customer has executed two day trades.
Example C:

09:30 Buy 500 ABC

13:00 Sell 100 ABC

13:01 Sell 100 ABC

13:03 Sell 300 ABC

The customer has executed one day trade.
Example D:

09:30 Buy 250 ABC

09:31 Buy 300 ABC

13:01 Buy 100 ABC

13:02 Sell 150 ABC

13:03 Sell 175 ABC

The customer has executed one day trade.
Example E:

09:30 Buy 199 ABC

09:31 Buy 142 ABC

13:00 Sell 1 ABC

13:01 Buy 45 ABC

13:02 Sell 100 ABC

13:03 Sell 200 ABC

The customer has executed two day trades.
Example F:

09:30 Buy 200 ABC

09:30 Buy 100 XYZ

13:00 Sell 100 ABC

13:00 Sell 100 XYZ
The customer has executed two day trades.
For further information, please visit Regulatory Notice 21-13 | FINRA.org 

## Alpaca’s Order Rejection

Alpaca Trading platform monitors the number of day trades for the account for the past 5 business days and rejects a newly submitted orders on exit of a position if it could potentially result in the account being flagged for PDT. This protection triggers only when the previous day’s closing account equity is less than $25,000 at the time of order submission.
In addition to the filled orders, the system also takes into consideration pending orders in the account. In this case, regardless of the order of pending orders, a pair of buy and sell orders is counted as a potential day trade. This is because orders that are active (pending) in the marketplace may fill in random orders. Therefore, even if your sell limit order is submitted first (without being filled yet) and another buy order on the same security is submitted later, this buy order will be blocked if your account already has 3 day trades in the last 5 business days.

## Pattern Day Trader (PDT) Restriction at Alpaca

If an account falls below the required $25,000 securities equity at the end of the trading day, it will be flagged for not meeting the Pattern Day Trader (PDT) requirements. When this happens, the account will be restricted from placing any new day trades on the following business day. Day trading will remain blocked until either:
A PDT Restriction lift is granted, or
A One-Time PDT Removal is granted, or
The account equity once again meets the $25,000 minimum requirement by the end of the trading day.
To request a PDT Restriction lift or One-Time PDT Removal* in order to place a day trade, please contact our support team at [email&#160;protected].
*Note: The One-Time PDT Removal applies for the life of all accounts at Alpaca. By requesting this, you are removing the PDT flag from your account and agree not to engage in future pattern day trading.
Please also note that once the restriction is lifted and you place a day trade, your account will be limited to liquidation-only activity for 90 days, or until the $25,000 equity requirement is met.

## Paper Trading

The same protection triggers in your paper trading account. It is advised to test your algorithm with the realistic balance amount you would manage when going live, to make sure your assumption works under this PDT protection as well.

For more details of Pattern Day Trader rule, please visit the FINRA website.

# Day Trade Margin Call (DTMC) Protection at Alpaca

In order to prevent Alpaca Brokerage Account customers from unintentionally receiving day trading margin calls, Alpaca implements two forms of DTMC protection.

## The Rule

Day traders are required to have a minimum of $25,000 OR 25% of the total market value of securities (whichever is higher) maintained in their account.
The buying power of a pattern day trader is 4x the excess of the maintenance margin from the closing of the previous day. If you exceed this amount, you will receive a day trading margin call.

## How Alpaca’s DTMC Protection Settings Work

Users only receive day trading buying power when marked as a pattern day trader. If the user is designated a pattern day trader, the account.multiplier is equal to 4.
Daytrading buying power cannot increase beyond its start of day value. In other words, closing an overnight position will not add to your daytrading buying power.
The following scenarios and protections are applicable only for accounts that are designated as pattern day traders. Please check your Account API result for the multiplier field.
Every trading day, you start with the new `daytrading_buying_power`. This beginning value is calculated as `4 * (last_equity - last_maintenance_margin)`. The last_equity and last_maintenance_margin values can be accessed through Account API. These values are stored from the end of the previous trading day.
Throughout the day, each time you enter a new position, your  `daytrading_buying_power` is reduced by that amount. When you exit that position within the same day, that same amount is credited back, regardless of position’s P/L.
At the end of the trading day, on close, the maximum exposure of your day trading position is checked. A Day Trade Margin Call (DTMC) is issued the next day if the maximum exposure of day trades exceeded your day trading buying power from the beginning of that day.
The buying_power value is the larger of `regt_buying_power` and `daytrading_buying_power`. Since the basic buying power check runs on this buying_power value, you could be exceeding your `daytrading_buying_power` when you enter the position if `regt_buying_power` is larger than your `daytrading_buying_power` at one point in the day.
The following is an example scenario:

- Your equity is $50k
- You hold overnight positions up to $100k
- Your maintenance margin is $30k (~30%), therefore your day trading buying power at the beginning of day is $80k using the calculation of 4 * ($50k - $30k)
- You sell all of the overnight positions ($100k value) in the morning, which brings your `regt_buying_power` up to $100k
- You now buy and sell the same security up to $100k
- At the end of the day, you have a $20k Day Trade Margin Call ($100k - $80k)

By default, Alpaca users have DTMC protections on entry of a position. This means that if your entering order would exceed `daytrading_buying_power` at the moment, it will be blocked, even if `regt_buying_power` still has room for it. This is based on the assumption that any entering position could be day trades later in the day. This option is the more conservative of the two DTMC protections that our users have.
The second DTMC protection option is protection on exit of a position. This means that Alpaca will block the exit of positions that would cause a Day Trading Margin Call. This may cause users to be unable to liquidate a position until the next day.
Neither of the DTMC protection options evaluate crypto orders since crypto cannot be purchased using margin.
One of the two protections will be enabled for all users (you cannot have both protections disabled). If you would like to switch your protection option, please contact our support.
We are working towards features to allow users to change their DTMC protection setting on their own without support help.

## Equity/Order Ratio Validation Check

In order to help Alpaca Brokerage Account customers from placing orders larger than the calculated buying power, Alpaca has instituted a control on the account independent of the buying power for the account. Alpaca will restrict the account to closing transactions when an account has a position that is 600% larger than the equity in the account. The account will remain restricted for closing transactions until a member of Alpaca’s trading team reviews the account. The trading team will either clear the alert by allowing opening transactions or will notify the client of the restriction and take corrective actions as necessary.

## Paper Trading

he same protection triggers in your paper trading account. It is advised to test your algorithm with the realistic balance amount you would manage when going live, to make sure your assumption works under this DTMC protection as well.
For more details of Pattern Day Trader rule, please read FINRA’s margin requirements. For more details on day trade margins, please read FINRA’s Mind Your Margin article.

# Preventing Wash Trades at Alpaca

At Alpaca, we want to help our customers avoid making unintentional wash trades. A wash trade happens when a customer buys and sells the same security at the same time, which can be seen as a form of market manipulation. To prevent this, the Alpaca Trading platform checks for potential wash trades every time a customer places an order. If we detect a possible wash trade, we reject the order and send back an error message with the HTTP status code 403 (Forbidden).

## The Rule

A wash trade occurs when a customer&#x27;s two orders could potentially interact with each other. Here are a couple of examples:

- 
A customer places an order to buy 1 share at $10 (a limit order). Then, the same customer places an order to sell 100 shares at $10 (another limit order). These orders could potentially interact, which would be a wash trade.

- 
A customer places an order to sell 100 shares at the market open (a market order). Then, the same customer places an order to buy 100 shares at $10 (a limit order). Again, these orders could potentially interact, which would be a wash trade.

## How Alpaca Handles Potential Wash Trades

The Alpaca Trading platform is always on the lookout for potential wash trades. If we determine that an order could result in a wash trade, we trigger our protection measures, reject the order, and send back an error message with the HTTP status code 403 (Forbidden).
If a customer wants to set up a &#x27;take profit&#x27; and a &#x27;stop loss&#x27; situation, we recommend using a bracket or OCO (One Cancels the Other) order. These complex orders and trailing stop orders are exceptions to our wash trade protection.
Here&#x27;s a table that shows when we would reject an order to prevent a potential wash trade:

Existing OrderNew OrderReject Condition
 | market buy | market sell | always rejected
 | market buy | limit sell | always rejected
 | market buy | stop sell | always rejected
 | market buy | stop_limit sell | always rejected
 | market sell | market buy | always rejected
 | market sell | limit buy | always rejected
 | market sell | stop buy | always rejected
 | market sell | stop_limit buy | always rejected
 | stop buy | market sell | always rejected
 | stop buy | limit sell | always rejected
 | stop buy | stop sell | always rejected
 | stop buy | stop_limit sell | always rejected
 | stop sell | market buy | always rejected
 | stop sell | limit buy | always rejected
 | stop sell | stop buy | always rejected
 | stop sell | stop_limit buy | always rejected
 | limit buy | market sell | always rejected
 | limit buy | limit sell | rejected if buy limit price >= sell limit price
 | limit buy | stop sell | always rejected
 | limit buy | stop_limit sell | rejected if buy limit price >= sell limit price
 | limit sell | market buy | always rejected
 | limit sell | limit buy | rejected if buy limit price >= sell limit price
 | limit sell | stop buy | always rejected
 | limit sell | stop_limit buy | rejected if buy limit price >= sell limit price
 | stop_limit buy | market sell | always rejected
 | stop_limit buy | limit sell | rejected if buy limit price >= sell limit price
 | stop_limit buy | stop sell | always rejected
 | stop_limit buy | stop_limit sell | rejected if buy limit price >= sell limit price
 | stop_limit sell | market buy | always rejected
 | stop_limit sell | limit buy | rejected if buy limit price >= sell limit price
 | stop_limit sell | stop buy | always rejected
 | stop_limit sell | stop_limit buy | rejected if buy limit price >= sell limit price

## Paper Trading

Our wash trade protection also applies to your paper trading account. We recommend testing your trading algorithm with a realistic balance amount. This way, you can make sure your strategy works under our wash trade protection rules before you start live trading.
For more details of wash trade rule, please read

FINRA&#x27;s self-trades requirements.Updated 3 months ago DMA Gateway / Advanced Order TypesWebsocket Streaming- Ask AI
