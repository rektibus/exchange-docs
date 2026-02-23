Address
Gopax WebSocket API can be accessed via the following address.

wss://wsapi.gopax.co.kr

 Example code is presented to roughly show how to use WebSocket API, not to present the best practice. Never use the example code in a production environment.
Authentication
import time, base64, hmac, hashlib, json
from urllib.parse import quote
from websocket import create_connection  # pip install websocket-client

API_KEY = '<Insert Yours>'
SECRET = '<Insert Yours>'

timestamp = str(int(time.time() * 1000))
msg = 't' + timestamp
key = base64.b64decode(SECRET)
signature = base64.b64encode(
  hmac.new(key, str(msg).encode('utf-8'), hashlib.sha512).digest()
).decode()

url = 'wss://wsapi.gopax.co.kr?apiKey={}&timestamp={}&signature={}'
url = url.format(quote(API_KEY), timestamp, quote(signature))
ws_conn = create_connection(url, timeout=10)
ws_conn.settimeout(None)

request = {
  'i': 1,  # can be omitted
  'n': 'SubscribeToOrderBook',
  'o': {'tradingPairName': 'BCH-KRW'}
}
ws_conn.send(json.dumps(request))

while True:
  raw_response = ws_conn.recv()
  if raw_response.startswith('"primus::ping::'):  # see the double quote
    ws_conn.send('"primus::pong::' + raw_response[15:])
  else:
    response = json.loads(raw_response)
    print(json.dumps(response, indent=2))
An API key and its secret are needed to use Gopax WebSocket API, which can be issued via Gopax's website.

Authentication is done through the following procedure:

Get a current timestamp in milliseconds without a decimal point.
Sign 't' + timestamp with the secret as the key to generate a signature.
Open a connection while sending apiKey, timestamp and signature as a query string.
If the connection is opened, it means that it has been authenticated and is ready to subscribe to real-time data.
The server sends a ping every 30 seconds (e.g. "primus::ping::1591318325140"). The user has to send back a pong within 30 seconds (e.g. "primus::pong::1591318325140"). If the server doesn't receive a pong within that time, the connection will be disconnected.

 Legacy API keys consist of 36 characters whereas API keys of the current version consist of 64 characters. In case you have a legacy API key, issue a new API key since legacy API keys cannot be used for WebSocket API.
 If the timestamp has a discrepancy of more than 5 seconds compared to the standard time, it can be rejected by the server. Check your time settings carefully.
 Each connection has a maximum age of 24 hours. If it expires, the connection is disconnected by the server. Moreover, in case of a service update, the connection might be disconnected without any notice.
 20 Concurrent connections can be opened at max per API key. Moreover, you can't try opening connections quicker than 20 times a second. If violated, the server returns a TOO_MANY_REQUESTS (429) error.
Private APIs
Private APIs need authentication.

Subscription to Outstanding Orders
Outstanding orders (i.e. pending orders on order books) can be subscribed to.

Request
{
  "n": "SubscribeToOrders",
  "o": {}
}

Response
Outstanding orders are returned as a response.

{
  "n": "SubscribeToOrders",
  "o": {
    "data": [
      {
        "orderId": 327347,            # order ID
        "status": 1,                  # 1(not filled), 2(canceled), 3(completely filled), 4(partially filled), 5(reserved)
        "side": 2,                    # 1(bid), 2(ask)
        "type": 1,                    # 1(limit), 2(market)
        "price": 5500000,             # price
        "orgAmount": 1,               # initially placed amount
        "remainAmount": 1,            # unfilled or remaining amount
        "createdAt": 1597218137,      # placement time
        "updatedAt": 1597218137,      # last update time
        "tradedBaseAmount": 0,        # filled base asset amount (in ZEC for this case)
        "tradedQuoteAmount": 0,       # filled quote asset amount (in KRW for this case)
        "feeAmount": 0,               # fee amount
        "feeAssetName": "KRW",        # fee asset name
        "rewardAmount": 0,            # reward amount
        "rewardAssetName": "KRW",     # reward asset name
        "timeInForce": 0,             # 0(gtc), 1(post only), 2(ioc), 3(fok)
        "protection": 1,              # 1(not applied), 2(applied)
        "forcedCompletionReason": 0,  # 0(n/a), 1(timeInForce), 2(protection)
        "stopPrice": 0,               # stop price (> 0 only for stop orders)
        "takerFeeAmount": 0,          # fee amount paid as a taker position
        "tradingPairName": "ZEC-KRW"  # order book
      },
      ...
    ]
  }
}

Delta Push
Once subscribed, every delta (or change) is pushed in real-time.

When a BID order for 0.2 ZEC at 5,500,000 KRW / ZEC is placed, the following delta will be pushed.

{
  "i": -1,                            # always -1 in case of delta push
  "n": "OrderEvent",
  "o": {
    "orderId": 327347,
    "status": 4,                      # changed to 4(partially filled)
    "side": 2,
    "type": 1,
    "price": 5500000,
    "orgAmount": 1,
    "remainAmount": 0.8,              # -0.2 as 0.2 ZEC is filled
    "createdAt": 1597218137,
    "updatedAt": 1599093631,          # updated
    "tradedBaseAmount": 0.2,          # 0.2 ZEC goes out
    "tradedQuoteAmount": 1100000,     # 1,100,000 KRW comes in
    "feeAmount": 440,                 # fee amount (0.04% for this case)
    "feeAssetName": "KRW",            # fee asset name
    "rewardAmount": 0,                # reward amount
    "rewardAssetName": "KRW",         # reward asset name
    "timeInForce": 0,
    "protection": 1,
    "forcedCompletionReason": 0,
    "stopPrice": 0,
    "takerFeeAmount": 0,
    "tradingPairName": "ZEC-KRW"
  }
}

Subscription to Balances
Balances can be subscribed to.

Request
{
  "n": "SubscribeToBalances",
  "o": {}
}

Response
Balances are returned as a response.

