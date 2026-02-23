# Ace Exchange API Documentation (v2)

## General
**Public REST Base**: `https://ace.io/polarisex/oapi/v2`
**Private REST Base**: `https://ace.io/polarisex/open/v2`

## Market Data (REST)
- **Ticker**: `GET /list/tradePrice` (Values: `base_volume`, `last_price`, `quote_volume`)
- **Order Book**: `GET /public/getOrderBook` (Params: `currency_name`, `base_currency_name`)
- **Market Pairs**: `GET /list/marketPair`

## Websocket
**Note**: Not publicly documented or available for general market data. The exchange predominantly uses REST v2 for its integration.
