# 5. Rust RFC: bench black box

`C-rfc_2360-bench-black-box` · [C_github_commits_9step](README.md)

Source: <https://github.com/rust-lang/rfcs/blob/d2705ad64ba47e812a2b6b19d6f613fb4c14c5e0/text/2360-bench-black-box.md> · License: MIT OR Apache-2.0 · 23 commits touching the file; 21 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 3 | 0 | 0.00 | source_title |
| 1 | revision_1 | 659 | 0 | 0.23 | commit ec42fd0b7f (2018-03-12) |
| 2 | revision_2 | 791 | 0 | 0.48 | commit 6ccddcc324 (2018-08-29) |
| 3 | revision_3 | 859 | 0 | 0.52 | commit b0e04a6005 (2018-10-08) |
| 4 | revision_4 | 933 | 0 | 0.67 | commit b1cce1aefa (2018-10-10) |
| 5 | revision_5 | 985 | 0 | 0.73 | commit 51b12b91c5 (2019-02-19) |
| 6 | revision_6 | 996 | 0 | 0.78 | commit bb7876c2e6 (2019-02-19) |
| 7 | revision_7 | 1032 | 0 | 0.82 | commit ce164eeed0 (2019-02-19) |
| 8 | final | 1390 | 0 | 1.00 | commit f17e8623ee (2025-11-28) |

<details><summary><b>Step 0 — title</b> (3 words)</summary>

````text
bench black box
````

</details>

