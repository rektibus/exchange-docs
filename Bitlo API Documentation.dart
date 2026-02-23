Bitlo API Documentation
General Information
API Base URL (v1): https://api.bitlo.com

API Base URL (public api): https://api4.bitlo.com

API Base URL (public api): https://api3.bitlo.com

For GET endpoints, parameters must be sent as a query string.
For POST endpoints, parameters must be sent as a JSON object.
All endpoints return a JSON object.
You can use pair symbol parameter in this format: BTC-TRY
Authentication
All Private API endpoints (which are related to a user account) require authentication.

Below are the required parameters for authenticating a request:

x-pubkey: API Public Key
x-nonce: Nonce
x-signature: Signature
Note

Please reach out to Customer Support or send an email to destek@bitlo.com for receiving instructions on how to generate your API key.

Nonce

Nonce is a regular integer number. It must be current timestamp in milliseconds.

It is a must to sync your current time with API server time which is in miliseconds format. Our servers are using UTC timezone. You can check the server time here.

Signature

Signature is a HMAC-SHA256 encoded message. The HMAC-SHA256 code must be generated using a private key that contains a timestamp as nonce and your API key.


C#
PHP
Python
GoLang
Node.js
Ruby

var apiKey = YOUR_API_PUBLIC_KEY;
var apiSecret = YOUR_API_SECRET;
var nonce = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliSeconds();
string message = apiKey + nonce;
using (HMACSHA256 hmac = new HMACSHA256(Convert.FromBase64String(apiSecret)))
{
    byte[] signatureBytes = hmac.ComputeHash(Encoding.UTF8.GetBytes(message));
    string X_Signature = Convert.ToBase64String(signatureBytes));
}

Public Endpoints
All Public Endpoints
Endpoint Name	Path
Config	https://api4.bitlo.com/config
Ticker-All	https://api4.bitlo.com/market/ticker/all
Ticker-Currency	https://api4.bitlo.com/market/market-ticker
Orderbook	https://api4.bitlo.com/market/orderbook
Fills	https://api4.bitlo.com/market/orderbook/fills
Kline Data	https://api3.bitlo.com/api/v3/klines/history
Config
This endpoint provides information about all available assets, markets, market categories and fee schedules for Bitlo Crypto Exchange.

Sample Response: (partial representation)


