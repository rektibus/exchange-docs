# Hyperliquid API Documentation

Comprehensive reference for the Hyperliquid DEX API. Covers Info endpoint, Exchange endpoint, WebSocket subscriptions, and Python SDK types.

**Base URLs:**
- Mainnet REST: `https://api.hyperliquid.xyz`
- Mainnet WS: `wss://api.hyperliquid.xyz/ws`
- Testnet REST: `https://api.hyperliquid-testnet.xyz`
- Testnet WS: `wss://api.hyperliquid-testnet.xyz/ws`

All REST endpoints use POST with `Content-Type: application/json`.

---

# Info Endpoint

`POST https://api.hyperliquid.xyz/info`

## General Info Requests

### Retrieve mids for all coins
```json
{"type": "allMids"}
```
Optional: `dex` (perp dex name, defaults to first perp dex).

### Retrieve a user's open orders
```json
{"type": "openOrders", "user": "0x..."}
```

### Retrieve a user's open orders with frontend info
```json
{"type": "frontendOpenOrders", "user": "0x..."}
```

### Retrieve a user's fills
```json
{"type": "userFills", "user": "0x..."}
```
Returns at most 2000 most recent fills. Optional: `aggregateByTime: bool`.

**Fill format:**
```json
{
  "coin": "ARK",
  "px": "0.17936",
  "sz": "106.0",
  "side": "A",
  "time": 1772648968809,
  "startPosition": "-48183.0",
  "dir": "Open Short",
  "closedPnl": "0.0",
  "hash": "0x...",
  "oid": 338302315146,
  "crossed": true,
  "fee": "0.0",
  "tid": 445182652951374,
  "feeToken": "USDC",
  "twapId": null
}
```
> **NOTE**: Fills do NOT contain a `liquidation` field. Side is `"A"` (sell/ask) or `"B"` (buy/bid).

### Retrieve a user's fills by time
```json
{"type": "userFillsByTime", "user": "0x...", "startTime": 1234567890000}
```
Returns at most 2000 fills. Only the 10000 most recent fills are available. Optional: `endTime`, `aggregateByTime`.

### L2 Book snapshot
```json
{"type": "l2Book", "coin": "BTC"}
```
Returns at most 20 levels per side. Optional: `nSigFigs` (2-5), `mantissa` (1,2,5 — only if nSigFigs=5).

### Candle snapshot
```json
{"type": "candleSnapshot", "req": {"coin": "ETH", "interval": "1h", "startTime": 1234567890000, "endTime": 1234567899999}}
```
Only the most recent 5000 candles are available. Supported intervals: `1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 8h, 12h, 1d, 3d, 1w, 1M`.

### Query order status
```json
{"type": "orderStatus", "user": "0x...", "oid": 12345}
```
`oid` can be u64 order id or 16-byte hex cloid string.

**Order statuses**: `open`, `filled`, `canceled`, `triggered`, `rejected`, `marginCanceled`, `vaultWithdrawalCanceled`, `openInterestCapCanceled`, `selfTradeCanceled`, `reduceOnlyCanceled`, `siblingFilledCanceled`, `delistedCanceled`, `liquidatedCanceled`, `scheduledCancel`, `tickRejected`, `minTradeNtlRejected`, `perpMarginRejected`, `reduceOnlyRejected`, `badAloPxRejected`, `iocCancelRejected`, `badTriggerPxRejected`, `marketOrderNoLiquidityRejected`, `positionIncreaseAtOpenInterestCapRejected`, `positionFlipAtOpenInterestCapRejected`, `tooAggressiveAtOpenInterestCapRejected`, `openInterestIncreaseRejected`, `insufficientSpotBalanceRejected`, `oracleRejected`, `perpMaxPositionRejected`.

### Check builder fee approval
```json
{"type": "maxBuilderFee", "user": "0x...", "builder": "0x..."}
```

### Retrieve a user's historical orders
```json
{"type": "historicalOrders", "user": "0x..."}
```
Returns at most 2000 most recent historical orders.

