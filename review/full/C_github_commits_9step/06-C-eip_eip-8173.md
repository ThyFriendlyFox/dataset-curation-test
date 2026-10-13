# 6. Ethereum EIP: Foundations of EVM Control Flow

`C-eip_eip-8173` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/ethereum/EIPs/blob/4fbe53b41d524e98c811503aae1c9d6470af28e8/EIPS/eip-8173.md> · License: CC0-1.0 · 13 commits touching the file; 13 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 5 | 0 | 0.00 | source_title |
| 1 | revision_1 | 2759 | 0 | 0.64 | commit 2ae38c6916 (2026-04-22) |
| 2 | revision_2 | 2918 | 0 | 0.67 | commit 02c89e5faa (2026-05-26) |
| 3 | revision_3 | 2927 | 0 | 0.68 | commit 82c0765358 (2026-05-26) |
| 4 | revision_4 | 3191 | 0 | 0.78 | commit b8bfdfbeed (2026-05-30) |
| 5 | revision_5 | 3351 | 0 | 0.79 | commit 7d4215ebbf (2026-07-16) |
| 6 | revision_6 | 3704 | 0 | 0.83 | commit ed90fa59a6 (2026-07-22) |
| 7 | revision_7 | 4033 | 0 | 0.86 | commit 8fceedac5b (2026-07-29) |
| 8 | final | 3642 | 0 | 1.00 | commit 0b9221c795 (2026-08-30) |

<details><summary><b>Step 0 — title</b> (5 words)</summary>

````text
Foundations of EVM Control Flow
````

</details>

<details><summary><b>Step 1 — revision_1</b> (2759 words)</summary>

````text
## Abstract

This Informational EIP provides foundational context for understanding control flow in the EVM. It covers the historical development of control flow mechanisms in computing, the technical foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow, including [EIP-615](./eip-615.md): Subroutines and Static Jumps for the EVM, [EIP-4750](./eip-4750.md): EOF Functions, [EIP-7979](./eip-7979.md): Call and Return Opcodes, [EIP-8013](./eip-8013.md): Static Relative Jumps, discussions around RISC-V migration and ZK verification infrastructure, and discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards which controlled a system of rods, gears and other machinery to implement arithmetic, storage (for 1,000 40-digits decimal numbers) and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1842: Computer Programing

The first published description of the Analytical Engine was in French, by L. F. Menabre, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming. The notes include her famous program for recursively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

#### Turing, 1945: Calls and Returns

In 1945 Alan Turing proposed his Automatic Computing Engine[^2] (ACE), where he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE supported calls directly with a stack of mercury-filled memory crystals holding return addresses. Turing's design was for a 32-bit RISC machine with a vacuum tube integer ALU, floating point microcode, 32 registers, a 1024-entry return stack, and 32K of RAM on a 1 MHz bus. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names and levels of complexity have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  Physical machines including the Burroughs 5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000 and Intelx86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear time compilers also supports any other code that needs to traverse the control flow of a program of a program, traversing each path only once.

### Control Flow

Among the most imporant reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with no more than one entry and one exit)
* _Edges_ represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* constructing ZK proof systems
* and many more

#### Dynamic Control Flow: The Problem

Dynamic jumps make dynamic control flow possible, make quadraticaly complex _CFGs_ possible, and can make static analysis of control difficult to impossible.  Dynamic jumps are not a problem for machines which run on physical hardware -- their instructions are designed for speed.  But they are uncommon in virtual machines whose code is the source for downstream tools.  This is because, as we will illustrate below, building and traversing a dynamic control flow graph can take quadratic space and time.  For this reason Java and Wasm do not support dynamic jumps and CLI carefully restricts them.

#### EVM: Dynamic Control Flow

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail, what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```

   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with at most one entry (a `JUMPDEST`) and one exit (a `JUMP`), and each arc is a transfer of control.  Arcs on the left are backwards branches, arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![_ Graphs_](../assets/eip-8173/control-flow.svg)

To be precise the number of arcs in these graphs is equal to the number of blocks minus one, squared.  That is, the number of possible paths of control flow, and thus the time needed to traverse them all, is quadratic in the size of the program.  At each block's exiting instruction, (except the `stop`) the analyzer cannot know _a priori_ where control will transfer.  Every block might jump to any other block, creating a fully-connected CFG with O(N²) possible paths. Traversing all paths to verify them requires O(N²) time, and this is not just a theoretical worst-case, as shown above.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores intermediate links on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

For Ethereum, this quadratic behavior is a _denial-of-service vulnerability_ for any online static analysis, including validating bytecode and AOT compilation at contract creation time and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable or even mathematically impossible. For a few examples, consider these abstracts from just a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static analysis renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^3]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^4]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^5]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^6]

In our experience, to avoid the problems of dynamic control flow VMs use static jumps, calls and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _Static control flow_ means that the destinations of every jump or call is determinable _a priori,_ before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups [^7]

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups, we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace, a sequence of state changes recording the value of registers, memory, stack, storage, etc. at each step. The trace is a complete record of the computation.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied.
* _Witnesses:_ The witness is the data the prover provides to prove that a computation is correct. For an execution trace, the witness includes the trace itself plus auxiliary data that helps prove the constraints are satisfied.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, while revealing Zero Knowledge of the witness itself.

A _ZK-Rollup sequencer or prover batches many transactions and constructs a ZK proof that all transactions executed correctly. The proof is then submi_tted to L1, where it is quickly verified. Key implications:

* _Trace size:_ With dynamic jumps, the prover may need to explore many paths before finding the correct one, making traces longer and less efficient.
* _Circuit complexity:_ A circuit covering dynamic jumps must account for all possible jump destinations at each dynamic jump. This significantly increases constraint count.
* _Proof generation time:_ Larger traces and circuits mean more computation for the prover, directly affecting latency and cost.
* _Hardware requirements:_  More complex circuits and longer traces demand more memory and computation, requiring specialized hardware for rollup operators.

Static control flow enables:

* _Predictable trace sizes_ (linear in execution length, not exponential in jump possibilities)
* _Simpler circuits_ (only actual execution paths need constraints)
* _Faster proof generation_
* _Lower hardware requirements for prover operators_

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but require fraud proofs to dispute invalid state roots. A fraud proof is a proof that a specific transaction executed incorrectly. Key implications of static analysis include:

* _Bytecode validation:_ Cleaner bytecode with static control flow enables easier validation of contract behavior.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction and prove correctness (or incorrectness). Static control flow makes this re-execution and proof more tractable.
* _Interactive verification:_ Some optimistic rollup designs use interactive verification games. Clear control flow simplifies the game protocol.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK Clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture which is seeing increasing use in the ZK community.  One currrent strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or reth to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose we have [EIP-7937](./eip-7937.md): EVM64 — 64-bit mode EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big of a problem.

## Specification

Four EIPs currently specify new EVM opcodes and semantics for static control flow:  [EIP-615: Subroutines and Static Jumps for the EVM](./eip-615.md), [EIP-4750: EOF - Functions](./eip-4750.md), [EIP-7979: Call and Return Opcodes for the EVM](./eip-7979.md), and [EIP-8013: Static relative jumps and calls for the EVM](./eip-8013.md).  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other other.  In particular, EIP-7979 can be used to implement every other EIP here.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static  control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have leveraged for decades.

## Security Considerations

This Informational proposal itself specificies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the EIPs it references, rather, it helps to motivate and specify them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Menabre",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of The Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E"
        }
      ],
      "DOI": "comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "arXiv:2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "arXiv:2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a sound  Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "arXiv:2103.09113",
      "title": "EtherSolve: Computing an Accurate  Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "arXiv:2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain,  et al.  Doi: ",
          "given": "Akshita"
        }
      ],
      "DOI": "10.48550/Arxiv.2301.12695",
      "title": "Exploring The Efficacy Of Rollups’ A Comparative Study Of Optimistic And ZK-Rollups And Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://arxiv.org/10.48550/Arxiv.2301.12695"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 2 — revision_2</b> (2918 words)</summary>

````text
## Abstract

This Informational EIP provides foundational context for understanding control flow in the EVM. It covers the historical development of control flow mechanisms in computing, the technical foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow, including [EIP-615](./eip-615.md): Subroutines and Static Jumps for the EVM, [EIP-4750](./eip-4750.md): EOF Functions, [EIP-7979](./eip-7979.md): Call and Return Opcodes, [EIP-8013](./eip-8013.md): Static Relative Jumps, discussions around RISC-V migration and ZK verification infrastructure, and discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards which controlled a system of rods, gears and other machinery to implement arithmetic, storage (for 1,000 40-digits decimal numbers) and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1842: Computer Programing

The first published description of the Analytical Engine was in French, by L. F. Menabre, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming. The notes include her famous program for recursively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytic Engine's power:  "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection".[^2]:  "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1945: Calls and Returns

In 1945 Alan Turing proposed his Automatic Computing Engine[^3] (ACE), where he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE supported calls directly with a stack of mercury-filled memory crystals holding return addresses. Turing's design was for a 32-bit RISC machine with a vacuum tube integer ALU, floating point microcode, 32 registers, a 1024-entry return stack, and 32K of RAM on a 1 MHz bus. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names — subroutines, procedures, functions, methods — and levels of complexity — from link registers to explicit return stacks — have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  Physical machines including the Burroughs 5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000 and Intelx86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear time compilers also supports any other code that needs to traverse the control flow of a program of a program, traversing each path only once.

### Control Flow

Among the most imporant reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with no more than one entry and one exit)
* _Edges_ represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* constructing ZK proof systems
* and many more

#### Dynamic Control Flow: The Problem

Dynamic jumps make dynamic control flow possible, make quadraticaly complex _CFGs_ possible, and can make static analysis of control difficult to impossible.  Dynamic jumps are not a problem for machines which run on physical hardware -- their instructions are designed for speed.  But they are uncommon in virtual machines whose code is the source for downstream tools.  This is because, as we will illustrate below, building and traversing a dynamic control flow graph can take quadratic space and time.  For this reason Java and Wasm do not support dynamic jumps and CLI carefully restricts them.

#### EVM: Dynamic Control Flow

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail, what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```

   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with at most one entry (a `JUMPDEST`) and one exit (a `JUMP`), and each arc is a transfer of control.  Arcs on the left are backwards branches, arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![_ Graphs_](../assets/eip-8173/control-flow.svg)

