# Deribit API Documentation

Auto-fetched from 8 page(s)


---

# Source: https://docs.deribit.com/

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Introduction

Welcome to Deribit API

[Overview](/)[API Reference](/articles/json-rpc-overview)

##### Introduction

  * [Welcome to Deribit API](/)
  * [Quickstart Guide](/articles/deribit-quickstart)



##### Authentication

  * [Creating new API key](/articles/creating-api-key)
  * [Authentication](/articles/authentication)
  * [Access Scope](/articles/access-scope)
  * [Security Keys](/articles/security-keys)



##### Technical Information

  * [API Usage Policy](/articles/api-usage-policy)
  * [Rate Limits](/articles/rate-limits)



##### Best Practices

  * [Connection Management](/articles/connection-management-best-practices)
  * [Market Data Collection](/articles/market-data-collection-best-practices)
  * [Order Management](/articles/order-management-best-practices)



##### Guides

  * [Managing Deposits](/articles/managing-deposits-api)
  * [Managing Transfers](/articles/managing-transfers-api)
  * [Managing Subaccounts](/articles/managing-subaccounts-api)
  * [Managing Withdrawals](/articles/managing-withdrawals-api)
  * [Moving Positions](/articles/moving-positions-api)
  * [Block Trading](/articles/block-trading-api)
  * [Asymmetric API Keys](/articles/asymmetric-api-keys)
  * [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection)
  * [Accessing Historical Trades and Orders Using API](/articles/accessing-historical-trades-orders)
  * [Deribit Block RFQ API Walkthrough](/articles/block-rfq-api-walkthrough)
  * [Mass Quotes Specifications](/articles/mass-quotes-specifications)



