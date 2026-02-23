---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python: Python
  - go: Golang

includes:
  - changelog
  - introduction
  - clients
  - overview
  - examples
  - resources
  - explorer
  - faucet
  - status
  - broadcaster
  - exchangeapi
  - accountsrpc
  - spotrpc
  - derivativesrpc
  - oraclerpc
  - insurancerpc
  - auctionsrpc
  - explorerrpc
  - metarpc
  - portfoliorpc
  - chainapi
  - account
  - auction
  - authz
  - bank
  - chainstream
  - chainexchange
  - derivatives
  - spot
  - binaryoptions
  - erc20
  - evm
  - ibccorechannel
  - ibccoreclient
  - ibccoreconnection
  - ibctransfer
  - insurance
  - oracle
  - permissions
  - staking
  - tendermint
  - tokenfactory
  - txfees
  - wasm
  - wasmx
  - websocket
  - historicalqueries
  - healthapi
  - glossary
  - faq
  - errors
search: true

code_clipboard: true
---


# - WebSocket
The WebSocket endpoint provides a real-time streaming interface for Injective chain events. It is a wrapper on top of the Chain Stream gRPC service, so you receive the same event data (trades, orders, balances, oracle prices, etc.) over a standard WebSocket connection instead of gRPC. The request and response shapes match the [Chain Stream](#chain-stream) API: you use the same filters and receive the same stream payloads.

Use the WebSocket when your client environment supports WebSockets but not gRPC (e.g. browsers or some server runtimes), or when you prefer a single long-lived HTTP upgrade over gRPC streaming.

## Connecting

Connect to the WebSocket at the following path on a node that exposes the WebSocket server:

```
ws://<node-address>:<port>/injstream-ws
```

For secure connections, use a TLS-terminating proxy and connect with `wss://` to the proxy endpoint.

After the connection is established, send JSON-RPC 2.0 requests to subscribe or unsubscribe. All messages are JSON; text frames only.

> Connect and subscribe:

```py
import asyncio
import json

import websockets


async def main():
    uri = "ws://localhost:9998/injstream-ws"
    async with websockets.connect(uri) as ws:
        subscribe_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "subscribe",
            "params": {
                "req": {
                    "subscription_id": "my-oracle-prices",
                    "filter": {
                        "oracle_price_filter": {"symbol": ["INJ", "USDT"]}
                    },
                }
            },
        }
        await ws.send(json.dumps(subscribe_request))

        async for raw in ws:
            msg = json.loads(raw)
            print(msg)


if __name__ == "__main__":
    asyncio.run(main())
```
```go
package main

import (
	"encoding/json"
	"log"
	"net/url"

	"github.com/gorilla/websocket"
)

func main() {
	u := url.URL{Scheme: "ws", Host: "localhost:9998", Path: "/injstream-ws"}
	conn, _, err := websocket.DefaultDialer.Dial(u.String(), nil)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	subscribeReq := map[string]interface{}{
		"jsonrpc": "2.0",
		"id":      float64(1),
		"method":  "subscribe",
		"params": map[string]interface{}{
			"req": map[string]interface{}{
				"subscription_id": "my-oracle-prices",
				"filter": map[string]interface{}{
					"oracle_price_filter": map[string]interface{}{
						"symbol": []string{"INJ", "USDT"},
					},
				},
			},
		},
	}
	payload, _ := json.Marshal(subscribeReq)
	if err := conn.WriteMessage(websocket.TextMessage, payload); err != nil {
		log.Fatal(err)
	}

	for {
		_, data, err := conn.ReadMessage()
		if err != nil {
			log.Fatal(err)
		}
		var msg map[string]interface{}
		json.Unmarshal(data, &msg)
		log.Printf("%+v", msg)
	}
}
```

## Subscribing to events

Send a JSON-RPC 2.0 request with method `subscribe`. The request must include:

- `jsonrpc`: `"2.0"`
- `id`: A positive integer used to match responses for this subscription
- `method`: `"subscribe"`
- `params.req.subscription_id`: A **client-chosen unique identifier** for this subscription (used later to unsubscribe)
- `params.req.filter`: An object with one or more of the filter types below (same as [Chain Stream](#chain-stream))

At least one filter must be specified. You can combine multiple filters in a single subscription.

> Subscribe to oracle prices:

```javascript
const subscribeRequest = {
  jsonrpc: '2.0',
  id: 1,
  method: 'subscribe',
  params: {
    req: {
      subscription_id: 'my-oracle-prices',
      filter: {
        oracle_price_filter: {
          symbol: ['*']  // Use '*' to subscribe to all symbols
        }
      }
    }
  }
};

ws.send(JSON.stringify(subscribeRequest));
```

> Subscribe to spot orders for a specific market:

```javascript
const subscribeRequest = {
  jsonrpc: '2.0',
  id: 2,
  method: 'subscribe',
  params: {
    req: {
      subscription_id: 'spot-orders-market-1',
      filter: {
        spot_orders_filter: {
          market_ids: ['0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe'],
          subaccount_ids: ['*']
        }
      }
    }
  }
};

ws.send(JSON.stringify(subscribeRequest));
```

> Subscribe to multiple event types:

```javascript
const subscribeRequest = {
  jsonrpc: '2.0',
  id: 3,
  method: 'subscribe',
  params: {
    req: {
      subscription_id: 'my-trading-stream',
      filter: {
        spot_orders_filter: {
          market_ids: ['*'],
          subaccount_ids: ['0xeb8cf88b739fe12e303e31fb88fc37751e17cf3d000000000000000000000000']
        },
        derivative_orders_filter: {
          market_ids: ['*'],
          subaccount_ids: ['0xeb8cf88b739fe12e303e31fb88fc37751e17cf3d000000000000000000000000']
        },
        oracle_price_filter: {
          symbol: ['BTCUSD', 'ETHUSD']
        },
        positions_filter: {
          subaccount_ids: ['0xeb8cf88b739fe12e303e31fb88fc37751e17cf3d000000000000000000000000'],
          market_ids: ['*']
        }
      }
    }
  }
};

ws.send(JSON.stringify(subscribeRequest));
```

> Successful subscription response:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "success"
}
```

After a successful subscription, stream updates are sent as JSON-RPC responses with the same `id`. Only fields that match your filters will contain data; others will be empty arrays or omitted.

## Unsubscribing

To stop receiving events for a subscription, send a request with method `unsubscribe` and the same `subscription_id` you used when subscribing:

```javascript
const unsubscribeRequest = {
  jsonrpc: '2.0',
  id: 100,
  method: 'unsubscribe',
  params: {
    req: {
      subscription_id: 'my-oracle-prices'
    }
  }
};

ws.send(JSON.stringify(unsubscribeRequest));
```

> Successful unsubscribe response:

```json
{
  "jsonrpc": "2.0",
  "id": 100,
  "result": "success"
}
```

The `subscription_id` must match exactly the value you provided when creating the subscription. When the WebSocket connection is closed, all its subscriptions are cancelled automatically.

## Subscribe request filter

The `params.req.filter` object uses the same structure as the [Chain Stream](#chain-stream) **Stream Request**: the same filter names (e.g. `bank_balances_filter`, `spot_trades_filter`, `oracle_price_filter`) and the same parameters per filter. You must specify at least one filter. For the full list of filters, their parameters, and wildcard (`"*"`) support, see the [Chain Stream — Stream Request](#chain-stream-stream-request) section.

## Stream response format

Stream updates are delivered as JSON-RPC 2.0 responses. The `result` field is the same as the [Chain Stream](#chain-stream) **StreamResponse**: one message per block, with `block_height`, `block_time`, and arrays for each event type. For the full response shape and the structure of each event type (e.g. `SpotTrade`, `Position`, `OraclePrice`), see the [Chain Stream — StreamResponse](#chain-stream-streamresponse) section.

> Stream message:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "block_height": "12345678",
    "block_time": "1702123456789",
    "bank_balances": [],
    "subaccount_deposits": [],
    "spot_trades": [],
    "derivative_trades": [],
    "spot_orders": [],
    "derivative_orders": [],
    "spot_orderbook_updates": [],
    "derivative_orderbook_updates": [],
    "positions": [],
    "oracle_prices": [...],
    "gas_price": "160000000",
    "order_failures": [],
    "conditional_order_trigger_failures": []
  }
}
```

## Client behavior

- **Subscription ID:** You choose a unique `subscription_id` per subscription. It must be unique within the same connection. Use it when unsubscribing. After a reconnect, you can re-subscribe with the same IDs to get back the same logical subscriptions.
- **Connection lifecycle:** When the WebSocket connection is closed, all subscriptions for that connection are cancelled. Implement reconnection (e.g. with increasing delay between attempts to avoid hammering the server) and re-send subscribe requests for the streams you need. The stream is live-only: after reconnecting you only receive new events from that point; past events are not replayed.
- **Errors:** The server may send JSON-RPC error responses (e.g. invalid request or subscription already exists). Handle `error` in the JSON-RPC payload and optional ping/pong frames to detect stale connections.


# Clients

## Python Client

**Dependencies**

*Ubuntu*

`sudo apt install python3.X-dev autoconf automake build-essential libffi-dev libtool pkg-config`

*Fedora*

`sudo dnf install python3-devel autoconf automake gcc gcc-c++ libffi-devel libtool make pkgconfig`

*macOS*

`brew install autoconf automake libtool`

**Installation**

Install injective-py from PyPI using `pip`.

```bash
pip install injective-py
```
**Reference**

[InjectiveLabs/sdk-python](https://github.com/InjectiveLabs/sdk-python)


### Choose Exchange V1 or Exchange V2 queries

The Injective Python SDK provides two different clients for interacting with the exchange:

> Example - Exchange V1 Client

```python
from injective.async_client import AsyncClient
from injective.network import Network

async def main():
	# Initialize client with mainnet
	client = AsyncClient(network=Network.mainnet())
	# Or use testnet
	# client = AsyncClient(network=Network.testnet())
	# Use V1 exchange queries here
```

1. **Exchange V1 Client** (`async_client` module):
   - Use this client if you need to interact with the original Injective Exchange API
   - Import using: `from injective.async_client import AsyncClient`
   - Suitable for applications that need to maintain compatibility with the original exchange interface

> Example - Exchange V2 Client

```python
from injective.async_client_v2 import AsyncClient
from injective.network import Network

async def main():
	# Initialize client with mainnet
	client = AsyncClient(network=Network.mainnet())
	# Or use testnet
	# client = AsyncClient(network=Network.testnet())
	# Use V2 exchange queries here
```

2. **Exchange V2 Client** (`async_client_v2` module):
   - Use this client for the latest exchange features and improvements
   - Import using: `from injective.async_client_v2 import AsyncClient`
   - Recommended for new applications and when you need access to the latest exchange features


Both clients provide similar interfaces but with different underlying implementations. Choose V2 for new projects unless you have specific requirements for V1 compatibility.

**Market Format Differences**:

- V1 AsyncClient: Markets are initialized with values in chain format (raw blockchain values)
- V2 AsyncClient: Markets are initialized with values in human-readable format (converted to standard decimal numbers)

**Exchange Endpoint Format Differences**:

- V1 Exchange endpoints: All values (amounts, prices, margins, notionals) are returned in chain format
- V2 Exchange endpoints:
  - Human-readable format for: amounts, prices, margins, and notionals
  - Chain format for: deposit-related information (to maintain consistency with the Bank module)

<aside class="notice">
<b>NOTE:</b> The ChainClient (V1) will not receive any new endpoints added to the Exchange module. If you need access to new exchange-related endpoints or features, you should migrate to the V2 client. The V2 client ensures you have access to all the latest exchange functionality and improvements.
</aside>


## Golang Client

**1. Create your own client repo and go.mod file**

`go mod init foo`

**2. Import SDK into go.mod**

<code>
    require (
      github.com/InjectiveLabs/sdk-go v1.58.0
    )
</code>

*Consult the sdk-go repository to find the latest release and replace the version in your go.mod file. Version v1.39.4 is only an example and must be replaced with the newest release*

**3. Download the package**

Download the package using `go mod download`

`go mod download github.com/InjectiveLabs/sdk-go`


### Choose Exchange V1 or Exchange V2 queries

The SDK provides two different clients for interacting with the Injective Exchange:

> Example - ChainClient

```go
// For Exchange V1
client := chainclient.NewChainClient(...)

// For Exchange V2
clientV2 := chainclient.NewChainClientV2(...)
```

- `ChainClient`: Use this client if you need to interact with Exchange V1. This client maintains compatibility with the original exchange implementation and is suitable for existing applications that haven't migrated to V2 yet. Note that this client will not include any new endpoints added to the Exchange module - for access to new features, you should migrate to V2.

- `ChainClientV2`: Use this client for all new applications or when you need to interact with Exchange V2 features. This client provides access to the latest exchange functionality and improvements, including all new endpoints added to the Exchange module.

**Markets Assistant**

> Example - Markets Assistant

```go
// For Exchange V1 markets
marketsAssistant, err := chain.NewMarketsAssistant(ctx, client)  // ChainClient instance
if err != nil {
    // Handle error
}

// For Exchange V2 markets
marketsAssistantV2, err := chain.NewHumanReadableMarketsAssistant(ctx, clientV2)  // ChainClientV2 instance
if err != nil {
    // Handle error
}
```

The SDK provides a Markets Assistant to help you interact with markets in both V1 and V2. Here's how to create instances for each version

The Markets Assistant provides helper methods to:

- Fetch market information
- Get market prices
- Query orderbooks
- Access market statistics

Make sure to use the correct version of the Markets Assistant that matches your ChainClient version to ensure compatibility. The V1 assistant (`NewMarketsAssistant`) will only work with V1 markets, while the V2 assistant (`NewHumanReadableMarketsAssistant`) provides access to V2 markets and their features.

**Format Differences**

There are important format differences between V1 and V2 endpoints:

- **Exchange V1**: All values (amounts, prices, margins, notionals) are returned in chain format (raw numbers)
- **Exchange V2**: Most values are returned in human-readable format for better usability:
  - Amounts, prices, margins, and notionals are in human-readable format
  - Deposit-related information remains in chain format to maintain consistency with the Bank module

This format difference is one of the key improvements in V2, making it easier to work with market data without manual conversion.


### Markets and Tokens information

Since **version 1.49** the SDK is able also to get the markets and tokens information directly from the chain data (through the Indexer process). 
The benefit of this approach is that it is not necessary to update the SDK version when a new market is created in the chain or a new token is added.

> Example - Get markets and tokens from Indexer (ExchangeClient)

```go
package main

import (
	"context"
	"github.com/InjectiveLabs/sdk-go/client"
	"github.com/InjectiveLabs/sdk-go/client/core"
	exchangeclient "github.com/InjectiveLabs/sdk-go/client/exchange"
	"os"

	"github.com/InjectiveLabs/sdk-go/client/common"

	chainclient "github.com/InjectiveLabs/sdk-go/client/chain"
	rpchttp "github.com/cometbft/cometbft/rpc/client/http"
)

func main() {
	network := common.LoadNetwork("testnet", "lb")
	tmClient, err := rpchttp.New(network.TmEndpoint, "/websocket")
	if err != nil {
		panic(err)
	}

	senderAddress, cosmosKeyring, err := chainclient.InitCosmosKeyring(
		os.Getenv("HOME")+"/.injectived",
		"injectived",
		"file",
		"inj-user",
		"12345678",
		"5d386fbdbf11f1141010f81a46b40f94887367562bd33b452bbaa6ce1cd1381e", // keyring will be used if pk not provided
		false,
	)

	if err != nil {
		panic(err)
	}

	// initialize grpc client
	clientCtx, err := chainclient.NewClientContext(
		network.ChainId,
		senderAddress.String(),
		cosmosKeyring,
	)
	if err != nil {
		panic(err)
	}
	clientCtx = clientCtx.WithNodeURI(network.TmEndpoint).WithClient(tmClient)

	exchangeClient, err := exchangeclient.NewExchangeClient(network)
	if err != nil {
		panic(err)
	}

	ctx := context.Background()
	marketsAssistant, err := core.NewMarketsAssistantUsingExchangeClient(ctx, exchangeClient)
	if err != nil {
		panic(err)
	}
}

```

- To get the markets and tokens information directly from the chain, create an instance of MarketsAssistant using the `NewMarketsAssistantUsingExchangeClient` function and passing the ExchangeClient as parameter

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

> Example - MarketsAssistant with all tokens

```go
package main

import (
	"context"
	"github.com/InjectiveLabs/sdk-go/client"
	"github.com/InjectiveLabs/sdk-go/client/core"
	exchangeclient "github.com/InjectiveLabs/sdk-go/client/exchange"
	"os"

	"github.com/InjectiveLabs/sdk-go/client/common"

	chainclient "github.com/InjectiveLabs/sdk-go/client/chain"
	rpchttp "github.com/cometbft/cometbft/rpc/client/http"
)

func main() {
	network := common.LoadNetwork("testnet", "lb")
	tmClient, err := rpchttp.New(network.TmEndpoint, "/websocket")
	if err != nil {
		panic(err)
	}

	senderAddress, cosmosKeyring, err := chainclient.InitCosmosKeyring(
		os.Getenv("HOME")+"/.injectived",
		"injectived",
		"file",
		"inj-user",
		"12345678",
		"5d386fbdbf11f1141010f81a46b40f94887367562bd33b452bbaa6ce1cd1381e", // keyring will be used if pk not provided
		false,
	)

	if err != nil {
		panic(err)
	}

	// initialize grpc client
	clientCtx, err := chainclient.NewClientContext(
		network.ChainId,
		senderAddress.String(),
		cosmosKeyring,
	)
	if err != nil {
		panic(err)
	}
	clientCtx = clientCtx.WithNodeURI(network.TmEndpoint).WithClient(tmClient)

	exchangeClient, err := exchangeclient.NewExchangeClient(network)
	if err != nil {
		panic(err)
	}

	chainClient, err := chainclient.NewChainClient(
		clientCtx,
		network,
		common.OptionGasPrices(client.DefaultGasPriceWithDenom),
	)

	if err != nil {
		panic(err)
	}

	ctx := context.Background()
	marketsAssistant, err := core.NewMarketsAssistantWithAllTokens(ctx, exchangeClient, chainClient)
	if err != nil {
		panic(err)
	}
}

```

By default the MarketsAssistant will only initialize the tokens that are part of an active market. In order to let it use any of the tokens available in the chain, the user has to create the MarketsAssistant instance using the function  `NewMarketsAssistantWithAllTokens`.


The MarketsAssistant instance can be used with the following ChainClient functions:

- `CreateSpotOrder`
- `CreateDerivativeOrder`



**Reference**

[InjectiveLabs/sdk-go](https://github.com/InjectiveLabs/sdk-go).


## Typescript Client

**Installation**

Install the `@injectivelabs/sdk-ts` npm package using `yarn`

```bash
yarn add @injectivelabs/sdk-ts
```

**Reference**

- [Typescript SDK documentation](https://docs.ts.injective.network/)
  
- [InjectiveLabs/injective-ts](https://github.com/InjectiveLabs/injective-ts/tree/master/packages/sdk-ts)


To see Typescript examples please check the Typescript SDK documentation page listed above

## For other languages
Currently Injective provides SDKs only for Go, Python and TypeScript. To interact with the nodes using a different language please connect directly using the gRPC proto objects.
The compiled proto files for C++, C# and Rust can be found in [InjectiveLabs/injective-proto](https://github.com/InjectiveLabs/injective-proto)


