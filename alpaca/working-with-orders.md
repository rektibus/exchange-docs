# Working with /orders

Source: https://docs.alpaca.markets/docs/working-with-orders

---

## Introduction
- Welcome- About Alpaca- Alpaca API Platform- Authentication- SDKs and Tools- Additional Resources
## BROKER API
- About Broker API- Getting Started with Broker API- Credentials Management- Use Cases- Integration Setup with Alpaca- Broker API FAQs- Mandatory Corporate Actions- Voluntary Corporate Actions- FDIC Sweep Program- Instant Funding- Fully Paid Securities Lending- 24/5 Trading- OmniSub- Fixed Income- Customer Account Opening- Accounts Statuses- International Accounts- Domestic (USA) Accounts- Data Validations- IRA Accounts Overview- Crypto Trading- Crypto Wallets API- Funding Accounts- Journals API- Funding Wallets- ACH Funding- Instant Funding- Trading- Portfolio Rebalancing- SSE Events- Account Status Events for KYCaaS- Daily Processes and Reconcilations- Banking Holiday Funding Processes- Statements and Confirms- Local Currency Trading (LCT)- Example Trading App (Ribbit)- Options Trading Overview- Fixed Income- Tokenization Guide for Issuer- Tokenization Guide for Authorized Participant- Custodial accounts
## TRADING API
- About Trading API- Getting Started with Trading API- Working with /account- Working with /assets- Working with /orders- Working with /positions- Paper Trading- Trading Account- Crypto Spot Trading- Crypto Orders- Crypto Pricing Data- Crypto Spot Trading Fees- Options Trading- Options Orders- Options Level 3 Trading- Non-Trade Activities for Option Events- Account Activities- Fractional Trading- Margin and Short Selling- Placing Orders- DMA Gateway / Advanced Order Types- User Protection- Websocket Streaming- Trading API FAQs- Position Average Entry Price Calculation- Regulatory Fees- Alpaca&#x27;s MCP Server
## Market Data API
- About Market Data API- Getting Started with Market Data API- Historical API- Historical Stock Data- Historical Crypto Data- Historical Option Data- Historical News Data- WebSocket Stream- Real-time Stock Data- Real-time Crypto Data- Real-time News- Real-time Option Data- Market Data FAQ
## Connect API
- About Connect API- Registering Your App- Using OAuth2 and Trading API
## FIX API
- About FIX API- FIX Specification
# Working with /orders
Learn how to submit orders to Alpaca.This page contains examples of some of the things you can do with order objects through our API. For additional help understanding different types of orders and how they behave once they’re placed, please check out the Orders on Alpaca page.

# Place New Orders

Orders can be placed with a `POST` request to our `/v2/orders` endpoint.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# preparing limit order
limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# Limit order
limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Submit a market order to buy 1 share of Apple at market price
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "buy",
  type: "market",
  time_in_force: "day",
});