On this page

  * [API Interfaces](#api-interfaces)
  * [Get Started](#get-started)
  * [Core Concepts](#core-concepts)
  * [Environments](#environments)
  * [Need Help?](#need-help)



Introduction

# Welcome to Deribit API

Copy page

Deribit is a leading cryptocurrency derivatives exchange offering futures, perpetuals, and options trading. This documentation provides everything you need to integrate with our API and build powerful trading applications.

Copy page

Two versions of the API documentation are available. You can switch between them using the version selector button at the top of the page. Changes in the upcoming version will be available in the production version after the next release. For release notes and information about upcoming releases, visit the [Releases section](https://support.deribit.com/hc/en-us/sections/25944734788637-Releases).

## 

[​](#api-interfaces)

API Interfaces

Deribit provides three different interfaces to access the API:

## [JSON-RPC over WebSocketReal-time, bidirectional communication. Recommended for most use cases.](/articles/json-rpc-overview#websocket-preferred)## [JSON-RPC over HTTPSimple REST-like interface for HTTP requests.](/articles/json-rpc-overview#http-rest)## [FIX APIFinancial Information eXchange protocol for institutional trading.](/fix-api/production/overview)

## 

[​](#get-started)

Get Started

## [Quickstart GuideGet up and running in minutes with our step-by-step quickstart guide. Make your first API call and start building.](/articles/deribit-quickstart)

## 

[​](#core-concepts)

Core Concepts

## [AuthenticationLearn how to create and manage API keys, and authenticate your requests.](/articles/creating-api-key)## [Rate LimitsUnderstand rate limits, credit system, and how to optimize API usage.](/articles/rate-limits)## [Access ScopesLearn about API permissions and access scopes for controlling what operations your API keys can perform.](/articles/access-scope)## [NotificationsSubscribe to real-time market data and account updates.](/articles/notifications)## [Error CodesReference guide for all API error codes and error handling.](/articles/errors)## [API ConsoleInteractive API testing tool for exploring and testing API methods.](https://test.deribit.com/api_console/)

## 

[​](#environments)

Environments

Deribit provides separate test and production environments. All examples in this documentation use the test environment (`test.deribit.com`). Test and production require separate accounts and API keys.

## [Test Environment**Purpose:** Development and testing**HTTP Endpoint:** `https://test.deribit.com/api/v2`**WebSocket Endpoint:** `wss://test.deribit.com/ws/api/v2`**Links:**

  * [Platform](https://test.deribit.com)
  * [API Console](https://test.deribit.com/api_console/)
  * [API Management](https://test.deribit.com/account/BTC/api)

](https://test.deribit.com/dashboard)## [Production Environment**Purpose:** Live trading**HTTP Endpoint:** `https://www.deribit.com/api/v2`**WebSocket Endpoint:** `wss://www.deribit.com/ws/api/v2`**Links:**

  * [Platform](https://www.deribit.com)
  * [API Console](https://www.deribit.com/api_console/)
  * [API Management](https://www.deribit.com/account/BTC/api)

](https://www.deribit.com/)

## 

[​](#need-help)

Need Help?

## [Support CenterBrowse help articles and documentation.](https://support.deribit.com)## [Contact UsGet technical support, API assistance, or report bugs. Available via Telegram, email, or support portal.](https://insights.deribit.com/contact-us/)

Was this page helpful?

YesNo

[Quickstart Guide](/articles/deribit-quickstart)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/json-rpc-overview

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Methods overview

JSON-RPC 2.0 Protocol

[Overview](/)[API Reference](/articles/json-rpc-overview)

JSON-RPC API

##### Methods overview

  * [JSON-RPC 2.0 Protocol](/articles/json-rpc-overview)
  * [Error Codes](/articles/errors)



##### Methods

  * Authentication

  * Account Management

  * Block RFQ

  * Block Trade

  * Combo Books

  * Market Data

  * Session Management

  * Subscription Management

  * Supporting

  * Trading

  * Wallet




On this page

  * [What is JSON-RPC?](#what-is-json-rpc)
  * [Request Format](#request-format)
  * [Basic Structure](#basic-structure)
  * [Field Specifications](#field-specifications)
  * [Request ID Management](#request-id-management)
  * [Parameter Validation](#parameter-validation)
  * [HTTP REST Requests](#http-rest-requests)
  * [Authenticated Requests](#authenticated-requests)
  * [Response Format](#response-format)
  * [Success Response](#success-response)
  * [Error Response](#error-response)
  * [Response Fields](#response-fields)
  * [Error Object](#error-object)
  * [Conditional Response Formats](#conditional-response-formats)
  * [Detailed Response for Cancel Methods](#detailed-response-for-cancel-methods)
  * [Transport Protocols](#transport-protocols)
  * [WebSocket (Preferred)](#websocket-preferred)
  * [HTTP REST](#http-rest)
  * [Notification Messages](#notification-messages)
  * [Notification Format](#notification-format)
  * [Connection Management](#connection-management)
  * [Connection Limits](#connection-limits)
  * [Session vs Connection Scope](#session-vs-connection-scope)
  * [Instrument Naming](#instrument-naming)
  * [Best Practices](#best-practices)
  * [1\. Use unique request IDs](#1-use-unique-request-ids)
  * [2\. Handle errors appropriately](#2-handle-errors-appropriately)
  * [3\. Monitor timing fields](#3-monitor-timing-fields)
  * [4\. Use WebSocket for production systems](#4-use-websocket-for-production-systems)
  * [5\. Use HTTP for simple operations](#5-use-http-for-simple-operations)
  * [6\. Implement connection pooling (HTTP)](#6-implement-connection-pooling-http)
  * [7\. Optimize WebSocket usage](#7-optimize-websocket-usage)
  * [8\. Manage subscriptions efficiently](#8-manage-subscriptions-efficiently)
  * [9\. Implement robust error handling](#9-implement-robust-error-handling)
  * [10\. Handle reconnections gracefully](#10-handle-reconnections-gracefully)
  * [11\. Secure credential management](#11-secure-credential-management)
  * [12\. Validate all inputs](#12-validate-all-inputs)



Methods overview

# JSON-RPC 2.0 Protocol

Copy page

Deribit API uses JSON-RPC 2.0 for all API communications. This standardized protocol provides a simple and consistent way to make remote procedure calls.

Copy page

## 

[​](#what-is-json-rpc)

What is JSON-RPC?

JSON-RPC is a stateless, light-weight remote procedure call (RPC) protocol that uses JSON (RFC 7159) for data encoding. The Deribit API implements JSON-RPC 2.0 specification with specific extensions and limitations. **Key features** :

  * Simple request/response model with bidirectional communication support
  * Standardized error handling with structured error objects
  * Transport-agnostic design (HTTP, WebSocket, etc.)
  * Stateless protocol (each request is independent)
  * Type-safe parameter passing via named parameters only



**JSON-RPC 2.0 Feature Limitations** :The following JSON-RPC 2.0 specification features are **not supported** by the Deribit API:

  * **Positional parameters** : Only named parameters (object properties) are accepted
  * **Batch requests** : Each request must be sent individually; batching multiple requests in a single message is not supported
  * **Notifications as requests** : While the server sends notification messages (subscriptions), clients cannot send notification-style requests (requests without `id` field are rejected)

Attempting to use unsupported features will result in error responses with appropriate error codes.

WebSocket is the preferred transport mechanism because it’s faster, supports bidirectional communication, and enables real-time subscriptions. HTTP has fundamental limitations: subscriptions and cancel on disconnect are not supported due to HTTP’s request-response model.

## 

[​](#request-format)

Request Format

### 

[​](#basic-structure)

Basic Structure

All requests must conform to the JSON-RPC 2.0 request structure:

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "method": "public/get_instruments",
      "params": {
        "currency": "BTC",
        "kind": "future"
      },
      "id": 42
    }
    

### 

[​](#field-specifications)

Field Specifications

Field| Type| Required| Description  
---|---|---|---  
`jsonrpc`| string| Yes| JSON-RPC protocol version. Must be exactly `"2.0"`  
`method`| string| Yes| Method to be invoked. Format: `{scope}/{method_name}` (e.g., `public/get_time`, `private/buy`). Must match an available API method exactly  
`params`| object| Conditional| Parameter values for the method. Must be an object with named properties. Field names must match expected parameter names exactly (case-sensitive). Can be omitted if method requires no parameters  
`id`| integer|string| Yes| Request identifier. Must be unique within the connection context. The response will contain the same identifier. For WebSocket connections, use a monotonically increasing integer or UUID to ensure proper request/response correlation  
  
### 

[​](#request-id-management)

Request ID Management

**Critical for WebSocket connections** : Since WebSocket is full-duplex and responses may arrive out of order, proper request ID management is essential:

  * **Use unique IDs** : Each request must have a unique identifier within the connection lifetime
  * **Monotonically increasing integers** : Recommended pattern: start at 1, increment for each request
  * **UUIDs** : Alternative for distributed systems where multiple clients may share connection pools
  * **Store pending requests** : Maintain a map of `request_id -> callback/promise` to route responses correctly



### 

[​](#parameter-validation)

Parameter Validation

  * **Named parameters only** : All parameters must be passed as object properties
  * **Case-sensitive** : Parameter names are case-sensitive (`currency` ≠ `Currency`)
  * **Type validation** : Parameters are validated server-side; incorrect types will result in error responses
  * **Optional parameters** : Omit optional parameters entirely rather than passing `null` or empty values



### 

[​](#http-rest-requests)

HTTP REST Requests

**Endpoint** : `https://www.deribit.com/api/v2/{method}` (production)  
**Endpoint** : `https://test.deribit.com/api/v2/{method}` (test environment) **Technical Specifications** :

  * **HTTP Methods** : Both GET and POST are supported
  * **Content-Type** : `application/json` required when sending JSON-RPC in request body
  * **Parameter Passing** :
    * **GET** : Parameters can be passed as URL query string (URL-encoded) or in request body as JSON-RPC
    * **POST** : Parameters passed in request body as JSON-RPC
  * **Connection Lifetime** : Each HTTP connection expires after 15 minutes of inactivity
  * **Keep-Alive** : HTTP/1.1 keep-alive is supported but connections are terminated after 15 minutes regardless



  * GET (Query String)

  * GET (JSON-RPC Body)

  * POST




Report incorrect code

Copy

Ask AI
    
    
    curl "https://www.deribit.com/api/v2/public/get_instruments?currency=BTC&kind=future"
    

Report incorrect code

Copy

Ask AI
    
    
    curl -X GET "https://www.deribit.com/api/v2/public/get_instruments" \
      -H "Content-Type: application/json" \
      -d '{
        "jsonrpc": "2.0",
        "method": "public/get_instruments",
        "params": {
          "currency": "BTC",
          "kind": "future"
        },
        "id": 42
      }'
    

Report incorrect code

Copy

Ask AI
    
    
    curl -X POST "https://www.deribit.com/api/v2/public/get_instruments" \
      -H "Content-Type: application/json" \
      -d '{
        "jsonrpc": "2.0",
        "method": "public/get_instruments",
        "params": {
          "currency": "BTC",
          "kind": "future"
        },
        "id": 42
      }'
    

### 

[​](#authenticated-requests)

Authenticated Requests

For private methods, authentication is required. The mechanism differs by transport.

## [Authentication GuideComprehensive guide to OAuth 2.0 authentication, token management, and security best practices.](/articles/authentication)## [Connection ManagementLearn about connection scopes, session management, and connection limits.](/articles/connection-management-best-practices)

## 

[​](#response-format)

Response Format

### 

[​](#success-response)

Success Response

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "id": 42,
      "result": [
        {
          "tick_size": 2.5,
          "tick_size_steps": [],
          "taker_commission": 0.0005,
          "settlement_period": "month",
          "settlement_currency": "BTC",
          "quote_currency": "USD",
          "price_index": "btc_usd",
          "min_trade_amount": 10,
          "max_liquidation_commission": 0.0075,
          "max_leverage": 50,
          "maker_commission": 0,
          "kind": "future",
          "is_active": true,
          "instrument_name": "BTC-29SEP23",
          "instrument_id": 138583,
          "instrument_type": "reversed",
          "expiration_timestamp": 1695974400000,
          "creation_timestamp": 1664524802000,
          "counter_currency": "USD",
          "contract_size": 10,
          "block_trade_tick_size": 0.01,
          "block_trade_min_trade_amount": 200000,
          "block_trade_commission": 0.00025,
          "base_currency": "BTC"
        },
        {
          "tick_size": 0.5,
          "tick_size_steps": [],
          "taker_commission": 0.0005,
          "settlement_period": "perpetual",
          "settlement_currency": "BTC",
          "quote_currency": "USD",
          "price_index": "btc_usd",
          "min_trade_amount": 10,
          "max_liquidation_commission": 0.0075,
          "max_leverage": 50,
          "maker_commission": 0,
          "kind": "future",
          "is_active": true,
          "instrument_name": "BTC-PERPETUAL",
          "instrument_id": 124972,
          "instrument_type": "reversed",
          "expiration_timestamp": 32503708800000,
          "creation_timestamp": 1534167754000,
          "counter_currency": "USD",
          "contract_size": 10,
          "block_trade_tick_size": 0.01,
          "block_trade_min_trade_amount": 200000,
          "block_trade_commission": 0.00025,
          "base_currency": "BTC"
        }
      ]
    }
    

### 

[​](#error-response)

Error Response

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "id": 8163,
      "error": {
        "code": 11050,
        "message": "bad_request"
      },
      "testnet": false,
      "usIn": 1535037392434763,
      "usOut": 1535037392448119,
      "usDiff": 13356
    }
    

### 

[​](#response-fields)

Response Fields

Field| Type| Required| Description  
---|---|---|---  
`jsonrpc`| string| Yes| Always `"2.0"`  
`id`| integer|string| Yes| Same `id` that was sent in the request. Used to correlate responses with requests  
`result`| any| Conditional| Present only if request succeeded. Type and structure depend on the method called  
`error`| object| Conditional| Present only if request failed. Mutually exclusive with `result`  
`testnet`| boolean| Yes| `false` for production environment, `true` for test environment  
`usIn`| integer| Yes| Timestamp when request was received (microseconds since Unix epoch, UTC)  
`usOut`| integer| Yes| Timestamp when response was sent (microseconds since Unix epoch, UTC)  
`usDiff`| integer| Yes| Server-side processing time in microseconds (`usOut - usIn`)  
  
**Response Guarantees** :

  * Every request with a valid `id` will receive exactly one response
  * Responses maintain the same `id` as the request for correlation
  * `result` and `error` are mutually exclusive (never both present)



The fields `testnet`, `usIn`, `usOut`, and `usDiff` are **Deribit-specific extensions** to the JSON-RPC 2.0 specification. They are provided for:

  * **Environment identification** : Determine if response came from test or production
  * **Performance monitoring** : Calculate round-trip time and server processing time
  * **Latency analysis** : `usDiff` shows server-side processing time; compare with total RTT to identify network latency



### 

[​](#error-object)

Error Object

When an error occurs, the response contains an `error` object conforming to JSON-RPC 2.0 specification:

Field| Type| Required| Description  
---|---|---|---  
`code`| integer| Yes| Numeric error code indicating the error type. Negative codes are JSON-RPC standard errors; positive codes are Deribit-specific errors  
`message`| string| Yes| Human-readable error message. For standard JSON-RPC errors, matches specification messages  
`data`| any| No| Additional error context. May contain structured data, error details, or method-specific error information  
  
See [Error Codes](/articles/errors) for a complete list of error codes and handling strategies.

### 

[​](#conditional-response-formats)

Conditional Response Formats

Certain methods support a `detailed` boolean parameter that modifies the response structure. When `detailed=true`, the response format changes from a simple count to a comprehensive list of execution reports.

#### 

[​](#detailed-response-for-cancel-methods)

Detailed Response for Cancel Methods

The following methods support the `detailed` parameter:

  * [`private/cancel_all`](/api-reference/trading/private-cancel_all) \- Cancel all orders across all currencies and instrument kinds
  * [`private/cancel_all_by_currency`](/api-reference/trading/private-cancel_all_by_currency) \- Cancel all orders by currency
  * [`private/cancel_all_by_currency_pair`](/api-reference/trading/private-cancel_all_by_currency_pair) \- Cancel all orders by currency pair
  * [`private/cancel_all_by_instrument`](/api-reference/trading/private-cancel_all_by_instrument) \- Cancel all orders by instrument
  * [`private/cancel_all_by_kind_or_type`](/api-reference/trading/private-cancel_all_by_kind_or_type) \- Cancel all orders by kind or type
  * [`private/cancel_by_label`](/api-reference/trading/private-cancel_by_label) \- Cancel orders by label

**Default Behavior** (`detailed=false`):

  * Returns a single integer representing the total count of cancelled orders
  * Response format: `{ "jsonrpc": "2.0", "result": 5, "id": 42 }`

**Detailed Response** (`detailed=true`):

  * Returns an array of execution report objects
  * Each execution report corresponds to a separate internal cancellation request
  * Provides granular information about successful and failed cancellations per currency, order type, and instrument
  * Response format: `{ "jsonrpc": "2.0", "result": [{...}, {...}], "id": 42 }`

**Technical Implementation Details** : Internally, `cancel_all*` methods decompose the cancellation request into multiple sub-requests, each targeting a specific combination of:

  * Currency (e.g., BTC, ETH)
  * Order type (e.g., limit, stop)
  * Instrument book

When `detailed=true`, the response aggregates execution reports from all sub-requests, allowing clients to:

  * Identify which specific currency/type combinations succeeded or failed
  * Handle partial failures gracefully
  * Debug cancellation issues at a granular level
  * Track cancellation results per instrument or currency

**Example Usage** :

Report incorrect code

Copy

Ask AI
    
    
    // Request with detailed=true
    {
      "jsonrpc": "2.0",
      "method": "private/cancel_all",
      "params": {
        "detailed": true
      },
      "id": 42
    }
    
    // Response with detailed execution reports
    {
      "jsonrpc": "2.0",
      "id": 42,
      "result": [
        {
          "order": {
            "order_id": "12345678",
            "instrument_name": "BTC-PERPETUAL",
            "order_state": "cancelled",
            // ... full order details
          }
        },
        {
          "order": {
            "order_id": "87654321",
            "instrument_name": "ETH-PERPETUAL",
            "order_state": "cancelled",
            // ... full order details
          }
        }
        // ... additional execution reports for each currency/type combination
      ]
    }
    

**Performance Considerations** :

  * `detailed=true` increases response payload size significantly
  * Processing time may be slightly higher due to aggregation overhead
  * Use `detailed=false` (default) when only the cancellation count is needed
  * Use `detailed=true` when granular cancellation tracking is required for error handling or auditing



## 

[​](#transport-protocols)

Transport Protocols

### 

[​](#websocket-preferred)

WebSocket (Preferred)

**Endpoints** :

  * **Production** : `wss://www.deribit.com/ws/api/v2`
  * **Test Environment** : `wss://test.deribit.com/ws/api/v2`

**Technical Specifications** :

  * **Protocol** : WebSocket (RFC 6455) over TLS (WSS)
  * **Subprotocol** : None required
  * **Frame Format** : Text frames (UTF-8 encoded JSON)
  * **Message Format** : Each WebSocket message contains a single JSON-RPC request or response
  * **Connection Limits** : Maximum 32 connections per IP address
  * **Session Limits** : Maximum 16 sessions per API key

**Advantages** :

  * **Bidirectional Communication** : Full-duplex connection enables server-to-client notifications
  * **Lower Latency** : Persistent connection eliminates HTTP handshake overhead
  * **Real-time Subscriptions** : Supports subscription channels for live market data
  * **Cancel on Disconnect** : Automatic order cancellation on connection loss (when enabled)
  * **Session Persistence** : Session-scoped authentication persists across reconnections
  * **Higher Rate Limits** : Authenticated WebSocket connections have higher rate limits than HTTP

**Connection Lifecycle** :

  1. **Establish Connection** : Open WebSocket connection to endpoint
  2. **Authenticate** : Send `public/auth` request with credentials
  3. **Maintain Connection** : Keep connection alive with heartbeat/ping if needed
  4. **Handle Reconnection** : Implement reconnection logic with exponential backoff
  5. **Re-authenticate** : Re-authenticate and re-subscribe after reconnection

**Message Handling** :

  * **Request/Response Correlation** : Use `id` field to match responses to requests
  * **Notification Messages** : Handle server-initiated messages (method: `"subscription"`) without `id` field
  * **Message Ordering** : Responses may arrive out of order; use `id` for correlation
  * **Backpressure** : If client cannot process messages fast enough, connection may be terminated with `connection_too_slow` error



### 

[​](#http-rest)

HTTP REST

**Endpoints** :

  * **Production** : `https://www.deribit.com/api/v2/{method}`
  * **Test Environment** : `https://test.deribit.com/api/v2/{method}`

**Technical Specifications** :

  * **Protocol** : HTTP/1.1 or HTTP/2 over TLS (HTTPS)
  * **Methods** : GET and POST supported
  * **Content-Type** : `application/json` for POST requests
  * **Connection Lifetime** : 15 minutes maximum per connection
  * **Keep-Alive** : Supported but connections expire after 15 minutes regardless

**Limitations** :

  * **No Subscriptions** : HTTP’s request-response model cannot support server-initiated messages
  * **No Cancel on Disconnect** : No persistent connection to monitor for disconnection events
  * **Higher Latency** : Each request requires TCP/TLS handshake (unless connection pooling/reuse)
  * **Lower Rate Limits** : Unauthenticated HTTP requests have stricter rate limits
  * **No Session Persistence** : Each request is independent; no connection state

**Use Cases for HTTP** :

  * One-off data retrieval
  * Simple scripts and automation
  * Environments where WebSocket is not available
  * Testing and debugging



**HTTP Limitations** :

  * Subscriptions are **not supported** via HTTP. Use WebSocket for any subscription-based functionality.
  * Cancel on disconnect is **not supported** via HTTP. This feature requires a persistent WebSocket connection.
  * For production trading systems, WebSocket is strongly recommended for lower latency and real-time capabilities.



## 

[​](#notification-messages)

Notification Messages

JSON-RPC 2.0 defines notification messages as requests without an `id` field. Deribit uses this mechanism for server-to-client subscription updates.

### 

[​](#notification-format)

Notification Format

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "method": "subscription",
      "params": {
        "channel": "deribit_price_index.btc_usd",
        "data": {
          "timestamp": 1535098298227,
          "price": 6521.17,
          "index_name": "btc_usd"
        }
      }
    }
    

**Key Characteristics** :

  * **No`id` field**: Notifications do not include an `id` field (per JSON-RPC 2.0 spec)
  * **Method** : Always `"subscription"` for Deribit notifications
  * **Params Structure** : Always contains `channel` (string) and `data` (any) fields
  * **One-way Communication** : Notifications are server-initiated; no response expected

**Technical Considerations** :

  * **Message Ordering** : Notifications are sent in order per channel, but different channels may interleave
  * **Backpressure** : If client cannot process notifications fast enough, connection may be terminated
  * **Reconnection** : After reconnection, re-subscribe to channels; first notification per channel is typically a full snapshot

See [Notifications](/articles/notifications) for detailed information about subscription channels and notification handling.

## 

[​](#connection-management)

Connection Management

### 

[​](#connection-limits)

Connection Limits

  * **Per IP** : Maximum 32 simultaneous connections (HTTP + WebSocket combined)
  * **Per API Key** : Maximum 16 active sessions
  * **Per Account** : Maximum 20 subaccounts

**Connection Counting** :

  * Each HTTP request creates a temporary connection
  * Each WebSocket connection counts as one persistent connection
  * Both connection-scoped and session-scoped connections count toward limits



### 

[​](#session-vs-connection-scope)

Session vs Connection Scope

**Connection Scope** (default):

  * Token valid only for the specific connection
  * Token invalidated when connection closes
  * Must re-authenticate on reconnection
  * Does not count against session limit

**Session Scope** :

  * Token valid across multiple connections
  * Specify `session:name` in authentication request
  * Token persists until session expires or is invalidated
  * Counts against 16-session limit per API key
  * Subsequent requests on same connection can omit token

See [Connection Management Best Practices](/articles/connection-management-best-practices) for detailed guidance.

## 

[​](#instrument-naming)

Instrument Naming

Deribit tradeable assets or instruments use the following system of naming:

Kind| Examples| Template| Comments  
---|---|---|---  
Future| `BTC-25MAR23`, `BTC-5AUG23`| `BTC-DMMMYY`| `BTC` is currency, `DMMMYY` is expiration date, `D` stands for day of month (1 or 2 digits), `MMM` \- month (3 first letters in English), `YY` stands for year.  
Perpetual| `BTC-PERPETUAL`|  _(empty)_|  Perpetual contract for currency `BTC`.  
Option| `BTC-25MAR23-420-C`, `BTC-5AUG23-580-P`| `BTC-DMMMYY-STRIKE-K`| `STRIKE` is option strike price in USD. Template `K` is option kind: `C` for call options or `P` for put options. **In Linear Options`d` is used as a decimal point for decimal strikes.** **Example:** For `XRP_USDC-30JUN23-0d625-C` strike is 0.625.  
  
## 

[​](#best-practices)

Best Practices

1

[](#)

Request/Response Handling

#### 

[​](#1-use-unique-request-ids)

1\. Use unique request IDs

  * **Critical for WebSocket** : Responses may arrive out of order
  * Use monotonically increasing integers or UUIDs
  * Maintain a map of pending requests for correlation
  * Implement request timeouts (recommended: 30 seconds)



#### 

[​](#2-handle-errors-appropriately)

2\. Handle errors appropriately

  * Always check for `error` field in responses
  * Distinguish between JSON-RPC protocol errors and application errors
  * Implement retry logic for transient errors (rate limits, timeouts)
  * Log error details including `error.data` for debugging



#### 

[​](#3-monitor-timing-fields)

3\. Monitor timing fields

  * Track `usDiff` to identify slow server processing
  * Calculate total RTT: `(current_time - request_time) * 1000000` microseconds
  * Network latency = Total RTT - `usDiff`
  * Alert on high latency or processing times



2

[](#)

Transport Selection

#### 

[​](#4-use-websocket-for-production-systems)

4\. Use WebSocket for production systems

  * Lower latency for trading operations
  * Required for subscriptions and real-time data
  * Supports cancel on disconnect
  * Higher rate limits for authenticated connections



#### 

[​](#5-use-http-for-simple-operations)

5\. Use HTTP for simple operations

  * One-off data retrieval
  * Scripts and automation
  * Testing and debugging
  * When WebSocket is not available



3

[](#)

Performance Optimization

#### 

[​](#6-implement-connection-pooling-http)

6\. Implement connection pooling (HTTP)

  * Reuse connections when possible
  * Be aware of 15-minute connection expiration
  * Use HTTP/2 when available for multiplexing



#### 

[​](#7-optimize-websocket-usage)

7\. Optimize WebSocket usage

  * Keep connections alive and reuse them
  * Avoid connection churn (open/close repeatedly)
  * Implement exponential backoff for reconnections
  * Use session-scoped authentication to reduce token overhead



#### 

[​](#8-manage-subscriptions-efficiently)

8\. Manage subscriptions efficiently

  * Only subscribe to channels you need
  * Use aggregated intervals (`100ms`, `agg2`) when appropriate
  * Unsubscribe from unused channels
  * Monitor for `connection_too_slow` errors



4

[](#)

Error Handling & Reconnection

#### 

[​](#9-implement-robust-error-handling)

9\. Implement robust error handling

  * Handle rate limit errors (10028) with backoff
  * Detect and handle connection failures
  * Implement circuit breakers for repeated failures
  * Log errors with context for debugging



#### 

[​](#10-handle-reconnections-gracefully)

10\. Handle reconnections gracefully

  * Re-authenticate after reconnection
  * Re-subscribe to all active channels
  * Handle missed messages (use `change_id` for order books)
  * Maintain state across reconnections



5

[](#)

Security

#### 

[​](#11-secure-credential-management)

11\. Secure credential management

  * Never expose API keys or secrets in client-side code
  * Use environment variables or secure key stores
  * Rotate credentials regularly
  * Implement proper token refresh logic



#### 

[​](#12-validate-all-inputs)

12\. Validate all inputs

  * Validate parameters before sending requests
  * Handle unexpected response structures
  * Sanitize user inputs to prevent injection attacks



Was this page helpful?

YesNo

[Error Codes](/articles/errors)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/rate-limits

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Technical Information

Rate Limits

[Overview](/)[API Reference](/articles/json-rpc-overview)

##### Introduction

  * [Welcome to Deribit API](/)
  * [Quickstart Guide](/articles/deribit-quickstart)



##### Authentication

  * [Creating new API key](/articles/creating-api-key)
  * [Authentication](/articles/authentication)
  * [Access Scope](/articles/access-scope)
  * [Security Keys](/articles/security-keys)



##### Technical Information

  * [API Usage Policy](/articles/api-usage-policy)
  * [Rate Limits](/articles/rate-limits)



##### Best Practices

  * [Connection Management](/articles/connection-management-best-practices)
  * [Market Data Collection](/articles/market-data-collection-best-practices)
  * [Order Management](/articles/order-management-best-practices)



##### Guides

  * [Managing Deposits](/articles/managing-deposits-api)
  * [Managing Transfers](/articles/managing-transfers-api)
  * [Managing Subaccounts](/articles/managing-subaccounts-api)
  * [Managing Withdrawals](/articles/managing-withdrawals-api)
  * [Moving Positions](/articles/moving-positions-api)
  * [Block Trading](/articles/block-trading-api)
  * [Asymmetric API Keys](/articles/asymmetric-api-keys)
  * [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection)
  * [Accessing Historical Trades and Orders Using API](/articles/accessing-historical-trades-orders)
  * [Deribit Block RFQ API Walkthrough](/articles/block-rfq-api-walkthrough)
  * [Mass Quotes Specifications](/articles/mass-quotes-specifications)



Technical Information

# Rate Limits

Copy page

To maintain fair and stable access to our API, Deribit uses a credit-based rate limiting system.

Copy page

[​](#undefined)

Exchange-Wide Compliance (OTV & API Usage Policy)All API traffic—whether authenticated or public—**must follow Deribit’s broader trading-integrity rules** , including the **Order-to-Volume (OTV) limits** and other anti-abuse protections. Violations can trigger immediate session disconnects, additional throttling, or stronger enforcement actions.For full guidelines, please review our [API Usage Policy](/hc/en-us/articles/25944617449373#UUID-56019658-17b2-b28e-ee98-3335977015d2) (which also covers OTV thresholds and other exchange-abuse rules).

This system ensures efficient use of platform resources while accommodating different trading volumes.

Rate limits described in this article **do not apply to Mass Quotes**. Mass Quotes follow their own dedicated rate-limiting rules, which are documented separately in the [Mass Quotes Specifications article](/articles/mass-quotes-specifications).

## 

[​](#credit-based-system)

Credit-Based System

Each API request consumes a certain number of credits. The refill rate and maximum credit pool for your sub-account depend on your trading activity and tier. **If a request arrives when no credits remain, we immediately send a`too_many_requests` (`code 10028`) or similar error and terminate the session.** After a disconnect, you must wait for credits to replenish and then re-establish a new connection before sending additional requests. Key elements of this system include:

### 

[​](#credit-refill)

Credit Refill

Credits are **replenished continuously at a fixed rate** , depending on your sub-account’s tier. This refill acts like a **leaky bucket** : each second, a certain number of credits “drip” back into your sub-account’s credit pool. You can think of this as a “credits per second” (CPS) refill rate.

Rate limits are applied [per sub-account](/hc/en-us/articles/25944616386973#UUID-038b9516-2490-c84d-c77a-c8e627bd7b18). Each sub-account has its own independent rate limit.

  * **Example** : If your refill rate is 20 credits/second, and each request costs 1 credit, you can sustainably send 20 requests per second without depleting your credits.
  * The refill continues **even when you’re not making requests** , allowing you to accumulate credits back up to your **maximum credit limit**.
  * If your maximum credit cap is 200 and your refill rate is 20 credits/sec, it will take 10 seconds to fully refill from 0 to 200.

This refill mechanism helps to:

  * Allow **burst activity** (e.g., submitting multiple orders at once), as long as it doesn’t exceed the maximum credit limit.
  * Encourage **consistent and predictable usage** , minimizing sudden surges that could strain the system.



### 

[​](#maximum-credits)

Maximum Credits

This is the **upper bound** of your available credit pool. You cannot accumulate more credits than this cap, regardless of how long you wait. It determines the size of request bursts you can make.

### 

[​](#cost-per-request)

Cost per Request

Using WebSocket subscriptions for real-time data reduces REST credit consumption.

[​](#undefined)

Methods with Non-Default Rate LimitsThe following methods have custom rate limits that differ from the standard non-matching engine defaults:

Method| Cost| Credits| Sustained Rate| Burst Capacity  
---|---|---|---|---  
[`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments)| 10,000| 500,000| 1 request/second| 50 requests  
[`public/subscribe`](https://docs.deribit.com/api-reference/subscription-management/public-subscribe) [`private/subscribe`](https://docs.deribit.com/api-reference/subscription-management/private-subscribe)| 3,000| 30,000| ~3.3 requests/second| 10 requests  
[`private/move_positions`](https://docs.deribit.com/api-reference/trading/private-move_positions)| 100,000| 600,000| 6 requests/minute| 6 requests  
[`private/get_transaction_log`](https://docs.deribit.com/api-reference/account-management/private-get_transaction_log)| 10,000| 80,000| 1 request/second| 8 requests  
  
These limits are enforced using the same credit-based system as other methods, but with different cost and credit pool configurations.

**Weekly Usage Limit for[`private/move_positions`](https://docs.deribit.com/api-reference/trading/private-move_positions)**: In addition to the per-minute rate limit, there is a limit of **100 move_position uses per week (168 hours)**.

[​](#undefined)

Webpage Usage Also Consumes API CreditsPlease note that using the [Deribit web platform](https://www.deribit.com/futures/BTC-PERPETUAL) also generates API requests behind the scenes. This means **browsing certain pages (e.g., order book, positions, account info)** can **consume credits from your API rate limit** , just like programmatic API calls.If you are running automated scripts or trading bots in parallel with an open Deribit web session, you may reach your credit limit more quickly than expected. When this happens, you may receive a `too_many_requests` error (code `10028`), even if your script appears to be within the expected request volume.To optimize performance:

  * **Avoid keeping multiple browser tabs open** on data-intensive pages.
  * Consider logging out of the web interface when running high-frequency strategies.
  * **Note** : If you customize a trading page by adding more components, that may affect the rate limit.



## 

[​](#matching-vs-non-matching-engine-requests)

Matching vs Non-Matching Engine Requests

There are two main categories of API requests:

  * **Matching engine requests** : These interact with the order book, such as placing or cancelling an order.
  * **Non-matching engine requests** : These involve general queries, such as retrieving account information or market data.

Each type of request consumes credits at a different rate.

### 

[​](#default-settings-for-non-matching-engine-requests)

Default Settings for Non-Matching Engine Requests

  * **Cost per Request** : 500 credits.
  * **Maximum Credits** : 50,000 credits.
  * **Refill Rate** : Credits are refilled at a rate that allows up to 20 requests per second (10,000 credits per second).
  * **Burst Capacity** : Allows up to 100 requests at once, considering the maximum credit pool.



#### 

[​](#burst-and-refill-example-non-matching-defaults)

Burst and Refill Example (non-matching defaults)

All rate-limit values in this example are illustrative only. They describe how the mechanism works and do not represent your actual limits.

  * The burst counter starts with **50,000 credits** (the maximum pool).
  * Each request costs **500 credits** ; 100 back-to-back requests would fully drain the pool if you ignore refills.
  * Credits **refill continuously** at **10 credits per millisecond** (10,000 per second) even while you are bursting.
  * If credits reach zero, new requests fail with `too_many_requests` (code `10028`).
  * Sustained traffic at **20 req/s** (20 × 500 = 10,000) matches the refill rate, so the pool stays stable. A rapid **100+ request burst** can still trigger `10028` if it outpaces the current credits.
  * If you hit `10028` and need to cancel orders, waiting ~**50 ms** restores ~**500 credits** (10 credits/ms), enough to send a mass-cancel.



### 

[​](#matching-engine-requests)

Matching Engine Requests

Each sub-account has an hourly updated rate limit, applicable across all books. Users can check their current rate limits via the [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) method.

Tier Level| 7-Day Trading Volume| Sustained Rate Limit (Requests/Second)| Burst Rate Limit| Description  
---|---|---|---|---  
Tier 1| Over USD 25 million| 30 requests/second| 100 requests (burst)| Suitable for high-volume traders, allowing up to 100 requests in a rapid burst or a steady rate of 30 requests per second.  
Tier 2| Over USD 5 million| 20 requests/second| 50 requests (burst)| Designed for medium-volume traders, permitting up to 50 requests in a burst or 20 requests per second.  
Tier 3| Over USD 1 million| 10 requests/second| 30 requests (burst)| Appropriate for active traders, enabling up to 30 requests in a burst or 10 requests per second.  
Tier 4| Up to USD 1 million| 5 requests/second| 20 requests (burst)| For regular traders, allowing up to 20 requests in a burst or a steady rate of 5 requests per second.  
  
### 

[​](#automatic-rate-limit-updates)

Automatic Rate Limit Updates

  * We recalculate limits **every hour**. There is no “volume/7 per day” delay—the most recent 7-day trading volume is evaluated each hour for every sub-account that has trading stats.
  * **Volume window** : the trailing **7-day** trading volume determines your tier. Each hourly recalculation uses the latest 7-day sum.
  * **Upgrades** : if your 7-day volume crosses a higher-tier threshold during an hourly check, we immediately move you to that tier (we can skip intermediate tiers; e.g., jumping from Tier 1 straight to Tier 4 is possible).
  * **Downgrades** : during an hourly check, if your 7-day volume falls below your current tier’s threshold after being above it in the prior hour, the limits are lowered accordingly. This can also skip tiers if the 7-day volume drops multiple thresholds.



[​](#undefined)

Public Access LimitationsPublic, **non-authorized** API requests are rate-limited on a **per-IP basis** —they do not draw from the sub-account-level credit pool. If an IP exceeds its public request allowance, subsequent calls may be **temporarily rejected** or the connection **disconnected** to protect platform stability.Whenever possible, use **authorized requests tied to your API key**. Authenticated traffic benefits from:

  * **Higher and more transparent limits** that scale with your sub-account’s tier.
  * **Client-ID visibility** , letting us distinguish heavy legitimate usage from abusive traffic—so rather than an immediate block, we can apply graduated safeguards if your limit is exceeded.

In short, authorized requests are always the safer, more reliable option for sustained or high-frequency access.

Production and [Testnet environment](/document/preview/12390#UUID-f5f86659-ba8b-6f75-5208-2f751bee1531) operate **on separate, independently-tracked rate-limit pools**. **Limits are not shared** between environments—exceeding Testnet limits will not affect your Production credits, and vice-versa.

## 

[​](#checking-current-rate-limits)

Checking current rate limits

Users can access the current rate limits by calling the [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) method and receiving `limits` field in response. The configuration of rate limits can be either on a per-currency basis or a default set applied globally across all currencies. Per-currency limits are not the default setting and are enabled only for specific clients upon request.

Per-currency rate limits currently are used **exclusively to decrease** access limits for specific currencies when needed. They are not applied to increase rate limits.

### 

[​](#limits-field)

Limits field

`non_matching_engine`: Describes rate limits applicable to requests that do not involve the matching engine. Defined by:

  * `burst`: The maximum number of requests permitted in a short burst.
  * `rate`: The sustained number of requests allowed over time.

`matching_engine`: Outlines rate limits related to operations that utilize the matching engine, with the following structure:

### 

[​](#common-limits-for-all-configurations)

Common Limits for All Configurations

#### 

[​](#spot-and-cancel-limits)

Spot and Cancel Limits

  * `spot`: Applies to spot trading between two different currencies.
  * `cancel_all`: Used when canceling all orders globally or by label without specifying a currency.



### 

[​](#global-vs-per-currency-limits)

Global vs. Per-Currency Limits

  * When `limits_per_currency` = `false`, limits apply globally:
    * `trading`: Overall trading operations
    * `maximum_quotes`: Total number of quotes
    * `maximum_mass_quotes`: Mass quoting operations
    * `guaranteed_mass_quotes`: Guaranteed mass quotes
  * When `limits_per_currency` = `true`, limits are set **per settlement currency** under the `matching_engine` object:
    * Each currency key includes:
      * `trading`: Per-currency trading limits
      * `maximum_quotes`: Per-currency quote limits
      * `maximum_mass_quotes`: Per-currency mass quoting limits
      * `guaranteed_mass_quotes`: Per-currency guaranteed mass quotes



### 

[​](#cancel-method-logic)

Cancel Method Logic

  * [`private/cancel_all`](https://docs.deribit.com/api-reference/trading/private-cancel_all): Uses the global `cancel_all` limit.
  * [`private/cancel_all_by_currency`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_currency) / [`private/cancel_all_by_instrument`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_instrument): Applies the relevant trading or spot limit for the specified currency or instrument.
  * [`private/cancel_all_by_kind_or_type`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_kind_or_type):
    * No currency specified → uses cancel_all
    * Specific currency → uses per-currency trading limit
    * Spot instrument → uses spot limit

**Example for users without per currency config (default):**

Report incorrect code

Copy

Ask AI
    
    
    {
      "non_matching_engine": {
        "burst": 1500,
        "rate": 1000
      },
      "limits_per_currency": false,
      "matching_engine": {
        "trading": {
          "total": {
            "burst": 20,
            "rate": 5
          }
        },
        "spot": {
          "burst": 250,
          "rate": 200
        },
        "maximum_quotes": {
          "burst": 500,
          "rate": 500
        },
        "maximum_mass_quotes": {
          "burst": 10,
          "rate": 10
        },
        "guaranteed_mass_quotes": {
          "burst": 2,
          "rate": 2
        },
        "cancel_all": {
          "burst": 250,
          "rate": 200
        }
      }
    }
    

**Example for users with per currency config:**

Report incorrect code

Copy

Ask AI
    
    
    {
      "non_matching_engine": {
        "burst": 1500,
        "rate": 1000
      },
      "limits_per_currency": true,
      "matching_engine": {
        "cancel_all": {
          "burst": 250,
          "rate": 200
        },
        "spot": {
          "burst": 250,
          "rate": 200
        },
        "usdt": {
          "maximum_quotes": {
            "burst": 500,
            "rate": 500
          },
          "maximum_mass_quotes": {
            "burst": 10,
            "rate": 10
          },
          "guaranteed_mass_quotes": {
            "burst": 2,
            "rate": 2
          },
          "trading": {
            "total": {
              "burst": 250,
              "rate": 200
            }
          }
        },
        "usdc": {
          "maximum_quotes": {
            "burst": 500,
            "rate": 500
          },
          "maximum_mass_quotes": {
            "burst": 10,
            "rate": 10
          },
          "guaranteed_mass_quotes": {
            "burst": 2,
            "rate": 2
          },
          "trading": {
            "total": {
              "burst": 250,
              "rate": 200
            }
          }
        },
        "eth": {
          "maximum_quotes": {
            "burst": 500,
            "rate": 500
          },
          "maximum_mass_quotes": {
            "burst": 10,
            "rate": 10
          },
          "guaranteed_mass_quotes": {
            "burst": 2,
            "rate": 2
          },
          "trading": {
            "total": {
              "burst": 250,
              "rate": 200
            }
          }
        },
        "btc": {
          "maximum_quotes": {
            "burst": 500,
            "rate": 500
          },
          "maximum_mass_quotes": {
            "burst": 10,
            "rate": 10
          },
          "guaranteed_mass_quotes": {
            "burst": 2,
            "rate": 2
          },
          "trading": {
            "perpetuals": {
              "burst": 20,
              "rate": 10
            },
            "total": {
              "burst": 150,
              "rate": 100
            }
          }
        }
      }
    }
    

## 

[​](#matching-engine-requests-overview)

Matching Engine Requests Overview

All requests **not listed below** are treated as **non-matching engine** requests.

  * [`private/buy`](https://docs.deribit.com/api-reference/trading/private-buy)
  * [`private/sell`](https://docs.deribit.com/api-reference/trading/private-sell)
  * [`private/edit`](https://docs.deribit.com/api-reference/trading/private-edit)
  * [`private/edit_by_label`](https://docs.deribit.com/api-reference/trading/private-edit_by_label)
  * [`private/cancel`](https://docs.deribit.com/api-reference/trading/private-cancel)
  * [`private/cancel_by_label`](https://docs.deribit.com/api-reference/trading/private-cancel_by_label)
  * [`private/cancel_all`](https://docs.deribit.com/api-reference/trading/private-cancel_all)
  * [`private/cancel_all_by_instrument`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_instrument)
  * [`private/cancel_all_by_currency`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_currency)
  * [`private/cancel_all_by_kind_or_type`](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_kind_or_type)
  * [`private/close_position`](https://docs.deribit.com/api-reference/trading/private-close_position)
  * [`private/verify_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-verify_block_trade)
  * [`private/execute_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-execute_block_trade)
  * [`private/move_positions`](https://docs.deribit.com/api-reference/trading/private-move_positions)
  * [`private/mass_quote`](https://docs.deribit.com/api-reference/trading/private-mass_quote)
  * [`private/cancel_quotes`](https://docs.deribit.com/api-reference/trading/private-cancel_quotes)
  * [`private/add_block_rfq_quote`](https://docs.deribit.com/api-reference/block-rfq/private-add_block_rfq_quote)
  * [`private/edit_block_rfq_quote`](https://docs.deribit.com/api-reference/block-rfq/private-edit_block_rfq_quote)
  * [`private/cancel_block_rfq_quote`](https://docs.deribit.com/api-reference/block-rfq/private-cancel_block_rfq_quote)
  * [`private/cancel_all_block_rfq_quotes`](https://docs.deribit.com/api-reference/block-rfq/private-cancel_all_block_rfq_quotes)



## 

[​](#fix-message-types)

FIX Message Types

  * [`new_order_single`](https://docs.deribit.com/fix-api/production/new-order-single)
  * [`order_cancel_request`](https://docs.deribit.com/fix-api/production/order-cancel-request)
  * [`order_mass_cancel_request`](https://docs.deribit.com/fix-api/production/order-mass-cancel-request)
  * [`order_cancel_replace_request`](https://docs.deribit.com/fix-api/production/order-cancel-replace)
  * [`mass_quote`](https://docs.deribit.com/fix-api/production/mass-quote)
  * [`quote_cancel`](https://docs.deribit.com/fix-api/production/quote-cancel)



Was this page helpful?

YesNo

[API Usage Policy](/articles/api-usage-policy)[Connection Management](/articles/connection-management-best-practices)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/notifications

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Introduction

Notifications

[Overview](/)[API Reference](/articles/json-rpc-overview)

Subscription Channels

##### Introduction

  * [Notifications](/articles/notifications)



##### Websockets

  * Platform

  * Announcements

  * Orderbook

  * Market Data

  * Trades

  * Block Trade

  * User

  * Block Rfq




On this page

  * [Notification Format](#notification-format)
  * [Basic Structure](#basic-structure)
  * [Example Notification](#example-notification)
  * [Setting Up Subscriptions](#setting-up-subscriptions)
  * [Subscription Example](#subscription-example)
  * [Channel Types](#channel-types)
  * [Notification Intervals](#notification-intervals)
  * [Order Book Notifications](#order-book-notifications)
  * [First Notification (Full Book)](#first-notification-full-book)
  * [Subsequent Notifications (Incremental Updates)](#subsequent-notifications-incremental-updates)
  * [Change ID Tracking](#change-id-tracking)
  * [Action Types](#action-types)
  * [User-Specific Notifications](#user-specific-notifications)
  * [Order Updates](#order-updates)
  * [Trade Executions](#trade-executions)
  * [Portfolio Updates](#portfolio-updates)
  * [Notification Ordering and Reliability](#notification-ordering-and-reliability)
  * [Message Ordering](#message-ordering)
  * [Handling Missed Messages](#handling-missed-messages)
  * [Reconnection Handling](#reconnection-handling)
  * [Best Practices](#best-practices)
  * [Subscription Management](#subscription-management)
  * [Processing Notifications](#processing-notifications)
  * [Performance Considerations](#performance-considerations)



Introduction

# Notifications

Copy page

API users can subscribe to certain types of notifications.

Copy page

This means that they will receive JSON-RPC notification-messages from the server when certain events occur, such as changes to the index price, changes to the order book for a certain instrument, or updates to user account information.

## 

[​](#notification-format)

Notification Format

In accordance with the JSON-RPC specification, the format of a notification is that of a request message **without an`id` field**. The value of the `method` field will always be `"subscription"`. The `params` field will always be an object with 2 members: `channel` and `data`.

### 

[​](#basic-structure)

Basic Structure

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "channel_name",
            "data": {
                // Channel-specific data
            }
        }
    }
    

### 

[​](#example-notification)

Example Notification

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "deribit_price_index.btc_usd",
            "data": {
                "timestamp": 1535098298227,
                "price": 6521.17,
                "index_name": "btc_usd"
            }
        }
    }
    

## 

[​](#setting-up-subscriptions)

Setting Up Subscriptions

The API methods [`public/subscribe`](/api-reference/subscription-management/public-subscribe) and [`private/subscribe`](/api-reference/subscription-management/private-subscribe) are used to set up a subscription. Since HTTP does not support the sending of messages from server to client, these methods are **only available when using the WebSocket transport mechanism**. At the moment of subscription, a “channel” must be specified. The channel determines the type of events that will be received.

## [Subscription ChannelsComplete reference of all available subscription channels](/subscriptions)## [Connection ManagementBest practices for managing WebSocket connections and subscriptions](/articles/connection-management-best-practices)

### 

[​](#subscription-example)

Subscription Example

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "public/subscribe",
        "params": {
            "channels": [
                "book.BTC-PERPETUAL.100ms",
                "ticker.BTC-PERPETUAL.100ms",
                "deribit_price_index.btc_usd"
            ]
        },
        "id": 1
    }
    

## 

[​](#channel-types)

Channel Types

Deribit provides two main categories of channels:

  * Public Channels

  * Private Channels




Public channels provide market data and platform information that does not require authentication:

  * **Order Book** (`book.{instrument_name}.{interval}`) - Real-time order book updates
  * **Order Book (Grouped)** (`book.{instrument_name}.{group}.{depth}.{interval}`) - Grouped order book updates with specified depth
  * **Ticker** (`ticker.{instrument_name}.{interval}`) - Instrument price and volume information
  * **Incremental Ticker** (`incremental_ticker.{instrument_name}`) - Incremental ticker updates
  * **Trades** (`trades.{instrument_name}.{interval}`) - Public trade information
  * **Trades by Kind** (`trades.{kind}.{currency}.{interval}`) - Public trades filtered by instrument kind and currency
  * **Index Prices** (`deribit_price_index.{index_name}`) - Index price updates
  * **Price Ranking** (`deribit_price_ranking.{index_name}`) - Price ranking information
  * **Price Statistics** (`deribit_price_statistics.{index_name}`) - Price statistics
  * **Volatility Index** (`deribit_volatility_index.{index_name}`) - Volatility index updates
  * **Estimated Expiration Price** (`estimated_expiration_price.{index_name}`) - Estimated expiration price
  * **Platform State** (`platform_state`) - Platform status and announcements
  * **Platform State (Public Methods)** (`platform_state.public_methods_state`) - Public methods state
  * **Perpetual Funding** (`perpetual.{instrument_name}.{interval}`) - Funding rate information
  * **Chart Data** (`chart.trades.{instrument_name}.{resolution}`) - TradingView-compatible chart data
  * **Chart Data (Simple)** (`chart.trades.{instrument_name}`) - Chart data without resolution specification
  * **Quote** (`quote.{instrument_name}`) - Quote information
  * **Instrument State** (`instrument.state.{kind}.{currency}`) - Instrument state updates by kind and currency
  * **Mark Price (Options)** (`markprice.options.{index_name}`) - Options mark price updates
  * **Block RFQ Trades** (`block_rfq.trades.{currency}`) - Block RFQ trade information
  * **Block Trade Confirmations** (`block_trade_confirmations`) - Block trade confirmation updates
  * **Block Trade Confirmations (Currency)** (`block_trade_confirmations.{currency}`) - Block trade confirmations filtered by currency



Private channels require authentication and provide user-specific information:

  * **User Orders** (`user.orders.{instrument_name}.{interval}`) - Your order updates
  * **User Trades** (`user.trades.{instrument_name}.{interval}`) - Your trade executions
  * **User Portfolio** (`user.portfolio.{currency}`) - Account balance and position updates
  * **User Changes** (`user.changes.{instrument_name}.{interval}`) - Order and position changes
  * **MMP Triggers** (`user.mmp_trigger.{index_name}`) - Market Maker Protection triggers
  * **Access Log** (`user.access_log`) - API access logging
  * **User Locks** (`user.lock`) - Account lock status



## 

[​](#notification-intervals)

Notification Intervals

Many channels support different notification intervals to control the frequency of updates:

  * **`raw`** \- Immediate notifications for every change (order book only)
  * **`100ms`** \- Notifications aggregated over 100 milliseconds
  * **`agg2`** \- Notifications aggregated over 2 seconds



Using aggregated intervals (like `100ms` or `agg2`) can reduce the number of messages you receive and help manage bandwidth and processing load.

## 

[​](#order-book-notifications)

Order Book Notifications

Order book notifications have special characteristics:

### 

[​](#first-notification-full-book)

First Notification (Full Book)

The first notification after subscribing contains the **complete order book** (bid and ask amounts for all price levels):

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "book.BTC-PERPETUAL.100ms",
            "data": {
                "timestamp": 1535098298227,
                "instrument_name": "BTC-PERPETUAL",
                "change_id": 123456,
                "bids": [
                    ["new", 50000.0, 10.5],
                    ["new", 49999.5, 5.2],
                    // ... more price levels
                ],
                "asks": [
                    ["new", 50001.0, 8.3],
                    ["new", 50001.5, 12.1],
                    // ... more price levels
                ]
            }
        }
    }
    

### 

[​](#subsequent-notifications-incremental-updates)

Subsequent Notifications (Incremental Updates)

After the first notification, you will only receive **incremental updates** for changed price levels:

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "book.BTC-PERPETUAL.100ms",
            "data": {
                "timestamp": 1535098298327,
                "instrument_name": "BTC-PERPETUAL",
                "prev_change_id": 123456,
                "change_id": 123457,
                "bids": [
                    ["change", 50000.0, 9.8],
                    ["delete", 49999.5, 0]
                ],
                "asks": [
                    ["new", 50002.0, 3.5]
                ]
            }
        }
    }
    

### 

[​](#change-id-tracking)

Change ID Tracking

Each order book notification contains a `change_id` field, and each message (except the first) contains a `prev_change_id` field. This allows you to detect if any messages have been missed:

  * If `prev_change_id` matches the `change_id` of the previous message, no messages were missed
  * If `prev_change_id` does not match, you may have missed some updates and should consider re-subscribing



### 

[​](#action-types)

Action Types

Order book updates use three action types:

  * **`new`** \- A new price level has been added
  * **`change`** \- An existing price level has been updated
  * **`delete`** \- A price level has been removed (amount is typically 0)



## 

[​](#user-specific-notifications)

User-Specific Notifications

### 

[​](#order-updates)

Order Updates

Subscribe to receive real-time updates about your orders:

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "user.orders.BTC-PERPETUAL.100ms",
            "data": {
                "order": {
                    "order_id": "12345678",
                    "instrument_name": "BTC-PERPETUAL",
                    "direction": "buy",
                    "amount": 10.0,
                    "price": 50000.0,
                    "order_state": "open",
                    // ... more order fields
                }
            }
        }
    }
    

### 

[​](#trade-executions)

Trade Executions

Receive notifications when your orders are filled:

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "user.trades.BTC-PERPETUAL.100ms",
            "data": [
                {
                    "trade_id": "87654321",
                    "order_id": "12345678",
                    "instrument_name": "BTC-PERPETUAL",
                    "direction": "buy",
                    "amount": 5.0,
                    "price": 50000.0,
                    "timestamp": 1535098298227,
                    // ... more trade fields
                }
            ]
        }
    }
    

### 

[​](#portfolio-updates)

Portfolio Updates

Monitor your account balance and positions:

Report incorrect code

Copy

Ask AI
    
    
    {
        "jsonrpc": "2.0",
        "method": "subscription",
        "params": {
            "channel": "user.portfolio.BTC",
            "data": {
                "currency": "BTC",
                "equity": 100.5,
                "available_funds": 95.2,
                "maintenance_margin": 3.1,
                "initial_margin": 5.3,
                // ... more portfolio fields
            }
        }
    }
    

## 

[​](#notification-ordering-and-reliability)

Notification Ordering and Reliability

### 

[​](#message-ordering)

Message Ordering

  * Notifications are sent in the order they occur on the server
  * Different channels may send notifications at different rates
  * Notifications from different channels may arrive out of order relative to each other



### 

[​](#handling-missed-messages)

Handling Missed Messages

For order book subscriptions, use `change_id` and `prev_change_id` to detect gaps:

Report incorrect code

Copy

Ask AI
    
    
    let lastChangeId = null;
    
    ws.on('message', function incoming(data) {
        const message = JSON.parse(data);
        if (message.method === 'subscription' && message.params.channel.startsWith('book.')) {
            const changeId = message.params.data.change_id;
            const prevChangeId = message.params.data.prev_change_id;
            
            if (lastChangeId !== null && prevChangeId !== lastChangeId) {
                console.warn('Missed order book updates! Re-subscribing...');
                // Re-subscribe to get full book snapshot
                resubscribe();
            }
            
            lastChangeId = changeId;
        }
    });
    

### 

[​](#reconnection-handling)

Reconnection Handling

When a WebSocket connection is lost and re-established:

  1. **Re-authenticate** if using private channels
  2. **Re-subscribe** to all channels you were previously subscribed to
  3. For order book channels, the first notification will be a full snapshot
  4. For other channels, you may miss updates during the disconnection period



Consider implementing a subscription manager that tracks your active subscriptions and automatically re-subscribes after reconnection. See [Connection Management Best Practices](/articles/connection-management-best-practices) for more details.

## 

[​](#best-practices)

Best Practices

### 

[​](#subscription-management)

Subscription Management

  * **Limit the number of subscriptions** \- Each subscription consumes resources. Only subscribe to channels you actually need.
  * **Use appropriate intervals** \- Use aggregated intervals (`100ms`, `agg2`) when real-time updates aren’t critical to reduce message volume.
  * **Unsubscribe when done** \- Use [`public/unsubscribe`](/api-reference/subscription-management/public-unsubscribe) or [`private/unsubscribe`](/api-reference/subscription-management/private-unsubscribe) to clean up subscriptions you no longer need.



### 

[​](#processing-notifications)

Processing Notifications

  * **Handle notifications asynchronously** \- Don’t block your message handler with slow processing
  * **Validate notification structure** \- Always check that the expected fields are present
  * **Track change IDs** \- For order book subscriptions, monitor `change_id` to detect missed messages
  * **Separate concerns** \- Use different WebSocket connections for heavy market data subscriptions vs. order management to avoid blocking order execution



### 

[​](#performance-considerations)

Performance Considerations

  * **Separate connections** \- Consider using separate WebSocket connections for:
    * Heavy market data subscriptions (many instruments, high frequency)
    * Order management and user-specific notifications
    * This prevents market data floods from delaying order execution
  * **Filter subscriptions** \- Subscribe only to instruments you’re actively trading or monitoring
  * **Use aggregated intervals** \- For non-critical data, use `agg2` interval instead of `100ms` or `raw`



Subscribing to too many channels or using `raw` intervals for many instruments can overwhelm your connection and cause delays in processing other messages, including order execution confirmations.

Was this page helpful?

YesNo

[platform_state ](/subscriptions/platform/platform_state)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/errors

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Methods overview

Error Codes

[Overview](/)[API Reference](/articles/json-rpc-overview)

JSON-RPC API

##### Methods overview

  * [JSON-RPC 2.0 Protocol](/articles/json-rpc-overview)
  * [Error Codes](/articles/errors)



##### Methods

  * Authentication

  * Account Management

  * Block RFQ

  * Block Trade

  * Combo Books

  * Market Data

  * Session Management

  * Subscription Management

  * Supporting

  * Trading

  * Wallet




On this page

  * [Error Response Format](#error-response-format)
  * [Common Error Codes](#common-error-codes)
  * [Authentication Errors (10000-10099)](#authentication-errors-10000-10099)
  * [Token Errors (13000-13099)](#token-errors-13000-13099)
  * [Rate Limit Errors](#rate-limit-errors)
  * [Trading Errors (11000-11099)](#trading-errors-11000-11099)
  * [Complete RPC Error Codes Reference](#complete-rpc-error-codes-reference)
  * [Error Handling Strategies](#error-handling-strategies)
  * [Basic Error Handler](#basic-error-handler)
  * [Retry Logic](#retry-logic)
  * [Error Recovery](#error-recovery)
  * [Error Monitoring](#error-monitoring)
  * [Error Logger](#error-logger)
  * [Error Metrics](#error-metrics)
  * [Validation Errors](#validation-errors)
  * [Parameter Validation](#parameter-validation)
  * [Complete Error Handler](#complete-error-handler)
  * [Best Practices](#best-practices)
  * [1\. Always Check for Errors](#1-always-check-for-errors)
  * [2\. Implement Exponential Backoff](#2-implement-exponential-backoff)
  * [3\. Log All Errors](#3-log-all-errors)
  * [4\. Monitor Error Rates](#4-monitor-error-rates)



Methods overview

# Error Codes

Copy page

Complete reference for handling errors in the Deribit API.

Copy page

## 

[​](#error-response-format)

Error Response Format

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "error": {
        "code": 13009,
        "message": "invalid_token",
        "data": {
          "reason": "token has expired",
          "param": "access_token"
        }
      },
      "usIn": 1704153600000000,
      "usOut": 1704153600001234,
      "usDiff": 1234,
      "id": 42
    }
    

## 

[​](#common-error-codes)

Common Error Codes

### 

[​](#authentication-errors-10000-10099)

Authentication Errors (10000-10099)

Code| Message| Description| Solution  
---|---|---|---  
10000| `authorization_required`| Authentication needed| Provide valid access token  
10001| `invalid_credentials`| Invalid API key/secret| Check credentials  
10002| `insufficient_funds`| Not enough balance| Add funds or reduce order size  
10003| `invalid_request`| Malformed request| Check request format  
10004| `not_found`| Resource not found| Verify resource exists  
10005| `forbidden`| Operation not allowed| Check permissions  
10006| `not_open_yet`| Trading not started| Wait for market open  
10007| `already_closed`| Trading ended| Market is closed  
10008| `price_too_low`| Price below minimum| Increase price  
10009| `invalid_argument`| Invalid parameter| Check parameter values  
  
### 

[​](#token-errors-13000-13099)

Token Errors (13000-13099)

Code| Message| Description| Solution  
---|---|---|---  
13009| `invalid_token`| Token expired/invalid| Refresh or re-authenticate  
13010| `token_revoked`| Token was revoked| Re-authenticate  
13011| `insufficient_scope`| Missing permissions| Use token with correct scope  
  
### 

[​](#rate-limit-errors)

Rate Limit Errors

Code| Message| Description| Solution  
---|---|---|---  
10028| `too_many_requests`| Rate limit exceeded| Wait and retry with backoff  
  
### 

[​](#trading-errors-11000-11099)

Trading Errors (11000-11099)

Code| Message| Description| Solution  
---|---|---|---  
11000| `order_not_found`| Order doesn’t exist| Check order ID  
11001| `order_closed`| Order already filled/cancelled| Cannot modify  
11002| `order_in_liquidation`| Order in liquidation| Wait for completion  
11003| `price_out_of_range`| Price too far from mark| Adjust price  
11004| `amount_too_small`| Order size too small| Increase amount  
11005| `amount_too_large`| Order size too large| Reduce amount  
11006| `post_only_reject`| Would take liquidity| Use different order type  
11007| `reduce_only_reject`| Would increase position| Check position size  
11008| `max_position_exceeded`| Position limit reached| Close positions  
11009| `self_trade_reject`| Would trade with self| Adjust price  
  
## 

[​](#complete-rpc-error-codes-reference)

Complete RPC Error Codes Reference

The following table contains the complete list of all RPC error codes returned by the Deribit API.

Error Code| Short message| Description  
---|---|---  
0 or absent| | Success, No error.  
10000| `"authorization_required"`| Authorization issue, invalid or absent signature etc.  
10001| `"error"`| Some general failure, no public information available.  
10002| `"qty_too_low"`| Order quantity is too low.  
10003| `"order_overlap"`| Rejection, order overlap is found and self-trading is not enabled.  
10004| `"order_not_found"`| Attempt to operate with order that can’t be found by specified id or label.  
10005| `"price_too_low <Limit>"`| Price is too low, `<Limit>` defines current limit for the operation.  
10006| `"price_too_low4idx <Limit>"`| Price is too low for current index, `<Limit>` defines current bottom limit for the operation.  
10007| `"price_too_high <Limit>"`| Price is too high, `<Limit>` defines current up limit for the operation.  
10009| `"not_enough_funds"`| Account has not enough funds for the operation.  
10010| `"already_closed"`| Attempt of doing something with closed order.  
10011| `"price_not_allowed"`| This price is not allowed for some reason.  
10012| `"book_closed"`| Operation for an instrument which order book had been closed.  
10013| `"pme_max_total_open_orders <Limit>"`| Total limit of open orders has been exceeded, it is applicable for PME users.  
10014| `"pme_max_future_open_orders <Limit>"`| Limit of count of futures’ open orders has been exceeded, it is applicable for PME users.  
10015| `"pme_max_option_open_orders <Limit>"`| Limit of count of options’ open orders has been exceeded, it is applicable for PME users.  
10016| `"pme_max_future_open_orders_size <Limit>"`| Limit of size for futures has been exceeded, it is applicable for PME users.  
10017| `"pme_max_option_open_orders_size <Limit>"`| Limit of size for options has been exceeded, it is applicable for PME users.  
10018| `"non_pme_max_future_position_size <Limit>"`| Limit of size for futures has been exceeded, it is applicable for non-PME users.  
10019| `"locked_by_admin"`| Trading is temporary locked by the admin.  
10020| `"invalid_or_unsupported_instrument"`| Instrument name is not valid.  
10021| `"invalid_amount"`| Amount is not valid.  
10022| `"invalid_quantity"`| quantity was not recognized as a valid number (for API v1).  
10023| `"invalid_price"`| price was not recognized as a valid number.  
10024| `"invalid_max_show"`| `max_show` parameter was not recognized as a valid number.  
10025| `"invalid_order_id"`| Order id is missing or its format was not recognized as valid.  
10026| `"price_precision_exceeded"`| Extra precision of the price is not supported.  
10027| `"non_integer_contract_amount"`| Futures contract amount was not recognized as integer.  
10028| `"too_many_requests"`| Allowed request rate has been exceeded.  
10029| `"not_owner_of_order"`| Attempt to operate with not own order.  
10030| `"must_be_websocket_request"`| REST request where Websocket is expected.  
10031| `"invalid_args_for_instrument"`| Some of the arguments are not recognized as valid.  
10032| `"whole_cost_too_low"`| Total cost is too low.  
10033| `"not_implemented"`| Method is not implemented yet.  
10034| `"trigger_price_too_high"`| Trigger price is too high.  
10035| `"trigger_price_too_low"`| Trigger price is too low.  
10036| `"invalid_max_show_amount"`| Max Show Amount is not valid.  
10037| `"non_pme_total_short_options_positions_size <Limit>"`| Limit of total size for short options positions has been exceeded, it is applicable for non-PME users.  
10038| `"pme_max_risk_reducing_orders <Limit>"`| Limit of open risk reducing orders has been reached, it is applicable for PME users.  
10039| `"not_enough_funds_in_currency <Currency>"`| Returned when the user does not have sufficient spot reserves to complete the spot trade or when an option order would negatively impact the non-cross portfolio margin balance of Cross SM user.  
10040| `"retry"`| Request can’t be processed right now and should be retried.  
10041| `"settlement_in_progress"`| Settlement is in progress. Every day at settlement time for several seconds, the system calculates user profits and updates balances. That time trading is paused for several seconds till the calculation is completed.  
10043| `"price_wrong_tick"`| Price has to be rounded to an instrument tick size.  
10044| `"trigger_price_wrong_tick"`| Trigger Price has to be rounded to an instrument tick size.  
10045| `"can_not_cancel_liquidation_order"`| Liquidation order can’t be cancelled.  
10046| `"can_not_edit_liquidation_order"`| Liquidation order can’t be edited.  
10047| `"matching_engine_queue_full"`| Reached limit of pending Matching Engine requests for user.  
10048| `"not_on_this_server"`| The requested operation is not available on this server.  
10049| `"cancel_on_disconnect_failed"`| Enabling Cancel On Disconnect for the connection failed.  
10066| `"too_many_concurrent_requests"`| The client has sent too many public requests that have not yet been executed.  
10072| `"disabled_while_position_lock"`| Spot trading is disabled for users in reduce only mode.  
11008| `"already_filled"`| This request is not allowed in regards to the filled order.  
11013| `"max_spot_open_orders"`| Total limit of open orders on spot instruments has been exceeded.  
11021| `"post_only_price_modification_not_possible"`| Price modification for post only order is not possible.  
11022| `"max_spot_order_quantity"`| Limit of quantity per currency for spot instruments has been exceeded.  
11029| `"invalid_arguments"`| Some invalid input has been detected.  
11030| `"other_reject <Reason>"`| Some rejects which are not considered as very often, more info may be specified in `<Reason>`.  
11031| `"other_error <Error>"`| Some errors which are not considered as very often, more info may be specified in `<Error>`.  
11035| `"no_more_triggers <Limit>"`| Allowed amount of trigger orders has been exceeded.  
11036| `"invalid_trigger_price"`| Invalid trigger price (too high or too low) in relation to the last trade, index or market price.  
11037| `"outdated_instrument_for_IV_order"`| Instrument already not available for trading.  
11038| `"no_adv_for_futures"`| Advanced orders are not available for futures.  
11039| `"no_adv_postonly"`| Advanced post-only orders are not supported yet.  
11041| `"not_adv_order"`| Advanced order properties can’t be set if the order is not advanced.  
11042| `"permission_denied"`| Permission for the operation has been denied.  
11043| `"bad_argument"`| Bad argument has been passed.  
11044| `"not_open_order"`| Attempt to do open order operations with the not open order.  
11045| `"invalid_event"`| Event name has not been recognized.  
11046| `"outdated_instrument"`| At several minutes to instrument expiration, corresponding advanced implied volatility orders are not allowed.  
11047| `"unsupported_arg_combination"`| The specified combination of arguments is not supported.  
11048| `"wrong_max_show_for_option"`| Wrong Max Show for options.  
11049| `"bad_arguments"`| Several bad arguments have been passed.  
11050| `"bad_request"`| Request has not been parsed properly.  
11051| `"system_maintenance"`| System is under maintenance.  
11052| `"subscribe_error_unsubscribed"`| Subscription error. However, subscription may fail without this error, please check the list of subscribed channels returned, as some channels can be not subscribed due to wrong input or lack of permissions.  
11053| `"transfer_not_found"`| Specified transfer is not found.  
11054| `"post_only_reject"`| Request rejected due to `reject_post_only` flag.  
11055| `"post_only_not_allowed"`| Post only flag not allowed for given order type.  
11056| `"unauthenticated_public_requests_temporarily_disabled"`| Request rejected because of unauthenticated public requests were temporarily disabled.  
11090| `"invalid_addr"`| Invalid address.  
11091| `"invalid_transfer_address"`| Invalid address for the transfer.  
11092| `"address_already_exist"`| The address already exists.  
11093| `"max_addr_count_exceeded"`| Limit of allowed addresses has been reached.  
11094| `"internal_server_error"`| Some unhandled error on server. Please report to admin. The details of the request will help to locate the problem.  
11095| `"disabled_deposit_address_creation"`| Deposit address creation has been disabled by admin.  
11096| `"address_belongs_to_user"`| Withdrawal instead of transfer.  
11097| `"no_deposit_address"`| Deposit address not specified.  
11098| `"account_locked"`| Account locked.  
12001| `"too_many_subaccounts"`| Limit of subbacounts is reached.  
12002| `"wrong_subaccount_name"`| The input is not allowed as the name of subaccount.  
12003| `"login_over_limit"`| The number of failed login attempts is limited.  
12004| `"registration_over_limit"`| The number of registration requests is limited.  
12005| `"country_is_banned"`| The country is banned (possibly via IP check).  
12100| `"transfer_not_allowed"`| Transfer is not allowed. Possible wrong direction or other mistake.  
12998| `"security_key_authorization_over_limit"`| Too many failed security key authorizations. The client should wait for `wait` seconds to try again.  
13004| `"invalid_credentials"`| Invalid credentials have been used.  
13005| `"pwd_match_error"`| Password confirmation error.  
13006| `"security_error"`| Invalid Security Code.  
13007| `"user_not_found"`| User’s security code has been changed or wrong.  
13008| `"request_failed"`| Request failed because of invalid input or internal failure.  
13009| `"unauthorized"`| Wrong or expired authorization token or bad signature. For example, please check the scope of the token, “connection” scope can’t be reused for other connections.  
13010| `"value_required"`| Invalid input, missing value.  
13011| `"value_too_short"`| Input is too short.  
13012| `"unavailable_in_subaccount"`| Subaccount restrictions.  
13013| `"invalid_phone_number"`| Unsupported or invalid phone number.  
13014| `"cannot_send_sms"`| SMS sending failed — phone number is wrong.  
13015| `"invalid_sms_code"`| Invalid SMS code.  
13016| `"invalid_input"`| Invalid input.  
13018| `"invalid_content_type"`| Invalid content type of the request.  
13019| `"orderbook_closed"`| Closed, expired order book.  
13020| `"not_found"`| Instrument is not found, invalid instrument name.  
13021| `"forbidden"`| Not enough permissions to execute the request, forbidden.  
13025| `"method_switched_off_by_admin"`| API method temporarily switched off by the administrator.  
13028| `"temporarily_unavailable"`| The requested service is not responding or processing the response takes too long.  
13030| `"mmp_trigger"`| Order has been rejected due to the MMP trigger.  
13031| `"verification_required"`| API method allowed only for verified users.  
13032| `"non_unique_order_label"`| Request allowed only for orders uniquely identified by given label, more than one match was foun.  
13034| `"no_more_security_keys_allowed"`| Maximal number of tokens allowed reached.  
13035| `"active_combo_limit_reached"`| Limit of active combo books was reached. The client should wait some time before retrying the request.  
13036| `"unavailable_for_combo_books"`| Action is temporarily unavailable for combo books.  
13037| `"incomplete_KYC_data"`| KYC verification data is insufficient for external service provider.  
13040| `"mmp_required"`| User is not a MMP user.  
13042| `"cod_not_enabled"`| Cancel-on-Disconnect is not enabled for the connection.  
13043| `"quotes_frozen"`| Quotes are still frozen after previous cancel.  
13403| `"scope_exceeded"`| Error returned after the user tried to edit / delete an API key using an authorized key connection with insufficient scope.  
13503| `"unavailable"`| Method is currently not available.  
13666| `"request_cancelled_by_user"`| Request was cancelled by the user with other api request.  
13777| `"replaced"`| Edit request was replaced by other one.  
13778| `"raw_subscriptions_not_available_for_unauthorized"`| Raw subscriptions are not available for unauthorized requests.  
13780| `"move_positions_over_limit"`| The client cannot execute the request yet, and should wait for `wait` seconds to try again.  
13781| `"coupon_already_used"`| The coupon has already been used by current account.  
13791| `"KYC_transfer_already_initiated"`| Sharing of KYC data with a third party provider was already initiated.  
13792| `"incomplete_KYC_data"`| User’s KYC data stored on the platform is insufficient for sharing according to third party provider.  
13793| `"KYC_data_inaccessible"`| User’s KYC data is inaccessible at the moment. Client should try again later.  
13888| `"timed_out"`| Server did not manage to process request when it was valid (`valid_until`).  
13901| `"no_more_oto_orders"`| Total limit of open “one triggers other” orders has been exceeded.  
13902| `"mass_quotes_disabled"`| Mass Quotes feature disabled for this user and currency.  
13903| `"too_many_quotes"`| Number of quotes (in Mass Quotes requests) per second exceeded.  
13904| `"security_key_setup_required"`| Not allowed without a full security key setup.  
13905| `"too_many_quotes_per_block_rfq"`| Number of quotes for single block rfq exceeded.  
13906| `"too_many_quotes_per_block_rfq_side"`| Number of quotes per single block rfq side exceeded.  
13907| `"not_fully_filled"`| Block Rfq trade cannot be fully filled with matched quotes.  
13907| `"too_many_open_block_rfqs"`| Number of open block rfq by taker exceeds configured max amount.  
13910| `"quote_crossed"`| Quote placed by the maker crosses an already placed quote by the same maker.  
13911| `"max_broker_client_count"`| Number of broker client’s exceeds allowed max amount.  
13912| `"broker_cannot_be_client"`| Broker accounts cannot be clients of other brokers.  
13913| `"broker_already_linked"`| User has already been linked to this broker.  
13914| `"user_is_a_broker_client"`| User is a client of a broker account.  
13915| `"user_is_not_a_broker"`| User account is not configured as broker account.  
13916| `"app_registered_to_broker"`| Application is registered to a broker.  
13917| `"account_quote_limit_crossed"`| Block Rfq quote limits set for the account were crossed.  
13918| `"inverse_future_cross_trading"`| Placed block rfq quote would cross trade inverse futures with block rfq quote limits set on the account.  
13919| `"client_of_main_account"`| Subaccounts of brokers cannot be linked to their own broker account.  
-32602| `"Invalid params"`| See JSON-RPC spec.  
-32600| `"request entity too large"`| Error thrown when body size in POST request or single frame in websocket connection frame exceeds the limit (32 kB).  
-32601| `"Method not found"`| See JSON-RPC spec.  
-32700| `"Parse error"`| See JSON-RPC spec.  
-32000| `"Missing params"`| See JSON-RPC spec.  
  
## 

[​](#error-handling-strategies)

Error Handling Strategies

### 

[​](#basic-error-handler)

Basic Error Handler

Report incorrect code

Copy

Ask AI
    
    
    function handleError(error) {
      switch (error.code) {
        case 13009:
          // Token expired - refresh
          return refreshToken();
        
        case 10002:
          // Insufficient funds
          throw new Error('Insufficient funds for this operation');
        
        case 10028:
          // Rate limit - retry with backoff
          return retryWithBackoff();
        
        case 11006:
          // Post-only rejected
          console.log('Order would have taken liquidity');
          return null;
        
        default:
          throw new Error(`API Error ${error.code}: ${error.message}`);
      }
    }
    

### 

[​](#retry-logic)

Retry Logic

Report incorrect code

Copy

Ask AI
    
    
    async function retryWithBackoff(fn, maxRetries = 3) {
      for (let i = 0; i < maxRetries; i++) {
        try {
          return await fn();
        } catch (error) {
          if (error.code === 10028) {
            // Rate limit - exponential backoff
            const delay = Math.pow(2, i) * 1000;
            console.log(`Rate limited, retrying in ${delay}ms`);
            await sleep(delay);
            continue;
          }
          
          if (error.code === 13009) {
            // Token expired - refresh and retry
            await refreshToken();
            continue;
          }
          
          // Other errors - don't retry
          throw error;
        }
      }
      
      throw new Error('Max retries exceeded');
    }
    
    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
    

### 

[​](#error-recovery)

Error Recovery

Report incorrect code

Copy

Ask AI
    
    
    class ErrorRecovery {
      constructor(apiClient) {
        this.apiClient = apiClient;
        this.maxRetries = 3;
      }
    
      async executeWithRecovery(fn) {
        let lastError;
        
        for (let attempt = 0; attempt < this.maxRetries; attempt++) {
          try {
            return await fn();
          } catch (error) {
            lastError = error;
            
            const shouldRetry = await this.handleError(error, attempt);
            if (!shouldRetry) {
              throw error;
            }
          }
        }
        
        throw lastError;
      }
    
      async handleError(error, attempt) {
        switch (error.code) {
          case 13009: // Token expired
            await this.apiClient.refreshToken();
            return true;
          
          case 10028: // Rate limit
            const delay = Math.pow(2, attempt) * 1000;
            await sleep(delay);
            return true;
          
          case 10002: // Insufficient funds
            console.error('Insufficient funds - cannot retry');
            return false;
          
          case 11000: // Order not found
            console.warn('Order not found - may have been filled');
            return false;
          
          default:
            // Unknown error - don't retry
            return false;
        }
      }
    }
    
    // Usage
    const recovery = new ErrorRecovery(apiClient);
    
    try {
      const result = await recovery.executeWithRecovery(async () => {
        return await apiClient.placeOrder({
          instrument_name: 'BTC-PERPETUAL',
          amount: 10,
          price: 50000
        });
      });
      console.log('Order placed:', result);
    } catch (error) {
      console.error('Failed after retries:', error);
    }
    

## 

[​](#error-monitoring)

Error Monitoring

### 

[​](#error-logger)

Error Logger

Report incorrect code

Copy

Ask AI
    
    
    class ErrorLogger {
      constructor() {
        this.errors = [];
      }
    
      log(error, context = {}) {
        this.errors.push({
          code: error.code,
          message: error.message,
          data: error.data,
          context,
          timestamp: Date.now()
        });
        
        // Alert on critical errors
        if (this.isCritical(error)) {
          this.alert(error);
        }
      }
    
      isCritical(error) {
        const criticalCodes = [10002, 11008]; // Insufficient funds, max position
        return criticalCodes.includes(error.code);
      }
    
      alert(error) {
        console.error('CRITICAL ERROR:', error);
        // Send to monitoring service
      }
    
      getStats() {
        const errorCounts = {};
        this.errors.forEach(err => {
          errorCounts[err.code] = (errorCounts[err.code] || 0) + 1;
        });
        
        return {
          total: this.errors.length,
          byCode: errorCounts,
          recent: this.errors.slice(-10)
        };
      }
    }
    

### 

[​](#error-metrics)

Error Metrics

Report incorrect code

Copy

Ask AI
    
    
    class ErrorMetrics {
      constructor() {
        this.metrics = {
          total: 0,
          byCode: {},
          byMethod: {},
          lastHour: []
        };
      }
    
      record(error, method) {
        this.metrics.total++;
        
        // Count by error code
        this.metrics.byCode[error.code] = 
          (this.metrics.byCode[error.code] || 0) + 1;
        
        // Count by method
        this.metrics.byMethod[method] = 
          (this.metrics.byMethod[method] || 0) + 1;
        
        // Track recent errors
        this.metrics.lastHour.push({
          code: error.code,
          method,
          timestamp: Date.now()
        });
        
        // Clean old errors
        this.cleanOldErrors();
      }
    
      cleanOldErrors() {
        const oneHourAgo = Date.now() - 3600000;
        this.metrics.lastHour = this.metrics.lastHour.filter(
          err => err.timestamp > oneHourAgo
        );
      }
    
      getErrorRate() {
        return this.metrics.lastHour.length / 3600; // errors per second
      }
    
      getMostCommonErrors(limit = 5) {
        return Object.entries(this.metrics.byCode)
          .sort((a, b) => b[1] - a[1])
          .slice(0, limit)
          .map(([code, count]) => ({ code: parseInt(code), count }));
      }
    }
    

## 

[​](#validation-errors)

Validation Errors

### 

[​](#parameter-validation)

Parameter Validation

Report incorrect code

Copy

Ask AI
    
    
    function validateOrderParams(params) {
      const errors = [];
    
      // Required fields
      if (!params.instrument_name) {
        errors.push({
          code: 10009,
          message: 'invalid_argument',
          param: 'instrument_name'
        });
      }
    
      if (!params.amount || params.amount <= 0) {
        errors.push({
          code: 10009,
          message: 'invalid_argument',
          param: 'amount'
        });
      }
    
      // Type validation
      if (params.type === 'limit' && !params.price) {
        errors.push({
          code: 10009,
          message: 'invalid_argument',
          param: 'price',
          reason: 'price required for limit orders'
        });
      }
    
      return errors;
    }
    
    // Usage
    const errors = validateOrderParams(orderParams);
    if (errors.length > 0) {
      throw new Error(`Validation failed: ${JSON.stringify(errors)}`);
    }
    

## 

[​](#complete-error-handler)

Complete Error Handler

Report incorrect code

Copy

Ask AI
    
    
    class DeribitErrorHandler {
      constructor(apiClient) {
        this.apiClient = apiClient;
        this.logger = new ErrorLogger();
        this.metrics = new ErrorMetrics();
      }
    
      async handle(error, context = {}) {
        // Log error
        this.logger.log(error, context);
        this.metrics.record(error, context.method);
    
        // Handle specific errors
        switch (error.code) {
          case 13009:
            return this.handleTokenExpired();
          
          case 10028:
            return this.handleRateLimit(context.attempt || 0);
          
          case 10002:
            return this.handleInsufficientFunds(error);
          
          case 11006:
            return this.handlePostOnlyReject(context);
          
          default:
            return this.handleGenericError(error);
        }
      }
    
      async handleTokenExpired() {
        console.log('Token expired, refreshing...');
        await this.apiClient.refreshToken();
        return { retry: true };
      }
    
      async handleRateLimit(attempt) {
        const delay = Math.min(Math.pow(2, attempt) * 1000, 30000);
        console.log(`Rate limited, waiting ${delay}ms`);
        await sleep(delay);
        return { retry: true, delay };
      }
    
      handleInsufficientFunds(error) {
        console.error('Insufficient funds:', error.data);
        return { retry: false, fatal: true };
      }
    
      handlePostOnlyReject(context) {
        console.log('Post-only order would take liquidity');
        return { retry: false, adjustPrice: true };
      }
    
      handleGenericError(error) {
        console.error(`API Error ${error.code}: ${error.message}`);
        return { retry: false };
      }
    
      getMetrics() {
        return {
          logger: this.logger.getStats(),
          metrics: {
            total: this.metrics.metrics.total,
            errorRate: this.metrics.getErrorRate(),
            mostCommon: this.metrics.getMostCommonErrors()
          }
        };
      }
    }
    
    // Usage
    const errorHandler = new DeribitErrorHandler(apiClient);
    
    try {
      const result = await apiClient.placeOrder(params);
    } catch (error) {
      const action = await errorHandler.handle(error, {
        method: 'private/buy',
        params
      });
      
      if (action.retry) {
        // Retry the operation
      } else if (action.fatal) {
        // Stop and alert
      }
    }
    

## 

[​](#best-practices)

Best Practices

### 

[​](#1-always-check-for-errors)

1\. Always Check for Errors

Report incorrect code

Copy

Ask AI
    
    
    const response = await apiCall();
    if (response.error) {
      handleError(response.error);
    }
    

### 

[​](#2-implement-exponential-backoff)

2\. Implement Exponential Backoff

Report incorrect code

Copy

Ask AI
    
    
    async function withBackoff(fn, maxRetries = 3) {
      for (let i = 0; i < maxRetries; i++) {
        try {
          return await fn();
        } catch (error) {
          if (i === maxRetries - 1) throw error;
          await sleep(Math.pow(2, i) * 1000);
        }
      }
    }
    

### 

[​](#3-log-all-errors)

3\. Log All Errors

Report incorrect code

Copy

Ask AI
    
    
    function logError(error, context) {
      console.error({
        code: error.code,
        message: error.message,
        context,
        timestamp: new Date().toISOString()
      });
    }
    

### 

[​](#4-monitor-error-rates)

4\. Monitor Error Rates

Report incorrect code

Copy

Ask AI
    
    
    if (errorMetrics.getErrorRate() > 1) {
      console.warn('High error rate detected');
      // Alert or throttle requests
    }
    

Was this page helpful?

YesNo

[JSON-RPC 2.0 Protocol](/articles/json-rpc-overview)[public/auth](/api-reference/authentication/public-auth)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/creating-api-key

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Authentication

Creating new API key

[Overview](/)[API Reference](/articles/json-rpc-overview)

##### Introduction

  * [Welcome to Deribit API](/)
  * [Quickstart Guide](/articles/deribit-quickstart)



##### Authentication

  * [Creating new API key](/articles/creating-api-key)
  * [Authentication](/articles/authentication)
  * [Access Scope](/articles/access-scope)
  * [Security Keys](/articles/security-keys)



##### Technical Information

  * [API Usage Policy](/articles/api-usage-policy)
  * [Rate Limits](/articles/rate-limits)



##### Best Practices

  * [Connection Management](/articles/connection-management-best-practices)
  * [Market Data Collection](/articles/market-data-collection-best-practices)
  * [Order Management](/articles/order-management-best-practices)



##### Guides

  * [Managing Deposits](/articles/managing-deposits-api)
  * [Managing Transfers](/articles/managing-transfers-api)
  * [Managing Subaccounts](/articles/managing-subaccounts-api)
  * [Managing Withdrawals](/articles/managing-withdrawals-api)
  * [Moving Positions](/articles/moving-positions-api)
  * [Block Trading](/articles/block-trading-api)
  * [Asymmetric API Keys](/articles/asymmetric-api-keys)
  * [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection)
  * [Accessing Historical Trades and Orders Using API](/articles/accessing-historical-trades-orders)
  * [Deribit Block RFQ API Walkthrough](/articles/block-rfq-api-walkthrough)
  * [Mass Quotes Specifications](/articles/mass-quotes-specifications)



On this page

  * [Front-end interface](#front-end-interface)
  * [Configuration Options](#configuration-options)
  * [Restricted Block Trades feature](#restricted-block-trades-feature)
  * [Block Trade Approval Feature](#block-trade-approval-feature)
  * [Client ID](#client-id)
  * [Client Secret](#client-secret)
  * [Scopes and Access Control](#scopes-and-access-control)
  * [Creating the API key using the API](#creating-the-api-key-using-the-api)
  * [Request](#request)
  * [Response](#response)
  * [Creating read-only access for non‑trading stuff](#creating-read-only-access-for-non%E2%80%91trading-stuff)
  * [Authentication](#authentication)
  * [Testing out your new API key](#testing-out-your-new-api-key)



Authentication

# Creating new API key

Copy page

You can create new Deribit API key using front-end interface or by Deribit API.

Copy page

If you want to use the API, please head to [the Creating the API key using the API section](#creating-the-api-key-using-the-api).

Please note your first API key has to be created using front-end interface.

## 

[​](#front-end-interface)

Front-end interface

1

[](#)

Navigate to API Section

Please head to the [API section](https://www.deribit.com/account/BTC/api) inside top right Account Panel.

2

[](#)

Add New Key

Press **‘Add new key’** on the right side of the interface.

3

[](#)

Select Key Type

Select between Deribit-generated key and Self-generated key. Please refer to [Asymmetric API keys](/articles/asymmetric-api-keys) for more details on Self-generated keys.## [Asymmetric API KeysLearn about self-generated keys for enhanced security](/articles/asymmetric-api-keys)

4

[](#)

Configure API Key

Declare scopes and other API key details:

### 

[​](#configuration-options)

Configuration Options

  * **Scopes** : Describes maximal access for authorization with given key. For more information about access scopes, refer to the section [Scopes and Access Control](#scopes-and-access-control) below and consult [official API documentation](/articles/access-scope)
  * **Name field** : This is a custom input you can enter to use as an identifier for the key.
  * **Features field** : Additional optional features related to this API key. They may be expanded in future releases.



#### 

[​](#restricted-block-trades-feature)

Restricted Block Trades feature

Restricted block trades feature limits the `block_trade:read` scope of the API key to block trades that have been made using this specific API key. This method can be employed to restrict the visibility of user private block trades with third parties to whom the user has provided their API key.

#### 

[​](#block-trade-approval-feature)

Block Trade Approval Feature

Block trade approval introduces an additional layer to the block trade verification process. When activated, it necessitates an additional approval from the user from a different API key before a block trade can be executed with the specified API key. This functionality provides users with enhanced oversight, particularly when a registered partner possessing an API key intends to carry out a block trade on their behalf.

  * **IP Whitelisting** : An additional security feature, this field restricts which IPs can connect using this API key.

Once created you will receive **Client ID** and **Client Secret**

### 

[​](#client-id)

Client ID

The Client ID is a public identifier of the API key. It’s not a secret. It can be exposed in web browsers, source code, or wherever else without immediate security concerns. It’s mainly used to identify the key and is not used on its own for authentication.

### 

[​](#client-secret)

Client Secret

The Client Secret is a confidential piece of information. Think of it as a password. It should be kept secret and never exposed to the public. Exposing the Client Secret can lead to serious security risks. It’s used, in combination with the Client ID, to authenticate.

The Client Secret is only shown once when the key is created. Store it securely - you cannot retrieve it later.

## 

[​](#scopes-and-access-control)

Scopes and Access Control

Each API key on Deribit is assigned a default access scope, which defines the maximum permissions that can be granted when authenticating. These scopes determine what operations can be performed using the authenticated session.When calling the `public/auth` endpoint, you can request one or more access scopes by including them in the scope parameter, separated by spaces:

Report incorrect code

Copy

Ask AI
    
    
    scope: account:none custody:read block_trade:read
    

However, keep in mind:

  * The requested scope cannot exceed the default scope of the API key.

For example, if your API key’s default scope is `account:read` and you request `account:read_write`, the resulting token will still only have `account:read` access.

  * The effective scope of the authenticated session is a merge of:
    * the API key’s default scope, and
    * the requested scope, limited by the key’s permissions.

The assigned scope for the token is returned in the `scope` field of the `public/auth` response.## [Access ScopesLearn more about access scopes and permissions](/articles/access-scope)

## 

[​](#creating-the-api-key-using-the-api)

Creating the API key using the API

To create an API key via the Deribit API, use the `private/create_api_key` endpoint. Please note that this is a private endpoint and requires prior authentication through the `public/auth` method.

### 

[​](#request)

Request

Report incorrect code

Copy

Ask AI
    
    
    {
      "method": "private/create_api_key",
      "params": {
        "name": "test_key",
        "max_scope": "account:read trade:read_write wallet:read"
      },
      "jsonrpc": "2.0",
      "id": 1
    }
    

### 

[​](#response)

Response

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "max_scope": "trade:read_write wallet:read account:read",
        "ip_whitelist": [],
        "client_secret": "5gE6eyXwolP4RcVmsNqq8rhjtnjv5M1_HNHUHKAXsgt",
        "client_id": "GgUXjYUj",
        "enabled_features": [],
        "timestamp": 1721816749587,
        "name": "test_key",
        "id": 11,
        "enabled": true,
        "default": false
      }
    }
    

## 

[​](#creating-read-only-access-for-non‑trading-stuff)

Creating read-only access for non‑trading stuff

For use cases like internal dashboards, monitoring tools, or finance reporting—where trading actions are not required—you can create a secure read-only API key. This setup ensures that the key can only retrieve data without being able to execute any orders or initiate withdrawals, which significantly reduces risk in case the key is ever exposed. When configuring your new API key, make sure to only assign read-only scopes. These typically include:

  * `block_rfq:read` – view RFQs
  * `block_trade:read` – view existing block trades and trade history
  * `account:read` – access account details
  * `wallet:read` – check balances and transaction history
  * `trade:read` – review past trades and open positions
  * `custody:read` – used by third-party custodians when enabled by the client

Avoid selecting any scopes that end with `:write`. This ensures that the key cannot be used to place orders, transfer funds, or perform any actions that could impact your portfolio. You may also consider enabling IP whitelisting to further restrict the usage of the key to trusted systems. This is particularly helpful for automation scripts or monitoring dashboards operating from static server locations. This approach follows the principle of least privilege and is strongly recommended when API keys are used for integrations that do not require active trading functionality.

## 

[​](#authentication)

Authentication

You can authenticate using your API credentials in two ways:

  1. Directly in the Deribit login web-page using **“Log In with API credentials”** option
  2. Using Deribit API by calling the `public/auth` method and passing your `client_id`, `client_secret`, and the desired read-only scopes

Make sure that the scopes requested in the auth call match the permissions assigned to the key. For step-by-step guidance on authentication, visit [Authentication](/articles/authentication)

## 

[​](#testing-out-your-new-api-key)

Testing out your new API key

You can test your new API key in the [Deribit API console](https://www.deribit.com/api_console/?key_id=). Simply click the link to be redirected to the console, where you will already be authenticated with your new API key.

Was this page helpful?

YesNo

[Quickstart Guide](/articles/deribit-quickstart)[Authentication](/articles/authentication)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/access-scope

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Authentication

Access Scope

[Overview](/)[API Reference](/articles/json-rpc-overview)

##### Introduction

  * [Welcome to Deribit API](/)
  * [Quickstart Guide](/articles/deribit-quickstart)



##### Authentication

  * [Creating new API key](/articles/creating-api-key)
  * [Authentication](/articles/authentication)
  * [Access Scope](/articles/access-scope)
  * [Security Keys](/articles/security-keys)



##### Technical Information

  * [API Usage Policy](/articles/api-usage-policy)
  * [Rate Limits](/articles/rate-limits)



##### Best Practices

  * [Connection Management](/articles/connection-management-best-practices)
  * [Market Data Collection](/articles/market-data-collection-best-practices)
  * [Order Management](/articles/order-management-best-practices)



##### Guides

  * [Managing Deposits](/articles/managing-deposits-api)
  * [Managing Transfers](/articles/managing-transfers-api)
  * [Managing Subaccounts](/articles/managing-subaccounts-api)
  * [Managing Withdrawals](/articles/managing-withdrawals-api)
  * [Moving Positions](/articles/moving-positions-api)
  * [Block Trading](/articles/block-trading-api)
  * [Asymmetric API Keys](/articles/asymmetric-api-keys)
  * [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection)
  * [Accessing Historical Trades and Orders Using API](/articles/accessing-historical-trades-orders)
  * [Deribit Block RFQ API Walkthrough](/articles/block-rfq-api-walkthrough)
  * [Mass Quotes Specifications](/articles/mass-quotes-specifications)



Authentication

# Access Scope

Copy page

When requesting an access token, users can specify the required access level (called scope) which defines what type of functionality they want to use, and whether requests will only read data or also modify it.

Copy page

Scopes are required and validated for `private` methods. If you only plan to use `public` methods, you can use the default scope values. **📖 Related Support Article:** [Connection Management](/articles/connection-management-best-practices)

## 

[​](#assigning-scopes-during-api-key-creation)

Assigning Scopes During API Key Creation

Scopes are assigned when you create an API key, either through the web interface or via the API. The scopes you select during key creation define the **maximum permissions** that can be granted when authenticating with that key. When you authenticate using `public/auth`, you can request specific scopes, but they cannot exceed the scopes assigned to your API key. ## [Creating API KeysLearn how to create API keys and configure scopes during setup](/articles/creating-api-key)

## 

[​](#connection-and-session-management)

Connection and Session Management

These scopes control how tokens are bound to connections and sessions:

Scope| Description  
---|---  
 _connection_|  Access is granted for the duration of the connection (or until expiration). When the connection closes, users must repeat authentication to get new tokens. Set automatically by the server when neither **connection** nor **session** scope is specified.  
_session:name_|  Creates a new session with the specified _name_ , generating tokens bound to the session. Allows reconnection and token reuse within session lifetime. Maximum 16 sessions per user. For **WebSocket** : enables skipping `access_token` in subsequent requests.  
_mainaccount_|  Set **automatically** by the server when the connecting user’s credentials belong to the main account, otherwise not included in the final scope.  
  
## 

[​](#functional-access-scopes)

Functional Access Scopes

These scopes define what API functionality your token can access. Each functional area supports both read-only (`:read`) and read-write (`:read_write`) access levels.

### 

[​](#account-management)

Account Management

Scope| Description  
---|---  
 _account:read_|  Read-only access to **account** methods and data.  
_account:read_write_|  Full access to **account** methods - manage settings, add subaccounts, etc.  
  
### 

[​](#trading)

Trading

Scope| Description  
---|---  
 _trade:read_|  Read-only access to **trading** methods and data.  
_trade:read_write_|  Full access to **trading** methods - create and modify orders.  
  
### 

[​](#wallet-operations)

Wallet Operations

Scope| Description  
---|---  
 _wallet:read_|  Read-only access to **wallet** methods and data.  
_wallet:read_write_|  Full access to **wallet** methods - withdraw, generate deposit addresses, etc.  
  
### 

[​](#block-trading)

Block Trading

Scope| Description  
---|---  
 _block_trade:read_|  Read-only access to block trading information.  
_block_trade:read_write_|  Full access to create and manage block trades.  
  
### 

[​](#block-rfq)

Block RFQ

Scope| Description  
---|---  
 _block_rfq:read_|  Read-only access to Block RFQ information, quotes and available makers.  
_block_rfq:read_write_|  Full access to create and quote Block RFQs.  
  
## 

[​](#access-denial-scopes)

Access Denial Scopes

These scopes explicitly deny access to specific functionality, useful for creating restricted API keys:

Scope| Description  
---|---  
 _account:none_|  Explicitly block access to account management functionality.  
_trade:none_|  Explicitly block access to trading functionality.  
_wallet:none_|  Explicitly block access to wallet operations.  
  
## 

[​](#token-configuration-parameters)

Token Configuration Parameters

These parameters configure token behavior and security settings:

Parameter| Description  
---|---  
 _expires:NUMBER_|  Set token expiration time to `NUMBER` seconds.  
_ip:ADDR_|  Restrict token usage to specific IPv4 address. Use `*` to allow all IP addresses.  
  
**⚠️ NOTICE:** Depending on choosing an authentication method (`grant type`) some scopes could be narrowed by the server or limited by user API key configured scope, e.g. when `grant_type = client_credentials` and `scope = wallet:read_write` could be modified by the server as `scope = wallet:read`.**The user shouldn’t assume that requested values are blindly accepted and should verify assigned scopes.**

Was this page helpful?

YesNo

[Authentication](/articles/authentication)[Security Keys](/articles/security-keys)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)


---

# Source: https://docs.deribit.com/articles/deribit-quickstart

[Skip to main content](#content-area)

[Deribit API Documentation home page](/)

Production

Search...

⌘KAsk AI




Search...

Navigation

Introduction

Quickstart Guide

[Overview](/)[API Reference](/articles/json-rpc-overview)

##### Introduction

  * [Welcome to Deribit API](/)
  * [Quickstart Guide](/articles/deribit-quickstart)



##### Authentication

  * [Creating new API key](/articles/creating-api-key)
  * [Authentication](/articles/authentication)
  * [Access Scope](/articles/access-scope)
  * [Security Keys](/articles/security-keys)



##### Technical Information

  * [API Usage Policy](/articles/api-usage-policy)
  * [Rate Limits](/articles/rate-limits)



##### Best Practices

  * [Connection Management](/articles/connection-management-best-practices)
  * [Market Data Collection](/articles/market-data-collection-best-practices)
  * [Order Management](/articles/order-management-best-practices)



##### Guides

  * [Managing Deposits](/articles/managing-deposits-api)
  * [Managing Transfers](/articles/managing-transfers-api)
  * [Managing Subaccounts](/articles/managing-subaccounts-api)
  * [Managing Withdrawals](/articles/managing-withdrawals-api)
  * [Moving Positions](/articles/moving-positions-api)
  * [Block Trading](/articles/block-trading-api)
  * [Asymmetric API Keys](/articles/asymmetric-api-keys)
  * [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection)
  * [Accessing Historical Trades and Orders Using API](/articles/accessing-historical-trades-orders)
  * [Deribit Block RFQ API Walkthrough](/articles/block-rfq-api-walkthrough)
  * [Mass Quotes Specifications](/articles/mass-quotes-specifications)



Introduction

# Quickstart Guide

Copy page

Welcome to the Deribit API! This guide will help you make your first API call in minutes.

Copy page

Deribit provides three different interfaces to access the API:

  * **JSON-RPC over WebSocket** (recommended) - Real-time, bidirectional communication
  * **JSON-RPC over HTTP** \- Simple REST-like interface
  * **FIX API** \- Financial Information eXchange protocol for institutional trading



All examples in this documentation use the **test environment** (`test.deribit.com`). To use production, change the URLs to `www.deribit.com`. Test and production environments are separate and require different accounts and API keys.

1

[](#)

Get API Credentials

  1. Log in to your Deribit account at [www.deribit.com](https://www.deribit.com) or [test.deribit.com](https://test.deribit.com) for testing
  2. Navigate to **Account** → **API**
  3. Create a new API key with appropriate permissions
  4. Save your **Client ID** and **Client Secret** securely



Never share your API credentials or commit them to version control. The client secret is only shown once and cannot be retrieved later.

## [Creating API KeysStep-by-step guide to creating API keys](/articles/creating-api-key)## [Asymmetric API KeysUsing Ed25519 or RSA key pairs for enhanced security](/articles/asymmetric-api-keys)

2

[](#)

Choose Your Interface

  * HTTP (Simplest)

  * WebSocket (Recommended)

  * FIX API




Best for: Simple scripts, one-off requests, testing

Report incorrect code

Copy

Ask AI
    
    
    # Get market data (no authentication required)
    curl -X GET "https://test.deribit.com/api/v2/public/get_instruments?currency=BTC&kind=future"
    

Best for: Real-time data, subscriptions, trading bots

Report incorrect code

Copy

Ask AI
    
    
    const WebSocket = require('ws');
    const ws = new WebSocket('wss://test.deribit.com/ws/api/v2');
    
    ws.on('open', function open() {
      // Subscribe to order book updates
      ws.send(JSON.stringify({
        "jsonrpc": "2.0",
        "method": "public/subscribe",
        "params": {
          "channels": ["book.BTC-PERPETUAL.100ms"]
        },
        "id": 1
      }));
    });
    
    ws.on('message', function incoming(data) {
      console.log(JSON.parse(data));
    });
    

Best for: Institutional trading, high-frequency tradingSee the [FIX API documentation](/fix-api/production/overview) for details.

3

[](#)

Authenticate

For private methods, you need to authenticate. Deribit supports multiple authentication methods:

  * **Client Credentials** \- Standard OAuth 2.0 flow
  * **Client Signature** \- User generated signature
  * **Refresh Token** \- Token renewal



  * HTTP Authentication

  * WebSocket Authentication




Report incorrect code

Copy

Ask AI
    
    
    # Get access token using Client Credentials
    curl -X GET "https://test.deribit.com/api/v2/public/auth" \
      -d "grant_type=client_credentials" \
      -d "client_id=YOUR_CLIENT_ID" \
      -d "client_secret=YOUR_CLIENT_SECRET"
    

Response:

Report incorrect code

Copy

Ask AI
    
    
    {
      "jsonrpc": "2.0",
      "result": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "expires_in": 31536000,
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "scope": "account:read trade:read",
        "token_type": "bearer"
      }
    }
    

Report incorrect code

Copy

Ask AI
    
    
    const WebSocket = require('ws');
    const ws = new WebSocket('wss://test.deribit.com/ws/api/v2');
    
    ws.on('open', function open() {
      // Authenticate
      ws.send(JSON.stringify({
        "jsonrpc": "2.0",
        "method": "public/auth",
        "params": {
          "grant_type": "client_credentials",
          "client_id": "YOUR_CLIENT_ID",
          "client_secret": "YOUR_CLIENT_SECRET"
        },
        "id": 1
      }));
    });
    
    ws.on('message', function incoming(data) {
      const response = JSON.parse(data);
      if (response.result && response.result.access_token) {
        console.log('Authenticated! Access token:', response.result.access_token);
        // Now you can make private method calls
      }
    });
    

## [Access ScopesLearn more about API permissions and access scopes](/articles/access-scope)

4

[](#)

Make Your First Requests

  * Public Data (No Auth)

  * Private Data (Auth Required)

  * WebSocket Subscriptions




**Get Market Data**

Report incorrect code

Copy

Ask AI
    
    
    # Get all BTC futures
    curl -X GET "https://test.deribit.com/api/v2/public/get_instruments?currency=BTC&kind=future"
    
    # Get ticker for BTC-PERPETUAL
    curl -X GET "https://test.deribit.com/api/v2/public/ticker?instrument_name=BTC-PERPETUAL"
    
    # Get order book
    curl -X GET "https://test.deribit.com/api/v2/public/get_order_book?instrument_name=BTC-PERPETUAL&depth=5"
    

**Get Account Information**

Report incorrect code

Copy

Ask AI
    
    
    # Get account summary
    curl -X GET "https://test.deribit.com/api/v2/private/get_account_summary?currency=BTC" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    
    # Get open orders
    curl -X GET "https://test.deribit.com/api/v2/private/get_open_orders?currency=BTC" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    

**Subscribe to Real-Time Data**

Report incorrect code

Copy

Ask AI
    
    
    const WebSocket = require('ws');
    const ws = new WebSocket('wss://test.deribit.com/ws/api/v2');
    
    ws.on('open', function open() {
      // Subscribe to multiple channels
      ws.send(JSON.stringify({
        "jsonrpc": "2.0",
        "method": "public/subscribe",
        "params": {
          "channels": [
            "book.BTC-PERPETUAL.100ms",
            "ticker.BTC-PERPETUAL.100ms",
            "trades.BTC-PERPETUAL.100ms"
          ]
        },
        "id": 1
      }));
    });
    
    ws.on('message', function incoming(data) {
      const message = JSON.parse(data);
      if (message.method === 'subscription') {
        console.log('Update:', message.params.channel, message.params.data);
      }
    });
    

5

[](#)

Place a Test Order (Testnet Only)

Only use test.deribit.com for testing. Never test with real funds on production.

  * HTTP

  * WebSocket




Report incorrect code

Copy

Ask AI
    
    
    # Place a limit buy order (testnet)
    curl -X GET "https://test.deribit.com/api/v2/private/buy" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -d "instrument_name=BTC-PERPETUAL" \
      -d "amount=10" \
      -d "type=limit" \
      -d "price=50000"
    

Report incorrect code

Copy

Ask AI
    
    
    ws.send(JSON.stringify({
      "jsonrpc": "2.0",
      "method": "private/buy",
      "params": {
        "instrument_name": "BTC-PERPETUAL",
        "amount": 10,
        "type": "limit",
        "price": 50000,
        "access_token": "YOUR_ACCESS_TOKEN"
      },
      "id": 2
    }));
    

Was this page helpful?

YesNo

[Welcome to Deribit API](/)[Creating new API key](/articles/creating-api-key)

⌘I

[x](https://x.com/DeribitOfficial)[linkedin](https://www.linkedin.com/company/deribit)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:dev@deribit.com)
