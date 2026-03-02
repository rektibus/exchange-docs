# AEVO Exchange — WebSocket + REST API Documentation

> Source: https://api-docs.aevo.xyz/reference + https://github.com/aevoxyz/aevo-sdk
> SDK: `docs/external/aevo_sdk.py` (full Python SDK)

## Endpoints

| Type | Mainnet | Testnet |
|------|---------|---------|
| REST | `https://api.aevo.xyz` | `https://api-testnet.aevo.xyz` |
| WS   | `wss://ws.aevo.xyz` | `wss://ws-testnet.aevo.xyz` |

## WebSocket Message Format

### Request
```json
{
  "op": "subscribe",    // Operation: subscribe, unsubscribe, ping
  "data": [...],        // Parameters (optional)
  "id": 1              // Request ID (optional, integer)
}
```

### Response
```json
{
  "data": {...},        // JSON payload
  "channel": "...",     // Channel name (for subscriptions)
  "id": 1,             // Matching request ID (if provided)
  "error": "..."       // Error message (if error)
}
```

## Connection Lifecycle

1. Open WS to `wss://ws.aevo.xyz`
2. (Optional) Authenticate for private operations
3. Subscribe to channels
4. Connection streams data from subscriptions
5. **Connection times out after 15 minutes of inactivity**
6. Send `ping` to keep alive (or any other operation refreshes the timer)

## PUBLISH Operations (One-Time Calls)

### PUBLISH Channels
Get available channels to subscribe to.

**Request:**
```json
{"id": 1, "op": "channels"}
```

**Response:**
```json
{
  "id": 1,
  "data": [
    "orderbook:ETH-27JAN23-1050-P",
    "orderbook:ETH-13JAN23-850-P"
  ]
}
```

### PUBLISH Ping
Sends a ping to the server. Keeps connection alive.

**Request:**
```json
{"id": 1, "op": "ping"}
```

**Response:**
```json
{
  "id": 1,
  "data": {
    "success": true,
    "timestamp": "1673436052887313432"
  }
}
```
Note: timestamp is in **nanoseconds**.

## Rate Limits

### REST
- Returns HTTP 429 when exceeded
- `X-RETRY-AFTER` header = nanoseconds to wait

### WebSocket
- **No limit on number of subscriptions**
- Rate limit applies to MESSAGES sent (subscribe, unsubscribe, operations)
- **Exception: ping messages are NOT rate-limited**
- When exceeded:
```json
{
  "status": "error",
  "timestamp": "1664338190185908000",
  "error": "RATE_LIMIT_EXCEEDED",
  "data": {
    "retry_after": "4406000000"
  }
}
```

## Public WS Channels

### SUBSCRIBE Trades
Returns matched order details.

Subscribe by instrument: `{"op":"subscribe","data":["trades:{instrument_name}"]}`
Subscribe by asset: `{"op":"subscribe","data":["trades:{asset}"]}`

**Response fields:**
| Field | Type | Description |
|-------|------|-------------|
| `channel` | string | `trades:{instrument_name}` |
| `data.trade_id` | string | Trade transaction hash |
| `data.instrument_id` | string | Instrument ID |
| `data.instrument_name` | string | e.g. `ETH-PERP` |
| `data.instrument_type` | string | `OPTION` or `PERPETUAL` |
| `data.side` | string | `buy` or `sell` |
| `data.price` | string | Price in USD |
| `data.amount` | string | Amount of contracts |
| `data.created_timestamp` | string | Nanosecond timestamp |

**Example (perp):**
```json
{
  "channel": "trades:ETH-PERP",
  "data": {
    "trade_id": "Btj9ojmpgyjLKYxTvNNF3QoLqrW1x3QN7vSqyxZoFWUo",
    "instrument_id": "1",
    "instrument_name": "ETH-PERP",
    "instrument_type": "PERPETUAL",
    "side": "sell",
    "price": "1937.31",
    "amount": "0.03",
    "created_timestamp": "1772450889335076036"
  }
}
```

