La API de Buda.com
Qué bien! Has llegado a la documentación de la API de Buda.com. Si no eres desarrollador, quizás te sientas un poco perdido, pero no te preocupes, queremos que todos puedan entender cómo funciona y cómo podemos ayudarte.

La API de Buda.com es un puente que facilita la comunicación entre otros sistemas y nuestra plataforma. Consta de un conjunto de endpoints (rutas) mediante las cuales puedes realizar diversas consultas o acciones, ya sea sobre información pública o sobre tu cuenta de Buda.com si realizas la autenticación necesaria.

Si quieres seguir profundizando, en esta página se encuentra el detalle sobre cada uno de los endpoints que ofrece Buda.com, se describen sus propósitos, la estructura necesaria y la información que retornan.

Ahora que tienes una idea general de qué es la API, te contamos que ofrecemos APIs Rest y Websocket para ti o tu empresa. Estas te permiten construir lo que necesites de la manera más cómoda y flexible. Aquí encontrarás la documentación de ambos protocolos.

Si no eres desarrollador pero crees que a alguien de tu empresa o amigos les puede interesar, ¡no dudes en compartirles esta web para que se informen!

REST API
Introducción
Un ejemplo de llamada utilizando la librería requests

import requests # install requests with `pip install requests`

url = 'https://www.buda.com/api/v2/markets/eth-btc/ticker'
response = requests.get(url)
print(response.json())
La API de Buda.com, como la de la mayoría de los exchanges de criptomonedas, se divide en llamadas públicas y llamadas privadas:

Las llamadas públicas no requieren decir quién eres para usarlas, son datos públicos. De hecho, las puedes probar directamente en tu browser (agregando .json al final del path). Por ejemplo, prueba ingresando la siguiente URL: https://www.buda.com/api/v2/markets/eth-btc/ticker.json

Las llamadas privadas necesitan autenticación, así que para usarlas necesitas obtener un par API-KEY / API-SECRET desde tu cuenta. Para esto debes iniciar sesión en buda.com e ir a la sección de Configuración donde encontrarás la pestaña API Keys en la cual podrás crear llaves con diferentes niveles de permisos y fechas de expiración.

En general, los URL de nuestra API se forman así

https://www.buda.com/api/[version]/[path].[format]

Donde, por el momento:

Parameter	Value
version	v2
format	json
Librerias Open Source
Clientes
Si te quieres ahorrar un poco de trabajo, aquí tienes una recopilación de clientes de nuestra API en distintos lenguajes.

Ojo, estas librerías no son oficiales ni han sido probadas por el equipo de Buda.com, pero hemos hablado con sus autores y se ven buenas personas 😉

Lenguaje	Link
Go	https://github.com/niedbalski/go-buda
Java	https://github.com/FeroSalgado/java-surbtc-api
Java	https://github.com/daplay/jsurbtc
Javascript	https://github.com/ajunge/buda-promise
Python	https://github.com/delta575/trading-api-wrappers
Python	https://github.com/CriptoPagos/surbtc-api-client-python
Si quieres compartir tu librería o ejemplo con la comunidad, escríbenos a soporte@buda.com

Otras librerías
No podemos dejar de contarte sobre CCXT, una librería muy útil que te permite conectarte a más de 100 exchanges (incluyendo a Buda ❤️) usando Python, Javascript o PHP. Sí, en serio.

Llamadas Públicas
Mercados
import requests

url = 'https://www.buda.com/api/v2/markets'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "markets": [
    {
      "id": "BTC-CLP",
      "name": "btc-clp",
      "base_currency": "BTC",
      "quote_currency": "CLP",
      "minimum_order_amount": ["0.001", "BTC"],
      "taker_fee": "0.8",
      "maker_fee": "0.4",
      "max_orders_per_minute":100,
      "maker_discount_percentage":"0.0",
      "taker_discount_percentage":"0.0",
      "maker_discount_tiers":{
        "*": 0.5
      },
      "taker_discount_tiers":{
        "*": 0.0,
        "6": 0.2,
        "7": 0.3
      }
    },
    {
      "id": "BTC-COP",
      "name": "btc-cop",
      "base_currency": "BTC",
      "quote_currency": "COP",
      "minimum_order_amount": ["0.001", "BTC"],
      "taker_fee": "0.8",
      "maker_fee": "0.4",
      "max_orders_per_minute":100,
      "maker_discount_percentage":"0.0",
      "taker_discount_percentage":"0.0",
      "maker_discount_tiers":{
        "*": 0.5
      },
      "taker_discount_tiers":{
        "*": 0.0,
        "6": 0.2,
        "7": 0.3
      }
    },
    ...
  ]
}

