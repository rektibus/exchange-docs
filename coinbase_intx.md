> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome to Coinbase Advanced Trade API

## Introduction

The Advanced Trade API supports programmatic trading and order management with a REST API and WebSocket protocol for real-time market data. Make sure you read our [documentation and guides](/coinbase-app/introduction/welcome) to get started.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Best Bid/Ask

> Get the best bid/ask for all products. A subset of all products can be returned instead by using the product_ids input.



## OpenAPI

````yaml GET /api/v3/brokerage/best_bid_ask
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/best_bid_ask:
    get:
      tags:
        - Products
      summary: Get Best Bid/Ask
      description: >-
        Get the best bid/ask for all products. A subset of all products can be
        returned instead by using the product_ids input.
      operationId: RetailBrokerageApi_GetBestBidAsk
      parameters:
        - name: product_ids
          description: The list of trading pairs (e.g. 'BTC-USD').
          in: query
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetBestBidAskResponse
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetBestBidAskResponse
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.GetBestBidAskResponse:
      type: object
      properties:
        pricebooks:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PriceBook
          required:
            - pricebooks
      required:
        - pricebooks
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.PriceBook:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        bids:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.L2Level
          required:
            - bids
        asks:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.L2Level
          required:
            - asks
        time:
          type: string
          format: RFC3339 Timestamp
      required:
        - product_id
        - bids
        - asks
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.L2Level:
      type: object
      properties:
        price:
          type: string
        size:
          type: string
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Market Trades

> Get snapshot information by product ID about the last trades (ticks) and best bid/ask.



## OpenAPI

````yaml GET  /api/v3/brokerage/products/{product_id}/ticker
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/products/{product_id}/ticker:
    get:
      tags:
        - Products
      summary: Get Market Trades
      description: >-
        Get snapshot information by product ID about the last trades (ticks) and
        best bid/ask.
      operationId: RetailBrokerageApi_GetMarketTrades
      parameters:
        - name: product_id
          description: The trading pair (e.g. 'BTC-USD').
          in: path
          required: true
          schema:
            type: string
        - name: limit
          description: 'The number of trades to be returned. '
          in: query
          required: true
          schema:
            type: integer
            format: int32
        - name: start
          description: The UNIX timestamp indicating the start of the time interval.
          in: query
          required: false
          schema:
            type: string
        - name: end
          description: The UNIX timestamp indicating the end of the time interval.
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetMarketTradesResponse
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetMarketTradesResponse
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.GetMarketTradesResponse:
      type: object
      properties:
        trades:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.HistoricalMarketTrade
        best_bid:
          type: string
          example: '291.13'
          description: The best bid for the `product_id`, in quote currency.
        best_ask:
          type: string
          example: '292.40'
          description: The best ask for the `product_id`, in quote currency.
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.HistoricalMarketTrade:
      type: object
      properties:
        trade_id:
          type: string
          example: 34b080bf-fcfd-445a-832b-46b5ddc65601
          description: The ID of the trade that was placed.
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
        price:
          type: string
          example: '140.91'
          description: The price of the trade, in quote currency.
        size:
          type: string
          example: '4'
          description: The size of the trade, in base currency.
        time:
          type: string
          format: RFC3339 Timestamp
          example: '2021-05-31T09:59:59.000Z'
          description: The time of the trade.
        side:
          description: The maker side of the trade.
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.OrderSide
        exchange:
          type: string
          description: The exchange where the trade was placed.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.OrderSide:
      type: string
      enum:
        - BUY
        - SELL
      default: ''
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Product Candles

> Get rates for a single product by product ID, grouped in buckets.



## OpenAPI

````yaml GET /api/v3/brokerage/products/{product_id}/candles
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/products/{product_id}/candles:
    get:
      tags:
        - Products
      summary: Get Product Candles
      description: Get rates for a single product by product ID, grouped in buckets.
      operationId: RetailBrokerageApi_GetCandles
      parameters:
        - name: product_id
          description: The trading pair (e.g. 'BTC-USD').
          in: path
          required: true
          schema:
            type: string
        - name: start
          description: The UNIX timestamp indicating the start of the time interval.
          in: query
          required: true
          schema:
            type: string
        - name: end
          description: The UNIX timestamp indicating the end of the time interval.
          in: query
          required: true
          schema:
            type: string
        - name: granularity
          description: The timeframe each candle represents.
          in: query
          required: true
          schema:
            type: string
            enum:
              - UNKNOWN_GRANULARITY
              - ONE_MINUTE
              - FIVE_MINUTE
              - FIFTEEN_MINUTE
              - THIRTY_MINUTE
              - ONE_HOUR
              - TWO_HOUR
              - FOUR_HOUR
              - SIX_HOUR
              - ONE_DAY
            default: UNKNOWN_GRANULARITY
        - name: limit
          description: >-
            The number of candle buckets to be returned. By default, returns 350
            (max 350).
          in: query
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candles
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candles
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Candles:
      type: object
      properties:
        candles:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candle
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.Candle:
      type: object
      properties:
        start:
          type: string
          example: '1639508050'
          description: The UNIX timestamp indicating the start of the time interval.
        low:
          type: string
          example: '140.21'
          description: Lowest price during the bucket interval.
        high:
          type: string
          example: '140.21'
          description: Highest price during the bucket interval.
        open:
          type: string
          example: '140.21'
          description: Opening price (first trade) in the bucket interval.
        close:
          type: string
          example: '140.21'
          description: Closing price (last trade) in the bucket interval.
        volume:
          type: string
          example: '56437345'
          description: Volume of trading activity during the bucket interval.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Products

> Get a list of the available currency pairs for trading.



## OpenAPI