**Example (option):**
```json
{
  "channel": "trades:ETH-20JAN23-1200-P",
  "data": {
    "trade_id": "0x17897e438f15c459a3a4ed44687dc7f0c4c678b2b005ea87bbae35346f279f02",
    "instrument_id": 830,
    "instrument_name": "ETH-20JAN23-1200-P",
    "instrument_type": "OPTION",
    "side": "sell",
    "price": "0.58",
    "amount": "1",
    "created_timestamp": "1674118637229190091"
  }
}
```
- `data` is a single **object** (NOT an array)
- `created_timestamp` in **nanoseconds**
- Note: official docs example has typo `created_ttimestamp` — actual field is `created_timestamp`

### SUBSCRIBE Orderbook Throttled (NEW)
Returns orderbook snapshot on initial subscription, then deltas on changes. Throttled by 100ms or 500ms.

Subscribe: `{"op":"subscribe","data":["orderbook-100ms:{instrument_name}"]}`
Also available: `orderbook-500ms:{instrument_name}`

**Response fields:**
| Field | Type | Description |
|-------|------|-------------|
| `channel` | string | `orderbook-100ms:{instrument_name}` |
| `data.type` | string | `snapshot` or `update` |
| `data.instrument_id` | string | Instrument ID number |
| `data.instrument_name` | string | Instrument symbol |
| `data.instrument_type` | string | `OPTION` or `PERPETUAL` |
| `data.bids` | array | `[[price, amount, iv]]` (IV for options only) |
| `data.asks` | array | `[[price, amount, iv]]` |
| `data.last_updated` | string | Nanosecond timestamp |
| `data.checksum` | string | CRC32 checksum |

**Snapshot example:**
```json
{
  "channel": "orderbook-100ms:ETH-PERP",
  "data": {
    "type": "snapshot",
    "instrument_id": "1",
    "instrument_name": "ETH-PERP",
    "instrument_type": "PERPETUAL",
    "bids": [["1936.75", "4.58"], ["1936.74", "0.42"]],
    "asks": [["1937.07", "3.65"], ["1937.08", "0.98"]],
    "last_updated": "1772450114876177604",
    "checksum": "1321749405"
  }
}
```

**Update (delta):**
```json
{
  "channel": "orderbook-100ms:ETH-31MAR23-1350-C",
  "data": {
    "type": "update",
    "instrument_id": "165",
    "instrument_name": "ETH-31MAR23-1350-C",
    "instrument_type": "OPTION",
    "bids": [["1", "10", "0.75"]],
    "asks": [["10", "1", "0.85"]],
    "last_updated": "1673436052887313432",
    "checksum": "1321749405"
  }
}
```
- Amount `"0"` = price level removed from orderbook
- `last_updated` in **nanoseconds**

### SUBSCRIBE Book Ticker (NEW)
Returns instrument ticker info when top-of-book changes. Real-time updates.

Subscribe by instrument: `{"op":"subscribe","data":["book-ticker:{instrument_name}"]}`
Subscribe by asset+type: `{"op":"subscribe","data":["book-ticker:{asset}:{instrument_type}"]}`

**Example response:**
```json
{
  "channel": "book-ticker:ETH-31MAR23-1350-C",
  "data": {
    "timestamp": "1673436965238291661",
    "tickers": [
      {
        "instrument_id": 165,
        "instrument_name": "ETH-31MAR23-1350-C",
        "instrument_type": "OPTION",
        "bid": {
          "price": "2",
          "amount": "10",
          "delta": "0.2159",
          "theta": "-0.0303",
          "gamma": "0.0179",
          "rho": "0.6193",
          "vega": "2.4663",
          "iv": "0.0263"
        },
        "ask": {
          "price": "10",
          "amount": "1",
          "delta": "0.3757",
          "theta": "-0.0939",
          "gamma": "0.0097",
          "rho": "1.0635",
          "vega": "2.4663",
          "iv": "0.0628"
        }
      }
    ]
  }
}
```

### Orderbook Checksum

Every orderbook message contains a 32-bit integer checksum (base-10 string). Used to verify client orderbook state vs matching engine state. If checksums differ, re-subscribe to fetch a new snapshot.

