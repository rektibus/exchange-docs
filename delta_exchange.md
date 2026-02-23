<h1 id="ApiSection" class="section-header">Rest Api</h1>
This section documents the latest(v2) api for trading on Delta Exchange. The REST API has endpoints for account and order management as well as public market data.

If you are looking for the old api documentation, here is the link to [v1 api](https://github.com/delta-exchange/slate/blob/master/source/includes/_rest_api_v1.md) docs (now deprecated). 

REST API Endpoint URL for [Delta Exchange](https://www.delta.exchange)

 - **Production** - https://api.india.delta.exchange
 - **Testnet(Demo Account)** - https://cdn-ind.testnet.deltaex.org

<h1 id="delta-exchange-api-v2-assets">Assets</h1>

Get Asset List

## Get list of all assets

<a id="opIdgetAssets"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/assets', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/assets \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/assets',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /assets`

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    }
  ]
}
```

<h3 id="get-list-of-all-assets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Asset schema](#tocSasset)|Inline|

<h3 id="get-list-of-all-assets-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|deposit_status|enabled|
|deposit_status|disabled|
|withdrawal_status|enabled|
|withdrawal_status|disabled|

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-indices">Indices</h1>

Get Indices List

## Get indices

<a id="opIdgetIndices"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/indices', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/indices \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/indices',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /indices`

Indices refer to spot price indices that Delta Exchange creates by combining spot prices of prominent crypto exchanges. These indices form the underlying of futures and options contracts listed on Delta Exchange. All details of indices on Delta Exchange are available [here](https://www.delta.exchange/indices).

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  ]
}
```

<h3 id="get-indices-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Spot Index schema](#tocSindex)|Inline|

<h3 id="get-indices-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|index_type|spot_pair|
|index_type|fixed_interest_rate|
|index_type|floating_interest_rate|

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-products">Products</h1>

Get Product List

## Get list of products

<a id="opIdgetProducts"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /products`

The endpoint provides details about all available trading products on the platform. Each product represents a financial instrument like perpetual futures, options, or contracts for specific asset pairs.

<h3 id="get-list-of-products-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|contract_types|query|string|false|Comma separated list of contract types e.g. perpetual_futures,call_options, put_options|
|states|query|string|false|Comma separated list of states e.g. upcoming,live,expired,settled to get expired contracts.|
|after|query|string|false|after cursor for paginated request|
|before|query|string|false|before cursor for paginated request|
|page_size|query|string|false|size of a single page for paginated request, default: 100|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 27,
      "symbol": "BTCUSD",
      "description": "Bitcoin Perpetual futures, quoted, settled & margined in INR",
      "created_at": "2023-12-18T13:10:39Z",
      "updated_at": "2024-11-15T02:47:50Z",
      "settlement_time": null,
      "notional_type": "vanilla",
      "impact_size": 10000,
      "initial_margin": "0.5",
      "maintenance_margin": "0.25",
      "contract_value": "0.001",
      "contract_unit_currency": "BTC",
      "tick_size": "0.5",
      "product_specs": {
        "funding_clamp_value": 0.05,
        "only_reduce_only_orders_allowed": false,
        "tags": [
          "layer_1"
        ]
      },
      "state": "live",
      "trading_status": "operational",
      "max_leverage_notional": "100000",
      "default_leverage": "200",
      "initial_margin_scaling_factor": "0.0000025",
      "maintenance_margin_scaling_factor": "0.00000125",
      "taker_commission_rate": "0.0005",
      "maker_commission_rate": "0.0002",
      "liquidation_penalty_factor": "0.5",
      "contract_type": "perpetual_futures",
      "position_size_limit": 229167,
      "basis_factor_max_limit": "10.95",
      "is_quanto": false,
      "funding_method": "mark_price",
      "annualized_funding": "10.95",
      "price_band": "2.5",
      "underlying_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "quoting_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "settling_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "spot_index": {
        "id": 14,
        "symbol": ".DEXBTUSD",
        "constituent_exchanges": [
          {
            "name": "ExchangeA",
            "weight": 0.25
          }
        ],
        "underlying_asset_id": 13,
        "quoting_asset_id": 14,
        "tick_size": "0.5",
        "index_type": "spot_pair"
      }
    }
  ]
}
```

<h3 id="get-list-of-products-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Products](#tocSproduct)|Inline|

<h3 id="get-list-of-products-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|notional_type|vanilla|
|notional_type|inverse|
|state|live|
|state|expired|
|state|upcoming|
|trading_status|operational|
|trading_status|disrupted_cancel_only|
|trading_status|disrupted_post_only|
|deposit_status|enabled|
|deposit_status|disabled|
|withdrawal_status|enabled|
|withdrawal_status|disabled|
|index_type|spot_pair|
|index_type|fixed_interest_rate|
|index_type|floating_interest_rate|

<aside class="success">
This operation does not require authentication.
</aside>

## Get product by symbol

<a id="opIdgetProduct"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products/{symbol}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/{symbol} \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /products/{symbol}`

The endpoint retrieves details of a specific product identified by its symbol (e.g., BTCUSD, ETHUSD).

<h3 id="get-product-by-symbol-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|symbol of the desired product like BTCUSD, ETHUSD|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 27,
    "symbol": "BTCUSD",
    "description": "Bitcoin Perpetual futures, quoted, settled & margined in INR",
    "created_at": "2023-12-18T13:10:39Z",
    "updated_at": "2024-11-15T02:47:50Z",
    "settlement_time": null,
    "notional_type": "vanilla",
    "impact_size": 10000,
    "initial_margin": "0.5",
    "maintenance_margin": "0.25",
    "contract_value": "0.001",
    "contract_unit_currency": "BTC",
    "tick_size": "0.5",
    "product_specs": {
      "funding_clamp_value": 0.05,
      "only_reduce_only_orders_allowed": false,
      "tags": [
        "layer_1"
      ]
    },
    "state": "live",
    "trading_status": "operational",
    "max_leverage_notional": "100000",
    "default_leverage": "200",
    "initial_margin_scaling_factor": "0.0000025",
    "maintenance_margin_scaling_factor": "0.00000125",
    "taker_commission_rate": "0.0005",
    "maker_commission_rate": "0.0002",
    "liquidation_penalty_factor": "0.5",
    "contract_type": "perpetual_futures",
    "position_size_limit": 229167,
    "basis_factor_max_limit": "10.95",
    "is_quanto": false,
    "funding_method": "mark_price",
    "annualized_funding": "10.95",
    "price_band": "2.5",
    "underlying_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "quoting_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "settling_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "spot_index": {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  }
}
```

<h3 id="get-product-by-symbol-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|[Product](#tocSproduct)|Inline|

<h3 id="get-product-by-symbol-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|notional_type|vanilla|
|notional_type|inverse|
|state|live|
|state|expired|
|state|upcoming|
|trading_status|operational|
|trading_status|disrupted_cancel_only|
|trading_status|disrupted_post_only|
|deposit_status|enabled|
|deposit_status|disabled|
|withdrawal_status|enabled|
|withdrawal_status|disabled|
|index_type|spot_pair|
|index_type|fixed_interest_rate|
|index_type|floating_interest_rate|

<aside class="success">
This operation does not require authentication.
</aside>

## Get tickers for products

<a id="opIdgetTickers"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/tickers', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/tickers \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/tickers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /tickers`

This endpoint retrieves the live tickers for available trading products, with an optional filter by specified contract types. The contract types should be provided as a comma-separated list (e.g., futures, perpetual_futures, call_options). If no contract type is specified, data for all available products will be returned.

<h3 id="get-tickers-for-products-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|contract_types|query|string|false|A comma-separated list of contract types to filter the tickers. Example values include perpetual_futures, call_options, put_options.|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "close": 67321,
      "contract_type": "futures",
      "greeks": {
        "delta": "0.25",
        "gamma": "0.10",
        "rho": "0.05",
        "theta": "-0.02",
        "vega": "0.15"
      },
      "high": 68500.5,
      "low": 66300.25,
      "mark_price": "67000.00",
      "mark_vol": "500",
      "oi": "15000",
      "oi_value": "1000000",
      "oi_value_symbol": "USD",
      "oi_value_usd": "1050000",
      "open": 67000,
      "price_band": {
        "lower_limit": "61120.45",
        "upper_limit": "72300.00"
      },
      "product_id": 123456,
      "quotes": {
        "ask_iv": "0.25",
        "ask_size": "100",
        "best_ask": "150.00",
        "best_bid": "148.00",
        "bid_iv": "0.22",
        "bid_size": "50"
      },
      "size": 100,
      "spot_price": "67000.00",
      "strike_price": "68000.00",
      "symbol": "BTCUSD",
      "timestamp": 1609459200,
      "turnover": 5000000,
      "turnover_symbol": "USD",
      "turnover_usd": 5200000,
      "volume": 25000
    }
  ]
}
```

<h3 id="get-tickers-for-products-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of live [tickers](#tocSticker) for all products, including implied volatility (IV) for option strikes.|Inline|

<h3 id="get-tickers-for-products-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

## Get ticker for a product by symbol

<a id="opIdgetTicker"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/tickers/{symbol}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/tickers/{symbol} \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/tickers/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /tickers/{symbol}`

This endpoint retrieves the ticker data for a specific product, identified by its symbol. The ticker data includes live price data, open interest, implied volatility (IV) for options, and other related market data.

<h3 id="get-ticker-for-a-product-by-symbol-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|The symbol of the product for which the ticker data is requested (e.g., BTCUSD, ETHUSD).|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "close": 67321,
    "contract_type": "futures",
    "greeks": {
      "delta": "0.25",
      "gamma": "0.10",
      "rho": "0.05",
      "theta": "-0.02",
      "vega": "0.15"
    },
    "high": 68500.5,
    "low": 66300.25,
    "mark_price": "67000.00",
    "mark_vol": "500",
    "oi": "15000",
    "oi_value": "1000000",
    "oi_value_symbol": "USD",
    "oi_value_usd": "1050000",
    "open": 67000,
    "price_band": {
      "lower_limit": "61120.45",
      "upper_limit": "72300.00"
    },
    "product_id": 123456,
    "quotes": {
      "ask_iv": "0.25",
      "ask_size": "100",
      "best_ask": "150.00",
      "best_bid": "148.00",
      "bid_iv": "0.22",
      "bid_size": "50"
    },
    "size": 100,
    "spot_price": "67000.00",
    "strike_price": "68000.00",
    "symbol": "BTCUSD",
    "timestamp": 1609459200,
    "turnover": 5000000,
    "turnover_symbol": "USD",
    "turnover_usd": 5200000,
    "volume": 25000
  }
}
```

<h3 id="get-ticker-for-a-product-by-symbol-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|[Ticker](#tocSticker) data for the requested product, including implied volatility (IV) for option strikes, if applicable.|Inline|

<h3 id="get-ticker-for-a-product-by-symbol-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-orders">Orders</h1>

Placing Orders, Cancelling Orders, Placing batch orders, Cancelling batch orders, Get Open orders, Change Orders Leverage. Rate limits have been introduced recently that allows only set number of operations inside a matching engine in a timeframe. The current rate limits is 500 operations/sec for each product. For ex - placing 50 orders in a batch is equivalent to 50 operations as these orders will be processed by matching engine. Rate limits do not apply when cancelling orders.

## Place Order

<a id="opIdplaceOrder"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /orders`

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "stop_order_type": "stop_loss_order",
  "stop_price": "56000",
  "trail_amount": "50",
  "stop_trigger_method": "last_traded_price",
  "bracket_stop_loss_limit_price": "57000",
  "bracket_stop_loss_price": "56000",
  "bracket_trail_amount": "50",
  "bracket_take_profit_limit_price": "62000",
  "bracket_take_profit_price": "61000",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "reduce_only": false,
  "client_order_id": "34521712",
  "cancel_orders_accepted": false
}
```

<h3 id="place-order-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateOrderRequest](#schemacreateorderrequest)|true|Order which needs to be created. Rate limits apply.|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

<h3 id="place-order-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns [error](#place-order-error-description) if order could not be placed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="place-order-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Cancel Order

<a id="opIdcancelOrder"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`DELETE /orders`

> Body parameter

```json
{
  "id": 13452112,
  "client_order_id": "34521712",
  "product_id": 27
}
```

<h3 id="cancel-order-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteOrderRequest](#schemadeleteorderrequest)|true|Order which needs to be cancelled|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

<h3 id="cancel-order-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if order could not be cancelled|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="cancel-order-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Edit Order

<a id="opIdeditOrder"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /orders`

> Body parameter

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false,
  "cancel_orders_accepted": false,
  "stop_price": "56000",
  "trail_amount": "50"
}
```

<h3 id="edit-order-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditOrderRequest](#schemaeditorderrequest)|true|Order which needs to be edited. Rate limits apply.|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

<h3 id="edit-order-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns [error](#place-order-error-description) if order could not be placed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="edit-order-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get Active Orders

<a id="opIdgetOrders"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /orders`

<h3 id="get-active-orders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids, if not specified, all the orders will be returned|
|states|query|string|false|comma separated list of states - open,pending|
|contract_types|query|string|false|comma separated list of desired contract types, if not specified any parameters then, all the orders will be returned|
|order_types|query|string|false|comma separated order types|
|start_time|query|integer|false|from time in micro-seconds in epoc; referring to the order creation time|
|end_time|query|integer|false|from time in micro-seconds in epoc; referring to the order creation time|
|after|query|string|false|after cursor for pagination; becomes null if page after the current one does not exist|
|before|query|string|false|before cursor for pagination; becomes null if page before the current one does not exist|
|page_size|query|integer|false|number of records per page|

#### Enumerated Values

|Parameter|Value|
|---|---|
|contract_types|futures|
|contract_types|perpetual_futures|
|contract_types|call_options|
|contract_types|put_options|
|order_types|market|
|order_types|limit|
|order_types|stop_market|
|order_types|stop_limit|
|order_types|all_stop|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

<h3 id="get-active-orders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of orders as per the query|Inline|

<h3 id="get-active-orders-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Place Bracket order

<a id="opIdbracketOrder"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders/bracket', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders/bracket \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders/bracket',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /orders/bracket`

A bracket order is a set of TP and SL order. For a bracket order , size need not be specified as it closes the entire position. For a given contract, you can have multiple bracket orders for open orders but only a single bracket order for any open position.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "stop_loss_order": {
    "order_type": "limit_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "limit_price": "55000"
  },
  "take_profit_order": {
    "order_type": "limit_order",
    "stop_price": "65000",
    "limit_price": "64000"
  },
  "bracket_stop_trigger_method": "last_traded_price"
}
```

<h3 id="place-bracket-order-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateBracketOrderRequest](#schemacreatebracketorderrequest)|true|Bracket Order which needs to be updated |

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="place-bracket-order-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be updated|[ApiErrorResponse](#schemaapierrorresponse)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Edit Bracket order

<a id="opIdbracketOrder"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders/bracket', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders/bracket \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders/bracket',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /orders/bracket`

A bracket order is a set of TP and SL order. You can specify bracket order with an order that will create a new position. Use this api to change the bracket params attached with an order.

> Body parameter

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "bracket_stop_loss_limit_price": "55000",
  "bracket_stop_loss_price": "56000",
  "bracket_take_profit_limit_price": "65000",
  "bracket_take_profit_price": "64000",
  "bracket_trail_amount": "50",
  "bracket_stop_trigger_method": "last_traded_price"
}
```

<h3 id="edit-bracket-order-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditBracketOrderRequest](#schemaeditbracketorderrequest)|true|Bracket Order which needs to be updated |

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="edit-bracket-order-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be updated|[ApiErrorResponse](#schemaapierrorresponse)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Cancel all open orders

<a id="opIdcancelAllOrders"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders/all', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders/all \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders/all',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`DELETE /orders/all`

Cancels all orders for a given product id. If product id is not provided, it cancels orders for provided contract types. If none of them are provided, it cancels all the orders. Provide either product id or list of contract types at a time. If both are provided, contract types will be ignored.

> Body parameter

```json
{
  "product_id": 27,
  "contract_types": "perpetual_futures,put_options,call_options",
  "cancel_limit_orders": false,
  "cancel_stop_orders": false,
  "cancel_reduce_only_orders": false
}
```

<h3 id="cancel-all-open-orders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CancelAllFilterObject](#schemacancelallfilterobject)|false|Filters for selecting orders that needs to be cancelled|

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="cancel-all-open-orders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be cancelled|[ApiErrorResponse](#schemaapierrorresponse)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Create batch orders

<a id="opIdbatchCreate"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /orders/batch`

Orders in a batch should belong to the same contract. Max allowed size limit in a batch is 50. Rate limits apply. Please note that ioc is not valid time in force values for creating batch orders.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "limit_price": "59000",
      "size": 10,
      "side": "buy",
      "order_type": "limit_order",
      "time_in_force": "gtc",
      "mmp": "disabled",
      "post_only": false,
      "client_order_id": "34521712"
    }
  ]
}
```

<h3 id="create-batch-orders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchCreateOrdersRequest](#schemabatchcreateordersrequest)|true|Does not support time_in_force flag for orders, All orders in batch create are assumed to be gtc orders. batch create does not support stop orders, it support only limit orders|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

<h3 id="create-batch-orders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the orders placed|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be placed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="create-batch-orders-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Edit batch orders

<a id="opIdbatchEdit"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /orders/batch`

Orders to be edited in a batch. Rate limits apply.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 34521712,
      "limit_price": "59000",
      "size": 15,
      "mmp": "disabled",
      "post_only": false
    }
  ]
}
```

<h3 id="edit-batch-orders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchEditOrdersRequest](#schemabatcheditordersrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

<h3 id="edit-batch-orders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of edited orders|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be edited|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="edit-batch-orders-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Delete batch orders

<a id="opIdbatchDelete"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`DELETE /orders/batch`

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 13452112,
      "client_order_id": "34521712"
    }
  ]
}
```

<h3 id="delete-batch-orders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchDeleteOrdersRequest](#schemabatchdeleteordersrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

<h3 id="delete-batch-orders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the orders deleted|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be deleted|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="delete-batch-orders-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get Order by id

<a id="opIdgetOrderById"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/{order_id}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/{order_id} \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/{order_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /orders/{order_id}`

<h3 id="get-order-by-id-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|order_id|path|string|true|Id of the order|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

<h3 id="get-order-by-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|

<h3 id="get-order-by-id-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get Order by client oid

<a id="opIdgetOrderByCOI"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid} \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /orders/client_order_id/{client_oid}`

<h3 id="get-order-by-client-oid-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|client_oid|path|string|true|Client provided order id|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

<h3 id="get-order-by-client-oid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned client order id and latest state|Inline|

<h3 id="get-order-by-client-oid-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Change order leverage

<a id="opIdchangeOrderLeverage"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /products/{product_id}/orders/leverage`

> Body parameter

```json
{
  "leverage": 10
}
```

<h3 id="change-order-leverage-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|Product id of the ordered product|
|body|body|object|true|none|
|» leverage|body|string|true|Order leverage|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "leverage": 10,
    "order_margin": "563.2",
    "product_id": 27
  }
}
```

<h3 id="change-order-leverage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the OrderLeverage object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if leverage couldnt be changed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="change-order-leverage-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get order leverage

<a id="opIdgetOrderLeverage"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /products/{product_id}/orders/leverage`

