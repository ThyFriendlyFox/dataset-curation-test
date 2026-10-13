# 3. Rust RFC: feature unification

`C-rfc_3692-feature-unification` · [C_github_commits_9step](README.md)

Source: <https://github.com/rust-lang/rfcs/blob/d2705ad64ba47e812a2b6b19d6f613fb4c14c5e0/text/3692-feature-unification.md> · License: MIT OR Apache-2.0 · 73 commits touching the file; 60 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 102 | 0 | 0.03 | commit 14ca6f6550 (2014-03-10) |
| 2 | revision_2 | 811 | 0 | 0.08 | commit 97d49c29eb (2024-09-11) |
| 3 | revision_3 | 845 | 0 | 0.51 | commit c3b17e8657 (2024-09-11) |
| 4 | revision_4 | 848 | 0 | 0.58 | commit 4bbdc5135a (2024-09-17) |
| 5 | revision_5 | 1179 | 0 | 0.79 | commit 8f848a4068 (2024-09-17) |
| 6 | revision_6 | 1301 | 0 | 0.86 | commit c0158e71d4 (2024-10-01) |
| 7 | revision_7 | 1481 | 0 | 0.93 | commit 0e1fbc4cb8 (2024-10-03) |
| 8 | final | 1582 | 0 | 1.00 | commit f17e8623ee (2025-11-28) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
feature unification
````

</details>

<details><summary><b>Step 1 — revision_1</b> (102 words)</summary>

````text
# Summary

One para explanation of the feature.

# Motivation

Why are we doing this? What use cases does it support? What is the expected outcome?

# Detailed design

This is the bulk of the RFC. Explain the design in enough detail for somebody familiar
with the language to understand, and for somebody familiar with the compiler to implement.
This should get into specifics and corner-cases, and include examples of how the feature is used.

# Alternatives

What other designs have been considered? What is the impact of not doing this?

# Unresolved questions

What parts of the design are still TBD?
````

</details>

<details><summary><b>Step 2 — revision_2</b> (811 words)</summary>

````text
# Summary
[summary]: #summary

One paragraph explanation of the feature.

# Motivation
[motivation]: #motivation

Why are we doing this? What use cases does it support? What is the expected outcome?

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

Explain the proposal as if it was already included in the language and you were teaching it to another Rust programmer. That generally means:

- Introducing new named concepts.
- Explaining the feature largely in terms of examples.
- Explaining how Rust programmers should *think* about the feature, and how it should impact the way they use Rust. It should explain the impact as concretely as possible.
- If applicable, provide sample error messages, deprecation warnings, or migration guidance.
- If applicable, describe the differences between teaching this to existing Rust programmers and new Rust programmers.
- Discuss how this impacts the ability to read, understand, and maintain Rust code. Code is read and modified far more often than written; will the proposed feature make code easier to maintain?

For implementation-oriented RFCs (e.g. for compiler internals), this section should focus on how compiler contributors should think about the change, and give examples of its concrete impact. For policy RFCs, this section should provide an example-driven introduction to the policy, and explain its impact in concrete terms.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

This is the technical portion of the RFC. Explain the design in sufficient detail that:

- Its interaction with other features is clear.
- It is reasonably clear how the feature would be implemented.
- Corner cases are dissected by example.

The section should return to the examples given in the previous section, and explain more fully how the detailed proposal makes those examples work.

# Drawbacks
[drawbacks]: #drawbacks

Why should we *not* do this?

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

- Why is this design the best in the space of possible designs?
- What other designs have been considered and what is the rationale for not choosing them?
- What is the impact of not doing this?
- If this is a language proposal, could this be done in a library or macro instead? Does the proposed change make Rust code easier or harder to read, understand, and maintain?

# Prior art
[prior-art]: #prior-art

Discuss prior art, both the good and the bad, in relation to this proposal.
A few examples of what this can include are:

- For language, library, cargo, tools, and compiler proposals: Does this feature exist in other programming languages and what experience have their community had?
- For community proposals: Is this done by some other community and what were their experiences with it?
- For other teams: What lessons can we learn from what other communities have done here?
- Papers: Are there any published papers or great posts that discuss this? If you have some relevant papers to refer to, this can serve as a more detailed theoretical background.