**Preimage format:** `<best_bid_price>:<best_bid_size>:<best_ask_price>:<best_ask_size>:<second_best_bid_price>:...`
- Only the best 100 price levels are included
- Concatenate each order's price and size, sorted by price level

**Example:**
```
orderbook: { "bids": [["9", "2"]], "asks": [["10", "1"]] }
preimage: "9:2:10:1"
```

**Python checksum:**
```python
import zlib

def checksum(bids, asks):
    preimage = ""
    iterations = max(len(bids), len(asks))
    for index in range(min(iterations, 100)):
        if len(bids) > index:
            price, size = bids[index]
            preimage += price + ":" + size + ":"
        if len(asks) > index:
            price, size = asks[index]
            preimage += price + ":" + size + ":"
    preimage = preimage[:-1]  # strip last colon
    crc = zlib.crc32(preimage.encode("utf8")) & 0xFFFFFFFF
    return crc

print(checksum([["9", "2"]], [["10", "1"]]))  # 1226559413
```

### SUBSCRIBE Ticker Throttled (NEW)
Returns instrument ticker info including funding rates, mark price, bid/ask. Throttled by 500ms.

Subscribe by instrument: `{"op":"subscribe","data":["ticker-500ms:{instrument_name}"]}`
Subscribe by asset+type: `{"op":"subscribe","data":["ticker-500ms:{asset}:{instrument_type}"]}`

**Response fields:**
| Field | Type | Description |
|-------|------|-------------|
| `channel` | string | `ticker-500ms:{asset}:{type}` or `ticker-500ms:{name}` |
| `data.timestamp` | string | Nanosecond timestamp |
| `data.tickers[].instrument_id` | int | Instrument ID |
| `data.tickers[].instrument_name` | string | e.g. `ETH-PERP` |
| `data.tickers[].instrument_type` | string | `OPTION` or `PERPETUAL` |
| `data.tickers[].funding_rate` | string | Funding rate of last epoch |
| `data.tickers[].next_funding_rate` | string | Estimated next epoch funding rate |
| `data.tickers[].mark` | object | Mark price + greeks |
| `data.tickers[].bid` | object | Top bid price + greeks + amount |
| `data.tickers[].ask` | object | Top ask price + greeks + amount |

**Example response (perps):**
```json
{
  "channel": "ticker-500ms:ETH:OPTION",
  "data": {
    "timestamp": "1673436965238291661",
    "tickers": [
      {
        "instrument_id": 165,
        "instrument_name": "ETH-31MAR23-1350-C",
        "instrument_type": "OPTION",
        "funding_rate": "0.000026",
        "next_funding_rate": "0.00002",
        "mark": {
          "price": "140.007862",
          "delta": "0.540531375408708",
          "theta": "-0.9224266733203602",
          "gamma": "0.0010828257944813621",
          "rho": "1.2586305929021393",
          "vega": "2.466304065911212",
          "iv": "0.5898161402416873"
        },
        "bid": {
          "price": "2",
          "amount": "10",
          "delta": "0.2159147503564693",
          "theta": "-0.03033364841496897",
          "gamma": "0.017935537671398397",
          "rho": "0.6193026765188775",
          "vega": "2.466304065911212",
          "iv": "0.026280592178461275"
        },
        "ask": {
          "price": "10",
          "amount": "1",
          "delta": "0.3756922766741976",
          "theta": "-0.09391922572782523",
          "gamma": "0.009719490995099413",
          "rho": "1.063503444637495",
          "vega": "2.466304065911212",
          "iv": "0.06281820373274899"
        }
      }
    ]
  }
}
```

**EnsoX fields from ticker-500ms (for perps):**
- `data.tickers.0.funding_rate` → funding value
- `data.tickers.0.open_interest` → OI value (if present)
- `data.tickers.0.instrument_name` → symbol
- `data.timestamp` → timestamp

### SUBSCRIBE Index
Returns the index price for an asset.

Subscribe: `{"op":"subscribe","data":["index:{asset}"]}`