Obtener detalles de un mercado

import requests

market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "market": {
    "id": "BTC-CLP",
    "name": "btc-clp",
    "base_currency": "BTC",
    "quote_currency": "CLP",
    "minimum_order_amount": ["0.001", "BTC"],
    "taker_fee": "0.8",
    "maker_fee": "0.4",
    "max_orders_per_minute":100,
    "maker_discount_percentage":"0.0",
    "taker_discount_percentage":"0.0",
    "maker_discount_tiers":{},
    "taker_discount_tiers":{}
  }
}

Un mercado permite separar las compras y ventas por moneda. En un mercado se compra y vende un tipo de moneda (base_currency) y se usa otro tipo de moneda para pagar por estas compras y ventas (quote_currency). Por lo tanto, un mercado está identificado por las siglas que representa a este par de monedas.

Por ejemplo: el nombre del mercado en el cual se transan ethers (ETH) contra bitcoins (BTC) es: eth-btc.

HTTP Request

GET /markets

GET /markets/<market_id>

Path Parameters

Parámetro	Descripción
market_id	(opcional) La ID del mercado (Ej: btc-clp, eth-btc, etc).
Puedes obtener un listado completo de estos identificadores realizando la llamada sin incluir este parámetro.
Response Details

Key	Tipo	Descripción
id	[string]	Identificador del mercado
name	[string]	Nombre del mercado el cual corresponde al market_id
base_currency	[string]	Moneda de cambio
quote_currency	[string]	Moneda de pago
minimum_order_amount	[amount, currency]	Tamaño de orden mínimo aceptado
taker_fee	[amount]	Tarifa pagada por una orden taker
maker_fee	[amount]	Tarifa pagada por una orden maker
max_orders_per_minute	[amount]	Rate Limit para trading que tiene este mercado
maker_discount_percentage	[string]	Descuento Maker que tiene el mercado
taker_discount_percentage	[string]	Descuento Taker que tiene el mercado
maker_discount_tiers	[hash]	Descuento Maker por tiers que tiene el mercado
taker_discount_tiers	[hash]	Descuento Taker por tiers que tiene el mercado
Volumen transado
import requests

market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/volume'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "volume": {
    "ask_volume_24h": ["4.97241513", "BTC"],
    "ask_volume_7d": ["43.15391694", "BTC"],
    "bid_volume_24h": ["8.03642037", "BTC"],
    "bid_volume_7d": ["35.77704356", "BTC"],
    "market_id": "BTC-CLP"
  }
}
Esta llamada permite acceder a información del volumen transado en un determinado mercado, donde ask_volume representa el monto transado en órdenes de venta y bid_volume corresponde al monto transado de órdenes de compra.

HTTP Request

GET /markets/<market_id>/volume

Response Details

Key	Tipo	Descripción
ask_volume_24h	[amount, currency]	Monto transado de órdenes de venta durante las últimas 24 horas
ask_volume_7d	[string]	Monto transado de órdenes de venta durante las últimos 7 dias
bid_volume_24h	[amount, currency]	Monto transado de órdenes de compra durante las últimas 24 horas
bid_volume_7d	[string]	Monto transado de órdenes de compra durante las últimos 7 dias
market_id	[string]	Identificador del mercado consultado
Ticker
import requests

market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "ticker": {
    "last_price": ["879789.0", "CLP"],
    "market_id": "BTC-CLP",
    "max_bid": ["879658.0", "CLP"],
    "min_ask": ["876531.11", "CLP"],
    "price_variation_24h": "0.005",
    "price_variation_7d": "0.1",
    "volume": ["102.0", "BTC"]
  }
}
El ticker permite ver el estado actual de un determinado mercado. La respuesta a esta llamada entrega las mejores ofertas de compra y venta (bid y ask), asi como el precio de la ultima transacción (last_price) para el mercado solicitado. También incluye información como el volumen diario y cuanto ha cambiado el precio en las últimas 24 hrs.