{
  "n": "SubscribeToBalances",
  "o": {
    "result": true,
    "data": [
      ...
      {
        "assetId": 7,                     # asset ID
        "avail": 989.4998,                # amount that can be used to place an order
        "hold": 2,                        # amount that is outstanding on order books
        "pendingWithdrawal": 0,           # amount that is being withdrawn
        "blendedPrice": 429413.08986192,  # average purchase price
        "lastUpdatedAt": 1599097996.779,  # last update time
        "isoAlpha3": "ZEC"                # asset name
      },
      ...
  }
}

Delta Push
Once subscribed, every delta (or change) is pushed in real-time.

When an order with 1 ZEC remaining is cancelled, the following delta will be pushed.

{
  "i": -1,                                # always -1 in case of delta push
  "n": "BalanceEvent",
  "o": {
    "assetId": 7,
    "avail": 990.4998,                    # +1 as you can use 1 ZEC more to place a new order
    "hold": 1,                            # -1 as you take it back from an order book
    "pendingWithdrawal": 0,
    "blendedPrice": 429413.08986192,
    "lastUpdatedAt": 1599098077.27,
    "isoAlpha3": "ZEC"
  }
}

Subscription to Trades
Trades can be subscribed to.

Request
{
  "n": "SubscribeToTrades",
  "o": {}
}

Response
An empty response is returned.

{
  "n": "SubscribeToTrades",
  "o": {}
}

Delta Push
Once subscribed, every delta (or change) is pushed in real-time.

{
  "i": -1,
  "n": "TradeEvent",
  "o": {
    "tradeId": 74072,             # trade ID
    "orderId": 453529,            # order ID
    "side": 2,                    # 1(bid), 2(ask)
    "type": 1,                    # 1(limit), 2(market)
    "baseAmount": 0.01,           # filled base asset amount (in ZEC for this case)
    "quoteAmount": 1,             # filled quote asset amount (in KRW for this case)
    "fee": 0.0004,                # fee (negtive when reward)
    "feeAssetName": "KRW"         # fee asset name (reward asset when fee is negative)
    "price": 100,                 # price
    "isSelfTrade": false,         # whether both of matching orders are yours
    "occurredAt": 1603932107,     # trade occurrence time
    "tradingPairName": "ZEC-KRW"  # order book
  }
}

 The api only returns the current user's trading history.
Public APIs
Public APIs don't need authentication. There is no need to set Query String.

Subscription to Order Book
import time, base64, hmac, hashlib, json, traceback
from urllib.parse import quote
from websocket import create_connection  # pip install websocket-client

API_KEY = '<Insert Yours>'
SECRET = '<Insert Yours>'

timestamp = str(int(time.time() * 1000))
msg = 't' + timestamp
key = base64.b64decode(SECRET)
signature = base64.b64encode(
  hmac.new(key, str(msg).encode('utf-8'), hashlib.sha512).digest()
).decode()

url = 'wss://wsapi.gopax.co.kr?apiKey={}&timestamp={}&signature={}'
url = url.format(quote(API_KEY), timestamp, quote(signature))
ws_conn = create_connection(url, timeout=10)
ws_conn.settimeout(None)


def receive_response(ws_conn):
  resp_str = ws_conn.recv()
  while '::ping::' in resp_str:
    ws_conn.send(resp_str.replace('::ping::', '::pong::'))
    resp_str = ws_conn.recv()
  return json.loads(resp_str)


class OrderBook:
  def __init__(self):
    self.ask_entries = dict()
    self.bid_entries = dict()

  def update(self, response):
    for side, old_entries in [('ask', self.ask_entries), ('bid', self.bid_entries)]:
      new_entries = response['o'][side]
      for new_entry in new_entries:
        old_entry = old_entries.get(new_entry['price'], None)
        is_truly_newer = not old_entry \
                         or new_entry['updatedAt'] > old_entry['updatedAt'] \
                         or (new_entry['updatedAt'] == old_entry['updatedAt']
                             and new_entry['entryId'] > old_entry['entryId'])
        assert is_truly_newer
        if new_entry['volume'] == 0 and old_entry:
          del old_entries[new_entry['price']]
        else:
          old_entries[new_entry['price']] = new_entry

  def print(self, size=6):
    data_to_print = [
      ('ASK', sorted(list(self.ask_entries.keys()))[:size][::-1], self.ask_entries),
      ('BID', sorted(list(self.bid_entries.keys()))[::-1][:size], self.bid_entries),
    ]
    print('\n\n\n\nUpdated at ' + str(int(time.time() * 1000)))
    for label, prices, entries in data_to_print:
      print('=' * 35)
      for price in prices:
        print(label, '\t', price, '\t', format(entries[price]['volume'], '.8f'))
    print('=' * 35)


ws_conn.send(json.dumps({
  'n': 'SubscribeToOrderBook',
  'o': {'tradingPairName': 'BTC-KRW'},
}))
ob = OrderBook()
while True:
  ob.update(receive_response(ws_conn))
  ob.print()
A single connection can subscribe to order books for up to 50 market pairs.

Request Parameter
Parameter	Mandatory	Remarks
tradingPairName	O	A trading pair's name (e.g. "BCH-KRW")
limit	X	The max size of the returned order book, which should be 20 or more.
If omitted, the whole order book is returned.
 If you use the limit, you may find difficulty in maintaining your local order book.
Request
{
  "n": "SubscribeToOrderBook",
  "o": {
    "tradingPairName": "BCH-KRW"     # order book to be subscribed to
  }
}

Response
The whole order book is returned as a response.

{
  "n": "SubscribeToOrderBook",
  "o": {
    "ask": [                         # ask entry list
      {
        "entryId": 50,               # entry update sequence (+1 incremental)
        "price": 5100000,            # entry price
        "volume": 2.5,               # entry volume
        "updatedAt": 1599089007.614  # entry last update time
      }
    ],
    "bid": [                         # bid entry list
      {
        "entryId": 48,
        "price": 5000000,
        "volume": 5,
        "updatedAt": 1599088982.102
      },
      {
        "entryId": 49,
        "price": 4500000,
        "volume": 3,
        "updatedAt": 1599088992.407
      }
    ],
    "tradingPairName": "BCH-KRW",
    "maxEntryId": 50                 # the max of entry update sequences
  }
}

Delta Push
Once subscribed, every delta (or change) is pushed in real-time.

In case an ASK order is placed with the price of 450,000 KRW and the volume of 6.7 BCH, the following delta will be pushed.

{
  "i": -1,                           # always -1 in case of delta push
  "n": "OrderBookEvent",
  "o": {
    "ask": [],
    "bid": [
      {
        "entryId": 51,
        "price": 5000000,
        "volume": 0,
        "updatedAt": 1599089169.282
      },
      {
        "entryId": 52,
        "price": 4500000,
        "volume": 1.3,
        "updatedAt": 1599089169.282
      }
    ],
    "tradingPairName": "BCH-KRW"
  }
}

 The update order of order book entires can be described as "order by updatedAt, entryId".
 Intermittently, a delta arrives before the response. In that case, establishing a new fresh connection is a quick resolution. Or, you can consider the update order between the delta and response and decide on whether to apply or discard the delta.
Subscription to Trading Pair
All available types of data of a trading pair can be subscribed to, including order book.

Currently, OrderBookEvent and PublicTradeEvent are available.

Request Parameter
Same with Subscription to Order Book,

Request
{
  "n": "SubscribeToTradingPair",
  "o": {
    "tradingPairName": "BCH-KRW"     # order book to be subscribed to
  }
}

Response
Same with Subscription to Order Book,

Delta Push
Once subscribed, every delta (or change) is pushed in real-time.

The format of an OrderBookEvent is the same with Subscription to Order Book.

The format of an PublicTradeEvent is as follows.

{
  "i": -1,                        # always -1 in case of delta push
  "n": "PublicTradeEvent",
  "o": {
    "tradeId": 75021,             # public trade ID
    "baseAmount": 0.01,           # filled base asset amount (in BCH for this case)
    "quoteAmount": 1,             # filled quote asset amount (in KRW for this case)
    "price": 100,                 # price
    "isBuy": true,                # true(buy), false(sell)
    "occurredAt": 1609756772,     # trade occurrence time
    "tradingPairName": "BCH-KRW"  # order book
  }
}

 More available data types can be added without prior notice.
Subscription to Tickers
All Tickers can be subscribed to.

Request
{
  "n": "SubscribeToTickers",
  "o": {}
}

Response
Tickers are returned as a response.

{
 'n': 'SubscribeToTickers',
 'o': {
        'data': [
                  {
                    'baseVolume': 0.02,            # 24h accumulated traded volume (in base asset unit; BTC for this case)
                    'high': 37300000,              # highest trading price in last 24 hours
                    'highestBid': 0,               # max buying price on the order book
                    'last': 37300000,              # current price on the order book
                    'lastTraded': 1665640796413,   # Last trade time(Unix time)
                    'low': 37300000,               # Lowest trading price in the last 24 hours
                    'lowestAsk': 0,                # min selling price's volume on the order book
                    'open': 37300000,              # Opening Price, The price at which the first transaction was made after 00:00(KST)
                    'quoteVolume': 746000,         # 24h accumulated traded volume (in quote asset unit; KRW for this case)
                    'tradingPairName': 'BTC-KRW'   # order book
                  },
                  ...
                  {
                    'baseVolume': 0,
                    'high': 9000000,
                    'highestBid': 9000000,
                    'last': 9000000,
                    'lastTraded': 1629260634639,
                    'low': 9000000,
                    'lowestAsk': 9000000,
                    'open': 9000000,
                    'quoteVolume': 0,
                    'tradingPairName': 'UNC-KRW'
                  }
        ]
    }
}

Delta Push
Once subscribed, updates are pushed in 1 second aggregates.

{
  'i': -1,
  'n': 'TickerEvent',
  'o': {
        'BTC-KRW': {
                      'baseVolume': 0.02,
                      'high': 37300000,
                      'highestBid': 0,
                      'last': 37300000,
                      'lastTraded': 1665640796413,
                      'low': 37300000,
                      'lowestAsk': 0,
                      'open': 37300000,
                      'quoteVolume': 746000,
                      'tradingPairName': 'BTC-KRW'
            }
          ...
      }
}

Changelog
2022-10-25
(New) Public API
(New) Subscription to tickers
(change) move to Public API (Subscription to trading pair, order book)
2022-10-14
(Change) Subscription to orders - Adding fee/reward asset name
(Change) Subscription to trades - Adding fee asset name
2021-01-12
(New) Subscription to trading pair (order book & public trades)
2020-10-29
(New) Subscription to trades
2020-10-06
Ending the beta service and launching officially
(Improvement) Adding the limit parameter on SubscribeToOrderBook
2020-09-23
(New) Authentication and basic subscriptions - order book/outstanding orders/balances




indirizzo
L'indirizzo del server REST API di Gopax è il seguente:

https://api.gopax.co.kr

 È possibile accedere alla REST API di GOPAX tramite CCXT. CCXT è una libreria che consente di accedere a diversi exchange tramite un'unica interfaccia. Per ulteriori informazioni, visitare https://ccxt.trade .
certificazione
import base64, hashlib, hmac, json, requests, time

API_KEY = '<입력하세요>'
SECRET = '<입력하세요>'


def call(need_auth, method, path, body_json=None, recv_window=None):
  method = method.upper()
  if need_auth:
    timestamp = str(int(time.time() * 1000))
    include_querystring = method == 'GET' and path.startswith('/orders?')
    p = path if include_querystring else path.split('?')[0]
    msg = 't' + timestamp + method + p
    msg += (str(recv_window) if recv_window else '') + (json.dumps(body_json) if body_json else '')
    raw_secret = base64.b64decode(SECRET)
    raw_signature = hmac.new(raw_secret, str(msg).encode('utf-8'), hashlib.sha512).digest()
    signature = base64.b64encode(raw_signature)
    headers = {'api-key': API_KEY, 'timestamp': timestamp, 'signature': signature}
    if recv_window:
      headers['receive-window'] = str(recv_window)
  else:
    headers = {}
  req_func = {'GET': requests.get, 'POST': requests.post, 'DELETE': requests.delete}[method]
  resp = req_func(url='https://api.gopax.co.kr' + path, headers=headers, json=body_json)
  return {
    'statusCode': resp.status_code,
    'body': resp.json(),
    'header': dict(resp.headers),
  }


post_orders_req_body = {
  'side': 'buy', 'type': 'limit', 'amount': 1,
  'price': 10000, 'tradingPairName': 'BTC-KRW'
}
print(call(True, 'POST', '/orders', post_orders_req_body, 200))
print(call(True, 'GET', '/orders'))
print(call(True, 'GET', '/orders?includePast=true'))
print(call(True, 'GET', '/trades?limit=1'))
print(call(False, 'GET', '/trading-pairs/BTC-KRW/book?level=1'))
Per utilizzare l'API REST di Gopax, è necessaria la chiave API e il segreto rilasciati tramite il sito web di Gopax.

Ottiene il timestamp corrente in millisecondi senza punti decimali.
Concatena le seguenti stringhe per creare un messaggio:
stringa 't'
marca temporale
Mettere in maiuscolo il metodo di richiesta (ad esempio 'GET')
Percorso di richiesta (ad esempio '/ordini')
Corpo della richiesta (omesso se non c'è corpo)
Decodifica il segreto in base64 per ottenere il segreto grezzo.
Genera una firma raw firmando il messaggio con SHA512 HMAC come segreto raw.
Ottenere la firma codificando la firma grezza in base64.
Aggiungere api-key, timestamp e firma all'intestazione della richiesta.
 Il server può rifiutare una richiesta se il timestamp si discosta di più di un minuto dall'ora standard corrente.
 È possibile utilizzare un nonce anche al posto di un timestamp. Un nonce deve essere un valore univoco e in continuo aumento. Se una richiesta riutilizza un nonce utilizzato in precedenza, il server la rifiuterà. Sebbene ciò impedisca efficacemente richieste duplicate, può risultare scomodo quando si inviano molte richieste in un breve periodo di tempo o in un ambiente multithread. Sebbene l'utilizzo di un nonce sia essenziale per prevenire richieste duplicate, per il trading in cui la tempistica inferiore al secondo è fondamentale, si consiglia di impostare la finestra di ricezione a meno di 5 secondi e di utilizzare un timestamp. Se si desidera utilizzare un nonce al posto di un timestamp, omettere la stringa "t" e impostare la chiave di intestazione su nonce anziché su timestamp.
Finestra di ricezione
Si tratta di un componente aggiuntivo opzionale che fa sì che il server rifiuti gli ordini quando la latenza di rete supera una soglia definita dall'utente. I valori accettabili sono compresi tra 200 e 60.000, espressi in millisecondi. Ciò significa: "Rifiuta l'ordine se non raggiunge il server entro x millisecondi". Ecco come utilizzarlo:

Durante il processo di generazione della firma, inserire una finestra di ricezione subito dopo la voce "API Path" nel messaggio.
Aggiungi receive-window all'intestazione della tua richiesta HTTP.
Se l'orario in cui l'ordine raggiunge il server è successivo al timestamp dell'utente più la finestra di ricezione, l'ordine viene rifiutato dal server.

 Quando si utilizza una finestra di ricezione, se il timestamp specificato dall'utente è più di un secondo avanti rispetto all'ora standard, il server potrebbe rifiutare la richiesta come se l'utente avesse immesso un valore timestamp non valido.
API personale
Un'API personale è un'API che richiede un processo di autenticazione.

Richiesta di saldo
GET /balances

Esempio di chiamata
canale
GET /balances

richiesta
없음

risposta
[
  {
    "asset": "KRW",                   # 자산 이름
    "avail": 1759466.76,              # 주문 가능 보유 수량
    "hold": 16500,                    # 오더북에 올라가 있는 미체결 수량
    "pendingWithdrawal": 0,           # 출금 처리 중인 수량
    "lastUpdatedAt": "1600684352032"  # 해당 잔고 최근 갱신 시간
  },
  {
    "asset": "ETH",
    "avail": 100979.57523727,
    "hold": 50.02,
    "pendingWithdrawal": 0,
    "lastUpdatedAt": "1600686162591"
  },
  ...
]

Controllare il saldo specifico delle attività
GET /balances/<AssetName>

Esempio di chiamata
canale
GET /balances/ETH

richiesta
없음

risposta
{
  "asset": "ETH",                   # 자산 이름
  "avail": 100979.57523727,         # 주문 가능 보유 수량
  "hold": 50.02,                    # 오더북에 올라가 있는 미체결 수량
  "pendingWithdrawal": 0,           # 출금 처리 중인 수량
  "lastUpdatedAt": "1600686162591"  # 해당 잔고 최근 갱신 시간
}

Richiesta d'ordine
È possibile controllare gli ordini parzialmente evasi o non evasi.

GET /orders

stringa di query	Obbligatorio	Predefinito	spiegazione
includePast	selezionare	falso	Se è vero, nei risultati della ricerca vengono inclusi anche gli ordini completamente eseguiti o annullati
(la ricerca è disponibile solo per 10 minuti a partire dal momento dell'esecuzione completa o dell'annullamento).
impaginazione	selezionare	falso	Se il numero di ordini restituiti supera 3.000,
impostarlo su true per accedervi 1.000 per pagina.
tradingPairName	selezionare	-	Controlla gli ordini per la coppia di trading corrispondente (BTC-KRW, ETH-KRW, ecc.)
stato	selezionare	-	Ricerca per stato dell'ordine
(effettuato, annullato, completato, aggiornato, prenotato)
Da	selezionare	-	Timestamp dell'ora di inizio (in millisecondi)
filtroAggiornatoA	selezionare	falso	Utilizzare con since
true: il punto di partenza è basato su updatedAt
false: il punto di partenza è basato su createdAt
limite	selezionare	-	Numero massimo di ordini
coda	selezionare	falso	Utilizzare con limite
true: recupera i dati fino al limite dall'ordine più recente
false: recupera i dati fino al limite dall'ordine più vecchio
 Solo per GET /orders, la stringa di query deve essere inclusa nel processo di generazione della firma. Vedere il codice di esempio all'inizio del documento.
Esempio di chiamata
canale
GET /orders

richiesta
없음

risposta
[
  {
    "id": "453324",                           # 주문 ID
    "clientOrderId": "zeckrw23456",           # 클라이언트 오더 ID (존재할 경우에 한하여 표시됨)
    "status": "updated",                      # placed(미체결), cancelled(취소됨), completed(전체 체결됨), updated(일부 체결됨), reserved(예약됨)
    "forcedCompletionReason": undefined,      # 주문 중도 취소된 경우에 한하여 그 사유로 protection/timeInForce 중 하나
    "tradingPairName": "ZEC-KRW",             # 오더북
    "side": "buy",                            # buy(구매), sell(판매)
    "type": "limit",                          # limit(지정가), market(시장가)
    "price": 1000000,                         # 주문 가격
    "stopPrice": undefined,                   # 감시 가격 (예약가 주문에 한하여 표시됨)
    "amount": 4,                              # 최초 주문 수량
    "remaining": 1,                           # 오더북에 남아 있는 미체결 주문 수량
    "protection": "yes",                      # 최초 체결가 기준 ±10% 초과되는 주문 취소 여부로 yes/no 중 하나
    "timeInForce": "gtc",                     # 지정가 주문 유형으로 gtc/po/ioc/fok 중 하나
    "createdAt": "2020-09-25T04:06:20.000Z",  # 주문 넣은 시간
    "updatedAt": "2020-09-25T04:06:29.000Z",  # 주문 업데이트 시간
    "balanceChange": {
      "baseGross": 3,                         # base 자산 잔고 gross 변화 (이 경우 ZEC)
      "baseFee": {
        "taking": 0,                          # taker 포지션으로 발생한 base 자산 수수료
        "making": -0.0012                     # maker 포지션으로 발생한 base 자산 수수료
      },
      "baseNet": 2.9988,                      # base 자산 잔고 net 변화 (이 경우 ZEC)
      "quoteGross": -3000000,                 # quote 자산 잔고 gross 변화 (이 경우 KRW)
      "quoteFee": {
        "taking": 0,                          # taker 포지션으로 발생한 quote 자산 수수료
        "making": 0                           # maker 포지션으로 발생한 quote 자산 수수료
      },
      "quoteNet": -3000000                    # quote 자산 잔고 net 변화 (이 경우 KRW)
    }
  },
  ...
]

Cerca un ordine specifico
GET /orders/<OrderId>OGET /orders/clientOrderId/<ClientOrderID>

Esempio di chiamata
canale
GET /orders/453324

richiesta
없음

risposta
{
  "id": "453324",                           # 주문 ID
  "clientOrderId": "zeckrw23456",           # 클라이언트 오더 ID (존재할 경우에 한하여 표시됨)
  "status": "updated",                      # placed(미체결), cancelled(취소됨), completed(전체 체결됨), updated(일부 체결됨), reserved(예약됨)
  "forcedCompletionReason": undefined,      # 주문 중도 취소된 경우에 한하여 그 사유로 protection/timeInForce 중 하나
  "tradingPairName": "ZEC-KRW",             # 오더북
  "side": "buy",                            # buy(구매), sell(판매)
  "type": "limit",                          # limit(지정가), market(시장가)
  "price": 1000000,                         # 주문 가격
  "stopPrice": undefined,                   # 감시 가격 (예약가 주문에 한하여 표시됨)
  "amount": 4,                              # 최초 주문 수량
  "remaining": 1,                           # 오더북에 남아 있는 미체결 주문 수량
  "protection": "yes",                      # 최초 체결가 기준 ±10% 초과되는 주문 취소 여부로 yes/no 중 하나
  "timeInForce": "gtc",                     # 지정가 주문 유형으로 gtc/po/ioc/fok 중 하나
  "createdAt": "2020-09-25T04:06:20.000Z",  # 주문 넣은 시간
  "updatedAt": "2020-09-25T04:06:29.000Z",  # 주문 업데이트 시간
  "balanceChange": {
    "baseGross": 3,                         # base 자산 잔고 gross 변화 (이 경우 ZEC)
    "baseFee": {
      "taking": 0,                          # taker 포지션으로 발생한 base 자산 수수료
      "making": -0.0012                     # maker 포지션으로 발생한 base 자산 수수료
    },
    "baseNet": 2.9988,                      # base 자산 잔고 net 변화 (이 경우 ZEC)
    "quoteGross": -3000000,                 # quote 자산 잔고 gross 변화 (이 경우 KRW)
    "quoteFee": {
      "taking": 0,                          # taker 포지션으로 발생한 quote 자산 수수료
      "making": 0                           # maker 포지션으로 발생한 quote 자산 수수료
    },
    "quoteNet": -3000000                    # quote 자산 잔고 net 변화 (이 경우 KRW)
  }
}

 Gli ordini completamente eseguiti o annullati possono essere visualizzati solo per 10 minuti dal momento della completa esecuzione o dell'annullamento.
Registrazione dell'ordine
POST /orders

Esempio di chiamata
canale
POST /orders

richiesta
{
  "clientOrderId": "test4321",   # 선택 | 클라이언트 오더 ID로 최대 20자이고 [a-zA-Z0-9_-] 문자 사용 가능
  "tradingPairName": "BCH-KRW",  # 필수 | 오더북
  "side": "sell",                # 필수 | buy(구매), sell(판매)
  "type": "limit",               # 필수 | limit(지정가), market(시장가)
  "price": 11000000,             # 필수 (지정가에 한함) | 주문 가격
  "stopPrice": 12000000,         # 선택 (값이 있으면 예약가 주문으로 처리됨) | 감시 가격
  "amount": 0.5,                 # 필수 | 주문 수량
  "protection": "no",            # 선택 (디폴트 no) | 최초 체결가 기준 ±10% 초과되는 주문 취소 여부로 yes/no 중 택일
  "timeInForce": "gtc"           # 선택 (지정가에 한하며 디폴트는 gtc) | 지정가 주문 유형으로 gtc/po/ioc/fok 중 택일
}

risposta
{
  "id": "453327",                           # 주문 ID
  "clientOrderId": "test4321",              # 클라이언트 오더 ID (존재할 경우에 한하여 표시됨)
  "status": "reserved",                     # placed(미체결), cancelled(취소됨), completed(전체 체결됨), updated(일부 체결됨), reserved(예약됨)
  "forcedCompletionReason": undefined,      # 주문 중도 취소된 경우에 한하여 그 사유로 protection/timeInForce 중 하나
  "tradingPairName": "BCH-KRW",             # 오더북
  "side": "sell",                           # buy(구매), sell(판매)
  "type": "limit",                          # limit(지정가), market(시장가)
  "price": 11000000,                        # 주문 가격
  "stopPrice": 12000000,                    # 감시 가격 (예약가 주문에 한하여 표시됨)
  "amount": 0.5,                            # 최초 주문 수량
  "remaining": 0.5,                         # 오더북에 남아 있는 미체결 주문 수량
  "protection": "no",                       # 최초 체결가 기준 ±10% 초과되는 주문 취소 여부로 yes/no 중 하나
  "timeInForce": "gtc",                     # 지정가 주문 유형으로 gtc/po/ioc/fok 중 하나
  "createdAt": "2020-09-25T04:51:31.000Z",  # 주문 넣은 시간
  "balanceChange": {
    "baseGross": 0,                         # base 자산 잔고 gross 변화 (이 경우 BCH)
    "baseFee": {
      "taking": 0,                          # taker 포지션으로 발생한 base 자산 수수료
      "making": 0                           # maker 포지션으로 발생한 base 자산 수수료
    },
    "baseNet": 0,                           # base 자산 잔고 net 변화 (이 경우 BCH)
    "quoteGross": 0,                        # quote 자산 잔고 gross 변화 (이 경우 KRW)
    "quoteFee": {
      "taking": 0,                          # taker 포지션으로 발생한 quote 자산 수수료
      "making": 0                           # maker 포지션으로 발생한 quote 자산 수수료
    },
    "quoteNet": 0                           # quote 자산 잔고 net 변화 (이 경우 KRW)
  }
}

 Per gli ordini limite, l'importo è sempre espresso in unità dell'asset base. Per gli ordini a mercato, l'importo è espresso in unità dell'asset base per le vendite e in unità dell'asset quotato per gli acquisti. Ad esempio, nel book degli ordini ETH-KRW, l'ordine limite è espresso in unità di ETH indipendentemente dal fatto che si acquisti o si venda, mentre l'unità per gli ordini a mercato è ETH per le vendite e KRW per gli ordini a mercato.
 Tutte le commissioni di transazione vengono pagate sull'asset quotato della coppia di trading. (Applicato dopo la manutenzione ordinaria del 1° novembre 2022.)

Per gli ordini di vendita, la commissione viene applicata all'asset quotato ottenuto dopo il completamento della vendita. Ad esempio, un utente che ha ricevuto 10.000 won in una transazione di vendita riceverà 9.980 won dopo aver pagato una commissione di transazione di 20 won (ipotizzando una commissione dello 0,2%).

Per gli ordini di acquisto, l'acquirente deve disporre di un saldo sufficiente per pagare la commissione in aggiunta all'importo quotato. (saldo quotato > importo quotato ordine + commissione (importo * commissione)) Ad esempio, un utente che effettua un ordine di acquisto di 10.000 won richiede un minimo di 10.020 won (ipotizzando una commissione dello 0,2%).
 L'importo minimo dell'ordine tramite REST API è di 1.000 KRW se l'asset quotato è KRW e di 1 USDC se l'asset quotato è USDC.
 L'ID ordine cliente è un ID personalizzato che gli utenti possono assegnare agli ordini. È possibile utilizzare l'ID ordine cliente per registrare, visualizzare o annullare gli ordini.
 Un ordine in sospeso, noto anche come ordine stop, consente di prenotare un ordine specificando un prezzo di riferimento e di registrarlo quando il prezzo corrente raggiunge tale prezzo. Si prega di notare che sono supportati solo ordini limite; gli ordini di mercato non sono consentiti per garantire la stabilità del mercato.
 La protezione è una funzione di protezione degli ordini che impedisce l'esecuzione di ordini di acquisto/vendita a prezzi superiori al 10% del prezzo iniziale dell'ordine. Se il prezzo supera il 10%, l'ordine verrà annullato e il saldo rimanente verrà restituito al cliente. Questo vale sia per gli ordini limite che per quelli a mercato.
 Nel tipo di ordine limite, po (post only) significa annullare l'ordine se è presente un contrordine che può essere eseguito immediatamente, altrimenti registrare l'intero ordine (posizionando l'intero ordine sul book degli ordini o annullandolo).

ioc (immediate-or-cancel) significa evadere immediatamente la maggior quantità possibile e annullare l'importo rimanente senza inserirlo nel book degli ordini (esecuzione immediata e successiva cancellazione dell'importo rimanente).

fok (fill-or-kill) significa immettere l'ordine solo se l'intera quantità può essere eseguita immediatamente, altrimenti annullare l'intero ordine (esecuzione immediata o annullamento dell'intero ordine).

Si noti che il tipo di ordine limite viene ignorato per gli ordini di mercato e ioc e fok non possono essere utilizzati se la protezione è impostata su sì.
ritirare l'ordine
DELETE /orders/<OrderId>ODELETE /orders/clientOrderId/<ClientOrderID>

Esempio di chiamata
canale
DELETE /orders/453327

richiesta
없음

risposta
{}

 Se l'ordine corrispondente non esiste, viene restituito un errore 404.
Controllare i registri dei contratti
GET /trades

stringa di query	Obbligatorio	Predefinito	spiegazione
limite	selezionare	-	Numero di articoli restituiti (massimo 100)
pastmax	selezionare	-	Recupera i dati più vecchi di questo ID
latestmin	selezionare	-	Recupera i dati più recenti più recenti di questo ID
Dopo	selezionare	-	Recupera i dati da questo timestamp (in secondi)
Prima	selezionare	-	Recupera i dati prima di questo timestamp (in secondi)
Ricerca profonda	selezionare	falso	Se è vero, cercherà tutti i dati più vecchi di un mese
(ha priorità più alta rispetto ad altri parametri)
tradingPairName	selezionare	-	Visualizza i dati per la coppia di trading corrispondente (BTC-KRW, ETH-KRW, ecc.)
Esempio di chiamata
canale
GET /trades

richiesta
없음

risposta
[
  {
    "id": 73953,                              # 체결 이벤트 ID
    "orderId": 453324,                        # 주문 ID
    "baseAmount": 3,                          # 체결된 base 자산 수량
    "quoteAmount": 3000000,                   # 체결된 quote 자산 수량
    "fee": 0.0012,                            # 수수료
    "price": 1000000,                         # 체결 가격
    "timestamp": "2020-09-25T04:06:30.000Z",  # 체결 시간
    "side": "buy",                            # buy(구매), sell(판매)
    "feeAsset": "KRW",                        # 수수료 자산
    "tradingPairName": "ZEC-KRW",             # 오더북
    "position": "maker"                       # maker(메이커), taker(테이커)
  },
  ...
]

 Questa API personale mostra solo la cronologia delle transazioni relative ai tuoi ordini. Per visualizzare tutti i record delle transazioni, indipendentemente dal tipo di ordine, utilizza la funzione di query della cronologia delle transazioni nell'API pubblica.
Controllare i registri di deposito/prelievo
GET /deposit-withdrawal-status

stringa di query	Obbligatorio	Predefinito	spiegazione
limite	selezionare	-	Numero di articoli restituiti (massimo 20)
latestmin	selezionare	-	Recupera i dati più vecchi di questo ID
Dopo	selezionare	-	Recupera i dati dopo questo timestamp (in ms)
Prima	selezionare	-	Recupera i dati prima di questo timestamp (in ms)
completatoSolo	selezionare	falso	Visualizza solo la cronologia dei depositi/prelievi completati (seleziona vero/falso)
risorsa	selezionare	-	Controlla la cronologia dei depositi/prelievi dell'asset (BTC, ETH, ecc.)
Esempio di chiamata
canale
GET /deposit-withdrawal-status

richiesta
없음

risposta
[
  {
    "id": 640,                      # 입출금 이벤트 ID
    "asset": "BTC",                 # 자산 이름
    "type": "crypto_withdrawal",    # fiat_withdrawal(원화출금), fiat_deposit(원화입금), crypto_withdrawal(크립토출금), crypto_deposit(크립토입금)
    "netAmount": 0.0001,            # 입출금 자산의 수량
    "feeAmount": 0.0005,            # 수수료 (없을 경우 null)
    "status": "completed",          # reviewing(심사중), rejected(심사거절), processing(처리중), failed(처리실패), completed(처리완료)
    "reviewStartedAt": 1595556218,  # 입출금 요청 시간
    "completedAt": 1595556902,      # 입출금 처리 완료 시간 (처리완료 상태가 아닐 경우 null)
    "txId": "eaca5ad3...",          # 트랜잭션 ID
    "sourceAddress": null,          # 보낸 사람 주소 (크립토입금일 경우 값 존재)
    "destinationAddress: "3H8...",  # 받을 사람 주소 (크립토출금일 경우 값 존재)
    "destinationMemoId": null       # 받을 사람 주소의 메모 ID
  },
  ...
]

Controllare l'indirizzo di deposito delle risorse virtuali
GET /crypto-deposit-addresses

Esempio di chiamata
canale
GET /crypto-deposit-addresses

richiesta
없음

risposta
[
  {
    "asset": "BTC",                                   # 자산 이름
    "address": "1CwC2cMFu1jRQUBtw925cENbT1kctJBMdm",  # 입금 주소
    "memoId": null,                                   # 메모 ID (메모 ID를 통한 입금인 경우만 존재)
    "createdAt": 1594802312                           # 입금 주소 생성 시간
  },
  ...
]

Controlla l'indirizzo di prelievo delle risorse virtuali
GET /crypto-withdrawal-addresses

Esempio di chiamata
canale
GET /crypto-withdrawal-addresses

richiesta
없음

risposta
[
  {
    "asset": "BTC",                                   # 자산 이름
    "address": "3QEdPvg2XuK8Q1tGU1RpyzxkkEsiLkvQF3",  # 출금 주소
    "memoId": null,                                   # 메모 ID (메모 ID를 통한 출금인 경우만 존재)
    "nickname": "My External BTC Address",            # 출금 주소 별칭
    "createdAt": 1588417815                           # 출금 주소 등록 시간
  }
  ...
]

Prelievo di asset virtuali
POST /withdrawals

Esempio di chiamata
canale
POST /withdrawals

richiesta
{
  "asset": "BCH",                         # 필수 | 자산 이름
  "nickname": "WithdrawalAddress",        # 필수 | 출금 주소 별칭
  "amount": "10000000000",                # 필수 | 출금 수량
}

risposta
없음

 I prelievi sono possibili solo dagli IP preregistrati.
API pubblica
Le API pubbliche sono accessibili senza autenticazione. Ciò significa che possono essere richiamate senza includere requisiti di autenticazione nell'intestazione della richiesta.

Visualizza l'elenco delle risorse
GET /assets

Esempio di chiamata
canale
GET /assets

richiesta
없음

risposta
[
  ...,
  {
    "id": "ETH",                  # 자산 이름
    "name": "이더리움",             # 자산 이름 (국문)
    "englishName": "Ethereum",    # 자산 이름 (영문)
    "scale": 8,                   # 자산 최대 소수점 자리수
    "withdrawalFee": 0.03,        # 출금 수수료
    "withdrawalAmountMin": 0.015  # 출금 최소 금액
  },
  ...
]

Visualizza l'elenco delle coppie di trading
GET /trading-pairs

Esempio di chiamata
canale
GET /trading-pairs

richiesta
없음

risposta
[
  {
    "id": 1,                    # 거래쌍 ID
    "name": "ETH-KRW",          # 거래쌍 이름
    "baseAsset": "ETH",         # base 자산
    "quoteAsset": "KRW",        # quote 자산
    "baseAssetScale": 8,        # base 자산 최대 소수점 자리수
    "quoteAssetScale": 0,       # quote 자산 최대 소수점 자리수
    "priceMin": 1,              # 최소 주문 가격
    "restApiOrderAmountMin": {  # REST API 통해 주문 시 최소 주문 수량
      "limitAsk": {
        "amount": 1000,
        "unit": "KRW"
      },
      "limitBid": {
        "amount": 1000,
        "unit": "KRW"
      },
      "marketAsk": {
        "amount": 0.001,
        "unit": "ETH"
      },
      "marketBid": {
        "amount": 1000,
        "unit": "KRW"
      }
    },
    "makerFeePercent": 0.2,     # 메이커 거래 수수료 퍼센트
    "takerFeePercent": 0.2      # 테이커 거래 수수료 퍼센트
  },
  ...
]

Controlla la dimensione del tick del prezzo
GET /trading-pairs/<TradingPair>/price-tick-size

Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/price-tick-size

richiesta
없음

risposta
[
  { startPrice: 1, tickSize: 1 },
  { startPrice: 5000, tickSize: 5 },
  { startPrice: 10000, tickSize: 10 },
  { startPrice: 50000, tickSize: 50 },
  { startPrice: 100000, tickSize: 100 },
  { startPrice: 500000, tickSize: 500 },
  { startPrice: 2000000, tickSize: 1000 }
]

Richiesta di ticker
GET /trading-pairs/<TradingPair>/ticker

Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/ticker

richiesta
없음

risposta
{
  "price": 15393000,                   # 오더북 상의 현재 가격
  "ask": 15397000,                     # 오더북 상의 현재 가장 낮은 매도 가격
  "askVolume": 0.56,                   # 오더북 상의 현재 가장 낮은 매도 가격의 수량
  "bid": 15393000,                     # 오더북 상의 현재 가장 높은 매수 가격
  "bidVolume": 1.9513,                 # 오더북 상의 현재 가장 높은 매수 가격의 수량
  "volume": 487.43035427,              # 최근 24시간 누적 거래량 (base 자산 단위로 이 예시에서는 BTC)
  "quoteVolume": 7319576689.34135,     # 최근 24시간 누적 거래량 (quote 자산 단위로 이 예시에서는 KRW)
  "time": "2020-10-28T02:05:55.958Z"   # 티커 최근 갱신 시간
}

Richiesta di informazioni sul libro degli ordini
GET /trading-pairs/<TradingPair>/book

stringa di query	Obbligatorio	Predefinito	spiegazione
livello	selezionare	3	1 = 1 ciascuno per acquisto e vendita
2 = 50 ciascuno per acquisto e vendita
3 = Tutti
Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/book

richiesta
없음

risposta
{
  "sequence": 110815766,
  "ask": [              # 오더북 판매 엔트리 목록
    [
      "110815528",      # 오더북 엔트리 고유번호 (변화 발생 시마다 +1)
      12371000,         # 오더북 엔트리 가격
      0.808,            # 오더북 엔트리 물량
      "1601030126425"   # 오더북 엔트리 업데이트 시간
    ],
    ...
  ],
  "bid": [              # 오더북 구매 엔트리 목록
    ...,
    [
      "108223577",
      11870000,
      0.72446908,
      "1600956121521"
    ]
  ]
}

Controllare i registri dei contratti
GET /trading-pairs/<TradingPair>/trades

stringa di query	Obbligatorio	Predefinito	spiegazione
limite	selezionare	-	Numero di articoli restituiti (massimo 100)
pastmax	selezionare	-	Recupera i dati più vecchi di questo ID
latestmin	selezionare	-	Recupera i dati più recenti più recenti di questo ID
Dopo	selezionare	-	Recupera i dati da questo timestamp (in secondi)
Prima	selezionare	-	Recupera i dati prima di questo timestamp (in secondi)
Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/trades

richiesta
없음

risposta
[
  {
    "time": "2020-09-25T11:10:29.000Z",  # 체결 시간
    "date": 1601032229,                  # 체결 시간 초 단위 타임스탬프
    "id": 21876490,                      # 체결 이벤트 ID
    "price": 12353000,                   # 체결 가격
    "amount": 0.2951,                    # 체결 수량 (base 자산 단위로 이 예시에서는 BTC)
    "side": "sell"                       # buy(구매), sell(판매)
  },
  ...
]

Visualizza le statistiche delle ultime 24 ore
GET /trading-pairs/<TradingPair>/stats

Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/stats

richiesta
없음

risposta
{
  "open": 12132000,                   # 24시간 전 가격
  "high": 12543000,                   # 최근 24시간 동안 최고가
  "low": 12059000,                    # 최근 24시간 동안 최저가
  "close": 12349000,                  # 현재 가격 (1분마다 갱신됨)
  "volume": 332.12915604,             # 최근 24시간 누적 거래량 (base 자산 단위로 이 예시에서는 BTC)
  "time": "2020-09-25T11:13:47.371Z"  # 최근 통계 업데이트 시간
}

Visualizza le statistiche delle ultime 24 ore (tutte le coppie di trading)
GET /trading-pairs/stats

Esempio di chiamata
canale
GET /trading-pairs/stats

richiesta
없음

risposta
[
  {
    "name": "ETH-KRW",                  # 거래쌍
    "open": 394200,                     # 24시간 전 가격
    "high": 409900,                     # 최근 24시간 동안 최고가
    "low": 388700,                      # 최근 24시간 동안 최저가
    "close": 397200,                    # 현재 가격 (1분마다 갱신됨)
    "volume": 4017.90526766,            # 최근 24시간 누적 거래량 (base 자산 단위로 이 예시에서는 BTC)
    "time": "2020-09-25T11:14:14.866Z"  # 최근 통계 업데이트 시간
  },
  ...
]

Query sui dati del grafico
GET /trading-pairs/<TradingPair>/candles

stringa di query	Obbligatorio	Predefinito	spiegazione
inizio	essenziale	-	Timestamp dell'ora di inizio (in millisecondi)
FINE	essenziale	-	Timestamp del punto finale (in millisecondi)
intervallo	essenziale	-	Durata di ogni segmento (in minuti, scegli tra 1/5/30/1440)
limite	selezionare	1024	Numero di articoli restituiti (massimo 1024)
Esempio di chiamata
canale
GET /trading-pairs/BTC-KRW/candles?start=1601032379683&end=1601033046191&interval=1

richiesta
없음

risposta
[
  ...,
  [
    1601032200000,  # 구간 시작 시간
    12353000,       # 구간 최저가
    12361000,       # 구간 최고가
    12361000,       # 구간 시가
    12353000,       # 구간 종가
    0.5902          # 구간 누적 거래량 (base 자산 단위로 이 예시에서는 BTC)
  ],
  ...
]

 Un intervallo corrisponde a una barra del grafico.
Visualizza le informazioni di cautela sugli investimenti
GET /trading-pairs/cautions

stringa di query	Obbligatorio	Predefinito	spiegazione
mostraAttivo	selezionare	falso	true: vengono visualizzati solo gli elementi con rischi, false: vengono visualizzati tutti gli elementi
Esempio di chiamata
canale
GET /trading-pairs/cautions?showActive=true

richiesta
없음

risposta
[
  {
    "id": 1,                           # 거래쌍 ID
    "name": "ETH-KRW",                 # 거래쌍 이름
    "alertLevel": 0,                   # Alert Level - 정상(0), 주의(1), 경고(2)
    "isPriceChange": false,            # 가격 급등 또는 급락 여부
    "isMonopolyBuy": false,            # (deprecated)
    "isLowLiquidity": false,           # (deprecated)
    "isSoarTradingVolume": false,      # 거래량 급등 또는 급락 여부
    "isSoarDepositAmount": false,      # 입금량 급등 또는 급락 여부
    "isGlobalPriceDifference": false,  # 가격 차이 발생 여부
    "isMonopolyTrading": false,        # 소수 계정 거래 집중
  },
  ...
]

 Potrebbero verificarsi casi in cui tutti gli elementi sono falsi, ma il livello di allerta non è normale (0). Si tratta di un fenomeno naturale dovuto alla regola secondo cui, una volta emesso un avviso o una cautela, la situazione tornerà alla normalità solo se la situazione è sicura per 24 ore.
Visualizza tutti i ticker
GET /tickers

Visualizza l'elenco completo dei ticker.

Esempio di chiamata
canale
GET /tickers

richiesta
없음

risposta
[
  {
    'baseVolume': 0.02,            # 최근 24시간 누적 거래량 (base 자산 단위로 이 예시에서는 BTC)
    'high': 37300000,              # 최근 24시간 최고 거래 가격
    'highestBid': 0,               # 오더북 상의 현재 가장 높은 매수 가격
    'last': 37300000,              # 오더북 상의 현재 가격
    'lastTraded': 1665640796413,   # 최근 거래 시각(Unix time)
    'low': 37300000,               # 최근 24시간 최저 거래 가격
    'lowestAsk': 0,                # 오더북 상의 현재 가장 낮은 매도 가격
    'open': 37300000,              # 거래시작가, 한국시간(KST) 기준 00시 이후 첫 거래가 체결된 가격
    'quoteVolume': 746000,         # 최근 24시간 누적 거래량 (quote 자산 단위로 이 예시에서는 KRW)
    'tradingPairName': 'BTC-KRW'   # 오더북
  },
  ...
  {
    'baseVolume': 0,
    'high': 9000000,
    'highestBid': 9000000,
    'last': 9000000,
    'lastTraded': 1629260634639,
    'low': 9000000,
    'lowestAsk': 9000000,
    'open': 9000000,
    'quoteVolume': 0,
    'tradingPairName': 'UNC-KRW'
  }
]

Controlla l'ora del server
GET /time

Esempio di chiamata
canale
GET /time

richiesta
없음

risposta
{
  "serverTime": 1601033421109  # 밀리세컨드 단위 타임스탬프
}

Visualizza gli avvisi
GET /notices

stringa di query	Obbligatorio	Predefinito	spiegazione
limite	selezionare	20	Numero di elementi per pagina (massimo 20)
pagina	selezionare	0	Numero di pagina (a partire da 0)
tipo	selezionare	0	Tipo (0 = nessuna distinzione, 1 = avviso generale, 2 = inserzione, 3 = evento)
formato	selezionare	0	Modulo (0 = HTML, 1 = testo normale)
Esempio di chiamata
canale
GET /notices?format=1

richiesta
없음

risposta
[
  {
    "id": 531,                               # 공지사항 ID
    "type": 1,                               # 공지사항 타입
    "title": "정기점검",                       # 공지사항 제목
    "content": "곧 정기점검이 있을 예정입니다",    # 공지사항 내용
    "createdAt": "2020-12-29T01:24:13.000Z"  # 공지사항 생성 시간
    "updatedAt": "2020-12-29T01:24:13.000Z"  # 공지사항 갱신 시간
  },
  ...
]

Limite di velocità delle chiamate
Le API private sono limitate dalla chiave API, mentre le API pubbliche sono limitate dall'IP.
Per impostazione predefinita, è possibile effettuare un massimo di 20 chiamate nell'ultimo secondo. Le eccezioni includono:
Per gli ordini di tipo FOK o GET /trades?deepSearch=false, sono consentite al massimo 2 chiamate nell'ultimo secondo.
GET /trading-pairs/<TradingPair>/book o GET /trades?deepSearch=true possono essere chiamati al massimo una volta al secondo.
L'intestazione di risposta inviata dal server specifica il numero di chiamate utilizzate nell'ultimo secondo e la quantità rimanente.
x-gopax-ip-addr-used-weight: Numero di chiamate basate su IP utilizzate nell'ultimo secondo
x-gopax-ip-addr-left-weight : Peso rimanente del conteggio delle chiamate basate su IP
x-gopax-api-key-used-weight: numero di chiamate basate su API Key utilizzate nell'ultimo secondo
x-gopax-api-key-left-weight: peso rimanente del conteggio delle chiamate basate sulla chiave API
Se viene superato il limite del numero di chiamate, viene restituito il codice di stato 429 (Limite di richiesta superato).
Politica di scadenza della chiave API
La chiave API ha una data di scadenza di un anno dalla data di emissione.
La presente policy è in vigore dal 19/11/2024 e la data di scadenza delle chiavi API registrate in precedenza viene calcolata a partire dalla data di applicazione della policy.
Non è possibile rinnovare la data di scadenza e occorre emetterne una nuova.
Quando si rilascia una chiave API, l'indirizzo IP registrato in anticipo è limitato solo ai prelievi di asset virtuali.
errore
Codici di stato di errore HTTP

Codice di stato	Descrizione
400	Richiesta non valida - Formato di richiesta non valido
401	Non autorizzato - Chiave API non valida
403	Vietato - Non è consentito l'accesso alla risorsa richiesta
404	Non trovato
429	Troppe richieste - Limite di velocità API superato
500	Errore interno del server - Problema temporaneo con il servizio

errore

{
  "100": "Invalid Asset",
  "101": "Invalid Trading Pair",
  "102": "Invalid User",
  "104": "Not Enabled Trading Pair",
  "105": "Not Activated Trading Pair",
  "106": "Not Enabled Asset",
  "107": "Invalid Amount",
  "108": "Invalid Price",
  "201": "Insufficient Balance",
  "202": "Invalid Id",
  "203": "Invalid Numbers Overflow",
  "204": "Not Allowed Bid Order",
  "206": "Invalid Option Combination",
  "10004": "Not Authorized",  # check again your signing logic
  "10006": "User Not Found",
  "10033": "Asset Not Allowed",
  "10041": "Invalid Exchange",
  "10044": "Invalid Asset Id",
  "10052": "Order Server Not Available",  # stop trading for a while if it happens
  "10056": "No Registered Asset",
  "10057": "No Registered Trading Pair",
  "10058": "No Such Asset Code",
  "10059": "No Such Trading Pair",
  "10061": "Invalid Trading Pair Id",
  "10062": "Invalid Chart Interval",
  "10064": "User Locked",
  "10069": "No Such Order Id",
  "10074": "Send To Order Server Failed",  # stop trading for a while if it happens
  "10105": "Rate Limit Exceeded",  # you are causing too much traffic
  "10108": "Nonce Too Low",
  "10155": "Invalid Api Key",
  "10157": "Invalid Price",
  "10166": "Invalid Chart Range",
  "10195": "Invalid Internal Data",
  "10204": "Not Hedge Token User",  # visit the website and agree on using Pro market
  "10212": "Too Small Quote Amount",
  "10221": "No Such Client Order Id",
  "10222": "Client Order Id Being Used",
  "10223": "Soon Expired Client Order Id",
  "10227": "Invalid Client Order Id Format",
  "10229": "Invalid Signature",
  "10230": "No Api Key",
  "10231": "No Nonce And Timestamp",
  "10232": "Nonce Too High",
  "10233": "Unusable Api Key",
  "10234": "Cannot Check Rate Limit",
  "10255": "Too Long Request Body",
  "10256": "Unparsable Request Body",
  "10263": "Timestamp Too Low",
  "10264": "Timestamp Too High",
  "10265": "Choose Either Nonce Or Timestamp",
  "10296": "Invalid Receive Window",
  "10297": "Invalid Timestamp To Check Receive Window",
  "10298": "Fail To Meet Server Arrival Deadline",
  "10319": "Pagination Required",
  "10358": "Invalid Order Type",
  "10359": "Invalid Order Side",
  "10360": "Invalid Order Status",
  "10361": "Invalid Time In Force",
  "10362": "Invalid Protection",
  "10364": "Ip Address Banned Temporarily",  # you are causing too much traffic
  "10367": "Mandatory Query String Missing"
}

Cronologia delle modifiche
19-11-2024
Aggiungi funzionalità

POST /withdrawalsFunzionalità aggiunta per il prelievo di asset virtuali
Cambiamento di politica

Applica la politica sulla data di scadenza della chiave API
La validità è limitata a un anno dal momento dell'emissione e le chiavi API emesse in precedenza sono valide dal momento dell'applicazione della policy.
2024-10-07
Cambiamento di politica

Modificato l'importo minimo dell'ordine in won coreani (KRW 10.000 -> KRW 1.000)
25 luglio 2023
Aggiungi dati di risposta

GET /trading-pairs/cautionsAggiungere elementi di avviso isSoarTradingVolume, isSoarDepositAmount, isGlobalPriceDifference, ai dati di rispostaisMonopolyTrading
GET /trading-pairs/cautionsElementi di avviso nei dati di risposta isMonopolyBuy, isLowLiquiditydeprecati
7 febbraio 2022
Cambiamento di funzione

GET /assetsAggiungi la proprietà del nome della risorsa in inglese (englishName)
25 ottobre 2022
Aggiungi funzionalità

GET /tickersAggiunta la funzione di ricerca completa dei ticker
14 ottobre 2022
Cambiamento di funzione

GET /tradesAggiungere una proprietà di asset di commissione nella risposta (feeAsset)
POST /ordersAggiunto testo riguardante le modifiche alla politica sulle commissioni di transazione
Tutte le commissioni di negoziazione vengono pagate sull'asset quotato della coppia di trading. (Applicabile dopo la manutenzione ordinaria del 1° novembre 2022)
Per gli ordini di vendita, viene applicata una commissione all'asset quotato ottenuto dopo il completamento della vendita. Ad esempio, un utente che ha ricevuto 10.000 KRW in una transazione di vendita paga una commissione di transazione di 20 KRW (ipotizzando una commissione dello 0,2%) e riceve 9.980 KRW.
Per gli ordini di acquisto, l'acquirente deve disporre di un saldo sufficiente a coprire l'importo della quotazione dell'ordine più la commissione (saldo della quotazione > importo della quotazione dell'ordine + commissione (importo * commissione)) . Ad esempio, se un utente inserisce un ordine di acquisto per 10.000 won, è richiesto un minimo di 10.020 won (ipotizzando una commissione dello 0,2%).
https://www.gopax.co.kr/notice/1303
6 settembre 2022
Aggiungi funzionalità

