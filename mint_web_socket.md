# Mint + Mint.WebSocket — Deep Reference

> **Source**: `github.com/elixir-mint/mint_web_socket` (v1.0.5, cloned to `/tmp/mint_web_socket`)
> **Studied**: All 7 source files (1,660 lines total), 3 examples, README, `ws_worker.ex` production code


## 1. Architecture — Functional, Process-less

Mint is a **functional** HTTP client. No GenServer, no process. You own two mutable-by-rebind data structures:

| Struct | Purpose | Updated by |
|--------|---------|-----------|
| `Mint.HTTP1` (the `conn`) | TCP/SSL connection, HTTP state machine | Every `stream`, `stream_request_body`, `set_mode` call |
| `Mint.WebSocket` (the `websocket`) | WS frame codec, extension state, fragment buffer | Every `encode`, `decode` call |

**Critical rule**: Every Mint call returns a NEW struct. Always rebind:
```elixir
{:ok, conn, responses} = Mint.WebSocket.stream(conn, msg)  # conn is NEW
{:ok, websocket, data} = Mint.WebSocket.encode(websocket, frame)  # websocket is NEW
```


## 2. Connection Lifecycle (Complete)

### Step 1: TCP/SSL Connect
```elixir
{:ok, conn} = Mint.HTTP.connect(:https, host, port,
  transport_opts: [verify: :verify_none, nodelay: true],
  protocols: [:http1]
)
```

