# PXN OpenAPI


## GET /asset_pairs
Get All Asset Pairs

## GET /asset_pairs/{asset_pair_name}/ticker
Get Ticker

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | path | True | string |

## GET /asset_pairs/tickers
Get Multiple Tickers

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| pair_names | query | False | string |

## GET /asset_pairs/{asset_pair_name}/depth
Get Order Book

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | path | True | string |
| limit | query | False | integer |

## GET /asset_pairs/{asset_pair_name}/trades
Get Market Trades

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | path | True | string |

## GET /asset_pairs/{asset_pair_name}/candles
Get Candles

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | path | True | string |
| period | query | True | string |
| time | query | False | string |
| limit | query | False | integer |
| direction | query | False | string |

## GET /viewer/accounts
Get All Accounts

## GET /viewer/accounts/{asset_symbol}
Get Account by Symbol

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_symbol | path | True | string |

## GET /viewer/orders
Get Orders

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | query | True | string |
| page_token | query | False | string |
| side | query | False | string |
| state | query | False | string |
| limit | query | False | integer |

## POST /viewer/orders
Create Order

## GET /viewer/orders/{id}
Get Order by ID

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| id | path | True | integer |

## GET /viewer/order
Get Order by ID or Client ID

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| order_id | query | False | integer |
| client_order_id | query | False | string |

## POST /viewer/orders/multi
Create Multiple Orders

## POST /viewer/orders/{id}/cancel
Cancel Order by ID (Path)

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| id | path | True | integer |

## POST /viewer/order/cancel
Cancel Order by ID or Client ID

## POST /viewer/orders/cancel
Cancel All Orders

## GET /viewer/trades
Get User Trades

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_name | query | True | string |
| page_token | query | False | string |
| limit | query | False | integer |

## GET /viewer/trading_fees
Get Trading Fees

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| asset_pair_names | query | False | string |