// Submit a limit order to attempt to sell 1 share of AMD at a
// particular price ($20.50) when the market opens
alpaca.createOrder({
  symbol: "AMD",
  qty: 1,
  side: "sell",
  type: "limit",
  time_in_force: "opg",
  limit_price: 20.5,
});`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to buy 1 share of Apple at market price
            var order = await client.PostOrderAsync(MarketOrder.Buy("AAPL", 1));

            // Submit a limit order to attempt to sell 1 share of AMD at a
            // particular price ($20.50) when the market opens
            order = await client.PostOrderAsync(
                LimitOrder.Sell("AMD", 1, 20.50M).WithDuration(TimeInForce.Opg));

            Console.Read();
        }
    }
}`
```

```
`package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
	"github.com/shopspring/decimal"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Submit a market order to buy 1 share of Apple at market price
	symbol := "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Buy,
		Type: alpaca.Market,
		TimeInForce: alpaca.Day,
	})

	// Submit a limit order to attempt to sell 1 share of AMD at a
	// particular price ($20.50) when the market opens
	symbol = "AMD"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.Limit,
		TimeInForce: alpaca.OPG,
		LimitPrice: decimal.NewFromFloat(20.50),
	})
}`
```

# Submit Shorts

Short orders can also be placed for securities which you do not hold an open long position in.
PythonC#
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// With the Alpaca API, you can open a short position by submitting a sell
// order for a security that you have no open long position with.

namespace ShortingExample
{
    internal class ShortProgram
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        // The security we&#x27;ll be shorting
        private static string symbol = "TSLA";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var tradingClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            var dataClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaDataClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to open a short position of one share
            var order = await tradingClient.PostOrderAsync(MarketOrder.Sell(symbol, 1));
            Console.WriteLine("Market order submitted.");

            // Submit a limit order to attempt to grow our short position
            // First, get an up-to-date price for our security
            var snapshot = await dataClient.GetSnapshotAsync(symbol);
            var price = snapshot.MinuteBar.Close;

            // Submit another order for one share at that price
            order = await tradingClient.PostOrderAsync(LimitOrder.Sell(symbol, 1, price));
            Console.WriteLine($"Limit order submitted. Limit price = {order.LimitPrice}");

            // Wait a few seconds for our orders to fill...
            Thread.Sleep(2000);

            // Check on our position
            var position = await tradingClient.GetPositionAsync(symbol);
            if (position.Quantity < 0)
            {
                Console.WriteLine($"Short position open for {symbol}");
            }
        }
    }
}`
```

# Using Client Order IDs

`client_order_id` can be used to organize and track specific orders in your client program. Unique `client_order_ids` for different strategies is a good way of running parallel algos across the same account.
PythonJavaScriptC#
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    client_order_id=&#x27;my_first_order&#x27;,
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# Get our order using its Client Order ID.
my_order = trading_client.get_order_by_client_id(&#x27;my_first_order&#x27;)
print(&#x27;Got order #{}&#x27;.format(my_order.id))`
```

```
`const Alpaca = require(&#x27;@alpacahq/alpaca-trade-api&#x27;)
const alpaca = new Alpaca()

// Submit a market order and assign it a Client Order ID.
alpaca.createOrder({
    symbol: &#x27;AAPL&#x27;,
    qty: 1,
    side: &#x27;buy&#x27;,
    type: &#x27;market&#x27;,
    time_in_force: &#x27;day&#x27;,
    client_order_id=&#x27;my_first_order&#x27;
})

// Get our order using its Client Order ID.
alpaca.getOrderByClientOrderId(&#x27;my_first_order&#x27;)
    .then((myOrder) => {
        console.log(`Got order #${myOrder.id}.`)
    })`
```

```
`using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        private static string CLIENT_ORDER_ID = "my_first_order";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order and assign it a Client Order ID
            await client.PostOrderAsync(
                MarketOrder.Buy("AAPL", 1)
                    .WithClientOrderId(CLIENT_ORDER_ID));

            // Get our order using its Client Order ID
            var order = await client.GetOrderAsync(CLIENT_ORDER_ID);

            Console.WriteLine($"Got order #{order.ClientOrderId}");
            Console.Read();
        }
    }
}`
```

# Submitting Bracket Orders

Bracket orders allow you to create a chain of orders that react to execution and stock price. For more details, go to Bracket Order Overview.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

# preparing bracket order with both stop loss and take profit
bracket__order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=5,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.BRACKET,
                    take_profit=TakeProfitRequest(limit_price=400),
                    stop_loss=StopLossRequest(stop_price=300)
                    )

bracket_order = trading_client.submit_order(
                order_data=bracket__order_data
               )

# preparing oto order with stop loss
oto_order_data = LimitOrderRequest(
                    symbol="SPY",
                    qty=5,
                    limit_price=350,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.OTO,
                    stop_loss=StopLossRequest(stop_price=300)
                    )

