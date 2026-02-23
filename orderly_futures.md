orderly
Introduction
We provide two interfaces to communicate between Orderly and clients.
RESTful API interface: Provides sending events like create order, cancel order, fetch balance, etc.
Websocket interface: Provides real-time orderbook data feed and order update feed.
​
Base endpoints
https://api.orderly.org/ (Mainnet)
https://testnet-api.orderly.org (Testnet)
​
General Information on REST Endpoints
For GET and DELETE endpoints, parameters must be sent as a query string.
For POST and PUT endpoints, the parameters must be sent in the request body with content type application/json.
Parameters may be sent in any order.
​
Authorization
All our private interfaces require signing via cryptographically secure keys for authentication, also known as Orderly key.
Please set the corresponding header in your request. Please refer to API authentication for more information.
​
Symbol
Orderly uses the format of PERP_<SYMBOL>_USDC to represent a symbol name, for example: PERP_ETH_USDC.
​
Rate Limit
Rate limit is counted using the Orderly key. If your application reached the rate limit of certain endpoint, the server will return an error result with http code 429. You may need wait until next time horizon.
​
Error Message
Errors consist of three parts: an error code, detailed message and a success flag.
{
  "success": false,
  "code": -1005, // Error code
  "message": "order_price must be a positive number" // Detail message  
}
All API will return following json when api fails, the “message” will contain the detail error message, it may be because some data are in wrong format, or other reasons.
Specific error codes and messages are defined in Error Codes.






curl --request GET \
  --url https://api.orderly.org/v1/public/volume/stats

200
{
  "success": true,
  "data": {
    "perp_volume_ytd": 274148.0364,
    "perp_volume_ltd": 274148.0364,
    "perp_volume_today": 120272.7674,
    "perp_volume_last_1_day": 120272.7674,
    "perp_volume_last_7_days": 120272.7674,
    "perp_volume_last_30_days": 300730.5454
  },
  "timestamp": 1702989203989
}
Builder Info
Get Builder Volume
Limit: 10 requests per 1 second per IP address

GET /v1/public/volume/stats

Get the latest volume statistics of Orderly and its associated builders. Note that for builder volume, the volume is counted as the sum of the maker and taker volume, while for the full Orderly platform, the volume is the total amount matched on the platform (ie taker and maker are not double-counted.)

GET

https://api.orderly.org
/
v1
/
public
/
volume
/
stats

Try it
Query Parameters
​
broker_id
string
Provide broker_id to obtain statistics of a specific builder

Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989

Error Codes
Get Builder List
Ask a question...



Get Builder List

curl --request GET \
  --url https://api.orderly.org/v1/public/broker/name

200
{
  "success": true,
  "data": {
    "rows": [
      {
        "broker_id": "woofi_pro",
        "broker_name": "WOOFi Pro"
      }
    ]
  },
  "timestamp": 1702989203989
}



Get Builder Stats

curl --request GET \
  --url https://api.orderly.org/v1/public/broker/stats

200
{
  "success": true,
  "data": {
    "rows": [
      {
        "connected_user": "274148"
      }
    ]
  },
  "timestamp": 1702989203989
}








curl --request GET \
  --url https://api.orderly.org/v1/public/chain_info

200
{
  "success": true,
  "data": {
    "rows": [
      {
        "name": "Arbitrum",
        "public_rpc_url": "https://arb1.arbitrum.io/rpc",
        "chain_id": "42161",
        "currency_symbol": "ETH",
        "explorer_base_url": "https://arbiscan.io",
        "vault_address": "0x816f722424B49Cf1275cc86DA9840Fbd5a6167e9",
        "currency_decimal": 18,
        "broker_ids": [
          "woofi_pro"
        ]
      }
    ]
  },
  "timestamp": 1702989203989
}






curl --request GET \
  --url https://api.orderly.org/v1/public/futures_market

200
{
  "success": true,
  "data": {
    "rows": [
      {
        "symbol": "PERP_ETH_USDC",
        "index_price": 1901.6,
        "mark_price": 1950,
        "sum_unitary_funding": 387.891,
        "est_funding_rate": 0.00046875,
        "last_funding_rate": 0.00046875,
        "next_funding_time": 1683270060000,
        "open_interest": "None",
        "24h_open": 2115,
        "24h_close": 2115,
        "24h_high": 2115,
        "24h_low": 2115,
        "24h_amount": 0,
        "24h_volume": 0
      }
    ]
  },
  "timestamp": 1702989203989
}
Builder Info
Get Market Volume by Builder
Limit: 10 requests per 1 second per IP address

