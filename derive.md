# Derive (formerly Lyra) API Documentation

Source: https://derive.xyz / https://github.com/derivexyz/v1-core

## REST API
**Base URL**: `https://api.lyra.finance`

### Endpoints
- **Get Products (Instruments)**: `GET /public/get_all_instruments?instrument_type=perp&expired=false`
  Returns a list of active perpetual instruments.
- **Get Trades (History)**: `GET /public/get_trade_history`
  Returns recent trades. Parameters usually specify the instrument.

## Websocket
- The official Derive V2 WebSocket documentation does not explicitly detail a custom ping/pong application-level mechanism, implying standard native WebSocket pings are typically adequate to keep the connection alive.
