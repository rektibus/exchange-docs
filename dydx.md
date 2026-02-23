# dYdX v4 (Cosmos SDK Chain + Indexer)

## Architecture
dYdX v4 is a Cosmos SDK appchain. The **Indexer** service provides REST + WS APIs for off-chain data.
- **WS**: `wss://indexer.dydx.trade/v4/ws`
- **REST**: `https://indexer.dydx.trade`

## Products
`GET /v4/perpetualMarkets` → `{markets: {TICKER: {...}}}`

Dict keyed by ticker. Each market:
```json
{
  "ticker": "BTC-USD",
  "status": "ACTIVE",
  "oraclePrice": "66695.51516",
  "nextFundingRate": "-0.00001359",
  "openInterest": "290.9688",
  "stepSize": "0.0001",
  "tickSize": "1",
  "marketType": "CROSS"
}
```
**No explicit `base`/`quote` fields** — derive from `ticker` via split on `-`.

## WebSocket
### Connection
Sends `{type: "connected"}` on connect.

### Subscribe
```json
{"type":"subscribe","channel":"v4_trades","id":"BTC-USD"}
{"type":"subscribe","channel":"v4_orderbook","id":"BTC-USD"}
```
ACK: `{type: "subscribed", channel: "v4_trades", ...}` (includes initial snapshot for orderbook)

### Message Format
All updates: `{type: "channel_data", channel: "v4_trades"|"v4_orderbook", id: "BTC-USD", contents: {...}}`

**Trades** (`channel: "v4_trades"`):
```json
{"type":"channel_data","channel":"v4_trades","id":"BTC-USD","contents":{
  "trades":[{"side":"BUY","size":"0.0003","price":"66686","createdAt":"2026-02-19T05:32:59.174Z"}]
}}
```

**Orderbook Snapshot** (in `subscribed` message):
```json
{"type":"subscribed","channel":"v4_orderbook","contents":{
  "bids":[{"price":"66727","size":"0.0072"},...],
  "asks":[{"price":"66740","size":"0.01"},...]
}}
```

**Orderbook Delta** (in `channel_data` message):
```json
{"type":"channel_data","channel":"v4_orderbook","contents":{
  "bids":[["66727","0.01"]],
  "asks":[["67501","2.8125"]]
}}
```
Note: snapshots use named `{price, size}` objects, deltas use positional `[price, size]` arrays.

### Heartbeat
No WS heartbeat channel — use native ping/pong.

## REST Endpoints

### Trades (Recovery)
`GET /v4/trades/perpetualMarket/{ticker}?limit=100`
```json
{"trades":[{"id":"...","side":"BUY","size":"0.0003","price":"66686","type":"LIMIT","createdAt":"2026-02-19T05:32:59.174Z","createdAtHeight":"76671685"}]}
```
Pagination: `startingBeforeOrAtHeight` parameter.

### Historical Funding
`GET /v4/historicalFunding/{ticker}?limit=100`
```json
{"historicalFunding":[{"ticker":"BTC-USD","rate":"-0.00001","price":"66799.76","effectiveAt":"2026-02-19T05:00:00.562Z"}]}
```
Pagination: `effectiveBeforeOrAt` (ISO datetime).

### OI + Funding (Live Polling)
`GET /v4/perpetualMarkets?ticker={symbol}`
Returns `{markets: {TICKER: {openInterest: "290.96", nextFundingRate: "-0.00001359"}}}`.

### Orderbook
`GET /v4/orderbooks/perpetualMarket/{ticker}`

## Key Details
- All numbers are strings
- Timestamps: ISO 8601
- Side: `BUY`/`SELL` (uppercase)
- No liquidation events via API
- No LS ratio endpoint
- Pagination by block height for trades, by ISO datetime for funding