<h3 id="get-order-leverage-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|Product id of the ordered product|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "leverage": 10,
    "order_margin": "563.2",
    "product_id": 27
  }
}
```

<h3 id="get-order-leverage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the OrderLeverage object|Inline|

<h3 id="get-order-leverage-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<h1 id="delta-exchange-api-v2-positions">Positions</h1>

Get Open positions, Change Position Margin, Close Position, Close All Position

## Get margined positions

<a id="opIdgetMarginedPositions"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/positions/margined', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/positions/margined \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/positions/margined',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /positions/margined`

Change in position may take upto 10secs to reflect. Use 'GET /position' for real-time data.

<h3 id="get-margined-positions-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids. If not specified any parameters, all the open positions will be returned|
|contract_types|query|string|false|comma separated list of desired contract types. If not specified any parameters then, all the open positions will be returned|

#### Enumerated Values

|Parameter|Value|
|---|---|
|contract_types|perpetual_futures|
|contract_types|call_options|
|contract_types|put_options|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "user_id": 0,
      "size": 0,
      "entry_price": "string",
      "margin": "string",
      "liquidation_price": "string",
      "bankruptcy_price": "string",
      "adl_level": 0,
      "product_id": 0,
      "product_symbol": "string",
      "commission": "string",
      "realized_pnl": "string",
      "realized_funding": "string"
    }
  ]
}
```

<h3 id="get-margined-positions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of all [open positions](#tocSposition)|Inline|

<h3 id="get-margined-positions-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get position

<a id="opIdgetPositions"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/positions', params={
  'product_id': '27'
}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/positions?product_id=27 \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/positions',
  params: {
  'product_id' => '27'
}, headers: headers

p JSON.parse(result)

```

`GET /positions`

Get real-time positions data.

<h3 id="get-position-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|query|integer|true|id of the product. Only send either product_id or underlying_asset_symbol.|
|underlying_asset_symbol|query|string|false|Underlying asset symbol. e.g. 'BTC', 'ETH'. This gives a list of all positions in products which have the given underlying asset. Only send either product_id or underlying_asset_symbol.|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "size": 12,
    "entry_price": "string"
  }
}
```

<h3 id="get-position-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Open position for the give product id|Inline|

<h3 id="get-position-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Auto Topup

<a id="opIdchangeAutoTopup"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/positions/auto_topup', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/positions/auto_topup \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/positions/auto_topup',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /positions/auto_topup`

Changes position auto topup flag. Positions automatically inherits auto topup flag of the account. If account level auto topop is set to false, use this api to change auto topup flag for individual positions.

> Body parameter

```json
{
  "product_id": 0,
  "auto_topup": "false"
}
```

<h3 id="auto-topup-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» product_id|body|integer|true|none|
|» auto_topup|body|boolean|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
}
```

<h3 id="auto-topup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the position object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if position margin could not be changed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="auto-topup-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Add/Remove position margin

<a id="opIdchangePositionMargin"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/positions/change_margin', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/positions/change_margin \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/positions/change_margin',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /positions/change_margin`

> Body parameter

```json
{
  "product_id": 0,
  "delta_margin": "string"
}
```

<h3 id="add/remove-position-margin-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» product_id|body|integer|true|none|
|» delta_margin|body|string|true|Delta in the position margin, positive in case of adding margin & negative in case of removing margin|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
}
```

<h3 id="add/remove-position-margin-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the position object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if position margin could not be changed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="add/remove-position-margin-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Close all positions 

<a id="opIdcloseAllPosition"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/positions/close_all', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/positions/close_all \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/positions/close_all',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /positions/close_all`

> Body parameter

```json
{
  "close_all_portfolio": true,
  "close_all_isolated": true,
  "user_id": 0
}
```

<h3 id="close-all-positions--parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» close_all_portfolio|body|boolean|true|none|
|» close_all_isolated|body|boolean|true|none|
|» user_id|body|integer|true|none|

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="close-all-positions--responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if not able to close all positions|[ApiErrorResponse](#schemaapierrorresponse)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<h1 id="delta-exchange-api-v2-tradehistory">TradeHistory</h1>

Get Orders History, Get Fill History

## Get order history (cancelled and closed)

<a id="opIdgetOrderHistory"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/history', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/history \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/history',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /orders/history`

<h3 id="get-order-history-(cancelled-and-closed)-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids|
|contract_types|query|string|false|comma separated list of desired contract types|
|order_types|query|string|false|comma separated order types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

#### Enumerated Values

|Parameter|Value|
|---|---|
|order_types|market|
|order_types|limit|
|order_types|stop_market|
|order_types|stop_limit|
|order_types|all_stop|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

<h3 id="get-order-history-(cancelled-and-closed)-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of closed and cancelled orders. [Order schema](#tocSorder)|Inline|

<h3 id="get-order-history-(cancelled-and-closed)-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## GET user fills by filters

<a id="opIdgetUserfills"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/fills', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/fills \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/fills',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /fills`

<h3 id="get-user-fills-by-filters-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids|
|contract_types|query|string|false|comma separated list of desired contract types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 0,
      "size": 0,
      "fill_type": "normal",
      "side": "buy",
      "price": "string",
      "role": "taker",
      "commission": "string",
      "created_at": "string",
      "product_id": 0,
      "product_symbol": "string",
      "order_id": "string",
      "settling_asset_id": 0,
      "settling_asset_symbol": "string",
      "meta_data": {
        "commission_deto": "string",
        "commission_deto_in_settling_asset": "string",
        "effective_commission_rate": "string",
        "liquidation_fee_deto": "string",
        "liquidation_fee_deto_in_settling_asset": "string",
        "order_price": "string",
        "order_size": "string",
        "order_type": "string",
        "order_unfilled_size": "string",
        "tfc_used_for_commission": "string",
        "tfc_used_for_liquidation_fee": "string",
        "total_commission_in_settling_asset": "string",
        "total_liquidation_fee_in_settling_asset": "string"
      }
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

<h3 id="get-user-fills-by-filters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of [fills](#tocSfill)|Inline|

<h3 id="get-user-fills-by-filters-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|fill_type|normal|
|fill_type|adl|
|fill_type|liquidation|
|fill_type|settlement|
|fill_type|otc|
|side|buy|
|side|sell|
|role|taker|
|role|maker|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Download Fills history

<a id="opIddownloadFillsHistory"></a>

> Code samples

```python
import requests
headers = {
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/fills/history/download/csv', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/fills/history/download/csv \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/fills/history/download/csv',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /fills/history/download/csv`

<h3 id="download-fills-history-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids|
|contract_types|query|string|false|comma separated list of desired contract types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|

<h3 id="download-fills-history-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|csv of fills for the filter query|None|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<h1 id="delta-exchange-api-v2-orderbook">Orderbook</h1>

L2Orderbook

## Get L2 orderbook

<a id="opIdgetL2Orderbook"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/l2orderbook/{symbol}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/l2orderbook/{symbol} \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/l2orderbook/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /l2orderbook/{symbol}`

<h3 id="get-l2-orderbook-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|none|
|depth|query|integer|false|number of levels on each side|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "buy": [
      {
        "depth": "983",
        "price": "9187.5",
        "size": 205640
      }
    ],
    "last_updated_at": 1654589595784000,
    "sell": [
      {
        "depth": "1185",
        "price": "9188.0",
        "size": 113752
      }
    ],
    "symbol": "BTCUSD"
  }
}
```

<h3 id="get-l2-orderbook-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|L2 orderbook for the product|Inline|

<h3 id="get-l2-orderbook-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-trades">Trades</h1>

Get Trades of a contract

## Get public trades

<a id="opIdgetTrades"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/trades/{symbol}', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/trades/{symbol} \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/trades/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /trades/{symbol}`

<h3 id="get-public-trades-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "trades": [
      {
        "side": "buy",
        "size": 0,
        "price": "string",
        "timestamp": 0
      }
    ]
  }
}
```

<h3 id="get-public-trades-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of recent trades of the product|Inline|

<h3 id="get-public-trades-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-wallet">Wallet</h1>

Get balances, Get transaction history

## Get Wallet Balances

<a id="opIdgetBalances"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/balances', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/balances \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/balances',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /wallet/balances`

> Example responses

> 200 Response

```json
{
  "meta": {
    "net_equity": "string",
    "robo_trading_equity": "string"
  },
  "result": [
    {
      "asset_id": 0,
      "asset_symbol": "string",
      "available_balance": "string",
      "available_balance_for_robo": "string",
      "balance": "string",
      "blocked_margin": "string",
      "commission": "string",
      "cross_asset_liability": "string",
      "cross_commission": "string",
      "cross_locked_collateral": "string",
      "cross_order_margin": "string",
      "cross_position_margin": "string",
      "id": 0,
      "interest_credit": "string",
      "order_margin": "string",
      "pending_referral_bonus": "string",
      "pending_trading_fee_credit": "string",
      "portfolio_margin": "string",
      "position_margin": "string",
      "trading_fee_credit": "string",
      "unvested_amount": "string",
      "user_id": 0
    }
  ],
  "success": true
}
```

<h3 id="get-wallet-balances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of wallets attached to the user account|[WalletPayload](#schemawalletpayload)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get Wallet transactions

<a id="opIdgetTransactions"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/transactions', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/transactions \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/transactions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /wallet/transactions`

<h3 id="get-wallet-transactions-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset_ids|query|integer|false|comma separated list of asset_ids for which to get txns logs|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|
|transaction_types|query|[TransactionTypes](#schematransactiontypes)|false|transaction types to retrieve|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 0,
      "amount": "string",
      "balance": "string",
      "transaction_type": "string",
      "meta_data": {},
      "product_id": 0,
      "asset_id": 0,
      "asset_symbol": 0,
      "created_at": "string"
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

<h3 id="get-wallet-transactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|list of [Wallet transactions](#tocStransaction)|Inline|

<h3 id="get-wallet-transactions-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|transaction_type|cashflow|
|transaction_type|deposit|
|transaction_type|withdrawal|
|transaction_type|commission|
|transaction_type|conversion|
|transaction_type|funding|
|transaction_type|settlement|
|transaction_type|liquidation_fee|
|transaction_type|spot_trade|
|transaction_type|withdrawal_cancellation|
|transaction_type|referral_bonus|
|transaction_type|sub_account_transfer|
|transaction_type|commission_rebate|
|transaction_type|promo_credit|
|transaction_type|trading_credits|
|transaction_type|trading_credits_forfeited|
|transaction_type|trading_credits_paid|
|transaction_type|trading_fee_credits_paid_liquidation_fee|
|transaction_type|trading_credits_reverted|
|transaction_type|interest_credit|
|transaction_type|external_deposit|
|transaction_type|credit_line|
|transaction_type|trading_competition|
|transaction_type|fund_deposit|
|transaction_type|fund_withdrawal|
|transaction_type|fund_wallet_deposit|
|transaction_type|fund_wallet_withdrawal|
|transaction_type|fund_reward|
|transaction_type|trade_farming_reward|
|transaction_type|interest_credit|
|transaction_type|revert|
|transaction_type|raf_bonus|
|transaction_type|fill_appropriation|
|transaction_type|incident_compensation|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Download Wallet transactions

<a id="opIddownloadTransactions"></a>

> Code samples

```python
import requests
headers = {
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/transactions/download', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/transactions/download \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/transactions/download',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /wallet/transactions/download`

<h3 id="download-wallet-transactions-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset_ids|query|integer|false|comma separated list of asset_ids|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

<h3 id="download-wallet-transactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|csv of transactions for that wallet|None|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Request asset transfer

<a id="opIdassetTransfer"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /wallets/sub_account_balance_transfer`

This api transfers asset from one subaccount to another subaccount or to the main/parent account. Please ensure that the subaccounts involved in the transfer should belong to the same parent account. Requests to transfer assets across subaccounts that belong to different parent accounts will fail. Please make sure that the api key used to make this api request belongs to the main/parent account.

> Body parameter

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null
}
```

<h3 id="request-asset-transfer-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetTransferSubaccountReq](#schemaassettransfersubaccountreq)|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": null
}
```

<h3 id="request-asset-transfer-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns success message|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error code|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="request-asset-transfer-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Request subaccount balance transfer history.

<a id="opIdSubaccountTransferHistory"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /wallets/sub_accounts_transfer_history`

This api returns the wallet balance transfers for subaccounts belonging to the parent/main account of an api user. Make sure you are calling this api from the main account. If no subaccount is mentioned in the request, data for all the subacounts will be returned. Use page size to get more entries in a single request.

> Body parameter

```json
{
  "subaccount_user_id": "string",
  "before": "string",
  "after": "string",
  "page_size": 10
}
```

<h3 id="request-subaccount-balance-transfer-history.-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SubaccountTransferHistory](#schemasubaccounttransferhistory)|true|none|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "transferrer_user_id": "string",
      "transferee_user_id": "string",
      "asset_symbol": "string",
      "amount": null,
      "created_at": "string",
      "transferee_user": {},
      "transferrer_user": {}
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

<h3 id="request-subaccount-balance-transfer-history.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns success message|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error code|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="request-subaccount-balance-transfer-history.-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<h1 id="delta-exchange-api-v2-stats">Stats</h1>

Get Volume Stats

## Get volume stats

<a id="opIdgetStat"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/stats', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/stats \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/stats',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /stats`

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "last_30_days_volume": 0,
    "last_7_days_volume": 0,
    "total_volume": 0
  }
}
```

<h3 id="get-volume-stats-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|sum of turnover in the last 7 and 30 days along with  Total Volume in the last 24 hours (in USD)|Inline|

<h3 id="get-volume-stats-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-mmp">MMP</h1>

Market maker protection

## Update MMP config

<a id="opIdupdateMMP"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/users/update_mmp', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/update_mmp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/users/update_mmp',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /users/update_mmp`

Channel provides updates when MMP is triggered. Market maker protection is available to registered market makers by default. Others can reach out to support for getting access to MMP. More info [here](https://guides.delta.exchange/delta-exchange-user-guide/market-makers-guide/market-maker-protection).

> Body parameter

```json
{
  "asset": "string",
  "window_interval": 0,
  "freeze_interval": 0,
  "trade_limit": "string",
  "delta_limit": "string",
  "vega_limit": "string",
  "mmp": "mmp1"
}
```

<h3 id="update-mmp-config-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MMPConfigUpdateRequest](#schemammpconfigupdaterequest)|true|mmp config for a given underlying asset|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 57354187,
    "default_auto_topup": true,
    "mmp_config": null,
    "deto_for_commission": false,
    "vip_level": 0,
    "vip_discount_factor": "0.00",
    "volume_30d": "1060.675333",
    "email_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": true,
      "order_fill": true,
      "stop_order_trigger": true
    },
    "notification_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": false,
      "order_fill": true,
      "price_alert": true,
      "stop_order_trigger": true
    },
    "price_alert_assets": [
      "BTC",
      "ETH"
    ],
    "enabled_portfolios": {},
    "interest_credit": false
  }
}
```

<h3 id="update-mmp-config-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the User Preference which contains mmp config|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if mmp is not enabled on the account|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="update-mmp-config-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Reset MMP

<a id="opIdresetMMP"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/users/reset_mmp', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/reset_mmp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/users/reset_mmp',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /users/reset_mmp`

> Body parameter

```json
{
  "asset": "string",
  "mmp": "mmp1"
}
```

<h3 id="reset-mmp-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MMPResetRequest](#schemammpresetrequest)|true|reset mmp config for a given underlying asset|

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="reset-mmp-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the User Preference which contains mmp config|[ApiSuccessResponse](#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if mmp is not enabled on the account|[ApiErrorResponse](#schemaapierrorresponse)|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<!-- <h1 id="delta-exchange-api-v2-dead-man-s-switch-auto-cancel-">Dead Man's Switch (Auto Cancel)</h1>

Set up timers for auto orders cancel in case of network malfunctions 

## Cancel After

<a id="opIdcancelAfter"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders/cancel_after', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders/cancel_after \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders/cancel_after',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`POST /orders/cancel_after`

> Body parameter

```json
{
  "cancel_after": "5000"
}
```

<h3 id="cancel-after-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CancelAfterRequest](#schemacancelafterrequest)|true|cancel after details|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "cancel_after_enabled": "true",
    "cancel_after_timestamp": "1669119262000"
  }
}
```

<h3 id="cancel-after-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the cancel_after configs set|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns if configs couldnt be set|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="cancel-after-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|cancel_after_enabled|false|
|cancel_after_enabled|true|

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside> -->

<h1 id="delta-exchange-api-v2-account">Account</h1>

Account level settings

## Get users trading preferences

<a id="opIdgetTradingPreferences"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/users/trading_preferences', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/users/trading_preferences \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/users/trading_preferences',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /users/trading_preferences`

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 57354187,
    "default_auto_topup": true,
    "mmp_config": null,
    "deto_for_commission": false,
    "vip_level": 0,
    "vip_discount_factor": "0.00",
    "volume_30d": "1060.675333",
    "email_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": true,
      "order_fill": true,
      "stop_order_trigger": true
    },
    "notification_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": false,
      "order_fill": true,
      "price_alert": true,
      "stop_order_trigger": true
    },
    "price_alert_assets": [
      "BTC",
      "ETH"
    ],
    "enabled_portfolios": {},
    "interest_credit": false
  }
}
```

<h3 id="get-users-trading-preferences-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User trading preferences attached to the account|Inline|

<h3 id="get-users-trading-preferences-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Update users trading preferences

<a id="opIdupdateTradingPreferences"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/users/trading_preferences', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/trading_preferences \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/users/trading_preferences',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /users/trading_preferences`

> Body parameter

```json
{
  "default_auto_topup": true,
  "showMarketOrdersForOptionsInBracket": true,
  "interest_credit": false,
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "order_cancel": true,
    "marketing": true
  },
  "notification_preferences": {
    "adl": false,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "price_alert": true,
    "marketing": true
  }
}
```

<h3 id="update-users-trading-preferences-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditUserPreference](#schemaedituserpreference)|true|trading preferences|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 57354187,
    "default_auto_topup": true,
    "mmp_config": null,
    "deto_for_commission": false,
    "vip_level": 0,
    "vip_discount_factor": "0.00",
    "volume_30d": "1060.675333",
    "email_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": true,
      "order_fill": true,
      "stop_order_trigger": true
    },
    "notification_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": false,
      "order_fill": true,
      "price_alert": true,
      "stop_order_trigger": true
    },
    "price_alert_assets": [
      "BTC",
      "ETH"
    ],
    "enabled_portfolios": {},
    "interest_credit": false
  }
}
```

<h3 id="update-users-trading-preferences-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User trading preferences attached to the account|Inline|

<h3 id="update-users-trading-preferences-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get subaccounts

<a id="opIdgetSubaccounts"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/sub_accounts', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/sub_accounts \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/sub_accounts',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /sub_accounts`

This api returns all the subaccounts belonging to the same parent/main user. Make sure to call this api from the parent user.

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": "98765432",
      "email": "rajtrader2342@gmail.com",
      "account_name": "Main",
      "first_name": "Rajesh",
      "last_name": "Sharma",
      "dob": "1985-08-25",
      "country": "India",
      "phone_number": "9876543210",
      "margin_mode": "isolated",
      "pf_index_symbol": ".DEXBTUSD",
      "is_sub_account": false,
      "is_kyc_done": true
    }
  ]
}
```

<h3 id="get-subaccounts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Subaccounts belonging to the same parent account.|Inline|

<h3 id="get-subaccounts-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Get user

<a id="opIdgetUser"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/profile', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/profile \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/profile',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /profile`

This api returns the user object.

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": "98765432",
    "email": "rajtrader2342@gmail.com",
    "account_name": "Main",
    "first_name": "Rajesh",
    "last_name": "Sharma",
    "dob": "1985-08-25",
    "country": "India",
    "phone_number": "9876543210",
    "margin_mode": "isolated",
    "pf_index_symbol": ".DEXBTUSD",
    "is_sub_account": false,
    "is_kyc_done": true
  }
}
```

