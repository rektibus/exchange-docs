# Duckdbex v0.3.21 — API Reference

> Pre-fetched from https://hexdocs.pm/duckdbex/Duckdbex.html and https://github.com/AlexR2D2/duckdbex

## CRITICAL: Return Value Conventions

**Not all functions wrap in `{:ok, ...}`!** Know the pattern:

| Function | Success Return | Error Return |
|----------|---------------|--------------|
| `open/0,1,2` | `{:ok, db}` | `{:error, reason}` |
| `connection/1` | `{:ok, conn}` | `{:error, reason}` |
| `query/2,3` | `{:ok, result_ref}` | `{:error, reason}` |
| **`fetch_all/1`** | **`list()`** (raw!) | `{:error, reason}` |
| **`fetch_chunk/1`** | **`list()`** (raw!) | `{:error, reason}` |
| **`columns/1`** | **`list()`** (raw!) | `{:error, reason}` |
| `appender/2,3` | `{:ok, appender}` | `{:error, reason}` |
| `appender_add_row/2` | `:ok` | `{:error, reason}` |
| `appender_add_rows/2` | `:ok` | `{:error, reason}` |
| `appender_flush/1` | `:ok` | `{:error, reason}` |
| `appender_close/1` | `:ok` | `{:error, reason}` |
| `prepare_statement/2` | `{:ok, stmt}` | `{:error, reason}` |
| `execute_statement/1,2` | `{:ok, result_ref}` | `{:error, reason}` |
| `begin_transaction/1` | `:ok` | `{:error, reason}` |
| `commit/1` | `:ok` | `{:error, reason}` |
| `rollback/1` | `:ok` | `{:error, reason}` |
| `release/1` | `:ok` | — |

## Types

All refs are `reference()`:

```elixir
@type db()           :: reference()
@type connection()   :: reference()
@type query_result() :: reference()
@type statement()    :: reference()
@type appender()     :: reference()
@type reason()       :: :atom | binary()
```

## Core Workflow

```elixir
# 1. Open database
{:ok, db} = Duckdbex.open("data/enso.duckdb")

# 2. Create connection (= native OS thread, NOT Elixir process)
#    Use different connections in different Elixir processes for parallelism
{:ok, conn} = Duckdbex.connection(db)

# 3. Run query → returns result reference (not data)
{:ok, result_ref} = Duckdbex.query(conn, "SELECT 1 as my_col;")

# 4. Fetch data — returns RAW list, NOT {:ok, list}
[[1]] = Duckdbex.fetch_all(result_ref)

# 5. Get column names — returns RAW list, NOT {:ok, list}
["my_col"] = Duckdbex.columns(result_ref)
```

## Query with Parameters

```elixir
{:ok, result_ref} = Duckdbex.query(conn, "SELECT 1 WHERE $1 = 1;", [1])
```

## Prepared Statements

```elixir
{:ok, stmt} = Duckdbex.prepare_statement(conn, "SELECT * FROM t WHERE id = $1;")
{:ok, res1} = Duckdbex.execute_statement(stmt, [1])
{:ok, res2} = Duckdbex.execute_statement(stmt, [42])
```

## Bulk Insert — Appender (RECOMMENDED for bulk data)

DuckDB docs say: do NOT use INSERT for more than a few records. Use Appender instead.

```elixir
{:ok, appender} = Duckdbex.appender(conn, "my_table")

# Add rows (cached in memory)
:ok = Duckdbex.appender_add_rows(appender, [[1, "Alice"], [2, "Bob"]])

# Or one at a time
:ok = Duckdbex.appender_add_row(appender, [3, "Charlie"])

# Flush to disk (also happens on close/GC)
:ok = Duckdbex.appender_flush(appender)

# Close when done
:ok = Duckdbex.appender_close(appender)
```

With schema:
```elixir
{:ok, appender} = Duckdbex.appender(conn, "my_schema", "my_table")
```

## Transactions

```elixir
:ok = Duckdbex.begin_transaction(conn)
# ... queries ...
:ok = Duckdbex.commit(conn)
# or
:ok = Duckdbex.rollback(conn)
```

## Resource Management

All refs (db, conn, result_ref) auto-close when garbage collected.
Explicit close: `Duckdbex.release(resource)`.

```elixir
:ok = Duckdbex.release(result_ref)
:ok = Duckdbex.release(conn)
:ok = Duckdbex.release(db)
```

## fetch_all Result Format

Rows are lists of values. Each row is a list. No maps, no keyword lists.

```elixir
# SELECT with columns
{:ok, res} = Duckdbex.query(conn, "SELECT id, name FROM people;")
Duckdbex.fetch_all(res)
# => [[1, "Mark"], [2, "Hannes"]]

# Empty result
Duckdbex.fetch_all(res)
# => []

# INSERT result (count affected rows)
{:ok, res} = Duckdbex.query(conn, "INSERT INTO people VALUES (3, 'Alex');")
Duckdbex.fetch_all(res)
# => [[1]]   ← 1 row inserted

# CREATE TABLE (no result)
{:ok, res} = Duckdbex.query(conn, "CREATE TABLE t (x INT);")
Duckdbex.fetch_all(res)
# => []
```

## fetch_chunk (Streaming)

For large results, fetch chunk by chunk:

```elixir
{:ok, res} = Duckdbex.query(conn, "SELECT * FROM big_table;")
chunk1 = Duckdbex.fetch_chunk(res)  # => [[...], [...], ...]
chunk2 = Duckdbex.fetch_chunk(res)  # => [[...], ...]
[]     = Duckdbex.fetch_chunk(res)  # => [] when exhausted
```

## DuckDB Data Type Mapping

| DuckDB Type | Elixir Type |
|-------------|------------|
| INTEGER, BIGINT | `integer()` |
| FLOAT, DOUBLE | `float()` |
| VARCHAR | `binary()` (string) |
| BOOLEAN | `true \| false` |
| DATE | `{year, month, day}` |
| TIMESTAMP | `{date, time}` |
| BLOB | `binary()` |
| HUGEINT | `{high :: integer(), low :: integer()}` |
| LIST | `list()` |
| STRUCT | `map()` |

## Connection Threading

Each DuckDB connection = native OS thread. Connections are thread-safe but lock during queries. For parallel performance, use separate connections in separate Elixir processes.

## CSV/Parquet Direct Load

DuckDB reads CSV/Parquet directly (bypasses ERTS):

```elixir
{:ok, res} = Duckdbex.query(conn, "SELECT * FROM 'data.csv';")
{:ok, _}   = Duckdbex.query(conn, "COPY (SELECT * FROM t) TO 'out.csv';")
```

## Extensions

```elixir
# Remote install
{:ok, _} = Duckdbex.query(conn, "INSTALL 'parquet';")
{:ok, _} = Duckdbex.query(conn, "LOAD 'parquet';")

# Check if loaded
true = Duckdbex.extension_is_loaded(db, "parquet")
```

## Configuration

```elixir
{:ok, db} = Duckdbex.open("my.duckdb", %Duckdbex.Config{
  checkpoint_wal_size: 8_388_608
})
```

## Utility

```elixir
Duckdbex.library_version()        # => "v1.1.3"
Duckdbex.source_id()              # => "..."
Duckdbex.number_of_threads(db)    # => 8
Duckdbex.platform()               # => "osx_arm64"
```