Aggiungere informazioni di cautela sugli investimenti
25 maggio 2021
Cambiamento di funzione

GET /trading-pairs/<TradingPair>/bookLimitare le chiamate a un massimo di 1 al secondo (prima della modifica: massimo 20 chiamate al secondo)
Per visualizzare il registro degli ordini in tempo reale, consigliamo di utilizzare la funzionalità "Abbonamento al registro degli ordini" dell'API Websocket.
2 marzo 2021
Aggiungi funzionalità

GET /orders?tradingPairName=ETH-KRWAggiunta l'opzione per visualizzare gli ordini per coppia di trading
GET /orders?status=completedAggiungi l'opzione di stato dell'ordine
GET /orders?since=1601032379683&filterByUpdatedAt=trueAggiunta opzione per impostare l'ora di inizio in base a createdAt/updatedAt
GET /orders?limit=1000&tail=trueAggiunta l'opzione per cercare in base al numero massimo di dati, agli ordini più recenti o più vecchi
GET /trades?tradingPairName=BTC-KRWAggiunta l'opzione per registrare le transazioni per coppia di trading
GET /deposit-withdrawal-status?asset=BTCAggiunta l'opzione per visualizzare i registri di deposito/prelievo per asset
GET /trading-pairs/BTC-KRW/candles?limit=1024Aggiunta l'opzione di conteggio dei dati del grafico
24 febbraio 2021
Cambiamento di funzione

