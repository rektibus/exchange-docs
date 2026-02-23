

  
    
    
    
    
    
    
    
    
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "G-TCF5LSR59D");
    
    코빗 API Docs
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  
    
      
      
        
          
            
            
              
            
            API

            
            
            
          
        
        
          
          
            Introduction시작Open API 소개API 키 생성API 키 관리REST API일반요청 보내기요청 수 제한자주 묻는 질문인증서명된 요청 보내기HMAC-SHA256 서명ED25519 서명시세현재가 조회GET호가 조회GET최근 체결 내역GET캔들스틱 조회GET거래지원 목록 조회GET호가 정책 조회GET주문개별 주문 조회GET미체결 주문 조회GET최근 주문 내역 조회GET최근 체결 내역 조회GET주문하기POST주문 취소하기DELETE자산자산 현황GET가상자산 입금입금 주소 전체 조회GET입금 주소 조회GET입금 주소 생성POST최근 입금내역 조회GET입금 진행상황 조회GET가상자산 출금출금 가능 주소 목록 조회GET출금 가능 수량 조회GET출금 요청POST출금 취소DELETE최근 출금내역 조회GET출금 진행상황 조회GET원화 입출금입금 요청POST출금 요청POST최근 입금내역 조회GET최근 출금내역 조회GET기타가상자산 정보 조회GET서버 시각 조회GET거래수수료율 조회GETAPI 키 정보 조회GETWebSocket API일반웹소켓 연결하기인증하기요청 보내기응답 메시지Public 타입현재가 (Ticker)호가 (Orderbook)체결 (Trade)Private 타입내 주문 (MyOrder)내 체결 (MyTrade)내 자산 (MyAsset)
          
        
      
      
        
          
          
          
          
            English
            개발자센터
            
              
                
                  
                  
                
              
              
              
                
                  
                    
                      라이트
                  
                  
                    
                      다크
                  
                  
                    
                      시스템 설정
                  
                
              
              
            
            
          
          
        
      
      
      
      
        
          
            
            
              
            
            API
          
          
            
            
              
                
                  
                
              
              
                
                  
                
              
            
            
            
              Open API 소개API 키 생성API 키 관리요청 보내기요청 수 제한자주 묻는 질문서명된 요청 보내기HMAC-SHA256 서명ED25519 서명현재가 조회호가 조회최근 체결 내역캔들스틱 조회거래지원 목록 조회호가 정책 조회개별 주문 조회미체결 주문 조회최근 주문 내역 조회최근 체결 내역 조회주문하기주문 취소하기자산 현황입금 주소 전체 조회입금 주소 조회입금 주소 생성최근 입금내역 조회입금 진행상황 조회출금 가능 주소 목록 조회출금 가능 수량 조회출금 요청출금 취소최근 출금내역 조회출금 진행상황 조회입금 요청출금 요청최근 입금내역 조회최근 출금내역 조회가상자산 정보 조회서버 시각 조회거래수수료율 조회API 키 정보 조회웹소켓 연결하기인증하기요청 보내기응답 메시지현재가 (Ticker)호가 (Orderbook)체결 (Trade)내 주문 (MyOrder)내 체결 (MyTrade)내 자산 (MyAsset)
            
          
        
      
      
    
    
      IntroductionOpen API 소개코빗의 새로운 Open API 서비스를 소개합니다! 가상자산의 시세 조회에서부터 주문, 입출금 등 가상자산 거래소의 다양한 기능을 Open API를 통해 자유롭게 이용할 수 있습니다.

코빗 회원이라면 누구나 코빗 Open API를 활용해서 직접 프로그램을 개발하거나 API 요청을 보내 거래소와 내 가상자산 거래 전략을 통합할 수 있습니다.

Open API에 관한 새로운 소식은 개발자센터에서 자세히 볼 수 있습니다. 이제 코빗 Open API를 활용해서 자신만의 프로그램이나 전략을 실행해 보세요!
REST API 기본 URL
https://api.korbit.co.kr
WebSocket API URL
wss://ws-api.korbit.co.kr/v2/public (Public 타입)
wss://ws-api.korbit.co.kr/v2/private (Private 타입)
API 키 생성코빗 Open API를 이용하려면 API 키를 생성해야만 합니다. 코빗 회원이라면 누구나 API 키를 개발자센터에서 만들 수 있습니다.

API 키를 만들 때에는 인증을 위한 서명 방식을 HMAC-SHA256과 ED25519 중에서 선택해야 합니다.

HMAC-SHA256 방식을 선택하면 코빗이 서명에 필요한 비밀 키(Secret Key)를 생성해서 이용자에게 제공하고, ED25519 방식을 선택하면 이용자가 직접 공개 키(Public Key)와 개인 키(Private Key)의 ED25519 키 페어(Key Pair)를 생성하고 공개 키를 API 키 생성 시에 코빗에 제공해야 합니다. 이후 Open API 이용 시, 인증이 필요한 API 요청을 보낼 때에 해당 API 키에 맞는 방식으로 서명된 API 요청을 보냄으로써 인증을 하게 됩니다.

HMAC-SHA256 방식은 코빗이 이용자의 비밀 키를 생성해 준다는 점에서 편리한 면이 있습니다. (코빗은 이용자의 비밀 키를 강력하게 암호화해서 보관합니다.) 이와 달리 ED25519 방식은 이용자가 직접 ED25519 키 페어를 생성해야 한다는 점에서 번거로운 면이 있으나 개인 키가 노출되지 않아 보안상 유리한 점이 있습니다. 더 자세한 내용은 개발자센터를 참조해 주세요.
ED25519 키 페어 생성 (Node.js)
import { generateKeyPairSync } from "crypto";

const { publicKey, privateKey } = generateKeyPairSync("ed25519", {
  publicKeyEncoding: {
    type: "spki",
    format: "pem",
  },
  privateKeyEncoding: {
    type: "pkcs8",
    format: "pem",
  },
});

// PKIX 형식의 공개 키와 PKCS #8 형식의 개인 키를 생성합니다.
console.log(publicKey, privateKey);
ED25519 키 페어 생성 (OpenSSL 사용)
# 개인 키 생성
openssl genpkey -algorithm ED25519 -out private_key.pem
# 공개 키 변환
openssl pkey -in private_key.pem -pubout -out public_key.pem
API 키 관리API 키는 개발자센터에서 권한 등의 내용을 수정하거나 API 키를 삭제할 수 있습니다. API 키는 생성한 때로부터 1년 간 유효하며, 설정된 권한에 따라 접근할 수 있는 기능에 차이가 있습니다. 예를 들어, 새로운 주문을 내거나 주문을 취소하고자 한다면 주문 신청 권한이 있는 API 키를 사용해야 합니다.

또한, API 키는 API 키마다 이용자가 설정한 IP 주소에서만 이용할 수 있습니다(최대 20개까지 입력 가능). 접속할 수 있는 IP 주소의 설정도 개발자센터에서 가능합니다.