### User rate limits
```json
{"type": "userRateLimit", "user": "0x..."}
```

---

## Perpetuals-Specific Info

### Retrieve all perpetual dexs
```json
{"type": "perpDexs"}
```

### Retrieve perpetuals metadata (universe + margin tables)
```json
{"type": "meta"}
```
Optional: `dex`. Returns `{"universe": [{"name": "BTC", "szDecimals": 5, ...}]}`.

### Retrieve perpetuals asset contexts (mark price, funding, OI)
```json
{"type": "metaAndAssetCtxs"}
```
Returns `[Meta, [AssetCtx, ...]]`. AssetCtx fields: `funding`, `openInterest`, `prevDayPx`, `dayNtlVlm`, `premium`, `oraclePx`, `markPx`, `midPx`, `impactPxs`, `dayBaseVlm`.

### Retrieve user's perpetuals account summary
```json
{"type": "clearinghouseState", "user": "0x..."}
```
Returns open positions and margin summary.

### Retrieve user's funding history or non-funding ledger updates
```json
{"type": "userFunding", "user": "0x...", "startTime": 1234567890000}
```
Or:
```json
{"type": "userNonFundingLedgerUpdates", "user": "0x...", "startTime": 1234567890000}
```
Non-funding ledger updates include deposits, transfers, withdrawals, and **liquidations**. Optional: `endTime`.

### Retrieve historical funding rates
```json
{"type": "fundingHistory", "coin": "ETH", "startTime": 1234567890000}
```
Optional: `endTime`.

### Retrieve predicted funding rates
```json
{"type": "predictedFundings"}
```

### Query perps at open interest caps
```json
{"type": "perpsAtOpenInterestCaps"}
```

---

## Spot-Specific Info

### Retrieve spot metadata
```json
{"type": "spotMeta"}
```

### Retrieve spot metadata and asset contexts
```json
{"type": "spotMetaAndAssetCtxs"}
```

### Retrieve spot account summary
```json
{"type": "spotClearinghouseState", "user": "0x..."}
```

---

## Vault Info

### Retrieve vault details
```json
{"type": "vaultDetails", "vaultAddress": "0x..."}
```
Returns: `name`, `vaultAddress`, `leader`, `description`, `portfolio`, `apr`, `followers`, `maxDistributable`, `maxWithdrawable`, `isClosed`, `relationship` (parent/child), `allowDeposits`.

**HLP Vault**: `0xdfc24b077bc1425ad1dea75bcb6f8158e10df303` — Hyperliquidity Provider. Has 7 child sub-accounts for different strategies. Description: "provides liquidity, performs liquidations, and accrues platform fees."

**HLP Child Addresses** (as of 2026-03):
- `0x010461c14e146ac35fe42271bdc1134ee31c703a` (active, 2000+ fills/hr)
- `0x2e3d94f0562703b25c83308a05046ddaf9a8dd14`
- `0x2ed5c4484ea3ff8b57d5f2fb152a40d9f2b68308`
- `0x31ca8395cf837de08b24da3f660e77761dfb974b` (active, 2000+ fills/hr)
- `0x469f690213c467c39a23efacfd2816896009d7d8`
- `0x5e177e5e39c0f4e421f5865a6d8beed8d921cb70`
- `0xb0a55f13d22f66e6d495ac98113841b2326e9540`

### Retrieve all vault summaries
```json
{"type": "vaultSummaries"}
```

---

# Exchange Endpoint

`POST https://api.hyperliquid.xyz/exchange`

All exchange requests require `action`, `nonce`, `signature`. Optional: `vaultAddress` (for vault/subaccount trading), `expiresAfter` (ms timestamp).

### Asset IDs
- Perps: index in `meta.universe` array (0-based)
- Spot: `10000 + index` in `spotMeta.universe`

### Subaccounts and Vaults
Subaccounts/vaults don't have private keys. Sign with master account and set `vaultAddress`.