This section is intended to encourage you as an author to think about the lessons from other languages, provide readers of your RFC with a fuller picture.
If there is no prior art, that is fine - your ideas are interesting to us whether they are brand new or if it is an adaptation from other languages.

Note that while precedent set by other languages is some motivation, it does not on its own motivate an RFC.
Please also take into consideration that rust sometimes intentionally diverges from common language features.

# Unresolved questions
[unresolved-questions]: #unresolved-questions

- What parts of the design do you expect to resolve through the RFC process before this gets merged?
- What parts of the design do you expect to resolve through the implementation of this feature before stabilization?
- What related issues do you consider out of scope for this RFC that could be addressed in the future independently of the solution that comes out of this RFC?

# Future possibilities
[future-possibilities]: #future-possibilities

Think about what the natural extension and evolution of your proposal would
be and how it would affect the language and project as a whole in a holistic
way. Try to use this section as a tool to more fully consider all possible
interactions with the project and language in your proposal.
Also consider how this all fits into the roadmap for the project
and of the relevant sub-team.

This is also a good place to "dump ideas", if they are out of scope for the
RFC you are writing but otherwise related.

If you have tried and cannot think of any future possibilities,
you may simply state that you cannot think of anything.

Note that having something written down in the future-possibilities section
is not a reason to accept the current or a future RFC; such notes should be
in the section on motivation or rationale in this or subsequent RFCs.
The section merely provides additional information.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (845 words)</summary>

````text
# Summary
[summary]: #summary

Allow users to control feature unifcation.

Related issues:
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

# Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled baed on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependemncies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation

Explain the proposal as if it was already included in the language and you were teaching it to another Rust programmer. That generally means:

- Introducing new named concepts.
- Explaining the feature largely in terms of examples.
- Explaining how Rust programmers should *think* about the feature, and how it should impact the way they use Rust. It should explain the impact as concretely as possible.
- If applicable, provide sample error messages, deprecation warnings, or migration guidance.
- If applicable, describe the differences between teaching this to existing Rust programmers and new Rust programmers.
- Discuss how this impacts the ability to read, understand, and maintain Rust code. Code is read and modified far more often than written; will the proposed feature make code easier to maintain?

For implementation-oriented RFCs (e.g. for compiler internals), this section should focus on how compiler contributors should think about the change, and give examples of its concrete impact. For policy RFCs, this section should provide an example-driven introduction to the policy, and explain its impact in concrete terms.

# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

### Rust Version

We'll add two new modes to feature unifcation:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current target
3. Resolve features
4. Filter for selected packages

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there is disjoint sets of features.

For example purposes., this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only enabled for each package, preferring duplicate builds of dependencies to when different feature sets are selected

# Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run-to-run, this covers more use cases
- As this fits easily into the `resolver` table. there is less design work

This will not support exceptions for mutually exclusive features because those are officially unsupported.
Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).

# Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

# Unresolved questions
[unresolved-questions]: #unresolved-questions


# Future possibilities
[future-possibilities]: #future-possibilities

Add a related field to manifests that the config can override.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (848 words)</summary>

````text
# Summary
[summary]: #summary

Allow users to control feature unifcation.

Related issues:
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

# Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled based on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependencies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

We'll add two new modes to feature unification:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current target
3. Resolve features
4. Filter for selected packages

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there are disjoint sets of features.

For example purposes., this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.
The initial implementation may be sub-optimal.
Likely, the implementation could be improved over time.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only enabled for each package, preferring duplicate builds of dependencies to when different feature sets are selected

# Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

If someone enables mutually exclusive features in different packages, then `workspace` unification will fail.
Officially, features are supposed to be additive, making mutually exclusive features officially unsupported.
Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).

Some features cannot be enabled in some packages, like a `no_std` package not wanting `std` features.
These workspaces will not be able to use `workspace` unification.
For now, unifying for the `"workspace"` is primarily targeted at single-application workspaces.
The other config fields can always be used instead.

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run-to-run, this covers more use cases
- As this fits easily into the `resolver` table. there is less design work

We could extend this with configuration for to exclude packages for the various use cases mentioned.
Supporting excludes as environemnt/project configuration complexity as well as implementation complexity.

# Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

# Unresolved questions
[unresolved-questions]: #unresolved-questions

