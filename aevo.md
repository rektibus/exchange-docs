# Aevo API Documentation

Auto-fetched from 4 page(s)


---

# Source: https://api-docs.aevo.xyz/reference/overview

[Jump to Content](#content)

[](/reference)

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog) v1.0.2v1.0.3-beta

* * *

[Log In](/login?redirect_uri=/reference/overview)[](/reference)

 __API Reference

[Log In](/login?redirect_uri=/reference/overview)

v1.0.3-beta

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog)

Introduction

All

Pages

###### Start typing to search…

JUMP TO

## Aevo API

  * [Introduction](/reference/overview)
  * [API Key Setup __](/reference/api-key-setup-via-ui)
    * [Via UI](/reference/api-key-setup-via-ui)
    * [ Via API](/reference/api-key-setup-api)
  * [Signing Orders](/reference/signing-orders)
  * [Signing Orders Without Timestamp](/reference/signing-orders-copy)
  * [Rate Limits](/reference/rate-limits-1)
  * [Orderbook Checksum](/reference/orderbook-checksum)
  * [Errors](/reference/errors)



## Aevo REST API

  * [Endpoints](/reference/urls)
  * [Public API __](/reference/getassets)
    * [GET /assets get](/reference/getassets)
    * [GET /expiriesget](/reference/getexpiries)
    * [GET /indexget](/reference/getindex)
    * [GET /index-historyget](/reference/getindexhistory)
    * [GET /mark-historyget](/reference/getmarkhistory)
    * [GET /settlement-historyget](/reference/getsettlementhistory)
    * [GET /marketsget](/reference/getmarkets)
    * [GET /statisticsget](/reference/getstatistics)
    * [GET /coingecko-statisticsget](/reference/getcoingeckostatistics)
    * [GET /orderbookget](/reference/getorderbook)
    * [GET /fundingget](/reference/getfunding)
    * [GET /funding-historyget](/reference/getfundinghistory)
    * [GET /instrument/{instrument_name}get](/reference/getinstrumentinstrumentname)
    * [GET /instrument/{instrument_name}/trade-historyget](/reference/getinstrumentinstrumentnametradehistory)
    * [GET /check-referralget](/reference/getcheckreferral)
    * [GET /emissionsget](/reference/getemissions)
    * [POST /account/unsubscribepost](/reference/postaccountunsubscribe)
    * [GET /timeget](/reference/gettime)
    * [GET /strategiesget](/reference/getstrategies)
    * [GET /yield-vaultget](/reference/getyieldvault)
    * [POST /swap/previewpost](/reference/postswappreview)
    * [GET /airdrop-incentivized-assetsget](/reference/getairdropincentivizedassets)
    * [GET /weethget](/reference/getweeth)
    * [GET /options-historyget](/reference/getoptionshistory)
    * [POST /account/email-verifiedpost](/reference/postaccountemailverified)
    * [GET /strategy/{strategy_address}/positionsget](/reference/getstrategystrategyaddresspositions)
    * [GET /strategy/{strategy_address}/trade-historyget](/reference/getstrategystrategyaddresstradehistory)
    * [GET /strategy/{strategy_address}/portfolioget](/reference/getstrategystrategyaddressportfolio)
    * [GET /strategy/{strategy_address}/balance-historyget](/reference/getstrategystrategyaddressbalancehistory)
    * [GET /strategy/{strategy_address}/transaction-historyget](/reference/getstrategystrategyaddresstransactionhistory)
    * [GET /strategy/{strategy_address}/pnl-historyget](/reference/getstrategystrategyaddresspnlhistory)
  * [Private API __](/reference/rest-authentication)
    * [Authentication](/reference/rest-authentication)
    * [ POST /registerpost](/reference/postregister)
    * [DELETE /api-keydel](/reference/deleteapikey)
    * [GET /api-keyget](/reference/getapikey)
    * [POST /api-keypost](/reference/postapikey)
    * [DELETE /signing-keydel](/reference/deletesigningkey)
    * [GET /authget](/reference/getauth)
    * [GET /accountget](/reference/getaccount)
    * [GET /positionsget](/reference/getpositions)
    * [GET /account/cancel-on-disconnectget](/reference/getaccountcancelondisconnect)
    * [POST /account/cancel-on-disconnectpost](/reference/postaccountcancelondisconnect)
    * [POST /account/portfolio-marginpost](/reference/postaccountportfoliomargin)
    * [GET /account/email-addressget](/reference/getaccountemailaddress)
    * [POST /account/email-addresspost](/reference/postaccountemailaddress)
    * [POST /account/email-preferencepost](/reference/postaccountemailpreference)
    * [GET /account/email-preferencesget](/reference/getaccountemailpreferences)
    * [GET /account/email-verifiedget](/reference/getaccountemailverified)
    * [GET /account/accumulated-fundingsget](/reference/getaccountaccumulatedfundings)
    * [POST /account/update-marginpost](/reference/postaccountupdatemargin)
    * [POST /account/margin-typepost](/reference/postaccountmargintype)
    * [POST /account/leveragepost](/reference/postaccountleverage)
    * [GET /account/trades/csvget](/reference/getaccounttradescsv)
    * [GET /account/transactions/csvget](/reference/getaccounttransactionscsv)
    * [GET /account/statsget](/reference/getaccountstats)
    * [POST /account/network-addresspost](/reference/postaccountnetworkaddress)
    * [GET /portfolioget](/reference/getportfolio)
    * [POST /withdrawpost](/reference/postwithdraw)
    * [GET /strategies/accountget](/reference/getstrategiesaccount)
    * [GET /strategies/account-historyget](/reference/getstrategiesaccounthistory)
    * [POST /strategy/{strategy_address}/initiate-withdrawpost](/reference/poststrategystrategyaddressinitiatewithdraw)
    * [POST /transferpost](/reference/posttransfer)
    * [GET /ordersget](/reference/getorders)
    * [POST /orderspost](/reference/postorders)
    * [DELETE /orders/{order_id}del](/reference/deleteordersorderid)
    * [GET /orders/{order_id}get](/reference/getordersorderid)
    * [POST /orders/{order_id}post](/reference/postordersorderid)
    * [DELETE /orders-alldel](/reference/deleteordersall)
    * [GET /order-historyget](/reference/getorderhistory)
    * [GET /order-history/stopsget](/reference/getorderhistorystops)
    * [GET /trade-historyget](/reference/gettradehistory)
    * [GET /transaction-historyget](/reference/gettransactionhistory)
    * [GET /referral-rewards-historyget](/reference/getreferralrewardshistory)
    * [GET /referral-historyget](/reference/getreferralhistory)
    * [GET /referral-statisticsget](/reference/getreferralstatistics)
    * [POST /claim-referral-rewardspost](/reference/postclaimreferralrewards)
    * [POST /claim-trade-feespost](/reference/postclaimtradefees)
    * [GET /trade-fees-campaign-statsget](/reference/gettradefeescampaignstats)
    * [GET /mmpget](/reference/getmmp)
    * [POST /mmppost](/reference/postmmp)
    * [POST /reset-mmppost](/reference/postresetmmp)
    * [DELETE /rfqsdel](/reference/deleterfqs)
    * [GET /rfqsget](/reference/getrfqs)
    * [POST /rfqspost](/reference/postrfqs)
    * [DELETE /rfqs/{block_id}del](/reference/deleterfqsblockid)
    * [GET /rfqs/{block_id}/quotesget](/reference/getrfqsblockidquotes)
    * [DELETE /quotesdel](/reference/deletequotes)
    * [GET /quotesget](/reference/getquotes)
    * [POST /quotespost](/reference/postquotes)
    * [POST /quotes/previewpost](/reference/postquotespreview)
    * [DELETE /quotes/{quote_id}del](/reference/deletequotesquoteid)
    * [PUT /quotes/{quote_id}put](/reference/putquotesquoteid)
    * [POST /swappost](/reference/postswap)
    * [GET /farm-boostget](/reference/getfarmboost)
    * [POST /farm-boostpost](/reference/postfarmboost)
    * [GET /proof-dataget](/reference/getproofdata)
    * [GET /proofs-dataget](/reference/getproofsdata)
    * [GET /leaderboard/campaignget](/reference/getleaderboardcampaign)
    * [POST /campaign-sign-uppost](/reference/postcampaignsignup)
    * [GET /otc/accountget](/reference/getotcaccount)
    * [POST /otc/create-requestpost](/reference/postotccreaterequest)
    * [POST /otc/unwindpost](/reference/postotcunwind)
    * [POST /account/usernamepost](/reference/postaccountusername)
    * [GET /twap-ordersget](/reference/gettwaporders)
    * [POST /twap-orderspost](/reference/posttwaporders)
    * [DELETE /twap-orders/{order_id}del](/reference/deletetwapordersorderid)
    * [GET /twap-orders/{order_id}get](/reference/gettwapordersorderid)
    * [GET /twap-order-historyget](/reference/gettwaporderhistory)
    * [GET /account/weekly-volumeget](/reference/getaccountweeklyvolume)
    * [GET /stakeget](/reference/getstake)
    * [POST /batch-orderspost](/reference/postbatchorders)