{
  "markets": [
    {
      "code": "BTC-TRY",
      "name": "BTC/TRY",
      "baseAssetCode": "BTC",
      "baseAssetName": "Bitcoin",
      "baseAssetScale": 8,
      "quoteAssetCode": "TRY",
      "quoteAssetName": "Türk Lirası",
      "quoteAssetScale": 2,
      "tradingEnabled": true,
      "orderCancelEnabled": true,
      "mobileTradingEnabled": true,
      "mobileOrderCancelEnabled": true,
      "minimumPrice": "500000",
      "maximumPrice": "4000000",
      "priceStep": "1",
      "priceStepCount": "0",
      "minimumQuantity": "0.000001",
      "maximumQuantity": "2",
      "quantityStep": "0.000001",
      "quantityStepCount": "6",
      "minimumNotionalValue": "0.99",
      "maximumOrderCountPerCustomer": 20,
      "category": [
        8,
        11,
        15
      ],
      "keyWords": "bitkoin koin,",
      "isNew": 0,
      "stopEnabled": 1,
      "marketOrderEnabled": 1,
      "limitOrderEnabled": 1,
      "chainOrderEnabled": 1
    }
  ],
  "assets": [
    {
      "code": "BTC",
      "name": "Bitcoin",
      "type": "CRYPTO",
      "scale": 8,
      "depositEnabled": true,
      "withdrawEnabled": true,
      "dailyWithdrawQuantityLimit": "10",
      "monthlyWithdrawQuantityLimit": "100",
      "assetNetworks": [
        {
          "code": "BTC",
          "name": "Bitcoin",
          "depositEnabled": true,
          "depositRequestRequired": false,
          "depositRequestUrlPresent": false,
          "minimumDepositQuantity": "0.0001",
          "maximumDepositRequestQuantity": "0",
          "withdrawEnabled": true,
          "minimumWithdrawQuantity": "0.003",
          "withdrawFee": "0.002"
        }
      ],
      "keyWords": "bitkoin koin"
    }
  ],
  "settings": {
    "api1interval": 8000,
    "api2interval": 2000,
    "mobileTradingEnabled": true,
    "mobileOrderCancelEnabled": true,
    "androidVersion": 23112021,
    "iosVersion": 23112021
  },
  "marketCategories": [
    {
      "id": 1,
      "name": "Sepet",
      "title": "Kripto Para Sepetleri - Sepet Token",
      "slug": "sepet",
      "enabled": "true",
      "priority": 11,
      "is_visible": true
    },
    {
      "id": 7,
      "name": "Stabil",
      "title": "Stablecoin Listesi ve Fiyatları",
      "slug": "stable",
      "enabled": "true",
      "priority": 20,
      "is_visible": true
    },
    {
      "id": 3,
      "name": "DeFi",
      "title": "DeFi Coinleri ve DeFi Tokenlari Listesi",
      "slug": "defi",
      "enabled": "true",
      "priority": 90,
      "is_visible": false
    },
    {
      "id": 8,
      "name": "Layer 1",
      "title": "Layer 1 Coinleri Listesi ve Fiyatları",
      "slug": "layer-1",
      "enabled": "true",
      "priority": 100,
      "is_visible": false
    }
  ],
  "exchangeFeeSchedule": [
    {
      "minimumVolume": 0,
      "maximumVolume": 250000,
      "makerFee": 0.0035,
      "takerFee": 0.0035
    },
    {
      "minimumVolume": 250000,
      "maximumVolume": 1000000,
      "makerFee": 0.0025,
      "takerFee": 0.0035
    }
  ]
}
Ticker-All
This endpoint provides information about the last trade (tick), best bid/ask, last 24 hours lowest/highest quotes and volume data for all markets.

Sample Response: (partial representation)


[
    {
        "marketCode": "1INCH-TRY",
        "currentQuote": "12.19",
        "change24h": "-0.52",
        "change24hPercent": "-4.09",
        "highestQuote24h": "12.72",
        "lowestQuote24h": "12.07",
        "weightedAverage24h": "12.30",
        "volume24h": "11149.86193168",
        "notionalVolume24h": "137216.60",
        "ask": "12.24",
        "bid": "12.14"
    }
]
Ticker-Currency
This endpoint provides information about the last trade (tick), best bid/ask, last 24 hours lowest/highest quotes and volume data for the given market.

Parameters

Name	Type	Required	Example Value
market	query string	yes	AAVE-TRY
Sample Request:

https://api4.bitlo.com/market/market-ticker?market=AAVE-TRY

Sample Response:


{
    "marketCode": "AAVE-TRY",
    "currentQuote": "2607.00",
    "change24h": "-51.00",
    "change24hPercent": "-1.92",
    "highestQuote24h": "2656.00",
    "lowestQuote24h": "2586.00",
    "weightedAverage24h": "2612.66",
    "volume24h": "54.20858677",
    "notionalVolume24h": "141628.92",
    "ask": "2621.00",
    "bid": "2599.00"
}
Orderbook
This endpoint returns bids and asks for the given market (first 20 records only for each).

Parameters

Name	Type	Required	Example Value
market	query string	yes	BTC-TRY
Sample Request:

https://api4.bitlo.com/market/orderbook?market=BTC-TRY

Sample Response: (partial representation)


{
  "sequenceId": 18899301,
  "bids": [
    {
      "0": "1315051.00",
      "1": "0.09007100"
    },
    {
      "0": "1314999.00",
      "1": "0.00007600"
    },
    {
      "0": "1314891.00",
      "1": "0.09010000"
    }
  ],
  "asks": [
    {
      "0": "1315586.00",
      "1": "0.20306500"
    },
    {
      "0": "1316502.00",
      "1": "0.11864500"
    },
    {
      "0": "1317796.00",
      "1": "0.15369700"
    }
  ]
}
Fills
This endpoint returns the list of latest trades for the given market (last 12 records only).

