# Options Trading Overview

Source: https://docs.alpaca.markets/docs/options-trading-overview

---

## Introduction
- Welcome- About Alpaca- Alpaca API Platform- Authentication- SDKs and Tools- Additional Resources
## BROKER API
- About Broker API- Getting Started with Broker API- Credentials Management- Use Cases- Integration Setup with Alpaca- Broker API FAQs- Mandatory Corporate Actions- Voluntary Corporate Actions- FDIC Sweep Program- Instant Funding- Fully Paid Securities Lending- 24/5 Trading- OmniSub- Fixed Income- Customer Account Opening- Accounts Statuses- International Accounts- Domestic (USA) Accounts- Data Validations- IRA Accounts Overview- Crypto Trading- Crypto Wallets API- Funding Accounts- Journals API- Funding Wallets- ACH Funding- Instant Funding- Trading- Portfolio Rebalancing- SSE Events- Account Status Events for KYCaaS- Daily Processes and Reconcilations- Banking Holiday Funding Processes- Statements and Confirms- Local Currency Trading (LCT)- Example Trading App (Ribbit)- Options Trading Overview- Fixed Income- Tokenization Guide for Issuer- Tokenization Guide for Authorized Participant- Custodial accounts
## TRADING API
- About Trading API- Getting Started with Trading API- Working with /account- Working with /assets- Working with /orders- Working with /positions- Paper Trading- Trading Account- Crypto Spot Trading- Crypto Orders- Crypto Pricing Data- Crypto Spot Trading Fees- Options Trading- Options Orders- Options Level 3 Trading- Non-Trade Activities for Option Events- Account Activities- Fractional Trading- Margin and Short Selling- Placing Orders- DMA Gateway / Advanced Order Types- User Protection- Websocket Streaming- Trading API FAQs- Position Average Entry Price Calculation- Regulatory Fees- Alpaca&#x27;s MCP Server
## Market Data API
- About Market Data API- Getting Started with Market Data API- Historical API- Historical Stock Data- Historical Crypto Data- Historical Option Data- Historical News Data- WebSocket Stream- Real-time Stock Data- Real-time Crypto Data- Real-time News- Real-time Option Data- Market Data FAQ
## Connect API
- About Connect API- Registering Your App- Using OAuth2 and Trading API
## FIX API
- About FIX API- FIX Specification
# Options Trading Overview

# Initial Options Offering

## Supported

- US listed equities options, all american style
- Level 1-3 options trading
- Fully Disclosed partner relationships
- Automatic account approval process via the API along with SSE events
- Ability for partners to downgrade/disable options trading
- Ability to exercise options via the API
- DNE (do not exercise) via API
- New options specific activities
- Access to options market data (at a cost) or referral to market data partner

## Not supported

- LCT (local currency trading)
- Fractional options
- Extended hours

# Options Enablement

## Enabling Options Trading on a new Account

Per FINRA Rule 2360, each customer account has to be approved for options before the first options trade is made. Once options trading is enabled on a correspondent you can start requesting accounts to be approved for options trading. For existing accounts there will be a few new data points that need to be patched on the account along with a new options agreement that the customer will need to sign. Below are the new fields that will need to be provided specifically for options.

- Annual Income
- Net Worth
- Liquid Net Worth
- Liquidity Needs
- Investment Experience
- Investment Risk Tolerance
- Investment Objective
- Investment Time Horizon
- Marital Status
- Number of Dependents