<h3 id="get-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User Object|Inline|

<h3 id="get-user-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

## Change margin mode

<a id="opIdchangeMarginMode"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/users/margin_mode', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/margin_mode \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/users/margin_mode',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`PUT /users/margin_mode`

> Body parameter

```json
{
  "margin_mode": "isolated",
  "subaccount_user_id": "5112346"
}
```

<h3 id="change-margin-mode-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ChangeMarginModeRequest](#schemachangemarginmoderequest)|true|changes margin mode of the user|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": "98765432",
    "email": "rajtrader2342@gmail.com",
    "account_name": "Main",
    "first_name": "Rajesh",
    "last_name": "Sharma",
    "dob": "1985-08-25",
    "country": "India",
    "phone_number": "9876543210",
    "margin_mode": "isolated",
    "pf_index_symbol": ".DEXBTUSD",
    "is_sub_account": false,
    "is_kyc_done": true
  }
}
```

<h3 id="change-margin-mode-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns the [profile](#tocSuser) with the updated margin mode|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if margin mode could not be changed|[ApiErrorResponse](#schemaapierrorresponse)|

<h3 id="change-margin-mode-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
</aside>

<h1 id="delta-exchange-api-v2-settlement-prices">Settlement Prices</h1>

## Get product settlement prices

<a id="opIdgetProduct"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products/?states=expired', params={

}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/?states=expired \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/?states=expired',
  params: {
  }, headers: headers

p JSON.parse(result)

```

`GET /products/?states=expired`

<h3 id="get-product-settlement-prices-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|states|query|string|false|Comma separated list of states e.g. to get expired contracts https://api.india.delta.exchange/v2/products?contract_types=call_options&states=expired |
|page_size|query|string|false|size of a single page for paginated request, default: 100|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 27,
    "symbol": "BTCUSD",
    "description": "Bitcoin Perpetual futures, quoted, settled & margined in INR",
    "created_at": "2023-12-18T13:10:39Z",
    "updated_at": "2024-11-15T02:47:50Z",
    "settlement_time": null,
    "notional_type": "vanilla",
    "impact_size": 10000,
    "initial_margin": "0.5",
    "maintenance_margin": "0.25",
    "contract_value": "0.001",
    "contract_unit_currency": "BTC",
    "tick_size": "0.5",
    "product_specs": {
      "funding_clamp_value": 0.05,
      "only_reduce_only_orders_allowed": false,
      "tags": [
        "layer_1"
      ]
    },
    "state": "live",
    "trading_status": "operational",
    "max_leverage_notional": "100000",
    "default_leverage": "200",
    "initial_margin_scaling_factor": "0.0000025",
    "maintenance_margin_scaling_factor": "0.00000125",
    "taker_commission_rate": "0.0005",
    "maker_commission_rate": "0.0002",
    "liquidation_penalty_factor": "0.5",
    "contract_type": "perpetual_futures",
    "position_size_limit": 229167,
    "basis_factor_max_limit": "10.95",
    "is_quanto": false,
    "funding_method": "mark_price",
    "annualized_funding": "10.95",
    "price_band": "2.5",
    "underlying_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "quoting_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "settling_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "spot_index": {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  }
}
```

<h3 id="get-product-settlement-prices-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of products|Inline|

<h3 id="get-product-settlement-prices-responseschema">Response Schema</h3>

#### Enumerated Values

|Property|Value|
|---|---|
|notional_type|vanilla|
|notional_type|inverse|
|state|live|
|state|expired|
|state|upcoming|
|trading_status|operational|
|trading_status|disrupted_cancel_only|
|trading_status|disrupted_post_only|
|deposit_status|enabled|
|deposit_status|disabled|
|withdrawal_status|enabled|
|withdrawal_status|disabled|
|index_type|spot_pair|
|index_type|fixed_interest_rate|
|index_type|floating_interest_rate|

<aside class="success">
This operation does not require authentication.
</aside>

<h1 id="delta-exchange-api-v2-historical-ohlc-candles-sparklines">Historical OHLC Candles/Sparklines</h1>

## GET historical ohlc candles

<a id="opIdgetCandles"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/history/candles', params={
  'resolution': '5m',  'symbol': 'BTCUSD',  'start': '1685618835',  'end': '1722511635'
}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/history/candles?resolution=5m&symbol=BTCUSD&start=1685618835&end=1722511635 \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/history/candles',
  params: {
  'resolution' => '5m',
'symbol' => 'BTCUSD',
'start' => '1685618835',
'end' => '1722511635'
}, headers: headers

p JSON.parse(result)

```

`GET /history/candles`

It returns historical Open-High-Low-Close(ohlc) candles data of the symbol as per input values for resolution, start time and end time. Also, it can return only upto 2000 candles maximum in a response.

<h3 id="get-historical-ohlc-candles-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|resolution|query|string|true|ohlc candle time frames like 1m, 5m, 1h|
|symbol|query|string|true|To get funding history pass symbol as FUNDING:${symbol}, mark price MARK:${symbol} and OI data OI:${symbol} for e.g. - FUNDING:BTCUSD, MARK:C-BTC-66400-010824, OI:ETHUSD|
|start|query|integer|true|Start time: unix timestamp in seconds|
|end|query|integer|true|End time: unix timestamp in seconds|

#### Enumerated Values

|Parameter|Value|
|---|---|
|resolution|1m|
|resolution|3m|
|resolution|5m|
|resolution|15m|
|resolution|30m|
|resolution|1h|
|resolution|2h|
|resolution|4h|
|resolution|6h|
|resolution|1d|
|resolution|1w|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "time": 0,
      "open": 0,
      "high": 0,
      "low": 0,
      "close": 0,
      "volume": 0
    }
  ]
}
```

<h3 id="get-historical-ohlc-candles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|ohlc|Inline|

<h3 id="get-historical-ohlc-candles-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

## GET product history sparklines

<a id="opIdgetSparklines"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/history/sparklines', params={
  'symbols': 'ETHUSD,MARK:BTCUSD'
}, headers = headers)

print r.json()

```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/history/sparklines?symbols=ETHUSD%2CMARK%3ABTCUSD \
  -H 'Accept: application/json'

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/history/sparklines',
  params: {
  'symbols' => 'ETHUSD,MARK:BTCUSD'
}, headers: headers

p JSON.parse(result)