**Response fields:**
| Field | Type | Description |
|-------|------|-------------|
| `channel` | string | `index:{asset}` |
| `data.price` | string | Price in USD |
| `data.timestamp` | string | Nanosecond timestamp |

**Example:**
```json
{
  "channel": "index:ETH",
  "data": {
    "price": "1337.16",
    "timestamp": "1673438070391698947"
  }
}
```

### Subscription ACK
When a subscription succeeds, AEVO returns:
```json
{"data": ["trades:ETH-PERP"]}
```
This echoes back the subscribed channel names as an array.

## Authentication (Private Operations)

### WebSocket Auth
```json
{
  "id": 1,
  "op": "auth",
  "data": {
    "key": "<API_KEY>",
    "secret": "<API_SECRET>"
  }
}
```

### API Key Registration (via `/register` endpoint)

Parameters:
- `account`: Ethereum address
- `signing_key`: randomly generated Ethereum address
- `expiry`: UNIX timestamp in nanoseconds
- `account_signature`: signed with account's private key
- `signing_key_signature`: signed with signing_key's private key

**Generate signing_key:**
```javascript
const signer = ethers.Wallet.createRandom()
```

**Generate account_signature:**
```javascript
// Hash the register data
const registerHash = ethers.utils._TypedDataEncoder.hash(
    {
      name: "Aevo Mainnet",
      version: "1",
      chainId: 1,
    },
    {
      Register: [
        { name: "key", type: "address" },
        { name: "expiry", type: "uint256" },
      ],
    },
    {
      key: await signer.getAddress(),
      expiry: ethers.constants.MaxUint256.toString(),
    }
);

// Sign the hash
const res = await promisify(provider.provider.sendAsync)({
  method: "eth_sign",
  params: [account.toLowerCase(), registerHash],
});

// This is the account_signature
const accountSignature = res.result;
```

**Generate signing_key_signature:**
```javascript
const signingKeySignature = await signer._signTypedData(
    {
      name: "Aevo Mainnet",
      version: "1",
      chainId: 1,
    },
    {
      SignKey: [{ name: "account", type: "address" }],
    },
    {
      account: your_wallet_address
    }
);
```

### Signing Orders (EIP-712)

> **Note:** The `timestamp` field is mandatory since 21 August 2023 00:00 UTC (replay attack prevention).

Orders are signed using the account's **Signing Key** (generated during Enable Trading), following [EIP-712](https://eips.ethereum.org/EIPS/eip-712).

> **Important:** The signature for order submission is DIFFERENT from the signature for authentication.

**Python example:**
```python
from random import randint
from eip712_structs import EIP712Struct, Address, Uint, Boolean, make_domain
from web3 import Web3
from eth_account import Account

# Generate Salt
salt = randint(0, 10**6)

# Limit price and amount is in 6 decimal places
decimals = 10**6
limit_price = int(100 * decimals)  # Limit price of $100
amount = int(2 * decimals)  # Size of 2 contracts

# Current timestamp in UNIX seconds
timestamp = 1690434000

# instrument_id from /options-chain
instrument = 1

class Order(EIP712Struct):
    maker = Address()
    isBuy = Boolean()
    limitPrice = Uint(256)
    amount = Uint(256)
    salt = Uint(256)
    instrument = Uint(256)
    timestamp = Uint(256)

order_struct = Order(
    maker="your_address",  # The wallet's main address
    isBuy=True,            # True if buy, False if sell
    limitPrice=limit_price,
    amount=amount,
    salt=salt,
    instrument=instrument,
    timestamp=timestamp
)

# Get bytes
domain = make_domain(name="Aevo Mainnet", version="1", chainId=1)
# Testnet: domain = make_domain(name='Aevo Testnet', version='1', chainId=11155111)
signable_bytes = Web3.keccak(order_struct.signable_bytes(domain=domain))

# Sign with key
key = "your_signing_key"
signature = Account._sign_hash(signable_bytes, key).signature.hex()
```

## REST API

### GET /assets
Returns the list of active underlying assets.

```
GET https://api.aevo.xyz/assets
```