## Place an order
```json
{
  "action": {
    "type": "order",
    "orders": [{
      "a": 0,
      "b": true,
      "p": "50000.0",
      "s": "0.01",
      "r": false,
      "t": {"limit": {"tif": "Gtc"}},
      "c": "0x..."
    }],
    "grouping": "na",
    "builder": {"b": "0x...", "f": 10}
  },
  "nonce": 1234567890000,
  "signature": {...}
}
```
Keys: `a`=asset, `b`=isBuy, `p`=price, `s`=size, `r`=reduceOnly, `t`=type, `c`=cloid (optional).
TIF: `Alo` (post-only), `Ioc` (immediate-or-cancel), `Gtc` (good-til-canceled).
Trigger orders: `{"trigger": {"isMarket": true, "triggerPx": "50000.0", "tpsl": "tp"}}`.
Builder: `b`=builder address, `f`=fee in tenths of basis points (10 = 1bp).

## Cancel order(s)
```json
{"action": {"type": "cancel", "cancels": [{"a": 0, "o": 12345}]}, "nonce": ..., "signature": ...}
```
Keys: `a`=asset, `o`=oid.

## Cancel by cloid
```json
{"action": {"type": "cancelByCloid", "cancels": [{"asset": 0, "cloid": "0x..."}]}, "nonce": ..., "signature": ...}
```

## Schedule cancel (dead man's switch)
```json
{"action": {"type": "scheduleCancel", "time": 1234567890000}, "nonce": ..., "signature": ...}
```
Set `time` to null to cancel the scheduled cancel.

## Modify an order
```json
{"action": {"type": "batchModify", "modifies": [{"oid": 12345, "order": {...}}]}, "nonce": ..., "signature": ...}
```

## Update leverage
```json
{"action": {"type": "updateLeverage", "asset": 0, "isCross": true, "leverage": 10}, "nonce": ..., "signature": ...}
```

## Update isolated margin
```json
{"action": {"type": "updateIsolatedMargin", "asset": 0, "isBuy": true, "ntli": 100}, "nonce": ..., "signature": ...}
```

## USDC Transfer
```json
{"action": {"type": "usdClassTransfer", "amount": "100.0", "toPerp": true, "nonce": ...}, "nonce": ..., "signature": ...}
```

## Vault deposit/withdraw
```json
{"action": {"type": "vaultTransfer", "vault": "0x...", "isDeposit": true, "usd": 1000.0}, "nonce": ..., "signature": ...}
```

## TWAP Orders
Place: `{"action": {"type": "twapOrder", "twap": {"a": 0, "b": true, "s": "1.0", "r": false, "m": 5, "t": true}}}`.
Keys: `a`=asset, `b`=isBuy, `s`=size, `r`=reduceOnly, `m`=minutes, `t`=randomize.
Cancel: `{"action": {"type": "twapCancel", "a": 0, "t": 12345}}`.

## Approve API wallet
```json
{"action": {"type": "approveAgent", "agentAddress": "0x...", "agentName": "my-bot"}, "nonce": ..., "signature": ...}
```

## Approve builder fee
```json
{"action": {"type": "approveBuilderFee", "maxFeeRate": "0.001%", "builder": "0x...", "nonce": ...}, "nonce": ..., "signature": ...}
```

---

# WebSocket API

`wss://api.hyperliquid.xyz/ws`

## Connecting
```
wscat -c wss://api.hyperliquid.xyz/ws
> {"method": "subscribe", "subscription": {"type": "trades", "coin": "SOL"}}
< {"channel":"subscriptionResponse","data":{"method":"subscribe","subscription":{"type":"trades","coin":"SOL"}}}
```

Handle disconnects gracefully. Missed data available via snapshot ack on reconnect or corresponding info request.

## Subscription Types