# Market order
oto_order = trading_client.submit_order(
                order_data=oto_order_data
               )`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

const symbol = "AAPL";
alpaca
  .getBars("minute", symbol, {
    limit: 5,
  })
  .then((barset) => {
    const currentPrice = barset[symbol].slice(-1)[0].closePrice;

    // We could buy a position and add a stop-loss and a take-profit of 5 %
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "bracket",
      stop_loss: {
        stop_price: currentPrice * 0.95,
        limit_price: currentPrice * 0.94,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });

    // We could buy a position and just add a stop loss of 5 % (OTO Orders)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oto",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
    });

    // We could split it to 2 orders. first buy a stock,
    // and then add the stop/profit prices (OCO Orders)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
    });

    // wait for it to buy position and then
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "sell",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oco",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });
  });`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace ShortingExample
{
    internal class ShortProgram
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        private static string symbol = "APPL";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var tradingClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            var dataClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaDataClient(new SecretKey(API_KEY, API_SECRET));

            var snapshot = await dataClient.GetSnapshotAsync(symbol);
            var price = snapshot.MinuteBar.Close;

            // We could buy a position and add a stop-loss and a take-profit of 5 %
            await tradingClient.PostOrderAsync(
                MarketOrder.Buy(symbol, 1)
                .WithDuration(TimeInForce.Gtc)
                .Bracket(
                    stopLossStopPrice: price * 0.95M,
                    takeProfitLimitPrice: price * 0.94M,
                    stopLossLimitPrice: price * 1.05M));

            // We could buy a position and just add a stop loss of 5 % (OTO Orders)
            await tradingClient.PostOrderAsync(
                MarketOrder.Buy(symbol, 1)
                .WithDuration(TimeInForce.Gtc)
                .StopLoss(
                    stopLossStopPrice: price * 0.95M));

            // We could split it to 2 orders. first buy a stock,
            // and then add the stop/profit prices (OCO Orders)
            await tradingClient.PostOrderAsync(
                LimitOrder.Buy(symbol, 1, price));

            await tradingClient.PostOrderAsync(
                LimitOrder.Sell(symbol, 1, price)
                .WithDuration(TimeInForce.Gtc)
                .OneCancelsOther(
                    stopLossStopPrice: price * 0.95M,
                    stopLossLimitPrice: price * 1.05M));
        }
    }
}`
```

```
`package main

import (
    "github.com/alpacahq/alpaca-trade-api-go/alpaca"
    "github.com/alpacahq/alpaca-trade-api-go/common"
    "github.com/shopspring/decimal"
)

func init() {
    API_KEY := "YOUR_API_KEY_HERE"
    API_SECRET := "YOUR_API_SECRET_HERE"
    BASE_URL := "https://paper-api.alpaca.markets"
    // Check for environment variables
    if common.Credentials().ID == "" {
        os.Setenv(common.EnvApiKeyID, API_KEY)
    }
    if common.Credentials().Secret == "" {
        os.Setenv(common.EnvApiSecretKey, API_SECRET)
    }
    alpaca.SetBaseUrl(BASE_URL)
}

func main() {
    // Submit a limit order to buy 1 share of Apple and add
    // StopLoss and TakeProfit orders.
    client := alpaca.NewClient(common.Credentials())
    symbol := "AAPL"
    tpp := decimal.NewFromFloat(320.)
    spp := decimal.NewFromFloat(317.)
    limit := decimal.NewFromFloat(318.)
    tp := &alpaca.TakeProfit{LimitPrice: &tpp}
    sl := &alpaca.StopLoss{
        LimitPrice: nil,
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Bracket,
        TakeProfit:  tp,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // We could buy a position and just add a stop loss (OTO Orders)
    spp := decimal.NewFromFloat(317.)
    limit := decimal.NewFromFloat(318.)
    sl := &alpaca.StopLoss{
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Oto,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // We could split it to 2 orders. first buy a stock,
    // and then add the stop/profit prices (OCO Orders)
    limit := decimal.NewFromFloat(318.)
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Simple,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // wait for it to complete and then
    tpp := decimal.NewFromFloat(320.)
    spp := decimal.NewFromFloat(317.)
    tp := &alpaca.TakeProfit{LimitPrice: &tpp}
    sl := &alpaca.StopLoss{
        LimitPrice: nil,
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Sell,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Oco,
        TakeProfit:  tp,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)
}`
```

# Submitting Trailing Stop Orders

Trailing stop orders allow you to create a stop order that automatically changes the stop price allowing you to maximize your profits while still protecting your position with a stop price. For more details, go to Trailing Stop Order Overview.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

trailing_percent_data = TrailingStopOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    trail_percent=1.00 # hwm * 0.99
                    )

trailing_percent_order = trading_client.submit_order(
                order_data=trailing_percent_data
               )

trailing_price_data = TrailingStopOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    trail_price=1.00 # hwm - $1.00
                    )

