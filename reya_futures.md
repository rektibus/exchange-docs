# Rest API Reference

**Base URL**: `https://api.reya.xyz/v2`

## Overview

The Reya DEX REST API v2 provides programmatic access to the Reya Perpetual Exchange, enabling traders to interact with the platform algorithmically. This API is designed for developers and professional traders who want to build automated trading systems, integrate with existing platforms, or develop custom interfaces for the Reya DEX ecosystem.

## Key Features

* **Market Data**: Access comprehensive market information, including asset definitions, market summaries, and real-time price data
* **Order Management**: Create, cancel, and monitor orders with support for various order types (limit, trigger)
* **Position Tracking**: Monitor your current positions and historical executions
* **Wallet Integration**: Manage wallet configurations and access wallet-specific data
* **Price Data**: Access historical price data with customizable time intervals through candle endpoints

## API Structure

The API is organized into several logical sections:

* **Reference Data**:  Discover markets and assets definitions, trading fees
* **Market Data**: Access real-time and historical market data, including prices, candles and order execution
* **Wallet Data**: Get information about the wallet's accounts, positions and orders
* **Order Entry**:  Create and cancel orders

## Signatures

For private endpoints that access user-specific data or perform actions on behalf of a user, authentication is required through wallet signatures. This ensures that only authorized users can create and update orders.

## Rate Limits

