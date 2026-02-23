# Aevo API Documentation

## Endpoints

REST API Endpoints:
- Mainnet: https://api.aevo.xyz
- Testnet: https://api-testnet.aevo.xyz

Websocket API Endpoints:
- Mainnet: wss://ws.aevo.xyz
- Testnet: wss://ws-testnet.aevo.xyz

Requests are all JSON objects.
Responses are either a JSON object or array.

SDKs:
- Python: https://github.com/aevoxyz/aevo-sdk

## Signing Orders

EIP-712 signature using account's Signing Key (generated during Enable Trading).
Order signature ≠ authentication signature.

```python
from eip712_structs import EIP712Struct, Address, Uint, Boolean, make_domain
from web3 import Web3
from eth_account import Account

class Order(EIP712Struct):
    maker = Address()
    isBuy = Boolean()
    limitPrice = Uint(256)
    amount = Uint(256)
    salt = Uint(256)
    instrument = Uint(256)
    timestamp = Uint(256)  # mandatory since 21 Aug 2023

# Prices/amounts in 6 decimal places
order_struct = Order(maker="address", isBuy=True,
    limitPrice=int(100 * 10**6), amount=int(2 * 10**6),
    salt=randint(0, 10**6), instrument=1, timestamp=1690434000)

domain = make_domain(name="Aevo Mainnet", version="1", chainId=1)
# Testnet: make_domain(name='Aevo Testnet', version='1', chainId=11155111)
signable_bytes = Web3.keccak(order_struct.signable_bytes(domain=domain))
signature = Account._sign_hash(signable_bytes, "signing_key").signature.hex()
```

## Rate Limits

**REST**: 429 status + `X-RETRY-AFTER` header (nanoseconds). Per-account (authenticated) or per-IP.
```json
{"error": "RATE_LIMIT_EXCEEDED", "retry_after": "4406000000"}
```

**WebSocket**: No limit on subscription count. Operations (subscribe/unsubscribe) are rate-limited. Ping exempt.
```json
{"status": "error", "timestamp": "1664338190185908000",
 "error": "RATE_LIMIT_EXCEEDED", "data": {"retry_after": "4406000000"}}
```

## Orderbook Checksum

Every orderbook message contains a CRC32 checksum (32-bit integer, base-10 string). Mismatch → re-subscribe to get fresh snapshot.

- Best 100 price levels only
- Format: `<best_bid_price>:<best_bid_size>:<best_ask_price>:<best_ask_size>:...`
- Example: bids `[["9","2"]]`, asks `[["10","1"]]` → preimage `9:2:10:1` → checksum `1226559413`

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
    return zlib.crc32(preimage.encode("utf8")) & 0xFFFFFFFF
```

## REST API Endpoints

### GET /assets
Returns list of active underlying assets. Response: `["ETH", ...]`

### GET /expiries
Params: `asset` (required). Returns expiry timestamps (nanoseconds). Response: `["1680249600000000000"]`

### GET /index
Params: `asset` (required). Returns `{price, timestamp}` (nanoseconds).
```json
{"price": "12.34", "timestamp": "1680249600000000000"}
```

### GET /index-history
Params: `asset` (required), `resolution` (interval in seconds, multiple of 30, default 30), `start_time` / `end_time` (nanoseconds), `limit` (default 10, max 50).
```json
{"history": [["1680249600000000000", "1323.45"]]}
```

### GET /mark-history
Params: `instrument_name` (required), `resolution` (multiple of 30), `limit` (max 50), `start_time` / `end_time` (nanoseconds).

### GET /settlement-history
Params: `asset`, `start_time` / `end_time` (nanoseconds), `limit` (max 50).

### GET /markets ⭐ (products endpoint)
Params: `asset`, `instrument_type` (OPTION | PERPETUAL | SPOT). Returns array of instruments.

Key fields: `instrument_id`, `instrument_name` (e.g. "ETH-30JUN23-1600-C"), `instrument_type`, `underlying_asset`, `quote_asset`, `price_step`, `amount_step`, `min_order_value`, `max_order_value`, `max_notional_value`, `mark_price`, `index_price`, `is_active`, `max_leverage`.
```json
{"instrument_id": "12", "instrument_name": "ETH-30JUN23-1600-C", "instrument_type": "OPTION",
 "underlying_asset": "ETH", "quote_asset": "USDC", "is_active": true, "max_leverage": "12"}