trailing_price_order = trading_client.submit_order(
                order_data=trailing_price_data
               )`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Submit a market order to buy 1 share of Apple at market price
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "buy",
  type: "market",
  time_in_force: "day",
});

// Submit a trailing stop order to sell 1 share of Apple at a
// trailing stop of
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "sell",
  type: "trailing_stop",
  trail_price: 1.0, // stop price will be hwm - 1.00$
  time_in_force: "day",
});

// Alternatively, you could use trail_percent:
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "sell",
  type: "trailing_stop",
  trail_percent: 1.0, // stop price will be hwm*0.99
  time_in_force: "day",
});`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to buy 1 share of Apple at market price
            var order = await client.PostOrderAsync(
                new NewOrderRequest("AAPL", 1, OrderSide.Buy, OrderType.Market, TimeInForce.Day));

            // Submit a trailing stop order to sell 1 share of Apple at a
            // trailing stop of
            order = await client.PostOrderAsync(
                TrailingStopOrder.Sell("AAPL", 1, TrailOffset.InDollars(1.00M))); // stop price will be hwm - 1.00$

            /**
            // Alternatively, you could use trail_percent:
            order = await client.PostOrderAsync(
                TrailingStopOrder.Sell("AAPL", 1, TrailOffset.InPercent(0.99M))); // stop price will be hwm * 0.99
            */

            Console.Read();
        }
    }
}`
```

```
`package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
	"github.com/shopspring/decimal"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Submit a market order to buy 1 share of Apple at market price
	symbol := "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Buy,
		Type: alpaca.Market,
		TimeInForce: alpaca.Day,
	})

	// Submit a trailing stop order to sell 1 share of Apple at a
    // trailing stop of
	symbol = "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.TrailingStop,
		StopPrice: decimal.NewFromFloat(1.00),  // stop price will be hwm - 1.00$
		TimeInForce: alpaca.Day,
	})

	// Alternatively, you could use trail_percent:
	symbol = "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.TrailingStop,
		TrailPercent: decimal.NewFromFloat(1.0),  // stop price will be hwm*0.99
		TimeInForce: alpaca.Day,
	})
}`
```

# Retrieve All Orders

If you’d like to see a list of your existing orders, you can send a `GET` request to our `/v2/orders` endpoint.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

# Get the last 100 closed orders
get_orders_data = GetOrdersRequest(
    status=QueryOrderStatus.CLOSED,
    limit=100,
    nested=True  # show nested multi-leg orders
)

trading_client.get_orders(filter=get_orders_data)`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get the last 100 of our closed orders
const closedOrders = alpaca
  .getOrders({
    status: "closed",
    limit: 100,
    nested: true, // show nested multi-leg orders
  })
  .then((closedOrders) => {
    // Get only the closed orders for a particular stock
    const closedAaplOrders = closedOrders.filter(
      (order) => order.symbol == "AAPL"
    );
    console.log(closedAaplOrders);
  });`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get the last 100 of our closed orders
            var closedOrders = await client.ListOrdersAsync(
                new ListOrdersRequest
                {
                    LimitOrderNumber = 100,
                    OrderStatusFilter = OrderStatusFilter.Closed
                });

            // Get only the closed orders for a particular stock
            var aaplOrders = closedOrders.Where(order => order.Symbol.Equals("AAPL"));

            Console.Read();
        }
    }
}`
```

