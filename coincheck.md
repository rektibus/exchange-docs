



    if(console in window){console.log=function(){}}else{console={};console.log=function(){};console.warn=function(){}}
  
  Exchange API document | Cryptocurrency Exchange, Coincheck
  
  

  
  

  
  

  
  

    
    

    
    
    
    
    


  
  
  
    
  
  
  
  
  
  
  
  
  

  
    
  
    
  
  
  
    
    
    
  
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('set', 'dimension1', 'not_login');
  ga('create', 'UA-53448644-1', 'auto');
  ga('require', 'linkid', 'linkid.js');
  ga('send', 'pageview');



    VueFromAngularCtrlLoader.module("coin").value("current_account", null)
      .value("current_user", null)
      .value("current_iam_user", null)
      .value("currentShop", null)
      .value("minConfirmation", 3)
      .value("pageType", "consumer")
      .value("ios", false)
      .value("android", false)
      .value("socketDomain", "https://ws.coincheck.com")
      .value("env", "production")
      .value("language", "en")
      .value("matchmedia", matchmedia)
      .value("$window", window)

    VueFromAngularPureDefaultMixins.push("AppCommon");
    VueFromAngularDefaultMixins.push("AppCtrl");
    i18next.changeLanguage("en")
  

    
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KGXLHSS');




    
    !function(n){var o=window[n]=function(){var n=[].slice.call(arguments);return o.x?o.x.apply(0,n):o.q.push(n)};o.q=[],o.i=Date.now(),o.allow=function(){o.o="allow"},o.deny=function(){o.o="deny"}}("krt")
    
    
    


  

  
  
  
  
    
  

  
  
    VueFromAngularCtrlLoader.module("coin").value("fixHeader", true)
  
  
  
    
      
        
          
            
              
                
              
            
            
              
                Sign in
                Sign in
                
                  
                
                
                  Exchange
                  Lending
                
              
                
                  
                    Create account
                  
                
              
              
  Notifications
  
    
  
  
    Notifications
    
      
      {{article.title}}
      {{$filters.date(article.date, 'YYYY/MM/dd HH:mm')}}
    
    View all notifications
  
  
    Notifications
    
      
    
        
            
                
            
        
    


    
    Loading
  


              
                {{ languageName(language) }}
                
                  
                
                
                  {{ languageName(langItem) }}
                
              
            
          


          
            
              
                
              
            
            
              
                Payment
                  
                
                
                
                  Exchange
                  Lending
                  Account Transfer
                    Identity
                  Signout
                
              
              
                
                  {{$filters.fraction(current_account.balance.btc, 8)}}
                  BTC
                
                
                  {{$filters.fraction(current_account.balance.jpy, 8)}}
                  JPY
                
              
            
          

          
            
              
                
                  
                
              
              
                
                
                
                  
                    
                     Net Assets
                    ¥ {{ $filters.cut_decimal_zero($filters.number(balance.net_assets.jpy, 1)) }}
                    
                      
                    
                    
  VueFromAngularCtrlLoader.module("coin").value("currencyIcons", {"jpy":"icon_jpy_B2oayzEaxL7Gr7Tr0YnK4zj1KjB6CgrB.svg","btc":"icon_btc_CbeyPRJtFqiAlQmJLflKnnfYMRE98H0s.svg","eth":"icon_eth_Uqq7Vwh1gjvzuv8Mf1Zn6eqPRWFJc12s.svg","etc":"icon_etc_Rf40JnydLwYlChZfj3iGQbenbAoJHWNP.svg","lsk":"icon_lsk_drN6RraU8UYNiyDP8nWHicZZiShVDs6S.svg","xrp":"icon_xrp_E3gMJ4etnuGfiAGmJkdLHcuamA2HXVdK.svg","xem":"icon_xem_F5PVZDLNMitQPPT0ADeEemkwp43F0oTk.svg","ltc":"icon_ltc_eCWkHMqz5cSVBoHpPE9K6ZrwDl8QfDh4.svg","bch":"icon_bch_Xafxnl3eGvOTa3JMJajtI4JX4r9Xo7GL.svg","mona":"icon_mona_eMcvrXnLn7VWBHWDAyK7qivj8khIsrAg.svg","xlm":"icon_xlm_PXIQRZWYaA33Foena2djgSFkb645ORE8.svg","qtum":"icon_qtum_7b3c2f091d5ba37094d7ec8c8fb99338.svg","bat":"icon_bat_JwAQ4hfU94ziTrqBYgjaVDhibVDay75C.svg","iost":"icon_iost_kQK2O9rrYXpsDqTiRQVoP6ME57iDqDLH.svg","enj":"icon_enj_xMvRFoMruajwd258Xh72cBiAbHXTF1zC.svg","sand":"icon_sand_t7bjs4Tg9bycWH9OA6OMOqio3C75a6w8.svg","xym":"icon_xym_Ug2va9J6Mxl41VN7ulkFyDfzjxXHPNak.svg","dot":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","flr":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","fnct":"icon_fnct_bL7WPQrKqhrmN343yypuiJs6HnNC29vA.svg","chz":"icon_chz_wBWMOA4T45bJKEXJL8GyQ.svg","link":"icon_link_xXI5yVTHLV9TAqi8mTljQ.svg","dai":"icon_dai_IqK4jIcbT68rpblEvw6Td9NKlPm9z1Sl.svg","matic":"icon_matic_ac76bcd3-60c5-4ff8-9243-f882bbe19974.svg","ape":"icon_ape_UN7u2ZroWR3KBlLfGtnQACzeQ4nTJHjW.svg","axs":"icon_axs_JrK66dmdx2LxjnQ1p5bnsj3BeGAvCLvE.svg","imx":"icon_imx_onP5OYdXLgJqgwZqkhjMd8yOpzen4Md8.svg","wbtc":"icon_wbtc_keasc3hrhTxAOu9XIHiudFlTykJ8HTCo.svg","shib":"icon_shib_wkteoqlzit9dh1l9jhotm4tnelj5hreg.svg","avax":"icon_avax_LJPISoxW2pGYAKQJO1luAGroGY4sh2Sl.svg","bril":"icon_bril_9ae1e142-206e-42b3-be9a-f238f85393d6.svg","bc":"icon_bc_b8f4cd33-7ed1-45b8-9442-8c02d9432eb4.svg","doge":"icon_doge_f6963378-42f1-4c8e-ad6e-f0d0822733ae.svg","sol":"icon_solana_e3f2e4ee-061d-4ae9-89ae-3f1aa05b0329.svg","grt":"icon_grt_5fe3e65d-f3bd-4187-91de-9921d6b6b9f9.svg","mana":"icon_mana_3d280d4d-aa78-4f4a-b049-3bfe155d2ae6.svg","mask":"icon_mask_0afc2ba1-a410-42f5-baee-32cf9325425e.svg","pepe":"icon_pepe_75e62212-b776-47a0-812a-48f6c92161c5.svg","fpl":"icon_fpl_f50833d5-8bde-4f35-bda2-882b746d3368.svg","trx":"icon_trx_0a4157f5-d838-420d-8cae-d36268a7cf2f.svg"})


  
    
      
        Net Assets
        
          Show in header
          
            
          
        
      
    
    
      
        
          
           Net Assets
        
        
          ¥ {{ $filters.cut_decimal_zero($filters.number(balance.net_assets.jpy, 1)) }}
        
      
    

    
      
        
        Available
        In Use
      
      
        
          
            
            {{ cur.toUpperCase() }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.available[cur])) }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.in_use[cur])) }}
          
        
      
    
  
  


                  
                
                
                
                
                  
                    Exchange
                    
                  
                  
                    
                  
                  
                    Lending
                      Identity
                  
                
                
  Notifications
  
    
  
  
    Notifications
    
      
      {{article.title}}
      {{$filters.date(article.date, 'YYYY/MM/dd HH:mm')}}
    
    View all notifications
  
  
    Notifications
    
      
    
        
            
                
            
        
    


    
    Loading
  


                
                  {{ languageName(language) }}
                  
                    
                  
                  
                    {{ languageName(langItem) }}
                  
                
              
            
          

          
            
              
                
              
            
            
              
                Lending
                  
                
                
                
                  Exchange
                  Account Transfer
                    Identity
                  Signout
                
              
            
          
          
        
      
      
    
    
      
        
          
            
          
          
            
            
            
              Net Assets
              
            
            
            
            
              Exchange
                
              
              
                
              
              
              
                Lending
                  Identity
              
            
            
              
            
            
              
  VueFromAngularCtrlLoader.module("coin").value("currencyIcons", {"jpy":"icon_jpy_B2oayzEaxL7Gr7Tr0YnK4zj1KjB6CgrB.svg","btc":"icon_btc_CbeyPRJtFqiAlQmJLflKnnfYMRE98H0s.svg","eth":"icon_eth_Uqq7Vwh1gjvzuv8Mf1Zn6eqPRWFJc12s.svg","etc":"icon_etc_Rf40JnydLwYlChZfj3iGQbenbAoJHWNP.svg","lsk":"icon_lsk_drN6RraU8UYNiyDP8nWHicZZiShVDs6S.svg","xrp":"icon_xrp_E3gMJ4etnuGfiAGmJkdLHcuamA2HXVdK.svg","xem":"icon_xem_F5PVZDLNMitQPPT0ADeEemkwp43F0oTk.svg","ltc":"icon_ltc_eCWkHMqz5cSVBoHpPE9K6ZrwDl8QfDh4.svg","bch":"icon_bch_Xafxnl3eGvOTa3JMJajtI4JX4r9Xo7GL.svg","mona":"icon_mona_eMcvrXnLn7VWBHWDAyK7qivj8khIsrAg.svg","xlm":"icon_xlm_PXIQRZWYaA33Foena2djgSFkb645ORE8.svg","qtum":"icon_qtum_7b3c2f091d5ba37094d7ec8c8fb99338.svg","bat":"icon_bat_JwAQ4hfU94ziTrqBYgjaVDhibVDay75C.svg","iost":"icon_iost_kQK2O9rrYXpsDqTiRQVoP6ME57iDqDLH.svg","enj":"icon_enj_xMvRFoMruajwd258Xh72cBiAbHXTF1zC.svg","sand":"icon_sand_t7bjs4Tg9bycWH9OA6OMOqio3C75a6w8.svg","xym":"icon_xym_Ug2va9J6Mxl41VN7ulkFyDfzjxXHPNak.svg","dot":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","flr":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","fnct":"icon_fnct_bL7WPQrKqhrmN343yypuiJs6HnNC29vA.svg","chz":"icon_chz_wBWMOA4T45bJKEXJL8GyQ.svg","link":"icon_link_xXI5yVTHLV9TAqi8mTljQ.svg","dai":"icon_dai_IqK4jIcbT68rpblEvw6Td9NKlPm9z1Sl.svg","matic":"icon_matic_ac76bcd3-60c5-4ff8-9243-f882bbe19974.svg","ape":"icon_ape_UN7u2ZroWR3KBlLfGtnQACzeQ4nTJHjW.svg","axs":"icon_axs_JrK66dmdx2LxjnQ1p5bnsj3BeGAvCLvE.svg","imx":"icon_imx_onP5OYdXLgJqgwZqkhjMd8yOpzen4Md8.svg","wbtc":"icon_wbtc_keasc3hrhTxAOu9XIHiudFlTykJ8HTCo.svg","shib":"icon_shib_wkteoqlzit9dh1l9jhotm4tnelj5hreg.svg","avax":"icon_avax_LJPISoxW2pGYAKQJO1luAGroGY4sh2Sl.svg","bril":"icon_bril_9ae1e142-206e-42b3-be9a-f238f85393d6.svg","bc":"icon_bc_b8f4cd33-7ed1-45b8-9442-8c02d9432eb4.svg","doge":"icon_doge_f6963378-42f1-4c8e-ad6e-f0d0822733ae.svg","sol":"icon_solana_e3f2e4ee-061d-4ae9-89ae-3f1aa05b0329.svg","grt":"icon_grt_5fe3e65d-f3bd-4187-91de-9921d6b6b9f9.svg","mana":"icon_mana_3d280d4d-aa78-4f4a-b049-3bfe155d2ae6.svg","mask":"icon_mask_0afc2ba1-a410-42f5-baee-32cf9325425e.svg","pepe":"icon_pepe_75e62212-b776-47a0-812a-48f6c92161c5.svg","fpl":"icon_fpl_f50833d5-8bde-4f35-bda2-882b746d3368.svg","trx":"icon_trx_0a4157f5-d838-420d-8cae-d36268a7cf2f.svg"})


  
    
      
        Net Assets
        
          Show in header
          
            
          
        
      
    
    
      
        
          
           Net Assets
        
        
          ¥ {{ $filters.cut_decimal_zero($filters.number(balance.net_assets.jpy, 1)) }}
        
      
    

    
      
        
        Available
        In Use
      
      
        
          
            
            {{ cur.toUpperCase() }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.available[cur])) }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.in_use[cur])) }}
          
        
      
    
  
  


            
          
          
            
              Sign in
              
                
              
              
                Exchange
                Lending
              
            
              
                
                  
                    Create account
                  
                
              
            
              
            
            
              
  VueFromAngularCtrlLoader.module("coin").value("currencyIcons", {"jpy":"icon_jpy_B2oayzEaxL7Gr7Tr0YnK4zj1KjB6CgrB.svg","btc":"icon_btc_CbeyPRJtFqiAlQmJLflKnnfYMRE98H0s.svg","eth":"icon_eth_Uqq7Vwh1gjvzuv8Mf1Zn6eqPRWFJc12s.svg","etc":"icon_etc_Rf40JnydLwYlChZfj3iGQbenbAoJHWNP.svg","lsk":"icon_lsk_drN6RraU8UYNiyDP8nWHicZZiShVDs6S.svg","xrp":"icon_xrp_E3gMJ4etnuGfiAGmJkdLHcuamA2HXVdK.svg","xem":"icon_xem_F5PVZDLNMitQPPT0ADeEemkwp43F0oTk.svg","ltc":"icon_ltc_eCWkHMqz5cSVBoHpPE9K6ZrwDl8QfDh4.svg","bch":"icon_bch_Xafxnl3eGvOTa3JMJajtI4JX4r9Xo7GL.svg","mona":"icon_mona_eMcvrXnLn7VWBHWDAyK7qivj8khIsrAg.svg","xlm":"icon_xlm_PXIQRZWYaA33Foena2djgSFkb645ORE8.svg","qtum":"icon_qtum_7b3c2f091d5ba37094d7ec8c8fb99338.svg","bat":"icon_bat_JwAQ4hfU94ziTrqBYgjaVDhibVDay75C.svg","iost":"icon_iost_kQK2O9rrYXpsDqTiRQVoP6ME57iDqDLH.svg","enj":"icon_enj_xMvRFoMruajwd258Xh72cBiAbHXTF1zC.svg","sand":"icon_sand_t7bjs4Tg9bycWH9OA6OMOqio3C75a6w8.svg","xym":"icon_xym_Ug2va9J6Mxl41VN7ulkFyDfzjxXHPNak.svg","dot":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","flr":"icon_dot_dXEDle69Z6P5Z040UF0rZHXYwwo3UHcS.svg","fnct":"icon_fnct_bL7WPQrKqhrmN343yypuiJs6HnNC29vA.svg","chz":"icon_chz_wBWMOA4T45bJKEXJL8GyQ.svg","link":"icon_link_xXI5yVTHLV9TAqi8mTljQ.svg","dai":"icon_dai_IqK4jIcbT68rpblEvw6Td9NKlPm9z1Sl.svg","matic":"icon_matic_ac76bcd3-60c5-4ff8-9243-f882bbe19974.svg","ape":"icon_ape_UN7u2ZroWR3KBlLfGtnQACzeQ4nTJHjW.svg","axs":"icon_axs_JrK66dmdx2LxjnQ1p5bnsj3BeGAvCLvE.svg","imx":"icon_imx_onP5OYdXLgJqgwZqkhjMd8yOpzen4Md8.svg","wbtc":"icon_wbtc_keasc3hrhTxAOu9XIHiudFlTykJ8HTCo.svg","shib":"icon_shib_wkteoqlzit9dh1l9jhotm4tnelj5hreg.svg","avax":"icon_avax_LJPISoxW2pGYAKQJO1luAGroGY4sh2Sl.svg","bril":"icon_bril_9ae1e142-206e-42b3-be9a-f238f85393d6.svg","bc":"icon_bc_b8f4cd33-7ed1-45b8-9442-8c02d9432eb4.svg","doge":"icon_doge_f6963378-42f1-4c8e-ad6e-f0d0822733ae.svg","sol":"icon_solana_e3f2e4ee-061d-4ae9-89ae-3f1aa05b0329.svg","grt":"icon_grt_5fe3e65d-f3bd-4187-91de-9921d6b6b9f9.svg","mana":"icon_mana_3d280d4d-aa78-4f4a-b049-3bfe155d2ae6.svg","mask":"icon_mask_0afc2ba1-a410-42f5-baee-32cf9325425e.svg","pepe":"icon_pepe_75e62212-b776-47a0-812a-48f6c92161c5.svg","fpl":"icon_fpl_f50833d5-8bde-4f35-bda2-882b746d3368.svg","trx":"icon_trx_0a4157f5-d838-420d-8cae-d36268a7cf2f.svg"})


  
    
      
        Net Assets
        
          Show in header
          
            
          
        
      
    
    
      
        
          
           Net Assets
        
        
          ¥ {{ $filters.cut_decimal_zero($filters.number(balance.net_assets.jpy, 1)) }}
        
      
    

    
      
        
        Available
        In Use
      
      
        
          
            
            {{ cur.toUpperCase() }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.available[cur])) }}
            ¥ {{ $filters.cut_decimal_zero($filters.number(balance.coincheck.in_use[cur])) }}
          
        
      
    
  
  


            
          
        
        
          
            
              
            
          
        
        
          
            
              
            
          
        
        
          
        
        
          
        
      
      
    

    
      
      
        
          
            

	
	