To be precise the number of arcs in these graphs is equal to the number of blocks minus one, squared.  That is, the number of possible paths of control flow, and thus the time needed to traverse them all, is quadratic in the size of the program.  At each block's exiting instruction, (except the `stop`) the analyzer cannot know _a priori_ where control will transfer.  Every block might jump to any other block, creating a fully-connected CFG with O(N²) possible paths. Traversing all paths to verify them requires O(N²) time, and this is not just a theoretical worst-case, as shown above.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores intermediate links on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

For Ethereum, this quadratic behavior is a _denial-of-service vulnerability_ for any online static analysis, including validating bytecode and AOT compilation at contract creation time and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable or even mathematically impossible. For a few examples, consider these abstracts from just a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static analysis renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In our experience, to avoid the problems of dynamic control flow VMs use static jumps, calls and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _Static control flow_ means that the destinations of every jump or call is determinable _a priori,_ before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups [^8]

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups, we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace, a sequence of state changes recording the value of registers, memory, stack, storage, etc. at each step. The trace is a complete record of the computation.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied.
* _Witnesses:_ The witness is the data the prover provides to prove that a computation is correct. For an execution trace, the witness includes the trace itself plus auxiliary data that helps prove the constraints are satisfied.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, while revealing Zero Knowledge of the witness itself.

A _ZK-Rollup sequencer or prover batches many transactions and constructs a ZK proof that all transactions executed correctly. The proof is then submi_tted to L1, where it is quickly verified. Key implications:

* _Trace size:_ With dynamic jumps, the prover may need to explore many paths before finding the correct one, making traces longer and less efficient.
* _Circuit complexity:_ A circuit covering dynamic jumps must account for all possible jump destinations at each dynamic jump. This significantly increases constraint count.
* _Proof generation time:_ Larger traces and circuits mean more computation for the prover, directly affecting latency and cost.
* _Hardware requirements:_  More complex circuits and longer traces demand more memory and computation, requiring specialized hardware for rollup operators.

Static control flow enables:

* _Predictable trace sizes_ (linear in execution length, not exponential in jump possibilities)
* _Simpler circuits_ (only actual execution paths need constraints)
* _Faster proof generation_
* _Lower hardware requirements for prover operators_

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but require fraud proofs to dispute invalid state roots. A fraud proof is a proof that a specific transaction executed incorrectly. Key implications of static analysis include:

* _Bytecode validation:_ Cleaner bytecode with static control flow enables easier validation of contract behavior.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction and prove correctness (or incorrectness). Static control flow makes this re-execution and proof more tractable.
* _Interactive verification:_ Some optimistic rollup designs use interactive verification games. Clear control flow simplifies the game protocol.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK Clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture which is seeing increasing use in the ZK community.  One currrent strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or reth to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose we have [EIP-7937](./eip-7937.md): EVM64 — 64-bit mode EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big of a problem.

## Specification

Four EIPs currently specify new EVM opcodes and semantics for static control flow:  [EIP-615: Subroutines and Static Jumps for the EVM](./eip-615.md), [EIP-4750: EOF - Functions](./eip-4750.md), [EIP-7979: Call and Return Opcodes for the EVM](./eip-7979.md), and [EIP-8013: Static relative jumps and calls for the EVM](./eip-8013.md).  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other other.  In particular, EIP-7979 can be used to implement every other EIP here.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static  control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have leveraged for decades.

## Security Considerations

This Informational proposal itself specificies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the EIPs it references, rather, it helps to motivate and specify them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabre",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of The Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```
[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.", 
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E"
        }
      ],
      "DOI": "comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "arXiv:2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "arXiv:2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a sound  Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "arXiv:2103.09113",
      "title": "EtherSolve: Computing an Accurate  Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "arXiv:2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain,  et al.  Doi: ",
          "given": "Akshita"
        }
      ],
      "DOI": "10.48550/Arxiv.2301.12695",
      "title": "Exploring The Efficacy Of Rollups’ A Comparative Study Of Optimistic And ZK-Rollups And Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://arxiv.org/10.48550/Arxiv.2301.12695"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 3 — revision_3</b> (2927 words)</summary>

````text
## Abstract

This Informational EIP provides foundational context for understanding control flow in the EVM. It covers the historical development of control flow mechanisms in computing, the technical foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow, including [EIP-615](./eip-615.md): Subroutines and Static Jumps for the EVM, [EIP-4750](./eip-4750.md): EOF Functions, [EIP-7979](./eip-7979.md): Call and Return Opcodes, [EIP-8013](./eip-8013.md): Static Relative Jumps, discussions around RISC-V migration and ZK verification infrastructure, and discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards which controlled a system of rods, gears and other machinery to implement arithmetic, storage (for 1,000 40-digits decimal numbers) and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1842: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabre, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming. The notes include her famous program for recursively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytic Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1945: Calls and Returns

In 1945 Alan Turing proposed his Automatic Computing Engine[^3] (ACE), where he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE supported calls directly with a stack of mercury-filled memory crystals holding return addresses. Turing's design was for a 32-bit RISC machine with a vacuum tube integer ALU, floating point microcode, 32 registers, a 1024-entry return stack, and 25K of RAM on a 1 MHz bus. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  Physical machines including the Burroughs 5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000 and Intelx86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program of a program, traversing each path only once.

### Control Flow

Among the most imporant reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with no more than one entry and one exit)
* _Edges_ represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* constructing ZK proof systems
* and many more

#### Dynamic Control Flow: The Problem

Dynamic jumps make dynamic control flow possible, make quadraticaly complex _CFGs_ possible, and can make static analysis of control difficult to impossible.  Dynamic jumps are not a problem for machines which run on physical hardware -- their instructions are designed for speed.  But they are uncommon in virtual machines whose code is the source for downstream tools.  This is because, as we will illustrate below, building and traversing a dynamic control flow graph can take quadratic space and time.  For this reason Java and Wasm do not support dynamic jumps and CLI carefully restricts them.

#### EVM: Dynamic Control Flow

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail, what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```

   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with at most one entry (a `JUMPDEST`) and one exit (a `JUMP`), and each arc is a transfer of control.  Arcs on the left are backwards branches, arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![_ Graphs_](../assets/eip-8173/control-flow.svg)

To be precise the number of arcs in these graphs is equal to the number of blocks minus one, squared.  That is, the number of possible paths of control flow, and thus the time needed to traverse them all, is quadratic in the size of the program.  At each block's exiting instruction, (except the `stop`) the analyzer cannot know _a priori_ where control will transfer.  Every block might jump to any other block, creating a fully-connected CFG with O(N²) possible paths. Traversing all paths to verify them requires O(N²) time, and this is not just a theoretical worst-case, as shown above.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores intermediate links on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

For Ethereum, this quadratic behavior is a _denial-of-service vulnerability_ for any online static analysis, including validating bytecode and AOT compilation at contract creation time and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable or even mathematically impossible. For a few examples, consider these abstracts from just a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static analysis renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In our experience, to avoid the problems of dynamic control flow VMs use static jumps, calls and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _Static control flow_ means that the destinations of every jump or call is determinable _a priori,_ before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups [^8]

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups, we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace, a sequence of state changes recording the value of registers, memory, stack, storage, etc. at each step. The trace is a complete record of the computation.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied.
* _Witnesses:_ The witness is the data the prover provides to prove that a computation is correct. For an execution trace, the witness includes the trace itself plus auxiliary data that helps prove the constraints are satisfied.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, while revealing Zero Knowledge of the witness itself.

A _ZK-Rollup sequencer or prover batches many transactions and constructs a ZK proof that all transactions executed correctly. The proof is then submi_tted to L1, where it is quickly verified. Key implications:

* _Trace size:_ With dynamic jumps, the prover may need to explore many paths before finding the correct one, making traces longer and less efficient.
* _Circuit complexity:_ A circuit covering dynamic jumps must account for all possible jump destinations at each dynamic jump. This significantly increases constraint count.
* _Proof generation time:_ Larger traces and circuits mean more computation for the prover, directly affecting latency and cost.
* _Hardware requirements:_  More complex circuits and longer traces demand more memory and computation, requiring specialized hardware for rollup operators.

Static control flow enables:

* _Predictable trace sizes_ (linear in execution length, not exponential in jump possibilities)
* _Simpler circuits_ (only actual execution paths need constraints)
* _Faster proof generation_
* _Lower hardware requirements for prover operators_

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but require fraud proofs to dispute invalid state roots. A fraud proof is a proof that a specific transaction executed incorrectly. Key implications of static analysis include:

* _Bytecode validation:_ Cleaner bytecode with static control flow enables easier validation of contract behavior.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction and prove correctness (or incorrectness). Static control flow makes this re-execution and proof more tractable.
* _Interactive verification:_ Some optimistic rollup designs use interactive verification games. Clear control flow simplifies the game protocol.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK Clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture which is seeing increasing use in the ZK community.  One currrent strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or reth to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose we have [EIP-7937](./eip-7937.md): EVM64 — 64-bit mode EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big of a problem.

## Specification

Four EIPs currently specify new EVM opcodes and semantics for static control flow:  [EIP-615: Subroutines and Static Jumps for the EVM](./eip-615.md), [EIP-4750: EOF - Functions](./eip-4750.md), [EIP-7979: Call and Return Opcodes for the EVM](./eip-7979.md), and [EIP-8013: Static relative jumps and calls for the EVM](./eip-8013.md).  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other other.  In particular, EIP-7979 can be used to implement every other EIP here.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static  control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have leveraged for decades.

## Security Considerations

This Informational proposal itself specificies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the EIPs it references, rather, it helps to motivate and specify them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabre",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of The Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```
[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.", 
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E"
        }
      ],
      "DOI": "comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "arXiv:2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "arXiv:2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a sound  Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "arXiv:2103.09113",
      "title": "EtherSolve: Computing an Accurate  Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "arXiv:2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain,  et al.  Doi: ",
          "given": "Akshita"
        }
      ],
      "DOI": "10.48550/Arxiv.2301.12695",
      "title": "Exploring The Efficacy Of Rollups’ A Comparative Study Of Optimistic And ZK-Rollups And Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://arxiv.org/10.48550/Arxiv.2301.12695"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3191 words)</summary>

