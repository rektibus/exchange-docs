# Currencies

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /currencies:
    get:
      summary: Currencies
      deprecated: false
      description: Get a list of all available currencies.
      operationId: currencies
      tags:
        - One Trading Public REST API/Public
        - public
      parameters: []
      responses:
        '200':
          description: >-
            The request was successful, and the server has returned the
            requested resource in the response body.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Currency'
              example:
                - code: BTC
                  precision: 8
                  unified_cryptoasset_id: 1
                  name: Bitcoin
                  collateral_percentage: 0
                - code: ETH
                  precision: 8
                  unified_cryptoasset_id: 1027
                  name: Ethereum
                  collateral_percentage: 0
                - code: EUR
                  precision: 2
                  unified_cryptoasset_id: 0
                  name: Euro
                  collateral_percentage: 100
          headers: {}
          x-apidog-name: OK
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612081-run
components:
  schemas:
    Currency:
      type: object
      properties:
        code:
          type: string
        precision:
          type: integer
        unified_cryptoasset_id:
          type: integer
        name:
          type: string
        collateral_percentage:
          type: integer
          x-apidog-mock: '50'
          minimum: 0
          maximum: 100
          description: >-
            The percentage of the asset's value that can be used as collateral
            for futures positions.
      required:
        - code
        - precision
        - unified_cryptoasset_id
        - name
        - collateral_percentage
      description: Currency
      x-apidog-orders:
        - code
        - precision
        - unified_cryptoasset_id
        - name
        - collateral_percentage
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Instruments

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /instruments:
    get:
      summary: Instruments
      deprecated: false
      description: >-
        Retrieves a list of available instrument pairs on the exchange,
        including details about the base and quote assets, precision levels,
        minimum and maximum trading limits, and the current market type. The
        response provides key information needed for trading, such as instrument
        unique IDs, pricing, and state (ACTIVE or otherwise). Optionally, the
        results can be filtered by market type using the type query parameter.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters:
        - name: type
          in: query
          description: >-
            Filters the instrument pairs by market type; valid values are SPOT
            for spot markets and PERP for perpetual futures.
          required: false
          schema:
            type: string
            enum:
              - SPOT
              - PERP
            x-apidog-enum:
              - value: SPOT
                name: ''
                description: ''
              - value: PERP
                name: ''
                description: ''
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Instrument'
              example:
                - base:
                    code: BTC
                    precision: 5
                  quote:
                    code: USDT
                    precision: 2
                  amount_precision: 5
                  market_precision: 2
                  min_size: '10.0'
                  min_price: '1000'
                  max_price: '10000000'
                  id: BTC_USDT
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: BTC
                    precision: 5
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 5
                  market_precision: 2
                  min_size: '10.0'
                  min_price: '1000'
                  max_price: '10000000'
                  id: BTC_EUR
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: ETH
                    precision: 4
                  quote:
                    code: USDT
                    precision: 2
                  amount_precision: 4
                  market_precision: 2
                  min_size: '10.0'
                  min_price: '100'
                  max_price: '10000000'
                  id: ETH_USDT
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: ETH
                    precision: 4
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 4
                  market_precision: 2
                  min_size: '10.0'
                  min_price: '10'
                  max_price: '10000000'
                  id: ETH_EUR
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: ETH
                    precision: 3
                  quote:
                    code: BTC
                    precision: 5
                  amount_precision: 3
                  market_precision: 5
                  min_size: '0.00022'
                  min_price: '0.0001'
                  max_price: '10000'
                  id: ETH_BTC
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: USDT
                    precision: 5
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 2
                  market_precision: 5
                  min_size: '1.0'
                  min_price: '0.1'
                  max_price: '10'
                  id: USDT_EUR
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: XRP
                    precision: 4
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 3
                  market_precision: 4
                  min_size: '10.0'
                  min_price: '0.0001'
                  max_price: '1000'
                  id: XRP_EUR
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: XRP
                    precision: 4
                  quote:
                    code: USDT
                    precision: 2
                  amount_precision: 3
                  market_precision: 4
                  min_size: '10.0'
                  min_price: '0.0001'
                  max_price: '1000'
                  id: XRP_USDT
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: SOL
                    precision: 4
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 4
                  market_precision: 3
                  min_size: '10.0'
                  min_price: '0.01'
                  max_price: '1000000'
                  id: SOL_EUR
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: SOL
                    precision: 4
                  quote:
                    code: USDT
                    precision: 2
                  amount_precision: 4
                  market_precision: 3
                  min_size: '10.0'
                  min_price: '0.01'
                  max_price: '1000000'
                  id: SOL_USDT
                  type: SPOT
                  state: ACTIVE
                - base:
                    code: BTC
                    precision: 5
                  quote:
                    code: EUR
                    precision: 2
                  amount_precision: 5
                  market_precision: 2
                  min_size: '10.0'
                  min_price: '1000'
                  max_price: '10000000'
                  id: BTC_EUR_P
                  type: PERP
                  state: ACTIVE
          headers: {}
          x-apidog-name: Success
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612082-run
components:
  schemas:
    Instrument:
      type: object
      properties:
        base:
          type: object
          properties:
            code:
              type: string
              description: The symbol for the base asset (e.g., `BTC`).
            precision:
              type: integer
              description: The number of decimal places allowed for the base asset.
          x-apidog-orders:
            - code
            - precision
          required:
            - code
            - precision
          description: An object representing the base asset in the trading pair.
          x-apidog-ignore-properties: []
        quote:
          type: object
          properties:
            code:
              type: string
              description: The symbol for the quote asset (e.g., `EUR`).
            precision:
              type: integer
              description: The number of decimal places allowed for the quote asset.
          x-apidog-orders:
            - code
            - precision
          required:
            - code
            - precision
          description: An object representing the quote asset in the trading pair.
          x-apidog-ignore-properties: []
        amount_precision:
          type: integer
          description: >-
            The number of decimal places allowed when specifying the trade
            amount (quantity of the base asset).
        market_precision:
          type: integer
          description: >-
            The number of decimal places allowed when specifying the price of
            the instrument.
        min_size:
          type: string
          description: >-
            The minimum allowable order value for the instrument, expressed in
            the quote asset (e.g., 10 EUR or 10 USDT). This is calculated as
            price × amount and ensures the order meets the required notional
            value.
        min_price:
          type: string
          description: >-
            The minimum allowable price for the instrument, expressed in the
            quote asset.
        max_price:
          type: string
          description: >-
            The maximum allowable price for the instrument, expressed in the
            quote asset.
        id:
          type: string
          description: >-
            he unique identifier for the trading pair (e.g., `BTC_USDT`). This
            is used when creating / cancelling orders as `instrument_code`.
        type:
          type: string
          enum:
            - SPOT
            - PERP
          x-apidog-enum:
            - value: SPOT
              name: ''
              description: ''
            - value: PERP
              name: ''
              description: ''
          description: >-
            The type of market for the instrument (e.g., `SPOT` for spot markets
            or `PERP` for perpetual futures).
        state:
          type: string
          enum:
            - ACTIVE
            - SUSPENDED
            - POST_ONLY
            - CLOSED
          x-apidog-enum:
            - value: ACTIVE
              name: ''
              description: ''
            - value: SUSPENDED
              name: ''
              description: ''
            - value: POST_ONLY
              name: ''
              description: ''
            - value: CLOSED
              name: ''
              description: ''
          description: >-
            The current state of the instrument, indicating whether it is ACTIVE
            (tradable) or not.
      x-apidog-orders:
        - base
        - quote
        - amount_precision
        - market_precision
        - min_size
        - min_price
        - max_price
        - id
        - type
        - state
      required:
        - base
        - quote
        - amount_precision
        - market_precision
        - min_size
        - min_price
        - max_price
        - id
        - type
        - state
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Candlesticks

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /candlesticks/{instrument_code}:
    get:
      summary: Candlesticks
      deprecated: false
      description: >-
        Get instrument candlesticks for a specified time period. The requested
        time period may include up to 5000 candlesticks; for example, a request
        for minutely candles is limited to at most approximately 83 hours.
        Please note that fewer candlesticks than the theoretical limit may be
        provided for a given time period due to gaps in trading activity.
        Additionally, the endpoint now accepts a parameter called 'countBack,'
        which specifies the exact number of bars to load. If not provided, the
        default value is set to 5000. It's important to note that 'countBack'
        takes precedence over 'from' when both parameters are present.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters:
        - name: instrument_code
          in: path
          description: Defines market by using unique instrument
          required: true
          example: BTC_EUR
          schema:
            type: string
        - name: unit
          in: query
          description: Defines the unit of candlestick time granularity
          required: true
          example: MINUTES
          schema:
            type: string
            enum:
              - MINUTES
              - HOURS
              - DAYS
              - WEEKS
              - MONTHS
            x-apidog-enum:
              - value: MINUTES
                name: ''
                description: ''
              - value: HOURS
                name: ''
                description: ''
              - value: DAYS
                name: ''
                description: ''
              - value: WEEKS
                name: ''
                description: ''
              - value: MONTHS
                name: ''
                description: ''
        - name: period
          in: query
          description: >-
            Defines the period of candlestick time granularity.


            Combined with the unit, supported resolutions are 1, 5, 15, 30
            MINUTES & 1, 4 HOURS & 1 DAYS & 1 WEEKS & 1 MONTHS.
          required: true
          example: '30'
          schema:
            type: string
        - name: from
          in: query
          description: Defines start of a query search
          required: true
          example: '2024-11-11T16:42:33.450Z'
          schema:
            type: string
        - name: to
          in: query
          description: Defines end of a query search
          required: true
          example: '2024-11-12T16:42:33.450Z'
          schema:
            type: string
        - name: countBack
          in: query
          description: Defines the exact number of candlesticks to load
          required: false
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  candlesticks:
                    type: array
                    items:
                      $ref: '#/components/schemas/Candlestick'
                x-apidog-orders:
                  - status
                  - candlesticks
                required:
                  - status
                  - candlesticks
                x-apidog-ignore-properties: []
              example:
                status: data
                candlesticks:
                  - last_sequence: 1730900885466242800
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '100000'
                    low: '100000'
                    open: '100000'
                    close: '100000'
                    volume: '2000.00'
                    time: '2024-11-06T13:59:59.999Z'
                    start_time: '2024-11-06T13:30:00.000Z'
                  - last_sequence: 1730369352914576100
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '100000'
                    low: '100000'
                    open: '100000'
                    close: '100000'
                    volume: '100.00'
                    time: '2024-10-31T10:29:59.999Z'
                    start_time: '2024-10-31T10:00:00.000Z'
                  - last_sequence: 1730368016064669000
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '10000'
                    low: '10000'
                    open: '10000'
                    close: '10000'
                    volume: '20.00'
                    time: '2024-10-31T09:59:59.999Z'
                    start_time: '2024-10-31T09:30:00.000Z'
                  - last_sequence: 1730362835479252000
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '100000'
                    low: '100000'
                    open: '100000'
                    close: '100000'
                    volume: '100.00'
                    time: '2024-10-31T08:29:59.999Z'
                    start_time: '2024-10-31T08:00:00.000Z'
                  - last_sequence: 1730330727170770700
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '100000'
                    low: '100000'
                    open: '100000'
                    close: '100000'
                    volume: '200.00'
                    time: '2024-10-30T23:29:59.999Z'
                    start_time: '2024-10-30T23:00:00.000Z'
                  - last_sequence: 1730328614342880500
                    instrument_code: BTC_EUR
                    granularity:
                      unit: MINUTES
                      period: 30
                    high: '100000'
                    low: '100000'
                    open: '100000'
                    close: '100000'
                    volume: '100.00'
                    time: '2024-10-30T22:59:59.999Z'
                    start_time: '2024-10-30T22:30:00.000Z'
          headers: {}
          x-apidog-name: Success
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612083-run
components:
  schemas:
    Candlestick:
      type: object
      properties:
        last_sequence:
          type: integer
        instrument_code:
          type: string
        granularity:
          type: object
          properties:
            unit:
              type: string
            period:
              type: integer
          x-apidog-orders:
            - unit
            - period
          required:
            - unit
            - period
          x-apidog-ignore-properties: []
        high:
          type: string
        low:
          type: string
        open:
          type: string
        close:
          type: string
        volume:
          type: string
        time:
          type: string
          format: date-time
        start_time:
          type: string
      x-apidog-orders:
        - last_sequence
        - instrument_code
        - granularity
        - high
        - low
        - open
        - close
        - volume
        - time
        - start_time
      required:
        - last_sequence
        - instrument_code
        - granularity
        - high
        - low
        - open
        - close
        - volume
        - time
        - start_time
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Fee Groups

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fees:
    get:
      summary: Fee Groups
      deprecated: false
      description: >-
        Returns details of all fee groups. Fee groups are separated into product
        types.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/FeeGroup'
              example:
                - fee_group_id: SPOT
                  display_text: The fee plan for spot trading.
                  volume_currency: EUR
                  fee_tiers:
                    - volume: 0
                      fee_group_id: SPOT
                      maker_fee: '0.1000'
                      taker_fee: '0.2000'
                    - volume: 10000
                      fee_group_id: SPOT
                      maker_fee: '0.0400'
                      taker_fee: '0.0600'
                    - volume: 100000
                      fee_group_id: SPOT
                      maker_fee: '0.0200'
                      taker_fee: '0.0500'
                    - volume: 1000000
                      fee_group_id: SPOT
                      maker_fee: '0.0190'
                      taker_fee: '0.0450'
                    - volume: 5000000
                      fee_group_id: SPOT
                      maker_fee: '0.0180'
                      taker_fee: '0.0400'
                    - volume: 25000000
                      fee_group_id: SPOT
                      maker_fee: '0.0130'
                      taker_fee: '0.0350'
                    - volume: 100000000
                      fee_group_id: SPOT
                      maker_fee: '0.0025'
                      taker_fee: '0.0300'
                    - volume: 500000000
                      fee_group_id: SPOT
                      maker_fee: '0.0000'
                      taker_fee: '0.0300'
                    - volume: 1000000000
                      fee_group_id: SPOT
                      maker_fee: '0.0000'
                      taker_fee: '0.0280'
                    - volume: 10000000000
                      fee_group_id: SPOT
                      maker_fee: '0.0000'
                      taker_fee: '0.0250'
                - fee_group_id: FUTURES
                  display_text: The fee plan for futures trading.
                  volume_currency: EUR
                  fee_tiers:
                    - volume: 0
                      fee_group_id: FUTURES
                      maker_fee: '0.1000'
                      taker_fee: '0.2000'
                    - volume: 10000
                      fee_group_id: FUTURES
                      maker_fee: '0.0400'
                      taker_fee: '0.0600'
                    - volume: 100000
                      fee_group_id: FUTURES
                      maker_fee: '0.0200'
                      taker_fee: '0.0500'
                    - volume: 1000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0190'
                      taker_fee: '0.0450'
                    - volume: 5000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0180'
                      taker_fee: '0.0400'
                    - volume: 25000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0130'
                      taker_fee: '0.0350'
                    - volume: 100000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0025'
                      taker_fee: '0.0300'
                    - volume: 500000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0000'
                      taker_fee: '0.0300'
                    - volume: 1000000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0000'
                      taker_fee: '0.0280'
                    - volume: 10000000000
                      fee_group_id: FUTURES
                      maker_fee: '0.0000'
                      taker_fee: '0.0250'
          headers: {}
          x-apidog-name: Success
        '404':
          description: ''
          content:
            application/json:
              schema:
                title: ''
                type: object
                properties:
                  error:
                    type: string
                x-apidog-orders:
                  - error
                required:
                  - error
                x-apidog-ignore-properties: []
              example:
                error: Not found.
          headers: {}
          x-apidog-name: Record Not Found
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612084-run
components:
  schemas:
    FeeGroup:
      type: object
      properties:
        fee_group_id:
          type: string
          description: Unique identifier of a FeeGroup
          enum:
            - SPOT
            - FUTURES
          x-apidog-enum:
            - value: SPOT
              name: ''
              description: ''
            - value: FUTURES
              name: ''
              description: ''
        display_text:
          type: string
          description: Textual description of a Fee Group
        volume_currency:
          type: string
          description: The code of the currency volume is denoted in.
        fee_tiers:
          type: array
          items:
            $ref: '#/components/schemas/FeeTier'
      x-apidog-orders:
        - fee_group_id
        - display_text
        - volume_currency
        - fee_tiers
      required:
        - fee_group_id
        - display_text
        - volume_currency
        - fee_tiers
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    FeeTier:
      type: object
      properties:
        volume:
          type: integer
          description: Volume beyond which this fee tier is activated
        fee_group_id:
          type: string
          description: Identifier of the fee group
        maker_fee:
          type: string
          description: >-
            Percentage fee rate that will be used for fee calculation when trade
            is settled as MAKER.
        taker_fee:
          type: string
          description: >-
            Percentage fee rate that will be used for fee calculation when trade
            is settled as TAKER.
      x-apidog-orders:
        - volume
        - fee_group_id
        - maker_fee
        - taker_fee
      required:
        - volume
        - fee_group_id
        - maker_fee
        - taker_fee
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Order Book

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /order-book/{instrument_code}:
    get:
      summary: Order Book
      deprecated: false
      description: Get the specified instrument's order book.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters:
        - name: instrument_code
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: level
          in: query
          description: |-
            Level 1 = best bid and ask
            Level 2 = Compiled order book up to market precision
            Level 3 = Full order book
          required: false
          example: '1'
          schema:
            type: string
            enum:
              - '1'
              - '2'
              - '3'
            x-apidog-enum:
              - value: '1'
                name: ''
                description: Best bid and ask
              - value: '2'
                name: ''
                description: Compiled order book up to market precision
              - value: '3'
                name: ''
                description: Full order book
            deprecated: true
            default: '3'
          deprecated: true
        - name: depth
          in: query
          description: >-
            The amount of bids and asks to return. Depth of 1 will return top of
            book.
          required: false
          example: '16'
          schema:
            type: string
            enum:
              - '1'
              - '2'
              - '4'
              - '8'
              - '16'
            x-apidog-enum:
              - value: '1'
                name: ''
                description: ''
              - value: '2'
                name: ''
                description: ''
              - value: '4'
                name: ''
                description: ''
              - value: '8'
                name: ''
                description: ''
              - value: '16'
                name: ''
                description: ''
            default: '16'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  asks:
                    type: array
                    items:
                      type: object
                      properties:
                        price:
                          type: string
                        amount:
                          type: string
                      x-apidog-orders:
                        - price
                        - amount
                      required:
                        - price
                        - amount
                  bids:
                    type: array
                    items:
                      type: object
                      properties:
                        price:
                          type: string
                        amount:
                          type: string
                      x-apidog-orders:
                        - price
                        - amount
                      required:
                        - price
                        - amount
                x-apidog-orders:
                  - asks
                  - bids
                required:
                  - asks
                  - bids
              example:
                asks:
                  - price: '100000'
                    amount: '6'
                bids:
                  - price: '10000'
                    amount: '6'
          headers: {}
          x-apidog-name: Success
        '400':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                x-apidog-orders:
                  - error
                required:
                  - error
              example:
                error: MISSING_INSTRUMENT_CODE
          headers: {}
          x-apidog-name: Bad Request
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612085-run
components:
  schemas: {}
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```

# Market Ticker

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /market-ticker:
    get:
      summary: Market Ticker
      deprecated: false
      description: >-
        The market ticker provides information about the current state of a
        market and summary statistics on activity within the last 24 hours.
        Volume, low, high and price change are calculated based on a sliding
        window of trades starting 24 hours and using minutely granularity.
        Market ticks are every minute when the 24 hour sliding window is moved
        forward and additionally on each trade.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  properties:
                    base_volume:
                      type: string
                    high:
                      type: string
                    highest_bid:
                      type: string
                    instrument_code:
                      type: string
                    last_price:
                      type: string
                    low:
                      type: string
                    lowest_ask:
                      type: string
                    price_change_percentage:
                      type: string
                    price_change:
                      type: string
                    quote_volume:
                      type: string
                    sequence:
                      type: integer
                    state:
                      type: string
                  required:
                    - base_volume
                    - high
                    - highest_bid
                    - instrument_code
                    - last_price
                    - low
                    - lowest_ask
                    - price_change_percentage
                    - price_change
                    - quote_volume
                    - sequence
                    - state
                  x-apidog-orders:
                    - base_volume
                    - high
                    - highest_bid
                    - instrument_code
                    - last_price
                    - low
                    - lowest_ask
                    - price_change_percentage
                    - price_change
                    - quote_volume
                    - sequence
                    - state
                  $ref: '#/components/schemas/MarketTicker'
              example:
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: BTC_USDT
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '100000.00'
                  highest_bid: '10000.00'
                  instrument_code: BTC_EUR
                  last_price: '100000.00'
                  low: '100000.00'
                  lowest_ask: '100000.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1730900885466242800
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: ETH_USDT
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.90'
                  high: '2000.00'
                  highest_bid: '2000.00'
                  instrument_code: ETH_EUR
                  last_price: '2000.00'
                  low: '2000.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '1800.00'
                  sequence: 1731326923439826000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: ETH_BTC
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: USDT_EUR
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: XRP_EUR
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: XRP_USDT
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '18.000'
                  high: '150.000'
                  highest_bid: '145.000'
                  instrument_code: SOL_EUR
                  last_price: '145.000'
                  low: '145.000'
                  lowest_ask: '0.000'
                  price_change_percentage: '-3.333'
                  price_change: '-5.000'
                  quote_volume: '2680.000'
                  sequence: 1731343689919892200
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '0.00'
                  highest_bid: '0.00'
                  instrument_code: SOL_USDT
                  last_price: '0.00'
                  low: '0.00'
                  lowest_ask: '0.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1731364403588000000
                  state: ACTIVE
                - base_volume: '0.00'
                  high: '64000.00'
                  highest_bid: '64000.00'
                  instrument_code: BTC_EUR_P
                  last_price: '64000.00'
                  low: '64000.00'
                  lowest_ask: '75000.00'
                  price_change_percentage: '0.00'
                  price_change: '0.00'
                  quote_volume: '0.00'
                  sequence: 1730900982376491800
                  state: ACTIVE
          headers: {}
          x-apidog-name: OK
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612086-run
components:
  schemas:
    MarketTicker:
      type: object
      properties:
        base_volume:
          type: string
        high:
          type: string
        highest_bid:
          type: string
        instrument_code:
          type: string
        last_price:
          type: string
        low:
          type: string
        lowest_ask:
          type: string
        price_change_percentage:
          type: string
        price_change:
          type: string
        quote_volume:
          type: string
        sequence:
          type: integer
        state:
          type: string
      required:
        - base_volume
        - high
        - highest_bid
        - instrument_code
        - last_price
        - low
        - lowest_ask
        - price_change_percentage
        - price_change
        - quote_volume
        - sequence
        - state
      x-apidog-orders:
        - base_volume
        - high
        - highest_bid
        - instrument_code
        - last_price
        - low
        - lowest_ask
        - price_change_percentage
        - price_change
        - quote_volume
        - sequence
        - state
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Market Ticker For Instrument

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /market-ticker/{instrument_code}:
    get:
      summary: Market Ticker For Instrument
      deprecated: false
      description: Get market statistics on a single market.
      tags:
        - One Trading Public REST API/Public
        - public
      parameters:
        - name: instrument_code
          in: path
          description: The market to get the market ticker data for
          required: true
          example: BTC_EUR
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MarketTicker'
              example:
                base_volume: '0.00'
                high: '100000.00'
                highest_bid: '10000.00'
                instrument_code: BTC_EUR
                last_price: '100000.00'
                low: '100000.00'
                lowest_ask: '100000.00'
                price_change_percentage: '0.00'
                price_change: '0.00'
                quote_volume: '0.00'
                sequence: 1730900885466242800
                state: ACTIVE
          headers: {}
          x-apidog-name: Success
        '404':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                x-apidog-orders:
                  - error
                required:
                  - error
                x-apidog-ignore-properties: []
              example:
                error: The requested market INVALID_MARKET is not available.
          headers: {}
          x-apidog-name: Record Not Found
      security: []
      x-apidog-folder: One Trading Public REST API/Public
      x-apidog-status: released
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3612087-run
components:
  schemas:
    MarketTicker:
      type: object
      properties:
        base_volume:
          type: string
        high:
          type: string
        highest_bid:
          type: string
        instrument_code:
          type: string
        last_price:
          type: string
        low:
          type: string
        lowest_ask:
          type: string
        price_change_percentage:
          type: string
        price_change:
          type: string
        quote_volume:
          type: string
        sequence:
          type: integer
        state:
          type: string
      required:
        - base_volume
        - high
        - highest_bid
        - instrument_code
        - last_price
        - low
        - lowest_ask
        - price_change_percentage
        - price_change
        - quote_volume
        - sequence
        - state
      x-apidog-orders:
        - base_volume
        - high
        - highest_bid
        - instrument_code
        - last_price
        - low
        - lowest_ask
        - price_change_percentage
        - price_change
        - quote_volume
        - sequence
        - state
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Introduction

## How futures work at One Trading
At One Trading, our futures platform is designed to offer precision, speed, and transparency, setting us apart as the only MIFID II regulated venue in Europe, and the only venue with minute-level settlements. This means that every open position is settled every minute, allowing for the realisation of profits and losses at unparalleled speed. This frequent settlement ensures a clear and up-to-date account of your portfolio, empowering you to make informed trading decisions.

Our futures contracts are perpetual, meaning they do not have an expiry date. These contracts allow traders to speculate on the price of assets without the need to hold the underlying asset, offering flexibility and leverage to enhance trading strategies.

## Identifying futures instruments
To find which assets are available for futures trading, use the [Instruments](https://docs.onetrading.com/rest/public/instruments.md) endpoint. Look for instruments with the type `PERP`, which indicates perpetual futures contracts, the endpoint allows filtering specifically by `type`. Each instrument is uniquely identified using the `id` property, e.g. `BTC_EUR_P`. This ID is what you would use to create orders for a particular futures market, as well as get positions data for it.

## Creating futures orders

:::info[Note]
You can only place orders on futures markets from futures subaccounts. These are created on the [One Trading UI](https://fast.exchange.onetrading.com/).
:::

Creating orders for futures markets works similarly to spot markets, using the same [Create Order](https://docs.onetrading.com/rest/trading/create-order.md) endpoint. The key difference lies in the id of the market you wish to trade. For futures, use the instrument ID of the perpetual market, such as `BTC_EUR_P`.

Unlike spot trading, futures orders leverage your account's margin, enabling you to open larger positions than your account balance alone would allow. There's no need to specify leverage when creating an order — your available margin determines the maximum order size. For example, if you have €100,000 of available margin, you could create an order of up to that value.

This streamlined approach ensures a simplified order creation process while empowering you to fully utilise the flexibility and leverage offered by perpetual futures trading.

## Collateral for futures trading
To determine how much of a particular asset can be collateralised, refer to the [Currencies](https://docs.onetrading.com/rest/public/currencies.md) endpoint. Each currency includes a property called `collateral_percentage`, indicating the percentage of that asset’s value that can be used as collateral against futures positions.

For example:

If the collateral_percentage for an asset is 50%, and you hold €1,000 worth of that asset, €500 can be used as collateral for futures trading.
This flexible collateral system enables you to optimise your portfolio and efficiently manage your margin requirements.


:::info[Note]
We currently only support EUR as collateral for futures positions.
:::

## Funding rate
Futures trading on One Trading incorporates a funding rate, which is a periodic payment between long and short position holders designed to keep the perpetual contract's price aligned with the underlying asset's spot price.

**Calculation Period**: Funding rates are settled on a 4-hour basis.

**Update Frequency**: The funding rate is updated minutely, ensuring that traders have the most accurate and timely information about their obligations or entitlements.

This approach ensures that funding payments reflect current market conditions, contributing to a fair and balanced trading environment.

The funding rate mechanism is an essential aspect of perpetual futures trading, ensuring price stability and reducing discrepancies between futures and spot prices.

Use the [Current Funding Rate](https://docs.onetrading.com/futures/current-funding-rate.md) endpoint to get the latest **1 minute** calculated funding rate.

Use the [Funding Rate History](https://docs.onetrading.com/futures/funding-rate-history.md) endpoint to get the historical 4 hour funding rates used for funding rate payments.

For a deeper dive into how funding rate is calculated, refer to the [Funding Rate Methodology](https://docs.onetrading.com/futures/funding-rate-methodology.md).
# Funding Rate Methodology

Perpetual Futures on One Trading include a funding rate, a periodic payment exchanged every 4 hours between long and short position holders. This mechanism helps align the perpetual contract's price with the underlying asset's spot price. One Trading does not charge fees on the funding rate. 

The funding rate consists of two components:

**Interest Rate Differential**: This component reflects the difference in interest rates between the base currency (the traded asset, e.g., BTC) and the quote currency (e.g., EUR). For example, in a BTC/EUR perpetual futures contract, if the EUR interest rate is higher than BTC's (which typically has no yield), the long position holder pays this differential to the short position holder. This is because the long position is effectively borrowing EUR (high interest rate) to gain BTC exposure (no/low interest rate). The interest rate component helps keep futures prices aligned with spot prices by accounting for the cost of holding positions.

**Premium Index**: This represents the difference between futures and spot prices. When futures trade at a premium, the long position pays funding to the short position, encouraging more shorts and fewer longs, thus converging prices. Conversely, when futures trade at a discount, the short position pays funding to the long position. This self-correcting mechanism maintains alignment between futures and spot prices.

## Methodology
### Interest Component

Set as a yearly percentage per market and converted to the funding period using the formula:

$ r = (1 + R)^{\frac{1}{n}} - 1 $


Where: \( $r$ \) is the period rate, \( $R$ \) is the annual interest rate, and \( $n$ \) is the number of funding periods per year.

### Premium Index
Given the Mark Price and Index Price, the premium index  \( $P$ \) series is calculated every 1 minute using the following equation:


![Screenshot 2025-04-09 at 15.11.47.png](https://api.eu.apidog.com/api/v1/projects/349694/resources/338675/image-preview)

where the $\text{Index Price} $ is the weighted average spot price of the underlying asset listed on major spot exchanges. 

#### Time-Weighted Average Premium Index

The time-weighted average premium index \( $\bar{P}$ \) is calculated over the funding period using the premium index series:


![Screenshot 2025-04-09 at 15.11.54.png](https://api.eu.apidog.com/api/v1/projects/349694/resources/338674/image-preview)

where $P_t$ denotes the t-th 1-minute observation of $P$, $w_t = w_0 + \alpha t$ is the weight for each observation (with $w_0$ being the starting weight and $\alpha$ being the scalar step increase), and T is the total number of 1-minute intervals within the 4-hour period.

### Funding Rate Calculation

The preliminary funding rate is calculated as:


![Screenshot 2025-04-09 at 15.11.59.png](https://api.eu.apidog.com/api/v1/projects/349694/resources/338671/image-preview)

where $\beta$ is the clamp boundary parameter.

The clamp function ensures a value stays within a specified range by limiting it to the nearest boundary if it would go outside that range:


![Screenshot 2025-04-09 at 15.12.05.png](https://api.eu.apidog.com/api/v1/projects/349694/resources/338670/image-preview)

Clamping ensures that the dampening adjustment \(-$\bar{P}$\) stays within \(-$\beta$\%\) and \(+$\beta$\%\). This means:
- If \(-$\bar{P}$\) is less than \(-$\beta$\%\), it will be set to \(-$\beta$\%\)
- If \(-$\bar{P}$\) is between \(-$\beta$\%\) and \(+$\beta$\%\), it will remain unchanged
- If \(-$\bar{P}$\) is greater than \(+$\beta$\%\), it will be set to \(+$\beta$\%\)

Finally, a cap is applied to the funding rate to determine the final funding rate:

![Screenshot 2025-04-09 at 15.12.11.png](https://api.eu.apidog.com/api/v1/projects/349694/resources/338669/image-preview)

where $\tau$ is the maximum absolute value allowed for the funding rate, ensuring the rate stays within reasonable bounds.


## Funding Rate Settings

| **Parameter** | **Symbol** | **Description** | **BTC_EUR_P** | **ETH_EUR_P** | **XRP_EUR_P** | **Unit** |
|----------------|-------------|------------------|---------------|---------------|---------------|-----------|
| **Instrument** | $i$ | Instrument code | BTC_EUR_P | ETH_EUR_P | XRP_EUR_P | - |
| **Annual Interest Rate** | $R$ | Yearly interest rate | 2.40% | 2.40% | 2.40% | % p.a. |
| **Period Interest Rate** | $r$ | Calculated period rate¹ | 0.001083% | 0.001083% | 0.001083% | % per period |
| **Funding Period** | $\text{pd}$ | Duration of funding cycle | 240 | 240 | 240 | minutes |
| **Funding Periods/Year** | $n$ | Number of periods per year² | 2,190 (2025) | 2,190 (2025) | 2,190 (2025) | periods |
| **Starting Weight** | $w_0$ | Time-weighted starting weight | 0 | 0 | 0 | - |
| **Alpha Parameter** | $\alpha$ | Time-weighted decay factor | 1 | 1 | 1 | - |
| **Clamp Threshold** | $\beta$ | Dampening clamp boundary | ±0.05% | ±0.05% | ±0.05% | % |
| **Funding Rate Cap** | $\tau$ | Maximum absolute funding rate | ±0.10% | ±0.10% | ±0.10% | % |

---

**Note:**  
The **Clamp Threshold (β)** widens to **±1.5%** from **Friday 20:00 UTC** through **Monday 00:00 UTC**.
# Funding Payments

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /account/futures/funding-payments:
    get:
      summary: Funding Payments
      deprecated: false
      description: >-
        Returns a paginated list of funding payments, grouped by instrument code
        and sorted in descending order by timestamp. If no instrument code is
        provided, funding payments are fetched for all markets.


        Default Behavior for `from` and `to` parameters


        | Parameters Provided | Behavior |

        |-------------------|----------|

        | **Neither `from` nor `to`** | Returns last 7 days from UTC midnight to
        current time |

        | **Only `from`** | Returns 7 days starting from the provided `from`
        date |

        | **Only `to`** | Returns 7 days ending at the provided `to` date
        (starting from UTC midnight 7 days prior) |

        | **Both `from` and `to`** | Returns funding payments within the
        specified date range (max 90 days) |





        ### Parameter Specification


        | Parameter       | Accepted Formats | Example Values |

        |-----------------|----------------|----------------|

        | `from`          | ISO 8601        | `2025-09-25T13:45:30Z` (s),
        `2025-09-25T13:45:30.123Z` (ms), `2025-09-25T13:45:30.123456Z` (us) |

        |                 | Epoch           | `1695647130` (s), `1695647130123`
        (ms), `1695647130123456` (us) |

        |                 | Date            | `2025-09-25` |

        | `to`            | ISO 8601        | `2025-09-26T18:00:00Z` (s),
        `2025-09-26T18:00:00.456Z` (ms), `2025-09-26T18:00:00.456789Z` (us) |

        |                 | Epoch           | `1695734400` (s), `1695734400456`
        (ms), `1695734400456789` (us) |

        |                 | Date            | `2025-09-26` |

        | `instrument_code` | String         | `BTC_EUR_P` (single) |

        |                  | List           | `BTC_EUR_P,ETH_EUR_P`
        (comma-separated list) |

        | `max_page_size`  | Integer        | `3` |

        | `cursor`         | String         |
        `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |


        ### Parameter Limits


        | Parameter        | Constraints / Range |

        |------------------|-------------------|

        | `from`           | Date between **2024-01-01** and **present** |

        | `to`             | Date **not earlier than** `from`; the period
        between `from` and `to` **must not exceed 30 days** |

        | `max_page_size`  | Integer between **0** and **10** |

        | `instrument_code`| Optional; must be valid market code(s) |

        | `cursor`         | Optional; string returned by previous response |


        ### Parameter Defaults


        | Parameter(s)    | Default Behavior |

        |-----------------|-----------------|

        | `from` / `to`   | Neither provided: `from` = 7 days ago at midnight
        UTC, `to` = present time |

        | `from` / `to`   | Only `from` provided: `to` = 7 days later or present
        time, whichever is smaller |

        | `from` / `to`   | Only `to` provided: `from` = 7 days earlier |

        | `instrument_code`| Defaults to all perpetual markets |

        | `max_page_size` | Defaults to 3 |
      tags:
        - One Trading Public REST API/Futures
      parameters:
        - name: from
          in: query
          description: 'Specifies the start of the period. '
          required: false
          example: '2025-10-15T10:30:00Z'
          schema:
            type: string
            enum:
              - '2025-01-15'
            x-apidog-enum:
              - value: '2025-01-15'
                name: date-string
                description: 'Date strings in '
            format: date-time
        - name: to
          in: query
          description: >-
            Specifies the end of the period; the range between start and end
            cannot exceed 90 days.
          required: false
          example: '2025-11-16T10:30:00Z'
          schema:
            type: string
        - name: instrument_code
          in: query
          description: >-
            Instrument(s) to filter by. Can be a single pair or a
            comma-separated string of pairs. Defaults to all instruments.
          required: false
          example: ''
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            Pointer indicating where the next page of results will be retrieved
            from.
          required: false
          example: ''
          schema:
            type: string
        - name: max_page_size
          in: query
          description: >-
            Sets the maximum number of results per page (default and maximum:
            200).
          required: false
          example: 100
          schema:
            type: integer
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  account_id:
                    type: string
                    description: The unique identifier for the futures account.
                    x-apidog-mock: '{{$string.uuid}}'
                    format: uuid
                  funding_payments:
                    type: object
                    properties:
                      instrument_code:
                        type: string
                        x-apidog-mock: '{{$string.symbol}}'
                        description: >-
                          The unique identifier for the futures market, e.g.
                          BTC_EUR_P.
                      funding_payment:
                        type: string
                        description: Funding payment amount, expressed in quote currency.
                      cash_balance:
                        type: string
                        description: >-
                          Cash balances after payment, expressed in quote
                          currency.
                    x-apidog-orders:
                      - instrument_code
                      - funding_payment
                      - cash_balance
                    required:
                      - instrument_code
                      - funding_payment
                      - cash_balance
                    description: Object containing funding payment details.
                  max_page_size:
                    type: integer
                    description: The paginated batch size.
                  cursor:
                    type: integer
                    description: >-
                      If more records are available, pass the returned cursor
                      into the next request to fetch the following batch of
                      funding payments.
                x-apidog-orders:
                  - account_id
                  - funding_payments
                  - max_page_size
                  - cursor
                required:
                  - funding_payments
                  - account_id
                  - max_page_size
          headers: {}
          x-apidog-name: OK
        '400':
          description: ''
          content:
            application/json:
              schema:
                title: ''
                type: object
                properties:
                  error:
                    type: string
                    description: Reason
                x-apidog-orders:
                  - error
                required:
                  - error
              example:
                error: Reason for rejection.
          headers: {}
          x-apidog-name: Bad Request
        '403':
          description: ''
          content:
            application/json:
              schema:
                title: ''
                type: object
                properties:
                  error:
                    type: string
                    description: Reason
                x-apidog-orders:
                  - error
                required:
                  - error
              example:
                error: Permission denied.
          headers: {}
          x-apidog-name: Forbidden
        '500':
          description: ''
          content:
            application/json:
              schema:
                title: ''
                type: object
                properties:
                  error:
                    type: string
                    description: Reason
                x-apidog-orders:
                  - error
                required:
                  - error
              example:
                error: Server error.
          headers: {}
          x-apidog-name: ServerError
      security:
        - bearer: []
      x-apidog-folder: One Trading Public REST API/Futures
      x-apidog-status: developing
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3877628-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Current Funding Rate

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /funding-rate:
    get:
      summary: Current Funding Rate
      deprecated: false
      description: >-
        Retrieve the current funding rate for one or all futures instruments.
        The funding rate is calculated every minute but is settled every 4
        hours.


        An instrument code is the `id` property from the
        [Instruments](https://docs.onetrading.com/rest/public/instruments.md)
        endpoint.



        :::info[]

        Funding rates are only available for futures markets.

        :::
      tags:
        - One Trading Public REST API/Futures
      parameters:
        - name: instrument_code
          in: query
          description: >-
            The specific instrument code (e.g. `BTC_EUR_P`) to fetch the funding
            rate for. If not provided, returns funding rates for all futures
            instruments.
          required: false
          example: BTC_EUR_P
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/FundingRateCurrent'
              examples:
                '1':
                  summary: Single Instrument Code
                  value:
                    - instrument_code: BTC_EUR_P
                      funding_rate: '0.02500000'
                      mark_price: '92500'
                      time: 1733397081146
                '2':
                  summary: Multiple Instruments
                  value:
                    - instrument_code: BTC_EUR_P
                      funding_rate: '0.02500000'
                      mark_price: '92500'
                      time: 1733397081146
                    - instrument_code: ETH_EUR_P
                      funding_rate: '0.00214000'
                      mark_price: '3726.58'
                      time: 1733397081146
          headers: {}
          x-apidog-name: Success
      security: []
      x-apidog-folder: One Trading Public REST API/Futures
      x-apidog-status: developing
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3642873-run
components:
  schemas:
    FundingRateCurrent:
      type: object
      properties:
        instrument_code:
          type: string
          description: The unique identifier for the instrument
          x-apidog-mock: BTC_EUR_P
        funding_rate:
          type: string
          description: >-
            The current funding rate for the specified instrument in fractional
            form. Negative rates indicate shorts paying longs, and positive
            rates indicate longs paying shorts.
          x-apidog-mock: '0.00002500000'
        mark_price:
          type: string
          description: >-
            The current mark price of the instrument, used as the reference
            price for funding rate calculation.
          x-apidog-mock: '92500'
        time:
          type: integer
          description: >-
            Unix timestamp (in milliseconds) indicating when the funding rate
            was last calculated.
          x-apidog-mock: '1733397081146'
      x-apidog-orders:
        - instrument_code
        - funding_rate
        - mark_price
        - time
      required:
        - instrument_code
        - funding_rate
        - mark_price
        - time
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```
# Funding Rate History

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /funding-rate/history:
    get:
      summary: Funding Rate History
      deprecated: false
      description: >-
        Retrieve the historical funding rates for a specific instrument. This
        endpoint provides the settled funding rates, updated every 4 hours.


        An instrument code is the `id` property from the
        [Instruments](https://docs.onetrading.com/rest/public/instruments.md)
        endpoint.



        :::info[]

        Funding rates are only available for futures markets.

        :::
      tags:
        - One Trading Public REST API/Futures
      parameters:
        - name: instrument_code
          in: query
          description: >-
            The specific instrument code (e.g. `BTC_EUR_P`) to fetch the funding
            rate for.
          required: true
          example: BTC_EUR_P
          schema:
            type: string
        - name: from
          in: query
          description: Timestamp in ms to get funding rate from (INCLUSIVE)
          required: false
          example: 1733397387858
          schema:
            type: integer
        - name: to
          in: query
          description: Timestamp in ms to get funding rate until (INCLUSIVE)
          required: false
          example: 1733411787858
          schema:
            type: integer
        - name: limit
          in: query
          description: Number of funding rate history records to return
          required: false
          example: 1000
          schema:
            type: integer
            maximum: 1000
            minimum: 1
            default: 100
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/FundingRateSettled'
              example:
                - instrument_code: BTC_EUR_P
                  funding_rate: '0.00002221799'
                  mark_price: '92525.35'
                  time: 1733397387858
                - instrument_code: BTC_EUR_P
                  funding_rate: '0.00002311127'
                  mark_price: '92812.40'
                  time: 1733411787858
                - instrument_code: BTC_EUR_P
                  funding_rate: '0.00002329418'
                  mark_price: '92955.98'
                  time: 1733411787858
          headers: {}
          x-apidog-name: Success
      security: []
      x-apidog-folder: One Trading Public REST API/Futures
      x-apidog-status: developing
      x-run-in-apidog: https://app.eu.apidog.com/web/project/349694/apis/api-3642952-run
components:
  schemas:
    FundingRateSettled:
      type: object
      properties:
        instrument_code:
          type: string
          description: The unique identifier for the instrument
          x-apidog-mock: BTC_USD_P
        funding_rate:
          type: string
          description: >-
            The funding rate applied at the time of settlement in fractional
            form. Negative rates indicate shorts paying longs, and positive
            rates indicate longs paying shorts.
          x-apidog-mock: '0.000017909161806883844'
        mark_price:
          type: string
          description: >-
            The mark price of the instrument at the time the funding rate was
            settled.
          x-apidog-mock: '87829.7'
        time:
          type: integer
          description: >-
            Millisecond Unix timestamp indicating the end of the funding period
            (deprecated; will be removed in future versions).
          x-apidog-mock: '1766491200000'
          deprecated: true
        timestamp:
          type: string
          description: >-
            Timestamp indicating the end of the funding period (ISO 8601 format,
            seconds precision).
          x-apidog-mock: '2025-12-23T12:00:00Z'
      x-apidog-orders:
        - instrument_code
        - funding_rate
        - mark_price
        - time
        - timestamp
      required:
        - instrument_code
        - funding_rate
        - mark_price
        - time
        - timestamp
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes: {}
servers:
  - url: https://api.onetrading.com/fast/v1
    description: Production Env
security: []

```





# Book Tick

:::warning[]
You must be [subscribed](https://docs.onetrading.com/websocket/subscribe.md) to the BOOK_TICKER channel to receive any book ticker related updates.
:::


```json
{
    "channel_name": "BOOK_TICKER",
    "type": "BOOK_TICK",
    "time": 1732056122430542800,
    "instrument_code": "BTC_EUR",
    "data": {
        "best_bid": "57500",
        "bid_amount": "0.1",
        "best_ask": "58000",
        "ask_amount": "0.1"
    }
}
```

<DataSchema id="406546" />

























































# Introduction

The One Trading WebSocket (WSS) API provides clients with access to real-time data feeds, including price evolution and market state information. In addition to subscribing to data feeds, the API allows clients to create and cancel orders over the same WebSocket connection.

<Container>
    WebSocket URL: 
  **<CopyToClipboard>wss://streams.fast.onetrading.com</CopyToClipboard>**
</Container>
# Authenticate


<Container>
  WebSocket URL:
**<CopyToClipboard>wss://streams.onetrading.com</CopyToClipboard>**

</Container>

All private channels require client authentication before subscription. Clients should first send an `AUTHENTICATE` message containing the API token, after which they can subscribe to any private channel. If the supplied API token is valid, it will be used to authorize subscriptions and requests for all private channels within this WebSocket connection.

An API token can be generated in the [One Trading UI](https://fast.exchange.onetrading.com/).


:::warning[]
You must ensure the API token you generate has the `Trade` permission, otherwise you will receive an `AUTH_ERROR`.
:::

## Authentication Request


```json
{
  "type": "AUTHENTICATE",
  "api_token": "eyJ..."
}
```

<DataSchema id="406381" />

## Authentication Response

### Success

```json
{
  "type": "AUTHENTICATED"
}
```

<DataSchema id="406385" />

### Error

```json
{
  "error": "AUTHENTICATION_FAILED"
}
```

<DataSchema id="406386" />
# Subscribe

Before you can send messages to a particular WebSocket channel, you must first subscribe to it.

Some of the market data websocket channels take an `instrument_codes` property alongside the name of the channel.


:::info[Note]
You can only subscribe to **one** channel in a single `SUBSCRIBE` message.
:::

### Subscription Request

```json
{
    "type": "SUBSCRIBE",
    "channels": [
      {
        "name": "TRADING"
      }
    ]
}
```

<DataSchema id="406387" />

### Subscription Response

#### Success
```json
{
    "type": "SUBSCRIPTIONS",
    "channels": [
        {
            "name": "TRADING"
        }
    ],
    "time": 1731671164898119453
}
```

<DataSchema id="406388" />

#### Error

```json
{
    "error": "Invalid channel."
}
```

<DataSchema id="406389" />
# Ping / Pong

# Overview
To ensure stable and reliable WebSocket connections, we have implemented native ping-pong support in our WebSocket API. This helps detect and close broken connections, preventing clients from holding onto stale sockets.

## How It Works
The WebSocket `ping` is sent from the client to check if the server is still responsive.
The server responds with a `pong` message, confirming that the connection is alive.
If a `pong` response is not received within a certain timeout period, the client should attempt to reconnect.

## Best Practices for Ping Management
A recommended strategy is to send a ping when receiving a heartbeat message from the server. This ensures efficient connection health monitoring without unnecessary traffic.

Example Workflow:


<Steps>
  <Step>
    The server sends a periodic heartbeat message.
      ```json
      {
        "type": "HEARTBEAT",
        "time": 1738602951685555981
      }
      ```
  </Step>
  <Step>
    Upon receiving a heartbeat, the client sends a ping request.
  </Step>
  <Step>
    The server responds with a pong, confirming that the connection is still active.
  </Step>
  <Step>
    If no pong response is received within a timeout period, the client should close the socket and reconnect.
  </Step>
</Steps>
# Introduction

The `ORDER_BOOK` WebSocket Channel allows clients to access real-time order book data for specified market(s). This channel provides an initial snapshot of the order book, giving a complete view of active bids and asks at the time of connection. Following the snapshot, clients receive incremental updates as changes occur in the order book, such as new orders, modifications, or cancellations.


## Subscribe

```json
{
    "type": "SUBSCRIBE",
    "channels": [
        {
            "name": "ORDER_BOOK",
            "instrument_codes": [
                "BTC_EUR",
                "ETH_EUR"
            ]
        }
    ]
}
```

## Subscription Confirmation

```json
{
    "type": "SUBSCRIPTIONS",
    "channels": [
        {
            "name": "ORDER_BOOK",
            "instrument_codes": [
                "BTC_EUR",
                "ETH_EUR"
            ]
        }
    ],
    "time": 1732050545807000000
}
```
# Orderbook Snapshot


:::warning[]
You must be [subscribed](https://docs.onetrading.com/websocket/subscribe.md) to the ORDER_BOOK channel to receive any order book related updates. You will only receive updates for `instrument_codes` you have specified.
:::

The `ORDER_BOOK_SNAPSHOT` provides an immediate overview of all the bids and aks in a particular market at the time of subscription.

```json
{
    "channel_name": "ORDER_BOOK",
    "type": "ORDER_BOOK_SNAPSHOT",
    "time": 1715268699262970610,
    "instrument_code": "BTC_EUR",
    "asks": [
        [
            "100000",
            "4"
        ]
    ],
    "bids": [
        [
            "10000",
            "6"
        ]
    ]
}
```

<DataSchema id="406395" />
# Orderbook Update

:::warning[]
You must be [subscribed](https://docs.onetrading.com/websocket/subscribe.md) to the ORDER_BOOK channel to receive any order book related updates. You will only receive updates for `instrument_codes` you have specified.
:::

The ORDER_BOOK_UPDATE provides an immediate overview of all the bids and aks in a particular market at the time of subscription.

```json
{
  "type": "ORDER_BOOK_UPDATE",
  "channel_name": "ORDER_BOOK",
  "time": 1715268699262970610,
  "instrument_code": "BTC_EUR",
  "changes": [
    [
      "BUY",
      "6500.09",
      "0.84702376"
    ]
  ]
}
```

In the array of changes, the 3 components are:

```json
[
  "BUY", // SIDE
  "6500.09", // PRICE
  "0.84702376" // AMOUNT
]
```

If the amount value is `0`, this means the price level has been removed from the orderbook.

<DataSchema id="406397" />


# Introduction

The `PRICE_TICKS` WebSocket channel provides clients with real-time price updates for specified market(s). This channel streams individual price tick events as they occur, offering granular insights into the latest trades and price movements. Each tick represents a single trade execution, including details such as price, quantity, and nanosecond timestamp.

For each instrument code specified, a price tick history will be sent initially containing the latest `80` price ticks.

## Subscribe

```json
{
    "type": "SUBSCRIBE",
    "channels": [
        {
            "name": "PRICE_TICKS",
            "instrument_codes": [
                "BTC_EUR",
                "ETH_EUR"
            ]
        }
    ]
}
```

## Subscription Confirmation

```json
{
    "type": "SUBSCRIPTIONS",
    "channels": [
        {
            "name": "PRICE_TICKS",
            "instrument_codes": [
                "BTC_EUR",
                "ETH_EUR"
            ]
        }
    ],
    "time": 1732051274299000000
}
```


<DataSchema id="408012" />
# Price Tick

:::warning[]
You must be [subscribed](https://docs.onetrading.com/websocket/subscribe.md) to the PRICE_TICKS channel to receive any price tick related updates. You will only receive updates for `instrument_codes` you have specified.
:::

When a trade is executed, a price tick is emitted.

```json
{
    "channel_name": "PRICE_TICKS",
    "type": "PRICE_TICK",
    "time": 1732051723847246300,
    "instrument_code": "BTC_EUR",
    "price": "100000",
    "amount": "0.001",
    "volume": "100",
    "best_bid": "10000",
    "best_ask": "100000",
    "taker_side": "BUY"
}
```

<DataSchema id="406543" />

# Introduction

The `BOOK_TICKER` WebSocket channel provides real-time updates for the best bid and ask prices, along with their associated quantities, for all symbols. This lightweight channel focuses solely on the most critical data points, offering a significant advantage for users who need to act quickly without processing the full order book.

Unlike the ORDER_BOOK channel, which delivers a complete and detailed view of all market orders, the BOOK_TICKER channel delivers only the best bid and ask updates. This reduces computational overhead, minimises bandwidth usage, and allows for faster data analysis.

Ideal for trading strategies that rely on top-of-book information, this channel empowers users with the speed and efficiency necessary to stay ahead in fast-moving markets.

## Subscribe

```json
{
    "type": "SUBSCRIBE",
    "channels": [
        {
            "name": "BOOK_TICKER"
        }
    ]
}
```

## Subscription Confirmation

```json
{
    "type": "SUBSCRIPTIONS",
    "channels": [
        {
            "name": "BOOK_TICKER"
        }
    ],
    "time": 1732051274299000000
}
```