Payment
            
              Account ID {{current_account.id}}
              

	
	


Exchange
              

	
	


Lending
              Account Transfer
            
            


Home
            


Sell Product
            



Sales History
            

	
	
	


Withdraw Yen
            


Shop Info
            


Sell on Tablet
            



Settings
            




Contact
          
        
        
          
            

	
	


Lending
            
              Account ID {{current_account.id}}
              

	
	


Exchange
              Account Transfer
            
            


Home
            


Lending
            





Send Coin
            








Receive Coin
            



Settings
          
        
      
    
  
  
  


  
    
      
        Overview
        Authentication
        Libraries
        Pagination
        
        Public API
        Ticker
        Public trades
        Order Book
        Order Rate
        Standard Rate
        Status Retrieval
        
        Private API
        Order
        
          New order
          Order Detail
          Unsettled order list
          Cancel Order
          Order cancellation status
          Order Transactions
          Order Transactions (Pagination)
        
        Account
        
          Balance
          Send BTC
          BTC sends history
          BTC deposits history
          Account information
        
        Withdraw JPY
        
          Bank account list
          Register bank account
          Remove bank account
          Withdraw history
          Create withdraw request
          Cancel withdraw request
        
        
        WebSocket API
        Public WebSocket API
          
            Public trades
            Order Book
          
        Private WebSocket API
          
            Order Events
            Execution Events
          
      
    
    
      
  Overview
  coincheck allows roughly two kinds of APIs; Public API and Private API.
  Public API allows you to browse order status and order book.
  Private API allows you to create and cancel new orders, and to check your balance.
  Request URL
  https://coincheck.com



      
  Authentication
  Please authenticate to use a Private API.

  Generate API Key
  First, please create your API Key. You can create one here.
  Please don't share your Access key and Secret Access key with others
  Make a request using these keys.

  Permission settings
  By generating an API key, you can set a permission for each function.
  And you can also give permission to IP addresses you prefer.
  
    
    Setting API permission
  

  Making a Request
  For requests that require authentication, you have to add information below to HTTP Header.
  
    
      ACCESS-KEY
      Access key you genertaed at API key
    
    
      ACCESS-NONCE
      Positive integer will increase every time you send request (managed for each API key). A common practice is to use UNIX time. Maximum value is 9223372036854775807.
    
    
      ACCESS-SIGNATURE
      SIGNATURE mentioned later
    
  

  Create Signature
  SIGNATURE is a HMAC-SHA256 encoded message containing: ACCESS-NONCE, Request URL and Request body by using API key.

  Ruby
  
