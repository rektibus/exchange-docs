# Bybit API Documentation

Source: Official Bybit OpenAPI Spec (bybit.yaml)

## Bybit Open API v5 explorer

Collection of v5 Restul API


Version: 3.0.0

## Servers

- https://api-testnet.bybit.com — Testnet server

## Endpoints

### GET `/v5/market/account-ratio`

**Get Long Short Ratio**

Get long short ratio

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| period | query | array | True | period |
| limit | query | integer | False | Maximum 500 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/delivery-price`

**Get Delivery Price**

Get delivery price

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type. linear, inverse, option |
| symbol | query | string | False | Symbol name |
| baseCoin | query | string | False | Base coin, for option only. Return BTC by default |
| limit | query | string | False | Maximum 200 |
| cursor | query | string | False | The cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/market/funding/history`

**Get Funding Rate History**

Get historical funding rate

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| startTime | query | integer | False | The start timstamp (ms) |
| endTime | query | integer | False | The end timstamp (ms) |
| limit | query | integer | False | Maximum 200 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/historical-volatility`

**Get Historical Volatility**

Get historical volatility

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| baseCoin | query | string | False | Base coin. If not passed, BTC returned by default |
| period | query | array | False | Period. If not passed, it returns 7 days by default. SOL does not have 180 and 270 |
| startTime | query | integer | False | The start timstamp (ms) |
| endTime | query | integer | False | The end timstamp (ms) |

**Responses:**

- `200`: successful operation

### GET `/v5/market/index-price-kline`

**Get Index Price Kline**

Get Index Price Kline data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| interval | query | array | True | kline interval |
| start | query | integer | False | start timestamp (ms). e.g., 1669852800000 (1 DEC 2022 UTC 0:00) |
| end | query | integer | False | end timestamp (ms). e.g., 1671062400000 (15 DEC 2022 UTC 0:00) |
| limit | query | integer | False | Maximum 1000 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/instruments-info`

**Get Instrument Info**

Get launched instruments information.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | False | Symbol name |
| status | query | string | False | Status filter |
| baseCoin | query | string | False | for linear, invere and option ONLY |
| limit | query | integer | False | Maximum 1000. spot does not have pagination |
| cursor | query | string | False | pass cursor from the response param "nagePageCursor" to paginate |

**Responses:**

- `200`: successful operation

### GET `/v5/market/insurance`

**Get Insurance**

Get Insurance

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| coin | query | string | False | Coin name |

**Responses:**

- `200`: successful operation

### GET `/v5/market/kline`

**Get Kline**

Get kline data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| interval | query | array | True | kline interval |
| start | query | integer | False | start timestamp (ms). e.g., 1669852800000 (1 DEC 2022 UTC 0:00) |
| end | query | integer | False | end timestamp (ms). e.g., 1671062400000 (15 DEC 2022 UTC 0:00) |
| limit | query | integer | False | Maximum 1000 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/mark-price-kline`

**Get Mark Price Kline**

Get Mark Price Kline data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| interval | query | array | True | kline interval |
| start | query | integer | False | start timestamp (ms). e.g., 1669852800000 (1 DEC 2022 UTC 0:00) |
| end | query | integer | False | end timestamp (ms). e.g., 1671062400000 (15 DEC 2022 UTC 0:00) |
| limit | query | integer | False | Maximum 1000 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/open-interest`

**Get Open Interest**

Get open interest

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| intervalTime | query | array | True | interval time |
| startTime | query | integer | False | The start timstamp (ms) |
| endTime | query | integer | False | The end timstamp (ms) |
| limit | query | integer | False | Maximum 200 |
| cursor | query | string | False | pass cursor from the response param "nagePageCursor" to paginate |

**Responses:**

- `200`: successful operation

### GET `/v5/market/orderbook`

**Get Orderbook**

