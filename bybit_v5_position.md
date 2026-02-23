# Bybit v5 position api explorer
Collection of Position - v5 Restul API, which covers USDT Perpetual, USDC Perpetual, Inverse Perpetual, Inverse Future and Option.


## GET /v5/position/list
Get Position Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| baseCoin | query | False | string |
| settleCoin | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## POST /v5/position/set-leverage
Set Leverage

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/switch-isolated
Switch Cross/Isolated Margin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/set-tpsl-mode
Set TP/SL Mode

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/switch-mode
Switch Position Mode

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/set-risk-limit
Set Risk Limit

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/trading-stop
Set Trading Stop

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/set-auto-add-margin
Set Auto Add Margin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/position/add-margin
Add Or Reduce Margin

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/execution/list
Get Execution (2 years)

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
| execType | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/position/closed-pnl
Get Closed PnL

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| category | query | True | string |
| symbol | query | False | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