GET /v1/public/futures_market

Get market volume filtered by broker.

GET

https://api.orderly.org
/
v1
/
public
/
futures_market

Try it
Query Parameters
​
symbol
string
​
broker_id
string
Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989

Get Supported Chains per Builder
Get TVL by Builder
Ask a question...

twitter
linkedin
discord
medium
Powered by







Get TVL by Builder

curl --request GET \
  --url https://api.orderly.org/v1/public/balance/stats

200
{
  "success": true,
  "data": {
    "total_holding": 100,
    "total_unsettled_balance": 21,
    "last_update_time": 1702989203989
  },
  "timestamp": 1702989203989
}




Get Positions Under Liquidation

curl --request GET \
  --url https://api.orderly.org/v1/public/liquidation

200
{
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "timestamp": 1685298157704,
        "type": "liquidated",
        "liquidation_id": 1730,
        "positions_by_perp": [
          {
            "symbol": "PERP_BTC_USDC",
            "position_qty": -0.22457,
            "liquidator_fee": 0.015
          }
        ]
      }
    ]
  },
  "timestamp": 1702989203989
}
Liquidations
Get Positions Under Liquidation
Limit: 10 requests per 1 second per IP address

GET /v1/public/liquidation

GET

https://api.orderly.org
/
v1
/
public
/
liquidation

Try it
Query Parameters
​
start_t
number
start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
end_t
number
end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
page
integer
the page you wish to query. start from 1

​
size
integer
Default: 60

Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989

Get All Trades of Specific Algo Order
Get Liquidated Positions Info
Ask a question...

twitter
linkedin
discord
medium
Powered by



Get Liquidated Positions Info

curl --request GET \
  --url https://api.orderly.org/v1/public/liquidated_positions

200
{
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "timestamp": 1683802462092,
        "liquidation_id": 29,
        "transfer_amount_to_insurance_fund": 0,
        "positions_by_perp": [
          {
            "symbol": "PERP_ETH_USDC",
            "position_qty": 0,
            "liquidator_fee": 0.015,
            "cost_position_transfer": 0,
            "transfer_price": 1860,
            "insurance_fund_fee": 0.011999,
            "abs_insurance_fund_fee": 0,
            "seq": 1730181536341943600,
            "abs_liquidator_fee": 0
          }
        ],
        "type": "liquidated"
      }
    ]
  },
  "timestamp": 1702989203989
}
Liquidations
Get Liquidated Positions Info
Limit: 10 requests per 1 second per IP address

GET /v1/public/liquidated_positions

GET

https://api.orderly.org
/
v1
/
public
/
liquidated_positions

Try it
Query Parameters
​
symbol
string
​
start_t
string
​
end_t
string
​
page
string
start from 1

​
size
string
Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989

Get Positions Under Liquidation
Get Liquidated Positions by Liquidator
Ask a question...

twitter
linkedin
discord
medium
Powered by


Get Liquidated Positions by Liquidator

curl --request GET \
  --url https://api.orderly.org/v1/client/liquidator_liquidations \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'

200
{
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "liquidation_id": 1728,
        "timestamp": 1685154032762,
        "type": "liquidated",
        "assigned": 1,
        "positions_by_perp": [
          {
            "symbol": "PERP_BTC_USDC",
            "abs_liquidator_fee": 1.152279,
            "cost_position_transfer": 21.002786,
            "liquidator_fee": 0.006,
            "position_qty": 0.00017,
            "transfer_price": 123545.8
          }
        ]
      }
    ]
  },
  "timestamp": 1702989203989
}