Get order book data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| limit | query | integer | False | spot：1-200，default：1. linear&inverse：1-200，default：25. option：1-25，default：1 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/premium-index-price-kline`

**Get Premium Index Price Kline**

Get Premium Index Price Kline data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name |
| interval | query | array | True | kline interval |
| start | query | integer | False | start timestamp (ms). e.g., 1669852800000 (1 DEC 2022 UTC 0:00) |
| end | query | integer | False | end timestamp (ms). e.g., 1671062400000 (15 DEC 2022 UTC 0:00) |
| limit | query | integer | False | Maximum 1000 |

**Responses:**

- `200`: successful operation

### GET `/v5/market/recent-trade`

**Get Public Recent Trading History**

Get public trade

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | True | Symbol name. |
| baseCoin | query | string | False | Base coin. Valid for option. Default is BTC |
| optionType | query | string | False | Option type. Valid for option. |
| limit | query | integer | False | Maximum 60 for spot. Maximum 1000 for others |

**Responses:**

- `200`: successful operation

### GET `/v5/market/risk-limit`

**Get Risk Limit**

Get risk limit

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| symbol | query | string | False | Symbol name |

**Responses:**

- `200`: successful operation

### GET `/v5/market/tickers`

**Get Tickers**

Get all latest information of symbols. All parameters are needed for OPTION

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| category | query | array | True | Product type |
| baseCoin | query | string | False | for option ONLY, baseCoin or symbol must be passed when query option |
| expDate | query | string | False | Expiry date. For option only. Default is all, and the parameter format is 25MAR22. |
| symbol | query | string | False | Symbol name |

**Responses:**

- `200`: successful operation

### GET `/v5/market/time`

**Get Bybit Server Time**

Get server time

**Responses:**

- `200`: successful operation

## Bybit v5 trade api explorer

Collection of Trade - v5 Restul API, which covers USDT Perpetual, USDC Perpetual, Inverse Perpetual, Inverse Future, Spot and Option.


Version: 3.0.0

## Servers

- https://api-testnet.bybit.com — Testnet server

## Endpoints

### POST `/v5/order/amend`

**Amend Order**

Amend an order.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/amend-batch`

**Batch Amend Order**

Batch amend orders

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/cancel`

**Cancel Order**

Cancel a single order.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/cancel-all`

**Cancel All Orders**

Cancel all orders.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/cancel-batch`

**Batch Cancel Order**

Batch cancel orders

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/create`

**Place Order**

Place an order.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/order/create-batch`

**Batch Place Order**

Batch place orders

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### GET `/v5/order/history`

**Get Order History (2 years)**

Get order history.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| baseCoin | query | string | False | Base coin |
| orderId | query | string | False |  |
| orderLinkId | query | string | False | User customised order id |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| orderStatus | query | string | False | Order status |
| orderFilter | query | string | False | Order filter |
| limit | query | integer | False | 1-50. max 50 |
| cursor | query | string | False | cursor to pagnition |

**Responses:**

- `200`: successful operation

### GET `/v5/order/realtime`

**Get Open Orders (real-time)**

Get unfilled orders or partially filled orders

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| baseCoin | query | string | False | Base coin |
| settleCoin | query | string | False | Settle coin. Spot is not available |
| orderId | query | string | False |  |
| orderLinkId | query | string | False | User customised order id |
| orderFilter | query | string | False | Order filter. Default：all kinds of orders |
| openOnly | query | integer | False | Whether to only query active orders, if openOnly = 0, only get active orders. If it is 1, return onl |
| limit | query | integer | False | 1-50. max 50 |
| cursor | query | string | False | cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/order/spot-borrow-check`

**Get Borrow Quota (Spot)**

Query user's spot available quota

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | True | Symbol name |
| side | query | string | True | Buy or Sell |

**Responses:**

- `200`: successful operation

## Bybit Open API v5 explorer

Collection of v5 Restul API


Version: 3.0.0

## Servers

- https://api-testnet.bybit.com — Testnet server

## Endpoints

### GET `/v5/account/borrow-history`

**Get Borrow History**

Get borrow history

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| currency | query | string | False | e.g., USDC, USDT, BTC, ETH |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit per page. 1-50 |
| cursor | query | string | False | Cusor, used for pagiation |

**Responses:**

- `200`: successful operation

### GET `/v5/account/coin-greeks`

**Get Coin Greeks**

Get coin greek info

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| baseCoin | query | string | False | Base coin |

**Responses:**

- `200`: successful operation

### GET `/v5/account/collateral-info`

**Get Collateral Info**