| Type | Subscribe Message | Data Format | Notes |
|------|------------------|-------------|-------|
| `allMids` | `{"type": "allMids"}` | `AllMids` | Optional: `dex` |
| `bbo` | `{"type": "bbo", "coin": "<coin>"}` | `WsBbo` | Only fires on bbo change |
| `l2Book` | `{"type": "l2Book", "coin": "<coin>"}` | `WsBook` | Optional: `nSigFigs`, `mantissa` |
| `trades` | `{"type": "trades", "coin": "<coin>"}` | `WsTrade[]` | |
| `candle` | `{"type": "candle", "coin": "<coin>", "interval": "<interval>"}` | `Candle[]` | |
| `orderUpdates` | `{"type": "orderUpdates", "user": "<addr>"}` | `WsOrder[]` | |
| `userEvents` | `{"type": "userEvents", "user": "<addr>"}` | `WsUserEvent` | fills, funding, **liquidation**, nonUserCancel |
| `userFills` | `{"type": "userFills", "user": "<addr>"}` | `WsUserFills` | Optional: `aggregateByTime` |
| `userFundings` | `{"type": "userFundings", "user": "<addr>"}` | `WsUserFundings` | |
| `userNonFundingLedgerUpdates` | `{"type": "userNonFundingLedgerUpdates", "user": "<addr>"}` | `WsUserNonFundingLedgerUpdates` | deposits, transfers, withdrawals, **liquidations** |
| `activeAssetCtx` | `{"type": "activeAssetCtx", "coin": "<coin>"}` | `WsActiveAssetCtx` | funding + OI |
| `activeAssetData` | `{"type": "activeAssetData", "user": "<addr>", "coin": "<coin>"}` | `WsActiveAssetData` | Perps only |
| `clearinghouseState` | `{"type": "clearinghouseState", "user": "<addr>"}` | `ClearinghouseState` | Optional: `dex` |
| `openOrders` | `{"type": "openOrders", "user": "<addr>"}` | `OpenOrders` | Optional: `dex` |
| `notification` | `{"type": "notification", "user": "<addr>"}` | `Notification` | |
| `webData3` | `{"type": "webData3", "user": "<addr>"}` | `WebData3` | |
| `userTwapSliceFills` | `{"type": "userTwapSliceFills", "user": "<addr>"}` | `WsUserTwapSliceFills` | |
| `userTwapHistory` | `{"type": "userTwapHistory", "user": "<addr>"}` | `WsUserTwapHistory` | |
| `twapStates` | `{"type": "twapStates", "user": "<addr>"}` | `TwapStates` | Optional: `dex` |

## Data Formats

Server responds to subscriptions with `channel: "subscriptionResponse"`. Then streams with `channel` set to subscription type and `data` containing the payload.

For streaming user endpoints (`WsUserFills`, `WsUserFundings`), first message has `isSnapshot: true`, subsequent updates have `isSnapshot: false`.

### WsUserEvent (IMPORTANT for liquidations)
```typescript
WsUserEvent = {
  "fills": WsFill[]     // OR
  "funding": WsUserFunding  // OR
  "liquidation": WsLiquidation  // OR
  "nonUserCancel": WsNonUserCancel[]
}
```
This is a discriminated union — only ONE variant per message.

### WsBook
```typescript
WsBook = { coin: string, levels: [WsLevel[], WsLevel[]], time: number }
WsLevel = { px: string, sz: string, n: number }
```

### WsTrade
```typescript
WsTrade = { coin: string, side: "A" | "B", px: string, sz: string, hash: string, time: number, tid: number }
```

### WsActiveAssetCtx
```typescript
WsActiveAssetCtx = {
  coin: string,
  ctx: {
    funding: string,
    openInterest: string,
    prevDayPx: string,
    dayNtlVlm: string,
    premium: string,
    oraclePx: string,
    markPx: string,
    midPx: string | null,
    impactPxs: [string, string] | null,
    dayBaseVlm: string
  }
}
```

### Fill (used in userFills and userEvents)
```typescript
Fill = {
  coin: string,
  px: string,
  sz: string,
  side: "A" | "B",
  time: number,
  startPosition: string,
  dir: string,           // "Open Long", "Open Short", "Close Long", "Close Short"
  closedPnl: string,
  hash: string,
  oid: number,
  crossed: boolean,
  fee: string,
  tid: number,
  feeToken: string,
  twapId: number | null
}
```

## WS Post Requests