HTTP Request

GET /markets/<market_id>/ticker

Path Parameters

Parámetro	Descripción
market_id	La ID del mercado (Ej: btc-clp, eth-btc, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados.
Response Details

Key	Tipo	Descripción
market_id	[currency]	Identificador del mercado consultado
last_price	[amount, currency]	Precio de la última orden ejecutada
min_ask	[amount, currency]	Menor precio de venta
max_bid	[amount, currency]	Máximo precio de compra
volume	[amount, currency]	Volumen transado en las últimas 24 horas
price_variation_24h	[float]	Cuanto ha variado el precio en las últimas 24 horas (porcentaje)
price_variation_7d	[float]	Cuanto ha variado el precio el los últimos 7 días (porcentaje)
Todos los Tickers
import requests

url = f'https://www.buda.com/api/v2/tickers'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "tickers": [
    {"market_id":"BTC-CLP","price_variation_24h":"0.001","price_variation_7d":"-0.004","last_price":["14525279.0","CLP"]},
    {"market_id":"ETH-CLP","price_variation_24h":"-0.002","price_variation_7d":"0.024","last_price":["1105000.0","CLP"]},
    ...
  ]
}
Permite ver el estado actual de todos los mercados. La respuesta a esta llamada entrega la varianción del precio en el último día y en la última semana, junto con el precio de la última transacción (last_price) para cada mercado.

HTTP Request

GET /tickers

Response Details

Key	Tipo	Descripción
market_id	[currency]	Identificador del mercado consultado
last_price	[amount, currency]	Precio de la última orden ejecutada
price_variation_24h	[float]	Cuanto ha variado el precio en las últimas 24 horas (porcentaje)
price_variation_7d	[float]	Cuanto ha variado el precio el los últimos 7 días (porcentaje)
Libro de órdenes
import requests

market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/order_book'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "order_book": {
    "asks": [
      ["836677.14", "0.447349"],
      ["837462.23", "1.43804963"],
      ["837571.89", "1.41498541"],
      ["837597.23", "0.13177617"],
      ["837753.25", "1.40724154"],
      ["837858.51", "1.40988433"],
      ["837937.0", "1.46619702"],
      ["838000.57", "1.4527277"],
      ["838305.78", "0.8317892"],
      ...
    ],
    "bids": [
      ["821580.0", "0.25667389"],
      ["821211.0", "0.27827307"],
      ["819882.39", "1.40003128"],
      ["819622.99", "1.40668862"],
      ["819489.9", "1.41736995"],
      ["818942.2", "1.41001753"],
      ["818820.29", "0.93677863"],
      ["816879.83", "1.44022295"],
      ...
    ]
  }
}
Obtén el listado de todas las órdenes que se encuentran activas en el mercado seleccionado.

HTTP Request

GET /markets/<market_id>/order_book

Path Parameters

Parámetro	Descripción
market_id	El ID del mercado (Ej: eth-btc, btc-clp, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados
Response Details

Key	Tipo	Descripción
asks	[price, amount]	Arreglo de ordenes del libro de ventas
bids	[price, amount]	Arreglo de ordenes del libro de compras
Trades
import time
import requests

market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/trades'
response = requests.get(url, params={
    'timestamp': int(time.time()) - 60 * 60 * 24 * 7,
    'limit': 50,
})
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "trades": {
    "timestamp": "1476905551698",
    "last_timestamp": "1476380738941",
    "market_id": "BTC-CLP",
    "entries": [
      ["1476905551687", "0.00984662", "435447.12", "buy"],
      ["1476905551676", "3.01572553", "435283.3", "buy"],
      ...
    ]
  }
}
Obtén el listado de las transacciones más recientes del mercado indicado.

HTTP Request

GET markets/<market_id>/trades

Path Parameters