Get collateral info

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| currency | query | string | False | Collateral asset |

**Responses:**

- `200`: successful operation

### GET `/v5/account/fee-rate`

**Get Fee Rate**

Get fee rate

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type. working for spot and option |
| symbol | query | string | False | Symbol name. valid for linear,inverse and spot |
| baseCoin | query | string | False | Base coin. Valid for option |

**Responses:**

- `200`: successful operation

### GET `/v5/account/info`

**Get Account Info**

Get account info

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/account/set-collateral-switch`

**Set Collateral Coin**

Set collateral coin

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/account/set-hedging-mode`

**Set Spot Hedging**

Set spot hedging for Portfolio margin

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/account/set-margin-mode`

**Set Margin Mode**

Set margin mode

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### GET `/v5/account/transaction-log`

**Get Transaction Log**

Get transaction log

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| accountType | query | string | False | Support `UNIFIED` for now |
| category | query | string | False | Product category |
| currency | query | string | False | Currency |
| baseCoin | query | string | False | Base coin |
| type | query | string | False | Transaction log type |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size for each page. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/account/upgrade-to-uta`

**Upgrade to Unified Account**

Upgrade to UTA

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### GET `/v5/account/wallet-balance`

**Get Wallet Balance**

Get wallet balance

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| accountType | query | string | True | Account type |
| coin | query | string | False | Coin name. You can pass mutiple coins like USDT,USDC |

**Responses:**

- `200`: successful operation

## Bybit Open API v5 explorer

Collection of v5 Restul API


Version: 3.0.0

## Servers

- https://api-testnet.bybit.com — Testnet server

## Endpoints

### GET `/v5/asset/coin/query-info`

**Get Coin Info**

Get coin info

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| coin | query | string | False | Coin name |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/delivery-record`

**Get Delivery Record**

Get delivery record

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| expDate | query | string | False | expired date |
| limit | query | integer | False | 1-50. max 50 |
| cursor | query | string | False | cursor, used for pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/asset/deposit/deposit-to-account`

**Set Deposit Account**

Set Deposit Account

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-address`

**Get Master Deposit Address**

Get master deposit address

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| coin | query | string | True | Coin name |
| chainType | query | string | False | Chain name |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-allowed-list`

**Get Allowed Deposit Coin Info**

Get allowed deposit coin info

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| coin | query | string | False | Coin name. coin and chain must be paired if passed |
| chain | query | string | False | Chain name. coin and chain must be paired if passed |
| limit | query | integer | False | Limit size. 1-35 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-internal-record`

**Get Internal Deposit Records (off-chain)**

Get deposit records through Bybit platform

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| coin | query | string | False | Coin name |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-record`

**Get Deposit Record (on-chain)**

Get deposit record

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| coin | query | string | False | Coin name |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used to pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-sub-member-address`

**Get Sub Deposit Address**

Get sub deposit address

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| coin | query | string | True | Coin name |
| chainType | query | string | True | Chain name |
| subMemberId | query | string | True | Sub UID |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/deposit/query-sub-member-record`

**Get Sub Account Deposit Records (on-chain)**

Get sub account deposit record

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| subMemberId | query | string | True | Sub UID |
| coin | query | string | False | Coin name |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/exchange/order-record`

**Get Coin Exchange Records**

Get exchange records

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| fromCoin | query | string | False | From coin |
| toCoin | query | string | False | To coin |
| limit | query | integer | True | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/settlement-record`

**Get USDC Session Settlement**

Get usdc session settlement record.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name. USDC perp or USDC futures |
| limit | query | integer | False | 1-50. max 50 |
| cursor | query | string | False | cursor, used for pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/asset/transfer/inter-transfer`

**Create Internal Transfer**

Create internal transfer

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-account-coin-balance`

**Get Single Coin Balance**

Get Single Coin Balance

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| memberId | query | string | False | If query sub user balance, please input sub uid |
| accountType | query | string | True | Account type |
| coin | query | string | True | Coin name |
| withBonus | query | integer | False | Query bonus or not. 0=false, 1=true |
| withTransferSafeAmount | query | integer | False | Whether query delay withdraw/transfer safe amount. 0：false, 1；true |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-account-coins-balance`

**Get All Coins Balance**

Get All Coins Balance

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| memberId | query | string | False | If query sub user balance, please input sub uid |
| accountType | query | string | True | Account type |
| coin | query | string | False | Coin name |
| withBonus | query | integer | False | Query bonus or not. 0=false, 1=true |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-asset-info`