````yaml GET /api/v3/brokerage/products
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/products:
    get:
      tags:
        - Products
      summary: List Products
      description: Get a list of the available currency pairs for trading.
      operationId: RetailBrokerageApi_GetProducts
      parameters:
        - name: limit
          description: The number of products to be returned.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: offset
          description: The number of products to skip before returning.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: product_type
          description: >-
            Only returns the orders matching this product type. By default,
            returns all product types.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_PRODUCT_TYPE
              - SPOT
              - FUTURE
            default: UNKNOWN_PRODUCT_TYPE
        - name: product_ids
          description: The list of trading pairs (e.g. 'BTC-USD').
          in: query
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
        - name: contract_expiry_type
          description: >-
            Only returns the orders matching the contract expiry type. Only
            applicable if product_type is set to FUTURE.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_CONTRACT_EXPIRY_TYPE
              - EXPIRING
              - PERPETUAL
            default: UNKNOWN_CONTRACT_EXPIRY_TYPE
        - name: expiring_contract_status
          description: Only returns contracts with this status (default is UNEXPIRED).
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_EXPIRING_CONTRACT_STATUS
              - STATUS_UNEXPIRED
              - STATUS_EXPIRED
              - STATUS_ALL
            default: UNKNOWN_EXPIRING_CONTRACT_STATUS
        - name: get_tradability_status
          description: >-
            Whether or not to populate view_only with the tradability status of
            the product. This is only enabled for SPOT products.
          in: query
          required: false
          schema:
            type: boolean
        - name: get_all_products
          description: >-
            If true, return all products of all product types (including expired
            futures contracts).
          in: query
          required: false
          schema:
            type: boolean
        - name: products_sort_order
          description: >-
            The order in which products are returned. By default, products are
            returned in 24 hour volume descending (in quote).
          in: query
          required: false
          schema:
            type: string
            enum:
              - PRODUCTS_SORT_ORDER_UNDEFINED
              - PRODUCTS_SORT_ORDER_VOLUME_24H_DESCENDING
              - PRODUCTS_SORT_ORDER_LIST_TIME_DESCENDING
            default: PRODUCTS_SORT_ORDER_UNDEFINED
        - name: cursor
          description: >-
            The cursor to use for pagination. This will be a base64 encoded
            string that decodes into the last productId of the previously
            returned page
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Products:
      type: object
      properties:
        products:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Product
          description: Array of objects, each representing one product.
        num_products:
          type: integer
          format: int32
          example: 100
          description: Number of products that were returned.
        pagination:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.Product:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        price:
          type: string
          example: '140.21'
          description: The current price for the product, in quote currency.
          required:
            - price
        price_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the price of the product has changed, in percent, in the
            last 24 hours.
          required:
            - price_percentage_change_24h
        volume_24h:
          type: string
          example: '1908432'
          description: The trading volume for the product in the last 24 hours.
          required:
            - volume_24h
        volume_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the volume of the product has changed, in percent, in the
            last 24 hours.
          required:
            - volume_percentage_change_24h
        base_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount base value can be increased or decreased at once.
          required:
            - base_increment
        quote_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount quote value can be increased or decreased at once.
          required:
            - quote_increment
        quote_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of quote currency.
          required:
            - quote_min_size
        quote_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of quote currency.
          required:
            - quote_max_size
        base_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of base currency.
          required:
            - base_min_size
        base_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of base currency.
          required:
            - base_max_size
        base_name:
          type: string
          example: Bitcoin
          description: Name of the base currency.
          required:
            - base_name
        quote_name:
          type: string
          example: US Dollar
          description: Name of the quote currency.
          required:
            - quote_name
        watched:
          type: boolean
          example: true
          description: Whether or not the product is on the user's watchlist.
          required:
            - watched
        is_disabled:
          type: boolean
          example: false
          description: Whether or not the product is disabled for trading.
          required:
            - is_disabled
        new:
          type: boolean
          example: true
          description: Whether or not the product is 'new'.
          required:
            - new
        status:
          type: string
          description: Status of the product.
          required:
            - status
        cancel_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be cancelled, not
            placed or edited.
          required:
            - cancel_only
        limit_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be limit orders, not
            market orders.
          required:
            - limit_only
        post_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be posted, not
            cancelled.
          required:
            - post_only
        trading_disabled:
          type: boolean
          example: false
          description: >-
            Whether or not the product is disabled for trading for all market
            participants.
          required:
            - trading_disabled
        auction_mode:
          type: boolean
          example: true
          description: Whether or not the product is in auction mode.
          required:
            - auction_mode
        product_type:
          description: Type of the product.
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductType
        quote_currency_id:
          type: string
          example: USD
          description: Symbol of the quote currency.
        base_currency_id:
          type: string
          example: BTC
          description: Symbol of the base currency.
        fcm_trading_session_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails
        mid_market_price:
          type: string
          example: '140.22'
          description: The current midpoint of the bid-ask spread, in quote currency.
        alias:
          type: string
          example: BTC-USD
          description: Product id for the corresponding unified book.
        alias_to:
          type: array
          example:
            - BTC-USDC
          items:
            type: string
          description: Product ids that this product serves as an alias for.
        base_display_symbol:
          type: string
          example: BTC
          description: Symbol of the base display currency.
          required:
            - base_display_symbol
        quote_display_symbol:
          type: string
          example: USD
          description: Symbol of the quote display currency.
          required:
            - quote_display_symbol
        view_only:
          type: boolean
          example: true
          description: >-
            Reflects whether an FCM product has expired. For SPOT, set
            get_tradability_status to get a return value here. Defaulted to
            false for all other product types.
        price_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount price can be increased or decreased at once.
        display_name:
          type: string
          example: BTC PERP
          description: Display name for the product e.g. BTC-PERP-INTX => BTC PERP
        product_venue:
          example: neptune
          description: >-
            The sole venue id for the product. Defaults to CBE if the product is
            not specific to a single venue
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductVenue
        approximate_quote_24h_volume:
          type: string
          example: '1908432'
          description: >-
            The approximate trading volume for the product in the last 24 hours
            based on the current quote.
        new_at:
          type: string
          format: RFC3339 Timestamp
          example: '2021-07-01T00:00:00.000Z'
          description: >-
            The timestamp when the product was listed. This is only populated if
            product has new tag.
        market_cap:
          type: string
          example: '1500000000000'
          description: The market capitalization of the product's base asset.
        icon_color:
          type: string
          example: red
          description: color for icon display
        icon_url:
          type: string
          example: https://metadata.cbhq.net/equity_icons/123456789.png
          description: A URL to the icon image.
        display_name_overwrite:
          type: string
          example: Bitcoin Perpetual
          description: An alternative name to display for the product.
        is_alpha_testing:
          type: boolean
          example: false
          description: flag for alpha user testing
        about_description:
          type: string
          example: >-
            nano Crude Oil Futures is a monthly cash-settled contract that
            allows participants to manage risk, trade on margin, or speculate on
            the price of oil.
          description: description used in about section for an asset
        future_product_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails
      title: Get Products
      required:
        - product_id
        - price
        - volume_24h
        - price_percentage_change_24h
        - volume_percentage_change_24h
        - base_increment
        - quote_increment
        - quote_min_size
        - quote_max_size
        - base_min_size
        - base_max_size
        - base_name
        - quote_name
        - watched
        - is_disabled
        - new
        - status
        - cancel_only
        - limit_only
        - post_only
        - trading_disabled
        - auction_mode
        - base_display_symbol
        - quote_display_symbol
    coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata:
      type: object
      properties:
        prev_cursor:
          type: string
        next_cursor:
          type: string
        has_next:
          type: boolean
        has_prev:
          type: boolean
      description: Pagination metadata for paginated responses.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.ProductType:
      type: string
      enum:
        - UNKNOWN_PRODUCT_TYPE
        - SPOT
        - FUTURE
      default: UNKNOWN_PRODUCT_TYPE
      description: Defines the type of a product.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails:
      type: object
      properties:
        is_session_open:
          type: boolean
        open_time:
          type: string
          format: RFC3339 Timestamp
        close_time:
          type: string
          format: RFC3339 Timestamp
        session_state:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState
        after_hours_order_entry_disabled:
          type: boolean
        closed_reason:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason
        maintenance:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance
    coinbase.public_api.authed.retail_brokerage_api.ProductVenue:
      type: string
      enum:
        - UNKNOWN_VENUE_TYPE
        - CBE
        - FCM
        - INTX
      default: UNKNOWN_VENUE_TYPE
      description: Defines the venue of a product.
    coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails:
      type: object
      properties:
        venue:
          type: string
        contract_code:
          type: string
        contract_expiry:
          type: string
          format: RFC3339 Timestamp
        contract_size:
          type: string
        contract_root_unit:
          type: string
        group_description:
          type: string
        contract_expiry_timezone:
          type: string
        group_short_description:
          type: string
        risk_managed_by:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.RiskManagementType
        contract_expiry_type:
          description: The contract expiry type (e.g. 'EXPIRING').
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType
        perpetual_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails
        contract_display_name:
          type: string
        time_to_expiry_ms:
          type: string
          format: int64
        non_crypto:
          type: boolean
        contract_expiry_name:
          type: string
        twenty_four_by_seven:
          type: boolean
        funding_interval:
          type: string
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        display_name:
          type: string
        region_enabled:
          type: object
          additionalProperties:
            type: boolean
        intraday_margin_rate:
          description: Margin rates during intraday trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        overnight_margin_rate:
          description: Margin rates during overnight trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        settlement_price:
          type: string
          description: The most recent official settlement price for the futures contract
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState:
      type: string
      enum:
        - FCM_TRADING_SESSION_STATE_UNDEFINED
        - FCM_TRADING_SESSION_STATE_PRE_OPEN
        - FCM_TRADING_SESSION_STATE_PRE_OPEN_NO_CANCEL
        - FCM_TRADING_SESSION_STATE_OPEN
        - FCM_TRADING_SESSION_STATE_CLOSE
      default: FCM_TRADING_SESSION_STATE_UNDEFINED
      description: Defines the state of a trading session.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason:
      type: string
      enum:
        - FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
        - FCM_TRADING_SESSION_CLOSED_REASON_REGULAR_MARKET_CLOSE
        - FCM_TRADING_SESSION_CLOSED_REASON_EXCHANGE_MAINTENANCE
        - FCM_TRADING_SESSION_CLOSED_REASON_VENDOR_MAINTENANCE
      default: FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
      description: >-
        This helps distinguish between regular market close and downtimes due to
        maintenance.
    coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance:
      type: object
      properties:
        start_time:
          type: string
          format: RFC3339 Timestamp
        end_time:
          type: string
          format: RFC3339 Timestamp
      description: Fcm specific scheduled maintenance details.
    coinbase.public_api.authed.retail_brokerage_api.RiskManagementType:
      type: string
      enum:
        - UNKNOWN_RISK_MANAGEMENT_TYPE
        - MANAGED_BY_FCM
        - MANAGED_BY_VENUE
      default: UNKNOWN_RISK_MANAGEMENT_TYPE
      description: Defines Risk management type.
    coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType:
      type: string
      enum:
        - UNKNOWN_CONTRACT_EXPIRY_TYPE
        - EXPIRING
        - PERPETUAL
      default: UNKNOWN_CONTRACT_EXPIRY_TYPE
      description: Represents the types of contract expiry.
    coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails:
      type: object
      properties:
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        max_leverage:
          type: string
        base_asset_uuid:
          type: string
        underlying_type:
          type: string
    coinbase.public_api.authed.retail_brokerage_api.MarginRate:
      type: object
      properties:
        long_margin_rate:
          type: string
          example: '0.5'
          description: Long margin rate
        short_margin_rate:
          type: string
          example: '0.5'
          description: Short margin rate
      title: Margin rate information for futures products
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Products