curl --request GET \
  --url https://api.orderly.org/v1/liquidations \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "liquidation_id": 101,
        "timestamp": 1663313562090,
        "transfer_amount_to_insurance_fund": 0,
        "margin_ratio": 0.10436069,
        "account_mmr": 0.012,
        "position_notional": 28.415534,
        "collateral_value": 2.965465,
        "positions_by_perp": [
          {
            "total_position": 41.6,
            "symbol": "PERP_BTC_USDC",
            "position_qty": 0.00017,
            "liquidator_fee": 0.006,
            "cost_position_transfer": 21.002786,
            "transfer_price": 123545.8,
            "insurance_fund_fee": 0.006,
            "abs_insurance_fund_fee": 0.126017,
            "mark_price": 123400,
            "abs_liquidator_fee": 0.252034
          }
        ]
      }
    ]
  },
  "timestamp": 1702989203989
}






curl --request POST \
  --url https://api.orderly.org/v1/liquidation \
  --header 'Content-Type: application/json' \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>' \
  --data '
{
  "liquidation_id": 123,
  "ratio_qty_request": 123,
  "limit_price": {
    "symbol": 123
  },
  "extra_liquidation_ratio": 123,
  "symbols": {
    "ratio_qty_request": 123,
    "symbol": "<string>"
  }
}
'


{
  "success": true,
  "data": {
    "liquidation_id": 123,
    "timestamp": 123,
    "type": "<string>",
    "positions_by_perp": [
      {
        "symbol": "PERP_BTC_USDC",
        "abs_liquidator_fee": 1.152279,
        "cost_position_transfer": 21.002786,
        "liquidator_fee": 0.006,
        "position_qty": 0.00017,
        "transfer_price": 123545.8
      }
    ]
  },
  "timestamp": 1702989203989
}


curl --request POST \
  --url https://api.orderly.org/v1/claim_insurance_fund \
  --header 'Content-Type: application/json' \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>' \
  --data '
{
  "claim_id": 123,
  "symbol": "<string>",
  "qty_request": 123,
  "limit_price": {
    "symbol": 123
  }
}
'

{
  "success": true,
  "data": {
    "liquidation_id": 101,
    "timestamp": 1663313562090,
    "positions_by_perp": [
      {
        "symbol": "PERP_BTC_USDC",
        "abs_liquidator_fee": 1.152279,
        "cost_position_transfer": 21.002786,
        "liquidator_fee": 0.006,
        "position_qty": 0.00017,
        "transfer_price": 123545.8
      }
    ]
  },
  "timestamp": 1702989203989
}



curl --request GET \
  --url https://api.orderly.org/v1/asset/history \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'



  {
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "id": "230707030600002",
        "tx_id": "0x4b0714c63cc7abae72bf68e84e25860b88ca651b7d27dad1e32bf4c027fa5326",
        "side": "WITHDRAW",
        "token": "USDC",
        "amount": 555,
        "fee": 0,
        "trans_status": "FAILED",
        "created_time": 1688699193034,
        "updated_time": 1688699193096,
        "chain_id": "986532"
      }
    ]
  },
  "timestamp": 1702989203989
}


curl --request GET \
  --url https://api.orderly.org/v1/client/holding \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "holding": [
      {
        "updated_time": 1580794149000,
        "token": "USDT",
        "holding": 282485.071904,
        "frozen": 0,
        "pending_short": -2000
      }
    ]
  },
  "timestamp": 1702989203989
}




curl --request GET \
  --url https://api.orderly.org/v1/withdraw_nonce \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "withdraw_nonce": 1
  },
  "timestamp": 1702989203989
}


curl --request GET \
  --url https://api.orderly.org/v1/settle_nonce \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'

  {
  "success": true,
  "data": {
    "settle_nonce": 1
  },
  "timestamp": 1702989203989
}


https://api.orderly.org
/
v1
/
settle_nonce



Get PnL Settlement History

curl --request GET \
  --url https://api.orderly.org/v1/pnl_settlement/history \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'

200
{
  "success": true,
  "data": {
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    },
    "rows": [
      {
        "id": 10001,
        "old_balance": 4050,
        "new_balance": 3050,
        "settled_amount": -500,
        "requested_time": 1575014255089,
        "settled_time": 1575014255910,
        "symbols": [
          {
            "symbol": "PERP_BTC_USDC",
            "settled_amount": -500
          }
        ]
      }
    ]
  },
  "timestamp": 1702989203989
}
https://api.orderly.org/v1/pnl_settlement/history



