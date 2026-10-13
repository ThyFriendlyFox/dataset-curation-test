# 7. Swift Evolution: Change `RangeReplaceableCollection.filter` to return `Self`

`C-se_0174-filter-range-replaceable` · [full/C_github_commits_5stage](README.md)

Source: <https://github.com/swiftlang/swift-evolution/blob/f4fa78fe9c8cf48b8fc312dfd400fe6d3e8f38db/proposals/0174-filter-range-replaceable.md> · License: Apache-2.0 · 12 commits touching the file; 7 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 5 | 0 | 0.02 | source_title |
| 1 | earliest_version | 707 | 0 | 0.77 | commit 8084cde39a (2017-04-28) |
| 2 | early_revision | 568 | 0 | 0.99 | commit bdb2fbfb98 (2021-04-16) |
| 3 | late_revision | 566 | 0 | 0.99 | commit a110042348 (2021-04-16) |
| 4 | final | 566 | 0 | 1.00 | commit d0e50d90a1 (2024-08-19) |

<details><summary><b>Step 0 — title</b> (5 words)</summary>

````text
Change `RangeReplaceableCollection.filter` to return `Self`
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (707 words)</summary>

````text
# Change `filter` to return an associated type

## Introduction

This proposal changes the `filter` operation on `Sequence` to return an
associated type, and adds a default implementation to
`RangeReplaceableCollection` to return the same type as the filtered collection.

## Motivation

The recently accepted
[SE-165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dic
 t.md) introduced a version of `filter` on `Dictionary` that returned a
`Dictionary`. This had both performance and useability benefits: in most cases,
a `Dictionary` is what the user wanted from the filter, and creating one
directly from the filter operation is much more efficient than first creating
an array then creating a `Dictionary` from it.

However, this does result in some inconsistencies. Users may be surprised that
this one specific collection returns `Self`, while other collections that would
benefit from the same change still return `[Element]`. And some collections,
such as `String`, might also benefit from usability and performance win similar
to `Dictionary`. Additionally, these wins will be lost in generic code – if you
pass a `Dictionary` into an algorithm that takes a `Sequence`, then when you
filter it, you will still get an `Array`.

## Proposed solution

The existing protocol requirement on `filter` will be changed to return an
associated type, `Filtered`. The extension providing a default implementation
will remain as-is, resulting in an inferred value for `Filtered` of
`[Element]`. `Dictionary` will automatically infer a filtered type of
`Dictionary` as a result of this change.