**Get Asset Info (Spot)**

Get spot asset

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| accountType | query | string | True | Account type |
| coin | query | string | False | Coin name |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-inter-transfer-list`

**Get Internal Transfer Records**

Get internal transfer records

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| transferId | query | string | False | Transfer id |
| coin | query | string | False | Coin name |
| status | query | string | False | Status |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-sub-member-list`

**Get Sub UID**

Get sub uid

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api key |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-transfer-coin-list`

**Get Transferable Coin**

Get transferable coins

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| fromAccountType | query | string | True | From account type |
| toAccountType | query | string | True | To account type |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/transfer/query-universal-transfer-list`

**Get Universal Transfer Records**

Get universal transfer record

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| transferId | query | string | False | Transfer id |
| coin | query | string | False | Coin name |
| status | query | string | False | Status |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used for pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/asset/transfer/universal-transfer`

**Create Universal Transfer**

Create universal transfer

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |

**Responses:**

- `200`: successful operation

### GET `/v5/asset/withdraw/query-record`

**Get Withdraw Records**

Get withdraw record

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | True | Use master UID api key |
| secret | header | string | True | Use master UID api secret |
| withdrawID | query | string | False | Withdraw ID |
| coin | query | string | False | Coin name |
| withdrawType | query | integer | False | Withdraw type. 0=on chain, 1=off chain, 2=all |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | Limit size. 1-50 |
| cursor | query | string | False | Cursor, used to pagination |

**Responses:**

- `200`: successful operation

## Bybit v5 position api explorer

Collection of Position - v5 Restul API, which covers USDT Perpetual, USDC Perpetual, Inverse Perpetual, Inverse Future and Option.


Version: 3.0.0

## Servers

- https://api-testnet.bybit.com — Testnet server

## Endpoints

### GET `/v5/execution/list`

**Get Execution (2 years)**

Get execution list

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| baseCoin | query | string | False | Base coin |
| orderId | query | string | False |  |
| orderLinkId | query | string | False | User customised order id |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| execType | query | string | False | Execution type |
| limit | query | integer | False | 1-100. max 100 |
| cursor | query | string | False | cursor to pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/position/add-margin`

**Add Or Reduce Margin**

Manually add or reduce margin for isolated margin position

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### GET `/v5/position/closed-pnl`

**Get Closed PnL**

Get closed pnl

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| startTime | query | integer | False | The start timestamp (ms) |
| endTime | query | integer | False | The end timestamp (ms) |
| limit | query | integer | False | 1-200. max 200 |
| cursor | query | string | False | cursor for pagination |

**Responses:**

- `200`: successful operation

### GET `/v5/position/list`

**Get Position Info**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |
| category | query | string | True | Product type |
| symbol | query | string | False | Symbol name |
| baseCoin | query | string | False | Base coin. For option only |
| settleCoin | query | string | False | Used for linear & inverse, symbol or settleCoin is required |
| limit | query | integer | False | 1-200. max 200 |
| cursor | query | string | False | cursor, used for pagination |

**Responses:**

- `200`: successful operation

### POST `/v5/position/set-auto-add-margin`

**Set Auto Add Margin**

Set Auto Add Margin

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/set-leverage`

**Set Leverage**

Set levearage.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/set-risk-limit`

**Set Risk Limit**

Set risk limit.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/set-tpsl-mode`

**Set TP/SL Mode**

Set tp/sl mode.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/switch-isolated`

**Switch Cross/Isolated Margin**

Select cross margin mode or isolated margin mode

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/switch-mode`

**Switch Position Mode**

Switch Position Mode

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

### POST `/v5/position/trading-stop`

**Set Trading Stop**

Set trade stop.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| apiKey | header | string | False | A UTA sub account API key is provided by default |
| secret | header | string | False | A UTA sub account API key is provided by default |

**Responses:**

- `200`: successful operation