Parámetro	Descripción
market_id	El ID del mercado (Ej: eth-btc, btc-clp, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados
URL Parameters

Se incluyen al final del URL ej: GET /markets/BTC-CLP/trades?timestamp=1502472564000

Parameter	Descripción
timestamp	(opcional) Unix timestamp en milisegundos del trade más reciente a solicitar.
limit	(opcional) Número de trades solicitados [default: 50, max: 100]
Response Details

Key	Tipo	Descripción
entries	[timestamp, amount, price, direction]	Arreglo de transacciones
timestamp	[timestamp]	Unix timestamp del trade más reciente incluido en la respuesta
last_timestamp	[timestamp]	Unix timestamp del trade más antiguo incluido en la respuesta
market_id	[currency]	Identificador del mercado consultado
Si necesitas abarcar un período de tiempo mayor que el entregado por este endpoint puedes "enlazar múltiples llamadas" en base a las respuestas timestamp y last_timestamp.
Cotizaciones
import requests

market = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
response = requests.post(url, json={
    'type': 'bid_given_size',
    'amount': 1,
})
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "quotation": {
    "amount": ["1.0", "BTC"],
    "base_balance_change": ["0.99200003", "BTC"],
    "base_exchanged": ["1.0", "BTC"],
    "fee": ["0.00799997", "BTC"],
    "incomplete": false,
    "limit": null,
    "order_amount": ["1.0", "BTC"],
    "quote_balance_change": ["-4872696.01", "CLP"],
    "quote_exchanged": ["4872696.01", "CLP"],
    "type": "bid_given_size"
  }
}
Obtén una cotización de acuerdo al libro de órdenes del momento.

 Esta llamada utiliza el estado del libro de ordenes en el momento en el que se consulta. Como el libro de órdenes cambia constantemente no es posible asegurar los valores de ejecución de una orden y debes considerar la respuesta a estas llamadas como una estimación.
Los tipos de cotizaciones

Dependiendo del dato que quieras saber, este endpoint permite realizar distintos tipos de cotizaciones.

Considerando que los mercados están identificados por el par de monedas <base_currency>-<quote_currency> (a continuación usaremos como ejemplo el mercado eth-btc), a través de este endpoint puedes obtener simulaciones correspondiente a ejecuciones de órdenes de compra o venta de cierta cantidad (amount) de base_currency o quote_currency. (Si no tienes muy claro lo que es una orden de compra o venta puedes revisar la documentación de la sección Mis órdenes).

Para esto, es necesario seleccionar una de las siguientes opciones y enviarla como parámetro type en el payload.

Tipo simulación	Descripción
bid_given_size ó bid_given_earned_base	Simula una orden de compra donde amount representa la cantidad de base_currency a recibir (ej: ¿Cuánto btc se requiere para obtener amount eth?)
bid_given_value ó bid_given_spent_quote	Simula una orden de compra donde amount representa la cantidad de quote_currency a gastar (ej: ¿Cuánto eth obtendré si ejecuto una orden de compra por amount btc?)
ask_given_size ó ask_given_spent_base	Simula una orden de venta donde amount representa la cantidad de base_currency a gastar. (ej: ¿Cuánto btc recibiría si ejecuto una orden de venta por amount eth?)
ask_given_value ó ask_given_earned_quote	Simula una orden de venta donde amount representa la cantidad de quote_currency a recibir (ej: ¿Cuánto eth se requiere para obtener amount btc?)
HTTP Request

POST '/markets/<market_id>/quotations

Path Parameters