```

`GET /history/sparklines`

<h3 id="get-product-history-sparklines-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbols|query|string|true|comma separated product symbols|

> Example responses

> 200 Response

```json
{
  "success": true,
  "result": {
    "ETHUSD": [
      [
        1594214051,
        0.00003826
      ],
      [
        1594214051,
        0.00003826
      ]
    ],
    "MARK:BTCUSD": [
      [
        1594215270,
        0.00003826
      ]
    ]
  }
}
```

<h3 id="get-product-history-sparklines-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|product history sparkline|Inline|

<h3 id="get-product-history-sparklines-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication.
</aside>

# Schemas

<h2 id="tocSapisuccessresponse">ApiSuccessResponse</h2>

<a id="schemaapisuccessresponse"></a>

```json
{
  "success": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|boolean|false|none|none|

<h2 id="tocSapierrorresponse">ApiErrorResponse</h2>

<a id="schemaapierrorresponse"></a>

```json
{
  "success": false,
  "error": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|boolean|false|none|none|
|error|object|false|none|none|

<h2 id="tocSindex">Index</h2>

<a id="schemaindex"></a>

```json
{
  "id": 14,
  "symbol": ".DEXBTUSD",
  "constituent_exchanges": [
    {
      "name": "ExchangeA",
      "weight": 0.25
    }
  ],
  "underlying_asset_id": 13,
  "quoting_asset_id": 14,
  "tick_size": "0.5",
  "index_type": "spot_pair"
}

```

*Details of an index used in trading, including its constituents and characteristics.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier for the index.|
|symbol|string|false|none|Symbol representing the index, typically prefixed by '.DE' followed by base asset and quoting asset.|
|constituent_exchanges|[object]|false|none|Details of constituent exchanges, including their names and weights in the index.|
|» name|string|false|none|Name of the constituent exchange.|
|» weight|number|false|none|Weight of the exchange in the index.|
|underlying_asset_id|integer|false|none|ID of the underlying asset for the index.|
|quoting_asset_id|integer|false|none|ID of the quoting asset for the index.|
|tick_size|string|false|none|Precision of the spot price in decimal format.|
|index_type|string|false|none|Type of the index.|

#### Enumerated Values

|Property|Value|
|---|---|
|index_type|spot_pair|
|index_type|fixed_interest_rate|
|index_type|floating_interest_rate|

<h2 id="tocSarrayofindices">ArrayOfIndices</h2>

<a id="schemaarrayofindices"></a>

```json
[
  {
    "id": 14,
    "symbol": ".DEXBTUSD",
    "constituent_exchanges": [
      {
        "name": "ExchangeA",
        "weight": 0.25
      }
    ],
    "underlying_asset_id": 13,
    "quoting_asset_id": 14,
    "tick_size": "0.5",
    "index_type": "spot_pair"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Index](#schemaindex)]|false|none|[Details of an index used in trading, including its constituents and characteristics.]|

<h2 id="tocSproductspecs">ProductSpecs</h2>

<a id="schemaproductspecs"></a>

```json
{
  "funding_clamp_value": 0.05,
  "only_reduce_only_orders_allowed": false,
  "tags": [
    "layer_1"
  ]
}

```

*Specifications related to the specific product or contract.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|funding_clamp_value|number|false|none|The maximum allowable funding rate clamp value.|
|only_reduce_only_orders_allowed|boolean|false|none|Indicates whether only reduce-only orders are allowed.|
|tags|[string]|false|none|Tags associated with the product specifications.|

<h2 id="tocSasset">Asset</h2>

<a id="schemaasset"></a>

```json
{
  "id": 14,
  "symbol": "USD",
  "precision": 8,
  "deposit_status": "enabled",
  "withdrawal_status": "enabled",
  "base_withdrawal_fee": "0.000000000000000000",
  "min_withdrawal_amount": "0.000000000000000000"
}

```

*Details of the asset used in the product or contract.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier for the asset.|
|symbol|string|false|none|Symbol representing the asset.|
|precision|integer|false|none|Number of decimal places supported for the asset.|
|deposit_status|string|false|none|Indicates if deposits are enabled for the asset.|
|withdrawal_status|string|false|none|Indicates if withdrawals are enabled for the asset.|
|base_withdrawal_fee|string|false|none|Fixed withdrawal fee for the asset.|
|min_withdrawal_amount|string|false|none|Minimum allowable withdrawal amount for the asset.|

#### Enumerated Values

|Property|Value|
|---|---|
|deposit_status|enabled|
|deposit_status|disabled|
|withdrawal_status|enabled|
|withdrawal_status|disabled|

<h2 id="tocSarrayofassets">ArrayOfAssets</h2>

<a id="schemaarrayofassets"></a>

```json
[
  {
    "id": 14,
    "symbol": "USD",
    "precision": 8,
    "deposit_status": "enabled",
    "withdrawal_status": "enabled",
    "base_withdrawal_fee": "0.000000000000000000",
    "min_withdrawal_amount": "0.000000000000000000"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Asset](#schemaasset)]|false|none|[Details of the asset used in the product or contract.]|

<h2 id="tocSproduct">Product</h2>

<a id="schemaproduct"></a>

```json
{
  "id": 27,
  "symbol": "BTCUSD",
  "description": "Bitcoin Perpetual futures, quoted, settled & margined in INR",
  "created_at": "2023-12-18T13:10:39Z",
  "updated_at": "2024-11-15T02:47:50Z",
  "settlement_time": null,
  "notional_type": "vanilla",
  "impact_size": 10000,
  "initial_margin": "0.5",
  "maintenance_margin": "0.25",
  "contract_value": "0.001",
  "contract_unit_currency": "BTC",
  "tick_size": "0.5",
  "product_specs": {
    "funding_clamp_value": 0.05,
    "only_reduce_only_orders_allowed": false,
    "tags": [
      "layer_1"
    ]
  },
  "state": "live",
  "trading_status": "operational",
  "max_leverage_notional": "100000",
  "default_leverage": "200",
  "initial_margin_scaling_factor": "0.0000025",
  "maintenance_margin_scaling_factor": "0.00000125",
  "taker_commission_rate": "0.0005",
  "maker_commission_rate": "0.0002",
  "liquidation_penalty_factor": "0.5",
  "contract_type": "perpetual_futures",
  "position_size_limit": 229167,
  "basis_factor_max_limit": "10.95",
  "is_quanto": false,
  "funding_method": "mark_price",
  "annualized_funding": "10.95",
  "price_band": "2.5",
  "underlying_asset": {
    "id": 14,
    "symbol": "USD",
    "precision": 8,
    "deposit_status": "enabled",
    "withdrawal_status": "enabled",
    "base_withdrawal_fee": "0.000000000000000000",
    "min_withdrawal_amount": "0.000000000000000000"
  },
  "quoting_asset": {
    "id": 14,
    "symbol": "USD",
    "precision": 8,
    "deposit_status": "enabled",
    "withdrawal_status": "enabled",
    "base_withdrawal_fee": "0.000000000000000000",
    "min_withdrawal_amount": "0.000000000000000000"
  },
  "settling_asset": {
    "id": 14,
    "symbol": "USD",
    "precision": 8,
    "deposit_status": "enabled",
    "withdrawal_status": "enabled",
    "base_withdrawal_fee": "0.000000000000000000",
    "min_withdrawal_amount": "0.000000000000000000"
  },
  "spot_index": {
    "id": 14,
    "symbol": ".DEXBTUSD",
    "constituent_exchanges": [
      {
        "name": "ExchangeA",
        "weight": 0.25
      }
    ],
    "underlying_asset_id": 13,
    "quoting_asset_id": 14,
    "tick_size": "0.5",
    "index_type": "spot_pair"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier of a product or contract.|
|symbol|string|false|none|Symbol of the product or contract like BTCUSD, ETHUSD.|
|description|string|false|none|Detailed description of the product or contract.|
|created_at|string|false|none|Creation timestamp of the product or contract.|
|updated_at|string|false|none|Last update timestamp of the product or contract.|
|settlement_time|string|false|none|Settlement timestamp for futures contracts.|
|notional_type|string|false|none|Type of notional calculation.|
|impact_size|integer|false|none|Size of a typical trade used for mark price computation.|
|initial_margin|string|false|none|Margin required to open a position.|
|maintenance_margin|string|false|none|Minimum margin required to maintain a position.|
|contract_value|string|false|none|Notional value of the contract (spot price x contract amount).|
|contract_unit_currency|string|false|none|Unit of the contract (underlying asset or settling asset).|
|tick_size|string|false|none|Minimum price interval between two successive prices.|
|product_specs|[ProductSpecs](#schemaproductspecs)|false|none|Specifications related to the specific product or contract.|
|state|string|false|none|Current state of the product.|
|trading_status|string|false|none|Trading status of the contract.|
|max_leverage_notional|string|false|none|Maximum notional position size at the highest leverage.|
|default_leverage|string|false|none|Default leverage assigned to the product.|
|initial_margin_scaling_factor|string|false|none|Scaling factor for initial margin.|
|maintenance_margin_scaling_factor|string|false|none|Scaling factor for maintenance margin.|
|taker_commission_rate|string|false|none|Commission rate for taker trades.|
|maker_commission_rate|string|false|none|Commission rate for maker trades.|
|liquidation_penalty_factor|string|false|none|Factor used to calculate liquidation penalty.|
|contract_type|string|false|none|Type of contract (e.g., futures, perpetual).|
|position_size_limit|integer|false|none|Maximum size for a single contract order.|
|basis_factor_max_limit|string|false|none|Maximum value for annualized basis.|
|is_quanto|boolean|false|none|Indicates if the contract is quanto.|
|funding_method|string|false|none|Method used for funding calculation.|
|annualized_funding|string|false|none|Maximum allowed annualized funding rate.|
|price_band|string|false|none|Price range allowed around the mark price (percentage).|
|underlying_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|quoting_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|settling_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|spot_index|[Index](#schemaindex)|false|none|Details of an index used in trading, including its constituents and characteristics.|

#### Enumerated Values

|Property|Value|
|---|---|
|notional_type|vanilla|
|notional_type|inverse|
|state|live|
|state|expired|
|state|upcoming|
|trading_status|operational|
|trading_status|disrupted_cancel_only|
|trading_status|disrupted_post_only|

<h2 id="tocSproductcategories">ProductCategories</h2>

<a id="schemaproductcategories"></a>

```json
{
  "PutOptions": "string",
  "CallOptions": "string",
  "MoveOptions": "string",
  "Spot": "string",
  "Futures": "string",
  "Perpetual Futures": "string"
}

```

*List of all the product category names on delta exchange. Please refer to this list while subscribing to various public and private channels on delta exchange websocket*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PutOptions|string|false|none|put_options|
|CallOptions|string|false|none|call_options|
|MoveOptions|string|false|none|move_options|
|Spot|string|false|none|spot|
|Futures|string|false|none|futures|
|Perpetual Futures|string|false|none|perpetual_futures|

<h2 id="tocSarrayofproducts">ArrayOfProducts</h2>

<a id="schemaarrayofproducts"></a>

```json
[
  {
    "id": 27,
    "symbol": "BTCUSD",
    "description": "Bitcoin Perpetual futures, quoted, settled & margined in INR",
    "created_at": "2023-12-18T13:10:39Z",
    "updated_at": "2024-11-15T02:47:50Z",
    "settlement_time": null,
    "notional_type": "vanilla",
    "impact_size": 10000,
    "initial_margin": "0.5",
    "maintenance_margin": "0.25",
    "contract_value": "0.001",
    "contract_unit_currency": "BTC",
    "tick_size": "0.5",
    "product_specs": {
      "funding_clamp_value": 0.05,
      "only_reduce_only_orders_allowed": false,
      "tags": [
        "layer_1"
      ]
    },
    "state": "live",
    "trading_status": "operational",
    "max_leverage_notional": "100000",
    "default_leverage": "200",
    "initial_margin_scaling_factor": "0.0000025",
    "maintenance_margin_scaling_factor": "0.00000125",
    "taker_commission_rate": "0.0005",
    "maker_commission_rate": "0.0002",
    "liquidation_penalty_factor": "0.5",
    "contract_type": "perpetual_futures",
    "position_size_limit": 229167,
    "basis_factor_max_limit": "10.95",
    "is_quanto": false,
    "funding_method": "mark_price",
    "annualized_funding": "10.95",
    "price_band": "2.5",
    "underlying_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "quoting_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "settling_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "spot_index": {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Product](#schemaproduct)]|false|none|none|

<h2 id="tocSorder">Order</h2>

<a id="schemaorder"></a>

```json
{
  "id": 123,
  "user_id": 453671,
  "size": 10,
  "unfilled_size": 2,
  "side": "buy",
  "order_type": "limit_order",
  "limit_price": "59000",
  "stop_order_type": "stop_loss_order",
  "stop_price": "55000",
  "paid_commission": "0.5432",
  "commission": "0.5432",
  "reduce_only": false,
  "client_order_id": "34521712",
  "state": "open",
  "created_at": "1725865012000000",
  "product_id": 27,
  "product_symbol": "BTCUSD"
}

```

*An Order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|Genraeted order id|
|user_id|integer|false|none|Client id|
|size|integer|false|none|Order size|
|unfilled_size|integer|false|none|Order size which is not filled yet|
|side|string|false|none|Side for which to place order|
|order_type|string|false|none|Order type - limit_order/market_order|
|limit_price|string|false|none|Price level on which order must be triggered|
|stop_order_type|string|false|none|Stop order type - stop loss or take profit|
|stop_price|string|false|none|Stop price level for the stop order|
|paid_commission|string|false|none|Commission paid for filled order|
|commission|string|false|none|Commission blocked for order|
|reduce_only|string|false|none|if set, will only close positions. New orders will not be placed|
|client_order_id|string|false|none|client order id provided by the user while creating order|
|state|string|false|none|Order Status|
|created_at|string|false|none|Created at unix timestamp of the order in micro seconds|
|product_id|integer|false|none|Product id of the ordered product|
|product_symbol|string|false|none|Product symbol of the ordered product|

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|reduce_only|false|
|reduce_only|true|
|state|open|
|state|pending|
|state|closed|
|state|cancelled|

<h2 id="tocSarrayoforders">ArrayOfOrders</h2>

<a id="schemaarrayoforders"></a>

```json
[
  {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Order](#schemaorder)]|false|none|[An Order object]|

<h2 id="tocScreateorderrequest">CreateOrderRequest</h2>

<a id="schemacreateorderrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "stop_order_type": "stop_loss_order",
  "stop_price": "56000",
  "trail_amount": "50",
  "stop_trigger_method": "last_traded_price",
  "bracket_stop_loss_limit_price": "57000",
  "bracket_stop_loss_price": "56000",
  "bracket_trail_amount": "50",
  "bracket_take_profit_limit_price": "62000",
  "bracket_take_profit_price": "61000",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "reduce_only": false,
  "client_order_id": "34521712",
  "cancel_orders_accepted": false
}

```

*A create order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|Order size|
|side|string|true|none|Buy order or Sell order|
|order_type|string|true|none|Limit order(limit_price must be defined) or Market order|
|stop_order_type|string|false|none|Stop order type - stop loss or take profit|
|stop_price|string|false|none|Stop loss price level if the order is stop order|
|trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|
|stop_trigger_method|string|false|none|Stop order trigger method - mark_price/last_traded_price/spot_price|
|bracket_stop_loss_limit_price|string|false|none|Bracket order stop loss limit price|
|bracket_stop_loss_price|string|false|none|Bracket order stop loss trigger price|
|bracket_trail_amount|string|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|bracket_take_profit_limit_price|string|false|none|Bracket order take profit limit price|
|bracket_take_profit_price|string|false|none|take profit trigger price for bracket order|
|time_in_force|string|false|none|GTC/IOC order type|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|reduce_only|string|false|none|if set, will only close positions. New orders will not be placed|
|client_order_id|string|false|none|client order id provided by the user while creating order|
|cancel_orders_accepted|string|false|none|if set, will cancel all existing orders for the product|

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|stop_order_type|stop_loss_order|
|stop_order_type|take_profit_order|
|stop_trigger_method|mark_price|
|stop_trigger_method|last_traded_price|
|stop_trigger_method|spot_price|
|time_in_force|gtc|
|time_in_force|ioc|
|mmp|disabled|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|
|post_only|true|
|post_only|false|
|reduce_only|true|
|reduce_only|false|
|cancel_orders_accepted|true|
|cancel_orders_accepted|false|

<h2 id="tocSbatchcreateorder">BatchCreateOrder</h2>

<a id="schemabatchcreateorder"></a>

```json
{
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "client_order_id": "34521712"
}

```

*A create order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|Order size|
|side|string|true|none|Buy order or Sell order|
|order_type|string|true|none|Limit order(limit_price must be defined) or Market order|
|time_in_force|string|false|none|GTC/IOC order type|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|client_order_id|string|false|none|client order id provided by the user while creating order|

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|
|order_type|limit_order|
|order_type|market_order|
|time_in_force|gtc|
|time_in_force|ioc|
|mmp|disabled|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|
|post_only|true|
|post_only|false|

<h2 id="tocSbatchcreateordersrequest">BatchCreateOrdersRequest</h2>

<a id="schemabatchcreateordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "limit_price": "59000",
      "size": 10,
      "side": "buy",
      "order_type": "limit_order",
      "time_in_force": "gtc",
      "mmp": "disabled",
      "post_only": false,
      "client_order_id": "34521712"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchCreateOrder](#schemabatchcreateorder)]|false|none|[A create order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

<h2 id="tocSarrayofcreateorderrequest">ArrayOfCreateOrderRequest</h2>

<a id="schemaarrayofcreateorderrequest"></a>

```json
[
  {
    "product_id": 27,
    "product_symbol": "BTCUSD",
    "limit_price": "59000",
    "size": 10,
    "side": "buy",
    "order_type": "limit_order",
    "stop_order_type": "stop_loss_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "stop_trigger_method": "last_traded_price",
    "bracket_stop_loss_limit_price": "57000",
    "bracket_stop_loss_price": "56000",
    "bracket_trail_amount": "50",
    "bracket_take_profit_limit_price": "62000",
    "bracket_take_profit_price": "61000",
    "time_in_force": "gtc",
    "mmp": "disabled",
    "post_only": false,
    "reduce_only": false,
    "client_order_id": "34521712",
    "cancel_orders_accepted": false
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CreateOrderRequest](#schemacreateorderrequest)]|false|none|[A create order object]|

<h2 id="tocSeditorderrequest">EditOrderRequest</h2>

<a id="schemaeditorderrequest"></a>

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false,
  "cancel_orders_accepted": false,
  "stop_price": "56000",
  "trail_amount": "50"
}

```

*edit order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|existing order id to be edited|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|total size after editing order|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|cancel_orders_accepted|string|false|none|if set, will cancel all existing orders for the product|
|stop_price|string|false|none|price to trigger stop order|
|trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|

#### Enumerated Values

|Property|Value|
|---|---|
|mmp|disabled|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|
|post_only|true|
|post_only|false|
|cancel_orders_accepted|true|
|cancel_orders_accepted|false|

<h2 id="tocSbatcheditorder">BatchEditOrder</h2>

<a id="schemabatcheditorder"></a>

```json
{
  "id": 34521712,
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false
}

```

*edit order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|existing order id to be edited|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|total size after editing order|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|

#### Enumerated Values

|Property|Value|
|---|---|
|mmp|disabled|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|
|post_only|false|
|post_only|true|

<h2 id="tocSbatcheditordersrequest">BatchEditOrdersRequest</h2>

<a id="schemabatcheditordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 34521712,
      "limit_price": "59000",
      "size": 15,
      "mmp": "disabled",
      "post_only": false
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchEditOrder](#schemabatcheditorder)]|false|none|[edit order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

<h2 id="tocScreatebracketorderrequest">CreateBracketOrderRequest</h2>

<a id="schemacreatebracketorderrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "stop_loss_order": {
    "order_type": "limit_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "limit_price": "55000"
  },
  "take_profit_order": {
    "order_type": "limit_order",
    "stop_price": "65000",
    "limit_price": "64000"
  },
  "bracket_stop_trigger_method": "last_traded_price"
}

```

*bracket order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|stop_loss_order|object|false|none|none|
|» order_type|string|false|none|Limit order(limit_price must be defined) or Market order|
|» stop_price|string|false|none|Stop loss price level|
|» trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|
|» limit_price|string|false|none|required for limit orders|
|take_profit_order|object|false|none|none|
|» order_type|string|false|none|Limit order(limit_price must be defined) or Market order|
|» stop_price|string|false|none|Stop price level|
|» limit_price|string|false|none|required for limit orders|
|bracket_stop_trigger_method|string|false|none|stop order trigger method for bracket orders- mark_price/last_traded_price/spot_price|

#### Enumerated Values

|Property|Value|
|---|---|
|order_type|limit_order|
|order_type|market_order|
|order_type|limit_order|
|order_type|market_order|
|bracket_stop_trigger_method|mark_price|
|bracket_stop_trigger_method|last_traded_price|
|bracket_stop_trigger_method|spot_price|

<h2 id="tocSeditbracketorderrequest">EditBracketOrderRequest</h2>

<a id="schemaeditbracketorderrequest"></a>

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "bracket_stop_loss_limit_price": "55000",
  "bracket_stop_loss_price": "56000",
  "bracket_take_profit_limit_price": "65000",
  "bracket_take_profit_price": "64000",
  "bracket_trail_amount": "50",
  "bracket_stop_trigger_method": "last_traded_price"
}

```

*bracket order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|Order ID for which bracket params are being updated|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|bracket_stop_loss_limit_price|string|false|none|stop loss limit price for bracket order|
|bracket_stop_loss_price|string|false|none|stop loss trigger price for bracket order|
|bracket_take_profit_limit_price|string|false|none|take profit limit price for bracket order|
|bracket_take_profit_price|string|false|none|take profit trigger price for bracket order|
|bracket_trail_amount|string|false|none|trail amount of bracket order|
|bracket_stop_trigger_method|string|false|none|stop order trigger method for bracket orders- mark_price/last_traded_price/spot_price|

#### Enumerated Values

|Property|Value|
|---|---|
|bracket_stop_trigger_method|mark_price|
|bracket_stop_trigger_method|last_traded_price|
|bracket_stop_trigger_method|spot_price|

<h2 id="tocSbatchdeleteorder">BatchDeleteOrder</h2>

<a id="schemabatchdeleteorder"></a>

```json
{
  "id": 13452112,
  "client_order_id": "34521712"
}

```

*A delete order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|client_order_id|string|false|none|client order id provided by the user while creating order|

<h2 id="tocSdeleteorderrequest">DeleteOrderRequest</h2>

<a id="schemadeleteorderrequest"></a>

```json
{
  "id": 13452112,
  "client_order_id": "34521712",
  "product_id": 27
}

```

*A delete order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|client_order_id|string|false|none|client order id provided by the user while creating order|
|product_id|integer|false|none|product_id of the product in the order|

<h2 id="tocScancelallfilterobject">CancelAllFilterObject</h2>

<a id="schemacancelallfilterobject"></a>

```json
{
  "product_id": 27,
  "contract_types": "perpetual_futures,put_options,call_options",
  "cancel_limit_orders": false,
  "cancel_stop_orders": false,
  "cancel_reduce_only_orders": false
}

```

*Cancel all request filter object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|contract_types|string|false|none|comma separated list of desired contract types|
|cancel_limit_orders|string|false|none|set true to cancel open limit orders|
|cancel_stop_orders|string|false|none|set as true to cancel stop orders|
|cancel_reduce_only_orders|string|false|none|set as true to cancel reduce only orders|

#### Enumerated Values

|Property|Value|
|---|---|
|cancel_limit_orders|true|
|cancel_limit_orders|false|
|cancel_stop_orders|true|
|cancel_stop_orders|false|
|cancel_reduce_only_orders|true|
|cancel_reduce_only_orders|false|

<h2 id="tocSbatchdeleteordersrequest">BatchDeleteOrdersRequest</h2>

<a id="schemabatchdeleteordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 13452112,
      "client_order_id": "34521712"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchDeleteOrder](#schemabatchdeleteorder)]|false|none|[A delete order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

<h2 id="tocSposition">Position</h2>

<a id="schemaposition"></a>

```json
{
  "user_id": 0,
  "size": 0,
  "entry_price": "string",
  "margin": "string",
  "liquidation_price": "string",
  "bankruptcy_price": "string",
  "adl_level": 0,
  "product_id": 0,
  "product_symbol": "string",
  "commission": "string",
  "realized_pnl": "string",
  "realized_funding": "string"
}

```

*A position object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|integer|false|none|none|
|size|integer|false|none|Position size, negative for short and positive for long|
|entry_price|string|false|none|none|
|margin|string|false|none|none|
|liquidation_price|string|false|none|none|
|bankruptcy_price|string|false|none|none|
|adl_level|integer|false|none|none|
|product_id|integer|false|none|none|
|product_symbol|string|false|none|none|
|commission|string|false|none|commissions blocked in the position|
|realized_pnl|string|false|none|Net realized pnl since the position was opened|
|realized_funding|string|false|none|Net realized funding since the position was opened|

<h2 id="tocSarrayofpositions">ArrayOfPositions</h2>

<a id="schemaarrayofpositions"></a>

```json
[
  {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Position](#schemaposition)]|false|none|[A position object]|

<h2 id="tocSfill">Fill</h2>

<a id="schemafill"></a>

```json
{
  "id": 0,
  "size": 0,
  "fill_type": "normal",
  "side": "buy",
  "price": "string",
  "role": "taker",
  "commission": "string",
  "created_at": "string",
  "product_id": 0,
  "product_symbol": "string",
  "order_id": "string",
  "settling_asset_id": 0,
  "settling_asset_symbol": "string",
  "meta_data": {
    "commission_deto": "string",
    "commission_deto_in_settling_asset": "string",
    "effective_commission_rate": "string",
    "liquidation_fee_deto": "string",
    "liquidation_fee_deto_in_settling_asset": "string",
    "order_price": "string",
    "order_size": "string",
    "order_type": "string",
    "order_unfilled_size": "string",
    "tfc_used_for_commission": "string",
    "tfc_used_for_liquidation_fee": "string",
    "total_commission_in_settling_asset": "string",
    "total_liquidation_fee_in_settling_asset": "string"
  }
}

```

*A fill object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|size|integer|false|none|none|
|fill_type|string|false|none|none|
|side|string|false|none|none|
|price|string|false|none|Price at which the fill happened, BigDecimal sent as string|
|role|string|false|none|none|
|commission|string|false|none|Commission paid on this fill, negative value means commission was earned because of maker role|
|created_at|string|false|none|none|
|product_id|integer|false|none|none|
|product_symbol|string|false|none|none|
|order_id|string|false|none|Will be order_id(Integer) in most cases. Will be UUID string of order when fill_type is settlement|
|settling_asset_id|integer|false|none|none|
|settling_asset_symbol|string|false|none|none|
|meta_data|[FillMetaData](#schemafillmetadata)|false|none|Meta data inside fill|

#### Enumerated Values

|Property|Value|
|---|---|
|fill_type|normal|
|fill_type|adl|
|fill_type|liquidation|
|fill_type|settlement|
|fill_type|otc|
|side|buy|
|side|sell|
|role|taker|
|role|maker|

<h2 id="tocSarrayoffills">ArrayOfFills</h2>

<a id="schemaarrayoffills"></a>

```json
[
  {
    "id": 0,
    "size": 0,
    "fill_type": "normal",
    "side": "buy",
    "price": "string",
    "role": "taker",
    "commission": "string",
    "created_at": "string",
    "product_id": 0,
    "product_symbol": "string",
    "order_id": "string",
    "settling_asset_id": 0,
    "settling_asset_symbol": "string",
    "meta_data": {
      "commission_deto": "string",
      "commission_deto_in_settling_asset": "string",
      "effective_commission_rate": "string",
      "liquidation_fee_deto": "string",
      "liquidation_fee_deto_in_settling_asset": "string",
      "order_price": "string",
      "order_size": "string",
      "order_type": "string",
      "order_unfilled_size": "string",
      "tfc_used_for_commission": "string",
      "tfc_used_for_liquidation_fee": "string",
      "total_commission_in_settling_asset": "string",
      "total_liquidation_fee_in_settling_asset": "string"
    }
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Fill](#schemafill)]|false|none|[A fill object]|

<h2 id="tocSfillmetadata">FillMetaData</h2>

<a id="schemafillmetadata"></a>

```json
{
  "commission_deto": "string",
  "commission_deto_in_settling_asset": "string",
  "effective_commission_rate": "string",
  "liquidation_fee_deto": "string",
  "liquidation_fee_deto_in_settling_asset": "string",
  "order_price": "string",
  "order_size": "string",
  "order_type": "string",
  "order_unfilled_size": "string",
  "tfc_used_for_commission": "string",
  "tfc_used_for_liquidation_fee": "string",
  "total_commission_in_settling_asset": "string",
  "total_liquidation_fee_in_settling_asset": "string"
}

```

*Meta data inside fill*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|commission_deto|string|false|none|none|
|commission_deto_in_settling_asset|string|false|none|none|
|effective_commission_rate|string|false|none|none|
|liquidation_fee_deto|string|false|none|none|
|liquidation_fee_deto_in_settling_asset|string|false|none|none|
|order_price|string|false|none|none|
|order_size|string|false|none|none|
|order_type|string|false|none|none|
|order_unfilled_size|string|false|none|none|
|tfc_used_for_commission|string|false|none|none|
|tfc_used_for_liquidation_fee|string|false|none|none|
|total_commission_in_settling_asset|string|false|none|none|
|total_liquidation_fee_in_settling_asset|string|false|none|none|

<h2 id="tocSorderleverage">OrderLeverage</h2>

<a id="schemaorderleverage"></a>

```json
{
  "leverage": 10,
  "order_margin": "563.2",
  "product_id": 27
}

```

*Order Leverage for a product*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|leverage|string|false|none|Leverage of all open orders for this product|
|order_margin|string|false|none|Margin blocked in open orders for this product|
|product_id|integer|false|none|Product id of the ordered product|

<h2 id="tocSl2orderbook">L2Orderbook</h2>

<a id="schemal2orderbook"></a>

```json
{
  "buy": [
    {
      "depth": "983",
      "price": "9187.5",
      "size": 205640
    }
  ],
  "last_updated_at": 1654589595784000,
  "sell": [
    {
      "depth": "1185",
      "price": "9188.0",
      "size": 113752
    }
  ],
  "symbol": "BTCUSD"
}

```

*L2 orderbook*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|buy|[object]|false|none|none|
|» depth|string|false|none|sum of size till that price level|
|» price|string|false|none|none|
|» size|integer|false|none|for derivatives -> number of contracts, for spot -> amount in underlying|
|last_updated_at|integer|false|none|none|
|sell|[object]|false|none|none|
|» depth|string|false|none|sum of size till that price level|
|» price|string|false|none|none|
|» size|integer|false|none|for derivatives -> number of contracts, for spot -> amount in underlying|
|symbol|string|false|none|none|

<h2 id="tocStrades">Trades</h2>

<a id="schematrades"></a>

```json
{
  "trades": [
    {
      "side": "buy",
      "size": 0,
      "price": "string",
      "timestamp": 0
    }
  ]
}

```

*trades of a symbol*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|trades|[object]|false|none|none|
|» side|string|false|none|none|
|» size|integer|false|none|none|
|» price|string|false|none|none|
|» timestamp|integer|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|side|buy|
|side|sell|

<h2 id="tocSwallet">Wallet</h2>

<a id="schemawallet"></a>

```json
{
  "asset_id": 0,
  "asset_symbol": "string",
  "available_balance": "string",
  "available_balance_for_robo": "string",
  "balance": "string",
  "blocked_margin": "string",
  "commission": "string",
  "cross_asset_liability": "string",
  "cross_commission": "string",
  "cross_locked_collateral": "string",
  "cross_order_margin": "string",
  "cross_position_margin": "string",
  "id": 0,
  "interest_credit": "string",
  "order_margin": "string",
  "pending_referral_bonus": "string",
  "pending_trading_fee_credit": "string",
  "portfolio_margin": "string",
  "position_margin": "string",
  "trading_fee_credit": "string",
  "unvested_amount": "string",
  "user_id": 0
}

```

*Wallet Data for each asset.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset_id|integer|false|none|Id for assets like BTC|
|asset_symbol|string|false|none|Symbol for assets like BTC|
|available_balance|string|false|none|Balance available for trading|
|available_balance_for_robo|string|false|none|Balance available for robo trading|
|balance|string|false|none|Total wallet balance|
|blocked_margin|string|false|none|Total blocked margin including commissions for all modes|
|commission|string|false|none|Commissions blocked in Isolated Mode|
|cross_asset_liability|string|false|none|Asset liability in Cross margin mode|
|cross_commission|string|false|none|Commision blocked in Cross margin mode|
|cross_locked_collateral|string|false|none|collateral blocked in Cross margin mode|
|cross_order_margin|string|false|none|margin blocked for open orders in Cross margin mode|
|cross_position_margin|string|false|none|margin blocked for open positions in Cross margin mode|
|id|integer|false|none|Wallet Id|
|interest_credit|string|false|none|Total interest credited|
|order_margin|string|false|none|margin blocked for open positions in isolated mode|
|pending_referral_bonus|string|false|none|Pending referral bonus|
|pending_trading_fee_credit|string|false|none|Credit of trading fee pending|
|portfolio_margin|string|false|none|Total margin blocked including commissions in portfolio margin mode|
|position_margin|string|false|none|Margin blocked in open positions in isolated mode|
|trading_fee_credit|string|false|none|Credit of trading fee|
|unvested_amount|string|false|none|Amount currently unvested|
|user_id|integer|false|none|User Id linked to this wallet|

<h2 id="tocSwalletpayload">WalletPayload</h2>

<a id="schemawalletpayload"></a>

```json
{
  "meta": {
    "net_equity": "string",
    "robo_trading_equity": "string"
  },
  "result": [
    {
      "asset_id": 0,
      "asset_symbol": "string",
      "available_balance": "string",
      "available_balance_for_robo": "string",
      "balance": "string",
      "blocked_margin": "string",
      "commission": "string",
      "cross_asset_liability": "string",
      "cross_commission": "string",
      "cross_locked_collateral": "string",
      "cross_order_margin": "string",
      "cross_position_margin": "string",
      "id": 0,
      "interest_credit": "string",
      "order_margin": "string",
      "pending_referral_bonus": "string",
      "pending_trading_fee_credit": "string",
      "portfolio_margin": "string",
      "position_margin": "string",
      "trading_fee_credit": "string",
      "unvested_amount": "string",
      "user_id": 0
    }
  ],
  "success": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|meta|[WalletMetaData](#schemawalletmetadata)|false|none|Meta data for robo trading|
|result|[ArrayOfWallets](#schemaarrayofwallets)|false|none|Array of wallet for every asset|
|success|boolean|false|none|none|

<h2 id="tocSwalletmetadata">WalletMetaData</h2>

<a id="schemawalletmetadata"></a>

```json
{
  "net_equity": "string",
  "robo_trading_equity": "string"
}

```

*Meta data for robo trading*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|net_equity|string|false|none|Net equity for robo trading|
|robo_trading_equity|string|false|none|trading equity for robo trading|

<h2 id="tocSarrayofwallets">ArrayOfWallets</h2>

<a id="schemaarrayofwallets"></a>

```json
[
  {
    "asset_id": 0,
    "asset_symbol": "string",
    "available_balance": "string",
    "available_balance_for_robo": "string",
    "balance": "string",
    "blocked_margin": "string",
    "commission": "string",
    "cross_asset_liability": "string",
    "cross_commission": "string",
    "cross_locked_collateral": "string",
    "cross_order_margin": "string",
    "cross_position_margin": "string",
    "id": 0,
    "interest_credit": "string",
    "order_margin": "string",
    "pending_referral_bonus": "string",
    "pending_trading_fee_credit": "string",
    "portfolio_margin": "string",
    "position_margin": "string",
    "trading_fee_credit": "string",
    "unvested_amount": "string",
    "user_id": 0
  }
]

```

*Array of wallet for every asset*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Wallet](#schemawallet)]|false|none|Array of wallet for every asset|

<h2 id="tocSassettransfersubaccountreq">AssetTransferSubaccountReq</h2>

<a id="schemaassettransfersubaccountreq"></a>

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transferrer_user_id|string|false|none|Debit account|
|transferee_user_id|string|false|none|Credit account|
|asset_symbol|string|false|none|Asset to transfer|
|amount|big_decimal|false|none|Amount to transfer. Only postive values allowed.|

<h2 id="tocSsubaccounttransferhistory">SubaccountTransferHistory</h2>

<a id="schemasubaccounttransferhistory"></a>

```json
{
  "subaccount_user_id": "string",
  "before": "string",
  "after": "string",
  "page_size": 10
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subaccount_user_id|string|false|none|subaccount user id|
|before|string|false|none|before cursor for pagination|
|after|string|false|none|after cursor for pagination|
|page_size|big_decimal|false|none|records per page|

<h2 id="tocStransactiontypes">TransactionTypes</h2>

<a id="schematransactiontypes"></a>

```json
"string"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|
|transaction_type|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|transaction_type|cashflow|
|transaction_type|deposit|
|transaction_type|withdrawal|
|transaction_type|commission|
|transaction_type|conversion|
|transaction_type|funding|
|transaction_type|settlement|
|transaction_type|liquidation_fee|
|transaction_type|spot_trade|
|transaction_type|withdrawal_cancellation|
|transaction_type|referral_bonus|
|transaction_type|sub_account_transfer|
|transaction_type|commission_rebate|
|transaction_type|promo_credit|
|transaction_type|trading_credits|
|transaction_type|trading_credits_forfeited|
|transaction_type|trading_credits_paid|
|transaction_type|trading_fee_credits_paid_liquidation_fee|
|transaction_type|trading_credits_reverted|
|transaction_type|interest_credit|
|transaction_type|external_deposit|
|transaction_type|credit_line|
|transaction_type|trading_competition|
|transaction_type|fund_deposit|
|transaction_type|fund_withdrawal|
|transaction_type|fund_wallet_deposit|
|transaction_type|fund_wallet_withdrawal|
|transaction_type|fund_reward|
|transaction_type|trade_farming_reward|
|transaction_type|interest_credit|
|transaction_type|revert|
|transaction_type|raf_bonus|
|transaction_type|fill_appropriation|
|transaction_type|incident_compensation|

<h2 id="tocStransaction">Transaction</h2>

<a id="schematransaction"></a>

```json
{
  "id": 0,
  "amount": "string",
  "balance": "string",
  "transaction_type": "string",
  "meta_data": {},
  "product_id": 0,
  "asset_id": 0,
  "asset_symbol": 0,
  "created_at": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|amount|string|false|none|amount credited/debited in this transaction (+ for credited, - for debited)|
|balance|string|false|none|net wallet balance after this transaction|
|transaction_type|[TransactionTypes](#schematransactiontypes)|false|none|none|
|meta_data|object|false|none|none|
|product_id|integer|false|none|none|
|asset_id|integer|false|none|none|
|asset_symbol|integer|false|none|none|
|created_at|string|false|none|none|

<h2 id="tocSarrayoftransactions">ArrayOfTransactions</h2>

<a id="schemaarrayoftransactions"></a>

```json
[
  {
    "id": 0,
    "amount": "string",
    "balance": "string",
    "transaction_type": "string",
    "meta_data": {},
    "product_id": 0,
    "asset_id": 0,
    "asset_symbol": 0,
    "created_at": "string"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Transaction](#schematransaction)]|false|none|none|

<h2 id="tocSsubaccounttransferlog">SubaccountTransferLog</h2>

<a id="schemasubaccounttransferlog"></a>

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null,
  "created_at": "string",
  "transferee_user": {},
  "transferrer_user": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transferrer_user_id|string|false|none|User id of the account debited with the asset.|
|transferee_user_id|string|false|none|User id of the account credited with the asset.|
|asset_symbol|string|false|none|Asset symbol transferred.|
|amount|big_decimal|false|none|Amount transferred.|
|created_at|string|false|none|transfer creation date and time|
|transferee_user|object|false|none|User details|
|transferrer_user|object|false|none|User details|

<h2 id="tocSarrayofsubaccounttransferlog">ArrayOfSubaccountTransferLog</h2>

<a id="schemaarrayofsubaccounttransferlog"></a>

```json
[
  {
    "transferrer_user_id": "string",
    "transferee_user_id": "string",
    "asset_symbol": "string",
    "amount": null,
    "created_at": "string",
    "transferee_user": {},
    "transferrer_user": {}
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SubaccountTransferLog](#schemasubaccounttransferlog)]|false|none|none|

<h2 id="tocSgreeks">greeks</h2>

<a id="schemagreeks"></a>

```json
{
  "delta": "0.25",
  "gamma": "0.10",
  "rho": "0.05",
  "theta": "-0.02",
  "vega": "0.15"
}

```

*The Greeks represent different factors that influence the pricing of options. These are key measures for assessing risk and managing option positions.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|delta|string|false|none|The rate of change of the option price with respect to changes in the underlying asset price. A measure of sensitivity to the asset price movement.|
|gamma|string|false|none|The rate of change of delta with respect to changes in the underlying asset price. A measure of the curvature of the option’s price sensitivity to the asset price.|
|rho|string|false|none|The rate of change of the option price with respect to changes in the risk-free interest rate. A measure of interest rate sensitivity.|
|theta|string|false|none|The rate of change of the option price with respect to time, often referred to as time decay. A measure of how the option's price declines as expiration approaches.|
|vega|string|false|none|The rate of change of the option price with respect to changes in the volatility of the underlying asset. A measure of volatility sensitivity.|

<h2 id="tocSprice_band">price_band</h2>

<a id="schemaprice_band"></a>

```json
{
  "lower_limit": "61120.45",
  "upper_limit": "72300.00"
}

```

*The price band defines the permissible price range for a product. The lower and upper limits represent the boundaries within which the product's price can fluctuate.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lower_limit|string|false|none|The minimum price limit for the product. It defines the lowest allowable price before triggering a price band constraint.|
|upper_limit|string|false|none|The maximum price limit for the product. It defines the highest allowable price before triggering a price band constraint.|

<h2 id="tocSquotes">quotes</h2>

<a id="schemaquotes"></a>

```json
{
  "ask_iv": "0.25",
  "ask_size": "100",
  "best_ask": "150.00",
  "best_bid": "148.00",
  "bid_iv": "0.22",
  "bid_size": "50"
}

```

*The 'quotes' object contains the latest bid and ask prices, their respective implied volatilities (IV), and order sizes for an asset. It provides key market data for understanding liquidity and pricing.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ask_iv|string|false|none|The implied volatility (IV) for the ask price. Represents the market's expectation of the future volatility of the underlying asset.|
|ask_size|string|false|none|The size of the ask order, representing the quantity of the asset available for sale at the ask price.|
|best_ask|string|false|none|The best (lowest) ask price available in the market for the asset.|
|best_bid|string|false|none|The best (highest) bid price available in the market for the asset.|
|bid_iv|string|false|none|The implied volatility (IV) for the bid price. Represents the market's expectation of future volatility for the bid side of the order book.|
|bid_size|string|false|none|The size of the bid order, representing the quantity of the asset that buyers are willing to purchase at the bid price.|

<h2 id="tocSticker">Ticker</h2>

<a id="schematicker"></a>

```json
{
  "close": 67321,
  "contract_type": "futures",
  "greeks": {
    "delta": "0.25",
    "gamma": "0.10",
    "rho": "0.05",
    "theta": "-0.02",
    "vega": "0.15"
  },
  "high": 68500.5,
  "low": 66300.25,
  "mark_price": "67000.00",
  "mark_vol": "500",
  "oi": "15000",
  "oi_value": "1000000",
  "oi_value_symbol": "USD",
  "oi_value_usd": "1050000",
  "open": 67000,
  "price_band": {
    "lower_limit": "61120.45",
    "upper_limit": "72300.00"
  },
  "product_id": 123456,
  "quotes": {
    "ask_iv": "0.25",
    "ask_size": "100",
    "best_ask": "150.00",
    "best_bid": "148.00",
    "bid_iv": "0.22",
    "bid_size": "50"
  },
  "size": 100,
  "spot_price": "67000.00",
  "strike_price": "68000.00",
  "symbol": "BTCUSD",
  "timestamp": 1609459200,
  "turnover": 5000000,
  "turnover_symbol": "USD",
  "turnover_usd": 5200000,
  "volume": 25000
}

```

*The 'Ticker' object provides real-time trading data for a specific product, including prices, volumes, open interest, and Greek values (for options). This data is essential for analyzing market trends and asset performance.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|close|integer|false|none|The closing price of the last trade for the product.|
|contract_type|string|false|none|Comma-separated list of contract types, such as futures, perpetual_futures, call_options, put_options.|
|greeks|[greeks](#schemagreeks)|false|none|The Greeks represent different factors that influence the pricing of options. These are key measures for assessing risk and managing option positions.|
|high|number|false|none|The highest price reached during the trading session.|
|low|number|false|none|The lowest price reached during the trading session.|
|mark_price|string|false|none|The market price of the product, reflecting the most recent transaction.|
|mark_vol|string|false|none|The market volume at the most recent trade price.|
|oi|string|false|none|The open interest, or the number of outstanding contracts, for the product.|
|oi_value|string|false|none|The value of the open interest in the base currency.|
|oi_value_symbol|string|false|none|The symbol representing the currency of the open interest value.|
|oi_value_usd|string|false|none|The open interest value converted to USD.|
|open|number|false|none|The opening price at the start of the trading session.|
|price_band|[price_band](#schemaprice_band)|false|none|The price band defines the permissible price range for a product. The lower and upper limits represent the boundaries within which the product's price can fluctuate.|
|product_id|number|false|none|A unique identifier for the product.|
|quotes|[quotes](#schemaquotes)|false|none|The 'quotes' object contains the latest bid and ask prices, their respective implied volatilities (IV), and order sizes for an asset. It provides key market data for understanding liquidity and pricing.|
|size|number|false|none|The size of the most recent order executed in the market.|
|spot_price|string|false|none|The current spot price of the underlying asset.|
|strike_price|string|false|none|The strike price for options contracts associated with the product.|
|symbol|string|false|none|The ticker symbol for the product.|
|timestamp|number|false|none|The timestamp of the last trade or update to the ticker.|
|turnover|number|false|none|The total turnover (value traded) for the product during the trading session.|
|turnover_symbol|string|false|none|The symbol representing the currency in which the turnover is measured.|
|turnover_usd|number|false|none|The turnover value converted to USD.|
|volume|integer|false|none|The total trading volume for the product during the trading session.|

<h2 id="tocSarrayoftickers">ArrayOfTickers</h2>

<a id="schemaarrayoftickers"></a>

```json
[
  {
    "close": 67321,
    "contract_type": "futures",
    "greeks": {
      "delta": "0.25",
      "gamma": "0.10",
      "rho": "0.05",
      "theta": "-0.02",
      "vega": "0.15"
    },
    "high": 68500.5,
    "low": 66300.25,
    "mark_price": "67000.00",
    "mark_vol": "500",
    "oi": "15000",
    "oi_value": "1000000",
    "oi_value_symbol": "USD",
    "oi_value_usd": "1050000",
    "open": 67000,
    "price_band": {
      "lower_limit": "61120.45",
      "upper_limit": "72300.00"
    },
    "product_id": 123456,
    "quotes": {
      "ask_iv": "0.25",
      "ask_size": "100",
      "best_ask": "150.00",
      "best_bid": "148.00",
      "bid_iv": "0.22",
      "bid_size": "50"
    },
    "size": 100,
    "spot_price": "67000.00",
    "strike_price": "68000.00",
    "symbol": "BTCUSD",
    "timestamp": 1609459200,
    "turnover": 5000000,
    "turnover_symbol": "USD",
    "turnover_usd": 5200000,
    "volume": 25000
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Ticker](#schematicker)]|false|none|[The 'Ticker' object provides real-time trading data for a specific product, including prices, volumes, open interest, and Greek values (for options). This data is essential for analyzing market trends and asset performance.]|

<h2 id="tocSpaginationmeta">PaginationMeta</h2>

<a id="schemapaginationmeta"></a>

```json
{
  "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
  "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|after|string|false|none|after cursor for pagination; becomes null if page after the current one does not exist|
|before|string|false|none|before cursor for pagination; becomes null if page before the current one does not exist|

<h2 id="tocSohlcdata">OHLCData</h2>

<a id="schemaohlcdata"></a>

```json
{
  "time": 0,
  "open": 0,
  "high": 0,
  "low": 0,
  "close": 0,
  "volume": 0
}

```

*A ohlc object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|time|integer|false|none|none|
|open|number|false|none|none|
|high|number|false|none|none|
|low|number|false|none|none|
|close|number|false|none|none|
|volume|number|false|none|none|

<h2 id="tocSarrayofohlcdata">ArrayOfOHLCData</h2>

<a id="schemaarrayofohlcdata"></a>

```json
[
  {
    "time": 0,
    "open": 0,
    "high": 0,
    "low": 0,
    "close": 0,
    "volume": 0
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[OHLCData](#schemaohlcdata)]|false|none|[A ohlc object]|

<h2 id="tocSsparklinedata">SparklineData</h2>

<a id="schemasparklinedata"></a>

```json
{
  "ETHUSD": [
    [
      1594214051,
      0.00003826
    ],
    [
      1594214051,
      0.00003826
    ]
  ],
  "MARK:BTCUSD": [
    [
      1594215270,
      0.00003826
    ]
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[integer]|false|none|array of timestamp and closing value|

<h2 id="tocSstats">Stats</h2>

<a id="schemastats"></a>

```json
{
  "last_30_days_volume": 0,
  "last_7_days_volume": 0,
  "total_volume": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|last_30_days_volume|integer|false|none|sum of turnover usd in the last 30 days|
|last_7_days_volume|integer|false|none|sum of turnover usd in the last 7 days|
|total_volume|integer|false|none|sum of turnover usd in the last 24 hours|

<h2 id="tocSmmpconfigupdaterequest">MMPConfigUpdateRequest</h2>

<a id="schemammpconfigupdaterequest"></a>

```json
{
  "asset": "string",
  "window_interval": 0,
  "freeze_interval": 0,
  "trade_limit": "string",
  "delta_limit": "string",
  "vega_limit": "string",
  "mmp": "mmp1"
}

```

*MMP config for an underlying*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|false|none|none|
|window_interval|integer|false|none|Window interval in seconds|
|freeze_interval|integer|false|none|MMP freeze interval in seconds. Setting this to zero will require a manual reset once mmp is triggered.|
|trade_limit|string|false|none|Notional trade limit for mmp to trigger (in USD)|
|delta_limit|string|false|none|Delta Adjusted notional trade limit for mmp to trigger (in USD)|
|vega_limit|string|false|none|vega traded limit for mmp to trigger (in USD)|
|mmp|string|false|none|Specify mmp flag for the config update|

#### Enumerated Values

|Property|Value|
|---|---|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|

<h2 id="tocSmmpresetrequest">MMPResetRequest</h2>

<a id="schemammpresetrequest"></a>

```json
{
  "asset": "string",
  "mmp": "mmp1"
}

```

*MMP config for an underlying*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|false|none|none|
|mmp|string|false|none|specify mmp flag to reset|

#### Enumerated Values

|Property|Value|
|---|---|
|mmp|mmp1|
|mmp|mmp2|
|mmp|mmp3|
|mmp|mmp4|
|mmp|mmp5|

<h2 id="tocSchangemarginmoderequest">ChangeMarginModeRequest</h2>

<a id="schemachangemarginmoderequest"></a>

```json
{
  "margin_mode": "isolated",
  "subaccount_user_id": "5112346"
}

```

*Request to change the margin mode for a main or subaccount.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_mode|string|false|none|The target margin mode: 'isolated' or 'portfolio'.|
|subaccount_user_id|string|false|none|The user ID of the account. Provide the main user ID for the main account or the respective subaccount user ID.|

#### Enumerated Values

|Property|Value|
|---|---|
|margin_mode|isolated|
|margin_mode|portfolio|

<h2 id="tocSuserpreference">UserPreference</h2>

<a id="schemauserpreference"></a>

```json
{
  "user_id": 57354187,
  "default_auto_topup": true,
  "mmp_config": null,
  "deto_for_commission": false,
  "vip_level": 0,
  "vip_discount_factor": "0.00",
  "volume_30d": "1060.675333",
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "margin_topup": false,
    "marketing": true,
    "order_cancel": true,
    "order_fill": true,
    "stop_order_trigger": true
  },
  "notification_preferences": {
    "adl": true,
    "liquidation": true,
    "margin_topup": false,
    "marketing": true,
    "order_cancel": false,
    "order_fill": true,
    "price_alert": true,
    "stop_order_trigger": true
  },
  "price_alert_assets": [
    "BTC",
    "ETH"
  ],
  "enabled_portfolios": {},
  "interest_credit": false
}

```

*User trading preferences*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|integer|false|none|Unique identifier for the user|
|default_auto_topup|boolean|false|none|Default auto top-up setting for newly acquired positions (only for isolated mode)|
|mmp_config|object¦null|false|none|Config object for market maker protection (only for MMP-enabled accounts)|
|deto_for_commission|boolean|false|none|Flag to determine whether to pay commissions in DETO|
|vip_level|integer|false|none|VIP level for this account. Customers get better fee discounting for higher VIP levels|
|vip_discount_factor|string|false|none|Discount factor based on the VIP level|
|volume_30d|string|false|none|30-day trading volume for the user|
|email_preferences|object|false|none|Email preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» margin_topup|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|notification_preferences|object|false|none|Notification preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» margin_topup|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» price_alert|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|price_alert_assets|[string]|false|none|Assets for which price alerts are set|
|enabled_portfolios|object|false|none|Enabled portfolios for the user|
|interest_credit|boolean|false|none|Whether the user is receiving interest credits|

<h2 id="tocSedituserpreference">EditUserPreference</h2>

<a id="schemaedituserpreference"></a>

```json
{
  "default_auto_topup": true,
  "showMarketOrdersForOptionsInBracket": true,
  "interest_credit": false,
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "order_cancel": true,
    "marketing": true
  },
  "notification_preferences": {
    "adl": false,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "price_alert": true,
    "marketing": true
  }
}

```

*Edit User Preference Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|default_auto_topup|boolean|false|none|Default auto top-up setting for newly acquired positions|
|showMarketOrdersForOptionsInBracket|boolean|false|none|Flag to display market orders for options in bracket orders|
|interest_credit|boolean|false|none|Whether the user is receiving interest credits|
|email_preferences|object|false|none|Email preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|notification_preferences|object|false|none|Notification preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|» price_alert|boolean|false|none|none|
|» marketing|boolean|false|none|none|

<!-- <h2 id="tocScancelafterrequest">CancelAfterRequest</h2>

<a id="schemacancelafterrequest"></a>

```json
{
  "cancel_after": "5000"
}

```

*Cancel After Request Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancel_after|string|false|none|Timer value in milliseconds after which orders are to be cancelled. To disable deadman switch and keep your orders open, set cancel_after to 0.|

<h2 id="tocScancelafterresponse">CancelAfterResponse</h2>

<a id="schemacancelafterresponse"></a>

```json
{
  "cancel_after_enabled": "true",
  "cancel_after_timestamp": "1669119262000"
}

```

*Cancel After Response Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancel_after_enabled|string|false|none|none|
|cancel_after_timestamp|string|false|none|timestamp after which orders will get cancelled|

#### Enumerated Values

|Property|Value|
|---|---|
|cancel_after_enabled|false|
|cancel_after_enabled|true| -->

<h2 id="tocSuser">User</h2>

<a id="schemauser"></a>

```json
{
  "id": "98765432",
  "email": "rajtrader2342@gmail.com",
  "account_name": "Main",
  "first_name": "Rajesh",
  "last_name": "Sharma",
  "dob": "1985-08-25",
  "country": "India",
  "phone_number": "9876543210",
  "margin_mode": "isolated",
  "pf_index_symbol": ".DEXBTUSD",
  "is_sub_account": false,
  "is_kyc_done": true
}

```

*Represents a user account with personal and account-related details.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|Unique user identifier, which can be an integer or string.|
|email|string|false|none|User's email address.|
|account_name|string|false|none|The main account or subaccount name.|
|first_name|string|false|none|User's first name.|
|last_name|string|false|none|User's last name.|
|dob|string(date)|false|none|Date of birth in YYYY-MM-DD format.|
|country|string|false|none|User's country of residence.|
|phone_number|string|false|none|User's phone number with country code.|
|margin_mode|string|false|none|The user's margin mode, which can be 'isolated' or 'portfolio'.|
|pf_index_symbol|string|false|none|Portfolio index symbol if the account is in portfolio margin mode.|
|is_sub_account|boolean|false|none|Indicates if the user account is a sub-account.|
|is_kyc_done|boolean|false|none|Indicates if the user's KYC verification is completed.|

<h2 id="tocSarrayofsubaccouns">ArrayOfSubaccouns</h2>

<a id="schemaarrayofsubaccouns"></a>

```json
[
  {
    "id": "98765432",
    "email": "rajtrader2342@gmail.com",
    "account_name": "Main",
    "first_name": "Rajesh",
    "last_name": "Sharma",
    "dob": "1985-08-25",
    "country": "India",
    "phone_number": "9876543210",
    "margin_mode": "isolated",
    "pf_index_symbol": ".DEXBTUSD",
    "is_sub_account": false,
    "is_kyc_done": true
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[User](#schemauser)]|false|none|[Represents a user account with personal and account-related details.]|

# Websocket Feed

Websocket api can be used for the following use cases

- Get real time feed of market data, this includes L2 orderbook and recent trades.
- Get price feeds - Mark prices of different contracts, price feed of underlying indexes etc.
- Get account specific notifications like fills, liquidations, [ADL](https://www.delta.exchange/user-guide/docs/trading-guide/ADL/) and PnL updates.
- Get account specific updates on orders, positions and wallets.

Websocket url for [Delta Exchange](https://www.delta.exchange)

- **Production** - wss://socket.india.delta.exchange
- **Testnet(Demo Account)** - wss://socket-ind.testnet.deltaex.org

There is a limit of 150 connections every 5 minutes per IP address. A connection attempt that goes beyond the limit will be disconnected with 429 HTTP status error. On receiving this error, wait for 5 to 10 minutes before making new connection requests.

You will be disconnected, if there is no activity within **60 seconds** after making connection.

# Subscribing to Channels

## Subscribe

To begin receiving feed messages, you must first send a subscribe message to the server indicating which channels and contracts to subscribe for.

To specify contracts within each channel, just pass a list of symbols inside the channel payload. Mention ***["all"]*** in symbols if you want to receive updates across all the contracts. Please note that snapshots are sent only for specified symbols,meaning no snapshots are sent for symbol: ***"all"***.

Once a subscribe message is received the server will respond with a subscriptions message that lists all channels you are subscribed to. Subsequent subscribe messages will add to the list of subscriptions. 

> Subscription Sample

```json
// Request: Subscribe to BTCUSD and ETHUSD with the ticker and orderbook(L2) channels.
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/ticker",
                "symbols": [
                    "BTCUSD",
                    "ETHUSD"
                ]
            },
            {
                "name": "l2_orderbook",
                "symbols": [
                    "BTCUSD"
                ]
            },
            {
                "name": "funding_rate",
                "symbols": [
                    "all"
                ]
            }
        ]
    }
}

// Response: Success
{
    "type": "subscriptions",
    "channels": [
        {
            "name": "l2_orderbook",
            "symbols": [
                "BTCUSD"
            ],
        },
        {
            "name": "v2/ticker",
            "symbols": [
                "BTCUSD",
                "ETHUSD"
            ]
        },
        {
            "name": "funding_rate",
            "symbols": [
                "all"
            ]
        }
    ]
}

// Response: Error 
{
    "type": "subscriptions",
    "channels": [
        {
            "name": "l2_orderbook",
            "symbols": [
                "BTCUSD"
            ],
        },
        {
            "name": "trading_notifications",
            "error": "subscription forbidden on trading_notifications. Unauthorized user"
        }
    ]
}
```


## Unsubscribe

If you want to unsubscribe from channel/contracts pairs, send an "unsubscribe" message. The structure is equivalent to subscribe messages. If you want to unsubscribe for specific symbols in a channel, you can pass it in the symbol list. As a shorthand you can also provide no symbols for a channel, which will unsubscribe you from the channel entirely.

> Unsubscribe Sample

```json
// Request: Unbubscribe from BTCUSD and ETHUSD with the ticker and orderbook(L2) channels.
{
    "type": "unsubscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/ticker",          // unsubscribe from ticker channel only for BTCUSD
                "symbols": [
                    "BTCUSD"
                ]
            },
            {
                "name": "l2_orderbook"      // unsubscribe from all symbols for l2_orderbook channel
            }
        ]
    }
}
```

# Authenticating

## Current method

Authentication allows clients to subscribe to user account related trading notifications using private channels like positions, orders, etc. This allows users to get real-time updates related to their orders, fills, liquidations, [adl](/#trading-notitifications) and pnl updates.

```python
# auth message with signed request
import websocket
import hashlib
import hmac
import time

api_key = 'a207900b7693435a8fa9230a38195d'
api_secret = '7b6f39dcf660ec1c7c664f612c60410a2bd0c258416b498bf0311f94228f'

def generate_signature(secret, message):
    message = bytes(message, 'utf-8')
    secret = bytes(secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest()

# Get open orders
method = 'GET'
timestamp = str(int(time.time()))
path = '/live'
signature_data = method + timestamp + path
signature = generate_signature(api_secret, signature_data)

ws = websocket.WebSocketApp('wss://socket.india.delta.exchange')

ws.send(json.dumps({
    "type": "key-auth",
    "payload": {
        "api-key": api_key,
        "signature": signature,
        "timestamp": timestamp
    }
}))

ws.send(json.dumps({
    "type": 'unauth',
    "payload": {}
}))
```

**Note**: For users migrating from older authentication method, the change is: "type" in request payload must be changed from "auth" to "key-auth". Rest of the request payload will remain the same. The response payloads have major changes. Check below for the response payloads.  


To authenticate, you must send a request of type **'key-auth'** on your socket connection. Authentication request is a json of the format:  
`{"type":"key-auth","payload":{"api-key":"#KEY#","timestamp":#TIMESTAMP#,"signature":"#SIGNATURE#"}}`  
**KEY** here is your API-key string.  
**TIMESTAMP** is current epoch Unix timestamp in seconds as a number.  
**SIGNATURE** is hash string of HMAC created using `'GET' + string(TIMESTAMP) + '/live'` and your API-secret.  
Note: Same timestamp must be used for TIMESTAMP and in generating SIGNATURE. 

Refer to the right side for a sample code.

<br><br><br>

**Authentication Responses**  
All authentication responses will be json containing following keys:  
**"type"** will always be "key-auth"  
**"success"** is a boolean indicating whether the authentication was a success or failure.  
**"status_code"** is number just like HTTP response status.  
**"status"** is a string describing the response status.  
**"message"** is a string which may be present describing authentication failure reason.


Success response:  
`{"type":"key-auth", "success":true, "status_code":200, "status":"authenticated"}`


Error responses:  

1. Lacking 'api-key' or 'sign' or 'timestamp' in the payload:  
`{"type":"key-auth", "success":false, "status_code":400, "status":"incomplete_payload", "message":"Incomplete payload"}`  

2. Request received after 5 secs:   
`{"type":"key-auth", "success":false, "status_code":408, "status":"request_expired", "message":"Timestamp header outside of allowed time window"}}`  

3. ApiKey does not exist:  
`{"type":"key-auth", "success":false, "status_code":404, "status":"api_key_not_found", "message":"ApiKey not found"}}`  

4. Invalid/wrong Signature:  
`{"type":"key-auth", "success":false, "status_code":401, "status":"invalid_signature", "message":"Invalid Signature"}`  

5. IP address not whitelisted for the API-key:  
`{"type":"key-auth", "success":false, "status_code":401, "status":"ip_not_whitelisted", "message":"IP address not whitelisted. Your IP: 172.16.19.91"}`  

6. Some internal server error:  
`{"type":"key-auth", "success":false, "status_code":500, "status":"internal_server_error", "message": "Internal Server Error. Code: 1001"`


## Old method

Note: This method of authentication will stop working from 31st December 2025.

Authentication allows clients to receives private messages, like trading notifications. Examples of the trading notifications are: fills, liquidations, [adl](/#trading-notitifications) and pnl updates.

To authenticate, you need to send a signed request of type **'auth'** on your socket connection. Check the authentication section above for more details on how to sign a request using api key and secret.

The payload for the signed request will be ***'GET' + timestamp + '/live'***

To subscribe to private channels, the client needs to first send an auth event, providing api-key, and signature. 

To unsubscribe from all private channels, just send a **'unauth'** message on the socket. This will automatically unsubscribe the connection from all authenticated channels.


# Sample Python Code

## Public Channels

**Summary:** 
The python script(right panel) connects to the Delta Exchange WebSocket to receive real-time market data.

- It opens a connection.
- Subscribes to `v2/ticker`(tickers data) and `candlestick_1m`(1 minute ohlc candlesticks) channels. (**MARK:BTCUSD** - mark price ohlc in candlesticks channel)
- When data arrives, it processes and prints it.
- If an error occurs, it prints an error message.
- If the connection closes, it notifies the user.
- The connection remains open indefinitely to keep receiving updates.

```python
import websocket
import json

# production websocket base url
WEBSOCKET_URL = "wss://socket.india.delta.exchange"

def on_error(ws, error):
    print(f"Socket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Socket closed with status: {close_status_code} and message: {close_msg}")

def on_open(ws):
  print(f"Socket opened")
  # subscribe tickers of perpetual futures - BTCUSD & ETHUSD, call option C-BTC-95200-200225 and put option - P-BTC-95200-200225
  subscribe(ws, "v2/ticker", ["BTCUSD", "ETHUSD", "C-BTC-95200-200225", "P-BTC-95200-200225"])
  # subscribe 1 minute ohlc candlestick of perpetual futures - MARK:BTCUSD(mark price) & ETHUSD(ltp), call option C-BTC-95200-200225(ltp) and put option - P-BTC-95200-200225(ltp).
  subscribe(ws, "candlestick_1m", ["MARK:BTCUSD", "ETHUSD", "C-BTC-95200-200225", "P-BTC-95200-200225"])

def subscribe(ws, channel, symbols):
    payload = {
        "type": "subscribe",
        "payload": {
            "channels": [
                {
                    "name": channel,
                    "symbols": symbols
                }
            ]
        }
    }
    ws.send(json.dumps(payload))

def on_message(ws, message):
    # print json response
    message_json = json.loads(message)
    print(message_json)

if __name__ == "__main__":
  ws = websocket.WebSocketApp(WEBSOCKET_URL, on_message=on_message, on_error=on_error, on_close=on_close)
  ws.on_open = on_open
  ws.run_forever() # runs indefinitely
```

## Private Channels

**Summary:** 
The python script(right panel) connects to the Delta Exchange WebSocket to receive real-time market data.

- It opens a connection.
- Sends authentication payload over socket with api_key, signature & timestamp.
- When authentication update arrives, it checks for success and then sends subscription for `orders` and `positions` channels for all contracts.
- Prints all other updates in json format.
- If an error occurs, it prints an error message.
- If the connection closes, it notifies the user.
- The connection remains open indefinitely to keep receiving updates.

```python
import websocket
import hashlib
import hmac
import json
import time

# production websocket base url and api keys/secrets
WEBSOCKET_URL = "wss://socket.india.delta.exchange"
API_KEY = 'a207900b7693435a8fa9230a38195d'
API_SECRET = '7b6f39dcf660ec1c7c664f612c60410a2bd0c258416b498bf0311f94228f'

def on_error(ws, error):
    print(f"Socket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Socket closed with status: {close_status_code} and message: {close_msg}")

def on_open(ws):
    print(f"Socket opened")
    # api key authentication
    send_authentication(ws)

def send_authentication(ws):
    method = 'GET'
    timestamp = str(int(time.time()))
    path = '/live'
    signature_data = method + timestamp + path
    signature = generate_signature(API_SECRET, signature_data)
    ws.send(json.dumps({
        "type": "key-auth",
        "payload": {
            "api-key": API_KEY,
            "signature": signature,
            "timestamp": timestamp
        }
    }))

def generate_signature(secret, message):
    message = bytes(message, 'utf-8')
    secret = bytes(secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest()

def on_message(ws, json_message):
    message = json.loads(json_message)
    # subscribe private channels after successful authentication
    if message['type'] == 'key-auth':
        if message['success']:
            print("Authentication successful")
            # subscribe orders channel for order updates for all contracts
            subscribe(ws, "orders", ["all"])
            # subscribe positions channel for position updates for all contracts
            subscribe(ws, "positions", ["all"])
        else:
            print("Authentication failed")
            print(message)
    else:
        print(json_message)

def subscribe(ws, channel, symbols):
    payload = {
        "type": "subscribe",
        "payload": {
            "channels": [
                {
                    "name": channel,
                    "symbols": symbols
                }
            ]
        }
    }
    ws.send(json.dumps(payload))

if __name__ == "__main__":
  ws = websocket.WebSocketApp(WEBSOCKET_URL, on_message=on_message, on_error=on_error, on_close=on_close)
  ws.on_open = on_open
  ws.run_forever() # runs indefinitely
```


# Detecting Connection Drops
Some client libraries might not detect connection drops properly. We provide two methods for the clients to ensure they are connected and getting subscribed data.

## Heartbeat (Recommended)
The client can enable heartbeat on the socket. If heartbeat is enabled, the server is expected to periodically send a heartbeat message to the client. Right now, the heartbeat time is set to 30 seconds. 

### How to Implement on client side

- Enable heartbeat (check sample code) after each successful socket connection
- Set a timer with duration of 35 seconds (We take 5 seconds buffer for heartbeat to arrive).
- When you receive a new heartbeat message, you reset the timer
- If the timer is called, that means the client didn't receive any heartbeat in last 35 seconds. In this case, the client should exit the existing connection and try to reconnect. 

```python
// Enable Heartbeat on successful connection
ws.send({
    "type": "enable_heartbeat"
})

// Disable Heartbeat
ws.send({
    "type": "disable_heartbeat"
})

// Sample Heartbeat message received periodically by client
{
    "type": "heartbeat"
}
```


## Ping/Pong
The client can periodically (~ every 30 seconds) send a ping frame or a raw ping message and the server will respond back with a pong frame or a raw pong response. If the client doesn't receive a pong response in next 5 seconds, the client should exit the existing connection and try to reconnect. 

```python
// Ping Request
ws.send({
    "type": "ping"
})

// Pong Response
ws.send({
    "type": "pong"
})
```

# Public Channels

## v2 ticker

The ticker channel provides **price change data** for the last **24 hrs** (rolling window).  
It is published every **5 seconds**.

To subscribe to the ticker channel, you need to send the list of **symbols** for which you would like to receive updates.

You can also subscribe to ticker updates for a **category of products** by sending a list of [category names](/#schemaproductcategories).  
For example, to receive updates for **put options** and **futures**, use the following format:  
```
{"symbols": ["put_options", "futures"]}
```

If you would like to subscribe to all listed contracts, pass:  
```
{ "symbols": ["all"] }
```

**Important:**  
If you subscribe to the ticker channel without specifying a symbols list, you will **not** receive any data.

> **Ticker Sample**

```json
// Subscribe to specific symbol
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/ticker",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}

// Subscribe to all symbols
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/ticker",
                "symbols": [
                    "all"
                ]
            }
        ]
    }
}
```

```json
// Response
{
    "open": 0.00001347, // The price at the beginning of the 24-hour period
    "close": 0.00001327, // The price at the end of the 24-hour period
    "high": 0.00001359, // The highest price during the 24-hour period
    "low": 0.00001323, // The lowest price during the 24-hour period
    "mark_price": "0.00001325", // The current market price
    "mark_change_24h": "-0.1202", // Percentage change in market price over the last 24 hours
    "oi": "812.6100", // Open interest, indicating the total number of outstanding contracts
    "product_id": 27, // The unique identifier for the product
    "quotes": {
        "ask_iv": "0.25", // Implied volatility for the ask price (if available)
        "ask_size": "922", // The size of the ask (the amount available for sale)
        "best_ask": "3171.5", // The best ask price (the lowest price at which the asset is being offered)
        "best_bid": "3171.4", // The best bid price (the highest price a buyer is willing to pay)
        "bid_iv": "0.25", // Implied volatility for the bid price (if available)
        "bid_size": "191", // The size of the bid (the amount a buyer is willing to purchase)
        "impact_mid_price": "61200", // Mid price impact, if available (the price midpoint between the best bid and ask)
        "mark_iv": "0.29418049" // Mark volatility (volatility of the asset used for mark price calculation)
    },
    "greeks": { // Options-related metrics, will be null for Futures and Spot products
        "delta": "0.01939861", // Rate of change of the option price with respect to the underlying asset's price
        "gamma": "0.00006382", // Rate of change of delta with respect to the underlying asset's price
        "rho": "0.00718630", // Rate of change of option price with respect to interest rate
        "spot": "63449.5", // The current spot price of the underlying asset
        "theta": "-81.48397021", // Rate of change of option price with respect to time (time decay)
        "vega": "0.72486575" // Sensitivity of the option price to volatility changes
    },
    "size": 1254631, // Number of contracts traded
    "spot_price": "0.00001326", // Spot price at the time of the ticker
    "symbol": "BTCUSD", // The symbol of the contract
    "timestamp": 1595242187705121, // The timestamp of the data (in microseconds)
    "turnover": 16.805033569999996, // The total turnover in the settling symbol
    "turnover_symbol": "BTC", // The symbol used for settling
    "turnover_usd": 154097.09108233, // The turnover value in USD
    "volume": 1254631 // Total volume, defined as contract value * size
}
```

## l1_orderbook

**l1_orderbook** channel provides level1 orderbook updates. You need to send the list of symbols for which you would like to subscribe to L1 orderbook. You can also subscribe to 
orderbook updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to L1 channel without specifying the symbols list, you will not receive any data.  
Publish interval: 100 millisecs  
Max interval (in case of same data): 5 secs

> L1 Orderbook Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "l1_orderbook",
                "symbols": [
                    "ETHUSD"
                ]
            }
        ]
    }
}
```

```json
// l1 orderbook Response
{
  "ask_qty":"839",
  "best_ask":"1211.3",
  "best_bid":"1211.25",
  "bid_qty":"772",
  "last_sequence_no":1671603257645135,
  "last_updated_at":1671603257623000,
  "product_id":176,"symbol":"ETHUSD",
  "timestamp":1671603257645134,
  "type":"l1_orderbook"
}
```

<!--
## l1ob

**l1ob** channel provides best ask and bid price, size updates in the orderbook. You need to send the list of symbols for which you would like to subscribe. If best ask/bid data is same for a symbol, same data will only be sent after the max interval (stated below) has passed since that symbol's data was last sent.
Please note that if you subscribe to l1ob channel without specifying the symbols list, you will not receive any data.  
Publish interval: 100 millisecs  
Max interval (in case of same data): 5 secs

> l1ob subscribe Sample

```
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "l1ob",
                "symbols": [
                    "BTCUSD",
                    "C-BTC-42000-260124"
                ]
            }
        ]
    }
}
```

```
// l1ob sample Response
{
  "type":"l1ob",
  "s":"BTCUSD",  //product symbol
  "d": ["37026.2","2133","37025.6","1977"],  
  // [BestAskPrice, BestAskSize, BestBidPrice, BestBidSize]
  // Price and Size will be null for the side with no orders.
  "t": 1701157803668868, //message publish time in microsec
  "T": 1701157444959989  //orderbook update time in microsec
}
```

## l1ob_c

**l1ob_c** channel provides best ask and bid price, size updates in the orderbook for an Option chain. You can subscribe to a Asset_Expiry. e.g. To subscribe to data for all BTC Options expiring on 26th January 2024, send "BTC_260124". If best ask/bid data is same for a symbol, same data will only be sent after the max interval (stated below) has passed since that symbol's data was last sent.
The data is Brotli compressed and in base64 encoded string format, to use this data first Brotli decompress to get a list of json. 
Please note that if you subscribe to l1ob_c channel without specifying the Asset_Expiry list, you will not receive any data.  
Publish interval: 100 millisecs  
Max interval (in case of same data): 5 secs

> l1ob_c subscribe Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "l1ob_c",
                "symbols": [
                    "BTC_260124",
                    "BTC_270124"
                ]
            }
        ]
    }
}
```

```json
// l1ob_c Response
{
  "type":"l1ob_c",
  "s":"BTC_011223",  //Asset_Expiry
  "c": "G6gA+B0HzjnKz3E2icneQi2yFbPX1mbq5Ok9j49QZ6iGuNDWLDpdfWEDjinwATeecMOF7GTgAjJOddfahjsUbHpW6fEp4spZhjoMQTFpZEo2fjnjvWcEAQyUk2E32VVd3ssdudqRE61qupUB",  
  //Brotli decompress this to get the below json.
  "t": 1701157556471116  //message publish time
}
//Brotli decompressed data format
[{
    "T":1701105329216885,  //orderbook update time in microsec
    "s":"C-BTC-32000-081223",  //product symbol
    "d":["5246.8","593","5053.2","6655"]  // [BestAskPrice, BestAskSize, BestBidPrice, BestBidSize]
},
{
    "T":1701105298898194,
    "d":["1064.8","593","936.0","989"],
    "s":"C-BTC-37500-081223"
}, ...
]
```
-->


## l2_orderbook

**l2_orderbook** channel provides the complete level2 orderbook for the sepecified list of symbols at a pre-determined frequency. The frequency of updates may vary for different symbols. You can only subscribe to upto 20 symbols on a single connection. Unlike L1 orderbook channel, L2 orderbook channel does not accept product category names or "all" as valid symbols. 
Please note that if you subscribe to L2 channel without specifying the symbols list, you will not receive any data.  
Publish interval: 1 sec  
Max interval (in case of same data): 10 secs

> L2 Orderbook Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "l2_orderbook",
                "symbols": [
                    "ETHUSD"
                ]
            }
        ]
    }
}
```

```json
// l2 orderbook Response
{
  "type":"l2_orderbook",
  "symbol":"ETHUSD",
  "product_id": 176,
  "buy": [
    {
        "limit_price":"101.5",
        "size":10,              // For Futures & Options: number of contracts integer. Spot product: Asset token quantity in string.
        "depth":"10"            // total size from best bid
    },
  ],
  "sell": [
    {
        "limit_price":"102.0",
        "size":20,
        "depth":"20"            // total size from best ask
    },
  ],
  "last_sequence_no": 6435634,
  "last_updated_at": 1671600133884000,
  "timestamp":1671600134033215,
}
```

## l2_updates

**l2_updates** channel provides initial snapshot and then incremental orderbook data. The frequency of updates may vary for different symbols. You can only subscribe to upto 100 symbols on a single connection. l2_updates channel does not accept product category names or "all" as valid symbols. 
Please note that if you subscribe to l2_updates channel without specifying the symbols list, you will not receive any data.  
Publish interval: 100 millisecs  
"action"="update" messages wont be published till there is an orderbook change.

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "l2_updates",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}

// Initial snapshot response
{
  "action":"snapshot",
  "asks":[["16919.0", "1087"], ["16919.5", "1193"], ["16920.0", "510"]],
  "bids":[["16918.0", "602"], ["16917.5", "1792"], ["16917.0", "2039"]],
  "timestamp":1671140718980723,
  "sequence_no":6199,
  "symbol":"BTCUSD",
  "type":"l2_updates",
  "cs":2178756498
}

// Incremental update response
{
  "action":"update",
  "asks":[["16919.0", "0"], ["16919.5", "710"]],
  "bids":[["16918.5", "304"]],
  "sequence_no":6200,
  "symbol":"BTCUSD",
  "type":"l2_updates",
  "timestamp": 1671140769059031,
  "cs":3409694612
}

// Error response
{
  "action":"error",
  "symbol":"BTCUSD",
  "type":"l2_updates",
  "msg":"Snapshot load failed. Verify if product is live and resubscribe after a few secs."
}
```

### How to maintain orderbook locally using this channel:

1) When you subscribe to this channel, the first message with "action"= "snapshot" resembles the complete l2_orderbook at this time. "asks" and "bids" are arrays of ["price", "size"]. (size is number of contracts at this price)

2) After the initial snapshot, messages will be with "action" = "update", resembling the difference between current and previous orderbook state. "asks" and "bids" are arrays of ["price", "new size"]. "asks" are sorted in increasing order of price. "bids" are sorted in decreasing order of price. This is true for both "snapshot" and "update" messages.

3) "sequence_no" field must be used to check if any messages were dropped. "sequence_no" must be +1 of the last message.  
e.g. In the snapshot message it is 6199, and the update message has 6200. The next update message must have 6201. In case of sequence_no mismatch, resubscribe to the channel, and start from the beginning.

4) If sequence_no is correct, edit the in-memory orderbook using the "update" message.  
Case 1: price already exists, new size is 0 -> Delete this price level.  
Case 2: price already exists, new size isn't 0 -> Replace the old size with new size.  
Case 3: price doesn’t exists -> insert the price level.  
e.g. for the shown snapshot and update messages to create the new orderbook: in the ask side, price level of "16919.0" will be deleted. Size at price level "16919.5" will be changed from "1193" to "710". In the bids side there was no price level of "16918.5", so add a new level of "16918.5" of size "304". Other price levels from the snapshot will remain the same.

5) If "action":"error" message is received, resubscribe this symbol after a few seconds. Can occur in rare cases, e.g. Failed to send "action":"snapshot" message after subscribing due to a race condition, instead an "error" message will be sent.

Checksum: Using this, users can verify the accuracy of orderbook data created using l2_updates. checksum is the "cs" key in the message payload.  
Steps to calculate checksum:  
1) Edit the old in-memory orderbook with the "update" message received.  
2) Create asks_string and bids_string as shown below. where priceN = price at Nth level, sizeN = size at Nth level. Asks are sorted in increasing order and bids in decreasing order by price.  
asks_string = price0:size0,price1:size1,…,price9:size9  
bids_string = price0:size0,price1:size1,…,price9:size9  
checksum_string = asks_string + "|" + bids_string  
Only consider the first 10 price levels on both sides. If orderbook as less than 10 levels, use only them.  
e.g. If after applying the update, the new orderbook becomes ->  
asks = [["100.00", "23"], ["100.05", "34"]]  
bids = [["99.04", "87"], ["98.65", "102"], ["98.30", "16"]]  
checksum_string = "100.00:23,100.05:34|99.04:87,98.65:102,98.30:16"  
3) Calculate the CRC32 value (32-bit unsigned integer) of checksum_string. This should be equal to the checksum provided in the “update” message.

