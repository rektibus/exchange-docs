# Futures




## Futures Market Data


**GET** `{{host}}/contract/public/details?symbol=BTCUSDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


**GET** `{{host}}/contract/public/depth?symbol=BTCUSDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


**GET** `{{host}}/contract/public/market-trade?symbol=BTCUSDT&limit=10`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| limit | 10 | Count(Default 50; max 100;)
 |


**GET** `{{host}}/contract/public/open-interest?symbol=BTCUSDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


**GET** `{{host}}/contract/public/funding-rate?symbol=BTCUSDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


**GET** `{{host}}/contract/public/kline?symbol=BTCUSDT&step=1&start_time=1684737708&end_time=1684739708`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| step | 1 | K-Line step, default is 1 minute. step: 1, 3, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080
 |
| start_time | 1684737708 | Start time. Timestamps need to be in seconds |
| end_time | 1684739708 | End time. Timestamps need to be in seconds |


**GET** `{{host}}/contract/public/markprice-kline?symbol=BTCUSDT&step=1&start_time=1684737708&end_time=1684739708`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| step | 1 | K-Line step, default is 1 minute. step: 1, 3, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080
 |
| start_time | 1684737708 | Start time. Timestamps need to be in seconds |
| end_time | 1684739708 | End time. Timestamps need to be in seconds |


**GET** `{{host}}/contract/public/funding-rate-history?symbol=BTCUSDT&limit=10`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| limit | 10 | Number of results per request. The maximum is 100; The default is 100
 |


**GET** `{{host}}/contract/public/leverage-bracket?symbol=BTCUSDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


## Futures Account Data


**GET** `{{host}}/contract/private/assets-detail`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |


## Futures Trading


**GET** `{{host}}/contract/private/trade-fee-rate?symbol=BTCUSDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |


**GET** `{{host}}/contract/private/order?symbol=BTCUSDT&order_id=22060966632123123&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| order_id | 22060966632123123 | Order ID |
| account | futures |  |


**GET** `{{host}}/contract/private/order-history?symbol=BTCUSDT&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| start_time | 1662368173 | Start time, default is the last 7 days |
| end_time | 1662368179 | End time, default is the last 7 days |
| account | futures |  |
| order_id | 12321313123123123 | Order ID |
| client_order_id | 12321312321312321 | Client-defined OrderId
 |


**GET** `{{host}}/contract/private/get-open-orders?symbol=BTCUSDT&type=limit&order_state=all&limit=1`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| type | limit | Order type -limit -marke |
| order_state | all | Order state
-all(default)
- partially_filled |
| limit | 1 | The number of returned results, with a maximum of 100 and a default of 100
 |


**GET** `{{host}}/contract/private/current-plan-order?symbol=BTCUSDT&type=limit&plan_type=plan&limit=1`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| type | limit | Order type -limit -marke |
| plan_type | plan | Plan order type
-plan
- profit_loss
default all |
| limit | 1 | The number of returned results, with a maximum of 100 and a default of 100
 |


**GET** `{{host}}/contract/private/position?symbol=BTCUSDT&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| account | futures |  |


**GET** `{{host}}/contract/private/position-v2?symbol=BTCUSDT&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| account | futures |  |


**GET** `{{host}}/contract/private/position-risk?symbol=BTCUSDT&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| account | futures |  |


**GET** `{{host}}/contract/private/trades?symbol=BTCUSDT&account=futures`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| start_time | 1662368173 | Start time, default is the last 7 days |
| end_time | 1662368179 | End time, default is the last 7 days |
| account | futures |  |


**GET** `{{host}}/contract/private/transaction-history?symbol=BTCUSDT&flow_type=3&page_size=10`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTCUSDT | Symbol of the contract(like BTCUSDT) |
| start_time | 1662368173 | Start time, timestamp in ms
 |
| end_time | 1662368179 | End time, timestamp in ms
 |
| flow_type | 3 | Type
- 0 = All (default)
- 1 = Transfer
- 2 = Realized PNL
- 3 = Funding Fee
- 4 = Commission Fee
- 5 = Liquidation Clearance |
| page_size | 10 | Default 100; max 1000
 |
| account | futures |  |


**GET** `{{host}}/contract/private/get-position-mode`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| account | futures |  |


**POST** `{{host}}/account/v1/transfer-contract-list`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "currency":"USDT",
    "time_start":1684391137804,
    "time_end":1684392577804,
    "page":1,
    "limit":10,
    "recvWindow":5000
}
```


**POST** `{{host}}/contract/private/submit-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTCUSDT",
  "side":4,
  "mode":1,
  "type":"limit",
  "leverage":"1",
  "open_type":"isolated",
  "size":10,
  "price":"2000000"
}
```


