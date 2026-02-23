# Spot




## Public Market Data


**GET** `{{host}}/spot/v1/currencies`


**GET** `{{host}}/spot/v1/symbols`


**GET** `{{host}}/spot/v1/symbols/details`


**GET** `{{host}}/spot/quotation/v3/tickers`


**GET** `{{host}}/spot/quotation/v3/ticker?symbol=BTC_USDT`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT |  |


**GET** `{{host}}/spot/quotation/v3/lite-klines?symbol=BTC_USDT&step=60`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT |  |
| step | 60 |  |
| before | 1525760116 |  |
| after | 1525769116 |  |
| limit | 100 |  |


**GET** `{{host}}/spot/quotation/v3/klines?symbol=BMX_ETH&step=15&limit=100`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_ETH |  |
| step | 15 |  |
| before | 1525760116 |  |
| after | 1525769116 |  |
| limit | 100 |  |


**GET** `{{host}}/spot/quotation/v3/books?symbol=BMX_USDT&limit=2`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT |  |
| limit | 2 |  |


**GET** `{{host}}/spot/quotation/v3/trades?symbol=BMX_USDT&limit=1`

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT |  |
| limit | 1 |  |


## Funding Account


**GET** `{{host}}/account/v1/wallet?currency=USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| currency | USDT |  |


**GET** `{{host}}/account/v1/currencies?currencies=BTC,ETH`

| Parameter | Value | Description |
|-----------|-------|-------------|
| currencies | BTC,ETH |  |


**GET** `{{host}}/spot/v1/wallet`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |


**GET** `{{host}}/account/v1/deposit/address?currency=BTC`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| currency | BTC | Token symbol, e.g., 'BTC' |


**GET** `{{host}}/account/v1/withdraw/address/list`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |


**GET** `{{host}}/account/v1/withdraw/charge?currency=BTC`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| currency | BTC | Token symbol, e.g., 'BTC' |


**POST** `{{host}}/account/v1/withdraw/apply`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "currency": "USDT-TRC20",
    "amount": "100.000",
    "destination": "To Digital Address",
    "address": "0x1EE6FA5A3803608fc22a1f3F*********",
    "address_memo": ""
}
```


**GET** `{{host}}/account/v2/deposit-withdraw/history?currency=BTC&operation_type=deposit&N=10&startTime=&endTime=`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| currency | BTC | Token symbol, e.g., 'BTC' |
| operation_type | deposit | type
-deposit=deposit
-withdraw=withdraw |
| N | 10 | Recent N records (value range 1-100) |
| startTime |  | Default: 90 days from current timestamp (milliseconds)
 |
| endTime |  | Default: present timestamp (milliseconds)
 |


**GET** `{{host}}/account/v1/deposit-withdraw/detail?id=1679952`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| id | 1679952 | withdraw_id or deposit_id |


**GET** `{{host}}/spot/v1/margin/isolated/account`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT | Trading pair (e.g. BMX_USDT), no symbol is passed, and all isolated margin assets are returned |


**POST** `{{host}}/spot/v1/margin/isolated/transfer`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "currency":"BTC",
    "amount":"1",
    "side":"in"
}
```


**GET** `{{host}}/spot/v1/user_fee`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT | Trading pair (e.g. BMX_USDT), no symbol is passed, and all isolated margin assets are returned |


**GET** `{{host}}/spot/v1/trade_fee?symbol=BMX_USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT | Trading pair (e.g. BMX_USDT) |


## Spot / Margin Trading


**POST** `{{host}}/spot/v2/submit_order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "side":"sell",
    "type":"limit",
    "size":"10",
    "price":"700000",
    "stpMode":"cancel_maker"
}
```


**POST** `{{host}}/spot/v3/cancel_order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol": "BTC_USDT",
    "order_id": "137478201134227466"
}
```


**POST** `{{host}}/spot/v4/cancel_all`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTC_USDT",
  "side":"buy"
}
```


**POST** `{{host}}/spot/v1/margin/submit_order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "side":"sell",
    "type":"limit",
    "size":"10",
    "price":"7000000",
    "clientOrderId":"dd23d23d23d23"
}
```


**POST** `{{host}}/spot/v4/batch_orders`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "recvWindow": 5000,
    "orderParams":[{
        "size":"0.1",
        "price":"9000000",
        "side":"sell",
        "type":"limit",
        "stpMode":"none"
        },{
        "size":"0.1",
        "price":"9000000",
        "side":"sell",
        "type":"limit",
        "stpMode":"cancel_maker"
        }
    ]
}
```


