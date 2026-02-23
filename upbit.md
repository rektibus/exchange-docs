# Intro (개요)

### What is This?

**Upbit(업비트) Cryptocurrency Exchange Open API Client of Multi-Programming Language Support**

Upbit Client(업비트 클라이언트)는 Upbit(업비트) OPEN API에 접근할 수 있는 인터페이스를 제공합니다.

### Support

<ul>
  <li>
    <b>
      <a href="https://upbit.com/">
        <img src="/images/upbit_favicon.png"> Upbit
      </a>
    </b>
  </li>
  <li>
    <b>
      <a href="https://github.com/swagger-api/">
        <img src="/images/swagger_favicon.png"> Swagger
      </a>
    </b>
  </li>
</ul>

### Powered By

<a href="https://github.com/slatedocs/slate">
  <img src="/images/logo-slate.png">
</a>
# Market (마켓)

## Market_info_all (마켓 코드 조회)
업비트에서 거래 가능한 마켓 목록을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Market.Market_info_all()
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"korean_name": "비트코인",
		"english_name": "Bitcoin"
	},
	{
		"market": "KRW-ETH",
		"korean_name": "이더리움",
		"english_name": "Ethereum"
	},
	{
		"market": "BTC-ETH",
		"korean_name": "이더리움",
		"english_name": "Ethereum"
	},
	{
		"market": "BTC-LTC",
		"korean_name": "라이트코인",
		"english_name": "Litecoin"
	},
	{
		"market": "BTC-XRP",
		"korean_name": "리플",
		"english_name": "Ripple"
    },
    ...
]
```

### Method
**GET** `/v1/market/all`

### Operation Code
`Market.Market_info_all`

### 요청 (Request)

Parameter      | Description
-------------- | -----------
isDetails      | 유의종목 필드과 같은 상세 정보 노출 여부 (선택 파라미터, 기본 값: false)

### 응답 (Response)

Parameter      | Description
-------------- | -----------
market         | 업비트에서 제공중인 시장 정보
korean_name    | 거래 대상 암호화폐 한글명
english_name   | 거래 대상 암호화폐 영문명
market_warning | 유의 종목 여부; (`NONE`: 해당 사항 없음, `CAUTION`: 투자 유의)# Trade (거래; 시세 체결)

## Trade_ticks (최근 체결 내역)

최근 체결 내역을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Trade.Trade_ticks(
    market='KRW-BTC'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"trade_date_utc": "2021-01-08",
		"trade_time_utc": "17:44:15",
		"timestamp": 1610127855000,
		"trade_price": 47560000.0,
		"trade_volume": 0.47572963,
		"prev_closing_price": 44698000.0,
		"change_price": 2862000.0,
		"ask_bid": "ASK",
		"sequential_id": 1610127855000000
    },
    ...
]
```

### Method

**GET** `/v1/trades/ticks`

### Operation Code

`Trade.Trade_ticks`

### 요청 (Request)

Parameter | Description
--------  | -----------
market *  | 마켓 코드 (ex. KRW-BTC, BTC-BCC)
to        | 마지막 캔들 시각 (exclusive). 포맷 : `yyyy-MM-dd'T'HH:mm:ssXXX` or `yyyy-MM-dd HH:mm:ss`. 비워서 요청시 가장 최근 캔들
count     | 캔들 개수 (최대 200개까지 요청 가능)
cursor    | 페이지네이션 커서 (`sequentialId`)
daysAgo   | 최근 체결 날짜 기준 7일 이내의 이전 데이터 조회 가능. 비워서 요청 시 가장 최근 체결 날짜 반환. (범위: 1 ~ 7)

### 응답 (Response)

Parameter          | Description
------------------ | -----------
trade_date_utc     | 체결 일자(UTC 기준)
trade_time_utc     | 체결 시각(UTC 기준)
timestamp          | 체결 타임스탬프
trade_price        | 체결 가격
trade_volume       | 체결량
prev_closing_price | 전일 종가
change_price       | 변화량
ask_bid            | 매도/매수
sequential_id      | 체결 번호 (Unique)

<aside class="notice">
    <code>sequential_id</code> 필드는 체결의 유일성 판단을 위한 근거로 쓰일 수 있습니다.
    <br/>
    하지만 체결의 순서를 보장하지는 못합니다.
</aside>

## Trade_ticker (시세 Ticker 조회 - 현재가 정보)

