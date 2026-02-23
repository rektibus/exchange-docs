# Bitso API Documentation

Auto-fetched from 3 page(s)


---

# Source: https://docs.bitso.com/docs/welcome-api

[Jump to Content](#content)

[](https://bitso.com/)[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)

[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

v1.0

* * *

[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)[Log In](/login?redirect_uri=/docs/api-overview)[](https://bitso.com/)

 __Guides

Search

``

[Log In](/login?redirect_uri=/bitso-api/docs/api-overview)

v1.0[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

Trading API: Overview

All

Pages

###### Start typing to search…

## TRADING

  * [Trading API: Overview](/bitso-api/docs/api-overview)
  * [Contact Us](/bitso-api/docs/contact-us)



## CHANGELOG

  * [History of Changes](/bitso-api/docs/history-of-changes)



## FIRST STEPS

  * [Set Up Your Testing Environment __](/bitso-api/docs/set-up-your-testing-environment)
    * [1\. Create Your Testing Account](/bitso-api/docs/1-create-your-testing-account)
    * [ 2\. Generate Your API Credentials](/bitso-api/docs/2-generate-your-api-credentials)
    * [3\. Add Funds to Your Account](/bitso-api/docs/3-add-funds-to-your-account)
  * [Authentication __](/bitso-api/docs/authentication)
    * [Create Signed Requests](/bitso-api/docs/create-signed-requests)
    * [ Nonce v2 Rollout](/bitso-api/docs/nonce-v2-rollout)
    * [Understand Bitso's Auth Mechanism](/bitso-api/docs/understand-bitsos-auth-mechanism)
  * [General](/bitso-api/docs/general-concepts)
  * [Currency Dictionary](/bitso-api/docs/currency-dictionary)



## BOOKS & TRADES

  * [List Available Books](/bitso-api/docs/list-available-books)
  * [Get Ticker](/bitso-api/docs/ticker)
  * [List Order Book](/bitso-api/docs/list-order-book)
  * [List Trades](/bitso-api/docs/list-trades)



## ORDERS

  * [Place an Order](/bitso-api/docs/place-an-order)
  * [Replace an Order](/bitso-api/docs/replace-an-order)
  * [Modify an Order](/bitso-api/docs/modify-an-order)
  * [List User Trades](/bitso-api/docs/user-trades)
  * [List Order Trades](/bitso-api/docs/list-user-trades)
  * [List Open Orders](/bitso-api/docs/list-open-orders)
  * [Look Up Orders](/bitso-api/docs/look-up-orders)
  * [Cancel an Order](/bitso-api/docs/cancel-an-order)
  * [List Fees](/bitso-api/docs/list-fees)



## WEBSOCKET API

  * [General](/bitso-api/docs/general)
  * [Trades Channel](/bitso-api/docs/trades-channel)
  * [Diff-Orders Channel](/bitso-api/docs/diff-orders-channel)
  * [Orders Channel](/bitso-api/docs/orders-channel)



## CONVERSIONS

  * [Understanding Conversions __](/bitso-api/docs/understanding-conversions)
    * [Request a Conversion Quote](/bitso-api/docs/request-a-conversion-quote-1)
    * [ Execute a Conversion Quote](/bitso-api/docs/execute-a-conversion-quote)
    * [Get a Conversion Status](/bitso-api/docs/get-a-conversion-status)



## OTC

  * [RFQ __](/bitso-api/docs/list-pairs)
    * [List Pairs](/bitso-api/docs/list-pairs)
    * [ Request a Quote](/bitso-api/docs/request-a-quote)
    * [Retrieve a Quote](/bitso-api/docs/retrieve-a-quote)
    * [Convert a Quote](/bitso-api/docs/convert-a-quote)
    * [Get RFQ Conversion](/bitso-api/docs/get-rfq-conversion)
    * [List RFQ Conversions](/bitso-api/docs/get-rfq-conversion-history)



## MARGIN TRADING [WIP]

  * [Creating a Margin Account](/bitso-api/docs/create-margin-account)
  * [Funding your Margin Account](/bitso-api/docs/process-margin-funds-movement)
  * [Borrowing and Repayments](/bitso-api/docs/borrowing-and-repayments)
  * [Place a Margin Order](/bitso-api/docs/place-margin-order)



## ACCOUNTS

  * [Get Account Balance](/bitso-api/docs/get-account-balance)
  * [Get Account Status [WIP]](/bitso-api/docs/get-account-status)



## ERROR CODES

  * [Error Categories __](/bitso-api/docs/error-categories)
    * [01: Unknown Errors](/bitso-api/docs/unknown-error-01-http-500)
    * [ 02: Authentication Errors](/bitso-api/docs/authentication-error-02-http-401)
    * [03: Validation Errors - Part 1](/bitso-api/docs/validation-errors-03-http-400)
    * [04: System-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400)
    * [05: User-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400-1)
    * [06: Funds Errors](/bitso-api/docs/funds-errors-06-http-400)
    * [07: Account Errors](/bitso-api/docs/account-errors-07-http-400)
    * [08: Throttling Errors](/bitso-api/docs/throttling-errors-08-http-420)
    * [09: Unsupported-Method Errors](/bitso-api/docs/unsupported-http-method-errors-09-http-400)
    * [10: Miscellaneous Errors](/bitso-api/docs/10-miscellaneous-errors)
    * [11: Operation Errors](/bitso-api/docs/11-operation-errors)
    * [12: Phone-Related Errors](/bitso-api/docs/12-phone-related-errors)
    * [13: OTP Errors](/bitso-api/docs/12-otp-errors)
    * [14: Not-Found Errors](/bitso-api/docs/14-not-found-errors)
    * [16: SPEI Remittance Errors](/bitso-api/docs/16-spei-remittance-errors)
    * [17: Validation Errors - Part 2](/bitso-api/docs/17-validation-errors-part-2)



Powered by [](https://readme.com?ref_src=hub&project=bitso3)

# Trading API: Overview

Learn about the business value of the API and how it can help you enhance your business.

Welcome to Bitso's Trading API documentation, a RESTful API that exposes Bitso's Digital and Fiat Currency Trading platform. We are excited you are here! 💛

Bitso's Trading API enables you to integrate the Bitso trading platform with third-party solutions, such as trading applications, charting programs, point-of-sale systems, and many more. The API is easy to use, and integrating it into your solutions is a short-lived and trouble-free effort.

The Trading API provides a set of four public endpoints to retrieve information such as available exchange order books and data from a specified book: trading information, open orders, and recent trades.

The service also comprises a set of private endpoints that enable you to manage your orders and your Bitso account. All of the requests to these private endpoints must be signed and require API Keys. For further details on how to get your API Keys and create signed requests, see the sections, [Set Up Your Testing Environment](https://docs.bitso.com/bitso-api/docs/set-up-your-testing-environment) and [Authentication](https://docs.bitso.com/bitso-api/docs/authentication).

This guide documents all the details on how the service works, its onboarding requirements, and the error messages it might throw. You will be up and running in a jiffy! 🚀

 __Updated 5 months ago

* * *

[Contact Us](/bitso-api/docs/contact-us)

Ask AI


---

# Source: https://docs.bitso.com/reference/available-books

[Jump to Content](#content)

[](https://bitso.com/)[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)

[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

v1.0

* * *

[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)[Log In](/login?redirect_uri=/docs/api-overview)[](https://bitso.com/)

 __Guides

Search

``

[Log In](/login?redirect_uri=/bitso-api/docs/api-overview)

v1.0[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

Trading API: Overview

All

Pages

###### Start typing to search…

## TRADING

  * [Trading API: Overview](/bitso-api/docs/api-overview)
  * [Contact Us](/bitso-api/docs/contact-us)



## CHANGELOG

  * [History of Changes](/bitso-api/docs/history-of-changes)



## FIRST STEPS

  * [Set Up Your Testing Environment __](/bitso-api/docs/set-up-your-testing-environment)
    * [1\. Create Your Testing Account](/bitso-api/docs/1-create-your-testing-account)
    * [ 2\. Generate Your API Credentials](/bitso-api/docs/2-generate-your-api-credentials)
    * [3\. Add Funds to Your Account](/bitso-api/docs/3-add-funds-to-your-account)
  * [Authentication __](/bitso-api/docs/authentication)
    * [Create Signed Requests](/bitso-api/docs/create-signed-requests)
    * [ Nonce v2 Rollout](/bitso-api/docs/nonce-v2-rollout)
    * [Understand Bitso's Auth Mechanism](/bitso-api/docs/understand-bitsos-auth-mechanism)
  * [General](/bitso-api/docs/general-concepts)
  * [Currency Dictionary](/bitso-api/docs/currency-dictionary)



## BOOKS & TRADES

  * [List Available Books](/bitso-api/docs/list-available-books)
  * [Get Ticker](/bitso-api/docs/ticker)
  * [List Order Book](/bitso-api/docs/list-order-book)
  * [List Trades](/bitso-api/docs/list-trades)



## ORDERS

  * [Place an Order](/bitso-api/docs/place-an-order)
  * [Replace an Order](/bitso-api/docs/replace-an-order)
  * [Modify an Order](/bitso-api/docs/modify-an-order)
  * [List User Trades](/bitso-api/docs/user-trades)
  * [List Order Trades](/bitso-api/docs/list-user-trades)
  * [List Open Orders](/bitso-api/docs/list-open-orders)
  * [Look Up Orders](/bitso-api/docs/look-up-orders)
  * [Cancel an Order](/bitso-api/docs/cancel-an-order)
  * [List Fees](/bitso-api/docs/list-fees)



## WEBSOCKET API

  * [General](/bitso-api/docs/general)
  * [Trades Channel](/bitso-api/docs/trades-channel)
  * [Diff-Orders Channel](/bitso-api/docs/diff-orders-channel)
  * [Orders Channel](/bitso-api/docs/orders-channel)



## CONVERSIONS

  * [Understanding Conversions __](/bitso-api/docs/understanding-conversions)
    * [Request a Conversion Quote](/bitso-api/docs/request-a-conversion-quote-1)
    * [ Execute a Conversion Quote](/bitso-api/docs/execute-a-conversion-quote)
    * [Get a Conversion Status](/bitso-api/docs/get-a-conversion-status)



## OTC

  * [RFQ __](/bitso-api/docs/list-pairs)
    * [List Pairs](/bitso-api/docs/list-pairs)
    * [ Request a Quote](/bitso-api/docs/request-a-quote)
    * [Retrieve a Quote](/bitso-api/docs/retrieve-a-quote)
    * [Convert a Quote](/bitso-api/docs/convert-a-quote)
    * [Get RFQ Conversion](/bitso-api/docs/get-rfq-conversion)
    * [List RFQ Conversions](/bitso-api/docs/get-rfq-conversion-history)



## MARGIN TRADING [WIP]

  * [Creating a Margin Account](/bitso-api/docs/create-margin-account)
  * [Funding your Margin Account](/bitso-api/docs/process-margin-funds-movement)
  * [Borrowing and Repayments](/bitso-api/docs/borrowing-and-repayments)
  * [Place a Margin Order](/bitso-api/docs/place-margin-order)



## ACCOUNTS

  * [Get Account Balance](/bitso-api/docs/get-account-balance)
  * [Get Account Status [WIP]](/bitso-api/docs/get-account-status)



## ERROR CODES

  * [Error Categories __](/bitso-api/docs/error-categories)
    * [01: Unknown Errors](/bitso-api/docs/unknown-error-01-http-500)
    * [ 02: Authentication Errors](/bitso-api/docs/authentication-error-02-http-401)
    * [03: Validation Errors - Part 1](/bitso-api/docs/validation-errors-03-http-400)
    * [04: System-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400)
    * [05: User-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400-1)
    * [06: Funds Errors](/bitso-api/docs/funds-errors-06-http-400)
    * [07: Account Errors](/bitso-api/docs/account-errors-07-http-400)
    * [08: Throttling Errors](/bitso-api/docs/throttling-errors-08-http-420)
    * [09: Unsupported-Method Errors](/bitso-api/docs/unsupported-http-method-errors-09-http-400)
    * [10: Miscellaneous Errors](/bitso-api/docs/10-miscellaneous-errors)
    * [11: Operation Errors](/bitso-api/docs/11-operation-errors)
    * [12: Phone-Related Errors](/bitso-api/docs/12-phone-related-errors)
    * [13: OTP Errors](/bitso-api/docs/12-otp-errors)
    * [14: Not-Found Errors](/bitso-api/docs/14-not-found-errors)
    * [16: SPEI Remittance Errors](/bitso-api/docs/16-spei-remittance-errors)
    * [17: Validation Errors - Part 2](/bitso-api/docs/17-validation-errors-part-2)



Powered by [](https://readme.com?ref_src=hub&project=bitso3)

# Trading API: Overview

Learn about the business value of the API and how it can help you enhance your business.

Welcome to Bitso's Trading API documentation, a RESTful API that exposes Bitso's Digital and Fiat Currency Trading platform. We are excited you are here! 💛

Bitso's Trading API enables you to integrate the Bitso trading platform with third-party solutions, such as trading applications, charting programs, point-of-sale systems, and many more. The API is easy to use, and integrating it into your solutions is a short-lived and trouble-free effort.

The Trading API provides a set of four public endpoints to retrieve information such as available exchange order books and data from a specified book: trading information, open orders, and recent trades.

The service also comprises a set of private endpoints that enable you to manage your orders and your Bitso account. All of the requests to these private endpoints must be signed and require API Keys. For further details on how to get your API Keys and create signed requests, see the sections, [Set Up Your Testing Environment](https://docs.bitso.com/bitso-api/docs/set-up-your-testing-environment) and [Authentication](https://docs.bitso.com/bitso-api/docs/authentication).

This guide documents all the details on how the service works, its onboarding requirements, and the error messages it might throw. You will be up and running in a jiffy! 🚀

 __Updated 5 months ago

* * *

[Contact Us](/bitso-api/docs/contact-us)

Ask AI


---

# Source: https://docs.bitso.com/reference/ticker

[Jump to Content](#content)

[](https://bitso.com/)[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)

[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

v1.0

* * *

[Payouts and Pay-Ins](https://docs.bitso.com/bitso-payouts-funding/docs/getting-started)[Juno](https://docs.bitso.com/juno/docs/getting-started)[Log In](/login?redirect_uri=/docs/api-overview)[](https://bitso.com/)

 __Guides

Search

``

[Log In](/login?redirect_uri=/bitso-api/docs/api-overview)

v1.0[ __Guides](/bitso-api/docs)[ __Recipes](/bitso-api/recipes)[ __API Reference](/bitso-api/reference)[ __Changelog](/bitso-api/changelog)[ __Discussions](/bitso-api/discuss)

Trading API: Overview

All

Pages

###### Start typing to search…

## TRADING

  * [Trading API: Overview](/bitso-api/docs/api-overview)
  * [Contact Us](/bitso-api/docs/contact-us)



## CHANGELOG

  * [History of Changes](/bitso-api/docs/history-of-changes)



## FIRST STEPS

  * [Set Up Your Testing Environment __](/bitso-api/docs/set-up-your-testing-environment)
    * [1\. Create Your Testing Account](/bitso-api/docs/1-create-your-testing-account)
    * [ 2\. Generate Your API Credentials](/bitso-api/docs/2-generate-your-api-credentials)
    * [3\. Add Funds to Your Account](/bitso-api/docs/3-add-funds-to-your-account)
  * [Authentication __](/bitso-api/docs/authentication)
    * [Create Signed Requests](/bitso-api/docs/create-signed-requests)
    * [ Nonce v2 Rollout](/bitso-api/docs/nonce-v2-rollout)
    * [Understand Bitso's Auth Mechanism](/bitso-api/docs/understand-bitsos-auth-mechanism)
  * [General](/bitso-api/docs/general-concepts)
  * [Currency Dictionary](/bitso-api/docs/currency-dictionary)



## BOOKS & TRADES

  * [List Available Books](/bitso-api/docs/list-available-books)
  * [Get Ticker](/bitso-api/docs/ticker)
  * [List Order Book](/bitso-api/docs/list-order-book)
  * [List Trades](/bitso-api/docs/list-trades)



## ORDERS

  * [Place an Order](/bitso-api/docs/place-an-order)
  * [Replace an Order](/bitso-api/docs/replace-an-order)
  * [Modify an Order](/bitso-api/docs/modify-an-order)
  * [List User Trades](/bitso-api/docs/user-trades)
  * [List Order Trades](/bitso-api/docs/list-user-trades)
  * [List Open Orders](/bitso-api/docs/list-open-orders)
  * [Look Up Orders](/bitso-api/docs/look-up-orders)
  * [Cancel an Order](/bitso-api/docs/cancel-an-order)
  * [List Fees](/bitso-api/docs/list-fees)



## WEBSOCKET API

  * [General](/bitso-api/docs/general)
  * [Trades Channel](/bitso-api/docs/trades-channel)
  * [Diff-Orders Channel](/bitso-api/docs/diff-orders-channel)
  * [Orders Channel](/bitso-api/docs/orders-channel)



## CONVERSIONS

  * [Understanding Conversions __](/bitso-api/docs/understanding-conversions)
    * [Request a Conversion Quote](/bitso-api/docs/request-a-conversion-quote-1)
    * [ Execute a Conversion Quote](/bitso-api/docs/execute-a-conversion-quote)
    * [Get a Conversion Status](/bitso-api/docs/get-a-conversion-status)



## OTC

  * [RFQ __](/bitso-api/docs/list-pairs)
    * [List Pairs](/bitso-api/docs/list-pairs)
    * [ Request a Quote](/bitso-api/docs/request-a-quote)
    * [Retrieve a Quote](/bitso-api/docs/retrieve-a-quote)
    * [Convert a Quote](/bitso-api/docs/convert-a-quote)
    * [Get RFQ Conversion](/bitso-api/docs/get-rfq-conversion)
    * [List RFQ Conversions](/bitso-api/docs/get-rfq-conversion-history)



## MARGIN TRADING [WIP]

  * [Creating a Margin Account](/bitso-api/docs/create-margin-account)
  * [Funding your Margin Account](/bitso-api/docs/process-margin-funds-movement)
  * [Borrowing and Repayments](/bitso-api/docs/borrowing-and-repayments)
  * [Place a Margin Order](/bitso-api/docs/place-margin-order)



## ACCOUNTS

  * [Get Account Balance](/bitso-api/docs/get-account-balance)
  * [Get Account Status [WIP]](/bitso-api/docs/get-account-status)



## ERROR CODES

  * [Error Categories __](/bitso-api/docs/error-categories)
    * [01: Unknown Errors](/bitso-api/docs/unknown-error-01-http-500)
    * [ 02: Authentication Errors](/bitso-api/docs/authentication-error-02-http-401)
    * [03: Validation Errors - Part 1](/bitso-api/docs/validation-errors-03-http-400)
    * [04: System-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400)
    * [05: User-Limit Errors](/bitso-api/docs/system-limit-errors-04-http-400-1)
    * [06: Funds Errors](/bitso-api/docs/funds-errors-06-http-400)
    * [07: Account Errors](/bitso-api/docs/account-errors-07-http-400)
    * [08: Throttling Errors](/bitso-api/docs/throttling-errors-08-http-420)
    * [09: Unsupported-Method Errors](/bitso-api/docs/unsupported-http-method-errors-09-http-400)
    * [10: Miscellaneous Errors](/bitso-api/docs/10-miscellaneous-errors)
    * [11: Operation Errors](/bitso-api/docs/11-operation-errors)
    * [12: Phone-Related Errors](/bitso-api/docs/12-phone-related-errors)
    * [13: OTP Errors](/bitso-api/docs/12-otp-errors)
    * [14: Not-Found Errors](/bitso-api/docs/14-not-found-errors)
    * [16: SPEI Remittance Errors](/bitso-api/docs/16-spei-remittance-errors)
    * [17: Validation Errors - Part 2](/bitso-api/docs/17-validation-errors-part-2)



Powered by [](https://readme.com?ref_src=hub&project=bitso3)

# Trading API: Overview

Learn about the business value of the API and how it can help you enhance your business.

Welcome to Bitso's Trading API documentation, a RESTful API that exposes Bitso's Digital and Fiat Currency Trading platform. We are excited you are here! 💛

Bitso's Trading API enables you to integrate the Bitso trading platform with third-party solutions, such as trading applications, charting programs, point-of-sale systems, and many more. The API is easy to use, and integrating it into your solutions is a short-lived and trouble-free effort.

The Trading API provides a set of four public endpoints to retrieve information such as available exchange order books and data from a specified book: trading information, open orders, and recent trades.

The service also comprises a set of private endpoints that enable you to manage your orders and your Bitso account. All of the requests to these private endpoints must be signed and require API Keys. For further details on how to get your API Keys and create signed requests, see the sections, [Set Up Your Testing Environment](https://docs.bitso.com/bitso-api/docs/set-up-your-testing-environment) and [Authentication](https://docs.bitso.com/bitso-api/docs/authentication).

This guide documents all the details on how the service works, its onboarding requirements, and the error messages it might throw. You will be up and running in a jiffy! 🚀

 __Updated 5 months ago

* * *

[Contact Us](/bitso-api/docs/contact-us)

Ask AI