Can send info/exchange requests over WS:
```json
{"method": "post", "id": 1, "request": {"type": "info", "payload": {"type": "allMids"}}}
```
Response:
```json
{"channel": "post", "data": {"id": 1, "response": {"type": "info", "payload": {...}}}}
```

## Unsubscribing
```json
{"method": "unsubscribe", "subscription": {"type": "trades", "coin": "SOL"}}
```

---

# Signing

Use existing SDK instead of manually generating signatures. Two signing schemes:
- `sign_l1_action` — for L1 actions
- `sign_user_signed_action` — for user-signed actions

Common errors:
1. Using wrong signing scheme
2. Field order matters for msgpack
3. Trailing zeroes on numbers
4. Uppercase characters in address fields (always lowercase before signing)
5. Believing signature is correct because local recover works — payload construction may differ

---

# Rate Limits

## Weight-based
- Exchange requests: `1 + floor(batch_length / 40)`
- Info/l2Book/allMids/clearinghouseState/orderStatus/spotClearinghouseState/exchangeStatus: weight 2
- Info/userRole: weight 60
- All other info: weight 20
- Some info endpoints have additional weight per 20 items returned: `recentTrades`, `historicalOrders`, `userFills`, `userFillsByTime`, `fundingHistory`, `userFunding`, `nonUserFundingUpdates`, `twapHistory`, `userTwapSliceFills`
- `candleSnapshot`: additional weight per 60 items returned
- Explorer: weight 40

## Connection Limits
- Max 10 websocket connections
- Max 30 new WS connections per minute
- Max 1000 WS subscriptions
- Max 10 unique users across user-specific WS subscriptions
- Max 2000 messages sent per minute across all WS connections
- Max 100 simultaneous inflight post messages
- Max 100 EVM JSON-RPC requests per minute for `rpc.hyperliquid.xyz/evm`

---

# Python SDK Type Definitions

Source: `hyperliquid-dex/hyperliquid-python-sdk` — `hyperliquid/utils/types.py`

