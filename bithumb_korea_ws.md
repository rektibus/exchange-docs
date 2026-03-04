# Bithumb Korea WebSocket API

Source: https://apidocs.bithumb.com/reference/websocket (user-provided 2026-03-04)

## Connection
- Public: `wss://ws-api.bithumb.com/websocket/v1`
- Private: `wss://ws-api.bithumb.com/websocket/v1/private`
- Rate limit: 10 connections/s per IP
- Idle timeout: ~120s without data
- PING: send text "PING", get `{"status":"UP"}` every 10s

## Subscribe Format
Same array format as Upbit: `[{ticket field}, {type field}, ..., {format field}]`

### Ticket Field
| Field  | Type   | Required |
|--------|--------|----------|
| ticket | String | Yes (UUID recommended) |

### Type Field
| Field           | Type    | Required | Default |
|-----------------|---------|----------|---------|
| type            | String  | Yes      | - |
| codes           | List    | Yes (UPPERCASE) | - |
| isOnlySnapshot  | Boolean | No       | false |
| isOnlyRealtime  | Boolean | No       | false |

Types: `ticker` (current price), `trade` (execution), `orderbook` (orderbook)

### Format Field
| Field  | Type   | Required | Default |
|--------|--------|----------|---------|
| format | String | No       | DEFAULT |

Values: `DEFAULT` (full names), `SIMPLE` (abbreviated)

## Trade Response (`type: "trade"`)

| Field           | Abbrev | Description                    | Type   |
|-----------------|--------|--------------------------------|--------|
| type            | ty     | "trade"                        | String |
| code            | cd     | Market code (KRW-BTC)          | String |
| trade_price     | tp     | Execution price                | Double |
| trade_volume    | tv     | Execution volume               | Double |
| ask_bid         | ab     | ASK=sell, BID=buy              | String |
| prev_closing_price | pcp | Previous day closing price     | Double |
| change          | c      | RISE/EVEN/FALL                 | String |
| change_price    | cp     | Unsigned change                | Double |
| trade_date      | tdt    | Date (KST) yyyy-MM-dd         | String |
| trade_time      | ttm    | Time (KST) HH:mm:ss           | String |
| trade_timestamp | ttms   | Timestamp (ms)                 | Long   |
| timestamp       | tms    | Server timestamp (ms)          | Long   |
| sequential_id   | sid    | Unique trade ID                | Long   |
| stream_type     | st     | SNAPSHOT or REALTIME           | String |

Example:
```json
{
    "type": "trade",
    "code": "KRW-BTC",
    "trade_price": 489700,
    "trade_volume": 1.4825,
    "ask_bid": "BID",
    "prev_closing_price": 484500,
    "change": "RISE",
    "change_price": 5200,
    "trade_date": "2024-09-10",
    "trade_time": "09:58:54",
    "trade_timestamp": 1725929934373,
    "sequential_id": 17259299343730000,
    "timestamp": 1725929934483,
    "stream_type": "REALTIME"
}
```

## Orderbook Response (`type: "orderbook"`)

| Field              | Abbrev | Description              | Type |
|--------------------|--------|--------------------------|------|
| type               | ty     | "orderbook"              | String |
| code               | cd     | Market code              | String |
| total_ask_size     | tas    | Total ask quantity        | Double |
| total_bid_size     | tbs    | Total bid quantity        | Double |
| orderbook_units    | obu    | Combined levels list      | List[Object] |
| obu[].ask_price    | ap     | Ask price                | Double |
| obu[].bid_price    | bp     | Bid price                | Double |
| obu[].ask_size     | as     | Ask size                 | Double |
| obu[].bid_size     | bs     | Bid size                 | Double |
| timestamp          | tms    | Timestamp (ms)           | Long |
| level              | lv     | Price grouping unit      | Double |
| stream_type        | st     | SNAPSHOT or REALTIME     | String |

15 levels by default, 30 for single market.

Example:
```json
{
    "type": "orderbook",
    "code": "KRW-BTC",
    "total_ask_size": 450.3526,
    "total_bid_size": 63.3006,
    "orderbook_units": [
        {"ask_price": 478800, "bid_price": 478300, "ask_size": 4.3478, "bid_size": 5.6370},
        {"ask_price": 489700, "bid_price": 477900, "ask_size": 2.3642, "bid_size": 0.9705}
    ],
    "level": 1,
    "timestamp": 1725930007672,
    "stream_type": "REALTIME"
}
```

## Notes
- Format is identical to Upbit API (same subscribe array, same field names, same orderbook_units)
- Both use [ticket, type, format] subscribe pattern
- Both use binary frames for data delivery
- Both use `ask_bid` with ASK/BID values
- Market codes: KRW-BTC format (quote-base)
