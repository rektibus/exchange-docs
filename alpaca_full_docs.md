# Alpaca Full Documentation



---

# Welcome (https://docs.alpaca.markets/docs/getting-started)

# Welcome

This page will help you get started with Alpaca Docs. You'll be up and running in a jiffy!

# Welcome to Alpaca 🦙

Alpaca offers simple, modern API-first solutions to enable anyone, either individuals or businesses, to connect applications and build algorithms to buy and sell stocks or crypto.

Whether you are launching an app to access the US equities market or deploy algorithmic trading-strategies with stocks and crypto, Alpaca has an API for you.

* Build trading apps and brokerage services for your end users. Tailored for businesses such as trading apps, challenger banks, etc. - **Start [here](/docs/getting-started-with-broker-api)**
* Stock trading for individuals and business accounts. Built for retail, algorithmic and proprietary traders. - **Start [here](https://docs.alpaca.markets/docs/getting-started-with-trading-api)**
* Access real-time market pricing data and up to 6+ years worth of historical data for stocks and crypto. - **Start [here](https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data)**
* Develop applications on Alpaca’s platform using OAuth2. Let any user with an Alpaca brokerage account connect to your app. - **Start [here](https://docs.alpaca.markets/docs/about-connect-api)**

If you are not a developer and an API is not for you, we also enable users to trade on our responsive web dashboard.

Stay tuned for our API updates as we have on roadmap plans for futures, FX, and much more!

Updated about 1 month ago

---

Ask AI

---

# About Alpaca (https://docs.alpaca.markets/docs/about-alpaca)

# About Alpaca

# About Alpaca

## History & Founders

Alpaca is a technology company headquartered in Silicon Valley that builds a simple and modern API for stock and crypto trading. Our Brokerage services are provided by Alpaca Securities LLC, a member of [FINRA](https://www.finra.org/#/)/[SIPC](https://www.sipc.org/). We are a team of diverse background individuals with deep financial and technology expertise, backed by some of the top investors in the industry globally. We are proud to be supported by the love of enthusiastic community members on various platforms.

Alpaca’s globally distributed team consists of developers, traders, and brokerage business specialists, who collectively have decades of financial services and technology industry experience at organizations such as FINRA, Apple, Wealthfront, Robinhood, EMC, Cloudera, JP Morgan, and Lehman Brothers. Alpaca is co-founded and led by [Yoshi Yokokawa](https://www.linkedin.com/in/yoshiyokokawa/) (CEO) and [Hitoshi Harada](https://www.linkedin.com/in/hitoshi-harada-02b01425/) (CPO).

Our investors include a group of well-capitalized investors including Portage Ventures, Spark Capital, Tribe Capital, Social Leverage, Horizons Ventures, Elderidge, and Y Combinator as well as highly experienced industry angel investors such as Joshua S. Levine (former CTO/COO of ETRADE), Nate Rodland (former COO of Robinhood & GP of Elefund), Patrick O’Shaughnessy (“Invest Like the Best” podcast host & Partner of Positive Sum), Jacqueline Reses (former Executive Chairman of Square Financial Services), Asiff Hirjii (former President/COO of Coinbase), Aaron Levie (CEO of Box), and founders of leading Fintech companies including Plaid and Wealthsimple.

## Vision

> ## Allow 8+ billion people on the planet to access financial markets.

We are committed to providing a secure, reliable and compliant platform for anyone who wants to build their own trading strategies, asset management automation, trading and robo-advisor apps, new brokerage services, investment advisory services and investment products. We value having a variety of developers who create exciting and innovative projects with our API.

## What Services Does Alpaca Provide?

Alpaca provides trading and clearing services for US equities under its subsidiary Alpaca Securities LLC. We currently support stocks, ETFs listed in the US public exchanges (NMS stocks), Options trading, and cryptocurrencies. Support for other asset classes, such as futures, FX, private equities, and international equities are on our roadmap.

We work with retail traders and institutional investors directly, and also work with app developers, broker-dealers globally, investment advisors and fintech companies that offer US stock investing features to their end customers, both in and out of the United States.

To serve our customers, we provide Web API, Web dashboards, market data, paper trading simulation, API sandbox environment, and community platforms.

Updated 5 months ago

---

Ask AI

---

# Alpaca API Platform (https://docs.alpaca.markets/docs/alpaca-api-platform)

# Alpaca API Platform

# Why API?

Alpaca’s features to access financial markets are provided primarily via API. We believe API is the means to interact with services such as ours and innovate your business. Our API is designed to fit your needs and we continue to build what you need.

# REST, SSE and Websockets

Our API is primarily built in the REST style. It is a simple and powerful way to integrate with our services.

In addition to the REST API which replies via synchronous communication, our API includes an asynchronous event API which is based on WebSocket and SSE, or [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html). As many types of events occur in the financial markets (orders fill based on the market movement, cash settles after some time, etc), this event-based API helps you get updates instantly and provide the best user experiences to your customers.

# Architecture

Alpaca’s platform consists of APIs, Web dashboards, trade simulator, sandbox environment, authentication services, order management system, trading routing, back office accounting and clearing system, and all of these components are built in-house from the ground up with modern architecture.

The Alpaca platform is currently hosted on the Google Cloud Platform in the us-east4 region. The site is connected with dedicated fiber lines to a data center in Secaucus, NJ, to cross-connect with various market venues.

Under the hood, Alpaca works with various third parties. As we are self clearing for equities trade clearing and settlement on DTCC, we are also self clearing for options trade clearing and settlement with the OCC. Cash transfers and custody are primarily provided by BMO Harris, We use Currency Cloud and Airwallex for funding wallets and international transfers. Citadel Securities, Virtu America, Jane Street, Ion Group, and other execution providers provide execution services for our customer orders. We integrate with multiple data service providers, with ICE Data Services being our primary vendor for various kinds of market data.

Alpaca Crypto executes customer trades on our internal central limit order book, self-clears all trades and does not custody customer cash but has banking relationships with Customers Bank, Cross River Bank, Choice Financial and FVBank. To provide live market data, Alpaca Crypto works with Coinbase, Kraken, FalconX and Stillman Digital.

# API Updates & Upgrades

In an effort to continuously provide value to our developers, Alpaca frequently performs updates and upgrades to our API.

We’ve added the following sections to our docs in order to help make sure that as a developer you know what to expect, when to expect, and how to properly handle certain scenarios .

## Backwards Compatible Changes

You should expect any of the following kind of changes that we make to our API to be considered a backwards compatible change:

* Adding new or similarly named APIs
* Adding new fields to already defined models and objects such as API return objects, nested objects, etc. (Example: adding a new code field to error payloads)
* Adding new items to defined sets or enumerations such as statuses, supported assets, etc. (Example: adding new account status to a set of all )
* Enhancing ordering on how certain lists get returned
* Supporting new HTTP versions (HTTP2, QUIC)
* Adding new HTTP method(s) for an existing endpoint
* Expecting new HTTP request headers (eg. new authentication)
* Sending new HTTP headers (eg. HTTP caching headers, gzip encoding, etc.)
* Increasing HTTP limits (eg. Nginx large-client-header-buffers)
* Increasing rate limits
* Supporting additional SSL/TLS versions

Generally, as a rule of thumb, any append or addition operation is considered a backwards compatible update and does not need an upfront communication. These updates should be backwards compatible with existing interfaces and not cause any disruption to any clients calling our APIs.

## Breaking Changes

When and if Alpaca decides to perform breaking changes to our APIs the following should be expected:

* Upfront communication with sufficient time to allow developers to be able to react to new upcoming changes
* Our APIs are versioned, if breaking changes are intended we will generally bump the API version. For example, a route might go from being `/v1/accounts/{account_id}` to `/v2/accounts/{account_id}` if we had to make a breaking change to either the parameters it can take or its return structure

Updated 4 months ago

---

Ask AI

---

# Authentication (https://docs.alpaca.markets/docs/authentication)

# Authentication

# How to call our API

Alpaca's APIs are available under different domain names, and you first need to make sure that you are calling the right one. This page describes the machine-to-machine authentication types available in the following scenarios:

* If you have a live account, you can call:
  + Trading API endpoints on `api.alpaca.markets`
  + Market Data API endpoints on `data.alpaca.markets`
* If you have a paper account, you can call:
  + Trading API endpoints on `paper-api.alpaca.markets`
  + Market Data API endpoints on `data.alpaca.markets`
* If you are a live broker partner, you can call:
  + Broker API endpoints on `broker-api.alpaca.markets`
  + Market Data API endpoints on `data.alpaca.markets`
  + Authentication endpoints on `authx.alpaca.markets`
* If you are a sandbox broker partner, you can call:
  + Broker API endpoints on `broker-api.sandbox.alpaca.markets`
  + Market Data API endpoints on `data.sandbox.alpaca.markets`
  + Authentication endpoints on `authx.sandbox.alpaca.markets`

If you have more than one account (or in case of broker partners, more than one correspondent), each of those have separate credentials. As an example, you cannot use your live account's credentials with the paper API, or vice versa.

# Authentication flows

## Client credentials

> 🚧
>
> The Client Credentials authentication flow is not yet available for Trading API.

When using this flow, you first need to exchange your credentials for a short-lived access token, then use that token to authenticate with our API. Do not request a new access token for each API call. Access tokens issued by our token endpoint are valid for 15 minutes.

We offer two types of credentials you can use with this flow:

* Use a client ID and a client secret (`client_secret`) - this is easier, as you can simply pass the secret that was generated when you created your credentials to our token endpoint. Note that we only support passing the client secret in the request body (`client_secret_post`), not in the `Authorization` header (`client_secret_basic`).
* Use a client ID and a signed client assertion (`private_key_jwt`) - this ensures that the private key used to sign client assertions never leaves your custody, but it requires you to construct and sign a JWT token with a private key before each call to the token endpoint. See [RFC 7523](https://www.rfc-editor.org/rfc/rfc7523.html#section-2.2) for more information on how to do so.

As an example, here is how a Broker API user would request an access token from our [token endpoint](../reference/issuetokens) using the first method:

cURL

```
curl -X POST "https://authx.alpaca.markets/v1/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials" \
     -d "client_id={YOUR_CLIENT_ID}" \
     -d "client_secret={YOUR_CLIENT_SECRET}"
```

The response will contain an access token:

JSON

```
{
    "access_token": "{TOKEN}",
    "expires_in": 899,
    "token_type": "Bearer"
}
```

The returned token can be used to authenticate with Broker API:

cURL

```
curl -X GET "https://broker-api.alpaca.markets/v1/accounts" \
     -H "Authorization: Bearer {TOKEN}"
```

## Legacy

Our older authentication flow lets you authenticate with your key ID and secret key directly. You have two options to authenticate your requests:

* Use HTTP Basic Authentication, send your key ID as the username, and your secret key as the password.
* Use the `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` headers to send your key ID and secret key.

As an example, here is how a Trading API user would authenticate with our API using the second method:

cURL

```
curl -X GET "https://api.alpaca.markets/v2/account" \
     -H "APCA-API-KEY-ID: {YOUR_API_KEY_ID}" \
     -H "APCA-API-SECRET-KEY: {YOUR_API_SECRET_KEY}"
```

Updated 3 months ago

---

Ask AI

---

# SDKs and Tools (https://docs.alpaca.markets/docs/sdks-and-tools)

# SDKs and Tools

# Official Client SDKs

Alpaca provides and supports the following open-source SDKs in a number of languages. You can leverage these libraries to easily access our API in your own application code or your trading scripts.

* **Python**: [alpaca-py](https://alpaca.markets/sdks/python/) / [PyPI](https://pypi.org/project/alpaca-py/)
* **.NET/C#**: [alpaca-trade-api-csharp](https://github.com/alpacahq/alpaca-trade-api-csharp/) / [NuGet](https://www.nuget.org/packages/Alpaca.Markets/)
* **Node**: [alpaca-trade-api-js](https://github.com/alpacahq/alpaca-trade-api-js/) / [npm](https://www.npmjs.com/package/@alpacahq/alpaca-trade-api)
* **Go**: [alpaca-trade-api-go](https://github.com/alpacahq/alpaca-trade-api-go/)
* **Python (legacy)**: [alpaca-trade-api-python](https://github.com/alpacahq/alpaca-trade-api-python/) / [PyPI](https://pypi.org/project/alpaca-trade-api/)

# Alpaca-py (Python SDK)

[**Alpaca-py**](https://alpaca.markets/sdks/python/getting_started.html) provides an interface for interacting with the API products Alpaca offers. These API products are provided as various REST, WebSocket and SSE endpoints that allow you to do everything from streaming market data to creating your own trading apps. Here are some things you can do with Alpaca-py:

* [**Market Data API**](https://alpaca.markets/sdks/python/api_reference/data_api.html): Access live and historical market data for 5000+ stocks and 20+ crypto.
* [**Trading API**](https://alpaca.markets/sdks/python/api_reference/trading_api.html): Trade stock and crypto with lightning fast execution speeds.
* [**Broker API & Connect**](https://alpaca.markets/sdks/python/api_reference/broker_api.html): Build investment apps - from robo-advisors to brokerages.

# Community-Made SDKs

In addition to the SDKs directly supported by Alpaca, individual members of our community have created and contributed their own wrappers for these other languages. We are providing these links as a courtesy to the community and to our users who are looking for the API wrapper in other languages or variants. Please be sure to carefully review any code you use to access our financial trading API and/or trust your account credentials to.

Made your own wrapper for a language not listed? Join our community Slack and let us know about it!

* **C++**: [alpaca-trade-api-cpp](https://github.com/marpaia/alpaca-trade-api-cpp)
* **Java**: [alpaca-java](https://github.com/Petersoj/alpaca-java)
* **Node.js** (TypeScript): [alpaca-ts](https://github.com/alpacahq/alpaca-ts)
* **R**: [alpaca-for-r](https://github.com/yogat3ch/AlpacaforR)
* **Rust**: [apca](https://github.com/d-e-s-o/apca) (SDK) & [apcacli](https://github.com/d-e-s-o/apcacli) (CLI)
* **Scala**: [Alpaca Scala](https://github.com/cynance/alpaca-scala)
* **Ruby**: [alpaca-trade-api](https://github.com/ccjr/alpaca-trade-api)
* **Elixir**: [alpaca\_elixir](https://github.com/jrusso1020/alpaca_elixir)

Updated 5 months ago

---

Ask AI

---

# Additional Resources (https://docs.alpaca.markets/docs/additional-resources)

# Additional Resources

# Alpaca Learn

We post regular content on our Alpaca Learn resource site where you can find the latest market updates, development tools and tips and much more to help you along your journey developing with Alpaca. For more click [here](https://alpaca.markets/learn/).

# Blog

Dont miss a beat and find the latest updates from Alpaca in our blog. For more click [here](https://alpaca.markets/blog/).

# Slack Community

We have an active community on Slack with developers and traders from all over the world. For Broker API we have a dedicated channel #broker-api for you to discuss with the rest of the community building new products using Broker API. You will be automatically added to `#announcements`, `#community`, `#feedback`, and `#q-and-a`. To join click [here](https://join.slack.com/t/alpaca-community/shared_invite/zt-1mwc1kpf8-ssNEGH6IyKgAAtFaSC_GMg).

# Forum

We have set up a community forum to discuss topics ranging from integration, programming, API questions, market data, etc. The forum is also a place to find up-to-date announcements about Alpaca and its features. The forum is the recommended place for discussion, since it has more advanced indexing and search functionality compared to our other community channels. For more click [here](https://forum.alpaca.markets/).

# Support

Have questions? Need help? Check out our support page for FAQs and to get in contact with our team. For more click [here](https://alpaca.markets/support).

# Systems Status

Stay up to date with Alpaca services status and any updates on outages. For more click [here](https://status.alpaca.markets/).

# Disclosures

To view our disclosures library click [here](https://alpaca.markets/disclosures).

Updated 5 months ago

---

Ask AI

---

# About Broker API (https://docs.alpaca.markets/docs/about-broker-api)

# About Broker API

This is the documentation about Broker API that helps you build trading apps and brokerage services for your end users. If you are looking to build your own trading bots and algos, read the Trading API documentation. With Alpaca Broker API, you can build the full brokerage experiences for your end users around account opening, funding and trading. This document describes all you need to know to build your trading app.

# Broker API Use Cases

There are several different use cases for Broker API integration. Below are some common ones, but please do not hesitate to reach out to our sales team if you have a different case in mind. We want our platform to encourage a broad range of use cases.

* Broker dealer (fully-disclosed, omnibus)
* Registered Investment Advisor (RIA)

*We support most use cases internationally.*

Depending on the case, the API methods you want to use could vary. For example, the omnibus broker-dealer case never uses API to open a customer account since the trading accounts are created upfront and you will submit orders to them, and manage your end customer accounting on your end. More details on each use case are described in the following sections.

Updated 5 months ago

---

Ask AI

---

# Getting Started with Broker API (https://docs.alpaca.markets/docs/getting-started-with-broker-api)

# Getting Started with Broker API

This guide is going to help you set everything up in a sandbox environment to get you up and running with Broker API.

The sandbox environment acts as a parallel environment where you can test our APIs safely without sending any real trades to the market. All prices, and execution times (i.e. market hours) hold true in sandbox and production.

You can either follow the steps below to test specific calls within the broker dashboard or access the Postman collection to view and test all possible requests in one place.

# Postman Collection

To get started with the Broker API Postman Collection you can either access the [Alpaca Workspace on Postman](https://www.postman.com/alpacamarkets/workspace/alpaca-public-workspace/overview) to fork the collection or import the file below directly to your own workspace.

## Fork Broker API Collection on Postman

Refer to this [tutorial](https://alpaca.markets/learn/try-our-postman-workspace-for-alpaca-apis/) to learn how to fork the collection and sample environment and get started with making calls right away. We recommend following this method so your collection stays up to date with the changes we make to the API.

## Import Broker API Collection

1. Download the [Broker API API Collection](https://www.postman.com/alpacamarkets/workspace/alpaca-public-workspace/collection/19455863-d72a0729-972d-486f-8aa9-2b5aede8d615?ctx=documentation)
2. Import the file into Postman (File -> Import..)
3. Create a Postman environment with the following variables. Be sure to select the environment in the upper right hand corner like pictured below.

![](https://files.readme.io/a8d4aae-image.png)

4. Send one of the defined HTTP requests while the created environment is selected.

# Testing on Broker Dashboard (Brokerdash)

## 0. Setting up Broker API on Brokerdash

### API Keys

When you sign up for an account at Alpaca you will receive an `API_KEY` and `API_SECRET`, please make sure you store those somewhere safe.

Broker API must authenticate using HTTP Basic authentication. Use your correspondent `API_KEY` and `API_SECRET` as the username and password. The format is key:secret. Encode the string with base-64 encoding, and you can pass it as an authentication header.

### Live Environment

We have provided in our dashboard an API tool that uses your API key credentials to send requests and receive responses straight from your browser.

Simply navigate to API/Devs > Live Testing and try out our APIs.

### Making Your First Request

At this point we can assume that you haven’t created any accounts yet, but one of the first API calls you can make is `GET /v1/assets`, which doesn’t require a request body and will give you all the assets available at Alpaca.

The response would contain an array of assets, with the first one being Agilent Technologies Inc. as of 2021-05-17

JSON

```
{
	"id": "7595a8d2-68a6-46d7-910c-6b1958491f5c",
	"class": "us_equity",
	"exchange": "NYSE",
	"symbol": "A",
	"name": "Agilent Technologies Inc.",
	"status": "active",
	"tradable": true,
	"marginable": true,
	"shortable": true,
	"easy_to_borrow": true,
	"fractionable": true
},
```

## 1. Create an Account

One of the first things you would need to do using Broker API is to create an account for your end user. Depending on the type of setup you have with Alpaca ([Fully-Disclosed](/docs/use-cases#fully-disclosed), [Omnibus](docs/use-cases#omnibus) or [RIA](/docs/use-cases#registered-investment-advisor-ria)) the requirements might differ.

Below is a sample request to create an account for a Fully-Disclosed setup:

JSON

```
{
    "contact": {
        "email_address": "[email protected]",
        "phone_number": "7065912538",
        "street_address": [
            "NG"
        ],
        "city": "San Mateo",
        "postal_code":"33345",
        "state":"CA"
    },
    "identity":      {   "given_name": "John",
        "family_name": "Doe",
        "date_of_birth": "1990-01-01",
        "tax_id_type": "USA_SSN",
        "tax_id": "661-010-666",
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
        "is_affiliated_exchange_or_finra": false,
        "is_affiliated_exchange_or_iiroc": false,
        "is_politically_exposed": false,
        "immediate_family_exposed": false
    },
    "agreements": [
        {
            "agreement": "customer_agreement",
            "signed_at": "2024-08-27T10:39:34+01:00",
            "ip_address": "185.11.11.11"
        },
            {
            "agreement": "options_agreement",
            "signed_at": "2024-08-27T10:39:34+01:00",
            "ip_address": "185.11.11.11"
        },
        {
      "agreement": "margin_agreement",
      "signed_at": "2020-09-11T18:09:33Z",
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
        "given_name": "xyz",
        "family_name": "wyz",
        "email_address": ""
    },
    "additional_information": "",
    "account_type": ""
}
```

If successful, the reponse would be

JSON

```
{
  "id": "b9b19618-22dd-4e80-8432-fc9e1ba0b27d",
  "account_number": "935142145",
  "status": "APPROVED",
  "currency": "USD",
  "last_equity": "0",
  "created_at": "2021-05-17T09:53:17.588248Z"
}
```

## 2. Fund an Account via ACH

### Creating an ACH Relationship

In order to virtually fund an account via ACH we must first establish the ACH Relationship with the account.

We will be using the following endpoint `POST /v1/accounts/{account_id}/ach_relationships` replacing the `account_id` with `b9b19618-22dd-4e80-8432-fc9e1ba0b27d`

JSON

```
{
  "account_owner_name": "Awesome Alpaca",
  "bank_account_type": "CHECKING",
  "bank_account_number": "32131231abc",
  "bank_routing_number": "121000358",
  "nickname": "Bank of America Checking"
}
```

Please make sure that the formatting for `bank_account_number` and `bank_routing_number` are in the correct format.

If successful you will receive an `ach_relationship` object like this:

JSON

```
{
  "id": "c9b420e0-ae4e-4f39-bcbf-649b407c2129",
  "account_id": "b9b19618-22dd-4e80-8432-fc9e1ba0b27d",
  "created_at": "2021-05-17T09:54:58.114433723Z",
  "updated_at": "2021-05-17T09:54:58.114433723Z",
  "status": "QUEUED",
  "account_owner_name": "Awesome Alpaca",
  "bank_account_type": "CHECKING",
  "bank_account_number": "32131231abc",
  "bank_routing_number": "121000358",
  "nickname": "Bank of America Checking"
}
```

Initially you will receive a `status = QUEUED`.

However, if you make a `GET/v1/accounts/{account_id}/ach_relationships`, after ~1 minute you should see `status = APPROVED`.

### Making a Virtual ACH Transfer

Now that you have an existing ACH relationship between the account and their bank, you can fund the account via ACH using the following endpoint `POST/v1/accounts/{account_id}/transfers` using the `relationship_id` we got in the response of the previous section.

JSON

```
{
  "transfer_type": "ach",
  "relationship_id": "c9b420e0-ae4e-4f39-bcbf-649b407c2129",
  "amount": "1234.567",
  "direction": "INCOMING"
}
```

The response you should get would look like this.

JSON

```
{
  "id": "750d8323-19f6-47d5-8e9a-a34ed4a6f2d2",
  "relationship_id": "c9b420e0-ae4e-4f39-bcbf-649b407c2129",
  "account_id": "b9b19618-22dd-4e80-8432-fc9e1ba0b27d",
  "type": "ach",
  "status": "QUEUED",
  "amount": "1234.567",
  "direction": "INCOMING",
  "created_at": "2021-05-17T09:56:05.445592162Z",
  "updated_at": "2021-05-17T09:56:05.445592162Z",
  "expires_at": "2021-05-24T09:56:05.445531104Z"
}
```

After around 10-30 minutes (to simulate ACH delay) the transfer should reflect on the user’s balance via a cash deposit activity (CSD) viewed via this endpoint `GET v1/accounts/activities/CSD\?account_id\={account_id}`

## 3. Journaling Between Accounts

In addition to transfer and funding via ACH and wire, we have enabled organizations to directly fund their Firm Accounts and then journal from those to user’s accounts in order to simulate near instantaneous funding.

### Introducing the Firm Account

Each team will come with a firm account in sandbox that is pre-funded for $50,000. You can use this account to simulate funding to your users or use it for rewards programs to fuel your app’s growth.

To illustrate our example, the Sweep account for this sandbox account looks like this

JSON

```
{
  "id": "8f8c8cee-2591-4f83-be12-82c659b5e748",
  "account_number": "927721227",
  "status": "ACTIVE",
  "currency": "USD",
  "last_equity": "45064.36",
  "created_at": "2021-03-03T17:50:06.568149Z"
}
```

### Journaling Cash

In the case of a signup reward, or simply attempting to simulate instant funding, journaling funds between your firm balance with Alpaca and the end user’s brokerage account is the best way.

You can simply pass in a request with `entry_type =JNLC` and choose the amount you want to journal to the user.

## 4. Passing an Order

The most common use case of Alpaca Broker API is to allow your end users to trade on the stock market. To do so simply pass in to `POST /v1/trading/accounts/{account_id}/orders` and again replacing the `account_id` with `b9b19618-22dd-4e80-8432-fc9e1ba0b27d`

JSON

```
{
  "symbol": "AAPL",
  "qty": 0.42,
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

Whatever the response from Alpaca would be (denoted by the status) you should receive an Order model in the response looking like this

JSON

```
{
  "id": "4c6cbac4-e17a-4373-b012-d446b20f9982",
  "client_order_id": "5a5e2660-88a7-410c-92c9-ab0c942df70b",
  "created_at": "2021-05-17T11:27:18.499336Z",
  "updated_at": "2021-05-17T11:27:18.499336Z",
  "submitted_at": "2021-05-17T11:27:18.488546Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "0.42",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "market",
  "type": "market",
  "side": "buy",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": null,
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0"
}
```

## 5. Events (SSE)

You can always listen to any event changes to accounts, journals or orders via our Events SSE.

An example for a journal update via this endpoint GET/v1/events/journal/updates where it shows all the different stages the journal id = 2f144d2a-91e6-46ff-8e37-959a701cc58d is going through.

```
data: {"at":"2021-05-07T10:28:23.163857Z","entry_type":"JNLC","event_id":1406,"journal_id":"2f144d2a-91e6-46ff-8e37-959a701cc58d","status_from":"","status_to":"queued"}

data: {"at":"2021-05-07T10:28:23.468461Z","entry_type":"JNLC","event_id":1407,"journal_id":"2f144d2a-91e6-46ff-8e37-959a701cc58d","status_from":"queued","status_to":"pending"}

data: {"at":"2021-05-07T10:28:23.522047Z","entry_type":"JNLC","event_id":1408,"journal_id":"2f144d2a-91e6-46ff-8e37-959a701cc58d","status_from":"pending","status_to":"executed"}
```

**You are now ready to explore more of Broker API!**

Have a look at our API References and feel free to contact us anytime through Intercom on your Broker Dashboard!

# Request ID

All Broker API endpoint provides a unique identifier of the API call in the response header with `X-Request-ID` key, the Request ID helps us to identify the call chain in our system.

Make sure you provide the Request ID in all support requests that you created, it could help us to solve the issue as soon as possible. Request ID can't be queried in other endpoints, that is why we suggest to persist the recent Request IDs.

Shell

```
$ curl -v https://broker-api.sandbox.alpaca.markets/v1/accounts
...
> GET /v1/accounts HTTP/1.1
> Host: broker-api.sandbox.alpaca.markets
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Date: Fri, 25 Aug 2023 09:10:03 GMT
< Content-Type: application/json
< Content-Length: 26
< Connection: keep-alive
< X-Request-ID: 65ddd35ed1b3433dbf29d11f6d932c88
<
...
```

Updated 5 months ago

---

What’s Next

Now Market Data supports Broker API  
Alpaca’s backoffice handling of Account Opening  
Alpaca’s Daily Processes

Ask AI

---

# Credentials Management (https://docs.alpaca.markets/docs/credential-management)

# Credentials Management

Authentication into the Broker API can be done through 2 different flows:

* [Client credentials](https://docs.alpaca.markets/docs/authentication#client-credentials-1) (recommended)
  + Client Secret
  + Private Key JWT
* [Legacy flow](https://docs.alpaca.markets/docs/authentication#legacy)

Both these flows offer access to expiration dates & fine-grained access control through BrokerDash.

## User Permissions

All user roles can view the credentials management page and see the list of existing API keys. However, only **superusers** have the ability to create new API credentials. This permission structure ensures proper access control while maintaining visibility of existing credentials for all team members.

## Credentials Expiration

To help enhance the security of your account and integration, all generated credentials can be assigned a specific expiration timeframe. This feature is a critical security control that automatically deactivates a key after a set period, limiting the risk associated with a key being compromised or forgotten.

![](https://files.readme.io/592650df55e6260de2b598524c2ac843eae8a4fe98841db15501f174834958f1-Filled.png)

The following options are available:

* Never
* 1 week
* 30 days
* 90 days
* 6 months
* 1 year
* Custom - select your own expiration date

## Fine-grained access control

When generating new API credentials, you have the option to define granular permissions using Access Controls. This feature is designed to enhance the security of your integration, while also allowing you to ensure a key only has the access required to perform its designated function.

You can choose from three distinct access control levels:

**Read only**: Grants permission to view data across all API scopes.

**Full access**: Grants permission to view and modify data across all API scopes.

**Custom**: Grants fine-grained, specific permissions for each API scope individually.

### Custom Access Controls

Instead of granting universal Read only or Full access, you can specify the access level for each distinct API scope.

For each API scope you can assign one of the following access levels:

**Read & Write**: Grants full permission to both view and modify data within that scope.

**Read only**: Grants permission to view data only.

**No Access**: Completely blocks all endpoints within that scope for this key.

![](https://files.readme.io/efe862a7f26305e37a6ce31cfa6a5e504e3e1f236b9c414f8a1bc0d2f3bd523a-Filled_Custom_Access_Controls.png)

You can choose one of the three custom access level for the following scopes:

* Accounts
* Funding
* Admin
* Crypto
* Rebalancing
* Trading
* Journaling
* Data
* Reporting
* SSE events

Updated 3 months ago

---

Ask AI

---

# Use Cases (https://docs.alpaca.markets/docs/use-cases)

# Use Cases

There are several different use cases for Broker API integration. Below are some common ones, but please do not hesitate to reach out to our sales team if you have a different case in mind. We want our platform to encourage a broad range of use cases.

* Broker dealer (fully-disclosed, omnibus)
* Registered Investment Advisor (RIA)

*We support most use cases internationally.*

Depending on the case, the API methods you want to use could vary. For example, the omnibus broker-dealer case never uses API to open a customer account since the trading accounts are created upfront and you will submit orders to them, and manage your end customer accounting on your end. More details on each use case are described in the following sections.

# Broker Dealer

## Fully-Disclosed

You are a registered broker-dealer in your jurisdiction and you introduce your customers to Alpaca to establish individual accounts on a fully-disclosed basis. Alpaca receives each customer’s information in order to open an account and provide our services.

Depending on your registration status and regulations in your jurisdiction, you may own the full end-to-end user experience from account opening, to trading, and reporting. You are responsible for maintaining a robust Customer Identification Program (CIP) and Know Your Customer (KYC) procedures, in accordance with Anti-Money Laundering (AML) regulations. To ensure compliance with applicable laws, Alpaca will conduct due diligence on your firm, including a thorough review of your CIP/KYC/AML program.

In this setup, you will use most of the API methods such as the Account, Transfer and Trading API. In addition, you can move cash and securities between your firm account and end-customer accounts using the Journal API to implement features such as reward programs.

## Omnibus

You are a registered broker-dealer and you manage customer accounting and one main trading account for the entire trading flow of your customers. In the omnibus setup, your end customer information (e.g. name, address) is not disclosed to Alpaca.

When submitting customer orders for your two trading accounts, you will indicate if the order is for the long or short position of each customer. To meet our regulatory requirements, you will be required to submit a “sub-tag” in each order to identify different customer’s order flow. This can be just an arbitrary text string such as UUID or a customer ID number. Alpaca, as well as our trading execution venues, need to be able to review and account for all trading activity. Failure to submit the required trading order flow information may result in the suspension of the entire order flow.

As each end customer is not disclosed to Alpaca, you are responsible for all tax reporting in your local jurisdiction. If you are a non-US broker-dealer, this will likely require registration with the IRS as a Foreign Financial Institution (FFI) and get certified as a Qualified Intermediary (QI) to be certified to manage taxes on the US-sourced income by foreigners.

# Registered Investment Advisor (RIA)

You are a SEC-registered RIA with customers either in or outside the US.

Similar to the Trading/Investing App approach described above, the end customer is introduced to Alpaca on an individual basis. The account approval process is owned by Alpaca, and you own the user experience and most of the communications. Unless you have a robust CIP/KYC/AML program in place that has been vetted by Alpaca, your customers will go through Alpaca’s CIP/KYC/AML process.

The Account API works slightly differently from the fully-disclosed case for this setup. Please see the rest of API documentation for more details.

As an RIA, you can communicate with your customers directly. Alpaca will work hand-in-hand with you to market your service using Broker API in a compliant manner.

Currently, Alpaca does not support order allocation and advisory fee calculation as built-in functionality. These items are on our roadmap.

Updated 5 months ago

---

Ask AI

---

# Integration Setup with Alpaca (https://docs.alpaca.markets/docs/integration-setup-with-alpaca)

# Integration Setup with Alpaca

If you are coming to Alpaca for the first time to build something using Broker API, please sign up for the dashboard. In this dashboard, you can acquire your API key for the sandbox environment and gain access to the test data immediately.

![](https://files.readme.io/6194f5d-image.png)

The sandbox behaves the same way as the live environment for the most parts with a few mocked. With this environment, you should be able to build a complete demo app that you can show to your friends, investors and other community members. Going live from here would be a matter of testing and updating the API calls for the mocked endpoints.

To go live, we will onboard you for the business integration. For more details of this step, please refer to [Going Live](/docs/integration-setup-with-alpaca#going-live).

Once you go live, you can keep using the same dashboard to view customer activity and resolve issues for them for both Sandbox and Live. You will also get support for the broker operations and technology support based on the agreement.

# Dashboard

Broker API users have access to a dashboard where you can view accounts and activities of your end users. You can sign up for an account with your email for free and get started with the sandbox API key.

You can invite team members to your account and view the same data as you make changes using API. You can switch the sandbox and live environment through this same dashboard. With all activity data, you can use this as your operation dashboard when going live as well.

You can assign different roles to each team member you invite.

![](https://files.readme.io/d4a3916-image.png)

# Sandbox

You have full access to the sandbox while developing your integration for free of charge. The sandbox is built with the same code as live with a few different behaviors.

## Account Approval

The account approval process slightly differs depending on your use case and you may need to test different scenarios in the sandbox first. The sandbox is fully automated with the account approval simulation with test fixtures, while the live environment may involve manual review and approval steps in some cases.

## Trading

All trades that happen in the sandbox environment are simulated. The simulator engine is the same as our paper trading engine. All assumptions and mock logic follow the paper trading behavior. Please refer to the [Trading API documentation](/docs/trading-api).

## Funding

The funding integration can vary depending on your country as well as the use case. In the sandbox environment, it is simplified with Transfer API. In order to simulate the deposit (credit) or withdrawal (debit) on the user account, simply call the POST method of Transfer API and it will become effective immediately. In the live environment, you may need to use Banks API as well as ACH endpoints if you are using ACH transfer within the USA. More details are described here.

## Journal Approval

When you make a Journal API request, if the amount exceeds the pre-configured limit amount, it goes into a pending status. In the live environment, Alpaca’s operation team is notified and manually reviews your request. In the sandbox environment, this process is simulated.

# Firm Accounts

A firm account is an account owned by your business for the purpose of operations. We could support a variety of accounts based on your needs. Here are some basic ones.

* Deposit Account: This is a deposit clearing account required for all clients going live. The exact amount required is based on the number of accounts and the number of trades. This account balance moves rarely.
* Sweep Account: This is the main firm account you will be using to journal funds between your firm and your users. It can be used to simulate instant funding, to provide intraday credit and many other flexible funding strategies.
* Rewards Account: This account can be used to trigger rewards you want to set up on your app to fuel growth such as sign up rewards, referrals rewards and achievement based rewards. This account supports both cash and stock rewards.

You can view your Firm Account balance from the Broker Dashboard along with all activities associated with the account.

# Going Live

Once you complete the sandbox integration, the next step is to go live. Please have another read about the differences between sandbox and live in the above section, and prepare for the go-live items. Generally speaking, we would need the following from you to open the live system for you.

* Your business entity documents, such as certificates of incorporation and tax ID
* Screenshots/video of your application interfaces
* KYC process document if you are fully-disclosed
* Expectation for the funding process if you already have something in mind

And with all this information provided, we will have a business agreement between you and Alpaca. We recommend allowing for enough time for the administrative tasks listed above, as we wouldn’t want to delay your production launch unnecessarily.

When launching into production, we recommend to start from alpha/beta launch with a limited access, to ensure the operation works well, both on your side and Alpaca’s side. Once the process is understood, you can go ahead with a full public launch. We are happy to consider participating in your PR / marketing launch!

Updated 5 months ago

---

Ask AI

---

# Broker API FAQs (https://docs.alpaca.markets/docs/broker-api-faq)

# Broker API FAQs

Frequently Asked Questions

# Broker API vs. Trading API

### What is the Difference Between Trading API and Broker API?

The Broker API is meant to support different use cases for Broker-Dealers, RIAs, and Trading/Investing applications, [see more here](https://docs.alpaca.markets/docs/use-cases).

Instead, the Trading API is meant for Retail users and algotraders to communicate with Alpaca’s brokerage service, [see more here](https://alpaca.markets/docs/api-references/trading-api/).

### Is the Authentication Different Between Trading API and Broker API?

Yes, the way a client authenticates with the Broker API is different than the Trading API.

With the Broker API, you’ll need to encode the keys and pass an authentication header that looks like this:

`Authorization: Basic <base64 encoded keys>`

[see more here](https://alpaca.markets/docs/api-references/broker-api/#authentication-and-rate-limit).

The same Broker API credentials with HTTP basic authentication can be used to access Market Data API, as described [here](https://docs.alpaca.markets/docs/about-market-data-api#broker-api).

# Accounts

### When Do the Values on the Accounts Trading Get Updated?

All the values that **do not** have the prefix - “last\_“ are updated Real-Time post trade executions and Corp Action activities. Might update outside market hours as well, post-trade settlements and FEE calculations like REG/TAF fee.

# Assets

### What is the difference between Tradable and Status Boolean in the Assets API?

### [Assets](https://alpaca.markets/docs/api-references/broker-api/assets/#asset-states)

There are some scenarios to consider here:

#### `tradable=true` and `status=active`

This is the scenario for most of the stocks listed. For example Apple Inc. This means it's tradable - both BUY and SELL are possible on this stock.

#### `tradable=false` and `status=active`

This is one of the rare conditions where we don't allow new opening transactions and only allow closing transactions. This usually happens when an asset is delisted from a US stock exchange and trades over the counter.

#### `tradable=false` and `status=inactive`

This is a scenario which can be achieved during the delisting of a company. If a stock is delisted, it is not tradable, which means we neither allow a `BUY` nor a `SELL` order for that particular stock. A delisted stock is either auto-liquidated or users are informed to close the positions within a specific amount of time.

### Can OTC tickers be traded?

Yes, you can always close any open positions.

### Are OTC symbols available in the Market Data?

No. OTC Market Data requires partners to directly have an agreement with OTC Markets. Once that is done, we can enable the same for our partners.

### Is there a way to differentiate between Stocks and ETFs in the Assets API?

Alpaca at this point in time does not support any categorization of Stocks and ETFs. Partner needs to categorize them personally using the names and symbols.

### How often does Alpaca refresh the assets master?

Alpaca refreshes the assets master 3 times per day. The 3 refresh times are outside of market hours, with the last refresh scheduled at 8:20 AM ET. If you are storing the list of assets locally, we recommend refreshing it from Alpaca at least once per day, preferably after 8:20 AM ET but before 9:30 AM ET.

# Events

### How Many SSE Connections Can be Alive Concurrently?

A maximum of **25** connection requests are allowed. Post that you will receive *“Too many requests“* error.

### After How Long Will the SSE Connection Close?

There is no such time. Alpaca would never stop responding, hence we also send “*heartbeat*“ to let partners know that the connection is alive. Sometimes the connections are un-knowingly closed by client-networks or network error happens. Nonetheless, you can always re-open and request data after a particular event using `since_id` or `since`.

### What is the Use-case for SSE?

Server-sent events can be useful when you want updates on the status of a certain transaction, without making multiple HTTP requests. Events endpoints will return multiple responses when you open a connection, and can also be used in a restful way to make sure you didn’t miss any event.

1. Account Status Updates - [Subscribe to Account Status Events (SSE)](https://docs.alpaca.markets/reference/suscribetoaccountstatussse)
2. Trade Updates - [Subscribe to Trade Events (SSE)](https://docs.alpaca.markets/reference/subscribetotradesse)
3. Journal Updates - [Subscribe to Journal Events (SSE)](https://docs.alpaca.markets/reference/subscribetojournalstatussse)
4. Any Transfer Event - [Subscribe to Transfer Events (SSE)](https://docs.alpaca.markets/reference/subscribetotransferstatussse)
5. Any relevant Non-Trading Activity - [Subscribe to Non-Trading Activities Events (SSE)](https://docs.alpaca.markets/reference/get-v1-events-nta)

# Market Data

### Does the Market Data API support corporate actions adjustments?

Yes, price adjustments are visible on the Market Data, you'll just need to make sure the adjustment parameter is set to all. The available query parameters for bars are available here - [Historical bars](https://docs.alpaca.markets/reference/stockbars#:~:text=adjustment,for%20the%20stocks.)

### Does the Market Data API support local currencies?

Yes. You can retrieve historical market data in the supported local currencies.

# Documents

### How are trade confirmations and account statements handled by Alpaca and its partners?

1. Both of them need to be mailed to users with [[email protected]](/cdn-cgi/l/email-protection#402135342f6d213223282936256d2224002d21292c25326e212c302123216e2d21322b253433) in BCC.
2. The email should contain the truncated alpaca account number and language as mentioned in the Statement and Confirms Document.
3. If sharing a customized statement or confirmation, in that case, the partner must allow users to have access to the original statements and confirms generated by Alpaca.

### When are these documents available?

Daily Trade Confirmations are available on the next day after the BOD job is finished(02:15 AM-02:30 AM EST).

Monthly statements are available after the 1st weekend of the next month.

### How can I retrieve these documents?

[Documents | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/documents/#retrieving-documents-for-one-account)

Query the above-mentioned endpoint with `type` as `account_statement` or `trade_confirmation`.

### Can I find a sample W-8 Ben Form and what details are needed to be filled in?

Can be found here -

### I’m getting a 400 error (request body format is invalid: JSON: cannot unmarshal object into Go value of type entities.BrokerAccountDocumentUploads) when uploading a W8-Ben. Is this expected?

Yes, the body of the request is an array of documents, make sure you’re using square brackets like in the sample response [Documents | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/documents/#sample-request).

# Journals

### How much time does JNLC’s or Journal usually take?

Most of the time, JNLCs are pretty fast and mostly instantaneous, with a sub-second average delay before the execution is complete.

There can be a delay of a few hours when exceeding the limits mentioned below.

### JNLC with larger amounts are executed the next day. Is this expected?

Yes. We have a limit called the JNLC Transaction Limit. This is the maximum amount of journaling you can do instantaneously. Any amount of journal greater than this would be executed as a part of the BOD job of the next day. The default value is $50.

This is a safeguard mechanism to prevent LARGE withdrawals for any user to prevent partners from the same. This is a “Configurable“ value that can be set to anything on the Sandbox but would require a discussion for the PROD.

There is also a JNLC Daily Limit, which is the summation of all the JNLC done in a day. If the limit is $1000(Default Limit), you can do 10 transactions of $100 each, but the 11th one would not pass. This is a “Configurable“ value that can be set to anything on the Sandbox but would require a discussion for the PROD.

### Can I subscribe to a journal status streaming without having to check it again and again?

Absolutely yes. You can listen to the journal server-sent events. - [Events | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/events/#journal-status)

## What are the use cases for the JNLS?

JNLS are usually used to Reward users for signing up on the platform by our partners.

## What is the direction and flow of JNLS?

JNLS can ONLY be done from the SWEEP ACCOUNT to the USER ACCOUNT and not vice-versa. Once, done, it can’t be sent back.

## Is the JNLS transactional limit per account configurable?

Yes, they are configurable.

## Are JNLS transactional limits per account USD or Stocks based?

They are USD-based.

# Trading

## Orders

### What is the minimum order value?

All buy orders must have a minimum market value of 1$ or the request will be rejected with a 422. Sell orders do not have this validation, so you can close any open position.

### What is the precision for notional and qty in the order request body?

A maximum of **2 decimal places** for *notional* and **9 decimal places** for *qty* should be used to send orders.

### Only limit is allowed as the order type for OCO. Does this rule apply to OTO?

No. OCO implements an order cancellation and hence it might be very difficult to cancel a market order. Whereas in the case of OTO, that isn't an issue and hence *market* and *limit* both orders are allowed!

### Order replacement is supported for OCO to update limit\_price and stop\_price.

Can we update the quantity as well? And can we use a notional amount instead of quantity?

Yes, you can update the quantity while patching the order using this API - [Orders | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/trading/orders/#patching-an-order) .

No, you can't use the notional amount. The reason for this is, that Alpaca at this point of time **doesn't** support *LIMIT* orders for *notional* orders and since OCO orders can only be a *LIMIT* order, it makes it compulsory to use the **quantity**.

### What orders can be cancelled?

We check that the order is in an "open" status before attempting to cancel it.
The [statuses](https://alpaca.markets/docs/trading/orders/#order-lifecycle "https://alpaca.markets/docs/trading/orders/#order-lifecycle") that we consider open are:

* Accepted
* New
* Partially Filled
* Calculated
* Pending New
* Pending Cancel
* Accepted for Bidding

If the order is in one of these statuses you should receive a 204 (unless there was a server error) while if it isn't you're going to receive a 422, as mentioned in the docs.
To check if the order was actually canceled, I suggest you check its status on the trades SSE or through the REST endpoints.

## Trade Settlement

### Why is there no cash\_withdrawable and cash\_transferable increase after selling a stock?

Settlement occurs one business day after the day the order executes, or T+1 (trade date plus one business day). For example, if you were to execute an order on Monday, it would typically settle on Tuesday. The `cash` is updated post the SELL trade is filled, but the `cash_withdrawable` and `cash_transferable` are updated post T+1.

### What are some fees, that can be expected while trading stocks?

#### REG and TAF Fees

This is charged(REG and TAF individually) to a User Account, every time a SELL Order is executed. This is charged by Alpaca but, is a pass thru fee from the FINRA and SEC itself that is levied to Alpaca on sell orders. The REG and TAF fees change rates periodically. More about this can be read in the blog from our co-founder - [REG/TAF Fee Updates with Alpaca](https://alpaca.markets/blog/reg-taf-fees/)

#### ADR Fees

Most ADRs charge a fee of $0.01 to $0.03 per share once or twice a year in order to cover the administrative costs associated with running the ADR program. ADR fees may be charged less frequently depending on how the depository bank runs the ADR program.

ADR fees are charged to clients typically once a month after we are charged by our depository.
The record date on the charge is usually the month before the actual date of the charge. Even if the client has since liquidated their shares, they will still be charged an ADR fee if they held shares on the record date.

#### Rounding rules

We will not charge the ADR fee if the calculated fee is less than a penny. However, if the amount is over a penny we will always round up to the next highest penny. For example, if the charge is .02 cents a share and the client owns 10.1 shares we would charge the client .21 for the ADR fee.

# Rebalancing

### Can I enter manual trades while using the Rebalancing API?

If the account is subscribed to a portfolio, it cannot execute manual trades or [manual rebalance runs](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#create-run-manual-rebalancing-event "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#create-run-manual-rebalancing-event"). Still, you can [delete the subscription](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#unsubscribe-account-delete-subscription "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#unsubscribe-account-delete-subscription") to execute manual trades or rebalance runs.

### How can I see the orders triggered by a rebalancing event?

You can easily retrieve [all the runs with this endpoint](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#list-all-runs "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#list-all-runs") or [a particular run by its ID](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#get-run-by-id "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#get-run-by-id"), where each run will have an array with all the orders that were executed and the ones that failed or were skipped.

# Important Links and Reads

1. Alpaca Daily Processes and Reconciliations - [Daily Processes and Reconcilations](https://docs.alpaca.markets/docs/daily-processes-and-reconcilations)
2. PDT - [User Protection](https://docs.alpaca.markets/docs/user-protection#pattern-day-trader-pdt-protection-at-alpaca)
3. Margins - [Margin and Short Selling](https://docs.alpaca.markets/docs/margin-and-short-selling)
4. Understanding Orders and Time in Force - [Orders at Alpaca](https://docs.alpaca.markets/docs/orders-at-alpaca)

---

##### Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.

##### This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered (Alpaca Securities is registered only in the United States).

Updated 5 months ago

---

Ask AI

---

# Mandatory Corporate Actions (https://docs.alpaca.markets/docs/mandatory-corporate-actions)

# Mandatory Corporate Actions

Frequently Asked Mandatory Corporate Action Questions

# Mandatory Corporate Actions

### What are the most common corporate actions Alpaca handles, and what are they?

* **Dividends** - Dividends are payments made by companies to shareholders to account for their share of profits made by the company. The usual timeline for dividend payments is quarterly payments, but this is fully dependent on the companies themselves. There are 3 main types of dividends; a brief overview of each is added below:
* **Cash** - Cash dividends are when companies pay out cash to their shareholders to account for their profits.
* **Stock** - Stock dividends are when companies pay out stock to their shareholders to account for their profits.
* **SPLITs** - Splits are events in which a company changes its number of shares, either by splitting a share into multiple shares, or combining multiple shares into 1. In both events, the quantity that a user owns in a stock will be affected and updated according to the SPLIT ratio.
  + **Forward** - A forward split is when the company splits 1 share into multiple shares, resulting in a lower price per share.
  + **Reverse** - A reverse split is when the company combines multiple shares into 1 share, resulting in a higher price per share.
* **SPIN** - Spinoffs occur when a company provides its shareholders shares in a subsidiary or business division. Clients will continue to hold original shares and cost basis may be adjusted due to the new spin off security.
* **Mergers** - A merger is when 2 companies join to become 1 new company.  
  For the explanations below, assume company A and company B are participants in a merger, with company B being the larger of the 2 companies. Company A is being merged into company B.
  + **Stock Merger** - This is when a shareholder of a company receives shares in another company due to the participation in a merger. For example, company B allocates 2 shares of B to a shareholder in company A after the merger is done.
  + **Cash Merger** - This is when the shareholders of a company receive cash due to participation in a merger. For example, company B pays 100$ to a shareholder in company A after the merger is done.
  + **Stock and Cash Merger** - This is when the shareholders of a company receive both stock & cash due to participation in a merger. For example, company B allocates 2 shares of B & pays 100$ to a shareholder in company A after the merger is done.
* **Full Call** - This is when the shareholders of a company receive cash due to the company exercising their right to purchase shares from shareholders. This is usually done on preferred shares.
* **Final Liquidation** - This is when the shareholders of a company receive cash and the underlying shares are removed. This is usually done on SPACs or securities such as CVRs and escrow shares.
* **Partial Liquidation** - This is when the shareholders of a company receive cash, but the underlying shares continue to be held in anticipation of potential future distributions. This is usually done on securities such as CVRs and escrow shares.
* **NC** - A name change occurs when a company changes its legal name, regardless of the reason behind the change. When this happens, the underlying asset might be affected in multiple ways:
  + **Symbol change** - This is when the symbol of the underlying asset changes as part of the name change event.
  + **CUSIP change** - This is when the CUSIP of the underlying asset changes as part of the name change event.
  + **Symbol & CUSIP change** - This is when both the symbol & CUSIP of the underlying asset change as part of the name change event.  
    Note: There might also be no change in either CUSIP or symbol, in which case the update to the asset will occur without triggering an NC event.

**Examples** of each type of Mandatory Event above are available in the docs [here](https://docs.alpaca.markets/docs/draft-sse-events#non-trade-activities-events).

---

### Which of all the dates in the response body should we use in each transaction detail?

Settle date.

---

### How does Alpaca handle stock-and-cash mergers?

Stock and cash mergers are mandatory events, so they are handled like all other mandatory events.

---

### For stock and cash mergers, what would we receive as NTAs?

You should receive 3 NTA events:

* 1 for the removal of the original security
* 1 for the allocation of new shares
* 1 for the allocation of cash

A sample is added below. This was a stock-and-cash merger with 5 shares of `384CVR015` and `$9.95` allocated for every `1 share` of `GRCL`:

**Removal of original security:**

json

```
{  
    "id": "",  
    "qty": -284.678660686,  
    "price": 6.04,  
    "status": "correct",  
    "symbol": "GRCL",  
    "entry_type": "MA",  
    "net_amount": 0,  
    "description": "Stock Merger 5 384CVR015 for 1 GRCL",  
    "settle_date": "2024-02-29",  
    "system_date": "2024-02-29",  
    "per_share_amount": null  
}
```

**Allocation of new shares:**

json

```
{  
    "id": "",  
    "qty": 1423.39330343,  
    "price": 1.21,  
    "status": "correct",  
    "symbol": "384CVR015",  
    "entry_type": "MA",  
    "net_amount": 0,  
    "description": "Stock Merger 5 384CVR015 for 1 GRCL",  
    "settle_date": "2024-02-29",  
    "system_date": "2024-02-29",  
    "per_share_amount": null  
}
```

In the removal & allocation of shares events, the quantity field represents the number of shares removed or allocated.

**Allocation of cash:**

json

```
{  
    "id": "",  
    "qty": 0,  
    "price": null,  
    "status": "executed",  
    "symbol": "GRCL",  
    "entry_type": "MA",  
    "net_amount": 2832.55,  
    "description": "Stock Cash Merger 5 384CVR015 and $9.95 for 1 GRCL",  
    "settle_date": "2024-02-29",  
    "system_date": "2024-02-29",  
    "per_share_amount": null  
}
```

In the cash events, `net_amount` will reflect the cash amount allocated.

---

### At a user level, are cash mergers always for 100% of the position, or are there cases where a user might keep 50% of their position and receive cash for the remaining 50%?

On a stock and cash merger, all shares of the old security are removed. The new stock and cash allocation are based on a ratio determined by the company based on current market conditions.

---

### Does Alpaca handle recapitalization?

Alpaca does not currently handle debt instruments. Recapitalization events deal with debt instruments and, accordingly, are not available on Alpaca.

---

### How does Alpaca handle tax withholding?

We receive a net rate per share from DTC based on the country of the company.

1. If it is a foreign company, then there may be a foreign dividend withholding tax that is withheld from the payment we receive from DTC. This payment would represent the `DIV` NTA entry.
2. With a foreign partner, there may be an additional withholding (the `DIVNRA` entry) based on their country and the withholding percentage for that country. If the company that paid the dividend has a tax exempt foreign status, then the `DIVNRA` entry may not apply.

In summary, you would receive a `DIV` event (the dividend) and a `DIVNRA` (the tax withholding) event. Noting that if a `DIVNRA` value is `< 0.01`, however, you will not receive a `DIVNRA` activity.

---

### Are there any cases where Alpaca does not withhold taxes on dividends?

If the company is a foreign company, then there may not be any `DIVNRA` withholdings

---

### Does the amount sent in the DIV event include the tax? In other words, to calculate the final amount, the amount in the DIVNRA event needs to be deducted from the amount on DIV event.

Yes, the amount sent in the `DIV` event is without the tax `DIVNRA`, so you need to determine the net amount after the `DIVNRA` by taking the `DIV` and reducing it by the `DIVNRA`.

---

### Are symbol changes notified via the SSE Events?

No, as of now the symbol changes need to be seen via the [Assets API](https://docs.alpaca.markets/reference/getassets "https://docs.alpaca.markets/reference/getassets"). Syncing at regular intervals is what is recommended to make sure you are up-to-date with the symbol changes.

---

### Do we have a new asset object, if there is a symbol change?

The answer is a YES and a NO. The reason for that is, if there is simply a symbol change without the CUSIP being updated, in that case, we just update the existing asset by updating the Symbol. If there is a CUSIP change, the current asset becomes INACTIVE and a new Asset Object is added the the response of the [Assets API](https://docs.alpaca.markets/reference/getassets "https://docs.alpaca.markets/reference/getassets").

---

### What happens when a stock split occurs?

For reverse splits all GTC orders will be canceled that were in the market with a trade date prior to the effective date of the reverse split.  
For forward splits, GTC buy limits and sell stops are adjusted. The price and quantity will be adjusted. Other orders will not be adjusted.

Please note that this piece is for general informational purposes only. The examples above are for illustrative purposes only. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.

Updated 5 months ago

---

Ask AI

---

# Voluntary Corporate Actions (https://docs.alpaca.markets/docs/voluntary-corporate-actions)

# Voluntary Corporate Actions

Frequently Asked Voluntary Corporate Action Questions

# Voluntary Corporate Actions

### How are voluntary corporate actions communicated to customers?

Alpaca works with a third party vendor to communicate voluntary corporate actions. Emails are sent to each customer when there is a voluntary corporate action with details and instructions on how to take action. These emails will have the broker partner name on them with an option to add a logo.

---

### Can we block all voluntary actions such as rights distribution?

No, those have to be sent to customers. There is a cost associated with these, which usually deters customers from acting on them. The cost is $100 per client per voluntary corporate action, which is stated in the email. Alpaca can reject a customer's decision to act if there is no cash in the account, which would be the case here.

---

### Why is there a field ‘qty’ that is != 0 in change name response body?

CUSIP change, symbol change, or a combination of both lead to this happening. Basically, there are two NC event the qty will be negative to remove the old symbol and positive when adding the new one.

---

### What are the possible voluntary actions?

* **Dutch Auction/Purchase/Tender Offer:** This is when a company wants to purchase your shares at a specific price or when they ask you to choose the price at which you would be willing to sell your shares.
* **Conversion/Exchange Offer:** This is when a company offers to exchange your shares for a new type of in-kind share like bonds or fixed income securities.
* **Election Merger:** This is when a company offers to pay cash, new shares, or a combination of both for your currently held shares.
* **Consent Request:** This is when a company usually asks for your permission, as a bondholder, to change the bond agreement.
* **Rights Offer:** This is when a company offers to sell you new shares (typically below the market price) before they offer these shares publicly.
* **Warrant Exercise:** This is when a company offers to sell you new shares at a specific exercise price. Expirations can be up to 5 years in the future.

---

### What are unit splits, and how does Alpaca handle them?

* Units are a type of security that usually contain a combination of common shares and warrants. Rights may also be included, but this is less common.
* Unit Splits can be either a mandatory event or a voluntary event
  + For a mandatory event
    - Clients will receive a combination of common shares and warrants based on the unit split ratio; no action is needed by the client
    - The REORG entry type will be used for this event
  + For a voluntary event
    - Clients can choose whether or not to split their units as long as the agent window is open to perform the unit split.
    - We don't usually have a lot of clients trading units, but as long as the window is open for a unit split, a Partner can request one at any time. This will have the $100.00 voluntary submission fee attached to it.
    - The VOF entry type will be used for this event

---

### How are voluntary corporate actions processed at Alpaca?

On Alpaca's end, voluntary corporate actions use 3 main NTA activity types: VOF, REORG, and FEE:

* `VOF` is used when there is a change in shares.
* `REORG` is used when there is a change in cash.
* `FEE` is used to book the fee associated with a VCA.

The general process at Alpaca to handle voluntary corporate actions is as follows:

1. The client's underlying shares are moved to a contra/placeholder security; this way, they don't liquidate the shares that were elected
   * This would be done with 2 `VOF` entries (1 to remove underlying shares and 1 to allocate contra)
2. Once we receive the allocation from DTC (which is normally a week or two after the client's election is submitted), we will then remove the contra security and allocate the voluntary payment (cash or new shares usually)
   * If they are receiving cash; there would be 1 `VOF` entry to remove the contra shares and 1 `REORG` entry to allocate the cash
   * If they are receiving new shares; there would be 2 `VOF` entries to remove the contra shares and allocate the new shares

Below are the different offer types and the standard Alpaca NTAs that would be created for them, noting that there might be slight differences on a case by case scenario:

* **Purchase/Tender offer** - explained [here](https://www.investopedia.com/terms/t/tenderoffer.asp), would be a combination of:
  + 3 `VOF`
    - Remove the underlying shares
    - Allocate contra shares
    - Remove the contra shares when we receive payment from DTC
  + `REORG` to allocate the cash to the client when we receive payment from DTC
  + `FEE` Entry
* **Exchange offer** - explained here, would be a combination of:
  + 4 `VOF`
    - Remove the underlying shares
    - Allocate contra shares
    - Remove the contra shares when we receive payment from DTC
    - Allocate the new shares when we receive payment from DTC
  + `FEE` Entry
* **Rights/Warrant offer** - explained here, would be a combination of:
  + Either 2 `VOF`
    - Distribution of the rights
    - Exercise the rights
  + OR 4 `VOF` (if there is a move to Contra needed similar to the previous cases)
  + 2 `FEE` Entries.
  + There might also be an additional `REORG` (for mandatory events like a worthless removal).
* **Consent request** - Doesn't apply

## Sample NTAs

Some sample NTAs that you would receive for the offer types mentioned above are added for reference:

### Sample Purchase/Tender Offer

`MNST` shares removed with a `VOF` entry

json

```
{  
  "id": "f2ad14c5-f46b-47bd-b6cc-422dd535f086",  
  "qty": -97,  
  "price": null,  
  "status": "executed",  
  "symbol": "MNST",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Monster Beverage voluntary submission (expiration 06/05/24)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

`611NSP014` (the contra security) was allocated with a `VOF` entry

json

```
{  
  "id": "221e1a62-5e43-4288-b320-0921c6bc56cb",  
  "qty": 97,  
  "price": null,  
  "status": "executed",  
  "symbol": "611NSP014",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Monster Beverage voluntary submission (expiration 06/05/24)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

`611NSP014` was removed with a `VOF` entry after allocation was received from DTC

json

```
{  
  "id": "aeb0dc92-1197-4c33-96f6-2545b43d37c6",  
  "qty": -97,  
  "price": null,  
  "status": "executed",  
  "symbol": "611NSP014",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Monster Beverage voluntary allocation (expiration 06/05/24)",  
  "settle_date": "2024-06-12",  
  "system_date": "2024-06-12",  
  "per_share_amount": null  
}
```

Cash was allocated to the client using a `REORG` entry

json

```
{
  "id": "6c452d1f-bcec-4300-b857-faae17f8624e",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "611NSP014",
  "entry_type": "REORG",
  "net_amount": 5141,
  "description": "Monster Beverage voluntary allocation (expiration 06/05/24)",
  "settle_date": "2024-06-12",
  "system_date": "2024-06-12",
  "per_share_amount": null
}
```

Fee was booked using a `Fee` entry

```
{  
  "id": "2af9d6d2-c1bd-49f1-a9df-6d14a13f4af5",  
  "qty": 0,  
  "price": null,  
  "status": "executed",  
  "symbol": "",  
  "entry_type": "FEE",  
  "net_amount": -100,  
  "description": "Monster Beverage Voluntary Submission Fee (expiration 06/05/24)",  
  "settle_date": "2024-06-12",  
  "system_date": "2024-06-12",  
  "per_share_amount": null  
}
```

### Sample Exchange Offer

`CMI` Shares were removed using a `REORG` entry

```
{  
  "id": "7642d450-69d0-4d7e-87e0-62b0b94a3097",  
  "qty": -99,  
  "price": null,  
  "status": "executed",  
  "symbol": "CMI",  
  "entry_type": "REORG",  
  "net_amount": 0,  
  "description": "Voluntary Tender Election for Cummins, Inc. (CMI)",  
  "settle_date": "2024-03-12",  
  "system_date": "2024-03-12",  
  "per_share_amount": null  
}
```

`231992017` (the contra security) was allocated with a `REORG` entry

json

```
{  
  "id": "c163bd41-c9d7-4204-816e-1b8bd98091df",  
  "qty": 99,  
  "price": null,  
  "status": "executed",  
  "symbol": "231992017",  
  "entry_type": "REORG",  
  "net_amount": 0,  
  "description": "Voluntary Tender Election for Cummins, Inc. (CMI)",  
  "settle_date": "2024-03-12",  
  "system_date": "2024-03-12",  
  "per_share_amount": null  
}
```

Fee was booked using a `Fee` entry

json

```
{  
  "id": "d9a91441-558a-41f9-8926-bd9446308c58",  
  "qty": 0,  
  "price": null,  
  "status": "executed",  
  "symbol": "",  
  "entry_type": "FEE",  
  "net_amount": -100,  
  "description": "Voluntary Tender Election for Cummins, Inc. (CMI) Fees",  
  "settle_date": "2024-03-12",  
  "system_date": "2024-03-12",  
  "per_share_amount": null  
}
```

`231992017` (the contra security) shares were removed using a `VOF` entry

```
{  
  "id": "58259fb2-973b-407d-8e18-e7080ae65bdc",  
  "qty": -99,  
  "price": null,  
  "status": "executed",  
  "symbol": "231992017",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Voluntary Tender Payment for Cummins, Inc. (CMI)",  
  "settle_date": "2024-03-20",  
  "system_date": "2024-03-20",  
  "per_share_amount": null  
}
```

`ATMU` shares were allocated with a `VOF` entry

json

```
{  
  "id": "04226589-e3a5-43fd-a69e-dbda35546b3e",  
  "qty": 1190,  
  "price": 22.33,  
  "status": "executed",  
  "symbol": "ATMU",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Voluntary Tender Payment for Cummins, Inc. (CMI)",  
  "settle_date": "2024-03-20",  
  "system_date": "2024-03-20",  
  "per_share_amount": null  
}
```

### Sample Rights Offer

`FEE` for the new shares:

json

```
{  
  "id": "f71b410e-b9c4-4071-b627-f5ea92633e89",  
  "qty": 0,  
  "price": null,  
  "status": "executed",  
  "symbol": "",  
  "entry_type": "FEE",  
  "net_amount": -2125,  
  "description": "Barnes & Noble Rights Exercise Cost (067RGT019)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

DTC Fee

json

```
{  
  "id": "8c82a56a-7602-4a83-977b-aafd1cea3db8",  
  "qty": 0,  
  "price": null,  
  "status": "executed",  
  "symbol": "",  
  "entry_type": "FEE",  
  "net_amount": -100,  
  "description": "Barnes & Noble Rights Exercise Submission Fee (067RGT019)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

`VOF` to remove underlying security

json

```
{  
  "id": "47007871-2f92-4adf-b7dc-efc6b1550fe7",  
  "qty": -2500,  
  "price": null,  
  "status": "executed",  
  "symbol": "067RGT019",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Rights Exercise (symbol BNED; expiration 06/05/24)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

`VOF` to allocate contra security

json

```
{  
  "id": "01233557-9f6b-403f-8832-6b70f057d85c",  
  "qty": 2500,  
  "price": null,  
  "status": "executed",  
  "symbol": "067BAS012",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Rights Exercise (symbol BNED; expiration 06/05/24)",  
  "settle_date": "2024-06-05",  
  "system_date": "2024-06-05",  
  "per_share_amount": null  
}
```

`VOF` to remove contra security

json

```
{  
  "id": "42830cc1-2dfb-4d6f-959b-463c148774ac",  
  "qty": -2500,  
  "price": null,  
  "status": "executed",  
  "symbol": "067BAS012",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Rights Payment (symbol BNED; expiration 06/05/24)",  
  "settle_date": "2024-06-11",  
  "system_date": "2024-06-11",  
  "per_share_amount": null  
}
```

`VOF` to allocate new shares

json

```
{  
  "id": "43eb77dd-1b8c-4b3d-81b1-647a00436aa3",  
  "qty": 42500,  
  "price": 0.09,  
  "status": "executed",  
  "symbol": "BNED",  
  "entry_type": "VOF",  
  "net_amount": 0,  
  "description": "Rights Payment (symbol BNED; expiration 06/05/24)",  
  "settle_date": "2024-06-11",  
  "system_date": "2024-06-11",  
  "per_share_amount": null  
}
```

In this case, there was also an extra `REORG` due to a mandatory event (worthless removal)

json

```
{  
  "id": "89f26a95-2624-43ab-a95c-a17db20dc361",  
  "qty": -150,  
  "price": null,  
  "status": "correct",  
  "symbol": "067RGT019",  
  "entry_type": "REORG",  
  "net_amount": 0,  
  "description": "Worthless Removal - 067RGT019",  
  "settle_date": "2024-06-13",  
  "system_date": "2024-06-13",  
  "per_share_amount": null  
}
```

Please note that this piece is for general informational purposes only. The examples above are for illustrative purposes only. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.

Updated 5 months ago

---

Ask AI

---

# FDIC Sweep Program (https://docs.alpaca.markets/docs/fdic-sweep-program)

# FDIC Sweep Program

### What is an FDIC Sweep program?

An FDIC Bank Sweep Program, is an insured deposit program that allows customers who opt-in to earn interest on eligible cash balances and offers expanded FDIC insurance coverage on those cash balances\*.

### How does FDIC sweep work?

Through the Alpaca FDIC Bank Sweep Program, eligible uninvested cash in a customer brokerage account can be swept to one or more of the participating [FDIC Sweep Program Banks](https://alpaca.markets/deposit-bank-list), where the swept cash becomes eligible for FDIC insurance up to a total maximum of $1,000,000 (FDIC insurance coverage is limited to $250,000 at each program bank)\*.

### How much is insured?

Currently FDIC insurance up to a total maximum of $1,000,000 (FDIC insurance coverage is limited to $250,000 at each program bank)\*.

### What are the eligibility requirements?

1. Partners must be using a fully disclosed structure (not available to Partners with an omnibus structure at launch).
2. A customer must elect to opt-in their account into the program:  
   *Existing:* Customers with an existing Alpaca account that have signed a Customer Agreement before August 21, 2024 (prior to revision 22.2024.08) must provide opt-in consent by signing the updated Customer Agreement and be presented the [Alpaca FDIC Bank Sweep Program Terms and Conditions](https://files.alpaca.markets/disclosures/Alpaca+FDIC+Bank+Sweep+Program+Terms+and+Conditions.pdf) on your front-end. Our Tech Integration team will help walk you through that process and the requirements.  
   *New:* Those who signed the Customer Agreement on or after August 21, 2024 (revision 22.2024.08 or newer) are automatically eligible to be enrolled.
3. The customer account is not flagged as a pattern day trader (PDT).

If an account is flagged as a PDT while enrolled in the FDIC Bank Sweep Program, it will be unenrolled from the program, and its sweep balance will be swept back from the program. Any accrued interest due will be paid, but no additional interest will be accrued unless the PDT flag is removed and the account is re-enrolled in the program by assigning an APR Tier.

4. The customer account has a base currency of USD.
5. The customer account is pre-funded (i.e., non-JIT).

### How does a user enroll?

Please see our blog article [Getting Started with High-Yield Cash for Broker API](https://alpaca.markets/learn/getting-started-with-high-yield-cash-for-broker-api)

### How can a user opt-out of the FDIC Sweep Program?

To opt-out a user from the Alpaca FDIC Bank Sweep Program, please email [[email protected]](/cdn-cgi/l/email-protection#a5d6d0d5d5cad7d1e5c4c9d5c4c6c48bc8c4d7cec0d1d6).

### What account types are supported?

We are currently supporting Individual Taxable and Custodial accounts at this time.

### What are the benefits of a user enrolling?

*Income:* Earn interest on eligible cash balances  
*Security:* Up to $1m FDIC insurance\* per customer via FDIC Bank Sweep  
*Liquidity:* Daily liquid, and available for use as buying power for trading activities

<https://alpaca.markets/blog/alpacas-global-high-yield-cash-api/>

### How does a user withdraw funds from the program?

Customers are unable to withdraw directly from the program banks. Customers must therefore, request a withdrawal or transfer on the partner’s front-end the same way it’s implemented today, for which the corresponding cash will be swept out of the program to cover the request.

### How can a user opt out of a specific bank in the program?

Currently, clients must opt out of the entire program by unenrolling. In an upcoming release, we aim to offer the ability to opt-out at the individual program bank level.

### How frequently does interest accrue?

Daily

### How often is interest compounded?

Monthly

### When is interest available?

Last business day of the month. The accrued interest is booked to the customer account, but remains within the program to compound into yield.

### What decimal is interest rounded to?

Daily accrued interest is rounded to 4 decimals, while month-end realized interest is rounded to 2 decimals

### When can cash be swept into and out of the program?

Daily, excluding US weekends and holidays

### Is the APR/APY fixed or variable?

The Program Rate is variable and subject to change without notice.

### How can I access the FDIC Bank Sweep Program Deposit Bank List?

[Deposit Bank List](https://alpaca.markets/deposit-bank-list)

### Is there more detailed information available?\*\*

[Alpaca Securities LLC FDIC Bank Sweep Program Terms and Conditions](https://files.alpaca.markets/disclosures/Alpaca+FDIC+Bank+Sweep+Program+Terms+and+Conditions.pdf)

### What are the key timing considerations to be mindful of?

*11:45 am ET*

-The cutoff for when a deposit can be settled and swept into the program same-day for accounts with cash\_interest.status = ACTIVE.  
-The cutoff for when a partial withdrawal request can be facilitated out of the program.  
-The cutoff for when an Assignment API request will process the same-day.  
-The cutoff for when a Reassignment API request will process the same-day.  
-The cutoff for when an Unenroll API request will process the same-day.

*12:15 pm - 2:00 pm ET*

When cash\_interest.status updates cycle from PENDING\_CHANGE to ACTIVE or INACTIVE.

*6:00 pm ET*

When the [Account Activities endpoint](https://docs.alpaca.markets/reference/getaccountactivitiesbytype-1) is updated to reflect realized interest credited to accounts on the last business day of the month. The qty will be reflected within that day’s cash\_interest value from the EOD Cash Interest Details response.

*8:00 pm ET*

When the [EOD Cash Interest Details endpoint](https://docs.alpaca.markets/reference/get-v1-get-eod-cash-interest-report) is updated to reflect that day’s ending state.

\*Alpaca Securities customers that enroll in the FDIC Bank Sweep are potentially eligible for enhanced FDIC pass-through insurance coverage. Neither Alpaca nor Alpaca Securities are FDIC-insured. FDIC pass-through insurance coverage is subject to various conditions. The Program’s enhanced FDIC insurance coverage is limited to the aggregate number of participating program banks, multiplied by the FDIC insurance limit (i.e., $250,000). The total number of program banks is subject to change and Alpaca Securities may not utilize all program banks at all times which will affect the Program’s enhanced FDIC insurance coverage amount. In addition, if a customer has a direct banking relationship with a program bank this may affect the amount of funds that are potentially eligible for FDIC-pass through insurance coverage. There is no guarantee that customer funds will be held in such a manner as to maximize possible FDIC pass-through insurance coverage.

Neither Alpaca, nor any of its affiliates or subsidiaries is a bank.

Alpaca Securities offers a cash management program pursuant to the FDIC Bank Sweep. Customer funds are treated differently and are subject to separate regulatory regimes depending on whether customer funds are held in their brokerage account or within the FDIC Bank Sweep. Specifically, Alpaca Securities is a member of the Securities Investor Protection Corporation (SIPC), which protects securities customers of its members up to $500,000 (including $250,000 for claims for cash). The Federal Deposit Insurance Corporation (FDIC) insures up to $250,000 per deposit against the failure of an FDIC member bank. Customer funds held in brokerage accounts are SIPC insured, but are not eligible for FDIC insurance coverage. Funds maintained in the FDIC Bank Sweep are intended to be eligible for pass-through FDIC insurance coverage, but are not subject to SIPC coverage. FDIC insurance coverage does not protect against the failure of Alpaca, Alpaca Securities, or any of its or their affiliates and/or malfeasance by any Alpaca or Alpaca Securities employee. Program banks that participate in the FDIC Bank Sweep are not members of SIPC and therefore funds held in the Program are not SIPC protected. Please see alpaca.markets/disclosures for important additional disclosures regarding Alpaca Securities brokerage offering as well as FDIC Bank Sweep terms and conditions.

Updated 5 months ago

---

Ask AI

---

# Instant Funding (https://docs.alpaca.markets/docs/instant-funding-1)

# Instant Funding

Frequently Asked Instant Funding Questions

# Generic Questions

### Is instant funding equivalent to granting a loan?

In a way yes. It allows you to give your customers instant buying power before the actual funds reach Alpaca.

---

### Is Instant Funding available for all international partners?

Instant Funding as an Alpaca Broker API product is available in the international countries listed [here](https://alpaca.markets/support/countries-alpaca-is-available/).

---

### Can Instant Funding be tested in sandbox first?

Yes, you can test Instant Funding on sandbox. To get started, kindly reach out to your sales representative or customer success manager, who will enable this feature for you.

---

### How long does activating the instant funding service need? Is there any procedure to be done on the partner side?

Commercials discussion will need to happen with the sales team & a pricing amendment will need to be signed by the partner. Additional technical configurations would also need to be done by the Alpaca technical team, and the partner will need to integrate with the [instant funding endpoints](https://docs.alpaca.markets/reference/get-v1-instant-funding-list).

---

### Is the partner required to keep a deposit with Alpaca?

Yes, a deposit will be required. Commercials discussion will need to happen with the sales team.

---

### Can the partner withdraw this deposit amount in case of emergency to settle instant funding transfers in case settlement funds don’t arrive to Alpaca on time?

The deposit should be left untouched in your DP account and it cannot be used for settlement. Any prefunding should happen from the RF firm account that will be provided to the partner, described under the accounts section below.

---

### Will the partner or their customers be considered the debtors to Alpaca?

The partner

---

### Do our customers need to sign a new contract with Alpaca to use the instant funding service?

No, the contract will be signed between Alpaca and the partner.

---

# Accounts

### What are each of these accounts used for and who creates them: SI, RF, FW?

These will be set up by Alpaca when you confirm you will be moving forward with Instant Funding.

**SI:** Instant Funding account - Instant funding transfers and reconciliations will be created with this as the source account.

**RF:** Reconciliation Facilitation account - Partners are able to pre-fund this account to be used in the event that the amount sent for Instant Funding settlement is not sufficient, so they can complete settlement without any issues.

---

### Why can the equity of an account with an unsettled memopost go negative?

**First, a general reminder on the trading details endpoint response fields:**

* Irrelevant to memoposts
  + `long_market_value`: Open long positions market value
  + `short_market_value`: Open short positions market value
* Includes unsettled memoposts.
  + `buying_power`: Total cash buying power available for the customer to trade on their account.
  + `cash`: Total **tradable cash** that is available for a customer to trade on their account.
  + `memoposts`: Total amount of pending memoposts on the account. AKA, this is the total amount of cash in the customer's account that is available for trading due to memoposts executed but not yet settled or cancelled.
* Does not include unsettled memoposts.
  + `cash_withdrawable`: The cash that is available for the user to withdraw.
  + `equity`: This is an account's total equity. Formula to calculate equity and account for memoposts is: `equity = cash + long_market_value + short_market_value - memoposts`

**Second, the logic for calculating equity:**

* When you create a new instant funding transfer to an account:
  + `buying_power`, `cash`, & `memoposts` will increase by the same amount
  + `cash_withdrawable`, `long_market_value`, & `short_market_value` will not change
  + `equity` will not change
* **The last point is the key point here.** Since the memopost is ONLY an extension of `buying_power`, it affects any field that shows tradable cash, but it does not affect fields that show settled cash only.
* Since `memoposts` are added to `cash`, and `equity` includes `cash`, the formula to calculate equity has to adjust by removing the value of the memoposts.

**Third, A practical example:**

* Account has 0 in `cash`, 0 `buying_power`, 0 `cash_withdrawable`, 0 `long_market_value`, 0 `equity`, & 0 `memoposts`
* They deposit 100$ on the app and you memopost 100$ into their account to offer them the instant experience. You will see the below on the account:
  + `buying_power` = 100
  + `cash` = 100
  + `memoposts` = 100
  + `cash_withdrawable` = 0
  + `long_market_value` = 0
  + `equity` = 0
  + **Notice`equity` here, it is still 0**

**Then, when does the negative equity happen?**

If a customer uses the buying power to buy stock, and the price of the stock shifts causing a loss, that loss would cause a negative equity value. Similarly, if the customer makes profit, the equity value will show a positive value.

**How to validate this?**

You can test in sandbox and monitor the values.

**Suggestions on how to handle this:**

If you are showing the equity value on the UI and want to avoid showing a negative value to your users, you can simply add the memoposts value you get from the API to the equity value you get, and that would avoid the issue to begin with.

---

# Transfers & Settlement

### How are instant funding deadlines managed? Which schedule does Alpaca follow?

Instant funding deadlines follow the US trading holiday schedule. In other words, you would not see an instant funding transfer due on a weekend or on a US trading holiday.

---

### What is the payment due date for instant funding transfers?

The payment due date for instant funding transfers will be on T+1 by 1 PM ET.

It’s also important to note that instant funding transfers created after 8 pm on T+0 will be considered as next day, meaning that the system date is considered as T+1 and the transfer will be due for settlement on T+2 by 1 PM ET.

The system\_date field that is returned via the Instant Funding API will be the source of truth for determining the date that the instant funding transfer was created on and the deadline field that is returned will be the source of truth for determining the date settlement is expected.

---

### When an instant funding transfer is not settled by 1:00 PM ET on T+1 at and a customer has not yet bought any stock, how will Alpaca handle this transfer?

* A late payment interest charge will be booked on T+1 at 1 PM ET, but the transfer will not be cancelled immediately.
* By 8 PM ET on T+1, if the transfer is still not settled, it will then be canceled and the account’s buying power will be decreased.

---

### How many transfers can be included in one settlement?

Alpaca has a limit of 50.000 transfers per settlement.

If more than 50.000 transfers need to be settled, they should be batched in multiple settlements.

---

### What happens if a customer uses the buying power allocated to their account after an instant funding transfer, but the transfer is not settled by 8 PM ET on T+1?

Instant funding transfers will be automatically canceled at 8 PM ET on T+1 if payment is still not received. If the instant funding transfer has been used to purchase any asset, the cash balance in the customer account at T+1 will be used to offset the instant funding transfer. Should this result in a negative balance on the account, Alpaca will issue a margin call on T+2 to cover the negative balance. On T+3 if the debit balance has not been addressed, positions in the account will be sold to cover. Daily interest will be charged at the margin interest rate until the account no longer has a negative balance. Late payment interest will be charged on the instant funding transfer at 1 PM ET on T+1 if it is not settled by then.

---

### If there is an unexpected event that prevents settlement funds from arriving to Alpaca on time, or there is a bank holiday, how should we settle instant funding transfers?

For this purpose we have introduced the RF account (detailed [here](https://docs.alpaca.markets/docs/instant-funding-1#what-are-each-of-these-accounts-used-for-and-who-creates-them-si-rf-fw)). You can hold funds there and journal into the SI account as needed to ensure timely settlement even in the event of bank holidays. If the instant funding transfers still cannot be settled, the scenarios explained [here](https://docs.alpaca.markets/docs/instant-funding-1#when-an-instant-funding-transfer-is-not-settled-by-100-pm-et-on-t1-at-and-a-customer-has-not-yet-bought-any-stock-how-will-alpaca-handle-this-transfer) & [here](https://docs.alpaca.markets/docs/instant-funding-1#what-happens-if-a-customer-uses-the-buying-power-allocated-to-their-account-after-an-instant-funding-transfer-but-the-transfer-is-not-settled-by-8-pm-et-on-t1) would apply.

---

### What is a late instant funding transfer? What is a debit balance?

An instant funding transfer is considered late if it is not settled by 1 PM ET on T+1. In this case, a late payment interest of 1 day will be charged (fed rate + 8%).

The transfer will then be canceled at 8 PM ET. If there is sufficient cash balance in the customer account, that would be used to offset the outstanding amount of the transfer. If there is not, the account would then fall into a debit balance and margin interest will be charged (at the rate documented [here](https://files.alpaca.markets/disclosures/library/MarginDiscStmt.pdf)) on this until the balance is no longer negative.

---

### In case of a margin call, what positions would be sold out?

Selected assets will be liquidated based on the discretion of our broker dealer operations team.

---

### Will interest accrued for late payments be deducted directly from the account?

Interest for late payments will be accrued and invoiced to you on a monthly basis.

---

### How is a debit balance settled?

A partner can settle a debit balance on an account by journaling funds from the RF account to the customer’s account directly. The partner can also collect the needed funds locally from their customer before initiating this journal.

---

### Can instant funding be enabled in parallel with aggregate funding?

Yes, you can be on both instant funding and aggregate funding at the same time.

---

### If a partner is on both instant funding and aggregate funding, can a customer that exceeds the pre-determined limit fund the excess amount they require using aggregate funding?

Yes. The funding flow would depend on the APIs you are using to fund the account. Under aggregate funding, you would use the Journal API to move funds from your firm account to the customer account. Under Instant Funding, you would use the Instant Funding API to create an instant funding transfer.

---

### Do we (the partner) decide which instant funding transfers are going to be settled?

You would use the Create Settlement API to do the reconciliation. In this API, you will need to specify the transfer ID that you are looking to reconcile - this means that the decision lies with the partner on the transfers to be reconciled.

---

### Does Alpaca have the ability to waive interest charges due to a technical issue on Alpaca's end or BMO events?

This is something that would need to be taken care of on a case by case basis. Your PM or CSM would be the best person to address this if such a case arises in the future.

---

### Is it possible to avoid the forced liquidation of customer assets and instead have action taken directly against the partner?

No, we would need to take action on the account of the margin call.

---

### Is it possible to extend the timeframe that is given to an account to resolve their debit balance?

No, we are obligated to remain compliant with timelines published by market regulators.

---

### If an account has remaining cash balance, will this be drawn to pay off the unreconciled instant funding transfers of the specific customer only?

Yes.

---

### Is there a case where the cash balance of a certain customer is used to pay off unsettled instant funding transfers of other customers?

No.

---

### Could you clarify how the below scenario would be handled by Alpaca:

**On t+0, the partner uses a credit limit worth USD 100,000 out of the total USD 400,000.**

**The instant funding transfers of the used USD 100,000 credit cannot be reconciled on t+1 1:00 PM (US ET)**

**How would the limit be updated on t+1 after 1 PM?**

The scenario is illustrated below:

| Date | Action | Amount | Total Limit | Amount in Use | Amount Available | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| (t+0) | - | - | 400,000 | 0 | 400,000 | This is the partner’s total available limit |
| (t+0) | MEM | 100,000$ | 400,000 | 100,000 | 300,000 | When the transfers are done, the remaining limit is reduced |
| (t+1) Before 8PM | - | - | 400,000 | 100,000 | 300,000 | As long as the transfers have not been cancelled yet, the remaining limit is not affected. In other words, since the 100k transfers are still not cancelled, the remaining limit available to be used is 300k |
| (t+1) After 8PM | MEM | -100,000 (cancelled transfer) | 400,000 | 0 | 400,000 | As soon as the transfers are cancelled, the available to use limit goes back to 400k |

In summary, as long as the transfers are not settled or cancelled yet, the remaining limit would be the partner’s total limit - the amount of executed transfers. As soon as the transfers are settled or cancelled, the remaining limit would reset.

**Note:** The instant funding transfers are due for settlement at 1PM ET on t+1, but they actually get cancelled at 8PM ET.

---

### What would be the best way for a partner to retrieve the overall cumulative outstanding amount, interest, and unreconciled instant funding transfers to date ?

Call the [GET all instant funding endpoint](https://docs.alpaca.markets/reference/get-v1-instant-funding-list) and filter by status.

---

### Are SSE events supported for IF transfers ?

Yes, SSE events for IF transfers can be subscribed to [here](https://docs.alpaca.markets/reference/get-v1-events-nta).

---

### Why do I need to send travel rule information?

Alpaca is a financial institution so it is required by US law for us to collect travel rule information when dealing with the movement of funds. Since instant funding transfers are only an extension of buying power we only require travel rule information upon settlement since that is when the instant funding transfer is converted to actual settled cash. For more information on the travel rule requirements please refer to the [FinCEN Advisory](https://www.fincen.gov/sites/default/files/advisory/advissu7.pdf) as needed.

---

# Limits

### Is it possible to increase the predefined correspondent limit?

Broker-Dealer will have to approve and more deposit is likely required, but yes this is possible.

---

### Does the partner have the ability to change the USD 1,000 limit per individual or does this need approval from Alpaca?

The default is set at USD $1,000. The partner can discuss with the sales team regarding the higher limit so that it can be factored into the commercial discussions.

---

### For the individual limit change, is it possible to assign different limit values to different customers? For example, setting the limit of User A to USD 1,000 & USD 5,000 for User B?

This would not be possible as the account limit is set on a correspondent level; all accounts would have the same limit.

---

### Is it possible for a partner to ignore the individual limit? For example, as long as each day the customers use up to the USD 400,000 limit on instant funding, each customer can fund their account with any amount they need.

We are able to support this configuration, whereby the Instant Funding limit is only on a partner level, and not on your individual user account level.

---

All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.

Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc. This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities are not registered or licensed, as applicable.

Updated 21 days ago

---

Ask AI

---

# Fully Paid Securities Lending (https://docs.alpaca.markets/docs/fully-paid-securities-lending)

# Fully Paid Securities Lending

**What is the Alpaca Fully Paid Securities Lending Program?**

Our program offers you the ability to earn additional income from the securities you already own by lending them to Alpaca, while you continue to retain full ownership. Once you activate Fully Paid Securities Lending, you'll receive monthly payments if we borrow your shares.

---

**How does the program work?**

Once enrolled in the program, Alpaca facilitates the lending of your eligible fully paid securities to borrowers, typically for short selling or trade settlements. These borrowers pay an interest rate based on current market conditions directly to Alpaca, and in turn, you will receive monthly interest payments based on the value of the loaned securities.

---

**What are the benefits of enrolling in the program?**

Lending your securities can provide you with additional income.  
The income generated from securities lending can be reinvested into other opportunities, creating the potential for additional growth.  
Lending your securities helps support market liquidity by enabling short sellers to execute their strategies, which can contribute to a more efficient market overall.  
When you lend your securities, you maintain ownership of the underlying assets, allowing you to benefit from any potential appreciation or dividends, even while generating income from the loan.

---

**What are the risks of enrolling in the program?**

Risks:  
There is no assurance that your securities will be lent or that a market for lending them exists.  
When securities are borrowed for a short sale, there is a possibility that their market price will decline.  
When you lend your securities, you will temporarily lose voting rights, as they are transferred to the borrower during the loan period.  
Income earned from lending your securities may have tax consequences, which could affect your overall returns.  
Securities lending is not protected by the Securities Investor Protection Corporation (SIPC), which means the loaned assets are not covered by SIPC.

---

**What are the eligibility requirements?**

One of the following criteria must be met in order to be eligible to participate.

* $2,500 in account balance
* $20,000 reported income
* $20,000 in liquid assets
* At least 1 year of trading experience

---

**What account types are eligible for the program?**

All account types with US equities that have been fully paid for or that are in excess of any margin debit.

---

**What types of investments are eligible for the program?**

All US equities that have been fully paid for or that are in excess of any margin debit will be eligible to loan

---

**Can I choose which stocks to lend out?**

You cannot choose specific stocks to lend. By enabling Fully Paid Securities Lending, all of your stocks, ADRs, and ETFs will be considered for lending.

---

**Will Alpaca lend out all eligible shares?**

There is no guarantee that all eligible shares in an account will be loaned through the Fully Paid Securities Lending Program. This may occur if there isn’t a favorable market rate for Alpaca to lend your shares.

---

**How are lending rates determined?**

Lending rates are determined by market conditions, based on the supply and demand for individual securities.

---

**When is interest earned on lent securities paid out?**

Monthly interest will be posted to your cash balance on the last settlement date of the following month.

---

**What is the potential income from lending out securities?**

When your securities are lent out, interest accumulates daily and is automatically credited to your account on a monthly basis. The interest you receive depends on the demand for the loaned shares. Here’s an example of how your earnings are calculated.

Shares on loan  
2,000  
Market price  
$20  
Market value  
$40,000  
Annualized lending interest rate  
9.00%  
Daily accrual ($40,000 x 9.00% / 360 days\_)  
$10.00  
Your hypothetical monthly income  
($10.00 x 30 days)  
$300.00

*Disclaimer: Interest accrual is based on a 360-day financial year, a standard billing practice. Actual earnings may vary.*

---

**Can I still sell a security while it is out on loan?**

Yes, you can sell a security at any time. However, once the loan is closed, which may happen concurrently with the sale of the asset, you will no longer receive loan interest.

---

**How will dividends be handled within the Securities Lending Fully Paid Program?**

The borrower will be entitled to the dividend, and the customer will be entitled to a “payment-in-lieu” which will be a cash payment grossed up for the respective tax rate of the customer.

---

**Will SIPC coverage be impacted?**

The investments and cash in your Alpaca investing account are generally protected by SIPC insurance. However, stocks on loan are not covered by SIPC. Instead, cash collateral is used to safeguard your loaned stocks. We strive to maintain cash equivalent to at least 100% of the value of your loaned stocks at a third-party bank. In the event that Alpaca files for bankruptcy and is unable to return your stocks, this bank would compensate you in cash for the value of your loaned securities. Additionally, any cash held at this third-party bank would be covered under FDIC insurance, but only up to the $250,000 limit.

---

**Will I continue to have voting rights for shares on loan?**

Usually, company shareholders can exercise voting power on matters like new policy proposals, board appointments, or corporate actions. However, when your shares in a company are on loan, you will not have shareholder voting rights. However, you can unenroll from the program at any time to restore your voting rights.

---

**How and where is the collateral held for loans in the Program?**

Currently it is held in cash at our bank BMO. This is subject to change at a future date.

---

**How does lending stock affect the calculation of my margin and excess liquidity?**

Lending stock through the Fully Paid Securities Lending Program does not affect the calculation of your margin or excess liquidity. Your borrowing capacity remains determined by your stock positions.

---

**Does the Fully Paid Securities Lending Program still provide benefits if I have written call options on my shares?**

If the stock is fully paid, the Program will benefit you the same whether or not it has call options written against it.

**What occurs with stock on loan if it is later delivered to fulfill a call assignment or put exercise?**

The loan will end on T+1 of the transaction (trade, assignment, or exercise) that closed or reduced the position.

---

**Is Pattern Day Trading still available while opted into the Program?**

Yes, we will support Pattern Day Trading while users are opted into the program.

---

**How does Short Stock Buy-Ins & Close-Outs work?**

When a user holds a short stock position, the clearing broker is obligated to deliver shares by the settlement date. If these shares cannot be borrowed, or are recalled by the lender, or if a "fail to deliver" occurs with the clearinghouse, a close-out may be initiated. If we are unable to borrow shares for delivery by the settlement date (T+1), a close-out will be initiated on T+2 at approximately 9:30 AM ET. Lenders can recall shares at any time. If we cannot replace these recalled shares, a buy-in will be executed by the lender. If we have a net short settlement obligation with the clearinghouse and cannot obtain the shares, a close-out will be initiated prior to the open of regular trading hours on the day following the settlement day.

*Please read I[mportant Risk Disclosures With Respect To Participating In Fully Paid Securities Lending Transactions](https://files.alpaca.markets/disclosures/Important+Risk+Disclosures+With+Respect+To+Participating+In+Fully+Paid+Securities+Lending+Transactions.pdf) carefully before deciding whether to participate in lending Fully Paid Securities or agreeing to enter into a Master Securities Lending Agreement with Alpaca Securities LLC.*

*These disclosures describe important characteristics of, and risks associated with engaging in, securities-lending transactions.*

*All investments involve risk and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not assure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.*

Updated 5 months ago

---

Ask AI

---

# 24/5 Trading (https://docs.alpaca.markets/docs/245-trading)

# 24/5 Trading

### What is 24/5 Trading (Overnight Trading)?

Overnight Trading extends market hours to provide a 24-hour, 5-day-a-week trading experience for all NMS securities. The overnight session operates from 8:00 PM ET Sunday to 4:00 AM ET Friday, bridging the gap between one day's post-market session and the next day's pre-market session.

---

### How does the overnight trading session work?

Overnight trade executions and market data are facilitated by the Blue Ocean Alternative Trading System (BOATS). As an Alternative Trading System (ATS), BOATS operates an independent overnight trading session outside of traditional stock exchanges.

---

### What are the hours for the 24/5 trading sessions?

The trading sessions are structured as follows, from Sunday evening to Friday evening:

* **Overnight Session:** 8:00 PM - 4:00 AM ET (technically occurs on the evening before the trade date)
* **Pre-Market Session:** 4:00 AM – 9:30 AM ET
* **Regular Market Session:** 9:30 AM - 4:00 PM ET
* **After-Hours Session:** 4:00 PM - 8:00 PM ET

The overnight session follows the NYSE holiday calendar. If US markets are fully closed for a holiday, the overnight trading session immediately preceding that holiday will not run. ***For example, the overnight session will be closed on the Wednesday evening before US Thanksgiving (8:00 PM ET) and will resume on Thursday evening at 8:00 PM ET.*** On US market half-days, the overnight trading session runs as normal for the full eight hours (8:00 PM ET – 4:00 AM ET), even if regular or after-hours trading closes early. ***For example, on the Friday after US Thanksgiving, the overnight session runs as usual, but the after-hours session does not.***

---

### How can I enable overnight trading?

Please contact your Customer Success Manager for details on pricing and the steps required to enable overnight trading for your account.

---

### How can I access market data for the overnight session?

We offer a high-accuracy indicative data feed through our partnership with Blue Ocean, available for a monthly fee. Please contact our sales team for pricing details.

---

### What is included in the overnight market data feed?

The market data feed provides access to:

* **Indicative Real-time Quotes:** Real-time bid and ask prices that are indicative of the market.
* **Indicative Trades:** Trade data that is delayed by 15 minutes and adjusted to fit within the real-time bid-ask spread.

---

### What securities are available for overnight trading?

All National Market System (NMS) securities are available for trading during the overnight session. Assets tradable in the overnight session can be identified via the `overnight_tradable` attribute in the Assets API. The list may be limited due to compliance or risk procedures, and the best way to validate the available securities is by using our Assets API as outlined above. OTC securities are not part of the NMS and are therefore not available.

### What order types and time-in-force (TIF) options are supported?

* **Order Type:** Only `limit` orders are supported during the overnight session.
* **Time-in-Force (TIF):** The only TIF currently supported is `day`. `day` orders placed during the overnight session will remain active through the regular and after-hours sessions of the upcoming trading day. If unfilled, the order is canceled at 8:00 PM ET. Support for `GTC` (Good-Til-Canceled) orders is planned for a future release.

---

### Is fractional share trading supported?

Yes, fractional share trading is supported during the overnight session and functions the same way as it does during other extended-hours sessions.

---

### Are there restrictions on margin or buying power during the overnight session?

Yes. Day Trading Buying Power (DTBP) does not apply to the overnight session. This means 2x multiplier is the max margin buying power for overnight session trades. If an account uses DTBP for an order during the post market session, the order might be rejected (at 8 PM ET) due to insufficient buying power (if reg\_t or non-DT buying power is insufficient).

---

### How does overnight trading impact Pattern Day Trader (PDT) rules?

A day trade is defined as buying and selling the same security on the same calendar day. Trades executed during the overnight session are assigned a trade date based on when they occur:

* Trades between **8:00 PM and 11:59 PM ET** are assigned the next day's trade date (T+1).
* Trades between **12:00 AM and 4:00 AM ET** are assigned the current day's trade date (T).

Therefore, a position opened during the overnight session and closed during the regular hours of the same assigned trade date would count as a day trade.

---

### What happens to an order that is not filled during the overnight session?

If your `day` order is not filled during the overnight session, it will automatically carry over into the pre-market, regular, and after-hours sessions for that trade date. It remains an active order until it is executed or the market closes at 8:00 PM ET.

---

### How does trade settlement work for overnight trades?

The overnight session marks the beginning of a new trading day. Trades are assigned a date based on their execution time and settle on a T+1 basis from that date.

* **Example:** A trade executed at 9:00 PM ET on a Monday is assigned a trade date of Tuesday and will settle on Wednesday (T+1).

---

### How do corporate actions affect overnight trading?

A security may be halted from trading during the overnight session while a pending corporate action is being processed. Furthermore, due to the way trade dates are assigned, purchasing a stock during the overnight session on its ex-dividend date will not entitle you to that stock's dividend.

---

### What happens when a security is halted during the overnight session?

If an asset is halted overnight (e.g., due to a corporate action or pending news), the halt typically persists for the entire session. Orders submitted for a halted security will be accepted by the system with a status of `accepted` but will be held in a pending state. This ensures your order can be executed as soon as the halt is lifted and trading resumes in the next session.

---

### What API changes are required to support overnight trading?

Integration requires awareness of two new boolean attributes in the `Assets` API endpoint:

* `overnight_tradable`: Indicates if the asset is eligible for trading in the overnight session.
* `overnight_halted`: Indicates if an `overnight_tradable` asset is currently halted.

Additionally, a new `overnight` feed name has been introduced for the Market Data API.

---

### How can I identify which assets are tradable overnight via the API?

You can identify eligible assets by calling the `v1/assets` endpoint and filtering for assets where the `overnight_tradable` attribute is `true`.

---

### When is the best time to sync the list of overnight-tradable assets?

We begin syncing our list of tradable assets at 7:05 PM ET and run updates every 10 minutes until 7:45 PM ET. For the most up-to-date list, we recommend syncing your asset list between 7:45 PM and 8:00 PM ET, with 7:55 PM ET being the ideal time.

---

  

### Can I access delayed historical overnight requests with an overnight subscription?

Yes, you can access delayed historical overnight requests with an overnight subscription, provided that the end parameter in your request is at least 15 minutes old.

**To access delayed historical overnight data, make sure to include the parameter `feed=boats` in your request, `feed=overnight` will give error.**

Example:
If you have an overnight subscription and want to request overnight/BOATS data ending at 10:00 PM EST , you can do so any time after 10:15 PM by specifying`feed=boats` in your request.

---



#### Disclosures

The content of this article is for general information only and is believed to be accurate as of the posting date, but may be subject to change. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.

Orders placed outside regular trading hours (9:30 a.m. – 4:00 p.m. ET) may experience price fluctuations, partial executions, or delays due to lower liquidity and higher volatility.

Orders not designated for extended hours execution will be queued for the next trading session.

Additionally, fractional trading may be limited during extended hours. For more details, please review [Alpaca Extended Hours & Overnight Trading Risk Disclosure](https://files.alpaca.markets/disclosures/library/ExtHrsOvernightRisk.pdf).

Fractional share trading allows a customer to buy and sell fractional share quantities and dollar amounts of certain securities. Fractional share trading presents unique risks and is subject to particular limitations that you should be aware of before engaging in such activity. See Alpaca Customer Agreement at [Alpaca - Disclosures and Agreements](https://alpaca.markets/disclosures) for more details.

Margin trading involves significant risk and is not suitable for all investors. Before considering a margin loan, it is crucial that you carefully consider how borrowing fits with your investment objectives and risk tolerance.

When trading on margin, you assume higher market risk, and potential losses can exceed the collateral value in your account. Alpaca may sell any securities in your account, without prior notice, to satisfy a margin call. Alpaca may also change its “house” maintenance margin requirements at any time without advance written notice. You are not entitled to an extension of time on a margin call. Please review the Firm’s [Margin Disclosure Statement](https://files.alpaca.markets/disclosures/library/MarginDiscStmt.pdf) before investing.

All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.

Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.

Cryptocurrency services are made available by Alpaca Crypto LLC ("Alpaca Crypto"), a FinCEN registered money services business (NMLS # 2160858), and a wholly-owned subsidiary of AlpacaDB, Inc. Alpaca Crypto is not a member of SIPC or FINRA. Cryptocurrencies are not stocks and your cryptocurrency investments are not protected by either FDIC or SIPC. Please see the [Disclosure Library](https://alpaca.markets/disclosures) for more information.

This is not an offer, solicitation of an offer, or advice to buy or sell securities or cryptocurrencies or open a brokerage account or cryptocurrency account in any jurisdiction where Alpaca Securities or Alpaca Crypto, respectively, are not registered or licensed, as applicable.

Updated about 1 month ago

---

Ask AI

---

# OmniSub (https://docs.alpaca.markets/docs/omnisub)

# OmniSub

**What is OmniSub and how is it legally structured?**

OmniSub is Alpaca’s omnibus account model that features internal sub-accounting. The structure is an omnibus brokerage account held by the partner at Alpaca Securities LLC. The sub-accounting layer is a technology solution provided by Alpaca DB and the sub-accounts are not considered fully disclosed broker accounts to Alpaca Securities LLC. Alpaca DB provides the technology layer to power your front-end customer experience while the only brokerage account opened will be the omni brokerage account.

A Partner, such as a broker or fintech, holds this single legal omnibus account, while all individual customer balances and activities are tracked as distinct "sub-accounts" within Alpaca DB systems for operational and reporting purposes.

---

**How are accounts structured in the OmniSub model?**

The model consists of three key components:

* Omnibus Account: This is the single, legal brokerage account that the partner establishes and owns at Alpaca Securities LLC. All aggregate activity from the sub-accounts rolls up into this account.
* Sub-accounts: These are not brokerage accounts of Alpaca Securities LLC, but are internal, technology-based records for tracking each end-customer's positions and activities. They are managed by the partner via API.

---

**Can I trade directly from the omnibus account?**

No, direct trading is disabled at the omnibus account level. All trading activities must originate from and be executed exclusively through the individual sub-accounts or the designated Default Account.

---

**Will I be able to see sub-accounts in Brokerdash?**

Yes, partners have visibility into their individual sub-accounts within Brokerdash, our partner dashboard. This view also includes two system accounts: the default account (for holding residuals) and a control account (for operational adjustments).

---

**Who is responsible for KYC/CIP and AML for the end-customers?**

The partner is solely responsible for all end-customer compliance. This includes:

* KYC/CIP: The partner must conduct their own comprehensive Know Your Customer (KYC) and Customer Identification Program (CIP) procedures for all end-customers.
* AML: The partner is primarily responsible for end-customer Anti-Money Laundering (AML) monitoring based on their own policies. While end-customer PII is not shared, the granular nature of sub-accounts gives Alpaca enhanced internal visibility to monitor transactions.
* Your AML program will be reviewed during onboarding as part of due diligence.

---

**How is tax reporting managed?**

Alpaca's tax reporting responsibility is limited to the omnibus account level only.

The partner is fully responsible for all tax reporting obligations for their individual end-customers.

---

**What funding methods are supported and how do they work?**

All funding activities (deposits, withdrawals) are performed centrally at the omnibus account level. OmniSub supports two main models:

* Pre-funding (Aggregated): The partner deposits funds into the omnibus account in advance. Buying power checks are enforced, and sub-accounts can only trade up to their allocated amount.
* Post-Trade Net Settlement (No Buying Power Checks): Trades can be executed without pre-funding up to a pre-set limit. At the end of the day, all trades are netted, and the partner settles the final net debit or credit balance. This model significantly optimizes capital efficiency.

---

**How are trades executed?**

Trades are placed at the sub-account level via API. The system then automatically mirrors these trades into the omnibus account to facilitate settlement, clearing, and regulatory reporting.

---

**How are corporate actions handled?**

Mandatory Corporate Actions: Events like dividends, stock splits, and mergers are processed simultaneously at both the sub-account and the omnibus account levels to ensure consistency. Any rounding residuals are booked to a designated control account.

---

**Why might a sub-account be blocked from trading?**

This is typically due to a pending corporate action. To ensure positions and balances are accurate, Alpaca will set trading\_blocked = true on a sub-account if corporate action processing is not complete before market open. Partners can monitor this status via the API.

---

**Who provides official statements and trade confirmations to the end customer?**

The Partner is always responsible for providing official statements and confirms to end clients. Alpaca provides the necessary JSON data for sub-accounts and official statements for the omnibus account to facilitate this.

---

**What is the process for error handling and trade corrections?**

* Alpaca Securities LLC’s Responsibility: Venue-related trade corrections (e.g., from exchange errors) and Client-originated errors (e.g., incorrect order entry) are handled by Alpaca Securities LLC.
* Processing: All trade corrections and busts are processed at the sub-account level and automatically propagate to the omnibus account to maintain reconciliation. The partner is responsible for addressing any resulting debit balances in a sub-account.

---

**How are ACATS handled?**

* Incoming ACATS: Asset transfers are allocated to the specified sub-account, and the partner is responsible for validating the allocation.
* Outgoing ACATS: The partner has a 24-hour validation window to approve an outgoing transfer request before Alpaca processes it.

---

**Do I need to handle my own CAT (Consolidated Audit Trail) reporting?**

Alpaca Securities LLC handles CAT reporting at the omnibus account level.

---

**Can I migrate my existing Fully-Disclosed accounts to an OmniSub model?**

It’s important to consider what’s important for your business as each business is unique. Alpaca will review your request and make a determination. Alpaca has a semi-automated process for this migration.

---

**Can my sub-accounts operate in a different currency than the omnibus account?**

No. All sub-accounts must use the same base currency as the parent omnibus account.

---

**How do I create a sub-account via the API?**

A partner can create a sub-account by calling the Broker API.

Endpoint: `POST /v1/accounts`

Request Body:  
`{ "account_type": "omnibus_sub", "primary_account_holder_id": "<the owner id of your omni account>" }`

---

The Omni-Sub product is offered by AlpacaDB as a technology service for sub-accounting related to omnibus clearing services. Approval for this technology service is subject to Alpaca Securities due diligence review.

The content of this document is for general information only and is believed to be accurate as of posting date but may be subject to change. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.

Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member FINRA/SIPC, a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.

This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered or licensed, as applicable.

Updated 5 months ago

---

Ask AI

---

# Fixed Income (https://docs.alpaca.markets/docs/fixed-income)

# Fixed Income

This article provides answers to common questions about Alpaca’s fixed income product offerings, including U.S. Treasuries and Corporate Bonds, available through the Broker API.

---

## General Product Offerings

### What types of fixed income products does Alpaca offer?

Alpaca supports two main categories of fixed income securities at this time:

* U.S. Treasuries: Government debt securities. We currently offer Treasury Bills (T-Bills).
* U.S. Corporate Bonds: Debt securities issued by U.S. corporations, including both investment-grade and high-yield options.

### Who can access these fixed income products?

These products are available to all Broker API partners and can be offered to their end-users. This applies to all fixed income products on our platform.

---

## Trading and Orders

### How does trading work for fixed income?

This process is the same for both U.S. Treasuries and Corporate Bonds. All trading is executed via the API. Alpaca aggregates quotes from multiple liquidity providers to ensure best-price execution during U.S. bond market hours.

### How are fixed income orders handled?

Due to our relationship with Moment, we are able to provide an equity-like experience for the handling and execution of fixed income orders. What does that mean? Fixed income orders, when placed, will be sent to an order book to pair against posted quotes. Your order will need to match both the price and the quantity requirement for the quote in order to pair. If your order does not immediately pair, it will be posted on the order book for the remainder of the trading day similar to a passive limit order in equity markets.

### What order types are supported for fixed income?

For fixed income trades only limit and market orders are accepted. Please note that market orders are submitted as marketable limits with a 2.5% collar from the eligible top-of-book quote (i.e. quote with min qty available that is smaller or equal than the order size).

### When do fixed income products trade?

The fixed income markets generally follow a schedule similar to equity trading with the majority of trading occurring between 9:30am ET and 4:00pm ET. However, bond markets can close sooner than equity markets on holidays or have treasury market closers while equity markets are still live. For an up to date schedule of bond market closures please refer to this website: <https://www.sifma.org/resources/guides-playbooks/holiday-schedule>

### Is fractional investing available?

No. Currently, all fixed income products (both Treasuries and Corporate Bonds) are traded in full denominations only, which is typically in increments of $1,000 face value. We are planning to introduce fractional investing for these products in the future.

### What happens if I place an order outside of market hours?

This process is the same for both U.S. Treasuries and Corporate Bonds. Orders submitted when the market is closed will be queued with an accepted status and will be sent for execution when the market reopens.

### How do I cancel an order?

This cancellation logic applies to orders for both U.S. Treasuries and Corporate Bonds:

* During Market Hours: A cancellation request is sent to the execution venue immediately.
* Outside Market Hours: If the order's status is accepted, it will be cancelled immediately. If it has already been sent to a venue (e.g., status is new), it will become pending\_cancel until the market opens.

### What are the minimum and maximum order sizes?

The order size limits are as follows:

* Minimum Order Size: $1000. This applies to both U.S. Treasuries and Corporate Bonds.
* Maximum Order Size: $1,000,000.

---

## Product Details: U.S. Treasuries

### What is a U.S. Treasury Bill (T-Bill)?

T-Bills are short-term debt securities issued by the U.S. government with a maturity of one year or less. They are issued at a discount to their face value and do not pay periodic interest. At maturity, the investor receives the full face value of the bill.

### What corporate actions are relevant for T-Bills on Alpaca?

As T-Bills do not pay coupons, the only corporate action is redemption. This occurs when the T-Bill matures and the holder is paid its face value.

### How can I see which Treasuries are offered by Alpaca?

See below, please ensure to check if the tradable flag is set to true.

For sandbox: GET

<https://broker-api.sandbox.alpaca.markets/v1/assets/fixed_income/us_treasuries>

For production: GET

<https://broker-api.alpaca.markets/v1/assets/fixed_income/us_treasuries>

More details can be found [here](https://docs.alpaca.markets/reference/ustreasuries-1).

---

## Product Details: Corporate Bonds

### What are Corporate Bonds?

Corporate Bonds are debt instruments issued by corporations to raise capital. When you buy a corporate bond, you are lending money to the company. In return, the company typically pays you periodic interest (coupons) over the life of the bond and repays the principal amount at maturity.

### Which types of corporate bonds are currently offered by Alpaca?

Investment-grade, non-puttable, non-callable, non-convertible, non-reg-s, non-144a corporate bonds. Please note that we are working to enable more types of corporate bonds soon.

### How can I see which corporate bonds are offered by Alpaca?

See below, please ensure to check if the tradable flag is set to true.

For sandbox: GET

<https://broker-api.sandbox.alpaca.markets/v1/assets/fixed_income/us_corporates>

For production: GET

<https://broker-api.alpaca.markets/v1/assets/fixed_income/us_corporates>

---

## Pricing, Yields, and Fees

### How are fixed income securities priced?

This pricing convention applies to both U.S. Treasuries and Corporate Bonds. The price is quoted as a percentage of its par value (face value). This is known as the "clean price" and does not include any accrued interest. The total settlement amount will include the clean price plus any accrued interest for coupon-bearing bonds in specific.

### How are markups and fees handled?

The concept of markups applies to both U.S. Treasuries and Corporate Bonds. Markups, which can be applied by Alpaca and/or partners, are included in the final execution price. It is important to note that for short-term U.S. Treasuries, the yield is highly sensitive to even small price markups.

### Are there any regulatory fees?

For U.S. Treasuries, sales are reportable to the Trade Reporting and Compliance Engine (TRACE), which incurs a small regulatory fee.

---

## API and Platform Integration

The following API functionalities apply to all fixed income securities available on the Alpaca platform.

### How can I find fixed income assets via the API?

You can query for available assets using dedicated endpoints, such as /assets/fixed\_income/us\_treasuries or /us\_corporates. You can filter results by identifiers like CUSIP or ISIN, subtype, and status.

### How can I determine if a bond is tradable via the API?

The asset object returned by the API contains a tradable boolean field. If tradable is true, the security is available for trading.

## What security identifiers are used?

We support both CUSIP (9-character) and ISIN (12-character) identifiers for all fixed income securities.

---

## Custody, Settlement, and Compliance

### Where are the assets held (custody)?

Custody differs by product type:

* U.S. Treasuries: Custody is provided by our partner, BMO.
* Corporate Bonds: Self-custodied by Alpaca in book-entry form at the Depository Trust Company (DTC), similar to equities.

### What is the settlement cycle?

The settlement cycle differs by product type:

* U.S. T-Bills: Settle on a T+1 basis (trade date plus one business day).
* Corporate Bonds: Settle on a T+2 basis (trade date plus two business days), following standard U.S. market conventions.

### Are there any special compliance requirements?

For end-users, there are no additional suitability assessments or customer agreements required (unlike options). For partners, a technical sign-off is required before enabling fixed income products in a production environment. All confirmations and statements comply with SEC Rule 10b-10.

---

*The content of this article is for general information only and is believed to be accurate as of posting date but may be subject to change*.

*Fixed income securities can experience a greater risk of principal loss when interest rates rise. These investments are also subject to additional risks, including credit quality fluctuations, market volatility, liquidity constraints, prepayment or early redemption, corporate actions, tax implications, and other influencing factors.*

*All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.*

*Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.*

*This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered or licensed, as applicable.*

Updated about 1 month ago

---

Ask AI

---

# Customer Account Opening (https://docs.alpaca.markets/docs/account-opening)

# Customer Account Opening

If you are a fully-disclosed broker-dealer, an RIA, or a trading app setup, you can open your end customer’s account using Account API. The POST method allows you to submit all KYC information to Alpaca. There are slight differences between setups. #

# Trading/Investing App and RIA

In this use case, Alpaca is responsible for the account approval step, while you can own the user experiences for collecting the end-customer information. We require you to collect a set of the information required for our approval process.

Upon the POST request, the account status starts from `SUBMITTED` status. Alpaca system will run the automatic KYC process asynchronously and update the KYC result as the account status. You can receive such updates in the [Event API](/reference/subscribetotransferstatussse) stream.

If all KYC information is verified without problems, the account status will be `APPROVED` and shortly transition to `ACTIVE`. In some cases, if the final approval is pending, the account status becomes `APPROVAL_PENDING` which will transition to `APPROVED` once it is approved. In the case of some action is required, the status becomes `ACTION_REQUIRED` and you will receive the reason for this. In most cases, you will need to collect additional information from the end user. One example would be that the residential address is not verified, so a copy of a document such as a utility bill needs to be uploaded. You can use [Document API](/reference/getdocsforaccount) to upload additional documents when requested.

# Fully-Disclosed Broker-Dealer

As a reminder, in this setup, you are required to have a proper broker-dealer license in your local jurisdiction and you are the broker on the record. Alpaca relies on your KYC process to open customers' accounts which you will send via the [CIP API](/reference/post-v1-accounts-account_id-cip).

In this case, as soon as a `POST` request is made and all fields are validated, we will first screen the account against our internal list of blacklisted accounts and an exact, or similar, match against this list will result in the account moving to either `REJECTED` or `APPROVAL_PENDING`. If there is no match then the account status starts from `APPROVED` status, meaning you have approved the account opening. Therefore, you need to complete your KYC for the account before making the `POST` request.

# Omnibus Broker-Dealer

In an omnibus setup, you will not request any new account opening. Your trading accounts will be set up by Alpaca when the go-live is approved. That said, you may want to simulate this structure using [Account API](/reference/createaccount) and you can open as many accounts as you want in the sandbox environment even if you are an omnibus.

# Account Type

Alpaca currently opens all accounts as margin accounts. We support individual taxable accounts and business accounts. Other types of accounts such as cash and IRA accounts are on our roadmap.

Even though all accounts at Alpaca are margin accounts, you have the ability to set accounts to be cash accounts (100% buying power) to disable margin trading for your users through account configurations [here](/reference/patch-patch-v1-trading-accounts-account_id-account-configurations).

Updated 5 months ago

---

Ask AI

---

# Accounts Statuses (https://docs.alpaca.markets/docs/accounts-statuses)

# Accounts Statuses

Updated 5 months ago

---

Ask AI

---

# International Accounts (https://docs.alpaca.markets/docs/international-accounts)

# International Accounts

## W-8 BEN

For certain individuals, a W-8 BEN form should be submitted at onboarding. If the individual is not a registered U.S. taxpayer (not subject to a W-9), the W-8 BEN form may need to be submitted. The IRS explains [here](https://www.irs.gov/instructions/iw8ben) which individuals this applies to and provides instructions on completing the form. Every three years, in addition to the calendar year it was signed, a new W-8 BEN form must be submitted.

The form can be submitted in JSON, JSONC, PNG, JPEG or PDF. If submitting it in JSON, please see the W-8 BEN completed with the corresponding field names for the API [here](https://github.com/alpacahq/bkdocs/files/7756721/W-8Ben_Example_Broker_Docs.pdf).

Note: The dates collected on the form are in a slightly different format than how they need to be submitted via Accounts API. It is requested by the user on the form in MM-DD-YYYY, but should be submitted as YYYY-MM-DD.

Updated 5 months ago

---

Ask AI

---

# Domestic (USA) Accounts (https://docs.alpaca.markets/docs/domestic-usa-accounts)

# Domestic (USA) Accounts

## State Validation

When [creating](https://docs.alpaca.markets/reference/createaccount) or [updating](https://docs.alpaca.markets/reference/patchaccount) accounts with `country_of_tax_residence = USA` we will accept either the 2 letter abbreviation code for the state or the complete name of the state (case insensitive) as defined below:

| State Abbreviation | State Name |
| --- | --- |
| AA | Armed Forces of the Americas |
| AE | Armed Forces of Europe |
| AK | Alaska |
| AL | Alabama |
| AP | Armed Forces of the Pacific |
| AR | Arkansas |
| AZ | Arizona |
| CA | California |
| CO | Colorado |
| CT | Connecticut |
| DC | District of Columbia |
| DE | Delaware |
| FL | Florida |
| GA | Georgia |
| HI | Hawaii |
| IA | Iowa |
| ID | Idaho |
| IL | Illinois |
| IN | Indiana |
| KS | Kansas |
| KY | Kentucky |
| LA | Louisiana |
| MA | Massachusetts |
| MD | Maryland |
| ME | Maine |
| MI | Michigan |
| MN | Minnesota |
| MO | Missouri |
| MS | Mississippi |
| MT | Montana |
| NC | North Carolina |
| ND | North Dakota |
| NE | Nebraska |
| NH | New Hampshire |
| NJ | New Jersey |
| NM | New Mexico |
| NV | Nevada |
| NY | New York |
| OH | Ohio |
| OK | Oklahoma |
| OR | Oregon |
| PA | Pennsylvania |
| RI | Rhode Island |
| SC | South Carolina |
| SD | South Dakota |
| TN | Tennessee |
| TX | Texas |
| UT | Utah |
| VA | Virginia |
| VT | Vermont |
| WA | Washington |
| WI | Wisconsin |
| WV | West Virginia |
| WY | Wyoming |

Updated 5 months ago

---

Ask AI

---

# Data Validations (https://docs.alpaca.markets/docs/data-validations)

# Data Validations

As part of Alpaca Securities LLC’s regulatory obligation to comply with new reporting requirements defined by FINRA, we are required to submit user information to comply with FINRA’s Customer & Account Information System (CAIS). The CAIS system will begin validating the data for correct formatting so we need to ensure that data is provided in correct format at the time of account creation to avoid errors and potential delays with reporting.

This validation will be live in production on **March 25, 2024**. The validation will be released in sandbox first on **March 5, 2024** so you can carry out any testing required.

## Validation Criteria

A validation check on user information submitted via the account creation ([POST /v1/accounts](https://docs.alpaca.markets/reference/createaccount)) and update ([PATCH /v1/accounts/{account\_id}](https://docs.alpaca.markets/reference/patchaccount)) endpoints will return a 422 error if the information submitted does not meet our validation criteria. The validation criteria will include the following:

* Name and Address Romanization
  + `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, and `tax_id` are all required to be provided in latin characters. The accepted input for these fields will be limited to ASCII character range 32-126
  + We have introduced the following fields to continue accepting name and address information in its original script if desired - `local_given_name`, `local_middle_name`, `local_family_name`, `local_street_address`, `local_unit`, `local_city`, and `local_state`
* `given_name` is now required for all users
* Tax ID Number Validation
  + `tax_id` is required for securities accounts
  + If the tax ID type is `USA_SSN` or `USA_TIN` then the following must be met:
    - No values having an Area Number (first three digits) of 000 nor 666.
    - No values having a Group Number (middle two digits) of 00.
    - No values having a Serial Number (last four digits) of 0000.
    - No values all of the same digit such as 000-00-0000, 111-11-1111, 333-33-3333, 666-66- 6666, 999-99-9999, nor all increasing or decreasing characters i.e. 123-45-6789 or 987-65-4321.
    - Values must be exactly 9 characters in length after dashes have been stripped
  + All tax ID types will undergo the following validation:
    - The length must be greater than 1 character i.e. submitting 0 as a tax ID will not be permitted
    - No values all of the same digit such as 000-00-0000, 111-11-1111, 333-33-3333, 666-66- 6666, 999-99-9999, nor all increasing or decreasing characters i.e. 123-45-6789 or 987-65-4321.
    - Max length of 40 characters
    - Only letters, digits, dashes (denoted by ASCII char 45), periods, and plus (+) signs will be permitted
    - Value most contain digits (i.e. submitting TIN\_NOT\_ISSUED or xxx-xxx-xxxx will not be permitted)
      * As a general reminder to our partners that onboard users in regions where tax ID numbers are not issued, there is still a requirement for a unique identifier to be submitted for those users. The identifier should be either a national identity card number, passport number, permanent resident number, drivers license number, etc. We have introduced the following tax\_id\_type values to support these classifications. These are also available in our documentation [here](https://docs.alpaca.markets/reference/createaccount).
        + `NATIONAL_ID`
        + `PASSPORT`
        + `PERMANENT_RESIDENT`
        + `DRIVER_LICENSE`
        + `OTHER_GOV_ID`
* `street_address` Validation
  + No values consisting of only digits
  + Length must be greater than 1 character
  + A new validation has been introduced to the street\_address field to prevent the submission of US Post Office Boxes (PO Boxes) for a residential address. This validation is case-insensitive and detects keywords indicative of a PO Box, including: PO Box, Post Office Box, P.O. Box, and Box #. If a prohibited value is detected, the request will be blocked, returning a **422 error** with the specific message: `"street_address cannot be a P.O. Box"`. This validation applies to requests via the `POST /v1/accounts` and `PATCH /v1/accounts/{account_id}` endpoints, and partners should ensure their systems are prepared to handle this new validation error.
* Postal Code Validation
  + If country of tax residence = USA:
    - The `postal_code` attribute will be required upon account creation
    - No values less than 5 characters in length and the first 5 characters must only contain digits
    - No values greater than 10 digits
* `date_of_birth` Validation
  + No values greater than or less than 10 characters in length. Values must be in YYYY-MM-DD format.
* Email addresses, after aliases are removed, are restricted to a maxim of 60 characters in length. Alpaca defines an alias as all characters after a + sign and before the @ sign.
* State Validation
  + For all countries
    - The max length for state should not be greater than 50 characters
    - State cannot consist of only digits. It can be alphanumeric
  + If country of tax residence = USA
    - State will be limited to either the 2 letter abbreviation code for the state or the complete name of the state as defined in our documentation [here](https://docs.alpaca.markets/docs/domestic-usa-accounts)
* The `city` attribute cannot consist of only digits. It can be alphanumeric
* Whitespace validation
  + The following validation will be applied to the `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, `tax_id_type`, and `tax_id` fields on the Accounts API:
    - The space character, denoted by ASCII character 32, will be the only whitespace character we accept
    - Leading and trailing spaces present in the string will return a 422 error
    - Additionally, we will be cleaning up the existing accounts in our system that contain invalid whitespace characters. We will follow up directly with the affected partners and share the complete list of accounts and data points that we will be updating.

Updated 3 months ago

---

Ask AI

---

# IRA Accounts Overview (https://docs.alpaca.markets/docs/ira-accounts-overview)

# IRA Accounts Overview

Individual Retirement Arrangement (IRA) accounts are a retirement account type available to US tax residents. Alpaca supports both Roth IRA and Traditional IRA accounts for our Broker API customers. This page serves as a guide to understanding IRA accounts at Alpaca and how to integrate them into your application. Please note IRA accounts have to be enabled for your account to begin creating them. Please reach out to Alpaca support to enable this feature for you in sandbox.

## Account Opening

The existing [account creation request](https://docs.alpaca.markets/reference/createaccount) will be used to create an IRA account but with the addition of a few new fields such as the `account_type` and `account_sub_type` fields. There will also be some additional onboarding questions that customers must answer to create their IRA account. Please reach out to your dedicated Customer Success Manager for the complete onboarding steps you'll need to guide your customers through.

**Sample Request Body**

```
{
    "account_type": "ira",
    "account_sub_type": "roth",
    "enabled_assets": ["us_equity"],
    "contact": {
        "email_address": "[email protected]",
        "phone_number": "555-666-7788",
        "street_address": ["20 N San Mateo Dr"],
        "unit": "6G",
        "city": "San Mateo",
        "state": "CA",
        "postal_code": "12345"
    },
    "identity": {
        "given_name": "John",
        "family_name": "Smith",
        "date_of_birth": "1940-01-01",
        "tax_id": "119119119",
        "tax_id_type": "USA_SSN",
        "country_of_citizenship": "USA",
        "country_of_tax_residence": "USA",
        "funding_source": ["employment_income"],
        "annual_income_min": "30000",
        "annual_income_max": "50000",
        "liquid_net_worth_min": "100000",
        "liquid_net_worth_max": "150000",
        "marital_status": "MARRIED"
    },
    "disclosures": {
        "is_control_person": false,
        "is_affiliated_exchange_or_finra": false,
        "is_politically_exposed": false,
        "immediate_family_exposed": false,
        "employment_status": "retired"
    },
    "agreements": [
        {
            "agreement": "customer_agreement",
            "signed_at": "2020-09-11T18:13:44Z",
            "ip_address": "185.13.21.99",
            "revision": "19.2022.02"
        }    
    ],
    "beneficiaries": [
        {
            "given_name": "Jane",
            "middle_name": "middle",
            "family_name": "Smith",
            "date_of_birth": "1940-01-01",
            "tax_id": "119119119",
            "tax_id_type": "USA_SSN",
            "relationship": "spouse",
            "type": "primary",
            "share_pct": "33.34"
        },
        {
            "given_name": "John",
            "family_name": "Smith",
            "date_of_birth": "2000-01-01",
            "tax_id": "119119119",
            "tax_id_type": "USA_SSN",
            "relationship": "other",
            "type": "primary",
            "share_pct": "33.33"
        },
        {
            "given_name": "Sally",
            "family_name": "Smith",
            "date_of_birth": "2000-01-01",
            "tax_id": "119119119",
            "tax_id_type": "USA_SSN",
            "relationship": "other",
            "type": "primary",
            "share_pct": "33.33"
        }
    ]
}
```

### Same user opening a taxable brokerage account and an IRA account

If the accounts are opened within 60 days of each other and Alpaca is performing KYC on each customer then we will reuse the KYC results tied to the account opened first provided that the original account was already approved. This means that you will only be charged for one KYC run from an invoicing perspective if these conditions are met. Please note this functionality has to be explicitly enabled for you so please reach out to Alpaca support to enable this feature to begin testing.

Regardless of the time that has passed since the user opened their first account, the user does not have to go through the full onboarding flow again. You can pre-populate the onboarding questions with their original answers, prompt the user to confirm information is still correct and allow them to modify any fields that need to be corrected, and present the user with the relevant account agreement and disclosure language to finish opening their second account.

## Modifying Beneficiaries After Account Creation

Beneficiaries are especially important for IRA accounts since they are meant to be used to generate savings over a long period of time. However, to ensure a smooth onboarding experience, specifying beneficiaries at the time of account opening is not required. Beneficiaries can be set or updated anytime after account creation. This function would be managed via the existing [account update endpoint](https://docs.alpaca.markets/reference/patchaccount).

> 🚧
>
> ### Important note: updating beneficiaries via this endpoint will replace ALL existing beneficiaries associated with the IRA account.

**Sample Request Body**

```
{
    "beneficiaries": [
        {
            "given_name": "Jane",
            "middle_name": "middle",
            "family_name": "Smith",
            "date_of_birth": "1940-01-01",
            "tax_id": "119119119",
            "tax_id_type": "USA_SSN",
            "relationship": "spouse",
            "type": "primary",
            "share_pct": "50"
        },
        {
            "given_name": "Sally",
            "family_name": "Smith",
            "date_of_birth": "2000-01-01",
            "tax_id": "119119119",
            "tax_id_type": "USA_SSN",
            "relationship": "other",
            "type": "primary",
            "share_pct": "50"
        }
    ]
}
```

### Spousal Consent in Community States

Please note that Alpaca is required to collect spousal consent in the event that a user has an IRA account, is married, does not list their spouse as a beneficiary, and resides in a community property state. The community property states as of October 2024 are Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin. Alpaca will reach out to you with a list of accounts we are required to collect spousal consent on a manual basis as needed.

## How to Process a Contribution (IRA Deposits)

Deposits to IRA accounts are considered contributions from the IRS’ perspective and Alpaca needs to collect additional data that isn't required for typical taxable brokerage accounts. The IRS sets specific contribution limits for how much a customer can deposit into their IRA account per tax year and allows contributions to the previous tax year up until the official deadline of April 15th.

Given this, Alpaca will require "tax\_year" as an input parameter when depositing via ACH using our existing [request transfer endpoint](https://docs.alpaca.markets/reference/createtransferforaccount). If a deposit is made via a push transaction, (i.e. a wire deposit or an ACH push transaction), the system will automatically default to classify the contribution for the current tax year.

**Sample Request Body**

```
{
    "transfer_type": "ach",
    "relationship_id": "99eeed85-dcca-4d4b-b3ed-42d597a2f96d",
    "amount": "7000",
    "direction": "INCOMING",
    "ira": {
      "tax_year": "2024"
    }
}
```

### Handling Excess Contributions

As mentioned above, the IRS imposes specific limits on how much a customer can contribute to their IRA in a given tax year. If a customer exceeds this limit, they may incur penalties during tax season. It’s advisable to monitor whether your customers are adhering to these IRS limits and, if not, send them a courtesy notice, guiding them to withdraw the excess funds to avoid penalties.

Alpaca simplifies this process by providing a [new endpoint](https://docs.alpaca.markets/reference/listiraexcesscontritbutions) that allows you to pull the list of accounts that have over contributed on demand. It’s important to note that the exact limit the IRS enforces for each individual will change depending on their income bracket, tax filing status, and age – Alpaca only monitors against the maximum allowed limit by age. Since the contribution limit applies to all IRAs, including those held at other brokerages, customers are ultimately responsible for monitoring their own limits. Providing a notification to your customers as a courtesy is recommended but not required.

## How to Process a Distribution (IRA Withdrawals)

Withdrawals from IRA accounts are considered distributions from the IRS’ perspective. Since these are designed for long term savings and retirement, there are several IRS rules that disincentivize individuals from withdrawing from an IRA account before they reach retirement age but there are limited exceptions that allow users to withdraw penalty free.

Because of this, the IRS requires we provide a reason for each distribution which must be collected from your end customer. There are also federal and state tax withholding elections that the customer must specify when requesting a distribution. As a guideline, the IRS requires 10% federal tax withholding unless the customer explicitly opts out. US state withholding requirements vary, so state-specific guidelines should be followed. Alpaca will withhold the elected amount (by deducting from the requested withdrawal amount) and remit payment to the IRS. Distributions will be processed via the existing [withdrawal request endpoint.](https://docs.alpaca.markets/reference/createtransferforaccount)

**Sample Request Body**

```
{
  "transfer_type": "ach",
  "relationship_id": "1b6bb433-3ce3-40fa-8e08-15164a408c6b",
  "amount": "143",
  "direction": "OUTGOING",
  "ira": {
    "distribution_reason": "normal_roth",
    "tax_withholding": {
        "fed_pct": "10",
        "state_pct": "5.5"
    }
  }
}
```

### DistributionReason ENUMs

We highly recommend researching when each tax code would be used for a given scenario and designing your frontend flow in a way that helps the user easily identify the correct reason to use. A brief description of each distribution reason Alpaca will support is provided below but the IRS guidelines should be considered the source of truth on this. Please also note that Alpaca will not support all IRA distribution types. If there is another distribution reason the user is eligible for (i.e. a disability distribution) the user would have to take an early distribution from Alpaca and work directly with the IRS to be reimbursed for any penalties that they may have incurred during tax season.

| Attribute | Description | Applicable for Traditional IRAs | Applicable for Roth IRAs | IRS Tax Code |
| --- | --- | --- | --- | --- |
| `normal` | Normal Distribution | X |  | 7 |
| `normal_roth` | Qualified distribution from a Roth IRA (IRA 5-year holding period has been reached and customer is over 59½, or is dead, or is disabled) |  | X | Q |
| `early_no_exception` | Early distribution, no known exception | X |  | 1 |
| `excess_removal_current_year` | Excess contributions plus earnings/excess deferrals (and/or earnings) taxable in current year | X |  | 8 |
| `excess_removal_current_year_under_59.5` | Removal of Excess Plus Earning/Excess Deferrals Taxable in current yr - < 59.5 | X |  | 81 |
| `excess_removal_roth` | Removal of Excess from a Roth IRA |  | X | 8J |
| `excess_removal_1_year_prior_roth` | Excess contributions plus earnings in prior year - Roth IRA |  | X | PJ |
| `excess_removal_1_year_prior_over_59.5` | Removal of Excess Plus Earning/Excess Deferrals Taxable in prior year - >59½ | X |  | P |
| `excess_removal_1_year_prior_under_59.5` | Removal of Excess Plus Earning/Excess Deferrals Taxable in prior year - <59½ | X |  | P1 |
| `early_roth_no_exception` | Early distribution from a Roth IRA, no known exception (when Code T or Code Q do not apply) |  | X | J |

## Other Important Considerations

1. Tax Documents & Required Minimum Distribution (RMD) Notices
   1. For IRA accounts, the primary documents provided will be tax statements and RMD notices for customers who are of RMD age. These documents will be attached to the account as an account document and available for download via the [existing Broker API endpoint](https://docs.alpaca.markets/reference/downloaddocfromaccount-1?ref=alpaca.markets).
2. Updating Contributions and Distributions
   1. There may be instances where a customer needs to make a correction on a contribution or distribution from time to time. For example, if a customer made a wire deposit and could not specify the tax year for the contribution – as a result, they might want to apply it to the prior tax year vs current. For these types of cases, it’s recommended that you reach out to [[email protected]](/cdn-cgi/l/email-protection#066474696d63747573767669747246676a76676567286b67746d637275) to handle each correction on a case by case basis.
3. Pricing
   1. Please reach out to your sales representative to inquire about IRA pricing for your use case. You will need to sign a pricing amendment if the pricing is not outlined in your initial contract with Alpaca before the product can be enabled for you in production.

## Notable Product Limitations

* RMD amount calculations will not be offered by Alpaca
* There is currently a limitation of 1 unique email address per user
* IRA accounts are by default setup with limited margin (1x margin)
* Crypto is not be supported for IRAs at this time
* Options (up to level 2) is supported for IRAs
* IRA transfers and rollovers and not yet supported at Alpaca
* Currently the API does not allow transfers between a customers' taxable account and their IRA account

## Resources

* [IRA Blog Post](https://alpaca.markets/blog/ira-accounts-now-available-through-alpacas-broker-api/)
* [IRA FAQs](https://alpaca.markets/support/tag/ira)
* [IRA Learn Article](https://alpaca.markets/learn/getting-started-with-ira-accounts-for-broker-api/)

Updated 5 months ago

---

Ask AI

---

# Crypto Trading (https://docs.alpaca.markets/docs/crypto-trading-1)

# Crypto Trading

Alpaca supports crypto trading 24 hours a day, every day. Crypto is available for testing in sandbox, in case you want to allow your users to trade crypto please reach out to the Sales or Developer Success team.

> 🌍
>
> ### To view the supported US regions for crypto trading, click [here](https://alpaca.markets/support/what-regions-support-cryptocurrency-trading).

# Enabling Crypto for an Account

To enable crypto trading for an account, the crypto agreements must be signed by the user. All account balances will represent the crypto trading activities.

In the case of new users, the crypto agreement can be submitted via the Accounts API where `crypto_agreement` is part of the agreements attribute.

*Part of the request*

JSON

```
{
  "agreements": [
    {
      "agreement": "crypto_agreement",
      "signed_at": "2023-01-01T18:09:33Z"
    }
  ]
}
```

In the case of existing users the account has to be updated with the `crypto_agreement` which can be submitted on the `PATCH /v1/accounts/{account_id}` endpoint.

*Part of the request*

JSON

```
{
  "agreements": [
    {
      "agreement": "crypto_agreement",
      "signed_at": "2023-01-01T18:13:44Z",
      "ip_address": "185.13.21.99"
    }
  ]
}
```

Once the crypto agreement is added to the user account no further edits can be made to the agreements.

To determine whether the account is all set to start trading crypto, use the `crypto_status` attribute from the Account API endpoint response object.

*Sample Response*

JSON

```
{
  "id": "9feee08f-22d2-4804-89c1-bf01166aad52",
  "account_number": "943690069",
  "status": "ACTIVE",
  "crypto_status": "ACTIVE"
}
```

| Attribute | Description |
| --- | --- |
| INACTIVE | Account not enabled to trade crypto live |
| ACTIVE | Crypto account is active and can start trading |
| SUBMISSION\_FAILED | Account submissions has failed |

# Supported Assets

We have over 20 coins available to trade via our APIs. We constantly evaluate the list and aim to to grow the number of supported currencies.

Tradable cryptocurrencies can be identified through the [Assets API](/reference/getassets) where the asset entity has `class = crypto` and `tradable = true`.

JSON

```
{
  "id": "64bbff51-59d6-4b3c-9351-13ad85e3c752",
  "class": "crypto",
  "exchange": "CRXL",
  "symbol": "BTC/USD",
  "name": "Bitcoin",
  "status": "active",
  "tradable": true,
  "marginable": false,
  "shortable": false,
  "easy_to_borrow": false,
  "fractionable": true
}
```

Please note that the symbol appears with `USD`, such as `BTC/USD` instead of `BTC`.

> 🚧
>
> ### Crypto Fee Revenue Notice
>
> If you enable non-USD crypto trading you will receive fees in the quote currency. Currently, non-USD quote crypto assets are BTC, USDC and USDT. As a broker business you would need to be ready to handle collecting crypto fees plus taking care of the necessary conversions if needed.

## Minimum Order Size

The minimum quantity value that is accepted in an order. This value is calculated dynamically based on the selected notional equivalent minimum, based on the last close price of the relevant asset(s). The maximum decimal places accepted is 9 i.e 0.000000001 for all crypto assets.

For `USD` pairs, the minimum order size calculation is: 1/USD asset price.

For `BTC`, `ETH` and `USDT` pairs, the minimum order size is `0.000000002`.

## Min Trade Increment

The minimum quantity allowed to be added to the `min_order_size`. E.g. if 0.1 we accept an order for 1.1 but we won’t accept 0.9 because it’s under the `min_order_size`. The maximum decimal places accepted are 9 i.e 0.000000001 for all crypto assets.

Price Increment: The minimum notional value that is accepted in an order. Similar to Min Order Size but for notional orders. The maximum decimal places accepted are 9 i.e 0.000000001 for all crypto assets.

All cryptocurrency assets are fractionable but the supported decimal points vary depending on the cryptocurrency.

# Supported Orders

When submitting crypto orders through the Orders API, Market, Limit and Stop Limit orders are supported while the supported `time_in_force` values are `gtc`, and `ioc`. We accept fractional orders as well with either `notional` or `qty` provided.

## Required Disclosures

Below you will find required disclosure templates to safely support crypto in your applications as a broker with Alpaca.

### Onboarding Disclosures

When onboarding your users as a broker offering crypto the following disclosure is required. During your onboarding flow make sure the user is able to read and affirmatively acknowledge, such as through a separate checkbox, the following text:

I have read, understood, and agree to be bound by Alpaca Crypto LLC and [your legal entity] account terms, and all other terms, disclosures and disclaimers applicable to me, as referenced in the Alpaca Crypto Agreement. I also acknowledge that the Alpaca Crypto Agreement contains a pre-dispute arbitration clause in Section 26.

### Buy/Sell Order Screen Disclosures

As a broker enabling the placement of cryptocurrency orders, the following disclosures should appear on the user’s order entry screen, on the app or website, immediately prior to the user submitting the buy or sell order.

#### Buy Order Disclosure

By placing an order to buy [$ amount of / number of ] [cryptocurrency], you are directing and authorizing Alpaca Securities LLC to transfer funds necessary to cover the purchase costs from your Alpaca Securities LLC account into your Alpaca Crypto LLC account. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC. [Disclosures](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://files.alpaca.markets/disclosures/library/CryptoRiskDisclosures.pdf).

#### Sell Order Disclosure

By placing an order to sell [$ amount of / number of ] [cryptocurrency], you are directing and authorizing Alpaca Crypto LLC to transfer settled funds from the sale into your Alpaca Securities LLC account. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC. Disclosures.

#### Crypto Pairs Order Disclosure

By placing an order, you are directing and authorizing Alpaca Crypto LLC to exchange [X amount of Cryptocurrency] for [Y amount of cryptocurrency]. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC.

# Margin and Short Selling

Cryptocurrencies are non-marginable. This means that you cannot use leverage to buy them and orders are evaluated against `non_marginable_buying_power`.

Cryptocurrencies are not shortable.

# Trading Hours

Crypto trading is offered for 24 hours everyday and your orders will be executed throughout the day.

# Trading Limits

Currently, an order (buy or sell) must not exceed $200k in notional. This is per an order.

# Crypto Order Commissions

Brokers can charge a commission on each crypto order by including a commission parameter when submitting orders. Commission support for crypto now includes both notional and bps (basis points) commission types. The amount is specified either in the quote currency of the trading pair (for notional) or as a percentage in bps.

To enable commission support, brokers must first contact Alpaca to configure their commission structure. Once set up, the commission amount can be provided in each order request, and it will also appear in the order entity of the API response.

On all orders (regardless of commission type), the commission charged will be prorated on each execution if the order has multiple executions. For example, if 10% of the order is filled in one execution, then the commission for that execution will be 10% of the total commission.

### Commission types:

* Notional: Charges commission on a per-order basis. When the commission\_type field is omitted from the order request, this is used as the default.
* Bps: The percent commission to charge the end user on the order (expressed in basis points). Alpaca will convert the order to a notional amount for calculating the commission.

# Market Data

Alpaca provides crypto data from multiple venues.

Crypto data providers utilized by Alpaca:

| Exchange | Exchange Code |
| --- | --- |
| `CBSE` | Coinbase |
| `CRXL` | Alpaca Crypto Exchange |
| `FLCX` | Falcon X |

# Features

## Price Band Protection

The price band validation in Alpaca will prevent trades from executing outside a predefined percentage range around an external reference price. Ensures market stability and prevents extreme price fluctuations due to erroneous trades. External reference prices are derived as a weighted average from `Coinbase`, `FalconX`, and `StillmanDigital`.

Orders that would execute at an invalid price will be automatically canceled with following reasons.

1. canceled due to reference price stale – Order was canceled because the reference price used for price band validation was outdated.
2. canceled due to price band protection. Index price: `<index_price>` Price band: `<price_band>`%, Rejected price: `<maker_order_price>` – Order was about to execute at a price exceeding the allowed range

Updated 5 months ago

---

Ask AI

---

# Crypto Wallets API (https://docs.alpaca.markets/docs/crypto-wallets-api)

# Crypto Wallets API

*Please note you have to reach out to Alpaca to enable Crypto Wallets API access. Please reach out to your Customer Success Manager or your Sales Representative to enable this feature for you.*

## **Overview**

The Alpaca Crypto Wallets API enables you to deposit, withdraw, and manage cryptocurrency assets within your Alpaca account. This document explains how to use Alpaca’s Crypto Wallets API to test fund accounts with crypto assets (like USDC), verify transfers, and begin trading.

## **Supported Assets**

### **Supported Testnets & Faucets (Sandbox)**

To test deposit and withdrawal flows for different assets across supported blockchain networks, you can use the following testnet faucets. Always ensure you’re requesting tokens and interacting on the correct network (e.g., Ethereum Sepolia, Solana Devnet).

**Stablecoins**

* **USDC (Testnet/Devnet Support)**
  + Networks: Ethereum Sepolia, Solana Devnet
  + Faucet: [Circle Testnet Faucet](https://faucet.circle.com/)
* **USDG (Testnet Support)**
  + Networks: Ethereum Sepolia, Solana Devnet
  + Faucet: [Paxos Faucet](https://faucet.paxos.com/)
* **USDT (Testnet)**
  + Network: Ethereum Sepolia
  + Faucet:
    - [WeenusTokenFaucet GitHub](https://github.com/bokkypoobah/WeenusTokenFaucet?tab=readme-ov-file#testnet-ether-faucets)
    - Contract Address: [0x7439...fB9 on Etherscan](https://sepolia.etherscan.io/address/0x7439E9Bb6D8a84dd3A23fe621A30F95403F87fB9#code)

**BTC (Testnet)**

* **tBTC** — [Bitcoin Testnet4 Faucet](https://faucet.testnet4.dev/)

**Solana (Devnet)**

* [Solana Devnet Faucet – Airdrop SOL](https://faucet.solana.com/)

**ETH (Sepolia)**

* [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
* [Google Cloud Sepolia Faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)
* [QuickNode Faucet](https://faucet.quicknode.com/ethereum)

**XRP (Testnet)**

* [XRPL Tesnet Faucet](https://test.bithomp.com/en/faucet)

---

## **Getting Started: Sandbox Testing Guide**

### **Step 1: Generate Your Funding Wallet Address**

Create or retrieve your crypto funding wallet address for the desired asset:

[`GET /v1/accounts/{account_id}/wallets?asset=USDC&network=ethereum`](https://docs.alpaca.markets/reference/listcryptofundingwallets-1)

**Response:**

JSON

```
{
    "asset_id": "5d0de74f-827b-41a7-9f74-9c07c08fe55f",
    "address": "0x42a76C83014e886e639768D84EAF3573b1876844",
    "created_at": "2025-08-07T08:52:40.656166Z"
}
```

### **Step 2: Fund Your Wallet (Sandbox)**

#### **For USDC Testing:**

1. Visit the **Circle Sepolia Faucet**: <https://faucet.circle.com>
2. Paste your wallet address from Step 1
3. Click **Send**
4. Wait for ~12 block confirmations (typically 2-3 minutes)

### **Step 3: Verifying Deposits**

Monitor incoming transfers to confirm your deposit:

#### Option 1: Poll transfers API

[`GET /v1/accounts/{account_id}/wallets/transfers`](https://docs.alpaca.markets/reference/listcryptofundingtransfers-1)

**Response:**

JSON

```
[
    {
        "id": "876b1c4f-df5e-4d1b-beaa-81af7f7bd02c",
        "tx_hash": "0xaca1f6ba105a68771d966b4ce17e0992ad3d8030d127cdb18e113efa3a864992",
        "direction": "INCOMING",
        "amount": "10",
        "usd_value": "9.99707",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0x3C3380cdFb94dFEEaA41cAD9F58254AE380d752D",
        "to_address": "0x42a76C83014e886e639768D84EAF3573b1876844",
        "status": "COMPLETE",
        "created_at": "2025-08-07T10:31:41.964121Z",
        "network_fee": "0",
        "fees": "0"
    },
    {
        "id": "bf31ecca-e28c-4f9a-8e81-12bbf79836fd",
        "tx_hash": "0x849de6f0f225c18b58f3dea5a76a42a0dcba4902ce069147bb0dcd585a3e699b",
        "direction": "INCOMING",
        "amount": "5",
        "usd_value": "4.998794999999999",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "to_address": "0x42a76C83014e886e639768D84EAF3573b1876844",
        "status": "COMPLETE",
        "created_at": "2025-08-08T11:13:26.263719Z",
        "network_fee": "0",
        "fees": "0"
    }
]
```

**Status Values:**

* `PROCESSING`: Transaction submitted to blockchain
* `COMPLETE`: Funds available for trading
* `FAILED`: Transaction failed

#### Option 2: [NTA SSE event](https://docs.alpaca.markets/reference/get-v1-events-nta)

Sample event showing incoming deposit:

JSON

```
{
    "id": "a6a3f62c-d4dd-4b6f-9b3a-fb65892c9695",
    "qty": 10,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "OCT",
    "net_amount": 0,
    "description": "Deposit Transaction, transfer_id: 296f3a5b-72e8-4ec6-b1fe-77048e77e87f, tx_hash: 0x97fa0e98598d7bedf2871bc1846daa076cddafaa9046b3697b6cd89ca7304932",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9997",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:09:01.061337Z",
    "event_ulid": "01K5GG9ZC5A3CVKP5QEZ79PVEX"
}
```

  

### **Step 4: Trading with Deposited Assets (Optional)**

Convert your deposited crypto to USD buying power by selling against USD:

[`POST /v1/trading/accounts/{account_id}/orders`](https://docs.alpaca.markets/reference/createorderforaccount)

**Request Body:**

JSON

```
{
  "symbol": "USDC/USD",
  "qty": "50",
  "side": "sell",
  "type": "market", 
  "time_in_force": "day"
}
```

### **Step 5: Start Trading**

Once your USDC converts to USD buying power, you can:

* Trade equities and ETFs
* Trade other crypto pairs

In order to check your USD buying power, you can call [Retrieve Trading Details for an Account](https://docs.alpaca.markets/reference/gettradingaccount-1) API endpoint, and look for `buying_power`.

---

## **Withdrawing Crypto Assets**

### **Overview**

Withdrawing cryptocurrency from your Alpaca account requires a multi-step process to ensure fund safety:

1. **Whitelist** the destination address
2. **Verify** whitelist approval status
3. **Request** withdrawal to approved address
4. **Monitor** withdrawal status

### **Step 1: Whitelist Destination Address**

Before withdrawing, you must whitelist the destination wallet address:

[`POST v1/accounts/{account_id}/wallets/whitelists`](https://docs.alpaca.markets/reference/createwhitelistedaddress-1)

**Request Body:**

JSON

```
{
  "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
  "asset": "USDC"
}
```

**Response:**

JSON

```
[
    {
        "id": "45efdedd-28cd-4665-98b4-601d5f34ae0a",
        "chain": "ETH",
        "asset": "USDC",
        "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "created_at": "2025-08-07T13:16:46.49111Z",
        "status": "PENDING"
    }
]
```

### **Step 2: Check Whitelist Approval Status**

Monitor your whitelisted addresses to confirm approval (within 24 hours):

[`GET v1/accounts/{account_id}/wallets/whitelists`](https://docs.alpaca.markets/reference/listwhitelistedaddress-1)

**Response:**

JSON

```
[
    {
        "id": "45efdedd-28cd-4665-98b4-601d5f34ae0a",
        "chain": "ETH",
        "asset": "USDC",
        "address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "created_at": "2025-08-07T13:16:46.49111Z",
        "status": "APPROVED"
    }
]
```

### **Step 3: Request Withdrawal**

Once approved, create a withdrawal transfer:

[`POST /v1/accounts/{account_id}/wallets/transfers`](https://docs.alpaca.markets/reference/createcryptotransferforaccount-1)

**Request Body:**

JSON

```
{
 "amount": "55",
 "address": "34c18dbe-0983-4e61-b493-9578714dae23",
 "asset": "USDC"
}
```

**Response:**

JSON

```
{
    "id": "f8fe06fe-702e-4d79-802c-f31cb1677f7c",
    "tx_hash": null,
    "direction": "OUTGOING",
    "amount": "55",
    "usd_value": "54.9725",
    "chain": "ETH",
    "asset": "USDC",
    "from_address": "0xA0D2C7210D7e2112A4F7888B8658CB579226dB3B",
    "to_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
    "status": "PROCESSING",
    "created_at": "2025-09-19T08:37:25.436307Z",
    "network_fee": "20",
    "fees": "0.3025"
}
```

### **Step 4: Monitor Withdrawal Status**

Track your withdrawal progress:

#### Option 1: Poll transfers API

[`GET /v1/accounts/{account_id}/wallets/transfers`](https://docs.alpaca.markets/reference/listcryptofundingtransfers-1)

**Response:**

JSON

```
[ {
        "id": "f8fe06fe-702e-4d79-802c-f31cb1677f7c",
        "tx_hash": null,
        "direction": "OUTGOING",
        "amount": "55",
        "usd_value": "54.9725",
        "chain": "ETH",
        "asset": "USDC",
        "from_address": "0xA0D2C7210D7e2112A4F7888B8658CB579226dB3B",
        "to_address": "0xf38Ecf5764fD2dEcB0dd9C1E7513a0b6eC0dD08a",
        "status": "PROCESSING",
        "created_at": "2025-09-19T08:37:25.436307Z",
        "network_fee": "0",
        "fees": "0.3025"
    }
]
```

#### Option 2: [NTA SSE event](https://docs.alpaca.markets/reference/get-v1-events-nta)

Sample event showing outgoing withdrawals:

JSON

```
{
    "id": "a554262e-71dc-4a02-a0c0-271bcb9480e4",
    "qty": -54.6975,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "OCT",
    "net_amount": 0,
    "description": "Withdrawal Transaction, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821881Z",
    "event_ulid": "01K5GJFGQDE4WQME5F38ZTXSTS"
}
```

You can also expect to see `CFEE` depending on your correspondent configuration linked to the withdrawal transactions.

JSON

```
{
    "id": "5abfdea7-de14-4985-8632-428e8ffb7aa5",
    "qty": 1.3475,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Correspondent Transaction Fee, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.819319Z",
    "event_ulid": "01K5GJFGQBCWVHV4YDV13QW68V"
}

{
    "id": "106a8e17-af4f-4dd1-a0a7-463ea035cb12",
    "qty": -0.275,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Transaction Fee, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821196Z",
    "event_ulid": "01K5GJFGQDDT69PTT6K37N1CQN"
}

{
    "id": "472f9c57-22b7-41a0-82b2-396e51fb99cf",
    "qty": -1.375,
    "cusip": "USDC12345",
    "status": "executed",
    "symbol": "USDCUSD",
    "entry_type": "CFEE",
    "net_amount": 0,
    "description": "Wallet Correspondent Transaction Income, transfer_id: f8fe06fe-702e-4d79-802c-f31cb1677f7c, tx_hash: 0xceaf451d26a11aa43681e6f9336987325b6c1c347d64f59b45811050d8789a24",
    "settle_date": "2025-09-19",
    "system_date": "2025-09-19",
    "price": "0.9995",
    "per_share_amount": null,
    "account_id": "34c18dbe-0983-4e61-b493-9578714dae23",
    "at": "2025-09-19T08:46:59.821937Z",
    "event_ulid": "01K5GJFGQDE5RGMVCJBDS42K0P"
}
```

Updated about 1 month ago

---

Ask AI

---

# Funding Accounts (https://docs.alpaca.markets/docs/funding-accounts)

# Funding Accounts

The funding process can vary depending on your setup and region and we support many cases, but everyone can do the same in the sandbox environment.

# Sandbox Funding

In the sandbox environment, Transfer API simulates deposits and withdrawals to/from an account. The target account is immediately credited or debited upon such a request. Once an account is credited, the account can start trading with the Orders API.

# ACH (US Domestic)

For US ACH, you will need to use Plaid to obtain the user’s bank account information. You then pass the information to Alpaca using [ACH API](/reference/createrecipientbank) to create a Bank Link object. Once a Bank Link between a user and their bank account is established, then you can initiate both deposit and withdrawal transactions using the [Transfers API](/reference/createtransferforaccount).

# Wire

Beginning June 1, 2022, we will begin charging for outgoing wires, both domestic and international. To help you provide the optimal customer experience we support two different flows for handling the fees:

1. **The end user pays the fee for every outgoing wire transfer that they initiate.** The `fee_payment_method` field will be equal to user in this case. It’s important to note that the fee stated in your contract with Alpaca will automatically be deducted from the amount entered via the Transfers API so we strongly recommend adding a notice to your UI stating that the end user will incur a fee and they should incorporate that fee into their withdrawal request.
2. You will also have the option to **pay the fee on behalf of your user for any given transfer**. When creating the transfer, you will have to set the `fee_payment_method` field to invoice. The fee stated in your contract will not be deducted from the amount entered via the Transfers API but you will be charged this fee in your next monthly invoice.

## Wire (US Domestic)

You can initiate a withdrawal transaction with wire transfer using the [Transfers API](/reference/createtransferforaccount). You need to create a bank object before that. For US domestic wire transactions, we will need ABA/routing number and the account number. You can supply additional text in each transaction.

**In order for us to receive the deposits and book automatically, we need an “FFC” instruction in each incoming wire transaction.** Please contact us for more details.

## International Wire (SWIFT)

Alpaca supports international wire transfers and the API endpoint is the same as the US domestic case. You need to provide the SWIFT code and account number of the beneficiary, as well as the address and name of the receiving bank.

The FFC instructions above work for international wires too.

# Cash Pooling

If you wish and are eligible, you can send customer deposits in a bulk to your firm account first and reconcile later using the [Journals API](/reference/createjournal).

We need to review the entire flow first to allow you to do so, and also you may need a local license to implement this process. Please check your counsel for the local requirements.

## Travel Rule

In an effort to fight the criminal financial transactions, FinCEN enacted the [Travel Rule](https://www.fincen.gov/sites/default/files/advisory/advissu7.pdf), which mandates that financial institutions transmitting funds more than $3,000 must share specific information with the recipient institutions. FAFT further adopted this from FinCEN to set the global standard, to regulate financial institutions including virtual asset service providers (VASPs) and is being implemented by many countries. **However, Alpaca requires adherence to this policy for all incoming deposits, regardless of amount.**

Under this rule, financial institutions that transmit the funds are required to submit the following information to the recipient financial institutions (financial institutions here include banks and nonbanks; essentially any party that initiates the transfers).

When using the following APIs, you will need to ensure compliance with the Travel Rule by including breakdowns and transmitter information where applicable.

* Journals API
  + [Create a Journal](https://docs.alpaca.markets/reference/createjournal)
* Instant Funding API - There are two APIs under instant funding that accept transmitter information, the recommendation is to pass the information at the time of settlement creation.
  + [Create an intant funding request](https://docs.alpaca.markets/reference/post-v1-instant-funding)
  + [Create a new settlement](https://docs.alpaca.markets/reference/post-v1-instant-funding-settlements)

The table given below gives an overview of the relevant fields for both the APIs along with the field descriptions.

| Journals | Instant Funding | Field description |
| --- | --- | --- |
| `transmitter_name` | `originator_full_name` | The full name of the customer who is initiating the transaction. |
| `transmitter_account_number` | `originator_bank_account_number` | The bank account number of the customer or the account number on broker partner's system that can be used to uniquely identify the customer. |
| `transmitter_address` | `originator_street_address`  `originator_state`  `originator_city`  `originator_country` | The street, city, state and country of the financial institution responsible for transmitting the funds. |
| `transmitter_financial_institution` | `originator_bank_name` | The name of the transmitter's financial institution |
|  | `other_identifying_information` | Recommended to be the originating bank's reference number for the transfer |

**Please note that the purpose of this requirement is for the investigators to track the flow of funds in case they need to. Failure to do so could cause a civil enforcement.**

Alpaca retains the collected information for at least five years. If the journal activities are used as part of the money transfer (other than cash movement within Alpaca), and if the journal requests don’t contain the transmitter information, we may contact you.

# Instant Deposit (Beta)

As international money transfers can take days usually, under certain conditions, Alpaca supports instant deposit for better user experience. Please contact us for more details.

# Post-trade Settlement

We support the post-trade settlement process (higher requirements and restrictions apply). Please contact us for more details.

Updated 5 months ago

---

Ask AI

---

# Journals API (https://docs.alpaca.markets/docs/funding-via-journals)

# Journals API

Journals API allows you to move cash or securities from one account to another.

For more on creating and retrieving journals please check out our [API reference section on journals](https://docs.alpaca.markets/reference/createjournal).

The most common use case is [cash pooling](https://docs.alpaca.markets/docs/funding-accounts#cash-pooling), a funding model where you can send bulk wires into your firm account and then move the money into each individual user account.

![Cash pooling funds flow](https://files.readme.io/c5b61f3-image.png)

Cash pooling funds flow

There are two types of journals:

**JNLC**  
Journal cash between accounts. You can simulate instant funding in both sandbox and production by journaling funds between your pre-funded sweep accounts and a user’s account.

You can only journal cash from a firm account to a user account and vice-versa but not from customer to customer.

**JNLS**  
Journal securities between accounts. Reward your users upon signing up or referring others by journaling small quantities of shares into their portfolios.

You can only journal securities from a firm account to a user account and not vice-versa or customer-to-customer.

## Journals Status

The most common status flow for journals is quite simple:

1. Upon creation, the journal will be created in a `queued` state.
2. Then, the journal will be `sent_to_clearing` meaning that the request has been submitted to our books and records system.
3. Lastly, if there are no issues the journal will be `executed`, meaning that the cash or securities have been successfully moved into the receiving account.

Still, there are other cases in which the journal is `rejected`, `refused` or requires manual intervention from Alpaca's cashiering team.

| Status | Description |
| --- | --- |
| `queued` | This is the initial status when the journal is still in the queue to be processed. |
| `sent_to_clearing` | The journal has been sent to be processed by Alpaca’s booking system. |
| `executed` | The journal has been completed and the balances have been updated for the accounts involved in the transaction. In some rare cases, journals can be reversed from this status by Alpaca's cashiering team if the transaction is not permitted. |
| `pending` | The journal is pending to be processed as it requires manual approval from Alpaca operations, for example, this can be caused by hitting the [journal limits](https://docs.alpaca.markets/edit/broker-api-faq). |
| `rejected` | The journal has been manually rejected. |
| `canceled` | The journal has been canceled, either via an API request or by Alpaca's operations team. |
| `refused` | The journal was never posted in Alpaca's ledger, probably because some of the preliminary checks failed. A common example would be a replayed request in close succession, where the first request is executed and the second request fails the balance check. |
| `correct` | The journal has been manually corrected. The previously executed journal is cancelled and a new journal with the correct amount is created. |
| `deleted` | The journal has been deleted from our ledger system. |

![Journal statuses flowchart](https://files.readme.io/8b024b3-image.png)

Journal statuses flowchart

Updated 5 months ago

---

Ask AI

---

# Funding Wallets (https://docs.alpaca.markets/docs/funding-wallets)

# Funding Wallets

Funding Wallets for Broker API allows you to create a dedicated wallet with a distinct account number for each user to deposit funds into.

# **Deposit Flow**

1. If funding wallet has not yet been created, [create a funding wallet](https://docs.alpaca.markets/reference/createfundingwallet#/)
2. [Retrieve funding wallet details](https://docs.alpaca.markets/reference/getfundingwallet#/)
3. [Retrieve funding details for the funding wallet](https://docs.alpaca.markets/reference/listfundingdetails#/)
4. Create a deposit request
   1. In sandbox, this can be simulated via this [endpoint](https://docs.alpaca.markets/reference/demodepositfunding#/)
   2. In production, customer initiates a deposit from the external bank to the funding details from #3
5. [Check the status of transfers](https://docs.alpaca.markets/reference/getfundingwallettransfers#/)

![](https://files.readme.io/7dcb6ad-Funding_wallet_docs_explanation_Deposit2x.png)

# **Withdrawal Flow**

1. If recipient bank has not yet been created, [create a recipient bank](https://docs.alpaca.markets/reference/createfundingwalletrecipientbank#/)
   1. Do note that depending on the country and beneficiary, the required fields might differ.
2. [Retrieve recipient bank details](https://docs.alpaca.markets/reference/getfundingwalletrecipientbank#/)
3. [Create a withdrawal request](https://docs.alpaca.markets/reference/createfundingwalletwithdrawal-1)
4. [Check the status of transfers](https://docs.alpaca.markets/reference/getfundingwallettransfers#/)

![](https://files.readme.io/2a7393d-Funding_Wallets2x_2.png)

# **Statuses and Descriptions**

The table below details the possible statuses and their descriptions. Transfers cannot be canceled, and `complete`, `rejected`, `failed` are terminal statuses.

| Status | Description |
| --- | --- |
| Pending | The transfer is pending to be processed. |
| Executed | The transfer has been sent to the bank. |
| Complete | The transfer has been settled and the balances have been updated for the accounts involved in the transaction. |
| Rejected | The transfer has been rejected by the bank, this is usually due to invalid input. |
| Failed | The transfer has failed, this is usually due to bank errors. |

You can read more in this [blog post](https://alpaca.markets/learn/getting-started-with-funding-wallets-for-broker-api/) and our [FAQs](https://alpaca.markets/support/funding-wallets-for-broker-api-2).

# **FAQ**

See full list of FAQs for Funding Wallets [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2).

1. **What local currencies are supported?**

The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these local currencies, you can send a swift wire in that local currency for it to be converted to USD. You can also withdraw in these local currencies via a swift wire.

2. **What regions are supported for local rail deposits?**

The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, local transfers can be converted to USD.

3. **What regions are supported for local rail withdrawals?**

The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, USD can be converted to local currency and paid out locally.

4. **What regions are supported for deposits to Funding Wallets?**

The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, we can support deposits via both local rails and swift wires. If a region is not listed here, that means that Currency Cloud (our partner) does not accept deposits from that region due to their own internal risk rating of that region.

5. **Can I test the flow in sandbox?**

Yes the end to end flow can be tested in sandbox using the [demo deposit endpoint](https://docs.alpaca.markets/reference/demodepositfunding#/) to mock receiving a push deposit in the sandbox environment. The only exception to note though is that testing the end to end flow in sandbox using local rails in the US is not currently supported. This is due to a limitation with Currencycloud that prevents us from fetching the local rail deposit instructions on a per account basis. This issue is only limited to the sandbox environment and the end to end flow is functional in the limited live and production environments.

Updated 4 months ago

---

Ask AI

---

# ACH Funding (https://docs.alpaca.markets/docs/ach-funding)

# ACH Funding

## Plaid Integration for Bank Transfers

We have integrated with Plaid to allow you to seamlessly link your Plaid account to Alpaca. The integration will allow your end-users to verify their account instantly through Plaid's trusted front-end module.

Leveraging this allows you to generate Plaid Processor Tokens on behalf of your end-users, which allows Alpaca to immediately retrieve a user's bank details in order to deposit or withdraw funds on the Alpaca platform.

You can utilize your Plaid account and activate the Alpaca integration within the Plaid dashboard.

The integration requires [Plaid API Keys](https://plaid.com/docs/auth/partnerships/alpaca/)

### Obtaining a Plaid Processor Token

A Plaid processor token is used to enable Plaid integrations with partners. After a customer connects their bank using Plaid Link, a processor token can be generated at any time. Please refer to the Plaid Processor Token using Alpaca page for creating a token and additional details.

Exchange token

cURL

```
curl -X POST https://sandbox.plaid.com/item/public_token/exchange 
	-H 'Content-Type: application/json' 
	-d '{ 
		"client_id": "PLAID_CLIENT_ID", 
		"secret": "PLAID_SECRET", 
		"public_token": "PUBLIC_TOKEN" 
}'
```

Create a processor token for a specific account id.

cURL

```
curl -X POST https://sandbox.plaid.com/processor/token/create 
	-H 'Content-Type: application/json' 
	-d '{
		"client_id": "PLAID_CLIENT_ID", 
		"secret": "PLAID_SECRET", 
		"access_token": "ACCESS_TOKEN", 
		"account_id": "ACCOUNT_ID", 
		"processor": "alpaca" 
}'
```

For a valid request, the API will return a JSON response similar to:

JSON

```
{ 
  "processor_token": "processor-sandbox-0asd1-a92nc", 
  "request_id": "m8MDnv9okwxFNBV" 
}
```

### Processor Token Flow

![](https://files.readme.io/c06c778-image.png)

1. End-user links bank account using Plaid.
2. Plaid returns a public token to you.
3. You will submit a public token to Plaid in exchange for an access token.
4. You will submit access token to Plaid's /processor/token/create endpoint and receive Processor Token (specific to Alpaca).
5. You will make a call to the processor endpoint to pass Alpaca the processor token, to initiate the payment. To pass the processor token use the ACH relationships endpoint (Link).

#### Sample Request

POST `/v1/accounts/{account_id}/ach_relationships`

JSON

```
{
  "processor_token": "processor-sandbox-161c86dd-d470-47e9-a741-d381c2b2cb6f"
}
```

#### Sample response

JSON

```
{
  "id": "794c3c51-71a8-4186-b5d0-247b6fb4045e",
  "account_id": "9d587d7a-7b2c-494f-8ad8-5796bfca0866",
  "created_at": "2021-04-08T23:01:53.35743328Z",
  "updated_at": "2021-04-08T23:01:53.35743328Z",
  "status": "QUEUED",
  "account_owner_name": "John Doe",
  "nickname": "Bank of America Checking"
}
```

6. Alpaca makes a call to Plaid to retrieve the Account and Routing number using the processor token.
7. Alpaca saves the processor token and account and routing number internally for future use. Alpaca uses account information for NACHA file creation and processing.

\*Can include Auth, Identity, Balance info - if the broker API wants to initiate a transfer, we use the transfer endpoint.

### ACH Status Flow

![](https://files.readme.io/51382cd-image.png)

Updated 4 months ago

---

Ask AI

---

# Instant Funding (https://docs.alpaca.markets/docs/instant-funding)

# Instant Funding

Instant Funding for Broker API, allows broker partners to offer their customers instant access to funds by creating an instant funding transfer i.e. extending buying power at the customer account level. This enables customers to begin trading immediately without the need for funds to arrive and settle at Alpaca.

## Key Features

Customers can access instant buying power allowing them to trade immediately.
Partners do not have to pre-fund or settle funds with Alpaca on T+0 for stock trading
The ability for a partner to set specific limits on end-user accounts for instant funding (by default USD 1000)
Partners have the option to create an additional revenue stream by configuring a flexible fee mark-up for customers

## Cutoffs & Interest Requirements

### Batching for Settlement:

All instant funding transfers within a 24-hour window (from 8 PM ET the previous day to 8 PM ET the current day) are grouped for settlement in the next cycle. The settlement of these instant transfers must be completed before 1 PM on T+1. Each settlement cycle has a report associated with it which can be obtained from the instant funding reports endpoint described here.

### Late Payment & Interest Charges:

Instant funding transfers not settled by 1 PM ET on T+1 will incur late payment interest which is invoiced monthly to the partner.
Penalty interest on late payments is calculated at FED UB + 8% (based on FRED Economic Data) and it is charged to the partner
Unreconciled instant funding transfers are automatically canceled at 8 PM ET on T+1 (date of settlement). The account may incur a margin interest rate (documented here) and end up in a debit balance if the user has already spent the instant funding credit.

### How it Works

Broker partners will collect funds from your customers and upon receipt of each payment you'll then call the Instant Funding API to create an instant funding transfer. This will extend the buying power to each end user.
The instant funding reports endpoint can be used to get the detail and summary report for the amount owed. The detailed view will give the breakdown of the amount owed for the instant funding transfer and the summary view will give the cumulative value.

You will then send one wire payment to Alpaca to settle the outstanding instant funding transfer by T+1 (the next business day) by 1 pm ET. This will be followed by using the settlement API to trigger the settlement which will check for funds in the SI account and perform the settlement.
Given below is a detailed overview of the process along with the working of the relevant APIs.

![This flow is illustrated in the diagram above](https://files.readme.io/bec23dfc4ade2879ab99ec6c3a0cc6a3149d78ec0845dc2877bc8d30af461290-if_process.png)

This flow is illustrated in the diagram above

## How to Create an Instant Funding Transfer

### Step 1: [Create an Instant Funding Transfer](https://docs.alpaca.markets/reference/post-v1-instant-funding-settlements)

You must specify the account you would like to credit with an instant funding transfer, the firm account the buying power will be borrowed from, and the amount to credit.

![](https://files.readme.io/dac3fbd145d1bcee7a7b4c4768c8a909825a5a92fba5d8d297c5785c50e1e1e4-ifguide.png)

**Request**
`POST v1/instant_funding`

JSON

```
{
 "account_no": "{ACCOUNT_NO}",
 "source_account_no": "{ACCOUNT_NO}",
 "amount": "20",
}
```

**Response**

JSON

```
{
  "account_no": "{ACCOUNT_NO}",
  "amount": "20",
  "created_at": "2024-11-11T08:20:10.726356556-05:00",
  "deadline": "2024-11-13",
  "fees": [],
  "id": "fcc6d9fc-ce36-484a-bd86-a27b98c2d1ab",
  "interests": [],
  "remaining_payable": "20",
  "source_account_no": "{ACCOUNT_NO}",
  "status": "PENDING",
  "system_date": "2024-11-12",
  "total_interest": "0"
}
```

Instant funding transfer executed (before settlement)

JSON

```
 {  
   "id": "20241111000000000::6b784928-f314-47bc-905f-0a49ebc9e413",  
   "account_id": "{ACCOUNT_ID}",  
   "activity_type": "MEM",  
   "date": "2024-11-11",  
   "net_amount": "0",  
   "description": "type: instant_funding_memopost, transfer_id: fcc6d9fc-ce36-484a-bd86-a27b98c2d1ab",  
   "symbol": "INSTANTUSD",  
   "qty": "20",  
   "status": "executed"  
 }
```

Instant funding transfer canceled (after settlement or after failed reconciliation)

JSON

```
{  
  "id": "20241111000000000::6b784928-f314-47bc-905f-0a49ebc9e413",  
  "account_id": "{ACCOUNT_ID}",  
  "activity_type": "MEM",  
  "date": "2024-11-11",  
  "net_amount": "0",  
  "description": "type: instant_funding_memopost, transfer_id: fcc6d9fc-ce36-484a-bd86-a27b98c2d1ab",  
  "symbol": "INSTANTUSD",  
  "qty": "20",  
  "status": "canceled"  
}
```

CSD executed (after settlement)

JSON

```
{  
  "id": "20241111000000000::daa5e4e9-7974-4273-a926-7ab0647d8850",  
  "account_id": "{ACCOUNT_ID}",  
  "activity_type": "CSD",  
  "date": "2024-11-11",  
  "net_amount": "20",  
  "description": "type: instant_funding_deposit, transfer_id: fcc6d9fc-ce36-484a-bd86-a27b98c2d1ab, settlement_id: 28f27c76-ea14-4d4c-8a04-8f666b14a224",  
  "status": "executed"  
}
```

### Step 1.1: [Check status of an Instant Funding Transfer](https://docs.alpaca.markets/reference/get-v1-instant-funding-single)

Fetch a specific instant funding transfer to check the current status of the transfer.

**Request**

`GET v1/instant_funding/:instant_funding_id`

**Response**

JSON

```
{  
    "account_no": "{ACCOUNT_NO}",  
    "amount": "20",  
    "created_at": "2024-09-10T09:12:36.88272Z",  
    "deadline": "2024-09-11",  
    "fees": [],  
    "id": "d96bdc91-6d1c-49b5-a3c3-03f16c70321b",  
    "interests": [],  
    "remaining_payable": "20",  
    "source_account_no": "{ACCOUNT_NO}",  
    "status": "EXECUTED",  
    "system_date": "2024-09-10",  
    "total_interest": "0"  
}
```

Additionally, all instant funding transfers can be listed using the following API

**Request**

`GET v1/instant_funding?sort_by=created_at&sort_order=DESC`

**Response**

JSON

```
{  
    "account_no": "{ACCOUNT_NO}",  
    "amount": "20",  
    "created_at": "2024-09-10T09:12:36.88272Z",  
    "deadline": "2024-09-11",  
    "fees": [],  
    "id": "d96bdc91-6d1c-49b5-a3c3-03f16c70321b",  
    "interests": [],  
    "remaining_payable": "20",  
    "source_account_no": "{ACCOUNT_NO}",  
    "status": "EXECUTED",  
    "system_date": "2024-09-10",  
    "total_interest": "0"  
}
```

### Step 1.2: [Display Increase in Buying Power](https://docs.alpaca.markets/reference/gettradingaccount#/)

Once the instant funding transfer is moved to a EXECUTED status you can fetch the user’s buying power via the GET trading account endpoint and guide your user to begin trading with their immediate funds.

**Request**
`GET /v1/trading/accounts/fc304c4d-5c2c-41f2-b357-99bbbed9ec90/account`

**Response**

JSON

```
{  
    "id": "{ACCOUNT_ID}",  
    "admin_configurations": {  
        "allow_instant_ach": true,  
        "disable_shorting": true,  
        "max_margin_multiplier": "1"  
    },  
    "user_configurations": null,  
    "account_number": "{ACCOUNT_NO}",  
    "status": "ACTIVE",  
    "crypto_status": "INACTIVE",  
    "currency": "USD",  
    "buying_power": "100",  
    "regt_buying_power": "100",  
    "daytrading_buying_power": "0",  
    "effective_buying_power": "100",  
    "non_marginable_buying_power": "0",  
    "bod_dtbp": "0",  
    "cash": "100",  
    "cash_withdrawable": "0",  
    "cash_transferable": "0",  
    "accrued_fees": "0",  
    "pending_transfer_out": "0",  
    "pending_transfer_in": "0",  
    "portfolio_value": "0",  
    "pattern_day_trader": false,  
    "trading_blocked": false,  
    "transfers_blocked": false,  
    "account_blocked": false,  
    "created_at": "2024-07-10T17:23:51.655324Z",  
    "trade_suspended_by_user": false,  
    "multiplier": "1",  
    "shorting_enabled": false,  
    "equity": "0",  
    "last_equity": "0",  
    "long_market_value": "0",  
    "short_market_value": "0",  
    "position_market_value": "0",  
    "initial_margin": "0",  
    "maintenance_margin": "0",  
    "last_maintenance_margin": "0",  
    "sma": "0",  
    "daytrade_count": 0,  
    "balance_asof": "2024-07-09",  
    "previous_close": "2024-07-09T20:00:00-04:00",  
    "last_long_market_value": "0",  
    "last_short_market_value": "0",  
    "last_cash": "0",  
    "last_initial_margin": "0",  
    "last_regt_buying_power": "0",  
    "last_daytrading_buying_power": "0",  
    "last_buying_power": "0",  
    "last_daytrade_count": 0,  
    "clearing_broker": "ALPACA_APCA",  
    "memoposts": "100",  
    "intraday_adjustments": "0",  
    "pending_reg_taf_fees": "0"  
}
```

### Step 2: Manage Limits (optional)

The total amount of buying power you can extend to all of your end users combined will be limited. This limit will be determined based on your business needs in production. In sandbox, this will be $100,000 USD by default but can be updated as needed. The amount you can credit to each end user will also be limited to $1,000 USD by default. If you anticipate needing a higher limit per account this can also be updated on request.

As you create instant funding transfers for multiple users throughout the day, you will want to keep an eye on how much of your total instant funding limit you’ve used up or how much buying power you are still able to extend to a specific account. Both of these limits can be monitored via API as shown below.

### Step 2.1: [View Instant Funding Limits at correspondent level](https://docs.alpaca.markets/reference/get-v1-instant-funding-correspondent-limits)

View the instant funding limit available for you to use across all your end users.

**Request**
`GET v1/instant_funding/limits`

**Response**

JSON

```
{  
    "amount_available": "99900",  
    "amount_in_use": "100",  
    "amount_limit": "100000"  
}
```

### Step 2.2: [View Account Level Instant Funding Limits](https://docs.alpaca.markets/reference/get-v1-instant-funding-account-limits)

View the instant funding limit available for a specific account or multiple accounts at once.
**Request**
`GET v1/instant_funding/limits/accounts?account_numbers={ACCOUNT_NO}`

**Response**

JSON

```
[  
    {  
        "account_no": "{ACCOUNT_NO}",  
        "amount_available": "900",  
        "amount_in_use": "100",  
        "amount_limit": "1000"  
    }  
]
```

## How to Settle an Instant Funding Transfer

All instant funding transfers are expected to be settled on T+1 by 1 pm ET, meaning that you will have one business day to convert the instant funding credit from an extension of buying power to actual settled cash. Alpaca makes this easy and convenient by providing two reports that you can rely on to determine exactly how much is owed for settlement and by when.

Once the funds have been sent to Alpaca you will have to explicitly trigger settlement via API.

When a settlement is triggered, Alpaca will perform balance checks to determine if the amount sent is sufficient to complete settlement or if there is an insufficient balance then settlement will not be executed.

![This flow is illustrated in the diagram above](https://files.readme.io/2db0b0227bd444b0f5cb14a562324c756557eab150e7c21f5deda467868cdaeb-instandfunding2.png)

This flow is illustrated in the diagram above

> 📘
>
> *Alpaca has a limit of 50.000 transfers per settlement.*
>
> *If more than 50.000 transfers need to be settled, they should be batched in multiple settlements.*

### Step 1:

[Fetch a Settlement Report](https://docs.alpaca.markets/reference/get-v1-instant-funding-reports)

Alpaca provides a high level summary report which shows the total amount due for settlement and a detailed report that is broken down to show each of the associated instant funding transfers that are due. These reports are meant to help you quickly understand how much you are expected to send to settle all instant funding transfers created on T+0 or to look back historically and know how much was owed for any given day.

Two kinds of reports can be obtained using this API:
Summary report - This presents an aggregated view of the balance owed to Alpaca
Detail report - This returns both the aggregate and amount at a per instant transfer level owed to Alpaca.

**Getting the summary settlement report :**

**Request**
`GET v1/instant_funding/reports?report_type=summary&system_date=2024-05-15`

**Response**

JSON

```
[  
    {  
        "account_no": "{ACCOUNT_NO}",  
        "deadline": "2024-05-16",  
        "system_date": "2024-05-15",  
        "total_amount_owed": "900",  
        "total_interest_penalty": "0.7"  
    }  
]
```

**Getting the detail settlement report :**

**Request**
`GET /v1/instant_funding/reports?report_type=detail&system_date=2024-09-09`

**Response**

JSON

```
[  
    {  
        "account_no": "{ACCOUNT_NO}",  
        "deadline": "2024-09-10",  
        "instant_funding_transfers": [  
            {  
                "account_no": "{ACCOUNT_NO}",  
                "amount": "10",  
                "created_at": "2024-09-09T13:20:13.175309Z",  
                "deadline": "2024-09-10",  
                "fees": [],  
                "id": "fade4447-b6ca-4ddf-b87b-3a475861cfeb",  
                "interests": [],  
                "remaining_payable": "10",  
                "source_account_no": "{ACCOUNT_NO}",  
                "status": "EXECUTED",  
                "system_date": "2024-09-09",  
                "total_interest": "0"  
            },  
            {  
                "account_no": "{ACCOUNT_NO}",  
                "amount": "20",  
                "created_at": "2024-09-09T13:21:48.050636Z",  
                "deadline": "2024-09-10",  
                "fees": [],  
                "id": "f1544394-a6f2-42a8-8758-408e8e0d5099",  
                "interests": [],  
                "remaining_payable": "20",  
                "source_account_no": "{ACCOUNT_NO}",  
                "status": "EXECUTED",  
                "system_date": "2024-09-09",  
                "total_interest": "0"  
            }  
        ],  
        "system_date": "2024-09-09",  
        "total_amount_owed": "30",  
        "total_interest_penalty": "0.11"  
    }  
]
```

### Step 2: Submit Payment to Alpaca

Once you are confident that you know exactly how much is owed for settlement, you can initiate a wire payment from your external bank account to Alpaca to be credited to your firm account denoted with the SI suffix. You can monitor the [non trade events stream](https://docs.alpaca.markets/reference/get-v1-events-nta) to know exactly when the funds are credited to your account.

### Step 3: [Trigger Settlement](https://docs.alpaca.markets/reference/post-v1-instant-funding-settlements)

You will trigger settlement via API and submit the list of instant funding transfers that you wish to settle with the funds credited to your SI firm account. At this stage, you will also include the travel rule details which Alpaca is required to collect. For more information on the travel rule requirements please refer to the FinCEN Advisory as needed.

Please note that only one settlement can be in progress at a time i.e. in pending or awaiting\_additional\_funds status at a time.

Details of fields required to be sent as part of the transmitter information -

| field | description |
| --- | --- |
| originator\_full\_name | Full name of the customer |
| originator\_street\_address | Street address of the entity transmitting funds |
| originator\_city | City of the entity transmitting funds |
| originator\_postal\_code | Postal code of the entity transmitting funds |
| originator\_country | Country of the entity transmitting funds |
| originator\_bank\_account\_number | Customer’s account number on the platform |
| originator\_bank\_name | Legal entity that is transmitting the funds |

**Request**
`POST v1/instant_funding/settlements`

JSON

```
{  
  "transfers": [  
    {  
      "instant_transfer_id": "29d8afd1-b7b1-4b47-830d-263244c4d28b",  
      "transmitter_info": {  
        "originator_full_name": "John Doe",  
        "originator_street_address": "123 Alpaca Way",  
        "originator_city": "San Mateo",  
        "originator_postal_code": "12345",  
        "originator_country": "USA",  
        "originator_bank_account_number": "123456789",  
        "originator_bank_name": "Citibank"  
      }  
    }  
  ],  
  "additional_info": "bulk wire sent to account {ACCOUNT_NO} from Citibank account number 191919191"  
}
```

**Response**

JSON

```
{  
    "created_at": "2024-05-24T08:56:01.440771581-04:00",  
    "id": "53d63f11-e844-4867-ab72-364bb1ac9258",  
    "interest_amount": "0",  
    "source_account_number": "{ACCOUNT_NO}",  
    "status": "PENDING",  
    "total_amount": "100",  
    "updated_at": "2024-05-24T08:56:01.440771581-04:00"  
}
```

  

### Step 4: [Check settlement status](https://docs.alpaca.markets/reference/get-v1-instant-funding-settlements-single)

After triggering the settlement, it’s important to check the status of the settlement to make sure that the reconciliation has been completed.

**Request**
`GET /v1/instant_funding/settlements/c9a89b1b-94fe-4852-8ba1-140b67aa7280`

**Response**

JSON

```
{  
    "completed_at": "2024-10-29T14:50:46.337084Z",  
    "created_at": "2024-10-29T14:50:15.926307Z",  
    "id": "a0f41a2c-60f3-49f2-90cd-e4ec2560c819",  
    "interest_amount": "0",  
    "source_account_number": "{ACCOUNT_NO}",  
    "status": "COMPLETED",  
    "total_amount": "20",  
    "updated_at": "2024-10-29T14:50:46.337131Z"  
}
```

### Step 4.1: Successful reconciliation

When a settlement is successful, the instant funding credit is canceled and the respective amount is debited from the SI account. In account activities, this is represented as a canceled MEM activity followed by an executed CSD activity for an amount equivalent to the instant funding transfer amount that was settled.

Given below is a sample response for a successful reconciliation.

**Response**

JSON

```
{  
    "completed_at": "2024-08-26T15:10:03.337899Z",  
    "created_at": "2024-08-26T15:09:18.077505Z",  
    "id": "133cef1d-0300-41cc-9ac4-9c75cd1518b1",  
    "interest_amount": "0",  
    "source_account_number": "{ACCOUNT_NO}",  
    "status": "COMPLETED",  
    "total_amount": "20",  
    "updated_at": "2024-08-26T15:10:03.337921Z"  
}
```

### Step 4.2: Handling failed reconciliation

If the settlement fails with the reason "reason": "insufficient balance, available: 0, required: 40", it implies that when the settlement was triggered, the source account did not have enough funds required for the reconciliation. In that case, additional funds can be added to the SI account by journaling money from RF to SI account or sending more funds to the SI account. Once the funds have been loaded, the settlement can be triggered again.

Here’s a sample response for a failed settlement -

**Response**

JSON

```
{  
    "created_at": "2024-08-27T08:30:24.517942Z",  
    "id": "c9a89b1b-94fe-4852-8ba1-140b67aa7280",  
    "interest_amount": "0",  
    "reason": "insufficient balance, available: 0, required: 40",  
    "source_account_number": "{ACCOUNT_NO}",  
    "status": "FAILED",  
    "total_amount": "40",  
    "updated_at": "2024-08-27T09:36:01.026356Z"  
}
```

### Step 4.3: [Late instant funding transfers and Accounts in debit balances](https://docs.alpaca.markets/reference/gettradingaccount-1a)

If an instant funding transfer is late i.e if it is not reconciled by 1 PM on T+1 and henceforth canceled by 8pm T+1, then one of the following scenarios would take place -

1. Account has sufficient funds - The cash balance in the customer account would be used to offset the outstanding amount of the instant funding transfer
2. Account has insufficient funds - Customer account would then fall into a debit balance and margin interest will be charged on this until the balance is no longer negative or Alpaca actions on the account to settle the negative balance.

When an account is in debit balance, the cash value for that account will be negative. The debit balance can be settled by the partners by journaling funds from the RF account to the customer’s account directly. The partner can also collect the needed funds locally from their customer before initiating this journal.

The debit balance of an account can be monitored as follows:

**Request**
`GET v1/trading/accounts/:account_id/account`

**Response**

JSON

```
{  
    "id": "{ACCOUNT_ID}",  
    "admin_configurations": {  
        "allow_instant_ach": true,  
        "disable_shorting": true,  
        "max_margin_multiplier": "1"  
    },  
    "user_configurations": null,  
    "account_number": "574631172",  
    "status": "ACTIVE",  
    "crypto_status": "ACTIVE",  
    "currency": "USD",  
    "buying_power": "0",  
    "regt_buying_power": "0",  
    "daytrading_buying_power": "0",  
    "effective_buying_power": "0",  
    "non_marginable_buying_power": "0",  
    "bod_dtbp": "0",  
    "cash": "-15.26",  
    "cash_withdrawable": "0",  
    "cash_transferable": "0",  
    "accrued_fees": "0.113961944444418396",  
    "pending_transfer_out": "0",  
    "portfolio_value": "-2.31",  
    "pattern_day_trader": false,  
    "trading_blocked": false,  
    "transfers_blocked": false,  
    "account_blocked": false,  
    "created_at": "2024-08-05T14:19:45.334013Z",  
    "trade_suspended_by_user": false,  
    "multiplier": "1",  
    "shorting_enabled": false,  
    "equity": "-2.31",  
    "last_equity": "-1.54",  
    "long_market_value": "62.95",  
    "short_market_value": "0",  
    "position_market_value": "62.95",  
    "initial_margin": "62.95",  
    "maintenance_margin": "18.88",  
    "last_maintenance_margin": "63.61",  
    "sma": "0",  
    "daytrade_count": 0,  
    "balance_asof": "2024-09-09",  
    "previous_close": "2024-09-09T20:00:00-04:00",  
    "last_long_market_value": "63.61",  
    "last_short_market_value": "0",  
    "last_cash": "-65.15",  
    "last_initial_margin": "63.61",  
    "last_regt_buying_power": "0",  
    "last_daytrading_buying_power": "0",  
    "last_buying_power": "0",  
    "last_daytrade_count": 0,  
    "clearing_broker": "ALPACA_APCA",  
    "memoposts": "50",  
    "intraday_adjustments": "0",  
    "pending_reg_taf_fees": "0"  
}
```

## [How to Delete an Instant Funding Transfer](https://docs.alpaca.markets/reference/delete-v1-instant-funding-single)

In case an existing instant funding transfer needs to be reversed, the below request can be made to delete the transfer

**Request**
`DELETE v1/instant_funding/{instant_funding_id}`

**Response**

JSON

```
HTTP 200 OK
```

## Other Resources

[Instant Funding Blog Post](https://alpaca.markets/learn/getting-started-with-instant-funding-for-broker-api/)

## Frequently Asked Questions

See our FAQs available [here](https://docs.alpaca.markets/docs/instant-funding-1) & [here](https://alpaca.markets/support/instant-funding-faq-who-is-it-for-broker-api-prospects-or-existing-partners-servicing-international-clients-interested-in-learning-more-about-instant-funding-for-broker-api-what-is-the?ref=alpaca.markets).

The content article is for general information only and is believed to be accurate as of posting date but may be subject to change. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.
All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not assure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.
Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member FINRA/SIPC, a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.
This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities are not registered or licensed, as applicable.

Updated 20 days ago

---

Ask AI

---

# Trading (https://docs.alpaca.markets/docs/brokerapi-trading)

# Trading

All the functionality from Alpaca Trading API for direct users is supported under Broker API. Please read the documentation for more details. There are additional capabilities for Trading API in the broker setup.

# Fractional Shares

Under the correspondent authentication, Trading API is extended for fractional shares trading.

## Asset API

Asset entity has an extra field named fractionable with type boolean, it is set to true if the asset is marked for fractional trading. Check out more about our Assets API [here](/reference/getassets).

## Order API

The `POST` method (to submit order) has an extra parameter called `notional` to denote the dollar amount to buy. This parameter is mutually exclusive to the qty parameter. You can also specify the `qty` parameter with fractional quantity. Note that the fractional shares trading is currently supported only for day orders and any other type of orders will result in API error.

The order entity includes the `notional` value if the order was submitted with the notional value. In this case, the order entity omits the `qty` field.

Check out more about our Order API [here](https://docs.alpaca.markets/reference/createorderforaccount).

### Sample Order Object

JSON

```
 {
    "id": "39c489ad-fcb1-42b3-9f62-e14c11c62157",
    "client_order_id": "a49c3e74-3f74-468e-a31a-f7a15de17128",
    "created_at": "2024-05-20T09:56:41.449735Z",
    "updated_at": "2024-05-20T13:30:00.876162Z",
    "submitted_at": "2024-05-20T13:23:01.24795Z",
    "filled_at": "2024-05-20T13:30:00.865454Z",
    "expired_at": null,
    "canceled_at": null,
    "failed_at": null,
    "replaced_at": null,
    "replaced_by": null,
    "replaces": null,
    "asset_id": "7595a8d2-68a6-46d7-910c-6b1958491f5c",
    "symbol": "A",
    "asset_class": "us_equity",
    "notional": null,
    "qty": "0.1",
    "filled_qty": "0.1",
    "filled_avg_price": "154.03",
    "order_class": "",
    "order_type": "market",
    "type": "market",
    "side": "sell",
    "time_in_force": "day",
    "limit_price": null,
    "stop_price": null,
    "status": "filled",
    "extended_hours": false,
    "legs": null,
    "trail_percent": null,
    "trail_price": null,
    "hwm": null,
    "commission": "0",
    "subtag": null,
    "source": "correspondent"
},
```

### Order Properties

| Attribute | Type | Description |
| --- | --- | --- |
| id | string/UUID | Order ID generated by Alpaca |
| client\_order\_id | string/UUID | Client unique order ID |
| created\_at | string/timestamp | Time when order was entered |
| updated\_at | string/timestamp | Time of most recent change to the order |
| submitted\_at | string/timestamp | Time the order was submitted for execution or, if not yet submitted the `created_at` time. Because orders are submitted for execution asynchronous to database updates, at times this may be before the `created_at` time. |
| filled\_at | string/timestamp | Time the order was filled. Can be null if not filled |
| expired\_at | string/timestamp | Can be null |
| cancelled\_at | string/timestamp | Can be null |
| failed\_at | string/timestamp | Can be null |
| replaced\_at | string/timestamp | Can be null |
| replaced\_by | string/UUID | The order ID that this order was replaced by. (Can be null) |
| replaces | string/UUID | The order ID that this order replaces. (Can be null) |
| asset\_id | string/UUID | The asset ID |
| symbol | string | The asset symbol |
| asset\_class | string | The asset class |
| notional | string/number | Ordered notional amount. If entered, qty will be null. Can take up to 2 decimal points. |
| qty | string/number | Ordered quantity. If entered, notional will be null. Can take up to 9 decimal points. |
| filled\_qty | string/number | Filled quantity. |
| filled\_avg\_price | string/number | Filled average price. Can be 0 until order is processed in case order is passed outside of market hours. |
| order\_class | string | Valid values: `simple`, `bracket`, `oco` or `oto`. |
| order\_type | string/number | (Will be deprecated in favor of type field below) Valid values: market, limit, stop, stop\_limit, trailing\_stop |
| type | string | Valid values: `market`,`limit`, `stop`, `stop_limit`, `trailing_stop`. |
| side | string | Valid values: `buy` and `sell`. |
| time\_in\_force | string | Please see the relevant section in [Time in Force](https://docs.alpaca.markets/docs/orders-at-alpaca#time-in-force) for more info on what values are possible for what kind of orders. |
| limit\_price | string/number | Limit price. |
| stop\_price | string/number | Stop price. |
| status | string | Order status. See Order statuses [here](https://docs.alpaca.markets/docs/orders-at-alpaca#order-lifecycle). |
| extended\_hours | boolean | If `true`, eligible for execution outside regular trading hours. |
| legs | array | When querying non-simple order\_class orders in a nested style, an array of Order entities associated with this order. Otherwise, null. |
| trail\_percent | string/number | The percent value away from the high water mark for trailing stop orders. |
| trail\_price | string/number | The dollar value away from the high water mark for trailing stop orders. |
| hwm | string/number | The highest (lowest) market price seen since the trailing stop order was submitted. |
| commission | string/number | The commission you want to charge the end user. |
| commission\_type | string | Select how to interpret the value provided in the commission field.  Available options: notional(default), qty, bps. |
| subtag | string/number | An account identifier for Omnibus partners. (Can be null) |
| source | string | Source of order. |

## Account Configuration API

Account configuration API adds another configuration key called `fractional_trading` and defaults to `true`. If you want to disable fractional trading for a specific account for any reason, you can set this to `false`.

# Commissions

You have the option to charge the commission for each order. You will need to contact Alpaca first to set up the commission structure, but once it’s set up, you can submit customer orders with a `commission` parameter indicating the dollar amount to charge. The respective field is attached in the order entity in the API response.

To charge commissions, first select desired method with `commission_type`. Then specify the desired dollar amount or percentage in `commission` field. Please note: On orders to sell if the commission input will be more than the principal of the transaction then the principal amount of the transaction (net of SEC REG and FINRA TAF fees) will be charged as commission and not the amount specified in the order. On all orders (regardless of commission type), the commission charged will be prorated on each execution if the order has multiple executions. For instance, if 10% of the order is filled on one execution then the commission on that execution will be 10% of the total commission.

* notional:  
  Charge commission on a per order basis. When the `commission_type` field is omitted from the order request, this is used as the default.
* qty:  
  Charge commission on a per qty/contract basis, pro rated.
* bps:  
  The percent commission you want to charge the end user on the order (expressed in bps). Alpaca will convert the order to a notional amount for purposes of calculating commission.

# Order Sub-tagging (Omnibus)

If you are an omnibus setup, we ask you to submit a “sub-tag” value in each order. This is for us to understand the order flow better from the trade surveillance requirements. In case you fail to attach proper sub-tags, we may need to reject all of the order flows coming from you as we may not be able to segregate particular malicious activities.

# FAQ

**What should I do if I receive a timeout message from Alpaca when submitting an order?**

The order may have been sent to the market for execution. You should not attempt to resend the order or mark the timed-out order as canceled until confirmed by Alpaca Support or the trading team. Before taking any action on the timed-out order you should check the broker dashboard and contact Alpaca support.  
Please contact our Support Team at [[email protected]](/cdn-cgi/l/email-protection#b7c4c2c7c7d8c5c3f7d6dbc7d6d4d699dad6c5dcd2c3c4) to verify if the order was successfully submitted and routed to the market.

Updated 5 months ago

---

Ask AI

---

# Portfolio Rebalancing (https://docs.alpaca.markets/docs/portfolio-rebalancing)

# Portfolio Rebalancing

[Rebalancing API](/reference/get-v1-rebalancing-portfolios) offers investment advisors a way to easily create investment portfolios that are automatically updated to the specified cash, stock symbol percentage weights, rebalance conditions, and triggers selected. Please see below for some definitions before we jump into an overview of the rebalancing flow:

* Portfolios: An allocation containing securities and/or cash with specific weights and conditions to be met
* Subscriptions: Accounts can be subscribed to a created portfolio and follow rebalancing events to ensure the account is kept in sync with the target portfolio
* Runs: A run is a set of orders that will be sent for execution to achieve a goal (liquidating a specified amount to set it aside for withdrawal or doing a full rebalance to the target allocation)

> 📘
>
> ### Rebalancing API Resource
>
> * [Postman Collection](https://www.postman.com/alpacamarkets/workspace/alpaca-public-workspace/folder/19455863-8fea51d0-40bf-4680-9da2-b0de1a7c8b18?ctx=documentation)
> * [How to Get Started with Rebalancing API](https://alpaca.markets/learn/how-to-get-started-with-rebalancing-api/)
> * [Rebalancing API Reference](/reference/get-v1-rebalancing-portfolios)

# Types of Rebalancing

Rebalancing API offers two types of rebalancing conditions:

* **Drift Band**: When a portfolio breaches a certain threshold, irrespective of the time period elapsed, the portfolio is adjusted. For instance, if we put a +/- 10% band on a portfolio, we would automatically adjust the entire portfolio when we reach the threshold for one of the holdings.
* **Calendar**: At the desired period, the state of the portfolio is analyzed and the portfolio is rebalanced to the default portfolio. For example, on April 1st our 50:50 AAPL TLT portfolio is not 55:45, so we would need to liquidate TLT and buy more AAPL to return to the desired state of exposure of 50:50.

# Create a Portfolio

To create a portfolio, use the [Create Portfolio](/reference/post-v1-rebalancing-portfolios) `POST` endpoint.

See below see example payload to create a portfolio with a mix of cash and securities:

JSON

```
{
    "name": "Balanced",
    "description": "A balanced portfolio of stocks and bonds",
    "weights": [
        {
            "type": "cash",
            "percent": "5"
        },
        {
            "type": "asset",
            "symbol": "SPY",
            "percent": "60"
        },
        {
            "type": "asset",
            "symbol": "TLT",
            "percent": "35"
        }
    ],
    "cooldown_days": 7,
    "rebalance_conditions": [
        {
            "type": "drift_band",
            "sub_type": "absolute",
            "percent": "5"
        },
        {
            "type": "drift_band",
            "sub_type": "relative",
            "percent": "20"
        }
    ]
}
```

Once executed, you can find the portfolio ID in the response payload similar to the one below. In this case, our newly created portfolio ID is 2d49d00e-ab1c-4014-89d8-70c5f64df2fc. This will be needed to subscribe an account to follow this new portfolio:

JSON

```
{
    "id": "2d49d00e-ab1c-4014-89d8-70c5f64df2fc",
    "name": "Balanced Two",
    "description": "A balanced portfolio of stocks and bonds",
    "status": "active",
    "cooldown_days": 7,
    "created_at": "2022-08-07T14:56:45.116867815-04:00",
    "updated_at": "2022-08-07T14:56:45.196857944-04:00",
    "weights": [
        {
            "type": "cash",
            "symbol": null,
            "percent": "5"
        },
        {
            "type": "asset",
            "symbol": "SPY",
            "percent": "60"
        },
        {
            "type": "asset",
            "symbol": "TLT",
            "percent": "35"
        }
    ],
    "rebalance_conditions": [
        {
            "type": "drift_band",
            "sub_type": "absolute",
            "percent": "5",
            "day": null
        },
        {
            "type": "drift_band",
            "sub_type": "relative",
            "percent": "20",
            "day": null
        }
    ]
}
```

You can also list all of your created portfolios with the List All Portfolios endpoint.

# Subscribe Account to a Portfolio

Once you have created a portfolio, the next step is to subscribe a given account to follow a portfolio. This will ensure that the account is subscribed to have the necessary orders executed when rebalancing conditions are met.

To subscribe an account to the newly created portfolio and its rebalancing conditions, you will need to create a new subscription. For example, to subscribe account ID bf2b0f93-f296-4276-a9cf-288586cf4fb7 to the newly created portfolio, use the Create Subscriptions endpoint with the following JSON payload:

JSON

```
{
    "account_id": "bf2b0f93-f296-4276-a9cf-288586cf4fb7",
    "portfolio_id": "57d4ec79-9658-4916-9eb1-7c672be97e3e"
}
```

# Check Rebalancing Events

Once an account is subscribed to a portfolio, we need to wait for the first rebalancing event to happen. We can check completed rebalancing events for all accounts by using the [List All Runs endpoint](/reference/get-v1-rebalancing-runs).

cURL

```
curl --location --request GET '{{HOST}}/v1/beta/rebalancing/runs?status=COMPLETED_SUCCESS' \
--header 'Authorization: Basic <TOKEN>' \
--data-raw ''
```

See example payload of a successful run:

JSON

```
{
    "runs": [
        {
            "id": "36699e7f-56a0-4b87-8e03-968363f4b6df",
            "type": "full_rebalance",
            "amount": null,
            "initiated_from": "system",
            "status": "COMPLETED_SUCCESS",
            "reason": null,
            "account_id": "b3130eeb-1219-46f3-8bfb-7715f00d736b",
            "portfolio_id": "4ad7d634-a60d-4e6e-955f-3c68ee24d285",
            "weights": [
                {
                    "type": "cash",
                    "symbol": null,
                    "percent": "5"
                },
                {
                    "type": "asset",
                    "symbol": "SPY",
                    "percent": "60"
                },
                {
                    "type": "asset",
                    "symbol": "TLT",
                    "percent": "35"
                }
            ],
            "orders": [
                {
                    "id": "c29dd94b-eaaf-4681-9d1f-4fd47571804b",
                    "client_order_id": "cb2d1ff5-8355-4c92-84d7-dfff43f44cb2",
                    "created_at": "2022-03-08T16:51:07.442125Z",
                    "updated_at": "2022-03-08T16:51:07.525039Z",
                    "submitted_at": "2022-03-08T16:51:07.438495Z",
                    "filled_at": "2022-03-08T16:51:07.520169Z",
                    "expired_at": null,
                    "canceled_at": null,
                    "failed_at": null,
                    "replaced_at": null,
                    "replaced_by": null,
                    "replaces": null,
                    "asset_id": "3b64361a-1960-421a-9464-a484544193df",
                    "symbol": "SPY",
                    "asset_class": "us_equity",
                    "notional": "30443.177578017",
                    "qty": null,
                    "filled_qty": "72.865432211",
                    "filled_avg_price": "417.8",
                    "order_class": "",
                    "order_type": "market",
                    "type": "market",
                    "side": "buy",
                    "time_in_force": "day",
                    "limit_price": null,
                    "stop_price": null,
                    "status": "filled",
                    "extended_hours": false,
                    "legs": null,
                    "trail_percent": null,
                    "trail_price": null,
                    "hwm": null,
                    "subtag": null,
                    "source": null
                },
                {
                    "id": "ab772dcb-b67c-4173-a5b5-e31b9ad236b5",
                    "client_order_id": "d6278f6c-3010-45ce-aaee-6e64136deec0",
                    "created_at": "2022-03-08T16:51:07.883352Z",
                    "updated_at": "2022-03-08T16:51:07.934602Z",
                    "submitted_at": "2022-03-08T16:51:07.877726Z",
                    "filled_at": "2022-03-08T16:51:07.928907Z",
                    "expired_at": null,
                    "canceled_at": null,
                    "failed_at": null,
                    "replaced_at": null,
                    "replaced_by": null,
                    "replaces": null,
                    "asset_id": "a106d0ef-e6f2-4736-8750-5dee1cadf75b",
                    "symbol": "TLT",
                    "asset_class": "us_equity",
                    "notional": "17121.076868834",
                    "qty": null,
                    "filled_qty": "124.408348124",
                    "filled_avg_price": "137.62",
                    "order_class": "",
                    "order_type": "market",
                    "type": "market",
                    "side": "buy",
                    "time_in_force": "day",
                    "limit_price": null,
                    "stop_price": null,
                    "status": "filled",
                    "extended_hours": false,
                    "legs": null,
                    "trail_percent": null,
                    "trail_price": null,
                    "hwm": null,
                    "subtag": null,
                    "source": null
                }
            ],
            "completed_at": null,
            "canceled_at": null,
            "created_at": "2022-03-08T16:36:07.053482Z",
            "updated_at": "2022-03-08T16:51:08.53806Z"
        },
        ...
    ],
    "next_page_token": 100
}
```

> 📘
>
> ### Note
>
> Cash inflows to the account (deposits, cash journals, etc.) will trigger buy trades to reduce drift.

# Manually Trigger Rebalancing Event (Run)

Rebalancing API will automatically configure systems to watch for portfolio rebalancing conditions and execute necessary orders. To execute a rebalancing run manually, please see [Create Run endpoint](/reference/post-v1-rebalancing-runs).

> 🚧
>
> ### Manually executing a run is currently only allowed for accounts without an active subscription.

# Portfolio Rebalance Evaluation

Portfolios are evaluated for potential rebalancing based on specific conditions, which are checked in a defined order.

**Prerequisites:**

* **Status:**

  + Only portfolios with an `active` status are considered for evaluation.
  + If an asset within a portfolio is found to be inactive, non-fractionable, or untradable during a rebalance, the portfolio's status automatically transitions to `needs_adjustment`.
* **Change required:** Portfolios in `needs_adjustment` are excluded from evaluation. To re-enable evaluation for such portfolios, you must first update their status back to `active` using a `PATCH` request.
* **Weights:**

  + portfolio weights are required to have a `percent` greater than zero.
  + If a weight of type cash has its percent set to zero, it will be automatically removed from the portfolio configuration.

**Evaluation Order and Conditions:**

The system checks for the following conditions sequentially. The first condition met may trigger a rebalance (or place the portfolio in a state requiring rebalance):

1. **`in_cooldown`**: Checks if the portfolio is currently within a defined cooldown period following a previous rebalance. If true, evaluation may stop here for this cycle.
2. **`calendar`**: Checks for scheduled rebalancing based on predefined intervals:
   * Annually
   * Quarterly
   * Monthly
   * Weekly
3. **`drift_band`**: Checks if portfolio asset allocations have deviated beyond configured thresholds:
   * `absolute`: Deviation measured in absolute percentage points (e.g., if target is 10%, drift triggers if allocation goes below 8% or above 12% for a 2% absolute threshold).
   * `relative`: Deviation measured relative to the target allocation percentage (e.g., if target is 10%, drift triggers if allocation goes below 9% or above 11% for a 10% relative threshold).

**Important Considerations:**

* **Minimum Order Size:** Be aware that a minimum order value (often around $1 per asset) typically applies during rebalancing trades. This means sufficient cash balance is required to execute orders across potentially many assets. An estimated minimum cash need could be `(Number of Assets in Portfolio) * $1`. Plan account funding accordingly, especially for portfolios with many assets.

**Daily Processing Runs**

Portfolios are evaluated daily for one of two mutually exclusive processing runs: `full_rebalance` or `invest_cash`. Only one type of run can execute per portfolio per day. The system checks eligibility in the following order:

1. `full_rebalance`: To realign the portfolio's current holdings to match its target weights as closely as possible, it will execute both buy and sell orders. (Note: This run typically triggers based on portfolio drift or other rebalancing criteria). Please note that there may be a cash buffer that is overlaid on the target weights to cover necessary fees and reserves for market volatility.
2. `invest_cash`: If a `full_rebalance` is not executed, the system then checks if an `invest_cash` run can be performed. This requires the portfolio's account to have an available cash balance exceeding $10 USD. If triggered, `invest_cash` only executes buy orders, utilizing the available cash to shift the portfolio's allocation closer to its target weights. This can occur a maximum of once per day.

# FAQ

**Q: What is the minimum cash required for a rebalancing run?**

For a rebalancing run to occur, there must be a minimum of $1 per asset in the portfolio.

Example 1 - A portfolio that is 50% AAPL, 25% TSLA, 25% GOOGL  
If all other rebalancing conditions and cooldown days are met, a rebalancing run would only occur with at least $1 per asset in the portfolio deposited. Anything less would not trigger a rebalance.

Example 2 - A portfolio that is 50% AAPL, 25% TSLA, 25% CASH  
If all other rebalancing conditions and cooldown days are met, a rebalancing run would only occur with at least $1 per asset in the portfolio deposited. Anything less would not trigger a rebalance.

For an invest\_cash run to occur, a minimum of $10 must be deposited. For invest\_cash runs, it is possible to change the $10 USD threshold and to disable this processing run type; please reach out to a member of the Alpaca team to do this.

**Q: Can rebalancing run partially for some assets where minimum notional is satisfied but not run for the assets where minimum notional is not satisfied?**

Yes. If a portfolio has 11 assets, but only $10 is deposited, there may be a partial rebalancing where trades are only executed for 10 assets.

**Q: When does a Rebalancing Job or invest\_cash job run at Alpaca?**

When cash is first invested into a portfolio (and the minimum cash requirement is met), a rebalancing job of type full\_rebalance will occur.

Thereafter, if a minimum of $10 (or other invest\_cash threshold) is invested, an invest\_cash job will run regardless of the portfolio rebalancing conditions and the cooldown period.

After the cooldown period, and if the rebalancing conditions are met, then a rebalancing job will run.

Both the rebalance and invest\_cash jobs run between 9:30 AM and 3:30 PM ET.

**Q: What are the steps for Cash Withdrawal if a user wants to close the positions and withdraw their cash?**

The steps are as follows:

1. Unsubscribe the user using the [https://broker-api.sandbox.alpaca.markets/v1/rebalancing/subscriptions/{subscription\_id}](https://broker-api.sandbox.alpaca.markets/v1/rebalancing/subscriptions/%7Bsubscription_id%7D) DELETE request.
2. Execute a manual run with revised portfolio weights using the <https://broker-api.sandbox.alpaca.markets/v1/rebalancing/runs> POST request.
3. Wait for the desired amount to be available as withdrawable cash, and then make a GET request to [https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account\_id}/account](https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/%7Baccount_id%7D/account) and check if cash\_withdrawable has the desired amount.

\*Note: The amount credited from the trade will be available for withdrawal on the next trading day (T+1).

4. Journal the money from user account to firm account using the <https://broker-api.sandbox.alpaca.markets/v1/journals> POST request.
5. Subscribe the user back to their portfolio using the <https://broker-api.sandbox.alpaca.markets/v1/rebalancing/subscriptions> POST request.

**Q: Under what conditions might the rebalancer stop rebalancing my portfolio?**

The rebalancer may cease operations if your account encounters certain restrictions that block trading activities. These include:

* **Pattern Day Trading (PDT) Flag:** If your account is marked as a Pattern Day Trader, trading will be restricted. For more details, refer to our PDT rule explanation.
* **ACH Return**: When an ACH deposit is returned by your bank, your account is automatically restricted and will lead to trading blocks on your account.
* **Position to Equity Ratio Exceeded:** This is calculated as (position\_market\_value / equity). If this ratio exceeds the maximum allowed limit (6:1), the account will be restricted during buying power verification.
* **Crypto Trading Restriction:** Set when account is restricted to liquidation for crypto trading.
* **Options Trading Restriction**: Set when account is restricted to liquidation for options trading.
* **Unspecified Restrictions:** Other unforeseen issues may also result in trading limitations.

To ensure continuous rebalancing run functionality, it is crucial to monitor your account for these conditions and address any issues promptly.

Updated 10 days ago

---

Ask AI

---

# SSE Events (https://docs.alpaca.markets/docs/sse-events)

# SSE Events

Alpaca Broker API provides replayable and real-time event streams via Server-Sent Event (SSE). The SSE protocol is a simple yet powerful protocol to satisfy a lot of your needs to build flawless user experience. Each endpoint can be queried by the event timestamp or monotonically incremental integer ID to seamlessly subscribe from the past point-in-time event to the real-time pushes with a simple HTTP request. While all SSE endpoints follow the same JSON object model as other REST endpoints, SSE protocol is a lightweight addition on top of the basic HTTP protocol which is a bit different from REST protocol. Please make sure your client program handles the SSE protocol correctly.

# Why Use SSE?

* Low Latency: Receive updates in real-time for timely decisions about your customers
* Resource Efficiency: A single connection serves multiple updates and streamlines where you receive updates about your customers
* Simplicity: Integration requires fewer lines of code compared to WebSockets.

## Best Practices

* Connection Health: Implement heartbeat checks.
* Error Recovery: Code for auto-reconnection.
* Selective Listening: Subscribe to specific event types relevant to your use case.

> 🛠️
>
> ### Note about /v1 and /v2beta1
>
> We are in the process of switching from integer IDs to ULIDs for our Events Streaming. ULIDs are designed to be lexicographically sortable, thanks to their structure that encodes a timestamp. This allows you to better sort and filter records based on when they occurred. While they are more complex to read than integer IDs, they contain more information.
>
> Currently only Admin Action Events and Trade Events leverage ULIDs, and over the next months we will be migrating the rest. Check back here to know which SSEs are on the new endpoint.
>
> ### What Should You Do?
>
> Legacy Events that still use an integer ID and have now an additional field called since\_ulid and until\_ulid. We highly recommend that you use those today so that you don't face any issues when we will eventually migrate the remaining events (account status, journal status, transfer status, trade status and non-trade-activity notifications) and deprecate the old ones.

# Types of SSE Events

## Account Status Events

Stay abreast of changes to account statuses. [Learn more here](https://docs.alpaca.markets/reference/suscribetoaccountstatussse).

You can find some sample responses below:

Equity & Crypto AccountEquity Only Account

```
{
    "account_blocked": false,
    "account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
    "account_number": "",
    "admin_configurations": {
        "allow_instant_ach": true,
        "disable_shorting": true
    },
    "at": "2023-10-13T13:34:28.30629Z",
    "crypto_status_from": "",
    "crypto_status_to": "APPROVED",
    "event_id": 12627517,
    "event_ulid": "01HCMKXQYJ3ZBV66Q21KCT1CRR",
    "pattern_day_trader": false,
    "status_from": "",
    "status_to": "APPROVED",
    "trading_blocked": false
}

{
    "account_id": "50333df9-66f0-46b9-a083-4212b152f749",
    "account_number": "307137914",
    "at": "2023-10-13T13:34:29.668043Z",
    "event_id": 12627518,
    "event_ulid": "01HCMKXS94ST351NFGEZR57EHV",
    "status_from": "APPROVED",
    "status_to": "ACTIVE"
}

:heartbeat

{
    "account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
    "account_number": "307645030",
    "at": "2023-10-13T13:35:18.145917Z",
    "crypto_status_from": "APPROVED",
    "crypto_status_to": "ACTIVE",
    "event_id": 12627519,
    "event_ulid": "01HCMKZ8M2XPNC9Y8HE159P2WK",
    "status_from": "APPROVED",
    "status_to": "APPROVED"
}

:heartbeat

{
    "account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
    "account_number": "307645030",
    "at": "2023-10-13T13:40:17.417798Z",
    "event_id": 12627521,
    "event_ulid": "01HCMM8CWAQETWNM75VJKA0YX2",
    "status_from": "APPROVED",
    "status_to": "ACTIVE"
}
```

```
{
    "account_blocked": false,
    "account_id": "d16f0c84-2bcc-4caf-bd68-a97889986d74",
    "account_number": "",
    "admin_configurations": {
        "allow_instant_ach": true,
        "disable_shorting": true
    },
    "at": "2023-10-13T13:18:16.936397Z",
    "crypto_status_from": "",
    "crypto_status_to": "INACTIVE",
    "event_id": 12627496,
    "event_ulid": "01HCMK03B8JV4YDB8W2HZ0K6V2",
    "pattern_day_trader": false,
    "status_from": "",
    "status_to": "APPROVED",
    "trading_blocked": false
}

{
    "account_id": "d16f0c84-2bcc-4caf-bd68-a97889986d74",
    "account_number": "307781498",
    "at": "2023-10-13T13:18:18.472537Z",
    "event_id": 12627497,
    "event_ulid": "01HCMK04V979EMCGB96Z6T0H00",
    "status_from": "APPROVED",
    "status_to": "ACTIVE"
}
```

## Journal Events

Stay notified on the status of journal transactions to make sure they have been executed and the cash has been moved from one account to another. [More details here](https://docs.alpaca.markets/edit/funding-via-journals).

You can find a sample response below:

JSON

```
{
    "at": "2023-10-13T13:11:10.57913Z",
    "entry_type": "JNLC",
    "event_id": 11751531,
    "event_ulid": "01HCMJK2ZKCPTYXMJYS66T0QJJ",
    "journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
    "status_from": "",
    "status_to": "queued"
}

{
    "at": "2023-10-13T13:11:10.634443Z",
    "entry_type": "JNLC",
    "event_id": 11751532,
    "event_ulid": "01HCMJK31AVBME4WNSH3C8E4HJ",
    "journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
    "status_from": "queued",
    "status_to": "sent_to_clearing"
}

{
    "at": "2023-10-13T13:11:10.67241Z",
    "entry_type": "JNLC",
    "event_id": 11751533,
    "event_ulid": "01HCMJK32GSBH2QG92TKZKDRRV",
    "journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
    "status_from": "sent_to_clearing",
    "status_to": "executed"
}
```

## Transfer Events

Be notified instantly when the statuses of deposits and withdrawals are updated. [Read further here](https://docs.alpaca.markets/reference/subscribetotransferstatussse).

You can find a sample response below:

JSON

```
{
  "account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
  "at":"2021-06-10T19:49:12.579109Z",
  "event_id":15960,
  "status_from":"",
  "status_to":"queued",
  "transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}


{
  "account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
  "at":"2021-06-10T19:52:24.066998Z",
  "event_id":15961,
  "status_from":"queued",
  "status_to":"sent_to_clearing",
 	"transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}

{
  "account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
  "at":"2021-06-10T20:02:24.280178Z",
  "event_id":15962,
  "status_from":"sent_to_clearing",
  "status_to":"executed",
  "transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}
```

## Trade Events

Keep tabs on the status of orders, trades, and executions in real-time. [Documentation here](https://docs.alpaca.markets/reference/subscribetotradev2sse).

v2beta1v1

```
{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:28:58.387652Z",
    "event_id": "01HCMKKNRK7S5C1JYP50QGDECQ",
    "event": "new",
    "timestamp": "2023-10-13T13:28:58.37957033Z",
    "order": {
        "id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
        "client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
        "created_at": "2023-10-13T13:28:58.361530031Z",
        "updated_at": "2023-10-13T13:28:58.386058029Z",
        "submitted_at": "2023-10-13T13:28:58.360070731Z",
        "filled_at": null,
        "expired_at": null,
        "cancel_requested_at": null,
        "canceled_at": null,
        "failed_at": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "symbol": "AAPL",
        "asset_class": "us_equity",
        "notional": "10",
        "qty": null,
        "filled_qty": "0",
        "filled_avg_price": null,
        "order_class": "",
        "order_type": "market",
        "type": "market",
        "side": "buy",
        "time_in_force": "day",
        "limit_price": null,
        "stop_price": null,
        "status": "new",
        "extended_hours": false,
        "legs": null,
        "trail_percent": null,
        "trail_price": null,
        "hwm": null,
        "commission": "0"
    },
    "execution_id": "7922ab44-5b33-4049-ab9a-0cfd805ba989"
}

:heartbeat

{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:30:00.664778Z",
    "event_id": "01HCMKNJJRJ4E3RNFA1XR8CX7R",
    "event": "fill",
    "timestamp": "2023-10-13T13:30:00.658443088Z",
    "order": {
        "id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
        "client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
        "created_at": "2023-10-13T13:22:21.887914Z",
        "updated_at": "2023-10-13T13:30:00.661902331Z",
        "submitted_at": "2023-10-13T13:23:05.411141Z",
        "filled_at": "2023-10-13T13:30:00.658443088Z",
        "expired_at": null,
        "cancel_requested_at": null,
        "canceled_at": null,
        "failed_at": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "symbol": "AAPL",
        "asset_class": "us_equity",
        "notional": "10",
        "qty": null,
        "filled_qty": "0.05513895",
        "filled_avg_price": "181.36",
        "order_class": "",
        "order_type": "market",
        "type": "market",
        "side": "buy",
        "time_in_force": "day",
        "limit_price": null,
        "stop_price": null,
        "status": "filled",
        "extended_hours": false,
        "legs": null,
        "trail_percent": null,
        "trail_price": null,
        "hwm": null,
        "commission": "0"
    },
    "price": "181.36",
    "qty": "0.05513895",
    "position_qty": "0.05513895",
    "execution_id": "a958bb42-b034-4d17-bf07-805cf0820ffe"
}

{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:30:00.673857Z",
    "event_id": "01HCMKNJK1Y0R7VF6Q6CAC3SH7",
    "event": "fill",
    "timestamp": "2023-10-13T13:30:00.658388668Z",
    "order": {
        "id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
        "client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
        "created_at": "2023-10-13T13:28:58.361530031Z",
        "updated_at": "2023-10-13T13:30:00.665807961Z",
        "submitted_at": "2023-10-13T13:28:58.360070731Z",
        "filled_at": "2023-10-13T13:30:00.658388668Z",
        "expired_at": null,
        "cancel_requested_at": null,
        "canceled_at": null,
        "failed_at": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "symbol": "AAPL",
        "asset_class": "us_equity",
        "notional": "10",
        "qty": null,
        "filled_qty": "0.05513895",
        "filled_avg_price": "181.36",
        "order_class": "",
        "order_type": "market",
        "type": "market",
        "side": "buy",
        "time_in_force": "day",
        "limit_price": null,
        "stop_price": null,
        "status": "filled",
        "extended_hours": false,
        "legs": null,
        "trail_percent": null,
        "trail_price": null,
        "hwm": null,
        "commission": "0"
    },
    "price": "181.36",
    "qty": "0.05513895",
    "position_qty": "0.1102779",
    "execution_id": "33cbb614-bfc0-468b-b4d0-ccf08588ef77"
}

:heartbeat

{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2024-09-23T13:30:00.673857Z",
    "event_id": "01HCMQR4S73L9G6EHI0JKL2M3N",
    "event": "trade_bust",
    "timestamp": "2024-09-23T15:30:48.601741737Z",
    "order": {
        "id": "c86e4d6c-2cdf-4b81-b658-5728bdc8310b",
        "client_order_id": "10671b99-2cb3-43c3-92a0-96054edd59a8",
        "created_at": "2024-09-23T15:30:48.599363562Z",
        "updated_at": "2024-09-23T16:09:21.642880502Z",
        "submitted_at": "2024-09-23T15:30:48.601741737Z",
        "filled_at": "2024-09-23T20:09:21.635Z",
        "expired_at": null,
        "cancel_requested_at": null,
        "canceled_at": null,
        "failed_at": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "asset_id": "a153fd9c-fd4e-4416-9adc-f9040aa2e125",
        "symbol": "JTAI",
        "asset_class": "us_equity",
        "notional": null,
        "qty": "2",
        "filled_qty": "0",
        "filled_avg_price": "0.107703",
        "order_class": "",
        "order_type": "market",
        "type": "market",
        "side": "buy",
        "time_in_force": "day",
        "limit_price": null,
        "stop_price": null,
        "status": "filled",
        "extended_hours": false,
        "legs": null,
        "trail_percent": null,
        "trail_price": null,
        "hwm": null
    },
    "price": "0.107703",
    "qty": "-2",
    "position_qty": "0",
    "execution_id": "df61d6ec-511f-4cc1-ae61-20456b0cb7a5",
    "previous_execution_id": "aeb60660-412f-4537-8d1f-1101b3fc8f64"
}

{
    
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2024-10-18T13:30:00.673857Z",
    "event_id": "01HCMQR4S73L9G6EHI0JKL2M3N",
    "event": "trade_correct",
    "timestamp": "2024-10-18T22:26:32.988Z",
    "order": {
        "id": "390cd7d0-07fa-4ab0-8b99-7ffb8d7408ff",
        "client_order_id": "21975666-5eae-4149-b86f-3682f4fd8c69",
        "created_at": "2024-10-18T09:10:13.311667892Z",
        "updated_at": "2024-10-18T18:26:32.996327532Z",
        "submitted_at": "2024-10-18T09:10:13.31490803Z",
        "filled_at": "2024-10-18T22:26:32.988Z",
        "expired_at": null,
        "cancel_requested_at": null,
        "canceled_at": null,
        "failed_at": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "asset_id": "6b0137a2-4efb-4fba-aa39-9f64f6afe5f4",
        "symbol": "BSRR",
        "asset_class": "us_equity",
        "notional": null,
        "qty": "1",
        "filled_qty": "1",
        "filled_avg_price": "25",
        "order_class": "",
        "order_type": "limit",
        "type": "limit",
        "side": "buy",
        "time_in_force": "day",
        "limit_price": "28.93",
        "stop_price": null,
        "status": "filled",
        "extended_hours": true,
        "legs": null,
        "trail_percent": null,
        "trail_price": null,
        "hwm": null
    },
    "price": "25",
    "qty": "1",
    "position_qty": "1",
    "execution_id": "2ff98545-9082-469a-8aa8-7f6c09ac258f",
    "previous_execution_id": "f116d6c7-fc4a-49b1-a649-317aace34783"
}
```

```
{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:22:21.927554Z",
    "event": "accepted",
    "event_id": 10676063,
    "event_ulid": "01HCMK7JJ3EJD9P4JSM1M0HTZ0",
    "order": {
        "asset_class": "us_equity",
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "cancel_requested_at": null,
        "canceled_at": null,
        "client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
        "commission": "0",
        "created_at": "2023-10-13T09:22:21.887913787-04:00",
        "expired_at": null,
        "extended_hours": false,
        "failed_at": null,
        "filled_at": null,
        "filled_avg_price": null,
        "filled_qty": "0",
        "hwm": null,
        "id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
        "legs": null,
        "limit_price": null,
        "notional": "10",
        "order_class": "",
        "order_type": "market",
        "qty": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "side": "buy",
        "status": "accepted",
        "stop_price": null,
        "submitted_at": "2023-10-13T09:22:21.886066537-04:00",
        "symbol": "AAPL",
        "time_in_force": "day",
        "trail_percent": null,
        "trail_price": null,
        "type": "market",
        "updated_at": "2023-10-13T09:22:21.887913787-04:00"
    },
    "timestamp": "2023-10-13T09:22:21.888053477-04:00"
}

:heartbeat

{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:30:01.118487Z",
    "event": "fill",
    "event_id": 10676567,
    "event_ulid": "01HCMKNJJRJ4E3RNFA1XR8CX7R",
    "execution_id": "a958bb42-b034-4d17-bf07-805cf0820ffe",
    "order": {
        "asset_class": "us_equity",
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "cancel_requested_at": null,
        "canceled_at": null,
        "client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
        "commission": "0",
        "created_at": "2023-10-13T13:22:21.887914Z",
        "expired_at": null,
        "extended_hours": false,
        "failed_at": null,
        "filled_at": "2023-10-13T13:30:00.658443088Z",
        "filled_avg_price": "181.36",
        "filled_qty": "0.05513895",
        "hwm": null,
        "id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
        "legs": null,
        "limit_price": null,
        "notional": "10",
        "order_class": "",
        "order_type": "market",
        "qty": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "side": "buy",
        "status": "filled",
        "stop_price": null,
        "submitted_at": "2023-10-13T13:23:05.411141Z",
        "symbol": "AAPL",
        "time_in_force": "day",
        "trail_percent": null,
        "trail_price": null,
        "type": "market",
        "updated_at": "2023-10-13T09:30:00.661902331-04:00"
    },
    "position_qty": "0.05513895",
    "price": "181.36",
    "qty": "0.05513895",
    "timestamp": "2023-10-13T13:30:00.658443088Z"
}

{
    "account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
    "at": "2023-10-13T13:30:02.667443Z",
    "event": "fill",
    "event_id": 10676601,
    "event_ulid": "01HCMKNJK1Y0R7VF6Q6CAC3SH7",
    "execution_id": "33cbb614-bfc0-468b-b4d0-ccf08588ef77",
    "order": {
        "asset_class": "us_equity",
        "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        "cancel_requested_at": null,
        "canceled_at": null,
        "client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
        "commission": "0",
        "created_at": "2023-10-13T09:28:58.361530031-04:00",
        "expired_at": null,
        "extended_hours": false,
        "failed_at": null,
        "filled_at": "2023-10-13T13:30:00.658388668Z",
        "filled_avg_price": "181.36",
        "filled_qty": "0.05513895",
        "hwm": null,
        "id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
        "legs": null,
        "limit_price": null,
        "notional": "10",
        "order_class": "",
        "order_type": "market",
        "qty": null,
        "replaced_at": null,
        "replaced_by": null,
        "replaces": null,
        "side": "buy",
        "status": "filled",
        "stop_price": null,
        "submitted_at": "2023-10-13T09:28:58.360070731-04:00",
        "symbol": "AAPL",
        "time_in_force": "day",
        "trail_percent": null,
        "trail_price": null,
        "type": "market",
        "updated_at": "2023-10-13T09:30:00.665807961-04:00"
    },
    "position_qty": "0.1102779",
    "price": "181.36",
    "qty": "0.05513895",
    "timestamp": "2023-10-13T13:30:00.658388668Z"
}
```

### Message Ordering

For the messages received on the SSE stream we guarantee that the order of the received events is the same as the order they were happening on a per account basis.

Example: if event E1 has been received earlier then another event E2 for the same account, then E1 happened before E2 according to our bookkeeping.

We do not have this guarantee across accounts: if two events for different accounts are received it is the consumer’s responsibility to decide which event happened first based on the timestamp/ulid fields of the event.

Example: E1 happened for account A1 before E2 which was affecting A2. The streaming endpoint might return the events in E1, E2 or E2, E1 ordering. Both responses should be considered valid.

Note: since ULIDs contain a random part other events might have arrived in the same millisecond as the last event received being lexiographicly less than the previous event.

If the stream is used for recon purposes, we recommend to restart the stream from a since that is a few mintues before the time of latest event received.

This approach means that the consumer will receive some events twice when restarting a stream: it is the consumer’s responsibility to process the recevied messages in an idempotent manner so that duplicate messages get ignored on the consumer side.

Note: since and until parameters are parsing as RFC3339 where timezone can be specified (e.g 2006-01-02T15:04:05+07:00), however plus sign character (+) is a special character in HTTP, so use the URL encoded version instead, e.g. ...events/trades?since=2006-01-02T15:04:05%2B07:00

### Comment messages

According to the SSE specification, any line that starts with a colon is a comment which does not contain data. It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.

##### Slow client

The server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`

##### Internal server error

An error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`

## Admin Action Events

These events pertain to administrative actions like account suspensions and liquidations performed by Alpaca Administrators. [See more here](https://docs.alpaca.markets/reference/subscribetoadminactionsse).

Account status change

```
[
  {
    "event_id": "01GTVS4FVS2KJDTPYH2WM6NAXF",
    "at": "2023-09-21T10:52:38.429059991Z",
    "note": "Status changed to REJECTED.", 
    "type": "legacy_note_admin_event", 
    "context": {}, 
    "category": "other", 
    "event_id": "03HBVNXKMWYGFTKTGNVR5R41F2", 
    "correspondent": "ABCD", 
    "belongs_to_kind": "account", 
    "created_by_kind": "admin", 
    "belongs_to_id_reference": "b4fe44b0-e51c-48f4-b674-990bea6cf8d7", 
    "created_by_id_reference": "f0e150df-94ad-48f9-8b0f-05433a3b53c3"
  }
]
```

## Non-Trade Activities Events

Covering non-trade activities like dividends, stock splits, and other corporate actions. [Read more here](https://docs.alpaca.markets/reference/get-v1-events-nta).

You can find some sample responses below:

Cash DIVStock DIVDIVNRASPLITSPINCash MAStock MASCMAREORGREG FEETAF FEEORF FEEOCC FEENRV FEENRC FEELCT FEECSDCSWNCVOFJNLCJNLSOPTRDOPEXPOPASNOPEXCOPCSHINTACATCACATSMGN INTQII INTSWP INTDIV.CDIV (options)NC.SNC (options)SPLIT.RSPLIT (options)SPLIT.FSPLIT (options)MA.SMA (options)SPIN (options)ACATS (options)

```
{
  "id": "{GUID}",
  "qty": 0,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "JEPQ",
  "group_id": "{GROUP_ID}",
  "entry_type": "DIV",
  "net_amount": 0.07,
  "description": "Cash DIV @ 0.465, Pos QTY: 0.15905, Rec Date: 2026-02-02",
  "settle_date": "2026-02-04",
  "system_date": "2026-02-04",
  "entry_sub_type": "CDIV",
  "per_share_amount": 0.46572,
  "corporate_action_id": "{CORP_ACTION_ID}",
  "account_id": "{ACCID}",
  "at": "2026-02-04T05:09:50.214Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0.05,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "LARK",
  "group_id": "{GROUP_ID}",
  "entry_type": "DIV",
  "net_amount": 0,
  "description": "Stock DIV @ 1.05, Pos QTY: -1, Rec Date: 2025-12-01",
  "settle_date": "2025-12-01",
  "system_date": "2025-12-15",
  "entry_sub_type": "SDIV",
  "per_share_amount": 1.05,
  "corporate_action_id": "{CORP_ACTION_ID}",
  "account_id": "{ACCID}",
  "at": "2025-12-15T05:09:50.214Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "YMAG",
  "entry_type": "DIVNRA",
  "net_amount": -1.70,
  "description": "DIV tax withholding on $5.8 at 30% for tax country ARE; w8w9: w8",
  "settle_date": "2026-02-05",
  "system_date": "2026-02-05",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2026-02-05T05:09:50.214Z",
  "event_ulid": "{ULID}"
}
```

```
# Reverse SPLIT
{
  "id": "{GUID}",
  "qty": -0.29194239,
  "price": 5.138,
  "status": "executed",
  "symbol": "FTCI",
  "cusip": "30320C103",
  "entry_type": "SPLIT",
  "net_amount": 0,
  "description": "REMOVE, From QTY:-0.29194239, To QTY:0.029194239, Position Value:1.5",
  "settle_date": "2024-12-02",
  "system_date": "2024-12-02",
  "entry_sub_type": "RSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-01T22:30:42.997Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": 0.029194239,
  "price": 51.38,
  "status": "executed",
  "symbol": "FTCI",
  "cusip": "30320C301",
  "entry_type": "SPLIT",
  "net_amount": 0,
  "description": "ADD, From QTY:-0.29194239, To QTY:0.029194239, Position Value:1.5",
  "settle_date": "2024-12-02",
  "system_date": "2024-12-02",
  "entry_sub_type": "RSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-01T22:33:41.647Z",
  "event_ulid": "{ULID}"
}

# Forward SPLIT
{
  "id": "{GUID}",
  "qty": -0.000807009,
  "price": 102.428,
  "status": "executed",
  "symbol": "ANET",
  "cusip": "040413106",
  "entry_type": "SPLIT",
  "net_amount": 0,
  "description": "REMOVE, From QTY:-0.000807009, To QTY:0.003228036, Position Value:0.08",
  "settle_date": "2024-12-04",
  "system_date": "2024-12-04",
  "entry_sub_type": "FSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-03T23:27:03.971Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": 0.003228036,
  "price": 25.607,
  "status": "executed",
  "symbol": "ANET",
  "cusip": "040413205",
  "entry_type": "SPLIT",
  "net_amount": 0,
  "description": "ADD, From QTY:-0.000807009, To QTY:0.003228036, Position Value:0.08",
  "settle_date": "2024-12-04",
  "system_date": "2024-12-04",
  "entry_sub_type": "FSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-03T23:36:20.775Z",
  "event_ulid": "{ULID}"  
}
```

```
{
  "id": "{GUID}",
  "qty": 0.054339042,
  "price": 12.8328,
  "status": "executed",
  "symbol": "CON",
  "cusip": "20603L102",
  "entry_type": "SPIN",
  "net_amount": 0,
  "description": "Target Symbol: CON, Initiating Symbol: SEM, 0.806971 CON for each 1 SEM",
  "settle_date": "2024-11-26",
  "system_date": "2024-11-26",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-26T00:31:04.184Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": 0.067337044,
  "price": 11.9203,
  "status": "executed",
  "symbol": "SEM",
  "cusip": "81619Q105",
  "entry_type": "SPIN",
  "net_amount": 0,
  "description": "ADD, Cost basis adjustment for source company",
  "settle_date": "2024-11-26",
  "system_date": "2024-11-26",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-26T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": -0.067337044,
  "price": 22.276,
  "status": "executed",
  "symbol": "SEM",
  "cusip": "81619Q105",
  "entry_type": "SPIN",
  "net_amount": 0,
  "description": "REMOVE, Cost basis adjustment for source company",
  "settle_date": "2024-11-26",
  "system_date": "2024-11-26",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-26T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -2,
  "price": 5.88,
  "status": "executed",
  "symbol": "HIE",
  "cusip": "600379101",
  "entry_type": "MA",
  "net_amount": 0,
  "description": "Cash Merger $12.6341694 per share",
  "settle_date": "2024-11-25",
  "system_date": "2024-11-25",
  "entry_sub_type": "CMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-25T10:59:08.776Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "HIE",
  "cusip": "600379101",
  "entry_type": "MA",
  "net_amount": 25.27,
  "description": "Cash Merger $12.6341694 per share",
  "settle_date": "2024-11-25",
  "system_date": "2024-11-25",
  "entry_sub_type": "CMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-25T10:59:08.776Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -0.716836558,
  "price": 24.1617,
  "status": "executed",
  "symbol": "MRO",
  "cusip": "718507106",
  "entry_type": "MA",
  "net_amount": 0,
  "description": "Stock Merger 0.255 COP for 1 MRO",
  "settle_date": "2024-11-22",
  "system_date": "2024-11-22",
  "entry_sub_type": "SMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-21T23:16:27.145Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}",
  "qty": 0.182793322,
  "price": 94.7518,
  "status": "executed",
  "symbol": "COP",
  "cusip": "912656105",
  "entry_type": "MA",
  "net_amount": 0,
  "description": "Stock Merger 0.255 COP for 1 MRO",
  "settle_date": "2024-11-22",
  "system_date": "2024-11-22",
  "entry_sub_type": "SMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-21T23:17:07.588Z",
  "event_ulid": "{ULID}"
}
```

```
# Removal of old shares
{
  "id": "{GUID}",
  "qty": -6.522449746,
  "price": 9.4663,
  "status": "executed",
  "symbol": "PSTX",
  "cusip": "73730P108",
  "entry_type": "MA",
  "net_amount": 0,
  "description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
  "settle_date": "2025-01-13",
  "system_date": "2025-01-13",
  "entry_sub_type": "SCMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2025-01-13T23:01:06.529338Z",
  "event_ulid": "{ULID}"
}


# Allocation of new shares
{
  "id": "{GUID}",
  "qty": 6.522449746,
  "price": 0.4663,
  "status": "executed",
  "symbol": "737CVR019",
  "cusip": "737CVR019",
  "entry_type": "MA",
  "net_amount": 0,
  "description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
  "settle_date": "2025-01-13",
  "system_date": "2025-01-13",
  "entry_sub_type": "SCMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2025-01-13T23:01:06.529338Z",
  "event_ulid": "{ULID}"
}

# Allocation of cash
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "PSTX",
  "cusip": "73730P108",
  "entry_type": "MA",
  "net_amount": 58.7,
  "description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
  "settle_date": "2025-01-13",
  "system_date": "2025-01-13",
  "entry_sub_type": "SCMA",
  "per_share_amount": null,
   "account_id": "{ACCID}",
  "at": "2025-01-13T23:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -8,
  "price": null,
  "status": "executed",
  "symbol": "SRV.RT",
  "cusip": "231631128",
  "entry_type": "REORG",
  "net_amount": 0,
  "description": "Worthless Removal - SRV.RT",
  "settle_date": "2024-11-27",
  "system_date": "2024-11-27",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-26T23:13:33.604Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": -0.01,
  "description": "REG fee for proceed of $15.37 on 2024-12-10 by {ACCOUNT_NUMBER}",
  "settle_date": "2024-12-11",
  "system_date": "2024-12-10",
  "entry_sub_type": "REG",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-10T17:19:17.525338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": -0.01,
  "description": "TAF fee for proceed of 1.371115174 shares (2 trades) on 2024-12-10 by {ACCOUNT_NUMBER}",
  "settle_date": "2024-12-11",
  "system_date": "2024-12-10",
  "entry_sub_type": "TAF",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-10T17:19:17.525338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": -0.17,
  "description": "ORF fee for proceed of 6 contracts on 2024-06-18 by 399748018",
  "settle_date": "2024-06-18",
  "system_date": "2024-06-18",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-06-18T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": -0.02,
  "description": "OCC Clearing Fee",
  "settle_date": "2024-06-18",
  "system_date": "2024-06-18",
  "execution_id": "{EXID}",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-06-18T08:01:06.529338Z",
  "event_ulid": "{ULID}" 
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": 0.05,
  "description": "2024-11-27 Non-Retail - Exchange Fees/Rebates",
  "settle_date": "2024-11-29",
  "system_date": "2024-11-29",
  "entry_sub_type": "NRV",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-29T08:01:06.529338Z",
  "event_ulid": "{ULID}" 
}
```

```
{
  "id": "{GUID}",
  "qty": 1341,
  "price": 0.0025,
  "status": "executed",
  "symbol": "",
  "entry_type": "FEE",
  "net_amount": -3.35,
  "description": "2024-11-27 Non-Retail - Alpaca Trading Fee",
  "settle_date": "2024-11-29",
  "system_date": "2024-11-29",
  "entry_sub_type": "NRC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-29T08:01:06.529338Z",
  "event_ulid": "{ULID}" 
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "swap_rate": 143.6265,
  "entry_type": "FEE",
  "net_amount": -1,
  "description": "Swap Fee Gross Income",
  "settle_date": "2024-10-02",
  "system_date": "2024-10-01",
  "execution_id": "{EXEC ID}",
  "entry_sub_type": "LCT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-08-01T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "CSD",
  "net_amount": 100,
  "description": "",
  "settle_date": "2024-03-11",
  "system_date": "2024-03-11",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-03-11T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "CSW",
  "net_amount": -32.97,
  "description": "type: ach, subtype: none, statement_id: 4f0cfc49-0395-475c-b8ca-3586e394d256, direction: OUTGOING",
  "settle_date": "2024-09-20",
  "system_date": "2024-09-20",
  "account_id": "{ACCID}",
  "event_ulid": "{ULID}",
  "at": "2024-09-20T08:01:06.529338Z",
  "per_share_amount": null
}
```

```
# Symbol Name Change (SNC)
{
  "id": "{GUID}",
  "qty": -1.25,
  "price": 9.99,
  "status": "executed",
  "symbol": "YTEN",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from YTEN to YTENQ",
  "settle_date": "2024-12-10",
  "system_date": "2024-12-10",
  "entry_sub_type": "SNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-09T23:01:06.529338Z",
  "event_ulid": "{ULID}"
}

{
  "id": "{GUID}",
  "qty": 1.25,
  "price": 9.99,
  "status": "executed",
  "symbol": "YTENQ",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from YTEN to YTENQ",
  "settle_date": "2024-12-10",
  "system_date": "2024-12-10",
  "entry_sub_type": "SNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-09T23:01:06.529338Z",
  "event_ulid": "{ULID}"
}

# CUSIP Name Change (CNC)
{
  "id": "{GUID}",
  "qty": -150,
  "price": 0.045,
  "status": "executed",
  "symbol": "RMSGW",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from RMSGW to RMSGW",
  "settle_date": "2024-11-21",
  "system_date": "2024-11-21",
  "entry_sub_type": "CNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-21T00:22:06.529338Z",
  "event_ulid": "{ULID}"
}

{
  "id": "{GUID}",
  "qty": 150,
  "price": 0.045,
  "status": "executed",
  "symbol": "RMSGW",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from RMSGW to RMSGW",
  "settle_date": "2024-11-21",
  "system_date": "2024-11-21",
  "entry_sub_type": "CNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-11-21T00:22:06.529338Z",
  "event_ulid": "{ULID}"
}

# Symbol & CUSIP Name Change (SCNC)

{
  "id": "{GUID}",
  "qty": -29,
  "price": 0.3166,
  "status": "executed",
  "symbol": "DXFFY",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from DXFFY to DXFFD",
  "settle_date": "2024-12-04",
  "system_date": "2024-12-04",
  "entry_sub_type": "SCNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-03T23:11:06.529338Z",
  "event_ulid": "{ULID}"
}

{
  "id": "{GUID}",
  "qty": 29,
  "price": 0.3166,
  "status": "executed",
  "symbol": "DXFFD",
  "cusip": "591018809",
  "entry_type": "NC",
  "net_amount": 0,
  "description": "Name Change from DXFFY to DXFFD",
  "settle_date": "2024-12-04",
  "system_date": "2024-12-04",
  "entry_sub_type": "SCNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-03T23:12:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 2650,
  "price": null,
  "status": "executed",
  "symbol": "067RGT019",
  "cusip": "067RGT019",
  "entry_type": "VOF",
  "net_amount": 0,
  "description": "BNED rights distribution",
  "settle_date": "2024-05-17",
  "system_date": "2024-05-17",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
{
  "id": "{GUID}", 
  "qty": -2500, 
  "price": null, 
  "status": "executed", 
  "symbol": "067RGT019", 
  "cusip": "067RGT019",
  "entry_type": "VOF", 
  "net_amount": 0, 
  "description": "Rights Exercise (symbol BNED; expiration 06/05/24)", 
  "settle_date": "2024-06-05", 
  "system_date": "2024-06-05", 
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-06-05T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "pending",
  "symbol": "",
  "entry_type": "JNLC",
  "net_amount": -0.29,
  "description": "Journal ID: {Journal ID}",
  "settle_date": "2024-05-17",
  "system_date": "2024-05-17",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -0.008611,
  "price": 993,
  "status": "executed",
  "symbol": "TSLA",
  "cusip": "88160R101",
  "entry_type": "JNLS",
  "net_amount": 0,
  "description": "ID: {ACCID} - {ACCID}",
  "settle_date": "2023-07-18",
  "system_date": "2023-07-18",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-07-18T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
"id": "{GUID}", 
 "qty": 100, 
 "cusip": "{CUSIP}",
 "price": 285, 
 "status": "executed",
 "symbol": "IBM", 
 "group_id": "{GROUP_ID}", 
 "entry_type": "OPTRD", 
 "net_amount": -28500, 
 "description": "Options Trade", 
 "settle_date": "2026-02-19", 
 "system_date": "2026-02-18", 
 "per_share_amount": null, 
 "account_id": "{ACCID}", 
 "at": "2026-02-19T05:09:50.529338Z", 
 "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -1,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "META260218C00667500",
  "group_id": "{GROUP_ID}",
  "entry_type": "OPEXP",
  "net_amount": 0,
  "description": "Options Expiry",
  "settle_date": "2026-02-18",
  "system_date": "2026-02-18",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2026-02-18T05:09:50.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 1,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "MSTX260220P00003500",
  "group_id": "{GROUP_ID}",
  "entry_type": "OPASN",
  "net_amount": 0,
  "description": "Options Assignment",
  "settle_date": "2026-02-18",
  "system_date": "2026-02-18",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2026-02-18T05:09:50.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -1,
  "cusip": "{CUSIP}",
  "price": null,
  "status": "executed",
  "symbol": "AUTL260220C00001500",
  "group_id": "{GROUP_ID}",
  "entry_type": "OPEXC",
  "net_amount": 0,
  "description": "Options Exercise",
  "settle_date": "2026-02-18",
  "system_date": "2026-02-18",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2026-02-18T05:09:50.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "group_id": "{GROUP_ID}",
  "entry_type": "OPCSH",
  "net_amount": -115.88,
  "description": "Options Cash",
  "settle_date": "2026-01-20",
  "system_date": "2026-01-16",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2026-01-20T05:09:50.289922Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "INT",
  "net_amount": -0.02,
  "description": "Monthly Int - {Month} {Year}",
  "settle_date": "2023-07-31",
  "system_date": "2023-08-01",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-08-01T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "swap_rate": 1,
  "entry_type": "ACATC",
  "net_amount": 5,
  "description": "",
  "settle_date": "2024-05-17",
  "system_date": "2024-05-17",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 6,
  "price": 135.34,
  "status": "executed",
  "symbol": "NVDA",
  "cusip": "67066G104",
  "entry_type": "ACATS",
  "net_amount": 0,
  "description": "DTC TRANSFER",
  "settle_date": "2024-12-02",
  "system_date": "2024-12-02",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-12-02T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
 	"qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "",
  "entry_type": "INT",
  "net_amount": -54.14,
  "description": "Monthly Int - SEPTEMBER 2024",
  "settle_date": "2024-09-30",
  "system_date": "2024-10-01",
  "entry_sub_type": "MGN",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-08-01T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": 0,
  "price": null,
  "status": "executed",
  "symbol": "TLT",
  "cusip": "464287432",
  "entry_type": "INT",
  "net_amount": 0.2,
  "description": "Qualified interest income reallocation for 2024",
  "settle_date": "2024-12-06",
  "system_date": "2024-12-06",
  "entry_sub_type": "QII",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-08-01T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
 	"qty": 9.25,
  "price": null,
  "status": "executed",
  "symbol": "SWEEPFDIC",
  "cusip": "SWEEPFDIC",
  "entry_type": "INT",
  "net_amount": 0,
  "description": "September 2024 Sweep",
  "settle_date": "2024-09-30",
  "system_date": "2024-09-30",
  "entry_sub_type": "SWP",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2023-08-01T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

```
{
  "id": "{GUID}",
  "qty": -5,
  "price": 0.49,
  "status": "executed",
  "symbol": "F250228P00010000",
  "entry_type": "OPCA",
  "net_amount": 245,
  "description": "REMOVE old contract symbol",
  "settle_date": "2025-02-18",
  "system_date": "2025-02-18",
  "entry_sub_type": "DIV.CDIV",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 5,
  "price": 0.49,
  "status": "executed",
  "symbol": "F250228P00009850",
  "entry_type": "OPCA",
  "net_amount": -245,
  "description": "ADD new contract symbol",
  "settle_date": "2025-02-18",
  "system_date": "2025-02-18",
  "entry_sub_type": "DIV.CDIV",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": -2,
  "price": 1.13,
  "status": "executed",
  "symbol": "NKLA270115C00000500",
  "entry_type": "OPCA",
  "net_amount": 226,
  "description": "REMOVE old contract symbol",
  "settle_date": "2025-02-26",
  "system_date": "2025-02-26",
  "entry_sub_type": "NC.SNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 2,
  "price": 1.13,
  "status": "executed",
  "symbol": "NKLAQ270115C00000500",
  "entry_type": "OPCA",
  "net_amount": -226,
  "description": "ADD new contract symbol",
  "settle_date": "2025-02-26",
  "system_date": "2025-02-26",
  "entry_sub_type": "NC.SNC",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": -15,
  "price": 0.08,
  "status": "executed",
  "symbol": "WKHS250417C00002000",
  "entry_type": "OPCA",
  "net_amount": 120,
  "description": "REMOVE old contract symbol",
  "settle_date": "2025-03-17",
  "system_date": "2025-03-17",
  "entry_sub_type": "SPLIT.RSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 15,
  "price": 0.08,
  "status": "executed",
  "symbol": "WKHS2250417C00002000",
  "entry_type": "OPCA",
  "net_amount": -120,
  "description": "ADD new contract symbol",
  "settle_date": "2025-03-17",
  "system_date": "2025-03-17",
  "entry_sub_type": "SPLIT.RSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": -1,
  "price": 10.5,
  "status": "executed",
  "symbol": "LRCX241115C00950000",
  "entry_type": "OPCA",
  "net_amount": 1050,
  "description": "REMOVE old contract symbol",
  "settle_date": "2024-10-03",
  "system_date": "2024-10-03",
  "entry_sub_type": "SPLIT.FSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 10,
  "price": 1.05,
  "status": "executed",
  "symbol": "LRCX241115C00095000",
  "entry_type": "OPCA",
  "net_amount": -1050,
  "description": "ADD new contract symbol",
  "settle_date": "2024-10-03",
  "system_date": "2024-10-03",
  "entry_sub_type": "SPLIT.FSPLIT",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": -2,
  "price": 0.65,
  "status": "executed",
  "symbol": "CEIX250117P00095000",
  "entry_type": "OPCA",
  "net_amount": 130,
  "description": "REMOVE old contract symbol",
  "settle_date": "2025-01-15",
  "system_date": "2025-01-15",
  "entry_sub_type": "MA.SMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 2,
  "price": 0.65,
  "status": "executed",
  "symbol": "CNR1250117P00095000",
  "entry_type": "OPCA",
  "net_amount": -130,
  "description": "ADD new contract symbol",
  "settle_date": "2025-01-15",
  "system_date": "2025-01-15",
  "entry_sub_type": "MA.SMA",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": -1,
  "price": 0.24,
  "status": "executed",
  "symbol": "CMPO250417C00020000",
  "entry_type": "OPCA",
  "net_amount": 24,
  "description": "REMOVE old contract symbol",
  "settle_date": "2025-02-28",
  "system_date": "2025-02-28",
  "entry_sub_type": "SPIN",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}

{
  "id": "{GUID}",
  "qty": 1,
  "price": 0.24,
  "status": "executed",
  "symbol": "CMPO1250417C00020000",
  "entry_type": "OPCA",
  "net_amount": -24,
  "description": "ADD new contract symbol",
  "settle_date": "2025-02-28",
  "system_date": "2025-02-28",
  "entry_sub_type": "SPIN",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2024-05-17T08:01:06.529338Z",
  "event_ulid": "{ULID}",
  "group_id": "617b39aa-475b-42cd-87c9-a5bde79b149b"
}
```

```
{
  "id": "{GUID}",
  "qty": 1,
  "price": 23.75,
  "status": "executed",
  "symbol": "PLTR261218C00120000",
  "entry_type": "ACATS",
  "net_amount": 0,
  "description": "ACAT Transfer 20250500034276",
  "settle_date": "2025-02-27",
  "system_date": "2025-02-27",
  "per_share_amount": null,
  "account_id": "{ACCID}",
  "at": "2025-02-27T08:01:06.529338Z",
  "event_ulid": "{ULID}"
}
```

## System Events

These events pertain to system-wide actions, and are mainly created by automated processes on our backends. [Documentation here](https://docs.alpaca.markets/reference/subscribeToSystemEventV2SSE)

Ballance sync readyPosition sync ready

```
{
  "event_id": "01KE90MX0DXW9NCG9HT4N2WDPW",
  "at": "2026-01-06T06:41:57.261948Z",
  "type": "eod_balances_ready", 
  "system_date": "2026-01-05",
  "description": "End-of-day balances are now available."
}
```

```
{
  "event_id": "01KE90P5Q4J1WPBEF6075A48RE",
  "at": "2026-01-06T06:42:38.948967Z",
  "type": "eod_positions_ready", 
  "system_date": "2026-01-05",
  "description": "End-of-day positions are now available."
}
```

Updated 5 days ago

---

Ask AI

---

# Account Status Events for KYCaaS (https://docs.alpaca.markets/docs/account-status-events-for-kycaas)

# Account Status Events for KYCaaS

For partners who utilize Alpaca’s KYC service for opening brokerage accounts, if an account is moved to `ACTION_REQUIRED` or `APPROVAL_PENDING` then that indicates that additional action may be needed from you or your user to approve the account. These status updates, along with the reason for the status change, will be relayed in real time via the [Account Status Events](https://docs.alpaca.markets/reference/suscribetoaccountstatussse). The specific KYC results that may require action from your end user will wind up in `ACCEPT`, `INDETERMINATE`, or `REJECT`. The `additional_information` field will be used to relay custom messages from our account opening team. If a KYC result is returned via the `ACCEPT` object then no further action is needed to resolve the request. KYC results returned in the `INDETERMINATE` or `REJECT` objects will require further action before the account can be opened. The following tables can be used to determine what is required from the account opener.

**Documentation Required**

| KYC Result Code | Government Issued ID Card | Tax ID Card | Statement (utility bill, etc.) | Selfie |
| --- | --- | --- | --- | --- |
| `IDENTITY_VERIFICATION` | **REQUIRED** |  |  |  |
| `TAX_IDENTIFICATION` |  | **REQUIRED** |  |  |
| `ADDRESS_VERIFICATION` | OPTIONAL |  | OPTIONAL |  |
| `DATE_OF_BIRTH` | **REQUIRED** |  |  |  |
| `SELFIE_VERIFICATION` |  |  |  | **REQUIRED** |

**Additional Information Required**

| KYC Result Code | Additional Information Required |
| --- | --- |
| `PEP` | Job title / occupation and address |
| `FAMILY_MEMBER_PEP` | Name of politically exposed person if immediate family |
| `CONTROL_PERSON` | Company name, company address, and company email |
| `AFFILIATED` | Company / firm name, company / firm address, company / firm email |
| `VISA_TYPE_OTHER` | Visa type and expiration date |
| `W8BEN_CORRECTION` | An updated W8BEN form with corrected information |
| `OTHER` | For specific cases our operational team might return with a customized message within the additional\_information attribute. |

Updated 4 months ago

---

Ask AI

---

# Daily Processes and Reconcilations (https://docs.alpaca.markets/docs/daily-processes-and-reconcilations)

# Daily Processes and Reconcilations

# Daily Processes

There are a few daily timings you want to keep in mind when you think about the operation. Note that these schedules follow daylight savings time.

| Process | Timing | Notes |
| --- | --- | --- |
| Beginning-of-day Sync (BOD) | 02:15AM-02:30AM EST | Trading accounts are updated with the previous day end-of-day values. Trade confirms are also synchronized around this time. |
| Incoming wire processing | 08:00AM-08:30AM EST | The incoming wires with FFC instructions are booked |
| Outgoing wire cutoff | 04:00PM EST | The outgoing wire requests before the cutoff will be processed for the day. |
| ACH cutoff | 02:00PM EST | The credit/debit of ACH requests before the cutoff will be processed for the day. |
| Trade reporting | 06:30PM-07:30PM EST | The day’s trades are finalized and reported. |
| End-of-day calculation (EOD) | 11:00PM-11:30PM EST | Close the day’s book, mark to market positions, cost basis calculation, margin requirements calculation etc. |

# Mandatory Corporate Actions

Currently the corporate actions are processed a semi-automated way, and you will see such records in Activity API as they happen. We are working to provide upfront information separately in the future.

## Dividends

Dividends are the most common corporate actions. The cash is paid (credited) to the customer accounts after the pay date, as we receive the cash from DTC. Please note that the actual credit transactions may be after the pay date if we don’t receive the cash from DTC. When such payout is transacted, you will see the account activity in Activity API as the DIV entry type.

Dividends are income gain. If your end customers are non-US residents, 30% withholding is applied by default. In case you claim to apply different rates for the tax treaty, please contact us.

Dividends are processed without waiting for DTC in the sandbox environment. This may not reflect the live side operation.

## Forward Splits and Reverse Splits

Share splits are processed as they happen and the beginning-of-day process will update the positions of the customer accounts. Both appear as a SPLIT entry type in the activity. In the case of reverse splits, there might be the cash in lieu for non-divisible shares which will not be processed immediately until we receive the cash from DTC.

## Symbol/CUSIP Change and Listing/Delisting

The symbol or CUSIP can change one day for a particular asset. The asset master data is refreshed on a daily basis and we do recommend you retrieve the asset endpoint every morning before the market open (or after the beginning-of-day timing). While Alpaca does not currently participate in the initial public offering, such stock on the IPO day will become tradable on the day it is listed, and start filling orders once the secondary market opens.

## Other Events

Mergers, acquisitions, and other type events are processed manually in our back office as they are rare and each case is often unique. Please contact Alpaca’s broker-dealer operation team if you have any questions.

# ACATS

Alpaca processes both sending and receiving ACATS requests. As of today, you can request our operation team for the receiving request, but we plan to provide this service as an API in the future.

# Monthly Processes

Monthly statement emails should be sent for the prior month on or before the 10th of the following month - for example, for the monthly statement for August, delivery via email must be on or prior to September 10.

Updated 3 months ago

---

Ask AI

---

# Banking Holiday Funding Processes (https://docs.alpaca.markets/docs/holiday-funding-processes)

# Banking Holiday Funding Processes

This section addresses operational procedures for scenarios where the bank is closed for a holiday, but the stock market remains open for trading (e.g., Columbus Day, Veterans Day).

# Funding & JIT

  

**Bank Holiday but Markets Trading:** The stock market will be open and trading as usual, but banks will be closed for the federal holiday.

**JIT Operations Continue as Normal:** Our Just-in-Time (JIT) funding operations will continue to run without interruption.

**Still Reconcile and Send Reports:** Partners should continue to reconcile trades and send required reports on time for both the preceding trading day and the market open holiday.

**Partners Should Treat as Two Separate Normal Trading Days:** Both the preceding trading day and the market open holiday trading sessions should be processed as distinct, regular trading days.

**Settlement Due for Holiday & Next Business Day:** Settlement Amount is Required by 1:00 PM EST business day after the bank holiday for Payment.

**Two Separate Wires on the First Business Day After a Holiday:** Partners should anticipate two distinct wire transfers on the morning of the first business day following a holiday — one representing the settlement from the prior business day and the other for the settlement on the holiday itself.

**Implementing Safety Measures to Prevent Amount Errors:** Our Engineering team have enhanced safety measures and checks to ensure accuracy and prevent any amount errors related to the dual-day settlement.

  

# Instant Funding

**Code Fixed to Base on Trade Settlement vs. Bank Holidays:** Our Instant Funding logic has been fixed to prioritize the trade settlement schedule over bank holidays, ensuring more consistent processing.

**Partners Need Settlement Amount by 1 PM ET:** Partners must provide the necessary settlement amount by 1:00 PM ET on the bank holiday to ensure Instant Funding is processed for payment on the next bank business day.

**RF Account Option for Instant Settlement During Holidays:** Partners can utilize the RF account option for instant settlement of funds during bank holiday periods.

**Partners Can Pre-Fund to Avoid Limit Issues:** We encourage partners to pre-fund their accounts ahead of long weekends or holidays where applicable to avoid hitting pre-set funding limits.

  

# Funds Processing

**Currency Cloud Transactions May Still Post:** Funds sent using Currency Cloud may still post to your account on a bank holiday, provided the transaction does not pass through a US bank for final processing.

**Wire Transfers and ACH Will Not Be Processed:** All standard US-based Wire Transfers and ACH transactions will be paused and will not be processed on the bank holiday. Processing will resume on the next bank business day.

Updated 3 months ago

---

Ask AI

---

# Statements and Confirms (https://docs.alpaca.markets/docs/statements-and-confirms)

# Statements and Confirms

# Requirements

Under the FINRA and SEC rules, Alpaca is required to ensure the customer statements and trade confirms are delivered correctly in time to the end customers. That being said, the actual communication and delivery do not have to be done by Alpaca directly. Very often, you want to own the full user experiences and to be responsible for these communications, which is totally possible.

# Document API Integration

You can retrieve the generated reports in PDF format through the [Documents API](https://docs.alpaca.markets/reference/downloaddocfromaccount). You can store the files on your storage if it is required for your regulation purpose, or you can let your customers download the files using the URL returned in the API response. If you are a fully-disclosed broker-dealer, you can insert your firm logo, name and address in the PDF template. Please send those data to Alpaca.

If you need even more customization on the template, we are currently working on the new API endpoint which will return only the data points so that you can build fully-customized documents with your own template. Alpaca still needs to review your final version of customized documents before delivering to the end customers for the first time.

Updated 5 days ago

---

Ask AI

---

# Local Currency Trading (LCT) (https://docs.alpaca.markets/docs/local-currency-trading-lct)

# Local Currency Trading (LCT)

Local Currency Trading allows customers to trade US equities in over 15+ local currencies, with FX conversion done on-the-fly. Customers can place, monitor and sell their positions in their local currency.

API responses are all in your local currency, with all calculations handled by Alpaca.

Further below, we will examine the some common scenarios with LCT. The recurring theme you will notice is that many of Alpaca’s API commands are almost the same, it is just the response that have changed. In some cases, barring the introduction of a currency specification or a swap rate, the only indication of the trade being in Local Currency is the inclusion of a USD second order JSON.

For further questions about LCT, such as supported currencies or any other relevant details, see [LCT FAQs](https://alpaca.markets/support/local-currency-trading-faq).

# Supported Features

| Features | LCT | Broker API (USD) |
| --- | --- | --- |
| Allows trading in user's/broker local currency of US equities | ✅ | ⛔️ |
| Supports JIT | ✅ | ✅ |
| Stop and Limit orders with Extended-Hours | ✅ | ✅ |
| Swap rate on the orders endpoint | ✅ | ⛔️ |
| Supports crypto trading | ⛔️ | ✅ |
| Market Data | ✅ (in local currency) | ⛔️ |
| Omnibus | ✅ | ✅ |
| Omnibus in subledger | ✅ | ✅ |
| Fully-disclosed account type | ✅ | ✅ |
| SSE Events | ✅ | ✅ |
| Rebalancing | ⛔️ | ✅ |
| Margin Trading | ⛔️ | ✅ |

# Get Market Data

With LCT, we have introduced a currency parameter for stock market data. You can request pricing data for any equity and we will handle the necessary conversions to quote the asset in the requested local currency.

The example below shows how to get pricing data for AAPL in JPY. The pricing information is converted from USD to the relevant local currency on the fly with the latest FX rate at the point in time of query.

cURL

```
curl --request GET 'https://data.alpaca.markets/v2/stocks/AAPL/bars?start=2024-08-01T0:00:00Z&end=2024-08-19T11:00:00Z&timeframe=1Min&currency=JPY'
```

JSON

```
{
    "bars": [
        {
            "c": 33481.21,
            "h": 33536.65,
            "l": 33476.71,
            "n": 129,
            "o": 33536.65,
            "t": "2024-08-01T08:00:00Z",
            "v": 2750,
            "vw": 33519.41
        },
        ...
    ],
    "currency": "JPY",
    "next_page_token": "QUFQTHxNfDE3MjI1OTg1NjAwMDAwMDAwMDA=",
    "symbol": "AAPL"
}
```

Note currency key value is `JPY`. Request the same endpoint without the `currency` parameter to compare the pricing data against its `USD` equivalent.

# Create an LCT Account

For LCT, you can leverage the traditional [Accounts API](reference/getallaccounts) to create any of the following account types:

* Fully Disclosed
* Omnibus
* Omnibus via the Alpaca Sub Ledger Solution

Below we provide an example of creating a account for a fully-disclosed setup with JPY as the local currency.

JSON

```
{
  "contact": {
    "email_address": "[email protected]",
    "phone_number": "555-666-7788",
    "street_address": ["20 N San Mateo Dr"],
    "city": "San Mateo",
    "state": "CA",
    "postal_code": "94401",
    "country": "USA"
  },
  "identity": {
    "given_name": "John",
    "family_name": "Doe",
    "date_of_birth": "1990-01-01",
    "tax_id": "666-55-4321",
    "tax_id_type": "USA_SSN",
    "country_of_citizenship": "USA",
    "country_of_birth": "USA",
    "country_of_tax_residence": "USA",
    "funding_source": ["employment_income"],
    "annual_income_min": "30000",
    "annual_income_max": "50000",
    "liquid_net_worth_min": "100000",
    "liquid_net_worth_max": "150000"
  },
  "disclosures": {
    "is_control_person": false,
    "is_affiliated_exchange_or_finra": false,
    "is_politically_exposed": false,
    "immediate_family_exposed": false
  },
  "agreements": [
   {
      "agreement": "customer_agreement",
      "signed_at": "2020-09-11T18:13:44Z",
      "ip_address": "185.13.21.99",
      "revision": "19.2022.02"
   },
   {
      "agreement": "crypto_agreement",
      "signed_at": "2020-09-11T18:13:44Z",
      "ip_address": "185.13.21.99",
      "revision": "04.2021.10"
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
    "email_address": "[email protected]"
  },
  "currency": "JPY"
}
```

Note the newly introduced `currency` parameter as part of the payload to create a new code.

# Fund LCT Account

Accounts can be funded for LCT by either:

* Bank Wire
* Just in Time Cash
* Just In Time

The below example funds one of our JPY accounts created above, with JIT API `POST /v1/transfers/jit/transactions` with the following body:

JSON

```
{
  "account_id": "27529bc0-3ab5-34f5-ac29-54a98162472d",
  "entry_type": "JTD",
  "currency": "JPY",
  "amount": "500000",
  "description": "Test JIT JPY"
}
```

Calling the above mentioned API yields the following response,

JSON

```
{
    "id": "9a0ab8c2-4575-46b6-a6cc-f280c899b756",
    "account_id": "27529bc0-3ab5-34f5-ac29-54a98162472d",
    "created_at": "2022-08-31T16:29:44-04:00",
    "system_date": "2022-08-31",
    "entry_type": "JTD",
    "amount": "500000",
    "currency": "JPY",
    "description": "Test JIT JPY"
}
```

# Estimate Stock Order

Customers using LCT for the first time may not be sure how much their local currency can buy of a US stock. To address this pain point we created the [Order Estimation Endpoint](/reference/get-v1-trading-accounts-account_id-orders-estimation). The customer can enter:

* the security
* the notional value
* on the developer side you can input your swap rate to return the realistic value that your customer will receive.

We get in return indicative quantity, average price and USD value.

JSON

```
{
  "symbol": "AAPL",
  "side": "buy",
  "type": "market",
  "time_in_force": "day",
  "notional": "4000",
  "swap_fee_bps": 100
}
```

The above payload will get an estimation for a market order to purchase AAPL stock with a notional amount of 4000 JPY.

JSON

```
{
  "id": "2f88dc2f-b9d8-4d52-aa35-fa8e076be3a3",
  "client_order_id": "8cfc4159-1e07-438b-bdda-1d37a0176bc7",
  "created_at": "2024-08-20T09:58:57.119084817Z",
  "updated_at": "2024-08-20T09:58:57.137113377Z",
  "submitted_at": "2024-08-20T09:58:57.119084817Z",
  "filled_at": "2024-08-20T09:58:57.119084817Z",
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0.1189",
  "filled_avg_price": "33109.4937825",
  "order_class": "",
  "order_type": "market",
  "type": "market",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": null,
  "status": "filled",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "swap_rate": "146.4795",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.3075",
    "filled_avg_price": "226.035",
    "limit_price": null,
    "stop_price": null
  }
}
```

Note the `usd` object at the bottom.

# Submit Order

Alpaca currently supports LCT trading for market, limit, stop & stop limit orders with a **time in force=Day**, accommodating both fractional quantities and notional values. You can pass either a fractional amount (qty), or a notional value (notional) in your local currency in any POST/v2/orders request. Note that entering a value for either parameters, will automatically nullify the other. If both qty and notional are entered the request will be rejected with an error status 400.

Moreover, we support fractional shares trading not only during standard market hours, but extending into pre-market (4:00 a.m. - 9:30 a.m. ET) and post-market (4:00 p.m. - 8:00 p.m. ET) hours, offering global investors the ability to trade during the full extended hours session.

## Submit a Stock Market Order

Once having estimated a given order, we can actually commit to and execute the order using the usual [Orders API](/reference/createorderforaccount).

We note here a few key LCT specific order attributes:

* `swap_fee_bps` - this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted

NotionalQuantity

```
{
  "side": "buy",
  "type": "market",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "notional": "4000",
  "swap_fee_bps": "100"
}
```

```
{
  "side": "buy",
  "type": "market",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "qty": "1",
  "swap_fee_bps": "100"
}
```

The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,

NotionalQuantity

```
{
  "id": "c02b6a70-4fa1-4906-a6b8-1a6c6acc66c5",
  "client_order_id": "c0f1f5b0-9234-4356-89cf-181c9efb54ef",
  "created_at": "2024-08-19T10:25:55.259941759Z",
  "updated_at": "2024-08-19T10:25:55.261581339Z",
  "submitted_at": "2024-08-19T10:25:55.259941759Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "market",
  "type": "market",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": null,
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "146.4085",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.3208",
    "filled_avg_price": null,
    "limit_price": null,
    "stop_price": null
  }
}
```

```
{
  "id": "eafe73ef-107f-40fc-9fed-75bc1b3f145f",
  "client_order_id": "7f31aa39-fabd-4d35-a1dd-a0db3fd2ca0b",
  "created_at": "2024-08-19T10:27:50.850340619Z",
  "updated_at": "2024-08-19T10:27:50.851623759Z",
  "submitted_at": "2024-08-19T10:27:50.850340619Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "1",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "market",
  "type": "market",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": null,
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "146.4515",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": null,
    "filled_avg_price": null,
    "limit_price": null,
    "stop_price": null
  }
}
```

## Submit a Stock Limit Order

We note here a few key LCT specific order attributes:

* `limit_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `swap_fee_bps` - this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted
* Extended-Hours orders will also be accepted

NotionalQuantityNotional Extended-HoursQuantity Extended-Hours

```
{
  "side": "buy",
  "type": "limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "notional": "4000",
  "symbol": "AAPL",
  "limit_price": "226",
  "swap_fee_bps": "100"
}
```

```
{
  "side": "buy",
  "type": "limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "limit_price": "226",
  "swap_fee_bps": "100",
  "qty": "1"
}
```

```
{
  "side": "buy",
  "type": "limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "notional": "4000",
  "symbol": "AAPL",
  "limit_price": "226",
  "swap_fee_bps": "100",
  "extended_hours": true
}
```

```
{
  "side": "buy",
  "type": "limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "limit_price": "226",
  "swap_fee_bps": "100",
  "qty": "1",
  "extended_hours": true
}
```

The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,

NotionalQuantityNotional Extended-HoursQuantity Extended-Hours

```
{
  "id": "49a5badc-a480-4d56-a765-71808c970885",
  "client_order_id": "78f3d279-c8bd-41ea-9e6e-3b76846f8b22",
  "created_at": "2024-08-19T10:52:35.927390475Z",
  "updated_at": "2024-08-19T10:52:35.928676035Z",
  "submitted_at": "2024-08-19T10:52:35.927390475Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "limit",
  "type": "limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "33387",
  "stop_price": null,
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.72765",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.0768",
    "filled_avg_price": null,
    "limit_price": "226",
    "stop_price": null
  }
}
```

```
{
  "id": "f86b3bee-8f40-4951-8805-e489b42bbdff",
  "client_order_id": "2db8a272-4948-4416-afb7-d8af74621d51",
  "created_at": "2024-08-19T10:54:35.993838801Z",
  "updated_at": "2024-08-19T10:54:35.995571381Z",
  "submitted_at": "2024-08-19T10:54:35.993838801Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "1",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "limit",
  "type": "limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "33389",
  "stop_price": null,
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.738255",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": null,
    "filled_avg_price": null,
    "limit_price": "226",
    "stop_price": null
  }
}
```

```
{
  "id": "9562cde5-cb43-49fe-a85e-c8342df2b55e",
  "client_order_id": "1d5dc589-9566-4f17-b6d9-d0b028bfe16a",
  "created_at": "2024-08-19T10:56:03.761481808Z",
  "updated_at": "2024-08-19T10:56:03.763734497Z",
  "submitted_at": "2024-08-19T10:56:03.761481808Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "limit",
  "type": "limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "33404",
  "stop_price": null,
  "status": "pending_new",
  "extended_hours": true,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.804915",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.0626",
    "filled_avg_price": null,
    "limit_price": "226",
    "stop_price": null
  }
}
```

```
{
  "id": "89986aad-d019-468f-bbc6-c83abd391f4b",
  "client_order_id": "af5236c7-5b3e-44c7-8ef5-2be2a6f921f8",
  "created_at": "2024-08-19T10:57:33.6435754Z",
  "updated_at": "2024-08-19T10:57:33.64546282Z",
  "submitted_at": "2024-08-19T10:57:33.6435754Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "1",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "limit",
  "type": "limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "33407",
  "stop_price": null,
  "status": "pending_new",
  "extended_hours": true,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.81653",
  "swap_fee_bps": "150",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": null,
    "filled_avg_price": null,
    "limit_price": "226",
    "stop_price": null
  }
}
```

## Submit a Stock Stop Order

We note here a few key LCT specific order attributes:

* `stop_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* Stop buy orders are automatically converted into Stop Limit Buy orders for risk protection [Stop Orders Conversion](https://docs.alpaca.markets/docs/orders-at-alpaca#stop-orders).
* `swap_fee_bps` - this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted

NotionalQuantity

```
{
  "side": "buy",
  "type": "stop",
  "time_in_force": "day",
  "commission_type": "notional",
  "notional": "4000",
  "symbol": "AAPL",
  "stop_price": "230"
}
```

```
{
  "side": "buy",
  "type": "stop",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "stop_price": "230",
  "qty": "1"
}
```

The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,

NotionalQuantity

```
{
  "id": "274361ce-7c05-4ad0-83ed-517603685f17",
  "client_order_id": "eb829da0-7c58-4efd-be76-a5707c3548dd",
  "created_at": "2024-08-19T11:01:47.400438062Z",
  "updated_at": "2024-08-19T11:01:47.402600012Z",
  "submitted_at": "2024-08-19T11:01:47.400438062Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "stop",
  "type": "stop",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": "34001",
  "status": "new",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.82663",
  "swap_fee_bps": "100",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.0587",
    "filled_avg_price": null,
    "limit_price": "235.75",
    "stop_price": "230"
  }
}
```

```
{
  "id": "fb9546aa-9e27-4bfb-b758-5fa23571da56",
  "client_order_id": "6da8e54a-568b-4252-bef0-d06c3aabac4e",
  "created_at": "2024-08-19T11:05:43.513481595Z",
  "updated_at": "2024-08-19T11:05:43.515201354Z",
  "submitted_at": "2024-08-19T11:05:43.513481595Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "1",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "stop",
  "type": "stop",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": null,
  "stop_price": "33983",
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.749365",
  "swap_fee_bps": "100",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": null,
    "filled_avg_price": null,
    "limit_price": "235.75",
    "stop_price": "230"
  }
}
```

## Submit a Stock Stop Limit Order

We note here a few key LCT specific order attributes:

* `stop_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `limit_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `swap_fee_bps` - this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted

NotionalQuantity

```
{
  "side": "buy",
  "type": "stop_limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "notional": "4000",
  "symbol": "AAPL",
  "stop_price": "230",
  "limit_price": "235"
}
```

```
{
  "side": "buy",
  "type": "stop_limit",
  "time_in_force": "day",
  "commission_type": "notional",
  "symbol": "AAPL",
  "stop_price": "230",
  "qty": "1",
  "limit_price": "235"
}
```

The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,

NotionalQuantity

```
{
  "id": "1a643eba-f503-4add-ac55-c605680e17a7",
  "client_order_id": "ad4edbad-14dc-4323-ac71-03114945adfd",
  "created_at": "2024-08-19T11:36:10.751938789Z",
  "updated_at": "2024-08-19T11:36:10.763268199Z",
  "submitted_at": "2024-08-19T11:36:10.751938789Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": "4000",
  "qty": null,
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "stop_limit",
  "type": "stop_limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "34704",
  "stop_price": "33966",
  "status": "new",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.675635",
  "swap_fee_bps": "100",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": "27.0863",
    "filled_avg_price": null,
    "limit_price": "235",
    "stop_price": "230"
  }
}
```

```
{
  "id": "b964b06e-fd4f-4650-9658-e4997a8972d0",
  "client_order_id": "6d94f717-ea4d-4dc3-bdba-b9aee88b1639",
  "created_at": "2024-08-19T11:37:05.102784954Z",
  "updated_at": "2024-08-19T11:37:05.105484514Z",
  "submitted_at": "2024-08-19T11:37:05.102784954Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "symbol": "AAPL",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "1",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "",
  "order_type": "stop_limit",
  "type": "stop_limit",
  "side": "buy",
  "position_intent": "buy_to_open",
  "time_in_force": "day",
  "limit_price": "34700",
  "stop_price": "33961",
  "status": "accepted",
  "extended_hours": false,
  "legs": null,
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "commission": "0",
  "commission_type": "notional",
  "swap_rate": "147.655435",
  "swap_fee_bps": "100",
  "subtag": null,
  "source": null,
  "usd": {
    "notional": null,
    "filled_avg_price": null,
    "limit_price": "235",
    "stop_price": "230"
  }
}
```

# Get Account Position

The below position is the `AAPL` stock purchased previously with 4000 JPY.

JSON

```
[
  {
    "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
    "symbol": "AAPL",
    "exchange": "NASDAQ",
    "asset_class": "us_equity",
    "asset_marginable": true,
    "qty": "0.1199",
    "avg_entry_price": "33001.59760325",
    "side": "long",
    "market_value": "3957.039656317",
    "cost_basis": "3956.89155263",
    "unrealized_pl": "0.148103687",
    "unrealized_plpc": "0.0000374293015187",
    "unrealized_intraday_pl": "0.148103687325",
    "unrealized_intraday_plpc": "0.0000374293016008",
    "current_price": "33002.83283",
    "lastday_price": "33043.76295",
    "change_today": "-0.0012386640123866",
    "swap_rate": "146.179",
    "avg_entry_swap_rate": "146.1745",
    "usd": {
      "avg_entry_price": "225.7685",
      "market_value": "27.069823",
      "cost_basis": "27.0696431500022234",
      "unrealized_pl": "0.0010131666450037",
      "unrealized_plpc": "0.0000374293015187",
      "unrealized_intraday_pl": "0.001013166647227",
      "unrealized_intraday_plpc": "0.0000374293016008",
      "current_price": "225.77",
      "lastday_price": "226.05",
      "change_today": "-0.0000084736112053"
    },
    "qty_available": "0.1199"
  }
]
```

# Journaling Local Currency

Journalling in LCT is almost exactly the same as our regular Journals API.

In this example we will journal some JPY between two accounts.

JSON

```
{
  "from_account": "51461a2a-8f98-3aa5-ae51-fad8d03037b3",
  "entry_type": "JNLC",
  "to_account": "27529bc0-3ab5-34f5-ac29-54a98162472d",
  "amount": "3000",
  "currency": "JPY",
  "description": "Test JPY Journal"
}
```

and the response

JSON

```
{
    "id": "1717b9c7-f516-4e85-a21b-bbeb7ef7a87a",
    "entry_type": "JNLC",
    "from_account": "51461a2a-8f98-3aa5-ae51-fad8d03037b3",
    "to_account": "27529bc0-3ab5-34f5-ac29-54a98162472d",
    "symbol": "",
    "qty": null,
    "price": "0",
    "status": "queued",
    "settle_date": null,
    "system_date": null,
    "net_amount": "4000",
    "description": "Test JPY Journal",
    "currency": "JPY"
}
```

Updated 5 months ago

---

Ask AI

---

# Example Trading App (Ribbit) (https://docs.alpaca.markets/docs/example-trading-app-ribbit)

# Example Trading App (Ribbit)

# What is Ribbit?

Ribbit is a skeleton mobile app designed to showcase the capabilities of the Broker API. It’s a fully functional trading application that demonstrates how users would interact with your product. It uses all the different functionality that the Broker API offers including onboarding new users, funding an account, managing market data, and handling trade activity.

# User Experience Example

The screenshots below demonstrate how a native user would walk through Ribbit to accomplish various tasks.

## Create a New Account

Once Ribbit users sign up with their email and create a password, it triggers the brokerage account onboarding process to begin. The following screens prompt users to input their information such as name, date of birth, tax ID, and more information that is required by law to open a brokerage account. At the end of this process, Ribbit calls the [Accounts API](https://docs.alpaca.markets/docs/account-opening) to submit all the information to Alpaca where we verify the information and approve the account application.

The app demonstrates a common flow that brokerage apps have to implement to collect all the necessary data points and required user agreements. For your own app, you may also be interested in performing various input checks on the client side so that the account approval process is as quick as possible. See below screenshots of the actual flow.

Once the account creation flow is completed, Ribbit continues to use the Accounts API to retrieve real-time information about the user’s account. The API can also be used to update the account information as well as request to close an account.

![Beginning and end state of an account opening experience](https://files.readme.io/1c28843-image.png)

Beginning and end state of an account opening experience

## Fund an Account

The next step for the new users is to deposit the money to start trading. Ribbit uses [Plaid](https://www.plaid.com) to validate the bank information so that Alpaca can simply link the bank account to the brokerage account. From the Plaid Link component, Ribbit receives the bank routing number and account number for the user and submits the bank link request using [ACH Relationships](https://docs.alpaca.markets/reference/createachrelationshipforaccount).

As a demo app, Ribbit uses the Plaid sandbox which simulates the production environment behavior. When you try the app, use `user_good` and `pass_good` for the credentials with any banks shown in the app. Alpaca’s sandbox where Ribbit simulates the ACH transactions and the virtual money is credited in the user’s account in a moment.

Allowing your end users to connect to their personal bank and fund their account on your app can be intimidating if you aren’t familiar with the high level financial requirements and flows. Fortunately, our [Bank](https://docs.alpaca.markets/reference/createrecipientbank), [ACH Relationships](https://docs.alpaca.markets/reference/createachrelationshipforaccount), and [Transfers APIs](https://docs.alpaca.markets/reference/createfundingwalletwithdrawal) make it easy to achieve this! The Bank API lets you create, retrieve, and delete bank relationships between their personal bank and their account on your app. The ACH Relationships API deals with connecting, getting, and deleting your end user’s specific bank account that will be used to initiate and receive ACH transfers from your app. Finally, the Transfers API initiates, lists, and cancels the actual transfer initiated from your app on behalf of your end user. See how this flow is implemented from your user’s perspective below.

![Example of a funding flow using Plaid](https://files.readme.io/a37a6e7-image.png)

Example of a funding flow using Plaid

## View and Execute Trades

When it comes to managing stock market data, Alpaca provides seamless integration via the [Market Data API](https://docs.alpaca.markets/docs/about-market-data-api#broker-professional). Ribbit uses the historical data endpoint to draw the chart in the individual stock screen, and the real-time data endpoint to show the most up-to-date price information in the order screen. See how Ribbit makes use of the Market Data API below.

![Typical screens for trading and portfolio](https://files.readme.io/acf4740-image.png)

Typical screens for trading and portfolio

In the order screen, Ribbit uses the Orders API. It allows you to submit a new order, replace/cancel an open order, and retrieve a list of orders from a user’s history. Ribbit connects to Alpaca’s sandbox environment where an order execution simulator engine runs. This simulator will take the order you submitted on the backend and execute it using the real-time market price which makes it easy to test trading functionality before you launch your app to users.

Ribbit shows all the account activities using the Activities API which returns the relevant transaction history for a given account. As a trading app, some of the important requirements to deliver to your users are monthly statements and trade confirmations. Ribbit accomplishes this by using the Documents API. The documents are generated in PDF format by Alpaca so all you need to do is call the API to retrieve the list of downloadable URLs and show them in the app.

# Architecture

The end user interacts with Ribbit’s UI to achieve a task while Ribbit’s backend processes the requests by making calls to Broker API. See the diagram below for an example of how the account creation process works.

![](https://files.readme.io/cdbd289-image.png)

The backend application serves as a thin layer to proxy the API requests coming from the mobile app but makes sure each request is authorized for the appropriate user.

# Technology

The user interface is written in Swift for iOS and Java for Android. The backend is implemented using Go.

## Alpaca APIs

All of the technology that is needed for users to interact with Ribbit’s core functionality is acheived through the Broker API. Accessing information related to the market is gathered using the Market Data API.

> 📘
>
> ### Where Can I Access the Source Code?
>
> The codebase is hosted on GitHub and separated into three different repositories for the implementation of the [backend](https://github.com/alpacahq/ribbit-backend), [iOS user interface](https://github.com/alpacahq/ribbit-ios), and [Android user interface](https://github.com/alpacahq/ribbit-android).

Updated 5 months ago

---

Ask AI

---

# Options Trading Overview (https://docs.alpaca.markets/docs/options-trading-overview)

# Options Trading Overview

# Initial Options Offering

## Supported

* US listed equities options, all american style
* Level 1-3 options trading
* Fully Disclosed partner relationships
* Automatic account approval process via the API along with SSE events
* Ability for partners to downgrade/disable options trading
* Ability to exercise options via the API
* DNE (do not exercise) via API
* New options specific activities
* Access to options market data (at a cost) or referral to market data partner

## Not supported

* LCT (local currency trading)
* Fractional options
* Extended hours

# Options Enablement

## Enabling Options Trading on a new Account

Per FINRA Rule 2360, each customer account has to be approved for options before the first options trade is made. Once options trading is enabled on a correspondent you can start requesting accounts to be approved for options trading. For existing accounts there will be a few new data points that need to be [patched](https://docs.alpaca.markets/v1.1/reference/patchaccount-1) on the account along with a new options agreement that the customer will need to sign. Below are the new fields that will need to be provided specifically for options.

* Annual Income
* Net Worth
* Liquid Net Worth
* Liquidity Needs
* Investment Experience
* Investment Risk Tolerance
* Investment Objective
* Investment Time Horizon
* Marital Status
* Number of Dependents

Below is an example of a request for opening a new account with options enabled. More details on creating an account can be found [here](https://docs.alpaca.markets/v1.1/reference/createaccount-1)**.**

JSON

```
{
    "enabled_assets": [
        "us_equity",
        "crypto",
        "us_option"
    ],
    "contact": {
        "email_address": "[email protected]",
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
                "company_compliance_email": "[email protected]"
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
        "email_address": "[email protected]"
    }
}
```

## Enabling Options Trading on an existing Account

Below are sample requests and responses for enabling options trading on an existing account, using the approval [endpoint](https://docs.alpaca.markets/reference/requestoptionsforaccount).

Example: Account with level 1 requirements requesting for level 1 options trading approval

Request

```
{
  "level": 1   
}
```

Response

```
{
    "id": "43c2f8a9-9e39-48b1-921c-e510dfeeff47",
    "account_id": "492b6297-45fc-4435-abc7-08ab15480b1c",
    "created_at": "2024-05-14T04:34:03.527165162-04:00",
    "updated_at": "2024-05-14T04:34:03.527165162-04:00",
    "requested_level": 1,
    "status": "APPROVED"
}
```

Example: Account with level 1 requirements requesting for level 2 options trading approval

Request

```
{
  "level": 2   
}
```

Response

```
{
    "id": "43c2f8a9-9e39-48b1-921c-e510dfeeff47",
    "account_id": "492b6297-45fc-4435-abc7-08ab15480b1c",
    "created_at": "2024-05-14T04:34:03.527165162-04:00",
    "updated_at": "2024-05-14T04:34:03.527165162-04:00",
    "requested_level": 2,
    "status": "LOWER_LEVEL_APPROVED"
}
```

### Options Approval Statuses

| Status | Description |
| --- | --- |
| `APPROVED` | User has been approved for requested options trading level. |
| `LOWER_LEVEL_APPROVED` | User has been approved for a lower level than the requested options trading level. |
| `PENDING` | Pending manual review |
| `REJECTED` | User has been rejected for requested options trading level. |

### Approval fixtures

Options Approval API supports approval fixtures in the Sandbox environment. You can pass the desired approval level and approval status to test all different scenario of options approval flow (approved, lower\_level\_approved, rejected) to the same approval [endpoint](https://docs.alpaca.markets/reference/requestoptionsforaccount).

Example use cases:

1. Requesting an `APPROVED` status for options trading level 1

JSON

```
{
  "level": 1,   
  "fixtures": {
    "status":"APPROVED"
  }
}
```

2. Requesting an `REJECTED` status for options trading level 2

JSON

```
{
  "level": 2,   
  "fixtures": {
    "status":"REJECTED"
  }
}
```

3. Requesting a `LOWER_LEVEL_APPROVED` status (simulating a flow where level 2 was requested but user is approved for level 2 instead)

JSON

```
{
  "level": 2,   
  "fixtures": {
    "status":"LOWER_LEVEL_APPROVED",
    "level":1
  }
}
```

## Downgrading/disabling Options

Once an account is approved for options trading the customer has the ability to downgrade the options level or disable it altogether. This is done by setting the max\_options\_trading\_level via the trading account configuration [endpoint.](https://docs.alpaca.markets/v1.1/reference/patch-patch-v1-trading-accounts-account_id-account-configurations-1)

Once the max options trading level is set the options trading level on the trading account endpoint will get upgraded to the value set by the user. Note the options trading level will always be the same or lower than the options approved level. Below is an example of a user being approved for level 2 but downgrading to level 1.

JSON

```
{
  ...
  "options_approved_level": 2,
  "options_trading_level": 1,
  ...
}
```

# Trading

## Trading Overview

When placing orders via the [orders api](https://docs.alpaca.markets/v1.1/reference/createorderforaccount-1) for options below is what is supported and what is not supported

### Supported

* Options symbol
* Time in force of day
* Market and limit order types
* Ability to replace and cancel orders
* Level 1 + 2 option strategies

### Not supported

* Extended hours
* Fractional or notional order support

## Trading Levels

Alpaca supports the below options trading levels.

| Level | Supported Trades | Validation |
| --- | --- | --- |
| 0 | * Options trading is disabled | * NA |
| 1 | * Sell a covered call * Sell cash-secured put | * User must own sufficient underlying shares * User must have sufficient options buying power |
| 2 | * Level 1 * Buy a call * Buy a put | * User must have sufficient options buying power |

### Trading Level Validation

If a user tries to trade a strategy above their level this will result in an error message. Below is an example of a user who is approved for level 1 trying to place a level 2 options trade.

JSON

```
{
   "code": 40310000,
   "message": "account not eligible for level2 options trading"
}
```

## Asset Master

Similar to the asset master for securities and crypto there is an options contract [endpoint](https://docs.alpaca.markets/v1.1/reference/get-options-contracts-1) which will return all the options contract for an underlying symbol. Below is a sample

JSON

```
{
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
 }
```

## Order Examples

**Buying a call**

JSON

```
{  
  "symbol": "PTON240126C00000500",  
  "qty": "1",  
  "side":"buy",  
  "type": "market",  
  "time_in_force": "day"  
}
```

**Buying a put**

JSON

```
{  
  "symbol": "TSLA240126P00210000",  
  "qty": "1",  
  "side": "buy",  
  "type": "market",  
  "time_in_force": "day"  
}
```

**Selling a covered call**

JSON

```
{  
  "symbol": "AAPL240126C00050000", 
  "qty": "1", 
  "side": "sell", 
  "type": "market", 
  "time_in_force": "day"  
}
```

**Selling a cash secured put**

JSON

```
{  
  "symbol": "QS240126P00006500",  
  "qty": "1",  
  "side": "sell",  
  "type": "market",  
  "time_in_force": "day"  
}
```

## Buying Power Checks

With options we introduce a new field on the [trading account endpoint](https://docs.alpaca.markets/v1.1/reference/gettradingaccount-1) called options\_buying\_power which is evaluated when trying to open new options positions.

For both **buying a call** or **buying a put** sufficient buying power is necessary to pay for the premium of the contract otherwise an error will occur as shown below.

JSON

```
{
"options_buying_power": "7267.84",
"code": 40310000,
"cost_basis": "38000",
"message": "insufficient options buying power"
}
```

For **Selling Covered Call** you need to have enough stocks as collateral otherwise the order will error out as shown below.

JSON

```
 {
   "available_qty": "0",
   "code": 40310000,
   "message": "insufficient underlying qty available for covered call (required: 100, available: 0)",
   "required_qty": "100",
   "symbol": "AAPL240126C00050000",
   "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415"
}
```

For **selling cash secured put** you will need enough buying power to pay for the underlying stock minus the premium that would be received otherwise the order will error out as shown below

JSON

```
{
  "buying_power": "9395",
  "code": 40310000,
  "message": "insufficient options buying power for cash-secured put (required: 20310, available: 9395)",
  "required_options_buying_power": "20310"
}
```

# Positions

Option positions will show up like any other position in the positions endpoint. Below is an example of an options position.

JSON

```
{
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
}
```

# Post Trade

## Exercising

As the buyer of an option (call or put), the holder has the right, but not the obligation, to buy or sell the option's underlying security at a specified price on or before a specified date in the future. If the holder decides to act on those rights they are choosing to exercise. An option can be exercised via the exercise [endpoint](https://docs.alpaca.markets/v1.1/reference/optionexercise-1) and instructions for DNE (do not exercise) instructions can be supplied via [Do not exercise](https://docs.alpaca.markets/reference/optiondonotexercise-1) endpoint. Note exercise requests will be processed instantly and requests sent outside of market hours will be rejected. When exercising there will be 2 new activities per exercise which are:

* **OPEXC** - removes the options position as a result of exercising
* **OPTRD** - trading activity that is paired with the exercising

### Exercising Call

A long call exercise results in **buying the underlying stock** at the strike price. Below is an example of this.

JSON

```
{
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
}
```

### Exercising Put

A long put exercise results in **selling the underlying stock** at the strike price. Below is an example of this.

JSON

```
{
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
```

## Assignment

When selling an options contract (call or put) the user collects a premium but in turn takes on the obligation to buy or sell the stock at the agreed upon strike price if assigned. It is important to note that the OCC assigns a random account and sellers of contracts can be assigned overnight. When assigned there will be 2 new activities per assignment which are:

* **OPASN** - removes the options position as a result of assignment
* **OPTRD** - trading activity that is paired with the assignment

### Call Assignment

For call options, the seller takes on the **obligation to sell** the stock at the agreed upon strike price. Below is an example of activities that result as a result of a call assignment

JSON

```
 {
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
}
```

### Put Assignment

For put options, the seller takes on the **obligation to buy** the stock at the agreed upon strike price. Below is an example of activities that result as a result of a put assignment

JSON

```
{
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
}
```

## Expiration

Unlike stocks, option contracts have an expiration date. If the user does not close out their position or exercise their options (if they have the buying power to support the exercise), Alpaca will need to potentially take action on it for risk management purposes based on the criteria described below.

* Starting at 3:30 pm EST on the date of expiration, Alpaca continuously evaluates any open positions that expire that day and stops accepting new orders to open/extend any positions.
* If the position for a long call or put **is ITM (in the money)** by .01 or more, Alpaca checks if the account has enough buying power to exercise in the case of a call or enough shares in the case of a put
  + If there is **enough buying power or shares** Alpaca will not liquidate the options and will let the option auto-exercise.
  + If there is **not enough buying power or shares**, then Alpaca will liquidate while it’s still ITM
* If the position **is for a covered call or cash secured put and ITM** by .01 or more **Alpaca will automatically assign after close on date of expiry**
* If the position **is not ITM** in other words it’s **ATM (at the money)** or **OTM (out of the money)**, Alpaca may skip it and it will expire after close as shown in the examples below. (Note that positions slightly OTM may also be liquidated depending on market and underlying conditions. Alpaca will take into consideration fast moving markets and/or fast stocks that may be moving from ITM and OTM throughout the day. There may be instances where OTM positions are also closed out.)

### Call Expiration

JSON

```
{
  "id": "20240301000000000::31ff5d4c-a608-43bb-8e59-678a96a4a42c",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXP",
  "date": "2024-03-01",
  "net_amount": "0",
  "description": "Option Expiry",
  "symbol": "QS240301C00010500",
  "qty": "-1",
  "status": "executed"
}
```

### Put Expiration

JSON

```
{
  "id": "20240301000000000::4bd8c683-0b2c-489f-9df9-1243ff621648",
  "account_id": "21c36b57-2304-4e5b-8364-8effbcba853e",
  "activity_type": "OPEXP",
  "date": "2024-03-01",
  "net_amount": "0",
  "description": "Option Expiry",
  "symbol": "QS240301P00000500",
  "qty": "-1",
  "status": "executed"
}
```

# Market Data

Alpaca provides access to options market data (at a cost) in the same user-friendly format it does for stocks and crypto. Additionally, we can refer partners to external data vendors with whom Alpaca has a close relationship if necessary.

| Endpoint | Noteste |
| --- | --- |
| [Latest Quotes](https://docs.alpaca.markets/v1.1/reference/optionlatestquotes) | Latest quotes. Supports multiple symbols |
| [Latest Trades](https://docs.alpaca.markets/v1.1/reference/optionlatesttrades) | Latest trades. Supports multiple symbols |
| [Historical Trades](https://docs.alpaca.markets/v1.1/reference/optiontrades) | Historical trades. Supports multiple symbols |
| [Snapshots](https://docs.alpaca.markets/v1.1/reference/optionsnapshots) | Combine quotes and trades for multiple symbols |
| [Option chain](https://docs.alpaca.markets/reference/optionchain) | Query option chain by the underlying (stock) symbols |
| [Historical bars](https://docs.alpaca.markets/v1.1/reference/optionbars) | Historical bars.Supports multiple symbol |

Options trading is not suitable for all investors due to its inherent high risk, which can potentially result in significant losses. Please read [Characteristics and Risks of Standardized Options](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document) before investing in options.

Updated 18 days ago

---

Ask AI

---

# Fixed Income (https://docs.alpaca.markets/docs/fixed-income-1)

# Fixed Income

This guide provides a comprehensive reference for integrating U.S. Treasuries and U.S. Corporate Bonds into your platform.

## Overview of Fixed Income Products

Alpaca offers Broker API partners access to a growing range of fixed income securities. These products provide a way for end-users to diversify their portfolios with debt instruments.

### Product Categories

* U.S. Treasuries: Sovereign debt securities issued by the U.S. government. We currently support Treasury Bills (T-Bills) and will be expanding to include Treasury Notes (T-Notes) and Treasury Bonds (T-Bonds).
* U.S. Corporate Bonds: Debt securities issued by U.S. corporations. We support a variety of investment-grade, and high-yield bonds.

### Key Features

* API-Driven Trading: All trading and data retrieval is executed via the Broker API.
* Best-Price Execution: Alpaca aggregates quotes from multiple liquidity providers to ensure competitive pricing during U.S. bond market hours.
* Broad Access: Available to all Broker API partners and their end-users.
* Full Denominations: Securities are traded in full denominations, typically in increments of $1,000 face value. Fractional trading is planned for a future release.

---

## Trading and Orders

The core mechanics of placing and managing orders are consistent across all fixed income products.

### Market Hours

* Regular Hours: 9:30 AM - 4:00 PM ET.
* Pre-Market and After-Hours Queue: Orders submitted between 4.00 PM - 9:30 AM ET (next day) are queued and sent for execution at the market open. For weekends, orders submitted between 4.00 PM on Friday until 9.30 AM ET Monday will be queued and executed on Monday when the market opens.

### Order Management

* Placing Orders: All orders are submitted via the API. Currently, market and limit orders with a day time-in-force are supported.
* Order Queuing: Orders placed outside of market hours are given an accepted status and are executed when the market reopens.
* Cancellations:
  + During Market Hours: Cancellation requests are sent to the execution venue immediately.
  + Outside Market Hours: Orders with an accepted status are cancelled immediately. Orders already sent to a venue will become pending\_cancel until the market reopens.

### Order Size

* Minimum Order Size: $1,000 face value.
* Maximum Order Size: $1,000,000 face value.

### Pricing, Markups, and Fees

* Clean Price: Prices are quoted as a percentage of the bond's par value (face value). This is the "clean price" and does not include accrued interest. The final settlement amount will include any accrued interest for coupon-bearing bonds.
* Markups: Markups from Alpaca and/or partners are included in the final execution price.
* Regulatory Fees: Sales of U.S. Treasuries are reportable to the Trade Reporting and Compliance Engine (TRACE) and incur a small regulatory fee.

---

## U.S. Treasuries API Reference

U.S. Treasury Bills (T-Bills) are short-term government debt securities with maturities of one year or less. They are issued at a discount and redeemed at face value at maturity, with no periodic coupon payments.

### List U.S. Treasuries

Retrieve a list of available U.S. Treasury securities.

* Endpoint: GET /v1/assets/fixed\_income/us\_treasuries
* Sandbox URL: <https://broker-api.sandbox.alpaca.markets/v1/assets/fixed_income/us_treasuries>
* Production URL: <https://broker-api.alpaca.markets/v1/assets/fixed_income/us_treasuries>

Query Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| subtype | string | (Optional) Filter by type: bill, note, bond, strips, tips, floating. |
| bond\_status | string | (Optional) Filter by status: outstanding, matured, pre\_issuance. |
| cusips | string | (Optional) Comma-separated list of up to 1000 CUSIPs. |
| isins | string | (Optional) Comma-separated list of up to 1000 ISINs. |

Sample Response:

JSON

```
{
  "us_treasuries": [
    {
      "cusip": "912797MU8",
      "isin": "US912797MU86",
      "bond_status": "outstanding",
      "tradable": true,
      "subtype": "bill",
      "issue_date": "2025-02-13",
      "maturity_date": "2025-03-27",
      "description": "United States Treasury 0.0%, 03/27/2025",
      "description_short": "UST 0.0% 03/27/2025",
      "close_price": 99.6839,
      "close_price_date": "2025-02-27",
      "close_yield_to_maturity": 4.214,
      "close_yield_to_worst": 4.214,
      "coupon": 0,
      "coupon_type": "zero",
      "coupon_frequency": "zero"
    }
  ]
}
```

### Get Latest Prices

Retrieve the latest real-time prices for specified U.S. Treasuries.

* Endpoint: GET /v1/assets/fixed\_income/us\_treasuries/prices

Query Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| isins | string | (Required) Comma-separated list of up to 1000 ISINs. |

Sample Response:

JSON

```
{
  "prices": {
    "US912797KJ59": {
      "t": "2025-02-14T20:58:00.648Z",
      "p": 99.6459,
      "ytm": 4.249,
      "ytw": 4.249
    },
    "US912797KS58": {
      "t": "2025-02-14T20:58:00.648Z",
      "p": 99.3193,
      "ytm": 4.2245,
      "ytw": 4.2245
    }
  }
}
```

---

## U.S. Corporate Bonds API Reference

Corporate bonds are debt instruments issued by corporations. They typically pay periodic interest (coupons) and repay the principal at maturity. Alpaca currently supports non-puttable, non-reg-s, non-144a corporate bonds, but work is in progress to add more soon.

### List U.S. Corporate Bonds

Retrieve a list of available U.S. Corporate Bonds.

* Endpoint: GET /v1/assets/fixed\_income/us\_corporates
* Sandbox URL: <https://broker-api.sandbox.alpaca.markets/v1/assets/fixed_income/us_corporates>
* Production URL: <https://broker-api.alpaca.markets/v1/assets/fixed_income/us_corporates>

Query Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| bond\_status | string | (Optional) Filter by status: outstanding, matured, pre\_issuance. |
| cusips | string | (Optional) Comma-separated list of up to 1000 CUSIPs. |
| isins | string | (Optional) Comma-separated list of up to 1000 ISINs. |
| ticker | string | (Optional) Comma-separated list of up to 1000 issuer stock tickers. |

Sample Response:

JSON

```
{
  "us_corporates": [
    {
      "cusip": "00138CAU2",
      "isin": "US00138CAU27",
      "bond_status": "outstanding",
      "tradable": true,
      "ticker": "AIG",
      "issue_date": "2023-07-03",
      "maturity_date": "2026-07-02",
      "issuer": "Corebridge Global Funding",
      "description": "Corebridge Global Funding 5.75%, 07/02/2026",
      "coupon": 5.75,
      "coupon_type": "fixed",
      "coupon_frequency": "semi_annual",
      "close_price": 101.2792,
      "close_price_date": "2025-08-13",
      "close_yield_to_maturity": 4.252774,
      "close_yield_to_worst": 4.252774
    }
  ]
}
```

### Get Latest Prices

This endpoint is the same as for Treasuries and can be used to query prices for corporate bonds using their ISINs.

---

## Common Trading Endpoints

These endpoints are used for trading and managing positions for both U.S. Treasuries and Corporate Bonds.

### Create an Order

* Endpoint: POST /v1/accounts/`{account_id}`/orders

Path Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| account\_id | string | (Required) The account ID to place the order for. |

Body Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| symbol | string | (Required) The security identifier (CUSIP or ISIN). |
| qty | string | (Required) The face value (par value) of the bond to trade. |
| side | string | (Required) buy or sell. |
| type | string | (Required) Must be market. |
| time\_in\_force | string | (Required) Must be day. |

Sample Request (Treasury):

JSON

```
{
  "symbol": "912797MU8",
  "qty": "1000",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

Sample Request (Corporate Bond):

JSON

```
{
  "symbol": "06050WFN0",
  "qty": "1000",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

Sample Response (Order Confirmation):

JSON

```
{
  "id": "7b08df51-c1ac-453c-99f9-323a5f075f0d",
  "client_order_id": "5680c4bc-9ac1-4a12-a44c-df427ba53032",
  "created_at": "2025-03-26T14:13:02.790553657Z",
  "symbol": "912797MU8",
  "asset_class": "treasury", // Will be "corporate" for corporate bonds
  "qty": "1000",
  "filled_qty": "0",
  "type": "market",
  "side": "buy",
  "time_in_force": "day",
  "status": "pending_new",
  ...
}
```

### List Open Positions

* Endpoint: GET /v1/accounts/`{account_id}`/positions

Sample Response (Treasury Position):

JSON

```
[
  {
    "asset_id": "904837e3-3b76-47ec-b432-046db621571b",
    "symbol": "912797MU8",
    "asset_class": "treasury",
    "avg_entry_price": "98.0",
    "qty": "2000",
    "market_value": "1980.0",
    "cost_basis": "1960.0",
    "current_price": "99.0"
  }
]
```

### Trade Events (Server-Sent Events)

Receive real-time updates on the status of orders, including fills. Refer to the [guide on the order life cycle](https://docs.alpaca.markets/docs/orders-at-alpaca#order-lifecycle) for more details on event statuses.

Sample Response (Filled Order):

JSON

```
{
  "account_id": "529248ad-c4cc-4a50-bea4-6bfd2953f83a",
  "at": "2022-04-19T14:12:30.656741Z",
  "event": "fill",
  "order": {
    "id": "edada91a-8b55-4916-a153-8c7a9817e708",
    "symbol": "912797MU8",
    "asset_class": "treasury",
    "side": "buy",
    "status": "filled",
    "filled_qty": "1000",
    "filled_avg_price": "98.72",
    "filled_at": "2022-04-19T10:12:30.609783218-04:00"
    ...
  }
}
```

---

## Custody, Settlement, and Compliance

### Security Identifiers

We support both CUSIP (9-character) and ISIN (12-character) identifiers for all fixed income securities.

### Tradability

To determine if a bond is available for trading, check the tradable boolean field in the asset object returned from the /assets endpoints. If true, the security can be traded.

### Custody

* U.S. Treasuries: Custodied with our partner, BMO.
* Corporate Bonds: Self-custodied by Alpaca at the Depository Trust Company (DTC), similar to equities.

### Settlement Cycle

* U.S. T-Bills: Settle on a T+1 basis (trade date + 1 business day).
* Corporate Bonds: Settle on a T+2 basis (trade date + 2 business days).

### Compliance

* End-Users: No additional suitability assessments or agreements are required.
* Partners: A technical sign-off is needed before enabling fixed income products in a production environment.
* Confirmations: All trade confirmations and statements comply with SEC Rule 10b-10.

*The content of this presentation is for general information only and is believed to be accurate as of posting date but may be subject to change.*

*Fixed income securities can experience a greater risk of principal loss when interest rates rise. These investments are also subject to additional risks, including credit quality fluctuations, market volatility, liquidity constraints, prepayment or early redemption, corporate actions, tax implications, and other influencing factors.*

*All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.*

*Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.*

*This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered or licensed, as applicable.*

Updated about 1 month ago

---

Ask AI

---

# Tokenization Guide for Issuer (https://docs.alpaca.markets/docs/tokenization-guide-for-issuer)

# Tokenization Guide for Issuer

Instant Tokenization Network (ITN) is a platform designed to streamline and accelerate the process of in-kind mint and redemption of tokenized assets. The goal of ITN is to enable efficient, secure, and rapid conversion of real-world and digital assets to and from various tokens issued by partners on the network. The network acts as instant settlement rails for market participants to programmatically rebalance inventory, thereby stitching together fragmented tokenized asset liquidity across the industry. This document will guide the **Issuer** of tokenized assets on how to start using Alpaca’s Instant Tokenization Network.

# Overview

Before you start integrating into Alpaca's ITN (Instant Tokenization Network) as an issuer of tokenized assets, you would need to:

* Complete your integration into Alpaca's Broker API offering.
* Have an account in your name at Alpaca.

If you have not done so yet, please make sure to reach out to Alpaca sales to initiate the conversation.

If you have already done so, the below document will guide you to integrate into ITN. This will be achieved by:

* Implementing 4 endpoints on your platform that Alpaca will utilize to process account linking & token minting.
  + [Account Linking](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#issuers-account-linking-endpoint)
  + [Tokenized Assets](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#tokenized-assets-data)
  + [Mint Request](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#issuers-mint-request-endpoint)
  + [Mint Confirmation](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#issuer-mint-journal-confirmation-endpoint)
* Integrating with 2 Alpaca endpoints that you will utilize to complete token minting and redemption flows.
  + [Mint Confirmation Callback](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#alpacas-mint-confirmation-callback-endpoint)
  + [Redeem Request](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#alpacas-redeem-request-endpoint)

## Important Prerequisite

During the mint and redeem process, Instant Tokenization Network will journal securities to/from the AP's Alpaca account to/from the Issuer's Alpaca account. If you, as an issuer, hold multiple accounts at Alpaca, please ensure to inform Alpaca which of your accounts should be designated for tokenization.

# Handshake Process

Before an entity can mint or redeem your tokenized assets through ITN, they will need to reach out to Alpaca’s operation team for a "handshake" step through which Alpaca will need to verify that the entity is:

* An existing client of Alpaca.
* An existing client of your firm and registered as an authorized participant (AP) on your platform.

To automate this process, you will need to provide an account linking endpoint that Alpaca can utilize to link an AP’s account at Alpaca to their account on your platform. Alpaca will maintain this linking and use it during the mint and redeem processes.

#### Issuer’s Account Linking Endpoint

Alpaca will invoke your account linking endpoint by providing the AP's email and their Alpaca account number. Your endpoint should respond with the AP’s account number on your platform that Alpaca will store for future use during the mint and redeem flow:

**Expected Request**

**Endpoint**

HTML

```
POST /tokenization/accounts/connect
```

**Body**

JSON

```
{
  "email": "[email protected]",
  "account" : "alpaca_account_number"
}
```

| Field | Description |
| --- | --- |
| email | AP’s email used on the Issuer’s platform |
| account | AP's Alpaca account number |

**Expected Response**

**Body**

JSON

```
{
  "client_id": "5505-1234-ABC-4G45"
}
```

| Field | Description |
| --- | --- |
| client\_id | AP’s account identifier on the Issuer’s platform |

**Status Codes**

| Status | Description |
| --- | --- |
| 200 | OK - Successful link |
| 404 | Email not found |
| 409 | Account already linked |

# Tokenized Assets Data

You will need to provide Alpaca an endpoint that can be used to retrieve the list of supported tokenized assets on your issuer platform. The endpoint should provide the following data:

* underlying symbol
* token symbol
* supported blockchain networks

**Expected Request**

**Endpoint**

HTML

```
GET /tokenization/tokens
```

**Expected Response**

**Body**

JSON

```
{
  "tokens": [
    {
	"underlying": "AAPL",
	"token": "tAAPL",	
	"networks": ["solana", "ethereum"]
    },
    {
	"underlying": "TSLA",
  	"token": "tTSLA",
	"networks": ["solana", "ethereum"]
   }
  ]
}
```

| Field | Description |
| --- | --- |
| tokens | List of supported tokens |
| underlying | Underlying asset symbol |
| token | Token asset symbol |
| networks | List of supported networks |

Alpaca will use this information when validating an AP's mint request.

# Mint Endpoint and Workflow

The token minting flow has multiple steps that begin when an AP requests token minting from Alpaca. The steps are explained below & depicted in Figure 1 to help you visualize, and all endpoints mentioned are documented below as well.

1. The Authorized Participant sends Alpaca a mint request.
2. Alpaca invokes [an endpoint on your platform to submit a mint request](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#issuers-mint-request-endpoint), with a JSON object in the body. Your platform will need to validate the mint request.
3. Alpaca journals the underlying security from the AP’s account into your Alpaca account.
4. Alpaca invokes [another endpoint on your platform to confirm the underlying asset's journal status](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#issuer-mint-journal-confirmation-endpoint).
5. Your platform deposits the tokens into the AP’s wallet on a successful journal.
6. Your platform invokes [Alpaca’s endpoint to confirm the successful token mint](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#alpacas-mint-confirmation-callback-endpoint), providing the designated Alpaca tokenization account\_id as a URL parameter in the endpoint.

![](https://files.readme.io/3f7824e1f515ce0e46b759d7a4f4052cc4e5a0c736e2b33a3671b251c0c162b5-Minting_Redeeming2x.png)

Figure 1. Minting a tokenized asset

## Endpoints you need to provide

#### Issuer’s Mint Request Endpoint

This endpoint will be invoked by Alpaca at step 2.

**Expected Request**

**Endpoint**

HTML

```
POST /tokenization/mint
```

**Body**

JSON

```
{
  "id": "12345-678-90AB",
  "qty": "1.23",
  "underlying_symbol": "TSLA",
  "token_symbol": "TSLAx",
  "network": "solana",
  "client_id": "98765432",
  "wallet_address": "<AP's wallet address to deposit the tokenized asset>"
}
```

| Field | Description |
| --- | --- |
| id | Unique request identifier assigned by Alpaca |
| qty | The underlying quantity to convert into the tokenized asset. The value can be fractional. |
| underlying\_symbol | Underlying asset symbol |
| token\_symbol | Tokenized asset symbol |
| network | The token’s blockchain network. Currently, we support the following networks:   * solana * base |
| client\_id | AP’s account identifier on the Issuer's platform. This is the account identifier received during the handshake/account linking step. |
| wallet\_address | The destination wallet address where the tokenized assets should be deposited |

**Expected Response**

**Body**

JSON

```
{
  "issuer_request_id": "123-456-ABCD-7890",
  "status": "created"
}
```

| Field | Description |
| --- | --- |
| issuer\_request\_id | Unique identifier assigned by the Issuer |
| status | Tokenization request status. Once the request has been successfully validated, the Issuer will create a mint tokenization request on their platform. This does not mean that the token is created.   * created |

**Status Codes**

| Status | Description |
| --- | --- |
| 200 | OK |
| 400 | * Invalid Wallet: Wallet does not belong to client * Invalid Token: Token not available on the network * Insufficient Eligibility: Client not eligible * Failed Validation: Invalid data payload |

#### Issuer Mint Journal Confirmation Endpoint

This endpoint will be invoked by Alpaca at step 4.

**Expected Request**

**Endpoint**

HTML

```
/tokenization/mint/confirm
```

**Body**

JSON

```
{
  "id": "12345-678-90AB",
  "issuer_request_id": "ABC-123-DEF-456",
  "status": "<completed/rejected>"
}
```

| Field | Description |
| --- | --- |
| id | Unique request identifier previously assigned by Alpaca |
| issuer\_request\_id | Unique identifier assigned by the Issuer as previously received on the mint response |
| status | The journal status. Valid values are:   * rejected * completed |

**Expected Response**

**Expected Status Codes**

| Status | Description |
| --- | --- |
| 200 | OK |

  

## Endpoints you need to integrate with

#### Alpaca's Mint Confirmation Callback Endpoint

This endpoint will be invoked by your platform at step 6.

**Request**

**Endpoint**

HTML

```
POST /v1/accounts/:account_id/tokenization/callback/mint
```

**Body**

JSON

```
{
  "id": "12345-678-90AB",
  "client_id": "5505-1234-ABC-4G45",
  "wallet_address": "<AP's wallet address where the tokenized assets were deposited>",
  "tx_hash": "0x12345678",
  "network": "solana"
}
```

| Field | Description |
| --- | --- |
| id | Unique request identifier previously assigned by Alpaca |
| client\_id | AP’s account identifier on the Issuer's platform |
| wallet\_address | Wallet address where the tokenized assets were deposited |
| tx\_hash | Mint’s transaction hash on the blockchain |
| network | The token’s blockchain network. Currently, we support the following networks:   * solana * base |

**Response**

**Status Codes**

| Status | Description |
| --- | --- |
| 200 | OK |
| 400 | Internal failure while processing the mint confirmation |

  

# Redeem Endpoint and Workflow

The token redeem flow has multiple steps that begin when an AP deposits token into a redemption wallet address that you provide them with. The steps are explained below & depicted in Figure 2 to help you visualize, and all endpoints mentioned are documented below as well.

1. The token redemption process will be initiated by an end client by moving tokens into the a redemption wallet address provided by you as an Issuer, at which point these tokens should be removed from circulation.
2. Your platform should then notify Alpaca that an AP has redeemed their tokens by invoking [an endpoint](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#alpacas-redeem-request-endpoint). Your platform should provide their designated Alpaca tokenization account\_id as a URL parameter in the endpoint.
3. Alpaca will journal the underlying asset from your Alpaca account as an issuer, into the AP’s Alpaca account.

![](https://files.readme.io/661cc0f3b3881fcdf4d87de2ca7866efe56bea8f8e250965836952699552ea5f-Minting_Redeeming2x_2.png)

Figure 2. Redeeming a tokenized asset

## Endpoint you need to integrate with

#### Alpaca's Redeem Request Endpoint

This endpoint will be invoked by your platform at step 2.

**Request**

**Endpoint**

HTML

```
POST /v1/accounts/:account_id/tokenization/redeem
```

**Body**

JSON

```
{
  "issuer_request_id": "ABC-123-DEF-456",
  "underlying_symbol": "AAPL",
  "token_symbol": "AAPLx",
  "client_id": "5505-1234-ABC-4G45",
  "qty": "1.23",
  "network": "solana",
  "wallet_address": "<the originating wallet address for the redeemed tokens>",
  "tx_hash": "0x12345678"
}
```

| Field | Description |
| --- | --- |
| issuer\_request\_id | Unique identifier assigned by the Issuer |
| underlying\_symbol | Underlying asset symbol |
| token\_symbol | Token asset symbol |
| client\_id | AP’s account identifier on the Issuer's platform |
| qty | The quantity to convert into the underlying asset. The value can be fractional. |
| network | The originating token’s blockchain network. Currently, we support the following networks:   * solana * base |
| wallet\_address | The address where the redeemed tokens were originally held |
| tx\_hash | The transaction hash of the tokens being sent to the Issuer's redemption wallet |

**Response**

**Body**

JSON

```
{
  "id": "12345-678-90AB",
  "issuer_request_id": "ABCDEF123",
  "created_at":"2025-09-12T17:28:48.642437-04:00",
  "type": "redeem",
  "status": "completed",
  "underlying_symbol": "TSLA",
  "token_symbol" : "TSLAx",
  "qty" : "123.45",
  "issuer" : "xstocks",
  "network": "solana",
  "wallet_address": "0x1234567A",
  "tx_hash" : "0x1234567A",
  "fees" : "0.567"
}
```

| Field | Description |
| --- | --- |
| id | Unique request identifier assigned by Alpaca |
| issuer\_request\_id | Unique identifier assigned by the Issuer |
| created\_at | Timestamp when Alpaca received the redeem request |
| type | Tokenization request type:   * redeem |
| status | Current status of the redemption request:   * pending * completed * rejected |
| underlying\_symbol | The underlying asset symbol |
| token\_symbol | The tokenized asset symbol |
| qty | The quantity to convert into the underlying asset. It can be fractional. |
| issuer | The tokenized asset's Issuer. Valid values are:   * xstocks * st0x |
| network | The token's blockchain network. Valid values are:   * solana * base |
| wallet\_address | The originating wallet where the tokenized assets were previously held |
| tx\_hash | The transaction hash of the tokens being sent to the Issuer's redemption wallet |
| fees | The fees charged for this tokenization request |

  

# Additional Useful Endpoints

#### List Tokenization Requests

You can use the following endpoint to list the tokenization requests performed through your platform. You will need to provide your designated Alpaca tokenization account\_id as a URL parameter in the endpoint.

**Request**

**Endpoint**

HTML

```
GET /v1/accounts/:account_id/tokenization/requests
```

**Response**

**Body**

JSON

```
[
   {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  }
]
```

| Field | Description |
| --- | --- |
| id | Unique request identifier assigned by Alpaca |
| issuer\_request\_id | Unique identifier assigned by the Issuer |
| created\_at | Timestamp when the request was created |
| updated\_at | Timestamp when the request was last updated |
| type | Tokenization request type. Valid values are:   * mint * redeem |
| status | Current status of the tokenization request:   * pending * completed * rejected |
| underlying\_symbol | The underlying asset symbol |
| token\_symbol | The token asset symbol |
| qty | The quantity for this request |
| issuer | The tokenized asset's Issuer. Valid values are:   * xstocks * st0x |
| network | The token's blockchain's network. Valid values are:   * solana * base |
| wallet\_address | The wallet address associated with this request |
| tx\_hash | The transaction hash on the blockchain |
| fees | The fees charged for this tokenization request |

# Glossary

* **Authorized Participant**: An entity licensed to conduct digital asset business in the tokenized asset, e.g xstocks. The Issuer only sells tokenized assets to Authorized Participants (AP). The AP can sell the tokenized assets to their clients.
* **Issuer**: Financial entity which purchases the underlying equity securities, wraps them and creates/issues tokens which are backed by the same.
* **Mint**: The act of converting underlying equity securities into tokenized assets.
* **Redeem**: The act of converting tokenized assets into their underlying equity securities.

  

*Alpaca's Instant Tokenization Network is owned and developed by AlpacaDB, Inc. and Alpaca Crypto LLC.
Additional geographic restrictions may apply for tokenization services based on local regulatory requirements. Neither Alpaca Crypto LLC nor Alpaca Securities LLC are the issuer of, nor directly involved in, the tokenization of any assets. Tokenization is performed by a third party. Tokenized assets do not represent direct equity ownership in any underlying company or issuer. Instead, tokenized assets generally provide economic exposure to the equity securities of an underlying issuer. As such, holders of tokenized assets have no voting rights, dividend entitlements, or legal claims to the underlying company shares or any residual assets in the event of the underlying company’s liquidation or insolvency, unless explicitly stated otherwise. All investments involve risk. For more information, please see our Tokenization Risk [Disclosure](https://files.alpaca.markets/disclosures/library/Tokenization+Disclosure.pdf).*

Updated about 1 month ago

---

Ask AI

---

# Tokenization Guide for Authorized Participant (https://docs.alpaca.markets/docs/tokenization-guide-for-authorized-participant)

# Tokenization Guide for Authorized Participant

The Instant Tokenization Network (ITN) is a platform designed to streamline and accelerate the process of in-kind creation and redemption of tokenized assets. The goal of the ITN is to enable efficient, secure, and rapid conversion of real-world and digital assets to and from various tokens issued by partners on the network. The network acts as instant settlement rails for market participants to programmatically rebalance inventory thereby stitching together fragmented tokenized asset liquidity across the industry. This document will guide the **Authorized Participant** on how to start using Alpaca’s Instant Tokenization Network.

# Overview

Before you can start integrating into Alpaca's ITN (Instant Tokenization Network) as an authorized participant, there are multiple steps that you need to complete:

1. Sign up as an authorized participant with the issuer(s) directly so that you are allowed to mint and redeem their tokens.
2. Integrate into Alpaca's Broker API or Trading API offering to buy and sell stocks on an account in your name at Alpaca. This would allow Alpaca to move stocks to/from your account during the token mint and redeem flows.

Once you have completed the above, this document will guide you to integrate into ITN as an AP. You will need to:

* Provide Alpaca's integration team with:
  + The email address you used when signing up with the issuer(s) as an AP.
  + The Alpaca account number that you expect stock to be moved to/from.
  + Alpaca's integration team will need to perform a handshake process with the issuer to link your Alpaca account to your Issuer account.
* Integrate with 1 Alpaca endpoint that you will utilize to complete token minting flow.
  + [Mint Request](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-authorized-participant#alpacas-mint-request)

# Mint Endpoint and Workflow

The token minting flow has multiple steps that begin when you, as an AP, request token minting from Alpaca. The steps are explained below & depicted in Figure 1 to help you visualize. Any referenced endpoints are also documented below.

1. Once the handshake process mentioned earlier is completed, you will be able to request minting of tokenized assets using [Alpaca's mint request endpoint](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-authorized-participant#alpacas-mint-request).
2. The mint request is validated by both Alpaca and the Issuer.
   1. Alpaca will validate that you:
      1. Are an AP authorized for tokenizations.
      2. Have enough underlying position to mint on your registered Alpaca account.
   2. The Issuer will validate that:
      1. The wallet address you provided is registered to the AP.
      2. The requested token is available on the requested network.
3. Upon successful validation of the mint request, Alpaca journals the requested quantity of the underlying security from your Alpaca account into the Issuer's Alpaca account.
4. Alpaca confirms with the Issuer that the underlying security has been journaled to their account.
5. The issuer then deposits the tokenized assets in the wallet address you've provided on the mint request.
6. Finally, the Issuer informs Alpaca of the successful deposit of tokens in the AP’s wallet address.

![](https://files.readme.io/a23b585ba0b7474a3b1b825ab4bec1429ae6c6dd4b4bd3a9832c5eb51768ac5e-3f7824e1f515ce0e46b759d7a4f4052cc4e5a0c736e2b33a3671b251c0c162b5-Minting_Redeeming2x.png)

Figure 1. Minting a tokenized asset

#### Alpaca's Mint Request

**Endpoint**

HTML

```
POST /v1/accounts/:account_id/tokenization/mint
```

| Field | Description |
| --- | --- |
| account\_id | Your Alpaca account\_id that Alpaca linked to your AP account at the issuer. |

**Body**

JSON

```
{
  "underlying_symbol": "AAPL",
  "qty": "1.23",
  "issuer": "xstocks",
  "network": "solana",
  "wallet_address": "0x1234567A"
}
```

| Field | Description |
| --- | --- |
| underlying\_symbol | Underlying asset symbol |
| qty | The underlying quantity to convert into the tokenized asset. The value can be fractional. |
| issuer | The tokenized asset's Issuer. Valid values are:   * xstocks * st0x |
| network | The token's blockchain's network. Valid values are:   * solana * base |
| wallet\_address | The destination wallet address where the tokenized assets should be deposited.   **Important Note:** You will need to check with the issuer whether this wallet address has to be whitelisted on their platform, and if so you will need to whitelist the address before you can use it as part of a mint request. |

**Response**

**Body**

JSON

```
{
  "id": "14d484e3-46f9-4e11-99ac-6fee0d4455c7",
  "created_at":"2025-09-12T17:28:48.642437-04:00",
  "type": "mint",
  "status": "pending",
  "underlying_symbol": "AAPL",
  "token_symbol": "AAPLx",
  "qty": "3",
  "issuer": "xstocks",
  "network": "solana",
  "wallet_address": "0x1234567A",
  "fees" : "0.567"
}
```

| Field | Description |
| --- | --- |
| id | Unique request identifier assigned by Alpaca |
| created\_at | Timestamp when Alpaca received the mint request |
| type | Tokenization request type:   * mint |
| status | Current status of the mint request:   * pending * completed * rejected |
| underlying\_symbol | The underlying asset symbol |
| token\_symbol | The tokenized asset symbol |
| qty | The underlying quantity to convert into the tokenized asset. It can be fractional. |
| issuer | The tokenized asset's issuer. Valid values are:   * xstocks * st0x |
| network | The token's blockchain network. Valid values are:   * solana * base |
| wallet\_address | The wallet address to receive the tokenized assets |
| fees | Fees charged for this tokenization request |

**Status Codes**

| Status | Description |
| --- | --- |
| 200 | OK - Mint request created successfully |
| 403 | Forbidden - Insufficient position quantity, unsupported account etc. |
| 422 | Invalid Parameters - One or more parameters provided are invalid. |

# Redeem Workflow

The token redeem flow has multiple steps that begin when you, as an AP, deposit tokens to an issuer's redemption wallet address. The steps are explained below & depicted in Figure 2 to help you visualize.

1. The token redemption process will be initiated by the AP by moving their tokens into the Issuer’s redemption wallet address. The Issuer will remove these tokens from circulation.
2. The Issuer will then notify Alpaca that an AP has redeemed their tokens. The issuer will provide multiple fields to Alpaca as documented [here](https://docs.alpaca.markets/v1.3/docs/copy-of-tokenization-guide-for-issuer#/alpacas-redeem-request-endpoint).
3. Finally, Alpaca will journal the underlying asset from the Issuer’s Alpaca account into the AP’s Alpaca account.

Figure 2 depicts the full tokenized asset redemption workflow.

![](https://files.readme.io/3263fe54e35d13d4b3c214298696e9c5d2498a10ea1eb0bb22759627044aa10c-661cc0f3b3881fcdf4d87de2ca7866efe56bea8f8e250965836952699552ea5f-Minting_Redeeming2x_2.png)

Figure 2. Redeeming a tokenized asset

# Additional Useful Endpoints

#### List Tokenization Requests

You can use the following endpoint to list the tokenization requests performed on the Instant Tokenization Network platform.

**Request**

**Endpoint**

HTML

```
GET /v1/accounts/:account_id/tokenization/requests
```

**Response**

**Body**

JSON

```
[
   {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  },
  {
    "id": "12345-678-90AB",
    "issuer_request_id": "ABCDEF123",
    "created_at":"2025-09-12T17:28:48.642437-04:00",
    "updated_at":"2025-09-12T17:28:48.642437-04:00",
    "type": "redeem",
    "status": "completed",
    "underlying_symbol": "TSLA",
    "token_symbol" : "TSLAx",
    "qty" : "123.45",
    "issuer" : "xstocks",
    "network": "solana",
    "wallet_address": "0x1234567A",
    "tx_hash" : "0x1234567A",
    "fees" : "0.567"
  }
]
```

| Field | Description |
| --- | --- |
| id | Unique request identifier assigned by Alpaca |
| issuer\_request\_id | Unique identifier assigned by the Issuer |
| created\_at | Timestamp when the request was created |
| updated\_at | Timestamp when the request was last updated |
| type | Tokenization request type. Valid values are:   * mint * redeem |
| status | Current status of the tokenization request:   * pending * completed * rejected |
| underlying\_symbol | The underlying asset symbol |
| token\_symbol | The token asset symbol |
| qty | The quantity for this request |
| issuer | The tokenized asset's Issuer. Valid values are:   * xstocks * st0x |
| network | The token's blockchain's network. Valid values are:   * solana * base |
| wallet\_address | The wallet address associated with this request |
| tx\_hash | The transaction hash on the blockchain |
| fees | The fees charged for this tokenization request |

# Glossary

* **Authorized Participant**: An entity licensed to conduct digital asset business in the tokenized asset, e.g xstocks. The Issuer only sells tokenized assets to Authorized Participants (AP). The AP can sell the tokenized assets to their clients.
* **Issuer**: Financial entity which purchases the underlying equity securities, wraps them and creates/issues tokens which are backed by the same.
* **Mint**: The act of converting underlying equity securities into tokenized assets.
* **Redeem**: The act of converting tokenized assets into their underlying equity securities.

  

*Alpaca's Instant Tokenization Network is owned and developed by AlpacaDB, Inc. and Alpaca Crypto LLC.
Additional geographic restrictions may apply for tokenization services based on local regulatory requirements. Neither Alpaca Crypto LLC nor Alpaca Securities LLC are the issuer of, nor directly involved in, the tokenization of any assets. Tokenization is performed by a third party. Tokenized assets do not represent direct equity ownership in any underlying company or issuer. Instead, tokenized assets generally provide economic exposure to the equity securities of an underlying issuer. As such, holders of tokenized assets have no voting rights, dividend entitlements, or legal claims to the underlying company shares or any residual assets in the event of the underlying company’s liquidation or insolvency, unless explicitly stated otherwise. All investments involve risk. For more information, please see our Tokenization Risk [Disclosure](https://files.alpaca.markets/disclosures/library/Tokenization+Disclosure.pdf).*

Updated about 1 month ago

---

Ask AI

---

# Custodial accounts (https://docs.alpaca.markets/docs/custodial-accounts)

# Custodial accounts

A custodial account enables an adult to open an account on behalf of a minor, who otherwise does not have the capacity to enter into a legal contract to open a brokerage account. Alpaca currently supports two custodial account types: Uniform Transfers to Minors Act (UTMA) and Uniform Gifts to Minors Act (UGMA). As part of the offering, Alpaca will custody the account, generate monthly custodial account statements, and handle all annual tax reporting. Please be aware that all tax reporting will be based on the minor's information. Furthermore, a minor cannot use or trade in a custodial account as they are only the beneficiary. Custodial accounts do not support shorting, margin, or pattern day trading. Each of the account opening steps are the same as standard brokerage accounts that Alpaca offers, and any KYC checks will be run on the adult. This documentation will serve to highlight any notable differences between the account opening processes.

**Custodial Account Object**

| Attribute | Notes |
| --- | --- |
| account\_type | Designate which type of account is to be opened with Alpaca - passing 'custodial' will create a custodial account. |
| contact | Contact information about the user. |
| identity | KYC information about the user. |
| disclosures | Required disclosures about the user. |
| documents | Any documents that need to be uploaded (eg. passport, visa, …). |
| trusted\_contact | The contact information of a trusted contact to the user in case account recovery is needed. |
| minor\_identity | Information about the minor that is associated with the account. All fields in this object will be required when account\_type is 'custodial'. |

**Minor identity object**

| Attribute | Type |
| --- | --- |
| given\_name | string |
| family\_name | string |
| email | string |
| date\_of\_birth | date |
| tax\_id | string |
| tax\_id\_type | ENUM.TaxIdType |
| country\_of\_citizenship | string |
| country\_of\_birth | string |
| country\_of\_tax\_residence | string |
| state | string |

  

## Creating a Custodial Account

```
POST /v1/accounts
```

The custodian, or adult associated with the account, will submit an account application with the required information and a signed custodian customer agreement. This will create a custodial account for the adult on behalf of the minor, whose information will be submitted in the minor\_identity section.

If you utilize Alpaca for KYCaaS, we will perform the necessary checks and approve the account once we have determined the custodian information is legitimate. Please refer to the Events API for account status changes and any KYC updates that require you to take further action.

Note: All account statuses and their definitions can be found [here](https://docs.alpaca.markets/docs/accounts-statuses).

**Sample Request**

JSON

```
{
  "account_type": "custodial",
  "contact": {
    "email_address": "[email protected]",
    "phone_number": "555-676-7788",
    "street_address": ["20 N San Mateo Dr"],
    "city": "San Mateo",
    "state": "CA",
    "postal_code": "94401",
    "country": "USA"
  },
  "identity": {
    "given_name": "John",
    "family_name": "Doe",
    "date_of_birth": "1990-01-01",
    "tax_id": "676-55-4321",
    "tax_id_type": "USA_SSN",
    "country_of_citizenship": "USA",
    "country_of_birth": "USA",
    "country_of_tax_residence": "USA",
    "funding_source": ["employment_income"],
    "annual_income_min": "30000",
    "annual_income_max": "50000",
    "liquid_net_worth_min": "100000",
    "liquid_net_worth_max": "150000",
    "total_net_worth_min": "10000",
    "total_net_worth_max": "10000",
    "liquidity_needs": "does_not_matter",
    "investment_experience_with_stocks": "over_5_years",
    "investment_experience_with_options": "over_5_years",
    "risk_tolerance": "conservative",
    "investment_objective": "market_speculation",
    "investment_time_horizon": "more_than_10_years",
    "marital_status": "MARRIED",
    "middle_name": "M",
    "number_of_dependents": 5
  },
  "disclosures": {
    "is_control_person": false,
    "is_affiliated_exchange_or_finra": false,
    "is_politically_exposed": false,
    "immediate_family_exposed": false
  },
  "agreements": [

         {
      "agreement": "customer_agreement",
      "signed_at": "2025-09-11T18:13:44Z",
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
    "email_address": "[email protected]"
  },
  "minor_identity": {
    "given_name": "Jimmy",
    "family_name": "Doe",
    "email": "[email protected]",
    "date_of_birth": "2015-01-01",
    "tax_id": "676-54-4321",
    "tax_id_type": "USA_SSN",
    "country_of_citizenship": "USA",
    "country_of_birth": "USA",
    "country_of_tax_residence": "USA",
    "state": "CA"
  }
}
```

*A copy of the custodian customer agreement and the custodial account disclosure are available upon request - please reach out to Alpaca for more information.*

*Note: Revisions follow the RR.MM.YYYY format (RR denotes the revision number); the request payload must include the latest customer\_agreement (rev ≥ 18) with the revision explicitly specified.*

**Response model**

| Attribute | Type | Notes |
| --- | --- | --- |
| id | string/UUID | UUID that identifies the account for later reference |
| account\_number | string | A human-readable account number that can be shown to the end user |
| status | ENUM.AccountStatus |  |
| currency | string | Always USD |
| last\_equity | string | EOD equity calculation (cash + long market value + short market value) |
| created\_at | string | RFC3339 format |

  

JSON

```
{
  "account": {
    "id": "0d18ae51-3c94-4511-b209-101e1666416b",
    "account_number": "9034005019",
    "status": "ACTIVE",
    "currency": "USD",
    "last_equity": "1500.65",
    "created_at": "2019-09-30T23:55:31.185998Z"
  }
}
```

**Error Codes**

| Error Code | Description |
| --- | --- |
| 400 | Bad Request: The body in the request is not valid |
| 409 | Conflict: There is already an existing account registered with the same email address. |
| 422 | Unprocessable Entity: Invalid input value. |
| 500 | Internal Server Error: Some server error occurred. Please contact Alpaca. |

  

## Updating an Account

```
PATCH /v1/accounts/{account_id}
```

This operation updates custodial account information. In addition to what is listed for traditional brokerage accounts, the minor identity information is modifiable.

**Response Parameters**

| Attribute | Requirement |
| --- | --- |
| contact | Optional |
| identity | Optional |
| disclosures | Optional |
| documents | Optional |
| trusted\_contact | Optional |
| minor\_identity | Optional |

**Minor Identity parameters**

| Attribute | Type | Requirement | Notes |
| --- | --- | --- | --- |
| given\_name | string | Optional |  |
| family\_name | string | Optional |  |
| email | string | Optional |  |
| date\_of\_birth | date | Optional | RFC3339 format |
| tax\_id | string | Optional |  |
| tax\_id\_type | ENUM.TaxIdType | Required | Must be 'USA\_SSN' |
| country\_of\_citizenship | string | Required | Must be 'USA' |
| country\_of\_birth | string | Required | 3 letter country code acceptable |
| country\_of\_tax\_residence | string | Required | Must be 'USA' |
| state | string | Required | Only accepts two letter state codes |

**Response**

If all parameters are valid and updates have been made, it returns with status code 200. The response is the account model.

**Error Codes**

| Error Code | Description |
| --- | --- |
| 400 | Bad Request: The body in the request is not valid |
| 422 | Unprocessable Entity: The request body contains an attribute that is not permitted to be updated. |
| 500 | Internal Server Error: Some server error occurred. Please contact Alpaca. |

## Appendix

\*\*Sample Monthly Statement: \*\*

![](https://files.readme.io/40faeb129dcc35af0396dc34b218db02b4128e655a8c5b8147970409b0806c72-Screenshot_2025-12-01_at_11.12.58_PM.png)

Updated about 1 month ago

---

Ask AI

---

# About Trading API (https://docs.alpaca.markets/docs/trading-api)

# About Trading API

Trade stocks & crypto with Alpaca’s easy to use Trading API. Up to 4X intraday & 2X overnight buying power. Short selling. Advanced order types. All packaged and delivered through our API.

# Paper Trading

Paper trading is free and available to all Alpaca users. Paper trading is a real-time simulation environment where you can test your code. You can reset and test your algorithm as much as you want using free, real-time market data. For more click [here](/docs/paper-trading).

# Account Plans

Anyone globally can create an paper only account. All you need to do is sign up with your email address. Alpaca also offers live brokerage accounts (with real money) for individuals and businesses plus crypto accounts. For more click [here](/docs/account-plans).

# Crypto Trading

Alpaca offers crypto trading through our API and the Alpaca web dashboard! Trade all day, seven days a week, as frequently as you’d like. For more click [here](/docs/crypto-trading).

# Understand Orders

Our Trading API supports different order types such as market, limit and stop orders plus more complex ones. For more click [here](/docs/orders-at-alpaca).

# Fractional Trading

Fractional shares are fractions of a whole share, meaning that you don’t need to buy a whole share to own a portion of a company. You can now buy as little as $1 worth of shares for over 2,000 US equities. For more click [here](/docs/fractional-trading).

We only allow market orders for fractional trading at the moment.

# User Protections

We have enabled several types of protections to enhance your trading experience. For more click [here](/docs/user-protection).

Updated 5 months ago

---

Ask AI

---

# Getting Started with Trading API (https://docs.alpaca.markets/docs/getting-started-with-trading-api)

# Getting Started with Trading API

This section outlines how to install Alpaca’s SDKs, create a free alpaca account, locate your API keys, and how to submit orders applicable for both stocks and crypto.

# Request ID

All trading API endpoint provides a unique identifier of the API call in the response header with `X-Request-ID` key, the Request ID helps us to identify the call chain in our system.

Make sure you provide the Request ID in all support requests that you created, it could help us to solve the issue as soon as possible. Request ID can't be queried in other endpoints, that is why we suggest to persist the recent Request IDs.

Shell

```
$ curl -v https://paper-api.alpaca.markets/v2/account
...
> GET /v2/account HTTP/1.1
> Host: paper-api.alpaca.markets
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Date: Fri, 25 Aug 2023 09:34:40 GMT
< Content-Type: application/json
< Content-Length: 26
< Connection: keep-alive
< X-Request-ID: 649c5a79da1ab9cb20742ffdada0a7bb
<
...
```

Updated 5 months ago

---

Ask AI

---

# Working with /account (https://docs.alpaca.markets/docs/working-with-account)

# Working with /account

Learn how to use the /account endpoint to learn about the state of your account

# View Account Information

By sending a `GET` request to our `/v2/account` endpoint, you can see various information about your account, such as the amount of buying power available or whether or not it has a PDT flag.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get our account information.
alpaca.getAccount().then((account) => {
  // Check if our account is restricted from trading.
  if (account.trading_blocked) {
    console.log("Account is currently restricted from trading.");
  }

  // Check how much money we can use to open new positions.
  console.log(`$${account.buying_power} is available as buying power.`);
});
```

```
using Alpaca.Markets;
using System;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get our account information.
            var account = await client.GetAccountAsync();

            // Check if our account is restricted from trading.
            if (account.IsTradingBlocked)
            {
                Console.WriteLine("Account is currently restricted from trading.");
            }

            Console.WriteLine(account.BuyingPower + " is available as buying power.");

            Console.Read();
        }
    }
}
```

```
package main

import (
	"fmt"

	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get our account information.
	account, err := alpaca.GetAccount()
	if err != nil {
		panic(err)
	}

	// Check if our account is restricted from trading.
	if account.TradingBlocked {
		fmt.Println("Account is currently restricted from trading.")
	}

	// Check how much money we can use to open new positions.
	fmt.Printf("%v is available as buying power.\n", account.BuyingPower)
}
```

# View Gain/Loss of Portfolio

You can use the information from the account endpoint to do things like calculating the daily profit or loss of your account.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get account information.
alpaca.getAccount().then((account) => {
  // Calculate the difference between current balance and balance at the last market close.
  const balanceChange = account.equity - account.last_equity;

  console.log("Today's portfolio balance change:", balanceChange);
});
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// With the Alpaca API, you can check on your daily profit or loss by
// comparing your current balance to yesterday's balance.

namespace GetPnLExample
{
    internal class GetPnL
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get account info
            var account = await client.GetAccountAsync();

            // Check our current balance vs. our balance at the last market close
            var balance_change = account.Equity - account.LastEquity;

            Console.WriteLine($"Today's portfolio balance change: ${balance_change}");
        }
    }
}
```

```
package main

import (
	"fmt"
	"log"

	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func main() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")

	// Get account information.
	account, err := alpaca.GetAccount()
	if err != nil {
		log.Fatalln(err)
	}

	// Calculate the difference between current balance and balance at the last market close.
	balanceChange := account.Equity.Sub(account.LastEquity)

	fmt.Println("Today's portfolio balance change:", balanceChange)
}
```

Updated 5 months ago

---

Ask AI

---

# Working with /assets (https://docs.alpaca.markets/docs/working-with-assets)

# Working with /assets

Learn how to use the `/assets` endpoint to learn more about assets available on Alpaca. Both Securities and Crypto can be retrieved from the `/assets` endpoint.

# Get a List of Assets

If you send a `GET` request to our `/v2/assets` endpoint, you’ll receive a list of US equities.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

trading_client = TradingClient('api-key', 'secret-key')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get a list of all active assets.
const activeAssets = alpaca
  .getAssets({
    status: "active",
  })
  .then((activeAssets) => {
    // Filter the assets down to just those on NASDAQ.
    const nasdaqAssets = activeAssets.filter(
      (asset) => asset.exchange == "NASDAQ"
    );
    console.log(nasdaqAssets);
  });
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get a list of all active assets.
            var assets = await client.ListAssetsAsync(
                new AssetsRequest { AssetStatus = AssetStatus.Active });

            // Filter the assets down to just those on NASDAQ.
            var nasdaqAssets = assets.Where(asset => asset.Exchange == Exchange.NyseMkt);

            Console.Read();
        }
    }
}
```

```
package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get a list of all active assets.
	status := "active"
	assets, err := alpaca.ListAssets(&status)
	if err != nil {
		panic(err)
	}

	// Filter the assets down to just those on NASDAQ.
	nasdaq_assets := []alpaca.Asset{}
	for _, asset := range assets {
		if asset.Exchange == "NASDAQ" {
			nasdaq_assets = append(nasdaq_assets, asset)
		}
	}
}
```

# See If a Particular Asset is Tradable on Alpaca

By sending a symbol along with our request, we can get the information about just one asset. This is useful if we just want to make sure that a particular asset is tradable before we attempt to buy it.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# search for AAPL
aapl_asset = trading_client.get_asset('AAPL')

if aapl_asset.tradable:
    print('We can trade AAPL.')
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Check if AAPL is tradable on the Alpaca platform.
alpaca.getAsset("AAPL").then((aaplAsset) => {
  if (aaplAsset.tradable) {
    console.log("We can trade AAPL.");
  }
});
```

```
using Alpaca.Markets;
using System;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Check if AAPL is tradable on the Alpaca platform.
            try
            {
                var asset = await client.GetAssetAsync("AAPL");
                if (asset.IsTradable)
                {
                    Console.WriteLine("We can trade AAPL");
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Asset not found for AAPL.");
            }

            Console.Read();
        }
    }
}
```

```
package main

import (
	"fmt"
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Check if AAPL is tradable on the Alpaca platform.
	asset, err := alpaca.GetAsset("AAPL")
	if err != nil {
		fmt.Println("Asset not found for AAPL.")
	} else if asset.Tradable {
		fmt.Println("We can trade AAPL.")
	}
}
```

Updated 5 months ago

---

Ask AI

---

# Working with /orders (https://docs.alpaca.markets/docs/working-with-orders)

# Working with /orders

Learn how to submit orders to Alpaca.

This page contains examples of some of the things you can do with order objects through our API. For additional help understanding different types of orders and how they behave once they’re placed, please check out the Orders on Alpaca page.

# Place New Orders

Orders can be placed with a `POST` request to our `/v2/orders` endpoint.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# preparing limit order
limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# Limit order
limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Submit a market order to buy 1 share of Apple at market price
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "buy",
  type: "market",
  time_in_force: "day",
});

// Submit a limit order to attempt to sell 1 share of AMD at a
// particular price ($20.50) when the market opens
alpaca.createOrder({
  symbol: "AMD",
  qty: 1,
  side: "sell",
  type: "limit",
  time_in_force: "opg",
  limit_price: 20.5,
});
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to buy 1 share of Apple at market price
            var order = await client.PostOrderAsync(MarketOrder.Buy("AAPL", 1));

            // Submit a limit order to attempt to sell 1 share of AMD at a
            // particular price ($20.50) when the market opens
            order = await client.PostOrderAsync(
                LimitOrder.Sell("AMD", 1, 20.50M).WithDuration(TimeInForce.Opg));

            Console.Read();
        }
    }
}
```

```
package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
	"github.com/shopspring/decimal"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Submit a market order to buy 1 share of Apple at market price
	symbol := "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Buy,
		Type: alpaca.Market,
		TimeInForce: alpaca.Day,
	})

	// Submit a limit order to attempt to sell 1 share of AMD at a
	// particular price ($20.50) when the market opens
	symbol = "AMD"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.Limit,
		TimeInForce: alpaca.OPG,
		LimitPrice: decimal.NewFromFloat(20.50),
	})
}
```

# Submit Shorts

Short orders can also be placed for securities which you do not hold an open long position in.

PythonC#

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// With the Alpaca API, you can open a short position by submitting a sell
// order for a security that you have no open long position with.

namespace ShortingExample
{
    internal class ShortProgram
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        // The security we'll be shorting
        private static string symbol = "TSLA";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var tradingClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            var dataClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaDataClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to open a short position of one share
            var order = await tradingClient.PostOrderAsync(MarketOrder.Sell(symbol, 1));
            Console.WriteLine("Market order submitted.");

            // Submit a limit order to attempt to grow our short position
            // First, get an up-to-date price for our security
            var snapshot = await dataClient.GetSnapshotAsync(symbol);
            var price = snapshot.MinuteBar.Close;

            // Submit another order for one share at that price
            order = await tradingClient.PostOrderAsync(LimitOrder.Sell(symbol, 1, price));
            Console.WriteLine($"Limit order submitted. Limit price = {order.LimitPrice}");

            // Wait a few seconds for our orders to fill...
            Thread.Sleep(2000);

            // Check on our position
            var position = await tradingClient.GetPositionAsync(symbol);
            if (position.Quantity < 0)
            {
                Console.WriteLine($"Short position open for {symbol}");
            }
        }
    }
}
```

# Using Client Order IDs

`client_order_id` can be used to organize and track specific orders in your client program. Unique `client_order_ids` for different strategies is a good way of running parallel algos across the same account.

PythonJavaScriptC#

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    client_order_id='my_first_order',
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# Get our order using its Client Order ID.
my_order = trading_client.get_order_by_client_id('my_first_order')
print('Got order #{}'.format(my_order.id))
```

```
const Alpaca = require('@alpacahq/alpaca-trade-api')
const alpaca = new Alpaca()

// Submit a market order and assign it a Client Order ID.
alpaca.createOrder({
    symbol: 'AAPL',
    qty: 1,
    side: 'buy',
    type: 'market',
    time_in_force: 'day',
    client_order_id='my_first_order'
})

// Get our order using its Client Order ID.
alpaca.getOrderByClientOrderId('my_first_order')
    .then((myOrder) => {
        console.log(`Got order #${myOrder.id}.`)
    })
```

```
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        private static string CLIENT_ORDER_ID = "my_first_order";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order and assign it a Client Order ID
            await client.PostOrderAsync(
                MarketOrder.Buy("AAPL", 1)
                    .WithClientOrderId(CLIENT_ORDER_ID));

            // Get our order using its Client Order ID
            var order = await client.GetOrderAsync(CLIENT_ORDER_ID);

            Console.WriteLine($"Got order #{order.ClientOrderId}");
            Console.Read();
        }
    }
}
```

# Submitting Bracket Orders

Bracket orders allow you to create a chain of orders that react to execution and stock price. For more details, go to Bracket Order Overview.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing bracket order with both stop loss and take profit
bracket__order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=5,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.BRACKET,
                    take_profit=TakeProfitRequest(limit_price=400),
                    stop_loss=StopLossRequest(stop_price=300)
                    )

bracket_order = trading_client.submit_order(
                order_data=bracket__order_data
               )

# preparing oto order with stop loss
oto_order_data = LimitOrderRequest(
                    symbol="SPY",
                    qty=5,
                    limit_price=350,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.OTO,
                    stop_loss=StopLossRequest(stop_price=300)
                    )

# Market order
oto_order = trading_client.submit_order(
                order_data=oto_order_data
               )
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

const symbol = "AAPL";
alpaca
  .getBars("minute", symbol, {
    limit: 5,
  })
  .then((barset) => {
    const currentPrice = barset[symbol].slice(-1)[0].closePrice;

    // We could buy a position and add a stop-loss and a take-profit of 5 %
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "bracket",
      stop_loss: {
        stop_price: currentPrice * 0.95,
        limit_price: currentPrice * 0.94,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });

    // We could buy a position and just add a stop loss of 5 % (OTO Orders)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oto",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
    });

    // We could split it to 2 orders. first buy a stock,
    // and then add the stop/profit prices (OCO Orders)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
    });

    // wait for it to buy position and then
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "sell",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oco",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });
  });
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace ShortingExample
{
    internal class ShortProgram
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        private static string symbol = "APPL";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var tradingClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            var dataClient = Alpaca.Markets.Environments.Paper
                .GetAlpacaDataClient(new SecretKey(API_KEY, API_SECRET));

            var snapshot = await dataClient.GetSnapshotAsync(symbol);
            var price = snapshot.MinuteBar.Close;

            // We could buy a position and add a stop-loss and a take-profit of 5 %
            await tradingClient.PostOrderAsync(
                MarketOrder.Buy(symbol, 1)
                .WithDuration(TimeInForce.Gtc)
                .Bracket(
                    stopLossStopPrice: price * 0.95M,
                    takeProfitLimitPrice: price * 0.94M,
                    stopLossLimitPrice: price * 1.05M));

            // We could buy a position and just add a stop loss of 5 % (OTO Orders)
            await tradingClient.PostOrderAsync(
                MarketOrder.Buy(symbol, 1)
                .WithDuration(TimeInForce.Gtc)
                .StopLoss(
                    stopLossStopPrice: price * 0.95M));

            // We could split it to 2 orders. first buy a stock,
            // and then add the stop/profit prices (OCO Orders)
            await tradingClient.PostOrderAsync(
                LimitOrder.Buy(symbol, 1, price));

            await tradingClient.PostOrderAsync(
                LimitOrder.Sell(symbol, 1, price)
                .WithDuration(TimeInForce.Gtc)
                .OneCancelsOther(
                    stopLossStopPrice: price * 0.95M,
                    stopLossLimitPrice: price * 1.05M));
        }
    }
}
```

```
package main

import (
    "github.com/alpacahq/alpaca-trade-api-go/alpaca"
    "github.com/alpacahq/alpaca-trade-api-go/common"
    "github.com/shopspring/decimal"
)

func init() {
    API_KEY := "YOUR_API_KEY_HERE"
    API_SECRET := "YOUR_API_SECRET_HERE"
    BASE_URL := "https://paper-api.alpaca.markets"
    // Check for environment variables
    if common.Credentials().ID == "" {
        os.Setenv(common.EnvApiKeyID, API_KEY)
    }
    if common.Credentials().Secret == "" {
        os.Setenv(common.EnvApiSecretKey, API_SECRET)
    }
    alpaca.SetBaseUrl(BASE_URL)
}

func main() {
    // Submit a limit order to buy 1 share of Apple and add
    // StopLoss and TakeProfit orders.
    client := alpaca.NewClient(common.Credentials())
    symbol := "AAPL"
    tpp := decimal.NewFromFloat(320.)
    spp := decimal.NewFromFloat(317.)
    limit := decimal.NewFromFloat(318.)
    tp := &alpaca.TakeProfit{LimitPrice: &tpp}
    sl := &alpaca.StopLoss{
        LimitPrice: nil,
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Bracket,
        TakeProfit:  tp,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // We could buy a position and just add a stop loss (OTO Orders)
    spp := decimal.NewFromFloat(317.)
    limit := decimal.NewFromFloat(318.)
    sl := &alpaca.StopLoss{
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Oto,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // We could split it to 2 orders. first buy a stock,
    // and then add the stop/profit prices (OCO Orders)
    limit := decimal.NewFromFloat(318.)
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Buy,
        LimitPrice:  &limit,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Simple,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)

    // wait for it to complete and then
    tpp := decimal.NewFromFloat(320.)
    spp := decimal.NewFromFloat(317.)
    tp := &alpaca.TakeProfit{LimitPrice: &tpp}
    sl := &alpaca.StopLoss{
        LimitPrice: nil,
        StopPrice:  &spp,
    }
    req := alpaca.PlaceOrderRequest{
        AccountID:   common.Credentials().ID,
        AssetKey:    &symbol,
        Qty:         decimal.New(1, 0),
        Side:        alpaca.Sell,
        TimeInForce: alpaca.GTC,
        Type:        alpaca.Limit,
        OrderClass:  alpaca.Oco,
        TakeProfit:  tp,
        StopLoss:    sl,
    }
    order, err := client.PlaceOrder(req)
    fmt.Println(order)
    fmt.Println(err)
}
```

# Submitting Trailing Stop Orders

Trailing stop orders allow you to create a stop order that automatically changes the stop price allowing you to maximize your profits while still protecting your position with a stop price. For more details, go to Trailing Stop Order Overview.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)


trailing_percent_data = TrailingStopOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    trail_percent=1.00 # hwm * 0.99
                    )

trailing_percent_order = trading_client.submit_order(
                order_data=trailing_percent_data
               )


trailing_price_data = TrailingStopOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    trail_price=1.00 # hwm - $1.00
                    )

trailing_price_order = trading_client.submit_order(
                order_data=trailing_price_data
               )
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Submit a market order to buy 1 share of Apple at market price
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "buy",
  type: "market",
  time_in_force: "day",
});

// Submit a trailing stop order to sell 1 share of Apple at a
// trailing stop of
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "sell",
  type: "trailing_stop",
  trail_price: 1.0, // stop price will be hwm - 1.00$
  time_in_force: "day",
});

// Alternatively, you could use trail_percent:
alpaca.createOrder({
  symbol: "AAPL",
  qty: 1,
  side: "sell",
  type: "trailing_stop",
  trail_percent: 1.0, // stop price will be hwm*0.99
  time_in_force: "day",
});
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Submit a market order to buy 1 share of Apple at market price
            var order = await client.PostOrderAsync(
                new NewOrderRequest("AAPL", 1, OrderSide.Buy, OrderType.Market, TimeInForce.Day));

            // Submit a trailing stop order to sell 1 share of Apple at a
            // trailing stop of
            order = await client.PostOrderAsync(
                TrailingStopOrder.Sell("AAPL", 1, TrailOffset.InDollars(1.00M))); // stop price will be hwm - 1.00$

            /**
            // Alternatively, you could use trail_percent:
            order = await client.PostOrderAsync(
                TrailingStopOrder.Sell("AAPL", 1, TrailOffset.InPercent(0.99M))); // stop price will be hwm * 0.99
            */

            Console.Read();
        }
    }
}
```

```
package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
	"github.com/shopspring/decimal"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Submit a market order to buy 1 share of Apple at market price
	symbol := "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Buy,
		Type: alpaca.Market,
		TimeInForce: alpaca.Day,
	})

	// Submit a trailing stop order to sell 1 share of Apple at a
    // trailing stop of
	symbol = "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.TrailingStop,
		StopPrice: decimal.NewFromFloat(1.00),  // stop price will be hwm - 1.00$
		TimeInForce: alpaca.Day,
	})

	// Alternatively, you could use trail_percent:
	symbol = "AAPL"
	alpaca.PlaceOrder(alpaca.PlaceOrderRequest{
		AssetKey: &symbol,
		Qty: decimal.NewFromFloat(1),
		Side: alpaca.Sell,
		Type: alpaca.TrailingStop,
		TrailPercent: decimal.NewFromFloat(1.0),  // stop price will be hwm*0.99
		TimeInForce: alpaca.Day,
	})
}
```

# Retrieve All Orders

If you’d like to see a list of your existing orders, you can send a `GET` request to our `/v2/orders` endpoint.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# Get the last 100 closed orders
get_orders_data = GetOrdersRequest(
    status=QueryOrderStatus.CLOSED,
    limit=100,
    nested=True  # show nested multi-leg orders
)

trading_client.get_orders(filter=get_orders_data)
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get the last 100 of our closed orders
const closedOrders = alpaca
  .getOrders({
    status: "closed",
    limit: 100,
    nested: true, // show nested multi-leg orders
  })
  .then((closedOrders) => {
    // Get only the closed orders for a particular stock
    const closedAaplOrders = closedOrders.filter(
      (order) => order.symbol == "AAPL"
    );
    console.log(closedAaplOrders);
  });
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get the last 100 of our closed orders
            var closedOrders = await client.ListOrdersAsync(
                new ListOrdersRequest
                {
                    LimitOrderNumber = 100,
                    OrderStatusFilter = OrderStatusFilter.Closed
                });

            // Get only the closed orders for a particular stock
            var aaplOrders = closedOrders.Where(order => order.Symbol.Equals("AAPL"));

            Console.Read();
        }
    }
}
```

```
package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get the last 100 of our closed orders
	status := "closed"
	limit := 100
	nested := true // show nested multi-leg orders
	closed_orders, err := alpaca.ListOrders(&status, nil, &limit, &nested)
	if err != nil {
		panic(err)
	}

	// Get only the closed orders for a particular stock
	var aaplOrders []alpaca.Order
	for _, order := range closed_orders {
		if order.Symbol == "AAPL" {
			aaplOrders = append(aaplOrders, order)
		}
	}
}
```

# Listen for Updates to Orders

You can use Websockets to receive real-time updates about the status of your orders as they change. You can see the full documentation here.

PythonJavaScriptC#Go

```
from alpaca.trading.stream import TradingStream

stream = TradingStream('api-key', 'secret-key', paper=True)


@conn.on(client_order_id)
async def on_msg(data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(data.event))

stream.subscribe_trade_updates(on_msg)
# Start listening for updates.
stream.run()
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Prepare the websocket connection and subscribe to trade_updates.
alpaca.websocket.onConnect(function () {
  console.log("Connected");
  client.subscribe(["trade_updates"]);
  setTimeout(() => {
    client.disconnect();
  }, 30 * 1000);
});
alpaca.websocket.onDisconnect(() => {
  console.log("Disconnected");
});
alpaca.websocket.onStateChange((newState) => {
  console.log(`State changed to ${newState}`);
});

// Handle updates on an order you've given a Client Order ID.
const client_order_id = "my_client_order_id";
alpaca.websocket.onOrderUpdate((orderData) => {
  const event = orderData["event"];
  if (orderData["order"]["client_order_id"] == client_order_id) {
    console.log(`Update for ${client_order_id}. Event: ${event}.`);
  }
});

// Start listening for updates.
alpaca.websocket.connect();
```

```
using Alpaca.Markets;
using System;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        // Print a message to the console when the account's status changes.
        public static async Task Main(string[] args)
        {
            // Prepare the websocket connection and subscribe to trade_updates.
            var alpacaStreamingClient = Environments.Paper
                .GetAlpacaStreamingClient(new SecretKey(API_KEY, API_SECRET));

            await alpacaStreamingClient.ConnectAndAuthenticateAsync();
            alpacaStreamingClient.OnTradeUpdate += HandleTradeUpdate;

            Console.Read();
        }

        // Handle incoming trade updates.
        private static void HandleTradeUpdate(ITradeUpdate update)
        {
            if (update.Order.ClientOrderId.Equals("my_client_order_id"))
            {
                Console.WriteLine($"Update for {update.Order.ClientOrderId}. Event: {update.Event}");
            }
        }
    }
}
```

```
package main

import (
	"fmt"

	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
    "github.com/alpacahq/alpaca-trade-api-go/stream"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	if err := stream.Register(alpaca.TradeUpdates, tradeHandler); err != nil {
        panic(err)
    }
}

func tradeHandler(msg interface{}) {
	tradeupdate := msg.(alpaca.TradeUpdate)
	if tradeupdate.Order.ClientOrderID == "my_client_order_id" {
		fmt.Printf("Update for {}. Event: {}.\n", tradeupdate.Order.ClientOrderID, tradeupdate.Event)
	}
}
```

# FAQ

**What should I do if I receive a timeout message from Alpaca when submitting an order?**

The order may have been sent to the market for execution. You should not attempt to resend the order or mark the timed-out order as canceled until confirmed by Alpaca Support or the trading team. Before taking any action on the timed-out order you should check the broker dashboard and contact Alpaca support.  
Please contact our Support Team at [[email protected]](/cdn-cgi/l/email-protection#40333530302f323400212c302123216e2d21322b253433) to verify if the order was successfully submitted and routed to the market.

Updated 5 months ago

---

Ask AI

---

# Working with /positions (https://docs.alpaca.markets/docs/working-with-positions)

# Working with /positions

You can view the positions in your portfolio by making a `GET` request to the `/v2/positions` endpoint. If you specify a symbol, you’ll see only your position for the associated stock.

PythonJavaScriptC#Go

```
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

# Get our position in AAPL.
aapl_position = trading_client.get_open_position('AAPL')

# Get a list of all of our positions.
portfolio = trading_client.get_all_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))
```

```
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get our position in AAPL.
aaplPosition = alpaca.getPosition("AAPL");

// Get a list of all of our positions.
alpaca.getPositions().then((portfolio) => {
  // Print the quantity of shares for each position.
  portfolio.forEach(function (position) {
    console.log(`${position.qty} shares of ${position.symbol}`);
  });
});
```

```
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get our position in AAPL.
            var aaplPosition = await client.GetPositionAsync("AAPL");

            // Get a list of all of our positions.
            var positions = await client.ListPositionsAsync();

            // Print the quantity of shares for each position.
            foreach (var position in positions)
            {
                Console.WriteLine($"{position.Quantity} shares of {position.Symbol}.");
            }

            Console.Read();
        }
    }
}
```

```
package main

import (
	"fmt"
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get our position in AAPL.
	aapl_position, err := alpaca.GetPosition("AAPL")
	if err != nil {
		fmt.Println("No AAPL position.")
	} else {
		fmt.Printf("AAPL position: %v shares.\n", aapl_position.Qty)
	}

	// Get a list of all of our positions.
	positions, err := alpaca.ListPositions()
	if err != nil {
		fmt.Println("No positions found.")
	} else {
		// Print the quantity of shares for each position.
		for _, position := range positions {
			fmt.Printf("%v shares in %s", position.Qty, position.Symbol)
		}
	}
}
```

The current price reflected will be based on the following:

**4:00 am ET - 9:30 am ET** - Last trade based on the premarket

**9:30 am ET - 4pm ET** - Last trade

**4:00 pm ET - 10:00 pm ET** - Last trade based on after-hours trading

**10 pm ET - 4:00 am ET next trading day** - Official closing price from the primary exchange at 4 pm ET.

Updated 5 months ago

---

Ask AI

---

# Paper Trading (https://docs.alpaca.markets/docs/paper-trading)

# Paper Trading

Test your algos in our paper environment. Free and available to all Alpaca users.

Paper trading is a real-time simulation environment where you can test your code. You can reset and test your algorithm as much as you want using free, real-time market data. Paper trading simulates crypto trading as well. Paper trading works the same way as live trading end to end - except the order is not routed a live exchange. Instead, the system simulates the order filling based on the real-time quotes.

When you run your algorithm with the live market, there are many things that can happen that you may not see in backtesting. Orders may not be filled, prices may spike, or your network may get disconnected and retry may be needed. During the software development process, it is important to test your algorithm to catch these things in advance.

> 🌍
>
> ### Anyone globally can create an Alpaca **Paper Only Account**! All you need to do is sign up with your email address.

An Alpaca **Paper Only Account** is for paper trading only. It allows you to fully utilize the Alpaca API and run your algorithm in our paper trading environment only. You won’t be trading real money, but you will be able to track your simulated activity and balance in the Alpaca web dashboard. As an Alpaca Paper Only Account holder, you are only entitled to receive and make use of IEX market data. For more information about our paper trading environment, please refer to Paper Trading Specification.

# Paper vs Live

We are thrilled that many users have found paper trading useful, and we continue to work on improving our paper trading assumptions so that users may have a superior experience. However, please note that paper trading is only a simulation. It provides a good approximation for what one might expect in real trading, but it is not a substitute for real trading and performance may differ. Specifically, paper trading does not account for:

* Market impact of your orders
* Information leakage of your orders
* Price slippage due to latency
* Order queue position (for non-marketable limit orders)
* Price improvement received
* Regulatory fees
* Dividends

If you are interested to incorporate these issues into your testing, you may do so by trading a live brokerage account. Even small amounts of real money can often provide insight into issues not seen in a simulation environment.

## Paper vs Live

| Feature | Paper | Live |
| --- | --- | --- |
| Eligibility | ✅ | ✅ |
| API Access | ✅ | ✅ |
| Free IEX Real Time Data | ✅ | ✅ |
| MFA | ✅ | ✅ |
| Margin Trading | ✅ | ✅ |
| Short Selling | ✅ | ✅ |
| Premarket/After Hours Trading | ✅ | ✅ |
| Borrow Fees | ⛔️ (Coming Soon!) | ✅ |

# Comparing Other Simulators

Users may be interested to compare their paper trading results on Alpaca with their paper trading results on other platforms such as Quantopian or Interactive Brokers. Please note there are several factors that may lead to performance differences. Paper trading platforms may have different:

* Fill prices
* Fill assumptions
* Liquidity assumptions
* Return calculation methodologies
* Market data sources

# Getting Started with Paper Trading

Your initial paper trading account is created with $100k balance as a default setting. You can reset the paper trading account at any time later with arbitrary amount as you configure.

Your paper trading account will have a different API key from your live account, and all you need to do to start using your paper trading account is to replace your API key and API endpoint with ones for the paper trading. The API spec is the same between the paper trading and live accounts. The API endpoint (base URL) is displayed in your paper trading dashboard, and please follow the instruction about how to set it depending on the library you are using. In most cases, you need to set an environment variable `APCA_API_BASE_URL = https://paper-api.alpaca.markets`

# Reset Your Paper Trading Account

We've updated the dashboard to allow you to create and delete paper accounts, rather than resetting them.

To create a new paper account, click the paper account number in the upper left corner of the dashboard and select "Open New Paper Account."

To delete an existing paper account, click the paper account number in the upper left corner, then go to "Account Settings." Locate the paper account you'd like to remove and click the "Delete Account" button next to it.

Don't forget to generate new API keys for any newly created account.

# Rules and Assumptions

* Paper trading account simulates our Pattern Day Trader checks. Orders that would generate a 4th Day Trade within 5 business days will be rejected if the real-time net worth is below $25,000. Please read the [Pattern DayTrader Protection](/docs/user-protection#pattern-day-trader-pdt-protection-at-alpaca) page for more details.
* Paper trading account **does NOT** simulate dividends.
* Paper trading account **does NOT** send order fill emails.
* Market Data API works identically.
* You cannot change the account balance after it is created, unless you reset it.
* Orders are filled only when they become marketable. This means that a non-marketable buy limit order will not be filled until its limit price is equal to or greater than the best ask price, and a non-marketable sell limit order will not be filled until its limit price is equal to or less than the best bid.
* Your order quantity is not checked against the NBBO quantities. In other words, you can submit and receive a fill for an order that is much larger than the actual available liquidity.  
  When orders are eligible to be filled, they will receive partial fills for a random size 10% of the time. If the order price is still marketable, the remaining quantity would be re-evaluated for a subsequent fill.
* Regardless of whether you have a Paper Trading Only account or a real money brokerage account, all orders submitted in paper trading will be matched against the best available current market price (NBBO).

Updated 5 months ago

---

Ask AI

---

# Trading Account (https://docs.alpaca.markets/docs/account-plans)

# Trading Account

# Alpaca Brokerage Account (Live Trading)

After creating an Alpaca Paper Only Account, you can enable live trading by becoming an Alpaca Brokerage Account holder. This requires you to go through an account on-boarding process with Alpaca Securities LLC, a FINRA member and SEC registered broker-dealer. We now support brokerage accounts for individuals and business entities from around the world.

With a brokerage account, you will be able to fully utilize Alpaca for your automated trading and investing needs. Using the Alpaca API, you’ll be able to buy and sell stocks in your brokerage account, and you’ll receive real-time consolidated market data. In addition, you will continue to be able to test your strategies and simulate your trades in our paper trading environment. And with the Alpaca web dashboard, it’s easy to monitor both your paper trading and your real money brokerage account. All accounts are opened as margin accounts. Accounts with $2,000 or more equity will have access to margin trading and short selling.

## Individuals

Alpaca Securities LLC supports individual taxable brokerage accounts. At this time, we do not support retirement accounts.

## Businesses/Incorporated Entities

You can open a business trading account to use Alpaca for trading purposes, but not for building apps/services.

> 👀
>
> ### Alpaca currently accepts entities that are *Corporations*, *LLCs* and *Partnerships* in the U.S., and around the world. There is a $30,000 minimum deposit required for opening a business account at Alpaca.

# Markets Supported

Currently, Alpaca only supports trading of listed U.S. stocks and select cryptocurrencies.

# The Account Object

The account API serves important information related to an account, including account status, funds available for trade, funds available for withdrawal, and various flags relevant to an account’s ability to trade.

An account maybe be blocked for just for trades (`trading_blocked` flag) or for both trades and transfers (`account_blocked` flag) if Alpaca identifies the account to be engaging in any suspicious activity. Also, in accordance with FINRA’s pattern day trading rule, an account may be flagged for pattern day trading (`pattern_day_trader` flag), which would inhibit an account from placing any further day-trades.

Please note that cryptocurrencies are not eligible assets to be used as collateral for margin accounts and will require the asset be traded using cash only.

## Sample Object

JSON

```
{
  "account_blocked": false,
  "account_number": "010203ABCD",
  "buying_power": "262113.632",
  "cash": "-23140.2",
  "created_at": "2019-06-12T22:47:07.99658Z",
  "currency": "USD",
  "crypto_status": "ACTIVE",
  "non_marginable_buying_power": "7386.56",
  "accrued_fees": "0",
  "pending_transfer_in": "0",
  "pending_transfer_out": "0",
  "daytrade_count": "0",
  "daytrading_buying_power": "262113.632",
  "equity": "103820.56",
  "id": "e6fe16f3-64a4-4921-8928-cadf02f92f98",
  "initial_margin": "63480.38",
  "last_equity": "103529.24",
  "last_maintenance_margin": "38000.832",
  "long_market_value": "126960.76",
  "maintenance_margin": "38088.228",
  "multiplier": "4",
  "pattern_day_trader": false,
  "portfolio_value": "103820.56",
  "regt_buying_power": "80680.36",
  "short_market_value": "0",
  "shorting_enabled": true,
  "sma": "0",
  "status": "ACTIVE",
  "trade_suspended_by_user": false,
  "trading_blocked": false,
  "transfers_blocked": false
}
```

## Account Properties

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | string`<uuid>` | Account ID. |
| `account_number` | string | Account number. |
| `status` | string<account\_status> | See detailed account statuses below |
| `crypto_status` | string<account\_status> | The current status of the crypto enablement. See detailed crypto statuses below. |
| `currency` | string | "USD" |
| `cash` | string`<number>` | Cash balance |
| `portfolio_value` | string`<number>` | * *lpaca Broker*\* Total value of cash + holding positions (Equivalent to the equity field) |
| `non_marginable_buying_power` | string`<number>` | Current available non-margin dollar buying power |
| `accrued_fees` | string`<number>` | The fees collected. |
| `pending_transfer_in` | string`<number>` | Cash pending transfer in. |
| `pending_transfer_out` | string`<number>` | Cash pending transfer out |
| `pattern_day_trader` | boolean | Whether or not the account has been flagged as a pattern day trader |
| `trade_suspended_by_user` | boolean | User setting. If `true`, the account is not allowed to place orders. |
| `trading_blocked` | boolean | If `true`, the account is not allowed to place orders. |
| `transfers_blocked` | boolean | If `true`, the account is not allowed to request money transfers. |
| `account_blocked` | boolean | If `true`, the account activity by user is prohibited. |
| `created_at` | string`<timestamp>` | Timestamp this account was created at |
| `shorting_enabled` | boolean | Flag to denote whether or not the account is permitted to short |
| `long_market_value` | string`<number>` | Real-time MtM value of all long positions held in the account |
| `short_market_value` | string`<number>` | Real-time MtM value of all short positions held in the account |
| `equity` | string`<number>` | `cash` + `long_market_value` + `short_market_value` |
| `last_equity` | string`<number>` | Equity as of previous trading day at 16:00:00 ET |
| `multiplier` | string`<number>` | Buying power (BP) multiplier that represents account margin classification  Valid values:   * **1** (standard limited margin account with 1x BP), * **2** (reg T margin account with 2x intraday and overnight BP; this is the default for all non-PDT accounts with $2,000 or more equity), * **4** (PDT account with 4x intraday BP and 2x reg T overnight BP) |
| `buying_power` | string`<number>` | Current available $ buying power; If multiplier = 4, this is your daytrade buying power which is calculated as (last\_equity - (last) maintenance\_margin)\_ 4; If multiplier = 2, buying\_power = max(equity – initial\_margin,0)\_ 2; If multiplier = 1, buying\_power = cash |
| `initial_margin` | string`<number>` | Reg T initial margin requirement (continuously updated value) |
| `maintenance_margin` | string`<number>` | Maintenance margin requirement (continuously updated value) |
| `sma` | string`<number>` | Value of special memorandum account (will be used at a later date to provide additional buying\_power) |
| `daytrade_count` | int | The current number of daytrades that have been made in the last 5 trading days (inclusive of today) |
| `last_maintenance_margin` | string`<number>` | Your maintenance margin requirement on the previous trading day |
| `daytrading_buying_power` | string`<number>` | Your buying power for day trades (continuously updated value) |
| `regt_buying_power` | string`<number>` | Your buying power under Regulation T (your excess equity - equity minus margin value - times your margin multiplier) |

# Account Status ENUMS

The following are the possible account status values. Most likely, the account status is `ACTIVE` unless there is an issue. The account status may get to `ACCOUNT_UPDATED` when personal information is being updated from the dashboard, in which case you may not be allowed trading for a short period of time until the change is approved.

| status | description |
| --- | --- |
| `ONBOARDING` | The account is onboarding. |
| `SUBMISSION_FAILED` | The account application submission failed for some reason. |
| `SUBMITTED` | The account application has been submitted for review. |
| `ACCOUNT_UPDATED` | The account information is being updated. |
| `APPROVAL_PENDING` | The final account approval is pending. |
| `ACTIVE` | The account is active for trading. |
| `REJECTED` | The account application has been rejected. |

Updated about 2 months ago

---

Ask AI

---

# Crypto Spot Trading (https://docs.alpaca.markets/docs/crypto-trading)

# Crypto Spot Trading

Trade crypto through our API and the Alpaca web dashboard! Trade all day, seven days a week, as frequently as you’d like.

> 🚧
>
> ### As of November 18, 2022, cryptocurrency trading is open to select international jurisdictions and some U.S. jurisdictions.
>
> To view the supported US regions for crypto trading, click [here](https://alpaca.markets/support/what-regions-support-cryptocurrency-trading).

# Supported Coins

Alpaca supports over 20+ unique crypto assets across 56 trading pairs. Current trading pairs are based on BTC, USD, USDT and USDC) with more assets and trading pairs coming soon.

To query all available crypto assets and pairs you can you use the following API call:

cURL

```
curl --request GET 'https://api.alpaca.markets/v2/assets?asset_class=crypto' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>'
```

Below is a sample trading pair object composed of two assets, BTC and USD.

JSON

```
{
  "id": "276e2673-764b-4ab6-a611-caf665ca6340",
  "class": "crypto",
  "exchange": "ALPACA",
  "symbol": "BTC/USD",
  "name": "BTC/USD pair",
  "status": "active",
  "tradable": true,
  "marginable": false,
  "shortable": false,
  "easy_to_borrow": false,
  "fractionable": true,
  "min_order_size": "0.0001",
  "min_trade_increment": "0.0001",
  "price_increment": "1"
}
```

Note that symbology for trading pairs has changed from our previous format, where `BTC/USD` was previously referred to as `BTCUSD`. Our API has made proper changes to support the legacy convention as well for backwards compatibility.

For further reference see Assets API. **add link**

# Supported Orders

When submitting crypto orders through the Orders API and the Alpaca web dashboard, Market, Limit and Stop Limit orders are supported while the supported `time_in_force` values are `gtc`, and `ioc`. We accept fractional orders as well with either `notional` or `qty` provided.

You can submit crypto orders for any supported crypto pair via API, see the below cURL POST request.

cURL

```
curl --request POST 'https://paper-api.alpaca.markets/v2/orders' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "symbol": "BTC/USD",
  "qty": "0.0001",
  "side": "buy",
  "type": "market",
  "time_in_force": "gtc"
}'
```

The above request submits a market order via API to buy 0.0001 BTC with USD (BTC/USD pair) that is good till end of day.

To learn more see **orders** and **fractional trading**.

All cryptocurrency assets are fractionable but the supported decimal points vary depending on the cryptocurrency. See **Assets entity** for information on fractional precisions per asset.

Note these values could change in the future.

# Crypto Market Data

You can check out the [documentation](https://docs.alpaca.markets/docs/historical-crypto-data-1) and the [API reference](https://docs.alpaca.markets/reference/cryptobars-1) of our crypto market data.

Here we provide an example to request the latest order book data (bids and asks) for the following three coin pairs: BTC/USD, ETH/BTC, and ETH/USD.

cURL

```
curl 'https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD'
```

JSON

```
{
    "orderbooks": {
        "BTC/USD": {
            "a": [
                {
                    "p": 66051.621,
                    "s": 0.275033
                },
                ...
            ],
            "b": [
                {
                    "p": 65986.962,
                    "s": 0.27813
                },
                ...
            ],
            "t": "2024-07-24T07:31:01.373709495Z"
        },
        "ETH/USD": { ... }
        },
        "ETH/BTC": { ... }
    }
}
```

Additionally, you can subscribe to real-time crypto data via Websockets. Example below leverages wscat to subscribe to BTC/USD order book.

JSON

```
$ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action":"auth","key":"<YOUR API KEY>","secret":"<YOUR API SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe","quotes":["ETH/USD"]}
< [{"T":"subscription","trades":[],"quotes":["ETH/USD"],"orderbooks":[],"bars":[],"updatedBars":[],"dailyBars":[]}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3450.2,"as":4.3803,"t":"2024-07-24T07:38:06.88490478Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3451.1,"as":8.73823,"t":"2024-07-24T07:38:06.88493591Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88511154Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.644,"bs":8.797,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88512141Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.51,"bs":4.33,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88516355Z"}]
```

For further reference of real-time crypto pricing data see [its documentation](https://docs.alpaca.markets/docs/real-time-crypto-pricing-data).

# Transferring Crypto

Alpaca now offers native on-chain crypto transfers with wallets! If you have crypto trading enabled and reside in an eligible US state or international jurisdiction you can access wallets on the web dashboard via the Crypto Transfers tab.

Alpaca wallets currently support transfers for Bitcoin, Ethereum, and all Ethereum (ERC20) based tokens. To learn more on transferring crypto with Alpaca, see **[Crypto Wallets FAQs](https://alpaca.markets/support/crypto-wallet-faq)**

# Crypto Spot Trading Fees

While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller's posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. **A maker is someone who adds liquidity, and the order gets placed on the order book. A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.**

See the below table with volume-tiered fee pricing:

| Tier | 30D Trading Volume (USD) | Maker | Taker |
| --- | --- | --- | --- |
| 1 | 0 - 100,000 | 15 bps | 25 bps |
| 2 | 100,000 - 500,000 | 12 bps | 22 bps |
| 3 | 500,000 - 1,000,000 | 10 bps | 20 bps |
| 4 | 1,000,000 - 10,000,000 | 8 bps | 18 bps |
| 5 | 10,000,000 - 25,000,000 | 5 bps | 15 bps |
| 6 | 25,000,000 - 50,000,000 | 2 bps | 13 bps |
| 7 | 50,000,000 - 100,000,000 | 2 bps | 12 bps |
| 8 | 100,000,000+ | 0 bps | 10 bps |

The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples,

* Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
* Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`

To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`. See below example of CFEE object:

JSON

```
{
    "id": "20220812000000000::53be51ba-46f9-43de-b81f-576f241dc680",
    "activity_type": "CFEE",
    "date": "2022-08-12",
    "net_amount": "0",
    "description": "Coin Pair Transaction Fee (Non USD)",
    "symbol": "ETHUSD",
    "qty": "-0.000195",
    "price": "1884.5",
    "status": "executed"
}
```

Fees are currently calculated and posted end of day. If you query on same day of trade you might not get results. We will be providing an update for fee posting to be real-time in the near future.

# Margin and Short Selling

Cryptocurrencies cannot be bought on margin. This means that you cannot use leverage to buy them and orders are evaluated against `non_marginable_buying_power`.

Cryptocurrencies can not be sold short.

# Trading Hours

Crypto trading is offered for 24 hours everyday and your orders will be executed throughout the day.

# Trading Limits

Currently, an order (buy or sell) must not exceed $200k in notional. This is per an order.

Updated 5 months ago

---

Ask AI

---

# Crypto Orders (https://docs.alpaca.markets/docs/crypto-orders)

# Crypto Orders

You can submit crypto orders through the traditional orders API endpoints (`POST/orders`).

* The following order types are supported: `market`, `limit` and `stop_limit`
* The following `time_in_force` values are supported: `gtc`, and `ioc`
* We accept fractional orders as well with either `notional` or `qty` provided

You can submit crypto orders for a any supported crypto pair via API, see the below cURL POST request.

cURL

```
curl --request POST 'https://paper-api.alpaca.markets/v2/orders' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "symbol": "BTC/USD",
  "qty": "0.0001",
  "side": "buy",
  "type": "market",
  "time_in_force": "gtc"
}'
```

The above request submits a market order via API to buy 0.0001 BTC with USD (BTC/USD pair) that is good till end of day.

Updated 5 months ago

---

Ask AI

---

# Crypto Pricing Data (https://docs.alpaca.markets/docs/crypto-pricing-data)

# Crypto Pricing Data

Alpaca provides free limited crypto data and a more advanced unlimited paid plan.

To request trading pairs data via REST API, see [Crypto Pricing Data REST API](https://docs.alpaca.markets/reference/v1beta2cryptobars) Reference.

The example below requests the latest order book data (bid and asks) for the following three crypto trading pairs: BTC/USD, ETH/BTC and ETH/USD.

cURL

```
curl --request GET 'https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD,SOL/USDT' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>'
```

```
{
    "orderbooks": {
        "BTC/USD": {
            "a": [
                {
                    "p": 27539.494,
                    "s":  0.2632414
                },
                ...
            ],
            "b": [
                {
                    "p": 27511.78083,
                    "s": 0.26265668
                },
                ...
            ],
            "t": "2023-03-18T13:31:44.932988033Z"
        },
        "ETH/USD": { ... },
        "ETH/BTC": { ... },
        "SOL/USDT": { ... }
    }
}
```

# Real-Time Crypto Market Data

Additionally, you can subscribe to real-time crypto data via Websockets. Example below leverages wscat to subscribe to:

* BTC/USD trades.
* ETH/USDT and ETH/USD quotes.
* BTC/USD order books

```
 $ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "<KEY>", "secret": "<SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe", "trades":["BTC/USD"], "quotes":["ETH/USDT","ETH/USD"], "orderbooks":["BTC/USD"]}
< [{"T":"subscription","trades":["BTC/USD"],"quotes":["ETH/USDT","ETH/USD"],"orderbooks":["BTC/USD"],"updatedBars":[],"dailyBars":[]}]
< [{"T":"o","S":"BTC/USD","t":"2023-03-18T13:51:29.754747009Z","b":[{"p":27485.3445,"s":0.25893365},{"p":27466.92727,"s":0.52351568},...],"a":[{"p":27512.92,"s":0.26137249},{"p":27547.9425,"s":0.52011956},...],"r":true}]
< [{"T":"q","S":"ETH/USDT","bp":1815.55510989,"bs":8.24941727,"ap":1818.4,"as":4.15121428,"t":"2023-03-18T13:51:33.256826818Z"}]
< ...
```

Updated 5 months ago

---

Ask AI

---

# Crypto Spot Trading Fees (https://docs.alpaca.markets/docs/crypto-fees)

# Crypto Spot Trading Fees

While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller's posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. **A maker is someone who adds liquidity, and the order gets placed on the order book. A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.**

See the below table with volume-tiered fee pricing:

| Tier | 30D Crypto Volume (USD) | Maker | Take |
| --- | --- | --- | --- |
| 1 | 0 - 100,000 | 0.15% | 0.25% |
| 2 | 100,000 - 500,000 | 0.12% | 0.22% |
| 3 | 500,000 - 1,000,000 | 0.10% | 0.20% |
| 4 | 1,000,000 - 10,000,000 | 0.08% | 0.18% |
| 5 | 10,000,000- 25,000,000 | 0.05% | 0.15% |
| 6 | 25,000,000 - 50,000,000 | 0.02% | 0.13% |
| 7 | 50,000,000 - 100,000,000 | 0.02% | 0.12% |
| 8 | 100,000,000+ | 0.00% | 0.10% |

The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples:

* Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
* Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`

To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`.

See below example of CFEE object:

JSON

```
{
    "id": "20220812000000000::53be51ba-46f9-43de-b81f-576f241dc680",
    "activity_type": "CFEE",
    "date": "2022-08-12",
    "net_amount": "0",
    "description": "Coin Pair Transaction Fee (Non USD)",
    "symbol": "ETHUSD",
    "qty": "-0.000195",
    "price": "1884.5",
    "status": "executed"
}
```

Fees are currently calculated and posted end of day. If you query on same day of trade you might not get results. We will be providing an update for fee posting to be real-time in the near future.

> 📘
>
> ### Check out our Crypto Trading FAQ [here](https://alpaca.markets/support/alpaca-crypto-coin-pair-faq)

Updated 5 months ago

---

Ask AI

---

# Options Trading (https://docs.alpaca.markets/docs/options-trading)

# Options Trading

We're excited to support options trading! Use this section to read up on Alpaca's options trading capabilities.

> 🎉
>
> ### Options trading is now available on Live!
>
> Share your feedback on [Options API for Trading API here](https://docs.google.com/forms/d/e/1FAIpQLScIYvKDJnKjXWESs6qxzpgk7pbvkt0IF1_nhv46t4o31-YOng/viewform)

# OpenAPI Spec

You can find our Open API docs here: [<https://docs.alpaca.markets/reference>](https://docs.alpaca.markets/reference).

# Enablement

In the Paper environment, options trading capability will be enabled by default - there's nothing you need to do!

*Note, in production there will be a more robust experience to request options trading.*

For those who do not wish to have options trading enabled, you can disable options trading by navigating to your Trading Dashboard; Account > Configure.

The [Trading Account](https://docs.alpaca.markets/v1.1/reference/getaccount-2) model was updated to reflect the account's options approved and trading levels.

The [Account Configuration](https://docs.alpaca.markets/v1.1/reference/getaccountconfig-1) model was updated to show the maximum options trading level, and allow a user to downgrade to a lower level. Note, a different API will be provided for requesting a level upgrade for live account.

## Trading Levels

Alpaca supports the below options trading levels.

| Level | Supported Trades | Validation |
| --- | --- | --- |
| 0 | * Options trading is disabled | * NA |
| 1 | * Sell a covered call * Sell cash-secured put | * User must own sufficient underlying shares * User must have sufficient options buying power |
| 2 | * Level 1 * Buy a call * Buy a put | * User must have sufficient options buying power |
| 3 | * Level 1,2 * Buy a call spread * Buy a put spread | * User must have sufficient options buying power |

# Option Contracts

## Assets API Update

The [Assets](https://docs.alpaca.markets/v1.1/reference/get-v2-assets-1) endpoint has an existing `attributes` query parameter. Symbols which have option contracts will have an attribute called `options_enabled`.

Querying for symbols with the `options_enabled` attribute allows users to identify the universe of symbols with corresponding option contracts.

## Fetch Contracts

To obtain contract details, a new endpoint was introduced: `/v2/options/contracts?underlying_symbols=`. The endpoint supports fetching a single contract such as `/v2/options/contracts/{symbol_or_id}`

The default params are:

* expiration\_date\_lte: Next weekend
* limit: 100

Example: if `/v2/options/contracts` is called on Thursday, the response will include Thursday and Friday data. If called on a Saturday, the response will include Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, and Friday.

Here is an example of a response object:

JSON

```
{
    "option_contracts": [
        {
            "id": "6e58f870-fe73-4583-81e4-b9a37892c36f",
            "symbol": "AAPL240119C00100000",
            "name": "AAPL Jan 19 2024 100 Call",
            "status": "active",
            "tradable": true,
            "expiration_date": "2024-01-19",
            "root_symbol": "AAPL",
            "underlying_symbol": "AAPL",
            "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
            "type": "call",
            "style": "american",
            "strike_price": "100",
            "size": "100",
            "open_interest": "6168",
            "open_interest_date": "2024-01-12",
            "close_price": "85.81",
            "close_price_date": "2024-01-12"
        },
...
	],
   "page_token": "MTAw",
   "limit": 100
}
```

More detailed information regarding this endpoint can be found on the OpenAPI spec [here](https://docs.alpaca.markets/v1.1/reference/get-options-contracts).

# Market Data

Alpaca offers both [real-time](https://docs.alpaca.markets/docs/real-time-option-data) and [historical](https://docs.alpaca.markets/docs/historical-option-data) option data.

# Placing an Order

Placing an order for an option contract uses the same [Orders API](https://docs.alpaca.markets/v1.1/reference/postorder-1) that is used for equities and crypto asset classes.

Given the same Orders API endpoint is being used, Alpaca has implemented a series of validations to ensure the options order does not include attributes relevant to other asset classes. Some of these validations include:

* Ensuring `qty` is a whole number
* `Notional` must not be populated
* `time_in_force` must be `day`
* `extended_hours` must be `false` or not populated
* `type` must be `market`,`limit`,`stop` or ,`stop_limit` (`stop` and `stop_limit` are only available for single-leg orders)

Examples of valid order payloads can be found as a child page [here](https://docs.alpaca.markets/docs/options-orders).

# Options Positions

Good news - the existing [Positions API](https://docs.alpaca.markets/reference/getallopenpositions) model will work with options contracts. There is not expected to be a change to this model.

As an additive feature, we aim to support fetching positions of a certain asset class; whether that be options, equities, or crypto.

# Account Activities

The existing schema for trade activities (TAs) are applicable for the options asset class. For example, the `FILL` activity is applicable to options and maintains it's current shape for options.

There are new non-trade activities (NTAs) entry types for options, however the schema stays the same. These NTAs reflect exercise, assignment, and expiry. More details can be found on a child page [here](https://docs.alpaca.markets/docs/non-trade-activities-for-option-events) and on the OpenAPI spec [here](https://docs.alpaca.markets/v1.1/reference/getaccountactivities-2).

> 🚧
>
> ### On PAPER NTAs are synced at the start of the following day. While your balance and positions are updated instantly, NTAs on PAPER will be visible in the Activities endpoint only the next day

# Exercise and DNE Instructions

## Exercise

Contract holders may submit exercise instructions to Alpaca. Alpaca will process instructions and work with our clearing partner accordingly.

All available held shares of this option contract will be exercised. By default, Alpaca will automatically exercise in-the-money (ITM) contracts at expiry.

Exercise requests will be processed immediately once received. Exercise requests submitted between market close and midnight will be rejected to avoid any confusion about when the exercise will settle.

Endpoint: `POST /v2/positions/{symbol_or_contract_id}/exercise`(no body)

More details in our OpenAPI Spec [here](https://docs.alpaca.markets/v1.1/reference/optionexercise).

## Do Not Exercise

To submit a Do-not-exercise (DNE) instruction, please contact our support team.

# Expiration

* In the event no instruction is provided on an ITM contract, the Alpaca system will exercise the contract as long as it is ITM by at least $0.01 USD.
* Alpaca Operations has tooling and processes in place to identify accounts which pose a buying power risk with ITM contracts.
* In the event the account does not have sufficient buying power to exercise an ITM position, Alpaca will sell-out the position within 1 hour before expiry.

# Assignment

Options assignments are not delivered through websocket events. To check for assignment activity (non-trade activity, or NTA events), you’ll need to poll the REST API endpoints. Websocket support for NTAs is not currently available.

# FAQ

Please see our full FAQs here: <https://alpaca.markets/support/tag/options>

Updated about 2 months ago

---

Ask AI

---

# Options Orders (https://docs.alpaca.markets/docs/options-orders)

# Options Orders

This page provides examples of valid order payloads

# Tier 1 Orders

## Sell a Covered Call

```
{
  "symbol": "AAPL231201C00195000",
  "qty": "2",
  "side": "sell",
  "type": "limit",
  "limit_price": "1.05",
  "time_in_force": "day"
}
```

Note, the account must have an existing position of 200 shares of AAPL as the order is for 2 contracts, and each option contract is for 100 shares of underlying.

## Sell a Cash-Secured Put

```
{
  "symbol": "AAPL231201P00175000",
  "qty": "1",
  "side": "sell",
  "type": "market",
  "time_in_force": "day"
}
```

Note, the account must have sufficient buying power. The account must have ($175 strike) x (100 shares) x (1 contract) = $17,500 USD buying power available.

# Tier 2 Orders

## Buy a Call

```
{
  "symbol": "AAPL240119C00190000",
  "qty": "1",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

The account must have sufficient buying power to afford the call option. If the market order is executed at $5.10, the account must have ($5.10 execution price) x (100 shares) x (1 contract) = $510.00 USD buying power.

## Buy a Put

```
{
  "symbol": "AAPL240119P00170000",
  "qty": "1",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

The account must have sufficient buying power to afford purchasing put option. If the market order is executed at $1.04, the account must have ($1.04 execution price) x (100 shares) x (1 contract) = $104.00 USD buying power.

Updated 5 months ago

---

Ask AI

---

# Options Level 3 Trading (https://docs.alpaca.markets/docs/options-level-3-trading)

# Options Level 3 Trading

We're excited to support Multi-leg options trading! Use this section to read up on Alpaca's Multi-leg options trading capabilities.

> 🎉
>
> ### Multi-leg options trading is now available for live trading!

## What are Multi-leg Orders?

A multi-leg (MLeg) order is a single, combined order that includes multiple option contracts – calls, puts, or even shares—on the same underlying security. By bundling all legs together, the trade is executed as a single unit and each leg is associated with its own strike price, expiration date, or position type (long or short). MLeg orders are often used when traders need to set up complex strategies with several moving parts. A common example is the call spread, where the trader buys a call option at one strike price while simultaneously selling another call option at a higher strike, both for the same underlying asset.

## Why are Multi-leg Orders useful?

MLeg orders are particularly useful because they allow traders to execute complex options or stock combinations in one streamlined process, avoiding the delay or slippage risk of placing each transaction separately. By handling multiple legs at once, traders gain better control over their target price, reduce the chance of partial fills that could distort the intended strategy, and simplify trade management. The potential to minimize transaction costs—whether through tighter spreads, combined commissions, or efficient margin usage, also adds to their appeal.

A trader anticipates a stock will remain in a narrow price range.  
They set up an iron condor, which involves four legs:

* Buying one out-of-the-money (OTM) call.
* Selling a call at a closer strike.
* Buying an OTM put.
* Selling another put.

Placing these four legs as a single MLeg order ensures they fill together or not at all.  
This reduces the risk of partial fills, which could otherwise leave the trader with unwanted market exposure or unbalanced positions.

## How to submit a Multi-leg Order?

To submit a multi-leg (MLeg) order, set your “order\_class” to “mleg” and list each component of the strategy in a “legs” array, specifying details like the symbol, side (buy or sell), ratio quantity, and position intent (e.g., buy\_to\_open). Include any additional parameters (limit price, time in force, etc.) as part of the order’s settings. Below is a cURL example showing how to place a POST request to the Alpaca API, passing in the necessary headers and JSON payload:

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "0.6",
  "time_in_force": "day",
  "legs": [
    {"symbol": "AAPL250117P00200000", "ratio_qty": "1", "side": "buy", "position_intent": "buy_to_open"},
    {"symbol": "AAPL250117C00250000", "ratio_qty": "1", "side": "buy", "position_intent": "buy_to_open"}
  ]
}' | jq -r
```

## Some examples

### Long Call Spread

![](https://files.readme.io/444efc02ec4fecfc528035df0c4dabacf34a9082a46b08af4de56859ef498e02-long_call_spread.png)

Buy a lower-strike (190) call and sell a higher-strike (210) call on the same underlying:

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "1.00",
  "time_in_force": "day",
  "legs": [
    {
      "symbol": "AAPL250117C00190000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    },
    {
      "symbol": "AAPL250117C00210000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    }
  ]
}' | jq -r
```

### Long Put Spread

![](https://files.readme.io/a807ae88d756237e9fc54b29b2c0bcfa4d24c0013becbfbda70244f2144082f8-long_put_spread.png)

Buy a higher-strike (210) put and sell a lower-strike (190) put on the same underlying:

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "1.25",
  "time_in_force": "day",
  "legs": [
    {
      "symbol": "AAPL250117P00210000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    },
    {
      "symbol": "AAPL250117P00190000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    }
  ]
}' | jq -r
```

### Iron Condor

![](https://files.readme.io/f86f771f0b68ce6af0706ba6e7a6d308af0678bbf3d71c23027722c600d67854-iron_condor.png)

Combine two spreads (a put spread and a call spread) to bet on limited movement:

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "1.80",
  "time_in_force": "day",
  "legs": [
    {
      "symbol": "AAPL250117P00190000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    },
    {
      "symbol": "AAPL250117P00195000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    },
    {
      "symbol": "AAPL250117C00205000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    },
    {
      "symbol": "AAPL250117C00210000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    }
  ]
}' | jq -r
```

Learn about the [differences between an iron condor and iron butterfly](https://alpaca.markets/learn/iron-condor-vs-iron-butterfly).

### Roll a Call Spread (strike price)

Close an existing short call spread and open a new one at different strikes in a single transaction:

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "2.05",
  "time_in_force": "day",
  "legs": [
    {
      "symbol": "AAPL250117C00200000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_close"
    },
    {
      "symbol": "AAPL250117C00205000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_close"
    },
    {
      "symbol": "AAPL250117C00210000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    },
    {
      "symbol": "AAPL250117C00215000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    }
  ]
}' | jq -r
```

### Roll a Call Spread (expiration date)

Below is an example of rolling a short call spread from one expiration date to another in a single multi-leg (MLeg) order. The first two legs (with symbols ending in `250117`) are closed (`buy_to_close` and `sell_to_close`), and the new positions are opened at later-dated strikes (`250224`):

cURL

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "order_class": "mleg",
  "qty": "1",
  "type": "limit",
  "limit_price": "2.05",
  "time_in_force": "day",
  "legs": [
    {
      "symbol": "AAPL250117C00200000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_close"
    },
    {
      "symbol": "AAPL250117C00205000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_close"
    },
    {
      "symbol": "AAPL250124C00200000",
      "ratio_qty": "1",
      "side": "sell",
      "position_intent": "sell_to_open"
    },
    {
      "symbol": "AAPL250124C00205000",
      "ratio_qty": "1",
      "side": "buy",
      "position_intent": "buy_to_open"
    }
  ]
}' | jq -r
```

## Some deeper explanations

### How do we calculate maintenance margin requirements?

1. **Ignore Premiums**  
   When calculating maintenance margin, do not factor in the premiums paid or received. Instead, focus on the intrinsic (exercise) payoffs.
2. **Model Each Option’s Payoff**  
   Each option is represented by a piecewise linear payoff function (PnL) based on the underlying price (p).

   ![](https://files.readme.io/32286a51ed97659a53b176cec7edbe0df282c76a42831ac7f81dc7bf80c4d26d-Screenshot_2025-01-20_at_19.01.45.png)
3. **Combine Positions**  
   To determine total payoff, sum the piecewise functions for all open positions:

   ![](https://files.readme.io/995133508c4fd0176faf1c370ba26aa1444b74719ecbb3e3d6ec4cb2d3b8f77a-Screenshot_2025-01-20_at_19.05.08.png)
4. **Find Theoretical Maximum Loss**  
   Maintenance margin is based on the worst-case scenario for the portfolio:

   ![](https://files.readme.io/66772ec029ae5859d8c97d2e063ea2893faa9c0c794c8593ee2af5f7fe514111-Screenshot_2025-01-20_at_19.04.45.png)

In other words, you determine the underlying price p that yields the lowest (most negative) net payoff. The absolute value of this lowest point is the margin requirement.

5. **Different Expirations**  
   For option positions with multiple expiration dates, calculate this theoretical maximum-loss approach separately for each expiration date, then use the largest resulting requirement across all expirations.

Lets see an example in order to understand why this way of calculating the maintenance margin is benefiting the customers.

Lets assume that a customer has the following positions

* Long Call for AAPL with Strike Price = 100
* Short Call for AAPL with Strike Price = 110
* Long Call for AAPL with Strike Price = 200
* Short Call for AAPL with Strike Price = 190

Using the traditional way of calculating maintenance margin we would form 2 spreads

Spread 1 (Call Credit Spread):

* Long Call for AAPL with Strike Price = 200
* Short Call for AAPL with Strike Price = 190

![](https://files.readme.io/12a13471e5bdfaeb7669cac5d145b9f5ed1c7545b93c82999a38c447bde6f158-call_spread_1.png)

With maintenance margin = 1000 since the difference between strike prices is 10 and the option’s multiplier is 100 so the `maintenance_margin = strike_price_diff * multiplier`

Spread 2 (Call Debit Spread):

* Long Call for AAPL with Strike Price = 100
* Short Call for AAPL with Strike Price = 110

![](https://files.readme.io/ec7e1a5000f960cb984d595becc471067bafb8b8fa597cc08f15ac986c64aa88-call_spread_2.png)

With maintenance margin = 0 since the difference between strike prices is 10 but the long is higher than the short.

So the **Total Maintenance Margin (Traditional) = 1000 + 0 = $1000**

**Universal Spread Rule Calculation**

When combining all four positions and evaluating the theoretical maximum combined loss, the payoff analysis shows that losses from one spread offset gains or losses in the other, resulting in a net theoretical maximum loss of zero. Hence:

* **Total Maintenance Margin (Universal Spread) = $0**

![](https://files.readme.io/e30a3e59350972901aed6ff30df3409cba7f8115e4b88df66a9c33dfa8337bec-2_call_spreads.png)

This “universal spread rule” or piecewise-payoff approach better reflects the true risk when these positions are considered together. By recognizing how the different calls offset one another’s exposures, the required margin is lower—benefiting the customer by aligning margin requirements with the actual worst-case scenario of the entire portfolio rather than assigning sums of individual spreads.

---

References:  
<https://cdn.cboe.com/resources/membership/Margin_Manual.pdf>

*First, compute the intrinsic value of the options at price points for the underlying security or instrument that are set to correspond to every exercise price present in the spread. Then, net the intrinsic values at each price point. The maximum potential loss is the greatest loss, if any, from among the results.*

<https://cdn.cboe.com/resources/regulation/rule_filings/margin_requirements/SR-CBOE-2012-043.pdf>

*(A) For spreads as defined in subparagraph (a)(5) of this Rule, the long options  
must be paid for in full. In addition, margin is required equal to the lesser of the  
amount required for the short option(s) by subparagraph (c)(5)(A) or (B),  
whichever is applicable, or the spread’s maximum potential loss, if any. To  
determine the spread’s maximum potential loss, first compute the intrinsic value  
of the options at price points for the underlying security or instrument that are set  
to correspond to every exercise price present in the spread. Then, net the intrinsic  
values at each price point. The maximum potential loss is the greatest loss, if any,  
from among the results. The proceeds for establishing the short options may be  
applied toward the cost of the long options and/or any margin requirement.*

---

### How do we calculate order cost basis?

**Definition:**

The **cost basis** of a multi-leg (MLeg) order is the **sum of**:

1. The **maintenance margin** required for the combined positions (as determined by the universal spread rule), and
2. The **net price** (debit/credit) from buying or selling the option contracts.

**Example:**

Consider a call credit spread on AAPL:

* Long Call (buy) for AAPL with Strike Price = 200
* Short Call (sell) for AAPL with Strike Price = 190

**Maintenance Margin:** Universal spread rule requires a margin of $1,000 for this spread.

**Net Option Price:**

* The **long call** premium to be paid is $10 (cost to the buyer).
* The **short call** premium to be received is $15 (credit to the seller).
* **Net Price** = (15−10)=(15 - 10) =$5 credit
* Because each option contract covers 100 shares, multiply by 100:  
  Net Price (per contract) x 100 = 5 x 100 = $500
* However, for cost-basis purposes, a credit (positive $5) effectively reduces the overall cost, so it becomes **-$5** in the order’s net debit/credit calculation.

So, Total Cost Basis:  
Cost Basis = (Maintenance Margin) + (Net Price×Option Multiplier) = 1000 + (-5 x 100) = 1000 - 500 = $500

Hence, the cost basis—and the amount charged to the customer—for this multi-leg order is $500.

### Some Edge Scenarios

#### GCD `ratio_qty` requirement

When submitting an MLeg order, each leg’s `leg_ratio` must be in its simplest form. In other words, the greatest common divisor (GCD) among the `leg_ratio` values for the legs must be 1.

**Example** (wrong)

* Leg 1: `leg_ratio = 4`
* Leg 2: `leg_ratio = 2`

Because both ratios share a common divisor of 2, the system will reject this order. If a ratio must be 2:4, for instance, the user should enter it as 1:2 instead (dividing both sides by the GCD of 2).

**Reason for Enforcing Simplified Ratios**

By requiring that leg ratios be in their simplest form (prime to each other), the system can:

**Avoid Redundant Parent Quantities**: The ratio is intended to show the relative proportions of each leg; if the ratio isn’t simplified, you’re effectively duplicating the same information already available through the parent order quantity.

This approach ensures clarity in trade definitions and prevents potential confusion or errors in calculating fill quantities and margin requirements.

#### Restrictions on Combo Order(equity leg + contract leg)

MLeg orders that include an equity leg are not supported at this time. This means that combining an equity position with an options contract in a single order is not currently available for any trading strategy.

#### MLeg restrictions regarding uncovered legs

Starting on day zero of Options Level 3 trading, an MLeg order is accepted only if all its legs are covered within the same MLeg order. For example, an MLeg order containing two short call legs would be rejected, though submitting those short calls separately as single-leg orders is allowed. This restriction also impacts certain strategies, including rolling a short contract or rolling a calendar spread, since they would involve uncovered short legs within the same multi-leg order.

---

*The content of this article is for general informational purposes only. All examples are for illustrative purposes only.*

*Options trading is not suitable for all investors due to its inherent high risk, which can potentially result in significant losses. Please read[Characteristics and Risks of Standardized Options](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document) before investing in options.*

*All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.*

*Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member[FINRA/SIPC](https://www.finra.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.*

*This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities are not registered or licensed, as applicable.*

Updated 5 months ago

---

Ask AI

---

# Non-Trade Activities for Option Events (https://docs.alpaca.markets/docs/non-trade-activities-for-option-events)

# Non-Trade Activities for Option Events

This page provides an overview of new NTAs for options-specific events

# Option Exercise

```
[
  {
    "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
    "activity_type": "OPEXC",
    "date": "2023-07-21",
    "net_amount": "0",
    "description": "Option Exercise",
    "symbol": "AAPL230721C00150000",
    "qty": "-2",
    "status": "executed"
  },
  {
      "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
      "activity_type": "OPTRD",
      "date": "2023-07-21",
      "net_amount": "-30000",
      "description": "Option Trade",
      "symbol": "AAPL",
      "qty": "200",
      "price": "90",
      "status": "executed"
    }
]
```

The exercise event (OPEXC) is applicable to 2 contracts, and the corresponding trade (OPTRD) represents 200 of the underlying shares being purchased at a per-share amount of $150 (strike price).

# Option Assignment

```
[
    {
      "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
      "activity_type": "OPASN",
      "date": "2023-07-01",
      "net_amount": "0",
      "description": "Option Assignment",
      "symbol": "AAPL230721C00150000",
      "qty": "2",
      "status": "executed"
    },
    {
      "activity_type": "OPTRD",
      "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
      "date": "2023-07-01",
      "net_amount": "30000",
      "description": "Option Trade",
      "symbol": "AAPL",
      "qty": "-200",
      "price": "150",
      "status": "executed"
    }
]
```

The assignment event (OPASN) is applicable to 2 contracts, and the corresponding trade (OPTRD) represents 200 of the underlying shares being sold at a per-share amount of $150 (strike price).

# ITM Option Expiry

In the event of an in-the-money (ITM) option reaching expiration without being designated as "Do Not Exercise" (DNE), the Alpaca system will automatically initiate the exercise process on behalf of the user. This process mirrors the Exercise event described earlier. In cases where there is insufficient buying power or underlying positions to facilitate the exercise, the system will generate an automated order for the liquidation of the position.

# OTM Option Expiry

```
[
  {
    "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
    "activity_type": "OPEXP",
    "date": "2023-07-21",
    "net_amount": "0",
    "description": "Option Expiry",
    "symbol": "AAPL230721C00150000",
    "qty": "-2",
    "status": "executed"
  }
]
```

When a contract expires OTM, the Alpaca system will flatten the position and no further action is taken.

Updated 5 months ago

---

Ask AI

---

# Account Activities (https://docs.alpaca.markets/docs/account-activities)

# Account Activities

The account activities API provides access to a historical record of transaction activities that have impacted your account.

# The TradeActivity Object

## Sample TradeActivity

JSON

```
{
  "activity_type": "FILL",
  "cum_qty": "1",
  "id": "20190524113406977::8efc7b9a-8b2b-4000-9955-d36e7db0df74",
  "leaves_qty": "0",
  "price": "1.63",
  "qty": "1",
  "side": "buy",
  "symbol": "LPCN",
  "transaction_time": "2019-05-24T15:34:06.977Z",
  "order_id": "904837e3-3b76-47ec-b432-046db621571b",
  "type": "fill"
}
```

## Properties

| Attribute | Type | Description |
| --- | --- | --- |
| `activity_type` | string | For trade activities, this will always be `FILL` |
| `cum_qty` | string<number> | The cumulative quantity of shares involved in the execution. |
| `id` | string | An ID for the activity. Always in `::` format. Can be sent as `page_token` in requests to facilitate the paging of results. |
| `leaves_qty` | string<number> | For `partially_filled` orders, the quantity of shares that are left to be filled. |
| `price` | string<number> | The per-share price that the trade was executed at. |
| `qty` | string<number> | The number of shares involved in the trade execution. |
| `side` | string | `buy` or `sell` |
| `symbol` | string | The symbol of the security being traded. |
| `transaction_time` | string<timestamp> | The time at which the execution occurred. |
| `order_id` | string<uuid> | The id for the order that filled. |
| `type` | string | `fill` or `partial_fill` |

# The NonTradeActivity (NTA) Object

## Sample NTA

JSON

```
{
  "activity_type": "DIV",
  "id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
  "date": "2019-08-01",
  "net_amount": "1.02",
  "symbol": "T",
  "cusip": "C00206R102",
  "qty": "2",
  "per_share_amount": "0.51"
}
```

## Properties

| Attribute | Type | Description |
| --- | --- | --- |
| `activity_type` | string | See below for a list of possible values. |
| `id` | string | An ID for the activity. Always in `::` format. Can be sent as `page_token` in requests to facilitate the paging of results. |
| `date` | string<timestamp> | The date on which the activity occurred or on which the transaction associated with the activity settled. |
| `net_amount` | string<number> | The net amount of money (positive or negative) associated with the activity. |
| `symbol` | string | The symbol of the security involved with the activity. Not present for all activity types. |
| `cusip` | string | The CUSIP of the security involved with the activity. Not present for all activity types. |
| `qty` | string<number> | For dividend activities, the number of shares that contributed to the payment. Not present for other activity types. |
| `per_share_amount` | string<number> | For dividend activities, the average amount paid per share. Not present for other activity types. |

# Pagination of Results

Pagination is handled using the `page_token` and `page_size` parameters.

`page_token` represents the ID of the end of your current page of results. If specified with a direction of desc, for example, the results will end before the activity with the specified ID. If specified with a direction of `asc`, results will begin with the activity immediately after the one specified. `page_size` is the maximum number of entries to return in the response. If `date` is not specified, the default and maximum value is 100. If `date` is specified, the default behavior is to return all results, and there is no maximum page size.

# Activity Types

| `activity_type` | Description |
| --- | --- |
| `FILL` | Order fills (both partial and full fills) |
| `TRANS` | Cash transactions (both CSD and CSW) |
| `MISC` | Miscellaneous or rarely used activity types (All types except those in TRANS, DIV, or FILL) |
| `ACATC` | ACATS IN/OUT (Cash) |
| `ACATS` | ACATS IN/OUT (Securities) |
| `CFEE` | Crypto fee |
| `CSD` | Cash deposit(+) |
| `CSW` | Cash withdrawal(-) |
| `DIV` | Dividends |
| `DIVCGL` | Dividend (capital gain long term) |
| `DIVCGS` | Dividend (capital gain short term) |
| `DIVFEE` | Dividend fee |
| `DIVFT` | Dividend adjusted (Foreign Tax Withheld) |
| `DIVNRA` | Dividend adjusted (NRA Withheld) |
| `DIVROC` | Dividend return of capital |
| `DIVTW` | Dividend adjusted (Tefra Withheld) |
| `DIVTXEX` | Dividend (tax exempt) |
| `FEE` | Fee denominated in USD |
| `FOPT` | Free of Payment Transfer |
| `INT` | Interest (credit/margin) |
| `INTNRA` | Interest adjusted (NRA Withheld) |
| `INTTW` | Interest adjusted (Tefra Withheld) |
| `JNL` | Journal entry |
| `JNLC` | Journal entry (cash) |
| `JNLS` | Journal entry (stock) |
| `MA` | Merger/Acquisition |
| `NC` | Name change |
| `OPASN` | Option assignment |
| `OPEXP` | Option expiration |
| `OPXRC` | Option exercise |
| `PTC` | Pass Thru Charge |
| `PTR` | Pass Thru Rebate |
| `REORG` | Reorg CA |
| `SC` | Symbol change |
| `SSO` | Stock spinoff |
| `SSP` | Stock split |

Updated 18 days ago

---

Ask AI

---

# Fractional Trading (https://docs.alpaca.markets/docs/fractional-trading)

# Fractional Trading

Fractional shares are fractions of a whole share, meaning that you don’t need to buy a whole share to own a portion of a company. You can now buy as little as $1 worth of shares for over 2,000 US equities.

By default all Alpaca accounts are allowed to trade fractional shares in both live and paper environments. Please make sure you reset your paper account if you run into any issues dealing with fractional shares.

# Supported Order Types

Alpaca currently supports fractional trading for market, limit, stop & stop limit orders with a time in force=Day, accommodating both fractional quantities and notional values. You can pass either a fractional amount (qty), or a notional value (notional) in any POST/v2/orders request. Note that entering a value for either parameters, will automatically nullify the other. If both qty and notional are entered the request will be rejected with an error status 400.

Both notional and qty fields can take up to 9 decimal point values.

Moreover, we support fractional shares trading not only during standard market hours, but extending into pre-market (4:00 a.m. - 9:30 a.m. ET), post-market (4:00 p.m. - 8:00 p.m. ET) and overnight (8:00 p.m. - 4:00 a.m.) hours, offering global investors the ability to trade during the full extended hours session.

# Eligible Securities

Only exchange-listed securities are eligible to trade in the extended hours. Additionally, the asset must be enabled as a fractional asset on Alpaca’s side. If there is an asset you want to trade in the extended hours and it is not eligible, please contact our [support](/cdn-cgi/l/email-protection#25565055554a5751654449554446440b4844574e405156) team.

# Sample Requests

## Notional Request

JSON

```
{
  "symbol": "AAPL",
  "notional": 500.75,
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

## Fractional Request

JSON

```
{
  "symbol": "AAPL",
  "qty": 3.654,
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

# Supported Assets

Not all assets are fractionable yet so please make sure you query assets details to check for the parameter `fractionable = true`.

Supported fractionable assets would return a response that looks like this

JSON

```
{
  "id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
  "class": "us_equity",
  "exchange": "NASDAQ",
  "symbol": "AAPL",
  "name": "Apple Inc. Common Stock",
  "status": "active",
  "tradable": true,
  "marginable": true,
  "shortable": true,
  "easy_to_borrow": true,
  "fractionable": true
}
```

If you request a fractional share order for a stock that is not yet fractionable, the order will get rejected with an error message that reads `requested asset is not fractionable`.

# Dividends

Dividend payments occur the same way in fractional shares as with whole shares, respecting the proportional value of the share that you own.

For example if the dividend amount is $0.10 per share and you own 0.5 shares of that stock then you will receive $0.05 as dividend. As a general rule of thumb all dividends are rounded to the nearest penny.

# Notes on Fractional Trading

* We do not support short sales in fractional orders. All fractional sell orders are marked long.
* The expected price of fill is the NBBO quote at the time the order was submitted. If you submit an order for a whole and fraction, the price for the whole share fill will be used to price the fractional portion of the order.
* Day trading fractional shares counts towards your day trade count.
* You can cancel a fractional share order that is pending, the same way as whole share orders.
* Limit orders are supported for both fractional and notional orders. Extended hours are also supported with limit orders (same as whole share orders).
* Fees for fractional trading work the same way as with whole shares.

Alpaca does not make recommendations with regard to fractional share trading, whether to use fractional shares at all, or whether to invest in any specific security. A security’s eligibility on the list of fractional shares available for trading is not an endorsement of any of the securities, nor is it intended to convey that such stocks have low risk. Fractional share transactions are executed either on a principal or riskless principal basis, and can only be bought or sold with market orders during normal market hours.

Updated 5 months ago

---

Ask AI

---

# Margin and Short Selling (https://docs.alpaca.markets/docs/margin-and-short-selling)

# Margin and Short Selling

> In order to trade on margin or sell short, you must have $2,000 or more account equity. Accounts with less than $2,000 will not have access to these features and will be restricted to 1x buying power.
>
> This is only for Equities Trading. Margin Trading for Crypto is not applicable. In addition, PDT checks do not count towards crypto orders or fills.

# How Margin Works

Trading on margin allows you to trade and hold securities with a value that exceeds your account equity. This is made possible by funds loaned to you by your broker, who uses your account’s cash and securities as collateral. For example, a Reg T Margin Account holding $10,000 cash may purchase and hold up to $20,000 in marginable securities overnight (Note: some securities may have a higher maintenance margin requirement making the full 2x overnight buying power effectively unavailable). In addition to the 2x buying power afforded to margin accounts, a Reg T Margin Account flagged as a Pattern Day Trader(PDT) with $25,000 or greater equity will further be allowed to use up to 4x intraday buying power. As an example, a PDT account holding $50,000 cash may purchase and hold up to $200,000 in securities intraday; however, to avoid receiving a margin call the next morning, the securities held would need to be reduced to $100,000 or less depending on the maintenance margin requirement by the end of the day.

## Initial Margin

Initial margin denotes the percentage of the trade price of a security or basket of securities that an account holder must pay for with available cash in the margin account, additions to cash in the margin account or other marginable securities.

Alpaca applies a minimum initial margin requirement of 50% for marginable securities and 100% for non-marginable securities per Regulation T of the Federal Reserve Board.

## Maintenance Margin

Maintenance margin is the amount of cash or marginable securities required to continue holding an open position. FINRA has set the minimum maintenance requirement to at least 25% of the total market value of the securities, but brokers are free to set higher requirements as part of their risk management.

Alpaca uses the following table to calculate the overnight maintenance margin applied to each security held in an account:

| Position Side | Condition | Margin Requirement |
| --- | --- | --- |
| LONG | share price < $2.50 | 100% of EOD market value |
| LONG | share price >= $2.50 | 30% of EOD market value |
| LONG | 2x Leveraged ETF | 50% of EOD market value |
| LONG | 3x Leveraged ETF | 75% of EOD market value |
| SHORT | share price < $5.00 | Greater of $2.50/share or 100% |
| SHORT | share price >= $5.00 | Greater of $5.00/share or 30% |

## Margin Calls

If your account does not satisfy its initial and maintenance margin requirements at the end of the day, you will receive a margin call the following morning. We will contact you and advise you of the call amount that you will need to satisfy either by depositing new funds or liquidating some or all of your positions to reduce your margin requirement sufficiently.

We may contact you prior to the end of the day and ask you to liquidate your positions immediately in the event that your account equity is materially below your maintenance requirement. Furthermore, although we will make every effort to contact you so that you can determine how to best resolve your margin call, we reserve the right to liquidate your holdings in the event we cannot get ahold of you and your account equity is in danger of turning negative.

Calculating and tracking your margin requirement at all times is helpful to avoid receiving a margin call. We strongly recommend doing so if you plan to aggressively use overnight leverage. Please use a 50% initial requirement and refer to the maintenance margin table above. In the future, we will provide real-time estimated initial and maintenance margin values as part of the Account API to help users better manage their risk.

# Margin Interest Rate

We are pleased to offer a competitive and low annual margin interest rate of 4.75% for elite users and 6.25% for non-elite users (check “Alpaca Securities Brokerage Fee Schedule” on **Important Disclosures** for the latest rate).

The rate is charged only on your account’s end of day (overnight) debit balance using the following calculation:

`daily_margin_interest_charge = (settlement_date_debit_balance * rate[non-elite: 0.0625 | elite: 0.0475])) / 360`

Interest will accrue daily and post to your account at the end of each month. Note that if you have a settlement date debit balance as of the end of day Friday, you will incur interest charges for 3 days (Fri, Sat, Sun).

As an example, if you are a regular trader and deposited $10,000 into your account and bought $15,000 worth of securities that you held at the end of the day, you would be borrowing $5,000 overnight and would incur a daily interest expense of ($5000 \* 0.0625) / 360 = $0.87.

On the other hand, if you deposited $10,000 and bought $15,000 worth of stock that you liquidated the same day, you would not incur any interest expense. In other words, this allows you to make use of the additional buying power for intraday trading without any cost.

# Stock Borrow Rates

Alpaca currently only supports opening short positions in easy to borrow (“ETB”) securities. Any open short order in a stock that changes from ETB to hard to borrow (“HTB”) overnight will be automatically cancelled prior to market open.

**Note: Support for HTB securities is not yet available, but we are actively working towards supporting HTB in the future.**

**In addition, Alpaca has introduced $0 borrow fees on all ETB (easy-to-borrow) shares for Trading API users.**

Please note that stock borrow availability changes daily, and we update our assets table each morning, so please use our API to check each stock’s borrow status daily. It is infrequent but names can go from ETB → HTB and vice versa.
While we do not currently support opening short positions in HTB securities, we will not force you to close out a position in a stock that has gone from ETB to HTB unless the lender has called the stock. If a stock you hold short has gone from ETB to HTB, you will incur a daily stock borrow fee for that stock. We do not currently provide HTB rates via our API, so please contact us in these cases.

If you hold an HTB short at any time during the day, you will incur a daily stock borrow fee:

`Daily stock borrow fee = Daily HTB stock borrow fee`

Where,

`Daily HTB stock borrow fee = Σ((each stock’s HTB short $ market value _ that stock’s HTB rate) / 360)`

Please note that if you hold HTB short positions as of a Friday settlement date, you will incur stock borrow fees for 3 days (Fri, Sat, Sun). HTB stock borrow fees are charged in the nearest round lot (100 shares), regardless of the actual number of shares shorted. This is because stocks are borrowed in round lots.

# Concentrated Margin Requirements

Accounts concentrated into a single position will see an increased maintenance margin rate on the symbol in which the account is concentrated.

1. Concentration is defined as a single security accounting for 70% of the market value of equities and the account is carrying a margin balance of $100,000 or more.
2. The Maintenance Margin Rate on the concentrated position will increase to 50%.

---

**Margin trading involves significant risk and is not suitable for all investors.** Before considering a margin loan, it is crucial that you carefully consider how borrowing fits with your investment objectives and risk tolerance.
When trading on margin, you assume higher market risk, and potential losses can exceed the collateral value in your account. Alpaca may sell any securities in your account, without prior notice, to satisfy a margin call. Alpaca may also change its “house” maintenance margin requirements at any time without advance written notice. You are not entitled to an extension of time on a margin call. Please review the Firm’s [Margin Disclosure Statement](https://files.alpaca.markets/disclosures/library/MarginDiscStmt.pdf) before investing.

Updated 2 months ago

---

Ask AI

---

# Placing Orders (https://docs.alpaca.markets/docs/orders-at-alpaca)

# Placing Orders

Using Alpaca's Trading API, users can monitor, place, and cancel orders. Each order has a unique identifier provided by the client. If the client does not provide one, the system will automatically generate a client-side unique order ID. This ID is returned as part of the order object, along with the other fields described below. Once an order is placed, it can be queried using either the client-provided order ID or the system-assigned unique ID to check its status. Updates on open orders are also delivered through the streaming interface, which is the recommended method for maintaining order state.

# Buying Power

To accept orders that open new positions or add to existing ones, your account must have sufficient buying power. Alpaca applies a buying power check to both long buys and short sells.

The calculated value of an opening short sell order is MAX(order’s limit price, 3% above the current ask price) \* order quantity. For market short orders, the value is simply (3% above the current ask price) \* order quantity.

The order’s calculated value is then compared against your available buying power to determine whether it can be accepted. Note that your available buying power is reduced by existing open buy long and sell short orders. Your sell long and buy to cover orders do not replenish your available buying power until they are executed.

For example, if your buying power is $10,000 and you submit a limit buy order with a value of $3,000, the order will be accepted and your remaining available buying power will be $7,000. Even if the order remains unfilled, it will continue to count against your available buying power until it is either executed or canceled. If you then submit another order with a value of $8,000, it will be rejected.

**Initial buying power checks on orders:**

When the core session is open: Far side of the NBBO (using Bid & Ask Price)

If the order is entered while the extended hours session is open: Midpoint of the inside market

If the order is entered when the core session and extended hours session are closed (pre-market hours): the latest trade from market cache

# Equities Trading

The following section deals with equity trading

## Orders Submitted Outside of Eligible Trading Hours

Orders not eligible for extended hours submitted after 4:00pm ET will be queued up for release the next trading day.

Orders eligible for extended hours submitted outside of 4:00am - 8:00pm ET are handled as described in the section below.

## Extended Hours Trading

Using API v2, you can submit and fill orders during pre-market and after-hours. Extended hours trading has specific risks due to the less liquidity. Please read through [Alpaca’s Extended Hours Trading Risk Disclosure](https://files.alpaca.markets/disclosures/library/ExtHrsRisk.pdf) for more details.

Currently, we support full extended hours:

* Overnight: 8:00pm - 4:00am ET, Sunday to Friday
* Pre-market: 4:00am - 9:30am ET, Monday to Friday
* After-hours: 4:00pm - 8:00pm ET, Monday to Friday

### Submitting an Extended Hours Eligible Order

To indicate an order is eligible for extended hours trading, you need to supply a boolean parameter named `extended_hours` to your order request. By setting this parameter to `true`, the order is will be eligible to execute in the pre-market or after-hours.

Only limit orders with a `time_in_force` = `day` orders will be accepted as extended hours eligible. All other order types and TIFs will be rejected with an error. You must adhere to these settings in order to participate in extended hours:

1. The order type must be set to `limit` (with a limit price). Any other type of orders will be rejected with an error.
2. Time-in-force must be set to be `day`. Any other `time_in_force` will be rejected with an error.

For Fractional Orders, starting on October 27, 2021, customers will not be able to send the following sequence of orders outside of market hours for the same security. This is so customers will not have a net short position. Examples of the order sequences that will be rejected are shown below.

| Summary | Order 1 | Order 2 | Second Order Handling Accept/Reject |
| --- | --- | --- | --- |
| 2x Sell | Notional Sell | Quantity Sell | Reject |
| 2x Sell | Notional Sell | Notional Sell | Reject |
| 2x Sell | Quantity Sell | Notional Sell | Reject |
| 2 x Sell [with Correct Quantity] | Quantity Sell | Quantity Sell | Accept |
| 2 x Sell [with Correct Quantity] | Quantity Sell | Quantity Sell | Reject |

For more information - please see our [Blog Post](https://alpaca.markets/blog/shorting-prevention-breaking-change-notification/) on this topic.

If this is done you will see the following error message: `"unable to open new notional orders while having open closing position orders"`.

All symbols supported during regular market hours are also supported during extended hours. Short selling is also treated the same. Assets tradable in the overnight session can be identified via the assets endpoint, please see our [24/5 FAQ](https://docs.alpaca.markets/docs/245-trading) for more information

## IPO Symbols

Alpaca supports trading symbols which have recently begun trading publicly on major exchanges such as the NYSE and NASDAQ. This process is known as a company going public, or an IPO.

As a registered broker/dealer, Alpaca must follow FINRA [regulations](https://www.finra.org/rules-guidance/guidance/faqs/finra-rule-5131-frequently-asked-questions) regarding order types for IPO symbols:

* Alpaca is only able to accept `limit` orders prior to the security’s first trade on the exchange
* Once an IPO begins trading on an exchange, `market` orders are accepted

To assist our customers, Alpaca will expose an `attribute` called `ipo` on the [Assets](https://docs.alpaca.markets/reference/getassets) model. The `ipo` attribute will flag to customers that this particular symbol has an IPO coming up, or is just about to begin trading on an exchange, and therefore a `limit` order must be used.

# Order Types

When you submit an order, you can choose one of supported order types. Currently, Alpaca supports four different types of orders.

## Market Order

A market order is a request to buy or sell a security at the currently available market price. It provides the most likely method of filling an order. Market orders fill nearly instantaneously.

As a trade-off, your fill price may slip depending on the available liquidity at each price level as well as any price moves that may occur while your order is being routed to its execution venue. There is also the risk with market orders that they may get filled at unexpected prices due to short-term price spikes.

## Limit Order

A limit order is an order to buy or sell at a specified price or better. A buy limit order (a limit order to buy) is executed at the specified limit price or lower (i.e., better). Conversely, a sell limit order (a limit order to sell) is executed at the specified limit price or higher (better). Unlike a market order, you have to specify the limit price parameter when submitting your order.

While a limit order can prevent slippage, it may not be filled for a quite a bit of time, if at all. For a buy limit order, if the market price is within your specified limit price, you can expect the order to be filled. If the market price is equivalent to your limit price, your order may or may not be filled; if the order cannot immediately execute against resting liquidity, then it is deemed non-marketable and will only be filled once a marketable order interacts with it. You could miss a trading opportunity if price moves away from the limit price before your order can be filled.

### Sub-penny increments for limit orders

The minimum price variance exists for limit orders. Orders received in excess of the minimum price variance will be rejected.

* Limit price >=$1.00: Max Decimals= 2
* Limit price <$1.00: Max Decimals = 4

```
{
  "code": 42210000,
  "message": "invalid limit_price 290.123. sub-penny increment does not fulfill minimum pricing criteria"
}
```

## Stop Orders

A stop (market) order is an order to buy or sell a security when its price moves past a particular point, ensuring a higher probability of achieving a predetermined entry or exit price. Once the order is elected, the stop order becomes a market order. Alpaca converts buy stop orders into stop limit orders with a limit price that is 4% higher than a stop price < $50 (or 2.5% higher than a stop price >= $50). Sell stop orders are not converted into stop limit orders.

A stop order does not guarantee the order will be filled at a certain price after it is converted to a market order.

In order to submit a stop order, you will need to specify the stop price parameter in the API.

**Example:**

* Let's say you want to buy 100 shares of TSLA only if it goes up to $210 (assuming current trading price at $200).
* You place a **buy stop order at $210.**
* In Alpaca, this buy stop order is converted into a **stop-limit order** with a **limit price 2.5%** higher than $210 (**i.e., $215.25**).
* If TSLA reaches **$210**, the order is activated and turns into a **limit order at $215.25**. This means the order will not execute above **$215.25**.

### Sub-penny increments for stop orders

The minimum price variance exists for stop orders. Orders received in excess of the minimum price variance will be rejected.

* Stop price >=$1.00: Max Decimals= 2
* Stop price <$1.00: Max Decimals = 4

```
{
  "code": 42210000,
  "message": "invalid stop_price 290.123. sub-penny increment does not fulfill minimum pricing criteria"
}
```

## Stop Limit Order

A stop-limit order is a conditional trade over a set time frame that combines the features of a stop order with those of a limit order and is used to mitigate risk. The stop-limit order will be executed at a specified limit price, or better, after a given stop price has been reached. Once the stop price is reached, the stop-limit order becomes a limit order to buy or sell at the limit price or better. In the case of a gap down in the market that causes the election of your order, but not the execution, your order will remain active as a limit order until it is executable or cancelled.

In order to submit a stop limit order, you will need to specify both the limit and stop price parameters in the API.

**Example:**

* You want to buy 50 shares of TSLA, currently trading at $200.
* You want to buy only if it breaks above **$210**, but not higher than **$215.**
* You place a buy stop-limit order with:
  + **Stop price: $210** → The order is activated when TSLA reaches this price.
  + **Limit price: $215** → The order will only execute at $215 or better.
* If TSLA moves to **$210**, the order is triggered and converted into a **limit order at $215.**

## Opening and Closing Auction Orders

Market on open and limit on open orders are only eligible to execute in the opening auction. Market on close and limit on close orders are only eligible to execute in the closing auction. Please see the [Time in Force](/docs/orders-at-alpaca#time-in-force) section for more details.

## Bracket Orders

A bracket order is a chain of three orders that can be used to manage your position entry and exit. It is a common use case of an OTOCO (One Triggers OCO {One Cancels Other}) order.

The first order is used to enter a new long or short position, and once it is completely filled, two conditional exit orders are activated. One of the two closing orders is called a take-profit order, which is a limit order, and the other is called a stop-loss order, which is either a stop or stop-limit order. Importantly, only one of the two exit orders can be executed. Once one of the exit orders is filled, the other is canceled. Please note, however, that in extremely volatile and fast market conditions, both orders may fill before the cancellation occurs.

Without a bracket order, you would not be able to submit both entry and exit orders simultaneously since Alpaca’s system only accepts exit orders for existing positions. Additionally, even if you had an open position, you would not be able to submit two conditional closing orders since Alpaca’s system would view one of the two orders as exceeding the available position quantity. Bracket orders address both of these issues, as Alpaca’s system recognizes the entry and exit orders as a group and queues them for execution appropriately.

In order to submit a bracket order, you need to supply additional parameters to the API. First, add a parameter `order_class` as “bracket”. Second, give two additional fields `take_profit` and stop\_loss both of which are nested JSON objects. The `take_profit` object needs `limit_price` as a field value that specifies limit price of the take-profit order, and the `stop_loss` object needs a mandatory `stop_price` field and optional `limit_price` field. If `limit_price` is specified in `stop_loss`, the stop-loss order is queued as a stop-limit order, but otherwise it is queued as a stop order.

An example JSON body parameter to submit a bracket order is as follows.

JSON

```
{
  "side": "buy",
  "symbol": "SPY",
  "type": "market",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "bracket",
  "take_profit": {
    "limit_price": "301"
  },
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "298.5"
  }
}
```

This creates three orders.

* A buy market order for 100 SPY with GTC
* A sell limit order for the same 100 SPY, with limit price = 301
* A sell stop-limit order, with stop price = 299 and limit price = 298.5

The second and third orders won’t be active until the first order is completely filled. Additional bracket order details include:

* If any one of the orders is canceled, any remaining open order in the group is canceled.
* `take_profit.limit_price` must be higher than `stop_loss.stop_price` for a buy bracket order, and vice versa for a sell.
* Both `take_profit.limit_price` and `stop_loss.stop_price` must be present.
* Extended hours are not supported. `extended_hours` must be “false” or omitted.
* `time_in_force` must be `day` or `gtc`.
* Each order in the group is always sent with a DNR/DNC (Do Not Reduce/Do Not Cancel) instruction. Therefore, the order price will not be adjusted and the order will not be canceled in the event of a dividend or other corporate action.
* If the take-profit order is partially filled, the stop-loss order will be adjusted to the remaining quantity.
* Order replacement (`PATCH /v2/orders`) is supported to update `limit_price` and `stop_price`.

Each order of the group is reported as an independent order in GET /v2/orders endpoint. But if you specify additional parameter nested=true, the order response will nest the result to include child orders under the parent order with an array field legs in the order entity.

## OCO Orders

OCO (One-Cancels-Other) is another type of advanced order type. This is a set of two orders with the same side (buy/buy or sell/sell) and currently only exit order is supported. In other words, this is the second part of the bracket orders where the entry order is already filled, and you can submit the take-profit and stop-loss in one order submission.

With OCO orders, you can add take-profit and stop-loss after you open the position, without thinking about those two legs upfront.

In order to submit an OCO order, specify “oco” for the order\_class parameter.

SELLBUY

```
{
  "side": "sell",
  "symbol": "SPY",
  "type": "limit",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "oco",
  "take_profit": {
    "limit_price": "301"
  },
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "298.5"
  }
}
```

```
{
  "side": "buy",
  "symbol": "SPY",
  "type": "limit",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "oco",
  "take_profit":{
    "limit_price": "298"
  },
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "300"
  }
}
```

The type parameter must always be “limit”, indicating the take-profit order type is a limit order. The stop-loss order is a stop order if only `stop_price` is specified, and is a stop-limit order if both `limit_price` and `stop_price` are specified (i.e. `stop_price` must be present in any case). Those two orders work exactly the same way as the two legs of the bracket orders.

Note that when you retrieve the list of orders with the `nested` parameter true, the take-profit order shows up as the parent order while the stop-loss order appears as a child order.

Like bracket orders, order replacement is supported to update limit\_price and stop\_price.

## OTO Orders

OTO (One-Triggers-Other) is a variant of bracket order. It takes one of the take-profit or stop-loss order in addition to the entry order. For example, if you want to set only a stop-loss order attached to the position, without a take-profit, you may want to consider OTO orders.

The order submission is done with the `order_class` parameter be “oto”.

JSON

```
{
  "side": "buy",
  "symbol": "SPY",
  "type": "market",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "oto",
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "298.5"
  }
}
```

Either of `take_profit` or `stop_loss` must be present (the above example is for take-profit case), and the rest of requirements are the same as the bracket orders.

Like bracket orders, order replacement is not supported yet.

### Threshold on stop price of stop-loss orders

For the stop-loss order leg of advanced orders, please be aware the order request can be rejected because of the restriction of the stop\_price parameter value. The stop price input has to be at least $0.01 below (for stop-loss sell, above for buy) than the “base price”. The base price is determined as follows.

* It is the limit price of the take-profit, for OCO orders.
* It is the limit price of the entry order, for bracket or OTO orders if the entry type is limit.
* It is also the current market price for any, of OCO, OTO and bracket.

This restriction is to avoid potential race-conditions in the order handling, but as we improve our system capability, this may be loosened in the future.

## Trailing Stop Orders

Trailing stop orders allow you to continuously and automatically keep updating the stop price threshold based on the stock price movement. You request a single order with a dollar offset value or percentage value as the trail and the actual stop price for this order changes as the stock price moves in your favorable way, or stay at the last level otherwise. This way, you don’t need to monitor the price movement and keep sending replace requests to update the stop price close to the latest market movement.

Trailing stop orders keep track of the highest (for sell, lowest for buy) prices (called high water mark, or hwm) since the order was submitted, and the user-specified trail parameters determine the actual stop price to trigger relative to high water mark. Once the stop price is triggered, the order turns into a market order, and it may fill above or below the stop trigger price.

To submit a trailing stop order, you will set the type parameter to “trailing\_stop”. There are two order submission parameters related to trailing stop, one of which is required when type is “trailing\_stop”.

| field | type | description |
| --- | --- | --- |
| trail\_price | string`<number>` | a dollar value away from the highest water mark. If you set this to 2.00 for a sell trailing stop, the stop price is always `hwm - 2.00`. |
| trail\_percent | string`<number>` | a percent value away from the highest water mark. If you set this to 1.0 for a sell trailing stop, the stop price is always `hwm \* 0.99`. |

One of these values must be set for trailing stop orders. The following is an example of trailing order submission JSON parameter.

JSON

```
{
  "side": "sell",
  "symbol": "SPY",
  "type": "trailing_stop",
  "qty": "100",
  "time_in_force": "day",
  "trail_price": "6.15"
}
```

The Order entity returned from the `GET` method has a few fields related to trailing stop orders.

| field | type | description |
| --- | --- | --- |
| `trail_price` | string`<number>` | This is the same value as specified when the order was submitted. It will be null if this was not specified. |
| `trail_percent` | string`<number>` | This is the same value as specified when the order was submitted. It will be null if this was not specified. |
| `hwm` | string`<number>` | The high water mark value. This continuously changes as the market moves towards your favorable way. |
| `stop_price` | string`<number>` | This is the same as stop price in the regular stop/stop limit orders, but this is derived from `hwm` and trail parameter, and continuously updates as hwmchanges. |

If a trailing stop order is accepted, the order status becomes “new”. While the order is pending stop price trigger, you can update the trail parameter by the PATCH method.

| field | type | description |
| --- | --- | --- |
| `trail` | string`<number>` | The new value of the `trail_price` or `trail_percent` value. Such a replace request is effective only for the order type is “trailing\_stop” before the stop price is hit. Note, you cannot change the price trailing to the percent trailing or vice versa. |

Some notes on trailing stop orders

* Trailing stop will not trigger outside of the regular market hours.
* Valid time-in-force values for trailing stop are “day” and “gtc”.
* Trailing stop orders are currently supported only with single orders. However, we plan to support trailing stop as the stop loss leg of bracket/OCO orders in the future.

Proper use of Trailing Stop orders requires understanding the purpose and how they operate. The primary point to keep in mind with Trailing Stop orders is to ensure the difference between the trailing stop and the price is big enough that typical price fluctuations do not trigger a premature execution.

In fast moving markets, the execution price may be less favorable than the stop price. The potential for such vulnerability increases for GTC orders across trading sessions or stocks experiencing trading halts. The stop price triggers a market order and therefore, it is not necessarily the case that the stop price will be the same as the execution price.

With regard to stock splits, Alpaca reserves the right to cancel or adjust pricing and/or share quantities of trailing stop orders based upon its own discretion. Since Alpaca relies on third parties for market data, corporate actions or incorrect price data may cause a trailing stop to be triggered prematurely.

# Time in Force

> 🚧
>
> ### Crypto Time in Force
>
> For Crypto Trading, Alpaca only supports `gtc`, and `ioc`.
>
> `OPG`, `fok`, `day`, and `CLS` are not supported.

Alpaca supports the following Time-In-Force designations:

| time\_in\_force | description |
| --- | --- |
| `day` | A day order is eligible for execution only on the day it is live. By default, the order is only valid during Regular Trading Hours (9:30am - 4:00pm ET). If unfilled after the closing auction, it is automatically canceled. If submitted after the close, it is queued and submitted the following trading day. However, if marked as eligible for extended hours, the order can also execute during supported extended hours. |
| `gtc` | The order is good until canceled. Non-marketable GTC limit orders are subject to price adjustments to offset corporate actions affecting the issue. We do not currently support Do Not Reduce(DNR) orders to opt out of such price adjustments. |
| `opg` | Use this TIF with a market/limit order type to submit “market on open” (MOO) and “limit on open” (LOO) orders. This order is eligible to execute only in the market opening auction. Any unfilled orders after the open will be cancelled. OPG orders submitted after 9:28am but before 7:00pm ET will be rejected. OPG orders submitted after 7:00pm will be queued and routed to the following day’s opening auction. On open/on close orders are routed to the primary exchange. Such orders do not necessarily execute exactly at 9:30am / 4:00pm ET but execute per the exchange’s auction rules. |
| `cls` | Use this TIF with a market/limit order type to submit “market on close” (MOC) and “limit on close” (LOC) orders. This order is eligible to execute only in the market closing auction. Any unfilled orders after the close will be cancelled. CLS orders submitted after 3:50pm but before 7:00pm ET will be rejected. CLS orders submitted after 7:00pm will be queued and routed to the following day’s closing auction. Only available with API v2. |
| `ioc` | An Immediate Or Cancel (IOC) order requires all or part of the order to be executed immediately. Any unfilled portion of the order is canceled. Only available with API v2. Most market makers who receive IOC orders will attempt to fill the order on a principal basis only, and cancel any unfilled balance. On occasion, this can result in the entire order being cancelled if the market maker does not have any existing inventory of the security in question. |
| `fok` | A Fill or Kill (FOK) order is only executed if the entire order quantity can be filled, otherwise the order is canceled. Only available with API v2. |

## Aged order policy

Alpaca implements an aged order policy that will automatically cancel GTC orders 90 days after creation to manage risk, reduce errors, and help achieve operational efficiency.  
The `List/Get` Orders API endpoint has a field titled `expires_at`, which provides information on the expiration.  
On the `expires_at` date there will be a job that will submit a cancel request to cancel the GTC orders.  
This will take place on the `expires_at` date at 4:15 pm ET. The orders will remain in pending\_cancel until canceled by the execution venue that Alpaca routed the order to for execution.

## Order Types vs Supported Time in Force

This section contains the tables showing time-in-force options for various order types.

***Note**: Please contact the sales team for any TIF marked with a\** .

### Whole qty orders (USD)

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | Yes | Yes | Yes | Yes |
| **DAY** | Yes | Yes | Yes | Yes |
| **IOC** | Yes\* | Yes\* | No | No |
| **FOK** | Yes\* | Yes\* | No | No |
| **OPG** | Yes\* | Yes\* | No | No |
| **CLS** | Yes\* | Yes\* | No | No |

### Fractional orders (USD)

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | No | No | No | No |
| **DAY** | Yes | Yes | Yes | Yes |
| **IOC** | No | No | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

### LCT (Whole qty or Fractional)

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | No | No | No | No |
| **DAY** | Yes | Yes | Yes | Yes |
| **IOC** | No | No | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

### Extended Hours orders

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | No | No | No | No |
| **DAY** | No | Yes | No | No |
| **IOC** | No | No | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

### Crypto orders

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | Yes | Yes | No | Yes |
| **DAY** | No | Yes | No | No |
| **IOC** | Yes | Yes | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

### OTC Assets

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | Yes | Yes | Yes | Yes |
| **DAY** | Yes | Yes | Yes | Yes |
| **IOC** | No | No | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

### Options Orders

| Time in Force | Market Order | Limit Order | Stop Order | Stop Limit Order |
| --- | --- | --- | --- | --- |
| **GTC** | No | No | No | No |
| **DAY** | Yes | Yes | No | No |
| **IOC** | No | No | No | No |
| **FOK** | No | No | No | No |
| **OPG** | No | No | No | No |
| **CLS** | No | No | No | No |

# Order Lifecycle

An order executed through Alpaca can experience several status changes during its lifecycle.

![](https://files.readme.io/d7ec892-Order_status_flow.png)

The most common statuses are described in detail below:

| status | description |
| --- | --- |
| `new` | The order has been received by Alpaca, and routed to exchanges for execution. This is the usual initial state of an order. |
| `partially_filled` | The order has been partially filled. |
| `filled` | The order has been filled, and no further updates will occur for the order. |
| `done_for_day` | The order is done executing for the day, and will not receive further updates until the next trading day. |
| `canceled` | The order has been canceled, and no further updates will occur for the order. This can be either due to a cancel request by the user, or the order has been canceled by the exchanges due to its time-in-force. |
| `expired` | The order has expired, and no further updates will occur for the order. |
| `replaced` | The order was replaced by another order, or was updated due to a market event such as corporate action. |
| `pending_cancel` | The order is waiting to be canceled. |
| `pending_replace` | The order is waiting to be replaced by another order. The order will reject cancel request while in this state. |

Less common states are described below. Note that these states only occur on very rare occasions, and most users will likely never see their orders reach these states:

| status | description |
| --- | --- |
| `accepted` | The order has been received by Alpaca, but hasn’t yet been routed to the execution venue. This could be seen often out side of trading session hours. |
| `pending_new` | The order has been received by Alpaca, and routed to the exchanges, but has not yet been accepted for execution. This state only occurs on rare occasions. |
| `accepted_for_bidding` | The order has been received by exchanges, and is evaluated for pricing. This state only occurs on rare occasions. |
| `stopped` | The order has been stopped, and a trade is guaranteed for the order, usually at a stated price or better, but has not yet occurred. This state only occurs on rare occasions. |
| `rejected` | The order has been rejected, and no further updates will occur for the order. This state occurs on rare occasions and may occur based on various conditions decided by the exchanges. |
| `suspended` | The order has been suspended, and is not eligible for trading. This state only occurs on rare occasions. |
| `calculated` | The order has been completed for the day (either filled or done for day), but remaining settlement calculations are still pending. This state only occurs on rare occasions. |

An order may be canceled through the API up until the point it reaches a state of either `filled`, `canceled`, or `expired`.

# Odd Lots and Block Trades

When trading stocks, a round lot is typically defined as 100 shares, or a larger number that can be evenly divided by 100. An odd lot is anything that cannot be evenly divided by 100 shares (e.g. 48, 160, etc.). A block trade is typically defined as a trade that involves 10,000 shares or more.

For trading purposes, odd lots are typically treated like round lots. However, regulatory trading rules allow odd lots to be treated differently. Similarly, block trades are usually broken up for execution and may take longer to execute due to the market having to absorb the block of shares over time rather than in one large execution. When combined with a thinly traded stock, it’s quite possible that odd lots and block trades may not get filled or execute in a timely manner, and sometimes, not at all, depending on other factors like order types used.

# Short Sales

A short sale is the sale of a stock that a seller does not own. In general, a short seller sells borrowed stock in anticipation of a price decline. The short seller later closes out the position by purchasing the stock.

# Order Handling Standards at Alpaca Securities LLC

Market and limit order orders are protected on the primary exchange opening print. We do not necessarily route retail orders to the exchange, but will route orders to market makers who will route orders on your behalf to the primary market opening auction. This protection is subject to exchange time cutoff for each exchange’s opening process. For instance, if you enter a market order between 9:28:01 and 9:29:59 on a Nasdaq security you would not receive the Nasdaq Official Opening Price (NOOP) since Nasdaq has a cutoff of 9:28 for market orders to be sent to the cross. Any market orders received before 9:28 will be filled at the Nasdaq Official Opening Price.

Stop orders and trailing stops are elected on the consolidated print. Your sell stop order will only elect if there is a trade on the consolidated tape at or lower than your stop price and provided the electing trade is not outside of the NBBO. Your buy stop order will only elect if there is a trade on the consolidated tape that is at or above your stop price that is not outside of the NBBO.

Limit Orders are generally subject to limit order display and protection. Protection implies that you should not see the stock trade better than your limit without you receiving an execution. Limit Order Display is bound by REG NMS Rule 611. Your orders will be displayed if they are the National Best Bid or Best Offer excluding exceptions outlined REG NMS Rule 611. Some examples are listed below:

* An odd lot order (under a unit of trade). Most NMS securities have a unit of trade of 100 shares.
* Block Order. A block order under REG NMS is designated as an order of at least 10,000 shares or at least $200,000 notional.
* An “all or none” order
* The client requests the order to not be displayed.
* Not Held orders

# OTC Positions

OTC positions that are actively trading will not be automatically removed/liquidated from a user's account. The user can submit orders if the client wishes to remove or liquidate them.

OTC markets have several market tiers and depending on the market tier there may be more considerations when placing an order to close the position.

**OTC Market Tier**  
*OTCQX, OTCQB, Pink (Current, limited, No information)*  
Clients can enter market orders, limit orders and stop orders to close positions. For market orders, clients can mix whole shares and fractional shares.

*Expert Market, Caveat Emptor*  
Clients must enter day-limit orders when placing orders to close out an OTC expert market security. However, Alpaca will accept market orders that are only fractional shares, but it is a best practice to enter a day-limit order for your whole, mixed (whole and fraction) or fractional order.

Example: User owns 10.53 shares of WXYZ Stock: Sell Limit Order for 10.53 shares of WXYZ Stock at a limit price.

OTC market data is a separate data subscription. In many circumstances, a client can obtain a real-time level one quote from otcmarkets.com. Additionally, you can check the OTC market tier on that website as well.

Updated 5 months ago

---

Ask AI

---

# DMA Gateway / Advanced Order Types (https://docs.alpaca.markets/docs/alpaca-elite-smart-router)

# DMA Gateway / Advanced Order Types

Take Control of Your Trades with Direct Market Access Gateway and Advanced Order Types

# Elite Smart Router

Elite Smart Router is designed to meet the needs of institutional clients and experienced algorithmic traders. A wide array of advanced investing and trading strategies are supported with higher API limits and cost-effective pricing.

One year after launching Alpaca Elite, we are expanding the feature set of the Elite Smart Router. The two key additions are Direct Market Access (DMA) Gateway*\** and Advanced Order Types. Direct Market Access Gateway\* (DMA Gateway) gives you direct control of where your orders are sent. This, along with advanced order types like Volume-Weighted Average Price (VWAP) and Time-Weighted Average Price (TWAP), enables you to efficiently manage large orders, control execution costs, help minimize market impact, and meet your specific trading objectives. DMA Gateway, VWAP, and TWAP can only be accessed if users are on the Elite Smart Router as part of the Alpaca Elite Program.

\*Direct Market Access Gateway is provided solely by DASH Financial Technologies ("DASH"), a member of the listed exchanges. Alpaca enables customers to route orders to the selected exchange through DASH’s DMA capabilities.

## DMA Gateway

DMA Gateway is a tool that gives you customization over where your trades are sent.

Benefits:

* Efficiently manage large orders
* Execution customization
* Help minimize market impact
* Meet your specific trading objectives

### Implementation

DMA orders are configured using `advanced_instructions` in your order request payload:

SubmitCancel

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "side": "buy",
  "symbol": "AAPL",
  "type": "limit",
  "qty": "100",
  "time_in_force": "day",
  "limit_price": "212",
  "order_class": "simple",
  "advanced_instructions": {
    "algorithm":  "DMA",
    "destination":  "NYSE",
    "display_qty":  "100"
  }
}' | jq -r
```

```
curl --request DELETE \
     --url $APIDOMAIN/v2/orders/<your_order_id> \
     --header 'accept: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
```

#### Parameters

| Parameter | Required | Description | Values |
| --- | --- | --- | --- |
| `algorithm` | **mandatory** | Must be set to "DMA" for Direct Market Access routing | `"DMA"` |
| `destination` | **mandatory** | Target exchange for order execution | `"NYSE"`, `"NASDAQ"`, `"ARCA"` |
| `display_qty` | optional | Maximum shares/contracts displayed on the exchange at any time | Must be in round lot increments (100s) |

Notes:

* Parameter replacement is not supported for DMA orders

#### Available Destinations

* **NYSE** - New York Stock Exchange
* **NASDAQ** - NASDAQ Stock Market
* **ARCA** - NYSE Arca

We’re starting with the three destinations listed above, with plans to expand to 10+ additional destinations—including BATS, IEX, AMEX, and more—in the coming months.

### Extended Hours Trading

DMA orders support extended hours trading for the following destinations:

* **NASDAQ** - Pre-market and after-hours sessions
* **ARCA** - Pre-market and after-hours sessions

## VWAP: Volume-Weighted Average Price Orders

A VWAP order is designed to execute a trade at or near the volume-weighted average price of a security over a specified time period. It is calculated by dividing the total dollar value traded for the security (price × volume) by the total volume traded during that period.

VWAP automatically weights each trade price by its corresponding trade volume, ensuring the average reflects both price and trading activity. This makes VWAP a valuable reference for assessing execution quality and market trends.

Benefits:

* Market Impact Management: VWAP orders are designed to execute in proportion to market volume, which may help reduce the likelihood of large trades significantly influencing the market price.
* Benchmark Alignment: VWAP can be used as a benchmark strategy, aiming to achieve execution prices close to the volume-weighted average price over a specified time period. This approach may help align fills with average market pricing trends.

### Implementation

VWAP orders are configured using `advanced_instructions` in your order request payload:

SubmitReplaceCancel

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "side": "buy",
  "symbol": "AAPL",
  "type": "limit",
  "qty": "100",
  "time_in_force": "day",
  "limit_price": "212",
  "order_class": "simple",
  "advanced_instructions": {
    "algorithm":  "VWAP",
    "start_time": "2025-07-21T09:30:00-04:00",
    "end_time": "2025-07-21T15:30:00-04:00",
	  "max_percentage": "0.123"
  }
}' | jq -r
```

```
curl --request PATCH \
     --url $APIDOMAIN/v2/orders/<your_order_id> \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "qty": "200",
  "advanced_instructions": {
    "algorithm":  "VWAP",
    "start_time": "2025-07-21T09:40:00-04:00",
    "end_time": "2025-07-21T15:20:00-04:00",
	  "max_percentage": "0.321"
  }
}' | jq -r
```

```
curl --request DELETE \
     --url $APIDOMAIN/v2/orders/<your_order_id> \
     --header 'accept: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
```

Notes:

* If `advanced_instructions` is not included in the replace payload then it will remain the same
* If `advanced_instructions` is included in the replace payload then it will replace the original one. So if the client wants to update only the `end_time` and keep the rest parameters as is, then the whole `advanced_instructions` payload needs to be sent in the replace request, including the unchanged parameters.

#### Parameters

| Parameter | Required | Description | Values |
| --- | --- | --- | --- |
| `algorithm` | **mandatory** | Must be set to "VWAP" for Volume-Weighted Average Price Orders | `"VWAP"` |
| `start_time` | optional | When the algorithm is to start executing | `RFC3339` Timestamp, must be within current market trading hours. Defaults to start immediately or at start of the regular market hours (whichever is later). VWAP orders do NOT participate in Open Auction. |
| `end_time` | optional | When the algorithm is to be done executing | `RFC3339` Timestamp, must be within current market trading hours and after `start_time`. Defaults to end of regular market hours. VWAP orders do NOT participate in Close Auction. |
| `max_percentage` | optional | Maximum percentage of the ticker's period volume this  order might participate in | Decimal number, must be 0 < `max_percentage` < 1, with up to 3 decimal points precision. |

## TWAP: Time-Weighted Average Price Orders

A TWAP order is designed to execute a trade evenly over a specified time period, regardless of market volume. The order is divided into equal-sized trades that are placed at regular, pre-defined intervals until the order is complete.

Benefits:

* Reduces Market Impact: By spreading the order evenly across time, TWAP can help minimize the risk of significant price swings caused by large trades.
* Execution Predictability: Unlike VWAP, which adjusts based on market volume, TWAP may offer more consistent, evenly paced execution, which can be helpful in managing certain trading strategies.
* Effective in Low-Liquidity Environments: When volume patterns are unpredictable, TWAP can help prevent trades from disrupting the market and can help maintain price stability.

### Implementation

TWAP orders are configured using `advanced_instructions` in your order request payload:

SubmitReplaceCancel

```
curl --request POST \
     --url $APIDOMAIN/v2/orders \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "side": "buy",
  "symbol": "AAPL",
  "type": "limit",
  "qty": "100",
  "time_in_force": "day",
  "limit_price": "212",
  "order_class": "simple",
  "advanced_instructions": {
    "algorithm":  "TWAP",
    "start_time": "2025-07-21T09:30:00-04:00",
    "end_time": "2025-07-21T15:30:00-04:00",
	  "max_percentage": "0.123"
  }
}' | jq -r
```

```
curl --request PATCH \
     --url $APIDOMAIN/v2/orders/<your_order_id> \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
     --data '
{
  "qty": "200",
  "advanced_instructions": {
    "algorithm":  "TWAP",
    "start_time": "2025-07-21T09:40:00-04:00",
    "end_time": "2025-07-21T15:20:00-04:00",
	  "max_percentage": "0.321"
  }
}' | jq -r
```

```
curl --request DELETE \
     --url $APIDOMAIN/v2/orders/<your_order_id> \
     --header 'accept: application/json' \
     --header "Apca-Api-Key-Id: $APIKEY" \
     --header "Apca-Api-Secret-Key: $SECRET" \
```

Notes:

* If `advanced_instructions` is not included in the replace payload then it will remain the same
* If `advanced_instructions` is included in the replace payload then it will replace the original one. So if the client wants to update only the `end_time` and keep the rest parameters as is, then the whole `advanced_instructions` payload needs to be sent in the replace request, including the unchanged parameters.

#### Parameters

| Parameter | Required | Description | Values |
| --- | --- | --- | --- |
| `algorithm` | **mandatory** | Must be set to "TWAP" for Time-Weighted Average Price Orders | `"TWAP"` |
| `start_time` | optional | When the algorithm is to start executing | `RFC3339` Timestamp, must be within current market trading hours. Defaults to start immediately or at start of the regular market hours (whichever is later). TWAP orders do NOT participate in Open Auction. |
| `end_time` | optional | When the algorithm is to be done executing | `RFC3339` Timestamp, must be within current market trading hours and after `start_time`. Defaults to end of regular market hours. TWAP orders do NOT participate in Close Auction. |
| `max_percentage` | optional | Maximum percentage of the ticker's period volume this  order might participate in | Decimal number, must be 0 < `max_percentage` < 1, with up to 3 decimal points precision. |

## Key Considerations:

* `advanced_instructions` will be accepted for paper trading; however, the order will not be simulated in the paper environment.
* DMA gateway only supports market and limit orders and Time in Force (TIF) = day. If you wish to use MOO/MOC, gtc, or stop orders, you cannot specify advanced\_instructions

---

*Direct Market Access Gateway is provided solely by DASH Financial Technologies ("DASH"), a member of the listed exchanges. Alpaca enables customers to route orders to the selected exchange through DASH’s DMA capabilities..*

*Please note that this is currently only available to users who are on the[Elite Smart Router](https://alpaca.markets/elite). For more information on Alpaca Elite please see the [term and conditions](https://files.alpaca.markets/disclosures/library/Alpaca+Elite+Agreement.pdf).*

*The content of this article is for general informational purposes only. All examples are for illustrative purposes only.*

*All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.*

*Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member[FINRA/SIPC](https://www.finra.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.*

*This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities are not registered or licensed, as applicable.*

Updated 5 months ago

---

Ask AI

---

# User Protection (https://docs.alpaca.markets/docs/user-protection)

# User Protection

We have enabled several types of protections to enhance your trading experience.

1. Pattern Day Trader (PDT) Protection
2. Day Trade Margin Call (DTMC) Protection
3. Preventing Wash Trades
4. Limit order price away sanity check

Please note that these do not apply to crypto trading as cryptocurrencies are not marginable. Pattern Day Trading rule does not apply to crypto trading either. Preventing Wash Trades does apply to crypto trading.

# Pattern Day Trader (PDT) Protection at Alpaca

In order to prevent Alpaca Brokerage Account customers from unintentionally being designated as a Pattern Day Trader (PDT), the Alpaca Trading platform checks the PDT rule condition every time an order is submitted from a customer. If the order could potentially result in the account being flagged as a PDT, the order is rejected, and API returns error with HTTP status code 403 (Forbidden).

## The Rule

A day trade is defined as a round-trip pair of trades within the same day (including extended hours). This is best described as an initial or opening transaction that is subsequently closed later in the same calendar day. For long positions, this would consist of a buy and then sell. For short positions, selling a security short and buying it back to cover the short position on the same day would also be considered a day trade.

An account is designated as a Pattern Day Trader if it makes four (4) or more day trades within five (5) business days, and the number of day trades represents more than six percent (6%) of the total trades within the same five (5) business days window. Day trades less than this criteria will not flag the account for PDT.

Cryptocurrency trading is not subject to the PDT rule. As a result, crypto orders are not evaluated by PDT protection logic and round-trip crypto trades on the same day do not contribute to the day trade count.

Day trades are counted regardless of share quantity or frequency throughout the day. Here are some FINRA-provided examples:

Example A:

09:30 Buy 250 ABC  
09:31 Buy 250 ABC  
13:00 Sell 500 ABC  
The customer has executed one day trade.

Example B:  
09:30 Buy 100 ABC  
09:31 Sell 100 ABC  
09:32 Buy 100 ABC  
13:00 Sell 100 ABC  
The customer has executed two day trades.

Example C:  
09:30 Buy 500 ABC  
13:00 Sell 100 ABC  
13:01 Sell 100 ABC  
13:03 Sell 300 ABC  
The customer has executed one day trade.

Example D:  
09:30 Buy 250 ABC  
09:31 Buy 300 ABC  
13:01 Buy 100 ABC  
13:02 Sell 150 ABC  
13:03 Sell 175 ABC  
The customer has executed one day trade.

Example E:  
09:30 Buy 199 ABC  
09:31 Buy 142 ABC  
13:00 Sell 1 ABC  
13:01 Buy 45 ABC  
13:02 Sell 100 ABC  
13:03 Sell 200 ABC  
The customer has executed two day trades.

Example F:  
09:30 Buy 200 ABC  
09:30 Buy 100 XYZ  
13:00 Sell 100 ABC  
13:00 Sell 100 XYZ

The customer has executed two day trades.

For further information, please visit [Regulatory Notice 21-13 | FINRA.org](https://www.finra.org/rules-guidance/notices/21-13)

## Alpaca’s Order Rejection

Alpaca Trading platform monitors the number of day trades for the account for the past 5 business days and rejects a newly submitted orders on exit of a position if it could potentially result in the account being flagged for PDT. This protection triggers only when the previous day’s closing account equity is less than $25,000 at the time of order submission.

In addition to the filled orders, the system also takes into consideration pending orders in the account. In this case, regardless of the order of pending orders, a pair of buy and sell orders is counted as a potential day trade. This is because orders that are active (pending) in the marketplace may fill in random orders. Therefore, even if your sell limit order is submitted first (without being filled yet) and another buy order on the same security is submitted later, this buy order will be blocked if your account already has 3 day trades in the last 5 business days.

  

## Pattern Day Trader (PDT) Restriction at Alpaca

If an account falls below the required **$25,000 securities equity** at the end of the trading day, it will be flagged for not meeting the **Pattern Day Trader (PDT)** requirements. When this happens, the account will be restricted from placing any new day trades on the following business day. Day trading will remain blocked until either:

**A PDT Restriction lift is granted, or**

**A One-Time PDT Removal is granted, or**

**The account equity once again meets the $25,000 minimum requirement by the end of the trading day.**

To request a **PDT Restriction lift or One-Time PDT Removal**\* in order to place a day trade, please contact our support team at [[email protected]](/cdn-cgi/l/email-protection#bbc8cecbcbd4c9cffbdad7cbdad8da95d6dac9d0decfc8).

\***Note:** The **One-Time PDT Removal** applies for the life of all accounts at Alpaca. By requesting this, you are removing the PDT flag from your account and agree not to engage in future pattern day trading.
Please also note that once the restriction is lifted and you place a day trade, your account will be limited to **liquidation-only activity for 90 days**, or until the **$25,000 equity requirement** is met.

  

## Paper Trading

The same protection triggers in your paper trading account. It is advised to test your algorithm with the realistic balance amount you would manage when going live, to make sure your assumption works under this PDT protection as well.

> For more details of Pattern Day Trader rule, please visit the [FINRA website](https://www.finra.org/investors/investing/investment-products/stocks/day-trading).

# Day Trade Margin Call (DTMC) Protection at Alpaca

In order to prevent Alpaca Brokerage Account customers from unintentionally receiving day trading margin calls, Alpaca implements two forms of DTMC protection.

## The Rule

Day traders are required to have a minimum of $25,000 OR 25% of the total market value of securities (whichever is higher) maintained in their account.

The buying power of a pattern day trader is 4x the excess of the maintenance margin from the closing of the previous day. If you exceed this amount, you will receive a day trading margin call.

## How Alpaca’s DTMC Protection Settings Work

Users only receive day trading buying power when marked as a pattern day trader. If the user is designated a pattern day trader, the account.multiplier is equal to 4.

Daytrading buying power cannot increase beyond its start of day value. In other words, closing an overnight position will not add to your daytrading buying power.

The following scenarios and protections are applicable only for accounts that are designated as pattern day traders. Please check your Account API result for the multiplier field.

Every trading day, you start with the new `daytrading_buying_power`. This beginning value is calculated as `4 * (last_equity - last_maintenance_margin)`. The last\_equity and last\_maintenance\_margin values can be accessed through Account API. These values are stored from the end of the previous trading day.

Throughout the day, each time you enter a new position, your `daytrading_buying_power` is reduced by that amount. When you exit that position within the same day, that same amount is credited back, regardless of position’s P/L.

At the end of the trading day, on close, the maximum exposure of your day trading position is checked. A Day Trade Margin Call (DTMC) is issued the next day if the maximum exposure of day trades exceeded your day trading buying power from the beginning of that day.

The buying\_power value is the larger of `regt_buying_power` and `daytrading_buying_power`. Since the basic buying power check runs on this buying\_power value, you could be exceeding your `daytrading_buying_power` when you enter the position if `regt_buying_power` is larger than your `daytrading_buying_power` at one point in the day.

The following is an example scenario:

1. Your equity is $50k
2. You hold overnight positions up to $100k
3. Your maintenance margin is $30k (~30%), therefore your day trading buying power at the beginning of day is $80k using the calculation of 4 \* ($50k - $30k)
4. You sell all of the overnight positions ($100k value) in the morning, which brings your `regt_buying_power` up to $100k
5. You now buy and sell the same security up to $100k
6. At the end of the day, you have a $20k Day Trade Margin Call ($100k - $80k)

By default, Alpaca users have DTMC protections on entry of a position. This means that if your entering order would exceed `daytrading_buying_power` at the moment, it will be blocked, even if `regt_buying_power` still has room for it. This is based on the assumption that any entering position could be day trades later in the day. This option is the more conservative of the two DTMC protections that our users have.

The second DTMC protection option is protection on exit of a position. This means that Alpaca will block the exit of positions that would cause a Day Trading Margin Call. This may cause users to be unable to liquidate a position until the next day.

Neither of the DTMC protection options evaluate crypto orders since crypto cannot be purchased using margin.

One of the two protections will be enabled for all users (you cannot have both protections disabled). If you would like to switch your protection option, please contact our support.

We are working towards features to allow users to change their DTMC protection setting on their own without support help.

## Equity/Order Ratio Validation Check

In order to help Alpaca Brokerage Account customers from placing orders larger than the calculated buying power, Alpaca has instituted a control on the account independent of the buying power for the account. Alpaca will restrict the account to closing transactions when an account has a position that is 600% larger than the equity in the account. The account will remain restricted for closing transactions until a member of Alpaca’s trading team reviews the account. The trading team will either clear the alert by allowing opening transactions or will notify the client of the restriction and take corrective actions as necessary.

## Paper Trading

he same protection triggers in your paper trading account. It is advised to test your algorithm with the realistic balance amount you would manage when going live, to make sure your assumption works under this DTMC protection as well.

For more details of Pattern Day Trader rule, please read [FINRA’s margin requirements](https://www.finra.org/investors/learn-to-invest/advanced-investing/day-trading-margin-requirements-know-rules-rot). For more details on day trade margins, please read [FINRA’s Mind Your Margin](https://www.finra.org/investors/day-trading) article.

# Preventing Wash Trades at Alpaca

At Alpaca, we want to help our customers avoid making unintentional wash trades. A wash trade happens when a customer buys and sells the same security at the same time, which can be seen as a form of market manipulation. To prevent this, the Alpaca Trading platform checks for potential wash trades every time a customer places an order. If we detect a possible wash trade, we reject the order and send back an error message with the HTTP status code 403 (Forbidden).

## The Rule

A wash trade occurs when a customer's two orders could potentially interact with each other. Here are a couple of examples:

* A customer places an order to buy 1 share at $10 (a limit order). Then, the same customer places an order to sell 100 shares at $10 (another limit order). These orders could potentially interact, which would be a wash trade.
* A customer places an order to sell 100 shares at the market open (a market order). Then, the same customer places an order to buy 100 shares at $10 (a limit order). Again, these orders could potentially interact, which would be a wash trade.

## How Alpaca Handles Potential Wash Trades

The Alpaca Trading platform is always on the lookout for potential wash trades. If we determine that an order could result in a wash trade, we trigger our protection measures, reject the order, and send back an error message with the HTTP status code 403 (Forbidden).

If a customer wants to set up a 'take profit' and a 'stop loss' situation, we recommend using a bracket or OCO (One Cancels the Other) order. These complex orders and trailing stop orders are exceptions to our wash trade protection.

Here's a table that shows when we would reject an order to prevent a potential wash trade:

| Existing Order | New Order | Reject Condition |
| --- | --- | --- |
| market buy | market sell | always rejected |
| market buy | limit sell | always rejected |
| market buy | stop sell | always rejected |
| market buy | stop\_limit sell | always rejected |
| market sell | market buy | always rejected |
| market sell | limit buy | always rejected |
| market sell | stop buy | always rejected |
| market sell | stop\_limit buy | always rejected |
| stop buy | market sell | always rejected |
| stop buy | limit sell | always rejected |
| stop buy | stop sell | always rejected |
| stop buy | stop\_limit sell | always rejected |
| stop sell | market buy | always rejected |
| stop sell | limit buy | always rejected |
| stop sell | stop buy | always rejected |
| stop sell | stop\_limit buy | always rejected |
| limit buy | market sell | always rejected |
| limit buy | limit sell | rejected if buy limit price >= sell limit price |
| limit buy | stop sell | always rejected |
| limit buy | stop\_limit sell | rejected if buy limit price >= sell limit price |
| limit sell | market buy | always rejected |
| limit sell | limit buy | rejected if buy limit price >= sell limit price |
| limit sell | stop buy | always rejected |
| limit sell | stop\_limit buy | rejected if buy limit price >= sell limit price |
| stop\_limit buy | market sell | always rejected |
| stop\_limit buy | limit sell | rejected if buy limit price >= sell limit price |
| stop\_limit buy | stop sell | always rejected |
| stop\_limit buy | stop\_limit sell | rejected if buy limit price >= sell limit price |
| stop\_limit sell | market buy | always rejected |
| stop\_limit sell | limit buy | rejected if buy limit price >= sell limit price |
| stop\_limit sell | stop buy | always rejected |
| stop\_limit sell | stop\_limit buy | rejected if buy limit price >= sell limit price |

## Paper Trading

Our wash trade protection also applies to your paper trading account. We recommend testing your trading algorithm with a realistic balance amount. This way, you can make sure your strategy works under our wash trade protection rules before you start live trading.

For more details of wash trade rule, please read  
[FINRA's self-trades requirements](https://www.finra.org/rules-guidance/rulebooks/finra-rules/5210).

Updated 3 months ago

---

Ask AI

---

# Websocket Streaming (https://docs.alpaca.markets/docs/websocket-streaming)

# Websocket Streaming

Learn how to stream market data using Websockets.

Alpaca’s API offers WebSocket streaming for trade, account, and order updates which follows the [RFC6455 WebSocket protocol](https://datatracker.ietf.org/doc/html/rfc6455).

To connect to the WebSocket follow the standard opening handshake as defined by the RFC specification to `wss://paper-api.alpaca.markets/stream` or `wss://api.alpaca.markets/stream`. Alpaca’s streaming service supports both JSON and MessagePack codecs.

Once the connection is authorized, the client can listen to the `trade_updates` stream to get updates on trade, account, and order changes.

> 📘
>
> ### Note:
>
> The `trade_updates` stream coming from `wss://paper-api.alpaca.markets/stream` uses binary frames, which differs from the text frames that comes from the `wss://data.alpaca.markets/stream` stream.

In order to listen to streams, the client sends a `listen` message to the server as follows:

JSON

```
{
  "action": "listen",
  "data": {
    "streams": ["trade_updates"]
  }
}
```

The server acknowledges by replying a message in the listening stream.

JSON

```
{
  "stream": "listening",
  "data": {
    "streams": ["trade_updates"]
  }
}
```

If any of the requested streams are not available, they will not appear in the streams list in the acknowledgement. Note that the streams field in the listen message is to tell the set of streams to listen, so if you want to stop receiving updates from the stream, you must send an empty list of streams values as a listen message. Similarly, if you want to add more streams to get updates in addition to the ones you are already doing so, you must send all the stream names, not only the new ones.

Subscribing to real-time trade updates ensures that a user always has the most up-to-date picture of their account actvivity.

> 📘
>
> ### Note
>
> To request with MessagePack, add the header: Content-Type: `application/msgpack`.

# Authentication

The WebSocket client can be authenticated using the same API key when making HTTP requests. Upon connecting to the WebSocket, client must send an authentication message over the WebSocket connection with the API key and secret key as its payload.

JSON

```
{
  "action": "auth",
  "key": "{YOUR_API_KEY_ID}",
  "secret": "{YOUR_API_SECRET_KEY}"
}
```

The server will then authorize the connection and respond with either an authorized (successful) response

JSON

```
{
  "stream": "authorization",
  "data": {
    "status": "authorized",
    "action": "authenticate"
  }
}
```

or an unauthorized (unsuccessful) response:

JSON

```
{
  "stream": "authorization",
  "data": {
    "status": "unauthorized",
    "action": "authenticate"
  }
}
```

In the case that the socket connection is not authorized yet, a new message under the authorization stream is issued in response to the listen request.

JSON

```
{
  "stream": "authorization",
  "data": {
    "status": "unauthorized",
    "action": "listen"
  }
}
```

# Trade Updates

With regards to the account associated with the authorized API keys, updates for orders placed at Alpaca are dispatched over the WebSocket connection under the event trade\_updates. These messages include any data pertaining to orders that are executed with Alpaca. This includes order fills, partial fills, cancellations and rejections of orders. Clients may listen to this stream by sending a listen message:

JSON

```
{
  "action": "listen",
  "data": {
    "streams": ["trade_updates"]
  }
}
```

Any listen messages received by the server will be acknowledged via a message on the listening stream. The message’s data payload will include the list of streams the client is currently listening to:

JSON

```
{
  "stream": "listening",
  "data": {
    "streams": ["trade_updates"]
  }
}
```

The fields present in a message sent over the `trade_updates` stream depend on the type of event they are communicating. All messages contain an `event` type and an `order` field, which is the same as the order object that is returned from the REST API. Potential event types and additional fields that will be in their messages are listed below.

## Common Events

These are the events that are the expected results of actions you may have taken by sending API requests.

* `new`: Sent when an order has been routed to exchanges for execution.
* `fill`: Sent when an order has been completely filled.
  + `timestamp`: The time at which the order was filled.
  + `price`: The price per share for the fill event. This may be different from the average fill price for the order if there were partial fills.
  + `qty`: The number of shares for the fill event. This will be different from the filled quantity for the order if there were partial fills.
  + `position_qty`: The total size of your position after this event, in shares. Positive for long positions, negative for short positions.
* `partial_fill`: Sent when a number of shares less than the total remaining quantity on your order has been filled.
  + `timestamp`: The time at which the order was partially filled.
  + `price`: The price per share for the partial fill event.
  + `qty`: The number of shares for the partial fill event.
  + `position_qty`: The total size of your position after this event, in shares. Positive for long positions, negative for short positions.
* `canceled`: Sent when your requested cancelation of an order is processed.
  + `timestamp`: The time at which the order was canceled.
* `expired`: Sent when an order has reached the end of its lifespan, as determined by the order’s time in force value.
  + `timestamp`: The time at which the order was expired.
* `done_for_day`: Sent when the order is done executing for the day, and will not receive further updates until the next trading day.
* `replaced`: Sent when your requested replacement of an order is processed.
  + `timestamp`: The time at which the order was replaced.

## Less Common Events

These are events that may rarely be sent due to uncommon circumstances on the exchanges. It is unlikely you will need to design your code around them, but you may still wish to account for the possibility that they can occur.

* `accepted`: Sent when your order has been received by Alpaca, but hasn’t yet been routed to the execution venue.
* `rejected`: Sent when your order has been rejected.
  + `timestamp`: The time at which the order was rejected.
* `pending_new`: Sent when the order has been received by Alpaca and routed to the exchanges, but has not yet been accepted for execution.
* `stopped`: Sent when your order has been stopped, and a trade is guaranteed for the order, usually at a stated price or better, but has not yet occurred.
* `pending_cancel`: Sent when the order is awaiting cancelation. Most cancelations will occur without the order entering this state.
* `pending_replace`: Sent when the order is awaiting replacement.
* `calculated`: Sent when the order has been completed for the day - it is either “filled” or “done\_for\_day” - but remaining settlement calculations are still pending.
* `suspended`: Sent when the order has been suspended and is not eligible for trading.
* `order_replace_rejected`: Sent when the order replace has been rejected.
* `order_cancel_rejected`: Sent when the order cancel has been rejected.

# Example

An example of a message sent over the `trade_updates` stream looks like:

JSON

```
{
  "stream": "trade_updates",
  "data": {
    "event": "fill",
    "execution_id": "2f63ea93-423d-4169-b3f6-3fdafc10c418",
    "order": {
      "asset_class": "crypto",
      "asset_id": "1cf35270-99ee-44e2-a77f-6fab902c7f80",
      "cancel_requested_at": null,
      "canceled_at": null,
      "client_order_id": "4642fd68-d59a-47d7-a9ac-e22f536828d1",
      "created_at": "2022-04-19T13:45:04.981350886-04:00",
      "expired_at": null,
      "extended_hours": false,
      "failed_at": null,
      "filled_at": "2022-04-19T17:45:05.024916716Z",
      "filled_avg_price": "105.8988475",
      "filled_qty": "1790.86",
      "hwm": null,
      "id": "a5be8f5e-fdfa-41f5-a644-7a74fe947a8f",
      "legs": null,
      "limit_price": null,
      "notional": null,
      "order_class": "",
      "order_type": "market",
      "qty": "1790.86",
      "replaced_at": null,
      "replaced_by": null,
      "replaces": null,
      "side": "sell",
      "status": "filled",
      "stop_price": null,
      "submitted_at": "2022-04-19T13:45:04.980944666-04:00",
      "symbol": "SOLUSD",
      "time_in_force": "gtc",
      "trail_percent": null,
      "trail_price": null,
      "type": "market",
      "updated_at": "2022-04-19T13:45:05.027690731-04:00"
    },
    "position_qty": "0",
    "price": "105.8988475",
    "qty": "1790.86",
    "timestamp": "2022-04-19T17:45:05.024916716Z"
  }
}
```

An example message for MultilegOptionsOrder fill event:

JSON

```
{
    "stream": "trade_updates",
    "data": {
        "at": "2025-01-21T07:32:40.70095Z",
        "event_id": "01JJ3WE73W5PG672TC4XACXH5R",
        "event": "fill",
        "timestamp": "2025-01-21T07:32:40.695569506Z",
        "order": {
            "id": "31cd620f-3bd5-41b7-8bb2-6834524679d0",
            "client_order_id": "fe999618-6435-497b-9fdd-a63d3da3615f",
            "created_at": "2025-01-21T07:32:40.678963102Z",
            "updated_at": "2025-01-21T07:32:40.699359002Z",
            "submitted_at": "2025-01-21T07:32:40.691562346Z",
            "filled_at": "2025-01-21T07:32:40.695569506Z",
            "expired_at": null,
            "cancel_requested_at": null,
            "canceled_at": null,
            "failed_at": null,
            "replaced_at": null,
            "replaced_by": null,
            "replaces": null,
            "asset_id": "00000000-0000-0000-0000-000000000000",
            "symbol": "",
            "asset_class": "",
            "notional": null,
            "qty": "1",
            "filled_qty": "1",
            "filled_avg_price": "1.62",
            "order_class": "mleg",
            "order_type": "limit",
            "type": "limit",
            "side": "buy",
            "time_in_force": "day",
            "limit_price": "2",
            "stop_price": null,
            "status": "filled",
            "extended_hours": false,
            "legs": [
                {
                    "id": "3cbe69ef-241c-43ba-9d8c-09361930a1af",
                    "client_order_id": "e868fb88-ce92-442b-91be-4b16defbc883",
                    "created_at": "2025-01-21T07:32:40.678963102Z",
                    "updated_at": "2025-01-21T07:32:40.697474882Z",
                    "submitted_at": "2025-01-21T07:32:40.687356797Z",
                    "filled_at": "2025-01-21T07:32:40.695564076Z",
                    "expired_at": null,
                    "cancel_requested_at": null,
                    "canceled_at": null,
                    "failed_at": null,
                    "replaced_at": null,
                    "replaced_by": null,
                    "replaces": null,
                    "asset_id": "925af3ed-5c00-4ef1-b89b-e4bd05f04486",
                    "symbol": "AAPL250321P00200000",
                    "asset_class": "us_option",
                    "notional": null,
                    "qty": "1",
                    "filled_qty": "1",
                    "filled_avg_price": "1.6",
                    "order_class": "mleg",
                    "order_type": "",
                    "type": "",
                    "side": "buy",
                    "time_in_force": "day",
                    "limit_price": null,
                    "stop_price": null,
                    "status": "filled",
                    "extended_hours": false,
                    "legs": null,
                    "trail_percent": null,
                    "trail_price": null,
                    "hwm": null,
                    "ratio_qty": "1"
                },
                {
                    "id": "ec694de5-5028-4347-8f89-d8ea00c9341f",
                    "client_order_id": "0a1bf1e1-6992-4c23-85a6-9469bbe05f1a",
                    "created_at": "2025-01-21T07:32:40.678963102Z",
                    "updated_at": "2025-01-21T07:32:40.699294952Z",
                    "submitted_at": "2025-01-21T07:32:40.691562346Z",
                    "filled_at": "2025-01-21T07:32:40.695569506Z",
                    "expired_at": null,
                    "cancel_requested_at": null,
                    "canceled_at": null,
                    "failed_at": null,
                    "replaced_at": null,
                    "replaced_by": null,
                    "replaces": null,
                    "asset_id": "9f8c3d65-f5f7-42cd-acbc-9636cc32d3b5",
                    "symbol": "AAPL250321C00380000",
                    "asset_class": "us_option",
                    "notional": null,
                    "qty": "1",
                    "filled_qty": "1",
                    "filled_avg_price": "0.02",
                    "order_class": "mleg",
                    "order_type": "",
                    "type": "",
                    "side": "buy",
                    "time_in_force": "day",
                    "limit_price": null,
                    "stop_price": null,
                    "status": "filled",
                    "extended_hours": false,
                    "legs": null,
                    "trail_percent": null,
                    "trail_price": null,
                    "hwm": null,
                    "ratio_qty": "1"
                }
            ],
            "trail_percent": null,
            "trail_price": null,
            "hwm": null
        },
        "price": "1.62",
        "qty": "1",
        "position_qtys": {
            "AAPL250321P00200000": "1",
            "AAPL250321C00380000": "1"
        },
        "legs": [
            {
                "execution_id": "69a70e98-f370-427d-bcd3-834dc4800aed",
                "qty": "1",
                "price": "1.6",
                "order_id": "3cbe69ef-241c-43ba-9d8c-09361930a1af",
                "symbol": "AAPL250321P00200000",
                "timestamp": "2025-01-21T07:32:40.695564076Z"
            },
            {
                "execution_id": "fb878d87-569e-49f3-b42e-a09ad06e3d3a",
                "qty": "1",
                "price": "0.02",
                "order_id": "ec694de5-5028-4347-8f89-d8ea00c9341f",
                "symbol": "AAPL250321C00380000",
                "timestamp": "2025-01-21T07:32:40.695569506Z"
            }
        ]
    }
}
```

## Error messages

In the case of in-stream errors, the server sends an `error` action before closing the connection.

JSON

```
{
  "action": "error",
  "data": {
    "error_message": "internal server error"
  }
}
```

Updated 5 months ago

---

Ask AI

---

# Trading API FAQs (https://docs.alpaca.markets/docs/position-average-entry-price-calculation)

# Position Average Entry Price Calculation

How is the average entry price of a position is calculated?

# Description

The average entry price and the cost basis of a position are returned in the `avg_entry_price` and `cost_basis` fields in the [positions endpoints](https://docs.alpaca.markets/reference/positions).

JSON

```
{
  "asset_id": "904837e3-3b76-47ec-b432-046db621571b",
  "symbol": "AAPL ",
  "exchange": "NASDAQ",
  "asset_class": "us_equity",
  "avg_entry_price": "100.0",
  "qty": "5",
  "qty_available": "4",
  "side": "long",
  "market_value": "600.0",
  "cost_basis": "500.0",
  "unrealized_pl": "100.0",
  "unrealized_plpc": "0.20",
  "unrealized_intraday_pl": "5.0",
  "unrealized_intraday_plpc": "0.0084",
  "current_price": "120.0",
  "lastday_price": "119.0",
  "change_today": "0.0084"
}
```

There are different methods that can be used to calculate the cost basis and the average entry price of a position such as `Strict FIFO`, `Compressed FIFO`, `Weighted Average`, and others. Each method has its own rules for calculating the cost basis and average entry price after a sell transaction. This page aims to clarify which method is Alpaca using.

# Which Method is Alpaca Using?

* [Weighted Average](doc:position-average-entry-price-calculation#weighted-average) is used for intraday positions (positions from intraday trades)
* [Compressed FIFO](doc:position-average-entry-price-calculation#compressed-fifo-first-in-first-out) is used for the end-of-day positions (positions from previous trading days)

## Strict FIFO (First-In, First-Out)

Under the Strict FIFO method, the first position bought is the first position sold. Let's understand how it works:

The cost basis after the sell is calculated by deducting from the previous cost basis the price of the first open position multiplied by the sell quantity. In Strict FIFO, the sell quantity is covered using the first open position, however, if the first open position's quantity is not enough to cover the sell quantity, subsequent open positions are used.

### Example:

Suppose we have the following transactions:

Day 1:

1. Buy 100 shares at $10 per share (Cost basis = $1,000)
2. Buy 50 shares at $12 per share (Cost basis = $600)

Day 2:

1. Buy 30 shares at $15 per share (Cost basis = $450)

Day 3:

1. Sell 120 shares

After the sell transaction:

* Cost basis: `2050 - 100*10 - 20*12` = `$810`
* Average Entry Price: `cost_basis/qty_left` = `810/60` = `$13.5`

## Compressed FIFO (First-In, First-Out)

The Compressed FIFO method follows similar rules to Strict FIFO, with one key difference. It compresses intraday positions using a weighted average. Let's see how it differs:

### Example 1:

Using the same example from before:  
Day 1:

1. Buy 100 shares at $10 per share (Cost basis = $1,000)
2. Buy 50 shares at $12 per share (Cost basis = $600)

Day 2:

1. Buy 30 shares at $15 per share (Cost basis = $450)

Day 3:

1. Sell 120 shares

After the sell transaction:

* Cost Basis: `2050 - 120*(100*10 + 50*12)/150` = `$770`
* Average entry price: `cost_basis/qty_left` = `770/60` = `$12.83`

As you can see the positions in Day 1 were compressed into a total of 150 shares with an average price of `(100*10 + 50*12)/150`.

### Example 2

Day 1:

1. Buy 100 shares at $10 per share (Cost basis = $1,000)
2. Buy 50 shares at $9 per share (Cost basis = $450)
3. Sell 50 shares
4. Buy 50 shares at $11 per share (Cost basis = $550)

At the end of Day 1:

* Cost Basis: `2000 - 50*(100*10 + 50*9 + 50*11)/200` = `$1,500`
* Average Entry Price: `1500/150` = `$10`

## Weighted Average

The Weighted Average method calculates the cost basis based on the weighted average price per share. Here's how it works:

On Sell: The cost basis for the sold quantity is calculated by deducting the sell quantity multiplied by the average entry price of all the opened positions that the account holds.

### Example:

Using the same example from before:

Day 1:

1. Buy 100 shares at $10 per share (Cost basis = $1,000)
2. Buy 50 shares at $12 per share (Cost basis = $600)

Day 2:

1. Buy 30 shares at $15 per share (Cost basis = $450)

Day 3:

1. Sell 120 shares

After the sell the calculations based on the Weighted average method would be:

* Cost Basis: `2050 - 120*(100*10 + 50*12 + 30*15)/180` = `$683.33`
* Average Entry Price: `cost_basis/qty_left` = `683.33/60` = `$11.39`

# FAQ

## Why did the `avg_entry_price` and `cost_basis` of a position change the next day?

As described in the [Which method is Alpaca using?](doc:position-average-entry-price-calculation#which-method-is-alpaca-using) the calculation method for determining the `avg_entry_price` and `cost_basis` differs between the `intraday positions` and the `end-of-day positions`. Consequently, it is possible for the `avg_entry_price` and `cost_basis` fields of a position to change the day after the last trade has occurred. This change occurs when our beginning-of-day (BOD) job executes and synchronizes positions from our ledger. For details regarding the timing of the beginning-of-day (BOD) job, please refer to the [Daily Processes and Reconciliations](doc:daily-processes-and-reconcilations).

Updated 5 months ago

---

Ask AI

---

# Regulatory Fees (https://docs.alpaca.markets/docs/regulatory-fees)

# Regulatory Fees

## FEE types and effective rates

The following FEEs are applied to options trades.

| Type | When | Charged By |
| --- | --- | --- |
| Trading Activity Fee (TAF) | Sells only | FINRA |
| Options Regulatory Fee (ORF) | Buys and sells | Options Exchanges |
| Options Clearing Corporation | Buys and sells up to 2750 contracts | OCC |
| Consolidated Audit Trail (CAT) | Buys and sells | FINRA-CAT |

The following FEEs are applied to equities.

| Type | When | Charged By |
| --- | --- | --- |
| Trading Activity Fee (TAF) | Sells only | FINRA |
| Consolidated Audit Trail (CAT) | Buys and sells | FINRA-CAT |

For our current effective rates, please refer to our brokerage fee schedule available here:
<https://alpaca.markets/disclosures>

## How Fees are charged and reflected in account balances

1. Alpaca's trading system keeps track of the accrued FEE amounts intraday and deducts the pending amounts from account balances.
2. At EOD, we charge each account the fees for that trading day
3. We round up total fees based on the currency’s precision to the nearest decimal place.
   For example, USD has a precision of 0.01. If the total fee is calculated as 0.00083, it will be rounded up to 0.01 (i.e., 1 penny).

## Additional resources

* <https://www.finra.org/rules-guidance/rulebooks/industry/trading-activity-fee>
* <https://www.catnmsplan.com/>
* <https://www.sec.gov/newsroom/press-releases/2024-47>

Updated 5 months ago

---

Ask AI

---

# Alpaca's MCP Server (https://docs.alpaca.markets/docs/alpaca-mcp-server)

# Alpaca's MCP Server

Turn your words into action with Alpaca’s MCP Server

Alpaca’s MCP Server allows traders to research markets, analyze data, and place orders using natural language across AI chat applications, coding tools, and Command Line Interfaces.

Alpaca’s MCP Server GitHub URL: <https://github.com/alpacahq/alpaca-mcp-server>

For more information, visit [Alpaca's MCP Server Homepage](https://alpaca.markets/mcp-server).

*All data and instructions are current as of November 20, 2025.*

## MCP Server Overview

An MCP server is a component of the [Model Context Protocol](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) (MCP) architecture developed by Anthropic. MCP is an open standard that provides a consistent way for AI applications, code editors, or Command Line Interface to interact with external tools, data sources, and services through a structured protocol.

As AI interfaces improve, connecting them to trading workflows often requires multiple APIs, custom integrations, and authentication steps. MCP architecture streamlines this by providing a standard method for accessing data and performing actions.

An MCP server itself acts as a bridge between the MCP client (AI interfaces) and the capabilities. It presents these capabilities in a predictable and secure format so an AI model can request market data, retrieve information, or carry out defined operations without additional SDKs or complex setup.

## Alpaca’s MCP Server Overview

Alpaca’s MCP Server brings this same bridge-like concept to trading by exposing capabilities powered by Alpaca’s Trading API, including:

* Market data, both historical and live
* Order actions such as entry, change, and cancel
* Portfolio details like positions, buying power, and unrealized P/L
* Optional automation like alerts or risk checks

This helps users accelerate their research, streamline decision making, and support efficient trade execution, helping users capitalize on potential market opportunities more efficiently.
For more information about the available functions, please see the Available Endpoints section below.

## Main Benefits

### Reinforced Decisions, Transparent Execution

Alpaca’s MCP Server gives your AI model structured access to real time market data, news context, portfolio details, and order actions powered by Alpaca’s Trading API. Instead of acting on its own, the AI assistants help surface relevant insights, organize information, and prepare the actions you ask for.

### One Interface for Many Markets

Alpaca’s MCP Server brings equities, ETFs, crypto, and multi-leg options into one workflow and interface. This allows an AI agent to research, analyze, and help execute trading ideas without switching between platforms or juggling APIs.

### Code-Optional, Extensible by Design

Alpaca’s MCP Server lets traders begin with natural language prompts and move into vibe coding or full code whenever they want to optimize strategies.

  

## Supported MCP Clients and Connection Types

Alpaca’s MCP Server can be configured on the following MCP clients. Each client has its own setup requirements. For more details, visit [Alpaca’s MCP Server GitHub](https://github.com/alpacahq/alpaca-mcp-server) . The connection type indicates how you can set up Alpaca’s MCP Server.

Note: Remote hosting for Alpaca’s MCP Server is not yet available. Traders who wish to use it remotely will need to self host for now. We may consider additional options for remote MCP Server use over time, depending on feasibility and demand.

For instructions on self hosting Alpaca’s remote MCP Server, visit our learn article “[How to Deploy Alpaca’s MCP Server Remotely on Claude Mobile App](https://alpaca.markets/learn/how-to-deploy-alpaca-mcp-server-remotely-on-claude-mobile-app) ”.

| MCP client name | Connection type |
| --- | --- |
| Cloud Desktop | Local or Remote |
| Claude Web | Remote only |
| Claude Mobile App | Remote only |
| ChatGPT Web | Remote only |
| ChatGPT Desktop | Remote only |
| ChatGPT Mobile App | Remote only |
| VS Code | Local or Remote |
| Cursor | Local or Remote |
| PyCharm | Local or Remote |
| Claude Code (CLI) | Local or Remote |
| Gemini CLI | Local or Remote |

## Prerequisites for Connections

You will need the following prerequisites to configure and run Alpaca’s MCP Server. The requirements may vary depending on which MCP client you connect it with remotely or locally.

* Terminal (macOS/Linux) | Command Prompt or PowerShell (Windows)
* Python 3.10+ (Check the [official installation guide](https://www.python.org/downloads/) and confirm the version by typing the following command: `python3 --version` in Terminal)
* uv (Install using the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/)) for local setup
  + Tip: uv can be installed either through a package manager (like Homebrew) or directly using `curl | sh`.
* Alpaca Trading API keys (free paper trading account available)
  + To find your Alpaca API keys, please check our “[How to Get Alpaca’s Trading API Key and Start Connect](https://alpaca.markets/learn/connect-to-alpaca-api) ” or “[How to Start Paper Trading with Alpaca](https://alpaca.markets/learn/start-paper-trading) ”
* MCP client (Claude Desktop, Cursor, VS Code, etc.)
  + Some MCP clients may require a paid subscription if you use the MCP server frequently

## Available Endpoints

Alpaca’s MCP Server offers 43 functions (endpoints) of Trading API. We are optimizing and expanding the capabilities of our MCP server.

| Category | Function name | Description |
| --- | --- | --- |
| Account | get\_account\_info | Retrieves current account information including balances, buying power, and account status. |
| Positions | get\_all\_positions | Retrieves all current positions in the portfolio with details like quantity, market value, and P&L. |
| Positions | get\_open\_position | Retrieves detailed information for a specific open position. |
| Portfolio History | get\_portfolio\_history | Retrieves account portfolio history with equity and P&L over a requested time window. |
| Assets | get\_asset | Retrieves detailed information about a specific asset including trading status and attributes. |
| Assets | get\_all\_assets | Retrieves all available assets with optional filtering by status, class, and exchange. |
| Watchlist | create\_watchlist | Creates a new watchlist with specified symbols for tracking assets. |
| Watchlist | get\_watchlists | Retrieves all watchlists for the account with their symbols. |
| Watchlist | update\_watchlist\_by\_id | Updates an existing watchlist by modifying names or symbols. |
| Watchlist | get\_watchlist\_by\_id | Get a specific watchlist by its ID. |
| Watchlist | add\_asset\_to\_watchlist\_by\_id | Add an asset by symbol to a specific watchlist by ID. |
| Watchlist | remove\_asset\_from\_watchlist\_by\_id | Remove an asset by symbol from a specific watchlist by ID. |
| Watchlist | delete\_watchlist\_by\_id | Delete a specific watchlist by its ID. |
| Corporate Actions | get\_corporate\_actions | Retrieves corporate action announcements like earnings, dividends, and stock splits. |
| Calendar | get\_calendar | Retrieves market calendar for specified date range showing trading days and holidays. |
| Clock | get\_market\_clock | Retrieves current market status and next open or close times. |
| Market Data (Stock) | get\_stock\_bars | Retrieves historical stock price bars with OHLCV data using flexible timeframes. |
| Market Data (Stock) | get\_stock\_quote | Retrieves the historical quote for a stock including bid or ask prices and volumes. |
| Market Data (Stock) | get\_stock\_trades | Retrieves historical trade data for a stock with individual trade details. |
| Market Data (Stock) | get\_stock\_latest\_bar | Retrieves the most recent minute bar for a stock. |
| Market Data (Stock) | get\_stock\_latest\_quote | Retrieves the latest quote for a stock including bid or ask prices and volumes. |
| Market Data (Stock) | get\_stock\_latest\_trade | Retrieves the latest trade information for a stock. |
| Market Data (Stock) | get\_stock\_snapshot | Retrieves comprehensive snapshot with latest quote, trade, minute bar, daily bar, and previous daily bar. |
| Market Data (Crypto) | get\_crypto\_bars | Retrieves historical cryptocurrency price bars with OHLCV data. |
| Market Data (Crypto) | get\_crypto\_quotes | Retrieves historical cryptocurrency quote data with bid or ask information. |
| Market Data (Crypto) | get\_crypto\_trades | Retrieves historical trade prints for one or more cryptocurrencies. |
| Market Data (Crypto) | get\_crypto\_latest\_quote | Returns the latest quote for one or more crypto symbols. |
| Market Data (Crypto) | get\_crypto\_latest\_bar | Returns the latest minute bar for one or more crypto symbols. |
| Market Data (Crypto) | get\_crypto\_latest\_trade | Returns the latest trade for one or more crypto symbols. |
| Market Data (Crypto) | get\_crypto\_snapshot | Returns snapshots including latest trade, quote, minute bar, daily and previous daily bars for crypto symbols. |
| Market Data (Crypto) | get\_crypto\_latest\_orderbook | Returns the latest orderbook for one or more crypto symbols. |
| Market Data (Options) | get\_option\_contracts | Searches for option contracts with flexible filtering by expiration, strike price, and type. |
| Market Data (Options) | get\_option\_latest\_quote | Retrieves the latest quote for an option contract with bid or ask prices and Greeks. |
| Market Data (Options) | get\_option\_snapshot | Retrieves comprehensive snapshots of option contracts including latest trade, quote, implied volatility, and Greeks. |
| Trading (Orders) | get\_orders | Retrieves order history with filtering options by status, date range, and limits. |
| Trading (Orders) | place\_stock\_order | Places a stock order with support for market, limit, stop, stop limit, and trailing stop orders. |
| Trading (Orders) | place\_crypto\_order | Places a cryptocurrency order with support for market, limit, and stop limit orders. |
| Trading (Orders) | place\_option\_market\_order | Places option orders including single leg and multi leg strategies like spreads and straddles. |
| Trading (Orders) | cancel\_all\_orders | Cancels all open orders and returns the status of each cancellation. |
| Trading (Orders) | cancel\_order\_by\_id | Cancels a specific order by its ID. |
| Trading (Positions) | close\_position | Closes a specific position for a single symbol, either partially or completely. |
| Trading (Positions) | close\_all\_positions | Closes all open positions in the portfolio. |
| Trading (Positions) | exercise\_options\_position | Exercises a held option contract, converting it into the underlying asset. |

## Important Considerations When Trading with Alpaca’s MCP Server

Using Alpaca’s MCP Server introduces a few important considerations:

1. Make sure your Alpaca API keys are linked to the correct account type such as live or paper.
2. Some AI tools (MCP clients) may require a paid subscription if you use the MCP Server frequently.
3. Review and confirm orders directly on your Alpaca dashboard. You can do this in real time to ensure accuracy before or after submitting trades.

## Security Considerations for Remote MCP Server Deployment

Running an MCP server remotely introduces a few important security considerations. Many early stage examples such as FastMCP are designed for local testing and may not include authentication or encrypted communication by default.

When a server is publicly accessible, it is possible for external requests to reach it. If the server handles sensitive information such as Alpaca Trading API keys, this can create a risk of unauthorized access or unintended tool execution.

To reduce these risks, a secure deployment should include HTTPS or TLS for encrypted communication and a reliable token based authentication method. Taking these steps helps protect your credentials and ensures that only trusted clients can interact with your MCP server.

  

## Disclosure

*Insights generated by our MCP server and connected AI agents are for educational and informational purposes only and should not be taken as investment advice. Past performance from models does not guarantee future results. Please conduct your own due diligence before making any decisions..*

Updated 21 days ago

---

Ask AI

---

# About Market Data API (https://docs.alpaca.markets/docs/about-market-data-api)

# About Market Data API

Gain seamless access to a wealth of data with Alpaca Market Data API, offering real-time and historical information for equities, options, crypto and more.

# Overview

The Market Data API offers seamless access to market data through both HTTP and WebSocket protocols. With a focus on historical and real-time data, developers can efficiently integrate these APIs into their applications.

To simplify the integration process, we provide user-friendly SDKs in [Python](https://github.com/alpacahq/alpaca-py), [Go](https://github.com/alpacahq/alpaca-trade-api-go), [NodeJS](https://github.com/alpacahq/alpaca-trade-api-js), and [C#](https://github.com/alpacahq/alpaca-trade-api-csharp). These SDKs offer comprehensive functionalities, making it easier for developers to work with the Market Data APIs & Web Sockets.

To experiment with the APIs, developers can try them with [Postman](https://www.postman.com/): either through the [public workspace on Postman](https://www.postman.com/alpacamarkets) or directly from our [GitHub repository](https://github.com/alpacahq/alpaca-postman).

By leveraging Alpaca Market Data API and its associated SDKs, developers can seamlessly incorporate historical and real-time market data into their applications, enabling them to build powerful and data-driven financial products.

# Subscription Plans

Alpaca offers two distinct subscription models depending on how you access our platform:

* **Trading API:** For individual traders using Alpaca's trading platform directly
* **Broker API:** For broker partners building their own trading platforms on top of Alpaca's infrastructure

> ℹ️
>
> Which one applies to me?
>
> If you signed up for an Alpaca account to trade or build a personal trading app, you're using the Trading API. If you're a business integrating Alpaca as your backend brokerage provider, you're using the Broker API.

## Trading API Subscriptions

For individual traders and developers using Alpaca's Trading API, we offer two subscription plans: **Basic** and **Algo Trader Plus**.

The **Basic** plan serves as the default option for both Paper and Live trading accounts, ensuring all users can access essential data with zero cost. However, this plan only includes limited real-time data: for equities only the IEX exchange, for options only the indicative feed. For advanced traders we recommend subscribing to **Algo Trader Plus** which includes complete market coverage for stocks and options as well.

### Equities

|  | Basic | Algo Trader Plus |
| --- | --- | --- |
| Pricing | Free | $99 / month |
| Securities coverage | US Stocks & ETFs | US Stocks & ETFs |
| Real-time market coverage | IEX | All US Stock Exchanges |
| Websocket subscriptions | 30 symbols | Unlimited |
| Historical data timeframe | Since 2016 | Since 2016 |
| Historical data limitation\* | latest 15 minutes | no restriction |
| Historical API calls | 200 / min | 10,000 / min |

Our data sources are directly fed by the CTA (Consolidated Tape Association), which is administered by NYSE (New York Stock Exchange), and the UTP (Unlisted Trading Privileges) stream, which is administered by Nasdaq. The synergy of these two sources ensures comprehensive market coverage, encompassing 100% of market volume.

### Options

|  | Basic | Algo Trader Plus |
| --- | --- | --- |
| Securities coverage | US Options Securities | US Options Securities |
| Real-time market coverage | Indicative Pricing Feed | OPRA Feed |
| Websocket subscriptions | 200 quotes | 1000 quotes |
| Historical data limitation\* | latest 15 minutes | no restriction |
| Historical API calls | 200 / min | 10,000 / min |

Our options data sources are directly fed by OPRA (Options Price Reporting Authority).

## Broker API Subscriptions

For broker partners integrating Alpaca's Broker API, we offer tiered subscription plans designed for higher-volume, multi-user platforms.

For equities, the below subscription plans are available.

| Subscription Name | RPM (Request Per Minute) | Stream Connection Limit | Stream Symbol Limit | Price (per month) | Options Indicative Feed |
| --- | --- | --- | --- | --- | --- |
| Standard | 1,000 | 5 | unlimited | included | additional $1,000 per month |
| StandardPlus3000 | 3,000 | 5 | unlimited | $500 | additional $1,000 per month |
| StandardPlus5000 | 5,000 | 5 | unlimited | $1,000 | included |
| StandardPlus10000 | 10,000 | 10 | unlimited | $2,000 | included |

Note: Standard subscription plans will only be active when integration starts. Prior to that, the account will be on the Basic plan listed above. Additionally, similar to the free plan all the standard plans are real time IEX or 15 mins delayed SIP.

For partners on the Standard and StandardPlus3000 plans, an additional subscription fee of $1,000 / month enables access to the same equities plan for options. For StandardPlus5000 and StandardPlus10000 plans, options are included.

> 📘
>
> We offer custom pricing and tailored solutions for Broker API partners seeking to leverage our comprehensive market data. Our goal is to meet the specific needs and requirements of our valued partners, ensuring they have access to the data and tools necessary to enhance their services and provide exceptional value to their customers. If none of the subscription plans listed above are believed to be suitable, kindly reach out to our [sales team](https://alpaca.markets/contact).

# Authentication

With the exception of historical crypto data, all market data endpoints require authentication. Authentication differs between the Trading & Broker API. API keys can be acquired in the web UI (under the API keys on the right sidebar).

### Trading API

You should authenticate by passing the key / secret pair in the HTTP request headers named:

* `APCA-API-KEY-ID`
* `APCA-API-SECRET-KEY`

### Broker API

Broker API uses the [Client Credentials](https://docs.alpaca.markets/docs/authentication#client-credentials) authentication flow. You must first exchange your credentials for a short-lived access token, then use that token to authenticate API requests.

* Step 1: Request an access token

cURL

```
curl -X POST "https://authx.alpaca.markets/v1/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials" \
     -d "client_id={YOUR_CLIENT_ID}" \
     -d "client_secret={YOUR_CLIENT_SECRET}"
```

* Step 2: Use the token to authenticate

cURL

```
curl -X GET "https://data.alpaca.markets/v2/..." \
     -H "Authorization: Bearer {TOKEN}"
```

> 🚧
>
> Note: Access tokens are valid for 15 minutes. Do not request a new token for each API call.

For the WebSocket stream authentication, kindly refer to the [WebSocket Stream documentation](https://docs.alpaca.markets/docs/streaming-market-data#authentication).

Updated 25 days ago

---

Ask AI

---

# Getting Started with Market Data API (https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data)

# Getting Started with Market Data API

This is a quick guide on how to start consuming market data via APIs. Starting from beginning to end, this section outlines how to install Alpaca’s software development kit (SDK), create a free alpaca account, locate your API keys, and how to request both historical and real-time data.

# Installing Alpaca’s Client SDK

In this guide, we’ll be making use of the SDKs provided by Alpaca. Alpaca maintains SDKs in four languages: Python, JavaScript, C#, and Go. Follow the steps in the installation guide below to install the SDK of your choice before proceeding to the next section.

PythonGoJavaScriptC#

```
pip install alpaca-py
```

```
go get -u github.com/alpacahq/alpaca-trade-api-go/v3/alpaca
```

```
npm install --save @alpacahq/alpaca-trade-api
```

```
dotnet add package Alpaca.Markets
```

# Generate API Keys

Go to the [Alpaca dashboard](https://app.alpaca.markets/brokerage/dashboard/overview) and find the **API Keys** section on the right sidebar. Click on Generate New Keys and save the generated API credentials. If you have previously generated keys there and you lost the secret, you can also regenerate them here.

# How to Request Market Data Through the SDK

With the SDK installed and our API keys ready, you can start requesting market data. Alpaca offers many options for both historical and real-time data, so to keep this guide succint, these examples are on obtaining historical and real-time bar data. Information on what other data is available can be found in the Market Data API reference.

To start using the SDK for historical data, import the SDK and instantiate the crypto historical data client. It’s not required for this client to pass in API keys or a paper URL.

PythonGoJavaScript

```
from alpaca.data.historical import CryptoHistoricalDataClient

# No keys required for crypto data
client = CryptoHistoricalDataClient()
```

```
package main

import "github.com/alpacahq/alpaca-trade-api-go/v3/marketdata"

func main() {
	// No keys required for crypto data
	client := marketdata.NewClient(marketdata.ClientOpts{})
}
```

```
import Alpaca from "@alpacahq/alpaca-trade-api";

// Alpaca() requires the API key and sectret to be set, even for crypto
const alpaca = new Alpaca({
  keyId: "YOUR_API_KEY",
  secretKey: "YOUR_API_SECRET",
});
```

Next we’ll define the parameters for our request. Import the request class for crypto bars, CryptoBarsRequest and TimeFrame class to access time frame units more easily. This example queries for historical daily bar data of Bitcoin in the first week of September 2022.

PythonGoJavaScript

```
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  start=datetime(2022, 9, 1),
  end=datetime(2022, 9, 7)
)
```

```
request := marketdata.GetCryptoBarsRequest{
  TimeFrame: marketdata.OneDay,
  Start:     time.Date(2022, 9, 1, 0, 0, 0, 0, time.UTC),
  End:       time.Date(2022, 9, 7, 0, 0, 0, 0, time.UTC),
}
```

```
let options = {
  start: "2022-09-01",
  end: "2022-09-07",
  timeframe: alpaca.newTimeframe(1, alpaca.timeframeUnit.DAY),
};
```

Finally, send the request using the client’s built-in method, get\_crypto\_bars. Additionally, we’ll access the .df property which returns a pandas DataFrame of the response.

PythonGoJavaScript

```
# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
btc_bars.df
```

```
	bars, err := client.GetCryptoBars("BTC/USD", request)
	if err != nil {
		panic(err)
	}
	for _, bar := range bars {
		fmt.Printf("%+v\n", bar)
	}
```

```
(async () => {  
  const bars = await alpaca.getCryptoBars(["BTC/USD"], options);

  console.table(bars.get("BTC/USD"));
})();
```

Returns

PythonGoJavaScript

```
                                       open      high       low     close        volume  trade_count          vwap
symbol  timestamp
BTC/USD 2022-09-01 05:00:00+00:00  20055.79  20292.00  19564.86  20156.76   7141.975485     110122.0  19934.167845
        2022-09-02 05:00:00+00:00  20156.76  20444.00  19757.72  19919.47   7165.911879      96231.0  20075.200868
        2022-09-03 05:00:00+00:00  19924.83  19968.20  19658.04  19806.11   2677.652012      51551.0  19800.185480
        2022-09-04 05:00:00+00:00  19805.39  20058.00  19587.86  19888.67   4325.678790      62082.0  19834.451414
        2022-09-05 05:00:00+00:00  19888.67  20180.50  19635.96  19760.56   6274.552824      84784.0  19812.095982
        2022-09-06 05:00:00+00:00  19761.39  20026.91  18534.06  18724.59  11217.789784     128106.0  19266.835520
```

```
{Timestamp:2022-09-01 05:00:00 +0000 UTC Open:20055.79 High:20292 Low:19564.86 Close:20156.76 Volume:7141.975485 TradeCount:110122 VWAP:19934.1678446199}
{Timestamp:2022-09-02 05:00:00 +0000 UTC Open:20156.76 High:20444 Low:19757.72 Close:19919.47 Volume:7165.911879 TradeCount:96231 VWAP:20075.2008677126}
{Timestamp:2022-09-03 05:00:00 +0000 UTC Open:19924.83 High:19968.2 Low:19658.04 Close:19806.11 Volume:2677.652012 TradeCount:51551 VWAP:19800.1854803241}
{Timestamp:2022-09-04 05:00:00 +0000 UTC Open:19805.39 High:20058 Low:19587.86 Close:19888.67 Volume:4325.67879 TradeCount:62082 VWAP:19834.4514137038}
{Timestamp:2022-09-05 05:00:00 +0000 UTC Open:19888.67 High:20180.5 Low:19635.96 Close:19760.56 Volume:6274.552824 TradeCount:84784 VWAP:19812.0959815687}
{Timestamp:2022-09-06 05:00:00 +0000 UTC Open:19761.39 High:20026.91 Low:18534.06 Close:18724.59 Volume:11217.789784 TradeCount:128106 VWAP:19266.8355201911}
```

```
┌─────────┬──────────┬──────────┬──────────┬────────────┬──────────┬────────────────────────┬──────────────┬──────────────────┐
│ (index) │ Close    │ High     │ Low      │ TradeCount │ Open     │ Timestamp              │ Volume       │ VWAP             │
├─────────┼──────────┼──────────┼──────────┼────────────┼──────────┼────────────────────────┼──────────────┼──────────────────┤
│ 0       │ 20156.76 │ 20292    │ 19564.86 │ 110122     │ 20055.79 │ '2022-09-01T05:00:00Z' │ 7141.975485  │ 19934.1678446199 │
│ 1       │ 19919.47 │ 20444    │ 19757.72 │ 96231      │ 20156.76 │ '2022-09-02T05:00:00Z' │ 7165.911879  │ 20075.2008677126 │
│ 2       │ 19806.11 │ 19968.2  │ 19658.04 │ 51551      │ 19924.83 │ '2022-09-03T05:00:00Z' │ 2677.652012  │ 19800.1854803241 │
│ 3       │ 19888.67 │ 20058    │ 19587.86 │ 62082      │ 19805.39 │ '2022-09-04T05:00:00Z' │ 4325.67879   │ 19834.4514137038 │
│ 4       │ 19760.56 │ 20180.5  │ 19635.96 │ 84784      │ 19888.67 │ '2022-09-05T05:00:00Z' │ 6274.552824  │ 19812.0959815687 │
│ 5       │ 18724.59 │ 20026.91 │ 18534.06 │ 128106     │ 19761.39 │ '2022-09-06T05:00:00Z' │ 11217.789784 │ 19266.8355201911 │
└─────────┴──────────┴──────────┴──────────┴────────────┴──────────┴────────────────────────┴──────────────┴──────────────────┘
```

# Request ID

All market data API endpoint provides a unique identifier of the API call in the response header with `X-Request-ID` key, the Request ID helps us to identify the call chain in our system.

Make sure you provide the Request ID in all support requests that you created, it could help us to solve the issue as soon as possible. Request ID can't be queried in other endpoints, that is why we suggest to persist the recent Request IDs.

Shell

```
$ curl -v https://data.alpaca.markets/v2/stocks/bars
...
> GET /v2/stocks/bars HTTP/1.1
> Host: data.alpaca.markets
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Date: Fri, 25 Aug 2023 09:37:03 GMT
< Content-Type: application/json
< Content-Length: 26
< Connection: keep-alive
< X-Request-ID: 0d29ba8d9a51ee0eb4e7bbaa9acff223
<
...
```

Updated 5 months ago

---

Ask AI

---

# Historical API (https://docs.alpaca.markets/docs/historical-api)

# Historical API

This RESTful API provides historical market data through the HTTP protocol. This allows you to query historical market information, which can be used for charting, backtesting and to power your trading strategies.

Historical market data is available for the following types:

* [Stocks](https://docs.alpaca.markets/docs/historical-stock-data-1)
* [Crypto](https://docs.alpaca.markets/docs/historical-crypto-data-1)
* [Options](https://docs.alpaca.markets/docs/historical-option-data)
* [News](https://docs.alpaca.markets/docs/historical-news-data)

# Base URL

The Base URL for the historical endpoints is

```
https://data.alpaca.markets/{version}
```

Sandbox URL (for broker partners):

```
https://data.sandbox.alpaca.markets/{version}
```

Updated 5 months ago

---

Ask AI

---

# Historical Stock Data (https://docs.alpaca.markets/docs/historical-stock-data-1)

# Historical Stock Data

This API provides historical market data for equities. Check the [API Reference](https://docs.alpaca.markets/reference/stockbars) for detailed descriptions of all REST endpoints.

# Data Sources

Alpaca offers market data from various data sources described below. You can use the `feed` parameter on all the stock endpoints to switch between them.

| Source | Description |
| --- | --- |
| **iex** | IEX ([The Investors Exchange](https://www.iexexchange.io/)) is ideal for initial app testing and situations where precise pricing may not be the primary focus. It's a single US exchange that accounts for approximately ~2.5% of the market volume.  ℹ️ This is the only feed that can be used without a subscription. |
| **sip** | This feed covers all US exchanges, originating directly from exchanges and is consolidated by the Securities Information Processors: [UTP](https://utpplan.com/) (Nasdaq) and [CTA](https://www.nyse.com/data/cta) (NYSE). These SIPs play a crucial role in connecting various U.S. markets, processing and consolidating all bid/ask quotes and trades from multiple trading venues into a single, easily accessible data feed.  Our data delivery ensures ultra-low latency and high reliability, as the information is transmitted directly to Alpaca's bare metal servers located in New Jersey, situated alongside many market participants.  SIP data is particularly advantageous for developing your trading app, where precise and up-to-date price information is essential for traders and internal operations. It accounts for 100% of the market volume, providing comprehensive coverage for your trading needs. |
| **boats** | [Blue Ocean ATS](https://blueocean-tech.io/) is the first alternative trading system to expand market hours, filling the gap to trade equities continuously throughout US evening hours. |
| **overnight** | Our "overnight" feed is Alpaca's derived feed from the original BOATS source. It offers a cheaper, but slightly less accurate alternative for overnight US market data. The trades are 15 minutes delayed and adjusted to fit the bid-ask spread. |

Updated 13 days ago

---

Ask AI

---

# Historical Crypto Data (https://docs.alpaca.markets/docs/historical-crypto-data-1)

# Historical Crypto Data

This API provides historical market data for crypto. Check the [API Reference](https://docs.alpaca.markets/reference/cryptobars-1) for the detailed descriptions of all the endpoints.

Since Alpaca now executes all crypto orders in its own exchange, the v1beta3 crypto market data endpoints no longer distribute data from other providers, but from Alpaca itself.

> 📘
>
> ### Crypto bars contain quote mid-prices
>
> Due to the volatility of some currencies, including lack of trade volume at any given time, we include the quote midpoint prices in the bars to offer a better data experience. If in a bar no trade happens, the volume will be 0, but the prices will be determined by the quote prices.

Updated 5 months ago

---

Ask AI

---

# Historical Option Data (https://docs.alpaca.markets/docs/historical-option-data)

# Historical Option Data

This API provides historical market data for options. Check the [API Reference](https://docs.alpaca.markets/reference/optionbars) for the detailed descriptions of all the endpoints.

> 🚧
>
> ### Data availability
>
> Currently we only offer historical option data since February 2024.

# Data sources

Similarly to stocks, Alpaca offers two different data sources for options:

| Source | Description |
| --- | --- |
| **Indicative** | Indicative Pricing Feed is a free derivative of the original OPRA feed: the quotes are not actual OPRA quotes, they’re just indicative derivatives. The trades are also derivatives and they’re delayed by 15 minutes. |
| **OPRA (Options Price Reporting Authority)** | OPRA is the consolidated BBO feed of OPRA. [OPRA Plan](https://www.opraplan.com/document-library) defines the BBO as the highest bid and lowest offer for a series of options available in one or more of the options markets maintained by the parties. OPRA feed is only available to subscribed users. |

Updated 5 months ago

---

Ask AI

---

# Historical News Data (https://docs.alpaca.markets/docs/historical-news-data)

# Historical News Data

This API provides historical news data dating back to 2015. You can expect to receive an average of 130+ news articles per day. All news data is currently provided directly by [Benzinga](https://www.benzinga.com/). With a single endpoint, you can request news for both stocks and cryptocurrency tickers. Check the [API Reference](https://docs.alpaca.markets/reference/news-3) for the detailed descriptions the endpoint.

# Use Cases

News API is a versatile tool that can be used to support a variety of use cases, such as building an app with the Broker API or Algorithmic Trading using Sentiment Analysis on News with the Trading API.

1. **News Widgets**

   News API can be used to create visual news widgets for web and mobile apps. These widgets can be used to display the latest news for any stock or crypto symbol, and they include different sized images to give your app a visual appeal.
2. **News Sentiment Analysis**  
   News API can be used to train models that can determine the sentiment of a given headline or news content. This can be done by using historical data from News API to train the model on a variety of different sentiment labels.
3. **Realtime Trading on News**  
   [Real-time news over WebSockets](https://docs.alpaca.markets/edit/streaming-real-time-news) can be used to enable your trading algorithms to react to the latest news across any stock or cryptocurrency.

Updated 5 months ago

---

Ask AI

---

# WebSocket Stream (https://docs.alpaca.markets/docs/streaming-market-data)

# WebSocket Stream

This API provides a [WebSocket](https://en.wikipedia.org/wiki/WebSocket) stream for real-time market data. This allows you to receive the most up-to-date market information, which can be used to power your trading strategies.

The WebSocket stream provides real-time updates of the following market data:

* [Stocks](https://docs.alpaca.markets/docs/real-time-stock-pricing-data)
* [Crypto](https://docs.alpaca.markets/docs/real-time-crypto-pricing-data)
* [Options](https://docs.alpaca.markets/docs/real-time-option-data)
* [News](https://docs.alpaca.markets/docs/streaming-real-time-news)

# Steps to use the stream

To use the WebSocket stream follow these steps:

## Connection

To establish a connection use the stream URL depending on the data you'd like to consume. The general schema of the URL is

```
wss://stream.data.alpaca.markets/{version}/{feed}
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/{version}/{feed}
```

Any attempt to access a data feed not available for your subscription will result in an error during authentication.

> 📘
>
> ### Test stream
>
> We provide a test stream that is available all the time, even outside market hours, on this URL:
>
> ```
> wss://stream.data.alpaca.markets/v2/test
> ```
>
> Use the symbol "FAKEPACA" when trying out this test stream.

Upon successfully connecting, you will receive the welcome message:

JSON

```
[{"T":"success","msg":"connected"}]
```

> 🚧
>
> ### Connection limit
>
> The number of connections to a single endpoint from a user is limited based on the user's subscription, but in most subscriptions (including Algo Trader Plus) this limit is 1. If you try to open a second connection, you'll get this error:
>
> JSON
>
> ```
> [{"T":"error","code":406,"msg":"connection limit exceeded"}]
> ```

## Authentication

You need to authenticate yourself using your credentials. This can be done multiple ways

### For the Trading API, Authenticate with HTTP headers

You can set the same headers used for the historical market data and trading endpoints:

* `APCA-API-KEY-ID`
* `APCA-API-SECRET-KEY`

Here's an example using a WebSocket client called [websocat](https://github.com/vi/websocat):

```
$ websocat wss://stream.data.alpaca.markets/v2/test \
  -H="APCA-API-KEY-ID: {KEY_ID}" -H="APCA-API-SECRET-KEY: {SECRET}"
```

### For the Broker API, Authenticate with Basic Authentication

You can use the same Basic Authentication header used for the historical market data and trading endpoints:

* `Authorization` = `base64encode({KEY}:{SECRET})`

**Note:** `base64encode({KEY_ID}:{SECRET})` is the base64 encoding of the `{KEY}:{SECRET}` string.

### For both Trading & Broker API, Authenticate with a message

Alternatively, for both the trading & broker API, you can authenticate with a message after connection:

JSON

```
{"action": "auth", "key": "{KEY_ID}", "secret": "{SECRET}"}
```

Keep in mind though, that you only have 10 seconds to do so after connecting.

If you provided correct credentials you will receive another success message:

JSON

```
[{"T":"success","msg":"authenticated"}]
```

### For OAuth applications, Authenticate with a message

For an OAuth integration, authenticate with a message and use “oauth” as your key, and user token as the “secret”. (do NOT use your Client Secret)

json

```
{"action": "auth", "key": "oauth", "secret": "{TOKEN}"}
```

Keep in mind that most users can have only 1 active stream connection. If that connection is used by another 3rd party application, you will receive an error: 406 and “connection limit exceeded” message. Similarly, if the user wants to access their stream from an API or another 3rd party application, they will also receive the same error message.

## Subscription

Congratulations, you are ready to receive real-time market data!

You can send one or more subscription messages. The general format of the subscribe message is this:

JSON

```
{
  "action": "subscribe",
  "<channel1>": ["<SYMBOL1>"],
  "<channel2>": ["<SYMBOL2>","<SYMBOL3>"],
  "<channel3>": ["*"]
}
```

You can subscribe to a particular symbol or to every symbol using the `*` wildcard. A subscribe message should contain what subscription you want to add to your current subscriptions in your session so you don’t have to send what you’re already subscribed to.

For example in the test stream, you can send this message:

JSON

```
{"action":"subscribe","trades":["FAKEPACA"]}
```

The available channels are described for each streaming endpoints separately.

Much like subscribe you can also send an unsubscribe message that subtracts the list of subscriptions specified from your current set of subscriptions.

JSON

```
{"action":"unsubscribe","quotes":["FAKEPACA"]}
```

After subscribing or unsubscribing you will receive a message that describes your current list of subscriptions.

JSON

```
[{"T":"subscription","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["*"],"updatedBars":[],"dailyBars":["VOO"],"statuses":["*"],"lulds":[],"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
```

You will always receive your entire list of subscriptions, as illustrated by the sample communication excerpt below:

JSON

```
> {"action": "subscribe", "trades": ["AAPL"], "quotes": ["AMD", "CLDR"], "bars": ["*"]}
< [{"T":"subscription","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["*"],"updatedBars":[],"dailyBars":[],"statuses":[],"lulds":[],"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
...
> {"action": "unsubscribe", "bars": ["*"]}
< [{"T":"subscription","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":[],"updatedBars":[],"dailyBars":[],"statuses":[],"lulds":[],"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
```

# Messages

## Format

Every message you receive from the server will be in the format:

json

```
[{"T": "{message_type}", {contents}},...]
```

Control messages (i.e. where `T` is `error`, `success` or `subscription`) always arrive in arrays of size one to make their processing easier.

Data points however may arrive in arrays that have a length that is greater than one. This is to facilitate clients whose connection is not fast enough to handle data points sent one by one. Our server buffers the outgoing messages but slow clients may get disconnected if their buffer becomes full.

## Content type

You can use the `Content-Type` header to switch between text and binary message [data frame](https://datatracker.ietf.org/doc/html/rfc6455#section-5.6):

* `Content-Type: application/json`
* `Content-Type: application/msgpack`

## Encoding and Compression

Messages over the websocket are in encoded as clear text.

To reduce bandwidth requirements we have implemented compression as per [RFC-7692](https://datatracker.ietf.org/doc/html/rfc7692). [Our SDKs](doc:sdks-and-tools) handle this for you so in most cases you won’t have to implement anything yourself.

## Errors

You may receive an error during your session. Below are the general errors you may run into.

| Code | Message | Description |
| --- | --- | --- |
| 400 | invalid syntax | The message you sent to the server did not follow the specification.  ⚠️ This can also be sent if the symbol in your subscription message is in invalid format. |
| 401 | not authenticated | You have attempted to subscribe or unsubscribe before [authentication](https://docs.alpaca.markets/docs/streaming-market-data#authentication). |
| 402 | auth failed | You have provided invalid authentication credentials. |
| 403 | already authenticated | You have already successfully authenticated during your current session. |
| 404 | auth timeout | You failed to successfully authenticate after connecting. You only have a few seconds to authenticate after connecting. |
| 405 | symbol limit exceeded | The symbol subscription request you sent would put you over the limit set by your subscription package. If this happens your symbol subscriptions are the same as they were before you sent the request that failed. |
| 406 | connection limit exceeded | You already have the number of sessions allowed by your subscription. |
| 407 | slow client | You may receive this if you are too slow to process the messages sent by the server. Please note that this is not guaranteed to arrive before you are disconnected to avoid keeping slow connections active forever. |
| 409 | insufficient subscription | You have attempted to access a data source not available in your subscription package. |
| 410 | invalid subscribe action for this feed | You tried to subscribe to channels not available in the stream, for example to `bars` in the [option stream](https://docs.alpaca.markets/docs/real-time-option-data) or to `trades` in the [news stream](https://docs.alpaca.markets/docs/streaming-real-time-news). |
| 500 | internal error | An unexpected error occurred on our end. Please let us know if this happens. |

Beside these there can be some endpoint specific errors, for example in the [option stream](https://docs.alpaca.markets/docs/real-time-option-data#errors).

# Example

Here's a complete example of the test stream using the [wscat](https://github.com/websockets/wscat) cli tool:

JSON

```
$ wscat -c wss://stream.data.alpaca.markets/v2/test
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action":"auth","key":"<YOUR API KEY>","secret":"<YOUR API SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe","bars":["FAKEPACA"],"quotes":["FAKEPACA"]}
< [{"T":"subscription","trades":[],"quotes":["FAKEPACA"],"bars":["FAKEPACA"]}]
< [{"T":"q","S":"FAKEPACA","bx":"O","bp":133.85,"bs":4,"ax":"R","ap":135.77,"as":5,"c":["R"],"z":"A","t":"2024-07-24T07:56:53.639713735Z"}]
< [{"T":"q","S":"FAKEPACA","bx":"O","bp":133.85,"bs":4,"ax":"R","ap":135.77,"as":5,"c":["R"],"z":"A","t":"2024-07-24T07:56:58.641207127Z"}]
< [{"T":"b","S":"FAKEPACA","o":132.65,"h":136,"l":132.12,"c":134.65,"v":205,"t":"2024-07-24T07:56:00Z","n":16,"vw":133.7}]
```

Updated 5 months ago

---

Ask AI

---

# Real-time Stock Data (https://docs.alpaca.markets/docs/real-time-stock-pricing-data)

# Real-time Stock Data

This API provides stock market data on a websocket stream. This helps receive the most up to date market information that could help your trading strategy to act upon certain market movements. If you wish to access the latest pricing data, using the stream provides much better accuracy and performance than polling the latest historical endpoints.

You can find the general description of the real-time WebSocket Stream [here](https://docs.alpaca.markets/docs/streaming-market-data). This page focuses on the stock stream.

# URL

The URL for the stock stream is

```
wss://stream.data.alpaca.markets/{version}/{feed}
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/{version}/{feed}
```

Substitute `{version}/{feed}` to one of the followings:

* `v2/sip` is the SIP (Securities Information Processor) feed
* `v2/iex` is the IEX (Investors Exchange) feed
* `v2/delayed_sip` is a 15-minute delayed SIP feed
* `v1beta1/boats` is the BOATS (Blue Ocean ATS) feed
* `v1beta1/overnight` is the derived Alpaca overnight feed

These feeds are described [here](https://docs.alpaca.markets/docs/historical-stock-data-1#feed-parameter).

Any attempt to access a data feed not available for your subscription will result in an error during authentication.

# Channels

You can [subscribe](https://docs.alpaca.markets/docs/streaming-market-data#subscription) to the channels described in this section. For example

JSON

```
{"action":"subscribe","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["*"]}
```

## Trades

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “t” |
| `S` | string | symbol |
| `i` | int | trade ID |
| `x` | string | exchange code where the trade occurred |
| `p` | number | trade price |
| `s` | int | trade size |
| `c` | array`<string>` | trade condition |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "t",
  "i": 96921,
  "S": "AAPL",
  "x": "D",
  "p": 126.55,
  "s": 1,
  "t": "2021-02-22T15:51:44.208Z",
  "c": ["@", "I"],
  "z": "C"
}
```

## Quotes

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “q” |
| `S` | string | symbol |
| `ax` | string | ask exchange code |
| `ap` | number | ask price |
| `as` | int | ask size in round lots |
| `bx` | string | bid exchange code |
| `bp` | number | bid price |
| `bs` | int | bid size in round lots |
| `c` | array`<string>` | quote condition |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "q",
  "S": "AMD",
  "bx": "U",
  "bp": 87.66,
  "bs": 1,
  "ax": "Q",
  "ap": 87.68,
  "as": 4,
  "t": "2021-02-22T15:51:45.335689322Z",
  "c": ["R"],
  "z": "C"
}
```

## Bars

There are three separate channels where you can stream trade aggregates (bars).

#### Minute Bars (`bars`)

Minute bars are emitted right after each minute mark. They contain the trades from the previous minute. Trades from pre-market and aftermarket are also aggregated and sent out on the bars channel.

Note: Understanding which trades are excluded from minute bars is crucial for accurate data analysis. For more detailed information on how minute bars are calculated and excluded trades, please refer to this article [Stock Minute Bars](https://alpaca.markets/learn/stock-minute-bars/).

#### Daily Bars (`dailyBars`)

Daily bars are emitted right after each minute mark after the market opens. The daily bars contain all trades until the time they were emitted.

#### Updated Bars (`updatedBars`)

Updated bars are emitted after each half-minute mark if a “late” trade arrived after the previous minute mark. For example if a trade with a timestamp of `16:49:59.998` arrived right after `16:50:00`, just after `16:50:30` an updated bar with `t` set to `16:49:00` will be sent containing that trade, possibly updating the previous bar’s closing price and volume.

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type: “b”, “d” or “u” |
| `S` | string | symbol |
| `o` | number | open price |
| `h` | number | high price |
| `l` | number | low price |
| `c` | number | close price |
| `v` | int | volume |
| `vw` | number | volume-weighted average price |
| `n` | int | number of trades |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |

### Example

JSON

```
{
  "T": "b",
  "S": "SPY",
  "o": 388.985,
  "h": 389.13,
  "l": 388.975,
  "c": 389.12,
  "v": 49378,
  "n": 461,
  "vw": 389.062639,
  "t": "2021-02-22T19:15:00Z"
}
```

## Trade Corrections

These messages indicate that a previously sent trade was incorrect and they contain the corrected trade.

Subscription to trade corrections and cancel/errors is automatic when you subscribe to the trade channel.

```
{"action":"subscribe","trades":["AAPL"]}
[{"T":"subscription","trades":["AAPL"],"quotes":[],"bars":[],"updatedBars":[],"dailyBars":[],"statuses":[],"lulds":[],
"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
```

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type, always “c” |
| `S` | string | symbol |
| `x` | string | exchange code |
| `oi` | int | original trade id |
| `op` | number | original trade price |
| `os` | int | original trade size |
| `oc` | array`<string>` | original trade conditions |
| `ci` | int | corrected trade id |
| `cp` | number | corrected trade price |
| `cs` | int | corrected trade size |
| `cc` | array`<string>` | corrected trade conditions |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "c",
  "S": "EEM",
  "x": "M",
  "oi": 52983525033527,
  "op": 39.1582,
  "os": 440000,
  "oc": [
    " ",
    "7"
  ],
  "ci": 52983525034326,
  "cp": 39.1809,
  "cs": 440000,
  "cc": [
    " ",
    "7"
  ],
  "z": "B",
  "t": "2023-04-06T14:25:06.542305024Z"
}
```

## Trade Cancels/Errors

These messages indicate that a previously sent trade was canceled.

Subscription to trade corrections and cancel/errors is automatic when you subscribe to the trade channel.

```
{"action":"subscribe","trades":["AAPL"]}
[{"T":"subscription","trades":["AAPL"],"quotes":[],"bars":[],"updatedBars":[],"dailyBars":[],"statuses":[],"lulds":[],
"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
```

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type, always “x” |
| `S` | string | symbol |
| `i` | int | trade id |
| `x` | string | trade exchange |
| `p` | number | trade price |
| `s` | int | trade size |
| `a` | string | action (“C” for cancel, “E” for error) |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "x",
  "S": "GOOGL",
  "i": 465,
  "x": "D",
  "p": 105.31,
  "s": 300,
  "a": "C",
  "z": "C",
  "t": "2023-04-06T13:15:42.83540958Z"
}
```

## LULDs

Limit Up - Limit Down messages provide upper and lower limit price bands to securities.

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type, always “l” |
| `S` | string | symbol |
| `u` | number | limit up price |
| `d` | number | limit down price |
| `i` | string | indicator |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "l",
  "S": "IONM",
  "u": 3.24,
  "d": 2.65,
  "i": "B",
  "t": "2023-04-06T13:34:45.565004401Z",
  "z": "C"
}
```

## Trading Status

Identifies the trading status applicable to the security and reason for the trading halt if any. The status messages can be accessed from any {source} depending on your subscription.

To enable market data on a production environment please reach out to our sales team.

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type, always “s” |
| `S` | string | symbol |
| `sc` | string | status code |
| `sm` | string | status message |
| `rc` | string | reason code |
| `rm` | string | reason message |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |
| `z` | string | tape |

### Example

JSON

```
{
  "T": "s",
  "S": "AAPL",
  "sc": "H",
  "sm": "Trading Halt",
  "rc": "T12",
  "rm": "Trading Halted; For information requested by NASDAQ",
  "t": "2021-02-22T19:15:00Z",
  "z": "C"
}
```

### Status Codes

#### Tape A & B (CTA)

| Code | Value |
| --- | --- |
| 2 | Trading Halt |
| 3 | Resume |
| 5 | Price Indication |
| 6 | Trading Range Indication |
| 7 | Market Imbalance Buy |
| 8 | Market Imbalance Sell |
| 9 | Market On Close Imbalance Buy |
| A | Market On Close Imbalance Sell |
| C | No Market Imbalance |
| D | No Market On Close Imbalance |
| E | Short Sale Restriction |
| F | Limit Up-Limit Down |

#### Tape C & O (UTP)

| Codes | Resume |
| --- | --- |
| H | Trading Halt |
| Q | Quotation Resumption |
| T | Trading Resumption |
| P | Volatility Trading Pause |

### Reason Codes

#### Tape A & B (CTA)

| Code | Value |
| --- | --- |
| D | News Released (formerly News Dissemination) |
| I | Order Imbalance |
| M | Limit Up-Limit Down (LULD) Trading Pause |
| P | News Pending |
| X | Operational |
| Y | Sub-Penny Trading |
| 1 | Market-Wide Circuit Breaker Level 1 – Breached |
| 2 | Market-Wide Circuit Breaker Level 2 – Breached |
| 3 | Market-Wide Circuit Breaker Level 3 – Breached |

#### Tape C & O (UTP)

| Code | Value |
| --- | --- |
| T1 | Halt News Pending |
| T2 | Halt News Dissemination |
| T5 | Single Stock Trading Pause In Affect |
| T6 | Regulatory Halt Extraordinary Market Activity |
| T8 | Halt ETF |
| T12 | Trading Halted; For information requested by NASDAQ |
| H4 | Halt Non Compliance |
| H9 | Halt Filings Not Current |
| H10 | Halt SEC Trading Suspension |
| H11 | Halt Regulatory Concern |
| 01 | Operations Halt, Contact Market Operations |
| IPO1 | IPO Issue not yet Trading |
| M1 | Corporate Action |
| M2 | Quotation Not Available |
| LUDP | Volatility Trading Pause |
| LUDS | Volatility Trading Pause – Straddle Condition |
| MWC1 | Market Wide Circuit Breaker Halt – Level 1 |
| MWC2 | Market Wide Circuit Breaker Halt – Level 2 |
| MWC3 | Market Wide Circuit Breaker Halt – Level 3 |
| MWC0 | Market Wide Circuit Breaker Halt – Carry over from previous day |
| T3 | News and Resumption Times |
| T7 | Single Stock Trading Pause/Quotation-Only Period |
| R4 | Qualifications Issues Reviewed/Resolved; Quotations/Trading to Resume |
| R9 | Filing Requirements Satisfied/Resolved; Quotations/Trading To Resume |
| C3 | Issuer News Not Forthcoming; Quotations/Trading To Resume |
| C4 | Qualifications Halt ended; maint. Req. met; Resume |
| C9 | Qualifications Halt Concluded; Filings Met; Quotes/Trades To Resume |
| C11 | Trade Halt Concluded By Other Regulatory Auth,; Quotes/Trades Resume |
| R1 | New Issue Available |
| R | Issue Available |
| IPOQ | IPO security released for quotation |
| IPOE | IPO security – positioning window extension |
| MWCQ | Market Wide Circuit Breaker Resumption |

## Order imbalances

Order imbalance is a situation resulting from an excess of buy or sell orders for a specific security on a trading exchange, making it impossible to match the orders of buyers and sellers. Order imbalance messages are typically sent during limit-up and limit-down trading halts. You have to subscribe to these messages using the `imbalances` JSON key:

JSON

```
{"action":"subscribe","imbalances":["INAQU"]}
```

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “i” |
| `S` | string | symbol |
| `p` | number | price |
| `z` | string | tape |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |

### Example

JSON

```
{
  "T": "i",
  "S": "INAQU",
  "p": 9.12,
  "z": "C",
  "t": "2024-12-13T19:58:09.242138635Z"
}
```

# Example

Shell

```
$ wscat -c wss://stream.data.alpaca.markets/v2/sip
connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "*****", "secret": "*****"}
< [{"T":"success","msg":"authenticated"}]
> {"action": "subscribe", "trades": ["AAPL"], "quotes": ["AMD", "CLDR"], "bars": ["*"],"dailyBars":["VOO"],"statuses":["*"]}
< [{"T":"subscription","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["*"],"updatedBars":[],"dailyBars":["VOO"],"statuses":["*"],"lulds":[],"corrections":["AAPL"],"cancelErrors":["AAPL"]}]
< [{"T":"q","S":"AMD","bx":"K","bp":91.95,"bs":2,"ax":"Q","ap":91.98,"as":1,"c":["R"],"z":"C","t":"2023-04-06T11:54:21.670905508Z"}]
< [{"T":"t","S":"AAPL","i":628,"x":"K","p":162.92,"s":3,"c":["@","F","T","I"],"z":"C","t":"2023-04-06T11:54:26.838232225Z"},{"T":"t","S":"AAPL","i":75,"x":"Z","p":162.92,"s":3,"c":["@","F","T","I"],"z":"C","t":"2023-04-06T11:54:26.838562809Z"},{"T":"t","S":"AAPL","i":1465,"x":"P","p":162.91,"s":71,"c":["@","F","T","I"],"z":"C","t":"2023-04-06T11:54:26.83915973Z"}]
< [{"T":"q","S":"AMD","bx":"P","bp":91.9,"bs":1,"ax":"Q","ap":91.98,"as":1,"c":["R"],"z":"C","t":"2023-04-06T11:54:27.924933876Z"}]
```

Updated 5 months ago

---

Ask AI

---

# Real-time Crypto Data (https://docs.alpaca.markets/docs/real-time-crypto-pricing-data)

# Real-time Crypto Data

Crypto Data API provides websocket streaming for trades, quotes, orderbooks, minute bars and daily bars. This helps receive the most up to date market information that could help your trading strategy to act upon certain market movements.

Alpaca executes your crypto orders in its own exchange, and also supports Kraken, which is another crypto exchange. Therefore, `v1beta3` crypto market data endpoint distributes data from Alpaca and Kraken.

You can find the general description of the real-time WebSocket Stream [here](https://docs.alpaca.markets/docs/streaming-market-data). This page focuses on the crypto stream.

> 👍
>
> ### Advanced Websockets Tutorial
>
> Check out our tutorial [Advanced Live Websocket Crypto Data Streams in Python](https://alpaca.markets/learn/advanced-live-websocket-crypto-data-streams-in-python/) for some tips on handling live crypto data stream in Python.

# URL

The URL for the crypto stream is

```
wss://stream.data.alpaca.markets/v1beta3/crypto/{loc}
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/v1beta3/crypto/{loc}
```

Possible values `{loc}` can have are:

* us - Alpaca US
* us-1 - Kraken US
* eu-1 - Kraken EU

The location us-1 represents the states listed below:

1. AL (Alabama)
2. AK (Alaska)
3. AR (Arkansas)
4. CO (Colorado)
5. DC (District of Columbia)
6. DE (Delaware)
7. FL (Florida)
8. HI (Hawaii)
9. LA (Louisiana)
10. MN (Minnesota)
11. NV (Nevada)
12. NH (New Hampshire)
13. NJ (New Jersey)
14. NM (New Mexico)
15. OK (Oklahoma)
16. OR (Oregon)
17. PA (Pennsylvania)
18. PR (Puerto Rico)
19. TN (Tennessee)
20. TX (Texas)
21. VA (Virginia)
22. WI (Wisconsin)
23. WY (Wyoming)

Please note that, at the moment `us-1` and `eu-1` stream Kraken market data (which is another crypto exchange), but the providers may change over time.

Multiple data points may arrive in each message received from the server. These data points have the following formats, depending on their type.

# Channels

## Trades

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “t” |
| `S` | string | symbol |
| `p` | number | trade price |
| `s` | number | trade size |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `i` | int | trade ID |
| `tks` | string | taker side: B for buyer, S for seller |

### Example

JSON

```
{
  "T": "t",
  "S": "AVAX/USD",
  "p": 47.299,
  "s": 29.205707815,
  "t": "2024-03-12T10:27:48.858228144Z",
  "i": 3447222699101865076,
  "tks": "S"
}
```

## Quotes

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “q” |
| `S` | string | symbol |
| `bp` | number | bid price |
| `bs` | number | bid size |
| `ap` | number | ask price |
| `as` | number | ask size |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |

### Example

JSON

```
{
  "T": "q",
  "S": "BAT/USD",
  "bp": 0.35718,
  "bs": 13445.46,
  "ap": 0.3581,
  "as": 13561.902,
  "t": "2024-03-12T10:29:43.111588173Z"
}
```

## Bars

> 📘
>
> ### Crypto bars contain quote mid-prices
>
> Due to the volatility of some currencies, including lack of trade volume at any given time, we include the quote midpoint prices in the bars to offer a better data experience. If in a bar no trade happens, the volume will be 0, but the prices will be determined by the quote prices.

There are three separate channels where you can stream trade aggregates (bars).

#### Minute Bars (`bars`)

Minute bars are emitted right after each minute mark. They contain the trades and quote midpoints from the previous minute.

#### Daily Bars (`dailyBars`)

Daily bars are emitted right after each minute mark after the market opens. The daily bars contain all trades and quote midprices until the time they were emitted.

#### Updated Bars (`updatedBars`)

Updated bars are emitted after each half-minute mark if a “late” trade arrived after the previous minute mark. For example if a trade with a timestamp of `16:49:59.998` arrived right after `16:50:00`, just after `16:50:30` an updated bar with `t` set to `16:49:00` will be sent containing that trade, possibly updating the previous bar’s closing price and volume.

### Schema

| Attribute | Type | Description |
| --- | --- | --- |
| `T` | string | message type: “b”, “d” or “u” |
| `S` | string | symbol |
| `o` | number | open price |
| `h` | number | high price |
| `l` | number | low price |
| `c` | number | close price |
| `v` | int | volume |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |

### Example

JSON

```
{
  "T": "b",
  "S": "BTC/USD",
  "o": 71856.1435,
  "h": 71856.1435,
  "l": 71856.1435,
  "c": 71856.1435,
  "v": 0,
  "t": "2024-03-12T10:37:00Z",
  "n": 0,
  "vw": 0
}
```

## Orderbooks

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “o” |
| `S` | string | symbol |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `b` | array | bids: array of `p` (price) and `s` pairs. If `s` is zero, it means that that bid entry was removed from the orderbook. Otherwise it was added or updated. |
| `a` | array | asks: array of `p` (price) and `s` pairs. If `s` is zero, it means that that ask entry was removed from the orderbook. Otherwise it was added or updated. |
| `r` | boolean | reset: if true, the orderbook message contains the whole server side orderbook. This indicates to the client that they should reset their orderbook. Typically sent as the first message after subscription. |

### Example

#### Initial full orderbook

JSON

```
{
  "T": "o",
  "S": "BTC/USD",
  "t": "2024-03-12T10:38:50.79613221Z",
  "b": [
    {
      "p": 71859.53,
      "s": 0.27994
    },
    {
      "p": 71849.4,
      "s": 0.553986
    },
    {
      "p": 71820.469,
      "s": 0.83495
    },
   ...
  ],
  "a": [
    {
      "p": 71939.7,
      "s": 0.83953
    },
    {
      "p": 71940.4,
      "s": 0.28025
    },
    {
      "p": 71950.715,
      "s": 0.555928
    },
    ...
  ],
  "r": true
}
```

`r` is true, meaning that this message contains the whole BTC/USD orderbook. It's truncated here for readability, the actual book has a lot more bids & asks.

#### Update message

json

```
{
  "T": "o",
  "S": "MKR/USD",
  "t": "2024-03-12T10:39:39.445492807Z",
  "b": [],
  "a": [
    {
      "p": 2614.587,
      "s": 12.5308
    }
  ]
}
```

This means that the ask price level 2614.587 was changed to 12.5308. If there were previously no 2614.587 ask entry in the orderbook, then it should be added, if there were, its size should be updated.

#### Remove message

JSON

```
{
  "T": "o",
  "S": "CRV/USD",
  "t": "2024-03-12T10:39:40.501160019Z",
  "b": [
    {
      "p": 0.7904,
      "s": 0
    }
  ],
  "a": []
}
```

This means that the 0.7904 bid price level should be removed from the orderbook.

# Example

```
$ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "**\***", "secret": "**\***"}
< [{"T":"success","msg":"authenticated"}]
> {"action": "subscribe", "bars": ["BTC/USD"]}
< [{"T":"subscription","trades":[],"quotes":[],"orderbooks":[],"bars":["BTC/USD"],"updatedBars":[],"dailyBars":[]}]
< [{"T":"b","S":"BTC/USD","o":26675.04,"h":26695.36,"l":26668.79,"c":26688.7,"v":3.227759152,"t":"2023-03-17T12:28:00Z","n":93,"vw":26679.5912436798}]
< [{"T":"b","S":"BTC/USD","o":26687.9,"h":26692.91,"l":26628.55,"c":26651.39,"v":11.568622108,"t":"2023-03-17T12:29:00Z","n":197,"vw":26651.7679765663}]
```

Updated 3 months ago

---

Ask AI

---

# Real-time News (https://docs.alpaca.markets/docs/streaming-real-time-news)

# Real-time News

This API provides stock market news on a websocket stream. You can find the general description of the real-time WebSocket Stream [here](https://docs.alpaca.markets/docs/streaming-market-data). This page focuses on the news stream.

# URL

The URL for the news stream is

```
wss://stream.data.alpaca.markets/v1beta1/news
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/v1beta1/news
```

# Channels

## News

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| T | string | Type of message (“n” for news) |
| id | int | News article ID |
| headline | string | Headline or title of the article |
| summary | string | Summary text for article (may be first sentence of content) |
| author | string | Original author of news article |
| created\_at | string | Date article was created in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format |
| updated\_at | string | Date article was updated in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format |
| content | string | Content of news article (might contain HTML) |
| url | string | URL of article (if applicable) |
| symbols | array`<string>` | List of related or mentioned symbols |
| source | string | Source where the news originated from (e.g. Benzinga) |

### Example

JSON

```
{
    "T": "n",
    "id": 24918784,
    "headline": "Corsair Reports Purchase Of Majority Ownership In iDisplay, No Terms Disclosed",
    "summary": "Corsair Gaming, Inc. (NASDAQ:CRSR) (“Corsair”), a leading global provider and innovator of high-performance gear for gamers and content creators, today announced that it acquired a 51% stake in iDisplay",
    "author": "Benzinga Newsdesk",
    "created_at": "2022-01-05T22:00:37Z",
    "updated_at": "2022-01-05T22:00:38Z",
    "url": "https://www.benzinga.com/m-a/22/01/24918784/corsair-reports-purchase-of-majority-ownership-in-idisplay-no-terms-disclosed",
    "content": "\u003cp\u003eCorsair Gaming, Inc. (NASDAQ:\u003ca class=\"ticker\" href=\"https://www.benzinga.com/stock/CRSR#NASDAQ\"\u003eCRSR\u003c/a\u003e) (\u0026ldquo;Corsair\u0026rdquo;), a leading global ...",
    "symbols": ["CRSR"],
    "source": "benzinga"
}
```

# Example

JSON

```
$ websocat -H="APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H="APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_STREAM_URL}/v1beta1/news"
[{"T":"success","msg":"connected"}]
[{"T":"success","msg":"authenticated"}]
{"action":"subscribe","news":["*"]}
[{"T":"subscription","news":["*"]}]
[{"T":"n","id":40892639,"headline":"VinFast Officially Launches VF 3 Electric Vehicle In The Philippines","summary":"VinFast Auto has officially opened pre-orders for the VF 3 in the Philippines. From September 19 to 30, early customers who reserve the VF 3 will enjoy several attractive incentives and privileges, including a","author":"Benzinga Newsdesk","created_at":"2024-09-17T09:02:44Z","updated_at":"2024-09-17T09:02:45Z","url":"https://www.benzinga.com/news/24/09/40892639/vinfast-officially-launches-vf-3-electric-vehicle-in-the-philippines","content":"\u003cp\u003eVinFast Auto has officially opened pre-orders for the VF 3 in the Philippines.\u003c/p\u003e\u003cp\u003e\u0026nbsp;\u003c/p\u003e\u003cp\u003eFrom September 19 to 30, early customers who reserve the VF 3 will enjoy several attractive incentives and privileges, including a special price of 605,000 pesos (battery subscription) or 705,000 pesos (battery included). After this period, the prices will revert to the MSRP of 645,000 pesos (battery subscription) and 745,000 pesos (battery included).\u003cbr\u003e\u003cbr\u003eAdditionally, early VF 3 customers will have the privilege of choosing from nine striking exterior paint colors, including four base colors and five premium options, free of charge. Premium paint colors will cost an additional 20,000 pesos after this period.\u003cbr\u003e\u003cbr\u003eMoreover, from September 19 to 30, for only 40,000 pesos, early customers can customize their car's paint beyond the nine available colors. This will be the only time VinFast offers this exclusive privilege for the VF 3.\u003cbr\u003e\u003cbr\u003eVinFast is accepting deposits of 5,000 pesos through its official website or at authorized dealerships (refundable under VinFast's terms).\u003cbr\u003e\u0026nbsp;\u003c/p\u003e","symbols":["VFS"],"source":"benzinga"}]
```

Updated 5 months ago

---

Ask AI

---

# Real-time Option Data (https://docs.alpaca.markets/docs/real-time-option-data)

# Real-time Option Data

This API provides option market data on a websocket stream. This helps receive the most up to date market information that could help your trading strategy to act upon certain market movements. If you wish to access the latest pricing data, using the stream provides much better accuracy and performance than polling the latest historical endpoints.

You can find the general description of the real-time WebSocket Stream [here](https://docs.alpaca.markets/docs/streaming-market-data). This page focuses on the option stream.

# URL

The URL for the option stream is

```
wss://stream.data.alpaca.markets/v1beta1/{feed}
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/v1beta1/{feed}
```

Substitute `indicative` or `opra` for `{feed}` depending on your subscription. The capabilities and differences for the `indicative` and `opra` subscriptions can be found [[here](https://docs.alpaca.markets/docs/about-market-data-api#options)].

Any attempt to access a data feed not available for your subscription will result in an error during authentication.

# Message format

> 🚧
>
> ### Msgpack
>
> Unlike the stock and crypto stream, the option stream is only available in [msgpack](https://msgpack.org/index.html) format. The SDKs are using this format automatically. For readability, the examples in the rest of this documentation will still be in json format (because msgpack is binary encoded).

# Channels

## Trades

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “t” |
| `S` | string | symbol |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `p` | number | trade price |
| `s` | int | trade size |
| `x` | string | exchange code where the trade occurred |
| `c` | string | trade condition |

### Example

JSON

```
{
  "T": "t",
  "S": "AAPL240315C00172500",
  "t": "2024-03-11T13:35:35.13312256Z",
  "p": 2.84,
  "s": 1,
  "x": "N",
  "c": "S"
}
```

## Quotes

### Schema

| Attribute | Type | Notes |
| --- | --- | --- |
| `T` | string | message type, always “q” |
| `S` | string | symbol |
| `t` | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `bx` | string | bid exchange code |
| `bp` | number | bid price |
| `bs` | int | bid size |
| `ax` | string | ask exchange code |
| `ap` | number | ask price |
| `as` | int | ask size |
| `c` | string | quote condition |

### Example

JSON

```
{
  "T": "q",
  "S": "SPXW240327P04925000",
  "t": "2024-03-12T11:59:38.897261568Z",
  "bx": "C",
  "bp": 9.46,
  "bs": 53,
  "ax": "C",
  "ap": 9.66,
  "as": 38,
  "c": "A"
}
```

# Errors

Other than the [general stream errors](https://docs.alpaca.markets/docs/streaming-market-data#errors), you may receive these option-specific errors during your session:

| Error Message | Description |
| --- | --- |
| `[{"T":"error","code":412,"msg":"option messages are only available in MsgPack format"}]` | Use the `Content-Type: application/msgpack` header. |
| `[{"T":"error","code":413,"msg":"star subscription is not allowed for option quotes"}]` | You cannot subscribe to `*` for option quotes (there are simply too many of them). |

Updated 5 months ago

---

Ask AI

---

# Market Data FAQ (https://docs.alpaca.markets/docs/market-data-faq)

# Market Data FAQ

Frequently Asked Questions

# General

## Why am I getting HTTP 403 (Forbidden)?

The market data endpoints return HTTP 403 if any of the following conditions are true:

* the request was not authenticated
* the provided credentials were incorrect
* the authenticated user has insufficient permissions

To fix these issues, there are two checklists, one for regular users and one for broker partners. If you're unsure which refers to you, check this [FAQ](https://docs.alpaca.markets/docs/broker-api-faq#what-is-the-difference-between-trading-api-and-broker-api). If you're still unsure, then check your access key. If it starts with the letter `C`, then you're a broker partner, otherwise you're a regular user. If you don't have an access key yet, generate it on the right-hand side of the Alpaca [dashboard](https://app.alpaca.markets/brokerage/dashboard/overview).

### Checklist for regular users

* make sure you provide your credentials in the following HTTP headers:
  + `APCA-API-KEY-ID`
  + `APCA-API-SECRET-KEY`
* make sure your credentials are valid:
  + check the key on the [web UI](https://app.alpaca.markets/brokerage/dashboard/overview)
  + when you reset your paper account, you need to regenerate your credentials
* make sure the host is `data.alpaca.markets` [for historical](https://docs.alpaca.markets/docs/historical-api#base-url) or `stream.data.alpaca.markets` [for live](https://docs.alpaca.markets/docs/streaming-market-data#connection)
* if you get a message like `subscription does not permit querying recent SIP data` in the HTTP response body, make sure you have the proper [subscription](https://docs.alpaca.markets/docs/about-market-data-api#subscription-plans)
  + for example to query any SIP trades or quotes in the last 15 minutes, you need the Algo Trader Plus subscription

### Checklist for broker partners

* make sure you provide your credentials in [HTTP basic authentication](https://docs.alpaca.markets/docs/about-market-data-api#subscription-plans)
* make sure your credentials are valid
* make sure you're using the right host based on your environment:
  + the production host is `data.alpaca.markets` [for historical](https://docs.alpaca.markets/docs/historical-api#base-url) and `stream.data.alpaca.markets` [for live](https://docs.alpaca.markets/docs/streaming-market-data#connection)
  + the sandbox host (for testing) is `data.sandbox.alpaca.markets` [for historical](https://docs.alpaca.markets/docs/historical-api#base-url) and `stream.data.sandbox.alpaca.markets` [for live](https://docs.alpaca.markets/docs/streaming-market-data#connection)
* if you get a message like `subscription does not permit querying recent SIP data` in the HTTP response body, make sure you have the proper [subscription](https://docs.alpaca.markets/docs/about-market-data-api#broker-partners)
  + for example, to query any SIP trades or quotes in the last 15 minutes, you need a special subscription

## How do I subscribe to AlgoTrader Plus?

You can subscribe to AlgoTrader Plus on the [Alpaca UI](https://app.alpaca.markets/account/plans-and-features): on the left sidebar of the main page click on "Plans & Features" and on that page click on "Upgrade to AlgoTrader Plus" inside the Market Data box.

# Stocks

## What's the difference between IEX and SIP data?

SIP is short for [Securities Information Processor](https://en.wikipedia.org/wiki/Securities_information_processor). All US exchanges are mandated by the regulators to report their activities (trades and quotes) to the consolidated tape. This is what we call SIP data.

IEX ([Investors Exchange](https://en.wikipedia.org/wiki/IEX)) is a single stock exchange.

#### [Websocket stream](doc:real-time-stock-pricing-data)

Our free market data offering includes live data only from the IEX exchange:

```
wss://stream.data.alpaca.markets/v2/iex
```

The Algo Trader Plus subscription on the other hand offers SIP data:

```
wss://stream.data.alpaca.markets/v2/sip
```

#### [Historical data](https://docs.alpaca.markets/reference/stockbars)

On the historical endpoints, use the `feed` parameter to switch between the two data feeds:

JSON

```
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=sip&timeframe=1Day&start=2023-09-29&limit=1" | jq .
{
  "bars": [
    {
      "t": "2023-09-29T04:00:00Z",
      "o": 172.02,
      "h": 173.07,
      "l": 170.341,
      "c": 171.21,
      "v": 51861083,
      "n": 535134,
      "vw": 171.599691
    }
  ],
  "symbol": "AAPL",
  "next_page_token": "QUFQTHxEfDIwMjMtMDktMjlUMDQ6MDA6MDAuMDAwMDAwMDAwWg=="
}
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=iex&timeframe=1Day&start=2023-09-29&limit=1" | jq .
{
  "bars": [
    {
      "t": "2023-09-29T04:00:00Z",
      "o": 172.015,
      "h": 173.06,
      "l": 170.36,
      "c": 171.29,
      "v": 923134,
      "n": 12630,
      "vw": 171.716432
    }
  ],
  "symbol": "AAPL",
  "next_page_token": null
}
```

In this example (2023-09-29 Apple daily bar), you can clearly see the difference between the two feeds: there were **12 630** eligible trades on the IEX exchange that day and more than **535 136** trades in total across all exchanges (naturally including IEX). Similar differences can be seen between their volumes.

All the latest endpoints (including the [snapshot](https://docs.alpaca.markets/reference/stocksnapshotsingle) endpoint), require a subscription to be used with the SIP feed. For historical queries, the `end` parameter must be at least 15 minutes old to query SIP data without a subscription. The default value for `feed` is always the "best" available feed based on the user's subscription.

JSON

```
$  curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/trades/latest" | jq .
{
  "symbol": "AAPL",
  "trade": {
    "t": "2023-09-29T19:59:59.246196362Z",
    "x": "V",  // << IEX exchange code
    "p": 171.29,
    "s": 172,
    "c": [
      "@"
    ],
    "i": 12727,
    "z": "C"
  }
}
$ curl -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/trades/latest?feed=sip"
{"code":42210000,"message":"subscription does not permit querying recent SIP data"}
```

In this example, we're querying the latest AAPL trade without a subscription. The default `feed` in this case is `iex`. If we were to try to query the SIP feed, we would get an error. To fix that error, we need to subscribe to [Algo Trader Plus](https://docs.alpaca.markets/docs/about-market-data-api#subscription-plans).

## Why can't I find market data for a particular symbol (e.g. CGRNQ)?

### OTC

Make sure the symbol is not traded in OTC using the [assets endpoint](https://docs.alpaca.markets/reference/get-v2-assets-symbol_or_asset_id). `https://api.alpaca.markets/v2/assets/CGRNQ` returns

JSON

```
{
  "id": "dc2d8be9-33b5-4a32-8f57-5b7d209d2c82",
  "class": "us_equity",
  "exchange": "OTC", // << This symbol is traded in OTC
  "symbol": "CGRNQ",
  "name": "CAPSTONE GREEN ENERGY CORP COM PAR $.001",
  "status": "active",
  "tradable": false,
  "marginable": false,
  "maintenance_margin_requirement": 100,
  "shortable": true,
  "easy_to_borrow": true,
  "fractionable": true,
  "attributes": []
}
```

Market data for OTC symbols can only be queried with a special subscription currently available only for broker partners. If you do have the subscription, you can use `feed=otc` to query the data.

### Inactive

Make sure the asset is active. Check the `status` field of the [same endpoint](https://docs.alpaca.markets/reference/get-v2-assets-symbol_or_asset_id).

### Halt

Make sure the symbol isn't or wasn't halted at the time you're querying. You can check the [current halts](https://www.nasdaqtrader.com/trader.aspx?id=TradeHalts) or the [historical halts](https://www.nasdaqtrader.com/Trader.aspx?id=TradingHaltSearch) on the Nasdaq website. For example, the symbol SVA has been halted since 2019-02-22.

## What happens when a ticker symbol of a company changes?

Perhaps the most famous example for this was when Facebook decided to [rename itself](https://about.fb.com/news/2021/10/facebook-company-is-now-meta/) to Meta and to change its ticker symbol from FB to META. This transition happened on 2022-06-09.

### Latest endpoints

On the latest endpoints ([latest trades](https://docs.alpaca.markets/reference/stocklatesttrades-1), [latest quotes](https://docs.alpaca.markets/reference/stocklatestquotes-1), [latest bars](https://docs.alpaca.markets/reference/stocklatestbars-1) and [snapshots](https://docs.alpaca.markets/reference/stocksnapshots-1)), the data is never manipulated in any way. These endpoints always return the data as it was received at the time (this is also why there is no `adjustment` parameter on the [latest bars](https://docs.alpaca.markets/reference/stocklatestbars-1)). So, in this case, the latest FB trade returns the last trade when the company was still called FB:

JSON

```
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" "${APCA_API_DATA_URL}/v2/stocks/trades/latest?symbols=FB" | jq .
{
  "trades": {
    "FB": {
      "c": [
        "@",
        "T"
      ],
      "i": 31118,
      "p": 196.29,
      "s": 121,
      "t": "2022-06-08T23:59:55.103033856Z",
      "x": "P",
      "z": "C"
    }
  }
}
```

Note the timestamp in the response is 2022-06-08, the night before the name change.

### Stream endpoints

The symbols always reflect the ones used by the companies at the time of the transmission on the [streaming endpoints](https://docs.alpaca.markets/edit/real-time-stock-pricing-data) as well. In practice this means that a stream client must resubscribe to the new symbol after a name change to continue receiving data. The resubscribe requires no reconnection, in the Facebook example you could simply send a [subscribe message](https://docs.alpaca.markets/docs/streaming-market-data#subscription) to META.

### Historical endpoints

On the historical endpoints we introduced the `asof` parameter to link together the data before and after the rename. By default, this parameter is "enabled", so even if you don't specify it, you will get the data for both the old and new symbol when querying the new symbol after the rename.

For the example of the FB - META rename, we can simply query the daily bars for META for the whole week (the rename happened on Thursday), yet we see the bars for Monday, Tuesday and Wednesday as well, even though on those days, the company was still called FB.

Shell

```
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11" | \
  jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

If you disable the `asof` parameter, you won't get the FB bars:

Shell

```
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11&asof=-" | \
  jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

If you set `asof` to a date before the rename, you can query by the old ticker:

Shell

```
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=FB&start=2022-06-06&end=2022-06-11&asof=2022-06-06" | \
  jq -r '.bars.FB[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

Unfortunately, the `asof` mapping is only available on our historical endpoints the day after the rename. In the FB-META example, it was available since 2022-06-10, so running the same queries on the day of the rename (2022-06-09) didn't return the FB bars. This is because of a limitation of one of our data sources. We're actively working on improving this and doing the mapping before the market opens with the new symbol.

## How are bars aggregated?

Minute and daily bars are aggregated from trades. The (SIP) timestamp of the trade is truncated to the minute for minute bars and to the day (in New York) for daily bars. For example, a trade at 14:52:28 belongs to the 14:52:00 minute bar, which contains all the trades between 14:52:00 (inclusive) and 14:53:00 (exclusive). The timestamp of the bar is the left side of the interval (14:52:00 in this example).

There are three parts of the bar that a trade can potentially update:

* open / close price
* high / low price
* volume

The rules of these updates depend on

* the tape of the trade (`A`, `B`: NYSE, `C`: Nasdaq, `O`: OTC)
* the conditions of the trade
* the type of the bar (`M`: minute, `D`: daily)
  + Some rules are different for minute and daily bars. For example `P` (Prior Reference Price) relates to an obligation to trade at an earlier point in the trading day. This will update the high / low price of a daily bar but will not update the high / low price of a minute bar, because that price possibly happened in another minute.

The rules are based on the guidelines of the SIPs:

* the [CTS specification](https://www.ctaplan.com/publicdocs/ctaplan/CTS_Pillar_Output_Specification.pdf) for NYSE (tape `A` and `B`)
* the [UTP specification](https://utpplan.com/DOC/UtpBinaryOutputSpec.pdf) for Nasdaq (tape `C`)
* the [TDDS specification](https://www.finra.org/sites/default/files/2022-05/TDDS-2.1-MOLD.pdf) for OTC (tape `O`)

The following table contains all the updating rules:

| Condition code | Condition description | Tape | Bar type | Update open / close | Update high / low | Update volume |
| --- | --- | --- | --- | --- | --- | --- |
|  | Regular Sale | AB | MD | 🟢 | 🟢 | 🟢 |
| `@` | Regular Sale | CO | MD | 🟢 | 🟢 | 🟢 |
| `A` | Acquisition | C | MD | 🟢 | 🟢 | 🟢 |
| `B` | Average Price Trade | AB | MD | 🔴 | 🔴 | 🟢 |
| `B` | Bunched Trade | C | MD | 🟢 | 🟢 | 🟢 |
| `C` | Cash Sale | ABCO | MD | 🔴 | 🔴 | 🟢 |
| `D` | Distribution | C | MD | 🟢 | 🟢 | 🟢 |
| `E` | Automatic Execution | AB | MD | 🟢 | 🟢 | 🟢 |
| `F` | Intermarket Sweep | ABC | MD | 🟢 | 🟢 | 🟢 |
| `G` | Bunched Sold Trade | C | M | 🔴 | 🔴 | 🟢 |
| `G` | Bunched Sold Trade | C | D | 🟡 | 🟢 | 🟢 |
| `H` | Price Variation Trade | ABC | MD | 🔴 | 🔴 | 🟢 |
| `I` | Odd Lot Trade | ABCO | MD | 🔴 | 🔴 | 🟢 |
| `K` | Rule 127 or Rule 155 | ABC | MD | 🟢 | 🟢 | 🟢 |
| `L` | Sold Last | ABC | MD | 🟢 | 🟢 | 🟢 |
| `M` | Market Center Official Close | ABC | MD | 🔴 | 🔴 | 🔴 |
| `N` | Next Day | ABCO | MD | 🔴 | 🔴 | 🟢 |
| `O` | Market Center Opening Trade | ABC | MD | 🟢 | 🟢 | 🟢 |
| `P` | Prior Reference Price | ABCO | M | 🔴 | 🔴 | 🟢 |
| `P` | Prior Reference Price | ABCO | D | 🟡 | 🟢 | 🟢 |
| `Q` | Market Center Official Open | ABC | MD | 🔴 | 🔴 | 🔴 |
| `R` | Seller | ABCO | MD | 🔴 | 🔴 | 🟢 |
| `T` | Extended Hours Trade | ABCO | M | 🟢 | 🟢 | 🟢 |
| `T` | Extended Hours Trade | ABCO | D | 🔴 | 🔴 | 🟢 |
| `U` | Extended Trading Hours | ABCO | MD | 🔴 | 🔴 | 🟢 |
| `V` | Contingent Trade | ABC | MD | 🔴 | 🔴 | 🟢 |
| `W` | Average Price Trade | CO | MD | 🔴 | 🔴 | 🟢 |
| `X` | Cross Trade | ABC | MD | 🟢 | 🟢 | 🟢 |
| `Y` | Yellow Flag Regular Trade | C | MD | 🟢 | 🟢 | 🟢 |
| `Z` | Sold Out Of Sequence | ABC | M | 🔴 | 🔴 | 🟢 |
| `Z` | Sold Out Of Sequence | ABC | D | 🟡 | 🟢 | 🟢 |
| `4` | Derivatively Priced | ABC | M | 🔴 | 🔴 | 🟢 |
| `4` | Derivatively Priced | ABC | D | 🟡 | 🟢 | 🟢 |
| `5` | Market Center Reopening Trade | ABC | MD | 🟢 | 🟢 | 🟢 |
| `6` | Market Center Closing Trade | ABC | MD | 🟢 | 🟢 | 🟢 |
| `7` | Qualified Contingent Trade | ABC | MD | 🔴 | 🔴 | 🟢 |
| `9` | Corrected Consolidated Close | ABC | M | 🔴 | 🔴 | 🔴 |
| `9` | Corrected Consolidated Close | ABC | D | 🟢 | 🟢 | 🔴 |

* 🟢 means that the given condition updates the value
* 🟡 means that the given condition updates the open / close price only if the trade is the first trade of the bar
* 🔴 means that the given condition does not update the value

In the original [CTS](https://www.ctaplan.com/publicdocs/ctaplan/CTS_Pillar_Output_Specification.pdf) / [UTP](https://utpplan.com/DOC/UtpBinaryOutputSpec.pdf) specifications, there are some more complicated update rules (see the footnotes in the linked specifications), but we don't use any of these. In most of the cases, we simply use 🟡 (or 🟢) instead.

A trade can have more than one condition. In this case the strictest rule is applied. For example, if a Nasdaq trade has these conditions: `@`, `4`, `I` and a daily bar is being generated, none of the prices of the bar are going to be updated (both open / close and high / low is 🔴 because it's an odd lot trade), only the volume 🟢 is going to be updated. If the trade had no `I` condition (`@` and `4` only), then the open / close price would only be updated if this is the first trade of the bar 🟡 , and both the high / low price 🟢 and the volume 🟢 would be updated. If it was a regular trade (`@`), then all of its values would be updated.

Once the combined updating rule of the trade has been calculated, the bar's fields are updated:

* Open is set if it hasn't been set yet and the update open / close rule is 🟢 or 🟡
* High is set if it hasn't been set yet or if the price of the trade is higher than the previous high and the update high / low is 🟢
* Low is set if it hasn't been set yet or if the price of the trade is lower than the previous low and the update high / low rule is 🟢
* Close is set if the update open / close rule is 🟢 or if it's 🟡 and the close price hasn't been set yet
* Volume is increased by the size of the trade if the update volume rule is 🟢
* The trade count is increased by one if the update volume rule is 🟢
* [VWAP](https://en.wikipedia.org/wiki/Volume-weighted_average_price) is the ratio of these two internal variables:
  + The volume-weighted total price is increased by the product of the trade's price and volume if both the update high / low rule and the update volume rule is 🟢
  + The total volume is increased by the size of the trade if both the update high / low rule and the update volume rule is 🟢. This means that this volume can be different from the "normal" volume field of the bar if there are trades in the bar that update the volume but not the high / low price (for example condition `R`)

Finally, the bar is only emitted if none of its fields (open, high, low, close, volume) are 0. So if there are no trades in the bar's interval, or if there's only a single `I` trade (which only updates the volume, but none of the prices), then no bar is generated.

All the other non-minute and non-daily bars are aggregated from the minute and daily bars. For example, an hour (`1Hour`) bar is aggregated from all the minute bars in the given hour and a weekly bar (`1Week`) is aggregated from all the daily bars in the given week. This aggregation no longer considers the actual trades that happened in the given interval, but instead the bars are aggregated using these rules:

* Open is the open of the first bar
* High is the maximum of the bars' high prices
* Low is the minimum of the bars' low prices
* Close is the close of the last bar
* Volume is the sum of the bars' volumes
* Trade count is the sum of the bars' trade counts
* VWAP is the volume-weighted average of the bars' VWAPs

# Crypto

## Why are there crypto bars with 0 volume / trade count?

Our crypto market data reflects trades and quotes from our own Alpaca exchange. Due to the volatility of some cryptocurrencies, including lack of trade volume at any given time, we include the quote midpoint prices to offer a better data experience. If within a bar no trade happens, the volume will be 0, but the prices will be determined by the quote prices.

Updated 5 months ago

---

Ask AI

---

# About Connect API (https://docs.alpaca.markets/docs/about-connect-api)

# About Connect API

Develop applications on Alpaca’s platform using OAuth2. Let 4M+ users with an Alpaca brokerage account connect to your app.

Develop applications on Alpaca’s platform using OAuth2. Alpaca’s OAuth allows you to seamlessly integrate financial markets into your application and expand your audience to the over 100K brokerage accounts on Alpaca’s platform.

Read Register Your App to learn how you can register your app. In addition, you can visit OAuth Integration Guide to learn more about using OAuth to connect your applications with Alpaca.

# Broker Partners

Broker partners are able to create their own OAuth service. Allow your end users to use OAuth apps like TradingView through your Broker API application. Learn more about OAuth with Broker API in the Broker API reference

# Terms of Access and Use

* You must read the terms and register in order to connect and use Alpaca’s APIs
* All API clients must authenticate with OAuth 2.0
* You may not imply that the app was developed by Alpaca.
* If you are building a commercial application that makes money (including ads, in-app purchases, etc), you must disclose it in the registration form and receive written approval.
* To allow live trading for other users, the app needs to be approved by Alpaca. Please contact [[email protected]](/cdn-cgi/l/email-protection#1b6b7a696f757e696873726b5b7a776b7a787a35767a69707e6f68).
* Live trading is allowed for the app developer user without approval.

> ❗️
>
> ### This is not an offer, solicitation of an offer, or advice to open a brokerage account.
>
> Disclosure can be found [here](https://alpaca.markets/#disclosures)

# FAQs

### Q: What can an OAuth app do?

A: OAuth allows you to manage your end-user’s Alpaca brokerage account on their behalf. This means you can create many types of financial services including automated investing, portfolio analytics and much more.

### Q: Should I use OAuth or Broker API?

A: OAuth allows you to expand your audience to users with Alpaca brokerage accounts. On the otherhand, Broker API allows you to build an application fully within your environment. Users sign up for a brokerage account under your application. If you want to create your own brokerage, automated investment app, or any app where you want to own your users, use the Broker API. If you want to build your trading service on Alpaca’s platform, use OAuth.

### Q: How secure is OAuth?

A: OAuth2 itself is very secure. However you must make sure to follow good practices in how you handle tokens. Make sure to never publicly expose your client secret and access tokens.

### Q: How to get OAuth App live?

A: You will need to register your app in the OAuth apps section of the dashboard. Learn more about Register Your App.

### Q: I’m developing an app/service targeting non-US users. Can we integrate with Alpaca’s OAuth API?

A: Alpaca’s platform supports brokerage accounts for international users. When you build an app on OAuth, all users on Alpaca’s platform will be able to use your service, including international users.

Updated 5 months ago

---

Ask AI

---

# Registering Your App (https://docs.alpaca.markets/docs/registering-your-app)

# Registering Your App

Before integrating with Alpaca, you’ll first need to create a new OAuth app under your OAuth Apps page. The OAuth Apps page is accessible from the dashboard, which requires you to login to your Alpaca brokerage account to visit.

### 1. Visit Alpaca Connect on Dashboard

![Alpaca Connect](https://files.readme.io/224a3dc-20230627_connect.png)

### 2. Click on Submit and Fill in the Details

![](https://files.readme.io/824cdd8-Screenshot_2023-05-09_at_13.41.56.png)

### 3. Obtain (and store) Your Credentials

Once you add your relevant information and create the app, you will receive your Client ID and Client Secret.

![](https://files.readme.io/7db8c14-Screenshot_2023-05-09_at_13.45.51.png)

Updated 5 months ago

---

Ask AI

---

# Using OAuth2 and Trading API (https://docs.alpaca.markets/docs/using-oauth2-and-trading-api)

# Using OAuth2 and Trading API

Alpaca implements OAuth 2.0 to allow third party applications to access Alpaca Trading API on behalf of the end-users. This document describes how you can integrate with Alpaca through OAuth.

By default once you have a valid client\_id and client\_secret, any paper account and the live account associated with the OAuth Client will be available to connect to your app. We welcome developers to build applications and products that are powered by Alpaca while also protecting the privacy and security of our users. To build using Alpaca’s APIs, please follow the guide below.

> ℹ️
>
> ### Note
>
> An single Alpaca OAuth token may authorize access to either:
>
> * One live account
> * One paper account
> * One live account and one paper account
>
> For users with multiple paper accounts, the user must go through the authorization flow separately for each account they want to connect.

# Getting the Access Token

At a high level the flow looks like this, we will go into detail about each step

1. User requests a connection between your application and Alpaca
2. User is redirected to Alpaca to login and authorize the application from inside the dashbaord
3. Alpaca grants an authorization token to your application thorugh user-agent
4. You application then makes an access token request
5. Alpaca returns an access token grant.

## 1. Request for Connection on Behalf of User

When redirecting a user to Alpaca to authorize access to your application, you’ll need to construct the authorization URL with the correct parameters and scopes.

```
GET https://app.alpaca.markets/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URL&state=SOMETHING_RANDOM&scope=account:write%20trading&env=live
```

Here’s a list of parameters you should always specify:

| Parameter | Required? | Description |
| --- | --- | --- |
| `response_type` | Required | Must be `code` to request an authorization code. |
| `client_id` | Required | The `client_id` you were provided with when registering your app |
| `redirect_uri` | Required | The redirect URL where the user will be sent after authorization. It must match one of the whitelisted redirect URIs for your application. |
| `state` | Optional | An unguessable random string, used to protect against request forgery attacks. |
| `scope` | Optional | A space-delimited list of scopes your application requests access to. Read-only endpoint access is assumed by default. |
| `env` | Optional | If provided, must be one of `live` or `paper`. If not specified, the user will be prompted to authorized both a live and a paper account. |

**Allowed Scopes**

| Scope | Description |
| --- | --- |
| `account:write` | Write access for account configurations and watchlists. |
| `trading` | Place, cancel or modify orders. |
| `data` | Access to the Data API. |

## 2. Users Authorizing App to Access Alpaca Account

After you redirect a user to Alpaca, we will display the following OAuth consent screen and ask the user to authorize your app to connect to their Alpaca account.

![](https://files.readme.io/06f62610cde297ce4ce76d38c3570190006ea4a6e4612eade17a658d03025b6b-Screenshot_2025-02-14_at_12.00.23_PM.png)

If you specify a value for the `env` parameter when redirecting to us, we will ask the user to authorize only a live or a paper account, depending on whether you specified `live` or `paper` respectivley.

For example, if specifying `env=paper` as a query parameter, we will show the following consent screen.

![](https://files.readme.io/9b92fd7ba5d76739d84d77054f4c37f453eb5f86a9fcfa66a57342d1bdef8dfb-Screenshot_2025-02-14_at_11.57.09_AM.png)

## 3. Alpaca Redirect Back to App

If the user approves access, Alpaca will redirect them back to your `redirect_uri` with a temporary `code` parameter. If you specified a state parameter in step 1, it will be returned as well. The parameter will always match the value specified in step 1. If the values don’t match, the request should not be trusted.

Example

```
GET https://example.com/oauth/callback?code=67f74f5a-a2cc-4ebd-88b4-22453fe07994&state=8e02c9c6a3484fadaaf841fb1df290e1
```

## 4. App Receives Authorization Code

You can then use this code to exchange for an access token.

## 5. App Exchanges Auth Code with Access Token

After you have received the temporary `code`, you can exchange it for an access token. This can be done by making a `POST` call to `https://api.alpaca.markets/oauth/token`

### Parameters (All Required)

| Parameter | Description |
| --- | --- |
| `grant_type` | Must be set to authorization\_code for an access token request. |
| `code` | The authorization code received in step 4 |
| `client_id` | The Client ID you received when you registered the application. |
| `client_secret` | The Client Secret you received when you registered the application. |
| `redirect_uri` | The redirect URI you used for the authorization code request. |

> 🚧
>
> ### Note
>
> This request should take place behind-the-scenes from your backend server and shouldn’t be visible to the end users for security purposes.

The content type must be application/x-www-form-urlencoded as defined in RFC.

Example request:

cURL

```
curl -X POST https://api.alpaca.markets/oauth/token \
  -d 'grant_type=authorization_code&code=67f74f5a-a2cc-4ebd-88b4-22453fe07994&client_id=fc9c55efa3924f369d6c1148e668bbe8&client_secret=5b8027074d8ab434882c0806833e76508861c366&redirect_uri=https://example.com/oauth/callback'
```

After a successful request, a valid access token will be returned in the response:

JSON

```
{
    "access_token": "79500537-5796-4230-9661-7f7108877c60",
    "token_type": "bearer",
    "scope": "account:write trading"
}
```

# API Calls

Once you have integrated and have a valid access token you can start make calls to Alpaca Trading API v2 on behalf of the end-user.

## Example Requests

A

cURL

```
curl https://api.alpaca.markets/v2/account /
  -H 'Authorization: Bearer 79500537-5796-4230-9661-7f7108877c60'
```

cURL

```
curl https://paper-api.alpaca.markets/v2/orders /
  -H 'Authorization: Bearer 79500537-5796-4230-9661-7f7108877c60'
```

The OAuth token can also be used for the trade update websockets stream.

```
{
  "action": "authenticate",
  "data": {
    "oauth_token": "79500537-5796-4230-9661-7f7108877c60"
  }
}
```

The OAuth Token can be used to authenticate for Market Data Stream. Please note that most users can have only 1 active stream connection. If that connection is used by another 3rd party application, you will receive an error: 406 and “connection limit exceeded” message.

```
{
"action": "auth",
"key": "oauth",
"secret": "79500537-5796-4230-9661-7f7108877c60"
}
```

Updated 5 months ago

---

Ask AI

---

# About FIX API (https://docs.alpaca.markets/docs/5f36ea05-b1b4-5fd1-91b5-ef51db361a4b)

# About FIX API

Alpaca FIX (Financial Information eXchange) API

# Introduction

Welcome to the Alpaca FIX (Financial Information eXchange) API! The purpose of this document is to show how the FIX messaging protocol can be used to place orders, receive order updates and trades, replace orders and cancel orders.

## Overview

Our API is based on FIX 4.2 specification. Please reach out to our support for FIX credentials.

## Hours of Operation

FIX connectivity is available between <3:30a-4a> and <8p-8:15p> New York time, Monday through Friday for equities trading. Any changes or maintenance activities will be notified via email.

Updated 5 months ago

---

Ask AI

---

# FIX Specification (https://docs.alpaca.markets/docs/fix-messages)

# FIX Specification

This document describes the implementation of the FIX 4.2 protocol used by Alpaca to enable order entry via FIX.

Version 1.0.4

## Supported Message Types

| Message | MsgType | Description |
| --- | --- | --- |
| [Logon](#logon-a) | A | Sent by FIX client to authenticate and establish the FIX session |
| [Heartbeat](#heartbeat-0) | 0 | Sent by either client or server at preset interval within the working FIX session |
| [Test Request](#test-request-1) | 1 | Sent to force a heartbeat from the opposing application |
| [Resend Request](#resend-request-2) | 2 | To request retransmission of messages which were missed |
| [Reject](#reject-3) | 3 | Response to a message that could not be processed |
| [Sequence Reset](#sequence-reset-4) | 4 | To reset the FIX session sequence number |
| [Logout](#logout-5) | 5 | To safely disconnect the connected FIX session |
| [New Order - Single](#new-order---single-d) | D | To submit a new single order |
| [Execution Report](#execution-report-8) | 8 | Sent whenever the state of the order changes |
| [Order Cancel Request](#order-cancel-request-f) | F | To request cancellation of an order |
| [Order Cancel/Replace Request](#order-cancelreplace-request-g) | G | To request modification of an order |
| [Order Cancel Reject](#order-cancel-reject-9) | 9 | Sent if the Order Cancel Request (F) or Order Cancel/Replace Request (G) could not be executed |

## Message Header

All messages should contain the following tags in the header:

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 8 | BeginString | Y | FIX.4.2 |
| 9 | BodyLength | Y | Size of the message body in bytes |
| 34 | MsgSeqNum | Y | Message sequence number |
| 35 | MsgType | Y | Message type, should be one of the types supported in this doc |
| 49 | SenderCompID | Y | Provided by Alpaca, must be present in all FIX messages. This will be returned as TargetCompID (56) in all FIX messages to clients |
| 52 | SendingTime | Y | UTC timestamp of message transmission. Precision supported: Millis, Micros, Nanos |
| 56 | TargetCompID | Y | Provided by Alpaca, must be present in all FIX messages. This will be returned as SenderCompID (49) in all FIX messages to clients |

## Message Trailer

All messages should contain the following tags in the trailer:

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 10 | CheckSum | Y | Last field in the messages with trailing `<SOH>`. Value calculated by the FIX engine from message data |

## Logon (A)

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | A - For Logon |
| 98 | EncryptMethod | Y | 0 - None, only accepted value |
| 108 | HeartBtInt | Y | Must be set to `30` for 30 seconds |
| 141 | ResetSeqNumFlag | N | Y - Resets both sender and target sequence number to 1 |

**Example FIX Message**

Logon (A)

```
|8=FIX.4.2|9=73|35=A|34=1|49=SENDER|52=20240524-16:02:42.003|56=ALPACA|98=0|108=30|141=Y|10=131|
```

## Heartbeat (0)

Sent by either client or server if no message has been received since the last heartbeat interval. This is also sent in response to a Test Request (1).

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 0 - For Heartbeat |
| 112 | TestReqID | N | Required only when Heartbeat is sent in response to a Test Request (1) |

**Example FIX Message**

Heartbeat

```
|8=FIX.4.2|9=91|35=0|49=SENDER|56=ALPACA|34=2|52=20230330-16:52:321.029|10=049|
```

## Test Request (1)

May be sent by either client or server, to force a Heartbeat (0) from the other party.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 1 - For Test Request |
| 112 | TestReqID | Y | Identifier to be returned in the resulting Heartbeat (0) |

**Example FIX Message**

Test Request

```
|8=FIX.4.2|9=91|35=1|49=SENDER|56=ALPACA|34=2|52=20230330-16:52:321.029|112=TEST|10=049|
```

## Resend Request (2)

Sent to request retransmission of messages which were missed.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 2 - For Resend Request |
| 7 | BeginSeqNo | Y | Beginning sequence number of requested messages |
| 16 | EndSeqNo | Y | Ending sequence number of requested messages |

**Example FIX Message**

Resend Request

```
|8=FIX.4.2|9=66|7=9|16=36|34=12|35=2|49=SENDER|52=20230627-14:10:21.769|56=ALPACA|10=126|
```

## Reject (3)

Sent when a message is rejected or cannot be processed by the FIX server.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 3 - For Reject |
| 45 | RefSeqNum | Y | Sequence number of the rejected message |
| 58 | Text | N | Reason for rejection |
| 371 | RefTagID | N | The tag number of the FIX field being referenced |
| 372 | RefMsgType | N | The MsgType (35) of the FIX message being referenced |
| 373 | SessionRejectReason | N | Reject reason codes.  0 - Invalid tag number  1 - Required tag missing  2 - Tag not defined for this message type  3 - Unsupported Message Type  4 - Tag specified without a value  5 - Value is incorrect (out of range) for this tag  6 - Incorrect data format for value  9 - CompID problem  10 - SendingTime accuracy problem  11 - Invalid MsgType |

**Example FIX Message**

Reject

```
|8=FIX.4.2|9=0134|35=3|34=44196|49=ALPACA|56=TARGET|52=20230330-20:18:38.039|58=0005 Tag specified without a value|45=44196|371=11|372=8|373=4|10=092|
```

## Sequence Reset (4)

Sent to reset the incoming sequence number on the other side. The sequence reset should be used only to increase the sequence number. Any request to decrease the sequence number will result in a Reject (3) message.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 4 - For Sequence Reset |
| 36 | NewSeqNo | Y | New sequence number |
| 123 | GapFillFlag | N | N - Sequence reset to recover from an out-of-sequence condition, MsgSeqNum(34) is ignored  Y - Gap fill message, MsgSeqNum(34) field must be valid |

**Example FIX Message**

Sequence Reset

```
|8=FIX.4.2|9=61|34=12|35=4|36=9|49=SENDER|52=20230627-14:14:51.732|56=ALPACA|10=156|
```

## Logout (5)

May be sent by either client or server, to terminate the session. The other party would respond with a confirming Logout message as an acknowledgement.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 5 - For Logout |

**Example FIX Message**

Logout

```
|8=FIX.4.2|9=56|34=12|35=5|49=SENDER|52=20230627-14:16:50.690|56=ALPACA|10=197|
```

## New Order - Single (D)

Sent by the client to submit a new single order.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | D - For New Order - Single |
| 1 | Account | Y | Account number |
| 11 | ClOrdID | Y | Unique identifier of the order assigned by the client (must be no longer than 48 characters) |
| 12 | Commission | N | Commission to collect from the account holder |
| 13 | CommType | N | 1 - per share  2 - percentage, 5% should be represented as .05  3 - absolute |
| 18 | ExecInst | N | 1 - Not held  5 - Held |
| 21 | HandlInst | Y | 1 - Automated execution with no broker intervention, only accepted value |
| 38 | OrderQty | N | Number of shares to trade, required if CashOrderQty (152) is not set |
| 40 | OrdType | Y | 1 - Market  2 - Limit  3 - Stop  4 - Stop limit  5 - Market on close  B - Limit on close |
| 44 | Price | N | Required for Limit `40=2` and Stop Limit `40=4` orders |
| 54 | Side | Y | 1 - Buy  2 - Sell |
| 55 | Symbol | Y | Ticker symbol |
| 59 | TimeInForce | Y | 0 - Day (day)  1 - Good Till Cancel (gtc)  2 - At the Opening (opg)  3 - Immediate or Cancel (ioc)  4 - Fill or Kill (fok)  7 - At the Close (cls) |
| 60 | TransactTime | Y | UTC timestamp of order creation by client |
| 77 | OpenClose | N | Indicates whether the resulting position from the trade would be an opening or closing position.  O - Open  C - Close |
| 99 | StopPx | N | Required for Stop `40=3` and Stop Limit `40=4` orders |
| 109 | ClientID | N | Sub-account tag for omnibus accounts |
| 152 | CashOrderQty | N | Notional value to trade, required if OrderQty (38) is not set |
| 336 | TradingSessionID | N | 8 - Extended Hours  Required for extended hours orders only |

**Example FIX Messages**

Market order (quantity based)Market order (notional based)Limit orderStop orderStop limit orderExtended Hours Order

```
|8=FIX.4.2|9=139|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=1|49=SENDER|52=20230613-14:01:37.330|54=1|55=SPY|56=ALPACA|59=1|10=030|
```

```
|8=FIX.4.2|9=141|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|40=1|49=SENDER|52=20230613-14:43:47.572|54=1|55=SPY|56=ALPACA|59=0|152=100|10=130|
```

```
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=2|44=350.78|49=SENDER|52=20230613-14:45:58.303|54=1|55=SPY|56=ALPACA|59=0|10=005|
```

```
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=3|49=SENDER|52=20230613-14:50:51.223|54=1|55=SPY|56=ALPACA|59=0|99=350.78|10=006|
```

```
|8=FIX.4.2|9=159|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=4|44=350.78|49=SENDER|52=20230613-15:26:35.992|54=1|55=SPY|56=ALPACA|59=0|99=350.78|10=246|
```

```
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=2|44=350.78|49=SENDER|52=20230613-14:45:58.303|54=1|55=SPY|56=ALPACA|59=5|10=005|
```

## Execution Report (8)

Sent by the server whenever an order receives an update. Each execution report contains field OrdStatus (39) which is used to convey the current status of the order as understood by Alpaca, as well as fields ExecType (150) and ExecTransType (20) which describe the purpose of the message.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 8 - For Execution Report |
| 1 | Account | Y | Account number |
| 6 | AvgPx | Y | Average price of all fills on this order |
| 11 | ClOrdID | Y | Unique identifier of the order as assigned by the client |
| 12 | Commission | N | Monetary commission value charged on a fill/partial fill |
| 14 | CumQty | Y | Filled quantity on the order |
| 15 | Currency | N | Account base currency, default USD |
| 17 | ExecID | Y | Unique identifier of the execution assigned by Alpaca |
| 19 | ExecRefID | N | ExecID (17) of the original execution being canceled or corrected when `20=1` or `20=2` |
| 20 | ExecTransType | Y | Transaction type.  0 - New  1 - Cancel  2 - Correct  3 - Status, for Restated (D) message upon stop trigger |
| 30 | LastMkt | N | Market of execution for this fill |
| 31 | LastPx | N | Price of this fill |
| 32 | LastShares | N | Quantity traded on this fill |
| 37 | OrderID | Y | Unique identifier of the order assigned by Alpaca |
| 38 | OrderQty | N | Either CashOrderQty (152) or OrderQty (38) is provided |
| 39 | OrdStatus | Y | Identifies current status of order.  0 - New  1 - Partially filled  2 - Filled  3 - Done for day  4 - Canceled  5 - Replaced  6 - Pending Cancel  8 - Rejected  A - Pending New  C - Expired  E - Pending Replace |
| 40 | OrdType | N | Same as specified on the order.  1 - Market  2 - Limit  3 - Stop  4 - Stop limit  5 - Market on close  B - Limit on close |
| 41 | OrigClOrdID | N | ClOrdID (11) of the original order in cancel and cancel/replace requests |
| 44 | Price | N | Sent when specified on the order |
| 54 | Side | Y | 1 - Buy  2 - Sell |
| 55 | Symbol | Y | Ticker symbol |
| 58 | Text | N | Contains reject reason when `150=8` |
| 59 | TimeInForce | N | Same as specified on the order.  0 - Day (day)  1 - Good Till Cancel (gtc)  2 - At the Opening (opg)  3 - Immediate or Cancel (ioc)  4 - Fill or Kill (fok)  7 - At the Close (cls) |
| 60 | TransactTime | N | Server time in UTC when execution occurred, nanoseconds precision |
| 99 | StopPx | N | Sent when specified on the order |
| 150 | ExecType | Y | Describes the type of execution report.  0 - New  1 - Partial fill  2 - Fill  3 - Done for day  4 - Canceled  5 - Replaced  6 - Pending Cancel, ack for Order Cancel Request (F)  8 - Rejected  A - Pending New  C - Expired  D - Restated, for stop price triggers  E - Pending Replace, ack for Order Cancel/Replace Request (G) |
| 151 | LeavesQty | Y | Unfilled quantity on the order. When order is closed (filled, done for day, canceled, replaced, rejected, expired) value could be 0 |
| 152 | CashOrderQty | N | Either CashOrderQty (152) or OrderQty (38) is provided. Specifies the notional amount conveyed on the order |
| 378 | ExecRestatementReason | N | Populated when ExecType (150) = Restated (D).  100 - Stop triggered, for stop and stop limit orders |

**Example FIX Messages**

Pending NewNewPartial FillFillPending ReplaceReplacedPending CancelCanceledRejected

```
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=A|40=1|49=ALPACA|52=20230615-18:14:29.702|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:14:29.702|150=A|151=10|10=088|
```

```
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=0|40=1|49=ALPACA|52=20230615-18:14:45.263|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:14:45.263|150=0|151=10|10=054|
```

```
|8=FIX.4.2|9=251|1=TEST_ACCOUNT|6=350.78|14=5|15=USD|17=694bc450-3ca6-461e-8566-f977dcec9e2d|31=350.78|32=5|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=1|40=1|49=ALPACA|52=20230615-18:15:00.622|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:00.622|150=1|151=5|10=185|
```

```
|8=FIX.4.2|9=253|1=TEST_ACCOUNT|6=350.78|14=10|15=USD|17=694bc450-3ca6-461e-8566-f977dcec9e2d|31=350.78|32=10|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=2|40=1|49=ALPACA|52=20230615-18:15:21.920|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:21.920|150=2|151=0|10=024|
```

```
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=E|40=1|49=ALPACA|52=20230615-18:26:53.971|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:26:53.971|150=E|151=10|10=112|
```

```
|8=FIX.4.2|9=256|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=5|40=1|41=56fcd203-7a97-430d-b14c-b0d9a7f59f2f|49=ALPACA|52=20230615-18:15:38.108|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:38.108|150=5|151=10|10=144|
```

```
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=6|40=1|49=ALPACA|52=20230615-18:24:50.191|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:24:50.191|150=6|151=10|10=060|
```

```
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=4|40=1|49=ALPACA|52=20230615-18:17:45.813|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:17:45.813|150=4|151=10|10=070|
```

```
|8=FIX.4.2|9=227|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=8|40=1|49=ALPACA|52=20230615-18:15:51.825|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:51.825|103=Price too low|150=8|10=191|
```

## Order Cancel Request (F)

Sent by the client to request cancellation of an order.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | F - For Order Cancel Request |
| 1 | Account | Y | Account number |
| 11 | ClOrdID | Y | Unique identifier of cancel request assigned by the client |
| 41 | OrigClOrdID | Y | ClOrdID (11) of the order to be canceled as assigned by the client |
| 54 | Side | Y | As specified on the order to be canceled |
| 55 | Symbol | Y | As specified on the order to be canceled |
| 60 | TransactTime | Y | UTC timestamp when cancel request was initiated |

To acknowledge this message, an Execution Report (8) with `150=6` is sent immediately followed by an Execution Report (8) with `150=4` or an Order Cancel Reject (9) message. Sometimes an Order Cancel Reject (9) message might be sent directly without sending an Execution Report (8) with `150=6`.

**Example FIX Messages**

Cancel Request

```
|8=FIX.4.2|9=190|35=F|34=5|49=SENDER|52=20240524-16:02:44.709|56=ALPACA|1=account1|11=b165965d-0c9d-467e-a174-ee30f3fe6dbe|41=b5db0b8e-bbc1-4906-aff8-c58d18ba3398|54=1|55=AAPL|60=20240524-16:02:44.709206406|10=226|
```

## Order Cancel/Replace Request (G)

Sent by the client to request modification of an order.

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | G - For Order Cancel/Replace Request |
| 1 | Account | Y | Account number |
| 11 | ClOrdID | Y | Unique identifier of the replacement order assigned by the client (must be no longer than 48 characters) |
| 21 | HandlInst | Y | 1 - Automated execution with no broker intervention, only accepted value |
| 38 | OrderQty | N | Modified quantity for the order |
| 40 | OrdType | Y | As specified on the original order |
| 41 | OrigClOrdID | Y | ClOrdID (11) of the order to be modified as assigned by the client |
| 44 | Price | N | Modified price for the order |
| 54 | Side | Y | As specified on the original order |
| 55 | Symbol | Y | As specified on the original order |
| 59 | TimeInForce | N | Modified time in force for the order |
| 60 | TransactTime | Y | UTC timestamp when cancel/replace request was initiated |
| 99 | StopPx | N | Modified stop price for the order |

**Example FIX Messages**

Cancel/Replace Request

```
|8=FIX.4.2|9=212|35=G|34=21|49=SENDER|52=20240524-16:16:58.956|56=ALPACA|1=account1|11=45169819-088a-4089-9758-f28e830e95f0|21=3|40=2|41=f001f209-2c3e-42e3-9ab1-10e74ee39fe5|44=1.50000|54=1|55=AAPL|60=20240524-16:16:58.956849295|10=173|
```

## Order Cancel Reject (9)

Sent by the server if the Order Cancel Request (F) or Order Cancel/Replace Request (G) message could not be honored. Some common reject scenarios include:

* when order is already filled or closed
* when a previous Order Cancel Request (F) or Order Cancel/Replace Request (G) is pending for this order

| Tag | Field | Mandatory | Description |
| --- | --- | --- | --- |
| 35 | MsgType | Y | 9 - For Order Cancel Reject |
| 1 | Account | Y | Account number |
| 11 | ClOrdID | Y | Unique identifier of cancel or cancel/replace request as assigned by the client |
| 37 | OrderID | Y | Unique identifier of the order as assigned by Alpaca for which the cancel or cancel/replace request was rejected |
| 39 | OrdStatus | Y | Order status after this cancel reject is applied |
| 41 | OrigClOrdID | Y | ClOrdID (11) of the order for which the cancel or cancel/replace request was rejected |
| 58 | Text | N | Reject reason |
| 60 | TransactTime | N | Server time in UTC when cancel or replace reject occurred |
| 102 | CxlRejReason | N | Code to identify reason for cancel rejection.  0 - Too late to cancel  1 - Unknown order  2 - Broker Option  3 - Order already in Pending Cancel or Pending Replace status |
| 434 | CxlRejResponseTo | Y | 1 - Response to Order Cancel Request (F)  2 - Response to Order Cancel/Replace Request (G) |

**Example FIX Messages**

Cancel RejectCancel/Replace Reject

```
|8=FIX.4.2|9=220|35=9|34=18|49=ALPACA|52=20240524-16:02:46.215|56=SENDER|1=account1|11=a7860828-4dc5-4f8f-bfb1-8fbca8855c88|37=f50af678-bba4-44ea-9b23-0fc452ed4921|39=6|41=2c017b79-a843-4146-a2b7-3bf83af89482|58=TOO_LATE_TO_CANCEL|434=1|10=116|
```

```
|8=FIX.4.2|9=198|35=9|34=45|49=ALPACA|52=20240524-16:16:59.085|56=SENDER|1=account1|11=5cdf9082-067b-4497-a90c-f5e8c666409b|37=UNKNOWN|39=8|41=c7feaf5a-54d2-458d-8ab2-9b2f337a28ec|58=replace pending for order|434=2|10=179|
```

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 08/05/2024 | Document Creation |
| 0.1.1 | 24/05/2024 | Changed FIX version to FIX.4.2  Removed ApplVerID (1128) from Message Header  Added ClOrdID (11) and OrigClOrdID (41) as required in Order Cancel Request (F) and Order Cancel/Replace Request (G)  Removed OrderID (37) from Order Cancel Request (F) and Order Cancel/Replace Request (G)  Added OrderQty (38) to Order Cancel/Replace Request (G)  Updated FIX examples |
| 0.1.2 | 12/06/2024 | Removed Account (1) and RawData (96) from Logon (A) message  Added RefTagID (371), RefMsgType (372) and SessionRejectReason (373) to Reject (3) message  Added HandlInst (21), TransactTime (60) and OpenClose (77) to New Order - Single (D)  Added 1 (per share) as an accepted value for CommType (13) in New Order - Single (D)  Updated AvgPx (6) to mandatory in Execution Report (8)  Added Commission (12), ExecRefID (19), ExecTransType (20), LastMkt (30), OrderQty (38) and CashOrderQty (152) to Execution Report (8)  Removed OrdRejReason (103) from Execution Report (8)  Updated possible values for ExecType (150) in Execution Report (8) |
| 1.0.0 | 13/06/2024 | Added Side (54), Symbol (55) and TransactTime (60) to Order Cancel Request (F)  Added OrderID (37) to Order Cancel Reject (9)  Added HandlInst (21), OrdType (40), Side (54), Symbol (55) and TransactTime (60) to Order Cancel/Replace Request (G) |
| 1.0.1 | 04/09/2024 | Added Market on close (5) and Limit on close (B) as values for OrdType (40) on New Order - Single (D)  Added At the Close (7) as a value for TimeInForce (59) on New Order - Single (D) |
| 1.0.2 | 08/10/2024 | Added Restated (D) as value for ExecType (150) on Execution Report (8)  Added ExecRestatementReason (378) to Execution Report (8)  Added Status (3) as value for ExecTransType (20) on Execution Report (8)  Added TransactTime (60) to Order Cancel Reject (9) |
| 1.0.3 | 14/01/2025 | Added Good Till Crossing (5) as a value for TimeInForce (59) on New Order - Single (D)  Added ClientID (109) to New Order - Single (D) |
| 1.0.4 | 03/04/2025 | Removed Good Till Crossing (5) as a valid value for TimeInForce (59) on New Order - Single (D)  Added TradingSessionID (336) to New Order - Single (D) |

Updated 5 months ago

---

Ask AI