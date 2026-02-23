# Working with /positions

Source: https://docs.alpaca.markets/docs/working-with-positions

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
# Working with /positions
You can view the positions in your portfolio by making a `GET` request to the `/v2/positions` endpoint. If you specify a symbol, you’ll see only your position for the associated stock.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;)

# Get our position in AAPL.
aapl_position = trading_client.get_open_position(&#x27;AAPL&#x27;)

# Get a list of all of our positions.
portfolio = trading_client.get_all_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get our position in AAPL.
aaplPosition = alpaca.getPosition("AAPL");

// Get a list of all of our positions.
alpaca.getPositions().then((portfolio) => {
  // Print the quantity of shares for each position.
  portfolio.forEach(function (position) {
    console.log(`${position.qty} shares of ${position.symbol}`);
  });
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

            // Get our position in AAPL.
            var aaplPosition = await client.GetPositionAsync("AAPL");

            // Get a list of all of our positions.
            var positions = await client.ListPositionsAsync();

            // Print the quantity of shares for each position.
            foreach (var position in positions)
            {
                Console.WriteLine($"{position.Quantity} shares of {position.Symbol}.");
            }

            Console.Read();
        }
    }
}`
```

```
`package main

import (
	"fmt"
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get our position in AAPL.
	aapl_position, err := alpaca.GetPosition("AAPL")
	if err != nil {
		fmt.Println("No AAPL position.")
	} else {
		fmt.Printf("AAPL position: %v shares.\n", aapl_position.Qty)
	}

	// Get a list of all of our positions.
	positions, err := alpaca.ListPositions()
	if err != nil {
		fmt.Println("No positions found.")
	} else {
		// Print the quantity of shares for each position.
		for _, position := range positions {
			fmt.Printf("%v shares in %s", position.Qty, position.Symbol)
		}
	}
}`
```

The current price reflected will be based on the following:
4:00 am ET - 9:30 am ET - Last trade based on the premarket
9:30 am ET - 4pm ET - Last trade
4:00 pm ET - 10:00 pm ET - Last trade based on after-hours trading
10 pm ET - 4:00 am ET next trading day - Official closing price from the primary exchange at 4 pm ET.Updated 5 months ago Working with /ordersPaper Trading- Ask AI
