# Hyperliquid API Documentation

Auto-fetched from 3 page(s)


---

# Source: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint

bars[Hyperliquid Docs](/hyperliquid-docs)

search

circle-xmark

`⌘Ctrl``k`

  * [Hyperliquid Docs](/hyperliquid-docs)
  * [Builder Tools](/hyperliquid-docs/builder-tools)
  * [Support](/hyperliquid-docs/support)



chevron-leftchevron-right

[Hyperliquid Docs](/hyperliquid-docs)

  * [About Hyperliquidchevron-right](/hyperliquid-docs)
  * [Onboardingchevron-right](/hyperliquid-docs/onboarding)
  * [HyperCorechevron-right](/hyperliquid-docs/hypercore)
  * [HyperEVMchevron-right](/hyperliquid-docs/hyperevm)
  * [Hyperliquid Improvement Proposals (HIPs)chevron-right](/hyperliquid-docs/hyperliquid-improvement-proposals-hips)
  * [Tradingchevron-right](/hyperliquid-docs/trading)
  * [Validatorschevron-right](/hyperliquid-docs/validators)
  * [Referralschevron-right](/hyperliquid-docs/referrals)
  * [Points](/hyperliquid-docs/points)
  * [Historical data](/hyperliquid-docs/historical-data)
  * [Risks](/hyperliquid-docs/risks)
  * [Bug bounty program](/hyperliquid-docs/bug-bounty-program)
  * [Audits](/hyperliquid-docs/audits)
  * [Brand kit](/hyperliquid-docs/brand-kit)
  * For developers

    * [APIchevron-right](/hyperliquid-docs/for-developers/api)

      * [Notation](/hyperliquid-docs/for-developers/api/notation)
      * [Asset IDs](/hyperliquid-docs/for-developers/api/asset-ids)
      * [Tick and lot size](/hyperliquid-docs/for-developers/api/tick-and-lot-size)
      * [Nonces and API wallets](/hyperliquid-docs/for-developers/api/nonces-and-api-wallets)
      * [Info endpointchevron-right](/hyperliquid-docs/for-developers/api/info-endpoint)

        * [Perpetuals](/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals)
        * [Spot](/hyperliquid-docs/for-developers/api/info-endpoint/spot)

      * [Exchange endpoint](/hyperliquid-docs/for-developers/api/exchange-endpoint)
      * [Websocketchevron-right](/hyperliquid-docs/for-developers/api/websocket)
      * [Error responses](/hyperliquid-docs/for-developers/api/error-responses)
      * [Signing](/hyperliquid-docs/for-developers/api/signing)
      * [Rate limits and user limits](/hyperliquid-docs/for-developers/api/rate-limits-and-user-limits)
      * [Activation gas fee](/hyperliquid-docs/for-developers/api/activation-gas-fee)
      * [Optimizing latency](/hyperliquid-docs/for-developers/api/optimizing-latency)
      * [Bridge2](/hyperliquid-docs/for-developers/api/bridge2)
      * [Deploying HIP-1 and HIP-2 assets](/hyperliquid-docs/for-developers/api/deploying-hip-1-and-hip-2-assets)
      * [HIP-3 deployer actions](/hyperliquid-docs/for-developers/api/hip-3-deployer-actions)

    * [HyperEVMchevron-right](/hyperliquid-docs/for-developers/hyperevm)
    * [Nodeschevron-right](/hyperliquid-docs/for-developers/nodes)



chevron-upchevron-down

[gitbookPowered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=yUdp569E6w18GdfqlGvJ)

xmark

block-quoteOn this pagechevron-down

copyCopychevron-down

  1. [For developers](/hyperliquid-docs/for-developers)chevron-right
  2. [API](/hyperliquid-docs/for-developers/api)



# Info endpoint

The info endpoint is used to fetch information about the exchange and specific users. The different request bodies result in different corresponding response body schemas.

### 

[hashtag](#pagination)

Pagination

Responses that take a time range will only return 500 elements or distinct blocks of data. To query larger ranges, use the last returned timestamp as the next `startTime` for pagination.

### 

[hashtag](#perpetuals-vs-spot)

Perpetuals vs Spot

The endpoints in this section as well as websocket subscriptions work for both Perpetuals and Spot. For perpetuals `coin` is the name returned in the `meta` response. For Spot, coin should be `PURR/USDC` for PURR, and `@{index}` e.g. `@1` for all other spot tokens where index is the index of the spot pair in the `universe` field of the `spotMeta` response. For example, the spot index for HYPE on mainnet is `@107` because the token index of HYPE is 150 and the spot pair `@107` has tokens `[150, 0]`. Note that some assets may be remapped on user interfaces. For example, `BTC/USDC` on app.hyperliquid.xyz corresponds to `UBTC/USDC` on mainnet HyperCore. The L1 name on the [token details pagearrow-up-right](https://app.hyperliquid.xyz/explorer/token/0x8f254b963e8468305d409b33aa137c67) can be used to detect remappings.

### 

[hashtag](#user-address)

User address

To query the account data associated with a master or sub-account, you must pass in the actual address of that account. A common pitfall is to use an agent wallet's address which leads to an empty result.

## 

[hashtag](#retrieve-mids-for-all-coins)

Retrieve mids for all coins

`POST` `https://api.hyperliquid.xyz/info`

Note that if the book is empty, the last trade price will be used as a fallback

#### 

[hashtag](#headers)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body)

Request Body

Name

Type

Description

type*

String

"allMids"

dex

String

Perp dex name. Defaults to the empty string which represents the first perp dex. Spot mids are only included with the first perp dex..

200: OK Successful Response

## 

[hashtag](#retrieve-a-users-open-orders)

Retrieve a user's open orders

`POST` `https://api.hyperliquid.xyz/info`

See a user's open orders

#### 

[hashtag](#headers-1)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-1)

Request Body

Name

Type

Description

type*

String

"openOrders"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

dex

String

Perp dex name. Defaults to the empty string which represents the first perp dex. Spot open orders are only included with the first perp dex.

200: OK Successful R

## 

[hashtag](#retrieve-a-users-open-orders-with-additional-frontend-info)

Retrieve a user's open orders with additional frontend info

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-2)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-2)

Request Body

Name

Type

Description

type*

String

"frontendOpenOrders"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

dex

String

Perp dex name. Defaults to the empty string which represents the first perp dex. Spot open orders are only included with the first perp dex.

200: OK 

## 

[hashtag](#retrieve-a-users-fills)

Retrieve a user's fills

`POST` `https://api.hyperliquid.xyz/info`

Returns at most 2000 most recent fills

#### 

[hashtag](#headers-3)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-3)

Request Body

Name

Type

Description

type*

String

"userFills"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

aggregateByTime

bool

When true, partial fills are combined when a crossing order gets filled by multiple different resting orders. Resting orders filled by multiple crossing orders are only aggregated if in the same block.

200: OK

## 

[hashtag](#retrieve-a-users-fills-by-time)

Retrieve a user's fills by time

`POST` `https://api.hyperliquid.xyz/info`

Returns at most 2000 fills per response and only the 10000 most recent fills are available

#### 

[hashtag](#headers-4)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-4)

Request Body

Name

Type

Description

type*

String

userFillsByTime

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

startTime*

int

Start time in milliseconds, inclusive

endTime

int

End time in milliseconds, inclusive. Defaults to current time.

aggregateByTime

bool

When true, partial fills are combined when a crossing order gets filled by multiple different resting orders. Resting orders filled by multiple crossing orders are only aggregated if in the same block.

200: OK Number of fills is limited to 2000

## 

[hashtag](#query-user-rate-limits)

Query user rate limits

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#request-body-5)

Request Body

Name

Type

Description

user

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

type

String

userRateLimit

200: OK A successful response

## 

[hashtag](#query-order-status-by-oid-or-cloid)

Query order status by oid or cloid

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#request-body-6)

Request Body

Name

Type

Description

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

type*

String

"orderStatus"

oid*

uint64 or string

Either u64 representing the order id or 16-byte hex string representing the client order id

The <status> string returned has the following possible values:

Order status

Explanation

open

Placed successfully

filled

Filled

canceled

Canceled by user

triggered

Trigger order triggered

rejected

Rejected at time of placement

marginCanceled

Canceled because insufficient margin to fill

vaultWithdrawalCanceled

Vaults only. Canceled due to a user's withdrawal from vault 

openInterestCapCanceled

Canceled due to order being too aggressive when open interest was at cap

selfTradeCanceled

Canceled due to self-trade prevention

reduceOnlyCanceled

Canceled reduced-only order that does not reduce position

siblingFilledCanceled

TP/SL only. Canceled due to sibling ordering being filled

delistedCanceled

Canceled due to asset delisting

liquidatedCanceled

Canceled due to liquidation

scheduledCancel

API only. Canceled due to exceeding scheduled cancel deadline (dead man's switch)

tickRejected

Rejected due to invalid tick price

minTradeNtlRejected

Rejected due to order notional below minimum

perpMarginRejected

Rejected due to insufficient margin

reduceOnlyRejected

Rejected due to reduce only

badAloPxRejected

Rejected due to post-only immediate match

iocCancelRejected

Rejected due to IOC not able to match

badTriggerPxRejected

Rejected due to invalid TP/SL price

marketOrderNoLiquidityRejected

Rejected due to lack of liquidity for market order

positionIncreaseAtOpenInterestCapRejected

Rejected due to open interest cap

positionFlipAtOpenInterestCapRejected

Rejected due to open interest cap

tooAggressiveAtOpenInterestCapRejected

Rejected due to price too aggressive at open interest cap

openInterestIncreaseRejected

Rejected due to open interest cap

insufficientSpotBalanceRejected

Rejected due to insufficient spot balance

oracleRejected

Rejected due to price too far from oracle

perpMaxPositionRejected

Rejected due to exceeding margin tier limit at current leverage

200: OK A successful response

200: OK Missing Order

## 

[hashtag](#l2-book-snapshot)

L2 book snapshot

`POST` `https://api.hyperliquid.xyz/info`

Returns at most 20 levels per side

**Headers**

Name

Value

Content-Type*

"application/json"

**Body**

Name

Type

Description

type*

String

"l2Book"

coin*

String

coin

nSigFigs

Number

Optional field to aggregate levels to `nSigFigs` significant figures. Valid values are 2, 3, 4, 5, and `null`, which means full precision

mantissa

Number

Optional field to aggregate levels. This field is only allowed if nSigFigs is 5. Accepts values of 1, 2 or 5.

**Response**

200: OK

## 

[hashtag](#candle-snapshot)

Candle snapshot

`POST` `https://api.hyperliquid.xyz/info`

Only the most recent 5000 candles are available

Supported intervals: "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "8h", "12h", "1d", "3d", "1w", "1M"

**Headers**

Name

Value

Content-Type*

"application/json"

**Body**

Name

Type

Description

type*

String

"candleSnapshot"

req*

Object

{"coin": <coin>, "interval": "15m", "startTime": <epoch millis>, "endTime": <epoch millis>} For HIP-3, you need to prefix with the dex name, e.g. "xyz:XYZ100"

**Response**

200: OK

## 

[hashtag](#check-builder-fee-approval)

Check builder fee approval

`POST` `https://api.hyperliquid.xyz/info`

**Headers**

Name

Value

Content-Type*

"application/json"

**Body**

Name

Type

Description

type*

String

"maxBuilderFee"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

builder*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

**Response**

200: OK

## 

[hashtag](#retrieve-a-users-historical-orders)

Retrieve a user's historical orders

`POST` `https://api.hyperliquid.xyz/info`

Returns at most 2000 most recent historical orders

#### 

[hashtag](#headers-5)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-7)

Request Body

Name

Type

Description

type*

String

"historicalOrders"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#retrieve-a-users-twap-slice-fills)

Retrieve a user's TWAP slice fills

`POST` `https://api.hyperliquid.xyz/info`

Returns at most 2000 most recent TWAP slice fills

#### 

[hashtag](#headers-6)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-8)

Request Body

Name

Type

Description

type*

String

"userTwapSliceFills"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#retrieve-a-users-subaccounts)

Retrieve a user's subaccounts

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-7)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-9)

Request Body

Name

Type

Description

type*

String

"subAccounts"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#retrieve-details-for-a-vault)

Retrieve details for a vault

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-8)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-10)

Request Body

Name

Type

Description

type*

String

"vaultDetails"

vaultAddress*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

user

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#retrieve-a-users-vault-deposits)

Retrieve a user's vault deposits

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-9)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-11)

Request Body

Name

Type

Description

type*

String

"userVaultEquities"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-role)

Query a user's role

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-10)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-12)

Request Body

Name

Type

Description

type*

String

"userRole"

user*

String

Address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

User

Agent

Vault

Subaccount

Missing

## 

[hashtag](#query-a-users-portfolio)

Query a user's portfolio

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-11)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-13)

Request Body

Name

Type

Description

type*

String

"portfolio"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-referral-information)

Query a user's referral information

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-12)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-14)

Request Body

Name

Type

Description

type*

String

"referral"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

Note that rewardHistory is for legacy rewards. Claimed rewards are now returned in nonFundingLedgerUpdate

## 

[hashtag](#query-a-users-fees)

Query a user's fees

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-13)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-15)

Request Body

Name

Type

Description

type*

String

"userFees"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-staking-delegations)

Query a user's staking delegations

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-14)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-16)

Request Body

Name

Type

Description

type*

String

"delegations"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-staking-summary)

Query a user's staking summary

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-15)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-17)