curl --request GET \
  --url https://api.orderly.org/v1/positions \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "current_margin_ratio_with_orders": 1.2385,
    "free_collateral": 450315.09115,
    "initial_margin_ratio": 0.1,
    "initial_margin_ratio_with_orders": 0.1,
    "maintenance_margin_ratio": 0.05,
    "maintenance_margin_ratio_with_orders": 0.05,
    "margin_ratio": 1.2385,
    "open_margin_ratio": 1.2102,
    "total_collateral_value": 489865.71329,
    "total_pnl_24_h": 0,
    "rows": [
      {
        "IMR_withdraw_orders": 0.1,
        "MMR_with_orders": 0.05,
        "average_open_price": 27908.14386047,
        "cost_position": -139329.358492,
        "est_liq_price": 117335.92899428,
        "fee_24_h": 0,
        "imr": 0.1,
        "last_sum_unitary_funding": 70.38,
        "mark_price": 27794.9,
        "mmr": 0.05,
        "pending_long_qty": 0,
        "pending_short_qty": 0,
        "pnl_24_h": 0,
        "position_qty": -5,
        "settle_price": 27865.8716984,
        "symbol": "PERP_BTC_USDC",
        "seq": 1730181536341943600,
        "timestamp": 1685429350571,
        "updated_time": 1685429350571,
        "unsettled_pnl": 354.858492,
        "leverage": 10
      }
    ]
  },
  "timestamp": 1702989203989
}

https://api.orderly.org/v1/positions





Get One Position Info
Limit: 30 requests per 10 second per user

GET /v1/position/{symbol}

GET

https://api.orderly.org
/
v1
/
position
/
{symbol}

curl --request GET \
  --url https://api.orderly.org/v1/position/{symbol} \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "IMR_withdraw_orders": 0.1,
    "MMR_with_orders": 0.05,
    "average_open_price": 27908.14386047,
    "cost_position": -139329.358492,
    "est_liq_price": 117335.92899428,
    "fee_24_h": 0,
    "imr": 0.1,
    "last_sum_unitary_funding": 70.38,
    "mark_price": 27794.9,
    "mmr": 0.05,
    "pending_long_qty": 0,
    "pending_short_qty": 0,
    "pnl_24_h": 0,
    "position_qty": -5,
    "settle_price": 27865.8716984,
    "symbol": "PERP_BTC_USDC",
    "seq": 1730181536341943600,
    "timestamp": 1685429350571,
    "updated_time": 1685429350571,
    "unsettled_pnl": 354.858492,
    "leverage": 10
  },
  "timestamp": 1702989203989
}



Get Position History
Limit: 10 requests per 1 second per user

GET /v1/position_history

GET

https://api.orderly.org
/
v1
/
position_history

Try i




curl --request GET \
  --url https://api.orderly.org/v1/position_history \
  --header 'orderly-account-id: <orderly-account-id>' \
  --header 'orderly-key: <orderly-key>' \
  --header 'orderly-signature: <orderly-signature>' \
  --header 'orderly-timestamp: <orderly-timestamp>'


  {
  "success": true,
  "data": {
    "rows": [
      {
        "position_id": 1,
        "status": "closed",
        "type": "liquidated",
        "symbol": "PERP_ETH_USDC",
        "avg_open_price": 61016.1,
        "avg_close_price": 61016.1,
        "max_position_qty": 56.6,
        "closed_position_qty": 56.6,
        "side": "LONG",
        "trading_fee": 0.015,
        "accumulated_funding_fee": 0.11,
        "insurance_fund_fee": 0,
        "liquidator_fee": 0,
        "liquidation_id": null,
        "realized_pnl": -9.09691927314905,
        "open_timestamp": 1685429350571,
        "close_timestamp": 1685429350571,
        "last_update_timestamp": 1685429350571,
        "leverage": 10
      }
    ]
  },
  "timestamp": 1702989203989
}


























Funding Rates
Get Funding Rate History for One Market
Limit: 10 requests per 1 second per IP address

GET /v1/public/funding_rate_history

Get funding rate history for one market.

GET

https://api.orderly.org
/
v1
/
public
/
funding_rate_history

Try it
Query Parameters
​
symbol
stringrequired
​
start_t
number
start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
end_t
number
end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
page
number
the page you wish to query. start from 1

