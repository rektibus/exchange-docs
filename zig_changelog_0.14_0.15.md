# Zig Changelog: 0.13 → 0.14 → 0.15.2

> Current version: **0.15.2** (Oct 12, 2025)
> Agent training cutoff: 0.13.x

---

## 0.14.0 (March 2025) — 251 contributors, 3467 commits

### Breaking Language Changes

| Change | Migration |
|--------|-----------|
| **`@fence` removed** | Use stronger memory orderings instead |
| **`@export` requires pointer** | Add `&` operator: `@export(&foo, ...)` |
| **`@setCold` → `@branchHint(.cold)`** | Replace all `@setCold(true)` calls |
| **Fields/declarations can't share names** | Rename conflicting identifiers |
| **`@typeInfo` union field access changed** | Update comptime reflection code |
| **`@splat` now supports arrays** | Non-breaking addition |
| **`@ptrCast` can change slice length** | Non-breaking addition |

### Breaking Stdlib Changes

| Change | Migration |
|--------|-----------|
| **`GeneralPurposeAllocator` → `DebugAllocator`** | Rename |
| **Unmanaged containers default** | `std.ArrayList` defaults to unmanaged — pass allocator explicitly to methods |
| **Managed containers deprecated** | Move to unmanaged variants |

### New Features
- **Labeled switch**: switch can be labeled, `continue :label` for state machines
- **Decl literals**: `.declLiteral()` syntax
- **Packed struct equality + atomics** improvements
- **Global variables** can init with address of each other
- **Faster x86 backend** (incremental compilation beta)

---

## 0.15.1 (Aug 20, 2025) — Major Release

### Breaking Language Changes

| Change | Impact | Migration |
|--------|--------|-----------|
| **`async/await` REMOVED** | Entire feature dropped | Use other concurrency patterns |
| **`usingnamespace` REMOVED** | Keyword eliminated | Explicitly import/reference needed decls |
| **Safer integer-to-float coercions** | Implicit coercions restricted | Add explicit `@intToFloat` / `@floatFromInt` |
| **`{f}` required for format methods** | `std.fmt` format strings | Add `{f}` specifier where needed |

### Breaking Stdlib Changes — I/O Overhaul ("Writergate")

| Change | Migration |
|--------|-----------|
| **Generic readers/writers removed** | Use `std.Io.Reader` and `std.Io.Writer` |
| **`writeFileAll`, `writeFileAllUnseeable` removed** | Use new file writer mechanisms |
| **`writeFileOptions` removed** | Use new file writer API |
| **`takeDelimiter` API changed** | Now `peekDelimiterInclusive` / `peekDelimiterExclusive` |
| **`std.fmt.allocPrintZ` → `std.fmt.allocPrintSentinel`** | Rename call |

### Performance
- **5x debug compilation speed** with x86 backend
- **aarch64 backend** in progress
- **Filesystem watching** for macOS build system

---

## 0.15.2 (Oct 12, 2025) — Bug Fix Release

- Primarily bug fixes
- String storage architecture fixes
- Union layout calculation fixes
- Minor `takeDelimiter` behavior tweak vs 0.15.1

---

## Impact on EnsoX Codebase

Our Zig code (`apps/data-plane-zig/src/`) successfully compiles on 0.15.2.
Key areas that were likely affected by the migration:

1. **No `async/await`** — we use NIF threading (Elixir schedules, Zig computes)
2. **No `usingnamespace`** — explicit imports everywhere
3. **Unmanaged allocators** — allocator passed to methods explicitly
4. **I/O changes** — `std.Io.Reader`/`Writer` if we use any (mostly we don't — QuestDB writes via TCP ILP)
5. **`@typeInfo` changes** — may affect comptime reflection in `comptime_adapter.zig`
