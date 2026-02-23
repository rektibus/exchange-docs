# BTCBox API Documentation

## General
**Base REST URL**: `https://www.btcbox.co.jp/api/v1`

## Market Data (REST)
- **Ticker**: `GET /ticker` (Params: `coin`. Returns high, low, buy, sell, last, vol)
- **Order Book**: `GET /depth` (Params: `coin`. Returns asks, bids)
- **Trades**: `GET /orders` (Params: `coin`. Returns latest 100 execution records)

## Websocket
**Note**: Not available. BTCBox only provides HTTP-based API endpoints.