Below is an example of a request for opening a new account with options enabled. More details on creating an account can be found here.
JSON
```
`{
    "enabled_assets": [
        "us_equity",
        "crypto",
        "us_option"
    ],
    "contact": {
        "email_address": "[email&#160;protected]",
        "phone_number": "555-666-7788",
        "street_address": [
            "20 N San Mateo Dr"
        ],
        "unit": "Apt 1A",
        "city": "San Mateo",
        "state": "CA",
        "postal_code": "94401",
        "country": "USA"
    },
    "identity": {
        "given_name": "John",
        "middle_name": "Smith",
        "family_name": "Doe",
        "date_of_birth": "1990-01-01",
        "tax_id": "124-55-4321",
        "tax_id_type": "USA_SSN",
        "country_of_citizenship": "USA",
        "country_of_birth": "USA",
        "country_of_tax_residence": "USA",
        "funding_source": [
            "employment_income"
        ],
        
        "annual_income_min": "10000",
        "annual_income_max": "10000",
        "total_net_worth_min": "10000",
        "total_net_worth_max": "10000",
        "liquid_net_worth_min": "10000",
        "liquid_net_worth_max": "10000",
        "liquidity_needs": "does_not_matter",
        "investment_experience_with_stocks": "over_5_years",
        "investment_experience_with_options": "over_5_years",
        "risk_tolerance": "conservative",
        "investment_objective": "market_speculation",
        "investment_time_horizon": "more_than_10_years",
        "marital_status":"MARRIED",
        "number_of_dependents":5
    },
    "disclosures": {
        "is_control_person": false,
        "is_affiliated_exchange_or_finra": true,
        "is_politically_exposed": false,
        "immediate_family_exposed": false,
        "context": [
            {
                "context_type": "AFFILIATE_FIRM",
                "company_name": "Finra",
                "company_street_address": [
                    "1735 K Street, NW"
                ],
                "company_city": "Washington",
                "company_state": "DC",
                "company_country": "USA",
                "company_compliance_email": "[email&#160;protected]"
            }
        ]
    },
    "agreements": [
        {
            "agreement": "margin_agreement",
            "signed_at": "2020-09-11T18:09:33Z",
            "ip_address": "185.13.21.99",
            "revision": "16.2021.05"
        },
        {
            "agreement": "account_agreement",
            "signed_at": "2020-09-11T18:13:44Z",
            "ip_address": "185.13.21.99",
            "revision": "16.2021.05"
        },
        {
            "agreement": "customer_agreement",
            "signed_at": "2020-09-11T18:13:44Z",
            "ip_address": "185.13.21.99",
            "revision": "16.2021.05"
        },
        {
            "agreement": "crypto_agreement",
            "signed_at": "2020-09-11T18:13:44Z",
            "ip_address": "185.13.21.99",
            "revision": "04.2021.10"
        },
        {
            "agreement": "options_agreement",
            "signed_at": "2020-09-11T18:13:44Z",
            "ip_address": "185.13.21.99"
        }
    ],
    "documents": [
        {
            "document_type": "identity_verification",
            "document_sub_type": "passport",
            "content": "/9j/Cg==",
            "mime_type": "image/jpeg"
        }
    ],
    "trusted_contact": {
        "given_name": "Jane",
        "family_name": "Doe",
        "email_address": "[email&#160;protected]"
    }
}`
```

## Enabling Options Trading on an existing Account

Below are sample requests and responses for enabling options trading on an existing account, using the approval endpoint.
Example: Account with level 1 requirements requesting for level 1 options trading approval
Request
```
`{
  "level": 1   
}`
```

Response
```
`{
    "id": "43c2f8a9-9e39-48b1-921c-e510dfeeff47",
    "account_id": "492b6297-45fc-4435-abc7-08ab15480b1c",
    "created_at": "2024-05-14T04:34:03.527165162-04:00",
    "updated_at": "2024-05-14T04:34:03.527165162-04:00",
    "requested_level": 1,
    "status": "APPROVED"
}`
```

Example:  Account with level 1 requirements requesting for level 2 options trading approval
Request
```
`{
  "level": 2   
}`
```

Response
```
`{
    "id": "43c2f8a9-9e39-48b1-921c-e510dfeeff47",
    "account_id": "492b6297-45fc-4435-abc7-08ab15480b1c",
    "created_at": "2024-05-14T04:34:03.527165162-04:00",
    "updated_at": "2024-05-14T04:34:03.527165162-04:00",
    "requested_level": 2,
    "status": "LOWER_LEVEL_APPROVED"
}`
```

### Options Approval Statuses

StatusDescription
 | `APPROVED` | User has been approved for requested options trading level.
 | `LOWER_LEVEL_APPROVED` | User has been approved for a lower level than the requested options trading level.
 | `PENDING` | Pending manual review
 | `REJECTED` | User has been rejected for requested options trading level.

### Approval fixtures

Options Approval API supports approval fixtures in the Sandbox environment. You can pass the desired approval level and approval status to test all different scenario of options approval flow (approved, lower_level_approved, rejected) to the same approval endpoint.
Example use cases:

- Requesting an `APPROVED` status for options trading level 1

JSON
```
`{
  "level": 1,   
  "fixtures": {
    "status":"APPROVED"
  }
}`
```

- Requesting an `REJECTED` status for options trading level 2

JSON
```
`{
  "level": 2,   
  "fixtures": {
    "status":"REJECTED"
  }
}`
```

- Requesting a `LOWER_LEVEL_APPROVED` status (simulating a flow where level 2 was requested but user is approved for level 2 instead)

JSON
```
`{
  "level": 2,   
  "fixtures": {
    "status":"LOWER_LEVEL_APPROVED",
    "level":1
  }
}`
```

## Downgrading/disabling Options

Once an account is approved for options trading the customer has the ability to downgrade the options level or disable it altogether. This is done by setting the max_options_trading_level via the trading account configuration endpoint.
Once the max options trading level is set the options trading level on the trading account endpoint will get upgraded to the value set by the user. Note the options trading level will always be the same or lower than the options approved level. Below is an example of a user being approved for level 2 but downgrading to level 1.
JSON
```
`{
  ...
  "options_approved_level": 2,
  "options_trading_level": 1,
  ...
}`
```

# Trading

## Trading Overview

When placing orders via the orders api for options below is what is supported and what is not supported

### Supported

- Options symbol
- Time in force of day
- Market and limit order types
- Ability to replace and cancel orders
- Level 1 + 2 option strategies

### Not supported

- Extended hours
- Fractional or notional order support

## Trading Levels

Alpaca supports the below options trading levels.

LevelSupported TradesValidation
 | 0 | 
- Options trading is disabled
 | 
- NA

 | 1 | 
- Sell a covered call
- Sell cash-secured put
 | 
- User must own sufficient underlying shares
- User must have sufficient options buying power

 | 2 | 
- Level 1
- Buy a call
- Buy a put
 | 
- User must have sufficient options buying power

### Trading Level Validation

If a user tries to trade a strategy above their level this will result in an error message. Below is an example of a user who is approved for level 1 trying to place a level 2 options trade.
JSON
```
`{
   "code": 40310000,
   "message": "account not eligible for level2 options trading"
}`
```

## Asset Master

Similar to the asset master for securities and crypto there is an options contract endpoint which will return all the options contract for an underlying symbol. Below is a sample
JSON
```
`{
  "id": "1fb904df-961a-4a07-a924-53a437626db2",
  "symbol": "AAPL240223C00095000",
  "name": "AAPL Feb 23 2024 95 Call",
  "status": "active",
  "tradable": true,
  "expiration_date": "2024-02-23",
  "root_symbol": "AAPL",
  "underlying_symbol": "AAPL",
  "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "type": "call",
  "style": "american",
  "strike_price": "95",
  "size": "100",
  "open_interest": "12",
  "open_interest_date": "2024-02-22",
  "close_price": "89.35",
  "close_price_date": "2024-02-22"
 }`
```

## Order Examples

Buying a call
JSON
```
`{  
  "symbol": "PTON240126C00000500",  
  "qty": "1",  
  "side":"buy",  
  "type": "market",  
  "time_in_force": "day"  
}`
```

Buying a put
JSON
```
`{  
  "symbol": "TSLA240126P00210000",  
  "qty": "1",  
  "side": "buy",  
  "type": "market",  
  "time_in_force": "day"  
}`
```

Selling a covered call
JSON
```
`{  
  "symbol": "AAPL240126C00050000", 
  "qty": "1", 
  "side": "sell", 
  "type": "market", 
  "time_in_force": "day"  
}`
```

Selling a cash secured put
JSON
```
`{  
  "symbol": "QS240126P00006500",  
  "qty": "1",  
  "side": "sell",  
  "type": "market",  
  "time_in_force": "day"  
}`
```

## Buying Power Checks

With options we introduce a new field on the trading account endpoint called options_buying_power which is evaluated when trying to open new options positions.
For both buying a call or buying a put sufficient buying power is necessary to pay for the premium of the contract otherwise an error will occur as shown below.
JSON
```
`{
"options_buying_power": "7267.84",
"code": 40310000,
"cost_basis": "38000",
"message": "insufficient options buying power"
}`
```

