# Bybit Open API v5 explorer - Spot leverage token
Collection of v5 Restul API


## GET /v5/spot-lever-token/info
Get Leverage Token Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| ltCoin | query | False | string |

## GET /v5/spot-lever-token/reference
Get Leverage Token Market

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| ltCoin | query | True | string |

## POST /v5/spot-lever-token/purchase
Purchase

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/spot-lever-token/redeem
Redeem

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/spot-lever-token/order-record
Get Purchase or Redeem Records

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| ltCoin | query | False | string |
| orderId | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| ltOrderType | query | False | integer |
| serialNo | query | False | string |