**`transport_opts`** are passed directly to `:ssl.connect/4` or `:gen_tcp.connect/4`:
- `verify: :verify_none` — skip TLS cert verification
- `nodelay: true` — TCP_NODELAY (disables Nagle's algorithm)
- `mode: :binary` — binary mode (default in Mint)
- `active: :once` — deliver one message then go passive (engine's setting)

### Step 2: WS Upgrade Request
```elixir
{:ok, conn, ref} = Mint.WebSocket.upgrade(:wss, conn, "/ws", headers, opts)
```

What happens internally (`web_socket.ex:268-280`):
1. Generates random 16-byte nonce (Base64)
2. Stores nonce + extensions in conn private data
3. Sends `GET /ws` with headers: `upgrade: websocket`, `connection: upgrade`, `sec-websocket-version: 13`, `sec-websocket-key: <nonce>`, `sec-websocket-extensions: <negotiated>`

**Extension negotiation**: Pass `extensions: [Mint.WebSocket.PerMessageDeflate]` in opts to request compression. Server may accept or reject.

### Step 3: Wait for Upgrade Response
Server sends back: status 101 + headers + done. Collect them:
```elixir
# In handle_info (active mode):
case Mint.WebSocket.stream(conn, message) do
  {:ok, conn, responses} ->
    # responses = [{:status, ref, 101}, {:headers, ref, [...]}, {:done, ref}]
```

### Step 4: Create WebSocket Struct
When `{:done, ref}` arrives:
```elixir
{:ok, conn, websocket} = Mint.WebSocket.new(conn, ref, status, resp_headers, opts)
```

What happens internally (`web_socket.ex:338-362`):
1. Validates status == 101
2. Checks `sec-websocket-accept` nonce matches
3. Initializes accepted extensions (e.g., sets up zlib streams for deflate)
4. Stores request_ref in conn private `:websockets` list
5. Sets `:mode` (default `:active`) in conn private data

**Options for `new/5`**:
- `mode: :active` (default) — socket delivers messages via `handle_info`
- `mode: :passive` — you must call `Mint.WebSocket.recv/3` to poll

### Step 5: Send Frames
Two-step: encode → send:
```elixir
{:ok, websocket, data} = Mint.WebSocket.encode(websocket, {:text, payload})
{:ok, conn} = Mint.WebSocket.stream_request_body(conn, ref, data)
```

**What `encode` does** (`frame.ex:99-111`):
1. Translates friendly tuple `{:text, "hello"}` → internal record
2. Runs through extension pipeline (deflate if enabled)
3. Generates random 4-byte mask (client→server frames MUST be masked per RFC6455)
4. Encodes: `fin|reserved|opcode|masked|length|mask|XOR(payload,mask)`

**What `stream_request_body` does** (`web_socket.ex:515-532`):
- For HTTP/1 WS: bypasses Mint HTTP entirely, writes directly to SSL/TCP socket
- `ssl.send(socket, data)` or `gen_tcp.send(socket, data)`
- This is important: NO HTTP framing overhead

### Step 6: Receive + Decode
```elixir
# In handle_info:
case Mint.WebSocket.stream(conn, message) do
  {:ok, conn, [{:data, ref, data}]} ->
    {:ok, websocket, frames} = Mint.WebSocket.decode(websocket, data)
```

**What `stream/2` does for HTTP/1 WS** (`web_socket.ex:404-438`):
1. Gets socket from conn
2. Pattern matches on `{:ssl, socket, data}` or `{:tcp, socket, data}`
3. **Re-arms socket**: calls `ssl.setopts(socket, active: :once)` (the `reset_mode` function)
4. Returns `{:ok, conn, [{:data, ref, data}]}`

> **This is the `active: :once` loop**: each `stream/2` call sets socket back to `active: :once`,
> so exactly one more TCP message will be delivered to the process mailbox.

**What `decode/2` does** (`frame.ex:208-225`):
1. Concatenates new data with any buffered partial frame
2. Parses binary: `fin|reserved|opcode|masked|length|mask?|payload`
3. Unmasks payload (XOR with mask bytes)
4. Runs through extension decode pipeline (inflate if deflate enabled)
5. Resolves frame fragments (continuation frames)
6. Returns list of decoded frames + updated websocket (with remaining buffer)


## 3. Socket Mode: `active: :once` Pattern (CRITICAL)

The engine uses `active: :once` in transport_opts. Here's the full lifecycle:

```
connect(active: :once) → socket delivers ONE message → handle_info receives it
    → Mint.WebSocket.stream() processes it
    → reset_mode() calls ssl.setopts(socket, active: :once)  ← RE-ARMS
    → socket delivers next message → ...
```

**Why `active: :once`**: Backpressure. With `active: true`, the socket dumps ALL received data
into the process mailbox as fast as TCP delivers. With `active: :once`, each message is
explicitly acknowledged before the next one arrives. This prevents mailbox flooding.

**Trade-off**: `active: :once` adds one `setopts` syscall per message. For high-throughput
streams (200+ trades/s), this is ~200 extra syscalls/s. The alternative `active: true`
eliminates this overhead but risks mailbox growth if the process can't keep up.

**ws_worker.ex behavior**:
- Line 497: `transport_opts: [..., active: :once]` — initial connection
- Line 175/272: `Mint.HTTP.set_mode(conn, :active)` — switches to `active` mode after connect!
- Line 228: `Mint.WebSocket.stream(conn, msg)` — internally calls `reset_mode`

**Wait — there's a conflict**: The engine sets both `active: :once` in transport AND then
calls `set_mode(:active)`. What wins? Looking at `reset_mode` (line 429-438): it checks
`get_private(conn, :mode)`. If mode is `:active`, it calls `setopts(socket, active: :once)`.
So `set_mode(:active)` on the conn sets the `private.mode` to `:active`, and then each
`stream/2` call re-arms with `active: :once`. **The engine effectively uses `active: :once`
per-message, NOT true `active: true`.**


## 4. TCP Tuning

### TCP_NODELAY (Nagle's Algorithm)
**Current engine**: Does **NOT** set `nodelay: true`. This means Nagle's algorithm is ON,
which can buffer small writes for up to 40ms trying to coalesce them.

For receiving-only connections (our WS clients), Nagle mainly affects the SUBSCRIBE message sent.
For data reception, it's the server's Nagle setting that matters. But setting `nodelay: true`
on our side ensures our pong responses and subscribe messages go out immediately.

```elixir
# To enable (in transport_opts):
transport_opts: [verify: :verify_none, nodelay: true, ...]
```

### Buffer Size
Erlang default TCP receive buffer: ~8KB. For bursty streams, increasing can help:
```elixir
transport_opts: [..., buffer: 65536, recbuf: 65536, sndbuf: 65536]
```

### Socket Options Reference
These are standard `:ssl` / `:gen_tcp` options passed via `transport_opts`:

| Option | Default | Description |
|--------|---------|-------------|
| `nodelay` | `false` | TCP_NODELAY — disable Nagle's algorithm |
| `buffer` | ~8KB | Erlang buffer size for received data |
| `recbuf` | OS default | OS-level receive buffer |
| `sndbuf` | OS default | OS-level send buffer |
| `active` | `:once` | Socket message delivery mode |
| `mode` | `:binary` | `:binary` or `:list` for received data |
| `verify` | `:verify_peer` | TLS verification mode |


## 5. Compression (PerMessageDeflate)

### How It Works
Extension negotiated during upgrade. Uses `:zlib` (Erlang NIF wrapping zlib C library).

**Encode** (send): `zlib.deflate(data, :sync)` → strips trailing 4 bytes `0x00 0x00 0xFF 0xFF`
**Decode** (receive): appends `0x00 0x00 0xFF 0xFF` → `zlib.inflate(data)`

### Configuration
```elixir
Mint.WebSocket.upgrade(:wss, conn, "/ws", [],
  extensions: [
    {Mint.WebSocket.PerMessageDeflate, [
      client_max_window_bits: 15,     # Our compression window (9-15, default 15)
      server_max_window_bits: 15,     # Server's compression window
      client_no_context_takeover: false,  # Reset zlib state per message
      server_no_context_takeover: false
    ], [
      zlib_level: :best_compression,  # :none, :default, :best_speed, :best_compression
      zlib_memory_level: 8            # 1-9, higher = more memory = better compression
    ]}
  ]
)
```

### When to Use / Not Use
- **Trade streams**: Messages are small (100-500 bytes). Compression adds CPU overhead
  with minimal bandwidth savings. **Don't use** for trade-only streams.
- **Depth snapshots**: Can be 10-100KB. Compression helps significantly. **Use** if
  the exchange supports it.
- **Binance**: Does NOT support permessage-deflate on WS API. Requesting it is harmless
  (server just ignores), but adds no benefit.


## 6. Frame Buffering (Partial TCP Reads)

TCP is a stream protocol — a single `recv` may contain:
- Part of one frame (buffered until next `recv`)
- Exactly one frame
- Multiple complete frames
- Multiple frames + partial frame at the end

**`frame.ex` handles this** (`binary_to_frames`, line 227-237):
1. Concatenates buffer with new data
2. Tries to decode as many complete frames as possible (`decode_raw`)
3. If data runs out mid-frame: stores remainder in `websocket.buffer`
4. Returns decoded frames + updated websocket

This is why you MUST rebind `websocket` after every `decode` — the buffer state changes.


## 7. Frame Wire Format (RFC6455 §5.2)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
```

| Opcode | Type | Notes |
|--------|------|-------|
| 0x0 | Continuation | Fragment |
| 0x1 | Text | Must be valid UTF-8 |
| 0x2 | Binary | Arbitrary bytes |
| 0x8 | Close | Control frame |
| 0x9 | Ping | Control frame |
| 0xA | Pong | Control frame |

**Masking**: Client→server MUST be masked (random 4-byte key, XOR'd with payload).
Server→client is NOT masked. The `apply_mask` function in frame.ex is highly optimized —
processes 4 bytes at a time using binary pattern matching.


## 8. ws_worker.ex vs Official Example

| Aspect | Official GenServer Example | ws_worker.ex (Engine) |
|--------|---------------------------|----------------------|
| Stream function | `Mint.WebSocket.stream/2` | `Mint.WebSocket.stream/2` (line 228) |
| Initial socket | Default (passive until GenServer) | `active: :once` in transport_opts |
| After connect | Nothing special | `Mint.HTTP.set_mode(conn, :active)` (line 175) |
| Effect | `active: :once` loop via `reset_mode` | Same — `active: :once` via `reset_mode` |
| TCP_NODELAY | Not set | **Not set** (missing optimization!) |
| Compression | Not negotiated | Not negotiated |
| State struct | `defstruct [:conn, :websocket, ...]` | Map with `:conn`, `:websocket`, etc. |
| Send pattern | `encode` → `stream_request_body` | Same, wrapped in `ws_send/2` |
| Ping/Pong | Manual in `handle_frames` | Manual in `dispatch_frames` |
| Reconnect | Not implemented | Full backoff + staleness + gap recovery |


## 9. Potential Optimizations for Engine

### Already Done
- [x] Correct endpoint (`stream.binance.com` not `data-stream.binance.vision`)

### Missing / Worth Testing
- [ ] **TCP_NODELAY**: Add `nodelay: true` to `transport_opts` in `open_connection`
- [ ] **Larger receive buffer**: Add `buffer: 65536` to reduce syscalls for bursty data
- [ ] **Compression**: Not relevant for Binance (doesn't support it), but other exchanges may
- [ ] **`active: true` vs `active: :once`**: Current engine does `active: :once` (backpressure).
  For our use case where the parsing is fast, `active: true` could reduce syscall overhead.
  But risk is mailbox flooding if Zig NIF blocks.


## 10. Common Mistakes (Hit During Benchmarking)

| Mistake | What Went Wrong | Fix |
|---------|----------------|-----|
| `send_frame/3` | Function doesn't exist | `encode/2` + `stream_request_body/3` |
| `Mint.HTTP.stream/2` for WS | Doesn't handle WS-specific socket ownership | Use `Mint.WebSocket.stream/2` |
| Forgot `Mint.WebSocket.new/4` | Upgrade gives `conn + ref`, not `websocket` | Call `new` after `{:done, ref}` |
| `active: :once` + separate process | Socket stops delivering after upgrade | `set_mode(:active)` before waiting, or use GenServer |
| Not rebinding `conn`/`websocket` | Stale state causes silent failures | Every call returns NEW struct |
| Multiple connections in one process | Hard to demux socket messages | Use separate GenServers (engine does this) |
| `mode: :passive` in `new/5` | `stream/2` doesn't re-arm | Use `recv/3` instead or omit option |
