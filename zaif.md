# Zaif API Documentation

Auto-fetched from 3 page(s)


---

# Source: https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html

[ Zaif API document ](index.html)

v2.1.0 

  * [現物公開API](#)
    * [共通情報](#id1)
      * [リクエスト方法](#id2)
      * [戻り値](#id3)
      * [エラーメッセージ](#id4)
      * [補足](#id5)
    * [個別情報](#id6)
      * [通貨情報の取得](#id7)
        * [リクエスト方法](#id8)
        * [パラメータ](#id9)
        * [戻り値](#id10)
        * [補足](#id11)
      * [通貨ペア情報の取得](#id12)
        * [リクエスト方法](#id13)
        * [パラメータ](#id14)
        * [戻り値](#id15)
        * [補足](#id16)
      * [現在の終値を取得](#id17)
        * [リクエスト方法](#id18)
        * [パラメータ](#id19)
        * [戻り値](#id20)
        * [エラーメッセージ](#id21)
      * [ティッカーの取得](#id22)
        * [リクエスト方法](#id23)
        * [パラメータ](#id24)
        * [戻り値](#id25)
        * [エラーメッセージ](#id26)
        * [補足](#id27)
      * [全ユーザー取引履歴の取得](#id28)
        * [リクエスト方法](#id29)
        * [パラメータ](#id30)
        * [戻り値](#id31)
        * [エラーメッセージ](#id32)
        * [補足](#id33)
      * [板情報の取得](#id34)
        * [リクエスト方法](#id35)
        * [パラメータ](#id36)
        * [戻り値](#id37)
        * [エラーメッセージ](#id38)
        * [補足](#id39)
      * [VASP情報の取得（ 2022年4月1日より取得可能 ）](#vasp-202241)
        * [リクエスト方法](#id40)
        * [パラメータ](#id41)
        * [戻り値](#id42)
      * [送金先国情報取得（ 2022年10月27日より取得可能 ）](#id43)
        * [リクエスト方法](#id44)
        * [パラメータ](#id45)
        * [戻り値](#id46)
      * [法人種別情報取得（ 2022年10月27日より取得可能 ）](#id47)
        * [リクエスト方法](#id48)
        * [パラメータ](#id49)
        * [戻り値](#id50)
  * [現物取引API](TradingAPI.html)
  * [信用取引 API](MarginTradingAPI.html)
  * [WebSocket API](WebSocket_API.html)
  * [OAuth API](OAuthAPI.html)
  * [決済 API](PaymentAPI.html)
  * [Q&A](Q%26A.html)
  * [その他](Others.html)



__[Zaif API document](index.html)

  * [](index.html)
  * 現物公開API
  * [ View page source](_sources/PublicAPI.md.txt)



* * *

# 現物公開API[](#api "この見出しへのパーマリンク")

  * [共通情報](#id1)

    * [リクエスト方法](#id2)

    * [戻り値](#id3)

    * [エラーメッセージ](#id4)

    * [補足](#id5)

  * [個別情報](#id6)

    * [通貨情報の取得](#id7)

    * [通貨ペア情報の取得](#id12)

    * [現在の終値を取得](#id17)

    * [ティッカーの取得](#id22)

    * [全ユーザー取引履歴の取得](#id28)

    * [板情報の取得](#id34)

    * [VASP情報の取得](#id39)

    * [送金先国情報取得](#id43)

    * [法人種別情報取得](#id47)




* * *

## 共通情報[](#id1 "この見出しへのパーマリンク")

現物公開APIの共通情報です。

* * *

### リクエスト方法[](#id2 "この見出しへのパーマリンク")

  * エンドポイント：https://api.zaif.jp/api/1

  * メソッド：GET




### 戻り値[](#id3 "この見出しへのパーマリンク")

  * 全てjson形式となっています。フォーマットはAPIによって変わります。




### エラーメッセージ[](#id4 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
unsupported method | サポート外のmethodです。  
  
### 補足[](#id5 "この見出しへのパーマリンク")

  * 呼び出しは1秒間に10回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。




* * *

## 個別情報[](#id6 "この見出しへのパーマリンク")

現物公開APIの個別情報です。

* * *

### 通貨情報の取得[](#id7 "この見出しへのパーマリンク")

通貨情報を取得します。

#### リクエスト方法[](#id8 "この見出しへのパーマリンク")

  * /currencies/{currency}




例）https://api.zaif.jp/api/1/currencies/btc

#### パラメータ[](#id9 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id10 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
name | 通貨の名前 | str  
is_token | token種別 | boolean  
  
currencyにallを指定した場合、有効な全ての通貨情報を取得します。
    
    
    [
        {
            "name": "btc",
            "is_token": false
        },
        {
            "name": "XCP",
            "is_token": true
        },
        ...
    ]
    

currencyにbtc等、有効な通貨情報を指定した場合、その情報のみを取得します。
    
    
    [
        {
            "name": "btc",
            "is_token": false
        }
    ]
    

#### 補足[](#id11 "この見出しへのパーマリンク")

  * token種別

tokenの場合、true。




* * *

### 通貨ペア情報の取得[](#id12 "この見出しへのパーマリンク")

通貨ペア情報を取得します。

#### リクエスト方法[](#id13 "この見出しへのパーマリンク")

  * /currency_pairs/{currency_pair}




例）https://api.zaif.jp/api/1/currency_pairs/btc_jpy

#### パラメータ[](#id14 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id15 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
name | 通貨ペアの名前 | str  
title | 通貨ペアのタイトル | str  
currency_pair | 通貨ペアのシステム文字列 | str  
description | 通貨ペアの詳細 | str  
is_token | token種別 | boolean  
event_number | イベントトークンの場合、0以外 | int  
seq | 通貨シークエンス | int  
item_unit_min | 基軸通貨最小値 | float  
item_unit_step | 基軸通貨最小単位 | float  
item_japanese | 基軸通貨日本語表記 | str  
aux_unit_min | 決済通貨最小値 | float  
aux_unit_step | 決済通貨最小単位 | float  
aux_unit_point | 決済通貨小数点桁数 | int  
aux_japanese | 決済通貨日本語表記 | str  
  
currency_pairにallを指定した場合、有効な全ての通貨ペア情報を取得します。
    
    
    [
        {
            "name": "BTC/JPY",
            "title": "BTC/JPY",
            "currency_pair": "btc_jpy",
            "description": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3\u30fb\u65e5\u672c\u5186\u306e\u53d6\u5f15\u3092\u884c\u3046\u3053\u3068\u304c\u3067\u304d\u307e\u3059",
            "is_token": false,
            "event_number": 0,
            "item_unit_min": 0.0001,
            "item_unit_step": 0.0001,
            "aux_unit_min": 5.0,
            "aux_unit_step": 5.0,
            "seq": 0,
            "aux_japanese": "\u65e5\u672c\u5186",
            "item_japanese": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3",
            "aux_unit_point": 0,
        },
        {
            "name": "KINOKOUSAKA/JPY",
            "title": "KINOKOUSAKA/JPY \u53d6\u5f15\u6240 - ZAIF Exchange",
            "currency_pair": "kinokousaka_jpy",
            "description": "KINOKOUSAKA/JPY \u53d6\u5f15\u6240\u3002KINOKOUSAKA\u3068\u65e5\u672c\u5186\u306e\u53d6\u5f15\u304c\u884c\u3048\u307e\u3059\u3002",
            "is_token": true,
            "event_number": 1,
            "item_unit_min": 0.01,
            "item_unit_step": 0.01,
            "aux_unit_min": 0.01,
            "aux_unit_step": 0.01,
            "seq": 134,
            "aux_japanese": "\u65e5\u672c\u5186",
            "item_japanese": "KINOKOUSAKA",
            "aux_unit_point": 2,
        }
        ...
    ]
    

currency_pairにbtc_jpy等、有効な通貨ペア情報を指定した場合、その情報のみを取得します。
    
    
    [
        {
            "name": "BTC/JPY",
            "title": "BTC/JPY",
            "currency_pair": "btc_jpy",
            "description": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3\u30fb\u65e5\u672c\u5186\u306e\u53d6\u5f15\u3092\u884c\u3046\u3053\u3068\u304c\u3067\u304d\u307e\u3059",
            "is_token": false,
            "event_number": 0,
            "item_unit_min": 0.0001,
            "item_unit_step": 0.0001,
            "aux_unit_min": 5.0,
            "aux_unit_step": 5.0,
            "seq": 0,
            "aux_japanese": "\u65e5\u672c\u5186",
            "item_japanese": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3",
            "aux_unit_point": 0,
        }
    ]
    

#### 補足[](#id16 "この見出しへのパーマリンク")

  * token種別

tokenの場合、true。




* * *

### 現在の終値を取得[](#id17 "この見出しへのパーマリンク")

現在の終値を取得します。

#### リクエスト方法[](#id18 "この見出しへのパーマリンク")

  * /last_price/{currency_pair}




例）https://api.zaif.jp/api/1/last_price/btc_jpy

注釈

currency_pairに指定できる値は [通貨ペア情報の取得](#id12) を参照してください。

#### パラメータ[](#id19 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id20 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
last_price | 現在の終値 | float  
      
    
    {
        "last_price": 134820.0
    }
    

#### エラーメッセージ[](#id21 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
unsupported currency_pair | サポートされていない通貨ペアです。  
currency_pair missing | リクエストされた通貨ペアが不適切です。  
  
* * *

### ティッカーの取得[](#id22 "この見出しへのパーマリンク")

ティッカーを取得します。

#### リクエスト方法[](#id23 "この見出しへのパーマリンク")

  * /ticker/{currency_pair}




例）https://api.zaif.jp/api/1/ticker/btc_jpy

注釈

currency_pairに指定できる値は [通貨ペア情報の取得](#id12) を参照してください。

#### パラメータ[](#id24 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id25 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
last | 終値 | float  
high | 過去24時間の高値 | float  
low | 過去24時間の安値 | float  
vwap | 過去24時間の加重平均 | float  
volume | 過去24時間の出来高 | float  
bid | 買気配値 | float  
ask | 売気配値 | float  
      
    
    {
        "last": 135875.0,
        "high": 136000.0,
        "low": 131570.0,
        "vwap": 133301.7489,
        "volume": 6889.215,
        "bid": 135875.0,
        "ask": 135920.0
    }
    

#### エラーメッセージ[](#id26 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
unsupported currency_pair | サポートされていない通貨ペアです。  
currency_pair missing | リクエストされた通貨ペアが不適切です。  
  
#### 補足[](#id27 "この見出しへのパーマリンク")

  * vwap算出方法

個々の取引価格*個々の取引量 → A

Aの過去24時間分を合算 → B

過去24時間分の個々の取引量を合算 → C

B/C → vwap




* * *

### 全ユーザー取引履歴の取得[](#id28 "この見出しへのパーマリンク")

全ユーザの取引履歴を取得します。  
取得できる取引履歴は最新のものから最大150件となります。  


#### リクエスト方法[](#id29 "この見出しへのパーマリンク")

  * /trades/{currency_pair}




例）https://api.zaif.jp/api/1/trades/btc_jpy

注釈

currency_pairに指定できる値は [通貨ペア情報の取得](#id12) を参照してください。

#### パラメータ[](#id30 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id31 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
date | 取引日時 | UNIX_TIMESTAMP  
price | 取引価格 | float  
amount | 取引量 | float  
tid | 取引ID | int  
currency_pair | 通貨ペア | str  
trade_type | 取引種別 | str  
      
    
    [
        {
            "date": 1491756592,
            "price": 135340.0,
            "amount": 0.02,
            "tid": 43054307,
            "currency_pair": "btc_jpy",
            "trade_type": "ask"
        },
        {
            "date": 1491756591,
            "price": 135345.0,
            "amount": 0.01,
            "tid": 43054306,
            "currency_pair": "btc_jpy",
            "trade_type": "bid"
        },
        ...
    ]
    

#### エラーメッセージ[](#id32 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
unsupported currency_pair | サポートされていない通貨ペアです。  
currency_pair missing | リクエストされた通貨ペアが不適切です。  
  
#### 補足[](#id33 "この見出しへのパーマリンク")

  * 取引種別

bid：買い ask：売り




* * *

### 板情報の取得[](#id34 "この見出しへのパーマリンク")

板情報を取得します。  
売り情報は価格の昇順、買い情報は価格の降順でソートされた状態で返却されます。  
情報数は最大150件となります。  


#### リクエスト方法[](#id35 "この見出しへのパーマリンク")

  * /depth/{currency_pair}




例）https://api.zaif.jp/api/1/depth/btc_jpy

注釈

currency_pairに指定できる値は [通貨ペア情報の取得](#id12) を参照してください。

#### パラメータ[](#id36 "この見出しへのパーマリンク")

  * なし




#### 戻り値[](#id37 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
asks | 売り板情報 | list  
bids | 買い板情報 | list  
      
    
    {
        "asks": [
            [
                134875.0,
                0.0063
            ],
            [
                134885.0,
                0.1639
            ],
            ...
        ],
        "bids": [
            [
                134870.0,
                0.01
            ],
            [
                134865.0,
                0.3066
            ],
            ...
        ]
    }
    

#### エラーメッセージ[](#id38 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
unsupported currency_pair | サポートされていない通貨ペアです。  
currency_pair missing | リクエストされた通貨ペアが不適切です。  
  
#### 補足[](#id39 "この見出しへのパーマリンク")

  * 売り(買い)板情報

配列の最初が価格、最後が量。




* * *

### VASP情報の取得（ 2022年4月1日より取得可能 ）[](#vasp-202241 "この見出しへのパーマリンク")

VASP情報を取得します。  
取得したIDを現物取引API withdraw (出金申請)の「VASP情報ID」に指定します。  
全てのレコードを取得する場合は、「vasp_master_id」に「all」を指定します。  
個別のIDに対応するレコードのみを取得する場合は、「vasp_master_id」に個別のIDを指定します。  
指定されたvasp_master_idに該当するIDが存在しなかった場合や、正しくないフォーマットの文字列が指定された場合は  
空のリストを返却します。  


#### リクエスト方法[](#id40 "この見出しへのパーマリンク")

  * /vasp_info/{vasp_master_id}




例）  
全件を取得する場合  
https://api.zaif.jp/api/1/vasp_info/all

個別のID毎で取得する場合  
https://api.zaif.jp/api/1/vasp_info/12

#### パラメータ[](#id41 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
vasp_master_id | Yes | VASP情報ID | str (all または個別のID) |   
  
#### 戻り値[](#id42 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
id | VASP情報ID | list  
name | VASP名 | list  
  
vasp_master_id 「all」の場合  

    
    
    [
        [
            2,
            {
                "id": 2,
                "name": "タロウ証券"
            }
        ],
        [
            3,
            {
                "id": 3,
                "name": "Coinhanako"
            }
        ],
    ・・・
        [
            1,
            {
                "id": 1,
                "name": "その他"
            }
        ]
    ]
    

vasp_master_id 「23」（個別のID）の場合  

    
    
    [
        {
            "id": 23,
            "name": "OKTaro"
        }
    ]
    

* * *

### 送金先国情報取得（ 2022年10月27日より取得可能 ）[](#id43 "この見出しへのパーマリンク")

送金先として有効な国コードと国名を一覧で取得します。  
取得した国コードをwithdraw (出金申請)の「beneficiary_country_id」に指定します。  
全ての国コードを取得する場合は、「code」に「all」を指定します。  
個別の国コードに対応するレコードのみを取得する場合は、「code」に個別の国コードを指定します。  
指定された国コードが存在しなかった場合や、正しくないフォーマットの文字列が指定された場合は  
空のリストを返却します。  


#### リクエスト方法[](#id44 "この見出しへのパーマリンク")

  * /country_info/{code}




例）  
全件を取得する場合  
https://api.zaif.jp/api/1/country_info/all

個別の国コードで取得する場合  
https://api.zaif.jp/api/1/country_info/JP

#### パラメータ[](#id45 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
code | Yes | 国コード | str (all または個別のID) |   
  
#### 戻り値[](#id46 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
code | 国コード | list  
name | 国名 | list  
  
code 「all」の場合  

    
    
    [
        {
            "code": "AF",
            "name": "Afghanistan"
        },
        {
            "code": "AX",
            "name": "\u00c5land Islands"
        },
        ・・・
        {
            "code": "ZW",
            "name": "Zimbabwe"
        }
    ]
    

code 「US」（個別の国コード）の場合  

    
    
    [
        {
            "code": "US",
            "name": "United States"
        }
    ]
    

* * *

### 法人種別情報取得（ 2022年10月27日より取得可能 ）[](#id47 "この見出しへのパーマリンク")

法人種別として有効なIDと法人種別の名称を一覧で取得します。  
取得したIDをwithdraw (出金申請)の「corp_type_id」に指定します。  
全ての法人種別を取得する場合は、「id」に「all」を指定します。  
個別の法人種別に対応するレコードのみを取得する場合は、「id」に個別のIDを指定します。  
指定されたIDに相当する法人種別が存在しなかった場合や、正しくないフォーマットの文字列が指定された場合は  
空のリストを返却します。  


#### リクエスト方法[](#id48 "この見出しへのパーマリンク")

  * /corp_type_id_info/{id}




例）  
全件を取得する場合  
https://api.zaif.jp/api/1/corp_type_id_info/all

個別の法人種別を取得する場合  
https://api.zaif.jp/api/1/corp_type_id_info/2

#### パラメータ[](#id49 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
id | Yes | 法人種別のID | str (all または個別のID) |   
  
#### 戻り値[](#id50 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
id | 法人種別のID | list  
name | 名称 | list  
  
id 「all」の場合  

    
    
    [
        [
        2,
            {
                "id": 2,
                "name": "株式会社"
            }
       ],
       [
       3,
            {
                "id": 3,
                "name": "有限会社"
            }
        ],
        ・・・
     ]
    

id 「2」（個別のID）の場合  

    
    
    [
        {
            "id": 2,
            "name": "株式会社"
        }
    ]
    

[ Previous](index.html "Zaif-API Documents") [Next ](TradingAPI.html "現物取引API")

* * *

© Copyright Ｚａｉｆ Ｉｎｃ．.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 


---

# Source: https://zaif-api-document.readthedocs.io/ja/latest/TradeAPI.html

ERROR: Failed to fetch: 404 Client Error: Not Found for url: https://zaif-api-document.readthedocs.io/ja/latest/TradeAPI.html


---

# Source: https://zaif-api-document.readthedocs.io/ja/latest/MarginTradingAPI.html

[ Zaif API document ](index.html)

v2.1.0 

  * [現物公開API](PublicAPI.html)
  * [現物取引API](TradingAPI.html)
  * [信用取引 API](#)
    * [共通情報](#id1)
      * [事前準備](#id2)
      * [リクエスト方法](#id3)
      * [認証](#id4)
      * [パラメータ](#id5)
      * [戻り値](#id6)
      * [エラーメッセージ](#id7)
      * [補足](#id8)
    * [個別情報](#id9)
      * [ユーザー自身の取引履歴を取得](#id10)
        * [パラメータ](#id11)
        * [戻り値](#id12)
        * [補足](#id13)
      * [ユーザー自身の取引履歴明細を取得](#id14)
        * [パラメータ](#id15)
        * [戻り値](#id16)
        * [エラーメッセージ](#id17)
        * [補足](#id18)
      * [未約定注文一覧の取得](#id19)
        * [パラメータ](#id20)
        * [戻り値](#id21)
        * [補足](#id22)
      * [注文](#id23)
        * [パラメータ](#id24)
        * [戻り値](#id25)
        * [エラーメッセージ](#id26)
        * [補足](#id27)
      * [注文の変更](#id28)
        * [パラメータ](#id29)
        * [戻り値](#id30)
        * [エラーメッセージ](#id31)
        * [補足](#id32)
      * [注文の取消し](#id33)
        * [パラメータ](#id34)
        * [戻り値](#id35)
        * [エラーメッセージ](#id36)
        * [補足](#id37)
  * [WebSocket API](WebSocket_API.html)
  * [OAuth API](OAuthAPI.html)
  * [決済 API](PaymentAPI.html)
  * [Q&A](Q%26A.html)
  * [その他](Others.html)



__[Zaif API document](index.html)

  * [](index.html)
  * 信用取引 API
  * [ View page source](_sources/MarginTradingAPI.md.txt)



* * *

# 信用取引 API[](#api "この見出しへのパーマリンク")

  * [共通情報](#id1)

    * [事前準備](#id2)

    * [リクエスト方法](#id3)

    * [認証](#id4)

    * [パラメータ](#id5)

    * [戻り値](#id6)

    * [エラーメッセージ](#id7)

    * [補足](#id8)

  * [個別情報](#id9)

    * [ユーザー自身の取引履歴を取得](#id10)

    * [ユーザー自身の取引履歴明細を取得](#id14)

    * [未約定入門一覧の取得](#id19)

    * [注文](#id23)

    * [注文の変更](#id28)

    * [注文の取消し](#id33)




* * *

## 共通情報[](#id1 "この見出しへのパーマリンク")

信用取引APIの共通情報です。

* * *

### 事前準備[](#id2 "この見出しへのパーマリンク")

  * 信用取引APIを利用するには、[アカウント情報](https://zaif.jp/api_keys) のページからAPI Keyの発行をおこなってください。




### リクエスト方法[](#id3 "この見出しへのパーマリンク")

  * エンドポイント：https://api.zaif.jp/tlapi

  * メソッド：POST




### 認証[](#id4 "この見出しへのパーマリンク")

  * 取得したAPI Keysを利用して、下記のようにHTTPヘッダを設定し、認証情報を送信します。


キー | 詳細 | 例  
---|---|---  
key | APIキー | 490f983a-5fab-49b2-b789-9d1f130874d3  
sign | 署名 | 詳細は下記  
  
注釈

signはPOSTする全てのパラメータ（nonceとmethodおよびメソッド毎のパラメータ）を URLエンコードしたクエリ形式(param1=val1&param2=val2)のメッセージとして、Secret Keyを用いてHMAC-SHA512で署名します。

### パラメータ[](#id5 "この見出しへのパーマリンク")

キー | 詳細 | 例  
---|---|---  
nonce | 1以上の数 | 23123  
method | APIメソッド名 | get_info  
type | 取引タイプ | margin  
  
注釈

メソッド毎の固有のパラメータも全てPOSTパラメータにて送信してください。 nonceパラメータの値は実効毎に増分されていないとエラーが発生します。また、増分量は少数点以下の値にも対応しております。

### 戻り値[](#id6 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
success | 成功フラグ | int  
return | 実行結果 | dict or string  
      
    
    {
        "success": 1,
        "return": {
            ...
        }
    }
    

### エラーメッセージ[](#id7 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
method not found | 指定されたメソッドが存在しません。  
no data found for the key | APIキーが無効です。  
time wait restriction, please try later. | 同じメソッドが短時間に多く呼び出しされたときに発生します。しばらく待ってから、再度お試しください。  
signature mismatch | 署名が不適切です。  
invalid access token | 無効なトークンが指定されています。  
expired access token | トークンの有効期限が切れています。トークン再発行APIを参考にし、トークンの再発行をしてください。  
nonce not incremented | 前回API実行時よりnonce値が加算されていません。  
nonce out of range | 値が最大値を超えています。新しいAPIキーを発行してください。  
api key don’t have {} permission | API Keyに権限がありません。  
invalid {} parameter | 指定されているパラメータが無効です。  
invalid type | 取引タイプが不正です。  
  
### 補足[](#id8 "この見出しへのパーマリンク")

  * 戻り値

処理に成功した場合、successには1が、returnには実行結果が設定されます。

処理に失敗した場合、successには0が、returnにはエラーメッセージが設定されます。



  * ※ 呼び出しの回数制限を解除するためには、当社の定めた条件(一定基準以上の取引高など)に基づく審査が必要になります。




* * *

## 個別情報[](#id9 "この見出しへのパーマリンク")

信用取引APIの個別情報です。

* * *

### ユーザー自身の取引履歴を取得[](#id10 "この見出しへのパーマリンク")

信用取引のユーザー自身の取引履歴を取得します。

#### パラメータ[](#id11 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | get_positions | str |   
group_id | No | グループID | int |   
from | No | この順番のレコードから取得 | int | 0  
count | No | 取得するレコード数 | int | 1000  
from_id | No | このトランザクションIDのレコードから取得 | int | 0  
end_id | No | このトランザクションIDのレコードまで取得 | int | infinity  
order | No | ソート順 | str (ASC or DESC) | DESC  
since | No | 開始タイムスタンプ | UNIX_TIMESTAMP | 0  
end | No | 終了タイムスタンプ | UNIX_TIMESTAMP | infinity  
currency_pair | No | 通貨ペア。指定なしで全通貨ペア | str (例) btc_jpy | 全通貨ペア  
  
#### 戻り値[](#id12 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
例）182 | 注文ID | int  
group_id | グループID | int  
currency_pair | 通貨ペア | str  
action | bid(買い) or ask(売り) | str  
amount | 数量 | float  
price | 価格 | float  
limit | リミット注文価格 | float  
stop | ストップ注文価格 | float  
timestamp | 発注日時 | UNIX_TIMESTAMP  
term_end | 注文の有効期限 | UNIX_TIMESTAMP  
leverage | レバレッジ | float  
fee_spent | 支払い手数料 | float  
timestamp_closed | クローズ日時 | UNIX_TIMESTAMP  
price_avg | 建玉平均価格 | float  
amount_done | 建玉数 | float  
close_avg | 決済平均価格 | float  
close_done | 決済数 | float  
deposit_xxx | 実際にデポジットした額(xxxは通貨コード） | float  
deposit_price_xxx | デポジット時計算レート(xxxは通貨コード） | float  
refunded_xxx | 実際に返却した額(xxxは通貨コード） | float  
refunded_price_xxx | 実際に返却した額(xxxは通貨コード） | float  
guard_fee | 追証ガード手数料 | float  
      
    
    {
        "success": 1,
        "return": {
            "182": {
                "group_id": 1,
                "currency_pair": "btc_jpy",
                "action": "bid",
                "leverage": 2.5,
                "price": 110005,
                "limit": 130000,
                "stop": 90000,
                "amount": 0.03,
                "fee_spent": 0,
                "timestamp": 1402018713,
                "term_end": 1404610713,
                "timestamp_closed": 1402019000,
                "deposit": 35.76 ,
                "deposit_jpy": 35.76,
                "refunded": 35.76 ,
                "refunded_jpy": 35.76,
                "swap": 0,
            }
        }
    }
    

#### 補足[](#id13 "この見出しへのパーマリンク")

  * 呼び出しは60秒間に10回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)

  * “since”もしくは”end”をセットした場合、”order”は強制的に”ASC”となります。

  * “from_id”もしくは”end_id”をセットした場合、”order”は強制的に”ASC”となります。




* * *

### ユーザー自身の取引履歴明細を取得[](#id14 "この見出しへのパーマリンク")

信用取引のユーザー自身の取引履歴の明細を取得します。

#### パラメータ[](#id15 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | position_history | str |   
group_id | No | グループID | int |   
leverage_id | Yes | 注文ID | int |   
  
#### 戻り値[](#id16 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
例）182 | 注文ID | int  
group_id | グループID | int  
currency_pair | 通貨ペア | str  
action | bid(買い) or ask(売り) | str  
amount | 数量 | float  
price | 価格 | float  
timestamp | 発注日時 | UNIX_TIMESTAMP  
your_action | bid(買い) or ask(売り)、自己取引の場合はboth | str  
bid_leverage_id | 買い注文ID(自分の注文の場合のみ) | int  
ask_leverage_id | 売り注文ID(自分の注文の場合のみ) | int  
      
    
    {
        "success": 1,
        "return": {
            "182": {
                "group_id": 1,
                "currency_pair": "btc_jpy",
                "action": "bid",
                "amount": 0.0001,
                "price": 499000
                "timestamp": 1504251232
                "your_action": "bid",
                "bid_leverage_id": 182,
            },
            "183": {
                "group_id": 1,
                "currency_pair": "btc_jpy",
                "action": "ask",
                "amount": 0.0001,
                "price": 450000
                "timestamp": 1504251267
                "your_action": "ask",
                "ask_leverage_id": 182,
            },
    
        }
    }
    

#### エラーメッセージ[](#id17 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
order not found | 注文が見つかりません。  
  
#### 補足[](#id18 "この見出しへのパーマリンク")

  * 呼び出しは60秒間に10回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)

  * leverage_idは[ユーザー自身の取引履歴](#id10)または[未約定注文一覧](#id19)で取得できます。




* * *

### 未約定注文一覧の取得[](#id19 "この見出しへのパーマリンク")

信用取引の現在有効な注文一覧を取得します（未約定注文一覧）。

#### パラメータ[](#id20 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | active_positions | str |   
group_id | No | グループID | int |   
currency_pair | No | 通貨ペア。指定なしで全通貨ペア | str(例) btc_jpy | 全通貨ペア  
  
#### 戻り値[](#id21 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
例）182 | 注文ID | int  
group_id | グループID | int  
currency_pair | 通貨ペア | str  
action | bid(買い) or ask(売り) | str  
amount | 数量 | float  
price | 価格 | float  
limit | リミット注文価格 | float  
stop | ストップ注文価格 | float  
timestamp | 発注日時 | UNIX_TIMESTAMP  
term_end | 注文の有効期限 | UNIX_TIMESTAMP  
leverage | レバレッジ | float  
fee_spent | 支払い手数料 | float  
price_avg | 建玉平均価格 | float  
amount_done | 建玉数 | float  
close_avg | 決済平均価格 | float  
close_done | 決済数 | float  
deposit_xxx | 実際にデポジットした額(xxxは通貨コード） | float  
deposit_price_xxx | デポジット時計算レート(xxxは通貨コード） | float  
      
    
    {
        "success": 1,
        "return": {
            "184": {
                "group_id": "1",
                "currency_pair": "btc_jpy",
                "action": "ask",
                "amount": 0.0001,
                "price": 450000,
                "timestamp": 1402021125,
                "term_end": 1404613125,
                "leverage": 1,
                "fee_spent": 0.0015,
                "price_avg": 450000,
                "amount_done": 0.0001,
                "deposit_jpy": 48.72
            }
        }
    }
    

#### 補足[](#id22 "この見出しへのパーマリンク")

  * 呼び出しは10秒間に20回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)




* * *

### 注文[](#id23 "この見出しへのパーマリンク")

信用取引の注文を行います。

#### パラメータ[](#id24 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | create_position | str |   
group_id | No | グループID | int |   
currency_pair | Yes | 通貨ペア | str(例) btc_jpy |   
action | Yes | bid(買い) or ask(売り) | str |   
amount | Yes | 数量 | numerical |   
price | Yes | 価格 | numerical |   
leverage | Yes | レバレッジ | numerical |   
limit | No | リミット注文価格 | numerical |   
stop | No | ストップ注文価格 | numerical |   
  
#### 戻り値[](#id25 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
leverage_id | 注文ID | int  
timestamp | 注文日時 | UNIX_TIMESTAMP  
term_end | 注文の有効期限 | UNIX_TIMESTAMP  
price_avg | 建玉平均価格 | float  
amount_done | 建玉数 | float  
deposit_xxx | 実際にデポジットした額(xxxは通貨コード） | float  
deposit_price_xxx | デポジット時計算レート(xxxは通貨コード） | float  
funds | 残高 | dict  
      
    
    {
        "success": 1,
        "return": {
            "leverage_id": 22258,
            "timestamp": 1504253833,
            "term_end": 1506845833,
            "price_avg": 118000,
            "amount_done": 0.0001,
            "deposit_jpy": 11.92,
            "funds": {
                "jpy": 325,
                "btc": 1.392,
                "mona": 2600
            }
        }
    }
    

#### エラーメッセージ[](#id26 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
trade temporarily unavailable | 取引が一時的に停止されています。  
your account is restricted now, KYC required. | 本人確認が完了していないため、取引ができません。本人確認を完了させて下さい。  
insufficient funds | 取引に必要な残高が存在しません。  
  
#### 補足[](#id27 "この見出しへのパーマリンク")

  * 呼び出しは10秒間に3回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)

  * パラメータ limitについて

リミット値（利確のための反対売買の指値）を指定することができます。 リミット値を指定した場合、注文が成立した分だけの数量について、自動的にリミット注文が発行されます。

  * パラメータ stopについて

ストップ値を指定した場合、設定価格まで下落（あるいは上昇）した場合に成行にて決済を試みます。 成行注文のため必ずしも設定価格で決済されることを保証する物ではございません。

  * 価格および数量の数値について

下記の単位以外で注文しようとした場合、invalid price parameterまたはinvalid amount parameterというエラーが返されます。

    * 価格（priceおよびlimit）

btc_jpy : 5円単位

    * 数量（amount）

btc_jpy : 0.0001BTC単位




* * *

### 注文の変更[](#id28 "この見出しへのパーマリンク")

信用取引の注文の変更を行います。

#### パラメータ[](#id29 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | change_position | str |   
group_id | No | グループID | int |   
leverage_id | Yes | 注文ID | int |   
price | Yes | 価格 | numerical |   
limit | No | リミット注文価格 | numerical |   
stop | No | ストップ注文価格 | numerical |   
  
#### 戻り値[](#id30 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
leverage_id | 注文ID | int  
timestamp_closed | クローズ日時 | UNIX_TIMESTAMP  
price_avg | 建玉平均価格 | float  
amount_done | 建玉数 | float  
close_avg | 決済平均価格 | float  
close_done | 決済数 | float  
refunded_xxx | 実際に返却した額(xxxは通貨コード） | float  
refunded_price_xxx | 実際に返却した額(xxxは通貨コード） | float  
guard_fee | 追証ガード手数料 | float  
      
    
    {
        "success": 1,
        "return": {
            "leverage_id": 22258,
            "price_avg": 118000,
            "amount_done": 0.0001,
        }
    }
    

#### エラーメッセージ[](#id31 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
order not found | 注文が見つかりません。  
order already closed | 注文が既にクローズしています。  
trade temporarily unavailable | 取引が一時的に停止されています。  
  
#### 補足[](#id32 "この見出しへのパーマリンク")

  * 呼び出しは10秒間に3回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)

  * パラメータ limitについて

limitを指定しなかった場合、設定済みのリミット注文は取り消されます。 継続してリミット注文を出し続けたい場合は毎回セットしてください。 リミット値を指定した場合、注文が成立した分だけの数量について、自動的にリミット注文が発行されます。

  * パラメータ stopについて

stopを指定しなかった場合、設定済みのストップ注文は取り消されます。 継続してストップ注文を出し続けたい場合は毎回必ずセットしてください。 ストップ値を指定した場合、設定価格まで下落（あるいは上昇）した場合に成行にて決済を試みます。 成行注文のため必ずしも設定価格で決済されることを保証する物ではございません。

  * 価格および数量の数値について

下記の単位以外で注文しようとした場合、invalid price parameterまたはinvalid amount parameterというエラーが返されます。

    * 価格（priceおよびlimit）

btc_jpy : 5円単位

    * 数量（amount）

btc_jpy : 0.0001BTC単位

  * leverage_idは[ユーザー自身の取引履歴](#id10)または[未約定注文一覧](#id19)で取得できます。




* * *

### 注文の取消し[](#id33 "この見出しへのパーマリンク")

信用取引の注文の取消しを行います。

#### パラメータ[](#id34 "この見出しへのパーマリンク")

パラメータ | 必須 | 詳細 | 型 | デフォルト  
---|---|---|---|---  
method | Yes | cancel_position | str |   
group_id | No | グループID | int |   
leverage_id | Yes | 注文ID | int |   
  
#### 戻り値[](#id35 "この見出しへのパーマリンク")

キー | 詳細 | 型  
---|---|---  
leverage_id | 注文ID | int  
fee_spent | 支払い手数料 | float  
timestamp_closed | クローズ日時 | UNIX_TIMESTAMP  
price_avg | 建玉平均価格 | float  
amount_done | 建玉数 | float  
close_avg | 決済平均価格 | float  
close_done | 決済数 | float  
refunded_xxx | 実際に返却した額(xxxは通貨コード） | float  
refunded_price_xxx | 実際に返却した額(xxxは通貨コード） | float  
guard_fee | 追証ガード手数料 | float  
funds | 残高 | dict  
      
    
    {
        'success': 1,
        'return': {
            'leverage_id': 2072,
            'refunded_jpy': 645.96,
            'funds': {
                'btc': 0.496,
                'jpy': 1564.96,
                'xem': 0.0,
                'mona': 10.0
            },
            'fee_spent': 0.0,
            'timestamp_closed': '1508384951',
            'swap': 0.0
        }
    }
    

#### エラーメッセージ[](#id36 "この見出しへのパーマリンク")

メッセージ | 詳細  
---|---  
order not found | 注文が見つかりません。  
order already closed | 注文が既にクローズしています。  
order is too new | 注文から一定時間の経過が必要です。  
  
#### 補足[](#id37 "この見出しへのパーマリンク")

  * 呼び出しは10秒間に3回以下におさまるようにしてください。呼び出しが多すぎるとアクセス拒否されることがあります。[（※）](#margin-notice-1)

  * leverage_idは[ユーザー自身の取引履歴](#id10)または[未約定注文一覧](#id19)で取得できます。




[ Previous](TradingAPI.html "現物取引API") [Next ](WebSocket_API.html "WebSocket API")

* * *

© Copyright Ｚａｉｆ Ｉｎｃ．.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 