Parámetro	Descripción
market_id	El ID del mercado (Ej: eth-btc, btc-clp, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados
Request Payload

Key	Required	Descripción
type	Yes	Tipo de cotización a realizar (ver siguiente tabla)
amount	Yes	Monto a simular (representa base_currency o quote_currency) dependiendo del parámetro type
limit	No	El precio pedido para la moneda en la cual se expresa el parámetro amount.
Response Details

Key	Tipo	Descripción
amount	[amount, currency]	Es el mismo valor del parámetro amount enviado como parte de la cotización
base_balance_change	[amount, currency]	Cuanto cambiaría tu saldo en la moneda base_currency (ya considerados los fees). Ten presente que este número puede ser positivo o negativo (tu saldo puede aumentar o disminuir después de la ejecución de una orden)
base_exchanged	[amount, currency]	El monto total de base_currency que se transaría en el mercado (siempre es un valor positivo)
fee	[amount, currency]	Tarifa que se cobraría por la ejcución de la orden.
incomplete	[boolean]	Indica si dadas las actuales condiciones del mercado (profundidad y tu saldo disponible) sólo sería posible ejecutar una porción de la orden.
limit	[amount, currency]	El parámetro limit enviado junto con la moneda correspondiente
order_amount	[amount, currency]	Corresponde al mismo valor que base_exchanged
quote_balance_change	[amount, currency]	Cuanto cambiaría tu saldo en la moneda quote_currency (ya considerados los fees). Ten presente que este número puede ser positivo o negativo (tu saldo puede aumentar o disminuir después de la ejecución de una orden)
quote_exchanged	[amount, currency]	El monto total de quote_currency que se transaría en el mercado (siempre es un valor positivo)
type	[string]	Tipo de cotización solicitada
Sobre el cálculo de las tarifas (fee)

Ten presente que las tarifas por transacciones dependen de los montos mensuales transados por cada usuario.
Es por esto que, en caso que consultes este endpoint sin autenticarte, las tarifas entregadas como respuestas corresponden a las tarifas máximas del mercado.
Si deseas realizar simulaciones considerando las tarifas reales que se te cobrarían debes consultar este endpoint usando autenticación.
Dependiendo del valor enviado como parámetro limit (si es que es enviado) puede suceder que cierto monto de la orden se ejecute inmediatamente a precio mercado y quede otro saldo pendiente de ejecución como una orden límite.
En caso que parte de la orden se ejecute inmediatamente como orden tipo mercado, los fees calculados corresponden a todo los fees de orden tipo mercado del monto que se transaría como una orden mercado + el fee de orden tipo límite correspondiente al monto que se transaría como una orden límite.
Costos de abonos/retiros
import requests

currency = 'btc'
transaction_type = 'withdrawal'
url = f'https://www.buda.com/api/v2/currencies/{currency}/fees/{transaction_type}'
response = requests.get(url)
print(response.json())
Esta llamada entrega un objeto con el siguiente formato:

{
  "fee": {
    "name": "withdrawal",
    "percent": 0,
    "base": ["0.00000015", "BTC"]
  }
}
Entrega los costos asociados a realizar un abono o retiro en la moneda seleccionada.

Ten presente:

Estos costos no están asociados a Buda, son los costos que cobra la red de la moneda seleccionada por la ejecución de la operación (por ejemplo, cuánto es el fee que se debe agregar a un retiro Bitcoin para que la transacción se incluya con una alta probabilidad dentro de los siguientes 3 bloques).
Dependiendo de la moneda, los abonos/retiros fiat también pueden tener costos asociados.
Es responsabilidad de quien realiza un abono cripto incluir el fee necesario para que la transacción se confirme en la red correspondiente.
HTTP Request

GET /currencies/<currency>/fees/<transaction_type>

Path Parameters

Parameter	Descripción
currency	Acrónimo de la moneda a consultar
transaction_type	Tipo de operación. Puede ser deposit (abono) o withdrawal (retiro)
Response Details (JSON)

Key	Tipo	Descripción
name	[string]	Tipo de operación consultada
percent	[number]	Porcentaje del monto total de la transacción que cobra la red por realizar la operación.
base	[amount, currency]	Costo fijo por transacción que cobra la red por realizar la operación.







Rate Limits
Tomamos alguna medidas para protegernos de ataques DoS o abusos en nuestra api. Esto para poder asegurar que el servicio sea estable para todos nuestros usuarios.

Si tu request es limitado, recibirás una respuesta con el código 429,debes esperar antes de intentar nuevamente.

Los límites se calculan en ventanas de 1 minuto y de 1 segundo. Para las ventanas de 1 segundo, mientras hagas menos 20 requests/segundo no debieras gatillar el límite.

General
Las llamadas anónimas (no autenticadas), serán limitadas por dirección IP a una tasa de 120 requests/minuto. Las llamadas autenticadas, serán limitadas por api key a 375 requests/minuto.

Trading (crear y cancelar órdenes)
Los endpoints para crear y eliminar órdenes son limitados por mercado. El limite es dependiente del tier. Puedes ver más detalles en la página de comisiones.

Tier	Volumen 30 días	Rate Limit
< 7	< $100 000	100 requests/minuto/mercado
>= 7	>= $100 000	250 requests/minuto/mercado
 Los valores de los límites estan en constante evaluación y ajuste. Si ocurre un cambio permanente de estos valores actualizaremos esta sección, por lo que te recomendamos revisarla periódicamente.
 Te pedimos que diseñes tu aplicación para que no tengas respuestas constantemente limitadas por el rate limit. Trata de mantenerte dentro de los límites para que tu cuenta no sea bloqueada.
Errores
Tratamos que la API se adhiera lo máximo posible a las convenciones de códigos de errores HTTP.

Adicionalmente, en caso de un error, la API además envía un objeto JSON con más información como muestra el ejemplo.

Example error response (HTTP 403):

{
  "code": "forbidden",
  "message": "You dont have access to this resource"
}
Una explicación más detallada de los códigos HTTP que la API de buda.com utiliza es la siguiente:

Código HTTP	Significado
400	Bad Request -- La solicitud contiene sintaxis errónea y no debería repetirse. Si estás haciendo una solicitud de tipo POST, revisa que el objeto que estás enviando va como JSON en el body de la solicitud y que estás usando la cabecera Content-Type: application/json.
401	Unauthorized -- Tu API Key es inválida o no estás realizando la autenticación de acuerdo al formato requerido por la API.
403	Forbidden -- La solicitud es válida, pero no cuentas con los permisos para realizarla.
404	Not Found -- Recurso no encontrado. Revisa la URL que estás solicitando.
405	Method Not Allowed -- Has intentado acceder a un endpoint con el método incorrecto (por ejemplo, hacer GET en vez de POST).
406	Not Acceptable -- Has solicitado un formato no soportado por el servidor. Revisa que la cabecera Accept que estás enviando especifique el formato JSON (Accept: application/json)
410	Gone -- El recurso solicitado fue eliminado y no tiene sentido reintentar la solicitud.
422	Unprocessable entity -- Has enviado información en un formato inválido. Revisa que el objeto que estás enviado como body en la solicitud POST calce con esta documentación (p.ej: en general los strings que debes enviar son case-sensitive).
429	Too Many Requests -- Has superado el límite de solicitudes Rate Limits
500	Internal Server Error -- Ha habido un problema con nuestro servidor y probablemente estamos rodeados por llamas mientras lo tratamos de solucionar 🔥. Vuelve a intentarlo más tarde.
503	Service Unavailable -- Estamos temporalmente fuera de servicio por mantenimiento. Vuelve a intentarlo más tarde.
Websockets API
Introducción
import websocket

def on_message(ws, message):
    print(message)

def on_open(ws):
    print('web-socket connected.')

def channels():
    pubsub_key = "pubsub_key"
    chs = [
        "book%40btcclp",
        "book%40ethclp",
        "trades%40btcclp",
        f"balances%40{pubsub_key}",
        f"orders%40{pubsub_key}"
    ]
    return ",".join(chs)



if __name__ == "__main__":
    SOCKET = f"wss://realtime.buda.com/sub?channel={channels()}"
    ws = websocket.WebSocketApp(SOCKET, on_message = on_message)
    ws.on_open = on_open
    ws.run_forever(ping_interval=10)
Los eventos tienen la siguiente estructura:

{
 ev: 'book-sync',
 ts: '123123123.123123',
 mk: 'BTC-CLP',
 ...
}
Los websockets permiten abrir canales entre cliente y servidor, para poder hacer streaming de datos en tiempo real. Con esta API puedes comunicarte con nuestro servidor y recibir respuestas en base a eventos, en vez de tener que estar constantemente consultando.

Para la comunicación realtime estamos usando Nchan, por lo que se puede usar websockets para subscribirse a los eventos. Hay más información de cómo funciona nchan con websockets en https://nchan.io/#subscriber-endpoints.

Para poder acceder a los websockets autenticados necesitas tu pubsub_key, la cual puedes encontrar en tu información personal.

En general, los URL de nuestros websockets se forman así:

wss://realtime.buda.com/sub?channel=[channel]

Para los casos que se requiere autenticación se forman así:

wss://realtime.buda.com/sub?channel=[channel]@[pubsub_key]

En caso de querer suscribirte a varios canales al mismo tiempo entonces se forman así:

wss://realtime.buda.com/sub?channel=[channel1,channel2,channel3@pubsub_key]

Donde:

Path Parameters

Parameter	Value
channel	canal a utilizar
pubsub-key	llave pubsub de tu cuenta que puede ser encontrada en información personal
Event Details

Key	Descripción
ev	Nombre del evento
ts	Unix timestamp del evento (segundos.nanosegundos)
mk	ID del mercado que corresponde en caso de haberlo (Ej: ETH-BTC, BTC-CLP, etc).
 Recuerda utilizar %40 en vez de @ al llamar a un canal si es que no estás manejando el encoding del url.
Canales públicos
Libro de órdenes
import websocket

def on_message(ws, message):
    print(message)

def on_open(ws):
    print('web-socket connected.')

if __name__ == "__main__":
    SOCKET = "wss://realtime.buda.com/sub?channel=book%40btcclp"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_message = on_message)
    ws.on_open = on_open
    ws.run_forever(ping_interval=10)