​
size
number
Default: 60

Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989




Funding Rates
Get Funding Rate History for One Market
Limit: 10 requests per 1 second per IP address

GET /v1/public/funding_rate_history

Get funding rate history for one market.

GET

https://api.orderly.org
/
v1
/
public
/
funding_rate_history

Try it
Query Parameters
​
symbol
stringrequired
​
start_t
number
start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
end_t
number
end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.

​
page
number
the page you wish to query. start from 1

​
size
number
Default: 60

Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989

{
  "success": true,
  "data": {
    "rows": [
      {
        "symbol": "PERP_ETH_USDC",
        "funding_rate": 0.0001,
        "funding_rate_timestamp": 1684224000000,
        "next_funding_time": 1684252800000
      }
    ],
    "meta": {
      "total": 9,
      "records_per_page": 25,
      "current_page": 1
    }
  },
  "timestamp": 1702989203989
}










Get Predicted Funding Rate for One Market
Limit: 30 requests per 1 second per IP address

GET /v1/public/funding_rate/{symbol}

Get latest funding rate for one market.

GET

https://api.orderly.org
/
v1
/
public
/
funding_rate
/
{symbol}

Try it
Path Parameters
​
symbol
stringrequired
Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989



curl --request GET \
  --url https://api.orderly.org/v1/public/funding_rate/{symbol}

curl --request GET \
  --url https://api.orderly.org/v1/public/funding_rate/{symbol}




  Funding Rates
Get Predicted Funding Rates for All Markets
Limit: 10 requests per 1 second per IP address

GET /v1/public/funding_rates

Get predicted funding rates for all futures trading pairs.

Get the :

last_funding_rate : latest hourly funding rate for all the markets for the last funding period (dt = 8h)
est_funding_rate : rolling average of all funding rates over the last 8 hours


curl --request GET \
  --url https://api.orderly.org/v1/public/funding_rates


{
  "success": true,
  "data": {
    "rows": [
      {
        "symbol": "PERP_ETH_USDC",
        "est_funding_rate": 0,
        "est_funding_rate_timestamp": 1683880020000,
        "last_funding_rate": 0.0001,
        "last_funding_rate_timestamp": 1683878400000,
        "next_funding_time": 1683907200000,
        "sum_unitary_funding": 521.367
      }
    ]
  },
  "timestamp": 1702989203989
}


Funding Rates
Get Funding Rate for All Markets
Limit: 10 requests per 1 second per IP address

GET /v1/public/market_info/funding_history

GET

https://api.orderly.org
/
v1
/
public
/
market_info
/
funding_history

Try it
Response
200 - application/json
Success

​
success
booleanrequired
Example:
true

​
data
objectrequired
Show child attributes

​
timestamp
integer
Example:
1702989203989


curl --request GET \
  --url https://api.orderly.org/v1/public/market_info/funding_history



  {
  "success": true,
  "data": {
    "rows": [
      {
        "symbol": "PERP_BTC_USDC",
        "data_start_time": "2022-01-01 00:00:00",
        "funding": {
          "last": {
            "rate": 0.00234,
            "positive": 1,
            "negative": 0
          },
          "1d": {
            "rate": -0.00828,
            "positive": 10,
            "negative": 10
          },
          "3d": {
            "rate": -0.00412,
            "positive": 9,
            "negative": 11
          },
          "7d": {
            "rate": 0.00012,
            "positive": 8,
            "negative": 12
          },
          "14d": {
            "rate": 0.00156,
            "positive": 7,
            "negative": 13
          },
          "30d": {
            "rate": 0.00345,
            "positive": 6,
            "negative": 14
          },
          "90d": {
            "rate": 0.01023,
            "positive": 5,
            "negative": 15
          },
          "180d": {
            "rate": 0.01567,
            "positive": 4,
            "negative": 16
          }
        }
      }
    ]
  },
  "timestamp": 1702989203989
}





























