**Response (200):** array of strings
```json
["ETH"]
```

---

### GET /expiries
Returns expiry timestamps of derivatives for the given asset.

```
GET https://api.aevo.xyz/expiries?asset={asset}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | ✅ | Name of underlying asset |

**Response (200):** array of strings (nanosecond timestamps)
```json
["1680249600000000000"]
```

---

### GET /index
Returns the current index price of the given asset.

```
GET https://api.aevo.xyz/index?asset={asset}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | ✅ | Name of underlying asset |

**Response (200):**
```json
{
  "price": "12.34",
  "timestamp": "1680249600000000000"
}
```

---

### GET /index-history
Returns historical index price for a given asset.

```
GET https://api.aevo.xyz/index-history?asset={asset}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | ✅ | Name of underlying asset |
| `resolution` | integer | | Interval in seconds. Must be multiple of 30. Default: 30 |
| `start_time` | integer | | Exclude entries before this time (ns). Default: 0 |
| `end_time` | integer | | Exclude entries after this time (ns). Default: now |
| `limit` | integer | | Max entries. Default: 10, max: 50 |

**Response (200):**
```json
{
  "history": [
    ["1680249600000000000", "1323.45"]
  ]
}
```
Format: `[timestamp_ns, price]`

---

### GET /mark-history
Returns historical mark prices for a given instrument.

```
GET https://api.aevo.xyz/mark-history?instrument_name={instrument_name}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `instrument_name` | string | ✅ | Instrument name (e.g. `ETH-PERP`) |
| `resolution` | integer | | Interval in seconds. Must be multiple of 30. Default: 30 |
| `start_time` | integer | | Exclude entries before this time (ns). Default: 0 |
| `end_time` | integer | | Exclude entries after this time (ns). Default: now |
| `limit` | integer | | Max entries. Default: 10, max: 50 |

**Response (200):**
```json
{
  "history": [
    ["1680249600000000000", "1323.45"]
  ]
}
```
Format: `[timestamp_ns, price]`

---

### GET /settlement-history
Returns historical settlement prices for a given asset.

```
GET https://api.aevo.xyz/settlement-history?asset={asset}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | | Name of underlying asset |
| `start_time` | integer | | Exclude entries before this time (ns). Default: 0 |
| `end_time` | integer | | Exclude entries after this time (ns). Default: now |
| `limit` | integer | | Max entries. Default: 10, max: 50 |

**Response (200):** array of objects
```json
[
  {
    "asset": "ETH",
    "expiry": "1680249600000000000",
    "settlement_price": "1734.23",
    "settlement_timestamp": "1680249600000000000"
  }
]
```

---

### GET /markets
Returns a list of instruments. If `asset` is not specified, returns all listed instruments.

```
GET https://api.aevo.xyz/markets?asset={asset}&instrument_type={type}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | | Name of underlying asset |
| `instrument_type` | string | | `OPTION`, `PERPETUAL`, or `SPOT` |

**Response (200):** array of objects
```json
[
  {
    "instrument_id": "12",
    "instrument_name": "ETH-30JUN23-1600-C",
    "instrument_type": "OPTION",
    "underlying_asset": "ETH",
    "quote_asset": "USDC",
    "price_step": "0.05",
    "amount_step": "0.1",
    "min_order_value": "0.1",
    "max_order_value": "0.1",
    "max_notional_value": "0.1",
    "mark_price": "12.23",
    "forward_price": "12.23",
    "index_price": "12.23",
    "is_active": true,
    "option_type": "put",
    "expiry": "1680249600000000000",
    "strike": "2500",
    "greeks": {
      "delta": "0.23",
      "gamma": "0.23",
      "rho": "0.23",
      "theta": "0.23",
      "vega": "0.23",
      "iv": "0.23"
    },
    "max_leverage": "12"
  }
]
```

**Key fields for EnsoX:**
- `instrument_name` → symbol
- `underlying_asset` → base
- `quote_asset` → quote
- `price_step` → tick_size
- `amount_step` → step_size
- `instrument_type` → `PERPETUAL` for perps, `SPOT` for spot
- `is_active` → filter active instruments only

