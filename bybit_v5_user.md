# Bybit Open API v5 explorer - User
Collection of v5 Restul API


## GET /v5/user/query-api
Get API Key Information

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |

## GET /v5/user/sub-apikeys
Get Sub Account All API Keys

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | True | string |
| secret | header | True | string |
| subMemberId | query | True | string |
| limit | query | False | integer |
| cursor | query | False | string |

## GET /v5/user/get-member-type
Get UID Wallet Type

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| memberIds | query | False | string |

## GET /v5/user/aff-customer-info
Get Affiliate User Info

### Parameters
| Name | In | Required | Type |
|---|---|---|---|
| apiKey | header | False | string |
| secret | header | False | string |
| uid | query | True | string |

