# Bybit Open API v5 explorer - Spot margin trade
Collection of v5 Restul API


## GET /v5/spot-margin-trade/data
Get VIP Margin Data

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| vipLevel | query | False | array |
| currency | query | False | string |

## POST /v5/spot-margin-trade/switch-mode
Toggle Margin Trade

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## POST /v5/spot-margin-trade/set-leverage
Set Leverage

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/spot-margin-trade/state
Get Status And Leverage

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