---

### GET /statistics
Returns market statistics for the given asset.

```
GET https://api.aevo.xyz/statistics?asset={asset}&instrument_type={type}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `asset` | string | | Name of underlying asset |
| `instrument_type` | string | | `OPTION`, `PERPETUAL`, or `SPOT` |
| `end_time` | integer | | Exclude entries after this time (ns). Default: now |

**Response (200):**
```json
{
  "asset": "ETH",
  "open_interest": {
    "calls": "1234.56",
    "puts": "1234.56",
    "total": "1234.56"
  },
  "daily_volume": "1234.56",
  "daily_buy_volume": "1234.56",
  "daily_sell_volume": "1234.56",
  "daily_volume_premium": "1234.56",
  "total_volume": "1234.56",
  "total_volume_premium": "1234.56",
  "daily_volume_contracts": "1234.5",
  "index_price": "12.23",
  "index_daily_change": "12.52",
  "mark_price": "12.23",
  "mark_price_24h_ago": "12.52",
  "mark_daily_change": "12.52",
  "funding_daily_avg": "12.52",
  "put_call_ratio": "0.23"
}
```

---

### GET /orderbook
Returns the orderbook for a given instrument.

```
GET https://api.aevo.xyz/orderbook?instrument_name={instrument_name}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `instrument_name` | string | ✅ | Instrument name (e.g. `ETH-PERP`) |

**Response (200):**
```json
{
  "type": "snapshot",
  "instrument_id": "12",
  "instrument_name": "ETH-30JUN23-1600-C",
  "instrument_type": "OPTION",
  "bids": [["1", "100", "12"]],
  "asks": [["1", "100", "12"]],
  "last_updated": "1680249600000000000",
  "checksum": "8479283742"
}
```
- Bids/asks arrays: `[price, amount, iv]` (IV only for options)
- `last_updated` in nanoseconds
- `type` is always `"snapshot"` for REST

---

### GET /funding
Returns the current funding rate for an instrument.

```
GET https://api.aevo.xyz/funding?instrument_name={instrument_name}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `instrument_name` | string | ✅ | Instrument name (e.g. `ETH-PERP`) |

**Response (200):**
```json
{
  "funding_rate": "0.00122",
  "next_epoch": "1680249600000000000"
}
```

---

### GET /funding-history
Returns the funding rate history for an instrument.

```
GET https://api.aevo.xyz/funding-history?instrument_name={instrument_name}
```

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `instrument_name` | string | | Instrument name |
| `start_time` | integer | | Exclude entries before this time (ns). Default: 0 |
| `end_time` | integer | | Exclude entries after this time (ns). Default: now |
| `limit` | integer | | Max entries. Default: 10, max: 50 |

**Response (200):**
```json
{
  "funding_history": [
    ["ETH-PERP", "1680249600000000000", "0.000123", "1892.82"]
  ]
}
```
Format: `[instrument_name, timestamp_ns, funding_rate, mark_price]`

---

## Symbol Format

- Instrument names: `{ASSET}-PERP` (e.g. `ETH-PERP`, `BTC-PERP`)
- All uppercase, dash-separated
- No lowercase transformation needed (`lowercase: false`)

## AEVO MCP Server

Hosted endpoints:
- Mainnet: `https://mcp.aevo.xyz/mcp`
- Testnet: `https://mcp-testnet.aevo.xyz/mcp`

Session-based auth. Credentials stored in memory only.
```bash
claude mcp add --transport http aevo-trading https://mcp.aevo.xyz/mcp
```

## SDK Reference

Full Python SDK at `docs/external/aevo_sdk.py` (from https://github.com/aevoxyz/aevo-sdk).

Key methods:
- `subscribe_trades(instrument_name)` — `{"op":"subscribe","data":["trades:{name}"]}`
- `subscribe_orderbook(instrument_name)` — `{"op":"subscribe","data":["orderbook:{name}"]}`
- `subscribe_ticker(channel)` — generic channel subscribe
- `open_connection()` — connects with `ping_interval=None`