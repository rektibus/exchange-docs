# EDX Markets FIX API Documentation

## General
**Protocol**: FIX 5.0 SP2
**Target**: Institutional clients and approved member firms

## FIX Specifications
### Market Data (FIX 5.0 SP2)
- Real-time market data feeds

### Order Entry (FIX 5.0 SP2)
- Order submission and execution reports

## Key Details
- **Throttle Limit**: 100 messages per 5 seconds per FIX ID (username)
- Exceeding limit → `RATE_LIMIT_EXCEEDED` message + disconnect (immediate reconnect allowed)
- **Sequence Reset**: Daily at 12 PM ET (FIX convention: reset to 1)
- **Test Requests**: Handles missed heartbeats
- **Resend Requests**: Handles sequence number gaps

## Environments
- Production environment
- UAT (User Acceptance Testing) environment
- FIX dictionaries available for both

## Access
- Requires membership and onboarding as an approved member firm
- No direct retail access
- Documentation at edxmarkets.com (currently returns 404; may need direct contact)