## Websocket API

  * [Endpoints](/reference/endpoints)
  * [Operations](/reference/operations)
  * [Message Format](/reference/messaging-format-1)
  * [Managing Connection](/reference/overview-1)
  * [Cancel on Disconnect](/reference/cancel-on-disconnect)
  * [Public Operations __](/reference/publish-channel)
    * [PUBLISH Channels](/reference/publish-channel)
    * [ PUBLISH Ping](/reference/publish-ping)
    * [SUBSCRIBE Orderbook Throttled (NEW)](/reference/subscribe-orderbook-throttled)
    * [SUBSCRIBE Book Ticker (NEW)](/reference/subcribe-book-ticker)
    * [SUBSCRIBE Ticker Throttled (NEW)](/reference/subscribe-ticker-throttled)
    * [SUBSCRIBE Index](/reference/subcribe-index)
    * [SUBSCRIBE Trades](/reference/subcribe-trades)
  * [Private Operations __](/reference/websocket-authentication)
    * [Authentication](/reference/websocket-authentication)
    * [ PUBLISH Status](/reference/get-status)
    * [PUBLISH Create Order](/reference/publish-create-order)
    * [PUBLISH Edit Order](/reference/publish-edit-order)
    * [PUBLISH Cancel Order](/reference/publish-cancel-order)
    * [PUBLISH Cancel All Orders](/reference/publish-cancel-all-orders)
    * [SUBCRIBE Orders](/reference/subcribe-orders)
    * [SUBCRIBE Fills](/reference/subcribe-fills)
    * [SUBCRIBE Positions](/reference/subcribe-positions)