require "openssl"

nonce = (Time.now.to_f * 1000).to_i.to_s
url = "https://coincheck.com/api/accounts/balance"
body = "hoge=foo"
message = nonce + url + body
secret = "API_SECRET"
OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new("sha256"), secret, message)
# => "3919705fea4b0cd073b9c6e01e139f3b056782c57c5cffd5aea6d8c4ac98bef7"
  

  PHP
  
$strUrl = "https://coincheck.com/api/accounts/balance";
$intNonce = (int) (microtime(true) * 1000);
$arrQuery = array("hoge" => "foo");
$strAccessSecret = "API_SECRET";
$strMessage = $intNonce . $strUrl . http_build_query($arrQuery);
$strSignature = hash_hmac("sha256", $strMessage, $strAccessSecret);
# => "3bc1f33d802056c61ba8c8108f6ffb7527bcd184461a3ea0fed3cee0a22ae15d"
  

  Request sample
  Ruby
  
require 'net/http'
require 'uri'
require 'openssl'

key = "API_KEY"
secret = "API_SECRET"
uri = URI.parse "https://coincheck.com/api/accounts/balance"
nonce = (Time.now.to_f * 1000).to_i.to_s
message = nonce + uri.to_s
signature = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new("sha256"), secret, message)
headers = {
  "ACCESS-KEY" => key,
  "ACCESS-NONCE" => nonce,
  "ACCESS-SIGNATURE" => signature
}

https = Net::HTTP.new(uri.host, uri.port)
https.use_ssl = true
response = https.start {
  https.get(uri.request_uri, headers)
}

puts response.body
  

  Java
  
import com.google.api.client.http.*;
import com.google.api.client.http.apache.ApacheHttpTransport;
import com.google.api.client.json.jackson2.JacksonFactory;
import org.apache.commons.codec.binary.Hex;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class CoincheckApi {
    private String apiKey;
    private String apiSecret;

    public static void main(String[] args) {
        String key = "API_KEY";
        String secret = "API_SECRET";
        CoincheckApi api = new CoincheckApi(key, secret);
        System.out.println(api.getTicker());
        System.out.println(api.getBalance());
    }

    public CoincheckApi(String apiKey, String apiSecret) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
    }

    public String getTicker() {
        String url = "https://coincheck.com/api/accounts/ticker";
        String jsonString = requestByUrlWithHeader(url, createHeader(url));
        return jsonString;
    }

    public String getBalance() {
        String url = "https://coincheck.com/api/accounts/balance";
        String jsonString = requestByUrlWithHeader(url, createHeader(url));
        return jsonString;
    }

    private Map<String, String> createHeader(String url) {
        Map<String, String> map = new HashMap<String, String>();
        String nonce = createNonce();
        map.put("ACCESS-KEY", apiKey);
        map.put("ACCESS-NONCE", nonce);
        map.put("ACCESS-SIGNATURE", createSignature(apiSecret, url, nonce));
        return map;
    }

    private String createSignature(String apiSecret, String url, String nonce) {
        String message = nonce + url;
        return HMAC_SHA256Encode(apiSecret, message);
    }

    private String createNonce() {
        long currentUnixTime = System.currentTimeMillis();
        String nonce = String.valueOf(currentUnixTime);
        return nonce;
    }

    private String requestByUrlWithHeader(String url, final Map<String, String> headers){
        ApacheHttpTransport transport = new ApacheHttpTransport();
        HttpRequestFactory factory = transport.createRequestFactory(new HttpRequestInitializer() {
            public void initialize(final HttpRequest request) throws IOException {
                request.setConnectTimeout(0);
                request.setReadTimeout(0);
                request.setParser(new JacksonFactory().createJsonObjectParser());
                final HttpHeaders httpHeaders = new HttpHeaders();
                for (Map.Entry<String, String> e : headers.entrySet()) {
                    httpHeaders.set(e.getKey(), e.getValue());
                }
                request.setHeaders(httpHeaders);
            }
        });
        String jsonString;
        try {
            HttpRequest request = factory.buildGetRequest(new GenericUrl(url));
            HttpResponse response = request.execute();
            jsonString = response.parseAsString();
        } catch (IOException e) {
            e.printStackTrace();
            jsonString = null;
        }
        return jsonString;
    }


    public static String HMAC_SHA256Encode(String secretKey, String message) {

        SecretKeySpec keySpec = new SecretKeySpec(
                secretKey.getBytes(),
                "hmacSHA256");

        Mac mac = null;
        try {
            mac = Mac.getInstance("hmacSHA256");
            mac.init(keySpec);
        } catch (NoSuchAlgorithmException e) {
            // can't recover
            throw new RuntimeException(e);
        } catch (InvalidKeyException e) {
            // can't recover
            throw new RuntimeException(e);
        }
        byte[] rawHmac = mac.doFinal(message.getBytes());
        return Hex.encodeHexString(rawHmac);
    }
}
  




      
  Libraries
  We developed a library for each programming language to be helpful when You use API of coincheck and distribute it.

  Ruby
  Librariy is available, if you execute the following commands than a command-line or
  $ gem install ruby_coincheck_client
  if you describe it as follows in Gemfile under Bundler environment.
  gem 'ruby_coincheck_client'
  We can download the gem file from GitHub.
   coincheckjp/ruby_coincheck_client

  PHP
  Add the following to composer.json.
  
  {
    "require": {
        "coincheck/coincheck": "1.0.0"
    }
  }
  
  Package install
  $ composer install
  We can download the package file from GitHub.
   coincheckjp/coincheck-php

  Scala
  
val key = "YOUR-KEY-HERE"
val secret = "YOUR-SECRET-HERE"

import net.pocketengineer.coincheckscala.CoinCheckApiService
import net.pocketengineer.coincheckscala.model._