````text
## Abstract

This Informational EIP provides foundational context for understanding control flow in the EVM. It covers the historical development of control flow mechanisms in computing, the technical foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow, including [EIP-615](./eip-615.md): Subroutines and Static Jumps for the EVM, [EIP-4750](./eip-4750.md): EOF Functions, [EIP-7979](./eip-7979.md): Call and Return Opcodes, [EIP-8013](./eip-8013.md): Static Relative Jumps, discussions around RISC-V migration and ZK verification infrastructure, and discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards which controlled a system of rods, gears and other machinery to implement arithmetic, storage (for 1,000 40-digits decimal numbers) and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1843: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabrea, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming, and published her translation in 1843. The notes include her famous program for iteratively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytic Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1946: Calls and Returns

In 1945 Alan Turing began designing his Automatic Computing Engine[^3] (ACE), completing the proposal in early 1946, where he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE used mercury delay-line memory, including a return stack holding return addresses. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  Physical machines including the Burroughs 5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000 and Intel x86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program, traversing each path only once.

### Control Flow

Among the most important reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with no more than one entry and one exit)
* _Edges_ represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* constructing ZK proof systems
* and many more

#### Dynamic Control Flow: The Problem

Dynamic jumps make dynamic control flow possible, make quadratically complex _CFGs_ possible, and can make static analysis of control difficult to impossible.  Dynamic jumps are not a problem for machines which run on physical hardware -- their instructions are designed for speed.  But they are uncommon in virtual machines whose code is the source for downstream tools.  This is because, as we will illustrate below, building and traversing a dynamic control flow graph can take quadratic space and time.  For this reason Java and Wasm do not support dynamic jumps and CLI carefully restricts them.

#### EVM: Dynamic Control Flow

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail, what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```

   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with at most one entry (a `JUMPDEST`) and one exit (a `JUMP`), and each arc is a transfer of control.  Arcs on the left are backwards branches, arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![_ Graphs_](../assets/eip-8173/control-flow.svg)

To be precise, the number of arcs in these graphs can be as large as the number of blocks times the number of blocks minus one — that is, O(N²) — since every block's dynamic jump might target any other block.  At each block's exiting instruction (except the `stop`) the analyzer cannot know _a priori_ where control will transfer, so every possible destination must be considered.  Building the complete CFG therefore requires O(N²) time and space, and this is not just a theoretical worst-case, as shown above.  Downstream analyses that must traverse all paths through the CFG — such as formal verification or ZK circuit construction — can be worse still, since the number of distinct paths through a fully-connected graph grows exponentially with the number of blocks.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores intermediate links on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

For Ethereum, this quadratic behavior is a _denial-of-service vulnerability_ for any online static analysis, including validating bytecode and AOT compilation at contract creation time and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable or even mathematically impossible. For a few examples, consider these abstracts from just a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static analysis renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In our experience, to avoid the problems of dynamic control flow VMs use static jumps, calls and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _Static control flow_ means that the destinations of every jump or call is determinable _a priori,_ before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups [^8]

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups, we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace: a concrete, step-by-step record of every opcode executed, with the values of the stack, memory, and storage at each step. The trace records what actually happened — including exactly where every jump went — so it is always linear in the number of steps executed.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied. Crucially, the circuit encodes the _rules_ for each opcode type (including the rule for JUMP), not the specific paths taken by any particular execution.
* _Witnesses:_ The witness is the private data the prover supplies to demonstrate that a specific execution was correct. It includes the execution trace itself plus auxiliary data. The public inputs are the pre- and post-state roots — what the state was before and after the transaction.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, without revealing the witness itself.

A ZK-Rollup sequencer or prover batches many transactions, generates a ZK proof that all transactions executed correctly, and submits that proof to L1, where it is quickly verified. The prover works from the _actual_ execution trace — it does not explore or enumerate possible paths. The jump destinations are already known because they were recorded when the transaction ran.

The benefits of static control flow for ZK proving are therefore not about path exploration, but about the efficiency of the code being proven and the tractability of the analyses that surround it:

* _Leaner bytecode:_ Static jumps, explicit subroutine calls, and better stack discipline (eliminating SWAP/DUP workarounds) produce significantly smaller and simpler bytecode. Because the prover must process every opcode in the execution trace, fewer opcodes means less work. Succint's Benchmarks of EOF (which introduces static control flow) against legacy EVM code show roughly 3x better cycle efficiency, 2.69x faster proof generation, and 50% smaller STARK proofs for equivalent computations.
* _Deployment-time validation:_ With static control flow, bytecode can be fully validated once at deployment in linear time — including stack safety and reachability — rather than requiring expensive per-execution checks or quadratic offline analysis. This is where the O(N²) CFG problem described above directly impacts ZK infrastructure: building and analyzing the CFG of legacy EVM code before constructing a circuit or a formal model requires quadratic work; static control flow reduces this to linear.
* _Parallelization:_ Static control flow makes it possible to partition execution into independent segments whose boundaries are provably non-interfering. This enables parallel proof generation across transactions and within a single transaction, significantly reducing end-to-end proving latency.
* _Faster proof generation and lower hardware requirements_ follow directly from the above: fewer opcodes to prove, cheaper analysis, and better parallelism reduce the compute and memory demands on rollup provers.

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but allow fraud proofs to dispute invalid state roots. A fraud proof re-executes the contested transaction and demonstrates that the submitted state root was wrong. Key implications of static control flow include:

* _Bytecode validation:_ Static control flow allows contract bytecode to be fully validated at deployment in linear time, establishing safety properties that can be relied on during dispute resolution.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction. The re-execution itself is deterministic regardless of control flow style, but static control flow makes the surrounding machinery — validators, formal checkers, and the interactive verification game — simpler to implement correctly and easier to reason about.
* _Interactive verification:_ Some optimistic rollup designs use multi-round interactive verification games that bisect execution to identify the disputed step. Clear, structured control flow makes the bisection protocol more tractable and reduces the risk of edge cases in the dispute game implementation.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK Clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture which is seeing increasing use in the ZK community.  One current strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or reth to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose we have [EIP-7937](./eip-7937.md): EVM64 — 64-bit mode EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big of a problem.

## Specification

Four EIPs currently specify new EVM opcodes and semantics for static control flow:  [EIP-615: Subroutines and Static Jumps for the EVM](./eip-615.md), [EIP-4750: EOF - Functions](./eip-4750.md), [EIP-7979: Call and Return Opcodes for the EVM](./eip-7979.md), and [EIP-8013: Static relative jumps and calls for the EVM](./eip-8013.md).  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other.  In particular, EIP-7979 can be used to implement every other EIP here.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static  control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers and auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have leveraged for decades.

## Security Considerations

This Informational proposal itself specifies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the EIPs it references, rather, it helps to motivate and specify them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabre",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of The Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.", 
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E"
        }
      ],
      "DOI": "comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "arXiv:2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "arXiv:2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a sound  Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "arXiv:2103.09113",
      "title": "EtherSolve: Computing an Accurate  Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "arXiv:2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain,  et al.  Doi: ",
          "given": "Akshita"
        }
      ],
      "DOI": "10.48550/Arxiv.2301.12695",
      "title": "Exploring The Efficacy Of Rollups’ A Comparative Study Of Optimistic And ZK-Rollups And Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://arxiv.org/10.48550/Arxiv.2301.12695"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 5 — revision_5</b> (3351 words)</summary>

````text
## Abstract

This Informational EIP provides foundational context for understanding control flow in the EVM. It covers the historical development of control flow mechanisms in computing, the technical foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow — past and current proposals for subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls — for discussions around RISC-V migration and ZK verification infrastructure, and for discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards that controlled a system of rods, gears, and other machinery to implement arithmetic, storage (for 1,000 40-digit decimal numbers), and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1843: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabrea, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming, and published her translation in 1843. The notes include her famous program for iteratively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytical Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1946: Calls and Returns

In 1945 Alan Turing began designing his Automatic Computing Engine[^3] (ACE), completing the proposal in early 1946, in which he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE used mercury delay-line memory, including a return stack holding return addresses. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames, register windows … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  physical machines including the Burroughs B5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000, and Intel x86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program, traversing each path only once.

### Control Flow

Among the most important reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with exactly one entry and one exit)
* _Edges_ represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* constructing ZK proof systems
* and many more

#### Dynamic Control Flow: The Problem

Dynamic jumps make dynamic control flow possible, make quadratically complex CFGs possible, and can make static analysis of control difficult to impossible.  Dynamic jumps are not a problem for machines that run on physical hardware — their instructions are designed for speed.  But they are uncommon in virtual machines whose code is the source for downstream tools.  This is because, as we will illustrate below, building and traversing a dynamic control flow graph can take quadratic space and time.  For this reason Java and Wasm do not support dynamic jumps and CLI carefully restricts them.

#### EVM: Dynamic Control Flow

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail; what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```

   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with one entry (a `JUMPDEST`) and one exit (a `JUMP`, or the final `stop`), and each arc is a transfer of control.  Arcs on the left are backwards branches; arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![Control flow graphs](../assets/eip-8173/control-flow.svg)

