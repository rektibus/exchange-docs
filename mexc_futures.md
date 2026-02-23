# MEXC V1 contract




## Quote


**GET** `{{api_url}}/api/v1/contract/ping`


**GET** `{{api_url}}/api/v1/contract/detail`


**GET** `https://contract.mexc.com/api/v1/contract/support_currencies`


**GET** `https://contract.mexc.com/api/v1/contract/support_currencies`


**GET** `https://contract.mexc.com/api/v1/contract/depth_commits/BTC_USDT/20`


**GET** `https://contract.mexc.com/api/v1/contract/depth_commits/BTC_USDT/20`


**GET** `https://contract.mexc.com/api/v1/contract/depth_commits/BTC_USDT/20`


**GET** `https://contract.mexc.com/api/v1/contract/depth_commits/BTC_USDT/20`


**GET** `https://contract.mexc.com/api/v1/contract/kline/BTC_USDT?interval=Min15&start=1609992674000&end=1652238485681`

| Parameter | Value | Description |
|-----------|-------|-------------|
| interval | Min15 |  |
| start | 1609992674000 |  |
| end | 1652238485681 |  |


**GET** `https://contract.mexc.com/api/v1/contract/kline/index_price/BTC_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| interval | Min15 | Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1 |
| start | 1609992674000 |  |
| end | 1609992694000 |  |


**GET** `https://contract.mexc.com/api/v1/contract/kline/fair_price/BTC_USDT?interval=Min15&start=1609992674000&end=1609992694000`

| Parameter | Value | Description |
|-----------|-------|-------------|
| interval | Min15 |  |
| start | 1609992674000 |  |
| end | 1609992694000 |  |


**GET** `https://contract.mexc.com/api/v1/contract/deals/BTC_USDT`


**GET** `https://contract.mexc.com/api/v1/contract/ticker`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | None |  |


**GET** `https://contract.mexc.com/api/v1/contract/risk_reverse`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | None |  |


**GET** `https://contract.mexc.com/api/v1/contract/risk_reverse/history?symbol=BTC_USDT&page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT |  |
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `{{api_url}}/api/v1/contract/funding_rate/history?symbol=BTC_USDT&page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT |  |
| page_num | 1 |  |
| page_size | 20 |  |


## Accounts and Transactions


**GET** `https://contract.mexc.com/api/v1/private/account/assets`


**GET** `{{api_url}}/api/v1/private/account/asset/USDT`


**GET** `https://contract.mexc.com/api/v1/private/account/transfer_record?page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| currency | None |  |
| state | None |  |
| type | None |  |
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `https://contract.mexc.com/api/v1/private/position/list/history_positions?page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol |  |  |
| type |  |  |
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `https://contract.mexc.com/api/v1/private/position/list/history_positions`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol |  |  |


**GET** `https://contract.mexc.com/api/v1/private/position/list/history_positions`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol |  |  |


**GET** `https://contract.mexc.com/api/v1/private/order/list/open_orders/BTC_USDT?page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `https://contract.mexc.com/api/v1/private/order/list/history_orders?page_num=1&page_size=20&symbol=BTC_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| page_num | 1 |  |
| page_size | 20 |  |
| states |  |  |
| category |  |  |
| start_time |  |  |
| end_time |  |  |
| side |  |  |
| symbol | BTC_USDT |  |


**GET** `https://contract.mexc.com/api/v1/private/order/list/history_orders?page_num=1&page_size=20&symbol=BTC_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| page_num | 1 |  |
| page_size | 20 |  |
| states |  |  |
| category |  |  |
| start_time |  |  |
| end_time |  |  |
| side |  |  |
| symbol | BTC_USDT |  |


**GET** `https://contract.mexc.com/api/v1/private/order/get/218699511659380224`


**GET** `https://contract.mexc.com/api/v1/private/order/batch_query?order_ids=1423534534`

| Parameter | Value | Description |
|-----------|-------|-------------|
| order_ids | 1423534534 | order number array，can be separated by "," for example :order_ids = 1,2,3(maximum 50 orders): |


**GET** `https://contract.mexc.com/api/v1/private/order/deal_details/2543756756876`