Websocket API
Websocket API
​
Market Data Base Endpoints:
Mainnet: wss://ws-evm.orderly.org/ws/stream/{account_id}
Testnet: wss://testnet-ws-evm.orderly.org/ws/stream/{account_id}
{account_id} is your account id.
Users can subscribe/unsubscribe to the following topics: orderbook, orderbookupdate, trade, ticker, tickers, bbo, bbos, estfundingrate, indexprice, indexprices, liquidation, markprice, markprices, openinterest, kline_1m, kline_5m, kline_15m, kline_30m, kline_1h, kline_1d, kline_1w, kline_1M
​
Private User Data Stream Base Endpoints:
Mainnet: wss://ws-private-evm.orderly.org/v2/ws/private/stream/{account_id}
Testnet: wss://testnet-ws-private-evm.orderly.org/v2/ws/private/stream/{account_id}
{account_id} is your account id
Users need to be authenticated before subscribing to any topic. They would be disconnected if authentication fails. For more information, refer to the Authentication section.
Users can subscribe/unsubscribe to the following topics: account, balance, executionreport, liquidationsaccount, liquidatorliquidations, notifications, settle, position, wallet
Get Kline History









Websocket API
PING/PONG
The server will send a ping command to the client every 10 seconds. If the pong from client is not received within 10 seconds for 10 consecutive times, it will actively disconnect the client.
The client can also send ping every 10s to keep alive.
Name	Type	Required	Description
event	string	Y	ping/pong


{
    "event":"pong",
    "ts":1614667590000
}



Authentication
Refer to API authentication for more details about how to sign the request with orderly-key and orderly-secret. The request method, request path, and request body are all blank. The message to sign is therefore just the timestamp.
wsprivate can now authenticate when creating the connection by appending the content of auth request into the subscription url in the form of query string.
For example, wss://ws-private-evm.orderly.org/v2/ws/private/stream/0xd7379678a303b57d7d43eb23c64dd7528ac8cb4efe983a3aedcfe9b4aa4cb984?orderly_key=xxxxxxxx&timestamp=xxxxx&sign=xxxxx will authenticate the user when creating the connection, no need to send auth request again.
Name	Type	Required	Description
orderly_key	string	Y	Orderly Key
sign	string	Y	signature
timestamp	timestamp	Y	timestamp




{
    "id":"123r",
    "event":"auth",
    "params":{
        "orderly_key":"ed25519:CUS69ZJOXwSV38xo...",
        "sign":"4180da84117fc9753b...",
        "timestamp":1621910107900
    }
}



{
    "id":"123r",
    "event":"auth",
    "success":true,
    "ts":1621910107315
}




Websocket API
Error Response
Example response if there is an error.
You can use the id field in response to map the error response with the request.
{
    "id": "clientID7",
    "event": "subscribe",
    "success": false,
    "ts": 1614141150601,
    "errorMsg": "invalid symbol SPOT_WOO_USDC.e"
}
Example response if there is an error.