> Get a list of the available currency pairs for trading.



## OpenAPI

````yaml GET /api/v3/brokerage/products
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/products:
    get:
      tags:
        - Products
      summary: List Products
      description: Get a list of the available currency pairs for trading.
      operationId: RetailBrokerageApi_GetProducts
      parameters:
        - name: limit
          description: The number of products to be returned.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: offset
          description: The number of products to skip before returning.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: product_type
          description: >-
            Only returns the orders matching this product type. By default,
            returns all product types.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_PRODUCT_TYPE
              - SPOT
              - FUTURE
            default: UNKNOWN_PRODUCT_TYPE
        - name: product_ids
          description: The list of trading pairs (e.g. 'BTC-USD').
          in: query
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
        - name: contract_expiry_type
          description: >-
            Only returns the orders matching the contract expiry type. Only
            applicable if product_type is set to FUTURE.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_CONTRACT_EXPIRY_TYPE
              - EXPIRING
              - PERPETUAL
            default: UNKNOWN_CONTRACT_EXPIRY_TYPE
        - name: expiring_contract_status
          description: Only returns contracts with this status (default is UNEXPIRED).
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_EXPIRING_CONTRACT_STATUS
              - STATUS_UNEXPIRED
              - STATUS_EXPIRED
              - STATUS_ALL
            default: UNKNOWN_EXPIRING_CONTRACT_STATUS
        - name: get_tradability_status
          description: >-
            Whether or not to populate view_only with the tradability status of
            the product. This is only enabled for SPOT products.
          in: query
          required: false
          schema:
            type: boolean
        - name: get_all_products
          description: >-
            If true, return all products of all product types (including expired
            futures contracts).
          in: query
          required: false
          schema:
            type: boolean
        - name: products_sort_order
          description: >-
            The order in which products are returned. By default, products are
            returned in 24 hour volume descending (in quote).
          in: query
          required: false
          schema:
            type: string
            enum:
              - PRODUCTS_SORT_ORDER_UNDEFINED
              - PRODUCTS_SORT_ORDER_VOLUME_24H_DESCENDING
              - PRODUCTS_SORT_ORDER_LIST_TIME_DESCENDING
            default: PRODUCTS_SORT_ORDER_UNDEFINED
        - name: cursor
          description: >-
            The cursor to use for pagination. This will be a base64 encoded
            string that decodes into the last productId of the previously
            returned page
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Products:
      type: object
      properties:
        products:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Product
          description: Array of objects, each representing one product.
        num_products:
          type: integer
          format: int32
          example: 100
          description: Number of products that were returned.
        pagination:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.Product:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        price:
          type: string
          example: '140.21'
          description: The current price for the product, in quote currency.
          required:
            - price
        price_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the price of the product has changed, in percent, in the
            last 24 hours.
          required:
            - price_percentage_change_24h
        volume_24h:
          type: string
          example: '1908432'
          description: The trading volume for the product in the last 24 hours.
          required:
            - volume_24h
        volume_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the volume of the product has changed, in percent, in the
            last 24 hours.
          required:
            - volume_percentage_change_24h
        base_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount base value can be increased or decreased at once.
          required:
            - base_increment
        quote_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount quote value can be increased or decreased at once.
          required:
            - quote_increment
        quote_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of quote currency.
          required:
            - quote_min_size
        quote_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of quote currency.
          required:
            - quote_max_size
        base_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of base currency.
          required:
            - base_min_size
        base_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of base currency.
          required:
            - base_max_size
        base_name:
          type: string
          example: Bitcoin
          description: Name of the base currency.
          required:
            - base_name
        quote_name:
          type: string
          example: US Dollar
          description: Name of the quote currency.
          required:
            - quote_name
        watched:
          type: boolean
          example: true
          description: Whether or not the product is on the user's watchlist.
          required:
            - watched
        is_disabled:
          type: boolean
          example: false
          description: Whether or not the product is disabled for trading.
          required:
            - is_disabled
        new:
          type: boolean
          example: true
          description: Whether or not the product is 'new'.
          required:
            - new
        status:
          type: string
          description: Status of the product.
          required:
            - status
        cancel_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be cancelled, not
            placed or edited.
          required:
            - cancel_only
        limit_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be limit orders, not
            market orders.
          required:
            - limit_only
        post_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be posted, not
            cancelled.
          required:
            - post_only
        trading_disabled:
          type: boolean
          example: false
          description: >-
            Whether or not the product is disabled for trading for all market
            participants.
          required:
            - trading_disabled
        auction_mode:
          type: boolean
          example: true
          description: Whether or not the product is in auction mode.
          required:
            - auction_mode
        product_type:
          description: Type of the product.
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductType
        quote_currency_id:
          type: string
          example: USD
          description: Symbol of the quote currency.
        base_currency_id:
          type: string
          example: BTC
          description: Symbol of the base currency.
        fcm_trading_session_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails
        mid_market_price:
          type: string
          example: '140.22'
          description: The current midpoint of the bid-ask spread, in quote currency.
        alias:
          type: string
          example: BTC-USD
          description: Product id for the corresponding unified book.
        alias_to:
          type: array
          example:
            - BTC-USDC
          items:
            type: string
          description: Product ids that this product serves as an alias for.
        base_display_symbol:
          type: string
          example: BTC
          description: Symbol of the base display currency.
          required:
            - base_display_symbol
        quote_display_symbol:
          type: string
          example: USD
          description: Symbol of the quote display currency.
          required:
            - quote_display_symbol
        view_only:
          type: boolean
          example: true
          description: >-
            Reflects whether an FCM product has expired. For SPOT, set
            get_tradability_status to get a return value here. Defaulted to
            false for all other product types.
        price_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount price can be increased or decreased at once.
        display_name:
          type: string
          example: BTC PERP
          description: Display name for the product e.g. BTC-PERP-INTX => BTC PERP
        product_venue:
          example: neptune
          description: >-
            The sole venue id for the product. Defaults to CBE if the product is
            not specific to a single venue
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductVenue
        approximate_quote_24h_volume:
          type: string
          example: '1908432'
          description: >-
            The approximate trading volume for the product in the last 24 hours
            based on the current quote.
        new_at:
          type: string
          format: RFC3339 Timestamp
          example: '2021-07-01T00:00:00.000Z'
          description: >-
            The timestamp when the product was listed. This is only populated if
            product has new tag.
        market_cap:
          type: string
          example: '1500000000000'
          description: The market capitalization of the product's base asset.
        icon_color:
          type: string
          example: red
          description: color for icon display
        icon_url:
          type: string
          example: https://metadata.cbhq.net/equity_icons/123456789.png
          description: A URL to the icon image.
        display_name_overwrite:
          type: string
          example: Bitcoin Perpetual
          description: An alternative name to display for the product.
        is_alpha_testing:
          type: boolean
          example: false
          description: flag for alpha user testing
        about_description:
          type: string
          example: >-
            nano Crude Oil Futures is a monthly cash-settled contract that
            allows participants to manage risk, trade on margin, or speculate on
            the price of oil.
          description: description used in about section for an asset
        future_product_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails
      title: Get Products
      required:
        - product_id
        - price
        - volume_24h
        - price_percentage_change_24h
        - volume_percentage_change_24h
        - base_increment
        - quote_increment
        - quote_min_size
        - quote_max_size
        - base_min_size
        - base_max_size
        - base_name
        - quote_name
        - watched
        - is_disabled
        - new
        - status
        - cancel_only
        - limit_only
        - post_only
        - trading_disabled
        - auction_mode
        - base_display_symbol
        - quote_display_symbol
    coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata:
      type: object
      properties:
        prev_cursor:
          type: string
        next_cursor:
          type: string
        has_next:
          type: boolean
        has_prev:
          type: boolean
      description: Pagination metadata for paginated responses.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.ProductType:
      type: string
      enum:
        - UNKNOWN_PRODUCT_TYPE
        - SPOT
        - FUTURE
      default: UNKNOWN_PRODUCT_TYPE
      description: Defines the type of a product.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails:
      type: object
      properties:
        is_session_open:
          type: boolean
        open_time:
          type: string
          format: RFC3339 Timestamp
        close_time:
          type: string
          format: RFC3339 Timestamp
        session_state:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState
        after_hours_order_entry_disabled:
          type: boolean
        closed_reason:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason
        maintenance:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance
    coinbase.public_api.authed.retail_brokerage_api.ProductVenue:
      type: string
      enum:
        - UNKNOWN_VENUE_TYPE
        - CBE
        - FCM
        - INTX
      default: UNKNOWN_VENUE_TYPE
      description: Defines the venue of a product.
    coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails:
      type: object
      properties:
        venue:
          type: string
        contract_code:
          type: string
        contract_expiry:
          type: string
          format: RFC3339 Timestamp
        contract_size:
          type: string
        contract_root_unit:
          type: string
        group_description:
          type: string
        contract_expiry_timezone:
          type: string
        group_short_description:
          type: string
        risk_managed_by:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.RiskManagementType
        contract_expiry_type:
          description: The contract expiry type (e.g. 'EXPIRING').
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType
        perpetual_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails
        contract_display_name:
          type: string
        time_to_expiry_ms:
          type: string
          format: int64
        non_crypto:
          type: boolean
        contract_expiry_name:
          type: string
        twenty_four_by_seven:
          type: boolean
        funding_interval:
          type: string
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        display_name:
          type: string
        region_enabled:
          type: object
          additionalProperties:
            type: boolean
        intraday_margin_rate:
          description: Margin rates during intraday trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        overnight_margin_rate:
          description: Margin rates during overnight trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        settlement_price:
          type: string
          description: The most recent official settlement price for the futures contract
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState:
      type: string
      enum:
        - FCM_TRADING_SESSION_STATE_UNDEFINED
        - FCM_TRADING_SESSION_STATE_PRE_OPEN
        - FCM_TRADING_SESSION_STATE_PRE_OPEN_NO_CANCEL
        - FCM_TRADING_SESSION_STATE_OPEN
        - FCM_TRADING_SESSION_STATE_CLOSE
      default: FCM_TRADING_SESSION_STATE_UNDEFINED
      description: Defines the state of a trading session.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason:
      type: string
      enum:
        - FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
        - FCM_TRADING_SESSION_CLOSED_REASON_REGULAR_MARKET_CLOSE
        - FCM_TRADING_SESSION_CLOSED_REASON_EXCHANGE_MAINTENANCE
        - FCM_TRADING_SESSION_CLOSED_REASON_VENDOR_MAINTENANCE
      default: FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
      description: >-
        This helps distinguish between regular market close and downtimes due to
        maintenance.
    coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance:
      type: object
      properties:
        start_time:
          type: string
          format: RFC3339 Timestamp
        end_time:
          type: string
          format: RFC3339 Timestamp
      description: Fcm specific scheduled maintenance details.
    coinbase.public_api.authed.retail_brokerage_api.RiskManagementType:
      type: string
      enum:
        - UNKNOWN_RISK_MANAGEMENT_TYPE
        - MANAGED_BY_FCM
        - MANAGED_BY_VENUE
      default: UNKNOWN_RISK_MANAGEMENT_TYPE
      description: Defines Risk management type.
    coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType:
      type: string
      enum:
        - UNKNOWN_CONTRACT_EXPIRY_TYPE
        - EXPIRING
        - PERPETUAL
      default: UNKNOWN_CONTRACT_EXPIRY_TYPE
      description: Represents the types of contract expiry.
    coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails:
      type: object
      properties:
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        max_leverage:
          type: string
        base_asset_uuid:
          type: string
        underlying_type:
          type: string
    coinbase.public_api.authed.retail_brokerage_api.MarginRate:
      type: object
      properties:
        long_margin_rate:
          type: string
          example: '0.5'
          description: Long margin rate
        short_margin_rate:
          type: string
          example: '0.5'
          description: Short margin rate
      title: Margin rate information for futures products
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````





> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Public Product

> Get information on a single product by product ID.



## OpenAPI

````yaml GET /api/v3/brokerage/market/products/{product_id}
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/market/products/{product_id}:
    get:
      tags:
        - Public
      summary: Get Public Product
      description: Get information on a single product by product ID.
      operationId: RetailBrokerageApi_GetPublicProduct
      parameters:
        - name: product_id
          description: The trading pair (e.g. 'BTC-USD').
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Product
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Product
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Product:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        price:
          type: string
          example: '140.21'
          description: The current price for the product, in quote currency.
          required:
            - price
        price_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the price of the product has changed, in percent, in the
            last 24 hours.
          required:
            - price_percentage_change_24h
        volume_24h:
          type: string
          example: '1908432'
          description: The trading volume for the product in the last 24 hours.
          required:
            - volume_24h
        volume_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the volume of the product has changed, in percent, in the
            last 24 hours.
          required:
            - volume_percentage_change_24h
        base_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount base value can be increased or decreased at once.
          required:
            - base_increment
        quote_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount quote value can be increased or decreased at once.
          required:
            - quote_increment
        quote_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of quote currency.
          required:
            - quote_min_size
        quote_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of quote currency.
          required:
            - quote_max_size
        base_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of base currency.
          required:
            - base_min_size
        base_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of base currency.
          required:
            - base_max_size
        base_name:
          type: string
          example: Bitcoin
          description: Name of the base currency.
          required:
            - base_name
        quote_name:
          type: string
          example: US Dollar
          description: Name of the quote currency.
          required:
            - quote_name
        watched:
          type: boolean
          example: true
          description: Whether or not the product is on the user's watchlist.
          required:
            - watched
        is_disabled:
          type: boolean
          example: false
          description: Whether or not the product is disabled for trading.
          required:
            - is_disabled
        new:
          type: boolean
          example: true
          description: Whether or not the product is 'new'.
          required:
            - new
        status:
          type: string
          description: Status of the product.
          required:
            - status
        cancel_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be cancelled, not
            placed or edited.
          required:
            - cancel_only
        limit_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be limit orders, not
            market orders.
          required:
            - limit_only
        post_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be posted, not
            cancelled.
          required:
            - post_only
        trading_disabled:
          type: boolean
          example: false
          description: >-
            Whether or not the product is disabled for trading for all market
            participants.
          required:
            - trading_disabled
        auction_mode:
          type: boolean
          example: true
          description: Whether or not the product is in auction mode.
          required:
            - auction_mode
        product_type:
          description: Type of the product.
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductType
        quote_currency_id:
          type: string
          example: USD
          description: Symbol of the quote currency.
        base_currency_id:
          type: string
          example: BTC
          description: Symbol of the base currency.
        fcm_trading_session_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails
        mid_market_price:
          type: string
          example: '140.22'
          description: The current midpoint of the bid-ask spread, in quote currency.
        alias:
          type: string
          example: BTC-USD
          description: Product id for the corresponding unified book.
        alias_to:
          type: array
          example:
            - BTC-USDC
          items:
            type: string
          description: Product ids that this product serves as an alias for.
        base_display_symbol:
          type: string
          example: BTC
          description: Symbol of the base display currency.
          required:
            - base_display_symbol
        quote_display_symbol:
          type: string
          example: USD
          description: Symbol of the quote display currency.
          required:
            - quote_display_symbol
        view_only:
          type: boolean
          example: true
          description: >-
            Reflects whether an FCM product has expired. For SPOT, set
            get_tradability_status to get a return value here. Defaulted to
            false for all other product types.
        price_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount price can be increased or decreased at once.
        display_name:
          type: string
          example: BTC PERP
          description: Display name for the product e.g. BTC-PERP-INTX => BTC PERP
        product_venue:
          example: neptune
          description: >-
            The sole venue id for the product. Defaults to CBE if the product is
            not specific to a single venue
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductVenue
        approximate_quote_24h_volume:
          type: string
          example: '1908432'
          description: >-
            The approximate trading volume for the product in the last 24 hours
            based on the current quote.
        new_at:
          type: string
          format: RFC3339 Timestamp
          example: '2021-07-01T00:00:00.000Z'
          description: >-
            The timestamp when the product was listed. This is only populated if
            product has new tag.
        market_cap:
          type: string
          example: '1500000000000'
          description: The market capitalization of the product's base asset.
        icon_color:
          type: string
          example: red
          description: color for icon display
        icon_url:
          type: string
          example: https://metadata.cbhq.net/equity_icons/123456789.png
          description: A URL to the icon image.
        display_name_overwrite:
          type: string
          example: Bitcoin Perpetual
          description: An alternative name to display for the product.
        is_alpha_testing:
          type: boolean
          example: false
          description: flag for alpha user testing
        about_description:
          type: string
          example: >-
            nano Crude Oil Futures is a monthly cash-settled contract that
            allows participants to manage risk, trade on margin, or speculate on
            the price of oil.
          description: description used in about section for an asset
        future_product_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails
      title: Get Products
      required:
        - product_id
        - price
        - volume_24h
        - price_percentage_change_24h
        - volume_percentage_change_24h
        - base_increment
        - quote_increment
        - quote_min_size
        - quote_max_size
        - base_min_size
        - base_max_size
        - base_name
        - quote_name
        - watched
        - is_disabled
        - new
        - status
        - cancel_only
        - limit_only
        - post_only
        - trading_disabled
        - auction_mode
        - base_display_symbol
        - quote_display_symbol
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.ProductType:
      type: string
      enum:
        - UNKNOWN_PRODUCT_TYPE
        - SPOT
        - FUTURE
      default: UNKNOWN_PRODUCT_TYPE
      description: Defines the type of a product.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails:
      type: object
      properties:
        is_session_open:
          type: boolean
        open_time:
          type: string
          format: RFC3339 Timestamp
        close_time:
          type: string
          format: RFC3339 Timestamp
        session_state:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState
        after_hours_order_entry_disabled:
          type: boolean
        closed_reason:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason
        maintenance:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance
    coinbase.public_api.authed.retail_brokerage_api.ProductVenue:
      type: string
      enum:
        - UNKNOWN_VENUE_TYPE
        - CBE
        - FCM
        - INTX
      default: UNKNOWN_VENUE_TYPE
      description: Defines the venue of a product.
    coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails:
      type: object
      properties:
        venue:
          type: string
        contract_code:
          type: string
        contract_expiry:
          type: string
          format: RFC3339 Timestamp
        contract_size:
          type: string
        contract_root_unit:
          type: string
        group_description:
          type: string
        contract_expiry_timezone:
          type: string
        group_short_description:
          type: string
        risk_managed_by:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.RiskManagementType
        contract_expiry_type:
          description: The contract expiry type (e.g. 'EXPIRING').
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType
        perpetual_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails
        contract_display_name:
          type: string
        time_to_expiry_ms:
          type: string
          format: int64
        non_crypto:
          type: boolean
        contract_expiry_name:
          type: string
        twenty_four_by_seven:
          type: boolean
        funding_interval:
          type: string
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        display_name:
          type: string
        region_enabled:
          type: object
          additionalProperties:
            type: boolean
        intraday_margin_rate:
          description: Margin rates during intraday trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        overnight_margin_rate:
          description: Margin rates during overnight trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        settlement_price:
          type: string
          description: The most recent official settlement price for the futures contract
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState:
      type: string
      enum:
        - FCM_TRADING_SESSION_STATE_UNDEFINED
        - FCM_TRADING_SESSION_STATE_PRE_OPEN
        - FCM_TRADING_SESSION_STATE_PRE_OPEN_NO_CANCEL
        - FCM_TRADING_SESSION_STATE_OPEN
        - FCM_TRADING_SESSION_STATE_CLOSE
      default: FCM_TRADING_SESSION_STATE_UNDEFINED
      description: Defines the state of a trading session.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason:
      type: string
      enum:
        - FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
        - FCM_TRADING_SESSION_CLOSED_REASON_REGULAR_MARKET_CLOSE
        - FCM_TRADING_SESSION_CLOSED_REASON_EXCHANGE_MAINTENANCE
        - FCM_TRADING_SESSION_CLOSED_REASON_VENDOR_MAINTENANCE
      default: FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
      description: >-
        This helps distinguish between regular market close and downtimes due to
        maintenance.
    coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance:
      type: object
      properties:
        start_time:
          type: string
          format: RFC3339 Timestamp
        end_time:
          type: string
          format: RFC3339 Timestamp
      description: Fcm specific scheduled maintenance details.
    coinbase.public_api.authed.retail_brokerage_api.RiskManagementType:
      type: string
      enum:
        - UNKNOWN_RISK_MANAGEMENT_TYPE
        - MANAGED_BY_FCM
        - MANAGED_BY_VENUE
      default: UNKNOWN_RISK_MANAGEMENT_TYPE
      description: Defines Risk management type.
    coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType:
      type: string
      enum:
        - UNKNOWN_CONTRACT_EXPIRY_TYPE
        - EXPIRING
        - PERPETUAL
      default: UNKNOWN_CONTRACT_EXPIRY_TYPE
      description: Represents the types of contract expiry.
    coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails:
      type: object
      properties:
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        max_leverage:
          type: string
        base_asset_uuid:
          type: string
        underlying_type:
          type: string
    coinbase.public_api.authed.retail_brokerage_api.MarginRate:
      type: object
      properties:
        long_margin_rate:
          type: string
          example: '0.5'
          description: Long margin rate
        short_margin_rate:
          type: string
          example: '0.5'
          description: Short margin rate
      title: Margin rate information for futures products
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Public Product Book

> Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.



## OpenAPI

````yaml GET /api/v3/brokerage/market/product_book
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/market/product_book:
    get:
      tags:
        - Public
      summary: Get Public Product Book
      description: >-
        Get a list of bids/asks for a single product. The amount of detail shown
        can be customized with the limit parameter.
      operationId: RetailBrokerageApi_GetPublicProductBook
      parameters:
        - name: product_id
          description: The trading pair (e.g. 'BTC-USD').
          in: query
          required: true
          schema:
            type: string
        - name: limit
          description: 'The number of bid/asks to be returned. '
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: aggregation_price_increment
          description: >-
            The minimum price intervals at which buy and sell orders are grouped
            or combined in the order book.
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetProductBookResponse
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.GetProductBookResponse
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.GetProductBookResponse:
      type: object
      properties:
        pricebook:
          required:
            - pricebook
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PriceBook
        last:
          type: string
        mid_market:
          type: string
        spread_bps:
          type: string
        spread_absolute:
          type: string
      required:
        - pricebook
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.PriceBook:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        bids:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.L2Level
          required:
            - bids
        asks:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.L2Level
          required:
            - asks
        time:
          type: string
          format: RFC3339 Timestamp
      required:
        - product_id
        - bids
        - asks
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.L2Level:
      type: object
      properties:
        price:
          type: string
        size:
          type: string
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Public Product Candles

