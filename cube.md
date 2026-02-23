
## About

Cube is a hybrid exchange built from first principles for the future of digital
and traditional asset trading. At it's core, a low-latency matching engine
powers trading at 200'000 operations per second with 200µs latency, and a
decentralized settlement layer powers a non-custodial peer-to-peer settlement
that ensures the safety of your assets.

## Overview

This documentation covers a large part of the Cube API, and is roughly
organized into the following:

- [Exchange Info](/exchange-info.md): Information about the exchange, such as
  assets, markets, account management, and more.
- [Market Data](/market-data/rest-api.md): Market data, including level 3 (order by
  order) book data, trade summaries, and more.
- [Order Entry](/order-entry/rest-api.md): Trading and order management.
- [Perpetual Futures](/perpetual-futures/README.md): Information about our
  perpetual futures contracts, including contract specifications, margin
  requirements, funding, settlement, and liquidation.
- [Fees](/cube-fees.md): Information about fees on Cube.

### Connectivity

- **REST**: For market data snapshots and order entry.
- **Websocket**: For realtime market data and trading.
- **TCP FIX and UDP Multicast**: Out lowest latency connectivity. Reach out for
  more information.


## Environments

If you're interested in building with us, reach out about getting access to our
staging environment, where you can test your integrations before going live!

## Contact

Reach out to us at [engineering@cube.xyz](mailto:engineering@cube.xyz) for
questions or feedback!
The base URL for endpoints described in this page of live trading API is `https://api.cube.exchange/ir/v0`.

[OpenAPI document for Market & User API](/generated/core/ir_api_30.json)

## Market Definitions