To be precise, the number of arcs in these graphs can be as large as the number of blocks times one less than the number of blocks — that is, O(N²) — since every block's dynamic jump might target any block.  At each block's exiting instruction (except the `stop`) the analyzer cannot know _a priori_ where control will transfer, so every possible destination must be considered.  Building the complete CFG therefore requires O(N²) time and space, and this is not just a theoretical worst case, as shown above.  Downstream analyses that must traverse all paths through the CFG — such as formal verification or ZK circuit construction — can be worse still, since the number of distinct paths through a fully connected graph grows factorially with the number of blocks.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores return addresses on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

The cost is easiest to see in the shape Solidity emits for internal function calls.  The EVM has no call instruction, so the compiler builds one: the return address is pushed as ordinary data, and the return is a jump.  And the helper is worth having — deployed bytes cost gas, and contracts are capped at 24576 of them, so shared code pays.  Here a helper squares a number for two callers:

```
CALL_A: push RTN_A      ; return address, as ordinary data
        push 2
        push SQUARE
        jump
RTN_A:  jumpdest
        ...
CALL_B: push RTN_B
        push 3
        push SQUARE
        jump
RTN_B:  jumpdest
        ...
SQUARE: jumpdest
        dup1
        mul
        swap1
        jump            ; return — but to where?
```

At run time the final `jump` goes wherever the pushed address says.  An analyzer must answer before the code runs, and the address is data — so it must follow both returns.  After one call it is in two places at once; after two calls, four; every call doubles the count.  Twenty calls is a million paths, one of them real.  To rule out the rest, the analyzer must track what the code keeps on the stack — the very bookkeeping an explicit call would have done for it.

With explicit calls and returns there is nothing to answer: every return goes back to its call.  Twenty calls, one path.

For Ethereum, these behaviors are a _denial-of-service vulnerability_ for any online static analysis, including bytecode validation and AOT compilation at contract creation time, and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable, or even mathematically impossible. For examples, consider these abstracts from a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static control flow renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In my experience, to avoid the problems of dynamic control flow, VMs use static jumps, calls, and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _static control flow_ means that the destination of every jump or call is determinable _a priori_, before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups[^8], we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace: a concrete, step-by-step record of every opcode executed, with the values of the stack, memory, and storage at each step. The trace records what actually happened — including exactly where every jump went — so it is always linear in the number of steps executed.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied. Crucially, the circuit encodes the _rules_ for each opcode type (including the rule for JUMP), not the specific paths taken by any particular execution.
* _Witnesses:_ The witness is the private data the prover supplies to demonstrate that a specific execution was correct. It includes the execution trace itself plus auxiliary data. The public inputs are the pre- and post-state roots — what the state was before and after the transaction.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, without revealing the witness itself.

A ZK-Rollup sequencer or prover batches many transactions, generates a ZK proof that all transactions executed correctly, and submits that proof to L1, where it is quickly verified. The prover works from the _actual_ execution trace — it does not explore or enumerate possible paths. The jump destinations are already known because they were recorded when the transaction ran.

The benefits of static control flow for ZK proving are therefore not about path exploration, but about the efficiency of the code being proven and the tractability of the analyses that surround it:

* _Leaner bytecode:_ Static jumps, explicit subroutine calls, and better stack discipline (eliminating SWAP/DUP workarounds) produce significantly smaller and simpler bytecode. Because the prover must process every opcode in the execution trace, fewer opcodes mean less work.
* _Deployment-time validation:_ With static control flow, bytecode can be fully validated once at deployment in linear time — including stack underflow, static stack heights, and reachability — rather than requiring expensive per-execution checks or quadratic offline analysis. This is where the O(N²) CFG problem described above directly impacts ZK infrastructure: building and analyzing the CFG of legacy EVM code before constructing a circuit or a formal model requires quadratic work; static control flow reduces this to linear.
* _Faster proof generation and lower hardware requirements_ follow directly from the above: fewer opcodes to prove and cheaper analysis reduce the compute and memory demands on rollup provers.

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but allow fraud proofs to dispute invalid state roots. A fraud proof re-executes the contested transaction and demonstrates that the submitted state root was wrong. Key implications of static control flow include:

* _Bytecode validation:_ Static control flow allows contract bytecode to be fully validated at deployment in linear time, establishing safety properties that can be relied on during dispute resolution.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction. The re-execution itself is deterministic regardless of control flow style, but static control flow makes the surrounding machinery — validators, formal checkers, and the interactive verification game — simpler to implement correctly and easier to reason about.
* _Interactive verification:_ Some optimistic rollup designs use multi-round interactive verification games that bisect execution to identify the disputed step. Clear, structured control flow makes the bisection protocol more tractable and reduces the risk of edge cases in the dispute game implementation.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture that is seeing increasing use in the ZK community.  One current strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or revm to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose there are current proposals for 64-bit EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big a problem.

## Specification

Several EIPs, past and current, specify new EVM opcodes and semantics for static control flow: subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls.  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other.  In particular, the simplest of them — three call and return opcodes — can be used to implement all of the others.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers and auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have leveraged for decades.

## Security Considerations

This Informational proposal itself specifies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the proposals it describes; rather, it helps to motivate and contextualize them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabrea",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of the Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "10.1093/mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.",
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E."
        }
      ],
      "DOI": "10.1093/comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "10.48550/arXiv.2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "10.48550/arXiv.2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a Sound Control Flow Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "10.48550/arXiv.2103.09113",
      "title": "EtherSolve: Computing an Accurate Control Flow Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "10.48550/arXiv.2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain",
          "given": "Akshita"
        }
      ],
      "DOI": "10.30696/JAC.XVIII.1.2024.297-315",
      "title": "Exploring the Efficacy of Rollups: A Comparative Study of Optimistic and ZK-Rollups and Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.30696/JAC.XVIII.1.2024.297-315"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 6 — revision_6</b> (3704 words)</summary>

````text
## Abstract

This Informational EIP provides background for understanding control flow in the EVM: the history of control flow in computing, the foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow — past and current proposals for subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls — for discussions around RISC-V migration and ZK verification infrastructure, and for discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards that controlled a system of rods, gears, and other machinery to implement arithmetic, storage (for 1,000 40-digit decimal numbers), and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1843: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabrea, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming, and published her translation in 1843. The notes include her famous program for iteratively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytical Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1946: Calls and Returns

In 1945 Alan Turing began designing his Automatic Computing Engine[^3] (ACE), completing the proposal in early 1946, in which he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE used mercury delay-line memory, including a return stack holding return addresses. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  physical machines including the Burroughs B5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000, and Intel x86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

A few connections show the range.  The CDC 7600 had no stack at all: its return jump planted the return in the code itself — self-modifying code, Wheeler's design for the EDSAC.  A call wrote a branch back to the caller into the subroutine's first word, then jumped to its second; the subroutine returned by jumping to its own first word and executing the planted branch.  It was fast, and it made recursion and shared code impossible — each subroutine could hold only one return at a time.  The IBM 360 kept the return address in a link register, and returning was a branch through it.  The PDP-11, VAX, 68000, and x86 push return addresses onto the same stack as data — the stack-frame design that C made universal, and that stack-smashing exploits have abused ever since, precisely because return addresses live where data can overwrite them.  The Burroughs B5000, built for Algol, gave its stack frames hardware protection.  And Forth, like Turing's ACE, keeps a separate return stack, sealed off from data — the design adopted by the proposals discussed below.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program, traversing each path only once.

### Control Flow

Among the most important reasons to traverse the control flow of a program is to extract the control flow graph.  The EVM makes this quadratically difficult due to its dynamic control flow.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a directed graph representation of a program where:

* _Nodes_ represent blocks of instructions (sequences with exactly one entry and one exit)
* _Edges_, or _arcs_, represent possible transfers of control between blocks

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* and many more

#### Dynamic Control Flow

Dynamic jumps make dynamic control flow possible.  They also make quadratically complex control flow possible, and can make static analysis of control difficult to impossible.  Physical machines run on dynamic jumps: every x86 return pops an address off the stack and jumps to it, and every IBM 360 return is a branch through a register.  Hardware only executes — it never analyzes — so its instructions are designed for speed, not post-hoc analysis, which is why recovering the control flow of machine code remains hard to this day.  Virtual machines are different: their code is validated when loaded, and is often the source for JITs and other downstream tools — and as we will show below, building and traversing a dynamic control flow graph can take quadratic space and time.  So the JVM's one restricted dynamic jump — jsr/ret, for implementing finally — so complicated its verifier that it was removed, Wasm never had one, and CLI carefully restricts theirs.

#### EVM: Dynamic Jumps and Control Flow Graphs

For an example, consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail; what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
                                                          ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each block of instructions in a graph is a sequence from the above programs with one entry (a `JUMPDEST`) and one exit (a `JUMP`, or the final `stop`), and each arc is a transfer of control.  Arcs on the left are backwards branches; arcs on the right are forwards branches.  See how the tangle of arcs goes up fast, faster than the programs get longer.

![Control flow graphs](../assets/eip-8173/control-flow.svg)

To be precise, the number of arcs in these graphs can be as large as the number of blocks times one less than the number of blocks — that is, O(N²) — since every block's dynamic jump might target any block.  At each block's exiting instruction (except the `stop`) the analyzer cannot know _a priori_ where control will transfer, so every possible destination must be considered.  Building the complete CFG therefore requires O(N²) time and space, and this is not just a theoretical worst case, as shown above.  Downstream analyses that must traverse all paths through the CFG — such as formal verification — can be worse still, since the number of distinct paths through a fully connected graph grows factorially with the number of blocks.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