> Get rates for a single product by product ID, grouped in buckets.



## OpenAPI

````yaml GET /api/v3/brokerage/market/products/{product_id}/candles
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/market/products/{product_id}/candles:
    get:
      tags:
        - Public
      summary: Get Public Product Candles
      description: Get rates for a single product by product ID, grouped in buckets.
      operationId: RetailBrokerageApi_GetPublicCandles
      parameters:
        - name: product_id
          description: The trading pair (e.g. 'BTC-USD').
          in: path
          required: true
          schema:
            type: string
        - name: start
          description: The UNIX timestamp indicating the start of the time interval.
          in: query
          required: true
          schema:
            type: string
        - name: end
          description: The UNIX timestamp indicating the end of the time interval.
          in: query
          required: true
          schema:
            type: string
        - name: granularity
          description: The timeframe each candle represents.
          in: query
          required: true
          schema:
            type: string
            enum:
              - UNKNOWN_GRANULARITY
              - ONE_MINUTE
              - FIVE_MINUTE
              - FIFTEEN_MINUTE
              - THIRTY_MINUTE
              - ONE_HOUR
              - TWO_HOUR
              - FOUR_HOUR
              - SIX_HOUR
              - ONE_DAY
            default: UNKNOWN_GRANULARITY
        - name: limit
          description: >-
            The number of candle buckets to be returned. By default, returns 350
            (max 350).
          in: query
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candles
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candles
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Candles:
      type: object
      properties:
        candles:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Candle
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.Candle:
      type: object
      properties:
        start:
          type: string
          example: '1639508050'
          description: The UNIX timestamp indicating the start of the time interval.
        low:
          type: string
          example: '140.21'
          description: Lowest price during the bucket interval.
        high:
          type: string
          example: '140.21'
          description: Highest price during the bucket interval.
        open:
          type: string
          example: '140.21'
          description: Opening price (first trade) in the bucket interval.
        close:
          type: string
          example: '140.21'
          description: Closing price (last trade) in the bucket interval.
        volume:
          type: string
          example: '56437345'
          description: Volume of trading activity during the bucket interval.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Server Time

> Get the current time from the Coinbase Advanced API.



## OpenAPI

````yaml GET /api/v3/brokerage/time
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/time:
    get:
      tags:
        - Public
      summary: Get Server Time
      description: Get the current time from the Coinbase Advanced API.
      operationId: RetailBrokerageApi_GetServerTime
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.retail.rest.proxy.common.ExtendedTimestamp
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.retail.rest.proxy.common.ExtendedTimestamp
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.retail.rest.proxy.common.ExtendedTimestamp:
      type: object
      properties:
        iso:
          type: string
          description: An ISO-8601 representation of the timestamp
        epochSeconds:
          type: string
          format: int64
          description: A second-precision representation of the timestamp
        epochMillis:
          type: string
          format: int64
          description: A millisecond-precision representation of the timestamp
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cdp.coinbase.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Public Products

> Get a list of the available currency pairs for trading.



## OpenAPI

````yaml GET /api/v3/brokerage/market/products
openapi: 3.0.0
info:
  title: Coinbase Advanced Trade API
  version: '0.1'
servers:
  - url: https://api.coinbase.com
security:
  - apiKeyAuth: []
paths:
  /api/v3/brokerage/market/products:
    get:
      tags:
        - Public
      summary: List Public Products
      description: Get a list of the available currency pairs for trading.
      operationId: RetailBrokerageApi_GetPublicProducts
      parameters:
        - name: limit
          description: The number of products to be returned.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: offset
          description: The number of products to skip before returning.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: product_type
          description: >-
            Only returns the orders matching this product type. By default,
            returns all product types.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_PRODUCT_TYPE
              - SPOT
              - FUTURE
            default: UNKNOWN_PRODUCT_TYPE
        - name: product_ids
          description: The list of trading pairs (e.g. 'BTC-USD').
          in: query
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
        - name: contract_expiry_type
          description: >-
            Only returns the orders matching the contract expiry type. Only
            applicable if product_type is set to FUTURE.
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_CONTRACT_EXPIRY_TYPE
              - EXPIRING
              - PERPETUAL
            default: UNKNOWN_CONTRACT_EXPIRY_TYPE
        - name: expiring_contract_status
          description: Only returns contracts with this status (default is UNEXPIRED).
          in: query
          required: false
          schema:
            type: string
            enum:
              - UNKNOWN_EXPIRING_CONTRACT_STATUS
              - STATUS_UNEXPIRED
              - STATUS_EXPIRED
              - STATUS_ALL
            default: UNKNOWN_EXPIRING_CONTRACT_STATUS
        - name: get_all_products
          description: >-
            If true, return all products of all product types (including expired
            futures contracts).
          in: query
          required: false
          schema:
            type: boolean
        - name: products_sort_order
          description: >-
            The order in which products are returned. By default, products are
            returned in 24 hour volume descending (in quote).
          in: query
          required: false
          schema:
            type: string
            enum:
              - PRODUCTS_SORT_ORDER_UNDEFINED
              - PRODUCTS_SORT_ORDER_VOLUME_24H_DESCENDING
              - PRODUCTS_SORT_ORDER_LIST_TIME_DESCENDING
            default: PRODUCTS_SORT_ORDER_UNDEFINED
        - name: cursor
          description: >-
            The cursor to use for pagination. This will be a base64 encoded
            string that decodes into the last productId of the previously
            returned page
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Products
        default:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/grpc.gateway.runtime.Error'