요청 당시 종목의 스냅샷을 반환합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Trade.Trade_ticker(
    markets='KRW-BTC, KRW-ETH'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"trade_date": "20210108",
		"trade_time": "174621",
		"trade_date_kst": "20210109",
		"trade_time_kst": "024621",
		"trade_timestamp": 1610127981000,
		"opening_price": 44698000.0,
		"high_price": 48550000.0,
		"low_price": 42271000.0,
		"trade_price": 47577000.0,
		"prev_closing_price": 44698000.0,
		"change": "RISE",
		"change_price": 2879000.0,
		"change_rate": 0.0644100407,
		"signed_change_price": 2879000.0,
		"signed_change_rate": 0.0644100407,
		"trade_volume": 0.00033988,
		"acc_trade_price": 861919074055.3187,
		"acc_trade_price_24h": 1082457070848.9071,
		"acc_trade_volume": 18804.39719428,
		"acc_trade_volume_24h": 23822.32449006,
		"highest_52_week_price": 48550000.0,
		"highest_52_week_date": "2021-01-08",
		"lowest_52_week_price": 5489000.0,
		"lowest_52_week_date": "2020-03-13",
		"timestamp": 1610127981564
	},
	{
		"market": "KRW-ETH",
		"trade_date": "20210108",
		"trade_time": "174619",
		"trade_date_kst": "20210109",
		"trade_time_kst": "024619",
		"trade_timestamp": 1610127979000,
		"opening_price": 1388000.0,
		"high_price": 1485000.0,
		"low_price": 1233500.0,
		"trade_price": 1410000.0,
		"prev_closing_price": 1388000.0,
		"change": "RISE",
		"change_price": 22000.0,
		"change_rate": 0.0158501441,
		"signed_change_price": 22000.0,
		"signed_change_rate": 0.0158501441,
		"trade_volume": 0.22966312,
		"acc_trade_price": 581867851790.185,
		"acc_trade_price_24h": 717996348913.0636,
		"acc_trade_volume": 422799.52433396,
		"acc_trade_volume_24h": 521320.18764923,
		"highest_52_week_price": 1485000.0,
		"highest_52_week_date": "2021-01-08",
		"lowest_52_week_price": 124350.0,
		"lowest_52_week_date": "2020-03-13",
		"timestamp": 1610127979352
	}
]
```

### Method

**GET** `/v1/ticker`

### Operation Code

`Trade.Trade_ticker`

### 요청 (Request)

Parameter  | Description
---------- | -----------
markets *  | 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)

### 응답 (Response)

Parameter             | Description
--------------------- | -----------
market                | 종목 구분 코드
trade_date            | 최근 거래 일자(UTC)
trade_time            | 최근 거래 시각(UTC)
trade_date_kst        | 최근 거래 일자(KST)
trade_time_kst        | 최근 거래 시각(KST)
opening_price         | 시가
high_price            | 고가
low_price             | 저가
trade_price           | 종가
prev_closing_price    | 전일 종가
change                | `EVEN`: 보합, `RISE`: 상승, `FALL`: 하락
change_price          | 변화액의 절대값
change_rate           | 변화율의 절대값
signed_change_price   | 부호가 있는 변화액
signed_change_rate    | 부호가 있는 변화율
trade_volume          | 가장 최근 거래량
acc_trade_price       | 누적 거래대금 (UTC 0시 기준)
acc_trade_price_24h   | 24시간 누적 거래대금
acc_trade_volume      | 누적 거래량 (UTC 0시 기준)
acc_trade_volume_24h  | 24시간 누적 거래량
highest_52_week_price | 52주 신고가
highest_52_week_date  | 52주 신고가 달성일
lowest_52_week_price  | 52주 신저가
lowest_52_week_date   | 52주 신저가 달성일
timestamp             | 타임스탬프

### 시세 관련 질문

### 1. 차트 보조지표를 계산하고 싶습니다.

업비트 차트의 보조지표들은 `Chartiq`, `Tradingview` 에서 제공하고 있으니 해당 사이트들을 참고하시길 바랍니다.

### 2. UBCI 지표를 API를 통해 수신하고 싶습니다.

UBCI API는 업비트 측에서 Open API로 제공하고 있지 않습니다.
업비트 공지사항을 통해 확인하시기 바랍니다.

### 3. 매수, 매도 (bid/ask) 결정 기준이 궁금합니다.

결정 기준은 아래와 같습니다.

- 매도 호가에 누군가 매수를 하면 체결은 매수(BID) 타입
- 매수 호가에 누군가 매도를 하면 체결은 매도(ASK) 타입

`making/taking` 관점에서 보면 `taking`의 주문 타입으로 결정이 됩니다.

### 4. 체결강도를 API를 통해 수신하고 싶습니다.

현재 업비트는 API를 통해 체결강도를 따로 제공해드리고 있지는 않습니다.
다만 `websocket`의 체결 데이터 수신을 통해 체결강도를 계산하실 수 있습니다.

<aside class="notice">
    <b>[ 체결강도 계산식 ]</b>
    <br/>
	체결강도 = 매수체결량/매도체결량 × 100%
	<br/>
	체결강도가 100보다 클 경우 매도보다 매수가 많은 것이며, 100보다 작을 경우는 매수보다 매도가 많다는 것을 의미
</aside>


체결강도는 UTC 0시(KST 9시)부터의 _매수누적체결량 / 매도누적체결량 * 100_ 으로 계산됩니다.
해당 계산식은 향후 서비스 운영 중 다른 형태로 별도의 고지 없이 변경될 수 있음을 참고 부탁드리겠습니다.

### 5. USDT 마켓의 원화 환산가격를 알고 싶습니다.

USDT 마켓의 원화 환산가격은 업비트 자체 마켓 시세를 통하여 계산됩니다.

- KRW-USDT = KRW-BTC / USDT-BTC
# Candle (시세 캔들; 봉)

## Candle_minutes (분; Minute 캔들)
분(Miniute) 단위로 시세 캔들을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Candle.Candle_minutes(
    unit=1,
    market='KRW-BTC'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"candle_date_time_utc": "2021-01-08T17:05:00",
		"candle_date_time_kst": "2021-01-09T02:05:00",
		"opening_price": 47550000.0,
		"high_price": 47563000.0,
		"low_price": 47550000.0,
		"trade_price": 47551000.0,
		"timestamp": 1610125540014,
		"candle_acc_trade_price": 44005459.60087,
		"candle_acc_trade_volume": 0.92535793,
		"unit": 1
    },
    ...
]
```

### Method
**GET** `/v1/candles/minutes/{unit}`

### Operation Code
`Candle.Candle_minutes`


### 요청 (Request)

Parameter  | Description
--------   | -----------
unit *     | 분 단위 (가능한 값: 1, 3, 5, 15, 10, 30, 60, 240) 
market *   | 마켓 코드 (ex. KRW-BTC, BTC-BCC)
to         | 마지막 캔들 시각 (exclusive). 포맷 : `yyyy-MM-dd'T'HH:mm:ssXXX` or `yyyy-MM-dd HH:mm:ss`. 비워서 요청시 가장 최근 캔들
count      | 캔들 개수 (최대 200개까지 요청 가능)

### 응답 (Response)

Parameter               | Description
----------------------- | -----------
market                  | 마켓명
candle_date_time_utc    | 캔들 기준 시각(UTC 기준)
candle_date_time_kst    | 캔들 기준 시각(KST 기준)
opening_price           | 시가
high_price              | 고가
low_price               | 저가
trade_price             | 종가
timestamp               | 해당 캔들에서 마지막 틱이 저장된 시각
candle_acc_trade_price  | 누적 거래 금액
candle_acc_trade_volume | 누적 거래량
unit                    | 분 단위 (유닛)

