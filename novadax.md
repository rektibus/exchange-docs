Introdução
Bem-vindo(a) à documentação API da NovaDAX
A NovaDAX disponibiliza sua documentação de API em busca de trazer uma experiência mais rápida, segura e profissional para seus clientes.

Com nossa API, você terá acesso a dados de mercado, histórico de ordens e gerenciamento de conta, de uma maneira automatizada e prática.

Realizaremos constantemente atualizações e otimizações para nosso SDK.

Antes de começar
Criar uma conta na NovaDAX
Caso você ainda não possua uma conta na NovaDAX, crie uma agora mesmo clicando aqui.

Gerar uma chave da API
É preciso adquirir uma chave de acesso (também chamada de AccessKey) e uma chave segredo (também chamada de SecretKey) para poder autenticar as requisições. Depois do login, encontre o símbolo do usuário no menu principal e clique em "Chave de API e Subconta" no submenu para criar chaves para API.

Comunicação com a API
Os endpoint da API NovaDAX se dividem em públicos e privados.

Endpoints públicos
Podem ser acessados sem necessidade de autenticação para obter:

Informações básicas
Dados de mercado
Endpoints privados
Precisam ser acessados com autenticação para gerenciar:

Ordens
Conta
Carteira
Acesso a URLs
https://api.novadax.com

Limites de Taxa do Endpoint
Cada endpoint é atribuído um peso correspondente, e o valor desse peso é diretamente proporcional ao consumo de recursos.
Cada endpoint retornará um cabeçalho X-Nova-Weight-Used na resposta para que você possa entender o peso consumido atualmente.
O peso total disponível por minuto é de 6000. Ao atingir esse limite, você receberá um erro HTTP 429.
Para endpoints públicos, o cálculo de peso é baseado em endereços IP, enquanto para endpoints privados, é baseado em AccountId.
Autenticação
A fim de proteger a comunicação da API contra alterações não autorizadas, todas as chamadas de endpoints privados precisam ser autenticadas com sua API AccessKey.

Estrutura das requisições válidas

É necessário fazer uma chamada para a URL api.novadax.com, por exemplo, https://api.novadax.com/v1/common/symbols.

AccessKeyId: sua API AccessKey

Signature Method: utilize HMAC-SHA256 hash

Timestamp: a hora atual do sistema em milissegundos, por exemplo, 1564988445199.

Parâmetros obrigatórios e opcionais: existem parâmetros obrigatórios e opcionais para acessar cada endpoint. Você pode verificar o significado desses parâmetros na descrição de cada endpoint.

Signature: mensagem criptografada para prevenir transportes e alterações não autorizadas.

Método de Autenticação
Passos para autenticar uma requisição GET
1. Query string é
queryStr = "name=joao&cpf=123456&birthday=2017-08-01"

2. Codifique a query string de consulta e ordene parâmetros seguindo a ordem ASCII.
sort(urlencode(queryStr)) // birthday=2017-08-01&cpf=123456&name=joao

3. Transforme a string com formato {método de requisição}\n{caminho de requisição}\n{string a ser codificada}\n{timeStamp}
signStr = GET\n/v1/orders/get\nbirthday=2017-08-01&cpf=123456&name=joao\n1564988445199

4. Utilize a string gerada no passo 3 e sua "SecretKey" para autenticar sua requisição
sign = hmac_sha256(signStr,SecretKey)

5. Adicione Accesskey, Signature e TimeStamp para o cabeçalho (header) da requisição.
request.header.add("X-Nova-Access-Key",AccessKey)

request.header.add("X-Nova-Signature",Sign)

request.header.add("X-Nova-Timestamp",TimeStamp)

6. Exemplo de autenticação GET em Java
Tux, the Linux mascot

Passos para autenticar uma requisição POST
1. O corpo da requisição (request body) é
body = {"name":"joao","cpf":"123456","birthday":"2017-08-01"} // MD5 value is 7d8f374d786079cfade9d1c2a358137c

2. Transforme o "corpo da requisição" com o algoritmo MD5, seguindo o formato %s\n%s\n%s\n%s
signStr = POST\n/v1/order/create\n7d8f374d786079cfade9d1c2a358137c\n1564988445199

3. Utilize a string gerada no passo 2 e sua "SecretKey" para autenticar sua requisição
sign = hmac_sha256(signStr,SecretKey)

4. Adicione Accesskey, Signature e TimeStamp para o header da requisição.
request.header.add("X-Nova-Access-Key",AccessKey)

request.header.add("X-Nova-Signature",Sign)

request.header.add("X-Nova-Timestamp",TimeStamp)

5. Exemplo de autenticação POST em Java
Tux, the Linux mascot

 %s\n%s\n%s\n%s contém método de requisição (request method), caminho de requisição (request path), string a ser codificada e timestamp. Timestamp é a hora atual do sistema ajustado para o horário UTC em milissegundos.
Subconta
Se precisar realizar operações relacionadas a pedidos usando uma subconta, por favor, adicione o cabeçalho de solicitação X-Nova-Account-Id à sua solicitação e defina o valor como o ID correspondente da subconta.

request.header.add("X-Nova-Account-Id", "CA1234567890")

Estrutura de resposta (response)
A resposta será retornada no formato JSON. O superior de reposta em JSON contém três meta dados que são "code", "data" e "message". A sua resposta correspondente por API está no campo "data".

Estrutura de resposta de sucesso

{
    "code": "A10000",
    "data": {...},
    "message": "Success"
}

Estrutura de resposta de erro

{
    "code": "A99999",
    "data": {...},
    "message": "fail."
}

Formato de resposta:

Campo	Tipo de	Descrição
code	string	O status retornado por endpoint
message	string	A resposta simplificada
data	object	A resposta detalhada se for disponível
Tabela de códigos de status
Código	Código de status HTTP	Mensagem	Descrição
A99999	500	Failed	Erro interno
A10000	200	Success	Sucesso
A10001	400	Params error	Parâmetro inválido
A10002	404	Api not found	Endpoint não encontrado
A10003	403	Authentication failed	Falha na autenticação
A10004	429	Too many requests	Excedeu o limite de requisições
A10005	403	Kyc required	É preciso completar verificação de conta primeiro
A10006	403	Customer canceled	Conta cancelada
A10007	400	Account not exist	Subconta não existe
A10011	400	Symbol not exist	O símbolo (par) não existe
A10012	400	Symbol not trading	O símbolo (par) não está disponível para transacionar no momento
A10013	503	Symbol maintain	O símbolo (par) está em manutenção
A30001	400	Order not found	A ordem não foi encontrada
A30002	400	Order amount is too small	A quantidade é insuficiente
A30003	400	Order amount is invalid	A quantidade é inválida
A30004	400	Order value is too small	O valor é insuficiente
A30005	400	Order value is invalid	O valor é inválido
A30006	400	Price is invalid	O preço é inválido
A30007	400	Insufficient balance	O saldo é insuficiente
A30008	400	Order was closed	A ordem já foi executada
A30009	400	Order canceled	A ordem já foi cancelada
A30010	400	Order cancelling	A ordem está sendo cancelada
A30011	400	Order price too high	O preço é alto demais
A30012	400	Order price too low	O preço é baixo demais
Dúvidas Frequentes
Falha na autenticação
Certifique-se de que a API AccessKey está válida e inserida corretamente e que o IP usado é permitido para acesso.
Certifique-se de que o timestamp está ajustado para o horário UTC.
Certifique-se de que os parâmetros codificados são ordenados de acordo com a ordem ASCII.
Certifique-se de que o formato de codificação é utf-8.

Certifique-se de que a chamada GET é enviado como formulário HTTP.

Certifique-se de que a chamada POST é feita no formato JSON.

Certifique-se de que a autenticação está codificada.

Certifique-se de Content-Type: application/json é colocado no header da chamada POST.

Registros de Atualização
15/11/2023
Otimização da lógica de limite de frequência, proporcionando limites de frequência independentes para cada subconta.
Suporte para transmitir informações de operações de pedidos de subcontas através do cabeçalho de solicitação X-Nova-Account-Id.
Modificação em POST /v1/orders/create: adição do campo clientOrderId.
Modificação em POST /v1/orders/cancel: adição do campo clientOrderId.
Modificação em GET /v1/orders/get: adição do campo clientOrderId.
Modificação em GET /v1/orders/list: adição do campo clientOrderId.
Adição de POST /v1/orders/batch-create: criação de pedidos em lote.
Adição de POST /v1/orders/batch-cancel: cancelamento de pedidos em lote.
Adição de POST /v1/orders/cancel-by-symbol: cancelamento de todos os pedidos com base no par de negociação.
12/09/2023
Os Limites de Taxa do Endpoint foram ajustados, não se baseando mais em um único endpoint, mas adotando um limite baseado em peso total.
30/01/2021
Modificado GET /crypto/chain/{code}: Adicionado o campo chainAlias na resposta.
Modificado POST /v1/wallet/withdraw/coin: Adicionado o parâmetro de solicitação chainAlias.
17/12/2020
Impacto na funcionalidade de consulta de pedidos criados pela API: Após o cancelamento, não é possível consultar por 2 horas, as interfaces relacionadas são as seguintes:
GET /v1/orders/get
GET /v1/orders/list
11/11/2020
Adicionadas interfaces relacionadas ao WebSocket.
12/10/2020
Adicionado GET /v1/wallet/query/deposit-withdraw: Consulta de registros de depósito e retirada de moeda do usuário.
Adicionado GET /v1/orders/fills: Consulta de detalhes de negociação históricos.
20/05/2020
Modificado GET /v1/orders/list: O parâmetro symbol foi alterado para ser opcional.
05/03/2020
Adicionado GET /v1/common/symbol: Obtenção da configuração de um único par de moedas de negociação.
05/12/2019
Modificado POST /v1/orders/create: Adicionado o campo accountId.
Modificado GET /v1/orders/list: Adicionado o campo accountId da subconta.
Adicionado GET /v1/account/subs: Obtenção da lista de subcontas.
Adicionado GET /v1/account/subs/balance: Consulta do saldo da subconta.
Adicionado GET /v1/account/subs/transfer/record: Consulta de registros de transferência da subconta.
Adicionado POST /v1/account/subs/transfer: Iniciar transferência entre subcontas.
18/09/2019
Adicionado POST /v1/account/withdraw/coin: Retirada de moeda.
Informações básicas
Dados de um símbolo (par) específico
Retorna regras de negociação de um símbolo (par) específico.

Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "symbol": "BTC_BRL",
        "baseCurrency": "BTC",
        "quoteCurrency": "BRL",
        "amountPrecision": 4,
        "pricePrecision": 2,
        "valuePrecision": 4,
        "minOrderAmount": "0.001",
        "minOrderValue": "5"
    },
    "message": "Success"
}
Caminho de requisição
GET /v1/common/symbol

Peso: 1
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo de negociação
baseCurrency	string	Moeda de base em um símbolo de negociação
quoteCurrency	string	Moeda de cotação em um símbolo de negociação
pricePrecision	number	Precisão (casas decimais) de preço
amountPrecision	number	Precisão (casas decimais) de quantidade
valuePrecision	number	Precisão (casas decimais) de valor
minOrderAmount	string	Quantidade mínima de ordem
minOrderValue	string	Valor mínimo de ordem
Todos os símbolos (pares)
Retorna todos os símbolos (pares) disponíveis para negociar na NovaDAX.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "symbol": "BTC_BRL",
            "baseCurrency": "BTC",
            "quoteCurrency": "BRL",
            "amountPrecision": 4,
            "pricePrecision": 2,
            "valuePrecision": 4,
            "minOrderAmount": "0.001",
            "minOrderValue": "5",
        },
        {
            "symbol": "ETH_BRL",
            "baseCurrency": "ETH",
            "quoteCurrency": "BRL",
            "amountPrecision": 4,
            "pricePrecision": 2,
            "valuePrecision": 4,
            "minOrderAmount": "0.01",
            "minOrderValue": "5"
        }
    ],
    "message": "Success"
}
Caminho de requisição
GET /v1/common/symbols