components:
  schemas:
    coinbase.public_api.authed.retail_brokerage_api.Products:
      type: object
      properties:
        products:
          type: array
          items:
            $ref: >-
              #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.Product
          description: Array of objects, each representing one product.
        num_products:
          type: integer
          format: int32
          example: 100
          description: Number of products that were returned.
        pagination:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata
    grpc.gateway.runtime.Error:
      type: object
      properties:
        error:
          type: string
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/google.protobuf.Any'
    coinbase.public_api.authed.retail_brokerage_api.Product:
      type: object
      properties:
        product_id:
          type: string
          example: BTC-USD
          description: The trading pair (e.g. 'BTC-USD').
          required:
            - product_id
        price:
          type: string
          example: '140.21'
          description: The current price for the product, in quote currency.
          required:
            - price
        price_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the price of the product has changed, in percent, in the
            last 24 hours.
          required:
            - price_percentage_change_24h
        volume_24h:
          type: string
          example: '1908432'
          description: The trading volume for the product in the last 24 hours.
          required:
            - volume_24h
        volume_percentage_change_24h:
          type: string
          example: 9.43%
          description: >-
            The amount the volume of the product has changed, in percent, in the
            last 24 hours.
          required:
            - volume_percentage_change_24h
        base_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount base value can be increased or decreased at once.
          required:
            - base_increment
        quote_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount quote value can be increased or decreased at once.
          required:
            - quote_increment
        quote_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of quote currency.
          required:
            - quote_min_size
        quote_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of quote currency.
          required:
            - quote_max_size
        base_min_size:
          type: string
          example: '0.00000001'
          description: Minimum size that can be represented of base currency.
          required:
            - base_min_size
        base_max_size:
          type: string
          example: '1000'
          description: Maximum size that can be represented of base currency.
          required:
            - base_max_size
        base_name:
          type: string
          example: Bitcoin
          description: Name of the base currency.
          required:
            - base_name
        quote_name:
          type: string
          example: US Dollar
          description: Name of the quote currency.
          required:
            - quote_name
        watched:
          type: boolean
          example: true
          description: Whether or not the product is on the user's watchlist.
          required:
            - watched
        is_disabled:
          type: boolean
          example: false
          description: Whether or not the product is disabled for trading.
          required:
            - is_disabled
        new:
          type: boolean
          example: true
          description: Whether or not the product is 'new'.
          required:
            - new
        status:
          type: string
          description: Status of the product.
          required:
            - status
        cancel_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be cancelled, not
            placed or edited.
          required:
            - cancel_only
        limit_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be limit orders, not
            market orders.
          required:
            - limit_only
        post_only:
          type: boolean
          example: true
          description: >-
            Whether or not orders of the product can only be posted, not
            cancelled.
          required:
            - post_only
        trading_disabled:
          type: boolean
          example: false
          description: >-
            Whether or not the product is disabled for trading for all market
            participants.
          required:
            - trading_disabled
        auction_mode:
          type: boolean
          example: true
          description: Whether or not the product is in auction mode.
          required:
            - auction_mode
        product_type:
          description: Type of the product.
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductType
        quote_currency_id:
          type: string
          example: USD
          description: Symbol of the quote currency.
        base_currency_id:
          type: string
          example: BTC
          description: Symbol of the base currency.
        fcm_trading_session_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails
        mid_market_price:
          type: string
          example: '140.22'
          description: The current midpoint of the bid-ask spread, in quote currency.
        alias:
          type: string
          example: BTC-USD
          description: Product id for the corresponding unified book.
        alias_to:
          type: array
          example:
            - BTC-USDC
          items:
            type: string
          description: Product ids that this product serves as an alias for.
        base_display_symbol:
          type: string
          example: BTC
          description: Symbol of the base display currency.
          required:
            - base_display_symbol
        quote_display_symbol:
          type: string
          example: USD
          description: Symbol of the quote display currency.
          required:
            - quote_display_symbol
        view_only:
          type: boolean
          example: true
          description: >-
            Reflects whether an FCM product has expired. For SPOT, set
            get_tradability_status to get a return value here. Defaulted to
            false for all other product types.
        price_increment:
          type: string
          example: '0.00000001'
          description: Minimum amount price can be increased or decreased at once.
        display_name:
          type: string
          example: BTC PERP
          description: Display name for the product e.g. BTC-PERP-INTX => BTC PERP
        product_venue:
          example: neptune
          description: >-
            The sole venue id for the product. Defaults to CBE if the product is
            not specific to a single venue
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ProductVenue
        approximate_quote_24h_volume:
          type: string
          example: '1908432'
          description: >-
            The approximate trading volume for the product in the last 24 hours
            based on the current quote.
        new_at:
          type: string
          format: RFC3339 Timestamp
          example: '2021-07-01T00:00:00.000Z'
          description: >-
            The timestamp when the product was listed. This is only populated if
            product has new tag.
        market_cap:
          type: string
          example: '1500000000000'
          description: The market capitalization of the product's base asset.
        icon_color:
          type: string
          example: red
          description: color for icon display
        icon_url:
          type: string
          example: https://metadata.cbhq.net/equity_icons/123456789.png
          description: A URL to the icon image.
        display_name_overwrite:
          type: string
          example: Bitcoin Perpetual
          description: An alternative name to display for the product.
        is_alpha_testing:
          type: boolean
          example: false
          description: flag for alpha user testing
        about_description:
          type: string
          example: >-
            nano Crude Oil Futures is a monthly cash-settled contract that
            allows participants to manage risk, trade on margin, or speculate on
            the price of oil.
          description: description used in about section for an asset
        future_product_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails
      title: Get Products
      required:
        - product_id
        - price
        - volume_24h
        - price_percentage_change_24h
        - volume_percentage_change_24h
        - base_increment
        - quote_increment
        - quote_min_size
        - quote_max_size
        - base_min_size
        - base_max_size
        - base_name
        - quote_name
        - watched
        - is_disabled
        - new
        - status
        - cancel_only
        - limit_only
        - post_only
        - trading_disabled
        - auction_mode
        - base_display_symbol
        - quote_display_symbol
    coinbase.public_api.authed.retail_brokerage_api.PaginationMetadata:
      type: object
      properties:
        prev_cursor:
          type: string
        next_cursor:
          type: string
        has_next:
          type: boolean
        has_prev:
          type: boolean
      description: Pagination metadata for paginated responses.
    google.protobuf.Any:
      type: object
      properties:
        type_url:
          type: string
          description: >-
            A URL/resource name that uniquely identifies the type of the
            serialized

            protocol buffer message. This string must contain at least

            one "/" character. The last segment of the URL's path must represent

            the fully qualified name of the type (as in

            `path/google.protobuf.Duration`). The name should be in a canonical
            form

            (e.g., leading "." is not accepted).


            In practice, teams usually precompile into the binary all types that
            they

            expect it to use in the context of Any. However, for URLs which use
            the

            scheme `http`, `https`, or no scheme, one can optionally set up a
            type

            server that maps type URLs to message definitions as follows:


            * If no scheme is provided, `https` is assumed.

            * An HTTP GET on the URL must yield a [google.protobuf.Type][]
              value in binary format, or produce an error.
            * Applications are allowed to cache lookup results based on the
              URL, or have them precompiled into a binary to avoid any
              lookup. Therefore, binary compatibility needs to be preserved
              on changes to types. (Use versioned type names to manage
              breaking changes.)

            Note: this functionality is not currently available in the official

            protobuf release, and it is not used for type URLs beginning with

            type.googleapis.com. As of May 2023, there are no widely used type
            server

            implementations and no plans to implement one.


            Schemes other than `http`, `https` (or the empty scheme) might be

            used with implementation specific semantics.
        value:
          type: string
          format: byte
          description: >-
            Must be a valid serialized protocol buffer of the above specified
            type.
      description: >-
        `Any` contains an arbitrary serialized protocol buffer message along
        with a

        URL that describes the type of the serialized message.


        Protobuf library provides support to pack/unpack Any values in the form

        of utility functions or additional generated methods of the Any type.


        Example 1: Pack and unpack a message in C++.

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }
            // or ...
            if (any.isSameTypeAs(Foo.getDefaultInstance())) {
              foo = any.unpack(Foo.getDefaultInstance());
            }

         Example 3: Pack and unpack a message in Python.

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

         Example 4: Pack and unpack a message in Go

             foo := &pb.Foo{...}
             any, err := anypb.New(foo)
             if err != nil {
               ...
             }
             ...
             foo := &pb.Foo{}
             if err := any.UnmarshalTo(foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use

        'type.googleapis.com/full.type.name' as the type URL and the unpack

        methods only use the fully qualified type name after the last '/'

        in the type URL, for example "foo.bar.com/x/y.z" will yield type

        name "y.z".


        JSON

        ====

        The JSON representation of an `Any` value uses the regular

        representation of the deserialized, embedded message, with an

        additional field `@type` which contains the type URL. Example:

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON

        representation, that representation will be embedded adding a field

        `value` which holds the custom JSON in addition to the `@type`

        field. Example (for message [google.protobuf.Duration][]):

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }
    coinbase.public_api.authed.retail_brokerage_api.ProductType:
      type: string
      enum:
        - UNKNOWN_PRODUCT_TYPE
        - SPOT
        - FUTURE
      default: UNKNOWN_PRODUCT_TYPE
      description: Defines the type of a product.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionDetails:
      type: object
      properties:
        is_session_open:
          type: boolean
        open_time:
          type: string
          format: RFC3339 Timestamp
        close_time:
          type: string
          format: RFC3339 Timestamp
        session_state:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState
        after_hours_order_entry_disabled:
          type: boolean
        closed_reason:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason
        maintenance:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance
    coinbase.public_api.authed.retail_brokerage_api.ProductVenue:
      type: string
      enum:
        - UNKNOWN_VENUE_TYPE
        - CBE
        - FCM
        - INTX
      default: UNKNOWN_VENUE_TYPE
      description: Defines the venue of a product.
    coinbase.public_api.authed.retail_brokerage_api.FutureProductDetails:
      type: object
      properties:
        venue:
          type: string
        contract_code:
          type: string
        contract_expiry:
          type: string
          format: RFC3339 Timestamp
        contract_size:
          type: string
        contract_root_unit:
          type: string
        group_description:
          type: string
        contract_expiry_timezone:
          type: string
        group_short_description:
          type: string
        risk_managed_by:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.RiskManagementType
        contract_expiry_type:
          description: The contract expiry type (e.g. 'EXPIRING').
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType
        perpetual_details:
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails
        contract_display_name:
          type: string
        time_to_expiry_ms:
          type: string
          format: int64
        non_crypto:
          type: boolean
        contract_expiry_name:
          type: string
        twenty_four_by_seven:
          type: boolean
        funding_interval:
          type: string
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        display_name:
          type: string
        region_enabled:
          type: object
          additionalProperties:
            type: boolean
        intraday_margin_rate:
          description: Margin rates during intraday trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        overnight_margin_rate:
          description: Margin rates during overnight trading hours
          allOf:
            - $ref: >-
                #/components/schemas/coinbase.public_api.authed.retail_brokerage_api.MarginRate
        settlement_price:
          type: string
          description: The most recent official settlement price for the futures contract
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionState:
      type: string
      enum:
        - FCM_TRADING_SESSION_STATE_UNDEFINED
        - FCM_TRADING_SESSION_STATE_PRE_OPEN
        - FCM_TRADING_SESSION_STATE_PRE_OPEN_NO_CANCEL
        - FCM_TRADING_SESSION_STATE_OPEN
        - FCM_TRADING_SESSION_STATE_CLOSE
      default: FCM_TRADING_SESSION_STATE_UNDEFINED
      description: Defines the state of a trading session.
    coinbase.public_api.authed.retail_brokerage_api.FcmTradingSessionClosedReason:
      type: string
      enum:
        - FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
        - FCM_TRADING_SESSION_CLOSED_REASON_REGULAR_MARKET_CLOSE
        - FCM_TRADING_SESSION_CLOSED_REASON_EXCHANGE_MAINTENANCE
        - FCM_TRADING_SESSION_CLOSED_REASON_VENDOR_MAINTENANCE
      default: FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED
      description: >-
        This helps distinguish between regular market close and downtimes due to
        maintenance.
    coinbase.public_api.authed.retail_brokerage_api.FcmScheduledMaintenance:
      type: object
      properties:
        start_time:
          type: string
          format: RFC3339 Timestamp
        end_time:
          type: string
          format: RFC3339 Timestamp
      description: Fcm specific scheduled maintenance details.
    coinbase.public_api.authed.retail_brokerage_api.RiskManagementType:
      type: string
      enum:
        - UNKNOWN_RISK_MANAGEMENT_TYPE
        - MANAGED_BY_FCM
        - MANAGED_BY_VENUE
      default: UNKNOWN_RISK_MANAGEMENT_TYPE
      description: Defines Risk management type.
    coinbase.public_api.authed.retail_brokerage_api.ContractExpiryType:
      type: string
      enum:
        - UNKNOWN_CONTRACT_EXPIRY_TYPE
        - EXPIRING
        - PERPETUAL
      default: UNKNOWN_CONTRACT_EXPIRY_TYPE
      description: Represents the types of contract expiry.
    coinbase.public_api.authed.retail_brokerage_api.PerpetualProductDetails:
      type: object
      properties:
        open_interest:
          type: string
        funding_rate:
          type: string
        funding_time:
          type: string
          format: RFC3339 Timestamp
        max_leverage:
          type: string
        base_asset_uuid:
          type: string
        underlying_type:
          type: string
    coinbase.public_api.authed.retail_brokerage_api.MarginRate:
      type: object
      properties:
        long_margin_rate:
          type: string
          example: '0.5'
          description: Long margin rate
        short_margin_rate:
          type: string
          example: '0.5'
          description: Short margin rate
      title: Margin rate information for futures products
  securitySchemes:
    apiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        A JWT signed using your CDP API Key Secret, encoded in base64. Refer to
        the [Creating API
        Keys](/coinbase-app/authentication-authorization/api-key-authentication)
        section of our Coinbase App Authentication docs for information on how
        to generate your Bearer Token.

````