Powered by [](https://readme.com?ref_src=hub&project=aevo)

# Introduction

Ask AI


---

# Source: https://api-docs.aevo.xyz/reference/getmarkets

[Jump to Content](#content)

[](/reference)

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog) v1.0.2v1.0.3-beta

* * *

[Log In](/login?redirect_uri=/reference/getmarkets)[](/reference)

 __API Reference

[Log In](/login?redirect_uri=/reference/getmarkets)

v1.0.3-beta

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog)

GET /markets

All

Pages

###### Start typing to search…

JUMP TO

## Aevo API

  * [Introduction](/reference/overview)
  * [API Key Setup __](/reference/api-key-setup-via-ui)
    * [Via UI](/reference/api-key-setup-via-ui)
    * [ Via API](/reference/api-key-setup-api)
  * [Signing Orders](/reference/signing-orders)
  * [Signing Orders Without Timestamp](/reference/signing-orders-copy)
  * [Rate Limits](/reference/rate-limits-1)
  * [Orderbook Checksum](/reference/orderbook-checksum)
  * [Errors](/reference/errors)



## Aevo REST API

  * [Endpoints](/reference/urls)
  * [Public API __](/reference/getassets)
    * [GET /assets get](/reference/getassets)
    * [GET /expiriesget](/reference/getexpiries)
    * [GET /indexget](/reference/getindex)
    * [GET /index-historyget](/reference/getindexhistory)
    * [GET /mark-historyget](/reference/getmarkhistory)
    * [GET /settlement-historyget](/reference/getsettlementhistory)
    * [GET /marketsget](/reference/getmarkets)
    * [GET /statisticsget](/reference/getstatistics)
    * [GET /coingecko-statisticsget](/reference/getcoingeckostatistics)
    * [GET /orderbookget](/reference/getorderbook)
    * [GET /fundingget](/reference/getfunding)
    * [GET /funding-historyget](/reference/getfundinghistory)
    * [GET /instrument/{instrument_name}get](/reference/getinstrumentinstrumentname)
    * [GET /instrument/{instrument_name}/trade-historyget](/reference/getinstrumentinstrumentnametradehistory)
    * [GET /check-referralget](/reference/getcheckreferral)
    * [GET /emissionsget](/reference/getemissions)
    * [POST /account/unsubscribepost](/reference/postaccountunsubscribe)
    * [GET /timeget](/reference/gettime)
    * [GET /strategiesget](/reference/getstrategies)
    * [GET /yield-vaultget](/reference/getyieldvault)
    * [POST /swap/previewpost](/reference/postswappreview)
    * [GET /airdrop-incentivized-assetsget](/reference/getairdropincentivizedassets)
    * [GET /weethget](/reference/getweeth)
    * [GET /options-historyget](/reference/getoptionshistory)
    * [POST /account/email-verifiedpost](/reference/postaccountemailverified)
    * [GET /strategy/{strategy_address}/positionsget](/reference/getstrategystrategyaddresspositions)
    * [GET /strategy/{strategy_address}/trade-historyget](/reference/getstrategystrategyaddresstradehistory)
    * [GET /strategy/{strategy_address}/portfolioget](/reference/getstrategystrategyaddressportfolio)
    * [GET /strategy/{strategy_address}/balance-historyget](/reference/getstrategystrategyaddressbalancehistory)
    * [GET /strategy/{strategy_address}/transaction-historyget](/reference/getstrategystrategyaddresstransactionhistory)
    * [GET /strategy/{strategy_address}/pnl-historyget](/reference/getstrategystrategyaddresspnlhistory)
  * [Private API __](/reference/rest-authentication)
    * [Authentication](/reference/rest-authentication)
    * [ POST /registerpost](/reference/postregister)
    * [DELETE /api-keydel](/reference/deleteapikey)
    * [GET /api-keyget](/reference/getapikey)
    * [POST /api-keypost](/reference/postapikey)
    * [DELETE /signing-keydel](/reference/deletesigningkey)
    * [GET /authget](/reference/getauth)
    * [GET /accountget](/reference/getaccount)
    * [GET /positionsget](/reference/getpositions)
    * [GET /account/cancel-on-disconnectget](/reference/getaccountcancelondisconnect)
    * [POST /account/cancel-on-disconnectpost](/reference/postaccountcancelondisconnect)
    * [POST /account/portfolio-marginpost](/reference/postaccountportfoliomargin)
    * [GET /account/email-addressget](/reference/getaccountemailaddress)
    * [POST /account/email-addresspost](/reference/postaccountemailaddress)
    * [POST /account/email-preferencepost](/reference/postaccountemailpreference)
    * [GET /account/email-preferencesget](/reference/getaccountemailpreferences)
    * [GET /account/email-verifiedget](/reference/getaccountemailverified)
    * [GET /account/accumulated-fundingsget](/reference/getaccountaccumulatedfundings)
    * [POST /account/update-marginpost](/reference/postaccountupdatemargin)
    * [POST /account/margin-typepost](/reference/postaccountmargintype)
    * [POST /account/leveragepost](/reference/postaccountleverage)
    * [GET /account/trades/csvget](/reference/getaccounttradescsv)
    * [GET /account/transactions/csvget](/reference/getaccounttransactionscsv)
    * [GET /account/statsget](/reference/getaccountstats)
    * [POST /account/network-addresspost](/reference/postaccountnetworkaddress)
    * [GET /portfolioget](/reference/getportfolio)
    * [POST /withdrawpost](/reference/postwithdraw)
    * [GET /strategies/accountget](/reference/getstrategiesaccount)
    * [GET /strategies/account-historyget](/reference/getstrategiesaccounthistory)
    * [POST /strategy/{strategy_address}/initiate-withdrawpost](/reference/poststrategystrategyaddressinitiatewithdraw)
    * [POST /transferpost](/reference/posttransfer)
    * [GET /ordersget](/reference/getorders)
    * [POST /orderspost](/reference/postorders)
    * [DELETE /orders/{order_id}del](/reference/deleteordersorderid)
    * [GET /orders/{order_id}get](/reference/getordersorderid)
    * [POST /orders/{order_id}post](/reference/postordersorderid)
    * [DELETE /orders-alldel](/reference/deleteordersall)
    * [GET /order-historyget](/reference/getorderhistory)
    * [GET /order-history/stopsget](/reference/getorderhistorystops)
    * [GET /trade-historyget](/reference/gettradehistory)
    * [GET /transaction-historyget](/reference/gettransactionhistory)
    * [GET /referral-rewards-historyget](/reference/getreferralrewardshistory)
    * [GET /referral-historyget](/reference/getreferralhistory)
    * [GET /referral-statisticsget](/reference/getreferralstatistics)
    * [POST /claim-referral-rewardspost](/reference/postclaimreferralrewards)
    * [POST /claim-trade-feespost](/reference/postclaimtradefees)
    * [GET /trade-fees-campaign-statsget](/reference/gettradefeescampaignstats)
    * [GET /mmpget](/reference/getmmp)
    * [POST /mmppost](/reference/postmmp)
    * [POST /reset-mmppost](/reference/postresetmmp)
    * [DELETE /rfqsdel](/reference/deleterfqs)
    * [GET /rfqsget](/reference/getrfqs)
    * [POST /rfqspost](/reference/postrfqs)
    * [DELETE /rfqs/{block_id}del](/reference/deleterfqsblockid)
    * [GET /rfqs/{block_id}/quotesget](/reference/getrfqsblockidquotes)
    * [DELETE /quotesdel](/reference/deletequotes)
    * [GET /quotesget](/reference/getquotes)
    * [POST /quotespost](/reference/postquotes)
    * [POST /quotes/previewpost](/reference/postquotespreview)
    * [DELETE /quotes/{quote_id}del](/reference/deletequotesquoteid)
    * [PUT /quotes/{quote_id}put](/reference/putquotesquoteid)
    * [POST /swappost](/reference/postswap)
    * [GET /farm-boostget](/reference/getfarmboost)
    * [POST /farm-boostpost](/reference/postfarmboost)
    * [GET /proof-dataget](/reference/getproofdata)
    * [GET /proofs-dataget](/reference/getproofsdata)
    * [GET /leaderboard/campaignget](/reference/getleaderboardcampaign)
    * [POST /campaign-sign-uppost](/reference/postcampaignsignup)
    * [GET /otc/accountget](/reference/getotcaccount)
    * [POST /otc/create-requestpost](/reference/postotccreaterequest)
    * [POST /otc/unwindpost](/reference/postotcunwind)
    * [POST /account/usernamepost](/reference/postaccountusername)
    * [GET /twap-ordersget](/reference/gettwaporders)
    * [POST /twap-orderspost](/reference/posttwaporders)
    * [DELETE /twap-orders/{order_id}del](/reference/deletetwapordersorderid)
    * [GET /twap-orders/{order_id}get](/reference/gettwapordersorderid)
    * [GET /twap-order-historyget](/reference/gettwaporderhistory)
    * [GET /account/weekly-volumeget](/reference/getaccountweeklyvolume)
    * [GET /stakeget](/reference/getstake)
    * [POST /batch-orderspost](/reference/postbatchorders)