Per migliorare la stabilità del sistema, il periodo di visualizzazione dopo l'annullamento dell'ordine o il saldo completo è stato ridotto da 1 ora a 10 minuti.
12 gennaio 2021
Aggiungi funzionalità

GET /trading-pairs/<TradingPair>/price-tick-sizeAggiungi funzionalità
29 dicembre 2020
Aggiungi funzionalità

GET /noticesAggiungi funzionalità
28 ottobre 2020
Aggiungi dati di risposta

GET /assetsscale, withdrawalFee, e withdrawalAmountMinaggiungi ai dati di risposta
GET /trading-pairsbaseAssetScale, quoteAssetScale, priceMin, e restApiOrderAmountMinaggiungi ai dati di risposta
GET /trading-pairs/<TradingPair>/tickersquoteVolumeAggiungi ai dati di risposta
6 ottobre 2020
Miglioramento della documentazione

Miglioramento della leggibilità e della concisione del documento
26 agosto 2020
Aggiungi funzionalità

GET /orders?pagination=trueLa paginazione viene fornita fornendo opzioni aggiuntive.
18 agosto 2020
Aggiungi dati di risposta

GET /balancesGET /trading-pairs/<Trading Pair>/bookAggiungere l'ora di aggiornamento più recente ai dati di risposta di
11 agosto 2020
Cambiamento di funzione