val cc = new CoinCheckApiService(key, secret)
// Ticker
val ticker: Ticker = cc.getTicker

// OrderBook
val orderBook: OrderBook = cc.getOrderBook

// Account Info
val balance: Balance = cc.getAccountInfo

// Trade
val orderId: Long = cc.tradeBtc(28400, 0.01F, BUY)

// OpenOrder
val openOrders: List[OpenOrder] = cc.getOpenOrder

// Cancel Order
val isSuccess: Boolean = cc.cancelOrder(ORDER_ID)
  
  Build
  sbt assembly
   dsaki/CoinCheckScala




      
  Pagination
  At Some API pagination of coincheck It is possible to get by dividing the data.
  PARAMETERS
  
    
      limit
      You can specify the number of acquisition per page.
    
    
      order
      You can specify "desc" or "asc".
      
    
    
      starting_after
      If you specify the ID you can set the start point of list.
      
    
    
      ending_before
      If you specify the ID you can set the start point of list.
      
    
  
  {"success":true,"pagination":{"limit":1,"order":"desc","starting_after":null,"ending_before":null},"data":[{"id":10,"pair":"btc_jpy","status":"open","created_at":"2015-12-02T05:27:53.000Z","closed_at":null,"open_rate":"43553.0","closed_rate":null,"amount":"1.51347797","all_amount":"1.51045705","side":"sell","pl":"-8490.81029287","new_order":{"id":23104033,"side":"sell","rate":null,"amount":null,"pending_amount":"0","status":"complete","created_at":"2015-12-02T05:27:52.000Z"},"close_orders":[{"id":23755132,"side":"buy","rate":"10000.0","amount":"1.0","pending_amount":"0.0","status":"cancel","created_at":"2015-12-05T05:03:56.000Z"}]}]}


      
  Public API
  Public API allows you to browse order status, order transactions and order book.


      
  Ticker
  Check latest information
  If pair is not specified, you can get the information of btc_jpy.
  HTTP REQUEST
  GET /api/ticker
  PARAMETERS
  
    
      pair
      Specify a currency pair to trade. btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy are now available.
    
  
  {"last":27390,"bid":26900,"ask":27390,"high":27659,"low":26400,"volume":"50.29627103","timestamp":1423377841}
  RESPONSE ITEMS
  
    
      last
      Latest quote
    
    
      bid
      Current highest buying order
    
    
      ask
      Current lowest selling order
    
    
      high
      The highest price within 24 hours
    
    
      low
      The lowest price within 24 hours
    
    
      volume
      24 hours trading volume
    
    
      timestamp
      Current time
    
  


      
  Public trades
  You can get current order transactions.
  HTTP REQUEST
  GET /api/trades
  PARAMETERS
  
    
      *pair
      Specify a currency pair to trade. btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy are now available.
    
  
  {"success":true,"pagination":{"limit":1,"order":"desc","starting_after":null,"ending_before":null},"data":[{"id":82,"amount":"0.28391","rate":"35400.0","pair":"btc_jpy","order_type":"sell","created_at":"2015-01-10T05:55:38.000Z"},{"id":81,"amount":"0.1","rate":"36120.0","pair":"btc_jpy","order_type":"buy","created_at":"2015-01-09T15:25:13.000Z"}]}
  ※ For itayose, order_type will be null.


      
  Order Book
  Fetch order book information.
  HTTP REQUEST
  GET /api/order_books
  PARAMETERS
  
    
      *pair
      Currency pair. btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy are now available.
    
  
  {"asks":[[27330,"2.25"],[27340,"0.45"]],"bids":[[27240,"1.1543"],[26800,"1.2226"]]}
  RESPONSE ITEMS
  
    
      asks
      Sell order status
    
    
      bids
      Buy order status
    
  


      
  Calc Rate
  To calculate the rate from the order of the exchange.
  HTTP REQUEST
  GET /api/exchange/orders/rate
  PARAMETERS
  
    
      *order_type
      Order type（"sell" or "buy"）
    
    
      *pair
      Specify a currency pair to trade. btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy are now available.
    
    
      amount
      Order amount (ex) 0.1
    
    
      price
      Order price (ex) 28000
    
    ※ Either price or amount must be specified as a parameter.
  

  {"success":true,"rate": 60000, "price": 60000, "amount": 1.0}
  RESPONSE ITEMS
  
    
      rate
      Order rate
    
    
      price
      Order price
    
    
      amount
      Order amount
    
  


      
  Standard Rate
  Standard Rate of Coin.
  HTTP REQUEST
  GET /api/rate/[pair]
  PARAMETERS
  
    
      *pair
      pair (e.g. "btc_jpy" )
    
  

  {"rate": "60000"}
  RESPONSE ITEMS
  
    
      rate
      rate
    
  


      
  Status Retrieval
  Retrieving the status of the exchange.
  For a description of the exchange status, please refer to this page.
  HTTP REQUEST
  GET /api/exchange_status
  PARAMETERS
  
    
      If pair is not specified, information on all tradable pairs is returned.
    
    
      If pair is specified, information is returned only for that particular currency.
      
        Currently available pairs are btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy.
      
    
  
  
    {
  "exchange_status": [
    {
      "pair": "btc_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "eth_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "etc_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "lsk_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "xrp_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "xem_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "bch_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "mona_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "iost_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "enj_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "chz_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "imx_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "shib_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "avax_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "fnct_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "dai_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "wbtc_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "bril_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "bc_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "doge_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "pepe_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "mask_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "mana_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "trx_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "grt_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "sol_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    },
    {
      "pair": "fpl_jpy",
      "status": "available",
      "timestamp": 1771858577,
      "availability": {
        "order": true,
        "market_order": true,
        "cancel": true
      }
    }
  ]
}
  
  RESPONSE ITEMS
  
    
      pair
      Symbol
    
    
      status
      Exchange status ( available, itayose, stop ).
    
    
      timestamp
      Time of Status Retrieval
    
    
      availability
      Limit orders ( order ) , market orders ( market_order ), cancel orders ( cancel ) can be placed
      
          
            order
            Availability of limit orders (true or false)
          
          
            market_order
            Availability of market orders (true or false)
          
          
            cancel
            Availability of cancel orders (true or false)
          
      
    
  


      
  Private API
  Private API allows you to order, cancel new orders and make sure your balance.


      
  Order
  You can use API about orders in exchange.


      
  New order
  Publish new order to exchange.
  For example if you'd like buy 10 BTC as 30000 JPY/BTC, you need to specify following parameters.rate: 30000, amount: 10, order_type: "buy", pair: "btc_jpy"
  In case of buying order, if selling order which is lower than specify price is already exist, we settle in low price order. In case of to be short selling order, remain as unsettled order. It is also true for selling order.
  About rate limit
  New order to the exchange can be up to 4 requests per second.
  If exceeded, it will return 429:too_many_requests error.
  Limits are not per currency pair.
  Limits may be changed depending on the system load status.

  About order_type
  There 4 types of order_type .
  
    
      "buy"
      Limit, Spot, Buy
    
    
      "sell"
      Limit, Spot, Sell
    
    
      "market_buy"
      Market, Spot, Buy
    
    
      "market_sell"
      Market, Spot, Sell
    
  
  "buy"
  Limit, Spot, Buy
  
    
      *rate
      Order rate. ex) 28000
    
    
      *amount
      Order amount. ex) 0.1
    
  
  "sell"
  Limit, Spot, Sell
  
    
      *rate
      Order rate. ex) 28000
    
    
      *amount
      Order amount. ex) 0.1
    
  
  "market_buy"
  Market, Spot, Buy
  In MarketBuy you have to specify JPY not BTC.
  
    
      *market_buy_amount
      Market buy amount in JPY not BTC. ex) 10000
    
  
  "market_sell"
  Market, Spot, Sell
  
    
      *amount
      Order amount. ex) 0.1
    
  
  HTTP REQUEST
  POST /api/exchange/orders
  PARAMETERS
  
    
      *pair
      Specify a currency pair to trade. btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy are now available.
    
    
      *order_type
      Specify order_type.
    
    
      rate
      Order rate. ex) 28000
    
    
      amount
      Order amount. ex) 0.1
    
    
      market_buy_amount
      Market buy amount in JPY not BTC. ex) 10000
    
    
      stop_loss_rate
      Stop Loss Rate. Trigger price for order execution (What is Stop Loss Order?) ex) 29500. Also, if it is not a stop loss order, null is also possible.
    
    
      time_in_force
      Time In Force(optional). The following values can be specified.
      
        
          good_til_cancelled
          The order will last until it is completed or you cancel it (default)
        
        
          post_only
          Only maker orders are placed. If the order would execute as a taker, it will be cancelled ( What is post only? )
        
      
    
  
  {"success": true, "id": 12345, "rate": "30010.0", "amount": "1.3", "order_type": "sell", "time_in_force": "good_til_cancelled", "stop_loss_rate": null, "pair": "btc_jpy", "created_at": "2015-01-10T05:55:38.000Z"}
  RESPONSE ITEMS
  
    
      id
      New order ID
    
    
      rate
      Order rate
    
    
      amount
      Order amount
    
    
      order_type
      Order type
    
    
      time_in_force
      Time In Force
    
    
      stop_loss_rate
      Stop Loss Rate
    
    
      pair
      Deal pair
    
    
      created_at
      Order date
    
  


      
  Order details
  You can get the details of the order.
  About rate limit
  Order details API calls can be requested to the exchange at most once per second.
  If exceeded, it will return 429:too_many_requests error.
  Limits are not per currency pair.
  Limits may be changed depending on the system load status.
  HTTP REQUEST
  GET /api/exchange/orders/[id]
  PARAMETERS
  
    
      *id
      Order ID（It's the same ID in New order.）
    
  
  
    {
  "success": true,
  "id": 12345,
  "pair": "btc_jpy",
  "status": "PARTIALLY_FILLED_EXPIRED",
  "order_type": "buy",
  "rate": "0.1",
  "stop_loss_rate": null,
  "maker_fee_rate": "0.001",
  "taker_fee_rate": "0.001",
  "amount": "1.0",
  "market_buy_amount": null,
  "executed_amount": "0",
  "executed_market_buy_amount": null,
  "expired_type": "self_trade_prevention",
  "prevented_match_id": 123,
  "expired_amount": "1.0",
  "expired_market_buy_amount": null,
  "time_in_force": "good_til_cancelled",
  "created_at": "2015-01-10T05:55:38.000Z"
}
  
  RESPONSE ITEMS
  
    
      id
      Order ID（It's the same ID in New order.）
    
    
      pair
      Deal pair
    
    
      status
      Order Status
      
          
            *NEW
            Order Received
          
          
            *WAITING_FOR_TRIGGER
            Before Trigger Conditions like Stoploss
          
          
            *PARTIALLY_FILLED
            Partially Filled
          
          
            *FILLED
            Fully Filled
          
          
            *CANCELED
            Canceled
          
          
            *EXPIRED
            Expired
          
          
            *PARTIALLY_FILLED_CANCELED
            Partially Filled and Canceled
          
          
            *PARTIALLY_FILLED_EXPIRED
            Partially Filled and Expired
          
      
    
    
      order_type
      Order type（It's the same order_type in New order.）
    
    
      rate
      Order rate
    
    
      stop_loss_rate
      Stop Loss Order's Rate
    
    
      maker_fee_rate
      Make fee rate（ex）0.001
    
    
      taker_fee_rate
      Taker fee rate（ex）0.001
    
    
      amount
      Order amount
    
    
      market_buy_amount
      Market buy amount
    
    
      executed_amount
      Executed amount（ex）0.03
    
    
      executed_market_buy_amount
      Executed market buy amount（ex）900.0
    
    
      expired_type
      Reasons for Expiration
      
          
            *self_trade_prevention
            Expired due to self-trade prevention
          
          
            *price_limit
            Expired due to price limit
          
          
            *post_only
            Expired because post-only order did not become a Maker
          
          
            *unfilled_market
            Expired because market order was not fully filled
          
          
            *itayose_market
            Market order expired while accepting limit orders
          
      
    
    
      prevented_match_id
      Prevented match ID（ex）123
    
    
      expired_amount
      Expired amount（ex）1.0
    
    
      expired_market_buy_amount
      Expired market buy amount（ex）100.0
    
    
      time_in_force
      Time In Force
      
        
          good_til_cancelled
          The order will last until it is completed or you cancel it (default)
        
        
          post_only
          Place only maker orders
        
      
    
    
      created_at
      Order date
    
  


      
  Unsettled order list
  You can get a unsettled order list.
  HTTP REQUEST
  GET /api/exchange/orders/opens

  {"success":true,"orders":[{"id":202835,"order_type":"buy","rate":26890,"pair":"btc_jpy","pending_amount":"0.5527", "pending_market_buy_amount": null,"stop_loss_rate": null, "created_at": "2015-01-10T05:55:38.000Z"},{"id":202836,"order_type":"sell","rate":26990,"pair":"btc_jpy","pending_amount":"0.77", "pending_market_buy_amount": null,"stop_loss_rate": null, "created_at": "2015-01-10T05:55:38.000Z"},{"id":38632107,"order_type":"buy","rate":null,"pair":"btc_jpy","pending_amount":null,"pending_market_buy_amount": "10000.0", "stop_loss_rate":"50000.0","created_at":"2016-02-23T12:14:50.000Z"}]}
  RESPONSE ITEMS
  
    
      id
      Order ID（It's the same ID in New order.）
    
    
      rate
      Order rate ( Market order if null)
    
    
      pending_amount
      Unsettle order amount
    
    
      pending_market_buy_amount
      Unsettled order amount (only for spot market buy order)
    
    
      order_type
      order type（"sell" or "buy"）
    
    
      stop_loss_rate
      Stop Loss Order's Rate
    
    
      pair
      Deal pair
    
    
      created_at
      Order date
    
  


      
  Cancel Order
  New OrderOr, you can cancel by specifyingunsettle order list's ID.
  HTTP REQUEST
  DELETE /api/exchange/orders/[id]
  PARAMETERS
  
    
      *id
      New order or Unsettle order list's ID
    
  
  {"success": true, "id": 12345}
  RESPONSE ITEMS
  
    
      id
      Canceled order ID
    
  


      
  Order cancellation status
  You can refer to the cancellation processing status of the order.
  HTTP REQUEST
  GET /api/exchange/orders/cancel_status?id=[id]
  PARAMETERS
  
    
      *id
      New Order Or, you can cancel by specifyingunsettle order list's ID.
    
  
  {"success": true, "id": 12345, "cancel": true, "created_at": "2020-07-29T17:09:33.000Z"}
  RESPONSE ITEMS
  
    
      id
      Order ID
    
    
      cancel
      Canceled（true or false）※1
    
    
      created_at
      Ordered time
    
  
  ※1 Expired orders are also treated as canceled orders.



      
  Transaction history
  Display your transaction history
  HTTP REQUEST
  GET /api/exchange/orders/transactions
  {"success":true,"transactions":[{"id":38,"order_id":49,"created_at":"2015-11-18T07:02:21.000Z","funds":{"btc":"0.1","jpy":"-4096.135"},"pair":"btc_jpy","rate":"40900.0","fee_currency":"JPY","fee":"6.135","liquidity":"T","side":"buy"},{"id":37,"order_id":48,"created_at":"2015-11-18T07:02:21.000Z","funds":{"btc":"-0.1","jpy":"4094.09"},"pair":"btc_jpy","rate":"40900.0","fee_currency":"JPY","fee":"-4.09","liquidity":"M","side":"sell"}]}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      order_id
      Order ID
    
    
      created_at
      Ordered time
    
    
      funds
      Each fund balance's increase and decrease
    
    
      pair
      Pair
    
    
      rate
      Rate
    
    
      fee_currency
      Fee currency
    
    
      fee
      Fee amount
    
    
      liquidity
      "T" ( Taker ) or "M" ( Maker ) or "itayose" ( Itayose )
    
    
      side
      "sell" or "buy"
    
  



      
  Transaction history (Pagination)
  Display your transaction history
  HTTP REQUEST
  GET /api/exchange/orders/transactions_pagination
  {"success":true,"pagination":{"limit":1,"order":"desc","starting_after":null,"ending_before":null},"data":[{"id":38,"order_id":49,"created_at":"2015-11-18T07:02:21.000Z","funds":{"btc":"0.1","jpy":"-4096.135"},"pair":"btc_jpy","rate":"40900.0","fee_currency":"JPY","fee":"6.135","liquidity":"T","side":"buy"},{"id":37,"order_id":48,"created_at":"2015-11-18T07:02:21.000Z","funds":{"btc":"-0.1","jpy":"4094.09"},"pair":"btc_jpy","rate":"40900.0","fee_currency":"JPY","fee":"-4.09","liquidity":"M","side":"sell"}]}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      order_id
      Order ID
    
    
      created_at
      Ordered time
    
    
      funds
      Each fund balance's increase and decrease
    
    
      pair
      Pair
    
    
      rate
      Rate
    
    
      fee_currency
      Fee currency
    
    
      fee
      Fee amount
    
    
      liquidity
      "T" ( Taker ) or "M" ( Maker ) or "itayose" ( Itayose )
    
    
      side
      "sell" or "buy"
    
  



      
  Account
  You can get balance and various information.


      
  Balance
  Check your account balance.
  It doesn't include jpy_reserved use unsettled orders injpy btc.
  HTTP REQUEST
  GET /api/accounts/balance
  {"success": true, "jpy": "0.8401", "btc": "7.75052654", "jpy_reserved": "3000.0", "btc_reserved": "3.5002", "jpy_lending": "0", "btc_lending": "0.1", "jpy_lend_in_use": "0", "btc_lend_in_use": "0.3", "jpy_lent": "0", "btc_lent": "1.2", "jpy_debt": "0", "btc_debt": "0", "jpy_tsumitate": "10000.0", "btc_tsumitate": "0.4034"}
  RESPONSE ITEMS
  This API dynamically returns balances for all currencies of the authenticated account. The above are representative examples (JPY, BTC).
  For each currency, the following 7 types of balance are returned (<currency> is the currency)
  
    
      <currency>
      Balance for currency
    
    
      <currency>_reserved
      Balance reserved for unsettled orders
    
    
      <currency>_lending
      Balance in lending account before applying for lending
    
    
      <currency>_lend_in_use
      Balance in lending account for which a lending application has been made
    
    
      <currency>_lent
      Balance lent in lending account
    
    
      <currency>_debt
      Borrowed balance
    
    
      <currency>_tsumitate
      Balance being accumulated (Tsumitate)
    
  


      
  Send Crypto Currency
  Sending Crypto Currency to specified address
  HTTP REQUEST
  POST /api/send_money
  PARAMETERS
  
    
      *remittee_list_id
      RemitteeList Id sending to
    
    
      *amount
      Amount
    
    
      *purpose_type
      Purpose Type
    
    
      purpose_details
      Purpose Details
    
  

  PURPOSE TYPES
  The following is a list of keys that can be specified for purpose_type. Depending on the value of purpose_type, it may be necessary to specify detailed information in object format in purpose_details.
  
      
        inheritance_or_donating
        Inheritance, gift of living expenses
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.001", "purpose_type": "inheritance_or_donating"}
          
            
              No purpose_details specification is required for this purpose_type.
            
          
      
      
        payment_of_importing
        Settlement of Import Payments
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.000001", "purpose_type": "payment_of_importing", "purpose_details": { "specific_items_of_goods": "食料品", "place_of_origin": "カナダ", "place_of_loading": "カナダ" }}
          
            
              *purpose_details
            
            
              
                  
                    *specific_items_of_goods
                    Specific Items of Goods
                  
                  
                    *place_of_origin
                    Place of Origin
                  
                  
                    *place_of_loading
                    Place of Loading
                  
              
            
          
      
      
        payment_of_intermediary_trade
        Settlement of Intermediary Trade Payments
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.002", "purpose_type": "payment_of_intermediary_trade", "purpose_details": { "specific_items_of_goods": "原材料", "place_of_origin": "タイ", "place_of_loading": "タイ", "place_of_destination": "日本" }}
          
            
              *purpose_details
            
            
              
                  
                    *specific_items_of_goods
                    Specific Items of Goods
                  
                  
                    *place_of_origin
                    Place of Origin
                  
                  
                    *place_of_loading
                    Place of Loading
                  
                  
                    *place_of_destination
                    Place of Destination
                  
              
            
          
      
      
        payment_of_domestic_transactions
        Settlement of payment for domestic transactions
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.001", "purpose_type": "payment_of_domestic_transactions"}
          
            
              No purpose_details specification is required for this purpose_type.
            
          
      
      
        keep_own_account
        Keep at own account with other crypto asset exchange, other services
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.001", "purpose_type": "keep_own_account"}
          
            
              No purpose_details specification is required for this purpose_type.
            
          
      
      
        keep_own_private_wallet
        Keep at own private wallet (e.g. MetaMask)
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.001", "purpose_type": "keep_own_private_wallet"}
          
            
              No purpose_details specification is required for this purpose_type.
            
          
      
      
        other
        Other
          Usage Example:
            {"remittee_list_id": 12345, "amount": "0.0005", "purpose_type": "other", "purpose_details": { "extra_text": "個人間送金" }}
          
            
              *purpose_details
            
            
              
                  
                    *extra_text
                    Specific Purpose of the Transfer
                  
              
            
          
      
  

  {"success": true, "id": "276", "address": "1v6zFvyNPgdRvhUufkRoTtgyiw1xigncc", "amount": "1.5", "fee": "0.002"}
  RESPONSE ITEMS
  
    
      id
      Send
    
    
      address
      Recipient's address
    
    
      amount
      Amount of sent
    
    
      fee
      fee
    
  


      
  Sending History
  BTC Sending history
  HTTP REQUEST
  GET /api/send_money
  PARAMETERS
  
    
      *currency
      Currency(Only BTC)
    
  

  {"success": true, "sends": [{ "id": 2, "amount": "0.05", "currency": "BTC", "fee": "0.0", "address": "13PhzoK8me3u5nHzzFD85qT9RqEWR9M4Ty", "created_at": "2015-06-13T08:25:20.000Z" }, { "id": 1, "amount": "0.05", "currency": "BTC", "fee": "0.0001", "address": "118ekvRwx6uc4241jkuQt5eYvLiuWdMW2", "created_at": "2015-06-13T08:21:18.000Z" }] }
  RESPONSE ITEMS
  
    
      id
      Send
    
    
      amount
      Amount of bitcoins sent
    
    
      fee
      Fee
    
    
      currency
      Currency
    
    
      address
      Recipient's bitcoin address
    
    
      created_at
      Date you sent
    
  




      
  Deposits History
  BTC deposit history
  HTTP REQUEST
  GET /api/deposit_money
  PARAMETERS
  
    
      *currency
      Currency(BTC now)
    
  

  {"success": true, "deposits": [{ "id": 2, "amount": "0.05", "currency": "BTC", "address": "13PhzoK8me3u5nHzzFD85qT9RqEWR9M4Ty", "status": "confirmed", "confirmed_at": "2015-06-13T08:29:18.000Z", "created_at": "2015-06-13T08:22:18.000Z" }, { "id": 1, "amount": "0.01", "currency": "BTC", "address": "13PhzoK8me3u5nHzzFD85qT9RqEWR9M4Ty", "status": "received", "confirmed_at": "2015-06-13T08:21:18.000Z", "created_at": "2015-06-13T08:21:18.000Z" }] }
  RESPONSE ITEMS
  
    
      id
      Received ID
    
    
      amount
      Amount of BTC received
    
    
      currency
      Currency
    
    
      address
      Bitcoin address you reveived BTC
    
    
      status
      Status
    
    
      confirmed_at
      Date Confirmed
    
    
      created_at
      Date when receiving process started
    
  


      
  Account information
  Display account information.
  HTTP REQUEST
  GET /api/accounts
  
    {
  "success": true,
  "id": 10000,
  "email": "test@gmail.com",
  "identity_status": "identity_pending",
  "bitcoin_address": "1v6zFvyNPgdRvhUufkRoTtgyiw1xigncc",
  "taker_fee": "0.15",
  "maker_fee": "0.0",
  "exchange_fees": {
    "btc_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "eth_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "etc_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    },
    "lsk_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "xrp_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "xem_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "bch_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "mona_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "iost_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    },
    "enj_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "chz_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "imx_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "shib_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "avax_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "fnct_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    },
    "dai_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "wbtc_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "bril_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    },
    "bc_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    },
    "doge_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "pepe_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "mask_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "mana_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "trx_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "grt_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "sol_jpy": {
      "maker_fee_rate": "0.0",
      "taker_fee_rate": "0.0"
    },
    "fpl_jpy": {
      "maker_fee_rate": "0.05",
      "taker_fee_rate": "0.1"
    }
  }
}
  
  RESPONSE ITEMS
  
    
      id
      Account ID. It's the same as the ID you specify when you deposit JPY.
    
    
      email
      Registered e-mail
    
    
      identity_status
      Your identity status.
    
    
      bitcoin_address
      Your bitcoin address for deposit
    
    
      taker_fee
      It displays the fee rate (%) in the case of performing the order as Taker.(BTC_JPY)
    
    
      maker_fee
      It displays the fee rate (%) in the case of performing the order as Maker.(BTC_JPY)
    
    
      exchange_fees
      It displays the fee for each order book.
    
  


      
  Withdraw JPY
  You can withdraw JPY through this API.


      
  Bank account list
  Display list of bank account you registered (withdrawal).
  HTTP REQUEST
  GET /api/bank_accounts

  {"success":true,"data":[{"id":243,"bank_name":"みずほ","branch_name":"東京営業部","bank_account_type":"futsu","number":"0123456","name":"タナカ　タロウ"}]}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      bank_name
      Bank name
    
    
      branch_name
      Branch name
    
    
      bank_account_type
      Type of bank account
    
    
      number
      Bank account number
    
    
      name
      Bank account name
    
  


      
  Register bank account
  Register bank account for withdrawal.
  HTTP REQUEST
  POST /api/bank_accounts
  PARAMETERS
  
    
      *bank_name
      Bank name
    
    
      *branch_name
      Branch name
    
    
      *bank_account_type
      Type of bank account ( "futsu" or "toza" )
    
    
      *number
      Bank account number (ex) "0123456"
    
    
      *name
      Bank account name
    
  

  {"success":true,"data":{"id":641,"bank_name":"熊本","branch_name":"田中","bank_account_type":"futsu","number":"0123456","name":"hoge"}}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      bank_name
      Bank name
    
    
      branch_name
      Branch name
    
    
      bank_account_type
      Type of bank account ( "futsu" or "toza" )
    
    
      number
      Bank account number (ex) "0123456"
    
    
      name
      Bank account name
    
  


      
  Remove bank account
  Will remove your bank account.
  HTTP REQUEST
  DELETE /api/bank_accounts/[id]
  PARAMETERS
  
    
      *id
      Bank account list iD
    
  

  {"success":true}


      
  Withdraw history
  Display Japanese YEN withdrawal request history.
  HTTP REQUEST
  GET /api/withdraws

  {"success":true,"pagination":{"limit":25,"order":"desc","starting_after":null,"ending_before":null},"data":[{"id":398,"status":"finished","amount":"242742.0","currency":"JPY","created_at":"2014-12-04T15:00:00.000Z","bank_account_id":243,"fee":"400.0", "is_fast": true}]}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      status
      Withdraw status ( pending, processing, finished, canceled )
    
    
      amount
      Amount
    
    
      currency
      Currency
    
    
      created_at
      Date you created
    
    
      bank_account_id
      Bank account ID
    
    
      fee
      Fee
    
    
      is_fast
      Fast withdraw option. Currently stopped.
    
  


      
  Create withdraw
  Request Japanese Yen withdrawal
  HTTP REQUEST
  POST /api/withdraws
  PARAMETERS
  
    
      *bank_account_id
      Bank account ID
    
    
      *amount
      Amount
    
    
      *currency
      Currency ( only "JPY" )
    
  

  {"success":true,"data":{"id":1043,"status":"pending","amount":"10000.0","currency":"JPY","created_at":"2015-08-31T11:32:45.213Z","bank_account_id":243,"fee":"300.0"}}
  RESPONSE ITEMS
  
    
      id
      ID
    
    
      status
      Withdraw status ( pending, processing, finished, canceled )
    
    
      amount
      Amount
    
    
      currency
      Currency ( only "JPY" )
    
    
      created_at
      Date you created
    
    
      bank_account_id
      Bank account ID
    
    
      fee
      Fee
    
  


      
  Cancel withdrawal
  Cancel withdrawal request.
  You can only cancel a withdrawal request that has the pending status.
  HTTP REQUEST
  DELETE /api/withdraws/[id]
  PARAMETERS
  
    
      *id
      Withdraw ID
    
  

  {"success":true}


      
  WebSocket API
  In addition to the REST API, Coincheck Exchange provides a WebSocket API. The WebSocket API allows you to receive market data and updates to your account's order status in real time. Unlike traditional HTTP polling with REST APIs, the WebSocket API enables low-latency and efficient communication through server-initiated data delivery. Because trade data is pushed the moment it occurs, this API is ideal for real-time monitoring applications.
  There are two types of WebSocket APIs available:
  Public WebSocket API
  The Public WebSocket API allows anyone to receive market data—such as trade history and order book updates—in real time. No authentication is required, making it ideal for use cases such as price monitoring, chart rendering, and alert systems.
  Private WebSocket API
  The Private WebSocket API delivers real-time updates for order events and trade executions. Authentication is required to use this API. It enables real-time monitoring of your trading activity and is well-suited for building automated trading systems and order management tools.


      
  Public WebSocket API
  Overview
  The Public WebSocket API is available without authentication. After establishing a connection, you can subscribe to multiple currency pair channels and monitor the entire market efficiently with a single WebSocket connection. Data is pushed approximately every 0.1 seconds when a trade occurs. We recommend implementing automatic reconnection logic in case of network interruptions.
  Connection Flow
  1. Establish WebSocket Connection
  Connect to the following URI:
  wss://ws-api.coincheck.com
  2. Subscribe to Channels
  Once connected, send a subscribe message to begin receiving updates from the desired channel.
  Example
  //JavaScript//Run in Chromesocket = new WebSocket("wss://ws-api.coincheck.com/")socket.send(JSON.stringify({type: "subscribe", channel: "btc_jpy-orderbook"}))socket.send(JSON.stringify({type: "subscribe", channel: "btc_jpy-trades"}))
  Supported Currency Pairs
  btc_jpy, eth_jpy, etc_jpy, lsk_jpy, xrp_jpy, xem_jpy, bch_jpy, mona_jpy, iost_jpy, enj_jpy, chz_jpy, imx_jpy, shib_jpy, avax_jpy, fnct_jpy, dai_jpy, wbtc_jpy, bril_jpy, bc_jpy, doge_jpy, pepe_jpy, mask_jpy, mana_jpy, trx_jpy, grt_jpy, sol_jpy, fpl_jpy
  Commands
  subscribe Command
  Begins subscribing to a specific channel. With the Public WebSocket API, each subscribe command can subscribe to only one channel. To subscribe to multiple channels, send a separate subscribe command for each.
  REQUEST ITEMS
  {"type":"subscribe","channel":"channel_name_to_subscribe"}
  REQUEST EXAMPLE
  {"type":"subscribe","channel":"btc_jpy-trades"}


      
  Public trades Channel
  The Public Trades Channel pushes information on recent transactions every 0.1 seconds. Specify the desired currency pair as [pair] based on the list of supported pairs above.
  REQUEST ITEMS
  {"type":"subscribe","channel":"[pair]-trades"}
  RESPONSE ITEMS
  ["transaction timestamp (unix time)", "transaction ID","pair","transaction rate","transaction amount","order side","ID of the Taker","ID of the Maker","ID of the Itayose order"]
  ※ Only information on Taker or Itayose orders is pushed through the stream.
  ※ Itayose is a separate category from Taker/Maker. Since all matched buy and sell information is streamed, the total aggregated volume will not match the actual total transaction volume.
  ※ For regular trades, the Itayose order ID will be null. For Itayose trades, the Taker/Maker order IDs will be null.
  REQUEST EXAMPLE
  {"type":"subscribe","channel":"btc_jpy-trades"}
  RESPONSE EXAMPLES
  ※ The transaction information will be pushed as a 2-dimensional array.
  [["1663318663","2357062","btc_jpy","2820896.0","5.0","sell","1193401","2078767",null],["1663318892","2357068","btc_jpy","2820357.0","0.7828","buy","4456513","8046665",null]]


      
  Order Book Channel
  Send the difference of order book information at regular intervals. Specify the desired currency pair as [pair] based on the list of supported pairs above.
  REQUEST ITEMS
  {"type":"subscribe", "channel":"[pair]-orderbook"}
  RESPONSE ITEMS
  ["[pair]",{"bids":[["order rate","order amount"],["order rate","order amount"]],"asks":[["order rate","order amount"],["order rate","order amount"]], "last_update_at": "timestamp (unix time)"}]
  ※ "bids" refer to buy orders, and "asks" refer to sell orders.
  REQUEST EXAMPLE
  {"type":"subscribe","channel":"btc_jpy-orderbook"}
  RESPONSE EXAMPLES
  ["btc_jpy",{"bids":[["148634.0","0.12"],["148633.0","0.0574"]],"asks":[["148834.0","0.0812"],["148833.0","1.0581"]],"last_update_at":"1659321701"}]


      
  Private WebSocket API

  Overview
  The Private WebSocket API requires authentication. Similar to the REST API, you must use your ACCESS-KEY, ACCESS-NONCE, and ACCESS-SIGNATURE to log in before receiving real-time events related to your orders and executions. The channels you can subscribe to depend on the permissions granted to your API key.
  If your connection is interrupted, or if the API key is updated or revoked, the Private WebSocket connection will be automatically closed. We recommend implementing automatic reconnection in your application.

  Connection Flow

  1. Preparation
  
    Create an API key and configure its permissions
      
        Ensure that the channels you intend to subscribe to under the WebSocket section are enabled
      
    
    Obtain your ACCESS-KEY and SECRET-KEY
      
        Optionally configure the source IP address for added security
      
    
  

  2. Establish WebSocket Connection
  Connect to the following URI:
  wss://stream.coincheck.com

  3. Authentication (login)
  
    To authenticate, use the ACCESS-KEY, ACCESS-NONCE, and ACCESS-SIGNATURE as described in the
    Authentication
    section.
  

  4. Subscribe to Channels
  After successful authentication, send a subscribe request for the desired channels.

  Ruby Example
  For the Private WebSocket API, the uri must always be wss://stream.coincheck.com/private .

  require 'uri'