Peso: 1
Parâmetro de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo de negociação
baseCurrency	string	Moeda de base em um símbolo de negociação
quoteCurrency	string	Moeda de cotação em um símbolo de negociação
pricePrecision	number	Precisão (casas decimais) de preço
amountPrecision	number	Precisão (casas decimais) de quantidade
valuePrecision	number	Precisão (casas decimais) de valor
minOrderAmount	string	Quantidade mínima de ordem
minOrderValue	string	Valor mínimo de ordem
Hora atual do sistema
Retorna a hora atual do sistema ajustado para o horário UTC em milissegundos.

Corpo de Resposta

{
    "code": "A10000",
    "data": 1565080348983,
    "message": "Success"
}
Caminho de requisição
GET /v1/common/timestamp

Peso: 1
Parâmetro de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
A hora atual do sistema ajustado para o horário UTC em milissegundos.

Dados de mercado
Obter dados de ticker de todos os pares de negociação
Retorna dados de negociação para todos os pares disponíveis na NovaDAX com o resumo de informações importantes das últimas 24 horas.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "ask": "34708.15",
            "baseVolume24h": "34.08241488",
            "bid": "34621.74",
            "high24h": "35079.77",
            "lastPrice": "34669.81",
            "low24h": "34330.64",
            "open24h": "34492.08",
            "quoteVolume24h": "1182480.09502814",
            "symbol": "BTC_BRL",
            "timestamp": 1571112216346
        }
    ],
    "message": "Success"
}

Caminho de requisição
GET /v1/market/tickers

Peso: 5
Parâmetros de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo da negociação
lastPrice	string	Preço unitário da última negociação
bid	string	Maior preço de oferta de compra das últimas 24 horas
ask	string	Menor preço de oferta de venda das últimas 24 horas
open24h	string	Preço unitário de abertura de negociação das últimas 24 horas
high24h	string	Maior preço unitário de negociação das últimas 24 horas
low24h	string	Menor preço unitário de negociação das últimas 24 horas
baseVolume24h	string	Volume de negociação na moeda de base das últimas 24 horas
quoteVolume24h	string	Volume de negociação na moeda de cotação das últimas 24 horas
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Obter dados de ticker de um par de negociação específico
Retorna dados de negociação para um par específico com o resumo de informações importantes das últimas 24 horas.

Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "ask": "34708.15",
        "baseVolume24h": "34.08241488",
        "bid": "34621.74",
        "high24h": "35079.77",
        "lastPrice": "34669.81",
        "low24h": "34330.64",
        "open24h": "34492.08",
        "quoteVolume24h": "1182480.09502814",
        "symbol": "BTC_BRL",
        "timestamp": 1571112216346
    },
    "message": "Success"
}
Caminho de requisição
GET /v1/market/ticker

Peso: 1
Parâmetros de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo de negociação
lastPrice	string	Preço unitário da última negociação
bid	string	Maior preço de oferta de compra das últimas 24 horas
ask	string	Menor preço de oferta de venda das últimas 24 horas
open24h	string	Preço unitário de abertura de negociação das últimas 24 horas
high24h	string	Maior preço unitário de negociação das últimas 24 horas
low24h	string	Menor preço unitário de negociação das últimas 24 horas
baseVolume24h	string	Volume de negociação na moeda de base das últimas 24 horas
quoteVolume24h	string	Volume de negociação na moeda de cotação das últimas 24 horas
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Obter dados de profundidade
Retorna informações de livro de ofertas para um par específico.

Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "asks": [
            ["43687.16", "0.5194"],
            ["43687.2", "1.3129"]
        ],
        "bids": [
            ["43657.57", "0.6135"],
            ["43657.46", "0.0559"]
        ],
        "timestamp": 1565057338020
    },
    "message": "Success"
}
Caminho de requisição
GET /v1/market/depth

Peso: 1
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
limit	false	number	O número de compras e vendas a retornar; máximo 50
Detalhes de resposta
Campo	Tipo	Detalhes
asks	array	Lista de ofertas de venda
asks[][0]	string	Preço de venda
asks[][1]	string	Quantidade de venda
bids	array	Lista de ofertas de compra
bids[][0]	string	Preço de compra
bids[][1]	string	Quantidade de compra
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Obter dados de execução de ordens
Retorna informações das negociações realizadas recentemente.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "price": "43657.57",
            "amount": "1",
            "side": "SELL",
            "timestamp": 1565007823401
        },
        {
            "price": "43687.16",
            "amount": "0.071",
            "side": "BUY",
            "timestamp": 1565007198261
        }
    ],
    "message": "Success"
}
Caminho de requisição
GET /v1/market/trades

Peso: 5
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
limit	false	number	O número de negociações a retornar; default 100
Detalhes de resposta
Campo	Tipo	Detalhes
price	string	Preço unitário da negociação na moeda de cotação
amount	string	Quantidade da negociação na moeda de base
side	string	A ponta executora da negociação (SELL ou BUY)
timestamp	number	Hora em que ordem foi executada
Obter dados de candlestick
Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "amount": 8.25709100,
            "closePrice": 62553.20,
            "count": 29,
            "highPrice": 62592.87,
            "lowPrice": 62553.20,
            "openPrice": 62554.23,
            "score": 1602501480,
            "symbol": "BTC_BRL",
            "vol": 516784.2504067500
        }
    ],
    "message": "Success"
}
Parâmetro de requisição
GET /v1/market/kline/history