API키를 추가, 수정, 삭제하는 경우, 변경사항이 반영되기까지 최대 1분정도 소요될 수 있습니다.
REST API요청 보내기API 요청 일반
REST API를 이용하기 위해서는 HTTP 요청을 Open API 서버(https://api.korbit.co.kr)로 보내야 합니다.

GET, DELETE 메소드 요청을 보낼 때에는 입력하려는 값을 URL 쿼리 스트링(Query String)으로, POST 메소드 요청을 보낼 때에는 입력하려는 값을 요청 본문(Body)에 application/x-www-form-urlencoded 형태로 입력해야 합니다. 입력 변수들의 순서는 무관합니다.

API 응답 일반
API 응답은 JSON 형태로 제공되며, 시간은 UNIX 타임스탬프(Timestamp)로 밀리초(ms) 단위에 맞춰 제공됩니다.

Public API
누구나 이용할 수 있게 공개된 퍼블릭 API인 시세 조회 등은 API 키나 인증이 필요하지 않습니다.

Private API
코빗 회원이 자신의 계정을 통해 이용할 수 있는 주문, 자산, 입출금 등의 프라이빗 API는 API 키를 발급받고 그에 맞게 서명된 API 요청을 보내 인증을 거침으로써 사용할 수 있습니다.

프라이빗 API는 API 키마다 설정할 수 있는 자산 조회, 주문 조회, 주문 신청, 입금 조회, 입금 신청, 출금 조회, 출금 신청의 7개 권한에 따라 접근 가능 여부가 달라집니다. 즉, Open API를 통해 가상자산 거래를 위해 주문을 내거나 낸 주문을 취소하고 싶다면 API 키에 주문 신청 권한을 부여하고, 거래만 가능하고 입출금은 할 수 없도록 제한을 두고 싶다면 입금 신청, 출금 신청 권한은 부여하지 않으면 됩니다.

서명에 관해서는 후술하는 서명된 요청 보내기 항목을 참조해 주세요.
요청 보내기
curl 'https://api.korbit.co.kr/v2/tickers?symbol=btc_krw'
요청 수 제한REST API 요청 시에는 요청 수 제한(Rate Limit)이 존재합니다. 이용자는 일정한 시간 동안 API 종류에 따라 각각 특정한 횟수만큼 API 요청을 보낼 수 있으며 요청 수 제한을 초과한 경우 429 Too Many Requests 오류가 발생할 수 있습니다. 단, 요청 수 제한을 초과함으로 인해서 얻는 불이익은 요청 수 제한이 풀릴 때까지 올바른 API 응답을 받을 수 없다는 것 외에는 없습니다.

Rate Limit 정책
요청 수 제한은 호가 조회 등 Public API는 IP 주소를 기준으로 측정되며, 주문하기 등 Private API는 회원 계정을 기준으로 측정됩니다(API 키가 아닌 회원 계정 기준입니다). API 종류에 따른 요청 수 제한 정책은 아래와 같습니다.


Public API: 초당 50회
주문하기: 초당 30회
주문 취소하기: 초당 30회
입출금 신청: 초당 5회
그 외 Private API: 초당 50회


잔여 요청 수는 HTTP 응답에서 `Ratelimit` 헤더의 `remaining` 값을 보시면 됩니다. `limit`는 해당 API Endpoint가 허용하는 최대 요청 수, `remaining`은 남은 허용 요청 수, `reset`는 요청 수 제한 초기화까지 남은 시간(초)입니다. `Ratelimit-Policy` 헤더는 해당 API Endpoint에 적용된 요청 수 제한 정책을 표시합니다(최대 요청 수;시간 윈도우(초)).
응답 헤더
200 OK
Ratelimit: limit=50, remaining=48, reset=1
Ratelimit-Policy: 50;w=1
응답 헤더
429 Too Many Requests
Retry-After: 1
Ratelimit-Policy: 30;w=1
자주 묻는 질문개발자센터에서 자주 묻는 질문을 제공하고 있습니다.

또한, 개발자센터에서 Private API를 이용하기 위한 HMAC-SHA256 또는 ED25519 서명된 요청을 보내는 코드 예시를 Go, Node.js, Python으로 작성해 제공하고 있습니다.

코빗 Open API는 비동기 시스템입니다. 따라서 응답 데이터에 약간의 지연이 있을 수 있으며, 이는 예상된 것으로 정상적인 작동입니다.

만일 한글 API 문서와 영문 API 문서에 차이가 있다면, 한글 API 문서가 우선합니다.

Open API 업데이트에 따라 API 응답에 항목이 추가될 수 있습니다. 따라서 Open API를 활용한 프로그램을 개발할 때, API 응답에 항목이 추가될 수 있음을 고려해 주세요.
서명된 요청 보내기아래에서는 API 키 생성 시에 선택한 인증 방식(HMAC-SHA256, ED25519)에 따라 API 요청을 서명하는 방법을 설명합니다. HMAC-SHA256 방식을 선택하면 코빗이 서명에 필요한 비밀 키(Secret Key)를 생성해서 이용자에게 제공하고, 이용자는 인증을 위해 그 비밀 키를 사용해서 HMAC-SHA256 방식으로 서명된 API 요청을 보내야 합니다.

ED25519 방식을 선택하면 이용자가 직접 ED25519 키 페어(Key Pair)를 생성하고 그 중 공개 키(Public Key)를 API 키 생성 시에 코빗에 제공해야 합니다. 그리고 이용자는 인증을 위해 키 페어 중 개인 키(Private Key)를 사용해서 ED25519 방식으로 서명된 API 요청을 보내야 합니다.

서명 일반
인증이 필요한 API 요청을 할 때에는 반드시 서명된 API 요청을 보내야 하고, 이를 위해 요청 변수에 signature, timestamp 변수를 추가로 반드시 입력해야 합니다.

서명은 signature로 입력하며, 입력하려는 변수들과 timestamp를 합친 문자열을 HMAC-SHA256 또는 ED25519 방식으로 서명한 결과 값입니다. 각 방식에 따른 서명 생성 방법은 아래 내용을 참조해 주세요. 서명은 URL 쿼리 스트링(Query String) 또는 요청 본문(Request Body)에 포함되어야 합니다.

시간 정보
서명을 할 때에는 시간 인증을 위해 현 시각의 UNIX 타임스탬프(Timestamp) 값을 밀리초(ms) 단위로 timestamp로 입력해야 합니다(필수). 따라서, 먼저 컴퓨터의 현재 시각이 표준 시각에 맞게 동기화되어 있는지 확인해야 합니다. (참고: 코빗 Open API 서버의 시각은 GET /v2/time API를 통해 확인할 수 있습니다.)

API 요청 시, 네트워크 또는 컴퓨터 환경 등의 지연으로 인해 클라이언트에서 서명을 한 때와 Open API 서버가 요청을 받은 때 사이에 시간차가 발생할 수 있습니다. 초를 다투는 가상자산 거래에서 시간의 중요성은 더 말할 필요가 없을 것입니다. 코빗 Open API에서는 이 시간차가 일정한 값보다 큰 경우, 요청을 무시하여 이용자의 의도와 다른 요청 결과가 발생할 가능성을 차단하도록 만들 수 있습니다.

이를 위해 recvWindow 변수를 추가로 입력해(단위: 밀리초) API 요청이 서명한 때로부터 유효한 시간을 이용자가 직접 지정할 수 있습니다. (recvWindow는 필수가 아니며, 입력하지 않을 경우 기본값은 5000이며(5초), 입력할 수 있는 최대값은 60000입니다.) 예를 들어, recvWindow=3000을 입력했다면, 코빗 Open API 서버가 요청을 수신한 때가 내가 입력한 timestamp보다 3초 이상 차이가 날 때 해당 요청은 거절됩니다.

마지막으로, timestamp 값은 코빗 Open API 서버의 현재 시각 대비 1000 (1초) 이상 큰 값을 입력하면 해당 요청은 거절됩니다.

시간 오차로 인해 API 요청이 거절된 경우 EXCEED_TIME_WINDOW 오류코드가 리턴되며, 이 경우 /v2/time API를 활용하여 서버 시각을 확인하여 주시기 바랍니다.
안정적인 동작을 위하여 NTP 시간 자동 동기화 기능을 사용하는 것을 추천합니다.
시간 정보 설명
 if (serverTime - timestamp <= recvWindow && timestamp < serverTime + 1000) {
    // 요청 처리
  } else {
    // 요청 거부
  }
HMAC-SHA256 서명빠른 안내
첨부된 Node.js 예제 코드를 참조해 주세요. API 키와 비밀 키만 본인의 것으로 바꾸면 해당 코드를 사용해 바로 주문을 입력할 수 있습니다.

필요 정보 확인
HMAC-SHA256 방식으로 인증을 진행하는 API 키(시스템 생성 키)를 생성하셨다면, 먼저 키 생성 시에 API 키와 함께 코빗에서 제공한 비밀 키를 확인해야 합니다. 그리고 해당 API 키가 원하시는 기능을 실행할 수 있는 권한이 있는지도 확인해 주세요.

요청 변수 입력
예를 들어, 주문하기 기능을 사용한다고 하면, 코빗 Open API에서 /v2/orders라는 주소로 POST 요청을 보내야 합니다. 그리고 주문하기 기능에서 요구하는 요청 변수들을 내 주문 내용에 맞춰 입력해야 합니다.

비트코인을 가격 1억 원에 1 BTC만큼 매수하겠다는 주문을 내려고 한다면, 즉, BTC/KRW 지정가 매수 주문(매수호가 100,000,000, 매수수량 1)을 내려고 한다면 다음과 같이 요청 변수들을 입력할 수 있습니다.

symbol은 btc_krw, side는 buy, price는 100000000, qty는 1이 됩니다. 그리고 timeInForce 값을 추가하면 GTC, IOC, FOK, Post Only를 설정할 수 있습니다만, 일반적인 단순한 지정가 주문은 GTC이므로 timeInForce를 생략하거나 또는 gtc로 입력해 줄 수도 있습니다. (지정가 주문은 timeInForce 기본값이 gtc로 설정됩니다.)

GET, DELETE 메소드 요청을 보낼 때에는 요청 변수를 URL 쿼리 스트링으로, POST 메소드 요청을 보낼 때에는 요청 본문에 application/x-www-form-urlencoded 형태로 입력해야 합니다.

타임스탬프 입력
다음으로는, 위에서 설명했듯 시간 정보를 입력해야 합니다. 현재 시각의 UNIX 타임스탬프(단위: 밀리초)를 timestamp라는 값으로 반드시 입력해야 합니다. 예제 코드에서는 recvWindow를 5000으로 설정했지만, recvWindow는 입력하지 않아도 됩니다. (입력하지 않을 경우 기본값 5000으로 설정됩니다.) 참고로 타임스탬프를 포함해 요청 변수들의 입력 순서는 무관합니다.

HMAC 서명 만들기
이제 메시지에 서명을 하기 위해서, 작성한 모든 요청 변수를 하나의 문자열로 합친 후, 비밀 키를 사용해 HMAC-SHA256 방식의 서명을 생성합니다.

즉, symbol=btc_krw&side=buy&price=100000000&qty=1&orderType=limit&timestamp=1719232467910 같은 문자열을 만들고, 이것을 비밀 키를 사용해 서명하게 됩니다. 각 프로그래밍 언어에 따른 HMAC-SHA256 서명 생성 방법은 API 문서 또는 개발자센터의 예제, 혹은 인터넷 검색이나 ChatGPT 등을 참고해 주세요.

아울러 모든 요청 변수를 하나로 합칠 때, 만일 URL 쿼리스트링과 HTTP 요청 본문에 각각 요청 변수가 존재한다면 그대로 두 문자열을 합치면 됩니다. 예를 들어, timestamp가 요청 본문이 아닌 URL 쿼리스트링에 timestamp=1719232467910 같이 있고, 요청 본문에는 symbol=btc_krw가 있다면, 서명을 해야 하는 문자열은 timestamp=1719232467910symbol=btc_krw이 됩니다. (주의: URL 쿼리스트링과 요청 본문을 합칠 때 &가 없습니다.)

서명이 생성되면, signature라는 이름으로 요청 변수에 더해주면 됩니다.

요청 보내기
이제 API 요청을 보낼 차례입니다. 주문하기와 같은 Private API 요청을 보낼 때에는 앞에서 만든 서명 메시지 외에, HTTP 요청 헤더에 X-KAPI-KEY라는 이름으로 API 키를 같이 전송해야 합니다. 만일 자동으로 HTTP 요청을 다루어 주는 라이브러리를 사용하지 않는다면, Content-Type으로 application/x-www-form-urlencoded도 추가해 주세요.

요청이 성공했다면, 주문이 되었다는 응답을 JSON 형태로 받을 수 있습니다. 물론 요청이 성공했어도 가상자산 매수를 위한 KRW 보유 자산이 충분하지 않다면 주문이 되지 않습니다.
HMAC-SHA256 서명 구현 (Node.js)
// Node.js 구현 예제
import crypto from "crypto";

const apiKey = "XyAZ_apaUv9pg4ZyGzNHTxabfIDrWIRpPBgk5-olIuM"; // API 키
const apiSecret = "ZwKS2evdxj9j3Neir2s0UHAmpNFfo4a0iHawEElGCBs"; // HMAC-SHA256 비밀 키

const baseUrl = "https://api.korbit.co.kr"; // 기본 URL

// HMAC-SHA256 서명 생성
const createHmacSignature = (query) => {
  return crypto.createHmac("sha256", apiSecret).update(query, "utf-8").digest("hex");
};

// 주문 접수 (POST 메소드 요청 예시)
const placeOrder = async (symbol, side, price, qty, orderType, timeInForce) => {
  const timestamp = Date.now(); // 현재 시각 타임스탬프(밀리세컨드)

  // 주문 정보(요청 변수)
  const params = new URLSearchParams({
    symbol: symbol,
    side: side,
    price: price,
    qty: qty,
    orderType: orderType,
    timeInForce: timeInForce,
    timestamp: timestamp,
  });

  // 주문 정보(요청 변수)를 바탕으로 서명 생성
  const signature = createHmacSignature(params.toString());

  // 서명을 요청 변수에 추가
  params.append("signature", signature);

  // 주문 접수 API Endpoint
  const url = `${baseUrl}/v2/orders`;

  const headers = {
    "X-KAPI-KEY": apiKey, // API 키
    "Content-Type": "application/x-www-form-urlencoded", // POST 요청일 때
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: headers,
      // POST 요청일 때, body에 요청 변수를 입력합니다.
      body: params.toString(),
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error Place Order:", error);
  }
};

// 주문 취소 (DELETE 메소드 요청 예시)
// HTTP 요청 메소드만 바꾸면 GET 요청 시에도 아래 코드를 사용할 수 있습니다.
const cancelOrder = async (symbol, orderId) => {
  const timestamp = Date.now(); // 현재 시각 타임스탬프(밀리세컨드)

  // 주문 정보
  const params = new URLSearchParams({
    symbol: symbol,
    orderId: orderId,
    timestamp: timestamp,
  });

  // 주문 정보를 바탕으로 서명을 생성
  const signature = createEd25519Signature(params.toString());

  // 주문 접수 API Endpoint
  const url = `${baseUrl}/v2/orders`;

  const headers = {
    "X-KAPI-KEY": apiKey, // API 키
  };

  // 서명을 요청 변수에 추가
  params.append("signature", signature);

  try {
    // GET, DELETE 메소드 사용시에는 URL Querystring으로 변수를 입력합니다.
    const response = await fetch(url + "?" + params.toString(), {
      method: "DELETE",
      headers: headers,
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error Cancel Order:", error);
  }
};

// BTC 매수 주문 전송
placeOrder("btc_krw", "buy", "90000000", "0.5", "limit", "gtc")
  .then((data) => console.log("Order Response:", data))
  .catch((err) => console.error("Order Error:", err));

// BTC, OrderID 1000001234 주문 취소
cancelOrder("btc_krw", 1000001234)
  .then((data) => console.log("Cancel Response:", data))
  .catch((err) => console.error("Cancel Error:", err));
ED25519 서명빠른 안내
첨부된 Node.js 예제 코드를 참조해 주세요. API 키와 개인 키만 본인의 것으로 바꾸면 해당 코드를 사용해 바로 주문을 입력할 수 있습니다.

필요 정보 확인
ED25519 방식으로 인증을 진행하는 API 키(이용자 생성 키)를 생성하셨다면, 먼저 키 생성 시에 코빗에 입력했던 제공한 개인 키를 확인해야 합니다. 그리고 해당 API 키가 원하시는 기능을 실행할 수 있는 권한이 있는지도 확인해 주세요.

요청 변수 입력
예를 들어, 주문하기 기능을 사용한다고 하면, 코빗 Open API에서 /v2/orders라는 주소로 POST 요청을 보내야 합니다. 그리고 주문하기 기능에서 요구하는 요청 변수들을 내 주문 내용에 맞춰 입력해야 합니다.

비트코인을 가격 1억 원에 1 BTC만큼 매수하겠다는 주문을 내려고 한다면, 즉, BTC/KRW 지정가 매수 주문(매수호가 100,000,000, 매수수량 1)을 내려고 한다면 다음과 같이 요청 변수들을 입력할 수 있습니다.

symbol은 btc_krw, side는 buy, price는 100000000, qty는 1이 됩니다. 그리고 timeInForce 값을 추가하면 GTC, IOC, FOK, Post Only를 설정할 수 있습니다만, 일반적인 단순한 지정가 주문은 GTC이므로 timeInForce를 생략하거나 또는 gtc로 입력해 줄 수도 있습니다. (지정가 주문은 timeInForce 기본값이 gtc로 설정됩니다.)

GET, DELETE 메소드 요청을 보낼 때에는 요청 변수를 URL 쿼리 스트링으로, POST 메소드 요청을 보낼 때에는 요청 변수를 요청 본문에 application/x-www-form-urlencoded 형태로 입력해야 합니다.

타임스탬프 입력
다음으로는, 위에서 설명했듯 시간 정보를 입력해야 합니다. 현재 시각의 UNIX 타임스탬프(단위: 밀리초)를 timestamp라는 값으로 반드시 입력해야 합니다. 예제 코드에서는 recvWindow를 5000으로 설정했지만, recvWindow는 입력하지 않아도 됩니다. (입력하지 않을 경우 기본값 5000으로 설정됩니다.) 참고로 타임스탬프를 포함해 요청 변수들의 입력 순서는 무관합니다.

ED25519 서명 만들기
이제 메시지에 서명을 하기 위해서, 작성한 모든 요청 변수를 하나의 문자열로 합친 후, 개인 키를 사용해 ED25519 방식의 서명을 생성합니다.

즉, symbol=btc_krw&side=buy&price=100000000&qty=1&orderType=limit&timestamp=1719232467910 같은 문자열을 만들고, 이것을 비밀 키를 사용해 서명하게 됩니다. 각 프로그래밍 언어에 따른 ED25519 서명 생성 방법은 API 문서 또는 개발자센터의 예제, 혹은 인터넷 검색이나 ChatGPT 등을 참고해 주세요.

그리고 생성된 ED25519 서명은 Base64 형식으로 인코딩해서 코빗으로 전송해야 합니다.

아울러 모든 요청 변수를 하나로 합칠 때, 만일 URL 쿼리스트링과 HTTP 요청 본문에 각각 요청 변수가 존재한다면 그대로 두 문자열을 합치면 됩니다. 예를 들어, timestamp가 요청 본문이 아닌 URL 쿼리스트링에 timestamp=1719232467910 같이 있고, 요청 본문에는 symbol=btc_krw가 있다면, 서명을 해야 하는 문자열은 timestamp=1719232467910symbol=btc_krw이 됩니다. (주의: URL 쿼리스트링과 요청 본문을 합칠 때 &가 없습니다.)

서명이 생성되면, signature라는 이름으로 요청 변수에 더해주면 됩니다.

요청 보내기
이제 API 요청을 보낼 차례입니다. 주문하기와 같은 Private API 요청을 보낼 때에는 앞에서 만든 서명 메시지 외에, HTTP 요청 헤더에 X-KAPI-KEY라는 이름으로 API 키를 같이 전송해야 합니다. 만일 자동으로 HTTP 요청을 다루어 주는 라이브러리를 사용하지 않는다면, Content-Type으로 application/x-www-form-urlencoded도 추가해 주세요.

ED25519 방식의 API 키를 사용할 때 주의할 점은, 앞서 signature를 Base64 형식으로 인코딩했기 때문에 이를 코빗으로 전송할 때 URL 인코딩을 빠트리지 않아야 한다는 점입니다. Node.js 예제에서처럼 문자열 변환 시 자동으로 이를 처리해주는 URLSearchParams 같은 것을 사용하거나 또는 HTTP 요청을 보낼 때 application/x-www-form-urlencoded이 설정되어 있다면 자동으로 내용을 URL 인코딩 해주는 라이브러리 등을 사용하지 않고 직접 HTTP 요청을 다룬다면 주의해 주세요. (cURL을 예로 들면  --data-urlencode를 설정해야)

요청이 성공했다면, 주문이 되었다는 응답을 JSON 형태로 받을 수 있습니다. 물론 요청이 성공했어도 가상자산 매수를 위한 KRW 보유 자산이 충분하지 않다면 주문이 되지 않습니다.
ED25519 서명 구현 (Node.js)
// Node.js 구현 예제
import crypto from "crypto";

const apiKey = "IrZybUY2WX-Quq_CHC5XQnq80CTVjUwd51TH3-yF6xY"; // API 키
const privateKeyPem = `-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIIyEYpSboChBdAqcvZUB7PVJNV37whhYeZq/wIo+PSej
-----END PRIVATE KEY-----`;

const baseUrl = "https://api.korbit.co.kr"; // 기본 URL

// ED25519 서명 생성
const createEd25519Signature = (data) => {
  const messageBuffer = Buffer.from(data);
  const signature = crypto.sign(null, messageBuffer, {
    key: privateKeyPem,
  });
  return signature.toString("base64");
};

// 주문 접수 (POST 메소드 요청 예시)
const placeOrder = async (symbol, side, price, qty, orderType, timeInForce) => {
  const timestamp = Date.now(); // 현재 시각 타임스탬프(밀리세컨드)

  // 주문 정보
  const params = new URLSearchParams({
    symbol: symbol,
    side: side,
    price: price,
    qty: qty,
    orderType: orderType,
    timeInForce: timeInForce,
    timestamp: timestamp,
  });

  // 주문 정보를 바탕으로 서명을 생성
  const signature = createEd25519Signature(params.toString());

  // 주문 접수 API Endpoint
  const url = `${baseUrl}/v2/orders`;

  const headers = {
    "X-KAPI-KEY": apiKey, // API 키
    "Content-Type": "application/x-www-form-urlencoded", // POST 요청일 때
  };

  // 서명 추가 (URLSearchParams: Base64 URL Safe)
  params.append("signature", signature);

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: headers,
      // POST 요청일 때, body에 요청 변수를 입력합니다.
      body: params.toString(),
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error Place Order:", error);
  }
};

// 주문 취소 (DELETE 메소드 요청 예시)
// HTTP 요청 메소드만 바꾸면 GET 요청 시에도 아래 코드를 사용할 수 있습니다.
const cancelOrder = async (symbol, orderId) => {
  const timestamp = Date.now(); // 현재 시각 타임스탬프(밀리세컨드)

  // 주문 정보
  const params = new URLSearchParams({
    symbol: symbol,
    orderId: orderId,
    timestamp: timestamp,
  });

  // 주문 정보를 바탕으로 서명을 생성
  const signature = createEd25519Signature(params.toString());

  // 주문 접수 API Endpoint
  const url = `${baseUrl}/v2/orders`;

  const headers = {
    "X-KAPI-KEY": apiKey, // API 키
  };

  // 서명 추가 (URLSearchParams: Base64 URL Safe)
  params.append("signature", signature);

  try {
    // GET, DELETE 메소드 사용시에는 URL Querystring으로 변수를 입력합니다.
    const response = await fetch(url + "?" + params.toString(), {
      method: "DELETE",
      headers: headers,
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error Cancel Order:", error);
  }
};

// BTC 매도 주문 전송
placeOrder("btc_krw", "sell", "100000000", "1.2345", "limit", "po")
  .then((data) => console.log("Order Response:", data))
  .catch((err) => console.error("Order Error:", err));

// BTC, OrderID 1000001234 주문 취소
cancelOrder("btc_krw", 1000001234)
  .then((data) => console.log("Cancel Response:", data))
  .catch((err) => console.error("Cancel Error:", err));
현재가 조회GET/v2/tickers
하나 또는 여러 거래쌍의 현재가(Ticker) 정보를 조회합니다.

요청 변수 (Query)



symbol
string


조회하고자 하는 거래쌍의 심볼을 입력합니다. 여러 거래쌍을 한 번에 조회하고자 한다면 콤마(,)로 구분해 입력합니다.
입력하지 않으면 코빗에서 거래 가능한 모든 거래쌍의 현재가 정보를 응답합니다.

예시btc_krw,eth_krw



응답 (Array)



symbol
string
필수

거래쌍

예시btc_krw




open
string
필수

최근 24시간 시가

예시361922.23




high
string
필수

최근 24시간 고가

예시361922.23




low
string
필수

최근 24시간 저가

예시361922.23




close
string
필수

최근 24시간 종가

예시361922.23




prevClose
string
필수

직전 24시간 종가

예시261922.23




priceChange
string
필수

직전 종가 대비 가격 변화량. prevClose - close으로 계산합니다.

예시261922.23




priceChangePercent
string
필수

직전 종가 대비 가격 변화율(단위: %). 100 * (prevClose - close) / prevClose으로 계산합니다.

예시10




volume
string
필수

최근 24시간 거래량(가상자산)

예시100




quoteVolume
string
필수

최근 24시간 거래대금(원화)

예시1000000000




bestBidPrice
string
필수

매수 1호가

예시5000




bestAskPrice
string
필수

매도 1호가

예시6000




lastTradedAt
number
필수

마지막 체결 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000


요청
curl 'https://api.korbit.co.kr/v2/tickers?symbol=btc_krw,eth_krw'
응답
{
  "success": true,
  "data": [
    {
      "symbol": "btc_krw",
      "open": "77060000",
      "high": "79650000",
      "low": "76550000",
      "close": "77136000",
      "prevClose": "77060000",
      "priceChange": "76000",
      "priceChangePercent": "0.1",
      "volume": "48.73739983",
      "quoteVolume": "3785149733.32633",
      "bestBidPrice": "77136000",
      "bestAskPrice": "77193000",
      "lastTradedAt": 1725525721041
    },
    {
      "symbol": "eth_krw",
      "open": "3259000",
      "high": "3370000",
      "low": "3222000",
      "close": "3250000",
      "prevClose": "3259000",
      "priceChange": "-9000",
      "priceChangePercent": "-0.28",
      "volume": "161.99278306",
      "quoteVolume": "532827941.01581",
      "bestBidPrice": "3251000",
      "bestAskPrice": "3254000",
      "lastTradedAt": 1725525545630
    }
  ]
}
호가 조회GET/v2/orderbook
단일 거래쌍의 호가 정보를 조회합니다.

요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




level
string


오더북 모아보기 단위. 모아보기 단위는 호가 정책 조회 API로 확인할 수 있습니다. 입력하지 않을 경우 모아보기를 적용하지 않습니다.

예시1000



응답



timestamp
number
필수

호가 정보의 기준 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000




bids
array of object
필수

매수 호가 정보 (호가 내림차순 정렬)





price
string
필수

매수호가

예시250000




qty
string
필수

매수잔량

예시10




amt
string


호가 금액 (오더북 모아보기를 사용하는 경우에만 세팅되며, 모아보기를 사용하지 않는 경우 price * qty로 계산할 수 있습니다.)

예시2500000






asks
array of object
필수

매도 호가 정보 (호가 오름차순 정렬)





price
string
필수

매도호가

예시250000




qty
string
필수

매도잔량

예시10




amt
string


호가 금액 (오더북 모아보기를 사용하는 경우에만 세팅되며, 모아보기를 사용하지 않는 경우 price * qty로 계산할 수 있습니다.)

예시2500000




요청
curl 'https://api.korbit.co.kr/v2/orderbook?symbol=btc_krw'
응답
{
  "success": true,
  "data": {
    "timestamp": 1708057740895,
    "bids": [
      {
        "price": "73303000",
        "qty": "0.00898326"
      },
      {
        "price": "73302000",
        "qty": "0.00790837"
      },
      {
        "price": "73301000",
        "qty": "0.00843099"
      },
      {
        "price": "73300000",
        "qty": "0.00054024"
      },
      {
        "price": "73299000",
        "qty": "0.00663446"
      }
    ],
    "asks": [
      {
        "price": "73304000",
        "qty": "0.00985212"
      },
      {
        "price": "73305000",
        "qty": "0.00367505"
      },
      {
        "price": "73306000",
        "qty": "0.0096254"
      },
      {
        "price": "73307000",
        "qty": "0.00502544"
      },
      {
        "price": "73308000",
        "qty": "0.00640584"
      }
    ]
  }
}
최근 체결 내역GET/v2/trades
최근 체결 내역을 조회합니다.

요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




limit
number


최대 조회 건수 (범위: 1 - 500)

예시100



응답 (Array)



timestamp
number
필수

체결 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000




price
string
필수

체결 가격

예시250000




qty
string
필수

체결량

예시10




isBuyerTaker
boolean
필수

매수 주문으로 인해 발생한 체결인지 여부

예시true




tradeId
number
필수

거래 체결 ID (각 거래쌍마다 생성된 개별 거래 체결 건의 ID)

예시1234


요청
curl 'https://api.korbit.co.kr/v2/trades?symbol=btc_krw&limit=4'
응답
{
  "success": true,
  "data": [
    {
      "timestamp": 1708057271149,
      "price": "70507000",
      "qty": "0.00981535",
      "isBuyerTaker": false
    },
    {
      "timestamp": 1708057271035,
      "price": "70508000",
      "qty": "0.00682475",
      "isBuyerTaker": false
    },
    {
      "timestamp": 1708057270922,
      "price": "70509000",
      "qty": "0.00844147",
      "isBuyerTaker": false
    },
    {
      "timestamp": 1708057270809,
      "price": "70510000",
      "qty": "0.00553963",
      "isBuyerTaker": false
    }
  ]
}
캔들스틱 조회GET/v2/candles
시세 캔들스틱 정보를 조회합니다.

요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




interval
string
필수

각 캔들 주기(단위)
허용되는 값:

1 1분
5 5분
15 15분
30 30분
60 1시간
240 4시간
1D 1일
1W 1주


예시60




start
number


조회 시작 시각(timestamp). 입력하지 않으면 거래쌍 상장 시점부터 조회합니다.

예시1619244573612




end
number


조회 종료 시각(timestamp). start보다 큰 값을 입력해야 합니다. 입력하지 않으면 현재 시점까지 조회합니다.

예시1715244369188




limit
number
필수

최대 조회 건수 (범위: 1 - 200)

예시100



응답 (Array)



timestamp
number
필수

캔들 시작 시각(timestamp)

예시1619244573612




open
string
필수

시가

예시361922.23




high
string
필수

고가

예시361922.23




low
string
필수

저가

예시361922.23




close
string
필수

종가

예시361922.23




volume
string
필수

거래량

예시100


요청
curl 'https://api.korbit.co.kr/v2/candles?symbol=btc_krw&interval=60&limit=5&end=1700000000000'
응답
{
  "success": true,
  "data": [
    {
      "timestamp": 1708041600000,
      "open": "71211000",
      "high": "9999990000",
      "low": "300000",
      "close": "71392000",
      "volume": "1.932320026577213946"
    },
    {
      "timestamp": 1708045200000,
      "open": "73510000",
      "high": "74605000",
      "low": "300000",
      "close": "72315000",
      "volume": "2.418698679231323743"
    },
    {
      "timestamp": 1708048800000,
      "open": "72315000",
      "high": "9999990000",
      "low": "300000",
      "close": "72380000",
      "volume": "1.947520219976227299"
    },
    {
      "timestamp": 1708052400000,
      "open": "70267000",
      "high": "74777000",
      "low": "300000",
      "close": "74049000",
      "volume": "2.254855048982521506"
    },
    {
      "timestamp": 1708056000000,
      "open": "68304000",
      "high": "74834000",
      "low": "68241000",
      "close": "74825000",
      "volume": "0.630193755379195341"
    }
  ]
}
거래지원 목록 조회GET/v2/currencyPairs

응답 (Array)



symbol
string
필수

거래쌍 심볼

예시btc_krw




status
string
필수

거래 가능 상태

launched 거래 가능
stopped 거래 중단


예시launched


요청
curl 'https://api.korbit.co.kr/v2/currencyPairs'
응답
{
  "success": true,
  "data": [
    {
      "symbol": "btc_krw",
      "status": "launched"
    },
    {
      "symbol": "eth_krw",
      "status": "launched"
    },
    {
      "symbol": "xrp_krw",
      "status": "stopped"
    }
  ]
}
호가 정책 조회GET/v2/tickSizePolicy
지정한 거래쌍의 호가 정책 및 오더북 모아보기 단위를 조회합니다.

요청 변수 (Query)



symbol
string
필수

거래쌍 심볼

예시xrp_krw



응답 (Array)



symbol
string
필수

거래쌍 심볼

예시xrp_krw




tickSizePolicy
array of object
필수

호가 정책 목록.
배열에서 주문가격 >= priceGte 조건을 만족하는 항목 중 가장 큰 priceGte 값을 가진 항목의 tickSize를 사용합니다.
예: 주문가격이 150원이라면, priceGte가 "100"인 항목의 tickSize를 사용합니다.





priceGte
string
필수

가격 범위 시작값 (이상)

예시0.1




tickSize
string
필수

해당 가격 범위의 호가 단위

예시0.0001






orderbookLevels
array of strings
필수

오더북 모아보기 단위 목록

예시["0.1", "1", "10", "100"]


요청
curl 'https://api.korbit.co.kr/v2/tickSizePolicy?symbol=xrp_krw'
응답
{
  "success": true,
  "data": [
    {
      "symbol": "xrp_krw",
      "tickSizePolicy": [
        {
          "priceGte": "0",
          "tickSize": "0.0001"
        },
        {
          "priceGte": "1",
          "tickSize": "0.001"
        },
        {
          "priceGte": "10",
          "tickSize": "0.01"
        },
        {
          "priceGte": "100",
          "tickSize": "0.1"
        },
        {
          "priceGte": "1000",
          "tickSize": "1"
        },
        {
          "priceGte": "5000",
          "tickSize": "5"
        },
        {
          "priceGte": "10000",
          "tickSize": "10"
        },
        {
          "priceGte": "50000",
          "tickSize": "50"
        },
        {
          "priceGte": "100000",
          "tickSize": "100"
        },
        {
          "priceGte": "500000",
          "tickSize": "500"
        },
        {
          "priceGte": "1000000",
          "tickSize": "1000"
        }
      ],
      "orderbookLevels": [
        "0.1",
        "1",
        "10",
        "100"
      ]
    }
  ]
}
개별 주문 조회GET/v2/orders
주문 ID(orderId) 또는 사용자 지정 주문 ID(clientOrderId)를 이용해 개별 주문 정보를 조회합니다.
단, expired, canceled 상태의 주문은 종결 후 약 3일이 지난 후에는 조회할 수 없습니다.

필요 권한
주문 조회
요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




orderId
number


주문 시 생성된 orderId 값. orderId와 clientOrderId 중 하나를 반드시 입력해야 합니다.

예시1234




clientOrderId
string


주문 시 입력한 clientOrderId 값. orderId와 clientOrderId 중 하나를 반드시 입력해야 합니다.

예시20141231-155959-abcdef



응답



orderId
number
필수

주문 ID

예시1234




clientOrderId
string


사용자 지정 주문 ID

예시20141231-155959-abcdef




symbol
string
필수

거래쌍의 심볼

예시btc_krw




orderType
string
필수

주문 유형 구분

limit 지정가 주문
market 시장가 주문
best BBO 주문 (Best-Bid-Offer, 최우선/최유리)


예시limit




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




timeInForce
string


주문 취소 조건

gtc 일반적인 지정가 주문. 전량 체결되거나 취소될 때까지 유효한 주문입니다. (Good-Till-Canceled)
ioc 주문호가 또는 더 좋은 가격으로 즉시 체결시킵니다. 체결되지 않은 잔량은 취소됩니다. (Immediate-Or-Cancel)
fok 주문호가 또는 더 좋은 가격으로 즉시 전량 체결시킵니다. 전량 체결이 불가하다면 주문이 취소됩니다. (Fill-Or-Kill)
po 주문 입력 시 바로 체결되는 상황이라면 주문이 취소됩니다. 즉, 메이커(Maker) 주문만 발생합니다. (Post-Only)

Time in Force 값을 입력하지 않았다면 다음 기본값이 설정됩니다.

지정가 주문: gtc
시장가 주문: ioc (시장가 주문에서는 ioc만 사용할 수 있습니다.)
BBO 주문에서는 Time in Force 값을 반드시 직접 입력해야 합니다.


예시gtc




price
string


지정가, BBO 주문의 주문 가격(호가).
시장가 주문은 주문 가격이 표시되지 않으며, BBO 주문은 주문 확정 이후 표시됩니다.

예시5000




qty
string


주문 수량 (가상자산). 지정가, BBO 및 시장가 매도 주문에서만 표시되며, BBO 매수 주문에서는 주문 확정 이후 표시됩니다.

예시10




amt
string


주문 대금 (KRW). 시장가 매수 및 BBO 매수 주문에서만 표시됩니다.

예시50000




filledQty
string
필수

체결량 (체결 수량)

예시10




filledAmt
string
필수

체결금액

예시50000




avgPrice
string


평균 체결 단가

예시5000




createdAt
number
필수

주문 접수 시각 (timestamp)

예시1700000000000




lastFilledAt
number


마지막 체결 시각 (timestamp)

예시1700000000000




triggeredAt
number


조건부 주문 발동 시각 (timestamp)

예시1700000000000




status
string
필수

주문 상태

pending 주문 접수 대기 중. 잔고가 부족하거나 timeInForce 조건에 해당할 경우, 주문이 실패해 expired 상태로 될 수 있습니다.
open 전량 미체결
filled 전량 체결
canceled 전량 취소
partiallyFilled 부분 체결
partiallyFilledCanceled 부분 체결 후 잔량 취소
expired 주문 접수 실패 (잔고 부족 또는 timeInForce 조건 해당 시)


예시partiallyFilled


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/orders?clientOrderId=20141231-155959-abcdef&symbol=btc_krw&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": {
    "orderId": 1234,
    "clientOrderId": "20141231-155959-abcdef",
    "symbol": "btc_krw",
    "orderType": "limit",
    "side": "buy",
    "timeInForce": "gtc",
    "avgPrice": "5000",
    "price": "5000",
    "qty": "10",
    "filledQty": "1",
    "filledAmt": "5000",
    "createdAt": 1700000000000,
    "lastFilledAt": 1700000000000,
    "status": "partiallyFilled"
  }
}
미체결 주문 조회GET/v2/openOrders
단일 거래쌍의 미체결 주문 목록을 조회합니다.
open, partiallyFilled 상태인 주문만 조회됩니다.

필요 권한
주문 조회
요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




limit
number


최대 조회 건수 (범위: 1 - 1000, 기본값 500)

예시100



응답 (Array)



orderId
number
필수

주문 ID

예시1234




clientOrderId
string


사용자 지정 주문 ID

예시20141231-155959-abcdef




orderType
string
필수

주문 유형 구분

limit 지정가 주문
market 시장가 주문
best BBO 주문 (Best-Bid-Offer, 최우선/최유리)


예시limit




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




price
string


지정가, BBO 주문의 주문 가격(호가).
시장가 주문은 주문 가격이 표시되지 않으며, BBO 주문은 주문 확정 이후 표시됩니다.

예시5000




qty
string


주문 수량 (가상자산). 지정가, BBO 및 시장가 매도 주문에서만 표시되며, BBO 매수 주문에서는 주문 확정 이후 표시됩니다.

예시10




amt
string


주문 대금 (KRW). 시장가 매수 및 BBO 매수 주문에서만 표시됩니다.

예시50000




filledQty
string
필수

체결량 (체결 수량)

예시10




filledAmt
string
필수

체결금액

예시50000




avgPrice
string


평균 체결 단가

예시5000




createdAt
number
필수

주문 접수 시각 (timestamp)

예시1700000000000




lastFilledAt
number


마지막 체결 시각 (timestamp)

예시1700000000000




status
string
필수

주문 상태

pending 주문 접수 대기 중. 잔고가 부족하거나 timeInForce 조건에 해당할 경우, 주문이 실패해 expired 상태로 될 수 있습니다.
open 전량 미체결
filled 전량 체결
canceled 전량 취소
partiallyFilled 부분 체결
partiallyFilledCanceled 부분 체결 후 잔량 취소
expired 주문 접수 실패 (잔고 부족 또는 timeInForce 조건 해당 시)


예시partiallyFilled


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/openOrders?limit=100&symbol=btc_krw&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "orderId": 1234,
      "orderType": "limit",
      "side": "buy",
      "avgPrice": "5000",
      "price": "5000",
      "qty": "10",
      "filledQty": "1",
      "filledAmt": "5000",
      "createdAt": 1700000000000,
      "lastFilledAt": 1700000000000,
      "status": "partiallyFilled"
    },
    {
      "orderId": 1235,
      "orderType": "limit",
      "side": "sell",
      "price": "5000",
      "qty": "10",
      "filledQty": "0",
      "filledAmt": "0",
      "createdAt": 1700000000000,
      "status": "open"
    },
  ],
}
최근 주문 내역 조회GET/v2/allOrders
단일 거래쌍의 최근 주문 목록을 조회합니다. 주문 생성 시각 기준으로 최근 36시간의 주문 내역만 조회 가능합니다.
이 API는 주문 이력 확인을 위한 것으로 제공되는 데이터에 수 초 가량의 지연이 발생할 수 있습니다.
지연 없는 현재 상태의 데이터가 필요할 경우 개별 주문 조회 또는 미체결 주문 조회 API를 사용해주세요.

