# Working with /account

Source: https://docs.alpaca.markets/docs/working-with-account

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
# Working with /account
Learn how to use the /account endpoint to learn about the state of your account
# View Account Information

By sending a `GET` request to our `/v2/account` endpoint, you can see various information about your account, such as the amount of buying power available or whether or not it has a PDT flag.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print(&#x27;Account is currently restricted from trading.&#x27;)

# Check how much money we can use to open new positions.
print(&#x27;${} is available as buying power.&#x27;.format(account.buying_power))`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get our account information.
alpaca.getAccount().then((account) => {
  // Check if our account is restricted from trading.
  if (account.trading_blocked) {
    console.log("Account is currently restricted from trading.");
  }

  // Check how much money we can use to open new positions.
  console.log(`$${account.buying_power} is available as buying power.`);
});`
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

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get our account information.
            var account = await client.GetAccountAsync();

            // Check if our account is restricted from trading.
            if (account.IsTradingBlocked)
            {
                Console.WriteLine("Account is currently restricted from trading.");
            }

            Console.WriteLine(account.BuyingPower + " is available as buying power.");

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
	// Get our account information.
	account, err := alpaca.GetAccount()
	if err != nil {
		panic(err)
	}

	// Check if our account is restricted from trading.
	if account.TradingBlocked {
		fmt.Println("Account is currently restricted from trading.")
	}

	// Check how much money we can use to open new positions.
	fmt.Printf("%v is available as buying power.\n", account.BuyingPower)
}`
```

# View Gain/Loss of Portfolio

You can use the information from the account endpoint to do things like calculating the daily profit or loss of your account.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;)

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f&#x27;Today\&#x27;s portfolio balance change: ${balance_change}&#x27;)`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get account information.
alpaca.getAccount().then((account) => {
  // Calculate the difference between current balance and balance at the last market close.
  const balanceChange = account.equity - account.last_equity;

  console.log("Today&#x27;s portfolio balance change:", balanceChange);
});`
```

```
`using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// With the Alpaca API, you can check on your daily profit or loss by
// comparing your current balance to yesterday&#x27;s balance.

namespace GetPnLExample
{
    internal class GetPnL
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get account info
            var account = await client.GetAccountAsync();

            // Check our current balance vs. our balance at the last market close
            var balance_change = account.Equity - account.LastEquity;

            Console.WriteLine($"Today&#x27;s portfolio balance change: ${balance_change}");
        }
    }
}`
```

```
`package main

import (
	"fmt"
	"log"

	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func main() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")

	// Get account information.
	account, err := alpaca.GetAccount()
	if err != nil {
		log.Fatalln(err)
	}

	// Calculate the difference between current balance and balance at the last market close.
	balanceChange := account.Equity.Sub(account.LastEquity)

	fmt.Println("Today&#x27;s portfolio balance change:", balanceChange)
}`
```
Updated 5 months ago Getting Started with Trading APIWorking with /assets- Ask AI