Peso: 5
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
unit	true	string	ONE_MIN,FIVE_MIN, FIFTEEN_MIN,HALF_HOU,ONE_HOU,ONE_DAY,ONE_WEE,ONE_MON;
from	true	number	data de início Apenas 3000 históricos preservados em qualquer unidade de tempo
to	true	number	data de término Apenas 3000 históricos preservados em qualquer unidade de tempo
Detalhes de respots
Campo	Tipo	Detalhes
unit	string	Unidade de tempo de execução
amount	string	Quantidade de moedas negociadas
count	string	Quantidade de negociações concluídas
openPrice	string	Preço no início
closePrice	string	Preço no fim
highPrice	string	Preço maior
lowPrice	string	Preço menor
symbol	string	Símbolo da negociação
score	string	Marca temporal
vol	string	Volume de negociação
Ordens
Introdução de ordem
tipo de ordem(order.type)
LIMIT: ordem limitada
MARKET: ordem a mercado
STOP_LIMIT: A ordem será colocada em fila de espera ao preço limite só quando o preço de mercado atingir o preço de disparo.
STOP_MARKET: A ordem será colocada em fila de espera ao preço de mercado só quando o preço de mercado atingir o preço de disparo.
Operador de stop ordem(order.operator)
GTE: Igual ou superior a
LTE: Igual ou inferior a
Direção(order.side)
BUY: Compra
SELL: Venda
status da ordem(order.status)
SUBMITTED: A ordem foi submetida, mas não processada, ainda não entrou na fila de execução. O status da ordem está unfinished.
PROCESSING: A ordem foi submetida e está na fila de execução. O status da ordem está unfinished.
PARTIAL_FILLED: A ordem foi parcialmente negociada e está na fila de execução, esperando por mais negociações. O status da ordem está unfinished.
PARTIAL_CANCELED: A ordem tinha sido parcialmente negociada e foi cancelada pelo usuário. Não está na fila de execução. O status da ordem está finished.
PARTIAL_REJECTED: A ordem foi recusada pelo sistema depois de ter sido parcialmente negociada. Agora não está na fila de execução. O status da ordem está finished.
FILLED: A ordem foi completamente negociada. Não está na fila de execução. O status da ordem está finished.
CANCELED: A ordem foi cancelada pelo usuário antes de ser negociada. Não está na fila de execução. O status da ordem está finished.
REJECTED: A ordem foi recusada pelo sistema antes de ser negociada. Não está na fila de execução. O status da ordem está finished.
CANCELING: A ordem está sendo cancelada, mas ainda está na fila de execução. O status da ordem está unfinished.
Papel da ordem(order.role)
MAKER: Contribui liquidez
TAKER: Tira liquidez
Criar ordem limitada de compra
Abre uma ordem limitada de compra e a envia para livro de ofertas para sua execução.

Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "id": "633679992971251712",
        "clientOrderId": "client_order_id_123456",
        "symbol": "BTC_BRL",
        "type": "MARKET",
        "side": "SELL",
        "price": null,
        "averagePrice": "0",
        "amount": "0.123",
        "filledAmount": "0",
        "value": null,
        "filledValue": "0",
        "filledFee": "0",
        "stopPrice": null,
        "operator": null,
        "status": "REJECTED",
        "timestamp": 1565165945588
    },
    "message": "Success"
}
Caminho de requisição
POST /v1/orders/create

Peso: 5
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
clientOrderId	false	string	ID exclusivo do pedido personalizado pelo cliente, com até 30 caracteres no máximo.
symbol	true	string	Símbolo da negociação, como BTC_BRL
type	true	string	Tipo de ordem, informe: LIMIT
side	true	string	A ponta executora da ordem, informe: BUY
price	true	string	Preço de compra
amount	true	string	Quantidade da moeda de base, por exemplo, a quantidade de BTC na compra de BTC_BRL
value	true	string	Quantidade da moeda de cotação, por exemplo, a quantidade de BRL na compra de BTC_BRL
operator	true	string	Operador de stop ordem(para mais informações, veja a introdução de ordem)
stopPrice	true	string	Preço de disparo
Com base no tipo de pedido e no lado, são exigidos alguns parâmetros:

type + side	Parâmetros obrigatórios
LIMIT BUY	price,amount
LIMIT SELL	price,amount
MARKET BUY	value
MARKET SELL	amount
STOP_LIMIT BUY	price,amount,operator,stopPrice
STOP_LIMIT SELL	price,amount,operator,stopPrice
STOP_MARKET BUY	value,operator,stopPrice
STOP_MARKET SELL	amount,operator,stopPrice
Detalhes de resposta
Campo	Tipo	Detalhes
id	string	ID da ordem
clientOrderId	string	ID de pedido exclusivo personalizado pelo cliente
symbol	string	Símbolo da negociação
type	string	Tipo da ordem
side	string	A ponta executora da ordem
price	string	Preço unitário da ordem
averagePrice	string	Preço médio da ordem
amount	string	Quantidade da moeda de base
filledAmount	string	Quantidade executada da moeda de base
value	string	Quantidade da moeda de cotação
filledValue	string	Quantidade executada da moeda de cotação
filledFee	string	Taxa paga
status	string	Status da ordem(consultar introdução de ordem)
timestamp	number	Hora da criação da ordem
Pedido em lote
Crear novos pedidos em lote, com suporte para até 20 pedidos simultâneos.

Corpo de Resposta

{
    "code": "A10000",
    "data": [{
        "id": "633679992971251712",
        "clientOrderId": "client_order_id_123456",
        "symbol": "BTC_BRL",
        "type": "MARKET",
        "side": "SELL",
        "price": null,
        "averagePrice": "0",
        "amount": "0.123",
        "filledAmount": "0",
        "value": null,
        "filledValue": "0",
        "filledFee": "0",
        "stopPrice": null,
        "operator": null,
        "status": "REJECTED",
        "timestamp": 1565165945588
    }, {
        "clientOrderId": "client_order_id_123456",
        "code": "A10001",
        "message": "Params error"
    }],
    "message": "Success"
}
Caminho de requisição
POST /v1/orders/batch-create