필요 권한
주문 조회
요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




startTime
number


조회 시작 시각(timestamp). 현재 시간으로부터 36시간 전 자료까지만 조회 가능합니다. (기본값: 36시간 전)





endTime
number


조회 종료 시각(timestamp). (기본값: 현재)





limit
number


최대 조회 건수 (범위: 1 - 1000, 기본값 500)

예시100



응답 (Array)



orderId
number
필수

주문 ID

예시1234




clientOrderId
string


사용자 지정 주문 ID

예시20141231-155959-abcdef




symbol
string
필수

거래쌍의 심볼

예시btc_krw




orderType
string
필수

주문 유형 구분

limit 지정가 주문
market 시장가 주문
best BBO 주문 (Best-Bid-Offer, 최우선/최유리)


예시limit




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




timeInForce
string


주문 취소 조건

gtc 일반적인 지정가 주문. 전량 체결되거나 취소될 때까지 유효한 주문입니다. (Good-Till-Canceled)
ioc 주문호가 또는 더 좋은 가격으로 즉시 체결시킵니다. 체결되지 않은 잔량은 취소됩니다. (Immediate-Or-Cancel)
fok 주문호가 또는 더 좋은 가격으로 즉시 전량 체결시킵니다. 전량 체결이 불가하다면 주문이 취소됩니다. (Fill-Or-Kill)
po 주문 입력 시 바로 체결되는 상황이라면 주문이 취소됩니다. 즉, 메이커(Maker) 주문만 발생합니다. (Post-Only)

