![image info](./DeepBook_Logo_White.png)

# DeepBook V3

DeepBook V3 is a next generation decentralized central limit order book (CLOB) built on Sui. It leverages Sui's parallel execution and low transaction fees to bring a highly performant, low latency exchange on chain. DBv3 comes with brand new features including flashloans, governance, improved account abstraction, and enhancements to the existing matching engine. With the addition of the DEEP token, staked takers can trade with fees as low as 0.25 bps / 2.5 bps on stable and volatile pairs, while allowing staked makers to earn rebates. Checkout the full whitepaper on [deepbook.tech](https://deepbook.tech).

## DeepBook V3 Information

- [Package and Pools](https://docs.google.com/document/d/1uK4MNqYa0LdhVqBD4KqOcWG1N1nNNe3JwbeUZc1kH1I)
- [Contract Documentation](https://docs.sui.io/standards/deepbookv3)
- [SDK Documentation](https://docs.sui.io/standards/deepbookv3-sdk)
- [Example SDK Usage](https://github.com/MystenLabs/ts-sdks/tree/main/packages/deepbook-v3/examples)
- [Whitepaper](https://cdn.prod.website-files.com/65fdccb65290aeb1c597b611/66059b44041261e3fe4a330d_deepbook_whitepaper.pdf)
- [Rust SDK(Unofficial)](https://github.com/hoh-zone/sui-deepbookv3)

## DeepBook Architecture

![image info](./DBv3Architecture.png)

## Balance Manager

The `BalanceManager` is a shared object that holds all balances of a single account. It has one owner and can have up to 1000 traders. When creating a `BalanceManager`, the sender of the transaction becomes the owner. The owner can add or remove traders. The owner cannot be changed.
The owner can deposit and withdraw funds from the `BalanceManager` as well as place orders, stake, and more. A trader cannot deposit and withdraw funds, but can do everything else. All actions are shared between owner/traders. For example, one trader can cancel an order placed by another trader within the same `BalanceManager`.
With exception to swaps, all interactions with DeepBook will require a `BalanceManager` as one of its inputs. When orders are matched, funds will be transferred to / from the `BalanceManager`. A single `BalanceManager` can be used between all pools.

## Pool

`Pool` is made up of three distinct parts: Book, State and Vault. These parts define the flow for the different types of actions that can be performed on DeepBook.

1.  Book - manages reading and writing to the order book. It fills orders and places orders into the order book.
2.  State - the most complex: maintains individual user data, overall volumes, historic volumes, and governance.
3.  Vault - the least complex: settles users funds after action execution.

Users can place, modify and cancel limit / market orders. These actions will require a funded `BalanceManager` with the appropriate amount of base and quote tokens as well as DEEP tokens for trading fees. DBv3 also supports direct swaps, allowing users as well as protocols building on top of DBv3 to place market orders with `Coin` objects as inputs drectly and receive `Coin` objects as outputs.

## $DEEP

### Trading Fees

In the initial release, all pool creation will be permissioned and DEEP tokens will be required to pay for trading fees. In the future upgrades, these restrictions will be removed, but usage of the DEEP token will still be incentivized. Both takers and makers will pay fees in DEEP, but makers with enough staked DEEP tokens will be eligible for rebates at the end of every epoch. Excess DEEP accumulated by all pools will be burned on a regular basis.
DEEP/SUI and DEEP/USDC pools will be launched and whitelisted. Whitelisted pools have 0% trading fees. This allows users to easily obtain DEEP tokens to pay for trading fees in non DEEP pools.

### DEEP Staking & Governance

DEEP tokens can be staked in individual pools, granting the staker access to governance. If the amount of DEEP tokens staked is greater than the pool's stake required, then that user will be able to reap additional benefits from the pool. These benefits include halved trading fees after reaching a trade volume requirement, as well as maker rebates. During every epoch, staked users can submit proposals to change three parameters: taker fees, maker fees, and stake required. If the proposal passes quorum, 1/2 of all current stake, then its effects will be live from the next epoch and onwards.
# DeepBook Margin

DeepBook Margin is a decentralized margin trading protocol built on top of DeepBookV3 on Sui. It
enables leveraged trading by allowing users to borrow assets against their collateral, execute
margin orders on DeepBook's central limit order book, and manage risk with advanced features like
take profit and stop loss conditional orders. The protocol includes a lending pool where
suppliers can earn interest by providing liquidity for margin traders to borrow.

## DeepBook Margin Information

- [Package and Pools](https://docs.google.com/document/d/1uK4MNqYa0LdhVqBD4KqOcWG1N1nNNe3JwbeUZc1kH1I)
- [Contract Documentation](https://docs.sui.io/standards/deepbook-margin)
- [SDK Documentation](https://docs.sui.io/standards/deepbook-margin-sdk)
- [Example SDK Usage](https://github.com/MystenLabs/ts-sdks/tree/main/packages/deepbook-v3/examples)

## Margin Manager

The `MarginManager` is a shared object that represents a single margin trading account. It holds
collateral balances, tracks borrowed positions, and interfaces with both DeepBookV3 for trading
and the MarginPool for borrowing. Each MarginManager is linked to a specific DeepBook pool and
its corresponding MarginPool.

Users can deposit collateral (base, quote, or DEEP tokens), borrow assets to increase their
trading position, and repay loans. The MarginManager tracks the user's risk ratio, which
determines liquidation eligibility. If a position becomes undercollateralized, it can be
liquidated by any party.

## Margin Pool

The `MarginPool` is a lending pool that provides liquidity for margin traders. It consists of:

1. **Supply Side** - Users can supply assets to earn interest from borrowers. Suppliers receive
   shares representing their portion of the pool.
2. **Borrow Side** - Margin traders borrow from the pool to leverage their positions. Interest
   accrues based on utilization rate.
3. **Interest Model** - Dynamic interest rates adjust based on pool utilization to balance supply
   and demand.

Suppliers mint a `SupplierCap` to track their deposits and can withdraw their supplied assets
plus accrued interest at any time, subject to available liquidity.

## Take Profit / Stop Loss (TPSL)

DeepBook Margin supports conditional orders that automatically execute when price conditions are
met:

- **Take Profit** - Automatically close a position when the price reaches a favorable target
- **Stop Loss** - Automatically close a position to limit losses when price moves against you

Conditional orders are stored on-chain and can be executed by anyone (permissionlessly) once the
trigger price is reached. This enables automated risk management without requiring users to
monitor positions constantly.

## Liquidation

When a MarginManager's risk ratio exceeds the maximum threshold (position becomes
undercollateralized), it becomes eligible for liquidation. Any user can call the liquidate
function to:

1. Repay the outstanding debt
2. Receive the collateral plus a liquidation bonus

This mechanism ensures the protocol remains solvent and incentivizes liquidators to maintain
system health.
![image info](../../DeepBook_Logo_White.png)

# DeepBook V3

DeepBook V3 is a next generation decentralized central limit order book (CLOB) built on Sui. It leverages Sui's parallel execution and low transaction fees to bring a highly performant, low latency exchange on chain. DBv3 comes with brand new features including flashloans, governance, improved account abstraction, and enhancements to the existing matching engine. With the addition of the DEEP token, staked takers can trade with fees as low as 0.25 bps / 2.5 bps on stable and volatile pairs, while allowing staked makers to earn rebates. Checkout the full whitepaper on [deepbook.tech](https://deepbook.tech).

## DeepBook V3 Information

- [Package and Pools](https://docs.google.com/document/d/1uK4MNqYa0LdhVqBD4KqOcWG1N1nNNe3JwbeUZc1kH1I)
- [Contract Documentation](https://docs.sui.io/standards/deepbookv3)
- [SDK Documentation](https://docs.sui.io/standards/deepbookv3-sdk)
- [Example SDK Usage](https://github.com/MystenLabs/ts-sdks/tree/main/packages/deepbook-v3/examples)
- [Whitepaper](https://cdn.prod.website-files.com/65fdccb65290aeb1c597b611/66059b44041261e3fe4a330d_deepbook_whitepaper.pdf)

## DeepBook Architecture

![image info](../../DBv3Architecture.png)

## Balance Manager

The `BalanceManager` is a shared object that holds all balances of a single account. It has one owner and can have up to 1000 traders. When creating a `BalanceManager`, the sender of the transaction becomes the owner. The owner can add or remove traders. The owner cannot be changed.
The owner can deposit and withdraw funds from the `BalanceManager` as well as place orders, stake, and more. A trader cannot deposit and withdraw funds, but can do everything else. All actions are shared between owner/traders. For example, one trader can cancel an order placed by another trader within the same `BalanceManager`.
With exception to swaps, all interactions with DeepBook will require a `BalanceManager` as one of its inputs. When orders are matched, funds will be transferred to / from the `BalanceManager`. A single `BalanceManager` can be used between all pools.

## Pool

`Pool` is made up of three distinct parts: Book, State and Vault. These parts define the flow for the different types of actions that can be performed on DeepBook.

1.  Book - manages reading and writing to the order book. It fills orders and places orders into the order book.
2.  State - the most complex: maintains individual user data, overall volumes, historic volumes, and governance.
3.  Vault - the least complex: settles users funds after action execution.

Users can place, modify and cancel limit / market orders. These actions will require a funded `BalanceManager` with the appropriate amount of base and quote tokens as well as DEEP tokens for trading fees. DBv3 also supports direct swaps, allowing users as well as protocols building on top of DBv3 to place market orders with `Coin` objects as inputs drectly and receive `Coin` objects as outputs.

## $DEEP

### Trading Fees

In the initial release, all pool creation will be permissioned and DEEP tokens will be required to pay for trading fees. In the future upgrades, these restrictions will be removed, but usage of the DEEP token will still be incentivized. Both takers and makers will pay fees in DEEP, but makers with enough staked DEEP tokens will be eligible for rebates at the end of every epoch. Excess DEEP accumulated by all pools will be burned on a regular basis.
DEEP/SUI and DEEP/USDC pools will be launched and whitelisted. Whitelisted pools have 0% trading fees. This allows users to easily obtain DEEP tokens to pay for trading fees in non DEEP pools.

### DEEP Staking & Governance

DEEP tokens can be staked in individual pools, granting the staker access to governance. If the amount of DEEP tokens staked is greater than the pool's stake required, then that user will be able to reap additional benefits from the pool. These benefits include halved trading fees after reaching a trade volume requirement, as well as maker rebates. During every epoch, staked users can submit proposals to change three parameters: taker fees, maker fees, and stake required. If the proposal passes quorum, 1/2 of all current stake, then its effects will be live from the next epoch and onwards.
# DeepBook Server

The DeepBook Server is a Rust application that provides a RESTful API for the DeepBook project. It allows users to interact with the DeepBook database and retrieve information about DeepBook events.

## Health & Status Endpoints

### `/` - Health Check
Basic health check endpoint that returns HTTP 200 OK if the server is running.

```bash
curl http://localhost:9008/
```

### `/status` - Indexer Status
Returns detailed information about the indexer's health, including checkpoint lag and synchronization status.

```bash
curl http://localhost:9008/status
```

**Query Parameters:**
- `max_checkpoint_lag` (optional, default: 100) - Maximum acceptable checkpoint lag for "healthy" status
- `max_time_lag_seconds` (optional, default: 60) - Maximum acceptable time lag in seconds for "healthy" status

**Examples:**
```bash
# Use default thresholds (checkpoint_lag < 100, time_lag < 60 seconds)
curl http://localhost:9008/status

# Custom thresholds: allow up to 500 checkpoint lag and 300 seconds time lag
curl "http://localhost:9008/status?max_checkpoint_lag=500&max_time_lag_seconds=300"

# Strict thresholds: only healthy if checkpoint_lag < 10 and time_lag < 5 seconds
curl "http://localhost:9008/status?max_checkpoint_lag=10&max_time_lag_seconds=5"
```

**Example Response:**
```json
{
  "status": "OK",
  "latest_onchain_checkpoint": 12345678,
  "current_time_ms": 1732567890000,
  "earliest_checkpoint": 12345673,
  "max_lag_pipeline": "deepbook_indexer",
  "pipelines": [
    {
      "pipeline": "deepbook_indexer",
      "indexed_checkpoint": 12345673,
      "indexed_epoch": 500,
      "indexed_timestamp_ms": 1732567878000,
      "checkpoint_lag": 5,
      "time_lag_seconds": 12,
      "latest_onchain_checkpoint": 12345678
    }
  ],
  "max_checkpoint_lag": 5,
  "max_time_lag_seconds": 12
}
```

**Response Fields:**
- `status` - Overall health: `"OK"` or `"UNHEALTHY"` (based on client-provided thresholds)
- `latest_onchain_checkpoint` - Latest checkpoint on the blockchain
- `current_time_ms` - Current server timestamp
- `earliest_checkpoint` - The lowest checkpoint across all pipelines (useful for alerting)
- `max_lag_pipeline` - Name of the pipeline with the highest checkpoint lag (useful for alerting)
- `pipelines` - Array of per-pipeline details
- `max_checkpoint_lag` - Maximum checkpoint lag across all pipelines
- `max_time_lag_seconds` - Maximum time lag in seconds across all pipelines

**Status Values:**
- `OK` - Indexer is synced and up-to-date (based on thresholds)
- `UNHEALTHY` - Indexer is behind or experiencing delays

This endpoint is useful for monitoring the indexer's synchronization status and detecting stale data.