Public Market Data
Request orderbook
​
Request orderbook
{
    "id": "clientID2",
    "topic": "PERP_NEAR_USDC@orderbookupdate",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generated by client
event	string	Y	request
params.type	string	Y	orderbook
params.symbol	string	Y	{symbol}


{
    "id": "clientID1",
    "event": "request",
    "params": {
        "type": "orderbook",
        "symbol": "PERP_NEAR_USDC"
    }
}



{
    "id":"123r",
    "event":"request",
    "success":true,
    "ts":1618880432419,
    "data":{
        "symbol":"PERP_NEAR_USDC",
        "ts":1618880432380,
        "asks":[
            [
                15,
                0.443951
            ],
            [
                15.02,
                0.002566
            ],
            ...
        ],
        "bids":[
            [
                14.99,
                2.887466
            ],
            [
                14.76,
                2.034711
            ],
           ...
        ]
    }
}



Public Market Data
Orderbook
{symbol}@orderbook depth 100 push every 1s
{
    "id": "clientID2",
    "topic": "PERP_WOO_USDC@orderbook",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	Y	{symbol}@orderbook
params.symbol	string	Y	{symbol}
Request orderbook
Order book update


{
    "id": "clientID2",
    "event": "subscribe",
    "success": true,
    "ts": 1609924478533
}



{
    "topic": "PERP_WOO_USDC@orderbook",
    "ts": 1614152140945,
    "data": {
        "symbol": "PERP_WOO_USDC",
        "asks": [
            [
                0.31075,
                2379.63
            ],
            [
                0.31076,
                4818.76
            ],
            [
                0.31078,
                8496.1
            ],
            ...
        ],
        "bids": [
            [
                0.30891,
                2469.98
            ],
            [
                0.3089,
                482.5
            ],
            [
                0.30877,
                20
            ],
            ...
        ]
    }
}









Order book update
{symbol}@orderbookupdate updated orderbook push every 200ms
{
    "id": "clientID2",
    "topic": "PERP_NEAR_USDC@orderbookupdate",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	Y	{symbol}@orderbooku



{
    "id": "clientID2",
    "event": "subscribe",
    "success": true,
    "ts": 1609924478533
}


{
    "topic":"PERP_NEAR_USDC@orderbookupdate",
    "ts":1618826337580,
    "data":{
        "symbol":"PERP_NEAR_USDC",
        "prevTs":1618826337380,
        "asks":[
            [
                15.15,
                3.92864
            ],
            [
                15.8,
                0
            ],
            ...
        ],
        "bids":[
            [
                14.2,
                1.03895025
            ],
            [
                13.6,
                1.0807
            ],
            ...
        ]
    }
}



Public Market Data
Trade
Push interval: real-time push
{
    "id": "clientID3",
    "topic": "PERP_WOO_USDC@trade",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	Y	{symbol}@trade


{
    "id": "clientID3",
    "event": "subscribe",
    "success": true,
    "ts": 1609924478533
}


{
    "topic":"PERP_WOO_USDC@trade",
    "ts":1618820361552,
    "data":{
        "symbol":"PERP_WOO_USDC",
        "price":0.37988,
        "size":300,
        "side":"BUY"
    }
}




Traders Open Interest
Push interval: every 1m
{
    "id": "clientID11",
    "topic": "traders_open_interests",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	N	traders_open_interest
Market Price Changes Info


{
   "id":"clientID11",
   "event":"subscribe",
   "success":true,
   "ts":1682242408023
}


{
  "topic": "traders_open_interests",
  "ts": 1618820615000,
  "data": [
    {
      "symbol": "PERP_BTC_USDC",
      "long_oi": 31000,
      "short_oi": 31000
    },
    {
      "symbol": "PERP_ETH_USDC",
      "long_oi": 31000,
      "short_oi": 31000
    }
  ]
}




Open interest
Push interval: push every 1 second if open interest change and 10 seconds force update even if no change.
{
    "id": "clientID10",
    "topic": "PERP_ETH_USDC@openinterest",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	N	{symbol}@openinterest




{
   "id":"clientID10",
   "event":"subscribe",
   "success":true,
   "ts":1682242071080
}




{
   "topic":"PERP_ETH_USDC@openinterest",
   "ts":1682242080006,
   "data":{
      "symbol":"PERP_ETH_USDC",
      "openInterest":1.2741
   }
}




Public Market Data
Estimated funding rate
Push interval: 15s
{
    "id": "clientID11",
    "topic": "PERP_ETH_USDC@estfundingrate",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	N	{symbol}@estfundingrate



{
   "id":"clientID11",
   "event":"subscribe",
   "success":true,
   "ts":1682242408023
}



{
   "topic":"PERP_ETH_USDC@estfundingrate",
   "ts":1682242440000,
   "data":{
      "symbol":"PERP_ETH_USDC",
      "fundingRate":0.00046875,
      "fundingTs":1682242440000
   }
}




Public Market Data
Liquidation push
Push interval: push on addition/removal/update from list within 1s
{
    "id": "clientID12",
    "topic": "liquidation",
    "event": "subscribe"
}
Parameters
Name	Type	Required	Description
id	string	Y	id generate by client
event	string	Y	subscribe/unsubscribe
topic	string	N	liquidation




{
   "id":"clientID12",
   "event":"subscribe",
   "success":true,
   "ts":1682243349558
}



{
   "topic":"liquidation",
   "ts":1684926668235,
   "data":[
      {
         "liquidationId":1,
         "timestamp":1684821114917,
         "type":"liquidated",
         "positionsByPerp":[
            {
               "symbol":"PERP_NEAR_USDC",
               "positionQty":12.6,
               "liquidatorFee":0.0175
            }
         ]
      },
      ...
   ]
}