## Candle_days (일; Day 캔들)
일(Day) 단위로 시세 캔들을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Candle.Candle_days(
    market='KRW-BTC'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"candle_date_time_utc": "2021-01-08T00:00:00",
		"candle_date_time_kst": "2021-01-08T09:00:00",
		"opening_price": 44698000.0,
		"high_price": 48550000.0,
		"low_price": 42271000.0,
		"trade_price": 47544000.0,
		"timestamp": 1610126678593,
		"candle_acc_trade_price": 868607517589.245,
		"candle_acc_trade_volume": 18953.44414088,
		"prev_closing_price": 44698000.0,
		"change_price": 2846000.0,
		"change_rate": 0.0636717527
    },
    ...
]
```

### Method
**GET** `/v1/candles/days`

### Operation Code
`Candle.Candle_days`


### 요청 (Request)

Parameter                | Description
------------------------ | -----------
market *                 | 마켓 코드 (ex. KRW-BTC, BTC-BCC)
to                       | 마지막 캔들 시각 (exclusive). 포맷 : `yyyy-MM-dd'T'HH:mm:ssXXX` or `yyyy-MM-dd HH:mm:ss`. 비워서 요청시 가장 최근 캔들
convertingPriceUnit      | 종가 환산 화폐 단위 (생략 가능, KRW로 명시할 시 원화 환산 가격을 반환.)

### 응답 (Response)

Parameter               | Description
----------------------- | -----------
market                  | 마켓명
candle_date_time_utc    | 캔들 기준 시각(UTC 기준)
candle_date_time_kst    | 캔들 기준 시각(KST 기준)
opening_price           | 시가
high_price              | 고가
low_price               | 저가
trade_price             | 종가
timestamp               | 해당 캔들에서 마지막 틱이 저장된 시각
candle_acc_trade_price  | 누적 거래 금액
candle_acc_trade_volume | 누적 거래량
prev_closing_price      | 전일 종가(UTC 0시 기준)
change_price            | 전일 종가 대비 변화 금액
change_rate             | 전일 종가 대비 변화량
converted_trade_price   | 종가 환산 화폐 단위로 환산된 가격(요청에 `convertingPriceUnit` 파라미터 없을 시 해당 필드 포함되지 않음.)

## Candle_weeks (주; Week 캔들)
주(Week) 단위로 시세 캔들을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Candle.Candle_weeks(
    market='KRW-BTC'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"candle_date_time_utc": "2021-01-04T00:00:00",
		"candle_date_time_kst": "2021-01-04T09:00:00",
		"opening_price": 37537000.0,
		"high_price": 48550000.0,
		"low_price": 33000000.0,
		"trade_price": 47617000.0,
		"timestamp": 1610126559879,
		"candle_acc_trade_price": 3531977900551.1753,
		"candle_acc_trade_volume": 88370.43948385,
		"first_day_of_period": "2021-01-04"
    },
    ...
]
```

### Method
**GET** `/v1/candles/weeks`

### Operation Code
`Candle.Candle_weeks`


### 요청 (Request)

Parameter  | Description
--------   | -----------
market *   | 마켓 코드 (ex. KRW-BTC, BTC-BCC)
to         | 마지막 캔들 시각 (exclusive). 포맷 : `yyyy-MM-dd'T'HH:mm:ssXXX` or `yyyy-MM-dd HH:mm:ss`. 비워서 요청시 가장 최근 캔들
count      | 캔들 개수 (최대 200개까지 요청 가능)

### 응답 (Response)

Parameter               | Description
----------------------- | -----------
market                  | 마켓명
candle_date_time_utc    | 캔들 기준 시각(UTC 기준)
candle_date_time_kst    | 캔들 기준 시각(KST 기준)
opening_price           | 시가
high_price              | 고가
low_price               | 저가
trade_price             | 종가
timestamp               | 해당 캔들에서 마지막 틱이 저장된 시각
candle_acc_trade_price  | 누적 거래 금액
candle_acc_trade_volume | 누적 거래량
first_day_of_period     | 캔들 기간의 가장 첫 날

## Candle_month (월; Month 캔들)
월(Month) 단위로 시세 캔들을 조회합니다.

> Request Example

```python
from upbit.client import Upbit

client = Upbit()
resp = client.Candle.Candle_month(
    market='KRW-BTC'
)
print(resp['result'])
```

> Response Example

```json
[
	{
		"market": "KRW-BTC",
		"candle_date_time_utc": "2021-01-01T00:00:00",
		"candle_date_time_kst": "2021-01-01T09:00:00",
		"opening_price": 32037000.0,
		"high_price": 48550000.0,
		"low_price": 31800000.0,
		"trade_price": 47609000.0,
		"timestamp": 1610126792251,
		"candle_acc_trade_price": 5279753367606.828,
		"candle_acc_trade_volume": 136975.61257404,
		"first_day_of_period": "2021-01-01"
    },
    ...
]
```

### Method
**GET** `/v1/candles/months`

### Operation Code
`Candle.Candle_month`

### 요청 (Request)

Parameter  | Description
--------   | -----------
market *   | 마켓 코드 (ex. KRW-BTC, BTC-BCC)
to         | 마지막 캔들 시각 (exclusive). 포맷 : `yyyy-MM-dd'T'HH:mm:ssXXX` or `yyyy-MM-dd HH:mm:ss`. 비워서 요청시 가장 최근 캔들
count      | 캔들 개수 (최대 200개까지 요청 가능)

### 응답 (Response)

Parameter               | Description
----------------------- | -----------
market                  | 마켓명
candle_date_time_utc    | 캔들 기준 시각(UTC 기준)
candle_date_time_kst    | 캔들 기준 시각(KST 기준)
opening_price           | 시가
high_price              | 고가
low_price               | 저가
trade_price             | 종가
timestamp               | 해당 캔들에서 마지막 틱이 저장된 시각
candle_acc_trade_price  | 누적 거래 금액
candle_acc_trade_volume | 누적 거래량
first_day_of_period     | 캔들 기간의 가장 첫 날
# WebSocket (웹 소켓)
## 개요

### 1. 시세 정보
WebSocket을 이용하여 수신할 수 있는 정보는 다음과 같습니다.

1. 현재가 (스냅샷, 실시간 정보 제공)
2. 체결 (스냅샷, 실시간 정보 제공)
3. 호가 (스냅샷, 실시간 정보 제공)

