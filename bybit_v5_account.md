# Bybit Open API v5 explorer
Collection of v5 Restul API


## GET /v5/account/wallet-balance
Get Wallet Balance

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| accountType | query | True | string |
| coin | query | False | string |

## POST /v5/account/upgrade-to-uta
Upgrade to Unified Account

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/account/set-collateral-switch
Set Collateral Coin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/account/borrow-history
Get Borrow History

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| currency | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/account/collateral-info
Get Collateral Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| currency | query | False | string |

## GET /v5/account/coin-greeks
Get Coin Greeks

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| baseCoin | query | False | string |

## GET /v5/account/fee-rate
Get Fee Rate

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| baseCoin | query | False | string |

## GET /v5/account/info
Get Account Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/account/transaction-log
Get Transaction Log

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| accountType | query | False | string |
| category | query | False | string |
| currency | query | False | string |
| baseCoin | query | False | string |
| type | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## POST /v5/account/set-margin-mode
Set Margin Mode

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/account/set-hedging-mode
Set Spot Hedging

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