Peso: 50
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
>clientOrderId	false	string	ID exclusivo do pedido personalizado pelo cliente, com até 30 caracteres no máximo.
>symbol	true	string	Símbolo da negociação, como BTC_BRL
>type	true	string	Tipo de ordem, informe: LIMIT
>side	true	string	A ponta executora da ordem, informe: BUY
>price	true	string	Preço de compra
>amount	true	string	Quantidade da moeda de base, por exemplo, a quantidade de BTC na compra de BTC_BRL
>value	true	string	Quantidade da moeda de cotação, por exemplo, a quantidade de BRL na compra de BTC_BRL
>operator	true	string	Operador de stop ordem(para mais informações, veja a introdução de ordem)
>stopPrice	true	string	Preço de disparo
Com base no tipo de pedido e no lado, são exigidos alguns parâmetros:

type + side	Parâmetros obrigatórios
LIMIT BUY	price,amount
LIMIT SELL	price,amount
MARKET BUY	value
MARKET SELL	amount
STOP_LIMIT BUY	price,amount,operator,stopPrice
STOP_LIMIT SELL	price,amount,operator,stopPrice
STOP_MARKET BUY	value,operator,stopPrice
STOP_MARKET SELL	amount,operator,stopPrice
Detalhes de resposta
Campo	Tipo	Detalhes
data	array	Lista de Pedidos
>id	string	ID da ordem
>clientOrderId	string	ID de pedido exclusivo personalizado pelo cliente
>symbol	string	Símbolo da negociação
>type	string	Tipo da ordem
>side	string	A ponta executora da ordem
>price	string	Preço unitário da ordem
>averagePrice	string	Preço médio da ordem
>amount	string	Quantidade da moeda de base
>filledAmount	string	Quantidade executada da moeda de base
>value	string	Quantidade da moeda de cotação
>filledValue	string	Quantidade executada da moeda de cotação
>filledFee	string	Taxa paga
>status	string	Status da ordem(consultar introdução de ordem)
>timestamp	number	Hora da criação da ordem
Cancelar ordem
Solicita o cancelamento de uma ordem.

 Este endpoint é apenas para solicitar o cancelamento de ordem. O resultado do cancelamento é disponível no endpoint `Get Order Details`.
Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "result": true
    },
    "message": "Success"
}
Caminho de requisição
POST /v1/orders/cancel

Peso: 1
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
id	false	string	ID da ordem
clientOrderId	false	string	ID de pedido exclusivo personalizado pelo cliente
Detalhes de resposta
Campo	Tipo	Detalhes
result	boolean	Resultado do cancelamento
Cancelar pedidos em lote com base no ID.
Pedido de cancelamento em lote submetido, suportando no máximo a submissão simultânea de 20 pedidos.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "id": "608695623247466496",
            "result": true,
            "code": "A10000",
            "message": "Success"
        },
        {
            "clientOrderId": "client_order_id_123457",
            "result": true,
            "code": "A10000",
            "message": "Success"
        },
        {
            "clientOrderId": "client_order_id_123458",
            "result": false,
            "code": "A30001",
            "message": "Order not found",
        }
    ],
    "message": "Success"
}
 Este endpoint é apenas para solicitar o cancelamento de ordem. O resultado do cancelamento é disponível no endpoint `Get Order Details`.
Caminho de requisição
POST /v1/orders/batch-cancel

Peso: 10
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
>id	true	string	ID da ordem
>clientOrderId	false	string	ID de pedido exclusivo personalizado pelo cliente
Detalhes de resposta
Campo	Tipo	Detalhes
data	array	Lista de Pedidos Cancelados
>id	string	ID da ordem
>clientOrderId	string	ID de pedido exclusivo personalizado pelo cliente
>result	boolean	Resultado do cancelamento
Cancelar a ordem de acordo com o par de negociação.
Cancelar o pedido enviado de acordo com o par de negociação.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "id": "608695623247466496",
            "clientOrderId": "client_order_id_123456",
            "result": true,
            "code": "A10000",
            "message": "Success"
        },
        {
            "id": "608695623247466497",
            "clientOrderId": "client_order_id_123457",
            "result": true,
            "code": "A10000",
            "message": "Success"
        }
    ],
    "message": "Success"
}
 Este endpoint é apenas para solicitar o cancelamento de ordem. O resultado do cancelamento é disponível no endpoint `Get Order Details`.
Caminho de requisição
POST /v1/orders/cancel-by-symbol

Peso: 10
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação, como BTC_BRL
Detalhes de resposta
Campo	Tipo	Detalhes
data	array	Lista de Pedidos Cancelados
>id	string	ID da ordem
>clientOrderId	string	ID de pedido exclusivo personalizado pelo cliente
>result	boolean	Resultado do cancelamento
Conferir detalhes de ordens
Retorna os detalhes atualizados de uma ordem. Ordens criadas via API não serão encontradas depois de duas horas após seu cancelamento.

Corpo de Resposta

{
    "code": "A10000",
    "data": {
        "id": "608695623247466496",
        "clientOrderId": "client_order_id_123456",
        "symbol": "BTC_BRL",
        "type": "MARKET",
        "side": "SELL",
        "price": null,
        "averagePrice": "0",
        "amount": "0.123",
        "filledAmount": "0",
        "value": null,
        "filledValue": "0",
        "filledFee": "0",
        "stopPrice": null,
        "operator": null,
        "status": "REJECTED",
        "timestamp": 1565165945588
    },
    "message": "Success"
}
Caminho de requisição
GET /v1/orders/get

