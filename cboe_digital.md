# Cboe Digital (formerly ErisX) FIX API Documentation

## General
**Protocol**: FIX 4.4
**Formerly**: ErisX

## FIX Specifications
Cboe Digital provides two FIX specifications:

### 1. Market Data & Order Entry (FIX 4.4 Spec V3.15.5)
- Market data feeds and order submission
- Supports: Limit, Stop-Limit, Market, Post-Only orders
- `TransactTime (60)` with nanosecond precision
- Application messages for market data, order submission, and execution reports

### 2. STP (Straight Through Processing) (FIX 4.4 STP Spec V3.8)
- Guaranteed trade capture reports
- Middle/back office reconciliation

## Access
- Requires membership / client onboarding
- Contact: Client Services at cboedigital.com
- Credentials: User ID (tag 49) + Password (tag 554) in Logon message
- FIX sessions: 24/7 with daily logical session rollover

## Notes
- Documentation was publicly accessible at cboedigital.com/resources but the page now returns 404
- Specs may need to be requested directly from Cboe Digital sales