```python
from typing import Any, Dict, List, Literal, Optional, Tuple, TypedDict, Union

# === Core Types ===
Side = Union[Literal["A"], Literal["B"]]
SIDES: List[Side] = ["A", "B"]

AssetInfo = TypedDict("AssetInfo", {"name": str, "szDecimals": int})
Meta = TypedDict("Meta", {"universe": List[AssetInfo]})

SpotAssetInfo = TypedDict("SpotAssetInfo", {"name": str, "tokens": List[int], "index": int, "isCanonical": bool})
SpotTokenInfo = TypedDict("SpotTokenInfo", {
    "name": str, "szDecimals": int, "weiDecimals": int, "index": int,
    "tokenId": str, "isCanonical": bool, "evmContract": Optional[str], "fullName": Optional[str],
})
SpotMeta = TypedDict("SpotMeta", {"universe": List[SpotAssetInfo], "tokens": List[SpotTokenInfo]})
SpotAssetCtx = TypedDict("SpotAssetCtx", {
    "dayNtlVlm": str, "markPx": str, "midPx": Optional[str],
    "prevDayPx": str, "circulatingSupply": str, "coin": str,
})

# === Subscription Types ===
AllMidsSubscription = TypedDict("AllMidsSubscription", {"type": Literal["allMids"]})
BboSubscription = TypedDict("BboSubscription", {"type": Literal["bbo"], "coin": str})
L2BookSubscription = TypedDict("L2BookSubscription", {"type": Literal["l2Book"], "coin": str})
TradesSubscription = TypedDict("TradesSubscription", {"type": Literal["trades"], "coin": str})
UserEventsSubscription = TypedDict("UserEventsSubscription", {"type": Literal["userEvents"], "user": str})
UserFillsSubscription = TypedDict("UserFillsSubscription", {"type": Literal["userFills"], "user": str})
CandleSubscription = TypedDict("CandleSubscription", {"type": Literal["candle"], "coin": str, "interval": str})
OrderUpdatesSubscription = TypedDict("OrderUpdatesSubscription", {"type": Literal["orderUpdates"], "user": str})
UserFundingsSubscription = TypedDict("UserFundingsSubscription", {"type": Literal["userFundings"], "user": str})
UserNonFundingLedgerUpdatesSubscription = TypedDict(
    "UserNonFundingLedgerUpdatesSubscription", {"type": Literal["userNonFundingLedgerUpdates"], "user": str}
)
ActiveAssetCtxSubscription = TypedDict("ActiveAssetCtxSubscription", {"type": Literal["activeAssetCtx"], "coin": str})
ActiveAssetDataSubscription = TypedDict(
    "ActiveAssetDataSubscription", {"type": Literal["activeAssetData"], "user": str, "coin": str}
)

Subscription = Union[
    AllMidsSubscription, BboSubscription, L2BookSubscription, TradesSubscription,
    UserEventsSubscription, UserFillsSubscription, CandleSubscription, OrderUpdatesSubscription,
    UserFundingsSubscription, UserNonFundingLedgerUpdatesSubscription,
    ActiveAssetCtxSubscription, ActiveAssetDataSubscription,
]

# === WS Message Types ===
L2Level = TypedDict("L2Level", {"px": str, "sz": str, "n": int})
L2BookData = TypedDict("L2BookData", {"coin": str, "levels": Tuple[List[L2Level], List[L2Level]], "time": int})
L2BookMsg = TypedDict("L2BookMsg", {"channel": Literal["l2Book"], "data": L2BookData})
BboData = TypedDict("BboData", {"coin": str, "time": int, "bbo": Tuple[Optional[L2Level], Optional[L2Level]]})
BboMsg = TypedDict("BboMsg", {"channel": Literal["bbo"], "data": BboData})
Trade = TypedDict("Trade", {"coin": str, "side": Side, "px": str, "sz": int, "hash": str, "time": int})
TradesMsg = TypedDict("TradesMsg", {"channel": Literal["trades"], "data": List[Trade]})
PongMsg = TypedDict("PongMsg", {"channel": Literal["pong"]})
AllMidsData = TypedDict("AllMidsData", {"mids": Dict[str, str]})
AllMidsMsg = TypedDict("AllMidsMsg", {"channel": Literal["allMids"], "data": AllMidsData})

PerpAssetCtx = TypedDict("PerpAssetCtx", {
    "funding": str, "openInterest": str, "prevDayPx": str, "dayNtlVlm": str,
    "premium": str, "oraclePx": str, "markPx": str, "midPx": Optional[str],
    "impactPxs": Optional[Tuple[str, str]], "dayBaseVlm": str,
})
ActiveAssetCtx = TypedDict("ActiveAssetCtx", {"coin": str, "ctx": PerpAssetCtx})
ActiveAssetCtxMsg = TypedDict("ActiveAssetCtxMsg", {"channel": Literal["activeAssetCtx"], "data": ActiveAssetCtx})

CrossLeverage = TypedDict("CrossLeverage", {"type": Literal["cross"], "value": int})
IsolatedLeverage = TypedDict("IsolatedLeverage", {"type": Literal["isolated"], "value": int, "rawUsd": str})
Leverage = Union[CrossLeverage, IsolatedLeverage]

ActiveAssetData = TypedDict("ActiveAssetData", {
    "user": str, "coin": str, "leverage": Leverage,
    "maxTradeSzs": Tuple[str, str], "availableToTrade": Tuple[str, str], "markPx": str,
})
ActiveAssetDataMsg = TypedDict("ActiveAssetDataMsg", {"channel": Literal["activeAssetData"], "data": ActiveAssetData})

# Fill type — used in userFills and userEvents
Fill = TypedDict("Fill", {
    "coin": str, "px": str, "sz": str, "side": Side, "time": int,
    "startPosition": str, "dir": str, "closedPnl": str, "hash": str,
    "oid": int, "crossed": bool, "fee": str, "tid": int, "feeToken": str,
})

# NOTE: UserEventsData uses total=False — fields are optional (union type)
# The actual variants are: fills, funding, liquidation, nonUserCancel
# SDK TODO says: "handle other types of user events"
UserEventsData = TypedDict("UserEventsData", {"fills": List[Fill]}, total=False)
UserEventsMsg = TypedDict("UserEventsMsg", {"channel": Literal["user"], "data": UserEventsData})

UserFillsData = TypedDict("UserFillsData", {"user": str, "isSnapshot": bool, "fills": List[Fill]})
UserFillsMsg = TypedDict("UserFillsMsg", {"channel": Literal["userFills"], "data": UserFillsData})

# Builder fee
BuilderInfo = TypedDict("BuilderInfo", {"b": str, "f": int})

# Cloid — 128-bit hex string (16 bytes), prefixed with 0x
# Example: 0x1234567890abcdef1234567890abcdef
```