**POST** `{{host}}/contract/private/modify-limit-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "order_id":220906179559421,
  "price":"1450",
  "size":1
}
```


**POST** `{{host}}/contract/private/cancel-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "order_id": "220906179559421"
}
```


**POST** `{{host}}/contract/private/cancel-orders`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT"
}
```


**POST** `{{host}}/contract/private/cancel-all-after`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "timeout": 10
}
```


**POST** `{{host}}/contract/private/submit-plan-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTCUSDT",
  "side":1,
  "mode":1,
  "type":"limit",
  "leverage":"1",
  "open_type":"isolated",
  "size":10,
  "trigger_price":"20000",
  "executive_price":"14500",
  "price_type":1,
  "price_way":1
}
```


**POST** `{{host}}/contract/private/modify-plan-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "client_order_id":"123456789",
  "order_id":"220906179559421",
  "trigger_price":"2000",
  "executive_price":"1450",
  "price_type":1,
  "type":"limit"
}
```


**POST** `{{host}}/contract/private/cancel-plan-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "order_id": "220906179559421"
}
```


**POST** `{{host}}/contract/private/submit-leverage`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "leverage":"5",
  "open_type":"isolated"
}
```


**POST** `{{host}}/account/v1/transfer-contract`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "currency":"USDT",
  "amount":"10",
  "type":"spot_to_contract",
  "recvWindow":5000
}
```


**POST** `{{host}}/contract/private/submit-tp-sl-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "side":2,
  "type":"take_profit",
  "size":10,
  "trigger_price":"2000",
  "executive_price":"1450",
  "price_type":1,
  "plan_category":1,
  "client_order_id":"123456789",
  "category":"limit"
}
```


**POST** `{{host}}/contract/private/modify-tp-sl-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "trigger_price":"2100",
  "executive_price":"2100",
  "price_type":2,
  "order_id":"37758000001",
  "client_order_id":"",
  "plan_category":2,
  "category": "limit"
}
```


**POST** `{{host}}/contract/private/modify-preset-plan-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"ETHUSDT",
  "order_id":"220609666322019",
  "preset_take_profit_price":"2000",
  "preset_stop_loss_price":"1900",
  "preset_take_profit_price_type":1,
  "preset_stop_loss_price_type":1
}
```


**POST** `{{host}}/contract/private/submit-trail-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTCUSDT",
  "side":1,
  "leverage":"10",
  "open_type":"isolated",
  "size":10,
  "activation_price":"2000",
  "callback_rate":"1",
  "activation_price_type":1
}
```


**POST** `{{host}}/contract/private/cancel-trail-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTCUSDT",
  "order_id": "220906179559421"
}
```


**POST** `{{host}}/contract/private/set-position-mode`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "position_mode":"hedge_mode"
}
```


## Main-Sub Account


### For Main-Account


**POST** `{{host}}/account/contract/sub-account/main/v1/sub-to-main`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca5",
    "amount":"1",
    "currency":"USDT",
    "subAccount":"subAccountName@xxx.com"
}
```


**POST** `{{host}}/account/contract/sub-account/main/v1/main-to-sub`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"USDT",
    "subAccount":"subAccountName@xxx.com"
}
```


**GET** `{{host}}/account/contract/sub-account/main/v1/transfer-list?subAccount=subAccountName@xxx.com&limit=1`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| subAccount | subAccountName@xxx.com |  |
| limit | 1 |  |


### For Sub-Account


**POST** `{{host}}/account/contract/sub-account/sub/v1/sub-to-main`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"USDT"
}
```


**GET** `{{host}}/account/contract/sub-account/main/v1/wallet?subAccount=subAccountName@xxx.com&currency=USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| subAccount | subAccountName@xxx.com |  |
| currency | USDT |  |


**GET** `{{host}}/account/contract/sub-account/v1/transfer-history?limit=1`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| limit | 1 |  |


## Futures Affiliate


**GET** `{{host}}/contract/private/affiliate/rebate-list?page=1&size=10&currency=USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| user_id | None | user ID
 |
| page | 1 | Page number
 |
| size | 10 | Number of records per page
 |
| currency | USDT | query currency
 |
| rebate_start_time | None | Query rebate start timestamp
 |
| rebate_end_time | None | Query rebate end timestamp
 |
| register_start_time | None | Query register start timestamp
 |
| register_end_time | None | Query register end timestamp
 |


**GET** `{{host}}/contract/private/affiliate/trade-list?user_id=123123121&page=1&size=10&type=1`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| user_id | 123123121 | user ID
 |
| page | 1 | Page number
 |
| size | 10 | Number of records per page
 |
| type | 1 | Query type:
-1=U-based
-2=Coin-based |
| start_time |  | Query start timestamp
 |
| end_time |  | Query end timestamp
 |
