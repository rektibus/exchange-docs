CoinMate.io Trading Portal APIIntroductionExamples in Java, TypeScript, Python, PHP (https://github.com/coinmate-io/coinmate-api-examples)SecurityPublic operations are available without any user authentication and they are not secured at all. Private operations are secured by message signing. User must generate public and private key beforehand.From the version 1.3 it is possible to generate more API key pairs for one account.In each private operation, it is necessary to send these parameters along:client IDpublicKey (optional)noncesignatureEach user can find out client ID and generate API key pairs in application GUI (Account -> API).Public key identifies, which key pair is used. The oldest generated key is used if the publicKey parameter is omitted.Nonce is a number that can be used only once. Each following operation must have greater nonce than previous operation with the same key pair. For example, if first operation had nonce equal to 1, then second operation would have nonce at least 2. It is generally recommended to use unix timestamps as nonce.You may receive access denied if the nonce is used incorrectly (for example parallel calls may arrive in different order).Signature is created as a message encrypted using HMAC-SHA256 algorithm. Its input contains a nonce, client ID and public API key, such as signatureInput = nonce + clientId + publicApiKey. This signatureInput is then encrypted using private key. Resulting string must be converted to hexadecimal format as 64 characters containing only numbers and digits A to F.Sample Python code that calculates signature:import hashlib
import hmac

def createSignature(clientId, publicKey, privateKey, nonce):
    message = bytes(f"{nonce}{clientId}{publicKey}", encoding="utf-8")
    signature = hmac.new(privateKey, message, digestmod=hashlib.sha256).hexdigest()
    return signature.upper()
Example of parameters with publicKey:clientId=6&publicKey=CpmRVUJL0OGByT2otAfCKeeDdU6yfi6OzvnXcAwaHvE&nonce=0&signature=E4F27EAB0A836873CEE325A2526CC7476E2A3F2BE8026CADFB7A66B72D582DE8
WebsocketCoinmate offers standard Websocket API in two versions.First version (1.0) offers connection to websockets at different URLs. Once the connection is established, the client is automatically subscribed to channel mapped to mentioned URL.Second version (2.0) offers connection on single URL and client needs to send messages described below to subscribe/unsubscribe concrete channels. The URL for connection to Coinmate Websocket API version 2.0 is wss://coinmate.io/api/websocket. After successful connection to Websocket API of version 2.0, the client can subscribe to desired channels. The message has following JSON format:event: subscribedata:channel - [channelName]clientId (only for private channels)publicKey (only for private channels)signature (only for private channels)nonce (only for private channels)There is example subscribe message: {"event":"subscribe", "data":{"channel":"trades-BTC_EUR"}}Channel names are listed in examples below. The event for unsubscription is unsubscribe. The authentication data for private channels is standard data described in Security section.Please refer to the javascript Websocket documentation or documentations for other programming languages to connect to our websocket streams. You can also find an example for each channel below.Every websocket message sent by coinmate is one of listed types of events:data - contains payload field with requested dataping - sent every x seconds to keep the connection livepong - sent as a response to ping message from client (not mandatory to keep connection live)subscribe_success - sent as a response to successful subscriptionunsubscribe_success - sent as a response to successful unsubscriptionerror - sent as a response to invalid message and contains message field with descriptionThe XChange library (https://github.com/knowm/XChange) also supports websockets.Public channelsFor version 1.0, public channels are available at URLs with prefixes wss://coinmate.io/api/websocket/channel and it is not necessary to send any authentication data for the connection. Please refer to the public channels demo for a detailed connection example.New tradesRequestURL for version 1.0/trades/{CURRENCY_PAIR}Channel name for version 2.0trades-{CURRENCY_PAIR}CURRENCY_PAIR can be any valid currency pair e.g. BTC_EURResponse streams (JSON)date - Trade timestamp. Timestamp is in milliseconds.price - Trade priceamount - Trade amount. Meaning quantity of the last fill(lastQty).type - type of the trade (BUY or SELL)buyOrderId - Trade buy order idsellOrderId - Trade sell order idOrder bookRequestURL for version 1.0/order-book/{CURRENCY_PAIR}Channel name for version 2.0order_book-{CURRENCY_PAIR}CURRENCY_PAIR can be any valid currency pair e.g. BTC_EURResponse streams (JSON)Bids - List of bidsPriceAmountAsks - List of asksPriceAmountTrade statisticsRequestURL for version 1.0/trade-stats/{CURRENCY_PAIR}Channel name for version 2.0statistics-{CURRENCY_PAIR}CURRENCY_PAIR can be any valid currency pair e.g. BTC_EURResponse streams (JSON)lastRealizedTrade - Price of last realized trade.todaysOpen - Price of today's open trade.dailyChange - Daily percentual price change.volume24Hours - Daily traded volume.high24hours - Today's highest traded price.low24hours - Today's lowest traded price.Private channelsFor version 1.0, Private channels are available at URL with prefix wss://coinmate.io/api/websocket/channel and it is necessary to send authentication data as request parameters for the connection. The authentication data is standard data described in Security section. Please refer to the private channels demo for a detailed connection example.User open ordersRequestURLs for version 1.0/my-open-orders/{CURRENCY_PAIR}/my-open-orders for open orders independent on currency pairChannel names for version 2.0private-open_orders-{ACCOUNT_ID}-{CURRENCY_PAIR}private-open_orders-{ACCOUNT_ID} for open orders independent on currency pairCURRENCY_PAIR can be any valid currency pair e.g. BTC_EURACCOUNT_ID is ID of account (the same as clientID from authentication data)Snapshot of open orders in a form of order list is sent right after the subscription.Response streams (JSON)List of user ordersamount - Order size in first currency (e.g. in BTC for BTC_EUR currency pair)date - Order creation time as unix timestamp. Timestamp is in milliseconds.hidden - Flag indicating that order is or is not hidden. Valid flag value is true or falseid - Order IDclientOrderId - Order ID specified by API clientoriginal - Original order size.price - Pricetype - Order type e.g. "BUY", "BUY STOP", "SELL", "SELL STOP"stopPrice - Stop loss price. Attribute available just for stop loss orderstrailing - Indicates whether stop loss order is also trailing. Valid flag value is true or falseoriginalStopPrice - In case of stop loss trailing order holds stop price specified during order creation. Attribute available just for stop loss trailing orderspriceAtStopLossCreation - In case of stop loss trailing order holds market price at time of during order creation. Attribute available just for stop loss trailing orderspriceAtStopLossUpdate - In case of stop loss trailing order holds market price at time of last stop price update. Attribute available just for stop loss trailing orderstrailingUpdatedTimestamp - Time of the last update of stop price. Time is unix timestamp in milliseconds Timestamp is in milliseconds. Attribute available just for stop loss trailing orderscurrencyPair - Currency pair.orderChangePushEvent - REMOVAL, UPDATE, CREATION or SNAPSHOTorderChangePushEvent meaningCREATION - Order has been createdUPDATE - Order with given id has been updated with given parameters (e.g. partially filled)REMOVAL - Order with given id has been removed (e.g. cancelled or filled)SNAPSHOT - Order snapshot stateUser balancesRequestURL for version 1.0/my-balancesChannel name for version 2.0private-user_balances-{ACCOUNT_ID}ACCOUNT_ID is ID of account (the same as clientID from authentication data)Response streams (JSON)List of user balancesbalance - current financial amountreserved - financial amount reserved for open ordersUser tradesRequestURLs for version 1.0/my-trades/{CURRENCY_PAIR}/my-trades for trades independent on currency pairChannel names for version 2.0private-user-trades-{ACCOUNT_ID}-{CURRENCY_PAIR}private-user-trades-{ACCOUNT_ID} for trades independent on currency pairCURRENCY_PAIR can be any valid currency pair e.g. BTC_EURACCOUNT_ID is ID of account (the same as clientID from authentication data)Response streams (JSON)List of user tradestransactionId - transaction IDdate - transaction creation time as unix timestamp, Timestamp is in milliseconds.amount - traded volumeprice - price in case of buy / sellbuyOrderId - order ID of buying order in the transactionsellOrderId - order ID of selling order in the transactionorderType - type of user order in the trade ("BUY" or "SELL")type - type of trade ("BUY" or "SELL") - indicates which order acts as taker order in the tradefee - transaction fee amounttradeFeeType - transaction fee type from user point of view ("MAKER" or "TAKER")currencyPair - Currency pair.clientOrderId - Order ID specified by API clientUser transfersRequestURL for version 1.0/my-transfersChannel name for version 2.0private-user-transfers-{ACCOUNT_ID}ACCOUNT_ID is ID of account (the same as clientID from authentication data)Response streams (JSON)User transfer (when created or updated)id - transaction IDdate - transaction creation time as unix timestamp, Timestamp is in milliseconds.type - type of transfers ("DEPOSIT" or "WITHDRAWAL")currency - Currency nameamount - transfer amountfee - transfer feetotal - amount without feedestination - destination address or account numberdescription - transaction hash or bank transfer detailsstatus - current status of transfer ("NEW", "PENDING", etc.)Changelog2025-06-16Added new endpoint POST /bankWireWithdrawalAllows to withdraw funds via bank wire transfer2025-02-27Disabled stop loss ordersrequests using parameter stopPrice will receive error Not implementedAffected Endpoints: /buyLimit, /sellLimit, /replaceByBuyLimit, /replaceBySellLimitAdded new endpoint POST /currencies2025-02-11Updated Transfers / transferStatus enum description
ReferenceRequest limitsPlease not make more than 100 request per minute or we will ban your IP address. For trades and order book we recommend to use [Websocket API] (http://docs.coinmate.apiary.io/#introduction/websocket).
XChangeLatest configuration file for the XChange library (https://github.com/knowm/XChange) is available at https://coinmate.io/api/xchange
CurrenciesInformation about available currencies and their networksInfo about each currency has following attributes:currency - currency shortcutcurrencyName - name of currencydepositEnabled - boolean value indicating if deposits are enabledwithdrawEnabled - boolean value indicating if withdrawals are enabledprecision - maximum number of decimals you may use when entering amountnetworks - list of supported networksnetwork - network namedepositenabled - boolean value indicating if deposits are enabledfixFee - fixed fee for depositpercentageFee - if it is greater than zero, the fee is calculated as a percentage of amountminAmount - minimum deposit amountminConfirmations - maximum deposit confirmationswithdrawenabled - boolean value indicating if withdrawals are enabledrequiresTag - boolean value indicating if withdrawal requires tagfee - list of possible fee variantfixFee - fixed fee for withdrawpercentageFee - if it is greater than zero, the fee is calculated as a percentage of amountvariant - withdraw variantminAmount - minimum withdraw amountmax24hLimit - maximum withdraw amount per day
Get currenciesUSER OPERATIONReturns a list currencies
POST
Trading PairsInformation about available trading pairsInfo about each trading pair has following attributes:name - trading pair namefirstCurrency - name of first currency in the pairsecondCurrency - name of second currency in the pairpriceDecimals - maximum number of decimals you may use when entering price on the trading pairlotDecimals - maximum number of decimals you may use when entering amount on the trading pairminAmount - minimum amount
Get trading pairsPUBLIC OPERATIONReturns a list trading pairs
GET
Order BookOrder for buying or selling.Order has following attributes:Bids - List of bidsPriceAmountAsks - List of asksPriceAmount
Get order bookPUBLIC OPERATIONReturns a list of orders to buy and to sell. It returns only limited amount of highest asks (resp. bids) depending on configuration parameter.Consider to advantages of use Order book from [Websocket API] (http://docs.coinmate.apiary.io/#introduction/websocket) instead of calling this method.
GET
TickerRepresents basic details about current market situation.Ticker has following attributes.Last - current rateHigh - highest rate within last 24 hoursLow - lowest rate within last 24 hoursAmount - transactions amount within last 24 hoursBid - highest order for buyingAsk - lowest order for sellingOpen - today's openChange - daily change as percentage difference between today's open and last realized tradeTimestamp - unix timestamp. Timestamp is in milliseconds.
Get tickerPUBLIC OPERATIONReturns a ticker.
GET
Get ticker allPUBLIC OPERATIONReturns a ticker for all currency pairs.
GET
Currency pairsInformation about available currency trading pairs.
Get currency pairsPUBLIC OPERATIONReturns all available currency trading pairs.Currency pair has following attributes.id - currency pair namefromSymbol - first currency nametoSymbol - second currency name
GET
TransactionsMaterialized transaction.Transaction has following attributes.timestamp - unix timestamp. Timestamp is in milliseconds.transactionId - unique transaction IDprice - priceamount - amountcurrencyPair - currency pair (BTC_EUR, BTC_CZK)tradeType (BUY,SELL)
TransactionsPUBLIC OPERATIONReturns a list of last materialized transactions.Consider to advantages of use New trades from [Websocket API] (http://docs.coinmate.apiary.io/#introduction/websocket) instead of calling this method.
GET
BalanceAccount has following attributes.balance - current financial amountreserved - financial amount reserved for open ordersavailable - available financial amount (available = balance - reserved)
Get balancesUSER OPERATIONList of balances by individual currencies.
POST
Trader Fees
Get trading feesUSER OPERATIONMaker and taker fees for selected currency pair.
Required input parameters	
currency pair	selected currency pair, for example: BTC_EUR
Output parameters	
maker	Maker fee for selected currency.
taker	Taker fee for selected currency.
timestamp	Unix timestamp. Timestamp is in milliseconds.
POST
Transaction HistoryTransaction has following attributes:transactionId - transaction IDtimestamp - transaction creation time as unix timestamp, Timestamp is in milliseconds.transactionType - transaction type (BUY, SELL, INSTANT_BUY, INSTANT_SELL, QUICK_BUY, QUICK_SELL, DEPOSIT, WITHDRAWAL, CREATE_VOUCHER, USED_VOUCHER, NEW_USER_REWARD, OTHER, DEBIT, CREDIT, REFERRAL)amount - transaction amountamountCurrency - transaction amount currencyprice - price in case of buy / sellpriceCurrency - currency of transaction pricefee - transaction feefeeCurrency - fee currencydescription - transaction descriptionstatus -transaction status (WAITING, SENT, CREATED, OK, PENDING, NEW, CANCELED)orderId - order ID of BUY or SELL transaction
Get transaction historyUSER OPERATIONList of transactions that user has materialized. Maximum amount of transactions is also limited by a limit defined in application configuration itself. Application limit is superior to the limit specified by user. Result items are ordered by timestamp.
Optional input parameters	
offset	Number of transactions that should be skipped from the beginning. Default value is 0
limit	Maximum number of transactions that should be returned. Default value is 1000. Maximum is 1000.
sort	If transaction should be sorted by timestamp in 'ASC' or 'DESC' order. Default is 'DESC'
orderId	If defined, returns only BUY and SELL transactions with given orderId
timestampFrom	If defined, returns only transactions with timestamp greater than or equals to given timestampFrom (as unix timestamp in milliseconds)
timestampTo	If defined, returns only transactions with timestamp lower than or equals to given timestampTo (as unix timestamp in milliseconds)
POST
Trade HistoryTrade history has these following attributes:transactionId - transaction IDcreatedTimestamp - transaction creation time as unix timestamp, Timestamp is in milliseconds.currencyPair - trade's currency pairtype - BUY / SELLorderType - LIMIT / INSTANT / QUICKorderId - ID of the relevant orderamount - amount tradedprice - price of the total tradefee - fee pricefeeType - MAKER / TAKER
Get trade historyUSER OPERATIONReturns user's trade history.
Optional input parameters	
limit	Maximum number of trades that should be returned. Default value is equal to the maximum value, which is 1000.
lastId	Only trades with transaction ID lower/greater (depending on sort value) are returned
sort	If trades should be sorted by timestamp in 'ASC' or 'DESC' order. Default is 'DESC'
timestampFrom	If defined, returns only trades with timestamp greater or equal than given timestampFrom (unix timestamp in milliseconds)
timestampTo	If defined, returns only trades with timestamp lower or equal than given timestampTo (unix timestamp in milliseconds)
currencyPair	If defined, returns only trades with the given currency pair name
orderId	If defined, returns only trades with the given order ID
POST
TransfersTransfer has following attributes:id - transaction idfee - transfer feetransferType - transfer type (WITHDRAWAL,DEPOSIT)timestamp - timestamp in millisecondstransferStatus - status of the transferNEW - starting state, ready for processingBEFORE_SEND - short lived state, for internal retry mechanismSENT - withdrawal was sent, waiting for confirmationsPENDING - transfer exceeded verification transfer limits and is waiting for renewal or waiting for confirmation from 3rd party serviceWAITING - transfer is waiting for manual approvalERRORCANCELLEDCOMPLETEDVERIFIED - COMPLETED state with extra manual verification/approvalamount - transfer amountamountCurrency - currencywalletType - wallet type (BANK_WIRE, BTC, LTC ...)txid - txid of the transfer in blockchain. Only for virtual currency transfers.destination - virtual currency address. Only for virtual currency transfers.destinationTag - XRP destination tag. Only for XRP transfers.
Get transferUSER OPERATIONReturns specific transfer with given transaction ID.
Required input parameters	
transactionId	Transaction id of the transfer you want to get information about.
POST
Get transfer historyUSER OPERATIONReturns history of transfers.
Optional input parameters	
limit	Maximum number of transfers that should be returned. Default value is 1000. Maximum is 1000.
lastId	Only transfers with transactionId lower/greater (depending on sort value) are returned
sort	If transfers should be sorted by timestamp in 'ASC' or 'DESC' order. Default is 'DESC'
timestampFrom	If defined, returns only transfers with timestamp greater or equal than given timestampFrom (unix timestamp in milliseconds)
timestampTo	If defined, returns only transfers with timestamp lower or equal than given timestampTo (unix timestamp in milliseconds)
currency	If defined, returns only transfers of given currency
POST
OrderEach order used in the following methods has following attributes.id - order IDtimestamp - order creation time as unix timestamp. Timestamp is in milliseconds.type - order type (BUY or SELL)price - priceamount - amountNote Minimum order size is 0.001 BTC.
Order historyUSER OPERATIONThis method is available from version 1.5. It will return list of orders.
Required input parameters	
currencyPair	Currency pair identified for example by "BTC_EUR".
limit	Integer defined value, which determines maximum value of returned orders. It's optional value. In case of not using this parameter, default value from configuration will be used.
Output parameters	
List of an object with following items :	
id	Order ID.
timestamp	Order creation time as unix timestamp. Timestamp is in milliseconds.
type	Order type(BUY or SELL).
price	Price.
remainingAmount	Amount of the order that has not been matched.
originalAmount	Original order size.
status	Status of order. Possible outcomes : "CANCELLED", "FILLED", "PARTIALLY_FILLED", "OPEN".
orderTradeType	Order trade type (LIMIT, INSTANT, QUICK, LIMIT_STOP)
stopPrice	Stop loss price
trailing	Indicates whether stop loss order is also trailing
trailingUpdatedTimestamp	Time of the last update of stop price (or null if it has not been updated yet). Time is unix timestamp in milliseconds
originalStopPrice	In case of stop loss trailing order holds stop price specified during order creation
marketPriceAtLastUpdate	In case of stop loss trailing order holds market price at time of last stop price update
marketPriceAtOrderCreation	In case of stop loss trailing order holds market price at time of during order creation
hidden	Indicates whether order is hidden
avgPrice	Average price of order across all fills
trailing	Indicates whether stop loss order is also trailing
stopLossOrderId	Stop-loss order ID that was replaced by a system-generated market order in case when a stopPrice (of Stop-loss order) was breached
originalOrderId	Id of the original (cancelled) stop-loss order
POST
Get open ordersUSER OPERATIONReturns a list of open orders.
Optional input parameters	
currencyPair	currency pair identified for example by BTC_EUR
Output parameters	
List of an object with following items :	
id	Order ID.
timestamp	Order creation time as unix timestamp. Timestamp is in milliseconds.
type	Order type (BUY or SELL).
currencyPair	Currency pair identifier
price	Price.
amount	Amount
orderTradeType	Order trade type (LIMIT, MARKET, LIMIT_STOP)
stopPrice	Stop loss price
trailing	Indicates whether stop loss order is also trailing
trailingUpdatedTimestamp	Time of the last update of stop price (or null if it has not been updated yet). Time is unix timestamp in milliseconds
originalStopPrice	In case of stop loss trailing order holds stop price specified during order creation
marketPriceAtLastUpdate	In case of stop loss trailing order holds market price at time of last stop price update
marketPriceAtOrderCreation	In case of stop loss trailing order holds market price at time of during order creation
hidden	Indicates whether order is hidden
trailing	Indicates whether stop loss order is also trailing
clientOrderId	Order ID specified by API client
stopLossOrderId	Stop-loss order ID that was replaced by a system-generated market order in case when a stopPrice (of Stop-loss order) was breached
originalOrderId	Id of the original (cancelled) stop-loss order
POST
Get order by clientOrderIdUSER OPERATIONReturns a list of orders with given clientOrderId.
Required input parameters	
clientOrderId	Client specified order id in number format.
Output parameters	
List of objects with following attributes :	
id	Order ID.
timestamp	Order creation time as unix timestamp. In milliseconds.
type	Order type(BUY or SELL).
price	Price.
remainingAmount	Amount of the order that has not been matched.
originalAmount	Original order size.
cumulativeAmount	Cumulative amount on trades.
stopPrice	Stop price of stop loss order.
status	Status of order. Possible outcomes : "CANCELLED", "FILLED", "PARTIALLY_FILLED", "OPEN".
avgPrice	Average price of order across all fills.
trailing	Indicates whether stop loss order is also trailing
stopLossOrderId	Stop-loss order ID that was replaced by a system-generated market order in case when a stopPrice (of Stop-loss order) was breached
originalOrderId	Id of the original (cancelled) stop-loss order
trades	Trades which fulfilled the order.
POST
Get order by orderIdUSER OPERATIONReturns a order with given orderId
Required input parameters	
orderId	Order ID.
Output parameters	
id	Order ID.
timestamp	Order creation time as unix timestamp. In milliseconds.
type	Order type(BUY or SELL).
price	Price.
remainingAmount	Amount of the order that has not been matched.
originalAmount	Original order size.
cumulativeAmount	Cumulative amount on trades.
stopPrice	Stop price of stop loss order.
status	Status of order. Possible outcomes : "CANCELLED", "FILLED", "PARTIALLY_FILLED", "OPEN".
avgPrice	Average price of order across all fills.
trailing	Indicates whether stop loss order is also trailing
stopLossOrderId	Stop-loss order ID that was replaced by a system-generated market order in case when a stopPrice (of Stop-loss order) was breached
originalOrderId	Id of the original (cancelled) stop-loss order
trades	Trades which fulfilled the order.
POST
Cancel orderUSER OPERATIONCancels open order.
Required input parameters	
orderId	ID of order to be cancelled
Output parameters	
success	true if order was found and cancelled successfully, false otherwise
POST
Cancel all open ordersUSER OPERATIONCancels all open orders for the specified currency pair or for all currency pairs, if one is not specified.
Optional input parameters	
currencyPair	currency pair identified for example by BTC_EUR
Output parameters version	
id to remaining amount mapping collection	a dictionary which keys are defined as cancelled order IDs and values are not matched remaining amounts of those cancelled orders
POST
Cancel order with infoUSER OPERATIONCancels open order. Operation is available from version 1.3
Required input parameters	
orderId	ID of order to be cancelled
Output parameters from version 1.3	
success	true if order was found and cancelled successfully, false otherwise
remainingAmount	amount of the order that has not been matched
POST
Buy limit orderUSER OPERATIONCreates new order for buying of type limit order. If stop loss price is set creates limit_stop order.When current price crosses stopPrice, market buy is created for amount * price.
Required input parameters	
amount	Order size in first currency (e.g. in BTC for BTC_EUR currency pair)
price	price
currencyPair	currency pair identified for example by BTC_EUR
Optional input parameters	
stopPrice
DISABLED	Stop loss price. Must be higher than current price.
trailing	Flag indicating that stop loss order should be created as trailing. Valid flag value is 0 or 1. Default value is 0
hidden	Flag indicating that order should be created as hidden. Valid flag value is 0 or 1. Default value is 0
immediateOrCancel	In case the flag is set: if limit order is not fully settled immediately the remaining part of the order is cancelled at the end of request. Valid flag value is 0 or 1. Default value is 0
postOnly	Post-Only (also called Maker-Or-Cancel) flag - in case the flag is set the entire order is either placed as maker, or if any part of the order can be filled immediately, the entire order is canceled (ensuring you pay the maker fee only). Valid flag value is 0 or 1. Default value is 0
clientOrderId	Numeric client ID of order used to access order in case of not receiving order id.
Output parameters	
id	order ID
POST
Replace existing order by buy limit orderUSER OPERATIONReplaces existing order by newly created limit buy order. Order to be replaced can be of any type. Replace operation consists of two operations - cancel and create. At first cancel is called on orderIdToBeReplaced. Subsequent create is called only if the previous cancel is successful (order wasn't fully matched or canceled). The call result contains information about unsuccessful cancel. Please note that the cancellation of previous order is reverted if new order creation fails.
Required input parameters	
amount	Order size in first currency (e.g. in BTC for BTC_EUR currency pair)
price	price
currencyPair	currency pair identified for example by BTC_EUR
orderIdToBeReplaced	id of order which should be replaced
Optional input parameters	
stopPrice
DISABLED	Stop loss price. Must be higher than current price.
trailing	Flag indicating that stop loss order should be created as trailing. Valid flag value is 0 or 1. Default value is 0
hidden	Flag indicating that order should be created as hidden. Valid flag value is 0 or 1. Default value is 0
immediateOrCancel	In case the flag is set: if limit order is not fully settled immediately the remaining part of the order is cancelled at the end of request. Valid flag value is 0 or 1. Default value is 0
postOnly	Post-Only (also called Maker-Or-Cancel) flag - in case the flag is set the entire order is either placed as maker, or if any part of the order can be filled immediately, the entire order is canceled (ensuring you pay the maker fee only). Valid flag value is 0 or 1. Default value is 0
clientOrderId	Id (number) of order used to access order in case of not receiving order id. Please do not specify more than 20 digits
Output parameters	
createdOrderId	ID of newly created Order
replacedOrderCancellationFinished	indicates whether cancel finished (if true then create operation has been called)
replacedOrderCancellationResult	result of cancel operation in text form
replacedOrderRemainingAmount	amount of the cancelled order that has not been matched
POST
Sell limit orderUSER OPERATIONCreates new order for selling of type limit order. If stop loss price is set creates limit_stop order.When current price crosses stopPrice, market sell is created for amount.
Required input parameters	
amount	Order size in first currency (e.g. in BTC for BTC_EUR currency pair)
price	price
currencyPair	currency pair identified for example by BTC_EUR
Optional input parameters	
stopPrice
DISABLED	Stop loss price. Must be lower than current price.
trailing	Flag indicating that stop loss order should be created as trailing. Valid flag value is 0 or 1. Default value is 0
hidden	Flag indicating that order should be created as hidden. Valid flag value is 0 or 1. Default value is 0
immediateOrCancel	In case the flag is set: if limit order is not fully settled immediately the remaining part of the order is cancelled at the end of request. Valid flag value is 0 or 1. Default value is 0
postOnly	Post-Only (also called Maker-Or-Cancel) flag - in case the flag is set the entire order is either placed as maker, or if any part of the order can be filled immediately, the entire order is canceled (ensuring you pay the maker fee only). Valid flag value is 0 or 1. Default value is 0
clientOrderId	Numeric client ID of order used to access order in case of not receiving order id.
Output parameters	
id	order ID
POST
Replace existing order by sell limit orderUSER OPERATIONReplaces existing order by newly created limit sell order. Order to be replaced can be of any type. Replace operation consists of two operations - cancel and create. At first cancel is called on orderIdToBeReplaced. Subsequent create is called only if the previous cancel is successful (order wasn't fully matched or canceled). The call result contains information about unsuccessful cancel. Please note that the cancellation of previous order is reverted if new order creation fails.
Required input parameters	
amount	Order size in first currency (e.g. in BTC for BTC_EUR currency pair)
price	price
currencyPair	currency pair identified for example by BTC_EUR
orderIdToBeReplaced	id of order which should be replaced
Optional input parameters	
stopPrice
DISABLED	Stop loss price. Must be lower than current price.
trailing	Flag indicating that stop loss order should be created as trailing. Valid flag value is 0 or 1. Default value is 0
hidden	Flag indicating that order should be created as hidden. Valid flag value is 0 or 1. Default value is 0
immediateOrCancel	In case the flag is set: if limit order is not fully settled immediately the remaining part of the order is cancelled at the end of request. Valid flag value is 0 or 1. Default value is 0
postOnly	Post-Only (also called Maker-Or-Cancel) flag - in case the flag is set the entire order is either placed as maker, or if any part of the order can be filled immediately, the entire order is canceled (ensuring you pay the maker fee only). Valid flag value is 0 or 1. Default value is 0
clientOrderId	Id (number) of order used to access order in case of not receiving order id. Please do not specify more than 20 digits
Output parameters	
createdOrderId	ID of newly created Order
replacedOrderCancellationFinished	indicates whether cancel finished (if true then create operation has been called)
replacedOrderCancellationResult	result of cancel operation in text form
replacedOrderRemainingAmount	amount of the cancelled order that has not been matched
POST
Buy instant orderUSER OPERATIONCreates new order for buying of type instant order. User only specifies amount of EUR that should be used for buying BTC.
Required input parameters	
total	amount to pay in second currency (e.g. in EUR for BTC_EUR currency pair)
currencyPair	currency pair identified for example by BTC_EUR
Optional input parameters	
clientOrderId	Numeric client ID of order used to access order in case of not receiving order id.
Output parameters	
id	order ID
POST
Replace existing order by buy instant orderUSER OPERATIONReplaces existing order by newly created instant buy order. Order to be replaced can be of any type. Replace operation consists of two operations - cancel and create. At first cancel is called on orderIdToBeReplaced. Subsequent create is called only if the previous cancel is successful (order wasn't fully matched or canceled). The call result contains information about unsuccessful cancel. Please note that the cancellation of previous order is reverted if new order creation fails.
Required input parameters	
total	amount to pay in second currency (e.g. in EUR for BTC_EUR currency pair)
currencyPair	currency pair identified for example by BTC_EUR
orderIdToBeReplaced	id of order which should be replaced
Optional input parameters	
clientOrderId	Id (number) of order used to access order in case of not receiving order id. Please do not specify more than 20 digits
Output parameters	
createdOrderId	ID of newly created Order
replacedOrderCancellationFinished	indicates whether cancel finished (if true then create operation has been called)
replacedOrderCancellationResult	result of cancel operation in text form
replacedOrderRemainingAmount	amount of the cancelled order that has not been matched
POST
Sell instant orderUSER OPERATIONCreates new order for selling of type instant order. User only specifies amount of bitcoins to sell.
Required input parameters	
amount	amount to sell in first currency (e.g. in BTC for BTC_EUR currency pair)
currencyPair	currency pair identified for example by BTC_EUR
Optional input parameters	
clientOrderId	Numeric client ID of order used to access order in case of not receiving order id.
Output parameters	
id	order id
POST
Replace existing order by sell instant orderUSER OPERATIONReplaces existing order by newly created instant sell order. Order to be replaced can be of any type. Replace operation consists of two operations - cancel and create. At first cancel is called on orderIdToBeReplaced. Subsequent create is called only if the previous cancel is successful (order wasn't fully matched or canceled). The call result contains information about unsuccessful cancel. Please note that the cancellation of previous order is reverted if new order creation fails.
Required input parameters	
amount	amount to sell in first currency (e.g. in BTC for BTC_EUR currency pair)
currencyPair	currency pair identified for example by BTC_EUR
orderIdToBeReplaced	id of order which should be replaced
Optional input parameters	
clientOrderId	Id (number) of order used to access order in case of not receiving order id. Please do not specify more than 20 digits
Output parameters	
createdOrderId	ID of newly created Order
replacedOrderCancellationFinished	indicates whether cancel finished (if true then create operation has been called)
replacedOrderCancellationResult	result of cancel operation in text form
replacedOrderRemainingAmount	amount of the cancelled order that has not been matched
POST
Virtual currency withdrawal and deposit
Withdraw virtual currencyUSER OPERATIONPlease note that the maximum number of decimal places for XRP and ADA is 6. It is difference from the other currencies, where the number of decimal places is 8
Required input parameters	
currencyName	name of virtual currency to withdraw (ADA, BTC, ETH, LTC, SOL, USDT, XRP)
address	address where to send assets
amount	number of assets to withdraw
Optional input parameters	
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
destinationTag	destination tag where to send assets (for XRP only)
feePriority	Priority type of withdrawal (HIGH or LOW). Default value is HIGH. (for BTC only)
Output parameters	
id	Coinmate transaction ID
POST
Virtual currency deposit addressesUSER OPERATION
Required input parameters	
currencyName	name of virtual currency to withdraw (ADA, BTC, ETH, LTC, SOL, USDT, XRP)
Output parameters	
List of selected virtual currency addresses and destination tags	
POST
Unconfirmed virtual currency depositsUSER OPERATION
Required input parameters	
currencyName	name of virtual currency to withdraw (ADA, BTC, ETH, LTC, SOL, USDT, XRP)
Output parameters	
id	transaction ID
amount	amount of assets
address	address / destination tag where to send assets
numberOfConfirmations	number of confirmations
POST
Bitcoin withdrawal and deposit
Withdraw bitcoinsUSER OPERATION
Required input parameters	
amount	number of bitcoins to withdraw
address	address where to send bitcoins
Optional input parameters	
feePriority	Priority type of withdrawal (HIGH or LOW). Default value is HIGH.
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Bitcoin withdrawal feesUSER OPERATION
Output parameters	
low	Bitcoin low priority withdrawal fee.
high	Bitcoin high priority withdrawal fee.
timestamp	Unix timestamp. Timestamp is in milliseconds.
POST
Bitcoin deposit addressesUSER OPERATION
Output parameters	
List of bitcoin addresses	
POST
Unconfirmed bitcoin depositsUSER OPERATION
Output parameters	
id	bitcoin transaction ID
amount	number of bitcoins
address	address where to send bitcoins
numberOfConfirmations	number of confirmations
POST
Bitcoin lightning depositsUSER OPERATIONLimits for amount are same as on web.
Required input parameters	
amount	amount for deposit in BTC
clientId	API client ID.
Output parameters	
currency	BTC
address	BTC deposit lightning address
POST
Bitcoin lightning withdrawalsUSER OPERATIONLimits for amount are same as on web.
Required input parameters	
address	BTC lightning address
clientId	API client ID.
Optional input parameters	
amount	amount for withdrawal in BTC if is not specified in invoice
Output parameters	
id	Coinmate transaction ID
POST
Litecoin withdrawal and deposit
Withdraw litecoinsUSER OPERATION
Required input parameters	
amount	number of litecoins to withdraw
address	address where to send litecoins
Optional input parameters	
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Litecoin deposit addressesUSER OPERATION
Output parameters	
List of litecoin addresses	
POST
Unconfirmed litecoin depositsUSER OPERATION
Output parameters	
id	litecoin transaction ID
amount	number of litecoins
address	address where to send litecoins
numberOfConfirmations	number of confirmations
POST
Ethereum withdrawal and deposit
Withdraw EthereumUSER OPERATION
Required input parameters	
amount	number of Ethers to withdraw
address	address where to send Ethers
Optional input parameters	
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Ethereum deposit addressesUSER OPERATION
Output parameters	
List of ethereum addresses	
POST
Unconfirmed ethereum depositsUSER OPERATION
Output parameters	
id	ethereum transaction ID
amount	number of Ethers
address	address where to send Ethers
numberOfConfirmations	number of confirmations
POST
Ripple withdrawal and deposit
Withdraw RippleUSER OPERATIONPlease note that the maximum number of decimal places for amount is 6. It is difference from the other currencies, where the number of decimal places is 8
Required input parameters	
amount	number of XRP to withdraw (max. number of decimal places is 6)
address	address where to send XRP
Optional input parameters	
destinationTag	destination tag where to send XRPs
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Ripple deposit addressesUSER OPERATION
Output parameters	
List of pairs ripple address and destination tag	
POST
Unconfirmed ripple depositsUSER OPERATION
Output parameters	
id	ripple transaction ID
amount	number of XRPs
address	address where to send XRPs
destinationTag	destination tag where to send XRPs
numberOfConfirmations	number of confirmations
POST
Cardano withdrawal and deposit
Withdraw CardanoUSER OPERATIONPlease note that the maximum number of decimal places for amount is 6. It is difference from the other currencies, where the number of decimal places is 8.
Required input parameters	
amount	number of ADA to withdraw (max. number of decimal places is 6)
address	address where to send ADA
Optional input parameters	
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Cardano deposit addressesUSER OPERATION
Output parameters	
List of Cardano address	
POST
Unconfirmed Cardano depositsUSER OPERATION
Output parameters	
id	Cardano transaction ID
amount	number of ADAs
address	address where to send ADAs
numberOfConfirmations	number of confirmations
POST
Solana withdrawal and deposit
Withdraw SolanaUSER OPERATIONPlease note that the maximum number of decimal places for amount is 8. It is difference from the default Solana decimal places which is 9.
Required input parameters	
amount	number of SOL to withdraw (max. number of decimal places is 8)
address	address where to send SOL
Optional input parameters	
amountType	Withdrawal amount type specifying, if withdrawal amount includes fee or not ("NET" or "GROSS"). Default is amountType "GROSS".
Output parameters	
id	Coinmate transaction ID
POST
Solana deposit addressesUSER OPERATION
Output parameters	
List of Solana address	
POST
Unconfirmed Solana depositsUSER OPERATION
Output parameters	
id	Solana transaction ID
amount	number of SOLs
address	address where to send SOLs
numberOfConfirmations	number of confirmations
POST
USDT withdrawal and depositWithdraw USDTPlease visit section Withdraw virtual currency.USDT deposit addressesPlease visit section Virtual currency deposit addresses.Unconfirmed USDT depositsPlease visit section Unconfirmed virtual currency deposits.
FIAT withdrawal and deposit
Bankwire withdrawalUSER OPERATIONWithdraws funds from the user's account to their bank account. Supports both domestic (CZK) and SEPA (EUR) transfers.Important notes:Bank accounts (CZK or EUR) must be stored as a withdrawal template. Requests to unknown or non-whitelisted accounts will be rejected with an Insufficient key privileges error.The token permission for bank withdrawals must be manually assigned to the API key by our support staff. Contact support to enable this permission.SEPA transfers are not processed immediatelly.
Required input parameters	
currencyName	Currency to withdraw ("EUR" or "CZK")
amount	Amount to withdraw (must be positive)
accountNumber	Bank account number (format depends on currency)
bankCode	Bank code (format depends on currency)
For CZK withdrawals:accountNumber must be in domestic format (e.g., "123456789" or with prefix "19-123456789")bankCode must be 4 digits (e.g., "0800")For EUR withdrawals:accountNumber must be in IBAN format (e.g., "DE89370400440532013000")bankCode must be in BIC/SWIFT format (e.g., "DEUTDEFF")
Output parameters	
error	Indicates if the request was successful (false) or failed (true)
errorMessage	Error message if the request failed (null if successful)
data	Response data containing the transfer ID if successful
POST
SystemSystem-level endpoints providing metadata or technical details about the API or server.
Get server timePUBLIC OPERATIONReturns current server time in epoch timestamp format in milliseconds.
GET