---

# Liquidation Data on Hyperliquid

## Liquidation Mechanism

Two types of liquidations:

### 1. Market Liquidations (`method: "market"`)
Clearinghouse places a market order to close the user's position. Any trader on the book can fill it. No specific counterparty.

### 2. Backstop / HLP Vault Liquidations (`method: "backstop"`)
When market liquidation fails (insufficient liquidity), the HLP vault absorbs the position directly.

**HLP Liquidation Child**: `0xb0a55f13d22f66e6d495ac98113841b2326e9540` — confirmed from Allium node data.

## Liquidation Fill Format (verified from Allium)

The `liquidation` key is **only present** on liquidation fills — absent on regular fills. When present:

### Liquidated User Fill (both market and backstop)
```json
{
  "coin": "ETH",
  "px": "2316.0",
  "sz": "0.1037",
  "side": "A",
  "time": 1750541100096,
  "dir": "Liquidated Isolated Long",
  "closedPnl": "-9.94483",
  "crossed": false,
  "fee": "0.0",
  "feeToken": "USDC",
  "hash": "0x1328...",
  "oid": 104754754832,
  "tid": 361622066638684,
  "startPosition": "0.1037",
  "liquidation": {
    "liquidatedUser": "0x4e8ffa69c78d7a067e1795fbe16a5c80c90b6c05",
    "markPx": "2323.3",
    "method": "backstop"
  }
}
```

### HLP Vault Fill (backstop only — HLP is the counterparty)
```json
{
  "coin": "ETH",
  "px": "2316.0",
  "sz": "0.1037",
  "side": "B",
  "time": 1750541100096,
  "dir": "Liquidated Isolated Long",
  "closedPnl": "0.0",
  "crossed": true,
  "liquidation": {
    "liquidatedUser": "0x4e8ffa69c78d7a067e1795fbe16a5c80c90b6c05",
    "markPx": "2323.3",
    "method": "backstop"
  }
}
```

### Ledger Event (misc_events)
```json
{
  "hash": "0x1328...",
  "inner": {
    "LedgerUpdate": {
      "delta": {
        "accountValue": "0.756264",
        "leverageType": "Isolated",
        "liquidatedNtlPos": "240.92621",
        "liquidatedPositions": [{"coin": "ETH", "szi": "0.1037"}],
        "type": "liquidation"
      },
      "users": ["0x4e8ffa69c78d7a067e1795fbe16a5c80c90b6c05"]
    }
  },
  "time": "2025-06-21T21:25:00.096291909"
}
```

## Key Fields

| Field | Purpose |
|-------|---------|
| `liquidation` | Only present on liquidation fills — the main discriminator |
| `liquidation.liquidatedUser` | Address of the liquidated user |
| `liquidation.markPx` | Mark price at time of liquidation |
| `liquidation.method` | `"market"` or `"backstop"` |
| `dir` | Contains `"Liquidated"` prefix on liquidation fills |

## Detection Strategy for EnsoX

Subscribe to `userFills` for HLP liquidation child `0xb0a5...9540`. Filter fills with `liquidation` key. This captures **backstop liquidations** (large, meaningful — market liquidity failed). Market liquidations (clearinghouse market orders filled by regular traders) are not visible from any single address subscription.