<details><summary><b>Step 1 — revision_1</b> (659 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds two functions to `core::mem`: `black_box` and `clobber`, which are
mainly useful for writing benchmarks.

# Motivation
[motivation]: #motivation

The `black_box` and `clobber` functions are useful for writing synthetic
benchmarks where, due to the constrained nature of the benchmark, the compiler
is able to perform optimizations that wouldn't otherwise trigger in practice.

The implementation of these functions is backend-specific and requires inline
assembly. Such that if the standard library does not provide them, the users are
required to use brittle workarounds on nightly.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


## `mem::black_box`

The function:

```rust
pub fn black_box<T>(x: T) -> T;
```

prevents the value `x` from being optimized away and flushes pending reads/writes
to memory. It does not prevent optimizations on the expression generating the
value `x` nor on the return value of the function. For
example ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32{ 
  mem::black_box(2 + x);
  3
}
let a = foo(2);
```

Here, the compiler can simplify the expression `2 + x` into `2 + 2` and then
`4`, but it is not allowed to discard `4`. Instead, it must store `4` into a
register even though it is not used by anything afterwards.

## `mem::clobber`

The function

```rust
pub fn clobber() -> ();
```
 	 
flushes all pending writes to memory. Memory managed by block scope objects must
be "escaped" with `black_box` . 

Using `mem::{black_box, clobber}` we can benchmark `Vec::push` as follows:

```rust
fn bench_vec_push_back(bench: Bencher) -> BenchResult {
    let n = /* large enough number */;
    let mut v = Vec::with_capacity(n);
    bench.iter(|| {
        // Escape the vector pointer:
        mem::black_box(v.as_ptr());
        v.push(42_u8);
        // Flush the write of 42 back to memory:
        mem::clobber();
    })
}
```

To measure the cost of `Vec::push`, we pre-allocate the `Vec` to avoid
re-allocating memory during the iteration. Since we are allocating a vector,
writing values to it, and dropping it, LLVM is actually able of optimize code
like this away ([`rust.godbolt.org`](https://godbolt.org/g/QMs77J)). 

To make this a suitable benchmark, we use `mem::clobber()` to force LLVM to
write `42` back to memory. Note, however, that if we try this LLVM still manages
to optimize our benchmark away ([`rust.godbolt.org`](https://godbolt.org/g/r9K2Bk))!

The problem is that the memory of our vector is managed by an object in block
scope. That is, since we haven't shared this memory with anything, no other code
in our program can have a pointer to it, so LLVM does not need to schedule any
writes to this memory, and there are no pending memory writes to flush! 

What we must do is tell LLVM that something might also have a pointer to this
memory, and this is what we use `mem::black_box` for in this case
([`rust.godbolt.or`](https://godbolt.org/g/3wBxay)).

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

* `mem::black_box(x)`: flushes all pending writes/read to memory and prevents
  `x` from being optimized away while still allowing optimizations on the
  expression that generates `x`.
* `mem::clobber`: flushes all pending writes to memory.

# Drawbacks
[drawbacks]: #drawbacks

TBD.

# Rationale and alternatives
[alternatives]: #alternatives

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::mem::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::mem::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

These two exact functions are provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the `test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

TBD.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (791 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds one function, `core::hint::black_box`, which is a hint to the
optimizer to disable certain compiler optimizations. 

# Motivation
[motivation]: #motivation

A tool for preventing compiler optimizations is widely useful. One application
is writing synthetic benchmarks, where, due to the constrained nature of the
benchmark, the compiler is able to perform optimizations that wouldn't otherwise
trigger in practice. Another application is writing constant time code, where it
is undesirable for the compiler to optimize certain operations depending on the
context in which they are executed.

The implementation of this function is backend-specific and currently requires
inline assembly. No viable alternative is available in stable Rust.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


## `hint::black_box`

The function:

```rust
/// An _unknown_ function that returns `x`.
pub unsafe fn black_box<T>(x: T) -> T;
```

is an _unknown_ function, that is, a function that the compiler cannot make any
assumptions about. It can potentially use `x` in any possible valid way that
`unsafe` Rust code is allowed to, and requires the compiler to be maximally
pessimistic in terms of optimizations. The compiler is still allowed to optimize
the expression generating `x`. This function returns `x` and is a no-op in the
virtual machine.

For example ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32{ 
  unsafe { hint::black_box(2 + x) };
  3
}
let a = foo(2);
```

In the call to `foo(2)` the compiler is allowed to simplify the expression `2 + x` 
down to `4`, but `4` must be stored into memory even though it is not read by
anything afterwards because `black_box` could try to read it.

### Benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
snippet, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

Here, we allocate the `Vec`, push into it without growing its capacity, and drop
it, without ever using it for anything. If we look at the assembly
(https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

it is pretty amazing: LLVM has actually managed to completely optimize the `Vec`
allocation and call to `push_cap` away! In our real application, we would
probably use the vector for something, preventing all of these optimizations
from triggering, but in this synthetic benchmark LLVM optimizations are
producing a benchmark that won't tell us anything about the cost of `Vec::push`.

We can use `hint::black_box` to create a more realistic synthetic benchmark
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        unsafe {
            black_box(v.as_ptr());
            v.push(black_box(i));
            black_box(v.as_ptr());
        }
    }
}
```

that prevents LLVM from assuming anything about the vector across the calls to
`Vec::push`.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```
mod core::hint {
    /// An _unknown_ unsafe function that returns `x`.
    pub unsafe fn black_box<T>(x: T) -> T;
}
```

is an _unknown_ `unsafe` function that can perform any valid operation on `x`
that `unsafe` Rust is allowed to perform. This function returns `x` and is a
no-op in the virtual machine.

# Drawbacks
[drawbacks]: #drawbacks

TBD.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

TBD.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (859 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds one function, `core::hint::black_box`, which is a hint to the
optimizer to disable certain compiler optimizations. 

# Motivation
[motivation]: #motivation

A tool for preventing compiler optimizations is widely useful. One application
is writing synthetic benchmarks, where, due to the constrained nature of the
benchmark, the compiler is able to perform optimizations that wouldn't otherwise
trigger in practice. Another application is writing constant time code, where it
is undesirable for the compiler to optimize certain operations depending on the
context in which they are executed.

The implementation of this function is backend-specific and currently requires
inline assembly. No viable alternative is available in stable Rust.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


## `hint::black_box`

The function:

```rust
/// An _unknown_ function that returns `x`.
pub fn black_box<T>(x: T) -> T;
```

returns `x` and is an _unknown_ function, that is, a function that the compiler
cannot make any assumptions about. It can use `x` in any possible valid way that
Rust code is allowed to without introducing undefined behavior in the calling
code. This requires the compiler to be maximally pessimistic in terms of
optimizations. While the compiler must assume that `black_box` performs any
legal mutation of `x`, the programmer can rely on `black_box` not actually
having any effect (other than inhibiting optimizations).

For example ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32{ 
  hint::black_box(2 + x);
  3
}
let a = foo(2);
```

In the call to `foo(2)` the compiler is allowed to simplify the expression `2 +
x` down to `4`. However, even though `4` is not read by anything afterwards, it
must be computed and materialized, for example, by storing it into memory, a
register, etc. because `black_box` could try to read it.

### Benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
snippet, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

Here, we allocate the `Vec`, push into it without growing its capacity, and drop
it, without ever using it for anything. If we look at the assembly
(https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

it is pretty amazing: LLVM has actually managed to completely optimize the `Vec`
allocation and call to `push_cap` away! In our real application, we would
probably use the vector for something, preventing all of these optimizations
from triggering, but in this synthetic benchmark LLVM optimizations are
producing a benchmark that won't tell us anything about the cost of `Vec::push`.

We can use hint::black_box to create a more realistic synthetic benchmark. The
compiler has to assume that `black_box` observes and mutates its argument, hence
it cannot optimize away the whole benchmark (https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        black_box(v.as_ptr());
        v.push(black_box(i));
        black_box(v.as_ptr());
    }
}
```

that prevents LLVM from assuming anything about the vector across the calls to
`Vec::push`.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```
mod core::hint {
    /// An _unknown_ function that returns `x`.
    pub fn black_box<T>(x: T) -> T;
}
```

hint is a `NOP` that returns `x`. It behaves like an _unknown_ function that can
perform any valid operation on `x` that Rust is allowed to perform without
introducing undefined behavior in the calling code.

Note: in practice this means that the compiler will optimize under the
pessimistic assumption that `black_box` might do anything with the data it got.

# Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

TBD.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (933 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds `core::hint::black_box`, a hint to disable certain compiler
optimizations.

# Motivation
[motivation]: #motivation

A hint to disable compiler optimizations is widely useful. One such application
is writing synthetic benchmarks where, due to the constrained nature of the
benchmark, the compiler is able to perform optimizations that wouldn't otherwise
trigger in practice.

There are currently no viable stable Rust alternatives for `black_box`. The
current nightly Rust implementations all rely on inline assembly.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

## `hint::black_box`

The hint:

```rust
pub fn black_box<T>(x: T) -> T;
```

behaves like the [identity function][identity_fn]: it just returns `x` and has
no effects. However, Rust implementations are _encouraged_ to assume that
`black_box` can use `x` in any possible valid way that Rust code is allowed to
without introducing undefined behavior in the calling code. That is,
implementations are encouraged to be maximally pessimistic in terms of
optimizations.

This property makes `black_box` useful for writing code in which certain
optimizations are not desired. However, disabling optimizations is not
guaranteed, which means that `black_box` is not a solution for programs that
rely on certain optimizations being disabled for correctness, like, for example,
constant time code.

### Example 1 - basics 

Example 1 ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32{ 
  hint::black_box(2 + x);
  3
}
let a = foo(2);
```

In this example, the compiler simplifies the expression `2 + x` down to `4`.
However, even though `4` is not read by anything afterwards, it must be computed
and materialized, for example, by storing it into memory, a register, etc.
because the current Rust implementation assumes that `black_box` could try to
read it.

### Example 2 - benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
example, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

This example allocates a `Vec`, pushes into it without growing its capacity, and
drops it, without ever using it for anything. The current Rust implementation
emits the following `x86_64` machine code (https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

LLVM is pretty amazing: it has optimized the `Vec` allocation and the calls to
`push_cap` away. In doing so, it has made our benchmark useless. It won't
measure the time it takes to perform the calls to `Vec::push` as we intended. 

In real applications, the program will use the vector for something, preventing
these optimizations. To produce a benchmark that takes that into account, we can
hint the compiler that the `Vec` is used for something
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        black_box(v.as_ptr());
        v.push(black_box(i));
        black_box(v.as_ptr());
    }
}
```

Inspecting the machine code reveals that, for this particular Rust
implementation, `black_box` successfully prevents LLVM from performing the
optimization that removes the `Vec::push` calls that we wanted to measure.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```rust
mod core::hint {
    /// Identity function that disables optimizations.
    pub fn black_box<T>(x: T) -> T;
}
```

is a `NOP` that returns `x`, that is, its operational semantics are equivalent
to the [identity function][identity_fn].


Implementations are encouraged, _but not required_, to treat `black_box` as an
_unknown_ function that can perform any valid operation on `x` that Rust is
allowed to perform without introducing undefined behavior in the calling code.
That is, to optimize `black_box` under the pessimistic assumption that it might
do anything with the data it got.

[identity_fn]: https://doc.rust-lang.org/nightly/std/convert/fn.identity.html

# Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

@Centril asked whether `black_box` should be a `const fn`. The current
implementation uses inline assembly. It is unclear at this point whether
`black_box` should be a `const fn`, and if it should, how exactly would we go
about it. We do not have to resolve this issue before stabilization since we can
always make it a `const fn` later, but we should not forget about it either.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (985 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds `core::hint::black_box` (see [black box]), an identity function
that hints the compiler to be maximally pessimistic in terms of the assumptions
about what `black_box` could do.

[black box]: https://en.wikipedia.org/wiki/Black_box

# Motivation
[motivation]: #motivation

Due to the constrained nature of synthetic benchmarks, the compiler is often
able to perform optimizations that wouldn't otherwise trigger in practice, like
completely removing a benchmark if it has no side-effects. 

Currently, stable Rust users need to introduce expensive operations into their
programs to prevent these optimizations. Examples thereof are volatile loads and
stores, or calling unknown functions via C FFI. These operations incur overheads
that often would not be present in the application the synthetic benchmark is
trying to model.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

## `hint::black_box`

The hint:

```rust
pub fn black_box<T>(x: T) -> T;
```

behaves like the [identity function][identity_fn]: it just returns `x` and has
no effects. However, Rust implementations are _encouraged_ to assume that
`black_box` can use `x` in any possible valid way that Rust code is allowed to
without introducing undefined behavior in the calling code. That is,
implementations are encouraged to be maximally pessimistic in terms of
optimizations.

This property makes `black_box` useful for writing code in which certain
optimizations are not desired. However, disabling optimizations is not
guaranteed, which means that `black_box` is not a solution for programs that
rely on certain optimizations being disabled for correctness, like, for example,
constant time code.

### Example 1 - basics 

Example 1 ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32 { 
  hint::black_box(2 + x);
  3
}
let a = foo(2);
```

In this example, the compiler may simplify the expression `2 + x` down to `4`.
However, even though `4` is not read by anything afterwards, it must be computed
and materialized, for example, by storing it into memory, a register, etc.
because the current Rust implementation assumes that `black_box` could try to
read it.

### Example 2 - benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
example, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

This example allocates a `Vec`, pushes into it without growing its capacity, and
drops it, without ever using it for anything. The current Rust implementation
emits the following `x86_64` machine code (https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

LLVM is pretty amazing: it has optimized the `Vec` allocation and the calls to
`push_cap` away. In doing so, it has made our benchmark useless. It won't
measure the time it takes to perform the calls to `Vec::push` as we intended. 

In real applications, the program will use the vector for something, preventing
these optimizations. To produce a benchmark that takes that into account, we can
hint the compiler that the `Vec` is used for something
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        black_box(v.as_ptr());
        v.push(black_box(i));
        black_box(v.as_ptr());
    }
}
```

Inspecting the machine code reveals that, for this particular Rust
implementation, `black_box` successfully prevents LLVM from performing the
optimization that removes the `Vec::push` calls that we wanted to measure.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```rust
mod core::hint {
    /// Identity function that disables optimizations.
    pub fn black_box<T>(x: T) -> T;
}
```

is a `NOP` that returns `x`, that is, its operational semantics are equivalent
to the [identity function][identity_fn].


Implementations are encouraged, _but not required_, to treat `black_box` as an
_unknown_ function that can perform any valid operation on `x` that Rust is
allowed to perform without introducing undefined behavior in the calling code.
That is, to optimize `black_box` under the pessimistic assumption that it might
do anything with the data it got, even though it actually does nothing.

[identity_fn]: https://doc.rust-lang.org/nightly/std/convert/fn.identity.html

# Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

@Centril asked whether `black_box` should be a `const fn`. The current
implementation uses inline assembly. It is unclear at this point whether
`black_box` should be a `const fn`, and if it should, how exactly would we go
about it. We do not have to resolve this issue before stabilization since we can
always make it a `const fn` later, but we should not forget about it either
````

</details>

<details><summary><b>Step 6 — revision_6</b> (996 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds `core::hint::black_box` (see [black box]), an identity function
that hints the compiler to be maximally pessimistic in terms of the assumptions
about what `black_box` could do.

[black box]: https://en.wikipedia.org/wiki/Black_box

# Motivation
[motivation]: #motivation

Due to the constrained nature of synthetic benchmarks, the compiler is often
able to perform optimizations that wouldn't otherwise trigger in practice, like
completely removing a benchmark if it has no side-effects. 

Currently, stable Rust users need to introduce expensive operations into their
programs to prevent these optimizations. Examples thereof are volatile loads and
stores, or calling unknown functions via C FFI. These operations incur overheads
that often would not be present in the application the synthetic benchmark is
trying to model.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

## `hint::black_box`

The hint:

```rust
pub const fn black_box<T>(x: T) -> T;
```

behaves like the [identity function][identity_fn]: it just returns `x` and has
no effects. However, Rust implementations are _encouraged_ to assume that
`black_box` can use `x` in any possible valid way that Rust code is allowed to
without introducing undefined behavior in the calling code. That is,
implementations are encouraged to be maximally pessimistic in terms of
optimizations.

This property makes `black_box` useful for writing code in which certain
optimizations are not desired. However, disabling optimizations is not
guaranteed, which means that `black_box` is not a solution for programs that
rely on certain optimizations being disabled for correctness, like, for example,
constant time code.

### Example 1 - basics 

Example 1 ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32 { 
  hint::black_box(2 + x);
  3
}
let a = foo(2);
```

In this example, the compiler may simplify the expression `2 + x` down to `4`.
However, even though `4` is not read by anything afterwards, it must be computed
and materialized, for example, by storing it into memory, a register, etc.
because the current Rust implementation assumes that `black_box` could try to
read it.

### Example 2 - benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
example, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

This example allocates a `Vec`, pushes into it without growing its capacity, and
drops it, without ever using it for anything. The current Rust implementation
emits the following `x86_64` machine code (https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

LLVM is pretty amazing: it has optimized the `Vec` allocation and the calls to
`push_cap` away. In doing so, it has made our benchmark useless. It won't
measure the time it takes to perform the calls to `Vec::push` as we intended. 

In real applications, the program will use the vector for something, preventing
these optimizations. To produce a benchmark that takes that into account, we can
hint the compiler that the `Vec` is used for something
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        black_box(v.as_ptr());
        v.push(black_box(i));
        black_box(v.as_ptr());
    }
}
```

Inspecting the machine code reveals that, for this particular Rust
implementation, `black_box` successfully prevents LLVM from performing the
optimization that removes the `Vec::push` calls that we wanted to measure.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```rust
mod core::hint {
    /// Identity function that disables optimizations.
    pub const fn black_box<T>(x: T) -> T;
}
```

is a `NOP` that returns `x`, that is, its operational semantics are equivalent
to the [identity function][identity_fn].


Implementations are encouraged, _but not required_, to treat `black_box` as an
_unknown_ function that can perform any valid operation on `x` that Rust is
allowed to perform without introducing undefined behavior in the calling code.
That is, to optimize `black_box` under the pessimistic assumption that it might
do anything with the data it got, even though it actually does nothing.

[identity_fn]: https://doc.rust-lang.org/nightly/std/convert/fn.identity.html

# Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *const T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

* Naming: it is unclear whether `black_box` is the right name for this primitive
  at this point. Some argumens in favor or against are that:
     * pro: [black box] is a common term in computer programming, that conveys that
       nothing can be assumed about it except for its inputs and outputs.
     * con: `_box` has nothing to do with `Box` or `box`-syntax, which might be confusing
 
  Alternative names suggested: `pessimize`, `unoptimize`, `unprocessed`, `unknown`,
  `do_not_optimize` (Google Benchmark).
````

</details>

<details><summary><b>Step 7 — revision_7</b> (1032 words)</summary>

````text
# Summary
[summary]: #summary

This RFC adds `core::hint::black_box` (see [black box]), an identity function
that hints the compiler to be maximally pessimistic in terms of the assumptions
about what `black_box` could do.

[black box]: https://en.wikipedia.org/wiki/Black_box

# Motivation
[motivation]: #motivation

Due to the constrained nature of synthetic benchmarks, the compiler is often
able to perform optimizations that wouldn't otherwise trigger in practice, like
completely removing a benchmark if it has no side-effects. 

Currently, stable Rust users need to introduce expensive operations into their
programs to prevent these optimizations. Examples thereof are volatile loads and
stores, or calling unknown functions via C FFI. These operations incur overheads
that often would not be present in the application the synthetic benchmark is
trying to model.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

## `hint::black_box`

The hint:

```rust
pub fn black_box<T>(x: T) -> T;
```

behaves like the [identity function][identity_fn]: it just returns `x` and has
no effects. However, Rust implementations are _encouraged_ to assume that
`black_box` can use `x` in any possible valid way that Rust code is allowed to
without introducing undefined behavior in the calling code. That is,
implementations are encouraged to be maximally pessimistic in terms of
optimizations.

This property makes `black_box` useful for writing code in which certain
optimizations are not desired, but too unreliable when disabling these
optimizations is required for correctness.

### Example 1 - basics 

Example 1 ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32 { 
  hint::black_box(2 + x);
  3
}
let a = foo(2);
```

In this example, the compiler may simplify the expression `2 + x` down to `4`.
However, even though `4` is not read by anything afterwards, it must be computed
and materialized, for example, by storing it into memory, a register, etc.
because the current Rust implementation assumes that `black_box` could try to
read it.

### Example 2 - benchmarking `Vec::push`

The `hint::black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
example, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

This example allocates a `Vec`, pushes into it without growing its capacity, and
drops it, without ever using it for anything. The current Rust implementation
emits the following `x86_64` machine code (https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

LLVM is pretty amazing: it has optimized the `Vec` allocation and the calls to
`push_cap` away. In doing so, it has made our benchmark useless. It won't
measure the time it takes to perform the calls to `Vec::push` as we intended. 

In real applications, the program will use the vector for something, preventing
these optimizations. To produce a benchmark that takes that into account, we can
hint the compiler that the `Vec` is used for something
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        black_box(v.as_ptr());
        v.push(black_box(i));
        black_box(v.as_ptr());
    }
}
```

Inspecting the machine code reveals that, for this particular Rust
implementation, `black_box` successfully prevents LLVM from performing the
optimization that removes the `Vec::push` calls that we wanted to measure.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```rust
mod core::hint {
    /// Identity function that disables optimizations.
    pub fn black_box<T>(x: T) -> T;
}
```

is a `NOP` that returns `x`, that is, its operational semantics are equivalent
to the [identity function][identity_fn].


Implementations are encouraged, _but not required_, to treat `black_box` as an
_unknown_ function that can perform any valid operation on `x` that Rust is
allowed to perform without introducing undefined behavior in the calling code.
That is, to optimize `black_box` under the pessimistic assumption that it might
do anything with the data it got, even though it actually does nothing.

[identity_fn]: https://doc.rust-lang.org/nightly/std/convert/fn.identity.html

# Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

# Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

## `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

## `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

# Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

# Unresolved questions
[unresolved]: #unresolved-questions

* `const fn`: it is unclear whether `black_box` should be a `const fn`. If it
  were, that would hint that it cannot have any side-effects, or that it cannot
  do anything that `const fn`s cannot do. 

* Naming: it is unclear whether `black_box` is the right name for this primitive
  at this point. Some argumens in favor or against are that:
     * pro: [black box] is a common term in computer programming, that conveys
       that nothing can be assumed about it except for its inputs and outputs.
       con: [black box] often hints that the function has no side-effects, but
       this is not something that can be assumed about this API.
     * con: `_box` has nothing to do with `Box` or `box`-syntax, which might be confusing
 
  Alternative names suggested: `pessimize`, `unoptimize`, `unprocessed`, `unknown`,
  `do_not_optimize` (Google Benchmark).
````

</details>

<details><summary><b>Step 8 — final</b> (1390 words)</summary>

````text
## Summary
[summary]: #summary

This RFC adds `core::hint::bench_black_box` (see [black box]), an identity function
that hints the compiler to be maximally pessimistic in terms of the assumptions
about what `bench_black_box` could do.

[black box]: https://en.wikipedia.org/wiki/black_box

## Motivation
[motivation]: #motivation

Due to the constrained nature of synthetic benchmarks, the compiler is often
able to perform optimizations that wouldn't otherwise trigger in practice, like
completely removing a benchmark if it has no side-effects. 

Currently, stable Rust users need to introduce expensive operations into their
programs to prevent these optimizations. Examples thereof are volatile loads and
stores, or calling unknown functions via C FFI. These operations incur overheads
that often would not be present in the application the synthetic benchmark is
trying to model.

## Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

### `hint::bench_black_box`

The hint:

```rust
pub fn bench_black_box<T>(x: T) -> T;
```

behaves like the [identity function][identity_fn]: it just returns `x` and has
no effects. However, Rust implementations are _encouraged_ to assume that
`bench_black_box` can use `x` in any possible valid way that Rust code is allowed to
without introducing undefined behavior in the calling code. That is,
implementations are encouraged to be maximally pessimistic in terms of
optimizations.

This property makes `bench_black_box` useful for writing code in which certain
optimizations are not desired, but too unreliable when disabling these
optimizations is required for correctness.

#### Example 1 - basics 

Example 1 ([`rust.godbolt.org`](https://godbolt.org/g/YP2GCJ)):

```rust
fn foo(x: i32) -> i32 { 
  hint::bench_black_box(2 + x);
  3
}
let a = foo(2);
```

In this example, the compiler may simplify the expression `2 + x` down to `4`.
However, even though `4` is not read by anything afterwards, it must be computed
and materialized, for example, by storing it into memory, a register, etc.
because the current Rust implementation assumes that `bench_black_box` could try to
read it.

#### Example 2 - benchmarking `Vec::push`

The `hint::bench_black_box` is useful for producing synthetic benchmarks that more
accurately represent the behavior of a real application. In the following
example, the function `bench` executes `Vec::push` 4 times in a loop:

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
      v.push(i);
    }
}

pub fn bench_push() -> Duration { 
    let mut v = Vec::with_capacity(4);
    let now = Instant::now();
    push_cap(&mut v);
    now.elapsed()
}
```

This example allocates a `Vec`, pushes into it without growing its capacity, and
drops it, without ever using it for anything. The current Rust implementation
emits the following `x86_64` machine code (https://rust.godbolt.org/z/wDckJF):


```asm
example::bench_push:
  sub rsp, 24
  call std::time::Instant::now@PLT
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 16], rdx
  lea rdi, [rsp + 8]
  call std::time::Instant::elapsed@PLT
  add rsp, 24
  ret
```

LLVM is pretty amazing: it has optimized the `Vec` allocation and the calls to
`push_cap` away. In doing so, it has made our benchmark useless. It won't
measure the time it takes to perform the calls to `Vec::push` as we intended. 

In real applications, the program will use the vector for something, preventing
these optimizations. To produce a benchmark that takes that into account, we can
hint the compiler that the `Vec` is used for something
(https://rust.godbolt.org/z/CeXmxN):

```rust
fn push_cap(v: &mut Vec<i32>) {
    for i in 0..4 {
        bench_black_box(v.as_ptr());
        v.push(bench_black_box(i));
        bench_black_box(v.as_ptr());
    }
}
```

Inspecting the machine code reveals that, for this particular Rust
implementation, `bench_black_box` successfully prevents LLVM from performing the
optimization that removes the `Vec::push` calls that we wanted to measure.

## Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

The 

```rust
mod core::hint {
    /// Identity function that disables optimizations.
    pub fn bench_black_box<T>(x: T) -> T;
}
```

is a `NOP` that returns `x`, that is, its operational semantics are equivalent
to the [identity function][identity_fn].


Implementations are encouraged, _but not required_, to treat `bench_black_box` as an
_unknown_ function that can perform any valid operation on `x` that Rust is
allowed to perform without introducing undefined behavior in the calling code.
That is, to optimize `bench_black_box` under the pessimistic assumption that it might
do anything with the data it got, even though it actually does nothing.

[identity_fn]: https://doc.rust-lang.org/nightly/std/convert/fn.identity.html

## Drawbacks
[drawbacks]: #drawbacks

Slightly increases the surface complexity of `libcore`.

## Rationale and alternatives
[alternatives]: #alternatives

Further rationale influencing this design is available in
https://github.com/nikomatsakis/rust-memory-model/issues/45

### `clobber`

A previous version of this RFC also provided a `clobber` function:

```rust
/// Flushes all pending writes to memory. 
pub fn clobber() -> ();
```

In https://github.com/nikomatsakis/rust-memory-model/issues/45 it was realized
that such a function cannot work properly within Rust's memory model.

### `value_fence` / `evaluate_and_drop`

An alternative design was proposed during the discussion on
[rust-lang/rfcs/issues/1484](https://github.com/rust-lang/rfcs/issues/1484), in
which the following two functions are provided instead:

```rust
#[inline(always)]
pub fn value_fence<T>(x: T) -> T {
    let y = unsafe { (&x as *T).read_volatile() };
    std::hint::forget(x);
    y
}

#[inline(always)]
pub fn evaluate_and_drop<T>(x: T) {
    unsafe {
        let mut y = std::hint::uninitialized();
        std::ptr::write_volatile(&mut y as *mut T, x);
        drop(y); // not necessary but for clarity
    }
}
```

This approach is not pursued in this RFC because these two functions:

* add overhead ([`rust.godbolt.org`](https://godbolt.org/g/aCpPfg)): `volatile`
  reads and stores aren't no ops, but the proposed `bench_black_box` and `clobber`
  functions are.
* are implementable on stable Rust: while we could add them to `std` they do not
  necessarily need to be there.

### `bench_input` / `bench_outpu`

@eddyb proposed
[here](https://github.com/rust-lang/rfcs/pull/2360#issuecomment-463594450) (and
the discussion that followed) to add two other hints instead:

* `bench_input`: `fn(T) -> T` (identity-like) may prevent some optimizations
  from seeing through the valid `T` value, more specifically, things like
  const/load-folding and range-analysis miri would still check the argument, and
  so it couldn't be e.g. uninitialized the argument computation can be
  optimized-out (unlike `bench_output`) mostly implementable today with the same
  strategy as `black_box`.

* `bench_output`: `fn(T) -> ()` (drop-like) may prevent some optimizations from
  optimizing out the computation of its argument the argument is not treated as
  "escaping into unknown code", i.e., you can't implement `bench_output(x)` as
  `{ bench_input(&mut x); x }`. What that would likely prevent is placing `x`
  into a register instead of memory, but optimizations might still see the old
  value of `x`, as if it couldn't have been mutated potentially implementable
  like `black_box` but `readonly`/`readnone` in LLVM.

From the RFC discussion there was consensus that we might want to add these
benchmarking hints in the future as well because their are easier to specify and
provide stronger guarantees than `bench_black_box`.

Right now, however, it is unclear whether these two hints can be implemented
strictly in LLVM. The comment thread shows that the best we can actually do
ends up implementing both of these as `bench_black_box` with the same effects.

Without a strict implementation, it is unclear which value these two intrinsics
would add, and more importantly, since their difference in semantics cannot be
shown, it is also unclear how we could teach users to use them correctly.

If we ever able to implement these correctly, we might want to consider
deprecating `bench_black_box` at that point, but whether it will be worth
deprecating is not clear either.

## Prior art
[prior-art]: #prior-art

Similar functionality is provided in the [`Google
Benchmark`](https://github.com/google/benchmark) C++ library: are called
[`DoNotOptimize`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L306)
(`bench_black_box`) and
[`ClobberMemory`](https://github.com/google/benchmark/blob/61497236ddc0d797a47ef612831fb6ab34dc5c9d/include/benchmark/benchmark.h#L317).
The `black_box` function with slightly different semantics is provided by the
`test` crate:
[`test::black_box`](https://github.com/rust-lang/rust/blob/master/src/libtest/lib.rs#L1551).

## Unresolved questions
[unresolved]: #unresolved-questions

* `const fn`: it is unclear whether `bench_black_box` should be a `const fn`. If it
  were, that would hint that it cannot have any side-effects, or that it cannot
  do anything that `const fn`s cannot do. 

* Naming: during the RFC discussion it was unclear whether `black_box` is the
  right name for this primitive but we settled on `bench_black_box` for the time
  being. We should resolve the naming before stabilization.
  
  Also, we might want to add other benchmarking hints in the future, like
  `bench_input` and `bench_output`, so we might want to put all of this
  into a `bench` sub-module within the `core::hint` module. That might
  be a good place to explain how the benchmarking hints should be used 
  holistically.
  
  Some arguments in favor or against using "black box" are that:
     * pro: [black box] is a common term in computer programming, that conveys
       that nothing can be assumed about it except for its inputs and outputs.
       con: [black box] often hints that the function has no side-effects, but
       this is not something that can be assumed about this API.
     * con: `_box` has nothing to do with `Box` or `box`-syntax, which might be confusing
 
  Alternative names suggested: `pessimize`, `unoptimize`, `unprocessed`, `unknown`,
  `do_not_optimize` (Google Benchmark).
````

</details>