#### EVM: Calls, Returns, and Symbolic Execution

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its argument from the stack and stores return addresses on the stack. So control flow _must be_ dynamic, which creates the quadratic CFG problems explained above.

Tools that must know what code does execute it _symbolically_ — walking the code, computing facts in place of values.

Consider a tool that computes how much gas a call uses.  Here is code a compiler might emit for internal function calls — in this case a helper squaring a number for two callers, with the gas in the comments:

```
CALL_A: push RTN_A     ; 3   return address, as ordinary data
        push 2         ; 3
        push SQUARE    ; 3
        jump           ; 8
RTN_A:  jumpdest       ; 1
        ...
CALL_B: push RTN_B     ; 3
        push 3         ; 3
        push SQUARE    ; 3
        jump           ; 8
RTN_B:  jumpdest       ; 1
        ...
SQUARE: jumpdest       ; 1
        dup1           ; 3
        mul            ; 5
        swap1          ; 3
        jump           ; 8   return — but to where?
```

The algorithm is plain:

```
   for each instruction in code
      cost = cost + gas(instruction)
```

Accumulating the costs of each instruction is easy.  Executed on the code above, from CALL_A: 17 gas through the call, 20 gas through SQUARE, 1 gas to land at RTN_A — a call costs 38 gas.  The _for each instruction_ is not easy.  _Falling through_ an instruction is just an increment of the instruction pointer, but _following a jump_ requires an address on the stack.  We knew the final `jump` lands at RTN_A only because we followed the pushed address through the `dup` and `swap` — in general the address on the stack can be any destination.

So this gas estimator must walk every return the jump might reach, and every unresolved return doubles the walks: twenty calls is a million walks — exponential in the number of calls.  With explicit calls and returns there is nothing to follow: every return goes back to its call.  One walk, one number — 38.  Twenty calls, one path.

Nothing here is special to gas: every algorithm that walks the paths of any program computing facts — proving safety, finding bugs, decompiling, translating — splits at the same jumps and pays the same exponential cost, or worse.

For Ethereum, these behaviors are a _denial-of-service vulnerability_ for any online static analysis, including bytecode validation and AOT compilation at contract creation time, and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable, or even mathematically impossible. For further examples, consider these abstracts from a few recent papers on the problem.  The last paper resorts to neural nets to disassemble (most) Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static control flow renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In my experience, to avoid the problems of dynamic control flow, VMs use static jumps, calls, and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _static control flow_ means that the destination of every jump or call is determinable _a priori_, before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups[^8], we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace: a concrete, step-by-step record of every opcode executed, with the values of the stack, memory, and storage at each step. The trace records what actually happened — including exactly where every jump went — so it is always linear in the number of steps executed.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied. Crucially, the circuit encodes the _rules_ for each opcode type (including the rule for JUMP), not the specific paths taken by any particular execution.
* _Witnesses:_ The witness is the private data the prover supplies to demonstrate that a specific execution was correct. It includes the execution trace itself plus auxiliary data. The public inputs are the pre- and post-state roots — what the state was before and after the transaction.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, without revealing the witness itself.

A ZK-Rollup sequencer or prover batches many transactions, generates a ZK proof that all transactions executed correctly, and submits that proof to L1, where it is quickly verified. The prover works from the _actual_ execution trace — it does not explore or enumerate possible paths. The jump destinations are already known because they were recorded when the transaction ran.

The benefits of static control flow for ZK proving are therefore not about path exploration, but about the efficiency of the code being proven and the tractability of the analyses that surround it:

* _Leaner bytecode:_ Static jumps, explicit subroutine calls, and better stack discipline (eliminating SWAP/DUP workarounds) produce significantly smaller and simpler bytecode. Because the prover must process every opcode in the execution trace, fewer opcodes mean less work.
* _Deployment-time validation:_ With static control flow, bytecode can be fully validated once at deployment in linear time — including stack underflow, static stack heights, and reachability — rather than requiring expensive per-execution checks or quadratic offline analysis. This is where the O(N²) CFG problem described above directly impacts ZK infrastructure: building and analyzing the CFG of legacy EVM code before constructing a circuit or a formal model requires quadratic work; static control flow reduces this to linear.
* _Faster proof generation and lower hardware requirements_ follow directly from the above: fewer opcodes to prove and cheaper analysis reduce the compute and memory demands on rollup provers.

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but allow fraud proofs to dispute invalid state roots. A fraud proof re-executes the contested transaction and demonstrates that the submitted state root was wrong. Key implications of static control flow include:

* _Bytecode validation:_ Static control flow allows contract bytecode to be fully validated at deployment in linear time, establishing safety properties that can be relied on during dispute resolution.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction. The re-execution itself is deterministic regardless of control flow style, but static control flow makes the surrounding machinery — validators, formal checkers, and the interactive verification game — simpler to implement correctly and easier to reason about.
* _Interactive verification:_ Some optimistic rollup designs use multi-round interactive verification games that bisect execution to identify the disputed step. Clear, structured control flow makes the bisection protocol more tractable and reduces the risk of edge cases in the dispute game implementation.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture that is seeing increasing use in the ZK community.  One current strategy for creating a ZK-EVM is to compile an EVM interpreter like evmone or revm to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose there are current proposals for 64-bit EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big a problem.

## Specification

Several EIPs, past and current, specify new EVM opcodes and semantics for static control flow: subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls.  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other.  In particular, the simplest of them — three call and return opcodes — can be used to implement all of the others.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers and auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have relied on for decades.

## Security Considerations

This Informational proposal itself specifies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the proposals it describes; rather, it helps to motivate and contextualize them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabrea",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of the Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "10.1093/mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.",
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E."
        }
      ],
      "DOI": "10.1093/comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "10.48550/arXiv.2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "10.48550/arXiv.2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a Sound Control Flow Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "10.48550/arXiv.2103.09113",
      "title": "EtherSolve: Computing an Accurate Control Flow Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "10.48550/arXiv.2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain",
          "given": "Akshita"
        }
      ],
      "DOI": "10.30696/JAC.XVIII.1.2024.297-315",
      "title": "Exploring the Efficacy of Rollups: A Comparative Study of Optimistic and ZK-Rollups and Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.30696/JAC.XVIII.1.2024.297-315"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 7 — revision_7</b> (4033 words)</summary>

````text
## Abstract

This Informational EIP provides background for understanding control flow in the EVM: the history of control flow in computing, the foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow — past and current proposals for subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls — for discussions around RISC-V migration and ZK verification infrastructure, and for discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards that controlled a system of rods, gears, and other machinery to implement arithmetic, storage (for 1,000 40-digit decimal numbers), and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1843: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabrea, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming, and published her translation in 1843. The notes include her famous program for iteratively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytical Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]  

#### Turing, 1946: Calls and Returns

In 1945 Alan Turing began designing his Automatic Computing Engine[^3] (ACE), completing the proposal in early 1946, in which he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE used mercury delay-line memory, including a return stack holding return addresses. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  physical machines including the Burroughs B5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000, and Intel x86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

A few connections show the range.  The CDC 7600 had no stack at all: its return jump planted the return in the code itself — self-modifying code, Wheeler's design for the EDSAC.  A call wrote a branch back to the caller into the subroutine's first word, then jumped to its second; the subroutine returned by jumping to its own first word and executing the planted branch.  It was fast, and it made recursion and shared code impossible — each subroutine could hold only one return at a time.  The IBM 360 kept the return address in a link register, and returning was a branch through it.  The PDP-11, VAX, 68000, and x86 push return addresses onto the same stack as data — the stack-frame design that C made universal, and that stack-smashing exploits have abused ever since, precisely because return addresses live where data can overwrite them.  The Burroughs B5000, built for Algol, gave its stack frames hardware protection.  And Forth, like Turing's ACE, keeps a separate return stack, sealed off from data — the design adopted by the proposals discussed below.

Especially relevant to the EVM's design are the Java, WebAssembly (Wasm), and CLI (.NET) VMs. They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program, traversing each edge only once.

### Control Flow

Tools that must know what code does have to follow where control can go: walk the code, taking every jump.  How much such a walk costs — and whether it is possible at all — depends on the code's control flow.  The EVM makes it cost more than it should.

#### Control Flow Graphs

A _control flow graph (CFG)_ is a map of where control can go in a program:

* _Nodes_ are the _blocks_ of code — runs of instructions with one entry and one exit, executed together or not at all
* _Edges_ are the possible moves between blocks: each jump to its destinations, each fall-through to the next block

A _path_ is one possible route through the code from the start: which blocks, in which order.  Every execution follows some path; a program with branches has many.

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* and many more

The graph need not be drawn to be used: many tools simply walk the code, following the edges in place.  Drawing the CFG is just such a walk that takes notes.

#### Dynamic Control Flow

Dynamic jumps make dynamic control flow possible.  They also make quadratically complex control flow possible, and can make static analysis of control difficult to impossible.  Physical machines run on dynamic jumps: every x86 return pops an address off the stack and jumps to it, and every IBM 360 return is a branch through a register.  Hardware only executes — it never analyzes — so its instructions are designed for speed, not post-hoc analysis, which is why recovering the control flow of machine code remains hard to this day.  Virtual machines are different: their code is validated when loaded, and is often the source for JITs and other downstream tools — and as we will show below, building and traversing a dynamic control flow graph can take quadratic space and time.  So Java and Wasm do not support dynamic jumps, and CLI carefully restricts theirs.

#### EVM: Calls, Returns, and the Cost of Walking Code

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns. Instead, they _must_ be synthesized using the dynamic `JUMP` instruction, which takes its destination from the stack — and stores return addresses on the stack.  Here is a complete program a compiler might emit this way, with the gas in the comments: a squaring routine, called from two places, computing 2² + 3².