Parameters

Name	Type	Required	Example Value
market	query string	yes	XRP-TRY
Sample Request:

https://api4.bitlo.com/market/orderbook/fills?market=XRP-TRY

Sample Response: (partial representation)


{
  "fills": [
    {
      "marketCode": "XRP-TRY",
      "buyOrderId": "del",
      "buyCustomerId": "del",
      "sellOrderId": "del",
      "sellCustomerId": "del",
      "price": "15.54",
      "quantity": "28.63000000",
      "value": "444.9102000000",
      "buyFee": "0.00",
      "sellFee": "0.00",
      "side": "BUY",
      "timestamp": "2024-02-04T22:58:46.389Z"
    },
    {
      "marketCode": "XRP-TRY",
      "buyOrderId": "del",
      "buyCustomerId": "del",
      "sellOrderId": "del",
      "sellCustomerId": "del",
      "price": "15.54",
      "quantity": "6.75000000",
      "value": "104.8950000000",
      "buyFee": "0.00",
      "sellFee": "0.00",
      "side": "BUY",
      "timestamp": "2024-02-04T22:55:58.673Z"
    }
  ]
}
Kline Data
This endpoint returns Kline candlestick bars for the given symbol.

Parameters

Name	Type	Required	Example Value
symbol	query string	yes	BTC-TRY
resolution	query string	yes	15, 60, 240, 1D, 1W
from	query string	yes	1707070000
to	query string	yes	1707088000
from and to parameter values must be Unix time in seconds.
Sample Request:

https://api3.bitlo.com/api/v3/klines/history?symbol=BTC-TRY&resolution=60&from=1707070000&to=1707088000

Sample Response: (partial representation)


{
  "s": "ok",
  "t": [
    1707069600
  ],
  "h": [
    1324153
  ],
  "l": [
    1318471
  ],
  "o": [
    1322601
  ],
  "c": [
    1319812
  ],
  "v": [
    0
  ]
}
Flag	Description
t	Timestamp
h	High
o	Open
l	Low
c	Close
v	Volume
Private Endpoints
All Private Endpoints
Endpoint Name	Path
Summary	https://api.bitlo.com/customer/account/summary
Open Orders	https://api.bitlo.com/market/order/open
All Orders	https://api.bitlo.com/market/order/all
Submit Order	https://api.bitlo.com/market/order
Cancel Order	https://api.bitlo.com/market/cancel
Summary
This endpoint returns the account summary (all asset balances) for the customer.

This endpoint requires authentication. Please check Authentication section for details.

Sample Response: (partial representation)


{
  "totalBalanceTry": 25487.74707706,
  "totalHoldTry": 20484.53455,
  "totalAvailableTry": 5003.21252706,
  "totalBalanceUsdt": 823.510164,
  "totalHoldUsdt": 661.85895152,
  "totalAvailableUsdt": 161.65121246,
  "balances": [
    {
      "asset": "RSR",
      "balance": "124562.50000000",
      "balanceTry": "8719.37500000",
      "balanceUsdt": "281.72455573",
      "available": "0.50000000",
      "hold": "124562.00000000",
      "availableTry": "0.03500000",
      "availableUsdt": "0.00113085",
      "holdTry": "8719.34000000",
      "holdUsdt": "281.72342487",
      "assetPrice": "0.07"
    },
    {
      "asset": "LTC",
      "balance": "2.18602205",
      "balanceTry": "4509.76348915",
      "balanceUsdt": "145.71125974",
      "available": "0.00002205",
      "hold": "2.18600000",
      "availableTry": "0.04548915",
      "availableUsdt": "0.00146976",
      "holdTry": "4509.71800000",
      "holdUsdt": "145.70978998",
      "assetPrice": "2063.0"
    }    
  ],
  "promotions": []
}
Open Orders
This endpoint lists current open orders for the customer. If an order is no longer open or it's settled, then it will no longer appear in the response. If market parameter is provided, only open orders for the given market is returned. Otherwise, all open orders will be returned.

