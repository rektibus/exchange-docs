# XT Futures API Documentation

Official Docs: https://doc.xt.com/docs/futures/Access%20Description/BasicInformationOfTheInterface

## Base URLs

| Service | URL |
|---------|-----|
| REST | `https://fapi.xt.com` |
| WebSocket V2 | See WebsocKetV2 section in docs |

## Futures REST Endpoints

### GET /future/market/v1/public/cg/contracts
Get all futures contract information (public, no auth).

```json
[
  {
    "id": 123,
    "symbol": "eth_usd",
    "ticker_id": "ETH-USD",
    "base_currency": "ETH",
    "target_currency": "USD",
    "index_currency": "USD",
    "index_name": "ETH-USD",
    "product_type": "PERPETUAL",
    "contractSize": 10,
    "last_price": "1817.31",
    "index_price": "1816.61",
    "bid": "1817.31",
    "ask": "1817.32",
    "high": "1828.89",
    "low": "1778.65",
    "base_volume": "13267684284",
    "target_volume": "73698647.51054371",
    "open_interest": "2419347630",
    "funding_rate": "-0.03",
    "next_funding_rate": "-0.03",
    "next_funding_rate_timestamp": 1698681600000,
    "start_timestamp": 1651328033000,
    "end_timestamp": 253402099200000,
    "underlyingType": 1
  }
]
```

| Field | Description |
|-------|-------------|
| `symbol` | Trading pair (lowercase, underscore) |
| `ticker_id` | Display name with dash separator |
| `product_type` | `PERPETUAL` for perps |
| `contractSize` | Units per contract |
| `underlyingType` | 1=Coin-M, 2=USDT-M |
| `funding_rate` | Current funding rate |
| `open_interest` | Open interest in contracts |

## Additional Futures Sections

### Quote Collection
- Contract info, market data

### MarketData
- Client IP, server time

### Order
- Create orders, batch orders, cancel

### Entrust
- Trigger orders (stop-loss, take-profit)

### User
- Account info, positions, PnL

### WebsocKetV2
- Real-time futures market data stream
- Trade, depth, ticker, kline channels

## Symbol Format
Futures use underscore: `btc_usdt`, `eth_usd`
`underlyingType` 1 = Coin-Margined (inverse), 2 = USDT-Margined (linear)