## HLP Vault Structure

| Address | Role | Activity |
|---------|------|----------|
| `0xdfc24b077bc1425ad1dea75bcb6f8158e10df303` | Parent vault | No fills (delegates to children) |
| `0x010461c14e146ac35fe42271bdc1134ee31c703a` | MM child | 2000+ fills/hr (active market making) |
| `0x31ca8395cf837de08b24da3f660e77761dfb974b` | MM child | 2000+ fills/hr (active market making) |
| `0xb0a55f13d22f66e6d495ac98113841b2326e9540` | **Liquidation child** | Infrequent — only activates on backstop events |
| `0x2e3d94f0562703b25c83308a05046ddaf9a8dd14` | Inactive | |
| `0x2ed5c4484ea3ff8b57d5f2fb152a40d9f2b68308` | Inactive | |
| `0x469f690213c467c39a23efacfd2816896009d7d8` | Inactive | |
| `0x5e177e5e39c0f4e421f5865a6d8beed8d921cb70` | Inactive | |

## Trade IDs

Trade IDs are NOT guaranteed to be unique. They are a 50-bit hash of buyer and seller order IDs. For unique identification use: `coin + timestamp + trade_id` for trades, additionally `user` for fills.

## Public Trade Stream

REST `recentTrades` includes `users: [addr1, addr2]` (counterparty addresses). The WS `trades` stream data format (`WsTrade`): `{coin, side, px, sz, hash, time, tid}` — does NOT include `users` in the WS stream.

## Source

Allium: Hyperliquid data provider running in-house nodes. Provides `hyperliquid.raw.fills`, `hyperliquid.raw.misc_events` with complete liquidation data. See `hyperliquid.dex.trades` enriched table for `liquidated_user`, `liquidation_mark_price`, `liquidation_method` columns.

---

# Liquidation Mechanics (from official Hyperliquid docs)

## Trigger
Account equity drops below **maintenance margin** (half of initial margin at max leverage).
- 3x leverage → maintenance margin = 16.67%
- 10x leverage → maintenance margin = 5%
- 40x leverage → maintenance margin = 1.25%

## Two Liquidation Phases

### Phase 1: Market Liquidation (Order Book)
- Clearinghouse sends market orders to the book
- **All users can compete** for liquidation flow — no clearance fee
- For positions >100K USDC: only **20% liquidated first**, 30s cooldown, then full position
- Uses **mark price** (combines external CEX prices + Hyperliquid book state)

### Phase 2: Backstop Liquidation (HLP Vault)
- Triggers when equity drops below **2/3 of maintenance margin**
- Liquidator vault (HLP component) takes over the position
- Trader's cross positions + cross margin ALL transferred to liquidator
- **Maintenance margin is NOT returned** to the user (buffer for vault profitability)
- On average, backstop liquidations are profitable for HLP

## gRPC Stream Approach (Dwellir)
Node-level `StreamFills` gRPC endpoint provides ALL fills globally. Each fill arrives as:
```python
[user_address, fill_data]
```
Liquidation detection:
```python
if 'liquidation' in fill_data:
    liquidated_user = fill_data['liquidation']['liquidatedUser']
    direction = fill_data['dir']  # "Close Long", "Close Short", etc.
    is_closing = 'close' in direction.lower()
    is_victim = user_address.lower() == liquidated_user.lower()
    if is_closing and is_victim:
        # This is the liquidated user's fill
```

## Key Insights
- Liquidation fills create MULTIPLE fills: one for liquidated trader, one for liquidator(s)
- Filter for `user_address == liquidatedUser` to get the victim's fill (not the liquidator's)
- `dir` field: "Liquidated Isolated Long", "Liquidated Cross Short", etc.
- Via public WS API: subscribe to `userFills` for HLP child `0xb0a5...9540` (backstop fills)
- Via gRPC node: `StreamFills` gives ALL fills for ALL users (requires node access)
- Reference repo: `thunderhead-labs/hyperliquid-stats` (cloned to `docs/external/hyperliquid-stats/`)
