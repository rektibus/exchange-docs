# Bybit v5 trade api explorer
Collection of Trade - v5 Restul API, which covers USDT Perpetual, USDC Perpetual, Inverse Perpetual, Inverse Future, Spot and Option.


## POST /v5/order/create
Place Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/order/amend
Amend Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/order/cancel
Cancel Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/order/realtime
Get Open Orders (real-time)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| baseCoin | query | False | string |
| settleCoin | query | False | string |
| orderId | query | False | string |
| orderLinkId | query | False | string |
| orderFilter | query | False | string |
| openOnly | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## POST /v5/order/cancel-all
Cancel All Orders

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/order/history
Get Order History (2 years)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| baseCoin | query | False | string |
| orderId | query | False | string |
| orderLinkId | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| orderStatus | query | False | string |
| orderFilter | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## POST /v5/order/create-batch
Batch Place Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/order/amend-batch
Batch Amend Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/order/cancel-batch
Batch Cancel Order

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/order/spot-borrow-check
Get Borrow Quota (Spot)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | True | string |
| side | query | True | string |