**POST** `{{host}}/spot/v4/cancel_orders`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTC_USDT",
  "orderIds":[
    "5e925f3981"
  ],
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "orderId":"118100034543076010",
  "queryState":"open",
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/client-order`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "clientOrderId":"118100034543076010",
  "queryState":"open",
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/open-orders`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTC_USDT",
  "orderMode":"spot",
  "startTime":1682239652931,
  "endTime":1682239657931,
  "limit":10,
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/history-orders`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTC_USDT",
  "orderMode":"spot",
  "startTime":1682239502394,
  "endTime":1682239507394,
  "limit":10,
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/trades`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "symbol":"BTC_USDT",
  "orderMode":"spot",
  "startTime":1744787545000,
  "endTime":1747379545000,
  "limit":10,
  "recvWindow":5000
}
```


**POST** `{{host}}/spot/v4/query/order-trades`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
  "orderId":"118100034543076010",
  "recvWindow":5000
}
```


## Margin Loan


**POST** `{{host}}/spot/v1/margin/isolated/borrow`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "currency":"BTC",
    "amount":"10000000"
}
```


**POST** `{{host}}/spot/v1/margin/isolated/repay`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "symbol":"BTC_USDT",
    "currency":"BTC",
    "amount":"1"
}
```


**GET** `{{host}}/spot/v1/margin/isolated/borrow_record?symbol=BMX_USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BMX_USDT | Trading pair (e.g. BMX_USDT) |
| borrow_id | None | Borrow order id |
| start_time | None | Query start time: Timestamp |
| end_time | None | Query end time: Timestamp |
| N | None | Query record size, allowed range[1-100]. Default is 50 |


**GET** `{{host}}/spot/v1/margin/isolated/repay_record?symbol=BMX_USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| repay_id |  | Repayment ID |
| start_time |  | Query start time: Timestamp |
| end_time |  | Query end time: Timestamp |
| N |  | Query record size, allowed range[1-100]. Default is 50 |
| symbol | BMX_USDT | Trading pair (e.g. BMX_USDT) |
| currency | None | Currency |


**GET** `{{host}}/spot/v1/margin/isolated/pairs?symbol=BTC_USDT`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| symbol | BTC_USDT | It can be multiple-choice; if not filled in, then return all, like BTC_USDT, ETH_USDT
 |


## Main-Sub Account


### For Main Account


**POST** `{{host}}/account/sub-account/main/v1/sub-to-main`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "subAccount":"subAccountName@xxx.com"
}
```


**POST** `{{host}}/account/sub-account/main/v1/main-to-sub`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "subAccount":"subAccountName@xxx.com"
}
```


**POST** `{{host}}/account/sub-account/main/v1/sub-to-sub`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "fromAccount":"subAccountName1@xxx.com",
    "toAccount":"subAccountName2@xxx.com"
}
```


**GET** `{{host}}/account/sub-account/main/v1/transfer-list?moveType=spot to spot&N=10`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| moveType | spot to spot | type
-spot to spot=Spot wallet transfer to spot wallet |
| accountName |  | Sub-Account username |
| N | 10 | Recent N records, allowed range[1,100] |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "fromAccount":"subAccountName1@xxx.com",
    "toAccount":"subAccountName2@xxx.com"
}
```


**GET** `{{host}}/account/sub-account/main/v1/wallet?subAccount=subAccount1@xxx.com`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| subAccount | subAccount1@xxx.com | Sub-Account username |
| currency | None | Currency |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "fromAccount":"subAccountName1@xxx.com",
    "toAccount":"subAccountName2@xxx.com"
}
```


**GET** `{{host}}/account/sub-account/main/v1/subaccount-list`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "fromAccount":"subAccountName1@xxx.com",
    "toAccount":"subAccountName2@xxx.com"
}
```


### For Sub Account


**POST** `{{host}}/account/sub-account/sub/v1/sub-to-main`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "subAccount":"subAccountName@xxx.com"
}
```


**POST** `{{host}}/account/sub-account/sub/v1/sub-to-sub`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "subAccount":"subAccountName@xxx.com"
}
```


**GET** `{{host}}/account/sub-account/v1/transfer-history?moveType=spot to spot&N=10`

| Header | Value |
|--------|-------|
| X-BM-KEY | {{bitmart-access-key}} |
| X-BM-SIGN | {{x-bm-sign}} |
| X-BM-TIMESTAMP | {{x-bm-timestamp}} |

| Parameter | Value | Description |
|-----------|-------|-------------|
| moveType | spot to spot | type
-spot to spot=Spot wallet transfer to spot wallet |
| N | 10 | Recent N records, allowed range[1,100] |

```json
{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "fromAccount":"subAccountName1@xxx.com",
    "toAccount":"subAccountName2@xxx.com"
}
```
