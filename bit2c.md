# Bit2C API Documentation

Bit2C offers a REST API with public and private endpoints. There are **no native WebSocket endpoints** available for Bit2C.

## Public Endpoints

Base URL: `https://bit2c.co.il`

### Get Ticker
*   **Endpoint:** `/Exchanges/[Pair]/Ticker.json`
*   **Example URL:** `https://bit2c.co.il/Exchanges/BtcNis/Ticker.json`
*   **Method:** GET
*   **Response:**
    ```json
    {
      "h": 320000.0, // High
      "l": 300000.0, // Low
      "ll": 310000.0, // Last price
      "v": 15.5, // Volume
      "a": 315000.0 // Average price
    }
    ```

### Get Order Book (Depth)
*   **Endpoint:** `/Exchanges/[Pair]/orderbook.json`
*   **Example URL:** `https://bit2c.co.il/Exchanges/BtcNis/orderbook.json`
*   **Method:** GET
*   **Response:**
    ```json
    {
      "bids": [
        [310000.0, 0.5], // [Price, Amount]
        [309000.0, 1.2]
      ],
      "asks": [
        [311000.0, 0.8],
        [312000.0, 2.0]
      ]
    }
    ```

### Get Recent Trades
*   **Endpoint:** `/Exchanges/[Pair]/trades.json`
*   **Example URL:** `https://bit2c.co.il/Exchanges/BtcNis/trades.json`
*   **Parameters:** `since` (optional, trade ID)
*   **Method:** GET
*   **Response:**
    ```json
    [
      {
        "date": 1678886400, // Unix timestamp (seconds)
        "price": 310000.0,
        "amount": 0.5,
        "tid": 123456, // Trade ID
        "isBid": true // true if Maker was a buyer, false otherwise
      }
    ]
    ```

## Private Endpoints (Authenticated)

Authentication uses basic API Key/Secret mechanisms. Private endpoints are located under `/Order/*` or `/Account/*`.

### Add Order
*   **Endpoint:** `/Order/AddOrder`
*   **Method:** POST
*   **Parameters:** `Amount`, `Price`, `IsBid` (bool), `Pair`

### Cancel Order
*   **Endpoint:** `/Order/CancelOrder`
*   **Method:** POST
*   **Parameters:** `id`

### Get Account Balance
*   **Endpoint:** `/Account/Balance`
*   **Method:** GET

*Note: For the purpose of EnsoX, we typically rely on `Ticker.json`, `orderbook.json`, and `trades.json` for live/historical ingestion.*