**GET** `{{api_url}}/api/v1/private/order/list/order_deals?symbol=LUNA_USDT&page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | LUNA_USDT |  |
| page_num | 1 |  |
| page_size | 20 |  |
| start_time | 1 |  |
| end_time | 100000 |  |


**GET** `https://contract.mexc.com/api/v1/private/planorder/list/orders?page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol |  |  |
| states |  |  |
| start_time |  |  |
| end_time |  |  |
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `https://contract.mexc.com/api/v1/private/stoporder/list/orders?page_num=1&page_size=20`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol |  |  |
| states |  |  |
| start_time |  |  |
| end_time |  |  |
| page_num | 1 |  |
| page_size | 20 |  |


**GET** `{{api_url}}/api/v1/private/account/risk_limit`


**GET** `https://contract.mexc.com/api/v1/private/account/tiered_fee_rate?symbol=BTC_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT |  |


**POST** `{{api_url}}/api/v1/private/position/change_margin?positionId=279313529050999808&amount=1&type=ADD`

| Parameter | Value | Description |
|-----------|-------|-------------|
| positionId | 279313529050999808 |  |
| amount | 1 |  |
| type | ADD | type ,ADD: increase,SUB: decrease |

```json
{ "positionId": 279313529050999808, "amount": 1, "type": "ADD"}
```


**GET** `https://contract.mexc.com/api/v1/private/position/leverage?symbol=LUNA_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | LUNA_USDT |  |


**POST** `{{api_url}}/api/v1/private/position/change_leverage`

```json
{"openType": 1,"leverage": 20,"symbol": "BTC_USDT","positionType": 1}
```


**GET** `{{api_url}}/api/v1/private/position/leverage?symbol=LUNA_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | LUNA_USDT |  |


**POST** `{{api_url}}/api/v1/private/position/change_position_mode`

```json
{ "positionMode": 1 }
```


**POST** `{{api_url}}/api/v1/private/order/submit`

```json
{"symbol": "DOGE_USDT","price": "0.16","vol": 1,"leverage": 20,"side": 3,"type": 5,"openType": 1, "positionMode": 2}
```


**POST** `{{api_url}}/api/v1/private/order/submit`

```json
[
  {
    "symbol": "BTC_USD",
    "price": 8800,
    "vol": 100,
    "leverage": 20,
    "side": 1,
    "type": 1,
    "openType": 1,
    "externalOid": "order1"
  },
  {
    "symbol": "BTC_USD",
    "price": 500,
    "vol": 100,
    "leverage": 50,
    "side": 3,
    "type": 1,
    "openType": 1,
    "externalOid": "order2"
  }
]
```


**POST** `{{api_url}}/api/v1/private/order/cancel`

```json
[ 218699511659380224 ]
```


**POST** `{{api_url}}/api/v1/private/order/cancel_with_external`

```json
{"symbol": "DOGE_USDT","externalOid": "218699511659380224"}
```


**POST** `{{api_url}}/api/v1/private/order/cancel_all`

```json
{"symbol": "DOGE_USDT"}
```


**POST** `{{api_url}}/api/v1/private/planorder/place`

```json
{"symbol":"DOGE_USDT","price":"0.06","vol":1,"leverage":20,"side":1,"openType":1,"triggerPrice":0.06,"triggerType":2,"executeCycle":1,"orderType":5,"trend":1}
```


**POST** `{{api_url}}/api/v1/private/planorder/cancel`

```json
[281077101510558208]
```


**POST** `{{api_url}}/api/v1/private/planorder/cancel_all`

```json
{"symbol": "BTC_USDT"}
```


**POST** `{{api_url}}/api/v1/private/stoporder/cancel`

| Parameter | Value | Description |
|-----------|-------|-------------|
|  |  |  |

```json
[{"stopPlanOrderId": "281077101510558208"}]
```


**POST** `{{api_url}}/api/v1/private/stoporder/cancel_all`


**POST** `{{api_url}}/api/v1/private/stoporder/change_price`

```json
{"orderId":"279995533824136192","stopLossPrice":"0.04","takeProfitPrice":"0.1"}
```


**POST** `{{api_url}}/api/v1/private/stoporder/change_plan_price`

```json
{"stopPlanOrderId":"279995533824136192","stopLossPrice":"0.02"}
```