Time in Force 값을 입력하지 않았다면 다음 기본값이 설정됩니다.

지정가 주문: gtc
시장가 주문: ioc (시장가 주문에서는 ioc만 사용할 수 있습니다.)
BBO 주문에서는 Time in Force 값을 반드시 직접 입력해야 합니다.


예시gtc




price
string


지정가, BBO 주문의 주문 가격(호가).
시장가 주문은 주문 가격이 표시되지 않으며, BBO 주문은 주문 확정 이후 표시됩니다.

예시5000




qty
string


주문 수량 (가상자산). 지정가, BBO 및 시장가 매도 주문에서만 표시되며, BBO 매수 주문에서는 주문 확정 이후 표시됩니다.

예시10




amt
string


주문 대금 (KRW). 시장가 매수 및 BBO 매수 주문에서만 표시됩니다.

예시50000




filledQty
string
필수

체결량 (체결 수량)

예시10




filledAmt
string
필수

체결금액

예시50000




avgPrice
string


평균 체결 단가

예시5000




createdAt
number
필수

주문 접수 시각 (timestamp)

예시1700000000000




lastFilledAt
number


마지막 체결 시각 (timestamp)

예시1700000000000




triggeredAt
number


조건부 주문 발동 시각 (timestamp)

예시1700000000000




status
string
필수

주문 상태

pending 주문 접수 대기 중. 잔고가 부족하거나 timeInForce 조건에 해당할 경우, 주문이 실패해 expired 상태로 될 수 있습니다.
open 전량 미체결
filled 전량 체결
canceled 전량 취소
partiallyFilled 부분 체결
partiallyFilledCanceled 부분 체결 후 잔량 취소
expired 주문 접수 실패 (잔고 부족 또는 timeInForce 조건 해당 시)


예시partiallyFilled


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/allOrders?limit=100&symbol=btc_krw&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "orderId": 1234,
      "clientOrderId": "20141231-155959-abcdef",
      "symbol": "btc_krw",
      "orderType": "limit",
      "side": "buy",
      "timeInForce": "gtc",
      "avgPrice": "5000",
      "price": "5000",
      "qty": "10",
      "filledQty": "1",
      "filledAmt": "5000",
      "createdAt": 1700000000000,
      "lastFilledAt": 1700000000000,
      "status": "partiallyFilled"
    },
    {
      "orderId": 1235,
      "clientOrderId": "20141231-155959-abcdeg",
      "symbol": "btc_krw",
      "orderType": "limit",
      "side": "sell",
      "timeInForce": "gtc",
      "price": "5000",
      "qty": "10",
      "filledQty": "0",
      "filledAmt": "0",
      "createdAt": 1700000000000,
      "lastFilledAt": 1700000000000,
      "status": "open"
    },
  ],
}
최근 체결 내역 조회GET/v2/myTrades
단일 거래쌍의 최근 체결 목록을 조회합니다. 최근 36시간의 체결 내역만 조회 가능합니다.
이 API는 체결 이력 확인을 위한 API로 제공되는 데이터에 수 초 가량의 지연이 발생할 수 있습니다.

필요 권한
주문 조회
요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




startTime
number


조회 시작 시각(timestamp). 현재 시간으로부터 36시간 전 자료까지만 조회 가능합니다. (기본값: 36시간 전)





endTime
number


조회 종료 시각(timestamp). (기본값: 현재)





limit
number


최대 조회 건수 (범위: 1 - 1000, 기본값 500)

예시100



응답 (Array)



symbol
string
필수

거래쌍의 심볼

예시btc_krw




tradeId
number
필수

거래 체결 ID (각 거래쌍마다 생성된 개별 거래 체결 건의 ID)

예시1234




orderId
number
필수

원주문 ID

예시1234




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




price
string
필수

체결 단가

예시5000




qty
string
필수

체결 수량

예시10




amt
string
필수

체결 금액

예시50000




tradedAt
number
필수

주문 체결 시각(timestamp)

예시1700000000000




isTaker
boolean
필수

테이커(Taker) 체결 여부(Taker=true, Maker=false)

예시true




feeCurrency
string


수수료 지불 자산

예시krw




feeQty
string


수수료 수량

예시50


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/myTrades?limit=100&symbol=btc_krw&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "symbol": "btc_krw",
      "tradeId": 52,
      "orderId": 382312,
      "side": "buy",
      "price": "5000",
      "qty": "10",
      "amt": "50000",
      "tradedAt": 1700000000000,
      "isTaker": true,
      "feeCurrency": "krw",
      "feeQty": "50"
    }
  ],
}
주문하기POST/v2/orders
신규 주문을 생성합니다.

필요 권한
주문 신청
요청 변수 (POST)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




price
string


지정가 주문의 주문 가격.
시장가, BBO 주문의 경우 생략합니다.

예시250000




qty
string


주문 수량(가상자산).
지정가 주문과 시장가 매도 및 BBO 매도 주문인 경우 사용하며, 시장가 매수 및 BBO 매수 주문의 경우 생략합니다.

예시10




amt
string


주문 대금(KRW).
시장가 매수 및 BBO 매수 주문인 경우 사용하며, 지정가 주문과 시장가 매도 및 BBO 매도 주문의 경우 생략합니다.

예시250000




orderType
string
필수

주문 유형 구분

limit 지정가 주문
market 시장가 주문
best BBO 주문 (Best-Bid-Offer, 최유리/최우선 주문). BBO 주문은 timeInForce 및 bestNth 값을 반드시 입력해야 합니다.


예시limit




bestNth
number


주문 유형이 best인 경우 주문 가격을 선택합니다. (그 외 주문 유형에서는 생략합니다.)

timeInForce가 gtc, ioc, fok인 경우, 상대 방향 N호가(최유리)를 의미하며 1~5 사이의 값을 입력합니다.
timeInForce가 po인 경우, 자기 방향 N호가(최우선)를 의미하며 1~5 사이의 값을 입력합니다.


예시1




timeInForce
string


주문 취소 조건

gtc 일반적인 지정가 주문. 전량 체결되거나 취소될 때까지 유효한 주문입니다. (Good-Till-Canceled)
ioc 주문호가 또는 더 좋은 가격으로 즉시 체결시킵니다. 체결되지 않은 잔량은 취소됩니다. (Immediate-Or-Cancel)
fok 주문호가 또는 더 좋은 가격으로 즉시 전량 체결시킵니다. 전량 체결이 불가하다면 주문이 취소됩니다. (Fill-Or-Kill)
po 주문 입력 시 바로 체결되는 상황이라면 주문이 취소됩니다. 즉, 메이커(Maker) 주문만 발생합니다. (Post-Only)

Time in Force 값을 입력하지 않았다면 다음 기본값이 설정됩니다.

지정가 주문: gtc
시장가 주문: ioc (시장가 주문에서는 ioc만 사용할 수 있습니다.)
BBO 주문에서는 Time in Force 값을 반드시 직접 입력해야 합니다.


예시gtc




clientOrderId
string