For Selling Covered Call you need to have enough stocks as collateral otherwise the order will error out as shown below.
JSON
```
` {
   "available_qty": "0",
   "code": 40310000,
   "message": "insufficient underlying qty available for covered call (required: 100, available: 0)",
   "required_qty": "100",
   "symbol": "AAPL240126C00050000",
   "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415"
}`
```

For selling cash secured put you will need enough buying power to pay for the underlying stock minus the premium that would be received otherwise the order will error out as shown below
JSON
```
`{
  "buying_power": "9395",
  "code": 40310000,
  "message": "insufficient options buying power for cash-secured put (required: 20310, available: 9395)",
  "required_options_buying_power": "20310"
}`
```

# Positions

Option positions will show up like any other position in the positions endpoint. Below is an example of an options position.
JSON
```
`{
  "asset_id": "fe4f43e5-60a4-4269-ba4c-3d304444d58b",
  "symbol": "PTON240126C00000500",
  "exchange": "",
  "asset_class": "us_option",
  "asset_marginable": true,
  "qty": "2",
  "avg_entry_price": "6.05",
  "side": "long",
  "market_value": "1068",
  "cost_basis": "1210",
  "unrealized_pl": "-142",
  "unrealized_plpc": "-0.1173553719008264",
  "unrealized_intraday_pl": "-142",
  "unrealized_intraday_plpc": "-0.1173553719008264",
  "current_price": "5.34",
  "lastday_price": "5.34",
  "change_today": "0",
  "qty_available": "2"
}`
```

# Post Trade

## Exercising

As the buyer of an option (call or put), the holder has the right, but not the obligation, to buy or sell the option&#x27;s underlying security at a specified price on or before a specified date in the future. If the holder decides to act on those rights they are choosing to exercise. An option can be exercised via the exercise endpoint and instructions for DNE (do not exercise) instructions can be supplied via Do not exercise endpoint. Note exercise requests will be processed instantly and requests sent outside of market hours will be rejected. When exercising there will be 2 new activities per exercise which are:

- OPEXC - removes the options position as a result of exercising
- OPTRD - trading activity that is paired with the exercising

### Exercising Call

A long call exercise results in buying the underlying stock at the strike price. Below is an example of this.
JSON
```
`{
  "id": "20240227000000000::197118f0-afd8-4adb-b154-167f4a87b1f5",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXC",
  "date": "2024-02-27",
  "net_amount": "0",
  "description": "Option Exercise",
  "symbol": "QS240301C00006500",
  "qty": "-1",
  "status": "executed"
},

{
  "id": "20240227000000000::aa97cbc4-5163-49ab-b832-682a3a3e85bb",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPTRD",
  "date": "2024-02-27",
  "net_amount": "-650",
  "description": "Option Trade",
  "symbol": "QS",
  "qty": "100",
  "price": "6.5",
  "status": "executed"
}`
```

### Exercising Put

A long put exercise results in selling the underlying stock at the strike price. Below is an example of this.
JSON
```
`{
  "id": "20240227000000000::f62ee8f5-0279-4e81-9bd1-4ef197c7b2f3",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXC",
  "date": "2024-02-27",
  "net_amount": "0",
  "description": "Option Exercise",
  "symbol": "QS240301P00006500",
  "qty": "-1",
  "status": "executed"
},

{
  "id": "20240227000000000::74e1db8e-9316-4dcf-b69c-50f51427b7c1",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPTRD",
  "date": "2024-02-27",
  "net_amount": "650",
  "description": "Option Trade",
  "symbol": "QS",
  "qty": "-100",
  "price": "6.5",
  "status": "executed"
}
`
```

## Assignment

When selling an options contract (call or put) the user collects a premium but in turn takes on the obligation to buy or sell the stock at the agreed upon strike price if assigned. It is important to note that the OCC assigns a random account and sellers of contracts can be assigned overnight. When assigned there will be 2 new activities per assignment which are:

- OPASN - removes the options position as a result of assignment
- OPTRD - trading activity that is paired with the assignment

### Call Assignment