Los eventos de este canal tienen la siguiente estructura:

{
  ev: 'book-changed',
  change: [
    'asks'|'bids',
    <nivel de precio>,
    <cambio de monto>
  ]
}

{
  ev: 'book-sync',
  order_book: <libro de órdenes serializado>
}
Para suscribirse al canal de cambios en el libro de órdenes del mercado indicado. Cada 5 minutos se envía un snapshot completo del libro para ayudar en la sincronización.

Channel endpoint

channel=book@<market_id>

Path Parameters

Parámetro	Descripción
market_id	El ID del mercado (Ej: ethbtc, btcclp, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados
 Recuerda utilizar %40 en vez de @ al llamar a un canal si es que no estás manejando el encoding del url.
Trades
import websocket

def on_message(ws, message):
    print(message)

def on_open(ws):
    print('web-socket connected.')

if __name__ == "__main__":
    SOCKET = "wss://realtime.buda.com/sub?channel=trades%40btcclp"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_message = on_message)
    ws.on_open = on_open
    ws.run_forever(ping_interval=10)
Los eventos de este canal tienen la siguiente estructura:

{
  ev: 'trade-created',
  trade: [
    <timestamp>,
    <monto trade>,
    <precio trade>,
    'buy'|'sell',
    <id>
  ]
}
Para suscribirse al canal de las nuevas transacciones públicas del mercado indicado.