Request Body

Name

Type

Description

type*

String

"delegatorSummary"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-staking-history)

Query a user's staking history

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-16)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-18)

Request Body

Name

Type

Description

type*

String

"delegatorHistory"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-staking-rewards)

Query a user's staking rewards

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-17)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-19)

Request Body

Name

Type

Description

type*

String

"delegatorRewards"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-hip-3-dex-abstraction-state)

Query a user's HIP-3 DEX abstraction state

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-18)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-20)

Request Body

Name

Type

Description

type*

String

"userDexAbstraction"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-a-users-abstraction-state)

Query a user's abstraction state

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-19)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-21)

Request Body

Name

Type

Description

type*

String

"userAbstraction"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-aligned-quote-token-status)

Query aligned quote token status

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-20)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-22)

Request Body

Name

Type

Description

type*

String

"alignedQuoteTokenInfo"

token*

Number

token index

200: OK

## 

[hashtag](#query-borrow-lend-user-state)

Query borrow/lend user state

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-21)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-23)

Request Body

Name

Type

Description

type*

String

"borrowLendUserState"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

## 

[hashtag](#query-borrow-lend-reserve-state)

Query borrow/lend reserve state

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-22)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-24)

Request Body

Name

Type

Description

type*

String

"borrowLendReserveState"

token*

Number

token index

200: OK

## 

[hashtag](#query-all-borrow-lend-reserve-states)

Query all borrow/lend reserve states

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-23)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-25)

Request Body

Name

Type

Description

type*

String

"allBorrowLendReserveStates"

200: OK

## 

