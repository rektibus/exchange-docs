# Coinone API Documentation

Auto-fetched from 3 page(s)


---

# Source: https://docs.coinone.co.kr/reference/common

ERROR: Failed to fetch: 404 Client Error: Not Found for url: https://docs.coinone.co.kr/reference/common


---

# Source: https://docs.coinone.co.kr/reference/orderbook

[Jump to Content](#content)

[](/)

[ __Home](/)[ __이용 안내](/docs)[ __API 레퍼런스](/reference)[ __변경 내역](/changelog) v1.0v1.1v1.2v1.3v1.4v1.5v1.6v1.7

* * *

[](/search)[](/)

 __API 레퍼런스

v1.7 __

[__Home](/)[ __이용 안내](/docs)[ __API 레퍼런스](/reference)[ __변경 내역](/changelog)

오더북 조회

JUMP TO

## PUBLIC API V2

  * [개별 호가 단위 조회get](/reference/range-unit)
  * [전체 종목 정보 조회get](/reference/markets)
  * [개별 종목 정보 조회get](/reference/market)
  * [오더북 조회get](/reference/orderbook)
  * [최근 체결 주문 조회get](/reference/recent-completed-orders)
  * [전체 티커 정보 조회get](/reference/tickers)
  * [개별 티커 정보 조회get](/reference/ticker)
  * [전체 티커 정보 조회 (UTC)get](/reference/utc-tickers)
  * [개별 티커 정보 조회 (UTC)get](/reference/utc-ticker)
  * [전체 가상자산 정보 조회get](/reference/currencies)
  * [개별 가상자산 정보 조회get](/reference/currency)
  * [캔들 차트 조회get](/reference/chart)



## PRIVATE API V2.1

  * [잔고 조회 __](/reference/find-balance)
    * [전체 잔고 조회 post](/reference/find-balance)
    * [특정 자산 잔고 조회post](/reference/find-balance-by-currencies)
  * [고객 정보 __](/reference/find-all-trade-fees)
    * [전체 수수료 조회 post](/reference/find-all-trade-fees)
    * [개별 종목 수수료 조회post](/reference/find-trade-fee-by-pair)
  * [주문 조회 __](/reference/find-active-orders)
    * [미체결 주문 조회 post](/reference/find-active-orders)
    * [주문 정보 조회post](/reference/order-detail)
    * [전체 체결 주문 조회post](/reference/find-all-completed-orders)
    * [종목 별 체결 주문 조회post](/reference/find-completed-orders)
    * [전체 미체결 주문 조회post](/reference/find-all-open-orders)
    * [종목 별 미체결 주문 조회post](/reference/find-open-orders)
    * [특정 주문 정보 조회post](/reference/find-order-info)
  * [주문 권한 __](/reference/place-order)
    * [매수/매도 주문 post](/reference/place-order)
    * [종목 별 전체 주문 취소post](/reference/cancel-orders)
    * [개별 주문 취소post](/reference/cancel-order)
    * [지정가 매매 주문post](/reference/order-place-limit-order)
  * [입출금 조회 __](/reference/krw-transaction-history)
    * [원화 입출금 내역 조회 post](/reference/krw-transaction-history)
    * [가상자산 입출금 내역 조회post](/reference/coin-transaction-history)
    * [가상자산 입출금 내역 단건 조회post](/reference/single-coin-transaction-history)
    * [가상자산 출금 한도 조회post](/reference/coin-withdrawal-limit)
    * [출금 주소 목록 조회post](/reference/coin-withdrawal-address-book)
  * [출금 권한 __](/reference/coin-withdrawal)
    * [가상자산 출금 post](/reference/coin-withdrawal)
  * [주문 리워드 이벤트 __](/reference/order-reward-event)
    * [주문 리워드 종목 정보 조회 post](/reference/order-reward-programs)
    * [주문 리워드 내역 조회post](/reference/order-reward-history)



## Websocket

  * [Public 웹소켓 __](/reference/public-websocket-1)
    * [커넥션 관리 (PING)](/reference/public-websocket-ping)
    * [ 오더북 응답 (ORDERBOOK)](/reference/public-websocket-orderbook)
    * [티커 응답 (TICKER)](/reference/public-websocket-ticker)
    * [체결정보 응답 (TRADE)](/reference/public-websocket-trade)
    * [차트 응답 (CHART)](/reference/public-websocket-chart)
  * [Private 웹소켓 __](/reference/private-websocket-1)
    * [커넥션 관리 (PING)](/reference/private-websocket-1-ping)
    * [ 내 주문 변동 (MYORDER)](/reference/private-websocket-1-myorder)
    * [내 자산 변동 (MYASSET)](/reference/private-websocket-1-myasset)



## PRIVATE API

  * [잔고 조회 __](/reference/balance)
    * [잔고 조회 post](/reference/balance)
  * [고객 정보 __](/reference/deposit-address)
    * [입금 주소 조회 post](/reference/deposit-address)
    * [고객 정보 조회post](/reference/user-information)
    * [가상계좌 정보 조회post](/reference/virtual-account)
  * [주문 조회 __](/reference/my-complete-orders)
    * [체결 주문 조회 post](/reference/my-complete-orders)
    * [지정가 주문 조회post](/reference/my-limit-orders)
    * [특정 주문 조회post](/reference/my-order-information)
  * [주문 권한 __](/reference/cancel-order-1)
    * [주문 취소 post](/reference/cancel-order-1)
    * [지정가 매수 주문post](/reference/limit-buy)
    * [지정가 매도 주문post](/reference/limit-sell)
  * [입출금 조회 __](/reference/coin-transaction-history-1)
    * [가상자산 입출금 내역 조회 post](/reference/coin-transaction-history-1)
    * [원화 입출금 내역 조회post](/reference/krw-transaction-history-1)



## PUBLIC API V1 (Deprecated)

  * [오더북 조회get](/reference/orderbook-deprecated)
  * [티커 정보 조회get](/reference/ticker-1)
  * [티커 정보 조회 UTCget](/reference/ticker-utc-deprecated)
  * [최근 체결 주문 조회get](/reference/recent-complete-orders-deprecated)



Powered by [](https://readme.com?ref_src=hub&project=coinone)

# 오더북 조회

Ask AI

get

https://api.coinone.co.kr/public/v2/orderbook/{quote_currency}/{target_currency}

특정 종목의 오더북 정보 조회 (호가 단위 별)

## 

Path Params

[](#path-params)

field| type| required/optional| description  
---|---|---|---  
quote_currency| String| required| 마켓 기준 통화  
*예: KRW  
target_currency| String| required| 조회하려는 종목의 심볼  
*예: BTC  
  
## 

Query Params

[](#query-params)

field| type| required/optional| description  
---|---|---|---  
size| Enum| optional| 오더북 개수 (기본값 15)  
(5, 10, 15, 16) 4개 값만 허용  
order_book_unit| Number| optional| 모아보기 단위로 종목 정보 조회 응답의 order_book_unit 값을 사용  
(기본값 0.0)  
  
## 

Response Body

[](#response-body)

field| type| description  
---|---|---  
result| String| 정상 반환 시 success, 에러 코드 반환 시 error  
error_code| String| error 발생 시 에러코드 반환, 성공인 경우 0 반환  
timestamp| Number| 오더북의 최근 업데이트 시간 (ms)  
id| String| order book id 값, id 값이 클수록 최신 OrderBook 정보  
quote_currency| String| 마켓 기준 통화  
target_currency| String| 조회 요청한 종목  
order_book_unit| NumberString| 현재 오더북 단위  
bids| Array[Object]| 매수 오더북 정보  
-price| NumberString| 매수 호가  
-qty| NumberString| 매수 수량  
asks| Array[Object]| 매도 오더북 정보  
-price| NumberString| 매도 호가  
-qty| NumberString| 매도 수량  
  
Language

 __Shell __Node __Ruby __PHP __Python

Response

Click `Try It!` to start a request and see the response here!


---

# Source: https://docs.coinone.co.kr/docs/getting-started

ERROR: Failed to fetch: 404 Client Error: Not Found for url: https://docs.coinone.co.kr/docs/getting-started
