# BitBNS API Documentation

**Documentation**: [Postman Collection](https://documenter.getpostman.com/view/2372406/Szt5hBp7)

## General
**Base URL**: `https://api.bitbns.com/api/trade/v1` (v2 for some endpoints)

## Market Data
- **Ticker/Volume**: `https://bitbns.com/order/getTickerWithVolume`
- **Exchange Data**: Various routes under `exchangeData`

## Websocket API
**Endpoints** (Socket.IO):
- Ticker/Orderbook: `https://ws{marketname}mv2.bitbns.com/` (e.g., `wsusdtmv2.bitbns.com`)
- Private Orders: `https://wsorderv2.bitbns.com/`

Note: Config seems to heavily rely on market-specific subdomains for websockets.