```
        push RTN_A     ; 3   return address, as ordinary data
        push 2         ; 3
        push SQUARE    ; 3
        jump           ; 8   call SQUARE(2)
RTN_A:  jumpdest       ; 1   back, with 4 on the stack
        push RTN_B     ; 3
        push 3         ; 3
        push SQUARE    ; 3
        jump           ; 8   call SQUARE(3)
RTN_B:  jumpdest       ; 1   back, with 9 on the stack
        add            ; 3
        stop           ; 0   13 on the stack
SQUARE: jumpdest       ; 1
        dup1           ; 3
        mul            ; 5
        swap1          ; 3
        jump           ; 8   return — but to where?
```

Take a pencil and run it.  The values resolve every jump for you: the first call enters SQUARE with 2, squares it, and the `swap1` brings RTN_A to the top for the final `jump` home; the second call brings RTN_B.  The program leaves 13 on the stack and consumes 79 gas — 38 for each call (17 through the call, 20 through SQUARE, 1 to land) and 3 for the `add`.  One walk, and both answers: what it computes, and what it costs.

Now consider a tool that must answer "what does a call to SQUARE cost?" for _every_ program, not just this one.  It cannot run the code — it has no inputs, and running is what it is trying to price.  So it walks the code the way you just did, but computing facts in place of values: this slot holds _some_ argument; that slot holds _the constant RTN_A_.  Walking code and computing facts in place of values is called _symbolic execution_, and most every tool that must know what code does — analyzers, optimizers, decompilers, provers — does some form of it.

On this program the walk goes through, because the return addresses are pushed constants that can be followed through the `dup1` and `swap1`.  But in general the address on the stack can be any value from anywhere — computed, stored, reloaded — and following it is hopeless.  Then the walker standing on SQUARE's final `jump` cannot tell whose call this walk belongs to: the destination might be RTN_A or RTN_B, and it must walk _both_ returns.  Each place that shares the routine doubles the walks.  Twenty calls is a million walks — what the literature calls a _path explosion_.  Faced with that, honest tools report what their users know too well: _cost unknown_.

With explicit calls and returns there is nothing to follow: every return goes back to its call.  One walk, one number.  Twenty calls, one path.

Nothing here is special to gas: every algorithm that walks the paths of any program computing facts — proving safety, finding bugs, decompiling, translating — splits at the same jumps and pays the same exponential cost, or worse.

#### EVM: Any Jump, Anywhere

Worse is available.  The walker above at least had candidates — two labeled returns to try.  When the destination is computed, the walker has no candidates at all, and must assume what the machine allows: _any_ jump may go to _any_ destination in the code.  Consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  It's not important that at runtime `gas` isn't random or that the `jump` will most often fail; what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each node is a block from the programs above — one entry (a `jumpdest`), one exit (a `jump`, or the final `stop`) — and each edge is a move the machine might make.  Edges on the left are backwards branches; edges on the right are forwards branches.  See how the tangle of edges goes up fast, faster than the programs get longer.

![Control flow graphs](../assets/eip-8173/control-flow.svg)

Merely _drawing_ this graph costs the square of the code size: every block's `jump` might reach every block, so the edges number the blocks times one less than the blocks — O(N²) — and any tool that must consider where jumps can go pays that price whether it draws the graph or not.  _Walking_ the graph costs far more.  A walk that never revisits a block chooses among all the remaining blocks at every step, so the routes multiply by a growing factor each time:

| blocks | edges to draw | walks to make |
|-------:|--------------:|--------------:|
|      3 |             6 |             5 |
|      4 |            12 |            16 |
|      5 |            20 |            65 |
|     10 |            90 |       986,410 |
|     20 |           380 | ≈ 3 × 10¹⁷    |

Forking between two known returns doubles the walks — exponential.  Forking among everything multiplies them by a number that grows with the code — factorial, which outruns every exponential.  The edge count is what building or validating pays, and with dynamic jumps it is already quadratic; the walk count is what every deeper analysis pays — formal verification must consider the paths — and it is astronomical before the code is twenty blocks long.

In Java, Wasm, and CLI it is simply impossible to have programs like these.

For Ethereum, these behaviors are a _denial-of-service vulnerability_ for any online static analysis, including bytecode validation and AOT compilation at contract creation time, and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable, or even mathematically impossible. For further examples, consider these abstracts from a few recent papers on the problem.  The last paper brings neural networks to bear, and still disassembles only most Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static control flow renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In my experience, to avoid the problems of dynamic control flow, VMs use static jumps, calls, and returns.

### Static Control Flow and Ethereum Scaling

As laid out above, _static control flow_ means that the destination of every jump or call is determinable _a priori_, before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups[^8], we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace: a concrete, step-by-step record of every opcode executed, with the values of the stack, memory, and storage at each step. The trace records what actually happened — including exactly where every jump went — so it is always linear in the number of steps executed.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied. Crucially, the circuit encodes the _rules_ for each opcode type (including the rule for JUMP), not the specific paths taken by any particular execution.
* _Witnesses:_ The witness is the private data the prover supplies to demonstrate that a specific execution was correct. It includes the execution trace itself plus auxiliary data. The public inputs are the pre- and post-state roots — what the state was before and after the transaction.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, without revealing the witness itself.

A ZK-Rollup sequencer or prover batches many transactions, generates a ZK proof that all transactions executed correctly, and submits that proof to L1, where it is quickly verified. The prover works from the _actual_ execution trace — it does not explore or enumerate possible paths. The jump destinations are already known because they were recorded when the transaction ran.

The benefits of static control flow for ZK proving are therefore not about path exploration, but about the efficiency of the code being proven and the tractability of the analyses that surround it:

* _Leaner bytecode:_ Static jumps, explicit subroutine calls, and better stack discipline (eliminating SWAP/DUP workarounds) produce significantly smaller and simpler bytecode. Because the prover must process every opcode in the execution trace, fewer opcodes mean less work.
* _Deployment-time validation:_ With static control flow, bytecode can be fully validated once at deployment in linear time — including stack underflow, static stack depths, and reachability — rather than requiring expensive per-execution checks or quadratic offline analysis. This is where the O(N²) CFG problem described above directly impacts ZK infrastructure: building and analyzing the CFG of legacy EVM code before constructing a circuit or a formal model requires quadratic work; static control flow reduces this to linear.
* _Faster proof generation and lower hardware requirements_ follow directly from the above: fewer opcodes to prove and cheaper analysis reduce the compute and memory demands on rollup provers.

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but allow fraud proofs to dispute invalid state roots. A fraud proof re-executes the contested transaction and demonstrates that the submitted state root was wrong. Key implications of static control flow include:

* _Bytecode validation:_ Static control flow allows contract bytecode to be fully validated at deployment in linear time, establishing safety properties that can be relied on during dispute resolution.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction. The re-execution itself is deterministic regardless of control flow style, but static control flow makes the surrounding machinery — validators, formal checkers, and the interactive verification game — simpler to implement correctly and easier to reason about.
* _Interactive verification:_ Some optimistic rollup designs use multi-round interactive verification games that bisect execution to identify the disputed step. Clear, structured control flow makes the bisection protocol more tractable and reduces the risk of edge cases in the dispute game implementation.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK clients, whether on L1, L2, or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture that is seeing increasing use in the ZK community.  One current strategy for creating a ZK-EVM is to compile an EVM interpreter like revm to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose there are current proposals for 64-bit EVM opcodes.  It's also the case that the prover has the actual trace, and can tell how many bits are actually in use at each step of the computation, so the 256-bit registers might not be that big a problem.

## Specification

Several EIPs, past and current, specify new EVM opcodes and semantics for static control flow: subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls.  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other.  In particular, the simplest of them — three call and return opcodes — can be used to implement all of the others.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers and auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have relied on for decades.

## Security Considerations

This Informational proposal itself specifies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the proposals it describes; rather, it helps to motivate and contextualize them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabrea",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of the Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "10.1093/mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.",
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E."
        }
      ],
      "DOI": "10.1093/comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "10.48550/arXiv.2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "10.48550/arXiv.2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a Sound Control Flow Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "10.48550/arXiv.2103.09113",
      "title": "EtherSolve: Computing an Accurate Control Flow Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "10.48550/arXiv.2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain",
          "given": "Akshita"
        }
      ],
      "DOI": "10.30696/JAC.XVIII.1.2024.297-315",
      "title": "Exploring the Efficacy of Rollups: A Comparative Study of Optimistic and ZK-Rollups and Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.30696/JAC.XVIII.1.2024.297-315"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 8 — final</b> (3642 words)</summary>

````text
## Abstract

This Informational EIP provides background for understanding control flow in the Ethereum Virtual Machine (EVM): the history of control flow in computing, the foundations of control flow analysis, and the impact of static control flow on Ethereum's scaling roadmap.

This document serves as background material for proposals for static control flow — past and current proposals for subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls — for discussions around RISC-V migration and zero-knowledge (ZK) verification infrastructure, and for discussions still to come.

## Motivation

### Historical Context

#### Babbage 1833: Jumps and Conditional Jumps

In 1833 Charles Babbage began the design of the Analytical Engine: a steam-powered, mechanical, Turing-complete computer. Programs were to be encoded on punched cards that controlled a system of rods, gears, and other machinery to implement arithmetic, storage (for 1,000 40-digit decimal numbers), and conditional jumps.  Jumps were supported by cards that shuffled the card deck forwards or backwards a fixed number of cards.

#### Lovelace 1843: Computer Science and Machine Intelligence

The first published description of the Analytical Engine was in French, by L. F. Menabrea, 1842[^1]. The English translator, Ada Augusta, Countess of Lovelace, made extensive notes on the science of computer programming, and published her translation in 1843. The notes include her famous program for iteratively computing Bernoulli numbers — arguably the world's first complete computer program — which used conditional jumps to implement the required nested loops.