A default implementation on `RangeReplaceableCollection` will be provided,
using `init()` and `append(_:)`, so all range-replaceable collections will
have a `Filtered` of `Self`. Per [SE-163](https://github.com/apple/swift-evolution/blob/master/proposals/0163-string-revision-1.md),
this will include `String`.

Note, many sequences (for example, strides or ranges), cannot represent a
filtered `self` as `Self` and will continue to return an array. If this is a
performance problem, `lazy` remains a good solution.

## Detailed design

Add a `Filtered` associated type to `Sequence`, and change the requirement to
return it:

```swift
protocol Sequence {
  associatedtype Filtered
  /// Returns an filtered sequence containing, in order, the elements of the 
  /// sequence that satisfy the given predicate.
  ///
  /// In this example, `filter` is used to include only names shorter than
  /// five characters.
  ///
  ///     let cast = ["Vivien", "Marlon", "Kim", "Karl"]
  ///     let shortNames = cast.filter { $0.characters.count < 5 }
  ///     print(shortNames)
  ///     // Prints "["Kim", "Karl"]"
  ///
  /// - Parameter isIncluded: A closure that takes an element of the
  ///   sequence as its argument and returns a Boolean value indicating
  ///   whether the element should be included in the returned sequence.
  /// - Returns: An array of the elements that `includeElement` allowed.
  func filter(
    _ isIncluded: (Iterator.Element) throws -> Bool
  ) rethrows -> Filtered
}
```

Add a default implementation of `filter` to `RangeReplaceableCollection`
returning `Self`:

```swift
extension RangeReplaceableCollection {
    func filter(_ isIncluded: (Iterator.Element) throws -> Bool) rethrows -> Self {
        var result = Self()
        for element in self {
            if try isIncluded(element) {
                result.append(element)
            }
        }
        return result
    }
}
```

Specific concrete collections may choose to implement a faster version, but
this is an implementation detail.

## Source compatibility

This change is subtly source breaking. In most cases users will not notice.
They may be be relying on an array being returned (albeit often in order to
then transform it back into the original type), but this version will still
be available (via the extension on `Sequence`) and will be called if forced
through type context. The only code that will break is if this operation spans
multple lines:

```swift
// filtered used to be [Character], now String
let filtered = "abcd".filter { $0 == "a" }
useArray(filtered) // won't compile
```

Because of this, the new implementation of `RangeReplaceableCollection.filter`
will only be available in Swift 4.

## Effect on ABI stability

This change will affect the ABI of `Sequence` and needs to be made before
declaring ABI stability.

## Effect on API resilience

N/A

## Alternatives considered

Status-quo. There are benefits to the consistency of always returning `[Element]`.

It could be worthwhile to make a similar change to `map`, but this is beyond
the capabilities of the current generics system because `map` does not preserve
the element type (more specifically, you cannot express a type that is `Self`
except with a different `Element` in order to provide the default
implementation on `RangeReplaceableCollection`).
````

</details>

<details><summary><b>Step 2 — early_revision</b> (568 words)</summary>

````text
# Change `filter` to return an associated type

## Introduction

This proposal implements the `filter` operation on `RangeReplaceableCollection`
to return the same type as the filtered collection.

## Motivation

The recently accepted
[SE-165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md)
introduced a version of `filter` on `Dictionary` that returned a
`Dictionary`. This had both performance and usability benefits: in most cases,
a `Dictionary` is what the user wanted from the filter, and creating one
directly from the filter operation is much more efficient than first creating
an array then creating a `Dictionary` from it.

However, this does result in some inconsistencies. Users may be surprised that
this one specific collection returns `Self`, while other collections that would
benefit from the same change still return `[Element]`. And some collections,
such as `String`, might also benefit from usability and performance win similar
to `Dictionary`. Additionally, these wins will be lost in generic code – if you
pass a `Dictionary` into an algorithm that takes a `Sequence`, then when you
filter it, you will still get an `Array`.

## Proposed solution

An implementation of `filter` on `RangeReplaceableCollection` will be provided,
using `init()` and `append(_:)`, so all range-replaceable collections will
have a `filter` method returning of `Self`. Per [SE-163](https://github.com/apple/swift-evolution/blob/master/proposals/0163-string-revision-1.md),
this will include `String`.

Note, many sequences (for example, strides or ranges), cannot represent a
filtered `self` as `Self` and will continue to return an array. If this is a
performance problem, `lazy` remains a good solution.

## Detailed design

Add a default implementation of `filter` to `RangeReplaceableCollection`
returning `Self`:

```swift
extension RangeReplaceableCollection {
    func filter(_ isIncluded: (Iterator.Element) throws -> Bool) rethrows -> Self {
        var result = Self()
        for element in self {
            if try isIncluded(element) {
                result.append(element)
            }
        }
        return result
    }
}
```

Specific concrete collections may choose to implement a faster version, but
this is an implementation detail.

## Source compatibility

This change is subtly source breaking. In most cases users will not notice.
They may be be relying on an array being returned (albeit often in order to
then transform it back into the original type), but this version will still
be available (via the extension on `Sequence`) and will be called if forced
through type context. The only code that will break is if this operation spans
multple lines:

```swift
// filtered used to be [Character], now String
let filtered = "abcd".filter { $0 == "a" }
useArray(filtered) // won't compile
```

Because of this, the new implementation of `RangeReplaceableCollection.filter`
will only be available in Swift 4.

## Effect on ABI stability

This change will affect the ABI of `RangeReplaceableCollection` and needs to be made before
declaring ABI stability.

## Effect on API resilience

N/A

## Alternatives considered

Status-quo. There are benefits to the consistency of always returning `[Element]`.
The version on `Sequence` can be reached via type context (`"abc".filter(predicate) as [Element]`).

It could be worthwhile to make a similar change to `map`, but this is beyond
the capabilities of the current generics system because `map` does not preserve
the element type (more specifically, you cannot express a type that is `Self`
except with a different `Element` in order to provide the 
implementation on `RangeReplaceableCollection`).

## History

This proposal originally included a new associated type `Filtered` on `Sequence`. However, this
was unimplementable due to requiring a recursive type constraint (`Filtered: Sequence`). While
these were supported in later Swift versions, the additional associated type was not implemented
and that portion of the proposal has [expired](https://forums.swift.org/t/addressing-unimplemented-evolution-proposals/).
````

</details>

<details><summary><b>Step 3 — late_revision</b> (566 words)</summary>

````text
# Change `RangeReplaceableCollection.filter` to return `Self`

## Introduction

This proposal implements the `filter` operation on `RangeReplaceableCollection`
to return the same type as the filtered collection.

## Motivation

The recently accepted
[SE-165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md)
introduced a version of `filter` on `Dictionary` that returned a
`Dictionary`. This had both performance and usability benefits: in most cases,
a `Dictionary` is what the user wanted from the filter, and creating one
directly from the filter operation is much more efficient than first creating
an array then creating a `Dictionary` from it.

However, this does result in some inconsistencies. Users may be surprised that
this one specific collection returns `Self`, while other collections that would
benefit from the same change still return `[Element]`. And some collections,
such as `String`, might also benefit from usability and performance win similar
to `Dictionary`. Additionally, these wins will be lost in generic code – if you
pass a `Dictionary` into an algorithm that takes a `Sequence`, then when you
filter it, you will still get an `Array`.

## Proposed solution

An implementation of `filter` on `RangeReplaceableCollection` will be provided,
using `init()` and `append(_:)`, so all range-replaceable collections will
have a `filter` method returning of `Self`. Per [SE-163](https://github.com/apple/swift-evolution/blob/master/proposals/0163-string-revision-1.md),
this will include `String`.

Note, many sequences (for example, strides or ranges), cannot represent a
filtered `self` as `Self` and will continue to return an array. If this is a
performance problem, `lazy` remains a good solution.

## Detailed design

Add a default implementation of `filter` to `RangeReplaceableCollection`
returning `Self`:

```swift
extension RangeReplaceableCollection {
    func filter(_ isIncluded: (Iterator.Element) throws -> Bool) rethrows -> Self {
        var result = Self()
        for element in self {
            if try isIncluded(element) {
                result.append(element)
            }
        }
        return result
    }
}
```

Specific concrete collections may choose to implement a faster version, but
this is an implementation detail.

## Source compatibility

This change is subtly source breaking. In most cases users will not notice.
They may be be relying on an array being returned (albeit often in order to
then transform it back into the original type), but this version will still
be available (via the extension on `Sequence`) and will be called if forced
through type context. The only code that will break is if this operation spans
multple lines:

```swift
// filtered used to be [Character], now String
let filtered = "abcd".filter { $0 == "a" }
useArray(filtered) // won't compile
```

Because of this, the new implementation of `RangeReplaceableCollection.filter`
will only be available in Swift 4.

## Effect on ABI stability

This change will affect the ABI of `RangeReplaceableCollection` and needs to be made before
declaring ABI stability.

## Effect on API resilience

N/A

## Alternatives considered

Status-quo. There are benefits to the consistency of always returning `[Element]`.
The version on `Sequence` can be reached via type context (`"abc".filter(predicate) as [Element]`).

It could be worthwhile to make a similar change to `map`, but this is beyond
the capabilities of the current generics system because `map` does not preserve
the element type (more specifically, you cannot express a type that is `Self`
except with a different `Element` in order to provide the 
implementation on `RangeReplaceableCollection`).

## History

This proposal originally included a new associated type `Filtered` on `Sequence`. However, this
was unimplementable due to requiring a recursive type constraint (`Filtered: Sequence`). While
these were supported in later Swift versions, the additional associated type was not implemented
and that portion of the proposal has [expired](https://forums.swift.org/t/addressing-unimplemented-evolution-proposals/).
````

</details>

<details><summary><b>Step 4 — final</b> (566 words)</summary>

````text
# Change `RangeReplaceableCollection.filter` to return `Self`

## Introduction

This proposal implements the `filter` operation on `RangeReplaceableCollection`
to return the same type as the filtered collection.

## Motivation

The recently accepted
[SE-165](https://github.com/swiftlang/swift-evolution/blob/master/proposals/0165-dict.md)
introduced a version of `filter` on `Dictionary` that returned a
`Dictionary`. This had both performance and usability benefits: in most cases,
a `Dictionary` is what the user wanted from the filter, and creating one
directly from the filter operation is much more efficient than first creating
an array then creating a `Dictionary` from it.

However, this does result in some inconsistencies. Users may be surprised that
this one specific collection returns `Self`, while other collections that would
benefit from the same change still return `[Element]`. And some collections,
such as `String`, might also benefit from usability and performance win similar
to `Dictionary`. Additionally, these wins will be lost in generic code – if you
pass a `Dictionary` into an algorithm that takes a `Sequence`, then when you
filter it, you will still get an `Array`.

## Proposed solution

An implementation of `filter` on `RangeReplaceableCollection` will be provided,
using `init()` and `append(_:)`, so all range-replaceable collections will
have a `filter` method returning of `Self`. Per [SE-163](https://github.com/swiftlang/swift-evolution/blob/master/proposals/0163-string-revision-1.md),
this will include `String`.

Note, many sequences (for example, strides or ranges), cannot represent a
filtered `self` as `Self` and will continue to return an array. If this is a
performance problem, `lazy` remains a good solution.

## Detailed design

Add a default implementation of `filter` to `RangeReplaceableCollection`
returning `Self`:

```swift
extension RangeReplaceableCollection {
    func filter(_ isIncluded: (Iterator.Element) throws -> Bool) rethrows -> Self {
        var result = Self()
        for element in self {
            if try isIncluded(element) {
                result.append(element)
            }
        }
        return result
    }
}
```

Specific concrete collections may choose to implement a faster version, but
this is an implementation detail.

## Source compatibility

This change is subtly source breaking. In most cases users will not notice.
They may be be relying on an array being returned (albeit often in order to
then transform it back into the original type), but this version will still
be available (via the extension on `Sequence`) and will be called if forced
through type context. The only code that will break is if this operation spans
multiple lines:

```swift
// filtered used to be [Character], now String
let filtered = "abcd".filter { $0 == "a" }
useArray(filtered) // won't compile
```

Because of this, the new implementation of `RangeReplaceableCollection.filter`
will only be available in Swift 4.

## Effect on ABI stability

This change will affect the ABI of `RangeReplaceableCollection` and needs to be made before
declaring ABI stability.

## Effect on API resilience

N/A

## Alternatives considered

Status-quo. There are benefits to the consistency of always returning `[Element]`.
The version on `Sequence` can be reached via type context (`"abc".filter(predicate) as [Element]`).

It could be worthwhile to make a similar change to `map`, but this is beyond
the capabilities of the current generics system because `map` does not preserve
the element type (more specifically, you cannot express a type that is `Self`
except with a different `Element` in order to provide the 
implementation on `RangeReplaceableCollection`).

## History

This proposal originally included a new associated type `Filtered` on `Sequence`. However, this
was unimplementable due to requiring a recursive type constraint (`Filtered: Sequence`). While
these were supported in later Swift versions, the additional associated type was not implemented
and that portion of the proposal has [expired](https://forums.swift.org/t/addressing-unimplemented-evolution-proposals/).
````

</details>