```

### GET /statistics ⭐ (OI + funding source)
Params: `asset`, `instrument_type` (OPTION | PERPETUAL | SPOT), `end_time` (nanoseconds).

Key fields: `open_interest.total`, `daily_volume`, `daily_buy_volume`, `daily_sell_volume`, `index_price`, `mark_price`, `funding_daily_avg`.
```json
{"asset": "ETH", "open_interest": {"calls": "1234.56", "puts": "1234.56", "total": "1234.56"},
 "daily_volume": "1234.56", "mark_price": "12.23", "funding_daily_avg": "12.52"}
```

### GET /coingecko-statistics
Returns all perp stats. Key fields: `ticker_id` (e.g. "ETH-PERP"), `open_interest`, `funding_rate`, `index_price`, `next_funding_rate_timestamp`.

### GET /orderbook ⭐ (depth source)
Params: `instrument_name` (required). Returns snapshot with `bids`/`asks` arrays — each level is **3 elements**: `[price, amount, IV]`. Also: `instrument_id`, `instrument_name`, `instrument_type`, `last_updated` (nanoseconds), `checksum`, `type` (always "snapshot" for REST).
```json
{"type": "snapshot", "instrument_name": "ETH-30JUN23-1600-C",
 "bids": [["1", "100", "12"]], "asks": [["1", "100", "12"]],
 "last_updated": "1680249600000000000", "checksum": "8479283742"}
```

### GET /funding ⭐ (funding rate)
Params: `instrument_name` (required). Returns `funding_rate` (decimal) + `next_epoch` (nanoseconds).
```json
{"funding_rate": "0.00122", "next_epoch": "1680249600000000000"}
```

### GET /funding-history
Params: `instrument_name`, `start_time` / `end_time` (nanoseconds), `limit` (max 50). Returns `funding_history` array of `[instrument_name, timestamp_ns, funding_rate, mark_price]`.
```json
{"funding_history": [["ETH-PERP", "1680249600000000000", "0.000123", "1892.82"]]}
```

### GET /instrument/{instrument_name}
Returns instrument detail. Key fields: `instrument_id`, `instrument_name`, `mark_price`, `index_price`, `best_bid` / `best_ask` (objects with `price`, `amount`, `iv`), `markets.total_oi`, `markets.daily_volume`, `greeks`.
```json
{"instrument_name": "ETH-30JUN23-1600-C", "mark_price": "12.23",
 "best_bid": {"price": "12.34", "amount": "1000000", "iv": "0.23"},
 "markets": {"daily_volume": "1234.56", "total_oi": "1234.56"}}
```

### GET /instrument/{instrument_name}/trade-history ⭐ (recovery source)
Returns `count` + `trade_history` array. Fields: `trade_id`, `instrument_id`, `instrument_name`, `instrument_type`, `side` ("buy"/"sell"), `price`, `amount`, `created_timestamp` (nanoseconds).
```json
{"count": "5", "trade_history": [
  {"trade_id": "DwmD...", "instrument_name": "ETH-30JUN23-1600-C",
   "side": "buy", "price": "12.34", "amount": "1000000",
   "created_timestamp": "1680249600000000000"}]}
```

### GET /time
Returns server time. Fields: `name`, `timestamp` (nanoseconds), `time`, `sequence`, `block`.

### GET /swap (trading)
Returns swap quote. Fields: `quote_amount`, `fees`, `fee_rate`, `base_balance`, `quote_balance`, `amount`, `price`.

## WebSocket API

**Endpoints**: `wss://ws.aevo.xyz` (mainnet), `wss://ws-testnet.aevo.xyz` (testnet)

**Request format**: `{op, data, id}` — `op` = "subscribe" | "unsubscribe" | "ping", `data` = params, `id` = optional request ID.

**Response format**: `{data, channel, error, id}` — `channel` = the subscription channel name (discriminator!), `data` = payload, `error` = optional.

**Connection**: Timeout after 15min inactivity. Ping or any operation refreshes. Two operation types: PUBLISH (one-time) and SUBSCRIBE (streaming).

### PUBLISH Channels (list available)
Request: `{"op": "channels"}` → Response: `{"data": ["orderbook:ETH-27JAN23-1050-P", ...]}`

### PUBLISH Ping
Request: `{"op": "ping"}` → Response: `{"data": {"success": true, "timestamp": "1673436052887313432"}}`