In Lady Lovelace's notes we also find her prescient recognition of the Analytical Engine's power — "In enabling mechanism to combine together general symbols in successions of unlimited variety and extent, a uniting link is established between the operations of matter and the abstract mental processes of the most abstract branch of mathematical science."[^1]  Here also we find what Alan Turing later called "Lady Lovelace's Objection"[^2] to the possibility of machine intelligence — "It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths. Its province is to assist us in making available what we are already acquainted with."[^1]

#### Turing, 1946: Calls and Returns

In 1945 Alan Turing began designing his Automatic Computing Engine[^3] (ACE), completing the proposal in early 1946, in which he introduced the concept of calls and returns: _"To start on a subsidiary operation we need only make a note of where we left off the major operation and then apply the first instruction of the subsidiary. When the subsidiary is over we look up the note and continue with the major operation."_

The ACE used mercury delay-line memory, including a return stack holding return addresses. The smaller Pilot ACE was for a time the world's fastest computer.

#### Industry Practice: 1945 to present

Call and return facilities of various names … subroutines, procedures, functions, methods … and levels of complexity … link registers, return stacks, stack frames … have proven their worth across a long line of important machines over the last 80 years, including most of the machines I have programmed or implemented:  physical machines including the Burroughs B5000, CDC 7600, IBM 360, PDP-11, VAX, Motorola 68000, and Intel x86, and virtual machines including those for Scheme, Forth, Pascal, Java, and WebAssembly.

A few connections show the range.  The CDC 7600 had no stack at all: its return jump planted the return in the code itself — self-modifying code, Wheeler's design for the EDSAC.  A call wrote a branch back to the caller into the subroutine's first word, then jumped to its second; the subroutine returned by jumping to its own first word and executing the planted branch.  It was fast, and it made recursion and shared code impossible — each subroutine could hold only one return at a time.  The IBM 360 kept the return address in a link register, and returning was a branch through it.  The PDP-11, VAX, 68000, and x86 push return addresses onto the same stack as data — the stack-frame design that C made universal, and that stack-smashing exploits have abused ever since, precisely because return addresses live where data can overwrite them.  The Burroughs B5000, built for Algol, gave its stack frames hardware protection.  And Forth, like Turing's ACE, keeps a separate return stack, sealed off from data — the design adopted by the proposals discussed below.

Especially relevant to the EVM's design are the Java Virtual Machine (JVM), WebAssembly (Wasm), and .NET's Common Language Runtime (CLR). They share crucial common properties:

* they are represented with portable bytecode
* that can be directly interpreted
* with static control flow
* that can be validated before runtime
* and can be compiled to machine code at runtime
* in _linear time_.

The static control flow that supports linear-time compilers also supports any other code that needs to traverse the control flow of a program, traversing each edge only once.

### Control Flow

Tools that must know what code does have to follow where control can go: traverse the code, taking every jump.  How much such a traversal costs — and whether it is possible at all — depends on the code's control flow.  The EVM makes it cost more than it should.

#### Control Flow Graphs

The map of where control can go in a program is its _control flow graph (CFG)_:

* _Nodes_ are the _blocks_ of code: runs of instructions with one entry and one exit
* _Edges_ are the possible moves between blocks: each jump to its destinations, each fall-through to the next block

A jump whose destination is known before execution is _static_; a jump that takes its destination from the stack at runtime is _dynamic_.  Code has _static control flow_ when every jump is static.  A _path_ is one route through the graph from the start; every execution follows some path.

A _complete and sound CFG_ represents all and only the possible paths of program execution and is a fundamental starting point for many downstream tasks, including many static analyses:

* validating bytecode before execution
* translating bytecode to other representations (virtual register code, machine code)
* automated formal security analysis
* and many more

#### Dynamic Control Flow

Dynamic jumps make dynamic control flow possible.  They also make quadratically complex control flow possible, and can make static analysis of control difficult to impossible.  Physical machines run on dynamic jumps: every x86 return pops an address off the stack and jumps to it, and every IBM 360 return is a branch through a register.  Hardware only executes — it never analyzes — so its instructions are designed for speed, not post-hoc analysis, which is why recovering the control flow of machine code remains hard to this day.  Virtual machines are different: their code is validated when loaded, and is often the source for just-in-time compilers (JITs) and other downstream tools — and as we will show below, building and traversing a dynamic control flow graph can take quadratic space and time.  So the JVM and Wasm do not support dynamic jumps, and the CLR carefully restricts theirs.

#### EVM: Calls and Returns

The Ethereum Virtual Machine does _not_ provide explicit facilities for calls and returns.  Instead, compilers _must_ synthesize them with the dynamic `JUMP`: the return address is pushed as ordinary data, carried on the stack, and jumped to when the routine is done.  So dynamic jumps are not exotic — every internal function call in every deployed contract is one, and its destination is data.  A tool that must know where a return goes — to price it, to prove it safe, to decompile it — walks the code computing facts in place of values, _symbolic execution_, and must walk every return point the jump might reach.  Every routine shared by two callers doubles the walks: twenty calls is a million — what the literature calls a _path explosion_.  With explicit calls and returns there is nothing to guess: every return goes back to its call.  One walk, one answer.  A mechanical demonstration — a walker counting its walks over the same programs written both ways — accompanies this EIP in its [assets](../assets/eip-8173/walk-count/).

#### EVM: Any Jump, Anywhere

A return at least has candidates — a compiler's labels are good guesses.  When the destination is computed there are no candidates at all, and the walker must assume what the machine allows: _any_ jump may go to _any_ destination in the code.  Consider these EVM programs and the easily generated series of longer programs like them ... the really long ones make for nice exploits.  `gas` pushes the gas remaining; it's not important that at runtime this isn't random or that the `jump` will most often fail; what matters is that because the jump destination is taken from the stack it is impossible to know _a priori_ where the jumps go, so every path must be explored.

```
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   gas                gas               gas               ...
   jump               jump              jump              ...
   jumpdest           jumpdest          jumpdest          ...
   stop               gas               gas               ...
                      jump              jump              ...
                      jumpdest          jumpdest          ...
                      stop              gas               ...
                                        jump              ...
                                        jumpdest          ...
                                        stop              ...
                                                          ...
```

The control flow graphs for these programs make the problem clear.  Each node is a block from the programs above — one entry (a `jumpdest`), one exit (a `jump`, or the final `stop`) — and each edge is a move the machine might make.  Edges on the left are backwards branches; edges on the right are forwards branches.  See how the tangle of edges goes up fast, faster than the programs get longer.

![Control flow graphs](../assets/eip-8173/control-flow.svg)

Merely _traversing_ this graph is quadratic in the size of the code: every block's `jump` might reach every block's `jumpdest`, so the number of edges is the number of jumps times the number of destinations — quadratic, O(N²).  Any tool that must consider where jumps can go pays that price whether it actually draws the graph or not.  _Walking_ the paths costs far more.  A tool that must follow all of the paths forks its walk at every jump whose destination it cannot know, and the forks compound: the number of walks can grow exponentially or, worse, factorially in the size of the code — O(eᴺ) or O(N!).

In the JVM, Wasm, and the CLR it is simply impossible to have programs like these.

For Ethereum, these behaviors are a _denial-of-service vulnerability_ for any online static analysis, including bytecode validation and ahead-of-time (AOT) compilation at contract creation time, and JIT compilation at runtime.

Even offline, dynamic jumps (and the lack of calls and returns) can cause static analyses of many contracts to become quadratically impractical, exponentially intractable, or even mathematically impossible. The problem lies where several fields meet — graph theory, compilers, languages, virtual machines, security — each naming the same things differently.  For further examples, consider these abstracts from a few recent papers on the problem.  The last paper brings neural networks to bear, and still disassembles only most Solidity programs.  There is an entire academic literature of complex, incomplete solutions to problems that static control flow renders trivial.

> "Ethereum smart contracts are distributed programs running on top of the Ethereum blockchain. Since program flaws can cause significant monetary losses and can hardly be fixed due to the immutable nature of the blockchain, there is a strong need of automated analysis tools which provide formal security guarantees. Designing such analyzers, however, proved to be challenging and error-prone."[^4]
>
> "The EVM language is a simple stack-based language ... with one significant difference between the EVM and other virtual machine languages (like Java bytecode or CLI for .Net programs): the use of the stack for saving the jump addresses instead of having it explicit in the code of the jumping instructions. Static analyzers need the complete control flow graph (CFG) of the EVM program in order to be able to represent all its execution paths."[^5]
>
> "Static analysis approaches mostly face the challenge of analyzing compiled Ethereum bytecode... However, due to the intrinsic complexity of Ethereum bytecode (especially in jump resolution), static analysis encounters significant obstacles."[^6]
>
> "Analyzing contract binaries is vital ... comprising function entry identification and detecting its boundaries... Unfortunately, it is challenging to identify functions ... due to the lack of internal function call statements."[^7]

In my experience, to avoid the problems of dynamic control flow, VMs use static jumps, calls, and returns.

### Static Control Flow and Ethereum Scaling