For call options, the seller takes on the obligation to sell the stock at the agreed upon strike price. Below is an example of activities that result as a result of a call assignment
JSON
```
` {
   "id": "20240301000000000::001140db-3947-456b-aefc-253861fb65df",
   "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
   "activity_type": "OPASN",
   "date": "2024-03-01",
   "net_amount": "0",
   "description": "",
   "symbol": "QS240301C00004500",
   "qty": "1",
   "status": "executed"
}

{
  "id": "20240301000000000::a88c089f-a8c3-4672-9b68-2f6f2d05e914",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPTRD",
  "date": "2024-03-01",
  "net_amount": "450",
  "description": "Option Trade",
  "symbol": "QS",
  "qty": "-100",
  "price": "4.5",
  "status": "executed"
}`
```

### Put Assignment

For put options, the seller takes on the obligation to buy the stock at the agreed upon strike price. Below is an example of activities that result as a result of a put assignment
JSON
```
`{
  "id": "20240301000000000::fcd92e5c-46e4-4c6e-8866-d56cd7d2bde2",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPASN",
  "date": "2024-03-01",
  "net_amount": "0",
  "description": "",
  "symbol": "QS240301P00009000",
  "qty": "1",
  "status": "executed"
}

{
  "id": "20240301000000000::1e1c2804-ce68-4516-9fa4-62d49b14c334",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPTRD",
  "date": "2024-03-01",
  "net_amount": "-900",
  "description": "Option Trade",
  "symbol": "QS",
  "qty": "100",
  "price": "9",
  "status": "executed"
}`
```

## Expiration

Unlike stocks, option contracts have an expiration date. If the user does not close out their position or exercise their options (if they have the buying power to support the exercise), Alpaca will need to potentially take action on it for risk management purposes based on the criteria described below.

- Starting at 3:30 pm EST on the date of expiration, Alpaca continuously evaluates any open positions that expire that day and stops accepting new orders to open/extend any positions.
- If the position for a long call or put is ITM (in the money) by .01 or more, Alpaca checks if the account has enough buying power to exercise in the case of a call or enough shares in the case of a put

- If there is enough buying power or shares Alpaca will not liquidate the options and will let the option auto-exercise.
- If there is not enough buying power or shares, then Alpaca will liquidate while it’s still ITM

- If the position is for a covered call or cash secured put and ITM by .01 or more Alpaca will automatically assign after close on date of expiry
- If the position is not ITM  in other words it’s ATM (at the money) or OTM (out of the money), Alpaca may skip it and it will expire after close as shown in the examples below. (Note that positions slightly OTM may also be liquidated depending on market and underlying conditions. Alpaca will take into consideration fast moving markets and/or fast stocks that may be moving from ITM and OTM throughout the day. There may be instances where OTM positions are also closed out.)

### Call Expiration

JSON
```
`{
  "id": "20240301000000000::31ff5d4c-a608-43bb-8e59-678a96a4a42c",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXP",
  "date": "2024-03-01",
  "net_amount": "0",
  "description": "Option Expiry",
  "symbol": "QS240301C00010500",
  "qty": "-1",
  "status": "executed"
}`
```

### Put Expiration

JSON
```
`{
  "id": "20240301000000000::4bd8c683-0b2c-489f-9df9-1243ff621648",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXP",
  "date": "2024-03-01",
  "net_amount": "0",
  "description": "Option Expiry",
  "symbol": "QS240301P00000500",
  "qty": "-1",
  "status": "executed"
}`
```

# Market Data

Alpaca provides access to options market data (at a cost) in the same user-friendly format it does for stocks and crypto. Additionally, we can refer partners to external data vendors with whom Alpaca has a close relationship if necessary.

EndpointNoteste
 | Latest Quotes | Latest quotes. Supports multiple symbols
 | Latest Trades | Latest trades. Supports multiple symbols
 | Historical Trades | Historical trades. Supports multiple symbols
 | Snapshots | Combine quotes and trades for multiple symbols
 | Option chain | Query option chain by the underlying (stock) symbols
 | Historical bars | Historical bars.Supports multiple symbol
Options trading is not suitable for all investors due to its inherent high risk, which can potentially result in significant losses. Please read Characteristics and Risks of Standardized Options before investing in options.Updated 18 days ago Example Trading App (Ribbit)Fixed Income- Ask AI
