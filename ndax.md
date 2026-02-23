# Ndax API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://apidoc.ndax.io/

[ NAV  ](#)

[json](#)



  * [Introduction](#introduction)
    * [Revised calls](#revised-calls)
    * [Previously unrevealed calls](#previously-unrevealed-calls)
    * [New Endpoints](#new-endpoints)
  * [Background Information](#background-information)
    * [Message Frame](#message-frame)
    * [Standard response objects and common error codes](#standard-response-objects-and-common-error-codes)
    * [Modules](#modules)
    * [Users, Accounts, and Permissions](#users-accounts-and-permissions)
    * [Products and Instruments](#products-and-instruments)
    * [Quotes and Orders](#quotes-and-orders)
    * [Timeâ and Date-Stamp Formats](#time-ndash-and-date-stamp-formats)
    * [The Trading Day](#the-trading-day)
  * [Users](#users)
    * [Activate2FA](#activate2fa)
    * [AddUserAffiliateTag](#adduseraffiliatetag)
    * [Authenticate2FA](#authenticate2fa)
    * [AuthenticateUser](#authenticateuser)
    * [CancelUserReport](#canceluserreport)
    * [EnableXP2FA](#enablexp2fa)
    * [GetL2Snapshot](#getl2snapshot)
    * [GetLevel1](#getlevel1)
    * [GetUserAccountInfos](#getuseraccountinfos)
    * [GetUserAccounts](#getuseraccounts)
    * [GetUserAffiliateCount](#getuseraffiliatecount)
    * [GetUserAffiliateTag](#getuseraffiliatetag)
    * [GetUserReportTickets](#getuserreporttickets)
    * [GetUserReportWriterResultRecords](#getuserreportwriterresultrecords)
    * [LogOut](#logout)
    * [SubscribeAccountEvents](#subscribeaccountevents)
    * [SubscribeLevel1](#subscribelevel1)
    * [SubscribeLevel2](#subscribelevel2)
    * [SubscribeTicker](#subscribeticker)
    * [SubscribeTrades](#subscribetrades)
    * [UnsubscribeLevel1](#unsubscribelevel1)
    * [UnsubscribeLevel2](#unsubscribelevel2)
    * [UnsubscribeTicker](#unsubscribeticker)
    * [UnsubscribeTrades](#unsubscribetrades)
    * [UpdateUserAffiliateTag](#updateuseraffiliatetag)
  * [Accounts](#accounts)
    * [GenerateTradeActivityReport](#generatetradeactivityreport)
    * [GenerateTransactionActivityReport](#generatetransactionactivityreport)
    * [GenerateTreasuryActivityReport](#generatetreasuryactivityreport)
    * [GetAccountInfo](#getaccountinfo)
    * [GetAccountPositions](#getaccountpositions)
    * [GetTreasuryProductsForAccount](#gettreasuryproductsforaccount)
    * [ScheduleTradeActivityReport](#scheduletradeactivityreport)
    * [ScheduleTransactionActivityReport](#scheduletransactionactivityreport)
    * [ScheduleTreasuryActivityReport](#scheduletreasuryactivityreport)
  * [Trades](#trades)
    * [GetAccountTrades](#getaccounttrades)
    * [GetAccountTransactions](#getaccounttransactions)
    * [GetOpenTradeReports](#getopentradereports)
    * [GetTickerHistory](#gettickerhistory)
    * [GetTradesHistory](#gettradeshistory)
    * [Trades](#cmc-trades)
  * [OMS Orders](#oms-orders)
    * [CancelAllOrders](#cancelallorders)
    * [CancelOrder](#cancelorder)
    * [CancelQuote](#cancelquote)
    * [CancelReplaceOrder](#cancelreplaceorder)
    * [CreateQuote](#createquote)
    * [GetOpenOrders](#getopenorders)
    * [GetOpenQuotes](#getopenquotes)
    * [GetOrderFee](#getorderfee)
    * [GetOrderHistory](#getorderhistory)
    * [GetOrderHistoryByOrderId](#getorderhistorybyorderid)
    * [GetOrdersHistory](#getordershistory)
    * [GetOrderStatus](#getorderstatus)
    * [ModifyOrder](#modifyorder)
    * [OrderBook](#cmc-orderBook)
    * [SendOrder](#sendorder)
    * [UpdateQuote](#updatequote)
  * [Products](#products)
    * [GetProduct](#getproduct)
    * [GetProducts](#getproducts)
  * [Instruments](#instruments)
    * [Assets](#cmc-assets)
    * [GetInstrument](#getinstrument)
    * [GetInstruments](#getinstruments)
  * [Tickets](#tickets)
    * [Deposit and Withdraw Templates](#deposit-and-withdraw-templates)
    * [AddDepositTicketAttachment](#adddepositticketattachment)
    * [AddWithdrawTicketAttachment](#addwithdrawticketattachment)
    * [ConfirmWithdraw](#confirmwithdraw)
    * [CreateDepositTicket](#createdepositticket)
    * [GetAccountDepositTransactions](#getaccountdeposittransactions)
    * [GetAccountWithdrawTransactions](#getaccountwithdrawtransactions)
    * [GetAllDepositRequestInfoTemplates](#getalldepositrequestinfotemplates)
    * [GetDepositRequestInfoTemplate](#getdepositrequestinfotemplate)
    * [GetDeposits](#getdeposits)
    * [GetDepositTicket](#getdepositticket)
    * [GetDepositTicketAttachment](#getdepositticketattachment)
    * [GetDepositTickets](#getdeposittickets)
    * [GetWithdrawFee](#getwithdrawfee)
    * [GetWithdraws](#getwithdraws)
    * [GetWithdrawTicket](#getwithdrawticket)
    * [GetWithdrawTicketAttachment](#getwithdrawticketattachment)
    * [GetWithdrawTickets](#getwithdrawtickets)
    * [SubmitDepositTicketComment](#submitdepositticketcomment)
    * [SubmitWithdrawTicketComment](#submitwithdrawticketcomment)
  * [Miscellaneous](#miscellaneous)
    * [GetEarliestTickTime](#getearliestticktime)
    * [Ticker](#cmc-ticker)
    * [Summary](#cmc-summary)
    * [Ping](#ping)


  * [Documentation Powered by Slate](https://github.com/lord/slate)



# Introduction

This API covers the User-category calls in **version 3.3** of the NDAX Exchange software. It includes calls required for log-in and authentication.

The calls have been organized roughly to correspond to similar functions you would find in the NDAX Admin. For example, in the Admin you manage users in the Users function. So calls that manage users have been gathered in the Users section of the API.

### Revised calls

Generally, upper- and lowercase is not important for the key-value pairs inside a request or response. If an otherwise well formed call returns an unexpected error, check the case of the key-value pairs in the request.

**AuthenticateUser**

Some integer Request values are now strings

> Old AuthenticateUser Request
    
    
    {
        "UserName": "",
        "Password":""
    } or
    {
        "APIKey": "",
        "Signature": "",
        "UserId":1,
        "Nonce": 12345
    }
    

> New AuthenticateUser Request
    
    
    {
        "UserName": "",
        "Password": ""
    } or 
    {
        "APIKey": "",
        "Signature": "",
        "UserId": "1",
        "Nonce": "12345"
     }
    

**CancelAllOrders**

The _userId_ and _instrumentId_ have been eliminated from the Request.

> Old CancelAllOrders Request
    
    
    {
        "AccountId": 0,
        "UserId": 0,
        "OMSId": 0,
        "InstrumentId": 0
    }
    

> New CancelAllOrders Request
    
    
    {
        "AccountId": 0,
        "OMSId": 0
    }
    

**CancelOrder**

_AccountId_ added to Request.

> Old CancelOrder Request
    
    
    {
        "OMSId": 0,
        "OrderId": 0,
        "ClientOrderId": 0
    }
    

> New CancelOrder Request
    
    
    {
        "OMSId": 0,
        "AccountId": 0,
        "OrderId": 0,
        "ClientOrderId": 0
    }
    

**CancelQuote**

Now separate Response objects for _BidResult_ and _AskResult_ in Response

> Old CancelQuote Response
    
    
    {
        "BidResult": "",
        "AskResult": ""
    }
    

> New CancelQuote Response
    
    
    {
     "BidResult": {
     "result": true,
      "errormsg": "",
      "errorcode": 0,
      "detail": "",
     },
     "AskResult": {
      "result": true,
       "errormsg": "",
       "errorcode": 0,
       "detail": "",
     }
    }
    

**CreateQuote**

Revised Request structure; separate Response objects for _BidResult_ and _AskResult[_

> Old CreateQuote Request
    
    
    {
        "BidQuoteId": 1,
        "BidRequest": "",
        "AskQuoteId": 1,
        "AskRequest": "" 
    }
    

> New CreateQuote Request
    
    
    {
     "OMSId": 0,
     "AccountId": 0,
     "InstrumentId": 0,
     "Bid": 0,
     "BidQty": 0,
     "Ask": 0,
     "AskQty": 0,
    }
    

> Old CreateQuote Response
    
    
    { 
        "BidQuoteId": 1,
        "BidRequest": "",
        "AskQuoteId": 1,
        "AskRequest": ""
    }
    

> New CreateQuote Response
    
    
    {
     /"BidResult": {
     / /"result": true,
     / /"errormsg": "",
     / /"errorcode": 0,
     / /"detail": "",
     /},
     /"AskResult": {
     / /"result": true,
     / /"errormsg": "",
     / /"errorcode": 0,
     / /"detail": "",
     /}
    }
    

**GetAccountInfo**

_accountHandle_ removed from Request.

> Old GetAccountInfo Request
    
    
    {
        "omsId": 0,
        "accountId": 0,
        "accountHandle": ""
    }
    

> New GetAccountInfo Request
    
    
    {
        "omsId":0,
        "accountId":0
    }
    

**GetAccountTrades**

Extended Response structure

> Old GetAccountTrades Response
    
    
    [
        {
            "omsId":0,
            "executionId":0,
            "tradeId":0,
            "orderId":0,
            "accountId":0,
            "subAccountId":0,
            "clientOrderId":0,
            "instrumentId":0,
            "side":0,
            "quantity":0.0,
            "remainingQuantity":0.0,
            "price":0.0,
            "value":0.0,
            "tradeTime":0
        },
    ]
    

> New GetAccountTrades Response
    
    
    [
        {
            "omsId": 0,
            "executionId": 0,
            "tradeId": 0,
            "orderId": 0,
            "accountId": 0,
            "subAccountId": 0,
            "clientOrderId": 0,
            "instrumentId": 0,
            "side": 0,
            "quantity": 0.0,
            "remainingQuantity": 0.0,
            "price": 0.0,
            "value": 0.0,
            "tradeTime": 0,
            "counterParty": null,
            "orderTradeRevision": 0,
            "direction": 0,
            "isBlockTrade": false,
            "tradeTimeMS": 0,
            "fee": 0.0,
            "feeProductId": 0,
            "orderOriginator": 0
        },
    ]
    

**GetAccountTransactions**

_transactionType_ and _referenceType_ have changed to integer in Response.

> Old GetAccountTransactions Response
    
    
    [
        {
            {
            "TransactionId": 0,
            "OMSId": 0,
            "AccountId": 0,
            "CR": 0,
            "DR": 0,
            "CounterParty": 0,
            "TransactionType": {
            "Options": [
                "Fee",
                "Trade",
                "Other",
                "Reverse",
                "Hold" ]
             },
            "ReferenceId": 0,
            "ReferenceType": {
                "Options": [
                  "Trade",
                  "Deposit",
                  "Withdraw",
                  "Transfer",
                  "OrderHold",
                  "WithdrawHold",
                  "DepositHold",
                  "MarginHold" ]
                },
                "ProductId": 0,
                "Balance": 0,
                "TimeStamp": 0,
            }
        ]
    

> New GetAccountTransactions Response
    
    
    [
      {
        "transactionId":0,
        "omsId":0,
        "accountId":0,
        "cr":0.0,
        "dr":0.0,
        "counterparty":0,
        "transactionType":0,
        "referenceId":0,
        "referenceType":0,
        "productId":0,
        "balance":0.0,
        "timeStamp":0
        },
    ]
    

**GetInstrument**

_priceIncrement_ added to Response

> Old GetInstrument Response
    
    
    {
        "omsId":0,
        "instrumentId":0,
        "symbol":null,
        "product1":0,
        "product1Symbol":null,
        "product2":0,
        "product2Symbol":null,
        "instrumentType":0,
        "venueInstrumentId":0,
        "venueId":0,
        "sortIndex":0,
        "sessionStatus":0,
        "previousSessionStatus":0,
        "sessionStatusDateTime":"0001-01-01T00:00:00",
        "selfTradePrevention":false,
        "quantityIncrement":0.0
    }
    

> New GetInstrument Response
    
    
    {
        "omsId": 0,
        "instrumentId": 0,
        "symbol": null,
        "product1": 0,
        "product1Symbol": null,
        "product2": 0,
        "product2Symbol": null,
        "instrumentType": 0,
        "venueInstrumentId": 0,
        "venueId": 0,
        "sortIndex": 0,
        "sessionStatus": 0,
        "previousSessionStatus": 0,
        "sessionStatusDateTime": "0001-01-01T00:00:00",
        "selfTradePrevention": false,
        "quantityIncrement": 0.0,
        "priceIncrement": 0.0
    }
    

**GetInstruments**

_priceIncrement_ added to Response

> Old GetInstruments Response
    
    
    [
        {
            "omsId":0,
            "instrumentId":0,
            "symbol":"",
            "product1":0,
            "product1Symbol":"",
            "product2":0,
            "product2Symbol":"",
            "instrumentType":0,
            "venueInstrumentId":0,
            "venueId":0,
            "sortIndex":0,
            "sessionStatus":0,
            "previousSessionStatus":0,
            "sessionStatusDateTime":"0001-01-01T00:00:00",
            "selfTradePrevention":false,
            "quantityIncrement":0.0
        },
    ]
    

> New GetInstruments Response
    
    
    [
        {
            "omsId":0 ,
            "instrumentId": 0,
            "symbol": "",
            "product1": 0,
            "product1Symbol": "",
            "product2": 0,
            "product2Symbol": "",
            "instrumentType": 0,
            "venueInstrumentId": 0,
            "venueId":0,"sortIndex": 0,
            "sessionStatus": 0,
            "previousSessionStatus": 0,
            "sessionStatusDateTime": "0001-01-01T00:00:00",
            "selfTradePrevention": false,
            "quantityIncrement": 0.0,
            "priceIncrement": 0.0
        },
    ]
    

**GetOpenOrders**

Expanded and reorganized Response structure

> Old GetOpenOrders Response
    
    
    [
        {"omsId":0,
         "side":0,
         "orderId":0,
         "price":0.0,
         "quantity":0.0,
         "displayQuantity":0.0,
         "instrument":0,
         "account":0,
         "orderType":0,
         "clientOrderId":0,
         "orderState":0
        },
    ]
    

> New GetOpenOrders Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    

**GetOpenQuotes**

Expanded and reorganized Response structure

> Old GetOpenQuotes Response
    
    
    {
        "Bid":"",
        "Ask":""
    }
    

> New GetOpenQuotes Response
    
    
    {
        "bid": {
            "omsId": 0,
            "side": 0,
            "orderId": 0,
            "price": 0.0,
            "quantity": 0.0,
            "displayQuantity": 0.0,
            "instrument": 0,
            "account": 0,
            "orderType": 0,
            "clientOrderId": 0,
            "orderState": 0
        },
        "ask": {
            "omsId": 0,
            "side": 0,
            "orderId": 0,
            "price": 0.0,
            "quantity": 0.0,
            "displayQuantity": 0.0,
            "instrument": 0,
            "account": 0,
            "orderType": 0,
            "clientOrderId": 0,
            "orderState": 0
        }
    }
    

**GetOpenTradeReports**

Expanded and reorganized Response structure

> Old GetOpenTradeReports Response
    
    
    [
        {
            "omsId":0,
            "side":0,
            "orderId":0,
            "price":0.0,
            "quantity":0.0,
            "displayQuantity":0.0,
            "instrument":0,
            "account":0,
            "orderType":0,
            "clientOrderId":0,
            "orderState":0
        },
    ]
    

> New GetOpenTradeReports Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

**GetOrderHistory**

Expanded and reorganized Response structure

> Old GetOrderHistory Response
    
    
    [
        {
            "omsId":0,
            "side":0,
            "orderId":0,
            "price":0.0,
            "quantity":0.0,
            "displayQuantity":0.0,
            "instrument":0,
            "account":0,
            "orderType":0,
            "clientOrderId":0,
            "orderState":0
        }
    ]
    

> New GetOrderHistory Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

**GetOrderHistoryByOrderId**

Expanded and reorganized Response structure

> Old GetOrderHistoryByOrderId Response
    
    
    [
        {
            "omsId":0,
            "side":0,
            "orderId":0,
            "price":0.0,
            "quantity":0.0,
            "displayQuantity":0.0,
            "instrument":0,
            "account":0,
            "orderType":0,
            "clientOrderId":0,
            "orderState":0
        }
    ]
    

> New GetOrderHistoryByOrderId Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

**GetOrdersHistory**

Expanded and reorganized Response structure

> Old GetOrdersHistory Response
    
    
    [
        {
            "omsId":0,
            "side":0,
            "orderId":0,
            "price":0.0,
            "quantity":0.0,
            "displayQuantity":0.0,
            "instrument":0,
            "account":0,
            "orderType":0,
            "clientOrderId":0,
            "orderState":0
        }
    ]
    

> New GetOrdersHistory Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

**GetOrderStatus**

Expanded and reorganized Response structure

> Old GetOrderStatus Response
    
    
    {
        "omsId":0,
        "side":0,
        "orderId":0,
        "price":0.0,
        "quantity":0.0,
        "displayQuantity":0.0,
        "instrument":0,
        "account":0,
        "orderType":0,
        "clientOrderId":0,
        "orderState":0
    }
    

> New GetOrderStatus Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

**GetTradesHistory**

Extended Response structure

> Old GetTradesHistory Response
    
    
    [
        {
            "omsId":0,
            "executionId":0,
            "tradeId":0,
            "orderId":0,
            "accountId":0,
            "subAccountId":0,
            "clientOrderId":0,
            "instrumentId":0,
            "side":0,
            "quantity":0.0,
            "remainingQuantity":0.0,
            "price":0.0,
            "value":0.0,
            "tradeTime":0
        }
    ]
    

> New GetTradesHistory Response
    
    
    [
        {
            "omsId": 0,
            "executionId": 0,
            "tradeId": 0,
            "orderId": 0,
            "accountId": 0,
            "subAccountId": 0,
            "clientOrderId": 0,
            "instrumentId": 0,
            "side": 0,
            "quantity": 0.0,
            "remainingQuantity": 0.0,
            "price": 0.0,
            "value": 0.0,
            "tradeTime": 0,
            "counterParty": null,
            "orderTradeRevision": 0,
            "direction": 0,
            "isBlockTrade": false,
            "tradeTimeMS": 0,
            "fee": 0.0,
            "feeProductId": 0,
            "orderOriginator": 0
        },
    ]
    

**SendOrder**

Request: _timeInOrder_ removed; _quantity,_ _PegPriceType_ changed to integer enumerations

> Old SendOrder Request
    
    
    {
        "InstrumentId": 1,
        "OMSId": 1,
        "AccountId": 1,
        "TimeInForce": 1,
        "ClientOrderId": 1,
        "OrderIdOCO": 0, 
        "TimeInOrder":0, 
        "UseDisplayQuantity":false, 
        "Side": 0,
        "quantity": "1",
        "OrderType": 2,
        "PegPriceType": "3",
        "LimitPrice": 8800 
    }
    

> New SendOrder Request
    
    
    {
         "InstrumentId": 1,
         "OMSId": 1,
         "AccountId": 1,
         "TimeInForce": 1,
         "ClientOrderId": 1,
         "OrderIdOCO": 0,
         "UseDisplayQuantity": false,
         "Side": 0,
         "quantity": 1,
         "OrderType": 2,
         "PegPriceType": 3,
         "LimitPrice": 8800
     }
    

**SubscribeLevel2**

Request alternative available; changed to comma-separated data from numerical key-value pairs in the Response.

> Old SubscribeLevel2 Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1,
        "Depth": 10
    }
    

> New SubscribeLevel2 Request
    
    
    {
        "OMSId":  1,
        "InstrumentId": 0
        "Depth":  10 
    }
    or
    {
        "OMSId":  1,
        "Symbol": "BTCUSD",
        "Depth":  10 
    }
    

> Old SubscribeLevel2 Response
    
    
    [
        {
            0: 1,
            1: 1,
            2: 1534865075981,
            3: 0,
            4: 6415.01,
            5: 1,
            6: 6399.79,
            7: 1, 
            8: 1.49364749, 
            9: 0
        }
    ]
    

> New SubscribeLevel2 Response
    
    
    [
        [
            0, // MDUpdateId        
            1, // AccountId
            123,// ActionDateTime in Posix format X 1000
            0,   // ActionType 0 (New), 1 (Update), 2(Delete)
            0.0, // LastTradePrice
            0, // OrderId
            0.0, //Price
            0,  // ProductPairCode
            0.0, // Quantity
            0, // Side
        ],
    ]
    

### Previously unrevealed calls

**AddProductAttributes**

_InstrumentId_ changed to _ProductId_ in Request

> Old AddProductAttributes Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1,
        "KeyName": key,
        "KeyValue": "value"
    }
    

> New AddProductAttributes Request
    
    
    {
        "OMSId": 1,
        "ProductId": 1,
        "KeyName": key,
        "KeyValue": "value"
    }
    

**AddUserInstrumentPermissionsBulk**

_InstrumentIds_ now an array in Request

> Old AddUserInstrumentPermissionsBulk Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1,
        "UserId": 1
    }
    

> New AddUserInstrumentPermissions Bulk Request
    
    
    {
        "OMSId": 1,
        "InstrumentIds": [1,2],
        "UserId": [1,2]
    }
    

**AddUserProductPermissionsBulk**

_ProductIds_ now an array in Request

> Old AddUserProductPermissionsBulk Request
    
    
    {
        "omsid":0,
        "productids":"",
        "userids":""}
    
    

> New AddUserProductPermissionsBulk Request
    
    
    {
        "omsid": 0,
        "productids": [1,2],
        "userids": [1,2]
    }
    

**GetEarliestTickTime**

Request requires only _OMSId_ and _instrumentId_

> Old GetEarliestTickTime Request
    
    
    {
        "InstrumentId": 1,
        "FromDate": date
    }
    

> New GetEarliestTickTime
    
    
    {
        "InstrumentId": 1,
        "OMSId": 1
    }
    

**RemoveProductAttributes**

_InstrumentId_ changed to _ProductId_ in Request

> Old RemoveProductAttributes Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1, 
        "KeyName": key, 
        "KeyValue": "value" 
    }
    

> New RemoveProductAttributes Request
    
    
    {
        "OMSId": 1,
        "ProductId": 1,
        "KeyName": "key",
        "KeyValue": "value"
    }
    

### New Endpoints

We have included the following new endpoints

  * **[Ticker](#cmc-ticker)**
  * **[Assets](#cmc-assets)**
  * **[Summary](#cmc-summary)**
  * **[Trades](#cmc-trades)**
  * **[OrderBook](#cmc-orderBook)**



# Background Information

This section provides important information about NDAX Exchange software.

## Message Frame

> A JSON-formatted frame object.
    
    
    {
        "m": 0,
        "i": 0,
        "n":"function name",
        "o":"payload"
    }
    

Wrap all calls in a JSON-formatted frame object. Responses from the server are similarly wrapped. The API calls are documented as payloads by function name.

Key | Value  
---|---  
_m_ message type | **integer.** The type of the message. One of:  
0 request  
1 reply  
2 subscribe-to event  
3 event  
4 unsubscribe-from event  
5 error  
_i_ sequence number | **long integer.** The sequence number identifies an individual request or request-and-response pair, to your application.  
  
The system requires a non-zero sequence number, but the numbering scheme you use is up to you. No arbitrary sequence numbering scheme is enforced by NDAX.  
  
**Best Practices:** A client-generated API call (of message types 0, 2, and 4) should:  
Carry an even sequence number  
Begin at the start of each user session  
Be unique within each user session.  
Begin with 2 (as in 2, 4, 6, 8)  
  
Message types 1 (reply), 3 (event), and 5 (error) are generated by the server. These messages echo the sequence number of the message to which they respond. See the example, following.  
_n_ function name | **string.** The function name is the name of the function being called or that the server is responding to. The server echoes your call. See the example, following.  
_o_ payload | Payload is a JSON-formatted string containing the data being sent with the message. Payload may consist of request parameters (key-value pairs) or response parameters.  
**Note:Â** You can send the key-value pairs inside the payload in any order. The server controls the order of its response.

### Example 1

> Example 1
    
    
    var frame =
    {
        "m":0,
        "i":0,
        "n":"function name",
        "o":""
    };
    
    var requestPayload =
    {
        "parameter1":"value",
        "parameter2":0
    };
    
    frame.o = json.Stringify(requestPayload);
    // Stringify escapes the payload's quotation marks automatically.
    WS.Send(json.Sringify(frame)); // WS.Send escapes the frame
    

When sending a request in the frame to the software using JavaScript, a call looks like Example 1.

> Example 2

### Example 2
    
    
    var frame = json.Parse(wsMessage);
    
    if (frame.m == 1) // message of type reply
    {
        //This is a reply
        if (frame.n == "WebAuthenticateUser")
        {
            var LoginReply = json.Parse(frame.o);
            if (loginReply.Authenticated)
            {
                var user = LoginReplay.User;
            }
        }
    }
    

When receiving a frame from the software, use the frame to determine the context, and then unwrap the content, as in Example 2.

**Note:Â** If not using JSON Stringify, escape quotation marks.

## Standard response objects and common error codes

A response to an API call usually consists of a specific response, but both successful and unsuccessful responses may consist of a generic response object that verifies only that the call was received, and not that the action requested by the call took place. A generic response to an unsuccessful call provides an error code. A generic response looks like Example 3.

### Example 3

> Example 3
    
    
    {
        "result":true,
        "errormsg":"",
        "errorcode": 0,
        "detail":"",
    }
    

Key | Value  
---|---  
result | **Boolean.** If the call has been successfully received by the Order Management System, result is _true_ ; otherwise it is _false_.  
errormsg | **string.** A successful receipt of the call returns _null_. The _errormsg_ key for an unsuccessful call returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Response (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the call returns 0. An unsuccessful receipt of the call returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. The content of this key is usually _null_.  
  
## Modules

The NDAX software consists of several modules that include the Order Management System (OMS), the matching engine, and the Asset Manager. During installation, each is assigned an ID.

The Order Management System is the mechanism that manages access to the trading venue. The OMS controls permissions, accounts, and users. The OMS must be specified in many calls.

The order book resides on the NDAX matching engine.

A trading venue is a combination of OMS and matching engine that creates a place to access the market and trade. A venue maintains its order book and matching engine, and may access several Order Management Systems.

The Asset Manager controls the deposit and withdrawal of funds belonging to an account. These funds can be denominated in any product that the trading venue allows.

## Users, Accounts, and Permissions

The NDAX software differentiates between _user_ and _account_. A user is the person who logs in; an account represents the funds and trading that the user does — much like a bank account represents funds and checks.

As with a bank account, an individual user may have multiple Exchange accounts. Similarly, multiple users may trade through a single account. There may be users who have trading access to one set of accounts that overlap (but do not duplicate) the set of accounts that another user can access. There may be a many-to-many relationship where two or more users have access to a set of accounts.

The use case for this kind of "joint tenancy" is an active trading desk where a specific individual may not always be present. If User A will not be present, User B can monitor and trade on the market. User A may wish to cancel his pending trades for a specific account or instrument, but not those of his trading partner under the same account or for the same instrument.

Permissions handle the rules that determine what a user can access and do with orders, cancellations, and the other tasks of a trading venue. Most permissions encompass tasks such as trading, depositing, or withdrawing funds; but a permission can be set for each API call for each individual in the venue.

An administrator with Operator permission sets up a user's permissions on the OMS when the user joins the trading venue, and only an administrator with Operator permission or above can change them. A full discussion of permissions is not part of this API.

## Products and Instruments

In NDAX software, a _product_ is an asset that is tradable or paid out. A product might be a national currency, a crypto-currency, or something else such as a commodity. For example, a product might be a US Dollar or a New Zealand Dollar or a BitCoin or an ounce of gold. Transaction and withdrawal fees are denominated in products. (Products may be referred to as _assets_ in some API calls.)

An _instrument_ is a pair of exchanged products (or fractions of them). For example, US Dollar for BitCoin. In conventional investment parlance, a stock or a bond is called an instrument, but implicit in that is the potential exchange of one product for another (stock for dollars). NDAX software thinks of that exchange as explicit, and separates product from instrument.

## Quotes and Orders

The NDAX API includes calls related to both quotes and orders. Quoting is not enabled for the retail end user of NDAX software. Only registered market participants or marketmakers may quote. Your trading venue may offer quotes separately from orders.

  * A quote expresses a willingness to buy or sell at a given price.
  * An order is a directive to buy or sell.



In this version of the NDAX matching engine software, quotes and orders are synonymous. They both can buy or sell. This is because the matching engine (like most matching engines) requires a "firm quote" — a guaranteed bid or ask.

For both quotes and orders, trading priority is the same, and no preference is given one over the other. In code, the matching engine flags a quote for eventual regulatory and compliance rules, but for current software operation and trade execution, quotes and orders behave equivalently.

### Best Practices/Quotes and Orders

Use the order-related API calls in preference to quote-related calls unless you specifically require quote-related calls.

## Time– and Date-Stamp Formats

NDAX software uses two different time– and date-stamp formats, POSIX and Microsoft Ticks. Where the value of a time field key is an integer or long, the value is in POSIX format; when the value of a time field key is a string, it is in Microsoft Ticks format (also called _datetime_).

  * **POSIX** stores date/time values as the number of seconds since 1 January 1970 (long integer). NDAX software often multiples this number by 1000 for the number of milliseconds since 1 January 1970. **Recognize POSIX format:** POSIX format is a long integer. It is usually formatted like this: `1501603632000`  
  

  * **Microsoft Ticks** (datetime) format represents the number of ticks that have elapsed since 00:00:00 UTC, 1 January 0001, in the Gregorian calendar. A single tick represents one hundred nanoseconds (one ten-millionth of a second). There are 10,000 ticks in a millisecond; ten million ticks in a second. Ticks format does not include the number of ticks attributable to leap-seconds. **Recognize Ticks format:** Ticks format is a string. In NDAX software, it is usually formatted like this: `"2018-08-17T17:57:56Z"` Note that a T (for time) separates the initial date from the time. The trailing Z represents the time zone, in all cases in NDAX software, this is UTC (also called Zulu time).



## The Trading Day

Most NDAX installations operate 24-hour computer-based trading venues. The trading day runs from UTC Midnight to UTC Midnight (essentially, London time, but without any summertime offset), regardless of the nominal location of the venue. Values such as open or close are those values as of UTC Midnight. Values for day, month, or annual periods run from UTC Midnight to UTC Midnight.

# Users

These calls correspond roughly to the Users function of the Exchange Admin and Admin Guide.

## Activate2FA

**Category:** Activation  
**Permissions:** Public  
**Call Type:** Synchronous

### Request
    
    
    {
      "Code":"YourCode"
    }
    

Completes the second half of a two-factor authentication by sending the 2FA code while registering for the exchange.

Key | Value  
---|---  
Code | **string.** The alphanumeric code you received for authentication.  
  
### Response
    
    
    {
      "Activated": true,
      "Error":"ErrorMessage"
    }
    

Key | Value  
---|---  
Activated | **Boolean.** _True_ if the activation code is accepted; _false_ if not.  
Error | **string.** Error message from the server.  
  
## AddUserAffiliateTag

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Associates a user affiliate tag to a user. An affiliate tag allows a user to encourage others to join the exchange and provides a way to track those new members back to the initiating user.

### Request
    
    
    {
      "omsId":0,
      "userId":0,
      "affiliateId":0,
      "affiliateTag":""
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the user operates.  
userId | **integer.** The user's ID.  
affiliateId | **integer.** The affiliate ID.  
affiliateTag | **string.** The alphanumeric tag used to identify new affiliating members.  
  
### Response
    
    
    {
      "result":true,
      "errormsg":"",
      "errorcode":0,
      "detail":""
    }
    

Key | Value  
---|---  
result | **Boolean.** _True_ signifies that the server has received the request to associate the affiliate tag with a specific user (not that it has done so); _false_ signifies an error.  
errormsg | **string.** A successful response returns _null_ ; the _errormsg_ parameter for an unsuccessful response returns one of the following messages: Not Authorized (_errorcode_ 20), Invalid Request (_errorcode_ 100), Operation Failed (_errorcode_ 101), Server Error (_errorcode_ 102), Resource Not Found (_errorcode_ 104)  
errorcode | **integer.** A successful response returns 0. An unsuccessful response returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## Authenticate2FA

**Category:** Authentication  
**Permissions:** Public  
**Call Type:** Synchronous

### Request
    
    
    {
    Â â¯"Code": "YourCode"
    }
    

Completes the second part of a two-factor authentication by sending the authentication token from the non-AlphaPoint authentication system to the Order Management System. The call returns a verification that the user logging in has been authenticated, and a token.

Here is how the two-factor authentication process works:

  1. Call **webauthenticateuser**. The response includes values for _TwoFAType_ and _TwoFAToken_. For example, _TwoFAType_ may return "Google," and the _TwoFAToken_ then returns a Google-appropriate token (which in this case would be a QR code).
  2. Enter the _TwoFAToken_ into the two-factor authentication program, for example, Google Authenticator. The authentication program returns a different token.
  3. Call **authenticate2FA** with the token you received from the two-factor authentication program (shown as _YourCode_ in the Request example below).

Key | Value  
---|---  
Code | **string**. _Code_ holds the token obtained from the other authentication source.  
  
### Response
    
    
    {
    Â â¯"Authenticated": true,
    Â â¯"SessionToken": "YourSessionToken"
    }
    

Key | Value  
---|---  
Authenticated | **Boolean**. A successful authentication returns _true_. Unsuccessful returns _false_.  
SessionToken | **string**. The _SessionToken_ is valid during the current session for connections from the same IP address. If the connection is interrupted during the session, you can sign back in using the _SessionToken_ instead of repeating the full two-factor authentication process. A session lasts one hour after the last-detected activity or until logout.  
  
> To send a session token to re-establish an interrupted session:
    
    
    {
    Â â¯"SessionToken": "YourSessionToken"
    }
    

## AuthenticateUser

**Category:** Authentication  
**Permissions:** Public  
**CallType:** Synchronous

### Request

> Use this request call
    
    
    {
      "UserName": "",
      "Password": ""
    }
    

> Or you can use this request call
    
    
    {
      "APIKey": "28c68ac3fcfafc3d4e8d653fe57e5baf",
      "Signature": "29c15c42e4fabcc9e229421e148e647903927c503ab4578ada55bb13a63a9636",
      "UserId": "96",
      "Nonce": "2247733562"
    }
    

Authenticates a user for the current websocket session.

Key | Value  
---|---  
Username | **string.** The user's assigned user name.  
Password | **string.** The user's assigned password.  
  
or

Key | Value  
---|---  
APIKey | **string.** This is an AlphaPoint-generated key used in user-identification.  
Signature | **string.** A long, alphanumeric string generated by AlphaPoint by using the APIKey and Nonce.  
UserId | **string.** The ID of the user, stated as a string.  
Nonce | **string.** Any arbitrary number or random string used with the APIKey to generate a signature.  
  
### Response
    
    
    {
      "user":
      { "userId": 0,
        "userName": "",
        "email": "",
        "emailVerified": false,
        "accountId": 0,
        "omsId": 0,
        "use2FA": false
      },
      "authenticated": false,
      "locked": false,
      "requires2FA": false,
      "twoFAType": "",
      "twoFAToken": ""
    }
    
    

Key | Value  
---|---  
user | JSON user object (below)  
authenticated | **Boolean.** _True_ if the user is authenticated; _false_ otherwise.  
locked | **Boolean.** _True_ if this affiliated user is currently locked; _false_ otherwise. A user may be locked by trying to log in too many times in rapid succession. He must be _unlocked_ by an admin.  
requires2FA | **Boolean.** _True_ if the user must use two-factor authentication; _false_ otherwise.  
twoFAType | **string.** Returns the type of 2FA this user requires. For example, "Google."  
twoFAToken | **string.** Returns an appropriate token. In the case of Google, this is a QR code.  
  
JSON user object:

Key | Value  
---|---  
userId | **integer.** The ID of the user being authenticated on the exchange.  
userName | **string.** The name of the user.  
email | **string.** The email address of the user.  
emailVerified | **Boolean.** Whether the email address has been verified by the registration process or directly by an Admin.  
accountId | **integer.** The ID of the account with which the user is associated (each user has a default account).  
omsId | **integer.** The ID of the Order Management System with which the user and account are associated.  
use2FA | **Boolean.** _True_ if the user must use 2FA to log in; _false_ otherwise.  
  
## CancelUserReport

**Category:** Users  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

You can generate or schedule a variety of reports through this API on demand. This call cancels a scheduled report by its report ID. **GetUserReportTickets** can provide a list of GUIDs for scheduled reports.

### Request
    
    
    {
      "UserReportId": guid-as-a-string //GUID not GUIDE
    }
    

Key | Value  
---|---  
UserReport | **string**. The GUID is a globally unique ID string that identifies the user report to be canceled. The Order Management System provides this ID when you create a report.  
  
### Response
    
    
    {
      "result": true,
      "errormsg": "",
      "errorcode": 0,
      "detail": "",
    }
    

The response to **CancelUserReport** verifies that the call was received, not that the user report has been canceled successfully. Individual event updates sent to the user show cancellations. To verify that a report has been canceled, call **GetUserReportTickets** or **GetUserReportWriterResultRecords**.

Key | Value  
---|---  
result | **Boolean**. A successful receipt of the cancellation returns true; and unsuccessful receipt of the cancellation (an error condition) returns false.  
errormsg | **string**. A successful receipt of the cancellation returns null; the _errormsg_ parameter for an unsuccessful receipt returns one of the following messages: Not Authorized (errorcode 20, Invalid Request (errorcode 100), Operation Failed (errorcode 101), Server Error (errorcode 102), Resource Not Found (errorcode 104)  
errorcode | **integer**. A successful receipt of the cancellation returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string**. Message text that the system may send. Usually _null_.  
  
## EnableXP2FA

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

EnableXP2FA is a custom two-factor-authentication scheme (like Google 2FA). It generates 2FA code and has the ability to verify these codes.

### Request
    
    
    {
      "Phone": "",
      "Capability":""
    }
    

Key | Value  
---|---  
Phone | **string.** A 13-digit Brazilian phone number. Example: +5511965536992  
Capability | **string.** Method of validation. Possible values are:  
SMS  
Phone  
OTP (an app)  
  
### Response
    
    
    {
      "Enabled2FA": true,
      "Activate2FA":true
    }
    

Key | Value  
---|---  
Enabled2FA | **Boolean.** _True_ if XP two-factor authentication is enabled; _false_ if not.  
Activate2FA | **Boolean.** _True_ if XP two-factor authentication is to be activated; _false_ if not.  
  
## GetL2Snapshot

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Provides a current Level 2 snapshot of a specific instrument trading on an Order Management System to a user-determined market depth. The Level 2 snapshot allows the user to specify the level of market depth information on either side of the bid and ask.

Depth in this call is "depth of market," the number of buyers and sellers at greater or lesser prices in the order book for the instrument.

### Request
    
    
    {
      "OMSId": 1,
      "InstrumentId": 1,
      "Depth": 100 
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System where the instrument is traded.  
InstrumentId | **integer**. The ID of the instrument that is the subject of the snapshot.  
Depth | **integer**. Depth of the market â the number of buyers and sellers at greater or lesser prices in the order book for the instrument. Defaults to 100.  
  
### Response
    
    
    [
        [
            0, // MDUpdateId        
            1, // AccountId
            123,// ActionDateTime in Posix format X 1000
            0,   // ActionType 0 (New), 1 (Update), 2(Delete)
            0.0, // LastTradePrice
            0, // OrderId
            0.0, //Price
            0,  // ProductPairCode
            0.0, // Quantity
            0, // Side
        ],
    ]
    
    // This is how the response is sent:
    
    [[0,1,123,0,0.0,0,0.0,0,0.0,0]]
    

The response is an array of elements for one specific instrument, the number of elements corresponding to the market depth specified in the Request. It is sent as an uncommented, comma-delimited list of numbers. The example is commented. The _Level2UpdateEvent_ contains the same data, but is sent by the OMS whenever trades occur. To receive _Level2UpdateEvents_ , a user must subscribe to _Level2UpdateEvents_.

Key | Value  
---|---  
MDUpdateID | **integer**. Market Data Update ID. This sequential ID identifies the order in which the update was created.  
AccountId | **integer**. The ID of the account trading the instrument.  
ActionDateTime | **long integer.**. _ActionDateTime_ identifies the time and date that the snapshot was taken or the event occurred, in POSIX format X 1000 (milliseconds since 1 January 1970).  
ActionType | **integer**. L2 information provides price data. This value shows whether this data is:  
**0** new  
**1** update  
**2** deletion  
LastTradePrice | **real**. The price at which the instrument was last traded.  
OrderId | **integer**. The ID of the order.  
Price | **real**. Bid or Ask price for the Quantity (see _Quantity_ below).  
ProductPairCode | **integer**. _ProductPairCode_ is the same value and used for the same purpose as _InstrumentID_. The two are completely equivalent. _InstrumentId_ 47 = _ProductPairCode_ 47.  
Quantity | **real**. Quantity available at a given Bid or Ask price (see _Price_ above).  
Side | **integer**. One of:  
**0** Buy  
**1** Sell  
**2** Short (reserved for future use)  
**3** Unknown (error condition)  
  
## GetLevel1

**Category:** User  
**Permissions:** GetLevel1, Trading  
**Call Type:** Synchronous

Provides a current Level 1 snapshot (best bid, best offer) of a specific instrument trading on an Order Management System. The Level 1 snapshot does not allow the user to specify the level of market depth information on either side of the bid and ask.

### Request
    
    
    {
      "OMSId":1,
      "InstrumentId":1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the OMS on which the snapshot will be taken.  
InstrumentId | **integer.** The ID of the instrument whose Level 1 market snapshot will be taken.  
  
### Response

> _productPairCode_ is the same as _InstrumentId_. The two are synonymous and refer to the same object.
    
    
    {
      "exchangeId": 0,
      "productPairCode": 0,
      "bestBid": 0.0,
      "bestOffer": 0.0,
      "volume": 0.0,
      "lastTradedPx": 0.0,
      "lastTradedVolume": 0.0,
      "lastTradeTime": 0,
      "timeStamp": 0,
      "bidQty": 0.0,
      "askQty": 0.0,
      "bidOrderCt": 0,
      "askOrderCt": 0,
      "sessionOpen": 0.0,
      "sessionHigh": 0.0,
      "sessionLow": 0.0,
      "sessionClose": 0.0,
      "currentDayVolume": 0.0,
      "currentDayNumTrades": 0.0,
      "currentDayPxChange": 0.0,
      "rolling24HrVolume": 0.0,
      "rolling24NumTrades": 0.0,
      "rolling24HrPxChange": 0.0,
      "rolling24HrPxChangePercent": 0.0
    } 
    

Key | Value  
---|---  
exchangeId | **integer.** The ID of the exchange whose snapshot was taken.  
productPairCode | **integer.** The ID of the instrument (the product pair) whose prices, bids, asks, and volumes are being reported.  
bestBid | **real.** The current best bid for the instrument (product pair).  
bestOffer | **real.** The current best offer for the instrument (product pair).  
volume | **real.** The unit volume of the instrument traded, either during a true session (with a market open and close), or in 24-hour markets, it is the period from UTC Midnight to UTC Midnight, regardless of the nominal location of the market.  
lastTradedPX | **real.** The last-traded price for the instrument.  
lastTradedVolume | **real.** The last quantity that was traded.  
lastTradeTime | **real.** The last time that the instrument was traded.  
timeStamp | **real.** The date and time of this snapshot.  
bidQty | **real.** The quantity currently being bid.  
askQty | **real.** The quantity currently being asked.  
bidOrderCt | **integer.** The count of bid orders.  
askOrderCt | **integer.** The count of ask orders.  
sessionOpen | **real.** Opening price. In markets with openings and closings, this is the opening price for the current session; in 24-hour markets, it is the price as of UTC Midnight beginning the current day.  
sessionHigh | **real.** Highest price during the trading day, either during a true session (openings and closings) or UTC Midnight to UTC Midnight.  
sessionLow | **real.** Lowest price during the trading day, either during a true session (openings and closings) or UTC Midnight to UTC Midnight.  
sessionClose | **real.** The closing price. In markets that open and close, this is the closing price for the current or most recent session; for 24-hour markets, it is the price as of the most recent UTC Midnight.  
currentDayVolume | **real.** The unit volume of the instrument that is the subject of the snapshot, either during a true session (openings and closings) or in 24-hour markets, during the period UTC Midnight to UTC Midnight.  
currentDayNumTrades | **integer.** The number of trades during the current day, either during a true session (openings and closings) or in a 24-hour market the period from UTC Midnight to UTC Midnight.  
currentDayPxChange | **real.** Change in price over the current session or from UTC Midnight to UTC Midnight.  
rolling24HrVolume | **real.** Unit volume of the instrument over the past 24 hours, regardless of time zone. This value recalculates continuously.  
rolling24HrNumTrades | **real.** Number of trades during the past 24 hours, regardless of time zone. This value recalculates continuously.  
rolling24HrPxChange | **real.** Price change during the past 24 hours, regardless of time zone. This value recalculates continuously.  
rolling24HrPxChangePercent | **real.** Percent change in price during the past 24 hours.  
  
## GetUserAccountInfos

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns a list of account information for all accounts belonging to the specified user.

### Request
    
    
    {
    Â â¯"OMSId": 0,
    Â â¯"UserId": 0,
    Â â¯"UserName": "",
    }
    

Key | Value  
---|---  
OMSId | **integer**. The Order Management System on which the user has one ore more accounts.  
UserId | **integer**. The ID of the user whose accounts you want to return.  
UserName | **string**. The name of the user.  
  
### Response

> Returns a JSON list of account objects; one for each account associated with the user.
    
    
    {
    Â â¯"OMSID": 0,
    Â â¯"AccountId": 0,
    Â â¯"AccountName": "",
    Â â¯"AccountHandle": "",
    Â â¯"FirmId": "",
    Â â¯"FirmName": "",
    Â â¯"AccountType": {
    Â â¯Â â¯"Options":[
    Â â¯Â â¯Â â¯"Asset",
    Â â¯Â â¯Â â¯"Liability",
    Â â¯Â â¯Â â¯"ProfitLoss"
    Â â¯Â â¯] 
    Â â¯},
    Â â¯"FeeGroupID": 0,
    Â â¯"ParentID": 0,
    Â â¯"RiskType": {
    Â â¯Â â¯"Options": [
    Â â¯Â â¯Â â¯"Unknown",
    Â â¯Â â¯Â â¯"Normal",
    Â â¯Â â¯Â â¯"NoRiskCheck",
    Â â¯Â â¯Â â¯"NoTrading"
    Â â¯Â â¯] 
    Â â¯},
    Â â¯"VerificationLevel": 0,
    Â â¯"FeeProductType": {
    Â â¯Â â¯"Options": [
    Â â¯Â â¯Â â¯"BaseProduct",
    Â â¯Â â¯Â â¯"SingleProduct"
    Â â¯Â â¯] 
    Â â¯},
    Â â¯"FeeProduct": 0,
    Â â¯"RefererId": 0,
    Â â¯"SupportedVenueIds": [
    Â â¯Â â¯0
    Â â¯],
    }
    

Key | Value  
---|---  
OMSID | **integer**. The ID of the Order Management System on which the account resides.  
AccountId | **integer**. The ID of the account for which information was requested.  
AccountName | **string.** The name of the account.  
AccountHandle | **string**. _AccountHandle_ is a unique user-assigned name that is checked at create time by the Order Management System.  
FirmId | **string**. An arbitrary identifier assigned by a trading venue operator to a trading firm as part of the initial company, user, and account set up process. For example, Smith Financial Partners might have the ID SMFP.  
FirmName | **string**. A longer, non-unique version of the trading firmâs name; for example, Smith Financial Partners.  
AccountType | **string**. The type of the account for which information is being returned. One of:   
Asset  
Liability  
ProfitLoss  
  
Responses for this string/value pair for Market Participants are almost exclusively _Asset_.  
FeeGroupID | **integer**. Defines account attributes relating to how fees are calculated and assessed. Set by trading venue operator.  
ParentID | **integer**. Reserved for future development.  
RiskType | **string**. One of:  
Unkown (an error condition)  
Normal  
NoRiskCheck  
NoTrading   
  
Returns _Normal_ for virtually all market participants. Other types indicate account configurations assignable by the trading venue operator.  
VerificationLevel | **Integer**. Verification level ID (how much verification does this account require) defined by and set by the trading venue operator for this account.  
FeeProductType | **string**. One of:  
BaseProduct  
SingleProduct   
  
Transaction fees may be charged by a trading venue operator. This value shows whether fees for this accountâs trades are charged in the product being traded (_BaseProduct_ , for example BitCoin) or whether the account has a preferred fee-paying product (_SingleProduct_ , for example USD) to use in all cases and regardless of product being traded.  
FeeProduct | **integer**. The ID of the preferred fee product, if _SingleProduct_ is the value of _FeeProductType_.  
RefererId | **integer**. Captures the ID of the person who referred this account to the trading venue, usually for marketing purposes.  
SupportedVenueIds | **integer array**. Comma-separated array. Reserved for future expansion. Currently returns 0.  
  
## GetUserAccounts

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns a list of account IDs for a given user. More than one user may be associated with a given account. 

### Request
    
    
    {
    Â â¯"omsId": 0,
    Â â¯"userId": 0,
    Â â¯"userName": "",
    }
    

Key | Value  
---|---  
OMSId | **integer**. The Order Management System on which the user has one ore more accounts.  
UserId | **integer**. The ID of the user whose accounts you want to return.  
UserName | **string**. The name of the user.  
  
### Response

The response returns list of comma-separated account IDs.
    
    
    {
    Â â¯0, // a list of account IDs
    }
    

## GetUserAffiliateCount

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Gets a count of users who have been referred to the exchange by the identified user.

### Request
    
    
    {
      "OMSId":1,
      "UserId":1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the user operates.  
UserId | **integer.** The ID of the user.  
  
### Response
    
    
    {
      "Count":0
    }
    

Key | Value  
---|---  
Count | **integer.** The count of exchange users who have been referred to the exchange by the user identified by _UserId_ in the request.  
  
## GetUserAffiliateTag

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an array of affiliate tags associated with the identified user. The exchange can use an affiliate tag to identify new users who join the exchange as a result of a recommendation from the identified user. A user may have multiple affiliate tags.

### Request
    
    
    {
      "userId": 0,
      "omsId": 0
    }
    

Key | Value  
---|---  
userId | **integer.** The ID of the user whose affiliate tag you want to retrieve.  
omsId | **integer.** The ID of the Order Management System on which the user operates.  
  
### Response

The response is an array of affiliate tag information, with an object for each affiliate tag associated with the user.
    
    
    [
      {
         "omsId": 0,
         "userId": 0,
         "affiliateId": 0,
         "affiliateTag": ""
      },
    ]
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the user operates. This echoes the _omsId_ in the request.  
userId | **integer.** The ID of the user whose affiliate tag is returned. Echoes the _userId_ in the request.  
affiliateId | **integer.** The ID of the affiliate.  
affiliateTag | **string.** The tag that the user can share.  
  
## GetUserReportTickets

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an array of user report tickets for a specific user ID. A user report ticket identifies a report requested or subscribed to by a user. Reports can run once or periodically.

### Request
    
    
    {
      "UserId":  1 
    }
    

Key | Value  
---|---  
UserId | **integer**. The ID of the user whose user report tickets will be returned.  
  
### Response

The response returns an array of tickets, each ticket representing a report.
    
    
    [
      {
        {
          "RequestingUser": 0,
          "OMSId": 0,
          "reportFlavor": {
            "Options": [
                  "TradeActivity",
                  "Transaction",
                  "Treasury"
             ]
           },
           "createTime": "0001-01-01T05:00:00Z",
           "initialRunTime": "0001-01-01T05:00:00Z",
           "intervalStartTime": "0001-01-01T05:00:00Z",
           "intervalEndTime": "0001-01-01T05:00:00Z",
           "RequestStatus": {
             "Options": [
               "Submitted",
               "Validating",
               "Scheduled",
               "InProgress",
               "Completed",
               "Aborting",
               "Aborted",
               "UserCancelled",
               "SysRetired",
               "UserCancelledPending"
             ]
           },
           "ReportFrequency": {
             "Options": [
               "onDemand",
               "Hourly",
               "Daily",
               "Weekly",
               "Monthly",
               "Annually"
              ]
            }
           "intervalDuration": 0,
           "RequestId": "I2nCtvyY8UuHsoSyrLe2QA==",
           "lastInstanceId": "AAAAAAAAAAAAAAAAAAAAAA==",
           "accountIds": [
             1
            ],
          },
        }
      ]
    

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the report.  
OMSId | **integer.** The ID of the Order Management System on which the report was run.  
reportFlavor | **string.** The type of report. One of  
Tradeactivity  
Transaction  
Treasury  
createTime | **string.** The time and date at which the request for the report was made, Microsoft Ticks format.  
initialRunTime | **string.** The time and date at which the report was first run, Microsoft Ticks format.  
intervalStartTime | **string.** The start of the period that the report will cover, Microsoft Ticks format.  
intervalEndTime | **string.** The end of the period that the report will cover, Microsoft Ticks format.  
RequestStatus | **string.** The status of the request for the report. Each status returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelPending  
ReportFrequency | **string.** When the report runs:  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report looks backward relative to the run date, in POSIX format. The system calculates _intervalDuration_ between _intervalStartTime_ and _intervalEndTime_ and reports it in POSIX format. For example, say that you specify a 90-day start-to-end-date window for a report. The _intervalDuration_ value returns a value equivalent to 90 days and represents the backward-looking period of the report. Say that you have set up a weekly report to look back 90 days. When the report runs again in a week's time, it again looks back 90 days -- but now those 90 days are offset by a week from the first report.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report. This will be _null_ for a Generate~Report call, because generated reports are all on-demand.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## GetUserReportWriterResultRecords

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

The call returns an array of user report writer results. The results are the details of when reports have been run and the status of each report run.

Users with Trading permission can request user report writer result records only for their own user IDs; users with Operator permission can request any user's report writer result records.

**Note:Â** "Depth" in this call is the count of records to be returned, not market depth.

### Request
    
    
    {
        "userId":0,
        "depth":50,
        "startIndex":0
    }
    

Key | Value  
---|---  
userId | **integer.** The ID of the user whose report writer result records will be returned.  
depth | **integer.** The count of records to be returned, beginning at _startIndex_ and working backwards into the past. For example, for a _startIndex_ of 100 and a _depth_ of 50 **GetUserReportWriterResultRecords** will return records numbered between 100 and 149, inclusive. The value of _depth_ defaults to 50.  
startIndex | **integer.** The record number at which the call starts returning records; from there, record return moves into the past. The most recent record is record 0. The value of _startIndex_ defaults to 50.  
  
### Response
    
    
    [
        {
            "RequestingUser":1,
            "urtTicketId":"mGzjUfylGEmqgJIxu651aQ==",
            "descriptorId":"47TlpPQyTkKR4LKl9Hy1yA==",
            "resultStatus":"SuccessComplete",
            "reportExecutionStartTime":"2018-08-17T17:57:56Z",
            "reportExecutionCompleteTime":"2018-08-17T17:57:57Z",
            "reportOutputFilePathname":"",
            "reportDescriptiveHeader":"TradeActivity|onDemand|2018-08-10T04:00:00.000Z|2018-08-10T05:00:00.000Z|2018-08-17T17:57:51.852Z|2018-08-17T17:57:56.840Z|0.19634 seconds"
        },
    ]
    

Key | Value  
---|---  
RequestingUser | **Integer**. ID of the user requesting the report writer result records.  
urtTicketId | **string**. An alphanumeric string containing the unique report ID of the report.  
descriptorId | **string**. A GUID (globally-unique identifier) that describes the report separately from the report ticket.  
resultStatus | **string**. The status of each run of the reports. One of:  
0 NotStarted  
1 NotComplete  
2 ErrorComplete  
3 SuccessComplete  
4 Cancelled  
reportExecutionStartTime | **string.** The time that the report writer began execution, in Microsoft Ticks format.  
reportExecutionCompleteTime | **string.** The time that the report writer completed the report, in Microsoft Ticks format.  
reportOutputFilePathname | **string.** The pathname (location) of the report output file.  
reportDescriptiveHeader | **string**. A string describing the report.  
  
## LogOut

**Category:** Authentication  
**Permissions:** Public  
**Call Type:** Synchronous

**LogOut** ends the current websocket session.

### Request

There is no payload for a **LogOut** request.
    
    
    { }
    

### Response
    
    
    {
    Â â¯"result":true,
    Â â¯"errormsg":null,
    Â â¯"errorcode":0,
    Â â¯"detail":null
    }
    

Key | Value  
---|---  
result | **Boolean**. A successful logout returns _true_ ; an unsuccessful logout (an error condition) returns _false_.  
errormsg | **string**. A successful logout returns null; the _errormsg_ parameter for an unsuccessful logout returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Response (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
  
Not Authorized and Resource Not Found are unlikely errors for a **LogOut**.  
errorcode | **integer**. A successful logout returns _0_. An unsuccessful logout returns one of the errorcodes shown in the _errormsg_ list.  
detail | **string**. Message text that the system may send. Usually _null_.  
  
## SubscribeAccountEvents

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Subscribes the user to notifications about the status of account-level events: orders, trades, position updates, deposits, and withdrawals for a specific account on the Order Management System (OMS). The subscription reports all events associated with a given account; there is no filter at the call level to subscribe to some events and not others.

Account event information is supplied in comma-separated-value (CSV) format. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
      "AccountId":  1,
      "OMSId":  1 
    }
    

Key | Value  
---|---  
AccountId | **integer**. The ID of the account for the logged-in user.  
OMSId | **integer**. The ID of the Order Management System to which the account belongs.  
  
### Response
    
    
    {
      "Subscribe":  true 
    }
    

Key | Value  
---|---  
Subscribe | **Boolean**. A successful subscription returns _true_ ; otherwise, _false_.  
  
### The Events

When you call **SubscribeAccountEvents** , you subscribe to all of the following list of events. The Order Management System may supply them at irregular intervals and in any order; software must listen for these events. The system sends each of these events in a message frame.

### AccountPositionEvent

> **AccountPositionEvent** The balance in your account changes.
    
    
    {
        "OMSId":4, //The OMSId. [Integer]
        "AccountId":4, // account id number. [Integer]
        "ProductSymbol":"BTC", //The Product Symbol for this balance message. [String]
        "ProductId":1, //The Product Id for this balance message. [Integer]
        "Amount":10499.1,  //The total balance in the account for the specified product. [Dec]
        "Hold": 2.1,  //The total amount of the balance that is on hold. Your available                          //balance for trading and withdraw is (Amount - Hold). [Decimal]
        "PendingDeposits":0, //Total Deposits Pending for the specified product. [Decimal]
        "PendingWithdraws":0, //Total Withdrawals Pending for the specified product. [Decimal]
        "TotalDayDeposits":0, //The total 24-hour deposits for the specified product. UTC. [Dec]
        "TotalDayWithdraws":0 //The total 24-hour withdraws for the specified product. UTC [Dec]
    }
    

**Trigger:** The balance in your account changes.

### CancelAllOrdersRejectEvent

> **CancelAllOrdersRejectEvent** All orders for your account are rejected.
    
    
    {
        "OMSId": 1, // OMS ID [Integer]
        "AccountId": 4, // ID of the account being tracked [Integer]
        "InstrumentId": 0, // ID of the instrument in the order [Long Integer]
        "Status": "Rejected", // Accepted/Rejected [String]
        "RejectReason": "Instrument not found." // Reason for rejection [String]
    }
    

**Trigger:** All orders for your account are rejected.

### CancelOrderRejectEvent

> **CancelOrderRejectEvent** Your order is canceled.
    
    
    {
        "OMSId": 1, //OMS Id [Integer] Always 1
        "AccountId": 4, //Your Account ID. [Integer]
        "OrderId": 1, //The Order ID from your Cancel request. [64 Bit Integer]
        "OrderRevision": 0, //The Revision of the Order, if any was found. [64 Bit Integer]
        "OrderType": "Unknown", // See "Order Types" in Introduction
        "InstrumentId": 1,  // The InstrumentId from your Cancel request. [Integer]
        "Status": "Rejected", //Always "Rejected" [String]
        "RejectReason": "Order Not Found" //A message describing the reason for the rejection.          // [String]
    }
    

**Trigger:** Your order is canceled.

### CancelReplaceOrderRejectEvent

> **CancelReplaceOrderRejectEvent** Your order is rejected even if a cancel-replace order was placed.
    
    
    {
        "OMSId": 1, // ID of the OMS [integer]
        "AccountId": 4, // ID of the account [integer]
        "OrderId": 9342, // The ID of the rejected order [integer]
        "ClientOrderId": 1234, // The client-supplied order ID [long integer]
        "LimitPrice": 99.1, // The limit price of the order.
        "OrderIdOCO": 0, // The ID of the other ordre to cancel if this is executed.
        "OrderType": "Limit", // See "Order Types" in Introduction.
        "PegPriceType": "Bid", // Where to peg the stop/trailing order.
        "OrderIdToReplace": 9333, // The ID of the order being cancelled and replaced.
        "InstrumentId": 1, // ID of the instrument traded in the order.
        "ReferencePrice": 99.1, // used internally.
        "Quantity": 1.0, // Quantity of the replacement order
        "Side": "Buy", // Side of the order: Buy, Sell, Short (future)
        "StopPrice":0, // The price at which to execute the new order.
        "TimeInForce":"GTC", // Period when new order can be executed.
        "Status":"Rejected", // Status of the order â always "rejected"
        "RejectReason":"Order Not Found" // Reason the order was rejected.
    }
    

**Trigger:** Your order is rejected even if a cancel-replace order was placed.

### MarketStateUpdate

> **MarketStateUpdate** The market state is altered administratively.
    
    
    {
        "ExchangeId":1, // Exchange Id [Integer]
        "VenueAdapterId":1,  // Internal [Integer]
        "VenueInstrumentId":1, // Instrument Id on a specific venue [Integer]
        "Action":"ReOpen",
            // Market State Action [String] Values are 
            // "Pause", "Resume", "Halt", "ReOpen"
        "PreviousStatus":"Stopped", 
            // Previous Market Status for Instrument [String] Values are
            // "Running", "Paused", "Stopped", "Starting"
        "NewStatus":"Running",
            // Market Status for Instrument [String] Values are 
            // "Running", "Paused", "Stopped", "Starting"
        "ExchangeDateTime":"2016-04-21T21:48:22Z"
            // ISO 8601 format UTC time zone
    }
    

**Trigger:** The market state is altered administratively.

### NewOrderRejectEvent

> **NewOrderRejectEvent** An order associated with your account is rejected.
    
    
    {
        "OMSId": 1, //OMS Id [Integer] Always 1
        "AccountId": 4, //Your Account Id [Integer]
        "ClientOrderId": 1234, //Your Client Order Id [64 Bit Integer]
        "Status": "Rejected", //Always "Rejected"
        "RejectReason": "No More Market" //A message describing the reason for the reject.
    }
    

**Trigger:** An order associated with your account is rejected.

### OrderStateEvent

> **OrderStateEvent** The status changes for an order associated with your account.
    
    
    {
        "Side":"Sell",
            // The side of your order. [String] Values are "Sell", 
            // "Buy", "Short"
        "OrderId": 9849, //The Server-Assigned Order Id. [64-bit Integer]
        "Price": 97, //The Price of your order. [Decimal]
        "Quantity":1,
            // The Quantity (Remaining if partially or fully executed) of 
            // your order. [Decimal]
        "Instrument":1, // The InstrumentId your order is for. [Integer]
        "Account":4, // Your AccountId [Integer]
        "OrderType":"Limit",
            // The type of order. [String] Values are "Market", "Limit",
            // "StopMarket", "StopLimit", "TrailingStopMarket", and
            // "TrailingStopLimit"
        "ClientOrderId":0, // Your client order id. [64-bit Integer]
        "OrderState":"Working", // The current state of the order. [String]
                // Values are "Working", "Rejected", "FullyExecuted", "Canceled",
                // "Expired"
        "ReceiveTime":0, // Timestamp in POSIX format
        "OrigQuantity":1, // The original quantity of your order. [Decimal]
        "QuantityExecuted":0, // The total executed quantity. [Decimal]
        "AvgPrice":0, // Avergage executed price. [Decimal]
        "ChangeReason":"NewInputAccepted"
            // The reason for the order state change. [String] Values are 
            // "NewInputAccepted", "NewInputRejected", "OtherRejected",
            // "Expired", "Trade", SystemCanceled BelowMinimum", 
            // "SystemCanceled NoMoreMarket", "UserModified"
    }
    

**Trigger:** The status changes for an order associated with your account.

### OrderTradeEvent

> **OrderTradeEvent** An order associated with your account results in a trade.
    
    
    {
        "OMSId":1, //OMS Id [Integer]
        "TradeId":213, //Trade Id [64-bit Integer]
        "OrderId":9848, //Order Id [64-bit Integer]
        "AccountId":4, //Your Account Id [Integer]
        "ClientOrderId":0, //Your client order id. [64-bit Integer]
        "InstrumentId":1, //Instrument Id [Integer]
        "Side":"Buy", //[String] Values are "Buy", "Sell", "Short" (future)
        "Quantity":0.01, //Quantity [Decimal]
        "Price":95,  //Price [Decimal]
        "Value":0.95,  //Value [Decimal]
        "TradeTime":635978008210426109, // TimeStamp in Microsoft ticks format
        "ContraAcctId":3,
            // The Counterparty of the trade. The counterparty is always 
            // the clearing account. [Integer]
        "OrderTradeRevision":1, //Usually 1 
        "Direction":"NoChange" //"Uptick", "Downtick", "NoChange"
    }
    

**Trigger:** An order associated with your account results in a trade.

### PendingDepositUpdate

> **PendingDepositUpdate** Deposit pending on your account.
    
    
    {
        "AccountId": 4, // Your account id number. [Integer]
        "AssetId": 1, // The ProductId of the pending deposit. [Integer]
        "TotalPendingDepositValue": 0.01 //The value of the pending deposit. [Decimal]
        "Requires2FA": false,
        "TwoFAType": "",
        "TwoFAToken": "",
    }
    

**Trigger:** Deposit pending on your account.

## SubscribeLevel1

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Retrieves the latest Level 1 Ticker information and then subscribes the user to ongoing Level 1 market data event updates for one specific instrument. 

The **SubscribeLevel1** call responds with the Level 1 response shown below. The OMS then periodically sends in the same format as this response _Leve1UpdateEvent_ information when best-bid/best-offer issue, until you send the **UnsubscribeLevel1** call.

Only a user with Operator permission can issue Level1MarketData permission using the call _**AddUserMarketDataPermission._ * 

### Request

> You can identify the instrument with its ID or with its market symbol (string).
    
    
    {
        "OMSId":  1,
        "InstrumentId": 0
    }
    

> Or
    
    
    {
        "OMSId":  1,
        "Symbol": "BTCUSD"
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System on which the instrument trades.  
InstrumentId | **integer**. The ID of the instrument youâre tracking. _Conditionally optional._  
Symbol | **string**. The symbol of the instrument youâre tracking. _Conditionally optional._  
  
### Response

The **SubscribeLevel1** response and _Level1UpdateEvent_ both provide the same information. 
    
    
    {
      "OMSId": 1,
      "InstrumentId": 1,
      "BestBid": 6423.57,
      "BestOffer": 6436.53,
      "LastTradedPx": 6423.57,
      "LastTradedQty": 0.96183964,
      "LastTradeTime": 1534862990343,
      "SessionOpen": 6249.64,
      "SessionHigh": 11111,
      "SessionLow": 4433,
      "SessionClose": 6249.64,
      "Volume": 0.96183964,
      "CurrentDayVolume": 3516.31668185,
      "CurrentDayNumTrades": 8529,
      "CurrentDayPxChange": 173.93,
      "Rolling24HrVolume": 4319.63870783,
      "Rolling24NumTrades": 10585,
      "Rolling24HrPxChange": -0.4165607307408487,
      "TimeStamp": "1534862990358"
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System on which the instrument trades.  
InstrumentId | **integer**. The ID of the instrument being tracked.  
BestBid | **real**. The current best bid for the instrument.  
BestOffer | **real**. The current best offer for the instrument.  
LastTradedPx | **real**. The last-traded price for the instrument.  
LastTradedQty | **real**. The last-traded quantity for the instrument.  
LastTradeTime | **long integer**. The time of the last trade, in POSIX format.  
SessionOpen | **real**. Opening price. In markets with openings and closings, this is the opening price for the current session; in 24-hour markets, it is the price as of UTC Midnight.  
SessionHigh | **real**. Highest price during the trading day, either during a session with opening and closing prices or UTC midnight to UTC midnight.  
SessionLow | **real**. Lowest price during the trading day, either during a session with opening and closing prices or UTC midnight to UTC midnight.  
SessionClose | **real**. The closing price. In markets with openings and closings, this is the closing price for the current session; in 24-hour markets, it is the price as of UTC Midnight.  
Volume | **real**. The unit volume of the instrument traded, either during a session with openings and closings or in 24-hour markets, the period from UTC Midnight to UTC Midnight.  
CurrentDayVolume | **real**. The unit volume of the instrument traded either during a session with openings and closings or in 24-hour markets, the period from UTC Midnight to UTC Midnight.  
CurrentDayNumTrades | **integer**. The number of trades during the current day, either during a session with openings and closings or in 24-hour markets, the period from UTC Midnight to UTC Midnight.  
CurrentDayPxChange | **real**. Current day price change, either during a trading session or UTC Midnight to UTC midnight.  
Rolling24HrVolume | **real**. Unit volume of the instrument during the past 24 hours, regardless of time zone. Recalculates continuously.  
Rolling24HrNumTrades | **integer**. Number of trades during the past 24 hours, regardless of time zone. Recalculates continuously.  
Rolling24HrPxChange | **real**. Price change during the past 24 hours, regardless of time zone. Recalculates continuously.  
TimeStamp | **long integer**. The time this information was provided, in POSIX format.  
  
## SubscribeLevel2

**Category:** User  
**Permissions:** Operator, Trading, Level2MarketData  
**Call Type:** Synchronous

Retrieves the latest Level 2 Ticker information and then subscribes the user to Level 2 market data event updates for one specific instrument. Level 2 allows the user to specify the level of market depth information on either side of the bid and ask. The **SubscribeLevel2** call responds with the Level 2 response shown below. The OMS then periodically sends _Level2UpdateEvent_ information in the same format as this response until you send the **UnsubscribeLevel2** call.

Only a user with Operator permission can issue a Level2MarketData permission using the call **AddUserMarketDataPermission.**

**Note:** _Depth_ in this call is "depth of market," the number of buyers and sellers at greater or lesser prices in the order book for the instrument.

### Request
    
    
    {
        "OMSId":  1,
        "InstrumentId": 0
        "Depth":  10 
    }
    

> or
    
    
    {
        "OMSId":  1,
        "Symbol": "BTCUSD"
        "Depth":  10 
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the instrument trades.  
InstrumentId | **integer.** The ID of the instrument youâre tracking. _Conditionally optional._  
Symbol | **string.** The symbol of the instrument youâre tracking. _Conditionally optional._  
Depth | **integer.** The depth of the order book. The example request returns 10 price levels on each side of the market.  
  
### Response
    
    
    [
        [
            0, // MDUpdateId        
            1, // AccountId
            123,// ActionDateTime in Posix format X 1000
            0,   // ActionType 0 (New), 1 (Update), 2(Delete)
            0.0, // LastTradePrice
            0, // OrderId
            0.0, //Price
            0,  // ProductPairCode
            0.0, // Quantity
            0, // Side
        ],
    ]
    

The response is an array of elements for one specific instrument, the number of elements corresponding to the market depth specified in the Request. It is sent as an uncommented, comma-delimited list of numbers. The example is commented.

Key | Value  
---|---  
MDUpdateID | **integer**. Market Data Update ID. This sequential ID identifies the order in which the update was created.  
AccountId | **integer**. The ID of the account trading the instrument.  
ActionDateTime | **long integer.**. _ActionDateTime_ identifies the time and date that the snapshot was taken or the event occurred, in POSIX format X 1000 (milliseconds since 1 January 1970).  
ActionType | **integer**. L2 information provides price data. This value shows whether this data is:  
**0** new  
**1** update  
**2** deletion  
LastTradePrice | **real**. The price at which the instrument was last traded.  
OrderId | **integer**. The ID of the order.  
Price | **real**. Bid or Ask price for the Quantity (see _Quantity_ below).  
ProductPairCode | **integer**. _ProductPairCode_ is the same value and used for the same purpose as _InstrumentID_. The two are completely equivalent. _InstrumentId_ 47 = _ProductPairCode_ 47.  
Quantity | **real**. Quantity available at a given Bid or Ask price (see _Price_ above).  
Side | **integer**. One of:  
**0** Buy  
**1** Sell  
**2** Short (reserved for future use)  
**3** Unknown (error condition)  
  
## SubscribeTicker

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Subscribes a user to a Ticker Market Data Feed for a specific instrument and interval. **SubscribeTicker** sends a response object as described below, and then periodically returns a _TickerDataUpdateEvent_ that matches the content of the response object.

Only a user with Operator permission can issue a Level1MarketData permission using the call **AddUserMarketDataPermission.**

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1,
        "Interval": 60,
        "IncludeLastCount": 100 
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System  
InstrumentId | **long integer.** The ID of the instrument whose information you want to track.  
Interval | **integer.** Specifies in seconds how frequently to obtain ticker updates. Default is 60 â one minute.  
IncludeLastCount | **integer.** The limit of records returned in the ticker history. The default is 100.  
  
### Response
    
    
    [
      [1501603632000, \\DateTime - UTC - Milliseconds since 1/1/1970
       2700.33, \\High 
       2701.2687.01, \\Low
       2687.01, \\Open
       2687.01, \\Close
       24.86100992, \\Volume
       0, \\Inside Bid Price
       2870.95, \\Inside Ask Price
       1], \\InstrumentId
    
      [1501604532000,2792.73,2667.95,2687.01,2700.81,242.61340767,0,2871,0]
        ]
    

The response returns an array of objects , each object an unlabeled, comma-delimited array of numbers. The Open price and Close price are those at the beginning of the tick â the Interval time subscribed to in the request. For 24-hour exchanges, the trading day runs from UTC midnight to UTC midnight; highs, lows, opens, closes, and volumes consider that midnight-to-midnight period to be the trading day. The data order is:

  * date/time UTC in milliseconds since 1/1/1970
  * high
  * low
  * open
  * close
  * volume
  * inside bid price
  * inside ask price
  * instrument ID



A typical response might look like this: `[[1510719222970.21,6943.51,6890.27,6898.41,6891.16,0,6890.98,6891.98,1,1510718681956.34]],`

## SubscribeTrades

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Subscribes an authenticated user to the Trades Market Data Feed for a specific instrument. Each trade has two sides: _Buy_ and _Sell_.

**SubscribeTrades** returns the response documented here for your immediate information, then periodically sends the _OrderTradeEvent_ documented in **SubscribeAccountEvents.**

Only a user with Operator permission can issue the permission Level1MarketData using the call **AddUserMarketDataPermission.**

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1,
        "IncludeLastCount": 100 
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System on which the instrument is traded.  
InstrumentId | **long integer**. The ID of the instrument whose trades will be reported.  
IncludeLastCount | **integer**. Specifies the number of previous trades to retrieve in the immediate snapshot. Default is 100.  
  
### Response

> Numerical keys reduce package transmission load. See Response table for an explanation.
    
    
    [
         {
             0: 1713390,
             1: 1,
             2: 0.25643269,
             3: 6419.77,
             4: 203100209,
             5: 203101083,
             6: 1534863265752,
             7: 2,
             8: 1,
             9: 0,
             10: 0
         }
     ]
    

The response returns an array of trades. The keys of each trade are numbers to reduce payload traffic.

Key | Value  
---|---  
0 (TradeId) | **integer.** The ID of this trade.  
1 (ProductPairCode) | **integer.** _ProductPairCode_ is the same number and used for the same purpose as _InstrumentID_. The two are completely equivalent in value. InstrumentId 47 = ProductPairCode 47.  
2 (Quantity) | **real.** The quantity of the instrument traded.  
3 (Price) | **real.** The price at which the instrument traded.  
4 (Order1) | **integer.** The ID of the first order that resulted in the trade, either Buy or Sell.  
5 (Order2) | **integer.** The ID of the second order that resulted in the trade, either Buy or Sell.  
6 (Tradetime) | **long integer.** UTC trade time in Total Milliseconds. POSIX format.  
7 (Direction) | **integer.** Effect of the trade on the instrumentâs market price. One of:  
0 NoChange  
1 UpTick  
2 DownTick  
8 (TakerSide) | **integer.** Which side of the trade took liquidity? One of:  
0 Buy  
1 Sell  
  
The maker side of the trade provides liquidity by placing the order on the book (this can be a buy or a sell order). The other, taker, side takes the liquidity. It, too, can be buy-side or sell-side.  
9 (BlockTrade) | **Boolean.** Was this a privately negotiated trade that was reported to the OMS? A private trade returns 1 (_true_); otherwise 0 (_false_). Default is _false_. Block trades are not supported in exchange version 3.1  
10 (order1ClientId or order2ClientId) | **integer.** The client-supplied order ID for the trade. Internal logic determines whether the program reports the _order1ClientId_ or the _order2ClientId_.  
  
## UnsubscribeLevel1

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Unsubscribes the user from a Level 1 Market Data Feed subscription.

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the user has subscribed to a Level 1 market data feed.  
InstrumentId | **long integer.** The ID of the instrument being tracked by the Level 1 market data feed.  
  
### Response
    
    
    {
        "result": true,
        "errormsg": null,
        "errorcode":0,
        "detail": null
    }
    

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the unsubscribe request returns _true_ ; and unsuccessful receipt (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the unsubscribe request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the unsubscribe request returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## UnsubscribeLevel2

**Category:** User  
**Permissions:** Operator, Trading, Level2MarketData  
**Call Type:** Synchronous

Unsubscribes the user from a Level 2 Market Data Feed subscription.

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the user has subscribed to a Level 2 market data feed.  
InstrumentId | **long integer.** The ID of the instrument being tracked by the Level 2 market data feed.  
  
### Response
    
    
    {
        "result": true,
        "errormsg": null,
        "errorcode":0,
        "detail": null
    }
    

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the unsubscribe request returns _true_ ; and unsuccessful receipt (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the unsubscribe request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the unsubscribe request returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## UnsubscribeTicker

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Unsubscribes the user from a Ticker Market Data Fee.

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the user has subscribed to a ticker market data feed.  
InstrumentId | **long integer.** The ID of the instrument being tracked by the ticker market data feed.  
  
### Response
    
    
    {
        "result": true,
        "errormsg": null,
        "errorcode":0,
        "detail": null
    }
    

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the unsubscribe request returns _true_ ; and unsuccessful receipt (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the unsubscribe request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the unsubscribe request returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## UnsubscribeTrades

**Category:** User  
**Permissions:** Operator, Trading, Level1MarketData  
**Call Type:** Synchronous

Unsubscribes the user from a Trades Market Data Feed

### Request
    
    
    {
        "OMSId": 1,
        "InstrumentId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the user has subscribed to a trades market data feed.  
InstrumentId | **long integer.** The ID of the instrument being tracked by the trades market data feed.  
  
### Response
    
    
    {
        "result": true,
        "errormsg": null,
        "errorcode":0,
        "detail": null
    }
    

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the unsubscribe request returns _true_ ; and unsuccessful receipt (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the unsubscribe request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the unsubscribe request returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## UpdateUserAffiliateTag

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Updates the user affiliate tag with new or revised information. An affiliate tag allows a user to encourage others to join the exchange and provides a way to track those new members back to the initiating user.

### Request
    
    
    {
        "omsId":0,
        "userId":0,
        "affiliateId":0,
        "affiliateTag":""
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the user and his affiliate tag operates.  
userId | **integer.** The ID of the user whose affiliate tag you are modifying.  
affiliateId | **integer.** The ID of the affiliate.  
affiliateTag | **string.** The alphanumeric tag used to identify new affiliating members.  
  
### Response
    
    
    {
      "result":true,
      "errormsg":"",
      "errorcode":0,
      "detail":""
     }
    

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the unsubscribe request returns _true_ ; and unsuccessful receipt (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the unsubscribe request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** A successful receipt of the unsubscribe request returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
# Accounts

These calls correspond roughly to the Accounts function of the Exchange Admin and Admin Guide.

## GenerateTradeActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Creates an immediate report on historical trade activity on a specific Order Management System for a list of accounts during a specified time interval.

A user with Trading permission can only generate reports for accounts with which he is associated; a user with Operator permission can generate reports for accounts associated with others.

The Trade Activity Report is delivered as a comma-separated (CSV) file. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
        "accountIdList": [
            0 // one or more Account IDs
        ],
        "omsId": 0,
        "startTime": "0001-01-01T05:00:00Z",
        "endTime": "0001-01-01T05:00:00Z",
    }
    

Key | Value  
---|---  
accountIdList | **integer array.** A comma-delimited array of one ore more account IDs, each valid on a single Order Management System for the authenticated user. The account user may not be the only user of the account.  
omsId | **integer.** The ID of the Order Management System on which the array of account IDs exist.  
startTime | **string.** _startTime_ identifies the time and date for the historic beginning of the trade activity report.  
endTime | **string.** _endTime_ identifies the time and date for the historic end of the trade activity report.  
  
### Response
    
    
    {
      "RequestingUser":1,
      "OMSId":1,
      "reportFlavor": {
             "Options": [
                "TradeActivity",
                "Transaction",
                "Treasury"
            ] 
        },
      "createTime":"2018-08-17T15:34:20Z",
      "initialRunTime":"2018-08-17T15:34:20Z",
      "intervalStartTime":"2019-04-10T04:00:00Z",
      "intervalEndTime":"2020-04-10T04:00:00Z",
      "RequestStatus": {
             "Options": [
                "Submitted",
                "Validating",
                "Scheduled",
                "InProgress",
                "Completed",
                "Aborting",
                "Aborted",
                "UserCancelled",
                "SysRetired",
                "UserCancelledPending"
            ] 
        },
      "ReportFrequency": {
             "Options":  [
                "onDemand",
                "Hourly",
                "Daily",
                "Weekly",
                "Monthly",
                "Annually"
            ] 
        },
      "intervalDuration":316224000000000,
      "RequestId":"Moy/IpfPA0SLUHNYt54q4w==",
      "lastInstanceId":"AAAAAAAAAAAAAAAAAAAAAA==",
      "accountIds":[1]
     }
    

Similar objects are returned for **Generate~Report** and **Schedule~Report** calls. As a result, for an on-demand **Generate~Report** call, some string-value pairs such as _initialRunTime_ may return the current time and _ReportFrequency_ will always return _OnDemand_ because the report is only generated once and on demand.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the trade activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the trade activity report will be run.  
reportFlavor | **string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the trade activity report was made.  
initialRunTime | **string.** The time and date at which the trade activity report was first run.  
intervalStartTime | **string.** The start of the period that the report will cover.  
intervalEndTime | **string.** The end of the period that the report will cover.  
RequestStatus | **string.** The status of the request for the trade activity report. A Generate~Report request will always return _Submitted_. Each request returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelled  
Pending  
ReportFrequency | **string.** When the report runs. For a **Generate~Report** call, this is always OnDemand. One of:  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date. The **Generate~Report** call requires a start time and an end time. The AlphaPoint software calculates the difference between them as _intervalDuration_.  
  
For example, say that you specify a 90-day start-date-to-end-date window for a report. The _intervalDuration_ value returns a value equivalent to 90 days. If you have called **Generate~Report** , that value simply confirms the length of time that the on-demand report covers.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report. Will be _null_ for a **Generate~Report** call, because generated reports are on-demand.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## GenerateTransactionActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Generates an immediate report on account transaction activity for a list of accounts under a single Order Management System during a specified time. A user with Trading permission can only generate reports for accounts with which he is associated; a user with Operator permission can generate reports for accounts associated with others. There can be multiple users associated with an account. 

The Transaction Activity Report is delivered as a comma-separated (CSV) file. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
        "accountIdList": [
            0
        ],
        "omsId": 0,
        "startTime": "0001-01-01T05:00:00Z",
        "endTime": "0001-01-01T05:00:00Z",
    }
    

Key | Value  
---|---  
accountIdList | **integer array.** A comma-delimited array of one ore more account IDs, each valid on the same Order Management System on which the user is authenticated.  
omsId | **integer.** The ID of the Order Management System on which the array of account IDs exist.  
startTime | **string.** _startTime_ identifies the time and date for the beginning of the transaction activity report, in ISO 8601 format.  
endTime | **string.** _endTime_ identifies the time and date for the end of the transaction activity report, in ISO 8601 format.  
  
### Response
    
    
    { 
      "RequestingUser":1,
      "OMSId":1,
      "reportFlavor": {
             "Options":  [
                "TradeActivity",
                "Transaction",
                "Treasury"
            ] 
        },
      "createTime":"2018-08-17T15:46:07Z",
      "initialRunTime":"2018-08-17T15:46:07Z",
      "intervalStartTime":"2019-04-10T04:00:00Z",
      "intervalEndTime":"2020-04-10T04:00:00Z",
      "RequestStatus": {
             "Options": [
                "Submitted",
                "Validating",
                "Scheduled",
                "InProgress",
                "Completed",
                "Aborting",
                "Aborted",
                "UserCancelled",
                "SysRetired",
                "UserCancelledPending"
            ] 
        },
      "ReportFrequency": {
             "Options":  [
                "onDemand",
                "Hourly",
                "Daily",
                "Weekly",
                "Monthly",
                "Annually"
            ] 
        },
      "intervalDuration":316224000000000,
      "RequestId":"+QgyhnEFqEazyZ46Q902MA==",
      "lastInstanceId":"AAAAAAAAAAAAAAAAAAAAAA==",
      "accountIds":[1]
    }
    

Similar objects are returned for **Generate~Report** and **Schedule~Report** calls. As a result, for an on-demand **Generate~Repor** t call, some string-value pairs such as _initialRunTime_ may return the current time and _ReportFrequency_ will always return _OnDemand_ because the report is only generated once and on demand.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the transaction activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the transaction activity report will be run.  
reportFlavor | **string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the trade activity report was made.  
initialRunTime | **string.** The time and date at which the trade activity report was first run. Returns the current time for a **Generate~Report** call.  
intervalStartTime | **string.** The start of the period that the report will cover.  
intervalEndTime | **string.** The end of the period that the report will cover.  
RequestStatus | **string.** The status of the request for the trade activity report. A **Generate~Report** request will always return _Submitted_. Each request returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelled  
Pending  
ReportFrequency | **string.** When the report runs. For a **Generate~Report** call, this is always _OnDemand_.  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date. The **Generate~Report** call requires a start time and an end time. The AlphaPoint software calculates the difference between them as _intervalDuration_.   
  
For example, say that you specify a 90-day start-date-to-end-date window for a report. The _intervalDuration_ value returns a value equivalent to 90 days. If you have called **Generate~Report** , that value simply confirms the length of time that the on-demand report covers.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report. Will be _null_ for a **Generate~Report** call, because generated reports are on-demand.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## GenerateTreasuryActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Generates an immediate report on all company _treasury_ activities related to the trading venue â those withdrawals, transfers, and funds movements that are unrelated to specific trades â over a specified period. 

A user with Trading permission can only generate reports for accounts with which he is associated; a user with Operator permission can generate reports for accounts associated with others. There can be multiple users associated with an account.

The Trade Activity Report is delivered as a comma-separated (CSV) file. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
        "accountIdList": [
            0
        ],
        "omsId": 0,
        "startTime": "0001-01-01T05:00:00Z",
        "endTime": "0001-01-01T05:00:00Z",
    }
    

Key | Value  
---|---  
accountIdList | **integer array.** A comma-delimited array of one ore more account IDs, each valid on a single Order Management System. For a user with Trading permission, the user must be associated with the accounts. The account user might not be the only user of the account.  
omsId | **integer.** The ID of the Order Management System on which the array of account IDs exists.  
startTime | **string.** _startTime_ identifies the time and date for the historic beginning of the trade activity report.  
endTime | **string.** _endTime_ identifies the time and date for the historic end of the trade activity report  
  
### Response
    
    
    {
        "RequestingUser":1,
        "OMSId":1,
        "reportFlavor": {
             "Options":  [
                "TradeActivity",
                "Transaction",
                "Treasury"
            ] 
        },
        "createTime":"2018-08-17T15:38:59Z",
        "initialRunTime":"2018-08-17T15:38:59Z",
        "intervalStartTime":"2019-04-10T04:00:00Z",
        "intervalEndTime":"2020-04-10T04:00:00Z",
        "RequestStatus": {
             "Options":  [
                "Submitted",
                "Validating",
                "Scheduled",
                "InProgress",
                "Completed",
                "Aborting",
                "Aborted",
                "UserCancelled",
                "SysRetired",
                "UserCancelledPending"
            ] 
        },
        "ReportFrequency": {
             "Options":  [
                "onDemand",
                "Hourly",
                "Daily",
                "Weekly",
                "Monthly",
                "Annually"
            ] 
        },
        "intervalDuration":316224000000000,
        "RequestId":"adduAIKE6Ee0eGxFM+ydsg==",
        "lastInstanceId":"AAAAAAAAAAAAAAAAAAAAAA==",
        "accountIds":[1]
    }
    

Similar objects are returned for **Generate~Report** and **Schedule~Report** calls. As a result, for an on-demand **Generate~Report** call, some string-value pairs such as _initialRunTime_ may return the current time and _ReportFrequency_ will always return _OnDemand_ because the report is only generated once and on demand.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the treasury activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the transaction activity report will be run. Note capitalization change from the request.  
reportFlavor | **string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the trade activity report was made.  
initialRunTime | **string.** The time and date at which the trade activity report was first run. Returns the current time for a Generate~Report call.  
intervalStartTime | **string.** The start of the period that the report will cover.  
intervalEndTime | **string.** The end of the period that the report will cover.  
RequestStatus | **string.** The status of the request for the trade activity report. A Generate~Report request will always return _Submitted_. Each request returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelled  
Pending  
ReportFrequency | **string.** When the report runs. For a **Generate~Report** call, this is always OnDemand.  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date. The Generate~Report call requires a start time and an end time. The AlphaPoint software calculates the difference between them as _intervalDuration_.   
  
For example, say that you specify a 90-day start-date-to-end-date window for a report. The _intervalDuration_ value returns a value equivalent to 90 days. If you have called **Generate~Report,** that value simply confirms the length of time that the on-demand report covers.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report. Will be _null_ for a **Generate~Report** call, because generated reports are on-demand.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## GetAccountInfo

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns detailed information about one specific account and existing on a specific Order Management System.

### Request
    
    
    {
        "omsId":0,
        "accountId":0
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the account exists.  
accountId | **integer.** The ID of the account on the Order Management System for which information will be returned.  
  
### Response
    
    
    {
        "omsid":0,
        "accountId":0,
        "accountName":"",
        "accountHandle":"",
        "firmId":"",
        "firmName":"",
        "accountType": {
    Â â¯Â â¯  "Options": [
    Â â¯Â â¯Â â¯ "Asset", // 0 
    Â â¯Â â¯Â â¯ "Liability", // 1
    Â â¯Â â¯Â â¯ "ProfitLoss" // 2
    Â â¯Â â¯  ] 
    Â   â¯},
        "feeGroupID":0,
        "parentID":0,
        "riskType": {
    Â â¯Â â¯  "Options": [
    Â â¯Â â¯Â     â¯"Unknown", // 0
    Â â¯Â â¯Â     â¯"Normal", // 1
    Â â¯Â â¯Â     â¯"NoRiskCheck", // 2
    Â â¯Â â¯Â â¯  "NoTrading" // 3
    Â â¯Â â¯  ] 
    Â â¯   },
        "verificationLevel":0,
        "feeProductType": {
    Â â¯Â â¯  "Options": [
    Â â¯Â â¯Â â¯ "BaseProduct", // 0
    Â â¯Â â¯Â â¯ "SingleProduct" // 1
    Â â¯Â â¯  ] 
    Â â¯   },
        "feeProduct":0,
        "refererId":0,
        "loyaltyProductId":0,
        "loyaltyEnabled":false,
        "marginEnabled":false,
        "liabilityAccountId":0,
        "lendingAccountId":0,
        "profitLossAccountId":0
    }
    
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the account resides.  
accountId | **integer.** The ID of the account for which information was requested.  
accountName | **string.** A non-unique name for the account assigned by the user.  
accountHandle | **string.** _accountHandle_ is a unique user-assigned name that is checked at create time by the Order Management System to assure its uniqueness.  
firmId | **string.** An arbitrary identifier assigned by a trading venue operator to a trading firm as part of the initial company, user, and account set up process. For example, Smith Financial Partners might have the ID SMFP.  
firmName | **string.** A longer, non-unique version of the trading firmâs name; for example, Smith Financial Partners.  
accountType | **integer.** The type of the account for which information is being returned. One of:  
Asset (0)  
Liability (1)  
ProfitLoss (2)  
  
Responses for this string/value pair for Market Participants are almost exclusively Asset.  
feeGroupID | **integer.** Defines account attributes relating to how fees are calculated and assessed. Set by trading venue operator.  
parentID | **integer.** Reserved for future development.  
riskType | **integer.** One of:  
Unkown (0) (an error condition)  
Normal (1)  
NoRiskCheck (2)  
NoTrading (3)  
  
Returns Normal for virtually all market participants. Other types indicate account configurations assignable by the trading venue operator.  
verificationLevel | **integer.** Verification level limits the amounts of deposits and withdrawals. It is defined by and set by the trading venue operator for each account and is part of the KYC ("Know Your Customer") process, which may be automated or manual. An account can earn a higher Verification Level over time.  
feeProductType | **string.** One of:  
BaseProduct  
SingleProduct  
  
Trading fees may be charged by a trading venue operator. (Withdrawal fees may also be charged, but that is a separate setting dependent on product and instrument.) This value shows whether fees for this accountâs trades are charged in the product being traded (BaseProduct, for example BitCoin) or whether the account has a preferred fee-paying product (SingleProduct, for example USD) to use in all cases and regardless of product being traded.  
feeProduct | **integer.** The ID of the preferred fee product, if any. Defaults to 0.  
refererId | **integer.** Captures the ID of the entity who referred this account to the trading venue, usually captured for marketing purposes.  
loyaltyProductId | **integer.** The Loyalty Token is a parallel fee structure that replaces the general set of transaction fees. An exchange can promote activity on a specific cryptocurrency token by offering discounted transaction fees denominated in that token to customers who choose that fee structure. This key is the ID of the loyalty product chosen by the Exchange. There can be one Loyalty Token per OMS.  
loyaltyEnabled | **Boolean.** If _true_ , this account has accepted the Loyalty Token fee structure. If _false_ , the account has not accepted it. The default setting is _false_.  
marginEnabled | **Boolean.** If _true_ , this account can trade on margin. If _false_ , the account cannot trade on margin. The default is _false._  
liabilityAccountId | **integer.** The ID of the liability account associated with the account named in the _accountId_ key. A liability account is necessary for this account to trade on margin. Used internally.  
lendingAccountId | **integer.** The ID of the lending account associated with the account named in the _accountId_ key. A lending account is necessary for this account to trade on margin. Used internally.  
profitLossAccountId | **integer.** The ID of the profit-and-loss account associated with the account named in the _accountId_ key. A profit-and-loss account is necessary for this account to trade on margin. Used internally.  
|   
  
## GetAccountPositions

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Retrieves a list of positions (balances) for a specific user account running under a specific Order Management System. The trading day runs from UTC Midnight to UTC Midnight.

Users with Trading or AccountReadOnly permission must specify an account ID with which they're associated on the Order Management System. Users with Operator permission can specify other accounts.

### Request
    
    
    {
    Â â¯"AccountId":4,
    Â â¯"OMSId": 1
    }
    

Key | Value  
---|---  
AccountId | **integer.** The ID of the authenticated userâs account on the Order Management System for which positions will be returned.  
OMSId | **integer.** The ID of the Order Management System to which the user belongs. A user will belong only to one OMS.  
  
### Response
    
    
    [
        {
            "omsId":1,
            "accountId":4,
            "productSymbol":"BTC",
            "productId":1,
            "amount":0.0,
            "hold":0.0,
            "pendingDeposits":0.0,
            "pendingWithdraws":0.0,
            "totalDayDeposits":0.0,
            "totalMonthDeposits":0.0,
            "totalYearDeposits":0.0,
            "totalYearDepositNotional":0.0,
            "totalDayWithdraws":0.0,
            "totalMonthWithdraws":0.0,
            "totalYearWithdraws":0.0,
            "totalYearWithdrawNotional":0.0
        },
        {
            "omsId":1,
            "accountId":4,
            "productSymbol":"USD",
            "productId":2,
            "amount":0.0,
            "hold":0.0,
            "pendingDeposits":0.0,
            "pendingWithdraws":0.0,
            "totalDayDeposits":0.0,
            "totalMonthDeposits":0.0,
            "totalYearDeposits":0.0,
            "totalYearDepositNotional":0.0,
            "totalDayWithdraws":0.0,
            "totalMonthWithdraws":0.0,
            "totalYearWithdraws":0.0,
            "totalYearWithdrawNotional":0.0
        }
    ]
    

The response returns an array of one or more positions for the account. This example response has returned two positions.

Key | Value  
---|---  
omsId | **Integer.** The ID of the Order Management System (OMS) to which the user belongs. A user will only ever belong to one Order Management System. Note the change in capitalization from the request.  
accountId | **integer.** Returns the ID of the userâs account to which the positions belong. Note the change in capitalization from the request.  
productSymbol | **string.** The symbol of the product on this accountâs side of the trade. For example:  
BTC â BitCoin  
USD â US Dollar  
NZD â New Zealand Dollar   
  
Many other values are possible depending on the nature of the trading venue.  
productId | **integer.** The ID of the product being traded. The system assigns product IDs as they are entered into the system. Use **GetProduct** to return information about the product by its ID.  
amount | **real.** Unit amount of the product; for example, 10 or 138.5.  
hold | **real.** Amount of currency held and not available for trade. A pending trade of 100 units at $1 each will reduce the amount in the account available for trading by $100 and produce a $100 hold. Amounts on hold cannot be withdrawn while a trade is pending.  
pendingDeposits | **real.** Deposits accepted but not yet cleared for trade.  
pendingWithdraws | **real.** Withdrawals acknowledged but not yet cleared from the account. Amounts in _PendingWithdraws_ are not available for trade.  
totalDayDeposits | **real.** Total deposits on todayâs date. The trading day runs between UTC Midnight and UTC Midnight.  
totalMonthDeposits | **real.** Total deposits for the month as of today's date.  
totalYearDeposits | **real.** Total deposits for the year as of today's date.  
totalYearDepositNotional | **real.** Yearly amount for deposit of crypto-currencies. It is usually calculated as  
value = (Amount * Bid/Ask Price). 10 BitCoin each at $6700 equals $67000.  
totalDayWithdraws | **real.** Total withdrawals on todayâs date. The trading day runs between UTC Midnight and UTC Midnight.  
totalMonthWithdraws | **real.** Total withdrawals during this month to date. The trading day runs between UTC Midnight and UTC Midnight â likewise a month begins at UTC Midnight on the first day of the month.  
totalYearWithdraws | **real.** Total withdrawals during the current year to date.  
totalYearWithdrawNotional | **real.** Yearly withdrawals for crypto-currencies. It is usually calculated as  
value = (Amount * Bid/Ask Price). 10 BitCoin each at $6700 equals $67000.  
  
## GetTreasuryProductsForAccount

**Category:** User  
**Permissions:** Operator, Trading, Withdraw, Deposit  
**Call Type:** Synchronous

Returns a list of product symbols (BTC, USD, etc.) upon which the account named by AccountId is allowed to execute treasury operations.

Users with Trading, Withdraw, and Deposit permission must be associated with the account named by AccountId. Users with Operator permission can request the list of treasury products for any account.

### Request
    
    
    {
        "AccountId": 1,
        "OMSId": 1
    }
    

Key | Value  
---|---  
AccountId | **integer.** The ID of the account whose permitted treasury products will be returned.  
OMSId | **integer.** The ID of the Order Management System where the account operates.  
  
### Response

> An array of code symbol lists.
    
    
    [ { "LTC", "BTC", "USD" }, ]
    

The response returns an array of code symbol lists.

## ScheduleTradeActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Schedules a series of trade activity reports to run for a list of accounts on a single Order Management System, starting at a specific date/time, and covering a specific time duration. The reports will run periodically until canceled.

Users with Trading permission can schedule reports for accounts with which they are associated; users with Operator permissions can schedule reports for any accounts.

Trade Activity Reports are delivered in comma-separated-value (CSV) format. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
      "frequency": {
             "Options": [
                "OnDemand", // 0 
                "Hourly", // 1
                "Daily", // 2
                "Weekly", // 3
                "Monthly", // 4
                "Annual" // 5
            ] 
        },
      "accountIdList":[1],
      "omsId":1,
      "beginTime":"2018-08-10T04:00:00.000Z",
      "intervalDuration":10
    }
    

Key | Value  
---|---  
frequency | **integer.** How often the report will run. One of:  
0 OnDemand  
1 Hourly  
2 Daily  
3 Weekly  
4 Monthly  
5 Annually  
accountIdList | **integer array.** Comma-separated integers; each element an account ID on the Order Management System whose trade activity will be reported on. All accounts must be from the same OMS.  
omsId | **integer.** The ID of the Order Management System on which the accounts named in the list reside.  
beginTime | **string.** The time at which the periodic reports begin; the day and time when you want reporting to start, in Microsoft Ticks format.  
intervalDuration | **integer.** The length of time prior to the run time that the report covers, in days. For example, 90 for 90 days. Whatever the report's frequency, it looks back 90 days. A monthly report, for example, would look back 90 days; an annual report would look back 90 days.  
  
### Response
    
    
    {
        "RequestingUser":1,
        "OMSId":1,
        "reportFlavor": { // enumerated string
             "Options": [
                "TradeActivity",
                "Transaction",
                "Treasury"
            ] 
        },
        "createTime":"2018-08-17T17:57:51Z",
        "initialRunTime":"2018-08-10T04:00:00Z",
        "intervalStartTime":"2018-08-10T04:00:00Z",
        "intervalEndTime":"2018-08-10T05:00:00Z",
        "RequestStatus": { // enumerated string
             "Options": [
                "Submitted",
                "Validating",
                "Scheduled",
                "InProgress",
                "Completed",
                "Aborting",
                "Aborted",
                "UserCancelled",
                "SysRetired",
                "UserCancelledPending"
            ] 
        },
        "ReportFrequency": { // enumerated string
             "Options": [
                "onDemand",
                "Hourly",
                "Daily",
                "Weekly",
                "Monthly",
                "Annually"
            ] 
        },
        "intervalDuration":36000000000,
        "RequestId":"mGzjUfylGEmqgJIxu651aQ==",
        "lastInstanceId":"AAAAAAAAAAAAAAAAAAAAAA==",
        "accountIds":[1]
    }
    
    

The response returns an object confirming the settings in the call.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the trade activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the trade activity report will be run.  
reportFlavor | **enumerated string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the trade activity report was made, in Microsoft Ticks format.  
initialRunTime | **string.** The time and date at which the trade activity report was first run, in Microsoft Ticks format.  
intervalStartTime | **string.** The start of the period that the report will cover, in Microsoft Ticks format.  
intervalEndTime | **string.** The end of the period that the report will cover, in Microsoft Ticks format.  
RequestStatus | **enumerated string.** The status of the request for the trade activity report. Each request returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelledPending  
ReportFrequency | **enumerated string.** When the report runs:  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date, in POSIX format. The call specifies a start time and an _intervalDuration_.  
  
For example, say that you schedule a weekly report with a 90-day _intervalDuration_ value. _intervalDuration_ represents the backward-looking period of the report. When the report runs again in a weekâs time, it again looks back 90 days â but now those 90 days are offset by a week from the first report.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## ScheduleTransactionActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Schedules a series of transaction activity reports for a list of accounts on a single Order Management System, starting at a specific date/time, and covering a specific time interval (90 days, for example). The reports run periodically until canceled.

Users with Trading permission can schedule transaction activity reports only for accounts with which they are associated; users with Operator permission can schedule transaction activity reports for any account.

Transaction Activity Reports are delivered in comma-separated-value (CSV) format. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
      "frequency": 0,
      "accountIdList": [1],
      "omsId": 1,
      "beginTime": "2018-08-10T04:00:00.000Z",
      "intervalDuration": 10
    }
    

Key | Value  
---|---  
frequency | **integer:** How often the report will run. Expressed as an integer that maps to this list:  
**0** OnDemand  
**1** Hourly  
**2** Daily  
**3** Weekly  
**4** Monthly  
**5** Annually  
accountIdList | **integer array.** Comma-separated integers; each element is an account ID whose transaction activity will be reported on. All accounts must be from the same OMS.  
omsId | **integer.** The Order Management System on which the accounts named in the list reside.  
beginTime | **string.** The time from which the transaction activities will be reported, in Microsoft Ticks format.  
intervalDuration | **integer.** The length of time prior to the run time that the report covers, in days. For example, 90 means 90 days. Whenever the report runs, it looks back 90 days.  
  
### Response
    
    
    {
        "RequestingUser": 1,
        "OMSId": 1,
        "reportFlavor": "Transaction",
        "createTime": "2018-08-17T18:02:23Z",
        "initialRunTime": "2018-08-10T04:00:00Z",
        "intervalStartTime": "2018-08-10T04:00:00Z",
        "intervalEndTime": "2018-08-10T05:00:00Z",
        "RequestStatus": "Submitted",
        "ReportFrequency": "Hourly",
        "intervalDuration": 36000000000,
        "RequestId": "I2nCtvyY8UuHsoSyrLe2QA==",
        "lastInstanceId": "AAAAAAAAAAAAAAAAAAAAAA==",
        "accountIds": [1]
    }
    

Similar objects are returned for **Generate~Report** and **Schedule~Report** calls.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the transaction activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the transaction activity report will be run.  
reportFlavor | **string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the transaction activity report was made, in Microsoft Ticks format.  
initialRunTime | **string.** The time and date at which the transaction activity report was first run, in Microsoft Ticks format.  
intervalStartTime | **string.** The start of the period that the report will cover, in Microsoft Ticks format.  
intervalEndTime | **string.** The end of the period that the report will cover, in Microsoft Ticks format.  
requestStatus | **string.** The status of the request for the transaction activity report. Each request returns one of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelledPending  
ReportFrequency | **string.** When the report runs:  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date, in POSIX format. For example, say that you schedule a weekly report with a 90-day _intervalDuration_ value. _intervalDuration_ represents the backward-looking period of the report. When the report runs again in a weekâs time, it again looks back 90 days â but now those 90 days are offset by a week from the first report.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
## ScheduleTreasuryActivityReport

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Schedules a series of treasury activity reports for a list of accounts on a single Order Management System, starting at a specific date/time, and covering a specific time interval. Treasury activities are non-trading transactions such as deposits and withdrawals. The reports runs periodically until canceled.

A user with Trading permission may schedule reports only for accounts with which he is associated; a user with Operator permission may schedule reports for any accounts.

The Treasury Activity Report itself is delivered as a comma-separated-value (CSV) file. For specific CSV formatting information, see the APEX Extract CSV Data Dictionary, available from AlphaPoint.

### Request
    
    
    {
      "frequency":0,
      "accountIdList":[1],
      "omsId":1,
      "beginTime":"2018-08-10T04:00:00.000Z",
      "intervalDuration":10
     }
    
    

Key | Value  
---|---  
frequency | **integer.** How often the report will run. A number represents one of:  
0 OnDemand  
1 Hourly  
2 Daily  
3 Weekly  
4 Monthly  
5 Annually  
accountIdList | **integer array.** Comma-separated integers; each element is an account ID whose treasury activity will be reported on. All accounts must be from the same OMS.  
omsId | **integer.** The Order Management System on which the accounts named in the list reside.  
beginTime | **string.** The time from which the treasury activities will be reported, in Microsoft Ticks format.  
intervalDuration | **integer.** The length of time prior to the run time that the report covers. For example, 90 days. Whenever the report runs, it looks back 90 days.  
  
### Response
    
    
    {
      "RequestingUser":1,
      "OMSId":1,
      "reportFlavor":"Treasury",
      "createTime":"2018-08-17T18:02:03Z",
      "initialRunTime":"2018-08-10T04:00:00Z",
      "intervalStartTime":"2018-08-10T04:00:00Z",
      "intervalEndTime":"2018-08-10T05:00:00Z",
      "RequestStatus":"Submitted",
      "ReportFrequency":"Hourly",
      "intervalDuration":36000000000,
      "RequestId":"xbsVgAuUcEyTFgf/gpWB2A==",
      "lastInstanceId":"AAAAAAAAAAAAAAAAAAAAAA==",
      "accountIds":[1]
    }
    

Similar objects are returned for **Generate~Report** and **Schedule~Report** calls.

Key | Value  
---|---  
RequestingUser | **integer.** The User ID of the person requesting the treasury activity report. This confirms the ID of the authenticated user who made the request by returning it as part of the response.  
OMSId | **integer.** The ID of the Order Management System on which the treasury activity report will be run.  
reportFlavor | **string.** The type of report to be generated. One of:  
TradeActivity  
Transaction  
Treasury  
  
The _reportFlavor_ string confirms the nature of the call.  
createTime | **string.** The time and date on which the request for the treasury activity report was made, in Microsoft Ticks format.  
initialRunTime | **string.** The time and date at which the treasury activity report was first run, in Microsoft Ticks format.  
intervalStartTime | **string.** The start of the period that the report will cover, in Microsoft Ticks format.  
intervalEndTime | **string.** The end of the period that the report will cover, in Microsoft Ticks format.  
requestStatus | **string.** The status of the request for the treasury activity report. One of:  
Submitted  
Validating  
Scheduled  
InProgress  
Completed  
Aborting  
Aborted  
UserCancelled  
SysRetired  
UserCancelledPending  
ReportFrequency | **string.** When the report runs. Note that _frequency_ in the request is an integer; but _ReportFrequency_ in the response is a string.  
OnDemand  
Hourly  
Daily  
Weekly  
Monthly  
Annually  
intervalDuration | **long integer.** The period that the report covers relative to the run date, in POSIX format.  
  
For example, say that you schedule a weekly report with a 90-day _intervalDuration_ value. _intervalDuration_ represents the backward-looking period of the report. When the report runs again in a weekâs time, it again looks back 90 days â but now those 90 days are offset by a week from the first report.  
RequestId | **string.** The ID of the original request. Request IDs are long strings unique within the Order Management System.  
lastInstanceId | **string.** For scheduled reports, the report ID of the most recent previously run report.  
accountIds | **integer array.** A comma-delimited array of account IDs whose trades are reported in the trade activity report.  
  
# Trades

These calls correspond roughly to the Trades function of the Exchange Admin and Admin Guide.

## GetAccountTrades

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Requests the details on up to 200 past trade executions for a single specific account and Order Management System, starting at index _i_ , where _i_ is an integer identifying a specific execution in reverse order; that is, the most recent execution has an index of 0, and increments by one as trade executions recede into the past.

Users with Trading or AccountReadOnly permission may access trade information only for accounts with which they are associated; users with Operator permission may access trade information for any account.

The operator of the trading venue determines how long to retain an accessible trading history before archiving.

### Request
    
    
    {
        "OMSId": 0,
        "AccountId":0,
        "StartIndex":0,
        "Count":0
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System to which the user belongs. A user will belong to only one OMS.  
AccountId | **integer.** The ID of the account.  
StartIndex | **integer.** The starting index into the history of trades, beginning from 0 (the most recent trade).  
Count | **integer.** The number of trades to return. The system can return up to 200 trades.  
  
### Response
    
    
    [
        {
            "omsId": 0,
            "executionId": 0,
            "tradeId": 0,
            "orderId": 0,
            "accountId": 0,
            "subAccountId": 0,
            "clientOrderId": 0,
            "instrumentId": 0,
            "side": 0,
            "quantity": 0.0,
            "remainingQuantity": 0.0,
            "price": 0.0,
            "value": 0.0,
            "tradeTime": 0,
            "counterParty": null,
            "orderTradeRevision": 0,
            "direction": 0,
            "isBlockTrade": false,
            "tradeTimeMS": 0,
            "fee": 0.0,
            "feeProductId": 0,
            "orderOriginator": 0
        },
    ]
    

The response is an array of objects, each of which represents the accountâs side of a trade (either buy or sell).

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System to which the account belongs.  
executionId | **integer.** The ID of this account's side of the trade. Every trade has two sides.  
tradeId | **integer.** The ID of the overall trade.  
orderId | **long integer.** The ID of the order causing the trade (buy or sell).  
accountId | **integer.** The ID of the account that made the trade (buy or sell).  
subAccountId | **integer.** Not currently used; reserved for future use. Defaults to 0.  
clientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _clientOrderId_ defaults to 0 if not supplied.  
instrumentId | **integer.** The ID of the instrument being traded. An instrument comprises two products, for example Dollars and BitCoin.  
side | **integer.** A number representing one of the following potential sides of a trade:   
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
quantity | **real.** The unit quantity of this side of the trade.  
remainingQuantity | **real.** The number of units remaining to be traded by the order after this execution. This number is not revealed to the other party in the trade. This value is also known as "leave size" or "leave quantity."  
price | **real.** The unit price at which the instrument traded.  
value | **real.** The total value of the deal. The system calculates this as:  
unit price X quantity executed.  
tradeTime | **long integer.** The date and time stamp of the trade, in POSIX format.  
counterParty | **string.** The ID of the other party in a block trade. Usually, IDs are stated as integers; this value is an integer written as a string.  
orderTradeRevision | **integer.** The revision number of this trade; usually 1.  
direction | **integer.** The effect of the trade on the instrument's market price. One of:  
**0** No change  
**1** Uptick  
**2** DownTick  
isBlockTrade | **Boolean.** A value of _true_ means that this trade was a block trade; a value of _false_ that it was not a block trade.  
tradeTimeMS | **long integer.** The date and time that the trade took place, in milliseconds and POSIX format. All dates and times are UTC.  
fee | **real.** Any fee levied against the trade by the Exchange.  
feeProductId | **integer.** The ID of the product in which the fee was levied.  
orderOriginator | **integer.** The ID of the user who initiated the trade.  
  
## GetAccountTransactions

**Category:** User  
**Permissions:** Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns a list of transactions for a specific account on an Order Management System. The owner of the trading venue determines how long to retain order history before archiving. The caller must be associated with the account named in _AccountId_.

**Note:** In this call, âDepthâ refers not to the depth of the order book, but to the count of trades to report.

### Request
    
    
    {
      "OMSId": 1,
      "AccountId": 1,
      "Depth": 200
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System from which the accountâs transactions will be returned.  
AccountId | **integer.** The ID of the account for which transactions will be returned. If not specified, the call returns transactions for the default account for the logged-in user.  
Depth | **integer.** The number of transactions that will be returned, starting with the most recent transaction.  
  
### Response
    
    
    [
      {
        "transactionId":0,
        "omsId":0,
        "accountId":0,
        "cr":0.0,
        "dr":0.0,
        "counterparty":0,
        "transactionType":0,
        "referenceId":0,
        "referenceType":0,
        "productId":0,
        "balance":0.0,
        "timeStamp":0
        },
    ]
    

The response returns an array of transaction objects. Note capitalization changes from the request.

Key | Value  
---|---  
transactionId | **Integer.** The ID of the transaction.  
omsId | **Integer.** The ID of the Order Management System under which the requested transactions took place.  
accountId | **Integer.** The single account under which the transactions took place.  
cr | **real.** Credit entry for the account on the order book. Funds entering an account.  
dr | **real.** Debit entry for the account on the order book. Funds leaving an account.  
counterparty | **long integer.** The corresponding party in a trade.  
transactionType | **integer.** A number representing the type of transaction:  
1 Fee  
2 Trade  
3 Other  
4 Reverse  
5 Hold  
6 Rebate  
7 MarginAcquisition  
8 MarginRelinquish  
referenceId | **long integer.** The ID of the action or event that triggered this transaction.  
referenceType | **integer.** A number representing the type of action or event that triggered this transaction. One of:  
1 Trade  
2 Deposit  
3 Withdraw  
4 Transfer  
5 OrderHold  
6 WithdrawHold  
7 DepositHold  
8 MarginHold  
9 ManualHold  
10 ManualEntry  
11 MarginAcquisition  
12 MarginRelinquish  
13 MarginQuoteHold  
productId | **integer.** The ID of the product on this accountâs side of the transaction. For example, in a dollars-for-BitCoin transaction, one side will have the product Dollar and the other side will have the product BitCoin. Use **GetProduct** to return information about a product based on its ID.  
balance | **real.** The balance in the account after the transaction.  
timeStamp | **long integer.** Time at which the transaction took place, in POSIX format.  
  
## GetOpenTradeReports

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Retrieves an array of open trade information for the account named in _AccountId_. 

Users with Trading or AccountReadOnly permission must be associated with the named account; users with Operator permission can retrieve open trade reports on any account.

### Request
    
    
    { 
      "OMSId": 1,
      "AccountId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the account operates.  
AccountId | **integer.** The ID of the account whose open trade information will be returned.  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOpenTradeReports** returns an array containing all four types of orders for the named account. The call returns an empty array if there are no open trades for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format.  
ReceiveTimeTicks | **long integer.** Time stamp of the order in POSIX format.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## GetTickerHistory

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Requests a ticker history (high, low, open, close, volume, bid, ask, ID) of a specific instrument from a given date to the present. You will need to format the returned data per your requirements.

Because permission is Public, any user can retrieve the ticker history for any instrument on the OMS.

### Request
    
    
    {
        "InstrumentId": 1,
        "Interval": 60,
        "FromDate": "2018-07-18",
        "ToDate": "2018-07-19",
        "OMSId":1
    }
    

Key | Value  
---|---  
InstrumentId | **integer.** The ID of a specific instrument. The current Order Management System is assumed.  
Interval | **integer.** The time between ticks, in seconds. For example, a value of 60 returns ticker array elements between _FromDate_ to _ToDate_ in 60-second increments.  
FromDate | **string.** Oldest date from which the ticker history will start, in Micrisoft Ticks format. The report moves toward _ToDate_ from this point.  
ToDate | **string.** Most recent date, at which the ticker history will end, in Microsoft Ticks format.  
OMSId | **integer.** The ID of the Order Management System where the ticker history comes from.  
  
### Response

> The response is an array of arrays of comma-separated, but unlabeled, numbers. This sample shows comments applied to identify the data being returned (comments are not part of the response; the second array shows how the data actually is reported):
    
    
    [
      [
        1501603632000, \\DateTime - UTC - Milliseconds since 1/1/1970 - POSIX format
        2700.33, \\High
        2687.01, \\Low
        2687.01, \\Open
        2687.01, \\Close
        24.86100992,  \\Volume
        0,  \\Inside Bid Price
        2870.95,  \\Inside Ask Price
        1 \\InstrumentId
      ],
      [1501604532000,2792.73,2667.95,2687.01,2700.81,242.61340767,0,2871,0],
    ]
    

The response returns an array of arrays dating from the _FromDate_ value of the request to the _ToDate_. The data are returned oldest-date first. The data returned in the arrays are not labeled.

## GetTradesHistory

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Retrieves a list of trades for a specified account, order ID, user, instrument, or starting and ending time stamp. The returned list begins at start index _i,_ where _i_ is an integer identifying a specific trade in reverse order; that is, the most recent trade has an index of 0. âDepthâ is the count of trades to report backwards from _StartIndex_. 

Users with Trading permission can retrieve trade history for accounts with which they are associated; users with Operator permission can retrieve trade history for any account.

**Caution** : You must coordinate *StartIndex*, *Depth*, *StartTimeStamp*, and *EndTimeStamp* to retrieve the historical information you need. As the diagram shows, it is possible to specify values (for example, *EndTimeStamp* and *Depth*) that can exclude information you may want (the red areas). **Note** : In this call, âDepthâ refers not to the depth of the order book, but to the count of trades to report. The owner of the trading venue determines how long to retain order history before archiving.

### Request

> All values in the request other than omsId are optional. 
    
    
    {
        "omsId": 0,
        "accountId": 0,
        "instrumentId": 0,
        "tradeId": 0,
        "orderId": 0,
        "userId": 0,
        "startTimestamp": 0,
        "endTimestamp": 0,
        "depth": 100,
        "startIndex": 0,
        "executionId": 0
    }
    

Key | Value  
---|---  
omsId | **Integer.** The ID of the Order Management System on which the trades took place. If no other values are specified, **GetTradesHistory** returns the trades associated with the default account for the logged-in user on this Order Management System. _Required key and value._  
accountId | **Integer.** The account ID that made the trades. If no account ID is supplied, the system assumes the default account for the logged-in user making the call.  
instrumentId | **long integer.** The ID of the instrument whose trade history is reported. If no instrument ID is included, the system returns trades for all instruments associated with the account ID and OMS.  
tradeId | **integer.** The ID of a specific trade. If you specify _TradeId_ , **GetTradesHistory** can return all states for a single trade.  
orderId | **integer.** The ID of the order resulting in the trade. If specified, the call returns all trades associated with the order.  
userId | **integer.** The ID of the logged-in user. If not specified, the call returns trades associated with the users belonging to the default account for the logged-in user of this OMS.  
startTimeStamp | **long integer.** The historical date and time at which to begin the trade report, in POSIX format. If not specified, reverts to the start date of this account on the trading venue.  
endTimeStamp | **long integer.** Date at which to end the trade report, in POSIX format.  
depth | **integer.** In this case, the count of trades to return, counting from the _StartIndex_. If _Depth_ is not specified, returns all trades between _BeginTimeStamp_ and _EndTimeStamp_ , beginning at _StartIndex_.  
startIndex | **integer.** The starting index into the history of trades, from 0 (the most recent trade) and moving backwards in time. If not specified, defaults to 0.  
executionId | **integer.** The ID of the individual buy or sell execution. If not specified, returns all.  
  
### Response
    
    
    [
        {
            "omsId": 0,
            "executionId": 0,
            "tradeId": 0,
            "orderId": 0,
            "accountId": 0,
            "subAccountId": 0,
            "clientOrderId": 0,
            "instrumentId": 0,
            "side": 0,
            "quantity": 0.0,
            "remainingQuantity": 0.0,
            "price": 0.0,
            "value": 0.0,
            "tradeTime": 0,
            "counterParty": null,
            "orderTradeRevision": 0,
            "direction": 0,
            "isBlockTrade": false,
            "tradeTimeMS": 0,
            "fee": 0.0,
            "feeProductId": 0,
            "orderOriginator": 0
        },
    ]
    

The response is an array of objects, each element of which represents the accountâs side of a trade (either buy or sell).

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System to which the account belongs.  
executionId | **integer.** The ID of this account's side of the trade. Every trade has two sides.  
tradeId | **integer.** The ID of the overall trade.  
orderId | **long integer.** The ID of the order causing the trade (buy or sell).  
accountId | **integer.** The ID of the account that made the trade (buy or sell).  
subAccountId | **integer.** Not currently used; reserved for future use. Defaults to 0.  
clientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _clientOrderId_ defaults to 0 if not supplied.  
instrumentId | **integer.** The ID of the instrument being traded. An instrument comprises two products, for example Dollars and BitCoin.  
side | **integer.** A number representing one of the following potential sides of a trade:   
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
quantity | **real.** The unit quantity of this side of the trade.  
remainingQuantity | **real.** The number of units remaining to be traded by the order after this execution. This number is not revealed to the other party in the trade. This value is also known as "leave size" or "leave quantity."  
price | **real.** The unit price at which the instrument traded.  
value | **real.** The total value of the deal. The system calculates this as:  
unit price X quantity executed.  
tradeTime | **long integer.** The date and time stamp of the trade, in POSIX format.  
counterParty | **string.** The ID of the other party in a block trade. Usually, IDs are stated as integers; this value is an integer written as a string.  
orderTradeRevision | **integer.** The revision number of this trade; usually 1.  
direction | **integer.** The effect of the trade on the instrument's market price. One of:  
**0** No change  
**1** Uptick  
**2** DownTick  
isBlockTrade | **Boolean.** A value of _true_ means that this trade was a block trade; a value of _false_ that it was not a block trade.  
tradeTimeMS | **long integer.** The date and time that the trade took place, in milliseconds and POSIX format. All dates and times are UTC.  
fee | **real.** Any fee levied against the trade by the Exchange.  
feeProductId | **integer.** The ID of the product in which the fee was levied.  
orderOriginator | **integer.** The ID of the user who initiated the trade.  
  
## Trades

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

The trades endpoint is to return data on all recently completed trades for a given market pair.

### Request
    
    
    {
        "Code": "BTCCAD"
    }
    

Key | Value  
---|---  
market_pair | **string** A pair such as BTCCAD.  
  
### Response
    
    
    [
        {
            "trade_id": 500773,
            "price": 75381.58,
            "base_volume": 1.93203,
            "quote_volume": 145639.4740074,
            "timestamp": "2021-11-16T18:49:57.590Z",
            "type": "sell"
        },
    ]
    

The response returns an array of JSON objects with the following key/value pair 

Key | Value  
---|---  
trade_id | **integer** A unique ID associated with the trade for the currency pair transaction.  
price | **decimal** Last transacted price of base currency based on given quote currency.  
base_volume | **decimal** Transaction amount in BASE currency.  
quote_volume | **decimal** Transaction amount in QUOTE currency.  
timestamp | **integer** Unix timestamp in milliseconds for when the transaction occurred.  
type | **string** Used to determine whether or not the transaction originated as a buy or sell. Buy â Identifies an ask was removed from the order book. Sell â Identifies a bid was removed from the order book.   
  
# OMS Orders

These calls correspond roughly to the OMS Orders function of the Exchange Admin and Admin Guide.

## CancelAllOrders

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Cancels all open matching orders for the specified account on an Order Management System. 

A user with Trading permission can cancel orders for himselfd; a user with Operator permissions can cancel orders for any account, instrument, or user.

**Note:** Multiple users may have access to the same account.

### Request
    
    
    {
    Â â¯"AccountId": 0,
    Â â¯"OMSId": 0
    }
    

Key | Value  
---|---  
AccountId | **integer.** The account for which all orders are being canceled. _Conditionally optional._  
OMSId | **integer.** The Order Management System under which the account operates. _Required_.  
  
### Response
    
    
    {
        "result": true,
        "errormsg": "",
        "errorcode": 0,
        "detail": ""
    }
    

The Response is a standard response object.

Key | Value  
---|---  
result | **Boolean.** If the call has been successfully received by the Order Management System, _result_ is _true;_ otherwise it is _false._  
errormsg | **string.** A successful receipt of the call returns _null._ The _errormsg_ key for an unsuccessful call returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Response (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
errorcode | **integer.** A successful receipt of the call returns 0. An unsuccessful receipt of the call returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send.  
  
## CancelOrder

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Cancels an open order that has been placed but has not yet been fully executed. 

A user with Trading permission can cancel an order only for an account with which he is associated; a user with Operator permission can cancel an order for any account.

### Request
    
    
    {
    Â â¯"OMSId": 0,
    Â â¯"AccountId": 0,Â â¯// conditionally optional
    Â â¯"ClientOrderId": 0,Â â¯// conditionally optional
    Â â¯"OrderId": 0,Â â¯Â â¯// conditionally optional
    }
    

The OMS ID and the Order ID precisely identify the order you wish to cancel. The Order ID is unique across an OMS.

If you specify the OMS ID and the Account ID, you must also specify at least the Client Order ID. The OMS is unable to identify the order using only the OMS ID and the Client Order ID, as the Client Order ID may not be unique.

Key | Value  
---|---  
OMSId | **integer.** The Order Management System on which the order exists. _Required_.  
AccountId | **integer.** The ID of the account under which the order was placed. _Conditionally optional_.  
ClientOrderId | **long integer.** A user-assigned ID for the order (like a purchase-order number assigned by a company). _ClientOrderId_ defaults to 0. _Conditionally optional._  
OrderId | **long integer.** The order to be canceled. _Conditionally optional_.  
  
### Response
    
    
    {
    Â â¯"result": true,
    Â â¯"errormsg": "",
    Â â¯"errorcode": 0,
    Â â¯"detail": "",
    }
    

The response to **CancelOrder** verifies that the call was received, not that the order has been canceled successfully. Individual event updates to the user show order cancellation. To verify that an order has been canceled, call **GetOrderStatus** or **GetOpenOrders.**

Key | Value  
---|---  
result | **Boolean.** Returns _true_ if the call to cancel the order has been successfully received, otherwise returns _false_.  
errormsg | **string.** A successful receipt of a call to cancel an order returns _null_ ; the _errormsg_ parameter for an unsuccessful call to cancel an order returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
errorcode | **integer.** A successfully received call to cancel an order returns 0. An unsuccessfully received call to cancel an order returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. The contents of this parameter are usually null.  
  
## CancelQuote

**Category:** User  
**Permissions:** Operator, Marketmaker  
**Call Type:** Synchronous

Cancels a quote that has not been executed yet.

**Note:** Quoting is not enabled for the retail end user of the AlphaPoint software. Only registered market participants or marketmakers may quote. Only a user with Operator permission can cancel quotes for another user.

### Request
    
    
    {
        "omsId": 0,
        "accountId": 0,
        "instrumentId": 0,
        "bidQuoteId": 0,
        "askQuoteId": 0
    }
    

You must identify the quote to be canceled by both _BidQuoteId_ and _AskQuoteId_ , which were supplied by the system when the quote was created. You can optionally identify the canceled quote using _AccountId_ and _InstrumentId_. If the call does not include _AccountId_ , the call assumes the default _AccountId_ for the logged-in user; if the call does not include _InstrumentId_ , the call operates on any instruments quoted by the account.

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System where the quote was requested. Required.  
accountId | **integer.** The ID of the account that requested the quote. _Conditionally optional_.  
instrumentId | **long integer.** The ID of the instrument being quoted. _Conditionally optional_.  
bidQuoteId | **integer.** The ID of the bid quote. _Required_.  
askQuoteId | **integer.** The ID of the ask quote. _Required_.  
  
### Response
    
    
    {
    Â â¯"BidResult": "{
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯}",
    Â â¯"AskResult": "{
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯}"
    }
    

Returns two json objects, one for Bid and one for Ask.

The response to **CancelQuote** verifies that the call was received, not that the quote has been canceled successfully. Individual event updates to the user show quotes as they cancel. To verify that a quote has been canceled, use **GetOpenQuotes.**

Key | Value  
---|---  
BidResult | **object.** Returns a response object for Bid (see below).  
AskResult | **object.** Returns a response object for Ask.  
  
Objects for both _BidResult_ and _AskResult_ :

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the cancelation returns _true_ ; and unsuccessful receipt of the cancelation (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the cancelation returns _null_ ; the _errormsg_ parameter for an unsuccessful receipt returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
errorcode | **integer.** A successful receipt of the cancelation returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually null.  
  
## CancelReplaceOrder

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

**CancelReplaceOrder** is a single API call that both cancels an existing order and replaces it with a new order. Canceling one order and replacing it with another also cancels the orderâs priority in the order book. You can use **ModifyOrder** to preserve priority in the book; but **ModifyOrder** only allows a reduction in order quantity.

**Warning:** **CancelReplaceOrder** sacrifices the order's priority in the order book.

### Request
    
    
    {
        "omsId":0,
        "orderIdToReplace":0,
        "clientOrdId":0,
        "orderType":0,
        "side":0,
        "accountId":0,
        "instrumentId":0,
        "useDisplayQuantity":false,
        "displayQuantity":0.0,
        "limitPrice":0.0,
        "stopPrice":0.0,
        "referencePrice":0.0,
        "pegPriceType":0,
        "timeInForce":0,
        "orderIdOCO":0,
        "quantity":0.0
    }
    

Key | Value  
---|---  
omsId | **integer**. The ID of the Order Management System on which the order is being canceled and replaced by another order.  
orderIdToReplace | **long integer**. The ID of the order to replace with this order.  
clientOrderId | **long integer**. A user-assigned ID for the new, replacement order (like a purchase-order number assigned by a company). This ID is useful for recognizing future states related to this order. If unspecified, _ClientOrderId_ defaults to 0.  
orderType | **integer.** An integer representing the type of the replacement order:   
0 Unknown  
1 Market  
2 Limit  
3 StopMarket  
4 StopLimit  
5 TrailingStopMarket  
6 TrailingStopLimit  
7 BlockTrade  
side | **integer.** An integer representing the side of the replacement order:  
0 Buy  
1 Sell  
2 Short  
3 Unknown (error condition)  
accountId | **integer**. The ID of the account under which the original order was placed and the new order will be placed.  
instrumentId | **integer**. The ID of the instrument being traded.  
useDisplayQuantity | **Boolean.** The display quantity is the quantity of a product shown to the market to buy or sell. A larger quantity may be wanted or available, but it may disadvantageous to display it when buying or selling. The display quantity is set when placing an order (using **SendOrder** or **CancelReplaceOrder** for instance). If you enter a Limit order with reserve, you must set _useDisplayQuantity_ to _true_.  
displayQuantity | **real.** The quantity of a product that is available to buy or sell that is publicly displayed to the market.  
limitPrice | **real.** The price at which to execute the new order, if the new order is a limit order.  
stopPrice | **real.** The price at which to execute the new order, if the order is a stop order.  
referencePrice | **real.** The reference price of the instrument in the order.  
pegPriceType | **integer.** An integer that represents the type of price you set in a stop/trailing order to "peg the stop."  
0 Unknown (error condition)  
1 Last  
2 Bid  
3 Ask  
4 Midpoint  
timeInForce | **integer.** An integer that represents the period during which the new order is executable. One of:  
0 Unknown (error condition)  
1 GTC (good 'til canceled, the default)  
2 OPG (execute as close to opening price as possible)  
3 IOC (immediate or canceled)  
4 FOK (fill or kill — fill the order immediately, or cancel it immediately)  
5 GTX (good 'til executed)  
6 GTD (good 'til date)  
orderIdOCO | **integer.** One Cancels the Other â If the order being canceled in this call is order A, and the order replacing order A in this call is order B, then _OrderIdOCO_ refers to an order C that is currently open. If order C executes, then order B is canceled. You can also set up order C to watch order B in this way, but that will require an update to order C.  
quantity | **real.** The amount of the order (either buy or sell).  
  
### Response
    
    
    {
    Â â¯"replacementOrderId": 1234,
    Â â¯"replacementClOrdId": 1561,
    Â â¯"origOrderId": 5678,
    Â â¯"origClOrdId": 91011,
    }
    

The response returns the new replacement order ID and echoes back any replacement client ID you have supplied, along with the original order ID and the original client order ID.

Key | Value  
---|---  
replacementOrderId | **integer.** The order ID assigned to the replacement order by the server.  
replacementClOrdId | **long integer.** Echoes the contents of the _clientOrderId_ value from the request.  
origOrderId | **integer.** Echoes _orderIdToReplace_ , which is the original order you are replacing.  
origClOrdId | **long integer.** Provides the client order ID of the original order (not specified in the requesting call).  
  
## CreateQuote

**Category:** User  
**Permissions:** Operator, MarketMaker  
**Call Type:** Synchronous

**TK** call and response may change

Creates a quote. A quote expresses a willingness to buy or sell at a given price. Both a quote and an order will execute. Only a user with Operator or MarketMaker permission can create a quote.

**Note:** Quoting is not enabled for the retail end user of AlphaPoint software. Only registered market participants or market makers may quote.

### Request
    
    
    {
    Â â¯"OMSId": 0,
    Â â¯"AccountId": 0,
    Â â¯"InstrumentId": 0,
    Â â¯"Bid": 0,
    Â â¯"BidQty": 0,
    Â â¯"Ask": 0,
    Â â¯"AskQty": 0,
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the quote is being created. _Required_.  
AccountId | **integer.** The ID of the account in which the quote is being created. If the call provides no AccountId, the system assumes the default account ID for the logged-in user on the OMS.  
InstrumentId | **long integer.** The ID of the instrument being quoted. _Required_.  
Bid | **real.** The bid price. _Required_.  
BidQty | **real.** The quantity of the bid. _Required_.  
Ask | **real.** The ask price. _Required_.  
AskQty | **real.** The quantity of the ask. _Required_.  
  
### Response
    
    
    {
    Â â¯"BidResult": {
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯},
    Â â¯"AskResult": {
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯}
    }
    

Key | Value  
---|---  
BidResult | **object.** Returns a response object for Bid (see below).  
AskResult | **object.** Returns a response object for Ask.  
  
Objects for both _BidResult_ and _AskResult_ :

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the cancelation returns _true_ ; and unsuccessful receipt of the cancelation (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the cancelation returns _null_ ; the _errormsg_ parameter for an unsuccessful receipt returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
errorcode | **integer.** A successful receipt of the cancelation returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually null.  
  
## GetOpenOrders

**Category:** User  
**Permissions:** Operator, Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns an array of 0 or more orders that have not yet been filled (open orders) for a single account on a specific Order Management System. The call returns an empty array if an account has no open orders.

A user with Trading or AccountReadOnly permission must be associated with the account named by AccountId; a user with Operator permissoin can get open orders for any account.

### Request
    
    
    {
      "OMSId": 1
      "AccountId":4,
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System to which the user belongs. A user will belong only to one OMS.  
AccountId | **integer.** The ID of the authenticated userâs account.  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOpenOrders** returns an array containing both buy-side and a sell-side open orders for the named account. The call returns an empty array if there are no open orders for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format x 1000 (milliseconds since 1/1/1970 in UTC time zone).  
ReceiveTimeTicks | **long integer.** Time stamp of the order Microsoft Ticks format and UTC time zone. **Note:** Microsoft Ticks format is usually provided as a string. Here it is provided as a long integer.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## GetOpenQuotes

**Category:** User  
**Permissions:** Operator, MarketMaker  
**Call Type:** Synchronous

Returns the current bid and ask quotes for a given instrument ID and account ID.

### Request
    
    
    {
    Â â¯"omsId": 0,
    Â â¯"accountId": 0,
    Â â¯"instrumentId": 0,
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System where the instrument is traded whose quote may be open.  
AccountId | **integer**. The ID of the account whose open quotes will be returned.  
InstrumentId | **integer**. The ID of the instrument being quoted.  
  
### Response
    
    
    {
        "bid": {
            "omsId": 0,
            "side": 0,
            "orderId": 0,
            "price": 0.0,
            "quantity": 0.0,
            "displayQuantity": 0.0,
            "instrument": 0,
            "account": 0,
            "orderType": 0,
            "clientOrderId": 0,
            "orderState": 0
        },
        "ask": {
            "omsId": 0,
            "side": 0,
            "orderId": 0,
            "price": 0.0,
            "quantity": 0.0,
            "displayQuantity": 0.0,
            "instrument": 0,
            "account": 0,
            "orderType": 0,
            "clientOrderId": 0,
            "orderState": 0
        }
    }
    

Returns a JSON object comprising a bid and an ask object. Both object comprise the same key-value pairs.

Key | Value  
---|---  
bid | Bid object (see below)  
ask | Ask object (see below)  
  
Bid and Ask objects differ only in the values for the keys.

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System containing the open quotes.  
side | **integer.** One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (error condition)  
orderId | **long integer.** The ID of this quote. Quotes and orders are both executable, but only Operators and MarketMakers may quote.  
price | **real.** Price of the Bid/Ask quote.  
quantity | **real.** Quantity of the Bid/Ask quote.  
displayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _DisplayQuantity_ value, an order must be a Limit order with a reserve.  
instrument | **integer.** The ID of the instrument being quoted.  
account | **integer.** The ID of the account quoting the instrument.  
orderType | **integer.** A number describing the type of order (or in this case, quote). One of:  
**0** Unknown  
**1** Market  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
cientOrderId | **long integer.** A user-assigned ID for the quote (like a purchase-order number assigned by a company). _ClientOrderId_ defaults to 0.  
orderState | **integer.** A number describing the current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** FullyExecuted  
  
An open quote will probably have an _OrderState_ of Working.  
  
## GetOrderFee

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an estimate of the transaction fee for a specific order side, instrument, and order type. Fees are set and calculated by the operator of the trading venue.

The exchange generally deducts fees from the "receiving" side of the trade (although an operator can modify this). There are two products in every trade (and in every instrument); for example, the instrument BTCUSD comprises a BitCoin product and a US dollar product. Placing a buy order on the book causes fees to be deducted from Product 1, in this case, BitCoin; placing a sell order causes fees to be deducted from Product 2, in this case, US dollar.

A user with Trading permission can get fee estimates for any account that user is associated with and for any instrument or product that that account can trade; a user with Operator permission can get fee estimates for any account, instrument, or product.

### Request
    
    
    {
        "omsId":0,
        "accountId":0,
        "instrumentId":0,
        "productId":0,
        "amount":0.0,
        "price":0.0,
        "orderType":0,
        "makerTaker":0,
        "side":0
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the trade would take place.  
accountId | **integer.** The ID of the account requesting the fee estimate.  
instrumentId | **integer.** The proposed instrument against which a trading fee would be charged.  
productId | **integer.** The ID of the product (currency) in which the fee will be denominated.  
amount | **real.** The quantity of the proposed trade for which the Order Management System would charge a fee.  
price | **real.** The price at which the proposed trade would take place. Supply your price for a limit order; the exact price is difficult to know before execution.  
orderType | **integer..** The type of the proposed order. One of:  
0 Unknown  
1 Market  
2 Limit  
3 StopMarket  
4 StopLimit  
5 TrailingStopMarket  
6 TrailingStopLimit  
7 BlockTrade  
  
makerTaker | **integer.** Depending on the venue, there may be different fees for a maker (one who places the order on the books, either buy or sell) or taker (one who accepts the order, either buy or sell). If the user places a large order that is only partially filled, he is a partial maker.  
0 Unknown  
1 Maker  
2 Taker  
side | **integer.** One of:  
0 Buy  
1 Sell  
2 Short  
3 Unknown  
  
### Response
    
    
    {
    Â â¯"OrderFee":  0.01,
    Â â¯"ProductId":  1 
    }
    

Key | Value  
---|---  
OrderFee | **real.** The estimated fee for the trade as described. The minimum value is 0.01.  
ProductId | **integer.** The ID of the product (currency) in which the fee is denominated.  
  
## GetOrderHistory

**Category:** User  
**Permissions:** Trading, AccountReadOnly  
**Call Type:** Synchronous

Returns a complete list of all orders, both open and executed, for a specific account on the specified Order Management System. The account named in the request must be associated with the calling user.

### Request
    
    
    {
    Â â¯"OMSId":  1,
    Â â¯"AccountId":  1 
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System where the orders were placed.  
AccountId | **integer**. The ID of the account whose orders will be returned  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOrderHistory** returns an array containing both buy-side and a sell-side orders for the named account. The call returns an empty array if there are no open orders for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format x 1000 (milliseconds since 1/1/1970 in UTC time zone).  
ReceiveTimeTicks | **long integer.** Time stamp of the order Microsoft Ticks format and UTC time zone. **Note:** Microsoft Ticks format is usually provided as a string. Here it is provided as a long integer.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## GetOrderHistoryByOrderId

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Retrieves the full order history of a specific order by its order ID, including any changes.

A user with Trading permission can retrieve an order history only for the user's accounts and instruments; a user with Operator permission can retrieve all accounts and instruments.

### Request
    
    
    {
      "omsId": 0,
      "orderId": 0
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System where the account's order history resides.  
orderId | **long integer.** The ID of the of the order whose history you want to return.  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOrderHistoryByOrderId** returns an array containing all four types of orders for the named account. The call returns an empty array if there are no orders for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format x 1000 (milliseconds since 1/1/1970 in UTC time zone).  
ReceiveTimeTicks | **long integer.** Time stamp of the order Microsoft Ticks format and UTC time zone. **Note:** Microsoft Ticks format is usually provided as a string. Here it is provided as a long integer.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## GetOrdersHistory

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Retrieves an array of multiple orders (hence, **GetOrdersHistory** with plural _Orders_) for the specified account, order ID, user, instrument, or time stamp. The history starts at index _i_ , where _i_ is an integer identifying a specific order (the most recent order has an index of 0). âDepthâ is the count of trades to report backwards from _startIndex_. All values in the call other than _OMSId_ are optional.

For example, if _depth_ = 200 and _startIndex_ = 0, the history returns 200 orders into the past starting with the most recent (0) order. If _depth_ = 200 and _startIndex_ = 100, the history returns 200 orders into the past starting at 100 orders in the past.

The owner of the trading venue determines how long to retain order history before archiving.

A user with Trading permission can retrieve a history only for accounts with which the user is associated; a user with Operator permission can retrieve a history for any user or account.

**Note:** In this call, "Depth" refers to the count of trades to report, not the depth of the order book.

### Request
    
    
    {
        "omsId": 0,
        "accountId": 0,
        "clientOrderId": 0,
        "originalOrderId": 0,
        "originalClientOrderId": 0,
        "userId": 0,
        "instrumentId": 0,
        "startTimestamp": 0,
        "endTimestamp": 0,
        "depth": 100,
        "startIndex": 0
    }
    

All values other than _OMSId_ are optional. If account ID is not supplied, the Exchange assumes the default account of the user issuing the call.

Key | Value  
---|---  
omsId | **Integer**. The ID of the Order Management System on which the orders took place. _Required_. If no other values are specified, the call returns the orders associated with the default account for the logged-in user on this Order Management System.  
accountId | **Integer**. The account ID that made the trades. A user with Trading permission must be associated with this account, although other users also can be associated with the account. If no account ID is supplied, the system assumes the default account for the logged-in user.  
clientOrderId | **long integer**. A user-assigned ID for the order (like a purchase-order number assigned by a company). _clientOrderId_ defaults to 0.  
originalOrderId | **long integer**. The original ID of the order. If specified, the call returns changed orders associated with this order ID.  
originalClientOrderId | **long integer**. If the order has been changed, shows the original client order ID, a value that the client can create (much like a purchase order).  
userId | **integer**. The ID of the user whose account orders will be returned. If not specified, the call returns the orders of the logged-in user.  
instrumentId | **long integer**. The ID of the instrument named in the order. If not specified, the call returns orders for all instruments traded by this account.  
startTimestamp | **long integer**. Date and time at which to begin the orders history, in POSIX format.  
endTimestamp | **long integer**. Date and time at which to end the orders report, in POSIX format.  
depth | **integer**. In this case, the count of orders to return, counting from the _StartIndex_. If not specified, returns all orders between _BeginTimeStamp_ and _EndTimeStamp_ , beginning at _StartIndex_ and working backwards.  
startIndex | **integer**. The starting index into the order history, from 0 (the most recent trade) and moving backwards in time. If not specified, defaults to 0.  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOrdersHistory** returns an array containing all four types of orders for the named account. The call returns an empty array if there are no orders for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format x 1000 (milliseconds since 1/1/1970 in UTC time zone).  
ReceiveTimeTicks | **long integer.** Time stamp of the order Microsoft Ticks format and UTC time zone. **Note:** Microsoft Ticks format is usually provided as a string. Here it is provided as a long integer.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## GetOrderStatus

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Retrieves the status information for a single order.

A user with Trading permission can retrieve status information for accounts and orders with which the user is associated; a user with Operator permission can retreive status information for any account or order ID.

### Request
    
    
    {
    Â â¯"omsId": 0,
    Â â¯"accountId": 0,
    Â â¯"orderId": 0,
    }
    

Key | Value  
---|---  
omsId | **Integer.** The ID of the Order Management System on which the order was placed.  
accountId | **integer.** The ID of the account under which the order was placed.  
orderId | **integer.** The ID of the order whose status will be returned.  
  
### Response
    
    
    [
        {
            "Side": "Buy",
            "OrderId": 0,
            "Price":  0.0,
            "Quantity":  0.0,
            "DisplayQuantity":  0.0,
            "Instrument": 0,
            "Account": 0,
            "OrderType": "Unknown",
            "ClientOrderId": 0,
            "OrderState": "Unknown",
            "ReceiveTime": 0,
            "ReceiveTimeTicks": 0,
            "OrigQuantity": 0.0,
            "QuantityExecuted": 0.0,
            "AvgPrice": 0.0,
            "CounterPartyId": 0,
            "ChangeReason": "Unknown",
            "OrigOrderId": 0,
            "OrigClOrdId": 0,
            "EnteredBy": 0,
            "IsQuote": false,
            "InsideAsk": 0.0,
            "InsideAskSize": 0.0,
            "InsideBid": 0.0,
            "InsideBidSize": 0.0,
            "LastTradePrice": 0.0,
            "RejectReason": "",
            "IsLockedIn": false,
            "CancelReason": "",
            "OMSId": 0
        },
    ]
    

The call **GetOrderStatus** returns an array containing both buy-side and a sell-side open orders for the named account. The call returns an empty array if there are no open orders for the account.

Key | Value  
---|---  
Side | **string.** The side of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** Unknown (an error condition)  
OrderId | **long integer.** The ID of the open order. The _OrderID_ is unique in each Order Management System.  
Price | **real.** The price at which the buy or sell has been ordered.  
Quantity | **real.** The quantity of the product to be bought or sold.  
DisplayQuantity | **real.** The quantity available to buy or sell that is publicly displayed to the market. To display a _displayQuantity_ value, an order must be a Limit order with a reserve.  
Instrument | **integer.** ID of the instrument being traded. The call **GetInstruments** can supply the instrument IDs that are available.  
orderType | **string.** Describes the type of order this is. One of:  
**0** Unknown (an error condition)  
**1** Market order  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade  
ClientOrderId | **integer.** An ID supplied by the client to identify the order (like a purchase order number). The _ClientOrderId_ defaults to 0 if not supplied.  
OrderState | **string.** The current state of the order. One of:  
**0** Unknown  
**1** Working  
**2** Rejected  
**3** Canceled  
**4** Expired  
**5** Fully Executed.  
ReceiveTime | **long integer.** Time stamp of the order in POSIX format x 1000 (milliseconds since 1/1/1970 in UTC time zone).  
ReceiveTimeTicks | **long integer.** Time stamp of the order Microsoft Ticks format and UTC time zone. **Note:** Microsoft Ticks format is usually provided as a string. Here it is provided as a long integer.  
OrigQuantity | **real.** If the open order has been changed or partially filled, this value shows the original quantity of the order.  
QuantityExecuted | **real.** If the open order has been at least partially executed, this value shows the amount that has been executed.  
AvgPrice | **real.** The average executed price for the instrument in the order.  
CounterPartyId | **integer.** The ID of the other party in an off-market trade.  
ChangeReason | **string.** If the order has been changed, this string value holds the reason. One of:  
**0** Unknown  
**1** NewInputAccepted  
**2** NewInputRejected  
**3** OtherRejected  
**4** Expired  
**5** Trade  
**6** SystemCanceled_NoMoreMarket  
**7** SystemCanceled_BelowMinimum  
**8** SystemCanceled_PriceCollar  
**9** SystemCanceled_MarginFailed  
**100** UserModified  
OrigOrderId | **integer.** If the order has been changed, this is the ID of the original order.  
OrigClOrdId | **integer.** If the order has been changed, this is the ID of the original client order ID.  
EnteredBy | **integer.** The user ID of the person who entered the order.  
IsQuote | **Boolean.** If this order is a quote, the value for _IsQuote_ is _true,_ else _false._  
InsideAsk | **real.** If this order is a quote, this value is the Inside Ask price.  
InsideAskSize | **real.** If this order is a quote, this value is the quantity of the Inside Ask quote.  
InsideBid | **real.** If this order is a quote, this value is the Inside Bid price.  
InsideBidSize | **real.** If this order is a quote, this value is the quantity of the Inside Bid quote.  
LastTradePrice | **real.** The last price that this instrument traded at.  
RejectReason | **string.** If this open order has been rejected, this string holds the reason for the rejection.  
IsLockedIn | **Boolean.** For a block trade, if both parties to the block trade agree that one of the parties will report the trade for both sides, this value is _true._ Othersise, _false._  
CancelReason | **string.** If this order has been canceled, this string holds the cancelation reason.  
OMSId | **integer.** The ID of the Order Management System on which the order took place.  
  
## ModifyOrder

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Reduces an orderâs quantity without losing priority in the order book. An orderâs quantity can only be reduced. The other call that can modify an order — **CancelReplaceOrder** — resets order book priority, but you can use it to increase an order.

**Note:** **ModifyOrder** does not surrender or reset order book priority.

### Request
    
    
    {
    Â â¯"OMSId": 0,
    Â â¯"OrderId": 0,
    Â â¯"InstrumentId": 0,
    Â â¯"PreviousOrderRevision": 0,
    Â â¯"Quantity": 0 
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System where the original order was placed.  
OrderId | **long integer.** The ID of the order to be modified. The ID was supplied by the server when the order was created.  
InstrumentId | **integer.** The ID of the instrument traded in the order.  
PreviousOrderRevision | **integer.** The order revision number at the time you make the modification order. This ensures that you have the latest order state at the time you make the request.  
Quantity | **real.** The new quantity of the order. This value can only be reduced from a previous quantity.  
  
### Response
    
    
    {
    Â â¯"result": false,
    Â â¯"errormsg": "",
    Â â¯"errorcode": 0,
    Â â¯"detail": "",
    }
    

The response acknowledges the successful receipt of your request to modify an order; it does not indicate that the order has been modified. To find if an order has been modified, check using **GetOpenOrders** and **GetOrderHistory.**

Key | Value  
---|---  
result | **Boolean.** The successful receipt of a modify order request returns _true_ ; otherwise, returns _false_. This is the acknowledgment of receipt of the request to modify, not a confirmation that the modification has taken place.  
errormsg | **string.** A successful receipt of a modify request returns _null_ ; the _errormsg_ parameter for an unsuccessful request returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
errorcode | **integer.** The receipt of a successful request to modify returns 0. An unsuccessful request returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually _null_.  
  
## OrderBook

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

The order book endpoint is to provide a complete level 2 order book (arranged by best asks/bids) with full depth returned for a given market pair.

### Request
    
    
    {
        "market_pair": "BTCCAD"
        "depth": 10
        "level": 3
    }
    

Key | Value  
---|---  
market_pair | **string** A pair such as BTCCAD.  
depth | **integer** Orders depth quantity: [0,5,10,20,50,100,500]. Not defined or 0 = full order book. Depth = 100 means 50 for each bid/ask side.  
level | **integer** Level 1 â Only the best bid and ask. Level 2 â Arranged by best bids and asks. Level 3 â Complete order book, no aggregation.  
  
### Response
    
    
    {
        "timestamp": 500773,
        "bids": [
            [
            0.0003,
            76013.2
            ],
        ],
        "asks": [
            [
            0.36840,
            76121.85
            ],
        ],
    }
    

The response returns JSON object that contains timestamp, asks array, and bids array 

Key | Value  
---|---  
timestamp | **integer** Unix timestamp in milliseconds for when the last updated time occurred.  
bids | **decimal** An array containing 2 elements. The offer price and quantity for each bid order.  
asks | **decimal** An array containing 2 elements. The ask price and quantity for each ask order.  
  
## SendOrder

**Category:** User  
**Permissions:** Operator, Trading  
**Call Type:** Asynchronous

Creates an order. 

Anyone submitting an order should also subscribe to the various market data and event feeds, or call **GeOpenOrders** or **GetOrderStatus** to monitor the status of the order. If the order is not in a state to be executed, **GetOpenOrders** will not return it.

A user with Trading permission can create an order only for those accounts and instruments with which the user is associated; a user with Operator permissions can create an order for any account and instrument.

**Note:** Call Type is asynchronous.

### Request
    
    
     {
         "InstrumentId": 1,
         "OMSId": 1,
         "AccountId": 1,
         "TimeInForce": 1,
         "ClientOrderId": 1,
         "OrderIdOCO": 0,
         "UseDisplayQuantity": false,
         "Side": 0,
         "quantity": 1,
         "OrderType": 2,
         "PegPriceType": 3,
         "LimitPrice": 8800
     }
    

Key | Value  
---|---  
InstrumentId | **integer.** The ID of the instrument being traded.  
OMSId | **integer.** The ID of the Order Management System where the instrument is being traded.  
AccountId | **integer.** The ID of the account placing the order.  
TimeInForce | **integer.** An integer that represents the period during which the new order is executable. One of:  
**0** Unknown (error condition)  
**1** GTC (good 'til canceled, the default)  
**2** OPG (execute as close to opening price as possible)  
**3** IOC (immediate or canceled)  
**4** FOK (fill-or-kill — fill immediately or kill immediately)  
**5** GTX (good 'til executed)  
**6** GTD (good 'til date)  
ClientOrderId | **long integer.** A user-assigned ID for the order (like a purchase-order number assigned by a company). This ID is useful for recognizing future states related to this order. _ClientOrderId_ defaults to 0.  
OrderIdOCO | **long integer.** The order ID if One Cancels the Other â If this order is order A, _OrderIdOCO_ refers to the order ID of an order B (which is _not_ the order being created by this call). If order B executes, then order A created by this call is canceled. You can also set up order B to watch order A in the same way, but that may require an update to order B to make it watch this one, which could have implications for priority in the order book. See **CancelReplaceOrder** and **ModifyOrder.**  
UseDisplayQuantity | **Boolean.** If you enter a Limit order with a reserve, you must set _UseDisplayQuantity_ to _true_.  
Side | **integer.** A number representing on of the following potential sides of a trade. One of:  
**0** Buy  
**1** Sell  
**2** Short  
**3** unknown (an error condition)  
Quantity | **real.** The quantity of the instrument being ordered.  
OrderType | **integer.** A number representing the nature of the order. One of:  
**0** Unknown  
**1** Market  
**2** Limit  
**3** StopMarket  
**4** StopLimit  
**5** TrailingStopMarket  
**6** TrailingStopLimit  
**7** BlockTrade.  
PegPriceType | **integer.** When entering a stop/trailing order, set _PegPriceType_ to an integer that corresponds to the type of price that pegs the stop:  
**1** Last  
**2** Bid  
**3** Ask  
**4** Midpoint  
LimitPrice | **real.** The price at which to execute the order, if the order is a Limit order.  
  
### Response
    
    
    {
    Â â¯"status": "Accepted",
    Â â¯"errormsg": "",
    Â â¯"OrderId": 123 // Server order id
    }
    

Key | Value  
---|---  
status | **string**. If the order is accepted by the system, it returns "Accepted," if not it returns "Rejected."  
Accepted  
Rejected  
errormsg | **string**. Any error message the server returns.  
OrderId | **long integer**. The ID assigned to the order by the server. This allows you to track the order.  
  
## UpdateQuote

**Category:** User  
**Permissions:** Operator, MarketMaker  
**Call Type:** Synchronous

Updates an existing quote. Quoting is not enabled for the retail end user of the AlphaPoint software. Only registered market participants or market makers may quote.

**Warning** **UpdateQuote** resets the quote's priority in the order book.

### Request
    
    
    {
        "OMSId": 0,
        "AccountId": 0,
        "InstrumentId": 0,
        "BidQuoteId": 0,
        "Bid": 0,
        "BidQTY": 0,
        "AskQuoteId": 0,
        "Ask": 0,
        "AskQTY": 0,
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System where the quote is located.  
AccountId | **integer.** The ID of the account whose quote will be updated.  
InstrumentId | **long integer.** The ID of the instrument whose quote is being updated.  
BidQuoteId | **integer.** The ID of the original bid quote being updated.  
Bid | **real.** The new amount of the bid quote.  
BidQTY | **real.** The new quantity of the bid quote.  
AskQuoteId | **integer.** The ID of the original ask quote being updated.  
Ask | **real.** The new amount of the ask quote.  
AskQTY | **real.** The new quantity of the ask quote.  
  
### Response
    
    
    {
    Â â¯"BidResult": {
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯},
    Â â¯"AskResult": {
    Â â¯Â â¯"result": true,
    Â â¯Â â¯"errormsg": "",
    Â â¯Â â¯"errorcode": 0,
    Â â¯Â â¯"detail": "",
    Â â¯}
    }
    

Key | Value  
---|---  
BidResult | **object.** Returns a response object for Bid (see below).  
AskResult | **object.** Returns a response object for Ask.  
  
Objects for both _BidResult_ and _AskResult_ :

Key | Value  
---|---  
result | **Boolean.** A successful receipt of the update returns _true_ ; and unsuccessful receipt of the update (an error condition) returns _false_.  
errormsg | **string.** A successful receipt of the update returns _null_ ; the _errormsg_ parameter for an unsuccessful receipt returns one of the following messages:  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
errorcode | **integer.** A successful receipt of the update returns 0. An unsuccessful receipt returns one of the _errorcodes_ shown in the _errormsg_ list.  
detail | **string.** Message text that the system may send. Usually null.  
  
# Products

These calls correspond roughly to the Products function of the Exchange Admin and Admin Guide.

## GetProduct

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Retrieves the details about a specific product on the trading venue. A product is an asset that is tradable or paid out.

### Request
    
    
    {
    Â â¯"OMSId":  1,
    Â â¯"ProductId":  1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System that includes the product.  
ProductId | **long integer.** The ID of the product on the specified Order Management System.  
  
### Response
    
    
    {
        "omsId":0,
        "productId":0,
        "product":null,
        "productFullName":null,
        "productType":0,
        "decimalPlaces":0.0,
        "tickSize":0.0,
        "noFees":false
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System that offers the product.  
productId | **long integer.** The ID of the product.  
product | **string.** âNicknameâ or shortened name of the product. For example, NZD (New Zealand Dollar).  
productFullName | **string.** Full and official name of the product. For example, New Zealand Dollar.  
productType | **string.** The nature of the product. One of:  
0 Unknown (an error condition)  
1 NationalCurrency  
2 CryptoCurrency  
3 Contract  
decimalPlaces | **integer.** The number of decimal places in which the product is divided. The maximum is 8. For example, US Dollars are divided into 100 units, or 2 decimal places. Other products may be different. Burundi Francs use 0 decimal places and the Rial Omani uses 3.  
tickSize | **real.** The smallest increment in which the product may trade.  
noFees | **Boolean.** Shows whether trading the product incurs transaction fees. The default is _false_ ; that is, if _NoFees_ is _false_ , transaction fees will be incurred. If _NoFees_ is _true_ , no fees are incurred.  
  
## GetProducts

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Returns an array of products and currencies available on the exchange. A product is an asset that is tradable or paid out. 

### Request
    
    
    {
    Â â¯"OMSId": 1,
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System for which the array of available products and currencies will be returned.  
  
### Response
    
    
    [
        {
            "omsId":0,
            "productId":0,
            "product":"",
            "productFullName":"",
            "productType":0,
            "decimalPlaces":0.0,
            "tickSize":0.0,
            "noFees":false
        },
    ]
    

The response returns an array of objects, one object for each product available on the Order Management System.

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System that offers the product.  
productId | **long integer.** The ID of the product.  
product | **string.** âNicknameâ or shortened name of the product. For example, NZD (New Zealand Dollar).  
productFullName | **string.** Full and official name of the product. For example, New Zealand Dollar.  
productType | **integer.** A number describing the nature of the product. One of:  
0 Unknown (an error condition)  
1 NationalCurrency  
2 CryptoCurrency  
3 Contract  
decimalPlaces | **integer.** The number of decimal places in which the product is divided. The maximum is 8. For example, US Dollars are divided into 100 units, or 2 decimal places. Other products may be different. Burundi Francs use 0 decimal places and the Rial Omani uses 3.  
tickSize | **real.** The smallest increment in which the product can trade.  
noFees | **Boolean.** Shows whether trading the product incurs transaction fees. The default is _false_ ; that is, if _NoFees_ is _false_ , transaction fees will be incurred. If _NoFees_ is _true_ , no fees are incurred.  
  
# Instruments

These calls correspond roughly to the Instruments function of the Exchange Admin and Admin Guide.

## Assets

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

The assets endpoint is to provide a detailed summary for each currency available on the exchange.

### Request

This endpoint doesnt require any request parameters

### Response
    
    
    [
        {
            "name": "Bitcoin",
            "unified_cryptoasset_id": 1,
            "min_withdraw": 0.0000000100000000000000000000
        },
    ]
    

The response returns an array of JSON objects with the following key/value pair 

Key | Value  
---|---  
name | **string** Full name of cryptocurrency.  
unified_cryptoasset_id | **integer** Unique ID of cryptocurrency assigned by Unified Cryptoasset ID.  
min_withdraw | **decimal** Identifies the single minimum withdrawal amount of a cryptocurrency.  
  
## GetInstrument

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Retrieves the details of a specific instrument from the Order Management System of the trading venue. An instrument is a pair of exchanged products (or fractions of them) such as US dollars and BitCoin.

### Request
    
    
    {
    Â â¯"OMSId": 1,
    Â â¯"InstrumentId": 1 
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System on which the instrument is traded.  
InstrumentId | **integer**. The ID of the instrument.  
  
### Response
    
    
    {
        "omsId": 0,
        "instrumentId": 0,
        "symbol": null,
        "product1": 0,
        "product1Symbol": null,
        "product2": 0,
        "product2Symbol": null,
        "instrumentType": 0,
        "venueInstrumentId": 0,
        "venueId": 0,
        "sortIndex": 0,
        "sessionStatus": 0,
        "previousSessionStatus": 0,
        "sessionStatusDateTime": "0001-01-01T00:00:00",
        "selfTradePrevention": false,
        "quantityIncrement": 0.0,
        "priceIncrement": 0.0
    }
    

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the instrument is traded.  
instrumentId | **integer.** The ID of the instrument.  
symbol | **string.** Trading symbol of the instrument, for example BTCUSD.  
product1 | **integer.** The ID of the first product comprising the instrument.  
product1Symbol | **string.** The symbol for Product 1 on the trading venue. For example, BTC.  
product2 | **integer.** The ID of the second product comprising the instrument.  
product2Symbol | **string.** The symbol for Product 2 on the trading venue. For example, USD.  
instrumentType | **integer.** A number representing the type of the instrument. All instrument types currently are _standard_ , an exchange of one product for another (or _unknown_ , an error condition), but this may expand to new types in the future.  
0 Unknown (an error condition)  
1 Standard  
venueInstrumentId | **integer** A venue instrument is created at the exchange level as an instrument "template" for adding new instruments to the exchange. This is the ID of the venue instrument behind the instrument being requested.  
venueId | **integer.** The ID of the trading venue on which the instrument trades.  
sortIndex | **integer.** The numerical position in which to sort the returned list of instruments on a visual display. Since this call returns information about a single instrument, _SortIndex_ should return 0.  
sessionStatus | **integer.** Is the market for this instrument currently open and operational? Returns one of:  
0 Unknown  
1 Running  
2 Paused  
3 Stopped  
4 Starting  
previousSessionStatus | **string.** What was the previous session status for this instrument? One of:  
0 Unknown  
1 Running  
2 Paused  
3 Stopped  
4 Starting  
sessionStatusDateTime | **string.** The time and date at which the session status was reported, in Microsoft Ticks format.  
selfTradePrevention | **Boolean.** An account that is trading with itself still incurs fees. If this instrument prevents an account from trading the instrument with itself, the value returns _true_ ; otherwise defaults to _false_.  
quantityIncrement | **real.** The smallest tradeable increment of the instrument. For example, for BTCUSD, the quantity increment might be 0.0005, but for ETHUSD, the quantity increment might be 50.  
priceIncrement | **real.** The smallest amount by which the instrument can rise or fall in the market.  
  
## GetInstruments

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Retrieves a list of instruments available on the exchange. An instrument is a pair of exchanged products (or fractions of them) such as US dollars and BitCoin. 

### Request
    
    
    {
        "OMSId":  1
    }
    

Key | Value  
---|---  
OMSId | **integer**. The ID of the Order Management System on which the instruments are available.  
  
### Response
    
    
    [
        {
            "omsId":0 ,
            "instrumentId": 0,
            "symbol": "",
            "product1": 0,
            "product1Symbol": "",
            "product2": 0,
            "product2Symbol": "",
            "instrumentType": 0,
            "venueInstrumentId": 0,
            "venueId":0,"sortIndex": 0,
            "sessionStatus": 0,
            "previousSessionStatus": 0,
            "sessionStatusDateTime": "0001-01-01T00:00:00",
            "selfTradePrevention": false,
            "quantityIncrement": 0.0,
            "priceIncrement": 0.0
        },
    ]
    

The response for **GetInstruments** is an array of objects listing all the instruments available on the Order Management System.

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which the instrument is traded.  
instrumentId | **integer.** The ID of the instrument.  
symbol | **string.** Trading symbol of the instrument, for example BTCUSD.  
product1 | **integer.** The ID of the first product comprising the instrument.  
product1Symbol | **string.** The symbol for Product 1 on the trading venue. For example, BTC.  
product2 | **integer.** The ID of the second product comprising the instrument.  
product2Symbol | **string.** The symbol for Product 2 on the trading venue. For example, USD.  
instrumentType | **integer.** A number representing the type of the instrument. All instrument types currently are _standard_ , an exchange of one product for another (or _unknown_ , an error condition), but this may expand to new types in the future.  
0 Unknown (an error condition)  
1 Standard  
venueInstrumentId | **integer** A venue instrument is created at the exchange level as an instrument "template" for adding new instruments to the exchange. This is the ID of the venue instrument behind the instrument being requested.  
venueId | **integer.** The ID of the trading venue on which the instrument trades.  
sortIndex | **integer.** The numerical position in which to sort the returned list of instruments on a visual display. Since this call returns information about a single instrument, _SortIndex_ should return 0.  
sessionStatus | **integer.** Is the market for this instrument currently open and operational? Returns one of:  
0 Unknown  
1 Running  
2 Paused  
3 Stopped  
4 Starting  
previousSessionStatus | **string.** What was the previous session status for this instrument? One of:  
0 Unknown  
1 Running  
2 Paused  
3 Stopped  
4 Starting  
sessionStatusDateTime | **string.** The time and date at which the session status was reported, in Microsoft Ticks format.  
selfTradePrevention | **Boolean.** An account that is trading with itself still incurs fees. If this instrument prevents an account from trading the instrument with itself, the value returns _true_ ; otherwise defaults to _false_.  
quantityIncrement | **real.** The smallest tradeable increment of the instrument. For example, for BTCUSD, the quantity increment might be 0.0005, but for ETHUSD, the quantity increment might be 50.  
priceIncrement | **real.** The amount by which the instrument can rise or fall in the market.  
  
# Tickets

These calls correspond roughly to the Tickets function of the Exchange Admin and Admin Guide.

## Deposit and Withdraw Templates

Templates provide a set of information about banking tasks during deposits and withdrawals in the form of specific key-value pairs. Each template has a name. There are different templates for different types of deposit and withdrawal, determined by the product or asset (BitCoin, Monero, US Dollar, etc.), the specific bank or other Account Provider, and the information that the Account Provider requires for the transaction.

Most templates are used for withdrawals.

Example 1 and 2 are two example templates.

> Template Example 1
    
    
    "TemplateformType": "Standard",
    {
        "Full Name": "John Smith",
        "Language": "en",
        "Comment": "",
        "BankAddress": "123 Fourth St.",
        "BankAccountNumber": "12345678",
        "BankAccountName": "John Smith & Sons",
        "Swiftcode": "ABCDUSA1"
    }
    

> Template Example 2
    
    
    "TemplateFormType": "TetherRPCWithdraw",
    {
        "TemplateType": "TetherRPCWithdraw",
        "Comment": "TestWithdraw",
        "ExternalAddress": "ms6C3pKAAr8gRCcnVebs8VRkVrjcvqNYv3"
    }
    

The content of the template depends on the Account Provider that you use for deposits and withdrawals. The Account Provider does not supply the template _per se_ (they do, however, determine the fields that are in the template). The template is specific to each Account Provider. 

To determine which withdrawal template types are available to you, call **GetWithdrawTemplateTypes.**

## AddDepositTicketAttachment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Adds an attachment to a deposit ticket.

User with Trading permission can add an attachment only to their own deposit tickets; users with Operator permission can add an attachment to any deposit ticket.

### Request
    
    
    {
        "base64Attachment": "",
        "attachmentId": 0,
        "submittedByUserId": 0, 
        "submittedByUserName": "",
        "uploadDate": "0001-01-01T00:00:00",
        "uploadIP": "",
        "ticketNumber": 0,
        "description": ""
    }
    

Key | Value  
---|---  
base64Attachment | **string.** Any attachment file; PDF, spreadsheet, blob.  
attachmentId | **long integer.** The ID of the attachment. Assign 0 to this key. The system will assign an ID to the attachment and return it in the response when it receives the call.  
submittedByUserId | **integer.** The user ID of the user submitting the attachment.  
submittedByUserName | **string.** The user name of the user submitting the attachment; for example, jsmith.  
uploadDate | **string.** The date and time stamp showing when the attachment was uploaded, in Microsoft Ticks format. All date and time stamps are in UTC.  
uploadIp | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The number of the deposit ticket to which the attachment is being attached.  
description | **string.** A description of the attachment.  
  
### Response
    
    
    {
        "success": true,
        "attachmentid": 100000002
    }
    

Unlike many responses, a _true_ response in the _success_ field indicates that the attachment was received and attached to the deposit ticket.

Key | Value  
---|---  
success | **Boolean.** A _true_ value means that the attachment was received and attached to the deposit ticket specified in the Request. A _false_ value indicates that it was not.  
attachmentid | **long integer.** The ID for the attachment, supplied by the system.  
  
## AddWithdrawTicketAttachment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Adds an attachment to a withdraw ticket.

Users with Trading permission can add an attachment only to their own withdraw tickets; users with Operator permission can add an attachment to any withdraw ticket.

### Request
    
    
    {
        "base64Attachment": "",
        "attachmentId": 0,
        "submittedByUserId": 0,
        "submittedByUserName": "",
        "uploadDate": "0001-01-01T00:00:00",
        "uploadIP": "",
        "ticketNumber": 0,
        "description": ""
    }
    

Key | Value  
---|---  
base64Attachment | **string.** Any attachment file; PDF, spreadsheet, blob, or other format.  
attachmentId | **long integer.** The ID of the attachment. Assign a 0 value to this key. The system will assign an ID to the attachment and return it in the response when it receives this call.  
submittedByUserId | **integer.** The user ID of the user submitting the attachment.  
submittedByUserName | **string.** The user name of the user submitting the attachment; for example, Jsmith.  
uploadDate | **string.** The date and time stamp showing when the attachment was uploaded, in Microsoft Ticks format. All date and time stamps are in UTC.  
uploadIp | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The number of the withdraw ticket to which the attachment is being attached.  
description | **string.** A description of the attachment.  
  
### Response
    
    
    {
        "success": true,
        "attachmentid": 100000002
    }
    

Unlike many responses, a _true_ response in the _success_ field indicates that the attachment was received and attached to the withdraw ticket.

Key | Value  
---|---  
success | **Boolean.** A _true_ value means that the attachment was received and attached to the withdraw ticket specified in the Request. A _false_ value indicates that it was not.  
attachmentid | **long integer.** The ID for the attachment, supplied by the system.  
  
## ConfirmWithdraw

**Category:** System  
**Permissions:** Public  
**Call Type:** Synchronous

Checks whether the user has clicked the confirmation link in an email. The email confirms whether the user issued the withdrawal request.

### Request
    
    
    {
        "UserId": 1,
        "VerifyCode": "Verify Code GUID"
    }
    

Key | Value  
---|---  
UserId | **integer.** The ID of the calling user.  
VerifyCode | **string.** The globally unique identifier (GUID) that identifies a specific withdrawal.  
  
### Response
    
    
    {
        "result": true
    }
    

Key | Value  
---|---  
result | **Boolean.** Returns _true_ if the user has clicked the link in the confirming email). Returns false if the withdrawal has not clicked the link.  
  
## CreateDepositTicket

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

**CreateDepositTicket** records a deposit ticket for deposits of fiat money (non-crypto national currencies, for example). Crypto-currencies, such as BitCoin or Monero are handled by a different deposit mechanism described in **GetDepositInfo.**

The ticketing mechanism of the Order Management System tracks deposits and withdrawals, interacting with the Asset Manager.

### Request
    
    
    {
        "assetManagerId": 0,
        "accountId": 0,
        "assetId": 0,
        "assetName": null,
        "amount": 0.0,
        "omsId": 0,
        "requestCode": null,
        "requestIP": null,
        "requestUser": 0,
        "requestUserName": null,
        "operatorId": 0,
        "Status": 0,
        "feeAmt": 0.0,
        "updatedByUser": 0,
        "updatedByUserName": null,
        "ticketNumber": 0,
        "depositInfo": "",
        "createdTimestamp": "0001-01-01T00:00:00",
        "lastUpdateTimeStamp": "0001-01-01T00:00:00",
        "comments": null,
        "attachments": null
    }
    

Key | Value  
---|---  
assetManagerId | **integer.** The ID of the system's asset manager module, usually 1.  
accountId | **integer.** The account receiving the deposit.  
assetId | **integer.** The ID of the asset being deposited. An asset is functionally the same as a product; you can obtain a list of products/assets available on the Exchange by using **GetProducts.**  
assetName | **string.** The short name of the asset being deposited. For example, USD (US Dollars) or BTC (BitCoin).  
amount | **real.** The quantity of the asset being deposited. This is not the monetary value of the asset. For example, 2.5 BitCoins is 2.5.  
omsId | **integer.** The ID of the Order Management System where the deposit is being made, usually 1.  
requestCode | **string.** A _requestCode_ is a globally unique ID assigned by the system. Leave the value for this string null when issuing the **CreateDepositTicket** call; the Response returns the value for the _requestCode,_ which you may need for other calls.  
requestIp | **string.** The IP address from which the calling user makes the deposit ticket request.  
requestUser | **integer.** The user ID of the user making the deposit ticket request.  
requestUserName | **string.** The user name of the user making the deposit ticket request, for example, jsmith.  
operatorId | **integer.** The ID of the trading venue operator.  
status | **integer.** The current status of the deposit, stated as a number. A new deposit will always have a status of 0.  
feeAmt | **real.** The amount of any fee for the deposit.  
updatedByUser | **integer.** If the deposit ticket has been updated, this field contains the user ID of the user who updated the ticket. Because **CreateDepositTicket** creates the ticket, it is unlikely to have been updated yet; this value should be 0.  
updatedByUserName | **string.** If the deposit ticket has been updated, this field contains the name of the user who updated the ticket. Because **CreateDepositTicket** creates the ticket, it is unlikely to have been updated yet; this value should be an empty string (null).  
ticketNumber | **long integer.** A number assigned by the calling user to identify this deposit ticket, much as a purchase order identifies an order.  
depositInfo | **object.** Leave this string as empty: " ".  
createdTimeStamp | **string.** The time and date stamp for when the deposit ticket was created, in Microsoft Ticks format. All time and date stamps are given as UTC.  
lastUpdateTimeStamp | **string.** The time and date stamp for the last update to the deposit ticket after it was created. Because **CreateDepositTicket** creates the ticket, it is unlikely that it has been updated, and this string should be empty.  
comments | **string.** Any comments appended to the deposit ticket.  
attachments | **string.** Any attachments appended to the deposit ticket.  
|   
  
### Response
    
    
    {
        "success": true,
        "requestcode": "866f21fe-3461-41d1-91aa-5689bc38503f",
    }
    

The successful response to **CreateDepositTicket** is a Boolean _true_ value and a request code to allow tracking the ticket. To view and confirm ticket contents, use the call **GetDepositTicket.**

String | Value  
---|---  
success | **Boolean.** Returns true if the system has created the deposit ticket successfully; otherwise returns false.  
requestcode | **string.** A globally-unique ID (GUID) that identifies this specific deposit ticket.  
  
An unsuccessful response to **CreateDepositTicket** is a standard response object that includes an error code and error message, as explained in "Standard response objects and common error codes" in **Background Information.**

## GetAccountDepositTransactions

**Category:** User  
**Permissions:** Trading, AccountReadOnly  
**Call Type:** Synchronous

Obtains a list of deposits for the account.

Users with Trading and AccountReadOnly permission can return deposit transactions only from an account with which they are associated.

The owner of the trading venue determines how long to retain transaction history before archiving.

**Note:Â** Depth in this call is a count of how many deposit transactions to report. It is not "depth of market."

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "Depth": 200
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the account transactions took place.  
AccountId | **integer.** The ID of the account whose transactions will be returned.  
Depth | **integer.** The count of deposit transactions to be returned. Defaults to 200.  
  
### Response
    
    
    [
      {
        "transactionId": 0,
        "omsId": 0,
        "accountId": 0,
        "cr": 0.0,
        "dr": 0.0,
        "counterparty": 0,
        "transactionType": 0,
        "referenceId": 0,
        "referenceType": 0,
        "productId": 0,
        "balance": 0.0,
        "timeStamp": 0
        },
    ]
    

The response returns an array of transaction objects.

Key | Value  
---|---  
transactionId | **Integer.** The ID of the transaction.  
omsId | **Integer.** The ID of the Order Management System under which the requested transactions took place.  
accountId | **Integer.** The single account under which the transactions took place.  
cr | **real.** Credit entry for the account on the order book. Funds entering an account.  
dr | **real.** Debit entry for the account on the order book. Funds leaving an account.  
counterparty | **long integer.** The corresponding party in a trade.  
transactionType | **integer.** A number representing the type of transaction:  
**1** Fee  
**2** Trade  
**3** Other  
**4** Reverse  
**5** Hold  
**6** Rebate  
**7** MarginAcquisition  
**8** MarginRelinquish  
referenceId | **long integer.** The ID of the action or event that triggered this transaction.  
referenceType | **integer.** A number representing the type of action or event that triggered this transaction. One of:  
**1** Trade  
**2** Deposit  
**3** Withdraw  
**4** Transfer  
**5** OrderHold  
**6** WithdrawHold  
**7** DepositHold  
**8** MarginHold  
**9** ManualHold  
**10** ManualEntry  
**11** MarginAcquisition  
**12** MarginRelinquish  
**13** MarginQuoteHold  
productId | **integer.** The ID of the product in which the deposit was made. Use **GetProduct** to return information about a product based on its ID.  
balance | **real.** The balance in the account after the transaction.  
timeStamp | **long integer.** Time at which the transaction took place, in POSIX format.  
  
## GetAccountWithdrawTransactions

**Category:** User  
**Permissions:** Trading, AccountReadOnly  
**Call Type:** Synchronous

Obtains a list of withdrawals for an account.

Users with Trading and AccountReadOnly permission can return withdrawal transactions only from an account with which they are associated.

The owner of the trading venue determines how long to retain transaction history before archiving.

**Note:** Depth in this call is a count of how many withdrawal transactions to report. It is not "depth of market."

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "Depth": 200
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the account transactions took place.  
AccountId | **integer.** The ID of the account whose transactions will be returned.  
Depth | **integer.** The count of withdrawal transactions to be returned. Defaults to 200.  
  
### Response
    
    
    [
      {
        "transactionId":0,
        "omsId":0,
        "accountId":0,
        "cr":0.0,
        "dr":0.0,
        "counterparty":0,
        "transactionType":0,
        "referenceId":0,
        "referenceType":0,
        "productId":0,
        "balance":0.0,
        "timeStamp":0
        },
    ]
    

The response returns an array of transaction objects.

Key | Value  
---|---  
transactionId | **Integer.** The ID of the transaction.  
omsId | **Integer.** The ID of the Order Management System under which the requested transactions took place.  
accountId | **Integer.** The single account under which the transactions took place.  
cr | **real.** Credit entry for the account on the order book. Funds entering an account.  
dr | **real.** Debit entry for the account on the order book. Funds leaving an account.  
counterparty | **long integer.** The corresponding party in a trade.  
transactionType | **integer.** A number representing the type of transaction:  
1 Fee  
2 Trade  
3 Other  
4 Reverse  
5 Hold  
6 Rebate  
7 MarginAcquisition  
8 MarginRelinquish  
referenceId | **long integer.** The ID of the action or event that triggered this transaction.  
referenceType | **integer.** A number representing the type of action or event that triggered this transaction. One of:  
1 Trade  
2 Deposit  
3 Withdraw  
4 Transfer  
5 OrderHold  
6 WithdrawHold  
7 DepositHold  
8 MarginHold  
9 ManualHold  
10 ManualEntry  
11 MarginAcquisition  
12 MarginRelinquish  
13 MarginQuoteHold  
productId | **integer.** The ID of the product that was withdrawn. Use **GetProduct** to return information about a product based on its ID.  
balance | **real.** The balance in the account after the transaction.  
timeStamp | **long integer.** Time at which the transaction took place, in POSIX format.  
  
## GetAllDepositRequestInfoTemplates

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an array of all templates available to the caller that describe a deposit form for a specific product.

An Account Provider may require specific deposit information. Deposit templates answer than need.

### Request
    
    
    {
        "OMSId": 1,
        "ProductId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the product is traded.  
ProductId | **integer.** The ID of the product to be deposited.  
|   
  
### Response
    
    
    [
        {
            "Template": {
                "ProviderType": "BitcoinRpc",
                "Template": "{}",
                "ProcessInfo": "",
                "UseGetDepositWorkflow": true,
                "DepositWorkflow": "CryptoWallet"
                },
            "result": true,
            "errormsg": null,
            "statuscode": 0
        },
    ]
    

The Response is an array of information for templates appropriate to the product specified in the Request and available to the caller, along with fields that show whether the Response successfully returned the Template information. The key-value pairs of the inner Template object vary from Account Provider to Account Provider.

#### Template object

Key | Value  
---|---  
ProviderType | **String.** The type of asset handled by the Account Provider. Possible values are:  
  
BitcoinRpc  
BitGoRpc  
Internal Accounting  
WsAccountingProvider  
EthereumERC20  
EthereumRPC  
Template | **JSON object.** The key-value pairs of _Template_ vary from Account Provider to Account Provider.  
ProcessInfo | **String.** The _ProcessInfo_ string varies with the Account Provider and the asset being deposited. In a generic deposit template, the _ProcessingInfo_ key-value pair is empty; in other cases it is an address for processing the deposit.  
UseGetDepositWorkflow | **Boolean.** A _true_ value causes the deposit to use the deposit workflow named in _DepositWorkflow._ A _false_ value causes the deposit not to use that defined workflow.  
DepositWorkflow | **String.** A set of defined workflows for this template. The workflows are defined and named during the installation of the Exchange. Choices are:  
  
CryptoWallet  
ManualDeposit  
MerchantForm  
MerchantRedirect  
Custom  
  
#### Response fields

Key | Value  
---|---  
result | **Boolean.** If the call has been successfully received by the Order Management System, returns _true,_ otherwise returns _false._  
errormsg | **String.** A successful receipt of the call returns _null._ The _errormsg_ key for an unsuccessful call can return:  
  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
statusCode | **integer.** If _result_ is _false,_ _statusCode_ can return:   
  
**32** Not Authorized  
**33** Asset_Manager_Not_Found  
  
If no Account Provider is located, _statusCode_ returns _null._  
  
## GetDepositRequestInfoTemplate

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns a single object describing a single deposit form template that is available to the caller and the caller's account, and appropriate to the product being deposited.

### Request
    
    
    {
        "OMSId": 1,
        "ProductId": 1,
        "AccountId": 1,
        "TemplateType": "TrustPay"
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the product is traded.  
ProductId | **integer.** The ID of the product to be deposited.  
AccountId | **integer.** The ID of the account into which the deposit will be made.  
TemplateType | **string.** The name of the deposit template you want to return.  
  
### Response
    
    
    {
        "Template": {
            "ProviderType":"BitcoinRpc",
            "Template": "{}",
            "ProcessInfo": "",
            "UseGetDepositWorkflow": true,
            "DepositWorkflow": "CryptoWallet"
        },
        "result": true,
        "errormsg": null,
        "statuscode": 0
    }
    

The Response is a single template appropriate to the product specified in the Request and available to the caller, along with fields that show whether the Response successfully returned the Template information. The key-value pairs of the inner Template object vary from Account Provider to Account Provider.

#### Template object

Key | Value  
---|---  
ProviderType | **String.** The type of asset handled by the Account Provider. Possible values are:  
  
BitcoinRpc  
BitGoRpc  
Internal Accounting  
WsAccountingProvider  
EthereumERC20  
EthereumRPC  
Template | **JSON object.** The key-value pairs of _Template_ vary from Account Provider to Account Provider.  
ProcessInfo | **String.** The _ProcessInfo_ string varies with the Account Provider and the asset being deposited. In a generic deposit template, the _ProcessingInfo_ key-value pair is empty; in other cases it is an address for processing the deposit.  
UseGetDepositWorkflow | **Boolean.** A _true_ value causes the deposit to use the deposit workflow named in _DepositWorkflow._ A _false_ value causes the deposit not to use that defined workflow.  
DepositWorkflow | **String.** A set of defined workflows for this template. The workflows are defined and named during the installation of the Exchange. Choices are:  
  
CryptoWallet  
ManualDeposit  
MerchantForm  
MerchantRedirect  
Custom  
  
#### Response fields

Key | Value  
---|---  
result | **Boolean.** If the call has been successfully received by the Order Management System, returns _true,_ otherwise returns _false._  
errormsg | **String.** A successful receipt of the call returns _null._ The _errormsg_ key for an unsuccessful call can return:  
  
Not Authorized (errorcode 20)  
Invalid Request (errorcode 100)  
Operation Failed (errorcode 101)  
Server Error (errorcode 102)  
Resource Not Found (errorcode 104)  
Operation Not Supported (errorcode 106)  
statusCode | **integer.** If _result_ is _false,_ _statusCode_ can return:   
  
**32** Not Authorized  
**33** Asset_Manager_Not_Found  
  
If no Account Provider is located, _statusCode_ returns _null._  
  
## GetDeposits

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an array of deposit objects with information about the deposits of a specific account.

Users with Trading permission can get deposit information only for their own accounts; users with Operator permission can get deposit information for any account.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the deposits were made.  
AccountId | **integer.** The ID of the account into which the deposits were made.  
  
### Response
    
    
    [
        {
            "omsId": 0,
            "depositId": 0,
            "accountId": 0,
            "subAccountId": 0,
            "productId": 0,
            "amount": 0.0
        },
    ]
    

The Response is an array of deposit objects.

Key | Value  
---|---  
omsId | **integer.** The ID of the Order Management System on which this deposit was made.  
depositId | **integer.** The ID of this deposit, assigned by the system.  
accountId | **integer.** The ID of the account into which this deposit was made.  
subAccountId | **integer.** Not currently used; reserved for future use. Defaults to 0.  
productId | **integer.** The ID of the product or asset (the two are synonymous) that was deposited.  
amount | **real.** The unit and fractional quantity of the product or asset that was deposited. For example 2.5 BitCoin or 2018.17 US Dollars.  
  
## GetDepositTicket

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns details about a single deposit ticket. A deposit ticket documents that a deposit was made or attempted.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "RequestCode": "Request Code GUID",
        "TicketId": 100000002
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the deposit ticket was created.  
AccountId | **integer.** The ID of the account into which the deposit was made.  
RequestCode | **string.** A globally unique ID (GUID) that identifies this specific deposit.  
TicketId | **long integer.** The ID of the specific deposit ticket, as assigned by the system.  
  
### Response
    
    
    {
        "assetManagerId": 0,
        "accountId": 0,
        "assetId": 0,
        "assetName": null,
        "amount": 0.0,
        "omsId": 0,
        "requestCode": null,
        "requestIP": null,
        "requestUser": 0,
        "requestUserName": null,
        "operatorId": 0,
        "Status": 0,
        "feeAmt": 0.0,
        "updatedByUser": 0,
        "updatedByUserName": null,
        "ticketNumber": 0,
        "depositInfo": null,
        "createdTimestamp": "0001-01-01T00:00:00",
        "lastUpdateTimeStamp": "0001-01-01T00:00:00",
        "comments": null,
        "attachments": null
    }
    

Key | Value  
---|---  
assetManagerId | **integer.** The ID of the Asset Manager on which the deposit was made.  
accountId | **integer.** The ID of the account into which the deposit was made.  
assetId | **integer.** The ID of the asset (product) that was deposited.  
assetName | **string.** The short name of the asset (product) that was deposited, for example BTC for BitCoin or USD for US Dollars.  
amount | **real.** The unit and fractional amount of the asset that was deposited, for example 2.5 BitCoin or 2018.17 US Dollars.  
omsId | **integer.** The ID of the Order Management System on which the deposit was made.  
requestCode | **string.** A globally unique alphanumeric string (GUID) assigned by the system that identifies this specific deposit.  
requestIP | **string.** The IP address from which the deposit request was made.  
requestUser | **integer.** The user ID of the user who made the deposit request.  
requestUserName | **string.** The user name of the user who made the deposit request, for example, jsmith.  
operatorId | **integer.** The user ID of the operator who managed the deposit request.  
status | **integer.** The current status of this deposit ticket. Some of these statuses are valid only for cryptocurrency deposits; some are only valid for deposits of fiat (national) currency; others are used by AlphaPoint internally. Any of the statuses may appear on a deposit ticket.  
  
**Deposit ticket statuses**  
**0** New (new ticket awaiting operator review)  
**1** AdminProcessing (an admin is looking at the ticket)  
**2** Accepted (an admin accepts the ticket)  
**3** Rejected (admin rejects the ticket)  
**4** SystemProcessing (automatic processing; an unlikely status for a deposit)  
**5** FullyProcessed (the deposit has concluded)  
**6** Failed (the deposit has failed for some reason)  
**7** Pending (Account Provider has set status to pending)  
**8** Confirmed (Account Provider confirms the deposit)  
**9** AmlProcessing (anti-money-laundering process underway)  
**10** AmlAccepted (anti-money-laundering process successful)  
**11** AmlRejected (deposit did not stand up to anti-money-laundering process)  
**12** AmlFailed (anti-money-laundering process failed/did not complete)  
**13** LimitsAccepted (deposit meets limits for fiat or crypto asset)  
**14** LimitsRejected (deposit does not meet limits for fiat or crypto asset)  
feeAmt | **real.** The fee assessed for making the deposit, if any. Deposit fees usually are assessed in the asset/product being deposited.  
updatedByUser | **integer.** The user ID of the last user to have updated the ticket (status, amount, etc.; this is usually an admin).  
updatedByUserName | **string.** The user name of the last user to have updated the ticket, for example, jsmith.  
ticketNumber | **long integer.** An ID number assigned by the system to identify the ticket (as opposed to identifying the deposit).  
depositInfo | **string.** A set of key-value pairs that holds information about the source of the funds being deposited. This information was entered when the deposit ticket was created, as required by the Account Provider. It can vary from Account Provider to Account Provider.  
createdTimeStamp | **string.** The date and time when the deposit ticket was created, in Microsoft Ticks format. All dates and times are UTC.  
lastUpdateTimeStamp | **string.** The date and time when the deposit ticket last was updated — usually by an admin changing its status — in Microsoft Ticks format. All dates and times are UTC.  
comments | **string.** Any comment appended to the deposit ticket.  
attachments | **string.** Any attachment to the deposit ticket.  
  
## GetDepositTicketAttachment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns a single specific deposit ticket attachment based solely on the attachment ID.

A user with Trading permission can return an attachment only from a deposit made to that user's associated account; a user with Operator permission can return any attachment.

### Request
    
    
    {
        "attachmentId": 0
    }
    

Key | Value  
---|---  
attachmentId | **integer.** The ID of an attachment that is part of a deposit ticket associated with the account of the issuing user (if Trading permission) or any account or user (if Operator permission).  
  
### Response
    
    
    {
        "base64Attachment": null,
        "attachmentId": 0,
        "submittedByUserId": 0,
        "submittedByUserName": null,
        "uploadDate": "0001-01-01T00:00:00",
        "uploadIP": null,
        "ticketNumber": 0,
        "description": null
    }
    

Key | Value  
---|---  
base64Attachment | **string.** Any attachment file; PDF, spreadsheet, blob.  
attachmentId | **integer.** The ID of the attachment. The system assigned the attachment ID when the attachment was uploaded.  
submittedByUserId | **integer.** The user ID of the submitting user.  
submittedByUserName | **string.** The user name of the submitting user, for example, Jsmith.  
uploadDate | **string.** The time and date that the attachment was uploaded, in Microsoft Ticks format. All times and dates are UTC.  
uploadIP | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The ID number of the deposit ticket to which the attachment was linked.  
description | **string.** A description of the attachment.  
  
## GetDepositTickets

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns an array of deposit ticket objects for a specific account. The call returns _all_ tickets for a given account. Use **GetDepositTicket** to return a single ticket. Operators (only) can use **GetAllDepositTickets** to return a subset of tickets.

Users with Trading permission can return deposit ticket information only for accounts with which they're associated; users with Operator permission can return deposit ticket information for any account.

### Request
    
    
    {
        "OMSId": 1,
        "OperatorId": 1,
        "AccountId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the account operates whose tickets you want to return.  
OperatorId | **integer.** A user with Operator permission should put the Operator's ID here; a user with Trading permission should put the value 1 here.  
AccountId | **integer.** The account whose deposit tickets you want to return.  
  
### Response
    
    
    [
        {
            "assetManagerId": 0,
            "accountId": 0,
            "assetId": 0,
            "assetName": null,
            "amount": 0.0,
            "omsId": 0,
            "requestCode": "",
            "requestIP": "",
            "requestUser": 0,
            "requestUserName": "",
            "operatorId": 0,
            "Status": 0,
            "feeAmt": 0.0,
            "updatedByUser": 0,
            "updatedByUserName": "",
            "ticketNumber": 0,
            "depositInfo": null,
            "createdTimestamp": "0001-01-01T00:00:00",
            "lastUpdateTimeStamp": "0001-01-01T00:00:00",
            "comments": null,
            "attachments": null
        },
    ]
    

The Response returns an array of deposit ticket information.

Key | Value  
---|---  
assetManagerId | **integer.** The ID of the Asset Manager module that handled the deposit.  
accountId | **integer.** The ID of the account into which the deposit was made.  
assetId | **integer.** The ID of the asset (product) deposited. This may be cryptocurrency or fiat (national) currency.  
assetName | **string.** The short name of the asset being deposited, for example USD (US Dollars), BTC (BitCoin), etc.  
amount | **real.** The unit quantity and fractional quantity of the asset being deposited. For example, 2.5 BitCoin or 2018.17 US Dollars.  
omsId | **integer.** The ID of the Order Management System through which the asset was deposited.  
requestCode | **string.** A globally unique ID (GUID) that identifies the deposit ticket on the Exchange.  
requestIP | **string.** The IP address from which the deposit was received, for example 127.0.0.1.  
requestUser | **integer.** The user ID of the user making the deposit.  
requestUserName | **string.** The user name of the user making the deposit, for example, _jsmith._  
operatorId | **integer.** The user ID of the human admin (operator) who accepted, rejected or placed the ticket in the Pending status. Operators set the status of fiat currency deposits; cryptocurrency deposits are handled automatically.  
Status | **integer.** The current status of the deposit ticket. Some of these statuses are valid only for cryptocurrency deposits and some are valid for fiat currency deposits. Some of these statuses are used by AlphaPoint internally, yet they may appear on returned Deposit Ticket information.  
  
**Deposit ticket statuses:**  
**0** New (new ticket awaiting operator review)  
**1** AdminProcessing (An admin is looking at the ticket)  
**2** Accepted (An admin accepts the ticket)  
**3** Rejected (Admin rejects the ticket)  
**4** SystemProcessing (automatic processing; an unlikely status for a deposit)  
**5** FullyProcessed (the deposit has concluded)  
**6** Failed (the deposit failed for some reason)  
**7** Pending (Account Provider has set status to pending)  
**8** Confirmed (Account Provider confirms the deposit)  
**9** AmlProcessing (anti-money-laundering process underway)  
**10** AmlAccepted (anti-money-laundering process successful)  
**11** AmlRejected (deposit did not stand up to anti-money-laundering process)  
**12** AmlFailed (anti-money-laundering process failed/did not complete)  
**13** LimitsAccepted (deposit meets limits for fiat or crypto asset)  
**14** LimitsRejected (deposit does not meet limits for fiat or crypto asset)  
feeAmt | **real.** The fee assessed by the Exchange for making the deposit, if any. Such a fee normally is assessed in the asset being deposited.  
updatedByUser | **integer.** The user ID of the person who made the most recent update to the deposit ticket. This user should be an admin (Operator).  
updatedByUserName | **string.** The user name of the person (admin/Operator) who made the most recent update to the deposit ticket.  
ticketNumber | **integer.** Number of the ticket on the Exchange.  
depositInfo | **object.** A set of key-value pairs that holds information about the source of funds being deposited. This information was entered when the deposit ticket was created, as required by the Account Provider. It can vary from Account Provider to Account Provider.  
createdTimeStamp | **string.** The date and time that the deposit ticket was created, in Microsoft Ticks format. All dates and times are UTC.  
lastupdateTimeStamp | **string.** The date and time stamp that the deposit ticket last was updated, in Microsoft Ticks format. All dates and times are UTC.  
comments | **string.** Any comment appended to the deposit ticket.  
attachments | **string.** Any attachment to the deposit ticket.  
  
## GetWithdrawFee

**Category:** User  
**Permissions:** Operator, Trading, Withdraw  
**Call Type:** Synchronous

Gets an estimate of a fee for a withdrawal. The Products function of the AlphaPoint Admin can set withdraw fees OMS-wide. You can also set a withdraw fee programmatically using **SetOMSFee,** but **SetOMSFee** is a System (not User) call with permission reserved to an exchange operator. Exchange-wide withdrawal fees cannot be overridden.

A user with Trading or Withdraw permissions can obtain withdrawal fee estimates only for products and accounts with which the user is associated; a user with Operator permission can obtain withdrawal fee estimates for any product or account.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "ProductId": 1,
        "Amount": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System trading the product.  
AccountId | **integer.** The ID of the account making the withdrawal.  
ProductId | **integer.** The ID of the product intended to be withdrawn. Fees may vary with product.  
Amount | **real.** The amount of product intended to be withdrawn.  
  
### Response
    
    
    {
        "FeeAmount":1.06
    }
    

Key | Value  
---|---  
FeeAmount | **real.** The estimated amount of the fee for the indicated withdrawal.  
  
## GetWithdraws

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns a list of withdrawals for a given account ID.

Users with Trading permission can return withdrawals only for an account with which they are associated; users with Operator permission can return withdrawals for any account.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System on which the withdrawal was issued.  
AccountId | **integer.** The ID of the account for which withdrawal information will be returned.  
  
### Response
    
    
    [
        {
            "amount": 0.0,
            "feeAmount": 0.0,
            "notionalValue": 0.0,
            "withdrawId": 0,
            "assetManagerId": 0,
            "accountId": 0,
            "assetId": 0,
            "templateForm": "{
                âTemplateTypeâ: âTetherRPCWithdrawâ,
                âCommentâ: âTestWithdrawâ,
                âExternalAddressâ: âms6C3pKAAr8gRCcnVebs8VRkVrjcvqNYv3â 
                }",
            "templateFormType": "TetherRPCWithdraw",
            "omsId": 0,
            "TicketStatus": 0,
            "ticketNumber": 0,
            "WithdrawTransactionDetails": "",
            "withdrawType": "",
            "withdrawCode": "490b4fa3-53fc-44f4-bd29-7e16be86fba3",
            "AssetType": 0,
            "reaccepted": true,
            "notionalProductId": 0
    
        },
    ]
    

The Response is an array of withdrawals made on the specified Order Management System for the specified account.

Key | Value  
---|---  
amount | **real.** The amount of product or fractions of product being withdrawn (not the dollar value, unless the products being withdrawn are dollars).  
feeAmount | **real.** The amount of withdrawal fee charged. Withdrawal fees usually are charged in the product being withdrawn.  
notionalValue | **real.** In some regions, withdrawals in cryptocurrency must first be converted to the local currency. Thus, the "notional value" of a withdrawal is the value of the cryptocurrency expressed in the local fiat currency.  
withdrawId | **integer.** The ID of this withdrawal, assigned by the system.  
assetManagerId | **integer.** The ID of the Asset Manager through which the withdrawal was made.  
accountId | **integer.** The ID of the account from which the withdrawal was made.  
assetId | **integer.** The ID of the asset (product) being withdrawn.  
templateform | **string.** The contents of the withdrawal template (key-value pairs). Templates vary from Account Provider to Account Provider, depending on the asset being withdrawn and the identity of the Account Provider.  
templateFormType | **string.** The name of the withdrawal template. The template controls the destination of the asset being withdrawn. To get a list of withdrawal templates available to you, call **GetWithdrawTemplateTypes.**  
omsId | **integer.** The ID of the Order Management System on which the withdrawal occurred.  
TicketStatus | **integer.** The current status of the withdrawal ticket. Some of these statuses are valid only for cryptocurrency withdrawals (which uses an automated withdrawal process), and some are valid for fiat currency withdrawals (which requires a human admin operator). Some of these statuses are used by the AlphaPoint Exchange internally, yet they may appear on a returned withdrawal ticket.  
  
**Withdraw ticket statuses:**  
**0** New (awaiting operator review)  
**1** AdminProcessing (An admin is looking at the ticket)  
**2** Accepted (withdrawal will proceed)  
**3** Rejected (admin or automatic rejection)  
**4** SystemProcessing (automatic processing underway)  
**5** FullyProcessed (the withdrawal has concluded)  
**6** Failed (the withdrawal failed for some reason)  
**7** Pending (the admin has placed the withdrawal in pending status)  
**8** Pending2Fa (user must click 2-factor authentication confirmation link)  
**9** AutoAccepted (withdrawal will be automatically processed)  
**10** Delayed (waiting for funds to be allocated for the withdrawal)  
**11** UserCanceled (withdraw canceled by user or Superuser)  
**12** AdminCanceled (withdraw canceled by Superuser)  
**13** AmlProcessing (anti-money-laundering process underway)  
**14** AmlAccepted (anti-money-laundering process complete)  
**15** AmlRejected (withdrawal did not stand up to anti-money-laundering process)  
**16** AmlFailed (withdrawal did not complete anti-money-laundering process)  
**17** LimitsAccepted (withdrawal meets limits for fiat or crypto asset)  
**18** LimitsRejected (withdrawal does not meet limits for fiat or crypto asset)  
**19** Submitted (withdrawal sent to Account Provider; awaiting blockchain confirmation)  
**20** Confirmed (Account Provider confirms that withdrawal is on the blockchain)  
**21** ManuallyConfirmed (admin has sent withdrawal via wallet or admin function directly; marks ticket as FullyProcessed; debits account)  
**22** Confirmed2Fa (user has confirmed withdraw via 2-factor authentication.)  
ticketNumber | **integer.** The number of the ticket, as assigned by the system (different from the ID of the withdrawal).  
withdrawTransactionDetails | **JSON string object.** Dynamic information that changes from Account Provider to Account Provider. The values of _withdrawTransactionDetails_ may (but do not have to) include key-value pairs for:  
**TxId** transaction ID  
**ExternalAddress**  
**Amount**  
**Confirmed**  
**LastUpdated**  
**TimeSubmitted**  
**AccountProviderName**  
withdrawType | **string.** Shows whether the withdrawal is cryptocurrency or fiat (national) currency.  
withdrawCode | **string.** A GUID that uniquely identifies the withdrawal (as opposed to the ticket representing the withdrawal). The value for _widrawCode_ is the same as _requestCode_ as returned by **GetWithdrawTicket** and **GetWithdrawTickets.**  
AssetType | **integer.** Describes the nature of the product. One of:  
**0** Unknown (an error condition)  
**1** NationalCurrency  
**2** CryptoCurrency  
**3** Contract  
reaccepted | **Boolean.** If a ticket was initially rejected, but later accepted for withdrawal, _true_ shows that the ticket was re-accepted for processing after an initial rejection.  
notionalProductId | **integer.** In those regions where withdrawal of cryptocurrency must be expressed in terms of local fiat currency, the _notionalProductId_ expresses that local currency.  
  
## GetWithdrawTicket

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns a single withdrawal ticket that matches all values in the Request. No optional fields; partial matches are not returned.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "RequestCode": "1d3d01eb-9e7b-47e0-9056-db420bf157ee"
    }
    

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System through which the withdrawal was made.  
AccountId | **integer.** The ID of the Account from which the withdrawal was made.  
RequestCode | **string.** The GUID assigned by the system to the withdraw ticket on creation. The call **GetWithdrawTickets** can return a set of _RequestCode_ values to allow you to zero-in on an unknown ticket _RequestCode._  
  
### Response
    
    
    {
      "assetManagerId": 0,
      "accountId": 0,
      "assetId": 0,
      "assetName": "",
      "amount": 0.0,
      "templateForm": "{
         âTemplateTypeâ: âTetherRPCWithdrawâ,
         âCommentâ: âTestWithdrawâ,
         âExternalAddressâ: âms6C3pKAAr8gRCcnVebs8VRkVrjcvqNYv3â, 
         }",
       "templateFormType": "ThetherRPCWithdraw",
       "omsId": 0,
       "requestCode": "490b4fa3-53fc-44f4-bd29-7e16be86fba3",
       "requestIP": "",
       "requestUserId": 0,
       "requestUserName": "",
       "operatorId": 0,
       "Status": 0,
       "feeAmt": 0.0,
       "updatedByUser": 0,
       "updatedByUserName": "",
       "ticketNumber": 0,
       "createdTimestamp": "0001-01-01T00:00:00",
       "lastUpdateTimestamp": "0001-01-01T00:00:00",
       "Comments": "[
          {
            "commentId": 0,
            "enteredBy": 0,
            "enteredDateTime": "0001-01-01T00:00:00",
            "comment": "",
            "operatorId": 0,
            "omsId": 0,
            "ticketCode": "",
            "ticketId": 0
           }
         ]",
        "Attachments": "[
           {
             "attachmentId": 0,
             "submittedByUserId": 0,
             "submittedByUserName": "",
             "uploadDate": "0001-01-01T00:00:00",
             "uploadIP": "",
             "ticketNumber": 0
            }
         ]",
        "AuditLog": "[]"
    }
    

Key | Value  
---|---  
assetManagerId | **integer.** The ID of the Asset Manager through which the withdrawal was made.  
accountId | **integer.** The ID of the account that made the withdrawal.  
assetId | **integer.** The ID of the asset (product) that was withdrawn. Withdrawal fees (if any) are usually assessed in the same asset that was withdrawn.  
assetName | **string.** The short name of the asset. For example, BTC for BitCoin or USD for US Dollars.  
amount | **real.** The number of units or fractions of units of the asset that were withdrawn (not the asset's monetary value). For example, 2.5 BitCoin or 2018.00 US Dollars.  
templateForm | **JSON string object.** The contents of the template form vary from Account Provider to Account Provider depending on the asset being withdrawn and the identity of the Account Provider. The Response returns this information as a string, not an object.  
templateFormType | **string.** The name of the template being used. Templates vary from Account Provider to Account Provider.  
omsId | **integer.** The ID of the Order Management System on which the withdrawal was made.  
requestCode | **string.** A globally unique identifier (GUID) that identifies this specific withdrawal.  
requestIP | **string.** The IP address from which the withdrawal was initiated.  
requestUserId | **integer.** The user ID of the user who submitted the withdrawal.  
requestUserName | **string.** The user name of the user who submitted the withdrawal. For example, jsmith.  
operatorId | **integer.** The ID of the administrator (operator) who processed the withdrawal. Withdrawals of cryptocurrency are handled automatically; withdrawals of fiat (national) currency are approved by a human operator.  
Status | **integer.** The current status of the withdrawal ticket. Some of these statuses are valid only for cryptocurrency withdrawals, which uses an automated withdrawal process, and some are valid for fiat currency withdrawals, which requires a human admin (operator). Some of these statuses are used by AlphaPoint internally, yet they may appear on a returned Withdraw Ticket.  
  
**Withdraw ticket statuses:**  
**0** New (awaiting operator review)  
**1** AdminProcessing (An admin is looking at the ticket)  
**2** Accepted (withdrawal will proceed)  
**3** Rejected (admin or automatic rejection)  
**4** SystemProcessing (automatic processing underway)  
**5** FullyProcessed (the withdrawal has concluded)  
**6** Failed (the withdrawal failed for some reason)  
**7** Pending (the admin has placed the withdrawal in pending status)  
**8** Pending2Fa (user must click 2-factor authentication confirmation link)  
**9** AutoAccepted (withdrawal will be automatically processed)  
**10** Delayed (waiting for funds to be allocated for the withdrawal)  
**11** UserCanceled (withdraw canceled by user or Superuser)  
**12** AdminCanceled (withdraw canceled by Superuser)  
**13** AmlProcessing (anti-money-laundering process underway)  
**14** AmlAccepted (anti-money-laundering process complete)  
**15** AmlRejected (withdrawal did not stand up to anti-money-laundering process)  
**16** AmlFailed (withdrawal did not complete anti-money-laundering process)  
**17** LimitsAccepted (withdrawal meets limits for fiat or crypto asset)  
**18** LimitsRejected (withdrawal does not meet limits for fiat or crypto asset)  
**19** Submitted (withdrawal sent to Account Provider; awaiting blockchain confirmation)  
**20** Confirmed (Account Provider confirms that withdrawal is on the blockchain)  
**21** ManuallyConfirmed (admin has sent withdrawal via wallet or admin function directly; marks ticket as FullyProcessed; debits account)  
**22** Confirmed2Fa (user has confirmed withdraw via 2-factor authentication.)  
feeAmt | **real.** The amount of any fee that was charged for the withdrawal. _feeAmt_ is always denominated in the asset or product that was withdrawn.  
updatedByUser | **integer.** The user ID of the most recent user who may have updated the withdrawal ticket. This user is usually an admin (operator).  
updatedByUserName | **string.** The user name of the most recent user who may have updated the withdrawal ticket. This user is usually an admin (operator).  
ticketNumber | **integer.** The number of the ticket, as assigned by the system.  
createdTimeStamp | **string.** The time and date when the withdrawal ticket was created, in Microsoft Ticks format. All times and dates are UTC.  
lastUpdateTimeStamp | **string.** The time and date when the withdrawal ticket was last updated, in Microsoft Ticks format. All times and dates are UTC.  
Comments | **array of JSON string objects.** An array of key-value pairs appended as comments to the withdrawal ticket. See _Comments_ example.  
Attachments | **array of JSON string objects.** An array of any attachments appended to the withdrawal ticket. See _Attachments_ example.  
AuditLog | **array of JSON string objects.** Reserved for future use.  
  
#### Comments Example

> Comments Example
    
    
    "Comments":"[
                {
                "commentId": 0,
                "enteredBy": 0,
                "enteredDateTime": "0001-01-01T00:00:00",
                "comment": "",
                "operatorId": 0,
                "omsId": 0,
                "ticketCode": "",
                "ticketId": 0
                }
            ]",
    

Comments appear as an array.

Key | Value  
---|---  
commentId | **integer.** The ID assigned to the comment by the system.  
enteredBy | **integer.** The ID of the user who entered the comment.  
enteredDateTime | **string.** The time and date that the comment was entered, in Microsoft Ticks format. All times and dates are UTC.  
comment | **string.** The text of the comment.  
operatorId | **integer.** The ID of the admin (operator) making the comment.  
omsId | **integer.** The ID of the Order Management System where the withdrawal ticket and comment were created. (They are unlikely to be different).  
ticketCode | **string.** A globally unique ID (GUID) assigned by the system that identifies the ticket.  
ticketId | **integer.** The ID of the ticket as assigned by the system.  
  
#### Attachments Example

> Attachments Example
    
    
    "Attachments":"[
                {
                "attachmentId": 0,
                "submittedByUserId": 0,
                "submittedByUserName": "",
                "uploadDate": "0001-01-01T00:00:00",
                "uploadIP": "",
                "ticketNumber": 0
                }
            ]",
    

Any attachments appear as an array.

Key | Value  
---|---  
attachmentId | **integer.** The ID assigned to the attachment by the system.  
submittedByUserId | **integer.** The user ID of the person who added the attachment to the withdrawal ticket.  
submittedByUserName | **integer.** The user name of the person who submitted the attachment.  
uploadDate | **string.** The date and time that the attachment was uploaded, in Microsoft Ticks format. All times and dates are UTC.  
uploadIP | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The number of the withdrawal ticket, as assigned by the system.  
  
## GetWithdrawTicketAttachment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Retrieves an attachment from a withdrawal ticket.

### Request
    
    
    {
        "attachmentId": 0
    }
    

Key | Value  
---|---  
attachmentId | **integer.** The ID of the specific attachment you want to retrieve. You can use the call **GetWithdrawTicket** to return any attachments appended to a specific ticket and learn the _attachmentId_ if you don't already have it.  
  
### Response
    
    
    {
        "base64Attachment": "",
        "attachmentId": 0,
        "submittedByUserId": 0,
        "submittedByUserName": "",
        "uploadDate": "0001-01-01T00:00:00",
        "uploadIP": "",
        "ticketNumber": 0,
        "description": ""
    }
    

Key | Value  
---|---  
base64Attachment | **string.** The attachment file. May be PDF, spreadsheet, blob, or other.  
attachmentId | **integer.** The ID assigned to the attachment by the system. Echoes the ID in the Request.  
submittedByUserId | **integer.** The user ID of the person who added the attachment to the withdrawal ticket.  
submittedByUserName | **string.** The user name of the person who submitted the attachment.  
uploadDate | **string.** The date and time that the attachment was uploaded, in Microsoft Ticks format. All dates and times are UTC.  
uploadIP | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The number of the withdrawal ticket, as assigned by the system.  
  
## GetWithdrawTickets

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Returns a limited array of withdrawal tickets from the specified Order Management System and account.

**GetWithdrawTickets** is usable with Operator and Trading permissions. It returns tickets from a single account. A similar call, **GetAllWithdrawTickets,** can be used only with Operator permission and returns tickets from all accounts.

### Request
    
    
    {
        "OMSId": 1,
        "AccountId": 1,
        "StartIndex": 0,
        "Limit": 200
    }
    

The key-value pairs _StartIndex_ and _Limit_ are optional. The oldest ticket is ticket _0_. This differs from other calls where the newest ticket is ticket _0._ The value of _StartIndex_ is a pointer into the stream of withdrawal tickets, and the value of _Limit_ shows how far into the past (towards ticket _0_) to return tickets. For example, if there are 1500 current tickets (oldest ticket _0_ through newest ticket _1499_), _StartIndex_ = 100, and _Limit_ = 100; then **GetWithdrawTickets** would return ticket numbers 1399 through 1300.

Key | Value  
---|---  
OMSId | **integer.** The ID of the Order Management System where the withdrawal tickets reside.  
AccountId | **integer.** The ID of the account from which the withdrawals were made. A user with Operator permission can return withdrawal tickets for any account; a user with Trading permission can return withdrawal tickets only for an account with which that user is associated.  
StartIndex | **integer.** OPTIONAL A pointer into the stream of withdrawal tickets. The oldest ticket is ticket _0._ The default value for _StartIndex_ is _0._  
Limit | **integer.** OPTIONAL The number of withdrawal tickets to return, beginning at the ticket marked by _StartIndex._ The default value for _Limit_ is 200.  
  
### Response
    
    
    [
        {
            "assetManagerId": 0,
            "accountId": 0,
            "assetId": 0,
            "assetName": "",
            "amount": 0.0,
            "templateForm": "{
                âTemplateTypeâ: âTetherRPCWithdrawâ,
                âCommentâ: âTestWithdrawâ,
                âExternalAddressâ: âms6C3pKAAr8gRCcnVebs8VRkVrjcvqNYv3â, 
                }",
            "templateFormType": "ThetherRPCWithdraw",
            "omsId": 0,
            "requestCode": "490b4fa3-53fc-44f4-bd29-7e16be86fba3",
            "requestIP": "",
            "requestUserId": 0,
            "requestUserName": "",
            "operatorId": 0,
            "Status": 0,
            "feeAmt": 0.0,
            "updatedByUser": 0,
            "updatedByUserName": "",
            "ticketNumber": 0,
            "createdTimestamp": "0001-01-01T00:00:00",
            "lastUpdateTimestamp": "0001-01-01T00:00:00",
            "Comments": "[
                    {
                    "commentId": 0,
                    "enteredBy": 0,
                    "enteredDateTime": "0001-01-01T00:00:00",
                    "comment": "",
                    "operatorId": 0,
                    "omsId": 0,
                    "ticketCode": "",
                    "ticketId": 0
                    }
                ]",
            "Attachments": "[
                    {
                    "attachmentId": 0,
                    "submittedByUserId": 0,
                    "submittedByUserName": "",
                    "uploadDate": "0001-01-01T00:00:00",
                    "uploadIP": "",
                    "ticketNumber": 0
                    }
                ]",
            "AuditLog": "[]"
        }
    ]
    

The Response is an array of detail information about the withdrawal.

Key | Value  
---|---  
assetManagerId | **integer.** The ID of the Asset Manager through which the withdrawal was made.  
accountId | **integer.** The ID of the account that made the withdrawal.  
assetId | **integer.** The ID of the asset (product) that was withdrawn. Withdrawal fees (if any) are usually assessed in the same asset that was withdrawn.  
assetName | **string.** The short name of the asset. For example, BTC for BitCoin or USD for US Dollars.  
amount | **real.** The number of units or fractions of units of the asset that were withdrawn (not the asset's monetary value). For example, 2.5 BitCoin or 2018.00 US Dollars.  
templateForm | **JSON string object.** The contents of the template form vary from Account Provider to Account Provider depending on the asset being withdrawn and the identity of the Account Provider. The Response returns this information as a string.  
templateFormType | **string.** The name of the template being used. Templates vary from Account Provider to Account Provider.  
omsId | **integer.** The ID of the Order Management System on which the withdrawal was made.  
requestCode | **string.** A globally unique identifier (GUID) that identifies this specific withdrawal.  
requestIP | **string.** The IP address from which the withdrawal was initiated.  
requestUserId | **integer.** The user ID of the user who submitted the withdrawal.  
requestUserName | **string.** The user name of the user who submitted the withdrawal. For example, jsmith.  
operatorId | **integer.** The ID of the administrator (operator) who processed the withdrawal. Withdrawals of cryptocurrency are handled automatically; withdrawals of fiat (national) currency are approved by a human operator.  
Status | **integer.** The current status of the withdrawal ticket. Some of these statuses are valid only for cryptocurrency withdrawals, which uses an automated withdrawal process, and some are valid for fiat currency withdrawals, which requires a human admin (operator). Some of these statuses are used by AlphaPoint internally, yet they may appear on a returned Withdraw Ticket.  
  
**Withdraw ticket statuses:**  
**0** New (awaiting operator review)  
**1** AdminProcessing (An admin is looking at the ticket)  
**2** Accepted (withdrawal will proceed)  
**3** Rejected (admin or automatic rejection)  
**4** SystemProcessing (automatic processing underway)  
**5** FullyProcessed (the withdrawal has concluded)  
**6** Failed (the withdrawal failed for some reason)  
**7** Pending (the admin has placed the withdrawal in pending status)  
**8** Pending2Fa (user must click 2-factor authentication confirmation link)  
**9** AutoAccepted (withdrawal will be automatically processed)  
**10** Delayed (waiting for funds to be allocated for the withdrawal)  
**11** UserCanceled (withdraw canceled by user or Superuser)  
**12** AdminCanceled (withdraw canceled by Superuser)  
**13** AmlProcessing (anti-money-laundering process underway)  
**14** AmlAccepted (anti-money-laundering process complete)  
**15** AmlRejected (withdrawal did not stand up to anti-money-laundering process)  
**16** AmlFailed (withdrawal did not complete anti-money-laundering process)  
**17** LimitsAccepted (withdrawal meets limits for fiat or crypto asset)  
**18** LimitsRejected (withdrawal does not meet limits for fiat or crypto asset)  
**19** Submitted (withdrawal sent to Account Provider; awaiting blockchain confirmation)  
**20** Confirmed (Account Provider confirms that withdrawal is on the blockchain)  
**21** ManuallyConfirmed (admin has sent withdrawal via wallet or admin function directly; marks ticket as FullyProcessed; debits account)  
**22** Confirmed2Fa (user has confirmed withdraw via 2-factor authentication.)  
feeAmt | **real.** The amount of any fee that was charged for the withdrawal. _feeAmt_ is always denominated in the asset or product that was withdrawn.  
updatedByUser | **integer.** The user ID of the most recent user who may have updated the withdrawal ticket. This user is usually an admin (operator).  
updatedByUserName | **string.** The user name of the most recent user who may have updated the withdrawal ticket. This user is usually an admin (operator).  
ticketNumber | **integer.** The number of the ticket, as assigned by the system.  
createdTimeStamp | **string.** The time and date when the withdrawal ticket was created, in Microsoft Ticks format. All times and dates are UTC.  
lastUpdateTimeStamp | **string.** The time and date when the withdrawal ticket was last updated, in Microsoft Ticks format. All times and dates are UTC.  
Comments | **array of JSON string objects.** An array of key-value pairs appended as comments to the withdrawal ticket. See _Comments_ example.  
Attachments | **array of JSON string objects.** An array of any attachments appended to the withdrawal ticket. See _Attachments_ example.  
AuditLog | **array of JSON string objects.** Reserved for future use.  
  
#### Comments Example

> Comments Example
    
    
    "Comments":"[
                {
                "commentId": 0,
                "enteredBy": 0,
                "enteredDateTime": "0001-01-01T00:00:00",
                "comment": "",
                "operatorId": 0,
                "omsId": 0,
                "ticketCode": "",
                "ticketId": 0
                }
            ]",
    

Comments appear as an array.

Key | Value  
---|---  
commentId | **integer.** The ID assigned to the comment by the system.  
enteredBy | **integer.** The ID of the user who entered the comment.  
enteredDateTime | **string.** The time and date that the comment was entered, in Microsoft Ticks format. All times and dates are UTC.  
comment | **string.** The text of the comment.  
operatorId | **integer.** The ID of the admin (operator) making the comment.  
omsId | **integer.** The ID of the Order Management System where the withdrawal ticket and comment were created. (They are unlikely to be different).  
ticketCode | **string.** A globally unique ID (GUID) assigned by the system that identifies the ticket.  
ticketId | **integer.** The ID of the ticket as assigned by the system.  
  
#### Attachments Example

> Attachments Example
    
    
    "Attachments":"[
                {
                "attachmentId":0,
                "submittedByUserId":0,
                "submittedByUserName":"",
                "uploadDate":"0001-01-01T00:00:00",
                "uploadIP":"",
                "ticketNumber":0
                }
            ]",
    

Any attachments appear as an array.

Key | Value  
---|---  
attachmentId | **integer.** The ID assigned to the attachment by the system.  
submittedByUserId | **integer.** The user ID of the person who added the attachment to the withdrawal ticket.  
submittedByUserName | **integer.** The user name of the person who submitted the attachment.  
uploadDate | **string.** The date and time that the attachment was uploaded, in Microsoft Ticks format. All times and dates are UTC.  
uploadIP | **string.** The IP address from which the attachment was uploaded.  
ticketNumber | **long integer.** The number of the withdrawal ticket, as assigned by the system.  
  
## SubmitDepositTicketComment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Creates a comment and attaches that comment to a specific deposit ticket.

### Request
    
    
    {
        "commentId": 0,
        "enteredBy": 0,
        "enteredDateTime": "0001-01-01T00:00:00",
        "comment": "",
        "operatorId": 0,
        "omsId": 0,
        "ticketCode": "43d1a9f0-8dc3-46f9-b457-297c800d8c9c",
        "ticketId": 0
    }
    

Key | Value  
---|---  
commentId | **integer.** The ID of this specific comment. In the Request, set this to 0. The Response supplies the system-assigned value for _commentId._  
enteredBy | **integer.** The user ID of the user making the comment. If an operator (admin) is making the request, this should be the generic user ID of the admin (not the operator ID).  
enteredDateTime | **string.** The date and time that the comment was created, in Microsoft Ticks format and UTC time.  
comment | **string.** The comment string itself.  
operatorId | **integer.** The ID of an operator (admin) making the comment. The value for _operatorId_ should be available programmatically from the ticket being commented.  
omsId | **integer.** The ID of the Order Management System on which the deposit is being made.  
ticketCode | **string.** A GUID (globally unique identifier) that identifies the deposit ticket to which the comment is attached. The value for _ticketCode_ should be available programmatically from the ticket being commented.  
ticketId | **integer.** An ID assigned by the system to the ticket. You can obtain this value from the calls **CreateDepositTicket,** **GetAllDepositTickets,** **GetDepositTicket,** and **GetDepositTickets.** In all these calls, the key is named _ticketNumber._  
  
### Response
    
    
    {
        "success": true,
        "commentid": 10000002
    }
    

Key | Value  
---|---  
success | **Boolean.** A _true_ value means that the comment has been successfully attached to the deposit ticket; _false_ means that it has not been attached.  
commentId | **integer.** The ID assigned by the system to this specific comment.  
  
## SubmitWithdrawTicketComment

**Category:** System  
**Permissions:** Operator, Trading  
**Call Type:** Synchronous

Creates a comment and attaches that comment to a specific withdrawal ticket.

### Request
    
    
    {
        "commentId": 0,
        "enteredBy": 0,
        "enteredDateTime": "0001-01-01T00:00:00",
        "comment": "",
        "operatorId": 0,
        "omsId": 0,
        "ticketCode": "43d1a9f0-8dc3-46f9-b457-297c800d8c9c",
        "ticketId": 0
    }
    

Key | Value  
---|---  
commentId | **integer.** The ID of this specific comment. In the Request, set this to 0. The Response supplies the system-assigned value for _commentId._  
enteredBy | **integer.** The user ID of the user making the comment. If an operator (admin) is making the request, this should be the generic user ID of the admin (not the operator ID).  
enteredDateTime | **string.** The date and time that the comment was created, in Microsoft Ticks format and UTC time.  
comment | **string.** The comment string itself.  
operatorId | **integer.** The ID of an operator (admin) making the comment. The value for _operatorId_ should be available programmatically from the ticket being commented.  
omsId | **integer.** The ID of the Order Management System on which the withdrawal is being made.  
ticketCode | **string.** A GUID (globally unique identifier) that identifies the withdrawal ticket to which the comment is attached. The value for _ticketCode_ should be available programmatically from the ticket being commented.  
ticketId | **integer.** An ID assigned by the system to the ticket. You can obtain this value from the calls **GetWithdrawTicket,** **GetAllWithdrawTickets,** and **GetWithdrawTickets.** In all these calls, the key is named _ticketNumber._  
  
### Response
    
    
    {
        "success": true,
        "commentid": 10000002
    }
    

Key | Value  
---|---  
success | **Boolean.** A _true_ value means that the comment has been successfully attached to the withdrawal ticket; _false_ means that it has not been attached.  
commentId | **integer.** The ID assigned by the system to this specific comment.  
  
# Miscellaneous

These are User-category calls that don't fit well into the Admin Guide organization.

## GetEarliestTickTime

**Category:** User  
**Permissions:** Operator, Level1MarketData  
**Call Type:** Synchronous

Gets the earliest ticker reading of the trading day.

Users with Level1MarketData permission can obtain the earliest tick time only for an instrument they have permission to trade; users with Operator permission can get earliest tick time for any instrument.

### Request
    
    
    {
        "InstrumentId": 1,
        "OMSId": 1
    }
    

Key | Value  
---|---  
InstrumentId | **integer.** The ID of an instrument on the Order Management System for which the earliest ticker time is being requested.  
OMSId | **integer** The ID of the Order Management System that will return the earliest ticker time of the day.  
  
### Response
    
    
    [
        1501603632000 \\DateTime - UTC - Milliseconds since 1/1/1970 
    ]
    

Despite the array brackets, the response returns a single value.

Key | Value  
---|---  
1501603632000 | **long integer** Time of the earliest ticker tick, in POSIX format and UTC.  
  
## Ticker

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

The ticker endpoint is to provide a 24-hour pricing and volume summary for each market pair available on the exchange.

### Request

This endpoint doesnt require any request parameters

### Response
    
    
    {
        "BTC_CAD": {
             "base_id": 1,
             "quote_id": 8564,
             "last_price": 75854.93,
             "base_volume": 66.621310000000000000000000000,
             "quote_volume": 5127348.6661163000000000000000,
        },
    }
    

The response returns JSON objects with the following key/value pair 

Key | Value  
---|---  
base_id | **integer** The quote pair Unified Cryptoasset ID.  
quote_id | **integer** The base pair Unified Cryptoasset ID.  
last_price | **decimal** Last transacted price of base currency based on given quote currency.  
base_volume | **decimal** 24-hour trading volume denoted in BASE currency.  
quote_volume | **decimal** 24 hour trading volume denoted in QUOTE currency.  
  
## Summary

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

The summary endpoint is to provide an overview of market data for all tickers and all market pairs on the exchange.

### Request

This endpoint doesnt require any request parameters

### Response
    
    
    [
        {
            "trading_pairs": "BTC_CAD",
            "last_price": 75925.37,
            "lowest_ask": 75926.63,
            "highest_bid": 66.435340000000000000000000000,
            "base_volume": 75774.93,
            "quote_volume": 5112197.7830825000000000000000,
            "price_change_percent_24h": -5.3894893561980828521107542600,
            "highest_price_24h": 79813.51,
            "lowest_price_24h": 73700.01
        },
    ]
    

The response returns an array of JSON objects with the following key/value pair 

Key | Value  
---|---  
trading_pairs | **string** Identifier of a ticker with delimiter to separate base/quote, eg. BTC-USD (Price of BTC is quoted in USD).  
last_price | **decimal** Last transacted price of base currency based on given quote currency.  
lowest_ask | **decimal** Lowest Ask price of base currency based on given quote currency.  
highest_bid | **decimal** Highest bid price of base currency based on given quote currency.  
base_volume | **decimal** 24-hr volume of market pair denoted in BASE currency.  
quote_volume | **decimal** 24-hr volume of market pair denoted in QUOTE currency.  
price_change_percent_24h | **decimal** 24-hr % price change of market pair.  
highest_price_24h | **decimal** Highest price of base currency based on given quote currency in the last 24-hrs.  
lowest_price_24h | **decimal** Lowest price of base currency based on given quote currency in the last 24-hrs.  
  
## Ping

**Category:** User  
**Permissions:** Public  
**Call Type:** Synchronous

Used to keep a connection alive.

### Request
    
    
    { }
    

Ping requires no payload.

### Response
    
    
    PONG
    

Response is PONG.

[json](#)