```
`package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get the last 100 of our closed orders
	status := "closed"
	limit := 100
	nested := true // show nested multi-leg orders
	closed_orders, err := alpaca.ListOrders(&status, nil, &limit, &nested)
	if err != nil {
		panic(err)
	}

	// Get only the closed orders for a particular stock
	var aaplOrders []alpaca.Order
	for _, order := range closed_orders {
		if order.Symbol == "AAPL" {
			aaplOrders = append(aaplOrders, order)
		}
	}
}`
```

# Listen for Updates to Orders

You can use Websockets to receive real-time updates about the status of your orders as they change. You can see the full documentation here.
PythonJavaScriptC#Go
```
`from alpaca.trading.stream import TradingStream

stream = TradingStream(&#x27;api-key&#x27;, &#x27;secret-key&#x27;, paper=True)

@conn.on(client_order_id)
async def on_msg(data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(data.event))

stream.subscribe_trade_updates(on_msg)
# Start listening for updates.
stream.run()`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Prepare the websocket connection and subscribe to trade_updates.
alpaca.websocket.onConnect(function () {
  console.log("Connected");
  client.subscribe(["trade_updates"]);
  setTimeout(() => {
    client.disconnect();
  }, 30 * 1000);
});
alpaca.websocket.onDisconnect(() => {
  console.log("Disconnected");
});
alpaca.websocket.onStateChange((newState) => {
  console.log(`State changed to ${newState}`);
});

// Handle updates on an order you&#x27;ve given a Client Order ID.
const client_order_id = "my_client_order_id";
alpaca.websocket.onOrderUpdate((orderData) => {
  const event = orderData["event"];
  if (orderData["order"]["client_order_id"] == client_order_id) {
    console.log(`Update for ${client_order_id}. Event: ${event}.`);
  }
});

// Start listening for updates.
alpaca.websocket.connect();`
```

```
`using Alpaca.Markets;
using System;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        // Print a message to the console when the account&#x27;s status changes.
        public static async Task Main(string[] args)
        {
            // Prepare the websocket connection and subscribe to trade_updates.
            var alpacaStreamingClient = Environments.Paper
                .GetAlpacaStreamingClient(new SecretKey(API_KEY, API_SECRET));

            await alpacaStreamingClient.ConnectAndAuthenticateAsync();
            alpacaStreamingClient.OnTradeUpdate += HandleTradeUpdate;

            Console.Read();
        }

        // Handle incoming trade updates.
        private static void HandleTradeUpdate(ITradeUpdate update)
        {
            if (update.Order.ClientOrderId.Equals("my_client_order_id"))
            {
                Console.WriteLine($"Update for {update.Order.ClientOrderId}. Event: {update.Event}");
            }
        }
    }
}`
```

```
`package main

import (
	"fmt"

	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
    "github.com/alpacahq/alpaca-trade-api-go/stream"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	if err := stream.Register(alpaca.TradeUpdates, tradeHandler); err != nil {
        panic(err)
    }
}

func tradeHandler(msg interface{}) {
	tradeupdate := msg.(alpaca.TradeUpdate)
	if tradeupdate.Order.ClientOrderID == "my_client_order_id" {
		fmt.Printf("Update for {}. Event: {}.\n", tradeupdate.Order.ClientOrderID, tradeupdate.Event)
	}
}`
```

# FAQ

What should I do if I receive a timeout message from Alpaca when submitting an order?
The order may have been sent to the market for execution. You should not attempt to resend the order or mark the timed-out order as canceled until confirmed by Alpaca Support or the trading team. Before taking any action on the timed-out order you should check the broker dashboard and contact Alpaca support.

Please contact our Support Team at [email&#160;protected] to verify if the order was successfully submitted and routed to the market.Updated 5 months ago Working with /assetsWorking with /positions- Ask AI