Peso: 1
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
id	false	string	ID da ordem
clientOrderId	false	string	ID de pedido exclusivo personalizado pelo cliente
Detalhes de resposta
Campo	Tipo	Detalhes
id	string	ID da ordem
symbol	string	Símbolo da negociação
type	string	Tipo de ordem(consultar introdução de ordem)
side	string	A ponta executora da ordem, opções: BUY or SELL
price	string	Preço unitário de ordem
averagePrice	string	Preço médio da ordem
amount	string	Quantidade da moeda de base
filledAmount	string	Quantidade executada da moeda de base
value	string	Quantidade da moeda de cotação
filledValue	string	Quantidade executada da moeda de cotação
filledFee	string	Taxa paga
status	string	Status da ordem(consultar introdução de ordem)
timestamp	number	Hora da criação da ordem
Conferir histórico de ordens
Retorna o histório de ordens de acordo com o filtro informado. Ordens criadas via API não serão encontradas depois de duas horas após seu cancelamento.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "id": "608695678650028032",
            "clientOrderId": "client_order_id_123456",
            "symbol": "BTC_BRL",
            "type": "MARKET",
            "side": "SELL",
            "price": null,
            "averagePrice": "0",
            "amount": "0.123",
            "filledAmount": "0",
            "value": null,
            "filledValue": "0",
            "filledFee": "0",
            "stopPrice": null,
            "operator": null,
            "status": "REJECTED",
            "timestamp": 1565165958796
        },
        {
            "id": "608695623247466496",
            "clientOrderId": "client_order_id_123457",
            "symbol": "BTC_BRL",
            "type": "MARKET",
            "side": "SELL",
            "price": null,
            "averagePrice": "0",
            "amount": "0.123",
            "filledAmount": "0",
            "value": null,
            "filledValue": "0",
            "filledFee": "0",
            "stopPrice": null,
            "operator": null,
            "status": "REJECTED",
            "timestamp": 1565165945588
        }
    ],
    "message": "Success"
}
Caminho de requisição
GET /v1/orders/list

Peso: 10
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	false	string	Símbolo da negociação, como BTC_BRL
status	false	string	Você pode encontrar as opções dos status de ordem na introdução. Use vírgula para separar vários status. Você pode pesquisar “FINISHED” para encontrar ordens não concluídas, e pesquisar “UNFINISHED” para encontrar ordens concluídas.
fromId	false	string	Ordem de início
toId	false	string	Ordem de término
fromTimestamp	false	number	Data de início, considerando a hora da criação da ordem em milissegundos
toTimestamp	false	number	Data de término, considerando a hora da criação da ordem em milissegundos
limit	false	string	O número de ordens a retornar, default 100, máx 100
Detalhes de resposta
Campo	Tipo	Detalhes
id	string	ID da ordem
symbol	string	Símbolo da negociação
type	string	Tipo de ordem
side	string	A ponta executora da ordem
price	string	Preço unitário de ordem
averagePrice	string	Preço médio da ordem
amount	string	Quantidade da moeda de base
filledAmount	string	Quantidade executada da moeda de base
value	string	Quantidade da moeda de cotação
filledValue	string	Quantidade executada da moeda de cotação
filledFee	string	Taxa paga
status	string	Status da ordem(consultar introdução de ordem)
timestamp	number	Hora da criação da ordem
Conferir detalhes de execução de ordens
Retorna o resultado da execução de uma ordem.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "id": "608717046691139584",
            "orderId": "608716957545402368",
            "symbol": "BTC_BRL",
            "side": "BUY",
            "amount": "0.0988",
            "price": "45514.76",
            "fee": "0.0000988 BTC",
            "feeAmount": "0.0000988",
            "feeCurrency": "BTC",
            "role": "MAKER",
            "timestamp": 1565171053345
        },
        {
            "id": "608717065729085441",
            "orderId": "608716957545402368",
            "symbol": "BTC_BRL",
            "side": "BUY",
            "amount": "0.0242",
            "price": "45514.76",
            "fee": "0.0000242 BTC",
            "feeAmount": "0.0000988",
            "feeCurrency": "BTC",
            "role": "MAKER",
            "timestamp": 1565171057882
        }
    ],
    "message": "Success"
}
Caminho de requisição
GET /v1/orders/fills

Peso: 10
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
orderId	true	string	ID da ordem
symbol	false	string	Símbolo da negociação, como BTC_BRL
fromId	false	string	Ordem de início
toId	false	string	Ordem de término
fromTimestamp	false	number	Data de início, considerando a hora da execução da ordem em milissegundos
toTimestamp	false	number	Data de término, considerando a hora da execução da ordem em milissegundos
limit	false	string	O número de ordens a retornar, default 100, máx 100
Detalhes de resposta
Campo	Tipo	Detalhes
id	string	ID da execução de ordem
orderId	string	ID da ordem
symbol	string	Símbolo da negociação
side	string	A ponta executora da ordem(consultar introdução de ordem)
price	string	Preço executado
amount	string	Quantidade executada
fee	string	Taxa paga
feeCurrency	string	Moeda de taxa
feeAmount	string	Quantidade de moeda de taxa
role	string	Papel na execução(consultar introdução de ordem)
fromTimestamp	false	number
Conta
Obter saldo da conta
Retorna os saldos das moedas da sua conta.

Corpo de Resposta

{
    "code": "A10000",
    "data": [
        {
            "available": "1.23",
            "balance": "0.23",
            "currency": "BTC",
            "hold": "1"
        }
    ],
    "message": "Success"
}
Caminho de requisição
GET /v1/account/getBalance

Peso: 1
Parâmetro de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
Campo	Tipo	Detalhes
currency	string	A moeda do saldo
balance	string	O saldo da moeda
hold	string	O saldo em ordens
available	string	O saldo disponível
Lista de sub-conta
Retorna a lista de todas as subcontas da conta principal

Corpo de Resposta

{
    "code": "A10000",
    "data": [{
        "subId": "CA648856083527372800",
        "state": "Normal",
        "subAccount": "003",
        "subIdentify": "003"
    }],
    "message": "Success"
}
Caminho de requisição
GET /v1/account/subs

Peso: 1
Parâmetro de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
Campo	Tipo	Detalhes
subId	string	ID da subconta
state	string	Status da subconta, Normal/Frozen (normal ou bloqueada)
subAccount	string	Nome da subconta
subIdentify	string	Descrição da subconta
Saldo da sub-conta
Retorna o saldo da subconta

Corpo de Resposta

{
    "code":"A10000",
    "data":[
        {
            "balance":"7.22",
            "currency":"BTC"
        }
    ],
    "message":"Success"
}
Caminho de requisição
GET /v1/account/subs/balance

