# Itbit API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://api.itbit.com/docs

[__  Back to top](#top)

 __

[Message Types](#message-types)

  * [Logon](#message-types-logon)
  * [Logon with Reset Seq Num](#message-types-logon-with-reset-seq-num)
  * [Replay Messages](#message-types-replay-messages)
  * [Heartbeat](#message-types-heartbeat)
  * [New Order](#message-types-new-order)
  * [Order Cancel Request](#message-types-order-cancel-request)
  * [Order Cancel Reject](#message-types-order-cancel-reject)
  * [Order Status Request](#message-types-order-status-request)
  * [Execution Report - Pending New](#message-types-execution-report-pending-new)
  * [Execution Report - New](#message-types-execution-report-new)
  * [Execution Report - Filled](#message-types-execution-report-filled)
  * [Execution Report - Expired](#message-types-execution-report-expired)
  * [Execution Report - Partial Fill](#message-types-execution-report-partial-fill)
  * [Execution Report - Pending Cancel](#message-types-execution-report-pending-cancel)
  * [Execution Report - Canceled](#message-types-execution-report-canceled)
  * [Execution Report - Order Reject](#message-types-execution-report-order-reject)
  * [Execution Report - Order Status](#message-types-execution-report-order-status)
  * [Logout](#message-types-logout)



 __

[Encoded Tags](#encoded-tags)

  * [1\. MsgType:](#header-1.-msgtype-)
  * [2\. ExecType](#header-2.-exectype)



# FIX API Reference

FIX (Financial Information eXchange) is an electronic messaging protocol widely adopted by financial institutions to transmit trading activity such as submitting or canceling orders and receiving execution information. The API is based on FIX 4.2 and modeled after common forex FIX implementations.

### Just Getting Started?

Check out the [Onboarding](https://docs.paxos.com/fix/onboard) guide in the [FIX documentation](https://docs.paxos.com/fix).

## Message Types [¶](#message-types)

The supported message types and corresponding fields are listed in this section. The required fields outside of the standard headers for the message type are highlighted.

### Logon [ ¶](#message-types-logon)

A FIX session is initiated by the client with a Logon message. EncryptedMethod (FIX tag 98) must be set to 0. HeartBtInt (108) needs to be set, the default value is 30 seconds.

#### Message Format [¶](#header-message-format)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 72 |   
35 | MsgType |  | A | Logon  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 1 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
10 | CheckSum |  | 078 |   
  
**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 72 |   
35 | MsgType |  | A | Logon  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 1 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
10 | CheckSum |  | 078 |   
  
### Logon with Reset Sequence Number Flag[ ¶](#message-types-logon-with-reset-seq-num)

The API supports client initiated message sequence number resets via Logon with ResetSeqNumFlag (141) set to Y.

Note: We recommend implementing a [sequence number management](https://docs.paxos.com/crypto-brokerage/fix/best-practices#sequence-number-management) strategy to promote a stable trading environment for everyone.

#### Message Format [¶](#header-message-format-1)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 78 |   
35 | MsgType |  | A | Logon  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 1 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
141 | ResetSeqNumFlag | Y | Y | Yes, reset sequence numbers on both sides of the FIX connection  
10 | CheckSum |  | 133 |   
  
**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 78 |   
35 | MsgType |  | A | Logon  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 1 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
141 | ResetSeqNumFlag | Y | Y | Yes, reset sequence numbers on both sides of the FIX connection  
10 | CheckSum |  | 017 |   
  
### Replay Messages [ ¶](#message-types-replay-messages)

Replay messages, also known as resend request, logic is the session mechanism used to request a range of ordered messages be sent from the counterparty. Replaying messages can be used to request a single message, a range of messages, or all messages subsequent to a particular message. For example, the receiving application sends the replay message to initiate the retransmission of messages if:

  * a gap in sequence numbers is detected,
  * the receiving application lost a message, or
  * higher than expected message sequence numbers are detected from the counterparty.



The counterparty then resends the requested message range sequentially until both systems are back in sequence.

#### Message Format [¶](#header-message-format-2)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
7 | BeginSeqNo | Y | To request a single message, BeginSeqNo <7> = EndSeqNo <16>  To request a range of messages: BeginSeqNo <7> = first message of range and EndSeqNo <16> = last message of range  To request all messages subsequent to a particular message, EndSeqNo <16> = 0 | Message sequence number of the first message in range to be resent  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 72 |   
16 | EndSeqNo | Y | To request a single message, BeginSeqNo <7> = EndSeqNo <16>  To request a range of messages: BeginSeqNo <7> = first message of range and EndSeqNo <16> = last message of range  To request all messages subsequent to a particular message, EndSeqNo <16> = 0 | Message sequence number of the first message in range to be resent  
35 | MsgType |  | 2 | Resend request  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 1 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
10 | CheckSum |  | 078 |   
  
**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
7 | BeginSeqNo | Y |  | Message sequence number of the first message in range to be resent  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 72 |   
16 | EndSeqNo | Y |  | Message sequence number of the first message in range to be resent  
35 | MsgType |  | 2 | Unsent execution reports  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 1 |   
43 | PossDupFlag |  | Y | Indicates possible retransmission of message with this sequence number  
122 | OrigSendingTime |  | 20220818-15:40:52 | Original time of message transmission when transmitting orders as the result of a resend request  
52 | SendingTime |  | 20150607-15:43:16.543 |   
98 | EncryptedMethod | Y | 0 | Method of encryption  
108 | HeartBtInt | Y | 30 |   
10 | CheckSum |  | 078 |   
  
### Heartbeat [ ¶](#message-types-heartbeat)

In standard FIX, when either end of the FIX connection has not received a message in HeartBtInt (108) seconds, a heartbeat message will be transmitted (MsgType 0). As noted above, the default value for HeartBtInt is 30 seconds.

The (Test Request 1) message forces a heartbeat from the opposing side. The (Test Request 1) message checks sequence numbers or verifies the connection status. The opposite side then responds to the (Test Request 1) with a (Heartbeat 0) containing the TestReqID (112).

The TestReqID (112) verifies that the opposite side is generating the heartbeat as the result of (Test Request 1) and not a normal timeout. The opposite side includes the TestReqID (112) in the resulting (Heartbeat 0). Any string can be used as the TestReqID (112) (one suggestion is to use a timestamp string).

During periods of inactivity, FIX clients should generate a heartbeat message at regular time intervals. The Heartbeat (0) message is used by a FIX client to monitor the status of the communication link. FIX clients should reset the heartbeat interval timer **after every transmitted message** (not just heartbeats). When the client stops receiving data for the specified heartbeat interval, it should send a (Test Request 1) message to verify the connection. The counterparty should send a (Heartbeat 0) message in response. If a party receives no (Heartbeat 0) message in a reasonable amount of time, the connection should be considered lost.

#### Message Format [¶](#header-message-format-2)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 60 |   
35 | MsgType | Y | 0 | Heartbeat  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 2 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
112 | TestReqID | Y | 20150607-15:43:16.543 | Test Request  
10 | CheckSum |  | 017 |   
  
**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0056 |   
35 | MsgType | Y | 0 | Heartbeat  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 2 |   
52 | SendingTime |  | 20150607-15:43:16.534 |   
112 | TestReqID | Y | 20150607-15:43:16.543 | Test Request  
10 | CheckSum |  | 185 |   
  
### Reject (Type 3) [ ¶](#message-types-reject-3)

The reject message should be issued when a message is received but cannot be properly processed due to a session-level rule violation.

#### Message Format [¶](#header-message-format-5)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0180 |   
35 | MsgType |  | 3 | Reject  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 221 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
45 | RefSeqNum |  | 44 | Reference message sequence number  
58 | Text |  |  | Text including reason for reject message  
373 | SessionRejectReason |  | 6 |   
10 | CheckSum |  | 112 |   
  
### New Order [ ¶](#message-types-new-order)

Orders should be submitted as New Order Single (MsgType D). The API currently supports market orders (OrdType 1), limit orders (OrdType 2), stop market orders (OrdType 3) and stop limit orders (OrdType 4). Price (44) must not be specified for market and stop market orders. In addition, market buy orders must include CashOrderQty (152), specifying the amount of fiat to convert to cryptocurrency. In the case of stop market and stop limit orders (currently only sell stop loss orders are supported), StopPx (99) needs to be provided. Market sell orders, stop market sell orders, stop limit sell orders, and all limit orders must specify OrderQty 38. HandlInst (21) must be set to with a value of 1. Along with the currency pair populated in Symbol (55), the SecurityType (167) must be set to FOR.

Note that limit orders for XBT and ETH have a tick size requirement. Price (44) for all XBT markets must be evenly divisible by 0.25, and for all ETH markets must be evenly divisible by 0.05. In addition, the maximum allowed notional value for a market order is 500,000 USD. The maximum allowed notional value for a limit order is 1,500,000 USD for XBTUSD and ETHUSD markets, and 1,000,000 USD for other markets.

Note: Limit Orders will be rejected if order is taker and price deviates a 15% or more from the midpoint.

#### Message Format [¶](#header-message-format-3)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 230 |   
35 | MsgType |  | D | Order Single  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 209 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
11 | ClOrdID | Y | Order_762 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
21 | HandlInst | Y | 1 | Automated execution order private no broker intervention  
55 | Symbol | Y | XBTUSD |   
167 | SecurityType | Y | FOR | Foreign Exchange Contract  
54 | Side | Y | 1 | 1 for Buy, 2 for Sell  
60 | TransactTime | Y | 20150607-15:43:16.543 |   
38 | OrderQty |  | 1 | Market Sell orders, Stop Market Sell orders, Stop Limit Sell orders, and all limit orders must specify OrderQty 38. Only 1 of tag 38 or tag 152 should be sent. Only supports float notation (ie. '1.005').  
152 | CashOrderQty |  |  | Required for Market Buy orders; the fiat value of the order  
40 | OrdType | Y | 2 | 1 for Market, 2 for Limit, 3 for Stop Market, 4 for Stop Limit  
18 | ExecInst |  | 6 | Optional (6) for Post-Only Limit orders  
44 | Price |  | 230 | Required for Limit and Stop Limit orders. Must conform to tick size - 0.25 for XBT markets and 0.05 for ETH markets  
99 | StopPx | Nn | 230n | Required for Stop Market and Stop Limit orders. Must conform to tick size - 0.25 for XBT markets and 0.05 for ETH markets  
59 | TimeInForce | N | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time). Limit orders can be set with a value of 1, 3, 4, or 6. Market orders can be set with a value of 3. Stop Market and Stop Limit orders can be set with a value of 1 or 6. The default values for Limit and Stop Market orders is 1, and for Market orders is 3.  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 185 |   
  
### Order Cancel Request [ ¶](#message-types-order-cancel-request)

Orders should referenced by their ClOrdID (11) and OrigClOrdID (41) Note that orders can be cancelled only after “New Order” confirmation

#### Message Format [¶](#header-message-format-4)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 257 |   
35 | MsgType |  | F | Order cancel request  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 210 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
41 | OrigClOrdID | Y | Order_762 |   
11 | ClOrdID | Y | Cancel763 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
55 | Symbol | Y | XBTUSD |   
167 | SecurityType | Y | FOR | Foreign Exchange Contract  
54 | Side | Y | 1 | Buy  
60 | TransactTime | Y | 20150607-15:43:16.543 |   
38 | OrderQty |  | 1 |   
152 | CashOrderQty |  |  |   
10 | CheckSum |  | 246 |   
  
### Order Cancel Reject [ ¶](#message-types-order-cancel-reject)

If an order can not be canceled, an Order Cancel Reject message will be sent to the client with CxRejReason (102) populated with a rejection reason

#### Message Format [¶](#header-message-format-5)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0180 |   
35 | MsgType |  | 9 | Order cancel reject  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 221 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
434 | CxlRejResponseTo | Y | 1 |   
11 | ClOrdID | Y | Cancel764 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
39 | OrdStatus | Y | 4 | Canceled  
41 | OrigClOrdID | Y | Order_762 |   
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
102 | CxlRejReason | Y | 0 | Too late to cancel  
10 | CheckSum |  | 112 |   
  
### Order Status Request [ ¶](#message-types-order-status-request)

Order Status Request (MsgType H) is used to query the current status of an order.

#### Message Format [¶](#header-message-format-6)

**Outgoing Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 170 |   
35 | MsgType |  | H | Order status request  
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 341 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
11 | ClOrdID | Y | Order_782 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
55 | Symbol | Y | XBTUSD |   
54 | Side | Y | 1 | Buy  
10 | CheckSum |  | 247 |   
  
### Execution Report - Pending New [ ¶](#message-types-execution-report-pending-new)

New Orders will return a Pending New Order Execution Report response (MsgType 8), (OrdStatus A).

#### Message Format [¶](#header-message-format-7)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 296 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 208 |   
52 | SendingTime |  | 20150607-15:43:16.500 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | A | Pending New  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
151 | LeavesQty | Y | 1 |   
12 | Commission | Y | 0.0 |   
60 | TransactTime | Y | 20150607-15:43:16.500 |   
58 | Text | Y | Pending New Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 0 |   
14 | CumQty | Y | 0 |   
13 | CommType | Y | 3 |   
11 | ClOrdID | Y | 1806809709 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 6000 |   
99 | StopPx | N | 6000 | Only returned when OrdType is 3 (Stop Market) or 4 (Stop Limit)  
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | 1806809709 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | A | Pending New  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 00000000-0000-0000-0000-000000000000 | All Zeros for pending new order  
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 224 |   
  
### Execution Report - New [ ¶](#message-types-execution-report-new)

New Orders will return a New Order Execution Report response (MsgType 8), (OrdStatus 0)

#### Message Format [¶](#header-message-format-8)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 230 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 209 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 0, D | NewWhen 150=D and 378=4, identifies when a Stop Limit order has been triggered  
378 | ExecRestatementReason |  | 4 | NewWhen 378=4 and 150=D, identifies when a Stop Limit order has been triggered  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
151 | LeavesQty | Y | 1 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | New Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 0 |   
14 | CumQty | Y | 0 |   
11 | ClOrdID | Y | Order_762 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 230 |   
99 | StopPx | N | 6000 | Only returned when OrdType is 3 (Stop Market) or 4 (Stop Limit)  
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | Order_762 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 0 | New  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 039 |   
  
### Execution Report - Filled [ ¶](#message-types-execution-report-filled)

Filled Order Execution Report responses are returned for entirely filled orders.  
_Note that Market Buy Order executions are captured in partial fill messages. The fill message is a summary execution confirming that the order is closed and filled._

#### Message Format [¶](#header-message-format-9)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 273 |   
12 | Commission |  | 0.1234 | Commission Paid  
13 | CommType |  | 3 | Absolute Value  
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 262 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 2 | Filled  
32 | lastShares | Y | 1 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 231 |   
151 | LeavesQty | Y | 0 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Filled Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 11365 |   
14 | CumQty | Y | 1 |   
11 | ClOrdID | Y | Order_762 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 230 |   
99 | StopPx | N | 6000 | Only returned when OrdType is 3 (Stop Market) or 4 (Stop Limit)  
6 | AvgPx | Y | 230 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 2 | Filled  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5851 | LiquidityInd |  | 1 | 1-Add, 2-Remove  
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 231 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 026 |   
  
### Execution Report - Expired [ ¶](#message-types-execution-report-expired)

Expired Order Execution Report responses are returned for market buy orders that have closed with a small amount of unexecuted quote currency left over.  
_Note that Market Buy Order executions are captured in partial fill messages. The expired message is a summary execution confirming that the order is closed._

#### Message Format [¶](#header-message-format-9)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 273 |   
12 | Commission |  | 0 | Commission Paid  
13 | CommType |  | 3 | Absolute Value  
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 262 |   
39 | OrdStatus |  | C |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | C | Expired  
32 | lastShares | Y | 1 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 231 |   
151 | LeavesQty | Y | 0 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Expired Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 10821572-6806-4c95-12c2-d93293942a7d |   
14 | CumQty | Y | 1 |   
11 | ClOrdID | Y | Order_762 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 230 |   
6 | AvgPx | Y | 230 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 2 | Filled  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5851 | LiquidityInd |  | 1 | 1-Add, 2-Remove  
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 231 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 026 |   
  
### Execution Report - Partial Fill [ ¶](#message-types-execution-report-partial-fill)

Partial Fill Execution Report responses are returned for partially filled orders.

#### Message Format [¶](#header-message-format-10)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0279 |   
12 | Commission |  | 0.1234 | Commission Paid  
13 | CommType |  | 3 | Absolute Value  
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 250 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 1 | Partially Filled  
32 | lastShares | Y | 0.2 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 250 |   
151 | LeavesQty | Y | 0.8 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Filled Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 11361 |   
14 | CumQty | Y | 0.2 |   
11 | ClOrdID | Y | Order_774 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 345 |   
6 | AvgPx | Y | 250 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 1 | Partially Filled  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5851 | LiquidityInd |  | 1 | 1-Add, 2-Remove  
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 50 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 082 |   
  
### Execution Report - Pending Cancel [ ¶](#message-types-execution-report-pending-cancel)

A Pending Cancel Execution Report is an acknowledgement that a cancel request has been received. It is not an indication the order has been canceled.

#### Message Format [¶](#header-message-format-11)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0286 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 218 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 6 | Pending Cancel  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
151 | LeavesQty | Y | 1 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Order Cancel Pending |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 0 |   
14 | CumQty | Y | 0 |   
11 | ClOrdID | Y | Cancel763 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 345 |   
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | Order_762 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 6 | Pending cancel  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 137 |   
  
### Execution Report - Canceled [ ¶](#message-types-execution-report-canceled)

An Execution Report with OrdStatus 4 is sent when an order has been canceled.

#### Message Format [¶](#header-message-format-12)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0314 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 219 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 4 | Canceled  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
151 | LeavesQty | Y | 1 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Cancelled Order |   
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | 00000000-0000-0000-0000-000000000000 |   
14 | CumQty | Y | 0 |   
11 | ClOrdID | Y | Cancel763 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 0 |   
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | Order_762 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 4 | Canceled  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 096 |   
  
### Execution Report - Order Reject [ ¶](#message-types-execution-report-order-reject)

If an order is rejected for any reason, an Order Reject Execution Report will be sent with OrdRejReason populated

#### Message Format [¶](#header-message-format-13)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0327 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 341 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 8 | Rejected  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
103 | OrdrejReason | Y | 1 | Refer to table below  
151 | LeavesQty | Y | 0 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y | Symbol is invalid | Reject message  
20 | ExecTransType | Y | 0 | New  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | dkcyba019-1ser-ace3-0193-nlandlb0911 |   
14 | CumQty | Y | 0 |   
11 | ClOrdID | Y | Cancel785 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 230 |   
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | Order_785 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 8 | Rejected  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 174 |   
  
An order can be rejected for different reasons **Reject Reason for tag 103**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
103 | OrdrejReason | Y | 0 | Broker option  
103 | OrdrejReason | Y | 1 | Unknown symbol  
103 | OrdrejReason | Y | 2 | Exchange closed  
103 | OrdrejReason | Y | 3 | Order exceeds limit  
103 | OrdrejReason | Y | 5 | Unknown Order  
103 | OrdrejReason | Y | 6 | Duplicate Order  
103 | OrdrejReason | Y | 8 | Stale Order  
  
Additional detailed failure reasons (tag 58)

Tag | Description  
---|---  
58 |  InsufficientBalance  
58 | InvalidTimeInForce  
58 | InvalidRecipientProfileId  
58 | InvalidIdentityId  
58 | InvalidIdentityAccountId  
58 | MissingExpirationDate  
58 | DisabledIdentityId  
58 | DisabledIdentityAccountId  
58 | NotionalValueTooLarge  
58 | InvalidFundCommissionOption  
58 | PendingIdentityId  
58 | PendingIdentityAccountId  
58 | ClientId Is required  
58 | ClientOrderId Is required  
58 | Account Is required  
58 | Symbol Is required  
58 | OriginalClientOrderId Is required  
58 | HandlingInstructions Expected Value for this field is 1  
58 | Side {value} is not an acceptable value for this field  
58 | OrderType {value} is not an acceptable value for this field  
58 | CashOrderQty Must be greater than zero  
58 | OrderQuantity Must be greater than zero  
58 | StopPrice Must be zero  
58 | Market conditions have invalidated this order  
58 | ExpirationTime must be of format YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss  
58 | TimeInForce Not supported  
58 | Account Is not a GUID  
58 | ClientId Is not a GUID  
58 | Invalid Message Type  
58 | PaxAccountingUnknownError  
58 | InvalidPriceForTakerOrder  
  
### Execution Report - Order Status [ ¶](#message-types-execution-report-order-status)

An order status request message will return the current status of an order. The fields lastShares (32) and and lastPx (31) contain the price and amount of the the latest partial or full execution of the order, a completed order will have a value of 0 in the LeavesQty (151) field. Note: lastShares (32) was relabeled as lastQty in later versions of FIX, the tag number and purpose are identical.

#### Message Format [¶](#header-message-format-14)

**Response Message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 |   
9 | BodyLength |  | 0300 |   
35 | MsgType |  | 8 | Execution report  
49 | SenderCompID |  | ITBIT |   
56 | TargetCompID |  | CLIENT01 |   
34 | MsgSeqNum |  | 330 |   
52 | SendingTime |  | 20150607-15:43:16.543 |   
54 | Side | Y | 1 | Buy  
150 | ExecType | Y | 0 | New  
32 | lastShares | Y | 0 |   
109 | ClientID | Y | 5A196279-2203-XC44-9102-KL9E4E16A36F |   
1 | Account | Y | 6CKH6123-09XC-5611-671K-1900KBO6A889 |   
31 | LastPx | Y | 0 |   
151 | LeavesQty | Y | 0 |   
60 | TransactTime | Y | 20150607-15:43:16.543 |   
58 | Text | Y |  |   
20 | ExecTransType | Y | 3 | Status  
55 | Symbol | Y | XBTUSD |   
17 | ExecID | Y | dkcyba019-1ser-ace3-0193-nlandlb0911 |   
14 | CumQty | Y | 0 |   
11 | ClOrdID | Y | Order_782 | Client order identifier. Can be reused if the order has been closed for more than 30 days. Allowed characters are  
a-z, A-Z, 0-9 and . - _ $ :   
44 | Price | Y | 230 |   
6 | AvgPx | Y | 0 |   
41 | OrigClOrdID | Y | Order_782 |   
40 | OrdType | Y | 2 | Limit  
18 | ExecInst |  | 6 | (6) for Post-Only  
39 | OrdStatus | Y | 0 | New  
38 | OrderQty |  | 1 | Echoed back for Limit and Market Sell orders  
152 | CashOrderQty |  |  | Echoed for Market Buy orders only  
37 | OrderID | Y | 11196679-9103-JK44-0901-XKNE4E16A12K |   
5047 | AllocBrokerAccountID |  |  | For brokerage client use only (IdentityAccountId)  
50 | SenderSubID |  |  | For brokerage client use only (IdentityId)  
5074 | FundCommissionOption |  |  | For brokerage client use only  
381 | GrossTradeAmt | Y | 0 | lastShares <32> * LastPx <31>  
59 | TimeInForce | Y | 1 | 1 (Good Till Cancel), 3 (Immediate or Cancel), 4 (Fill or Kill), 6 (Good Till Time)  
126 | ExpireTime | N | 20210714-17:03:50 | Required for TIF = 6, format should be YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss Note: milliseconds are ignored   
5000 | RecipientProfileId | N | 761j25ca-a75e-483f-8d89-40e742dcd8c0 | For brokerage client use only. The profileID that will receive settled currency.  
2362 | SelfMatchPreventionID | N | UA54dSVd-yWGB-FWj2-zHbjJMGd | The string field used to prevent matching against an opposite side order submitted by the same Crypto Brokerage customer. If this field is not submitted, an order that matches against another order submitted by the same customer will cancel the original resting order. Up to 36 characters are supported. This field requires additional permissions only available to certain accounts. Reach out to your Paxos Representative for more information.  
10 | CheckSum |  | 118 |   
  
### Logout [ ¶](#message-types-logout)

A logout message initiates or confirms the termination of a FIX session. Disconnection without the exchange of logout messages should be interpreted as an abnormal condition. An unsolicited logout may indicate a connection or account issue, SendingTime (52) will have a human readable message indicating if there is an issue. In some cases, a logout message may be associated with an account’s trading permissions being suspended; if you are unable to reconnect with ResetSeqNumFlag (141) set to Y, please engage with support.

#### Message Format [¶](#header-message-format-15)

**Incoming message**

Tag | Field Name | Req. | Value | Description  
---|---|---|---|---  
8 | BeginString |  | FIX.4.2 | Logout  
9 | BodyLength |  | 0056 |   
35 | MsgType |  | 5 |   
49 | SenderCompID |  | CLIENT01 |   
56 | TargetCompID |  | ITBIT |   
34 | MsgSeqNum |  | 2 |   
52 | SendingTime |  | 20150607-15:43:16.534 |   
58 | Text |  | 00140000000Wn1ynf_590- CODE: 1-200-A-141: Expected Logon Message with 141 |   
10 | CheckSum |  | 107 |   
  
## Encoded Tags [¶](#encoded-tags)

Some FIX Tag short codes and their values are listed below. The description field in the message type tables above also contain this information.

#### 1\. MsgType: [¶](#header-1.-msgtype-)

Value | Description  
---|---  
A | Logon  
D | New Order Single  
F | Order Cancel Request  
H | Order Status Request  
0 | Heartbeat  
2 | Resend Request  
8 | Execution Report  
9 | Order Cancel Reject  
  
#### 2\. ExecType [¶](#header-2.-exectype)

Value | Description  
---|---  
0 | New  
1 | Partially Filled  
2 | Filled  
3 | Done  
4 | Canceled  
6 | Pending Cancel  
8 | Rejected  
A | Pending New Order  
D | Order Changed  
C | Order Expired  
  
* * *
