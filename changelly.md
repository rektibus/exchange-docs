# Changelly API Documentation

Auto-fetched from 3 page(s)


---

# Source: https://docs.changelly.com/api/pro-api/market-data-endpoints

[Skip to main content](#__docusaurus_skipToContent_fallback)

[**Changelly Exchange API**](/)

  * [Introduction](/)
  * [Usage](/category/usage)

  * [Development](/category/development)

  * [Currencies](/currencies)

  * [Limits](/limits)

  * [Floating rate transactions](/category/floating-rate-transactions)

  * [Fixed rate transactions](/category/fixed-rate-transactions)

  * [Transaction info](/category/transaction-info)

  * [Address validation](/validate-address)
  * [Migration from Exchange API v1](/migration-guide)



  * [](/)
  * Introduction



On this page

# Introduction

The following methods are used to empower your service with Changelly exchange features. You can request more features by contacting our development team. Changelly API is a white-label exchange solution.

Changelly API v2 is a faster, safer and more flexible version of our API.

info

Rates and limits received using the API v2 estimation methods are compatible only with API v2 and can be used only to create a transaction using API v2 methods (`createTransaction`, `createFixTransaction`). You can't use the rate received by one version of API to create a transaction with another version.

## Getting Started[â](#getting-started "Direct link to Getting Started")

  1. Read the following documentation;
  2. [Generate the private and public keys pair](/development/generate-keys);
  3. Keep your private key in a safe place and _don 't share it with anyone, not even us_;
  4. Register on [the Changelly website](https://changelly.com/) if you don't have an account yet.
  5. Contact us at [[email protected]](/cdn-cgi/l/email-protection#a0d0d2cfe0c3c8c1cec7c5ccccd98ec3cfcd) to register your:


  * E-mail address connected to your account;
  * Public API key;
  * Public API key Base64;


  6. If you have any questions, please write us at [[email protected]](/cdn-cgi/l/email-protection#ef9f9d80af8c878e81888a838396c18c8082).



info

  * For the currencies with multiple outputs in a transaction (BTC, LTC, etc), we do not accept more than one output per address in one transaction.
  * The integration with our API should be implemented on the backend side:
  * If you try to integrate with our API on the frontend side, then your API key will be accessible to all users.
  * It is not necessary to use Node.js for your backend, any other server language is suitable.



## Your API Extra Fee[â](#your-api-extra-fee "Direct link to Your API Extra Fee")

After setting up an API key, you may want to set up your API extra fee.

For example, you may choose to charge a 0.5% fee on top of Changelly exchange fee.

To set up an extra commission, [please email us](/cdn-cgi/l/email-protection#6b1b19042b08030a050c0e07071245080406) with a link to your service.

Your API extra commission in percent is included in a result of [getTransactions](/info/get-transactions) function call.

[NextUsage](/category/usage)

  * [Getting Started](#getting-started)
  * [Your API Extra Fee](#your-api-extra-fee)




---

# Source: https://docs.changelly.com/api/pro-api/account-endpoints

[Skip to main content](#__docusaurus_skipToContent_fallback)

[**Changelly Exchange API**](/)

  * [Introduction](/)
  * [Usage](/category/usage)

  * [Development](/category/development)

  * [Currencies](/currencies)

  * [Limits](/limits)

  * [Floating rate transactions](/category/floating-rate-transactions)

  * [Fixed rate transactions](/category/fixed-rate-transactions)

  * [Transaction info](/category/transaction-info)

  * [Address validation](/validate-address)
  * [Migration from Exchange API v1](/migration-guide)



  * [](/)
  * Introduction



On this page

# Introduction

The following methods are used to empower your service with Changelly exchange features. You can request more features by contacting our development team. Changelly API is a white-label exchange solution.

Changelly API v2 is a faster, safer and more flexible version of our API.

info

Rates and limits received using the API v2 estimation methods are compatible only with API v2 and can be used only to create a transaction using API v2 methods (`createTransaction`, `createFixTransaction`). You can't use the rate received by one version of API to create a transaction with another version.

## Getting Started[â](#getting-started "Direct link to Getting Started")

  1. Read the following documentation;
  2. [Generate the private and public keys pair](/development/generate-keys);
  3. Keep your private key in a safe place and _don 't share it with anyone, not even us_;
  4. Register on [the Changelly website](https://changelly.com/) if you don't have an account yet.
  5. Contact us at [[email protected]](/cdn-cgi/l/email-protection#cfbfbda08faca7aea1a8aaa3a3b6e1aca0a2) to register your:


  * E-mail address connected to your account;
  * Public API key;
  * Public API key Base64;


  6. If you have any questions, please write us at [[email protected]](/cdn-cgi/l/email-protection#1363617c53707b727d74767f7f6a3d707c7e).



info

  * For the currencies with multiple outputs in a transaction (BTC, LTC, etc), we do not accept more than one output per address in one transaction.
  * The integration with our API should be implemented on the backend side:
  * If you try to integrate with our API on the frontend side, then your API key will be accessible to all users.
  * It is not necessary to use Node.js for your backend, any other server language is suitable.



## Your API Extra Fee[â](#your-api-extra-fee "Direct link to Your API Extra Fee")

After setting up an API key, you may want to set up your API extra fee.

For example, you may choose to charge a 0.5% fee on top of Changelly exchange fee.

To set up an extra commission, [please email us](/cdn-cgi/l/email-protection#59292b36193a3138373e3c353520773a3634) with a link to your service.

Your API extra commission in percent is included in a result of [getTransactions](/info/get-transactions) function call.

[NextUsage](/category/usage)

  * [Getting Started](#getting-started)
  * [Your API Extra Fee](#your-api-extra-fee)




---

# Source: https://docs.changelly.com/api/pro-api/order-endpoints

[Skip to main content](#__docusaurus_skipToContent_fallback)

[**Changelly Exchange API**](/)

  * [Introduction](/)
  * [Usage](/category/usage)

  * [Development](/category/development)

  * [Currencies](/currencies)

  * [Limits](/limits)

  * [Floating rate transactions](/category/floating-rate-transactions)

  * [Fixed rate transactions](/category/fixed-rate-transactions)

  * [Transaction info](/category/transaction-info)

  * [Address validation](/validate-address)
  * [Migration from Exchange API v1](/migration-guide)



  * [](/)
  * Introduction



On this page

# Introduction

The following methods are used to empower your service with Changelly exchange features. You can request more features by contacting our development team. Changelly API is a white-label exchange solution.

Changelly API v2 is a faster, safer and more flexible version of our API.

info

Rates and limits received using the API v2 estimation methods are compatible only with API v2 and can be used only to create a transaction using API v2 methods (`createTransaction`, `createFixTransaction`). You can't use the rate received by one version of API to create a transaction with another version.

## Getting Started[â](#getting-started "Direct link to Getting Started")

  1. Read the following documentation;
  2. [Generate the private and public keys pair](/development/generate-keys);
  3. Keep your private key in a safe place and _don 't share it with anyone, not even us_;
  4. Register on [the Changelly website](https://changelly.com/) if you don't have an account yet.
  5. Contact us at [[email protected]](/cdn-cgi/l/email-protection#4737352807242f262920222b2b3e6924282a) to register your:


  * E-mail address connected to your account;
  * Public API key;
  * Public API key Base64;


  6. If you have any questions, please write us at [[email protected]](/cdn-cgi/l/email-protection#fa8a8895ba99929b949d9f969683d4999597).



info

  * For the currencies with multiple outputs in a transaction (BTC, LTC, etc), we do not accept more than one output per address in one transaction.
  * The integration with our API should be implemented on the backend side:
  * If you try to integrate with our API on the frontend side, then your API key will be accessible to all users.
  * It is not necessary to use Node.js for your backend, any other server language is suitable.



## Your API Extra Fee[â](#your-api-extra-fee "Direct link to Your API Extra Fee")

After setting up an API key, you may want to set up your API extra fee.

For example, you may choose to charge a 0.5% fee on top of Changelly exchange fee.

To set up an extra commission, [please email us](/cdn-cgi/l/email-protection#1c6c6e735c7f747d727b79707065327f7371) with a link to your service.

Your API extra commission in percent is included in a result of [getTransactions](/info/get-transactions) function call.

[NextUsage](/category/usage)

  * [Getting Started](#getting-started)
  * [Your API Extra Fee](#your-api-extra-fee)