## all_trades

**all_trades** channel provides a real time feed of all trades (fills).
You need to send the list of symbols for which you would like to subscribe to all trades channel. After subscribing to this channel, you get a snapshot of last 50 trades and then trade data in real time. You can also subscribe to
all trades updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to all_trades channel without specifying the symbols list, you will not receive any data.

> All Trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "all_trades",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}
```

```json
// All Trades Response Snapshot
{
    "symbol": "BTCUSD",
    "type": "all_trades_snapshot",          // "type" is not "all_trades"
    "trades": [                             // Recent trades list
        {
            "buyer_role": "maker",
            "seller_role": "taker",
            "size": 53,                     // size in contracts
            "price": "25816.5",
            "timestamp": 1686577411879974   // time of the trade.
        },
         // More recent trades.
    ]
}
```

```json
// All Trades Response
{
    "symbol": "BTCUSD",
    "price": "25816.5",
    "size": 100,
    "type": "all_trades",
    "buyer_role": "maker",
    "seller_role": "taker",
    "timestamp": 1686577411879974
}
```



## mark_price

**mark_price** channel provides mark price updates at a fixed interval. This is the price on which all open positions are marked for liquidation.Please note that the product symbol is prepended with a "MARK:" to subscribe for mark price.  
You need to send the list of symbols for which you would like to subscribe to mark price channel. You can also subscribe to 
mark price updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.  
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.  
You can also subscribe to a Options chain, by passing 'Asset-Expiry', e.g. `{"symbols": ["BTC-310524"] }` will subscribe to all BTC Options expirying on 31st May 2024.  
Please note that if you subscribe to mark price channel without specifying the symbols list, you will not receive any data.  
Publish interval: 2 secs.


> Mark Price Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "mark_price",
                "symbols": [
                    "MARK:C-BTC-13000-301222"
                ]
            }
        ]
    }
}
```