## Websocket API

  * [Endpoints](/reference/endpoints)
  * [Operations](/reference/operations)
  * [Message Format](/reference/messaging-format-1)
  * [Managing Connection](/reference/overview-1)
  * [Cancel on Disconnect](/reference/cancel-on-disconnect)
  * [Public Operations __](/reference/publish-channel)
    * [PUBLISH Channels](/reference/publish-channel)
    * [ PUBLISH Ping](/reference/publish-ping)
    * [SUBSCRIBE Orderbook Throttled (NEW)](/reference/subscribe-orderbook-throttled)
    * [SUBSCRIBE Book Ticker (NEW)](/reference/subcribe-book-ticker)
    * [SUBSCRIBE Ticker Throttled (NEW)](/reference/subscribe-ticker-throttled)
    * [SUBSCRIBE Index](/reference/subcribe-index)
    * [SUBSCRIBE Trades](/reference/subcribe-trades)
  * [Private Operations __](/reference/websocket-authentication)
    * [Authentication](/reference/websocket-authentication)
    * [ PUBLISH Status](/reference/get-status)
    * [PUBLISH Create Order](/reference/publish-create-order)
    * [PUBLISH Edit Order](/reference/publish-edit-order)
    * [PUBLISH Cancel Order](/reference/publish-cancel-order)
    * [PUBLISH Cancel All Orders](/reference/publish-cancel-all-orders)
    * [SUBCRIBE Orders](/reference/subcribe-orders)
    * [SUBCRIBE Fills](/reference/subcribe-fills)
    * [SUBCRIBE Positions](/reference/subcribe-positions)