Definitions are [available as JSON](https://api.cube.exchange/ir/v0/markets)
and provide all of the information needed to convert between on-chain amounts
and the values used on the exchange.  For further details, see the [Trade Api](/trade-api.md).

### Market Status Field

Some trading pairs appear in multiple markets,
but only a single market will be in use
for a given trading pair at any given time.

Definitions appear for markets that are no longer in use; these can be used to interpret historical orders.

- Markets that are currently active for trading will have a `status` of `1` or `2`.
- Markets that are no longer in use will have a `status` of `3`.

## Authentication Headers

The REST API uses the following HTTP headers for authentication:

* `x-api-key`:\
  The API Key ID, as specified on the [API settings page](https://cube.exchange/settings/api).
    * Each API key has an associated access level, which is determined at the time of key creation.
        * Read access allows only read HTTP methods (GET, HEAD, etc.).
        * Write access permits all HTTP methods.
* `x-api-signature`:\
  The API signature string authenticating this request.
    * The payload to be signed is a concatenation of the byte string `cube.xyz` and the current Unix epoch timestamp in seconds, converted into an 8-byte little-endian array. The signature is the HMAC-SHA256 digest of the payload, using the secret key associated with the specified API key.
    * Implementation notes:
        * The signature is base-64 encoded with the 'standard' alphabet and padding: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`.
        * The timestamp should be encoded as an 8-byte little-endian array of bytes.
        * The secret key should be decoded from a hex string into a 32-byte array of bytes.
* `x-api-timestamp`:\
  The timestamp used for signature generation.

## Endpoints, public

{% swagger src="/generated/core/ir_api_30.json" path="/markets" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/history/klines" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

## Endpoints, authentication required

Endpoints in this section require [REST Authentication
headers](#authentication-headers).

{% swagger src="/generated/core/ir_api_30.json" path="/users/check" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/apikeys" method="post" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/apikeys/{api_key}" method="delete" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccounts" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccounts" method="post" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}" method="patch" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/positions" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/transfers" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/deposits" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/withdrawals" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/orders" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/subaccount/{subaccount_id}/fills" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/fee-estimates" method="post" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/address" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/address/settings" method="get" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/ir_api_30.json" path="/users/withdraw" method="post" %}
[ir_api_30.json](/generated/core/ir_api_30.json)
{% endswagger %}
This page describes the various fees charged by Cube.

## Trading Fees

Trading Fees are calculated on each individual **fill** as a ratio of the filled quantity,
and are always charged as a deduction from the asset received in that trade.

The amount of the fee is indicated on Fill acknowlegements by a Fee Ratio
expressed as a fixed-point decimal number consisting of a mantissa and an exponent.
Generally, the exponent will be "-4", indicating that the mantissa is equivalent to pips,
Though some fees may be expressed with greater granularity.

### Example

Consider the case of a trade resulting in a credit of 5 Bitcoin:
- Asset received is BTC
- `fee_ratio.mantissa` = 11
- `fee_ratio.exponent` = -4

...in which case:
- The fee ratio would be 0.0011, or 11 pips.
- The fee would be equal to 0.0055 BTC.
- The total amount credited at settlement would be 4.9945 BTC.

If you need exact granularity at time of trade, you can replicate the fee calculation performed by the exchange.
To avoid rounding errors, this entire process is performed in integer math using the exponent as a divisor.
In the example above, the full fee amount in indivisible [RawUnits](/order-entry/websocket-api.md#rawunits) would be calculated as:
```text
5 * 100_000_000 * 11 / 10_000 = 550_000 RawUnits

(in the BTC case, that would be 550,000 Satoshi)
```

Since the fee is expressed with a decimal exponent, it's possible that this calculation results in a non-whole number.
Since `RawUnit`s are indivisible, the fee must be a whole number,
so it's rounded down to the nearest `RawUnit` during the final truncating division.

# Implied Match Fee

Each aggressing order into a market enabled for implied match may incur a fee,
the value of which will always be less than a single lot of either the base or quote asset from that market,
using the lot sizes from the source markets providing the implied liquidity.

Unlike the Trading Fee, the Implied Match Fee is calculated per-order rather than per-fill.
The amount is based on the prices and quantities executed,
as well as the relationship between the lot sizes in the different markets,
i.e. the number of fills in the match does not affect the amount of the fee.

See the [documentation on Implied Matching](./implied-matching.md#ImpliedMatchFee) for a detailed desciption.
Certain markets will be enabled for Implied Matching.  In these markets, aggressing orders may be matched against other markets' books
when doing so would result in a better price than matching against resting orders in the market where the order was placed.

## Terminology and Concept
Consider a trade in an ETH/BTC market where the price of ETH/BTC is implied via ETH/USDC and BTC/USDC.  In this case:
- ETH is the base asset
- BTC is the quote asset
- USDC is the implied-through asset
- ETH/USDC is the source market for the base asset
- BTC/USDC is the source market for the quote asset

In this case, there are two sets of orders for the ETH/BTC pair:
- The direct market, consisting of the order book for the ETH/BTC market.
- The implied market, calculated from the orders on the source base and source quote markets.

The term "implied match" describes such a match against the orders in the source markets,
while the term "direct match" describes a match against orders on the book
in the same market as the aggressing order.

An aggressing Bid in ETH/BTC triggering an implied match would result in:
- first, selling the BTC in the BTC/USDC market to acquire the implied-through asset, USDC
- second, using that USDC to Buy ETH in the ETH/USDC market

... thus executing the intent of the original order - to acquire ETH using BTC.

The same logic applies if the order is an Ask, with the markets reversed:
- first, acquire USDC by Selling ETH into the ETH/USDC market
- second, acquire BTC by Buying BTC in the BTC/USDC market using the proceeds of the first transaction

... as this would acquire BTC using ETH.

## Match Characteristics
When a match takes place in a market with implied pricing enabled:
- The match will take place against whichever of the direct and implied books offers the best price.
- If a price level is exhausted during the match, both direct and implied books will be considered again for the best price before matching further quantity
- A single match could result in a combination of direct and implied fills, but regardless of the distribution, all fills in the match are executed atomically from the perspective of all relevant markets
- Currently, only aggressing orders can match against the implied market.
  This means that price movements in the implied market could cause it to cross resting orders on the book in the direct market, creating an arbitrage opportunity.

# Implied Price

The implied price for a single fill is the ratio of the prices of the source markets.

If the aggressing order trades against multiple levels, the price will be the average of the implied prices at each executed level,  weighted by the quantity executed at each level.

Since that value may be between price levels and the API requires an integer for price, the price reported on the API will be rounded to the next price level away from the market (i.e. up for bids, down for asks).

The market data `TopOfBook` feed disseminates best bid and ask levels in separate fields for:
- the direct market
- the implied market
- the better of the two considered together

## Example Calculation

Since lot sizes can differ between markets, we need to adjust for them.  Here's one way to calculate the implied price:
```
lot size ratio = base lot size / quote lot size

lot size factor =
    ratio(implied market)
    * ratio(quote source market)
    / ratio (base source market)

implied price =
    base source market price
    / quote source market price
    * lot size factor
```

More concretely, using the markets above:
```
ETH/BTC implied price = (ETH/USDC price / BTC/USDC price) * lot size factor

If buying ETH/BTC: implied price =
    (ETH/USDC ask price / BTC/USDC bid price)
    * (ETH/BTC base lot size / ETH/BTC quote lot size)
    * (BTC/USDC base lot size / BTC/USDC quote lot size)
    / (ETH/USDC base lot size / ETH/USDC quote lot size)

If selling ETH/BTC: implied price =
    (ETH/USDC bid price / BTC/USDC ask price)  # flipped bid/ask vs. the buy case; below lines are the same
    * (ETH/BTC base lot size / ETH/BTC quote lot size)
    * (BTC/USDC base lot size / BTC/USDC quote lot size)
    / (ETH/USDC base lot size / ETH/USDC quote lot size)
```

# Implied Match Fee
Because trades in the spot markets are currency swaps and the tick size of an asset can vary between markets,
it's common that the amount of the implied-through asset that can be acquired in the first source market (in this case, the USDC)
is not evenly divisible into lots in the second market where that asset is divested.

In the event of a lot size mismatch, the Cube matching engine will:
- round out to the next worst price level (i.e. the next whole lot)
- charge a fee equal to the amount of the rounding

For example:
```text
Aggressing Bid for 1 base lot matches when Implied Price is 6.7:
  Aggressor is credited the 1 base lot
  Aggressor is debited 7 quote lots
  Cube takes implied match fee equal to 0.3 quote lots
```

Since rounding is done to the lot, the value of the fee for any given order
will always be less than a single lot of either the base or quote asset.
**Note that this is the lot size of the asset in the source market providing the liquidity,
not the market in which the aggressing order is placed.**

The [implied match example](implied-matching.md#example) contains a more precise illustration of this behavior.

## Notes on Implied Match Fee
When an aggressing order results in an implied match, the Order Service will send an `ImpliedMatchFee` message after the match completes.  This information has no effect on settlement as the amount of the fee is already accounted for in the quantities reported in each `Fill` message.

Like the per-fill trading fee, the Implied Match Fee is reported in the asset received in the trade:
- Bid => fee paid in base asset
- Ask => fee paid in quote asset

This conversion is done using the last filled price of the X/S source market, where:
- X is the asset received (either BTC or ETH in above example)
- S is the implied-through asset (USDC in above example)

Unlike the trading fee, which is charged per-fill,
the implied match fee is charged once on the entire match,
i.e. once per-order.

If the lot sizes of the source markets happen to line up perfectly,
the amount of the implied match fee will be zero.

## Notes on Trading Fee
Implied fills incur trading fees in [the same way as direct fills](cube-fees.md).

All legs of the implied trade are treated the same way as a direct fill would be in their respective books:
- the aggressing order will be charged the taker fee rate
- all resting orders involved in the match, on the books of any of the markets involved, will be charged the maker fee rate

## Calculating Amount to be Settled
The `quantity` fields in the `Fill` message reflect the amounts that will be settled:
- **Inclusive** of any implied asset fees
- **Exclusive** of any trading fees

...such that calculating the `RawUnit` amount filled remains the same as for a direct market, namely:

```text
Divested Asset:
  -(quantity * lot size)
Received Asset:
  (quantity * lot size) - trade fee amount
```

## Relationship to `fill_price`

Note that for trades resulting in an [Implied Match Fee](implied-matching.md#implied-match-fee),
**the price reported in the fill message will not equal the ratio of the quote quantity to the base quantity**,
for two reasons:
- The `fill_price` reported is net of the implied asset fee, if any
- If the implied price is fractional, it will be rounded to the next worst level due to API limitations

> ### Important
> Do not rely on the `fill_price` field when calculating `RawUnit` amounts for transacted assets.
>
> Use the `fill_quantity * base lot size` for the base asset
> and the `fill_quote_quantity * quote lot size` for the quote asset.

## Opting Out
Implied Match is a feature of the market, so there's no way to disable it for your account.

If you don't wish to participate in implied matching, or to be subject to the implied match fee,
you can still trade on these markets by sending orders as POST_ONLY.

# Detailed Example
Consider a hypothetical aggressing order to buy 5 ETH on the ETH/BTC market, assuming:
- "Price of Best Order" is the price of the side that would be hit during the implied match
- There's more than enough quantity at that price level in both source markets to fill the aggressing order via implied match
- Structure is:

| Asset | Decimals | Name of Raw Units* |
|-------|----------|--------------------|
| BTC   | 8        | satoshi            |
| ETH   | 18       | wei                |
| USDC  | 6        | rawUSDC            |

*referenced in description below to reduce ambiguity

| Market    | Role     | Base Lot Size | Quote Lot Size | Price of Best Order On Book*            |
|-----------|----------|---------------|----------------|-----------------------------------------|
| BTC/USDC  | source   | 1e3           | 1e0            | 692,000  (= 1 BTC to 69,200 USDC)       |
| ETH/USDC  | source   | 1e15          | 1e1            | 350,000  (= 1 ETH to 3,500 USDC)        |
| ETH/BTC   | implied  | 1e16          | 1e0            | book is empty (i.e. will implied match) |

*integer value as entered on API; defined as `number of quote lots per base lot`

### Value of Traded Assets

In human-readable terms, this trade will exchange:

```
5 ETH for 0.2529 BTC
via 17,500.68 USDC (of which 0.68 USDC will be taken as an Implied Match Fee)
```

### Aggressing Order Calculation (API)

#### Implied Price
The implied price in the implied market is:
```text
(ETH/USDC price / BTC/USDC price) * lot size factor
= 350,000 / 692,000 * 1e5
= 50,578.035
```

#### Matching Process

1. Aggressing order to Buy 5 ETH on the ETH/BTC market:
    - ETH decimals is 18, i.e. 1 ETH = 1e18 wei
    - Order amount = 5 ETH * 1e18 = 5e18 wei

2. Need to acquire 5e18 wei in the ETH/USDC market:
    - Hit ask at price 350,000: for every 1e15 wei, we will need to pay 350,000 * 1e1 = `3,500,000 rawUSDC`
    - 5e18 wei / 1e15 * 3,500,000 = `17,500,000,000 rawUSDC`

3. How much BTC will we have to sell in the BTC/USDC market to acquire the 1.75e10 rawUSDC needed to cover that purchase?
    - Hit bid at price 692,000: for every 1000 satoshis, we will receive 692,000 * 1e0 = `692,000 rawUSDC` (because quote lot size is 1)
    - 17,500,000,000 rawUSDC / price of 692,000 = `25,289.0173 base lots` in the BTC/USDC market

4. This presents an issue as we can only transact in whole lots, which in this case means whole multiples of 1000 satoshis.  To compensate:
    - We round up and oversell `25,290 lots` of BTC into the BTC/USDC market
    - The fractional `0.9827 lots` of BTC will be taken as the Implied Match Fee

#### Filled Legs

The resulting fill will consist of three legs, one in each market.

Pricing in lots, based on the amount transacted and lot size in each market:
- ETH/BTC:
  - base lots = 5e18 wei / 1e16 = `500`
  - quote lots = 25,290,000 satoshis / 1e0 = `25,290,000` (from step 4)
  - price = `50,579` (implied price rounded up, since this is a Bid)
- ETH/USDC:
  - base lots = 5e18 wei / 1e15 = `5000`
  - quote lots = 17,500,000,000 rawUSDC / 1e1 = `1,750,000`
  - price = `350,000` (price level of the resting order)
- BTC/USDC:
  - base lots = `25290` (from step 4)
  - quote lots = 17,500,680,000 rawUSDC / 1e0 = `17,500,680,000`
  - price = `692,000` (price level of the resting order)

Note that in the aggressed market, ETH/BTC,
**the implied price is not the ratio of the base/quote (50,580)**
because it's inclusive of the Implied Match Fee.

## Price, Quantity, and Lots

All orders are placed on a single market, specified by the market-id. The
market definition specifies the base and quote assets and their respective
lot sizes for the particular market. Prices and quantities in this API are in
units of base and quote _lots_. That is, a quantity of 1 equals 1 base lot,
and a price of 10 equals 10 quote lots / base lot (read as quote lots per
base lot).

For example, consider an ETH/BTC market. ETH is the base asset and BTC is the
quote asset. ETH has 18 decimal places (`1 ETH = 10^18 WEI`) and BTC has 8
decimal places (`1 BTC = 10^8 SAT`). Suppose that in this example, the ETH/BTC
market has a base lot size of `10^15` and a quote lot size of `10^0` (`1`).
Then an order placed with `quantity = 230` and `limit price = 6300` in
market-agnostic terms is an order for `0.23 ETH` at a price of `0.06300 BTC /
ETH`, calculated from:

```text
230 base lots
  * (10^15 WEI / base lot)
  / (10^18 WEI / ETH)
  = 0.230 ETH

6300 quote lots / base lot
  * (1 SAT / quote lot)
  / (10^15 WEI / base lot)
  * (10^18 WEI / ETH)
  / (10^8 SAT / BTC)
  = 0.06300 BTC / ETH
```

When calculating `RawUnit` amounts for transacted assets, e.g. for reconciliation,
**use the `fill_quantity * base lot size` for the base asset
and the `fill_quote_quantity * quote lot size` for the quote asset**.

When orders are filled in a market enabled for implied matching,
**the price may not reflect the exact ratio between the base and quote asset transacted**.
See [Implied Matching](implied-matching.md) for more details.

## Exchange Order ID

Each order is assigned a unique ID by the exchange. This order ID is
consistent across modifies (including cancel-replace), and other operations.
The exchange order ID can be used to find a particular order in the
market-by-order market data feed, which allows the determination of FIFO
queue priority, etc.

## Transact Time

The transact time is the matching engine timestamp for when an event is
processed. Events that occur with the same transact time occur atomically
from the perspective of the matching engine.
The base URL for endpoints described in this page of live trading API is `https://api.cube.exchange/md/v0`.

Definitions for requests and responses can be found in the [Market Data OpenAPI Document](/generated/core/md_api_30.json).

Further specifics for field enums, reject codes, etc. can be found in the [Market Data API Websocket Documentation](./websocket-api.md).

## Endpoints, public

Endpoints in this section do not require authentication.

{% swagger src="/generated/core/md_api_30.json" path="/book/{market_id}/snapshot" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/md_api_30.json" path="/book/{market_id}/recent-trades" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/md_api_30.json" path="/tickers/snapshot" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/md_api_30.json" path="/parsed/tickers" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/md_api_30.json" path="/parsed/book/{market_symbol}/snapshot" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/md_api_30.json" path="/parsed/book/{market_symbol}/recent-trades" method="get" %}
[md_api_30.json](/generated/core/md_api_30.json)
{% endswagger %}
# WebSocket: Market Data API

This schema defines the Protobuf messages used for communication with the
Cube Market Data Service (Mendelev, MD). The `proto` definition file can be
found [here](https://github.com/cubexch/ws-api/blob/main/schema/market_data.proto).

### Order Book Data

The market data service exposes a websocket endpoint for order book data for
a given market at `wss://api.cube.exchange/md/book/:market_id`. The order
book can be consumed by both
price level through the Market by Price (MBP) and order-by-order through the
Market by Order (MBO). In addition, clients can subscribe to the trade stream
and price candlesticks.

Upon connection, clients should submit a [`Config`](#config) and then
process a stream of [`MdMessages`](#mdmessages).
Note that this message type is distinct from the [`MdMessage`](#mdmessage),
where the former is a wrapper containing one or more of the latter.

### Aggregate Book Tops Data

The market data service exposes a websocket endpoint for aggregated
tops-of-book for all markets at `wss://api.cube.exchange/md/tops`. Client
should process [`AggMessage`](#aggmessage).

### Heartbeats

Application-level heartbeats are expected every 30 seconds. If more than one
interval is missed, the market data service will disconnect the websocket.



## MdMessage
Every exchange message from `/book/:market_id` will be wrapped as an
[`MdMessages`](#mdmessages) which contains multiple `MdMessage`'s.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| heartbeat | [Heartbeat](#heartbeat) |  | Server heartbeat reply |
| summary | [Summary](#summary) |  | 24h summary |
| trades | [Trades](#trades) |  | Recent trades |
| mbo_snapshot | [MarketByOrder](#marketbyorder) |  | Market by order snapshot |
| mbo_diff | [MarketByOrderDiff](#marketbyorderdiff) |  | Market by order diff |
| mbp_snapshot | [MarketByPrice](#marketbyprice) |  | Market by price snapshot |
| mbp_diff | [MarketByPriceDiff](#marketbypricediff) |  | Market by price diff |
| kline | [Kline](#kline) |  | Candlestick |
| market_status | [MarketStatus](#marketstatus) |  |  |
| funding_calculation | [FundingCalculation](#fundingcalculation) |  | Funding calculation |
| funding_application | [FundingApplication](#fundingapplication) |  | Funding application |
| contract_statistics | [ContractStatistics](#contractstatistics) |  |  |
| contract_price | [ContractPrice](#contractprice) |  |  |
| market_id | [uint64](#uint64) | optional | The market ID that this message is for. Null for `MdMessage.Heartbeat`. |







### MarketByPrice
Market by price snapshot message. This is chunked into `num_chunks` and starts
with `chunk = 0`. A snapshot is sent on first connect. `Level`'s should be
concatened until `chunk = num_chunks - 1`. Currently, the chunks and levels
are streamed from tightest price level outwards with interleaved Bid and Ask
levels, but no ordering is guaranteed.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| levels | [MarketByPrice.Level](#marketbyprice.level) | repeated |  |
| chunk | [uint32](#uint32) |  |  |
| num_chunks | [uint32](#uint32) |  |  |







### MarketByPrice.Level
Each price level is the aggregate total quantity of orders placed at that
price.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| price | [uint64](#uint64) |  |  |
| quantity | [uint64](#uint64) |  |  |
| side | [Side](#side) |  |  |







### MarketByPriceDiff
Market by price diff message. Book updates for the MBP feed are sent as diffs
after the initial snapshot. The number of total side levels are for
reconciliation.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| diffs | [MarketByPriceDiff.Diff](#marketbypricediff.diff) | repeated |  |
| total_bid_levels | [uint32](#uint32) |  | Total number of bid levels after this diff is applied. |
| total_ask_levels | [uint32](#uint32) |  | Total number of ask levels after this diff is applied. |







### MarketByPriceDiff.Diff
A price level diff overwrites the existing price level.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| price | [uint64](#uint64) |  |  |
| quantity | [uint64](#uint64) |  |  |
| side | [Side](#side) |  |  |
| op | [MarketByPriceDiff.DiffOp](#marketbypricediff.diffop) |  |  |







### MarketByOrder
Market by order snapshot message. This is chunked into `num_chunks` and starts
with `chunk = 0`. A snapshot is sent on first connect. `Level`'s should be
concatened until `chunk = num_chunks - 1`. Orders are sent in order of FIFO
queue priority so the first order of a level should be the first order to be
matched when that level is aggressed.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| orders | [MarketByOrder.Order](#marketbyorder.order) | repeated |  |
| chunk | [uint32](#uint32) |  |  |
| num_chunks | [uint32](#uint32) |  |  |







### MarketByOrder.Order
A resting order.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| price | [uint64](#uint64) |  |  |
| quantity | [uint64](#uint64) |  |  |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |
| side | [Side](#side) |  |  |
| priority | [uint64](#uint64) |  | Order priority for execution. Valid within a price level and side. That is, orders must first be sorted by side and price (in descending order for bids and ascending for asks), and then the OrderPriority within the level. A lower value is a higher priority. |







### MarketByOrderDiff
Market by order diff message. Book updates for the MBO feed are sent as diffs
after the initial snapshot. The number of total side levels and orders are
for reconciliation.

Note that for orders that are cancel-replace'd (a modify that lost queue
priority), the new price and quantity will be reported as a `REPLACE` but the
exchange order ID will not change.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| diffs | [MarketByOrderDiff.Diff](#marketbyorderdiff.diff) | repeated |  |
| total_bid_levels | [uint32](#uint32) |  | Total number of bid levels after this diff is applied. |
| total_ask_levels | [uint32](#uint32) |  | Total number of ask levels after this diff is applied. |
| total_bid_orders | [uint32](#uint32) |  | Total number of bid orders after this diff is applied. |
| total_ask_orders | [uint32](#uint32) |  | Total number of ask orders after this diff is applied. |







### MarketByOrderDiff.Diff
An order diff creates, updates, or deletes a resting order based on the
`exchange_order_id`


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| price | [uint64](#uint64) |  |  |
| quantity | [uint64](#uint64) |  |  |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |
| side | [Side](#side) |  |  |
| op | [MarketByOrderDiff.DiffOp](#marketbyorderdiff.diffop) |  |  |
| priority | [uint64](#uint64) |  | See [`MarketByOrder.Order`](#marketbyorder.order) |







### MarketStatus



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transact_time | [uint64](#uint64) |  |  |
| market_state | [MarketState](#marketstate) |  |  |







### FundingCalculation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transact_time | [uint64](#uint64) |  | Server time that this funding calculation was made. |
| predicted_funding_rate | [int64](#int64) |  | Predicted funding rate percentage for the next funding interval. See `FundingApplication.funding_rate` for details on calculation. |
| next_funding_application_time | [uint64](#uint64) |  | The server target time for the next funding application. Expressed in nanoseconds. <br> `countdown = next_funding_application_time - transact_time` |
| premium_index | [int64](#int64) |  | Premium (or discount) percentage relative to the index price. <br> `premium_index = (MAX(impact_bid_price - index_price, 0) - MAX(index_price - impact_ask_price, 0)) / index_price` <br> Expressed with 9 decimals. |
| index_price | [uint64](#uint64) |  | The index price used for the premium index calculation. Expressed with 9 decimals. |
| latest_funding_rate | [int64](#int64) |  | The latest funding application's `funding_rate`. |







### FundingApplication



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transact_time | [uint64](#uint64) |  |  |
| funding_rate | [int64](#int64) |  | Funding rate percentage for this interval, calculated based on the average premium index over the funding interval. <br> `funding_rate = premium_index + clamp(interest_rate - premium_index, -clamp, +clamp)` </br> |
| funding_delta | [FundingDelta](#fundingdelta) |  | The quote amount to be paid (or received) based on the given funding rate, funding interval duration, and current index price. |
| next_funding_application_time | [uint64](#uint64) |  | The server target time for the next funding application. |







### ContractStatistics
Statistics for the contract.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transact_time | [uint64](#uint64) |  |  |
| open_interest | [int64](#int64) |  | The total number of open contracts for this product. Counts both longs and shorts |







### ContractPrice
Latest contract price information.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transact_time | [uint64](#uint64) |  |  |
| index_price | [uint64](#uint64) |  | The spot index price of the contract. Expressed with 9 decimals. |
| mark_price | [uint64](#uint64) |  | The mark price at `transact_time`. <br> `funding_basis = funding_rate * (time until funding / funding interval)` `mark_price = (1 + funding_basis) * index_price` </br> |







### Trades
Trades since the latest `Trades` message. The result of the trades will also
appear in the MBP and MBO feeds independently as updates to the resting
orders and levels, respectively.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| trades | [Trades.Trade](#trades.trade) | repeated |  |







### Trades.Trade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tradeId | [uint64](#uint64) |  | The ID assigned to this trade. All trades that occur from the same event will be assigned the same ID, and are considered to be an atomic batch. |
| price | [uint64](#uint64) |  | The price that this trade occurred at. |
| aggressing_side | [AggressingSide](#aggressingside) |  | The side of the aggressing order. |
| resting_exchange_order_id | [uint64](#uint64) |  | The [Exchange order ID](/trade-api.md#exchange-order-id) of the resting order. |
| fill_quantity | [uint64](#uint64) |  |  |
| transact_time | [uint64](#uint64) |  | The [transact time](/trade-api.md#transact-time) assigned by the matching engine for this trade. All trades that occur from the same event will be assigned the same transact time. |
| aggressing_exchange_order_id | [uint64](#uint64) |  | The [Exchange order ID](/trade-api.md#exchange-order-id) of the aggressing order. |







### Summary
Rolling 24h stats.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| open | [uint64](#uint64) | optional | 24h open price |
| close | [uint64](#uint64) | optional | Latest price |
| low | [uint64](#uint64) | optional | 24h low price |
| high | [uint64](#uint64) | optional | 24h high price |
| base_volume_lo | [uint64](#uint64) |  | Low 64-bits of the base quantity traded |
| base_volume_hi | [uint64](#uint64) |  | High 64-bits of the base quantity traded |
| quote_volume_lo | [uint64](#uint64) |  | Low 64-bits of the quote quantity traded |
| quote_volume_hi | [uint64](#uint64) |  | High 64-bits of the quote quantity traded |







### Kline
Candlestick bar.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| interval | [KlineInterval](#klineinterval) |  |  |
| start_time | [uint64](#uint64) |  | The unix nanosecond timestamp that this kline covers. |
| open | [uint64](#uint64) | optional | Kline open price. |
| close | [uint64](#uint64) | optional | Kline close price. |
| high | [uint64](#uint64) | optional | Kline high price. |
| low | [uint64](#uint64) | optional | Kline low price. |
| volume_lo | [uint64](#uint64) |  | Low 64-bits of the base quantity traded. |
| volume_hi | [uint64](#uint64) |  | High 64-bits of the base quantity traded. |







### Heartbeat
A client and server heartbeat. The heartbeat reply, including the timestamp
value, comes from the market data service.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the Heartbeat |
| timestamp | [uint64](#uint64) |  |  |







### MdMessages
A wrapper containing one or more Market Data messages,
each of which will be an [`MdMessage`](#mdmessage).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| messages | [MdMessage](#mdmessage) | repeated |  |







## AggMessage
Every exchange message from `/tops` will be wrapped as an `AggMessage`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| heartbeat | [Heartbeat](#heartbeat) |  | Server heartbeat reply |
| top_of_books | [TopOfBooks](#topofbooks) |  | Top of books |
| rate_updates | [RateUpdates](#rateupdates) |  | Rates for all assets |







### TopOfBook
Top of book


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| market_id | [uint64](#uint64) |  |  |
| transact_time | [uint64](#uint64) |  | The [transact time](/trade-api.md#transact-time) of the latest book update on this market. |
| bid_price | [uint64](#uint64) | optional | The best bid price of the direct or implied book, whichever is better. |
| bid_quantity | [uint64](#uint64) | optional | The total bid quantity at the best bid price. |
| ask_price | [uint64](#uint64) | optional | The best ask price of the direct or implied book, whichever is better. |
| ask_quantity | [uint64](#uint64) | optional | The total ask quantity at the best ask price. |
| last_price | [uint64](#uint64) | optional | The last trade price. |
| rolling24h_price | [uint64](#uint64) | optional | The 24h open price. |
| market_state | [MarketState](#marketstate) |  | Which trading operations are currently allowed on this market. |







### TopOfBooks
Top of books for all books that were updates since the last top-of-books
message.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tops | [TopOfBook](#topofbook) | repeated |  |







### RateUpdate
Rate update. Used in conjuction with another rate update to get the price of
that divisor. Rate's should not be used alone. For example, given a
RateUpdate for `assetId = BTC, updateSide = BASE` of `r1`, and `assetId =
EUR, updateSide = QUOTE` of `r2`, the BTC-EUR price estimate is `r1 * r2`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| asset_id | [uint64](#uint64) |  |  |
| timestamp | [uint64](#uint64) |  | The nanosecond timestamp of the update. |
| rate | [uint64](#uint64) |  | The asset rate at the given timestamp. |
| side | [RateUpdateSide](#rateupdateside) |  |  |







### RateUpdates
Rates for all assets. Published on connect and updates since the last
rate-updates message.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| updates | [RateUpdate](#rateupdate) | repeated |  |







## ClientMessage
Client heartbeats and configs. This wrapper is used for both
`/book/:market_id` and `/tops`, but `config` messages are ignored on the
latter.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| heartbeat | [Heartbeat](#heartbeat) |  |  |
| config | [Config](#config) |  |  |







### Config
Set the message subscriptions for `/book/:market_id`. At most one of `mbp`
and `mbo` can be set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mbp | [bool](#bool) |  | Enable MBP feeds |
| mbo | [bool](#bool) |  | Enable MBO feeds |
| trades | [bool](#bool) |  | Enable recent trades |
| summary | [bool](#bool) |  | Enable 24h summary |
| klines | [KlineInterval](#klineinterval) | repeated | Enable price klines |
| market_ids | [uint64](#uint64) | repeated | Market's to subscribe to. Limit 3. |








## Numeric Types
### FundingDelta
Funding delta to be applied per open contract unit, for a particular funding
interval. The delta is expressed as a signed (twos-complement) fixed point
number with 18 decimal places.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| word0 | [uint64](#uint64) |  |  |
| word1 | [uint64](#uint64) |  |  |







## Enums


### Side
Side specifies whether the level, order, or diff, is for buying or selling
the base asset.

| Name | Number | Description |
| ---- | ------ | ----------- |
| BID | 0 | Bids buy the base asset with the quote asset. |
| ASK | 1 | Asks (or offers) sell the base asset and get the quote asset. |




### KlineInterval
The candlestick interval.

| Name | Number | Description |
| ---- | ------ | ----------- |
| S1 | 0 | 1 second |
| M1 | 1 | 1 minute |
| M15 | 2 | 15 minutes |
| H1 | 3 | 1 hour |
| H4 | 4 | 4 hours |
| D1 | 5 | 1 day |




### MarketState
The per-market matching engine state. Affects order-entry.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSPECIFIED | 0 | Sentinel |
| NORMAL_OPERATION | 1 | The market is in its normal operating state. All order operations are supported. |
| CANCEL_ONLY | 2 | The market is in cancel-only mode. Existing orders are not automatically canceled, and may be filled when the market transitions back to normal-operation. |




### AggressingSide
The side of the aggressing order. This also indicates if the aggressing order
was an implied order (i.e aggressed into a different market and executed into
this one through implieds)

| Name | Number | Description |
| ---- | ------ | ----------- |
| AGGRESSING_BID | 0 |  |
| AGGRESSING_ASK | 1 |  |
| AGGRESSING_IMPLIED_BID | 2 |  |
| AGGRESSING_IMPLIED_ASK | 3 |  |




### RateUpdateSide
The side of the rate update. Given a `BASE` rate of `r`, the `QUOTE` rate is
`1 / r`, and vice versa.

| Name | Number | Description |
| ---- | ------ | ----------- |
| BASE | 0 | The asset serves as the base asset for the given rate. |
| QUOTE | 1 | The asset serves as the quote asset for the given rate. |




### MarketByPriceDiff.DiffOp
The operation to apply for this price level. Currently, new price levels
are created with `REPLACE`.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ADD | 0 | This operation is NOT used for MBP. The operation of adding a new price level is specified as `REPLACE`. |
| REMOVE | 1 | This operation is used when a price level is removed from the book. |
| REPLACE | 2 | This operation is used when a new price level is added or an existing price level is modified. |




### MarketByOrderDiff.DiffOp
The operation to apply for this price level. For example, an resting order
that gets filled will be `REPLACE`'d with the new resting quantity. An
order is `REMOVE`'d when it is fully filled or canceled.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ADD | 0 |  |
| REMOVE | 1 |  |
| REPLACE | 2 |  |








## Scalar Value Types

| .proto Type | Notes | Rust | C++ | Python | Go |
| ----------- | ----- | ---- | --- | ------ | -- |
| double |  | f64 | double | float | float64 |
| float |  | f32 | float | float | float32 |
| int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | i32 | int32 | int | int32 |
| int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | i64 | int64 | int/long | int64 |
| uint32 | Uses variable-length encoding. | u32 | uint32 | int/long | uint32 |
| uint64 | Uses variable-length encoding. | u64 | uint64 | int/long | uint64 |
| sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | i32 | int32 | int | int32 |
| sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | i64 | int64 | int/long | int64 |
| fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | u64 | uint32 | int | uint32 |
| fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | u64 | uint64 | int/long | uint64 |
| sfixed32 | Always four bytes. | i32 | int32 | int | int32 |
| sfixed64 | Always eight bytes. | i64 | int64 | int/long | int64 |
| bool |  | bool | bool | boolean | bool |
| string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | String | string | str/unicode | string |
| bytes | May contain any arbitrary sequence of bytes. | Vec<u8> | string | str | []byte |

The base URL for endpoints described in this page of live trading API is `https://api.cube.exchange/os/v0`.

Definitions for requests and responses can be found in the [Trade OpenAPI Document](/generated/core/os_api_30.json).

Further specifics for field enums, reject codes, etc. can be found in the [Trade API Websocket Documentation](./websocket-api.md).

## Endpoints, authentication required

Endpoints in this section require [Authentication
headers](/exchange-info.md#authentication-headers). Note that only API keys
with access-level `WRITE` are able to access _any_ of these endpoints.

{% swagger src="/generated/core/os_api_30.json" path="/orders" method="get" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/os_api_30.json" path="/orders" method="delete" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/os_api_30.json" path="/order" method="post" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/os_api_30.json" path="/order" method="delete" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/os_api_30.json" path="/order" method="patch" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}

{% swagger src="/generated/core/os_api_30.json" path="/positions" method="get" %}
[os_api_30.json](/generated/core/os_api_30.json)
{% endswagger %}
# WebSocket: Trade API

This schema defines the Protobuf messages used for communication with the
Cube Order Service (OS, or "Osmium").

- The connection URL for this Websocket API is `wss://api.cube.exchange/os`.

- See also:
  - The [Protobuf definition file for the Websocket connection](https://github.com/cubexch/ws-api/blob/main/schema/trade.proto)
  - [General documentation pertaining to the Trade API](https://cubexch.gitbook.io/cube-api/trade-api.md)

### Connection

The order service exposes a websocket endpoint for clients to connect to.
Once connected, clients should submit a [`Credentials`](#credentials)
message, listen for [`Bootstrap`](#bootstrap) messages for resting orders
and positions, and then can begin submitting
[`OrderRequest`](#orderrequest) and processing
[`OrderResponse`](#orderresponse).

### Heartbeats

Application-level heartbeats are expected every 30 seconds. If more than one
interval is missed, the order service will disconnect the websocket.



## Credentials
Sent by client on websocket initialization. Once the websocket has been
connected, the client is expected to send this credentials message
immediately. The API key (UUID) and secret access key (hex-encoded 32-byte
array) should be generated on the settings page with the write access. The
signature should be calculated as the concatenation of the byte string
`cube.xyz` and the current unix epoch in seconds interpreted at a
little-endian 64-bit number.

### Implementation notes
- The signature is base-64 encoded with the 'standard' alphabet and
  padding.

  ```
  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
  ```
- The timestamp should be encoded as 8-byte little-endian (array of bytes)
- The secret key should be decoded from a hex string into a 32-byte array of
  bytes

If the credentials provided are incorrect, the server will drop the connection with a close code of 4401.

### Examples

In the following examples, replace "cafecafecafe..." with your secret key.
When calculated for:
- secret key: "cafecafecafecafecafecafecafecafecafecafecafecafecafecafecafecafe"
- timestamp: 1706546268
...the resulting signature should be:
- "tmtSP4NIzTLXyVUHIOfinotGnPWyfM8JefxivBdSjc8="

#### Rust

```rust compile_fail
// With crates hmac, base64, hex:
use base64::Engine;
use hmac::{Hmac, Mac, NewMac};
use std::time::SystemTime;

let secret_key = hex::decode("cafecafecafecafecafecafecafecafecafecafecafecafecafecafecafecafe").expect("secret key valid hex").as_slice();

let timestamp: u64 = SystemTime::now().duration_since(SystemTime::UNIX_EPOCH).unwrap().as_secs();

let mut mac = Hmac::<sha2::Sha256>::new_from_slice(
    secret_key
).expect("new HMAC error");
mac.update(b"cube.xyz");
mac.update(&timestamp.to_le_bytes());

let signature_bytes = <[u8; 32]>::from(mac.finalize().into_bytes());
let signature = base64::general_purpose::STANDARD.encode(signature_bytes);

println!("{}", signature);
```

#### Typescript
```typescript
import { createHmac } from 'crypto';

const secretKey = "cafecafecafecafecafecafecafecafecafecafecafecafecafecafecafecafe";
const timestampSecs = Math.floor(Date.now() / 1000);
const timestampBytes = Buffer.alloc(8);
timestampBytes.writeBigInt64LE(BigInt(timestampSecs));

const signature = createHmac('sha256', Buffer.from(secretKey, 'hex'))
  .update(`cube.xyz`)
  .update(timestampBytes)
  .digest('base64');

console.log(signature)
```

#### Python
```python
import base64
import hmac

# Calculates "signature" field for "Credentials" message
def calculate_signature(secret_key: bytes, timestamp_seconds: int) -> str:
    h = hmac.new(secret_key, digestmod=hashlib.sha256)
    h.update("cube.xyz".encode('utf-8'))
    h.update(timestamp_seconds.to_bytes(8, byteorder="little", signed=False))
    signature_bytes = h.digest()
    return base64.standard_b64encode(signature_bytes).decode('utf-8')

secret_key = bytes.fromhex("cafecafecafecafecafecafecafecafecafecafecafecafecafecafecafecafe")
timestamp = int(time.time())
signature = calculate_signature(secret_key, timestamp)

print(signature)
````


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| access_key_id | [string](#string) |  | Public API key |
| signature | [string](#string) |  | HMAC signature, base-64 encoded |
| timestamp | [uint64](#uint64) |  | Timestamp in seconds |







## OrderRequest
Every client message, aside from Credentials, must be wrapped as an
OrderRequest.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new | [NewOrder](#neworder) |  |  |
| cancel | [CancelOrder](#cancelorder) |  |  |
| modify | [ModifyOrder](#modifyorder) |  |  |
| heartbeat | [Heartbeat](#heartbeat) |  |  |
| mc | [MassCancel](#masscancel) |  |  |







### NewOrder
Place a new order.

Execution details:
- For market orders, exactly one of `quantity` or `quote_quantity` must be
  specified.
- For MARKET_WITH_PROTECTION, if `price` is specified, it will override the
  default protection price.
- Matching will stop upon reaching the protection price, or `quantity` (or
  `quote_quantity`) filled.
- When specifying `quote_quantity`, the order is considered 'fully filled'
  when there is insufficient remaining quote quantity to fill 1 lot at the
  next trade price. In that case, there will _not_ be a `CancelOrderAck`
  published.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| client_order_id | [uint64](#uint64) |  | A unique order ID assigned by the client for this order. The ID must be unique among open orders by this subaccount. |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the NewOrderAck or NewOrderReject |
| market_id | [uint64](#uint64) |  |  |
| price | [uint64](#uint64) | optional |  |
| quantity | [uint64](#uint64) | optional | Required for LIMIT orders. |
| side | [Side](#side) |  |  |
| time_in_force | [TimeInForce](#timeinforce) |  |  |
| order_type | [OrderType](#ordertype) |  |  |
| subaccount_id | [uint64](#uint64) |  | The subaccount to place this order on. This subaccount must be writable by the API key specified in the Credentials message. |
| self_trade_prevention | [SelfTradePrevention](#selftradeprevention) | optional |  |
| post_only | [PostOnly](#postonly) |  |  |
| cancel_on_disconnect | [bool](#bool) |  | If true, this order will be automatically cancelled after the closure of the network connection between Cube's servers and the client that placed the order.

If the client initiates the disconnect or network instability drops the connection, the order will be cancelled when Cube's servers recognize the disconnection.

In the event of a server-side disconnect that causes a halt in trading, such as scheduled downtime, the order will be cancelled before trading resumes. |
| quote_quantity | [uint64](#uint64) | optional | The quantity of the quote asset that the user wants to spend (for a BID) or receive (for an ASK). For limit orders, this is immediately converted to a base quantity using the provided price. For market orders, this is the maximum quantity that will be executed.

Note that lot size rules will be respected, and the actual quantity executed will be expressed in base quantity units. |







### CancelOrder
Cancel a resting order.
Note that this can be done before the order is acknowledged (an aggressive
cancel) since the identifying field is the `client_order_id`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| market_id | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The order ID specified by the client on the NewOrder request. |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the CancelOrderAck or CancelOrderReject |
| subaccount_id | [uint64](#uint64) |  | The subaccount that the NewOrder was placed on. |







### ModifyOrder
Modify a resting order.
- If the `newPrice` and the current resting order's price is the same, and
`newQuantity` is not greater, then the modify is considered a modify down,
and the FIFO queue priority is maintained. Otherwise, the modify-order
request is treated as an atomic cancel-replace and the replacement order is
placed at the end of the FIFO queue for the new price level.
- If post-only is specified and the replacement order would trade, then the
request is rejected and the current resting order remains resting.

Currently, in-flight-mitigation (IFM) is always enabled. That is, the
cumulative fill qty is subtracted from `newQuantity` to calculate the new
resting quantity. For example:

```text
         | Resting | Filled
---------+---------+--------
New 5    | 5       | 0
Fill 2   | 3       | 2
Modify 4 | 2       | 2
```

The post-modify quantity will be `newQuantity - filled = 4 - 2 = 2`.

Regardless of IFM, the invariant for order quantity is that `quantity =
remaining_quantity + cumulative_quantity`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| market_id | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The order ID specified by the client on the NewOrder request. |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the ModifyOrderAck or ModifyOrderReject |
| new_price | [uint64](#uint64) |  |  |
| new_quantity | [uint64](#uint64) |  |  |
| subaccount_id | [uint64](#uint64) |  | The subaccount that the NewOrder was placed on. |
| self_trade_prevention | [SelfTradePrevention](#selftradeprevention) | optional |  |
| post_only | [PostOnly](#postonly) |  |  |







### MassCancel
Cancel all resting orders, optionally limiting to a particular market and /
or order book side.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subaccount_id | [uint64](#uint64) |  | The subaccount to cancel orders for. |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the MassCancelAck and individual CancelOrderAck's. |
| market_id | [uint64](#uint64) | optional | If specified, only orders on the corresponding market will be canceled. |
| side | [Side](#side) | optional | If specified, only orders with this side will be canceled. |







### Heartbeat
A client and server heartbeat. The heartbeat reply, including the timestamp
value, comes from the order service and not the matching engine. Matching
engine timestamps can be extracted from `transact_time` (below).

Latency can be estimated from this, but only the relative difference between
successive server messages should be used. In particular, the client and
server clock should not be expected to be synchronized.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | [uint64](#uint64) |  | A request ID that is echoed back on the Heartbeat |
| timestamp | [uint64](#uint64) |  |  |







## OrderResponse
Every exchange message after the initial bootstrap will be wrapped as an
OrderResponse.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new_ack | [NewOrderAck](#neworderack) |  |  |
| cancel_ack | [CancelOrderAck](#cancelorderack) |  |  |
| modify_ack | [ModifyOrderAck](#modifyorderack) |  |  |
| new_reject | [NewOrderReject](#neworderreject) |  |  |
| cancel_reject | [CancelOrderReject](#cancelorderreject) |  |  |
| modify_reject | [ModifyOrderReject](#modifyorderreject) |  |  |
| fill | [Fill](#fill) |  |  |
| heartbeat | [Heartbeat](#heartbeat) |  |  |
| position | [AssetPosition](#assetposition) |  |  |
| mass_cancel_ack | [MassCancelAck](#masscancelack) |  |  |
| trading_status | [TradingStatus](#tradingstatus) |  |  |
| implied_match_fee | [ImpliedMatchFee](#impliedmatchfee) |  |  |
| contract_position | [ContractPosition](#contractposition) |  |  |







### NewOrderAck
New-order-ack confirms a new-order request. The ack will be ordered before
any fills for this order.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the new-order request. |
| request_id | [uint64](#uint64) |  | The request ID specified in the new-order request. |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |
| market_id | [uint64](#uint64) |  |  |
| price | [uint64](#uint64) |  | The price that matching completed at. For limit orders, this will be the limit price. For market orders, this will be the protection price. |
| quantity | [uint64](#uint64) |  | If `quote_quantity` was not specified, the quantity submitted in the new-order request. Otherwise, the quantity of the base asset that was executed. |
| side | [Side](#side) |  |  |
| time_in_force | [TimeInForce](#timeinforce) |  |  |
| order_type | [OrderType](#ordertype) |  |  |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| cancel_on_disconnect | [bool](#bool) |  |  |
| quote_quantity | [uint64](#uint64) | optional |  |







### CancelOrderAck
Cancel-order-ack confirms a cancel request, or that an order has been
canceled as the result of a different user-initiated reason.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  |  |
| request_id | [uint64](#uint64) |  | If the Reason is `DISCONNECT`, `IOC`, `STP_RESTING`, or `STP_AGGRESSING`, this request ID will be `u64::MAX`. Otherwise, it will be the request ID of the initiated cancel action. For a mass cancel, each cancel order ack will have the MassCancel's request_id. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| reason | [CancelOrderAck.Reason](#cancelorderack.reason) |  |  |
| market_id | [uint64](#uint64) |  |  |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |







### ModifyOrderAck
Modify-order-ack confirms a modify-order request. If the modify resulted in
an aggressing cancel-replace, the ack will be ordered before any fills for
this order.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  |  |
| request_id | [uint64](#uint64) |  | The request ID specified in the modify request. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| remaining_quantity | [uint64](#uint64) |  | The quantity remaining on the book after applying the modify request. |
| subaccount_id | [uint64](#uint64) |  |  |
| market_id | [uint64](#uint64) |  |  |
| price | [uint64](#uint64) |  |  |
| quantity | [uint64](#uint64) |  | The quantity submitted in the modify request. |
| cumulative_quantity | [uint64](#uint64) |  | The cumulative filled quantity for this order. |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |







### MassCancelAck
Mass-cancel-ack confirms a mass-cancel request. If `reason` is set, the mass
cancel was not applied and there are no affected orders. Individual
CancelOrderAck's will be sent for each order that was affected.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| subaccount_id | [uint64](#uint64) |  |  |
| request_id | [uint64](#uint64) |  | The request ID specified in the mass-cancel request. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| reason | [MassCancelAck.Reason](#masscancelack.reason) | optional |  |
| total_affected_orders | [uint32](#uint32) |  | The total number of orders that were canceled. |







### NewOrderReject
New-order-reject indicates that a new-order request was not applied.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the new-order request. |
| request_id | [uint64](#uint64) |  | The request ID specified in the new-order request. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| reason | [NewOrderReject.Reason](#neworderreject.reason) |  |  |
| market_id | [uint64](#uint64) |  |  |
| price | [uint64](#uint64) | optional |  |
| quantity | [uint64](#uint64) | optional |  |
| side | [Side](#side) |  |  |
| time_in_force | [TimeInForce](#timeinforce) |  |  |
| order_type | [OrderType](#ordertype) |  |  |
| quote_quantity | [uint64](#uint64) | optional |  |







### CancelOrderReject
Cancel-order-reject indicates that a cancel-order request was not applied.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the cancel-order request. |
| request_id | [uint64](#uint64) |  | The request ID specified in the cancel-order request. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| reason | [CancelOrderReject.Reason](#cancelorderreject.reason) |  |  |
| market_id | [uint64](#uint64) |  |  |







### ModifyOrderReject
Modify-order-reject indicates that a modify-order request was not applied.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the modify-order request. |
| request_id | [uint64](#uint64) |  | The request ID specified in the modify-order request. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| reason | [ModifyOrderReject.Reason](#modifyorderreject.reason) |  |  |
| market_id | [uint64](#uint64) |  |  |







### Fill
A fill for an order.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| market_id | [uint64](#uint64) |  |  |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the new-order request. |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |
| fill_price | [uint64](#uint64) |  | The price at which this trade occured. In the case of an implied fill, this price may be fractional, and will be truncated in that case. To determine the exact amount of the assets exchanged in the fill, use the fill_quantity and fill_quote_quantity fields. |
| fill_quantity | [uint64](#uint64) |  | The quantity of the base asset that was traded in this fill, expressed in lots of the base asset. |
| leaves_quantity | [uint64](#uint64) |  | The remaining base quantity for this order after the fill is applied. |
| fill_quote_quantity | [uint64](#uint64) |  | The quantity of the quote asset that was traded in this fill, expressed in lots of the quote asset. This will generally be the same as the base fill_quantity * fill_price, but may be different in the case of an implied fill. |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| subaccount_id | [uint64](#uint64) |  |  |
| cumulative_quantity | [uint64](#uint64) |  | The cumulative filled base quantity for this order after the fill is applied. |
| side | [Side](#side) |  |  |
| aggressor_indicator | [bool](#bool) |  |  |
| fee_ratio | [FixedPointDecimal](#fixedpointdecimal) |  | Indicates the fee charged on this trade. See [Trading Fees](/cube-fees.md#trading-fees) for details. |
| trade_id | [uint64](#uint64) |  | The unique trade ID associated with a match event. Each order participanting in the match event will receive this trade ID |







### ImpliedMatchFee
Indicates the implied match fee for a trade.
This message will be delivered once for each aggressing NewOrder (taker order)
that results in one or more implied fills.
If an implied match occurs but the implied match fee is zero,
this message will still be delivered and the fee_amount will be zero.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| msg_seq_num | [uint64](#uint64) |  |  |
| transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| market_id | [uint64](#uint64) |  | The ID of the market in which the order was placed |
| subaccount_id | [uint64](#uint64) |  | The ID of the subaccount which placed the aggressing order that resulted in the implied match. |
| client_order_id | [uint64](#uint64) |  | The ID assigned by the client that placed the aggressing order that resulted in the implied match. |
| exchange_order_id | [uint64](#uint64) |  | The ID assigned by the exchange to the agressing order that resulted in the implied match. |
| fee_asset_id | [uint64](#uint64) |  | The ID of the asset demoninating the fee_amount. |
| fee_amount | [RawUnits](#rawunits) |  | The magnitude of the implied match fee in indivisible RawUnits. For details on how this is calculated, reference the documentation related to Implied Matching. Note that, unlike trading fees, this value is already accounted for in the quantities reported by the fill_quantity and fill_quote_quantity fields. It does not need to be subtracted when reconciling the associated order's fills against on-chain settlement. |
| fee_direction | [AdjustmentDirection](#adjustmentdirection) |  | Which way the fee_amount funds are moving, from the perspective of the client. |







### AssetPosition
The user's underlying asset position. These are sent asynchronously as
positions are updated and broadcast through internal position channels. They
can also be tracked by applying other OrderResponse messages individually.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subaccount_id | [uint64](#uint64) |  |  |
| asset_id | [uint64](#uint64) |  |  |
| total | [RawUnits](#rawunits) |  |  |
| available | [RawUnits](#rawunits) |  | The available amount after open orders are subtracted. |







### ContractPosition
The user's open contract position and open orders. Also see `AssetPosition`

`quote` is the settled offsetting quote balance for the open contract
units (and is thus almost almost always the opposite sign of
`net_contract_units`).

Funding payments (/ credits) are applied to this balance directly and are
not immediately settled. Also note that index price changes are not
immediately reflected in the `quote` balance. These are all settled at time
of PnL settlement, and subsequent `ContractPosition` and `AssetPosition`
messages will reflect those changes.

The unsettled PnL (different from the unrealized pnl) of the position,
which includes funding payments et al, is calculated as:

```rust compile_file
// the contract multiplier as defined in the contract specification
let contract_decimals = ...;

// from the index price market data feed, with 9 decimals of precision
let index_price = ...;

// base notional with 18 digits of precision
let base_notional
  = net_contract_units * 10.pow(9) / 10.pow(contract_decimals)
  * index_price
  ;

// quote is published with 18 decimals of precision
let quote = ...;

// pnl with 18 digits of precision.
let unsettled_pnl = base_notional + quote;
```


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subaccount_id | [uint64](#uint64) |  |  |
| contract_id | [uint64](#uint64) |  |  |
| net_contract_units | [int64](#int64) |  | The net number of open contracts held by this subaccount. |
| quote | [HealthValue](#healthvalue) |  |  |
| bids | [RawUnits](#rawunits) |  |  |
| asks | [RawUnits](#rawunits) |  |  |
| cost_basis | [HealthValue](#healthvalue) |  | The cost basis paid for the current position. Lots are averaged together. <br> The cost basis will be the same sign as `net_contract_units`. <br> Display only. Reset when the position is closed or the position direction changes. |
| realized_pnl | [HealthValue](#healthvalue) |  | The realized PnL for the current position. Calculated as the sum of differences between contract value at time of close and average cost basis. <br> Display only. Reset when the position is closed or the position direction changes. |
| funding | [HealthValue](#healthvalue) |  | Total funding paid (positive) or received (negative) by this position. <br> Display only. Reset when the position is closed or the position direction changes. |
| leverage | [uint32](#uint32) |  | The leverage override applied to the contract. (0 if there is no override) <br> Leverage ratio affects the maximum notional position size as well as the initial margin requirements for the position. Note that this does not directly affect the maintenance margin requirements. |







## Bootstrap
A bootstrap message sent after Credentials authentication.
Client resting and pending orders used to bootstrap state.
Sent as the first message(s) after initialization.
A message containing the `Done` variant indicates that the Bootstrap is complete.
Multiple messages may be received for `RestingOrders` and `AssetPositions`
and these should be concatenated.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| done | [Done](#done) |  |  |
| resting | [RestingOrders](#restingorders) |  |  |
| position | [AssetPositions](#assetpositions) |  |  |
| trading_status | [TradingStatus](#tradingstatus) |  |  |
| contract_position | [ContractPositions](#contractpositions) |  |  |







### RestingOrders
A chunk of resting orders. Sent on bootstrap.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| orders | [RestingOrder](#restingorder) | repeated |  |







### AssetPositions
A chunk of asset positions. Sent on bootstrap.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| positions | [AssetPosition](#assetposition) | repeated |  |







### ContractPositions
A chunk of contract positions. Sent on bootstrap.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| positions | [ContractPosition](#contractposition) | repeated |  |







### Done
An indication that bootstrap is complete.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| latest_transact_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) |
| read_only | [bool](#bool) |  | DEPRECATED: will be removed in a future version; read the "connection_status" field in the "Bootstrap.TradingStatus" message that arrives before the "Done" message |







### TradingStatus
Indicates the scope of the ability to trade via this connection.
This message will be sent each time that scope changes.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| connection_status | [ConnectionStatus](#connectionstatus) |  | Indicates which operations are available through this connection as of this message. |







### RestingOrder
A resting order. Sent on bootstrap in `RestingOrders`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| client_order_id | [uint64](#uint64) |  | The client order ID specified in the new-order request. |
| exchange_order_id | [uint64](#uint64) |  | [Exchange order ID](/trade-api.md#exchange-order-id) |
| market_id | [uint64](#uint64) |  |  |
| price | [uint64](#uint64) |  |  |
| order_quantity | [uint64](#uint64) |  | The quantity submitted in the latest quantity-modifying request. If the order has not been modified, then it is the quantity on the new-order-ack. If it has been modified, then it is the quantity of the latest modify-order-ack. |
| side | [Side](#side) |  |  |
| time_in_force | [TimeInForce](#timeinforce) |  |  |
| order_type | [OrderType](#ordertype) |  |  |
| remaining_quantity | [uint64](#uint64) |  | The current remaining quantity on the book. |
| rest_time | [uint64](#uint64) |  | [Transact time](/trade-api.md#transact-time) of the NewOrderAck |
| subaccount_id | [uint64](#uint64) |  |  |
| cumulative_quantity | [uint64](#uint64) |  | The cumulative filled quantity for this order. |
| cancel_on_disconnect | [bool](#bool) |  |  |








## Numeric Types
### FixedPointDecimal
A fixed-point decimal number.
Matches the representation preferred by the FIX protocol,
except that the exponent is int32 since Protobuf does not have an int8 type.
The value is computed as `mantissa * 10^exponent`;
for example, `mantissa = 1234` and `exponent = -2` is `12.34`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mantissa | [int64](#int64) |  |  |
| exponent | [int32](#int32) |  |  |







### RawUnits
Raw-units is a 256-bit number for the amount of an asset. The precision is
based on the underlying asset. For example, ETH is specified as if in
fixed-point 10^18, while BTC is specified as if in fixed-point 10^8.

The number is interpreted in 'little-endian' as `[word0, word1, word2,
word3]`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| word0 | [uint64](#uint64) |  |  |
| word1 | [uint64](#uint64) |  |  |
| word2 | [uint64](#uint64) |  |  |
| word3 | [uint64](#uint64) |  |  |







### HealthValue
Signed (twos-complement), fixed point 18-decimal-digit value.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| word0 | [uint64](#uint64) |  |  |
| word1 | [uint64](#uint64) |  |  |
| word2 | [uint64](#uint64) |  |  |
| word3 | [uint64](#uint64) |  |  |







## Enums


### Side
Side specifies whether the order is buying or selling the base asset. A trade
is matched when a buyer (BID) and a seller (ASK) agree on a price (cross).
The bid-ask spread is the gap between the highest bid price and lowest ask
price on the orderbook.

| Name | Number | Description |
| ---- | ------ | ----------- |
| BID | 0 | A bid order buys the base asset with the quote asset. |
| ASK | 1 | An ask (or offer) order sells the base asset and gets the quote asset. |




### AdjustmentDirection
AdjustmentDirection specifies the directionality for a movement of funds between the client and the exchange.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSPECIFIED | 0 | This value should never appear, and is used to detect if this field has been serialized correctly. |
| FEE | 1 | Funds are moving from the client to the exchange. |
| REBATE | 2 | Funds are moving from the exchange to the client. |




### TimeInForce
Time-in-force (TIF) specifies how long the order remains in effect.

| Name | Number | Description |
| ---- | ------ | ----------- |
| IMMEDIATE_OR_CANCEL | 0 | Immediate-or-cancel (IOC), also known as fill-and-kill (FAK), orders are immediately executed against resting orders. If the order cannot be fully filled, the remaining balance will be canceled, and an additional CancelOrderAck with the IOC reason will be sent. |
| GOOD_FOR_SESSION | 1 | Good-for-session (GFS) orders are active until they are completely executed, canceled, or when the session expires. |
| FILL_OR_KILL | 2 | Fill-or-kill (FOK), also known as all-or-none (AON), orders must be filled immediately against resting orders or the entire order is canceled. |




### OrderType
Order-type specifies how the order will be placed into the order book.

Limit orders refer to orders of type:
- LIMIT

Market orders refer to orders of type:
- MARKET_LIMIT
- MARKET_WITH_PROTECTION

Pre-flight quantity checks:
- Note that for LIMIT orders, there is a pre-flight check that there is
  sufficient available balance to place this order at the price and quantity
  specified. Otherwise, the order will be rejected with the
  EXCEEDED_SPOT_POSITION reason.
- For Market orders, there is no quantity-based pre-flight check and a
  submitted order will be partially filled up until the subaccount's position
  limit. The remaining quantity will be canceled with the POSITION_LIMIT
  reason.

For the following section, let

```
P_r = reference price
L = protection levels
P_ap = default protection ask price = P_r + L
P_bp = default protection bid price = P_r - L
```

Market order protections:
- Before execution, the following pre-flight slippage check is always
  performed:

    ```
    P_a = best book ask price
    P_b = best book bid price
    if side == BID:
      ensure P_a <= P_ap
    if side == ASK:
      ensure P_b >= P_bp
    ```

  Note that this calculation is irrespective of the order parameters.
- During execution, the match stops depending on the exit condition specified
  by the order type.

| Name | Number | Description |
| ---- | ------ | ----------- |
| LIMIT | 0 | A limit order is accompanied with a price (inclusive) that specifies the upper limit to buy and the lower limit to sell. If the price is not immediately available and the TIF allows resting orders, the limit order will rest until filled or canceled. |
| MARKET_LIMIT | 1 | A market limit order crosses the bid-ask spread and, if not fully filled, becomes a limit order at the best available market price. - If there is no opposing market, the order is rejected with the NO_OPPOSING_RESTING_ORDER reason. - The price must be null. |
| MARKET_WITH_PROTECTION | 2 | A market with protection order crosses the bid-ask spread and continues to cross until the order is fully filled or the protection level is reached. - The protection price is defined as: - If the price is provided, this price is used as the protection price. - If the price is null, the best market price widened by a market-specific protection point count. - If the protection price would not cross the resting market, the order is rejected with the NO_OPPOSING_RESTING_ORDER reason instead of resting at that level. |




### SelfTradePrevention
Self-trade-prevention (STP) allows market participants to prevent the matching
of orders for accounts with common ownership. Currently, STP only applies for
orders with the same subaccount_id. STP will only be applied when a match is
about to occur between the two orders. That is, if the aggressing order is
fully filled before reaching the resting order in FIFO order, no STP cancels
will happen.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CANCEL_RESTING | 0 | Cancel-resting specifies that if a self-trade is about to occur, the resting order should be canceled instead and further order book processing should occur as normal. |
| CANCEL_AGGRESSING | 1 | Cancel-aggressing specifies that if a self-trade is about to occur, the aggressing order should be canceled instead and no further action should be taken. |
| ALLOW_SELF_TRADE | 2 | Allow-self-trade disables STP functionality. |




### PostOnly
Post-only specifies whether a new order is allowed to immediately execute.
Post-only cannot be enabled with market orders or with a TIF that does not
allow resting orders.

| Name | Number | Description |
| ---- | ------ | ----------- |
| DISABLED | 0 |  |
| ENABLED | 1 |  |




### ConnectionStatus
Indicates which operations are allowed on this connection.
The ConnectionStatus may change during a single connection's lifetime.

| Name | Number | Description |
| ---- | ------ | ----------- |
| READ_ONLY | 0 | This connection may query balances and see resting orders but may not create, modify, or cancel orders e.g. |
| READ_WRITE | 1 | There are no restrictions imposed by this connection (though restrictions may apply from elsewhere in the system). |




### CancelOrderAck.Reason


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNCLASSIFIED | 0 |  |
| DISCONNECT | 1 |  |
| REQUESTED | 2 | This order was specified in a cancel request. |
| IOC | 3 | This was an IOC new-order that does not get fully filled. |
| STP_RESTING | 4 | A resting order was STP canceled. |
| STP_AGGRESSING | 5 | An aggressing order was STP canceled. |
| MASS_CANCEL | 6 | This order was covered by a mass-cancel request. |
| POSITION_LIMIT | 7 | This order was canceled because asset position limits would be otherwise breached. |
| LIQUIDATION | 8 | This order was canceled because the subaccount health was insufficient and a liquidation event was triggered. |




### MassCancelAck.Reason


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNCLASSIFIED | 0 |  |
| INVALID_MARKET_ID | 1 |  |
| INVALID_SIDE | 2 |  |




### NewOrderReject.Reason
Reasons that are prefixed with `INVALID_` normally indicate that the
corresponding field did not take a valid value.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNCLASSIFIED | 0 |  |
| INVALID_QUANTITY | 1 | Quantity was zero. |
| INVALID_MARKET_ID | 2 | The specified market ID does not exist. |
| DUPLICATE_ORDER_ID | 3 | The specified client order ID was not unique among open orders for this subaccount. |
| INVALID_SIDE | 4 |  |
| INVALID_TIME_IN_FORCE | 5 |  |
| INVALID_ORDER_TYPE | 6 |  |
| INVALID_POST_ONLY | 7 |  |
| INVALID_SELF_TRADE_PREVENTION | 8 |  |
| UNKNOWN_TRADER | 9 | Internal error: the matching engine could not find this subaccounts positions. |
| PRICE_WITH_MARKET_LIMIT_ORDER | 10 |  |
| POST_ONLY_WITH_MARKET_ORDER | 11 |  |
| POST_ONLY_WITH_INVALID_TIF | 12 |  |
| EXCEEDED_SPOT_POSITION | 13 | The sum of open orders and this new-order would exceed the subaccounts spot limits. |
| NO_OPPOSING_RESTING_ORDER | 14 | There are no opposing resting orders to trade against. |
| POST_ONLY_WOULD_TRADE | 15 | The post-only order would have crossed and traded. |
| DID_NOT_FULLY_FILL | 16 | A FOK was not fully fillable against resting orders at the requested price and quantity. |
| ONLY_ORDER_CANCEL_ACCEPTED | 17 | The given market accepts no new orders at this time |
| PROTECTION_PRICE_WOULD_NOT_TRADE | 18 | A more specific error code for market-with-protection orders that could trade but have a user-specified protection price that is too tight. |
| NO_REFERENCE_PRICE | 19 | Market orders cannot be place because there is currently no internal reference price |
| SLIPPAGE_TOO_HIGH | 20 | A market order would trade beyond the internal reference price offset by protection levels in the direction of aggress. |
| OUTSIDE_PRICE_BAND | 21 | Limit orders cannot have bid price too low or ask price too high that is multiple times away from the internal reference price. |
| LIMIT_ORDER_WITHOUT_PRICE | 22 |  |
| CONFLICTING_QUANTITY_TYPE | 23 | Both `quantity` and `quote_quantity` were specified. |
| NO_QUANTITY_TYPE | 24 | Neither `quantity` nor `quote_quantity` was specified. |
| ORDER_QUANTITY_TOO_LOW | 25 | The quantity of this order, if traded fully, would represent less than the minimum amount allowed for this market. See `minOrderQuoteAmt` in the market definitions. |
| ORDER_QUANTITY_TOO_HIGH | 26 | The quantity of this order, if traded fully, would represent greater than the maximum amount allowed for this market. See `maxOrderQuoteAmt` in the market definitions. |
| MARGIN_TRADING_UNAVAILABLE | 27 | This subaccount is not enabled for margin trading. |
| EXCEEDS_FREE_BALANCE | 28 | The spot balance required to place this order exceeds the free balance usable given current open positions and margin requirements. |
| INSUFFICIENT_INITIAL_MARGIN | 29 | The subaccount does not have sufficient additional initial margin to place this order. |
| INSUFFICIENT_MAINTENANCE_MARGIN | 30 | The subaccount does not have sufficient additional maintenance margin to place this order. |
| EXCEEDS_INITIAL_NOTIONAL_LIMIT | 31 | The value of the order, if executed, would cause the subaccount's total position to exceed the initial notional limit for the configured leverage. |




### CancelOrderReject.Reason


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNCLASSIFIED | 0 |  |
| INVALID_MARKET_ID | 1 | The specified market ID does not exist. |
| ORDER_NOT_FOUND | 2 | The specified client order ID does not exist for the corresponding market ID and subaccount ID. |




### ModifyOrderReject.Reason
Reasons that are prefixed with `INVALID_` normally indicate that the
corresponding field did not take a valid value.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNCLASSIFIED | 0 |  |
| INVALID_QUANTITY | 1 | Quantity was zero. |
| INVALID_MARKET_ID | 2 | The specified market ID does not exist. |
| ORDER_NOT_FOUND | 3 | The specified client order ID does not exist for the corresponding market ID and subaccount ID. |
| INVALID_IFM | 4 |  |
| INVALID_POST_ONLY | 5 |  |
| INVALID_SELF_TRADE_PREVENTION | 6 |  |
| UNKNOWN_TRADER | 7 | Internal error: the matching engine could not find this subaccounts positions. |
| EXCEEDED_SPOT_POSITION | 8 | If the modify-order would cause a cancel-replace, the sum of open orders and this replacement order would exceed the subaccounts spot limits. |
| POST_ONLY_WOULD_TRADE | 9 | If the modify-order would cause a cancel-replace, the post-only replacement would have crossed and traded. |
| ONLY_ORDER_CANCEL_ACCEPTED | 17 | The given market accepts no order modifications at this time |
| OUTSIDE_PRICE_BAND | 11 | Limit orders cannot have bid price too low or ask price too high that is multiple times away from the internal reference price. |
| ORDER_QUANTITY_TOO_LOW | 12 | The value of the modified order, if traded fully, would be less than the minimum value allowed for this market. See `minOrderQuoteAmt` in the market definitions. |
| ORDER_QUANTITY_TOO_HIGH | 13 | The value of the modified order, if traded fully, would be greater than the maximum value allowed for this market. See `maxOrderQuoteAmt` in the market definitions. |
| MARGIN_TRADING_UNAVAILABLE | 14 | This subaccount is not enabled for margin trading. |
| EXCEEDS_FREE_BALANCE | 15 | The spot balance required to place this order exceeds the free balance usable given current open positions and margin requirements. |
| INSUFFICIENT_INITIAL_MARGIN | 16 | The subaccount does not have sufficient additional initial margin to place this order. |
| INSUFFICIENT_MAINTENANCE_MARGIN | 18 | The subaccount does not have sufficient additional maintenance margin to place this order. |
| EXCEEDS_INITIAL_NOTIONAL_LIMIT | 19 | The value of the order, if executed, would cause the subaccount's total position to exceed the initial notional limit for the configured leverage. |








## Scalar Value Types

| .proto Type | Notes | Rust | C++ | Python | Go |
| ----------- | ----- | ---- | --- | ------ | -- |
| double |  | f64 | double | float | float64 |
| float |  | f32 | float | float | float32 |
| int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | i32 | int32 | int | int32 |
| int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | i64 | int64 | int/long | int64 |
| uint32 | Uses variable-length encoding. | u32 | uint32 | int/long | uint32 |
| uint64 | Uses variable-length encoding. | u64 | uint64 | int/long | uint64 |
| sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | i32 | int32 | int | int32 |
| sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | i64 | int64 | int/long | int64 |
| fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | u64 | uint32 | int | uint32 |
| fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | u64 | uint64 | int/long | uint64 |
| sfixed32 | Always four bytes. | i32 | int32 | int | int32 |
| sfixed64 | Always eight bytes. | i64 | int64 | int/long | int64 |
| bool |  | bool | bool | boolean | bool |
| string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | String | string | str/unicode | string |
| bytes | May contain any arbitrary sequence of bytes. | Vec<u8> | string | str | []byte |

# Market Price Protection Limits

Price protection limits constrain where orders can be placed in a given market.

## Goals

There are a few competing goals to the protection logic:
- to prevent fills at undesirable prices, e.g. when using Market orders on wide markets or with no specified protection price
- to allow seamless trading when the market is tight
- to make sure that new quotes that would improve the book are never blocked

## Parameters

Three parameters affect price protection, and they can differ between markets:
- `priceBandBidPct`
- `priceBandAskPct`
- `protectionPriceLevels`

You can see the parameters configured for each market in the `markets` section of
the [Cube Market Definitions](https://api.cube.exchange/ir/v0/markets/).

For more details on those definitions, see [Exchange Info](/exchange-info.md).

## Protection Checks

There are two separate checks applied to each incoming order.  Both are considered separately.

When the characteristics of an order fall outside the boundaries of the check,
the order is rejected.

1. `priceBandBidPct` and`priceBandAskPct`
    - check is relative to the last known reference price
    - determines how far orders can be placed from the reference price
    - expressed as percentages, e.g. "25" means 25% of reference price
    - typically, these are very wide (25% and 400% for a factor of 4x ref price)
2. `protectionPriceLevels`
    - check is relative to the current top-of-book prices (TOB)
    - determines how far orders can be placed from the aggressing-side's best (i.e. TOB) price
    - expressed as a number of levels, e.g. 20 levels away from price 500 is price 520
    - applies only to markets with opposing orders
    - see diagram below for details

## Diagram

This diagram illustrates which prices will cause orders to be rejected.
Note the range of acceptable order prices in yellow:

<figure>
  <picture>
    <img
      src="/images/protection_price_levels_diagram.svg"
      alt="Diagram showing where market price protections apply"
    />
  </picture>
  <figcaption>Market Price Protection Levels</figcaption>
</figure>

### Description

1. Off-Market Limit Check (`priceBandBid/AskPct`)
    * The **reference price** is the last known price for the asset pair from an external price source.
    * Orders placed more than `priceBandBid/AskPct` off the reference price will be rejected.
    * This hints to participants to establish a market near the last known externally verified price
while still leaving ample room for the market to move away from that price.

2. Aggressing Threshold Calculation (`protectionPriceLevels`)
    * The aggressing threshold (`a_thresh`) is the tighter of the aggressing TOB and the reference price, improved by `protection_levels`.
    * Note that when sending a MarketWithProtection order with no price specified, the aggressing threshold will be used as the halting price.

3. Aggressing Threshold Limit Check (applies only when an opposing market exists, for which there are two possible cases):
    * Order Would Not Cross Market / Not Match (3a)
        * Market orders that don't cross the book will be rejected
        * Limit orders that don't cross the book are always accepted, regardless of the aggressing threshold, assuming they don't violate the Off-Market Limit Check in (1).

    * Order Would Cross Market / Match Immediately (3b)
        * Market orders will execute up to the aggressing threshold (`a_thresh`) or their specified protection price, whichever is tighter.
        * Limit orders with prices better, i.e. less aggressive than `a_thresh` will be accepted and will match immediately.
        * Limit orders with prices worse, i.e. more aggressive than `a_thresh` will be rejected.

Note that if a trader wants to cross a wide market:
- they can 'walk' the aggressing threshold over the opposing side of the market by repeatedly placing non-crossing limit orders close to same-side TOB.
- this moves the `a_thresh` and allows placing an order that crosses the book while remaining within the `a_thresh`.

This behavior encourages tighter markets and allows for gradual price discovery while still preventing trades at undesirable prices.

## Relevant Reject Errors

The following `NewRejectReason`s are sent when price protection rejects an order:

### `PROTECTION_PRICE_WOULD_NOT_TRADE`
- Trader sent a market order with a given protection price
- The protection price is tighter than the opposing TOB, so the order would not trade

Resolution: loosen the protection price to allow more slippage

### `SLIPPAGE_TOO_HIGH`
- Trader sent a market order
- the calculated `a_thresh` is tighter than the opposing TOB, so the order would not trade

Note that this can also appear when sending market orders with a specified protection price
as the order may be able to trade at that price, but not at `a_thresh`.

Resolution: place limit orders on the book to reduce the spread, then try crossing the market again

### `OUTSIDE_PRICE_BAND`
- `a_thresh` is tighter than the limit price or market price
- The order would cross the book and trade at the limit price or market price
- The market is wide, so the order is rejected

This reject is also sent for orders that are too far off the reference price,
or orders with a price of 0.

Resolution: place limit orders on the book to reduce the spread, then try crossing the market again
[Perpetual futures contracts](./contracts.md) are derivatives instruments that
provide continuous exposure to an underlying asset without explicit expiration
dates. These contracts maintain price alignment with the spot market through a
funding rate mechanism.

The [funding rate](./funding.md) facilitates price convergence between
perpetual futures and spot markets by transferring payments between long and
short position holders at regular intervals, typically every 8 hours, based on
the magnitude divergence from the underlying spot price and a prevailing
interest rate. When perpetual futures trade at a premium to spot, long
positions pay shorts. Conversely, when perpetual futures trade at a discount,
short positions pay longs.

Cube's perpetual futures trade on a central limit order book, which is a
transparent system that matches orders based on their 'price time priority'.
The highest bid (buy order) and lowest ask (offer or sell order) constitute the
best market for a given contract, ensuring transparent and efficient execution.
This best bid-ask spread is a component of funding rate determination.

Trading perpetual futures requires a Margin-enabled subaccount with sufficient
collateral. Currently, all Cube perpetuals are denominated in and
collateralized with USDC. Each contract specifies [margin
requirements](./margin.md) for opening and maintaining positions and open
orders. Subaccounts that breach maintenance margin requirements are subject to
[liquidation](./liquidation.md).

Position maintenance costs fluctuate based on market conditions, as funding
rates reflect the relative demand for long versus short exposure. During
periods of strong directional sentiment, funding rates can impose significant
holding costs on positions aligned with the prevailing market bias.
Cube currently offers cross-margined linear perpetual futures contracts for
various digital assets. Each perpetual contract is designed to track the
underlying spot price while providing leverage opportunities.

## Contract Specifications

Perpetual contracts and their parameters are defined as `assets` with
`AssetType::Perpetual` under [market
definitions](/exchange-info.md#markets). The high-level structure is as
follows:

| Field               | Description                                                                                                                                        | Example                                                       |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| underlying_asset_id | The underlying asset tracked by this contract                                                                                                      | BTC                                                           |
| settlement_asset_id | Asset used for settlement. This is implicitly also the contract's denominating asset (e.g the contract's Index price is denominated in this asset) | USDC                                                          |
| decimals            | Contract quantity precision, relative to whole units of the underlying asset                                                                       | -5 (each contract unit represents 1e-5 BTC, or 1000 satoshis) |
| symbol              | Trading pair symbol                                                                                                                                | BTC-USDC                                                      |
| market_id           | Unique identifier for the trading market. Each perpetual contract is one-to-one with a market.                                                     | 1000                                                          |
| margin_tier_table_id| The margin tier table for this contract                                                                                                            |                                                               |

Each contract's margin table information can be found in the corresponding
margin table.


## Pricing and Indexes

### Index Price
The index price is calculated using data from multiple exchanges to ensure
robust and manipulation-resistant prices. Used for funding calculations.

The index price calculation follows these key principles:

1. **Multi-Exchange Aggregation**: Prices are sourced from multiple major
   cryptocurrency exchanges to create a weighted average. This diversification
   helps prevent manipulation from any single exchange.

2. **Source-Quality-Weighted**: Each source's contribution to the index is
   weighted based on the source's quality score (which is a function of factors
   including trading volume, liquidity, etc.).

3. **Outlier Filtering**: Extreme price outliers are filtered out using
   statistical methods to maintain index stability and prevent manipulation
   attempts.

4. **Real-Time Updates**: The index price is updated frequently to ensure
   accurate tracking of the underlying market.

5. **Fallback Mechanisms**: If too many sources are unavailable, the market may
   enter a reduce-only mode.

### Mark Price
The mark price is used for PNL calculation and liquidation purposes. Used for
margin calculations (e.g unsettled PnL, liquidation, etc). It is derived from:

The mark price is calculated from the index price, funding rate, and time until
the end of the current funding interval.

```
funding basis = funding rate * (time until funding / funding interval)
mark price    = index price * (1 + funding basis)
```

An implication of this is that at the instant of funding payment, the mark
price change offsets the funding payment, and so the instantaneous account
equity does not change (though the margin requirements might). This results in
a mark price that converges to the spot index price over the course of each
funding interval. Squinting, it's like the future settles every funding
interval. See [funding](./funding.md) for more details.
Funding occurs at regular intervals in order to encourage price convergence
betweewn the perpetual contract and the underlying index price. Funding is only
paid by those with an open position at the time of the funding event,
regardless of when during the interval the position was opened. Moreover, the
amount of funding paid is based proportionally on the position value (defined
as `ABS(open contracts * mark price)`) at the time of the funding event,
regardless of subaccount leverage.

# Funding Calculation

The funding rate is composed of an interest component and a premium/discount
component.

The premium/discount component is calculated based on the average divergence of
the perpetual contract market from the index price.

Specifically, every `funding_rate_calculation_interval`, a 'snapshot' of the
order book is taken by sampling the perpetual contract's impact bid and ask
prices. Where `impact_bid_price` and `impact_ask_price` are the average
execution prices of aggressing `impact_bid_quantity` and `impact_ask_quantity`
into the order book. From this, we calculate the premium index as:

```
premium_index = (
  MAX(impact_bid_price - index_price, 0)
  - MAX(index_price - impact_ask_price, 0)
) / index_price
```

Every `funding_interval`, the funding rate is calculated as:

```
premium_index = AVG(premium_index)
funding_rate = premium_index + clamp(interest_rate - premium_index, -clamp, +clamp)
```

Currently, the interest rate is a fixed 0.01% per day, and clamp is a fixed 0.05%.

This funding is then clamped between the contract-specified minimum/maximum
funding rates. The clamped funding rate is then applied to the position value
to calculate the funding.

# Funding Application

```
funding = open contracts * index price
    * funding_rate
    * funding_interval / funding_period
```

Funding is credited or debited from the unsettled balance for every open
position, and is net zero across all positions since there are no fees
collected on the payments.

Funding is an atomic event from the perspective of exchange participants.
During the funding event, note that `mark_price == index_price`, and only after
the event is complete does the mark price get offset by the [funding
basis](./contracts.md#mark-price).
## Margin Modes

Currently, all Cube margin subaccounts are cross margined. As such, all
positions share the same margin balance. Positive PnL in one contract can be
used to offset negative PnL in another, but margin calculations and limits are
done and applied independently for each contract.

## Margin Table

Each contract is associated with a Margin Table, which defines the supported
margin tiers. Each margin tie is defined as follows

| Field                    | Description                                                                                                                                                                                                         |
| -------------------      | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    |
| Position Notional        | The maximum position notional that can be opened for this leverage tier. Note that a position (long or short) can increase in size beyond this limit due to mark price changes, but new contracts cannot be opened. |
| Max Leverage             | The maximum leverage allowed for this tier.                                                                                                                                                                         |
| Maintenance Margin Ratio | The maintenance margin ratio required for position notional within this tier.                                                                                                                                       |
| Maintenance Deduction    | A derived value useful for maintenance magrin calculations                                                                                                                                                          |

Where

```
MMR(N) = maintenance margin ratio on tier N
MD(N)  = maintenance margin deduction on tier N
       = position notional of tier N-1 * (MMR(N) - MMR(N-1)) + MD(N-1)
Maintenance Margin = Position Notional * MMR(N) - MD(N)
```

For example,

 | Tier | Position Notional | Max Leverage | Maintenance Margin Ratio | Maintenance Deduction |
 | ---- | ----------------- | ------------ | ------------------------ | --------------------- |
 | 1    | 50000.0           | 100          | 0.005                    | 0.0                   |
 | 2    | 200000.0          | 50           | 0.01                     | 250.0                 |
 | 3    | 500000.0          | 25           | 0.02                     | 2250.0                |
 | 4    | 1000000.0         | 10           | 0.05                     | 17250.0               |
 | 5    | 5000000.0         | 5            | 0.075                    | 42250.0               |
 | 6    | 10000000.0        | 3            | 0.166                    | 497250.0              |
 | 7    | 20000000.0        | 2            | 0.25                     | 1337250.0             |
 | 8    | 50000000.0        | 1            | 0.5                      | 6337250.0             |

These tiers follow strict monotonic rules: as tiers progress, position notionals
increase, maximum leverage decrease, and maintenance rates increase.
Additionally, each tier's maintenance rate is always lower than its initial
margin rate (determined by maximum leverage).

## Leverage and Initial Margin

Each subaccount has a configurable leverage ratio per perpetual contract.
The maximum leverage for a contract is effectively defined defined by the
maximum leverage of the highest leverage tier (100x in the above example). The
initial margin rate required to open the position is calculated as the
reciprocal of leverage.

When placing an order, the _effective notional_ of the position is calculated
inclusive of the new order at the current [mark
price](./contracts.md#mark-price) as

```text
Open Position Value = units * mark price
Effective Notional = Max (
    Abs(Open Position Value + Bid Order Notional),
    Abs(Open Position Value - Ask Order Notional),
)
```

For example, if the open position is short 1 BTC perpetual contract (`-1 *
10^-decimals` units) at a mark price of 100k, with an additional `0.5@90k` bid
and `0.2@110k` ask, the effective notional is `MAX(ABS(-100k + 45k), ABS(-100k - 22k)) = 122k`.

The initial margin is used by the position and cannot be used for other
operations (e.g opening more perpetual positions or placing spot orders or
withdrawals). Unrealized PnL is automatically available as initial margin for
new perpetual positions, but only realized PnL is available for spot
operations.

A subaccount's leverage ratio can be changed with open positions and orders,
but the new leverage ratio must satisfy all current position constraints.

### Order Entry

New orders are immediately marked to the contract's mark price, regardless of
the execution price. As such, unrealized PnL is considered part of the initial
margin requirements for new orders. As with spot orders, market orders are
cancelled when reaching the position limit (initial margin limit) instead of
being rejected, while limit orders are preflight-checked as having executed at
their specified limit price, and rejected if there is insufficient margin.

## Maintenance Margin

Cube's maintenance margin system operates independently of the leverage used to
open positions. Instead of considering how a position was opened, it focuses
solely on the position's notional value. This system employs tiers where larger
positions naturally require higher maintenance margins, with each tier defining
its specific maintenance margin rate.

Higher notional amounts required more conservative trading parameters through
lower maximum leverage and higher maintenance requirements. This tiered
approach helps manage risk concentration and potential market impact of large
positions. Positions are liquidated when the subaccount value (including
unrealized PnL) is less than the maintenance margin required.
Liquidation is a multi-step process that is trigged when a trader's account
equity is below the maintenance margin requirement. The liquidation process
helps prevent negative account equity and maintains market stability.

# Liquidation Process

Liquidation occurs over the following steps:

1. Open Market Liquidation
    - Open order cancellation
    - Market close positions
2. Takeover Liquidation and Auto-Deleveraging (ADL)
3. Insurance Fund and Socialized Loss

At each step, if the account equity is now above the maintenance margin
requirements, liquidation is complete and the process stops.

## Open Market Liquidation

Liquidation begins with forced open-market operations. Here, the liquidatee
(subaccount being liquidated) automatically performs market operations to
attempt to increase account health.

### Open Order Cancellation

First, the system automatically cancels all open orders. This cancellation is
crucial as open orders require maintenance margin allocation. By releasing this
allocated margin, the account may return to a healthy state without further
intervention.

### Market Close Positions

Second, if the position remains unhealthy after order cancellation, the system
attempts to close positions through market orders. These orders will target
prices that leave the account with 70% of the maintenance margin requirement as
equity.

For example, if there is an open position for 1 BTC @ 100'000 perpetual with a
maintenance margin of 10'000 USDC, market closes will leave at least 7'000
USDC, and so will aggress at a price of 97'000.

## Takeover Liquidation and Auto-Deleveraging (ADL)

If open market liquidation is unsuccessful, the protocol enables position
takeover through two mechanisms:

Active backstop liquidity providers may takeover all positions, and are
compensated by the liquidatee a `liquidator_fee` percentage of the position's
notional. This provides an opportunity for market participants to strategically
acquire positions while supporting system stability. Note that the
`liquidator_fee` is expressed as a percentage of the maintenance margin
requirement, and is based on the position's initial leverage, where higher
leverage positions are charged a greater percentage fee.

If there is insufficient capacity for backstop liquidity, the system implements
Auto-Deleveraging (ADL), where traders holding opposing positions automatically
assume portions of the liquidated position. The ADL process prioritizes traders
based on their PnL ranking.

```
unrealized PnL = open contracts * (mark price - cost basis)
effective leverage = open contract * mark price / account equity

ranking = if unrealized PnL > 0 {
    unrealized PnL * effective leverage
} else {
    unrealized PnL / effective leverage
}
```

Position rankings are calculated for open positions and sorted to determine the
order of deleveraging.


## Insurance Fund and Socialized Loss

Once all positions are closed, any remaining settlement-asset losses are
evaluated against the insurance fund. The fund serves as a protective buffer,
covering losses to the extent of its available resources.

In cases where the insurance fund is insufficient to cover remaining losses,
the protocol implements socialized loss distribution. Losses are allocated
across all traders proportionally to their current notional position sizes,
ensuring system stability through collective risk sharing.

# Liquidation Clearance Fee

To compensate for the risk and operational costs associated with liquidation,
there is an additional liquidation clearance fee charged to the liquidatee in
the market close and backstop liquidity phases. This liquidation clearance fee
is charged on the position's notional value cleared.

The liquidation clearance fee is paid to the insurance fund.

# Prices

## Liquidation Price

The price for a perpetual contract at which liquidation occurs for the
calculated subaccount, supposing that the prices of everything else is
constant.

Liquidation occurs when account equity is below the maintenance margin
requirement. The constituent changes in the provided contract's price is as
follows:

```text
   SUM(spot balance) + SUM(units * price + quote) < SUM(maintenance_margin(units * price))
=> SUM(s_i) + SUM(u_j * p_j + q_j) < SUM(maintenace_margin_j(u_j * p_j))
=> SUM(s_i) + SUM_j!=x(u_j * p_j + q_j) + (u_x * p_x + q_x)
        < SUM_j!=x(maintenace_margin_j(u_j * p_j)) + maintenace_margin_x(u_x * p_x)

   let C1 = SUM(s_i) = spot_balance
   let C2 = SUM_j!=x(u_j * p_j + q_j)
          = unsettled - (u_x * p_x + q_x)
   let C3 = SUM_j!=x(maintenace_margin_j(u_j * p_j))
          = maintenance_margin - maintenance_margin_x(u_x * p_x)
   let K = C3 - C1 - C2

=> C1 + C2 + (u_x * p_x + q_x) < C3 + maintenance_margin_x(u_x * p_x)
=> (u_x * p_x + q_x) - maintenance_margin_x(u_x * p_x) < K
=> (u_x * p_x) - maintenance_margin_x(u_x * p_x) < K - q_x
```

The left-hand-side is a piecewise continuous function of the contract's price.
We can then back out threshold price from the margin table. i.e for a given
tier:

```text
   maintence_margin_x(u_x * p_x) = MMR * u_x * p_x - OFFSET
=> (u_x * p_x) - (MMR * ABS(u_x * p_x) - OFFSET) = K - q_x
=> p_x = (K - q_x - OFFSET) / (1 - MMR * SIGN(u_x)) / u_x
```

## Bankruptcy Price

The price at which the account is bankrupt, supposing that the prices of
everything else is constant.

```text
   SUM(spot balance) + SUM(units * price + quote) < 0
=> C1 + C2 + (u_x * p_x + q_x) < 0
=> p_x < -(C1 + C2 + q_x) / u_x
```

## Spot Balance

Settlement asset (USDC) in the account. Spot balance is the [`available` amount
in AssetPosition](/order-entry/websocket-api.md#assetposition).

This is the settled USDC balance, and is always in your MPC wallet on chain.
Note that this balance excludes spot units this are reserved for open spot
orders or intents.

## Unsettled Balance

The unsettled balance (including Pnl, funding, fees, etc) for a particular
perpetual contract. This is equal to [`units * mark_price +
quote`](/order-entry/websocket-api.md#contractposition) for each perpetual
contract position. That is, each perpetual contract has a separate unsettled
balance, and the account's unsettled balance is their linear sum.

Note that this is distinct from the _unrealized PnL_, which is determined by
the cost basis and current mark price.

## Settlement

As mark prices change continuously, the value of open positions also change
continuously. Settlement is the discretized process of moving unsettled balance
from the open perpetual positions into the settlement asset (USDC) token
balance. Note that settlement does not have an impact on open positions or
account health, and is performed over the entire subaccount (i.e positive
unsettled balance in one contract cannot be settled independently of others).

Settlement takes two perpetual market participants with unsettled balance of
opposite signs, and reduces the magnitude of that unsettled balance equally for
each party by transferring USDC between the accounts. Settlement is fully
peer-to-peer, and require on-chain transactions to settle the token balance.
Note that since settlement is between accounts and not perpetual contracts,
party A who only traded contract X might be settled with party B who only
traded contract Y (where ostensibly some chain of intermediate parties had the
offsetting positions between).

Morever, settlement can only be initiated by acconuts with positive
realized PnL (and specifically, when the free balance is positive). But note
that the counterparty's negative unsettled PnL might be entirely from
unrealized PnL.

PnL can be settled at any time, and is settlement is performed automatically
when spot operations are performed that require additional spot balance.

### Example

Suppose Alice buys 1 BTC perpetual from Bob at 100k. Both have sufficient spot
balance.

| Operation         | Alice Open | Alice Unsettled | Alice Realized | Bob Open | Bob Unsettled | Bob Realized |
| ----------------- | ---------- | --------------- | -------------- | -------- | ------------- | ------------ |
| Initial           | 0          | 0               | 0              | 0        | 0             | 0            |
| Trade 1 @ 100k    | +1 BTC     | 0               | 0              | -1 BTC   | 0             | 0            |
| BTC mark @ 110k   | +1 BTC     | 10000           | 0              | -1 BTC   | -10000        | 0            |
| Funding 10 USDC   | +1 BTC     | 9990            | -10            | -1 BTC   | -9990         | 10           |
| Trade -0.5 @ 110k | +0.5 BTC   | 9990            | 4990           | -0.5 BTC | -9990         | -4990        |
| Trade -0.5 @ 100k | 0          | 4990            | 4990           | 0        | -4990         | -4990        |
| Settlement        | 0          | 0               | 4990           | 0        | 0             | -4990        |

Throughout this process, Alice and Bob's spot balances remain unchanged until
the final Settlement operation.

## Other Terminology

- **Unrealized PnL**: The total profit or loss of open positions.
- **Equity**: The total value of the account.
- **Wallet Balance**: The total value of the account, excluding unrealized PnL.
- **Available Balance**: The total value of the account, minus margin requirements.
- **Free Balance**: The amount of funds that can be used for spot operations
  from the account.

As formulas:

```
Unrealized PnL = SUM(Quantity * (Price - Cost Basis))
Equity = Spot Balance + Unsettled Balance
Wallet Balance = Equity - Unrealized PnL
Available Balance = Equity - Margin Requirement
Free Balance = max(0, min(Wallet Balance, Available Balance) - Margin Requirement)
```

# Margin Subaccounts

- To trade perpetual futures, you must create a subaccount enabled for `margin`
  trading. This subaccount is a superset of the `spot` subaccount type, and can
  perform all relevant spot operations (assuming sufficient margin).
    - [`{"accountType": "margin"}`](/exchange-info.md#users-subaccounts-1)

- To change the leverage override for a praticular contract.
    - [`{"contractId":"123","leverage":10}`](/exchange-info.md#users-subaccount-subaccount_id-1)

# New Messages

## Order Entry

- [ContractPosition](/order-entry/websocket-api.md#contractposition)
    - Open perpetual contract positions. Including (average) cost basis used
      for PnL calculations (used for e.g [free
      balance](./settlement.md#other-terminology) calculations).,
      cumulative funding paid / accrued, etc.

## Market Data

- [FundingCalculation](/market-data/websocket-api.md#fundingcalculation)
- [FundingApplication](/market-data/websocket-api.md#fundingapplication)
- [ContractStatistics](/market-data/websocket-api.md#contractstatistics)
