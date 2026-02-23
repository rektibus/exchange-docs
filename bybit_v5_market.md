# Bybit Open API v5 explorer
Collection of v5 Restul API


## GET /v5/market/time
Get Bybit Server Time

## GET /v5/market/kline
Get Kline

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| interval | query | True | array |
| start | query | False | integer |
| end | query | False | integer |
| limit | query | False | integer |

## GET /v5/market/mark-price-kline
Get Mark Price Kline

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| interval | query | True | array |
| start | query | False | integer |
| end | query | False | integer |
| limit | query | False | integer |

## GET /v5/market/index-price-kline
Get Index Price Kline

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| interval | query | True | array |
| start | query | False | integer |
| end | query | False | integer |
| limit | query | False | integer |

## GET /v5/market/premium-index-price-kline
Get Premium Index Price Kline

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| interval | query | True | array |
| start | query | False | integer |
| end | query | False | integer |
| limit | query | False | integer |

## GET /v5/market/instruments-info
Get Instrument Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | False | string |
| status | query | False | string |
| baseCoin | query | False | string |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/market/orderbook
Get Orderbook

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| limit | query | False | integer |

## GET /v5/market/tickers
Get Tickers

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| baseCoin | query | False | string |
| expDate | query | False | string |
| symbol | query | False | string |

## GET /v5/market/funding/history
Get Funding Rate History

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |

## GET /v5/market/recent-trade
Get Public Recent Trading History

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| baseCoin | query | False | string |
| optionType | query | False | string |
| limit | query | False | integer |

## GET /v5/market/open-interest
Get Open Interest

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| intervalTime | query | True | array |
| startTime | query | False | integer |
| endTime | query | False | integer |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/market/historical-volatility
Get Historical Volatility

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| baseCoin | query | False | string |
| period | query | False | array |
| startTime | query | False | integer |
| endTime | query | False | integer |

## GET /v5/market/insurance
Get Insurance

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| coin | query | False | string |

## GET /v5/market/risk-limit
Get Risk Limit

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | False | string |

## GET /v5/market/delivery-price
Get Delivery Price

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | False | string |
| baseCoin | query | False | string |
| limit | query | False | string |
| cursor | query | False | string |

## GET /v5/market/account-ratio
Get Long Short Ratio

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| category | query | True | array |
| symbol | query | True | string |
| period | query | True | array |
| limit | query | False | integer |