Peso: 1
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
subId	ture	string	ID da subconta
Detalhes de resposta
Campo	Tipo	Detalhes
balance	string	Saldo da subconta
currency	string	Moeda do saldo
Histórico de transferência da sub-conta
Retorna o histórico de transferências entre conta principal e subcontas

Corpo de Resposta

{
    "code": "A10000",
    "data": [{
        "subId": "CA648855702269333504",
        "amount": "103.22",
        "currency": "BRL",
        "state": "success",
        "type": "master-transfer-out"
    }, {
        "subId": "CA648855702269333504",
        "amount": "3.5",
        "currency": "BRL",
        "state": "success",
        "type": "master-transfer-in"
    }],
    "message": "Success"
}
Caminho de requisição
GET /v1/account/subs/transfer/record

Peso: 10
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
subId	ture	string	ID da subconta
Detalhes de resposta
Campo	Tipo	Detalhes
subId	string	ID da subconta
amount	string	Quantidade transferida
currency	string	Moeda da transferência
state	string	Status da transferência: success/fail (sucesso/falha)
type	string	Tipo: master-transfer-in (transferido para conta principal) ou master-transfer-out (transferido da conta principal)
Transferência da sub-conta
Você pode utilizar este endpoint para transferir ativos entre conta principal e subcontas

Corpo de Resposta

{
  "code":"A10000",
  "message":"Success",
  "data":40
}
Caminho de requisição
POST /v1/account/subs/transfer

Peso: 5
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
subId	true	string	ID da subconta
currency	true	string	Moeda da transferência
transferAmount	true	string	Quantidade da transferência
transferType	true	string	Tipo，master-transfer-in ou master-transfer-out
Detalhes de resposta
O campo "data" retorna o ID da transferência realizada.

Carteira
Registros de depósito e saque de carteira
The endpoint returns the records of deposits and withdraws.

Corpo de Resposta

{
    "code": "A10000",
    "data": [{
        "id": "DR562339304588709888",
        "type": "COIN_IN",
        "currency": "XLM",
        "chain": "XLM",
        "address": "GCUTK7KHPJC3ZQJ3OMWWFHAK2OXIBRD4LNZQRCCOVE7A2XOPP2K5PU5Q",
        "addressTag": "1000009",
        "amount": 1.0,
        "state": "SUCCESS",
        "txHash": "39210645748822f8d4ce673c7559aa6622e6e9cdd7073bc0fcae14b1edfda5f4",
        "createdAt": 1554113737000,
        "updatedAt": 1601371273000
    }...],
    "message": "Success"
}
Caminho de requisição
GET /v1/wallet/query/deposit-withdraw

Peso: 10
Parâmetro de requisição
Campo	Tipo	Mandatório	Detalhes	Valor padrão
currency	string	false	The currency code. e.g. BTC	NA
type	string	false	default record type to search	coin_in and coin_out
direct	string	false	the order of records,e.g. asc or desc	asc
size	int	false	the number of iterms to return	100
start	string	false	the id of record,	NA
Detalhes de resposta
Campo	Tipo	Detalhes
id	string	the id of record
type	string	the type of record
currency	string	the currency code of record
txHash	string	the txid of chain
address	string	the dst address of txHash
addressTag	string	the tag of txHash
chain	string	Block chain name,internal means transfer through novadax inside rather than chain
amount	decimal	the amount of txHash
state	string	the state of record
createdAt	long	The timestamp in milliseconds for the transfer creation
updatedAt	long	The timestamp in milliseconds for the transfer's latest update
List of possible record state
State	Detalhes
Pending	the record is wait broadcast to chain
x/M confirming	the comfirming state of tx,the M is total confirmings needed
SUCCESS	the record is success full
FAIL	the record failed
Sacar criptomoedas
 Esse endpoint é utilizado para sacar criptomoedas e está temporariamente disponível apenas para clientes no whitelist. Você pode solicitar sua inclusão com o time de suporte. Os limites e taxas são as mesmas aplicadas na versão web.
Corpo de Resposta

{
  "code":"A10000",
  "data": "DR123",
  "message":"Success"
}
Caminho de requisição
POST /v1/account/withdraw/coin

Peso: 600
Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
code	ture	string	Símbolo da moeda, como BTC
amount	true	string	Valor do saque
wallet	true	string	Endereço de carteira de destino
chainAlias	true	string	Endereço de carteira de destino apelido de cadeia
tag	false	string	Tag, requerido ao enviar XLM, XRP e EOS
Detalhes de resposta
O campo data retorna o id do saque.

Pesquisa em rede Chain
Caminho de requisição
GET /crypto/chain/{code}

Peso: 5
Parâmetro de requisição
param name	param type	param note
code	String	Código da conta,default value is "ALL"
Detalhes de resposta
param name	param type	param note
accountCode	String	Código da conta
accountType	String	Tipo da conta: DIGITAL, LEGAL
accountPrecision	Integer	Precisão da conta
accountOrder	Integer	Ordem da conta
accountState	Integer	Estado da conta. 1: em uso; 2; não em uso
tokens	List	Lista da rede de cripto
List of tokens

parame name	param type	param note
codeAccount	String	Código da conta
chainAlias	String	Apelido da cadeia de cripto, usado para enviar cripto
chainName	String	Nome da cadeia de cripto, usado só para ler
mainAddr	String	Endereço principal par criptos com memo. O valor default é nulo
useMemo	Integer	Usar memo ou não. 1: usado; 0: não usado
useDynamicSendFee	String	Usar taxas dinâmicas para envio. 1: usado; 0: não usado
minConf	Integer	Confirmações mínimas da cadeia
useFirst	Integer	A cadeia default será escolhida quando "chainAlias" for nulo em API
state	Integer	A cadeia está em uso. 1: em uso; 0: não em uso
chainURL	String	URL da cadeia
chainAddressURL	String	URL do endereço da cadeia
chainHashURL	String	URL do hash da cadeia
officialURL	String	URL da cadeia oficial
WebSocket
Acesso
NovaDAX WebSocket API baseia-se em Socket.io. Você pode encontrar mais informações sobre Socket.io em seu site oficial.