```json
// Mark Price Response
{
    "ask_iv":null,
    "ask_qty":null,
    "best_ask":null,
    "best_bid":"9532",
    "bid_iv":"5.000",
    "bid_qty":"896",
    "delta":"0",
    "gamma":"0",
    "implied_volatility":"0",
    "price":"3910.088012",
    "price_band":{"lower_limit":"3463.375340559572217228510815","upper_limit":"4354.489445440427782771489185"},
    "product_id":39687,
    "rho":"0",
    "symbol":"MARK:C-BTC-13000-301222",
    "timestamp":1671867039712836,
    "type":"mark_price",
    "vega":"0"
}
```

## candlesticks
This channel provides last ohlc candle for given time resolution. Traded price candles and Mark Price candles data can be received by sending appropriate symbol string. "product_symbol" gives traded_price candles, and "MARK:product_symbol" gives mark_price candles.  
e.g. symbols: ["BTCUSD"] gives you Traded Price candlestick data for BTCUSD  
symbols: ["MARK:C-BTC-75000-310325"] gives you Mark Price candlestick data for C-BTC-75000-310325

Subscribe to **candlestick_${resolution}** channel for updates. 

List of supported resolutions
["1m","3m","5m","15m","30m","1h","2h","4h","6h","12h","1d","1w"]
 