각각의 정보는 `스냅샷`과 `실시간 데이터`로 나뉘며 요청 방법에 따라 수신할 수 있는 데이터가 달라집니다.

`스냅샷` 정보란 요청 당시의 상태를 의미합니다.

`실시간` 정보란 요청 정보가 스트림 형태로 지속적으로 제공되는 것을 의미합니다.

WebSocket을 이용하여 스냅샷 정보나 실시간 정보를 요청할 수 있으며 둘 중 하나의 정보만을 요청할 수도 있습니다.

자세한 요청 방법은 `2. 요청 포맷` 섹션과 `UpbitWebSocket` 섹션에서 다룹니다.

### 2. 요청 형식
연결이 성공적으로 이루어졌다면 웹소켓 서버에 여러가지 요청을 할 수 있습니다.
요청은 JSON Object를 이용하며 응답 또한 JSON Object 입니다.

요청은 크게 `[{ticket field}, {type field}, {format field}]` 로 나누어지며 각각의 필드는 다음 구성요소로 이루어져 있습니다.

**Ticket Field**

일반적으로 용도를 식별하기 위해 `ticket` 이라는 필드값이 필요합니다.

이 값은 시세를 수신하는 대상을 식별하며 되도록 유니크한 값을 사용하도록 권장합니다. (UUID 등)

필드 명 | 내용    | 타입   | 필요 여부
------- | ------ | ------ | ---------
ticket  | 식별값 | String | O


**Type Field**

수신하고 싶은 시세 정보를 나열하는 필드입니다.

`isOnlySnapshot`, `isOnlyRealtime` 필드는 생략 가능하며 모두 생략시 스냅샷과 실시간 데이터 모두를 수신합니다.

하나의 요청에 `{type field}` 는 여러개를 명시할 수 있습니다.

필드명         | 내용                                                                                   | 타입    | 필요 여부
-------------- | ------------------------------------------------------------------------------------- | ------- | ---------
type           | 수신할 시세 타입 (현재가: `ticker`, 체결: `trade`, 호가: `orderbook`)                   | String  | O
codes          | 수신할 시세 종목 정보 (**주의**: codes 필드에 명시되는 종목들은 대문자로 요청해야 합니다.) | List    | O
isOnlySnapshot | 시세 스냅샷만 제공                                                                      | Boolean | X
isOnlyRealtime | 실시간 시세만 제공                                                                      | Boolean | X

<aside class="notice">
    <b>NOTE</b>: v1.1.0 Orderbook Unit 갯수 커스텀 수신기능 추가
    <br/><br/>
    v1.1.0 부터 orderbook 타입의 패킷에 한하여 Orderbook Unit의 갯수를 최대 제공 갯수(15개) 안에서 원하는 만큼 조절하여 호출 가능합니다.
    <br/>
    기존의 <code>codes</code> 항목에 시세 종목과 원하는 Unit 갯수를 넣어주시면 됩니다.
    <br/>
    형식: <code>{code}.{count}</code>
    <br/>
    ex) "KRW-BTC.5", "BTC-XRP.3"
    <br/><br/>
</aside>


**Format Field**

마지막으로 포맷 정보입니다. `Simple`로 지정될 경우 응답의 필드명이 모두 간소화됩니다.

트래픽 부담이 클 때 사용하는 방법입니다.