사용자 지정 주문 ID. 동일한 clientOrderId로 여러 번 요청해도 한 번만 처리되며, GET /v2/orders API에서 clientOrderId로 주문을 검색할 수 있습니다.
숫자와 영문 대소문자 및 -, _, . 등으로 이루어진 문자열을 최대 36자까지 설정할 수 있습니다. 정규표현식: [0-9a-zA-Z.:_-]{1,36}
단, expired, canceled 상태의 주문은 종결 후 약 3일이 지난 후에는 clientOrderId로 검색할 수 없거나 그 clientOrderId를 다시 사용할 수 있습니다.

예시20141231-155959-abcdef




pp
string


가격 보호 사용 여부. true를 입력하면 가격 보호 기능을 사용해, 이 주문은 Taker 체결 시 가격 보호 범위 안에서만 체결되게 합니다.
ppPercent 값으로 가격 보호 범위를 설정할 수 있습니다.





ppPercent
string


가격 보호 범위. 1 이상 100 이하의 정수를 입력합니다. 가격 보호 범위가 5라면, 이 주문은 Taker 체결 시 중간가(매도 1호가와 매수 1호가의 중간) 대비 5% 내에서만 체결되고 체결되지 않은 수량은 취소됩니다.
가격 보호를 사용하지만 ppPercent를 입력하지 않았다면 거래소 기본값(5)을 사용합니다.




응답



orderId
number
필수

주문 ID

예시1234



오류 코드
Common Errors +DUPLICATE_CLIENT_ORDER_ID: 중복된 clientOrderId입니다.INVALID_CURRENCY_PAIR: 잘못된 거래쌍입니다.INVALID_USER_STATUS: 거래가 제한된 계정입니다. 코빗 웹사이트 또는 고객센터를 통해 상태를 확인하세요.BAD_REQUEST: 잘못된 입력입니다.NO_BALANCE: 잔고가 부족합니다.ONLY_SELL_LIMIT_ORDERS_ALLOWED: 거래지원 직후에는 지정가 매도 주문만 가능합니다.ORDER_VALUE_TOO_LARGE: 주문 최대 금액 초과입니다. 수량*가격을 10억원 이하로 변경해 주세요.ORDER_VALUE_TOO_SMALL: 주문 최소금액 미달입니다. 수량*가격을 5,000원 이상으로 변경해 주세요.PRICE_OVER_UPPER_BOUND: 거래지원 직후에는 특정한 가격 초과의 호가를 입력할 수 없습니다.PRICE_UNDER_LOWER_BOUND: 거래지원 직후에는 특정한 가격 미만의 호가를 입력할 수 없습니다.PRICE_TICK_SIZE_INVALID: 지정가 입력 단위가 올바르지 않습니다.TOO_MANY_OPEN_ORDERS: 미체결 주문 개수 제한을 초과했습니다.요청
curl -X POST -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/orders' -H Content-Type: application/x-www-form-urlencoded --data-raw orderType=limit&price=250000&qty=10&side=buy&symbol=btc_krw&timeInForce=gtc&timestamp=시각&signature=서명
응답
{
  "success": true,
  "data": {
    "orderId": 1234
  }
}
주문 취소하기DELETE/v2/orders
주문 취소 요청을 전송합니다.
API 요청이 성공한 경우 주문 취소 요청이 성공적으로 접수되었음을 뜻합니다.
오류 코드가 ORDER_ALREADY_CANCELED, ORDER_ALREADY_FILLED, ORDER_ALREADY_EXPIRED 중 하나인 경우, 지정한 주문이 이미 종결되었음을 뜻합니다.

필요 권한
주문 신청
요청 변수 (Query)



symbol
string
필수

대상 거래쌍의 심볼

예시btc_krw




orderId
number


주문하기 API에서 생성된 orderId 값. orderId와 clientOrderId 중 하나를 반드시 입력해야 합니다.

예시1234




clientOrderId
string


주문하기 API 요청 시 입력한 clientOrderId 값. orderId와 clientOrderId 중 하나를 반드시 입력해야 합니다.

예시20141231-155959-abcdef



오류 코드
Common Errors +ORDER_NOT_FOUND: 지정한 주문 ID가 존재하지 않습니다.ORDER_ALREADY_CANCELED: 지정한 주문이 이미 취소되었습니다.ORDER_ALREADY_FILLED: 지정한 주문이 이미 전량 체결되었습니다.ORDER_ALREADY_EXPIRED: 지정한 주문은 실패 처리된 주문입니다.TRY_AGAIN: 주문 접수 처리중입니다. 잠시 후 다시 시도해 주세요.요청
curl -X DELETE -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/orders?orderId=1234&symbol=btc_krw&timestamp=시각&signature=서명'
응답
{
  "success": true
}
자산 현황GET/v2/balance
내가 가지고 있는 자산 목록을 조회합니다.

필요 권한
자산 조회
요청 변수 (Query)



currencies
string


조회할 자산 목록. 콤마(,)로 구분하여 입력합니다. 입력하지 않으면 보유 중인 모든 자산을 조회합니다.

예시btc,eth



응답 (Array)



currency
string
필수

자산 이름

예시krw




balance
string
필수

보유 수량. 사용 가능 수량 + 거래 중 수량 + 출금 중 수량으로 계산합니다.

예시100




available
string
필수

사용 가능 수량

예시70




tradeInUse
string
필수

거래 중 수량

예시20




withdrawalInUse
string
필수

출금 중 수량

예시10




avgPrice
string
필수

매수평균가

예시5000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/balance?currencies=btc%2Ceth&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "currency": "btc",
      "balance": "100",
      "available": "70",
      "tradeInUse": "20",
      "withdrawalInUse": "10",
      "avgPrice": "5000"
    },
    {
      "currency": "eth",
      "balance": "100",
      "available": "70",
      "tradeInUse": "20",
      "withdrawalInUse": "10",
      "avgPrice": "5000"
    }
  ]
}
입금 주소 전체 조회GET/v2/coin/depositAddresses
가상자산 입금 주소 목록을 조회합니다.

필요 권한
입금 조회
응답 (Array)



currency
string
필수

가상자산 심볼

예시btc




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

입금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


입금 2차 주소 (Destination Tag, Memo 등. 없으면 null)



요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/depositAddresses?timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "currency": "btc",
      "network": "BTC",
      "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    },
    {
      "currency": "xrp",
      "network": "XRP",
      "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
      "secondaryAddress": "1234",
    }
  ]
}
입금 주소 조회GET/v2/coin/depositAddress
개별 가상자산의 입금 주소를 조회합니다.

필요 권한
입금 조회
요청 변수 (Query)



currency
string
필수

가상자산 심볼

예시btc




network
string


블록체인 네트워크 심볼.  네트워크 정보는 /v2/currencies API로 확인 가능합니다.
미입력시 해당 가상자산의 기본 네트워크를 사용합니다. 기본 네트워크는 변경될 수 있으므로, 오류를 방지하기 위하여 네트워크를 항상 명시해주시기 바랍니다.

예시BTC



응답



currency
string
필수

가상자산 심볼

예시btc




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

입금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


입금 2차 주소 (Destination Tag, Memo 등. 없으면 null)



요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/depositAddress?currency=btc&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": {
    "currency": "btc",
    "network": "BTC",
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
  }
}
입금 주소 생성POST/v2/coin/depositAddress
가상자산을 입금할 주소를 발급합니다. 입금 주소가 이미 존재한다면 신규 발급 없이 기존 입금 주소를 응답합니다.

필요 권한
입금 신청
요청 변수 (POST)



currency
string
필수

가상자산의 심볼

예시btc




network
string


블록체인 네트워크 심볼.  네트워크 정보는 /v2/currencies API로 확인 가능합니다.
미입력시 해당 가상자산의 기본 네트워크를 사용합니다. 기본 네트워크는 변경될 수 있으므로, 오류를 방지하기 위하여 네트워크를 항상 명시해주시기 바랍니다.

예시BTC



응답



currency
string
필수

가상자산 심볼

예시btc




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

입금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


입금 2차 주소 (Destination Tag, Memo 등. 없으면 null)



요청
curl -X POST -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/depositAddress' -H Content-Type: application/x-www-form-urlencoded --data-raw currency=btc&timestamp=시각&signature=서명
응답
{
  "success": true,
  "data": {
    "currency": "btc",
    "network": "BTC",
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
  }
}
최근 입금내역 조회GET/v2/coin/recentDeposits
최근 가상자산 입금 내역을 조회합니다.

필요 권한
입금 조회
요청 변수 (Query)



currency
string
필수

가상자산의 심볼

예시btc




limit
number
필수

최대 조회 건수 (범위: 1 - 100)

예시100



응답 (Array)



id
number
필수

코인 입금 ID

예시1234




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

입금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


입금 2차 주소 (Destination Tag, Memo 등. 없으면 null)





status
string
필수

입금 진행 상황

pending 블록체인 네트워크에서 입금 트랜잭션을 발견한 상태
actionRequired 입금계류 서류제출 대기 중 (입금을 위해서는 코빗 웹사이트에서 필요한 서류를 제출해야 합니다.)
reviewing 입금계류 제출서류 심사 중
done 입금 완료
refunded 심사 거절 후 입금 금액이 반환된 상태
failed 입금 실패 (입금 트랜잭션에 문제가 있는 경우 등)


예시done




transactionHash
string
필수

블록체인 트랜잭션 해시

예시0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f




currency
string
필수

입금 중인 가상자산의 심볼

예시btc




quantity
string
필수

입금 중인 가상자산의 수량 (트랜잭션에 기록되는 수량과 같음)

예시1.234




createdAt
number
필수

입금 수신 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/recentDeposits?currency=btc&limit=100&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "id": 1234,
      "network": "BTC",
      "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
      "secondaryAddress": null,
      "status": "done",
      "transactionHash": "0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
      "currency": "btc",
      "quantity": "1.234",
      "createdAt": 1700000000000
    }
  ]
}
입금 진행상황 조회GET/v2/coin/deposit
가상자산 입금 진행 상태를 조회합니다.

필요 권한
입금 조회
요청 변수 (Query)



currency
string
필수

가상자산의 심볼

예시btc




coinDepositId
number
필수

가상자산 입금 ID

예시1234



응답



id
number
필수

코인 입금 ID

예시1234




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

입금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


입금 2차 주소 (Destination Tag, Memo 등. 없으면 null)





status
string
필수

입금 진행 상황

pending 블록체인 네트워크에서 입금 트랜잭션을 발견한 상태
actionRequired 입금계류 서류제출 대기 중 (입금을 위해서는 코빗 웹사이트에서 필요한 서류를 제출해야 합니다.)
reviewing 입금계류 제출서류 심사 중
done 입금 완료
refunded 심사 거절 후 입금 금액이 반환된 상태
failed 입금 실패 (입금 트랜잭션에 문제가 있는 경우 등)


예시done




transactionHash
string
필수

블록체인 트랜잭션 해시

예시0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f




currency
string
필수

입금 중인 가상자산의 심볼

예시btc




quantity
string
필수

입금 중인 가상자산의 수량 (트랜잭션에 기록되는 수량과 같음)

예시1.234




createdAt
number
필수

입금 수신 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/deposit?coinDepositId=1234&currency=btc&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": {
    "id": 1234,
    "network": "BTC",
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "secondaryAddress": null,
    "status": "done",
    "transactionHash": "0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
    "currency": "btc",
    "quantity": "1.234",
    "createdAt": 1700000000000
  }
}
출금 가능 주소 목록 조회GET/v2/coin/withdrawableAddresses
API 출금 가능 주소로 등록된 주소를 조회합니다.

필요 권한
출금 조회
응답 (Array)



network
string
필수

블록체인 네트워크 심볼

예시ETH




currency
string


가상자산의 심볼. 네트워크를 대상으로 등록된 지갑 주소의 경우 생략되며, 이 경우 모든 자산을 출금할 수 있습니다.

예시btc




address
string
필수

등록된 출금 가능 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


2차 주소 (Destination Tag, Memo 등. 없으면 null)



요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/withdrawableAddresses?timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "network": "BTC",
      "currency": "btc",
      "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    },
    {
      "network": "ETH",
      "address": "0x05a56e2d52c817161883f50c441c3228cfe54d9f"
    }
  ]
}
출금 가능 수량 조회GET/v2/coin/withdrawableAmount
출금 가능 수량을 조회합니다.

필요 권한
출금 조회
요청 변수 (Query)



currency
string


가상자산의 심볼. 입력하지 않으면 모든 가상자산을 조회합니다.

예시btc



응답 (Array)



currency
string
필수

가상자산의 심볼

예시btc




withdrawableAmount
string
필수

출금 가능 수량

예시1.52




withdrawalInUseAmount
string
필수

출금 진행 중 수량

예시0.005


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/withdrawableAmount?currency=btc&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "currency": "btc",
      "withdrawableAmount": "1.52",
      "withdrawalInUseAmount": "0.005"
    },
    {
      "currency": "eth",
      "withdrawableAmount": "10.52",
      "withdrawalInUseAmount": "2.5"
    }
  ]
}
출금 요청POST/v2/coin/withdrawal
가상자산 출금을 요청합니다. 출금 API를 사용하기 위해서는, 코빗 개발자센터에서 API 출금 허용주소 등록이 필요합니다.

필요 권한
출금 신청
요청 변수 (POST)



currency
string
필수

출금할 가상자산의 심볼

예시btc




network
string


블록체인 네트워크 심볼.  네트워크 정보는 /v2/currencies API로 확인 가능합니다.
미입력시 해당 가상자산의 기본 네트워크를 사용합니다. 기본 네트워크는 변경될 수 있으므로, 오류를 방지하기 위하여 네트워크를 항상 명시해주시기 바랍니다.

예시BTC




amount
string
필수

출금할 가상자산의 수량 (수수료 별도)

예시0.02521236




address
string
필수

가상자산을 받을 주소. API 출금이 허용된 주소로만 출금할 수 있습니다.

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


2차 주소 (Destination Tag, Memo 등. 없으면 "" (빈 문자열) 세팅 또는 생략)




응답



status
string
필수

출금 진행상황

pending 출금 요청 접수됨
actionRequired (출금 취소 가능) 이메일 확인 대기 중. 계속 진행하기 위해서는 코빗 회원정보의 주소로 전송된 출금 확인 이메일을 확인해야 합니다.
reviewing (출금 취소 가능) 출금 심사 중. 코빗 정책에 따라 심사 후 출금이 지연될 수 있습니다.
processing 출금 처리 중
done 출금 완료
canceled 출금 취소
failed 출금 실패 (잔고 부족 또는 기타 오류)


예시pending




