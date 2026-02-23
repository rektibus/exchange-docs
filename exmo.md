# Exmo API

<html><head></head><body><h1 id="change-log">Change Log</h1>
<p><strong>2022-02-28</strong></p>
<ul>
<li>Added new parameter <code>pair</code> to the <code>user_open_orders</code> method.</li>
</ul>
<p><strong>2021-07-07</strong></p>
<ul>
<li>Added Margin Websocket API documentation.</li>
</ul>
<p><strong>2021-06-03</strong></p>
<ul>
<li>Added new parameter <code>parent_order_id_str</code> to the <code>stop_market_order_create</code> method.</li>
</ul>
<p><strong>2021-05-20</strong></p>
<ul>
<li>Added new optional parameter <code>order_id</code> to the <code>order_max_quantity</code> method.</li>
</ul>
<p><strong>2021-04-26</strong></p>
<ul>
<li>Added Margin API documentation.</li>
</ul>
<p><strong>2020-11-12</strong></p>
<ul>
<li>Added new optional parameter <code>client_id</code> to the <code>stop_market_order_create</code> method.</li>
</ul>
<p><strong>2020-10-16</strong></p>
<ul>
<li>Added new optional parameter <code>client_id</code> to the <code>order_create</code> method.<br>If this parameter was set, then it'll be also added to the responses of these methods: <code>user_open_orders</code>, <code>user_cancelled_orders</code>, <code>user_trades</code>, <code>order_trades</code>.</li>
</ul>
<p><strong>2020-07-13</strong></p>
<ul>
<li>Added the new method <code>code_check</code></li>
</ul>
<p><strong>2020-07-10</strong></p>
<ul>
<li>Added the new method <code>currency_list_extended</code></li>
</ul>
<p><strong>2020-06-26</strong></p>
<ul>
<li>Added the new method <code>payments_providers_crypto_list</code>.</li>
</ul>
<p><strong>2020-06-22</strong></p>
<ul>
<li>Added <code>original_quantity</code> and <code>original_amount</code> fields to WebSocket API Order entries.</li>
</ul>
<p><strong>2020-06-16</strong></p>
<ul>
<li>Added WebSocket API documentation.</li>
</ul>
<p><strong>2020-04-29</strong></p>
<ul>
<li>Added the new method <code>wallet_operations</code>.</li>
<li>Removed previous limitation about number of API requests from one IP address for <code>Walle

## REST
<p>EXMO offers its users four ways to access API.</p>
<p><strong>Public API</strong></p>
<p>Public API does not require authorization and can be accessed using the GET or POST methods.</p>
<p><strong>Authenticated API</strong></p>
<p>Authenticated API requires authorization and can be accessed using only the POST method.</p>
<p><strong>Excode API</strong></p>
<p>Excode API – private functions available only upon authorization. In order to access these functions, you need to contact the technical

### v1.1
#### Public API
<p>This API does not require authorization and can be accessed using the GET or POST methods.</p>
<p>General URL with API access looks like this: <code>https://api.exmo.com/v1.1/{api_name}?{api_params}</code> where <code>api_name</code> is the name of API you are accessing and <code>api_params</code> are the incoming request parameters (if necessary)</p>


##### trades
**POST** `https://api.exmo.com/v1.1/trades`

##### order_book
**POST** `https://api.exmo.com/v1.1/order_book`

##### ticker
**POST** `https://api.exmo.com/v1.1/ticker`

##### pair_settings
**POST** `https://api.exmo.com/v1.1/pair_settings`

##### currency
**POST** `https://api.exmo.com/v1.1/currency`

##### currency_list_extended
**GET** `https://api.exmo.com/v1.1/currency/list/extended`

##### required_amount
**POST** `https://api.exmo.com/v1.1/required_amount`

##### candles_history
**GET** `https://api.exmo.com/v1.1/candles_history?symbol=BTC_USD&resolution=30&from=1585556979&to=1585557979`

##### payments_providers_crypto_list
**GET** `https://api.exmo.com/v1.1/payments/providers/crypto/list`