Powered by [](https://readme.com?ref_src=hub&project=aevo)

# GET /markets

Ask AI

get

https://api.aevo.xyz/markets

Returns a list of instruments. If `asset` is not specified, the response will include all listed instruments.

Language

 __Shell __Node __Ruby __PHP __Python

Response

Click `Try It!` to start a request and see the response here!


---

# Source: https://api-docs.aevo.xyz/reference/websocket

ERROR: Failed to fetch: 404 Client Error: Not Found for url: https://api-docs.aevo.xyz/reference/websocket


---

# Source: https://api-docs.aevo.xyz/reference/postorders

[Jump to Content](#content)

[](/reference)

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog) v1.0.2v1.0.3-beta

* * *

[Log In](/login?redirect_uri=/reference/postorders)[](/reference)

 __API Reference

[Log In](/login?redirect_uri=/reference/postorders)

v1.0.3-beta

[ __Technical Docs](/docs)[ __API Reference](/reference)[ __Changelog](/changelog)

POST /orders

All

Pages

###### Start typing to search…

JUMP TO

## Aevo API

  * [Introduction](/reference/overview)
  * [API Key Setup __](/reference/api-key-setup-via-ui)
    * [Via UI](/reference/api-key-setup-via-ui)
    * [ Via API](/reference/api-key-setup-api)
  * [Signing Orders](/reference/signing-orders)
  * [Signing Orders Without Timestamp](/reference/signing-orders-copy)
  * [Rate Limits](/reference/rate-limits-1)
  * [Orderbook Checksum](/reference/orderbook-checksum)
  * [Errors](/reference/errors)



## Aevo REST API

  * [Endpoints](/reference/urls)
  * [Public API __](/reference/getassets)
    * [GET /assets get](/reference/getassets)
    * [GET /expiriesget](/reference/getexpiries)
    * [GET /indexget](/reference/getindex)
    * [GET /index-historyget](/reference/getindexhistory)
    * [GET /mark-historyget](/reference/getmarkhistory)
    * [GET /settlement-historyget](/reference/getsettlementhistory)
    * [GET /marketsget](/reference/getmarkets)
    * [GET /statisticsget](/reference/getstatistics)
    * [GET /coingecko-statisticsget](/reference/getcoingeckostatistics)
    * [GET /orderbookget](/reference/getorderbook)
    * [GET /fundingget](/reference/getfunding)
    * [GET /funding-historyget](/reference/getfundinghistory)
    * [GET /instrument/{instrument_name}get](/reference/getinstrumentinstrumentname)
    * [GET /instrument/{instrument_name}/trade-historyget](/reference/getinstrumentinstrumentnametradehistory)
    * [GET /check-referralget](/reference/getcheckreferral)
    * [GET /emissionsget](/reference/getemissions)
    * [POST /account/unsubscribepost](/reference/postaccountunsubscribe)
    * [GET /timeget](/reference/gettime)
    * [GET /strategiesget](/reference/getstrategies)
    * [GET /yield-vaultget](/reference/getyieldvault)
    * [POST /swap/previewpost](/reference/postswappreview)
    * [GET /airdrop-incentivized-assetsget](/reference/getairdropincentivizedassets)
    * [GET /weethget](/reference/getweeth)
    * [GET /options-historyget](/reference/getoptionshistory)
    * [POST /account/email-verifiedpost](/reference/postaccountemailverified)
    * [GET /strategy/{strategy_address}/positionsget](/reference/getstrategystrategyaddresspositions)
    * [GET /strategy/{strategy_address}/trade-historyget](/reference/getstrategystrategyaddresstradehistory)
    * [GET /strategy/{strategy_address}/portfolioget](/reference/getstrategystrategyaddressportfolio)
    * [GET /strategy/{strategy_address}/balance-historyget](/reference/getstrategystrategyaddressbalancehistory)
    * [GET /strategy/{strategy_address}/transaction-historyget](/reference/getstrategystrategyaddresstransactionhistory)
    * [GET /strategy/{strategy_address}/pnl-historyget](/reference/getstrategystrategyaddresspnlhistory)
  * [Private API __](/reference/rest-authentication)
    * [Authentication](/reference/rest-authentication)
    * [ POST /registerpost](/reference/postregister)
    * [DELETE /api-keydel](/reference/deleteapikey)
    * [GET /api-keyget](/reference/getapikey)
    * [POST /api-keypost](/reference/postapikey)
    * [DELETE /signing-keydel](/reference/deletesigningkey)
    * [GET /authget](/reference/getauth)
    * [GET /accountget](/reference/getaccount)
    * [GET /positionsget](/reference/getpositions)
    * [GET /account/cancel-on-disconnectget](/reference/getaccountcancelondisconnect)
    * [POST /account/cancel-on-disconnectpost](/reference/postaccountcancelondisconnect)
    * [POST /account/portfolio-marginpost](/reference/postaccountportfoliomargin)
    * [GET /account/email-addressget](/reference/getaccountemailaddress)
    * [POST /account/email-addresspost](/reference/postaccountemailaddress)
    * [POST /account/email-preferencepost](/reference/postaccountemailpreference)
    * [GET /account/email-preferencesget](/reference/getaccountemailpreferences)
    * [GET /account/email-verifiedget](/reference/getaccountemailverified)
    * [GET /account/accumulated-fundingsget](/reference/getaccountaccumulatedfundings)
    * [POST /account/update-marginpost](/reference/postaccountupdatemargin)
    * [POST /account/margin-typepost](/reference/postaccountmargintype)
    * [POST /account/leveragepost](/reference/postaccountleverage)
    * [GET /account/trades/csvget](/reference/getaccounttradescsv)
    * [GET /account/transactions/csvget](/reference/getaccounttransactionscsv)
    * [GET /account/statsget](/reference/getaccountstats)
    * [POST /account/network-addresspost](/reference/postaccountnetworkaddress)
    * [GET /portfolioget](/reference/getportfolio)
    * [POST /withdrawpost](/reference/postwithdraw)
    * [GET /strategies/accountget](/reference/getstrategiesaccount)
    * [GET /strategies/account-historyget](/reference/getstrategiesaccounthistory)
    * [POST /strategy/{strategy_address}/initiate-withdrawpost](/reference/poststrategystrategyaddressinitiatewithdraw)
    * [POST /transferpost](/reference/posttransfer)
    * [GET /ordersget](/reference/getorders)
    * [POST /orderspost](/reference/postorders)
    * [DELETE /orders/{order_id}del](/reference/deleteordersorderid)
    * [GET /orders/{order_id}get](/reference/getordersorderid)
    * [POST /orders/{order_id}post](/reference/postordersorderid)
    * [DELETE /orders-alldel](/reference/deleteordersall)
    * [GET /order-historyget](/reference/getorderhistory)
    * [GET /order-history/stopsget](/reference/getorderhistorystops)
    * [GET /trade-historyget](/reference/gettradehistory)
    * [GET /transaction-historyget](/reference/gettransactionhistory)
    * [GET /referral-rewards-historyget](/reference/getreferralrewardshistory)
    * [GET /referral-historyget](/reference/getreferralhistory)
    * [GET /referral-statisticsget](/reference/getreferralstatistics)
    * [POST /claim-referral-rewardspost](/reference/postclaimreferralrewards)
    * [POST /claim-trade-feespost](/reference/postclaimtradefees)
    * [GET /trade-fees-campaign-statsget](/reference/gettradefeescampaignstats)
    * [GET /mmpget](/reference/getmmp)
    * [POST /mmppost](/reference/postmmp)
    * [POST /reset-mmppost](/reference/postresetmmp)
    * [DELETE /rfqsdel](/reference/deleterfqs)
    * [GET /rfqsget](/reference/getrfqs)
    * [POST /rfqspost](/reference/postrfqs)
    * [DELETE /rfqs/{block_id}del](/reference/deleterfqsblockid)
    * [GET /rfqs/{block_id}/quotesget](/reference/getrfqsblockidquotes)
    * [DELETE /quotesdel](/reference/deletequotes)
    * [GET /quotesget](/reference/getquotes)
    * [POST /quotespost](/reference/postquotes)
    * [POST /quotes/previewpost](/reference/postquotespreview)
    * [DELETE /quotes/{quote_id}del](/reference/deletequotesquoteid)
    * [PUT /quotes/{quote_id}put](/reference/putquotesquoteid)
    * [POST /swappost](/reference/postswap)
    * [GET /farm-boostget](/reference/getfarmboost)
    * [POST /farm-boostpost](/reference/postfarmboost)
    * [GET /proof-dataget](/reference/getproofdata)
    * [GET /proofs-dataget](/reference/getproofsdata)
    * [GET /leaderboard/campaignget](/reference/getleaderboardcampaign)
    * [POST /campaign-sign-uppost](/reference/postcampaignsignup)
    * [GET /otc/accountget](/reference/getotcaccount)
    * [POST /otc/create-requestpost](/reference/postotccreaterequest)
    * [POST /otc/unwindpost](/reference/postotcunwind)
    * [POST /account/usernamepost](/reference/postaccountusername)
    * [GET /twap-ordersget](/reference/gettwaporders)
    * [POST /twap-orderspost](/reference/posttwaporders)
    * [DELETE /twap-orders/{order_id}del](/reference/deletetwapordersorderid)
    * [GET /twap-orders/{order_id}get](/reference/gettwapordersorderid)
    * [GET /twap-order-historyget](/reference/gettwaporderhistory)
    * [GET /account/weekly-volumeget](/reference/getaccountweeklyvolume)
    * [GET /stakeget](/reference/getstake)
    * [POST /batch-orderspost](/reference/postbatchorders)



## Websocket API

  * [Endpoints](/reference/endpoints)
  * [Operations](/reference/operations)
  * [Message Format](/reference/messaging-format-1)
  * [Managing Connection](/reference/overview-1)
  * [Cancel on Disconnect](/reference/cancel-on-disconnect)
  * [Public Operations __](/reference/publish-channel)
    * [PUBLISH Channels](/reference/publish-channel)
    * [ PUBLISH Ping](/reference/publish-ping)
    * [SUBSCRIBE Orderbook Throttled (NEW)](/reference/subscribe-orderbook-throttled)
    * [SUBSCRIBE Book Ticker (NEW)](/reference/subcribe-book-ticker)
    * [SUBSCRIBE Ticker Throttled (NEW)](/reference/subscribe-ticker-throttled)
    * [SUBSCRIBE Index](/reference/subcribe-index)
    * [SUBSCRIBE Trades](/reference/subcribe-trades)
  * [Private Operations __](/reference/websocket-authentication)
    * [Authentication](/reference/websocket-authentication)
    * [ PUBLISH Status](/reference/get-status)
    * [PUBLISH Create Order](/reference/publish-create-order)
    * [PUBLISH Edit Order](/reference/publish-edit-order)
    * [PUBLISH Cancel Order](/reference/publish-cancel-order)
    * [PUBLISH Cancel All Orders](/reference/publish-cancel-all-orders)
    * [SUBCRIBE Orders](/reference/subcribe-orders)
    * [SUBCRIBE Fills](/reference/subcribe-fills)
    * [SUBCRIBE Positions](/reference/subcribe-positions)



Powered by [](https://readme.com?ref_src=hub&project=aevo)

# POST /orders

Ask AI

post

https://api.aevo.xyz/orders

Creates a new order.

Language

 __Shell __Node __Ruby __PHP __Python

Credentials

Header +1

 __

__

Response

Click `Try It!` to start a request and see the response here!