This endpoint requires authentication. Please check Authentication section for details.

Parameters

Name	Type	Required	Example Value
market	query string	no	FTT-TRY
page	query string	no	0 (page numbers start from zero)
size	query string	no	5 (number of records per page)
Sample Request:

https://api.bitlo.com/market/order/open?market=FTT-TRY&page=0&size=5

Sample Response:


{
    "orders": [
        {
            "id": "xxxxxxxx",
            "customerId": "yyyyyy",
            "market": "FTT-TRY",
            "type": "LIMIT",
            "side": "SELL",
            "timeInForce": "GTC",
            "price": "76.00",
            "funds": "7012.3680000000",
            "quantity": "92.26800000",
            "executedValue": "0.0000000000",
            "executedQuantity": "0.00000000",
            "executedFees": "0",
            "remainingQuantity": "92.26800000",
            "remainingFunds": "7012.3680000000",
            "fillQuantity": "0.00000000",
            "fillValue": "0.0000000000",
            "fillAveragePrice": "0",
            "status": "OPEN",
            "created": "2024-02-01T08:10:03.215166Z",
            "settled": null,
            "updated": "2024-02-01T08:10:03.237Z",
            "done": null,
            "stopAmount": "0.00",
            "groupId": "0",
            "marketOrderId": "0",
            "title": "",
            "description": ""
        }
    ],
    "pageable": {
        "page": 0,
        "size": 5,
        "totalCount": 5
    }
}
All Orders
This endpoint lists all orders (open, partially filled, filled or cancelled) for the customer. If market parameter is provided, only all orders for the given market is returned. Otherwise, all orders will be returned.

This endpoint requires authentication. Please check Authentication section for details.

Parameters

Name	Type	Required	Example Value
market	query string	no	RSR-TRY
page	query string	no	0 (page numbers start from zero)
size	query string	no	5 (number of records per page)
Sample Request:

https://api.bitlo.com/market/order/all?market=RSR-TRY&page=0&size=5

Sample Response:


{
    "orders": [
        {
            "id": "xxxxxxxx",
            "customerId": "yyyyyy",
            "market": "RSR-TRY",
            "type": "LIMIT",
            "side": "SELL",
            "timeInForce": "GTC",
            "price": "0.09",
            "funds": "11210.5800000000",
            "quantity": "124562.00000000",
            "executedValue": "0.0000000000",
            "executedQuantity": "0.00000000",
            "executedFees": "0",
            "remainingQuantity": "124562.00000000",
            "remainingFunds": "11210.5800000000",
            "fillQuantity": "0.00000000",
            "fillValue": "0.0000000000",
            "fillAveragePrice": "0",
            "status": "OPEN",
            "created": "2024-01-12T23:38:41.926447Z",
            "settled": null,
            "updated": "2024-01-12T23:38:41.942Z",
            "done": null,
            "stopAmount": "0.00",
            "groupId": "0",
            "marketOrderId": "0",
            "title": "",
            "description": ""
        },
        {
            "id": "zzzzzzzz",
            "customerId": "yyyyyy",
            "market": "RSR-TRY",
            "type": "LIMIT",
            "side": "BUY",
            "timeInForce": "GTC",
            "price": "0.08",
            "funds": "10000.0000000000",
            "quantity": "125000.00000000",
            "executedValue": "10000.0000000000",
            "executedQuantity": "125000.00000000",
            "executedFees": "437.500000000000",
            "remainingQuantity": "0.00000000",
            "remainingFunds": "0.0000000000",
            "fillQuantity": "125000.00000000",
            "fillValue": "10000.0000000000",
            "fillAveragePrice": "0.08000000",
            "status": "FILLED",
            "created": "2024-01-12T06:35:18.005326Z",
            "settled": "2024-01-12T22:27:01.900Z",
            "updated": "2024-01-12T22:27:01.898Z",
            "done": "2024-01-12T22:27:01.898Z",
            "stopAmount": "0.00",
            "groupId": "0",
            "marketOrderId": "0",
            "title": "",
            "description": ""
        }
    ],
    "pageable": {
        "page": 0,
        "size": 5,
        "totalCount": 5
    }
}
Submit Order
This endpoint creates an order. You need to send request with [POST] method. Returns the order object if it's successfully created.