[As laid out above](#control-flow-graphs), _static control flow_ means that the destination of every jump or call is determinable _a priori_, before execution. This has concrete implications for Ethereum's scaling roadmap, particularly around ZK verification, rollups, and future execution layer changes.

#### Static Control Flow and Rollups

##### ZK-Rollups

To understand why static control flow matters for ZK-Rollups[^8], we need to briefly understand how ZK systems verify computation:

* _Execution Traces:_ When a transaction executes, it produces an execution trace: a concrete, step-by-step record of every opcode executed, with the values of the stack, memory, and storage at each step. The trace records what actually happened — including exactly where every jump went — so it is always linear in the number of steps executed.
* _Circuits:_ A circuit is a mathematical model of a computation. For a ZK system, the circuit encodes the rules of the EVM: what states can follow from what prior states, how gas is consumed, which memory accesses are valid, etc. The circuit is a set of polynomial constraints that must all be satisfied. Crucially, the circuit encodes the _rules_ for each opcode type (including the rule for JUMP), not the specific paths taken by any particular execution.
* _Witnesses:_ The witness is the private data the prover supplies to demonstrate that a specific execution was correct. It includes the execution trace itself plus auxiliary data. The public inputs are the pre- and post-state roots — what the state was before and after the transaction.
* _Proofs:_ A ZK proof is a cryptographic proof that the witness satisfies the circuit's constraints, without revealing the witness itself.

A ZK-Rollup sequencer or prover batches many transactions, generates a ZK proof that all transactions executed correctly, and submits that proof to layer 1 (L1), where it is quickly verified. The prover works from the _actual_ execution trace — it does not explore or enumerate possible paths. The jump destinations are already known because they were recorded when the transaction ran.

The benefits of static control flow for ZK proving are therefore not about path exploration, but about the efficiency of the code being proven and the tractability of the analyses that surround it:

* _Leaner bytecode:_ Static jumps, explicit subroutine calls, and better stack discipline (eliminating SWAP/DUP workarounds) produce significantly smaller and simpler bytecode. Because the prover must process every opcode in the execution trace, fewer opcodes mean less work.
* _Deployment-time validation:_ With static control flow, bytecode can be fully validated once at deployment in linear time — including stack underflow, static stack depths, and reachability — rather than requiring expensive per-execution checks or quadratic offline analysis. This is where the O(N²) CFG problem [described above](#evm-any-jump-anywhere) directly impacts ZK infrastructure: building and analyzing the CFG of legacy EVM code before constructing a circuit or a formal model requires quadratic work; static control flow reduces this to linear.
* _Faster proof generation and lower hardware requirements_ follow directly from the above: fewer opcodes to prove and cheaper analysis reduce the compute and memory demands on rollup provers.

##### Optimistic Rollups

_Optimistic Rollups_ assume transactions are valid but allow fraud proofs to dispute invalid state roots. A fraud proof re-executes the contested transaction and demonstrates that the submitted state root was wrong. Key implications of static control flow include:

* _Bytecode validation:_ Static control flow allows contract bytecode to be fully validated at deployment in linear time, establishing safety properties that can be relied on during dispute resolution.
* _Dispute resolution:_ When a fraud dispute arises, the dispute system must re-execute the contested transaction. The re-execution itself is deterministic regardless of control flow style, but static control flow makes the surrounding machinery — validators, formal checkers, and the interactive verification game — simpler to implement correctly and easier to reason about.
* _Interactive verification:_ Some optimistic rollup designs use multi-round interactive verification games that bisect execution to identify the disputed step. Clear, structured control flow makes the bisection protocol more tractable and reduces the risk of edge cases in the dispute game implementation.

#### Static Control Flow and Code Generation

As already discussed, static control flow enables contracts to be compiled to machine code before execution, just-in-time or ahead-of-time.  This is an obvious win for non-ZK clients, whether on L1, layer 2 (L2), or EVM-compatible chains.

#### Static Control Flow and RISC-V Migration

There are ongoing discussions within the Ethereum research community about potentially replacing the EVM with a RISC-V execution environment. RISC-V has a standard instruction set architecture that is seeing increasing use in the ZK community.  One current strategy for creating a ZK-EVM is to compile an EVM interpreter like revm to RISC-V for use in a ZK-VM.  Supporting RISC-V directly eliminates the overhead of the EVM interpreter.  An EVM with static control flow opens up another strategy — compile the EVM code to RISC-V code.  That gives good RISC-V code in one linear-time pass, and better code in multiple passes, altogether linear time.

A missing piece in this puzzle is that RISC-V is a 32-bit or 64-bit architecture, but the current EVM is a 256-bit architecture.  For that purpose there are current proposals for 64-bit EVM opcodes.  It's also the case that newer proof systems can charge for only the bits actually used[^9], which may in time blunt the width problem.  Today's zkVMs, though, pay per executed 256-bit instruction.

## Specification

Several EIPs, past and current, specify new EVM opcodes and semantics for static control flow: subroutines and static jumps, container-format functions, call and return opcodes, and static relative jumps and calls.  They are all implemented with the standard Turing return stack architecture, and are for the most part compatible with each other.  In particular, the simplest of them — three call and return opcodes — can be used to implement all of the others.

## Rationale

Static control flow has been a cornerstone of efficient computation since Babbage and Turing. The EVM's reliance on dynamic jumps is an anomaly among virtual machines and a significant barrier to analysis, compilation, and scaling. Proposals to introduce explicit call/return opcodes and enforce static control flow bring the EVM in line with industry best practices and unlock a range of optimizations critical to Ethereum's scaling roadmap.

Static control flow is not a silver bullet. But it is a _foundational piece_ that enables:

* Better tooling and security analysis for language developers and auditors
* Faster execution via compilation for non-ZK clients
* Future migrations to other execution environments (RISC-V, etc.)
* Efficient ZK proof generation for ZK-Rollups
* Cleaner fraud proofs for Optimistic Rollups

By making control flow explicit and enforceable, the EVM becomes compatible with the full ecosystem of optimization and analysis techniques that other VMs and processor designs have relied on for decades.

## Security Considerations

This Informational proposal itself specifies no changes to the protocol.  Therefore it has no direct security implications.  It does not affect the security considerations of the proposals it describes; rather, it helps to motivate and contextualize them.

[^1]:
    ```csl-json
    {
      "type": "article",
      "id": 1,
      "author": [
        {
          "family": "Menabrea",
          "given": "L.F."
        }
      ],
      "DOI": "10.1145/2809523.2809528",
      "title": "Sketch of the Analytical Engine Invented by Charles Babbage.",
      "original-date": {
        "date-parts": [
          [1842, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1145/2809523.2809528"
    }
    ```

[^2]:
    ```csl-json
    {
      "type": "article",
      "id": 2,
      "author": [
        {
          "family": "Turing",
          "given": "A.M."
        }
      ],
      "DOI": "10.1093/mind/LIX.236.433",
      "title": "Computing Machinery and Intelligence.",
      "original-date": {
        "date-parts": [
          [1950, 10, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/mind/LIX.236.433"
    }
    ```

[^3]:
    ```csl-json
    {
      "type": "article",
      "id": 3,
      "author": [
        {
          "family": "Carpenter",
          "given": "B.E."
        }
      ],
      "DOI": "10.1093/comjnl/20.3.269",
      "title": "The other Turing machine.",
      "original-date": {
        "date-parts": [
          [1977, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.1093/comjnl/20.3.269"
    }
    ```

[^4]:
    ```csl-json
    {
      "type": "article",
      "id": 4,
      "author": [
        {
          "family": "Schneidewind",
          "given": "Clara"
        }
       ],
       "DOI": "10.48550/arXiv.2101.05735",
       "title": "The Good, the Bad and the Ugly: Pitfalls and Best Practices in Automated Sound Static Analysis of Ethereum Smart Contracts.",
       "original-date": {
         "date-parts": [
         [2021, 1, 14]
        ]
      },
      "URL": "https://arxiv.org/abs/2101.05735"
    }
    ```

[^5]:
    ```csl-json
    {
      "type": "article",
      "id": 5,
      "author": [
        {
          "family": "Albert",
          "given": "Elvira"
        }
      ],
      "DOI": "10.48550/arXiv.2004.14437",
      "title": "Analyzing Smart Contracts: From EVM to a Sound Control Flow Graph.",
      "original-date": {
        "date-parts": [
          [2020, 4, 29]
        ]
      },
      "URL": "https://arxiv.org/abs/2004.14437"
    }
    ```

[^6]:
    ```csl-json
    {
      "type": "article",
      "id": 6,
      "author": [
        {
          "family": "Contro",
          "given": "Filippo"
        }
      ],
      "DOI": "10.48550/arXiv.2103.09113",
      "title": "EtherSolve: Computing an Accurate Control Flow Graph from Ethereum Bytecode.",
      "original-date": {
        "date-parts": [
          [2021, 3, 16]
        ]
      },
      "URL": "https://arxiv.org/abs/2103.09113"
    }
    ```

[^7]:
    ```csl-json
    {
      "type": "article",
      "id": 7,
      "author": [
        {
          "family": "He",
          "given": "Jiahao"
        }
      ],
      "DOI": "10.48550/arXiv.2301.12695",
      "title": "Neural-FEBI: Accurate Function Identification in Ethereum Virtual Machine Bytecode.",
      "original-date": {
        "date-parts": [
          [2023, 1, 30]
        ]
      },
      "URL": "https://arxiv.org/abs/2301.12695"
    }
    ```

[^8]:
    ```csl-json
    {
      "type": "article",
      "id": 8,
      "author": [
        {
          "family": "Jain",
          "given": "Akshita"
        }
      ],
      "DOI": "10.30696/JAC.XVIII.1.2024.297-315",
      "title": "Exploring the Efficacy of Rollups: A Comparative Study of Optimistic and ZK-Rollups and Their Popular Implementations.",
      "original-date": {
        "date-parts": [
          [2024, 1, 1]
        ]
      },
      "URL": "https://doi.org/10.30696/JAC.XVIII.1.2024.297-315"
    }
    ```

[^9]:
    ```csl-json
    {
      "type": "article",
      "id": 9,
      "author": [
        {
          "family": "Diamond",
          "given": "Benjamin E."
        }
      ],
      "DOI": "10.1007/978-3-031-91134-7_4",
      "title": "Succinct Arguments over Towers of Binary Fields.",
      "original-date": {
        "date-parts": [
          [2025, 5, 4]
        ]
      },
      "URL": "https://doi.org/10.1007/978-3-031-91134-7_4"
    }
    ```

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>
