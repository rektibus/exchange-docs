# Get Started Using HTTP / WebSocket APIs

If you don't have or don't want to use a [client library](/docs/references/client-libraries) in your preferred programming language, you can access the XRP Ledger directly through the APIs of its core server software, [`rippled`](/docs/concepts/networks-and-servers). The server provides APIs over JSON-RPC and WebSocket protocols. If you don't [run your own instance of `rippled`](/docs/infrastructure/installation) you can still use a [public server](/docs/tutorials/public-servers).

You can dive right into the API with the [**WebSocket API Tool**](/resources/dev-tools/websocket-api-tool), or use the [XRP Ledger Explorer](https://livenet.xrpl.org/) to watch the progress of the ledger live.

## Differences Between JSON-RPC and WebSocket

Both JSON-RPC and WebSocket are HTTP-based protocols, and for the most part the data provided over both protocols is the same. The major differences are as follows:

- JSON-RPC uses individual HTTP requests and responses for each call, similar to a RESTful API. You can use any common HTTP client such as [curl](https://curl.se/), [Postman](https://www.postman.com/downloads/), or [Requests](https://requests.readthedocs.io/) to access this API.
- WebSocket uses a persistent connection that allows the server to push data to the client. Functions that require push messages, like [event subscriptions](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe), are only available using WebSocket.


Both APIs can be served unencrypted (`http://` and `ws://`) or encrypted using TLS (`https://` and `wss://`). Unencrypted connections should not be served over open networks, but can be used when the client is on the same machine as the server.

## Admin Access

The API methods are divided into [Public Methods](/docs/references/http-websocket-apis/public-api-methods) and [Admin Methods](/docs/references/http-websocket-apis/admin-api-methods) so that organizations can offer public servers for the benefit of the community. To access admin methods, or admin functionality of public methods, you must connect to the API on a **port and IP address marked as admin** in the server's config file.

The [example config file](https://github.com/XRPLF/rippled/blob/f00f263852c472938bf8e993e26c7f96f435935c/cfg/rippled-example.cfg#L1154-L1179) listens for connections on the local loopback network (127.0.0.1), with JSON-RPC (HTTP) on port 5005 and WebSocket (WS) on port 6006, and treats all connected clients as admin.

## WebSocket API

If you are looking to try out some methods on the XRP Ledger, you can skip writing your own WebSocket code and go straight to using the API at the [WebSocket API Tool](/resources/dev-tools/websocket-api-tool). Later on, when you want to connect to your own `rippled` server, you can [build your own client](/docs/tutorials/http-websocket-apis/build-apps/monitor-incoming-payments-with-websocket) or use a [client library](/docs/references/client-libraries) with WebSocket support.

Example WebSocket API request:


```json
{
  "id": "my_first_request",
  "command": "server_info",
  "api_version": 1
}
```

The response shows you the current status of the server.

Read more: [Request Formatting >](/docs/references/http-websocket-apis/api-conventions/request-formatting) [Response Formatting >](/docs/references/http-websocket-apis/api-conventions/response-formatting) [About the server_info method >](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_info)

## JSON-RPC

You can use any HTTP client (like [RESTED for Firefox](https://addons.mozilla.org/en-US/firefox/addon/rested/), [Postman for Chrome](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) or [Online HTTP client ExtendsClass](https://extendsclass.com/rest-client-online.html)) to make JSON-RPC calls a `rippled` server. Most programming languages have a library for making HTTP requests built in. 

Example JSON-RPC request:


```json
POST http://s1.ripple.com:51234/
Content-Type: application/json

{
    "method": "server_info",
    "params": [
        {
            "api_version": 1
        }
    ]
}
```

The response shows you the current status of the server.

Read more: [Request Formatting >](/docs/references/http-websocket-apis/api-conventions/request-formatting#json-rpc-format) [Response Formatting >](/docs/references/http-websocket-apis/api-conventions/response-formatting) [About the server_info method >](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_info)

## Commandline

The commandline interface connects to the same service as the JSON-RPC one, so the public servers and server configuration are the same. By default, the commandline connects to a `rippled` server running on the same machine.

Example commandline request:


```
rippled --conf=/etc/opt/ripple/rippled.cfg server_info
```

Read more: [Commandline Usage Reference >](/docs/infrastructure/commandline-usage)

The commandline interface is intended for administrative purposes only and is *not a supported API*.  New versions of `rippled` may introduce breaking changes to the commandline API without warning!

## Available Methods

For a full list of API methods, see:

- [Public `rippled` Methods](/docs/references/http-websocket-apis/public-api-methods): Methods available on public servers, including looking up data from the ledger and submitting transactions.
- [Admin `rippled` Methods](/docs/references/http-websocket-apis/admin-api-methods): Methods for [managing](/docs/infrastructure/installation/install-rippled-on-ubuntu) the `rippled` server.


## See Also

- **Concepts:**
  - [XRP Ledger Overview](/about/)
  - [Client Libraries](/docs/references/client-libraries)
  - [Parallel Networks](/docs/concepts/networks-and-servers/parallel-networks)
- **Tutorials:**
  - [Get Started Using JavaScript](/docs/tutorials/http-websocket-apis/build-apps/get-started)
  - [Reliable Transaction Submission](/docs/concepts/transactions/reliable-transaction-submission)
  - [Manage the rippled Server](/docs/infrastructure/installation/install-rippled-on-ubuntu)
- **References:**
  - [rippled API Reference](/docs/references/http-websocket-apis)

  # Monitor Incoming Payments with WebSocket

This tutorial shows how to monitor for incoming [payments](/docs/concepts/payment-types) using the [WebSocket API](/docs/references/http-websocket-apis). Since all XRP Ledger transactions are public, anyone can monitor incoming payments to any address.

WebSocket follows a model where the client and server open one connection, then send messages both ways through the same connection, which stays open until explicitly closed (or until the connection fails). This is in contrast to the HTTP-based API model (including JSON-RPC and RESTful APIs), where the client opens and closes a new connection for each request.[¹](#footnote-1)

The examples in this page use JavaScript so that the examples can run natively in a web browser. If you are developing in JavaScript, you can also use the [xrpl.js library for JavaScript](https://js.xrpl.org/) to simplify some tasks. This tutorial shows how to monitor for transactions *without* using a xrpl.js so that you can translate the steps to other programming languages that don't have a native XRP Ledger client library.

## Prerequisites

- The examples in this page use JavaScript and the WebSocket protocol, which are available in all major modern browsers. If you have some JavaScript knowledge and expertise in another programming language with a WebSocket client, you can follow along while adapting the instructions to the language of your choice.
- You need a stable internet connection and access to an XRP Ledger server. The embedded examples connect to Ripple's pool of public servers. If you [run your own `rippled` or Clio server](/docs/infrastructure/installation), you can also connect to that server locally.
- To properly handle XRP values without rounding errors, you need access to a number type that can do math on 64-bit unsigned integers. The examples in this tutorial use [big.js](https://github.com/MikeMcl/big.js/). If you are working with [tokens](/docs/concepts/tokens), you need even more precision. For more information, see [Currency Precision](/docs/references/protocol/data-types/currency-formats#xrp-precision).


script
script
script

// Helper stuff for this interactive tutorial specifically

function writeToConsole(console_selector, message) {
  let write_msg = "<div class='console-entry'>" + message + "</div>"
  $(console_selector).find(".placeholder").remove()
  $(console_selector).append(write_msg)
  // TODO: JSON pretty-printing, maybe w/ multiple input args?
}

## 1. Connect to the XRP Ledger

The first step of monitoring for incoming payments is to connect to the XRP Ledger, specifically a `rippled` server.

The following JavaScript code connects to one of Ripple's public server clusters. It then logs a message to the console, sends a request using the [ping method](/docs/references/http-websocket-apis/public-api-methods/utility-methods/ping) and sets up a handler to log to the console again when it receives any message from the server side.


```js
const socket = new WebSocket('wss://s.altnet.rippletest.net:51233')
socket.addEventListener('open', (event) => {
  // This callback runs when the connection is open
  console.log("Connected!")
  const command = {
    "id": "on_open_ping_1",
    "command": "ping"
  }
  socket.send(JSON.stringify(command))
})
socket.addEventListener('message', (event) => {
  console.log('Got message from server:', event.data)
})
socket.addEventListener('close', (event) => {
  // Use this event to detect when you have become disconnected
  // and respond appropriately.
  console.log('Disconnected...')
})
```

The above example opens a secure connection (`wss://`) to one of Ripple's public API servers on the [Test Net](/resources/dev-tools/xrp-faucets). To connect to a locally-running `rippled` server with the default configuration instead, open an *unsecured* connection (`ws://`) on port **6006** locally, using the following first line:


```js
const socket = new WebSocket('ws://localhost:6006')
```

By default, connecting to a local `rippled` server gives you access to the full set of [admin methods](/docs/references/http-websocket-apis/admin-api-methods) and admin-only data in some responses such as [server_info](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_info), plus the [public methods](/docs/references/http-websocket-apis/public-api-methods) that are available when you connect to public servers over the internet.

Example:

Connect
Connect
Connection status:
Not connected

h5
Console:
div
span
(Log is empty)
script

let socket;
$("#connect-socket-button").click((event) => {
  socket = new WebSocket('wss://s.altnet.rippletest.net:51233')
  socket.addEventListener('open', (event) => {
    // This callback runs when the connection is open
    writeToConsole("#monitor-console-connect", "Connected!")
    $("#connection-status").text("Connected")
    const command = {
      "id": "on_open_ping_1",
      "command": "ping"
    }
    socket.send(JSON.stringify(command))

    complete_step("Connect")
    $("#connect-button").prop("disabled", "disabled")
    $("#enable_dispatcher").prop("disabled",false)
  })
  socket.addEventListener('close', (event) => {
    $("#connection-status").text("Disconnected")
    $("#connect-button").prop("disabled", false)
  })
  socket.addEventListener('message', (event) => {
    writeToConsole("#monitor-console-connect", "Got message from server: " +
          JSON.stringify(event.data))
  })
})

## 2. Dispatch Incoming Messages to Handlers

Since WebSocket connections can have several messages going each way and there is not a strict 1:1 correlation between requests and responses, you need to identify what to do with each incoming message. A good model for coding this is to set up a "dispatcher" function that reads incoming messages and relays each message to the correct code path for handling it. To help dispatch messages appropriately, the `rippled` server provides a `type` field on every WebSocket message:

- For any message that is a direct response to a request from the client side, the `type` is the string `response`. In this case, the server also provides the following:
  - An `id` field that matches the `id` provided in the request this is a response for. (This is important because responses may arrive out of order.)
  - A `status` field that indicates whether the API successfully processed your request. The string value `success` indicates [a successful response](/docs/references/http-websocket-apis/api-conventions/response-formatting). The string value `error` indicates [an error](/docs/references/http-websocket-apis/api-conventions/error-formatting).
When submitting transactions, a `status` of `success` at the top level of the WebSocket message does not mean that the transaction itself succeeded. It only indicates that the server understood your request. For looking up a transaction's actual outcome, see [Look Up Transaction Results](/docs/concepts/transactions/finality-of-results/look-up-transaction-results).
- For follow-up messages from [subscriptions](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe), the `type` indicates the type of follow-up message it is, such as the notification of a new transaction, ledger, or validation; or a follow-up to an ongoing [pathfinding request](/docs/references/http-websocket-apis/public-api-methods/path-and-order-book-methods/path_find). Your client only receives these messages if it subscribes to them.


The [xrpl.js library for JavaScript](https://js.xrpl.org/) handles this step by default. All asynchronous API requests use Promises to provide the response, and you can listen to streams using the `.on(event, callback)` method of the `Client`.

The following JavaScript code defines a helper function to make API requests into convenient asynchronous [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises), and sets up an interface to map other types of messages to global handlers:


```js
const AWAITING = {}
const handleResponse = function(data) {
  if (!data.hasOwnProperty("id")) {
    console.error("Got response event without ID:", data)
    return
  }
  if (AWAITING.hasOwnProperty(data.id)) {
    AWAITING[data.id].resolve(data)
  } else {
    console.warn("Response to un-awaited request w/ ID " + data.id)
  }
}

let autoid_n = 0
function api_request(options) {
  if (!options.hasOwnProperty("id")) {
    options.id = "autoid_" + (autoid_n++)
  }

  let resolveHolder;
  AWAITING[options.id] = new Promise((resolve, reject) => {
    // Save the resolve func to be called by the handleResponse function later
    resolveHolder = resolve
    try {
      // Use the socket opened in the previous example...
      socket.send(JSON.stringify(options))
    } catch(error) {
      reject(error)
    }
  })
  AWAITING[options.id].resolve = resolveHolder;
  return AWAITING[options.id]
}

const WS_HANDLERS = {
  "response": handleResponse
  // Fill this out with your handlers in the following format:
  // "type": function(event) { /* handle event of this type */ }
}
socket.addEventListener('message', (event) => {
  const parsed_data = JSON.parse(event.data)
  if (WS_HANDLERS.hasOwnProperty(parsed_data.type)) {
    // Call the mapped handler
    WS_HANDLERS[parsed_data.type](parsed_data)
  } else {
    console.log("Unhandled message from server", event)
  }
})

// Show api_request functionality
async function pingpong() {
  console.log("Ping...")
  const response = await api_request({command: "ping"})
  console.log("Pong!", response)
}
// Add pingpong() to the 'open' listener for socket
```

Dispatch Messages
Enable Dispatcher
Ping!

h5
Responses
div
span
(Log is empty)
script

const AWAITING = {}
const handleResponse = function(data) {
  if (!data.hasOwnProperty("id")) {
    writeToConsole("#monitor-console-ping", "Got response event without ID:", data)
    return
  }
  if (AWAITING.hasOwnProperty(data.id)) {
    AWAITING[data.id].resolve(data)
  } else {
    writeToConsole("#monitor-console-ping", "Response to un-awaited request w/ ID " + data.id)
  }
}

let autoid_n = 0
function api_request(options) {
  if (!options.hasOwnProperty("id")) {
    options.id = "autoid_" + (autoid_n++)
  }
  let resolveFunc;
  AWAITING[options.id] = new Promise((resolve, reject) => {
    // Save the resolve func to be called by the handleResponse function later
    resolveFunc = resolve
    try {
      // Use the socket opened in the previous example...
      socket.send(JSON.stringify(options))
    } catch(error) {
      reject(error)
    }
  })
  AWAITING[options.id].resolve = resolveFunc
  return AWAITING[options.id]
}

const WS_HANDLERS = {
  "response": handleResponse
}
$("#enable_dispatcher").click((clickEvent) => {
  socket.addEventListener('message', (event) => {
    const parsed_data = JSON.parse(event.data)
    if (WS_HANDLERS.hasOwnProperty(parsed_data.type)) {
      // Call the mapped handler
      WS_HANDLERS[parsed_data.type](parsed_data)
    } else {
      writeToConsole("#monitor-console-ping", "Unhandled message from server: " + event)
    }
  })
  complete_step("Dispatch Messages")
  $("#dispatch_ping").prop("disabled", false)
  $("#tx_subscribe").prop("disabled", false)
})

async function pingpong() {
  const response = await api_request({command: "ping"})
  writeToConsole("#monitor-console-ping", "Pong! " + JSON.stringify(response))
}

$("#dispatch_ping").click((event) => {
  pingpong()
})

## 3. Subscribe to the Account

To get a live notification whenever a transaction affects your account, you can subscribe to the account with the [subscribe method](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe). In fact, it doesn't have to be your own account: since all transactions are public, you can subscribe to any account or even a combination of accounts.

After you subscribe to one or more accounts, the server sends a message with `"type": "transaction"` on each *validated* transaction that affects any of the specified accounts in some way. To confirm this, look for `"validated": true` in the transaction messages.

The following code sample subscribes to the Test Net Faucet's sending address. It logs a message on each such transaction by adding a handler to the dispatcher from the previous step.


```js
async function do_subscribe() {
  const sub_response = await api_request({
    command:"subscribe",
    accounts: ["rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe"]
  })
  if (sub_response.status === "success") {
    console.log("Successfully subscribed!")
  } else {
    console.error("Error subscribing: ", sub_response)
  }
}
// Add do_subscribe() to the 'open' listener for socket

const log_tx = function(tx) {
  console.log(tx.transaction.TransactionType + " transaction sent by " +
              tx.transaction.Account +
              "\n  Result: " + tx.meta.TransactionResult +
              " in ledger " + tx.ledger_index +
              "\n  Validated? " + tx.validated)
}
WS_HANDLERS["transaction"] = log_tx
```

For the following example, try opening the [Transaction Sender](/resources/dev-tools/tx-sender) in a different window or even on a different device and sending transactions to the address you subscribed to:

Subscribe
Test Net Address:

Subscribe

h5
Transactions
div
span
(Log is empty)
script

async function do_subscribe() {
  const sub_address = $("#subscribe_address").val()
  const sub_response = await api_request({
    command:"subscribe",
    accounts: [sub_address]
  })
  if (sub_response.status === "success") {
    writeToConsole("#monitor-console-subscribe", "Successfully subscribed!")
  } else {
    writeToConsole("#monitor-console-subscribe",
                   "Error subscribing: " + JSON.stringify(sub_response))
  }
}
$("#tx_subscribe").click((event) => {
  do_subscribe()
  complete_step("Subscribe")
  $("#tx_read").prop("disabled", false)
})

const log_tx = function(tx) {
  writeToConsole("#monitor-console-subscribe",
                  tx.transaction.TransactionType + " transaction sent by " +
                  tx.transaction.Account +
                  "<br/>&nbsp;&nbsp;Result: " + tx.meta.TransactionResult +
                  " in ledger " + tx.ledger_index +
                  "<br/>&nbsp;&nbsp;Validated? " + tx.validated)
}
WS_HANDLERS["transaction"] = log_tx

## 4. Read Incoming Payments

When you subscribe to an account, you get messages for *all transactions to or from the account*, as well as *transactions that affect the account indirectly*, such as trading its [tokens](/docs/concepts/tokens). If your goal is to recognize when the account has received incoming payments, you must filter the transactions stream and process the payments based on the amount they actually delivered. Look for the following information:

- The **`validated` field** indicates that the transaction's outcome is [final](/docs/concepts/transactions/finality-of-results). This should always be the case when you subscribe to `accounts`, but if you *also* subscribe to `accounts_proposed` or the `transactions_proposed` stream then the server sends similar messages on the same connection for unconfirmed transactions. As a precaution, it's best to always check the `validated` field.
- The **`meta.TransactionResult` field** is the [transaction result](/docs/references/protocol/transactions/transaction-results). If the result is not `tesSUCCESS`, the transaction failed and cannot have delivered any value.
- The **`transaction.Account`** field is the sender of the transaction. If you are only looking for transactions sent by others, you can ignore any transactions where this field matches your account's address. (Keep in mind, it *is* possible to make a cross-currency payment to yourself.)
- The **`transaction.TransactionType` field** is the type of transaction. The transaction types that can possibly deliver currency to an account are as follows:
  - **[Payment transactions](/docs/references/protocol/transactions/types/payment)** can deliver XRP or [tokens](/docs/concepts/tokens). Filter these by the `transaction.Destination` field, which contains the address of the recipient, and always use the `meta.delivered_amount` to see how much the payment actually delivered. XRP amounts are [formatted as strings](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts).
If you use the `transaction.Amount` field instead, you may be vulnerable to the [partial payments exploit](/docs/concepts/payment-types/partial-payments#partial-payments-exploit). Malicious users can use this exploit to trick you into allowing the malicious user to trade or withdraw more money than they paid you.
  - **[CheckCash transactions](/docs/references/protocol/transactions/types/checkcash)** allow an account to receive money authorized by a different account's [CheckCreate transaction](/docs/references/protocol/transactions/types/checkcreate). Look at the metadata of a **CheckCash transaction** to see how much currency the account received.
  - **[EscrowFinish transactions](/docs/references/protocol/transactions/types/escrowfinish)** can deliver XRP by finishing an [Escrow](/docs/concepts/payment-types/escrow) created by a previous [EscrowCreate transaction](/docs/references/protocol/transactions/types/escrowcreate). Look at the metadata of the **EscrowFinish transaction** to see which account received XRP from the escrow and how much.
  - **[OfferCreate transactions](/docs/references/protocol/transactions/types/offercreate)** can deliver XRP or tokens by consuming offers your account has previously placed in the XRP Ledger's [decentralized exchange](/docs/concepts/tokens/decentralized-exchange). If you never place offers, you cannot receive money this way. Look at the metadata to see what currency the account received, if any, and how much.
  - **[PaymentChannelClaim transactions](/docs/references/protocol/transactions/types/paymentchannelclaim)** can deliver XRP from a [payment channel](/docs/concepts/payment-types/payment-channels). Look at the metadata to see which accounts, if any, received XRP from the transaction.
  - **[PaymentChannelFund transactions](/docs/references/protocol/transactions/types/paymentchannelfund)** can return XRP from a closed (expired) payment channel to the sender.
- The **`meta` field** contains [transaction metadata](/docs/references/protocol/transactions/metadata), including exactly how much of which currency or currencies was delivered where. See [Look Up transaction Results](/docs/concepts/transactions/finality-of-results/look-up-transaction-results) for more information on how to understand transaction metadata.


The following sample code looks at transaction metadata of all the above transaction types to report how much XRP an account received:

function CountXRPDifference(affected_nodes, address) {
  // Helper to find an account in an AffectedNodes array and see how much
  // its balance changed, if at all. Fortunately, each account appears at most
  // once in the AffectedNodes array, so we can return as soon as we find it.

  // Note: this reports the net balance change. If the address is the sender,
  // the transaction cost is deducted and combined with XRP sent/received

  for (let i=0; i<affected_nodes.length; i++) {
    if ((affected_nodes[i].hasOwnProperty("ModifiedNode"))) {
      // modifies an existing ledger entry
      let ledger_entry = affected_nodes[i].ModifiedNode
      if (ledger_entry.LedgerEntryType === "AccountRoot" &&
          ledger_entry.FinalFields.Account === address) {
        if (!ledger_entry.PreviousFields.hasOwnProperty("Balance")) {
          console.log("XRP balance did not change.")
        }
        // Balance is in PreviousFields, so it changed. Time for
        // high-precision math!
        const old_balance = new Big(ledger_entry.PreviousFields.Balance)
        const new_balance = new Big(ledger_entry.FinalFields.Balance)
        const diff_in_drops = new_balance.minus(old_balance)
        const xrp_amount = diff_in_drops.div(1e6)
        if (xrp_amount.gte(0)) {
          console.log("Received " + xrp_amount.toString() + " XRP.")
          return
        } else {
          console.log("Spent " + xrp_amount.abs().toString() + " XRP.")
          return
        }
      }
    } else if ((affected_nodes[i].hasOwnProperty("CreatedNode"))) {
      // created a ledger entry. maybe the account just got funded?
      let ledger_entry = affected_nodes[i].CreatedNode
      if (ledger_entry.LedgerEntryType === "AccountRoot" &&
          ledger_entry.NewFields.Account === address) {
        const balance_drops = new Big(ledger_entry.NewFields.Balance)
        const xrp_amount = balance_drops.div(1e6)
        console.log("Received " + xrp_amount.toString() + " XRP (account funded).")
        return
      }
    } // accounts cannot be deleted at this time, so we ignore DeletedNode
  }

  console.log("Did not find address in affected nodes.")
  return
}

function CountXRPReceived(tx, address) {
  if (tx.meta.TransactionResult !== "tesSUCCESS") {
    console.log("Transaction failed.")
    return
  }
  if (tx.tx_json.TransactionType === "Payment") {
    if (tx.tx_json.Destination !== address) {
      console.log("Not the destination of this payment.")
      return
    }
    if (typeof tx.meta.delivered_amount === "string") {
      const amount_in_drops = new Big(tx.meta.delivered_amount)
      const xrp_amount = amount_in_drops.div(1e6)
      console.log("Received " + xrp_amount.toString() + " XRP.")
      return
    } else {
      console.log("Received non-XRP currency.")
      return
    }
  } else if (["PaymentChannelClaim", "PaymentChannelFund", "OfferCreate",
          "CheckCash", "EscrowFinish"].includes(
          tx.tx_json.TransactionType)) {
    CountXRPDifference(tx.meta.AffectedNodes, address)
  } else {
    console.log("Not a currency-delivering transaction type (" +
                tx.tx_json.TransactionType + ").")
  }
}

Read Payments
Start Reading

h5
Transactions
div
span
(Log is empty)
script

function CountXRPDifference(affected_nodes, address) {
  // Helper to find an account in an AffectedNodes array and see how much
  // its balance changed, if at all. Fortunately, each account appears at most
  // once in the AffectedNodes array, so we can return as soon as we find it.

  // Note: this reports the net balance change. If the address is the sender,
  // any XRP balance changes combined with the transaction cost.

  for (let i=0; i<affected_nodes.length; i++) {
    if ((affected_nodes[i].hasOwnProperty("ModifiedNode"))) {
      // modifies an existing ledger entry
      let ledger_entry = affected_nodes[i].ModifiedNode
      if (ledger_entry.LedgerEntryType === "AccountRoot" &&
          ledger_entry.FinalFields.Account === address) {
        if (!ledger_entry.PreviousFields.hasOwnProperty("Balance")) {
          writeToConsole("#monitor-console-read", "XRP balance did not change.")
        }
        // Balance is in PreviousFields, so it changed. Time for
        // high-precision math!
        const old_balance = new Big(ledger_entry.PreviousFields.Balance)
        const new_balance = new Big(ledger_entry.FinalFields.Balance)
        const diff_in_drops = new_balance.minus(old_balance)
        const xrp_amount = diff_in_drops.div(1e6)
        if (xrp_amount.gte(0)) {
          writeToConsole("#monitor-console-read", "Received " + xrp_amount.toString()+" XRP.")
          return
        } else {
          writeToConsole("#monitor-console-read", "Spent " + xrp_amount.abs().toString() + " XRP.")
          return
        }
      }
    } else if ((affected_nodes[i].hasOwnProperty("CreatedNode"))) {
      // created a ledger entry. maybe the account got funded?
      let ledger_entry = affected_nodes[i].CreatedNode
      if (ledger_entry.LedgerEntryType === "AccountRoot" &&
          ledger_entry.NewFields.Account === address) {
        const balance_drops = new Big(ledger_entry.NewFields.Balance)
        const xrp_amount = balance_drops.div(1e6)
        writeToConsole("#monitor-console-read", "Received " + xrp_amount.toString() + " XRP (account funded).")
        return
      }
    } // accounts cannot be deleted at this time, so we ignore DeletedNode
  }

  writeToConsole("#monitor-console-read", "Did not find address in affected nodes.")
  return
}

function CountXRPReceived(tx, address) {
  if (tx.meta.TransactionResult !== "tesSUCCESS") {
    writeToConsole("#monitor-console-read", "Transaction failed.")
    return
  }
  if (tx.transaction.TransactionType === "Payment") {
    if (tx.transaction.Destination !== address) {
      writeToConsole("#monitor-console-read", "Not the destination of this payment. (We're " +
                      address + "; they're " + tx.transaction.Destination + ")")
      return
    }
    if (typeof tx.meta.delivered_amount === "string") {
      const amount_in_drops = new Big(tx.meta.delivered_amount)
      const xrp_amount = amount_in_drops.div(1e6)
      writeToConsole("#monitor-console-read", "Received " + xrp_amount.toString() + " XRP.")
      return
    } else {
      writeToConsole("#monitor-console-read", "Received non-XRP currency.")
      return
    }
  } else if (["PaymentChannelClaim", "PaymentChannelFund", "OfferCreate",
          "CheckCash", "EscrowFinish"].includes(
          tx.transaction.TransactionType)) {
    CountXRPDifference(tx.meta.AffectedNodes, address)
  } else {
    writeToConsole("#monitor-console-read", "Not a currency-delivering transaction type (" +
                tx.transaction.TransactionType + ").")
  }
}

$("#tx_read").click((event) => {
  // Wrap the existing "transaction" handler to do the old thing and also
  // do the CountXRPReceived thing
  const sub_address = $("#subscribe_address").val()
  const old_handler = WS_HANDLERS["transaction"]
  const new_handler = function(data) {
    old_handler(data)
    CountXRPReceived(data, sub_address)
  }
  WS_HANDLERS["transaction"] = new_handler
  // Disable the button so you can't stack up multiple levels of the new handler
  $("#tx_read").prop("disabled", "disabled")
  complete_step("Read Payments")
})

## Next Steps

- [Look Up Transaction Results](/docs/concepts/transactions/finality-of-results/look-up-transaction-results) to see exactly what a transaction did, and build your software to react appropriately.
- Try [Sending XRP](/docs/tutorials/how-tos/send-xrp) from your own address.
- Try monitoring for transactions of advanced types like [Escrows](/docs/concepts/payment-types/escrow), [Checks](/docs/concepts/payment-types/checks), or [Payment Channels](/docs/concepts/payment-types/payment-channels), and responding to incoming notifications.


## Other Programming Languages

Many programming languages have libraries for sending and receiving data over a WebSocket connection. If you want a head-start on communicating with `rippled`'s WebSocket API in a language other than JavaScript, the following examples show how:

Go
package main

// Connect to the XRPL Ledger using websocket and subscribe to an account
// translation from the JavaScript example to Go
// https://xrpl.org/monitor-incoming-payments-with-websocket.html
// This example uses the Gorilla websocket library to create a websocket client
// install: go get github.com/gorilla/websocket

import (
    "encoding/json"
    "flag"
    "log"
    "net/url"
    "os"
    "os/signal"
    "time"

    "github.com/gorilla/websocket"
)

// websocket address
var addr = flag.String("addr", "s.altnet.rippletest.net:51233", "http service address")

// Payload object
type message struct {
    Command  string   `json:"command"`
    Accounts []string `json:"accounts"`
}

func main() {
    flag.Parse()
    log.SetFlags(0)

    var m message

    // check for interrupts and cleanly close the connection
    interrupt := make(chan os.Signal, 1)
    signal.Notify(interrupt, os.Interrupt)

    u := url.URL{Scheme: "ws", Host: *addr, Path: "/"}
    log.Printf("connecting to %s", u.String())

    // make the connection
    c, _, err := websocket.DefaultDialer.Dial(u.String(), nil)
    if err != nil {
        panic(err)
    }
    // on exit close
    defer c.Close()

    done := make(chan struct{})

    // send a subscribe command and a target XRPL account
    m.Command = "subscribe"
    m.Accounts = append(m.Accounts, "rUCzEr6jrEyMpjhs4wSdQdz4g8Y382NxfM")

    // struct to JSON marshalling
    msg, _ := json.Marshal(m)
    // write to the websocket
    err = c.WriteMessage(websocket.TextMessage, []byte(string(msg)))
    if err != nil {
        panic(err)
    }

    // read from the websocket
    _, message, err := c.ReadMessage()
    if err != nil {
        panic(err)
    }
    // print the response from the XRP Ledger
    log.Printf("recv: %s", message)

    // handle interrupt
    for {
        select {
        case <-done:
            return
        case <-interrupt:
            log.Println("interrupt")

            // Cleanly close the connection by sending a close message and then
            // waiting (with timeout) for the server to close the connection.
            err := c.WriteMessage(websocket.CloseMessage, websocket.FormatCloseMessage(websocket.CloseNormalClosure, ""))
            if err != nil {
                panic(err)
            }
            select {
            case <-done:
            case <-time.After(time.Second):
            }
            return
        }
    }
}

Python
import asyncio
import websockets
import json

# Using client libraries for ASYNC functions and websockets are needed in python.
# To install, use terminal command 'pip install asyncio && pip install websockets'

# Handles incoming messages
async def handler(websocket):
    message = await websocket.recv()
    return message

# Use this to send API requests
async def api_request(options, websocket):
    try:
        await websocket.send(json.dumps(options))
        message = await websocket.recv()
        return json.loads(message)
    except Exception as e:
        return e

# Tests functionality of API_Requst
async def pingpong(websocket):
    command = {
        "id": "on_open_ping_1",
        "command": "ping"
    }
    value = await api_request(command, websocket)
    print(value)

async def do_subscribe(websocket):
    command = await api_request({
        'command': 'subscribe',
        'accounts': ['rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe']
        }, websocket)

    if command['status'] == 'success':
        print('Successfully Subscribed!')
    else:
        print("Error subscribing: ", command)
    print('Received message from server', await handler(websocket))


async def run():
    # Opens connection to ripple testnet
    async for websocket in websockets.connect('wss://s.altnet.rippletest.net:51233'):
        try:
           await pingpong(websocket)
           await do_subscribe(websocket)
        except websockets.ConnectionClosed:
            print('Disconnected...')

# Runs the webhook on a loop
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
    print('Restarting Loop')

if __name__ == '__main__':
    main()
Don't see the programming language of your choice? Click the "Edit on GitHub" link at the top of this page and contribute your own sample code!

## Footnotes

[1.](#from-footnote-1)  In practice, when calling an HTTP-based API multiple times, the client and server may reuse the same connection for several requests and responses. This practice is called [HTTP persistent connection, or keep-alive](https://en.wikipedia.org/wiki/HTTP_persistent_connection). From a development standpoint, the code to use an HTTP-based API is the same regardless of whether the underlying connection is new or reused.

## See Also

- **Concepts:**
  - [Transactions](/docs/concepts/transactions)
  - [Finality of Results](/docs/concepts/transactions/finality-of-results) - How to know when a transaction's success or failure is final. (Short version: if a transaction is in a validated ledger, its outcome and metadata are final.)
- **Tutorials:**
  - [Reliable Transaction Submission](/docs/concepts/transactions/reliable-transaction-submission)
  - [Look Up Transaction Results](/docs/concepts/transactions/finality-of-results/look-up-transaction-results)
- **References:**
  - [Transaction Types](/docs/references/protocol/transactions/types)
  - [Transaction Metadata](/docs/references/protocol/transactions/metadata) - Summary of the metadata format and fields that appear in metadata
  - [Transaction Results](/docs/references/protocol/transactions/transaction-results) - Tables of all possible result codes for transactions.



Public API Methods
Copy

Communicate directly with an XRP Ledger server using the public API methods. Public methods are not necessarily meant for the general public, but they are used by any client attached to the server. Think of public methods as being for members or customers of the organization running the server.

Account Methods
An account in the XRP Ledger represents a holder of XRP and a sender of transactions. Use these methods to work with account info.

account_channels - Get a list of payment channels where the account is the source of the channel.
account_currencies - Get a list of currencies an account can send or receive.
account_info - Get basic data about an account.
account_lines - Get info about an account's trust lines.
account_nfts - Get a list of non-fungible tokens owned by an account.
account_objects - Get all ledger objects owned by an account.
account_offers - Get info about an account's currency exchange offers.
account_tx - Get info about an account's transactions.
gateway_balances - Calculate total amounts issued by an account.
noripple_check - Get recommended changes to an account's Default Ripple and No Ripple settings.
Ledger Methods
A ledger version contains a header, a transaction tree, and a state tree, which contain account settings, trust lines, balances, transactions, and other data. Use these methods to retrieve ledger info.

ledger - Get info about a ledger version.
ledger_closed - Get the latest closed ledger version.
ledger_current - Get the current working ledger version.
ledger_data - Get the raw contents of a ledger version.
ledger_entry - Get one element from a ledger version.
Transaction Methods
Transactions are the only thing that can modify the shared state of the XRP Ledger. All business on the XRP Ledger takes the form of transactions. Use these methods to work with transactions.

submit - Send a transaction to the network.
submit_multisigned - Send a multi-signed transaction to the network.
transaction_entry - Retrieve info about a transaction from a particular ledger version.
tx - Retrieve info about a transaction from all the ledgers on hand.
By default, the following methods are admin-only. They can be used as public methods if the server admin has enabled public signing.

sign - Cryptographically sign a transaction.
sign_for - Contribute to a multi-signature.
Path and Order Book Methods
Paths define a way for payments to flow through intermediary steps on their way from sender to receiver. Paths enable cross-currency payments by connecting sender and receiver through order books. Use these methods to work with paths and other books.

amm_info - Get info about an Automated Market Maker (AMM).
book_offers - Get info about offers to exchange two currencies.
deposit_authorized - Look up whether one account is authorized to send payments directly to another.
nft_buy_offers - Retrieve a list of buy offers for a specified NFToken object.
nft_sell_offers - Retrieve a list of sell offers for a specified NFToken object.
path_find - Find a path for a payment between two accounts and receive updates.
ripple_path_find - Find a path for payment between two accounts, once.
Payment Channel Methods
Payment channels are a tool for facilitating repeated, unidirectional payments, or temporary credit between two parties. Use these methods to work with payment channels.

channel_verify - Check a payment channel claim's signature.
By default, the following method is admin-only. It can be used as a public method if the server admin has enabled public signing.

channel_authorize - Sign a claim for money from a payment channel.
Subscription Methods
Use these methods to enable the server to push updates to your client when various events happen, so that you can know and react right away. WebSocket API only.

subscribe - Listen for updates about a particular subject.
unsubscribe - Stop listening for updates about a particular subject.
Server Info Methods
Use these methods to retrieve information about the current state of the rippled server.

fee - Get information about transaction cost.
feature - Returns information about amendments this server knows about.
server_info - Retrieve status of the server in human-readable format.
server_state - Retrieve status of the server in machine-readable format.
server_definitions - Retrieve a list of types and fields used for the XRPL's canonical binary format.
manifest - Retrieve the latest ephemeral public key information about a known validator.
Clio Methods
Use these methods to retrieve information using Clio server APIs.

server_info - Retrieve status of the Clio server.
ledger - Get info about a ledger version using Clio server's ledger API.
nft_info - Retrieve information about the specified NFT using Clio server's nft_info API.
nft_history - Retrieve the history of ownership and transfers for the specified NFT.
nfts_by_issuer - Returns a list of NFTokens that are issued by the specified account.
Utility Methods
Use these methods to perform convenient tasks, such as ping and random number generation.

json - Use as a proxy to running other commands. Accepts the parameters for the command as a JSON value. Commandline only.
ping - Confirm connectivity with the server.
random - Generate a random number.
Vault Methods
Use these methods to retrieve vault information.

vault_info - Get information about a specific vault.
Deprecated Methods
The following methods are deprecated and either have been removed, or may be removed without further notice:

owner_info - Use account_objects instead.
tx_history - Use either the account_tx method, or the ledger method with the transactions field set to true.


# Account Methods

An account in the XRP Ledger represents a holder of XRP and a sender of transactions. Use these methods to work with account info.



# Ledger Methods

A ledger version contains a header, a transaction tree, and a state tree, which contain account settings, trustlines, balances, transactions, and other data. Use these methods to retrieve ledger info.



# Transaction Methods

Transactions are the only thing that can modify the shared state of the XRP Ledger. All business on the XRP Ledger takes the form of transactions. Use these methods to work with transactions.



# Path and Order Book Methods

Paths define a way for payments to flow through intermediary steps on their way from sender to receiver. Paths enable cross-currency payments by connecting sender and receiver through order books. Use these methods to work with paths and other books.

# amm_info

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/AMMInfo.cpp)

The  method gets information about an [Automated Market Maker (AMM)](/docs/concepts/tokens/decentralized-exchange/automated-market-makers) instance.

AMM
### Request Format

An example of the request format:

Note
There is no commandline syntax for this method. You can use the [json method](/docs/references/http-websocket-apis/public-api-methods/utility-methods/json) to access this method from the commandline instead.

WebSocket

```json
{
    "command": "",
    "asset": {
      "currency": "XRP"
    },
    "asset2": {
      "currency": "TST",
      "issuer": "rP9jPyP5kyvFRb6ZiRghAGw5u8SGAmU4bd"
    }
}
```

JSON-RPC

```json
{
    "method": "",
    "params": [{
      "asset": {
        "currency": "XRP"
      },
      "asset2": {
        "currency": "TST",
        "issuer": "rP9jPyP5kyvFRb6ZiRghAGw5u8SGAmU4bd"
      }
    }]
}
```

The request includes the following parameters:

| `Field` | Type | Required? | Description |
|  --- | --- | --- | --- |
| `account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | No | Show only LP Tokens held by this liquidity provider. |
| `amm_account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | No | The address of the AMM's special AccountRoot. (This is the `issuer` of the AMM's LP Tokens.) |
| `asset` | Object | No | One of the assets of the AMM to look up, as an object with `currency` and `issuer` fields (omit `issuer` for XRP), like [currency amounts](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts). |
| `asset2` | Object | No | The other of the assets of the AMM, as an object with `currency` and `issuer` fields (omit `issuer` for XRP), like [currency amounts](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts). |


You must specify *either* `amm_account` or both `asset` and `asset2`.

### Response Format

An example of a successful response:

WebSocket

```json
{
  "result": {
    "amm": {
      "account": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
      "amount": "296890496",
      "amount2": {
        "currency": "TST",
        "issuer": "rP9jPyP5kyvFRb6ZiRghAGw5u8SGAmU4bd",
        "value": "25.81656470648473"
      },
      "asset2_frozen": false,
      "auction_slot": {
        "account": "rJVUeRqDFNs2xqA7ncVE6ZoAhPUoaJJSQm",
        "auth_accounts": [
          {
            "account": "r3f2WpQMsAd8k4Zoijv2PZ78EYFJ2EdvgV"
          },
          {
            "account": "rnW8FAPgpQgA6VoESnVrUVJHBdq9QAtRZs"
          }
        ],
        "discounted_fee": 60,
        "expiration": "2023-Jan-26 00:28:40.000000000 UTC",
        "price": {
          "currency": "039C99CD9AB0B70B32ECDA51EAAE471625608EA2",
          "issuer": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
          "value": "0"
        },
        "time_interval": 0
      },
      "lp_token": {
        "currency": "039C99CD9AB0B70B32ECDA51EAAE471625608EA2",
        "issuer": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
        "value": "87533.41976112682"
      },
      "trading_fee": 600,
      "vote_slots": [
        {
          "account": "rJVUeRqDFNs2xqA7ncVE6ZoAhPUoaJJSQm",
          "trading_fee": 600,
          "vote_weight": 9684
        }
      ]
    },
    "ledger_current_index": 316725,
    "validated": false
  },
  "status": "success",
  "type": "response"
}
```

JSON-RPC

```json
200 OK

{
  "result": {
    "amm": {
      "account": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
      "amount": "296890496",
      "amount2": {
        "currency": "TST",
        "issuer": "rP9jPyP5kyvFRb6ZiRghAGw5u8SGAmU4bd",
        "value": "25.81656470648473"
      },
      "asset2_frozen": false,
      "auction_slot": {
        "account": "rJVUeRqDFNs2xqA7ncVE6ZoAhPUoaJJSQm",
        "auth_accounts": [
          {
            "account": "r3f2WpQMsAd8k4Zoijv2PZ78EYFJ2EdvgV"
          },
          {
            "account": "rnW8FAPgpQgA6VoESnVrUVJHBdq9QAtRZs"
          }
        ],
        "discounted_fee": 0,
        "expiration": "2023-Jan-26 00:28:40.000000000 UTC",
        "price": {
          "currency": "039C99CD9AB0B70B32ECDA51EAAE471625608EA2",
          "issuer": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
          "value": "0"
        },
        "time_interval": 0
      },
      "lp_token": {
        "currency": "039C99CD9AB0B70B32ECDA51EAAE471625608EA2",
        "issuer": "rp9E3FN3gNmvePGhYnf414T2TkUuoxu8vM",
        "value": "87533.41976112682"
      },
      "trading_fee": 600,
      "vote_slots": [
        {
          "account": "rJVUeRqDFNs2xqA7ncVE6ZoAhPUoaJJSQm",
          "trading_fee": 600,
          "vote_weight": 9684
        }
      ]
    },
    "ledger_current_index": 316745,
    "status": "success",
    "validated": false
  }
}
```

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting), with a successful result containing the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `amm` | Object | An [**AMM Description Object**](#amm-description-object) for the requested asset pair. |
| `ledger_current_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Omitted if `ledger_index` is provided instead)* The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the current in-progress ledger, which was used when retrieving this information. |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | *(Omitted if `ledger_current_index` is provided instead)* The identifying hash of the ledger version that was used when retrieving this data. |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Omitted if `ledger_current_index` is provided instead)* The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the ledger version used when retrieving this information. |
| `validated` | Boolean | If `true`, the ledger used for this request is validated and these results are final; if omitted or set to `false`, the data is pending and may change. |


### AMM Description Object

The `amm` field is an object describing the current status of an Automated Market Maker (AMM) in the ledger, and contains the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `account` | String | The [Address](/docs/references/protocol/data-types/basic-data-types#addresses) of the AMM Account. |
| `amount` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | The total amount of one asset in the AMM's pool. (Note: This could be `asset` *or* `asset2` from the request.) |
| `amount2` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | The total amount of the other asset in the AMM's pool. (Note: This could be `asset` *or* `asset2` from the request.) |
| `asset_frozen` | Boolean | *(Omitted for XRP)* If `true`, the `amount` currency is currently [frozen](/docs/concepts/tokens/fungible-tokens/freezes). |
| `asset2_frozen` | Boolean | *(Omitted for XRP)* If `true`, the `amount2` currency is currently [frozen](/docs/concepts/tokens/fungible-tokens/freezes). |
| `auction_slot` | Object | *(May be omitted)* An [Auction Slot Object](#auction-slot-object) describing the current auction slot holder, if there is one. |
| `lp_token` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | The total amount of this AMM's LP Tokens outstanding. If the request specified a liquidity provider in the `account` field, instead, this is the amount of this AMM's LP Tokens held by that liquidity provider. |
| `trading_fee` | Number | The AMM's current trading fee, in units of 1/100,000; a value of 1 is equivalent to a 0.001% fee. |
| `vote_slots` | Array | *(May be omitted)* The current votes for the AMM's trading fee, as [Vote Slot Objects](#vote-slot-objects). |


### Auction Slot Object

The `auction_slot` field of the `amm` object describes the current auction slot holder of the AMM, and contains the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `account` | String | The [Address](/docs/references/protocol/data-types/basic-data-types#addresses) of the account that owns the auction slot. |
| `auth_accounts` | Array | A list of additional accounts that the auction slot holder has designated as being eligible of the discounted trading fee. Each member of this array is an object with one field, `account`, containing the address of the designated account. |
| `discounted_fee` | Number | The discounted trading fee that applies to the auction slot holder, and any eligible accounts, when trading against this AMM. This is 1/10 of the AMM's normal trading fee. |
| `expiration` | String | The ISO 8601 UTC timestamp after which this auction slot expires. After expired, the auction slot does not apply (but the data can remain in the ledger until another transaction replaces it or cleans it up). |
| `price` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | The amount, in LP Tokens, that the auction slot holder paid to win the auction slot. This affects the price to outbid the current slot holder. |
| `time_interval` | Number | The current 72-minute time interval this auction slot is in, from 0 to 19. The auction slot expires after 24 hours (20 intervals of 72 minutes) and affects the cost to outbid the current holder and how much the current holder is refunded if someone outbids them. |


### Vote Slot Objects

Each entry in the `vote_slots` array represents one liquidity provider's vote to set the trading fee, and contains the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `account` | String | The [Address](/docs/references/protocol/data-types/basic-data-types#addresses) of this liquidity provider. |
| `trading_fee` | Number | The trading fee this liquidity provider voted for, in units of 1/100,000. |
| `vote_weight` | Number | How much this liquidity provider's vote counts towards the final trading fee. This is proportional to how much of the AMM's LP Tokens this liquidity provider holds. The value is equal to 100,000 times the number of this LP Tokens this liquidity provider holds, divided by the total number of LP Tokens outstanding. For example, a value of 1000 means that the liquidity provider holds 1% of this AMM's LP Tokens. |


### Possible Errors

- Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
- `actNotFound` - The AMM for this asset pair does not exist, or an account specified in the request does not exist.
- `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.


## See Also

- [AMM object](/docs/references/protocol/ledger-data/ledger-entry-types/amm) - The canonical storage format of the AMM object
- [AMMBid](/docs/references/protocol/transactions/types/ammbid) - More info on the auction slot and bidding mechanism
- [AMMVote](/docs/references/protocol/transactions/types/ammvote) - More info on the trading fee voting mechanism





# book_changes

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/BookChanges.h)

The  method reports information about changes to the order books in the [decentralized exchange (DEX)](/docs/concepts/tokens/decentralized-exchange) compared with the previous ledger version. This may be useful for building "candlestick" charts.

### Request Format

An example of the request format:

WebSocket

```json
{
    "id": "example_book_changes",
    "command": "",
    "ledger_index": 88530953
}
```

JSON-RPC

```json
{
    "method": "",
    "params": [{
      "ledger_index": 88530953
    }]
}
```

Commandline

```sh
#Syntax: book_changes [<ledger hash|id>]
rippled book_changes 88530953
```

The request includes the following parameters:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | A 32-byte hex string for the ledger version to use. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | No | The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the ledger to use, or a shortcut string to choose a ledger automatically. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |


## Response Format

An example of a successful response:

WebSocket
{
    "result": {
      "type": "bookChanges",
      "ledger_hash": "7AB08A2415C10E07201521F3260F77ADFF4902A528EA66378E259A07767A24B9",
      "ledger_index": 88530953,
      "ledger_time": 771100891,
      "validated": true,
      "changes": [
        {
          "currency_a": "XRP_drops",
          "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
          "volume_a": "44082741",
          "volume_b": "158.6978676",
          "high": "277777.7777777778",
          "low": "277777.7777777778",
          "open": "277777.7777777778",
          "close": "277777.7777777778"
        },
        {
          "currency_a": "XRP_drops",
          "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
          "volume_a": "44191586",
          "volume_b": "217.6925474337355",
          "high": "202999.9948135647",
          "low": "202999.9948135647",
          "open": "202999.9948135647",
          "close": "202999.9948135647"
        },
        {
          "currency_a": "XRP_drops",
          "currency_b": "rf5YPb9y9P3fTjhxNaZqmrwaj5ar8PG1gM/47414C4100000000000000000000000000000000",
          "volume_a": "100000000",
          "volume_b": "1242.61659179386",
          "high": "80475.34586323083",
          "low": "80475.34586323083",
          "open": "80475.34586323083",
          "close": "80475.34586323083"
        },
        {
          "currency_a": "XRP_drops",
          "currency_b": "rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz/534F4C4F00000000000000000000000000000000",
          "volume_a": "33734",
          "volume_b": "0.1454210006367",
          "high": "231974.7481608686",
          "low": "231974.7481608686",
          "open": "231974.7481608686",
          "close": "231974.7481608686"
        },
        {
          "currency_a": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
          "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
          "volume_a": "158.6978670792",
          "volume_b": "21.76925474337",
          "high": "7.290000000001503",
          "low": "7.290000000001503",
          "open": "7.290000000001503",
          "close": "7.290000000001503"
        },
        {
          "currency_a": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
          "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
          "volume_a": "21.76925474337355",
          "volume_b": "217.6925474337355",
          "high": "0.1",
          "low": "0.1",
          "open": "0.1",
          "close": "0.1"
        }
      ]
    },
    "id": "example_book_changes",
    "status": "success",
    "type": "response",
    "warnings": [
      {
        "id": 2001,
        "message": "This is a clio server. clio only serves validated data. If you want to talk to rippled, include 'ledger_index':'current' in your request"
      }
    ]
  }

JSON-RPC
200 OK

{
    "result" : {
       "changes" : [
          {
             "close" : "277777.7777777778",
             "currency_a" : "XRP_drops",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
             "high" : "277777.7777777778",
             "low" : "277777.7777777778",
             "open" : "277777.7777777778",
             "volume_a" : "44082741",
             "volume_b" : "158.6978676"
          },
          {
             "close" : "202999.9948135647",
             "currency_a" : "XRP_drops",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
             "high" : "202999.9948135647",
             "low" : "202999.9948135647",
             "open" : "202999.9948135647",
             "volume_a" : "44191586",
             "volume_b" : "217.6925474337355"
          },
          {
             "close" : "80475.34586323083",
             "currency_a" : "XRP_drops",
             "currency_b" : "rf5YPb9y9P3fTjhxNaZqmrwaj5ar8PG1gM/47414C4100000000000000000000000000000000",
             "high" : "80475.34586323083",
             "low" : "80475.34586323083",
             "open" : "80475.34586323083",
             "volume_a" : "100000000",
             "volume_b" : "1242.61659179386"
          },
          {
             "close" : "231974.7481608686",
             "currency_a" : "XRP_drops",
             "currency_b" : "rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz/534F4C4F00000000000000000000000000000000",
             "high" : "231974.7481608686",
             "low" : "231974.7481608686",
             "open" : "231974.7481608686",
             "volume_a" : "33734",
             "volume_b" : "0.1454210006367"
          },
          {
             "close" : "7.290000000001503",
             "currency_a" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
             "high" : "7.290000000001503",
             "low" : "7.290000000001503",
             "open" : "7.290000000001503",
             "volume_a" : "158.6978670792",
             "volume_b" : "21.76925474337"
          },
          {
             "close" : "0.1",
             "currency_a" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
             "high" : "0.1",
             "low" : "0.1",
             "open" : "0.1",
             "volume_a" : "21.76925474337355",
             "volume_b" : "217.6925474337355"
          }
       ],
       "ledger_hash" : "7AB08A2415C10E07201521F3260F77ADFF4902A528EA66378E259A07767A24B9",
       "ledger_index" : 88530953,
       "ledger_time" : 771100891,
       "status" : "success",
       "type" : "bookChanges"
    }
}

Commandline
Loading: "/etc/opt/ripple/rippled.cfg"
2024-Jun-07 18:41:45.257772761 UTC HTTPClient:NFO Connecting to 127.0.0.1:5005

{
    "result" : {
       "changes" : [
          {
             "close" : "277777.7777777778",
             "currency_a" : "XRP_drops",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
             "high" : "277777.7777777778",
             "low" : "277777.7777777778",
             "open" : "277777.7777777778",
             "volume_a" : "44082741",
             "volume_b" : "158.6978676"
          },
          {
             "close" : "202999.9948135647",
             "currency_a" : "XRP_drops",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
             "high" : "202999.9948135647",
             "low" : "202999.9948135647",
             "open" : "202999.9948135647",
             "volume_a" : "44191586",
             "volume_b" : "217.6925474337355"
          },
          {
             "close" : "80475.34586323083",
             "currency_a" : "XRP_drops",
             "currency_b" : "rf5YPb9y9P3fTjhxNaZqmrwaj5ar8PG1gM/47414C4100000000000000000000000000000000",
             "high" : "80475.34586323083",
             "low" : "80475.34586323083",
             "open" : "80475.34586323083",
             "volume_a" : "100000000",
             "volume_b" : "1242.61659179386"
          },
          {
             "close" : "231974.7481608686",
             "currency_a" : "XRP_drops",
             "currency_b" : "rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz/534F4C4F00000000000000000000000000000000",
             "high" : "231974.7481608686",
             "low" : "231974.7481608686",
             "open" : "231974.7481608686",
             "volume_a" : "33734",
             "volume_b" : "0.1454210006367"
          },
          {
             "close" : "7.290000000001503",
             "currency_a" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
             "high" : "7.290000000001503",
             "low" : "7.290000000001503",
             "open" : "7.290000000001503",
             "volume_a" : "158.6978670792",
             "volume_b" : "21.76925474337"
          },
          {
             "close" : "0.1",
             "currency_a" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
             "currency_b" : "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/XLM",
             "high" : "0.1",
             "low" : "0.1",
             "open" : "0.1",
             "volume_a" : "21.76925474337355",
             "volume_b" : "217.6925474337355"
          }
       ],
       "ledger_hash" : "7AB08A2415C10E07201521F3260F77ADFF4902A528EA66378E259A07767A24B9",
       "ledger_index" : 88530953,
       "ledger_time" : 771100891,
       "status" : "success",
       "type" : "bookChanges"
    }
}

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting), with a successful result containing the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `changes` | Array | List of [Book Update Objects](#book-update-objects), containing one entry for each order book that was updated in this ledger version. The array is empty if no order books were updated. |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | The identifying hash of the ledger version that was used when retrieving this data. |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | The ledger index of the ledger version that was used when retrieving this data. |
| `ledger_time` | Number | The official close time of the ledger that was used when retrieving this data, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time). |
| `type` | String | The string `bookChanges`, which indicates that this is an order book update message. |
| `validated` | Boolean | *(May be omitted)* If `true`, the information comes from a validated ledger version. |


### Book Update Objects

A Book Update Object represents the changes to a single order book in a single ledger version, and contains the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `currency_a` | String | An identifier for the first of the two currencies in the order book. For XRP, this is the string `XRP_drops`. For [tokens](/docs/concepts/tokens), this is formatted as the address of the issuer in [base58](/docs/references/protocol/data-types/base58-encodings), followed by a forward-slash (`/`), followed by the [Currency Code](/docs/references/protocol/data-types/currency-formats#currency-codes) for the token, which can be a 3-character standard code or a 20-character hexadecimal code. |
| `currency_b` | String | An identifier for the second of two currencies in the order book. This is in the same format as `currency_a`, except `currency_b` can never be XRP. |
| `volume_a` | String - Number | The total amount, or *volume*, of the first currency (that is, `currency_a`) that moved as a result of trades through this order book in this ledger. |
| `volume_b` | String - Number | The volume of the second currency (that is, `currency_b`) that moved as a result of trades through this order book in this ledger. |
| `high` | String - Number | The highest exchange rate among all offers matched in this ledger, as a ratio of the first currency to the second currency. (In other words, `currency_a : currency_b`.) |
| `low` | String - Number | The lowest exchange rate among all offers matched in this ledger, as a ratio of the first currency to the second currency. |
| `open` | String - Number | The exchange rate at the top of this order book before processing the transactions in this ledger, as a ratio of the first currency to the second currency. |
| `close` | String - Number | The exchange rate at the top of this order book after processing the transactions in this ledger, as a ratio of the first currency to the second currency. |


For XRP-token order books, XRP is always `currency_a`. For token-token order books, the currencies are sorted alphabetically by the issuer and then currency code.

Exchange rates involving XRP are always calculated using [drops of XRP](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts). For example, if the rate from XRP to FOO is 1.0 XRP to 1 FOO, the rate reported by the API is `1000000` (1 million drops of XRP per 1 FOO).

## Possible Errors

* Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
* `lgrNotFound` - The ledger specified by the `ledger_hash` or `ledger_index` does not exist, or it does exist but the server does not have it.
* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.



# book_offers

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/BookOffers.cpp)

The `book_offers` method retrieves a list of [offers](/docs/concepts/tokens/decentralized-exchange/offers) between two currencies, also known as an *order book*. The response omits [unfunded offers](/docs/concepts/tokens/decentralized-exchange/offers#lifecycle-of-an-offer) and reports how much of each remaining offer's total is currently funded.

## Request Format

An example of the request format:

WebSocket

```json
{
  "id": 4,
  "command": "book_offers",
  "taker": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
  "taker_gets": {
    "currency": "XRP"
  },
  "taker_pays": {
    "currency": "USD",
    "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
  },
  "limit": 10
}
```

JSON-RPC

```json
{
    "method": "book_offers",
    "params": [
        {
            "taker": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "taker_gets": {
                "currency": "XRP"
            },
            "taker_pays": {
                "currency": "USD",
                "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
            },
            "limit": 10
        }
    ]
}
```

Commandline

```sh
#Syntax: book_offers taker_pays taker_gets [taker [ledger [limit] ] ]
rippled book_offers 'USD/rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B' 'EUR/rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
```

The request includes the following parameters:

| `Field` | Type | Required? | Description |
|  --- | --- | --- | --- |
| `taker_gets` | Object | Yes | The asset the account taking the offer would receive, as a [currency without an amount](/docs/references/protocol/data-types/currency-formats#specifying-without-amounts). |
| `taker_pays` | Object | Yes | The asset the account taking the offer would pay, as a [currency without an amount](/docs/references/protocol/data-types/currency-formats#specifying-without-amounts). |
| `domain` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | The ledger entry ID of a permissioned domain. If provided, return offers from the corresponding [permissioned DEX](/docs/concepts/tokens/decentralized-exchange/permissioned-dexes) instead of using the open DEX.  |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | The unique hash of the ledger version to use. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | No | The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the ledger to use, or a shortcut string to choose a ledger automatically. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |
| `limit` | Number | No | The maximum number of offers to return. The response may include fewer results. |
| `taker` | String | No | The [Address](/docs/references/protocol/data-types/basic-data-types#addresses) of an account to use as a perspective. The response includes this account's Offers even if they are unfunded. (You can use this to see what Offers are above or below yours in the order book.) |


## Response Format

An example of a successful response:

WebSocket

```json
{
  "id": 11,
  "status": "success",
  "type": "response",
  "result": {
    "ledger_current_index": 7035305,
    "offers": [
      {
        "Account": "rM3X3QSr8icjTGpaF52dozhbT2BZSXJQYM",
        "BookDirectory": "7E5F614417C2D0A7CEFEB73C4AA773ED5B078DE2B5771F6D55055E4C405218EB",
        "BookNode": "0000000000000000",
        "Flags": 0,
        "LedgerEntryType": "Offer",
        "OwnerNode": "0000000000000AE0",
        "PreviousTxnID": "6956221794397C25A53647182E5C78A439766D600724074C99D78982E37599F1",
        "PreviousTxnLgrSeq": 7022646,
        "Sequence": 264542,
        "TakerGets": {
          "currency": "EUR",
          "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
          "value": "17.90363633316433"
        },
        "TakerPays": {
          "currency": "USD",
          "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
          "value": "27.05340557506234"
        },
        "index": "96A9104BF3137131FF8310B9174F3B37170E2144C813CA2A1695DF2C5677E811",
        "quality": "1.511056473200875"
      },
      {
        "Account": "rhsxKNyN99q6vyYCTHNTC1TqWCeHr7PNgp",
        "BookDirectory": "7E5F614417C2D0A7CEFEB73C4AA773ED5B078DE2B5771F6D5505DCAA8FE12000",
        "BookNode": "0000000000000000",
        "Flags": 131072,
        "LedgerEntryType": "Offer",
        "OwnerNode": "0000000000000001",
        "PreviousTxnID": "8AD748CD489F7FF34FCD4FB73F77F1901E27A6EFA52CCBB0CCDAAB934E5E754D",
        "PreviousTxnLgrSeq": 7007546,
        "Sequence": 265,
        "TakerGets": {
          "currency": "EUR",
          "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
          "value": "2.542743233917848"
        },
        "TakerPays": {
          "currency": "USD",
          "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
          "value": "4.19552633596446"
        },
        "index": "7001797678E886E22D6DE11AF90DF1E08F4ADC21D763FAFB36AF66894D695235",
        "quality": "1.65"
      }
    ]
  }
}
```

JSON-RPC

```json
200 OK

{
    "result": {
        "ledger_current_index": 8696243,
        "offers": [],
        "status": "success",
        "validated": false
    }
}
```

Commandline

```json
{
   "result" : {
      "ledger_current_index" : 56867201,
      "offers" : [
         {
            "Account" : "rnixnrMHHvR7ejMpJMRCWkaNrq3qREwMDu",
            "BookDirectory" : "7E5F614417C2D0A7CEFEB73C4AA773ED5B078DE2B5771F6D56038D7EA4C68000",
            "BookNode" : "0000000000000000",
            "Flags" : 131072,
            "LedgerEntryType" : "Offer",
            "OwnerNode" : "0000000000000000",
            "PreviousTxnID" : "E43ADD1BD4AC2049E0D9DE6BC279B7FD95A99C8DE2C4694A4A7623F6D9AAAE29",
            "PreviousTxnLgrSeq" : 47926685,
            "Sequence" : 219,
            "TakerGets" : {
               "currency" : "EUR",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "2.459108753792364"
            },
            "TakerPays" : {
               "currency" : "USD",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "24.59108753792364"
            },
            "index" : "3087B4828C6B5D8595EA325D69C0F396C57452893647799493A38F2C164990AB",
            "owner_funds" : "2.872409153061363",
            "quality" : "10"
         },
         {
            "Account" : "rKwjWCKBaASEvtHCxtvReNd2i9n8DxSihk",
            "BookDirectory" : "7E5F614417C2D0A7CEFEB73C4AA773ED5B078DE2B5771F6D56038D7EA4C68000",
            "BookNode" : "0000000000000000",
            "Flags" : 131072,
            "LedgerEntryType" : "Offer",
            "OwnerNode" : "0000000000000000",
            "PreviousTxnID" : "B63B2ECD124FE6B02BC2998929517266BD221A02FEE51DDE4992C1BCB7E86CD3",
            "PreviousTxnLgrSeq" : 43166305,
            "Sequence" : 19,
            "TakerGets" : {
               "currency" : "EUR",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "3.52"
            },
            "TakerPays" : {
               "currency" : "USD",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "35.2"
            },
            "index" : "89865F2C70D1140796D9D249AC2ED765AE2D007A52DEC6D6D64CCB1A77A6EB7F",
            "owner_funds" : "3.523192614770459",
            "quality" : "10",
            "taker_gets_funded" : {
               "currency" : "EUR",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "3.516160294182094"
            },
            "taker_pays_funded" : {
               "currency" : "USD",
               "issuer" : "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
               "value" : "35.16160294182094"
            }
         }
      ],
      "status" : "success",
      "validated" : false
   }
}
```

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting), with a successful result containing the following fields:

| `Field` | Type | Description |
|  --- | --- | --- |
| `ledger_current_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Omitted if `ledger_current_index` is provided)* The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the current in-progress ledger version, which was used to retrieve this information. |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Omitted if `ledger_current_index` provided)* The ledger index of the ledger version that was used when retrieving this data, as requested. |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | *(May be omitted)* The identifying hash of the ledger version that was used when retrieving this data, as requested. |
| `offers` | Array | Array of offer objects, as described below: |


Each member of the `offers` array contains canonical fields of an [Offer entry](/docs/references/protocol/ledger-data/ledger-entry-types/offer) and can also contain the following additional fields:

| `Field` | Type | Description |
|  --- | --- | --- |
| `owner_funds` | String | Amount of the `TakerGets` currency the side placing the offer has available to be traded. (XRP is represented as drops; any other currency is represented as a decimal value.) If a trader has multiple offers in the same book, only the highest-ranked offer includes this field. |
| `taker_gets_funded` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | *(Only included in partially-funded offers)* The maximum amount of currency that the taker can get, given the funding status of the offer. |
| `taker_pays_funded` | [Currency Amount](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts) | *(Only included in partially-funded offers)* The maximum amount of currency that the taker would pay, given the funding status of the offer. |
| `quality` | String | The exchange rate, as the ratio `taker_pays` divided by `taker_gets`. For fairness, offers that have the same quality are automatically taken first-in, first-out. (In other words, if multiple people offer to exchange currency at the same rate, the oldest offer is taken first.) |


## Possible Errors

* Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.
* `lgrNotFound` - The ledger specified by the `ledger_hash` or `ledger_index` does not exist, or it does exist but the server does not have it.
* `srcCurMalformed` - The `taker_pays` field in the request is not formatted properly.
* `dstAmtMalformed` - The `taker_gets` field in the request is not formatted properly.
* `srcIsrMalformed` - The `issuer` field of the `taker_pays` field in the request is not valid.
* `dstIsrMalformed` - The `issuer` field of the `taker_gets` field in the request is not valid.
* `badMarket` - The desired order book does not exist; for example, offers to exchange a currency for itself.




# deposit_authorized

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/DepositAuthorized.cpp)

The `deposit_authorized` command indicates whether one account is authorized to send payments directly to another. See [Deposit Authorization](/docs/concepts/accounts/depositauth) for information on how to require authorization to deliver money to your account.

## Request Format

An example of the request format:

WebSocket

```json
{
  "id": 1,
  "command": "deposit_authorized",
  "source_account": "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de",
  "destination_account": "rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8",
  "credentials": [
    "A182EFBD154C9E80195082F86C1C8952FC0760A654B886F61BB0A59803B4387B",
    "383D269D6C7417D0A8716B09F5DB329FB17B45A5EFDBAFB82FF04BC420DCF7D5"
  ],
  "ledger_index": "validated"
}
```

JSON-RPC

```json
{
  "method": "deposit_authorized",
  "params": [
    {
      "source_account": "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de",
      "destination_account": "rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8",
      "credentials": [
        "A182EFBD154C9E80195082F86C1C8952FC0760A654B886F61BB0A59803B4387B",
        "383D269D6C7417D0A8716B09F5DB329FB17B45A5EFDBAFB82FF04BC420DCF7D5"
      ],
      "ledger_index": "validated"
    }
  ]
}
```

Commandline

```bash
#Syntax: deposit_authorized <source_account> <destination_account> [<ledger>]
rippled deposit_authorized rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8 validated
```

The request includes the following parameters:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `source_account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | Yes | The sender of a possible payment. |
| `destination_account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | Yes | The recipient of a possible payment. |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | A 32-byte hex string for the ledger version to use. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | No | The [ledger index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the ledger to use, or a shortcut string to choose a ledger automatically. (See [Specifying Ledgers](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers)) |
| `credentials` | Array | No | A set of credentials to take into account when checking if the sender can send funds to the destination. Each member of the array must be the unique ID of a [Credential entry](/docs/references/protocol/ledger-data/ledger-entry-types/credential) in the ledger. Cannot be an empty array. |


Note
If you provide a set of credentials that does not exactly match a set of credentials preauthorized by the destination, the payment is not authorized, even if the destination has preauthorized a subset of those credentials. This matches the behavior of transaction processing.

## Response Format

An example of a successful response:

WebSocket

```json
{
  "id": 1,
  "result": {
    "credentials": [
      "A182EFBD154C9E80195082F86C1C8952FC0760A654B886F61BB0A59803B4387B",
      "383D269D6C7417D0A8716B09F5DB329FB17B45A5EFDBAFB82FF04BC420DCF7D5"
    ],
    "deposit_authorized": true,
    "destination_account": "rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8",
    "ledger_hash": "BD03A10653ED9D77DCA859B7A735BF0580088A8F287FA2C5403E0A19C58EF322",
    "ledger_index": 8,
    "source_account": "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de",
    "validated": true
  },
  "status": "success",
  "type": "response"
}
```

JSON-RPC

```json
{
  "result": {
    "credentials": [
      "A182EFBD154C9E80195082F86C1C8952FC0760A654B886F61BB0A59803B4387B",
      "383D269D6C7417D0A8716B09F5DB329FB17B45A5EFDBAFB82FF04BC420DCF7D5"
    ],
    "deposit_authorized": true,
    "destination_account": "rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8",
    "ledger_hash": "BD03A10653ED9D77DCA859B7A735BF0580088A8F287FA2C5403E0A19C58EF322",
    "ledger_index": 8,
    "source_account": "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de",
    "status": "success",
    "validated": true
  }
}
```

Commandline

```json
Loading: "/etc/rippled.cfg"
2018-Jul-30 20:07:38.771658157 HTTPClient:NFO Connecting to 127.0.0.1:5005

{
   "result" : {
      "credentials": [
        "A182EFBD154C9E80195082F86C1C8952FC0760A654B886F61BB0A59803B4387B",
        "383D269D6C7417D0A8716B09F5DB329FB17B45A5EFDBAFB82FF04BC420DCF7D5"
      ],
      "deposit_authorized" : true,
      "destination_account" : "rsUiUMpnrgxQp24dJYZDhmV4bE3aBtQyt8",
      "ledger_hash" : "BD03A10653ED9D77DCA859B7A735BF0580088A8F287FA2C5403E0A19C58EF322",
      "ledger_index" : 8,
      "source_account" : "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de",
      "status" : "success",
      "validated" : true
   }
}
```

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting), with a successful result containing the following fields:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `credentials` | Array of [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | The credentials specified in the request, if any. |
| `deposit_authorized` | Boolean | Yes | Whether the specified source account is authorized to send payments directly to the destination account. If `true`, either the destination account does not require [deposit authorization](/docs/concepts/accounts/depositauth) or the source account is preauthorized. |
| `destination_account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | Yes | The destination account specified in the request. |
| `ledger_hash` | String | No | The identifying hash of the ledger that was used to generate this response. |
| `ledger_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | No | The ledger index of the ledger version that was used to generate this response. |
| `ledger_current_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | No | The ledger index of the current in-progress ledger version, which was used to generate this response. |
| `source_account` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | Yes | The source account specified in the request. |
| `validated` | Boolean | No | If `true`, the information comes from a validated ledger version. |


Note
A `deposit_authorized` status of `true` does not guarantee that a payment can be sent from the specified source to the specified destination. For example, the destination account may not have a [trust line](/docs/concepts/tokens/fungible-tokens) for the specified currency, or there may not be enough liquidity to deliver a payment.

## Possible Errors

* Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.
* `actMalformed` - An [Address](/docs/references/protocol/data-types/basic-data-types#addresses) specified in the `source_account` or `destination_account` field of the request was not properly formatted. (It may contain a typo or be the wrong length, causing a failed checksum.)
* `badCredentials` - At least one of the supplied credentials does not exist, is expired, or has not been accepted.
* `dstActNotFound` - The `destination_account` field of the request does not correspond to an account in the ledger.
* `lgrNotFound` - The ledger specified by the `ledger_hash` or `ledger_index` does not exist, or it does exist but the server does not have it.
* `srcActNotFound` - The `source_account` field of the request does not correspond to an account in the ledger.




# get_aggregate_price

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/GetAggregatePrice.cpp)

The `get_aggregate_price` method retrieves the aggregate price of specified `Oracle` objects, returning three price statistics: mean, median, and trimmed mean.

PriceOracle
## Request Format

An example of the request format:

WebSocket

```json
{
  "command": "get_aggregate_price",
  "ledger_index": "current",
  "base_asset": "XRP",
  "quote_asset": "USD",
  "trim": 20,
  "oracles": [
    {
      "account": "rp047ow9WcPmnNpVHMQV5A4BF6vaL9Abm6",
      "oracle_document_id": 34
    },
    {
      "account": "rp147ow9WcPmnNpVHMQV5A4BF6vaL9Abm7",
      "oracle_document_id": 56
    },
    {
      "account": "rp247ow9WcPmnNpVHMQV5A4BF6vaL9Abm8",
      "oracle_document_id": 2
    },
    {
      "account": "rp347ow9WcPmnNpVHMQV5A4BF6vaL9Abm9",
      "oracle_document_id": 7
    },
    {
      "account": "rp447ow9WcPmnNpVHMQV5A4BF6vaL9Abm0",
      "oracle_document_id": 109
    }
  ]
}
```

JSON-RPC

```json
{
  "method": "get_aggregate_price",
  "params": [
    {
      "ledger_index": "current",
      "base_asset": "XRP",
      "quote_asset": "USD",
      "trim": 20,
      "oracles": [
        {
          "account": "rNZ9m6AP9K7z3EVg6GhPMx36V4QmZKeWds",
          "oracle_document_id": 34
        },
        {
          "account": "rMVKq8zrVsJZQFEiTARyC6WfZznhhLMcNi",
          "oracle_document_id": 100
        },
        {
          "account": "r92kJTnUbUUq15t2BBZYGYxY79RnNc7rLQ",
          "oracle_document_id": 2
        }
      ]
    }
  ]
}
```

The request contains the following parameters:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `base_asset` | String | Yes | The currency code of the asset to be priced. |
| `quote_asset` | String | Yes | The currency code of the asset to quote the price of the base asset. |
| `trim` | Number | No | The percentage of outliers to trim. Valid trim range is 1-25. If included, the API returns statistics for the `trimmed mean`. |
| `trim_threshold` | Number | No | Defines a time range in seconds for filtering out older price data. Default value is 0, which doesn't filter any data. |
| `oracles` | Array | Yes | An array of oracle identifier objects. You must list between 1 and 200 oracle identifiers. |


Each member of the `oracles` array is an oracle identifier object with the following fields:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `account` | String | Yes | The XRPL account that controls the `Oracle` object. |
| `oracle_document_id` | Number | Yes | A unique identifier of the price oracle for the `Account` |


## Response Format

An example of the response format:


```json
{
  "result": {
    "entire_set": {
      "mean": "0.78",
      "size": 3,
      "standard_deviation": "0.03464101615137754"
    },
    "ledger_current_index": 3677185,
    "median": "0.8",
    "time": 1724877762,
    "trimmed_set": {
      "mean": "0.78",
      "size": 3,
      "standard_deviation": "0.03464101615137754"
    },
    "validated": false
  },
  "status": "success",
  "type": "response"
}
```

| Field | Type | Description |
|  --- | --- | --- |
| `entire_set` | Object | The statistics from the collected oracle prices. |
| `entire_set.mean` | String - Number | The simple mean. |
| `entire_set.size` | Number | The size of the data set to calculate the mean. |
| `entire_set.standard_deviation` | String - Number | The standard deviation. |
| `trimmed_set` | Object | The trimmed statistics from the collected oracle prices. Only appears if the `trim` field was specified in the request. |
| `trimmed_set.mean` | String - Number | The simple mean of the trimmed data. |
| `trimmed_set.size` | Number | The size of the data to calculate the trimmed mean. |
| `trimmed_set.standard_deviation` | String - Number | The standard deviation of the trimmed data. |
| `time` | Number | The most recent timestamp out of all `LastUpdateTime` values, represented in Unix time. |


Notes
- The most recent `Oracle` objects are obtained for the specified oracles.
- The most recent `LastUpdateTime` among all objects is chosen as the upper time threshold.
- An `Oracle` object is included in the aggregation dataset if it contains the specified `base_asset`/`quote_asset` pair, has an `AssetPrice` field, and its `LastUpdateTime` is within the time range specified.
- If an `Oracle` object doesn't contain an `AssetPrice` for the specified token pair, then up to three previous `Oracle` objects are examined and the most recent one that fulfills the requirements is included.


## Possible Errors

- Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
- `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.
- `internal` - The `trim_threshold` setting removed all prices.
- `objectNotFound` - There are no prices in the dataset.
- `oracleMalformed` - The `oracles` array is malformed. At least one object field is specified incorrectly or missing, or the number of objects is outside the bounds of 1 to 200.





































# Payment Channel Methods

Payment channels are a tool for facilitating repeated, unidirectional payments, or temporary credit between two parties. Use these methods to work with payment channels.




# Subscription Methods

Use these methods to enable the server to push updates to your client when various events happen, so that you can know and react right away. WebSocket API only.


# subscribe

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/Subscribe.cpp)

The `subscribe` method requests periodic notifications from the server when certain events happen.

## Request Format

An example of the request format:

Subscribe to accounts

```json
{
  "id": "Example watch Bitstamp's hot wallet",
  "command": "subscribe",
  "accounts": ["rrpNnNLKrartuEqfJGpqyDwPj1AFPg9vn1"]
}
```

Subscribe to order book

```json
{
    "id": "Example subscribe to XRP/GateHub USD order book",
    "command": "subscribe",
    "books": [
        {
            "taker_pays": {
                "currency": "XRP"
            },
            "taker_gets": {
                "currency": "USD",
                "issuer": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq"
            },
            "snapshot": true
        }
    ]
}
```

Subscribe to ledger stream

```json
{
  "id": "Example watch for new validated ledgers",
  "command": "subscribe",
  "streams": ["ledger"]
}
```

The request includes the following parameters:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `streams` | Array | No | Streams to subscribe to, as explained below. Each member of the array must be the string name of a stream. |
| `accounts` | Array | No | Array with the unique [addresses](/docs/references/protocol/data-types/basic-data-types#addresses) of accounts to monitor for validated transactions. The server sends a `transaction` type message whenever a transaction affects at least one of these accounts. |
| `accounts_proposed` | Array | No | Like `accounts`, but include transactions that are not yet finalized. |
| `books` | Array | No | Order books to monitor for updates. Each member of the array must be a [book object](#book-objects), as defined below. The server sends a `transaction` type message whenever a transaction affects this account. |
| `url` | String | Optional for Websocket; Required for JSON-RPC | **(Admin only)** URL where the server sends JSON-RPC callbacks for each event. |
| `url_username` | String | No | Username to provide for basic authentication at the callback URL. |
| `url_password` | String | No | Password to provide for basic authentication at the callback URL. |


The following parameters are deprecated and may be removed without further notice: `user`, `password`, `rt_accounts`.

The `streams` parameter provides access to the following default streams of information:

| Stream Name | Message Type | Description |
|  --- | --- | --- |
| `book_changes` | `bookChanges` | Sends order book changes whenever the consensus process declares a new validated ledger. |
| `consensus` | `consensusPhase` | Sends a message whenever the server changes phase in the consensus cycle. |
| `ledger` | `ledgerClosed` | Sends a message whenever the consensus process declares a new validated ledger. |
| `manifests` | `manifestReceived` | Sends a message whenever the server receives an update to a validator's ephemeral signing key. |
| `peer_status` | `peerStatusChange` | **(Admin only)** Information about connected peer `rippled` servers, especially with regards to the consensus process. |
| `transactions` | `transaction` | Sends a message whenever a transaction is included in a closed ledger. |
| `transactions_proposed` | `transaction` | Sends a message whenever a transaction is included in a closed ledger, as well as some transactions that have not yet been included in a validated ledger and may never be. Not all proposed transactions appear before validation. [Even some transactions that don't succeed are included](/docs/references/protocol/transactions/transaction-results) in validated ledgers, because they take the anti-spam transaction fee. |
| `server` | `serverStatus` | Sends a message whenever the status of the `rippled` server (for example, network connectivity) changes. |
| `validations` | `validationReceived` | Sends a message whenever the server receives a validation message, regardless of if the server trusts the validator. (An individual `rippled` declares a ledger validated when the server receives validation messages from at least a quorum of trusted validators.) |


The following streams are not available from Clio servers: `server`, `peer_status`, `consensus`. If you request one of these streams, Clio returns the error `reportingUnsupported`. New in: Clio v2.0

### Book Objects

Each member of the `books` array, if provided, is an object with the following fields:

| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `taker_gets` | Object - Currency | Yes | Specification of which currency the account taking the offer would receive, as a [currency object with no amount](/docs/references/protocol/data-types/currency-formats#specifying-without-amounts). |
| `taker_pays` | Object - Currency | Yes | Specification of which currency the account taking the offer would pay, as a [currency object with no amount](/docs/references/protocol/data-types/currency-formats#specifying-without-amounts). |
| `both` | Boolean | No | If `true`, return both sides of the order book. The default is `false`. |
| `domain` | String - [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | No | The ledger entry ID of a permissioned domain. If provided, subscribe to the order books for the corresponding [permissioned DEX](/docs/concepts/tokens/decentralized-exchange/permissioned-dexes) instead of the open DEX.  |
| `snapshot` | Boolean | No | If `true`, return the current state of the order book once when you subscribe before sending updates. The default is `false`. |
| `taker` | String - [Address](/docs/references/protocol/data-types/basic-data-types#addresses) | No | The acount to use as a perspective for viewing offers. This affects the funding status and fees of [offers](/docs/concepts/tokens/decentralized-exchange/offers). |


## Response Format

An example of a successful response:

WebSocket

```json
{
  "id": "Example watch Bitstamp's hot wallet",
  "status": "success",
  "type": "response",
  "result": {}
}
```

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting). The fields contained in the response vary depending on what subscriptions were included in the request.

* `accounts` and `accounts_proposed` - No fields returned.
* *Stream: `server`* - Information about the server status, such as `load_base` (the current load level of the server), `random` (a randomly-generated value), and others, subject to change.
* *Stream: `transactions`*, *Stream: `transactions_proposed`*, *Stream: `validations`*, and *Stream: `consensus`* - No fields returned.
* *Stream: `ledger`* - Information about the ledgers on hand and current fee schedule. This includes the same fields as a [ledger stream message](#ledger-stream), except that it omits the `type` and `txn_count` fields.
* `books` - No fields returned by default. If `"snapshot": true` is set in the request, returns `offers` (an array of offer definition objects defining the order book).


## Possible Errors

* Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.
* `noPermission` - The request included the `url` field, but you are not connected as an admin.
* `unknownStream` - One or more the members of the `streams` field of the request is not a valid stream name.
* `malformedStream` - The `streams` field of the request is not formatted properly.
* `malformedAccount` - One of the addresses in the `accounts` or `accounts_proposed` fields of the request is not a properly-formatted XRP Ledger address. (**Note:**: You *can* subscribe to the stream of an address that does not yet have an entry in the global ledger to get a message when that address becomes funded.)
* `srcCurMalformed` - One or more `taker_pays` sub-fields of the `books` field in the request is not formatted properly.
* `dstAmtMalformed` - One or more `taker_gets` sub-fields of the `books` field in the request is not formatted properly.
* `srcIsrMalformed` - The `issuer` field of one or more `taker_pays` sub-fields of the `books` field in the request is not valid.
* `dstIsrMalformed` - The `issuer` field of one or more `taker_gets` sub-fields of the `books` field in the request is not valid.
* `badMarket` - One or more desired order books in the `books` field does not exist; for example, offers to exchange a currency for itself.


When you subscribe to a particular stream, you receive periodic responses on that stream until you unsubscribe or close the WebSocket connection. The content of those responses depends on what you subscribed to. Here are some examples:

## Ledger Stream

The `ledger` stream only sends `ledgerClosed` messages when [the consensus process](/docs/concepts/consensus-protocol) declares a new validated ledger. The message identifies the ledger and provides some information about its contents.


```json
{
  "type": "ledgerClosed",
  "fee_base": 10,
  "fee_ref": 10,
  "ledger_hash": "687F604EF6B2F67319E8DCC8C66EF49D84D18A1E18F948421FC24D2C7C3DB464",
  "ledger_index": 7125358,
  "ledger_time": 455751310,
  "network_id": 1,
  "reserve_base": 20000000,
  "reserve_inc": 5000000,
  "txn_count": 7,
  "validated_ledgers": "32570-7125358"
}
```

The fields from a ledger stream message are as follows:

| Field | Type | Description |
|  --- | --- | --- |
| `type` | String | `ledgerClosed` indicates this is from the ledger stream |
| `fee_base` | Number | The [reference transaction cost](/docs/concepts/transactions/transaction-cost#reference-transaction-cost) as of this ledger version, in [drops of XRP](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts). If this ledger version includes a [SetFee pseudo-transaction](/docs/references/protocol/transactions/pseudo-transaction-types/setfee) the new transaction cost applies starting with the following ledger version. |
| `fee_ref` | Number | *(May be omitted)* The [reference transaction cost](/docs/concepts/transactions/transaction-cost#reference-transaction-cost) in "fee units". If the *[XRPFees amendment](/resources/known-amendments#xrpfees)* is enabled, this field is permanently omitted as it will no longer be relevant. |
| `ledger_hash` | String - [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | The identifying hash of the ledger version that was closed. |
| `ledger_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | The ledger index of the ledger that was closed. |
| `ledger_time` | Number | The time this ledger was closed, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time) |
| `network_id` | Number | The XRPL network of this stream. |
| `reserve_base` | Number | The minimum [reserve](/docs/concepts/accounts/reserves), in [drops of XRP](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts), that is required for an account. If this ledger version includes a [SetFee pseudo-transaction](/docs/references/protocol/transactions/pseudo-transaction-types/setfee) the new base reserve applies starting with the following ledger version. |
| `reserve_inc` | Number | The [owner reserve](/docs/concepts/accounts/reserves#owner-reserves) for each object an account owns in the ledger, in [drops of XRP](/docs/references/protocol/data-types/basic-data-types#specifying-currency-amounts). If the ledger includes a [SetFee pseudo-transaction](/docs/references/protocol/transactions/pseudo-transaction-types/setfee) the new owner reserve applies after this ledger. |
| `txn_count` | Number | Number of new transactions included in this ledger version. |
| `validated_ledgers` | String | *(May be omitted)* Range of ledgers that the server has available. This may be a disjoint sequence such as `24900901-24900984,24901116-24901158`. This field is not returned if the server is not connected to the network, or if it is connected but has not yet obtained a ledger from the network. |


## Validations Stream

The validations stream sends messages whenever it receives validation messages, also called validation votes, regardless of whether or not the validation message is from a trusted validator. The message looks like the following:


```json
{
    "type": "validationReceived",
    "amendments":[
        "42426C4D4F1009EE67080A9B7965B44656D7714D104A72F9B4369F97ABF044EE",
        "4C97EBA926031A7CF7D7B36FDE3ED66DDA5421192D63DE53FFB46E43B9DC8373",
        "6781F8368C4771B83E8B821D88F580202BCB4228075297B19E4FDC5233F1EFDC",
        "C1B8D934087225F509BEB5A8EC24447854713EE447D277F69545ABFA0E0FD490",
        "DA1BD556B42D85EA9C84066D028D355B52416734D3283F85E216EA5DA6DB7E13"
    ],
    "base_fee":10,
    "flags":2147483649,
    "full":true,
    "ledger_hash":"EC02890710AAA2B71221B0D560CFB22D64317C07B7406B02959AD84BAD33E602",
    "ledger_index":"6",
    "load_fee":256000,
    "master_key": "nHUon2tpyJEHHYGmxqeGu37cvPYHzrMtUNQFVdCgGNvEkjmCpTqK",
    "network_id": 1,
    "reserve_base":20000000,
    "reserve_inc":5000000,
    "signature":"3045022100E199B55643F66BC6B37DBC5E185321CF952FD35D13D9E8001EB2564FFB94A07602201746C9A4F7A93647131A2DEB03B76F05E426EC67A5A27D77F4FF2603B9A528E6",
    "signing_time":515115322,
    "validation_public_key":"n94Gnc6svmaPPRHUAyyib1gQUov8sYbjLoEwUBYPH39qHZXuo8ZT"
}
```

The fields from a validations stream message are as follows:

| Field | Type | Description |
|  --- | --- | --- |
| `type` | String | The value `validationReceived` indicates this is from the validations stream. |
| `amendments` | Array of Strings | *(May be omitted)* The [amendments](/docs/concepts/networks-and-servers/amendments) this server wants to be added to the protocol. |
| `base_fee` | Integer | *(May be omitted)* The unscaled transaction cost (`reference_fee` value) this server wants to set by [Fee Voting](/docs/concepts/consensus-protocol/fee-voting). |
| `cookie` | String - Number | *(May be omitted)* An arbitrary value chosen by the server at startup. If the same validation key pair signs validations with different cookies concurrently, that usually indicates that multiple servers are incorrectly configured to use the same validation key pair. New in: rippled 1.8.1 |
| `flags` | Number | Bit-mask of flags added to this validation message. The flag `0x80000000` indicates that the validation signature is fully-canonical. The flag `0x00000001` indicates that this is a full validation; otherwise it's a partial validation. Partial validations are not meant to vote for any particular ledger. A partial validation indicates that the validator is still online but not keeping up with consensus. |
| `full` | Boolean | If `true`, this is a full validation. Otherwise, this is a partial validation. Partial validations are not meant to vote for any particular ledger. A partial validation indicates that the validator is still online but not keeping up with consensus. |
| `ledger_hash` | String | The identifying hash of the proposed ledger is being validated. |
| `ledger_index` | String - Number | The [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of the proposed ledger. |
| `load_fee` | Integer | *(May be omitted)* The local load-scaled transaction cost this validator is currently enforcing, in fee units. |
| `master_key` | String | *(May be omitted)* The validator's master public key, if the validator is using a validator token, in the XRP Ledger's [base58](/docs/references/protocol/data-types/base58-encodings) format. (See also: [Enable Validation on your `rippled` Server](/docs/infrastructure/configuration/server-modes/run-rippled-as-a-validator#3-enable-validation-on-your-rippled-server).) |
| `network_id` | Number | The [XRPL network](/docs/references/protocol/transactions/common-fields#networkid-field) of this stream. New in: rippled 2.6.0 |
| `reserve_base` | Integer | *(May be omitted)* The minimum reserve requirement (`account_reserve` value) this validator wants to set by [Fee Voting](/docs/concepts/consensus-protocol/fee-voting). |
| `reserve_inc` | Integer | *(May be omitted)* The increment in the reserve requirement (`owner_reserve` value) this validator wants to set by [Fee Voting](/docs/concepts/consensus-protocol/fee-voting). |
| `server_version` | String - Number | *(May be omitted)* An 64-bit integer that encodes the version number of the validating server. For example, `"1745990410175512576"`. Only provided once every 256 ledgers. New in: rippled 1.8.1 |
| `signature` | String | The signature that the validator used to sign its vote for this ledger. |
| `signing_time` | Number | When this validation vote was signed, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time). |
| `validated_hash` | String | The unique hash of the proposed ledger this validation applies to. New in: rippled 1.8.1 |
| `validation_public_key` | String | The public key from the key-pair that the validator used to sign the message, in the XRP Ledger's [base58](/docs/references/protocol/data-types/base58-encodings) format. This identifies the validator sending the message and can also be used to verify the `signature`. If the validator is using a token, this is an ephemeral public key. |


## Transaction Streams

Many subscriptions result in messages about transactions, including the following:

* The `transactions` stream
* The `transactions_proposed` stream
* `accounts` subscriptions
* `accounts_proposed` subscriptions
* `book` (Order Book) subscriptions


The `transactions_proposed` stream, strictly speaking, is a superset of the `transactions` stream: it includes all validated transactions, as well as some suggested transactions that have not yet been included in a validated ledger and may never be. You can identify these "in-flight" transactions by their fields:

* The `validated` field is missing or has a value of `false`.
* There is no `meta` or `metadata` field.
* Instead of `ledger_hash` and `ledger_index` fields specifying in which ledger version the transactions were finalized, there is a `ledger_current_index` field specifying in which ledger version they are currently proposed.


Otherwise, the messages from the `transactions_proposed` stream are the same as ones from the `transactions` stream.

Since the only thing that can modify an account or an order book is a transaction, the messages that are sent as a result of subscribing to particular `accounts` or `books` also take the form of transaction messages, the same as the ones in the `transactions` stream. The only difference is that you only receive messages for transactions that affect the accounts or order books you're watching.

The `accounts_proposed` subscription works the same way, except it also includes unconfirmed transactions, like the `transactions_proposed` stream, for the accounts you're watching.


```json
{
  "close_time_iso": "2024-11-01T23:59:01Z",
  "engine_result": "tesSUCCESS",
  "engine_result_code": 0,
  "engine_result_message": "The transaction was applied. Only final in a validated ledger.",
  "hash": "6489E52A909208E371ACE82E19CAE59896C7F8BA40E7C36C5B8AA3C451914BED",
  "ledger_hash": "0B6F44849E6D702D0CFB447FDBD7B603C269E9EEECE9176882EF376E0C9DFF6A",
  "ledger_index": 1969852,
  "meta": {
    "AffectedNodes": [
      {
        "ModifiedNode": {
          "FinalFields": {
            "Account": "rH3PxjJPrrkvsATddBXkayjAyWR8xigaE8",
            "Balance": "39999964",
            "Flags": 0,
            "OwnerCount": 0,
            "Sequence": 1969812
          },
          "LedgerEntryType": "AccountRoot",
          "LedgerIndex": "EDE60B24659BCC06CCE1EA2804A4A202F1C88155CEAED9C140833C0C39100617",
          "PreviousFields": {
            "Balance": "59999976",
            "Sequence": 1969811
          },
          "PreviousTxnID": "1DBC93373D47794A684A5013178D0EBE10E6641D7C262BF20151B0E19156FF79",
          "PreviousTxnLgrSeq": 1969843
        }
      },
      {
        "ModifiedNode": {
          "FinalFields": {
            "Account": "rfdGuuVnq9juqWDV4W3LoLiNcW8g2hAXhN",
            "Balance": "160000000",
            "Flags": 0,
            "OwnerCount": 0,
            "Sequence": 1969810
          },
          "LedgerEntryType": "AccountRoot",
          "LedgerIndex": "F7D350FB54C5BBA734AE574EE6BF7A9294E11F9B75413972F98846AFC587C62C",
          "PreviousFields": {
            "Balance": "140000000"
          },
          "PreviousTxnID": "1DBC93373D47794A684A5013178D0EBE10E6641D7C262BF20151B0E19156FF79",
          "PreviousTxnLgrSeq": 1969843
        }
      }
    ],
    "TransactionIndex": 4,
    "TransactionResult": "tesSUCCESS",
    "delivered_amount": "20000000"
  },
  "status": "closed",
  "tx_json": {
    "Account": "rH3PxjJPrrkvsATddBXkayjAyWR8xigaE8",
    "DeliverMax": "20000000",
    "Destination": "rfdGuuVnq9juqWDV4W3LoLiNcW8g2hAXhN",
    "Fee": "12",
    "Flags": 0,
    "LastLedgerSequence": 1969870,
    "Sequence": 1969811,
    "SigningPubKey": "ED0761CDA5507784F6CEB445DE2343F861DD5EC7A869F75B08C7E8F29A947AD9FC",
    "TransactionType": "Payment",
    "TxnSignature": "20D5447ED7095BCCC3D42EA1955600D97D791811072E93D2A358AD9FB258C3A7F004974039D25708F5AE598C78F85B688DD586158F7E9C13AE0F30CC18E3390D",
    "date": 783820741
  },
  "type": "transaction",
  "validated": true
}
```

Transaction stream messages have the following fields:

API v2
| Field | Type | Description |
|  --- | --- | --- |
| `close_time_iso` | String | The time the ledger containing this transaction was closed, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `type` | String | `transaction` indicates this is the notification of a transaction, which could come from several possible streams. |
| `engine_result` | String | String [Transaction result code](/docs/references/protocol/transactions/transaction-results) |
| `engine_result_code` | Number | Numeric [transaction response code](/docs/references/protocol/transactions/transaction-results), if applicable. |
| `engine_result_message` | String | Human-readable explanation for the transaction response |
| `hash` | String | The unique hash identifier of the transaction. |
| `ledger_current_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Unvalidated transactions only)* The ledger index of the current in-progress [ledger version](/docs/concepts/ledgers) for which this transaction is currently proposed. |
| `ledger_hash` | String - [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | *(Validated transactions only)* The identifying hash of the ledger version that includes this transaction |
| `ledger_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Validated transactions only)* The ledger index of the ledger version that includes this transaction. |
| `meta` | Object | *(Validated transactions only)* The [transaction metadata](/docs/references/protocol/transactions/metadata), which shows the exact outcome of the transaction in detail. |
| `tx_json` | Object | The [definition of the transaction](/docs/references/protocol/transactions) in JSON format. |
| `validated` | Boolean | If `true`, this transaction is included in a validated ledger and its outcome is final. Responses from the `transaction` stream should always be validated. |


API v1
| Field | Type | Description |
|  --- | --- | --- |
| `type` | String | `transaction` indicates this is the notification of a transaction, which could come from several possible streams. |
| `engine_result` | String | String [Transaction result code](/docs/references/protocol/transactions/transaction-results) |
| `engine_result_code` | Number | Numeric [transaction response code](/docs/references/protocol/transactions/transaction-results), if applicable. |
| `engine_result_message` | String | Human-readable explanation for the transaction response |
| `ledger_current_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Unvalidated transactions only)* The ledger index of the current in-progress [ledger version](/docs/concepts/ledgers) for which this transaction is currently proposed. |
| `ledger_hash` | String - [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | *(Validated transactions only)* The identifying hash of the ledger version that includes this transaction |
| `ledger_index` | Number - [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | *(Validated transactions only)* The ledger index of the ledger version that includes this transaction. |
| `meta` | Object | *(Validated transactions only)* The [transaction metadata](/docs/references/protocol/transactions/metadata), which shows the exact outcome of the transaction in detail. |
| `transaction` | Object | The [definition of the transaction](/docs/references/protocol/transactions) in JSON format. |
| `validated` | Boolean | If `true`, this transaction is included in a validated ledger and its outcome is final. Responses from the `transaction` stream should always be validated. |


## Peer Status Stream

The admin-only `peer_status` stream reports a large amount of information on the activities of other `rippled` servers to which this server is connected, in particular their status in the consensus process.

Example of a Peer Status stream message:


```json
{
    "action": "CLOSING_LEDGER",
    "date": 508546525,
    "ledger_hash": "4D4CD9CD543F0C1EF023CC457F5BEFEA59EEF73E4552542D40E7C4FA08D3C320",
    "ledger_index": 18853106,
    "ledger_index_max": 18853106,
    "ledger_index_min": 18852082,
    "type": "peerStatusChange"
}
```

Peer Status stream messages represent some event where the status of the peer `rippled` server changed. These messages are JSON objects with the following fields:

| Field | Value | Description |
|  --- | --- | --- |
| `type` | String | `peerStatusChange` indicates this comes from the Peer Status stream. |
| `action` | String | The type of event that prompted this message. See [Peer Status Events](#peer-status-events) for possible values. |
| `date` | Number | The time this event occurred, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time). |
| `ledger_hash` | String | (May be omitted) The identifying [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) of a ledger version to which this message pertains. |
| `ledger_index` | Number | (May be omitted) The [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) of a ledger version to which this message pertains. |
| `ledger_index_max` | Number | (May be omitted) The largest [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) the peer has currently available. |
| `ledger_index_min` | Number | (May be omitted) The smallest [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) the peer has currently available. |


### Peer Status Events

The `action` field of a Peer Status stream message can have the following values:

| `Value` | Meaning |
|  --- | --- |
| `CLOSING_LEDGER` | The peer closed a ledger version with this [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index), which usually means it is about to start consensus. |
| `ACCEPTED_LEDGER` | The peer built this ledger version as the result of a consensus round. **Note:** This ledger is still not certain to become immutably validated. |
| `SWITCHED_LEDGER` | The peer concluded it was not following the rest of the network and switched to a different ledger version. |
| `LOST_SYNC` | The peer fell behind the rest of the network in tracking which ledger versions are validated and which are undergoing consensus. |


## Order Book Streams

When you subscribe to one or more order books with the `books` field, you get back any transactions that affect those order books.

Example order book stream message:


```json
{
  "tx_json": {
    "Account": "rBTwLga3i2gz3doX6Gva3MgEV8ZCD8jjah",
    "Fee": "20",
    "Flags": 0,
    "LastLedgerSequence": 91826205,
    "OfferSequence": 156917168,
    "Sequence": 156917177,
    "SigningPubKey": "0253C1DFDCF898FE85F16B71CCE80A5739F7223D54CC9EBA4749616593470298C5",
    "TakerGets": "35992000000",
    "TakerPays": {
      "currency": "USD",
      "issuer": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq",
      "value": "18570.025718376"
    },
    "TransactionType": "OfferCreate",
    "TxnSignature": "30440220520439D8DDB6B6D0E4EA1504873D780ADE524E3961E02A5DD84B8B4C456BA3240220533CF99250737C13FD376C18F6D64149332BA1FE6EA04895442247BD29952193",
    "date": 783819060,
    "owner_funds": "36054185999"
  },
  "meta": {
    "AffectedNodes": [
      {
        "ModifiedNode": {
          "FinalFields": {
            "Flags": 0,
            "IndexNext": "0",
            "IndexPrevious": "0",
            "Owner": "rBTwLga3i2gz3doX6Gva3MgEV8ZCD8jjah",
            "RootIndex": "0A2600D85F8309FE7F75A490C19613F1CE0C37483B856DB69B8140154C2335F3"
          },
          "LedgerEntryType": "DirectoryNode",
          "LedgerIndex": "0A2600D85F8309FE7F75A490C19613F1CE0C37483B856DB69B8140154C2335F3",
          "PreviousTxnID": "73BBE254DDC97EAD6ECB2D9F7A7EB13DBA1A5B816C2727548FCFBC41B40604EF",
          "PreviousTxnLgrSeq": 91826203
        }
      },
      {
        "ModifiedNode": {
          "FinalFields": {
            "Account": "rBTwLga3i2gz3doX6Gva3MgEV8ZCD8jjah",
            "Balance": "36092186059",
            "Flags": 0,
            "OwnerCount": 14,
            "Sequence": 156917178
          },
          "LedgerEntryType": "AccountRoot",
          "LedgerIndex": "1ED8DDFD80F275CB1CE7F18BB9D906655DE8029805D8B95FB9020B30425821EB",
          "PreviousFields": {
            "Balance": "36092186079",
            "Sequence": 156917177
          },
          "PreviousTxnID": "73BBE254DDC97EAD6ECB2D9F7A7EB13DBA1A5B816C2727548FCFBC41B40604EF",
          "PreviousTxnLgrSeq": 91826203
        }
      },
      {
        "CreatedNode": {
          "LedgerEntryType": "Offer",
          "LedgerIndex": "3B4D42B185D1FE4EBED70F7E35A8E8AEA39028FB6B16DCDFC175363EA38DED28",
          "NewFields": {
            "Account": "rBTwLga3i2gz3doX6Gva3MgEV8ZCD8jjah",
            "BookDirectory": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E125486AFA57980",
            "Sequence": 156917177,
            "TakerGets": "35992000000",
            "TakerPays": {
              "currency": "USD",
              "issuer": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq",
              "value": "18570.025718376"
            }
          }
        }
      },
      {
        "DeletedNode": {
          "FinalFields": {
            "ExchangeRate": "4e12547b29376a80",
            "Flags": 0,
            "PreviousTxnID": "D4CB92E19CBADB14F82B0E0703B3F157338253EE1DD46DB91F6C98C93D01DA9C",
            "PreviousTxnLgrSeq": 91826201,
            "RootIndex": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E12547B29376A80",
            "TakerGetsCurrency": "0000000000000000000000000000000000000000",
            "TakerGetsIssuer": "0000000000000000000000000000000000000000",
            "TakerPaysCurrency": "0000000000000000000000005553440000000000",
            "TakerPaysIssuer": "2ADB0B3959D60A6E6991F729E1918B7163925230"
          },
          "LedgerEntryType": "DirectoryNode",
          "LedgerIndex": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E12547B29376A80"
        }
      },
      {
        "CreatedNode": {
          "LedgerEntryType": "DirectoryNode",
          "LedgerIndex": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E125486AFA57980",
          "NewFields": {
            "ExchangeRate": "4e125486afa57980",
            "RootIndex": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E125486AFA57980",
            "TakerPaysCurrency": "0000000000000000000000005553440000000000",
            "TakerPaysIssuer": "2ADB0B3959D60A6E6991F729E1918B7163925230"
          }
        }
      },
      {
        "DeletedNode": {
          "FinalFields": {
            "Account": "rBTwLga3i2gz3doX6Gva3MgEV8ZCD8jjah",
            "BookDirectory": "79C54A4EBD69AB2EADCE313042F36092BE432423CC6A4F784E12547B29376A80",
            "BookNode": "0",
            "Flags": 0,
            "OwnerNode": "0",
            "PreviousTxnID": "D4CB92E19CBADB14F82B0E0703B3F157338253EE1DD46DB91F6C98C93D01DA9C",
            "PreviousTxnLgrSeq": 91826201,
            "Sequence": 156917168,
            "TakerGets": "35992000000",
            "TakerPays": {
              "currency": "USD",
              "issuer": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq",
              "value": "18569.847557976"
            }
          },
          "LedgerEntryType": "Offer",
          "LedgerIndex": "F72F9E5C9C81C6D2403C062365B34AA371D5D0BB13E1787622E936D0B8B4A499"
        }
      }
    ],
    "TransactionIndex": 23,
    "TransactionResult": "tesSUCCESS"
  },
  "type": "transaction",
  "validated": true,
  "status": "closed",
  "close_time_iso": "2024-11-01T23:31:00Z",
  "ledger_index": 91826203,
  "ledger_hash": "746D115326E08B884D7EA5F0E379272774F1B41443C000044D5DF97781E0601D",
  "hash": "2250BB2914AC7BC143AD62E7DD36F23A22F2BC50495FC29B36C6B0CA570BB4FA",
  "engine_result_code": 0,
  "engine_result": "tesSUCCESS",
  "engine_result_message": "The transaction was applied. Only final in a validated ledger."
}
```

The format of an order book stream message is the same as that of [transaction stream messages](#transaction-streams), except that `OfferCreate` transactions also contain the following field:

| Field | Value | Description |
|  --- | --- | --- |
| `transaction.owner_funds` | String | Numeric amount of the `TakerGets` currency that the `Account` sending this OfferCreate transaction has after executing this transaction. This does not check whether the currency amount is [frozen](/docs/concepts/tokens/fungible-tokens/freezes).[API v2](/docs/references/http-websocket-apis#api-versioning) Renamed to `tx_json.owner_funds`. |


## Book Changes Stream

The `book_changes` stream sends `bookChanges` messages whenever a new ledger is validated. This message contains a summary of all changes to order books in the decentralized exchange that occurred in that ledger.

Example `bookChanges` message:


```json
{
  "type": "bookChanges",
  "ledger_index": 88530525,
  "ledger_hash": "E2F24290E1714C842D34A1057E6D6B7327C7DDD310263AFBC67CA8EFED7A331B",
  "ledger_time": 771099232,
  "changes": [
    {
      "currency_a": "XRP_drops",
      "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
      "volume_a": "23020993",
      "volume_b": "11.51049687275246",
      "high": "1999999.935232603",
      "low": "1999999.935232603",
      "open": "1999999.935232603",
      "close": "1999999.935232603"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo/43525950544F0000000000000000000000000000",
      "volume_a": "28062",
      "volume_b": "0.000643919229004",
      "high": "43580000.00000882",
      "low": "43580000.00000882",
      "open": "43580000.00000882",
      "close": "43580000.00000882"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rcEGREd8NmkKRE8GE424sksyt1tJVFZwu/5553444300000000000000000000000000000000",
      "volume_a": "147797392",
      "volume_b": "70.41143840513008",
      "high": "2099053.724049922",
      "low": "2099053.724049922",
      "open": "2099053.724049922",
      "close": "2099053.724049922"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rcRzGWq6Ng3jeYhqnmM4zcWcUh69hrQ8V/LTC",
      "volume_a": "350547165",
      "volume_b": "2.165759976556748",
      "high": "162573356.3100158",
      "low": "160134763.7403094",
      "open": "162573356.3100158",
      "close": "160134763.7403094"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rchGBxcD1A1C2tdxF6papQYZ8kjRKMYcL/BTC",
      "volume_a": "352373535",
      "volume_b": "0.00249291478138912",
      "high": "1413500174054660e-4",
      "low": "1413499999999996e-4",
      "open": "1413500174054660e-4",
      "close": "1413499999999996e-4"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rcvxE9PS9YBwxtGg1qNeewV6ZB3wGubZq/5553445400000000000000000000000000000000",
      "volume_a": "8768045",
      "volume_b": "4.193604075536",
      "high": "2090813.734932601",
      "low": "2090813.734932601",
      "open": "2090813.734932601",
      "close": "2090813.734932601"
    },
    {
      "currency_a": "XRP_drops",
      "currency_b": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq/USD",
      "volume_a": "28113",
      "volume_b": "0.013405652999",
      "high": "2097100.380123005",
      "low": "2097100.380123005",
      "open": "2097100.380123005",
      "close": "2097100.380123005"
    },
    {
      "currency_a": "r3dVizzUAS3U29WKaaSALqkieytA2LCoRe/58434F5245000000000000000000000000000000",
      "currency_b": "rcoreNywaoz2ZCQ8Lg2EbSLnGuRBmun6D/434F524500000000000000000000000000000000",
      "volume_a": "75.626516003375",
      "volume_b": "63.022096669479",
      "high": "1.200000000000003",
      "low": "1.200000000000003",
      "open": "1.200000000000003",
      "close": "1.200000000000003"
    },
    {
      "currency_a": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/CNY",
      "currency_b": "rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y/USD",
      "volume_a": "83.9115222024",
      "volume_b": "11.51049687275",
      "high": "7.290000000004561",
      "low": "7.290000000004561",
      "open": "7.290000000004561",
      "close": "7.290000000004561"
    },
    {
      "currency_a": "rcRzGWq6Ng3jeYhqnmM4zcWcUh69hrQ8V/LTC",
      "currency_b": "rchGBxcD1A1C2tdxF6papQYZ8kjRKMYcL/BTC",
      "volume_a": "0.64167647147626",
      "volume_b": "0.00073047551165797",
      "high": "878.4366638381051",
      "low": "878.4366638381051",
      "open": "878.4366638381051",
      "close": "878.4366638381051"
    },
    {
      "currency_a": "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq/USD",
      "currency_b": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B/USD",
      "volume_a": "0.013432464305",
      "volume_b": "0.013566788948",
      "high": "0.9900990099046391",
      "low": "0.9900990099046391",
      "open": "0.9900990099046391",
      "close": "0.9900990099046391"
    }
  ]
}
```

The fields from a Book Changes stream message are as follows:

| Field | Value | Description |
|  --- | --- | --- |
| `type` | String | The value `bookChanges` indicates this is from the Book Changes stream. |
| `ledger_index` | [Ledger Index](/docs/references/protocol/data-types/basic-data-types#ledger-index) | The ledger index of the ledger with these changes. |
| `ledger_hash` | [Hash](/docs/references/protocol/data-types/basic-data-types#hashes) | The identifying hash of the ledger with these changes. |
| `ledger_time` | Number | The official close time of the ledger with these changes, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time). |
| `changes` | Array | List of [Book Update Objects](/docs/references/http-websocket-apis/public-api-methods/path-and-order-book-methods/book_changes#book-update-objects), containing one entry for each order book that was updated in this ledger version. The array is empty if no order books were updated. |


## Consensus Stream

The `consensus` stream sends `consensusPhase` messages when [the consensus process](/docs/concepts/consensus-protocol) changes phase. The message contains the new phase of consensus the server is in.


```json
{
  "type": "consensusPhase",
  "consensus": "accepted"
}
```

The fields from a consensus stream message are as follows:

| Field | Type | Description |
|  --- | --- | --- |
| `type` | String | The value `consensusPhase` indicates this is from the consensus stream |
| `consensus` | String | The new consensus phase the server is in. Possible values are `open`, `establish`, and `accepted`. |










# unsubscribe

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/rpc/handlers/Unsubscribe.cpp)

The `unsubscribe` command tells the server to stop sending messages for a particular subscription or set of subscriptions.

## Request Format

An example of the request format:

WebSocket

```json
{
    "id": "Unsubscribe a lot of stuff",
    "command": "unsubscribe",
    "streams": ["ledger","server","transactions","transactions_proposed"],
    "accounts": ["rrpNnNLKrartuEqfJGpqyDwPj1AFPg9vn1"],
    "accounts_proposed": ["rrpNnNLKrartuEqfJGpqyDwPj1AFPg9vn1"],
    "books": [
        {
            "taker_pays": {
                "currency": "XRP"
            },
            "taker_gets": {
                "currency": "USD",
                "issuer": "rUQTpMqAF5jhykj4FExVeXakrZpiKF6cQV"
            },
            "both": true
        }
    ]
}
```

The parameters in the request are specified almost exactly like the parameters to the [subscribe method](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe), except that they are used to define which subscriptions to end instead. The parameters are:

| `Field` | Type | Required? | Description |
|  --- | --- | --- | --- |
| `streams` | Array | No | Array of string names of generic streams to unsubscribe from, including `ledger`, `server`, `transactions`, and `transactions_proposed`. |
| `accounts` | Array | No | Array of unique account addresses to stop receiving updates for, in the XRP Ledger's [base58](/docs/references/protocol/data-types/base58-encodings) format. (This only stops those messages if you previously subscribed to those accounts specifically. You cannot use this to filter accounts out of the general transactions stream.) |
| `accounts_proposed` | Array | No | Like `accounts`, but for `accounts_proposed` subscriptions that included not-yet-validated transactions. |
| `books` | Array | No | Array of objects defining order books to unsubscribe from, as explained below. |


The `rt_accounts` and `url` parameters, and the `rt_transactions` stream name, are deprecated and may be removed without further notice.

The objects in the `books` array are defined almost like the ones from subscribe, except that they don't have all the fields. The fields they have are as follows:

| `Field` | Type | Required? | Description |
|  --- | --- | --- | --- |
| `taker_gets` | Object | No | Specification of which currency the account taking the offer would receive, as an object with `currency` and `issuer` fields. Omit `issuer` for XRP. |
| `taker_pays` | Object | No | Specification of which currency the account taking the offer would receive, as an object with `currency` and `issuer` fields. Omit `issuer` for XRP. |
| `both` | Boolean | No | If `true`, remove a subscription for both sides of the order book. |


## Response Format

An example of a successful response:

WebSocket

```json
{
    "id": "Unsubscribe a lot of stuff",
    "result": {},
    "status": "success",
    "type": "response"
}
```

The response follows the [standard format](/docs/references/http-websocket-apis/api-conventions/response-formatting), with a successful result containing no fields.

## Possible Errors

* Any of the [universal error types](/docs/references/http-websocket-apis/api-conventions/error-formatting#universal-errors).
* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing.
* `noPermission` - The request included the `url` field, but you are not connected as an admin.
* `malformedStream` - The `streams` field of the request is not formatted properly.
* `malformedAccount` - One of the addresses in the `accounts` or `accounts_proposed` fields of the request is not a properly-formatted XRP Ledger address.
  * **Note:** You *can* subscribe to the stream of an address that does not yet have an entry in the global ledger to get a message when that address becomes funded.
* `srcCurMalformed` - One or more `taker_pays` sub-fields of the `books` field in the request is not formatted properly.
* `dstAmtMalformed` - One or more `taker_gets` sub-fields of the `books` field in the request is not formatted properly.
* `srcIsrMalformed` - The `issuer` field of one or more `taker_pays` sub-fields of the `books` field in the request is not valid.
* `dstIsrMalformed` - The `issuer` field of one or more `taker_gets` sub-fields of the `books` field in the request is not valid.
* `badMarket` - One or more desired order books in the `books` field does not exist; for example, offers to exchange a currency for itself.















# Server Info Methods

Use these methods to retrieve information about the current state of the rippled server.


# Clio Methods

These API methods are provided only by the Clio server, not `rippled`.




# Utility Methods

Use these methods to perform convenient tasks, such as ping and random number generation.





# Admin API Methods

Administer a `rippled` server using these admin API methods. Admin methods are meant only for trusted personnel in charge of keeping the server operational. Admin methods include commands for managing, monitoring, and debugging the server.

Admin commands are available only if you connect to `rippled` on a host and port that the `rippled.cfg` file identifies as admin. By default, the commandline client uses an admin connection. For more information on connecting to `rippled`, see [Getting Started with the `rippled` API](/docs/tutorials/http-websocket-apis/build-apps/get-started).

## [Key Generation Methods](/docs/references/http-websocket-apis/admin-api-methods/key-generation-methods)

Use these methods to generate and manage keys.

* **[`validation_create`](/docs/references/http-websocket-apis/admin-api-methods/key-generation-methods/validation_create)** - Generate formatted for `rippled` node key pair. (Validators should use [tokens](/docs/infrastructure/configuration/server-modes/run-rippled-as-a-validator) instead of keys generated by this method.)
* **[`wallet_propose`](/docs/references/http-websocket-apis/admin-api-methods/key-generation-methods/wallet_propose)** - Generate keys for a new account.


## [Logging and Data Management Methods](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods)

Use these methods to manage log levels and other data, such as ledgers.

* **[`can_delete`](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods/can_delete)** - Allow online deletion of ledgers up to a specific ledger.
* **[`ledger_cleaner`](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods/ledger_cleaner)** - Configure the ledger cleaner service to check for corrupted data.
* **[`ledger_request`](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods/ledger_request)** - Query a peer server for a specific ledger version.
* **[`log_level`](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods/log_level)** - Get or modify log verbosity.
* **[`logrotate`](/docs/references/http-websocket-apis/admin-api-methods/logging-and-data-management-methods/logrotate)** - Reopen the log file.


## [Server Control Methods](/docs/references/http-websocket-apis/admin-api-methods/server-control-methods)

Use these methods to manage the `rippled` server.

* **[`ledger_accept`](/docs/references/http-websocket-apis/admin-api-methods/server-control-methods/ledger_accept)** - Close and advance the ledger in stand-alone mode.
* **[`stop`](/docs/references/http-websocket-apis/admin-api-methods/server-control-methods/stop)** - Shut down the `rippled` server.


## [Signing Methods](/docs/references/http-websocket-apis/admin-api-methods/signing-methods)

Use these methods to sign transactions.

* **[`sign`](/docs/references/http-websocket-apis/admin-api-methods/signing-methods/sign)** - Cryptographically sign a transaction.
* **[`sign_for`](/docs/references/http-websocket-apis/admin-api-methods/signing-methods/sign_for)** - Contribute to a multi-signature.
* **[`channel_authorize`](/docs/references/http-websocket-apis/public-api-methods/payment-channel-methods/channel_authorize)** - Sign a claim for money from a payment channel.


By default, these methods are [admin-only](/docs/tutorials/http-websocket-apis/build-apps/get-started#admin-access). They can be used as public methods if the server admin has [enabled public signing](/docs/infrastructure/configuration/enable-public-signing).

## [Peer Management Methods](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods)

Use these methods to manage the server's connections in the peer-to-peer XRP Ledger network.

* **[`connect`](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods/connect)** - Force the `rippled` server to connect to a specific peer.
* **[`peer_reservations_add`](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods/peer_reservations_add)** - Add or update a reserved slot for a specific peer.
* **[`peer_reservations_del`](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods/peer_reservations_del)** - Remove a reserved slot for a specific peer.
* **[`peer_reservations_list`](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods/peer_reservations_list)** - List reserved slots for specific peers.
* **[`peers`](/docs/references/http-websocket-apis/admin-api-methods/peer-management-methods/peers)** - Get information about the peer servers connected.


## [Status and Debugging Methods](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods)

Use these methods to check the status of the network and server.

* **[`consensus_info`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/consensus_info)** - Get information about the state of consensus as it happens.
* **[`feature`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/feature)** - Get information about protocol amendments.
* **[`fetch_info`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/fetch_info)** - Get information about the server's sync with the network.
* **[`get_counts`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/get_counts)** - Get statistics about the server's internals and memory usage.
* **[`manifest`](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/manifest)** - Get the latest public key information about a known validator.
* **[`print`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/print)** - Get information about internal subsystems.
* **[`validator_info`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/validator_info)** - Get information about the server's validator settings, if configured as a validator.
* **[`validator_list_sites`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/validator_list_sites)** - Get information about sites that publish validator lists.
* **[`validators`](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/validators)** - Get information about the current validators.


## Deprecated Methods

The following admin commands are deprecated and either have been removed, or may be removed without further notice:

* `ledger_header` - Use the [ledger method](/docs/references/http-websocket-apis/public-api-methods/ledger-methods/ledger) instead.
* `unl_add`, `unl_delete`, `unl_list`, `unl_load`, `unl_network`, `unl_reset`, `unl_score` - Use the `validators.txt` config file for UNL management instead.
* `wallet_seed` - Use the [wallet_propose method](/docs/references/http-websocket-apis/admin-api-methods/key-generation-methods/wallet_propose) instead.
* `validation_seed` - Use the config file and `validator-keys-tool` for managing your seed instead.







# Request Formatting

## Example Request

WebSocket

```json
{
  "id": "example_ws_request_1",
  "command": "account_info",
  "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
  "ledger_index": "validated",
  "api_version": 2
}
```

JSON-RPC

```json
POST http://s1.ripple.com:51234/
Content-Type: application/json

{
    "method": "account_info",
    "params": [
        {
            "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "ledger_index": "validated",
            "api_version": 2
        }
    ]
}
```

Commandline

```sh
rippled account_info r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59 validated
```

## WebSocket Format

After you open a WebSocket to the `rippled` server, you can send commands as a [JSON](https://en.wikipedia.org/wiki/JSON) object with the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `command` | String | The name of the [API method](/docs/references/http-websocket-apis/public-api-methods). |
| `id` | (Various) | *(Optional)* A unique value to identify this request. The response to this request uses the same `id` field. This way, even if responses arrive out of order, you know which request prompted which response. |
| `api_version` | Number | *(Optional)* The API version to use. For details, see [API Versioning](/docs/references/http-websocket-apis#api-versioning). |
| (Method Parameters) | (Various) | Provide any parameters to the method at the top level. |


See [Response Formatting](/docs/references/http-websocket-apis/api-conventions/response-formatting) for the response from the server.

## JSON-RPC Format

To make a JSON-RPC request, send an HTTP **POST** request to the root path (`/`) on the port and IP where the `rippled` server is listening for JSON-RPC connections. You can use HTTP/1.0 or HTTP/1.1. If you use HTTPS, you should use TLS version 1.2. For security reasons, `rippled` *does not support* SSL version 3 or earlier.

Always include a `Content-Type` header with the value `application/json`.

If you plan on making multiple requests, use [Keep-Alives](http://tools.ietf.org/html/rfc7230#section-6.3) so that you do not have to close and re-open the connection in between requests. 

Send request body as a [JSON](https://en.wikipedia.org/wiki/JSON) object with the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `method` | String | The name of the [API method](/docs/references/http-websocket-apis/public-api-methods). |
| `params` | Array | *(Optional)* A **one-item array** containing a nested JSON object with the parameters to this method. You may omit this field if the method does not require any parameters. |


The object inside the `params` array can contain the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `api_version` | Number | *(Optional)* The API version to use. For details, see [API Versioning](#api-versioning). |
| (Method Parameters) | (Various) | Provide any parameters to the method here. |


See [Response Formatting](/docs/references/http-websocket-apis/api-conventions/response-formatting) for the response from the server.

## Commandline Format

Put the API method name after any normal (dash-prefaced) commandline options, followed by a limited set of parameters, separated by spaces. For any parameter values that might contain spaces or other unusual characters, use single-quotes to encapsulate them. Not all methods have commandline API syntax. For more information, see [Commandline Usage](/docs/infrastructure/commandline-usage#client-mode-options).

The commandline calls JSON-RPC, so its responses always match the JSON-RPC [response format](/docs/references/http-websocket-apis/api-conventions/response-formatting).

The commandline always uses the latest [API version](/docs/references/http-websocket-apis/api-conventions#api-versioning).

The commandline interface is intended for administrative purposes only and is *not a supported API*. New versions of `rippled` may introduce breaking changes to the commandline API without warning!




# Response Formatting

Responses are formatted slightly differently based on whether the method is called with the WebSocket, JSON-RPC, or Commandline interfaces. The Commandline and JSON-RPC interfaces use the same format because the Commandline interface calls JSON-RPC.

The fields of a successful response include:

WebSocket
| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `status` | String | Yes | The value `success` indicates the request was successfully received and understood by the server. Some [client libraries](/docs/references/client-libraries) omit this field on success. |
| `type` | String | Yes | The value `response` indicates a direct response to an API request. [Asynchronous notifications](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe) use a different value such as `ledgerClosed` or `transaction`. |
| `result` | Object | Yes | The result of the query; contents vary depending on the API method. |
| `id` | (Varies) | No | Arbitrary ID provided by the request that prompted this response. Omitted if the request didn't specify an ID. |
| `warning` | String | No | If this field is provided, the value is the string `load`. This means the client is approaching the [rate limiting](/docs/references/http-websocket-apis/api-conventions/rate-limiting) threshold where the server will disconnect this client.  |
| `warnings` | Array | No | If this field is provided, it contains one or more **Warnings Objects** with important warnings. For details, see [API Warnings](#api-warnings). |
| `forwarded` | Boolean | No | If `true`, this request and response have been forwarded from a Clio server to a P2P Mode server (and back) because the request requires data that is not available from Clio. The default is `false`. |


JSON-RPC
| Field | Type | Required? | Description |
|  --- | --- | --- | --- |
| `result` | Object | Yes | The result of the query; contents vary depending on the command. |
| `result.status` | String | Yes | The value `success` indicates the request was successfully received and understood by the server. Some [client libraries](/docs/references/client-libraries) omit this field on success. |
| `warning` | String | No | If this field is provided, the value is the string `load`. This means the client is approaching the [rate limiting](/docs/references/http-websocket-apis/api-conventions/rate-limiting) threshold where the server will disconnect this client.  |
| `warnings` | Array | No | If this field is provided, it contains one or more **Warnings Objects** with important warnings. For details, see [API Warnings](#api-warnings). |
| `forwarded` | Boolean | No | If `true`, this request and response have been forwarded from a Clio server to a P2P Mode server (and back) because the request requires data that is not available from Clio. The default is `false`. |


## Example Successful Response

WebSocket

```json
{
  "id": 2,
  "status": "success",
  "type": "response",
  "result": {
    "account_data": {
      "Account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
      "Balance": "27389517749",
      "Flags": 0,
      "LedgerEntryType": "AccountRoot",
      "OwnerCount": 18,
      "PreviousTxnID": "B6B410172C0B65575D89E464AF5B99937CC568822929ABF87DA75CBD11911932",
      "PreviousTxnLgrSeq": 6592159,
      "Sequence": 1400,
      "index": "4F83A2CF7E70F77F79A307E6A472BFC2585B806A70833CCD1C26105BAE0D6E05"
    },
    "ledger_index": 6760970
  }
}
```

JSON-RPC

```json
HTTP Status: 200 OK

{
    "result": {
        "account_data": {
            "Account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "Balance": "27389517749",
            "Flags": 0,
            "LedgerEntryType": "AccountRoot",
            "OwnerCount": 18,
            "PreviousTxnID": "B6B410172C0B65575D89E464AF5B99937CC568822929ABF87DA75CBD11911932",
            "PreviousTxnLgrSeq": 6592159,
            "Sequence": 1400,
            "index": "4F83A2CF7E70F77F79A307E6A472BFC2585B806A70833CCD1C26105BAE0D6E05"
        },
        "ledger_index": 6761012,
        "status": "success"
    }
}
```

Commandline

```json
{
    "result": {
        "account_data": {
            "Account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "Balance": "27389517749",
            "Flags": 0,
            "LedgerEntryType": "AccountRoot",
            "OwnerCount": 18,
            "PreviousTxnID": "B6B410172C0B65575D89E464AF5B99937CC568822929ABF87DA75CBD11911932",
            "PreviousTxnLgrSeq": 6592159,
            "Sequence": 1400,
            "index": "4F83A2CF7E70F77F79A307E6A472BFC2585B806A70833CCD1C26105BAE0D6E05"
        },
        "ledger_index": 6761012,
        "status": "success"
    }
}
```

## API Warnings

When the response contains a `warnings` array, each member of the array represents a separate warning from the server. Each such **Warning Object** contains the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `id` | Number | A unique numeric code for this warning message. |
| `message` | String | A human-readable string describing the cause of this message. Do not write software that relies the contents of this message; use the `id` (and `details`, if applicable) to identify the warning instead. |
| `details` | Object | *(May be omitted)* Additional information about this warning. The contents vary depending on the type of warning. |


The following reference describes all possible warnings.

### 1001. Unsupported amendments have reached majority

Example warning:


```json
"warnings" : [
  {
    "details" : {
      "expected_date" : 864030,
      "expected_date_UTC" : "2000-Jan-11 00:00:30.0000000 UTC"
    },
    "id" : 1001,
    "message" : "One or more unsupported amendments have reached majority. Upgrade to the latest version before they are activated to avoid being amendment blocked."
  }
]
```

This warning indicates that the one or more [amendments](/docs/concepts/networks-and-servers/amendments) to the XRP Ledger protocol are scheduled to become enabled, but the current server does not have an implementation for those amendments. If those amendments become enabled, the current server will become [amendment blocked](/docs/concepts/networks-and-servers/amendments#amendment-blocked-servers), so you should [upgrade to the latest `rippled` version](/docs/infrastructure/installation) as soon as possible. 

The server only sends this warning if the client is [connected as an admin](/docs/tutorials/http-websocket-apis/build-apps/get-started#admin-access).

This warning includes a `details` field with the following fields:

| Field | Type | Description |
|  --- | --- | --- |
| `expected_date` | Number | The time that the first unsupported amendment is expected to become enabled, in [seconds since the Ripple Epoch](/docs/references/protocol/data-types/basic-data-types#specifying-time). |
| `expected_date_UTC` | String | The timestamp, in UTC, when the first unsupported amendment is expected to become enabled. |


Due to the variation in ledger close times, these times are approximate. It is also possible that the amendment fails to maintain support from >80% of validators until the specified time, and does not become enabled at the expected time. The server will not become amendment blocked so long as the unsupported amendments do not become enabled.

### 1002. This server is amendment blocked

Example warning:


```json
"warnings" : [
  {
    "id" : 1002,
    "message" : "This server is amendment blocked, and must be updated to be able to stay in sync with the network."
  }
]
```

This warning indicates that the server is [amendment blocked](/docs/concepts/networks-and-servers/amendments#amendment-blocked-servers) and can no longer remain synced with the XRP Ledger.

The server administrator must [upgrade `rippled`](/docs/infrastructure/installation) to a version that supports the activated amendments.

### 2001. This is a clio server

Example warning:


```json
"warnings": [
  {
    "id": 2001,
    "message": "This is a clio server. clio only serves validated data. If you want to talk to rippled, include 'ledger_index':'current' in your request"
  }
]
```

This warning indicates that the server answering the request a Clio server, which does not have direct access to the peer-to-peer network. Certain API methods behave differently or may have additional information, and requests that require non-validated data are forwarded to a peer-to-peer server.

It is generally safe to ignore this warning.

If you request ledger data without explicitly [specifying a ledger version](/docs/references/protocol/data-types/basic-data-types#specifying-ledgers), Clio uses the latest validated ledger by default instead of the current in-progress ledger.

## See Also

- [Request Formatting](/docs/references/http-websocket-apis/api-conventions/request-formatting)
- [Error Formatting](/docs/references/http-websocket-apis/api-conventions/error-formatting) for unsuccessful API responses.
- **Concepts:**
  - [The `rippled` Server](/docs/concepts/networks-and-servers)
  - [Consensus](/docs/concepts/consensus-protocol)
  - [Amendments](/docs/concepts/networks-and-servers/amendments)
    - [Known Amendments](/resources/known-amendments)
- **Tutorials:**
  - [Get Started with XRP Ledger APIs](/docs/tutorials/http-websocket-apis/build-apps/get-started)
  - [Install and Update `rippled`](/docs/infrastructure/installation)
- **References:**
  - [feature method](/docs/references/http-websocket-apis/admin-api-methods/status-and-debugging-methods/feature)
  - [server_info method](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_info)




# Error Formatting

It is impossible to list all the possible ways an error can occur. Some may occur in the transport layer (for example, loss of network connectivity), in which case the results vary depending on what client and transport you are using. However, if the `rippled` server successfully receives your request, it tries to respond in a standardized error format.

When your request results in an error, the entire request is copied back as part of the response, so that you can try to debug the error. However, this also includes any secrets that were passed as part of the request. When sharing error messages, be very careful not to accidentally expose important account secrets to others.

Some example errors:

WebSocket

```json
{
  "id": 3,
  "status": "error",
  "type": "response",
  "error": "ledgerIndexMalformed",
  "request": {
    "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
    "command": "account_info",
    "id": 3,
    "ledger_index": "-",
    "strict": true
  }
}
```

JSON-RPC

```json
HTTP Status: 200 OK

{
    "result": {
        "error": "ledgerIndexMalformed",
        "request": {
            "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "command": "account_info",
            "ledger_index": "-",
            "strict": true
        },
        "status": "error"
    }
}
```

Commandline

```json
{
    "result": {
        "error": "ledgerIndexMalformed",
        "request": {
            "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "command": "account_info",
            "ledger_index": "-",
            "strict": true
        },
        "status": "error"
    }
}
```

## WebSocket Format

| `Field` | Type | Description |
|  --- | --- | --- |
| `id` | (Varies) | ID provided in the Web Socket request that prompted this response |
| `status` | String | `"error"` if the request caused an error |
| `type` | String | Typically `"response"`, which indicates a successful response to a command. |
| `error` | String | A unique code for the type of error that occurred |
| `request` | Object | A copy of the request that prompted this error, in JSON format. **Caution:** If the request contained any secrets, they are copied here! |
| `api_version` | Number | *(May be omitted)* The `api_version` specified in the request, if any. |


## JSON-RPC Format

Some JSON-RPC request respond with an error code on the HTTP layer. In these cases, the response is a plain-text explanation in the response body. For example, if you forgot to specify the command in the `method` parameter, the response is like this:


```
HTTP Status: 400 Bad Request
Null method
```

For other errors that returned with HTTP status code 200 OK, the responses are formatted in JSON, with the following fields:

| `Field` | Type | Description |
|  --- | --- | --- |
| `result` | Object | Object containing the response to the query |
| `result.error` | String | A unique code for the type of error that occurred |
| `result.status` | String | `"error"` if the request caused an error |
| `result.request` | Object | A copy of the request that prompted this error, in JSON format. **Caution:** If the request contained any account secrets, they are copied here! **Note:** The request is re-formatted in WebSocket format, regardless of the request made. |


## Universal Errors

All methods can potentially return any of the following values for the `error` code:

- `amendmentBlocked` - The server is [amendment blocked](/docs/concepts/networks-and-servers/amendments#amendment-blocked-servers) and needs to be updated to the latest version to stay synced with the XRP Ledger network.
- `failedToForward` - (Clio servers only) The server tried to forward this request to a `rippled` server, but the connection failed.
- `invalid_API_version` - The server does not support the [API version number](/docs/references/http-websocket-apis/api-conventions/request-formatting#api-versioning) from the request.
- `jsonInvalid` - (WebSocket only) The request is not a proper JSON object.
  - JSON-RPC returns a 400 Bad Request HTTP error in this case instead.
- `missingCommand` - (WebSocket only) The request did not specify a `command` field.
  - JSON-RPC returns a 400 Bad Request HTTP error in this case instead.
- `noClosed` - The server does not have a closed ledger, typically because it has not finished starting up.
- `noCurrent` - The server does not know what the current ledger is, due to high load, network problems, validator failures, incorrect configuration, or some other problem.
- `noNetwork` - The server is having trouble connecting to the rest of the XRP Ledger peer-to-peer network (and is not running in stand-alone mode).
- `tooBusy` - The server is under too much load to do this command right now. Generally not returned if you are connected as an admin.
- `unknownCmd` - The request does not contain a [command](/docs/references/http-websocket-apis) that the `rippled` server recognizes.
- `wsTextRequired` - (WebSocket only) The request's [opcode](https://tools.ietf.org/html/rfc6455#section-5.2) is not text.






# Markers and Pagination

Some methods return more data than can efficiently fit into one response. When there are more results than contained, the response includes a `marker` field. You can use this to retrieve more pages of data across multiple calls. In each request, pass the `marker` value from the previous response to resume from the point where you left off. If the `marker` is omitted from a response, then you have reached the end of the data set.

The format of the `marker` field is intentionally undefined. Each server can define a `marker` field as desired, so it may take the form of a string, a nested object, or another type. Different servers, and different methods provided by the same server, can have different `marker` definitions. Each `marker` is ephemeral, and may not work as expected after 10 minutes.

Python
from xrpl.clients import JsonRpcClient
from xrpl.models.requests import LedgerData

# Create a client to connect to the network.
client = JsonRpcClient("https://xrplcluster.com/")

# Query the most recently validated ledger for info.
ledger = LedgerData(ledger_index="validated")
ledger_data = client.request(ledger).result
ledger_data_index = ledger_data["ledger_index"]

# Create a function to run on each API call.
def printLedgerResult():
    print(ledger_data)

# Execute function at least once before checking for markers.
while True:
    printLedgerResult()
    if "marker" not in ledger_data:
        break
    
    # Specify the same ledger and add the marker to continue querying.
    ledger_marker = LedgerData(ledger_index=ledger_data_index, marker=ledger_data["marker"])
    ledger_data = client.request(ledger_marker).result

JavaScript
const xrpl = require("xrpl")

async function main() {

  // Create a client and connect to the network.
  const client = new xrpl.Client("wss://xrplcluster.com/")
  await client.connect()

  // Query the most recently validated ledger for info.
  let ledger = await client.request({
    "command": "ledger_data",
    "ledger_index": "validated",
  })
  const ledger_data_index = ledger["result"]["ledger_index"]

  // Create a function to run on each API call.
  function printLedgerResult(){
    console.log(ledger["result"])
  }

  // Execute function at least once before checking for markers.
  do {
    printLedgerResult()

    if (ledger["result"]["marker"] === undefined) {
        break
    }

    // Specify the same ledger and add the marker to continue querying.
    const ledger_marker = await client.request({
        "command": "ledger_data",
        "ledger_index": ledger_data_index,
        "marker": ledger["result"]["marker"]
    })
    ledger = ledger_marker

  } while (true)

  // Disconnect when done. If you omit this, Node.js won't end the process.
  await client.disconnect()
}

main()



# Rate Limiting

The `rippled` server limits the rate at which API clients can make requests on public APIs. Rate limiting is based on the IP address of the client, so clients behind [network address translation](https://en.wikipedia.org/wiki/Network_address_translation) share a limit based on their public IP address.

Rate limiting does not apply when the client is connected [as an admin](/docs/tutorials/http-websocket-apis/build-apps/get-started#admin-access).

When a client is approaching the rate limit, the server adds the field `"warning": "load"` at the top level of an [API response](/docs/references/http-websocket-apis/api-conventions/response-formatting). This warning is not added to every response, but the server may send several such warnings before it disconnects a client.

If a client exceeds the rate limit, the server disconnects that client and does not serve further requests from the client's IP address for a while. The WebSocket and JSON-RPC APIs use different disconnect messages.

## WebSocket API Disconnect Message

For the WebSocket API, the server closes the connection and provides a close message and code. The way you access these messages depends on your WebSocket client implementation. For example, using the [Node.js ws library](https://github.com/websockets/ws), the following code prints the close reason when disconnected:


```js
const WebSocket = require('ws')
const ws = new WebSocket('ws://localhost:6007/')
ws.on('close', (code,reason) => {
  console.log("Disconnected. \ncode: ", code, "\nreason: ", reason)
})

// If rate limited, prints:
// Disconnected.
// code:  1008
// reason:  threshold exceeded
```

If the connection is closed because of rate limiting, the close code is `1008` and the close message is the string `threshold exceeded`.

## JSON-RPC Rate Limited Error

For a JSON-RPC API request, the server responds with the HTTP status code **503 Service Unavailable** when the client is over the rate limit. This response has a text (not JSON) body stating that the server is overloaded:


```text
503 Service Unavailable

Server is overloaded
```

## Rate Per Request

[[Source]](https://github.com/XRPLF/rippled/blob/master/src/libxrpl/resource/Fees.cpp)

The server calculates a client's usage rate based on the number of requests made over time, and weighs different types of requests based on approximately how much work the server must do to serve them. Follow-up messages from the server for the [subscribe method](/docs/references/http-websocket-apis/public-api-methods/subscription-methods/subscribe) and [path_find method](/docs/references/http-websocket-apis/public-api-methods/path-and-order-book-methods/path_find) also count towards a client's usage rate.

The usage rate drops off exponentially over time, so a client that does not make requests automatically has its access restored after a period of seconds to minutes.

## See Also

- **Concepts:**
  - [The `rippled` Server](/docs/concepts/networks-and-servers)
  - [Software Ecosystem](/docs/introduction/software-ecosystem)
- **Tutorials:**
  - [Getting Started with XRP Ledger APIs](/docs/tutorials/http-websocket-apis/build-apps/get-started)
  - [Troubleshooting rippled](/docs/infrastructure/troubleshooting)
- **References:**
  - [rippled API Reference](/docs/references/http-websocket-apis)
    - [Error Formatting](/docs/references/http-websocket-apis/api-conventions/error-formatting)



# rippled Server States

Depending on how the `rippled` server is configured, how long it has been running, and other factors, a server may be participating in the global XRP Ledger peer-to-peer network to different degrees. This is represented as the `server_state` field in the responses to the [server_info method](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_info) and [server_state method](/docs/references/http-websocket-apis/public-api-methods/server-info-methods/server_state). The possible responses follow a range of ascending interaction, with each later value superseding the previous one. Their definitions are as follows (in order of increasing priority):

| `Value` | Description |
|  --- | --- |
| `disconnected` | The server is not connected to the XRP Ledger peer-to-peer network whatsoever. It may be running in offline mode, or it may not be able to access the network for whatever reason. |
| `connected` | The server believes it is connected to the network. |
| `syncing` | The server is currently behind on ledger versions. (It is normal for a server to spend a few minutes catching up after you start it.) |
| `tracking` | The server is in agreement with the network |
| `full` | The server is fully caught-up with the network and could participate in validation, but is not doing so (possibly because it has not been configured as a validator). |
| `validating` | The server is currently participating in validation of the ledger |
| `proposing` | The server is participating in validation of the ledger and currently proposing its own version. |


The distinction between `full`, `validating`, and `proposing` is based on synchronization with the rest of the global network, and it is normal for a server to fluctuate between these states as a course of general operation.





# Compact Transaction Identifier

A Compact Transaction Identifier (CTID) is a unique identifier for a validated transaction that applies across any [network](/docs/concepts/networks-and-servers/parallel-networks), not just the XRP Ledger Mainnet.

The differences between a CTID and a transaction's [identifying hash](/docs/concepts/transactions#identifying-transactions) are as follows:

- A CTID identifies a validated transaction based on its network ID, ledger index, and position within the ledger. Since it specifies which network a transaction has been validated on, it can be used in contexts where you are interacting with more than one network, such as connecting to sidechains. A CTID is 64 bits, typically written as 16 characters of uppercase hexadecimal starting with `C`, for example `C005523E00000000`.
- An transaction's identifying hash identifies a signed transaction based on its contents, regardless of if that transaction has been validated on any chains. Since it's a cryptographic hash, it can also be used to prove that the transaction contents are intact. A transaction hash is 256 bits, typically written as 64 characters of hexadecimal, for example `E08D6E9754025BA2534A78707605E0601F03ACE063687A0CA1BDDACFCD1698C7`.


Do not try to use a CTID for a transaction that has not yet been validated. The canonical order of the transaction can change between when the transaction is initially applied and when it is validated by the consensus process, resulting in a CTID that identifies a different transaction or no transaction at all.

## Structure

A CTID contains the following parts, in order (big-endian):

1. 4 bits: The hex nibble `C` indicating that this is a CTID.
2. 28 bits: The ledger index of the ledger where the transaction was validated.
3. 16 bits: The transaction index, its place within the ledger's canonical order. This is provided as the field `TransactionIndex` in [transaction metadata](/docs/references/protocol/transactions/metadata).
4. 16 bits: The [network ID](/docs/references/protocol/transactions/common-fields#networkid-field) of the network that validated this transaction.


The ledger index is normally stored as a 32-bit unsigned integer which increases by 1 each time a new ledger is created. If a network's ledger index is greater than 268,435,455, it won't fit in 28 bits, so the leading `C` should be incremented to `D`, `E`, or `F` as necessary. This is not expected to be necessary until at least the year 2043.

## See Also

For more information including sample code and background, see the [XLS-0037 Standard](https://github.com/XRPLF/XRPL-Standards/tree/master/XLS-0037-concise-transaction-identifier-ctid).



# Short Names of Ledger Entries

Some API methods, specifically the [account_objects method](/docs/references/http-websocket-apis/public-api-methods/account-methods/account_objects) and [ledger_data method](/docs/references/http-websocket-apis/public-api-methods/ledger-methods/ledger_data), allow filtering the ledger entries they return based on the type of ledger entry. The type field you specify can use either the canonical name of the [ledger entry](/docs/references/protocol/ledger-data/ledger-entry-types) or a short name, as in the following table.

The "Ownable" column indicates whether the ledger entry type can appear in owner directories. Ledger entries that are not ownable cannot appear in `account_objects` responses and cannot be used as a `type` filter in that method.

| Canonical Name | Short Name | Ownable | Related Amendment |
|  --- | --- | --- | --- |
| `AccountRoot` | `account` | No |  |
| `Amendments` | `amendments` | No |  |
| `AMM` | `amm` | No |  |
| `Bridge` | `bridge` | Yes |  |
| `Check` | `check` | Yes |  |
| `Credential` | `credential` | Yes |  |
| `Delegate` | `delegate` | Yes |  |
| `DepositPreauth` | `deposit_preauth` | Yes |  |
| `DID` | `did` | Yes |  |
| `DirectoryNode` | `directory` | No |  |
| `Escrow` | `escrow` | Yes |  |
| `FeeSettings` | `fee` | No |  |
| `LedgerHashes` | `hashes` | No |  |
| `MPToken` | `mptoken` | Yes |  |
| `MPTokenIssuance` | `mpt_issuance` | Yes |  |
| `NegativeUNL` | `nunl` | No |  |
| `NFTokenOffer` | `nft_offer` | Yes |  |
| `NFTokenPage` | `nft_page` | Yes |  |
| `Offer` | `offer` | Yes |  |
| `Oracle` | `oracle` | Yes |  |
| `PayChannel` | `payment_channel` | Yes |  |
| `PermissionedDomain` | `permissioned_domain` | Yes |  |
| `RippleState` | `state` | Yes |  |
| `SignerList` | `signer_list` | Yes |  |
| `Ticket` | `ticket` | Yes |  |
| `XChainOwnedClaimID` | `xchain_owned_claim_id` | Yes |  |
| `XChainOwnedCreate``AccountClaimID` | `xchain_owned_``create_account_claim_id` | Yes |  |

