coinWithdrawalId
number
필수

출금 요청 건의 고유 ID

예시1234



오류 코드
Common Errors +INVALID_CURRENCY: 잘못된 가상자산 심볼입니다.WITHDRAWAL_SUSPENDED: 출금이 중단된 상태입니다.UNREGISTERED_WITHDRAWAL_ADDRESS: Open API 출금 허용 주소로 등록되어 있지 않은 주소입니다.FORBIDDEN_WITHDRAWAL_ADDRESS: 코빗 정책에 따라 출금이 불가능한 주소입니다.WITHDRAWAL_ALREADY_IN_PROGRESS: 이미 출금 진행 중입니다. 다른 출금 건이 완료된 후 다시 시도해 주세요.INVALID_USER_STATUS: 거래가 제한된 계정입니다. 코빗 웹사이트 또는 고객센터를 통해 상태를 확인하세요.NO_BALANCE: 잔고가 부족합니다. 참고: 잔고가 부족한 경우, `NO_BALANCE` 오류가 발생할 수도 있고 출금 요청은 성공했으나 출금 내역 조회 시 `failed` 상태로 표시될 수도 있습니다.DAILY_LIMIT_EXCEEDED: 일일 출금 한도를 초과했습니다.요청
curl -X POST -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/withdrawal' -H Content-Type: application/x-www-form-urlencoded --data-raw address=1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa&amount=0.02521236&currency=btc&timestamp=시각&signature=서명
응답
{
  "success": true,
  "data": {
    "status": "pending",
    "coinWithdrawalId": 1234
  }
}
출금 취소DELETE/v2/coin/withdrawal
가상자산 출금을 취소합니다.
해당 출금 건의 상태가 아래 중 하나인 경우에만 취소 가능합니다.

actionRequired
reviewing


필요 권한
출금 신청
요청 변수 (Query)



coinWithdrawalId
number
필수

출금 ID (출금 요청 API 응답에서 받은 값)

예시1234



오류 코드
Common Errors +WITHDRAWAL_ALREADY_FINISHED: 출금이 이미 완료되었습니다.CANNOT_CANCEL_WITHDRAWAL: 출금 취소가 불가능합니다. (출금 처리가 이미 시작된 경우 등)NOT_FOUND: 출금 정보가 존재하지 않습니다.요청
curl -X DELETE -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/withdrawal?coinWithdrawalId=1234&timestamp=시각&signature=서명'
응답
{
  "success": true
}
최근 출금내역 조회GET/v2/coin/recentWithdrawals
최근 가상자산 출금내역을 조회합니다.

필요 권한
출금 조회
요청 변수 (Query)



currency
string
필수

조회할 가상자산의 심볼

예시btc




limit
number
필수

최대 조회 건수 (범위: 1 - 100)

예시100



응답 (Array)



id
number
필수

가상자산 출금 ID

예시1234




quantity
string
필수

출금된 가상자산 수량. (수수료를 제외한 값으로 블록체인 트랜잭션에 기록되는 수량과 동일함)

예시1.234




fee
string
필수

출금 수수료

예시0.0001




currency
string
필수

출금 요청한 가상자산의 심볼

예시btc




status
string
필수

출금 진행상황

pending 출금 요청 접수됨
actionRequired (출금 취소 가능) 이메일 확인 대기 중. 계속 진행하기 위해서는 코빗 회원정보의 주소로 전송된 출금 확인 이메일을 확인해야 합니다.
reviewing (출금 취소 가능) 출금 심사 중. 코빗 정책에 따라 심사 후 출금이 지연될 수 있습니다.
processing 출금 처리 중
done 출금 완료
canceled 출금 취소
failed 출금 실패 (잔고 부족 또는 기타 오류)


예시done




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

출금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


출금 2차 주소 (Destination Tag, Memo 등. 없으면 null)





transactionHash
string


블록체인 트랜잭션 해시. (아직 네트워크로 전송되지 않았다면 null)

예시0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f




createdAt
number
필수

출금 요청 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/recentWithdrawals?currency=btc&limit=100&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "id": 1234,
      "quantity": "1.234",
      "fee": "0.0001",
      "currency": "btc",
      "status": "done",
      "network": "BTC",
      "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
      "secondaryAddress": null,
      "transactionHash": "0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
      "createdAt": 1700000000000
    }
  ]
}
출금 진행상황 조회GET/v2/coin/withdrawal
요청한 출금의 진행 상황을 조회합니다.

필요 권한
출금 조회
요청 변수 (Query)



currency
string
필수

조회할 가상자산의 심볼

예시btc




coinWithdrawalId
number
필수

가상자산 출금 ID

예시1234



응답



id
number
필수

가상자산 출금 ID

예시1234




quantity
string
필수

출금된 가상자산 수량. (수수료를 제외한 값으로 블록체인 트랜잭션에 기록되는 수량과 동일함)

예시1.234




fee
string
필수

출금 수수료

예시0.0001




currency
string
필수

출금 요청한 가상자산의 심볼

예시btc




status
string
필수

출금 진행상황

pending 출금 요청 접수됨
actionRequired (출금 취소 가능) 이메일 확인 대기 중. 계속 진행하기 위해서는 코빗 회원정보의 주소로 전송된 출금 확인 이메일을 확인해야 합니다.
reviewing (출금 취소 가능) 출금 심사 중. 코빗 정책에 따라 심사 후 출금이 지연될 수 있습니다.
processing 출금 처리 중
done 출금 완료
canceled 출금 취소
failed 출금 실패 (잔고 부족 또는 기타 오류)


예시done




network
string
필수

블록체인 네트워크 심볼

예시ETH




address
string
필수

출금 주소

예시1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa




secondaryAddress
string


출금 2차 주소 (Destination Tag, Memo 등. 없으면 null)





transactionHash
string


블록체인 트랜잭션 해시. (아직 네트워크로 전송되지 않았다면 null)

예시0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f




createdAt
number
필수

출금 요청 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/coin/withdrawal?coinWithdrawalId=1234&currency=btc&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": {
    "id": 1234,
    "quantity": "1.234",
    "fee": "0.0001",
    "currency": "btc",
    "status": "done",
    "network": "BTC",
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "secondaryAddress": null,
    "transactionHash": "0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
    "createdAt": 1700000000000
  }
}
입금 요청POST/v2/krw/sendKrwDepositPush
코빗 모바일 앱으로 원화 입금 요청 알림을 전송합니다.
알림 수신 후, 앱에서 인증을 완료해야 원화 입금이 진행됩니다.
알림 수신을 위해서는 앱 알림 설정에서 앱 푸시 알림 받기 설정이 되어 있어야 합니다.

필요 권한
입금 신청
요청 변수 (POST)



amount
string
필수

입금 요청할 금액

예시50000


요청
curl -X POST -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/krw/sendKrwDepositPush' -H Content-Type: application/x-www-form-urlencoded --data-raw amount=50000&timestamp=시각&signature=서명
응답
{"success":true}
출금 요청POST/v2/krw/sendKrwWithdrawalPush
코빗 모바일 앱으로 원화 출금 요청 알림을 전송합니다.
알림 수신 후, 앱에서 인증을 완료해야 원화 출금이 진행됩니다.
알림 수신을 위해서는 앱 알림 설정에서 앱 푸시 알림 받기 설정이 되어 있어야 합니다.

필요 권한
출금 신청
요청 변수 (POST)



amount
string
필수

출금 요청할 금액

예시50000


요청
curl -X POST -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/krw/sendKrwWithdrawalPush' -H Content-Type: application/x-www-form-urlencoded --data-raw amount=50000&timestamp=시각&signature=서명
응답
{"success":true}
최근 입금내역 조회GET/v2/krw/recentDeposits
최근 KRW 입금 내역을 조회합니다.

필요 권한
입금 조회
요청 변수 (Query)



limit
number
필수

최대 조회 건수 (범위: 1 - 100)

예시100




includeAll
string


전체 내역 조회 여부

false 일반 원화 입금만 (기본값)
true 원화 입금 외 예치금 이용료, 이벤트 보상 지급 등 포함





응답 (Array)



id
number
필수

KRW 입금 ID

예시1234




type
string


입금 구분 (includeAll=true인 경우)

general 일반 원화 입금
depositInterest 예치금 이용료
makerIncentive 메이커 인센티브
reward 이벤트 보상
etc 기타


예시depositInterest




status
string
필수

KRW 입금 진행 상황

pending 입금 접수중
processing 입금 처리중
reviewing 입금 심사중 (취소 가능)
done 입금 완료
canceling 입금 취소 접수됨
canceled 입금 취소 완료
failed 입금 실패


예시done




quantity
string
필수

입금 금액

예시1.234




createdAt
number
필수

입금 수신 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/krw/recentDeposits?limit=100&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "id": 1234,
      "status": "done",
      "quantity": "50000",
      "createdAt": 1700000000000
    }
  ]
}
최근 출금내역 조회GET/v2/krw/recentWithdrawals
최근 KRW 출금내역을 조회합니다.

필요 권한
출금 조회
요청 변수 (Query)



limit
number
필수

최대 조회 건수 (범위: 1 - 100)

예시100



응답 (Array)



id
number
필수

KRW 출금 ID

예시1234




quantity
string
필수

출금된 KRW 수량. (수수료 제외 수량)

예시50000




fee
string
필수

출금 수수료

예시1000




status
string
필수

KRW 출금 진행 상황

processing 출금 처리중
done 출금 완료
failed 출금 실패
canceled 출금 취소


예시done




createdAt
number
필수

출금 요청 시각(timestamp)

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/krw/recentWithdrawals?limit=100&timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "id": 1234,
      "quantity": "50000",
      "fee": "1000",
      "status": "done",
      "createdAt": 1700000000000
    }
  ]
}
가상자산 정보 조회GET/v2/currencies
가상자산 정보를 조회합니다.

응답 (Array)



name
string
필수

자산 심볼

예시btc




fullName
string
필수

자산 이름

예시Bitcoin




withdrawalStatus
string


(삭제 예정) 출금 가능 상태. networkList 하단의 withdrawalStatus 필드를 참조해주세요.





depositStatus
string


(삭제 예정) 입금 가능 상태. networkList 하단의 depositStatus 필드를 참조해주세요.





confirmationCount
string


(삭제 예정) 입금에 필요한 컨펌 수. networkList 하단의 confirmationCount 필드를 참조해주세요.





withdrawalTxFee
string


(삭제 예정) 출금 수수료. networkList 하단의 withdrawalTxFee 필드를 참조해주세요.





withdrawalMinAmount
string


(삭제 예정) 최소 출금 수량. networkList 하단의 withdrawalMinAmount 필드를 참조해주세요.





withdrawalMaxAmountPerRequest
string
필수

요청 1회당 최대 출금 수량

예시10




defaultNetwork
string


기본 네트워크 심볼

예시BTC




networkList
array of object
필수

지원하는 블록체인 네트워크 목록





name
string
필수

네트워크 심볼

예시ETH




fullName
string
필수

네트워크 이름

예시Ethereum




withdrawalStatus
string
필수

출금 가능 상태.
값:

launched 출금 가능
stopped 출금 중단


예시launched




depositStatus
string
필수

입금 가능 상태
값:

launched 입금 가능
stopped 입금 중단


예시launched




confirmationCount
string
필수

입금에 필요한 컨펌 수

예시3




withdrawalTxFee
string
필수

출금 수수료

예시0.0001




withdrawalMinAmount
string
필수

최소 출금 수량

예시0.00000001




withdrawalPrecision
number
필수

출금 수량의 소숫점 자릿수

예시8




hasSecondaryAddr
boolean
필수

2차 주소 존재 여부





contractAddress
string


컨트랙트 주소

예시0x6b3595068778dd592e39a122f4f5a5cf09c90fe2




addressExplorerUrl
string


블록체인 탐색기 주소

예시https://etherscan.io/address/




요청
curl 'https://api.korbit.co.kr/v2/currencies'
응답
{
    "success": true,
    "data": [
        {
            "name": "krw",
            "fullName": "Won",
            "withdrawalMaxAmountPerRequest": "5000000000",
            "depositStatus": "launched",
            "withdrawalStatus": "launched",
            "withdrawalTxFee": "1000",
            "withdrawalMinAmount": "1000"
        },
        {
            "name": "btc",
            "fullName": "Bitcoin",
            "withdrawalMaxAmountPerRequest": "120",
            "defaultNetwork": "BTC",
            "networkList": [
                {
                    "name": "BTC",
                    "fullName": "Bitcoin",
                    "depositStatus": "launched",
                    "withdrawalStatus": "launched",
                    "confirmationCount": 3,
                    "withdrawalTxFee": "0.0008",
                    "withdrawalMinAmount": "0.0001",
                    "withdrawalPrecision": 8,
                    "hasSecondaryAddr": false,
                    "addressExplorerUrl": "https://www.blockchain.com/ko/btc/address/"
                }
            ],
            "depositStatus": "launched",
            "withdrawalStatus": "launched",
            "confirmationCount": "3",
            "withdrawalTxFee": "0.0008",
            "withdrawalMinAmount": "0.0001"
        },
        {
            "name": "eth",
            "fullName": "Ethereum",
            "withdrawalMaxAmountPerRequest": "2000",
            "defaultNetwork": "ETH",
            "networkList": [
                {
                    "name": "ETH",
                    "fullName": "Ethereum",
                    "depositStatus": "launched",
                    "withdrawalStatus": "launched",
                    "confirmationCount": 45,
                    "withdrawalTxFee": "0.005",
                    "withdrawalMinAmount": "0.0001",
                    "withdrawalPrecision": 8,
                    "hasSecondaryAddr": false,
                    "addressExplorerUrl": "https://etherscan.io/address/"
                },
                {
                    "name": "BASE",
                    "fullName": "BASE",
                    "depositStatus": "launched",
                    "withdrawalStatus": "launched",
                    "confirmationCount": 1,
                    "withdrawalTxFee": "0.001",
                    "withdrawalMinAmount": "0.0001",
                    "withdrawalPrecision": 8,
                    "hasSecondaryAddr": false,
                    "addressExplorerUrl": "https://basescan.org/address/"
                }
            ],
            "depositStatus": "launched",
            "withdrawalStatus": "launched",
            "confirmationCount": "45",
            "withdrawalTxFee": "0.005",
            "withdrawalMinAmount": "0.0001"
        },
        {
            "name": "usdt",
            "fullName": "Tether",
            "withdrawalMaxAmountPerRequest": "500000",
            "defaultNetwork": "TRX",
            "networkList": [
                {
                    "name": "TRX",
                    "fullName": "Tron",
                    "depositStatus": "launched",
                    "withdrawalStatus": "launched",
                    "confirmationCount": 1,
                    "withdrawalTxFee": "1",
                    "withdrawalMinAmount": "1",
                    "withdrawalPrecision": 6,
                    "hasSecondaryAddr": false,
                    "addressExplorerUrl": "https://tronscan.org/#/address/"
                }
            ],
            "depositStatus": "launched",
            "withdrawalStatus": "launched",
            "confirmationCount": "1",
            "withdrawalTxFee": "1",
            "withdrawalMinAmount": "1"
        }
    ]
}
서버 시각 조회GET/v2/time
서버 시각을 조회합니다.