require 'openssl'

key = "API_KEY"
secret = "API_SECRET"

# URI is a fixed value
uri = URI.parse "wss://stream.coincheck.com/private"

nonce = (Time.now.to_f * 1000).to_i.to_s
# => "1756746080103"

message = nonce + uri.to_s
signature = OpenSSL::HMAC.hexdigest(
  OpenSSL::Digest.new("sha256"), 
  secret, 
  message
)
# => "577ea3f3900bac682d65751d76fcc21ea11a8a57431e6e8e83efbba8effd4265"

  Example: Connect Using websocat
  
    websocat is a command-line WebSocket client that you can use to test the Private WebSocket API. The following example demonstrates the login and channel subscription flow.
  
  
    Use the generated ACCESS-KEY, ACCESS-NONCE, and ACCESS-SIGNATURE to authenticate. Once logged in, you may subscribe to any enabled private channels. You can also unsubscribe from channels as needed. Note that channels must be enabled in the
    Authentication
    Authentication permissions section to be accessible.
  

  $ websocat wss://stream.coincheck.com/
{"type":"login","access_key":"ACCESS_KEY","access_nonce":"1756746080103","access_signature":"577ea3f3900bac682d65751d76fcc21ea11a8a57431e6e8e83efbba8effd4265"}
{"success":true,"available_channels":["order-events","execution-events"]}
{"type":"subscribe","channels":["order-events","execution-events"]}
{"type":"unsubscribe","channels":["order-events"]}
^C

  Commands

  login Command
  Performs authentication.

  REQUEST ITEMS
  {
  "type":"login",
  "access_key":"ACCESS-KEY",
  "access_nonce":"ACCESS-NONCE",
  "access_signature":"ACCESS-SIGNATURE"
}

  REQUEST EXAMPLE
  {"type":"login","access_key":"ACCESS_KEY","access_nonce":"1756746080103","access_signature":"577ea3f3900bac682d65751d76fcc21ea11a8a57431e6e8e83efbba8effd4265"}
  RESPONSE ITEMS
  {
  "success": "true if authentication succeeded, false otherwise",
  "available_channels": "list of channels authorized for the current API key"
}

  RESPONSE EXAMPLE
  {
  "success":true,
  "available_channels":["order-events","execution-events"]
}

  subscribe Command
  Begins subscription to one or more channels.
  The Private WebSocket API allows subscribing to multiple channels with a single subscribe command.

  REQUEST ITEMS
  {
  "type":"subscribe",
  "channels": "Channels to subscribe (multiple channels allowed in array format)"
}

  REQUEST EXAMPLE
  {"type":"subscribe","channels":["order-events","execution-events"]}

  unsubscribe Command
  Stops subscription to specified channels.

  REQUEST ITEMS
  {
  "type":"unsubscribe",
  "channels": "List of channels to unsubscribe (multiple channels allowed in array format)"
}

  REQUEST EXAMPLE
  {"type":"unsubscribe","channels":["order-events","execution-events"]}


      
  Order Events Channel
  This channel delivers order-related events.
  The following order event types may be received:

  
    
      
        
          Event Description
          order_event
        
      
      
        
          Stop Loss Order triggered
          TRIGGERED
        
        
          Partial fill
          PARTIALLY_FILL
        
        
          Filled
          FILL
        
        
          Expired
          EXPIRY
        
        
          Canceled
          CANCEL
        
      
    
  

  
    Note: Messages are not re-delivered. To retrieve missed events, please use the
    Order Detail
    endpoint in the REST API.
  

  REQUEST ITEMS
  {"type":"subscribe","channels":["order-events"]}

  RESPONSE ITEMS
  {
  "channel": "order-events",
  "id": "Order ID (It's the same ID in Order Detail)",
  "pair": "Deal pair",
  "order_event": "Event type",
  "order_type": "Order type",
  "rate": "Order rate",
  "stop_loss_rate": "Stop Loss Order's Rate",
  "maker_fee_rate": "Maker fee rate",
  "taker_fee_rate": "Taker fee rate",
  "amount": "Order amount",
  "market_buy_amount": "Market buy amount",
  "latest_executed_amount": "Latest executed amount",
  "latest_executed_market_buy_amount": "Latest executed market buy amount",
  "expired_type": "Reasons for Expiration",
  "prevented_match_id": "Prevented match ID",
  "expired_amount": "Expired amount",
  "expired_market_buy_amount": "Expired market buy amount",
  "time_in_force": "Time In Force",
  "event_time": "Event time"
}

  RESPONSE EXAMPLE
  {
  "channel": "order-events",
  "id": 12345,
  "pair": "btc_jpy",
  "order_event": "EXPIRY",
  "order_type": "buy",
  "rate": "0.1",
  "stop_loss_rate": null,
  "maker_fee_rate": "0.001",
  "taker_fee_rate": "0.001",
  "amount": "1.0",
  "market_buy_amount": null,
  "latest_executed_amount": "0",
  "latest_executed_market_buy_amount": null,
  "expired_type": "self_trade_prevention",
  "prevented_match_id": 123,
  "expired_amount": "1.0",
  "expired_market_buy_amount": null,
  "time_in_force": "good_til_cancelled",
  "event_time": "2015-01-10T05:55:38.000Z"
}

      
  Execution Events Channel
  This channel delivers execution-related events. Messages are not re-delivered.

  
    To retrieve missed executions, please use the
    Transaction history
    endpoint in the REST API.
  

  REQUEST ITEMS
  {"type":"subscribe","channels":["execution-events"]}

  RESPONSE ITEMS
  {
  "channel": "execution-events",
  "id": "Order ID (It's the same ID in Transaction history)",
  "order_id": "Order ID",
  "event_time": "Event time",
  "funds": {
    "btc": "Balance change",
    "jpy": "Balance change"
  },
  "pair": "Pair",
  "rate": "Rate",
  "fee_currency": "Fee currency",
  "fee": "Fee amount",
  "liquidity": "'T' (Taker) or 'M' (Maker) or 'itayose'",
  "side": "buy"
}

  RESPONSE EXAMPLE
  {
  "channel": "execution-events",
  "id": 38,
  "order_id": 49,
  "event_time": "2015-11-18T07:02:21.000Z",
  "funds": {
    "btc": "0.1",
    "jpy": "-4096.135"
  },
  "pair": "btc_jpy",
  "rate": "40900.0",
  "fee_currency": "JPY",
  "fee": "6.135",
  "liquidity": "T",
  "side": "buy"
}

      

  
    
      
        Coincheck
        
      
        
          Documents
          
        
      
        Exchange API document
          
      
    
  


        
    
      
        
          
            Language
            
              English
              日本語
            
          
          
            
              
                
                  
                
                
                  
                
              
              Coincheck, Inc.
              Digital Currency ExchangeRegistration Number: Kanto Finance Bureau 00014
              General Incorporated AssociationJVCEA Member
            
            
              PRODUCTS
              
                
                  Buy Bitcoin
                  Exchange
                  Coincheck App
                  Coincheck Periodic Payment Plans
                  Coincheck IEO
                  Coincheck NFT
                  Coincheck Electric
                  Coincheck Gas
                  Coincheck Survey
                  Lending
                  Staking Service(Beta)
                  OTC Trading
                  Coincheck Prime
                  Coincheck Partners
                
              
            
            
              SERVICE GUIDES
              
                
                  Buy Bitcoin
                  Exchange API
                
              
            
            
              SUPPORT
              
                
                  Help Center / Contact
                  Closing prices for supported currencies
                  Fee
                  Fees for NFT Marketplace
                  FAQ article about order number
                  Policy Regarding Disputes and Complaints
                  Notes on prohibited transactions
                  Regarding Unfair Trading
                
              
            
            
              INFO
              
                
                  About Cryptocurrency
                  What is Bitcoin?
                  What is Altcoin?
                  Coincheck Column
                  Cryptocurrency Charts List
                  Trading manual
                  Coincheck Periodic Payment Plans Trading manual
                  Coincheck NFT Trading manual
                  Coincheck Lending transaction manual
                  Coincheck OnRamp transaction manual
                  Outline of Cryptocurrency
                  Listing Examination of New Crypto Assets
                  
                    X | @coincheckjp
                    Facebook | Official Page
                  
                
              
            
            
              ABOUT
              
                
                  About
                  Current campaigns
                  Jobs
                  Terms of use
                  Coincheck Periodic Payment Plans Terms of service
                  Coincheck NFT Terms of service
                  Cryptographic asset loan agreement
                  Terms of lending service
                  Legal
                  Privacy Policy
                  External Transmission
                  System Risk Management Policy
                  Information Security Policy
                  Fundamental Policies Against Organized Crime
                  Money Laundering Prevention
                  Company response guidelines for planned Hard Forks and new coins
                  Policy on the performance of obligations
                  Best Practice Policy
                  Countervailing interests management policy
                  Solicitation Policy
                  Site policy
                
              
            
          
        
      
    
  

    
  




  