GET /trades?deepSearch=trueAggiungi opzioni
30 giugno 2020
Aggiungi funzionalità

GET /orders?includePast=trueFornisce un'opzione aggiuntiva per visualizzare un elenco degli ordini completamente eseguiti e annullati.
9 giugno 2020
Aggiungi funzionalità

Quando si forniscono dati sull'ordine, balanceChange viene fornito per identificare facilmente le modifiche al saldo dell'utente dovute all'ordine.
Le commissioni maker e taker sono descritte separatamente in balanceChange.
26 maggio 2020
Aggiungi funzionalità

Introduzione di RECEIVE-WINDOW, una delle funzionalità avanzate, che consente ai clienti di specificare il valore massimo consentito di latenza di rete.
13 maggio 2020
Aggiungi funzionalità

Introdotto il timestamp per sostituire il Nonce esistente, per comodità del cliente.
24 marzo 2020
Aggiungi funzionalità

Controlla la cronologia dei depositi/prelievi
Controlla l'indirizzo di deposito delle risorse virtuali (criptovalute)
Controlla l'indirizzo di prelievo delle risorse virtuali (criptovalute)
Controlla l'ora del server
7 marzo 2020
Cambiamento di politica

Migrazione del Nonce e impostazione del limite superiore del Nonce (miglioramento dei problemi causati dall'eccessivo aumento del Nonce)
25 febbraio 2020
Aggiungi funzionalità

ID ordine cliente: quando si registra un ordine, l'utente può effettuare un ordine con qualsiasi ID ordine.
19 febbraio 2020
Aggiungi funzionalità

Stop Order: registra un ordine di un tipo predefinito quando il prezzo corrente raggiunge il prezzo Stop.
7 gennaio 2020
Aggiungi funzionalità

Protezione degli ordini: questa funzione di protezione degli ordini impedisce l'esecuzione di ordini di acquisto/vendita a prezzi superiori al 10% del prezzo iniziale dell'ordine. Se il prezzo supera il 10%, il saldo rimanente dell'ordine viene annullato.
PO (solo per posta): se è presente un contrordine che può essere eseguito immediatamente, l'ordine viene annullato. In caso contrario, l'intero ordine viene registrato.
IOC (Immediate-Or-Cancel Order): condizione in cui una transazione viene conclusa per la quantità per la quale è possibile concludere un contratto di vendita tra le quantità indicate al momento della ricezione dell'ordine, e la quantità per la quale non è stato concluso un contratto di vendita viene annullata (conclusione immediata, annullamento della quantità rimanente).
FOK (Fill-Or-Kill Order): se un contratto di vendita può essere concluso per l'intera quantità indicata al momento della ricezione dell'offerta, la transazione è conclusa. In caso contrario, l'intera quantità viene annullata (contratto completo, annullamento totale).
8 agosto 2018
Aggiungi funzionalità

Ordine di mercato: eseguito al prezzo di mercato corrente senza specificare un prezzo.
16 dicembre 2017
funzione

Chiamate che richiedono l'autenticazione
Controlla il saldo
Controlla il saldo in base al nome dell'asset
Controlla l'ordine
Cerca ordini per ID ordine
Registra il tuo ordine
Annulla un ordine tramite ID ordine
Visualizza la cronologia delle transazioni dell'utente
Richieste che non richiedono autenticazione
Controllare le risorse
Cerca una coppia di trading specifica
Controlla il volume di trading di una coppia di trading specifica
Visualizza il libro degli ordini per una coppia di trading specifica
Visualizza le transazioni recenti
Visualizza le statistiche delle ultime 24 ore per una specifica coppia di trading.
Visualizza i record passati per una coppia di trading specifica
Visualizza le statistiche delle ultime 24 ore per tutte le coppie di trading