- This keeps build/host feature unification behavior delegated to `workspace.resolver`
  - `cargo hakari` exposes multiple ways to configure this, see [unify-target-host](https://docs.rs/cargo-hakari/latest/cargo_hakari/config/index.html#unify-target-host)
  - For Oxide this reduced build units from 1900 to 1500, dramatically improving compile times, see https://github.com/oxidecomputer/omicron/pull/4535
  - However, this required effort to make sure additional settings are unified between host and target
  - This might be somewhat related to [`-Ztarget-applies-to-host`](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#target-applies-to-host)
  - If this got pulled in, there would no longer be enough of a case to justify `cargo-hakari` development

# Future possibilities
[future-possibilities]: #future-possibilities

Add a related field to manifests that the config can override.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (1179 words)</summary>

````text
# Summary
[summary]: #summary

Allow users to control feature unifcation.

Related issues:
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

# Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled based on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependencies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

We'll add two new modes to feature unification:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current target
3. Resolve features
4. Filter for selected packages

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there are disjoint sets of features.

For example purposes., this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.
The initial implementation may be sub-optimal.
Likely, the implementation could be improved over time.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only enabled for each package, preferring duplicate builds of dependencies to when different feature sets are selected

# Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

If someone enables mutually exclusive features in different packages, then `workspace` unification will fail.
Officially, features are supposed to be additive, making mutually exclusive features officially unsupported.
Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).

Some features cannot be enabled in some packages, like a `no_std` package not wanting `std` features.
These workspaces will not be able to use `workspace` unification.
For now, unifying for the `"workspace"` is primarily targeted at single-application workspaces.
The other config fields can always be used instead.

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run-to-run, this covers more use cases
- As this fits easily into the `resolver` table. there is less design work

We could extend this with configuration for to exclude packages for the various use cases mentioned.
Supporting excludes as environemnt/project configuration complexity as well as implementation complexity.

# Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

# Unresolved questions
[unresolved-questions]: #unresolved-questions

- How to name the config field to not block the future possibilities

# Future possibilities
[future-possibilities]: #future-possibilities

### Manifest support

Add a related field to manifests that the config can override.

### Dependency version unification

Unlike feature unification, dependency versions are alwayd unified across the
entire workspace, making `Cargo.lock` the same regardless of which package you
select or how you build.

This can mask minimal-version bugs.
If a version-req is lower than it needs, `-Zminimal-versions` won't resolve down to that to show the problem if another version req in the workspace is higher.
We have `-Zdirect-minimal-versions` which will error if workspace members do not have the lowest version reqs of all of the workspace but that is brittle.

If you have a workspace with multiple MSRVs, you can't verify your MSRV if you
set a high-MSRV package's version req for a dependency that invalidates the
MSRV-requirements of a low-MSRV package.

We could offer an opt-in to per-package `Cargo.lock` files.  For builds, this
could be implemented similar to `resolver.feature-unification = "package"`.

This could run into problems with
- `cargo update` being workspace-focused
- third-party updating tools

As for the MSRV-case, this would only help if you develop with the latest
versions locally and then have a job that resolves down to your MSRVs.

### Unify features in other settings

[`workspace.resolver = "2"`](https://doc.rust-lang.org/cargo/reference/resolver.html#features) removed unification from the following scenarios
- Cross-platform target unification
- `build-dependencies` / `dependencies` unification
- `dev-dependencies` / `dependencies` unification unless a dev target is enabled

Depending on how we design this, the solution might be good enough to
re-evaluate
[build-target features](https://github.com/rust-lang/rfcs/pull/3374) as we
could offer a way for users to opt-out of build-target unification.

Like with `resolver.incompatible-rust-version`, a solution for this would override the defaults of `workspace.resolver`.

`cargo hakaro` gives control over `build-dependencies` / `dependencies` unification with
[`unify-target-host`](https://docs.rs/cargo-hakari/latest/cargo_hakari/config/index.html#unify-target-host):
- [`none`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.None): Perform no unification across the target and host feature sets.
  - The same as `resolver = "2"`
- [`unify-if-both`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.UnifyIfBoth): Perform unification across target and host feature sets, but only if a dependency is built on both the target and the host.
- [`replicate-target-on-host`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.ReplicateTargetOnHost): Perform unification across target and host feature sets, and also replicate all target-only lines to the host.
- [`auto`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.Auto) (default): select `replicate-target-on-host` if a workspace member may be built for the host (used as a proc-macro or build-dependency)

`unify-target-host` might be somewhat related to [`-Ztarget-applies-to-host`](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#target-applies-to-host)

For Oxide `unify-target-host` reduced build units from 1900 to 1500, dramatically improving compile times, see https://github.com/oxidecomputer/omicron/pull/4535
If integrated into cargo, there would no longer be a use case for the current maintainer of `cargo-hakari` to continue maintenance.
````

</details>

<details><summary><b>Step 6 — revision_6</b> (1301 words)</summary>

````text
# Summary
[summary]: #summary

Allow users to control feature unification.

Related issues:
- [#5210: Resolve feature and optional dependencies for workspace as a whole](https://github.com/rust-lang/cargo/issues/5210)
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

# Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled based on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependencies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

We'll add two new modes to feature unification:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current build-target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current build-target
3. Resolve features
4. Filter for selected packages

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there are disjoint sets of features.

For example, this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.
The initial implementation may be sub-optimal.
Likely, the implementation could be improved over time.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only considered on a package-by-package basis, preferring duplicate builds of dependencies when different sets of feature are activated by the packages.

# Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

If someone enables mutually exclusive features in different packages, then `workspace` unification will fail.
Officially, features are supposed to be additive, making mutually exclusive features officially unsupported.
Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).

Some features cannot be enabled in some packages, like a `no_std` package not wanting `std` features.
These workspaces will not be able to use `workspace` unification.
For now, unifying for the `"workspace"` is primarily targeted at single-application workspaces.
The other config fields can always be used instead.

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run to run, this covers more use cases.
- As this fits easily into the `resolver` table, there is less design work.

We could extend this with configuration to exclude packages for the various use cases mentioned.
Supporting excludes adds environment/project configuration complexity as well as implementation complexity.

# Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

# Unresolved questions
[unresolved-questions]: #unresolved-questions

- How to name the config field to not block the future possibilities

# Future possibilities
[future-possibilities]: #future-possibilities

### Support in manifests

Add a related field to manifests that the config can override.

### Dependency version unification

Unlike feature unification, dependency versions are always unified across the
entire workspace, making `Cargo.lock` the same regardless of which package you
select or how you build.

This can mask minimal-version bugs.
If a version-req is lower than it needs, `-Zminimal-versions` won't resolve down to that to show the problem if another version req in the workspace is higher.
We have `-Zdirect-minimal-versions` which will error if workspace members do not have the lowest version reqs of all of the workspace but that is brittle.

If you have a workspace with multiple MSRVs, you can't verify your MSRV if you
set a high-MSRV package's version req for a dependency that invalidates the
MSRV-requirements of a low-MSRV package.

We could offer an opt-in to per-package `Cargo.lock` files.  For builds, this
could be implemented similar to `resolver.feature-unification = "package"`.

This could run into problems with
- `cargo update` being workspace-focused
- third-party updating tools

As for the MSRV-case, this would only help if you develop with the latest
versions locally and then have a job that resolves down to your MSRVs.

### Unify features in other settings

[`workspace.resolver = "2"`](https://doc.rust-lang.org/cargo/reference/resolver.html#features) removed unification from the following scenarios
- Cross-platform build-target unification
- `build-dependencies` / `dependencies` unification
- `dev-dependencies` / `dependencies` unification unless a dev build-target is enabled

Depending on how we design this, the solution might be good enough to
re-evaluate
[build-target features](https://github.com/rust-lang/rfcs/pull/3374) as we
could offer a way for users to opt-out of build-target unification.

Like with `resolver.incompatible-rust-version`, a solution for this would override the defaults of `workspace.resolver`.

`cargo hakari` gives control over `build-dependencies` / `dependencies` unification with
[`unify-target-host`](https://docs.rs/cargo-hakari/latest/cargo_hakari/config/index.html#unify-target-host):
- [`none`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.None): Perform no unification across the target and host feature sets.
  - The same as `resolver = "2"`
- [`unify-if-both`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.UnifyIfBoth): Perform unification across target and host feature sets, but only if a dependency is built on both the platform-target and the host.
- [`replicate-target-on-host`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.ReplicateTargetOnHost): Perform unification across platform-target and host feature sets, and also replicate all target-only lines to the host.
- [`auto`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.Auto) (default): select `replicate-target-on-host` if a workspace member may be built for the host (used as a proc-macro or build-dependency)

`unify-target-host` might be somewhat related to [`-Ztarget-applies-to-host`](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#target-applies-to-host)

For Oxide `unify-target-host` reduced build units from 1900 to 1500, dramatically improving compile times, see https://github.com/oxidecomputer/omicron/pull/4535
If integrated into cargo, there would no longer be a use case for the current maintainer of `cargo-hakari` to continue maintenance.

If we supported `dev-dependencies` / `dependencies` like `resolver = "1"`, it
could help with cases like `cargo miri` where through `dev-dependencies` a
`libc` feature is enabled. preventing reuse of builds between `cargo build` and
`cargo test` for local development.

In helping this case, we should make clear that this can also break people
- `fail` injects failures into your production code, only wanting it enabled for tests
- Tests generally enabled `std` on dependencies for `no_std` packages
- We were told of use cases around private keys where `Clone` is only provided when testing but not for production to help catch the leaking of secrets
````

</details>

<details><summary><b>Step 7 — revision_7</b> (1481 words)</summary>

````text
# Summary
[summary]: #summary

Give users control over the feature unification that happens based on the packages they select.
- A way for `cargo check -p foo -p bar` to build like `cargo check -p foo && cargo check -p bar`
- A way for `cargo check -p foo` to build `foo` as if `cargo check --workspace` was used

Related issues:
- [#5210: Resolve feature and optional dependencies for workspace as a whole](https://github.com/rust-lang/cargo/issues/5210)
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

# Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled based on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependencies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

# Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


# Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

We'll add two new modes to feature unification:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current build-target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current build-target
3. Resolve features
4. Filter for selected packages

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there are disjoint sets of features.

For example, this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.
The initial implementation may be sub-optimal.
Likely, the implementation could be improved over time.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only considered on a package-by-package basis, preferring duplicate builds of dependencies when different sets of feature are activated by the packages.

# Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

If someone enables mutually exclusive features in different packages, then `workspace` unification will fail.
Officially, features are supposed to be additive, making mutually exclusive features officially unsupported.
Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).

Some features cannot be enabled in some packages, like a `no_std` package not wanting `std` features.
These workspaces will not be able to use `workspace` unification.
For now, unifying for the `"workspace"` is primarily targeted at single-application workspaces.
The other config fields can always be used instead.

# Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run to run, this covers more use cases.
- As this fits easily into the `resolver` table, there is less design work.

We could extend this with configuration to exclude packages for the various use cases mentioned.
Supporting excludes adds environment/project configuration complexity as well as implementation complexity.

This field will not apply to `cargo install` to match the behavior of `resolver.incompatible-rust-versions`.

The `workspace` setting breaks down if there are more than one "application" in
a workspace, particularly if there are shared dependencies with intentionally
disjoint feature sets.
What this use case is really modeling is being able to tell Cargo "build package X as if its a dependency of package Y".
There are many similar use cases to this (e.g. [cargo#2644](https://github.com/rust-lang/cargo/issues/2644), [cargo#14434](https://github.com/rust-lang/cargo/issues/14434)).
While a solution that targeted this higher-level need would cover more uses cases,
there is a lot more work to do within the design space and it could end up being more unwieldy.
The solution offered in this RFC is simple in that it is just a re-framing of what already happens on the command line.

# Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

# Unresolved questions
[unresolved-questions]: #unresolved-questions

- How to name the config field to not block the future possibilities

# Future possibilities
[future-possibilities]: #future-possibilities

### Support in manifests

Add a related field to manifests that the config can override.

### Dependency version unification

Unlike feature unification, dependency versions are always unified across the
entire workspace, making `Cargo.lock` the same regardless of which package you
select or how you build.

This can mask minimal-version bugs.
If a version-req is lower than it needs, `-Zminimal-versions` won't resolve down to that to show the problem if another version req in the workspace is higher.
We have `-Zdirect-minimal-versions` which will error if workspace members do not have the lowest version reqs of all of the workspace but that is brittle.

If you have a workspace with multiple MSRVs, you can't verify your MSRV if you
set a high-MSRV package's version req for a dependency that invalidates the
MSRV-requirements of a low-MSRV package.

We could offer an opt-in to per-package `Cargo.lock` files.  For builds, this
could be implemented similar to `resolver.feature-unification = "package"`.

This could run into problems with
- `cargo update` being workspace-focused
- third-party updating tools

As for the MSRV-case, this would only help if you develop with the latest
versions locally and then have a job that resolves down to your MSRVs.

### Unify features in other settings

[`workspace.resolver = "2"`](https://doc.rust-lang.org/cargo/reference/resolver.html#features) removed unification from the following scenarios
- Cross-platform build-target unification
- `build-dependencies` / `dependencies` unification
- `dev-dependencies` / `dependencies` unification unless a dev build-target is enabled

Depending on how we design this, the solution might be good enough to
re-evaluate
[build-target features](https://github.com/rust-lang/rfcs/pull/3374) as we
could offer a way for users to opt-out of build-target unification.

Like with `resolver.incompatible-rust-version`, a solution for this would override the defaults of `workspace.resolver`.

`cargo hakari` gives control over `build-dependencies` / `dependencies` unification with
[`unify-target-host`](https://docs.rs/cargo-hakari/latest/cargo_hakari/config/index.html#unify-target-host):
- [`none`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.None): Perform no unification across the target and host feature sets.
  - The same as `resolver = "2"`
- [`unify-if-both`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.UnifyIfBoth): Perform unification across target and host feature sets, but only if a dependency is built on both the platform-target and the host.
- [`replicate-target-on-host`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.ReplicateTargetOnHost): Perform unification across platform-target and host feature sets, and also replicate all target-only lines to the host.
- [`auto`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.Auto) (default): select `replicate-target-on-host` if a workspace member may be built for the host (used as a proc-macro or build-dependency)

`unify-target-host` might be somewhat related to [`-Ztarget-applies-to-host`](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#target-applies-to-host)

For Oxide `unify-target-host` reduced build units from 1900 to 1500, dramatically improving compile times, see https://github.com/oxidecomputer/omicron/pull/4535
If integrated into cargo, there would no longer be a use case for the current maintainer of `cargo-hakari` to continue maintenance.

If we supported `dev-dependencies` / `dependencies` like `resolver = "1"`, it
could help with cases like `cargo miri` where through `dev-dependencies` a
`libc` feature is enabled. preventing reuse of builds between `cargo build` and
`cargo test` for local development.

In helping this case, we should make clear that this can also break people
- `fail` injects failures into your production code, only wanting it enabled for tests
- Tests generally enabled `std` on dependencies for `no_std` packages
- We were told of use cases around private keys where `Clone` is only provided when testing but not for production to help catch the leaking of secrets
````

</details>

<details><summary><b>Step 8 — final</b> (1582 words)</summary>

````text
## Summary
[summary]: #summary

Give users control over the feature unification that happens based on the packages they select.
- A way for `cargo check -p foo -p bar` to build like `cargo check -p foo && cargo check -p bar`
- A way for `cargo check -p foo` to build `foo` as if `cargo check --workspace` was used

Related issues:
- [#5210: Resolve feature and optional dependencies for workspace as a whole](https://github.com/rust-lang/cargo/issues/5210)
- [#4463: Feature selection in workspace depends on the set of packages compiled](https://github.com/rust-lang/cargo/issues/4463)
- [#8157: --bin B resolves features differently than -p B in a workspace](https://github.com/rust-lang/cargo/issues/8157)
- [#13844: The cargo build --bins re-builds binaries again after cargo build --all-targets](https://github.com/rust-lang/cargo/issues/13844)

## Motivation
[motivation]: #motivation

Today, when Cargo is building, features in dependencies are enabled based on the set of packages selected to build.
This is an attempt to balance
- Build speed: we should reuse builds between packages within the same invocation
- Ability to verify features for a given package

This isn't always ideal.

If a user is building an application, they may be jumping around the application's components which are packages within the workspace.
The final artifact is the same but Cargo will select different features depending on which package they are currently building,
causing build churn for the same set of dependencies that, in the end, will only be used with the same set of features.
The "cargo-workspace-hack" is a pattern that has existed for years
(e.g. [`rustc-workspace-hack`](https://crates.io/crates/rustc-workspace-hack))
where users have all workspace members that depend on a generated package that depends on direct-dependencies in the workspace along with their features.
Tools like [`cargo-hakari`](https://crates.io/crates/cargo-hakari) automate this process.
To allow others to pull in a package depending on a workspace-hack package as a git dependency, you then need to publish the workspace-hack as an empty package with no dependencies
and then locally patch in the real instance of it.

This also makes testing of features more difficult because a user can't just run `cargo check --workspace` to verify that the correct set of features are enabled.
This has led to the rise of tools like [cargo-hack](https://crates.io/crates/cargo-hack) which de-unify packages.

## Guide-level explanation
[guide-level-explanation]: #guide-level-explanation


## Reference-level explanation
[reference-level-explanation]: #reference-level-explanation

We'll add two new modes to feature unification:

**Unify features across the workspace, independent of the selected packages**

This would be built-in support for "cargo-workspace-hack".

This would require effectively changing from
1. Resolve dependencies
2. Filter dependencies down for current build-target and selected packages
3. Resolve features

To
1. Resolve dependencies
2. Filter dependencies down for current build-target
3. Resolve features
4. Filter for selected packages

The same result can be achieved with `cargo check --workspace`,
but with fewer packages built.
Therefore, no fundamentally new "mode" is being introduced.

**Features will be evaluated for each package in isolation**

This will require building duplicate copies of build units when there are disjoint sets of features.

For example, this could be implemented as either
- Loop over the packages, resolving, and then run a build plan for that package
- Resolve for each package and generate everything into the same build plan

This is not prescriptive of the implementation but to illustrate what the feature does.
The initial implementation may be sub-optimal.
Likely, the implementation could be improved over time.

The same result can be achieved with `cargo check -p foo && cargo check -p bar`,
but with the potential for optimizing the build further.
Therefore, no fundamentally new "mode" is being introduced.

**Note:** these features do not need to be stabilized together.

##### `resolver.feature-unification`

*(update to [Configuration](https://doc.rust-lang.org/cargo/reference/config.html))*

* Type: string
* Default: "selected"
* Environment: `CARGO_RESOLVER_FEATURE_UNIFICATION`

Specify which packages participate in [feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

* `selected`: merge dependency features from all package specified for the current build
* `workspace`: merge dependency features across all workspace members, regardless of which packages are specified for the current build
* `package`: dependency features are only considered on a package-by-package basis, preferring duplicate builds of dependencies when different sets of feature are activated by the packages.

## Drawbacks
[drawbacks]: #drawbacks

This increases entropy within Cargo and the universe at large.

As `workspace` unifcation builds dependencies the same way as `--workspace`, it has the same drawbacks as `--workspace`, including
- If a build would fail with `--workspace`, then it will fail with `workspace` unification as well.
  - For example, if two packages in a workspace enable mutually exclusive features, builds will fail with both `--workspace` and `workspace` unification.
    Officially, features are supposed to be additive, making mutually exclusive features officially unsupported.
    Instead, effort should be put towards [official mutually exclusive globals](https://internals.rust-lang.org/t/pre-rfc-mutually-excusive-global-features/19618).
- If `--workspace` would produce an invalid binary for your requirements, then it will do so with `workspace` unification as well.
  - For example, if you have regular packages and a `no_std` package in the same workspace, the `no_std` package may end up with dependnencies built with `std` features.

## Rationale and alternatives
[rationale-and-alternatives]: #rationale-and-alternatives

This is done in the config instead of the manifest:
- As this can change from run to run, this covers more use cases.
- As this fits easily into the `resolver` table, there is less design work.

We could extend this with configuration to exclude packages for the various use cases mentioned.
Supporting excludes adds environment/project configuration complexity as well as implementation complexity.

This field will not apply to `cargo install` to match the behavior of `resolver.incompatible-rust-versions`.

The `workspace` setting breaks down if there are more than one "application" in
a workspace, particularly if there are shared dependencies with intentionally
disjoint feature sets.
What this use case is really modeling is being able to tell Cargo "build package X as if its a dependency of package Y".
There are many similar use cases to this (e.g. [cargo#2644](https://github.com/rust-lang/cargo/issues/2644), [cargo#14434](https://github.com/rust-lang/cargo/issues/14434)).
While a solution that targeted this higher-level need would cover more uses cases,
there is a lot more work to do within the design space and it could end up being more unwieldy.
The solution offered in this RFC is simple in that it is just a re-framing of what already happens on the command line.

## Prior art
[prior-art]: #prior-art

[`cargo-hakari`](https://crates.io/crates/cargo-hakari) is a "cargo-workspace-hack" generator that builds a graph off of `cargo metadata` and re-implements feature unification.

[cargo-hack](https://crates.io/crates/cargo-hack) can run each selected package in a separate `cargo` invocation to prevent unification.

## Unresolved questions
[unresolved-questions]: #unresolved-questions

- How to name the config field to not block the future possibilities

## Future possibilities
[future-possibilities]: #future-possibilities

### Support in manifests

Add a related field to manifests that the config can override.

### Dependency version unification

Unlike feature unification, dependency versions are always unified across the
entire workspace, making `Cargo.lock` the same regardless of which package you
select or how you build.

This can mask minimal-version bugs.
If a version-req is lower than it needs, `-Zminimal-versions` won't resolve down to that to show the problem if another version req in the workspace is higher.
We have `-Zdirect-minimal-versions` which will error if workspace members do not have the lowest version reqs of all of the workspace but that is brittle.

If you have a workspace with multiple MSRVs, you can't verify your MSRV if you
set a high-MSRV package's version req for a dependency that invalidates the
MSRV-requirements of a low-MSRV package.

We could offer an opt-in to per-package `Cargo.lock` files.  For builds, this
could be implemented similar to `resolver.feature-unification = "package"`.

This could run into problems with
- `cargo update` being workspace-focused
- third-party updating tools

As for the MSRV-case, this would only help if you develop with the latest
versions locally and then have a job that resolves down to your MSRVs.

### Unify features in other settings

[`workspace.resolver = "2"`](https://doc.rust-lang.org/cargo/reference/resolver.html#features) removed unification from the following scenarios
- Cross-platform build-target unification
- `build-dependencies` / `dependencies` unification
- `dev-dependencies` / `dependencies` unification unless a dev build-target is enabled

Depending on how we design this, the solution might be good enough to
re-evaluate
[build-target features](https://github.com/rust-lang/rfcs/pull/3374) as we
could offer a way for users to opt-out of build-target unification.

Like with `resolver.incompatible-rust-version`, a solution for this would override the defaults of `workspace.resolver`.

`cargo hakari` gives control over `build-dependencies` / `dependencies` unification with
[`unify-target-host`](https://docs.rs/cargo-hakari/latest/cargo_hakari/config/index.html#unify-target-host):
- [`none`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.None): Perform no unification across the target and host feature sets.
  - The same as `resolver = "2"`
- [`unify-if-both`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.UnifyIfBoth): Perform unification across target and host feature sets, but only if a dependency is built on both the platform-target and the host.
- [`replicate-target-on-host`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.ReplicateTargetOnHost): Perform unification across platform-target and host feature sets, and also replicate all target-only lines to the host.
- [`auto`](https://docs.rs/hakari/0.17.4/hakari/enum.UnifyTargetHost.html#variant.Auto) (default): select `replicate-target-on-host` if a workspace member may be built for the host (used as a proc-macro or build-dependency)

`unify-target-host` might be somewhat related to [`-Ztarget-applies-to-host`](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#target-applies-to-host)

For Oxide `unify-target-host` reduced build units from 1900 to 1500, dramatically improving compile times, see https://github.com/oxidecomputer/omicron/pull/4535
If integrated into cargo, there would no longer be a use case for the current maintainer of `cargo-hakari` to continue maintenance.

If we supported `dev-dependencies` / `dependencies` like `resolver = "1"`, it
could help with cases like `cargo miri` where through `dev-dependencies` a
`libc` feature is enabled. preventing reuse of builds between `cargo build` and
`cargo test` for local development.

In helping this case, we should make clear that this can also break people
- `fail` injects failures into your production code, only wanting it enabled for tests
- Tests generally enabled `std` on dependencies for `no_std` packages
- We were told of use cases around private keys where `Clone` is only provided when testing but not for production to help catch the leaking of secrets
````

</details>