### SUBSCRIBE Orderbook Throttled ⭐ (depth)
Channel: **`orderbook-100ms:{instrument_name}`** (or `orderbook-500ms:`)
Subscribe: `{"op": "subscribe", "data": ["orderbook-100ms:ETH-31MAR23-1350-C"]}`

Response — `channel` contains full channel name, `data` has the orderbook:
- `data.type`: "snapshot" | "update"
- `data.instrument_id`, `data.instrument_name`, `data.instrument_type`
- `data.bids` / `data.asks`: arrays of **3 elements** `[price, amount, IV]` — amount=0 means level removed
- `data.last_updated`: nanoseconds
- `data.checksum`: CRC32 checksum
```json
{"channel": "orderbook-100ms:ETH-31MAR23-1350-C",
 "data": {"type": "update", "instrument_id": "165",
   "instrument_name": "ETH-31MAR23-1350-C", "instrument_type": "OPTION",
   "bids": [["1", "10", "0.75"]], "asks": [["10", "1", "0.85"]],
   "last_updated": "1673436052887313432", "checksum": "1321749405"}}
```

### SUBSCRIBE Book Ticker
Channel: **`book-ticker:{instrument_name}`** or **`book-ticker:{asset}:{instrument_type}`**
Subscribe: `{"op": "subscribe", "data": ["book-ticker:ETH-31MAR23-1350-C"]}`

Response — `data.tickers` array, each with `instrument_id`, `instrument_name`, `instrument_type`, `bid` / `ask` objects (with `price`, `amount`, greeks).
```json
{"channel": "book-ticker:ETH-31MAR23-1350-C",
 "data": {"timestamp": "1673436965238291661",
   "tickers": [{"instrument_id": 165, "instrument_name": "ETH-31MAR23-1350-C",
     "bid": {"price": "2", "amount": "10", "iv": "0.026..."},
     "ask": {"price": "10", "amount": "1", "iv": "0.062..."}}]}}
```

### SUBSCRIBE Index
Channel: **`index:{asset}`** (e.g. `index:ETH`)
Subscribe: `{"op": "subscribe", "data": ["index:ETH"]}`
```json
{"channel": "index:ETH", "data": {"price": "1337.16", "timestamp": "1673438070391698947"}}
```

### SUBSCRIBE Trades ⭐ (trade source)
Channel: **`trades:{instrument_name}`** or **`trades:{asset}`** (e.g. `trades:ETH-31MAR23-1350-C` or `trades:ETH`)
Subscribe: `{"op": "subscribe", "data": ["trades:ETH-31MAR23-1350-C"]}`

Response — **single trade object** in `data` (NOT an array):
- `data.trade_id`: hash string
- `data.instrument_id`, `data.instrument_name`, `data.instrument_type`
- `data.side`: "buy" | "sell"
- `data.price`: string USD
- `data.amount`: string contracts
- `data.created_timestamp`: nanoseconds (note: Aevo docs have typo `created_ttimestamp`)
```json
{"channel": "trades:ETH-20JAN23-1200-P",
 "data": {"trade_id": "0x17897e...", "instrument_id": 830,
   "instrument_name": "ETH-20JAN23-1200-P", "instrument_type": "OPTION",
   "side": "sell", "price": "0.58", "amount": "1",
   "created_timestamp": "1674118637229190091"}}
```

### SUBSCRIBE Ticker Throttled ⭐ (funding via WS)
Channel: **`ticker-500ms:{asset}:{instrument_type}`** or **`ticker-500ms:{instrument_name}`**
Subscribe: `{"op": "subscribe", "data": ["ticker-500ms:ETH:PERPETUAL"]}`

Response — `data.tickers` array, each with:
- `instrument_id`, `instrument_name`, `instrument_type`
- **`funding_rate`**: last epoch funding rate
- **`next_funding_rate`**: estimated next epoch
- `mark`: object with `price`, greeks
- `bid` / `ask`: objects with `price`, `amount`, greeks
```json
{"channel": "ticker-500ms:ETH:OPTION",
 "data": {"timestamp": "1673436965238291661",
   "tickers": [{"instrument_id": 165, "instrument_name": "ETH-31MAR23-1350-C",
     "funding_rate": "0.000026", "next_funding_rate": "0.00002",
     "mark": {"price": "140.007862"},
     "bid": {"price": "2", "amount": "10"},
     "ask": {"price": "10", "amount": "1"}}]}}
```

