# BigONE Contract REST API
API for BigONE Contract Trading. 
The base URL for all requests is `https://api.big.one/api/contract/v2`.
Authentication is required for all private endpoints.


## GET /instruments
Get List of Contracts Detail

## GET /depth@{symbol}/snapshot
Get OrderBook Snapshot

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | path | True | string |

## GET /accounts
Get Cash and Position Detail

## PUT /positions/{symbol}/margin
Adjust Leverage / Margin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | path | True | string |

## PUT /positions/{symbol}/risk-limit
Set Risk Limit

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | path | True | string |

## POST /orders
Place Order

## GET /orders
Get Order List

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| start-time | query | False | integer |
| end-time | query | False | integer |
| id | query | False | string |
| type | query | False | string |
| side | query | False | string |
| status | query | False | string |
| opt | query | False | string |
| limit | query | False | integer |

## GET /orders/opening
Get Active Order List

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| id | query | False | string |
| start-time | query | False | integer |
| end-time | query | False | integer |
| limit | query | False | integer |

## GET /orders/{id}
Get Order Detail

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| id | path | True | string |

## DELETE /orders/{id}
Cancel Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| id | path | True | string |

## GET /orders/count
Count Orders

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| id | query | False | string |
| start-time | query | False | integer |
| end-time | query | False | integer |
| type | query | False | string |
| side | query | False | string |
| status | query | False | string |
| opt | query | False | string |

## GET /orders/opening/count
Count Active Orders

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| start-time | query | False | integer |
| end-time | query | False | integer |

## GET /trades
Get Trade List

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| id | query | False | string |
| limit | query | False | integer |
| side | query | False | string |
| order-id | query | False | string |

## GET /trades/count
Get Count of Trades

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| symbol | query | False | string |
| id | query | False | string |
| limit | query | False | integer |
| side | query | False | string |
| order-id | query | False | string |