Channel endpoint

channel=trades@<market_id>

Path Parameters

Parámetro	Descripción
market_id	El ID del mercado (Ej: ethbtc, btcclp, etc).
Puedes obtener un listado completo de estos identificadores a través de la llamada al endpoint de Mercados
Event Details

Key	Descripción
ev	Nombre del evento
timestamp	Unix timestamp del trade más reciente
monto	Monto del trade más reciente
precio	Precio del trade más reciente
 Recuerda utilizar %40 en vez de @ al llamar a un canal si es que no estás manejando el encoding del url.
Canales privados
Balances
import websocket

def on_message(ws, message):
    print(message)

def on_open(ws):
    print('web-socket connected.')

if __name__ == "__main__":
    SOCKET = "wss://realtime.buda.com/sub?channel=balances%40{pubsub_key}"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_message = on_message)
    ws.on_open = on_open
    ws.run_forever(ping_interval=10)
Los eventos de este canal tienen la siguiente estructura:

{
 ev: 'balance-updated',
 balance: <balance serializado>
}
Para suscribirse al canal de cambios en tu balance.

Channel endpoint

channel=balances@<pubsub_key>

Path Parameters

Parámetro	Descripción
pubsub_key	llave pubsub de tu cuenta que puede ser encontrada en información personal
 Recuerda utilizar %40 en vez de @ al llamar a un canal si es que no estás manejando el encoding del url.