응답



time
number
필수

서버 시각(timestamp)

예시1700000000000


요청
curl 'https://api.korbit.co.kr/v2/time'
응답
{
  "success": true,
  "data": {
    "time": 1700000000000
  }
}
거래수수료율 조회GET/v2/tradingFeePolicy
현재 회원 계정에 적용되는 거래수수료율을 조회합니다.

요청 변수 (Query)



symbol
string


조회하려는 거래쌍을 입력합니다. 여러 거래쌍을 입력하려면 콤마(,)로 구분해 입력합니다. 입력하지 않으면 코빗에서 거래 가능한 모든 거래쌍의 정보를 응답합니다.

예시btc_krw,eth_krw



응답 (Array)



symbol
string
필수

거래쌍

예시btc_krw




buyFeeCurrency
string
필수

매수 주문시 수수료 수취 자산

예시btc




sellFeeCurrency
string
필수

매도 주문시 수수료 수취 자산

예시krw




maxFeeRate
string
필수

최대 수취 가능 수수료율. buyFeeCurrency가 krw인 거래쌍의 매수 주문 시, 수량*가격*maxFeeRate만큼의 KRW가 추가로 필요하며(사용 중 금액으로 전환) 주문이 체결되면 체결시 수수료율에 따라 정산됩니다.

예시0.0015




takerFeeRate
string
필수

테이커(Taker) 주문 체결시 수수료율

예시0.0007




makerFeeRate
string
필수

메이커(Maker) 주문 체결시 수수료율

예시0.0003


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/tradingFeePolicy?timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": [
    {
      "symbol": "btc_krw",
      "buyFeeCurrency": "btc",
      "sellFeeCurrency": "krw",
      "maxFeeRate": "0.0015",
      "takerFeeRate": "0.0015",
      "makerFeeRate": "0"
    },
    {
      "symbol": "eth_krw",
      "buyFeeCurrency": "eth",
      "sellFeeCurrency": "krw",
      "maxFeeRate": "0.0015",
      "takerFeeRate": "0.0015",
      "makerFeeRate": "0"
    },
    {
      "symbol": "etc_krw",
      "buyFeeCurrency": "krw",
      "sellFeeCurrency": "krw",
      "maxFeeRate": "0.0015",
      "takerFeeRate": "0.0015",
      "makerFeeRate": "0"
    },
    {
      "symbol": "xrp_krw",
      "buyFeeCurrency": "krw",
      "sellFeeCurrency": "krw",
      "maxFeeRate": "0.0015",
      "takerFeeRate": "0.0015",
      "makerFeeRate": "0"
    }
  ]
}
API 키 정보 조회GET/v2/currentKeyInfo
현재 사용중인 API 키의 정보를 조회합니다.

필요 권한
없음
응답



apiKey
string
필수

API 키 ID

예시FFSoRME97Sr7WBCMZJ_NO5Bj8MZ03EyArRzqyr1NKIA




type
string
필수

키 종류

hmac-sha256
ed25519


예시hmac-sha256




publicKey
string


ed25519 공개 키. 키 종류가 ed25519일 때만 출력됩니다.

예시-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAk+Yp3C31eFwoky+zyRNB6rAv/lgULTeghxTQpqwQHzM=
-----END PUBLIC KEY-----




permissions
array of strings
필수

API 키의 권한 목록

readBalances
readOrders
writeOrders
readDeposits
writeDeposits
readWithdrawals
writeWithdrawals


예시["readBalances", "readOrders"]




whitelist
string
필수

API 키의 접속 가능한 IP 주소 목록. 여러 개의 주소는 콤마(,)로 구분합니다.

예시1.2.3.4,5.6.7.8




expiration
number
필수

API 키 만료 시각

예시1700000000000




status
string
필수

API 키 상태

activated 활성화
deactivated 비활성화


예시activated




label
string


API 키 라벨

예시test key




createdAt
number
필수

API 키 생성 시각

예시1700000000000


요청
curl -H X-KAPI-KEY=API키 'https://api.korbit.co.kr/v2/currentKeyInfo?timestamp=시각&signature=서명'
응답
{
  "success": true,
  "data": {
    "apiKey": "FFSoRME97Sr7WBCMZJ_NO5Bj8MZ03EyArRzqyr1NKIA",
    "type": "ed25519",
    "publicKey": "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAk+Yp3C31eFwoky+zyRNB6rAv/lgULTeghxTQpqwQHzM=\n-----END PUBLIC KEY-----\n",
    "permissions": ["readBalances", "readOrders"],
    "expiration": 1700000000000,
    "status": "activated",
    "label": "test key",
    "createdAt": 1700000000000
  }
}
WebSocket API웹소켓 연결하기WebSocket API는 코빗 서버와 이용자 클라이언트 간의 양방향 통신을 위한 웹소켓 연결 인터페이스입니다. WebSocket API를 사용하면 코빗 가상자산 거래소의 실시간 정보를 가장 빠른 속도로 수신할 수 있습니다.

REST API를 사용할 경우에는 이용자가 HTTP 요청을 해서 응답을 받아야 비로소 정보를 알 수 있지만, WebSocket API를 사용할 경우에는 코빗 서버와 이용자 클라이언트 간 양방향 연결이 계속 이루어져 있어 시세 변동이나 주문 체결 등의 이벤트가 발생하면 코빗 서버에서 이용자 클라이언트로 실시간으로 정보를 지속적으로 제공합니다. 따라서, 시세나 주문, 체결 등의 실시간 정보를 빠르고 편리하게 수신하고자 한다면 REST API보다는 WebSocket API의 사용을 권장합니다.

WebSocket API에서 제공하는 데이터는 공개 정보인지, 개별 이용자만의 정보인지에 따라 Public 타입과 Private 타입으로 나눌 수 있으며, Public 타입 데이터는 별다른 인증 없이 수신할 수 있습니다. 반면, Private 타입 데이터를 수신하기 위해서는 웹소켓 연결 시 코빗 Open API 키 인증을 해야만 수신할 수 있습니다.

Public 타입 데이터는 웹소켓을 통한 데이터 구독 요청을 보내면, 요청 당시의 최신 데이터를 스냅샷 데이터로 바로 제공합니다. (스냅샷 데이터는 실시간 데이터가 아닙니다.) 스냅샷 데이터가 아닌 데이터는 모두 실시간 데이터입니다.

Public 타입 및 Private 타입의 웹소켓 접속 URL이 다르므로, 구독하고자 하는 타입에 맞는 URL로 접속해야 합니다.

시세: Public 타입
웹소켓 접속 URL: wss://ws-api.korbit.co.kr/v2/public

현재가 ticker : 지정한 거래쌍의 스냅샷, 실시간 현재가를 제공합니다.
호가 orderbook : 지정한 거래쌍의 스냅샷, 실시간 호가를 제공합니다.
체결 trade : 지정한 거래쌍의 스냅샷, 실시간 체결 내역을 제공합니다.

네트워크가 느리거나 트래픽이 과도할 경우, 일부 메시지가 드랍될 수 있습니다.

주문: Private 타입
웹소켓 접속 URL: wss://ws-api.korbit.co.kr/v2/private

내 주문 myOrder : 내 주문에 관한 실시간 상태 변화 정보를 제공합니다.
내 체결 myTrade : 내 체결에 관한 실시간 체결 발생 정보를 제공합니다.
내 자산 myAsset : 내 자산의 실시간 변동 내역을 제공합니다.

네트워크가 느리거나 트래픽이 과도할 경우, 웹소켓 커넥션이 강제 종료될 수 있으나 메시지가 드랍되지는 않습니다.

Public 타입 URL
wss://ws-api.korbit.co.kr/v2/public
Private 타입 URL
wss://ws-api.korbit.co.kr/v2/private
인증하기Public 타입 데이터(현재가, 호가, 체결)는 별다른 인증 없이 단순히 웹소켓 연결 후 구독 메시지를 보내는 것만으로 수신할 수 있습니다. 하지만, Private 타입 데이터(내 주문, 내 체결)는 웹소켓 연결 시 코빗 Open API 키를 이용한 인증을 거쳐야만 수신할 수 있습니다.

REST API의 인증 방법과 동일하게 웹소켓 연결 시 X-KAPI-KEY 헤더와 HMAC-SHA256 또는 ED25519 서명을 한 요청을 보내서 인증을 진행합니다. 즉, 요청 헤더에는 X-KAPI-KEY, URL 쿼리스트링에는 timestamp, signature 정보를 입력해야 합니다.

서명된 요청 보내기의 설명과 첨부하는 예시 코드를 참고해 주세요.
HMAC-SHA256 서명 구현 (Node.js)
// Node.js 구현 예제, 필요시 npm i ws 실행
import crypto from "crypto";
import WebSocket from "ws";

const apiKey = "XyAZ_apaUv9pg4ZyGzNHTxabfIDrWIRpPBgk5-olIuM"; // API 키
const apiSecret = "ZwKS2evdxj9j3Neir2s0UHAmpNFfo4a0iHawEElGCBs"; // HMAC-SHA256 비밀 키

const wsUrl = "wss://ws-api.korbit.co.kr/v2/private"; // Private 타입 접속 URL

// HMAC-SHA256 서명 생성
const createHmacSignature = (query) => {
  return crypto.createHmac("sha256", apiSecret).update(query, "utf-8").digest("hex");
};

const timestamp = Date.now(); // 현재 시각 타임스탬프(밀리세컨드)

const params = new URLSearchParams({
  timestamp: timestamp,
});

const signature = createHmacSignature(params.toString());

// 서명을 요청 변수에 추가
params.append("signature", signature);

// API 키를 요청 헤더에 추가하고 웹소켓 연결
const ws = new WebSocket(`${wsUrl}?${params.toString()}`, [], {
  headers: {
    "X-KAPI-KEY": apiKey,
  }
});

ws.on("open", () => {
  console.log("connected!");
  // 웹소켓 연결 후 메시지 구독 요청 전송
  ws.send(`[{"method":"subscribe","type":"myOrder","symbols":["btc_krw","eth_krw"]},{"method":"subscribe","type":"myTrade","symbols":["btc_krw","eth_krw"]}]`);
});

ws.on("error", (error) => {
  console.error('websocket error', error);
});

ws.on("message", (data) => {
  const message = JSON.parse(data);
  console.log(message);
});

ws.on("close", (code, message) => {
  console.log("connection closed!", code, message);
});

ws.on("unexpected-response", async (request, response) => {
  let data = '';
  for await (const chunk of response) {
    data += chunk;
  }
  console.log("websocket connect fail", response.statusCode, data);

  if (response.headers["content-type"]?.startsWith("application/json")) {
    const errorJson = JSON.parse(data)
    const msg = errorJson.error?.message
    // e.g.) EXCEED_TIME_WINDOW, KEY_NOT_FOUND, ...
    console.log("auth error", msg)
  }
});
요청 보내기웹소켓이 연결된 후에는 어떤 타입의 데이터를 구독하겠다는 요청을 보내야만 합니다. WebSocket API에서는 구독 요청 메시지를 JSON 형식으로 전송하고, method, type, symbols를 각각 입력해야 합니다.

여러 개의 메시지를 한 번에 입력할 수 있으므로, 요청 메시지는 1개를 보낼 때에도 반드시 대괄호([])로 묶어서 보내야 합니다. (대소문자 구분에 유의해 주세요.)

[{"method":"subscribe","type":"ticker","symbols":["btc_krw","eth_krw"]}]
[{"method":"subscribe","type":"ticker","symbols":["btc_krw","eth_krw"]},[{"method":"subscribe","type":"orderbook","symbols":["btc_krw","eth_krw"]}]]
# 예시로 Node.js 환경에서 wscat을 사용합니다.
$ npm install -g wscat
$ wscat -c wss://ws-api.korbit.co.kr/v2/public
connected (press CTRL+C to quit)

# 웹소켓이 연결되면 데이터 구독 요청을 보냅니다.
> [{"method":"subscribe","type":"ticker","symbols":["btc_krw","eth_krw"]}]
< {"symbol":"btc_krw","timestamp":1730365099072,"type":"ticker","snapshot":true,"data":{"open":"100500000","high":"100651000","low":"100492000","close":"100650000","prevClose":"100497000","priceChange":"153000","priceChangePercent":"0.15","volume":"0.89102242","quoteVolume":"89632429.21566","bestAskPrice":"100651000","bestBidPrice":"100650000","lastTradedAt":1730356819663}}
< {"symbol":"eth_krw","timestamp":1730365099072,"type":"ticker","snapshot":true,"data":{"open":"4390000","high":"4390000","low":"4357000","close":"4357000","prevClose":"4456000","priceChange":"-99000","priceChangePercent":"-2.22","volume":"0.1702132","quoteVolume":"744416.83456","bestAskPrice":"4357000","bestBidPrice":"4324000","lastTradedAt":1730361789775}}
< {"symbol":"btc_krw","timestamp":1730365220489,"type":"ticker","data":{"open":"100501000","high":"100651000","low":"100501000","close":"100650000","prevClose":"100492000","priceChange":"158000","priceChangePercent":"0.16","volume":"0.81866504","quoteVolume":"82360867.25161","bestAskPrice":"100651000","bestBidPrice":"100650000","lastTradedAt":1730356819663}}
위 예시에서는 비트코인(btc_krw)과 이더리움(eth_krw) 거래쌍에 대해 현재가(ticker) 정보를 받고 싶다는 구독 요청을 보내면, 가장 먼저 스냅샷 데이터가 수신되고 이후 실시간 데이터가 계속해서 수신됨을 알 수 있습니다. 여러 거래쌍에 관한 정보를 받고 싶다면 위 예시와 같이 여러 거래쌍을 대괄호([])로 감싼 후 콤마(,)로 구분해 입력합니다.

