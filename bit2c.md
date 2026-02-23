Bit2C API Documantation
General
API access to our platform with JSON responses.

Public Methods
Ticker
Request URL
GET https://bit2c.co.il/Exchanges/[BtcNis/EthNis/LtcNis/UsdcNis]/Ticker.json
Parameters: none

JSON Response:
Parameter	Description
ll	last price
av	last 24 hours price avarage
a	last 24 hours volume
h	highest buy order
l	lowest sell order
c	last 24 hours average change - decimal(nullable)
up	last change - true = up , false - down , null - no change

Order Book
Request URL
GET https://bit2c.co.il/Exchanges/[BtcNis/EthNis/LtcNis/UsdcNis]/orderbook.json
Parameters: none
JSON Response:
{
"asks":[[price,amount],...],
"bids":[[price,amount],...]
}

Last 24h Trades (executions)
Request URL
GET https://bit2c.co.il/Exchanges/[BtcNis/EthNis/LtcNis/UsdcNis]/lasttrades
Parameters: none

JSON Response:
Parameter	Type	Description
date	number	unix timestamp date and time
isBid	boolean	a boolean value
ture = taker buy
false = taker sell
price	number	price
amount	number	amount
tid	number	transaction id

All Trades (executions)
Request URL
GET https://bit2c.co.il/Exchanges/[BtcNis/EthNis/LtcNis/UsdcNis]/trades.json
Parameters:
limit (number)
since (number)
date (number)

JSON Response:
Parameter	Type	Description
date	number	unix timestamp date and time
isBid	boolean	a boolean value
ture = taker buy
false = taker sell
amount	number	amount
tid	number	transaction id