#### Authenticated API
<p>To access this API it is necessary to use the POST method.</p>
<p><strong>URL</strong> — should be used the following address: <code>https://api.exmo.com/v1.1/{api_name}</code> where <code>api_name</code> is the name of API method</p>
<p>Authorization is realized by sending the following headers to the server:</p>
<p><strong>Key</strong> — Public key that can be found in user’s profile settings
(example: K-7cc97c89aed2a2fd9ed7792d48d63f65800c447b)</p>
<p><strong>Sign</strong> — POST data (par

##### user_info
**POST** `https://api.exmo.com/v1.1/user_info`

##### order_create
**POST** `https://api.exmo.com/v1.1/order_create`

##### order_cancel
**POST** `https://api.exmo.com/v1.1/order_cancel`

##### stop_market_order_create
**POST** `https://api.exmo.com/v1.1/stop_market_order_create`

##### stop_market_order_cancel
**POST** `https://api.exmo.com/v1.1/stop_market_order_cancel`

##### user_open_orders
**POST** `https://api.exmo.com/v1.1/user_open_orders`

##### user_trades
**POST** `https://api.exmo.com/v1.1/user_trades`

##### user_cancelled_orders
**POST** `https://api.exmo.com/v1.1/user_cancelled_orders`

##### order_trades
**POST** `https://api.exmo.com/v1.1/order_trades`

#### Excode API
<p>Using EXCODE API you can create and upload EXCODE coupons. <strong>The access is given only after a request to the Technical Support.</strong></p>


##### excode_create
**POST** `https://api.exmo.com/v1.1/excode_create`

##### excode_load
**POST** `https://api.exmo.com/v1.1/excode_load`

##### code_check
**POST** `https://api.exmo.com/v1.1/code_check`

#### Wallet API
<p>Wallet API call the same as Authenticated API.</p>


##### deposit_address
**POST** `https://api.exmo.com/v1.1/deposit_address`

##### withdraw_crypt
**POST** `https://api.exmo.com/v1.1/withdraw_crypt`

##### withdraw_get_txid
**POST** `https://api.exmo.com/v1.1/withdraw_get_txid`

##### wallet_history
**POST** `https://api.exmo.com/v1.1/wallet_history`

##### wallet_operations
**POST** `https://api.exmo.com/v1.1/wallet_operations`

#### Margin API
<p>Margin API call the same as Authenticated API.</p>


##### order_create
**POST** `https://api.exmo.com/v1.1/margin/user/order/create`

##### order_update
**POST** `https://api.exmo.com/v1.1/margin/user/order/update`

##### order_cancel
**POST** `https://api.exmo.com/v1.1/margin/user/order/cancel`

##### position_close
**POST** `https://api.exmo.com/v1.1/margin/user/position/close`

##### margin_add
**POST** `https://api.exmo.com/v1.1/margin/user/position/margin_add`

##### margin_remove
**POST** `https://api.exmo.com/v1.1/margin/user/position/margin_remove`

##### currency_list
**POST** `https://api.exmo.com/v1.1/margin/currency/list`

##### pair_list
**POST** `https://api.exmo.com/v1.1/margin/pair/list`

##### settings
**POST** `https://api.exmo.com/v1.1/margin/settings`

##### funding_list
**POST** `https://api.exmo.com/v1.1/margin/funding/list`

##### user_info
**POST** `https://api.exmo.com/v1.1/margin/user/info`

##### order_list
**POST** `https://api.exmo.com/v1.1/margin/user/order/list`

##### order_history
**POST** `https://api.exmo.com/v1.1/margin/user/order/history`

##### order_trades
**POST** `https://api.exmo.com/v1.1/margin/user/order/trades`

##### order_max_quantity
**POST** `https://api.exmo.com/v1.1/margin/user/order/max_quantity`

##### position_list
**POST** `https://api.exmo.com/v1.1/margin/user/position/list`

##### margin_remove_info
**POST** `https://api.exmo.com/v1.1/margin/user/position/margin_remove_info`

##### margin_add_info
**POST** `https://api.exmo.com/v1.1/margin/user/position/margin_add_info`

##### wallet_list
**POST** `https://api.exmo.com/v1.1/margin/user/wallet/list`

##### wallet_history
**POST** `https://api.exmo.com/v1.1/margin/user/wallet/history`

##### user_trade_list
**POST** `https://api.exmo.com/v1.1/margin/user/trade/list`

##### trades
**POST** `https://api.exmo.com/v1.1/margin/trades`

##### liquidation_feed
**POST** `https://api.exmo.com/v1.1/margin/liquidation/feed`

### v1
#### Public API
<p>This API does not require authorization and can be accessed using the GET or POST methods.</p>
<p>General URL with API access looks like this: <code>https://api.exmo.com/v1/{api_name}?{api_params}</code> where <code>api_name</code> is the name of API you are accessing and <code>api_params</code> are the incoming request parameters (if necessary)</p>


##### trades
**POST** `https://api.exmo.com/v1/trades`

##### order_book
**POST** `https://api.exmo.com/v1/order_book`

##### ticker
**POST** `https://api.exmo.com/v1/ticker`

##### pair_settings
**POST** `https://api.exmo.com/v1/pair_settings`

##### currency
**POST** `https://api.exmo.com/v1/currency`

##### required_amount
**POST** `https://api.exmo.com/v1/required_amount`

##### candles_history
**GET** `https://api.exmo.com/v1/candles_history?symbol=BTC_USD&resolution=30&from=1585556979&to=1585557979`

#### Authenticated API
<p>To access this API it is necessary to use the POST method.</p>
<p><strong>URL</strong> — should be used the following address: <code>https://api.exmo.com/v1/{api_name}</code> where <code>api_name</code> is the name of API method</p>
<p>Authorization is realized by sending the following headers to the server:</p>
<p><strong>Key</strong> — Public key that can be found in user’s profile settings
(example: K-7cc97c89aed2a2fd9ed7792d48d63f65800c447b)</p>
<p><strong>Sign</strong> — POST data (param

##### user_info
**POST** `https://api.exmo.com/v1/user_info`

##### order_create
**POST** `https://api.exmo.com/v1/order_create`

##### order_cancel
**POST** `https://api.exmo.com/v1/order_cancel`

##### user_open_orders
**POST** `https://api.exmo.com/v1/user_open_orders`

##### user_trades
**POST** `https://api.exmo.com/v1/user_trades`

##### user_cancelled_orders
**POST** `https://api.exmo.com/v1/user_cancelled_orders`

##### order_trades
**POST** `https://api.exmo.com/v1/order_trades`

#### Excode API
<p>Using EXCODE API you can create and upload EXCODE coupons. <strong>The access is given only after a request to the Technical Support.</strong></p>


##### excode_create
**POST** `https://api.exmo.com/v1/excode_create`

##### excode_load
**POST** `https://api.exmo.com/v1/excode_load`

#### Wallet API
<p>Wallet API call the same as Authenticated API.</p>


##### deposit_address
**POST** `https://api.exmo.com/v1/deposit_address`

##### withdraw_crypt
**POST** `https://api.exmo.com/v1/withdraw_crypt`

##### withdraw_get_txid
**POST** `https://api.exmo.com/v1/withdraw_get_txid`

##### wallet_history
**POST** `https://api.exmo.com/v1/wallet_history`

## Websocket
### v1
#### General
<p>EXMO WS API provides market and user's data in real-time.</p>
<ul>
<li>General endpoint is ws-api.exmo.com</li>
<li>Each message received from API is JSON than contains <code>ts</code> field with current timestamp in UTC timezone in milliseconds and <code>event</code> field representing type of given message</li>
<li>A single connection to a WS API server is valid for 24 hours</li>
<li>WS API server sends a ping frame every 3 minutes. If server does not receive a pong frame back within a 10-m

#### Public API
<p>Public API allows to get market data in real-time.
To use this API it is necessary to establish websocket connection on <code>wss://ws-api.exmo.com:443/v1/public</code>.</p>
<p>Data provided:</p>
<ul>
<li>trades</li>
<li>ticker</li>
<li>order book changes</li>
</ul>
<p>To start receiving this data you need to send a subscribe command message into the connection with topics you wish</p>


##### Trades
<p><strong>Data:</strong> all trades by certain pair since subscription time</p>
<p><strong>Topics name:</strong> spot/trades:&lt;**pair**&gt;</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> -</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "update",
  "topic": "spot/trades:BTC_USD",
  "data": [
    {
      "trade_id": 3,
      "type": "sell",
      "price": "100",
      "quantity": "1",
      "amount": "100"

##### Ticker
<p><strong>Data:</strong> exchange ticker</p>
<p><strong>Topics name:</strong> spot/ticker:&lt;**pair**&gt;</p>
<p><strong>Update speed:</strong> approximately 10s</p>
<p><strong>Snapshot:</strong> -</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "update",
  "topic": "spot/ticker:BTC_USD",
  "data": {
    "buy_price": "9740.48",
    "sell_price": "9745.33",
    "last_trade": "9742.2",
    "high": "9800",
    "low": "9667.16",
    "avg": "973

##### Order book snapshots
<p><strong>Data:</strong> top-25 order book positions</p>
<p><strong>Topics name:</strong> spot/order_book_snapshots:&lt;**pair**&gt;</p>
<p><strong>Update speed:</strong> 100ms</p>
<p><strong>Snapshot:</strong> -</p>
<p>Order book position format is JSON array of 3 numbers:
<code>["price","quantity","amount"]</code></p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "update",
  "topic": "spot/order_book_snapshots:BTC_USD",
  "data": {
    "ask"

##### Order book updates
<p><strong>Data:</strong> top-400 order book updates</p>
<p><strong>Topics name:</strong> spot/order_book_updates:&lt;**pair**&gt;</p>
<p><strong>Update speed:</strong> 100ms</p>
<p><strong>Snapshot:</strong> Top-400 order book positions</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "snapshot",
  "topic": "spot/order_book_updates:BTC_USD",
  "data": {
    "ask": [["100","3","300"],["200","4","800"]],
    "bid": [["99","2","198"],["98","1","

#### Authenticated API
<p>Authenticated API allows one to get user trades, wallets changes, and order changes in real-time.</p>
<p>To use this API, it is necessary to establish websocket connection on <code>wss://ws-api.exmo.com:443/v1/private</code> and then log in using the Login method. Otherwise the connection will be terminated by server side in 30s</p>
<p>Data provided:</p>
<ul>
<li>user trades</li>
<li>wallet changes</li>
<li>orders changes</li>
</ul>


##### Login
<p>Command format:</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "method": "login",
  "id": 1,
  "api_key": "your_api_key",
  "sign": "your_sign",
  "nonce": 1574427585174
}
</code></pre><ul>
<li><strong>api_key</strong> is public key that can be found in user’s profile settings (example: K-7cc97c89aed2a2fd9ed7792d48d63f65800c447b)</li>
<li><strong>nonce</strong> is incremental numerical value (&gt;0) that should never be reiterated or decreased.</li>
<li><strong>sign</st

##### User trades
<p><strong>Data:</strong> all trades associated with the user since subscription time</p>
<p><strong>Topics name:</strong> spot/user_trades</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> -</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "update",
  "topic": "spot/user_trades",
  "data": {
    "trade_id": 51251,
    "type": "sell",
    "price": "7728",
    "quantity": "0.002",
    "amount": "15.456",
    "dat

##### Wallets
<p><strong>Data:</strong> all states of wallets since subscription time</p>
<p><strong>Topics name:</strong> spot/wallet</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> User wallets by all currencies on exchange</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "snapshot",
  "topic": "spot/wallet",
  "data": {
    "balances": {
      "BTC": "3",
      "USD": "1000"
    },
    "reserved": {
      "BTC": "0.5",
 

##### Orders
<p><strong>Data:</strong> all states of orders since subscription time</p>
<p><strong>Topics name:</strong> spot/orders</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> All limit orders and open stop orders</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
  "ts": 1574427585174,
  "event": "snapshot",
  "topic": "spot/orders",
  "data": [
    {
      "order_id": "14",
      "client_id":"100500",
      "created": "1574427585",
      "pair": "BTC_

#### Margin Authenticated API
<p>Margin Authenticated API allows one to get user margin trades, wallet and order changes in real-time.</p>
<p>To use this API, it is necessary to establish a websocket connection on <code>wss://ws-api.exmo.com:443/v1/margin/private</code> and then log in using the Login method. Otherwise the connection will be terminated by a server side in 30 seconds.</p>
<p>Data provided:</p>
<ul>
<li>user trades</li>
<li>wallet changes</li>
<li>order changes</li>
<li>user positions</li>
</ul>


##### Wallets
<p><strong>Data:</strong> all states of user wallets</p>
<p><strong>Topic name:</strong> margin/wallet</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> User wallets by all currencies on the exchange</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
   "ts":1624370076651,
   "event":"snapshot",
   "topic":"margin/wallets",
   "data":{
      "USDT":{
         "balance":"1000000",
         "used":"0",
         "free":"1000000"
      },
      "USD":

##### Orders
<p><strong>Data:</strong> all states of orders associated with the user</p>
<p><strong>Topic name:</strong> margin/orders</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> All orders</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
   "ts":1624371281773,
   "event":"snapshot",
   "topic":"margin/orders",
   "data":[
      {
         "order_id":"692844278081168665",
         "created":"1624371250919761600",
         "type":"limit_buy",
         "

##### User trades
<p><strong>Data:</strong> all trades associated with the user</p>
<p><strong>Topic name:</strong> margin/user_trades</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> last 100 user trades</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
   "ts":1624369720168,
   "event":"snapshot",
   "topic":"margin/user_trades",
   "data":[
      {
         "trade_id":"692844278081167054",
         "trade_dt":"1624369773990729200",
         "type":"buy",
     

##### Positions
<p><strong>Data:</strong> all positions associated with the user</p>
<p><strong>Topic name:</strong> margin/positions</p>
<p><strong>Update speed:</strong> real-time</p>
<p><strong>Snapshot:</strong> open user positions</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>{
   "ts":1624369965122,
   "event":"snapshot",
   "topic":"margin/positions",
   "data":[
      {
         "position_id":"692844278081167060",
         "created":"1624369773993800300",
         "pair":"BTC_USD",
 
