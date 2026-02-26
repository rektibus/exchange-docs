# Drift Protocol Data API Documentation

Source: https://drift-labs.github.io/v2-teacher/

## Data API Overview
The Drift Data API provides public access to various APIs that Drift uses, offering information about markets, contracts, and tokenomics.
- mainnet-beta: `https://data.api.drift.trade`
- devnet: `https://data-master.api.drift.trade/playground`

### Rate Limiting & Caching
REST API is rate limited. Responses may be cached for a short period (typically seconds to minutes).

## REST API Endpoints

### GET /contracts
Returns the contract information for each market. Contract information contains funding rate and open interest (oi).
Example: `https://data.api.drift.trade/contracts`

### GET /fundingRates
Returns historical funding rates. Can be filtered by `marketIndex`.
Example: `https://data.api.drift.trade/fundingRates?marketIndex=0`

### GET /rateHistory
Returns the borrow/deposit rate history.

### GET /candles
Returns OHLCV candle data for a market.
Parameters: `marketName` (e.g. 'SOL-PERP'), `resolution` (in minutes, e.g. 1, 5, 15, 60), `startTs`, `endTs`

## DLOB Server (Orderbook)
Drift runs a dlob-server to reduce RPC load.
- mainnet-beta: `https://dlob.drift.trade/`
- devnet: `https://master.dlob.drift.trade/`

### GET /l2
Returns the current L2 orderbook for a given market.
Parameters:
- `marketIndex` (number)
- `marketType` ('perp' or 'spot')
Example: `https://dlob.drift.trade/l2?marketIndex=0&marketType=perp`

### GET /l3
Returns the L3 orderbook with individual orders.

### WebSocket Subscriptions
DLOB provides WebSockets for real-time orderbook and trades.
Endpoint: `wss://dlob.drift.trade/ws`

Subscribe to trades:
```json
{"type": "subscribe", "channel": "trades", "marketType": "perp", "marketIndex": 0}
```

## Historical Data (S3 - Deprecated)
Historical trade records were stored in S3 CSV files but stopped updating in January 2025.
Use Data API `candles` or DLOB WebSocket `trades` channel for recent trade activity.

URL Prefix: `https://drift-historical-data-v2.s3.eu-west-1.amazonaws.com/program/dRiftyHA39MWEi3m9aunc5MzRF1JYuBsbn6VPcn33UH`
Path: `/market/${marketSymbol}/tradeRecords/${year}/${year}${month}${day}`