필드명 | 내용                                                         | 타입   | 필요 여부
------ | ----------------------------------------------------------- | ------ | ---------
format | 포맷 (`SIMPLE`: 간소화된 필드명, `DEFAULT`: 기본값(생략 가능) | String | X (기본: `Default`)


## UpbitWebSocket
고성능 네트워크 및 웹 서버 비동기(async) 프레임워크 기반의 동시성 코드 작성을 위한 업비트 웹 소켓 클래스를 생성합니다.

자세한 사항은 파이썬 표준 라이브러리 [`asyncio`](https://docs.python.org/3/library/asyncio.html) 패키지를 참고해주세요.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()
print(sock)

async with sock as conn:
    # Do something
    pass
```

> Result Example

```python
UpbitWebSocket(wss://api.upbit.com/websocket/v1)
```

### UpbitWebSocket(uri=WEBSOCKET_URI, ping_interval=None, ping_timeout=None)

Parameter      | Description
-------------- | --------------------
uri            | 웹 소켓에 연결할 URI. (기본값: `wss://api.upbit.com/websocket/v1`)
ping_interval  | ping 간격 제한 (기본값: `None`)
ping_timeout   | ping 시간 초과 제한 (기본값: `None`)


## socket.Connection
**Property**

웹 소켓에 연결하기 위해 생성된 Connection 객체입니다.

위의 예제와 동일한 결과를 가집니다.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()
connection = sock.Connection

async with connection as conn:
    # Do Something
    pass
```

## socket.connect
**Method**

URI에 연결을 시도하고 Connection 객체를 재생성합니다.

`UpbitWebSocket` 클래스의 `__init__` 메소드 호출 시 자동으로 호출됩니다.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()
sock.connect(
    ping_interval=20,
    ping_timeout=20
)

async with sock as conn:
    # Do Something
    pass
```

### socket.connect(ping_interval=None, ping_timeout=None)

Parameter      | Description
-------------- | --------------------
ping_interval  | ping 간격 제한 (기본값: `None`)
ping_timeout   | ping 시간 초과 제한 (기본값: `None`)


## conn.send
웹 소켓에 데이터를 수신합니다.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()

async with sock as conn:
    await conn.send('PING')
```

### conn.send(message)

Parameter      | Description
-------------- | --------------------
message *      | 서버에 수신할 데이터


## conn.recv
서버로부터 전달받은 바이트 스트림(bytes stream) 데이터를 받습니다.

예외를 발생시키는 경우는 아래와 같습니다.

- **ConnectionClosed**: `Connection` 객체가 `Close` 상태가 되었을 경우
- **RuntimeError**: 두 가지 코루틴이 동시에 `recv` 를 호출하는 경우

> Example Code

```python
import re
import json
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()

async with sock as conn:
    await conn.send('PING')
    data = await conn.recv()

    pattern = re.compile('{"\S+":"\S+"}')
    search = pattern.search(data.decode('utf8'))
    result = json.loads(search.group())
    print(result)
```

> Result

```json
{"status": "UP"}
```

### conn.recv()

No Parameters


## UpbitWebSocket.generate_type_field (Type Field Generate)
**staticmethod**

웹 소켓 수신에 필요한 payload의 type field 데이터를 generate 합니다.

요청 형식에 대한 사항은 위의 `2. 요청 형식` 섹션을 참고해주세요.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

currencies = ['KRW-BTC', 'KRW-ETH']

type_field = UpbitWebSocket.generate_type_field(
    type="trade",
    codes=currencies
)
print(type_field)
```

> Result

```json
{
    "type": "trade",
    "codes": ["KRW-BTC", "KRW-ETH"]
}
```

### UpbitWebSocket.generate_type_field(type, codes, isOnlySnapshot=None, isOnlyRealtime=None)
**staticmethod**

Parameter      | Description
-------------- | --------------------
type *         | 수신할 시세 타입 (현재가: `ticker`, 체결: `trade`, 호가: `orderbook`)
codes *        | 수신할 시세 종목 정보 (ex. `['KRW-BTC', 'KRW-ETH']`)
isOnlySnapshot | 시세 스냅샷만 제공 여부 (`True`, `False`)
isOnlyRealtime | 실시간 시세만 제공 여부 (`True`, `False`)


## UpbitWebSocket.generate_orderbook_codes (Orderbook Codes Generate)
**staticmethod**

`type` 파라미터가 `orderbook`일 경우에 필요한 `codes` 파라미터를 요청 형식에 맞춰 generate 합니다.

> Example Code

```python
from upbit.websocket import UpbitWebSocket

currencies = ['KRW-BTC', 'KRW-ETH']
counts = [5, 5]

codes = UpbitWebSocket.generate_orderbook_codes(
    currencies=currencies,
    counts=counts
)
print(codes)
```

> Result

```json
["KRW-BTC.5", "KRW-ETH.5"]
```

### UpbitWebSocket.generate_orderbook_codes(currencies, counts=None)

Parameter      | Description
-------------- | --------------------
currencies *   | 수신할 시세 종목들
counts         | 수신할 각 시세 종목에 대한 개수


## UpbitWebSocket.generate_payload (Payload Generate)
**staticmethod**

웹 소켓 수신에 필요한 payload 데이터를 json 포맷 형식의 문자열로 generate 합니다.

> Example Code

```python
from upbit.websocket import UpbitWebSocket


codes = ['KRW-BTC', 'KRW-ETH', 'KRW-BCH', 'KRW-XRP']
counts = [1 for _ in range(len(codes))]

ord_codes = UpbitWebSocket.generate_orderbook_codes(
    currencies=codes,
    counts=counts
)

trade = UpbitWebSocket.generate_type_field(
    type='trade',
    codes=codes
)
orderbook = UpbitWebSocket.generate_type_field(
    type='orderbook',
    codes=ord_codes
)

type_fields = [trade, orderbook]

payload = UpbitWebSocket.generate_payload(
    type_fields=type_fields,
    format='SIMPLE'
)

print(payload)
```

> Result

```json
[
    {
        "ticket": "43552c23-6596-478d-8f71-b8289779a996"
    },
    {
        "type": "trade",
        "codes": ["KRW-BTC", "KRW-ETH", "KRW-BCH", "KRW-XRP"]
    },
    {
        "type": "orderbook",
        "codes": ["KRW-BTC.1", "KRW-ETH.1", "KRW-BCH.1", "KRW-XRP.1"]
    },
    {
        "format": "SIMPLE"
    }
]
```


### UpbitWebSocket.generate_payload(type_fields, ticket=None, format='DEFAULT')

Parameter      | Description
-------------- | --------------------
type_fields *  | Type Fields
ticket         | 식별값 (기본값은 `uuid4` 형식으로 생성)
format         | 포맷, `SIMPLE`: 간소화된 필드명, `DEFAULT`: 기본 포맷 (생략 가능)


## 웹 소켓으로 시세 정보 요청하기
웹 소켓을 통해 시세 정보를 요청합니다.

> Example Code

```python
import json
import asyncio

from upbit.websocket import UpbitWebSocket


# Definition async function
async def ticker(sock, payload):
    async with sock as conn:
        await conn.send(payload)
        while True:
            recv = await conn.recv()
            data = recv.decode('utf8')
            result = json.loads(data)
            print(result)


sock = UpbitWebSocket()

currencies = ['KRW-BTC', 'KRW-ETH']
type_field = sock.generate_type_field(
    type='ticker',
    codes=currencies
)
payload = sock.generate_payload(
    type_fields=[type_field]
)

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete( ticker(sock, payload) )
```

> Result

```json
{
    "type": "ticker",
    "code": "KRW-BTC",
    "opening_price": 36408000.0,
    "high_price": 38161000.0,
    "low_price": 35907000.0,
    "trade_price": 36784000.0,
    "prev_closing_price": 36408000.0,
    "acc_trade_price": 466420626861.1874,
    "change": "RISE",
    "change_price": 376000.0,
    "signed_change_price": 376000.0,
    "change_rate": 0.0103274006,
    "signed_change_rate": 0.0103274006,
    "ask_bid": "BID",
    "trade_volume": 0.004996,
    "acc_trade_volume": 12633.27063535,
    "trade_date": "20210201",
    "trade_time": "192943",
    "trade_timestamp": 1612207783000,
    "acc_ask_volume": 6355.28646728,
    "acc_bid_volume": 6277.98416807,
    "highest_52_week_price": 48550000.0,
    "highest_52_week_date": "2021-01-08",
    "lowest_52_week_price": 5489000.0,
    "lowest_52_week_date": "2020-03-13",
    "trade_status": null,
    "market_state": "ACTIVE",
    "market_state_for_ios": null,
    "is_trading_suspended": false,
    "delisting_date": null,
    "market_warning": "NONE",
    "timestamp": 1612207783496,
    "acc_trade_price_24h": 503390500539.5724,
    "acc_trade_volume_24h": 13650.71883738,
    "stream_type": "SNAPSHOT"
},
{
    "type": "ticker",
    "code": "KRW-ETH",
    "opening_price": 1444000.0,
    "high_price": 1509500.0,
    "low_price": 1413000.0,
    "trade_price": 1444000.0,
    "prev_closing_price": 1444000.0,
    "acc_trade_price": 331846956832.1946,
    "change": "EVEN",
    "change_price": 0.0,
    "signed_change_price": 0.0,
    "change_rate": 0,
    "signed_change_rate": 0,
    "ask_bid": "ASK",
    "trade_volume": 1.0,
    "acc_trade_volume": 229202.315562,
    "trade_date": "20210201",
    "trade_time": "192925",
    "trade_timestamp": 1612207765000,
    "acc_ask_volume": 126760.03539062,
    "acc_bid_volume": 102442.28017138,
    "highest_52_week_price": 1626000.0,
    "highest_52_week_date": "2021-01-25",
    "lowest_52_week_price": 124350.0,
    "lowest_52_week_date": "2020-03-13",
    "trade_status": null,
    "market_state": "ACTIVE",
    "market_state_for_ios": null,
    "is_trading_suspended": false,
    "delisting_date": null,
    "market_warning": "NONE",
    "timestamp": 1612207765752,
    "acc_trade_price_24h": 354570292652.8257,
    "acc_trade_volume_24h": 244893.27187195,
    "stream_type": "SNAPSHOT"
},
...
```

### Request Parameters

Parameter      | Description
-------------- | --------------------
payload        | 포맷에 맞춰진 요청 데이터


### Response


**현재가(Ticker) 응답**

필드명                      | 축약형 (format: SIMPLE) | 내용                | 타입  | 값
-------------------------- | ---------------------- | ------------------- | ----- | -----
type                       | ty           | 타입                           | String | `ticker` : 현재가
code                       | cd           | 마켓 코드 (ex. KRW-BTC)        | String | -
opening_price              | op           | 시가                           | Double | -
high_price                 | hp           | 고가                           | Double | -
low_price                  | lp           | 저가                           | Double | -
trade_price                | tp           | 현재가                         | Double | -
prev_closing_price         | pcp          | 전일 종가                      | Double | 
change                     | c            | 전일 대비                      | String | `RISE`: 상승, `EVEN`: 보합, `FALL`: 하락
change_price               | cp           | 부호 없는 전일 대비 값          | Double | -
signed_change_price        | scp          | 전일 대비 값                   | Double | -
change_rate                | cr           | 부호 없는 전일 대비 등락율      | Double | -
signed_change_rate         | scr          | 전일 대비 등락율               | Double | -
trade_volume               | tv           | 가장 최근 거래량               | Double | -
acc_trade_volume           | atv          | 누적 거래량(UTC 0시 기준)      | Double | -
acc_trade_volume_24h       | atv24h       | 24시간 누적 거래량              | Double | -
acc_trade_price            | atp          | 누적 거래대금(UTC 0시 기준)     | Double | -
acc_trade_price_24h        | atp24h       | 24시간 누적 거래대금            | Double | -
trade_date                 | tdt          | 최근 거래 일자(UTC)            | String | `yyyyMMdd`
trade_time                 | ttm          | 최근 거래 시각(UTC)            | String | `HHmmss`
trade_timestamp            | ttms         | 체결 타임스탬프 (milliseconds) | Long | -
ask_bid                    | ab           | 매수/매도 구분                 | String  | `ASK`: 매도, `BID`: 매수
acc_ask_volume             | aav          | 누적 매도량                    | Double | -
acc_bid_volume             | abv          | 누적 매수량                    | Double | -
highest_52_week_price      | h52wp        | 52주 최고가                    | Double | -
highest_52_week_date       | h52wdt       | 52주 최고가 달성일              | String | `yyyy-MM-dd`
lowest_52_week_price       | l52wp        | 52주 최저가                    | Double | -
lowest_52_week_date        | l52wdt       | 52주 최저가 달성일              | String |`yyyy-MM-dd`
trade_status               | ts           | 거래상태 *deprecated           | String | -
market_state               | ms           | 거래상태                       | String | `PREVIEW`: 입금지원, `ACTIVE`: 거래지원가능, `DELISTED` : 거래지원종료
market_state_for_ios       | msfi         | 거래 상태 *deprecated          | String | - 
is_trading_suspended       | its          | 거래 정지 여부                  | Boolean | - 
delisting_date             | dd           | 상장폐지일                      | Date  | -
market_warning             | mw           | 유의 종목 여부                  | String | `NONE`: 해당없음, `CAUTION`: 투자유의
timestamp                  | tms          | 타임스탬프 (milliseconds)       | Long | -
stream_type                | st           | 스트림 타입                     | String | `SNAPSHOT`: 스냅샷, `REALTIME`: 실시간


**체결(Trade) 응답**

필드명 | 축약형 (format: SIMPLE) | 내용 | 타입 | 값
----- | ------------------------ | --- | --- | ----
type | ty | 타입 | String | `trade`: 체결
code | cd | 마켓 코드 (ex. KRW-BTC) | String | - 
trade_price | tp | 체결 가격 | Double | -
trade_volume | tv | 체결량 | Double | -
ask_bid | ab | 매수/매도 구분 | String | `ASK`: 매도, `BID`: 매수
prev_closing_price | pcp | 전일 종가 | Double | -
change | c | 전일 대비 | String | `RISE` : 상승, `EVEN` : 보합, `FALL` : 하락
change_price | cp | 부호 없는 전일 대비 값 | Double | -
trade_date | td | 체결 일자(UTC 기준) | String | `yyyy-MM-dd`
trade_time | ttm | 체결 시각(UTC 기준) | String | `HH:mm:ss`
trade_timestamp | ttms | 체결 타임스탬프 (millisecond) | Long | -
timestamp | tms | 타임스탬프 (millisecond) | Long | -
sequential_id | sid | 체결 번호 (Unique) | Long | -
stream_type | st | 스트림 타입 | String | `SNAPSHOT`: 스냅샷, `REALTIME`: 실시간

<aside class="notice">
    <code>sequential_id</code> 필드는 체결의 유일성 판단을 위한 근거로 쓰일 수 있습니다.
    <br/>
    하지만 체결의 순서를 보장하지는 못합니다.
</aside>


**호가(Orderbook) 응답**

필드명 | 축약형 (format: SIMPLE) | 내용 | 타입 | 값
------ | ----------------------- | --- | --- | -------
type | ty | 타입 | String | `orderbook`: 호가
code | cd | 마켓 코드 (ex. KRW-BTC) | String | - 
total_ask_size | tas | 호가 매도 총 잔량 | Double | - 
total_bid_size | tbs | 호가 매수 총 잔량 | Double | -
orderbook_units | obu | 호가 | List of Objects | -
ask_price | ap | 매도 호가 | Double | -
bid_price | bp | 매수 호가 | Double | -
ask_size | as | 매도 잔량 | Double | -
bid_size | bs | 매수 잔량 | Double | -
timestamp | tms | 타임스탬프 (millisecond) | Long | -

## Connection 관리 및 기타

> Example Code

```python
from upbit.websocket import UpbitWebSocket

sock = UpbitWebSocket()
pong = await sock.ping()
print(pong)
```

> Result

```json
{ "status": "UP" }
```

**PING/PONG**

업비트 OpenAPI WebSocket 서버는 2019년 3월 27일부터 안정적인 커넥션 관리와 유지를 위해 WebSocket PING/PONG Frame을 지원합니다. (참고 문서 : https://tools.ietf.org/html/rfc6455#section-5.5.2 )

**Client to Server PING**

- 서버에서는 기본적으로 아무런 데이터도 수/발신 되지 않은 채 약 120초가 경과하면 Idle Timeout으로 WebSocket Connection을 종료합니다.
- 이를 방지하기 위해 클라이언트에서 서버로 PING 메시지를 보내서 Connection을 유지하고, WebSocket 서버의 상태와 WebSocket Connection Status를 파악할 수 있습니다.
- 현재 업비트 OpenAPI WebSocket 서버에서는 **PING Frame 수신 대응 준비가 되어있는 상황**이며, 클라이언트에서 간단한 구현으로 PING 요청/PONG 응답(*PING에 대한 응답 Frame*)을 통해 서버의 상태를 파악할 수 있습니다.

## WebSocket Compression
업비트 OpenAPI WebSocket 서버에서는 더 빠른 데이터 전송을 위해 WebSocket Compression을 제공하고 있습니다. (참고 문서 : https://tools.ietf.org/html/rfc7692 )

- WebSocket Compression을 지원하는 WebSocket 클라이언트 에서는, 각 클라이언트 별로 정해진 옵션을 활성화 하면 Compression 된 상태로 통신이 지속됩니다. 사용자의 코드 레벨에는 decompressed 상태의 raw data가 제공되기 때문에 **사용자는 설정 옵션 활성화 외에 다른 대응 코드를 작성할 필요가 없습니다.**
- WebSocket Compression을 지원하지 않는 WebSocket 클라이언트 에서는 해당 기능을 사용할 수 없으며, Raw JSON 형태의 데이터를 주고받게 됩니다. 해당 기능을 사용하기 위해서는 WebSocket Client 교체가 필요합니다.
# Account (계좌)

## Account_info (전체 계좌 조회)

내가 보유한 자산 리스트를 보여줍니다.

> Request Example

```python
from upbit.client import Upbit

access_key = "Your Access Key"
secret_key = "Your Secret Key"

client = Upbit(access_key, secret_key)
resp = client.Account.Account_info()
print(resp['result'])
```

> Response Example

```json
[
    {
        "currency": "BTC",
        "balance": "0.00048",
        "locked": "0.0",
        "avg_buy_price": "20870000",
        "avg_buy_price_modified": false,
        "unit_currency": "KRW"
    },
    {
        "currency": "KRW",
        "balance": "0.34202414",
        "locked": "4999.99999922",
        "avg_buy_price": "0",
        "avg_buy_price_modified": true,
        "unit_currency": "KRW"
    },
    {
        "currency": "ETH",
        "balance": "0.00935861",
        "locked": "0.0",
        "avg_buy_price": "1068000",
        "avg_buy_price_modified": false,
        "unit_currency": "KRW"
    }
]
```

### Method

**GET** `/v1/accounts`

### Operation Code

`Account.Account_info`

### 요청 (Request)

No Parameters

### 응답 (Response)

| Parameter              | Description                      |
| ---------------------- | -------------------------------- |
| currency               | 화폐를 의미하는 영문 대문자 코드 |
| balance                | 주문가능 금액/수량               |
| locked                 | 주문 중 묶여있는 금액/수량       |
| avg_buy_price          | 매수평균가                       |
| avg_buy_price_modified | 매수평균가 수정 여부             |
| unit_currency          | 평단가 기준 화폐                 |

## Account_wallet (입출금 현황)

입출금 현황 및 블록 상태를 조회합니다.

> Request Example

```python
from upbit.client import Upbit

access_key = "Your Access Key"
secret_key = "Your Secret Key"

client = Upbit(access_key, secret_key)
resp = client.Account.Account_wallet()
print(resp['result'])
```

> Response Example

```json
[
    {
        "currency": "BTC",
        "net_type": "BTC",
        "wallet_state": "working",
        "block_state": "normal",
        "block_height": 665013,
        "block_updated_at": "2021-01-07T19:44:40.005+00:00",
        "block_elapsed_minutes": 14
    },
    {
        "currency": "POWR",
        "net_type": "POWR",
        "wallet_state": "working",
        "block_state": "normal",
        "block_height": 11609520,
        "block_updated_at": "2021-01-07T19:54:27.007+00:00",
        "block_elapsed_minutes": 5
    },
    {
        "currency": "ETH",
        "net_type": "ETH",
        "wallet_state": "working",
        "block_state": "normal",
        "block_height": 11609520,
        "block_updated_at": "2021-01-07T19:54:25.242+00:00",
        "block_elapsed_minutes": 5
    },
    {
        "currency": "ETC",
        "net_type": "ETC",
        "wallet_state": "working",
        "block_state": "normal",
        "block_height": 11947575,
        "block_updated_at": "2021-01-07T19:54:38.171+00:00",
        "block_elapsed_minutes": 4
    },
    ...
]
```

### Method

**GET** `/v1/status/wallet`

### Operation Code

`Account.Account_wallet`

### 요청 (Request)

No Parameters

<aside class="notice">
    <b>NOTE</b>: 입출금 현황 데이터는 실제 서비스 상태와 다를 수 있습니다.
    <br/>
    <br/>
    입출금 현황 API에서 제공하는 입출금 상태, 블록 상태 정보는 수 분 정도 지연되어 반영될 수 있습니다.
    <br/>
    본 API는 참고용으로만 사용하시길 바라며 실제 입출금을 수행하기 전에는 반드시 업비트 공지사항 및 입출금 현황 페이지를 참고해주시기 바랍니다.
</aside>

<aside class="notice">
    <b>네트워크 타입( <code>net_type</code> )이란?</b>
    <br/><br/>
    디지털 자산 입출금에 활용되는 블록체인 네트워크를 뜻하며, 디지털 자산의 종류에 따라 활용되는 네트워크(체인)이 다를 수 있습니다.
</aside>

### 응답 (Response)

<table>
  <tr>
    <th>
      Parameter
    </th>
    <th>
      Description
    </th>
  </tr>
  <tr>
    <td>
        currency
    </td>
    <td>
        화폐를 의미하는 영문 대문자 코드
    </td>
  </tr>
  <tr>
    <td>
        net_type
    </td>
    <td>
        입출금 네트워크
    </td>
  </tr>
  <tr>
    <td>
      wallet_state
    </td>
    <td>
      입출금 상태
      <ul>
        <li>working: 입출금 가능</li>
        <li>withdraw_only: 출금만 가능</li>
        <li>deposit_only: 입금만 가능</li>
        <li>paused: 입출금 중단</li>
        <li>unsupported : 입출금 미지원</li>
      </ul>
    </td>
  </tr>
  <tr>
  <td>
      block_state
  </td>
  <td>
      블록 상태
      <ul>
        <li>normal: 정상</li>
        <li>delayed: 지연</li>
        <li>inactive: 비활성 (점검 등)</li>
      </ul>
  </td>
</tr>
<tr>
  <td>
      block_height
  </td>
  <td>
      블록 높이
  </td>
</tr>
<tr>
  <td>
      block_updated_at
  </td>
  <td>
      블록 갱신 시각
  </td>
</tr>
</table>
# Authentication (인증)

> Request Example

```json
{
  "access_key": "발급 받은 acccess key (필수)",
  "nonce": "무작위의 UUID 문자열 (필수)",
  "query_hash": "해싱된 query string (파라미터가 있을 경우 필수)",
  "query_hash_alg": "query_hash를 생성하는 데에 사용한 알고리즘 (기본값 : SHA512)"
}
```

Upbit OPEN API는 기본적으로 REST API 요청시, 발급받은 access key와 secret key로 토큰을 생성하여 Authorization 헤더를 통해 전송합니다. 토큰은 <a href="https://jwt.io">JWT</a> 형식을 따릅니다.

서명 방식은 HS256 을 권장하며, 서명에 사용할 secret은 발급받은 secret key를 사용합니다.
Payload의 구성은 예제와 같습니다.

인증방식에 대한 세부적인 코드를 확인하고 싶으시면 <a href="https://github.com/uJhin/upbit-client/blob/main/client/python/upbit/authentication.py"><b>여기</b></a>를 참고해주시기 바랍니다.

<aside class="notice">
<b> NOTE: v1.0.3 업데이트부터 JWT payload를 생성하는 방식이 다음과 같이 변경되었습니다.</b>

<ul>
  <li><code>nonce</code> 필드의 값으로 무작위 UUID 문자열을 이용합니다.</li>
  <li><code>query</code> 필드가 <code>query_hash</code>, <code>query_hash_alg</code> 의 두 가지 필드로 대체됩니다.</li>
</ul>

기존의 JWT payload 생성 방식도 여전히 지원하지만, Open API 이용의 안정성을 위해 추가된 기능이므로 새로운 방식으로 변경하실 것을 권장드립니다.

자세한 사항은 <a href="https://docs.upbit.com/docs">공식 API 문서</a>를 참조해주세요.
</aside>

<aside class="warning">
payload의 <code>query_hash</code> 값을 생성할 때 사용하는 쿼리 값은 <code>query string</code> 이어야 합니다. JSON 및 기타 포멧은 허용되지 않습니다.
</aside>

<aside class="warning">
Signature 생성시 secret encoding 옵션을 확인해주세요. <b>발급된 <code>secret key</code>는 base64로 encoding 되어있지 않습니다.</b> JWT 관련 library를 사용하신다면 해당 옵션을 확인해주세요.
</aside>

<aside class="warning">
<b>NOTE: v1.3.0 업데이트 - urlencoded form 지원 종료 (2022. 3. 1.)</b>
<br/><br/>
2022년 3월부터 <code>urlencoded form</code> 형식을 이용한 HTTP body 요청은 지원이 종료될 예정입니다.
<br/>
JSON 형식을 이용해주시기 바랍니다.
<br/><br/>
자세한 변경사항은 <a href="https://docs.upbit.com/changelog/open-api-%EB%B3%80%EA%B2%BD%EC%82%AC%ED%95%AD-%EC%95%88%EB%82%B4">공지사항</a>을 참조해주세요.
</aside>

<aside class="warning">
<b>NOTE: v1.3.0 업데이트 - 기존 인증방식 지원 종료 (2022. 3. 1.)</b>
<br/><br/>
2022년 3월부터 query 필드를 이용한 JWT 페이로드 생성 방식은 지원이 종료될 예정입니다.
<br/>
<code>query_hash</code> 와 <code>query_hash_alg</code> 필드를 이용한 생성 방식을 이용해주시기 바랍니다.
<br/><br/>
자세한 변경사항은 <a href="https://docs.upbit.com/changelog/open-api-%EB%B3%80%EA%B2%BD%EC%82%AC%ED%95%AD-%EC%95%88%EB%82%B4">공지사항</a>을 참조해주세요.
</aside>