You need to send the list of symbols for which you would like to subscribe to candlesticks channel. 
You can also subscribe to candlesticks updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
Please note that if you subscribe to candlesticks channel without specifying the symbols list, you will not receive any data.

>OHLC candles update sample

```json
//Sample Subscribe Request
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "candlestick_5m",        // "candlestick_" + resolution
                "symbols": ["BTCUSD", "C-BTC-75000-271224"]
            }
        ]
    }
}



Sample feed response

{
    "candle_start_time": 1596015240000000,
    "close": 9223,
    "high": 9228,
    "low": 9220,
    "open": 9221,
    "resolution": "1m",
    "symbol": "BTCUSD",
    "timestamp": 1596015289339699,
    "type": "candlestick_1m",
    "volume": 1.2            // volume not present in Mark Price candlestick
}
```

## spot_price

**spot_price** channel provides a real time feed of the underlying index prices. Specifying symbols when subscribing to spot_price is necessary to receive updates. No updates are sent for symbol: ***"all"***

> Spot Price Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "spot_price",
                "symbols": [
                    ".DEBNBBTC"
                ]
            }
        ]
    }
}
```

```json
// Spot Price Response
{
    "symbol": ".DEBNBBTC",
    "price": "0.0014579",
    "type": "spot_price"
}
```

## v2/spot_price

**v2/spot_price** channel publishes data of underlying index prices at a fixed interval. Specifying symbols when subscribing to v2/spot_price is necessary to receive updates. No updates are sent for symbol: ***"all"***  
Publish interval: 1 sec  

> v2/spot_price Subscribe

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/spot_price",
                "symbols": [
                    ".DEETHUSD"
                ]
            }
        ]
    }
}
```

```json
// Response
{
    "s": ".DEETHUSD",   # spot index symbol
    "p": 1349.3412141,   # spot price
    "type": "v2/spot_price"
}
```

## spot_30mtwap_price

**spot_30mtwap_price** channel provides a real time feed of the 30 min twap of underlying index prices. 
This is the price used for settlement of options. Specifying symbols when subscribing to spot_30mtwap_price is necessary to receive updates. No updates are sent for symbol: ***"all"***

> Spot Price 30mtwap Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "spot_30mtwap_price",
                "symbols": [
                    ".DEXBTUSD"
                ]
            }
        ]
    }
}
```

```json
// Spot 30 minutes twap Price Response
{
    "symbol": ".DEXBTUSD",
    "price": "0.0014579",
    "type": "spot_30mtwap_price",
    "timestamp": 1561634049751430
}
```

## funding_rate

**funding_rate** channel provides a real time feed of funding rates for perpetual contracts.

You need to send the list of symbols for which you would like to subscribe to funding rate channel. You can also subscribe to funding rate updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to funding rate channel without specifying the symbols list, you will not receive any data.

> Funding Rate Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "funding_rate",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}
```

```json
// Funding Rate Response
{
    "symbol": "BTCUSD",
    "product_id": 139,
    "type": "funding_rate",
    "funding_rate": 0.005701298078111892,  // %
    "funding_rate_8h": 0.005701298078111892, // %
    "next_funding_realization": 1683734400000000, // %
    "predicted_funding_rate": 0.007221329334075148, // in us
    "timestamp": 1683711930547419   // in us
}
```

## product_updates
This channel provides updates when markets are disrupted and resumed. On opening, we conduct a single price auction and auction starting and finish events are also published on this channel. To subscribe, you dont need to pass the symbol list. This channel automatically subscribes to all markets by default.

>  Product Updates Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "product_updates"
            }
        ]
    }
}
```

```json
// Market Disruption Response
{
    "type":"product_updates",
    "event":"market_disruption",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"disrupted_cancel_only",
    },
    "timestamp": 1561634049751430,
}

// Auction Started Response
{
    "type":"product_updates",
    "event":"start_auction",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"disrupted_post_only",
    },
    "timestamp": 1561634049751430,
}