This endpoint requires authentication. Please check Authentication section for details.

Parameters

Name	Type	Required	Example Value
market	body / json	yes	BTC-TRY
side	body / json	yes	BUY, SELL
type	body / json	yes	MARKET, LIMIT, CANCEL, STOP_LIMIT, CHAIN_ORDER, AUTOSAVING_ORDER
timeInForce	body / json	yes	GTC (Good Til Cancelled), FOK (Fill or Kill), IOC (Immediate or Cancel)
price	body / json	no	1200000
quantity	body / json	no	0.00001
stopLimit	body / json	no	1100000
funds	body / json	no	100
Sample Request (Limit Order):


{
  "quantity":"0.00001",
  "price":"1200000",
  "market":"BTC-TRY",
  "side":"BUY",
  "timeInForce":"GTC",
  "stopLimit":"",
  "type":"LIMIT"
}
Sample Request (Market Order):

{
  "funds":"5",
  "market":"BTC-TRY",
  "side":"BUY",
  "timeInForce":"GTC",
  "type":"MARKET"
}
Sample Request (Stop Limit Order):


{
  "quantity":"0.001",
  "price":"1150000",
  "market":"BTC-TRY",
  "side":"BUY",
  "timeInForce":"GTC",
  "stopLimit":"1180000",
  "type":"STOP_LIMIT"
}
Sample Response:


{
    "order": {
        "id": "xxxxxxxx",
        "customerId": "yyyyyy",
        "market": "BTC-TRY",
        "type": "STOP_LIMIT",
        "side": "BUY",
        "timeInForce": "GTC",
        "price": "1150000.00",
        "funds": "1150.0000000000",
        "quantity": "0.00100000",
        "executedValue": "0",
        "executedQuantity": "0",
        "executedFees": "0",
        "remainingQuantity": "0.00100000",
        "remainingFunds": "0",
        "fillQuantity": "0",
        "fillValue": "0",
        "fillAveragePrice": "0",
        "status": "OPEN",
        "created": "2024-02-05T08:01:55.378Z",
        "settled": null,
        "updated": null,
        "done": null,
        "stopAmount": "1180000.00",
        "groupId": "0",
        "marketOrderId": "0",
        "title": "",
        "description": ""
    }
}
Cancel Order
This endpoint cancels the given order. You need to send request with [POST] method. Returns the order object if it's successfully cancelled.

This endpoint requires authentication. Please check Authentication section for details.

Parameters

Name	Type	Required	Example Value
orderId	body / json	yes	XXXXXXXX
type	body / json	yes	MARKET, LIMIT, CANCEL, STOP_LIMIT, CHAIN_ORDER, AUTOSAVING_ORDER
Sample Request:


{
  "orderId":"XXXXXXXX",
  "type":"LIMIT"
}
Sample Response:


{
    "order": {
        "id": "XXXXXXXX",
        "customerId": "yyyyyy",
        "market": "BTC-TRY",
        "type": "CANCEL",
        "side": "SELL",
        "timeInForce": "GTC",
        "price": "1200000.00",
        "funds": "0.0000000000",
        "quantity": "0.00000000",
        "executedValue": "0.0000000000",
        "executedQuantity": "0.00000000",
        "executedFees": "0",
        "remainingQuantity": null,
        "remainingFunds": null,
        "fillQuantity": "0.00000000",
        "fillValue": "0.0000000000",
        "fillAveragePrice": "0",
        "status": "NEW",
        "created": "2024-02-05T08:17:18.388051Z",
        "settled": null,
        "updated": null,
        "done": null,
        "stopAmount": "0.00",
        "groupId": "0",
        "marketOrderId": "0",
        "title": "",
        "description": ""
    }
}
 

