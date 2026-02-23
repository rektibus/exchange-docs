# Bybit Open API v5 explorer
Collection of v5 Restul API


## GET /v5/asset/exchange/order-record
Get Coin Exchange Records

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| fromCoin | query | False | string |
| toCoin | query | False | string |
| limit | query | True | integer |
| cursor | query | False | string |

## GET /v5/asset/delivery-record
Get Delivery Record

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| expDate | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/settlement-record
Get USDC Session Settlement

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/transfer/query-asset-info
Get Asset Info (Spot)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| accountType | query | True | string |
| coin | query | False | string |

## GET /v5/asset/transfer/query-account-coins-balance
Get All Coins Balance

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| memberId | query | False | string |
| accountType | query | True | string |
| coin | query | False | string |
| withBonus | query | False | integer |

## GET /v5/asset/transfer/query-account-coin-balance
Get Single Coin Balance

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| memberId | query | False | string |
| accountType | query | True | string |
| coin | query | True | string |
| withBonus | query | False | integer |
| withTransferSafeAmount | query | False | integer |

## GET /v5/asset/transfer/query-transfer-coin-list
Get Transferable Coin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| fromAccountType | query | True | string |
| toAccountType | query | True | string |

## POST /v5/asset/transfer/inter-transfer
Create Internal Transfer

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/asset/transfer/query-inter-transfer-list
Get Internal Transfer Records

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| transferId | query | False | string |
| coin | query | False | string |
| status | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/transfer/query-sub-member-list
Get Sub UID

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |

## POST /v5/asset/transfer/universal-transfer
Create Universal Transfer

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |

## GET /v5/asset/transfer/query-universal-transfer-list
Get Universal Transfer Records

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| transferId | query | False | string |
| coin | query | False | string |
| status | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/deposit/query-allowed-list
Get Allowed Deposit Coin Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| coin | query | False | string |
| chain | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## POST /v5/asset/deposit/deposit-to-account
Set Deposit Account

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |

## GET /v5/asset/deposit/query-record
Get Deposit Record (on-chain)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| coin | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/deposit/query-sub-member-record
Get Sub Account Deposit Records (on-chain)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| subMemberId | query | True | string |
| coin | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/deposit/query-internal-record
Get Internal Deposit Records (off-chain)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| coin | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/asset/deposit/query-address
Get Master Deposit Address

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| coin | query | True | string |
| chainType | query | False | string |

## GET /v5/asset/deposit/query-sub-member-address
Get Sub Deposit Address

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| coin | query | True | string |
| chainType | query | True | string |
| subMemberId | query | True | string |

## GET /v5/asset/coin/query-info
Get Coin Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| coin | query | False | string |

## GET /v5/asset/withdraw/query-record
Get Withdraw Records

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| withdrawID | query | False | string |
| coin | query | False | string |
| withdrawType | query | False | integer |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