[hashtag](#query-approved-builders-for-user)

Query approved builders for user

`POST` `https://api.hyperliquid.xyz/info`

#### 

[hashtag](#headers-24)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-26)

Request Body

Name

Type

Description

type*

String

"approvedBuilders"

user*

String

hexadecimal format; e.g. 0x0000000000000000000000000000000000000000.

200: OK

[PreviousNonces and API walletschevron-left](/hyperliquid-docs/for-developers/api/nonces-and-api-wallets)[NextPerpetualschevron-right](/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals)

Last updated 2 days ago

  * [Pagination](#pagination)
  * [Perpetuals vs Spot](#perpetuals-vs-spot)
  * [User address](#user-address)
  * [Retrieve mids for all coins](#retrieve-mids-for-all-coins)
  * [Retrieve a user's open orders](#retrieve-a-users-open-orders)
  * [Retrieve a user's open orders with additional frontend info](#retrieve-a-users-open-orders-with-additional-frontend-info)
  * [Retrieve a user's fills](#retrieve-a-users-fills)
  * [Retrieve a user's fills by time](#retrieve-a-users-fills-by-time)
  * [Query user rate limits](#query-user-rate-limits)
  * [Query order status by oid or cloid](#query-order-status-by-oid-or-cloid)
  * [L2 book snapshot](#l2-book-snapshot)
  * [Candle snapshot](#candle-snapshot)
  * [Check builder fee approval](#check-builder-fee-approval)
  * [Retrieve a user's historical orders](#retrieve-a-users-historical-orders)
  * [Retrieve a user's TWAP slice fills](#retrieve-a-users-twap-slice-fills)
  * [Retrieve a user's subaccounts](#retrieve-a-users-subaccounts)
  * [Retrieve details for a vault](#retrieve-details-for-a-vault)
  * [Retrieve a user's vault deposits](#retrieve-a-users-vault-deposits)
  * [Query a user's role](#query-a-users-role)
  * [Query a user's portfolio](#query-a-users-portfolio)
  * [Query a user's referral information](#query-a-users-referral-information)
  * [Query a user's fees](#query-a-users-fees)
  * [Query a user's staking delegations](#query-a-users-staking-delegations)
  * [Query a user's staking summary](#query-a-users-staking-summary)
  * [Query a user's staking history](#query-a-users-staking-history)
  * [Query a user's staking rewards](#query-a-users-staking-rewards)
  * [Query a user's HIP-3 DEX abstraction state](#query-a-users-hip-3-dex-abstraction-state)
  * [Query a user's abstraction state](#query-a-users-abstraction-state)
  * [Query aligned quote token status](#query-aligned-quote-token-status)
  * [Query borrow/lend user state](#query-borrow-lend-user-state)
  * [Query borrow/lend reserve state](#query-borrow-lend-reserve-state)
  * [Query all borrow/lend reserve states](#query-all-borrow-lend-reserve-states)
  * [Query approved builders for user](#query-approved-builders-for-user)



Copy
    
    
    {
        "APE": "4.33245",
        "ARB": "1.21695"
    }

Copy
    
    
    [
        {
            "coin": "BTC",
            "limitPx": "29792.0",
            "oid": 91490942,
            "side": "A",
            "sz": "0.0",
            "timestamp": 1681247412573
        }
    ]

Copy
    
    
    [
        {
            "coin": "BTC",
            "isPositionTpsl": false,
            "isTrigger": false,
            "limitPx": "29792.0",
            "oid": 91490942,
            "orderType": "Limit",
            "origSz": "5.0",
            "reduceOnly": false,
            "side": "A",
            "sz": "5.0",
            "timestamp": 1681247412573,
            "triggerCondition": "N/A",
            "triggerPx": "0.0",
        }
    ]

Copy
    
    
    [
        // Perp fill (first perp dex)
        {
            "closedPnl": "0.0",
            "coin": "AVAX",
            "crossed": false,
            "dir": "Open Long",
            "hash": "0xa166e3fa63c25663024b03f2e0da011a00307e4017465df020210d3d432e7cb8",
            "oid": 90542681,
            "px": "18.435",
            "side": "B",
            "startPosition": "26.86",
            "sz": "93.53",
            "time": 1681222254710,
            "fee": "0.01", // the total fee, inclusive of builderFee below
            "feeToken": "USDC",
            "builderFee": "0.01", // this is optional and will not be present if 0
            "tid": 118906512037719
        },
        // Perp Fill (HIP-3)
        {
            "coin": "xyz:XYZ100", // For HIP-3, the asset has the dex name as a prefix
            "px": "25372.0",
            "sz": "0.0353",
            "side": "B",
            "time": 1767651180109,
            "startPosition": "0.7045",
            "dir": "Open Long",
            "closedPnl": "0.0",
            "hash": "0xa166e3fa63c25663024b03f2e0da011a00307e4017465df020210d3d432e7cb9",
            "oid": 287286372177,
            "crossed": false,
            "fee": "0.026868",
            "tid": 164087028129848,
            "feeToken":" USDC"
        },
        // Spot fill - note the difference in the "coin" format. Refer to 
        // https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/asset-ids
        // for more information on how spot asset IDs work
        {
            "coin": "@107",
            "px": "18.62041381",
            "sz": "43.84",
            "side": "A",
            "time": 1735969713869,
            "startPosition": "10659.65434798",
            "dir": "Sell",
            "closedPnl": "8722.988077",
            "hash": "0x2222138cc516e3fe746c0411dd733f02e60086f43205af2ae37c93f6a792430b",
            "oid": 59071663721,
            "crossed": true,
            "fee": "0.304521",
            "tid": 907359904431134,
            "feeToken": "USDC"
        }
    ]

Copy
    
    
    [
        // Perp fill (first perp dex)
        {
            "closedPnl": "0.0",
            "coin": "AVAX",
            "crossed": false,
            "dir": "Open Long",
            "hash": "0xa166e3fa63c25663024b03f2e0da011a00307e4017465df020210d3d432e7cb8",
            "oid": 90542681,
            "px": "18.435",
            "side": "B",
            "startPosition": "26.86",
            "sz": "93.53",
            "time": 1681222254710,
            "fee": "0.01", // the total fee, inclusive of builderFee below
            "feeToken": "USDC",
            "builderFee": "0.01", // this is optional and will not be present if 0
            "tid": 118906512037719
        },
        // Perp Fill (HIP-3)
        {
            "coin": "xyz:XYZ100", // For HIP-3, the asset has the dex name as a prefix
            "px": "25372.0",
            "sz": "0.0353",
            "side": "B",
            "time": 1767651180109,
            "startPosition": "0.7045",
            "dir": "Open Long",
            "closedPnl": "0.0",
            "hash": "0xa166e3fa63c25663024b03f2e0da011a00307e4017465df020210d3d432e7cb9",
            "oid": 287286372177,
            "crossed": false,
            "fee": "0.026868",
            "tid": 164087028129848,
            "feeToken":" USDC"
        },
        // Spot fill - note the difference in the "coin" format. Refer to 
        // https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/asset-ids
        // for more information on how spot asset IDs work
        {
            "coin": "@107",
            "px": "18.62041381",
            "sz": "43.84",
            "side": "A",
            "time": 1735969713869,
            "startPosition": "10659.65434798",
            "dir": "Sell",
            "closedPnl": "8722.988077",
            "hash": "0x2222138cc516e3fe746c0411dd733f02e60086f43205af2ae37c93f6a792430b",
            "oid": 59071663721,
            "crossed": true,
            "fee": "0.304521",
            "tid": 907359904431134,
            "feeToken": "USDC"
        }
    ]

Copy
    
    
    {
      "cumVlm": "2854574.593578",
      "nRequestsUsed": 2890, // max(0, cumulative_used minus reserved)
      "nRequestsCap": 2864574, 
      "nRequestsSurplus": 0, // max(0, reserved minus cumulative_used)
    }

Copy
    
    
    {
      "status": "order",
      "order": {
        "order": {
          "coin": "ETH",
          "side": "A",
          "limitPx": "2412.7",
          "sz": "0.0",
          "oid": 1,
          "timestamp": 1724361546645,
          "triggerCondition": "N/A",
          "isTrigger": false,
          "triggerPx": "0.0",
          "children": [],
          "isPositionTpsl": false,
          "reduceOnly": true,
          "orderType": "Market",
          "origSz": "0.0076",
          "tif": "FrontendMarket",
          "cloid": null
        },
        "status": <status>,
        "statusTimestamp": 1724361546645
      }
    }

Copy
    
    
    {
      "status": "unknownOid"
    }

Copy
    
    
    {
      "coin": "BTC",
      "time": 1754450974231,
      "levels": [
        [
          {
            "px": "113377.0",
            "sz": "7.6699",
            "n": 17 // number of levels
          },
          {
            "px": "113376.0",
            "sz": "4.13714",
            "n": 8
          },
        ],
        [
          {
            "px": "113397.0",
            "sz": "0.11543",
            "n": 3
          }
        ]
      ]
    }

Copy
    
    
    [
      {
        "T": 1681924499999,
        "c": "29258.0",
        "h": "29309.0",
        "i": "15m",
        "l": "29250.0",
        "n": 189,
        "o": "29295.0",
        "s": "BTC",
        "t": 1681923600000,
        "v": "0.98639"
      }
    ]

Copy
    
    
    1 // maximum fee approved in tenths of a basis point i.e. 1 means 0.001%

Copy
    
    
    [
      {
        "order": {
          "coin": "ETH",
          "side": "A",
          "limitPx": "2412.7",
          "sz": "0.0",
          "oid": 1,
          "timestamp": 1724361546645,
          "triggerCondition": "N/A",
          "isTrigger": false,
          "triggerPx": "0.0",
          "children": [],
          "isPositionTpsl": false,
          "reduceOnly": true,
          "orderType": "Market",
          "origSz": "0.0076",
          "tif": "FrontendMarket",
          "cloid": null
        },
        "status": "filled" | "open" | "canceled" | "triggered" | "rejected" | "marginCanceled",
        "statusTimestamp": 1724361546645
      }
    ]

Copy
    
    
    [
        {
            "fill": {
                "closedPnl": "0.0",
                "coin": "AVAX",
                "crossed": true,
                "dir": "Open Long",
                "hash": "0x0000000000000000000000000000000000000000000000000000000000000000", // TWAP fills have a hash of 0
                "oid": 90542681,
                "px": "18.435",
                "side": "B",
                "startPosition": "26.86",
                "sz": "93.53",
                "time": 1681222254710,
                "fee": "0.01",
                "feeToken": "USDC",
                "tid": 118906512037719
            },
            "twapId": 3156
        }
    ]

Copy
    
    
    [
      {
        "name": "Test",
        "subAccountUser": "0x035605fc2f24d65300227189025e90a0d947f16c",
        "master": "0x8c967e73e6b15087c42a10d344cff4c96d877f1d",
        "clearinghouseState": {
          "marginSummary": {
            "accountValue": "29.78001",
            "totalNtlPos": "0.0",
            "totalRawUsd": "29.78001",
            "totalMarginUsed": "0.0"
          },
          "crossMarginSummary": {
            "accountValue": "29.78001",
            "totalNtlPos": "0.0",
            "totalRawUsd": "29.78001",
            "totalMarginUsed": "0.0"
          },
          "crossMaintenanceMarginUsed": "0.0",
          "withdrawable": "29.78001",
          "assetPositions": [],
          "time": 1733968369395
        },
        "spotState": {
          "balances": [
            {
              "coin": "USDC",
              "token": 0,
              "total": "0.22",
              "hold": "0.0",
              "entryNtl": "0.0"
            }
          ]
        }
      }
    ]

Copy
    
    
    {
      "name": "Test",
      "vaultAddress": "0xdfc24b077bc1425ad1dea75bcb6f8158e10df303",
      "leader": "0x677d831aef5328190852e24f13c46cac05f984e7",
      "description": "This community-owned vault provides liquidity to Hyperliquid through multiple market making strategies, performs liquidations, and accrues platform fees.",
      "portfolio": [
        [
          "day",
          {
            "accountValueHistory": [
              [
                1734397526634,
                "329265410.90790099"
              ]
            ],
            "pnlHistory": [
              [
                1734397526634,
                "0.0"
              ],
            ],
            "vlm": "0.0"
          }
        ],
        [
          "week" | "month" | "allTime" | "perpDay" | "perpWeek" | "perpMonth" | "perpAllTime",
          {...}
        ]
      ],
      "apr": 0.36387129259090006,
      "followerState": null,
      "leaderFraction": 0.0007904828725729887,
      "leaderCommission": 0,
      "followers": [
        {
          "user": "0x005844b2ffb2e122cf4244be7dbcb4f84924907c",
          "vaultEquity": "714491.71026243",
          "pnl": "3203.43026143",
          "allTimePnl": "79843.74476743",
          "daysFollowing": 388,
          "vaultEntryTime": 1700926145201,
          "lockupUntil": 1734824439201
        }
      ],
      "maxDistributable": 94856870.164485,
      "maxWithdrawable": 742557.680863,
      "isClosed": false,
      "relationship": {
        "type": "parent",
        "data": {
          "childAddresses": [
            "0x010461c14e146ac35fe42271bdc1134ee31c703a",
            "0x2e3d94f0562703b25c83308a05046ddaf9a8dd14",
            "0x31ca8395cf837de08b24da3f660e77761dfb974b"
          ]
        }
      },
      "allowDeposits": true,
      "alwaysCloseOnWithdraw": false
    }  

Copy
    
    
    [
      {
        "vaultAddress": "0xdfc24b077bc1425ad1dea75bcb6f8158e10df303",
        "equity": "742500.082809",
      }
    ]

Copy
    
    
    {"role":"user"} # "missing", "user", "agent", "vault", or "subAccount"

Copy
    
    
    {"role":"agent", "data": {"user": "0x..."}}

Copy
    
    
    {"role":"vault"}

Copy
    
    
    {"role":"subAccount", "data":{"master":"0x..."}}

Copy
    
    
    {"role":"missing"}

Copy
    
    
    [
      [
        "day",
        {
          "accountValueHistory": [
            [
              1741886630493,
              "0.0"
            ],
            [
              1741895270493,
              "0.0"
            ],
            ...
          ],
          "pnlHistory": [
            [
              1741886630493,
              "0.0"
            ],
            [
              1741895270493,
              "0.0"
            ],
            ...
          ],
          "vlm": "0.0"
        }
      ],
      ["week", { ... }],
      ["month", { ... }],
      ["allTime", { ... }],
      ["perpDay", { ... }],
      ["perpWeek", { ... }],
      ["perpMonth", { ... }],
      ["perpAllTime", { ... }]
    ]

Copy
    
    
    {
        "referredBy": {
            "referrer": "0x5ac99df645f3414876c816caa18b2d234024b487",
            "code": "TESTNET"
        },
        "cumVlm": "149428030.6628420055", // USDC Only
        "unclaimedRewards": "11.047361", // USDC Only
        "claimedRewards": "22.743781", // USDC Only
        "builderRewards": "0.027802", // USDC Only
        "tokenToState":[
          0,
          {
             "cumVlm":"149428030.6628420055",
             "unclaimedRewards":"11.047361",
             "claimedRewards":"22.743781",
             "builderRewards":"0.027802"
          }
       ],
        "referrerState": {
            "stage": "ready",
            "data": {
                "code": "TEST",
                "referralStates": [
                    {
                        "cumVlm": "960652.017122",
                        "cumRewardedFeesSinceReferred": "196.838825",
                        "cumFeesRewardedToReferrer": "19.683748",
                        "timeJoined": 1679425029416,
                        "user": "0x11af2b93dcb3568b7bf2b6bd6182d260a9495728"
                    },
                    {
                        "cumVlm": "438278.672653",
                        "cumRewardedFeesSinceReferred": "97.628107",
                        "cumFeesRewardedToReferrer": "9.762562",
                        "timeJoined": 1679423947882,
                        "user": "0x3f69d170055913103a034a418953b8695e4e42fa"
                    }
                ]
            }
        },
        "rewardHistory": []
    }

Copy
    
    
    {
      "dailyUserVlm": [
        {
          "date": "2025-05-23",
          "userCross": "0.0",
          "userAdd": "0.0",
          "exchange": "2852367.0770729999"
        },
        ...
      ],
      "feeSchedule": {
        "cross": "0.00045",
        "add": "0.00015",
        "spotCross": "0.0007",
        "spotAdd": "0.0004",
        "tiers": {
          "vip": [
            {
              "ntlCutoff": "5000000.0",
              "cross": "0.0004",
              "add": "0.00012",
              "spotCross": "0.0006",
              "spotAdd": "0.0003"
            },
            ...
          ],
          "mm": [
            {
              "makerFractionCutoff": "0.005",
              "add": "-0.00001"
            },
            ...
          ]
        },
        "referralDiscount": "0.04",
        "stakingDiscountTiers": [
          {
            "bpsOfMaxSupply": "0.0",
            "discount": "0.0"
          },
          {
            "bpsOfMaxSupply": "0.0001",
            "discount": "0.05"
          },
          ...
        ]
      },
      "userCrossRate": "0.000315",
      "userAddRate": "0.000105",
      "userSpotCrossRate": "0.00049",
      "userSpotAddRate": "0.00028",
      "activeReferralDiscount": "0.0",
      "trial": null,
      "feeTrialReward": "0.0",
      "nextTrialAvailableTimestamp": null,
      "stakingLink": {
        "type": "tradingUser",
        "stakingUser": "0x54c049d9c7d3c92c2462bf3d28e083f3d6805061"
      },
      "activeStakingDiscount": {
        "bpsOfMaxSupply": "4.7577998927",
        "discount": "0.3"
      }
    }

Copy
    
    
    [
        {
            "validator":"0x5ac99df645f3414876c816caa18b2d234024b487",
            "amount":"12060.16529862",
            "lockedUntilTimestamp":1735466781353
        },
        ...
    ]

Copy
    
    
    {
        "delegated": "12060.16529862",
        "undelegated": "0.0",
        "totalPendingWithdrawal": "0.0",
        "nPendingWithdrawals": 0
    }

Copy
    
    
    [
        {
            "time": 1735380381353,
            "hash": "0x55492465cb523f90815a041a226ba90147008d4b221a24ae8dc35a0dbede4ea4",
            "delta": {
                "delegate": {
                    "validator": "0x5ac99df645f3414876c816caa18b2d234024b487",
                    "amount": "10000.0",
                    "isUndelegate": false
                }
            }
        },
        ...
    ]

Copy
    
    
    [
        {
            "time": 1736726400073,
            "source": "delegation",
            "totalAmount": "0.73117184"
        },
        {
            "time": 1736726400073,
            "source": "commission",
            "totalAmount": "130.76445876"
        },
        ...
    ]

Copy
    
    
    true

Copy
    
    
    "unifiedAccount" | "portfolioMargin" | "disabled" | "default" | "dexAbstraction"

Copy
    
    
    {
        "isAligned": true,
        "firstAlignedTime": 1758949452538,
        "evmMintedSupply": "0.0",
        "dailyAmountOwed": [
            [
                "2025-10-04",
                "0.0"
            ],
            [
                "2025-10-05",
                "0.0"
            ],
            ...
        ],
        "predictedRate": "0.01"
    }
    

Copy
    
    
    {
        "tokenToState":[
            [
                0,
                {
                    "borrow":{
                        "basis": "0.0",
                        "value": "0.0"
                    },
                    "supply":{
                        "basis": "44.69295862",
                        "value": "44.69692314"
                    }
                }
            ],
            [
                1105,
                {
                    "borrow":{
                        "basis": "0.0",
                        "value": "0.0"
                    },
                    "supply":{
                        "basis": "0.0",
                        "value": "0.0"
                    }
                }
            ],
        ],
        "health":"healthy",
        "healthFactor":null
    }

Copy
    
    
    {
        "borrowYearlyRate": "0.05",
        "supplyYearlyRate": "0.0008245002",
        "balance": "3245939.4732256099",
        "utilization": "0.018322226",
        "oraclePx": "1.0",
        "ltv": "0.0",
        "totalSupplied": "3306509.7335290499",
        "totalBorrowed": "60582.61869494"
    }

Copy
    
    
    [
        [
            0,
            {
                "borrowYearlyRate": "0.05",
                "supplyYearlyRate": "0.0008244951",
                "balance": "3245960.0596176102",
                "utilization": "0.0183221137",
                "oraclePx": "1.0",
                "ltv": "0.0",
                "totalSupplied": "3306530.3251102199",
                "totalBorrowed": "60582.62446067"
            }
        ],
        [
            150,
            {
                "borrowYearlyRate": "0.05",
                "supplyYearlyRate": "0.0",
                "balance": "11318.09684696",
                "utilization": "0.0",
                "oraclePx": "23.99",
                "ltv": "0.5",
                "totalSupplied": "11318.09684696",
                "totalBorrowed": "0.0"
            }
        ]
    ]

Copy
    
    
    ["0x476fa87b4d3818f437f38f1263bee508d7672d82"]


---

# Source: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint

bars[Hyperliquid Docs](/hyperliquid-docs)

search

circle-xmark

`⌘Ctrl``k`

  * [Hyperliquid Docs](/hyperliquid-docs)
  * [Builder Tools](/hyperliquid-docs/builder-tools)
  * [Support](/hyperliquid-docs/support)



chevron-leftchevron-right

[Hyperliquid Docs](/hyperliquid-docs)

  * [About Hyperliquidchevron-right](/hyperliquid-docs)
  * [Onboardingchevron-right](/hyperliquid-docs/onboarding)
  * [HyperCorechevron-right](/hyperliquid-docs/hypercore)
  * [HyperEVMchevron-right](/hyperliquid-docs/hyperevm)
  * [Hyperliquid Improvement Proposals (HIPs)chevron-right](/hyperliquid-docs/hyperliquid-improvement-proposals-hips)
  * [Tradingchevron-right](/hyperliquid-docs/trading)
  * [Validatorschevron-right](/hyperliquid-docs/validators)
  * [Referralschevron-right](/hyperliquid-docs/referrals)
  * [Points](/hyperliquid-docs/points)
  * [Historical data](/hyperliquid-docs/historical-data)
  * [Risks](/hyperliquid-docs/risks)
  * [Bug bounty program](/hyperliquid-docs/bug-bounty-program)
  * [Audits](/hyperliquid-docs/audits)
  * [Brand kit](/hyperliquid-docs/brand-kit)
  * For developers

    * [APIchevron-right](/hyperliquid-docs/for-developers/api)

      * [Notation](/hyperliquid-docs/for-developers/api/notation)
      * [Asset IDs](/hyperliquid-docs/for-developers/api/asset-ids)
      * [Tick and lot size](/hyperliquid-docs/for-developers/api/tick-and-lot-size)
      * [Nonces and API wallets](/hyperliquid-docs/for-developers/api/nonces-and-api-wallets)
      * [Info endpointchevron-right](/hyperliquid-docs/for-developers/api/info-endpoint)
      * [Exchange endpoint](/hyperliquid-docs/for-developers/api/exchange-endpoint)
      * [Websocketchevron-right](/hyperliquid-docs/for-developers/api/websocket)
      * [Error responses](/hyperliquid-docs/for-developers/api/error-responses)
      * [Signing](/hyperliquid-docs/for-developers/api/signing)
      * [Rate limits and user limits](/hyperliquid-docs/for-developers/api/rate-limits-and-user-limits)
      * [Activation gas fee](/hyperliquid-docs/for-developers/api/activation-gas-fee)
      * [Optimizing latency](/hyperliquid-docs/for-developers/api/optimizing-latency)
      * [Bridge2](/hyperliquid-docs/for-developers/api/bridge2)
      * [Deploying HIP-1 and HIP-2 assets](/hyperliquid-docs/for-developers/api/deploying-hip-1-and-hip-2-assets)
      * [HIP-3 deployer actions](/hyperliquid-docs/for-developers/api/hip-3-deployer-actions)

    * [HyperEVMchevron-right](/hyperliquid-docs/for-developers/hyperevm)
    * [Nodeschevron-right](/hyperliquid-docs/for-developers/nodes)



chevron-upchevron-down

[gitbookPowered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=yUdp569E6w18GdfqlGvJ)

xmark

block-quoteOn this pagechevron-down

copyCopychevron-down

  1. [For developers](/hyperliquid-docs/for-developers)chevron-right
  2. [API](/hyperliquid-docs/for-developers/api)



# Exchange endpoint

The exchange endpoint is used to interact with and trade on the Hyperliquid chain. See the Python SDK for code to generate signatures for these requests.

### 

[hashtag](#asset)

Asset

Many of the requests take asset as an input. For perpetuals this is the index in the `universe` field returned by the`meta` response. For spot assets, use `10000 + index` where `index` is the corresponding index in `spotMeta.universe`. For example, when submitting an order for `PURR/USDC`, the asset that should be used is `10000` because its asset index in the spot metadata is `0`.

### 

[hashtag](#subaccounts-and-vaults)

Subaccounts and vaults

Subaccounts and vaults do not have private keys. To perform actions on behalf of a subaccount or vault signing should be done by the master account and the vaultAddress field should be set to the address of the subaccount or vault. The basic_vault.py example in the Python SDK demonstrates this.

### 

[hashtag](#expires-after)

Expires After

Some actions support an optional field `expiresAfter` which is a timestamp in milliseconds after which the action will be rejected. User-signed actions such as Core USDC transfer do not support the `expiresAfter` field. Note that actions consume 5x the usual address-based rate limit when canceled due to a stale `expiresAfter` field. 

See the Python SDK for details on how to incorporate this field when signing. 

## 

[hashtag](#place-an-order)

Place an order

`POST` `https://api.hyperliquid.xyz/exchange`

See Python SDK for full featured examples on the fields of the order request.

For limit orders, TIF (time-in-force) sets the behavior of the order upon first hitting the book.

ALO (add liquidity only, i.e. "post only") will be canceled instead of immediately matching.

IOC (immediate or cancel) will have the unfilled part canceled instead of resting.

GTC (good til canceled) orders have no special behavior.

Client Order ID (cloid) is an optional 128 bit hex string, e.g. `0x1234567890abcdef1234567890abcdef`

#### 

[hashtag](#headers)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body)

Request Body

Name

Type

Description

action*

Object

{

"type": "order", "orders": [{

"a": Number,

"b": Boolean,

"p": String,

"s": String,

"r": Boolean,

"t": {

"limit": {

"tif": "Alo" | "Ioc" | "Gtc"

} or

"trigger": {

"isMarket": Boolean,

"triggerPx": String,

"tpsl": "tp" | "sl"

}

},

"c": Cloid (optional)

}],

"grouping": "na" | "normalTpsl" | "positionTpsl",

"builder": Optional({"b": "address", "f": Number})

} Meaning of keys: a is asset b is isBuy p is price s is size r is reduceOnly t is type c is cloid (client order id) Meaning of keys in optional builder argument: b is the address the should receive the additional fee f is the size of the fee in tenths of a basis point e.g. if f is 10, 1bp of the order notional will be charged to the user and sent to the builder

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response (resting)

200: OK Error Response

200: OK Successful Response (filled)

## 

[hashtag](#cancel-order-s)

Cancel order(s)

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-1)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-1)

Request Body

Name

Type

Description

action*

Object

{

"type": "cancel",

"cancels": [

{

"a": Number,

"o": Number

}

]

} Meaning of keys: a is asset o is oid (order id)

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

200: OK Error Response

## 

[hashtag](#cancel-order-s-by-cloid)

Cancel order(s) by cloid

`POST` `https://api.hyperliquid.xyz/exchange `

#### 

[hashtag](#headers-2)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-2)

Request Body

Name

Type

Description

action*

Object

{

"type": "cancelByCloid",

"cancels": [

{

"asset": Number,

"cloid": String

}

]

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

200: OK Error Response

## 

[hashtag](#schedule-cancel-dead-mans-switch)

Schedule cancel (dead man's switch)

`POST` `https://api.hyperliquid.xyz/exchange `

#### 

[hashtag](#headers-3)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-3)

Request Body

Name

Type

Description

action*

Object

{

"type": "scheduleCancel",

"time": number (optional)

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

Schedule a cancel-all operation at a future time. Not including time will remove the scheduled cancel operation. The time must be at least 5 seconds after the current time. Once the time comes, all open orders will be canceled and a trigger count will be incremented. The max number of triggers per day is 10. This trigger count is reset at 00:00 UTC.

## 

[hashtag](#modify-an-order)

Modify an order

`POST` `https://api.hyperliquid.xyz/exchange `

#### 

[hashtag](#headers-4)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-4)

Request Body

Name

Type

Description

action*

Object

{

"type": "modify",

"oid": Number | Cloid,

"order": {

"a": Number,

"b": Boolean,

"p": String,

"s": String,

"r": Boolean,

"t": {

"limit": {

"tif": "Alo" | "Ioc" | "Gtc"

} or

"trigger": {

"isMarket": Boolean,

"triggerPx": String,

"tpsl": "tp" | "sl"

}

},

"c": Cloid (optional)

}

} Meaning of keys: a is asset b is isBuy p is price s is size r is reduceOnly t is type c is cloid (client order id)

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

200: OK Error Response

## 

[hashtag](#modify-multiple-orders)

Modify multiple orders

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-5)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-5)

Request Body

Name

Type

Description

action*

Object

{

"type": "batchModify",

"modifies": [{

"oid": Number | Cloid,

"order": {

"a": Number,

"b": Boolean,

"p": String,

"s": String,

"r": Boolean,

"t": {

"limit": {

"tif": "Alo" | "Ioc" | "Gtc"

} or

"trigger": {

"isMarket": Boolean,

"triggerPx": String,

"tpsl": "tp" | "sl"

}

},

"c": Cloid (optional)

}

}]

} Meaning of keys: a is asset b is isBuy p is price s is size r is reduceOnly t is type c is cloid (client order id)

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

## 

[hashtag](#update-leverage)

Update leverage

`POST` `https://api.hyperliquid.xyz/exchange`

Update cross or isolated leverage on a coin. 

#### 

[hashtag](#headers-6)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-6)

Request Body

Name

Type

Description

action*

Object

{

"type": "updateLeverage",

"asset": index of coin,

"isCross": true or false if updating cross-leverage,

"leverage": integer representing new leverage, subject to leverage constraints on that coin

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful response

## 

[hashtag](#update-isolated-margin)

Update isolated margin

`POST` `https://api.hyperliquid.xyz/exchange`

Add or remove margin from isolated position

Note that to target a specific leverage instead of a USDC value of margin change, there is an alternate action `{"type": "topUpIsolatedOnlyMargin", "asset": <asset>, "leverage": <float string>}`

#### 

[hashtag](#headers-7)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-7)

Request Body

Name

Type

Description

action*

Object

{

"type": "updateIsolatedMargin",

"asset": index of coin,

"isBuy": true, (this parameter won't have any effect until hedge mode is introduced)

"ntli": int representing amount to add or remove with 6 decimals, e.g. 1000000 for 1 usd,

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful response

## 

[hashtag](#core-usdc-transfer)

Core USDC transfer

`POST` `https://api.hyperliquid.xyz/exchange`

Send usd to another address. This transfer does not touch the EVM bridge. The signature format is human readable for wallet interfaces.

#### 

[hashtag](#headers-8)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-8)

Request Body

Name

Type

Description

action*

Object

{

"type": "usdSend",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"destination": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000,

"amount": amount of usd to send as a string, e.g. "1" for 1 usd,

"time": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#core-spot-transfer)

Core spot transfer

`POST` `https://api.hyperliquid.xyz/exchange`

Send spot assets to another address. This transfer does not touch the EVM bridge. The signature format is human readable for wallet interfaces.

#### 

[hashtag](#headers-9)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-9)

Request Body

Name

Type

Description

action*

Object

{

"type": "spotSend",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"destination": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000, "token": tokenName:tokenId; e.g. "PURR:0xc4bf3f870c0e9465323c0b6ed28096c2",

"amount": amount of token to send as a string, e.g. "0.01",

"time": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#initiate-a-withdrawal-request)

Initiate a withdrawal request

`POST` `https://api.hyperliquid.xyz/exchange`

This method is used to initiate the withdrawal flow. After making this request, the L1 validators will sign and send the withdrawal request to the bridge contract. There is a $1 fee for withdrawing at the time of this writing and withdrawals take approximately 5 minutes to finalize.

#### 

[hashtag](#headers-10)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-10)

Request Body

Name

Type

Description

action*

Object

{ "type": "withdraw3",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"amount": amount of usd to send as a string, e.g. "1" for 1 usd,

"time": current timestamp in milliseconds as a Number, should match nonce,

"destination": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

200: OK 

## 

[hashtag](#transfer-from-spot-account-to-perp-account-and-vice-versa)

Transfer from Spot account to Perp account (and vice versa)

`POST` `https://api.hyperliquid.xyz/exchange`

This method is used to transfer USDC from the user's spot wallet to perp wallet and vice versa.

**Headers**

Name

Value

Content-Type*

"application/json"

**Body**

Name

Type

Description

action*

Object

{

"type": "usdClassTransfer",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"amount": amount of usd to transfer as a string, e.g. "1" for 1 usd. If you want to use this action for a subaccount, you can include subaccount: address after the amount, e.g. "1" subaccount:0x0000000000000000000000000000000000000000,

"toPerp": true if (spot -> perp) else false,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

**Response**

200: OK

## 

[hashtag](#send-asset)

Send Asset

`POST` `https://api.hyperliquid.xyz/exchange`

This generalized method is used to transfer tokens between different perp DEXs, spot balance, users, and/or sub-accounts. Use "" to specify the default USDC perp DEX and "spot" to specify spot. Only the collateral token can be transferred to or from a perp DEX.

#### 

[hashtag](#headers-11)

Headers

Name

Value

Content-Type*

`application/json`

#### 

[hashtag](#body)

Body

Name

Type

Description

action*

Object

{

"type": "sendAsset",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead),

"signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"destination": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000,

"sourceDex": name of perp dex to transfer from,

"destinationDex": name of the perp dex to transfer to,

"token": tokenName:tokenId; e.g. "PURR:0xc4bf3f870c0e9465323c0b6ed28096c2",

"amount": amount of token to send as a string; e.g. "0.01",

"fromSubAccount": address in 42-character hexadecimal format or empty string if not from a subaccount,

"nonce": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

#### 

[hashtag](#response)

Response

200: OK

## 

[hashtag](#send-to-evm-with-data)

Send to EVM with data

`POST` `https://api.hyperliquid.xyz/exchange`

Specialized action for Core to EVM transfer that includes an additional data payload. See [HyperCore <> HyperEVM transfers](/hyperliquid-docs/for-developers/hyperevm/hypercore-less-than-greater-than-hyperevm-transfers) for more details. When used coreReceiveWithData will be called on the linked contract instead of transfer. IMPORTANT: it is the caller's responsibility to ensure that the token is properly linked and the linked contract supports the following interface: 

#### 

[hashtag](#headers-12)

Headers

Name

Value

Content-Type*

`application/json`

#### 

[hashtag](#body-1)

Body

Name

Type

Description

action*

Object

{

"type": "sendToEvmWithData",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead),

"signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"token": tokenName:tokenId; e.g. "PURR:0xc4bf3f870c0e9465323c0b6ed28096c2",

"amount": amount of token to send as a string; e.g. "0.01",

"sourceDex": name of perp dex to transfer from,

"destinationRecipient": address in addressEncoding format,

"addressEncoding": "hex" | "base58",

"destinationChainId": number,

"gasLimit": number,

"data": bytes,

"nonce": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

#### 

[hashtag](#response-1)

Response

200: OK

## 

[hashtag](#deposit-into-staking)

Deposit into staking

`POST` `https://api.hyperliquid.xyz/exchange`

This method is used to transfer native token from the user's spot account into staking for delegating to validators. 

#### 

[hashtag](#headers-13)

Headers

Name

Value

Content-Type*

`application/json`

#### 

[hashtag](#body-2)

Body

Name

Type

Description

action*

Object

{

"type": "cDeposit",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"wei": amount of wei to transfer as a number,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

#### 

[hashtag](#response-2)

Response

200: OK

## 

[hashtag](#withdraw-from-staking)

Withdraw from staking

`POST` `https://api.hyperliquid.xyz/exchange`

This method is used to transfer native token from staking into the user's spot account. Note that transfers from staking to spot account go through a 7 day unstaking queue.

#### 

[hashtag](#headers-14)

Headers

Name

Value

Content-Type*

`application/json`

#### 

[hashtag](#body-3)

Body

Name

Type

Description

action*

Object

{

"type": "cWithdraw",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"wei": amount of wei to transfer as a number,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

Number

Recommended to use the current timestamp in milliseconds, must match the nonce in the action Object above

signature*

Object

#### 

[hashtag](#response-3)

Response

200: OK

## 

[hashtag](#delegate-or-undelegate-stake-from-validator)

Delegate or undelegate stake from validator

`POST` `https://api.hyperliquid.xyz/exchange`

Delegate or undelegate native tokens to or from a validator. Note that delegations to a particular validator have a lockup duration of 1 day.

#### 

[hashtag](#headers-15)

Headers

Name

Value

Content-Type*

`application/json`

#### 

[hashtag](#body-4)

Body

Name

Type

Description

action*

Object

{

"type": "tokenDelegate",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"validator": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000, "isUndelegate": boolean,

"wei": number,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

number

Recommended to use the current timestamp in milliseconds

signature*

Object

#### 

[hashtag](#response-4)

Response

200: OK

## 

[hashtag](#deposit-or-withdraw-from-a-vault)

Deposit or withdraw from a vault

`POST` `https://api.hyperliquid.xyz/exchange`

Add or remove funds from a vault.

**Headers**

Name

Value

Content-Type*

`application/json`

**Body**

Name

Type

Description

action*

Object

{

"type": "vaultTransfer",

"vaultAddress": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000, "isDeposit": boolean,

"usd": number

}

nonce*

number

Recommended to use the current timestamp in milliseconds

signature*

Object

expiresAfter

Number

Timestamp in milliseconds

**Response**

200

## 

[hashtag](#approve-an-api-wallet)

Approve an API wallet

`POST` `https://api.hyperliquid.xyz/exchange`

Approves an API Wallet (also sometimes referred to as an Agent Wallet). See [herearrow-up-right](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/nonces-and-api-wallets#api-wallets) for more details.

**Headers**

Name

Value

Content-Type*

`application/json`

**Body**

Name

Type

Description

action*

Object

{ "type": "approveAgent",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"agentAddress": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000,

"agentName": Optional name for the API wallet. An account can have 1 unnamed approved wallet and up to 3 named ones. And additional 2 named agents are allowed per subaccount,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

number

Recommended to use the current timestamp in milliseconds

signature*

Object

**Response**

200

## 

[hashtag](#approve-a-builder-fee)

Approve a builder fee

`POST` `https://api.hyperliquid.xyz/exchange`

Approve a maximum fee rate for a builder.

**Headers**

Name

Value

Content-Type*

`application/json`

**Body**

Name

Type

Description

action*

Object

{ "type": "approveBuilderFee",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead), "signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"maxFeeRate": the maximum allowed builder fee rate as a percent string; e.g. "0.001%",

"builder": address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000,

"nonce": current timestamp in milliseconds as a Number, must match nonce in outer request body

}

nonce*

number

Recommended to use the current timestamp in milliseconds

signature*

Object

**Response**

200

## 

[hashtag](#place-a-twap-order)

Place a TWAP order

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-16)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-11)

Request Body

Name

Type

Description

action*

Object

{

"type": "twapOrder", "twap": {

"a": Number,

"b": Boolean,

"s": String,

"r": Boolean,

"m": Number,

"t": Boolean

}

} Meaning of keys: a is asset b is isBuy s is size r is reduceOnly

m is minutes t is randomize

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its Onchain address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

200: OK Error Response

## 

[hashtag](#cancel-a-twap-order)

Cancel a TWAP order

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-17)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-12)

Request Body

Name

Type

Description

action*

Object

{

"type": "twapCancel",

"a": Number,

"t": Number

} Meaning of keys: a is asset t is twap_id

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

vaultAddress

String

If trading on behalf of a vault or subaccount, its address in 42-character hexadecimal format; e.g. 0x0000000000000000000000000000000000000000

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

200: OK Error Response

## 

[hashtag](#reserve-additional-actions)

Reserve Additional Actions

`POST` `https://api.hyperliquid.xyz/exchange`

Instead of trading to increase the address based rate limits, this action allows reserving additional actions for 0.0005 USDC per request. The cost is paid from the Perps balance. 

#### 

[hashtag](#headers-18)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-13)

Request Body

Name

Type

Description

action*

Object

{

"type": "reserveRequestWeight",

"weight": Number

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

## 

[hashtag](#invalidate-pending-nonce-noop)

Invalidate Pending Nonce (noop)

`POST` `https://api.hyperliquid.xyz/exchange`

This action does not do anything (no operation), but causes the nonce to be marked as used. This can be a more effective way to cancel in-flight orders than the cancel action.

#### 

[hashtag](#headers-19)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-14)

Request Body

Name

Type

Description

action*

Object

{

"type": "noop"

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

expiresAfter

Number

Timestamp in milliseconds

200: OK Successful Response

## 

[hashtag](#enable-hip-3-dex-abstraction)

Enable HIP-3 DEX abstraction

`POST` `https://api.hyperliquid.xyz/exchange`

NOTE: deprecrated. Prefer `userSetAbstraction`. 

If set, actions on HIP-3 perps will automatically transfer collateral from validator-operated USDC perps balance for HIP-3 DEXs where USDC is the collateral token, and spot otherwise. When HIP-3 DEX abstraction is active, collateral is returned to the same source (validator-operated USDC perps or spot balance) when released from positions or open orders.

#### 

[hashtag](#headers-20)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-15)

Request Body

Name

Type

Description

action*

Object

{

"type": "userDexAbstraction",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead),

"signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"user": address in 42-character hexadecimal format. Can be a sub-account of the user,

"enabled": boolean,

"nonce": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#enable-hip-3-dex-abstraction-agent)

Enable HIP-3 DEX abstraction (agent)

NOTE: deprecrated. Prefer `agentSetAbstraction`. 

Same effect as UserDexAbstraction above, but only works if setting the value from `null` to `true`.

#### 

[hashtag](#headers-21)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-16)

Request Body

Name

Type

Description

action*

Object

{

"type": "agentEnableDexAbstraction"

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#set-user-abstraction)

Set User Abstraction

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-22)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-17)

Request Body

Name

Type

Description

action*

Object

{

"type": "userSetAbstraction",

"hyperliquidChain": "Mainnet" (on testnet use "Testnet" instead),

"signatureChainId": the id of the chain used when signing in hexadecimal format; e.g. "0xa4b1" for Arbitrum,

"user": address in 42-character hexadecimal format. Can be a sub-account of the user,

"abstraction": one of the strings ["disabled", "unifiedAccount", "portfolioMargin"],

"nonce": current timestamp in milliseconds as a Number, should match nonce

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#set-user-abstraction-agent)

Set User Abstraction (agent)

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-23)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-18)

Request Body

Name

Type

Description

action*

Object

{

"type": "agentSetAbstraction",

"abstraction": one of the strings ["i", "u", "p"] where "i" is "disabled", "u" is "unifiedAccount", and "p" is "portfolioMargin"

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

## 

[hashtag](#validator-vote-on-risk-free-rate-for-aligned-quote-asset)

Validator vote on risk-free rate for aligned quote asset

`POST` `https://api.hyperliquid.xyz/exchange`

#### 

[hashtag](#headers-24)

Headers

Name

Type

Description

Content-Type*

String

"application/json"

#### 

[hashtag](#request-body-19)

Request Body

Name

Type

Description

action*

Object

{

"type": "validatorL1Stream",

"riskFreeRate": String // e.g. "0.04" for 4% 

}

nonce*

Number

Recommended to use the current timestamp in milliseconds

signature*

Object

200: OK Successful Response

[PreviousSpotchevron-left](/hyperliquid-docs/for-developers/api/info-endpoint/spot)[NextWebsocketchevron-right](/hyperliquid-docs/for-developers/api/websocket)

Last updated 16 days ago

  * [Asset](#asset)
  * [Subaccounts and vaults](#subaccounts-and-vaults)
  * [Expires After](#expires-after)
  * [Place an order](#place-an-order)
  * [Cancel order(s)](#cancel-order-s)
  * [Cancel order(s) by cloid](#cancel-order-s-by-cloid)
  * [Schedule cancel (dead man's switch)](#schedule-cancel-dead-mans-switch)
  * [Modify an order](#modify-an-order)
  * [Modify multiple orders](#modify-multiple-orders)
  * [Update leverage](#update-leverage)
  * [Update isolated margin](#update-isolated-margin)
  * [Core USDC transfer](#core-usdc-transfer)
  * [Core spot transfer](#core-spot-transfer)
  * [Initiate a withdrawal request](#initiate-a-withdrawal-request)
  * [Transfer from Spot account to Perp account (and vice versa)](#transfer-from-spot-account-to-perp-account-and-vice-versa)
  * [Send Asset](#send-asset)
  * [Send to EVM with data](#send-to-evm-with-data)
  * [Deposit into staking](#deposit-into-staking)
  * [Withdraw from staking](#withdraw-from-staking)
  * [Delegate or undelegate stake from validator](#delegate-or-undelegate-stake-from-validator)
  * [Deposit or withdraw from a vault](#deposit-or-withdraw-from-a-vault)
  * [Approve an API wallet](#approve-an-api-wallet)
  * [Approve a builder fee](#approve-a-builder-fee)
  * [Place a TWAP order](#place-a-twap-order)
  * [Cancel a TWAP order](#cancel-a-twap-order)
  * [Reserve Additional Actions](#reserve-additional-actions)
  * [Invalidate Pending Nonce (noop)](#invalidate-pending-nonce-noop)
  * [Enable HIP-3 DEX abstraction](#enable-hip-3-dex-abstraction)
  * [Enable HIP-3 DEX abstraction (agent)](#enable-hip-3-dex-abstraction-agent)
  * [Set User Abstraction](#set-user-abstraction)
  * [Set User Abstraction (agent)](#set-user-abstraction-agent)
  * [Validator vote on risk-free rate for aligned quote asset](#validator-vote-on-risk-free-rate-for-aligned-quote-asset)



Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"order",
          "data":{
             "statuses":[
                {
                   "resting":{
                      "oid":77738308
                   }
                }
             ]
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"order",
          "data":{
             "statuses":[
                {
                   "error":"Order must have minimum value of $10."
                }
             ]
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"order",
          "data":{
             "statuses":[
                {
                   "filled":{
                      "totalSz":"0.02",
                      "avgPx":"1891.4",
                      "oid":77747314
                   }
                }
             ]
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"cancel",
          "data":{
             "statuses":[
                "success"
             ]
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"cancel",
          "data":{
             "statuses":[
                {
                   "error":"Order was never placed, already canceled, or filled."
                }
             ]
          }
       }
    }

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    Example sign typed data for generating the signature:
    {
      "types": {
        "HyperliquidTransaction:SpotSend": [
          {
            "name": "hyperliquidChain",
            "type": "string"
          },
          {
            "name": "destination",
            "type": "string"
          },
          {
            "name": "token",
            "type": "string"
          },
          {
            "name": "amount",
            "type": "string"
          },
          {
            "name": "time",
            "type": "uint64"
          }
        ]
      },
      "primaryType": "HyperliquidTransaction:SpotSend",
      "domain": {
        "name": "HyperliquidSignTransaction",
        "version": "1",
        "chainId": 42161,
        "verifyingContract": "0x0000000000000000000000000000000000000000"
      },
      "message": {
        "destination": "0x0000000000000000000000000000000000000000",
        "token": "PURR:0xc1fb593aeffbeb02f85e0308e9956a90",
        "amount": "0.1",
        "time": 1716531066415,
        "hyperliquidChain": "Mainnet"
      }
    }

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    interface ICoreReceiveWithData {
      function coreReceiveWithData(
        address from,
        bytes32 destinationRecipient,
        uint32 destinationChainId,
        uint256 amount,
        uint64 nonce,
        bytes calldata data
      ) external;
    }

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"twapOrder",
          "data":{
             "status": {
                "running":{
                   "twapId":77738308
                }
             }
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"twapOrder",
          "data":{
             "status": {
                "error":"Invalid TWAP duration: 1 min(s)"
             }
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"twapCancel",
          "data":{
             "status": "success"
          }
       }
    }

Copy
    
    
    {
       "status":"ok",
       "response":{
          "type":"twapCancel",
          "data":{
             "status": {
                "error": "TWAP was never placed, already canceled, or filled."
             }
          }
       }
    }

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}

Copy
    
    
    {'status': 'ok', 'response': {'type': 'default'}}


---

# Source: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket

bars[Hyperliquid Docs](/hyperliquid-docs)

search

circle-xmark

`⌘Ctrl``k`

  * [Hyperliquid Docs](/hyperliquid-docs)
  * [Builder Tools](/hyperliquid-docs/builder-tools)
  * [Support](/hyperliquid-docs/support)



chevron-leftchevron-right

[Hyperliquid Docs](/hyperliquid-docs)

  * [About Hyperliquidchevron-right](/hyperliquid-docs)
  * [Onboardingchevron-right](/hyperliquid-docs/onboarding)
  * [HyperCorechevron-right](/hyperliquid-docs/hypercore)
  * [HyperEVMchevron-right](/hyperliquid-docs/hyperevm)
  * [Hyperliquid Improvement Proposals (HIPs)chevron-right](/hyperliquid-docs/hyperliquid-improvement-proposals-hips)
  * [Tradingchevron-right](/hyperliquid-docs/trading)
  * [Validatorschevron-right](/hyperliquid-docs/validators)
  * [Referralschevron-right](/hyperliquid-docs/referrals)
  * [Points](/hyperliquid-docs/points)
  * [Historical data](/hyperliquid-docs/historical-data)
  * [Risks](/hyperliquid-docs/risks)
  * [Bug bounty program](/hyperliquid-docs/bug-bounty-program)
  * [Audits](/hyperliquid-docs/audits)
  * [Brand kit](/hyperliquid-docs/brand-kit)
  * For developers

    * [APIchevron-right](/hyperliquid-docs/for-developers/api)

      * [Notation](/hyperliquid-docs/for-developers/api/notation)
      * [Asset IDs](/hyperliquid-docs/for-developers/api/asset-ids)
      * [Tick and lot size](/hyperliquid-docs/for-developers/api/tick-and-lot-size)
      * [Nonces and API wallets](/hyperliquid-docs/for-developers/api/nonces-and-api-wallets)
      * [Info endpointchevron-right](/hyperliquid-docs/for-developers/api/info-endpoint)
      * [Exchange endpoint](/hyperliquid-docs/for-developers/api/exchange-endpoint)
      * [Websocketchevron-right](/hyperliquid-docs/for-developers/api/websocket)

        * [Subscriptions](/hyperliquid-docs/for-developers/api/websocket/subscriptions)
        * [Post requests](/hyperliquid-docs/for-developers/api/websocket/post-requests)
        * [Timeouts and heartbeats](/hyperliquid-docs/for-developers/api/websocket/timeouts-and-heartbeats)

      * [Error responses](/hyperliquid-docs/for-developers/api/error-responses)
      * [Signing](/hyperliquid-docs/for-developers/api/signing)
      * [Rate limits and user limits](/hyperliquid-docs/for-developers/api/rate-limits-and-user-limits)
      * [Activation gas fee](/hyperliquid-docs/for-developers/api/activation-gas-fee)
      * [Optimizing latency](/hyperliquid-docs/for-developers/api/optimizing-latency)
      * [Bridge2](/hyperliquid-docs/for-developers/api/bridge2)
      * [Deploying HIP-1 and HIP-2 assets](/hyperliquid-docs/for-developers/api/deploying-hip-1-and-hip-2-assets)
      * [HIP-3 deployer actions](/hyperliquid-docs/for-developers/api/hip-3-deployer-actions)

    * [HyperEVMchevron-right](/hyperliquid-docs/for-developers/hyperevm)
    * [Nodeschevron-right](/hyperliquid-docs/for-developers/nodes)



chevron-upchevron-down

[gitbookPowered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=yUdp569E6w18GdfqlGvJ)

xmark

block-quoteOn this pagechevron-down

copyCopychevron-down

  1. [For developers](/hyperliquid-docs/for-developers)chevron-right
  2. [API](/hyperliquid-docs/for-developers/api)



# Websocket

WebSocket endpoints are available for real-time data streaming and as an alternative to HTTP request sending on the Hyperliquid exchange. The WebSocket URLs by network are:

  * Mainnet: `wss://api.hyperliquid.xyz/ws`

  * Testnet: `wss://api.hyperliquid-testnet.xyz/ws`.




### 

[hashtag](#connecting)

Connecting

To connect to the WebSocket API, establish a WebSocket connection to the respective URL based on the desired network. Once connected, you can start sending subscription messages to receive real-time data updates.

Example from command line:

Copy
    
    
    $ wscat -c  wss://api.hyperliquid.xyz/ws
    Connected (press CTRL+C to quit)
    >  { "method": "subscribe", "subscription": { "type": "trades", "coin": "SOL" } }
    < {"channel":"subscriptionResponse","data":{"method":"subscribe","subscription":{"type":"trades","coin":"SOL"}}}

Important: all automated users should handle disconnects from the server side and gracefully reconnect. Disconnection from API servers may happen periodically and without announcement. Missed data during the reconnect will be present in the snapshot ack on reconnect. Users can also manually query any missed data using the corresponding info request.

Note: this doc uses Typescript for defining many of the message types. The python SDK also has examples [herearrow-up-right](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/hyperliquid/utils/types.py) and example connection code [herearrow-up-right](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/hyperliquid/websocket_manager.py).

[PreviousExchange endpointchevron-left](/hyperliquid-docs/for-developers/api/exchange-endpoint)[NextSubscriptionschevron-right](/hyperliquid-docs/for-developers/api/websocket/subscriptions)

Last updated 1 month ago