WebSocket Feed
General Information
Endpoint: wss://api4.bitlo.com/ws

Bitlo WebSocket feed provides real-time data updates for tickers and markets.
Bitlo WebSocket feed is publicly available and does not require authentication.
Bitlo WebSocket feed encodes all messages as JSON objects. All messages have a content-type attribute.
You can use STOMP.js library for your node.js applications.

Java

import org.springframework.messaging.converter.MappingJackson2MessageConverter;
import org.springframework.messaging.simp.stomp.StompSession;
import org.springframework.web.socket.messaging.WebSocketStompClient;
import org.springframework.web.socket.sockjs.client.RestTemplateXhrTransport;
import org.springframework.web.socket.sockjs.client.SockJsClient;
import org.springframework.web.socket.sockjs.client.Transport;

import java.util.concurrent.TimeUnit;

public class StompClient {
  private String url;
  public static long lastMessageTime = 0;

  SockJsClient client;
  private final StompSocketHandler myWebSocketHandler;
  WebSocketStompClient stompClient;
  private final StompSessHandler sessionHandler;
  StompSession stompSession;

  public StompClient(StompSessHandler sessionHandler, StompSocketHandler myWebSocketHandler, String url) {
    this.sessionHandler = sessionHandler;
    this.myWebSocketHandler = myWebSocketHandler;
    this.url = url;
    connect();
  }

  public void connect() {
    log.info("Start connecting to url : "+ url);
    List<Transport> transports = new ArrayList<>(1);
    transports.add(new RestTemplateXhrTransport());
    client = new SockJsClient(transports);

    stompClient = new WebSocketStompClient(client);
    stompClient.setMessageConverter(new MappingJackson2MessageConverter());
    try {
      stompSession = stompClient.connect(url, sessionHandler).get(60, TimeUnit.SECONDS);
      log.info("Socket connected...");
    } catch (InterruptedException | ExecutionException | TimeoutException e) {
      log.error("Socket connection error",e);
    }
  }
}

import org.springframework.messaging.simp.stomp.StompHeaders;
import org.springframework.messaging.simp.stomp.StompSession;
import org.springframework.messaging.simp.stomp.StompSessionHandlerAdapter;

public class StompSessHandler extends StompSessionHandlerAdapter {

  @Override
  public void afterConnected(StompSession session, StompHeaders connectedHeaders) {
    System.out.println("New session established : " + session.getSessionId());
    StompClient.lastMessageTime = System.currentTimeMillis() + 60000;
    session.subscribe("/topic/ticker/*", this);
    session.subscribe("/topic/market/*", this);
    System.out.println("All Subscribed.");
  }

  @Override
  public Type getPayloadType(StompHeaders headers) {
    switch (headers.getSubscription()) {
      case "0": // ticker
        return <YourTickerObject.class>;
      case "1": // market
        return <YourMarketObject.class>;
      default:
        return null;
    }
  }
}

import org.springframework.web.socket.WebSocketHandler;
import org.springframework.web.socket.WebSocketSession;

public class StompSocketHandler implements WebSocketHandler {

  @Override
  public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    System.out.println("Connected");
    StompClient.lastMessageTime = System.currentTimeMillis() + 60000;
  }

  @Override
  public boolean supportsPartialMessages() {
    return false;
  }
}

Channel, Event and Model
You need to subscribe to specific channels for receiving messages after successful login to the websocket feed.
You'll continue to receive those messages unless the unsubscribe message is sent.
Channel	Description
/topic/ticker	Sends ticker data for all markets. e.g.: /topic/ticker/all
/topic/market	Sends market data updates for the given pair. e.g.: /topic/market/BTC-TRY
 Back to top
© 2024 Bitlo
Made with Material for MkDocs