Endereço
wss://api.novadax.com

// Socket.io exemplo de estabelecer conexão
const io = require("socket.io-client");

const socket = io("wss://api.novadax.com", {
transports: ['websocket']
});

// Socket.io exemplo de subscrição
socket.emit("SUBSCRIBE", ["MARKET.BTC_USDT.TICKER", "MARKET.BTC_USDT.TRADE"])
socket.on("MARKET.BTC_USDT.TICKER", (ticker) => {
    console.log(ticker)
})
socket.on("MARKET.BTC_USDT.TRADE", (trade) => {
    console.log(trade)
})

// Socket.io exemplo de cancelar subscrição
socket.emit("UNSUBSCRIBE", ["MARKET.BTC_USDT.DEPTH.LEVEL0"])
Limite
Suporta apenas websocket transports de Socket.io
Um IP só pode estabelecer 10 conexões WebSocket
Subscrever tópicos
Ao subscrever um tópico, você receberá todas as notificações relacionadas com ele. Formato de subscrição:

socket.emit("SUBSCRIBE", ["XXX"])

Cancelar subscrição
Depois de subscrever um tópico, se você não quiser receber notificações sobre ele, pode cancelar a subscrição. Formato de cancelar a subscrição:

socket.emit("UNSUBSCRIBE", ["XXX"])

Subscrever dados de ticker de um par de negociação específico
Após a subscrição, o sistema enviará dados de ticker de todos os pares de negociação uma vez por segundo.

Valor de retorno

[
  {
      "ask": "34708.15",
      "baseVolume24h": "34.08241488",
      "bid": "34621.74",
      "high24h": "35079.77",
      "lastPrice": "34669.81",
      "low24h": "34330.64",
      "open24h": "34492.08",
      "quoteVolume24h": "1182480.09502814",
      "symbol": "BTC_BRL",
      "timestamp": 1571112216346
  }
]
Tópico de subscrição
MARKET.TICKERS

Parâmetros de requisição
Nenhum parâmetro é necessário para este endpoint.

Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo da negociação
lastPrice	string	Preço unitário da última negociação
bid	string	Maior preço de oferta de compra das últimas 24 horas
ask	string	Menor preço de oferta de venda das últimas 24 horas
open24h	string	Preço unitário de abertura de negociação das últimas 24 horas
high24h	string	Maior preço unitário de negociação das últimas 24 horas
low24h	string	Menor preço unitário de negociação das últimas 24 horas
baseVolume24h	string	Volume de negociação na moeda de base das últimas 24 horas
quoteVolume24h	string	Volume de negociação na moeda de cotação das últimas 24 horas
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Subscrever dados de ticker de um único par de negociação
Após a subscrição, o sistema enviará dados de ticker do par de negociação definido uma vez por segundo.

Valor de retorno

{
    "ask": "34708.15",
    "baseVolume24h": "34.08241488",
    "bid": "34621.74",
    "high24h": "35079.77",
    "lastPrice": "34669.81",
    "low24h": "34330.64",
    "open24h": "34492.08",
    "quoteVolume24h": "1182480.09502814",
    "symbol": "BTC_BRL",
    "timestamp": 1571112216346
}
Tópico de subscrição
MARKET.{{symbol}}.TICKER

Parâmetros de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
Detalhes de resposta
Campo	Tipo	Detalhes
symbol	string	Símbolo de negociação
lastPrice	string	Preço unitário da última negociação
bid	string	Maior preço de oferta de compra das últimas 24 horas
ask	string	Menor preço de oferta de venda das últimas 24 horas
open24h	string	Preço unitário de abertura de negociação das últimas 24 horas
high24h	string	Maior preço unitário de negociação das últimas 24 horas
low24h	string	Menor preço unitário de negociação das últimas 24 horas
baseVolume24h	string	Volume de negociação na moeda de base das últimas 24 horas
quoteVolume24h	string	Volume de negociação na moeda de cotação das últimas 24 horas
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Subscrever dados de profundidade
Após a subscrição, o sistema enviará dados de profundidade dos paress de negociação definidos uma vez por segundo.

Valor de retorno

{
    "asks": [
        ["43687.16", "0.5194"],
        ["43687.2", "1.3129"]
    ],
    "bids": [
        ["43657.57", "0.6135"],
        ["43657.46", "0.0559"]
    ],
    "timestamp": 1565057338020
}
Tópico de subscrição
MARKET.{{symbol}}.DEPTH.LEVEL0

Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
limit	false	number	O número de compras e vendas a retornar; máximo 20
Detalhes de resposta
Campo	Tipo	Detalhes
asks	array	Lista de ofertas de venda
asks[][0]	string	Preço de venda
asks[][1]	string	Quantidade de venda
bids	array	Lista de ofertas de compra
bids[][0]	string	Preço de compra
bids[][1]	string	Quantidade de compra
timestamp	number	A hora atual do sistema ajustada para o horário UTC
Subscrever dados de execução de ordens
Após a subscrição, o sistema enviará notificações sobre as ordens recém-executadas.

Valor de retorno

[
    {
        "price": "43657.57",
        "amount": "1",
        "side": "SELL",
        "timestamp": 1565007823401
    },
    {
        "price": "43687.16",
        "amount": "0.071",
        "side": "BUY",
        "timestamp": 1565007198261
    }
]
Tópico de subscrição
MARKET.{{symbol}}.TRADE

Parâmetro de requisição
Campo	Mandatório	Tipo	Detalhes
symbol	true	string	Símbolo da negociação
Detalhes de resposta
Campo	Tipo	Detalhes
price	string	Preço unitário da negociação na moeda de cotação
amount	string	Quantidade da negociação na moeda de base
side	string	A ponta executora da negociação (SELL ou BUY)
timestamp	number	Hora em que ordem foi executada