To ensure fair usage and optimal performance, the API implements rate limiting. For more information, see the [Rate Limits ](https://docs.reya.xyz/developers/rest-api-reference/rate-limits)documentation.

For real-time data needs, consider using our [WebSocket API](https://docs.reya.xyz/developers/broken-reference) for streaming updates.


# Rest API Reference

**Base URL**: `https://api.reya.xyz/v2`

## Overview

The Reya DEX REST API v2 provides programmatic access to the Reya Perpetual Exchange, enabling traders to interact with the platform algorithmically. This API is designed for developers and professional traders who want to build automated trading systems, integrate with existing platforms, or develop custom interfaces for the Reya DEX ecosystem.

## Key Features

* **Market Data**: Access comprehensive market information, including asset definitions, market summaries, and real-time price data
* **Order Management**: Create, cancel, and monitor orders with support for various order types (limit, trigger)
* **Position Tracking**: Monitor your current positions and historical executions
* **Wallet Integration**: Manage wallet configurations and access wallet-specific data
* **Price Data**: Access historical price data with customizable time intervals through candle endpoints

## API Structure

The API is organized into several logical sections:

* **Reference Data**:  Discover markets and assets definitions, trading fees
* **Market Data**: Access real-time and historical market data, including prices, candles and order execution
* **Wallet Data**: Get information about the wallet's accounts, positions and orders
* **Order Entry**:  Create and cancel orders

## Signatures

For private endpoints that access user-specific data or perform actions on behalf of a user, authentication is required through wallet signatures. This ensures that only authorized users can create and update orders.

## Rate Limits

To ensure fair usage and optimal performance, the API implements rate limiting. For more information, see the [Rate Limits ](https://docs.reya.xyz/developers/rest-api-reference/rate-limits)documentation.

For real-time data needs, consider using our [WebSocket API](https://docs.reya.xyz/developers/broken-reference) for streaming updates.


# Reference Data

Market definitions, global parameters, liquidity parameters, etc.

## GET /marketDefinitions

> Get market definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/marketDefinitions":{"get":{"summary":"Get market definitions","operationId":"getMarketDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of market definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/MarketDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"MarketDefinition":{"title":"MarketDefinition","$id":"#MarketDefinition","type":"object","required":["symbol","marketId","minOrderQty","qtyStepSize","tickSize","liquidationMarginParameter","initialMarginParameter","maxLeverage","oiCap"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each market, only needed to generate signatures"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"},"liquidationMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered to avoid liquidation procedures for a given market; below this value, your account is subject to liquidation procedures. When cross margining, all requirements across markets are covered by the same balance, and all positions are subject to liquidations."},"initialMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered post trade; if the account does not satisfy this requirement, trades will not get executed."},"maxLeverage":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maximum leverage allowed"},"oiCap":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Maximum one-sided open interest in units for a given market."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /spotMarketDefinitions

> Get spot market definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/spotMarketDefinitions":{"get":{"summary":"Get spot market definitions","operationId":"getSpotMarketDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of spot market definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/SpotMarketDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"SpotMarketDefinition":{"title":"SpotMarketDefinition","$id":"#SpotMarketDefinition","type":"object","required":["symbol","marketId","baseAsset","quoteAsset","minOrderQty","qtyStepSize","tickSize"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each spot market"},"baseAsset":{"type":"string","description":"Base asset symbol"},"quoteAsset":{"type":"string","description":"Quote asset symbol"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum order quantity (base asset)"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment (base asset)"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /assetDefinitions

> Get asset definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/assetDefinitions":{"get":{"summary":"Get asset definitions","operationId":"getAssetDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of asset definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/AssetDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"AssetDefinition":{"title":"AssetDefinition","$id":"#AssetDefinition","type":"object","required":["asset","priceHaircut","liquidationDiscount","status","decimals","displayDecimals"],"properties":{"asset":{"$ref":"#/components/schemas/Asset"},"spotMarketSymbol":{"$ref":"#/components/schemas/Symbol"},"priceHaircut":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Notional discount to the value of a collateral when used to satisfy the margin requirements; it does not imply any token conversion, but is rather an accounting adjustment."},"liquidationDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Discount in the token price when liquidating collateral."},"status":{"type":"string","enum":["ENABLED","WITHDRAWAL_ONLY"],"description":"Status of asset (ENABLED = deposits and withdrawals allowed, WITHDRAWAL_ONLY = only withdrawals allowed)"},"decimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places for record keeping amounts of this asset (e.g. 18 for ETH, 6 for RUSD)"},"displayDecimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places shown for display purposes in frontends"}},"additionalProperties":true},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /liquidityParameters

> Get liquidity parameters

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/liquidityParameters":{"get":{"summary":"Get liquidity parameters","operationId":"getLiquidityParameters","tags":["Reference Data"],"responses":{"200":{"description":"List of liquidity parameters","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/LiquidityParameters"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"LiquidityParameters":{"title":"LiquidityParameters","$id":"#LiquidityParameters","type":"object","required":["symbol","depth","velocityMultiplier"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"depth":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the liquidity distribution along the AMM pricing curve, in particular expanding or contracting the max exposure parameter that would otherwise be determined by the capital available."},"velocityMultiplier":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the sensitivity of the dynamic funding rate to the size of the imbalances; higher multiplier means that the funding rate will diverge faster, all else being equal."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /globalFeeParameters

> Get global fee parameters

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/globalFeeParameters":{"get":{"summary":"Get global fee parameters","operationId":"getGlobalFeeParameters","tags":["Reference Data"],"responses":{"200":{"description":"Global fee parameters","content":{"application/json":{"schema":{"$ref":"#/components/schemas/GlobalFeeParameters"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"GlobalFeeParameters":{"title":"GlobalFeeParameters","$id":"#GlobalFeeParameters","type":"object","required":["ogDiscount","refereeDiscount","referrerRebate","affiliateReferrerRebate"],"properties":{"ogDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"OG user discount"},"refereeDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referee discount"},"referrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referrer rebate"},"affiliateReferrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Affiliate referrer rebate"}},"additionalProperties":true},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /feeTiers

> Get fee tiers

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/feeTiers":{"get":{"summary":"Get fee tiers","operationId":"getFeeTierParameters","tags":["Reference Data"],"responses":{"200":{"description":"List of fee tier parameters","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/FeeTierParameters"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"FeeTierParameters":{"title":"FeeTierParameters","$id":"#FeeTierParameters","type":"object","required":["tierId","takerFee","makerFee","volume14d","tierType"],"properties":{"tierId":{"$ref":"#/components/schemas/UnsignedInteger"},"takerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Taker fee rate (fee will be qty * takerFee)"},"makerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Maker fee rate (fee will be qty * makerFee)"},"volume14d":{"$ref":"#/components/schemas/UnsignedDecimal","description":"14-day volume level required this fee tier to be applied to a wallet"},"tierType":{"$ref":"#/components/schemas/TierType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

# Reference Data

Market definitions, global parameters, liquidity parameters, etc.

## GET /marketDefinitions

> Get market definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/marketDefinitions":{"get":{"summary":"Get market definitions","operationId":"getMarketDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of market definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/MarketDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"MarketDefinition":{"title":"MarketDefinition","$id":"#MarketDefinition","type":"object","required":["symbol","marketId","minOrderQty","qtyStepSize","tickSize","liquidationMarginParameter","initialMarginParameter","maxLeverage","oiCap"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each market, only needed to generate signatures"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"},"liquidationMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered to avoid liquidation procedures for a given market; below this value, your account is subject to liquidation procedures. When cross margining, all requirements across markets are covered by the same balance, and all positions are subject to liquidations."},"initialMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered post trade; if the account does not satisfy this requirement, trades will not get executed."},"maxLeverage":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maximum leverage allowed"},"oiCap":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Maximum one-sided open interest in units for a given market."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /spotMarketDefinitions

> Get spot market definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/spotMarketDefinitions":{"get":{"summary":"Get spot market definitions","operationId":"getSpotMarketDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of spot market definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/SpotMarketDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"SpotMarketDefinition":{"title":"SpotMarketDefinition","$id":"#SpotMarketDefinition","type":"object","required":["symbol","marketId","baseAsset","quoteAsset","minOrderQty","qtyStepSize","tickSize"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each spot market"},"baseAsset":{"type":"string","description":"Base asset symbol"},"quoteAsset":{"type":"string","description":"Quote asset symbol"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum order quantity (base asset)"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment (base asset)"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /assetDefinitions

> Get asset definitions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/assetDefinitions":{"get":{"summary":"Get asset definitions","operationId":"getAssetDefinitions","tags":["Reference Data"],"responses":{"200":{"description":"List of asset definitions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/AssetDefinition"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"AssetDefinition":{"title":"AssetDefinition","$id":"#AssetDefinition","type":"object","required":["asset","priceHaircut","liquidationDiscount","status","decimals","displayDecimals"],"properties":{"asset":{"$ref":"#/components/schemas/Asset"},"spotMarketSymbol":{"$ref":"#/components/schemas/Symbol"},"priceHaircut":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Notional discount to the value of a collateral when used to satisfy the margin requirements; it does not imply any token conversion, but is rather an accounting adjustment."},"liquidationDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Discount in the token price when liquidating collateral."},"status":{"type":"string","enum":["ENABLED","WITHDRAWAL_ONLY"],"description":"Status of asset (ENABLED = deposits and withdrawals allowed, WITHDRAWAL_ONLY = only withdrawals allowed)"},"decimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places for record keeping amounts of this asset (e.g. 18 for ETH, 6 for RUSD)"},"displayDecimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places shown for display purposes in frontends"}},"additionalProperties":true},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /liquidityParameters

> Get liquidity parameters

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/liquidityParameters":{"get":{"summary":"Get liquidity parameters","operationId":"getLiquidityParameters","tags":["Reference Data"],"responses":{"200":{"description":"List of liquidity parameters","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/LiquidityParameters"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"LiquidityParameters":{"title":"LiquidityParameters","$id":"#LiquidityParameters","type":"object","required":["symbol","depth","velocityMultiplier"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"depth":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the liquidity distribution along the AMM pricing curve, in particular expanding or contracting the max exposure parameter that would otherwise be determined by the capital available."},"velocityMultiplier":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the sensitivity of the dynamic funding rate to the size of the imbalances; higher multiplier means that the funding rate will diverge faster, all else being equal."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /globalFeeParameters

> Get global fee parameters

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/globalFeeParameters":{"get":{"summary":"Get global fee parameters","operationId":"getGlobalFeeParameters","tags":["Reference Data"],"responses":{"200":{"description":"Global fee parameters","content":{"application/json":{"schema":{"$ref":"#/components/schemas/GlobalFeeParameters"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"GlobalFeeParameters":{"title":"GlobalFeeParameters","$id":"#GlobalFeeParameters","type":"object","required":["ogDiscount","refereeDiscount","referrerRebate","affiliateReferrerRebate"],"properties":{"ogDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"OG user discount"},"refereeDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referee discount"},"referrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referrer rebate"},"affiliateReferrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Affiliate referrer rebate"}},"additionalProperties":true},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /feeTiers

> Get fee tiers

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Reference Data","description":"Market definitions, global parameters, liquidity parameters, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/feeTiers":{"get":{"summary":"Get fee tiers","operationId":"getFeeTierParameters","tags":["Reference Data"],"responses":{"200":{"description":"List of fee tier parameters","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/FeeTierParameters"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"FeeTierParameters":{"title":"FeeTierParameters","$id":"#FeeTierParameters","type":"object","required":["tierId","takerFee","makerFee","volume14d","tierType"],"properties":{"tierId":{"$ref":"#/components/schemas/UnsignedInteger"},"takerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Taker fee rate (fee will be qty * takerFee)"},"makerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Maker fee rate (fee will be qty * makerFee)"},"volume14d":{"$ref":"#/components/schemas/UnsignedDecimal","description":"14-day volume level required this fee tier to be applied to a wallet"},"tierType":{"$ref":"#/components/schemas/TierType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```
# Wallet Data

Accounts, positions, trades, etc.

## GET /wallet/{address}/accounts

> Get wallet accounts

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/accounts":{"get":{"summary":"Get wallet accounts","operationId":"getWalletAccounts","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"}],"responses":{"200":{"description":"List of accounts","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/Account"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"Account":{"title":"Account","$id":"#Account","type":"object","required":["accountId","name","type"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"name":{"type":"string"},"type":{"$ref":"#/components/schemas/AccountType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Get wallet perp executions

> Returns up to 100 perp executions for a given wallet.

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/perpExecutions":{"get":{"summary":"Get wallet perp executions","description":"Returns up to 100 perp executions for a given wallet.","operationId":"getWalletPerpExecutions","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"},{"$ref":"#/components/parameters/StartTimeParam"},{"$ref":"#/components/parameters/EndTimeParam"}],"responses":{"200":{"description":"List of perpetual executions","content":{"application/json":{"schema":{"$ref":"#/components/schemas/PerpExecutionList"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}},"StartTimeParam":{"name":"startTime","in":"query","required":false,"description":"Return results after this sequence number (for pagination)","schema":{"$ref":"#/components/schemas/UnsignedInteger"}},"EndTimeParam":{"name":"endTime","in":"query","required":false,"description":"Return results before this sequence number (for pagination)","schema":{"$ref":"#/components/schemas/UnsignedInteger"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"PerpExecutionList":{"title":"PerpExecutionList","$id":"#PerpExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/PerpExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Get wallet spot executions

> Returns up to 100 spot executions for a given wallet.

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/spotExecutions":{"get":{"summary":"Get wallet spot executions","description":"Returns up to 100 spot executions for a given wallet.","operationId":"getWalletSpotExecutions","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"},{"$ref":"#/components/parameters/StartTimeParam"},{"$ref":"#/components/parameters/EndTimeParam"}],"responses":{"200":{"description":"List of spot executions","content":{"application/json":{"schema":{"$ref":"#/components/schemas/SpotExecutionList"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}},"StartTimeParam":{"name":"startTime","in":"query","required":false,"description":"Return results after this sequence number (for pagination)","schema":{"$ref":"#/components/schemas/UnsignedInteger"}},"EndTimeParam":{"name":"endTime","in":"query","required":false,"description":"Return results before this sequence number (for pagination)","schema":{"$ref":"#/components/schemas/UnsignedInteger"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SpotExecutionList":{"title":"SpotExecutionList","$id":"#SpotExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/SpotExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## GET /wallet/{address}/positions

> Get wallet positions

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/positions":{"get":{"summary":"Get wallet positions","operationId":"getWalletPositions","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"}],"responses":{"200":{"description":"List of positions","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/Position"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"Position":{"title":"Position","$id":"#Position","type":"object","required":["exchangeId","symbol","accountId","qty","side","avgEntryPrice","avgEntryFundingValue","lastTradeSequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"avgEntryPrice":{"$ref":"#/components/schemas/SignedDecimal"},"avgEntryFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Average of funding values at the entry times of currently open exposure, which serves as a baseline from which to compute the accrued funding in the position: units x (fundingValue - avgEntryFundingValue)"},"lastTradeSequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Sequence number of last execution taken into account for the position."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Get wallet account balances

> Returns all account real balances for a wallet.

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/accountBalances":{"get":{"summary":"Get wallet account balances","description":"Returns all account real balances for a wallet.","operationId":"getWalletAccountBalances","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"}],"responses":{"200":{"description":"List of account balances","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/AccountBalance"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"AccountBalance":{"title":"AccountBalance","$id":"#AccountBalance","type":"object","required":["accountId","asset","realBalance","balanceDEPRECATED"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"asset":{"$ref":"#/components/schemas/Asset"},"realBalance":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals) and realized pnl from closed positions. Realized pnl only applies to RUSD given it is the only settlement asset"},"balanceDEPRECATED":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals). This field is deprecated and will be removed in a future release"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Get wallet open orders

> Returns all pending orders for a wallet.

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/openOrders":{"get":{"summary":"Get wallet open orders","description":"Returns all pending orders for a wallet.","operationId":"getWalletOpenOrders","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"}],"responses":{"200":{"description":"List of open orders","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/Order"}}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"Order":{"title":"Order","$id":"#Order","type":"object","required":["exchangeId","symbol","accountId","orderId","side","limitPx","orderType","status","createdAt","lastUpdateAt"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"orderId":{"type":"string"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"side":{"$ref":"#/components/schemas/Side"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Price at which TP/SL orders will be triggered, should not be set for other order types."},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"status":{"$ref":"#/components/schemas/OrderStatus"},"createdAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Creation timestamp (milliseconds)"},"lastUpdateAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Get wallet configuration

> Returns trading configuration for a wallet

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Wallet Data","description":"Accounts, positions, trades, etc."}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/wallet/{address}/configuration":{"get":{"summary":"Get wallet configuration","description":"Returns trading configuration for a wallet","operationId":"getWalletConfiguration","tags":["Wallet Data"],"parameters":[{"$ref":"#/components/parameters/AddressParam"}],"responses":{"200":{"description":"Wallet configuration","content":{"application/json":{"schema":{"$ref":"#/components/schemas/WalletConfiguration"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"parameters":{"AddressParam":{"name":"address","in":"path","required":true,"schema":{"$ref":"#/components/schemas/Address"}}},"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"WalletConfiguration":{"title":"WalletConfiguration","$id":"#WalletConfiguration","type":"object","required":["feeTierId","ogStatus","affiliateStatus","refereeStatus"],"properties":{"feeTierId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Fee tier identifier"},"ogStatus":{"type":"boolean","description":"OG status"},"affiliateStatus":{"type":"boolean","description":"Affiliate status"},"refereeStatus":{"type":"boolean","description":"Referee status"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```
# Order Entry

Order entry operations

## Create order

> Create a new order (IOC, GTC, SL, TP)

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Order Entry","description":"Order entry operations"}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/createOrder":{"post":{"summary":"Create order","description":"Create a new order (IOC, GTC, SL, TP)","operationId":"createOrder","tags":["Order Entry"],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/CreateOrderRequest"}}}},"responses":{"200":{"description":"Order creation response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/CreateOrderResponse"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"CreateOrderRequest":{"title":"CreateOrderRequest","$id":"#CreateOrderRequest","type":"object","required":["exchangeId","accountId","isBuy","limitPx","orderType","signature","nonce","signerWallet"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"isBuy":{"type":"boolean","description":"Whether this is a buy order"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Trigger price, only for TP/SL orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"Order nonce, see signatures and nonces section for more details."},"signerWallet":{"$ref":"#/components/schemas/Address"},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for PERP IOC orders and all SPOT orders). In seconds since epoch. The order will only be filled before this timestamp."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Optional field that allows clients to assign their own unique identifier to orders."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"},"CreateOrderResponse":{"title":"CreateOrderResponse","$id":"#CreateOrderResponse","type":"object","required":["status"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"orderId":{"type":"string","description":"Created order ID (currently generated for all order types except IOC)"},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Cancel order

> Cancel an existing order

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Order Entry","description":"Order entry operations"}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/cancelOrder":{"post":{"summary":"Cancel order","description":"Cancel an existing order","operationId":"cancelOrder","tags":["Order Entry"],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/CancelOrderRequest"}}}},"responses":{"200":{"description":"Order cancellation response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/CancelOrderResponse"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"CancelOrderRequest":{"title":"CancelOrderRequest","$id":"#CancelOrderRequest","type":"object","required":["signature"],"properties":{"orderId":{"type":"string","description":"Internal matching engine order ID to cancel. Provide either orderId OR clientOrderId, not both. For spot markets, this is the order ID returned in the CreateOrderResponse."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Provide either orderId OR clientOrderId, not both. This is the same clientOrderId provided in CreateOrderRequest."},"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID that owns the order. Required for spot markets."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Market symbol for the order.Required for spot market orders. If not provided, assumes perp market for backwards compatibility."},"signature":{"type":"string","description":"See signatures section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details. Compulsory for spot orders."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for SPOT orders). In seconds since epoch."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"CancelOrderResponse":{"title":"CancelOrderResponse","$id":"#CancelOrderResponse","type":"object","required":["status","orderId"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"orderId":{"type":"string","description":"Cancelled order ID"},"clientOrderId":{"type":"integer","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```

## Cancel all orders

> Cancel all orders matching the specified filters (mass cancel)

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"tags":[{"name":"Order Entry","description":"Order entry operations"}],"servers":[{"url":"https://api.reya.xyz/v2","description":"Production server"},{"url":"https://api-test.reya.xyz/v2","description":"Testnet server"}],"paths":{"/cancelAll":{"post":{"summary":"Cancel all orders","description":"Cancel all orders matching the specified filters (mass cancel)","operationId":"cancelAll","tags":["Order Entry"],"requestBody":{"required":false,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/MassCancelRequest"}}}},"responses":{"200":{"description":"Mass cancel response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/MassCancelResponse"}}}},"400":{"$ref":"#/components/responses/BadRequest"},"500":{"$ref":"#/components/responses/InternalServerError"}}}}},"components":{"schemas":{"MassCancelRequest":{"title":"MassCancelRequest","$id":"#MassCancelRequest","type":"object","required":["signature","nonce","accountId","expiresAfter"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID to cancel orders for."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Symbol to cancel orders for. If not specified, cancels orders for all symbols."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp. In seconds since epoch."}},"additionalProperties":true,"description":"Request to cancel all orders matching the specified filters"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"MassCancelResponse":{"title":"MassCancelResponse","$id":"#MassCancelResponse","type":"object","required":["cancelledCount"],"properties":{"cancelledCount":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of orders that were cancelled"}},"additionalProperties":true},"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"},"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}},"responses":{"BadRequest":{"description":"Bad request","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RequestError"}}}},"InternalServerError":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ServerError"}}}}}}}
```
# Models

## The RequestError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The ServerError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The MarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketDefinition":{"title":"MarketDefinition","$id":"#MarketDefinition","type":"object","required":["symbol","marketId","minOrderQty","qtyStepSize","tickSize","liquidationMarginParameter","initialMarginParameter","maxLeverage","oiCap"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each market, only needed to generate signatures"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"},"liquidationMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered to avoid liquidation procedures for a given market; below this value, your account is subject to liquidation procedures. When cross margining, all requirements across markets are covered by the same balance, and all positions are subject to liquidations."},"initialMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered post trade; if the account does not satisfy this requirement, trades will not get executed."},"maxLeverage":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maximum leverage allowed"},"oiCap":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Maximum one-sided open interest in units for a given market."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotMarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotMarketDefinition":{"title":"SpotMarketDefinition","$id":"#SpotMarketDefinition","type":"object","required":["symbol","marketId","baseAsset","quoteAsset","minOrderQty","qtyStepSize","tickSize"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each spot market"},"baseAsset":{"type":"string","description":"Base asset symbol"},"quoteAsset":{"type":"string","description":"Quote asset symbol"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum order quantity (base asset)"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment (base asset)"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The AssetDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AssetDefinition":{"title":"AssetDefinition","$id":"#AssetDefinition","type":"object","required":["asset","priceHaircut","liquidationDiscount","status","decimals","displayDecimals"],"properties":{"asset":{"$ref":"#/components/schemas/Asset"},"spotMarketSymbol":{"$ref":"#/components/schemas/Symbol"},"priceHaircut":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Notional discount to the value of a collateral when used to satisfy the margin requirements; it does not imply any token conversion, but is rather an accounting adjustment."},"liquidationDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Discount in the token price when liquidating collateral."},"status":{"type":"string","enum":["ENABLED","WITHDRAWAL_ONLY"],"description":"Status of asset (ENABLED = deposits and withdrawals allowed, WITHDRAWAL_ONLY = only withdrawals allowed)"},"decimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places for record keeping amounts of this asset (e.g. 18 for ETH, 6 for RUSD)"},"displayDecimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places shown for display purposes in frontends"}},"additionalProperties":true},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The FeeTierParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"FeeTierParameters":{"title":"FeeTierParameters","$id":"#FeeTierParameters","type":"object","required":["tierId","takerFee","makerFee","volume14d","tierType"],"properties":{"tierId":{"$ref":"#/components/schemas/UnsignedInteger"},"takerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Taker fee rate (fee will be qty * takerFee)"},"makerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Maker fee rate (fee will be qty * makerFee)"},"volume14d":{"$ref":"#/components/schemas/UnsignedDecimal","description":"14-day volume level required this fee tier to be applied to a wallet"},"tierType":{"$ref":"#/components/schemas/TierType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The GlobalFeeParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"GlobalFeeParameters":{"title":"GlobalFeeParameters","$id":"#GlobalFeeParameters","type":"object","required":["ogDiscount","refereeDiscount","referrerRebate","affiliateReferrerRebate"],"properties":{"ogDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"OG user discount"},"refereeDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referee discount"},"referrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referrer rebate"},"affiliateReferrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Affiliate referrer rebate"}},"additionalProperties":true},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The LiquidityParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"LiquidityParameters":{"title":"LiquidityParameters","$id":"#LiquidityParameters","type":"object","required":["symbol","depth","velocityMultiplier"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"depth":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the liquidity distribution along the AMM pricing curve, in particular expanding or contracting the max exposure parameter that would otherwise be determined by the capital available."},"velocityMultiplier":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the sensitivity of the dynamic funding rate to the size of the imbalances; higher multiplier means that the funding rate will diverge faster, all else being equal."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The WalletConfiguration object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"WalletConfiguration":{"title":"WalletConfiguration","$id":"#WalletConfiguration","type":"object","required":["feeTierId","ogStatus","affiliateStatus","refereeStatus"],"properties":{"feeTierId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Fee tier identifier"},"ogStatus":{"type":"boolean","description":"OG status"},"affiliateStatus":{"type":"boolean","description":"Affiliate status"},"refereeStatus":{"type":"boolean","description":"Referee status"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The MarketSummary object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketSummary":{"title":"MarketSummary","$id":"#MarketSummary","type":"object","required":["symbol","updatedAt","longOiQty","shortOiQty","oiQty","fundingRate","longFundingValue","shortFundingValue","fundingRateVelocity","volume24h"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Time when the market summary was last calculated (milliseconds)"},"longOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Long open interest in lots"},"shortOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Short open interest in lots"},"oiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total open interest quantity"},"fundingRate":{"$ref":"#/components/schemas/SignedDecimal","description":"Current hourly funding rate"},"longFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"shortFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"fundingRateVelocity":{"$ref":"#/components/schemas/SignedDecimal","description":"Funding rate velocity"},"volume24h":{"$ref":"#/components/schemas/UnsignedDecimal"},"pxChange24h":{"$ref":"#/components/schemas/SignedDecimal"},"throttledOraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last oracle price, at the moment of the last market summary update"},"throttledPoolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last pool price, at the moment of the last market summary update"},"pricesUpdatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of the last price update (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Position object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Position":{"title":"Position","$id":"#Position","type":"object","required":["exchangeId","symbol","accountId","qty","side","avgEntryPrice","avgEntryFundingValue","lastTradeSequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"avgEntryPrice":{"$ref":"#/components/schemas/SignedDecimal"},"avgEntryFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Average of funding values at the entry times of currently open exposure, which serves as a baseline from which to compute the accrued funding in the position: units x (fundingValue - avgEntryFundingValue)"},"lastTradeSequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Sequence number of last execution taken into account for the position."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Order object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Order":{"title":"Order","$id":"#Order","type":"object","required":["exchangeId","symbol","accountId","orderId","side","limitPx","orderType","status","createdAt","lastUpdateAt"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"orderId":{"type":"string"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"side":{"$ref":"#/components/schemas/Side"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Price at which TP/SL orders will be triggered, should not be set for other order types."},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"status":{"$ref":"#/components/schemas/OrderStatus"},"createdAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Creation timestamp (milliseconds)"},"lastUpdateAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The Account object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Account":{"title":"Account","$id":"#Account","type":"object","required":["accountId","name","type"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"name":{"type":"string"},"type":{"$ref":"#/components/schemas/AccountType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The AccountBalance object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountBalance":{"title":"AccountBalance","$id":"#AccountBalance","type":"object","required":["accountId","asset","realBalance","balanceDEPRECATED"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"asset":{"$ref":"#/components/schemas/Asset"},"realBalance":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals) and realized pnl from closed positions. Realized pnl only applies to RUSD given it is the only settlement asset"},"balanceDEPRECATED":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals). This field is deprecated and will be removed in a future release"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The PerpExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecutionList":{"title":"PerpExecutionList","$id":"#PerpExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/PerpExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The SpotExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecutionList":{"title":"SpotExecutionList","$id":"#SpotExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/SpotExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The Price object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Price":{"title":"Price","$id":"#Price","type":"object","required":["symbol","updatedAt","oraclePrice"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"oraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Price given by the Stork feeds, used both as the peg price for prices on Reya, as well as Mark Prices. The Stork price feed is usually the perp prices across three major CEXs"},"poolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"The price currently quoted by the AMM for zero volume, from which trades are priced (equivalent to mid price in an order book); a trade of any size will be move this price up or down depending on the direction."},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CandleHistoryData object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CandleHistoryData":{"title":"CandleHistoryData","$id":"#CandleHistoryData","type":"object","required":["t","o","h","l","c"],"properties":{"t":{"type":"array","items":{"$ref":"#/components/schemas/UnsignedInteger"},"description":"Array of timestamps (seconds)"},"o":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of opening prices"},"h":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of high prices"},"l":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of low prices"},"c":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of closing prices"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The CreateOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderRequest":{"title":"CreateOrderRequest","$id":"#CreateOrderRequest","type":"object","required":["exchangeId","accountId","isBuy","limitPx","orderType","signature","nonce","signerWallet"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"isBuy":{"type":"boolean","description":"Whether this is a buy order"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Trigger price, only for TP/SL orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"Order nonce, see signatures and nonces section for more details."},"signerWallet":{"$ref":"#/components/schemas/Address"},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for PERP IOC orders and all SPOT orders). In seconds since epoch. The order will only be filled before this timestamp."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Optional field that allows clients to assign their own unique identifier to orders."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The CreateOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderResponse":{"title":"CreateOrderResponse","$id":"#CreateOrderResponse","type":"object","required":["status"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"orderId":{"type":"string","description":"Created order ID (currently generated for all order types except IOC)"},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CancelOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderRequest":{"title":"CancelOrderRequest","$id":"#CancelOrderRequest","type":"object","required":["signature"],"properties":{"orderId":{"type":"string","description":"Internal matching engine order ID to cancel. Provide either orderId OR clientOrderId, not both. For spot markets, this is the order ID returned in the CreateOrderResponse."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Provide either orderId OR clientOrderId, not both. This is the same clientOrderId provided in CreateOrderRequest."},"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID that owns the order. Required for spot markets."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Market symbol for the order.Required for spot market orders. If not provided, assumes perp market for backwards compatibility."},"signature":{"type":"string","description":"See signatures section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details. Compulsory for spot orders."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for SPOT orders). In seconds since epoch."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The CancelOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderResponse":{"title":"CancelOrderResponse","$id":"#CancelOrderResponse","type":"object","required":["status","orderId"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"orderId":{"type":"string","description":"Cancelled order ID"},"clientOrderId":{"type":"integer","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The MassCancelRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelRequest":{"title":"MassCancelRequest","$id":"#MassCancelRequest","type":"object","required":["signature","nonce","accountId","expiresAfter"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID to cancel orders for."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Symbol to cancel orders for. If not specified, cancels orders for all symbols."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp. In seconds since epoch."}},"additionalProperties":true,"description":"Request to cancel all orders matching the specified filters"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The MassCancelResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelResponse":{"title":"MassCancelResponse","$id":"#MassCancelResponse","type":"object","required":["cancelledCount"],"properties":{"cancelledCount":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of orders that were cancelled"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The Depth object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Depth":{"title":"Depth","$id":"#Depth","type":"object","required":["symbol","type","bids","asks","updatedAt"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"type":{"$ref":"#/components/schemas/DepthType"},"bids":{"type":"array","description":"Bid side levels aggregated by price, sorted descending by price","items":{"$ref":"#/components/schemas/Level"}},"asks":{"type":"array","description":"Ask side levels aggregated by price, sorted ascending by price","items":{"$ref":"#/components/schemas/Level"}},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Snapshot generation timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"},"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The ServerErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Symbol object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The UnsignedInteger object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The UnsignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The RequestErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Asset object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"}}}}
```

## The SignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The TierType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The Side object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"}}}}
```

## The ExecutionType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PerpExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PaginationMeta object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The DepthType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"}}}}
```

## The Level object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The Address object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The AccountType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The OrderType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"}}}}
```

## The TimeInForce object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"}}}}
```

## The OrderStatus object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```
# Models

## The RequestError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The ServerError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The MarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketDefinition":{"title":"MarketDefinition","$id":"#MarketDefinition","type":"object","required":["symbol","marketId","minOrderQty","qtyStepSize","tickSize","liquidationMarginParameter","initialMarginParameter","maxLeverage","oiCap"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each market, only needed to generate signatures"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"},"liquidationMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered to avoid liquidation procedures for a given market; below this value, your account is subject to liquidation procedures. When cross margining, all requirements across markets are covered by the same balance, and all positions are subject to liquidations."},"initialMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered post trade; if the account does not satisfy this requirement, trades will not get executed."},"maxLeverage":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maximum leverage allowed"},"oiCap":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Maximum one-sided open interest in units for a given market."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotMarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotMarketDefinition":{"title":"SpotMarketDefinition","$id":"#SpotMarketDefinition","type":"object","required":["symbol","marketId","baseAsset","quoteAsset","minOrderQty","qtyStepSize","tickSize"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each spot market"},"baseAsset":{"type":"string","description":"Base asset symbol"},"quoteAsset":{"type":"string","description":"Quote asset symbol"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum order quantity (base asset)"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment (base asset)"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The AssetDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AssetDefinition":{"title":"AssetDefinition","$id":"#AssetDefinition","type":"object","required":["asset","priceHaircut","liquidationDiscount","status","decimals","displayDecimals"],"properties":{"asset":{"$ref":"#/components/schemas/Asset"},"spotMarketSymbol":{"$ref":"#/components/schemas/Symbol"},"priceHaircut":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Notional discount to the value of a collateral when used to satisfy the margin requirements; it does not imply any token conversion, but is rather an accounting adjustment."},"liquidationDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Discount in the token price when liquidating collateral."},"status":{"type":"string","enum":["ENABLED","WITHDRAWAL_ONLY"],"description":"Status of asset (ENABLED = deposits and withdrawals allowed, WITHDRAWAL_ONLY = only withdrawals allowed)"},"decimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places for record keeping amounts of this asset (e.g. 18 for ETH, 6 for RUSD)"},"displayDecimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places shown for display purposes in frontends"}},"additionalProperties":true},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The FeeTierParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"FeeTierParameters":{"title":"FeeTierParameters","$id":"#FeeTierParameters","type":"object","required":["tierId","takerFee","makerFee","volume14d","tierType"],"properties":{"tierId":{"$ref":"#/components/schemas/UnsignedInteger"},"takerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Taker fee rate (fee will be qty * takerFee)"},"makerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Maker fee rate (fee will be qty * makerFee)"},"volume14d":{"$ref":"#/components/schemas/UnsignedDecimal","description":"14-day volume level required this fee tier to be applied to a wallet"},"tierType":{"$ref":"#/components/schemas/TierType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The GlobalFeeParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"GlobalFeeParameters":{"title":"GlobalFeeParameters","$id":"#GlobalFeeParameters","type":"object","required":["ogDiscount","refereeDiscount","referrerRebate","affiliateReferrerRebate"],"properties":{"ogDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"OG user discount"},"refereeDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referee discount"},"referrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referrer rebate"},"affiliateReferrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Affiliate referrer rebate"}},"additionalProperties":true},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The LiquidityParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"LiquidityParameters":{"title":"LiquidityParameters","$id":"#LiquidityParameters","type":"object","required":["symbol","depth","velocityMultiplier"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"depth":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the liquidity distribution along the AMM pricing curve, in particular expanding or contracting the max exposure parameter that would otherwise be determined by the capital available."},"velocityMultiplier":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the sensitivity of the dynamic funding rate to the size of the imbalances; higher multiplier means that the funding rate will diverge faster, all else being equal."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The WalletConfiguration object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"WalletConfiguration":{"title":"WalletConfiguration","$id":"#WalletConfiguration","type":"object","required":["feeTierId","ogStatus","affiliateStatus","refereeStatus"],"properties":{"feeTierId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Fee tier identifier"},"ogStatus":{"type":"boolean","description":"OG status"},"affiliateStatus":{"type":"boolean","description":"Affiliate status"},"refereeStatus":{"type":"boolean","description":"Referee status"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The MarketSummary object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketSummary":{"title":"MarketSummary","$id":"#MarketSummary","type":"object","required":["symbol","updatedAt","longOiQty","shortOiQty","oiQty","fundingRate","longFundingValue","shortFundingValue","fundingRateVelocity","volume24h"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Time when the market summary was last calculated (milliseconds)"},"longOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Long open interest in lots"},"shortOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Short open interest in lots"},"oiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total open interest quantity"},"fundingRate":{"$ref":"#/components/schemas/SignedDecimal","description":"Current hourly funding rate"},"longFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"shortFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"fundingRateVelocity":{"$ref":"#/components/schemas/SignedDecimal","description":"Funding rate velocity"},"volume24h":{"$ref":"#/components/schemas/UnsignedDecimal"},"pxChange24h":{"$ref":"#/components/schemas/SignedDecimal"},"throttledOraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last oracle price, at the moment of the last market summary update"},"throttledPoolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last pool price, at the moment of the last market summary update"},"pricesUpdatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of the last price update (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Position object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Position":{"title":"Position","$id":"#Position","type":"object","required":["exchangeId","symbol","accountId","qty","side","avgEntryPrice","avgEntryFundingValue","lastTradeSequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"avgEntryPrice":{"$ref":"#/components/schemas/SignedDecimal"},"avgEntryFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Average of funding values at the entry times of currently open exposure, which serves as a baseline from which to compute the accrued funding in the position: units x (fundingValue - avgEntryFundingValue)"},"lastTradeSequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Sequence number of last execution taken into account for the position."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Order object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Order":{"title":"Order","$id":"#Order","type":"object","required":["exchangeId","symbol","accountId","orderId","side","limitPx","orderType","status","createdAt","lastUpdateAt"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"orderId":{"type":"string"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"side":{"$ref":"#/components/schemas/Side"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Price at which TP/SL orders will be triggered, should not be set for other order types."},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"status":{"$ref":"#/components/schemas/OrderStatus"},"createdAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Creation timestamp (milliseconds)"},"lastUpdateAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The Account object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Account":{"title":"Account","$id":"#Account","type":"object","required":["accountId","name","type"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"name":{"type":"string"},"type":{"$ref":"#/components/schemas/AccountType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The AccountBalance object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountBalance":{"title":"AccountBalance","$id":"#AccountBalance","type":"object","required":["accountId","asset","realBalance","balanceDEPRECATED"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"asset":{"$ref":"#/components/schemas/Asset"},"realBalance":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals) and realized pnl from closed positions. Realized pnl only applies to RUSD given it is the only settlement asset"},"balanceDEPRECATED":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals). This field is deprecated and will be removed in a future release"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The PerpExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecutionList":{"title":"PerpExecutionList","$id":"#PerpExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/PerpExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The SpotExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecutionList":{"title":"SpotExecutionList","$id":"#SpotExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/SpotExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The Price object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Price":{"title":"Price","$id":"#Price","type":"object","required":["symbol","updatedAt","oraclePrice"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"oraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Price given by the Stork feeds, used both as the peg price for prices on Reya, as well as Mark Prices. The Stork price feed is usually the perp prices across three major CEXs"},"poolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"The price currently quoted by the AMM for zero volume, from which trades are priced (equivalent to mid price in an order book); a trade of any size will be move this price up or down depending on the direction."},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CandleHistoryData object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CandleHistoryData":{"title":"CandleHistoryData","$id":"#CandleHistoryData","type":"object","required":["t","o","h","l","c"],"properties":{"t":{"type":"array","items":{"$ref":"#/components/schemas/UnsignedInteger"},"description":"Array of timestamps (seconds)"},"o":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of opening prices"},"h":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of high prices"},"l":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of low prices"},"c":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of closing prices"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The CreateOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderRequest":{"title":"CreateOrderRequest","$id":"#CreateOrderRequest","type":"object","required":["exchangeId","accountId","isBuy","limitPx","orderType","signature","nonce","signerWallet"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"isBuy":{"type":"boolean","description":"Whether this is a buy order"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Trigger price, only for TP/SL orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"Order nonce, see signatures and nonces section for more details."},"signerWallet":{"$ref":"#/components/schemas/Address"},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for PERP IOC orders and all SPOT orders). In seconds since epoch. The order will only be filled before this timestamp."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Optional field that allows clients to assign their own unique identifier to orders."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The CreateOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderResponse":{"title":"CreateOrderResponse","$id":"#CreateOrderResponse","type":"object","required":["status"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"orderId":{"type":"string","description":"Created order ID (currently generated for all order types except IOC)"},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CancelOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderRequest":{"title":"CancelOrderRequest","$id":"#CancelOrderRequest","type":"object","required":["signature"],"properties":{"orderId":{"type":"string","description":"Internal matching engine order ID to cancel. Provide either orderId OR clientOrderId, not both. For spot markets, this is the order ID returned in the CreateOrderResponse."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Provide either orderId OR clientOrderId, not both. This is the same clientOrderId provided in CreateOrderRequest."},"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID that owns the order. Required for spot markets."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Market symbol for the order.Required for spot market orders. If not provided, assumes perp market for backwards compatibility."},"signature":{"type":"string","description":"See signatures section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details. Compulsory for spot orders."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for SPOT orders). In seconds since epoch."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The CancelOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderResponse":{"title":"CancelOrderResponse","$id":"#CancelOrderResponse","type":"object","required":["status","orderId"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"orderId":{"type":"string","description":"Cancelled order ID"},"clientOrderId":{"type":"integer","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The MassCancelRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelRequest":{"title":"MassCancelRequest","$id":"#MassCancelRequest","type":"object","required":["signature","nonce","accountId","expiresAfter"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID to cancel orders for."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Symbol to cancel orders for. If not specified, cancels orders for all symbols."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp. In seconds since epoch."}},"additionalProperties":true,"description":"Request to cancel all orders matching the specified filters"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The MassCancelResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelResponse":{"title":"MassCancelResponse","$id":"#MassCancelResponse","type":"object","required":["cancelledCount"],"properties":{"cancelledCount":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of orders that were cancelled"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The Depth object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Depth":{"title":"Depth","$id":"#Depth","type":"object","required":["symbol","type","bids","asks","updatedAt"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"type":{"$ref":"#/components/schemas/DepthType"},"bids":{"type":"array","description":"Bid side levels aggregated by price, sorted descending by price","items":{"$ref":"#/components/schemas/Level"}},"asks":{"type":"array","description":"Ask side levels aggregated by price, sorted ascending by price","items":{"$ref":"#/components/schemas/Level"}},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Snapshot generation timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"},"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The ServerErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Symbol object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The UnsignedInteger object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The UnsignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The RequestErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Asset object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"}}}}
```

## The SignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The TierType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The Side object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"}}}}
```

## The ExecutionType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PerpExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PaginationMeta object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The DepthType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"}}}}
```

## The Level object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The Address object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The AccountType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The OrderType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"}}}}
```

## The TimeInForce object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"}}}}
```

## The OrderStatus object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```
# Models

## The RequestError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestError":{"title":"RequestError","$id":"#RequestError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/RequestErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The ServerError object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerError":{"title":"ServerError","$id":"#ServerError","type":"object","required":["error","message"],"properties":{"error":{"$ref":"#/components/schemas/ServerErrorCode"},"message":{"type":"string","description":"Human-readable error message"}},"additionalProperties":true},"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The MarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketDefinition":{"title":"MarketDefinition","$id":"#MarketDefinition","type":"object","required":["symbol","marketId","minOrderQty","qtyStepSize","tickSize","liquidationMarginParameter","initialMarginParameter","maxLeverage","oiCap"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each market, only needed to generate signatures"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"},"liquidationMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered to avoid liquidation procedures for a given market; below this value, your account is subject to liquidation procedures. When cross margining, all requirements across markets are covered by the same balance, and all positions are subject to liquidations."},"initialMarginParameter":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum percentage of notional that needs to be covered post trade; if the account does not satisfy this requirement, trades will not get executed."},"maxLeverage":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maximum leverage allowed"},"oiCap":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Maximum one-sided open interest in units for a given market."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotMarketDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotMarketDefinition":{"title":"SpotMarketDefinition","$id":"#SpotMarketDefinition","type":"object","required":["symbol","marketId","baseAsset","quoteAsset","minOrderQty","qtyStepSize","tickSize"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"marketId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Numerical identifier for each spot market"},"baseAsset":{"type":"string","description":"Base asset symbol"},"quoteAsset":{"type":"string","description":"Quote asset symbol"},"minOrderQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum order quantity (base asset)"},"qtyStepSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum size increment (base asset)"},"tickSize":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Minimum price increment"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The AssetDefinition object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AssetDefinition":{"title":"AssetDefinition","$id":"#AssetDefinition","type":"object","required":["asset","priceHaircut","liquidationDiscount","status","decimals","displayDecimals"],"properties":{"asset":{"$ref":"#/components/schemas/Asset"},"spotMarketSymbol":{"$ref":"#/components/schemas/Symbol"},"priceHaircut":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Notional discount to the value of a collateral when used to satisfy the margin requirements; it does not imply any token conversion, but is rather an accounting adjustment."},"liquidationDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Discount in the token price when liquidating collateral."},"status":{"type":"string","enum":["ENABLED","WITHDRAWAL_ONLY"],"description":"Status of asset (ENABLED = deposits and withdrawals allowed, WITHDRAWAL_ONLY = only withdrawals allowed)"},"decimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places for record keeping amounts of this asset (e.g. 18 for ETH, 6 for RUSD)"},"displayDecimals":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of decimal places shown for display purposes in frontends"}},"additionalProperties":true},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The FeeTierParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"FeeTierParameters":{"title":"FeeTierParameters","$id":"#FeeTierParameters","type":"object","required":["tierId","takerFee","makerFee","volume14d","tierType"],"properties":{"tierId":{"$ref":"#/components/schemas/UnsignedInteger"},"takerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Taker fee rate (fee will be qty * takerFee)"},"makerFee":{"$ref":"#/components/schemas/SignedDecimal","description":"Maker fee rate (fee will be qty * makerFee)"},"volume14d":{"$ref":"#/components/schemas/UnsignedDecimal","description":"14-day volume level required this fee tier to be applied to a wallet"},"tierType":{"$ref":"#/components/schemas/TierType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The GlobalFeeParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"GlobalFeeParameters":{"title":"GlobalFeeParameters","$id":"#GlobalFeeParameters","type":"object","required":["ogDiscount","refereeDiscount","referrerRebate","affiliateReferrerRebate"],"properties":{"ogDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"OG user discount"},"refereeDiscount":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referee discount"},"referrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Referrer rebate"},"affiliateReferrerRebate":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Affiliate referrer rebate"}},"additionalProperties":true},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The LiquidityParameters object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"LiquidityParameters":{"title":"LiquidityParameters","$id":"#LiquidityParameters","type":"object","required":["symbol","depth","velocityMultiplier"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"depth":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the liquidity distribution along the AMM pricing curve, in particular expanding or contracting the max exposure parameter that would otherwise be determined by the capital available."},"velocityMultiplier":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Parameter determining the sensitivity of the dynamic funding rate to the size of the imbalances; higher multiplier means that the funding rate will diverge faster, all else being equal."}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The WalletConfiguration object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"WalletConfiguration":{"title":"WalletConfiguration","$id":"#WalletConfiguration","type":"object","required":["feeTierId","ogStatus","affiliateStatus","refereeStatus"],"properties":{"feeTierId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Fee tier identifier"},"ogStatus":{"type":"boolean","description":"OG status"},"affiliateStatus":{"type":"boolean","description":"Affiliate status"},"refereeStatus":{"type":"boolean","description":"Referee status"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The MarketSummary object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MarketSummary":{"title":"MarketSummary","$id":"#MarketSummary","type":"object","required":["symbol","updatedAt","longOiQty","shortOiQty","oiQty","fundingRate","longFundingValue","shortFundingValue","fundingRateVelocity","volume24h"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Time when the market summary was last calculated (milliseconds)"},"longOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Long open interest in lots"},"shortOiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Short open interest in lots"},"oiQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total open interest quantity"},"fundingRate":{"$ref":"#/components/schemas/SignedDecimal","description":"Current hourly funding rate"},"longFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"shortFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Current reference value of funding accrued by one unit of exposure; there is one funding value per market and per direction, with short v long funding values differing possibly due to Auto-Deleveraging (ADL)"},"fundingRateVelocity":{"$ref":"#/components/schemas/SignedDecimal","description":"Funding rate velocity"},"volume24h":{"$ref":"#/components/schemas/UnsignedDecimal"},"pxChange24h":{"$ref":"#/components/schemas/SignedDecimal"},"throttledOraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last oracle price, at the moment of the last market summary update"},"throttledPoolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Last pool price, at the moment of the last market summary update"},"pricesUpdatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of the last price update (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Position object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Position":{"title":"Position","$id":"#Position","type":"object","required":["exchangeId","symbol","accountId","qty","side","avgEntryPrice","avgEntryFundingValue","lastTradeSequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"avgEntryPrice":{"$ref":"#/components/schemas/SignedDecimal"},"avgEntryFundingValue":{"$ref":"#/components/schemas/SignedDecimal","description":"Average of funding values at the entry times of currently open exposure, which serves as a baseline from which to compute the accrued funding in the position: units x (fundingValue - avgEntryFundingValue)"},"lastTradeSequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Sequence number of last execution taken into account for the position."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The Order object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Order":{"title":"Order","$id":"#Order","type":"object","required":["exchangeId","symbol","accountId","orderId","side","limitPx","orderType","status","createdAt","lastUpdateAt"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"orderId":{"type":"string"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"side":{"$ref":"#/components/schemas/Side"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Price at which TP/SL orders will be triggered, should not be set for other order types."},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"status":{"$ref":"#/components/schemas/OrderStatus"},"createdAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Creation timestamp (milliseconds)"},"lastUpdateAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The Account object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Account":{"title":"Account","$id":"#Account","type":"object","required":["accountId","name","type"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"name":{"type":"string"},"type":{"$ref":"#/components/schemas/AccountType"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The AccountBalance object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountBalance":{"title":"AccountBalance","$id":"#AccountBalance","type":"object","required":["accountId","asset","realBalance","balanceDEPRECATED"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"asset":{"$ref":"#/components/schemas/Asset"},"realBalance":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals) and realized pnl from closed positions. Realized pnl only applies to RUSD given it is the only settlement asset"},"balanceDEPRECATED":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Sum of account net deposits (transfers, deposits and withdrawals). This field is deprecated and will be removed in a future release"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The PerpExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecutionList":{"title":"PerpExecutionList","$id":"#PerpExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/PerpExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The SpotExecutionList object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecutionList":{"title":"SpotExecutionList","$id":"#SpotExecutionList","type":"object","required":["data","meta"],"properties":{"data":{"type":"array","items":{"$ref":"#/components/schemas/SpotExecution"}},"meta":{"$ref":"#/components/schemas/PaginationMeta"}},"additionalProperties":true},"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"},"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true}}}}
```

## The Price object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Price":{"title":"Price","$id":"#Price","type":"object","required":["symbol","updatedAt","oraclePrice"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"oraclePrice":{"$ref":"#/components/schemas/SignedDecimal","description":"Price given by the Stork feeds, used both as the peg price for prices on Reya, as well as Mark Prices. The Stork price feed is usually the perp prices across three major CEXs"},"poolPrice":{"$ref":"#/components/schemas/SignedDecimal","description":"The price currently quoted by the AMM for zero volume, from which trades are priced (equivalent to mid price in an order book); a trade of any size will be move this price up or down depending on the direction."},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Last update timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CandleHistoryData object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CandleHistoryData":{"title":"CandleHistoryData","$id":"#CandleHistoryData","type":"object","required":["t","o","h","l","c"],"properties":{"t":{"type":"array","items":{"$ref":"#/components/schemas/UnsignedInteger"},"description":"Array of timestamps (seconds)"},"o":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of opening prices"},"h":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of high prices"},"l":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of low prices"},"c":{"type":"array","items":{"$ref":"#/components/schemas/SignedDecimal"},"description":"Array of closing prices"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The CreateOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderRequest":{"title":"CreateOrderRequest","$id":"#CreateOrderRequest","type":"object","required":["exchangeId","accountId","isBuy","limitPx","orderType","signature","nonce","signerWallet"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"isBuy":{"type":"boolean","description":"Whether this is a buy order"},"limitPx":{"$ref":"#/components/schemas/SignedDecimal"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"orderType":{"$ref":"#/components/schemas/OrderType"},"timeInForce":{"$ref":"#/components/schemas/TimeInForce","description":"Order time in force, exclusively used for LIMIT orders"},"triggerPx":{"$ref":"#/components/schemas/SignedDecimal","description":"Trigger price, only for TP/SL orders"},"reduceOnly":{"type":"boolean","description":"Whether this is a reduce-only order, exclusively used for LIMIT IOC orders."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"Order nonce, see signatures and nonces section for more details."},"signerWallet":{"$ref":"#/components/schemas/Address"},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for PERP IOC orders and all SPOT orders). In seconds since epoch. The order will only be filled before this timestamp."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Optional field that allows clients to assign their own unique identifier to orders."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"},"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"},"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The CreateOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CreateOrderResponse":{"title":"CreateOrderResponse","$id":"#CreateOrderResponse","type":"object","required":["status"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"execQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Executed quantity in the current order update."},"cumQty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Total Executed quantity accross all fills where the order is involved."},"orderId":{"type":"string","description":"Created order ID (currently generated for all order types except IOC)"},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The CancelOrderRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderRequest":{"title":"CancelOrderRequest","$id":"#CancelOrderRequest","type":"object","required":["signature"],"properties":{"orderId":{"type":"string","description":"Internal matching engine order ID to cancel. Provide either orderId OR clientOrderId, not both. For spot markets, this is the order ID returned in the CreateOrderResponse."},"clientOrderId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Client-provided order ID for tracking and correlation. Provide either orderId OR clientOrderId, not both. This is the same clientOrderId provided in CreateOrderRequest."},"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID that owns the order. Required for spot markets."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Market symbol for the order.Required for spot market orders. If not provided, assumes perp market for backwards compatibility."},"signature":{"type":"string","description":"See signatures section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details. Compulsory for spot orders."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp (exclusively for SPOT orders). In seconds since epoch."}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The CancelOrderResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"CancelOrderResponse":{"title":"CancelOrderResponse","$id":"#CancelOrderResponse","type":"object","required":["status","orderId"],"properties":{"status":{"$ref":"#/components/schemas/OrderStatus"},"orderId":{"type":"string","description":"Cancelled order ID"},"clientOrderId":{"type":"integer","description":"Client-provided order ID echoed back from the request"}},"additionalProperties":true},"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```

## The MassCancelRequest object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelRequest":{"title":"MassCancelRequest","$id":"#MassCancelRequest","type":"object","required":["signature","nonce","accountId","expiresAfter"],"properties":{"accountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Account ID to cancel orders for."},"symbol":{"$ref":"#/components/schemas/Symbol","description":"Symbol to cancel orders for. If not specified, cancels orders for all symbols."},"signature":{"type":"string","description":"See signatures and nonces section for more details on how to generate."},"nonce":{"type":"string","description":"See signatures and nonces section for more details."},"expiresAfter":{"$ref":"#/components/schemas/UnsignedInteger","description":"Expiration timestamp. In seconds since epoch."}},"additionalProperties":true,"description":"Request to cancel all orders matching the specified filters"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The MassCancelResponse object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"MassCancelResponse":{"title":"MassCancelResponse","$id":"#MassCancelResponse","type":"object","required":["cancelledCount"],"properties":{"cancelledCount":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of orders that were cancelled"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The Depth object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Depth":{"title":"Depth","$id":"#Depth","type":"object","required":["symbol","type","bids","asks","updatedAt"],"properties":{"symbol":{"$ref":"#/components/schemas/Symbol"},"type":{"$ref":"#/components/schemas/DepthType"},"bids":{"type":"array","description":"Bid side levels aggregated by price, sorted descending by price","items":{"$ref":"#/components/schemas/Level"}},"asks":{"type":"array","description":"Ask side levels aggregated by price, sorted ascending by price","items":{"$ref":"#/components/schemas/Level"}},"updatedAt":{"$ref":"#/components/schemas/UnsignedInteger","description":"Snapshot generation timestamp (milliseconds)"}},"additionalProperties":true},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"},"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The ServerErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ServerErrorCode":{"title":"ServerErrorCode","$id":"#ServerErrorCode","type":"string","enum":["INTERNAL_SERVER_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Symbol object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"}}}}
```

## The UnsignedInteger object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The UnsignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The RequestErrorCode object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"RequestErrorCode":{"title":"RequestErrorCode","$id":"#RequestErrorCode","type":"string","enum":["SYMBOL_NOT_FOUND","NO_ACCOUNTS_FOUND","NO_PRICES_FOUND_FOR_SYMBOL","INPUT_VALIDATION_ERROR","CREATE_ORDER_OTHER_ERROR","CANCEL_ORDER_OTHER_ERROR","ORDER_DEADLINE_PASSED_ERROR","ORDER_DEADLINE_TOO_HIGH_ERROR","INVALID_NONCE_ERROR","UNAVAILABLE_MATCHING_ENGINE_ERROR","UNAUTHORIZED_SIGNATURE_ERROR","NUMERIC_OVERFLOW_ERROR"],"description":"Standardized error codes for API responses"}}}}
```

## The Asset object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Asset":{"title":"Asset","$id":"#Asset","type":"string","pattern":"^[A-Za-z0-9]+$"}}}}
```

## The SignedDecimal object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The TierType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TierType":{"title":"TierType","$id":"#TierType","type":"string","enum":["REGULAR","VIP"],"description":"Fee tier type (REGULAR = Standard tier, VIP = VIP tier)"}}}}
```

## The Side object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"}}}}
```

## The ExecutionType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PerpExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PerpExecution":{"title":"PerpExecution","$id":"#PerpExecution","type":"object","required":["exchangeId","symbol","accountId","qty","side","fee","price","type","timestamp","sequenceNumber"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"side":{"$ref":"#/components/schemas/Side"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"},"sequenceNumber":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution sequence number, increases by 1 for every perp execution in reya chain"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The PaginationMeta object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"PaginationMeta":{"title":"PaginationMeta","$id":"#PaginationMeta","type":"object","required":["limit","count"],"properties":{"limit":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items requested"},"count":{"$ref":"#/components/schemas/UnsignedInteger","description":"Number of items returned"},"endTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of last result, in milliseconds"},"startTime":{"$ref":"#/components/schemas/UnsignedInteger","description":"Timestamp of first result, in milliseconds"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0}}}}
```

## The DepthType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"DepthType":{"title":"DepthType","$id":"#DepthType","type":"string","enum":["SNAPSHOT","UPDATE"],"description":"Depth message type (SNAPSHOT = full book, UPDATE = single level change)"}}}}
```

## The Level object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Level":{"title":"Level","$id":"#Level","type":"object","required":["px","qty"],"properties":{"px":{"$ref":"#/components/schemas/SignedDecimal","description":"Price level"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal","description":"Aggregated quantity at this price level"}},"additionalProperties":true},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"}}}}
```

## The SpotExecution object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"SpotExecution":{"title":"SpotExecution","$id":"#SpotExecution","type":"object","required":["symbol","accountId","makerAccountId","qty","side","fee","price","type","timestamp"],"properties":{"exchangeId":{"$ref":"#/components/schemas/UnsignedInteger"},"symbol":{"$ref":"#/components/schemas/Symbol"},"accountId":{"$ref":"#/components/schemas/UnsignedInteger"},"makerAccountId":{"$ref":"#/components/schemas/UnsignedInteger","description":"Maker account ID (counterparty)"},"orderId":{"type":"string","description":"Order ID for the taker"},"makerOrderId":{"type":"string","description":"Order ID for the maker"},"side":{"$ref":"#/components/schemas/Side"},"qty":{"$ref":"#/components/schemas/UnsignedDecimal"},"price":{"$ref":"#/components/schemas/SignedDecimal"},"fee":{"$ref":"#/components/schemas/SignedDecimal"},"type":{"$ref":"#/components/schemas/ExecutionType"},"timestamp":{"$ref":"#/components/schemas/UnsignedInteger","description":"Execution timestamp (milliseconds)"}},"additionalProperties":true},"UnsignedInteger":{"title":"UnsignedInteger","$id":"#UnsignedInteger","type":"integer","minimum":0},"Symbol":{"title":"Symbol","$id":"#Symbol","type":"string","pattern":"^[A-Za-z0-9]+$","description":"Trading symbol (e.g., BTCRUSDPERP, WETHRUSD)"},"Side":{"title":"Side","$id":"#Side","type":"string","enum":["B","A"],"description":"Order side (B = Buy/Bid, A = Ask/Sell)"},"UnsignedDecimal":{"title":"UnsignedDecimal","$id":"#UnsignedDecimal","type":"string","pattern":"^\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"SignedDecimal":{"title":"SignedDecimal","$id":"#Decimal","type":"string","pattern":"^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"},"ExecutionType":{"title":"ExecutionType","$id":"#ExecutionType","type":"string","enum":["ORDER_MATCH","LIQUIDATION","ADL"],"description":"Type of execution"}}}}
```

## The Address object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"Address":{"title":"Address","$id":"#Address","type":"string","pattern":"^0x[a-fA-F0-9]{40}$"}}}}
```

## The AccountType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"AccountType":{"title":"AccountType","$id":"#AccountType","type":"string","enum":["MAINPERP","SUBPERP","SPOT"],"description":"SPOT = account that can only trade spot, MAINPERP = main perp account, SUBPERP = sub perp account"}}}}
```

## The OrderType object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderType":{"title":"OrderType","$id":"#OrderType","type":"string","enum":["LIMIT","TP","SL"],"description":"Order type, (LIMIT = Limit, TP = Take Profit, SL = Stop Loss)"}}}}
```

## The TimeInForce object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"TimeInForce":{"title":"TimeInForce","$id":"#TimeInForce","type":"string","enum":["IOC","GTC"],"description":"Order time in force (IOC = Immediate or Cancel, GTC = Good Till Cancel)"}}}}
```

## The OrderStatus object

```json
{"openapi":"3.0.3","info":{"title":"Reya DEX Trading API v2","version":"2.1.3"},"components":{"schemas":{"OrderStatus":{"title":"OrderStatus","$id":"#OrderStatus","type":"string","enum":["OPEN","FILLED","CANCELLED","REJECTED"],"description":"Order status"}}}}
```









# Websocket API Reference

## Table of Contents

1. [Overview](#overview)
2. [Server Endpoints](#server-endpoints)
3. [Channel Architecture](#channel-architecture)
4. [Message Structure](#message-structure)
5. [Channels Reference](#channels-reference)
6. [Data Types & Schemas](#data-types--schemas)
7. [Connection Management](#connection-management)

## Overview

The Reya DEX Trading WebSocket API v2 provides real-time streaming data for decentralized exchange operations on the Reya Network. This version offers user-friendly data structures with human-readable formats, removing blockchain-specific details while maintaining comprehensive trading functionality.

## Server Endpoints

### Production Environment

* **URL**: `wss://ws.reya.xyz`
* **Protocol**: WSS
* **Description**: Production WebSocket server for live trading

### Staging Environment

* **URL**: `wss://websocket-staging.reya.xyz`
* **Protocol**: WSS
* **Description**: Staging WebSocket server for pre-production testing

### Test Environment

* **URL**: `wss://websocket-testnet.reya.xyz`
* **Protocol**: WSS
* **Description**: Test WebSocket server for development

## Channel Architecture

The API uses a hierarchical channel structure with clear separation between different data types:

### Channel Categories

1. **Market Data Channels**
   * `/v2/markets/summary` - Perp market summaries
   * `/v2/market/{symbol}/summary` - Individual perp market summary
   * `/v2/market/{symbol}/perpExecutions` - Market-specific perpetual executions
   * `/v2/market/{symbol}/depth` - L2 order book depth snapshots, only relevant for markets using the Reya Order Book instead of the AMM
   * `/v2/market/{symbol}/spotExecutions` - Market-specific spot executions
   * `/v2/prices` - All symbol prices
   * `/v2/prices/{symbol}` - Individual symbol prices
2. **Wallet Data Channels**
   * `/v2/wallet/{address}/positions` - Position updates
   * `/v2/wallet/{address}/orderChanges` - Order change updates
   * `/v2/wallet/{address}/perpExecutions` - Wallet-specific perpetual executions
   * `/v2/wallet/{address}/spotExecutions` - Wallet-specific spot executions
   * `/v2/wallet/{address}/accountBalances` - Account balance updates

### Parameter Validation

#### Symbol Parameter

* **Pattern**: `^[A-Za-z0-9]+$`
* **Examples**: `BTCRUSDPERP`, `ETHRUSD`, `kBONKRUSDPERP`, `AI16ZRUSDPERP`
* **Description**: Trading symbol supporting alphanumeric characters

#### Address Parameter

* **Pattern**: `^0x[a-fA-F0-9]{40}$`
* **Example**: `0x6c51275fd01d5dbd2da194e92f920f8598306df2`
* **Description**: Ethereum wallet address (40 hexadecimal characters)

## Message Structure

All WebSocket messages follow a standardized envelope structure:

### Base Message Envelope

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/market/BTCRUSDPERP/summary",
  "data": { /* channel-specific data */ }
}
```

### Message Components

* **type**: Always `"channel_data"` for data updates
* **timestamp**: Server timestamp in milliseconds
* **channel**: Specific channel identifier
* **data**: Channel-specific payload (object or array)

### Heartbeat Messages

#### Ping Message (Server → Client)

```json
{
  "type": "ping",
  "timestamp": 1747927089946
}
```

#### Pong Message (Client → Server)

```json
{
  "type": "pong",
  "timestamp": 1747927089946
}
```

## Channels Reference

### 1. Market Data Channels

#### `/v2/markets/summary`

**Purpose**: Real-time updates for all market summaries

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/markets/summary"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/markets/summary",
  "data": [
    {
      "symbol": "BTCRUSDPERP",
      "updatedAt": 1747927089946,
      "longOiQty": "154.741",
      "shortOiQty": "154.706",
      "oiQty": "154.741",
      "fundingRate": "-0.000509373441021089",
      "longFundingValue": "412142.26",
      "shortFundingValue": "412142.26",
      "fundingRateVelocity": "-0.00000006243",
      "volume24h": "917833.49891",
      "pxChange24h": "92.6272285500004",
      "throttledOraclePrice": "2666.48162040777",
      "throttledPoolPrice": "2666.48166680625",
      "pricesUpdatedAt": 1747927089597
    }
  ]
}
```

<details>

<summary><strong>Data Type - MarketSummary</strong></summary>

* `symbol` (string): Trading symbol
* `updatedAt` (integer): Last calculation timestamp (milliseconds)
* `longOiQty` (string): Long open interest in lots
* `shortOiQty` (string): Short open interest in lots
* `oiQty` (string): Total open interest quantity
* `fundingRate` (string): Current hourly funding rate
* `longFundingValue` (string): Current long funding value
* `shortFundingValue` (string): Current short funding value
* `fundingRateVelocity` (string): Funding rate velocity
* `volume24h` (string): 24-hour trading volume
* `pxChange24h` (string, optional): 24-hour price change
* `throttledOraclePrice` (string, optional): Last oracle price at summary update
* `throttledPoolPrice` (string, optional): Last pool price at summary update
* `pricesUpdatedAt` (integer, optional): Last price update timestamp

</details>

#### `/v2/market/{symbol}/summary`

**Purpose**: Real-time updates for a specific market's summary

**Parameters**:

* `symbol`: Trading symbol (e.g., `BTCRUSDPERP`, `kBONKRUSDPERP`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/market/BTCRUSDPERP/summary"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/market/BTCRUSDPERP/summary",
  "data": {
    "symbol": "BTCRUSDPERP",
    "updatedAt": 1747927089946,
    "longOiQty": "154.741",
    "shortOiQty": "154.706",
    "oiQty": "154.741",
    "fundingRate": "-0.000509373441021089",
    "longFundingValue": "412142.26",
    "shortFundingValue": "412142.26",
    "fundingRateVelocity": "-0.00000006243",
    "volume24h": "917833.49891",
    "pxChange24h": "92.6272285500004",
    "throttledOraclePrice": "2666.48162040777",
    "throttledPoolPrice": "2666.48166680625",
    "pricesUpdatedAt": 1747927089597
  }
}
```

<details>

<summary><strong>Data Type - MarketSummary</strong></summary>

Same as above - see `/v2/markets/summary` channel for complete field definitions.

</details>

#### `/v2/market/{symbol}/perpExecutions`

**Purpose**: Real-time perpetual executions for a specific market

**Parameters**:

* `symbol`: Trading symbol (e.g., `BTCRUSDPERP`, `AI16ZRUSDPERP`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/market/BTCRUSDPERP/perpExecutions"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/market/BTCRUSDPERP/perpExecutions",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "BTCRUSDPERP",
      "accountId": 12345,
      "qty": "1.0",
      "side": "B",
      "price": "43000.00",
      "fee": "0.50",
      "type": "ORDER_MATCH",
      "timestamp": 1747927089946,
      "sequenceNumber": 152954
    }
  ]
}
```

<details>

<summary><strong>Data Type - PerpExecution</strong></summary>

* `exchangeId` (integer): Exchange identifier
* `symbol` (string): Trading symbol
* `accountId` (integer): Account identifier
* `qty` (string): Execution quantity
* `side` (Side): Execution side (B=Buy, A=Sell)
* `fee` (string): Execution fee
* `price` (string): Execution price
* `type` (ExecutionType): Execution type (ORDER\_MATCH, LIQUIDATION, ADL)
* `timestamp` (integer): Execution timestamp (milliseconds)
* `sequenceNumber` (integer): Global sequence number

</details>

#### `/v2/prices`

**Purpose**: Real-time price updates for all symbols

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/prices"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/prices",
  "data": [
    {
      "symbol": "BTCRUSDPERP",
      "oraclePrice": "43000.00",
      "poolPrice": "42999.50",
      "updatedAt": 1747927089946
    },
    {
      "symbol": "ETHRUSDPERP",
      "oraclePrice": "2500.00",
      "poolPrice": "2499.75",
      "updatedAt": 1747927089946
    }
  ]
}
```

<details>

<summary><strong>Data Type - Price</strong></summary>

* `symbol` (string): Trading symbol
* `oraclePrice` (string): Oracle price - Price given by the Stork feeds, used both as the peg price for prices on Reya, as well as Mark Prices
* `poolPrice` (string, optional): Pool price - The price currently quoted by the AMM for zero volume
* `updatedAt` (integer): Last update timestamp (milliseconds)

</details>

#### `/v2/prices/{symbol}`

**Purpose**: Real-time price updates for a specific symbol

**Parameters**:

* `symbol`: Trading symbol (e.g., `BTCRUSDPERP`, `kBONKRUSDPERP`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/prices/BTCRUSDPERP"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/prices/BTCRUSDPERP",
  "data": {
    "symbol": "BTCRUSDPERP",
    "oraclePrice": "43000.00",
    "poolPrice": "42999.50",
    "updatedAt": 1747927089946
  }
}
```

<details>

<summary><strong>Data Type - Price</strong></summary>

Same as above - see `/v2/prices` channel for complete field definitions.

</details>

#### `/v2/market/{symbol}/depth`

**Purpose**: Real-time L2 order book depth snapshots for a specific market

**Parameters**:

* `symbol`: Trading symbol (e.g., `BTCRUSDPERP`, `DOGERUSDPERP`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/market/BTCRUSDPERP/depth"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/market/BTCRUSDPERP/depth",
  "data": {
    "symbol": "BTCRUSDPERP",
    "type": "SNAPSHOT",
    "bids": [
      { "px": "42999.50", "qty": "1.5" },
      { "px": "42998.00", "qty": "2.0" }
    ],
    "asks": [
      { "px": "43000.50", "qty": "1.0" },
      { "px": "43001.00", "qty": "3.0" }
    ],
    "updatedAt": 1747927089946
  }
}
```

<details>

<summary><strong>Data Type - Depth</strong></summary>

* `symbol` (string): Trading symbol
* `type` (DepthType): Depth message type (SNAPSHOT, UPDATE)
* `bids` (array): Bid side levels aggregated by price, sorted descending by price
  * `px` (string): Price level
  * `qty` (string): Aggregated quantity at this price level
* `asks` (array): Ask side levels aggregated by price, sorted ascending by price
  * `px` (string): Price level
  * `qty` (string): Aggregated quantity at this price level
* `updatedAt` (integer): Snapshot generation timestamp (milliseconds)

</details>

#### `/v2/market/{symbol}/spotExecutions`

**Purpose**: Real-time spot executions for a specific market

**Parameters**:

* `symbol`: Trading symbol (e.g., `ETHRUSD`, `BTCRUSD`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/market/ETHRUSD/spotExecutions"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/market/ETHRUSD/spotExecutions",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "ETHRUSD",
      "accountId": 12345,
      "makerAccountId": 67890,
      "orderId": "63552420354981888",
      "makerOrderId": "63552420037263360",
      "qty": "1.0",
      "side": "B",
      "price": "2500.00",
      "fee": "0.0",
      "type": "ORDER_MATCH",
      "timestamp": 1747927089946
    }
  ]
}
```

<details>

<summary><strong>Data Type - SpotExecution</strong></summary>

* `exchangeId` (integer, optional): Exchange identifier
* `symbol` (string): Trading symbol
* `accountId` (integer): Account identifier (taker)
* `makerAccountId` (integer): Maker account ID (counterparty)
* `orderId` (string, optional): Order ID for the taker
* `makerOrderId` (string, optional): Order ID for the maker
* `qty` (string): Execution quantity
* `side` (Side): Execution side (B=Buy, A=Sell)
* `price` (string): Execution price
* `fee` (string): Execution fee
* `type` (ExecutionType): Execution type (ORDER\_MATCH, LIQUIDATION, ADL)
* `timestamp` (integer): Execution timestamp (milliseconds)

</details>

***

### 2. Wallet Data Channels

#### `/v2/wallet/{address}/positions`

**Purpose**: Real-time position updates for a wallet

**Parameters**:

* `address`: Ethereum wallet address (e.g., `0x6c51275fd01d5dbd2da194e92f920f8598306df2`)

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/positions"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/positions",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "BTCRUSDPERP",
      "accountId": 12345,
      "qty": "1.5",
      "side": "B",
      "avgEntryPrice": "43000.00",
      "avgEntryFundingValue": "100.25",
      "lastTradeSequenceNumber": 152954
    }
  ]
}
```

<details>

<summary><strong>Data Type - Position</strong></summary>

* `exchangeId` (integer): Exchange identifier
* `symbol` (string): Trading symbol
* `accountId` (integer): Account identifier
* `qty` (string): Position quantity
* `side` (Side): Position side (B=Buy, A=Sell)
* `avgEntryPrice` (string): Average entry price
* `avgEntryFundingValue` (string): Average entry funding value
* `lastTradeSequenceNumber` (integer): Last execution sequence number

</details>

#### `/v2/wallet/{address}/orderChanges`

**Purpose**: Real-time order change updates for wallet

**Parameters**:

* `address`: Ethereum wallet address

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/orderChanges"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/orderChanges",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "BTCRUSDPERP",
      "accountId": 12345,
      "orderId": "123456789-123123123",
      "qty": "1.0",
      "execQty": "0.5",
      "side": "B",
      "limitPx": "43000.00",
      "orderType": "LIMIT",
      "triggerPx": "50000.0",
      "timeInForce": "GTC",
      "reduceOnly": false,
      "status": "OPEN",
      "createdAt": 1747927089946,
      "lastUpdateAt": 1747927089946
    }
  ]
}
```

<details>

<summary><strong>Data Type - Order</strong></summary>

* `exchangeId` (integer): Exchange identifier
* `symbol` (string): Trading symbol
* `accountId` (integer): Account identifier
* `side` (Side): Order side (B=Buy, A=Sell)
* `limitPx` (string): Limit price
* `orderType` (OrderType): Order type (LIMIT, TP, SL)
* `status` (OrderStatus): Order status (OPEN, FILLED, CANCELLED, REJECTED)
* `createdAt` (integer): Creation timestamp (milliseconds)
* `lastUpdateAt` (integer): Last update timestamp (milliseconds)
* `orderId` (string): Order identifier
* `qty` (string, optional): Order quantity
* `execQty` (string, optional): Executed quantity in the current order update
* `cumQty` (string, optional): Total executed quantity across all fills
* `triggerPx` (string, optional): Trigger price for TP/SL orders
* `timeInForce` (TimeInForce, optional): Time in force (IOC, GTC)
* `reduceOnly` (boolean, optional): Reduce-only flag (exclusively for LIMIT IOC orders)

</details>

#### `/v2/wallet/{address}/perpExecutions`

**Purpose**: Real-time perpetual execution updates for a wallet

**Parameters**:

* `address`: Ethereum wallet address

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/perpExecutions"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/perpExecutions",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "BTCRUSDPERP",
      "accountId": 12345,
      "qty": "1.0",
      "side": "B",
      "price": "43000.00",
      "fee": "0.50",
      "type": "ORDER_MATCH",
      "timestamp": 1747927089946,
      "sequenceNumber": 152954
    }
  ]
}
```

<details>

<summary><strong>Data Type - PerpExecution</strong></summary>

Same as above - see `/v2/market/{symbol}/perpExecutions` channel for complete field definitions.

</details>

#### `/v2/wallet/{address}/spotExecutions`

**Purpose**: Real-time spot execution updates for a wallet

**Parameters**:

* `address`: Ethereum wallet address

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/spotExecutions"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/spotExecutions",
  "data": [
    {
      "exchangeId": 1,
      "symbol": "ETHRUSD",
      "accountId": 12345,
      "makerAccountId": 67890,
      "orderId": "63552420354981888",
      "makerOrderId": "63552420037263360",
      "qty": "1.0",
      "side": "B",
      "price": "2500.00",
      "fee": "0.0",
      "type": "ORDER_MATCH",
      "timestamp": 1747927089946
    }
  ]
}
```

<details>

<summary><strong>Data Type - SpotExecution</strong></summary>

Same as above - see `/v2/market/{symbol}/spotExecutions` channel for complete field definitions.

</details>

#### `/v2/wallet/{address}/accountBalances`

**Purpose**: Real-time account balance updates for a wallet

**Parameters**:

* `address`: Ethereum wallet address

**Subscription**:

```json
{
  "type": "subscribe",
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/accountBalances"
}
```

**Message Structure**:

```json
{
  "type": "channel_data",
  "timestamp": 1747927089946,
  "channel": "/v2/wallet/0x6c51275fd01d5dbd2da194e92f920f8598306df2/accountBalances",
  "data": [
    {
      "accountId": 12345,
      "asset": "WSTETH",
      "realBalance": "1.25",
      "balance_DEPRECATED": "1.25"
    }
  ]
}
```

<details>

<summary><strong>Data Type - AccountBalance</strong></summary>

* `accountId` (integer): Account identifier
* `asset` (string): Asset symbol (e.g., WSTETH, RUSD)
* `realBalance` (string): Sum of account net deposits and realized PnL from closed positions
* `balance_DEPRECATED` (string): Sum of account net deposits only (deprecated, will be removed)

</details>

## Data Types & Schemas

### Enumeration Types

<details>

<summary><strong>Side</strong> - Order/position side indicator</summary>

* `B`: Buy/Bid
* `A`: Ask/Sell

</details>

<details>

<summary><strong>ExecutionType</strong> - Type of execution that occurred</summary>

* `ORDER_MATCH`: Regular order matching
* `LIQUIDATION`: Liquidation execution
* `ADL`: Auto-deleveraging execution

</details>

<details>

<summary><strong>OrderStatus</strong> - Current status of an order</summary>

* `OPEN`: Order is active and can be filled
* `FILLED`: Order has been completely filled
* `CANCELLED`: Order has been cancelled
* `REJECTED`: Order was rejected

</details>

<details>

<summary><strong>OrderType</strong> - Type of order placed</summary>

* `LIMIT`: Limit order
* `TP`: Take profit order
* `SL`: Stop loss order

</details>

<details>

<summary><strong>TimeInForce</strong> - Order duration specification</summary>

* `IOC`: Immediate or Cancel
* `GTC`: Good Till Cancel

</details>

<details>

<summary><strong>DepthType</strong> - Order book depth message type</summary>

* `SNAPSHOT`: Full order book snapshot
* `UPDATE`: Single level change update

</details>

<details>

<summary><strong>AccountType</strong> - Account type classification</summary>

* `MAINPERP`: Main perpetual trading account
* `SUBPERP`: Sub perpetual trading account
* `SPOT`: Spot trading only account

</details>

## Connection Management

### Heartbeat Management

The API implements a ping/pong heartbeat mechanism:

1. **Server Ping**: Server sends periodic ping messages
2. **Client Pong**: Client must respond with pong messages
3. **Connection Health**: Failure to respond may result in disconnection

### Connection Best Practices

1. **Implement Reconnection Logic**: Handle connection drops gracefully
2. **Manage Subscriptions**: Track active subscriptions for reconnection
3. **Handle Backpressure**: Process messages efficiently to avoid buffer overflow
4. **Monitor Latency**: Track message timestamps for performance monitoring
5. **Validate Messages**: Verify message structure and required fields

### Control Messages

#### Subscribe Message (Client → Server)

```json
{
  "type": "subscribe",
  "channel": "/v2/markets/summary",
  "id": "req123"
}
```

#### Subscribed Confirmation (Server → Client)

```json
{
  "type": "subscribed",
  "channel": "/v2/markets/summary",
  "contents": { /* optional initial data */ }
}
```

#### Unsubscribe Message (Client → Server)

```json
{
  "type": "unsubscribe",
  "channel": "/v2/markets/summary",
  "id": "req123"
}
```

#### Unsubscribed Confirmation (Server → Client)

```json
{
  "type": "unsubscribed",
  "channel": "/v2/markets/summary"
}
```

#### Error Message (Server → Client)

```json
{
  "type": "error",
  "message": "Invalid channel",
  "channel": "/v2/invalid/channel"
}
```



https://github.com/Reya-Labs/reya-python-sdk










# Smart Contract Withdrawals

As shown in the dApp funds on Reya Network are non-custodial and available to withdraw at anytime. You may use the withdrawal buttons on the dApp, or alternative you can withdraw directly from the Reya Network smart contracts.

**Follow the guide below to withdraw from the smart contracts.**

***

1. Bridge ETH to Reya Network for gas fees and Socket bridge fees by using this bridge: <https://bridge.gelato.network/bridge/reya-network>. Note that:

   1. The bridge does not support ETH withdrawals for the time being, so make sure you don’t bridge too much ETH.
   2. Trading on Reya Network is made gas-free via a relayer architecture, if you’re interacting with the contracts directly you will need to pay a small amount of gas (hence the ETH needed).

   ![](https://docs.reya.network/~gitbook/image?url=https%3A%2F%2F4172979140-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIHVxf7CaLQzjdZ5a8tyE%252Fuploads%252FaYn82zYOMm7iFAfnjhYp%252Fimage.png%3Falt%3Dmedia%26token%3D175dfb8f-b628-418b-8ed0-6874fd01cdbd\&width=768\&dpr=4\&quality=100\&sign=2bfc19e9\&sv=2)
2. Withdraw funds from the Passive Pool into your wallet on Reya Network by calling the removeLiquidity function here: <https://usecannon.com/packages/reya-omnibus/latest/1729-main/interact/reya-omnibus/PassivePoolProxy/0xB4B77d6180cc14472A9a7BDFF01cc2459368D413#selector-0x0b7c92f9>. To do this, you need to input the following parameters:

   1. poolId: 1
   2. sharesAmount: the amount you want to withdraw multiplied by 10^30 (10 to the power of 30).
   3. minAmount: the amount you want to withdraw multiplied by 10^6

   For example, if you want to withdraw 99.5 rUSD, the parameters will be:

   1. poolId: 1
   2. sharesAmount: 99500000000000000000000000000000
   3. minAmount: 99500000
3. Unwrap rUSD into USDC by calling the withdraw function here: <https://usecannon.com/packages/reya-omnibus/latest/1729-main/interact/reya-omnibus/RUSDProxy/0xa9F32a851B1800742e47725DA54a09A7Ef2556A3#selector-0x2e1a7d4d>. To do this, you need to input the following parameters:
   1. amount: the amount withdrawn at the previous step, same as minAmount (multiplied by 1000000). For example, if you withdrawn 99.5 rUSD, the parameters will be amount = 99500000
4. Confirm you have USDC in your Reya Wallet.
   1. Add the chain to your wallet. There is a link in the footer of: <https://explorer.reya.network/> ![](https://docs.reya.network/~gitbook/image?url=https%3A%2F%2F4172979140-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIHVxf7CaLQzjdZ5a8tyE%252Fuploads%252FmQFS3KfuEx5eVQamrkW2%252Fimage.png%3Falt%3Dmedia%26token%3Db0825ced-080e-4ee0-9a0d-d9c8df6e03b3\&width=300\&dpr=4\&quality=100\&sign=aa83514e\&sv=2)
   2. Add the token at address: 0x3B860c0b53f2e8bd5264AA7c3451d41263C933F2 For example using Metamask: ![](https://docs.reya.network/~gitbook/image?url=https%3A%2F%2F4172979140-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIHVxf7CaLQzjdZ5a8tyE%252Fuploads%252FlagVs3y8tJKlcI7VKyfG%252Fimage.png%3Falt%3Dmedia%26token%3D6513882f-6622-462f-b389-334a9149f93d\&width=300\&dpr=4\&quality=100\&sign=7f0b7758\&sv=2) Enter the contract address and the symbol and decimals should auto-populate. Press Next ![](https://docs.reya.network/~gitbook/image?url=https%3A%2F%2F4172979140-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIHVxf7CaLQzjdZ5a8tyE%252Fuploads%252FDRHuHJdi2GeZp76DMDkc%252Fimage.png%3Falt%3Dmedia%26token%3D594bf99b-00ef-4112-8834-b278aa77be9e\&width=300\&dpr=4\&quality=100\&sign=d475d9df\&sv=2)
5. Once confirmed, you should bridge funds from Reya Network to a source chain (Ethereum Mainnet/Arbitrum/Optimism/Polygon). To do this, you have to call the bridge function on the Socket contract here: <https://explorer.reya.network/address/0x1d43076909Ca139BFaC4EbB7194518bE3638fc76?tab=write_contract#405e720a>.

   ![](https://docs.reya.network/~gitbook/image?url=https%3A%2F%2F4172979140-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIHVxf7CaLQzjdZ5a8tyE%252Fuploads%252FIImwsvtmdBvDQQD9BG05%252Fimage.png%3Falt%3Dmedia%26token%3Dfd994820-d3b2-42ba-abca-d2ff0b66b4d3\&width=300\&dpr=4\&quality=100\&sign=c66e47c8\&sv=2) To do this, you have to provide the following parameters:

   1. receiver: your wallet address on the source chain (the chain you are withdrawing to)
   2. amount: the amount withdrawn at the previous steps, same as minAmount (still multiplied by 1000000).
      1. note: the pull down at the end of the row will help you multiply by 10^6 but this number should be the same as the one used in the previous steps
   3. msgGasLimit: 10000000
   4. connector: the socket connector address assigned to the source chain you want to withdraw to.

      NetworkConnector Address

      Ethereum Mainnet

      0x807B2e8724cDf346c87EEFF4E309bbFCb8681eC1

      Arbitrum

      0x663dc7E91157c58079f55C1BF5ee1BdB6401Ca7a

      Optimism

      0xe48AE3B68f0560d4aaA312E12fD687630C948561

      Polygon

      0x54CAA0946dA179425e1abB169C020004284d64D3
   5. execPayload: 0x
   6. options: 0x
   7. Send native ETH (uint256): the socket bridge fees. As these are dynamic, you can use 10000000000000000 to account for most cases (this is equivalent to 0.01 ETH). Note that you can use lower amount as well (e.g. 1000000000000000, which is equivalent to 0.001 ETH), but it might fail if Socket fees increase.

   Upon completion of these steps, funds should be in the destination wallet address entered, on the network corresponding to the network connecter address used, in 10-15min. If you have not received your funds after an hour, please open a support ticket in our Discord and we can try and help.
