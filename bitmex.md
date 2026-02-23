# BitMEX API Documentation

Source: Official OpenAPI Spec (/tmp/bitmex.json)

## BitMEX API

## REST API for the BitMEX Trading Platform

_If you are building automated tools, please subscribe to the_
_[BitMEX API RSS Feed](https://blog.bitmex.com/api_announcement/feed/) for changes. The feed will be updated_
_regularly and is the most reliable way to get downtime and update announcements._

[View Changelog](/app/apiChangelog)

---

#### Getting Started

Base URI: [https://www.bitmex.com/api/v1](/api/v1)

##### Fetching Data

All REST endpoints are documented below. You can try out any query right from this interface.

Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.

Additional documentation regarding filters, timestamps, and authentication
is available in [the main API documentation](/app/restAPI).

_All_ table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want
to have the quickest possible data without being subject to ratelimits.

##### Return Types

By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.

##### Trade Data Queries

_This is only a small subset of what is available, to get you started._

Fill in the parameters and click the `Try it out!` button to try any of these queries.

- [Pricing Data](#!/Quote/Quote_get)

- [Trade Data](#!/Trade/Trade_get)

- [OrderBook Data](#!/OrderBook/OrderBook_getL2)

- [Settlement Data](#!/Settlement/Settlement_get)

- [Exchange Statistics](#!/Stats/Stats_history)

Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.

##### Swagger Specification

[⇩ Download Swagger JSON](swagger.json)

---

## All API Endpoints

Click to expand a section.


Version: 1.2.0

## Endpoints

### POST `/address`

**Creates a new saved address.**

### Verification

Please note that `skip2FA` and `skipConfirm` require verification:
 - `skip2FA` can be verified by providing `otpToken` in this request. If `otpToken` is not provided, a 2FA code can be entered by following the the link included in the email sent upon address creation.

 - `skipConfirm` can be verified by following the link included in the email sent upon address creation.

Please note that the email will be valid for 30 minutes.

### Whitelist

If the address book has the `whitelist` setting enabled, then creating a saved address will require both 2FA verification and the passage of cooldown period. 2FA can either be provided immediately (`otpToken`) or by following the link included in the email sent upon address creation.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | formData | string | False | Currency of the address. Options: `XBt`, `USDt` |
| network | formData | string | True | Selected network. |
| address | formData | string | True | Destination Address. |
| name | formData | string | True | Name of the entry, eg. 'Hardware wallet'. |
| note | formData | string | False | Optional annotation. |
| skipConfirm | formData | boolean | False | Skip e-mail confirmations for transfers to this address. An email will be sent for confirmation to v |
| skip2FA | formData | boolean | False | Skip 2FA confirmations for transfers to this address. If otpToken is not provided in this request, a |
| memo | formData | string | False | Destination Memo. |
| otpToken | formData | string | False | 2FA token. Provide to verify skip2FA or to start the cooldown period on address with whitelist setti |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/address`

**Get your addresses.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### PUT `/address`

**Update an address.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| addressId | formData | number | True | Address ID. |
| name | formData | string | False | Name of the entry, eg. 'Hardware wallet'. |
| note | formData | string | False | Optional annotation. |
| beneficiary | formData | string | False | Beneficiary Details. |
| vasp | formData | string | False | Virtual Asset Service Provider Details. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/addressConfig`

**Get your address book settings.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/announcement`

**Get site announcements.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/announcement/urgent`

**Get urgent (banner) announcements.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/apiKey`

**Get your API Keys.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| reverse | query | boolean | False | If true, will sort results newest first. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/chat`

**Get chat messages.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| count | query | number | False | Number of results to fetch. |
| start | query | number | False | Starting ID for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| channelID | query | number | False | Channel id. GET /chat/channels for ids. Global English by default |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/chat`

**Send a chat message.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| message | formData | string | True |  |
| channelID | formData | number | False | Channel to post to. Default 1 (English). |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/chat/channels`

**Get available channels.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/chat/connected`

**Get connected users.**

Returns an array with browser users in the first position and API users (bots) in the second position.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/chat/pinned`

**Get pinned message for a channel.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| channelID | query | number | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/execution`

**Get all raw executions for your account.**

This returns all raw transactions, which includes order opening and cancelation, and order status
changes. It can be quite noisy. More focused information is available at `/execution/tradeHistory`.

You may also use the `filter` param to target your query. Specify an array as a filter value, such as
`{"execType": ["Settlement", "Trade"]}` to filter on multiple values.

See [the FIX Spec](http://www.onixs.biz/fix-dictionary/5.0.SP2/msgType_8_8.html) for explanations of these fields.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/execution/tradeHistory`

**Get all balance-affecting executions.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountId | query | number | False | AccountId fetching the trade history, must be a paired account with main user. |
| targetAccountIds | query | string | False | AccountIds fetching the trade history, must be a paired account with main user. Can be wildcard * to |
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/funding`

**Get funding history.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/globalNotification`

**Get your current GlobalNotifications.**

This is an upcoming feature and currently does not return data.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild`

**Creates a new guild**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| name | formData | string | True | Name of the guild, must be unique, must be at least 5 characters |
| emoji | formData | string | True | Emoji name. |
| potDistributionPercent | formData | number | True | How much of the pot should be distributed to the guild members, must be between 0 and 100 |
| potDistributionType | formData | string | True | How the pot should be distributed to the guild members, must be one of the following: ROLL_OVER, TOP |
| description | formData | string | False | Guild description, can be used to explain the guild to other users. |
| twitter | formData | string | False | Guild twitter handle. |
| discord | formData | string | False | Guild discord link. |
| telegram | formData | string | False | Guild telegram link. |
| imgUrl | formData | string | False | URL for the profile image of the guild, is used by clients to add some color to the guild, if no ima |
| isPrivate | formData | boolean | False | Guild privacy status |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### PUT `/guild`

**Edit guild new guild**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| name | formData | string | True | Name of the guild, must be unique, must be at least 5 characters |
| emoji | formData | string | True | Emoji name. |
| potDistributionPercent | formData | number | True | How much of the pot should be distributed to the guild members, must be between 0 and 100 |
| potDistributionType | formData | string | True | How the pot should be distributed to the guild members, must be one of the following: ROLL_OVER, TOP |
| potTraderId | formData | number | False | User ID of the guild member with order write permission for the pot |
| description | formData | string | False | Guild description, can be used to explain the guild to other users. |
| twitter | formData | string | False | Guild twitter handle. |
| discord | formData | string | False | Guild discord link. |
| telegram | formData | string | False | Guild telegram link. |
| imgUrl | formData | string | False | URL for the profile image of the guild, is used by clients to add some color to the guild, if no ima |
| isPrivate | formData | boolean | False | Guild privacy status |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/guild`

**Get all guilds**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild/archive`

**Archive a guild**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild/join`

**Request to Join a private guild or join a public guild**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| code | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild/kick`

**Kick member from guild**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| memberUserId | formData | number | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild/leave`

**Leave guild or cancel guild join request**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/guild/shareTrades`

**Toggle share trades for your account, which controls whether your guild members can see your orders and positions in their UI**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| shareTrades | formData | boolean | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument`

**Get instruments.**

This returns all instruments and indices, including those that have settled or are unlisted.
Use this endpoint if you want to query for individual instruments or use a complex filter.
Use `/instrument/active` to return active instruments, or use a filter like `{"state": "Open"}`.

The instrument type is specified by the `typ` param.

- Perpetual Contracts - `FFWCSX`
- Perpetual Contracts (FX underliers) - `FFWCSF`
- Spot - `IFXXXP`
- Futures - `FFCCSX`
- BitMEX Basket Index - `MRBXXX`
- BitMEX Crypto Index - `MRCXXX`
- BitMEX FX Index - `MRFXXX`
- BitMEX Lending/Premium Index - `MRRXXX`
- BitMEX Volatility Index - `MRIXXX`


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/active`

**Get all active instruments and instruments that have expired in <24hrs.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/activeAndIndices`

**Helper method. Gets all active instruments and all indices. This is a join of the result of /indices and /active.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/activeIntervals`

**Return all active contract series and interval pairs.**

This endpoint is useful for determining which pairs are live. It returns two arrays of   strings. The first is intervals, such as `["XBT:perpetual", "XBT:quarterly", "XBT:biquarterly", "ETH:quarterly", ...]`. These identifiers are usable in any query's `symbol` param. The second array is the current resolution of these intervals. Results are mapped at the same index.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/compositeIndex`

**Show constituent parts of an index.**

Composite indices are built from multiple external price sources.

Use this endpoint to get the underlying prices of an index. For example, send a `symbol` of `.BXBT` to
get the ticks and weights of the constituent exchanges that build the ".BXBT" index.

A tick with reference `"BMI"` and weight `null` is the composite index tick.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | The composite index symbol. |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/indices`

**Get all price indices.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/instrument/usdVolume`

**Get a summary of exchange statistics in USD.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Filter by symbol. |
| columns | query | string | False | Array of column names to fetch. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/insurance`

**Get insurance fund history.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/leaderboard`

**Get current leaderboard. Use "method" param for v1 format (notional/ROE), or "sortBy" + "period" for v2.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| method | query | string | False | V1 ranking type. Options: "notional", "ROE" |
| sortBy | query | string | False | Options: "PNL_TOP", "PNL_BOTTOM", "ROI_TOP", "ROI_BOTTOM", "VOLUME_TOP", "VOLUME_BOTTOM" |
| period | query | string | False | Time period for flexible mode. Options: "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR" |
| count | query | number | False | Number of results to return (1-1000, default: 100). Only used with sortBy/period. |
| start | query | number | False | Starting position for pagination. Only used with sortBy/period. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/leaderboard/name`

**Get your alias on the leaderboard.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/leagueoftrader/myRankings`

**Get leaderboard with rankings for all leader accounts owned by the authenticated user.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| period | query | number | False | Timeframe for ranking evaluation in days. Options: 1, 7, 30, 90, 180. Default: 30 |
| sort_by | query | string | False | Metric to sort by. Options: roi, pnl, mdd, aum, copiers, sharpe, risk, win_ratio. Default: roi |
| asc | query | number | False | Sort order: 0 for descending (default), 1 for ascending |
| min_roi | query | number | False | Minimum ROI filter (%) |
| max_roi | query | number | False | Maximum ROI filter (%) |
| min_mdd | query | number | False | Minimum Maximum Drawdown filter (%) |
| max_mdd | query | number | False | Maximum Maximum Drawdown filter (%) |
| min_aum | query | number | False | Minimum Assets Under Management filter (USD) |
| max_aum | query | number | False | Maximum Assets Under Management filter (USD) |
| min_copier | query | number | False | Minimum number of copiers filter |
| max_copier | query | number | False | Maximum number of copiers filter |
| min_balance | query | number | False | Minimum account balance filter (USD) |
| max_balance | query | number | False | Maximum account balance filter (USD) |
| min_pnl | query | number | False | Minimum Profit/Loss filter (USD) |
| max_pnl | query | number | False | Maximum Profit/Loss filter (USD) |
| min_copier_pnl | query | number | False | Minimum copier Profit/Loss filter (USD) |
| max_copier_pnl | query | number | False | Maximum copier Profit/Loss filter (USD) |
| name | query | string | False | Filter by leader name (case-insensitive fuzzy search). When provided, other filters except period, s |
| bookmarks | query | number | False | Filter only bookmarked leaders. 0 = all, 1 = only bookmarked. Default: 0 |
| copied | query | number | False | Filter only copied leaders. 0 = all, 1 = only copied. Default: 0 |
| kind | query | string | False | Filter by leader type. Options: normal, hyper |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/liquidation`

**Get liquidation orders.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/order`

**Get your orders.**

To get open orders only, send {"open": true} in the filter param.

See <a href="http://www.onixs.biz/fix-dictionary/5.0.SP2/msgType_D_68.html">the FIX Spec</a> for explanations of these fields.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/order`

**Create a new order.**

## Placing Orders

This endpoint is used for placing orders. See individual fields below for more details on their use.

#### Order Types

All orders require a `symbol`. All other fields are optional except when otherwise specified.

These are the valid `ordType`s:

- **Limit**: The default order type. Specify an `orderQty` and `price`.
- **Market**: A traditional Market order. A Market order will execute until filled or your bankruptcy price is reached, at
  which point it will cancel.
- **Stop**: A Stop Market order. Specify an `orderQty` and `stopPx`. When the `stopPx` is reached, the order will be entered
  into the book.
  - On sell orders, the order will trigger if the triggering price is lower than the `stopPx`. On buys, higher.
  - Note: Stop orders do not consume margin until triggered. Be sure that the required margin is available in your
    account so that it may trigger fully.
  - `Close` Stops don't require an `orderQty`. See Execution Instructions below.
- **StopLimit**: Like a Stop Market, but enters a Limit order instead of a Market order. Specify an `orderQty`, `stopPx`,
  and `price`.
- **MarketIfTouched**: Similar to a Stop, but triggers are done in the opposite direction. Useful for Take Profit orders.
- **LimitIfTouched**: As above; use for Take Profit Limit orders.
- **Pegged**: Pegged orders allow users to submit a limit price relative to the current market price. Specify a
  `pegPriceType`, and `pegOffsetValue`.
  - Pegged orders **must** have an `execInst` of `Fixed`. This means the limit price is set at the time the order
    is accepted and does not change as the reference price changes.
  - `PrimaryPeg`: Price is set relative to near touch price.
  - `MarketPeg`: Price is set relative to far touch price.
  - A `pegPriceType` submitted with no `ordType` is treated as a `Pegged` order.

#### Execution Instructions

The following `execInst`s are supported. If using multiple, separate with a comma (e.g. `LastPrice,Close`).

- **ParticipateDoNotInitiate**: Also known as a Post-Only order. If this order would have executed on placement, it will cancel instead.
  This is intended to protect you from the far touch moving towards you while the order is in transit.
  It is not intended for speculating on the far touch moving away after submission - we consider such behaviour abusive and monitor for it.
- **MarkPrice, LastPrice, IndexPrice**: Used by stop and if-touched orders to determine the triggering price.
  Use only one. By default, `MarkPrice` is used. Also used for Pegged orders to define the value of `LastPeg`. IndexPrice is not applicable to spot trading symbols.
- **ReduceOnly**: A `ReduceOnly` order can only reduce your position, not increase it. If you have a `ReduceOnly`
  limit order that rests in the order book while the position is reduced by other orders, then its order quantity will
  be amended down or canceled. If there are multiple `ReduceOnly` orders the least aggressive will be amended first. Not applicable to spot trading symbols.
- **Close**: `Close` implies `ReduceOnly`. A `Close` order will cancel other active limit orders with the same side
  and symbol if the open quantity exceeds the current position. This is useful for stops: by canceling these orders, a
  `Close` Stop is ensured to have the margin required to execute, and can only execute up to the full size of your
  position. If `orderQty` is not specified, a `Close` order has an `orderQty` equal to your current position's size. Not applicable to spot trading symbols.
  - Note that a `Close` order without an `orderQty` requires a `side`, so that BitMEX knows if it should trigger
    above or below the `stopPx`.
- **LastWithinMark**: Used by stop orders with `LastPrice` to allow stop triggers only when:
  - For Sell Stop Market / Stop Limit Order
    - Last Price &lt= Stop Price
    - Last Price &gt= Mark Price × (1 - 5%)
  - For Buy Stop Market / Stop Limit Order:
    - Last Price &gt= Stop Price
    - Last Price &lt= Mark Price × (1 + 5%)
  - Not applicable to spot trading symbols.
- **Fixed**: Pegged orders **must** have an `execInst` of `Fixed`. This means the limit price is set at the time
  the order is accepted and does not change as the reference price changes.

#### Pegged Orders

Pegged orders allow users to submit a limit price relative to the current market price.
The limit price is set once when the order is submitted and does not change with the reference price.
This order type is not intended for speculating on the far touch moving away after submission - we consider such behaviour abusive and monitor for it.

Pegged orders have an `ordType` of `Pegged`, and an `execInst` of `Fixed`.

A `pegPriceType` and `pegOffsetValue` must also be submitted:

- `PrimaryPeg` - price is set relative to the **near touch** price
- `MarketPeg` - price is set relative to the **far touch** price

#### Trailing Stop Pegged Orders

Use `pegPriceType` of `TrailingStopPeg` to create Trailing Stops.

The price is set at submission and updates once per second if the underlying price (last/mark/index) has moved by
more than 0.1%. `stopPx` then moves as the market moves away from the peg, and freezes as the market moves toward it.

Use `pegOffsetValue` to set the `stopPx` of your order. The peg is set to the triggering price specified in the
`execInst` (default `MarkPrice`). Use a negative offset for stop-sell and buy-if-touched orders.

Requires `ordType`: `Stop`, `StopLimit`, `MarketIfTouched`, `LimitIfTouched`.

#### Linked Orders

Linked Orders are an advanced capability. It is very powerful, but its use requires careful coding and testing.
Please follow this document carefully and use the [Testnet Exchange](https://testnet.bitmex.com) while developing.

BitMEX offers four advanced Linked Order types:

- **OCO**: _One Cancels the Other_. A very flexible version of the standard Stop / Take Profit technique.
  Multiple orders may be linked together using a single `clOrdLinkID`. Send a `contingencyType` of
  `OneCancelsTheOther` on the orders. The first order that fully or partially executes (or activates
  for `Stop` orders) will cancel all other orders with the same `clOrdLinkID`.
- **OTO**: _One Triggers the Other_. Send a `contingencyType` of `'OneTriggersTheOther'` on the primary order and
  then subsequent orders with the same `clOrdLinkID` will be not be triggered until the primary order fully executes.

#### Trailing Stops

You may use `pegPriceType` of `'TrailingStopPeg'` to create Trailing Stops. The pegged `stopPx` will move as the market
moves away from the peg, and freeze as the market moves toward it.

To use, combine with `pegOffsetValue` to set the `stopPx` of your order. The peg is set to the triggering price
specified in the `execInst` (default `'MarkPrice'`). Use a negative offset for stop-sell and buy-if-touched orders.

Requires `ordType`: `'Stop', 'StopLimit', 'MarketIfTouched', 'LimitIfTouched'`.

#### Simple Quantities

[Simple Quantities are deprecated as of 2018/10/26](https://blog.bitmex.com/api_announcement/deprecation-of-simpleorderqty-functionality/)

#### Rate Limits

You can improve your reactivity to market movements while staying under your rate limit by using the
[Amend](#!/Order/Order_amend) endpoint (PUT /order). This allows you to stay
in the market and avoids the cancel/replace cycle.

#### Tracking Your Orders

If you want to keep track of order IDs yourself, set a unique `clOrdID` per order.
This `clOrdID` will come back as a property on the order and any related executions (including on the WebSocket),
and can be used to get or cancel the order. Max length is 36 characters.

You can also change the `clOrdID` by amending an order, supplying an `origClOrdID`, and your desired new
ID as the `clOrdID` param, like so:

```
# Amends an order's leavesQty, and updates its clOrdID to "def-456"
PUT /api/v1/order {"origClOrdID": "abc-123", "clOrdID": "def-456", "leavesQty": 1000}
```


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Instrument symbol. e.g. 'XBTUSD'. |
| strategy | formData | string | False | Order strategy. e.g. 'OneWay', 'Long', 'Short'. |
| side | formData | string | False | Order side. Valid options: Buy, Sell. Defaults to 'Buy' unless `orderQty` is negative. |
| simpleOrderQty | formData | number | False | Deprecated: simple orders are not supported after 2018/10/26 |
| orderQty | formData | number | False | Order quantity in units of the instrument (i.e. contracts, for spot it is base currency in minor cur |
| price | formData | number | False | Optional limit price for 'Limit', 'StopLimit', and 'LimitIfTouched' orders. |
| displayQty | formData | number | False | Optional quantity to display in the book. Use 0 for a fully hidden order. |
| stopPx | formData | number | False | Optional trigger price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders. Use  |
| clOrdID | formData | string | False | Optional Client Order ID. This clOrdID will come back on the order and any related executions. |
| clOrdLinkID | formData | string | False | Optional Client Order Link ID for contingent orders |
| pegOffsetValue | formData | number | False | Optional trailing offset from the current price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'Lim |
| pegPriceType | formData | string | False | Optional peg price type. Valid options: MarketPeg, PrimaryPeg, TrailingStopPeg. |
| ordType | formData | string | False | Order type. Valid options: Market, Limit, Stop, StopLimit, MarketIfTouched, LimitIfTouched, Pegged.  |
| timeInForce | formData | string | False | Time in force. Valid options: Day, GoodTillCancel, ImmediateOrCancel, FillOrKill. Defaults to 'GoodT |
| execInst | formData | string | False | Optional execution instructions. Valid options: ParticipateDoNotInitiate, AllOrNone, MarkPrice, Inde |
| contingencyType | formData | string | False | Optional contingency type for use with `clOrdLinkID`. Valid options: OneCancelsTheOther, OneTriggers |
| text | formData | string | False | Optional order annotation. e.g. 'Take profit'. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### PUT `/order`

**Amend the quantity or price of an open order.**

Send an `orderID` or `origClOrdID` to identify the order you wish to amend.

Both order quantity and price can be amended. Only one `qty` field can be used to amend.

Use the `leavesQty` field to specify how much of the order you wish to remain open. This can be useful
if you want to adjust your position's delta by a certain amount, regardless of how much of the order has
already filled.

> A `leavesQty` can be used to make a "Filled" order live again, if it is received within 60 seconds of the fill.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| orderID | formData | string | False | Order ID |
| origClOrdID | formData | string | False | Client Order ID. See POST /order. |
| clOrdID | formData | string | False | Optional new Client Order ID, requires `origClOrdID`. |
| simpleOrderQty | formData | number | False | Deprecated: simple orders are not supported after 2018/10/26 |
| orderQty | formData | number | False | Optional order quantity in units of the instrument (i.e. contracts, for spot it is the base currency |
| simpleLeavesQty | formData | number | False | Deprecated: simple orders are not supported after 2018/10/26 |
| leavesQty | formData | number | False | Optional leaves quantity in units of the instrument (i.e. contracts, for spot it is the base currenc |
| price | formData | number | False | Optional limit price for 'Limit', 'StopLimit', and 'LimitIfTouched' orders. |
| stopPx | formData | number | False | Optional trigger price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders. Use  |
| pegOffsetValue | formData | number | False | Optional trailing offset from the current price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'Lim |
| text | formData | string | False | Optional amend annotation. e.g. 'Adjust skew'. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### DELETE `/order`

**Cancel order(s). Send multiple order IDs to cancel in bulk.**

Either an orderID or a clOrdID must be provided.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| orderID | formData | string | False | Order ID(s). |
| clOrdID | formData | string | False | Client Order ID(s). See POST /order. |
| text | formData | string | False | Optional cancellation annotation. e.g. 'Spread Exceeded'. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### DELETE `/order/all`

**Cancels all of your orders.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountIds | formData | string | False | AccountIds to cancel all orders, must be a paired account with main user. Also accepts wildcard, [*] |
| symbol | formData | string | False | Optional symbol. If provided, only cancels orders for that symbol. |
| filter | formData | string | False | Optional filter for cancellation. Use to only cancel some orders, e.g. `{"side": "Buy"}`. |
| text | formData | string | False | Optional cancellation annotation. e.g. 'Spread Exceeded' |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/order/cancelAllAfter`

**Automatically cancel all your orders after a specified timeout.**

Useful as a dead-man's switch to ensure your orders are canceled in case of an outage.
If called repeatedly, the existing offset will be canceled and a new one will be inserted in its place.

Example usage: call this route at 15s intervals with an offset of 60000 (60s).
If this route is not called within 60 seconds, all your orders will be automatically canceled.

This is also available via [WebSocket](https://www.bitmex.com/app/wsAPI#Dead-Mans-Switch-Auto-Cancel).


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| timeout | formData | number | True | Timeout in ms. Set to 0 to cancel this timer.  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/order/closePosition`

**Close a position. [Deprecated, use POST /order with execInst: 'Close']**

If no `price` is specified, a market order will be submitted to close the whole of your position. This will also close all other open orders in this symbol.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Symbol of position to close. |
| price | formData | number | False | Optional limit price. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/orderBook/L2`

**Get current orderbook in vertical format.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | True | Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. |
| depth | query | number | False | Orderbook depth per side. Send 0 for full depth. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/porl/nonce`

**Get your Proof of Reserves nonce and data.**

## Proof of Reserves Nonce

This endpoint will return the nonce and associated data needed to validate BitMEX reserves data.

<!-- TODO link to docs, GitHub, etc -->


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/porl/snapshots`

**Get Proof of Reserves historical snapshots**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/position`

**Get your positions.**

This endpoint is used for retrieving position information. The fields largely follow the [FIX spec](http://www.onixs.biz/fix-dictionary/5.0.SP2/msgType_AP_6580.html) definitions. Some selected fields are explained in more detail below.

The fields _account_, _symbol_, _currency_ are unique to each position and form its key.

Spot trading symbols returns a subset of the position fields, mainly the open order aggregates.

- **account**: Your unique account ID.
- **symbol**: The contract for this position.
- **currency**: The margin currency for this position.
- **underlying**: Meta data of the _symbol_.
- **quoteCurrency**: Meta data of the _symbol_, All prices are in the _quoteCurrency_
- **commission**: The maximum of the maker, taker, and settlement fee.
- **initMarginReq**: The initial margin requirement. This will be at least the symbol's default initial maintenance margin, but can be higher if you choose lower leverage.
- **maintMarginReq**: The maintenance margin requirement. This will be at least the symbol's default maintenance maintenance margin, but can be higher if you choose a higher risk limit.
- **riskLimit**: This is a function of your _maintMarginReq_.
- **leverage**: 1 / initMarginReq.
- **crossMargin**: True/false depending on whether you set cross margin on this position.
- **deleveragePercentile**: Indicates where your position is in the ADL queue.
- **rebalancedPnl**: The value of realised PNL that has transferred to your wallet for this position.
- **prevRealisedPnl**: The value of realised PNL that has transferred to your wallet for this position since the position was closed.
- **currentQty**: The current position amount in contracts.
- **currentCost**: The current cost of the position in the settlement currency of the symbol (_currency_).
- **currentComm**: The current commission of the position in the settlement currency of the symbol (_currency_).
- **realisedCost**: The realised cost of this position calculated with regard to average cost accounting.
- **unrealisedCost**: _currentCost_ - _realisedCost_.
- **grossOpenPremium**: The amount your bidding above the mark price in the settlement currency of the symbol (_currency_).
- **markPrice**: The mark price of the symbol in _quoteCurrency_.
- **markValue**: The _currentQty_ at the mark price in the settlement currency of the symbol (_currency_).
- **homeNotional**: Value of position in units of _underlying_.
- **foreignNotional**: Value of position in units of _quoteCurrency_.
- **realisedPnl**: The negative of _realisedCost_.
- **unrealisedPnl**: _unrealisedGrossPnl_.
- **liquidationPrice**: Once markPrice reaches this price, this position will be liquidated.
- **bankruptPrice**: Once markPrice reaches this price, this position will have no equity.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| filter | query | string | False | Table filter. For example, send {"symbol": "XBTUSD"}. |
| columns | query | string | False | Which columns to fetch. For example, send ["columnName"]. |
| count | query | number | False | Number of rows to fetch. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/position/crossLeverage`

**Choose leverage for a cross position.**

Users can choose an isolated leverage. This will automatically enable isolated margin.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Symbol of position to adjust. |
| leverage | formData | number | True | Leverage value. Send a number between 0.01 and 100 to enable isolated margin with a fixed leverage.  |
| targetAccountId | formData | number | False | AccountId for the position that the leverage would be changed on, must be a paired account with main |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/position/isolate`

**Enable isolated margin or cross margin per-position.**

Users can switch isolate margin per-position. This function allows switching margin isolation (aka fixed margin) on and off.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Position symbol to isolate. |
| enabled | formData | boolean | False | True for isolated margin, false for cross margin. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/position/leverage`

**Choose leverage for a position.**

Users can choose an isolated leverage. This will automatically enable isolated margin.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Symbol of position to adjust. |
| leverage | formData | number | True | Leverage value. Send a number between 0.01 and 100 to enable isolated margin with a fixed leverage.  |
| targetAccountId | formData | number | False | AccountId for the position that the leverage would be changed on, must be a paired account with main |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/position/riskLimit`

**Update your risk limit.**

Risk Limits limit the size of positions you can trade at various margin levels. Larger positions require more margin. Please see the Risk Limit documentation for more details.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Symbol of position to update risk limit on. |
| riskLimit | formData | number | True | New Risk Limit, in Satoshis. |
| targetAccountId | formData | number | False | AccountId for the position that the risk limit would be updated on, must be a paired account with ma |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/position/transferMargin`

**Transfer equity in or out of a position.**

When margin is isolated on a position, use this function to add or remove margin from the position. Note that you cannot remove margin below the initial margin threshold.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True | Symbol of position to isolate. |
| amount | formData | number | True | Amount to transfer, in Satoshis. May be negative. |
| targetAccountId | formData | number | False | AccountId for the position that the margin would be transfered to, must be a paired account with mai |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/quote`

**Get Quotes.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/quote/bucketed`

**Get previous quotes in time buckets.**

Timestamps returned by our bucketed endpoints are the **end** of the period, indicating when the bucket was written to disk. Some other common systems use the timestamp as the beginning of the period. Please be aware of this when using this endpoint.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| binSize | query | string | False | Time interval to bucket by. Available options: [1m,5m,1h,1d]. |
| partial | query | boolean | False | If true, will send in-progress (incomplete) bins for the current time period. |
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/referralCode`

**Create a new referral code**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| data | body |  | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/referralCode`

**Returns all referral codes for the logged-in user**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/referralCode/check/{code}`

**Check if a referral code is valid**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| code | path | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/referralCode/code/{code}`

**Get a referral code by code**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| code | path | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### PUT `/referralCode/{id}`

**Update an existing referral code**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| id | path | number | True |  |
| data | body |  | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### DELETE `/referralCode/{id}`

**Delete a referral code**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| id | path | number | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/referralCode/{id}`

**Get a referral code by ID**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| id | path | number | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/schema`

**Get model schemata for data objects returned by this API.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| model | query | string | False | Optional model filter. If omitted, will return all models. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/schema/websocketHelp`

**Returns help text & subject list for websocket usage.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/settlement`

**Get settlement history.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/stats`

**Get exchange-wide and per-series turnover and volume statistics.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/stats/history`

**Get historical exchange-wide and per-series turnover and volume statistics.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/stats/historyUSD`

**Get a summary of exchange statistics in USD.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/trade`

**Get Trades.**

Please note that indices (symbols starting with `.`) post trades at intervals to the trade feed. These have a `size` of 0 and are used only to indicate a changing price.

See [the FIX Spec](http://www.onixs.biz/fix-dictionary/5.0.SP2/msgType_AE_6569.html) for explanations of these fields.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/trade/bucketed`

**Get previous trades in time buckets.**

Timestamps returned by our bucketed endpoints are the **end** of the period, indicating when the bucket was written to disk. Some other common systems use the timestamp as the beginning of the period. Please be aware of this when using this endpoint.

Also note the `open` price is equal to the `close` price of the previous timeframe bucket.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| binSize | query | string | False | Time interval to bucket by. Available options: [1m,5m,1h,1d]. |
| partial | query | boolean | False | If true, will send in-progress (incomplete) bins for the current time period. |
| symbol | query | string | False | Instrument symbol. Send a bare series (e.g. XBT) to get data for the nearest expiring contract in th |
| filter | query | string | False | Generic table filter. Send JSON key/value pairs, such as `{"key": "value"}`. You can key on individu |
| columns | query | string | False | Array of column names to fetch. If omitted, will return all columns.  Note that this method will alw |
| count | query | number | False | Number of results to fetch. Must be a positive integer. |
| start | query | number | False | Starting point for results. |
| reverse | query | boolean | False | If true, will sort results newest first. |
| startTime | query | string | False | Starting date filter for results. |
| endTime | query | string | False | Ending date filter for results. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user`

**Get your user model.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/addSubaccount`

**Creates a new sub-account.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| accountName | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/affiliateStatus`

**Get your current affiliate/referral status.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/cancelWithdrawal`

**Cancel a withdrawal.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| token | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/checkReferralCode`

**Check if a referral code is valid.**

If the code is valid, responds with the referral code's discount (e.g. `0.1` for 10%). Otherwise, will return a 404 or 451 if invalid.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| referralCode | query | string | False |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/commission`

**Get your account's commission status.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/communicationToken`

**Register your communication token for mobile clients**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| token | formData | string | True |  |
| platformAgent | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/confirmEmail`

**Confirm your email address with a token.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| token | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/confirmWithdrawal`

**Confirm a withdrawal.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| token | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/createIndependentSubaccount`

**Creates a new independant sub-account.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| email | formData | string | True |  |
| accountName | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/csa`

**Get your account's CSA status.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/depositAddress`

**Get a deposit address.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | True | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |
| network | query | string | True | The `network` parameter is used to indicate which blockchain you would like to deposit from. The acc |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/depositAddressInformation`

**Get a deposit address.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | True | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |
| network | query | string | True | The `network` parameter is used to indicate which blockchain you would like to deposit from. The acc |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/executionHistory`

**Get the execution history by day.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | True |  |
| timestamp | query | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/getWalletTransferAccounts`

**Get the list of accounts you can transfer funds between.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/logout`

**Log out of BitMEX.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/margin`

**Get your account's margin status. Send a currency of "all" to receive an array of all supported currencies.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/marginingMode`

**This function allows switching margining mode between single-asset margining and multi-asset margining.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountId | formData | number | False | AccountId to update the margining mode of. |
| marginingMode | formData | string | False | Margining mode. Provide the value MultiAsset for multi-asset margining. Leave the field empty for si |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/preferences`

**Save user preferences.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| prefs | formData | string | True |  |
| overwrite | formData | boolean | False | If true, will overwrite all existing preferences. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/quoteFillRatio`

**Get 7 days worth of Quote Fill Ratio statistics.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountId | query | number | False | AccountId to get quote fill ratio for, must be a paired account with main user. Can be wildcard * to |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/quoteValueRatio`

**Get Quote Value Ratio statistics over the last 3 days**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountId | query | number | False | AccountId to get quote value ratio for, must be a paired account with main user. Can be wildcard * t |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/requestWithdrawal`

**Request a withdrawal to an external wallet or separate BitMEX account.**

### Email Confirmation

In most cases, this endpoint will send a confirmation email to the email address on record. When withdrawing to a saved address (i.e. given `addressId` or a corresponding `address`) with `skipConfirm` configured, the withdrawal will be immediately confirmed.

### Two-Factor Authentication

A valid 2FA code (`otpToken`) is required for all withdrawals unless the destination address is associated with either a saved address with `skip2FA` configured or a linked BitMEX account (e.g. a subaccount).

### Internal Transfers

If a valid BitMEX deposit address is provided, the transaction will be made directly between BitMEX accounts. There will be no resulting on-chain transaction and no network fee will be charged.

When given another account ID (`targetUserId`), the request will only succeed if the account is linked to the authenticated account.

Note that `/api/v1/user/walletTransfer` may be a more suitable endpoint for transfers between linked accounts.

### Saved Address Verification

Please note that when using saved addresses, `skip2FA` and `skipConfirm` require verification:
 - `skip2FA` can be verified by providing `otpToken` when creating the address. If `otpToken` is not provided, a 2FA code can be provided by visiting the link included in the email sent upon address creation.

 - `skipConfirm` can be verified by visiting the link included in the email sent upon address creation.

### Whitelist

If the address book has the `whitelist` setting enabled, all withdrawal requests must be directed to either a saved addresses or a linked account. All other addresses will be rejected. Note that saved addresses must be __active__. A new saved address is active if it has been 2FA verified and a cooldown period has passed since its creation.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| otpToken | formData | string | False | 2FA token. Required for all external withdrawals unless the destination is a saved address with `ski |
| currency | formData | string | True | Currency you're withdrawing. Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAsse |
| network | formData | string | True | The `network` parameter is used to indicate which blockchain you would like to withdraw from. The ac |
| amount | formData | number | True | Amount of withdrawal currency. |
| address | formData | string | False | Destination Address. One of `address`, `addressId`, `targetUserId` has to be specified. |
| memo | formData | string | False | Destination Memo. If `address`, is specified, destination Memo can also be specified. If given an `a |
| addressId | formData | number | False | ID of the Destination Address. One of `address`, `addressId`, `targetUserId` has to be specified. |
| targetUserId | formData | number | False | ID of a linked BitMEX account. One of `address`, `addressId`, `targetUserId` has to be specified. |
| fee | formData | number | False | Network fee for Bitcoin withdrawals. If not specified, a default value will be calculated based on B |
| text | formData | string | False | Optional annotation, e.g. 'Transfer to home wallet'. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/staking`

**Get the current user staking amount.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/staking/instruments`

**List staking instruments**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | query | string | False |  |
| currency | query | string | False |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/staking/tiers`

**List staking tiers for a given currency**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/tradingVolume`

**Get your 30 days USD average trading volume**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/unstakingRequests`

**Get the current user unstaking requests**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| status | query | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/unstakingRequests`

**Create unstaking request**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| symbol | formData | string | True |  |
| amount | formData | number | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### DELETE `/user/unstakingRequests`

**Cancel unstaking request**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| redemptionID | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/updateSubaccount`

**Updates the sub-account name.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| targetAccountId | formData | number | True |  |
| accountName | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/wallet`

**Get your current wallet information.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/walletHistory`

**Get a history of all of your wallet transactions (deposits, withdrawals, PNL).**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |
| count | query | number | False | Number of results to fetch. Fetch results from start to start + count. Max: 10,000 rows. |
| start | query | number | False | Starting point for results, integer. Default 0. |
| targetAccountId | query | number | False | AccountId to view the history of, must be a paired account with the authorised user requesting the h |
| reverse | query | boolean | False | Start from the latest transaction record. Default true. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/user/walletSummary`

**Get a summary of all of your wallet transactions (deposits, withdrawals, PNL).**

Provides an aggregated view of transactions, by transaction type, over a specific time period.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | query | string | False | Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAssetsConfig">asset config endpoi |
| startTime | query | string | False | Start time for the summary |
| endTime | query | string | False | End time for the summary |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### POST `/user/walletTransfer`

**Execute a transfer to a linked account.**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| currency | formData | string | True | Currency you're transfering. Any currency. For all currencies, see <a href="#!/Wallet/Wallet_getAsse |
| amount | formData | number | True | Amount of transfer. |
| fromAccountId | formData | number | False | AccountID to send the transfer from. Must be paired account with the authenticated user. |
| targetAccountId | formData | number | True | AccountId to send the transfer to, must be a paired account with the user sending the transfer. |
| includeVouchers | formData | boolean | False | Whether to include vouchers in the transfer. Defaults to false. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### DELETE `/user/withdrawal`

**Cancel pending withdrawal**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| transactID | formData | string | True |  |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/userAffiliates`

**Get user's affiliates to a given depth**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| depth | query | number | False | the depth of affiliates to return. Eg depth = 2 would return direct affiliates and their affiliates |
| targetAccountId | query | number | False | AccountId of Sub-Affiliate Account |
| selectUserId | query | number | False | User id of result array to keep |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/userEvent`

**Get your user events**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| count | query | number | False | Number of results to fetch. |
| startId | query | number | False | Cursor for pagination. |

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/wallet/assets`

**Get Assets Config**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/wallet/haircuts`

**Get Frontend Currency Config**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

### GET `/wallet/networks`

**Get Networks Config**

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Request was successful
- `400`: Parameter Error
- `401`: Unauthorized
- `403`: Access Denied
- `404`: Not Found

## Schemas

### APIKey

Persistent API Keys for Developers

| Property | Type | Description |
|----------|------|-------------|
| id | string |  |
| secret | string |  |
| name | string |  |
| nonce | number |  |
| cidr | string |  |
| cidrs | array |  |
| targetAccountId | number |  |
| permissions | array |  |
| enabled | boolean |  |
| userId | number |  |
| created | string |  |

### AccessToken

| Property | Type | Description |
|----------|------|-------------|
| updated | string |  |
| targetTtl | number |  |
| authorizedAccounts | object |  |
| id | string |  |
| ttl | number | time to live in seconds (2 weeks by default) |
| created | string |  |
| userId | number |  |

### Account

Account information

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| state | string |  |
| typ | string |  |
| settlementFeeDiscount | number |  |
| insuranceFeeDiscount | number |  |
| referralDiscount | number |  |
| referrerAccount | number |  |
| affiliatePayout | number |  |
| affiliateDiscount | number |  |
| isSuspended | boolean |  |
| marginingMode | string |  |
| positionMode | string |  |
| timeoutTimestamp | string |  |
| makerFeeDiscount | number |  |
| takerFeeDiscount | number |  |
| timestamp | string |  |
| apiBrokerID | number |  |

### Address

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| currency | string |  |
| created | string |  |
| userId | number |  |
| address | string |  |
| name | string |  |
| note | string |  |
| skipConfirm | boolean |  |
| skipConfirmVerified | boolean |  |
| skip2FA | boolean |  |
| skip2FAVerified | boolean |  |
| network | string |  |
| memo | string |  |
| cooldownExpires | string |  |
| verified | boolean |  |

### AddressConfig

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| whitelist | boolean |  |
| created | string |  |
| disabled | string |  |
| userId | number |  |
| defaultCooldown | number |  |
| frozen | boolean |  |

### Affiliate

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| currency | string |  |
| prevPayout | number |  |
| prevTurnover | number |  |
| prevComm | number |  |
| prevTimestamp | string |  |
| execTurnover | number |  |
| execComm | number |  |
| totalReferrals | number |  |
| totalTurnover | number |  |
| totalComm | number |  |
| payoutPcnt | number |  |
| pendingPayout | number |  |
| timestamp | string |  |
| referrerAccount | number |  |
| referralDiscount | number |  |
| affiliatePayout | number |  |

### Announcement

Public Announcements

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| link | string |  |
| title | string |  |
| content | string |  |
| date | string |  |

### AssetsConfig

| Property | Type | Description |
|----------|------|-------------|
| asset | string |  |
| currency | string |  |
| majorCurrency | string |  |
| name | string |  |
| currencyType | string |  |
| scale | number |  |
| enabled | boolean |  |
| isMarginCurrency | boolean |  |
| memoRequired | boolean |  |
| networks | array |  |

### AssetsConfigNetworkItem

| Property | Type | Description |
|----------|------|-------------|
| asset | string |  |
| tokenAddress | string |  |
| depositEnabled | boolean |  |
| withdrawalEnabled | boolean |  |
| withdrawalFee | number |  |
| minFee | number |  |
| maxFee | number |  |

### Beneficiary

| Property | Type | Description |
|----------|------|-------------|
| type | string |  |
| entityType | string |  |
| firstName | string |  |
| lastName | string |  |
| fullName | string |  |
| id | number |  |

### Chat

Trollbox Data

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| date | string |  |
| user | string |  |
| userColor | string |  |
| message | string |  |
| html | string |  |
| channelID | number |  |

### ChatChannel

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| name | string |  |
| isPrivate | boolean |  |

### CollateralSupportAgreement

| Property | Type | Description |
|----------|------|-------------|
| csaID | string |  |
| account | number |  |
| currency | string |  |
| amount | number |  |
| minAmount | number |  |
| threshold | number |  |
| mmRatioMarginCall | number |  |
| mmRatioLiquidation | number |  |
| startTime | string |  |
| maturityTime | string |  |
| maturityInstruction | string |  |
| csaStatus | string |  |
| requester | string |  |
| clientDetails | string |  |
| text | string |  |
| timestamp | string |  |

### ConnectedUsers

| Property | Type | Description |
|----------|------|-------------|
| users | number |  |
| bots | number |  |

### DepositAddress

Deposit Address

| Property | Type | Description |
|----------|------|-------------|
| address | string |  |
| memo | string |  |

### Error

| Property | Type | Description |
|----------|------|-------------|
| error | object |  |

### Execution

Raw Order and Balance Data

| Property | Type | Description |
|----------|------|-------------|
| execID | string |  |
| orderID | string |  |
| origClOrdID | string |  |
| clOrdID | string |  |
| clOrdLinkID | string |  |
| account | number |  |
| symbol | string |  |
| strategy | string |  |
| side | string |  |
| lastQty | number |  |
| lastPx | number |  |
| lastLiquidityInd | string |  |
| orderQty | number |  |
| price | number |  |
| displayQty | number |  |
| stopPx | number |  |
| pegOffsetValue | number |  |
| pegPriceType | string |  |
| currency | string |  |
| settlCurrency | string |  |
| execType | string |  |
| ordType | string |  |
| timeInForce | string |  |
| execInst | string |  |
| contingencyType | string |  |
| ordStatus | string |  |
| triggered | string |  |
| workingIndicator | boolean |  |
| ordRejReason | string |  |
| leavesQty | number |  |
| cumQty | number |  |
| avgPx | number |  |
| commission | number |  |
| brokerCommission | number |  |
| feeType | string |  |
| tradePublishIndicator | string |  |
| text | string |  |
| trdMatchID | string |  |
| execCost | number |  |
| execComm | number |  |
| execCommCcy | string |  |
| brokerExecComm | number |  |
| homeNotional | number |  |
| foreignNotional | number |  |
| transactTime | string |  |
| timestamp | string |  |
| realisedPnl | number |  |
| trdType | string |  |
| maxSlippagePct | number |  |
| pool | string |  |
| destination | string |  |
| algoOrderDetails | object |  |
| error | string |  |

### Funding

Swap Funding History

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| fundingInterval | string |  |
| fundingRate | number |  |
| fundingRateDaily | number |  |

### GlobalNotification

Account Notifications

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| date | string |  |
| title | string |  |
| body | string |  |
| ttl | number |  |
| type | string |  |
| closable | boolean |  |
| persist | boolean |  |
| waitForVisibility | boolean |  |
| sound | string |  |

### Guild

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| created | string |  |
| updated | string |  |
| archived | boolean |  |
| name | string |  |
| imgUrl | string |  |
| mobileHeroImgUrl | string |  |
| emoji | string |  |
| logoUrl | string |  |
| description | string |  |
| chatChannelId | number |  |
| isPrivate | boolean |  |
| affiliateId | string |  |
| potDistributionPreferences | object |  |
| socials | object |  |
| deleted | boolean |  |

### IndexComposite

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| indexSymbol | string |  |
| indexMultiplier | number |  |
| reference | string |  |
| lastPrice | number |  |
| sourcePrice | number |  |
| conversionIndex | string |  |
| conversionIndexPrice | number |  |
| weight | number |  |
| logged | string |  |

### Instrument

Tradeable Contracts, Indices, and History

| Property | Type | Description |
|----------|------|-------------|
| symbol | string |  |
| rootSymbol | string |  |
| state | string |  |
| typ | string |  |
| listing | string |  |
| front | string |  |
| expiry | string |  |
| settle | string |  |
| listedSettle | string |  |
| positionCurrency | string |  |
| underlying | string |  |
| quoteCurrency | string |  |
| underlyingSymbol | string |  |
| reference | string |  |
| referenceSymbol | string |  |
| calcInterval | string |  |
| publishInterval | string |  |
| publishTime | string |  |
| maxOrderQty | number |  |
| minPrice | number |  |
| maxPrice | number |  |
| lotSize | number |  |
| tickSize | number |  |
| multiplier | number |  |
| settlCurrency | string |  |
| underlyingToPositionMultiplier | number |  |
| underlyingToSettleMultiplier | number |  |
| quoteToSettleMultiplier | number |  |
| isQuanto | boolean |  |
| isInverse | boolean |  |
| initMargin | number |  |
| maintMargin | number |  |
| riskLimit | number |  |
| riskStep | number |  |
| limit | number |  |
| taxed | boolean |  |
| deleverage | boolean |  |
| makerFee | number |  |
| takerFee | number |  |
| settlementFee | number |  |
| fundingBaseSymbol | string |  |
| fundingQuoteSymbol | string |  |
| fundingPremiumSymbol | string |  |
| fundingTimestamp | string |  |
| fundingInterval | string |  |
| fundingRate | number |  |
| indicativeFundingRate | number |  |
| rebalanceTimestamp | string |  |
| rebalanceInterval | string |  |
| launchingTimestamp | string |  |
| prevClosePrice | number |  |
| limitDownPrice | number |  |
| limitUpPrice | number |  |
| totalVolume | number |  |
| volume | number |  |
| volume24h | number |  |
| prevTotalTurnover | number |  |
| totalTurnover | number |  |
| turnover | number |  |
| turnover24h | number |  |
| homeNotional24h | number |  |
| foreignNotional24h | number |  |
| prevPrice24h | number |  |
| vwap | number |  |
| highPrice | number |  |
| lowPrice | number |  |
| lastPrice | number |  |
| lastPriceProtected | number |  |
| lastTickDirection | string |  |
| lastChangePcnt | number |  |
| bidPrice | number |  |
| midPrice | number |  |
| askPrice | number |  |
| impactBidPrice | number |  |
| impactMidPrice | number |  |
| impactAskPrice | number |  |
| hasLiquidity | boolean |  |
| openInterest | number |  |
| openValue | number |  |
| fairMethod | string |  |
| fairBasisRate | number |  |
| fairBasis | number |  |
| fairPrice | number |  |
| markMethod | string |  |
| markPrice | number |  |
| indicativeSettlePrice | number |  |
| settledPriceAdjustmentRate | number |  |
| settledPrice | number |  |
| instantPnl | boolean |  |
| minTick | number |  |
| fundingBaseRate | number |  |
| fundingQuoteRate | number |  |
| farLegSymbol | string |  |
| nearLegSymbol | string |  |
| timestamp | string |  |

### InstrumentInterval

| Property | Type | Description |
|----------|------|-------------|
| intervals | array |  |
| symbols | array |  |

### Insurance

Insurance Fund Data

| Property | Type | Description |
|----------|------|-------------|
| currency | string |  |
| timestamp | string |  |
| walletBalance | number |  |

### Leaderboard

Information on Top Users

| Property | Type | Description |
|----------|------|-------------|
| name | string |  |
| isRealName | boolean |  |
| profit | number |  |

### Liquidation

Active Liquidations

| Property | Type | Description |
|----------|------|-------------|
| orderID | string |  |
| symbol | string |  |
| side | string |  |
| price | number |  |
| leavesQty | number |  |

### Margin

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| currency | string |  |
| riskLimit | number |  |
| state | string |  |
| amount | number |  |
| prevRealisedPnl | number |  |
| grossComm | number |  |
| grossOpenCost | number |  |
| grossOpenPremium | number |  |
| grossExecCost | number |  |
| grossMarkValue | number |  |
| riskValue | number |  |
| initMargin | number |  |
| maintMargin | number |  |
| targetExcessMargin | number |  |
| realisedPnl | number |  |
| unrealisedPnl | number |  |
| walletBalance | number |  |
| marginBalance | number |  |
| marginLeverage | number |  |
| marginUsedPcnt | number |  |
| excessMargin | number |  |
| availableMargin | number |  |
| withdrawableMargin | number |  |
| systemWithdrawableMargin | number |  |
| makerFeeDiscount | number |  |
| takerFeeDiscount | number |  |
| timestamp | string |  |
| foreignMarginBalance | number |  |
| foreignRequirement | number |  |

### NetworksConfig

| Property | Type | Description |
|----------|------|-------------|
| network | string |  |
| name | string |  |
| currency | string |  |
| networkSymbol | string |  |
| transactionExplorer | string |  |
| tokenExplorer | string |  |
| depositConfirmations | number |  |
| enabled | boolean |  |

### Order

Placement, Cancellation, Amending, and History

| Property | Type | Description |
|----------|------|-------------|
| orderID | string |  |
| currency | string |  |
| ordRejReason | string |  |
| pegPriceType | string |  |
| cumQty | number |  |
| workingIndicator | boolean |  |
| destination | string |  |
| side | string |  |
| triggered | string |  |
| timestamp | string |  |
| strategy | string |  |
| text | string |  |
| orderQty | number |  |
| clOrdID | string |  |
| price | number |  |
| transactTime | string |  |
| settlCurrency | string |  |
| leavesQty | number |  |
| ordType | string |  |
| avgPx | number |  |
| stopPx | number |  |
| displayQty | number |  |
| algoOrderDetails | object |  |
| execInst | string |  |
| pool | string |  |
| error | string |  |
| pegOffsetValue | number |  |
| contingencyType | string |  |
| clOrdLinkID | string |  |
| symbol | string |  |
| maxSlippagePct | number |  |
| account | number |  |
| ordStatus | string |  |
| timeInForce | string |  |

### OrderBookL2

| Property | Type | Description |
|----------|------|-------------|
| symbol | string |  |
| id | number |  |
| side | string |  |
| size | number |  |
| price | number |  |
| pool | string |  |
| timestamp | string |  |
| transactTime | string |  |

### PinnedMessage

Pinned Messages

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| channelID | number |  |
| messageId | number |  |
| created | string |  |
| ended | string |  |
| createdUserId | number |  |
| endedUserId | number |  |

### Porl

Proof of Reserves/Liabilities

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| nonce | string |  |
| accountNonce | string |  |
| total | number |  |
| balance | number |  |
| filename | string |  |
| height | number |  |
| created | string |  |

### Position

Summary of Open and Closed Positions

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| symbol | string |  |
| strategy | string |  |
| currency | string |  |
| underlying | string |  |
| quoteCurrency | string |  |
| commission | number |  |
| initMarginReq | number |  |
| maintMarginReq | number |  |
| riskLimit | number |  |
| leverage | number |  |
| crossMargin | boolean |  |
| deleveragePercentile | number |  |
| rebalancedPnl | number |  |
| prevRealisedPnl | number |  |
| prevUnrealisedPnl | number |  |
| openingQty | number |  |
| openOrderBuyQty | number |  |
| openOrderBuyCost | number |  |
| openOrderBuyPremium | number |  |
| openOrderSellQty | number |  |
| openOrderSellCost | number |  |
| openOrderSellPremium | number |  |
| currentQty | number |  |
| currentCost | number |  |
| currentComm | number |  |
| realisedCost | number |  |
| unrealisedCost | number |  |
| grossOpenPremium | number |  |
| isOpen | boolean |  |
| markPrice | number |  |
| markValue | number |  |
| riskValue | number |  |
| homeNotional | number |  |
| foreignNotional | number |  |
| posState | string |  |
| posCost | number |  |
| posCross | number |  |
| posComm | number |  |
| posLoss | number |  |
| posMargin | number |  |
| posMaint | number |  |
| initMargin | number |  |
| maintMargin | number |  |
| realisedPnl | number |  |
| unrealisedPnl | number |  |
| unrealisedPnlPcnt | number |  |
| unrealisedRoePcnt | number |  |
| avgCostPrice | number |  |
| avgEntryPrice | number |  |
| breakEvenPrice | number |  |
| marginCallPrice | number |  |
| liquidationPrice | number |  |
| bankruptPrice | number |  |
| timestamp | string |  |

### Quote

Best Bid/Offer Snapshots & Historical Bins

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| bidSize | number |  |
| bidPrice | number |  |
| askPrice | number |  |
| askSize | number |  |
| pool | string |  |

### QuoteFillRatio

Daily Quote Fill Ratio Statistic

| Property | Type | Description |
|----------|------|-------------|
| date | string |  |
| account | number |  |
| quoteCount | number |  |
| dealtCount | number |  |
| quotesMavg7 | number |  |
| dealtMavg7 | number |  |
| quoteFillRatioMavg7 | number |  |

### QuoteValueRatio

Hourly Quote Value Ratio Statistic

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| account | number |  |
| symbol | string |  |
| quoteCount | number |  |
| volumeXBT | number |  |
| QVR | number |  |
| id | number |  |

### ReferralCode

| Property | Type | Description |
|----------|------|-------------|
| id | string |  |
| userId | number |  |
| code | string |  |
| details | object |  |
| created | string |  |
| modified | string |  |
| isDefault | boolean |  |
| isPrimary | boolean |  |

### Settlement

Historical Settlement Data

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| settlementType | string |  |
| settledPrice | number |  |
| optionStrikePrice | number |  |
| optionUnderlyingPrice | number |  |
| bankrupt | number |  |
| taxBase | number |  |
| taxRate | number |  |

### StakingRecord

Get the current user staking amount in vertical format.

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| amount | number |  |
| currency | string |  |

### Stats

Exchange Statistics

| Property | Type | Description |
|----------|------|-------------|
| rootSymbol | string |  |
| currency | string |  |
| volume24h | number |  |
| turnover24h | number |  |
| openInterest | number |  |
| openValue | number |  |

### StatsHistory

| Property | Type | Description |
|----------|------|-------------|
| date | string |  |
| rootSymbol | string |  |
| currency | string |  |
| volume | number |  |
| turnover | number |  |

### StatsUSD

| Property | Type | Description |
|----------|------|-------------|
| rootSymbol | string |  |
| currency | string |  |
| turnover24h | number |  |
| turnover30d | number |  |
| turnover365d | number |  |
| turnover | number |  |

### StatsUSDBySymbol

| Property | Type | Description |
|----------|------|-------------|
| symbol | string |  |
| currency | string |  |
| turnover24h | number |  |
| turnover30d | number |  |
| turnover365d | number |  |
| turnover | number |  |

### Trade

Individual & Bucketed Trades

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| side | string |  |
| size | number |  |
| price | number |  |
| tickDirection | string |  |
| trdMatchID | string |  |
| grossValue | number |  |
| homeNotional | number |  |
| foreignNotional | number |  |
| trdType | string |  |
| pool | string |  |

### TradeBin

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string |  |
| symbol | string |  |
| open | number |  |
| high | number |  |
| low | number |  |
| close | number |  |
| trades | number |  |
| volume | number |  |
| vwap | number |  |
| lastSize | number |  |
| turnover | number |  |
| homeNotional | number |  |
| foreignNotional | number |  |
| pool | string |  |

### TradingVolume

30 days USD average trading volume

| Property | Type | Description |
|----------|------|-------------|
| advUsd | number |  |
| advUsdSpot | number |  |
| advUsdContract | number |  |

### Transaction

| Property | Type | Description |
|----------|------|-------------|
| transactID | string |  |
| account | number |  |
| currency | string |  |
| network | string |  |
| transactType | string |  |
| amount | number |  |
| walletBalance | number |  |
| fee | number |  |
| transactStatus | string |  |
| address | string |  |
| tx | string |  |
| orderID | string |  |
| text | string |  |
| transactTime | string |  |
| timestamp | string |  |
| memo | string |  |
| subType | string |  |

### User

Account Operations

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| firstname | string |  |
| lastname | string |  |
| username | string |  |
| accountName | string |  |
| isUser | boolean |  |
| email | string |  |
| dateOfBirth | string |  |
| phone | string |  |
| created | string |  |
| lastUpdated | string |  |
| preferences | #/definitions/UserPreferences |  |
| TFAEnabled | string |  |
| affiliateID | string |  |
| country | string |  |
| geoipCountry | string |  |
| geoipRegion | string |  |
| firstTradeTimestamp | string |  |
| firstDepositTimestamp | string |  |
| isElite | boolean |  |
| lastKnownAuthority | string |  |
| typ | string |  |

### UserCommissionsBySymbol

| Property | Type | Description |
|----------|------|-------------|

### UserEvent

User Events for Auditing

| Property | Type | Description |
|----------|------|-------------|
| id | number |  |
| type | string |  |
| status | string |  |
| userId | number |  |
| createdById | number |  |
| ip | string |  |
| geoipCountry | string |  |
| geoipRegion | string |  |
| geoipSubRegion | string |  |
| eventMeta | object |  |
| created | string |  |

### UserPreferences

| Property | Type | Description |
|----------|------|-------------|
| alertOnLiquidations | boolean |  |
| animationsEnabled | boolean |  |
| announcementsLastSeen | string |  |
| botsAdvancedMode | boolean |  |
| botVideosHidden | boolean |  |
| chatChannelID | number |  |
| colorTheme | string |  |
| currency | string |  |
| debug | boolean |  |
| disableChartQuotes | boolean |  |
| disableEmails | array |  |
| disablePush | array |  |
| displayCorpEnrollUpsell | boolean |  |
| equivalentCurrency | string |  |
| features | array |  |
| favourites | array |  |
| favouritesAssets | array |  |
| favouritesOrdered | array |  |
| favouriteBots | array |  |
| favouriteContracts | array |  |
| hasSetTradingCurrencies | boolean |  |
| hideConfirmDialogs | array |  |
| hideConnectionModal | boolean |  |
| hideFromLeaderboard | boolean |  |
| hideNameFromLeaderboard | boolean |  |
| hidePnlInGuilds | boolean |  |
| hideRoiInGuilds | boolean |  |
| hideNotifications | array |  |
| hidePhoneConfirm | boolean |  |
| guidesShownVersion | number |  |
| pnlDashboardGuidesShownVersion | number |  |
| isSensitiveInfoVisible | boolean |  |
| isWalletZeroBalanceHidden | boolean |  |
| locale | string |  |
| localeSetTime | number |  |
| marginPnlRow | string |  |
| marginPnlRowKind | string |  |
| mobileLocale | string |  |
| msgsSeen | array |  |
| notifications | object |  |
| optionsBeta | boolean |  |
| orderBookBinning | object |  |
| orderBookBinningDisabled | boolean |  |
| orderBookType | string |  |
| orderClearImmediate | boolean |  |
| orderControlsPlusMinus | boolean |  |
| orderControlsOpenCloseTabs | boolean |  |
| orderControlsSlider | boolean |  |
| orderInputType | string |  |
| platformLayout | string |  |
| selectedFiatCurrency | string |  |
| showChartBottomToolbar | boolean |  |
| showLocaleNumbers | boolean |  |
| sounds | array |  |
| spacingPreference | string |  |
| strictIPCheck | boolean |  |
| strictTimeout | boolean |  |
| tickerGroup | string |  |
| tickerPinned | boolean |  |
| tradeLayout | string |  |
| userColor | string |  |
| videosSeen | array |  |

### Vasp

| Property | Type | Description |
|----------|------|-------------|
| addressType | string |  |
| name | string |  |
| website | string |  |
| id | string |  |
| did | string |  |
| source | string |  |

### Wallet

Assets and Networks Data

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| currency | string |  |
| deposited | number |  |
| withdrawn | number |  |
| transferIn | number |  |
| transferOut | number |  |
| amount | number |  |
| pendingCredit | number |  |
| pendingDebit | number |  |
| confirmedDebit | number |  |
| timestamp | string |  |

### WalletSummaryRecord

| Property | Type | Description |
|----------|------|-------------|
| account | number |  |
| currency | string |  |
| transactType | string |  |
| symbol | string |  |
| amount | number |  |
| pendingDebit | number |  |
| realisedPnl | number |  |
| walletBalance | number |  |
| unrealisedPnl | number |  |
| marginBalance | number |  |

### x-any

| Property | Type | Description |
|----------|------|-------------|