// Auction Finished Response
{
    "type":"product_updates",
    "event":"finish_auction",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"operational",
    },
    "timestamp": 1561634049751430,
}
```
### Market Disruption
When markets are disrupted, orderbook enters into cancel only mode. You can refer to "trading_status" field in product info to determine this. In cancel only mode, you can only cancel your orders. No matching happens in this mode.

### Auction Started
When markets need to come up, we conduct a single price auction. In this case, orderbook enters into post only mode. In post only mode, you can post new orders, cancel exisiting orders, add more margin to open positions. No matching happens in this mode. It is possible to see an overlap between asks and bids during this time.


### Auction Finished
When auction finishes, markets enter into operational mode and trading continues as usual. 

You can read more about the single price auction [here](https://www.delta.exchange/blog/bootstrapping-liquidity-using-auctions/)


## announcements
This channel will be deprecated on 28 February 2026. Please use the system_status channel for all maintenance-related updates.

This channel provides updates on system wide announcements like scheduled maintenance, maintenance started etc. No need to pass any symbols while subscribing to this channel. Below are types and examples of messages sent for more details:  
1. "event": "maintenance_scheduled" is sent when maintenance is scheduled. This is around 6 to 24 hours before the actual maintenance. Contains estimated start and finish time for maintenance.  
2. "event": "maintenance_started" is sent when maintenance actually starts and markets are disrupted. Contains estimated finish time for maintenance.  
3. "event": "maintenance_finished" is sent when maintenance finishes and market is set in auction node for short duration; then trading is resumed.  

> Announcements Sample


```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "announcements"
            }
        ]
    }
}
```

```json
// Maintenance Scheduled Response
{
    "type": "announcements",
    "event": "maintenance_scheduled",
    "maintenance_start_time": 1742301546000000,   // estimated maintenance start time in microseconds
    "maintenance_finish_time": 1742301647000000   // estimated finish time
}

```json
// Maintenance Started Response
{
    "type":"announcements",
    "event":"maintenance_started",
    "maintenance_finish_time": 1561638049751430, // estimated finish time in microseconds.
    "timestamp": 1561634049751430,
}

// Maintenance Finished Response
{
    "type":"announcements",
    "event":"maintenance_finished",
    "timestamp": 1561634049751430,
}
```

## system_status
This is a public websocket channel that provides updates on system-wide status events such as scheduled maintenance, maintenance start and finish, degraded mode, and fallback operation. No symbols are required when subscribing to this channel. Below are the types of messages sent for more details:
> System status Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "system_status"
            }
        ]
    }
}
```

```json
// Maintenance Scheduled Response
{
    "type": "system_status",
    "status": "live",
    "event": "maintenance_scheduled",
    "maintenance_start_time": 1765259125000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764548092000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259428000000, // estimated finish time
    "timestamp": 1765239292000000
}

// Maintenance Started Response
{
    "type":"system_status",
    "status": "maintenance",
    "event":"maintenance_started",
    "maintenance_start_time": 1765259301000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764720892000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259450000000, // estimated finish time in microseconds.
    "timestamp": 1765259716000000
}

// Maintenance Cancelled Response
{
    "type":"system_status",
    "status": "api_fallback", // current status
    "event":"maintenance_cancelled",
    "maintenance_start_time": 1765259325000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764807292000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259526000000, // estimated finish time in microseconds.
    "timestamp": 1765259727000000
}

// Maintenance Finished Response
{
    "type":"system_status",
    "status": "live",
    "event":"maintenance_finished",
    "maintenance_start_time": 1765259338000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764634492000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259575000000, // estimated finish time in microseconds.
    "timestamp": 1765259744000000
}
```

snapshot → This event is sent as soon as you subscribe to the system_status channel. The data in this event contains the current system status details.

1. "event": "maintenance_scheduled" is sent when maintenance is scheduled, usually 6 to 24 hours before the actual maintenance. It includes the estimated start and finish times.  
2. "event": "maintenance_started" is sent when maintenance begins. It indicates service disruption and includes the estimated finish time. For unscheduled maintenance, this event may be sent directly without the prior maintenance_scheduled event.  
3. "event": "maintenance_finished" is sent when maintenance is complete. Usually, after this event, there is an auction period lasting around 5 to 10 minutes.  
4. "event": "maintenance_cancelled" is sent when upcoming scheduled maintenance has been cancelled.

Note: Maintenance start and finish times are approximate estimates. The actual start time is confirmed by the maintenance_started event, and the actual completion is confirmed by the maintenance_finished event.

These values describe the current state of the entire system.

The payload["status"] describe the current state of the entire system. Below are the possible values:

1. "live": The system is operating normally. All services (REST APIs, WebSocket, backend processes) are functioning as expected.  
2. "maintenance": The system is currently under maintenance. Some features or services may be temporarily unavailable or disrupted.  
3. "api_fallback": Our system might be facing some technical issues, but most core functions remain available. Mostly used by our internal system. You can treat this as "live" mode, and check with our support team.  
4. "degraded_mode": Our system might be facing some technical issues, but most core functions remain available. Mostly used by our internal system. You can treat this as "live" mode, and check with our support team.  

Changing status to between these three: ["api_fallback", "degraded_mode", "live"] is done by sending message with 

"event":  "app_status_update".

e.g. payload = %{type: "system_status", event: "app_status_update", status: "api_fallback", maintenance_announcement_time: time, maintenance_start_time: time, maintenance_finish_time: time, timestamp: current_time}

Note: The "app_status_update" messages will still contain correct maintenance related timestamps.

In addition to the event field, the status field reflects the overall system state, such as: live, maintenance, api_fallback, or degraded_mode.
All timestamps are in epoch microseconds.

# Private Channels

Private channels require clients to authenticate.

## Margins
This channel provides updates on wallet balances. Updates are sent for a specific asset whenever there is a change in wallet balances and margins for that asset. 

> Margins Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "margins"
            }
        ]
    }
}
```
```json
// margin update
{
    "action": "update",
    "asset_id": 2,                           // BTC
    "asset_symbol": "BTC",                   // BTC
    "available_balance": "9.385",            // Available balance for trading = balance - blocked_margin
    "available_balance_for_robo": "9.385",   // Available balance for robo trading = balance - blocked_margin
    "balance": "10",                         // Wallet balance = deposits - withdrawals + realised_cashflows
    "blocked_margin": "0.615",               // Total Margin blocked
    "commission": "0.001",                   // Commissions blocked in isolated margined positions and orders
    "cross_asset_liability": "0",            // Liability between asset in cross margin mode
    "cross_commission": "0.002",             // Commissions blocked in cross margined positions and orders
    "cross_locked_collateral": "0.003",      // Balance blocked for collateral
    "cross_order_margin": "0.004",           // Margin blocked in cross margined open orders
    "cross_position_margin": "0.005",        // Margin blocked in cross margined positions
    "id": 1,                                 // Wallet Id
    "interest_credit": "0",                  // Interest credited
    "order_margin": "0.1",                   // Margin blocked in isolated margined open orders
    "pending_referral_bonus": "0",           // Bonus pending
    "pending_trading_fee_credit": "0",       // Pending trading fee to credit
    "portfolio_margin": "0.2",               // Margin blocked for portfolio margined positions and orders. Same as blocked margin in portfolio margins channel.
    "position_margin": "0.3",                // Margin blocked in isolated margined positions
    "robo_trading_equity": "0",              // Equity for robo trading
    "timestamp": 1719397302569921,           // Unix timestamp in microseconds
    "trading_fee_credit": "0",               // Trading fee credited
    "type": "margins",                       // Margins channel
    "unvested_amount": "0",                  // Amount locked. Relevant only for DETO
    "user_id": 1                             // User id
}
```


## Positions
This channel provides updates whenever there is any change in your open positions.

A snapshot of current open position will be sent after subscribing a symbol, incremental updates will be sent on trade executions.
You need to send the list of symbols for which you would like to subscribe to positions channel. You can also subscribe to positions 
updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to positions channel without specifying the symbols list, you will not receive any data.

> Positions Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "positions",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}

//Subscribe for all the symbols
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "positions",
                "symbols": ["all"]
            }
        ]
    }
}
```

```json
// Position update
{
    "type": "positions",
    "action": "",                       // "create"/"update"/"delete"
    "reason": "",                       // null, "auto_topup"
    "symbol": "BTCUSD",           // Product Symbol
    "product_id": 1,                    // Product ID
    "size": -100,                       // Position size, if > 0 -> long else short
    "margin": "0.0121",                 // Margin blocked in the position
    "entry_price": "3500.0",            // Avg Entry price of the position
    "liquidation_price": "3356.0",      // Liquidation trigger price
    "bankruptcy_price": "3300.0",       // Bankruptcy Price
    "commission": "0.00001212"          // Commissions blocked for closing the position
}

//Snapshot 
{
   "result":[
      {
         "adl_level":"4.3335",
         "auto_topup":false,
         "bankruptcy_price":"261.82",
         "commission":"17.6571408",
         "created_at":"2021-04-29T07:25:59Z",
         "entry_price":"238.023457888493475682",
         "liquidation_price":"260.63",
         "margin":"4012.99",
         "product_id":357,
         "product_symbol":"ZECUSD",
         "realized_funding":"-3.08",
         "realized_pnl":"6364.57",
         "size":-1686,
         "updated_at":"2021-04-29T10:00:05Z",
         "user_id":1,
         "symbol":"ZECUSD"
      }
   ],
   "success":true,
   "type":"positions",
   "action":"snapshot"
}
```

## Orders
Channel provides updates when any order is updated for any action such as fill, quantity change. Need to pass list of product symbols while subscribing.

A snapshot of all open/pending orders will be sent after subscribing a symbol. And all incremental updates will be sent on create/update/delete of orders

All updates including snapshot will have incremental seq_id. seq_id is separate for each symbol.

Any of the following events can be tracked by the reason field in this channel

- fill
- stop_update
- stop_trigger
- stop_cancel
- liquidation
- self_trade


You need to send the list of symbols for which you would like to subscribe to orders channel. You can also subscribe to orders
updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to orders channel without specifying the symbols list, you will not receive any data.

> Orders Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "orders",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}
```
```json
// Order update

{
    "type": "orders",
    "action": "create",                 // "create"/"update"/"delete"
    "reason": "",                       // "fill"/"stop_update"/"stop_trigger"/"stop_cancel"/"liquidation"/"self_trade"/null
    "symbol": "BTCUSD",           // Product Symbol
    "product_id": 27,                    // Product ID
    "order_id": 1234,                    // Order id
    "client_order_id": "",              // Client order id
    "size": 100,                        // Order size
    "unfilled_size": 55,                // Unfilled size
    "average_fill_price": "8999.00",     // nil for unfilled orders
    "limit_price": "9000.00",                  // Price of the order
    "side": "buy",                       // Order side (buy or sell)
    "cancellation_reason": "cancelled_by_user",        // Cancellation reason in case of cancelled order, null otherwise
    "stop_order_type": "stop_loss_order",             // If a Stop Order -> "stop_loss_order"/"take_profit_order", null otherwise
    "bracket_order": false,              // true for a bracket_order, false otherwise
    "state": "open",                     // "open"/"pending"/"closed"/"cancelled"
    "seq_no": 1,                         // Incremental sequence number
    "timestamp": 1594105083998848,       // Unix timestamp in microseconds
    "stop_price": "9010.00",                             // stop_price of stop order        
    "trigger_price_max_or_min": "9020.00",               // for trailing stop orders
    "bracket_stop_loss_price": "8090.00",
    "bracket_stop_loss_limit_price": "8090.00",
    "bracket_take_profit_price": "9020",      
    "bracket_take_profit_limit_price": "9020",
    "bracket_trail_amount": "10.00"
}
```

```json
// Snapshot
{
  "meta": {
    "seq_no": 7,
    "timestamp": 1594149235554045
  },
  "result": [
    {
      "id": 1592130,
      "limit_price": "9000",
      "order_type": "limit_order",
      "product_id": 13,
      "reduce_only": false,
      "side": "buy",
      "size": 1,
      "state": "open",
      "stop_order_type": null,
      "stop_price": null,
      "time_in_force": "gtc",
      "trail_amount": null,
      "unfilled_size": 1,
      "average_fill_price": "8999.00",
      "user_id": 1132
    }
  ],
  "success": true,
  "symbol": "BTCUSD",
  "type": "orders",
  "action": "snapshot"
}
```

## UserTrades
Please use "v2/user_trades" channel for better latency.

Channel provides updates for fills. Need to pass list of product symbols while subscribing.

All updates will have incremental seq_id. seq_id is separate for each symbol.

Auto Deleverage Liquidations of a position can be tracked by reason: "adl" in the user_trades channel.
You need to send the list of symbols for which you would like to subscribe to user trades channel. You can also subscribe to user trades
updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to user trades channel without specifying the symbols list, you will not receive any data.

> User Trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "user_trades",
                "symbols": ["BNBBTC_30Nov"]
            }
        ]
    }
}
```
```json
// user_trades
{
    "symbol": "BNBBTC_30Nov",
    "fill_id": "1234-abcd-qwer-3456",
    "reason": "normal",                      // "normal" or "adl"
    "product_id": 7,
    "type": "user_trades",
    "user_id": 1998,
    "order_id": 3283999,
    "side": "buy",
    "size": 190,
    "price": "0.00145791",
    "role": "taker",
    "client_order_id": "GA123",
    "timestamp": 1544091555086559,
    "seq_no": 1
}
    
```

## v2/user_trades
Channel provides updates for fills. Need to pass list of product symbols while subscribing. This channel is similar to user_trades channel, only difference is that, it is faster than user_trades and doesn't contain commission data.

All updates will have incremental sequence_id. sequence_id is separate for each symbol, useful for identifying if any v2/user_trades messages were missed/dropped. The sequence_id will reset to 1 after our systems restart. (usually after maintainaince/market disruption).

Auto Deleverage Liquidations of a position can be tracked by reason: "adl".
Liquidation of a position can be tracked by reason: "liquidation".  
You need to send the list of symbols for which you would like to subscribe to v2/user_trades channel. You can also subscribe to v2/user_trades updates for category of products by sending [category-names](/#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.  
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.  
Please note that if you subscribe to v2/user_trades channel without specifying the symbols list, you will not receive any data.

> v2/user_trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/user_trades",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}
```
```json
// v2/user_trades
{
    "type": "v2/user_trades",
    "sy": "BTCUSD",              // symbol
    "f": "1234-abcd-qwer-3456",  // fill_id
    "R": "normal",               // reason: "normal", "adl", "liquidation"
    "u": 1998,                   // user_id
    "o": 3283999,                // order_id
    "S": "buy",                  // side: "buy" or "sell"
    "s": 190,                    // size in contracts
    "p": "17289.2",              // price
    "po": 5,                     // position (in contracts) after this fill.
    "r": "taker",                // role: "taker" or "maker"
    "c": "GA123",                // client_order_id
    "t": 1685794274866438,       // timestamp of fill creation
    "se": 4                      // incremental sequence_no
}
    
```

## PortfolioMargins
Channel provides updates for portfolio margin values of the selected sub-account. These updates are sent every 2 seconds. In case portfolio margin is not enabled on the selected sub-account, no updates will be sent on this channel.

For detailed description of portfolio margin please see [user guide](https://guides.delta.exchange/delta-exchange-user-guide/trading-guide/margin-explainer/portfolio-margin)

UCF: is unrealised cashflows of your portfolio. These are the cashflows (negative for outgoing and positive for incoming) that will take place if all the positions in your portfolio are closed at prevailing mark prices.

> Portfolio Margin Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "portfolio_margins",
                "symbols": [".DEXBTUSD"]
            }
        ]
    }
}
```
```json
// portfolio margin update

{
    "type": "portfolio_margins",
    "user_id": 1,
    "asset_id": 2,                   // BTC
    "index_symbol": ".DEXBTUSD",
    "liquidation_risk": false,
    "blocked_margin": "100", // Margin blocked for current portfolio. Same as portfolio_margin in margins channel.
    "mm_wo_ucf": "80",
    "mm_w_ucf": "80",
    "im_wo_ucf": "100",
    "im_w_ucf": "100",
    "positions_upl": "0", 
    "risk_margin": "100",
    "risk_matrix":{"down":[{"is_worst":false,"pnl":"230.03686162","price_shock":"10"}],"unchanged":[{"is_worst":false,"pnl":"230.03686162","price_shock":"10"}],"up":[]},
    "futures_margin_floor": "20",
    "short_options_margin_floor": "20",
    "long_options_margin_floor": "20",
    "under_liquidation": false,
    "commission": "3.444",
    "margin_floor": "60",
    "timestamp": 1544091555086559, //timestamp in microseconds
    "margin_shortfall": "4.5"             // key sent when liquidation_risk is true 
}

```

Keys - 

<dl>
    <dt>index_symbol</dt>
    <dd>This is the coin on which portfolio margin is enabled.</dd>
    <dt>positions_upl</dt>
    <dd>This is unrealised cashflows (UCF) of your portfolio. These are the cashflows (negative for outgoing and positive for incoming) that will take place if all the positions in your portfolio are closed at prevailing mark prices. Unrealised cashflow is positive for long options and negative for short options.</dd>
    <dt>im_w_ucf</dt>
    <dd>This is the initial margin (IM) requirement for the portfolio. IM is computed as max(risk_margin, margin_floor) - UCF.</dd>
    <dd>If UCF > max(risk_margin, margin_floor) then IM is negative. Negative margin requirement results in increase in your balance available for trading.</dd>
    <dd>If the Wallet Balance (ex spot orders) is less than IM then you would only be able to place orders that reduce the risk of the portfolio.</dd>
    <dt>im_wo_ucf</dt>
    <dd>This is IM without UCF.</dd>
    <dt>mm_w_ucf</dt>
    <dd>This is the maintenance margin (MM) requirement for the portfolio. MM is computed as 80% * max(risk_margin, margin_floor) - UCF.</dd>
    <dd>If the Wallet Balance (ex spot orders) is less than MM then the portfolio will go into liquidation.</dd>
    <dd></dd>
    <dt>mm_wo_ucf</dt>
    <dd>This is MM without UCF.</dd>
    <dt>commission</dt>
    <dd>This is the trading fees blocked for the open orders/positions (for closing the positions) in the portfolio.</dd>
    <dd>This is in addition to the IM requirement.</dd>
    <dt>blocked_margin</dt>
    <dd>The margin actually blocked for your portfolio. If your Wallet Balance (ex spot orders) is greater than IM + commission then blocked_margin = IM + commissions. Otherwise blocked_margin is equal to the maximum amout we are able to block to meet the portfolio margin requirement.</dd>
    <dd>If blocked_margin < MM then the portfolio goes into liquidation.</dd>
    <dt>liquidation_risk</dt>
    <dd>This flag indicates if the portfolio is at liquidation risk.</dd>
    <dd>This flag is set to TRUE when blocked_margin < im_w_ucf + commissions.</dd>
    <dt>under_liquidation</dt>
    <dd>This flag is set to TRUE when the portfolio is under liquidation.</dd>
    <dt>margin_shortfall</dt>
    <dd>This is the minimum topup amount needed to bring the portfolio out of liquidation risk state.</dd>
    <dt>risk_margin</dt>
    <dd>The maximum likely loss of the portfolio under the various simulated stress scenarios.</dd>
    <dt>risk_matrix</dt>
    <dd>Matrix showing the profit/loss of the portfolio under various simulated stress scenarios.</dd>
    <dd> Profit/loss for each position and open order is computed with reference to the prevailing mark prices. Positive numbers indicate profit and negative numbers indicate loss.</dd>
    <dt>margin_floor</dt>
    <dd>Margin Floor is the minimum risk_margin required for a portfolio. </dd>
    <dd>It is comprised of sum of futures_margin_floor, long_options_margin_floor, short_options_margin_floor</dd>
</dl>

## MMP Trigger
Channel provides updates when MMP is triggered. Market maker protection is available to registered market makers by default. Others can reach out to support for getting access to MMP. More info [here](https://guides.delta.exchange/delta-exchange-user-guide/market-makers-guide/market-maker-protection).  

> MMP Trigger Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "mmp_trigger"
            }
        ]
    }
}
```
```json
// mmp_trigger response
{
    "user_id": 1,
    "asset": "BTC",
    "frozen_till": 1561634049751430     # timestamp is microseconds, will be -1 if manual reset is enabled 
}
```