구독할 때에는 method를 subscribe로, 해당 타입의 데이터를 더 이상 받고 싶지 않다면 method를 unsubscribe로 해서 구독을 해제할 수 있습니다.

각 타입마다의 구독 요청 메시지 및 응답 예시는 아래를 참조해 주세요.
응답 메시지서버로부터 전송되는 응답 메시지에는 2가지 종류가 있습니다.

실시간 데이터
아래와 같이 status 필드가 존재하지 않는 메시지는 subscribe 요청을 통하여 구독한 실시간 데이터입니다.
{"type": "메시지 종류", ...}
{"type": "ticker", "timestamp": 1700000027754, "symbol": "btc_krw", "data": {...}}
제어 메시지
아래와 같이 status 필드를 가지는 메시지는 서버에서 처리 결과 또는 오류를 통지하기 위한 메시지입니다.
{"status": "success", "requestId": 1}
{"status": "fail", "requestId": 2, "code": "..."}
{"status": "error", "message": "..."}
기본적으로는 subscribe/unsubscribe 요청이 성공한 경우 별도의 응답이 전송되지 않으며, 실패한 경우에만 오류 메시지가 전송됩니다.

각 요청의 처리 결과를 확인하고 싶은 경우, 아래와 같이 임의의 정수를 요청 메시지의 requestId 필드에 입력하면 성공/실패 여부와 관계 없이 아래 예시와 같이 응답 메시지가 전송됩니다.

요청:
[{"requestId": 1, "method": "subscribe", "type": "myOrder", "symbols": ["btc_krw", "eth_krw"]}]
응답:
{"requestId": 1, "status": "success"}
{"requestId": 1, "status": "fail", "code": "INVALID_SYMBOL", "message": "The symbol does not exist (eth_btc)"}
현재가 (Ticker)현재가 정보를 조회합니다.

요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 ticker 입력





symbols
array of strings
필수

조회하고자 하는 거래쌍의 심볼을 입력합니다.

예시["btc_krw","eth_krw"]



응답



type
string
필수

고정 값 ticker





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




symbol
string
필수

거래쌍

예시btc_krw




snapshot
boolean


스냅샷 데이터 여부.
true - 구독 요청 직후 최초로 전송되는 메시지로서 요청 당시의 최신 정보를 전송합니다.
false 또는 null - 이벤트 발생에 따라 실시간으로 전송되는 메시지입니다.





data
object
필수






open
string
필수

최근 24시간 시가

예시361922.23




high
string
필수

최근 24시간 고가

예시361922.23




low
string
필수

최근 24시간 저가

예시361922.23




close
string
필수

최근 24시간 종가

예시361922.23




prevClose
string
필수

직전 24시간 종가

예시261922.23




priceChange
string
필수

직전 종가 대비 가격 변화량. prevClose - close으로 계산합니다.

예시261922.23




priceChangePercent
string
필수

직전 종가 대비 가격 변화율(단위: %). 100 * (prevClose - close) / prevClose으로 계산합니다.

예시10




volume
string
필수

최근 24시간 거래량(가상자산)

예시100




quoteVolume
string
필수

최근 24시간 거래대금(원화)

예시1000000000




bestBidPrice
string
필수

매수 1호가

예시5000




bestAskPrice
string
필수

매도 1호가

예시6000




lastTradedAt
number
필수

마지막 체결 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000




요청
[{"method":"subscribe","type":"ticker","symbols":["btc_krw","eth_krw"]}]
응답
{
  "type": "ticker",
  "timestamp": 1700000027754,
  "symbol": "btc_krw",
  "snapshot": true,
  "data": {
    "open": "94679000",
    "high": "111162000",
    "low": "93861000",
    "close": "99027000",
    "prevClose": "94679000",
    "priceChange": "4348000",
    "priceChangePercent": "4.59",
    "volume": "147.94385655",
    "quoteVolume": "14311735005.18033",
    "bestAskPrice": "99027000",
    "bestBidPrice": "99026000",
    "lastTradedAt": 1700000010022
  }
}
호가 (Orderbook)호가 정보를 조회합니다. 최대 30호가까지 조회 가능합니다.

요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 orderbook 입력





symbols
array of strings
필수

조회하고자 하는 거래쌍의 심볼을 입력합니다.

예시["btc_krw","eth_krw"]




level
string


오더북 모아보기 단위. 모아보기 단위는 호가 정책 조회 API로 확인할 수 있습니다. 입력하지 않을 경우 모아보기를 적용하지 않습니다.

예시1000



응답



type
string
필수

고정 값 orderbook





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




symbol
string
필수

거래쌍

예시btc_krw




snapshot
boolean


스냅샷 데이터 여부.
true - 구독 요청 직후 최초로 전송되는 메시지로서 요청 당시의 최신 정보를 전송합니다.
false 또는 null - 이벤트 발생에 따라 실시간으로 전송되는 메시지입니다.





data
object
필수






timestamp
number
필수

호가 정보의 기준 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000




bids
array of object
필수

매수 호가 정보 (호가 내림차순 정렬)





price
string
필수

매수호가

예시250000




qty
string
필수

매수잔량

예시10




amt
string


호가 금액 (오더북 모아보기를 사용하는 경우에만 세팅되며, 모아보기를 사용하지 않는 경우 price * qty로 계산할 수 있습니다.)

예시2500000






asks
array of object
필수

매도 호가 정보 (호가 오름차순 정렬)





price
string
필수

매도호가

예시250000




qty
string
필수

매도잔량

예시10




amt
string


호가 금액 (오더북 모아보기를 사용하는 경우에만 세팅되며, 모아보기를 사용하지 않는 경우 price * qty로 계산할 수 있습니다.)

예시2500000






요청
[{"method":"subscribe","type":"orderbook","symbols":["btc_krw"]}]
응답
{
  "type": "orderbook",
  "timestamp": 1700000006177,
  "symbol": "btc_krw",
  "snapshot": true,
  "data": {
    "timestamp": 1700000000234,
    "asks": [
      {
        "price": "99131000",
        "qty": "0.00456677"
      },
      {
        "price": "99132000",
        "qty": "0.00616665"
      },
      {
        "price": "99133000",
        "qty": "0.00808569"
      }
    ],
    "bids": [
      {
        "price": "99120000",
        "qty": "0.00363422"
      },
      {
        "price": "99119000",
        "qty": "0.00475577"
      },
      {
        "price": "99118000",
        "qty": "0.00389054"
      }
    ]
  }
}
체결 (Trade)최근 체결 내역을 조회합니다.

요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 trade 입력





symbols
array of strings
필수

조회하고자 하는 거래쌍의 심볼을 입력합니다.

예시["btc_krw","eth_krw"]



응답



type
string
필수

고정 값 trade





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




symbol
string
필수

거래쌍

예시btc_krw




snapshot
boolean


스냅샷 데이터 여부.
true - 구독 요청 직후 최초로 전송되는 메시지로서 요청 당시의 최신 정보를 전송합니다.
false 또는 null - 이벤트 발생에 따라 실시간으로 전송되는 메시지입니다.





data
array of object
필수






timestamp
number
필수

체결 시각 (단위: Unix Timestamp (밀리초))

예시1700000000000




price
string
필수

체결 가격

예시250000




qty
string
필수

체결량

예시10




isBuyerTaker
boolean
필수

매수 주문으로 인해 발생한 체결인지 여부

예시true




tradeId
number
필수

거래 체결 ID (각 거래쌍마다 생성된 개별 거래 체결 건의 ID)

예시1234




요청
[{"method":"subscribe","type":"trade","symbols":["btc_krw"]}]
응답
{
  "symbol": "btc_krw",
  "timestamp": 1700000005498,
  "type": "trade",
  "snapshot": true,
  "data": [
    {
      "timestamp": 1700000001239,
      "price": "98909000",
      "qty": "0.00146702",
      "isBuyerTaker": true,
      "tradeId": 123456
    }
  ]
}
내 주문 (MyOrder)주문 상태 변화를 실시간으로 조회합니다.

필요 권한
주문 조회
요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 myOrder 입력





symbols
array of strings
필수

조회하고자 하는 거래쌍의 심볼을 입력합니다.

예시["btc_krw","eth_krw"]



응답



channelType
string
필수

고정 값 myOrder





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




symbol
string
필수

거래쌍

예시btc_krw




order
object
필수






orders
array of object
필수






orderId
number
필수

주문 ID

예시1234




status
string
필수

주문 상태

pending 주문 접수 대기중. 잔고가 부족한 경우 주문이 실패해 expired 상태로 전환될 수 있습니다.
unfilled 전량 미체결 (REST API의 open 상태와 동일)
filled 전량 체결
canceled 전량 취소
partiallyFilled 부분 체결
partiallyFilledCanceled 부분 체결 후 잔량 취소
expired 주문 접수 실패


예시partiallyFilled




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




orderType
string
필수

주문 유형 구분

limit 지정가 주문
market 시장가 주문
best BBO 주문 (Best-Bid-Offer, 최우선/최유리)


예시limit




timeInForce
string


주문 취소 조건

gtc 일반적인 지정가 주문. 전량 체결되거나 취소될 때까지 유효한 주문입니다. (Good-Till-Canceled)
ioc 주문호가 또는 더 좋은 가격으로 즉시 체결시킵니다. 체결되지 않은 잔량은 취소됩니다. (Immediate-Or-Cancel)
fok 주문호가 또는 더 좋은 가격으로 즉시 전량 체결시킵니다. 전량 체결이 불가하다면 주문이 취소됩니다. (Fill-Or-Kill)
po 주문 입력 시 바로 체결되는 상황이라면 주문이 취소됩니다. 즉, 메이커(Maker) 주문만 발생합니다. (Post-Only)


예시gtc




price
string


지정가 주문의 주문 가격(주문호가).
시장가 주문은 주문 가격이 표시되지 않습니다.

예시5000




qty
string


주문 수량 (가상자산). 지정가, BBO 및 시장가 매도 주문에서만 표시되며, BBO 매수 주문에서는 주문 확정 이후 표시됩니다.

예시10




filledQty
string
필수

체결량 (체결 수량)

예시10




amt
string


주문 대금 (KRW). 시장가 매수 및 BBO 매수 주문에서만 표시됩니다.

예시50000




filledAmt
string
필수

체결금액

예시50000




avgPrice
string


평균 체결 단가

예시5000




createdAt
number
필수

주문 접수 시각 (timestamp)

예시1700000000000




lastFilledAt
number


마지막 체결 시각 (timestamp)

예시1700000000000




clientOrderId
string


주문 시 입력한 clientOrderId 값

예시20141231-155959-abcdef






요청
[{"method":"subscribe","type":"myOrder","symbols":["btc_krw"]}]
응답
{
  "symbol": "btc_krw",
  "timestamp": 1700000000000,
  "channelType": "myOrder",
  "order": {
    "orders": [
      {
        "orderId": 123456,
        "status": "partiallyFilled",
        "side": "buy",
        "orderType": "limit",
        "timeInForce": "gtc",
        "price": "99017000",
        "qty": "0.9",
        "filledQty": "0.53793136",
        "amt": "89115300",
        "filledAmt": "53260583.9536",
        "avgPrice": "99010000",
        "createdAt": 1700000001000,
        "lastFilledAt": 1700000002000,
        "clientOrderId": "tjcfiDfSjq94giNAat31"
      }
    ]
  }
}
내 체결 (MyTrade)내 주문의 체결 내역을 실시간으로 조회힙니다.

필요 권한
주문 조회
요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 myTrade 입력





symbols
array of strings
필수

조회하고자 하는 거래쌍의 심볼을 입력합니다.

예시["btc_krw","eth_krw"]



응답



channelType
string
필수

고정 값 myTrade





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




symbol
string
필수

거래쌍

예시btc_krw




trade
object
필수






trades
array of object
필수






tradeId
number
필수

거래 체결 ID (각 거래쌍마다 생성된 개별 거래 체결 건의 ID)

예시1234




orderId
number
필수

원주문 ID

예시1234




side
string
필수

매수, 매도 구분

buy 매수
sell 매도


예시buy




price
string
필수

체결 단가

예시5000




qty
string
필수

체결 수량

예시10




fee
string
필수

수수료

예시10




feeCurrency
string
필수

수수료 자산

예시krw




filledAt
number
필수

체결 시각 (timestamp)

예시1700000000000




isTaker
boolean
필수

테이커(Taker) 체결 여부(Taker=true, Maker=false)

예시true






요청
[{"method":"subscribe","type":"myTrade","symbols":["btc_krw"]}]
응답
{
  "symbol": "btc_krw",
  "timestamp": 1700000001000,
  "channelType": "myTrade",
  "trade": {
    "trades": [
      {
        "tradeId": 123456,
        "orderId": 456789,
        "side": "buy",
        "price": "99051000",
        "qty": "0.0013",
        "fee": "50",
        "feeCurrency": "krw",
        "filledAt": 1700000000000,
        "isTaker": true
      }
    ]
  }
}
내 자산 (MyAsset)내 자산의 변동 내역을 실시간으로 조회힙니다.

필요 권한
자산 조회
요청 변수



method
string
필수

고정 값 subscribe 또는 unsubscribe 입력





type
string
필수

고정 값 myAsset 입력




응답



channelType
string
필수

고정 값 myAsset





timestamp
number
필수

현재 서버 시간 (단위: Unix Timestamp (밀리초))

예시1700000000000




asset
object
필수






assets
array of object
필수






currency
string
필수

자산 이름

예시krw




balance
string
필수

보유 수량. 사용 가능 수량 + 거래 중 수량 + 출금 중 수량으로 계산합니다.

예시100




available
string
필수

사용 가능 수량

예시70




tradeInUse
string
필수

거래 중 수량

예시20




withdrawalInUse
string
필수

출금 중 수량

예시10




avgPrice
string
필수

매수평균가

예시5000




updatedAt
number
필수

변동 시각

예시1700000000000






요청
[{"method":"subscribe","type":"myAsset"}]
응답
{
  "timestamp": 1700000001000,
  "channelType": "myAsset",
  "asset": {
    "assets": [
      {
        "currency": "btc",
        "balance": "10",
        "available": "7",
        "tradeInUse": "2",
        "withdrawalInUse": "1",
        "avgPrice": "50000",
        "updatedAt": 1700000000000
      },
      {
        "currency": "eth",
        "balance": "100",
        "available": "70",
        "tradeInUse": "20",
        "withdrawalInUse": "10",
        "avgPrice": "5000",
        "updatedAt": 1700000000000
      }
    ]
  }
}

    
  

