# Working with /assets

Source: https://docs.alpaca.markets/docs/working-with-assets

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
# Working with /assets
Learn how to use the `/assets` endpoint to learn more about assets available on Alpaca. Both Securities and Crypto can be retrieved from the `/assets` endpoint.
# Get a List of Assets

If you send a `GET` request to our `/v2/assets` endpoint, you’ll receive a list of US equities.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;)

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get a list of all active assets.
const activeAssets = alpaca
  .getAssets({
    status: "active",
  })
  .then((activeAssets) => {
    // Filter the assets down to just those on NASDAQ.
    const nasdaqAssets = activeAssets.filter(
      (asset) => asset.exchange == "NASDAQ"
    );
    console.log(nasdaqAssets);
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

            // Get a list of all active assets.
            var assets = await client.ListAssetsAsync(
                new AssetsRequest { AssetStatus = AssetStatus.Active });

            // Filter the assets down to just those on NASDAQ.
            var nasdaqAssets = assets.Where(asset => asset.Exchange == Exchange.NyseMkt);

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
	// Get a list of all active assets.
	status := "active"
	assets, err := alpaca.ListAssets(&status)
	if err != nil {
		panic(err)
	}

	// Filter the assets down to just those on NASDAQ.
	nasdaq_assets := []alpaca.Asset{}
	for _, asset := range assets {
		if asset.Exchange == "NASDAQ" {
			nasdaq_assets = append(nasdaq_assets, asset)
		}
	}
}`
```

# See If a Particular Asset is Tradable on Alpaca

By sending a symbol along with our request, we can get the information about just one asset. This is useful if we just want to make sure that a particular asset is tradable before we attempt to buy it.
PythonJavaScriptC#Go
```
`from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient(&#x27;api-key&#x27;, &#x27;secret-key&#x27;)

# search for AAPL
aapl_asset = trading_client.get_asset(&#x27;AAPL&#x27;)

if aapl_asset.tradable:
    print(&#x27;We can trade AAPL.&#x27;)`
```

```
`const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Check if AAPL is tradable on the Alpaca platform.
alpaca.getAsset("AAPL").then((aaplAsset) => {
  if (aaplAsset.tradable) {
    console.log("We can trade AAPL.");
  }
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

            // Check if AAPL is tradable on the Alpaca platform.
            try
            {
                var asset = await client.GetAssetAsync("AAPL");
                if (asset.IsTradable)
                {
                    Console.WriteLine("We can trade AAPL");
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Asset not found for AAPL.");
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
	// Check if AAPL is tradable on the Alpaca platform.
	asset, err := alpaca.GetAsset("AAPL")
	if err != nil {
		fmt.Println("Asset not found for AAPL.")
	} else if asset.Tradable {
		fmt.Println("We can trade AAPL.")
	}
}`
```
Updated 5 months ago Working with /accountWorking with /orders- Ask AI
