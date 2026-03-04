Get Started
Build on Gemini

Copy page

AI/LLM users: Fetch the complete documentation index at docs.gemini.com/llms.txt

Gemini is a regulated cryptocurrency exchange and prediction market trusted by millions of users and institutions worldwide. Our developer platform gives you secure, reliable access to crypto markets through REST APIs, WebSocket APIs, and FIX connections.

What you can build
Trading applications — Execute orders and manage portfolios
Market data tools — Access real-time prices and order books
Portfolio trackers — Monitor balances and transaction history
Prediction market bots — Trade event contracts programmatically
Enterprise solutions — Integrate crypto into your business
APIs
Get market data
Public REST APIs provide:

Current order book
Recent trading activity
Trade history
Manage accounts
Private REST APIs enable:

Place and cancel orders
View active orders
Check trading history and volume
Review available balances
Trade prediction markets
Prediction Markets API supports:

Browse events and contracts
Place and cancel limit orders
Track positions and order history
Sandbox

Copy page

Gemini's sandbox site is an instance of the Gemini Exchange that offers full exchange functionality using test funds.

Gemini has an automated system that makes trades on the exchange to simulate normal exchange activity
all funds are for testing purposes. Only Testnet BTC deposits and withdrawals are supported.
Sandbox URLs
Website

https://exchange.sandbox.gemini.com

REST API

https://api.sandbox.gemini.com

WebSocket Feed

wss://api.sandbox.gemini.com

Documentation

https://docs.sandbox.gemini.com

Create your account
Go to the sandbox site to register for a test account to begin trading.

use the website to get comfortable trading on Gemini
use the API to validate your trading systems before deploying them against the real Gemini exchange
Your account will automatically be credited with USD, BTC, ETH, BCH, LTC, OXT, LINK, BAT and DAI. You may use these funds to trade, both through the web site and through the API.

Gemini's sandbox site does not support either depositing or withdrawing your test funds, which can only be used to trade on the sandbox exchange.

Sandbox does not support email notifications. If you need this as part of your testing plan, please contact trading@gemini.com.

If you have any issues, or if you need to adjust your balances (to test insufficient funds handling, for example), contact trading@gemini.com.

Two Factor Authentication
Two factor authentication ("2FA") is enabled by default for all sandbox accounts. To disable 2FA for automated testing, please do the following:

At the Authy 2FA entry screen, set a cookie or an HTTP header with the name GEMINI-SANDBOX-2FA. The value doesn’t matter.
Enter 9999999 as your 2FA code



PI Key

Copy page

Private API invocation
Payload creation
Authentication
Gemini uses API keys to allow access to private APIs. You can obtain these by logging on and creating a key in Settings/API. This will give you both an "API Key" that will serve as your user name, and an "API Secret" that you will use to sign messages.

All requests must contain a nonce. When provisioning a session key, you have the option of selecting "Uses a time based nonce". If this option is selected, the nonce, which must be in seconds, has to be within +/- 30 seconds of Unix Epoch timestamp to be deemed valid.

If you do not choose the option of a time based nonce, then the nonce has to be a number that will never be repeated and must increase between requests. This is to prevent an attacker who has captured a previous request from simply replaying that request. We recommend using a timestamp at millisecond or higher precision. The nonce need only be increasing with respect to the session that the message is on.

Sessions
A single account may have multiple API keys provisioned. In this document, we'll refer to these as "sessions". All orders will be recorded with the session that created them. The nonce associated with a request needs to be increasing with respect to the session that the nonce is used on.

This allows multithreaded or distributed trading systems to place orders independently of each other, without needing to synchronize clocks to avoid race conditions.

In addition, some operations (such as Cancel All Session Orders) act on the orders associated with a specific session.

Require Heartbeat
When provisioning a session key you have the option of marking the session as "Requires Heartbeat". The intention here is to specify that if connectivity to the exchange is lost for any reason, then all outstanding orders on this session should be canceled.

If this option is selected for a session, then if the exchange does not receive a message for 30 seconds, then it will assume there has been an interruption in service, and cancel all outstanding orders. To maintain the session, the trading system should send a heartbeat message at a more frequent interval. We suggest at most 15 seconds between heartbeats.

The heartbeat message is provided for convenience when there is no trading activity. Any authenticated API call will reset the 30 second clock, even if explicit heartbeats are not sent.

This feature is often referred to as "Cancel on Disconnect" on connection-oriented exchange protocols.

Payload
The payload of the requests will be a JSON object, which will be described in the documentation below. Rather than being sent as the body of the POST request, it will be base-64 encoded and stored as a header in the request.

Authenticated APIs do not submit their payload as POSTed data, but instead put it in the X-GEMINI-PAYLOAD header.
All of them will include the request name and the nonce associated with the request.

Header	Value
Content-Length	0
Content-Type	text/plain
X-GEMINI-APIKEY	Your Gemini API key
X-GEMINI-PAYLOAD	The base64-encoded JSON payload
X-GEMINI-SIGNATURE	hex(HMAC_SHA384(base64(payload), key=api_secret))
Cache-Control	no-cache
Master API Key
A group that contains multiple accounts can provision a Master API key. Master API keys offer the convenience of invoking any account API on behalf of an account within that group. To invoke an API on behalf of an account, add that account's nickname as an account parameter to your request payload.

Master API keys are formatted with a prepending master-, while account level API keys are formatted with a prepending account-.

The account parameter may be used on any API that performs an action for or against a single account.

Generating payload and signature header examples
cURL
Code

# Create a proper payload with a single nonce value
NONCE=$(date +%s.%N)
PAYLOAD=$(echo -n "{\"request\":\"/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z\",\"nonce\":$NONCE}" | base64 | tr -d '\n')
SIGNATURE=$(echo -n "$PAYLOAD" | openssl dgst -sha384 -hmac "GEMINI_API_SECRET" | cut -d ' ' -f2)
# Execute the command with the calculated values
curl -X GET "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z" \
  -H "Content-Type: text/plain" \
  -H "Content-Length: 0" \
  -H "X-GEMINI-APIKEY: GEMINI_API_KEY" \
  -H "X-GEMINI-PAYLOAD: $PAYLOAD" \
  -H "X-GEMINI-SIGNATURE: $SIGNATURE" \
  -H "Cache-Control: no-cache"
Python
Code

import json
import base64
import hmac
import hashlib
import time
url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
gemini_api_secret = "GEMINI_API_SECRET".encode()
gemini_api_key= "GEMINI_API_KEY"
payload_nonce = time.time()
# Extract path from URL
_, path = url.split(".com")
# Create payload object
payload =  {"request": path, "nonce": payload_nonce}
# Convert payload to JSON string
encoded_payload = json.dumps(payload).encode()
# Base64 encode the payload
b64 = base64.b64encode(encoded_payload)
# Create HMAC signature using SHA-384
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()
# Headers
request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
}
print(request_headers)
Javascript
Code

const crypto = require('crypto');
const url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
const geminiAPISecret = Buffer.from("GEMINI_API_SECRET");
const geminiAPIKey = "GEMINI_API_KEY";
const payloadNonce = Date.now() / 1000;
// Extract path from URL
const [_, path] = url.split(".com");
// Create payload object
const payload = {
  request: path,
  nonce: payloadNonce
};
// Convert payload to JSON string
const encodedPayload = JSON.stringify(payload);
// Base64 encode the payload
const b64 = Buffer.from(encodedPayload).toString('base64');
// Create HMAC signature using SHA-384
const signature = crypto.createHmac('sha384', geminiAPISecret)
  .update(b64)
  .digest('hex');
// Headers
const requestHeaders = {
  'Content-Type': "text/plain",
  'Content-Length': "0",
  'X-GEMINI-APIKEY': geminiAPIKey,
  'X-GEMINI-PAYLOAD': b64,
  'X-GEMINI-SIGNATURE': signature,
  'Cache-Control': "no-cache"
};
console.log(requestHeaders);
C#
Code

using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
class Program
{
    static void Main()
    {
        string url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
        byte[] gemini_api_secret = Encoding.UTF8.GetBytes("GEMINI_API_SECRET");
        string gemini_api_key = "GEMINI_API_KEY";
        double payload_nonce = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds() / 1000.0;
        // Extract path from URL
        string path = url.Split(new[] { ".com" }, StringSplitOptions.None)[1];
        // Create payload object
        var payload = new Dictionary<string, object>
        {
            { "request", path },
            { "nonce", payload_nonce }
        };
        // Convert payload to JSON string
        string jsonPayload = JsonSerializer.Serialize(payload);
        byte[] encodedPayload = Encoding.UTF8.GetBytes(jsonPayload);
        // Base64 encode the payload
        string b64 = Convert.ToBase64String(encodedPayload);
        // Create HMAC signature using SHA-384
        using (var hmac = new HMACSHA384(gemini_api_secret))
        {
            byte[] signatureBytes = hmac.ComputeHash(Encoding.UTF8.GetBytes(b64));
            string signature = BitConverter.ToString(signatureBytes).Replace("-", "").ToLower();
            // Headers
            var request_headers = new Dictionary<string, string>
            {
                { "Content-Type", "text/plain" },
                { "Content-Length", "0" },
                { "X-GEMINI-APIKEY", gemini_api_key },
                { "X-GEMINI-PAYLOAD", b64 },
                { "X-GEMINI-SIGNATURE", signature },
                { "Cache-Control", "no-cache" }
            };
            Console.WriteLine(string.Join("\n", request_headers));
        }
    }
}
Kotlin
Code

import java.util.*
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import java.nio.charset.StandardCharsets
import kotlinx.serialization.json.*
fun main() {
    val url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
    val gemini_api_secret = "GEMINI_API_SECRET".toByteArray(StandardCharsets.UTF_8)
    val gemini_api_key = "GEMINI_API_KEY"
    val payload_nonce = System.currentTimeMillis() / 1000.0
    // Extract path from URL
    val path = url.split(".com")[1]
    // Create payload object
    val payload = buildJsonObject {
        put("request", JsonPrimitive(path))
        put("nonce", JsonPrimitive(payload_nonce))
    }
    // Convert payload to JSON string
    val encodedPayload = payload.toString().toByteArray(StandardCharsets.UTF_8)
    // Base64 encode the payload
    val b64 = Base64.getEncoder().encodeToString(encodedPayload)
    // Create HMAC signature using SHA-384
    val mac = Mac.getInstance("HmacSHA384")
    val secretKeySpec = SecretKeySpec(gemini_api_secret, "HmacSHA384")
    mac.init(secretKeySpec)
    val signatureBytes = mac.doFinal(b64.toByteArray(StandardCharsets.UTF_8))
    val signature = signatureBytes.joinToString("") { "%02x".format(it) }
    // Headers
    val request_headers = mapOf(
        "Content-Type" to "text/plain",
        "Content-Length" to "0",
        "X-GEMINI-APIKEY" to gemini_api_key,
        "X-GEMINI-PAYLOAD" to b64,
        "X-GEMINI-SIGNATURE" to signature,
        "Cache-Control" to "no-cache"
    )
    println(request_headers)
}
Objective-C
Code

#import <Foundation/Foundation.h>
#import <CommonCrypto/CommonHMAC.h>
@interface NSData (HexString)
- (NSString *)hexString;
@end
@implementation NSData (HexString)
- (NSString *)hexString {
    const unsigned char *bytes = (const unsigned char *)[self bytes];
    NSMutableString *hex = [NSMutableString new];
    
    for (NSInteger i = 0; i < [self length]; i++) {
        [hex appendFormat:@"%02x", bytes[i]];
    }
    return hex;
}
@end
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSString *url = @"https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
        NSString *gemini_api_secret_str = @"GEMINI_API_SECRET";
        NSData *gemini_api_secret = [gemini_api_secret_str dataUsingEncoding:NSUTF8StringEncoding];
        NSString *gemini_api_key = @"GEMINI_API_KEY";
        NSTimeInterval payload_nonce = [[NSDate date] timeIntervalSince1970];
        
        // Extract path from URL
        NSArray *components = [url componentsSeparatedByString:@".com"];
        NSString *path = components[1];
        
        // Create payload object
        NSDictionary *payload = @{
            @"request": path,
            @"nonce": @(payload_nonce)
        };
        
        // Convert payload to JSON string
        NSError *error;
        NSData *encodedPayload = [NSJSONSerialization dataWithJSONObject:payload
                                                                 options:0
                                                                   error:&error];
        
        // Base64 encode the payload
        NSString *b64 = [encodedPayload base64EncodedStringWithOptions:0];
        
        // Create HMAC signature using SHA-384
        NSData *b64Data = [b64 dataUsingEncoding:NSUTF8StringEncoding];
        unsigned char hmac[CC_SHA384_DIGEST_LENGTH];
        
        CCHmac(kCCHmacAlgSHA384, 
               [gemini_api_secret bytes], 
               [gemini_api_secret length], 
               [b64Data bytes], 
               [b64Data length], 
               hmac);
        
        NSData *signatureData = [NSData dataWithBytes:hmac length:sizeof(hmac)];
        NSString *signature = [signatureData hexString];
        
        // Headers
        NSDictionary *request_headers = @{
            @"Content-Type": @"text/plain",
            @"Content-Length": @"0",
            @"X-GEMINI-APIKEY": gemini_api_key,
            @"X-GEMINI-PAYLOAD": b64,
            @"X-GEMINI-SIGNATURE": signature,
            @"Cache-Control": @"no-cache"
        };
        
        NSLog(@"%@", request_headers);
    }
    return 0;
}
PHP
Code

<?php
$url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
$gemini_api_secret = "GEMINI_API_SECRET";
$gemini_api_key = "GEMINI_API_KEY";
$payload_nonce = microtime(true);
// Extract path from URL
$parts = explode(".com", $url);
$path = $parts[1];
// Create payload object
$payload = [
    "request" => $path,
    "nonce" => $payload_nonce
];
// Convert payload to JSON string
$encoded_payload = json_encode($payload);
// Base64 encode the payload
$b64 = base64_encode($encoded_payload);
// Create HMAC signature using SHA-384
$signature = hash_hmac('sha384', $b64, $gemini_api_secret);
// Headers
$request_headers = [
    'Content-Type' => "text/plain",
    'Content-Length' => "0",
    'X-GEMINI-APIKEY' => $gemini_api_key,
    'X-GEMINI-PAYLOAD' => $b64,
    'X-GEMINI-SIGNATURE' => $signature,
    'Cache-Control' => "no-cache"
];
print_r($request_headers);
?>
Ruby
Code

require 'json'
require 'base64'
require 'openssl'
require 'time'
url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
gemini_api_secret = "GEMINI_API_SECRET"
gemini_api_key = "GEMINI_API_KEY"
payload_nonce = Time.now.to_f
# Extract path from URL
_, path = url.split(".com")
# Create payload object
payload = {"request" => path, "nonce" => payload_nonce}
# Convert payload to JSON string
encoded_payload = JSON.generate(payload)
# Base64 encode the payload
b64 = Base64.strict_encode64(encoded_payload)
# Create HMAC signature using SHA-384
signature = OpenSSL::HMAC.hexdigest('sha384', gemini_api_secret, b64)
# Headers
request_headers = {
  'Content-Type' => "text/plain",
  'Content-Length' => "0",
  'X-GEMINI-APIKEY' => gemini_api_key,
  'X-GEMINI-PAYLOAD' => b64,
  'X-GEMINI-SIGNATURE' => signature,
  'Cache-Control' => "no-cache"
}
puts request_headers
Swift
Code

import Foundation
import CommonCrypto
let url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
let gemini_api_secret = "GEMINI_API_SECRET".data(using: .utf8)!
let gemini_api_key = "GEMINI_API_KEY"
let payload_nonce = Date().timeIntervalSince1970
// Extract path from URL
let components = url.components(separatedBy: ".com")
let path = components[1]
// Create payload object
let payload: [String: Any] = ["request": path, "nonce": payload_nonce]
// Convert payload to JSON string
let jsonData = try! JSONSerialization.data(withJSONObject: payload, options: [])
// Base64 encode the payload
let b64 = jsonData.base64EncodedString()
// Create HMAC signature using SHA-384
let signature = b64.data(using: .utf8)!.withUnsafeBytes { b64Ptr in
    gemini_api_secret.withUnsafeBytes { secretPtr in
        var digest = [UInt8](repeating: 0, count: Int(CC_SHA384_DIGEST_LENGTH))
        CCHmac(CCHmacAlgorithm(kCCHmacAlgSHA384), secretPtr.baseAddress!, gemini_api_secret.count, b64Ptr.baseAddress!, b64.count, &digest)
        return digest.map { String(format: "%02x", $0) }.joined()
    }
}
// Headers
let request_headers = [
    "Content-Type": "text/plain",
    "Content-Length": "0",
    "X-GEMINI-APIKEY": gemini_api_key,
    "X-GEMINI-PAYLOAD": b64,
    "X-GEMINI-SIGNATURE": signature,
    "Cache-Control": "no-cache"
]
print(request_headers)
Go
Code

package main
import (
	"crypto/hmac"
	"crypto/sha512"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"strings"
	"time"
)
func main() {
	url := "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
	gemini_api_secret := []byte("GEMINI_API_SECRET")
	gemini_api_key := "GEMINI_API_KEY"
	payload_nonce := float64(time.Now().UnixNano()) / 1e9
	// Extract path from URL
	parts := strings.Split(url, ".com")
	path := parts[1]
	// Create payload object
	payload := map[string]interface{}{
		"request": path,
		"nonce":   payload_nonce,
	}
	// Convert payload to JSON string
	jsonPayload, _ := json.Marshal(payload)
	// Base64 encode the payload
	b64 := base64.StdEncoding.EncodeToString(jsonPayload)
	// Create HMAC signature using SHA-384
	h := hmac.New(sha512.New384, gemini_api_secret)
	h.Write([]byte(b64))
	signature := hex.EncodeToString(h.Sum(nil))
	// Headers
	request_headers := map[string]string{
		"Content-Type":       "text/plain",
		"Content-Length":     "0",
		"X-GEMINI-APIKEY":    gemini_api_key,
		"X-GEMINI-PAYLOAD":   b64,
		"X-GEMINI-SIGNATURE": signature,
		"Cache-Control":      "no-cache",
	}
	fmt.Println(request_headers)
}
Java
Code

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import org.json.JSONObject;
public class GeminiAPI {
    public static void main(String[] args) throws Exception {
        String url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
        String gemini_api_secret = "GEMINI_API_SECRET";
        String gemini_api_key = "GEMINI_API_KEY";
        double payload_nonce = Instant.now().toEpochMilli() / 1000.0;
        // Extract path from URL
        String path = url.split("\\.com")[1];
        // Create payload object
        Map<String, Object> payload = new HashMap<>();
        payload.put("request", path);
        payload.put("nonce", payload_nonce);
        // Convert payload to JSON string
        JSONObject jsonPayload = new JSONObject(payload);
        String payloadString = jsonPayload.toString();
        byte[] encodedPayload = payloadString.getBytes(StandardCharsets.UTF_8);
        // Base64 encode the payload
        String b64 = Base64.getEncoder().encodeToString(encodedPayload);
        // Create HMAC signature using SHA-384
        Mac sha384HMAC = Mac.getInstance("HmacSHA384");
        SecretKeySpec secretKeySpec = new SecretKeySpec(
            gemini_api_secret.getBytes(StandardCharsets.UTF_8), "HmacSHA384");
        sha384HMAC.init(secretKeySpec);
        byte[] signatureBytes = sha384HMAC.doFinal(b64.getBytes(StandardCharsets.UTF_8));
        StringBuilder signature = new StringBuilder();
        for (byte b : signatureBytes) {
            signature.append(String.format("%02x", b));
        }
        // Headers
        Map<String, String> request_headers = new HashMap<>();
        request_headers.put("Content-Type", "text/plain");
        request_headers.put("Content-Length", "0");
        request_headers.put("X-GEMINI-APIKEY", gemini_api_key);
        request_headers.put("X-GEMINI-PAYLOAD", b64);
        request_headers.put("X-GEMINI-SIGNATURE", signature.toString());
        request_headers.put("Cache-Control", "no-cache");
        System.out.println(request_headers);
    }
}
Rust
Code

use std::time::{SystemTime, UNIX_EPOCH};
use hmac::{Hmac, Mac};
use sha2::Sha384;
use base64::encode;
use serde_json::{json, to_string};
use std::collections::HashMap;
fn main() {
    let url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z";
    let gemini_api_secret = b"GEMINI_API_SECRET";
    let gemini_api_key = "GEMINI_API_KEY";
    let payload_nonce = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64();
    // Extract path from URL
    let path = url.split(".com").nth(1).unwrap();
    // Create payload object
    let payload = json!({
        "request": path,
        "nonce": payload_nonce
    });
    // Convert payload to JSON string
    let encoded_payload = to_string(&payload).unwrap();
    
    // Base64 encode the payload
    let b64 = encode(encoded_payload.as_bytes());
    // Create HMAC signature using SHA-384
    type HmacSha384 = Hmac<Sha384>;
    let mut mac = HmacSha384::new_from_slice(gemini_api_secret).unwrap();
    mac.update(b64.as_bytes());
    let signature_bytes = mac.finalize().into_bytes();
    let signature = signature_bytes.iter()
        .map(|b| format!("{:02x}", b))
        .collect::<String>();
    // Headers
    let mut request_headers = HashMap::new();
    request_headers.insert("Content-Type", "text/plain");
    request_headers.insert("Content-Length", "0");
    request_headers.insert("X-GEMINI-APIKEY", gemini_api_key);
    request_headers.insert("X-GEMINI-PAYLOAD", &b64);
    request_headers.insert("X-GEMINI-SIGNATURE", &signature);
    request_headers.insert("Cache-Control", "no-cache");
    println!("{:?}", request_headers);
}
Scala
Code

import java.util.Base64
import java.nio.charset.StandardCharsets
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import scala.collection.mutable.Map
import play.api.libs.json._
object GeminiAPI {
  def main(args: Array[String]): Unit = {
    val url = "https://api.gemini.com/v2/fxrate/EURUSD/2025-04-16T23:07:27.189Z"
    val gemini_api_secret = "GEMINI_API_SECRET".getBytes(StandardCharsets.UTF_8)
    val gemini_api_key = "GEMINI_API_KEY"
    val payload_nonce = System.currentTimeMillis() / 1000.0
    // Extract path from URL
    val parts = url.split("\\.com")
    val path = parts(1)
    // Create payload object
    val payload = Json.obj(
      "request" -> path,
      "nonce" -> payload_nonce
    )
    // Convert payload to JSON string
    val encodedPayload = Json.stringify(payload).getBytes(StandardCharsets.UTF_8)
    // Base64 encode the payload
    val b64 = Base64.getEncoder.encodeToString(encodedPayload)
    // Create HMAC signature using SHA-384
    val mac = Mac.getInstance("HmacSHA384")
    val secretKeySpec = new SecretKeySpec(gemini_api_secret, "HmacSHA384")
    mac.init(secretKeySpec)
    val signatureBytes = mac.doFinal(b64.getBytes(StandardCharsets.UTF_8))
    val signature = signatureBytes.map("%02x".format(_)).mkString
    // Headers
    val request_headers = Map[String, String](
      "Content-Type" -> "text/plain",
      "Content-Length" -> "0",
      "X-GEMINI-APIKEY" -> gemini_api_key,
      "X-GEMINI-PAYLOAD" -> b64,
      "X-GEMINI-SIGNATURE" -> signature,
      "Cache-Control" -> "no-cache"
    )
    println(request_headers)
  }
}

OAuth 2.0

Copy page

In addition to the API key methods described in private APIs, Gemini supports OAuth 2.0 flows and adheres to the OAuth 2.0 Standards. Both authorization code and implicit OAuth flows are supported, however use of authorization code flows is strongly recommended for most use cases because of enhanced security and the ability to support features such as refresh tokens.

The first step in using Gemini OAuth is to create a new OAuth application which you can do via API Settings. You will be asked for some basic information including a name, description, background information, logo, and the scopes that you are requesting access to. We will provide you a client_id and a client_secret which are used to identify and secure your app.

Once your app is registered it will be reviewed by Gemini, and then set live for use. You may also follow the same process in our Sandbox Environment to build a test integration.

Please email trading@gemini.com with any questions. We will provide you a client_id and a client_secret. Your client_id will be used in all your requests to identify your app, and client_secret must be sent in all POST requests

Instead of API Keys OAuth 2.0 uses access tokens and, if using the authorization code grant flow, refresh tokens. Access tokens are short-lived (24 hour expiration) and are used in Gemini API calls while refresh tokens don't expire and are used solely to generate new access tokens.

Authorization Code Grant Flow
The OAuth 2.0 authorization code grant flow involves the user being directed to an authorization server which returns an authorization code that may then be exchanged for access and refresh tokens. Access tokens are short-lived (24 hour expiration) and are used as authentication against Gemini APIs, while refresh tokens never expire and are used to regenerate access tokens.

Authorization Request
Users should first be redirected to Gemini to authorize access to your application. The user will be prompted to login using a Gemini OAuth window.

GET https://exchange.gemini.com/auth

Example authorization request:

GET https://exchange.gemini.com/auth?client_id=my_id&response_type=code&redirect_uri=www.example.com/redirect&state=82350325&scope=balances:read,orders:create

URL Parameters
Parameter	Type	Description
client_id	string	Unique id of your application. This is provided in your API settings
response_type	string	The literal string "code"
redirect_uri	string	The URL users should be returned to when they authorize. Note, this URL must be included in your list of approved redirect_uris in your app registration
state	string	A random string that will be returned to you in the response.
scope	string	A comma separated list of scopes corresponding to the access you're requesting for your application. Note, these scopes must be included in your list of scopes in your app registration
Authorization Response
Example redirect_uri response after user login

https://www.example.com/redirect?code=90123465-86ee-44ef-b4e3-835cc89bc8a3&state=82350325

On successful authorization Gemini will redirect your user to the redirect_uri you supplied with additional parameters code and state. The parameter state should match the state you provided, otherwise you should not trust the response. code is a temporary code which you will then use to obtain access and refresh tokens.

Authorization Token Request
Once you have received a code you can exchange it for access and refresh tokens.

POST https://exchange.gemini.com/auth/token

Parameter	Type	Description
client_id	string	Unique id of your application. This is provided in your API settings
client_secret	string	Secret of your application. This is provided when you first register an app in API settings
code	string	The code you received from the authorization request
redirect_uri	string	This must match the redirect_uri provided in the authorization request
grant_type	string	The literal string "authorization_code"
Example Token Request

Code

{
    "client_id": "my_id",
    "client_secret": "my_secret",
    "code": "90123465-86ee-44ef-b4e3-835cc89bc8a3",
    "redirect_uri": "www.example.com/redirect",
    "grant_type": "authorization_code"
}
Authorization Token Response
Field	Type	Description
access_token	string	A short-lived token to use in API call authentication. Is valid until the expires_in time reaches 0
refresh_token	string	A refresh token to be used to generate new access tokens
token_type	string	The literal string "bearer"
scope	string	The scopes the access token will have access to
expires_in	integer	The lifetime in seconds of the access token, as measured in seconds from the current time
Example Token Response

Code

{
    "access_token": "d9af2411-3e85-41bb-89f4-cf53750f04df",
    "refresh_token": "215c5a89-6df7-457b-ba0b-70695da8c91f",
    "token_type": "Bearer",
    "scope": "balances:read,orders:create",
    "expires_in": 86399
}
Using Refresh Tokens
The access token you receive will be relatively short-lived (default 24 hours). Once an access token has expired you can use your refresh token to generate a new access token. Refresh tokens never expire, however they are one-time use only as your request for a new access token will also return a new refresh token.

Getting a new access token is similar to getting the initial access and refresh tokens with slightly different parameters

Refresh Token Request
POST https://exchange.gemini.com/auth/token

Example Token Request

Code

{
    "client_id": "my_id",
    "client_secret": "my_secret",
    "refresh_token": "215c5a89-6df7-457b-ba0b-70695da8c91f",
    "grant_type":"refresh_token"
}
Parameter	Type	Description
client_id	string	Unique id of your application
client_secret	string	Secret of your application. This is provided when you first register an app in API settings
refresh_token	string	Your refresh token
grant_type	string	The literal string "refresh_token"
Refresh Token Response
The response is the same as the initial token response – it will contain a new access token to query APIs and a new refresh token for when the access token expires.

Parameter	Type	Description
access_token	string	A short-lived token to use in API call authentication
refresh_token	string	A refresh token to be used to generate new access tokens
token_type	string	The literal string "bearer"
scope	string	The scopes the access token will have access to
expires_in	integer	The lifetime in seconds of the access token, as measured in seconds from the current time
Example Token Response

Code

{
  "access_token": "c5e9459d-dc6f-4567-bce4-050ec965f22e",
  "expires_in": 86399,
  "scope": "balances:read,orders:create",
  "refresh_token": "ce0f14af-74dd-4767-a4e7-286e98b944c1",
  "token_type": "Bearer"
}
Implicit Grant Flow
In addition to the authorization code flow, Gemini also supports the OAuth 2.0 implicit grant flow. This is a simplified version of the authorization code flow and is not recommended for most applications. This OAuth flow is not available by default, please reach out to trading@gemini.com to request access to the implicit grant flow.

When the access_token expires you must request a new one using either the implicit flow or authorization code flow.

Send request to following URL with URL parameters

GET https://exchange.gemini.com/auth

First direct users to Gemini like the example below

GET https://exchange.gemini.com/auth?response_type=token&client_id=my_id&redirect_uri=https://example.com/redirect?scope=Trader&state=7j87

URL Parameters
Parameter	Type	Description
response_type	string	The literal string "token"
client_id	string	Unique id of your application. This is provided in your API settings
redirect_uri	string	The URL users should be returned to when they authorize. Note, this URL must be included in your list of approved redirect_uris in your app registration
state	string	A random string that will be returned to you in the response.
scope	string	A comma separated list of scopes corresponding to the access you're requesting for your application. Note, these scopes must be included in your list of scopes in your app registration
Users will then be sent to Gemini login with their credentials. Once they do they will be sent to the redirect_uri provided.

Authorization Response (URL Parameters)
Example redirect_uri response after user login

https://example.com/redirect#access_token=3b7661f0-f156-498a-ad17-0fa4025ec907&state=7j87&token_type=bearer&scope=Trader&expires_in=83534

On successful authorization Gemini will redirect your user to the redirect_uri you supplied with additional parameters code and state. The parameter state should match the state you provided, otherwise you should not trust the response. access_token is the access token which you will use to make API calls on behalf of the user.

Field	Type	Description
access_token	string	A short-lived token to use in API call authentication. Is valid until the expires_in time reaches 0
token_type	string	The literal string "bearer"
scope	string	The scopes the access token will have access to
expires_in	integer	The lifetime in seconds of the access token, as measured in seconds from the current time
Using Access Tokens
Once you have an access token you can use it to call any Gemini API.

Most of the examples for the private APIs in these docs make use of API keys and corresponding headers, to use an access token simply update your header:

Header	Description
Authorization	The literal string "Bearer " concatenated to your temporary access_token
X-GEMINI-PAYLOAD	The base64-encoded JSON payload (the payloads on OAuth do not require a nonce)
Code

import requests
import json
import base64
url = "https://api.gemini.com/v1/mytrades"
access_token = "Bearer d9af2411-3e85-41bb-89f4-cf53750f04df"
payload = {
    "request": "/v1/mytrades",
    "symbol": "btcusd"
}
encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
request_headers = { 
    "Authorization": access_token,
    "X-GEMINI-PAYLOAD": b64
}
response = requests.post(url,
                        data=None,
                        headers=request_headers,
                        verify=False)
my_trades = response.json()
Code

import requests
import json
import base64
url = "https://api.gemini.com/v1/orders/history"
access_token = "Bearer d9af2411-3e85-41bb-89f4-cf53750f04df"
payload = {
    "request": "/v1/orders/history",
    "symbol": "btcusd"
}
encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
request_headers = { 
    "Authorization": access_token,
    "X-GEMINI-PAYLOAD": b64
}
response = requests.post(url,
                        data=None,
                        headers=request_headers,
                        verify=False)
my_orders = response.json()
OAuth Scopes
Gemini uses a role-based system for its API. All OAuth applications are limited to the scopes in the following chart:

Endpoint	URI	Scope
Get Deposit Addresses	/v1/addresses/:network	addresses:read, addresses:create
New Deposit Address	/v1/deposit/:network/newAddress	addresses:create
List Approved Addresses	/v1/approvedAddresses/account/:network	addresses:read
Remove Approved Address	/v1/approvedAddresses/:network/remove	addresses:create
Get Available Balances	/v1/balances	balances:read
Get Notional Balances	v1/notionalbalances/:currency	balances:read
Add A Bank	/v1/payments/addbank	banks:create
Add A Bank CAD	/v1/payments/addbank/cad	banks:create
View Payment Methods	/v1/payments/methods	banks:read, banks:create
New Clearing Order	/v1/clearing/new	clearing:create
Cancel Clearing Order	/v1/clearing/cancel	clearing:create
Confirm Clearing Order	/v1/clearing/confirm	clearing:create
Clearing Order Status	/v1/clearing/status	clearing:read
Clearing Order List	/v1/clearing/list	clearing:read
Clearing Broker List	/v1/clearing/broker/list	clearing:read
Clearing Trades	/v1/clearing/trades	clearing:read
Withdraw Crypto Funds	/v1/withdraw/:currency	crypto:send
List Past Trades	/v1/mytrades	history:read
Get Orders History	/v1/orders/history	history:read
Get Notional Volume	/v1/notionalvolume	history:read
Get Trade Volume	/v1/tradevolume	history:read
Transfers	/v1/transfers	history:read
Custody Account Fees	/v1/custodyaccountfees	history:read
Create New Order	/v1/order/new	orders:create
Cancel Order	/v1/order/cancel	orders:create
Cancel All Session Orders	/v1/order/cancel/session	orders:create
Cancel All Active Orders	/v1/order/cancel/all	orders:create
Wrap Order	/v1/wrap/:symbol	orders:create
Get Instant Quote	/v1/instant/quote	orders:create
Execute Instant Order	/v1/instant/execute	orders:create
Get Order Status	/v1/order/status	orders:read
Get Active Orders	/v1/orders	orders:read
Account Detail	/v1/account	account:read
API keys use different roles for to access Gemini APIs. Please see roles for descriptions of each role and scope for API keys.

Revoke OAuth Token
See Revoke OAuth Token Endpoint

Revision History
Date	Notes
2020/08/20	Initial OAuth documentation


Symbols and minimums

Copy page

Available Trading Symbols (Live from API)
Filter symbols...
Sort A→Z
↓
Symbol	Minimum Order Size	Tick Size	Quote Currency Price Increment
2zgusd	0.2 2Z (2e-1)	0.000001 2Z (1e-6)	0.000001 GUSD
2zrlusd	0.2 2Z (2e-1)	0.000001 2Z (1e-6)	0.000001 RLUSD
2zusd	0.2 2Z (2e-1)	0.000001 2Z (1e-6)	0.000001 USD
2zusdc	0.2 2Z (2e-1)	0.000001 2Z (1e-6)	0.000001 USDC
aavegusd	0.001 AAVE (1e-3)	0.000001 AAVE (1e-6)	0.0001 GUSD
aaverlusd	0.001 AAVE (1e-3)	0.000001 AAVE (1e-6)	0.0001 RLUSD
aaveusd	0.001 AAVE (1e-3)	0.000001 AAVE (1e-6)	0.0001 USD
aaveusdc	0.001 AAVE (1e-3)	0.000001 AAVE (1e-6)	0.0001 USDC
aligusd	2 ALI (2e+0)	0.000001 ALI (1e-6)	0.000001 GUSD
alirlusd	2 ALI (2e+0)	0.000001 ALI (1e-6)	0.000001 RLUSD
aliusd	2 ALI (2e+0)	0.000001 ALI (1e-6)	0.000001 USD
aliusdc	2 ALI (2e+0)	0.000001 ALI (1e-6)	0.000001 USDC
ampgusd	10 AMP (1e+1)	0.000001 AMP (1e-6)	0.00001 GUSD
amprlusd	10 AMP (1e+1)	0.000001 AMP (1e-6)	0.00001 RLUSD
ampusd	10 AMP (1e+1)	0.000001 AMP (1e-6)	0.00001 USD
ampusdc	10 AMP (1e+1)	0.000001 AMP (1e-6)	0.00001 USDC
ankrgusd	0.1 ANKR (1e-1)	0.000001 ANKR (1e-6)	0.000001 GUSD
ankrrlusd	0.1 ANKR (1e-1)	0.000001 ANKR (1e-6)	0.000001 RLUSD
ankrusd	0.1 ANKR (1e-1)	0.000001 ANKR (1e-6)	0.000001 USD
ankrusdc	0.1 ANKR (1e-1)	0.000001 ANKR (1e-6)	0.000001 USDC
apegusd	0.02 APE (2e-2)	0.000001 APE (1e-6)	0.0001 GUSD
aperlusd	0.02 APE (2e-2)	0.000001 APE (1e-6)	0.0001 RLUSD
apeusd	0.02 APE (2e-2)	0.000001 APE (1e-6)	0.0001 USD
apeusdc	0.02 APE (2e-2)	0.000001 APE (1e-6)	0.0001 USDC
api3gusd	0.03 API3 (3e-2)	0.000001 API3 (1e-6)	0.001 GUSD
api3rlusd	0.03 API3 (3e-2)	0.000001 API3 (1e-6)	0.001 RLUSD
api3usd	0.03 API3 (3e-2)	0.000001 API3 (1e-6)	0.001 USD
api3usdc	0.03 API3 (3e-2)	0.000001 API3 (1e-6)	0.001 USDC
arbgusd	0.2 ARB (2e-1)	0.01 ARB (1e-2)	0.0001 GUSD
arbrlusd	0.2 ARB (2e-1)	0.01 ARB (1e-2)	0.0001 RLUSD
arbusd	0.2 ARB (2e-1)	0.01 ARB (1e-2)	0.0001 USD
arbusdc	0.2 ARB (2e-1)	0.01 ARB (1e-2)	0.0001 USDC
atomgusd	0.01 ATOM (1e-2)	0.000001 ATOM (1e-6)	0.001 GUSD
atomrlusd	0.01 ATOM (1e-2)	0.000001 ATOM (1e-6)	0.001 RLUSD
atomusd	0.01 ATOM (1e-2)	0.000001 ATOM (1e-6)	0.001 USD
atomusdc	0.01 ATOM (1e-2)	0.000001 ATOM (1e-6)	0.001 USDC
audgusd	0.2 AUD (2e-1)	0.000001 AUD (1e-6)	1e-8 GUSD
audrlusd	0.2 AUD (2e-1)	0.000001 AUD (1e-6)	1e-8 RLUSD
audusd	0.2 AUD (2e-1)	0.000001 AUD (1e-6)	1e-8 USD
audusdc	0.2 AUD (2e-1)	0.000001 AUD (1e-6)	1e-8 USDC
avaxgusd	0.00499999 AVAX (4.99999e-3)	0.000001 AVAX (1e-6)	0.001 GUSD
avaxgusdperp	0.1 AVAX (1e-1)	0.1 AVAX (1e-1)	0.001 GUSD
avaxrlusd	0.00499999 AVAX (4.99999e-3)	0.000001 AVAX (1e-6)	0.001 RLUSD
avaxusd	0.00499999 AVAX (4.99999e-3)	0.000001 AVAX (1e-6)	0.001 USD
avaxusdc	0.00499999 AVAX (4.99999e-3)	0.000001 AVAX (1e-6)	0.001 USDC
avaxusdcperp	0.1 AVAX (1e-1)	0.1 AVAX (1e-1)	0.001 USDC
batgusd	1 BAT (1e+0)	0.000001 BAT (1e-6)	0.00001 GUSD
batrlusd	1 BAT (1e+0)	0.000001 BAT (1e-6)	0.00001 RLUSD
batusd	1 BAT (1e+0)	0.000001 BAT (1e-6)	0.00001 USD
batusdc	1 BAT (1e+0)	0.000001 BAT (1e-6)	0.00001 USDC
bchgusd	0.001 BCH (1e-3)	0.000001 BCH (1e-6)	0.01 GUSD
bchgusdperp	0.001 BCH (1e-3)	0.001 BCH (1e-3)	0.01 GUSD
bchrlusd	0.001 BCH (1e-3)	0.000001 BCH (1e-6)	0.01 RLUSD
bchusd	0.001 BCH (1e-3)	0.000001 BCH (1e-6)	0.01 USD
bchusdc	0.001 BCH (1e-3)	0.000001 BCH (1e-6)	0.01 USDC
bchusdcperp	0.001 BCH (1e-3)	0.001 BCH (1e-3)	0.01 USDC
bnbgusd	0.0002 BNB (2e-4)	0.000001 BNB (1e-6)	0.0001 GUSD
bnbgusdperp	0.01 BNB (1e-2)	0.01 BNB (1e-2)	0.05 GUSD
bnbrlusd	0.0002 BNB (2e-4)	0.000001 BNB (1e-6)	0.0001 RLUSD
bnbusd	0.0002 BNB (2e-4)	0.000001 BNB (1e-6)	0.0001 USD
bnbusdc	0.0002 BNB (2e-4)	0.000001 BNB (1e-6)	0.0001 USDC
bnbusdcperp	0.01 BNB (1e-2)	0.01 BNB (1e-2)	0.05 USDC
bomegusd	10 BOME (1e+1)	0.01 BOME (1e-2)	0.000001 GUSD
bomerlusd	10 BOME (1e+1)	0.01 BOME (1e-2)	0.000001 RLUSD
bomeusd	10 BOME (1e+1)	0.01 BOME (1e-2)	0.000001 USD
bomeusdc	10 BOME (1e+1)	0.01 BOME (1e-2)	0.000001 USDC
bonkgusd	4000 BONK (4e+3)	0.000001 BONK (1e-6)	1e-9 GUSD
bonkgusdperp	5000 BONK (5e+3)	1 BONK (1e+0)	1e-9 GUSD
bonkrlusd	4000 BONK (4e+3)	0.000001 BONK (1e-6)	1e-9 RLUSD
bonkusd	4000 BONK (4e+3)	0.000001 BONK (1e-6)	1e-9 USD
bonkusdc	4000 BONK (4e+3)	0.000001 BONK (1e-6)	1e-9 USDC
bonkusdcperp	5000 BONK (5e+3)	1 BONK (1e+0)	1e-9 USDC
btceur	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 EUR
btcgbp	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 GBP
btcgusd	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 GUSD
btcgusdperp	0.0001 BTC (1e-4)	0.0001 BTC (1e-4)	0.5 GUSD
btcrlusd	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 RLUSD
btcsgd	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 SGD
btcusd	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 USD
btcusdc	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 USDC
btcusdcperp	0.0001 BTC (1e-4)	0.0001 BTC (1e-4)	0.5 USDC
btcusdt	0.00001 BTC (1e-5)	1e-8 BTC (1e-8)	0.01 USDT
chillguygusd	0.5 CHILLGUY (5e-1)	0.01 CHILLGUY (1e-2)	0.0001 GUSD
chillguyrlusd	0.5 CHILLGUY (5e-1)	0.01 CHILLGUY (1e-2)	0.0001 RLUSD
chillguyusd	0.5 CHILLGUY (5e-1)	0.01 CHILLGUY (1e-2)	0.0001 USD
chillguyusdc	0.5 CHILLGUY (5e-1)	0.01 CHILLGUY (1e-2)	0.0001 USDC
chzgusd	0.5 CHZ (5e-1)	0.000001 CHZ (1e-6)	0.00001 GUSD
chzrlusd	0.5 CHZ (5e-1)	0.000001 CHZ (1e-6)	0.00001 RLUSD
chzusd	0.5 CHZ (5e-1)	0.000001 CHZ (1e-6)	0.00001 USD
chzusdc	0.5 CHZ (5e-1)	0.000001 CHZ (1e-6)	0.00001 USDC
compgusd	0.001 COMP (1e-3)	0.000001 COMP (1e-6)	0.01 GUSD
comprlusd	0.001 COMP (1e-3)	0.000001 COMP (1e-6)	0.01 RLUSD
compusd	0.001 COMP (1e-3)	0.000001 COMP (1e-6)	0.01 USD
compusdc	0.001 COMP (1e-3)	0.000001 COMP (1e-6)	0.01 USDC
crvgusd	0.1 CRV (1e-1)	0.000001 CRV (1e-6)	0.0001 GUSD
crvrlusd	0.1 CRV (1e-1)	0.000001 CRV (1e-6)	0.0001 RLUSD
crvusd	0.1 CRV (1e-1)	0.000001 CRV (1e-6)	0.0001 USD
crvusdc	0.1 CRV (1e-1)	0.000001 CRV (1e-6)	0.0001 USDC
ctxgusd	0.002 CTX (2e-3)	0.000001 CTX (1e-6)	0.0001 GUSD
ctxrlusd	0.002 CTX (2e-3)	0.000001 CTX (1e-6)	0.0001 RLUSD
ctxusd	0.002 CTX (2e-3)	0.000001 CTX (1e-6)	0.0001 USD
ctxusdc	0.002 CTX (2e-3)	0.000001 CTX (1e-6)	0.0001 USDC
cubegusd	0.01 CUBE (1e-2)	0.000001 CUBE (1e-6)	0.0001 GUSD
cuberlusd	0.01 CUBE (1e-2)	0.000001 CUBE (1e-6)	0.0001 RLUSD
cubeusd	0.01 CUBE (1e-2)	0.000001 CUBE (1e-6)	0.0001 USD
cubeusdc	0.01 CUBE (1e-2)	0.000001 CUBE (1e-6)	0.0001 USDC
daigusd	0.1 DAI (1e-1)	0.000001 DAI (1e-6)	0.00001 GUSD
dairlusd	0.1 DAI (1e-1)	0.000001 DAI (1e-6)	0.00001 RLUSD
daiusd	0.1 DAI (1e-1)	0.000001 DAI (1e-6)	0.00001 USD
daiusdc	0.1 DAI (1e-1)	0.000001 DAI (1e-6)	0.00001 USDC
dogebtc	1 DOGE (1e+0)	1e-8 DOGE (1e-8)	1e-9 BTC
dogeeth	1 DOGE (1e+0)	1e-8 DOGE (1e-8)	1e-8 ETH
dogegusd	0.1 DOGE (1e-1)	0.000001 DOGE (1e-6)	0.00001 GUSD
dogegusdperp	1 DOGE (1e+0)	1 DOGE (1e+0)	0.00001 GUSD
dogerlusd	0.1 DOGE (1e-1)	0.000001 DOGE (1e-6)	0.00001 RLUSD
dogeusd	0.1 DOGE (1e-1)	0.000001 DOGE (1e-6)	0.00001 USD
dogeusdc	0.1 DOGE (1e-1)	0.000001 DOGE (1e-6)	0.00001 USDC
dogeusdcperp	1 DOGE (1e+0)	1 DOGE (1e+0)	0.00001 USDC
dotgusd	0.01 DOT (1e-2)	0.000001 DOT (1e-6)	0.0001 GUSD
dotrlusd	0.01 DOT (1e-2)	0.000001 DOT (1e-6)	0.0001 RLUSD
dotusd	0.01 DOT (1e-2)	0.000001 DOT (1e-6)	0.0001 USD
dotusdc	0.01 DOT (1e-2)	0.000001 DOT (1e-6)	0.0001 USDC
driftgusd	0.1 DRIFT (1e-1)	0.000001 DRIFT (1e-6)	0.0001 GUSD
driftrlusd	0.1 DRIFT (1e-1)	0.000001 DRIFT (1e-6)	0.0001 RLUSD
driftusd	0.1 DRIFT (1e-1)	0.000001 DRIFT (1e-6)	0.0001 USD
driftusdc	0.1 DRIFT (1e-1)	0.000001 DRIFT (1e-6)	0.0001 USDC
elongusd	60000 ELON (6e+4)	0.000001 ELON (1e-6)	1e-9 GUSD
elonrlusd	60000 ELON (6e+4)	0.000001 ELON (1e-6)	1e-9 RLUSD
elonusd	60000 ELON (6e+4)	0.000001 ELON (1e-6)	1e-9 USD
elonusdc	60000 ELON (6e+4)	0.000001 ELON (1e-6)	1e-9 USDC
ensgusd	0.002 ENS (2e-3)	0.000001 ENS (1e-6)	0.001 GUSD
ensrlusd	0.002 ENS (2e-3)	0.000001 ENS (1e-6)	0.001 RLUSD
ensusd	0.002 ENS (2e-3)	0.000001 ENS (1e-6)	0.001 USD
ensusdc	0.002 ENS (2e-3)	0.000001 ENS (1e-6)	0.001 USDC
ethbtc	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.00001 BTC
etheur	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 EUR
ethgbp	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 GBP
ethgusd	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 GUSD
ethgusdperp	0.001 ETH (1e-3)	0.001 ETH (1e-3)	0.05 GUSD
ethrlusd	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 RLUSD
ethsgd	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 SGD
ethusd	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 USD
ethusdc	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 USDC
ethusdcperp	0.001 ETH (1e-3)	0.001 ETH (1e-3)	0.05 USDC
ethusdt	0.001 ETH (1e-3)	0.000001 ETH (1e-6)	0.01 USDT
eulgusd	0.01 EUL (1e-2)	0.000001 EUL (1e-6)	0.0001 GUSD
eulrlusd	0.01 EUL (1e-2)	0.000001 EUL (1e-6)	0.0001 RLUSD
eulusd	0.01 EUL (1e-2)	0.000001 EUL (1e-6)	0.0001 USD
eulusdc	0.01 EUL (1e-2)	0.000001 EUL (1e-6)	0.0001 USDC
eurusd	0.1 EUR (1e-1)	0.000001 EUR (1e-6)	0.00001 USD
eurusdc	0.1 EUR (1e-1)	0.000001 EUR (1e-6)	0.00001 USDC
fartcoingusd	0.1 FARTCOIN (1e-1)	0.000001 FARTCOIN (1e-6)	0.000001 GUSD
fartcoinrlusd	0.1 FARTCOIN (1e-1)	0.000001 FARTCOIN (1e-6)	0.000001 RLUSD
fartcoinusd	0.1 FARTCOIN (1e-1)	0.000001 FARTCOIN (1e-6)	0.000001 USD
fartcoinusdc	0.1 FARTCOIN (1e-1)	0.000001 FARTCOIN (1e-6)	0.000001 USDC
fetgusd	0.1 FET (1e-1)	0.000001 FET (1e-6)	0.00001 GUSD
fetrlusd	0.1 FET (1e-1)	0.000001 FET (1e-6)	0.00001 RLUSD
fetusd	0.1 FET (1e-1)	0.000001 FET (1e-6)	0.00001 USD
fetusdc	0.1 FET (1e-1)	0.000001 FET (1e-6)	0.00001 USDC
filgusd	0.1 FIL (1e-1)	0.000001 FIL (1e-6)	0.0001 GUSD
filrlusd	0.1 FIL (1e-1)	0.000001 FIL (1e-6)	0.0001 RLUSD
filusd	0.1 FIL (1e-1)	0.000001 FIL (1e-6)	0.0001 USD
filusdc	0.1 FIL (1e-1)	0.000001 FIL (1e-6)	0.0001 USDC
flokigusd	400 FLOKI (4e+2)	0.000001 FLOKI (1e-6)	1e-7 GUSD
flokigusdperp	500 FLOKI (5e+2)	1 FLOKI (1e+0)	1e-8 GUSD
flokirlusd	400 FLOKI (4e+2)	0.000001 FLOKI (1e-6)	1e-7 RLUSD
flokiusd	400 FLOKI (4e+2)	0.000001 FLOKI (1e-6)	1e-7 USD
flokiusdc	400 FLOKI (4e+2)	0.000001 FLOKI (1e-6)	1e-7 USDC
flokiusdcperp	500 FLOKI (5e+2)	1 FLOKI (1e+0)	1e-8 USDC
ftmgusd	0.03 FTM (3e-2)	0.000001 FTM (1e-6)	0.0001 GUSD
ftmrlusd	0.03 FTM (3e-2)	0.000001 FTM (1e-6)	0.0001 RLUSD
ftmusd	0.03 FTM (3e-2)	0.000001 FTM (1e-6)	0.0001 USD
ftmusdc	0.03 FTM (3e-2)	0.000001 FTM (1e-6)	0.0001 USDC
galagusd	0.4 GALA (4e-1)	0.000001 GALA (1e-6)	0.00001 GUSD
galarlusd	0.4 GALA (4e-1)	0.000001 GALA (1e-6)	0.00001 RLUSD
galausd	0.4 GALA (4e-1)	0.000001 GALA (1e-6)	0.00001 USD
galausdc	0.4 GALA (4e-1)	0.000001 GALA (1e-6)	0.00001 USDC
gmtgusd	0.1 GMT (1e-1)	0.000001 GMT (1e-6)	0.00001 GUSD
gmtrlusd	0.1 GMT (1e-1)	0.000001 GMT (1e-6)	0.00001 RLUSD
gmtusd	0.1 GMT (1e-1)	0.000001 GMT (1e-6)	0.00001 USD
gmtusdc	0.1 GMT (1e-1)	0.000001 GMT (1e-6)	0.00001 USDC
goatgusd	0.1 GOAT (1e-1)	0.000001 GOAT (1e-6)	0.0001 GUSD
goatrlusd	0.1 GOAT (1e-1)	0.000001 GOAT (1e-6)	0.0001 RLUSD
goatusd	0.1 GOAT (1e-1)	0.000001 GOAT (1e-6)	0.0001 USD
goatusdc	0.1 GOAT (1e-1)	0.000001 GOAT (1e-6)	0.0001 USDC
grtgusd	0.1 GRT (1e-1)	0.000001 GRT (1e-6)	0.0001 GUSD
grtrlusd	0.1 GRT (1e-1)	0.000001 GRT (1e-6)	0.0001 RLUSD
grtusd	0.1 GRT (1e-1)	0.000001 GRT (1e-6)	0.0001 USD
grtusdc	0.1 GRT (1e-1)	0.000001 GRT (1e-6)	0.0001 USDC
gusdgbp	0.1 GUSD (1e-1)	0.0001 GUSD (1e-4)	0.00001 GBP
gusdsgd	0.1 GUSD (1e-1)	0.000001 GUSD (1e-6)	0.00001 SGD
hntgusd	0.04 HNT (4e-2)	0.000001 HNT (1e-6)	0.0001 GUSD
hntrlusd	0.04 HNT (4e-2)	0.000001 HNT (1e-6)	0.0001 RLUSD
hntusd	0.04 HNT (4e-2)	0.000001 HNT (1e-6)	0.0001 USD
hntusdc	0.04 HNT (4e-2)	0.000001 HNT (1e-6)	0.0001 USDC
hypegusd	0.002 HYPE (2e-3)	0.000001 HYPE (1e-6)	0.0001 GUSD
hypegusdperp	0.1 HYPE (1e-1)	0.1 HYPE (1e-1)	0.001 GUSD
hyperlusd	0.002 HYPE (2e-3)	0.000001 HYPE (1e-6)	0.0001 RLUSD
hypeusd	0.002 HYPE (2e-3)	0.000001 HYPE (1e-6)	0.0001 USD
hypeusdc	0.002 HYPE (2e-3)	0.000001 HYPE (1e-6)	0.0001 USDC
hypeusdcperp	0.1 HYPE (1e-1)	0.1 HYPE (1e-1)	0.001 USDC
imxgusd	0.1 IMX (1e-1)	0.000001 IMX (1e-6)	0.00001 GUSD
imxrlusd	0.1 IMX (1e-1)	0.000001 IMX (1e-6)	0.00001 RLUSD
imxusd	0.1 IMX (1e-1)	0.000001 IMX (1e-6)	0.00001 USD
imxusdc	0.1 IMX (1e-1)	0.000001 IMX (1e-6)	0.00001 USDC
injgusd	0.01 INJ (1e-2)	0.000001 INJ (1e-6)	0.0001 GUSD
injgusdperp	0.1 INJ (1e-1)	0.1 INJ (1e-1)	0.001 GUSD
injrlusd	0.01 INJ (1e-2)	0.000001 INJ (1e-6)	0.0001 RLUSD
injusd	0.01 INJ (1e-2)	0.000001 INJ (1e-6)	0.0001 USD
injusdc	0.01 INJ (1e-2)	0.000001 INJ (1e-6)	0.0001 USDC
injusdcperp	0.1 INJ (1e-1)	0.1 INJ (1e-1)	0.001 USDC
iotxgusd	3 IOTX (3e+0)	0.000001 IOTX (1e-6)	0.000001 GUSD
iotxrlusd	3 IOTX (3e+0)	0.000001 IOTX (1e-6)	0.000001 RLUSD
iotxusd	3 IOTX (3e+0)	0.000001 IOTX (1e-6)	0.000001 USD
iotxusdc	3 IOTX (3e+0)	0.000001 IOTX (1e-6)	0.000001 USDC
jitosolgusd	0.0005 JITOSOL (5e-4)	0.000001 JITOSOL (1e-6)	0.0001 GUSD
jitosolrlusd	0.0005 JITOSOL (5e-4)	0.000001 JITOSOL (1e-6)	0.0001 RLUSD
jitosolsol	0.0005 JITOSOL (5e-4)	0.000001 JITOSOL (1e-6)	0.0001 SOL
jitosolusd	0.0005 JITOSOL (5e-4)	0.000001 JITOSOL (1e-6)	0.0001 USD
jitosolusdc	0.0005 JITOSOL (5e-4)	0.000001 JITOSOL (1e-6)	0.0001 USDC
jtogusd	0.05 JTO (5e-2)	0.000001 JTO (1e-6)	0.0001 GUSD
jtorlusd	0.05 JTO (5e-2)	0.000001 JTO (1e-6)	0.0001 RLUSD
jtousd	0.05 JTO (5e-2)	0.000001 JTO (1e-6)	0.0001 USD
jtousdc	0.05 JTO (5e-2)	0.000001 JTO (1e-6)	0.0001 USDC
jupgusd	0.3 JUP (3e-1)	0.000001 JUP (1e-6)	0.000001 GUSD
juprlusd	0.3 JUP (3e-1)	0.000001 JUP (1e-6)	0.000001 RLUSD
jupusd	0.3 JUP (3e-1)	0.000001 JUP (1e-6)	0.000001 USD
jupusdc	0.3 JUP (3e-1)	0.000001 JUP (1e-6)	0.000001 USDC
kmnogusd	1 KMNO (1e+0)	0.000001 KMNO (1e-6)	0.000001 GUSD
kmnorlusd	1 KMNO (1e+0)	0.000001 KMNO (1e-6)	0.000001 RLUSD
kmnousd	1 KMNO (1e+0)	0.000001 KMNO (1e-6)	0.000001 USD
kmnousdc	1 KMNO (1e+0)	0.000001 KMNO (1e-6)	0.000001 USDC
ksl2gusdperp	0.1 KSL2 (1e-1)	0.01 KSL2 (1e-2)	0.01 GUSD
ksl2usdcperp	0.1 KSL2 (1e-1)	0.01 KSL2 (1e-2)	0.01 USDC
kt5gusdperp	0.01 KT5 (1e-2)	0.001 KT5 (1e-3)	0.1 GUSD
kt5usdcperp	0.01 KT5 (1e-2)	0.001 KT5 (1e-3)	0.1 USDC
ldogusd	0.02 LDO (2e-2)	0.000001 LDO (1e-6)	0.001 GUSD
ldorlusd	0.02 LDO (2e-2)	0.000001 LDO (1e-6)	0.001 RLUSD
ldousd	0.02 LDO (2e-2)	0.000001 LDO (1e-6)	0.001 USD
ldousdc	0.02 LDO (2e-2)	0.000001 LDO (1e-6)	0.001 USDC
linkbtc	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	1e-8 BTC
linketh	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	1e-7 ETH
linkgusd	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	0.00001 GUSD
linkgusdperp	0.1 LINK (1e-1)	0.1 LINK (1e-1)	0.001 GUSD
linkrlusd	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	0.00001 RLUSD
linksusd	700 LINKS (7e+2)	0.000001 LINKS (1e-6)	1e-9 USD
linkusd	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	0.00001 USD
linkusdc	0.1 LINK (1e-1)	0.000001 LINK (1e-6)	0.00001 USDC
linkusdcperp	0.1 LINK (1e-1)	0.1 LINK (1e-1)	0.001 USDC
lptgusd	0.001 LPT (1e-3)	0.000001 LPT (1e-6)	0.0001 GUSD
lptrlusd	0.001 LPT (1e-3)	0.000001 LPT (1e-6)	0.0001 RLUSD
lptusd	0.001 LPT (1e-3)	0.000001 LPT (1e-6)	0.0001 USD
lptusdc	0.001 LPT (1e-3)	0.000001 LPT (1e-6)	0.0001 USDC
lrcgusd	0.1 LRC (1e-1)	0.000001 LRC (1e-6)	0.00001 GUSD
lrcrlusd	0.1 LRC (1e-1)	0.000001 LRC (1e-6)	0.00001 RLUSD
lrcusd	0.1 LRC (1e-1)	0.000001 LRC (1e-6)	0.00001 USD
lrcusdc	0.1 LRC (1e-1)	0.000001 LRC (1e-6)	0.00001 USDC
ltcbtc	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	1e-7 BTC
ltceth	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	0.00001 ETH
ltcgusd	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	0.01 GUSD
ltcgusdperp	0.1 LTC (1e-1)	0.1 LTC (1e-1)	0.01 GUSD
ltcrlusd	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	0.01 RLUSD
ltcusd	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	0.01 USD
ltcusdc	0.01 LTC (1e-2)	0.00001 LTC (1e-5)	0.01 USDC
ltcusdcperp	0.1 LTC (1e-1)	0.1 LTC (1e-1)	0.01 USDC
managusd	1 MANA (1e+0)	0.000001 MANA (1e-6)	0.00001 GUSD
manarlusd	1 MANA (1e+0)	0.000001 MANA (1e-6)	0.00001 RLUSD
manausd	1 MANA (1e+0)	0.000001 MANA (1e-6)	0.00001 USD
manausdc	1 MANA (1e+0)	0.000001 MANA (1e-6)	0.00001 USDC
maskgusd	0.01 MASK (1e-2)	0.000001 MASK (1e-6)	0.001 GUSD
maskrlusd	0.01 MASK (1e-2)	0.000001 MASK (1e-6)	0.001 RLUSD
maskusd	0.01 MASK (1e-2)	0.000001 MASK (1e-6)	0.001 USD
maskusdc	0.01 MASK (1e-2)	0.000001 MASK (1e-6)	0.001 USDC
mewgusd	10 MEW (1e+1)	0.01 MEW (1e-2)	0.000001 GUSD
mewgusdperp	10 MEW (1e+1)	1 MEW (1e+0)	0.000001 GUSD
mewrlusd	10 MEW (1e+1)	0.01 MEW (1e-2)	0.000001 RLUSD
mewusd	10 MEW (1e+1)	0.01 MEW (1e-2)	0.000001 USD
mewusdc	10 MEW (1e+1)	0.01 MEW (1e-2)	0.000001 USDC
mewusdcperp	10 MEW (1e+1)	1 MEW (1e+0)	0.000001 USDC
mongusd	1 MON (1e+0)	0.000001 MON (1e-6)	0.000001 GUSD
monrlusd	1 MON (1e+0)	0.000001 MON (1e-6)	0.000001 RLUSD
monusd	1 MON (1e+0)	0.000001 MON (1e-6)	0.000001 USD
monusdc	1 MON (1e+0)	0.000001 MON (1e-6)	0.000001 USDC
moodenggusd	1 MOODENG (1e+0)	0.000001 MOODENG (1e-6)	0.000001 GUSD
moodengrlusd	1 MOODENG (1e+0)	0.000001 MOODENG (1e-6)	0.000001 RLUSD
moodengusd	1 MOODENG (1e+0)	0.000001 MOODENG (1e-6)	0.000001 USD
moodengusdc	1 MOODENG (1e+0)	0.000001 MOODENG (1e-6)	0.000001 USDC
opgusd	0.07 OP (7e-2)	0.000001 OP (1e-6)	0.0001 GUSD
opgusdperp	1 OP (1e+0)	0.1 OP (1e-1)	0.0001 GUSD
oprlusd	0.07 OP (7e-2)	0.000001 OP (1e-6)	0.0001 RLUSD
opusd	0.07 OP (7e-2)	0.000001 OP (1e-6)	0.0001 USD
opusdc	0.07 OP (7e-2)	0.000001 OP (1e-6)	0.0001 USDC
opusdcperp	1 OP (1e+0)	0.1 OP (1e-1)	0.0001 USDC
paxggusd	0.0001 PAXG (1e-4)	1e-8 PAXG (1e-8)	0.01 GUSD
paxgrlusd	0.0001 PAXG (1e-4)	1e-8 PAXG (1e-8)	0.01 RLUSD
paxgusd	0.0001 PAXG (1e-4)	1e-8 PAXG (1e-8)	0.01 USD
paxgusdc	0.0001 PAXG (1e-4)	1e-8 PAXG (1e-8)	0.01 USDC
pengugusd	3 PENGU (3e+0)	0.000001 PENGU (1e-6)	1e-7 GUSD
pengurlusd	3 PENGU (3e+0)	0.000001 PENGU (1e-6)	1e-7 RLUSD
penguusd	3 PENGU (3e+0)	0.000001 PENGU (1e-6)	1e-7 USD
penguusdc	3 PENGU (3e+0)	0.000001 PENGU (1e-6)	1e-7 USDC
pepegusd	1000 PEPE (1e+3)	0.000001 PEPE (1e-6)	1e-9 GUSD
pepegusdperp	1 PEPE (1e+0)	1 PEPE (1e+0)	1e-9 GUSD
peperlusd	1000 PEPE (1e+3)	0.000001 PEPE (1e-6)	1e-9 RLUSD
pepeusd	1000 PEPE (1e+3)	0.000001 PEPE (1e-6)	1e-9 USD
pepeusdc	1000 PEPE (1e+3)	0.000001 PEPE (1e-6)	1e-9 USDC
pepeusdcperp	1 PEPE (1e+0)	1 PEPE (1e+0)	1e-9 USDC
pnutgusd	0.2 PNUT (2e-1)	0.0001 PNUT (1e-4)	0.0001 GUSD
pnutrlusd	0.2 PNUT (2e-1)	0.0001 PNUT (1e-4)	0.0001 RLUSD
pnutusd	0.2 PNUT (2e-1)	0.0001 PNUT (1e-4)	0.0001 USD
pnutusdc	0.2 PNUT (2e-1)	0.0001 PNUT (1e-4)	0.0001 USDC
polgusd	0.4 POL (4e-1)	0.000001 POL (1e-6)	0.000001 GUSD
polgusdperp	1 POL (1e+0)	1 POL (1e+0)	0.0001 GUSD
polrlusd	0.4 POL (4e-1)	0.000001 POL (1e-6)	0.000001 RLUSD
polusd	0.4 POL (4e-1)	0.000001 POL (1e-6)	0.000001 USD
polusdc	0.4 POL (4e-1)	0.000001 POL (1e-6)	0.000001 USDC
polusdcperp	1 POL (1e+0)	1 POL (1e+0)	0.0001 USDC
popcatgusd	0.07 POPCAT (7e-2)	0.000001 POPCAT (1e-6)	0.0001 GUSD
popcatgusdperp	1 POPCAT (1e+0)	0.1 POPCAT (1e-1)	0.0001 GUSD
popcatrlusd	0.07 POPCAT (7e-2)	0.000001 POPCAT (1e-6)	0.0001 RLUSD
popcatusd	0.07 POPCAT (7e-2)	0.000001 POPCAT (1e-6)	0.0001 USD
popcatusdc	0.07 POPCAT (7e-2)	0.000001 POPCAT (1e-6)	0.0001 USDC
popcatusdcperp	1 POPCAT (1e+0)	0.1 POPCAT (1e-1)	0.0001 USDC
pumpgusd	20 PUMP (2e+1)	0.00001 PUMP (1e-5)	1e-8 GUSD
pumprlusd	20 PUMP (2e+1)	0.00001 PUMP (1e-5)	1e-8 RLUSD
pumpusd	20 PUMP (2e+1)	0.00001 PUMP (1e-5)	1e-8 USD
pumpusdc	20 PUMP (2e+1)	0.00001 PUMP (1e-5)	1e-8 USDC
pythgusd	0.2 PYTH (2e-1)	0.000001 PYTH (1e-6)	0.00001 GUSD
pythrlusd	0.2 PYTH (2e-1)	0.000001 PYTH (1e-6)	0.00001 RLUSD
pythusd	0.2 PYTH (2e-1)	0.000001 PYTH (1e-6)	0.00001 USD
pythusdc	0.2 PYTH (2e-1)	0.000001 PYTH (1e-6)	0.00001 USDC
qntgusd	0.0004 QNT (4e-4)	0.000001 QNT (1e-6)	0.01 GUSD
qntrlusd	0.0004 QNT (4e-4)	0.000001 QNT (1e-6)	0.01 RLUSD
qntusd	0.0004 QNT (4e-4)	0.000001 QNT (1e-6)	0.01 USD
qntusdc	0.0004 QNT (4e-4)	0.000001 QNT (1e-6)	0.01 USDC
rlusdgusd	0.1 RLUSD (1e-1)	0.000001 RLUSD (1e-6)	0.0001 GUSD
rlusdusd	0.1 RLUSD (1e-1)	0.000001 RLUSD (1e-6)	0.0001 USD
rlusdusdc	0.1 RLUSD (1e-1)	0.000001 RLUSD (1e-6)	0.0001 USDC
rndrgusd	0.02 RNDR (2e-2)	0.000001 RNDR (1e-6)	0.001 GUSD
rndrrlusd	0.02 RNDR (2e-2)	0.000001 RNDR (1e-6)	0.001 RLUSD
rndrusd	0.02 RNDR (2e-2)	0.000001 RNDR (1e-6)	0.001 USD
rndrusdc	0.02 RNDR (2e-2)	0.000001 RNDR (1e-6)	0.001 USDC
samogusd	10 SAMO (1e+1)	0.000001 SAMO (1e-6)	1e-7 GUSD
samorlusd	10 SAMO (1e+1)	0.000001 SAMO (1e-6)	1e-7 RLUSD
samousd	10 SAMO (1e+1)	0.000001 SAMO (1e-6)	1e-7 USD
samousdc	10 SAMO (1e+1)	0.000001 SAMO (1e-6)	1e-7 USDC
sandgusd	0.1 SAND (1e-1)	0.000001 SAND (1e-6)	0.00001 GUSD
sandrlusd	0.1 SAND (1e-1)	0.000001 SAND (1e-6)	0.00001 RLUSD
sandusd	0.1 SAND (1e-1)	0.000001 SAND (1e-6)	0.00001 USD
sandusdc	0.1 SAND (1e-1)	0.000001 SAND (1e-6)	0.00001 USDC
shibgusd	1000 SHIB (1e+3)	0.000001 SHIB (1e-6)	1e-9 GUSD
shibgusdperp	50 SHIB (5e+1)	50 SHIB (5e+1)	1e-9 GUSD
shibrlusd	1000 SHIB (1e+3)	0.000001 SHIB (1e-6)	1e-9 RLUSD
shibusd	1000 SHIB (1e+3)	0.000001 SHIB (1e-6)	1e-9 USD
shibusdc	1000 SHIB (1e+3)	0.000001 SHIB (1e-6)	1e-9 USDC
shibusdcperp	50 SHIB (5e+1)	50 SHIB (5e+1)	1e-9 USDC
sklgusd	0.1 SKL (1e-1)	0.000001 SKL (1e-6)	0.00001 GUSD
sklrlusd	0.1 SKL (1e-1)	0.000001 SKL (1e-6)	0.00001 RLUSD
sklusd	0.1 SKL (1e-1)	0.000001 SKL (1e-6)	0.00001 USD
sklusdc	0.1 SKL (1e-1)	0.000001 SKL (1e-6)	0.00001 USDC
skygusd	1 SKY (1e+0)	0.000001 SKY (1e-6)	1e-7 GUSD
skyrlusd	1 SKY (1e+0)	0.000001 SKY (1e-6)	1e-7 RLUSD
skyusd	1 SKY (1e+0)	0.000001 SKY (1e-6)	1e-7 USD
skyusdc	1 SKY (1e+0)	0.000001 SKY (1e-6)	1e-7 USDC
solbtc	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	1e-7 BTC
soleth	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	0.000001 ETH
solgusd	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	0.001 GUSD
solgusdperp	0.1 SOL (1e-1)	0.1 SOL (1e-1)	0.005 GUSD
solrlusd	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	0.001 RLUSD
solusd	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	0.001 USD
solusdc	0.001 SOL (1e-3)	0.000001 SOL (1e-6)	0.001 USDC
solusdcperp	0.1 SOL (1e-1)	0.1 SOL (1e-1)	0.005 USDC
storjgusd	0.1 STORJ (1e-1)	0.000001 STORJ (1e-6)	0.00001 GUSD
storjrlusd	0.1 STORJ (1e-1)	0.000001 STORJ (1e-6)	0.00001 RLUSD
storjusd	0.1 STORJ (1e-1)	0.000001 STORJ (1e-6)	0.00001 USD
storjusdc	0.1 STORJ (1e-1)	0.000001 STORJ (1e-6)	0.00001 USDC
sushigusd	0.01 SUSHI (1e-2)	0.000001 SUSHI (1e-6)	0.0001 GUSD
sushirlusd	0.01 SUSHI (1e-2)	0.000001 SUSHI (1e-6)	0.0001 RLUSD
sushiusd	0.01 SUSHI (1e-2)	0.000001 SUSHI (1e-6)	0.0001 USD
sushiusdc	0.01 SUSHI (1e-2)	0.000001 SUSHI (1e-6)	0.0001 USDC
tongusd	0.05 TON (5e-2)	0.000001 TON (1e-6)	0.0001 GUSD
tonrlusd	0.05 TON (5e-2)	0.000001 TON (1e-6)	0.0001 RLUSD
tonusd	0.05 TON (5e-2)	0.000001 TON (1e-6)	0.0001 USD
tonusdc	0.05 TON (5e-2)	0.000001 TON (1e-6)	0.0001 USDC
trumpgusd	0.01 TRUMP (1e-2)	0.000001 TRUMP (1e-6)	0.0001 GUSD
trumpgusdperp	0.1 TRUMP (1e-1)	0.001 TRUMP (1e-3)	0.001 GUSD
trumprlusd	0.01 TRUMP (1e-2)	0.000001 TRUMP (1e-6)	0.0001 RLUSD
trumpusd	0.01 TRUMP (1e-2)	0.000001 TRUMP (1e-6)	0.0001 USD
trumpusdc	0.01 TRUMP (1e-2)	0.000001 TRUMP (1e-6)	0.0001 USDC
trxgusd	0.3 TRX (3e-1)	0.000001 TRX (1e-6)	0.000001 GUSD
trxrlusd	0.3 TRX (3e-1)	0.000001 TRX (1e-6)	0.000001 RLUSD
trxusd	0.3 TRX (3e-1)	0.000001 TRX (1e-6)	0.000001 USD
trxusdc	0.3 TRX (3e-1)	0.000001 TRX (1e-6)	0.000001 USDC
umagusd	0.01 UMA (1e-2)	0.000001 UMA (1e-6)	0.0001 GUSD
umarlusd	0.01 UMA (1e-2)	0.000001 UMA (1e-6)	0.0001 RLUSD
umausd	0.01 UMA (1e-2)	0.000001 UMA (1e-6)	0.0001 USD
umausdc	0.01 UMA (1e-2)	0.000001 UMA (1e-6)	0.0001 USDC
unigusd	0.01 UNI (1e-2)	0.000001 UNI (1e-6)	0.0001 GUSD
unigusdperp	0.1 UNI (1e-1)	0.1 UNI (1e-1)	0.001 GUSD
unirlusd	0.01 UNI (1e-2)	0.000001 UNI (1e-6)	0.0001 RLUSD
uniusd	0.01 UNI (1e-2)	0.000001 UNI (1e-6)	0.0001 USD
uniusdc	0.01 UNI (1e-2)	0.000001 UNI (1e-6)	0.0001 USDC
uniusdcperp	0.1 UNI (1e-1)	0.1 UNI (1e-1)	0.001 USDC
usd1usd	0.1 USD1 (1e-1)	0.000001 USD1 (1e-6)	0.00001 USD
usdcusd	0.1 USDC (1e-1)	0.000001 USDC (1e-6)	0.00001 USD
usdggusd	0.1 USDG (1e-1)	0.000001 USDG (1e-6)	0.000001 GUSD
usdgrlusd	0.1 USDG (1e-1)	0.000001 USDG (1e-6)	0.000001 RLUSD
usdgusd	0.1 USDG (1e-1)	0.000001 USDG (1e-6)	0.000001 USD
usdgusdc	0.1 USDG (1e-1)	0.000001 USDG (1e-6)	0.000001 USDC
usdtgusd	0.1 USDT (1e-1)	0.000001 USDT (1e-6)	0.00001 GUSD
usdtrlusd	0.1 USDT (1e-1)	0.000001 USDT (1e-6)	0.00001 RLUSD
usdtusd	0.1 USDT (1e-1)	0.000001 USDT (1e-6)	0.00001 USD
usdtusdc	0.1 USDT (1e-1)	0.000001 USDT (1e-6)	0.00001 USDC
wctgusd	0.3 WCT (3e-1)	0.000001 WCT (1e-6)	0.000001 GUSD
wctrlusd	0.3 WCT (3e-1)	0.000001 WCT (1e-6)	0.000001 RLUSD
wctusd	0.3 WCT (3e-1)	0.000001 WCT (1e-6)	0.000001 USD
wctusdc	0.3 WCT (3e-1)	0.000001 WCT (1e-6)	0.000001 USDC
wifgusd	0.07 WIF (7e-2)	0.000001 WIF (1e-6)	0.0001 GUSD
wifgusdperp	1 WIF (1e+0)	1 WIF (1e+0)	0.00001 GUSD
wifrlusd	0.07 WIF (7e-2)	0.000001 WIF (1e-6)	0.0001 RLUSD
wifusd	0.07 WIF (7e-2)	0.000001 WIF (1e-6)	0.0001 USD
wifusdc	0.07 WIF (7e-2)	0.000001 WIF (1e-6)	0.0001 USDC
wifusdcperp	1 WIF (1e+0)	1 WIF (1e+0)	0.00001 USDC
wldgusd	0.1 WLD (1e-1)	0.000001 WLD (1e-6)	0.000001 GUSD
wldrlusd	0.1 WLD (1e-1)	0.000001 WLD (1e-6)	0.000001 RLUSD
wldusd	0.1 WLD (1e-1)	0.000001 WLD (1e-6)	0.000001 USD
wldusdc	0.1 WLD (1e-1)	0.000001 WLD (1e-6)	0.000001 USDC
wlfigusd	0.1 WLFI (1e-1)	0.000001 WLFI (1e-6)	0.000001 GUSD
wlfirlusd	0.1 WLFI (1e-1)	0.000001 WLFI (1e-6)	0.000001 RLUSD
wlfiusd	0.1 WLFI (1e-1)	0.000001 WLFI (1e-6)	0.000001 USD
wlfiusdc	0.1 WLFI (1e-1)	0.000001 WLFI (1e-6)	0.000001 USDC
xrpgusd	0.1 XRP (1e-1)	0.000001 XRP (1e-6)	0.00001 GUSD
xrpgusdperp	1 XRP (1e+0)	1 XRP (1e+0)	0.0001 GUSD
xrprlusd	0.1 XRP (1e-1)	0.000001 XRP (1e-6)	0.00001 RLUSD
xrpusd	0.1 XRP (1e-1)	0.000001 XRP (1e-6)	0.00001 USD
xrpusdc	0.1 XRP (1e-1)	0.000001 XRP (1e-6)	0.00001 USDC
xrpusdcperp	1 XRP (1e+0)	1 XRP (1e+0)	0.0001 USDC
xtzgusd	0.02 XTZ (2e-2)	0.000001 XTZ (1e-6)	0.0001 GUSD
xtzrlusd	0.02 XTZ (2e-2)	0.000001 XTZ (1e-6)	0.0001 RLUSD
xtzusd	0.02 XTZ (2e-2)	0.000001 XTZ (1e-6)	0.0001 USD
xtzusdc	0.02 XTZ (2e-2)	0.000001 XTZ (1e-6)	0.0001 USDC
yfigusd	0.00001 YFI (1e-5)	0.000001 YFI (1e-6)	0.01 GUSD
yfirlusd	0.00001 YFI (1e-5)	0.000001 YFI (1e-6)	0.01 RLUSD
yfiusd	0.00001 YFI (1e-5)	0.000001 YFI (1e-6)	0.01 USD
yfiusdc	0.00001 YFI (1e-5)	0.000001 YFI (1e-6)	0.01 USDC
zecgusd	0.001 ZEC (1e-3)	0.000001 ZEC (1e-6)	0.01 GUSD
zecrlusd	0.001 ZEC (1e-3)	0.000001 ZEC (1e-6)	0.01 RLUSD
zecusd	0.001 ZEC (1e-3)	0.000001 ZEC (1e-6)	0.01 USD
zecusdc	0.001 ZEC (1e-3)	0.000001 ZEC (1e-6)	0.01 USDC
Total symbols: 449
Precision on the exchange
Quantity and price on incoming orders are strictly held to the minimums and increments on the table shown above.

However, once on the exchange, quantities and notional values may exhibit additional precision down to two decimal places past the "minimum order increment" listed above. For instance, it is possible that a btcusd trade could execute for a quantity of 0.0000000001 (1e-10) BTC. This is due to:

Incoming market orders that may result in partial fills
Fees
Holds
This additional precision is marketable once on the exchange.

Your account balances are maintained to full fractional precision in each currency.

Get Started
Data Types

Copy page

The protocol description below will contain references to various types, which are collected here for reference

Type	Description
string	A simple quoted string, following standard JSON rules; see the JSON spec for details.
decimal	A decimal value, encoded in a JSON string. The contents will be a series of digits, followed by an optional decimal point and additional digits.
timestamp	The number of seconds since 1970-01-01 UTC. This is usually provided for compatibility; implementors should use the more precise timestampms when available. When used as an input, either the millisecond or second precision is usable; this is unambiguous for dates past 1/29/1970
timestampms	The number of milliseconds since 1970-01-01 UTC. The begin date is the standard UNIX epoch, so this will be 1000 times the UNIX timestamp in seconds. This will be transmitted as a JSON number, not a string.
integer	A whole number, transmitted as a JSON number.
boolean	A JSON boolean, the literal string true or false
array	a JSON array. Each element contains a payload that will be described.





Roles

Copy page

Gemini uses a role-based system for private API endpoints so that you can separate privileges for your API keys.

By assigning different roles to different API keys, you can create:

One API key that can trade, and
Another API key that can withdraw digital assets, or
An API key to have access to read-only endpoints
You can configure which roles are assigned to your API keys by logging in to the Gemini Exchange website and going to API Settings to configure your API keys.

When you create an API key, the Trader role is assigned by default.
If you try to access an endpoint that requires a role you did not assign to your API key, you will get back a response with:

403 status
a JSON response body with:
reason set to MissingRole, and
message explaining what role you need to add to your API key to use this endpoint
See Error Codes for more information about API error responses.

Administrator
The Administrator role is exclusive to Master API keys.
Assigning the Administrator role to an API key allows this API key to:

Create accounts within the Master Group View accounts within the Master Group

Trader
Assigning the Trader role to an API key allows this API key to:

Check balances
Place and cancel orders
Check the status of orders
See all deposit addresses
See all active orders
See your trade history and volume
View accounts within the Master Group
Fund Manager
Assigning the Fund Manager role to an API key allows this API key to:

Check balances
See all deposit addresses
Request new cryptocurrency deposit addresses
Withdraw cryptocurrency funds
View accounts within the Master Group
Execute internal transfers between two accounts within the same Master group
Auditor
The Auditor role is read-only and cannot be combined with other roles.
Assigning the Auditor role to an API key allows this API key to:

Check balances
Check the status of orders
See transfers such as deposits and withdrawals
See all deposit addresses
See all active orders
See trade volume
See past trades
View accounts within the Master Group
Endpoint summary
Here's a summary of which role you need to assign to your API key to use each endpoint in the API:

Account Scoped Endpoints
Endpoint	URI	Trader can access?	Fund Manager can access?	Auditor can access?
Create New Order	/v1/order/new	✓	✗	✗
Cancel Order	/v1/order/cancel	✓	✗	✗
Cancel All Session Orders	/v1/order/cancel/session	✓	✗	✗
Cancel All Active Orders	/v1/order/cancel/all	✓	✗	✗
Wrap Order	/v1/wrap/:symbol	✓	✗	✗
Order Status	/v1/order/status	✓	✗	✓
Get Active Orders	/v1/orders	✓	✗	✓
List Past Trades	/v1/mytrades	✓	✗	✓
Get Orders History	/v1/orders/history	✓	✗	✓
Get Trade Volume	/v1/tradevolume	✓	✗	✓
Get Notional Volume	/v1/notionalvolume	✓	✗	✓
Heartbeat	/v1/heartbeat	✓	✗	✗
Get Available Balances	/v1/balances	✓	✓	✓
Get Notional Balances	v1/notionalbalances/:currency	✓	✓	✓
Get Deposit Addresses	/v1/addresses/:network	✓	✓	✓
New Deposit Address	/v1/deposit/:network/newAddress	✗	✓	✗
Transfers	/v1/transfers	✓	✓	✓
Custody Account Fees	/v1/custodyaccountfees	✓	✓	✓
Withdraw Crypto Funds	/v1/withdraw/:currency	✗	✓	✗
New Clearing Order	/v1/clearing/new	✓	✗	✗
Clearing Order Status	/v1/clearing/status	✓	✗	✓
Cancel Clearing Order	/v1/clearing/cancel	✓	✗	✗
Confirm Clearing Order	/v1/clearing/confirm	✓	✗	✗
Clearing Order List	/v1/clearing/list	✓	✗	✗
Clearing Broker List	/v1/clearing/broker/list	✓	✗	✗
Clearing Trades	/v1/clearing/trades	✓	✗	✗
Get Instant Quote	/v1/instant/quote	✓	✗	✗
Execute Instant Order	/v1/instant/execute	✓	✗	✗
Add A Bank	/v1/payments/addbank	✗	✓	✗
Add A Bank CAD	/v1/payments/addbank/cad	✗	✓	✗
View Payment Methods	/v1/payments/methods	✓	✓	✓
Account Detail	/v1/account	✓	✓	✓
List Approved Addresses	/v1/approvedAddresses/account/:network	✓	✓	✓
Create Approved Address	/v1/approvedAddresses/:network/request	✗	✓	✗
Remove Approved Address	/v1/approvedAddresses/:network/remove	✗	✓	✗
FX Rate	/v2/fxrate/:symbol/:timestamp	✗	✗	✓
Master Scoped Endpoints
Endpoint	URI	Administrator can access?	Trader can access?	Fund Manager can access?	Auditor can access?
Create Account	/v1/account/create	✓	✗	✗	✗
Rename Account	/v1/account/rename	✓	✗	✗	✗
Get Accounts	/v1/account/list	✓	✓	✓	✓
Transfer Between Accounts	/v1/account/transfer/:currency	✗	✗	✓	✗
Transactions	/v1/transactions	✓	✓	✓	✓





Error Codes

Copy page

If a response is in error, then the HTTP response code will be set to reflect this, and a JSON body will be returned that will contain information about the failure.

HTTP Error Codes
HTTP Status	Meaning
200	Request was successful
30x	API entry point has moved, see Location: header. Most likely an http: to https: redirect.
400	Market not open, or the request was malformed; in the case of a private API request, missing or malformed Gemini private API authentication headers
403	The API key is missing the role necessary to access this private API endpoint
404	Unknown API entry point or Order not found
406	Insufficient Funds
429	Rate Limiting was applied
500	The server encountered an error
502	Technical issues are preventing the request from being satisfied
503	The exchange is down for maintenance
Error payload
In the event of an error, a non-200 error code will be returned, and the response body will be a json object with three fields:

result, which will always be "error"
reason, which will be one of the strings listed in the table below
message, a human-readable English string indicating additional error information.
Reason	Meaning
ClientOrderIdTooLong	The Client Order ID must be under 100 characters
ClientOrderIdMustBeString	The Client Order ID must be a string
ConflictingOptions	New orders using a combination of order execution options are not supported
ConflictingAccountName	The specified name is already in use within the master group
EndpointMismatch	The request was submitted to an endpoint different than the one in the payload
EndpointNotFound	No endpoint was specified
GTSTradeIDMustBeString	The Clearing ID must be a string
InsufficientFunds	The order was rejected because of insufficient funds
InvalidJson	The JSON provided is invalid
InvalidNonce	The nonce was not greater than the previously used nonce or was not within +/- 30 seconds of Unix Epoch timestamp
InvalidOrderType	An unknown order type was provided
InvalidPrice	For new orders, the price was invalid
InvalidStopPrice	For new stop limit orders, the price was invalid
InvalidStopPriceSell	For new stop limit sell orders, the "stop_price" price was lower than the "sell" price
InvalidStopPriceBuy	For new stop limit buy orders, the "stop_price" price was greater than the "buy" price
InvalidStopPriceRatio	For new stop limit orders, the "buy" or "sell" price was not within 50% of the "stop_price"
InvalidQuantity	A negative or otherwise invalid quantity was specified
InvalidSide	For new orders, and invalid side was specified
InvalidSignature	The signature did not match the expected signature
InvalidSymbol	An invalid symbol was specified
InvalidTimestampInPayload	The JSON payload contained a timestamp parameter with an unsupported value.
InvalidAccountName	The specified name did not match any accounts within the master group
InvalidAccountType	The specified type did not match exchange or custody
InvalidFundTransfer	The fund transfer was not successful
Maintenance	The system is down for maintenance
MarketNotOpen	The order was rejected because the market is not accepting new orders
MissingAccountName	A required account name was not specified in a field requiring one
MissingAccounts	A required account field was not specified
MissingApikeyHeader	The X-GEMINI-APIKEY header was missing
MissingOrderField	A required order_id field was not specified
MissingRole	The API key used to access this endpoint does not have the required role assigned to it
MissingPayloadHeader	The X-GEMINI-PAYLOAD header was missing
MissingPayloadKey	The payload is missing a required key
MissingSignatureHeader	The X-GEMINI-SIGNATURE header was missing
MissingName	A required name field was not specified
MissingNonce	A nonce was not provided in the payload. See Private API Invocation for more detail.
MoreThanOneAccount	More than one account was specified on an API that only accepts a single account
AccountClosed	Account account is closed and cannot be used for this operation.
AccountsOnGroupOnlyApi	The account field was specified on a non-master API key
AccountLimitExceeded	The account field specified more than the maximum supported accounts for that API
NoAccountOfTypeRequired	The account field specified multiple accounts and some were not of the required account type
AccountNotOfTypeRequired	The account specified in the account field was not of the required account type
NotGroupApiCompatible	A master API key was used to invoke an account only API
ExceededMaxAccountsInGroup	An account could not be created as the master group already has the maximum number of allowed accounts in it
NoSSL	You must use HTTPS to access the API
OptionsMustBeArray	The options parameter must be an array.
OrderNotFound	The order specified was not found
RateLimit	Requests were made too frequently. See Rate Limits below.
System	We are experiencing technical issues
UnsupportedOption	This order execution option is not supported.
HasNotAgreedToCustodyTerms	The Group has not yet agreed to the Custody terms and conditions. Please visit https://exchange.gemini.com/custody to read the terms and conditions of custody accounts.
BadAccountType	The type parameter must contain a string of either exchange or custody.
RemoteAddressForbidden	Request received from an IP address that is not whitelisted under the group.
Last modified on February 25, 2026
Roles
Rate Limits
On this page
HTTP Error Codes
Error payload

Rate Limits

Copy page

To prevent abuse, Gemini imposes rate limits on incoming requests as described in the Gemini API Agreement.

For public API entry points, we limit requests to 120 requests per minute, and recommend that you do not exceed 1 request per second.

For private API entry points, we limit requests to 600 requests per minute, and recommend that you not exceed 5 requests per second.

How are rate limits applied?
When requests are received at a rate exceeding X requests per minute, we offer a "burst" rate of five additional requests that are queued but their processing is delayed until the request rate falls below the defined rate.

When you exceed the rate limit for a group of endpoints, you will receive a 429 Too Many Requests HTTP status response until your request rate drops back under the required limit.

Example: 600 requests per minute is ten requests per second, meaning one request every 0.1 second.

If you send 20 requests in close succession over two seconds, then you could expect:

the first ten requests are processed
the next five requests are queued
the next five requests receive a 429 response, meaning the rate limit for this group of endpoints has been exceeded
any further incoming request immediately receive a 429 response
after a short period of inactivity, the five queued requests are processed
following that, incoming requests begin to be processed at the normal rate again

Client Order ID

Copy page

Client order ID is a client-supplied order identifier that Gemini will echo back to you in all subsequent messages about that order.

Although this identifier is optional, Gemini strongly recommends supplying client_order_id when placing orders using the Create New Order endpoint.

This makes it easy to track the Order Events: Accepted and Order Events: Booked responses in your Order Events WebSocket subscription.

Visibility
Your client order ids are only visible to the Gemini exchange and you. They are never visible on any public API endpoints.

Uniqueness
Gemini recommends that your client order IDs should be unique per trading session.

Allowed characters
Your client order ids should match against this PCRE regular expression: [:\-_\.#a-zA-Z0-9]{1,36}.

Characters	Description	ASCII Codes (Dec)
A-Z	Uppercase A-Z	65 - 90
a-z	Lowercase a-z	97 - 122
0-9	Digits	48 - 57
#	Hash, octothorpe, number sign	35
-	Hyphen	45
.	Period	46
:	Colon	58
_	Underscore	95

Gemini Clearing

Copy page

Gemini Clearing allows two parties to settle a trade off the order book. The initiator enters the trade details for any supported symbol and generates a trade_id. If a counterparty_id is supplied, only the specified counterparty can confirm the order. If a counterparty_id is not supplied, the ticket will generate a trade_id that can filled by any counterparty.

Get Started
Account Administration Endpoints

Copy page

Account Detail
The account API will return detail about the specific account requested such as users, country codes, etc.

Roles
The API key you use to access this endpoint can be either a Master or Account level key with any role assigned. See Roles for more information.

Using Master API Keys
Gemini supports sub-account functionality which allows users to create multiple Gemini accounts off of their primary account. Administrators on the primary account can create a master API key via API Settings on the Gemini web UI.

Master API keys can be used for any account level endpoint as well if the proper roles are assigned to it. For example, if a master API key has the Administrator and Fund Manager roles assigned, the key can be used to check balances, create new deposit addresses and withdraw. The master API key will need to pass the account parameter in order to specify the account where the trade is placed.

An example of a Master Level API key performing at an account level on the balances endpoint.


























REST API
Market Data (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
List Symbols
GET
https://api.gemini.com
/v1/symbols
This endpoint retrieves all available symbols for trading.

List Symbols ›Responses
200
400
404
429
500
The full list of supported symbols.

string[]
GET/v1/symbols

cURL
curl --request GET \
  --url https://api.gemini.com/v1/symbols
shell

Example Responses

200
[
  "aavegusd",
  "aaveusd",
  "aligusd",
  "aliusd",
  "ampgusd",
  "ampusd",
  "ankrgusd",
  "ankrusd",
  "apegusd",
  "apeusd",
  "api3gusd",
  "api3usd",
  "arbgusd",
  "arbusd",
  "atomgusd",
  "atomusd",
  "avaxgusd",
  "avaxgusdperp",
  "avaxusd",
  "axsgusd",
  "axsusd",
  "batgusd",
  "batusd",
  "bchgusd",
  "bchgusdperp",
  "bchusd",
  "bnbgusdperp",
  "bomegusd",
  "bomegusdperp",
  "bomeusd",
  "bonkgusd",
  "bonkgusdperp",
  "bonkusd",
  "btceur",
  "btcgbp",
  "btcgusd",
  "btcgusdperp",
  "btcsgd",
  "btcusd",
  "btcusdt",
  "chillguygusd",
  "chillguyusd",
  "chzgusd",
  "chzusd",
  "compgusd",
  "compusd",
  "crvgusd",
  "crvusd",
  "ctxgusd",
  "ctxusd",
  "cubegusd",
  "cubeusd",
  "daigusd",
  "daiusd",
  "dogebtc",
  "dogeeth",
  "dogegusd",
  "dogegusdperp",
  "dogeusd",
  "dotgusd",
  "dotgusdperp",
  "dotusd",
  "efilfil",
  "elongusd",
  "elonusd",
  "ensgusd",
  "ensusd",
  "ethbtc",
  "etheur",
  "ethgbp",
  "ethgusd",
  "ethgusdperp",
  "ethsgd",
  "ethusd",
  "ethusdt",
  "fetgusd",
  "fetusd",
  "filgusd",
  "filusd",
  "flokigusd",
  "flokigusdperp",
  "flokiusd",
  "ftmgusd",
  "ftmusd",
  "galagusd",
  "galausd",
  "gmtgusd",
  "gmtusd",
  "goatgusd",
  "goatgusdperp",
  "goatusd",
  "grtgusd",
  "grtusd",
  "gusdgbp",
  "gusdsgd",
  "gusdusd",
  "hntgusd",
  "hntusd",
  "hypegusdperp",
  "imxgusd",
  "imxusd",
  "injgusd",
  "injgusdperp",
  "injusd",
  "iotxgusd",
  "iotxusd",
  "ksl2gusdperp",
  "kt5gusdperp",
  "ldogusd",
  "ldousd",
  "linkbtc",
  "linketh",
  "linkgusd",
  "linkgusdperp",
  "linkusd",
  "lptgusd",
  "lptusd",
  "lrcgusd",
  "lrcusd",
  "ltcbtc",
  "ltceth",
  "ltcgusd",
  "ltcgusdperp",
  "ltcusd",
  "managusd",
  "manausd",
  "maskgusd",
  "maskusd",
  "maticgusd",
  "maticusd",
  "mewgusd",
  "mewgusdperp",
  "mewusd",
  "mkrgusd",
  "mkrusd",
  "moodenggusd",
  "moodenggusdperp",
  "moodengusd",
  "opgusd",
  "opgusdperp",
  "opusd",
  "oxtgusd",
  "oxtusd",
  "paxggusd",
  "paxgusd",
  "pepegusd",
  "pepegusdperp",
  "pepeusd",
  "pnutgusd",
  "pnutgusdperp",
  "pnutusd",
  "polgusdperp",
  "popcatgusd",
  "popcatgusdperp",
  "popcatusd",
  "pythgusd",
  "pythgusdperp",
  "pythusd",
  "qntgusd",
  "qntusd",
  "raregusd",
  "rareusd",
  "rengusd",
  "renusd",
  "rlusdusd",
  "rndrgusd",
  "rndrusd",
  "samogusd",
  "samousd",
  "sandgusd",
  "sandusd",
  "shibgusd",
  "shibgusdperp",
  "shibusd",
  "sklgusd",
  "sklusd",
  "solbtc",
  "soleth",
  "solgusd",
  "solgusdperp",
  "solusd",
  "storjgusd",
  "storjusd",
  "sushigusd",
  "sushiusd",
  "trumpgusdperp",
  "umagusd",
  "umausd",
  "unigusd",
  "unigusdperp",
  "uniusd",
  "usdcusd",
  "usdtgusd",
  "usdtusd",
  "wifgusd",
  "wifgusdperp",
  "wifusd",
  "xrpgusd",
  "xrpgusdperp",
  "xrpusd",
  "xtzgusd",
  "xtzusd",
  "yfigusd",
  "yfiusd",
  "zecgusd",
  "zecusd",
  "zrxgusd",
  "zrxusd"
]
json
application/json
Get Symbol Details
GET
https://api.gemini.com
/v1/symbols/details/{symbol}
This endpoint retrieves extra detail on supported symbols, such as minimum order size, tick size, quote increment and more.

Get Symbol Details ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

Get Symbol Details ›Responses
200
400
404
429
500
Instrument responses examples

symbolstring
The requested symbol. See symbols and minimums

Example: BTCUSD
base_currencystring
CCY1 or the top currency. (i.e BTC in BTCUSD)

Example: BTC
quote_currencystring
CCY2 or the quote currency. (i.e USD in BTCUSD)

Example: USD
tick_sizenumber · decimal
The number of decimal places in the base_currency. (i.e 1e-8)

Example: 1e-8
quote_incrementnumber · decimal
The number of decimal places in the quote_currency (i.e 0.01)

Example: 0.01
min_order_sizestring
The minimum order size in base_currency units (i.e 0.00001)

Example: 0.00001
statusstring
Status of the current order book. Can be open, closed, cancel_only, post_only, limit_only.

Example: open
wrap_enabledboolean
When True, symbol can be wrapped using this endpoint:
POST https://api.gemini.com/v1/wrap/:symbol

Example: false
product_typestring
Instrument type spot / swap -- where swap signifies perpetual swap.

Example: spot
contract_typestring
vanilla / linear / inverse where vanilla is for spot while linear is for perpetual swap and inverse is a special case perpetual swap where the perpetual contract will be settled in base currency.

Example: vanilla
contract_price_currencystring
CCY2 or the quote currency for spot instrument (i.e. USD in BTCUSD) Or collateral currency of the contract in case of perpetual swap instrument.

Example: USD
GET/v1/symbols/details/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/symbols/details/:symbol
shell

Example Responses

200
{
  "symbol": "BTCUSD",
  "base_currency": "BTC",
  "quote_currency": "USD",
  "tick_size": 1e-8,
  "quote_increment": 0.01,
  "min_order_size": "0.00001",
  "status": "open",
  "wrap_enabled": false,
  "product_type": "spot",
  "contract_type": "vanilla",
  "contract_price_currency": "USD"
}
json
Spot instrument response
application/json

Spot instrument
Get Network
GET
https://api.gemini.com
/v1/network/{token}
This endpoint retrieves the associated network(s) for a requested token.

Many tokens are available on multiple blockchain networks. For example, USDC is available on Optimism, Solana, Base, Arbitrum, Monad, Avalanche, and Ethereum. Use this endpoint to discover which networks support deposits and withdrawals for a given token.

The network field in the response is always an array, which may contain one or more supported networks.

Get Network ›path Parameters
tokenstring · required
Token identifier. BTC, ETH, USDC, SOL etc. See symbols and minimums

Get Network ›Responses
200
400
404
429
500
The response will be a JSON object

tokenstring
The requested token identifier.

networkstring[]
Array of supported blockchain networks for the token. Many tokens (especially stablecoins like USDC, USDT) are available on multiple networks.

Supported networks include: bitcoin, ethereum, solana, optimism, arbitrum, base, monad, avalanche, litecoin, bitcoincash, dogecoin, zcash, filecoin, tezos, polkadot, cosmos, xrpl, linea, and more.

Example: ["optimism","solana","base","arbitrum","monad","avalanche","ethereum"]
GET/v1/network/{token}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/network/:token
shell

Example Responses

200
{
  "token": "BTC",
  "network": [
    "bitcoin"
  ]
}
json
application/json

Single network token (BTC)
Get Ticker
GET
https://api.gemini.com
/v1/pubticker/{symbol}
This endpoint retrieves information about recent trading activity for the symbol.

We recommend using Version 2 to retrieve recent ticker activty.

Get Ticker ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

Get Ticker ›Responses
200
400
404
429
500
The current ticker for the symbol

bidnumber · decimal
The highest bid currently available

Example: 977.59
asknumber · decimal
The lowest ask currently available

Example: 977.35
lastnumber · decimal
The price of the last executed trade

Example: 977.65
volumeobject
Information about the 24 hour volume on the exchange. See properties below


GET/v1/pubticker/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/pubticker/:symbol
shell

Example Responses

200
{
  "bid": "977.59",
  "ask": "977.35",
  "last": "977.65",
  "volume": {
    "BTC": "2210.505328803",
    "USD": "2135477.463379586263",
    "timestamp": 1483018200000
  }
}
json
application/json
List Fee Promos
GET
https://api.gemini.com
/v1/feepromos
This endpoint retrieves symbols that currently have fee promos.

List Fee Promos ›Responses
200
400
404
429
500
The response will be a JSON object

symbolsstring[]
Symbols that currently have fee promos

GET/v1/feepromos

cURL
curl --request GET \
  --url https://api.gemini.com/v1/feepromos
shell

Example Responses

200
{
  "symbols": [
    "PNUTGUSDPERP",
    "WIFGUSDPERP",
    "PYTHGUSDPERP",
    "MEWGUSDPERP",
    "BONKGUSDPERP",
    "BCHGUSDPERP",
    "BTCGUSDPERP",
    "BUSDUSD",
    "POLGUSDPERP",
    "FRAXUSD",
    "OPGUSDPERP",
    "DOTGUSDPERP",
    "TRUMPGUSDPERP",
    "GUSDGBP",
    "USDTUSD",
    "POPCATGUSDPERP",
    "FLOKIGUSDPERP",
    "MOODENGGUSDPERP",
    "LINKGUSDPERP",
    "ETHGUSDPERP",
    "UNIGUSDPERP",
    "MATICGUSDPERP",
    "USDTGUSD",
    "BNBGUSDPERP",
    "MIMUSD",
    "KSL2GUSDPERP",
    "LUSDUSD",
    "SHIBGUSDPERP",
    "AVAXGUSDPERP",
    "BOMEGUSDPERP",
    "USDCUSD",
    "HYPEGUSDPERP",
    "MOGGUSDPERP",
    "KT5GUSDPERP",
    "SOLGUSDPERP",
    "PEPEGUSDPERP",
    "DOGEGUSDPERP",
    "GUSDSGD",
    "INJGUSDPERP",
    "LTCGUSDPERP",
    "XRPGUSDPERP",
    "USTUSD",
    "GOATGUSDPERP",
    "DAIUSD"
  ]
}
json
application/json
Get Current Order Book
GET
https://api.gemini.com
/v1/book/{symbol}
This will return the current order book as two arrays (bids / asks).

The quantities and prices returned are returned as strings rather than numbers. The numbers returned are exact, not rounded, and it can be dangerous to treat them as floating point numbers.

Get Current Order Book ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

Get Current Order Book ›query Parameters
limit_bidsnumber · min: 1
Limit the number of bid (offers to buy) price levels returned. Default is 50. May be 0 to return the full order book on this side.

limit_asksnumber · min: 1
Limit the number of ask (offers to sell) price levels returned. Default is 50. May be 0 to return the full order book on this side.

Get Current Order Book ›Responses
200
400
404
429
500
The response will be two arrays. The bids and the asks are grouped by price, so each entry may represent multiple orders at that price. Each element of the array will be a JSON object.

bidsobject[]
The bid price levels currently on the book. These are offers to buy at a given price.


asksobject[]
The ask price levels currently on the book. These are offers to sell at a given price.


GET/v1/book/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/book/:symbol
shell

Example Responses

200
{
  "bids": [
    {
      "price": "3607.85",
      "amount": "6.643373",
      "timestamp": "1547147541"
    }
  ],
  "asks": [
    {
      "price": "3607.86",
      "amount": "14.68205084",
      "timestamp": "1547147541"
    }
  ]
}
json
application/json
List Trades
GET
https://api.gemini.com
/v1/trades/{symbol}
This public API endpoint is limited to retrieving seven calendar days of data.
Please contact us through this form for information about Gemini market data.
This will return the trades that have executed since the specified timestamp. Timestamps are either seconds or milliseconds since the epoch (1970-01-01). See the Data Types section about timestamp for information on this.

Each request will show at most 500 records.

If no since or timestamp is specified, then it will show the most recent trades; otherwise, it will show the most recent trades that occurred after that timestamp.

List Trades ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

List Trades ›query Parameters
timestamp
Only return trades after this timestamp. See Timestamps for more information. If not present, will show the most recent trades. For backwards compatibility, you may also use the alias since. With timestamp, there is a 90-day hard limit.

Timestamp in milliseconds

since_tidnumber
Only retuns trades that executed after this tid. since_tid trumps timestamp parameter which has no effect if provided too. You may set since_tid to zero to get the earliest available trade history data.

limit_tradesnumber · min: 0
The maximum number of trades to return. The default is 50.

Default: 50
include_breaksboolean
Whether to display broken trades. False by default. Can be 1 or true to activate

Default: false
List Trades ›Responses
200
400
404
429
500
The response will be an array of JSON objects, sorted by timestamp, with the newest trade shown first.

object[]

timestamp
timestamp


timestampms
timestamp


tidinteger
The trade ID number

Example: 5335307668
pricestring · decimal
The price the trade was executed at

Example: 3610.85
amountstring · decimal
The amount that was traded

Example: 0.27413495
exchangestring
Will always be "gemini"

Example: gemini
typestring · enum
buy means that an ask was removed from the book by an incoming buy order.
sell means that a bid was removed from the book by an incoming sell order.
Enum values:
buy
sell
Example: buy
brokenboolean
Whether the trade was broken or not. Broken trades will not be displayed by default; use the include_breaks to display them.

Example: false
GET/v1/trades/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/trades/:symbol
shell

Example Responses

200
{
  "timestamp": 1547146811,
  "timestampms": 1547146811357,
  "tid": 5335307668,
  "price": "3610.85",
  "amount": "0.27413495",
  "exchange": "gemini",
  "type": "buy",
  "broken": true
}
json
application/json
List Prices
GET
https://api.gemini.com
/v1/pricefeed
List Prices ›Responses
200
400
404
429
500
Response is a list of objects, one for each pair.

object[]

pairstring
Trading pair symbol. See symbols and minimums

pricestring
Current price of the pair on the Gemini order book

percentChange24hstring
24 hour change in price of the pair on the Gemini order book

GET/v1/pricefeed

cURL
curl --request GET \
  --url https://api.gemini.com/v1/pricefeed
shell

Example Responses

200
[
  {
    "pair": "BTCUSD",
    "price": "9500.00",
    "percentChange24h": "5.23"
  },
  {
    "pair": "ETHUSD",
    "price": "257.54",
    "percentChange24h": "4.85"
  },
  {
    "pair": "BCHUSD",
    "price": "450.10",
    "percentChange24h": "-2.91"
  },
  {
    "pair": "LTCUSD",
    "price": "79.50",
    "percentChange24h": "7.63"
  }
]
json
application/json
Get Funding Amount
GET
https://api.gemini.com
/v1/fundingamount/{symbol}
Get Funding Amount ›path Parameters
symbolstring · required
Trading pair symbol


BTCGUSDPERP, etc. See symbols and minimums.

Get Funding Amount ›Responses
200
400
404
429
500
The response will be an object

symbolstring
The requested symbol. See symbols and minimums

fundingDateTimestring
UTC date time in format yyyy-MM-ddThh:mm:ss.SSSZ format

fundingTimestampMilliSecsnumber · long
Current funding amount Epoc time.

nextFundingTimestampnumber · long
Next funding amount Epoc time.

amountnumber · decimal
The dollar amount for a Long 1 position held in the symbol for funding period (1 hour)

estimatedFundingAmountnumber · decimal
The estimated dollar amount for a Long 1 position held in the symbol for next funding period (1 hour)

GET/v1/fundingamount/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v1/fundingamount/:symbol
shell

Example Responses

200
{
  "symbol": "BTCGUSDPERP",
  "fundingDateTime": "2025-04-22T18:00:00.000Z",
  "fundingTimestampMilliSecs": 1745344800000,
  "nextFundingTimestamp": 1745348400000,
  "fundingAmount": -1.50991,
  "estimatedFundingAmount": -2.10595
}
json
application/json
Get Funding Amount Report File
GET
https://api.gemini.com
/v1/fundingamountreport/records.xlsx
Examples
symbol=BTCGUSDPERP&fromDate=2024-04-10&toDate=2024-04-25&numRows=1000
Compare and obtain the minimum records between (2024-04-10 to 2024-04-25) and 1000. If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch the minimum between 360 and 1000 records only.

symbol=BTCGUSDPERP&numRows=2024-04-10&toDate=2024-04-25
If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch 360 records only.

symbol=BTCGUSDPERP&numRows=1000
Fetch maximum 1000 records starting from Now to a historical date

symbol=BTCGUSDPERP
Fetch maximum 8760 records starting from Now to a historical date

Get Funding Amount Report File ›query Parameters
symbolstring · required
Trading pair symbol


BTCGUSDPERP, etc. See symbols and minimums.

fromDatestring · date
Mandatory if toDate is specified, else optional. If empty, will only fetch records by numRows value.

toDatestring · date
Mandatory if fromDate is specified, else optional. If empty, will only fetch records by numRows value.

numRowsinteger
If empty, default value '8760'

Get Funding Amount Report File ›Responses
200
400
404
429
500

application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
The response will be an excel / csv file. filename=FundingAmount_{SYMBOL}.{xlsx,csv}

string
GET/v1/fundingamountreport/records.xlsx

cURL
curl --request GET \
  --url 'https://api.gemini.com/v1/fundingamountreport/records.xlsx?symbol=%3Cstring%3E'
shell

Example Responses

200
No example specified for this content type

application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
Get Ticker V2
GET
https://api.gemini.com
/v2/ticker/{symbol}
This endpoint retrieves information about recent trading activity for the provided symbol.

Get Ticker V2 ›path Parameters
symbolstring · required
Trading pair symbol

Get Ticker V2 ›Responses
200
400
404
429
500
Successful response

symbolstring
The trading pair symbol

Example: BTCUSD
openstring · decimal
Open price from 24 hours ago

Example: 9121.76
highstring · decimal
High price from 24 hours ago

Example: 9440.66
lowstring · decimal
Low price from 24 hours ago

Example: 9106.51
closestring · decimal
Close price (most recent trade)

Example: 9347.66
changesstring[]
Hourly prices descending for past 24 hours

Example: ["9365.1","9386.16","9373.41","9322.56","9268.89","9265.38"]
bidstring · decimal
Current best bid

Example: 9345.70
askstring · decimal
Current best offer

Example: 9347.67
GET/v2/ticker/{symbol}

cURL
curl --request GET \
  --url https://api.gemini.com/v2/ticker/:symbol
shell

Example Responses

200
{
  "symbol": "BTCUSD",
  "open": "9121.76",
  "high": "9440.66",
  "low": "9106.51",
  "close": "9347.66",
  "changes": [
    "9365.1",
    "9386.16",
    "9373.41",
    "9322.56",
    "9268.89",
    "9265.38",
    "9245",
    "9231.43",
    "9235.88",
    "9265.8",
    "9295.18",
    "9295.47",
    "9310.82",
    "9335.38",
    "9344.03",
    "9261.09",
    "9265.18",
    "9282.65",
    "9260.01",
    "9225",
    "9159.5",
    "9150.81",
    "9118.6",
    "9148.01"
  ],
  "bid": "9345.70",
  "ask": "9347.67"
}
json
application/json
List Candles
GET
https://api.gemini.com
/v2/candles/{symbol}/{time_frame}
This endpoint retrieves time-intervaled data for the provided symbol.

List Candles ›path Parameters
symbolstring · required
Trading pair symbol

time_framestring · enum · required
Time range for each candle:

1m - 1 minute
5m - 5 minutes
15m - 15 minutes
30m - 30 minutes
1h - 1 hour
6h - 6 hours
1day - 1 day
Enum values:
1m
5m
15m
30m
1h
6h
1d
List Candles ›Responses
200
400
404
429
500
The response will be an array of arrays

Candlearray

GET/v2/candles/{symbol}/{time_frame}

cURL
curl --request GET \
  --url https://api.gemini.com/v2/candles/:symbol/:time_frame
shell

Example Responses

200
[
  [
    1559755800000,
    7781.6,
    7820.23,
    7776.56,
    7819.39,
    34.7624802159
  ],
  [
    1559755800000,
    7781.6,
    7829.46,
    7776.56,
    7817.28,
    43.4228281059
  ]
]
json
application/json
List Derivative Candles
GET
https://api.gemini.com
/v2/derivatives/candles/{symbol}/{time_frame}
This endpoint retrieves time-intervaled data for the provided perpetual symbol.

List Derivative Candles ›path Parameters
symbolstring · required
Trading pair symbol. Available only for perpetual pairs like BTCGUSDPERP

time_framestring · enum · required
Time range for each candle. 1m: 1 minute (only)

Enum values:
1m
List Derivative Candles ›Responses
200
400
404
429
500
The response will be an array of arrays

Candlearray

GET/v2/derivatives/candles/{symbol}/{time_frame}

cURL
curl --request GET \
  --url https://api.gemini.com/v2/derivatives/candles/:symbol/:time_frame
shell

Example Responses

200
[
  [
    1714126740000,
    68038,
    68038,
    68038,
    68038,
    0
  ],
  [
    1714126680000,
    68038,
    68038,
    68038,
    68038,
    0
  ]
]
json
application/json
FX Rate
GET
https://api.gemini.com
/v2/fxrate/{symbol}/{timestamp}
We have a growing international institutional customer base. When pulling market data for charting, it can be useful to have access to our FX rate for the relevant currency at that time.

Please note, Gemini does not offer foreign exchange services. This endpoint is for historical reference only and does not provide any guarantee of future exchange rates.

Roles
The API key you use to access this endpoint must have the Auditor role assigned. See Roles for more information.

Supported Pairs

[AUDUSD, CADUSD, COPUSD, EURUSD, CHFUSD, HKDUSD, NZDUSD, GBPUSD, BRLUSD, INRUSD, SGDUSD, KRWUSD, JPYUSD, CNYUSD]

FX Rate ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

timestamprequired
The timestamp to pull the FX rate for.

Gemini strongly recommends using milliseconds instead of seconds for timestamps.

timestamp

FX Rate ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
FX Rate ›Responses
200
400
401
403
404
429
500
Successful operation

fxPairstring
The requested currency pair

Example: AUDUSD
ratenumber · double
The exchange rate

Example: 0.69
asOf
timestamp


providerstring
The market data provider

Example: bcb
benchmarkstring
The market for which the retrieved price applies to

Example: Spot
GET/v2/fxrate/{symbol}/{timestamp}

cURL

curl --request GET \
  --url https://api.gemini.com/v2/fxrate/:symbol/:timestamp \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>'
shell

Example Responses

200
{
  "fxPair": "AUDUSD",
  "rate": "0.69",
  "asOf": 1594651859000,
  "provider": "bcb",
  "benchmark": "Spot"
}
json
application/json



Create New Order
POST
https://api.gemini.com
/v1/order/new
If you wish orders to be automatically cancelled when your session ends, see the require heartbeat section, or manually send the cancel all session orders message.

Master API keys do not support cancelation on disconnect via heartbeat.
Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards.

Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Margin Orders
Set margin_order: true to place an order using borrowed funds on a margin-enabled account. This allows you to trade with leverage beyond your available balance.

Important: Margin trading amplifies both gains and losses. Monitor your account using the Margin Account Summary endpoint and preview order impacts with Order Preview before placing margin orders.

Stop-Limit Orders
A Stop-Limit order is an order type that allows for order placement when a price reaches a specified level. Stop-Limit orders take in both a price and and a stop_price as parameters. The stop_price is the price that triggers the order to be placed on the continous live order book at the price. For buy orders, the stop_price must be below the price while sell orders require the stop_price to be greater than the price.

What about market orders?
The API doesn't directly support market orders because they provide you with no price protection.

Instead, use the “immediate-or-cancel” order execution option, coupled with an aggressive limit price (i.e. very high for a buy order or very low for a sell order), to achieve the same result.

Order execution options
Note that options is an array. If you omit options or provide an empty array, your order will be a standard limit order - it will immediately fill against any open orders at an equal or better price, then the remainder of the order will be posted to the order book.

If you specify more than one option (or an unsupported option) in the options array, the exchange will reject your order.

No options can be applied to stop-limit orders at this time.

The available limit order options are:

Option	Description
"maker-or-cancel"	This order will only add liquidity to the order book.

If any part of the order could be filled immediately, the whole order will instead be canceled before any execution occurs.

If that happens, the response back from the API will indicate that the order has already been canceled ("is_cancelled": true in JSON).

Note: some other exchanges call this option "post-only".
"immediate-or-cancel"	This order will only remove liquidity from the order book.

It will fill whatever part of the order it can immediately, then cancel any remaining amount so that no part of the order is added to the order book.

If the order doesn't fully fill immediately, the response back from the API will indicate that the order has already been canceled ("is_cancelled": true in JSON).
"fill-or-kill"	This order will only remove liquidity from the order book.

It will fill the entire order immediately or cancel.

If the order doesn't fully fill immediately, the response back from the API will indicate that the order has already been canceled ("is_cancelled": true in JSON).
Create New Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Order ›Request Body
requeststring · required
The literal string "/v1/order/new"

Example: /v1/order/new
noncenumber · required
The nonce, as described in Private API Invocation

symbolstring · required
The symbol for the new order

Example: BTCUSD
amountstring · required
Quoted decimal amount to purchase

Example: 5
pricestring · required
Quoted decimal amount to spend per unit

Example: 3633.00
sidestring · enum · required
Enum values:
buy
sell
Example: buy
typestring · enum · required
The order type. "exchange limit" for all order types except for stop-limit orders. "exchange stop limit" for stop-limit orders.

Enum values:
exchange limit
exchange stop limit
exchange market
Example: exchange limit
client_order_idstring
Recommended. A client-specified order id

optionsstring[]
An optional array containing at most one supported order execution option. See Order execution options for details.

Enum values:
maker-or-cancel
immediate-or-cancel
fill-or-kill
Example: ["maker-or-cancel"]
stop_pricestring
The price to trigger a stop-limit order. Only available for stop-limit orders.

margin_orderboolean
Set to true to place this order on a margin account using borrowed funds. Defaults to false. Only available for margin-enabled accounts. See Margin Trading for details.

Example: false
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Create New Order ›Responses
200
400
401
403
404
429
500
Response will be the fields included in Order Status

oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Limit Order Response	type = object
Stop-Limit Order Response	type = object
Properties for Limit Order Response:
order_idstring
idstring
symbolstring
exchangestring
avg_execution_pricestring
sidestring · enum
Enum values:
buy
sell
typestring · enum
Enum values:
exchange limit
exchange stop limit
exchange market
timestamp
timestamp


timestampms
timestamp


is_liveboolean
is_cancelledboolean
is_hiddenboolean
was_forcedboolean
executed_amountstring
remaining_amountstring · double
client_order_idstring
optionsstring[]
pricestring · double
original_amountstring · double
POST/v1/order/new

cURL
curl --request POST \
  --url https://api.gemini.com/v1/order/new \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/order/new",
  "nonce": "<nonce>",
  "client_order_id": "470135",
  "symbol": "BTCUSD",
  "amount": "5",
  "price": "3633.00",
  "side": "buy",
  "type": "exchange limit"
}
'
shell

Example Request Body
{
  "request": "/v1/order/new",
  "nonce": "<nonce>",
  "client_order_id": "470135",
  "symbol": "BTCUSD",
  "amount": "5",
  "price": "3633.00",
  "side": "buy",
  "type": "exchange limit"
}
json
JSON limit order payload
application/json

Limit Order

Example Responses

200
{
  "order_id": "106817811",
  "id": "106817811",
  "symbol": "BTCUSD",
  "exchange": "gemini",
  "avg_execution_price": "3632.8508430064554",
  "side": "buy",
  "type": "exchange limit",
  "timestamp": "1547220404",
  "timestampms": 1547220404836,
  "is_live": true,
  "is_cancelled": false,
  "is_hidden": false,
  "was_forced": false,
  "executed_amount": "3.7567928949",
  "remaining_amount": "1.2432071051",
  "client_order_id": "20190110-4738721",
  "options": [],
  "price": "3633.00",
  "original_amount": "5"
}
json
JSON limit order response
application/json

Limit Order
Cancel Order
POST
https://api.gemini.com
/v1/order/cancel
This will cancel an order. If the order is already canceled, the message will succeed but have no effect.

Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards.
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

All Cancellation Reasons
Under unique circumstances, orders may be automatically cancelled by the exchange. These scenarios are detailed in the table below:

Cancel Reason	Description
MakerOrCancelWouldTake	Occurs when the "maker-or-cancel" execution option is included in the order request and any part of the requested order could be filled immediately.
ExceedsPriceLimits	Occurs when there is not sufficient liquidity on the order book to support the entered trade. Orders will be automatically cancelled when liquidity conditions are such that the order would move price +/- 5%.
SelfCrossPrevented	Occurs when a user enters a bid that is higher than that user's lowest open ask or enters an ask that is lower than their highest open bid on the same pair.
ImmediateOrCancelWouldPost	Occurs when the "immediate-or-cancel" execution option is included in the order request and the requested order cannot be fully filled immediately. This type of cancellation will only cancel the unfulfilled part of any impacted order.
FillOrKillWouldNotFill	Occurs when the "fill-or-kill" execution option is included in the new order request and the entire order cannot be filled immediately.

Unlike "immediate-or-cancel" orders, this execution option will result in the entire order being cancelled rather than just the unfulfilled portion.
Requested	Cancelled via user request to /v1/order/cancel endpoint.
MarketClosed	Occurs when an order is placed for a trading pair that is currently closed.
TradingClosed	Occurs when an order is placed while the exchange is closed for trading.
Cancel Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Cancel Order ›Request Body
requeststring · required
The literal string "/v1/order/cancel"

Example: /v1/order/cancel
noncerequired
timestamp


order_idinteger · required
The order ID given by /order/new

Example: 106817811
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the order. Only available for exchange accounts.

Example: primary
Cancel Order ›Responses
200
400
401
403
404
429
500
Response will be the fields included in Order Status. If the order was already canceled, then the request will have no effect and the status will be returned. Note the is_cancelled node will have a value of 'true'

order_idstring · integer
idstring · integer
symbolstring
exchangestring
avg_execution_pricestring · double
sidestring · enum
Enum values:
buy
sell
typestring · enum
Enum values:
exchange limit
exchange stop limit
exchange market
timestamp
timestamp


timestampms
timestamp


is_liveboolean
is_cancelledboolean
is_hiddenboolean
was_forcedboolean
executed_amountstring · double
remaining_amountstring · double
reasonstring · enum
Enum values:
MakerOrCancelWouldTake
ExceedsPriceLimits
SelfCrossPrevented
ImmediateOrCancelWouldPost
FillOrKillWouldNotFill
Requested
MarketClosed
TradingClosed
optionsstring[]
pricestring · double
original_amountstring · double
POST/v1/order/cancel

cURL
curl --request POST \
  --url https://api.gemini.com/v1/order/cancel \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/order/cancel",
  "nonce": "<nonce>",
  "order_id": 106817811
}
'
shell

Example Request Body
{
  "request": "/v1/order/cancel",
  "nonce": "<nonce>",
  "order_id": 106817811
}
json
JSON payload to cancel an order using its order_id
application/json

Example Responses

200
{
  "order_id": "106817811",
  "id": "106817811",
  "symbol": "btcusd",
  "exchange": "gemini",
  "avg_execution_price": "3632.85101103",
  "side": "buy",
  "type": "exchange limit",
  "timestamp": "1495742383",
  "timestampms": 1495742383345,
  "is_live": false,
  "is_cancelled": true,
  "is_hidden": false,
  "was_forced": false,
  "executed_amount": "3.7610296649",
  "remaining_amount": "1.2389703351",
  "reason": "Requested",
  "options": [],
  "price": "2960.00",
  "original_amount": "5"
}
json
JSON response for a cancelled order
application/json
Cancel All Active Orders
POST
https://api.gemini.com
/v1/order/cancel/all
This will cancel all outstanding orders created by all sessions owned by this account, including interactive orders placed through the UI.

Note that this cancels orders that were not placed using this API key. Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards.
Typically Cancel All Session Orders is preferable, so that only orders related to the current connected session are cancelled.

Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Cancel All Active Orders ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Cancel All Active Orders ›Request Body
requeststring · required
The literal string "/v1/order/cancel/all"

Example: /v1/order/cancel/all
noncerequired
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the orders. Only available for exchange accounts.

Example: primary
Cancel All Active Orders ›Responses
200
400
401
403
404
429
500
JSON response

resultstring
detailsobject
cancelledOrders/cancelRejects with IDs of both


POST/v1/order/cancel/all

cURL
curl --request POST \
  --url https://api.gemini.com/v1/order/cancel/all \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/order/cancel/all",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/order/cancel/all",
  "nonce": "<nonce>"
}
json
JSON payload to cancel all orders
application/json

Example Responses

200
{
  "result": "ok",
  "details": {
    "cancelRejects": [],
    "cancelledOrders": [
      330429106,
      330429079,
      330429082
    ]
  }
}
json
application/json
Cancel All Session Orders
POST
https://api.gemini.com
/v1/order/cancel/session
This will cancel all orders opened by this session.

This will have the same effect as heartbeat expiration if "Require Heartbeat" is selected for the session.

Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Cancel All Session Orders ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Cancel All Session Orders ›Request Body
requeststring · required
The literal string "/v1/order/cancel/session"

Example: /v1/order/cancel/session
noncerequired
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the orders. Only available for exchange accounts.

Example: primary
Cancel All Session Orders ›Responses
200
400
401
403
404
429
500
JSON response

resultstring
detailsobject
cancelledOrders/cancelRejects with IDs of both


POST/v1/order/cancel/session

cURL
curl --request POST \
  --url https://api.gemini.com/v1/order/cancel/session \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/order/cancel/session",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/order/cancel/session",
  "nonce": "<nonce>"
}
json
JSON payload to cancel all orders opened by this session
application/json

Example Responses

200
{
  "result": "ok",
  "details": {
    "cancelRejects": [
      330429345
    ],
    "cancelledOrders": []
  }
}
json
application/json
Get Order Status
POST
https://api.gemini.com
/v1/order/status
Gemini recommends using our WebSocket Order Events API to receive order status changes. It's much better because you'll be notified of order status changes as they happen.
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.

Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards. Trade info for all perpetuals orders submitted prior to this timing, will not be available through this API.

Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Order Status ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Order Status ›Request Body
requeststring · required
The API endpoint path

Example: /v1/order/status
noncerequired
timestamp


order_idinteger · required
The order id to get information on. The order_id represents a whole number and is transmitted as an unsigned 64-bit integer in JSON format. order_id cannot be used in combination with client_order_id.

Example: 123456789012345
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
client_order_idstring
The client_order_id used when placing the order. client_order_id cannot be used in combination with order_id

include_tradesboolean
Either True or False. If True the endpoint will return individual trade details of all fills from the order.

Get Order Status ›Responses
200
400
401
403
404
429
500
The order status

order_idstring · integer
The order id

client_order_idstring · integer
An optional client-specified order id

symbolstring
The symbol of the order

exchangestring
Will always be "gemini"

pricestring · decimal
The price the order was issued at

avg_execution_pricestring · decimal
The average price at which this order as been executed so far. 0 if the order has not been executed at all.

sidestring · enum
Enum values:
buy
sell
typestring · enum
Description of the order

Enum values:
exchange limit
exchange stop limit
exchange market
optionsstring[]
An array containing at most one supported order execution option. See Order execution options for details.

timestamp
timestamp


timestampms
timestamp


is_liveboolean
true if the order is active on the book (has remaining quantity and has not been canceled)

is_cancelledboolean
true if the order has been canceled. Note the spelling, "cancelled" instead of "canceled". This is for compatibility reasons.

reasonstring
Populated with the reason your order was canceled, if available.

was_forcedboolean
Will always be false.

executed_amountstring · decimal
The amount of the order that has been filled.

remaining_amountstring · decimal
The amount of the order that has not been filled.

original_amountstring · decimal
The originally submitted amount of the order.

is_hiddenboolean
Will always return false.

tradesobject[]
Contains an array of JSON objects with trade details.


POST/v1/order/status

cURL
curl --request POST \
  --url https://api.gemini.com/v1/order/status \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/order/status",
  "nonce": "<nonce>",
  "order_id": 123456789012345,
  "include_trades": true
}
'
shell

Example Request Body
{
  "request": "/v1/order/status",
  "nonce": "<nonce>",
  "order_id": 123456789012345,
  "include_trades": true
}
json
application/json

Example Responses

200
{
  "order_id": "123456789012345",
  "id": "123456789012345",
  "symbol": "btcusd",
  "exchange": "gemini",
  "avg_execution_price": "400.00",
  "side": "buy",
  "type": "exchange limit",
  "timestamp": "1494870642",
  "timestampms": 1494870642156,
  "is_live": false,
  "is_cancelled": false,
  "is_hidden": false,
  "was_forced": false,
  "executed_amount": "3",
  "remaining_amount": "0",
  "options": [],
  "price": "400.00",
  "original_amount": "3"
}
json
JSON response for limit buy
application/json

Limit Buy Response
List Active Orders
POST
https://api.gemini.com
/v1/orders
Gemini recommends using our WebSocket Order Events API to maintain a current view of your active orders. It's both faster and more efficient than polling this endpoint.
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.

Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards.

Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

List Active Orders ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Active Orders ›Request Body
requeststring · required
The API endpoint path

Example: /v1/orders
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
List Active Orders ›Responses
200
400
401
403
404
429
500
The active orders

object[]

order_idstring · integer
The order id

client_order_idstring · integer
An optional client-specified order id

symbolstring
The symbol of the order

exchangestring
Will always be "gemini"

pricestring · decimal
The price the order was issued at

avg_execution_pricestring · decimal
The average price at which this order as been executed so far. 0 if the order has not been executed at all.

sidestring · enum
Enum values:
buy
sell
typestring · enum
Description of the order

Enum values:
exchange limit
exchange stop limit
exchange market
optionsstring[]
An array containing at most one supported order execution option. See Order execution options for details.

timestamp
timestamp


timestampms
timestamp


is_liveboolean
true if the order is active on the book (has remaining quantity and has not been canceled)

is_cancelledboolean
true if the order has been canceled. Note the spelling, "cancelled" instead of "canceled". This is for compatibility reasons.

reasonstring
Populated with the reason your order was canceled, if available.

was_forcedboolean
Will always be false.

executed_amountstring · decimal
The amount of the order that has been filled.

remaining_amountstring · decimal
The amount of the order that has not been filled.

original_amountstring · decimal
The originally submitted amount of the order.

is_hiddenboolean
Will always return false.

tradesobject[]
Contains an array of JSON objects with trade details.


POST/v1/orders

cURL
curl --request POST \
  --url https://api.gemini.com/v1/orders \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/orders",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/orders",
  "nonce": "<nonce>"
}
json
Basic request to get active orders
application/json

Basic Request

Example Responses

200
[
  {
    "order_id": "107421210",
    "id": "107421210",
    "symbol": "ethusd",
    "exchange": "gemini",
    "avg_execution_price": "0.00",
    "side": "sell",
    "type": "exchange limit",
    "timestamp": "1547241628",
    "timestampms": 1547241628042,
    "is_live": true,
    "is_cancelled": false,
    "is_hidden": false,
    "was_forced": false,
    "executed_amount": "0",
    "remaining_amount": "1",
    "options": [],
    "price": "125.51",
    "original_amount": "1"
  },
  {
    "order_id": "107421205",
    "id": "107421205",
    "symbol": "ethusd",
    "exchange": "gemini",
    "avg_execution_price": "125.41",
    "side": "buy",
    "type": "exchange limit",
    "timestamp": "1547241626",
    "timestampms": 1547241626991,
    "is_live": true,
    "is_cancelled": false,
    "is_hidden": false,
    "was_forced": false,
    "executed_amount": "0.029147",
    "remaining_amount": "0.970853",
    "options": [],
    "price": "125.42",
    "original_amount": "1"
  }
]
json
Response with multiple active orders
application/json

Multiple Active Orders
List Past Orders
POST
https://api.gemini.com
/v1/orders/history
This API retrieves (closed) orders history for an account.

Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

How to retrieve your order history
To retrieve your full order history walking backwards,

Initial request: POST to https://api.gemini.com/v1/orders/history with a JSON payload including a timestamp key with value 0 and a limit_orders key with value 500
When you receive the list of orders, it will be sorted by timestamp descending - so the first element in the list will have the highest timestamp value. For this example, say that value is X.
Create a second POST request with a JSON payload including a timestamp key with value X+1 and a limit_orders key with value 500.
Take the first element of the list returned with highest timestamp value Y and create a third POST request with a JSON payload including a timestamp key with value Y+1 and a limit_orders key with value 500.
Continue creating POST requests and retrieving orders until an empty list is returned.
Break Types
In the rare event that a trade has been reversed (broken), the trade that is broken will have this flag set. The field will contain one of these values

Value	Description
manual	The trade was reversed manually. This means that all fees, proceeds, and debits associated with the trade have been credited or debited to the account seperately. That means that this reported trade must be included for order for the account balance to be correct.
full	The trade was fully broken. The reported trade should not be accounted for. It will be as though the transfer of fund associated with the trade had simply not happened.
List Past Orders ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Past Orders ›Request Body
requeststring · required
The API endpoint /v1/orders/history

noncerequired
The nonce, as described in Private API Invocation


symbolstring
The symbol to retrieve orders for

limit_ordersinteger
The maximum number of orders to return. Default is 50, max is 500.

Default: 50
timestamp
In iso datetime with timezone format from that date you will get order history


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group.

List Past Orders ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

order_idstring · integer
The order id

client_order_idstring · integer
An optional client-specified order id

symbolstring
The symbol of the order

exchangestring
Will always be "gemini"

pricestring · decimal
The price the order was issued at

avg_execution_pricestring · decimal
The average price at which this order as been executed so far. 0 if the order has not been executed at all.

sidestring · enum
Enum values:
buy
sell
typestring · enum
Description of the order

Enum values:
exchange limit
exchange stop limit
exchange market
optionsstring[]
An array containing at most one supported order execution option. See Order execution options for details.

timestamp
timestamp


timestampms
timestamp


is_liveboolean
true if the order is active on the book (has remaining quantity and has not been canceled)

is_cancelledboolean
true if the order has been canceled. Note the spelling, "cancelled" instead of "canceled". This is for compatibility reasons.

reasonstring
Populated with the reason your order was canceled, if available.

was_forcedboolean
Will always be false.

executed_amountstring · decimal
The amount of the order that has been filled.

remaining_amountstring · decimal
The amount of the order that has not been filled.

original_amountstring · decimal
The originally submitted amount of the order.

is_hiddenboolean
Will always return false.

tradesobject[]
Contains an array of JSON objects with trade details.


POST/v1/orders/history

cURL
curl --request POST \
  --url https://api.gemini.com/v1/orders/history \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/orders/history",
  "nonce": "<nonce>",
  "limit_orders": 50
}
'
shell

Example Request Body
{
  "request": "/v1/orders/history",
  "nonce": "<nonce>",
  "limit_orders": 50
}
json
Basic request to get order history
application/json

Basic Request

Example Responses

200
[
  {
    "order_id": "73751560172006688",
    "id": "73751560172006688",
    "symbol": "ethgusd",
    "exchange": "gemini",
    "avg_execution_price": "0.00",
    "side": "buy",
    "type": "exchange limit",
    "timestamp": "1695629298",
    "timestampms": 1695629298505,
    "is_live": false,
    "is_cancelled": true,
    "is_hidden": false,
    "was_forced": false,
    "executed_amount": "0",
    "client_order_id": "fb5321b0-2114-47fd-8cca-531a66d7feaf",
    "options": [],
    "price": "420.00",
    "original_amount": "0.69",
    "remaining_amount": "0.69",
    "trades": []
  }
]
json
Response with a cancelled order
application/json

Cancelled Order
List Past Trades
POST
https://api.gemini.com
/v1/mytrades
Gemini recommends using our WebSocket Order Events API to be notified when a trade executes on your account instead of polling this endpoint.
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.

Enabled for perpetuals accounts from July 10th, 0100hrs ET onwards. Trade info for all perpetuals orders submitted prior to this timing, will not be available through this API.

Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

How to retrieve your trade history
To retrieve your full trade history walking backwards,

Initial request: POST to https://api.gemini.com/v1/mytrades with a JSON payload including a timestamp key with value 0 and a limit_trades key with value 500
When you receive the list of trades, it will be sorted by timestamp descending - so the first element in the list will have the highest timestamp value. For this example, say that value is X.
Create a second POST request with a JSON payload including a timestamp key with value X+1 and a limit_trades key with value 500.
Take the first element of the list returned with highest timestamp value Y and create a third POST request with a JSON payload including a timestamp key with value Y+1 and a limit_trades key with value 500.
Continue creating POST requests and retrieving trades until an empty list is returned.
Break Types
In the rare event that a trade has been reversed (broken), the trade that is broken will have this flag set. The field will contain one of these values

Value	Description
manual	The trade was reversed manually. This means that all fees, proceeds, and debits associated with the trade have been credited or debited to the account seperately. That means that this reported trade must be included for order for the account balance to be correct.
full	The trade was fully broken. The reported trade should not be accounted for. It will be as though the transfer of fund associated with the trade had simply not happened.
List Past Trades ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Past Trades ›Request Body
requeststring · required
The API endpoint path

Example: /v1/mytrades
noncerequired
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
symbolstring
The symbol to retrieve trades for

Example: btcusd
limit_tradesinteger
The maximum number of trades to return. Default is 50, max is 500.

Example: 50
timestamp
timestamp


List Past Trades ›Responses
200
400
401
403
404
429
500
The past trades

object[]

pricestring
amountstring
timestamp
timestamp


timestampms
timestamp


typestring · enum
Enum values:
Buy
Sell
Example: Buy
aggressorboolean
fee_currencystring
fee_amountstring
tidinteger
order_idstring
client_order_idstring
exchangestring
is_auction_fillboolean
breakstring · enum
Enum values:
trade correct
Example:
POST/v1/mytrades

cURL
curl --request POST \
  --url https://api.gemini.com/v1/mytrades \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/mytrades",
  "nonce": "<nonce>",
  "symbol": "btcusd"
}
'
shell

Example Request Body
{
  "request": "/v1/mytrades",
  "nonce": "<nonce>",
  "symbol": "btcusd"
}
json
Basic request to get past trades for a symbol
application/json

Basic Request

Example Responses

200
[
  {
    "price": "3648.09",
    "amount": "0.0027343246",
    "timestamp": 1547232911,
    "timestampms": 1547232911021,
    "type": "Buy",
    "aggressor": true,
    "fee_currency": "USD",
    "fee_amount": "0.024937655575035",
    "tid": 107317526,
    "order_id": "107317524",
    "exchange": "gemini",
    "is_clearing_fill": false,
    "symbol": "BTCUSD"
  },
  {
    "price": "3633.00",
    "amount": "0.00423677",
    "timestamp": 1547220640,
    "timestampms": 1547220640195,
    "type": "Buy",
    "aggressor": false,
    "fee_currency": "USD",
    "fee_amount": "0.038480463525",
    "tid": 106921823,
    "order_id": "106817811",
    "exchange": "gemini",
    "is_clearing_fill": false,
    "symbol": "BTCUSD"
  }
]
json
Response with multiple trades
application/json

Multiple Trades
Get Trading Volume
POST
https://api.gemini.com
/v1/tradevolume
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Trading Volume ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Trading Volume ›Request Body
requeststring · required
The API endpoint path

Example: /v1/tradevolume
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
Get Trading Volume ›Responses
200
400
401
403
404
429
500
The trade volume

object[]

symbolstring
base_currencystring
quote_currencystring
notional_currencystring
data_datestring
total_volume_basestring
maker_buy_sell_ratiostring
buy_maker_basestring
buy_maker_notionalstring
buy_maker_countinteger
sell_maker_basestring
sell_maker_notionalstring
sell_maker_countinteger
buy_taker_basestring
buy_taker_notionalstring
buy_taker_countinteger
sell_taker_basestring
sell_taker_notionalstring
sell_taker_countinteger
POST/v1/tradevolume

cURL
curl --request POST \
  --url https://api.gemini.com/v1/tradevolume \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/tradevolume",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/tradevolume",
  "nonce": "<nonce>"
}
json
Basic request to get trade volume
application/json

Basic Request

Example Responses

200
[
  [
    {
      "symbol": "btcusd",
      "base_currency": "BTC",
      "notional_currency": "USD",
      "data_date": "2019-01-10",
      "total_volume_base": 8.06021756,
      "maker_buy_sell_ratio": 1,
      "buy_maker_base": 6.06021756,
      "buy_maker_notional": 23461.3515203844,
      "buy_maker_count": 34,
      "sell_maker_base": 0,
      "sell_maker_notional": 0,
      "sell_maker_count": 0,
      "buy_taker_base": 0,
      "buy_taker_notional": 0,
      "buy_taker_count": 0,
      "sell_taker_base": 2,
      "sell_taker_notional": 7935.66,
      "sell_taker_count": 2
    },
    {
      "symbol": "ltcusd",
      "base_currency": "LTC",
      "notional_currency": "USD",
      "data_date": "2019-01-11",
      "total_volume_base": 3,
      "maker_buy_sell_ratio": 0,
      "buy_maker_base": 0,
      "buy_maker_notional": 0,
      "buy_maker_count": 0,
      "sell_maker_base": 0,
      "sell_maker_notional": 0,
      "sell_maker_count": 0,
      "buy_taker_base": 3,
      "buy_taker_notional": 98.22,
      "buy_taker_count": 3,
      "sell_taker_base": 0,
      "sell_taker_notional": 0,
      "sell_taker_count": 0
    }
  ]
]
json
Response with trade volume for multiple symbols
application/json

Multiple Symbols
Get Notional Trading Volume
POST
https://api.gemini.com
/v1/notionalvolume
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Notional Trading Volume ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Notional Trading Volume ›Request Body
requeststring · required
The API endpoint path

Example: /v1/notionalvolume
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
Get Notional Trading Volume ›Responses
200
400
401
403
404
429
500
The notional volume

datestring · date
last_updated_msinteger
web_maker_fee_bpsinteger
web_taker_fee_bpsinteger
web_auction_fee_bpsinteger
api_maker_fee_bpsinteger
api_taker_fee_bpsinteger
api_auction_fee_bpsinteger
fix_maker_fee_bpsinteger
fix_taker_fee_bpsinteger
fix_auction_fee_bpsinteger
notional_30d_volumestring
notional_1d_volumeobject[]

api_notional_30d_volumestring
fee_tierobject

POST/v1/notionalvolume

cURL
curl --request POST \
  --url https://api.gemini.com/v1/notionalvolume \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/notionalvolume",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/notionalvolume",
  "nonce": "<nonce>"
}
json
Basic request to get notional volume
application/json

Basic Request

Example Responses

200
{
  "web_maker_fee_bps": 25,
  "web_taker_fee_bps": 35,
  "web_auction_fee_bps": 25,
  "api_maker_fee_bps": 10,
  "api_taker_fee_bps": 35,
  "api_auction_fee_bps": 20,
  "fix_maker_fee_bps": 10,
  "fix_taker_fee_bps": 35,
  "fix_auction_fee_bps": 20,
  "notional_30d_volume": 150,
  "last_updated_ms": 1551371446000,
  "date": "2019-02-28",
  "notional_1d_volume": [
    {
      "date": "2019-02-22",
      "notional_volume": 75
    },
    {
      "date": "2019-02-14",
      "notional_volume": 75
    }
  ]
}
json
Response with notional volume and fee information
application/json

Standard Response
Wrap Order
POST
https://api.gemini.com
/v1/wrap/{symbol}
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Wrap Order ›path Parameters
symbolstring · required
Trading pair symbol


BTCUSD, etc. See symbols and minimums.

Wrap Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Wrap Order ›Request Body
requeststring · required
The literal string "/v1/wrap/symbol"

noncerequired
The nonce, as described in Private API Invocation


amountstring · required
The amount to wrap

sidestring · enum
"buy" or "sell"

Enum values:
buy
sell
client_order_idstring
A client-specified order id

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Wrap Order ›Responses
200
400
401
403
404
429
500
Successful operation

orderIdstring
The order ID

pairstring
Trading pair symbol

pricestring
The price of the order

priceCurrencystring
The currency in which the order is priced

sidestring
Either "buy" or "sell"

quantitystring
The amount that was executed

quantityCurrencystring
The currency label for the quantity field

totalSpendstring
Total quantity spent for the order

totalSpendCurrencystring
Currency of the totalSpend

feestring
The amount charged

feeCurrencystring
Currency that the fee was paid in

depositFeestring
The deposit fee quantity

depositFeeCurrencystring
Currency in which depositFee is taken

POST/v1/wrap/{symbol}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/wrap/:symbol \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/wrap/GUSDUSD",
  "nonce": "<nonce>",
  "amount": "1",
  "side": "buy",
  "client_order_id": "4ac6f45f-baf1-40f8-83c5-001e3ea73c7f"
}
'
shell

Example Request Body
{
  "request": "/v1/wrap/GUSDUSD",
  "nonce": "<nonce>",
  "amount": "1",
  "side": "buy",
  "client_order_id": "4ac6f45f-baf1-40f8-83c5-001e3ea73c7f"
}
json
application/json

Example Responses

200
{
  "orderId": 429135395,
  "pair": "GUSDUSD",
  "price": "1",
  "priceCurrency": "USD",
  "side": "buy",
  "quantity": "1",
  "quantityCurrency": "GUSD",
  "totalSpend": "1",
  "totalSpendCurrency": "USD",
  "fee": "0",
  "feeCurrency": "USD",
  "depositFee": "0",
  "depositFeeCurrency": "USD"
}
json
application/json















Get Available Balances
POST
https://api.gemini.com
/v1/balances
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.
This will show the available balances in the supported currencies

Please note that Gemini is currently in the process of introducing new API architecture that will impact how decimal balances are returned from this endpoint for fiat and crypto assets.
As a result of this change, requests to the balances endpoint routed via the new architecture will return fiat balances and crypto balances truncated to 15 and 19 decimal places, respectively. This change has been introduced to correct for the display of miniscule residual values that do not actually represent usable balances.

It is recommended that users floor the values returned from this endpoint to the correct precision until the migration to the new architecture has been completed.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Available Balances ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Available Balances ›Request Body
requeststring · required
The API endpoint path

Example: /v1/balances
nonceTimestampType · required
timestamp


accountstring · required
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
showPendingBalancesboolean
Whether to include pending balances such as in-flight crypto deposits or withdrawals in the balances response.

Example: true
Default: false
Get Available Balances ›Responses
200
400
401
403
404
429
500
The account balances

object[]

typestring · enum
Enum values:
exchange
Example: exchange
currencystring
The currency symbol

Example: BTC
amountnumber
The amount available

Example: 10.5
availablenumber
The amount available for trading

Example: 9
availableForWithdrawalnumber
The amount available for withdrawal

Example: 9
pendingWithdrawalnumber
The amount pending withdrawal

Example: 1
pendingDepositnumber
The amount pending deposit

Example: 0.5
POST/v1/balances

cURL
curl --request POST \
  --url https://api.gemini.com/v1/balances \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/balances",
  "nonce": "<nonce>",
  "account": "primary",
  "showPendingBalances": true
}
'
shell

Example Request Body
{
  "request": "/v1/balances",
  "nonce": "<nonce>",
  "account": "primary",
  "showPendingBalances": true
}
json
application/json

Example Responses

200
[
  {
    "type": "exchange",
    "currency": "BTC",
    "amount": "5.0",
    "available": "4.5",
    "availableForWithdrawal": "4.5",
    "pendingWithdrawal": "0.25",
    "pendingDeposit": "0.25"
  },
  {
    "type": "exchange",
    "currency": "USD",
    "amount": "15000.00",
    "available": "5000.00",
    "availableForWithdrawal": "5000.00"
  },
  {
    "type": "exchange",
    "currency": "ETH",
    "amount": "10.0",
    "available": "10.0",
    "availableForWithdrawal": "10.0"
  }
]
json
Response with multiple currency balances
application/json

Multiple Balances
Get Notional Balances
POST
https://api.gemini.com
/v1/notionalbalances/{currency}
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.
This will show the available balances in the supported currencies as well as the notional value in the currency specified.

Please note that Gemini is currently in the process of introducing new API architecture that will impact how decimal balances are returned from this endpoint for fiat and crypto assets.
As a result of this change, requests to the notional balances endpoint routed via the new architecture will return fiat balances and crypto balances truncated to 15 and 19 decimal places, respectively. This change has been introduced to correct for the display of miniscule residual values that do not actually represent usable balances.

It is recommended that users floor the values returned from this endpoint to the correct precision until the migration to the new architecture has been completed.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Notional Balances ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Get Notional Balances ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Notional Balances ›Request Body
requeststring · required
The literal string "/v1/notionalbalances/currency"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys. The name of the account within the subaccount group.

Get Notional Balances ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

currencystring
Currency code, see symbols and minimums

amountstring
The current balance

amountNotionalstring
Amount, in notional

availablestring
The amount that is available to trade

availableNotionalstring
Available, in notional

availableForWithdrawalstring
The amount that is available to withdraw

availableForWithdrawalNotionalstring
AvailableForWithdrawal, in notional

POST/v1/notionalbalances/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/notionalbalances/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/notionalbalances/usd",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/notionalbalances/usd",
  "nonce": "<nonce>"
}
json
Basic request to get notional balances in USD
application/json

Basic Request

Example Responses

200
[
  {
    "currency": "BTC",
    "amount": "1154.62034001",
    "amountNotional": "10386000.59",
    "available": "1129.10517279",
    "availableNotional": "10161000.71",
    "availableForWithdrawal": "1129.10517279",
    "availableForWithdrawalNotional": "10161000.71"
  },
  {
    "currency": "USD",
    "amount": "18722.79",
    "amountNotional": "18722.79",
    "available": "14481.62",
    "availableNotional": "14481.62",
    "availableForWithdrawal": "14481.62",
    "availableForWithdrawalNotional": "14481.62"
  },
  {
    "currency": "ETH",
    "amount": "20124.50369697",
    "amountNotional": "100621.31",
    "available": "20124.50369697",
    "availableNotional": "100621.31",
    "availableForWithdrawal": "20124.50369697",
    "availableForWithdrawalNotional": "100621.31"
  }
]
json
application/json
List Deposit Addresses
POST
https://api.gemini.com
/v1/addresses/{network}
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 2 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have addresses:read or addresses:create assigned to access this endpoint. See OAuth Scopes for more information.

List Deposit Addresses ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

List Deposit Addresses ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Deposit Addresses ›Request Body
requeststring · required
The literal string "/v1/addresses/network"

noncerequired
The nonce, as described in Private API Invocation


timestamp
Only returns addresses created on or after this timestamp


accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Deposit Addresses ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

addressstring
String representation of the cryptocurrency address

timestamp
timestamp


labelstring
If you provided a label when creating the address, it will be echoed back here

memostring
It would be present if applicable, it will be present for cosmos address

networkstring
The blockchain network for the address

POST/v1/addresses/{network}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/addresses/:network \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/addresses/bitcoin",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/addresses/bitcoin",
  "nonce": "<nonce>"
}
json
Basic request to get Bitcoin deposit addresses
application/json

Basic Request

Example Responses

200
[
  {
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "timestamp": 1424285102000,
    "label": "my bitcoin address"
  },
  {
    "address": "n2wpl14aJEu10bRgMNd0gdjH8dHJ3h2a3ks",
    "timestamp": 1824785101000
  }
]
json
Response with Bitcoin deposit addresses
application/json

Bitcoin Addresses
Create New Deposit Address
POST
https://api.gemini.com
/v1/deposit/{network}/newAddress
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 2 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
Roles
The API key you use to access this endpoint must have the Fund Manager role assigned. See Roles for more information.

The OAuth scope must have addresses:create assigned to access this endpoint. See OAuth Scopes for more information.

Create New Deposit Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Create New Deposit Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Deposit Address ›Request Body
requeststring · required
The literal string "/v1/deposit/network/newAddress"

noncerequired
The nonce, as described in Private API Invocation


labelstring
A label for the address

legacyboolean
Whether to generate a legacy P2SH-P2PKH litecoin address. False by default.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Create New Deposit Address ›Responses
200
400
401
403
404
429
500
Successful operation

addressstring
String representation of the cryptocurrency address

timestamp
timestamp


labelstring
If you provided a label when creating the address, it will be echoed back here

memostring
It would be present if applicable, it will be present for cosmos address

networkstring
The blockchain network for the address

POST/v1/deposit/{network}/newAddress

cURL
curl --request POST \
  --url https://api.gemini.com/v1/deposit/:network/newAddress \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/deposit/bitcoin/newAddress",
  "nonce": "<nonce>",
  "label": "optional test label"
}
'
shell

Example Request Body
{
  "request": "/v1/deposit/bitcoin/newAddress",
  "nonce": "<nonce>",
  "label": "optional test label"
}
json
Basic request to create a new Bitcoin deposit address
application/json

Basic Bitcoin Address Request

Example Responses

200
{
  "network": "bitcoin",
  "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
  "label": "optional test label"
}
json
Response with a new Bitcoin deposit address
application/json

Bitcoin Address
List Past Transfers
POST
https://api.gemini.com
/v1/transfers
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 5 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
This endpoint shows deposits and withdrawals in the supported currencies. When deposits show as Advanced or Complete they are available for trading.

This endpoint does not currently show cancelled advances, returned outgoing wires or ACH transactions, or other exceptional transaction circumstances.

Fiat transfers between non-derivative and derivatives accounts are prohibited.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

List Past Transfers ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Past Transfers ›Request Body
requeststring · required
The literal string "/v1/transfers"

noncerequired
The nonce, as described in Private API Invocation


currencystring
Currency code, see symbols and minimums

timestamp
Only return transfers after this timestamp


limit_transfersinteger
The maximum number of transfers to return. The default is 10 and the maximum is 50.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

show_completed_deposit_advancesboolean
Whether to display completed deposit advances. True by default.

List Past Transfers ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

typestring · enum
Enum values:
Deposit
Withdrawal
statusstring · enum
Enum values:
Complete
Pending
timestampms
timestamp


eidinteger
The transfer ID

currencystring
The currency transferred

amountstring
The amount transferred

txHashstring
The transaction hash if applicable

POST/v1/transfers

cURL
curl --request POST \
  --url https://api.gemini.com/v1/transfers \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/transfers",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/transfers",
  "nonce": "<nonce>"
}
json
Basic request to get all transfers
application/json

Basic Request

Example Responses

200
[
  {
    "type": "Reward",
    "status": "Advanced",
    "timestampms": 1507943543575,
    "eid": 320033681,
    "currency": "USD",
    "amount": "125.00",
    "method": "CreditCard"
  },
  {
    "type": "Deposit",
    "status": "Advanced",
    "timestampms": 1507913541275,
    "eid": 320013281,
    "currency": "USD",
    "amount": "36.00",
    "method": "ACH"
  },
  {
    "type": "Deposit",
    "status": "Advanced",
    "timestampms": 1499990797452,
    "eid": 309356152,
    "currency": "ETH",
    "amount": "100",
    "txHash": "605c5fa8bf99458d24d61e09941bc443ddc44839d9aaa508b14b296c0c8269b2"
  },
  {
    "type": "Withdrawal",
    "status": "Complete",
    "timestampms": 1450403787001,
    "eid": 82897811,
    "currency": "BTC",
    "amount": "5",
    "txHash": "c458b86955b80db0718cfcadbff3df3734a906367982c6eb191e61117b810bbb",
    "withdrawalId": "02176a83-a6b1-4202-9b85-1c1c92dd25c4",
    "outputIdx": 0,
    "destination": "mqjvCtt4TJfQaC7nUgLMvHwuDPXMTEUGqx"
  }
]
json
Response with multiple types of transfers
application/json

Multiple Transfers
List Custody Fee Transfers
POST
https://api.gemini.com
/v1/custodyaccountfees
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 5 seconds per subaccount. This rate is subject to change and will be updated here accordingly. This is the same limit as the transfers endpoint. One call to one affects the other.
This endpoint shows Custody fee records in the supported currencies.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

List Custody Fee Transfers ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Custody Fee Transfers ›Request Body
requeststring · required
The literal string "/v1/custodyaccountfees"

noncerequired
The nonce, as described in Private API Invocation


timestamp
Only return Custody fee records on or after this timestamp


limit_transfersinteger
The maximum number of Custody fee records to return. The default is 10 and the maximum is 50.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Custody Fee Transfers ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

txTimeinteger
Time of Custody fee record in milliseconds

feeAmountstring
The fee amount charged

feeCurrencystring
Currency that the fee was paid in

eidinteger
Custody fee event id

eventTypestring
Custody fee event type

POST/v1/custodyaccountfees

cURL
curl --request POST \
  --url https://api.gemini.com/v1/custodyaccountfees \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/custodyaccountfees",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/custodyaccountfees",
  "nonce": "<nonce>"
}
json
Basic request to get custody account fees
application/json

Basic Request

Example Responses

200
[
  {
    "txTime": 1657236174056,
    "feeAmount": "10",
    "feeCurrency": "BTC",
    "eid": 256627,
    "eventType": "Withdrawal"
  },
  {
    "txTime": 1652279045196,
    "feeAmount": "10000000",
    "feeCurrency": "ETH",
    "eid": 15364,
    "eventType": "CustodyFeeDebit"
  },
  {
    "txTime": 1652279025196,
    "feeAmount": "1850",
    "feeCurrency": "WFIL",
    "eid": 9016,
    "eventType": "RiaFeeDebit"
  },
  {
    "txTime": 1652279025196,
    "feeAmount": "1850",
    "feeCurrency": "WFIL",
    "eid": 9016,
    "eventType": "RiaFeeCredit"
  }
]
json
Response with multiple custody fee records
application/json
Withdraw Crypto Funds
POST
https://api.gemini.com
/v1/withdraw/{currency}
Before you can withdraw cryptocurrency funds to an approved address, you need three things:

You must have an approved address list for your account
The address you want to withdraw funds to needs to already be on that approved address list
An API key with the Fund Manager role added
If you would like to withdraw via API to addresses that are not on your approved address list, please reach out to trading@gemini.com. We can enable this feature for you provide a set of approved IP addresses. This functionality is only available for exchange accounts. Pre-approved IP addresses and addresses added to your approved address list are required to enable withdrawal APIs for custody accounts.

See Roles for more information on how to add the Fund Manager role to the API key you want to use.

Roles
The API key you use to access this endpoint must have the Fund Manager role assigned. See Roles for more information.

The OAuth scope must have crypto:send assigned to access this endpoint. See OAuth Scopes for more information.

Withdraw Crypto Funds ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Withdraw Crypto Funds ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Withdraw Crypto Funds ›Request Body
requeststring · required
The literal string "/v1/withdraw/currency"

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
The destination address

amountstring · required
The amount to withdraw

client_transfer_idstring
A client-supplied unique identifier for the withdrawal

accountstring
Required for Master API keys. The name of the account within the subaccount group.

memostring
For addresses that require a memo

Withdraw Crypto Funds ›Responses
200
400
401
403
404
429
500
Successful operation

addressstring
Standard string format of the withdrawal destination address

amountstring
The withdrawal amount

feestring
The fee in kind applied to the transaction

withdrawalIdstring
A unique ID for the withdrawal

messagestring
A human-readable English string describing the withdrawal

POST/v1/withdraw/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/withdraw/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/withdraw/btc",
  "nonce": "<nonce>",
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1"
}
'
shell

Example Request Body
{
  "request": "/v1/withdraw/btc",
  "nonce": "<nonce>",
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1"
}
json
JSON payload for BTC withdrawal
application/json

BTC Withdrawal

Example Responses

200
{
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1",
  "fee": "0",
  "withdrawalId": "02176a83-a6b1-4202-9b85-1c1c92dd25c4",
  "message": "You have requested a transfer of 1 BTC to mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR. This withdrawal will be sent to the blockchain within the next 60 seconds."
}
json
JSON response for BTC withdrawal
application/json

BTC Withdrawal Response
Get Gas Fee Estimation
POST
https://api.gemini.com
/v1/withdraw/{currencyCodeLowerCase}/feeEstimate
API users will not be aware of the transfer fees before starting the withdrawal process. This endpoint allows you to find out the estimated gas fees before you start a withdrawal.

Roles
The API key you use to access this endpoint can have the Trader, Fund Manager, Auditor, WealthManager or Administrator role assigned. See Roles for more information.

Get Gas Fee Estimation ›path Parameters
currencyCodeLowerCasestring · required
The supported cryptocurrency code in lowercase (e.g eth, btc)

Get Gas Fee Estimation ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Gas Fee Estimation ›Request Body
requeststring · required
The string /v1/withdraw/{currencyCodeLowerCase}/feeEstimate where :currencyCodeLowerCase is replaced with the currency code of a supported crypto-currency, e.g. eth, aave, etc. See Symbols and minimums

Example: /v1/withdraw/eth/feeEstimate
noncerequired
The nonce, as described in Private API Invocation


addressstring · required
Standard string format of cryptocurrency address

Example: 0x31c2105b8dea834167f32f7ea7d877812e059230
amountstring · required
Quoted decimal amount to withdraw

Example: 0.01
accountstring · required
The name of the account within the subaccount group.

Example: primary
Get Gas Fee Estimation ›Responses
200
400
401
403
404
429
500
JSON response for ETH withdrawal

currencystring
Currency code, see symbols.

Example: ETH
feestring
The estimated gas fee

Example: {currency: 'ETH', value: '0'}
isOverrideboolean
Value that shows if an override on the customer's account for free withdrawals exists

Example: false
monthlyLimitinteger
Total nunber of allowable fee-free withdrawals

Example: 1
monthlyRemaininginteger
Total number of allowable fee-free withdrawals left to use

Example: 1
POST/v1/withdraw/{currencyCodeLowerCase}/feeEstimate

cURL
curl --request POST \
  --url https://api.gemini.com/v1/withdraw/:currencyCodeLowerCase/feeEstimate \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/withdraw/eth/feeEstimate",
  "nonce": "<nonce>",
  "address": "0x31c2105b8dea834167f32f7ea7d877812e059230",
  "amount": "0.01",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/withdraw/eth/feeEstimate",
  "nonce": "<nonce>",
  "address": "0x31c2105b8dea834167f32f7ea7d877812e059230",
  "amount": "0.01",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "currency": "ETH",
  "fee": "{currency: 'ETH', value: '0'}",
  "isOverride": false,
  "monthlyLimit": 1,
  "monthlyRemaining": 1
}
json
application/json
Add Bank
POST
https://api.gemini.com
/v1/payments/addbank
The add bank API allows for banking information to be sent in via API. However, for the bank to be verified, you must still send in a wire for any amount from the bank account.

Roles
This API requires the FundManager role. See Roles for more information.

The OAuth scope must have banks:create assigned to access this endpoint. See OAuth Scopes for more information.

Add Bank ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Add Bank ›Request Body
requeststring · required
The literal string "/v1/payments/addbank"

noncerequired
The nonce, as described in Private API Invocation


accountnumberstring · required
Account number of bank account to be added

routingstring · required
Routing number of bank account to be added

typestring · enum · required
Type of bank account to be added. Accepts checking or savings

Enum values:
checking
savings
namestring · required
The name of the bank account as shown on your account statements

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

Add Bank ›Responses
200
400
401
403
404
429
500
Successful operation

referenceIdstring
Reference ID for the new bank addition request. Once received, send in a wire from the requested bank account to verify it and enable withdrawals to that account.

POST/v1/payments/addbank

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/addbank \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/addbank",
  "nonce": "<nonce>",
  "accountnumber": "account-number-string",
  "routing": "routing-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/addbank",
  "nonce": "<nonce>",
  "accountnumber": "account-number-string",
  "routing": "routing-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking"
}
json
application/json

Example Responses

200
{
  "referenceId": "BankAccountRefId(18428)"
}
json
application/json
Add Bank CAD
POST
https://api.gemini.com
/v1/payments/addbank/cad
The add bank API allows for CAD banking information to be sent in via API. However, for the bank to be verified, you must still send in a wire for any amount from the bank account.

Roles
This API requires the FundManager role. See Roles for more information.

The OAuth scope must have banks:create assigned to access this endpoint. See OAuth Scopes for more information.

Add Bank CAD ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Add Bank CAD ›Request Body
requeststring · required
The literal string "/v1/payments/addbank/cad"

noncerequired
The nonce, as described in Private API Invocation


swiftcodestring · required
The account SWIFT code

accountNumberstring · required
Account number of bank account to be added

typestring · enum · required
Type of bank account to be added. Accepts checking or savings

Enum values:
checking
savings
namestring · required
The name of the bank account as shown on your account statements

institutionNumberstring
The institution number of the account - optional but recommended.

branchnnumberstring
The branch number - optional but recommended.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

Add Bank CAD ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the request. "OK" indicates the account has been created successfully.

POST/v1/payments/addbank/cad

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/addbank/cad \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/addbank/cad",
  "nonce": "<nonce>",
  "swiftcode": "swift-code-string",
  "accountnumber": "account-number-string",
  "institutionnumber": "institution-number-string",
  "branchnumber": "branch-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking",
  "account": "account-string"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/addbank/cad",
  "nonce": "<nonce>",
  "swiftcode": "swift-code-string",
  "accountnumber": "account-number-string",
  "institutionnumber": "institution-number-string",
  "branchnumber": "branch-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking",
  "account": "account-string"
}
json
application/json

Example Responses

200
{
  "result": "OK"
}
json
application/json
List Payment Methods
POST
https://api.gemini.com
/v1/payments/methods
The payments methods API will return data on balances in the account and linked banks.

Roles
The API key you use to access this endpoint can be either a Master or Account level key with any role assigned. See Roles for more information.

The OAuth scope must have banks:read assigned to access this endpoint. See OAuth Scopes for more information.

List Payment Methods ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Payment Methods ›Request Body
requeststring · required
The literal string "/v1/payments/methods"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

List Payment Methods ›Responses
200
400
401
403
404
429
500
Successful operation

balancesobject[]
Array of JSON objects with available fiat currencies and their balances.


banksobject[]
Array of JSON objects with banking information


POST/v1/payments/methods

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/methods \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/methods",
  "account": "primary",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/methods",
  "account": "primary",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "balances": [
    {
      "type": "exchange",
      "currency": "USD",
      "amount": "50893484.26",
      "available": "50889972.01",
      "availableForWithdrawal": "50889972.01"
    }
  ],
  "banks": [
    {
      "bank": "Jpmorgan Chase Bank Checking  - 1111",
      "bankId": "97631a24-ca40-4277-b3d5-38c37673d029"
    }
  ]
}
json
application/json
List Approved Addresses
POST
https://api.gemini.com
/v1/approvedAddresses/account/{network}
Allows viewing of Approved Address list.

Roles
This API can accept any role. See Roles for more information.

List Approved Addresses ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

List Approved Addresses ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Approved Addresses ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/account/:network" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to view the approved address list.

List Approved Addresses ›Responses
200
400
401
403
404
429
500
Successful operation

approvedAddressesobject[]
Array of approved addresses on both the account and group level.


POST/v1/approvedAddresses/account/{network}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/account/:network \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/account/ethereum",
  "nonce": "<nonce>",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/account/ethereum",
  "nonce": "<nonce>",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "approvedAddresses": [
    {
      "network": "ethereum",
      "scope": "account",
      "label": "api_added_ETH_address",
      "status": "pending-time",
      "createdAt": "1602692572349",
      "address": "0x0000000000000000000000000000000000000000"
    },
    {
      "network": "ethereum",
      "scope": "group",
      "label": "api_added_ETH_address",
      "status": "pending-time",
      "createdAt": "1602692542296",
      "address": "0x0000000000000000000000000000000000000000"
    },
    {
      "network": "ethereum",
      "scope": "group",
      "label": "hardware_wallet",
      "status": "active",
      "createdAt": "1602087433270",
      "address": "0xA63123350Acc8F5ee1b1fBd1A6717135e82dBd28"
    },
    {
      "network": "ethereum",
      "scope": "account",
      "label": "hardware_wallet",
      "status": "active",
      "createdAt": "1602086832986",
      "address": "0xA63123350Acc8F5ee1b1fBd1A6717135e82dBd28"
    }
  ]
}
json
application/json
Create New Approved Address
POST
https://api.gemini.com
/v1/approvedAddresses/{network}/request
Allows for creation of an approved withdrawal address. Once the request is made, the 7 day waiting period will begin. Please note that all approved address requests are subject to the 7 day waiting period.

If you add an address using an account-scoped API key, then the address will be added to your account specific approved address list. If you use a master-scoped API key, the address will be added to your group-level approved address list unless you specify an account.

This endpoint is subject to additional security constraints and is only accessible via API keys which have configured Trusted IP controls.

Please reach out to trading@gemini.com if you have any questions about approved addresses.

Roles
This API requires the FundManager role. See Roles for more information.

Create New Approved Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Create New Approved Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Approved Address ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/:network/request" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
A string of the address to be added to the approved address list.

labelstring · required
The label of the approved address.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to add the approved address.

memostring
it would be present if applicable, it will be present for cosmos address.

Create New Approved Address ›Responses
200
400
401
404
429
500
Successful operation

messagestring
Upon successful request, the endpoint will return a string indicating the 7-day approval hold period has begun.

POST/v1/approvedAddresses/{network}/request

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/:network/request \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/ethereum/request",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000",
  "label": "api_added_ETH_address",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/ethereum/request",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000",
  "label": "api_added_ETH_address",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "message": "Approved address addition is now waiting a 7-day approval hold before activation."
}
json
application/json
Remove Approved Address
POST
https://api.gemini.com
/v1/approvedAddresses/{network}/remove
Allows for removal of active or time-pending addresses from the Approved Address list. Addresses that are pending approval from another user on the account cannot be removed via API.

Roles
This API requires the FundManager role. See Roles for more information.

Remove Approved Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Remove Approved Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Remove Approved Address ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/:network/remove" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
A string of the address to be removed from the approved address list.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to remove the approved address.

Remove Approved Address ›Responses
200
400
401
403
404
429
500
Successful operation

messagestring
Upon successful request, the endpoint will return a string indicating the address and whether it was removed from the group-level or account-level approved address list.

POST/v1/approvedAddresses/{network}/remove

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/:network/remove \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/ethereum/remove",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/ethereum/remove",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000"
}
json
application/json

Example Responses

200
{
  "message": "0x0000000000000000000000000000000000000000 removed from group pending-time approved addresses."
}
json
application/json
Transfer Between Accounts
POST
https://api.gemini.com
/v1/account/transfer/{currency}
This API allows you to execute an internal transfer between any two accounts within your Master Group. In the scenario of exchange account to exchange account there will be no activity on a blockchain network. All other combinations will result in a movement of funds on a blockchain network.

Gemini Custody account withdrawals will not occur until the daily custody run occurs. In the case of funds moving from a Gemini Custody account to a Gemini Exchange account, the exchange account will get a precredit for the amount to be received. The exchange account will be able to trade these funds but will be unable to withdraw until the funds are processed on the blockchain and received.

Gemini Custody accounts request withdrawals to approved addresses in all cases and require the request to come from an approved IP address. Please reach out to trading@gemini.com to enable API withdrawals for custody accounts.

Gemini Custody accounts do not support fiat currency transfers.

Fiat transfers between non-derivative and derivatives accounts are prohibited.

Roles
The API key you use to access this endpoint must be a Master level key and have the Fund Manager role assigned. See Roles for more information.

Transfer Between Accounts ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Transfer Between Accounts ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Transfer Between Accounts ›Request Body
requeststring · required
The string /v1/account/transfer/:currency where :currency is replaced with either usd or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc. See Symbols and minimums.

noncerequired
The nonce, as described in Private API Invocation


sourceAccountstring · required
Nickname of the account you are transferring from. Use the Get Accounts endpoint to get all account names in the group.

targetAccountstring · required
Nickname of the account you are transferring to. Use the Get Accounts endpoint to get all account names in the group.

amountstring · required
Quoted decimal amount to withdraw

clientTransferIdstring
A unique identifier for the internal transfer, in uuid4 format

withdrawalIdstring
Unique ID of the requested withdrawal.

Transfer Between Accounts ›Responses
200
400
401
403
404
429
500
JSON response

fromAccountstring
Source account where funds are sent from

toAccountstring
Target account to receive funds in the internal transfer

amountstring
Quantity of assets being transferred

feestring
Fee taken for the transfer. Exchange account to exchange account transfers will always be free and will not be deducted from the free monthly transfer amount for that account.

currencystring
Display Name. Can be Bitcoin, Ether, Zcash, Litecoin, Dollar, etc.

withdrawalIdstring
Excludes exchange to exchange. Unique ID of the requested withdrawal

uuidstring
Only for exchange to exchange. Unique ID of the completed transfer

messagestring
Message describing result of withdrawal. Will inform of success, failure, or pending blockchain transaction.

txHashstring
Only for Ethereum network transfers. Excludes exchange to exchange transfers. Transaction hash for ethereum network transfer.

POST/v1/account/transfer/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account/transfer/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account/transfer/btc",
  "nonce": "<nonce>",
  "sourceAccount": "primary",
  "targetAccount": "my-secondary-account",
  "amount": "1.0"
}
'
shell

Example Request Body
{
  "request": "/v1/account/transfer/btc",
  "nonce": "<nonce>",
  "sourceAccount": "primary",
  "targetAccount": "my-secondary-account",
  "amount": "1.0"
}
json
JSON payload for a basic internal transfer
application/json

Basic Transfer

Example Responses

200
{
  "fromAccount": "my-account",
  "toAccount": "my-other-account",
  "amount": "1",
  "currency": "Bitcoin",
  "uuid": "9c153d64-83ba-4532-a159-ebe3f6797766",
  "message": "Success, transfer completed."
}
json
application/json
Get Transaction History
POST
https://api.gemini.com
/v1/transactions
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. Due to current limitations with the v1/transactions endpoint, historical data can only be returned for dates _after_ August 1st, 2022. For any requests to this endpoint, please ensure that the value provided for _timestamp_nanos_ as after this date.
This endpoint shows trade detail and transactions. There is a continuation_token that is a pagination token used for subsequent requests.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned and have the master account scope. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Transaction History ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Transaction History ›Request Body
requeststring · required
The literal string "/v1/transactions"

noncerequired
The nonce, as described in Private API Invocation


timestamp_nanos
Only return transfers on or after this timestamp in nanos. If this is defined, do not define “continuation_token”.


limitinteger
The maximum number of transfers to return. The default is 100 and the maximum is 300.

Default: 100
continuation_tokenstring
For subsequent requests, use the returned continuation_token value for next page. If this is defined, do not define “timestamp_nanos”.

Get Transaction History ›Responses
200
400
401
403
404
429
500
The response will be an array of JSON objects, sorted by trade and transfer as well as a continuationToken to be used in subsequent requests.

resultsarray
Results will contain either a list of Trade or Transfer responses


POST/v1/transactions

cURL
curl --request POST \
  --url https://api.gemini.com/v1/transactions \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/transactions",
  "nonce": "<nonce>",
  "timestamp_nanos": 1630382206000000000,
  "limit": 50,
  "continuation_token": "daccgrp_123421:n712621873886999872349872349:a71289723498273492374978424:m2:iForward"
}
'
shell

Example Request Body
{
  "request": "/v1/transactions",
  "nonce": "<nonce>",
  "timestamp_nanos": 1630382206000000000,
  "limit": 50,
  "continuation_token": "daccgrp_123421:n712621873886999872349872349:a71289723498273492374978424:m2:iForward"
}
json
application/json

Example Responses

200
{
  "results": [
    {
      "account": "primary",
      "amount": "0.001",
      "clientOrderId": "",
      "price": "1730.95",
      "timestampms": 1659201465069,
      "side": "SIDE_TYPE_BUY",
      "isAggressor": true,
      "feeAssetCode": "ETH",
      "feeAmount": "0.000000000000000605",
      "orderId": 73716687406755680,
      "exchange": "gemini",
      "isAuctionFill": false,
      "isClearingFill": false,
      "symbol": "ETHUSD",
      "tid": 144115199446910530,
      "type": "trade"
    },
    {
      "account": "primary",
      "amount": "0.001",
      "clientOrderId": "",
      "price": "1679.02",
      "timestampms": 1659201465222,
      "side": "SIDE_TYPE_SELL",
      "isAggressor": true,
      "feeAssetCode": "ETH",
      "feeAmount": "0.00000000000000000587",
      "orderId": 73716687406755680,
      "exchange": "gemini",
      "isAuctionFill": false,
      "isClearingFill": false,
      "symbol": "ETHUSD",
      "tid": 144115199446910500,
      "type": "trade"
    }
  ],
  "continuationToken": "daccgrp_1500611:n7126218738869976937315434496:a7126216029949884380085223424:m2:iForward"
}
json
Trade Response
application/json










Fund Management (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Get Available Balances
POST
https://api.gemini.com
/v1/balances
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.
This will show the available balances in the supported currencies

Please note that Gemini is currently in the process of introducing new API architecture that will impact how decimal balances are returned from this endpoint for fiat and crypto assets.
As a result of this change, requests to the balances endpoint routed via the new architecture will return fiat balances and crypto balances truncated to 15 and 19 decimal places, respectively. This change has been introduced to correct for the display of miniscule residual values that do not actually represent usable balances.

It is recommended that users floor the values returned from this endpoint to the correct precision until the migration to the new architecture has been completed.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Available Balances ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Available Balances ›Request Body
requeststring · required
The API endpoint path

Example: /v1/balances
nonceTimestampType · required
timestamp


accountstring · required
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
showPendingBalancesboolean
Whether to include pending balances such as in-flight crypto deposits or withdrawals in the balances response.

Example: true
Default: false
Get Available Balances ›Responses
200
400
401
403
404
429
500
The account balances

object[]

typestring · enum
Enum values:
exchange
Example: exchange
currencystring
The currency symbol

Example: BTC
amountnumber
The amount available

Example: 10.5
availablenumber
The amount available for trading

Example: 9
availableForWithdrawalnumber
The amount available for withdrawal

Example: 9
pendingWithdrawalnumber
The amount pending withdrawal

Example: 1
pendingDepositnumber
The amount pending deposit

Example: 0.5
POST/v1/balances

cURL
curl --request POST \
  --url https://api.gemini.com/v1/balances \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/balances",
  "nonce": "<nonce>",
  "account": "primary",
  "showPendingBalances": true
}
'
shell

Example Request Body
{
  "request": "/v1/balances",
  "nonce": "<nonce>",
  "account": "primary",
  "showPendingBalances": true
}
json
application/json

Example Responses

200
[
  {
    "type": "exchange",
    "currency": "BTC",
    "amount": "5.0",
    "available": "4.5",
    "availableForWithdrawal": "4.5",
    "pendingWithdrawal": "0.25",
    "pendingDeposit": "0.25"
  },
  {
    "type": "exchange",
    "currency": "USD",
    "amount": "15000.00",
    "available": "5000.00",
    "availableForWithdrawal": "5000.00"
  },
  {
    "type": "exchange",
    "currency": "ETH",
    "amount": "10.0",
    "available": "10.0",
    "availableForWithdrawal": "10.0"
  }
]
json
Response with multiple currency balances
application/json

Multiple Balances
Get Notional Balances
POST
https://api.gemini.com
/v1/notionalbalances/{currency}
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting.
This will show the available balances in the supported currencies as well as the notional value in the currency specified.

Please note that Gemini is currently in the process of introducing new API architecture that will impact how decimal balances are returned from this endpoint for fiat and crypto assets.
As a result of this change, requests to the notional balances endpoint routed via the new architecture will return fiat balances and crypto balances truncated to 15 and 19 decimal places, respectively. This change has been introduced to correct for the display of miniscule residual values that do not actually represent usable balances.

It is recommended that users floor the values returned from this endpoint to the correct precision until the migration to the new architecture has been completed.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Notional Balances ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Get Notional Balances ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Notional Balances ›Request Body
requeststring · required
The literal string "/v1/notionalbalances/currency"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys. The name of the account within the subaccount group.

Get Notional Balances ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

currencystring
Currency code, see symbols and minimums

amountstring
The current balance

amountNotionalstring
Amount, in notional

availablestring
The amount that is available to trade

availableNotionalstring
Available, in notional

availableForWithdrawalstring
The amount that is available to withdraw

availableForWithdrawalNotionalstring
AvailableForWithdrawal, in notional

POST/v1/notionalbalances/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/notionalbalances/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/notionalbalances/usd",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/notionalbalances/usd",
  "nonce": "<nonce>"
}
json
Basic request to get notional balances in USD
application/json

Basic Request

Example Responses

200
[
  {
    "currency": "BTC",
    "amount": "1154.62034001",
    "amountNotional": "10386000.59",
    "available": "1129.10517279",
    "availableNotional": "10161000.71",
    "availableForWithdrawal": "1129.10517279",
    "availableForWithdrawalNotional": "10161000.71"
  },
  {
    "currency": "USD",
    "amount": "18722.79",
    "amountNotional": "18722.79",
    "available": "14481.62",
    "availableNotional": "14481.62",
    "availableForWithdrawal": "14481.62",
    "availableForWithdrawalNotional": "14481.62"
  },
  {
    "currency": "ETH",
    "amount": "20124.50369697",
    "amountNotional": "100621.31",
    "available": "20124.50369697",
    "availableNotional": "100621.31",
    "availableForWithdrawal": "20124.50369697",
    "availableForWithdrawalNotional": "100621.31"
  }
]
json
application/json
List Deposit Addresses
POST
https://api.gemini.com
/v1/addresses/{network}
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 2 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have addresses:read or addresses:create assigned to access this endpoint. See OAuth Scopes for more information.

List Deposit Addresses ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

List Deposit Addresses ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Deposit Addresses ›Request Body
requeststring · required
The literal string "/v1/addresses/network"

noncerequired
The nonce, as described in Private API Invocation


timestamp
Only returns addresses created on or after this timestamp


accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Deposit Addresses ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

addressstring
String representation of the cryptocurrency address

timestamp
timestamp


labelstring
If you provided a label when creating the address, it will be echoed back here

memostring
It would be present if applicable, it will be present for cosmos address

networkstring
The blockchain network for the address

POST/v1/addresses/{network}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/addresses/:network \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/addresses/bitcoin",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/addresses/bitcoin",
  "nonce": "<nonce>"
}
json
Basic request to get Bitcoin deposit addresses
application/json

Basic Request

Example Responses

200
[
  {
    "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
    "timestamp": 1424285102000,
    "label": "my bitcoin address"
  },
  {
    "address": "n2wpl14aJEu10bRgMNd0gdjH8dHJ3h2a3ks",
    "timestamp": 1824785101000
  }
]
json
Response with Bitcoin deposit addresses
application/json

Bitcoin Addresses
Create New Deposit Address
POST
https://api.gemini.com
/v1/deposit/{network}/newAddress
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 2 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
Roles
The API key you use to access this endpoint must have the Fund Manager role assigned. See Roles for more information.

The OAuth scope must have addresses:create assigned to access this endpoint. See OAuth Scopes for more information.

Create New Deposit Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Create New Deposit Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Deposit Address ›Request Body
requeststring · required
The literal string "/v1/deposit/network/newAddress"

noncerequired
The nonce, as described in Private API Invocation


labelstring
A label for the address

legacyboolean
Whether to generate a legacy P2SH-P2PKH litecoin address. False by default.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Create New Deposit Address ›Responses
200
400
401
403
404
429
500
Successful operation

addressstring
String representation of the cryptocurrency address

timestamp
timestamp


labelstring
If you provided a label when creating the address, it will be echoed back here

memostring
It would be present if applicable, it will be present for cosmos address

networkstring
The blockchain network for the address

POST/v1/deposit/{network}/newAddress

cURL
curl --request POST \
  --url https://api.gemini.com/v1/deposit/:network/newAddress \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/deposit/bitcoin/newAddress",
  "nonce": "<nonce>",
  "label": "optional test label"
}
'
shell

Example Request Body
{
  "request": "/v1/deposit/bitcoin/newAddress",
  "nonce": "<nonce>",
  "label": "optional test label"
}
json
Basic request to create a new Bitcoin deposit address
application/json

Basic Bitcoin Address Request

Example Responses

200
{
  "network": "bitcoin",
  "address": "n2saq73aDTu42bRgEHd8gd4to1gCzHxrdj",
  "label": "optional test label"
}
json
Response with a new Bitcoin deposit address
application/json

Bitcoin Address
List Past Transfers
POST
https://api.gemini.com
/v1/transfers
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 5 seconds per subaccount. This rate is subject to change and will be updated here accordingly.
This endpoint shows deposits and withdrawals in the supported currencies. When deposits show as Advanced or Complete they are available for trading.

This endpoint does not currently show cancelled advances, returned outgoing wires or ACH transactions, or other exceptional transaction circumstances.

Fiat transfers between non-derivative and derivatives accounts are prohibited.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

List Past Transfers ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Past Transfers ›Request Body
requeststring · required
The literal string "/v1/transfers"

noncerequired
The nonce, as described in Private API Invocation


currencystring
Currency code, see symbols and minimums

timestamp
Only return transfers after this timestamp


limit_transfersinteger
The maximum number of transfers to return. The default is 10 and the maximum is 50.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

show_completed_deposit_advancesboolean
Whether to display completed deposit advances. True by default.

List Past Transfers ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

typestring · enum
Enum values:
Deposit
Withdrawal
statusstring · enum
Enum values:
Complete
Pending
timestampms
timestamp


eidinteger
The transfer ID

currencystring
The currency transferred

amountstring
The amount transferred

txHashstring
The transaction hash if applicable

POST/v1/transfers

cURL
curl --request POST \
  --url https://api.gemini.com/v1/transfers \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/transfers",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/transfers",
  "nonce": "<nonce>"
}
json
Basic request to get all transfers
application/json

Basic Request

Example Responses

200
[
  {
    "type": "Reward",
    "status": "Advanced",
    "timestampms": 1507943543575,
    "eid": 320033681,
    "currency": "USD",
    "amount": "125.00",
    "method": "CreditCard"
  },
  {
    "type": "Deposit",
    "status": "Advanced",
    "timestampms": 1507913541275,
    "eid": 320013281,
    "currency": "USD",
    "amount": "36.00",
    "method": "ACH"
  },
  {
    "type": "Deposit",
    "status": "Advanced",
    "timestampms": 1499990797452,
    "eid": 309356152,
    "currency": "ETH",
    "amount": "100",
    "txHash": "605c5fa8bf99458d24d61e09941bc443ddc44839d9aaa508b14b296c0c8269b2"
  },
  {
    "type": "Withdrawal",
    "status": "Complete",
    "timestampms": 1450403787001,
    "eid": 82897811,
    "currency": "BTC",
    "amount": "5",
    "txHash": "c458b86955b80db0718cfcadbff3df3734a906367982c6eb191e61117b810bbb",
    "withdrawalId": "02176a83-a6b1-4202-9b85-1c1c92dd25c4",
    "outputIdx": 0,
    "destination": "mqjvCtt4TJfQaC7nUgLMvHwuDPXMTEUGqx"
  }
]
json
Response with multiple types of transfers
application/json

Multiple Transfers
List Custody Fee Transfers
POST
https://api.gemini.com
/v1/custodyaccountfees
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. This endpoint is currently restricted further than our standard rate limiting to a rate of 1 request per 5 seconds per subaccount. This rate is subject to change and will be updated here accordingly. This is the same limit as the transfers endpoint. One call to one affects the other.
This endpoint shows Custody fee records in the supported currencies.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

List Custody Fee Transfers ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Custody Fee Transfers ›Request Body
requeststring · required
The literal string "/v1/custodyaccountfees"

noncerequired
The nonce, as described in Private API Invocation


timestamp
Only return Custody fee records on or after this timestamp


limit_transfersinteger
The maximum number of Custody fee records to return. The default is 10 and the maximum is 50.

accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Custody Fee Transfers ›Responses
200
400
401
403
404
429
500
Successful operation

object[]

txTimeinteger
Time of Custody fee record in milliseconds

feeAmountstring
The fee amount charged

feeCurrencystring
Currency that the fee was paid in

eidinteger
Custody fee event id

eventTypestring
Custody fee event type

POST/v1/custodyaccountfees

cURL
curl --request POST \
  --url https://api.gemini.com/v1/custodyaccountfees \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/custodyaccountfees",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/custodyaccountfees",
  "nonce": "<nonce>"
}
json
Basic request to get custody account fees
application/json

Basic Request

Example Responses

200
[
  {
    "txTime": 1657236174056,
    "feeAmount": "10",
    "feeCurrency": "BTC",
    "eid": 256627,
    "eventType": "Withdrawal"
  },
  {
    "txTime": 1652279045196,
    "feeAmount": "10000000",
    "feeCurrency": "ETH",
    "eid": 15364,
    "eventType": "CustodyFeeDebit"
  },
  {
    "txTime": 1652279025196,
    "feeAmount": "1850",
    "feeCurrency": "WFIL",
    "eid": 9016,
    "eventType": "RiaFeeDebit"
  },
  {
    "txTime": 1652279025196,
    "feeAmount": "1850",
    "feeCurrency": "WFIL",
    "eid": 9016,
    "eventType": "RiaFeeCredit"
  }
]
json
Response with multiple custody fee records
application/json
Withdraw Crypto Funds
POST
https://api.gemini.com
/v1/withdraw/{currency}
Before you can withdraw cryptocurrency funds to an approved address, you need three things:

You must have an approved address list for your account
The address you want to withdraw funds to needs to already be on that approved address list
An API key with the Fund Manager role added
If you would like to withdraw via API to addresses that are not on your approved address list, please reach out to trading@gemini.com. We can enable this feature for you provide a set of approved IP addresses. This functionality is only available for exchange accounts. Pre-approved IP addresses and addresses added to your approved address list are required to enable withdrawal APIs for custody accounts.

See Roles for more information on how to add the Fund Manager role to the API key you want to use.

Roles
The API key you use to access this endpoint must have the Fund Manager role assigned. See Roles for more information.

The OAuth scope must have crypto:send assigned to access this endpoint. See OAuth Scopes for more information.

Withdraw Crypto Funds ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Withdraw Crypto Funds ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Withdraw Crypto Funds ›Request Body
requeststring · required
The literal string "/v1/withdraw/currency"

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
The destination address

amountstring · required
The amount to withdraw

client_transfer_idstring
A client-supplied unique identifier for the withdrawal

accountstring
Required for Master API keys. The name of the account within the subaccount group.

memostring
For addresses that require a memo

Withdraw Crypto Funds ›Responses
200
400
401
403
404
429
500
Successful operation

addressstring
Standard string format of the withdrawal destination address

amountstring
The withdrawal amount

feestring
The fee in kind applied to the transaction

withdrawalIdstring
A unique ID for the withdrawal

messagestring
A human-readable English string describing the withdrawal

POST/v1/withdraw/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/withdraw/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/withdraw/btc",
  "nonce": "<nonce>",
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1"
}
'
shell

Example Request Body
{
  "request": "/v1/withdraw/btc",
  "nonce": "<nonce>",
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1"
}
json
JSON payload for BTC withdrawal
application/json

BTC Withdrawal

Example Responses

200
{
  "address": "mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR",
  "amount": "1",
  "fee": "0",
  "withdrawalId": "02176a83-a6b1-4202-9b85-1c1c92dd25c4",
  "message": "You have requested a transfer of 1 BTC to mi98Z9brJ3TgaKsmvXatuRahbFRUFKRUdR. This withdrawal will be sent to the blockchain within the next 60 seconds."
}
json
JSON response for BTC withdrawal
application/json

BTC Withdrawal Response
Get Gas Fee Estimation
POST
https://api.gemini.com
/v1/withdraw/{currencyCodeLowerCase}/feeEstimate
API users will not be aware of the transfer fees before starting the withdrawal process. This endpoint allows you to find out the estimated gas fees before you start a withdrawal.

Roles
The API key you use to access this endpoint can have the Trader, Fund Manager, Auditor, WealthManager or Administrator role assigned. See Roles for more information.

Get Gas Fee Estimation ›path Parameters
currencyCodeLowerCasestring · required
The supported cryptocurrency code in lowercase (e.g eth, btc)

Get Gas Fee Estimation ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Gas Fee Estimation ›Request Body
requeststring · required
The string /v1/withdraw/{currencyCodeLowerCase}/feeEstimate where :currencyCodeLowerCase is replaced with the currency code of a supported crypto-currency, e.g. eth, aave, etc. See Symbols and minimums

Example: /v1/withdraw/eth/feeEstimate
noncerequired
The nonce, as described in Private API Invocation


addressstring · required
Standard string format of cryptocurrency address

Example: 0x31c2105b8dea834167f32f7ea7d877812e059230
amountstring · required
Quoted decimal amount to withdraw

Example: 0.01
accountstring · required
The name of the account within the subaccount group.

Example: primary
Get Gas Fee Estimation ›Responses
200
400
401
403
404
429
500
JSON response for ETH withdrawal

currencystring
Currency code, see symbols.

Example: ETH
feestring
The estimated gas fee

Example: {currency: 'ETH', value: '0'}
isOverrideboolean
Value that shows if an override on the customer's account for free withdrawals exists

Example: false
monthlyLimitinteger
Total nunber of allowable fee-free withdrawals

Example: 1
monthlyRemaininginteger
Total number of allowable fee-free withdrawals left to use

Example: 1
POST/v1/withdraw/{currencyCodeLowerCase}/feeEstimate

cURL
curl --request POST \
  --url https://api.gemini.com/v1/withdraw/:currencyCodeLowerCase/feeEstimate \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/withdraw/eth/feeEstimate",
  "nonce": "<nonce>",
  "address": "0x31c2105b8dea834167f32f7ea7d877812e059230",
  "amount": "0.01",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/withdraw/eth/feeEstimate",
  "nonce": "<nonce>",
  "address": "0x31c2105b8dea834167f32f7ea7d877812e059230",
  "amount": "0.01",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "currency": "ETH",
  "fee": "{currency: 'ETH', value: '0'}",
  "isOverride": false,
  "monthlyLimit": 1,
  "monthlyRemaining": 1
}
json
application/json
Add Bank
POST
https://api.gemini.com
/v1/payments/addbank
The add bank API allows for banking information to be sent in via API. However, for the bank to be verified, you must still send in a wire for any amount from the bank account.

Roles
This API requires the FundManager role. See Roles for more information.

The OAuth scope must have banks:create assigned to access this endpoint. See OAuth Scopes for more information.

Add Bank ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Add Bank ›Request Body
requeststring · required
The literal string "/v1/payments/addbank"

noncerequired
The nonce, as described in Private API Invocation


accountnumberstring · required
Account number of bank account to be added

routingstring · required
Routing number of bank account to be added

typestring · enum · required
Type of bank account to be added. Accepts checking or savings

Enum values:
checking
savings
namestring · required
The name of the bank account as shown on your account statements

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

Add Bank ›Responses
200
400
401
403
404
429
500
Successful operation

referenceIdstring
Reference ID for the new bank addition request. Once received, send in a wire from the requested bank account to verify it and enable withdrawals to that account.

POST/v1/payments/addbank

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/addbank \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/addbank",
  "nonce": "<nonce>",
  "accountnumber": "account-number-string",
  "routing": "routing-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/addbank",
  "nonce": "<nonce>",
  "accountnumber": "account-number-string",
  "routing": "routing-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking"
}
json
application/json

Example Responses

200
{
  "referenceId": "BankAccountRefId(18428)"
}
json
application/json
Add Bank CAD
POST
https://api.gemini.com
/v1/payments/addbank/cad
The add bank API allows for CAD banking information to be sent in via API. However, for the bank to be verified, you must still send in a wire for any amount from the bank account.

Roles
This API requires the FundManager role. See Roles for more information.

The OAuth scope must have banks:create assigned to access this endpoint. See OAuth Scopes for more information.

Add Bank CAD ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Add Bank CAD ›Request Body
requeststring · required
The literal string "/v1/payments/addbank/cad"

noncerequired
The nonce, as described in Private API Invocation


swiftcodestring · required
The account SWIFT code

accountNumberstring · required
Account number of bank account to be added

typestring · enum · required
Type of bank account to be added. Accepts checking or savings

Enum values:
checking
savings
namestring · required
The name of the bank account as shown on your account statements

institutionNumberstring
The institution number of the account - optional but recommended.

branchnnumberstring
The branch number - optional but recommended.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

Add Bank CAD ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the request. "OK" indicates the account has been created successfully.

POST/v1/payments/addbank/cad

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/addbank/cad \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/addbank/cad",
  "nonce": "<nonce>",
  "swiftcode": "swift-code-string",
  "accountnumber": "account-number-string",
  "institutionnumber": "institution-number-string",
  "branchnumber": "branch-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking",
  "account": "account-string"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/addbank/cad",
  "nonce": "<nonce>",
  "swiftcode": "swift-code-string",
  "accountnumber": "account-number-string",
  "institutionnumber": "institution-number-string",
  "branchnumber": "branch-number-string",
  "type": "checking",
  "name": "Satoshi Nakamoto Checking",
  "account": "account-string"
}
json
application/json

Example Responses

200
{
  "result": "OK"
}
json
application/json
List Payment Methods
POST
https://api.gemini.com
/v1/payments/methods
The payments methods API will return data on balances in the account and linked banks.

Roles
The API key you use to access this endpoint can be either a Master or Account level key with any role assigned. See Roles for more information.

The OAuth scope must have banks:read assigned to access this endpoint. See OAuth Scopes for more information.

List Payment Methods ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Payment Methods ›Request Body
requeststring · required
The literal string "/v1/payments/methods"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

List Payment Methods ›Responses
200
400
401
403
404
429
500
Successful operation

balancesobject[]
Array of JSON objects with available fiat currencies and their balances.


banksobject[]
Array of JSON objects with banking information


POST/v1/payments/methods

cURL
curl --request POST \
  --url https://api.gemini.com/v1/payments/methods \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/payments/methods",
  "account": "primary",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/payments/methods",
  "account": "primary",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "balances": [
    {
      "type": "exchange",
      "currency": "USD",
      "amount": "50893484.26",
      "available": "50889972.01",
      "availableForWithdrawal": "50889972.01"
    }
  ],
  "banks": [
    {
      "bank": "Jpmorgan Chase Bank Checking  - 1111",
      "bankId": "97631a24-ca40-4277-b3d5-38c37673d029"
    }
  ]
}
json
application/json
List Approved Addresses
POST
https://api.gemini.com
/v1/approvedAddresses/account/{network}
Allows viewing of Approved Address list.

Roles
This API can accept any role. See Roles for more information.

List Approved Addresses ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

List Approved Addresses ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Approved Addresses ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/account/:network" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to view the approved address list.

List Approved Addresses ›Responses
200
400
401
403
404
429
500
Successful operation

approvedAddressesobject[]
Array of approved addresses on both the account and group level.


POST/v1/approvedAddresses/account/{network}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/account/:network \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/account/ethereum",
  "nonce": "<nonce>",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/account/ethereum",
  "nonce": "<nonce>",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "approvedAddresses": [
    {
      "network": "ethereum",
      "scope": "account",
      "label": "api_added_ETH_address",
      "status": "pending-time",
      "createdAt": "1602692572349",
      "address": "0x0000000000000000000000000000000000000000"
    },
    {
      "network": "ethereum",
      "scope": "group",
      "label": "api_added_ETH_address",
      "status": "pending-time",
      "createdAt": "1602692542296",
      "address": "0x0000000000000000000000000000000000000000"
    },
    {
      "network": "ethereum",
      "scope": "group",
      "label": "hardware_wallet",
      "status": "active",
      "createdAt": "1602087433270",
      "address": "0xA63123350Acc8F5ee1b1fBd1A6717135e82dBd28"
    },
    {
      "network": "ethereum",
      "scope": "account",
      "label": "hardware_wallet",
      "status": "active",
      "createdAt": "1602086832986",
      "address": "0xA63123350Acc8F5ee1b1fBd1A6717135e82dBd28"
    }
  ]
}
json
application/json
Create New Approved Address
POST
https://api.gemini.com
/v1/approvedAddresses/{network}/request
Allows for creation of an approved withdrawal address. Once the request is made, the 7 day waiting period will begin. Please note that all approved address requests are subject to the 7 day waiting period.

If you add an address using an account-scoped API key, then the address will be added to your account specific approved address list. If you use a master-scoped API key, the address will be added to your group-level approved address list unless you specify an account.

This endpoint is subject to additional security constraints and is only accessible via API keys which have configured Trusted IP controls.

Please reach out to trading@gemini.com if you have any questions about approved addresses.

Roles
This API requires the FundManager role. See Roles for more information.

Create New Approved Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Create New Approved Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Approved Address ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/:network/request" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
A string of the address to be added to the approved address list.

labelstring · required
The label of the approved address.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to add the approved address.

memostring
it would be present if applicable, it will be present for cosmos address.

Create New Approved Address ›Responses
200
400
401
404
429
500
Successful operation

messagestring
Upon successful request, the endpoint will return a string indicating the 7-day approval hold period has begun.

POST/v1/approvedAddresses/{network}/request

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/:network/request \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/ethereum/request",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000",
  "label": "api_added_ETH_address",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/ethereum/request",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000",
  "label": "api_added_ETH_address",
  "account": "primary"
}
json
application/json

Example Responses

200
{
  "message": "Approved address addition is now waiting a 7-day approval hold before activation."
}
json
application/json
Remove Approved Address
POST
https://api.gemini.com
/v1/approvedAddresses/{network}/remove
Allows for removal of active or time-pending addresses from the Approved Address list. Addresses that are pending approval from another user on the account cannot be removed via API.

Roles
This API requires the FundManager role. See Roles for more information.

Remove Approved Address ›path Parameters
networkstring · required
Can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

Remove Approved Address ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Remove Approved Address ›Request Body
requeststring · required
The literal string "/v1/approvedAddresses/:network/remove" where :network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

noncerequired
The nonce, as described in Private API Invocation


addressstring · required
A string of the address to be removed from the approved address list.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to remove the approved address.

Remove Approved Address ›Responses
200
400
401
403
404
429
500
Successful operation

messagestring
Upon successful request, the endpoint will return a string indicating the address and whether it was removed from the group-level or account-level approved address list.

POST/v1/approvedAddresses/{network}/remove

cURL
curl --request POST \
  --url https://api.gemini.com/v1/approvedAddresses/:network/remove \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/approvedAddresses/ethereum/remove",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000"
}
'
shell

Example Request Body
{
  "request": "/v1/approvedAddresses/ethereum/remove",
  "nonce": "<nonce>",
  "address": "0x0000000000000000000000000000000000000000"
}
json
application/json

Example Responses

200
{
  "message": "0x0000000000000000000000000000000000000000 removed from group pending-time approved addresses."
}
json
application/json
Transfer Between Accounts
POST
https://api.gemini.com
/v1/account/transfer/{currency}
This API allows you to execute an internal transfer between any two accounts within your Master Group. In the scenario of exchange account to exchange account there will be no activity on a blockchain network. All other combinations will result in a movement of funds on a blockchain network.

Gemini Custody account withdrawals will not occur until the daily custody run occurs. In the case of funds moving from a Gemini Custody account to a Gemini Exchange account, the exchange account will get a precredit for the amount to be received. The exchange account will be able to trade these funds but will be unable to withdraw until the funds are processed on the blockchain and received.

Gemini Custody accounts request withdrawals to approved addresses in all cases and require the request to come from an approved IP address. Please reach out to trading@gemini.com to enable API withdrawals for custody accounts.

Gemini Custody accounts do not support fiat currency transfers.

Fiat transfers between non-derivative and derivatives accounts are prohibited.

Roles
The API key you use to access this endpoint must be a Master level key and have the Fund Manager role assigned. See Roles for more information.

Transfer Between Accounts ›path Parameters
currencystring · required
Either a fiat currency, e.g. usd or gbp, or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc.

Transfer Between Accounts ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Transfer Between Accounts ›Request Body
requeststring · required
The string /v1/account/transfer/:currency where :currency is replaced with either usd or a supported crypto-currency, e.g. gusd, btc, eth, aave, etc. See Symbols and minimums.

noncerequired
The nonce, as described in Private API Invocation


sourceAccountstring · required
Nickname of the account you are transferring from. Use the Get Accounts endpoint to get all account names in the group.

targetAccountstring · required
Nickname of the account you are transferring to. Use the Get Accounts endpoint to get all account names in the group.

amountstring · required
Quoted decimal amount to withdraw

clientTransferIdstring
A unique identifier for the internal transfer, in uuid4 format

withdrawalIdstring
Unique ID of the requested withdrawal.

Transfer Between Accounts ›Responses
200
400
401
403
404
429
500
JSON response

fromAccountstring
Source account where funds are sent from

toAccountstring
Target account to receive funds in the internal transfer

amountstring
Quantity of assets being transferred

feestring
Fee taken for the transfer. Exchange account to exchange account transfers will always be free and will not be deducted from the free monthly transfer amount for that account.

currencystring
Display Name. Can be Bitcoin, Ether, Zcash, Litecoin, Dollar, etc.

withdrawalIdstring
Excludes exchange to exchange. Unique ID of the requested withdrawal

uuidstring
Only for exchange to exchange. Unique ID of the completed transfer

messagestring
Message describing result of withdrawal. Will inform of success, failure, or pending blockchain transaction.

txHashstring
Only for Ethereum network transfers. Excludes exchange to exchange transfers. Transaction hash for ethereum network transfer.

POST/v1/account/transfer/{currency}

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account/transfer/:currency \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account/transfer/btc",
  "nonce": "<nonce>",
  "sourceAccount": "primary",
  "targetAccount": "my-secondary-account",
  "amount": "1.0"
}
'
shell

Example Request Body
{
  "request": "/v1/account/transfer/btc",
  "nonce": "<nonce>",
  "sourceAccount": "primary",
  "targetAccount": "my-secondary-account",
  "amount": "1.0"
}
json
JSON payload for a basic internal transfer
application/json

Basic Transfer

Example Responses

200
{
  "fromAccount": "my-account",
  "toAccount": "my-other-account",
  "amount": "1",
  "currency": "Bitcoin",
  "uuid": "9c153d64-83ba-4532-a159-ebe3f6797766",
  "message": "Success, transfer completed."
}
json
application/json
Get Transaction History
POST
https://api.gemini.com
/v1/transactions
Under the terms of the Gemini API Agreement, polling this endpoint may be subject to rate limiting. Due to current limitations with the v1/transactions endpoint, historical data can only be returned for dates _after_ August 1st, 2022. For any requests to this endpoint, please ensure that the value provided for _timestamp_nanos_ as after this date.
This endpoint shows trade detail and transactions. There is a continuation_token that is a pagination token used for subsequent requests.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned and have the master account scope. See Roles for more information.

The OAuth scope must have history:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Transaction History ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Transaction History ›Request Body
requeststring · required
The literal string "/v1/transactions"

noncerequired
The nonce, as described in Private API Invocation


timestamp_nanos
Only return transfers on or after this timestamp in nanos. If this is defined, do not define “continuation_token”.


limitinteger
The maximum number of transfers to return. The default is 100 and the maximum is 300.

Default: 100
continuation_tokenstring
For subsequent requests, use the returned continuation_token value for next page. If this is defined, do not define “timestamp_nanos”.

Get Transaction History ›Responses
200
400
401
403
404
429
500
The response will be an array of JSON objects, sorted by trade and transfer as well as a continuationToken to be used in subsequent requests.

resultsarray
Results will contain either a list of Trade or Transfer responses


POST/v1/transactions

cURL
curl --request POST \
  --url https://api.gemini.com/v1/transactions \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/transactions",
  "nonce": "<nonce>",
  "timestamp_nanos": 1630382206000000000,
  "limit": 50,
  "continuation_token": "daccgrp_123421:n712621873886999872349872349:a71289723498273492374978424:m2:iForward"
}
'
shell

Example Request Body
{
  "request": "/v1/transactions",
  "nonce": "<nonce>",
  "timestamp_nanos": 1630382206000000000,
  "limit": 50,
  "continuation_token": "daccgrp_123421:n712621873886999872349872349:a71289723498273492374978424:m2:iForward"
}
json
application/json

Example Responses

200
{
  "results": [
    {
      "account": "primary",
      "amount": "0.001",
      "clientOrderId": "",
      "price": "1730.95",
      "timestampms": 1659201465069,
      "side": "SIDE_TYPE_BUY",
      "isAggressor": true,
      "feeAssetCode": "ETH",
      "feeAmount": "0.000000000000000605",
      "orderId": 73716687406755680,
      "exchange": "gemini",
      "isAuctionFill": false,
      "isClearingFill": false,
      "symbol": "ETHUSD",
      "tid": 144115199446910530,
      "type": "trade"
    },
    {
      "account": "primary",
      "amount": "0.001",
      "clientOrderId": "",
      "price": "1679.02",
      "timestampms": 1659201465222,
      "side": "SIDE_TYPE_SELL",
      "isAggressor": true,
      "feeAssetCode": "ETH",
      "feeAmount": "0.00000000000000000587",
      "orderId": 73716687406755680,
      "exchange": "gemini",
      "isAuctionFill": false,
      "isClearingFill": false,
      "symbol": "ETHUSD",
      "tid": 144115199446910500,
      "type": "trade"
    }
  ],
  "continuationToken": "daccgrp_1500611:n7126218738869976937315434496:a7126216029949884380085223424:m2:iForward"
}
json
Trade Response
application/json





REST API
Margin Trading (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Get Margin Account Summary
POST
https://api.gemini.com
/v1/margin/account
Retrieves comprehensive margin account information including collateral, leverage, buying/selling power, and liquidation risk.

This endpoint provides real-time margin statistics for spot margin trading accounts, helping you monitor your account health and manage risk.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Account Type
This endpoint is only available for margin trading accounts. Standard exchange accounts will receive an error.

Get Margin Account Summary ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Margin Account Summary ›Request Body
requeststring · required
The literal string "/v1/margin/account"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group.

Get Margin Account Summary ›Responses
200
400
401
403
404
429
500
Margin account summary with risk statistics

marginAssetValueobject · required

availableCollateralobject · required

notionalValueobject · required

totalBorrowedobject · required

leveragestring · decimal · required
The current leverage ratio (notionalValue / marginAssetValue)

Example: 1.5
buyingPowerobject · required

sellingPowerobject · required

reservedBuyOrdersobject · required

reservedSellOrdersobject · required

liquidationRiskobject

interestRateobject

POST/v1/margin/account

cURL
curl --request POST \
  --url https://api.gemini.com/v1/margin/account \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/margin/account",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/margin/account",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "marginAssetValue": {
    "currency": "USD",
    "value": "10000.00"
  },
  "availableCollateral": {
    "currency": "USD",
    "value": "8500.00"
  },
  "notionalValue": {
    "currency": "USD",
    "value": "15000.00"
  },
  "totalBorrowed": {
    "currency": "USD",
    "value": "5000.00"
  },
  "leverage": "1.5",
  "buyingPower": {
    "currency": "USD",
    "value": "8500.00"
  },
  "sellingPower": {
    "currency": "USD",
    "value": "8500.00"
  },
  "liquidationRisk": {
    "lossPercentage": "0.1550",
    "liquidationPrice": {
      "currency": "USD",
      "value": "50000.00"
    }
  },
  "interestRate": {
    "rate": "0.00001141552511",
    "interval": "hour"
  },
  "reservedBuyOrders": {
    "currency": "USD",
    "value": "1000.00"
  },
  "reservedSellOrders": {
    "currency": "USD",
    "value": "500.00"
  }
}
json
application/json
Get Margin Interest Rates
POST
https://api.gemini.com
/v1/margin/rates
Retrieves current margin interest rates for all borrowable assets.

Returns hourly, daily, and annual borrow rates for each currency that can be borrowed on margin. Interest is charged on borrowed amounts at the hourly rate and compounds over time.

Roles
The API key you use to access this endpoint must have the Trader, Fund Manager or Auditor role assigned. See Roles for more information.

The OAuth scope must have balances:read assigned to access this endpoint. See OAuth Scopes for more information.

Account Type
This endpoint is only available for margin trading accounts.

Get Margin Interest Rates ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Margin Interest Rates ›Request Body
requeststring · required
The literal string "/v1/margin/rates"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group.

Get Margin Interest Rates ›Responses
200
400
401
403
404
429
500
Current margin interest rates for all borrowable assets

ratesobject[] · required
Array of interest rates for all borrowable currencies


POST/v1/margin/rates

cURL
curl --request POST \
  --url https://api.gemini.com/v1/margin/rates \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/margin/rates",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/margin/rates",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "rates": [
    {
      "currency": "BTC",
      "borrowRate": "0.00001141552511",
      "borrowRateDaily": "0.00027397260264",
      "borrowRateAnnual": "0.1",
      "lastUpdated": 1700000000000
    },
    {
      "currency": "ETH",
      "borrowRate": "0.00001141552511",
      "borrowRateDaily": "0.00027397260264",
      "borrowRateAnnual": "0.1",
      "lastUpdated": 1700000000000
    },
    {
      "currency": "USD",
      "borrowRate": "0.00000913242009",
      "borrowRateDaily": "0.00021917808216",
      "borrowRateAnnual": "0.08",
      "lastUpdated": 1700000000000
    }
  ]
}
json
application/json
Preview Margin Order Impact
POST
https://api.gemini.com
/v1/margin/order/preview
Previews the margin impact of a hypothetical spot order without actually placing it.

Returns both pre-order and post-order margin risk statistics, allowing you to understand how an order would affect your margin account before execution. This is useful for risk management and planning trades.

Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

Account Type
This endpoint is only available for margin trading accounts.

Preview Margin Order Impact ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Preview Margin Order Impact ›Request Body
requeststring · required
The literal string "/v1/margin/order/preview"

noncerequired
The nonce, as described in Private API Invocation


symbolstring · required
The trading pair symbol (e.g., "btcusd")

Example: btcusd
sidestring · enum · required
The order side

Enum values:
buy
sell
Example: buy
typestring · enum · required
The order type

Enum values:
market
limit
Example: limit
amountstring · decimal
The order amount in base currency (required for limit orders and sell market orders)

Example: 0.5
pricestring · decimal
The limit price (required for limit orders)

Example: 50000.00
totalSpendstring · decimal
Total spend in quote currency (required for buy market orders)

Example: 25000.00
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group.

Preview Margin Order Impact ›Responses
200
400
401
403
404
429
500
Pre-order and post-order margin risk statistics

preorderobject · required

postorderobject · required

POST/v1/margin/order/preview

cURL
curl --request POST \
  --url https://api.gemini.com/v1/margin/order/preview \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/margin/order/preview",
  "nonce": "<nonce>",
  "symbol": "btcusd",
  "side": "buy",
  "type": "limit",
  "amount": "0.5",
  "price": "50000.00"
}
'
shell

Example Request Body
{
  "request": "/v1/margin/order/preview",
  "nonce": "<nonce>",
  "symbol": "btcusd",
  "side": "buy",
  "type": "limit",
  "amount": "0.5",
  "price": "50000.00"
}
json
Preview a limit buy order
application/json

Limit Buy Order Preview

Example Responses

200
{
  "preorder": {
    "marginAssetValue": {
      "currency": "USD",
      "value": "10000.00"
    },
    "availableCollateral": {
      "currency": "USD",
      "value": "8500.00"
    },
    "notionalValue": {
      "currency": "USD",
      "value": "15000.00"
    },
    "totalBorrowed": {
      "currency": "USD",
      "value": "5000.00"
    },
    "leverage": "1.5",
    "reservedBuyOrders": {
      "currency": "USD",
      "value": "0.00"
    },
    "reservedSellOrders": {
      "currency": "USD",
      "value": "0.00"
    },
    "buyingPower": {
      "currency": "USD",
      "value": "8500.00"
    },
    "sellingPower": {
      "currency": "USD",
      "value": "8500.00"
    }
  },
  "postorder": {
    "marginAssetValue": {
      "currency": "USD",
      "value": "10000.00"
    },
    "availableCollateral": {
      "currency": "USD",
      "value": "6000.00"
    },
    "notionalValue": {
      "currency": "USD",
      "value": "40000.00"
    },
    "totalBorrowed": {
      "currency": "USD",
      "value": "30000.00"
    },
    "leverage": "4.0",
    "reservedBuyOrders": {
      "currency": "USD",
      "value": "0.00"
    },
    "reservedSellOrders": {
      "currency": "USD",
      "value": "0.00"
    },
    "buyingPower": {
      "currency": "USD",
      "value": "6000.00"
    },
    "sellingPower": {
      "currency": "USD",
      "value": "6000.00"
    },
    "liquidationRisk": {
      "lossPercentage": "0.6000",
      "liquidationPrice": {
        "currency": "USD",
        "value": "30000.00"
      }
    }
  }
}
json
application/json


























REST API
Session (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Heartbeat
POST
https://api.gemini.com
/v1/heartbeat
This will prevent a session from timing out and canceling orders if the require heartbeat flag has been set. Note that this is only required if no other private API requests have been made. The arrival of any message resets the heartbeat timer.

Heartbeat ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Heartbeat ›Request Body
requeststring
The literal string /v1/heartbeat

nonce
The nonce, as described in Private API Invocation


Heartbeat ›Responses
200
400
401
403
404
429
500
The heartbeat was received successfully

resultstring
ok

Example: ok
POST/v1/heartbeat

cURL
curl --request POST \
  --url https://api.gemini.com/v1/heartbeat \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/heartbeat",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/heartbeat",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "result": "ok"
}
json
application/json
























REST API
Clearing (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Create New Clearing Order
POST
https://api.gemini.com
/v1/clearing/new
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:create assigned to access this endpoint. See OAuth Scopes for more information.

Create New Clearing Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Clearing Order ›Request Body
requeststring · required
The literal string "/v1/clearing/new"

noncerequired
The nonce, as described in Private API Invocation


symbolstring · required
The trading pair

amountstring · required
The amount to trade

pricestring · required
The price

sidestring · enum · required
The direction of the trade

Enum values:
buy
sell
counterparty_idstring
The counterparty ID

expires_in_hrsinteger
The number of hours until the order expires

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Create New Clearing Order ›Responses
200
400
401
403
404
429
500
Successful operation

clearing_idstring
The clearing ID

symbolstring
The trading pair

pricestring
The order price

amountstring
The order amount

sidestring · enum
Enum values:
buy
sell
statusstring
The order status

timestamp
timestamp


timestampmsinteger
The timestamp in milliseconds

is_confirmedboolean
Whether the order is confirmed

POST/v1/clearing/new

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/new \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/new",
  "nonce": "<nonce>",
  "counterparty_id": "OM9VNL1G",
  "expires_in_hrs": 24,
  "symbol": "btcusd",
  "amount": "100",
  "price": "9500.00",
  "side": "buy"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/new",
  "nonce": "<nonce>",
  "counterparty_id": "OM9VNL1G",
  "expires_in_hrs": 24,
  "symbol": "btcusd",
  "amount": "100",
  "price": "9500.00",
  "side": "buy"
}
json
JSON payload for creating a new clearing order
application/json

Example Responses

200
{
  "result": "AwaitConfirm",
  "clearing_id": "0OQGOZXW"
}
json
application/json
Get Clearing Order
POST
https://api.gemini.com
/v1/clearing/status
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Clearing Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Clearing Order ›Request Body
requeststring · required
The literal string "/v1/clearing/status"

noncerequired
The nonce, as described in Private API Invocation


clearing_idstring · required
The clearing ID

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Get Clearing Order ›Responses
200
400
401
403
404
429
500
Successful operation

clearing_idstring
The clearing ID

symbolstring
The trading pair

pricestring
The order price

amountstring
The order amount

sidestring · enum
Enum values:
buy
sell
statusstring
The order status

timestamp
timestamp


timestampmsinteger
The timestamp in milliseconds

is_confirmedboolean
Whether the order is confirmed

POST/v1/clearing/status

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/status \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/status",
  "nonce": "<nonce>",
  "clearing_id": "OM9VNL1G"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/status",
  "nonce": "<nonce>",
  "clearing_id": "OM9VNL1G"
}
json
JSON payload for checking clearing order status
application/json

Example Responses

200
{
  "result": "ok",
  "status": "Confirmed"
}
json
application/json
Cancel Clearing Order
POST
https://api.gemini.com
/v1/clearing/cancel
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:create assigned to access this endpoint. See OAuth Scopes for more information.

Cancel Clearing Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Cancel Clearing Order ›Request Body
requeststring · required
The literal string "/v1/clearing/cancel"

noncerequired
The nonce, as described in Private API Invocation


clearing_idstring · required
The clearing ID

accountstring
Required for Master API keys. The name of the account within the subaccount group.

Cancel Clearing Order ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the cancel operation

detailsstring
Detailed description of the result

POST/v1/clearing/cancel

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/cancel \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/cancel",
  "nonce": "<nonce>",
  "clearing_id": "P0521QDV"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/cancel",
  "nonce": "<nonce>",
  "clearing_id": "P0521QDV"
}
json
JSON payload for canceling a clearing order
application/json

Example Responses

200
{
  "result": "ok",
  "details": "P0521QDV order canceled"
}
json
JSON response for successful order cancellation
application/json

Successful Cancel
Confirm Clearing Order
POST
https://api.gemini.com
/v1/clearing/confirm
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:create assigned to access this endpoint. See OAuth Scopes for more information.

Confirm Clearing Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Confirm Clearing Order ›Request Body
requeststring · required
The literal string "/v1/clearing/confirm"

noncerequired
The nonce, as described in Private API Invocation


clearing_idstring · required
The clearing ID

symbolstring · required
The trading pair

amountstring · required
The amount to trade

pricestring · required
The price

sidestring · enum · required
The direction of the trade

Enum values:
buy
sell
accountstring
Required for Master API keys. The name of the account within the subaccount group.

Confirm Clearing Order ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the confirmation operation

POST/v1/clearing/confirm

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/confirm \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/confirm",
  "nonce": "<nonce>",
  "clearing_id": "OM9VNL1G",
  "symbol": "btcusd",
  "amount": "100",
  "price": "9500.00",
  "side": "sell"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/confirm",
  "nonce": "<nonce>",
  "clearing_id": "OM9VNL1G",
  "symbol": "btcusd",
  "amount": "100",
  "price": "9500.00",
  "side": "sell"
}
json
JSON payload for confirming a clearing order
application/json

Example Responses

200
{
  "result": "confirmed"
}
json
JSON response for successful order confirmation
application/json

Successful Confirmation
List Clearing Orders
POST
https://api.gemini.com
/v1/clearing/list
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:read assigned to access this endpoint. See OAuth Scopes for more information.

List Clearing Orders ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Clearing Orders ›Request Body
requeststring · required
The literal string "/v1/clearing/list"

noncerequired
The nonce, as described in Private API Invocation


symbolstring
Trading pair

counterpartystring
counterparty_id or counterparty_alias

sidestring · enum
"buy" or "sell"

Enum values:
buy
sell
expiration_start
UTC timestamp. Requires expiration_end if set


expiration_end
UTC timestamp. Requires expiration_start if set


submission_start
UTC timestamp. Requires submission_end if set


submission_end
UTC timestamp. Requires submission_start if set


fundedboolean
Default value false if not set

statusstring
Filter by status

timestamp
Only return orders after this timestamp


limit_ordersinteger
The maximum number of orders to return

accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Clearing Orders ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the operation

ordersobject[]

POST/v1/clearing/list

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/list \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/list",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/list",
  "nonce": "<nonce>"
}
json
Basic request to get clearing orders
application/json

Basic Request

Example Responses

200
{
  "result": "success",
  "orders": [
    {
      "clearing_id": "9LVQE9X5",
      "counterparty_id": "YZ43LX81",
      "symbol": "BTCEUR",
      "side": "sell",
      "price": 2,
      "quantity": 10,
      "status": "AwaitTargetConfirm",
      "submission": 1641790800020,
      "expiration": 1641963600000
    },
    {
      "clearing_id": "2MYR07XP",
      "order_id": "trade1SrcOrderId",
      "counterparty_id": "KQ4P3XWE",
      "broker_id": "WV4V1DGN",
      "symbol": "BTCEUR",
      "side": "buy",
      "price": 1,
      "quantity": 50,
      "status": "AwaitSourceConfirm",
      "submission": 1641790800016,
      "expiration": 1642222800000
    },
    {
      "clearing_id": "EM8WO7LQ",
      "order_id": "trade4SrcOrderId",
      "broker_id": "WV4V1DGN",
      "symbol": "BTCEUR",
      "side": "buy",
      "price": 4,
      "quantity": 8,
      "status": "AwaitSourceTargetConfirm",
      "submission": 1641790800028,
      "expiration": 1642136400000
    }
  ]
}
json
JSON response with clearing orders
application/json
List Clearing Brokers
POST
https://api.gemini.com
/v1/clearing/broker/list
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:read assigned to access this endpoint. See OAuth Scopes for more information.

List Clearing Brokers ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Clearing Brokers ›Request Body
requeststring · required
The literal string "/v1/clearing/broker/list"

noncerequired
The nonce, as described in Private API Invocation


symbolstring
Trading pair

expiration_start
UTC timestamp. Requires expiration_end if set


expiration_end
UTC timestamp. Requires expiration_start if set


submission_start
UTC timestamp. Requires submission_end if set


submission_end
UTC timestamp. Requires submission_start if set


fundedboolean
Default value false if not set

statusstring
Filter by status

timestamp
Only return orders after this timestamp


limit_ordersinteger
The maximum number of orders to return

accountstring
Required for Master API keys. The name of the account within the subaccount group.

List Clearing Brokers ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Status of the operation

ordersobject[]

POST/v1/clearing/broker/list

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/broker/list \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/broker/list",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/broker/list",
  "nonce": "<nonce>"
}
json
Basic request to get broker clearing orders
application/json

Basic Request

Example Responses

200
{
  "result": "success",
  "orders": [
    {
      "clearing_id": "9LVQ98X5",
      "source_counterparty_id": "R54L3DG1",
      "source_order_id": "trade1SrcOrderId",
      "target_counterparty_id": "KQ4P3XWE",
      "target_order_id": "trade1TgtOrderId",
      "symbol": "BTCEUR",
      "source_side": "buy",
      "price": 1,
      "quantity": 50,
      "status": "AwaitSourceConfirm",
      "submission": 1641790800016,
      "expiration": 1642222800000
    },
    {
      "clearing_id": "VXQ341X4",
      "source_counterparty_id": "R54L3DG1",
      "source_order_id": "trade4SrcOrderId",
      "symbol": "BTCEUR",
      "source_side": "buy",
      "price": 4,
      "quantity": 8,
      "status": "AwaitSourceTargetConfirm",
      "submission": 1641790800028,
      "expiration": 1642136400000
    }
  ]
}
json
JSON response with broker clearing orders
application/json
Create New Broker Order
POST
https://api.gemini.com
/v1/clearing/broker/new
Gemini Clearing also allows for brokers to facilitate trades between two Gemini customers. A broker can submit a new Gemini Clearing order that must then be confirmed by each counterparty before settlement.

Create New Broker Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Broker Order ›Request Body
requeststring · required
The literal string "/v1/clearing/broker/new"

noncerequired
The nonce, as described in Private API Invocation


source_counterparty_idstring · required
A symbol that corresponds with the counterparty sourcing the clearing trade

target_counterparty_idstring · required
A symbol that corresponds with the counterparty where the clearing trade is targeted

symbolstring · required
The symbol of the order

amountstring · decimal · required
Quoted decimal amount to purchase

expires_in_hrsinteger · float · required
The number of hours before the trade expires. Your counterparty will need to confirm the order before this time expires.

pricestring · decimal · required
Quoted decimal amount to spend per unit

sidestring · enum · required
"buy" or "sell". This side will be assigned to the source_counterparty_id. The opposite side will be sent to the target_counterparty_id

Enum values:
buy
sell
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the broker account on which to place the order. Only available for exchange accounts.

Create New Broker Order ›Responses
200
400
401
403
404
429
500
Successful operation

resultstring
Will return AwaitSourceTargetConfirm, meaning the order is waiting for both the source and the target parties to confirm the order

clearing_idstring
A unique identifier for the clearing order.

POST/v1/clearing/broker/new

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/broker/new \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/broker/new",
  "nonce": "<nonce>",
  "source_counterparty_id": "R485E04Q",
  "target_counterparty_id": "Z4929ZDY",
  "symbol": "ethusd",
  "amount": "175.00",
  "expires_in_hrs": 1,
  "price": "200",
  "side": "sell"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/broker/new",
  "nonce": "<nonce>",
  "source_counterparty_id": "R485E04Q",
  "target_counterparty_id": "Z4929ZDY",
  "symbol": "ethusd",
  "amount": "175.00",
  "expires_in_hrs": 1,
  "price": "200",
  "side": "sell"
}
json
Sample payload for broker order initiation
application/json

Example Responses

200
{
  "result": "AwaitSourceTargetConfirm",
  "clearing_id": "8EM7NVXD"
}
json
application/json
List Clearing Trades
POST
https://api.gemini.com
/v1/clearing/trades
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have clearing:read assigned to access this endpoint. See OAuth Scopes for more information.

List Clearing Trades ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Clearing Trades ›Request Body
requeststring · required
The literal string "/v1/clearing/trades"

noncerequired
The nonce, as described in Private API Invocation


timestamp_nanosinteger
Only return transfers on or after this timestamp in nanos

limit_per_accountinteger
The maximum number of clearing trades to return. The default is 100 and the maximum is 300.

accountstring
Only required when using a master api-key. The name of the account within the subaccount group.

symbolstring
The trading pair

timestamp
Only return trades after this timestamp


limit_tradesinteger
The maximum number of trades to return

List Clearing Trades ›Responses
200
400
401
403
404
429
500
Successful operation

resultsobject[]

POST/v1/clearing/trades

cURL
curl --request POST \
  --url https://api.gemini.com/v1/clearing/trades \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/clearing/trades",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/clearing/trades",
  "nonce": "<nonce>"
}
json
Basic request to get clearing trades
application/json

Basic Request

Example Responses

200
{
  "results": [
    {
      "sourceAccount": "primary",
      "targetAccount": "primary",
      "pair": "BTCUSD",
      "sourceSide": "buy",
      "price": "1",
      "quantity": "1000",
      "clearingId": "41M23L5Q",
      "status": "Settled",
      "expirationTimeMs": 1662567706120,
      "createdMs": 1662481306139,
      "lastUpdatedMs": 1662481561668,
      "hasBroker": false,
      "wasNotified": false
    },
    {
      "sourceAccount": "primary",
      "targetAccount": "primary",
      "pair": "BTCUSD",
      "sourceSide": "buy",
      "price": "12",
      "quantity": "1000",
      "clearingId": "0EMOYLJ5",
      "status": "AwaitTargetConfirm",
      "expirationTimeMs": 1662567728123,
      "createdMs": 1662481328126,
      "lastUpdatedMs": 1662481561415,
      "hasBroker": false,
      "wasNotified": true
    }
  ]
}
json
JSON response with clearing trades
application/json




REST API
Instant (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Get Instant Quote
POST
https://api.gemini.com
/v1/instant/quote
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Get Instant Quote ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Instant Quote ›Request Body
requeststring · required
The literal string "/v1/instant/quote/"

sidestring · enum · required
"buy" or "sell"

Enum values:
buy
sell
symbolstring · required
The symbol for the order. Instant includes order books denominated in a supported currency, as CCY2

noncerequired
The nonce, as described in Private API Invocation


totalSpendstring · required
Quoted decimal amount to spend on the order. Must comply with stated minimums. The totalSpend will be CCY2 in buy orders and CCY1 in sell orders.

paymentMethodUuidstring
uuid provided as bankId in Payment Methods API

paymentMethodTypestring
Method used to specify payment method in buy order. Can be "AccountBalancePaymentType" to use funds available in USD balance held on Gemini, "BankAccountType" to initial an ACH from a linked bank account, or "CardAccountType" to use a linked debit card to fund the purchase.

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Get Instant Quote ›Responses
200
400
401
403
404
429
500
Sample Responses

quoteIdinteger
Unique ID for the quote. This is used in the execution of the order

maxAgeMsinteger
Number of milliseconds until this quote price expires. Once expired, you will need to request a new quote

pairstring
The symbol passed in the quote request

pricestring
The quoted price of the asset. This will not change when attempting execution

priceCurrencystring
The currency in which the order is priced. Matches CCY2 in the symbol

sidestring · enum
Either "buy" or "sell"

Enum values:
buy
sell
quantitystring
The quantity of the asset to be bought or sold

quantityCurrencystring
The currency label for the quantity field. Matches CCY1 in the symbol

feestring
The fee quantity to be taken for the order upon execution

feeCurrencystring
The currency label for the order

depositFeestring
The deposit fee quantity. Will be applied if a debit card is used for the order. Will return 0 if there is no depositFee

depositFeeCurrencystring
Currency in which depositFee is taken

totalSpendstring
Total quantity to spend for the order. Will be the sum inclusive of all fees and amount to be traded.

totalSpendCurrencystring
Currency of the totalSpend to be spent on the order

POST/v1/instant/quote

cURL
curl --request POST \
  --url https://api.gemini.com/v1/instant/quote \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/instant/quote",
  "nonce": "<nonce>",
  "symbol": "btcusd",
  "side": "buy",
  "totalSpend": "100"
}
'
shell

Example Request Body
{
  "request": "/v1/instant/quote",
  "nonce": "<nonce>",
  "symbol": "btcusd",
  "side": "buy",
  "totalSpend": "100"
}
json
JSON payload for BTCUSD buy quote
application/json

Buy Quote Request

Example Responses

200
{
  "quoteId": 1328,
  "maxAgeMs": 60000,
  "pair": "BTCUSD",
  "price": "6445.07",
  "priceCurrency": "USD",
  "side": "buy",
  "quantity": "0.01505181",
  "quantityCurrency": "BTC",
  "fee": "2.9900309233",
  "feeCurrency": "USD",
  "depositFee": "0",
  "depositFeeCurrency": "USD",
  "totalSpend": "100",
  "totalSpendCurrency": "USD"
}
json
Sample BTCUSD Buy Response
application/json

BTC Buy Quote Response
Execute Instant Order
POST
https://api.gemini.com
/v1/instant/execute
Roles
The API key you use to access this endpoint must have the Trader role assigned. See Roles for more information.

The OAuth scope must have orders:create assigned to access this endpoint. See OAuth Scopes for more information.

Execute Instant Order ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Execute Instant Order ›Request Body
requeststring · required
The literal string "/v1/instant/execute"

noncerequired
The nonce, as described in Private API Invocation


symbolstring · required
The symbol for the order.

sidestring · enum · required
"buy" or "sell"

Enum values:
buy
sell
quantitystring · required
The quantity of the asset bought or sold. quantity must match quantity returned in the quote

feestring · required
The fee for the order. fee must match fee returned in the quote

quoteIdinteger · required
Unique ID for the quote. quoteId must match quoteId returned in the quote

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Execute Instant Order ›Responses
200
400
401
403
404
429
500
JSON response

orderIdinteger
The ID for the executed order

pairstring
The symbol for the order.

pricestring
The price at which the order was executed

priceCurrencystring
The currency in which the order is priced. Matches CCY2 in the symbol

sidestring
Either "buy" or "sell"

quantitystring
The quantity of the asset bought or sold

quantityCurrencystring
The currency label for the quantity field.

totalSpendstring
Total quantity to spend for the order. Will be the sum inclusive of all fees and amount to be traded.

totalSpendCurrencystring
Currency of the totalSpend to be spent on the order

feestring
The fee quantity charged for the order

feeCurrencystring
The currency label for the fee.

depositFeestring
The deposit fee quantity. Will be applied if a debit card is used for the order. Will return 0 if there is no depositFee

depositFeeCurrencystring
Currency in which depositFee is taken

POST/v1/instant/execute

cURL
curl --request POST \
  --url https://api.gemini.com/v1/instant/execute \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/instant/execute",
  "nonce": "<nonce>",
  "symbol": "BTCUSD",
  "side": "buy",
  "quantity": "0.01505181",
  "price": "6445.07",
  "fee": "2.9900309233",
  "quoteId": 1328
}
'
shell

Example Request Body
{
  "request": "/v1/instant/execute",
  "nonce": "<nonce>",
  "symbol": "BTCUSD",
  "side": "buy",
  "quantity": "0.01505181",
  "price": "6445.07",
  "fee": "2.9900309233",
  "quoteId": 1328
}
json
Sample Instant Order Execution Request Payload BTCUSD Buy
application/json

Execute Buy Instant Order

Example Responses

200
{
  "orderId": 375089415,
  "pair": "BTCUSD",
  "price": "6445.07",
  "priceCurrency": "USD",
  "side": "buy",
  "quantity": "0.01505181",
  "quantityCurrency": "BTC",
  "totalSpend": "100",
  "totalSpendCurrency": "USD",
  "fee": "2.9900309233",
  "feeCurrency": "USD",
  "depositFee": "0",
  "depositFeeCurrency": "USD"
}
json
Sample Response BTCUSD Buy
application/json

Sample BTCUSD Buy



Get Account Detail
POST
https://api.gemini.com
/v1/account
The account API will return detail about the specific account requested such as users, country codes, etc.

Roles
The API key you use to access this endpoint can be either a Master or Account level key with any role assigned. See Roles for more information.

Get Account Detail ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Account Detail ›Request Body
requeststring · required
The literal string "/v1/account"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Master API keys can get all account names using the Get Accounts endpoint.

Get Account Detail ›Responses
200
400
401
403
404
429
500
Successful operation

accountobject
Contains information on the requested account


usersobject[]
Contains an array of JSON objects with user information for the requested account


memo_reference_codestring
Returns wire memo reference code for linked bank account

virtual_account_numberstring
Virtual account number for the account. Only populated if applicable for the account

POST/v1/account

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account",
  "account": "primary",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/account",
  "account": "primary",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "account": {
    "accountName": "Primary",
    "shortName": "primary",
    "type": "exchange",
    "created": "1498245007981"
  },
  "users": [
    {
      "name": "Satoshi Nakamoto",
      "lastSignIn": "2020-07-21T13:37:39.453Z",
      "status": "Active",
      "countryCode": "US",
      "isVerified": true
    },
    {
      "name": "Gemini Support",
      "lastSignIn": "2018-07-11T20:04:36.073Z",
      "status": "Suspended",
      "countryCode": "US",
      "isVerified": false
    }
  ],
  "memo_reference_code": "GEMPJBRDZ",
  "virtual_account_number": "123456"
}
json
application/json
Create New Account
POST
https://api.gemini.com
/v1/account/create
A Master API key can create a new exchange account within the group. This API will return the name of your new account for use with the account parameter in when using Master API keys to perform account level functions. Please see the example.

Roles
The API key you use to access this endpoint must be a Master level key and have the Administrator role assigned. See Roles for more information.

Create New Account ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Create New Account ›Request Body
requeststring · required
The literal string "/v1/account/create"

noncerequired
The nonce, as described in Private API Invocation


namestring · required
A unique name for the new account

typestring
Either exchange or custody is accepted. Will generate an exchange account if exchange or parameter is missing. Will generate a custody account if custody.

Create New Account ›Responses
200
400
401
403
404
429
500
Successful operation

accountstring
Account reference string for use in APIs based off the provided name field

typestring
Will return the type of account generated. exchange if an exchange account was created, custody if a custody account was created

POST/v1/account/create

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account/create \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account/create",
  "nonce": "<nonce>",
  "name": "My Secondary Account",
  "type": "exchange"
}
'
shell

Example Request Body
{
  "request": "/v1/account/create",
  "nonce": "<nonce>",
  "name": "My Secondary Account",
  "type": "exchange"
}
json
JSON payload to create a new account
application/json

Example Responses

200
{
  "account": "my-secondary-account",
  "type": "exchange"
}
json
application/json
Rename Account
POST
https://api.gemini.com
/v1/account/rename
A Master or Account level API key can rename an account within the group.

Roles
The API key you use to access this endpoint can be either a Master or Account level API key and must have the Administrator role assigned. See Roles for more information.

Rename Account ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Rename Account ›Request Body
requeststring · required
The literal string "/v1/account/rename".

noncerequired
The nonce, as described in Private API Invocation


accountstring
Only required when using a master api-key. The shortname of the account within the subaccount group. Master API keys can get all account shortnames from the account field returned by the Get Accounts endpoint.

newNamestring
A unique name for the new account. If not provided, name will not change.

newAccountstring
A unique shortname for the new account. If not provided, shortname will not change.

Rename Account ›Responses
200
400
401
403
404
429
500
An element containing the updated name of the account.

namestring
New name for the account based off the provided newName field. Only returned if newName was provided in the request.

accountstring
New shortname for the account based off the provided newAccount field. Only returned if newAccount was provided in the request.

POST/v1/account/rename

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account/rename \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account/rename",
  "nonce": "<nonce>",
  "account": "my-exchange-account",
  "newName": "My Exchange Account New Name",
  "newAccount": "my-exchange-account-new-name"
}
'
shell

Example Request Body
{
  "request": "/v1/account/rename",
  "nonce": "<nonce>",
  "account": "my-exchange-account",
  "newName": "My Exchange Account New Name",
  "newAccount": "my-exchange-account-new-name"
}
json
JSON payload to rename an account
application/json

Example Responses

200
{
  "name": "My Exchange Account New Name",
  "account": "my-exchange-account-new-name"
}
json
application/json
List Accounts in Group
POST
https://api.gemini.com
/v1/account/list
A Master API key can be used to get the accounts within the group. A maximum of 500 accounts can be listed in a single API call.

Roles
The API key you use to access this endpoint must be a Master level key. See Roles for more information.

The OAuth scope must have account:read assigned to access this endpoint. See OAuth Scopes for more information.

List Accounts in Group ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Accounts in Group ›Request Body
requeststring · required
The literal string "/v1/account/list"

noncerequired
The nonce, as described in Private API Invocation


limit_accountsinteger
The maximum number of accounts to return. Maximum and default values are both 500.

timestamp
Only return accounts created on or before the supplied timestamp. If not provided, the 500 most recently created accounts are returned.


List Accounts in Group ›Responses
200
400
401
403
404
429
500
The response will be a JSON object containing all accounts within the master group

object[]

namestring
The name of the account provided upon creation

accountstring
Nickname of the specific account (will take the name given, remove all symbols, replace all " " with "-" and make letters lowercase)

typestring
Either "exchange" or "custody" depending on type of account

counterparty_idstring
The Gemini clearing counterparty ID associated with the API key making the request. Will return None for custody accounts

created
The timestamp of account creation, displayed as number of milliseconds since 1970-01-01 UTC. This will be transmitted as a JSON number


statusstring
Either "open" or "closed"

POST/v1/account/list

cURL
curl --request POST \
  --url https://api.gemini.com/v1/account/list \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/account/list",
  "nonce": "<nonce>",
  "limit_accounts": 100,
  "timestamp": 1632485834721
}
'
shell

Example Request Body
{
  "request": "/v1/account/list",
  "nonce": "<nonce>",
  "limit_accounts": 100,
  "timestamp": 1632485834721
}
json
application/json

Example Responses

200
[
  {
    "name": "Primary",
    "account": "primary",
    "type": "exchange",
    "counterparty_id": "EMONNYXH",
    "created": 1495127793000,
    "status": "open"
  },
  {
    "name": "My Custody Account",
    "account": "my-custody-account",
    "type": "custody",
    "counterparty_id": null,
    "created": 1565970772000,
    "status": "open"
  },
  {
    "name": "Other exchange account!",
    "account": "other-exchange-account",
    "type": "exchange",
    "counterparty_id": "EMONNYXK",
    "created": 1565970772000,
    "status": "closed"
  }
]
json
application/json
Roles Endpoint
POST
https://api.gemini.com
/v1/roles
The v1/roles endpoint will return a string of the role of the current API key. The response fields will be different for account-level and master-level API keys.

Roles Endpoint ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Roles Endpoint ›Request Body
requeststring · required
The literal string "/v1/roles"

Example: /v1/roles
nonceTimestampType · required
timestamp


Roles Endpoint ›Responses
200
The response will be a JSON object indicating the assigned roles to the set of API keys used to call /v1/roles. The Auditor role cannot be combined with other roles. Fund Manager and Trader can be combined.

isAuditorboolean · required
True if the Auditor role is assigned to the API keys. False otherwise.

isFundManagerboolean · required
True if the Fund Manager role is assigned to the API keys. False otherwise.

isTraderboolean · required
True if the Trader role is assigned to the API keys. False otherwise.

counterparty_idstring
Only returned for master-level API keys. The Gemini clearing counterparty ID associated with the API key making the request.

isAccountAdminboolean
Only returned for master-level API keys.True if the Administrator role is assigned to the API keys. False otherwise.

POST/v1/roles

cURL
curl --request POST \
  --url https://api.gemini.com/v1/roles \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/roles",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/roles",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
{
  "isAuditor": false,
  "isFundManager": true,
  "isTrader": true
}
json
Successful response for account-scoped key
application/json

Account-scoped key



REST API
OAuth (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Revoke OAuth Token
POST
https://api.gemini.com
/v1/oauth/revokeByToken
The access_token may be revoked at any time by using v1/oauth/revokeByToken. Once a token is revoked or expires, it can no longer be used to make requests.

This endpoint is only available using an access_token and will revoke the token used to make the request.

Revoke OAuth Token ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Revoke OAuth Token ›Request Body
requeststring · required
The literal string "/v1/oauth/revokeByToken"

Revoke OAuth Token ›Responses
200
400
401
403
404
429
500
An object that indicates the access_token has been revoked.

messagestring
A message that indicates the token has been revoked for the account

POST/v1/oauth/revokeByToken

cURL
curl --request POST \
  --url https://api.gemini.com/v1/oauth/revokeByToken \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/oauth/revokeByToken"
}
'
shell

Example Request Body
{
  "request": "/v1/oauth/revokeByToken"
}
json
JSON payload to revoke an OAuth token
application/json

Example Responses

200
{
  "message": "OAuth tokens and codes have been revoked for 00000000-0000-0000-0000-000000000000 on your account."
}
json
JSON response for a successful token revocation
application/json










REST API
Derivatives (1.0.0)
Endpoint

https://api.gemini.com


1.0.0

API information
Get Account Margin
POST
https://api.gemini.com
/v1/margin
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Account Margin ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Account Margin ›Request Body
requeststring · required
The API endpoint path

Example: /v1/margin
nonceTimestampType · required
timestamp


symbolstring · required
Trading pair symbol. See symbols and minimums

accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
Get Account Margin ›Responses
200
JSON object

margin_assets_valuestring · decimal
The $ equivalent value of all the assets available in the current trading account that can contribute to funding a derivatives position.

initial_marginstring · decimal
The $ amount that is being required by the accounts current positions and open orders.

available_marginstring · decimal
The difference between the margin_assets_value and initial_margin.

margin_maintenance_limitstring · decimal
The minimum amount of margin_assets_value required before the account is moved to liquidation status.

leveragestring · decimal
The ratio of Notional Value to Margin Assets Value.

notional_valuestring · decimal
The $ value of the current position.

estimated_liquidation_pricestring · decimal
The estimated price for the asset at which liquidation would occur.

initial_margin_positionsstring · decimal
The contribution to initial_margin from open positions.

reserved_marginstring · decimal
The contribution to initial_margin from open orders.

reserved_margin_buysstring · decimal
The contribution to initial_margin from open BUY orders.

reserved_margin_sellsstring · decimal
The contribution to initial_margin from open SELL orders.

buying_powerstring · decimal
The amount of that product the account could purchase based on current initial_margin and margin_assets_value.

selling_powerstring · decimal
The amount of that product the account could sell based on current initial_margin and margin_assets_value.

POST/v1/margin

cURL
curl --request POST \
  --url https://api.gemini.com/v1/margin \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/margin",
  "nonce": "<nonce>",
  "symbol": "BTC-GUSD-PERP"
}
'
shell

Example Request Body
{
  "request": "/v1/margin",
  "nonce": "<nonce>",
  "symbol": "BTC-GUSD-PERP"
}
json
application/json

Example Responses

200
{
  "margin_assets_value": "9800",
  "initial_margin": "6000",
  "available_margin": "3800",
  "margin_maintenance_limit": "5800",
  "leverage": "12.34567",
  "notional_value": "1300",
  "estimated_liquidation_price": "1300",
  "initial_margin_positions": "3500",
  "reserved_margin": "2500",
  "reserved_margin_buys": "1800",
  "reserved_margin_sells": "700",
  "buying_power": "0.19",
  "selling_power": "0.19"
}
json
application/json
List Funding Payments
POST
https://api.gemini.com
/v1/perpetuals/fundingPayment
Note that the response field 'instrumentSymbol' is only attached to requests from 16th April 2024 onwards.
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

List Funding Payments ›query Parameters
since
If specified, only return funding payments after this point. Default value is 24h in past. See Timestamps for more information

timestamp

to
If specified, only returns funding payment until this point. Default value is now. See Timestamps for more information

timestamp

List Funding Payments ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
List Funding Payments ›Request Body
requeststring · required
The API endpoint path

Example: /v1/perpetuals/fundingPayment
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
List Funding Payments ›Responses
200
The response will be an array of funding payment objects.

object[]

eventTypestring · enum · required
Event type

Enum values:
Hourly Funding Transfer
hourlyFundingTransferobject · required

POST/v1/perpetuals/fundingPayment

cURL
curl --request POST \
  --url https://api.gemini.com/v1/perpetuals/fundingPayment \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/perpetuals/fundingPayment",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/perpetuals/fundingPayment",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
[
  {
    "eventType": "Hourly Funding Transfer",
    "hourlyFundingTransfer": {
      "eventType": "Hourly Funding Transfer",
      "timestamp": 1683730803940,
      "assetCode": "GUSD",
      "action": "Debit",
      "quantity": {
        "currency": "GUSD",
        "value": "4.78958"
      }
    }
  },
  {
    "eventType": "Hourly Funding Transfer",
    "hourlyFundingTransfer": {
      "eventType": "Hourly Funding Transfer",
      "timestamp": 1683734406746,
      "assetCode": "GUSD",
      "action": "Debit",
      "quantity": {
        "currency": "GUSD",
        "value": "4.78958"
      },
      "instrumentSymbol": "BTCGUSDPERP"
    }
  }
]
json
application/json
Get Funding Payment Report File
GET
https://api.gemini.com
/v1/perpetuals/fundingpaymentreport/records.xlsx
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

Examples
&fromDate=2024-04-10&toDate=2024-04-25&numRows=1000
Compare and obtain the minimum records between (2024-04-10 to 2024-04-25) and 1000. If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch the minimum between 360 and 1000 records only.

&numRows=2024-04-10&toDate=2024-04-25
If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch 360 records only.

&numRows=1000
Fetch maximum 1000 records starting from Now to a historical date

<blank>
Fetch maximum 8760 records starting from Now to a historical date

Get Funding Payment Report File ›query Parameters
fromDatestring · date
If empty, will only fetch records by numRows value.

toDatestring · date
If empty, will only fetch records by numRows value.

numRowsinteger
If empty, default value '8760'

Get Funding Payment Report File ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Funding Payment Report File ›Request Body
requeststring · required
The API endpoint path

Example: /v1/perpetuals/fundingpaymentreport/records.xlsx
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
Get Funding Payment Report File ›Responses
200
400
404
429
500
XLSX file downloaded containing funding payment report.

string
GET/v1/perpetuals/fundingpaymentreport/records.xlsx

cURL
curl --request GET \
  --url https://api.gemini.com/v1/perpetuals/fundingpaymentreport/records.xlsx \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/perpetuals/fundingpaymentreport/records.xlsx?fromDate=2024-04-10&toDate=2024-04-25&numRows=1000",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/perpetuals/fundingpaymentreport/records.xlsx?fromDate=2024-04-10&toDate=2024-04-25&numRows=1000",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
No example specified for this content type
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
Get Funding Payment Report JSON
POST
https://api.gemini.com
/v1/perpetuals/fundingpaymentreport/records.json
This endpoint retrieves funding payment report in JSON format.

Examples
&fromDate=2024-04-10&toDate=2024-04-25&numRows=1000
Compare and obtain the minimum records between (2024-04-10 to 2024-04-25) and 1000. If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch the minimum between 360 and 1000 records only.

&numRows=2024-04-10&toDate=2024-04-25
If (2024-04-10 to 2024-04-25) contains 360 records. Then fetch 360 records only.

&numRows=1000
Fetch maximum 1000 records starting from Now to a historical date

<blank>
Fetch maximum 8760 records starting from Now to a historical date

Get Funding Payment Report JSON ›query Parameters
fromDatestring · date
If empty, will only fetch records by numRows value.

toDatestring · date
If empty, will only fetch records by numRows value.

numRowsinteger
If empty, default value '8760'

Get Funding Payment Report JSON ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Funding Payment Report JSON ›Request Body
requeststring · required
The API endpoint path

Example: /v1/perpetuals/fundingpaymentreport/records.json?fromDate=2024-04-10&toDate=2024-04-25&numRows=1000
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
Get Funding Payment Report JSON ›Responses
200
400
404
429
500
JSON response containing funding payment report.

object[]

eventTypestring · enum · required
Event type

Enum values:
Hourly Funding Transfer
timestamprequired
timestamp


assetCodestring · required
Asset symbol

actionstring · enum · required
Credit or Debit

Enum values:
Credit
Debit
quantityobject · required

instrumentSymbolstring
Symbol of the underlying instrument. Note that this is only attached to requests from 16th April 2024 onwards.

POST/v1/perpetuals/fundingpaymentreport/records.json

cURL
curl --request POST \
  --url https://api.gemini.com/v1/perpetuals/fundingpaymentreport/records.json \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/perpetuals/fundingpaymentreport/records.json?fromDate=2024-04-10&toDate=2024-04-25&numRows=1000",
  "nonce": "<nonce>"
}
'
shell

Example Request Body
{
  "request": "/v1/perpetuals/fundingpaymentreport/records.json?fromDate=2024-04-10&toDate=2024-04-25&numRows=1000",
  "nonce": "<nonce>"
}
json
application/json

Example Responses

200
[
  {
    "eventType": "Hourly Funding Transfer",
    "timestamp": 1713344403617,
    "assetCode": "GUSD",
    "action": "Credit",
    "quantity": {
      "currency": "GUSD",
      "value": "35.81084"
    },
    "instrumentSymbol": "BTCGUSDPERP"
  }
]
json
application/json
Get Open Positions
POST
https://api.gemini.com
/v1/positions
Roles
The API key you use to access this endpoint must have the Trader or Auditor role assigned. See Roles for more information.

The OAuth scope must have orders:read assigned to access this endpoint. See OAuth Scopes for more information.

Get Open Positions ›Headers
X-GEMINI-APIKEYstring · required
Your API key

X-GEMINI-SIGNATUREstring · required
HEX-encoded HMAC-SHA384 of payload signed with API secret

X-GEMINI-PAYLOADstring · required
Base64-encoded JSON payload

Content-Typestring
Default: text/plain
Content-Lengthstring
Default: 0
Cache-Controlstring
Default: no-cache
Get Open Positions ›Request Body
requeststring · required
The literal string "/v1/positions"

noncerequired
The nonce, as described in Private API Invocation


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which the orders were placed. Only available for exchange accounts.

Get Open Positions ›Responses
200
400
401
403
404
429
500
Successful operation

openPositionsobject[]

POST/v1/positions

cURL
curl --request POST \
  --url https://api.gemini.com/v1/positions \
  --header 'Content-Type: application/json' \
  --header 'X-GEMINI-APIKEY: <string>' \
  --header 'X-GEMINI-PAYLOAD: <string>' \
  --header 'X-GEMINI-SIGNATURE: <string>' \
  --data '
{
  "request": "/v1/positions",
  "nonce": "<nonce>",
  "account": "primary"
}
'
shell

Example Request Body
{
  "request": "/v1/positions",
  "nonce": "<nonce>",
  "account": "primary"
}
json
application/json

Example Responses

200
[
  {
    "symbol": "btcgusdperp",
    "instrument_type": "perp",
    "quantity": "0.2",
    "notional_value": "4000.036",
    "realised_pnl": "1234.5678",
    "unrealised_pnl": "999.946",
    "average_cost": "15000.45",
    "mark_price": "20000.18"
  }
]
json
application/json
Get Risk Stats
GET
https://api.gemini.com
/v1/riskstats/{symbol}
Get Risk Stats ›path Parameters
symbolstring · required
Perps Trading pair symbol


BTCGUSDPERP, etc. See symbols and minimums.

Get Risk Stats ›Responses
200
The response will be an json object

product_typestring · enum
Contract type for which the symbol data is fetched

Enum values:
PerpetualSwapContract
mark_pricestring · decimal
Current mark price at the time of request

index_pricestring · decimal
Current index price at the time of request

open_intereststring · decimal
string representation of decimal value of open interest

open_interest_notionalstring · decimal
string representation of decimal value of open interest notional

GET/v1/riskstats/{symbol}

cURL

curl --request GET \
  --url https://api.gemini.com/v1/riskstats/:symbol
shell

Example Responses

200
{
  "product_type": "PerpetualSwapContract",
  "mark_price": "30080.00",
  "index_price": "30079.046",
  "open_interest": "14.439",
  "open_interest_notional": "434325.12"
}
json
application/json





































































REST API
Schemas(1.0.0)

API information
TimestampType
oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Variant 1	type = string
Variant 2	type = integer
Properties for Variant 1:
string
Gemini strongly recommends using milliseconds instead of seconds for timestamps.

Timestamp format	Example	Supported request type
string (seconds)	1495127793	POST only
string (milliseconds)	1495127793000	POST only
Example: 1495127793000
Nonce
oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Variant 1	type = TimestampType
Variant 2	type = integer
Properties for Variant 1:
oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Variant 1	type = string
Variant 2	type = integer
Properties for Variant 1:
string
Gemini strongly recommends using milliseconds instead of seconds for timestamps.

Timestamp format	Example	Supported request type
string (seconds)	1495127793	POST only
string (milliseconds)	1495127793000	POST only
Example: 1495127793000
ErrorResponse
resultstring
Error

reasonstring
A short description

messagestring
Detailed error message

SymbolDetails
symbolstring
The requested symbol. See symbols and minimums

Example: BTCUSD
base_currencystring
CCY1 or the top currency. (i.e BTC in BTCUSD)

Example: BTC
quote_currencystring
CCY2 or the quote currency. (i.e USD in BTCUSD)

Example: USD
tick_sizenumber · decimal
The number of decimal places in the base_currency. (i.e 1e-8)

Example: 1e-8
quote_incrementnumber · decimal
The number of decimal places in the quote_currency (i.e 0.01)

Example: 0.01
min_order_sizestring
The minimum order size in base_currency units (i.e 0.00001)

Example: 0.00001
statusstring
Status of the current order book. Can be open, closed, cancel_only, post_only, limit_only.

Example: open
wrap_enabledboolean
When True, symbol can be wrapped using this endpoint:
POST https://api.gemini.com/v1/wrap/:symbol

Example: false
product_typestring
Instrument type spot / swap -- where swap signifies perpetual swap.

Example: spot
contract_typestring
vanilla / linear / inverse where vanilla is for spot while linear is for perpetual swap and inverse is a special case perpetual swap where the perpetual contract will be settled in base currency.

Example: vanilla
contract_price_currencystring
CCY2 or the quote currency for spot instrument (i.e. USD in BTCUSD) Or collateral currency of the contract in case of perpetual swap instrument.

Example: USD
Ticker
bidnumber · decimal
The highest bid currently available

Example: 977.59
asknumber · decimal
The lowest ask currently available

Example: 977.35
lastnumber · decimal
The price of the last executed trade

Example: 977.65
volumeobject
Information about the 24 hour volume on the exchange. See properties below


OrderBook
bidsobject[]
The bid price levels currently on the book. These are offers to buy at a given price.


asksobject[]
The ask price levels currently on the book. These are offers to sell at a given price.


OrderBookEntry
pricenumber · decimal
The price

amountnumber · decimal
The total quantity remaining at the price

timestamp
DO NOT USE - this field is included for compatibility reasons only and is just populated with a dummy value.


Trade
timestamp
The time that the trade was executed

Example: 1547146811

timestampms
The time that the trade was executed in milliseconds

Example: 1547146811357

tidinteger
The trade ID number

Example: 5335307668
pricestring · decimal
The price the trade was executed at

Example: 3610.85
amountstring · decimal
The amount that was traded

Example: 0.27413495
exchangestring
Will always be "gemini"

Example: gemini
typestring · enum
buy means that an ask was removed from the book by an incoming buy order.
sell means that a bid was removed from the book by an incoming sell order.
Enum values:
buy
sell
Example: buy
brokenboolean
Whether the trade was broken or not. Broken trades will not be displayed by default; use the include_breaks to display them.

Example: false
Heartbeat
requeststring
The literal string /v1/heartbeat

nonce
The nonce, as described in Private API Invocation


NewOrderRequest
requeststring · required
The literal string "/v1/order/new"

Example: /v1/order/new
noncenumber · required
The nonce, as described in Private API Invocation

symbolstring · required
The symbol for the new order

Example: BTCUSD
amountstring · required
Quoted decimal amount to purchase

Example: 5
pricestring · required
Quoted decimal amount to spend per unit

Example: 3633.00
sidestring · enum · required
Enum values:
buy
sell
Example: buy
typestring · enum · required
The order type. "exchange limit" for all order types except for stop-limit orders. "exchange stop limit" for stop-limit orders.

Enum values:
exchange limit
exchange stop limit
exchange market
Example: exchange limit
client_order_idstring
Recommended. A client-specified order id

optionsstring[]
An optional array containing at most one supported order execution option. See Order execution options for details.

Enum values:
maker-or-cancel
immediate-or-cancel
fill-or-kill
Example: ["maker-or-cancel"]
stop_pricestring
The price to trigger a stop-limit order. Only available for stop-limit orders.

margin_orderboolean
Set to true to place this order on a margin account using borrowed funds. Defaults to false. Only available for margin-enabled accounts. See Margin Trading for details.

Example: false
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

CancelOrderRequest
requeststring · required
The literal string "/v1/order/cancel"

Example: /v1/order/cancel
nonceTimestampType · required
timestamp


order_idinteger · required
The order ID given by /order/new

Example: 106817811
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the order. Only available for exchange accounts.

Example: primary
CancelAllOrdersRequest
requeststring · required
The literal string "/v1/order/cancel/all"

Example: /v1/order/cancel/all
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the orders. Only available for exchange accounts.

Example: primary
CancelAllOrdersBySessionRequest
requeststring · required
The literal string "/v1/order/cancel/session"

Example: /v1/order/cancel/session
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to cancel the orders. Only available for exchange accounts.

Example: primary
OrderStatusRequest
requeststring · required
The API endpoint path

Example: /v1/order/status
nonceTimestampType · required
timestamp


order_idinteger · required
The order id to get information on. The order_id represents a whole number and is transmitted as an unsigned 64-bit integer in JSON format. order_id cannot be used in combination with client_order_id.

Example: 123456789012345
accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
client_order_idstring
The client_order_id used when placing the order. client_order_id cannot be used in combination with order_id

include_tradesboolean
Either True or False. If True the endpoint will return individual trade details of all fills from the order.

MyTradesRequest
requeststring · required
The API endpoint path

Example: /v1/mytrades
nonceTimestampType · required
timestamp


accountstring
Required for Master API keys as described in Private API Invocation. The name of the account within the subaccount group. Specifies the account on which you intend to place the order. Only available for exchange accounts.

Example: primary
symbolstring
The symbol to retrieve trades for

Example: btcusd
limit_tradesinteger
The maximum number of trades to return. Default is 50, max is 500.

Example: 50
timestamp
Only return trades on or after this timestamp. See Data Types: Timestamps for more information. If not present, will show the most recent orders.

Example: 1591084414000

LimitOrderResponse
order_idstring
idstring
symbolstring
exchangestring
avg_execution_pricestring
sidestring · enum
Enum values:
buy
sell
typestring · enum
Enum values:
exchange limit
exchange stop limit
exchange market
timestampTimestampType
timestamp


timestampmsTimestampType
timestamp


is_liveboolean
is_cancelledboolean
is_hiddenboolean
was_forcedboolean
executed_amountstring
remaining_amountstring · double
client_order_idstring
optionsstring[]
pricestring · double
original_amountstring · double
StopLimitOrderResponse
order_idstring
idstring
symbolstring
exchangestring
avg_execution_pricestring
sidestring · enum
Enum values:
buy
sell
typestring · enum
Enum values:
exchange stop limit
timestamp
timestamp


timestampms
timestamp


is_liveboolean
is_cancelledboolean
is_hiddenboolean
was_forcedboolean
executed_amountstring
optionsstring[]
stop_pricestring · double
pricestring · double
original_amountstring · double
CancelOrderResponse
order_idstring · integer
idstring · integer
symbolstring
exchangestring
avg_execution_pricestring · double
sidestring · enum
Enum values:
buy
sell
typestring · enum
Enum values:
exchange limit
exchange stop limit
exchange market
timestamp
timestamp


timestampms
timestamp


is_liveboolean
is_cancelledboolean
is_hiddenboolean
was_forcedboolean
executed_amountstring · double
remaining_amountstring · double
reasonstring · enum
Enum values:
MakerOrCancelWouldTake
ExceedsPriceLimits
SelfCrossPrevented
ImmediateOrCancelWouldPost
FillOrKillWouldNotFill
Requested
MarketClosed
TradingClosed
optionsstring[]
pricestring · double
original_amountstring · double
Order
order_idstring · integer
The order id

client_order_idstring · integer
An optional client-specified order id

symbolstring
The symbol of the order

exchangestring
Will always be "gemini"

pricestring · decimal
The price the order was issued at

avg_execution_pricestring · decimal
The average price at which this order as been executed so far. 0 if the order has not been executed at all.

sidestring · enum
Enum values:
buy
sell
typestring · enum
Description of the order

Enum values:
exchange limit
exchange stop limit
exchange market
optionsstring[]
An array containing at most one supported order execution option. See Order execution options for details.

timestamp
The timestamp the order was submitted. Note that for compatibility reasons, this is returned as a string. We recommend using the timestampms field instead.


timestampms
The timestamp the order was submitted in milliseconds.


is_liveboolean
true if the order is active on the book (has remaining quantity and has not been canceled)

is_cancelledboolean
true if the order has been canceled. Note the spelling, "cancelled" instead of "canceled". This is for compatibility reasons.

reasonstring
Populated with the reason your order was canceled, if available.

was_forcedboolean
Will always be false.

executed_amountstring · decimal
The amount of the order that has been filled.

remaining_amountstring · decimal
The amount of the order that has not been filled.

original_amountstring · decimal
The originally submitted amount of the order.

is_hiddenboolean
Will always return false.

tradesobject[]
Contains an array of JSON objects with trade details.


CancelAllResult
resultstring
detailsobject
cancelledOrders/cancelRejects with IDs of both


MyTrade
pricestring
amountstring
timestamp
timestamp

Example: 1591084414

timestampms
timestamp

Example: 1591084414622

typestring · enum
Enum values:
Buy
Sell
Example: Buy
aggressorboolean
fee_currencystring
fee_amountstring
tidinteger
order_idstring
client_order_idstring
exchangestring
is_auction_fillboolean
breakstring · enum
Enum values:
trade correct
Example:
TradeVolume
symbolstring
base_currencystring
quote_currencystring
notional_currencystring
data_datestring
total_volume_basestring
maker_buy_sell_ratiostring
buy_maker_basestring
buy_maker_notionalstring
buy_maker_countinteger
sell_maker_basestring
sell_maker_notionalstring
sell_maker_countinteger
buy_taker_basestring
buy_taker_notionalstring
buy_taker_countinteger
sell_taker_basestring
sell_taker_notionalstring
sell_taker_countinteger
Balance
typestring · enum
Enum values:
exchange
Example: exchange
currencystring
The currency symbol

Example: BTC
amountnumber
The amount available

Example: 10.5
availablenumber
The amount available for trading

Example: 9
availableForWithdrawalnumber
The amount available for withdrawal

Example: 9
pendingWithdrawalnumber
The amount pending withdrawal

Example: 1
pendingDepositnumber
The amount pending deposit

Example: 0.5
NotionalVolume
datestring · date
last_updated_msinteger
web_maker_fee_bpsinteger
web_taker_fee_bpsinteger
web_auction_fee_bpsinteger
api_maker_fee_bpsinteger
api_taker_fee_bpsinteger
api_auction_fee_bpsinteger
fix_maker_fee_bpsinteger
fix_taker_fee_bpsinteger
fix_auction_fee_bpsinteger
notional_30d_volumestring
notional_1d_volumeobject[]

api_notional_30d_volumestring
fee_tierobject

NotionalBalance
currencystring
Currency code, see symbols and minimums

amountstring
The current balance

amountNotionalstring
Amount, in notional

availablestring
The amount that is available to trade

availableNotionalstring
Available, in notional

availableForWithdrawalstring
The amount that is available to withdraw

availableForWithdrawalNotionalstring
AvailableForWithdrawal, in notional

Address
addressstring
String representation of the cryptocurrency address

timestamp
Creation date of the address


labelstring
If you provided a label when creating the address, it will be echoed back here

memostring
It would be present if applicable, it will be present for cosmos address

networkstring
The blockchain network for the address

Transfer
typestring · enum
Enum values:
Deposit
Withdrawal
statusstring · enum
Enum values:
Complete
Pending
timestampms
The timestamp in milliseconds


eidinteger
The transfer ID

currencystring
The currency transferred

amountstring
The amount transferred

txHashstring
The transaction hash if applicable

InstantQuote
quoteIdinteger
Unique ID for the quote. This is used in the execution of the order

maxAgeMsinteger
Number of milliseconds until this quote price expires. Once expired, you will need to request a new quote

pairstring
The symbol passed in the quote request

pricestring
The quoted price of the asset. This will not change when attempting execution

priceCurrencystring
The currency in which the order is priced. Matches CCY2 in the symbol

sidestring · enum
Either "buy" or "sell"

Enum values:
buy
sell
quantitystring
The quantity of the asset to be bought or sold

quantityCurrencystring
The currency label for the quantity field. Matches CCY1 in the symbol

feestring
The fee quantity to be taken for the order upon execution

feeCurrencystring
The currency label for the order

depositFeestring
The deposit fee quantity. Will be applied if a debit card is used for the order. Will return 0 if there is no depositFee

depositFeeCurrencystring
Currency in which depositFee is taken

totalSpendstring
Total quantity to spend for the order. Will be the sum inclusive of all fees and amount to be traded.

totalSpendCurrencystring
Currency of the totalSpend to be spent on the order

ClearingOrder
clearing_idstring
The clearing ID

symbolstring
The trading pair

pricestring
The order price

amountstring
The order amount

sidestring · enum
Enum values:
buy
sell
statusstring
The order status

timestamp
The timestamp


timestampmsinteger
The timestamp in milliseconds

is_confirmedboolean
Whether the order is confirmed

Account
namestring
The account name

account_idstring
The account ID

is_defaultboolean
Whether the account is the default account

createdstring
The creation date

Transaction
oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Trade Reponse	type = object
Transfer Reponse	type = object
Properties for Trade Reponse:
Trade Reponse
accountstring
The account.

amountstring
The quantity that was executed.

clientOrderIdstring
The client order ID, if defined. Otherwise an empty string.

pricestring
The price that the execution happened at.

timestampms
The time that the trade happened in milliseconds.


sidestring
Indicating the side of the original order.

isAggressorboolean
If true, this order was the taker in the trade.

feeAssetCodestring
The symbol that the trade was for

feeAmountstring
The fee amount charged

orderIdinteger · int64
The order that this trade executed against.

exchangestring
Will always be "gemini".

isAuctionFillboolean
True if the trade was a auction trade and not an on-exchange trade.

isClearingFillboolean
True if the trade was a clearing trade and not an on-exchange trade.

tidinteger · int64
The trade ID.

symbolstring
The symbol that the trade was for.

RevokeOauthTokenResponse
messagestring
A message that indicates the token has been revoked for the account

NetworkToken
tokenstring
The requested token identifier.

networkstring[]
Array of supported blockchain networks for the token. Many tokens (especially stablecoins like USDC, USDT) are available on multiple networks.

Supported networks include: bitcoin, ethereum, solana, optimism, arbitrum, base, monad, avalanche, litecoin, bitcoincash, dogecoin, zcash, filecoin, tezos, polkadot, cosmos, xrpl, linea, and more.

Example: ["optimism","solana","base","arbitrum","monad","avalanche","ethereum"]
FeePromos
symbolsstring[]
Symbols that currently have fee promos

PriceFeedResponse
object[]

pairstring
Trading pair symbol. See symbols and minimums

pricestring
Current price of the pair on the Gemini order book

percentChange24hstring
24 hour change in price of the pair on the Gemini order book

ApprovedAddress
networkstring
The network of the approved address. Network can be bitcoin, ethereum, bitcoincash, litecoin, zcash, filecoin, dogecoin, tezos, solana, polkadot, avalanche, cosmos, or xrpl

scopestring
Will return the scope of the address as either "account" or "group"

labelstring
The label assigned to the address

statusstring
The status of the address that will return as "active", "pending-time" or "pending-mua". The remaining time is exactly 7 days after the initial request. "pending-mua" is for multi-user accounts and will require another administator or fund manager on the account to approve the address.

createdAtstring
UTC timestamp in millisecond of when the address was created.

addressstring
The address on the approved address list.

OpenPosition
symbolstring
The symbol of the order.

instrument_typestring
The type of instrument. Either "spot" or "perp".

quantitystring · decimal
The position size. Value will be negative for shorts.

notional_valuestring · decimal
The value of position; calculated as (quantity * mark_price). Value will be negative for shorts.

realised_pnlstring · decimal
The current P&L that has been realised from the position.

unrealised_pnlstring · decimal
Current Mark to Market value of the positions.

average_coststring · decimal
The average price of the current position.

mark_pricestring · decimal
The current Mark Price for the Asset or the position.

FundingAmountResponse
symbolstring
The requested symbol. See symbols and minimums

fundingDateTimestring
UTC date time in format yyyy-MM-ddThh:mm:ss.SSSZ format

fundingTimestampMilliSecsnumber · long
Current funding amount Epoc time.

nextFundingTimestampnumber · long
Next funding amount Epoc time.

amountnumber · decimal
The dollar amount for a Long 1 position held in the symbol for funding period (1 hour)

estimatedFundingAmountnumber · decimal
The estimated dollar amount for a Long 1 position held in the symbol for next funding period (1 hour)

StakingBalance
typestring
Will always be "Staking"

Example: Staking
currencystring
Currency code, see symbols and minimums

Example: MATIC
balancenumber · decimal
The current Staking balance

Example: 10
availablenumber · decimal
The amount that is available to trade

Example: 0
availableForWithdrawalnumber · decimal
The Staking amount that is available to redeem to exchange account

Example: 10
balanceByProviderobject

StakingDeposit
transactionIdstring
A unique identifier for the staking transaction

Example: 65QN4XM5
providerIdstring
Provider Id, in uuid4 format

Example: 62b21e17-2534-4b9f-afcf-b7edb609dd8d
currencystring
Currency code, see symbols

Example: MATIC
amountnumber · decimal
The amount deposited

Example: 30
accrualTotalnumber · decimal
The total accrual

ratesobject
A JSON object including one or many rates. If more than one rate it would be an array of rates.


StakingTransaction
transactionIdstring
A unique identifier for the staking transaction

Example: MPZ7LDD8
transactionTypestring · enum
Can be any one of the following - Deposit, Redeem, Interest, RedeemPayment, AdminRedeem, AdminCreditAdjustment, AdminDebitAdjustment

Enum values:
Deposit
Redeem
Interest
RedeemPayment
AdminRedeem
AdminCreditAdjustment
AdminDebitAdjustment
Example: Redeem
amountCurrencystring
Currency code

Example: MATIC
amountnumber · decimal
The amount that is defined by the transactionType above

Example: 20
priceCurrencystring
A supported three-letter fiat currency code, e.g. usd

Example: USD
priceAmountnumber · decimal
Current market price of the underlying token at the time of the reward

Example: 0.1
dateTime
The time of the transaction in milliseconds

Example: 1667418560153

StakingHistory
providerIdstring
Provider Id, in uuid4 format

Example: 62b21e17-2534-4b9f-afcf-b7edb609dd8d
transactionsobject[]

StakingRate
providerIdstring
Provider Id, in uuid4 format

Example: 62bb4d27-a9c8-4493-a737-d4fa33994f1f
rateinteger
Staking interest rate in bps (Expressed as a simple rate. Interest on Staking balances compounds daily. In mobile and web applications, APYs are derived from this rate and rounded to 1/10th of a percent.)

Example: 429.386
apyPctnumber · decimal
Staking interest APY (Expressed as a percentage derived from the rate and rounded to 1/10th of a percent.)

Example: 4.39
ratePctnumber · decimal
rate expressed as a percentage

Example: 4.29386
depositUsdLimitinteger
Maximum new amount in USD notional of this crypto that can participate in Gemini Staking per account per month

Example: 500000
StakingRateProvider
Currency Symbol Keys
currency_symbolobject

StakingRateResponse
Provider UUID Keys
provider_uuidobject
Currency Symbol Keys


StakingRewardPeriod
providerIdstring
Provider Id, in uuid4 format

Example: 62b21e17-2534-4b9f-afcf-b7edb609dd8d
currencystring
Currency code, see symbols

Example: MATIC
apyPctnumber · decimal
Staking reward rate expressed as an APY at time of accrual. Interest on Staking balances compounds daily based on the simple rate which is available from /v1/staking/rates/

Example: 5.75
ratePctnumber · decimal
Rate expressed as a percentage

Example: 5.592369
numberOfAccrualsinteger
Number of accruals in the specific aggregate, typically one per day. If the rate is adjusted, new accruals are added.

Example: 1
accrualTotalnumber · decimal
The total accrual

Example: 0.0065678
firstAccrualAtstring
Time of first accrual. In iso datetime with timezone format

Example: 2022-08-23T20:00:00.000Z
lastAccrualAtstring
Time of last accrual. In iso datetime with timezone format

Example: 2022-08-23T20:00:00.000Z
StakingRewards
providerIdstring
Provider Id, in uuid4 format

Example: 62b21e17-2534-4b9f-afcf-b7edb609dd8d
currencystring
Currency code, see symbols

Example: MATIC
accrualTotalnumber · decimal
The total accrual

Example: 0.103994
ratePeriodsobject[]
Array of JSON objects with period accrual information


StakingRewardsProvider
Currency Symbol Keys
currency_symbolobject

StakingRewardsResponse
Provider UUID Keys
provider_uuidobject
Currency Symbol Keys


StakingWithdrawal
transactionIdstring
A unique identifier for the staking transaction

Example: MPZ7LDD8
amountnumber · decimal
The amount deposited

Example: 20
amountPaidSoFarnumber · decimal
The amount redeemed successfully

Example: 20
amountRemainingnumber · decimal
The amount pending to be redeemed

Example: 0
currencystring
Currency code

Example: MATIC
requestInitiatedstring
In ISO datetime with timezone format

Example: 2022-11-02T19:49:20.153Z
FeeEstimateRequest
requeststring · required
The string /v1/withdraw/{currencyCodeLowerCase}/feeEstimate where :currencyCodeLowerCase is replaced with the currency code of a supported crypto-currency, e.g. eth, aave, etc. See Symbols and minimums

Example: /v1/withdraw/eth/feeEstimate
noncerequired
The nonce, as described in Private API Invocation


addressstring · required
Standard string format of cryptocurrency address

Example: 0x31c2105b8dea834167f32f7ea7d877812e059230
amountstring · required
Quoted decimal amount to withdraw

Example: 0.01
accountstring · required
The name of the account within the subaccount group.

Example: primary
FeeEstimateResponse
currencystring
Currency code, see symbols.

Example: ETH
feestring
The estimated gas fee

Example: {currency: 'ETH', value: '0'}
isOverrideboolean
Value that shows if an override on the customer's account for free withdrawals exists

Example: false
monthlyLimitinteger
Total nunber of allowable fee-free withdrawals

Example: 1
monthlyRemaininginteger
Total number of allowable fee-free withdrawals left to use

Example: 1
RoleResponse
isAuditorboolean · required
True if the Auditor role is assigned to the API keys. False otherwise.

isFundManagerboolean · required
True if the Fund Manager role is assigned to the API keys. False otherwise.

isTraderboolean · required
True if the Trader role is assigned to the API keys. False otherwise.

counterparty_idstring
Only returned for master-level API keys. The Gemini clearing counterparty ID associated with the API key making the request.

isAccountAdminboolean
Only returned for master-level API keys.True if the Administrator role is assigned to the API keys. False otherwise.

MarginResponse
margin_assets_valuestring · decimal
The $ equivalent value of all the assets available in the current trading account that can contribute to funding a derivatives position.

initial_marginstring · decimal
The $ amount that is being required by the accounts current positions and open orders.

available_marginstring · decimal
The difference between the margin_assets_value and initial_margin.

margin_maintenance_limitstring · decimal
The minimum amount of margin_assets_value required before the account is moved to liquidation status.

leveragestring · decimal
The ratio of Notional Value to Margin Assets Value.

notional_valuestring · decimal
The $ value of the current position.

estimated_liquidation_pricestring · decimal
The estimated price for the asset at which liquidation would occur.

initial_margin_positionsstring · decimal
The contribution to initial_margin from open positions.

reserved_marginstring · decimal
The contribution to initial_margin from open orders.

reserved_margin_buysstring · decimal
The contribution to initial_margin from open BUY orders.

reserved_margin_sellsstring · decimal
The contribution to initial_margin from open SELL orders.

buying_powerstring · decimal
The amount of that product the account could purchase based on current initial_margin and margin_assets_value.

selling_powerstring · decimal
The amount of that product the account could sell based on current initial_margin and margin_assets_value.

MoneyAmount
currencystring · required
The currency code (e.g., "USD", "BTC", "ETH")

Example: USD
valuestring · decimal · required
The amount in the specified currency

Example: 10000.00
LiquidationRisk
lossPercentagestring · decimal · required
The percentage loss from current value that would trigger liquidation, formatted as decimal (e.g., "0.1550" = 15.50%)

Example: 0.1550
liquidationPriceobject
The estimated price at which liquidation would occur (optional, may not be present for all positions)


InterestRateInfo
ratestring · decimal · required
The interest rate as a decimal string

Example: 0.00001141552511
intervalstring · enum · required
The time interval for the rate (currently only "hour" is supported)

Enum values:
hour
Example: hour
MarginAccountSummary
marginAssetValueobject · required
The total value of all assets available in the margin account that can contribute to funding positions


availableCollateralobject · required
The amount of collateral available for new positions or withdrawals


notionalValueobject · required
The total value of all open positions


totalBorrowedobject · required
The total amount currently borrowed across all currencies


leveragestring · decimal · required
The current leverage ratio (notionalValue / marginAssetValue)

Example: 1.5
buyingPowerobject · required
The maximum value that can be purchased with available collateral


sellingPowerobject · required
The maximum value that can be sold with available collateral


reservedBuyOrdersobject · required
Collateral reserved for open buy orders


reservedSellOrdersobject · required
Collateral reserved for open sell orders


liquidationRiskobject
Liquidation risk information (only present if positions exist)


interestRateobject
Current interest rate on borrowed amounts (only present if borrows exist)


MarginInterestRate
currencystring · required
The currency code (e.g., "BTC", "ETH", "USD")

Example: BTC
borrowRatestring · decimal · required
The hourly borrow rate as a decimal

Example: 0.00001141552511
borrowRateDailystring · decimal · required
The daily borrow rate (hourly rate × 24)

Example: 0.00027397260264
borrowRateAnnualstring · decimal · required
The annualized borrow rate (daily rate × 365)

Example: 0.1
lastUpdatedinteger · int64 · required
Unix timestamp in milliseconds when the rate was last updated

Example: 1700000000000
MarginRatesResponse
ratesobject[] · required
Array of interest rates for all borrowable currencies


MarginRiskStats
marginAssetValueobject · required
The total value of all assets available in the margin account


availableCollateralobject · required
The amount of collateral available for new positions


notionalValueobject · required
The total value of all open positions


totalBorrowedobject · required
The total amount currently borrowed


leveragestring · decimal · required
The leverage ratio

Example: 1.5
reservedBuyOrdersobject · required
Collateral reserved for open buy orders


reservedSellOrdersobject · required
Collateral reserved for open sell orders


buyingPowerobject · required
The maximum value that can be purchased


sellingPowerobject · required
The maximum value that can be sold


liquidationRiskobject
Liquidation risk information (only present if applicable)


MarginOrderPreview
preorderobject · required
Margin risk statistics before the order would be executed


postorderobject · required
Margin risk statistics after the order would be executed


Quantity
currencystring · required
The currency code of the quantity.

valuestring · decimal · required
The value of the quantity.

FundingTransfer
eventTypestring · required
Event type

timestamprequired
Time of the funding payment


assetCodestring · required
Asset symbol

actionstring · enum · required
Credit or Debit

Enum values:
Credit
Debit
quantityobject · required
A nested JSON object describing the transaction amount


instrumentSymbolstring
Symbol of the underlying instrument. Note that this is only attached to requests from 16th April 2024 onwards.

FundingPayment
eventTypestring · enum · required
Event type

Enum values:
Hourly Funding Transfer
hourlyFundingTransferobject · required

FundingPaymentReportItem
eventTypestring · enum · required
Event type

Enum values:
Hourly Funding Transfer
timestamprequired
Time of the funding payment


assetCodestring · required
Asset symbol

actionstring · enum · required
Credit or Debit

Enum values:
Credit
Debit
quantityobject · required
A nested JSON object describing the transaction amount


instrumentSymbolstring
Symbol of the underlying instrument. Note that this is only attached to requests from 16th April 2024 onwards.

RiskStatsResponse
product_typestring · enum
Contract type for which the symbol data is fetched

Enum values:
PerpetualSwapContract
mark_pricestring · decimal
Current mark price at the time of request

index_pricestring · decimal
Current index price at the time of request

open_intereststring · decimal
string representation of decimal value of open interest

open_interest_notionalstring · decimal
string representation of decimal value of open interest notional

FxRate
fxPairstring
The requested currency pair

Example: AUDUSD
ratenumber · double
The exchange rate

Example: 0.69
asOf
The timestamp (in Epoch time format) that the requested fxrate has been retrieved for

Example: 1594651859000

providerstring
The market data provider

Example: bcb
benchmarkstring
The market for which the retrieved price applies to

Example: Spot
Candle
array

oneOf
Exactly one variant must match.
Decision Table
Variant	Matching Criteria
Variant 1	type = integer
Variant 2	type = number
Properties for Variant 1:
integer · int64
Timestamp in milliseconds

CandleResponse
Candlearray

TickerInfo
symbolstring
The trading pair symbol

Example: BTCUSD
openstring · decimal
Open price from 24 hours ago

Example: 9121.76
highstring · decimal
High price from 24 hours ago

Example: 9440.66
lowstring · decimal
Low price from 24 hours ago

Example: 9106.51
closestring · decimal
Close price (most recent trade)

Example: 9347.66
changesstring[]
Hourly prices descending for past 24 hours

Example: ["9365.1","9386.16","9373.41","9322.56","9268.89","9265.38"]
bidstring · decimal
Current best bid

Example: 9345.70
askstring · decimal
Current best offer

Example: 9347.67
On this page
TimestampType
Nonce
ErrorResponse
SymbolDetails
Ticker
OrderBook
OrderBookEntry
Trade
Heartbeat
NewOrderRequest
CancelOrderRequest
CancelAllOrdersRequest
CancelAllOrdersBySessionRequest
OrderStatusRequest
MyTradesRequest
LimitOrderResponse
StopLimitOrderResponse
CancelOrderResponse
Order
CancelAllResult
MyTrade
TradeVolume
Balance
NotionalVolume
NotionalBalance
Address
Transfer
InstantQuote
ClearingOrder
Account
Transaction
RevokeOauthTokenResponse
NetworkToken
FeePromos
PriceFeedResponse
ApprovedAddress
OpenPosition
FundingAmountResponse
StakingBalance
StakingDeposit
StakingTransaction
StakingHistory
StakingRate
StakingRateProvider
StakingRateResponse
StakingRewardPeriod
StakingRewards
StakingRewardsProvider
StakingRewardsResponse
StakingWithdrawal
FeeEstimateRequest
FeeEstimateResponse
RoleResponse
MarginResponse
MoneyAmount
LiquidationRisk
InterestRateInfo
MarginAccountSummary
MarginInterestRate
MarginRatesResponse
MarginRiskStats
MarginOrderPreview
Quantity
FundingTransfer
FundingPayment
FundingPaymentReportItem
RiskStatsResponse
FxRate
Candle
CandleResponse
TickerInfo







































































































Introduction

Copy page

Version: 0.10.7 • Status: Production • Public URL: wss://ws.gemini.com

Our WebSocket API provides low latency access to real-time market data and order execution for professional traders and institutions. Built from the ground up for performance, our WebSocket API delivers fastest latency on AWS with enterprise-grade reliability.

🚀 Try It Now with our interactive documentation

Key Features
Low Latency - Sub-10ms market data updates for competitive advantage
Real-Time Trading - Place, modify, and cancel orders via WebSocket
Multiple Streams - Subscribe to multiple markets simultaneously
Performance Tiers
Tier	Target	Description
Tier 2 (Public Internet)	p99~15ms	Public offering connecting to AWS us-east-1 over the public internet. Provides good baseline performance with minimal setup complexity.
Tier 1 (In Region)	p99~10ms	Direct connection to us-east-1 feed. Provides improved performance a step above the public offering but requires onboarding to peer to our infrastructure.
Tier 0 (Local Zone)	p99~5ms	Best performance outside of NY5, physically closest to our data center. Requires onboarding similar to us-east-1.



Authentication

Copy page

Generate an API Key
API keys for our WebSocket API have special requirements:

Navigate to API Settings
Click "Create API key"
Scope: Select the account you want to trade with
Settings:
✅ Enable "Uses a time-based nonce"
✅ Enable "Trading"
Save your API key and secret securely
Only account-scoped keys with time-based nonces are accepted.

Create an Authenticated Connection
Pass the following headers when establishing the websocket connection,

Header	Value
X-GEMINI-APIKEY	Your Gemini API key (session key)
X-GEMINI-NONCE	Current epoch timestamp in seconds
X-GEMINI-SIGNATURE	hex(HMAC_SHA384(base64(nonce), key=api_secret))
X-GEMINI-PAYLOAD	base64(nonce)
Authentication is required for trading operations and order event subscriptions. Market data streams are available without authentication.

Authentication headers must be provided during the initial WebSocket handshake—you cannot authenticate after the connection is established.

Signature Generation Step-by-Step
Code

# Create a nonce from the current epoch time in seconds
nonce = current_timestamp_in_seconds
# Our payload will be the base64 encoded nonce for simplicity
payload = base64_encode(nonce.toString)
# Generate a signature using the hmac_sha384 algorithm
signature = hmac_sha384(payload, api_secret)
# Convert the signature to hex so it can be passed in the headers
hexSignature = hex(signature)


Message Format

Copy page

Our WebSocket API uses JSON-formatted messages for all communication.

Request Format
All requests follow a consistent structure:

Code

{
  "id": "1",
  "method": "METHOD_NAME",
  "params": {...}
}
Field	Type	Required	Description
id	string | number	Yes	Unique identifier for matching request/response
method	string	Yes	The method to invoke
params	object | array	No	Method parameters (varies by method)
Response Format
Successful responses include the request ID and result:

Code

{
  "id": "1",
  "status": 200,
  "result": {...}
}
Field	Type	Description
id	string | number	Matches the request ID
status	number	HTTP status code
result	any	Method-specific response data
Error Response
Error responses include error details:

Code

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
Field	Type	Description
id	string | number	Matches the request ID
status	number	HTTP status code
error.code	number	Internal error code
error.msg	string	Human-readable error message
Error Codes
Code	HTTP Status	Description
-1000	500	Internal server error
-1002	401	Authentication required
-1003	429	Rate limit exceeded
-1013	400	Invalid parameters
-1020	400	Unsupported operation
-2010	400	Order rejected





Stream Reference

Copy page

Our WebSocket API provides multiple data streams for various exchange data:

L2 Order Book Data
Trade Events
Per Account Order Events
Book Ticker
Schema	Frequency	Description
{symbol}@bookTicker	Real-time	Real time updates to the best bid/ask price for an order book.
Try It
btcusd@bookTicker
disconnected
Send
Code

{
  "u": 1751505576085,
  "E": 1751508438600117161,
  "s": "btcusd",
  "b": "45000.50",
  "B": "1.25000000",
  "a": "45001.00",
  "A": "0.75000000"
}
Field	Type	Description
u	number	Update ID
E	number	Event time (nanoseconds)
s	string	Symbol
b	string	Best bid price
B	string	Best bid quantity
a	string	Best ask price
A	string	Best ask quantity
L2 Partial Depth Streams
Schema	Frequency	Description
{symbol}@depth5	Periodic (1s)	Periodic snapshot of the top 5 levels once per second
{symbol}@depth10	Periodic (1s)	Top 10 levels
{symbol}@depth20	Periodic (1s)	Top 20 levels
{symbol}@depth5@100ms	Periodic (100ms)	Top 5 levels every 100 milliseconds
{symbol}@depth10@100ms	Periodic (100ms)	Top 10 levels
{symbol}@depth20@100ms	Periodic (100ms)	Top 20 levels
Try It
btcusd@depth10@100ms
disconnected
Send
Code

{
  "lastUpdateId": 12345678,
  "bids": [
    ["45000.50", "1.25000000"],
    ["45000.25", "0.50000000"]
  ],
  "asks": [
    ["45001.00", "0.75000000"],
    ["45001.25", "2.00000000"]
  ]
}
Field	Type	Description
lastUpdateId	number	Last update ID
bids	array	Array of [price, quantity]
asks	array	Array of [price, quantity]
L2 Differential Depth Streams
Schema	Frequency	Description
{symbol}@depth	Periodic (1s)	List of all changed price levels in the last second
{symbol}@depth@100ms	Periodic (100ms)	In the last 100 milliseconds
Try It
btcusd@depth@100ms
disconnected
Send
Quantity zero indicates price level removal.

Code

{
  "e": "depthUpdate",
  "E": 1751508260659505382,
  "s": "btcusd",
  "U": 12345677,
  "u": 12345678,
  "b": [
    ["45000.50", "1.25000000"],
    ["45000.25", "0.00000000"]
  ],
  "a": [
    ["45001.00", "0.75000000"]
  ]
}
Field	Type	Description
e	string	Event type ("depthUpdate")
E	number	Event time (nanoseconds)
s	string	Symbol
U	number	First update ID in this event
u	number	Last update ID in this event
b	array	Bid updates [price, quantity]
a	array	Ask updates [price, quantity]
Trade Stream
Schema	Frequency	Description
{symbol}@trade	Real-time	Real time trade executions
Try It
btcusd@trade
disconnected
Send
Code

{
  "E": 1759873803503023900,
  "s": "btcusd",
  "t": 2840140956529623,
  "p": "120649.97000",
  "q": "0.0046190900",
  "m": true
}
Field	Type	Description
E	number	Event time (nanoseconds)
s	string	Symbol
t	number	Trade ID
p	string	Price
q	string	Quantity
m	boolean	Is buyer the maker
Order Events
Requires an authenticated session

Schema	Frequency	Description
orders@account	Real-time	Real time order activity for the account associated with the authenticated API key
orders@session	Real-time	Real time order activity for the authenticated API key
Code

# Order Event - New
{
  "E":1759291847686856569,
  "s":"BTCUSD",
  "i":73797746498585286,
  "c":"my-order-1759291847503",
  "S":"BUY",
  "o":"LIMIT",
  "X":"NEW",
  "p":"1.00000",
  "q":"0.0000100000",
  "z":"0.0000100000",
  "T":1759291847686856569
}
# Order Event - Canceled
{
  "E":1759291847731455006,
  "s":"BTCUSD",
  "i":73797746498585286,
  "c":"my-order-1759291847503",
  "X":"CANCELED",
  "T":1759291847731455006
}
Field	Type	Description
E	number	Event time (nanoseconds)
s	string	Symbol
i	number	Order ID
c	string	Client Order ID
S	string	Side, BUY / SELL
o	string	Type, LIMIT / MARKET
X	string	Status, NEW / OPEN / FILLED / PARTIALLY_FILLED / CANCELED / REJECTED / MODIFIED
p	string	Order price
P	string	Stop price
q	string	Original quantity
z	string	Remaining quantity
Z	string	Executed quantity. For FILLED / PARTIALLY_FILLED events, this is the quantity filled in the last execution. For CANCELED and other events, this is the cumulative quantity filled over the lifetime of the order.
L	string	Last execution price
t	number	Trade ID
r	string	Rejection reason
T	number	Update time (nanoseconds)
O	string	Event outcome for event contracts, YES / NO
Fields with empty or zero values may be omitted from the event.

Rejection Reasons
When an order is REJECTED, the r field contains one of:

Reason	Description
MarketNotOpen	Market is closed or paused
InsufficientFunds	Account lacks sufficient balance
InvalidPrice	Price violates constraints
LimitPriceOffTick	Price does not align with tick size
InvalidQuantity	Quantity below minimum or off increment
InvalidStopPrice	Stop price violates constraints
InvalidTotalSpend	Total spend calculation error
DuplicateOrder	Duplicate client order ID
InsufficientLiquidity	Not enough liquidity at price
UnknownInstrument	Trading pair does not exist
Cancellation Reasons
When an order is CANCELED by the system, the r field contains one of:

Reason	Description
SelfCrossPrevented	Self-trade prevention triggered
FillOrKillWouldNotFill	FOK order could not fill completely
ImmediateOrCancelWouldPost	IOC order would post to book
MakerOrCancelWouldTake	MOC order would take liquidity
AuctionCancelled	Auction-related cancellation
ExceedsPriceLimits	Price moved beyond limits
Balance Updates
Requires an authenticated session

Schema	Frequency	Description
balances@account	Real-time	Real time balance updates for the account associated with the authenticated API key
balances@account@1s	Periodic (1s)	Periodic snapshot of all balances every second for the account associated with the authenticated API key
The balances@account stream pushes updates in real time whenever a balance change occurs, and only includes the assets that changed. The balances@account@1s stream sends a complete snapshot of all account balances every second, regardless of whether they changed. On subscribe, balances@account@1s will immediately send the current balances if available.

Code

# Balance Update
{
  "e": "balanceUpdate",
  "E": 1768250434780,
  "u": 1768250421600,
  "B": [
    {
      "a": "USD",
      "f": "207.39"
    }
  ]
}
Field	Type	Description
e	string	Event type ("balanceUpdate")
E	number	Event time (nanoseconds)
u	number	Time of the last account update (nanoseconds)
B	array	Balance updates
a	string	Asset code
f	string	Asset balance


















Utility
(3 methods)
ping
disconnected
Ping the server to check connectivity.

Request

Send
{
  "id": "1",
  "method": "ping",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
conninfo
disconnected
Get the connection rate limits.

Request

Send
{
  "id": "1",
  "method": "conninfo",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "rateLimits": [
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 30000,
      "count": 1
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "intervalNum": 10,
      "limit": 1000,
      "count": 0
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "DAY",
      "intervalNum": 1,
      "limit": 1000000,
      "count": 0
    },
    {
      "rateLimitType": "CONNECTION_ATTEMPTS",
      "interval": "MINUTE",
      "intervalNum": 5,
      "limit": 300,
      "count": 1
    }
  ]
}
time
disconnected
Get the current server time in milliseconds since Unix epoch.

Request

Send
{
  "id": "1",
  "method": "time",
  "params": {}
}
Format JSON
Response

Response will appear here...
Subscriptions
(3 methods)
subscribe
disconnected
Subscribe to data streams. Multiple streams can be subscribed in a single request.

Parameters
Name	Type	Required	Description
params	array	required	Array of stream names to subscribe to
Request

Send
{
  "id": "1",
  "method": "subscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
Stream Data
10 messages
Clear
[10:35:21.211-9]

{
  "u": 1764528738061152,
  "E": 1772616921156491300,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.1835869400",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.210-8]

{
  "u": 1764528738061148,
  "E": 1772616921156258800,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.0367173900",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.168-7]

{
  "u": 1764528738060863,
  "E": 1772616921110983400,
  "s": "btcusd",
  "b": "71512.21000",
  "B": "0.0031000000",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.151-6]

{
  "u": 1764528738060736,
  "E": 1772616921100320800,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.0031000000",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.148-5]

{
  "u": 1764528738060732,
  "E": 1772616921100171500,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.1499695500",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.020-4]

{
  "u": 1764528738060197,
  "E": 1772616920963455700,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.1866869400",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:21.019-3]

{
  "u": 1764528738060192,
  "E": 1772616920963252700,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.0398173900",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:20.873-2]

{
  "u": 1764528738059867,
  "E": 1772616920822230800,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.0031000000",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:20.872-1]

{
  "u": 1764528738059864,
  "E": 1772616920822077000,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.1499695500",
  "a": "71519.38000",
  "A": "0.0007925000"
}
[10:35:20.858-0]

{
  "u": 1764528738058943,
  "E": 1772616920486344000,
  "s": "btcusd",
  "b": "71519.37000",
  "B": "0.1866869400",
  "a": "71519.38000",
  "A": "0.0007925000"
}
Showing latest 10 messages. Older messages are automatically removed.
unsubscribe
disconnected
Unsubscribe from a data streams. Multiple streams can be unsubscribed in a single request.

Parameters
Name	Type	Required	Description
streams	array	required	Array of stream names to unsubscribe from
Request

Send
{
  "id": "1",
  "method": "unsubscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
list_subscriptions
disconnected
Get a list of all active stream subscriptions for the current connection.

Request

Send
{
  "id": "1",
  "method": "list_subscriptions",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": null
}
L2 Data
(1 method)
depth
disconnected
Get a snapshot of the order book depth for a specific symbol, showing the current bids and asks up to the specified limit. Response includes rate limit status showing current usage and limits for weight-based rate limiting.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol (e.g., btcusd, ethusd)
limit	number	optional	Number of price levels to return (max: 5000)(default: 100)
Request

Send
{
  "id": "1",
  "method": "depth",
  "params": {
    "symbol": "btcusd",
    "limit": 5
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": {
    "lastUpdateId": 1764528738074447,
    "bids": [
      [
        "71516.44000",
        "0.0031000000"
      ],
      [
        "71514.30000",
        "0.3000000000"
      ],
      [
        "71512.29000",
        "0.0367020900"
      ],
      [
        "71508.92000",
        "0.1468083400"
      ],
      [
        "71507.00000",
        "1.3500000000"
      ]
    ],
    "asks": [
      [
        "71519.38000",
        "0.0007925000"
      ],
      [
        "71519.79000",
        "0.0000349600"
      ],
      [
        "71526.06000",
        "0.0500000000"
      ],
      [
        "71533.70000",
        "0.0031000000"
      ],
      [
        "71538.29000",
        "0.1887990000"
      ]
    ]
  }
}
Trading
(4 methods)
order.place
Auth Required
disconnected
Place a new order. Requires authentication via API key. Response includes rate limit status showing current order placement usage and limits per session.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol
side	string	required	Order side: BUY or SELL
type	string	required	Order type: LIMIT or MARKET
timeInForce	string	required	Time in force: GTC (Good Till Cancel), IOC (Immediate or Cancel), FOK (Fill or Kill), MOC (Maker or Cancel)
price	string	optional	Order price (required for LIMIT orders)
stopPrice	string	optional	Stop price for stop orders (optional)
quantity	string	required	Order quantity
clientOrderId	string	optional	Client-provided order ID for tracking
eventOutcome	string	optional	Event outcome for event contracts: YES or NO
Request

Send
{
  "id": "1",
  "method": "order.place",
  "params": {
    "symbol": "btcusd",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "45000.00",
    "quantity": "0.10"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel
Auth Required
disconnected
Cancel an existing order.

Parameters
Name	Type	Required	Description
orderId	string	required	Order ID to cancel
Request

Send
{
  "id": "1",
  "method": "order.cancel",
  "params": {
    "orderId": "12345678"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_all
Auth Required
disconnected
Cancel all existing orders.

Request

Send
{
  "id": "1",
  "method": "order.cancel_all",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_session
Auth Required
disconnected
Cancel all existing orders for session.

Request

Send
{
  "id": "1",
  "method": "order.cancel_session",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
(2 methods)
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}
connected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}















subscribe
disconnected
Subscribe to data streams. Multiple streams can be subscribed in a single request.

Parameters
Name	Type	Required	Description
params	array	required	Array of stream names to subscribe to
Request

Send
{
  "id": "1",
  "method": "subscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

Response will appear here...
unsubscribe
disconnected
Unsubscribe from a data streams. Multiple streams can be unsubscribed in a single request.

Parameters
Name	Type	Required	Description
streams	array	required	Array of stream names to unsubscribe from
Request

Send
{
  "id": "1",
  "method": "unsubscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

Response will appear here...
list_subscriptions
disconnected
Get a list of all active stream subscriptions for the current connection.

Request

Send
{
  "id": "1",
  "method": "list_subscriptions",
  "params": {}
}
Format JSON
Response

Response will appear here...
L2 Data
(1 method)
depth
disconnected
Get a snapshot of the order book depth for a specific symbol, showing the current bids and asks up to the specified limit. Response includes rate limit status showing current usage and limits for weight-based rate limiting.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol (e.g., btcusd, ethusd)
limit	number	optional	Number of price levels to return (max: 5000)(default: 100)
Request

Send
{
  "id": "1",
  "method": "depth",
  "params": {
    "symbol": "btcusd",
    "limit": 5
  }
}
Format JSON
Response

Response will appear here...
Trading
(4 methods)
order.place
Auth Required
disconnected
Place a new order. Requires authentication via API key. Response includes rate limit status showing current order placement usage and limits per session.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol
side	string	required	Order side: BUY or SELL
type	string	required	Order type: LIMIT or MARKET
timeInForce	string	required	Time in force: GTC (Good Till Cancel), IOC (Immediate or Cancel), FOK (Fill or Kill), MOC (Maker or Cancel)
price	string	optional	Order price (required for LIMIT orders)
stopPrice	string	optional	Stop price for stop orders (optional)
quantity	string	required	Order quantity
clientOrderId	string	optional	Client-provided order ID for tracking
eventOutcome	string	optional	Event outcome for event contracts: YES or NO
Request

Send
{
  "id": "1",
  "method": "order.place",
  "params": {
    "symbol": "btcusd",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "45000.00",
    "quantity": "0.10"
  }
}
Format JSON
Response

Response will appear here...
order.cancel
Auth Required
disconnected
Cancel an existing order.

Parameters
Name	Type	Required	Description
orderId	string	required	Order ID to cancel
Request

Send
{
  "id": "1",
  "method": "order.cancel",
  "params": {
    "orderId": "12345678"
  }
}
Format JSON
Response

Response will appear here...
order.cancel_all
Auth Required
disconnected
Cancel all existing orders.

Request

Send
{
  "id": "1",
  "method": "order.cancel_all",
  "params": {}
}
Format JSON
Response

Response will appear here...
order.cancel_session
Auth Required
disconnected
Cancel all existing orders for session.

Request

Send
{
  "id": "1",
  "method": "order.cancel_session",
  "params": {}
}
Format JSON
Response

Response will appear here...
(2 methods)
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

Response will appear here...
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

Response will appear here...


Utility
(3 methods)
ping
disconnected
Ping the server to check connectivity.

Request

Send
{
  "id": "1",
  "method": "ping",
  "params": {}
}
Format JSON
Response

Response will appear here...
conninfo
disconnected
Get the connection rate limits.

Request

Send
{
  "id": "1",
  "method": "conninfo",
  "params": {}
}
Format JSON
Response

Response will appear here...
time
disconnected
Get the current server time in milliseconds since Unix epoch.

Request

Send
{
  "id": "1",
  "method": "time",
  "params": {}
}
Format JSON
Response

Response will appear here...
Subscriptions
(3 methods)
subscribe
disconnected
Subscribe to data streams. Multiple streams can be subscribed in a single request.

Parameters
Name	Type	Required	Description
params	array	required	Array of stream names to subscribe to
Request

Send
{
  "id": "1",
  "method": "subscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

Response will appear here...
unsubscribe
disconnected
Unsubscribe from a data streams. Multiple streams can be unsubscribed in a single request.

Parameters
Name	Type	Required	Description
streams	array	required	Array of stream names to unsubscribe from
Request

Send
{
  "id": "1",
  "method": "unsubscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
list_subscriptions
disconnected
Get a list of all active stream subscriptions for the current connection.

Request

Send
{
  "id": "1",
  "method": "list_subscriptions",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": null
}
L2 Data
(1 method)
depth
disconnected
Get a snapshot of the order book depth for a specific symbol, showing the current bids and asks up to the specified limit. Response includes rate limit status showing current usage and limits for weight-based rate limiting.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol (e.g., btcusd, ethusd)
limit	number	optional	Number of price levels to return (max: 5000)(default: 100)
Request

Send
{
  "id": "1",
  "method": "depth",
  "params": {
    "symbol": "btcusd",
    "limit": 5
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": {
    "lastUpdateId": 1764528738340123,
    "bids": [
      [
        "71578.90000",
        "0.3000000000"
      ],
      [
        "71571.84000",
        "0.0031000000"
      ],
      [
        "71571.00000",
        "1.3500000000"
      ],
      [
        "71569.84000",
        "0.1043464900"
      ],
      [
        "71564.68000",
        "0.0031000000"
      ]
    ],
    "asks": [
      [
        "71596.00000",
        "2.5000000000"
      ],
      [
        "71601.94000",
        "0.1885150000"
      ],
      [
        "71617.82000",
        "0.1721730000"
      ],
      [
        "71644.99000",
        "0.0031000000"
      ],
      [
        "71648.78000",
        "0.0905222800"
      ]
    ]
  }
}
Trading
(4 methods)
order.place
Auth Required
disconnected
Place a new order. Requires authentication via API key. Response includes rate limit status showing current order placement usage and limits per session.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol
side	string	required	Order side: BUY or SELL
type	string	required	Order type: LIMIT or MARKET
timeInForce	string	required	Time in force: GTC (Good Till Cancel), IOC (Immediate or Cancel), FOK (Fill or Kill), MOC (Maker or Cancel)
price	string	optional	Order price (required for LIMIT orders)
stopPrice	string	optional	Stop price for stop orders (optional)
quantity	string	required	Order quantity
clientOrderId	string	optional	Client-provided order ID for tracking
eventOutcome	string	optional	Event outcome for event contracts: YES or NO
Request

Send
{
  "id": "1",
  "method": "order.place",
  "params": {
    "symbol": "btcusd",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "45000.00",
    "quantity": "0.10"
  }
}
Format JSON
Response

Response will appear here...
order.cancel
Auth Required
disconnected
Cancel an existing order.

Parameters
Name	Type	Required	Description
orderId	string	required	Order ID to cancel
Request

Send
{
  "id": "1",
  "method": "order.cancel",
  "params": {
    "orderId": "12345678"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_all
Auth Required
disconnected
Cancel all existing orders.

Request

Send
{
  "id": "1",
  "method": "order.cancel_all",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_session
Auth Required
disconnected
Cancel all existing orders for session.

Request

Send
{
  "id": "1",
  "method": "order.cancel_session",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
(2 methods)
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}



Utility
(3 methods)
ping
disconnected
Ping the server to check connectivity.

Request

Send
{
  "id": "1",
  "method": "ping",
  "params": {}
}
Format JSON
Response

Response will appear here...
conninfo
disconnected
Get the connection rate limits.

Request

Send
{
  "id": "1",
  "method": "conninfo",
  "params": {}
}
Format JSON
Response

Response will appear here...
time
disconnected
Get the current server time in milliseconds since Unix epoch.

Request

Send
{
  "id": "1",
  "method": "time",
  "params": {}
}
Format JSON
Response

Response will appear here...
Subscriptions
(3 methods)
subscribe
disconnected
Subscribe to data streams. Multiple streams can be subscribed in a single request.

Parameters
Name	Type	Required	Description
params	array	required	Array of stream names to subscribe to
Request

Send
{
  "id": "1",
  "method": "subscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

Response will appear here...
unsubscribe
disconnected
Unsubscribe from a data streams. Multiple streams can be unsubscribed in a single request.

Parameters
Name	Type	Required	Description
streams	array	required	Array of stream names to unsubscribe from
Request

Send
{
  "id": "1",
  "method": "unsubscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
list_subscriptions
disconnected
Get a list of all active stream subscriptions for the current connection.

Request

Send
{
  "id": "1",
  "method": "list_subscriptions",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": null
}
L2 Data
(1 method)
depth
disconnected
Get a snapshot of the order book depth for a specific symbol, showing the current bids and asks up to the specified limit. Response includes rate limit status showing current usage and limits for weight-based rate limiting.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol (e.g., btcusd, ethusd)
limit	number	optional	Number of price levels to return (max: 5000)(default: 100)
Request

Send
{
  "id": "1",
  "method": "depth",
  "params": {
    "symbol": "btcusd",
    "limit": 5
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": {
    "lastUpdateId": 1764528738340123,
    "bids": [
      [
        "71578.90000",
        "0.3000000000"
      ],
      [
        "71571.84000",
        "0.0031000000"
      ],
      [
        "71571.00000",
        "1.3500000000"
      ],
      [
        "71569.84000",
        "0.1043464900"
      ],
      [
        "71564.68000",
        "0.0031000000"
      ]
    ],
    "asks": [
      [
        "71596.00000",
        "2.5000000000"
      ],
      [
        "71601.94000",
        "0.1885150000"
      ],
      [
        "71617.82000",
        "0.1721730000"
      ],
      [
        "71644.99000",
        "0.0031000000"
      ],
      [
        "71648.78000",
        "0.0905222800"
      ]
    ]
  }
}
Trading
(4 methods)
order.place
Auth Required
connected
Place a new order. Requires authentication via API key. Response includes rate limit status showing current order placement usage and limits per session.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol
side	string	required	Order side: BUY or SELL
type	string	required	Order type: LIMIT or MARKET
timeInForce	string	required	Time in force: GTC (Good Till Cancel), IOC (Immediate or Cancel), FOK (Fill or Kill), MOC (Maker or Cancel)
price	string	optional	Order price (required for LIMIT orders)
stopPrice	string	optional	Stop price for stop orders (optional)
quantity	string	required	Order quantity
clientOrderId	string	optional	Client-provided order ID for tracking
eventOutcome	string	optional	Event outcome for event contracts: YES or NO
Request

Send
{
  "id": "1",
  "method": "order.place",
  "params": {
    "symbol": "btcusd",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "45000.00",
    "quantity": "0.10"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel
Auth Required
disconnected
Cancel an existing order.

Parameters
Name	Type	Required	Description
orderId	string	required	Order ID to cancel
Request

Send
{
  "id": "1",
  "method": "order.cancel",
  "params": {
    "orderId": "12345678"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_all
Auth Required
disconnected
Cancel all existing orders.

Request

Send
{
  "id": "1",
  "method": "order.cancel_all",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_session
Auth Required
disconnected
Cancel all existing orders for session.

Request

Send
{
  "id": "1",
  "method": "order.cancel_session",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
(2 methods)
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}








Utility
(3 methods)
ping
disconnected
Ping the server to check connectivity.

Request

Send
{
  "id": "1",
  "method": "ping",
  "params": {}
}
Format JSON
Response

Response will appear here...
conninfo
disconnected
Get the connection rate limits.

Request

Send
{
  "id": "1",
  "method": "conninfo",
  "params": {}
}
Format JSON
Response

Response will appear here...
time
disconnected
Get the current server time in milliseconds since Unix epoch.

Request

Send
{
  "id": "1",
  "method": "time",
  "params": {}
}
Format JSON
Response

Response will appear here...
Subscriptions
(3 methods)
subscribe
disconnected
Subscribe to data streams. Multiple streams can be subscribed in a single request.

Parameters
Name	Type	Required	Description
params	array	required	Array of stream names to subscribe to
Request

Send
{
  "id": "1",
  "method": "subscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

Response will appear here...
unsubscribe
disconnected
Unsubscribe from a data streams. Multiple streams can be unsubscribed in a single request.

Parameters
Name	Type	Required	Description
streams	array	required	Array of stream names to unsubscribe from
Request

Send
{
  "id": "1",
  "method": "unsubscribe",
  "params": [
    "btcusd@bookTicker"
  ]
}
Format JSON
Response

{
  "id": "1",
  "status": 200
}
list_subscriptions
disconnected
Get a list of all active stream subscriptions for the current connection.

Request

Send
{
  "id": "1",
  "method": "list_subscriptions",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": null
}
L2 Data
(1 method)
depth
disconnected
Get a snapshot of the order book depth for a specific symbol, showing the current bids and asks up to the specified limit. Response includes rate limit status showing current usage and limits for weight-based rate limiting.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol (e.g., btcusd, ethusd)
limit	number	optional	Number of price levels to return (max: 5000)(default: 100)
Request

Send
{
  "id": "1",
  "method": "depth",
  "params": {
    "symbol": "btcusd",
    "limit": 5
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 200,
  "result": {
    "lastUpdateId": 1764528738340123,
    "bids": [
      [
        "71578.90000",
        "0.3000000000"
      ],
      [
        "71571.84000",
        "0.0031000000"
      ],
      [
        "71571.00000",
        "1.3500000000"
      ],
      [
        "71569.84000",
        "0.1043464900"
      ],
      [
        "71564.68000",
        "0.0031000000"
      ]
    ],
    "asks": [
      [
        "71596.00000",
        "2.5000000000"
      ],
      [
        "71601.94000",
        "0.1885150000"
      ],
      [
        "71617.82000",
        "0.1721730000"
      ],
      [
        "71644.99000",
        "0.0031000000"
      ],
      [
        "71648.78000",
        "0.0905222800"
      ]
    ]
  }
}
Trading
(4 methods)
order.place
Auth Required
disconnected
Place a new order. Requires authentication via API key. Response includes rate limit status showing current order placement usage and limits per session.

Parameters
Name	Type	Required	Description
symbol	string	required	Trading pair symbol
side	string	required	Order side: BUY or SELL
type	string	required	Order type: LIMIT or MARKET
timeInForce	string	required	Time in force: GTC (Good Till Cancel), IOC (Immediate or Cancel), FOK (Fill or Kill), MOC (Maker or Cancel)
price	string	optional	Order price (required for LIMIT orders)
stopPrice	string	optional	Stop price for stop orders (optional)
quantity	string	required	Order quantity
clientOrderId	string	optional	Client-provided order ID for tracking
eventOutcome	string	optional	Event outcome for event contracts: YES or NO
Request

Send
{
  "id": "1",
  "method": "order.place",
  "params": {
    "symbol": "btcusd",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "45000.00",
    "quantity": "0.10"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel
Auth Required
disconnected
Cancel an existing order.

Parameters
Name	Type	Required	Description
orderId	string	required	Order ID to cancel
Request

Send
{
  "id": "1",
  "method": "order.cancel",
  "params": {
    "orderId": "12345678"
  }
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_all
Auth Required
disconnected
Cancel all existing orders.

Request

Send
{
  "id": "1",
  "method": "order.cancel_all",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
order.cancel_session
Auth Required
disconnected
Cancel all existing orders for session.

Request

Send
{
  "id": "1",
  "method": "order.cancel_session",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 401,
  "error": {
    "code": -1002,
    "msg": "Authentication required"
  }
}
(2 methods)
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}
disconnected
Request

Send
{
  "id": "1",
  "method": "",
  "params": {}
}
Format JSON
Response

{
  "id": "1",
  "status": 400,
  "error": {
    "code": -1020,
    "msg": "Unsupported operation"
  }
}


















